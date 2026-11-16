# Final register and monodromy-inventory QA

## Outcome

**PASS on coverage and status:** all **51** individually listed register entries are represented **exactly once** in `records/results_disposition.md`: all **44 returned-package leads** plus the **7 open/proved-return/intake/planning entries**, with no missing ID, extra ID, duplicate ID, false upgrade or transfer of a referee verdict. All individual A/B note-level prior scan locators agree with the supplied notes' metadata; the section-level descriptions and three unavailable-package limitations also agree with the register excerpts. The proposed adjustment of the B N37 row to unresolved signs/cones wording is appropriate and remains the root agent's edit.

**Actionable precision issues:** replace `177–179` by `177,179` in the WG2 and `MPL_14_002-044 §107` operator-source comparisons; consider the four compact correction-inventory additions below. No omitted substantive monodromy forward promise or author-flagged uncertainty was found.

This check used the register, the disposition table, both supplied same-cote note files, the existing research/integration/source records, and frozen TeX text only. No scans or optional external literature were opened; the only file written by this QA pass is this report.

## Inputs and evidence boundary

- Register: `context/notes/RESULTS_STATE.md`, build label **2026-11-15 16:00 UTC**.
- Disposition: `records/results_disposition.md`.
- Prior-note sources: `context/same_cote_33/MPL_33_002-049_notes.md` (A) and `context/same_cote_33/MPL_33_098-146_notes.md` (B).
- Inventory: `records/research_monodromy_final.md`; source candidates/search trail in `records/research_monodromy.md`.
- Auxiliary current-package cross-checks: `records/research_integration.md`, `records/primary_sources.md`, and the relevant R-note metadata in `records/research_reused_sheets_final.md`.

Coverage was checked by exact-ID set equality and uniqueness; statuses, wording and scopes were then inspected. “Source-scope verified” here means consistency with the **supplied register/notes and available frozen textual locators**, not a new independent reading of unavailable historical scans or full external papers.

### Audited text fingerprints

| Input | SHA-256 |
|---|---|
| `context/notes/RESULTS_STATE.md` | `ab9f6902dae53de4f65ebf48b60477489edd69bc3cfa17d737e49b619c05b2b4` |
| `MPL_33_147-181+34_002-017_work/records/results_disposition.md` | `028b9330e4a9224d4418f4d0d729b3284bf71d450f8563f784d8b1b480559034` |
| `MPL_33_147-181+34_002-017_work/records/research_monodromy_final.md` | `e038434643fb683aacbe034e5c751e1c433921f635739e5fc5680932d3468f61` |

## Seven non-lead rows

| Exact ID | Supplied status retained | Scope check |
|---|---|---|
| LM7 E.23 | Open (the return's claim) | Section-map image/fibres for geometric metabelian and marked depth-two quotients; §51.16, folios 733v–736v, project scans 172–178, (369)–(379); no conflation with cote 33 or tame centrality |
| LM4 D.12 | Open (the return's claim) | Full profinite $GT_0$/low-type torsion question; “25 bis,” 157 verso–160, 312–317; 30, 194 verso, 384; the disposition does not claim its answer follows from tame inertia |
| LM4 F.7 | Open (the return's claim) | Mapping-class profinite-completion centralizers, especially geometric $A_5$; §30, folios 194–196, scans 383–387, Parts D(b)/F(b); kept distinct from valuation completion |
| LM7_PUSH C.6 | Proved (the return's claim) | Class-two germ classification, source C.3; correctly not promoted to an individually refereed result |
| INTAKE LM7_CONTINUED §? | Intake reading, not a referee verdict | Part E/E.37 excerpt, integrality/convergence and section-map fibre language; full intake file explicitly unavailable |
| WG H9 | Hunch of the war game (Believe; unchecked) | Cote 44, Theorems 4–5, codimension-$m$ Mordell–Weil/Hodge-index question; pencil and Picard material does not settle it |
| WG2 §2.1 #2 | Question or plan item of the war game (round 2; unchecked) | Cotes 16,54,37 and graded endomorphism/Lefschetz programme; distinction from analytic operator pages is correct, with the exact current scan-list adjustment below |

The intake label is a faithful shortened status, although it omits the register's parenthetical model/effort provenance; it makes no stronger claim. The original file basenames are correct for all seven rows. The added section sign before “25 bis” is an editorial locator normalization rather than a mathematical change; use the register's bare “25 bis” if exact literal locator formatting is desired.

## All 44 returned-package leads

Every row below has the exact supplied **Lead** status, expanded in the disposition preamble as “observation (research note of a returned package, first pass; a lead).” The ledger checks identifiers, prior source and scope, not the mathematical truth of the earlier unreviewed notes.

| Exact register ID | Source scope checked | QA |
|---|---|---|
| MPL_33_002-049 §96 | A, register-disposition section | PASS; Lead retained |
| MPL_33_002-049 §2 | A, plan assessment; scans 002–048 | PASS; Lead retained |
| MPL_33_002-049 §93 | A, titles/outline labels | PASS; Lead retained |
| MPL_33_098-146 §1 | B, source/evidence scope | PASS; Lead retained |
| MPL_33_098-146 §65 | B, explicit unverified/deferred-step inventory | PASS; Lead retained |
| MPL_33_098-146 §76 | B, S19 comparison map | PASS; Lead retained |
| MPL_33_002-049 N01 | A, 002 | PASS; Lead retained |
| MPL_33_002-049 N11 | A, 012 | PASS; Lead retained |
| MPL_33_002-049 N21 | A, 020, 032, 034 | PASS; Lead retained |
| MPL_33_002-049 N29 | A, 028, 030 | PASS; Lead retained |
| MPL_33_002-049 N35 | A, 024, 034, 036 | PASS; Lead retained |
| MPL_33_002-049 T04 | A, handwritten outline, 002–048 | PASS; Lead retained |
| MPL_33_002-049 §100 | A, primary comparisons | PASS; Lead retained |
| MPL_33_098-146 N20 | B, 122 | PASS; Lead retained |
| MPL_33_098-146 N21 | B, 122 | PASS; Lead retained |
| MPL_33_098-146 N29 | B, 134, 136 | PASS; Lead retained |
| MPL_33_098-146 N37 | B, 146 | PASS; Lead retained |
| MPL_33_098-146 §3 | B, register disposition | PASS; Lead retained |
| MPL_33_098-146 §78 | B, stable Stacks locators | PASS; Lead retained |
| MPL_142_001-093 §316 | Register excerpt only; bibliography/verification limits | PASS; Lead retained |
| MPL_14_002-044 §107 | Register excerpt only; grading/Lefschetz-plan disposition | PASS; Lead retained |
| MPL_33_002-049 N15 | A, 014, 032 | PASS; Lead retained |
| MPL_33_002-049 N17 | A, 016 | PASS; Lead retained |
| MPL_33_002-049 N26 | A, 026 | PASS; Lead retained |
| MPL_33_002-049 N27 | A, 026 | PASS; Lead retained |
| MPL_33_002-049 N28 | A, 026, 028 | PASS; Lead retained |
| MPL_33_002-049 N31 | A, 032 | PASS; Lead retained |
| MPL_33_002-049 N33 | A, 028, 034 | PASS; Lead retained |
| MPL_33_002-049 N43 | A, 048 | PASS; Lead retained |
| MPL_33_002-049 N71 | A, 012 | PASS; Lead retained |
| MPL_33_002-049 T01 | A, 046 | PASS; Lead retained |
| MPL_33_002-049 §101 | A, outstanding original-source collation | PASS; Lead retained |
| MPL_33_002-049 §3 | A, note index | PASS; Lead retained |
| MPL_33_098-146 N01 | B, 098 | PASS; Lead retained |
| MPL_33_098-146 N08 | B, 108, 112 | PASS; Lead retained |
| MPL_33_098-146 N15 | B, 118 | PASS; Lead retained |
| MPL_33_098-146 N23 | B, 126 | PASS; Lead retained |
| MPL_33_098-146 N25 | B, 126–132 | PASS; Lead retained |
| MPL_33_098-146 N30 | B, 136, 140, 142 | PASS; Lead retained |
| MPL_33_098-146 N36 | B, 144, 146 | PASS; Lead retained |
| MPL_33_098-146 N40 | B, 128, 132, 146 | PASS; Lead retained |
| MPL_33_098-146 N41 | B, 130–146 | PASS; Lead retained |
| MPL_33_098-146 N54 | B, 145 | PASS; Lead retained |
| MPL_91_099-143 §68 | Register excerpt only; 124, 126, 128 | PASS; Lead retained |

### Section and unavailable-source checks

- A §2 really describes the handwritten 002–048 programme, so that range in the disposition is supported rather than an accidental truncation of the full 002–049 package.
- A §93, §96, §100 and §101 are respectively outline, register accounting, primary comparisons and remaining collation limits; no theorem is inferred merely from those section labels.
- B §1, §3, §65, §76 and §78 are respectively evidence scope, register accounting, self-flag inventory, S19 comparison map and stable locators; their statuses stay first-pass leads.
- `MPL_142_001-093 §316`, `MPL_14_002-044 §107`, and `MPL_91_099-143 §68` are correctly limited to register excerpts, with their full note files unavailable; the Néron row does not claim to verify the Greenberg/thickness material.
- The note-level scan lists N01/N11/N15/N17/N21/N26/N27/N28/N29/N31/N33/N35/N43/N71/T01/T04 in A and N01/N08/N15/N20/N21/N23/N25/N29/N30/N36/N37/N40/N41/N54 in B match the supplied note metadata, including B N36 at 144/146 and B N37 at 146.

### Referee and workflow statuses

The disposition exactly preserves the register's limited referee list: **LM4 D.32, D.34; LM7_PUSH D.44, D.50, E.58, E.61, E.62, E.64, E.65, E.67**. It correctly does not extend that review to C.6, the three open rows, the intake, planning guesses or archive-package leads. “RETURNED” is correctly treated as workflow state rather than mathematical validation. No separate Michel Hua row occurs in the supplied register.

## Specific wording actions

### Q1. Use the exact operator-source scan list

**Locations:** WG2 §2.1 #2 row and MPL_14_002-044 §107 row of `records/results_disposition.md`.

**Current:** “33/177–179.”

**Recommended:** “33/177,179.”

**Reason:** R20–R24 identify the typed analytic operator leaves at 177 and 179; the intervening 178 is handwritten duality material, so the inclusive range can accidentally blur the source distinction that the table otherwise preserves. This is a locator precision correction, not a change in the negative context-match conclusion.

### Q2. B N37 signs/cones wording

The root's stated replacement of “a doubtful sign-verification margin” by unresolved signs/cones wording is appropriate; no stronger claim about a definite authorial verification request should be recovered from an uncertain reading. The row's exact ID, earlier scan 146, Lead status and refusal to infer automatic sign verification are already correct.

### Q3. Four small additions to the M correction inventory

These source edits are already reflected in the note discussions or hypotheses, but are not each expressly indexed in the **major-withdrawal** table; adding the following compact rows would make its mathematical-scope corrections more complete without creating new claims or additional long notes.

| Suggested ID | Frozen locus | Literal revision | Scope safeguard |
|---|---|---|---|
| R14 | 34/004:6,13,22 | inserted “comm.”; inserted “pour $i=1$”; live properness and $i=1$ retained in the reordered Picard sentence | Commutative algebraic-group example and degree-one/proper Picard comparison; no extension to arbitrary groups or all degrees; M03/M04 |
| R15 | 34/007:20 | deleted “Sa puissance”; inserted “Sa puiss. tensorielle” | Tensor powers are explicit; the convention for negative integers still requires explanation outside the witness; M10 |
| R16 | 34/011:4,10 | deleted “l'isomorphisme de”; inserted “l'opération naturelle”; inserted “primitives” | The action, rather than a chosen trivialization, is intrinsic; generator choices require primitive roots; M16 |
| R17 | 34/012:10 | deleted “extension”; inserted “clôture” before “séparable” | The chosen object is a separable closure; the same sentence's literal repeated $K'$ and subsequent base-field label discrepancies remain reading questions; M17 |

**Do not make the nearby 34/011:6 change into a definite cancellation:** the frozen reading gives alternatives between a deleted/inserted “on a” / “il existe” construction and an underlined “il existe.” The certainty of the “primitives” insertion at line 10 does not resolve that line-6 ambiguity.

## M self-flag completeness check

No substantive forward promise, expressly requested verification, authorial caution, or cancelled open-task formulation is missing from the final inventories:

- Arithmetic-monodromy programme: 003:5, F01/M01/M28.
- Néron promise and reverse direction: 005:9, F02/M05; possible all-degree question mark remains uncertain in F03.
- Conditional invariant-cycle promise: 005:11, F04/M06.
- Deligne/Picard promise: 005:15–006:8, F05/M07/M08, with no inserted genericity.
- Seminar's inertia/extension programme: 008:20–009:4, F06/M11/M28.
- “On verra que” with “toute” changed to “parfois”: 009:4, F07/M12.
- Noncanonical root-choice caution: 011:10, F08/M16.
- Task to determine the inertia map, answered by 014:14: 013:4, F09/M18/M19.
- Cancelled complete-trait remark and “Attention”: 014:25–28, F10/M20.
- Remaining injectivity, reduced to known continuity: 015:11, F11/M22.
- Inertia-intersection verification request: 016:4–6, F12/M23.
- Cancelled “reste à examiner” and replacement conjugation argument: 016:18–017:14, F13/M25/M26.

The routine-future inventory also explicitly covers 003:14/20/30, deleted “On notera” on 007:20, conditional “on aura” on 008:18 and 013:39, “On notera / On vérifie trivialement” on 010:19, the proof reductions on 015:4, “On sait” on 015:6 and the general-theory “on aura” on 016:8. The blank Hironaka/Néron/Lefschetz reference slots are separately noted. Editorial `\unsure` marks are not generally misrepresented as authorial doubt, and the Néron question mark remains explicitly doubtful.

## Final QA limits

This is a register-and-inventory audit, not a fresh mathematical referee report on all current D/R/I notes. The mathematical/archival safeguards remain intact: no unreviewed lead is promoted; no arithmetic/anabelian open item is settled by tame centrality; cancellation is not treated as refutation; the quartic example remains conditional on the literal unrestricted Picard claim; and the completion comparison retains finite separability rather than importing excellence.
