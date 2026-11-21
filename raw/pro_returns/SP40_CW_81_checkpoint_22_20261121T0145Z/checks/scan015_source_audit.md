# Scan015 source completeness audit

## Result

The single targeted source pass is complete. The assembled TeX carries the selected text, formulas, cancellations, insertions, drawing labels, graphical commands, and final archive comment. Every returned source row is traceable. No unmapped source difference, missing root ink decision, omitted common passage, or duplicate selected graphical component remains in this audit.

One compact-manifest locator defect was found and repaired during the pass: the final C-source excerpt begins partway through its covering first line. The added exact-start locator now reproduces the recorded fragment hash. The repair changed the manifest only; the assembled TeX stayed unchanged.

Root approval of the completed main record remains with root. This audit makes no new ink choice.

## Sources and audited revision

Read the complete packet `packets/015/C.tex`, `H.tex`, `C_inventory.json`, `C_doubts.txt`, and `C_notes.txt`; all three final `out/readers/015/{A,B,C}/reading.tex` files and report row sets; and the root decisions, source map, union, selected-source manifest, and record draft. The report pointers were checked against the actual source JSON rows, with the raw files retained by fingerprint.

- Selected TeX: `out/checks/scan015_final_draft.tex`.
- TeX SHA-256: `943c29ba8517a981cd502b0d8c39eccb587f7ec09a1c6ef4d0854580a1f80017`.
- Selected-source map: `out/checks/scan015_final_source_map.json`.
- Repaired source-map SHA-256: `f86502bf247432bb917a58c3517285cd4ff83c34207b416d96e672bf47543a87`.
- Decision authority: `out/checks/scan015_main_decisions.md`, sections 01–26.
- Record examined: `out/checks/scan015_record_draft.json`, with 96 decisions, 66 union inventory elements, and 27 remaining-doubt clusters attached to the selected TeX.
- Original source manifest: `out/checks/scan015_reader_fingerprints.json`.

The earlier pending S/status prose in `scan015_source_map.json` is explicitly identified as historical by the completed record. The current root decisions and attachments supply the final state.

## Common text and final-source coverage

The 24 selected-source blocks partition all 241 final TeX lines without gaps or overlaps. Every block has its original reader source, covering line range, emitted range, and fragment hashes. All root decision sections 01–26 occur in the component map. The unchanged common passages have their own source blocks, including the purpose paragraph and the complete `Soit` sentence.

| Final source span | Content checked |
|---|---|
| Lines 1–26 | Page/group setup; cancelled heading predecessor and `Version I`; complete `Soient` sentence, indexed family, insertion and guide; full upper-left note, arrow, both closure formulas, and its final parenthesis |
| Lines 27–45 | Complete (a) and (b), their tags and corrected predecessors; right NB and separate qualified upper rule; full main NB; purpose paragraph with its quotation marks and endpoint |
| Lines 46–58 | Complete case heading, both qualified predecessors, two selected underline commands, and full `Soit` setup |
| Lines 59–104 | Selected C drawing, all six live labels, qualified cancelled label, qualified corrected exponent, crossing paths, and detached mark |
| Lines 105–154 | Formula (1), `ce qui`, cancelled `résulte de`, both cancelled inclusions, live inclusion and `et`, qualified equivalence word, cancelled Car-si cluster, cancelled `Si on avait`, complete live continuation, (2), detached pair, qualified symmetry phrase, and (2′) |
| Lines 155–172 | Complete B lower-correction arrangement: `Comme`, raised cancelled words, inclusion, inserted i.e. clause, cancelled `il contient les`, selected underline span, and qualified `on a` |
| Lines 173–214 | Both lower-note formulas, `i.e.`, qualified instruction and `avant`, both separately qualified guides, lower intersection display, `Car`, closure/intersection formula, selected lower rule, and nonempty relation |
| Lines 215–241 | One `(sinon`, qualified inserted l'ouvert, Sigma, selected hooked guide, `serait`, inserted `un`, connector alternatives, final qualified cancelled group and selected remnants, final `X serait disconnexe),`, closing group, and exact archive comment |

The archive entry occurs once, as the final `% archive sheet number: 14` comment. `(sinon`, the final prose ending, and the page setup each occur once. Explicitly redrawn cancellation groups retain one visible text payload and an invisible `\phantom{\deleted{...}}` annotation. The source keeps the chosen generic deletion wrappers for cancellations whose geometry was retained by root.

No common word or formula was supplied from expected mathematics. The audit followed the selected literal passages and the root's explicit changes.

## Selected graphical commands and labels

All 39 selected `\draw`/`\fill` commands match their cited reader source strings and appear once in their assigned block, in source order. The final command multiset matches the selected-command multiset. The separate B upper-NB `\rule{.8em}{.35pt}` is present in its selected qualified overset wrapper.

The C main drawing contains its nine oval commands, the one command carrying two chord subpaths, three brace commands inside the selected `(5,33)` scope, two upper-left cancellation commands, and its selected filled mark. The six live labels retain C's exact node positions and strings:

| Node position | Selected label |
|---|---|
| `(139,116)` | `E_1` |
| `(150,247)` | `E_2` |
| `(430,68)` | `\Sigma_1^+` |
| `(501,193)` | `\Sigma_1^{\deleted{\unsure{+}}\unsure{-}}` |
| `(23,135)` | `\Sigma_2^-` |
| `(131,308)` | `\Sigma_2^+` |

The cancelled label at `(167,48)` preserves its qualified candidates and its selected crossing paths.

The final cancelled cluster contains C's angular command once and B G07's selected short upright command once. B G07's first angular command is absent, following root section 24. The lower note contains A's selected short guide and arrowhead once, and C's selected longer guide once. A GUIDE03 is absent, following root section 21. The B lower group's two literal cancellation paths and the B final insertion guide are present, together with the root's local wording changes.

## Wrapper syntax and declared placements

The fixed-origin claims were checked against the actual node anchors, scope syntax, units, and `out/PREAMBLE.tex`'s annotation macro. Each listed nested wrapper uses `baseline=0pt`, `anchor=base west`, and zero inner/outer separation. The source's uncertainty macro places its graphic argument before the uncertainty suffix.

| Selected component | Actual parent anchor | Inner units | Source treatment checked |
|---|---|---|---|
| C drawing MARK01 | `(507,153)` | `.013cm,-.013cm` | Selected filled body and `(0,0)`–`(4,6)` rectangle retained |
| A inclusion MARK03 | `(155,16)` | `.013cm,-.013cm` | Both fills and `(0,0)`–`(5,8)` rectangle retained |
| C lower MARK02 | `(291,52)` | `.009cm,-.009cm` | Selected body/rectangle retained; conversion to B parent's units explicitly recorded |
| A short lower guide | `(211,103)` | `.009cm,-.009cm` | Actual inner scope is `shift={(-211,-103)}` around the two unchanged A commands |
| C longer lower guide | `(163,196)` | `.009cm,-.009cm` | Selected body/rectangle retained; conversion to A note's units explicitly recorded |
| B upper upright | `(12,1)` | `.013cm,-.013cm` | Only `\draw (24,6) -- (26,16);` is added within the retained local rectangle |

These are checks of declared source placement and literal wrapper syntax. No curve extrema, glyph bounds, printed-page coordinates, or numerical geometry were calculated. Relative prose and label typography remains described at the scope stated in the selected-source manifest.

## Source-row traceability

| Source collection | Actual rows | Checked final linkage |
|---|---:|---|
| Reader differences | A 60, B 61, C 60: **181** | Every `(reader, JSON pointer)` occurs once in the difference crosswalk; each source ID agrees; every target decision exists and has reverse provenance and a root section |
| Reader doubts | A 21, B 23, C 22: **66** | Every actual doubt pointer occurs once; each source difference ID and target decision agrees |
| Inventories | A 65, B 57, C 51, packet C 44: **217** | Every source pointer/element ID occurs once in the inventory crosswalk and has reverse links to the 66 union elements |
| Actual C doubtful-reading table | **21 rows / 24 primary loci** | Source row and line identity retained; only original rows 1, 9, and 21 split into two primary loci |

The primary C loci have **7 resolved** and **17 retained** statuses. The additional right-exponent, accent, and final-glyph component entries remain separately identified children. They do not add original C source rows or primary local loci. The notation, slips, and abbreviation sections remain in their original categories.

All 96 decisions, all 66 union inventory elements, and all 27 remaining-doubt clusters have nonempty `root_page_sources`. Across them, all **218 source spans** have valid character offsets, matching line ranges, matching assembly-map pointers/group anchors, and containment within their declared component blocks. Decision `final_source_attachment` entries agree with their `root_page_sources`; remaining-doubt attachments agree with their decisions. Every union inventory element has `transcribed: yes`.

## Shared counting parents

- `015-H-DRAW` carries the single H drawing count. Its 20 linked local drawing children each carry zero H count.
- `015-H17` carries the single H lower-note `\ill{}` recovery count. Its five linked children—`015-D16`, `015-G10a`, `015-G10b`, `015-S-NOTE-SECOND`, and `015-G10-GROUP`—each carry zero H count.
- All C/H parent references resolve. No counted child duplicates its parent's witness count.
- The record's reported totals agree with its actual decision booleans: C 30 and H 49. This check verifies the record's supplied counting structure.

All 96 decision entries have a supplied root section and approved local choice. `pending_root_decision_ids` is empty. The main record's approval/write step remains explicitly pending root.

## Locator correction and closure

The original compact manifest gave C reader lines 164–173 for `final_cancelled_group_and_ending`, while the selected fragment begins at the `% CANCEL03` comment within line 164. Its initial fragment hash consequently described a substring of the covering line range.

The repaired `source_exact_locator` gives the unique start literal `% CANCEL03: full-scan origin (920,2238)`, its first character as the start boundary, and end of source file as the end boundary. Reading that exact fragment reproduces the recorded SHA-256 `6e60823a913a17b10fd94bcff92773dc2fe80a334a270c705175972878c683ce`. The covering-line semantics are now explicit. The TeX hash is unchanged.

Source brace/environment structure and the math delimiter contexts were reviewed. No compiler, renderer, OCR, external research, image opening, ink adjudication, installation, mathematical proof, or numerical geometry check was used. Only this audit file was written by the reviewer. The targeted pass stopped after the source coverage, parent ownership, exact attachments, selected components, wrapper syntax, and locator defect were checked.
