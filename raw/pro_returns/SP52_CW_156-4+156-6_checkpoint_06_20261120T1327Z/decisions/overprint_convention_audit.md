# Focused overprint-convention audit: scans 065–071

Text-only candidate audit. No images were opened, no compilation was run, and no page or decision record was changed. Checked the seven decision JSONs, original C source quotes, corresponding final page files, and the consolidated transcription. Root retains all manuscript judgments.

Convention 4 explicitly represents an overwritten old form as `\deleted{old}` immediately before its live replacement. Consequently, `\deleted{old}live` does not itself assert separate manuscript positions. A one-position observation cannot alone disprove that C encoding.

## Three evidence-wording candidates

All three rows below have `change_c: true`, but **each also changes actual letter/deletion alternatives**. None can be discarded as a purely formatting change from this text-only audit. The risk is that the quoted spatial argument overstates what C asserts; root should distinguish any supported reading change from that argument.

### Scan 065 — 156-4_065-D017: interlinear note, crowded validité

- Record: `SP52_work/decisions/156-4_065.json`, row D017, `scan_shows` at line 289; repeated in dispute evidence at line 936 and remaining-doubt reasoning at line 1069.
- Exact C: `\deleted{\unsure{déd|val}} \unsure{validité|déduction}`. Confirmed in original C page line 8 (`source/SP52_CW_156-4+156-6_witnesses/codex/J156-4-08/pages/J156-4-08_156-4_scan065.tex`).
- Final: `\unsure{validité|\deleted{val}idité}`. Final page line 8; consolidated `.tex` line 10.
- Candidate phrase: “There is no separate old word followed by a second complete validité.” C's old/live sequence is permitted for overprinting, so it does not by itself claim those two positions.
- Actual reading change: removes the deleted `déd` candidate and live `déduction` candidate; admits an entirely live `validité` or cancellation of its `val` prefix. This is substantive, not merely joining two printed positions. Whether the ink supports that change is outside this audit.

### Scan 068 — R1-D048: revised anti compound

- Record: `SP52_work/decisions/156-4_068.json`, row R1-D048, `scan_shows` at line 955; repeated at lines 1329, 1345, 1720, 1736 and in dispute evidence at line 2320.
- Exact C: `anti\deleted{\unsure{isomorph|homéo}}\unsure{involution|bijection|dualité}`. Confirmed in original C page line 11 (`source/SP52_CW_156-4+156-6_witnesses/codex/J156-4-09/pages/J156-4-09_156-4_scan068.tex`).
- Final: `anti\unsure{\deleted{invo}lution|involution|bijection|dualité}`. Final page line 27; consolidated `.tex` line 202.
- Candidate phrase: “The ink does not independently establish two complete successive words isomorph/homéo and involution.” The source contains no inter-word space at this point, and its deleted/live sequence can represent overwritten layers at one position.
- Actual reading change: removes both proposed older forms `isomorph`/`homéo`, substitutes possible partial cancellation of `invo`, and permits no independently deleted layer. The count could rest on those changed readings; “two successive words” cannot alone justify it.

### Scan 070 — A-070-D027: dense d'une group and repetition

- Record: `SP52_work/decisions/156-4_070.json`, row A-070-D027, `scan_shows` at line 561; repeated at lines 1294, 1312, 1870, 1879 and dispute evidence at line 2003.
- Exact C: `\deleted{\unsure{d'un}} \unsure{d'une =|d'un =}`. Confirmed in original C page line 14 (`source/SP52_CW_156-4+156-6_witnesses/codex/J156-4-09/pages/J156-4-09_156-4_scan070.tex`).
- Final: `\unsure{d'|\deleted{d'}}\unsure{une|un} $=$`. Final page line 30; consolidated `.tex` line 299.
- Candidate phrases: “no second complete d’un or d’une-sized group is visible” and “not two sequential whole words.” Those are not positions necessarily asserted by C under convention 4.
- Actual reading change: replaces the proposed older complete `d'un` layer with uncertainty about cancellation of only the `d'` prefix; maintains `une`/`un` alternatives and resolves the literal equals sign. These are reading/state decisions, not just presentation.

## Scan 071: mixed substantive and formatting components

- **071-D26, inverted folio** (`156-4_071.json`, line 1050; dispute evidence line 2889): original C page line 19 is `\mspage{\deleted{\unsure{5\deleted{\unsure{4|3}}5}}}`; final page line 64 / consolidated line 385 is `\mspage{5\rlap{\deleted{\unsure{4|3}}}5}`. C already permits the inner deleted `4|3` to be an older layer beneath the second live 5; the `\rlap` change is formatting. However, removal of the outer folio deletion and outer uncertainty is substantive. “Only two positions exist” does not independently refute C. This is a wording/scope candidate, not a demonstrated spurious whole-row count.
- **071-D27, worked Phi**: C is `\deleted{\unsure{\mathcal F|F}}\Phi` (original page line 21); final page line 70 / consolidated line 391 adds alternatives including retraced `\Phi` alone and uses `\rlap{\ensuremath{...}}`. Same-position placement is formatting under convention 4; admitting no earlier F layer is a substantive uncertainty change. The current evidence does explicitly say that a complete prior F cannot be separated from retracing, so it is not solely a position argument.

## Math-mode `\rlap` result

**No remaining `\rlap` group containing `\mathcal` or `\mathscr` without explicit inner math was found in the final scan065–071 page files or consolidated `.tex`.** The only such final group is the scan071 Phi alternative at page line 70 / consolidated line 391, and it uses `\rlap{\ensuremath{\deleted{\mathcal F}}}`. The other final `\rlap` is the text-mode folio digit. Decision-record final strings agree. Original C's scan070 relation overlay also already uses `\ensuremath`.

No candidate of the requested sequence-convention kind was identified on scans 066, 067 or 069. No purely formatting-only counted row was established by this audit.


## Administrative clarification applied — 2026-11-20T12:50:04+00:00

Root authorized a wording-only correction after this candidate audit. The retained script `scripts/review_overprint_record_wording.py` corrected the related evidence, dispute, doubt, consequence and summary copies for scan065 D017, scan068 D048 and scan070 D027; added explicit formatting/substantive scope notes for scan071 D26/D27 and their doubt/dispute copies; and corrected the folio dispute's positional rationale. The scan065 live-word doubt location was renamed to remove its misleading 'following complete word' description. A dated clarification was appended to `brief_changes.md`; the original history paragraph and historical brief files were retained.

The exact before/after text of every changed JSON leaf is retained in `overprint_record_wording_changes.json`, together with the precise history append and protected-file SHA-256 values. All other JSON leaves were compared and left unchanged. Seven final page files, their seven C source pages, the consolidated transcription and eight historical brief files were hashed before and after and remained byte-identical. No images, compilation, build, finalization or new manuscript judgment occurred.
