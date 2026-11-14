### Independent root audit of D.32

We read the complete degree-eight proof and the seed, linear, Magnus,
centralizer, and Sylow programs. We copied their dependencies to a separate
scratch directory and reran the seed, the complete corrected centralizer
calculation, and the Sylow graph calculation. The seed took 26.997 seconds
and the centralizer run took 48.261 seconds. All certificate fields agree
exactly with the integrated certificates after removing elapsed-time fields.

The fresh calculation retains the 4,903,248-letter cusp word and its
904,756-letter Schreier collapse. Its lower coefficients vanish and its
degree-eight error has 32,296 nonzero coefficients. The multiplier column
has 6,561 nonzero coefficients. The successive complete centralizers have
base-two logarithmic orders 6, 16, 50, 152, 494, and 1666. Their construction
uses ordered independent coordinates in the actual finite groups. Descending
elimination preserves a full generating sequence for each connecting-map
kernel; it does not replace that kernel by a vector-space approximation.

The corrected separating functional annihilates every row in the final
rank-7777 image and all 1666 saved centralizer defects, and evaluates to one
on the actual target. Its construction now chooses the highest remaining
nonpivot coordinate before dual elimination. The final assertion was
verified by the fresh run.

We checked the comparison needed to exhaust the conjugators: D8(K) lies in
Phi(N), the lower quotient therefore retains G2, and an s-conjugator can be
normalized into F before the projected-centralizer calculation places its
lower difference in N/D8(K). The coprime order-three complement argument
accounts for the other torsion conjugator. The cusp order 48 to 96 includes
every multiplier contribution at this step.

We also inspected the original Herfort--Ribes page images, especially
section 2 on printed page 156 and Theorem B-prime with its proof on page
159. The allowed class of finite groups includes the finite two-groups.
Together with Theorem A-prime, the nine-edge Bass--Serre graph and the full
induced topology prove the stated Sylow free pro-two product. An element
centralizing s normalizes the entire preimage of its order-two subgroup;
the normalizer quotient rotates the three involution classes. This gives
the full relative centralizer and the required torsion-conjugacy transfer.

The proved exclusion concerns the recorded D.31 lower action. It does not
exclude every action with the same CM pair, and it does not assert that
D.30's earlier, explicitly different central representative is its image.
The exact map and this scope agree with the integrated statement.
