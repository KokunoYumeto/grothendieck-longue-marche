# Text-only audit — C123-01_123_scan019

## Scope and result

Compared `packets/C123-01_123_scan019/{C.tex,H.tex,C_questions.md}`, all three `out/readers/C123-01_123_scan019/R*/reading.tex` files and their reports, and the pending choices in `out/scripts/decide_p07.py`. This was an auxiliary textual audit, not a fourth reading. No images, OCR, other pages, web sources, TeX rendering, or mathematical proof checks were used.

The reports contain 43 difference rows for R1, 43 for R2, and 40 for R3. The pooled reports supply a locus for the substantive readings I found, subject to the accounting and representation issues below. No ordinary prose passage is missing from the complete readings.

## Accounting issues to retain in the final apparatus

1. **R2 omits a report locus for the diagram's terminal period.** R2's snippet retains C's standalone period after the two diagrams; H has no period. None of R2-01–R2-43 records that H omission. R1-D07 and R3-D08 cover the same source mark, so it is not missing from the pooled evidence.
2. **R1-D07 understates the change from C.** It has `c_changed=false`, although R1 moves C's post-diagram period beside the lower-right `Un_c`. R3-D08 explicitly identifies this as a placement change and has `c_changed=true`. Keep the final flag/count consistent with whether placement is counted.
3. **The condition's sequence differs from H.** H has the inserted replacement, then the live colon, then the struck original condition. All three complete readings put the struck original before the replacement and colon. The condition rows cover verb/index/semicolon differences, but do not explicitly describe this ordering difference. Expand an existing condition locus to state the placement treatment; another ink reading is not needed.
4. **The continuation hyphen uses two conventions.** R2-43 counts `der%` → `der-`; R1/R3 keep `der%` and explain the physical hyphen in comments/notes. Root has confirmed that the final apparatus will document the supplied joining convention and exclude this from substantive collation. Do not silently mix the two counting rules.

## Graphic representation and R3 inventory

R3's 41 inventory entries cover its broad prose blocks, two diagrams, source corrections, four insertion curves, underline, handwritten signs, marginal note, and archive number. That inventory is a useful base, but it cannot be copied unchanged for the combined final reading:

- Add or explicitly cross-reference the lower-arrow trace (R2-08), later `Dyn` n/o overlap (R2-15), separate cancellation cell after `les i` (R1-D19/R2-20), and separate cancellation cell after `point rationnel` (R1-D21).
- Give the final `invariante` letter's retained extra graphic trace an explicit inventory entry or cross-reference. R1 inventory item 34 lists it separately; R3's inventory only subsumes the word within its prose block.
- Update R3 inventory item 31, presently a **deletion**, when adopting R2's uncertain same-cell p/m overlap (R2-32). The resulting representation does not assert a deleted predecessor. Its inventory, notes, and remaining-doubts state must agree.
- R3-D37 describes a **fainter oblique trace above** the dark `paraboliques` connector, but the original R3 snippet draws only the dark stroke. R2-39 and R2's snippet retain both. Root reports that the pending script now adds the second stroke.
- R2-38 records handwritten `de` slightly raised above typed `classes`; the original R3 snippet puts them on one baseline. This already has a report locus. Root reports that the pending script now raises `de`.

Root has acknowledged the four added graphic elements and the final-e trace for the final inventory, and will change the p/m inventory state. These are reported dispositions, not claims that this audit inspected the eventual final output.

## Doubt review and structural checks

Every C question has a review in each reader, including both opening maps, all recurring low indices, the deleted group after `choisi`, the closing `Kostant` mark, `invariante`, the p/m cell, the marginal opening, the connector in `paraboliques`, and literal `de cette classe rationnel`. The duplicate connector question is explicitly recognized. The extra explicit C.tex doubts at the Deligne target and Lie-algebra glyph are also reviewed. The prior notes about invariance/injectivity, the marginal examples, the provisional characteristic-zero restriction, and the stabilizer question remain represented in the readers' notes; no mathematical assertion is treated as proved.

All three snippets pass a text-only balanced-brace and matched-`begin`/`end` check. This does not establish compilability or page layout. Differences consisting only of the stated macro normalization, ordinary spacing, H's editorial explanatory note, and archive-number convention were not promoted into additional source errors.



## Candidate reconciliation — current spec/preview

Checked the subsequently generated `C123-01_123_scan019_spec.json` and `C123-01_123_scan019_preview.tex` against the current pending script. The spec's replacement text exactly matches the preview; its old text exactly matches R3's complete reading. Preview SHA-256 at this check: `44502d16fa852af0ad08b918e858d58a351add27a87d921724bde3513b610b25`. The spec contains 40 base-locus overrides, seven added loci, and 49 inventory entries.

**Reconciled:** the inventory now includes the pale U trace, later Dyn overlap, both separate cancelling cells, final-e graphic, detached small-square point, live replacement colon, and diagram period. The p/m inventory entry is a drawing with no chronological state, consistent with the preview, C-doubt decision, remaining doubt, and R3-D30's explanation. The lower U trace and both connector strokes within `paraboliques` are present. Handwritten `de` is raised. R3-D08 records the period placement with `c_changed=true` and records R2's missing report row. R3-D14 explains the condition order and its exclusion from a separate error count. The final barred m agrees across preview, difference decision, inventory, abbreviation list, and notes. The `der%` convention and R2's isolated-page `der-` alternative are explicitly reconciled. The new `aue|aux` root reading is also recorded consistently in the preview, override, inventory, and remaining doubts.

**Three residual precision issues reported to root:**

1. `ROOT-02.final` says the extra cancellation x is a “TikZ text node,” inherited from R1. The actual preview uses two drawn strokes. The source mark is present; the description should simply say that the x is drawn.
2. `R3-D37.readers` copies abbreviated report descriptions. It should explicitly distinguish the actual one-stroke snippets of R1/R3 from R2's dark-plus-faint two-stroke snippet. The final choice and its evidence already describe both strokes, so this is an alternatives-description issue, not a missing locus.
3. The condition's final colon is described as raised and assigned to an unnamed hand in the inventory, while the preview leaves `:` outside the `handwritten`/`inserted` wrappers. R2 explicitly writes `handwritten{:}`, whereas R1/R3 leave it unwrapped. Record that hand/placement normalization or make the representation agree with the stated final state; no ink judgment was made here.

Apart from those identified description/representation points, no further unrecorded substantive reader divergence was found in this narrow reconciliation. The candidate still has balanced braces and matched environments in the text-only check. No script, spec, preview, source reading, report, or image was modified or inspected graphically.

Root subsequently accepted all three residual wording points: ROOT-02 will describe two drawn strokes; R3-D37 will distinguish the actual one-stroke R1/R3 snippets from R2's two strokes; and the colon wrapper difference will be stated as macro-only while its source medium/raised position remains in the inventory. These are apparatus wording dispositions and require no further image or ink review. This audit did not recheck the later regenerated files.
