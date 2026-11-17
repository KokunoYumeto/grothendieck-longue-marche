## Applied reconciliation

Applied 2026-11-17 23:04:29 UTC. Root approved all changes, confirmed scan036 placement, and supplied the final scan040 oval/tail. The operative inventory now contains **779 rows**, and the regenerated coverage file maps **all 446 current state macros**. Twelve rows were updated and thirty added. Noncontiguous split spans were placed around their intervening insertions in source order; scan032’s oval is attached to its second paragraph. The insertion row055-20 was moved before the final fini/des deletions to follow the current TeX. No page file or progress.log was changed. A before-application CSV is retained for the audit trail.

The earlier proposal snapshot below records the initial 41-change review; the final proposal CSV additionally includes the scan040 drawing.

# Mechanical inventory reconciliation

Snapshot: 2026-11-17 23:00:25 UTC. This review uses the current TeX fragments and existing CSV only. It does not read scan images or context, reconsider handwriting, or certify image-to-text completeness. Page files, the operative inventory, and progress.log have not been changed by this reconciliation.

## Deliverables

- `inventory_reconciliation_proposed.csv`: 12 proposed row updates and 29 proposed new rows. This is a change list, not a replacement inventory. `anchor` indicates the suggested insertion location; rows with the same anchor retain source-macro order.
- `inventory_state_macro_coverage.csv`: a source locator and proposed inventory mapping for each of all 445 occurrences of `deleted`, `inserted`, `margin`, `diagram`, and `figure` in the current fragments.

The existing inventory has 749 rows. Applying all proposed additions without removing other rows yields **778 rows**. Every existing state-kind row has a source counterpart; none is proposed for removal. All 445 current state macros have at least one specific existing or proposed row. This is a structural assertion about the TeX, not a claim about completeness against the manuscript.

## Specific additions

| Scan | New rows | Reason |
|---|---:|---|
| 024 | 2 | Newly added polygon around the L/J diagram and marginal bubble. |
| 025 | 2 | Newly added curved marginal-diagram enclosure and bubble around `sép. clos suffit!`. |
| 026 | 1 | Separate final deletion `toute`. |
| 027 | 5 | Separate noncontiguous deleted/inserted spans formerly grouped in four rows. |
| 032 | 1 | Newly added oval around `reduced geometric fibers`. Suggested anchor: after `032-06`. |
| 034 | 2 | Separate insertion `et` and deletion `App` from noncontiguous grouped spans. |
| 036 | 3 | Split three separated deletions into individual entries, and add the previously unlisted drawing. |
| 037 | 1 | Make the outer margin wrapper of the cancelled dimension drawing explicit. The drawing and cancellation already have rows; this is metadata granularity, not missing drawing content. |
| 041 | 8 | Seven individually marked nested deletions in the large cancellation, plus the deletion wrapper around the cancelled diagram. |
| 044 | 1 | Separate deleted `\otimes_T` and `\subset X`, which have live `Z` between them. |
| 045 | 1 | Newly added callout bubble. |
| 048 | 1 | Separate `On peut supposer` and `$S$ affine, dans le cas`, which have an insertion between them. |
| 055 | 1 | Newly added final deletion `des`. |

The scan 041 nested additions are `on a`, `hom`, `homomorphismes`, `$S,S'$`, `$S\longrightarrow T$`, `section`, and `des ouverts`, all retaining the uncertainty marks used in the fragment. The existing large-cancellation row does not individually locate these nested states. The final eighth addition records the deletion surrounding the diagram already represented by `041-18`.

## Updates and grouping decisions

`021-10` changes from **insertion** to **deletion**, with the current locator `\unsure{de|$\Rightarrow$}`.

Nine formerly grouped rows are restricted to their first span, with separate proposed rows for the later noncontiguous spans: `027-04`, `027-05`, `027-12`, `027-18`, `034-07`, `034-19`, `036-04`, `044-29`, and `048-15`. This decision is based on literal intervening live text or insertion macros in the TeX.

Three grouped deletion rows remain intact because their component deletion macros are immediately adjacent apart from whitespace, and the row already records the parts: `027-16` (the long cancelled marginal note followed by `??`), `040-22` (`affine`, `relatif`), and `044-16` (`Les`, `autres assertions`).

Two locator updates follow changed current-source wording without altering the transcription: `044-18` now locates `que le $=$ visé ...`, and `042-10` locates `$T\longrightarrow S$ est \unsure{géom. injectif|purement injectif}`, replacing the stale `univ. injectif` caption.

The enclosing margin macro on scan 025 is already represented by the two specific note rows `025-03` and `025-04`; its nested diagram has its own row. The cancelled list on scan 042 is represented by `042-09`, `042-10`, and `042-11`, which identify its distinct subparts. These are intentional multiple-row mappings to one outer macro.

## Application notes

New row identifiers use `NNN-RNN` and do not collide with existing element identifiers. Preserve the standard inventory columns when merging; the proposal-only columns `action`, `anchor`, `source_macro_ids`, `tex_lines`, and `reason` belong to this review file, not to the operative CSV. New drawing placement descriptions incorporate the root reader's completed visual-audit report; approximate TeX line references remain available in the proposal.

The proposed CSV and coverage CSV were generated after the six added enclosure figures and the final scan 055 deletion were present. Later source edits would require another mechanical pass before these mappings are treated as current.

## Syntax scope

The approved custom state commands remain those specified by the task. `\textcircled` is ordinary LaTeX and has been added to the validator's standard-command recognition list. No TeX dependencies have been installed. Existing engine binaries lack discoverable LaTeX formats, basic classes, and TikZ packages, so structural checks cannot be promoted to a successful compilation claim.
