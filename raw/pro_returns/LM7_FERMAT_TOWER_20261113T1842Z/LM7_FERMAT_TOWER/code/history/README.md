# Retained E106 exploratory work

The initial rank calculation and its actual stdout/JSON preceded
the full transformations and class maps. Its original workspace
path routing is retained literally.

The initial prime-wrapper source is retained. It ran the owned GP
calculation and printed the exit code and a truncated tail.
The arithmetic.out file is explicitly the complete actual GP
stream retained from the successful rebuild. The unchanged wrapper
was also freshly rerun in an isolated copy at the root audit's
request. Its complete actual stdout is e106_initial_prime_driver.out;
the new complete GP stream and exact replay record are beside it.
This replay is not represented as recovered original stdout.
The original freeze manifest, source, stdout and status are retained
under ledger/e106_original_author_freeze. The final portable driver
retains and checks the full GP stream directly.
