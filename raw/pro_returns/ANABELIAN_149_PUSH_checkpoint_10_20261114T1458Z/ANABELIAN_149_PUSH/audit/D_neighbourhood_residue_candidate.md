# Killing a new Brauer residue in an accessible étale neighbourhood

**Status:** candidate route analysis, not a D1–D4 resolution. The group-theoretic criterion and real obstruction below have been independently checked by `/root/finite_field`. No integrated manuscript file is changed during checkpoint07.

## 1. Exact accessible-cover criterion

Let

\[
1\longrightarrow \Pi\longrightarrow E\xrightarrow{\rho}G_k\longrightarrow1
\]

be the arithmetic fundamental group extension of a smooth geometrically connected hyperbolic curve U/k. Fix an actual continuous section s and an ordinary rational point a, with point section s_a. Put S=s(G_k) and D_a=s_a(G_k). Let chi:G_k→Z/n be a continuous character. Define the compact subset

\[
 C_\chi=\{\gamma s_a(\sigma)\gamma^{-1}:
                 \gamma\in\Pi,\;\chi(\sigma)\ne0\}\subset E.
\]

It is compact because Pi and the clopen set G_k−ker(chi) are compact. There is a connected finite étale neighbourhood V→U of s such that chi restricts to zero on **every residue field of every closed point above a** if and only if

\[
                       S\cap C_\chi=\varnothing.                 (1)
\]

Equivalently, for no sigma with chi(sigma)≠0 are s(sigma) and s_a(sigma) geometrically conjugate.

**Proof.** A neighbourhood is an open subgroup H⊂E containing S. Since rho(H)=G_k, the cover is geometrically connected. Its fibre over a is the finite D_a-set of cosets E/H. Every E-coset has a representative in Pi, because E=Pi H. The stabilizers of its D_a-orbits are D_a∩gamma H gamma^{-1}; under D_a≅G_k these are exactly the absolute Galois groups of the residue fields, with their chosen embeddings. Thus every residue field kills chi exactly when H∩C_chi is empty.

Necessity of (1) follows from S⊂H. Conversely, the subgroups SN, as N ranges over open normal subgroups of E, are open subgroups containing S and have intersection S. If every SN met C_chi, the closed subsets SN∩C_chi of the compact space C_chi would have the finite-intersection property, since replacing finitely many N by their intersection refines all of them. Their intersection would meet S, contrary to (1). Thus one SN is the required H. This argument does not require finite generation or a section-space compactness assertion.

An element of S∩C_chi has the form s(tau)=gamma s_a(sigma)gamma^{-1}. Applying rho gives tau=sigma. This proves the equivalent elementwise formulation. It is not the assertion that s and s_a are conjugate as homomorphisms on all of G_k, and ordinary point-section injectivity does not imply (1).

## 2. Positive consequence of a residue-killing neighbourhood

For U=P1_k−{0,1,infinity}, let a be an interior rational point, W=U−{a}, and

\[
 \beta_{a,\chi}=\kappa(t-a)\smile\chi\in\operatorname{Br}(W)[n].
\]

Suppose (1) holds and choose V as above. Let V_a be the inverse image of a. Since V→U is étale, the cohomological residue of beta pulled back to V−V_a at y∈V_a is exactly Res_{k(y)/k}(chi), with ramification index1. It vanishes at every y. The regular-curve purity sequence therefore extends the class uniquely to Br(V)[n]. This uses the same residue convention and opened primary source as D.27; no corestriction or degree cancellation is being substituted for restriction.

Choose an étale H2(V,mu_n) lift of the extended Brauer class. The hyperbolic affine curve is an étale K(pi,1), so s_V pulls that lift back to H2(k,mu_n)=Br(k)[n]. Independence of the Pic(V)/n ambiguity follows from the Chern-class vanishing established in D.23 (equivalently, local point/cusp pullbacks and Brauer–Hasse–Noether). Global reciprocity gives the corresponding canonical dual-character test. At an ordinary local point x_v≠a, the local section lifts to a k_v-point of V above x_v, and evaluation is beta_{a,chi}(x_v). If x_v=a, a rational point of the fibre forces chi_v=0, so any separately chosen new tangent has zero pairing with chi_v. At an old cusp, the evaluation is the existing cuspidal leading-term evaluation, as in D.27. Thus this method, whenever its cover exists, proves an actual missing reciprocity test rather than the existence of an arbitrary torus-fibre value.

It does **not** by itself prove the restricted-product condition for all translated Kummer classes. At most it proves that, for this fixed chi, its local symbol vanishes almost everywhere and its invariant sum is zero. The finite ramification support of the pulled-back global Brauer class can depend on chi and on V.

## 3. A genuine point section already obstructs universal residue killing

Take k=Q, U=P1−{0,1,infinity}, s=s_3, a=2, and chi the quadratic character of Q(i)/Q. Every finite étale neighbourhood V→U carrying s_3 has a Q-rational point over3: the section fixes a geometric point of the finite fibre at3. Its real point lifts the path from3 to2 inside the real interval (1,infinity). A finite étale morphism induces a finite topological covering on real smooth loci, so the lifted path ends at a real point above2.

Consequently at least one closed residue field k(y) above2 has a real embedding. It cannot contain Q(i), so Res_{k(y)/Q}(chi)≠0. No accessible neighbourhood kills chi at every point of the fibre. Equivalently, an ordinary real path from2 to3 produces an étale path fixed by complex conjugation, giving

\[
 s_3(c)=\gamma s_2(c)\gamma^{-1},\qquad\chi(c)\ne0.
\]

This is precisely a nonempty intersection in (1). The example does not refute the desired reciprocity: the actual canonical value at the point3 is 3−2=1, so its pairing with every character is zero. It refutes only the proposed assertion that every canonical test can always be supplied by a finite étale neighbourhood that kills its residue everywhere. Its obstruction is already present for a known geometric section.

The same argument works over a number field with a real place whenever the two rational points lie in the same real connected component and chi is nontrivial on that place's complex conjugation. Passing to a totally imaginary field or restricting to even characters removes this particular obstruction, but does not prove the compact separation condition (1).

## 4. What the full local fixed-group theorem does and does not provide

Claim C.7h implies a strong separation over a local cyclotomic subgroup with nonzero tame ell-image: two distinct ordinary local points cannot give conjugate restricted sections there, because their two primitive valuations would violate the RNS uniqueness theorem. This concerns a whole specified subgroup. Condition(1) quantifies over individual global Galois elements with a prescribed finite character value. Their closed cyclic groups may have no nonzero tame inertia image at any selected local place. C.7h therefore cannot be substituted directly for (1).

In particular, absence of one common conjugator for whole sections does not rule out distinct conjugators for individual elements. The compactness argument above identifies exactly the stronger assertion needed; it does not manufacture it from section injectivity.

## Sources and exact reliance

- Finite covers, fibre stabilizers and subgroup correspondence are the standard finite étale Galois-category equivalence used throughout the paper, supplied SGA1.
- Colliot-Thélène–Skorobogatov, opened author draft, Proposition3.6.1 and §1.4.1: residues, restriction with ramification index1, and extension across a regular curve point. The arrow here is the cohomological residue, negative Witt as fixed in D.27.
- The real-cover obstruction has an elementary finite-cover proof above; it does not require the full real section conjecture. The real section comparison already opened for D.22 gives the equivalent conjugation formulation.
- C.7h's exact RNS uniqueness hypothesis is retained, rather than replaced by cyclotomic openness or a statement about a single arbitrary global element.

**Remaining bridge:** produce restricted-product admissibility for the new canonical values and all their reciprocity tests by an argument that does not assert the false universal residue-killing condition. No such argument is established here.
