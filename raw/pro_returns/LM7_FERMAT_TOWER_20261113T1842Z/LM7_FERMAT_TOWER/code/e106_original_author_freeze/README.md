# Retained E106 exploratory work

The initial rank calculation and its actual stdout/JSON preceded
the full transformations and class maps. Its original workspace
path routing is retained literally.

The initial prime-wrapper source is retained. It ran the owned GP
calculation and printed the exit code and a truncated tail.
The arithmetic.out file is explicitly the complete actual GP
stream retained from the successful rebuild, rather than an
invented complete wrapper terminal transcript. The final portable
driver retains and checks the full GP stream directly.
