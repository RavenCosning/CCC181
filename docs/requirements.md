# TrimLine requirements

**Setting:** A walk-in barbershop with several barbers (4 at Mang Rey's shop)
**People who wait:** Customers like Migo — [personas.md](week3/personas.md)
**People who serve:** Barbers like Mang Rey — [personas.md](week3/personas.md)

**Problem statement:** Migo needs a way to know his place in line without sitting and guarding his spot, because stepping away means someone else takes his turn.

## Functional requirements

| ID | Requirement | Priority | Stores data? | Status |
| --- | --- | --- | --- | --- |
| FR-01 | A customer can join the queue for a service by entering their name and email. | Must | Yes | Built (Week 3) |
| FR-02 | A customer can see their ticket number, status, and how many people are ahead of them. | Must | Yes | Built (Week 3) |
| FR-03 | A customer can leave the queue before being called. | Must | Yes | Built (Week 3) |
| FR-04 | A barber can call the next waiting ticket for a service. | Must | Yes | Built (Week 3) |
| FR-05 | A barber can mark a called ticket as served or no-show. | Must | Yes | Built (Week 3) |
| FR-06 ★ | A customer can request a specific barber when joining, if one is free. | Must | Yes | Later |
| FR-07 | A customer sees an estimated wait time for a service before joining. | Should | No | Later |
| FR-08 ★ | A barber can see how many customers were no-shows today, per barber. | Should | Yes | Later |
| FR-09 ★ | A barber can add, rename, or switch off a service. | Must | Yes | This week |
| FR-10 | A customer can switch the page to a larger text size. | Could | No | Later |

## Non-functional requirements

| ID | Requirement | Category | Priority |
| --- | --- | --- | --- |
| NFR-01 | No ticket is lost when the server or database restarts. | Reliability | Must |
| NFR-02 | Two people can never get the same ticket, even if they join at the same moment. | Data integrity | Must |
| NFR-03 | My place loads in under 2 seconds on mobile data. | Performance | Should |
| NFR-04 | Every screen scores 90 or higher in the Lighthouse accessibility check. | Accessibility | Must |
| NFR-05 | No password or secret key is stored in the repository. | Security | Must |

## MVP

FR-01 to FR-05, FR-09, and all Must-priority NFRs (NFR-01, NFR-02, NFR-04, NFR-05). This is the smallest version that lets a customer join and wait, and a barber run the shop, with data that survives a restart.

## Out of scope

- FR-06 (preferred barber) — needs barber accounts and availability tracking, too much for this semester.
- FR-10 (text size switch) — a nice-to-have with no persona asking for it directly.

## Feedback from a real person

| Who (role only, no full name) | What they said | What I changed |
| --- | --- | --- |
| Customer | "If possible can I queue for my favorite barber? I want to choose which barber I want." | Raised FR-06 (preferred barber) from Should to Must |
| Customer | Most important: knowing their ticket number. | No change — FR-02 already Must |