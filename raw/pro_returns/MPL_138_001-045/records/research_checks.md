# Explicit comparisons used in the research notes

Prepared after the transcription freeze of 2026-11-17 22:02:50 UTC. These are the transcriber's calculations, with the context leads credited below; they have no effect on the frozen transcription. The accompanying `scripts/research_checks.py` verifies the polynomial identities and the finite enumerations, and writes `records/research_checks.json`. The arguments below supply the mathematical justification beyond those finite checks. No novelty is claimed.

## C1. The function on scan 019 and its quotient map

Put \(D=z^2-z+1\) and \(g=27z^2(z-1)^2/(4D^3)\). Direct substitution gives \(g(1-z)=g(z)=g(1/z)\); the two displayed transformations generate the six transformations permuting \(0,1,\infty\), and the reduced rational function has degree six. Consequently the explicit inclusion \(\mathbb Q(g)\hookrightarrow\mathbb Q(z)\) has degree six and its six displayed automorphisms exhaust that degree. This identifies the fixed field and the quotient map by actual coordinates.

The exact identities are

\[
4D^3-27z^2(z-1)^2=(z+1)^2(2z-1)^2(z-2)^2,
\qquad
g'=-\frac{27z(z-1)(z-2)(z+1)(2z-1)}{4D^4}.
\]

The fibre over zero consists of \(0,1,\infty\), each of multiplicity two; the fibre over one consists of \(-1,1/2,2\), each of multiplicity two; the fibre over infinity consists of the two roots of \(D\), each of multiplicity three. Their ramification contributions are \(3+3+4=10=2\cdot6-2\), exhausting the ramification. This checks the three branch values and the passport \((2^3,2^3,3^2)\) for this particular function. Hua, modernised reading of cote 138, §3, already supplies the corrected factorization; the calculation here makes the comparison with the retained scan-019 expression explicit.

## C2. A finite obstruction to the affine surjectivity question, scan 036

Choose the positive real \(\theta=2^{1/8}\) and \(\zeta=\exp(2\pi i/8)\). In the splitting field \(L=\mathbb Q(\theta,\zeta)\), write an automorphism as

\[
\sigma(\zeta)=\zeta^a,\qquad \sigma(\theta)=\zeta^b\theta,
\qquad a\in\{1,3,5,7\},\quad b\in\mathbb Z/8.
\]

The equality \(\theta^4=\sqrt2=\zeta+\zeta^{-1}\) gives

\[
(-1)^b=\chi_2(a),\qquad
\chi_2(1)=\chi_2(7)=1,\quad \chi_2(3)=\chi_2(5)=-1.
\]

In particular the affine pair \((a,b)=(1,1)\) is excluded. There are sixteen compatible pairs among the thirty-two elements of \(\operatorname{Aff}(\mathbb Z/8)\), with product \((a,b)(c,d)=(ac,ad+b)\). The polynomial \(X^8-2\) is Eisenstein at two, so \([\mathbb Q(\theta):\mathbb Q]=8\). The field \(\mathbb Q(\theta)\) is real, its intersection with \(\mathbb Q(\zeta)\) is contained in the maximal real subfield \(\mathbb Q(\sqrt2)\), and it contains that subfield. Thus \([L:\mathbb Q]=8\cdot4/2=16\), proving that all sixteen compatible pairs occur.

The tower action on \(K(2)\) reduces to this finite action by its eighth coordinate. On \(K(1/2)\), inversion of the chosen root replaces \(b\) by \(-b\) and preserves its parity. The tower image therefore fails surjectivity onto the full affine group. This calculation gives the exact index two at level eight; it does not compute the full tower index. Hua, modernised reading of cote 138, §§3 and 4, “Les fibres au-dessus des milieux de côtés”, supplies the lead involving \(\sqrt2\) and also claims full-tower index two; the latter stronger assertion remains credited to that unreviewed context.

## C3. A fixed-subgroup test of the equivalence on scan 011

Let \(E=D_8=\langle r,s\mid r^4=s^2=1,\ srs=r^{-1}\rangle\), \(K=\langle r^2\rangle\), and \(\Gamma=E/K\simeq C_2^2\). The subgroup \(\Gamma_i=\langle sK\rangle\) is normal in \(\Gamma\), and the section \(\Gamma_i\to E\) sending \(sK\) to \(s\) centralizes \(K\), which is central in \(E\). Its image \(\langle s\rangle\) fails normality in \(E\), because \(rsr^{-1}=r^2s\notin\langle s\rangle\). This is a finite witness for the two precise predicates used at the fixed subgroup on scan 011.

For comparison with a profinite arithmetic quotient, take the actual surjection \(\chi:G_{\mathbb Q}\to\operatorname{Gal}(\mathbb Q(\sqrt2,\sqrt3)/\mathbb Q)\simeq C_2^2\) and form \(E'=D_8\times_{C_2^2}G_{\mathbb Q}\). On \(\chi^{-1}\langle sK\rangle\), the map \(\gamma\mapsto(s^{\epsilon(\gamma)},\gamma)\), where \(\chi(\gamma)=s^{\epsilon(\gamma)}K\), is a continuous section centralizing the kernel \(K\). Conjugation by a lift of \(rK\) again takes \(s\) to \(r^2s\), while the quotient image remains \(sK\), so the section image again fails normality. No geometric realization of this particular extension by a covering in the manuscript is claimed.

Hua, modernised reading of cote 138, §1, “Descendre avec tous ses automorphismes : une extension centrale”, supplies a different route after shrinking the open subgroup. The concrete example records exactly why such a change of subgroup matters to the literal fixed-subgroup sentence; it does not re-prove FLAGGED_149 A9 or resolve FLAGGED_149 ZCF6.

## C4. The factor two in the branch-fibre description, scans 029–030

Let \(M=T^3/\operatorname{diag}T\), let \(\rho_i\) be the class of the corresponding coordinate vector, and let \(Z_i=T\rho_i\). The class of \(\rho_i\) in \(M/2M\) is the designated nonzero element \(i\). Translation by \(\rho_i\) takes the coset \(p_2^{-1}(i)\) to \(p_2^{-1}(0)\), so literal ordinary translation by \(Z_i\) does not preserve that fibre. The affine action \(m:y\mapsto y+2m\) does preserve the fibre, and the quotient \(p_2^{-1}(i)/(2Z_i)\) has stabilizer exactly \(Z_i\) under that action: \(2m\in2Z_i\) is equivalent to \(m\in Z_i\), since \(T\) and the quotient \(M/Z_i\) are torsion-free.

At finite level the equivalent formula sends a lift of the nonzero class in \(\pi_2\) to its class modulo the doubled inertia subgroup. The resulting torsor has deck quotient \(M/Z_i\), agreeing with the branch-fibre inertia calculation. Hua, modernised reading of cote 138, §4, “Les fibres au-dessus des sommets et des centres”, makes this correction; here the translation map and its stabilizer explain its scope. The frozen source still reads \(p_2^{-1}(i)/Z_i\).

There is also an exact interpretation of the source's denominator without changing its letters. The action of the abstract subgroup \(Z_i\) through the left-hand term of the multiplication-by-two sequence is \(z:y\mapsto y+2z\). Its orbit through \(y\) is \(y+2Z_i\). Consequently the identity on the fibre induces a bijection

\[
\bigl(p_2^{-1}(i)/Z_i\bigr)_{z\cdot y=y+2z}
\xrightarrow{\ [y]\mapsto[y]\ }
\bigl(p_2^{-1}(i)/(2Z_i)\bigr)_{t\cdot y=y+t},
\]

and its inverse is the same identity on representatives. Both induced \(M\)-actions use \(y\mapsto y+2m\). The displayed sequence on scan 030 already contains the doubling arrow, so the written denominator can denote the acting subgroup with this action; the need is to specify the orbit convention. Hua's denominator replacement and this action-based reading are thus compared by an actual isomorphism of orbit sets.

## C5. The invariant line at three, scan 034

In \(U=\mathbb F_3^3/\operatorname{diag}\mathbb F_3\), use the basis \([e_0],[e_1]\), so that \([e_2]=-[e_0]-[e_1]\). The cycle \(e_0\mapsto e_1\mapsto e_2\mapsto e_0\) acts by

\[
A=\begin{pmatrix}0&-1\\1&-1\end{pmatrix},\qquad
(A-I)^2=0\pmod3,\qquad
\ker(A-I)=\mathbb F_3(1,-1).
\]

An invariant one-dimensional subspace carries an eigenvalue in \(\mathbb F_3^\times\); the equality \(A^3=I\) forces that eigenvalue to be one, and the displayed kernel is one-dimensional. Thus the invariant line is unique, with nonzero vectors \((1,2)\) and \((2,1)\). The transposition swapping the basis vectors exchanges those two vectors, and multiplication by the cyclotomic value \(\chi_3\in\{1,-1\}\) gives the other sign. On this line the joint action is therefore exactly the product of the permutation sign and \(\chi_3\).

The fibre action in scan 034 is already drawn through multiplication by three: \(m:y\mapsto y+3m\) on \(p_3^{-1}(\omega)\). This agrees with Hua's explanatory formula, and the drawn multiplication map supplies source evidence omitted from any suggestion that the action is wholly unspecified there.

## C6. Cofinal roots and the two point expressions, scans 038–041

There is an explicit inverse pair of morphisms

\[
F:\varprojlim_n\mu_{3n}\longrightarrow\varprojlim_n\mu_n,
\quad (v_n)\longmapsto(v_n^3),
\qquad
G:(u_n)\longmapsto(u_{3n}).
\]

Compatibility gives \(u_{3n}^3=u_n\) and \(v_{3n}^3=v_n\), so \(FG=GF=1\). The compatible system \(v_n=\exp(2\pi i/(3n))\) goes to \(u_n=\exp(2\pi i/n)\). This supplies an exact reindexing interpretation of the scan-038 basis, preserving the source's \(3n\) denominator.

For scan 041 put \(\theta_n=2^{1/n}\) and \(j=\exp(2\pi i/3)\). The first written point, \((\theta_n^{-1}e^{-\pi i/n},\theta_n^{-1}e^{\pi i/n},1)\), satisfies \(x^n+y^n+z^n=-1/2-1/2+1=0\). Substitution of the scan-038 \(\zeta_n=e^{2\pi i/(3n)}\) into the next written expression instead gives \((\bar j+j)/2+1=1/2\). With \(\eta_n=e^{\pi i/n}\), the exact relation is \(\eta_n^2=\zeta_n^3\); it does not make \(\eta_n\) equal to \(\zeta_n\) at the displayed level.

The last inverse-limit expression on scan 041 also uses \(\theta_\infty\) where the preceding finite-level expression uses its inverse. Hua, modernised reading of cote 138, §4, “Trivialisation en alpha, et le transport parallèle”, retains the first coordinates in its modernized account. Both literal expressions and the final inverse discrepancy remain in the frozen transcription and are reading questions in the notes.

## C7. The coordinate map on completed rational units, scans 021–022

The prime-valuation map is the explicit isomorphism
\(\mathbb Q^\times\to\{1,-1\}\times\bigoplus_p\mathbb Z\),
\(q\mapsto(\operatorname{sign}q,(v_p(q))_p)\).
Under reduction modulo each positive integer \(n\), the prime coordinates have finite support. The induced injection

\[
\varprojlim_n\bigoplus_p\mathbb Z/n\hookrightarrow\prod_p\widehat{\mathbb Z}
\]

has image exactly the tuples \((a_p)\) for which each fixed modulus \(n\) leaves only finitely many nonzero residues: compatible finite-support residues give a preimage, and their projections recover the tuple uniquely. The tuple \(a_p=1\) for every prime fails this condition at \(n=2\). For the enumeration \(p_1,p_2,\ldots\), the tuple \(a_{p_i}=i!\) satisfies the condition at every modulus and has infinitely many nonzero coordinates in \(\widehat{\mathbb Z}\). These two concrete tuples exhibit both the restriction inside the product and the enlargement beyond the original direct sum. Hua, modernised reading of cote 138, §3, already identifies this restricted image; these examples explain the actual coordinate morphism without replacing the source's formula.

## C8. Marked automorphisms and the octahedron, scans 028 and 044

For \(C_1\simeq\mathbb P^1_{\overline{\mathbb Q}}\), the forgetful morphism \(\operatorname{Aut}(C_1,\{0,1,\infty\})\hookrightarrow\operatorname{Aut}(C_1)\) is the inclusion of the six fractional-linear transformations permuting the three marked points. The explicit automorphism \(t\mapsto t+2\) lies in the target and sends the marked triple to \(\{2,3,\infty\}\). This tests the unmarked notation in scan 028, equation (13), at the actual first level; Hua's marked-cover interpretation has precisely the displayed forgetful morphism.

For the Fermat map \([x:y:z]\mapsto[-x^n:z^n]\), its degree is \(n^2\). At each of the three marked values it has \(n\) points of ramification index \(n\), yielding
\(2g-2=-2n^2+3n(n-1)=n^2-3n\).
Thus \(g=(n-1)(n-2)/2\), agreeing with the listed values on scan 044. Pulling back the two triangular faces of the three-marked sphere gives \(F=2n^2\), \(E=3n^2\), \(V=3n\); at \(n=2\), these are \((V,E,F)=(6,12,8)\), with four incident faces at each vertex.

The four lifts of the open interval \(0<t<1\) at level two are explicitly \([\epsilon i\sqrt t:\delta i\sqrt{1-t}:1]\), with independent signs \(\epsilon,\delta\in\{1,-1\}\). They connect each of the two vertices over zero to each of the two over one. Coordinate permutations give the same incidence for the other two pairs of colours, producing the graph \(K_{2,2,2}\) with its eight triangular faces. This is the octahedron's coloured triangulation by explicit lifted edges.

At level two the group \(\pi_2\simeq\mathbb F_2^2\) acts by translations on four elements, and \(\mathfrak S_3\simeq\operatorname{GL}_2(\mathbb F_2)\) acts linearly. The explicit affine action \((A,b):v\mapsto Av+b\) is faithful, because its value at zero determines \(b\) and its values on a basis determine \(A\). It has \(4\cdot6=24\) elements, giving every permutation of the four-element set and hence the asserted isomorphism with \(\mathfrak S_4\). This verifies the group calculation within the octahedral claim marked “Sauf erreur”; Hua, modernised reading of cote 138, §5, “L'octaèdre”, already reports this identification.

The deck transformations and coordinate permutations are holomorphic on the conic, preserve its pulled-back triangulation, and preserve its orientation. An oriented automorphism of this connected triangulation is determined by the image of one face and one of its vertices: its cyclic order fixes the other vertices, and continuation across an edge fixes each adjacent face. The eight faces and three cyclic choices give at most twenty-four such automorphisms. The explicit group already has twenty-four, so it is the full oriented automorphism group of this triangulation.

## C9. The exact abelian quotient relevant to the historical question

The covering maps in scans 025–029 give
\(q:\widehat\pi_1(\mathbb P^1_{\overline{\mathbb Q}}\setminus\{0,1,\infty\})\to\varprojlim_n(\mu_n^3/\mu_n)\).
Under the three peripheral generators, \(q\) sends them to the three coordinate classes whose sum is zero; its induced map on abelianization is the displayed equation (14). In the free two-generator presentation, the finite quotient sending \(x\mapsto(12)\) and \(y\mapsto(23)\) sends the commutator to a nonidentity three-cycle, whereas \(q\) sends every commutator to the identity. This explicit quotient comparison locates the information retained by the Fermat tower. It makes no claim about the faithfulness of an unexamined action on every curve or every map, and it leaves the current register's full arithmetic-image questions at their supplied status.

The geometric finite-cover comparison used here is SGA 1, Exposé XII, §5, with the geometric base-change comparison for the curve over \(\overline{\mathbb Q}\): [primary SGA 1 edition](https://arxiv.org/pdf/math/0206203). The complex three-punctured sphere retracts onto two loops, giving the two displayed free generators and their third peripheral inverse product.

## C10. The canonical cocycle quotient at modulus two

On \(\mu_2=\{1,-1\}\), every element of \(G_{\mathbb Q}\) acts trivially. The coboundary map \(u\mapsto(\sigma\mapsto\sigma(u)/u)\) consequently has the one-element image. The canonical quotient \(q:Z^1(G_{\mathbb Q},\mu_2)\to H^1(G_{\mathbb Q},\mu_2)\) is an isomorphism and has trivial kernel.

For the other displayed candidate extension, the projection \(p:H^1(G_{\mathbb Q},\mu_2)\oplus\mathbb Z/2\to H^1(G_{\mathbb Q},\mu_2)\) has kernel \(\{0\}\oplus\mathbb Z/2\). The kernel functor on the groupoid of extensions over this fixed quotient sends an arrow \(f\) to its restriction to the kernel: commutation with the quotient maps gives this restriction, and \(K(f^{-1})K(f)=1=K(f)K(f^{-1})\). The two kernels here have one and two elements, so there is no isomorphism between the displayed extensions over the identified quotient. This argument concerns those explicit maps; it makes no assertion about arbitrary abstract isomorphisms between the underlying infinite groups.

Hua, modernised reading of cote 138, §3, already gives the general coboundary kernel \(\mu_n/\mu_n(\mathbb Q)\). The calculation here is a concrete check of the unfinished source diagram on scan 021 at its first even modulus, credited to that contextual correction.
