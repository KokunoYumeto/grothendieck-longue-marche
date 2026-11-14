# F.49 candidate: Hilbertian normal extensions and small geometric Galois groups

**Status:** complete proof candidate for independent review, 14 November2026.
Not integrated. This is a further sufficient class for the actual
closed-point-preserving reconstruction convention. It does not resolve F.9.

## 1. Proposed statements

Let D be finitely generated over Q of positive transcendence degree. Work in
one algebraic closure containing an algebraic closure Qbar of Q. Let k/D be
an algebraic Galois extension containing Qbar.

**Hilbertian core.** If k is Hilbertian, every finitely generated extension
L/k satisfies closed-point-preserving etale reconstruction.

**Small geometric Galois class.** A profinite group is called small here if
it has only finitely many open subgroups of each prescribed finite index.
If Gal(k/DQbar) is small, k is Hilbertian, and every positive-transcendence
subfield k0 of every finitely generated extension L/k reconstructs. The
positive-transcendence restriction on k0 is retained: Qbar itself fails.

The small class contains an example outside F.46's entire union of proper
geometric pro-formation classes. For D=Q(t), put K0=Qbar(t), and for m>=2
put n=2m+1 and

\[
 P_m(X)=X^{2m+1}-\frac{2(2m+1)}{m+1}X^{m+1}+(2m+1)X.
 \tag{49.1}
\]

Let Omega_m be the splitting field of P_m(X)-t over Q(t), and set

\[
 k=\overline{\mathbf Q}(t)\prod_{m\ge2}\Omega_m.
 \tag{49.2}
\]

Then k/D is Galois and

\[
 \operatorname{Gal}(k/K_0)\simeq\prod_{m\ge2}A_{2m+1}.
 \tag{49.3}
\]

This group is small but has alternating quotients of unbounded degree in
every open subgroup. Hence the example is outside F.46, including after a
change of finitely generated algebraic model. No intrinsic necessity of
Hilbertianity or smallness is asserted.

## 2. Normal finite-type descent and the divisible kernel

For a finitely generated extension L/k and any finite list of geometric
data over L, choose a finitely generated field F/Q containing D such that
L=Fk and the data descend to F. Then

\[
 L/F\text{ is algebraic Galois},\qquad B=F\overline{\mathbf Q}\subset L.
 \tag{49.4}
\]

This is normality of the compositum of the Galois extension k/D with F.
No Hilbert irreducibility over F is needed for the core argument; its use
there will be over the Hilbertian field L itself.

For every finite E/k we have

\[
 D(E^*):=\bigcap_{n\ge1}(E^*)^n\subset k^*.
 \tag{49.5}
\]

Indeed take a in D(E*) and a finite Galois extension M/D inside the common
closure with a in M and E contained in Mk. Such an M exists because E/k
is finite and k/D is algebraic. For sigma in Gal(Mk/k), sigma preserves M.
For every n choose z_n in E with z_n^n=a. If tau is in Gal(Mk/M), then tau
preserves k, because k/D is normal. The automorphisms sigma and tau commute
on M and k, hence on Mk. Also sigma fixes all roots of unity. Since
tau(z_n)/z_n is a root of unity, sigma(z_n)/z_n is fixed by tau and is in M.
Consequently sigma(a)/a belongs to D(M*). For the finitely generated
characteristic-zero field M, D(M*)={1}, by the divisor and number-field unit
argument already proved in F.4/F.33. Thus a is fixed by Gal(Mk/k), so a is
in k. Notice that no equality D(E*)=k* is claimed; k* need not be divisible.

For every finitely generated E/k the same inclusion holds. A normal proper
model over the relative algebraic closure k1 of k in E shows that an
infinitely divisible element has zero valuation along every prime divisor
and hence lies in k1*. The extension k1/k is finite, so (49.5) applies.
More explicitly, every chosen n-th root of that element in E is algebraic
over k1 and hence belongs to k1, by relative algebraic closedness. Thus the
element belongs to D(k1*), which is the hypothesis of the finite case.
Thus the scalar ambiguity in point evaluation will always lie in k*.

## 3. Hilbertian finite-quotient detection with unbounded point degree

If k is Hilbertian, every finitely generated L/k is Hilbertian. Finite
extensions preserve Hilbertianity, and positive-transcendence finitely
generated extensions are Hilbertian by the already opened
Bary-Soroker--Paran theorem used in F.45. These properties also show that L
is not separably closed, before and after any finite extension.

Let X/L be smooth and geometrically connected, and let Y->X be a connected
finite etale Galois cover with group G, representing an arbitrary finite
quotient of pi_1(X). For a curve X, compactify and take a rational function
of arbitrarily large degree d by Riemann--Roch, restricting to an open
where it is finite etale. The connected composite Y->P1 has degree d|G|.
Hilbert irreducibility, applied to this entire composite including its
arithmetic constant field, gives an L-rational specialization with one
residue field of degree d|G|. Its G-quotient is a closed point x of X of
degree d, and the fibre of Y over x is one field of degree |G| over L(x).
Thus the decomposition map G_{L(x)}->G is surjective. Excluding any
prescribed finite set and increasing d gives unbounded-degree detecting
points in every nonempty open. For higher-dimensional X, the
cover-preserving curve construction F.29 transfers this assertion, with
the same finite quotient and with any specified open restriction.

This proves precisely the finite-quotient detection and unbounded-degree
input used in F.45/F.46. It does not discard the constant quotient of G.

## 4. Integral Kummer residues: the fixed norm field

We spell out the arithmetic replacement needed to apply the reconstructed
unit argument. On a punctured line

\[
 U=\operatorname{Spec}L[T,1/(P_1\cdots P_r)]
\]

with distinct monic irreducible P_j, a compatible Kummer class normalized
at x0 has the form

\[
 \kappa(b_0)+\sum_j\lambda_j([P_j(T)]-[P_j(x_0)]),
 \qquad\lambda_j\in\widehat{\mathbf Z}.
 \tag{49.6}
\]

Assume it has an actual multiplicative value at every point over every
finite extension of L, as occurs for the pinned maps under consideration.
Choose F in (49.4) containing all coefficients and normalizing data.
Choose a nontrivial finite extension of L; after taking its Galois closure
and descending its defining polynomial, choose a finite Galois extension
M/Q(t1,...,ts) containing F, all roots of the P_j, and the descended
extension data. Then Mk/L is finite Galois and nontrivial. Choose a
nonidentity sigma in Gal(Mk/L). It preserves M, fixes k and Qbar, and acts
nontrivially on M. Apply the moved-geometric-divisor lemma proved in F.45
to M over M cap Qbar and sigma. Its construction gives the required
distinct prime valuations v_i with disjoint sigma-translates, all prescribed
coefficients and root differences units, and residue characteristic zero.

Semilocal approximation at these primes gives alpha in M such that

\[
 v_i(P_j(\alpha))=\delta_{ij},\qquad
 v_i(P_j(\sigma\alpha))=0.
 \tag{49.7}
\]

This is the same root-plus-uniformizer Taylor calculation as F.45.5; sigma
fixes the polynomial coefficients but is allowed to permute the roots.
Put R_j=P_j(sigma alpha)/P_j(alpha), so v_i(R_j)=-delta_ij, and choose an
actual value b_alpha in (Mk)*. Because k/D is algebraic, a single finite
extension S0/D inside k contains all coefficients needed to write this
value in the compositum. Put F'=MS0. This field is chosen once, independently
of n, and contains b_alpha, sigma(b_alpha), and every R_j.

If a in (F')* has z^n=a in Mk, then sigma(z)/z lies in F'. Indeed for every
tau in Gal(Mk/F'), sigma and tau commute on M and k; sigma fixes the root
of unity tau(z)/z. Hence tau fixes sigma(z)/z. Therefore

\[
 \sigma(a)/a\in((F')^*)^n.
 \tag{49.8}
\]

Represent lambda_j modulo n by integers a_{j,n}. Evaluation of (49.6)
and (49.8) gives

\[
 \frac{\sigma b_\alpha}{b_\alpha}
       \prod_j R_j^{-a_{j,n}}\in((F')^*)^n.
 \tag{49.9}
\]

Apply the integer-valued homomorphism v_i composed with N_{F'/M}. Since
the R_j are in M, this proves

\[
 [F':M]\lambda_i
   =-(v_i\circ N_{F'/M})(\sigma b_\alpha/b_\alpha)\in\mathbf Z.
 \tag{49.10}
\]

An element of Zhat whose nonzero integer multiple is an ordinary integer
is an ordinary integer: the rational quotient is integral at every prime.
Thus every lambda_i is in Z. This is exactly the fixed-field norm argument
of F.46; it uses normality, roots of unity and finite actual values, not a
pro-formation quotient or divisibility of every element of k.

## 5. From residues to the full topos reconstruction

For clarity we verify each remaining input rather than assuming that a
field with the same Galois quotients automatically reconstructs. Let X/L
be regular connected affine with an L-point x0, and let its pinned relative
map to Gm have its compatible Kummer class xi. Smoothness and geometric
connectedness follow as in the CHW reduction. Descend the geometry and the
generalized Albanese A to F in (49.4), after a finite extension splitting
the boundary. The integral Spieß--Szamuely comparison identifies H^1 of
Xbar with the dual of the full Albanese Tate module. Put H=G_L normal in
G_F and W=(V_l A)_H.

Finite-quotient detection in Section3 makes the projected point-Kummer
images span W: a functional annihilating all such images would, at a
finite coefficient level where it is nonzero, give a finite quotient whose
detecting decomposition group contradicts that annihilation. This is the
complete annihilating-functional argument supplied in F.43--F.46; Section3
checks its precise finite arithmetic quotient hypothesis here.

Choose finitely many spanning point images. Their coordinates and actual
multiplicative values descend to one finitely generated M/Q, enlarging F
by finite data. Normality of G_L in G_F makes W stable. Conjugating a point
cocycle changes it by a coboundary killed in H-coinvariants, whereas the
actual multiplicative value has the cyclotomic transformation rule. Thus
the functional is G_M-equivariant on the chosen spanning images and hence
on W. Jannsen's original Theorem4.3(ii), p676, is applied over this
finitely generated field M only. It places the functional in the integral
unit lattice, consistently in every coefficient prime after splitting the
boundary and normalizing at x0. No Tate theorem over k or L is assumed.

For a curve, norm to a punctured rational line and Section4 make each
boundary residue integral; the norm coefficient is the residue-field
degree. For a higher-dimensional X, take a smooth transverse curve through
each boundary divisor after the finite etale localization used in F.27.
The local equation becomes u z^a, transversality gives the same residue,
and Section4 again makes it integral. The injective divisor matrix of a
unit basis therefore gives an actual global unit h. Normalize h(x0)=b0.
Conjugate units have equal divisors and ratio one at x0, so h descends.
The residual class is geometrically zero at each finite Kummer level;
Hochschild--Serre makes it constant, and evaluation at x0 kills it. Hence

\[
                              \xi=\kappa(h).
 \tag{49.11}
\]

Every step in this paragraph is the proved norm/transverse/unit descent
argument F.27 and F.45--F.46 with the precise residue hypothesis now proved
in (49.10). It yields equality of the compatible Kummer class, not yet of
the full topos maps.

Let phi be the actual geometric point function. Equations (49.5) and
(49.11) give

\[
                         \phi(x)=c_xh(x),\qquad c_x\in k^*.
 \tag{49.12}
\]

If h is nonconstant on a curve, points of degree greater than deg(h) have
h(x) outside L and hence outside k. In particular phi is nonconstant.
Pulling back T-1 to its nonempty inverse open gives a unit h1 and scalars
d_x in k*. At a closed point whose degree exceeds the combined pole
degrees, the function c_xh-d_xh1-1 vanishes and hence is identically zero.
Thus h1=A h+B with nonzero A,B in k. Comparing values where h(x) is
outside k fixes c_x=-A/B=c. Repeat with T-b for each b in k*; the resulting
unit is e_b(ch-b). At an x with h(x) in k choose b=ch(x). If phi(x) differed
from b, the pulled-back unit would vanish inside its invertible locus.
Thus phi=ch everywhere, and normalization at x0 fixes c=1.

If h is constant, pass to a finite extension L'/L and choose beta with
beta/h outside k. Such a choice is available because L is Hilbertian and
therefore has a nontrivial finite separable extension: take beta outside L.
All earlier statements hold over L'. No point maps to beta by (49.12).
The inverse image of beta is closed; a nonempty closed subset of a finite-
type L'-scheme has a closed point. Hence T-beta pulls back as a unit on
the entire source. Its values lie in L' by (49.12), so unbounded-degree
points and the pole-degree bound make this unit constant. Normalizing
at x0 gives

\[
        (\phi(x)-\beta)/(h-\beta)\in k,
        \qquad \phi(x)/h\in k.
\]

Since beta/h is outside k, these two relations force phi(x)=h. For higher
dimension, after a finite extension join an arbitrary geometric point to
x0 by a smooth geometrically connected curve using F.29; the normalized
units have equal Kummer classes, and their ratio is an infinitely divisible
unit equal to one at x0, hence is one by the divisor argument. This gives
the same point function on X.

CHW Theorem4.18(5), already opened and used in F.45/F.46, now yields the
complete closed-point-preserving all-scheme reconstruction statement over
L. The full-topos conclusion comes from that theorem after equality of
point functions, not from a substitution of fundamental groups for topoi.

## 6. Why small geometric Galois groups supply the Hilbertian input

First, an open subgroup of a small profinite group is small. An open
subgroup of H of index n is an open subgroup of G of index n[G:H], so
there are finitely many. A quotient of a small group is small because
its open subgroups pull back injectively to open subgroups of the same
index. No closure under arbitrary closed subgroups is claimed.

Suppose Gal(k/K0) is small, K0=DQbar. For L=Fk and B=FQbar as in (49.4),
B/K0 is finitely generated. Its relative algebraic closure of K0 is
finite, so k cap B is finite over K0 (Stacks Tag030D, already used in
F.45/F.46). Restriction identifies

\[
       \operatorname{Gal}(L/B)=\operatorname{Gal}(k/(k\cap B)),
 \tag{49.13}
\]

an open subgroup of the small geometric group. Thus L/B is a small
Galois extension of the Hilbertian field B.

Here is a direct proof of the required Hilbertian property that retains
all constants. Take any connected finite Galois cover Y->X over L, with
X a smooth geometrically connected curve. Descend it to B after enlarging
F by finite data; the descended cover Y_B->X_B has group G and remains
connected over L. Its algebraic constant field M/B is finite Galois and
M cap L=B. Choose a Riemann--Roch function X_B->P1 of arbitrarily large
degree d, and put D0=d|G|.

There are only finitely many subextensions of L/B of degree at most D0.
Let S/B be the compositum of their Galois closures inside L. It is finite
Galois, and M cap S=B, so Y_B times_B S is connected. Hilbert
irreducibility over B, applied to its entire composite map to P1 of
degree D0[S:B], gives a single residue field of that full degree. Its
Y_B residue field E has degree D0 over B and is linearly disjoint from S.
Since E cap L has degree at most D0, it lies in S. Hence E cap L=B.
Because L/B is Galois, E and L are linearly disjoint over B. The point and
cover degrees d and |G| therefore survive base change to L, giving a
surjective decomposition map over L.

The same argument with X an open of A1 and the Galois closure of any
given irreducible separable polynomial over L(T) proves the Hilbertian
specialization property for L. All coefficients descend after increasing
F, so this treats every such polynomial. In particular k is Hilbertian.
The core theorem applies. The direct version also confirms the precise
finite-quotient and unbounded-degree inputs independently of terminology.

## 7. Arbitrary positive-transcendence subfields in the small class

Let k0 be a positive-transcendence subfield of a finitely generated L/k.
Choose a finite transcendence basis T of k0/Q and put A=Q(T). Enlarge the
descent field F in (49.4) to contain T. Let R be the relative algebraic
closure of A in F; R/A is finite and F/R is regular. Let N/R be the
possibly infinite normal closure of Rk0/R. Regularity identifies
R-conjugates with F-conjugates. Since L/F is normal, every one lies in L,
so N is contained in L. Base change preserves regularity, giving

\[
              N\overline{\mathbf Q}\cap F\overline{\mathbf Q}
                         =R\overline{\mathbf Q}.
 \tag{49.14}
\]

Restriction therefore makes Gal(NQbar/RQbar) a quotient of Gal(L/B).
It is small by (49.13). The extension NQbar/R is algebraic Galois,
contains Qbar, and R has positive finite transcendence degree. Section6
and the core theorem apply to NQbar. Finally NQbar/k0 is algebraic,
because R/A is finite, Qbar/Q is algebraic, and A is contained in k0.
F.32 descends reconstruction to k0.

This argument does not assert that every closed subgroup of a small group
is small, nor that a finite subdirect product preserves smallness. It does
not claim an equivalence between the full embedding class and a normal-
closure condition over a finitely generated subfield of k0. Such an
equivalence is not needed for the proved sufficient statement.

## 8. Explicit unbounded alternating example and strictness

For (49.1),

\[
 P'_m(X)=(2m+1)(X^m-1)^2,
 \qquad P_m(\zeta)=\frac{2m^2}{m+1}\zeta\quad(\zeta^m=1).
 \tag{49.15}
\]

Thus the m finite critical points have distinct branch values and exact
ramification index3. Infinity has index n=2m+1. Over Qbar the degree-n
polynomial cover is connected, so its monodromy is transitive. Its inertia
generators at finite branch points are 3-cycles. These generate the whole
geometric group: quotient by their normal closure would give a cover of
P1 unramified outside infinity, which is trivial by Riemann--Hurwitz in
characteristic zero. All those cycles are even.

A transitive subgroup of S_n generated by 3-cycles equals A_n. Here is the
elementary support argument. The support triples form a connected
hypergraph because its connected components are group orbits. Start with
one triple, generating A3. Add a triple meeting the accumulated vertex set.
If it adds one vertex, its conjugates under the existing alternating group
give all needed 3-cycles involving that vertex and generate the larger
alternating group. If it adds two vertices, conjugate it by an old 3-cycle
moving the shared old vertex; the two triples now meet in the two new
vertices and generate A4 on those two old and two new vertices. This
reduces to the preceding one-new-vertex step. Induction proves the claim.
Thus the geometric splitting group of P_m(X)-t is A_{2m+1}.

These nonabelian simple groups are pairwise nonisomorphic for m>=2.
Finite subfamilies of the corresponding Galois extensions over K0 are
linearly disjoint, by the elementary Goursat argument: a common nontrivial
quotient of one simple group and a product of the previously distinct
simple groups would force an isomorphism with one factor. This proves
(49.3). The field k/D is Galois because each Omega_m/D and DQbar/D is
Galois and their compositum is normal.

The product in (49.3) is small. For a subgroup of index d, its coset action
is a continuous homomorphism to S_d. A factor A_{2m+1} whose order exceeds
d! must act trivially, since a nontrivial image of that simple group is
injective. Only finitely many factors can remain, and their finite product
has finitely many subgroups. Continuity kills the entire product of the
remaining factors, since its finite-support subgroup is dense. Thus there are finitely many subgroups of
each index d. Conversely every open subgroup of the product contains all
but finitely many whole factors, so it has alternating quotients of
unbounded degree.

For strictness relative to F.46, suppose the field in (49.2) had a
finitely generated algebraic model F0 contained in k with virtually
pro-C geometric normal closure for an allowed proper formation C. Enlarge
F0 to F1=F0Q(t), a finite extension of both F0 and Q(t), since k has
transcendence degree one and is algebraic over each. Finite base change
preserves virtual pro-C, and the normality of k/Q(t) makes
Gal(k/F1Qbar) a quotient of that base-changed normal-closure group. Hence
it would be virtually pro-C. But it is an open subgroup of (49.3), and
each of its open subgroups has A_n quotients of unbounded n. F.44's
elementary proper-formation argument excludes all sufficiently large A_n
from C, a contradiction.

Therefore the example reconstructs by this new sufficient class and lies
outside the entire sufficient embedding class of F.46. It is not an
increasing union argument for reconstruction: the theorem proves the
infinite field directly, using smallness and normality.

## 9. Source and verification boundaries

The Hilbertian input over finitely generated extensions of Qbar is the
opened Bary-Soroker--Paran source recorded in F.45; the finite-extension
and complete-cover Hilbert specialization uses the opened Serre source
already recorded in F.44. Spieß--Szamuely, Jannsen, CHW and the moved-prime,
norm, transverse-curve and algebraic-extension descent results are used at
the exact loci independently reviewed in F.43--F.47. Preservation of
Hilbertianity in small Galois extensions is a known input: Bary-Soroker
(2008), arXiv0803.0451v3, Theorem4.4, p9, gives the assertion and a complete
proof; Bary-Soroker, Fehm, and Petersen (2023), arXiv2312.16219v1,
Theorem1.2 and Corollary4.3, pp1,5, prove the more general Hilbert-property
base-change statement and explicitly use the finite bounded-degree
compositum. Section6 supplies the constants-sensitive version needed here;
we do not claim that Hilbertian input or its bounded-degree mechanism as
new. Both primary texts were opened by root and independently by the
finite-field reviewer.

The weaker divisible-kernel inclusion, normal-field reconstruction proof,
small-group subfield descent, and explicit strict examples are proved in
this return. Focused searches and the exact opened passages are recorded
in audit/F_small_geometric_literature.md. Both independent full-candidate
reviews accepted Sections2--7 and the examples, with the explicit root and
dense-tail clarifications now incorporated. No priority, necessity, or
completion of F.9 is claimed.
