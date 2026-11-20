# Mechanical bookkeeping repair

Applied 2026-11-20 15:36:16 UTC.

No image was opened, no reading was decided, and no mathematical assertion was checked by this script. The page transcription changed only at the two documented scan023 TeX command boundaries. All confidence levels and error categories were retained. The upper scan007 link receives diff_C=no because the original grouped row already states that C and the final upper link are identical; the C difference remains on the lower link.

## Operations

- 71-007-007 -> 71-007-007a, 71-007-007b, 71-007-007c, 71-007-007d, 71-007-007e, 71-007-007f
- 71-007-011 -> 71-007-011a, 71-007-011b
- 71-017-024 -> 71-017-024a, 71-017-024b
- 71-021-011: exclude separately counted annotation material
- 71-021-014: exclude separately counted annotation material
- 71-021-015: exclude separately counted annotation material
- 71-021-017: exclude separately counted annotation material
- 71-021-018 -> 71-021-018a, 71-021-018b, 71-021-018c
- 71-022-001 -> 71-022-001a, 71-022-001b
- 71-023-017 -> 71-023-017a, 71-023-017b, 71-023-017c, 71-023-017d, 71-023-017e
- inventory 023-27 -> 023-27a, 023-27b
- inventory 023-36 -> 023-36a, 023-36b, 023-36c, 023-36d, 023-36e
- Scan023 page: separate cup/V and subset/D control-word boundaries only
- read023.py: normalize those two command boundaries immediately before saving

The arrow and attached Sigma in 71-007-013 remain one cancelled diagram fragment. No new difference was introduced there.

ID_REDIRECTS.tsv maps retired grouped IDs to their suffix IDs. Aggregate files were rebuilt from the repaired records. If an original readNNN.py is later rerun, rerun this repair script before final validation; the script will refuse unreviewed changes to its original target rows. The scan023 spacing safeguard is installed in read023.py itself.

## Additional authorized scan007 syntax repair

Applied 2026-11-20 15:37:14 UTC. The primary reader additionally authorized `\partialX_i` → `\partial X_i` in scan007 and a matching normalization immediately before its read007.py save call. This changes only the TeX control-word boundary, adds no reading-difference row, and leaves every glyph decision intact. File digests are appended to MECHANICAL_REPAIRS.tsv.

## Additional authorized scan017 syntax repair

Applied 2026-11-20 15:53:59 UTC. The primary reader authorized `U\subsetC` → `U\subset C` and the corresponding normalization immediately before the read017.py save call. Only the TeX control-word boundary changes; no reading-difference row is added. File hashes are in MECHANICAL_REPAIRS.tsv.

## Authorized scan032 comparison-scope repair

Applied 2026-11-20 16:07:32 UTC. In 71-032-020, only C/H/final set-name glyph references were replaced by `[set-name glyph separately collated: 71-032-001]`. All other fields, witness flags, categories, confidence and count scope remain unchanged. Matching metadata literals in read032.py were updated to preserve the fix on regeneration. No page text or ink reading changed.

## Authorized scan033 syntax repair

Applied 2026-11-20 16:08:44 UTC. `\inA.` was separated as `\in A.` in the page, and a matching read033.py normalization was installed before its omission-block extraction so future page and comparison fragments use the separated command. No reading-change row was added. Existing comparison-cell revisions remain proposals pending review.

## Authorized scan010 and scan013 count-scope repairs

Applied 2026-11-20 16:13:39 UTC. Row 71-010-033 now compares only the initial doubtful `de/sur` with H's `ill`; the unchanged final B/B-prime doubt remains in the doubts record. Its flags, category, and confidence are unchanged. Row 71-013-007 is split into 71-013-007a (vertical equality) and 71-013-007b (separate oblique link), allocating the existing comparison and evidence to their respective physical places. Both inherit C=no, H=yes, category, and confidence. ID_REDIRECTS.tsv preserves the original ID. Matching read010.py and read013.py metadata safeguards retain these decisions and all later IDs on regeneration. No page text changed; H and distinct-place counts each increase by one, while C is unchanged.

The separately approved 23 final-cell replacements were applied unchanged by apply_exact_fragment_replacements.py; source and original-row hash guards passed. Their application hashes are recorded in metadata/exact_fragment_applications.tsv. No image reading or mathematical checking was performed.

## Authorized scan033 exact comparisons and H glyph omissions

Applied 2026-11-20 16:17:39 UTC. The eight approved broad-block comparisons
71-033-012 through 019 now use the reviewed exact C/final fragments and
exclusions. Their final evidence removes the proposed-clarification label and
the obsolete C-only wording. The three excluded glyph rows 71-033-001 through
003 now have diff_H=yes and kind=omission, retaining diff_C=yes,
error_kind=Symbols and indices, confidence, and all reading/evidence cells.
This adds three H comparisons, with C and distinct-place totals unchanged.

The proposal TSV and all recorded source hashes are preserved unchanged.
metadata/scan033_comparison_applications.tsv records original and applied row
hashes and changed fields. apply_scan033_comparisons.py provides an idempotent,
guarded application and the in-memory regeneration step now called by
read033.py; changed page text or protected row fields require renewed review.
Redirect metadata is unchanged. All page and consolidated-transcription bytes
remain unchanged, and validation reports 25 pages, zero errors, zero warnings.

## Authorized scan023 inserted-sentence comparison

Applied 2026-11-20 16:24:09 UTC. Only the final cell of 71-023-011 was replaced by the exact already-consolidated insertion fragment, preserving both underlines and the final `.)` / `).` uncertainty. The corresponding literal in read023.py now supplies that same fragment on regeneration. All other row fields, counts, and page text are unchanged. No new ink decision was made.

## Approved original-C comparison fragments

Applied 2026-11-20 16:34:54 UTC. The primary reader reviewed and approved all 48 C-cell replacements unchanged, identifying proposal SHA256 `4b928bf81cbd0cea2562b37dc07f86d6764ce3b964dfd1519e670dbb32c40caf`. The guarded application verified the original source hashes, complete current-row hashes, and current final-cell hashes before changing C alone. The immutable proposal and approval/application ledger are in metadata/original_C_fragment_replacements_proposed.tsv and metadata/original_C_fragment_applications.tsv.

All flags, scopes, IDs, confidence levels and other fields remain unchanged. Counts remain C=72, H=499, distinct places=516, inventory rows=549 and check events=28. Aggregates were rebuilt exactly once. All 26 frozen transcription files remained byte-for-byte unchanged; package.py verify passed after the rebuild. Complete/audit structural validation reported zero errors and zero warnings. No first-reading script was rerun, and no page-done/audit event was added.
