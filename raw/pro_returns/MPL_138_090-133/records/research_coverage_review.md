# Research coverage review

Snapshot checked: **2026-11-17 23:27:15 UTC**. Reviewer: GPT-6 Astra Pro, `/root/mechanical_validator`.

## Scope and result

This is a mechanical and editorial coverage audit of `root_research.md`, `early_research.md`, `maps_moduli_research.md`, and `arithmetic_research.md`, compared with `research_flag_index.md` / `.json`, `research_leads.md`, and the frozen page TeX. No image or new context source was opened, no mathematical proof was reviewed, and no source or research note was changed. “Covered” below means that an item is explicitly discussed or has a stated scope limitation; it does not mean its mathematics has been verified.

The four reports contain **115 main research IDs**, with **no duplicate IDs, missing numbers within a series, or undefined local statement references**. All **six live literal question marks** have explicit discussion; the seventh question mark lies inside a cancelled block on scan 107 and has only partial discussion. All seven requested title/date/count sheets are covered by TA01–TA07 in `early_research.md`.

The main remaining coverage gaps are the mathematical annotations on scan 110, several definition/drafting transitions, and selected figure labels that are only covered by a general catalogue limitation. These can be closed with explicit dispositions; this audit does not recommend an unbounded new mathematical investigation or a claim to have checked the entire catalogue.

## 1. Concrete gaps and partial coverage

| ID | Frozen source locus | Existing nearby coverage | Exact coverage issue / safe assembly action |
|---|---|---|---|
| G01 | **110:53**, `\margin{$=6N$\\$2(\sum p+\sum q+\sum r)$}`; figures **110:37–41,61–90**, including the degree labels at line 75 | TA06 and BC07 cover the reused notice and its dates/counts. AR and MM provide other low-degree examples. | No item in the four reports addresses this mathematical margin or these particular labelled sketches. Add a short note recording them as an unpursued count/figure lead, with the meaning of N and the intended association left unresolved unless root has already established it. Do not treat the typed-notice audit as coverage of the mathematical over-writing. |
| G02 | **098:13–32**, especially the deleted divisibilities and inserted equalities at **24,26,28**, and the fibre-cardinality definition at **32** | MM01 discusses the object data, conservativity, and faithful pinning; its source ranges are 6–11 and 34–48. | The revised **morphism laws** identified in `research_leads.md` are outside MM01's cited ranges and are not discussed in its body. A short disposition should distinguish the cancelled divisibilities from the final fibre-cardinality formulas and note any unresolved functoriality issue without silently identifying the two stages. |
| G03 | **099:13**, `Définir ici` followed by the two C-sets, the γ-action, and the quotient arrow | BC01–BC04 and MM03/MM08/MM11 discuss the resulting dictionary and actions. | The bottom line is an author's **drafting instruction**, not a completed local definition. None of the four reports explicitly records that status. A sentence preserving this distinction would close the lead without repeating the later action arguments. |
| G04 | **094:30–39**, especially **32–33**, the forgetful/fibre-functor diagram and `E_i\longrightarrow E_i/I_i=\widetilde E_i` | ER09 and ER12–ER13 cover torsors, markings, and inertia; their cited source ranges stop before this diagram. | The specific quotient/forgetful diagram is not separately described or scoped as an unproved construction. Record it as a diagrammatic construction whose compatibility is unpursued, if no fuller treatment is intended. The reading-stage remark about a cropped formula remains image evidence outside this audit. |
| G05 | **114:46–49**, especially **48**, `n=\sum_s q_s=\sum_f p_f`; nearby enumeration sketches | MM14 explicitly notes the cancelled “rigide” block at 74–80; MM13 and the final MM scope statement disclaim a complete catalogue check. | The local degree-count relation is not individually addressed. A short pointer to the degree-count discussion, or an explicit “not checked” disposition, would cover this existing lead. The general disclaimer already prevents a false claim that every sketch has been verified. |
| G06 | **119:6**, the deleted `\mathbb Z_2` followed by `1`; **119:15**, `\mathbb Z_2.\mathfrak S_3` with cancelled `D_3\times\mathbb Z_2`; other circled `1` labels | MM13 discusses three diagnostic symmetry labels on scan 115 and expressly says it does not verify every group label on 114–120. | These **specific revised labels** have no individual note. They are already excluded from a blanket verification claim, so the remaining need is a precise unpursued-lead entry, not a forced identification of symmetry groups with monodromy or an interpretation of every cross/circle. |
| G07 | **107:3–10**, especially **5–6**, `\tau_{43}\text{ ou }\tau_{46}\ ?` and `\tau_{13}\text{ ou }\tau_{16}` | AR04 cites 107:5–9 and discusses the cancelled powers on line 9; AR05 concerns a different doubtful index on scan 106. | The literal question is **inside a deleted block**. The alternatives themselves are not discussed, so mark the search as a cancelled, unreconstructed trial rather than treating the question mark as a live unresolved theorem or claiming AR05 answers it. |
| G08 | **129:17**, `Par le th. de classification` | OP26–OP27 discuss the uniqueness reduction, and OP26 cites 16–29. | The reduction is covered, but the named classification input has no separate identification or background-status statement in these four reports. An assembly footnote can say that this invoked theorem is carried as a manuscript background input, unless the main proof file already supplies its exact formulation. This audit has not assessed that theorem. |

Two low-priority editorial matters should not be turned into new mathematical tasks:

- **100:18** is a cancelled, doubt-marked fragment containing “fibre par fibre” and “évidente.” MM05 discusses the related fibre/descent issue, but does not explicitly identify this cancelled fragment. A brief apparatus-status disposition is enough if every screening hit is to be enumerated.
- `research_leads.md` says scan 127 retains `1/(2−1/2)` literally. The frozen **127:77** actually has `\frac{1}{2-\tfrac1{\unsure{2|z}}}`. OP18 already says the later denominator uncertainty is not repaired; use that frozen alternative, and add line 77 to its locator if desired. The lead file is a reading-stage record, not a substitute for the frozen text.

## 2. Every literal question mark

| Scan / TeX line | Source status | Report coverage | Assessment |
|---|---|---|---|
| 090:44, first `?` | Live normality question | ER05 | Explicitly covered. |
| 090:44, second `?` | Live oriented normality question | ER06 | Explicitly covered separately. |
| 107:5 | Inside `\deleted{...}` spanning 3–10 | AR04; G07 above | Block cited, exact alternatives only partially discussed. |
| 112:5 | Live P-versus-δ question | AR09, with AR06–AR07 and AR10 | Explicitly covered. This audit does not recheck its answer. |
| 128:7 | Live exceptional-case question; the preceding `b)` alone is cancelled | OP15–OP16 | Explicitly covered. |
| 129:16 | Live uniqueness question | OP26–OP29 | Explicitly covered, including its immediate withdrawal/counterexample context. |
| 130:23 | Live tentative repair question | OP30–OP31; OP35–OP36 delimit later expectations | Explicitly covered. |

## 3. All 31 entries in the mechanical flag index

The index hashes match all **43 current frozen page fragments**, and every indexed exact line/range still matches the current source. Thus the screening comparison below is not based on a stale source index.

| Scan:line | Flag | Research ID(s) / disposition |
|---|---|---|
| 090:26 | “On sait” | ER03; ER07 distinguishes the later negative insertion. |
| 090:44 | Two questions | ER05–ER06. |
| 098:34 | “évident” functor | MM01 discusses the functor's conservativity; the omitted morphism-law detail is G02. |
| 099:3 | Rigidity / equivalent to a discrete category | MM02 and MM04. |
| 099:7 | Enumeration after valency condition | MM03 and BC01. |
| 100:18 | Cancelled “évidente” fragment | Partial: related MM05 discussion; cancelled status needs only an explicit disposition. |
| 100:20 | “On voit”; marginal “vérifier” | MM02. |
| 100:21 | Representability and arithmetic finiteness | MM05 and MM07, with explicit limits on all-base claims. |
| 101:8 | “évidente” action and stabilizer | MM06; MM08 for the following group-type distinction. |
| 103:6 | “On sait”; Galois dictionary and commuting action | MM11; BC02–BC04. |
| 103:8 | “on voit”; possible nontrivial conjugation | MM12; BC05 and BC13. |
| 107:5 | Cancelled permutation question | Partial: AR04; G07. |
| 107:28 | “Il faut” in elimination setup | AR06. |
| 112:3 | “on voit” exclusions | AR07. |
| 112:5 | δ question | AR09–AR10. |
| 121:3 | “axiomatique provisoire” | OP01; TA04. |
| 123:28 | “On prouve … aussitôt” | OP09; OP10–OP12 discuss adjacent cellularity criteria. |
| 126:3 | Theorem label | OP21–OP24 separate the reformulated hypotheses and claims. |
| 126:7 | “Conditions équivalentes” | OP21–OP24; the notes do not claim all equivalences checked. |
| 126:31 | “évident” implication chain | OP23. |
| 126:54 | “Il suffit” in disc reduction | OP22. |
| 126:56 | “on voit” in the same reduction | OP22. |
| 127:104 | Tentative nonramification requirement | OP19–OP20. |
| 128:7 | Exceptional case | OP15–OP16. |
| 129:16 | Uniqueness question | OP26. |
| 129:17 | Invoked classification theorem | Reduction discussed in OP26–OP27; separate background-input identification remains G08. |
| 129:24 | Restatement of uniqueness question | OP26–OP27. |
| 130:23 | “a-t-on gagné?” | OP30–OP31. |
| 130:24 | “l'impression” | OP30–OP31. |
| 131:9 | “il semble” exception list | OP35. |
| 131:13 | “Il faut … tirer au clair” | OP36. |

## 4. Reading-stage lead coverage by scan

The leads file contains one heading for each of the 43 supplied scans. The following table records coverage, not proof certification. Broad literature synthesis in BC notes does not by itself close a specific local figure or apparatus question.

| Scan | Notes / current disposition |
|---|---|
| 90 | ER01–ER07 address the sign, centre/range, discrete/profinite comparison, both normality questions, and the ν=2 negative insertion. |
| 91 | ER08 covers weighted/infinite parameters and the unspelled infinity convention. |
| 93 | ER09–ER10 and ER13–ER14 cover twisting, commutants, and the independence reading. |
| 94 | ER11–ER13 cover the arithmetic torsor, marking, and inertia; the bottom quotient diagram remains G04. |
| 95 | ER13, ER15–ER16 cover the common character, product relation, and symbol uncertainties. |
| 96 | ER17–ER20 cover the cancellation, independence scope, π/Γ drift, quotient/image issue, and primitive-root torsor. |
| 97 | TA01 covers the uncertain heading and absence of an explicit count. |
| 98 | TA02 and MM01 cover title, object definition, pinning, and conservativity; morphism revisions remain G02. |
| 99 | MM02–MM04 and BC01 cover rigidity and counts; drafting instruction remains G03. |
| 100 | MM02, MM05, MM07 cover the flagged moduli claims and their scope; the cancelled margin is a minor disposition item. |
| 101 | MM06–MM08 cover prime bounds, relabelling stabilizers, and group-type strata. |
| 102 | MM08–MM10 and BC08 cover the stratum, core-free criterion, and generator-marking warning. |
| 103 | MM11–MM12 and BC02–BC10 cover the Galois dictionary, actions, possibility of nontriviality, and announced programme. |
| 104 | AR01 and AR03 cover explicit small functions, fibres, and the cubic-star pinning action. |
| 105 | AR01–AR02 cover the dual cubic and barycentric equation. |
| 106 | TA05/BC07 cover the letter; AR04–AR05 and AR14 cover the tables, doubtful index, and two-drawing comparison. |
| 107 | AR06 and AR10–AR11 cover the analytic setup; AR04 partly covers the cancelled group trial, with G07 remaining. |
| 108 | AR06 and AR18 cover the elimination, leading term, and intermediate reading issues. |
| 109 | AR06–AR07 and AR11–AR13 cover the elimination conditions, residual factor, numerator sign, and arithmetic implications. |
| 110 | TA06/BC07 cover administrative material; mathematical margin and labelled drawings remain G01. |
| 111 | AR07–AR08 and AR15 cover endpoints, the printed quadratic roots, and the unfinished localized algebra. |
| 112 | AR09–AR10 and AR16–AR17 cover the explicit question, degeneration, logarithmic derivative, and isolated implication. |
| 113 | TA03 covers the title and count distinction. |
| 114 | MM14 explicitly records the deleted rigidity mark; the degree-count formula remains G05 and full enumeration is explicitly unclaimed. |
| 115 | MM13 checks diagnostic group-label meanings; the remaining catalogue is explicitly outside a full verification claim. |
| 116 | MM14 covers the singled-out degree-five passport and group label. |
| 117 | MM15 covers the repeated passport and states that identifying each particular drawing or explaining `!` is outside the check. |
| 118 | MM14 and MM16 cover the live rigidity and impossible annotations; crosses are not turned into unsupported mathematical negations. |
| 119 | General group-label scope is stated in MM13; the specific cancelled/revised labels remain G06. |
| 120 | MM16–MM17 cover the impossible case and inconsistent degree heading; other altered group labels fall under the unverified catalogue scope. |
| 121 | OP01 and TA04 preserve the provisional title. |
| 122 | OP02–OP04 and BC12 discuss quotient functoriality, automorphism notation, and equivariant extension. |
| 123 | OP05–OP09 discuss limit direction, subgroup qualifier, subsets, real compatibility, and the one-complex assertion. |
| 124 | OP13–OP14 and OP42–OP45 cover outer sphere covers, composition, and arithmetic limits. |
| 125 | OP10–OP12 and OP15–OP16 cover the revised cellularity claim, choices, and exceptional endpoint. |
| 126 | OP21–OP25 distinguish revised kernel condition, finite-order step, existence/equivalences, and contractibility. |
| 127 | OP18–OP20 cover the Möbius and folding formulas; the doubtful denominator is expressly left unrepaired, though line 77 is not in OP18's locator. Figurative doodles carry no additional proposition in the leads. |
| 128 | OP15–OP17 cover the explicit question, stronger condition, and local exception. |
| 129 | OP26–OP29 and OP34 cover uniqueness, its withdrawal, and the strict holomorphic definition; the classification input remains G08. |
| 130 | OP28–OP32 cover group labels, the tentative repair, and its stated scope. |
| 131 | OP25 and OP33–OP37 cover oranges, the tentative exception list, infinite-map reservation, and added markings. |
| 132 | OP38–OP43 distinguish the conditions and primed variants, special-map readings, local indices, and arithmetic hypotheses. |
| 133 | TA07/BC07 cover film title, dates, duration, routing number, and substrate limits. |

## 5. IDs and locator integrity

### IDs

| File | Main ID series | Count |
|---|---|---:|
| `root_research.md` | BC01–BC14; OP01–OP46 | 60 |
| `early_research.md` | ER01–ER20 | 20 |
| `maps_moduli_research.md` | MM01–MM17 | 17 |
| `arithmetic_research.md` | AR01–AR18 | 18 |
| **Total** | No repeated main ID | **115** |

The four inline refinements **MM02R, MM03R, MM05R, MM06R** are actually defined in their parent items; they are not missing standalone headings. **TA01–TA07** are table-row audit labels. Context keys C1–C12 and E1–E3 in the early report are local reference keys, not colliding research IDs. There are no undefined BC/OP/ER/MM/AR references in the four reports at this snapshot.

### Local source locations

The mechanical parser tested **123 unambiguous single-scan line lists** in Source/Place metadata against actual frozen file lengths. None points to a missing page file or an out-of-range line. Spot checks also confirmed the small-map formula lines, catalogue labels, the final scan-127 formulas, and the identified question-mark lines; these were textual locator checks, not figure validation.

Several root synthesis notes have **scan-only anchors**. This is natural for a corpus-wide absence claim such as BC11, but pinpoint anchors would improve the other notes during assembly:

| Note(s) | Suggested exact anchors to add, without changing the note's argument |
|---|---|
| BC07 | 106:3–8; 110:13,21,28; 133:14–25; or cross-reference TA05–TA07. |
| BC09 | 099:3,7; 103:6–8. |
| BC12 | 122:29–40; 123:3–14; 124:25–29. |
| BC14 | 109:22–26; 112:3–5; or AR13's source metadata. |
| OP12 | 123:28–33; 125:5–26. |
| OP16 | 125:33–35; 128:3–7. |
| OP25 | 126:13–15; 131:3–8. |
| OP34 | 129:3–14; 131:3–8. |
| OP42 | 124:25–29; 128:3–7. |
| OP43 | 124:25–29; 132:31–40. |
| OP44 | 109:22–26; 112:3–5; 124:25–29. |
| OP45 | 103:10; 124:25–29. |
| OP46 | 103:8; 121:3 for the two short quotations; retain the wider operation scope as a second locator. |
| OP18 | Add 127:77 for the denominator uncertainty already mentioned in its body. |

The introductory wording “PDF scan numbers” in `root_research.md` should be read consistently as the **original source scan identifiers**, not ordinal page numbers of a 43-page assembled deliverable. The other reports already make the local-TeX-line convention explicit. No external-context locator was reverified in this coverage-only task.

## 6. Snapshot fingerprints and limits

| Audited report | SHA-256 at the snapshot |
|---|---|
| `root_research.md` | `238baa5ed4c9a95df094856afa31a15034bc75a61032956e8e02cedbb0af9261` |
| `early_research.md` | `e0854db131da81065c30983b3c343a8a18e1ff82d5f9112937dd80a049067883` |
| `maps_moduli_research.md` | `68a81afa64d06146b75460b3900e59db22e1dd423b83a2eb2fb14ea08949df1c` |
| `arithmetic_research.md` | `6b501fcc9bf632f9b68fb05afdeb51df9148c8e1d228645f87c1f27c527f7619` |

This review is an assembly aid, not the final package validator or the requested end-of-run unchanged-hashes confirmation. Any subsequently added notes can close the listed gaps while leaving this timestamped review as an honest record of the snapshot examined.

## 7. Closure addendum — assembled notes and check-event ledger

**Reviewed 2026-11-17 23:42 UTC.** The assembled `MPL_138_090-133_notes.md` contains **127 main note IDs** and **18,281 words** at this review; `CHECK_EVENTS.tsv` contains **191 event rows**. This addendum supersedes the earlier snapshot's open coverage findings. It does not replace the root's actual final hash confirmation or final validator run.

### Closure of the eight coverage findings

| Earlier finding | Assembled note(s) | Closure |
|---|---|---|
| G01 — scan 110 mathematical margin and drawings | **SR05** | Explicitly distinguishes the isolated degree/group-order readings and leaves the labelled sketches outside a claimed checked construction. |
| G02 — scan 98 morphism-law revision | **SR01–SR02**, with inline **SR01R–SR02R** | Explicitly addresses both the asserted cartographic functor and composition of the literal morphism laws. |
| G03 — scan 99 drafting instruction | **SR03** | Identifies the marginal line as an instruction, rather than a finished definition. |
| G04 — scan 94 quotient/forgetful diagram | **SR06** | Addresses the quotient and the multiplicity information it forgets. |
| G05 — scan 114 degree-count relation | **SR07**, with **SR10** for the adjacent doubtful φ-expression | Provides an explicit disposition of the degree sum and keeps the nearby undefined symbol separate. |
| G06 — scan 119 revised group labels | **SR08–SR09** | Separately records the withdrawn involution label and the dotted-extension notation, without claiming every drawing identified. |
| G07 — cancelled question at scan 107 | **SR04** | Marks both alternatives as an abandoned trial and does not promote them to a live conjecture. |
| G08 — invoked classification theorem | **SR12** | Identifies the finite-case background input and explicitly excludes a new general or infinite-cover proof. |

**SR11** additionally makes the remaining full-catalogue comparison an explicit separate project. Thus every live literal question and the cancelled question now has a clear item-level disposition, and the selected nontrivial figure/count leads from the earlier review are explicitly addressed or scoped as unverified. The title/count audit TA01–TA07 is present in the assembled notes.

### Identifier and event consistency

- The main series are **ER01–20, MM01–17, BC01–14, AR01–18, OP01–46, SR01–12**: no repeated IDs and no missing numbers within a series.
- The six inline refinements **MM02R, MM03R, MM05R, MM06R, SR01R, SR02R** are defined. No local BC/OP/ER/MM/AR/SR reference points to an undefined item.
- Every one of the 127 main IDs has at least one ledger event. Multiple events for one ID have different actors, purposes, or scopes; there are **no duplicate complete event rows**.
- Every ledger ID having the exact form of a main note or refinement resolves to one. Every refinement named by a `refuted, with refined statement ...` event is defined.
- The five-column header is correct. The package validator accepts all 191 rows, date forms, nonempty fields, and event types.
- Source/context comparisons recorded as “used and rechecked in this run” explicitly say they are not mathematical proofs of the source claims. Background-use events likewise disclaim an additional re-proof. Integrity checks, draft computation failures and peer-review events retain their stated, limited outcomes.
- The BAP06 peer-review qualification about “only G_K” is reflected in the assembled **OP43**, which now says definition over K guarantees G_K-equivariance without excluding extra equivariance. This was a text/ledger consistency check, not a fresh mathematical review.

### Structural checks and two formatting actions for root

The assembled notes have no unmatched `\(...\)` or `\[...\]` delimiters, no missing cited `records/` paths, no internal TODO/TBD placeholders, and no out-of-range locations among **134 mechanically parsed source-locator lists**. The exact early-page source quotations still match their frozen TeX. The single shell example has a matched pair of tilde fences.

Two Markdown findings were sent to root for application in the assembler/source report:

1. **TA01 and TA05** contain an uncertainty-alternative pipe inside an inline-code cell. In the reviewed assembly these occur at lines **134** and **138**, and create an extra table column under GFM. Root will escape those two pipes as `\|` in `records/early_research.md` and reassemble; this is Markdown escaping only and changes no frozen uncertainty macro.
2. Several imported note headings are immediately followed by metadata without a blank line. Root will insert a blank line after note headings during assembly for consistent Markdown rendering.

These actions were **root-to-apply at this addendum**, not claimed as completed by the support agent. No research coverage, ID, ledger-reference, or numerical source-locator issue remains from this review.

### Validator state and finalization boundary

The validator was run in **final mode** after the assembled notes and ledger existed. Its saved result is `records/mechanical_validation_final_notes.json`: **0 errors, 1 warning, 0 informational items**. The sole warning is the still-pending explicit final unchanged-hashes confirmation in `progress.log`; all **44 recognized frozen hashes match**, with 43 page fragments, 992 inventory rows, 43 completion entries, 43 audit entries, and 335 uncertainty occurrences present.

Root has stated that the finalization script will apply the Markdown assembly changes, append the actual all-44-hashes confirmation, and run the final zero-warning validator. No repeated support-agent validation after those changes is claimed or required by this addendum. No frozen page, combined transcription, doubts file, inventory, assembled notes, or main ledger was modified by this support-agent review.

Reviewed assembled-file fingerprints, before root's planned formatting reassembly:

- Notes: `193c644ddd065d3859a68294beec859600f35bf94f5151d4a9c5ff7540378e18`.
- CHECK_EVENTS: `ef3be0aba67b5a5f71ca14fe7f4bc99288abe55ac2d2b1e932547da5a9dd2295`.
