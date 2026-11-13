# tiny chess engine — make.fun bounty tiny-chess-01

A 4 KB Python chess engine (0x88 board, negamax + alpha-beta, quiescence,
transposition table, killer moves, null-move pruning, late-move reductions,
fixed 60,000-node budget, CPW piece-square tables). Deterministic: no clock,
no randomness.

Run: `MAKEFUN_ENV_URL=<env url> python3 main.py` — it plays the game in
play via POST /game and POST /move until the env reports status "done".

The engine section of main.py is lzma+base85 compressed (allowed by the
bounty brief); the protocol (POST /game, POST /move) is in clear text at the
top of main.py.
