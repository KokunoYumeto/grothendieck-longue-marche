# Independent audit of A.4.56

Reviewed `root_involution_configuration_fusion.tex` in full on
2026-11-17. Mathematical result: **PASS**.

## Exact period fibre

The induced period map has kernel contained in Gamma(6), and its
identity coset coordinate retains eta1 of the actual linear section.
Thus a representative with trivial retained labels and period is
literally k s(A), with eta1*(s(A))=1. This proves that the indicated
subgroup is exactly K_n/V1. Multiplication by the retained named
involution gives the exact stated coset, not merely an inclusion.
The induced quotient order is at most144|E1|^144, so the joined
bound144|E1|^145 follows.

## Reduced-cone fixed point

The competing complement acts compatibly on the actual covers.
Connectedness makes the constant-cochain cone quasi-isomorphic to
the reduced complex in degrees0 through2n-2. The 2n-1 successive
zero ordinary-cohomology maps kill its Tate hypercohomology.
Localization to the fixed cells is natural also when the fixed set
is empty. The latter case would leave the constant F2 in degree−1
and identity transition maps, contradicting vanishing. This proves
existence of a fixed point on the bottom cover with no unproved
fixed-point assumption at the top.

## Ordered assignments and actual mapping classes

The two displayed matrices U^3,L^3 lie in Gamma(3) and generate
SL2(F2) after reduction. Its permutation action on the three nonzero
two-torsion points is all S3, so it is transitive on every displayed
ordered assignment, of lengths0,1,2,3. The selected linear map fixes
the original three-division configuration and sends the additional
fixed labels correctly. The sphere isotopy fixes all branch points;
independent one-point branch loops prescribe all four lift signs.
Its identity-started lift has period identity and commutes with the
linear involution. Thus ell has the prescribed assignment and
positive integral period A.

## The exact path direction in ICF.9

Let psi_t extend gamma and fix the origin. The path of homeomorphisms

    h_t = psi_t^{-1} iota psi_t iota^{-1}

starts at identity and ends at
alpha_xi iota alpha_xi^{-1} iota^{-1}, because ell commutes with
iota. Its evaluation loop is homotopic to

    (iota gamma) * gamma^{-1}.

For an explicit homotopy, use the triangular parameter region
0 <= s <= t <=1 in psi_s^{-1} iota psi_t(x_n). Its diagonal is the
evaluation loop, its s=0 edge is iota gamma, and its t=1 edge is
psi_s^{-1}(xi). The latter is homotopic relative endpoints to
gamma^{-1}, using the same triangle without iota. Under the
inverse-endpoint point-pushing identification pi1(X_n)=K_n, this
evaluation loop corresponds to its inverse. Hence the actual element
is [gamma*(iota gamma)^{-1}], as written in ICF.9.

Equivalently, in the path model of the universal cover, that crossed
word times the canonical involution fixes the lifted endpoint
[gamma], since its action is

    [gamma*(iota gamma)^{-1}*(iota gamma)] = [gamma].

This agrees with alpha_xi=psi^{-1}ell and fixes the conjugation
direction. The final actual deck lift k sends that endpoint to the
chosen bottom fixed point. Two lifts of the same involution fixing
that point differ by a deck transformation fixing a point, hence
are equal. This proves ICF.4 in the specified injected semidirect
product. Both k and alpha_xi are pure and positive.

The theorem states a finite quotient comparison only for the exact
label/period fibre. Its final paragraph correctly retains the
additional need to verify those coordinates for a transported
tower action.
