import os

from dotenv import load_dotenv
from flask import Flask, abort, flash, redirect, render_template, request, url_for
from flask_migrate import Migrate
from sqlalchemy import func
from sqlalchemy.exc import IntegrityError

from models import Barber, Service, Ticket, User, db

load_dotenv()

"""TrimLine: a walk-in queue for a barbershop.

Run it with:
    flask --app app run --debug
"""

app = Flask(__name__)
app.secret_key = "dev-only-change-me"

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DATABASE_URL"]
app.config["SQLALCHEMY_ECHO"] = os.environ.get("SQLALCHEMY_ECHO") == "1"

db.init_app(app)
migrate = Migrate(app, db)

STAFF_ACTIONS = {"call": "called", "serve": "served", "no-show": "no-show"}


def all_services():
    return db.session.scalars(db.select(Service).order_by(Service.name)).all()


def people_ahead(t):
    stmt = (db.select(func.count())
            .select_from(Ticket)
            .where(Ticket.service_id == t.service_id,
                   Ticket.status == "waiting",
                   Ticket.created_at < t.created_at))
    return db.session.scalar(stmt)


@app.route("/")
def index():
    return render_template("index.html")


@app.get("/join")
def join_form():
    return render_template("join.html", services=all_services(), form={}, errors={})


@app.post("/join")
def join():
    form = request.form
    name = form.get("name", "").strip()
    email = form.get("email", "").strip().lower()
    service_id = form.get("service_id", type=int)
    service = db.session.get(Service, service_id) if service_id else None

    errors = {}
    if not name or len(name) > 80:
        errors["name"] = "Enter your name (up to 80 characters)."
    if "@" not in email or len(email) > 120:
        errors["email"] = "Enter a valid email address."
    if service is None or not service.active:
        errors["service_id"] = "Choose a service."

    if errors:
        flash("Please fix the highlighted fields.", "danger")
        return render_template("join.html", services=all_services(),
                               form=form, errors=errors), 400

    user = db.session.scalar(db.select(User).filter_by(email=email))
    if user is None:
        user = User(name=name, email=email)
    ticket = Ticket(user=user, service=service)
    db.session.add(ticket)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        flash("Something went wrong saving your ticket. Please try again.", "danger")
        return render_template("join.html", services=all_services(),
                               form=form, errors={}), 409

    flash(f"You joined the queue. Your ticket is #{ticket.id}.", "success")
    return redirect(url_for("ticket", ticket_id=ticket.id))


@app.get("/queue/<int:ticket_id>")
def ticket(ticket_id):
    t = db.get_or_404(Ticket, ticket_id)
    return render_template("ticket.html", ticket=t, service=t.service,
                           ahead=people_ahead(t))


@app.get("/queue/<int:ticket_id>/status.json")
def ticket_status(ticket_id):
    t = db.get_or_404(Ticket, ticket_id)
    return {"status": t.status, "ahead": people_ahead(t)}


@app.post("/queue/<int:ticket_id>/leave")
def leave(ticket_id):
    t = db.get_or_404(Ticket, ticket_id)
    if t.status == "waiting":
        t.status = "left"
        db.session.commit()
    flash("You left the queue.", "info")
    return redirect(url_for("index"))


@app.get("/staff")
def staff_dashboard():
    service_id = request.args.get("service_id", type=int)
    stmt = (db.select(Ticket)
            .where(Ticket.status.in_(["waiting", "called"]))
            .order_by(Ticket.created_at))
    if service_id:
        stmt = stmt.where(Ticket.service_id == service_id)
    queue = db.session.scalars(stmt).all()
    return render_template("staff.html", queue=queue, services=all_services(),
                           selected=service_id)


@app.post("/staff/call-next")
def call_next():
    service_id = request.form.get("service_id", type=int)
    stmt = (db.select(Ticket)
            .where(Ticket.status == "waiting")
            .order_by(Ticket.created_at)
            .limit(1))
    if service_id:
        stmt = stmt.where(Ticket.service_id == service_id)
    nxt = db.session.scalar(stmt)
    if nxt is None:
        flash("Nobody is waiting.", "warning")
    else:
        nxt.status = "called"
        nxt.called_at = func.now()
        db.session.commit()
        flash(f"Ticket #{nxt.id} ({nxt.user.name}) called.", "info")
    return redirect(url_for("staff_dashboard", service_id=service_id))


@app.post("/staff/tickets/<int:ticket_id>/<action>")
def staff_action(ticket_id, action):
    new_status = STAFF_ACTIONS.get(action)
    if new_status is None:
        abort(404)
    t = db.get_or_404(Ticket, ticket_id)
    t.status = new_status
    if new_status == "called":
        t.called_at = func.now()
    db.session.commit()
    flash(f"Ticket #{ticket_id} marked {new_status}.", "info")
    return redirect(url_for("staff_dashboard"))


@app.post("/staff/tickets/<int:ticket_id>/delete")
def delete_ticket(ticket_id):
    t = db.get_or_404(Ticket, ticket_id)
    db.session.delete(t)
    db.session.commit()
    flash(f"Ticket #{ticket_id} was deleted.", "warning")
    return redirect(url_for("staff_dashboard"))

@app.get("/staff/services")
def services_list():
    services = all_services()
    return render_template("services.html", services=services)


@app.post("/staff/services")
def service_create():
    name = request.form.get("name", "").strip()
    minutes = request.form.get("avg_minutes", type=int)
    if not name or len(name) > 60 or not minutes or minutes <= 0:
        flash("Enter a name (up to 60 characters) and minutes greater than 0.", "danger")
        return redirect(url_for("services_list"))
    db.session.add(Service(name=name, avg_minutes=minutes))
    try:
        db.session.commit()
        flash(f"Service \u201c{name}\u201d added.", "success")
    except IntegrityError:
        db.session.rollback()
        flash(f"A service named \u201c{name}\u201d already exists.", "danger")
    return redirect(url_for("services_list"))


@app.post("/staff/services/<int:service_id>")
def service_edit(service_id):
    s = db.get_or_404(Service, service_id)
    name = request.form.get("name", "").strip()
    minutes = request.form.get("avg_minutes", type=int)
    if not name or len(name) > 60 or not minutes or minutes <= 0:
        flash("Enter a name (up to 60 characters) and minutes greater than 0.", "danger")
        return redirect(url_for("services_list"))
    s.name = name
    s.avg_minutes = minutes
    s.active = request.form.get("active") == "on"
    try:
        db.session.commit()
        flash(f"Service \u201c{name}\u201d updated.", "success")
    except IntegrityError:
        db.session.rollback()
        flash(f"A service named \u201c{name}\u201d already exists.", "danger")
    return redirect(url_for("services_list"))


@app.post("/staff/services/<int:service_id>/delete")
def service_delete(service_id):
    s = db.get_or_404(Service, service_id)
    if s.tickets:
        flash(f"\u201c{s.name}\u201d has tickets, so it cannot be deleted. Turn it off instead.", "danger")
        return redirect(url_for("services_list"))
    db.session.delete(s)
    db.session.commit()
    flash(f"Service \u201c{s.name}\u201d deleted.", "warning")
    return redirect(url_for("services_list"))


@app.cli.command("seed")
def seed():
    """Add the starting services if they are not there yet."""
    starting = [("Haircut", 15), ("Shave", 10), ("Haircut + shave", 25)]
    for name, minutes in starting:
        exists = db.session.scalar(db.select(Service).filter_by(name=name))
        if exists is None:
            db.session.add(Service(name=name, avg_minutes=minutes))
    db.session.commit()
    print("Services are ready.")


if __name__ == "__main__":
    app.run(debug=True)