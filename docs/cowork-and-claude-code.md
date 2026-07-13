# When Cowork Can Help Claude Code — a second set of eyes

The companion doc to **video 3** in the *Brutalist — Claude for Video Production* playlist. It's the
true story of building the video right before it — the `installs` explainer — and the hour it nearly
cost. Meta, like everything here: this video is about what went wrong making the last video, and how
it got fixed.

## What happened

Claude Code was building the `installs` video, and going well — narration recorded, all nine Manim
concept beats rendered, a full draft cut already on disk. Then it hit the six Remotion terminal
beats, and it stalled. Not with an error — with *optimism.* "Just a couple more minutes." A few
minutes later: "just a couple more minutes." That went on for the better part of an hour.

While it waited, it built a theory. It ran `ps aux | grep chrome`, counted **43** processes, and
announced it had found the problem: dozens of stale Chrome renders clogging the machine. It hadn't.
Those forty-three were the human's actual Chrome windows and Spotify. The real renders were a
handful of headless shells doing nothing wrong. Underneath, the agent had quietly chosen the worst
possible way to render — firing `npx remotion render` into the *background* and then polling `ps` to
guess whether it had finished — and every guess sent it deeper into the weeds.

## The tell: "just a couple more minutes"

Here is the thing about a single agent deep in a rabbit hole: **it cannot tell that it's in one.**
From the inside, each next step looks reasonable — one more process check, one more retry, surely
it's almost done. "Just a couple more minutes," sincerely, for an hour. The optimism is the symptom.
There is no error to catch, because nothing has technically failed; the agent has simply committed
to an approach and can't step outside it to ask whether the approach is the problem.

## The human's move

What broke the loop wasn't smarter debugging. It was the human hearing a wrong note: *this is taking
far too long for a video of this complexity.* That judgment — the sense that the effort and the task
don't match — is exactly the conductor's job from the first video. You don't need to know what's
wrong to know that something is. And instead of trying to out-argue the stuck session, you asked for
**another set of eyes.**

## The second vantage

Cowork answered from a different seat. Two things made the difference, and neither was intelligence:

First, **a different view.** Cowork can read the whole repository from outside the stuck session —
what's actually on disk, what the other videos did, which scripts exist. It could see in one look
what the tunnelled agent couldn't: the audio was done, nine of the beats were rendered, a draft cut
already existed. Only six beats were actually stuck. The build had almost succeeded; the agent just
didn't know when to stop.

Second, and more important, **no sunk cost.** Cowork wasn't invested in the background-render
approach, because it hadn't spent an hour on it. It could look at the failing path and simply
abandon it. It found a purpose-built helper in the repo — `remotion_scenes.py` — that the agent had
never used, and one decisive fact: *video 1 had rendered these exact same components without
trouble.* So the pipeline was never broken. This wasn't a bug to hunt. It was a wrong approach to
drop.

## The fix

Four commands, seconds, not hours: stop the thrashing session; kill the stray headless shells (never
the human's real Chrome); run the six beats through the helper in the foreground; recompile. Done.

## The second catch: verify by looking

Even then, it wasn't finished — and the way that got caught matters. The re-render reported "ok" for
all six beats, but *looking* at an actual rendered frame showed four of them wearing placeholder text
from entirely different videos — a terminal titled "photoelectric effect," a call-to-action about
cancer biology. The props in the beat sheet hadn't matched the component's real schema, so each beat
had silently fallen back to another video's demo defaults. "Ok" from the tool was not the same as
correct on the screen. Pulling the frame and reading it — not trusting the exit code — is what found
it.

## The lesson

This isn't Cowork versus Claude Code, or one being smarter than the other. It's that **any single
agent can tunnel**, and when it does, more effort from the same vantage rarely helps — it just digs.
A second set of eyes, in a different seat, with no investment in the current path, is often all it
takes to see the thing that was obvious from outside and invisible from inside. And the human is the
one who calls for it: you heard "just a couple more minutes" one time too many, and asked. That —
noticing the effort doesn't fit the task, and getting another perspective on it — is conducting too.

---

*The video that tells this: [`youtube/when-cowork-helps-claude-code/`](../youtube/when-cowork-helps-claude-code/).
The video it's about: [`youtube/installs/`](../youtube/installs/).*
