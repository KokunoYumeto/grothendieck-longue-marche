# Actual translations and the two remaining lower-handle coordinates

This note uses the E37/E95 based group, cusp paths and coordinates.  It
records a corrected reconstruction calculation.  The earlier assertion
that the unit central maps have rank28 failed.  Its source and error are
retained in history/a_handle_detection_rank28_attempt.*.

## Paths and the literal translation commutator

Use categorical composition with the rightmost map applied first.  Let
p_d go from the chosen unit tangent at O to the E37 unit tangent at d.
Thus k_d(g)=p_d^{-1}g(p_d), and the positive peripheral generator is
p_d^{-1}d_d p_d.  Its arithmetic image is
k_d(g)^{-1}(p_d^{-1}d_d p_d)^chi k_d(g), exactly as in E37.

Translation t_d on the proper cubic preserves its invariant differential.
In the literal E37 parameters this differential has leading coefficients

    O: -1/3;  A_i: zeta^i/3;  B_i,C_i: -zeta^i/3.

Consequently t_d carries the source unit tangent to the tangent with
parameter value a_d=-zeta^(-i) at A_i and zeta^(-i) at B_i,C_i.
The formulas follow directly from dx/(3y^2) on z=1 and
-ds/(3y^2) on x=1, with y=-zeta^i(1+s^3)^(1/3).

Let h_d be the formal-disc path from that tangent to the unit tangent at
d which sends the selected root alpha=a_d^(1/3^n) to1.  Its compatible
roots are literal powers of zeta_(3^(n+1)), and the roots of -1 are all
-1.  Coefficientwise arithmetic gives

    g(h_d)(alpha)=zeta_(3^n)^(-kappa_a_d(g)).

Hence h_d^{-1}g(h_d) is negative kappa_a_d inertia at the starting
tangent.  Set p_d^tr=h_d^{-1}p_d and

    T_d(n)=(p_d^tr)^(-1) t_d(n) p_d^tr.

The exact path identity is

    k_d^tr(g)
      =p_d^{-1}(h_d g(h_d)^{-1})p_d * k_d(g),
    (k_d^tr)^ab=k_d+kappa_a_d e_d.

In particular kappa_a_d=-i kappa_zeta for all three cusp types; the
extra minus sign at A_i has a Galois-fixed odd-root system.  The E95
columns therefore evaluate this abelian translation conjugator at every
actual arithmetic element.  For g in G_K, translations are defined over
the field fixed by g, and direct substitution gives

    rho_g T_d rho_g^{-1}=Ad((k_d^tr(g))^{-1}) T_d.

On N/gamma3 N, an inner automorphism depends only on the abelian
coordinate of its conjugating element.  This is exactly the point at
which E95's abelian k_d determines the needed class-two commutator.
No higher coordinate of the path has been replaced by that abelian
value.

## The actual linear translation and CM maps

Write j=(3I;U), with the E37 U.  Let P_d be the permutation of the nine
cusp classes under addition by d, expressed on the eight nonbase
classes using e_O=-sum e_d.  The exact action on V is

    A_d = [[I,0],[(U-P_d U)/3,P_d]].

The torus map and proper identity give the diagonal blocks; equivariance
of the actual j forces the lower block.  The displayed block is integral.
The code verifies all81 compositions, not just the two generating
translations.  For the covariant CM map delta:(x,y,z)->(x,y,zeta*z),
replace I by R and P_d by its cusp permutation.  The involution
(x,y,z)->(y,x,z) and complex conjugation have respectively the proper
matrices -I and C_E and their literal cusp permutations (with a minus
sign for conjugation).  These are the matrices used in the certificate.

Function-field lifts are kept separately.  The lift s^(1/m)->
zeta_(3m)s^(1/m) has cube the positive cusp deck transformation.
Its coefficientwise arithmetic commutator is positive kappa_zeta.
The induced covariant fundamental-group map is conjugation by the
inverse pullback, so the corresponding covariant formulas have the
inverse cusp conjugation.  The exact square in a_orbifold_decks.json,
P R=R^(-1)P modulo3, checks this convention on the actual proper
translations.  Both a map and its inverse have the same invariant
submodule.  The earlier peripheral-kernel computations used that
invariant submodule and therefore retain their matrices and ranks.

## Exact central unit kernel

Let L_f=Lambda2(f_ab) for every retained actual unit map to the
three-punctured line.  Include the seven ordinary-point witnesses with
their actual roots and path maps.  Their common matrix on M=Lambda2 V
has rank26.  Choose the explicit unimodular basis

    B=(j_1,j_2, f_1,f_2,e_A1,e_B0,e_B1,e_B2,e_C1,e_C2).

Its determinant is a unit (in fact plus or minus1).  The first17 exterior
basis columns, those involving j_1 or j_2, give the primitive submodule
K17=j(T3E) wedge V.  The common unit kernel K19 contains K17 and has
free quotient of rank2.  The actual local Smith factors of the remaining
28-column unit matrix are

    1^24, 3, 9.

The full rank19 basis, its left inverse, both Smith inverse pairs, and
the row-lattice maps are in a_handle_comparison.json.  In particular this
is a saturated kernel computation, not a rational-rank conclusion.

In the retained quotient basis the four actions on K19/K17 are

    delta=[[-1,1],[-1,0]], iota=-I,
    c=[[1,-1],[0,-1]], tau=49 I.

Translation invariants in K19 have rank3.  In the retained basis their
projection to K19/K17 is

    [[-3,0,0],[-3,3,0]],

and w=j_1 wedge j_2 is the third basis vector.  Thus the image is exactly
three times the rank-two quotient lattice, with kernel Z3*w.  The
translation equations have Smith factors 1^14,3,3.  Their entire
invariant lattice, with left inverse, is retained.

## The full two-handle comparison and its arithmetic module

A central IA difference fixing the peripheral class-two images vanishes
on W.  The translation comparison just proved makes its two handle
columns lie in the rank-three invariant lattice.  The actual CM
comparison gives D R=Lambda2(delta) D.  Its six-column matrix has
Smith factors 1,1,1,3 and a primitive rank-two kernel.  Every column of
the two resulting maps V/W->M and a common left inverse is retained.

The two residual coordinates have the exact actions

    delta=iota=I,
    c=[[-1,0],[-1,1]],
    tau=[[7,-21],[21,-14]].

The unimodular R=[[0,-1],[1,-1]] intertwines these matrices with
T3E(1) tensor chi_K: on the latter tau=7(I+3R) and c=+C_E.  This proves
the typed integral comparison.  It gives no value for the actual
arithmetic cocycle in this module.  The remaining two coordinates are
retained as actual elliptic data.

For reference, after normalization at c the continuous unramified
cohomology of this exact rank-two module is

    H1(P semidirect C2, H)=H/(tau-I)H^c = Z3 plus C3.

Indeed H^c is generated by (0,1), whose image is (-21,-15), a primitive
column times3.  This records the possible difference module; it does not
select the actual source action.  The ordinary geometric unit maps still
require their actual finite Heisenberg pullbacks and cannot be replaced
by their divisor rows when evaluating a representative action.

## Two further exact reconstruction tests

The complete retained 45-by2 handle columns have zero entries in every
exterior row involving f1 or f2.  Thus both maps have image in
wedge2(W), where W is the actual eight-dimensional cusp submodule of V.
The degree-two map to the once-punctured ambient metabelian quotient
of E50 kills exactly this submodule.  In the current ordered exterior
basis its projection selects the17 rows containing a handle; its two
composites with the residual handle maps are literally zero.  This is
why even an evaluated Nakamura ambient metabelian action would leave
these two coordinates undetected.  No conclusion about an ambient
higher-derived quotient follows from this zero map.

The residual C3 in H1 also survives every integral central IA change
of class-two coordinates, even changes that need not preserve the
translation and CM constraints.  Write D:H->Hom(V,wedge2 V) for the
retained primitive two-column inclusion, and h+=(0,1) in H^c.  The
normalized torsion cocycle has tau-value

    (T_H-1)h+/3=(-7,-5),

and rational c-fixed primitive D(h+)/3.  Any other rational primitive
differs from it by a T-fixed element of Hom(V,wedge2 V).

To compute that fixed space, use the actual rational basis
S=(j1,j2,e_A0,...,e_C2), whose determinant is9.  In this basis T is
diag(A_E,7I8), A_E=[[1,-3],[3,-2]].  The characteristic polynomials
on V and wedge2 V are respectively

    (x^2+x+7)(x-7)^8,
    (x-7)(x^2+7x+343)^8(x-49)^28.

Their sole common eigenfactor is x-7, with multiplicities8 and1.
The latter line is exactly Q3*w, w=j1 wedge j2.  Consequently every
rational T-fixed Hom map has image in Q3*w.  All these conclusions
come from the displayed coefficient change and its exterior inverse;
the certificate verifies the intertwining matrices directly.

In zero-based exterior row19, corresponding to e_A0 wedge e_B0,
the actual w entry is0, whereas D(h+) on source f1 has entry-2.
Every rational primitive therefore has that entry-2/3.  It cannot be
integral.  This proves that the nonzero residual C3 class remains
nonzero after mapping into H1 of the full central-IA module.  Thus a
rational regulator identification alone cannot remove this torsion
ambiguity by a larger integral coordinate change.

Both tests and their complete matrices are retained in
code/a_handle_torsion_gauge.py/.out/.json.  An initially slow symbolic
rank attempt was interrupted with exit130 and retained in history;
the successful program instead checks the exact rational block
decomposition and inverse matrices described above.
