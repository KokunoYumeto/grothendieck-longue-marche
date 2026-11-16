# Supplied-context coverage ledger for MPL_131

## Scope, status, and access limits

This ledger covers **48 primary entries**, the four run-summary entries, and the secondary identifiers actually visible in the two supplied context files: `MPL_131_context/README.md` and `MPL_131_context/notes/RESULTS_STATE.md`. It was prepared after the parent recorded the transcription freeze and context opening. It does not interpret the manuscript or change its transcription.

**The underlying result CSVs, intake documents, previous-package notes, planning documents, and Hua findings register are not supplied.** They have not been inspected. Many entry statements, status strings, and even location fields end in an ellipsis; missing hypotheses, conclusions, locations, or review qualifications must not be reconstructed from these excerpts. Source paths below reproduce register metadata; they do not establish access to those files. The external repository named for Hua was not accessed for this ledger.

`RESULTS_STATE.md` was built on 15 November 2026 at 16:00 UTC. The README's earlier statement that the ZIP contains only its README and that nothing yet bears on these folders is superseded by its appended 15 November notice and the actual presence of `RESULTS_STATE.md`; it is not an adequate description of the supplied bundle.

**Status discipline:** “Proved,” “Refuted,” “Known,” and “Open” ordinarily report a prior model run's own claim. An intake reading is not a referee verdict. Prior-package research notes are first-pass leads. Planning entries are unchecked. The register reports referee review for specifically named items; its stated limitations must accompany those claims.

Relevance labels below mean: **D**, direct same-cote lead requiring manuscript checking; **P**, planning obligation; **T**, a possible broad thematic connection, with no demonstrated transfer of results; **N**, no demonstrated connection to quasi-finite/unramified/étale representability in the supplied excerpt, and therefore a likely broad-term retrieval match; **M**, methodological, bibliographical, or coverage metadata. “Not stated” means no entry-specific scan is visible; a scan-like number inside an ID or a filename's package range is not silently promoted to a source location. `R` denotes the supplied `notes/RESULTS_STATE.md`; the following number is its physical line.

## Direct planning anchors and same-cote findings

| ID or anchor | Supplied status | Source and location | Relevance and limit |
|---|---|---|---|
| Rank 22; order W; Book I, I.VI, Chapter VI | Unchecked plan placement | README, “This package in our plan”; cote 131, scans 002–042 | **P.** Construction techniques: descent, representable functors, Hilbert and Hom. This is the direct organizational placement. The retained-scan exclusions come from the task, not from this context entry. |
| S19; “residue of Book I” | Standing planning item, unchecked; no separate full S19 text supplied | README, “What our planning document asks”; also MPL_33_002-049 §2, R53 | **P.** Applies to this package. README gives no question beyond the standing ones. The prior-note excerpt associates S19 with comparison against print and the Stacks project; the complete S19 specification is unavailable. |
| I.V, I.VI, I.XI, II.8; descent, heights, local symbols, étale cohomology | Preliminary subject guesses, explicitly to be tested | README, planning paragraph; rank 22 | **P.** The parent must confirm or reject each topic with manuscript evidence. “Heights” and “local symbols” are not established content merely because this bundle was selected under them. |
| 131-locally-quasi-finite-representability | Hua AI-produced claim; visible status begins “conjecture (candidate: their search found no reference)”; remaining status truncated. Intake: “new to us: our package for this cote is waiting” | R80; Hua findings register, exact filename not supplied; their pp. 1–5, 13, 15; explicitly mapped to our scans **002, 003, 004, 005, 006, 014, 016** | **D.** Claims a criterion for representation by a locally quasi-finite separated scheme over a locally noetherian base. The excerpt names descent, local finite presentation, completion effectivity, artinian pro-representability, and part of a valuative condition. The statement is truncated: do not reconstruct a complete biconditional or treat the no-reference search as novelty evidence. |
| 131-unramified-and-etale-corollaries | Hua AI-produced claim; visible status begins “literature: Nothing remains to settle for the unramified an…” and is truncated. Same “new to us” intake | R81; Hua findings register, exact filename not supplied; their pp. 11, 15–16; explicitly mapped to our scans **012, 016, 017** | **D.** Claims unramified/étale separated representability criteria, conditions (1)–(6), a one-dimensional extension condition, and announced applications including Hom of abelian schemes and Picard. Both statement and literature verdict are incomplete. Every comparison requires the parent's frozen readings and, for literature claims, independent source checking. |

For the Hua entries, use the **explicit scan lists above**. The register's prose describes a one-page numbering offset; it should not replace those explicit lists with a new inferred mapping. These two entries are the only primary entries expressly claiming findings on cote 131.

## Open result entries: 5 of 5

| ID | Supplied status | Underlying source and visible location | Relevance |
|---|---|---|---|
| LM7 E.23 | Open; run claim | `LM7_FERMAT_TOWER_results.csv`; §51.16, folios 733v–736v, scans 172–178, formulas (369)–(379); R13 | **N.** Arithmetic section maps and metabelian/depth-two quotients. Shared descent or étale vocabulary gives no representability implication. Statement truncated. |
| FLAGGED_149 B9 | Open; run claim | `FLAGGED_149_results.csv`; cote 149, §1, p.17, scans 35–36; R14 | **N.** Prime-to-p point/section question for hyperbolic curves. Do not equate it with functor representation. Statement truncated. |
| LM1 D.11 | Open; run claim | `LM1_GROUP_SCHEMES_results.csv`; location printed as “49; 608-609; 610; task D.c integral classification”; R15 | **T.** Arithmetic descent of an integral μ₂-extension group at 2 could require a precisely formulated group-scheme comparison. The excerpt supplies no such comparison; the meaning of the numeric locations is not expanded. |
| LM4 D.12 | Open; run claim | `LM4_FINITE_GROUP_ACTIONS_results.csv`; “25 bis; 157 verso--160; 312--317; 30; 194 verso; 384”; R16 | **N.** Profinite GT₀ torsion and low-type mapping-class groups. Numeric location types are not explicitly expanded; statement truncated. |
| LM4 F.7 | Open; run claim | `LM4_FINITE_GROUP_ACTIONS_results.csv`; §30, folios 194–196, scans 383–387, Part D(b)/F(b); R17 | **N.** Nonsolvable completion centralizers, not a supplied representability result. Statement truncated. |

## Settled-status result entries: 17 of 17

| ID | Supplied status | Underlying source and visible location | Relevance |
|---|---|---|---|
| FLAGGED_149 F17.1 | Known; run claim | `FLAGGED_149_results.csv`; cote149 §3, manuscript pp.49–51, scans100–103; R22 | **N.** Nonabelian good-reduction criterion over a DVR; truncated hypotheses/conclusion. |
| LM7_PUSH E.64 | Proved; run claim, with referee qualification: proved where checkable; E.39, Boggi 2026, and NTY 2010 not opened | `LM7_PUSH_results.csv`; “Where: E.3”; no scan stated; R23 | **N.** Hyperelliptic descent and CM comparison characters in a GT action. The word “descent” does not supply a link to quasi-finite representation. |
| LM7_PUSH E.67 | Proved; run claim; referee: general statements proved, 48 per-word fibre claims not recomputed | `LM7_PUSH_results.csv`; “Where: E.3”; no scan stated; R24 | **N.** Mordell sign/Gaussian norm comparison, not a general representability theorem. |
| LM7_PUSH F.30 | Proved; run claim | `LM7_PUSH_results.csv`; “Where: F.4”; no scan stated; R25 | **N.** Torsion test over actual finite p-adic covers. Truncated. |
| FLAGGED_149 A8 | Proved; run claim | `FLAGGED_149_results.csv`; cote149 §1, pp.4–6, scans10–13; R26 | **T.** Artin-model constructions are broadly adjacent to algebraic-geometric construction techniques, but the excerpt gives no direct theorem for the present functors. Truncated. |
| FLAGGED_149 B13 | Refuted; run claim | `FLAGGED_149_results.csv`; cote149 §1, p.18, scan38; R27 | **N.** A toric-kernel disjointness assertion in generalized Jacobians. The shared abelian-scheme setting does not transfer the counterexample. |
| FLAGGED_149 B6 | Proved; run claim | `FLAGGED_149_results.csv`; cote149 §1, p.17, scan35; R28 | **N.** Positive-characteristic point-section theorem for schemes admitting semiabelian immersions. Statement truncated. |
| FLAGGED_149 C3 | Proved; run claim | `FLAGGED_149_results.csv`; cote149 §3, manuscript pp.37–39,44, scans75–79,90; R29 | **N.** Nonabelian intersection formula; hypotheses and conclusion truncated. |
| FLAGGED_149 F17.7 | Proved; run claim | `FLAGGED_149_results.csv`; cote149 §3, manuscript pp.50–51, scans101–103; explicitly a reader correction of condition e; R30 | **N.** Potential good reduction, not the present separated-representability criterion. |
| LM7 C.1 | Known; run claim | `LM7_FERMAT_TOWER_results.csv`; §51.13–14, folios719–724, scans143–153, formulas(299)–(323); R31 | **N.** Fermat Picard 1-motive and realizations. “Picard” alone is insufficient to link to the Picard representability application. |
| LM7 C.5 | Proved; run claim | `LM7_FERMAT_TOWER_results.csv`; Part C(b), Lead3, comparison with §51.14; no explicit scan in this row; R32 | **N.** A specific generalized-Jacobian extension class and splitting exponent. |
| LM7 C.8 | Refuted; run claim | `LM7_FERMAT_TOWER_results.csv`; §51.13, folios719–720, scans143–145, formulas(299)–(304); §51.14, folios720′–724, scans146–153, formulas(305)–(323); R33 | **N.** Refutes a specific interpretation of Lead3; no general representability consequence supplied. |
| LM7 D.51 | Proved; run claim | `LM7_FERMAT_TOWER_results.csv`; visible location includes Part D(e), §51.16, folio734v, scan174; another §51.15/folio725… location is truncated; R34 | **N.** Class-two source-kernel image. Do not reconstruct the missing location or statement. |
| LM7 E.109 | Proved; run claim | `LM7_FERMAT_TOWER_results.csv`; §51.16, folios733v–736v, scans172–178; remaining location and statement truncated; R35 | **N.** Pro-five arithmetic action and a pure-CM module. |
| LM7 E.124 | Proved; run claim | `LM7_FERMAT_TOWER_results.csv`; §51.16, folios733v–736v, scans172–178, through E46 maps; further location truncated; R36 | **N.** Explicit unit norms and 3-class groups; no supplied scheme-representability connection. |
| LM7 E.96 | Proved; run claim | `LM7_FERMAT_TOWER_results.csv`; §51.16, folios733v–736v, scans172–178, formulas371–379, Part E(c),(d), follow-up4; R37 | **N.** A class-two arithmetic obstruction calculation. Statement truncated. |
| LM7_PUSH C.6 | Proved; run claim | `LM7_PUSH_results.csv`; “Where: C.3”; no scan stated; R38 | **N.** Class-two germ classification and a qualified pure-residue claim. The word “germ” is not evidence of a connection to local pro-representability. |

## Intake readings: 2 of 2

| ID | Supplied status | Underlying source and location | Relevance |
|---|---|---|---|
| INTAKE LM6_FINAL_20261114 §1 | Intake reading, explicitly not a referee verdict | `INTAKE_LM6_FINAL_20261114.md`, §1; no manuscript scan stated; R43 | **N.** A truncated overview of 13 open anabelian section rows, visibly including B.27. It does not expose the other twelve rows. |
| INTAKE LM7_CONTINUED §? | Intake reading, explicitly not a referee verdict; section identifier itself uncertain | `INTAKE_LM7_CONTINUED.md`, §?; no manuscript scan stated; R44 | **N.** A truncated table of 52 new rows about E.23, visibly including E.37. It is not 52 supplied statements or proofs. |

## Earlier-package research notes: 12 of 12

All entries in this table retain their supplied status as **first-pass leads**, including those labelled “observation.”

| ID | Supplied kind | Underlying source and explicit location | Relevance |
|---|---|---|---|
| MPL_33_002-049 §96 | Observation | `MPL_33_002-049_notes.md`, §96; no specific scan; R49 | **M.** Register-coverage appendix, itself stating that underlying originals were not opened. No mathematical result in the visible excerpt. |
| MPL_142_001-093 §316 | Observation | `MPL_142_001-093_notes.md`, §316; no specific scan; R50 | **M.** Bibliography and verification-limits section; SGA1 citation metadata is not a proof or a same-cote cross-reference. |
| MPL_14_002-044 §107 | Observation | `MPL_14_002-044_notes.md`, §107; no specific scan; R51 | **M/T.** A truncated plan-comparison table on effectivity, grading, and Lefschetz material. No concrete transfer to this cote is supplied. |
| MPL_14_002-044 §108 | Observation | `MPL_14_002-044_notes.md`, §108; no specific scan; R52 | **M.** Bibliographic key explanations; no new mathematical statement. |
| MPL_33_002-049 §2 | Observation | `MPL_33_002-049_notes.md`, §2; visible scan text stops at “002…”; R53 | **P/M.** Confirms that a previous package associated S19 with print/Stacks comparison. Its truncated scan reference cannot be expanded. |
| MPL_144_001-061 7.1 | Observation | `MPL_144_001-061_notes.md`, §7.1; visible source line **scan003:9**; R54 | **M/N.** An inventory of explicit questions/cautions; the dimension-related excerpt is too incomplete for a mathematical cross-link. |
| MPL_149_091-136 RN100-02 | Reading question | `MPL_149_091-136_notes.md`, RN100-02; no explicit scan field beyond the ID; R55 | **N.** Meaning of the abbreviation VA and a historical/publication attribution. Neither is established by the excerpt. |
| MPL_149_091-136 RN102-03 | Unpursued implication | `MPL_149_091-136_notes.md`, RN102-03; no explicit scan field beyond the ID; R56 | **N.** What a p-divisible-group criterion can detect in curve reduction; no representability criterion follows. |
| MPL_14_002-044 A26 | “Unproved claim: transposition and the c…”; label truncated | `MPL_14_002-044_notes.md`, A26; **scan037, lines5–12**; cross-search cites cote44 scans002,008 and cote54 scans003,005; R57 | **N/T.** Complementary-degree duality. The source shorthands T, N, and D08 are not resolved here; shared abelian/Picard vocabulary is insufficient. |
| MPL_33_002-049 §93 | Observation | `MPL_33_002-049_notes.md`, §93; no specific scan; R58 | **M.** Title/outline and folio-numbering inventory referring to T01–T04; no manuscript theorem. |
| MPL_33_098-146 §65 | Observation | `MPL_33_098-146_notes.md`, §65; no specific scan; R59 | **M.** Methodological example of distinguishing self-flagged steps and withdrawals. It provides no same-cote evidence. |
| MPL_91_099-143 §68 | Observation | `MPL_91_099-143_notes.md`, §68; visible scans **124** (title), **126,128** (thickness); further excerpt truncated; R60 | **T.** Greenberg–Néron/approximation vocabulary may justify a carefully specified future comparison. The underlying argument is unavailable and must not be cited as established. |

## War-game questions: 10 of 10

| ID | Supplied status | Underlying source and visible location | Relevance |
|---|---|---|---|
| WG H9 | Hunch, “Believe,” unchecked | `WARGAME_MATH_HUNCHES_20261112.md`; Book II, cote44, Th.4–5; no scan; R65 | **N.** Mordell–Weil lattice/height and Hodge-index material. The rank22 “heights” keyword is not evidence that cote131 treats it. |
| WG2 §1.1 #3 | Round2 plan, unchecked | `PROGRAM_WARGAME_ROUND2_20261112.md`; archive folders06–09; cotes16,44,47,54; no scan; R66 | **N/M.** Book II organization; no direct cote131 statement. |
| WG2 §2.1 #2 | Round2 plan, unchecked | Same source; cotes16,54,37 named; excerpt specifies manuscript pp.1–16, nos1–8, **scans3–18**, but its shortened context does not independently identify every attribution; R67 | **N.** Graded correspondence rings and Lefschetz operators. |
| WG2 §1.1 #2 | Round2 plan, unchecked | Same source; §1.1; no scan; R68 | **N.** Poincaré–Hodge algebras, Fourier functors, vector extensions, and heights. Shared “abelian schemes” is a broad-term match. |
| WG2 §2.3 #12 | Round2 plan, unchecked | Same source; §2.3; Th.2–5 listed, no scan; R69 | **N/T.** Algebraic representatives and duality, not an excerpted locally quasi-finite criterion. |
| WG2 §2.3 #13 | Round2 plan, unchecked | Same source; §2.3; no scan; R70 | **T.** Algebraic representatives, functoriality, and descent are a possible comparison topic only. Mentioned literature and bibliography keys have not been independently checked here. |
| WG2 §Summary #2 | Round2 plan, unchecked | Same source; summary; first package cotes16,47,54,44; no scan; R71 | **N/M.** Book II summary, not direct evidence about this cote. |
| WG H2 | Hunch, “Believe,” unchecked | `WARGAME_MATH_HUNCHES_20261112.md`; completes R4; no scan; R72 | **N.** Vanishing cycles and arithmetic actions on geometric fundamental groups. |
| WG2 §2.4 #4 | Round2 plan, unchecked | `PROGRAM_WARGAME_ROUND2_20261112.md`; folders06–09, cotes47,44, earlier Th.1–7; no scan; R73 | **N/T.** Search for another Fourier-transform/compatibility witness; no supplied witness in cote131. |
| WG2 §2.5 #6 | Round2 plan, unchecked | Same source; §2.5, referring to §6; no scan; R74 | **N.** Research prompts FOURIER_1970 and LEFSCHETZ_RINGS, not the representability intake. |

## Secondary identifiers visible without a full standalone entry

This section prevents short cross-references from being mistaken for separately supplied results. Prefixes are retained where explicit; local references are not assigned a different register by guesswork.

| Visible identifier(s) | Visible status or role | Source/scan availability and relevance |
|---|---|---|
| LM4 D.32; LM4 D.34 | Introductory referee paragraph says “refereed and proved as claimed” | R8; no statements or scans supplied here. **N**, GT/mapping-class context, not a usable representability lemma. |
| LM7_PUSH D.44; D.50; E.58; E.61; E.62; E.65 | Same introductory referee claim | R8; no full statements/scans. The displayed chain is D.50 → E.58 → E.65, reducing an E.3 question to a character Δ. **N**. E.64/E.67 are separately listed above with their detailed limits. |
| LM7_PUSH E.3 | Target question named in the referee paragraph and E.64/E.67 locations | No full entry or scan supplied. **N**. |
| LM7 E.16; E.37 | E.23 refers to E.16 section-map targets and an E.37 intrinsic pro-3 calculation; intake also mentions E.37 | R13,R44; no independent statement/proof/status beyond those descriptions. **N**. |
| LM4 D.29 | D.12 says it refutes a finite geometric-recognition assertion by an involution | R16; not a standalone supplied entry or separately stated review verdict. **N**. |
| E.39; E.64.28–29 | E.39 is a not-opened dependency named in E.64's qualifier; E.64.28–29 are references within E.67's excerpt | R23,R24; no independent contents. Do not silently treat equation-level references as reviewed rows. **N**. |
| LM7 D50; E46; Lead3; follow-up4 | Local dependencies/lead labels in D.51, E.124, C.5/C.8, and E.96 | R32–34,R36–37; no separate full entries. D50/E46 are printed without dots. Lead3 is described differently by C.5/C.8, but its original text is absent. **N**. |
| LM2, “two-torus and Fermat follow-ups” | Additional provenance reference within the truncated D.51 location field | R34; no LM2 result ID, statement, or complete location is supplied. **N/undetermined**. |
| LM7_PUSH F.4; C.1; C.3; C.11 | F.30/C.6 locations or task/dependency references; C.11 is said to disprove a verbatim pure-residue extension | R25,R38; no independent full statements or scans. **N**. |
| FLAGGED_149 F17; F12; C2; F17.6 | Local flags or hypotheses referenced by F17.1, C3, F17.7 | R22,R29–30; do not substitute the referencing excerpt for these absent statements. **N**. |
| B.27, within INTAKE LM6_FINAL_20261114 | Marked “main” among 13 open rows | R43; the visible point/section question is truncated. The other twelve IDs are not visible and cannot be enumerated. **N**. |
| WG2 §2.4 #3; WG2 §6. #9 | Unchecked plan references inside a prior-note comparison | R51, `MPL_14_002-044_notes.md` excerpt; no full entries/scans. **M/T**. |
| MPL_33_002-049 T01–T04, including T03 | Title/outline/folio evidence labels referred to by §93 | R58; original notes and their scan mappings unavailable. **M**. |
| WG R4 | Earlier hunch referred to by WG H2 | R72; statement, status, and source location not expanded. **N**. |
| FOURIER_1970; LEFSCHETZ_RINGS | Named research prompts | R74; unchecked plan descriptions, no full tasks. **N**. |
| T; N; D08; D09; D10; Tate66/T66; DM | Source/note/bibliography shorthands, not independently supplied result rows | R52,R57,R70. Some ownership is unresolved; Tate66/T66 are expressly equated and DM identified as Deligne–Milne by the excerpt. No external work was opened. **M**. |
| LM1 task D.c | Integral-classification task label | R15; no independent task text or resolved numeric scan mapping. **T**. |
| FLAGGED_149 ZCF6; ZD10; Z142g | Run summary says these remain open, alongside B9 | R85; no statements/scans supplied. **N/undetermined**, not additional usable open-problem descriptions. |

## Run-summary entries: 4 of 4

All four summaries cite `MATHS_PROMPTS_TALLY.md`, whose full path and contents are not supplied.

| Run ID | Supplied run state | Coverage limit |
|---|---|---|
| FLAGGED_149 | Returned 12 November; incomplete; B9, ZCF6, ZD10, Z142g open | R85; describes a run, not proof verification. |
| LM4 | Returned 14 November; intake 14 November | R86; intake metadata is not a referee verdict for every row. |
| LM7 | Returned 13–14 November; directory `answers/LM7_FERMAT_TOWER_20261114T0311Z_unzipped` | R87; directory is metadata, not accessible source material. |
| LM7_PUSH | Ran 13–14 November; checkpoint09 last material; intake14 November | R88; later or missing continuation must not be assumed. |

## Underlying source-path index, reproduced as metadata

Every path below is relative to the Documents folder named by the register; none of these underlying files is present in the supplied two-file context.

| Filename | Path printed in the register |
|---|---|
| PROGRAM_WARGAME_ROUND2_20261112.md | `grothendieck_archive_montpellier/PROGRAM_WARGAME_ROUND2_20261112.md` |
| WARGAME_MATH_HUNCHES_20261112.md | `grothendieck_archive_montpellier/WARGAME_MATH_HUNCHES_20261112.md` |
| MPL_142_001-093_notes.md | `grothendieck_archive_transcription_20261110/returns/MPL_142_001-093_unzipped/MPL_142_001-093_notes.md` |
| MPL_144_001-061_notes.md | `grothendieck_archive_transcription_20261110/returns/MPL_144_001-061_unzipped/MPL_144_001-061_notes.md` |
| MPL_149_091-136_notes.md | `grothendieck_archive_transcription_20261110/returns/MPL_149_091-136_unzipped/MPL_149_091-136_notes.md` |
| MPL_14_002-044_notes.md | `grothendieck_archive_transcription_20261110/returns/MPL_14_002-044_unzipped/MPL_14_002-044_notes.md` |
| MPL_33_002-049_notes.md | `grothendieck_archive_transcription_20261110/returns/MPL_33_002-049_unzipped/MPL_33_002-049_notes.md` |
| MPL_33_098-146_notes.md | `grothendieck_archive_transcription_20261110/returns/MPL_33_098-146_unzipped/MPL_33_098-146_notes.md` |
| MPL_91_099-143_notes.md | `grothendieck_archive_transcription_20261110/returns/MPL_91_099-143_unzipped/MPL_91_099-143_notes.md` |
| FLAGGED_149_results.csv | `longue_marche_pro_pilot_20261104/answers/FLAGGED_149_unzipped/FLAGGED_149_results.csv` |
| LM1_GROUP_SCHEMES_results.csv | `longue_marche_pro_pilot_20261104/answers/LM1_GROUP_SCHEMES_rerun_20261112_unzipped/LM1_GROUP_SCHEMES/LM1_GROUP_SCHEMES_results.csv` |
| LM4_FINITE_GROUP_ACTIONS_results.csv | `longue_marche_pro_pilot_20261104/answers/LM4_FINITE_GROUP_ACTIONS_20261114T0406Z_unzipped/LM4_FINITE_GROUP_ACTIONS_results.csv` |
| LM7_FERMAT_TOWER_results.csv | `longue_marche_pro_pilot_20261104/answers/LM7_FERMAT_TOWER_20261114T0311Z_unzipped/LM7_FERMAT_TOWER/LM7_FERMAT_TOWER_results.csv` |
| LM7_PUSH_results.csv | `longue_marche_pro_pilot_20261104/answers/LM7_PUSH_checkpoint_09_20261113T2242Z_unzipped/LM7_PUSH/LM7_PUSH_results.csv` |
| INTAKE_LM7_CONTINUED.md | `pro_intake_20261113/INTAKE_LM7_CONTINUED.md` |
| INTAKE_LM6_FINAL_20261114.md | `pro_intake_20261114/INTAKE_LM6_FINAL_20261114.md` |

## Working use for the research notes

For each manuscript note, the parent should record its actual context search and identify either a specific entry above or the absence of a substantive match. The direct Hua entries and planning S19/rank22 warrant explicit comparison. GT torsion, anabelian sections, CM/number-field calculations, heights, Lefschetz rings, and Fourier-transform plans should not become asserted connections solely because their excerpts were retrieved by “étale,” “abelian,” or “descent.” A tentative connection can be proposed as an own idea, with its additional hypotheses and absent evidence stated.

Read-only structural validation after context opening reported **38 pages, 679 inventory rows, 39 matching frozen SHA-256 records, zero errors, and zero warnings**. This records structural integrity only, not a second independent handwriting judgment.
