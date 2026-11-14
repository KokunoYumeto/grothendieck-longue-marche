# E.53 — the actual joint quotient of E50 and E54

The comparison starts with two based arithmetic maps from D=N/gamma4N: the multiplication-by-three elliptic quotient B of E50 and the h-induced quotient C of E54. The positive cusp valuation matrix has image exactly3Z3 x+Z3 y. Because h is surjective and N-prime lies in the peripheral kernel I, the image of I in C is the full preimage of that lattice, namely <x^3,y,c,d,e>.

The actual derived image is <c^3,d^3,e>. This follows from three literal group identities: [x^3,y]=c^3d^3, [x^3,c]=d^3, and [y,c]=e. The image is closed, normal and free abelian of rank3. Therefore the maximal common quotient is exactly C/<c^3,d^3,e>. Its coordinates are x^a y^b c^n d^r with a,b inZ3 and n,r modulo3.

Correcting a lift by the first kernel proves that D maps onto the actual fiber product B×_Q C. Its kernel is the intersection of the two actual kernels. Since E50's kernel is abelian Z3^332 and its image here is Z3^3, the intersection is the actual group Z3^329.

The integral graded calculation retains the factors three. The old degree-two kernel maps onto3Z3 c; the old degree-three kernel maps onto3Z3 d+Z3 e. Actual central commutators give every element of the latter image, so a degree-two kernel class can always be corrected integrally in degree three. This proves strict filtered exactness. The joint kernel has saturated graded ranks0,27,302, and the combined quotient has torsion-free ranks10,18,28.

The certificate supplies the actual peripheral matrix and a unimodular change to a cusp basis mapping to3x,y,0,...,0. A chosen handle basis then maps to x,0. The induced Hall maps are determinant formulas. On the old degree-three kernel their relative coordinates at3d,e have an explicit two-column integer right inverse. Subtracting these columns gives all302 integral kernel vectors; the degree-two calculation similarly gives27. Combining these with E50's retained rows gives integral quotient maps and right inverses of ranks18 and28. No rational-rank inference replaces these identities.

The common quotient has an additional explicit arithmetic comparison. Its x^3 is central, so the E54 based action depends on the path Kummer value k only modulo3. The genuine congruence k=(chi-1)/3 modulo3 therefore gives an actual cyclotomic action. At Frobenius4 the four generators map to x^4,y^4c,cd,d. The fiber product thus joins the elliptic comparison and the evaluated Frobenius quotient through their literal common action.

The executed program a_combined_quotient.py verifies all integer inverse identities,375 Hall tensor substitutions,270 kernel-normality identities,72 common-action checks, and the actual group commutator identities independently in the Magnus algebra. It imports the already executed a_class3_frobenius.py, which is part of the same deliverable. No new external source is required: E50 and E54 contain the verified geometric and arithmetic inputs.

This gives three further retained coordinates over B, of degrees two, three, three. The residual intrinsic kernel is stated explicitly, so the result does not identify the joint quotient with the full intrinsic class-three group.
