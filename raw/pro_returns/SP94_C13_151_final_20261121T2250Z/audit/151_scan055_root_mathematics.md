# Targeted checks for scan 055

These checks use the locally finite closed cover on scan045, covering and common-lower-piece condition (21) on scan052, and the finite-filter argument on scan054. They do not change any literal formula on scan055.

For a point x, let m=i(x) be the least index of a piece containing it. If x belongs to X_i^*, then m is at most i. If m were strictly smaller, x would lie in the boundary union of X_i; hence m=i. Conversely, minimality of m excludes every strictly smaller containing index, so x belongs to X_m^*. Thus x belongs to X_i^* exactly when i=i(x). This proves both the pairwise disjointness and the covering assertion in the proposition.

For the NB reduction let I' consist of indices with nonempty X_i^*. Every x is in X_{i(x)} and i(x) is in I', so the retained closed pieces still cover X. Local finiteness and inclusion compatibility pass to a subfamily. If x belongs to X_i intersect X_j for retained i,j, its least index m is retained and is at most both i and j. Consequently the common-lower-piece condition also passes to I'. For retained i, the new lower union equals the old one: a point in any removed lower piece X_j, j<i, belongs to X_m with retained m at most j<i. The open pieces therefore remain unchanged by this reduction.

This also explains why the literal two formulas in the proof are treated as slips, not repaired: the ink reads X_j backslash X_i^* in the first contradiction and x in X_i backslash X_k in the second, whereas the least-index argument above proves the intended proposition without those erroneous expressions.
