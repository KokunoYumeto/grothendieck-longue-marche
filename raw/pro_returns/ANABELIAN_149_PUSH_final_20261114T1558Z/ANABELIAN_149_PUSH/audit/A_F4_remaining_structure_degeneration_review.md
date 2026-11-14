# Independent review: structure of the remaining ordinary F4 pair

Reviewer: degeneration agent. Date: 14 November 2026.

Reviewed candidate: audit/A_F4_remaining_structure_candidate.md, Sections 1–6. Reviewed code: A_F4_remaining_structure.py, A_F4_remaining_frobenius_packets.py, A_F4_remaining_mixed_packets.py, and their stated output files. No candidate or integrated A source was edited.

**Conclusion: the stated structural results and the finite-support packet bounds pass.** In particular, the absolute-simplicity and full rational geometric-endomorphism arguments are valid, and the exclusion of odd-degree geometric isogenies from the particular split-branch theta-seven comparison curve is valid. These are method obstructions; they do not decide A1 for either remaining curve.

An independent certificate was written and run:

- code/A_F4_remaining_structure_degeneration.py
- code/A_F4_remaining_structure_degeneration.json

It passed direct counts over F4, F16, F256, all 18 cyclotomic exclusions, and 30 modular Frobenius identities. It uses its own binary finite-field arithmetic and direct polynomial arithmetic in \(\mathbf Z[X]/(P)\), rather than importing the packet search or its matrix inverse.

## 1. Counts and the actual Frobenius

The independent count uses the displayed descended model
\[
v^2+v=z+\alpha^2(z+1)/(z^2+z+\alpha).
\]
At a rational simple pole there is one point on the smooth normalization; at every other affine coordinate there are two points exactly when the absolute trace of the right side is zero. Infinity supplies one point. The resulting counts are \(7,15,255\) over F4, F16, F256.

The first two give
\[
P(X)=X^4+2X^3+X^2+8X+16,
\]
and the third agrees with the polynomial's fourth-power trace. The same independent count was made for the quadratic Artin–Schreier twist of \(y^2+y=x+\alpha/x+\alpha^2/(x+1)\), by adding the constant \(\alpha\). It gives the same three counts, confirming the comparison model used in Section 5.

Use of the actual F4 Frobenius, instead of only its square, is appropriate and matters for the integral polynomial annihilator. The proof does not confuse the orders \(\mathbf Z[\pi]\) and \(\mathbf Z[\pi^2]\).

## 2. Absolute simplicity

Modulo three, \(P=\Phi_{10}\), and \(3\) has order four modulo ten. Thus \(P\) is irreducible over \(\mathbf Q\).

Recomputation of the resultant and squarefree reduction gives exactly
\[
64Z^8+80Z^7+108Z^6+7Z^5+26Z^4+7Z^3+108Z^2+80Z+64.
\]
All possible nontrivial Frobenius-root ratios are roots of this polynomial. Its degree-eight bound is justified by writing the roots as \(a,4/a,b,4/b\): four cross ratios each occur twice, while the four reciprocal-pair ratios are the remaining possibilities. No unstated numerical root comparison is used.

The list of integers with Euler totient at most eight is exhaustive and all eighteen cyclotomic gcds were recomputed as one. If a nontrivial ratio were a root of unity of order \(n\), its minimal cyclotomic polynomial would divide the ratio polynomial and have degree at most eight, a contradiction.

For every \(m>0\), the four conjugates of \(\pi^m\) are consequently distinct. The minimal polynomial of \(\pi^m\) remains irreducible of degree four. A proper nonzero geometric abelian subvariety descends to a finite extension, and its rational Tate module would give a proper invariant factor of that finite-extension characteristic polynomial. Hence none exists.

## 3. Full rational geometric endomorphisms and the CM field

The relevant source was independently opened at
https://www.jmilne.org/math/CourseNotes/AV.pdf:
Chapter I, Theorem 10.15, printed p.49 / PDF p.54. The theorem gives the **tensor** injection
\[
\operatorname{Hom}(A,B)\otimes\mathbf Z_\ell
\hookrightarrow\operatorname{Hom}(T_\ell A,T_\ell B),
\]
not merely injectivity of the uncompleted group. This distinction is essential for the dimension argument and is correctly handled in the candidate.

Every geometric endomorphism is defined over a finite extension and commutes with \(\pi^m\) for some \(m\). Since \(\pi^m\) is regular semisimple of degree four on a four-dimensional rational Tate module, its centralizer has dimension four and equals \(\mathbf Q_\ell[\pi^m]=\mathbf Q_\ell[\pi]\). All geometric endomorphisms therefore lie in this same centralizer. Their rational algebra contains \(\mathbf Q(\pi)\), already four-dimensional, so equality follows. No Tate-surjectivity theorem or maximal-order assertion is required.

The calculation with \(s=\pi+4/\pi\) is exact:
\[
s^2+2s-7=0,\qquad
\mathbf Q(\pi)=\mathbf Q\bigl(\sqrt2,\sqrt{-7+4\sqrt2}\bigr).
\]
Both real conjugates of \(-7+4\sqrt2\) are negative, so this is a CM field. Their product is \(17\). If the field were normal, it would contain the other square root and therefore \(\sqrt{17}\); together with \(\sqrt2\) these would generate a real degree-four subfield, forcing the entire field to be real. This contradicts the negative discriminants. Thus the non-Galois assertion is also valid.

Geometric simplicity excludes an elliptic quotient. A nonconstant map to an abelian variety of two-rank zero would produce a nonzero abelian image of the Jacobian. Simplicity makes that image isogenous to the ordinary Jacobian, which cannot have two-rank zero. The claim concerns the original curve only and does not exclude targets after an admissible cover.

## 4. Odd-degree isogeny obstruction

The comparison is specifically with the quadratic twist of the known theta-seven curve. Both Frobenius operators satisfy the same irreducible polynomial \(P\).

The equality \(\mathbf Q(\pi^m)=\mathbf Q(\pi)\) gives a polynomial \(R_m\in\mathbf Q[X]\) with
\[
R_m(\pi^m)=\pi.
\]
The corresponding identity holds in \(\mathbf Q[X]/(P)\), so the **same polynomial** works for the Frobenius of both varieties. If a geometric homomorphism \(f\) is defined over \(\mathbf F_{4^m}\), then
\[
f\pi_A^m=\pi_B^m f
\quad\Longrightarrow\quad
f\pi_A=\pi_Bf.
\]
This justifies using original-F4 Frobenius equivariance even for a homomorphism initially defined only over an extension.

For the split-branch comparison curve, all three nonzero geometric two-torsion classes are fixed. For the remaining curve, Frobenius swaps the two finite ramification points and fixes infinity, so its action on the three nonzero classes is a transposition, with exactly one fixed class. The independent code checked the corresponding permutations; the identification with the three ramification differences is the explicit description for an ordinary genus-two Artin–Schreier curve with three poles.

An odd-degree isogeny induces an isomorphism on geometric two-torsion. Such an isomorphism cannot intertwine these different Frobenius actions. Therefore every geometric isogeny between these particular two Jacobians has even degree. The argument does not claim that no other isogenous Jacobian could supply useful geometry.

The asserted rational two-primary groups follow as well: both Jacobian groups have order \(P(1)=28\); one has exactly one nonzero rational point killed by two and hence a cyclic subgroup of order four, while the other has three and hence \(C_2\times C_2\).

## 5. Automorphisms

The normalized coefficients \((1,9,14)\) are pairwise distinct. An automorphism of a genus-two curve descends through its unique hyperelliptic map. It must permute its three branch points, hence is one of the six normalized Möbius transformations. These permute the three simple-pole coefficients. A rational Artin–Schreier change cannot alter those simple-pole coefficients: a nonconstant correction has an even-order pole in its square-plus-itself. Thus no nonidentity permutation preserves the triple. The remaining kernel is exactly the hyperelliptic involution. The claimed absence of an odd-order geometric Galois quotient follows.

## 6. Prime-primary and mixed-primary bounds

I reread the fixed-field arguments in A.C2.12 and A.C2.14. They apply to the theta divisor defined over F4, including mixed primary support. They do not require semisimplicity of Frobenius modulo \(\ell\).

Each displayed certificate is an equality in
\[
(\mathbf Z/\ell^{e+1}\mathbf Z)[X]/(P).
\]
Since \(P\) is monic, lifting the polynomial reduction gives an integral endomorphism identity
\[
(\pi^m-1)B(\pi)=\ell^e(1+\ell R(\pi)).
\]
On geometric \(\ell\)-primary torsion, the second factor is invertible by its finite geometric series at each level. Hence a \(\pi^m\)-fixed point is killed by \(\ell^e\). This is a uniform bound on the entire specified primary packet, not an inference from a finite enumeration of rational points.

The independent quotient-polynomial arithmetic verified all twenty single-prime certificates and all ten component certificates for the five mixed-support rows. The mixed fixed-field lemma must be applied first to the whole theta point; then its primary components are fixed and the component exponent bounds apply. The candidate uses that order of reasoning.

The negative geometric theta tests are explicitly linked to the saved complete Hankel results at the resulting finite exponents. This review checked those references and the modular certificates; it did not rerun every long Hankel scan. The existing all-minors/unit-gcd certificates remain the basis for those finite-level exclusions. In particular, individual prime-primary emptiness is not silently substituted for mixed-support emptiness.

The stated exclusions concern only the displayed primes or prime supports. The unexcluded bounds at \(17^2,41^2,47^2,71^2\), and the separately investigated theta-73 locus, are not turned into universal conclusions. No claim of A1 failure is supported or made.

