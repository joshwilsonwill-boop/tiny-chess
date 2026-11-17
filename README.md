# tiny-chess

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/joshwilsonwill-boop/tiny-chess/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/joshwilsonwill-boop/tiny-chess/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

<sub>Entered on [make.fun](https://make.fun/?ref=mc9159gw&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>

A chess engine in 4,096 bytes of Python. `main.py` is the whole engine:
0x88 board, alpha-beta search with quiescence, MVV-LVA move ordering,
material plus a pawn piece-square table, iterative deepening to a fixed
node budget.
Deterministic: no clock, no unseeded randomness, so replayed trials
play the same moves.

## A win from the practice gauntlet

Trial 0, game 1, vs the depth-2 house engine (Semi-Slav). The engine
played White and finished it with f7f8=Q#:

```
8 . . ♚ . . ♕ . .
7 . . . . ♕ . . .
6 . . ♟ . . . . .
5 . . . ♟ . . . .
4 ♟ . . . . . . .
3 ♙ . . . ♗ ♝ . .
2 . ♙ . . . . . .
1 ♖ . . . ♔ ♗ . .
  a b c d e f g h
```

## Run it

The engine talks to the make.fun env over HTTP. With the env running:

```sh
MAKEFUN_ENV_URL=http://127.0.0.1:8080 python3 -P -s main.py
```

It reads the brief from `MAKEFUN_PROMPT_FILE` and plays through
`POST /game`, `/move`, `/resign`. Standard library only, Python 3.13.
