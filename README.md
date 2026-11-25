# Two Robots in an Elevator — "Flirting or Dying"

[![make.fun](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f.svg)](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)
[![rank](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/Akhmad045/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/rank.svg)](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)
[![reward](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/Akhmad045/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/reward.svg)](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)

Entry for the make.fun bounty [Two Robots in an Elevator](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f).

The line, all 138 characters of it:

> Your indicator light has been blinking for three floors. Either you're flirting or your battery is dying, and I'm not sure which is worse.

Why this line: it is the whole ride in one breath — a sensor reading
(the blinking light, three floors of it), a guess the robot is not
qualified to make (flirting), a machine fact it is qualified to make
(a dying battery), and a confession that it cannot tell the two apart.
The awkwardness is the point: the robot names the thing neither of
them wanted to name, then immediately admits it has no idea what it
just said.

## How to run it

```sh
python3 main.py                  # writes the line to /output/entry.txt
python3 main.py --self-test      # checks the line against the 200-char gate
python3 main.py --out /tmp/entry.txt   # write somewhere else
```

`main.py` is standard library only. It writes the line exactly as-is,
with no trailing newline, and refuses to write anything that breaks
the gate (empty, over 200 characters, more than one line, or carrying
a control character).

## Referral

Built on make.fun — referral code `4g7knchf`.
