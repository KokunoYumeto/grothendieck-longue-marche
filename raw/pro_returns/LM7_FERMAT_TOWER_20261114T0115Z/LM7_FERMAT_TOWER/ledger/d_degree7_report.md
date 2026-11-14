# D.31: a compatible degree-seven replacement

D.31 proves an actual quotient automorphism for the fixed extra CM pair and its retained homology data. The full profinite realization of this pair remains unresolved.

## Exact quotient and computation

Let T2=B/D8(K), with the free rank-four relative kernel K of D.30. The image U of gamma3N is elementary abelian of dimension 1860. Its degree-six quotient has dimension 240 and its degree-seven subgroup dimension 1620. It is an actual Q-module: the inhomogeneous degree-six to degree-seven extension is retained, and conjugation by N is trivial. The calculation uses the actual elliptic conjugate paths when computing the separate central C1 corrections.

The cusp correction map on U has rank 1810 and cokernel dimension 50. The simultaneous 50 conditions and 15 class-two Z/4 conditions have rank 65 on the 4769-dimensional relation space. A solved seed has multiplier 1 and retains the rank-97 homology action. Its complete 4,903,248-letter cusp word evaluates to the identity in both the rank-97 class-two Z/4 Magnus model and the rank-four mod-two Magnus model through degree seven.

The exact orders are:

- T2: 576 times 2^3333.
- Common quotient C**=B/(gamma3N D8(K)): 576 times 2^1473.
- H^(2) times_C** T2: 576 times 2^11463.

The common quotient is proved by the product of the two actual normal kernels. The exponent relations [N,N]^4 and N^8 lie in D16(K), so their images in T2 vanish.

## Infinite extension and precise comparison

The seed extends to P2/(closure(gamma3N) intersect D8(K)), identified with the fibre product of the class-two pro2 completion and T2 over C**. The later stable corrections of D.29 start in D8(K). The cusp has order 48 in T2, and later multiplier increments are divisible by 144. Thus the finite action and conjugators remain fixed throughout the iteration. The resulting kernel over Q has class exactly three, third lower-central subgroup C2^1860, and trivial fourth subgroup.

The canonical map to D.30's target has kernel C2^1620. The new action descends through this map, but the descended action replaces D.30's recorded central representative. The second program proves that the symmetric matrix Z+Ms Z Ms^T is nonzero; it is the exact difference on the image of s in H^(1). The original and replacement certificates remain separate. The fixed G6 homology and CM data agree.

Every odd relative pro-prime completion and D.28's mixed quotient can be included through the previously proved exact common quotient H times_Q G3. Odd-primary conjugators are separately selected components; no statement identifies their abelianizations with that of the displayed discrete two-primary word. The compatible finite shadows are nonarithmetical on characteristic refinements retaining the G6 and CM data.

## Files and independent verification

- Section: sections/D_degree7.tex.
- Main certificate: code/d_cm_rank4_degree7.py, .out, .json.
- Explicit reduction comparison: code/d_cm_degree7_reduction.py, .out, .json.
- Statement ledger: ledger/d_degree7_results.json.

Root independently reran both complete programs with successful output. Agent A independently audited the entire theorem and programs, including generation of U, its inhomogeneous Q action, the joint correction equations, exact common quotient, stability of the inverse limit, and the explicit difference from D.30's recorded action. No genuine full profinite lift is inferred from these quotient automorphisms.

## Subsequent complete test in D.32

D.32 proves that the recorded T2 action has no peripheral lift to the full relative pro2 group. The degree-eight central map, every lower centralizer freedom, and the multiplier are exhausted. The quotient automorphisms of D.31 remain valid. This rejection does not exclude D.30's distinct central representative or every action with the same CM pair.
