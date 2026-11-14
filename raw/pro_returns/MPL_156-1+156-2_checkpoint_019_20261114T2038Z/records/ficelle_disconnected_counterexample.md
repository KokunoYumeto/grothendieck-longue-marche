# Own-analysis check: a disconnected compact ficelle

**Status:** independently verified counterexample to the unrestricted necessity claim as written in the frozen text; **confidence: high**, because every stated axiom has an explicit elementary quotient model. Reconstructed after the environment loss and checked against the restored frozen page files; no manuscript reading is changed.

**Source anchors:** 156-2/002:9–21 (regular immersion), 003:41–43 and 004:5–14 (ficelle), 004:23–31 (c'), 004:44–56 (reduction), 011:6 (existence claim), and 011:16 (suggested connected endpoints); numbers after colons are lines of the individual frozen LaTeX source files.

## Claim and example

Scan 011 says, “Pour qu'un espace compact triangulable admette une structure de ficelle, il f. et s. qu'il soit connexe, et non réduit à un point.” Define

\[
X=[0,1]\times\{-1,+1\},\qquad A=\{0\}\times\{-1,+1\},\qquad B=\{1\}\times\{-1,+1\},
\]

with the second factor discrete. X is two disjoint compact intervals and hence a disconnected compact finite polyhedron; A and B are its paired left and right endpoints.

| Written axiom | Explicit verification |
|---|---|
| Fic a: closed, nonopen ends | A and B are nonempty finite closed subsets; neither is open because interval endpoints are not isolated. |
| Fic b: disjoint ends | Their first coordinates are respectively 0 and 1. |
| Fic c: both punctured endpoint quotients connected | Both quotients are homeomorphic to (-1,1), by the maps below. |
| Fic d: regular immersion | X/A and X/B are each [-1,1], with the contracted endpoint set at its conic midpoint. |
| Optional c' formulation | U=(0,1)×{-1,+1} has two components, each of whose closure meets both A and B. |

The maps q_A(t,ε)=εt and q_B(t,ε)=ε(1−t) identify exactly A and exactly B respectively, giving homeomorphisms X/A≅[-1,1] and X/B≅[-1,1]; the induced continuous bijections are homeomorphisms because the domain quotients are compact and the target is Hausdorff. Restriction to the corresponding saturated open subsets gives

\[
(X\setminus B)/A\cong(-1,1),\qquad (X\setminus A)/B\cong(-1,1).
\]

For regular immersion choose 0<r<1: V=[-r,r] is a closed neighborhood of the contracted point 0, the cone on the compact base K={-r,r}, and V minus K=(-r,r) is open in either quotient. The definition permits a disconnected compact cone base and does not require A, B, or X to be connected, so no written hypothesis excludes this example.

## Scope and repair

The example refutes only the assertion that connectedness is necessary for an unrestricted, possibly nonreduced ficelle. It does not refute the separate reduced variant, and it does not establish the reduced existence or uniqueness assertions. Contracting both A and B turns this X into two arcs with the same endpoints, hence a circle with two marked points: the reduced ficelle is connected, consistently with “Ficelle réduite est connexe” at 004:56.

Requiring **both** endpoints connected repairs the necessity of connectedness. If a quotient Y/K by a connected nonempty subset is connected, then Y is connected: a clopen separation of Y would place K wholly in one member and descend to a clopen separation of the quotient. Under connected A and B, Fic c therefore makes X minus A and X minus B connected; their intersection U is nonempty, since otherwise A and B would be complementary open sets, contrary to Fic a, and their union is X. Thus X is connected.

This is only a repair of necessity; it does not prove sufficiency for every compact triangulable connected nonpoint and does not revive the separate endpoint-enlargement assertion retracted on scan 011. The connected-end condition is merely proposed as “raisonnable” on that scan and must not be inserted retrospectively into the definition.

## Four-sentence note suitable for the research register

**Source:** 156-2/011:6, with 004:5–14. **Kind:** own idea / counterexample. **Confidence:** high; each axiom has an explicit interval quotient model.

The assertion “il f. et s. qu'il soit connexe” fails for nonreduced ficelles as written: let X be two disjoint compact intervals, A their two left endpoints, and B their two right endpoints. Both punctured endpoint quotients are (-1,1), and X/A and X/B are [-1,1] with the contracted subset at the conic midpoint, so Fic a–d and even c' hold although X is disconnected. This does not refute the reduced variant, and requiring both endpoints connected repairs the necessary connectedness condition, consistently with the separate suggestion at 011:16. The example is the analyst's, not one attributed to the manuscript.

**Context:** search: ficelle|connected|endpoint|quotient; no direct corresponding result in RESULTS_STATE; README and **WG2 B15 (§1.2)** are unchecked planning hypotheses, with no earlier scan supplied for this point; this adds a counterexample to using connectedness of the uncontracted ambient space as a classifier of these decorated objects.
