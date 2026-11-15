# Exact completion of the four-branch/four-pair elliptic centralizer

Auditor: `levels_geometry`. This proves the specific centralizer and parameter comparison requested by `finite_models` on 2026-11-15. The marked torus has twelve points: four fixed points of the involution and four two-element orbits. In the torsion application the set is E[2] union E[3], of cardinality 4+9-1=12.

## 1. Discrete groups and the actual quotient

Let iota be the elliptic involution. Let G be the finite-index mixed subgroup of the orientation-preserving mapping class group that fixes its four fixed labels individually and preserves each of its four named two-element orbits. Thus its permitted finite permutations are the four independent pair flips. Put C=C_G(iota).

Deleting all twelve upstairs marked points and all eight downstairs marked points makes the double cover unramified. Its based surface groups are

`P0=pi1(S1,12)=F13 < E0=pi1(S0,8)=F7`,

with index two. The covering character E0→C2 has value one on the four branch cusps and zero on the four pair cusps.

There is an exact sequence with the actual quotient map

`1→<iota>→C→Gamma0,8→1`.

Here Gamma0,8 is pure and all eight labels are named. To justify the map directly, identify E0 with the inverse image of <iota> in Aut(P0) by conjugation; its centralizer of P0 is trivial. An upstairs centralizing mapping class therefore acts on E0 up to an inner automorphism. At a branch cusp the downstairs peripheral element u has square u² equal to the upstairs peripheral element. Preservation of that named upstairs cusp and unique roots in the discrete free group E0 imply preservation of the positive conjugacy class of u. At a pair cusp its two lifts are the two named upstairs points, so preservation of their pair gives the same downstairs peripheral class. The punctured-sphere Dehn–Nielsen–Baer theorem gives the stated pure downstairs mapping class. The kernel is exactly the two deck transformations. Conversely every pure downstairs mapping class preserves the displayed covering character, so lifts; its lifts preserve every fixed label and every named pair, and centralize the deck involution.

## 2. The quotient after full completion

Write P=P0hat=Fhat13 and E=E0hat=Fhat7. The index-two sequence is exact and P has its full topology in E. Both groups are center-free. Moreover C_E(P)=1: if e centralizes P, then e² lies in the center of P, so e²=1; the free profinite group E has no nontrivial finite-order element. Conjugation consequently identifies E as a closed subgroup of Aut(P), and it is precisely the inverse image of <iota> under Aut(P)→Out(P). Indeed it contains Inn(P) and has the required single nontrivial quotient coset.

Completing the discrete centralizer sequence is right exact. Its finite kernel <iota> is still embedded: the involution acts as -I on the filled torus homology modulo three, which detects its nonidentity element. Therefore

`1→<iota>→Chat→Gammahat0,8→1`

is exact. This uses the actual finite kernel, not an assumed exactness of an arbitrary subgroup completion.

There is a canonical continuous map

`r:C_Out(P)(iota)→Out(E)`.

Represent an outer automorphism by an automorphism of P. Centralizing iota means it normalizes the indicated inverse-image subgroup E in Aut(P). Conjugation then acts on E. Changing the representative by Inn(P) changes that action by an inner automorphism of E, so r is well defined. It is continuous: the conjugation maps on the finitely generated closed subgroup E are continuous on each finite characteristic quotient.

Let rho:Chat→Out(P) be the completed upstairs action and q:Chat→Gammahat0,8 the quotient above. The actual covering diagram gives

`r rho = rho0 q`,

where rho0 is the standard action of Gammahat0,8 on E. It is first an equality on the dense discrete C and hence on its completion. Genus-zero CSP, proved in D.19, makes rho0 injective. If rho(x)=1, then q(x)=1; exactness puts x in <iota>, whose action on P is nontrivial by the same torus homology calculation. Thus rho is injective.

The representation rho factors through the actual map Chat→Ghat followed by the completed surface-group monodromy. Consequently Chat→Ghat is injective. Compactness identifies its image with the closure of C, giving the full topology induced on C by G. The ambient genus-one CSP is not needed for this implication. Since G is good and of finite virtual cohomological type (the genus-one and finite-index arguments in D.35), Boggi–Zalesskii Theorem A at p=2 applies to iota and gives

`C_Ghat(iota)=closure(C)=Chat`,

and therefore the precise quotient

`C_Ghat(iota)/<iota> = Gammahat0,8`.

The same argument works with any of the four pairs forgotten, retaining the four branch labels. Every comparison is the restriction of ordinary upstairs forgetting and the corresponding actual downstairs forgetting.

## 3. Straightening the involution with the specified labels

For this permutation representation there is a single pure conjugacy class of geometric involutions. Finite-subgroup realization and uniformization identify its quotient family with the eight-point sphere having four branch labels and four ordinary labels. The branched double cover is determined by the four branch points. For each ordinary label there are two choices for its named first lift. Moving that ordinary point once around one branch point interchanges its two lifts and leaves the other choices unchanged. These four loops generate the independent C2^4 flips. Thus the cover parametrizing all choices of individual pair labels is connected over the connected M0,8; all realized marked involutions lie in one pure class.

An ordinary tower action fixes the finite permutation quotient. Theorem A geometrizes its image of iota. Removing the conjugator's finite permutation with a discrete mixed mapping class leaves a pure profinite conjugator and the same elementwise permutation data. The single pure class then supplies a pure discrete correction. After this adjustment the action fixes iota and preserves the centralizer and each named pair-forgetting map. Inner corrections supply the ordinary inner comparisons in the quotient diagrams.

## 4. The induced eight-point parameter is exactly A

The full induced quotient automorphism beta of Gammahat0,8 has, by Hoshi–Minamide–Mochizuki Corollary2.8 already used in E.12/E.24, a unique form `(B,s)∈GThat×S8`. For each of the four ordinary pair labels j, forget the other three pairs. The resulting map retains the same four branch labels and j, and is precisely the corresponding five-point quotient in E.37/E.44.

These four forgetting kernels are preserved. Their retained five-element subsets are distinct and intrinsically distinguished: a pair twist tau_uv survives the corresponding forgetful map exactly when both u and v are retained. Thus no two retained subsets have the same kernel. Since the GT factor preserves the named forgetting maps, s must preserve each of the four retained subsets. Their common intersection is the branch quartet and their four separate remaining elements are the pair labels. Therefore s fixes each pair label and can only permute the four branch labels.

The branch ordering in E.37/E.44 is pinned by the original fixed labels. Its comparison identifies the induced automorphism on each named five-point quotient with `(A,1)`. Restricting `(B,s)` to one such quotient therefore forces B=A and fixes all four branch labels, because the S5 factor in Out(Gammahat0,5) is faithful. Hence s=1 and beta is exactly the named genus-zero action A on Gammahat0,8.

This proves the completed group, topology, and parameter comparisons. It makes no assertion about an additional defect term or its vanishing; those require the subsequent torsion-configuration diagram being developed by the owner.

## 5. Independent audit of the successive fixed-point operation

The completed universal-curve inverse images of the elliptic involution, starting with the nine-point three-torsion orbit and then adding its three remaining fixed points, are precisely the completions of

(C2 * C2 * C2) * F4, (C2 * C2) * F5, C2 * F6, and F7.

The even kernels have ranks 10, 11, 12, 13. The free factors record the paired punctures; omitting them gives the wrong universal-curve group. The reduced-word torsion theorem gives three, two, one remaining order-two conjugacy classes. The p=2 case of the audited Boggi–Zalesskii Theorem A gives the same classes after completion and gives the closure of their discrete centralizers. Each whole-group class is one even-kernel class: the odd cone generator centralizes itself, so it corrects the parity of a conjugator.

The centralizer of a chosen lift intersects the even free kernel trivially. Its projection to the finite-index class stabilizer in the base is onto: lift a base element and correct its action on the chosen lift by an even-kernel conjugator. Thus projection is an isomorphism. Full topology follows by pulling finite quotients back along actual ordinary forgetting to that base class stabilizer. The full Birman kernel topology and the actual fibre-product lemma E.32 identify these with the completed universal-curve pullbacks. The ordered groupoid of all three successive lift choices, followed by its actual finite permutation descent, adjoins the three fixed points jointly and functorially. No independent torsion-configuration operation has been assumed.

## 6. Ordered quartic poles and the determinant-minus-one correction

Normalize the distinguished fifth point of the sphere to infinity and use the monic equation t² = product_i (x-alpha_i).

Its two sections at infinity are defined by t/x² tending to +1 and -1. A permutation of the four roots leaves this equation and both sections unchanged. Along every branch braid, the monic family therefore fixes each section individually. Under a change of affine coordinate x'=c*x+d, the transition is exactly t'=c²*t; it preserves the two signs and composes exactly on triple overlaps. This is the relative degree-two line-bundle descent and requires no choice of a square root of a leading coefficient.

Consequently every branch relabelling lifts to the group with its two elliptic labels individually fixed, Gamma1,2 = B4/Z(B4). The determinant-minus-one correction of the original three-torsion level basis only permutes those four branch labels. Its target comparison is therefore inner in this exact ordered group, not merely in the extension that permits swapping the two poles. On the source, it can be represented by half twists among the eight nonzero labelled points in a disk avoiding the origin; ordinary forgetting to the single origin kills that braid.

## 7. Exact CM stack map, topology, and the global gauge

The formulas in integrated E.49 are mutually inverse:

D = 4a³+27b²; t² = x⁴+2a*x²+4b*x-a²/3;

X = (t+x²+a)/2; Z = X-a/3; Y = X*x+b/2;

Y² = Z³+D/108; P = (-a/3,-b/2);

x = (Y-b/2)/(Z+a/3); t = 2(Z+a/3)-x²-a.

The two projective smooth completions are isomorphic by these birational inverse maps. Their named poles are the origin and P. After rigidifying the original central involution, the source has weights (2,3). The slice D=108 is isomorphic to the affine curve E0 minus its origin by (Z,Y)=(-a/3,-b/2), with inverse (a,b)=(-3Z,-2Y). The residual group is exactly mu6 with weights (2,3). Hence this is the actual stack isomorphism from [(a,b), D nonzero / Gm_(2,3)] to [(E0 minus O)/mu6].

It identifies the modular commutator subgroup B' with the point-push kernel. A primitive cusp remains primitive under an orbifold isomorphism; its sixth power is the primitive puncture in the index-six once-punctured-torus subgroup. The quotient sends the named cusp generator to the actual exponent R_+^epsilon, epsilon=+1 or -1. E.49 retains that exponent and does not replace a generator by a power.

The completed CM pullback is exactly G3=q^{-1}(C6): its discrete extension has free index-six kernel, whose completion embeds in the ambient group by full Birman exactness. The finite quotient C6 embeds as the actual CM subgroup in the base. The resulting map is the identity on kernel and quotient, hence is both injective and surjective. This is not an assertion that the CM pullback has finite index in the ambient twice-marked mapping class group.

Naturality of the intrinsic construction gives the single conjugator h of E.267. Both induced quotient actions are the identity on C6, so q(h) centralizes its generator. Modulo the central C2, the audited p=3 centralizer theorem for the finite free-product factor gives exactly C3; its preimage is C6. Thus q(h)=R_+^k with one exponent k modulo six. The same exponent acts at two and three. The integrated exact point-push normalization, affine commutator module, and signed frames then give the two equal parities in E.268.

**Final audit, 2026-11-15 15:36 UTC:** the complete integrated sections/E_cm_parity_vanishing.tex was read, including the scalar-free normalization and both finite-prime frame arguments. The geometric maps, full induced topologies, ordered-pole descent, primitive inertia, and single global gauge pass independently. The executed symbolic and finite-module certificates are the owner's b_cm_quartic.py and b_cm_module.py with their saved JSON/output. This note certifies the actual E.49 proof and its scope.
