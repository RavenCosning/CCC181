# Week 3 Self-Review: TrimLine

## Join the queue

**Works well:** The form has three labeled fields and one large "Get a ticket" button, so Migo can join in a few seconds on his phone. This follows "match with the real world" because the words are the ones people use at the shop.
**Problem:** Nothing on the page tells Migo how long the wait will be, so he cannot decide whether to join now or later. This breaks "visibility of system status."
**Change:** I am keeping the screen as it is for Week 3. An estimated wait needs real data, so I will add it in Week 4 when tickets move into the database.

## My place

**Works well:** The ticket number is the largest element, and the status is a word badge ("Waiting"), not only a color. This follows "visibility of system status," and Migo can read it with a quick glance while walking.
**Problem:** The page refreshes every 10 seconds, so a customer could miss the moment they are called. This also breaks "visibility of system status."
**Change:** I am keeping 10 seconds for Week 3 because it meets the requirement. In a later week I will shorten the interval or add a notification.

## Staff dashboard

**Works well:** Call next sits at the top right, where Mang Rey reaches it first, and the waiting-per-service cards show the queue at a glance. This supports "recognition rather than recall."
**Problem:** Call, Serve and No-show sit side by side with the same size, so a rushed tap could hit No-show instead of Serve. This breaks "error prevention."
**Change:** I am keeping the layout because the buttons are colored differently (blue, green, red outline) and labeled with the ticket number for screen readers. I will add a confirm step for No-show in a later week.