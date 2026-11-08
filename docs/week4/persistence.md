# TrimLine persistence proof

## Restart test

**Before restart:**

![Staff dashboard before restart](screenshots/before-restart-staff.png)

![Database query before restart](screenshots/before-restart-db.png)

Ran `docker compose down` (removed the container and network, kept the volume), then `docker compose up -d`, waited for healthy, then restarted Flask.

**After restart:**

![Staff dashboard after restart](screenshots/after-restart-staff.png)

![Database query after restart](screenshots/after-restart-db.png)

**Result: NFR-01 passes.** Every ticket, status and time matched exactly after the restart.

## Rebuild from scratch

Ran these commands to delete everything and rebuild the database from the migrations alone:

    docker compose down -v
    docker compose up -d
    flask --app app db upgrade
    flask --app app seed

`docker compose down -v` deleted the container and the data volume. `docker compose ps` then showed the new database as healthy. `flask db upgrade` ran both migrations (`Initial tables`, then `add barbers.active`) with no errors, and `flask seed` added the starting services. I then opened the join form, which listed Haircut, Haircut + shave and Shave, and joined the queue and reached My place.

**Result: the database rebuilds from scratch using only the migrations and the seed command.** No table or column was missing, and I did not use `db.create_all()`.