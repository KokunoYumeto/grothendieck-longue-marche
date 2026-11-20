# Scan 013 — limited mathematical work during reading

The main read the current C/H texts, C doubts/notes and S row SA21-K6-06. The supplied sweep event SA21-R6-08 describes the same proposed counterexample. No outside source was consulted, and no claim about a page beyond this task is adopted.

## Finite-order component of S's example

The script `scripts/check_scan013_order_example.py` explicitly defines the four objects empty, a, b, c, with empty below all, a and b below c, and reflexive pairs. Compatibility is reflexive and holds between empty and every object; a and b are incompatible. It exhaustively checks reflexivity, antisymmetry and transitivity, and enumerates the common bounds of a,b. The only common lower bound is empty and the only common upper bound is c. Thus their infimum is empty and their supremum exists, while compatibility fails. The exact result is saved in `working/scan013_order_example_check.json`.

This computation confirms only the finite-order component of the supplied example. It shows that these order facts by themselves do not force compatibility or disjointness. No check of At 1–At 10, the complete atelier construction, the claimed forward implication under those axioms, or the Atens 2 sufficient condition was performed. Those portions of S remain unverified in this run. The actual implication/equivalence signs, canceled states, empty-figure subscripts and marginal checking word must still be decided from the crops.

## Event to carry into the final record

Statement: scan013-S-SA21-K6-06-finite-order-component. Type: computation or formal certificate. Outcome: the enumerated order has inf(a,b)=empty, sup(a,b)=c, and a,b incompatible; restricted scope above. This is not a proof that the manuscript's intended atelier axioms admit the example.
