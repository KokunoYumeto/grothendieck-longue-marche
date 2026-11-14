# D.38: one mixed Fermat and degree-eight finite action

D.38 proves a simultaneous finite realization of the new mixed Fermat homology data and the recorded degree-eight component of D.33. It constructs an actual generating finite GT0 shadow on their exact fibre product. The new action retains the extra fixed-fibre CM pair and both evaluated compact-cover coordinates. D45 and its source-transport supplement exclude full profinite realization of this recorded action. The prescribed CM pair remains open for a replacement.

The proof is in D_fermat_degree8.tex. Four portable programs, their actual stdout and their full JSON certificates are in code/, using the final stems d_cm_fermat_degree8_module, d_cm_fermat_degree8_image, d_cm_fermat_degree8_joint and d_cm_fermat_degree8_covers. The result and source-evidence rows are in the two companion JSON files.

## The exact common quotient

Use the marked source \(B=C_2*C_3\), its rank-four subgroup \(K\), and D.37's subgroups \(L\subset L_4\). Put

\[
J_{12}=B/[L,L]L^{12},\qquad
E_2=B/[L_4,L_4]L_4^4,\qquad
T_3=B/D_9(K).
\]

D.37 proves that \(E_2\) is the universal relative pro-two quotient of \(J_{12}\) over the retained congruence quotient \(Q\). Since \(T_3\to Q\) has a two-group kernel, the canonical largest common quotient is

\[
C=B/\bigl([L_4,L_4]L_4^4D_9(K)\bigr).
\]

This statement concerns the displayed marked maps from \(B\). The proof derives it from the product of their normal kernels, so the comparison uses both quotient maps explicitly.

The coefficient module \(V=L_4^{\rm ab}/4\) is \((\mathbb Z/4)^{385}\). The image \(G\) of \(K\) in \(E_2\) has class-two exponent-four quotient \(K/L_4\) of order 128. Thus \(G\) has exponent dividing 16, its commutator subgroup has exponent dividing 8, and \(U=\gamma_3G\) lies in the abelian exponent-four module \(V\). If \(I\) is the augmentation ideal for the four actual marked \(K\) generators, the Zassenhaus product gives the exact formula

\[
\operatorname{im}(D_9K\to E_2)=I^6U+2I^2U.
\]

The program computes the full normal closure of the 24 basic triple commutators in the 2304-edge Bass–Serre graph module. It then computes all subsequent augmentation products over \(\mathbb Z/4\). The resulting types are:

| Subgroup | \(C_4\) factors | \(C_2\) factors |
|---|---:|---:|
| \(\gamma_3G\) | 375 | 1 |
| \(\gamma_4G\) | 355 | 11 |
| \(\gamma_5G\) | 316 | 38 |
| \(\gamma_6G\) | 252 | 85 |
| \(\gamma_7G\) | 178 | 134 |
| \(\gamma_8G\) | 106 | 146 |
| \(\gamma_9G\) | 51 | 127 |
| \(\operatorname{im}D_9K\) | 51 | 265 |

Odd pivots and the residual even binary system give the exact integral group types. All four \(K\)-generator actions and the complete \(s,r\) action preserve the computed final module. Consequently

\[
\ker(C\to H_4)\simeq C_4^{69}\oplus C_2^{265},
\qquad |C|=2304\cdot2^{403}=18\cdot2^{410}.
\]

Agent A independently checked the exact Zassenhaus formula before the simultaneous calculation.

## Exact matching and generation

The second program reconstructs D.33's two original long conjugator words without rerunning any earlier solver. Their SHA256 values agree with the retained source certificate; their cusp word has its original 12,921,196 letters. Evaluating those conjugators in \(E_2\) gives the precise target classes in \(C\). Their cusp defect lies in the computed image of \(D_9K\), as required by the quotient map.

The third program solves for two new \(L\)-cycle corrections modulo four. It includes the entire cusp equation, both exact common-conjugator equations modulo the recorded module, and the earlier exact \(G_2\) constraints. Its matrix has 2117 rows and 2938 columns. Unit elimination has rank 1588; the residual binary system has rank 263. The full coefficient-solution torsor is

\[
C_4^{1087}\oplus C_2^{263}.
\]

The first deterministic solution induces a rank-1153 automorphism on \(L^{\rm ab}/2\). Its mod-three correction is exactly the previously verified D.37 correction, so CRT gives a generating \(J_{12}\) automorphism. The corrected cusp word has 669,040 letters and vanishes in all 6912 coordinates modulo 12. Independent substitution checks all 1153 free-kernel basis images.

The new \(J_{12}\) and recorded \(T_3\) conjugators agree exactly in \(C\), with the corresponding module coefficients stored in the certificate. Their automorphisms therefore induce one common automorphism of \(C\), and the product restricts to an automorphism of

\[
\mathcal J
=B/\bigl([L,L]L^{12}\cap D_9K\bigr)
\simeq J_{12}\times_C T_3.
\]

This proves generation in the actual simultaneous finite group.

## The precise retained and replaced actions

Before applying the common Ihara gauge, the \(T_3\) action is exactly D.33's recorded action. The new \(J_{12}\) action replaces D.37's recorded one: the normalized images of both \(s\) and \(r\) differ on 5188 graph coordinates modulo 12 and already differ modulo two. Their normalized projections to the whole \(G_6\) and the whole \(J_3\) agree exactly.

The new displayed \(\beta\) abelianization is \((666,-108)\), giving gauge \(k=-774\). A compatible lift of the conjugator pair to \(F\) can change that abelianization by \(144\mathbb Z^2\). Writing it as \((666+144u,-108+144v)\), the displayed gauge gives

\[
f^{\rm ab}=(144(v-u),144(u-v)).
\]

Both \(x\) and \(y\) have order 144 in the joint quotient. Therefore multiplying \(f\) by \(x^{-144(v-u)}y^{144(v-u)}\) produces an actual commutator word in the same joint finite coset. This proves the required commutator condition for the simultaneous shadow, including the choice of a compatible \(T_3\) lift.

The common gauge changes the \(T_3\) component by the exact inner automorphism

\[
\operatorname{Int}(x^{-774})
=\operatorname{Int}(c_0^{258}).
\]

Its class in D.35's specified cusp-inner quotient is therefore unchanged. The pulled-back normal subgroup of \(B_3\) lies in \(PB_3\), the braid centre maps to one, the cusp order is 288, and \(N_{\rm ord}=144\). Both \(m=0\) hexagons hold. These are the finite-shadow conditions used in D.25 and D.37.

## Both compact-cover maps

The normalized word in the exact \(x,y\) basis has 97,388 letters. Direct Schreier substitutions for the cubic, quartic and cyclic-twelve covers pass, including both compact projection equations. They give cubic Tate4 equal to \(-I\) and quartic Tate3 equal to \(I\).

The exact compact change of basis from D.34's marked \(K\) model to the cubic Schreier model is

\[
B_{\rm c}=\begin{pmatrix}-1&1\\-1&0\end{pmatrix}.
\]

It has determinant one and intertwines the marked deck actions. Because \(D_9K\) maps to \(16K^{\rm ab}\), the simultaneous quotient retains the recorded cubic Tate16 matrix, which is unchanged by the cusp-inner gauge:

\[
\rho_{C_3,16}=
\begin{pmatrix}3&8\\8&11\end{pmatrix},
\qquad \rho_{C_4,3}=I.
\]

The cubic normalized sign is \(-1\), while the quartic projective \(i\)-exponent is zero. This violates D.36's proved arithmetic graph. The independently retained fixed-fibre pair is still \(T_4=I,\ W_3=[i]\), the extra pair excluded from the Galois image in D.25.

## Exact projection kernels and an untested source word

The joint group and its two projection kernels have orders

\[
|\mathcal J|=2^{13472}3^{1156},\qquad
|\ker(\mathcal J\to J_{12})|=2^{11158},\qquad
|\ker(\mathcal J\to T_3)|=2^{1903}3^{1154}.
\]

The source maps are
\(\widehat B\to\mathcal J\) and
\(\widehat F\to\ker(\mathcal J\to S_3)\).
Each has kernel equal to the closure, in its source, of
\([L,L]L^{12}\cap D_9K\).
The open embedding \(\widehat F\hookrightarrow\widehat B\) identifies these kernels.

For the first two marked generators \(a_1,a_2\) of \(K\), each \(a_i^{12}\) lies in \(L\). This follows from the exact exponent-12 image of \(K\) in \(H\), and both elements are checked directly. Thus

\[
w=[a_1^{12},a_2^{12}]^2
\]

lies in \([L,L]\). The first mod-two Magnus term of \(a_i^{12}-1\) is \(X_i^4\). The first term of \(w-1\) is

\[
(X_1^4X_2^4+X_2^4X_1^4)^2,
\]

which contains four distinct degree-16 monomials and is nonzero. Hence \(w\in D_{16}K\subset D_9K\), and its nonzero image in the free pro-two completion proves it is nonzero in the full profinite source. The program checks its 768-letter \(B\) representative, both finite projections, its exact free-\(K\) word and the four leading monomials.

This gives a specific remaining source kernel. D45 and its later source-transport supplement exclude a full lift of this recorded shadow. D.38 does not assert compatibility with D.33's entire infinite class-two tower or every previously retained mixed-prime quotient; it proves the displayed simultaneous finite quotient and the specified retained components.

## Reproduction and current review status

Run the four final-name programs in the order listed at the start of this report. They locate the earlier project certificates either beside themselves or in the exact enclosing LM7_FERMAT_TOWER/code directory. Their only nonstandard Python dependency is NumPy. The completed runs took approximately 21.5, 22.3, 28.4 and 1.2 seconds, respectively. Each has actual nonempty stdout and a full JSON certificate.

Root independently audited the entire proof and freshly ran the final joint program (which executes the module and image programs) and the cover program. Every mathematical JSON field in all four certificates is identical; only elapsed_seconds fields were excluded recursively. The exact common quotient, Zassenhaus image, integral correction system, generation, full commutator coset, compact-cover maps and remaining nonzero source kernel all passed. The actual fresh output is retained in root_d38_audit.out and the two root_d38_*_fresh.out files. The D(e) and D-after-LM2(1) coverage remains incomplete for genuine full profinite realization; the new finite compatibility step itself is proved.

## Later exact lifting decision

D.45 supplement: t has exact order32 in both consecutive sphere quotients, so every preserving two-adic multiplier is invisible in the tested layer. The actual source inner map Int(c0^258) transports the D33 action to D39. The marked index-nine pro2 free product and coprime complement conjugacy supply torsion conjugators for all normalized representatives, and the characteristic pro2 residual preserves the sphere projection. The specified D35 outer fibre and every D38 action retaining it are therefore excluded. The prescribed CM pair remains open for another finite action.
