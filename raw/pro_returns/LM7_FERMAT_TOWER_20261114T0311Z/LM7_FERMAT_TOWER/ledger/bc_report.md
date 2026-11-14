# Parts B and C: proofs, computations, and source audit

This component was produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). We claim no priority. The table concerns the assigned B/C tasks; it is not a completion claim for the other parts of the return.

| Task | Statements | Outcome |
|---|---|---|
| Item 2 | B.1–B.3, B.5–B.14 | (b): withdrawn freeness is false; the exact tower, modules, splitting, and uniqueness are proved |
| Lead 3 | C.1–C.8, B.14 | (b): proposed identification is false; the actual motives and comparison morphisms are constructed |
| B(a) | B.1, B.2, B.14 | (a): precise source problem and arithmetic tower identification |
| B(b) | B.4, B.5, B.8, B.9 | (a): discrete and full profinite rank-one theorem, inverse-limit maps, deck and permutation actions |
| B(c) | B.3, B.5–B.7, B.9 | (b): withdrawn action freeness refuted; general integral modules and n≤8 computations proved |
| B(d) | B.10–B.13 | (a): actual continuous H² class is zero, all N dividing 24 checked, unique conjugacy proved |
| C(a) | C.1–C.3, C.7, B.14 | (b): rank-two identification refuted by a finite example; actual 1-motive, realizations, CM ring map and norm comparison proved |
| C(b) | C.4–C.6 | (a): original Rohrlich theorem reduced to the extension; exact exponent n proved for every n≥3 |
| C(c) | C.7, C.8 | (b): proposed interpretation refuted; actual toric Kummer and elliptic generalized-Jacobian constructions proved |

## Exact comparison maps

We retain the source's arithmetic equation \(x_0^n+x_1^n+x_\infty^n=0\). The geometric comparison with \(x^n+y^n=z^n\) multiplies the third coordinate by a chosen \(\alpha_n\) with \(\alpha_n^n=-1\). For odd \(n\), \(\alpha_n=-1\) is rational. For \(n=4\), the displayed comparison is over \(\mathbb Q(\zeta_8)\); the plus quartic has no real points. These fields are retained in the arithmetic statements.

The cover \(q_n\) corresponds to \(K_n=\ker(F_2\to(\mathbb Z/n)^2)\). Its integral homology is the kernel of the Fox differential \((X-1,Y-1):R_n^2\to R_n\), and the exact covering comparison is
\[
0\longrightarrow R_n/\mathbb Z\mathcal N_n
\longrightarrow H_1(U_n,\mathbb Z)
\longrightarrow n\mathbb Z^2\longrightarrow0.
\]
Thus the finite affine homology includes the rank-two quotient. Its inverse limit is zero under the inclusion transition maps \(dn\widehat{\mathbb Z}^2\to n\widehat{\mathbb Z}^2\).

The compact homology has the integral presentation \(R_n/(S_X,S_Y,P_n)\), with \(P_n=\sum_{0\le j\le i<n}X^iY^j\). The quotient is obtained by the displayed peripheral-chain map; it is not inferred from complex characters. The transition formula
\[
P_{dn}\longmapsto dP_n+\binom d2\mathcal N_n
\]
makes the defining ideals pro-zero modulo every coefficient modulus. Together with a compactness proof comparing the closed commutator with the kernel homology tower, this proves the full \(\widehat{\mathbb Z}[[\widehat{\mathbb Z}^2]]\) rank-one assertion. No power-series-domain assumption or restriction to a pro-\(\ell\) component is used.

The generalized Jacobian \(\mathcal J_n\) is linked to the rank-two torus \(\mathcal J_1=T\) by the actual norm map. Its Tate realization has the exact sequence
\[
0\to(R_n/\mathbb Z\mathcal N_n)\otimes\widehat{\mathbb Z}
\to T_\bullet(\mathcal J_n)\to n\widehat M(1)\to0.
\]
At \(n=2\), the source has rank five, the target rank two and the kernel rank three. Modulo two the proposed full-realization identification would equate groups of orders 32 and 4. The finite example is recorded by program.

The CM ring map is \(R_n\to\operatorname{End}(J_n)\), with the same compact annihilator. Its rational image is the product of cyclotomic fields indexed by the permitted character orbits. This replaces the ambiguous expression \(\mathbb Z[\mu_n]^2\) by a specified homomorphism, kernel and image.

## Splitting calculation

The quotient by the central involution has the affine realization
\[
\rho=(R,0),\quad \sigma=(S,(1/3,-1/3)),\quad
R=\begin{pmatrix}0&-1\\1&-1\end{pmatrix},\
S=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]
The corrected generators \(\lambda_0\rho,\sigma\) fix \(p=(2/3,1/3)\). The resulting cochain \(b_h=p-A_hp-t_h\) is integral and satisfies \(c+\delta b=0\). For the full unit action, with \(\nu=(\mu-1)/2\), the correcting translation is \((-\nu,-\nu)\). The corrected scalar lift is the homothety of ratio \(\mu\) about \(p\), so it commutes with the finite complement.

The cohomology lemma is proved integrally for every coefficient abelian group: \(H^0(S_3,I^3/I)=H^1(S_3,I^3/I)=0\). It therefore proves the unique conjugator for the full profinite product. The finite normalized cochain computation independently gives \(|H^2(S_3,M/N)|=\gcd(N,3)\); the actual extension class is zero even where that obstruction group is nonzero.

## Cuspidal extension and exact exponent

The extension class is the homomorphism from the degree-zero cusp lattice to the dual Jacobian taking a divisor to its line bundle. We prove this by pushing the torus extension out through each character and identifying the resulting Poincaré line bundle.

For every pair of distinct coordinate cusps \(P,Q\), a tangent-line ratio has divisor \(n(P-Q)\). At \(Q\), the pole semigroup is exactly \(\langle n-1,n\rangle\): those two pole orders are realized explicitly, and their semigroup has precisely the genus number of gaps. Every proper divisor of \(n\) is a gap. Therefore \([P-Q]\) has exact order \(n\), for every \(n\ge3\), including even levels.

The extension consequently has exact order \(n\). Pullback along \([n]\) is split, and projection from that split pullback gives an isogeny \(T_{D_n}\times J_n\to\mathcal J_n\) with kernel \(J_n[n]\) and degree \(n^{2g_n}\). The splitting is unique and descends to \(\mathbb Q\). There is no integer killing all levels.

Rohrlich's original Theorem 1, printed p.101, supplies the whole geometric cuspidal group:
\[
(\mathbb Z/n)^{3n-7}\quad(n\text{ odd}),\qquad
(\mathbb Z/n)^{3n-7}\times\mathbb Z/2\quad(n\text{ even}).
\]
Its definitions on p.95 identify the quotient with the image of the extension-class homomorphism. This is the requested reduction, rather than an attribution based on a secondary citation. At \(n=3,4,5,7\), the exact exponents are \(3,4,5,7\).

## Programs actually run

All programs are standalone Python files and use exact integer or rational arithmetic. The Fox and Smith calculations use SymPy. Each has a text output and a machine-readable JSON output in the code directory.

| Program | Actual calculation |
|---|---|
| b_fermat_modules.py | Lifted graph, integral cycle basis, Fox matrices, deck and S3 matrices, cusp matrices, commutator orbit, compact ideals, all Smith checks, n=1,…,8 |
| b_splitting.py | Integral affine cocycle and trivializing cochain; normalized cochain matrices through C³; full-product factor-set checks for N=1,2,3,4,6,8,12,24 |
| b_freeness.py | Actual finite-field Fermat points and full/quotient stabilizers for n≤8; finite 1-motive rank counterexample n=m=2 |
| c_cuspidal_exponent.py | Exact gap certificates for requested levels and every n=3,…,32; Smith form of the checked six-relation odd cuspidal presentation at n=3,5,7 |

The affine ranks are \(2,5,10,17,26,37,50,65\); the compact ranks are \(0,0,2,6,12,20,30,42\). All cusp inclusions and compact quotients are torsion-free, as verified by their Smith forms. The largest full-product splitting check covers 82,944 pairs.

The odd-level cuspidal Smith factors are \(3,3\), eight copies of \(5\), and fourteen copies of \(7\). The even quartic exponent is checked through the independent gap certificate, not by extending the odd presentation.

## Sources actually read

We read the supplied checked transcriptions of scans 96–153 and relevant earlier scalar formulas. We visually inspected scan 98 and scans 135–145. We also used the actual equation at scan 151 and the subsequent transcriptions defining the multiplication fibre. Scan 121 is absent from the supplied scan folder; the body-heading reference to folio 708 is taken from its supplied transcription and is explicitly recorded that way.

We opened the supplied Deligne *Théorie de Hodge III*, §§10.1–10.3. Definitions and finite, Betti, étale and de Rham comparisons used in C.1 and C.7 are specified by number in the paper.

We searched for the full profinite Fermat homology assertion and opened Otsubo, *Homology of the Fermat Tower and Universal Measures for Jacobi Sums*, especially §§4–6 and Theorem 6.1. Its theorem agrees with our complete inverse-limit proof. Its notation for the intermediate affine curve differs from our all-cusp-deleted \(U_n\), so the comparison maps are written explicitly.

We searched Rohrlich's title, opened the original Göttingen digitization of Inventiones volume 39, and inspected pp.95, 97, 100 and 101. Theorem 1 and its even-level factor were checked in the original image. Vélu's original exposition, Theorem 1 and its relation argument, and Banerjee–Merel's arXiv version 1, Theorem 29, were opened to verify the six-relation presentation used by the program.

The five bibliography records in bc_refs.bib are marked verified and list the portions opened. Research downloads and page images are temporary reading aids, not generated deliverables; the final ZIP need not redistribute those published papers.

## Corrections and remaining reading uncertainty

The withdrawn assertion at scan 98 is about a scheme action, not freeness of an Alexander module. The full triple action has a diagonal kernel. The effective quotient action is free exactly on the stated punctured open, while the finite homology modules are generally nonfree. Both questions are answered through their actual maps.

The rank-two object in the source is the Tate module of the three-point torus. The source then constructs a generalized Jacobian of an elliptic curve with the three nonzero two-torsion points as modulus; its rank-two Tate module is the toric kernel in a rank-four sequence. The arbitrary Fermat generalized Jacobian is connected by the norm map above, whose nonzero kernel is computed.

The source's actual Fermat construction is the pullback of the multiplication tower on \(T=\mathbb G_m^3/\mathbb G_m\) along \(\psi(z)=[-z:z-1:1]\). For a marked section \(e\), the 1-motive \([\mathbb Z\to T]\), \(1\mapsto\psi(e)\), has the Fermat fibre as the fibre over 1 of its finite realization. These equations give the mathematical interpretation of the motive discussion. They do not determine the unread initial letters of the table-of-contents word “[??]tivisation”.

The readings register also retains the inconsistent tilde notation at scans 136 and 140, the missing diagonal in (227), the product-one torus's sign-twisted S3 comparison at scan 147, and the open-curve/marked-section qualification around (319). No proof depends on silently selecting one doubtful reading.

No mathematical step remains open within the assigned B/C task list. This assertion does not classify the further section sets or outer-lifting problems assigned to Part E.
