## Continuation: the actual skeleton section, cocompact operators, and affine marginal images

This continuation adds C.89, C.90, F.24 and F.25. The registers now contain 262 claims: 231 Proved, 3 Known, 25 Refuted and 3 Open. The return remains **INCOMPLETE**, governed by the same 39-obligation table. The four new results retain the original maps and their topologies. They do not change the unresolved status of the general C.12, D.12 or F.7 assertions.

### C.89: a global section on the actual compact lifted skeleton

Retain C.81's original closed disk, its original discrete free proper operator group, and its transitive boundary-fixed commuting subgroup. C.82 supplies an actual quotient triangulation whose lifted closed stars, and hence lifted triangles, form a null family in the original disk. The closure of its full one-skeleton is exactly that skeleton together with the original circle. It is a compact connected space \(X\).

The new result characterizes the exact image \(\mathscr B\) of restriction of the original centralizer to \(X\). Its intrinsic data are an embedding fixing the original circle, commuting with every actual operator on the skeleton, carrying each triangle boundary with its positive orientation, and leaving the interior of the bounded target Jordan disk disjoint from the entire embedded skeleton. These conditions force distinct target face interiors to be disjoint. An intersection would put one boundary in the other Jordan curve; injectivity of the embedding then identifies the original triangles.

For each chosen representative triangle, three labelled vertices normalize its source and target Riemann maps. The boundary comparison
\[
\eta_b=f_b^{-1}\,\iota b\iota^{-1}\,f
\]
is an exact circle homeomorphism fixing the three standard vertices. Its radial extension gives the full face map
\[
F_b=\iota^{-1} f_b\widehat\eta_b f^{-1}\iota,
\]
with its displayed inverse. It agrees with the prescribed embedding on the entire boundary. Every other triangle receives the literal transported map \(qF_bq^{-1}\). Triviality of triangle stabilizers, proved from the original covering, makes this prescription unique. Commutation on common edges pastes the maps, and both occurrences of \(q\) retain orientation even for orientation-reversing operators.

The bounded Jordan disk is contained in the convex hull of its boundary and has exactly the same Euclidean diameter. Nullity of the source triangles and uniform continuity of the embedding therefore prove continuity of the pasted map at every point of the original circle. Disjoint face interiors give injectivity; invariance of domain and compactness give surjectivity. Conversely every original centralizer map satisfies the intrinsic face conditions. This proves equality with the actual restriction image.

The section is continuous for the full original map-and-inverse topology. The verified Radó theorem gives closed-disk convergence of normalized Jordan maps on each fixed face. The additional three-boundary-point normalization is proved using convergent boundary preimages and the unique Möbius map of the three cyclic points. For all remaining faces at once, equicontinuity of a convergent family of skeleton embeddings and C.82 nullity bound both image diameters. The exact comparison through a common source boundary point is
\[
d_E(\mathfrak s(b_n)x,\mathfrak s(b)x)
\leq\operatorname{diam}b_n(\partial\Delta)
+\sup_Xd_E(b_n,b)+\operatorname{diam}b(\partial\Delta).
\]
Uniform convergence of inverse maps follows from the fixed inverse modulus on the compact disk. The chosen disk coordinate and its inverse have explicit metric moduli, so this is continuity in the original topology.

Restriction and the section give the inverse maps
\[
(b,k)\longmapsto\mathfrak s(b)k,
\qquad
h\longmapsto\bigl(h|X,\mathfrak s(h|X)^{-1}h\bigr)
\]
between \(\mathscr B\times\mathscr S_{Q,\Lambda}\) and the original centralizer. C.82's identity-fixed contraction of the second factor gives an actual strong deformation retraction onto the section image. The complete deformation of \(\mathscr B\) remains to be constructed. Root and an independent reviewer read the full proof and checked the original topology, all operator labels, both product maps, and the infinite-face estimate.

### C.90: every positive sphere fills for a compact actual quotient

For compact \(N=O/Q\), the proof now gives
\[
\pi_n(\mathscr C_Q,1)=0\qquad(n\geq1)
\]
in the original disk topology, with every original operator retained. The quotient may be nonorientable; the torus and Klein bottle are included. No boundary extension of an operator or an interior conjugacy is used.

C.81's exact evaluation bundle over the contractible original open disk identifies every positive homotopy group with that of the stabilizer of one actual point \(x\). A based sphere in this stabilizer descends continuously, for maps and inverses, to the identity component of \(\operatorname{Homeo}(N\operatorname{rel}\{p\})\), where \(p=\pi(x)\). Only the given based sphere is placed in this component; the argument does not identify the descents of arbitrary other components.

Yagasaki's original Lemma 2.1(i), printed page 2 with proof on page 3, contracts this exact pointed compact-surface group [C_Yagasaki2000]. All exceptions are checked. The quotient is closed and has contractible universal cover, so the sphere and projective plane are excluded. The torus and Klein-bottle exceptions listed by the source have empty fixed set. Here the fixed set contains the specified point. The boundary cases cannot occur. The applicable item is **(i)**; the boundary-fixed item **(ii)** used in earlier results is not substituted for it.

The normalized contraction \(J_r(b)=C_{1-r}(b)C_{1-r}(1)^{-1}\) starts at the identity, ends at \(b\), and fixes the group identity throughout. Lifting \(J_r(b_\xi)\pi\) from the identity through the original covering gives the family of interior homeomorphisms. Lifting the inverse family gives its exact inverse. Covering-homotopy uniqueness proves commutation with each individual deck operator, fixation of \(x\), the sphere basepoint condition, and literal agreement with the original sphere at the final endpoint.

C.88 supplies the missing original-boundary comparison: its compact-parameter tail condition is satisfied with the compact set \(K=N\). The identity extensions therefore give a continuous family of original disk maps and inverses. Concatenating with the based homotopy supplied by the evaluation bundle fills the original sphere. Root and a second independent reviewer checked the full proof, including the exact Yagasaki exception list and both original-source pages. The remaining noncompact quotient requires its own uniform tail control.

### F.24: exact rank-one restriction over every finite field

The actual negative marginal coordinates are
\[
V_-=\widehat F(X_1,\ldots,X_7),\qquad
R_-=\ker(V_-\to\widehat F(X_1,X_2,X_3)).
\]
For a finite field \(k\) and a continuous character \(\chi:V_-\to k^\times\) nontrivial on \(R_-\), restriction to the actual source subgroup \(\mathcal K_-\) is injective both on continuous crossed homomorphisms and on first continuous cohomology. The positive assertion follows by pullback through the explicit F.23.13 isomorphism and its inverse, which carry both \(R_-\) and \(\mathcal K_-\) to their specified positive counterparts.

The coefficient calculation takes place in
\[
\Lambda=\mathbb Z[t_1^{\pm1},\ldots,t_7^{\pm1}].
\]
On the dense discrete free group, the universal character sends \(X_i\) to \(t_i\), and the universal crossed homomorphism sends it to the row vector \(e_i\). Evaluation \(t_i\mapsto\chi(X_i)\) sends its row for a word \(w\) to the exact coefficient row computing \(d(w)\) from the seven values \(d(X_i)\).

The eight negative collision rows and eleven old-source action matrices are produced from the literal F.23 braid records by multiplication in the universal affine group
\[
(a,v)(b,w)=(a+b,v+t^a w),\qquad
(a,v)^{-1}=(-a,-t^{-a}v).
\]
The same decorated Artin words, erased eighth generator, conjugator \(u=c_8^{-1}\), and actual action \(u x_j u^{-1}\) are retained. Source normality places every collision seed and every selected source-conjugate seed in \(\mathcal K_-\). Purity of the old source braids fixes the universal character and proves the exact row chain rule.

The certificate uses 64 rows: the eight seeds and eight rows for each source index in \((2,9,8,10,1,0,7)\). It proves rank seven over each of the following rings or specialized strata:

| Chart | Exact coefficient condition | Recorded row operations | Final rank |
|---|---|---:|---:|
| 4 | Invert \(t_4-1\) | 389 | 7 |
| 5 | Invert \(t_5-1\) | 444 | 7 |
| 6 | Invert \(t_6-1\) | 445 | 7 |
| 7 | Set \(t_4=t_5=t_6=1\), invert \(t_7-1\) | 196 | 7 |

Every division by a character difference is checked by multiplication back, and every pivot is a signed Laurent monomial times a power of that chart's inverted difference. No integer other than \(1\) or \(-1\) is inverted. The first chart's final two one-column rows satisfy the explicit identity
\[
r_5=(1-t_6)e_2,\qquad
r_{48}=\bigl(t_1t_2t_3t_4t_5t_7(t_6-1)-1\bigr)e_2,
\]
\[
r_{48}+t_1t_2t_3t_4t_5t_7r_5=-e_2.
\]
These four charts exhaust every character nontrivial on the closed normal subgroup generated by \(X_4,\ldots,X_7\). The conclusion holds over every field, including characteristics 2 and 3; it is proved by the integer polynomial identities.

The independent verifier imports none of the three producers. It reconstructs all 19 literal word evaluations with generic affine multiplication, reconstructs all 64 rows, and replays the exact row operations, all divisibility identities, the triangular pivot orders, the displayed two-row identity, and the longer retained scalar-ideal certificate. It passes **13,982 exact assertions**. Root also executed it in an isolated directory; every mathematical output agrees with the original verification. The isolated output records its own paths, and the comparison checks their input hashes separately. All programs, inputs, outputs, manifests and stdout are retained.

A continuous crossed homomorphism vanishing on \(\mathcal K_-\) is killed by these 64 rows. Rank seven forces its generator values to zero, hence its values on the dense discrete subgroup to zero, and continuity gives zero on \(V_-\). A cohomology class whose restriction is principal is handled by subtracting the same principal crossed homomorphism on \(V_-\). This proves the stated maps on \(Z^1\) and \(H^1\), with their exact coefficient restrictions.

For every continuous scalar affine representation \(\rho:V_\pm\to\operatorname{Aff}_1(k)\), the two groups \(\rho(\mathcal K_\pm)\) and \(\rho(R_\pm)\) have exactly the same fixed-point set in \(k\). For a scalar character nontrivial on \(R_\pm\), that set also equals the fixed-point set of \(\rho(V_\pm)\). The proof applies the crossed-homomorphism assertion to \(g\mapsto\rho(g)z-z\). For a trivial scalar character on \(R_\pm\), F.21 normal generation through the actual maps \(D^+\to R_\pm\to\rho(R_\pm)\) proves equality of the translation images directly.

The marginal images themselves are equal for every representation satisfying the exact condition
\[
\rho(\mathcal K_\pm)\cap T_k=\{1\}.
\]
For \(M=\rho(\mathcal K_\pm)\), the scalar projection is then injective, so \(|M|\) divides \(|k|-1\). The explicit average \(|M|^{-1}\sum_{m\in M}m(0)\) is a fixed point. The proved fixed-point comparison places the whole image in its abelian scalar stabilizer, and the same actual normal-generation maps give the image equality. F.25 below further settles the nonzero translation intersections that are linear over the ambient scalar field, including every prime field. No ambient invariant quotient killing an unproved invariant intersection is assumed or constructed.

### F.25: equality of actual affine images over every prime field

F.25 enlarges the affine class settled in F.24. For an actual continuous representation
\[
\rho:V_\pm\longrightarrow\operatorname{Aff}_1(k),
\]
write
\[
M=\rho(\mathcal K_\pm),\quad N=\rho(R_\pm),\quad
D=\chi(V_\pm),\quad C=\chi(R_\pm),\quad
U=M\cap T_k,
\]
and put \(k_0=\mathbb F_p(D)\), \(k_1=\mathbb F_p(C)\). The result proves \(M=N\) for every representation whose actual additive subgroup \(U\subseteq k\) is a \(k_0\)-linear subspace. In particular it proves equality for every representation with \(k_1=k_0\), and for every representation into \(\operatorname{Aff}_1(\mathbb F_p)\), for every prime \(p\). The source and target retain the exact F.23 coordinates and original source maps.

F.21, followed through the actual onto map \(D^+\to R_\pm\), proves that the normal closure of \(M\) in \(N\) is \(N\). Its scalar projection is abelian, so \(\chi(\mathcal K_\pm)=C\). When \(C=1\), the target image is a translation group, and the same normal-generation equality directly gives \(M=N\).

For \(C\ne1\), multiplication in the affine group proves
\[
(b,c)(u,1)(b,c)^{-1}=(cu,1).
\]
Every \(c\in C\) has an actual lift in \(M\). Thus \(U\) is stable under \(C\), and hence under the finite ring \(\mathbb F_p[C]\). This ring is the field \(k_1\), proving the automatic \(k_1\)-linearity. The cyclicity of the finite multiplicative subgroup \(C\) is proved in the text by the maximal-order and polynomial-root argument. Choose a generator \(c\ne1\), an actual lift \((b,c)\in M\), and the explicit point
\[
z=b/(1-c).
\]
Conjugation by the translation \(\tau_z\), with inverse \(\tau_{-z}\), sends that lift to \((0,c)\). The new cocycle is \(d_z=d+(\chi-1)z\). It has exactly the same translation subgroup \(U\), and the full conjugated source image is literally
\[
M_z=U\rtimes C.
\]

Now take every \(k_0\)-linear functional \(\ell:k\to k_0\) annihilating \(U\). The cocycle \(\ell d_z\) has coefficient character \(\chi:V_\pm\to k_0^\times\); \(k_0\)-linearity proves the cocycle identity on the original group. It vanishes on the actual source subgroup, since every source translation coordinate lies in \(U\). F.24 over the coefficient field \(k_0\) proves \(\ell d_z=0\) on \(V_\pm\). Finite-dimensional linear algebra gives separating functionals for every vector outside the \(k_0\)-subspace \(U\). Consequently \(d_z(V_\pm)\subseteq U\). The scalar part of \(N_z\) lies in \(C\), so
\[
N_z\subseteq U\rtimes C=M_z.
\]
The reverse inclusion is the original source inclusion, and conjugation back proves \(M=N\). No quotient by an unproved ambient-invariant translation subgroup is used.

The entire proof and every coefficient map were read independently by root and a peer reviewer. F.25 uses the existing exact F.24 certificate and adds no computational premise. Its ten-entry evidence manifest binds the exact source, metadata, report and prior mathematical inputs. The remaining affine class has unequal fields \(k_1\subsetneq k_0\) and an actual source translation subgroup that is not \(k_0\)-linear. The full marginal inclusions and the interaction source image remain unresolved.

### Noncompact C.12: an exact failure of the proposed exhaustion estimate

The separate continuation retains C.84's original radial coordinate \(j(z)=z/(1+|z|)\) and the individual operator \(T(x,y)=(x+1,y)\). The quotient is the actual cylinder \(N=(\mathbb R/\mathbb Z)\times\mathbb R\). For \(m\geq1\), put \(R=m+1\), \(K_m=(\mathbb R/\mathbb Z)\times[-m,m]\), and
\[
\beta(u)=\max(0,1-4|u|),\qquad
F_{R,t}(x,y)=(x+tR\beta(y-R),y),\quad0\leq t\leq1.
\]
The inverse subtracts the same term. These exact formulas prove commutation with every original \(T^q\). The quotient support lies in the band \([R-1/4,R+1/4]\), which avoids \(K_m\). For each fixed \(R\), the displacement of both the map and inverse is bounded by \(R\), uniformly in \(t\). Radial conjugation therefore extends by identity on the original circle as a continuous path of original disk maps and inverses, fixing the lifted core throughout.

At \((0,R)\), the endpoint sends \((0,R)\) to \((R,R)\). The horizontal coordinate in the original disk gives
\[
\sup_{w\in\overline D}|jF_{R,1}j^{-1}(w)-w|
\geq \frac{R}{1+\sqrt2R}>\frac25.
\]
The last inequality is universal: for \(R=1+s\), \(s\geq0\), the positive quantity \(5R-2\) satisfies
\[
(5R-2)^2-8R^2=1+14s+17s^2>0.
\]
Thus the original uniform diameters of the complete core stabilizers, even their identity path components, stay bounded below as these cores exhaust the quotient. Their descended maps and inverses converge to the identity on every compact quotient subset, because their supports escape. The displayed inverse lift consequently fails continuity along this sequence for the original disk topology.

The source comparison is specific. Yagasaki's retained primary PDF, Lemma 4.4 and the proof of Proposition 4.1(1), printed pages 11–12, constructs a contraction using shrinking diameters of complete core stabilizers in a weighted compact-open metric [C_Yagasaki2000]. The displayed sequence proves failure of that diameter estimate for the actual uniform lift metric of C.88. C.87 already supplies a contraction of this same radial group. The unresolved issue is the general controlled construction, not any asserted obstruction to a contraction of this example.

Root read the complete note, code and cited source passage, then ran the producer in an isolated directory. All **3,692 checks** passed, and the output is byte-identical. The program separately records the universal integer polynomial identity and the rational sample checks; the written real-parameter inverse, support and commutation identities supply their full quantifiers. The proof note, root audit, producer, output and isolated replay are included.

### D.78: an odd-character criterion and a computed failure of fixed-point lifting

The unnumbered continuation retains D.78's actual split group \(B=K\rtimes\widehat{\mathbb Z}\), its specified quotient map and section, and its pro-odd kernel \(K\). It proves the exact equivalence
\[
K=1
\quad\Longleftrightarrow\quad
\dim_{\mathbb F_p}H^1(B_0,\mathbb F_p)=1
\text{ for every open }B_0\leq B\text{ and every odd prime }p.
\]
From a nontrivial \(K\), choose an odd Sylow subgroup meeting it nontrivially and containing the specified \(\mathbb Z_p\) section. Its map onto that section and its nontrivial kernel give a nonprocyclic pro-\(p\) group. A character independent of the quotient character can be adjusted to vanish on the specified section. Choosing an actual open normal subgroup of \(B\) inside its kernel extends this character to an actual open \(B_0\), where it is independent of the divided quotient character. The converse is computed on the open subgroups of \(\widehat{\mathbb Z}\).

The note carries this character into an actual finite \(E\)-set and an actual open free kernel. It chooses an open normal \(N_E\subseteq F\) with \(N_E\cap B\) killed by the finite character, and sets \(U=B_0TN_E\). The original parity coordinate gives \(U\cap B=B_0\). The identity coset in \(E/U\) is fixed by the original involution, with the specified stabilizer. This makes the remaining odd-character obstruction concrete. The attempted mod-two periodic-cohomology transfer supplies no detection of it: the order-two norm is invertible on the odd-characteristic coefficient module, and its positive-degree cohomology vanishes.

The fixed-quotient calculation is made on the actual standard punctured torus from D.61–D.64. Retain \(F=\widehat F(X,Y)\), \(c=[X,Y]\), \(\beta(X)=YXY^{-1}\), \(\beta(Y)=Y^{-1}\), and \(w=Y^{-1}v\). The original full fixed subgroup is \(C_F(w)=\overline{\langle X\rangle}\). The explicit characteristic quotient \(q:F\to Q\) is the two-generator class-three exponent-five group of order \(5^5=3125\). Five BCH coordinates, their multiplication, the exact peripheral images, both involution actions and all inverse formulas are provided in the code and proof note. The induced fixed-restriction map has the exact sizes
\[
|q(C_F(w))|=5,\qquad |C_Q(q_E(w))|=25.
\]
The missing fixed element \(q([Y,[Y,X]])\) has coordinates \((0,0,0,0,4)\). This proves non-surjectivity of this actual fixed-subgroup map in a standard full extension where \(K=1\).

The same actual quotient gives a degree-3125 cover with 625 cusps and genus 1251. The two original full involution classes fuse in the finite quotient; the conjugator and both finite transporter sets are recorded. The 25 invariant cusp edges have explicitly computed endpoint maps. Their graph has five connected components, each a cycle of length five. These are concrete data about the specified cover; no arbitrary finite fixed element is promoted to a lift in the original fixed group.

The producer verifies the five universal associativity polynomials symbolically, enumerates the entire generated finite group, and checks all the displayed fixed sets, actions, peripheral maps and incidence data. Root read the full proof note and producer and executed an isolated replay: **37 exact assertions** passed and the output was byte-identical. The note's earlier manifest field requesting root review is preserved as a historical field; the separate root audit supplies that review. Neither this quotient nor the odd-character criterion settles the general \(K=1\) assertion or the full peripheral equations.


### Exact remaining scope and source record

C.12 still retains its full admissible-surface zero-level kernel, the noncompact discrete-operator tail, the deformation of the entire compact skeleton image, arbitrary-frontier lifting and nonfixed-frontier pasting. C.89 and C.90 remove the exact global-section and cocompact subproblems proved above. D.12 retains its literal full peripheral equations, scalar cubic decision, and D.78's actual pro-odd fixed-group kernel. F.7 retains full marginal equality, the interaction source image, and the original residual membership equation. Within the affine class, the remaining field configuration has unequal marginal and ambient scalar fields and a source translation subgroup that is not linear over the latter.

No new bibliography entry is introduced by this continuation. The exact Radó and Yagasaki source uses are checked against the already retained original PDFs. The F.24 calculation derives its rows from the already audited actual F.23 source and supplies the complete new polynomial certificate. The proof audits and original-code hashes are retained. The final build and actual page-review records below govern the current PDF; earlier checkpoint counts and scope sentences remain historical records.

### Final 262-claim build and actual image review

The final manuscript has **578 pages and 262 numbered claim records**: **231 Proved, 3 Known, 25 Refuted and 3 Open**. The readings register has 36 rows. The bibliography has 81 verified source records, with 77 cited entries in the compiled paper. The full report retains the 39-obligation table immediately after its opening **INCOMPLETE** marker.

The preliminary 261-claim compile exposed two omitted closing display delimiters in the new F.24 source. Both were restored; the before-source, failed log, exact two-line repair and revised evidence hash are retained. No mathematical formula, program or output changed. The final four-stage LuaLaTeX/BibTeX build passed every stage. It has **zero overfull boxes, zero missing-glyph diagnostics, zero undefined references or citations, and zero fatal errors**. The historical overfull widths, in points, were 13.68645, 3.45642, 55.68105, 76.02393, 37.09235, 36.24559, 13.30484, 2.94995, 8.79562, 13.04182 and 7.59178; none remains in this build.

The complete final LuaLaTeX log, BibTeX log, four-command transcript and all four stage stdout files were read. The inherited nonfatal records are one underfull page-one table cell (badness 7133), one luaotfload fallback followed by successfully rendered T1 Latin Modern fonts, two generic microtype informational notices, and the BibTeX number-without-volume notice for the correctly retained Tukia series number. The intermediate request to rerun changed labels is absent from the final stages.

The final review covers **104 selected pages**: 65 assigned to root and 39 to the independent reviewer. **65 final images were freshly opened and actually viewed**; **39 final images were verified byte-for-byte and by hash against images actually viewed for the sealed 567-page checkpoint**. All final image hashes were then rechecked. The earlier truncated tool result for pages 160 and 303 was not counted: both were reopened and viewed. The historical D.37o formula was located on final page 351, rendered and viewed as an additional page. Every historical overflow passage and a spread of pages across the document are covered, together with the complete new C.89, C.90, F.24 and F.25 proofs. No clipping, overlapping text, detached equation tags or missing symbols were observed.

The final PDF SHA-256 is `7b32432e84921f17f1a8635e03621a30370b4f5254a1ea5656f0b8a0b1aa65ee`. The final rendered-review SHA-256 is `631e3f1a5f62622662c2a5bfdd011c58597d26494bdb2e430c51d0fe5da522d2`. The review record includes every PNG path and hash, the independent review, the exact log bindings and the historical-page mapping. F.24 also has an additional independent **17,116-assertion** unit-and-manifest audit: all 1,218 intermediate elimination multipliers are valid units and all 23 manifest entries match. This is recorded separately from the 13,982-assertion full polynomial replay.
