# Q1 — Tubulure and ombre: verified constructions and the remaining identification

Research opened after the transcription freeze of 2026-11-14 16:52:13 UTC; `context/README.md` and `context/notes/RESULTS_STATE.md` were read before these notes were written. The supplied 38 scan images were not opened, and no frozen transcription, inventory, doubts file, or progress log was edited. Public originals inspected here are outside that set.

## Answer and scope

**An earlier, securely dated étale-tubular passage is now located:** Grothendieck's autograph letter to Larry Breen of 17/19 July 1975, preserved in cote 134-2, current PDF scan 174, manuscript p. 29; the date is on current PDF scan 146, manuscript p. 1. For the neighborhood constructions, cote 147/140–142, cote 150/12–16, and cote 151/27–29 provide increasingly explicit data, recorded below. The literal nouns in cote 149/133 remain a question of precise identification: this search has not located a definition with an explicit comparison morphism identifying its $X_J$ or $\widehat X$ with one of these constructions.

Two other primary uses of *ombre* have been checked rather than discarded: the graded-module construction in cote 136 and the pointed-conformal-disc map in cote 67. Their actual maps are recorded in Q1-06 and Q1-07. Their relationship to the localization along $D_J$ in cote 149 remains unproved in the passages examined; no claim that such a relationship is impossible is made.

The checked original pages are a bounded selection, listed in the source ledger. The wider discovery search used public machine transcriptions as an index only: its omission of the words visible on 149/133 demonstrates that negative index results cannot establish absence from the manuscripts. Accordingly, the 1975 letter is an earlier located passage, not a proved first introduction in the whole archive.

## Short research notes

### Q1-01 — What 149/133 actually supplies

**Kind:** reading question; primary verification. **Source:** cote 149, PDF scan 133, archive footer 132, manuscript p. 66. **Anchors:** “ombres”; “tubulures étales”.

The three relevant places are the insertion above the completion of $X$ along $D$, the parenthesis describing the localization of $X$ along $D_J$, and the left-margin preference for étale tubulures. The notation fixes $\widehat X$, $X_J$, and the stated trace $U_J$ operationally, but this page supplies no site, universal property, or explicit comparison morphism that identifies the named *ombre* with a construction found elsewhere in this search. The original image supports both noun readings at moderate confidence, while the supplied transcription correctly retains uncertainty; the frozen text has not been changed. This **restates** the question in the supplied 149 notes and **adds** direct verification of the three places.

**Context search:** `context/MPL_149_091-136_transcription.tex`, scan 133; `context/MPL_149_091-136_notes.md`, scan 133, notes 133.2, 133-R0, 133-R1, 133.4; all context files searched for `ombre`, `tubulure`, `D_J`, and `\hat X` (Q1-01 in `q1_context_by_note.json`). **Register:** INTAKE 20261114 §13.2 — intake reading, not a referee verdict; WG2 §1.8 #5 and §1.1 #6 — unchecked plans; EXIT_ONE_TYPE P4e and FLAGGED_149 ZD8 — “Proved” as return claims, not promoted here to verified results. **Relation:** restates / adds; no verdict on those mathematical claims.

### Q1-02 — The dated 1975 étale-tubular passage

**Kind:** historical source; proposed construction. **Source:** cote 134-2, PDF scans 146 and 174–175, archive footers 145 and 173–174, manuscript pp. 1 and 29–30. **Anchor:** “voisinage tubulaire étale”.

In the letter to Breen dated 17/19 July 1975, Grothendieck writes the two-stratum sheaf data $F_0,F_1,F_0\to i_0^*i_{1*}F_1$ and proposes describing this last functor through an étale tubular topos of $X_0\subset X$. The following page gives the topological model, with $p:\partial T\to X_0$: $T=(\partial T\times[0,1])\amalg_{\partial T\times\{1\}}X_0$ and $T\setminus X_0\simeq\partial T\times[0,1[$. The étale construction is presented as a project he thinks possible; the concrete quotient and the 1975 date are directly visible. This **adds** an earlier dated source to the neighborhood language of 147/140 and the étale wording of 149/133, without asserting a first occurrence throughout the archive.

**Context search:** `context/MPL_147_138-190_transcription.tex`, scans 140–142 and 180; `context/MPL_149_091-136_transcription.tex`, scan 133; `context/STATEMENTS_WITH_STATUS.md`, STRATA C.1–C.8; all context files searched for tubular-neighborhood wording, recollement and the two inclusion indices (Q1-02 ledger). **Register:** WG2 §1.8 #5 — unchecked glossary plan; INTAKE 20261114 §13.2 — intake reading; EXIT_ONE_TYPE P1d1 — “Proved” as a return claim. **Relation:** adds a primary historical construction, with no reproof of coherent gluing.

### Q1-03 — The germ and its canonical maps in 147

**Kind:** definition / stated functoriality. **Source:** cote 147, PDF scans 140 and 142, archive footers 139 and 141, manuscript pp. 69–70. **Anchor:** “germe”.

For a local immersion $D'\to Y$ of smooth analytic spaces, 147/140 introduces the tubular neighborhood as a germ of analytic space around $D'$, explicitly independent of the additional normal-crossings divisor. Scan 142 envisages a direct topological/topos definition and records, for $D''\to D'\to Y$, the canonical diagram whose lower row is $\mathcal V_{D'',Y}\to\mathcal V_{D',Y}\to Y$ and whose upper row is $D''\to D'$. The qualification accompanying the proposed topological definition must remain attached to it: these pages state the germ construction and maps, while a full site construction is not written in the checked passage. This **restates** the supplied first-pass reading and **adds** original-page verification, giving a precise adjacent object for the glossary question.

**Context search:** `context/MPL_147_138-190_transcription.tex`, scans 140–146, 157–164; `context/MPL_147_138-190_notes.md`, notes attached to scans 163–164; Q1-03 ledger searches `germe`, local immersions and the $V$ notation in every context file. **Register:** EXIT_ONE_TYPE P1a1 and P1d1 — “Proved” as return claims; WG2 §1.8 #5 — unchecked plan. **Relation:** restates / adds source verification; neither claim is re-proved here.

### Q1-04 — The provisional neighborhood-limit description in 151

**Kind:** provisional definition. **Source:** cote 151, PDF scans 27–29, archive footers 26–28. **Anchor:** “à titre provisoire”.

For closed $Y\hookrightarrow X$ with $X$ paracompact, scan 28 proposes $V_{Y,X}$ as the germ around $Y$, regarded as a topos through the displayed projective limit of open neighborhoods. Scan 29 defines $V^*_{Y,X}=V_{Y,X}\cap(X\setminus Y)=V_{Y,X}\setminus Y$ and the span $V^*_{Y,X}\to V_{Y,X}$, $V^*_{Y,X}\to X\setminus Y$. This **adds** an explicit neighborhood-indexed description to 147/140–142 and **restates** the germ/punctured-germ pattern of the supplied 147/163–164. The heavily revised homotopy-equivalence paragraph on scan 28 is not treated as a settled assertion.

**Context search:** `context/MPL_147_138-190_transcription.tex`, scans 140–142, 157–164; `context/MPL_149_091-136_transcription.tex`, scan 133; all context searched for open neighborhoods, germs, $V$ notation and topological limits (Q1-04 ledger). **Register:** INTAKE 20261114 §13.2 — intake reading; MPL_150_085-099+151_001-031 §106–107 — first-pass research leads; EXIT_ONE_TYPE P1d1 — return claim. **Relation:** adds / restates; exact identification with $X_J$ remains a question.

### Q1-05 — The conical definition and an exact comparison of its parameters

**Kind:** definition; reader's concrete comparison. **Source:** cote 150, PDF scans 12 and 22, archive footers 11 and 21, manuscript pp. 1 and 6; relative version begins PDF scan 13; comparison source 134-2/175. **Anchor:** “cocartésien”.

Cote 150/12 specifies $Y\subset T$, a closed boundary $\dot T$, and a multiplicative $[0,1]$-action with $\lambda y=y$, $0T\subset Y$, and pushout square $\{0\}\times\dot T\to Y$, $[0,1]\times\dot T\to T$, giving $T=C(f)$, $f(x)=0x$, via $[(\lambda,x)]\mapsto\lambda x$. Scan 22 defines a germ by equality $\lambda T=\lambda'T'$ of rescaled neighborhoods with matching conical structures over $Y$. For the same $f$, the endpoint-one quotient of 134-2/175 maps to the endpoint-zero quotient by $[(x,t)]\mapsto[(1-t,x)]$, $y\mapsto y$, with inverse $[(\lambda,x)]\mapsto[(x,1-\lambda)]$. This concrete comparison has high confidence because both formulas preserve the quotient relations and compose to identities; the comparison map to 149's $X_J$ remains unspecified.

**Context search:** `context/MPL_147_138-190_transcription.tex`, scans 140–142 and 190 (tubular neighborhoods and local fibrations); `context/MPL_149_091-136_transcription.tex`, scan 133; all context searched for conical, cone, pushout and action notation (Q1-05 ledger, together with the Q1 tubular-germ search). **Register:** INTAKE 20261114 §13.2 — intake reading; WG2 §1.8 #5 — unchecked plan; EXIT_ONE_TYPE P1a1 — return claim. **Relation:** adds a verified definition and a concrete coordinate comparison; no conditional theorem is proposed.

### Q1-06 — A checked definition of module shadows in 136

**Kind:** definition; unresolved comparison. **Source:** cote 136, PDF scans 23–26, archive footers 22–25; cover at PDF scan 2. **Anchor:** “ombres virtuelles”.

Here $S=k\{T\}$ is the divided-power polynomial algebra, $S^{+(N)}=\bigoplus_{i\ge N}kT^{(i)}$, and scan 25 writes $\omega_0(M)=M\otimes_k S$, $\omega_N(M)=S^{+(N)}\omega_0(M)$; scan 26 calls the $\omega_N$ shadow functors and introduces $\mathrm{Omb}(k)$ through graded $S$-modules, with a question mark on the proposed lower grading bound. The recovery map is written $M\to\pi_N(\omega_N(M))$, $x\mapsto(xT^{(i)})_{i\ge N}$, where $\pi_N$ selects compatible families $T^{(j)}x_i=\binom{i+j}{i}x_{i+j}$. Scan 23 visibly has an $S$ under its first tensor sign, so the scan-25 formula is cited without silently altering that earlier line. This **adds** an explicit lexical and mathematical definition; no morphism from this construction to the $X_J$ or $\widehat X$ of 149/133 has been established in the checked passages.

**Context search:** every supplied context file searched for `ombre`, `omega_N`, `pi_N`, divided powers and graded-module wording; the noun hits meet `context/MPL_149_091-136_transcription.tex`, scan 133 and its notes, while the module formulas are newly located external material (Q1-06 ledger). **Register:** WG2 §1.8 #5 — unchecked glossary plan; INTAKE 20261114 §13.2 — intake reading of the previously bounded corpus. **Relation:** adds; it does not contradict an absence claim limited to 147/138–190 and 150/1–43. **Dating:** catalogue range begins 1975–1976; no autograph date on these checked leaves establishes their individual day or year.

### Q1-07 — A checked pointed-disc shadow map in 67

**Kind:** definition; unresolved comparison. **Source:** cote 67, PDF scans 63–64, archive footers 62–63, pencil numbers 65–66, manuscript p. 6 on scan 64. **Anchor:** “ombre de D”.

For fixed $(X',a)$, scan 63 considers compact pointed conformal discs $D\subset\operatorname{Int}(X')$ with the stated rectifiability condition on $\partial D$, associates a Euclidean disc in $T_{X',a}$ compatible with its conformal structure, and scan 64 names the map $D\mapsto o(D)$. It records compatibility with concentric rescaling, $o(\lambda D)=\lambda o(D)$, for $0<\lambda\le1$. This **adds** another explicitly mapped use of the noun, while its comparison with the localization along $D_J$ in 149 remains open in the checked material. The catalogue's range, beginning in 1977 and extending to 1984, does not date these individual leaves before the 1983 notes.

**Context search:** `context/MPL_149_091-136_transcription.tex`, scans 133–134; `context/MPL_147_138-190_transcription.tex`, scans 163–164; frozen `work/MPL_152+120_transcription.tex`, cote 152 scans 3 and 11 (disc data); all context searched for shadows, discs, the tangent notation and homotheties (Q1-07 ledger). **Register:** WG2 §1.8 #5 — unchecked glossary plan; INTAKE 20261114 §13.2 — bounded intake reading. **Relation:** adds a lexical construction; the occurrence of discs alone supplies no comparison map to the 152 data or to 149.

## Source and search ledger

### Primary originals actually inspected

All scan numbers below count the modern initial PDF cover. The archive footer generally equals PDF scan minus one; pencil numbers are separately reported where they differ. Local extracts preserve the original images and their hashes are recorded in `q1_primary_extract_manifest.json`; the original-source copies are outside `work/`.

| Source URL | Exact checked location | Passage checked / use |
|---|---|---|
| <https://grothendieck.umontpellier.fr/149.pdf#page=133> | PDF133; footer132; ms66 | Three noun locations, completion and localization notation; Q1-01 |
| <https://grothendieck.umontpellier.fr/147.pdf#page=140> | PDF140,142; footers139,141; ms69–70 | Germ and canonical neighborhood arrows; Q1-03 |
| <https://grothendieck.umontpellier.fr/134-2.pdf#page=146> | PDF146,174,175; footers145,173,174; ms1,29,30 | Autograph date; sheaf-gluing functor; endpoint-one cone; Q1-02 |
| <https://grothendieck.umontpellier.fr/150.pdf#page=2> | PDF2; footer1 | Autograph folder date: December 1981–January 1982 |
| <https://grothendieck.umontpellier.fr/150.pdf#page=12> | PDF12–16,22–23; footers11–15,21–22; ms1–3,6 | Action/pushout; relative neighborhood; boundary and strictness; germ and reconstruction data; Q1-05 |
| <https://grothendieck.umontpellier.fr/151.pdf#page=27> | PDF27–29; footers26–28 | Provisional limit, punctured object and gluing span; Q1-04 |
| <https://grothendieck.umontpellier.fr/136.pdf#page=23> | PDF2,23–26; footers1,22–25 | Cover; $\omega_N$, recovery map, virtual-shadow terminology; Q1-06 |
| <https://grothendieck.umontpellier.fr/67.pdf#page=63> | PDF63–64; footers62–63; pencil65–66 | Tangent-disc map and its name; Q1-07 |

The 151 extract also contains PDF2 and41–44, supplied to the root researcher for Q2; those latter pages are not used as Q1 evidence. Cote150 PDF22–23 were also inspected; scan22 is used in Q1-05, while the equivalence claim on scan23 is retained only as a source locator, without a verdict on its proof.

### Discovery search and evidential limits

1. **Complete supplied context text search:** all seven files under `context/`, plus the frozen combined transcription; no supplied scan image used. `q1_context_search.json` records the first broad sweep and `q1_context_by_note.json` records every query, hit, exact file, line and scan available for each proposed note. Previous notes and registers remain leads or claims with their recorded statuses.
2. **Public machine index:** 636 available French transcript files from <https://github.com/Commutator-IO/grothendieck-project>, excluding cotes120 and152, plus two canonical Longue Marche transcript files from <https://github.com/ivan-gentile/la-longue-marche>. Exact noun searches and broader tubular/germ searches were used for discovery, not as an edition; `q1_index_manifest.json` records exact paths, URLs, hashes and comparison to the observed repository tree, with word hits in `q1_public_index_hits.json`.
3. **False-negative control:** the machine text for149 omitted the two checked *ombre* readings and misread the margin containing *tubulures*. A negative result in this index therefore proves only a failure to retrieve that spelling from that index.
4. **Unverified leads retained as leads:** the later156-4/156-6/156-7/156-8 shadow vocabulary; the longer conical-neighborhood material indexed under119; a Cox1978 tubular-neighborhood reference in Brown's bibliography preserved in134-2. No technical claim here relies on those passages without original verification.
5. **Web lookup:** exact-term searches for Grothendieck with *tubulure*, *tubulures étales*, *ombre(s)* and *localisé*; official Montpellier catalogue verification for dates and direct PDF paths; author-text check in the *Esquisse*, §5, printed pp32–33, as an additional locator only. The selected web refs, exact URLs and search terms are in `q1_web_ledger.json`; direct PDF opens through the web reader failed, so verified HTTP byte-range retrieval supplied the original pages for visual inspection.

### Register handling and outstanding question

No return claim was silently upgraded. In particular, EXIT_ONE_TYPE P1a1/P1b1/P1d1/P4e, LM6 F.43 and FLAGGED_149 ZD8 retain the status **“Proved (the return's claim)”** recorded in `RESULTS_STATE.md`; WG2 §1.8 #5 and §1.1 #6 retain **unchecked plan** status, and INTAKE 20261114 §13.2 remains an **intake reading, not a referee verdict**.

The remaining concrete research question is to locate the site or universal property intended by the two words on149/133, together with the morphism to the localization along $D_J$ and the induced punctured object. Confidence is high that this is the unresolved step in this bounded search, because the checked 149 passage names the objects without such a construction, while the sources above supply precise adjacent maps but no identified comparison to that $X_J$.

### Quote budget

Q1 uses only the three-word quotation “à titre provisoire” from151, leaving the root researcher's Q2 quotations within the combined source budget. External134-2,136,67 and150 quotations are likewise brief; the repeated headings above are locators and have not been used to reproduce substantial manuscript prose. Source-derived summaries of each external manuscript have been kept short, with the original mathematical maps preserved.
