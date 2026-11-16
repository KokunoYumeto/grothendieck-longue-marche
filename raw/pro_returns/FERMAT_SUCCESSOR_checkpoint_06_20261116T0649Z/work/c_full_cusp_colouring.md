# Full pro-three cusp colouring: arithmetic construction and exact scope

**Date:** 2026-11-16. **Authoring agent:** Part C auditor, in collaboration with the root and Part B auditors. **Status:** B.10(b) and the corresponding rational-cusp implications of B.10(c) are refuted for the actual full pro-three group. The cross-prime question B.10(a) and the full infinite-ramification equivalence B.11 remain open.

## Outcome table

| Statement | Outcome | Exact contribution |
|---|---|---|
| B.29 | Proved | The actual local pro-three groups at the two primes above seven form the free pro-three product (G_{\mathbf Q(\zeta_3),\{3,7\}}^{(3)}). |
| B.30 | Refuted | Ramification at seven does not force a global rational-cusp packet: actual local packets at a non-rational (K)-cusp and its conjugate descend to full pro-three sections over (mathbf Q). |
| B.33 | Proved | Complete section coordinates for whole cocycles unramified outside (3,7), with all local-class fibres; every member of B.30 fails local geometry at three. |
| B.34 | Refuted | The same false global implication fails even when the local seven-adic cusp colour is the rational base cusp. An explicit condition on the local path produces an infinite-order compact class. |
| Task B.10(a) | Open | The constructions have only one possible ramified rational prime away from three and do not test equality of colours at distinct rational primes. |
| Task B.11, full pro-three form | Open | A new local factor cannot simply be adjoined; its actual Frobenius word is constrained. No full infinitely ramified counterexample is asserted. |

Manuscript files are `deliverable/sections/B_cusp_counterexample.tex` (B.29--B.30) and `deliverable/sections/B_seven_classification.tex` (B.33--B.34). Rows are `work/c_B29_B30_rows.json`, including all four statements. New bibliography entries are `work/c_b_references.bib`. The exact finite certificate is `deliverable/code/c_seven_free_product.py` and its independently run output `deliverable/code/c_seven_free_product.out`.

## 1. Why this is a full pro-three result

The arithmetic group is not replaced by a guessed presentation. Put (K=\mathbf Q(\zeta)), (lambda=1-zeta), (pi=2-zeta), and (arpi=3+zeta). Thus (piarpi=7), and the relevant set has the three primes ((lambda),(pi),(arpi)). Start with the actual maps from the two local maximal pro-three groups to (P_S=G_{K,S}^{(3)}). These maps are not presumed injective. The proof establishes that their induced map from their free pro-three product is an isomorphism.

The ring of Eisenstein integers is norm Euclidean, and after inverting (21) its cubic Kummer space has basis (zeta,lambda,pi,arpi). At the two primes above seven the residues of (zeta) are respectively (2,4), and those of (lambda) are (6,4). With the fixed global identification (1\mapstozeta), the cubic residue symbols give Frobenius rows ((2,0)) and ((2,2)) on the first two basis elements. The inertia rows on the last two elements are an identity matrix. The complete restriction matrix therefore has block form

\[
\begin{pmatrix}2&0&*&*\\2&2&*&*\\0&0&1&0\\0&0&0&1\end{pmatrix}.
\]

Its determinant is one modulo three regardless of the actual upper-right entries. This is the precise point at which the dependence of a Frobenius lift on other arithmetic generators is retained: the entries are not set equal to zero; their irrelevance to this determinant is proved.

The second-cohomology argument is equally essential. For (X=\operatorname{Spec}\mathcal O_K[1/21]), the maximal-pro-three comparison map (H^2(P_S,\mathbf F_3)\to H^2_{\rm et}(X,\mathbf F_3)) is injective. Schmidt states this directly before Proposition 2.1, and the text also explains the underlying vanishing of first cohomology on the universal pro-three cover. This uses no unproved (K(\pi,1)) assumption. Since (operatorname{Pic}(X)=0), the étale Kummer sequence identifies the target with (operatorname{Br}(X)[3]). The regular integral scheme Brauer group injects into that of (K). Outside the three allowed primes its local invariants vanish because the class extends over the completed local integer ring, which is henselian with finite residue field. The two seven-adic invariants determine the remaining three-adic invariant by their zero sum. Hence restriction to the two local groups detects (H^2(P_S,\mathbf F_3)).

The isomorphism on (H^1) makes the actual free-product map surjective. Its five-term sequence and the injection on (H^2) make the invariant first cohomology of its kernel vanish. A nontrivial kernel would have nontrivial image in a finite three-group quotient. Its Frattini quotient has nonzero coinvariants under that finite three-group, producing precisely a forbidden invariant character. Thus the kernel is trivial. This is a proof of the entire pro-three group identity, not an inference from finite nilpotent tests.

The local tame presentation is (\langle t,F\mid FtF^{-1}=t^7\rangle_{\rm pro-3}). Wild inertia is pro-seven, and the tame arithmetic action by seven factors through a pro-three unramified quotient because (7\equiv1\pmod3). The resulting exact presentation agrees with the actual arithmetic local maps just proved to embed.

## 2. The genuine nonlinear geometric action

The curve is the plus cubic with all nine coordinate cusps removed, and the base point is the rational unit tangent at (O=[0:-1:1]). Its actual geometric pro-three group is the invariant open subgroup

\[
N=\ker(F_2^{(3)}\to(\mathbf Z/3)^2),
\]

of rank ten. The based action is the restriction of the genuine tripod action, using the coherent rational Puiseux lift (X/Z=-s), (t=s^3), (Y/Z=-(1-s^3)^{1/3}). This specific choice matters: the proof needs an action, not merely an outer class. Over (K), the action on the tripod's Frattini quotient is trivial because the mod-three cyclotomic scalar is one. The corresponding IA automorphism kernel is pro-three; restricting its actual compact arithmetic image to (N) preserves that property. The action is unramified outside three by based good-reduction specialization. B.27 already establishes these facts in detail and was independently audited in `work/c_lifting_audit_B27.md`.

Let (c) be an actual complex conjugation. The maximal-pro-three kernel of (G_{K,S}) is characteristic and hence normal in (G_{\mathbf Q,\{3,7,\infty\}}). The latter has the actual quotient (Gamma_S=P_S\rtimes\langle c\rangle), split by that complex conjugation. Choose conjugate prolongations above the two seven-adic primes. Then (c) exchanges the two actual local factors literally. No nonexistent rational local decomposition group or abstractly assembled arithmetic product is used.

## 3. Non-rational local cusp counterexample

Choose (P=[0:-zeta:1]), which is a (K)-cusp and a (mathbf Q_7)-cusp in the embedding (zeta\equiv2\pmod7). On the first local factor choose the actual local tangential section at (P), using a fixed geometric path from the original tangent and twisting by (a\kappa_3(7)). Its graph in (N\rtimes\rho_N(G_{\mathbf Q_7})) has pro-three target, so it factors through the actual maximal pro-three local quotient. On the second factor take its complex conjugate. The free-product universal property extends the two local graph sections uniquely. That uniqueness gives (c)-equivariance, so the cocycle extends to (Gamma_S) with value one at (c).

Finally pull back the geometric cocycle along (G_{\mathbf Q}\toGamma_S), while retaining (g) itself as the arithmetic coordinate: (s(g)=(z(r(g)),g)). This is an actual section of (N\rtimes G_{\mathbf Q}). Saying that the section itself factors through (Gamma_S) would be a typing error; only its geometric cocycle and action do.

For a positive seven-adic tame generator, the abelian inertia coordinate is (ae_P). The entire boundary lattice

\[
W=\mathbf Z_3(1)[D]/\mathbf Z_3(1)\sum_{d\in D}e_d
\]

injects into (N^{\rm ab}). Any two distinct cusp vectors are linearly independent in (W). Since local inertia acts trivially on the abelianization, a geometric coboundary vanishes on inertia. Thus nonzero (ae_P) cannot equal the inertia coordinate (be_C) of a rational cusp (C). This proves noncuspidality and distinguishes all the parameters (a\in\mathbf Z_3). The obstruction survives every closed normal stable quotient with (J\subseteq N'), including the intrinsic metabelian quotient and the exact marked quotient (N/\overline{\gamma_3(I_Q)}), where (I_Q) is the closed normal closure of the marked rational peripheral generator.

No use is made of the earlier run's asserted classification of all local ramified packets. The local sections in the example are actual tangential sections by construction.

## 4. Complete finite-set coordinates

B.33 goes beyond the example. Every whole cocycle unramified outside (3,7) factors through (Gamma_S) by the same pro-three graph argument. If (b=z(c)), then (c(b)=b^{-1}), and the unique square root in the procyclic pro-three group generated by (b) explicitly normalizes its value at (c) to one. Remaining conjugations lie exactly in (Q^c).

For (Q=N/J), set (Phi=
ho_Q(F)). Every normalized section is determined by two local values (u=z(t)), (v=z(F)), with exactly one equation

\[
v\Phi(u)v^{-1}=u^7.
\]

This condition is sufficient as well as necessary, by the full local pro-three presentation. The entire section space modulo geometric conjugacy is this closed subset of (Q^2) modulo the explicit action

\[
w\cdot(u,v)=(wuw^{-1},wv\Phi(w)^{-1}),\qquad w\in Q^c.
\]

For a given local conjugacy class with stabilizer (S_\xi), its global fibre is (Q^c\backslash Q/S_\xi). In the full free group (N), these local stabilizers are trivial. The integral lower central graded pieces are free Hall Lie lattices. Frobenius on the first degree has compact characteristic polynomial (X^2+X+7) and boundary eigenvalues seven; on every positive Lie degree all eigenvalues have complex absolute value greater than one. Inner section twists act trivially on the graded pieces. Torsion-freeness then excludes every fixed vector, and residual nilpotence excludes a fixed element of (N). The full-group fibre is therefore (N^c\backslash N). This last simplification is not claimed for arbitrary quotients, whose graded pieces could have torsion.

## 5. Rational local colour is also insufficient

B.34 supplies a second family that avoids any interpretation requiring a rational local colour. Let (T=T_3E), choose (h\in T) with (c(h)\ne h), and use **every** element of the nonempty compact-abelianization fibre (mathcal N_h=\{n\in N:\operatorname{pr}_E(n)=h\}). In B.28's integral basis, (C_E=\left(\begin{smallmatrix}1&-1\\0&-1\end{smallmatrix}\right)), and (h=(0,1)^t) works. Surjectivity of compact abelianization proves the fibre is nonempty; no individual finite word is falsely claimed to have been numerically computed.

Conjugate the local base-cusp packet (a\kappa_3(7)) by (n), use the conjugate packet on the second local factor, and normalize at (c). Its local seven-adic cusp class remains the rational cusp (O). Its compact cocycle has (k(F)=(1-Phi_E)h), (k(t)=0), and (k(c)=0), independently of (a). If this cocycle were a coboundary over (\mathbf Q_3), a vector (m) would satisfy (c(m)=m) and ((1-Phi_E)m=(1-Phi_E)h). But (det(1-Phi_E)=9\ne0), so (m=h), a contradiction. The compact cohomology class has infinite order. All rational cusp packets have compact class killed by three, so none of these global sections is cuspidal. For (a\ne0) they ramify at seven with rational colour (O).

The same argument identifies the role of paths in the exact fibres. A local geometric conjugacy class need not determine a global geometric conjugacy class: the conjugator at the conjugate prime is forced to be its complex conjugate, while the global representative is normalized at (c). Treating local conjugacy as equality of actual graph maps would lose this obstruction.

## 6. Failure of local geometry at three

All members of B.30 share one compact cocycle, because the varying tangent twists are peripheral. That cocycle is unramified outside three and at seven is the Kummer class of (P-O). The nine coordinate cusps are the full (E[3]): the tangent line has divisor (3P), so differences from (O) are killed by three, and the nine points are distinct. They reduce distinctly at seven, where the exact point count is nine. Thus local three-primary Kummer theory distinguishes all nine. The compact class at seven is different from the image of every rational point of (E), of which A.10 gives exactly the three rational cusps.

If this compact cocycle were locally Kummer at three, it would be in the Tate Selmer group: at all other finite primes an unramified class is locally Kummer by good reduction, and at the real place odd-primary cohomology vanishes. A.10 and A.14 identify this Selmer group with the finite rational three-primary group. That contradicts the seven-adic class. Every B.30 member, including (a=0), therefore fails local geometry at three.

For B.34 the compact class has infinite order, whereas the same Tate Selmer group is finite. It too fails the local condition at three. These conclusions hold in every quotient retaining the abelianization. The counterexamples are consequently not claimed to refute a Selmer-section theorem; they refute exactly the unrestricted ramified-section implications asked in B.10.

## 7. What fails in the direct multi-prime extension

With (m) allowed (K)-primes away from the unique three-adic prime, Kummer theory gives (\dim H^1=m+2). Freely adjoining all their actual local tame factors would instead give dimension (2m). These match only for (m=2). Adding one new allowed prime adds one global Kummer generator but a full local factor would add two local generators. At the level of (H^2), the new prime also adds one Brauer coordinate; this agrees with an extra generator and an extra relation, not with a new independent Frobenius generator.

Thus the present free-product isomorphism cannot be iterated to add a second rational ramified prime. One would have to solve that prime's actual Frobenius word in the existing global generators and new inertia generators. A Chebotarev condition in each finite quotient is not, by itself, an exact infinite-level solution of that word constraint. Similarly, one cannot add infinitely many independent local cusp twists and claim continuity: their inertia values must tend to one and all their Frobenius constraints must hold in the full group. Neither B.10(a) nor full B.11 has been resolved by the present argument.

## 8. Opened sources and independently executed checks

1. Schmidt, A. (2007). *Rings of integers of type (K(\pi,1)).* Documenta Mathematica, 12, 441--471. DOI: 10.4171/DM/230. The author PDF at <https://www.mathi.uni-heidelberg.de/~schmidt/papers/kpi1.pdf> was opened; section 2, author-version p.4, explicitly supplies the degree-two injection before Proposition 2.1. Proposition 2.3 was also read, but full comparison is not needed for B.29. EMS Press publication metadata was independently opened.
2. Milne, J. S. (2020). *Class field theory*, version 4.03. <https://www.jmilne.org/math/CourseNotes/CFT.pdf>. The author source was opened and VIII, Theorem 4.2, including its exact Brauer invariant sequence, read. The shared B bibliography supplies `BMilneCFT2020`.
3. Colliot-Thélène, J.-L., & Skorobogatov, A. N. (2019). *The Brauer--Grothendieck group*, author manuscript, October31. <https://www.imo.universite-paris-saclay.fr/~jean-louis.colliot-thelene/BGgroup_book.pdf>. Theorems 3.5.4 and 3.4.2 and their proofs were opened for the generic-point injection and the henselian local Brauer group, respectively. The exact opened version is recorded, without pretending to have checked different later pagination.
4. SGA1's exact prime-to-residue-characteristic specialization is the already verified `BSGA1` input, as applied in B.27. The new construction independently checked that the base tangent and actual restriction to the invariant open subgroup are the ones to which that argument applies.

The standard-library Python certificate independently checks the Eisenstein identities and norms, both cubic residue rows, all (81) possible unspecified upper-right blocks, primitive rank-two independence of all (36) distinct boundary pairs, the full cubic point count over (\mathbf F_7), the non-fixed compact vector (h), and (det(1-Phi_E)=9). All assertions passed. The program explicitly states that it checks the finite inputs and does not replace the cohomological full-group proof.

No claim of priority is made. The complete local packet classification from LM7 E.61/E.66/E.71 and the general finite/infinite presentation of LM7 E.73 are not used as proof authorities. Their exact context is retained; the finite arithmetic group needed here was independently proved from primary inputs.

## 9. Attempted global embedding-problem extension and its precise failure

I also checked whether a general solvable embedding-problem theorem could turn the finite-set construction into a compatible infinitely ramified section. The opened primary author manuscript is Jarden and Ramiharimanana (2018), *Solving embedding problems with bounded ramification*, <https://www.math.tau.ac.il/~jarden/Articles/paper111.pdf>; the publisher metadata gives *Proceedings of the London Mathematical Society*, 117(1), 149--191, DOI 10.1112/plms.12126. Theorem A, author pp.3--4, gives solvability with prescribed finitely many local solutions under, among other hypotheses, \(\gcd(|H|,|\mu(L)|)=1\), where \(H\) is the embedding kernel and \(L\) is the fixed quotient field. This is also the exact roots-of-unity hypothesis retained from the quoted Neukirch theorem.

For the relevant nontrivial three-primary refinements of the actual arithmetic action, the quotient field contains \(\mathbf Q(\zeta_3)\). Thus three divides both the embedding-kernel order and the number of roots of unity in the quotient field. The stated theorem does not apply. This is a failed hypothesis, not evidence that the desired embedding problem has no solution. Nor does an abstract finite embedding theorem automatically retain actual local cusp geometry at every newly ramified prime, or produce an inverse system whose ramification coordinates have the required convergence. No infinite construction is claimed from that route.
