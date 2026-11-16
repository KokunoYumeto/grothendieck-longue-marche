# Final independent audit of the actual local integral phase (B.40)

## Audited outcome

The actual local extension class has the following thirteen Smith coordinates in the fixed B.35–B.36 normalization:

\[
(0,0,1,2,0;\ 2,5,9,6,9,24;\ 57,36)=b+6h_9.
\]

In particular

\[
\lambda_{81}(\eta(F_2))=57\pmod{81},
\qquad
\lambda_{\mathcal J}(\eta(F_2))=19\pmod{27}.
\]

I independently reconstructed the actual geometric displacements from every Schreier word, using fibre composition rather than chronological concatenation; recomputed their complete 54-element outer action; used a different strict symplectic CM intertwiner; used our exact invariant lattice; and inverted Frobenius by DVR elimination instead of B's polynomial. The result is uniquely candidate 5 among all 27 B.36 possibilities.

The finite group of B.39 is therefore a specified intrinsic detector whose requested statistic is now evaluated. This does not claim to have written equations for its cover or the entire quadratic Frobenius matrix. Nor does it rescue the inherited metabelian order-(3^{30}\) test: B.38 proves that test kills the entire mixed coefficient module and cannot evaluate the relevant refinement.

## 1. The actual index-nine cover and marking

The geometric morphism

\[
[3]: E-E[3]\longrightarrow E-O
\]

is finite étale of degree nine in characteristic zero and in characteristic two. On the complex once-punctured torus, choose chronological generators (a,b\) whose commutator

\[
\delta=aba^{-1}b^{-1}
\]

is the positive peripheral path in the cut fundamental parallelogram. The subgroup for the cover is

\[
N=\ker\bigl(\langle a,b\rangle\to(\mathbf Z/3)^2\bigr).
\]

The Schreier transversal (a^i b^j\), (0\le i,j<3\), gives exactly ten nontrivial generators. Every rewritten generator is checked back against its original word. The peripheral words are the conjugates of \(\delta\), and the transfer vectors are obtained by summing the directed edges over all nine cosets. These are actual covering-space constructions, not free rank-ten automorphisms chosen to fit a linear representation.

The ordered deck coordinates are those of the actual three-torsion points (A_0,A_2\). The previously verified Weil pairing is \(e_3(A_0,A_2)=\zeta_3\). The ordered eight nonzero points are

\[
(1,0),(2,2),(0,1),(2,0),(1,1),(0,2),(2,1),(1,2).
\]

The unique compatible boundary orientation is the positive one. With its peripheral columns (E\), the exact matrix

\[
P=\left(\frac{(u_{\rm tr},v_{\rm tr})-EU}{3},\ E\right)
\]

is integral and has determinant (-1\). Its inverse identifies both transfer vectors literally with the B.24 vectors (u,v\), and both deck transformations literally with the B.24 integral translation matrices. This checks the integral gluing, not only the compact or residual representation.

The positive boundary Tate frame and the compact Weil pairing fix the symplectic normalization. The full ten-dimensional determinant (-1\) of the chosen Schreier-to-gluing matrix is unrelated to a reversal of the compact polarization.

## 2. The CM and involution words represent the actual geometry

Start with

\[
\sigma_0(a)=b,\qquad\sigma_0(b)=b^{-1}a^{-1}.
\]

Its homology matrix is the required (R_3\), and

\[
\sigma_0(\delta)=(ab)^{-1}\delta(ab).
\]

Conjugating by (ab\) gives the explicitly boundary-fixing representative

\[
\sigma(a)=aba^{-1},\qquad\sigma(b)=b^{-1}a^{-1}.
\]

It fixes \(\delta\) literally and has exactly the required action on the nine cusp classes. The analogous involution words in the script fix \(\delta\) and have compact matrix (-I\).

The geometric identification is justified by the once-punctured-torus mapping-class theorem: its orientation-preserving mapping class is determined by the homology matrix. Equivalently, the kernel of \(\operatorname{Aut}(F_2)\to\operatorname{GL}_2(\mathbf Z)\) is inner. Thus the chosen words represent the actual CM and involution outer actions on the parent torus. Among their nine possible lifts to the cover, the one fixing the origin cusp is singled out. Any remaining parent inner discrepancy has trivial deck class, hence lies in (N\), and disappears after quotienting by \(\operatorname{ad}_wV\).

This theorem was opened in the **published** text of Farb and Margalit, *A Primer on Mapping Class Groups* (Princeton University Press, 2012), §2.2.4, pp. 54–55, and §8.2.7, pp. 234–235. The front matter and the displayed isomorphism were checked in the academic-mirror PDF:

<https://euclid.nmu.edu/~joshthom/teaching/ma589/farbmarg.pdf>

The relevant web source references are `turn323view0` and `turn324view0`, with the once-punctured-torus proof at lines 1787–1800 and the outer-free-group identification at lines 8011–8015. B adds the bibliography key `BFarbMargalit2012`. The earlier suggestion “§8.3” was corrected: §8.3 starts on p. 236.

## 3. The necessary chronological-to-fibre sign

This is essential to the numerical result and is fixed independently of candidate matching. A chronological path \(\gamma\) followed by \(\delta\) transports a fibre by

\[
M_{\gamma\delta}=M_\delta\circ M_\gamma.
\]

Hence the comparison from chronological words to the étale group \(\operatorname{Aut}(\text{fibre})\), whose multiplication is composition, reverses words. A positive loop of \(\mathbf G_m\) sends a chosen root to that root times \(\zeta\); it therefore preserves the chosen sign on degree-one Tate vectors.

The reversal map is an anti-map of the tensor algebra, identity on generators. On ordinary Lie degree (n\) it acts as \((-1)^{n-1}\). It is therefore identity on degree one, negative on degree two, and positive on degree three. If a chronological word automorphism has quadratic term \(B\), its actual fibre-composition quadratic term is \(-B\).

Equivalently the formal pure bracket \([u,v]\) maps to minus the actual pure bracket, while its cubic displacement maps with positive sign. The actual geometric displacement of the actual bracket is therefore

\[
t_{\rm actual}=-t_{\rm chronological}.
\]

The independent script implements this by **reversing each of the forty complete Schreier image words and recomputing its class-two logarithm**, rather than multiplying the final answer by a selected sign. It checks unchanged linear terms and negated quadratic terms for every word.

There is also a direct tangent check. The uncorrected \(\sigma_0\) has cube one, and

\[
(ab)\sigma_0(ab)\sigma_0^2(ab)=\delta,
\]

so the corrected chronological lift has cube \(\operatorname{Int}(\delta)\). In fibre composition its cube is conjugation by the inverse peripheral transport. This is the based automorphism obtained from the positive (120^\circ\) tangent path (p\) and the formula \(p^{-1}\sigma_*p\). It agrees with the tangent-rescaling convention used in B.35–B.36.

For comparison, the B.36 path identity itself keeps its positive Kummer sign. If \(\alpha=p^{-1}F(p)\), then

\[
TF=\operatorname{Int}(\alpha)FT,
\]

and writing \(T\omega=\omega+t\), \(F\omega=\chi(\omega+\eta)\) gives

\[
(T-I)\eta=[\alpha,w]+(\chi^{-1}F-I)t.
\]

On an ordinary division cover, (p\) sends the base lift to a division point (q\), so \(p^{-1}F(p)=Fq-q\), the positive Kummer cocycle. No sign was changed in those already proved local equations.

## 4. The geometric extension and comparison independence

After quotienting by the primitive inner image, the group acts on the genuine extension

\[
0\to Q\to\overline L_w(-1)\to\mathbf Z_3\to0,
\qquad Q=A(-1)/\operatorname{ad}_wV.
\]

The actual geometric displacements close under all 54 group relations. If they are denoted (t_a\), then

\[
h=-\frac1{54}\sum_{a\in\mathcal A}t_a
\]

satisfies (t_a=(a-I)h\). The code stores the integral numerator \(h_{27}=27h=-\tfrac12\sum t_a\), so averaging requires only division by the unit two in the actual computation.

The local quaternion basis has compatible CM matrix (S\), whereas the Schreier basis has (R_3\). A strict symplectic intertwiner satisfies \(SB=BR_3\), \(B\equiv I\pmod3\), \(\det B=1\), with full fixed-boundary gluing matrix

\[
K(B)=\begin{pmatrix}B&0\\U(B-I)/3&I\end{pmatrix}.
\]

Any two such intertwiners differ by the norm-one strict CM centralizer. Put \(\mathcal O=\mathbf Z_3[\zeta_3]\). The centralizer is

\[
\{c\in1+3\mathcal O:N(c)=1\}.
\]

The convergent logarithm identifies this with
\(3(\zeta_3-\zeta_3^2)\mathbf Z_3\). For

\[
\epsilon=\frac{1+3\zeta_3}{1+3\zeta_3^2},
\]

one has

\[
\frac{\log\epsilon}{3(\zeta_3-\zeta_3^2)}\equiv1\pmod3.
\]

Indeed the first logarithm term gives one, terms divisible by three in the series index vanish, and every other term after the first is divisible by three. Thus \(\epsilon\) topologically generates the entire strict norm-one centralizer.

Its full fixed-boundary action is the actual arithmetic coefficient action of \(\tau\bar\tau^{-1}\), whose cyclotomic multiplier is one. This actual arithmetic lift commutes with \(\mathcal A\) over (K\), so it fixes the actual geometric extension class in \(H^1(\mathcal A,Q)\), as does its closure. Therefore the transported geometric class is independent of the unknown strict symplectic comparison.

Only the norm-one, fixed-boundary assertion is used. An optional broader statement about an arbitrary norm requires simultaneous scaling of the boundary Tate frame and is not part of this proof.

As an independent numerical check, B chose an intertwiner from first column \((1,0)\); my verifier used \((1,3)\), followed by its determinant-one normalization. Both give the same unique candidate.

## 5. Exact comparison with the actual local candidate set

Let (R_4\) act on (Q\), and put (D=R_4-I\). For a local arithmetic representative (e=\eta(F_4)\), the commuting actual geometric and arithmetic actions give

\[
(a-I)e=D t_a.
\]

The positive-weight eigenvalues make (D\) rationally invertible. Thus (y=D^{-1}e\) has the same geometric connecting class as (h\) if and only if

\[
y-h\in Q+(Q\otimes\mathbf Q_3)^{\mathcal A}.
\tag{2}
\]

The invariant lattice is primitive and was independently constructed over the exact integers in `c_geometric_extension_test.py`, with the determinant-two minor and four-entry residual separator recorded in the preceding audit.

The complete B.36 list has 27 elements, written (b+s h_3+t h_9\), (s\bmod3\), (t\bmod9\). Every actual local class occurs in that list, across all three possible integral Kummer comparisons. Applying (2) to all of them leaves exactly one, (s=0,t=6\). A matching class need not be asserted geometrically realizable merely because it passes a linear test: existence of the actual curve supplies a class in the exhaustive list, and uniqueness under this necessary condition identifies it.

B inverts (D\) by an exact annihilating polynomial. I instead performed a full DVR Smith elimination, transporting both right-hand sides and column operations. The resulting valuations are

\[
0^{122},1^{70},2^{26},3^{82},4^{20}.
\]

All entries of (81D^{-1}e\) are integral. Working modulo \(3^{10}\) and with maximum pivot valuation four determines their reduction modulo \(3^6\), more than enough for (2) modulo 81. The intertwiner's gluing division loses one digit, still far above the four digits needed. This verifies that no finite-precision kernel is mistaken for an exact invariant or solution.

The actual (mathbf Q_2\) candidates are compared after restriction to (mathbf F_4\). Restriction is injective on these three-primary local cohomology groups because corestriction followed by restriction multiplies by two on the source. Thus the unique selected thirteen-coordinate (mathbf Q_2\) vector is the actual full local class, not merely a class modulo an unexamined quadratic-extension kernel.

## 6. Exact deliverables and scope

Independent replay files are now promoted into the deliverable:

- `deliverable/code/c_geometric_extension_test.py`, `.out`, `.json`, `_matrices.npz`;
- `deliverable/code/c_geometric_phase_verify.py`, `.out`, `.json`, `_matrices.npz`;
- `deliverable/code/c_residual_class_two_detector.py`, `.out`, `.json`, `_matrices.npz`.

The phase verifier reconstructs the geometry from the separately saved `b_elliptic_schreier` words, uses its own invariant basis and different compact intertwiner, and gives the exact final vector above. All promoted scripts were rerun after their paths were changed; they complete successfully.

This selects the integral phase among the three formal refinements of B.38. It is separate from the ((\mathbf F_3)^3\) abelian-path kernel of LM6 E.39, which was a different object, and it is not a computation in the inherited metabelian quotient that annihilates \(\mathcal J\). The corrected intrinsic detector and actual geometric extension provide the required extra arithmetic information.
