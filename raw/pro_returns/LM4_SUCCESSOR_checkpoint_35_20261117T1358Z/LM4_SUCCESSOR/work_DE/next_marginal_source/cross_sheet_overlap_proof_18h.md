# Exact one-step cross-sheet direct sum

Status: proved by the stated exact certificate and B94's separated
augmentation argument; complete independent CE reconstruction and proof
review PASS. This remains a fully proved research addition for
checkpoint18, without a new formal statement row this cycle.

Use the actual operator A=alpha_b^{-1}, the geometric pullback around
the old q=1 lasso, in the same paired marking as B94/B96. Let

    L = L_ret,  L_minus = A(L_ret).

The producer `check_odd_G_overlap.py` reconstructs all64 original node
commutators and their64 literal A-images in F21. For every one it
constructs the full product-tree two-chain, checks its complete edge
boundary against the actual word, and checks the literal negative-swap
F-image. Thus no identity is inferred from a rank or augmentation test.

Every column is then normalized to the unique G=(R x R) semidirect F5
coefficient-row basis of B94. After E-augmentation, each has one signed
retained group unit in one row. There are no row coincidences between
the two layers. Within each layer the64 physical ordered slot pairs
are distinct. Across the two layers, the same physical pair has
different relative retained word. In fact the y1 exponent parity
changes for every physical pair, while the other four parities do not.

Consequently the selected128x128 augmentation matrix is diagonal with
units. The exact same ordered coefficient induction as B94 applies:
a relation first has all coefficients in a=I_E Z[G], and then in every
a^n. Their intersection is zero. Hence all128 actual columns are
independent over the entire group ring Z[G]. It follows that

    L intersect L_minus = 0,
    L + L_minus = L direct_sum L_minus is free of rank128 over Z[G].

Both summands are actual F-stable submodules (B94 and the inherited
odd-discrepancy argument of B96). The direct sum is therefore equivariant.
Its positive-degree C2 cohomology is the direct sum of the two summands:
H1 is F2[R]^8 and H2 is zero. B94 gives the four first-sheet source
values rho_i-1; the actual canonical odd pullback gives the four
second-sheet source values sigma_i-1, with harmless inversions at
critical indices0,12. Therefore the complete image in H1(C2,P) is

    J_eight = sum_i F2[R](rho_i-1) + sum_i F2[R](sigma_i-1),

and is contained in the actual source ideal J_I. The inverse/sign
conventions are the actual source comparison, not an unbased
identification of the two sheets. The complete independent odd-source
audit is `check_odd_translate_independent.py/.out`.

This is the full-G direct sum of two specified translates. It is not
a statement about all even/odd old-base translates, arbitrary sums or
their intersections. Leading-row parity alone would not settle those
larger sums: cancellations within one class could first remove its
leading augmentation terms. No such cancellation is present here,
because all128 selected unit rows are distinct.

A concrete check reinforces this limitation. Color a row by its y1
parity relative to the original pivot of the same physical slot pair.
The complete chains have both colors in39 of64 original columns and
in all64 odd columns. Thus this specified pivot-relative coloring is
not a homogeneous grading of the full column modules. The exact
check and genuine output are `check_cross_sheet_parity_scope.py/.out`;
it searches no other gradings and does not weaken the128-unit-pivot
proof above.

The result does not prove source equality, full kappa vanishing,
nonlinear fixed lifting or any completed coefficient comparison.
Indeed J_eight is strictly smaller than J_I by the proved nonfinite-
generation lemma: a finite source-generated left ideal cannot contain
the infinite-rank actual source image.

Complete certificate: `odd_G_overlap.json`.
Producer and genuine output: `check_odd_G_overlap.py/.out/.err`.
All128 full columns, actual words, input hashes, selected augmentation
rows and the explicit absence of collision candidates are retained.

Independent evidence: CE's
`work_CE/code/check_cross_sheet_overlap_independent.py/.out/.err`
imports no producer and constructs the product chains by integrating
at B edges. It checks all128 chains,256 boundary identities,128 literal
F identities, the complete G coefficients and128 distinct augmentation
unit rows. All64 old-axis parity differences are independently checked.
The complete independent proof review is
`work_CE/review_cross_sheet_overlap_18h.txt`; its input-bound data are
`work_CE/next_symmetric_nodes/cross_sheet_overlap_independent_review.json`.

## One F-stable block carrying all eight source classes

Put L8=L_ret direct_sum alpha_b^{-1}(L_ret). Let B0 be the index-two
old-base subgroup and S_t its actual returned source operators, as in
B96. Then the full actual node relation module has the exact description

    Lbar = sum_(t in B0) S_t(L8).

Indeed the even coset gives S_t(L_ret). The odd coset gives
S_t(alpha_b(L_ret)), while the actual branch-square source operator S
satisfies alpha_b(L_ret)=S(alpha_b^{-1}(L_ret)) as G-submodules.
Multiplication by its actual inner correction is a G unit and does not
change the submodule. Since S is one of the returned source operators,
its extra occurrence is absorbed as t ranges over all of B0.

Each S_t commutes literally with F, unlike the uncorrected far old-base
operators. Thus this is a source-operator orbit sum of a single actual
F-stable free-G block of rank128 whose entire Tate image is J_eight.
The sum of the individual orbit-block images is exactly J_I, because
the eight source elements and all eleven signed source operators
generate I. This is an exact reformulation of the still unresolved
whole-overlap issue, not an interchange of cohomology with image sums.

For a finite source-word set T0, write V_T0=sum_(t in T0) S_t(L8).
To prove that adding S_s(L8) creates no new class modulo J_I, it would
suffice to prove H2(C2, V_T0 intersect S_s(L8))=0, or more generally
that its connecting contribution has zero diagonal modulo J_I.
The intersection must be with the whole preceding sum. Neither
pairwise intersection checks nor the bounded parity witness supplies
that quantified statement.
