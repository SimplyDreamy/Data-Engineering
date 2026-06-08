-----------
    Goal
-----------
figuring out what to learn
And decided that learning automation was not a bad idea as this project is too simple

I did learn about the star scheme, but I didn't plan a project around it
A star scheme is a hybrid approach of both normalized & denormalized data models

from what I can understand,
normalized has a lot of categories/dimensions so it could have relationships resembling a mindmap
- con is that you need to join these together, which is less optimal
  and analysts are more likely to make errors (and not know)
denormalized is way more simplified as it has fewer dimensions, but more repeated data

star scheme is popular as it balances the two, which makes analysis easier
it works by having a fact storing IDs(/keys), which points to other dimensions (normalized)
And the dimensions will elaborate on these keys (denormalized)
---------------------------
    technical yapping
---------------------------
I had use requests, pandas, and logging as:
requests allows me to interact with http to get info off the web
pandas is a popular library and its commonly used for cleaning data
logging is a better debugging tool than the classic print(), as you can sort the type of messages

The tool I decided to use for automation is GitHub because:
- I already had a GitHub account (So familiarity bias)
- You don't have to set up a server yourself, so it's manageable for a 1-day project
- Lower learning curve


-------------------------------
    Roadblocks & Debugging
-------------------------------
a huge chunk of my day was setting things up as I was on a new pc, so I wasn't able to focus as much on the project.

For example, I spent 30 minutes installing python off the official site.
But for some mysterious reason, 'python' wasn't recognized despite having it in my PATHS.
Then I found out it was supposed to be in systems, not user