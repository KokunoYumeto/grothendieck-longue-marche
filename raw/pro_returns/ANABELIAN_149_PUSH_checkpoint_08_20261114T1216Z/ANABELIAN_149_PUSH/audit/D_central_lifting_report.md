# D.23–D.24 and the unresolved canonical-local compatibility step

## Established result and review

D.23 proves central lifting for every finite reduced divisor of a hyperbolic curve over a number field, using the local theorem checked in D.19, the exact Borne–Emsalem–Stix torsor comparison, and Brauer–Hasse–Noether. The lifts can be chosen compatibly as the divisor varies at one fixed base curve, by choosing one lift per closed point and taking fibre products. This is stronger than separate finite-rank solvability and does not require compactness of the sets of splittings.

D.24 refutes the automatic compatibility of arbitrary central-lift choices under finite étale neighbourhoods. The explicit cover t=z², with lower point4 and upper point2, realizes the norm Q(i)/Q at the deleted point−1. The lower twist κ(3) does not lift, because every norm has even3-adic valuation. Root independently read the complete proof, the exact Borne–Emsalem–Stix passages and the geometric realization, and approved both results. The residue certificate was run; its output is retained separately.

The source audit confines the failure to Saïdi's old arXiv-v1 invariant-surjectivity argument and distinguishes the later finite-H1 hypothesis. Neither D.24 nor the further audit below proves nonexistence of a compatible system, or refutes a section conjecture.

## 1. A torus-fibre point is not the canonical punctured-curve point

Let V=P1_Q−{0,1,∞}, let a∈Q−{0,1}, and put W=V−{a}. Since Pic(V)=0, the diagonal line-bundle torsor F_a is trivial over V. More explicitly, write t for the coordinate. The restriction of O(Δ) to {a}×V is O_V(a); multiplication by t−a trivializes this line bundle. Under the resulting trivialization F_a≅V×Gm, the canonical map W→F_a is

\[
 t\longmapsto (t,(t-a)^{-1}).
\]

The inverse occurs because F_a parametrizes isomorphisms O_V(a)→O_V. Reversing the torus coordinate gives t−a instead and changes no conclusion.

Consequently a central lift of a section s of V is a pair

\[
 (s,A_a),\qquad A_a\in H^1(Q,\widehat Z(1))=\widehat{Q^\times}.
\]

If s_v is the section of a point x_v∈V(Q_v), a lift represented by an ordinary element b_v∈Q_v^× is the section of the torus-fibre point (x_v,b_v). This includes b_v=1 and supplies no relation between b_v and x_v. For the lift to be the image of the **canonical point of W**, when x_v≠a, one needs instead

\[
 A_a|_{Q_v}=\kappa_v((x_v-a)^{-1}).
\]

At x_v=a, a lift through the newly punctured curve would be cuspidal and carries a tangential Kummer class; D.6 does not assert that this class is represented by an actual rational tangent vector. This qualification is necessary when stating any translated-value criterion.

Thus D.23 cannot be upgraded to the desired canonical-local lifting statement merely by requiring a torus-fibre lift to be locally point-theoretic. At finite modulus n the latter requirement imposes no condition at all on the difference class for a quasi-trivial torus T: Hilbert90 and the Kummer sequence identify H1(Q_v,T[n]) with T(Q_v)/nT(Q_v). The canonical translated value is a **prescribed** local class, not the assertion that some local torus point exists.

## 2. What restricted-ramification compactness would require

For a finite Galois module A and a fixed finite set S containing its ramification, H1(G_{k,S},A) is finite. One can see this directly after passing to a finite extension that trivializes A: continuous cocycles correspond to bounded-degree extensions unramified outside a fixed finite set, of which there are finitely many by Hermite–Minkowski and the bounded local discriminant for a fixed degree. Therefore an inverse system of **nonempty finite sets of S-admissible splittings**, stable under transition, would have an inverse limit. A compatible family of homomorphisms to the finite quotients would then give a continuous section.

The missing assertion is not this compactness lemma. It is the simultaneous nonemptiness, with the required canonical local values, of a compatible system with a finite ramification bound at every fixed lower quotient. Passing to a different finite extension to kill each Kummer class separately does not prove that assertion. Changing the neighbourhood changes its residue fields, its norm maps and potentially its ramification requirements.

There is also a concrete integral obstruction not seen by the field-level Brauer argument. For R=O_{E,S}, with n invertible on R, the étale Kummer sequence gives

\[
 0\longrightarrow\operatorname{Pic}(R)/n
   \longrightarrow H^2(R,\mu_n)
   \longrightarrow H^2(R,G_m)[n]\longrightarrow0.
\]

The first term dies after restriction to E, and also after restriction to every local DVR, because those Picard groups vanish. Hence a Chern class may be generically zero and zero at every integral local place while remaining nonzero on Spec R. Brauer–Hasse–Noether over E does not eliminate that term. This is a statement about étale cohomology of the integral base; no unjustified identification with a particular pro-ell arithmetic K(pi,1) quotient is used.

### Fully checked example: E=Q(sqrt(−35)), n=2, R=O_E[1/2]

Set ω=(1+sqrt(−35))/2. Then O_E=Z[ω], the discriminant is−35, and

\[
 \omega^2-\omega+9=0,\qquad
 N(a+b\omega)=a^2+ab+9b^2.
\]

The polynomial x²−x+9 is irreducible modulo2, so2 is inert and the unique prime above2 is the principal ideal(2). Modulo3 it factors as x(x−1), so

\[
 (3)=\mathfrak p\mathfrak q,\quad
 \mathfrak p=(3,\omega),\quad
 \mathfrak q=(3,\omega-1).
\]

The element ω has norm9, is divisible by p, and is not divisible by q; hence (ω)=p². The ideal p is not principal: there is no element of norm3. Indeed,

\[
 a^2+ab+9b^2=(a+b/2)^2+35b^2/4;
\]

if b≠0 this is at least35/4>3, and if b=0 it is the square a².

Minkowski's bound is (2/π)sqrt(35)<4. Every ideal class therefore has a representative of norm1,2 or3. There is no ideal of norm2, and the two ideals of norm3 are p and q, whose classes are inverses. Since [p]²=1 and [p]≠1, the full class group is C2. Localizing at2 kills only the class of the principal prime(2), so

\[
 \operatorname{Pic}(R)=C_2.
\]

The nontrivial class has nonzero image in Pic(R)/2, hence gives a nonzero class in H2(R,μ2) that is zero over E and over every local DVR of R. The proof uses no unproved class-number computation. Milne's primary *Algebraic Number Theory*, v3.08, Theorem4.3, supplies exactly the displayed Minkowski bound; the relevant Kummer sequence is Stacks Tag03PK, Lemma59.28.1 and its displayed long exact sequence. Both were opened.

This example does **not** show that the obstruction arising from any specified geometric section equals this class. It shows exactly why generic and integral-local vanishing alone do not establish the integral splitting needed by the proposed compactness argument. At each fixed field one can enlarge S to kill its class group. No uniform enlargement for all neighbourhood residue fields has been proved.

## 3. Canonical translated Kummer classes and finite support

For a fixed local point family (x_v), the relevant stronger condition is the existence, for each rational a, of a global completed class A_a whose localizations equal κ_v(x_v−a) wherever x_v is finite and different from a, with separately specified tangential classes at equality places. The divisor-product construction of D.23 puts no such restrictions on the independently chosen A_a.

The exact published implication available is Stix's rank-one torus calculation (arXiv:1203.3236v3, Proposition2):

\[
 \widehat{Q^\times}\cap G_m(A_Q)_\bullet=Q^\times.
\]

Here **Gm-adeles** require ordinary nonzero local values and units at all but finitely many places. This is stronger than lying in the product of the local completions, and stronger than having unit valuations on a density-one set. His Corollary5 then characterizes noncuspidal Selmer sections of a hyperbolic curve by finite support; Corollary6 applies the torus calculation when a nonconstant global unit is available. These exact source passages were reread in the supplied arXiv LaTeX.

For example, if some A_a has ordinary nonzero local values at every finite place, is a unit cofinitely often, and agrees with x_v−a whenever x_v≠a, then A_a=q∈Q^×. The local point family is supported on {a,a+q} (and on any separately retained pole point, if such points were allowed in the formulation). This is a finite set of rational points. Stix's finite-support argument then applies to the original hyperbolic section. The arithmetic equality follows directly as well from Q^×={±1}×⊕_p p^Z: ordinary valuation coordinates with finite support force the completed class to be an actual rational number.

Two caveats prevent applying this statement from D.6 alone. First, infinitely many nonzero valuations divisible by increasingly large integers are compatible with a global completed class; D.20 explicitly exhibits them even with ordinary values at every finite place. Second, at a newly created cusp the tangential class need not have ordinary integer valuation. Neither caveat is removed by the fact that each finite-level local class has a representative in Q_v^×.

I have not proved that the simultaneous conditions for **all** rational a force such a cofinite bound for any one a, nor found a primary theorem with that exact implication. The published torus and finite-support results take the required adelicity as an input. Treating it as a consequence of separate local point sections would be circular at this point.

## 4. A precise uncompleted finite-cover route

Choosing the squareclasses of finitely many A_a gives a multiquadratic cover with equations y_a²=(t−a)/c_a. Canonical local values give local points on the twists. With sufficiently many branch points its smooth completion has genus at least2. This observation does not produce a global section of that completion: a central section of the punctured-line quotient does not lift to the full fundamental group of the branched cover. The cover is ramified over points interior to V, so it is not one of the finite étale neighbourhoods to which the original section already lifts. Applying D.19 or Faltings at this step would therefore require the very missing lifting assertion. No conclusion is drawn from this route.

## Sources opened for this supplementary audit

- Borne–Emsalem–Stix, *Lifting Galois sections along torsors*, arXiv:1301.4429v2, Definition2.1, Propositions3.1,3.4,3.5,4.2,4.4, Lemma4.5.
- Stix, *On the birational section conjecture with local conditions*, supplied arXiv:1203.3236v3 LaTeX and the reopened primary PDF <https://arxiv.org/pdf/1203.3236>, Section2.3, Proposition2; Section3, Corollaries5–7. The guessed author-PDF URL failed, but both the supplied source and the actual arXiv PDF were read.
- Milne, *Algebraic Number Theory*, v3.08,19July2020, Theorem4.3 and its proof; <https://www.jmilne.org/math/CourseNotes/ANT.pdf>.
- Stacks Project, Tag03PK, Lemma59.28.1 and the following Kummer long exact sequence; <https://stacks.math.columbia.edu/tag/03PK>.

The simultaneous translated-value condition does at least imply the precise **asymptotic integrality** of Stix's Definition8: for any fixed modulus n and any fixed rational boundary divisor, all but finitely many ordinary contact orders with that boundary are divisible by n. Indeed each A_a modulo n is represented by a rational number with finite valuation support. This is a divisibility statement, not eventual vanishing of the contact orders. The distinction is realized by the factorial valuations of D.20.

The supplementary route audit is not a new result-register claim. Its proved elementary obstructions and its unresolved global compatibility step are kept separate. A separate candidate, `audit/D_density_all_sections_candidate.md`, investigates whether D.6 and the Legendre dichotomy remove the birational-liftability hypothesis from density-one integrality specifically for the three-punctured line.
