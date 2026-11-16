# Standing registers: author flags, withdrawals, titles, and sheet counts

## Reading convention and supplied-context keys

These registers cover all **46 frozen pages**, cote **43**, scans **94–142 excluding 99, 111, 127**. `43:98:L12` denotes line 12 of `pages/MPL_43_094-142_43_scan098.tex`, with its scan macro at line 1. **SF01–SF41** correspond to F01–F41 in the fuller working record; SF19/SF22/SF27/SF28/SF30 and the inner arrow of SF34 explicitly retain possible readings. All other `\unsure` wrappers concern editorial reading confidence unless separately identified by an author word or mark. A cancelled block retains its cancelled state without an inferred reason.

Context filenames are abbreviated **CT** = `context/MPL_16+47+54+44_transcription.tex`; **CN** = `context/MPL_16+47+54+44_notes.md`; **RS** = `context/notes/RESULTS_STATE.md`; **Oda** = `context/Oda_1969_first_de_Rham_cohomology_Dieudonne_modules.pdf`. `Pnnn` and `Rnn` identify actual searches in `records/research_flags_titles_searches.jsonl`. A no-match is limited to the recorded literal/regex in the supplied text and PDF extraction; it establishes no mathematical absence. The earlier CT/CN witnesses retain the README's first-pass/lead qualification. A dash in the RS column means no result ID is assigned by this register.

| Key | Exact supplied-context match and limit |
|---|---|
| **CTX1** | **CT 16:30**, lines 1221–1233: multiplicative-group cohomology complex, labelled acyclic; **16:37/39**, lines 1451–1461/1528–1540: injective hulls and stalk construction; **16:41**, lines 1589–1611: internal Ext and derived Hom. **Oda PDF p.57**, lines 3–14: Leray hypercohomology. Exact Greenberg/Néron-Weil/relative-acyclicity phrases have no match in P094–P098/R01/R06. |
| **CTX2** | **Oda PDF p.19**, printed p.80, §3: perfect field, Witt schemes and operators; **PDF p.3**, lines 25–43: finite-group/Dieudonné setup. These are concrete Witt-object matches; the local quotient questioned at 43:102 is not located by P102/R07. |
| **CTX3** | **CT 47:3–4**, lines 2087–2215: Fourier kernel and convolution comparison; **47:6**, lines 2300–2324: shifted direct image/determinant line; **47:11**, lines 2550–2557: duality formula. **CN F6–F7/F20** remain prior leads, including unfinished compatibility and an unresolved checked-input convention. No map identifying these with the cote-43 comparisons is proved here. |
| **CTX4** | **CT 54:3/5/7**, lines 2611–2652/2694–2701/2716–2730: tangent/Hodge extensions, Cartier duality, Frobenius–Verschiebung, final reconstruction question. **Oda Theorem 1.1, Corollary 1.3, Theorem 3.19** are located comparison results (R07); **CN D01–D05** retain first-pass status. |
| **CTX5** | **CT 44:2/4/8**: “Programme de travail”, Néron margin, and cycle-Jacobian conjectures; **16:21**, line 886: Néron–Severi. **RS WG2 §2.3 #12** remains an unchecked question/plan; **WG H9** remains an unchecked hunch. These name/object matches do not settle the local-functor checks. |
| **CTX6** | **CT 54:4/6**, lines 2658–2677/2707–2710: revised flatness/generic-freeness drafts; **44:3**, lines 2809–2840: cancelled graded-completion argument; **16:56**, lines 2032–2040: flat descent/completion. **CN D06–D07** remain leads. No exact equidimensionality, Cohen, associated-prime, or semicontinuity match in R03. |
| **CTX7** | **CT 16:52**, lines 1912/1920–1922: different/trace and Kummer ramification plan; **16:28** and **Oda PDF p.74**: class-field bibliography. **RS CYCLOTOMIC_KERNEL C1, LM6 B.22, LM6 F.43** retain “Proved (the return's claim)”; **FLAGGED_149 B9, LM6 B.27** retain “Open (the return's claim)”. Their underlying packages were not supplied. |
| **CTX8** | **CT 44:3** supplies graded completion; **Oda PDF p.44**, lines 37–45, supplies Picard formal completions. The only `local cohomology` match is **Oda PDF p.73**, lines 43–44, a bibliography entry. Exact `i_!`, `j_!`, `H_U`, `H_Y`, `H_x`, `triangle exact`, `hensel`/`hensél` have no match (R04/R06); no particular support-arrow comparison is supplied by these searches. |
| **CTX9** | **CT 47:2**, Fourier/convolution title; **54:2**, uncertain “Dualité en Cohomologie des V. A.”; **44:2**, “Programme de travail”. **RS WG2 §1.1 #3** remains an unchecked folder plan. P101/P103/R02/R08 find no exact S-homotopy/intrinsic-join/Stiefel, Hilbert-cover, fine/soft-sheaf, III-42/III-49, Cassels, or `n°239` witness; references alone supply no sheet date. |

**External provenance update supplied by the main researcher:** R03 identifies the reused typed witness on scans 103/101/105 with M. F. Atiyah, *Thom Complexes*, published pp.308–310; the author is not named on these faces. The primary-source comparison and publication variants are documented in R03. This does not alter the limited supplied-context search results below.

## Self-flagged, deferred, and expressly limited items

The 30 literal question-mark characters comprise **28 outside `\unsure`, at 21 scan/line loci**, plus two possible readings: 118:L7 and 136:L31. The table also records explicit admissions/deferred proofs without a question mark. SF19/SF20 concern outline/administrative matters, SF39 is an express typed-source scope limit, and SF40 is bibliographical; their documentary scope is stated rather than converted into a mathematical conjecture.

| ID | Source locus and short quote | Scope | Context match / limited no-match | RS pointer and retained status |
|---|---|---|---|---|
| **SF01** | **43:94:L32–42**, “Il faudrait prouver alors que” | Deferred comparison of H and Ext in the perfect-field quasi setting. | CTX1; no exact quasi-group/calculation phrase (P094). | — |
| **SF02** | **43:95:L2–4**, “Il faudrait aussi … étudier”; “cohomologie galoisienne” | Deferred Galois-cohomology calculation in the quasi setting. | No French/English Galois-cohomology phrase (P095); CTX1. | — |
| **SF03** | **43:96:L21–24**, “application continue”; “formelles … ! ? !” | Questioned continuous-map/direct-image explanation of the Néron functor. | No exact continuous-map/Greenberg phrase (P096,R01); CTX1–2. | — |
| **SF04** | **43:97:L19–27**, “transforme injectifs en injectifs”; “à vérifier” | Injective preservation is explicitly pending; the adjoint proof attempt is cancelled. | CTX1 has stalk/injective-hull constructions; no identified Néron comparison (P097). | — |
| **SF05** | **43:98:L12–19**, “si on admet”; “vérifier” | First gate: acyclicity of internal Hom for relative H0; the extra H0_S clause is cancelled. | CTX1; no exact acyclicity clause (P098). | — |
| **SF06** | **43:98:L26–32**, “et admettant”; “vérifier” | Second gate: relative Hom is assumed acyclic for H0(k,-), for the next spectral sequence. | CTX1; no exact Hom_{S/k} clause (P098). | — |
| **SF07** | **43:102:L9–12**, marginal `?`; “10) Application 2” | Question beside the proposed Witt-quotient autoduality application; attachment is by position. | CTX2 supplies Witt objects; no located W_n(K)/F^mW_n(K) statement (P102). | — |
| **SF08** | **43:102:L24–28**, marginal `?` at L26 | Question beside the positive-degree comparison involving the written J(K)/J(V) expression. | CTX5/7 supplies Jacobian/class-field wording, without a proof of this comparison (P102). | WG2 §2.3 #12: unchecked plan only. |
| **SF09** | **43:104:L2–3**, circled “parfait ?” | Perfectness is questioned beside k←V→K. | CTX2 explicitly uses a perfect base field; no comparison settles this margin (P104). | — |
| **SF10** | **43:104:L20–29**, “`T^0` transforme injectifs en `\Gamma^0_k`-acycliques ??” | Property (i) has the double question mark; adjacent dimension/base-change properties (ii)/(iii) have none separately. | CTX1–2; no exact acyclicity property (P104). | — |
| **SF11** | **43:106:L29**, “Comment obtient on le carré du bas ?” | Construction of the lower Cartier/Serre/Pontryagin square is asked for. | CTX3–4 contains specified duality diagrams; no identified morphism comparison (P106). | — |
| **SF12** | **43:110:L4–16**, marginal `?` at L16 | Question attached to Proposition 6.7 and its fibre-length semicontinuity claim. | CTX6 supplies flatness drafts; no exact semicontinuity/length statement (P110,R03). | — |
| **SF13** | **43:110:L19–23**, “(réf)” twice; “il reste … à prouver” | Constructibility and DVR reduction have reference placeholders; the proof then starts. | CTX6; exact longueur/semicontinuity queries have no match (P110). | — |
| **SF14** | **43:110:L60–62**, “J'ignore si les assertions sont vraies” | Explicit uncertainty about omitting prior flatness at maximal fibre points. | CTX6; main mathematical notes examine the surviving flatness sentence separately (P110). | — |
| **SF15** | **43:110:L62–65**, “Question liée”; “prouver `\mathfrak m\in\operatorname{Ass}M/tM` !” | Linked associated-prime problem, with some hypotheses/glyphs uncertain. | No associated-prime/Ass operator match (P110,R03); CTX6. | — |
| **SF16** | **43:112:L39–42**, `??` in the `G_m` row | Questioned G_m row, beside K* and 0. | CTX2/4 supplies Witt/finite-group objects; no located table-cell answer (P112). | — |
| **SF17** | **43:112:L44–47**, `\mathbb Z\qquad??` | Questioned Z row, with H1(K,Q/Z) nearby. | CTX1–2; no exact local-field cohomology formula (P112,R06). | — |
| **SF18** | **43:116:L40–44**, cancelled “J'ignore”; “équidimensionnalité” | Cancelled question about essential equidimensionality hypotheses and equality in 2.6. | No equidimensionality/Cohen literal (P116,R03); CTX6. | — |
| **SF19** | **43:118:L7–9**, `\unsure{(?)}`; “Pourrait passer au Chap 0 ?” | Possible (?) reading beside regular morphisms; clear chapter-0 placement question in cancelled outline. | No matching chapter-placement note (P118,R08); CTX9. | — |
| **SF20** | **43:118:L48–59**, “Bott September 1963 ?” | Cancelled administrative/date question; no mathematical theorem is at issue. | No matching September-1963 list (P118,R08); CTX9. | — |
| **SF21** | **43:120:L44–49**, marginal `?` after (ii) | Question follows the H1(K,{}_nB)/Ext1 comparison; adjacent divisibility statement is separately written. | CTX4; no exact local-field formula (P120,R06). | — |
| **SF22** | **43:121:L36**, `\unsure{Joube\|doute}` | Possible author “doute”; frozen alternatives do not establish that reading. | No Euler-Poincaré/III-42 phrase (P121,R08); CTX6/9. | — |
| **SF23** | **43:123:L7–9**, `\operatorname{Ext}_{\unsure{m}}(M,A)\overset{?}{=}D(M)` | Questioned Ext-to-dual equality; the Ext subscript itself is editorially uncertain. | CTX8; no located answer for this equality (P123). | — |
| **SF24** | **43:123:L24–32**, two arrows labelled `?`, then `\unsure{U}\ ?` | Two questioned arrows in a formal/support Ext diagram, plus the underwritten U? location. | CTX8 has completion material; no matching arrows (P123). | — |
| **SF25** | **43:125:L24–31**, the final arrow `\overset{?}{\mathrel{-}}` | Questioned final comparison from support cohomology on a formal completion; target unfinished. | CTX8; no matching comparison (P125). | — |
| **SF26** | **43:128:L8**, “définis comme les `C`-groupes ?”; “Cela est-il équivalent … ?” | Two questions about k-group definitions and equivalence with Weil functors/schemes. | CTX3 has a Weil kernel at 47:3/6; no established equivalence of definitions (P128,R05). | — |
| **SF27** | **43:128:L18**, `\unsure{nous admettrons}`; finite `dim \unsure{ch.}` | Possible “nous admettrons” reading, admitting finite cohomological dimension of f_*. | No exact cohomological-dimension phrase (P128,R05); CTX1/3. | — |
| **SF28** | **43:129:L42–43**, `\unsure{(Montrer} … propriétés)` | Possible instruction to prove transfer for unspecified properties, inside a wholly cancelled draft. | CTX6 has regularity/local-algebra material; no missing property list supplied (P129). | — |
| **SF29** | **43:130:L3–12, L19–29**, “il reste à définir”; “si nous définissons un élément” | Trace-like map Rf_*Sσ→σ remains to be defined before the comparison by composition. | CTX3–4 supplies neighboring duality constructions; no identified map (P130). | — |
| **SF30** | **43:130:L31–39**, marginal `\unsure{préciser}` | Possible “préciser” reading next to changing finite/affine/no-abelian-component restrictions. | CTX3–4; no exact component restriction in context (P130). | — |
| **SF31** | **43:135:L4–12**, “On doit prouver” | Point-supported Ext comparison with degree shift is a stated proof obligation. | CTX4/8; no matching local-support proof located (P135). | — |
| **SF32** | **43:135:L13–15**, “Il est sans doute vrai” | Tentative Ext comparison over a henselization; local wording and support hypothesis are revised. | No hensel/hensél literal (P135,R04); CTX8. | — |
| **SF33** | **43:135:L18–38, L45–53**, “i.e. : vérifions”; “On est ramené à prouver” | Extension-by-zero comparison is to be verified; the announced μ_n calculation narrows n to prime-to-p. | CTX8; no i_!/j_! literal (P135,R06). | — |
| **SF34** | **43:136:L31, L34–44**, `\unsure{2\|?}` on an arrow; clear marginal `?` | Clear question on shifted triangle comparison; arrow 2/? remains only a possible reading. Box at L61 has m+1. | CTX3/8; no triangle/support formula located (P136,R06). | — |
| **SF35** | **43:138:L14–18**, vertical `\simeq ?` | Question after a cancelled lower isomorphism attempt in the dual localization diagram. | CTX8; no matching support formula (P138). | — |
| **SF36** | **43:140:L35–39**, boxed `\overset{?}{\simeq}` followed by `???` | Unshifted boxed support comparison is explicitly questioned; compare 136:L61. | CTX8; sole “local cohomology” hit is bibliography. Main notes give the separate degree test (P140). | — |
| **SF37** | **43:101:L6–9**, “will be given in a future publication” | Typed source defers determination of q_k through J(X) to a future publication; author not named on the face, external identification in R03. | No such witness in supplied context (P101,R02); CTX9. External identification: R03. | — |
| **SF38** | **43:101:L52–53**, “It would seem reasonable to suppose” | Typed source tentatively compares Df and Δ in S-homotopy type. | No exact homotopy terms in supplied context (P101,R02); CTX9. External identification: R03. | — |
| **SF39** | **43:103:L50–52**, “we make no assertion for the case `n<2k`” | Explicit scope restriction in typed Theorem (6.5), continued at 101:L4. | No Stiefel witness in supplied context (P103,R02); CTX9. External identification: R03. | — |
| **SF40** | **43:105:L36**, “(to appear)” | Bibliographical publication-status reservation; retained as documentary evidence only. | No Milnor/Spanier/James match in supplied context (P105,R02); CTX9. External identification: R03. | — |
| **SF41** | **43:132:L23–38**, “On va définir”; “associé à un hom” | Pairing and auxiliary comparison hom are announced, ending with an unfinished c). | CTX3–4; trace construction is also deferred at 130:L19–29 (P132). | — |

## Explicit withdrawal

| ID | Source locus and short quote | Scope and context |
|---|---|---|
| **WD01** | **43:96:L35–38; 43:97:L2–3**, “Non, car le foncteur … ne commute pas aux limites inductives” | The author expressly withdraws the inductive-limit compatibility note and gives noncommutation of `\mathbb V:k-alg→V-alg.` as the reason. **CTX1–2; P096–P097**: no exact matching context statement; no RS status change. |

The full working record, `records/research_flags_titles.md`, retains **34 material-revision entries and all 241 encoded deletion/insertion markers**, including the cancelled drafts, changed hypotheses, coefficient/degree changes, and cancelled cover titles. This standing section does not duplicate their mathematical analysis.

## Title, cover, reused-sheet, and count register

The inclusive scan range has 49 numbers; removal of 99, 111, 127 leaves **46 supplied faces: 27 text, 11 reused_typed, 4 cancelled_draft, 4 cover**. The 46 regular transcribed number marks are `scan−1`, giving 93–141 with gaps 98, 110, 126; additional number marks are included exactly below. **No explicit total extent (“N pages”/“N feuilles”) was located**: list/theorem/reference numbers and Roman labels remain their written marks.

The archive title in `context/README.md`, line 9, is “Dualité des groupes. Jacobiennes généralisées etc : notes et copies de notes manuscrites (s.d.).” Its approximate dates are metadata. The cancelled September-1963 list at 118:L49/51 and the reference dates at 105 do not date the surrounding mathematical sheets. RS reused-sheet observations **MPL_136_095-141 1.5, MPL_136_189-234 R008, MPL_136_235-281 N16** retain first-pass-lead status and establish no provenance for these particular faces.

| Scan | Sheet kind | Exact number marks with fragment lines | Title/headings, local numbers, and extent evidence | Context search / RS |
|---|---|---|---|---|
| **94** | text | `\mspage{93}` @ L43 | No separate title; opening description of the T-category; “règles de calcul” at L32–37. | CTX1; P094; RS — |
| **95** | text | `\mspage{94}` @ L11 | No separate title; continuation “Il faudrait aussi” at L2; cancelled N.B. at L9–10. | CTX1; P095; RS — |
| **96** | text | `\mspage{95}` @ L39 | “foncteur fondamental … dit de Néron” at L2; no extent statement. | CTX1–2; P096; RS — |
| **97** | text | `\mspage{96}` @ L32 | No separate title; previous cancelled note continues at L2–3; Néron derived functors. | CTX1; P097; RS — |
| **98** | text | `\mspage{97}` @ L42 | No separate title; relative Hom/Ext and two spectral-sequence gates. | CTX1; P098; RS — |
| **100** | text | `\mspage{99}` @ L63 | Outline items **1–8** at L25–62; “Dualité de Cartier”, “Dualité de Serre-Pontrjagin”, “Le th. de dualité”. These are item numbers. | CTX3–4; P100; RS — |
| **101** | reused_typed | `\mspage{100}` @ L2; `\mspage{22.}` @ L3 | Typed continuation of (6.5); “Pembroke College, Cambridge.” at L60–61; author not named on the face; external identification in R03. | CTX9; P101; RS — |
| **102** | text | `\mspage{101}` @ L43 | Outline items **9–14** at L2–22, continuing scan 100; Lang/Serre/Tate comparison table L36–41. | CTX2/5/7; P102; WG2 §2.3 #12 (unchecked plan) |
| **103** | reused_typed | `\mspage{102}` @ L2; `\mspage{21.}` @ L3 | Typed “Remark” L4, LEMMA (6.3) L24, LEMMA (6.4) L37, THEOREM (6.5) L45. Typed page 21 continues on typed page 22 at scan 101. | CTX9; P103; RS — |
| **104** | text | `\mspage{103}` @ L42 | No separate title; category/functor diagram and proposed properties (i)–(iii). | CTX1–2; P104; RS — |
| **105** | reused_typed | `\mspage{104}` @ L2 | “REFERENCES” L3; entries **1–16**. Their numbering and publication page ranges count references/cited pages. | CTX9; P105; RS — |
| **106** | text | `\mspage{105}` @ L56 | No separate title; Cartier/Serre/Pontryagin square; “Comment obtient on le carré du bas ?” L29. | CTX3–4; P106; RS — |
| **107** | text | `\mspage{106}` @ L43 | No separate title; pairing and Ext scratch calculations. | CTX4; P107; RS — |
| **108** | cancelled_draft | `\mspage{107}` @ L2 | Cancelled “Corollaire” with uncertain number 4/2.9.10 at L3; cancelled homology diagram L56–62. | CTX6; P108; RS — |
| **109** | text | `\mspage{108}` @ L62 | Case headings “2°) G=mu_p” L2, “3°) G=alpha_p” L22, repeated “3°) G=G_m” L26. The repeated item number is preserved. | CTX4; P109; RS — |
| **110** | reused_typed | `\mspage{109}` @ L66 | “IV 7 Oubli au n° 7.6.” L2; Proposition 6.7 L4; Lemme 6.8 L25. These are internal labels, with no extent count. | CTX6; P110; RS — |
| **112** | text | `\mspage{111}` @ L55 | No separate title; finite-group/Greenberg table. | CTX2/4; P112; RS — |
| **113** | cancelled_draft | `\mspage{112}` @ L41 | No separate title; whole local-reciprocity/Galois draft cancelled. | CTX7; P113; CYCLOTOMIC_KERNEL C1 / LM6 B.22 (return claims) |
| **114** | text | `\mspage{113}` @ L59 | No separate title; boxed Ext/cohomological pairings and unfinished displays. | CTX3; P114; RS — |
| **115** | reused_typed | `\mspage{114}` @ L2; `\mspage{III-49}` @ L3 | Typed page III-49, starts mid-word L4 and ends mid-Corollaire 1 L34–35. | CTX1/6; P115; RS — |
| **116** | text | `\mspage{115}` @ L45 | No separate title; spectral diagram, then cancelled “Remarque 2.7” and “Prop. 2.8. Continuité des Cohen-Macaulay” L40–44. | CTX6; P116; RS — |
| **117** | text | `\mspage{116}` @ L43 | Cancelled marginal “Vue d’ensemble” L19; displayed items (3), (2), (1) L7–16. | CTX4; P117; RS — |
| **118** | cancelled_draft | `\mspage{117}` @ L66 | Cancelled mathematical outline numbered **1–15** L3–33; cancelled administrative list L48–60, with September 1963 strings. | CTX9; P118; RS — |
| **119** | text | `\mspage{118}` @ L45 | No separate title; torsion-cohomology diagrams and Q,N scratch definitions. | CTX4; P119; RS — |
| **120** | text | `\mspage{119}` @ L50 | No separate title; 1°/2° and (i)/(ii)/(iii) L38–49, with (iii) unfinished. | CTX4; P120; RS — |
| **121** | reused_typed | `\mspage{III-42}` @ L2; `\mspage{120}` @ L38 | Typed page III-42; Proposition 13 L12, equations (15)/(16), Théorème 2 L25. | CTX6/9; P121; RS — |
| **122** | cover | `\mspage{121}` @ L7 | **Cover:** “Corps de classes / et dualité / des Courbes Algébriques” L3–5; last line underlined. | CTX5/9; P122; WG2 §1.1 #3 (unchecked plan) |
| **123** | text | `\mspage{122}` @ L48 | No separate title; support/Ext diagrams and a questioned duality expression. | CTX8; P123; RS — |
| **124** | reused_typed | `\mspage{84}` @ L2; `\mspage{123}` @ L9 | Typed “THEOREME 3” L4, partition of unity; marginal “n° 239” L3. | CTX9; P124; RS — |
| **125** | text | `\mspage{124}` @ L33 | No separate title; formal-scheme/completion diagram, “complété formel le long de Z” L28. | CTX8; P125; RS — |
| **126** | reused_typed | `\mspage{78}` @ L2; `\mspage{125}` @ L17 | Typed section **“3. Faisceaux mous”** L4; “DEFINITION 1” L12; marginal “n° 239” L3. | CTX9; P126; RS — |
| **128** | text | `\mspage{127}` @ L32 | Cancelled uncertain “Schémas” L2; C-group setup starts L4. | CTX1/3; P128; RS — |
| **129** | cancelled_draft | `\mspage{128}` @ L46 | Cancelled “Proposition” L3 and “passer au N° précédent” margin L4; Cor/Dem labels within wholly cancelled draft. | CTX6; P129; RS — |
| **130** | text | `\mspage{129}` @ L40 | “Th.” (i) L33 and (ii) L39; trace/comparison construction precedes it. | CTX3–4; P130; RS — |
| **131** | cover | `\mspage{130}` @ L10 | **Cover:** active over/underlined **V**, cancelled uncertain **IV/VI** L2; cancelled “Schémas de Hilbert, de Picard” L4; cancelled parenthetical “sans théorie des relations … avec les groupes fondamentaux” L6–8. | CTX5/9; P131; WG2 §1.1 #3 (unchecked plan) |
| **132** | text | `\mspage{131}` @ L39 | No separate title; labels a), b), circled star, final c) at L25/30/38. | CTX4; P132; RS — |
| **133** | text | `\mspage{132}` @ L49 | No separate title; cohomological table, marginal “autodualité de la Jacobienne” L43. | CTX4–5; P133; WG2 §2.3 #12 (unchecked plan) |
| **134** | cover | `\mspage{133}` @ L6 | **Cover:** cancelled over/underlined **V** L2; cancelled “Fidèle platitude / Descente fid. plate / Applications” L3–5. | CTX6/9; P134; RS — |
| **135** | text | `\mspage{134}` @ L54 | No separate title; point-support and extension-by-zero argument; uncertain omega)/a) marker L35. | CTX8; P135; RS — |
| **136** | text | `\mspage{135}` @ L74 | No separate title; “triangle exact de complexes de k-groupes” L27, support/duality diagrams. | CTX3/8; P136; RS — |
| **137** | reused_typed | `\mspage{136}` @ L23; centered `- 37 -` @ L2 | Typed page “- 37 -” L2, marginal “n°338” L3; PROPOSITION 9 begins at L22. | CTX6; P137; RS — |
| **138** | text | `\mspage{137}` @ L21 | No separate title; revised dual localization diagram. | CTX8; P138; RS — |
| **139** | reused_typed | `\mspage{138}` @ L11; centered `- 88 -` @ L2 | Typed page “- 88 -” L2, marginal “n° 239” L3; PROPOSITION 8 L6 and “Exercices. 1)” L10. | CTX9; P139; RS — |
| **140** | text | `\mspage{139}` @ L41 | No separate title; functor/support diagrams and boxed comparison question. | CTX8; P140; RS — |
| **141** | reused_typed | `\mspage{140}` @ L13; centered `- 87 -` @ L2 | Typed page “- 87 -” L2, marginal “n° 239” L3; PROPOSITION 8 L6, LEMME 2 L10. Its lemma continues at scan 139. | CTX9; P141; RS — |
| **142** | cover | `\mspage{141}` @ L6 | **Cover:** “Dualité de Tate- / Cassels” L3–4; line-break hyphen retained. | CTX9; P142; RS — |

Typed **21→22** corresponds to scans **103→101**; typed **87→88** corresponds to **141→139**. Both latter faces print “PROPOSITION 8”, retained without renumbering. III-42/III-49 and 78/84 are sparse witnesses; the selection does not supply their intervening pages. Cover V/IV/VI marks and “IV 7” remain marks, without a chronological assignment.
