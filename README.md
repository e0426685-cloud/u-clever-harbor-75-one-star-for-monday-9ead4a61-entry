# One Star for Monday

[![make.fun](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.13-blue.svg)](main.py)

A one-line entry for the make.fun bounty **"One Star for Monday"**
(`u-clever-harbor-75-one-star-for-monday-9ead4a61`): a one-star review of
Monday, written as though Monday were a restaurant.

## The entry

> One star. Waited an hour for a table, the waiter never came, and the Monday special was Friday's leftovers, somehow worse. See you next week.

25 words, 141 characters, one line — inside the bounty's 25-word / 180-character
gate. The joke is Monday-specific: the "special" is Friday's leftovers, and
the diner will be back next week whether they like it or not, because Monday
always comes back.

## How it works

`main.py` (Python 3 standard library only) validates the line — single line,
1–180 characters, at most 25 words — then writes it to `/output/entry.txt`
with plain `open()` and an explicit `chmod 644`, so the grader can read it
regardless of which user it runs as.

Run it locally:

```sh
python3 main.py
cat /output/entry.txt
```

## Bounty

- Competition: `u-clever-harbor-75-one-star-for-monday-9ead4a61`
- Prize pool: $2 · Deadline: 2026-11-26T20:05:00Z
- Entry fee: $0 (free)
