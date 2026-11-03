# TrimLine schema self-review

**Works well:** The `tickets.service_id` foreign key with `RESTRICT` (question 5, deletes) protects the shop's history — a barber can never accidentally delete a service that has past tickets, which matters for the no-show reports in FR-08.

**Problem:** Checking coverage (question 1) against FR-01 and the Join flow, nothing in the schema stops a customer from ending up with two `waiting` tickets for the same service at once, for example from a double form submit. There's no database constraint for this.
**Change:** Kept the schema as is — a DB-level constraint here would block a customer from legitimately queuing for two *different* services at once, which is allowed. Instead, this gets handled at the Flask layer in Part 7/10 (check for an existing waiting ticket before creating a new one).

**Problem:** Checking bad-data scenarios (question 4), `users.role` (visitor/staff) and the `barbers` table are unrelated — a staff user who logs into the dashboard and a "barber" a customer can request are two separate concepts with no link between them.
**Change:** Kept as is and documented here. Staff login/authentication is out of scope until Week 11 per the activity instructions, so `users.role` is just a placeholder for now. `barbers` only drives the ticket's preferred-barber field (FR-06), not who's logged in.