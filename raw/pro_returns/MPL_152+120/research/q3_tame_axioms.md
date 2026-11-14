# Q3 research working file: cote 120 and the o-minimal comparison

Prepared only after the transcription freeze. The supplied 38 scan images were not opened by this research worker. References to cote 120 use the frozen transcription; contextual transcriptions remain first-pass working evidence. Cote 121 and the bibliography are checked separately below; no statement in this file authorizes a change to the frozen transcription.

## Source conventions and status

`C147` means `context/MPL_147_138-190_transcription.tex`; `C149` means `context/MPL_149_091-136_transcription.tex`. `STATE` means `context/notes/RESULTS_STATE.md`, read before these notes. **WG2 B15 (§1.2)** is an unchecked planning question; **BISITE D.12** and **CATHOT E.17** are **Open (the return's claim)**, without a full review recorded here. **TOTASPH E.6** is **Proved (the return's claim)**. The additionally supplied `context/STATEMENTS_WITH_STATUS.md` has now been read directly: **STRATA C.1/C.5/C.6/C.8** are **Proved (the return's claim)**; **STRATA C.2/C.3** are **Known (the return's claim)**; **RESIDUE G.3** is **Open (the return's claim; no review)**. Its stated global limit is retained: no row there has had full-effort review, and the medium review does not promote a status. The **MPL_150_085-099+151_001-031 §106** research note remains only a first-pass lead.

The contextual searches are saved in `q3_context_searches.json`. Both contextual transcriptions were searched for `modér`, `compact`, `fonction`, `graphe`, `quotient`, `amalgam`, `limite`, `faisceau`, `anneau`, `corps`, `zéro`, `sépar`, `prolong`, `produit`, and `voisinage`; the relevant contextual notes and state register were searched as well. Neither supplied contextual transcription contains `modér`, so the exact M1–M11 terminology has no same-word antecedent in these two selections; the notes identify the actual nearest construction instead of inventing a previous axiom system.

## Direct answer supported by cote 120

### Q3-01 — A compact-model presentation has an explicit o-minimal realization

**Source:** 120 scans 3–24, especially 6 and 17. **Kind:** unpursued implication; reader's construction. **Quote:** “son graphe”; “les parties modérées … sont compactes”.

For a fixed o-minimal expansion \(\mathcal S\) of the real field with real parameters, put \(K_n(\mathcal S)=\{A\subset\mathbb R^n:A\text{ is compact and }\mathcal S\text{-definable}\}\): this supplies an explicit interpretation of the manuscript's compact branch, and the model functor sends \((n,A)\) to the same compact definable set and each map to the same function with the same graph. Its morphisms are exactly the continuous definable maps: a definable continuous map on compact \(A\) has compact graph, and a compact graph projects homeomorphically onto the Hausdorff domain \(A\). This **adds** an actual model to the compact/local vocabulary in C147 scans 181–184 and bears on **WG2 B15 (§1.2)** as a setting, without settling its localization question. **Confidence: high**, because the comparison on objects, arrows and underlying sets is explicit; the axiom verification appears in the table below.

### Q3-02 — The stated M1–M11 have a fully explicit non-finiteness model

**Source:** 120 scans 3, 10, 13, 15, 17–18, 21. **Kind:** own idea; concrete verification. **Quote:** “axiome (facultatif)” on scan 7; “compactes” on scan 17.

Take \(R=\mathbb R\) with its usual topology and let \(K_n^{\mathrm{all}}\) consist of **every** compact subset of \(\mathbb R^n\); the verification below proves M1–M11 for this family, on the branch in which optional M0 is absent. In particular the ternary Cantor set belongs to \(K_1^{\mathrm{all}}\), and its empty interior and infinitely many points exclude a presentation as a finite union of points and intervals, which is the one-dimensional finiteness clause in the cited o-minimal definition. This **adds** a concrete test to C147 scan 184's compactness/finiteness discussion and leaves **WG2 B15 (§1.2)** and **BISITE D.12** at their recorded statuses. **Confidence: high**, because the proof checks the actual coordinate maps, scalar functions, and compact graphs, rather than comparing terminology.

### Axiom-by-axiom realization and verification

This table is a proof for the two expressly defined families \(K_n(\mathcal S)\) and \(K_n^{\mathrm{all}}\), not an extra axiom attributed to the manuscript. For \(K_n(\mathcal S)\), all the displayed coordinate and field maps are definable; quantification over a definable compact set defines its distance function, and the definable Tietze extension used for M7 is Aschenbrenner–Fischer, Lemma 6.6. For \(K_n^{\mathrm{all}}\), ordinary continuous extension follows either from Tietze's theorem or from that same lemma applied to the expansion of \(\mathbb R\) naming every subset of every finite power (this expansion is definably complete because the real order is complete).

| Manuscript item | Exact operation or construction in the two compact families |
|---|---|
| M1, 120/003 | For \(u:[1,n]\to[1,m]\), the coordinate map \(u^*(x)_i=x_{u(i)}\) is continuous; its image of a compact set is compact. In the definable model this image is definable by the existential formula \(y_i=x_{u(i)}\). |
| M2, 120/003 | Surjective \(u\) makes \(u^*\) a closed coordinate embedding. The inverse image of a compact set is compact: the inverse on the image is a coordinate projection. |
| M3, 120/003 | \(A\cap(u^*)^{-1}(B)\) is closed in compact \(A\), since compact \(B\) is closed in a Euclidean space. This is the precise relative inverse-image operation retained by the axiom. |
| M4, 120/003 | The product \(A\times B\) is compact; its defining formula is the conjunction of the formulas for \(A\) and \(B\). |
| Optional M0, 120/007 | \(\mathbb R\) is noncompact in its usual topology, so these two concrete compact models follow the non-M0 branch explicitly allowed on scan 7. M0 and M9 on this underlying real topological space cannot both hold: they respectively put \(\mathbb R\) in \(\mathcal M_1\) and require that member to be compact. |
| M5, 120/010 | Finite unions of compact sets are compact; the empty set is compact. |
| M6, 120/013 | For nonempty closed \(Z\subseteq X\subset\mathbb R^n\), put \(h(x)=d(x,Z)\) and \(q(x)=(h(x),h(x)x_1,\ldots,h(x)x_n)\). The zero fibre is \(Z\), and equality \(q(x)=q(y)\) off \(Z\) gives \(h(x)=h(y)>0\) followed by \(x_i=y_i\) for every \(i\). Each graph is compact; \(Z=\varnothing\) is handled by \(h=1\). |
| M7, 120/013 | A moderate scalar function on compact \(Z\) is continuous by the compact-graph argument. Extend it continuously to the ambient Euclidean space by Tietze, or definably and continuously by the cited definable Tietze theorem, and restrict to compact \(X\); the restricted graph is compact. |
| M8, 120/015 | \(\mathbb R=\bigcup_{N\geq1}[-N,N]\), a filtered union of compact definable parts. |
| M9, 120/017 | The real line is Hausdorff and the members of each family are compact by definition. |
| M10, 120/018 | The closed intervals \([x-\varepsilon,x+\varepsilon]\), \(\varepsilon>0\), form a compact neighbourhood basis at \(x\). Real parameters supply these intervals in \(\mathcal S\). |
| M11(a), 120/021 | \(\{0\},\{1\}\) are compact definable sets. In fact \(R_0=\mathbb R\) for the chosen parameter convention. |
| M11(b), 120/021 | The restrictions of difference and multiplication to compact \(A\subset\mathbb R^2\) are continuous definable maps, with compact graphs. |
| M11(c), 120/021–023 | On compact \(A\subset\mathbb R^*\), inversion is continuous and has compact image \(A^{-1}\); use \(B=A^{-1}\) itself. The graph is the closed level set \(xy=1\) inside the compact rectangle \(A\times B\). |

### Q3-03 — The Boolean and compact operations are related by an explicit reconstruction

**Source:** 120 scans 3–5, 7, 17. **Kind:** unpursued implication; reader's construction. **Quote:** “\(\mathcal M_n\subset\mathcal P(R^n)\)”.

For the o-minimal realization \(K_n(\mathcal S)\), let \(\mathcal B_n\) be the Boolean algebra generated by these compact definable sets and use \(\tau_n(x)_i=x_i/\sqrt{1+x_i^2}\); then the formula \(\mathcal S_n=\{\tau_n^{-1}(B):B\in\mathcal B_n,\ B\subset(-1,1)^n\}\) recovers the original definable family. The proof is that every bounded definable set is a finite union of locally closed cells, each cell \(C\) is its compact closure minus the compact frontier relative to that closure \(\operatorname{cl}(C)\setminus C\), and \(\tau_n\) and its inverse are definable; the reverse containment follows directly from Boolean closure. This **adds** a specified passage from compact pieces to unrestricted definable sets beside C147 scans 181–184's passage from local pieces to a space, and bears on **WG2 B15 (§1.2)** without a localization conclusion. **Confidence: high** in this formula for the fixed o-minimal realization; no reconstruction claim for arbitrary M1–M11 is made.

### Q3-04 — A named geometric comparison has specified inverse assignments

**Source:** 120 scans 17–20. **Kind:** unpursued implication; literature comparison. **Quote:** “faisceau des germes de fonctions modérées”.

Van den Dries–Miller's analytic-geometric categories are related to o-minimal expansions of \(\mathbb R_{\mathrm{an}}\) by the actual inverse assignments \(\mathcal C\mapsto\mathcal S(\mathcal C)_n=\{A:A\in\mathcal C(\mathbb P^n(\mathbb R))\}\) and \(\mathcal S\mapsto\mathcal C(\mathcal S)\), the latter tested in analytic charts; equivalently the first uses the displayed \(\tau_n\). This supplies a named and proved global/local comparison to examine beside the compact-piece and sheaf descriptions on scans 17–20, while the explicit all-compact model in Q3-02 records what M1–M11 alone permits. It **adds** exact comparison assignments to C147 scan 182's sheafification language and bears on **WG2 B15 (§1.2)**; it supplies no change to **BISITE D.12**. The source is van den Dries–Miller, §§1–3 and Appendix D, with the 2012 corrections consulted.

### Exact modern definition: the coordinate operations compared

Coste, *Topological types of fewnomials* (1998), printed p. 82, gives S1–S6 and the graph definition of maps; the primary PDF is saved at `research_sources/coste-bcp44.pdf`. This table records the comparison in the already fixed family \(D_n=\mathcal S_n\); it does not combine separate manuscript conditions into an unstated axiom system.

| Modern clause | Actual manuscript operation and map in the realization |
|---|---|
| S1: Boolean algebra containing the ambient power | M0 supplies \(R^n\), M5 supplies unions, and M3 supplies intersections; complementation is explicit for the early 121 family (PDF 4). For the compact family the reconstruction Q3-03 explicitly performs Boolean completion followed by \(\tau_n^{-1}\). |
| S2: diagonals | M1 sends \(R^{n-1}\) under a coordinate-repetition map to \(\Delta_{ij}=\{x:x_i=x_j\}\). This uses M0 in the all-definable realization; on a compact domain it gives the corresponding compact diagonal. |
| S3: cylinders | The exact map is \((A,R)\mapsto A\times R\), using M4 and M0. |
| S4: coordinate projection | Use \(u:[1,n]\hookrightarrow[1,n+1]\); the manuscript's \(u^*\) is \((x_1,\ldots,x_{n+1})\mapsto(x_1,\ldots,x_n)\). |
| S5: addition and multiplication graphs | M11(b) on \(A=R^2\) gives difference and multiplication; the graph of addition follows from \(x+y=x-(0-y)\) by the proved graph-composition formula. |
| S6: one-dimensional finiteness | In the real-line realization of the early 121 family, finite locally closed decomposition plus clause (f) gives the finite interval/point conclusion proved at Q3-06. The compact family alone has the explicit Cantor countermodel Q3-02. |
| Maps | \(\Gamma_f\in D_{m+n}\) is precisely definability of \(f\); \(\Gamma_f\in K_{m+n}\) gives exactly continuous definable \(f\) on compact definable source and target, by the graph-projection homeomorphism. Q3-07 calculates the inclusion functor on these arrows. |

For the transported spaces of 120/006–007, choose a presentation \(i_X:|X|\xrightarrow\sim A_X\) and send an arrow to \(i_Y f i_X^{-1}\). These formulas preserve identities and composition, while the inverse assignment gives a concrete model its identity presentation; the maps \(i_X\) are the natural comparison isomorphisms. Thus the object/arrow calculation extends from embedded models to the manuscript's transported structures, with the specified charts supplying the equivalence data.

## Page-level notes on the mathematical development

### A120-01 — The graph calculus can be checked without a tameness finiteness axiom

**Source:** 120 scans 3–6. **Kind:** unproved claim, with explicit verification. **Quote:** “\(gf\) modéré”.

The composite graph is \(\Gamma_{gf}=p_{13}\bigl(p_{12}^{-1}(\Gamma_f)\cap p_{23}^{-1}(\Gamma_g)\bigr)\) inside \(A\times B\times C\), with the relative inverse images taken in that moderate product, so M3, M4 and M1 perform the three operations and coordinate interchange performs graph inversion. This **adds** an elementary graph-level construction beside the product diagrams in C147 scans 165 and 168; the context search found no earlier M-labelled graph calculus in the supplied selections. It bears on the choice of a concrete category in **WG2 B15 (§1.2)**, whose status remains an unchecked plan.

### A120-02 — Empty objects and admissible points are separate steps in the written construction

**Source:** 120 scans 4–5. **Kind:** unpursued implication; reading caution. **Quote:** “\(\mathrm{Card}\ R_0\ge2\)”.

The revision from \(R_0\ne\varnothing\) to \(|R_0|\ge2\) makes the empty-set conclusion use the actual intersection \(\{a\}\cap\{b\}=\varnothing\) for two distinct admissible points; one admissible point supplies no such intersection argument. This **adds** a nullary/finite-object check to C147 scan 164's elementary point object, and the exact formula \(\{x\}\in R^n\) on scan 5 remains a reading question rather than an edited formula. No selected register entry settles this point; **WG2 B15 (§1.2)** supplies only the surrounding programme.

### A120-03 — Finite unions impose a real extra closure operation

**Source:** 120 scans 6 and 10. **Kind:** unpursued implication; concrete example. **Quote:** “parties de cardinal \(\le1\)”; “stable par réunions finies”.

On a set containing distinct \(0,1\), the scan-6 family of empty and singleton subsets contains \(\{0\}\) and \(\{1\}\) while their union has cardinal two, so this example records exactly the extra operation introduced by M5. This **adds** an axiom-level finite-union test to C147 scan 184's finite-strata discussion, whose compactness argument concerns a specified stratification. The connection is to **WG2 B15 (§1.2)** as a proposed ambient framework, without changing its unchecked status.

### A120-04 — The categorical reconstruction is a claim to verify at the stated data

**Source:** 120 scans 7–8. **Kind:** unproved claim. **Quote:** “la donnée d'un \(\mathcal M_*\) est équivalente”.

The proposed reconstruction sends \(\mathcal M_n\) to the subsets underlying subobjects of \(R^n\) in \((\mathcal E,R,U)\), with \(U\) the faithful conservative transportable underlying-set functor carried from scan 6. A proof must check that the images of the coordinate maps land among those subobjects and that the recovered graph morphisms return exactly \(\mathcal E\); these are the actual maps behind the asserted equivalence. This **adds** a concrete-recognition problem beside C147 scan 150's topos-gluing equivalence, and bears on **WG2 B15 (§1.2)** without identifying that open-test localization with this reconstruction.

### A120-05 — Finite graph descent is supplied on the next sheet

**Source:** 120 scans 9–12. **Kind:** unproved claim followed by its proof. **Quote:** “leur réunion aussi”.

The scan-9 colimit assertion is explained on scan 12 by the equality \(\Gamma_f=\bigcup_i(g_i\times1_Y)(\Gamma_{f_i})\), whose finite union is moderate by M5. This **adds** an explicit finite-graph descent argument to the amalgamated-space diagrams of C147 scans 164 and 171; it is the quotient-set universal map and its graph that are checked here. It bears on **STRATA C.1, C.3, C.6** as an elementary comparison of gluing mechanisms, with the return-claim statuses and review limits stated above.

### A120-06 — The scan-11 separation criterion needs its span scope recorded

**Source:** 120 scans 10–11 and 13. **Kind:** reading question; own concrete test. **Quote:** “les \(f_\alpha\) … séparent … les pts de \(X_1\)”.

For the finite discrete span \(X_1=Z=\{0,1\}\), \(i_1=1_Z\), \(X_2=\{*\}\), and \(i_2\) constant, the pushout is \(\{*\}\), but every compatible pair of scalar functions is constant on \(X_1\), so scan 11(b)'s point-separation requirement fails for this span from scan 10's unrestricted question. Scan 13 expressly writes two inclusions in its proved construction, and the note should preserve this narrower geometric scope rather than silently extend the criterion to every span. This **differs** from the inclusion diagrams in C147 scans 164 and 171 and bears on **STRATA C.1/C.3**, whose specified crossing data remain untouched. **Confidence: high**, because every set and map in the test is displayed.

### A120-07 — The quotient by one moderate part is encoded by a finite map

**Source:** 120 scan 13. **Kind:** unpursued implication; explicit construction. **Quote:** “contraction de \(Z\) en un point”.

Write \(q=(f_\alpha):X\to R^A\); M6 says \(q^{-1}(e)=Z\) and gives point separation on \(X\setminus Z\), so the image \(q(X)\) has exactly the fibres prescribed by collapsing \(Z\), and its graph description supplies the moderate quotient. This **adds** a finite-coordinate quotient model beside the groupoid amalgam of C147 scan 156 and the spatial amalgam of scan 164. It bears on **WG2 B15 (§1.2)** and the elementary gluing setting of **STRATA C.1/C.3**, without settling their enhanced coefficient questions.

### A120-08 — M7 is the extension input in the amalgam construction

**Source:** 120 scans 13–14. **Kind:** unproved claim with manuscript proof mechanism. **Quote:** “qui prolonge”.

M7 extends the common embedding \(Z\hookrightarrow R^I\) to maps \(a_i:X_i\to R^I\), and M6 supplies \(h_i:X_i\to R^{A_i}\) with fibre \(Z\) over \(e_i\); the two maps \((a_1,h_1,e_2)\) and \((a_2,e_1,h_2)\) into \(R^{I\amalg A_1\amalg A_2}\) have exactly the required common image of \(Z\). Their finite union is the moderate model used by scan 12's graph-descent proof. This **adds** coordinate witnesses to C147 scan 171's product-of-spans diagram and bears on **STRATA C.1/C.3/C.6** as a comparison of explicit constructions, at the return-claim statuses stated above.

### A120-09 — Scalar extension is a precise modern point of contact

**Source:** 120 scan 13. **Kind:** unpursued implication; literature comparison. **Quote:** “\(\exists g:X\longrightarrow R\) modérée”.

In the compact definable realization, \(Z\subset X\) is closed and a moderate \(f\) is continuous, so Aschenbrenner–Fischer, Lemma 6.6, supplies a definable continuous extension to \(\mathbb R^n\), whose restriction to \(X\) has compact graph and is exactly M7's required arrow. This **adds** a verified extension theorem to the neighbourhood and gluing constructions of C147 scans 140–142 and 164; the supplied context contains no Tietze or M7 statement. The consequence bears on **WG2 B15 (§1.2)** only as an available tame model, not as a resolution of **BISITE D.12**.

### A120-09a — The marginal one-inclusion amalgam has a coordinate construction

**Source:** 120/013, margin, and 014. **Kind:** unpursued implication; reader's construction. **Quote:** “une … flèche … libre” (the frozen reading remains uncertain).

For the displayed span \(X_1\hookleftarrow Z\xrightarrow{u}X_2\), choose \(j:X_2\hookrightarrow R^I\), extend \(ju\) to \(a:X_1\to R^I\) by M7, and choose \(h:X_1\to R^A\) from M6 with \(e\in R_0^A\) and \(h^{-1}(e)=Z\); use the two maps \((a,h):X_1\to R^{I\amalg A}\) and \((j,e):X_2\to R^{I\amalg A}\). Their union identifies exactly \(z\sim u(z)\), since \(h\) separates points off \(Z\), while its \(e\)-fibre records precisely the image of \(u\); M5 and the scan-12 graph formula prove the pushout universal property. This **adds** an explicit reading of the margin's proposed generalization beside C147/164 and 171, and bears on **WG2 B15 (§1.2)** and the **MPL_150_085-099+151_001-031 §106 [first-pass lead]** to STRATA gluing. **Confidence: high** for the construction, independently of the uncertain marginal noun.

### A120-10 — The strict ind-structure specifies its bounded pieces

**Source:** 120 scans 15–16. **Kind:** unpursued implication; comparison construction. **Quote:** “de réunion \(E\)”; “\(A\cap\mathcal Y\)”.

The collection \(\mathcal M_E\), its finite unions, and the inherited structures on its members specify the directed system of actual inclusions used by the strict ind-object; a locally moderate part is tested by intersection with each one of these members. This **adds** a bounded-piece system to the local-stratum structure in C147 scans 181–184, where the chosen local germs and their sheafification carry different explicit data. It bears on **CATHOT E.17** as an ind-presentation comparison and on **TOTASPH E.6** **[Proved, return's claim]** through the directed indexing family, but supplies no proof of the open homotopy-invariant representability problem in E.17.

### A120-11 — The manuscript warns about a specific subobject passage

**Source:** 120 scans 16–17. **Kind:** self-flagged limitation. **Quote:** “ne correspond pas néc. à une partie … modérée”.

The warning must be kept beside the quotient claim: that claim uses intersections with every moderate piece, while a categorical monomorphism is given by its arrows in the ind-category, and the manuscript explicitly refuses to identify the two descriptions without further work. This **adds** a subobject-recognition issue to C147 scan 183's locally immersed stratum inclusion, whose source topology is separately specified. It bears on **CATHOT E.17** and **WG2 B15 (§1.2)** as a constraint on the comparison data, without changing either status.

### A120-12 — Compact graphs prove the continuity assertion

**Source:** 120 scan 17. **Kind:** unproved claim with short verification. **Quote:** “c'est OK si … compactes”.

For a moderate \(f:A\to B\), the graph projection \(p:\Gamma_f\to A\) is a continuous bijection from a compact space to a Hausdorff space, hence is a homeomorphism, and \(f=\pi_B\circ p^{-1}\) is continuous. This **adds** the exact comparison map behind the topology functor beside the neighbourhood maps in C147 scans 140–142. It bears on **WG2 B15 (§1.2)** by supplying actual continuous maps, while its objectwise proof does not evaluate the open-test localization of **BISITE D.12**.

### A120-13 — Countability is explicitly retained in the topology claim

**Source:** 120 scan 18. **Kind:** unproved claim. **Quote:** “quand on suppose … ind-dénombrable”.

The assertion that the final topology restricts to the original topology of each moderate part is stated for an increasing sequence, and that quantifier must remain attached to the assertion during comparison with ind-categories. This **adds** a countable-exhaustion restriction beside C147 scan 184's locally finite stratification discussion. It bears directly on **CATHOT E.17**'s sequential ind-presentation problem, but concerns the topology of already supplied compact pieces rather than the existence of the homotopy-invariant presentation asked for there.

### A120-14 — M10 supplies the local neighbourhood witnesses

**Source:** 120 scan 18. **Kind:** self-flagged desideratum made an axiom. **Quote:** “On voudrait”.

M10 supplies moderate neighbourhoods in \(R\), and finite products plus intersection with a model \(X\subset R^n\) supply the corresponding neighbourhoods in \(X\). This **adds** concrete basis objects to the fundamental-neighbourhood systems used in C147 scans 181–182, while those context passages additionally impose connectedness and local-product requirements on strata. It bears on **WG2 B15 (§1.2)** as geometric input and leaves the realization question **BISITE D.12** open as recorded.

### A120-15 — Locality of maps uses compactness and finite unions together

**Source:** 120 scan 19. **Kind:** unproved claim with proof mechanism. **Quote:** “au voisinage de chaque pt”.

Compactness extracts finitely many moderate neighbourhoods covering the moderate domain \(X\); the local graphs then form the finite union of the global graph, so M5 proves moderation of the map. This **adds** a compact-to-finite descent mechanism beside C147 scan 182's passage from a presheaf to its associated sheaf. It bears on **STRATA C.6** only as a comparison of descent data and on **WG2 B15 (§1.2)** as local geometry; neither register conclusion follows solely from this finite-graph argument.

### A120-16 — Scalar functions are a concrete probe of the structure

**Source:** 120 scan 19. **Kind:** unproved claim; verification target. **Quote:** “connue quand on connaît … dans \(R\)”.

For a target embedding \(Y\hookrightarrow R^n\), a candidate map \(f:X\to Y\) is tested by its \(n\) scalar coordinate functions, and the graph is recovered by their simultaneous graph equations; this is the actual map-level mechanism behind the scalar-probe claim. This **adds** a ringed or function-sheaf presentation to C147 scan 182's sheaf of local stratifications. It bears on **WG2 B15 (§1.2)** but gives no equivalence between the open-test cosheaf construction of **BISITE D.1/D.12** and this scalar-function sheaf.

### A120-17 — The compact-containment wording has a direct interval test

**Source:** 120 scan 20. **Kind:** reading question; own concrete test. **Quote:** “les parties compactes sont les parties contenues dans une partie modérée”.

In the compact semialgebraic realization, \((0,1)\hookrightarrow[0,1]\) is a subset contained in a moderate part, but the cover \((0,1)=\bigcup_{n\ge3}(1/n,1)\) has no finite subcover, so the literal compactness equivalence on this line fails for this actual inclusion. The words may be aimed at the ideal of relatively compact subsets, but that is a reading question, and the frozen sentence is retained. This **differs** from C147 scan 184's use of compactness for a given compact ambient space and bears on **WG2 B15 (§1.2)** and **BISITE D.12** as a warning about the actual category to compare. **Confidence: high** in the interval calculation; **low** in assigning an intended replacement wording.

### A120-18 — The marginal request about compact subparts tests the intended model

**Source:** 120 scan 20, margin. **Kind:** unproved claim or desideratum; own concrete test. **Quote:** “Dire qu'une partie compacte … est modérée”.

The ternary Cantor inclusion \(C\hookrightarrow[0,1]\) supplies a compact subpart of a compact semialgebraic space, while \(C\) has infinitely many points and no interval, so an o-minimal \(K_1(\mathcal S)\) cannot contain it. The proposed marginal closure therefore needs its own status recorded when comparing the text to that model; the all-compact model Q3-02 does satisfy it. This **adds** a specific compact-subobject test to C147 scan 184 and bears on **WG2 B15 (§1.2)** without deciding its open localization question. **Confidence: high**, from the displayed inclusion and the one-dimensional finiteness definition.

### A120-19 — The polynomial structure begins after topology is explicitly set aside

**Source:** 120 scans 21–22. **Kind:** unpursued implication. **Quote:** “Oublions les structures topologiques”.

The field section first asks for moderate graphs of \((x,y)\mapsto x-y\) and \((x,y)\mapsto xy\), so sums and products of scalar moderate functions are obtained by composing their joint graph with these two operations; constants come from \(0,1\in R_0\). This **adds** scalar algebra to C149 scan 105's ring/field objects and scan 122's local rings, whose particular arithmetic constructions are not identified with the manuscript's moderate function ring. No selected result directly settles this M11 calculation; **WG2 B15 (§1.2)** supplies the general geometric setting only.

### A120-20 — Subring and subfield conclusions occur on different sheets

**Source:** 120 scans 21 and 23. **Kind:** unproved claim with subsequent proof. **Quote:** “sous-anneau”; “sous-corps”.

The live scan-21 conclusion gives a subring, and scan 23 supplies inversion by the level set \(\{(x,y)\in A\times B:xy=1\}\), using M11(c)'s moderate bound \(B\); applying it to a nonzero admissible singleton yields its reciprocal singleton and the subfield conclusion. This **adds** the exact reciprocal construction to the field and valuation language in C149 scans 105 and 122. The supplied register has no direct moderate-scalar-field result, and none of the arithmetic status rows is altered by this elementary comparison.

### A120-21 — The inverse graph's dimension label remains a reading question

**Source:** 120 scans 22–23. **Kind:** reading question. **Quote:** “\((x,x^{-1})\in R^2\)”; “\(\in\mathcal M_1\)”.

The frozen scan-22 line places the inverse graph in \(\mathcal M_1\), while scan 23 constructs it as a subset of \(A\times B\subset R^2\); this is an internal dimensional reading question and provides no permission to rewrite the subscript. It **adds** a precise notation question beside C149 scan 105's expressly announced “révision de notations”. No selected register entry settles this reading.

### A120-22 — The zero-set argument supplies the separation off the collapsed part

**Source:** 120 scans 23–24. **Kind:** unproved claim with explicit argument. **Quote:** “séparent les pts de \(X\setminus Y\)”.

The joint map \(x\mapsto(f_\alpha(x),f_\alpha(x)g_\beta(x))_{\alpha,\beta}\) sends \(Y\) to zero, and equal images of two points outside \(Y\) give a shared nonzero \(f_\alpha\), then equality of every \(g_\beta\), and hence equality of the points. This **adds** the algebraic multiplication mechanism to the quotient construction of C147 scan 156, while the more directly comparable internal statement is M6 at 120 scan 13. It bears on **WG2 B15 (§1.2)** as an explicit quotient map and has no consequence for the unresolved enhanced gluing statuses.

### A120-23 — The final sentence on scan 24 overstates that same separation

**Source:** 120 scan 24, final proposition. **Kind:** reading question; own concrete test. **Quote:** “sépare les pts de \(X\)”.

On \(X=[0,1]\), \(Y=\{0,1\}\), use \(f(x)=x(1-x)\) and \(g(x)=x\): the resulting map \(x\mapsto(f(x),f(x)g(x))\) sends both endpoints to \((0,0)\), exactly as the quotient requires, so its coordinates cannot separate those two points of \(X\). The preceding paragraph's separation on \(X\setminus Y\) is the statement supported by the displayed proof; the final larger set and the misplaced-looking \(\lambda\) underbrace remain untouched in the transcription. This **adds** an explicit collapsed-fibre check to C147 scan 164's gluing data and bears on **WG2 B15 (§1.2)** only at the elementary quotient level. **Confidence: high**, because the two endpoint values are computed directly.

### A120-24 — A countable compact-definable exhaustion gives a precise named comparison object

**Source:** 120 scans 15, 18–20. **Kind:** unpursued implication; literature comparison. **Quote:** “suites croissantes d'espaces modérés”.

For a sequence \(X_1\subseteq X_2\subseteq\cdots\) of compact definable spaces, take the same union and stage inclusions, use definable open sets and continuous definable scalar functions on each stage, and declare an open family admissible when its trace on every stage has a finite subfamily covering that trace's union; this is the countable-exhaustion construction entering Piękosz's **weak polytopes** (his §6, WD1–WD6). The identity on every \(X_n\) is the comparison of objects, and maps represented by compatible definable maps from each source stage into some target stage supply the corresponding maps of these presentations. This **adds** a named stagewise model beside C147 scan 182's local sheaf construction and bears on **CATHOT E.17** without proving its general representability claim. **Confidence: high** for the displayed countable presentation; no equivalence of all possible manuscript ind-objects with all weakly definable spaces is asserted.

## Primary bibliography and retrieval ledger

1. Lou van den Dries and Chris Miller, *Geometric categories and o-minimal structures*, Duke Mathematical Journal 84 (1996), 497–540; author revision dated 20 February 2001: <https://people.math.osu.edu/miller.1987/newg.pdf>. Read §§1–3, Appendix B formulas for graph operations; web refs `turn20view1`, `turn23view0`, `turn28view0`. The bibliography uses its exact definitions and the inverse assignments, with proof checks in the present notes distinguished from attributed text.
2. Chris Miller, *An upgrade for “Geometric categories and o-minimal structures”*, version 14 November 2012: <https://people.math.osu.edu/miller.1987/geofix.pdf>. Web ref `turn20view2`; consulted the corrections; no Whitney-stratification-of-maps claim is used here.
3. Matthias Aschenbrenner and Andreas Fischer, *Definable versions of theorems by Kirszbraun and Helly*, Proceedings of the London Mathematical Society 102 (2011), 468–502, DOI <https://doi.org/10.1112/plms/pdq029>; author manuscript <https://www.mat.univie.ac.at/~maschenbrenner/pdf/KH.pdf>. Web refs `turn41view0`, `turn42view0`, `turn49view0`, `turn52view0`; §6.2 explicitly assumes a definably complete expansion of an ordered field and a closed nonempty domain, and Lemma 6.6 with its proof has now been checked. The empty-domain case is supplied by the zero function.
4. Artur Piękosz, *O-minimal homotopy and generalized (co)homology*, Rocky Mountain Journal of Mathematics 43 (2013), 573–617; author text <https://arxiv.org/abs/0808.3866>, web refs `turn41view1`, `turn42view1`. Read §6's exhaustion axioms and the definition of weak polytope; only the stated countable object construction is used. Page range checked against the author's publication list <https://piekosz.pl/> (`turn52search3`).
5. Heinrich Tietze, *Über Funktionen, die auf einer abgeschlossenen Menge stetig sind*, Journal für die reine und angewandte Mathematik 145 (1915), 9–14, metadata <https://geodesic.mathdoc.fr/item/JRAM_1915__145_149430/>, web ref `turn32view2`. The original full text was not successfully fetched; this is a bibliographic pointer, not the proof source for Q3-02.
6. Montpellier archive, cote 121, <https://grothendieck.umontpellier.fr/121.pdf>, grounded by the archive HTML `data-src="../web/viewer.html?file=../121.pdf"`. The PDF's header reports 73 scans, including the modern cover; downloading and primary-image checks are recorded in the continuation below.
7. Michel Coste, *Topological types of fewnomials*, Banach Center Publications 44 (1998), 81–92: <https://matwbn.icm.edu.pl/ksiazki/bcp/bcp44/bcp4416.pdf>. Printed p. 82 (PDF 2) supplies S1–S6 and the graph definition; the download succeeded and the primary PDF/text are saved locally. Search ref `turn64search23` contains the definition; direct web opening returned 403, while the direct Python download succeeded. The explicit comparison operations in the table are this reader's verification.
8. Ya'acov Peterzil and Charles Steinhorn, *Definable Compactness and Definable Subgroups of o-Minimal Groups*, Journal of the London Mathematical Society 59 (1999), 769–786, DOI <https://doi.org/10.1112/S0024610799007528>. Publisher abstract `turn69view0` confirms the closed-and-bounded characterization; the author-associated full-text page <https://www.academia.edu/18806220/Definable_Compactness_and_Definable_Subgroups_of_o_Minimal_Groups> was opened (`turn73view0`, `turn74view0`), and Definition 1.1 and Theorem 2.1 with its proof were checked there. No quotation from this source is used.

## Cote 121: retrieved primary manuscript and exact comparison

**All 121 scan references below now mean PDF page numbers including the cover, as required by the user; archive footer numbers are separate.** The official PDF is `research_sources/121-ranged.pdf` (27,378,881 bytes; SHA-256 `fc7b1ba2e63ebafaa72cfb6cf2dfcc76676b00833ae2d878aebf5502d146f37b`). It has 73 PDF pages: the modern wrapper is PDF page 1, so archive scan `s` is PDF page `s+1`; the handwritten folio is a third, separately reported numbering. The primary checks for this Q3 comparison used PDF scans 004–024 and 070–073 (archive footers 003–023 and 069–072); the Q4 worker checked PDF scans 030–037 (archive footers 029–036) after I located the diagram/stratification discussion there. This is a located comparison of those passages, not a claim that every paragraph of all 72 archive scans was transcribed or reviewed.

### The two presentations actually visible in cote 121

The following table contains the manuscript-content summary; the verification and examples following it are the reader's constructions. The final compact presentation is separately located from the earlier Boolean-family discussion: no sentence in the checked final four leaves identifies its families with the earlier family or carries over all of that family's conditions.

| Primary locus | Written mathematical data, paraphrased |
|---|---|
| 121/004 (footer 003; handwritten 5) | \(\mathcal F\subseteq\mathcal P(X)\): finite Boolean operations; finite-valued functions. |
| 121/005–006 (footers 004–005; handwritten 6–7) | Closure; dense interior in closure; descending closed nowhere-dense chains terminate. |
| 121/010 (footer 009; handwritten 11) | (f): locally closed members have finitely many connected components, each admissible. |
| 121/015–017 (footers 014–016) | Finite compatible decompositions; connected leaves use (f). |
| 121/019–024 (footers 018–023) | Restriction and local completion; compactness gives global equality. |
| 121/070–071 (footers 069–070; handwritten 71–72) | \(C_n\): coordinate maps, products, graphs, transport, coverage. |
| 121/072 (footer 071; handwritten 73) | Hausdorff base; compact models; model neighbourhoods; function sheaf. |
| 121/073 (footer 072; handwritten 74) | Finite unions/gluing; pushout and scalar-extension questions. |

The comparison with 120 sends the coordinate maps to M1, products to M4, coverage to M8, compactness to M9, neighbourhoods to M10, unions to M5, and the arrow \(f_X|_Y=f_Y\) to M7; every map is the identical coordinate or scalar function. This records formulas, without ordering the undated drafts chronologically.

### Q3-05 — The Boolean-family and compact-model presentations have an actual shared realization

**Source:** 120/003–024; 121/004–010 and 070–073. **Kind:** unpursued implication; reader's construction. **121 quote anchor:** “parties de X”.

For the same fixed o-minimal \(\mathcal S\), put \(D_n=\mathcal S_n\), \(K_n=\{A\in D_n:A\text{ compact}\}\), and \(\mathcal F_X=\{A\subseteq X:A\in D_n\}\) for a definable \(X\subseteq\mathbb R^n\); the displayed assignments supply the power families, compact parts and Boolean families without changing their underlying subsets. The compact graph map is sent to its identical definable graph, while a definable map \(f:X\to Y\) acts on Boolean families by the specified inverse-image homomorphism \(f^{-1}:\mathcal F_Y\to\mathcal F_X\). This **adds** actual comparison assignments beside C147/181–184's local-stratum and sheaf constructions, and bears on **WG2 B15 (§1.2)** as an unchecked choice of geometric setting. **Confidence: high**, because the operations are verified below; no equivalence for every manuscript family is asserted.

### Verification for the early 121 family

For \(\mathcal F_X=D(X)\), Boolean closure is built into the defining formulas. Closure is definable by
\[
x\in\overline A^{\,X}\quad\Longleftrightarrow\quad
x\in X\ \land\ \forall\varepsilon>0\ \exists a\in A\ (\|a-x\|<\varepsilon).
\]
Every definable set is a finite union of locally closed cells; a dense finite union of locally closed subsets of a space has dense interior, so the relative-interior clause follows for \(A\subseteq\overline A^X\). Here is an elementary proof of that finite-union assertion: write each locally closed piece as \(F_i\cap U_i\), discard the union of the closed nowhere-dense boundaries of the \(F_i\), and work in the resulting dense open part, where every surviving \(F_i\) is open as well as closed; there the pieces are open, and density supplies a nonempty piece in every remaining open set.

For a closed nowhere-dense inclusion \(B\subset A\), the identity \(B\subseteq\operatorname{cl}(A\setminus B)\setminus(A\setminus B)\) and the o-minimal frontier dimension inequality give
\[
\dim B<\dim(A\setminus B)\leq\dim A.
\]
Thus a chain of the kind on 121/006 has at most \(n+1\) nonempty dimension levels inside \(\mathbb R^n\). Finally the component theorem gives the precise finite family of connected components, each definable, required by 121/010. The cited inputs are van den Dries–Miller 4.2, 4.3 and 4.7(1), checked in `turn49view1` and `turn56view0`; the displayed closure formula and decreasing-dimension application are the present verification.

### Q3-06 — The one-dimensional finiteness clause has a direct proof in this comparison

**Source:** 121/006 and 010; compared to 120/003 and 017. **Kind:** unpursued implication; explicit proof. **121 quote anchor:** “connexes”.

The early 121 construction decomposes a family member into finitely many locally closed pieces (121/006–009), and its clause (f) splits each piece into finitely many connected members; on \(X=\mathbb R\), a connected subset is an interval or a point, since a missing \(c\) between two of its points separates it into the relatively open parts below and above \(c\). Hence the manuscript's actual finite decomposition and finite-component operations give the one-dimensional finite interval/point conclusion in that real-line realization, and the Cantor set used in Q3-02 fails exactly the finite-component test. This **adds** a precise finiteness mechanism to C147/184's compact-stratification claim and bears on **WG2 B15 (§1.2)** without settling its open localization problem. **Confidence: high** in this elementary real-line argument; it does not attribute coordinate-projection or real-field closure to the early family on an arbitrary topological \(X\).

### Verification detail for Q3-06: the finite decomposition recursion

The finite locally closed decomposition used in that argument has an explicit recursion with precisely the written operations:
\[
A_0=A,\quad F_j=\operatorname{cl}(A_j),\quad
U_j=\operatorname{int}_{F_j}(A_j)
      =F_j\setminus\operatorname{cl}_{F_j}(F_j\setminus A_j),\quad
A_{j+1}=A_j\setminus U_j.
\]
All these sets remain in the Boolean family, each \(U_j\) is open in the closed set \(F_j\), and \(F_{j+1}\subseteq F_j\setminus U_j\) is closed and nowhere dense in \(F_j\) by the dense-interior clause. The descending-chain clause therefore ends the recursion, giving the required finite disjoint union \(A=\coprod_jU_j\); this verifies the step without inserting a cell-decomposition theorem as a new manuscript axiom.

### Q3-07 — Optional M0 is realized by all definable sets, with a calculated map comparison

**Source:** 120/007 and 021; 121/004 and 070–073. **Kind:** own construction. **120 quote:** “Oublions les structures topologiques”.

The family \(D_n=\mathcal S_n\) realizes M0, M1–M8 and M11: M6 uses \(q(x)=0\) on \(Z\) and \(q(x)=(1,x)\) off \(Z\), M7 extends a scalar function by zero off \(Z\), and the remaining clauses use the displayed Boolean, coordinate and field formulas. Its graph-defined arrows are all definable functions, and the compact-model inclusion sends each \(K_n\)-object and continuous definable arrow to the same object and arrow in this model; the step function \(f:[0,1]\to\{0,1\}\), \(f(0)=0\), \(f(x)=1\) for \(x>0\), is an explicit definable arrow whose graph omits its limit point \((0,1)\), so it is not an arrow of the compact-graph model. This **adds** the exact functor and its arrow-level limit beside C147/182's function-sheaf discussion and bears on **WG2 B15 (§1.2)** at its unchanged unchecked status. **Confidence: high**, from the piecewise formulas and the missing graph limit point; the Euclidean compactness axiom M9 is not asserted for \(D_n\), which contains \(\mathbb R\).

### Q3-08 — Local completion has an explicit inclusion and an explicit new section

**Source:** 120/019–020; 121/019–024. **Kind:** unpursued implication; reader's construction. **121 quote anchor:** “Localisation”.

For \(\mathcal F=D(\mathbb R)\), the map to the locally completed family is the literal inclusion \(A\mapsto A\), and the integer subset \(\mathbb Z\) belongs to the completion because every point has an interval meeting it in either a singleton or the empty set. It is absent from \(D(\mathbb R)\) by the finite interval/point clause; on compact definable \(X\), finitely many definable neighbourhoods cover \(X\), and the locally defined set is the finite union of its definable traces, proving equality of the two families there. This **adds** a tested sheaf-completion map to C147/182's presheaf-to-sheaf passage and bears on **WG2 B15 (§1.2)** and **BISITE D.12**, the latter remaining open in the supplied register. **Confidence: high**, because both the new section and the finite-cover reconstruction are explicit.

### Q3-09 — Cote 121's final scalar-extension question has the same verified modern witness

**Source:** 121/072–073 and 120/013–014. **Kind:** self-flagged question; construction answering it in the specified model. **121 quote anchor:** “Question”.

On the compact definable realization, the map requested on 121/073 is the restriction to \(X\) of the definable continuous extension from Aschenbrenner–Fischer, Lemma 6.6; the quotient coordinates and amalgam maps already displayed for M6–M7 then give the two-inclusion pushout. This **restates**, at the exact extension-map level, the operation in 120/013–014 and **adds** a model with witnesses beside C147/164 and 171's amalgam diagrams. It bears on **STRATA C.1/C.3/C.6** and **WG2 B15 (§1.2)** at the return-claim statuses stated above, without elevating them or the unchecked plan to a new settlement. **Confidence: high** for the compact definable construction, with the arbitrary-span scope question still recorded at A120-06.

### Q3-10 — The admissible scalar field records a genuine parameter choice

**Source:** 120/004–005, 021–023. **Kind:** own construction. **120 quote:** “\(R_0\) est un sous-corps de \(R\)”.

Keep the ambient topological field \(R=\mathbb R\), but take only compact semialgebraic subsets defined over the real algebraic field \(F=\mathbb R\cap\overline{\mathbb Q}\); the earlier M1–M11 verification still works, since projection preserves this coefficient field, the distance and extension formulas introduce no new parameters, and rational-endpoint intervals supply M10 at every real point. Here \(R_0=F\): every \(a\in F\) supplies its singleton, while a finite Boolean formula in polynomial signs over \(F\) is locally constant at a transcendental real number because none of its nonzero polynomials vanish there, so it cannot define that singleton. This **adds** an explicit parameter convention and its inclusion into the all-real-parameter model beside C149/105 and 122's field language, and bears on **WG2 B15 (§1.2)** without identifying that field with the arithmetic fields in those context pages. **Confidence: high**, from the sign calculation and the parameter-preserving formulas; the main realization Q3-01 deliberately used all real parameters, making \(R_0=\mathbb R\).

### Q3-11 — A real-closed-field interval tests the exact topological clauses

**Source:** 120/017–018; 121/010 and 072. **Kind:** unpursued implication; reader's explicit test. **120 quote:** “\(R\) séparé”; “compactes”.

For \(F=\mathbb R\cap\overline{\mathbb Q}\), the coefficient inclusion \(F\hookrightarrow\mathbb R\) induces the concrete interval embedding \(i:[0,1]_F\hookrightarrow[0,1]_{\mathbb R}\), and \([0,1]_F\) is definably compact by Peterzil–Steinhorn, Theorem 2.1, being closed and bounded in the pure real-closed-field structure. Choose a transcendental \(c\in(0,1)\): the cover consisting of \([0,1]_F\cap(-\infty,a)\) for \(a\in F,\ a<c\), and \([0,1]_F\cap(b,\infty)\) for \(b\in F,\ b>c\), has no finite subcover, because a finite choice leaves algebraic points between its largest \(a\) and smallest \(b\). The same cuts between any two algebraic points show that all topological connected components of \([0,1]_F\) are singletons, so this concrete interval fails both literal topological compactness and the finite-component test, despite its one-interval definable description. This **adds** a checked base-field map beside C149/105's field vocabulary and C147/184's compactness discussion, with **WG2 B15 (§1.2)** still unchecked; **confidence high**, because the cover and each separating cut are explicit.

### Verification detail for Q3-10: preservation of the scalar parameter field

The checked proof of Aschenbrenner–Fischer Lemma 6.6 gives this extension on a nonempty closed \(Z\), writing \(g=\tau\circ f\):
\[
\tau(t)=\frac32+\frac{t}{2\sqrt{1+t^2}},\qquad
G(x)=
\begin{cases}
g(x),&x\in Z,\\
\displaystyle\inf_{a\in Z}\frac{g(a)\,d(x,a)}{d(x,Z)},&x\notin Z,
\end{cases}
\qquad \widetilde f=\tau^{-1}\circ G.
\]
Every constant displayed is rational, the quantified variable \(a\) ranges over the already defined \(Z\), and distances and the infimum are specified by order-field formulas using only the coefficients of \(Z\) and \(f\); real-closed-field quantifier elimination consequently produces semialgebraic definitions over that same \(F\). This is the reason for parameter preservation in Q3-10, rather than an assumption that an unspecified definable extension automatically preserves parameters; the empty-domain case uses the zero extension.

### Scope of the joint answer

The supported positive correspondences are the compact definable model and its graph arrows, the all-definable realization of the optional-M0 algebraic branch, the explicit Boolean compactification formula Q3-03, the early 121 family \(D(X)\) with its finite-dimensional and finite-component properties, and the named analytic-geometric and weak-polytope constructions Q3-04/A120-24. The proved all-compact counterexample is scoped to **120 M1–M11 without optional M0**; it is not a counterexample to the early 121 finite-component requirement. The precise remaining verification for a claimed equivalence of the entire manuscript apparatus with an o-minimal structure is to identify the actual family in each finite power, show that the early 121 Boolean/finiteness operations apply to those same families, and account for the real-field and graph-map convention; the checked leaves do not supply that identification, and no theorem with those missing identifications inserted as hypotheses is proposed here.

### Cote 121 quotation ledger

The four external-primary French anchors in Q3-05, Q3-06, Q3-08 and Q3-09 contain respectively 3, 1, 1 and 1 words: **6 words total**, without repeating them here. The mathematical content above is paraphrased; the primary images remain research sources rather than additions to the diplomatic transcription. The Q4 worker was asked to use no additional verbatim 121 quotations without coordinating this shared 25-word cap.
