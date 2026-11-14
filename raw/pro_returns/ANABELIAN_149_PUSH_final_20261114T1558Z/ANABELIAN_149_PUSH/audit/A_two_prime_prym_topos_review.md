# Independent review: two-prime primitive Pryms

**Reviewed file:** audit/A_two_prime_prym_candidate.md, Sections 1–8, as present on 14 November 2026.

**Conclusion:** the stated theorem and its degree-fifteen and \(3^a5^b\) consequences pass this independent review. No proof gap was found. The conclusion is conditional on the stated primitive theta-orbit hypothesis; this does not establish that hypothesis on every genus-two curve.

The review also reread the actual integrated A.3, A.C2.5 and A.C2.8, rather than assuming their content from the candidate's summaries.

## 1. Degree and intermediate-field checks

Over an algebraically closed characteristic-two field, an inseparable rational function is a square. A function of degree at most four that is inseparable therefore gives a function of degree at most two. The hyperellipticity exclusion consequently removes the inseparable cases before the tetragonal argument.

For a free cyclic group \(G\) of odd order \(n\), a \(G\)-invariant rational subfield of index \(d<n\) is impossible. If the action on the rational quotient is trivial, every fibre is invariant. If it is nontrivial, its odd cyclic image in \(\operatorname{PGL}_2\) has a fixed point, giving an invariant fibre. Each geometric orbit in that fibre has size \(n\), with constant multiplicity along the orbit. Its total degree must therefore be divisible by \(n\), contradicting \(0<d<n\). This argument does not require the action on the rational quotient to be faithful.

The hyperelliptic case is correctly reduced to this observation: its unique involution is centralized by \(G\), so the degree-two subfield is invariant. A degree-three pencil is unique because two distinct index-three rational subfields generate the full field: the degree of their compositum in the full field divides three, and degree three would force the subfields equal. Castelnuovo–Severi then gives genus at most four. Its uniqueness makes it invariant, which was excluded.

For a degree-four pencil \(k(z)\), noninvariance supplies a distinct conjugate \(k(\delta z)\). If
\[
F=k(z,\delta z),\qquad e=[k(D):F],
\]
then \(e\mid4\). The possibilities \(e=4\) and \(e=1\) give, respectively, equal pencils and genus at most nine. Since \(g(D)=n+1\ge16\), one has \(e=2\). Both rational subfields have index two in \(F\), and generate it, so the smooth curve with field \(F\) has genus at most one. Genus zero would make \(D\) hyperelliptic. Thus it is elliptic, and the extension \(k(D)/F\) is separable quadratic because it is intermediate in the previously established separable degree-four extension.

Two distinct elliptic subfields of index two would generate the full field, and Castelnuovo–Severi gives genus at most \(2+2+1=5\). Thus the bielliptic involution is unique and is centralized by every automorphism, including \(G\). No unjustified cancellation between two degree-four maps is used.

## 2. Wild ramification and the two-rank bound

The degree-two elliptic quotient has different degree \(2g(D)-2=2n\). It must ramify. Its ramification points form a nonempty \(G\)-stable finite set, and freeness makes its cardinality \(r\) a positive multiple of \(n\). At every ramification point the lower groups \(G_0,G_1\) both have order two, so the different exponent is at least two. Consequently \(2r\le2n\), forcing \(r=n\). The ramified Deuring–Shafarevich formula then gives
\[
f(D)-1=2(f(E)-1)+n,
\]
hence \(f(D)\ge n-1\).

The candidate's alternative proof of this lower bound is valid independently of that formula. The odd cyclic action on \(E\) is faithful, since its kernel on the quotient is contained in the quadratic deck group. A nonidentity element fixing a point of \(E\) would act trivially on its fibre of at most two geometric points: an odd-order permutation of such a fibre is trivial. It would then fix a point of \(D\), contradicting freeness. Every nonidentity element therefore acts without fixed points on \(E\).

Writing an elliptic automorphism as \(T_bu\) with \(u\) fixing the origin shows that a fixed-point-free automorphism must be a translation. If \(u\ne1\), the nonzero endomorphism \(1-u\) is surjective and solves the fixed-point equation. Hence the images \(b_i\) of the ramification orbit satisfy \(n(b_i-b_0)=0\). Pullback along the ramified quadratic map gives
\[
2n[P_i-P_0]=0.
\]
Any nonempty \(\mathbf F_2\)-relation among the \(n[P_i-P_0]\) would give a rational function whose divisor is supported at the ramification points and has an odd coefficient \(n\) at some \(P_i\). The divisor is invariant under the involution; the quotient of the conjugate function by the function is constant and squares to one, so equals one in characteristic two. The function descends to \(E\), forcing all those ramification valuations to be even. This contradiction proves \(n-1\) independent geometric two-torsion points.

Thus the key geometric lemma is supported by both a published formula and an elementary divisor argument.

## 3. Primitive characters and the full Tate module

For \(n=\ell^a m^b\), the two deck elements
\[
a_0=\sigma^{n/\ell},\qquad b_0=\sigma^{n/m}
\]
have orders \(\ell,m\). On the character of index \(i\), the scalar of
\[
A=(1-a_0)(1-b_0)
\]
is nonzero exactly when \(\ell\nmid i\) and \(m\nmid i\). Since \(n\) has exactly these two prime divisors, this is precisely the primitive-character condition. There is no omitted prime-power conductor case.

The theta-orbit hypothesis kills the Frobenius-stable parts of all primitive character spaces, by the explicit A.C2.5 calculation. It follows that
\[
f(D)\le f(C)+n-1-\varphi(n)\le n+1-\varphi(n)<n-1,
\]
because \(n\ge15\) and \(\varphi(n)\ge8\). No vanishing of the smaller-conductor parts is asserted.

The passage from geometric two-torsion to all two-primary torsion is justified integrally. A finite unramified extension of \(\mathbf Z_2\) contains all \(n\)-th roots of unity, and division by \(n\) is allowed there. The odd-order character idempotents therefore decompose the finite free étale Tate module integrally. Every summand has rank equal to the dimension of its reduction. Primitive summands have rank zero; on each nonprimitive summand one factor of \(A\) is identically zero. Thus \(A\) is identically zero on the Tate module and on all its finite quotients.

Duality between étale cohomology and geometric Tate modules may invert the character index. This does not change primitivity, so the conclusion is unaffected. Adding this sentence in the final text would make the duality convention explicit, but its absence is not a gap.

## 4. Section collisions and distinct divisors

A.3 applies after a finite extension defining the cyclic cover, its deck action and a chosen lift. Odd torsion is finite étale, so the defining torsion data can in fact be made rational over a finite separable extension. Equality of the original section classes is preserved, and A.3 supplies the corresponding rational lift with two-primary divisor difference.

Applying \(A\) to that difference gives the displayed degree-four divisor relation. The four group elements \(1,a_0,b_0,a_0b_0\) are distinct because their two nontrivial cyclic subgroups have coprime orders. Freeness gives four distinct points in each fibre. The two fibres are disjoint because the original points on \(C\) differ. Consequently the eight points in the relation are distinct, and the principal divisor has four simple zeros and four simple poles. Its function has degree four and is separable, since a square would have even valuation everywhere. This contradicts the geometric lemma.

The same argument survives finite extensions and forms retaining the geometric hypothesis. Injectivity for an open subcurve follows by the map to its proper compactification. It does not require a new assertion about nonproper Jacobians.

## 5. Arithmetic corollaries and scope

Symmetry of theta supplies both indices \(1\) and \(-1\). If these generate all primitive residues under doubling, every primitive orbit meets theta. The two displayed degree-fifteen orbits are complete and disjoint.

The orders of two modulo \(3^a\) and \(5^b\) follow from the stated valuation-one initial cases and the elementary prime-power lifting calculation. Their greatest common divisor is two, so two has index two in the product unit group. Minus one does not lie in its cyclic subgroup: the exponent must be odd modulo three but \(2\bmod4\) modulo five. Hence the full unit group is generated for all \(3^a5^b\).

Finally the square-class quotient of the unit group of an odd integer with \(r\) distinct prime factors has dimension \(r\) over \(\mathbf F_2\). Two generators force \(r\le2\), so the combined prime-power/two-prime theorem really covers every odd order under the advertised generator condition. It does not claim that all odd orders satisfy that condition.

## Sources independently opened

- Poonen, B. (2007). *Gonality of modular curves in characteristic p*. Primary author version, Proposition 2.1, author p.3: https://math.mit.edu/~poonen/papers/gonality.pdf. The proposition explicitly assumes a perfect field, generated compositum, and the two exact field degrees used above. The modular assertions are not used.
- Crew, R. M. (1984). *Étale p-covers in characteristic p*. *Compositio Mathematica, 52*(1), 31–45. Corollary 1.8, pp.35–36: https://www.numdam.org/item/CM_1984__52_1_31_0.pdf. The statement explicitly allows ramification. The candidate's independent two-torsion proof was checked in full, so the needed lower bound does not depend on any ambiguity in OCR of the displayed formula.
- Integrated sections/A.tex, A.3; sections/A_char2_theta.tex, A.C2.5; sections/A_char2_deck.tex, A.C2.8.

This review checks the general proof. It does not independently certify the separate exact-order-fifteen point program, which remains the responsibility of its own checked certificate.
