# Independent audit of E.105

**Verdict: PASS.** The entire statement, proof, three program sources, and cited source passages were read. All three copied programs completed with exit zero; every complete stdout and JSON file is byte-identical to the author's output. No field was excluded from comparison. No mathematical correction is requested.

Audited theorem source SHA256:
19aa0c26bf1745a49a8c823d3cc6a218fd904478035aa93c389ca22ef7dee0de.

The actual execution, copied sources and outputs, hashes, and complete comparisons are retained in rebuild.py, rebuild.out, rebuild.json, and copied/. The sole source-metadata amendment requested is the page index for Wickelgren's Proposition 7: PDF pages 13–14, rather than 2. Proposition 26 and Remark 28 are on PDF pages 27–28.

## Actual origin and central lift

I checked the four-coset identity directly from (E103.8). For lifts of \(g,h\), multiplication gives
\[
b_i(ef)=g b_i(f)+b_{h\cdot i}(e).
\]
Summation gives the crossed-homomorphism identity for \(B\), and \(B(a)=4a\). The expression \((-B(e)/4)e\) is independent of the lift and multiplicative. On each clopen coset the chosen \(H\)-section supplies a continuous lift, so the formula is continuous, including in the rational arithmetic pushout.

E.105 applies this construction to the pullback of the class-two arithmetic extension over a fixed abelian section. Its kernel is \(\Lambda^2 A\), with the actual exterior-square Galois action: an inner conjugation from the geometric abelian part is trivial on this central layer. Thus the hypothesis of the averaging formula holds.

For changed representatives \(e'_i=a_i e_i\), multiplication gives
\[
B'(e)-B(e)=g\sum_i a_i-\sum_i a_i.
\]
Writing \(q=\sum_i a_i/4\) proves
\[
s'_0=\operatorname{Int}(q)s_0,\qquad
s'_R=\operatorname{Int}(q-\iota r(q))s_R.
\]
Conjugation by the inverse of a lift of the specified vector returns the original abelian origin. The asserted change under a root coboundary has the same sign.

## Framed cusp paths and rational two-primary correction

The twelve formal branches and tangent-line functions have the stated fourth-order leading coefficients. Their leading-value ratios give all 121 retained values in \(\mathbb Q(\zeta_8)\), including each root-of-unity exponent. The simultaneous equations \(mu_m=z_d\), \(4u_m=v_m\) determine the odd division points uniquely and compatibly. Their proper images are fixed four-torsion points, so the proper Kummer cocycle is literally zero.

The endpoint tuple has entry \(+1\) at \(d\) and \(-1\) at every other non-origin cusp. On a degree-zero cusp divisor its character is \((-1)^{m_d+m_O}\), exactly the two endpoint signs of the regularized local differences. Its odd divisions are fixed. For rational two-primary coefficients its Kummer cocycle is \(d(\sigma_d/2)\), where \(\sigma_d\) is zero at \(d\) and one at the other non-origin coordinates.

The equality \(4u_n-v_n=b_{d,n}\) independently gives
\[
\kappa(z_d)=N_{\bullet d}\kappa_2/8+
d\bigl(b_d/4+K_{\bullet d}/32\bigr).
\]
Adding the endpoint tuple gives the full path correction
\[
b_d/4+K_{\bullet d}/32+\sigma_d/2.
\]
The last term is explicitly retained; its fourth power is one, so the fourth-power frame data alone do not recover it. Multiplying the return path by this vector subtracts its coboundary, directly from \(p\,g(p)^{-1}\). At the origin the root-of-unity cocycle is \(d(1/8,0)\). Simultaneous conjugation by \(\iota(1/8,0)\) therefore gives precisely the asserted toric-zero marking and preserves the displayed action in the transported coordinates.

The diagonal subgroup in the rational arithmetic pushout is closed and normal. The first factor commutes with it because geometric elements act by their inner automorphisms, and the arithmetic factor preserves it. Its intersection with the first factor is trivial. This checks the source and kernel maps, including their topology.

## Action and the complete toric image

The Hall-to-BCH conversion has the stated integral inverse when two is invertible. Expanding \(u_d^{-1}d_d^{\chi_g}u_d\) gives the sign \(\chi_g\kappa_2(g)e_d\wedge v_d\). The central part of the conjugator cancels. The displayed peripheral subgroup is genuinely stable over \(H\).

The coset average restricts to \(a(g)v\) with the sign in (E105.16). The proposed geometric cocycle
\[
(a(g)v,\tfrac12a(g)^2L(v))
\]
satisfies the full crossed-homomorphism equation under the actual action: the cross term is \(\chi_g a(g)a(h)L(v)\). It supplies the section of the central pullback.

After this origin change the action is \(L_v=L+v\wedge-\), and the exact frame matrix gives \(L_v\iota=0\). If \(dk=\alpha\cup\beta\), the central cochain
\[
z=-\bigl(k+\alpha\beta/2\bigr)\omega
\]
has differential equal to the negative BCH defect, since \(d(\alpha\beta)=-(\alpha\cup\beta+\beta\cup\alpha)\). Averaging the resulting central pullback retains the desired global abelian input.

For necessity, the actual morphism \(t=-(x/z)^4,\ 1-t=-(y/z)^4\) multiplies the two abelian coordinates by four and their central cup by sixteen. Its \(-1\) root correction is zero at odd coefficients and the stated coboundary at rational two-primary coefficients. The target path conjugator lies in the commutator subgroup, so its class-two action is pure cyclotomic. Thus sixteen times the cup vanishes; sixteen is invertible in exactly the coefficient rings of the theorem. Both image inclusions follow through these actual maps.

## Unrestricted continuous cup criterion

For odd \(\ell\ge5\), the Kummer/character calculation over \(\mathbb Q(\mu_\ell)\) selects the \(\omega^{-1}\) component. The torsion-free unit quotient is even under complex conjugation, and its odd part comes from \(\mu_\ell\), of character \(\omega\). Ribet's theorem in the Herbrand direction at \(k=2\) eliminates the required class component. The finite-module Euler factor is one for the even twist. This proves the asserted finite base \(H^2\) vanishing; the real-place formula and finiteness provide the other terms. The \(\ell=3\) base calculation is E.32.

The order of limits is correct. At each finite coefficient level, the removed-prime supports are taken in direct sum first. Their two-term complexes have surjective coefficient transitions. Their derived inverse limit is the actual restricted-sequence complex \([\,\mathcal R\xrightarrow{d}\mathcal R\,]\), with \(d(z)_q=(q-1)z_q\). The adjacent base terms vanish with the stated finite-group Mittag-Leffler argument. No closure is inserted in the image.

I independently checked the tame relation in the rank-two BCH pullback. Its central defect is
\[
q((q-1)w+A'_qb_q-B'_qa_q).
\]
The inertia twist divides by \(q\). Replacing actual Frobenius values by the specified residue logarithms changes the result by \(d\) of a restricted sequence: the discrepancies divided by \(q-1\) are uniformly integral, and each term is multiplied by \(a_q\) or \(b_q\). The changes of roots, cocycle representatives, and tame Frobenius give precisely the asserted formulas. This proves both the integrality and convergence tests.

For rational coefficients, every continuous cochain has compact bounded image and hence one common denominator. The displayed cochain-level scalar-extension map is therefore an isomorphism in every degree. Applying it after the derived localization construction gives \(c_0(\mathbb Q_\ell)\), with the finite-\(S\) rational base vanishings supplied by Hain–Matsumoto, including \(\ell=2\). The unique correction must tend to zero. The explicit infinite-support pair has correction \(-1\) at every selected prime, although all finite-level primitives exist; multiplication by a nonzero rational scalar still fails to make it restricted. The stated finite/local failure has the claimed completed source.

## Fibres and scope

The six determinant maps and their section columns check the exterior-square decomposition, of total rank136. There are no invariant vectors in \(A\), by restriction to the cusp splitting field for its torus and the actual proper isogeny for the compact factors. Thus the abelian conjugator aligning two sections is unique; its BCH lift leaves exactly the central coboundary ambiguity. Compactness proves the integral topological assertion. A finite injective linear matrix with a continuous left inverse proves the rational one.

The theorem computes the fixed origin and complete two-coordinate toric image. Its remaining cohomology factors and handle-action targets are explicitly retained. It makes no claim of an integral two-primary quartic section or a complete classification over all rank-seventeen abelian inputs.

## Primary passages independently opened

- Ribet, Main Theorem(1.1), printed p151/PDF index1, visually opened. The exact \(k=2\) Herbrand implication and character convention check. URL: https://math.berkeley.edu/~ribet/Articles/invent_34.pdf ; retrievals turn890view0, turn891view8.
- Hain–Matsumoto, Appendix B, Theorem B.1, Proposition B.2, Lemma B.3 with full proof, Theorem B.4 including its two-primary paragraph, and Lemma B.5 with full proof. URL: https://arxiv.org/pdf/math/0006158 ; retrievals turn894view1, turn894view2, turn896view0, turn896view1.
- Milne, Arithmetic Duality Theorems, I.4.10(c), I.4.15, I.5.1; II.0.1(f) with proof, II.1.7(b) with its valuation/Kummer derivation, and II.2.9 with proof. URL: https://math.stanford.edu/~conrad/BSDseminar/refs/MilneADT.pdf ; retrievals turn891view4, turn894view5, turn894view6, turn896view4, turn896view5, turn898view1, turn900view0, turn900view2, turn900view4.
- Jannsen, Proposition1.6 and Theorem2.2 with full proofs. URL: https://epub.uni-regensburg.de/26684/1/jannsen12.pdf ; retrievals turn896view2, turn896view3, turn898view0.
- Wickelgren, Proposition7 with the full explicit cochain proof, Proposition26, and Remark28. URL: https://sites.math.duke.edu/~kgw/papers/3NilP1.pdf ; retrievals turn898view3, turn898view4, turn899view2. The finite-symbol statement is used only in its stated scope.
