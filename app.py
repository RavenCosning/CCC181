"""TrimLine: a walk-in queue for a barbershop.

Run it with:
    flask --app app run --debug
"""
from flask import Flask, abort, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = "dev-only-change-me"  

SERVICES = [
    {"id": 1, "name": "Haircut"},
    {"id": 2, "name": "Shave"},
    {"id": 3, "name": "Haircut + shave"},
]


TICKETS = [
    {"number": 1, "name": "Ana", "email": "ana@example.com", "service_id": 1, "status": "waiting"},
    {"number": 2, "name": "Ben", "email": "ben@example.com", "service_id": 2, "status": "waiting"},
]


def find_ticket(ticket_id):
    return next((t for t in TICKETS if t["number"] == ticket_id), None)


def people_ahead(t):
    return sum(1 for x in TICKETS
               if x["service_id"] == t["service_id"]
               and x["status"] == "waiting"
               and x["number"] < t["number"])


@app.route("/")
def index():
    return render_template("index.html")


@app.get("/join")
def join_form():
    return render_template("join.html", services=SERVICES, form={}, errors={})


@app.post("/join")
def join():
    form = request.form
    name = form.get("name", "").strip()
    email = form.get("email", "").strip().lower()
    service_id = form.get("service_id", type=int)

    errors = {}
    if not name:
        errors["name"] = "Enter your name."
    if "@" not in email:
        errors["email"] = "Enter a valid email address."
    if service_id not in [s["id"] for s in SERVICES]:
        errors["service_id"] = "Choose a service."

    if errors:
        flash("Please fix the highlighted fields.", "danger")
        return render_template("join.html", services=SERVICES, form=form, errors=errors), 400

    number = TICKETS[-1]["number"] + 1 if TICKETS else 1
    TICKETS.append({"number": number, "name": name, "email": email,
                    "service_id": service_id, "status": "waiting"})
    flash(f"You joined the queue. Your ticket is #{number}.", "success")
    return redirect(url_for("ticket", ticket_id=number))


@app.get("/queue/<int:ticket_id>")
def ticket(ticket_id):
    t = find_ticket(ticket_id)
    if t is None:
        abort(404)
    service = next(s for s in SERVICES if s["id"] == t["service_id"])
    return render_template("ticket.html", ticket=t, service=service, ahead=people_ahead(t))


@app.post("/queue/<int:ticket_id>/leave")
def leave(ticket_id):
    t = find_ticket(ticket_id)
    if t is None:
        abort(404)
    t["status"] = "no-show"
    flash("You left the queue.", "info")
    return redirect(url_for("index"))


@app.get("/queue/<int:ticket_id>/status.json")
def ticket_status(ticket_id):
    t = find_ticket(ticket_id)
    if t is None:
        abort(404)
    return {"status": t["status"], "ahead": people_ahead(t)}


@app.get("/staff")
def staff_dashboard():
    service_id = request.args.get("service_id", type=int)
    queue = [t for t in TICKETS if t["status"] in ("waiting", "called")]
    if service_id:
        queue = [t for t in queue if t["service_id"] == service_id]
    names = {s["id"]: s["name"] for s in SERVICES}
    # Star feature: how many people are waiting per service
    waiting_counts = {s["id"]: sum(1 for t in TICKETS
                                   if t["service_id"] == s["id"] and t["status"] == "waiting")
                      for s in SERVICES}
    return render_template("staff.html", queue=queue, services=SERVICES, names=names,
                           selected=service_id, waiting_counts=waiting_counts)


@app.post("/staff/call-next")
def call_next():
    service_id = request.form.get("service_id", type=int)
    waiting = [t for t in TICKETS if t["status"] == "waiting"
               and (not service_id or t["service_id"] == service_id)]
    if not waiting:
        flash("Nobody is waiting.", "warning")
    else:
        nxt = min(waiting, key=lambda t: t["number"])
        nxt["status"] = "called"
        flash(f"Ticket #{nxt['number']} ({nxt['name']}) called.", "info")
    return redirect(url_for("staff_dashboard", service_id=service_id))


@app.post("/staff/tickets/<int:ticket_id>/<action>")
def staff_action(ticket_id, action):
    new_status = {"call": "called", "serve": "served", "no-show": "no-show"}.get(action)
    t = find_ticket(ticket_id)
    if t is None or new_status is None:
        abort(404)
    t["status"] = new_status
    flash(f"Ticket #{ticket_id} marked {new_status}.", "info")
    return redirect(url_for("staff_dashboard"))


if __name__ == "__main__":
    app.run(debug=True)