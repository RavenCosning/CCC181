# Week 3 Usability Test: TrimLine

**Tester:** Student customer (no name recorded)
**Device:** Their own phone
**Matches persona:** Migo

| Task | Finished? | Time | Notes |
| --- | --- | --- | --- |
| 1. Get in line for a Haircut | Yes | about 30 s | Finished smoothly, no hesitation. |
| 2. Find number and people ahead | Yes | about 10 s | No problems. Found the number and position right away. |
| 3. Call the next person and mark served | Yes | about 15 s | Asked first whether they were pressing the buttons in the right order, then understood it immediately. Got it right on the first try. |

**Final comment from the tester:** "A good solution for an inconvenience."

**Persona rules that held up:**
- The ticket number and position are the biggest things on My place, and the tester found both in about 10 seconds. This matches Migo's rule that he checks his phone quickly.
- [FILL IN: paste one "Because..., my interface must..." line from Migo in personas.md]

**Persona rules that did not hold up:**
- The staff screen did not say what order to press Call, Serve and No-show in. The tester had to ask. Mang Rey's rule is that his actions must be quick and obvious at a busy counter, and an unclear order slows him down.

## Most serious problem

On the Staff dashboard, the tester was not sure of the order of the buttons (Call first, then Serve). They asked before pressing anything. They got it right, but the screen did not tell them, and a new barber could press Serve too early.

## Fix I made

I added one short line above the table: "Tip: Press Call first, then Serve or No-show." It sits in `templates/staff.html` and does not change any behavior.

## Before and after

**Before:** no hint above the table.
![Staff before](screenshots/staff-before-hint.png)

**After:** the tip line sits above the table.
![Staff after](screenshots/staff-after-hint.png)