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

(filled in below)