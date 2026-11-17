# Finite group certificates for cote 64, scans 026–039

**Run:** 17 November 2026, after the transcription freeze at 22:58:22 UTC. The final certificate run completed at approximately 23:11 UTC, with every assertion passing. **Checking agent:** GPT-6 Astra Pro, `/root/delivery_tooling`, inherited run configuration; no separately specified effort setting is asserted. The agent read the frozen TeX and permitted research context, not scan images, and made no change to any page or combined transcription.

The main claims in scans 026–036 and 039 are confirmed by exact enumeration and the proofs below. Scans 037–038 pose a lifting problem. Its central extension has the explicit cocycle

\[
((s,d),(s',d'))\longmapsto \operatorname{sg}(s)d'\in\mathbf F_2,
\]

where \(s\in S_4\) acts on the four bifaces and \(d\) records the action on the two face colors. Consequently the obstruction is the cup product of the codiagonal and diagonal characters, with the hypotheses stated in MPL64-G05. This is a calculation completing the finite obstruction description here; it is not a novelty claim. The classical dihedral embedding obstruction appears in Ledet (2001, §0.4).

## Certificate, integrity, and conventions

Run from the package root:

```bash
python3 records/group_checks.py
```

The self-contained Python program requires only the standard library. It enumerates all 256 matrices over \(\mathbf Z/4\), selects the 96 invertible ones, and derives subgroups and actions directly. No small-groups database, symbolic algebra package, or imported result supplies the answers. `group_checks_results.json` records explicit summands, points, generators, counts, intersection indices, and the lifting witness. Assertions are part of the certificate, so use ordinary Python, without `-O`.

Matrices act on column vectors on the left; \(gh\) means first \(h\), then \(g\). Matrix tuples in JSON are row-major. \(D_8\) means the dihedral group of **order eight**; the manuscript and Hua often call it \(\mathfrak D_4\). The two conventions refer to the same group.

The program verifies that its source binding is the frozen combined transcription with SHA-256

`f5b4a21fa7e2d5bcac3f2f42e655abe0cbd277b4c3442b07e9c0438abf5a7932`.

The certificate script SHA-256 at this run is

`82d88ade33c1def8202742093b03a4d4b701822435e689d79066c907e239addf`.

The script reads the combined fragment only as bytes for this integrity binding. Its finite computations do not parse or modify the transcription.

## Results at a glance

| Local statement | Frozen scans | Result and scope |
|---|---|---|
| MPL64-G01 | 026–028, (10)–(17) | Canonical equivariant decomposition \(\operatorname{End}(V)=A\oplus W\), with \(A\simeq V\), \(W\simeq\mathbf F_2^{\omega(J)}\); trace identities; explicit answer to the earlier equivariance question. |
| MPL64-G02 | 026–029, (18)–(22) | The 16-point lift torsor gives the four-point set and square; the automorphism map is exactly \(\mathrm{GL}_2(\mathbf Z/4)\simeq S_4\times_{C_2}D_8\), supporting the canonical groupoid equivalence. |
| MPL64-G03 | 030–032 | Derived groups \(A_4\) and \(A_4\times C_2\); abelianizations \(C_4\) and \(C_2^2\); centers \(\{\pm I\}\); all five displayed subgroup squares and their indices. |
| MPL64-G04 | 033–037, 039 | Six vertices, twelve edges, eight faces, four bifaces; full octahedral image of order 48 with kernel \(\{\pm I\}\); \(\mathrm{PSL}_2(\mathbf Z/4)\simeq S_4\); all three characters and the orientation twist. |
| MPL64-G05 | 037–038 | Central extension is nonsplit; 16 dihedral and 2,304 projective quotient products verify the factor set; obstruction \([C_Q]\smile[D_Q]\), for a specified torsor lifting problem. |
| MPL64-G06 | Finite comparison with LM_140-3 scan 025 | The specified lower unipotent is a four-cycle on primitive-vector sign classes and fixes two vertices. This alone proves no geometric cusp assertion. |

All finite conclusions have high confidence, conditional only on the stated mathematical interpretation of the frozen formulas. No paleographic confidence has been reassessed.

## MPL64-G01. The canonical module decomposition

Put \(V=\mathbf F_2^2\), \(J=V\setminus\{0\}\), and order its elements temporarily as \(e_1,e_2,e_1+e_2\). This order is a computation coordinate, not an additional datum of the construction. For nonzero \(v\), let \(\sigma_v\) be the unique nonidentity element of \(\mathrm{GL}(V)\) fixing \(v\). Let \(\sigma_0=0\). In these coordinates,

\[
\alpha(x,y)=\sigma_{(x,y)}=
\begin{pmatrix}x+y&x\\y&x+y\end{pmatrix},
\quad
\rho=\begin{pmatrix}0&1\\1&1\end{pmatrix},
\quad
\rho^{-1}=\begin{pmatrix}1&1\\1&0\end{pmatrix}.
\]

The formula for \(\alpha\) includes the value zero. Its three nonzero values are the three reflections of the manuscript. In particular \(\alpha\) is linear. Conjugation carries the unique reflection fixing \(v\) to the unique reflection fixing \(gv\), proving equivariance intrinsically.

Let

\[
A=\alpha(V),\qquad
W=\{0,I,\rho,\rho^{-1}\}.
\]

The two 3-cycles are canonically indexed by the two cyclic orientations of \(J\). Sending their two basis vectors to \(\rho,\rho^{-1}\) identifies \(W\) with the permutation module \(\mathbf F_2^{\omega(J)}\); their sum is \(I\). Direct inspection gives \(A\cap W=0\), hence \(\operatorname{End}(V)=A\oplus W\). Moreover

\[
\operatorname{Tr}(aw)=0\ (a\in A,w\in W),\qquad
\mathfrak{sl}(V)=A\oplus\mathbf F_2 I,\qquad
W\cap\mathfrak{sl}(V)=\mathbf F_2 I.
\]

These are vector-space and group-module statements; no decomposition into subalgebras is asserted. Evaluation \(u\mapsto(u(v))_{v\in J}\) identifies \(\operatorname{End}(V)\) with the 16 sum-zero maps \(J\to V\). The relation \(e_1+e_2+(e_1+e_2)=0\) also gives the canonical map

\[
\mathbf F_2^J/\mathbf F_2\mathbf1\longrightarrow V,
\qquad [(c_v)]\longmapsto\sum_vc_vv.
\]

The middle tensor identification in scan 027 (10) uses the unique nonzero alternating bilinear form on a two-dimensional \(\mathbf F_2\)-space. It is invariant under all of \(\mathrm{GL}(V)\), since every determinant over \(\mathbf F_2\) is one, and gives \(V^\vee\simeq V\), hence \(\operatorname{End}(V)\simeq V\otimes V\).

Combining the coefficient map with \(\alpha\) gives the explicitly equivariant identification requested in LM_140-2 scan 569:

\[
\mathfrak{sl}(V)/\mathbf F_2I\simeq V
\simeq\mathbf F_2^J/\mathbf F_2\mathbf1.
\]

For \(T=\begin{pmatrix}a&b\\c&a\end{pmatrix}\), the first map is \([T]\mapsto(b,c)\). The earlier context already gives another formula: LM_P057 R17 sends \(T\) to \(\varphi_T(v)=\det(v,Tv)\), whose three values are \((c,b,b+c)\). Applying the displayed coefficient map yields \((b,c)\). The certificate rechecks this entire formula and its equivariance; it is **not a newly discovered solution** of an unaddressed context question.

The scalar line has four complements in \(\mathfrak{sl}(V)\). Their conjugation orbits have sizes one and three; \(A\) is the unique invariant complement. This verifies the linear count in LM_P057 S6 and adds the orbit description. It does not prove the proposed correspondence there with four lifts of \(\pi_{0,3}\).

**Sources and comparison:** Frozen scans 027–028; LM_140-2 scans 568–569, (68), and LM_P057 R14, R16–R17, S6; Hua, modernised reading of cote 64, §5, “Les Z/4Z-modules libres de rang 2.” The manuscript supports Hua’s decomposition exactly at the module level. Register relation: `64-gl2-z4-combinatorial-model`.

## MPL64-G02. The torsor and the canonical equivalence

For \(M=(\mathbf Z/4)^2\), identify \(2M\) with \(V=M/2M\) by \(2\widetilde v\leftrightarrow v\). The kernel of reduction is

\[
K=\{I+2\widetilde u:u\in\operatorname{End}(V)\},
\quad
(I+2\widetilde u)(I+2\widetilde v)=I+2(\widetilde u+\widetilde v).
\]

Its order is 16. Let \(P\) be the set of triples \((p_v)_{v\in J}\), where \(p_v\) lifts \(v\) and \(\sum p_v=0\). There are 16 triples. The kernel acts simply transitively by

\[
p_v\longmapsto p_v+2u(v).
\]

Thus \(P\) is canonically an \(\operatorname{End}(V)\)-torsor. Its two quotient torsors are

\[
I=P/W,\qquad S=P/A.
\]

Both have four elements. Equip \(S\) with square edges given by the two distinguished differences \(\rho\) and \(\rho^{-1}\) in \(W\). Its codiagonals are those two directions, hence identify with \(\omega(J)\). The four-point affine plane \(I\) has its three partitions into opposite pairs canonically identified with \(J\); parity on its four vertices agrees with parity on these three partitions. The orientation identification may be expressed by the usual convention taking the ordered four points \((i_0,i_1,i_2,i_3)\) to the three pairings \((01|23,02|13,03|12)\). It is invariant under even relabeling. This supplies the natural \(k:\omega(I)\to C(Q)\) used by the manuscript, without choosing a point of \(P\).

The computation verifies that the induced action on \(I\) is all \(S_4\), the action on \(Q\) is all \(D_8\), and the combined image is exactly

\[
\{(s,q)\in S_4\times D_8:\operatorname{sg}(s)=\chi_C(q)\},
\]

with 96 elements and trivial kernel. The construction is natural under module isomorphisms. Both the source groupoid of free rank-two modules and the target groupoid of triples \((I,Q,k)\) are nonempty and connected: every object is isomorphic to its standard model, and relabeling acts transitively on the two choices of \(k\). The isomorphism on automorphism groups therefore proves full faithfulness and essential surjectivity. This proves the groupoid equivalence, not an equivalence of categories containing arbitrary linear maps. It also descends to finite locally constant versions of these objects because the constructions and their inverse equivalence commute with descent.

To exhibit a splitting of reduction, the program chooses

\[
p_0=((1,0),(0,1),(3,3)).
\]

Its stabilizer is a six-element complement to \(K\), generated by

\[
r=\begin{pmatrix}0&3\\1&3\end{pmatrix},
\qquad s=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\qquad r^3=s^2=1,\quad srs=r^{-1}.
\]

This recovers the manuscript’s semidirect description **after a trivialization of \(P\)**. The quotient constructions and groupoid equivalence are canonical; this chosen splitting is not.

**Sources and comparison:** Frozen scans 026–029, especially theorem (18) and corollaries (21)–(22); Hua §5; RESULTS_STATE ID `64-gl2-z4-combinatorial-model`. The finite certificate and proof support the finding’s full groupoid statement rather than only its abstract order or group name. The finding remains credited to Hua’s project as a prior modern interpretation; the enumeration and proof recorded here are this run’s checks.

## MPL64-G03. Derived groups, characters, and lattice

Write \(G=\mathrm{GL}_2(\mathbf Z/4)\), \(G_1=\mathrm{SL}_2(\mathbf Z/4)\), and \(Z=\{\pm I\}\). Direct generation from **all** commutators gives

\[
[G_1,G_1]=A_4=\ker(G\to D_8),\quad
[G,G]=A_4\times Z,\quad
(G_1)_{\mathrm{ab}}\simeq C_4,\quad G_{\mathrm{ab}}\simeq C_2^2.
\]

The \(A_4\) designation is certified by its faithful action as exactly the twelve even permutations of \(I\). The centers of both groups are exactly \(Z\). Quotient element-order counts are \(1,1,2\) in orders \(1,2,4\) for \((G_1)_{\rm ab}\), and \(1,3\) in orders \(1,2\) for \(G_{\rm ab}\).

This also follows transparently from the fiber product: the determinant-one part of the square group is its rotation subgroup \(C_4\). Commutators of lifts have square component one and generate the \(A_4\) component. In the full group the square commutator contributes its central half-turn, giving \(A_4\times Z\).

Use additive bits \(\epsilon(g)\) and \(\delta(g)\) defined by \((-1)^{\epsilon(g)}=\operatorname{sg}(\bar g)\), \((-1)^{\delta(g)}=\det(g)\). In square coordinates \((x,y)\), every action has the form

\[
(x,y)\longmapsto(t_1,t_2)+\operatorname{swap}^{c}(x,y).
\]

The three character identities checked for every \(g\) are

| Square two-element set | Character bit |
|---|---|
| Codiagonals \(C_Q\) | \(c=\epsilon(g)\) |
| Diagonals \(D_Q\) | \(d=t_1+t_2=\epsilon(g)+\delta(g)\) |
| Orientations \(\operatorname{Or}(Q)\) | \(t_1+t_2+c=\delta(g)\) |

The class of \(U=\begin{pmatrix}1&0\\1&1\end{pmatrix}\) generates \((G_1)_{\rm ab}\). The program checks, for all 96 \(g\), that \([gUg^{-1}]=\det(g)[U]\), in additive cyclic order-four notation. Thus this abelianization transforms as the determinant line, supporting the identification with \(\bigwedge^2 M\) in the brace of scan 032, after fixing the displayed standard-generator convention.

Let \(K_A=1+2A\), \(K_W=1+2W\), and \(K_0=K\cap G_1\). The five cartesian squares in scan 032 are exactly the following intersections; inclusion indices are recorded in the JSON.

| Top group | The two intermediate groups | Their intersection |
|---|---|---|
| \(G\), order 96 | \(\ker\epsilon\), \(G_1\), orders 48,48 | \([G,G]\), order 24 |
| \(\ker\epsilon\), order 48 | \(K\), \([G,G]\), orders 16,24 | \(K_0\), order 8 |
| \([G,G]\), order 24 | \(K_0\), \(A_4\), orders 8,12 | \(K_A\), order 4 |
| \(K\), order 16 | \(K_W\), \(K_0\), orders 4,8 | \(Z\), order 2 |
| \(K_0\), order 8 | \(Z\), \(K_A\), orders 2,4 | \(1\) |

The chosen point \(p_0\) gives a subgroup \(S_4\le G\), with \(G\simeq K_W\rtimes S_4\) and \(\ker(\epsilon+\delta)\simeq S_4\times Z\). The action on \(W\) is through parity and exchanges \(\rho,\rho^{-1}\), so the first product is not a direct product. All eight elements of \(G_1\) with square one lie in \(K\); therefore reduction \(G_1\to S_3\) cannot have a section, which would have to lift a transposition to an element of order two. This distinguishes it from the split reduction of \(G\).

**Sources and comparison:** Frozen scans 028, 030–032; Hua §5, “Proposition,” “Le treillis,” and the semidirect descriptions. These calculations support those substantive interpretations. Hua’s footnote reports a direct-product reading in his page 31; the frozen scan 032 uses a dot at the relevant place. That is an unadjudicated reading comparison, not a reason to alter the frozen text.

## MPL64-G04. The octahedron and projective quotient

There are twelve primitive vectors in \(M\) and six classes modulo \(v\sim-v\). With lexicographically least representatives they are

\[
(0,1),(1,0),(1,1),(1,2),(1,3),(2,1).
\]

Reduction to \(J\) partitions them into three opposite pairs. Joining vertices in different pairs gives twelve edges, and choosing one vertex in each pair gives eight triangular faces. The 48 permutations preserving the three-pair partition form the full combinatorial octahedral group. The matrix action has exactly this image and kernel \(Z\).

The map

\[
P\longrightarrow F(\Delta),\qquad(p_v)\longmapsto\{[p_v]:v\in J\}
\]

is equivariant and has exactly the two-element \(Z\)-orbits as its fibers. Thus \(P/Z\simeq F(\Delta)\); taking antipodal face pairs gives \(P/W\simeq I\). In particular this verifies the manuscript’s identification of the four-point torsor with the bifaces.

The two face colors are exchanged with character \(\epsilon+\delta\). Octahedral orientation has character \(\delta\), while orientation of the three opposite pairs, or of the four bifaces, has character \(\epsilon\). One direct check is to identify the six vertices with the positive and negative coordinate axes in three-space: the determinant of a signed permutation is parity of the axis permutation plus parity of the sign flips. These are exactly \(\epsilon\) and the face-color character.

Consequently \(G_1/Z\) is the 24-element rotation group and acts as all of \(S_4\) on bifaces. The full octahedral group is the direct product of its rotation group and its central antipode. The preimage of that center in \(G\) is \(K_W\), of order four. Twisting the vertex action by the orientation character multiplies orientation-reversing actions by the antipode; its image is the rotation group and its kernel is \(K_W\). This certifies the \(\Delta^+\) construction in scan 037.

**Sources and comparison:** Frozen scans 033–037 and 039; Hua §6, “L’octaèdre d’un module, et récapitulation,” through the part corresponding to scan 039; LM_140-2 scan 569 (70), LM_P057 R18. The group expectation in R18 is verified. Neither the Fermat-conic identification in R19 nor the compatibility of a particular modular cover with a ramification convention follows from this finite certificate.

## MPL64-G05. What the central quotient loses

The square group is \(D_8=\mathbf F_2^2\rtimes\mathbf F_2\), with the last factor swapping the two coordinates. Write its elements as \((t_1,t_2,c)\). Its center is generated by \(z=(1,1,0)\), and its central quotient has coordinates

\[
(c,d)=(c,t_1+t_2),
\]

which are, respectively, the codiagonal and diagonal characters. Choose the set-theoretic section \(q(c,d)=(d,0,c)\). Direct multiplication gives

\[
q(c,d)q(c',d')=z^{cd'}q(c+c',d+d').
\]

Every one of these 16 products is checked. In the matrix group, identify the projective quotient with \(S_4(I)\times C_2\), the second coordinate being face color. For \((s,d)\) there is a unique matrix lift having square component \(q(\operatorname{sg}(s),d)\). Every one of its \(48^2=2,304\) products satisfies the same formula, with \(z=-I\). This verifies the reduction of the lifting problem to the square group, rather than presuming it from the equal orders.

**Precise lifting statement.** Let \(\Gamma\) be a group, or a profinite group with continuous actions, and let \(\rho:\Gamma\to\operatorname{Aut}_{\rm oct}(\Delta)\) be specified. Put \(\alpha=\operatorname{sg}(I)\circ\rho\) and \(\beta=\operatorname{color}\circ\rho\), as \(C_2=\mathbf F_2\)-valued characters. A lift \(\widetilde\rho:\Gamma\to G\) exists if and only if

\[
\alpha\smile\beta=0\quad\text{in }H^2(\Gamma,\mathbf F_2).
\]

Indeed, multiplying the chosen section by a function \((-I)^{b(\gamma)}\) makes it a homomorphism precisely when

\[
b(\gamma)+b(\eta)+b(\gamma\eta)
=\alpha(\gamma)\beta(\eta).
\]

The right side is the inhomogeneous cup-product cocycle. When solutions exist, their differences are \(\mathbf F_2\)-valued 1-cocycles. For torsors over a base, the corresponding statement uses the constant central sheaf \(C_2\): the lifting obstruction is \([C_Q]\smile[D_Q]\in H^2(S,C_2)\), and, **with the quotient identification fixed**, isomorphism classes of lifts form an \(H^1(S,C_2)\)-torsor. Automorphisms over that identification are \(H^0(S,C_2)\), hence \(C_2\) on a connected base. This is a descent statement about finite locally constant structures. It does not classify arbitrary algebraic rank-two bundles, and it does not say an isolated octahedron in the category of sets lacks a module model.

A concrete obstruction is already visible for \(\Gamma=C_2\). Choose an odd involution on \(I\) and reverse face colors. In the program’s labeling, the \(I\)-permutation is \((0,1,3,2)\) and one matrix lift is

\[
g=\begin{pmatrix}2&1\\3&2\end{pmatrix},\qquad g^2=-I.
\]

Both lifts \(g,-g\) have order four. Hence this order-two action has no order-two matrix lift. The global central extension is nonsplit as well: \(-I\in[G,G]\), whereas a splitting of a central order-two extension would make the kernel a direct factor disjoint from the derived subgroup.

The result is standard dihedral cohomology in the manuscript’s particular character coordinates. Ledet (2001, §0.4, pp. 283–284) gives the field embedding obstruction as the quaternion class \((a,ab)\) in rotation/reflection coordinates. Writing their character coordinates as \(x,y\) and ours as \(c=x,d=x+y\) gives \(c\smile d=x^2+x\smile y\), the same class. Identifying \(C_2\) with \(\mu_2\) for this field comparison requires characteristic different from two. Our factor-set proof itself needs no field and makes no claim of new dihedral obstruction theory.

**Sources and comparison:** Frozen scans 037–038, (47)–(48) and the square lifting paragraph; Hua §6, “Ce que l’octaèdre perd.” Hua correctly preserves the problem as an unfinished parenthesis. The cup-product formula above is a checked consequence developed in this run, not a quotation from the frozen pages or from Hua.

## MPL64-G06. The finite unipotent bridge

LM_140-3 §39, scan 025, (8)–(9), describes, with “sauf erreur” and up to conjugacy, the cusp-loop image as the subgroup \(\begin{pmatrix}1&0\\n&1\end{pmatrix}\), \(n\in\widehat{\mathbf Z}\). Taking \(n=1\) and reducing modulo four gives \(U\) above. Its exact action is

\[
(1,0)\longmapsto(1,1)\longmapsto(1,2)
\longmapsto(1,3)\longmapsto(1,0),
\]

fixing \((0,1)\) and \((2,1)\), with each pair representing its primitive-vector sign class. Thus the specified matrix acts as a quarter-turn. The calculation neither proves the geometric identification of cusp inertia with this unipotent subgroup nor transports an arithmetic or GT action to all congruence levels.

**Sources and register scope:** LM_140-3_text.tex, scan 025, (8)–(9), and frozen scans 033–036 for the finite octahedron model. `LM2 C.d1` and `LM2 C.r1`–`C.r3` in `LM2_CONGRUENCE_ROWS.md` remain background claims with their original statuses. RESULTS_STATE `LM4_SUCCESSOR B.38` and `E.10` concern unresolved higher congruence kernels and are untouched. No proof-check event is assigned to these claims merely because they were read or named.

## Two typing or reading questions to retain outside the transcription

1. **Scan 028 after (19):** the mathematically well-typed kernel map is \(u\mapsto I_M+2\widetilde u\), independent of the chosen lift \(\widetilde u\in\operatorname{End}_\Lambda(M)\). Its reduction is \(I_V\). The wording about the composite with reduction being \(u\mapsto I_M+2u\) mixes targets if taken literally. Hua §5 already calls out this issue. The frozen text is unchanged.
2. **Scan 037 (47):** the frozen lower label has \(\operatorname{Aut}_{\rm oct}(\Delta_M)'\), whereas (48) uses the unprimed group. The verified quotient \(G/Z\) has order 48 and is the **unprimed** octahedral group. If the extra prime in (47) is intended to mean a further central quotient, its order would be 24, inconsistent with the adjacent product of rotations and antipode. This is a conditional notation/reading question; this agent has not examined the ink and cannot decide whether the mark is a prime.

## Context search and check accounting

The context README and RESULTS_STATE were read after freeze; Hua’s README was read before his modernized interpretation was used. Targeted searches covered `End`, `sl`, `matrices scalaires`, `torseur`, `produit fibré`, `abélianisé`, `semi-direct`, `octaèdre`, `codiagonales`, the named result ID, and the congruence result IDs. Relevant matches were read in their surrounding sections. The mapping below records what was actually compared.

| Claim family | Context passages used | Treatment |
|---|---|---|
| Canonical module and trace decomposition | Hua §5; LM_140-2 568–569; LM_P057 R14, R16–R17, S6 | Direct comparison and independent exact check; R17’s existing solution explicitly credited. |
| Torsor/square equivalence | Hua §5; RESULTS_STATE `64-gl2-z4-combinatorial-model` | Targeted proof check and finite automorphism certificate. |
| Derived groups and subgroup lattice | Hua §5, “Proposition,” “Le treillis” | All relevant groups, indices, characters, and five intersections recomputed. |
| Octahedron and PSL identification | Hua §6; LM_P057 R18 | Finite actions recomputed; geometric cover assertions excluded. |
| Central quotient and lifting | Hua §6, “Ce que l’octaèdre perd”; Ledet (2001), §0.4 | Reduction checked, cocycle calculated, hypotheses made explicit. |
| Unipotent bridge and limits | LM_140-3 025; LM2_CONGRUENCE_ROWS; RESULTS_STATE B.38, E.10 | Matrix action checked; broader congruence claims merely scoped. |

`group_checks_events.tsv` contains only events that actually occurred. This is a finite enumeration certificate and written mathematical proof, not a theorem-prover formalization. No reviewed context result unrelated to the current packet has been rederived or promoted in status.

## References

Grothendieck, A. (n.d.). *Modules courbes elliptiques en caractéristiques ≠2: Notes manuscrites*, cote 64, scans 026–039. Frozen diplomatic transcription, MPL_64_002-039 run of 17 November 2026. Manuscript dating in the supplied catalog: from approximately 1980–1982.

Grothendieck, A. (n.d.). *Longue Marche*, cotes 140-2, scans 568–569, and 140-3, §39, scan 025. Supplied context transcriptions; LM_P057 research-note entries R14, R16–R19, S6 are prior-run claims at their stated status.

Hua, M., project. (2026). *Modernised reading of cote 64*, §§5–6, and findings-register entry `64-gl2-z4-combinatorial-model`. Supplied `hua_project/64.modern.tex`, downloaded by the context compilers on 14 November 2026. AI-produced interpretation, credited to the project; not a diplomatic transcription. [Project](https://github.com/Commutator-IO/grothendieck-project).

Ledet, A. (2001). Embedding problems and equivalence of quadratic forms. *Mathematica Scandinavica, 88*(2), 279–302. https://doi.org/10.7146/math.scand.a-14327. The relevant primary passage is §0.4, pp. 283–284. [Publisher PDF](https://journals.msp.org/mscand/article/download/878/877/909).

OpenAI, GPT-6 Astra Pro, `/root/delivery_tooling`. (2026, November 17). *Finite enumeration certificate for MPL64-G01–G06* [Python program and JSON output]. `group_checks.py` and `group_checks_results.json`, this package.
