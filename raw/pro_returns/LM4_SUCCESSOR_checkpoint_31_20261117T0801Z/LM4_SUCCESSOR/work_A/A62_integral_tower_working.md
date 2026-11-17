# Proposed unbounded integral cusp tower

This is a complete working proof for review, not an integrated statement. It concerns a specific noncofinal tower. It does not assert surjectivity onto arbitrary earlier new-frame choices.

## 1. Compatible actual coefficient quotients

Let O∞ be the unramified degree-three extension of Z2 and O_n=O∞/2^n. The actual H-module L∞=O∞^36 uses the same monomial permutations as V and the compatible Teichmüller seventh roots. Its reductions are L_n. The four integral cusp cocycles can be chosen over O∞: normalize their s-values to0; the r-norm kernel is a free rank24 summand, the s-fixed coboundaries form a free rank20 direct summand (a unit minor already exists modulo2), and the cusp restriction is an isomorphism between free rank4 modules. Fix a basis of this quotient over O∞ and actual representative cocycles d1,...,d4. Their reductions are compatible at every n.

Retain, separately, the four binary s-classes with zero cusp restriction. Define

    A_n=L_n^4 ⊕ V^4

and the actual source map Π→A_n⋊C using these eight cocycles. It is onto: its residual image in A_n reduces onto the complete eight-dimensional V-cocycle layer; finite2-group Nakayama then makes it all A_n. The transitions A_(n+1)→A_n reduce the free coordinates and keep the four binary coordinates unchanged. Thus the actual kernels W_n are nested. This point is necessary: binary s-cohomology need not lift under reduction of the coefficient L_(n+1) alone.

Each initial-base coefficient and its dual are acyclic on C by the actual normal pro-odd subgroup. A58 identifies the actual scalar-stable refinement D_n=Π/U_n, U_n=[W_n,Π]. Its residual class-two group P_n has abelianization A_n and center

    M_n = (O_n)^6 ⊕ k^30

in the weight/multiplicity notation, equivalently C_(2^n)^18⊕C2^90 as a finite abelian group. H acts trivially on this center. The diagonal terms remain order2; only the six free/free off-diagonal terms grow with n.

The source-compatible quotient maps D_(n+1)→D_n follow either from U_(n+1)⊂U_n or from the explicit group laws. For the latter, use the compatible cocycles above, the same C4 carry at s, and the compatible central correction by−1/3 of the r-cube. The exterior-square maps reduce the free center and keep its binary part. These are the actual quotient transitions, not merely abstract groups of matching order.

## 2. A fixed full lift supplies compatible involutory actions

Choose one full positive lift h0 from A56, retaining the older C and A47–A52 data, with b0=h0c. Its action on the binary complete layer is the already prescribed A56 action. Every integral cusp class is fixed by h0, because h0 fixes tau literally and acts as identity on H; actual c acts as minus identity on the integral cusp cohomology. The proof of A60 works over every O_n without change: the coefficient intertwiner C is literally identity on the four integral tau-invariant and coinvariant lines, v=Cv, w=Cw, and the exact source formula gives d(b0²g)=d(g).

Consequently h0 and c preserve every W_n, and b0² is identity on the affine quotient A_n⋊C. The central character argument killing tau then proves b0²=1 on D_n. Since these are restrictions of the same full h0, their actions are compatible under all transition maps. On the six free center coordinates, b0 acts+1; the central norm there is multiplication by2.

This is an action assertion. The normalizers supplied by h0 need not yet have order2 on D_n.

## 3. The all-n s-centralizer lemma

The order-two element s has no opposite-weight pair that it exchanges. Indeed, the chosen weight lambda has stabilizer<s>, and beta0 sends lambda to−lambda. An equality s(q lambda)=−q lambda would imply

    q^-1 s q ∈ beta0<s>={beta0,beta0 s}.

In Q6=S3×A4, beta0 has trivial S3 component, so it cannot be conjugate to s. The element beta0 s has trivial A4 component, whereas the A4 component of s is a nontrivial double transposition, so it also cannot be conjugate to s. Odd translations change scalar phases but do not change weight permutations, so this excludes every such exchange.

Therefore one can orient all unordered opposite-weight pairs s-invariantly: choose an orientation on each orbit of pairs and transport it by s. A fixed pair has its two weights fixed separately, so presents no ambiguity. In this orientation the monomial lift of s to the class-two group has no orientation carry at all.

Now take a vector a in the doubled free cusp subgroup2L_n^4 that is s-fixed. The source s has zero free cusp coordinate; all mixed center products with its binary coordinate vanish because a reduces to0. Its monomial orientation carry is zero by the chosen orientation. Thus (a,0) centralizes the actual source s in P_n⋊C, for every n. This is an exact centralizer lift, not an inference from the n=2 quadratic terms alone. Changing the orientation merely changes the central coordinate convention and does not alter the existence assertion.

## 4. Separate involutory frames at each n

Start with the actual full s/r-conjugators of h0, whose D1 images are the A56 frames. On the affine quotient A_n⋊C, A60/A61's integral joint-invariant construction gives s- and r-frames whose normalizers are involutions and whose reductions modulo2 are these same affine frames. The argument works over O_n: the relevant monomial groups are quotients of C2×C2 and S3, and their stabilizers have order dividing4 or6, hence no nontrivial character into C7. Orbitwise rescaling gives permutation modules, so integral invariants reduce onto their mod2 invariants for every n.

For s, the difference from the full conjugator's affine image is an element of2L_n^4 centralizing s. Section3 lifts it to an actual centralizer, so one obtains the desired affine norm condition without losing the actual s-conjugacy equation on D_n. For r, every lift of an affine r-conjugator has the right conjugacy equation: the central discrepancy between two elements of order3 lies in a two-group and is therefore zero.

After choosing their central coordinates to reduce to the A56 frames, the two normalizer squares lie in the kernel M_n→M_1, namely2(O_n)^6. Their binary center coordinates vanish. Since b0 acts+1 on the free center, choose independent central halves and multiply the frames by them. This kills both squares and changes neither conjugacy equation. It may alter the newer central frame choices at smaller levels, but their normalizer squares remain1, since they are reductions of the new involutory normalizers. It changes none of the older C or A47–A52 frame projections.

## 5. Actual full realization and compact simultaneous compatibility

For each n and each finite union of the older retained families, the residual abelianization of P_n has only the108-dimensional simple type, whereas the older abelianizations have only6/21/42-dimensional types. Equivariant Goursat gives the actual fiber product over C, and the same type separation gives H1-vanishing for the new dual coefficient over the retained base. Conditional A58 then identifies the same actual center and proves scalar stability on this joint quotient. A3 realizes its selected compatible action and the two literal frames by a full positive lift.

Take closed solution sets in the compact product of the full positive group and the two full frame groups. The conditions are: the already prescribed older actions/frames; the fixed quotient action induced by h0 on D_n; literal cusp fixation; and order-two s/r-normalizers on D_n. A finite collection of these conditions is handled by the maximum n and the finite union of the older families, as just proved. Therefore the sets have the finite-intersection property and admit a simultaneous point.

This gives compatible involutory images and compatible literal frame normalizers on the actual inverse limit lim D_n, together with all older families. No assertion that every previously chosen new frame lifts is used; the failed fixed A56 tuple is consistent with this existential compactness argument.

The tower has only a class-two pro-two residual with the displayed finite-rank coefficient types over C, so it is not claimed cofinal. The full negative square and the original involution-conjugacy problem remain Open.
