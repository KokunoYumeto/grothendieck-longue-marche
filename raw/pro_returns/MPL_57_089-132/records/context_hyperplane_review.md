# Post-freeze research memo: hyperplane comparison, Hua, and relative Picard existence

Prepared 2026-11-17 after the transcription freeze at **17:42:01 UTC**. This memo records research comparisons and editorial deductions only. No manuscript image was consulted by this reviewer, and no page transcription, combined transcription, doubts file, or inventory was changed. Every discrepancy below is a **post-freeze reading or statement question**, never a correction to the frozen text.

## Evidence and credit

The complete supplied `context/hua_project/57.modern.tex` (lines 1–2975), both context READMEs, and `context/notes/RESULTS_STATE.md` were read. Hua's file is an AI-produced modern interpretation, not an independent diplomatic witness or an established result of this package. Its page *n* normally corresponds to this package's scan *n* + 1; references below give both wherever needed.

Abbreviations: **F97:L13** means line 13 of `pages/MPL_57_089-132_57_scan097.tex`, relative to this package; likewise for other scans. **H** means `context/hua_project/57.modern.tex`; **RS** means `context/notes/RESULTS_STATE.md`; **CT** means `context/MPL_16+47+54+44_transcription.tex`; **CN57** means `context/same_cote_57/MPL_57_271-315_notes.md`. Those earlier transcriptions and notes are themselves supplied first-pass claims. Source titles, proposition numbers and local locators below allow the parent editor to cite the exact object rather than an unqualified project result.

The central register item is **Hua, findings register, 57-generic-hyperplane-h1-injective**, RS lines 21–24 and 455–459. RS calls it a conjecture/unsearched claim; that is the register's research status, not the heading or authorial presentation of F99.

## Recommended research notes (one to four sentences of discussion each)

### H01 — The generic-hyperplane claim is stated as a theorem, with a proof sketch

**File/scan:** F99:L3–24, L30–44; F100:L4–27.  
**Kind:** observation on authorial status.  
**Bears on:** Hua 57-generic-hyperplane-h1-injective; WG2 §1.1 #3.  
**Comparator/search:** Hua, modernised reading of cote 57, “La section hyperplane générique (pages 98 à 100),” H1446–1498; `Théorème`, `injectif`, `Bertini`, `vérification`.

F99 explicitly heads the claim “Théorème” and asserts injectivity, then reduces it to additive, finite and characteristic-p cases; F100 supplies Cartier-style differential reductions and ends the remaining lemma with “La vérification est presque triviale…”. It is therefore neither merely asked nor a fully written-out proof in these pages: the characteristic-zero specialization argument is announced, and several identifications and reductions still require checking. The appropriate revision to the register's description is **authorially asserted theorem with an incomplete written proof sketch**, without promoting Hua's modern reconstruction into verification.

### H02 — Exact hypotheses and the scope of G must remain visible

**File/scan:** F99:L3–20, L26.  
**Kind:** reading/statement question.  
**Bears on:** Hua 57-generic-hyperplane-h1-injective.  
**Comparator/search:** H1448–1465; `affine`, `composantes`, `comm.`, `dominant`.

The live hypotheses say that \(k\) is algebraically closed, \(X\subset\mathbf P^r_k\) is projective, normal and irreducible, and \(\dim X\ge2\); the target is the geometric generic hyperplane over \(\overline{k(t_1,\ldots,t_r)}\). The source describes \(G\) as affine and “sans composantes \(G_m\),” inserts finite algebraic groups as an example, and its structural reduction contains an uncertain reading “comm.”; Hua's cleaner phrase “commutative affine, finite or vectorial” is an interpretation, not the literal statement. The secure explicitly treated cases are \(G_a\), finite simple groups in the reduction, and \(\alpha_p,\mu_p\); the exact extension to all affine commutative groups without multiplicative composition factors should be stated as a scope question. The margin's dominant-map generalization is a proposal, not an extra proved hypothesis-free theorem.

### H03 — Modernizing the Frobenius formulas is a mathematical intervention

**File/scan:** F99:L36–44; F100:L8–21.  
**Kind:** post-freeze reading question and proof obligation.  
**Bears on:** Hua 57-generic-hyperplane-h1-injective.  
**Comparator/search:** H1467–1489; `F`, `Cartier`, `alpha_p`, `mu_p`.

Hua, modernised reading of cote 57, “La section hyperplane générique,” replaces the manuscript's superscript notation and its problematic multiplicative line by the modern identifications \(H^1_{\mathrm{fppf}}(X,\alpha_p)\simeq\ker(F:H^1(X,\mathcal O_X)\to H^1(X,\mathcal O_X))\) and \(H^1_{\mathrm{fppf}}(X,\mu_p)\simeq\operatorname{Pic}(X)[p]\), under the displayed proper integral/algebraically closed setting. These use the additive Frobenius and Kummer sequences and surjectivity on global constants; \(\alpha_p\) and \(\mu_p\) require flat cohomology rather than being silently treated as ordinary étale coefficients. Hua explicitly acknowledges changing the formulas in its footnote, so those changes belong in commentary only. A complete proof must also specify \(\widetilde\Omega^1\), justify the normality-based differential embeddings, and supply the announced specialization step.

### H04 — Constant classes are not the entire base-changed tangent space

**File/scan:** F99:L18, L24; F100:L25, L29–32.  
**Kind:** editorial logical distinction, high confidence.  
**Bears on:** Hua 57-generic-hyperplane-h1-injective; question about infinitesimal injectivity.  
**Comparator/search:** H1453–1455, H1491–1498 for Hua’s arrows and kernel account; F100:L29–32 alone for “sans partie fixe”; search terms: K, H^1, sans partie fixe (the last phrase is absent from Hua).

The asserted arrow has source \(H^1(X,G)\), not \(H^1(X_{\bar K},G_{\bar K})\): its input consists of classes defined over the original field. For \(G_a\), injectivity on that \(k\)-vector space need not imply injectivity of the restriction map on \(H^1(X,\mathcal O_X)\otimes_k\bar K\); the map \(k^2\to k(t),(a,b)\mapsto a+tb\) is injective, while its \(k(t)\)-linear extension has kernel generated by \((-t,1)\). Thus the theorem as written does not eliminate moving \(\bar K\)-linear tangent directions or, by itself, the infinitesimal kernel of the morphism of Picard schemes. This distinction accords with F100’s own description “sans partie fixe,” which Hua does not preserve, and must not be erased by changing the source field.

### H05 — Full Picard injectivity is false under the stated dimension-two hypotheses

**File/scan:** F99:L28 (deleted Picard corollary), L32–34.  
**Kind:** editorial counterexample to the deleted broad implication, high confidence.  
**Bears on:** Hua 57-generic-hyperplane-h1-injective; RS orientation question 1.  
**Comparator/search:** H1457–1489; `Pic`, `G_m`, `mu_p`, `injectif`.

The full Picard-injectivity corollary on F99 is visibly deleted, and \(G_m\) is excluded from the structural reduction. Explicitly, take \(X=\mathbf P^1\times\mathbf P^1\subset\mathbf P^3\) with its Segre embedding: a geometric generic hyperplane is a smooth divisor of bidegree \((1,1)\), hence a projective line, and the nontrivial bundle \(\mathcal O_X(1,-1)\) restricts to the degree-zero, therefore trivial, bundle on it. This example meets the live hypotheses on \(X\) and proves that they cannot give injectivity of the full abstract Picard group. The \(\mu_p\) and \(\alpha_p\) statements concern particular torsion and Frobenius directions and do not repair that deleted conclusion.

### H06 — The surviving Picard conclusion permits an infinitesimal kernel

**File/scan:** F100:L29–32; F101:L2.  
**Kind:** observation and limitation.  
**Bears on:** Hua 57-generic-hyperplane-h1-injective.  
**Comparator/search:** H1491–1498; `p-groupe`, `unipotent`, `purement`, `propre`.

The surviving corollary concerns the base-changed \(\operatorname{Pic}^{\tau}\) morphism and describes its kernel as a finite unipotent \(p\)-group, with “purement infinitésimal” in the margin and “sans partie fixe” in the body. Hua preserves the finite-unipotent assertion, but this is weaker than a zero scheme-theoretic kernel: a nontrivial finite local group scheme can have only the identity geometric point. Neither torsion point injectivity nor injectivity on the original \(k\)-defined additive classes establishes the missing full tangent or functorial injectivity. The separate properness insertion on F100 has the unresolved exponent 0/τ, and the reduction through normal hyperplanes and then curves on F100–101 has its own details to check.

### H07 — The Picard-zero row of the table needs a statement-level qualification

**File/scan:** F97:L4–19, L30–35.  
**Kind:** post-freeze reading/statement question, with editorial test.  
**Bears on:** WG2 §1.1 #3; Hua hyperplane section.  
**Comparator/search:** Hua, modernised reading of cote 57, “Le tableau (page 96),” H1402–1444, especially H1409–1416 and H1426–1428; `bijectif`, `général`, `Pic^0`.

Both the frozen table and Hua's reading give \(\operatorname{Pic}^0(X)\to\operatorname{Pic}^0(Y)\) as bijective for \(n\ge2\) and general \(Y\), while Hua expressly says it has not rechecked every cell. Taken as the full Picard varieties this fails for \(X=\mathbf P^2\) embedded by \(\mathcal O(3)\), whose general hyperplane section is a smooth cubic: the source Picard variety is zero and the target is an elliptic curve. This is a reason to ask whether a dimension bound, a fixed-part qualification, or the intended object is suppressed, not to alter the literal row. The table's no-cohomological-hypotheses surjectivity and “Démonstration algébrique ???” remain explicit authorial questions.

### H08 — The exact SGA 2 comparison retains the cohomological hypotheses

**File/scan:** F97:L13–14, L27, L30–35; F99:L30, L36.  
**Kind:** published comparison.  
**Bears on:** RS orientation question 2.  
**Comparator/search:** Grothendieck et al., *SGA 2*, XII, Corollaries 3.5–3.6, original p.153/recomposed p.121/PDF p.129; `SGA 2 Exposé XII Corollaire 3.6`, `Picard hyperplane dimension 4`.

SGA 2 XII.3.6 retains cohomological vanishings; global bijectivity also requires parafactoriality off the divisor. See the final notes for the full hypothesis comparison; this memo preserves only the reference and retrieval record.

### H09 — The depth/descent lemma is an actual argument, with a broader proposed margin

**File/scan:** F102:L2, L11–37; F103:L2.  
**Kind:** proof comparison and reading question.  
**Bears on:** WG2 §1.1 #3.  
**Comparator/search:** Hua, modernised reading of cote 57, “Picard et profondeur (pages 101 et 102),” H1512–1536; `profondeur`, `cartésien`, `surj`, `i_*`.

The page proves its Cartesian square through full faithfulness on \(U\), the candidate extension (i_*F), flat base change, and faithful-flat descent of local freeness. The depth-at-least-two margin is a proposed enlargement of the category and needs its own precise quasi-coherence and finiteness conditions. Hua changes the doubtful inverse-image notation to \(U'=f^{-1}(U)\), and states only the injective/bijective corollary, whereas F103 also includes “surj.” The difference should be registered as a reading or omitted-case question; the frozen alternatives are preserved.

### H10 — The Laurent-variable properness argument has its own proof obligation

**File/scan:** F101:L6–20.  
**Kind:** post-freeze reading question.  
**Bears on:** WG2 §1.1 #3.  
**Comparator/search:** Hua, modernised reading of cote 57, “La section hyperplane générique,” H1500–1510; `surjectif`, `platitude`, `convenable`.

F101 states properness of \(\operatorname{Pic}^0\) for geometrically normal projective \(X\) and reduces it to a Laurent-variable Picard surjectivity lemma, changing an earlier “bijectif.” Hua's clean account says the divisor-closure step follows by “stabilité,” whereas the frozen text says “platitude,” and its “convenable” replaces a doubtful marginal word. The precise argument should establish descent of local principality under the relevant faithfully flat map and identify the divisor obtained by pullback, not merely appeal to the plausibility of the result. These discrepancies do not authorize post-freeze lexical repairs.

### H11 — Connections and universal extensions supply a real but unfinished comparison

**File/scan:** F89:L3 onward; F91:L2–26; F92:L2–20; F94:L2–22.  
**Kind:** unpursued implication.  
**Bears on:** WG2 §1.1 #3; WG2 §2.4 #4.  
**Comparator/search:** Hua, modernised reading of cote 57, “Fibrés à connexion et extension du dual d'une variété abélienne,” especially “L'extension vectorielle universelle (pages 90 à 93),” H1271–1397; `universelle`, `connexion`, `fonctorialité`, `classe`.

Hua identifies the construction with universal vector extensions and the mixed cohomology components of the Poincaré class. The frozen text supports that programme but says “Je voudrais l'interpréter” on F92 and leaves the mixed-component calculation at “on trouve ce qu'on … pense” on F94. These words distinguish a proposed identification from a fully checked canonical isomorphism, especially before functoriality and the stated cohomological-flatness hypotheses are supplied. This material offers a useful comparator for the abelian/Picard programme, without completing cote 47's Fourier compatibility check.

### H12 — Seshadri's theorem is modernized with stronger explicit fibre assumptions

**File/scan:** F105:L2 and following proof; F113:L2–8.  
**Kind:** statement/reading question.  
**Bears on:** WG2 §1.1 #3.  
**Comparator/search:** Hua, modernised reading of cote 57, “Le théorème de Seshadri (pages 103 à 113),” H1538–1585; `S_2`, `séparable`, `intègre`, `D`, `expliciter`.

Hua formulates this discussion using geometrically integral fibres, (S_2), and effective divisors, and expressly explains why effectiveness is needed. F105's first statement instead visibly gives (S_2), an inserted separability/(R_0) condition, and existence plus essential properness of the Picard object; later integral-fibre uses and the move between arbitrary and positive divisors must be checked against that precise scope. F113's changes from divisor to 1-cycle and removal of “Cartier” show additional work on the statement itself. Treat Hua's streamlined hypotheses as a reconstruction to test, not as a recovered clean original theorem.

### H13 — The vertical-divisor argument is not complete in the surviving text

**File/scan:** F122:L8–22; F123:L4–41.  
**Kind:** self-flagged proof gap and Hua comparison.  
**Bears on:** WG2 §1.1 #3.  
**Comparator/search:** Hua, modernised reading of cote 57, “Séparation : unités et diviseurs à support dans les fibres (pages 114 à 123),” H1587–1649; `Non démontré`, `réduit`, `incidence`, `div`.

F122 explicitly marks Corollary 5 “Non démontré,” and F123 warns that the required intersection \(X_i\times_XY\) is not known to be reduced. Hua's account presents an incidence argument as reaching the vertical-divisor conclusion and even writes a fractional principal-divisor normalization absent from F123's literal line. A proof must justify the reducedness or replace the unit-factorization step where it is used before the componentwise exponents can be identified. The supplied pages therefore add a substantive authorial warning missing from the streamlined modern account.

### H14 — The triviality-locus theorem retains visible fibre conditions

**File/scan:** F124:L15.  
**Kind:** post-freeze statement question.  
**Bears on:** WG2 §1.1 #3.  
**Comparator/search:** H1640–1649; `n(y)`, `composantes`, `universellement`, `fermé`.

F124 visibly includes locally constant numbers of absolute irreducible fibre components and an uncertain universal degree-zero cohomology condition before its largest closed triviality-locus claim. Hua says the page stops before the fibre conditions, and describes the condition on the line bundle as coming from the base. The frozen wording instead speaks of being isomorphic to the trivial bundle and contains an uncertain base/target phrase. These differences demand an exact representability-and-base-change formulation rather than silently choosing Hua's more standard meaning.

### H15 — The relative-existence proof contains a third compatibility condition absent from Hua

**File/scan:** F126:L5–20; F127:L9–33; F128:L2–13.  
**Kind:** post-freeze reading question.  
**Bears on:** RS orientation question 2; WG2 §1.1 #3.  
**Comparator/search:** Hua, modernised reading of cote 57, “Le principe : recoller par descente (pages 125 à 128),” H1654–1704; `rigidification`, `c)`, `M,N,P`, `descente`, `prod`.

Hua says the third condition is cut off and models only \(K,L,M,N\), whereas F127 explicitly gives \(\bar g'_T{}^*\psi=\psi'_T\), and F128 adds \(P\), a third pair of arrows, and \(N\times P\). F126 also records a substantial list of flatness, universal \(f_*\mathcal O\), descent, and effective-descent hypotheses, and cancels a Weil-restriction factor that Hua retains in its cleaned target. The frozen witness supplies additional rigidification data but leaves a target/base interpretation question; none of these annotations may be discarded to make the argument look finished. The diagrams must be compared as written before their objects are identified.

### H16 — The compatibility equation appears to require a simultaneous equalizer

**File/scan:** F127:L20–23; F128:L7–13.  
**Kind:** editorial proof-completion proposal, with qualification.  
**Bears on:** relative-existence proof.  
**Comparator/search:** H1674–1690; `phi`, `psi`, `U`, `V`, `égal`.

Condition b), \(\bar q_2^*\psi=i''{}^*\varphi\,\bar q_1^*\psi\), depends on both the descent isomorphism \(\varphi\) and the rigidification \(\psi\), so the independent equalizers on \(K\) and \(L\) and the product \(U\times_SV\) do not follow as written. A precise editorial construction places all three equations on \(K\times_SL\), using its two universal isomorphisms and affine separated Hom targets, so that their simultaneous equalizer is closed and affine. Suppressed dependence of \(L\) or its arrows on a previously chosen \(\varphi\), with base changed to \(K\), could explain the shorthand, but the displayed text calls them \(S\)-schemes and does not state this. Hua's similar separation of the conditions, together with its omission of \(P\), does not independently complete this point.

### H17 — FGA V gives close published existence comparators, with exact scope

**File/scan:** F126–129, F131; compare F105.  
**Kind:** primary published comparison.  
**Bears on:** RS orientation question 2.  
**Comparator/search:** Grothendieck, Bourbaki exposé 232, *Les schémas de Picard : théorèmes d'existence* (February 1962), Theorem 3.1 and Proposition 6.3/Corollary 6.4; `Grothendieck Picard 232 Numdam`, `théorèmes existence relatifs`.

FGA V, Theorem 3.1 and Proposition 6.3/Corollary 6.4 are the existence and gluing comparators. Their precise hypotheses are recorded in the final notes; this memo preserves the references.

### H18 — Modern algebraic-space existence does not automatically settle scheme existence

**File/scan:** F126:L7–20; F127:L2; F129:L9.  
**Kind:** scope comparison.  
**Bears on:** RS orientation question 2.  
**Comparator/search:** The Stacks Project, Proposition 99.11.8, Tag 0D2C; `Picard scheme proper flat geometrically integral fibres existence`.

Stacks Tag 0D2C concludes representability by an algebraic space. See the final notes for its full hypotheses and the comparison with manuscript scheme existence.

### H19 — The comparison with cote 44 is at the divisor level

**File/scan:** F97–100; CT, cote 44:4, Theorem 6, CT2860–2886.  
**Kind:** unpursued implication.  
**Bears on:** WG2 §2.4 #4; WG2 §2.3 #12.  
**Comparator/search:** CN57 J06, lines 97–104; `hyperplan`, `facteur fixe`, `2i`, `bijectif`.

Cote 44's Theorem 6 distinguishes an isomorphism range, a fixed-factor assertion in the critical degree, and a surjectivity range for its higher \(P^i\) objects. The present Picard and torsor discussion is an explicit divisor-level comparison, and its “sans partie fixe” deserves comparison with that critical-degree language. It does not construct all higher representatives, establish those three ranges, or complete their dualities and polarization claims. CN57 J06 is a useful supplied lead about later hyperplane questions, not an established proof of the numbered theorem.

## Other parts of Hua's full reading and their relation to this selection

| Hua section and file lines | Current scans or status | What the comparison contributes or limits |
|---|---|---|
| “Fibrés à connexion et extension du dual d'une variété abélienne,” H1271–1397 | 89, 91–92, 94; the section begins earlier than this selection | The main direct comparator for connections, extension classes and the universal-extension aspiration; see H11. |
| “Critères d'équivalence par section hyperplane,” H1399–1510 | 96–97, 99–101 | The principal theorem/table comparison; both modern normalizations and admitted unchecked cells must be distinguished. |
| “Picard et profondeur,” H1512–1536 | 102–103 | Cartesian-square descent and the extra source corollary case. |
| “Le théorème de Seshadri,” H1538–1585 | 104–114 | Modern reconstruction of positivity and fibre hypotheses, not a literal second witness. |
| “Séparation : unités et diviseurs à support dans les fibres,” H1587–1649 | 115–124 | Unit extension, vertical divisors, and a claimed closed triviality locus; the frozen nonproof/reducedness warnings materially qualify it. |
| “Théorèmes d'existence relatifs,” H1651–1750 | 125–129, 131; later subsections extend beyond scan132 | “Le principe” directly compares; “Le noyau pour un morphisme surjectif” (H1706ff.) and the Leray subsection discuss later pages, so cannot be reported as newly witnessed here. |
| Hua's account of reused typescripts, H1–102 and H277–287 | 90, 93, 95, 117, 119, 130, 132 | Hua deliberately does not reconstruct every foreign reused typescript; absence there gives no evidence that the present annotations are unimportant or duplicates. |
| “Le Picard des schémas en courbes,” H1751ff.; “Le foncteur de Picard,” H1953ff.; formal/analytic and later questions sections | Outside scans89–132 | Useful context for descent, torsors and Picard functors, but not additional witnesses to this selected sequence. |

The full reading also discusses local Picard groups, component/torsion variation, degeneration examples, the Hironaka letter, analytic/formal comparison, Néron–Severi schemes, Igusa examples, pinching, and later open questions. None was used to fill a missing word or replace a cancelled claim in this selection. In particular, the later hyperplane questions near Hua pages308–310 show a continuing programme; they do not retroactively turn F99's incomplete sketch into a completed proof.

## Two independently checked deductions answering scan120's margin

### E01 — Affineness is essential for the stated extension criterion

**File/scan:** F120:L5–18, especially the first marginal question.  
**Kind:** editorial counterexample; high confidence; not the source's completed proof.  
**Search:** `affine`, `contre-exemple`, `section rationnelle` in the frozen page and Hua's separation section.

Let \(X=\mathbf A^2_k=\operatorname{Spec}k[x,y]\), \(f=x\), \(Y=V(x)\), and \(Z=X\times\mathbf P^1\), and take the rational section \(g(x,y)=[x:y]\). It is defined on \(D(x)\) and on a neighborhood of the generic point of \(Y\), while \(X\) is regular and excellent, \(f\) is regular and \(Y\) is reduced, so the page's other indicated ring/divisor assumptions hold. Any extension at the origin would restrict to the constant value \([1:0]\) along the punctured \(x\)-axis and \([0:1]\) along the punctured \(y\)-axis; separatedness forces the respective values at the origin, a contradiction. Thus replacing an affine \(Z/X\) by even a projective smooth \(Z/X\) invalidates the conclusion.

### E02 — Reducedness along Y follows from the live local hypotheses

**File/scan:** F120:L2–9, L18.  
**Kind:** editorial local proof; high confidence; not the source's completed proof.  
**Search:** `réduit`, `non diviseur`, `locale` in the frozen page and Hua's separation section.

At \(y\in Y\), put \(A=\mathcal O_{X,y}\), with nilradical \(N\), and keep the hypotheses that \(A\) is noetherian, \(f\in\mathfrak m_A\) is a nonzerodivisor and \(A/fA\) is reduced. Then \(N\subset fA\), and if a nilpotent \(n=fa\), the equation \(f^ma^m=0\) and regularity of \(f^m\) imply that \(a\) is nilpotent, so \(N=fN\). Since \(N\) is finitely generated, Nakayama gives \(N=0\). Hence the separate reducedness assumption at points of \(Y\) is redundant under the live hypotheses, matching the local direction of the margin; the section is already defined on \(D(f)\), so no additional reduction argument there is needed for extension.

## Published sources checked and retrieval record

The fuller published comparisons are retained in the final notes. The duplicate summaries above were condensed on 2026-11-17 to keep their aggregate source-derived wording small; exact sources and retrieval locators remain here.

1. **Grothendieck et al., SGA 2**, recomposed edition, 2005. [Primary PDF](https://arxiv.org/pdf/math/0511279). XII.3.5–3.6, recomposed pp.120–121, PDF pp.128–129, original marginal pp.152–153; extracted lines5681–5715. Tool references: `turn395487664view0`, `turn191735349view0`, `turn191735349view1`. Original indexed PDF: [wstein SGA2](https://wstein.org/sga/sga/pdf/sga2.pdf), `turn511427572search7`. Opening that file failed because of its size. The arXiv extraction drops inequality bars; the original indexed extract preserves them. Screenshot calls returned textual placeholders without accessible image content; no visual check is claimed.

2. **Grothendieck, A. (1962), “Technique de descente et théorèmes d'existence en géométrie algébrique. V. Les schémas de Picard : théorèmes d'existence,” Bourbaki exposé232, pp.143–161.** [Primary Numdam PDF](https://www.numdam.org/article/SB_1961-1962__7__143_0.pdf). Theorem3.1, Proposition6.3, Corollary6.4: PDF pp.7–8 and17–18; extracted lines169–181,409–433. Tool references: `turn395487664view1`, `turn191735349view2`, `turn191735349view3`.

3. **Grothendieck, “Erratum à l'exposé n°232” (1962), p.303.** [Primary Numdam PDF](https://www.numdam.org/item/SB_1961-1962__7__303_0.pdf), `turn395487664view2`, lines14–28. Read as an additional chronology/scope check; no broad conjecture in the original exposé was treated as a current theorem.

4. **The Stacks Project Authors, Proposition99.11.8, Tag0D2C.** [Official source](https://stacks.math.columbia.edu/tag/0D2C), `turn464703110view1`, lines22–32. A mirror was a discovery lead only.

**Parent citation handoff:** reopen the exact primary passages before final web citation. English translations and MathOverflow served only as discovery leads. The substantive literature comparisons belong in the final notes, avoiding duplicated paraphrase across this memo and those notes.

## Context and web search log

All searches/readings below occurred after freeze. The searches were restricted to supplied context/workspace files or public primary literature; no unavailable archive source was silently substituted.

| Search/read | Files or service | Outcome and boundary |
|---|---|---|
| Sequential read of all 2975 lines | H; both READMEs | Complete Hua reading, including out-of-selection topics; modernizations and stated omissions recorded. |
| Sequential read of RS1–503 | RS | Exact Hua finding, planning IDs and limits of existing claims recorded; RS itself says no current result bears directly. |
| `57-generic-hyperplane`, `Hua`, `SGA2`, `existence` | RS | Orientation lines21–24 and finding line459 are the direct prompts. |
| `hyperplan`, `Lefschetz`, `Seshadri`, `profondeur` | CT | Cote44:4/Theorem6 is the close programme comparator; earlier cote16 Lefschetz algebra and letters are distinct higher-cycle/operator questions. |
| `hyperplan`, `Lefschetz`, `Seshadri`, `rigidification`, `profondeur`, `existence`, `H9`, `LM7`, `E.23` | RS, CN57, earlier supplied notes | Returned many subject-level leads; exact CN57 J03–J06 and D07/E08 examined as unreviewed comparisons, not proofs. |
| Exact reads F97,99–103 | Frozen page text | Theorem heading, deleted Pic corollary, source field, finite infinitesimal-kernel statement, Cartesian proof and “surj” case checked. |
| Targeted `Fonctor`, `S_2`, `Non démontré`, `réduit`, `n(y)`, `c)`, `Hom`, `Sigma`, `rigid`, `plat`, `prod` | Frozen89,91–92,94,105,113,122–129,131 | Exact locators for differences from Hua and authorial proof obligations. |
| Exact read F120 and F127–128 | Frozen page text | Parent-requested affine/reducedness deductions and coupled-equalizer issue independently checked. |
| `SGA 2 Exposé XII Corollaire 3.6 Picard groupe projectif dimension4`; `SGA 2 exposé XII corollaire3.6 Picard hyperplane dimension4` | Public web search | Original PDF indexed excerpt, translations and secondary leads; original updated PDF subsequently opened. |
| `site.stacks.math.columbia.edu Picard scheme existence flat projective geometrically integral fibres`; `Picard scheme proper flat geometrically integral fibres existence` | Public web search | Tag0D2C located via mirror, then official primary page checked. |
| `SGA2 Grothendieck Laszlo pdf 3.6 3.5 XII 2005`; `Grothendieck techniques construction schémas existence IV Picard232 Numdam1962` | Public web search | Primary arXiv edition, Bourbaki232 and erratum located and read at the cited theorem passages. |
| `Corollaire3.6`, `3.1.`, `projectif` | Finds within primary PDFs | Exact SGA/FGA hypotheses and relative-existence comparison extracted. |

## Register implications and outstanding work

No existing result in RS is used as settling these Picard questions. **LM7 E.23** and **LM6 A.22** remain only distant Jacobian-related subject links: these pages do not calculate section classes, arithmetic Galois images, CM normalizers or their required profinite invariants. The direct planning connections are **WG2 §1.1 #3**, **WG2 §2.4 #4** and, at the higher-cycle boundary, **WG2 §2.3 #12**; **WG H9** is not upgraded by a Picard restriction discussion.

The strongest verified local outcomes here are the exact authorial-status distinction, the source-field distinction, the Segre-surface counterexample to the deleted full-Picard inference, the two explicit scan120 deductions, and the coupled-condition issue in the affine equalizer proof. A complete modern proof of the author's full permitted-G theorem, or a scheme-theoretic generic-hyperplane injectivity theorem under strengthened hypotheses, is not claimed. The comparisons remain research notes against the frozen diplomatic text.
