# Read-only editorial consistency review — reader B

## Scope and method

Review completed: 2026-11-20 21:45:06 UTC.

This review covers the completed audits for scans 003 and 005–018 (018 added after its audit was applied), plus the shared assembly, audit, sealing and verification code. It is a documentation/code review, not another image reading. No image was reopened or recropped, no OCR or external research was used, and no TeX compilation was run. No edition, report, sealed reading or global file was changed; this report is the only file written by this review.

The findings below distinguish current factual mismatches from optional safeguards. Paths are relative to `edition/`. Historical raw reader reports and sealed first/second TSVs are evidence and should remain unchanged. Suggested synchronization concerns the current reviewed reports and generated apparatus, with a separate repair record where needed.

## Factual findings

### F1 — Duplicated formula and unmatched math delimiter on scan 017 — corrected by root

**Files/locus:** `pages/145_scan017.tex`, line 13; `second/145_scan017_adjudication.json`, the B11-related page edit; `scripts/review_second_017.py`, corresponding replacement.

**Observed problem, reported immediately:** The page originally contained:

```tex
$P$ \unsure{à|:} $\bar P=\sigma_iP$=\sigma_iP$
```

The suffix `=\sigma_iP` was duplicated and the page had **61 unescaped dollar signs**. The B11 adjudicated reading itself contained only `$\bar P=\sigma_iP$`; the extra copy was introduced by the `page_edits` replacement. This was a serialization error, not an unresolved manuscript reading.

**Resolution:** Root removed the duplicate from the page and adjudication replacement and recorded the repair in the progress log. The current page has **60 unescaped dollar signs** and a single expression at this locus. The combined transcription now contains that corrected page verbatim. `scripts/complete_audit.py`, line 23, now checks even unescaped-dollar parity before either the page or report is written. No correction was performed by this reviewer.

### F2 — Current unlisted-decision records retain superseded pre-audit alternatives

**Files/locus:** The following `reader_reports/145_scanNNN_reviewed.json` entries under `unlisted_decisions`; the generated “Decisions on C doubts absent from MARKS.tsv” sections of `SP75_C13_145_changes.md`.

| Scan / local ID | Current unlisted record | Audited page and current doubts record |
| --- | --- | --- |
| 009 / U009-01 | `\deleted{\unsure{u}}` | `\deleted{\unsure{u\|\tau}}` |
| 012 / U012-03 | `\unsure{par\|près}` | `\unsure{par\|près\|puis}` |
| 013 / U013-05 | `\deleted{\unsure{l_\infty^{-1}l_\infty}}` | `\deleted{\unsure{l_\infty^{-1}l_1\|l_\infty^{-1}l_\infty\|l_0^{-1}l_1}}` |
| 014 / U014-01 | `\unsure{\varepsilon_\infty\|\varepsilon_1}` | `\unsure{\varepsilon_\infty\|\varepsilon_0\|\varepsilon_1}` |
| 014 / U014-02 | `\unsure{2}` | `\unsure{2\|3}`, within the cancellation |
| 015 / U015-01 | `\deleted{\unsure{stable}}` | `\deleted{\unsure{stable\|stables}}` |

The second audits explicitly broaden these alternatives. Their `report_replace` sets do not update `unlisted_decisions` on these pages. `build_edition.py` lines 46–48 publishes the old records as current decisions, without identifying them as historical first-pass snapshots. Scan 013 is especially material: its preferred first reading changes from `l_\infty^{-1}l_\infty` to `l_\infty^{-1}l_1`.

**Suggested correction:** Synchronize each current unlisted decision's reading and ink explanation with its accepted audit decision, adding the second crop reference where appropriate. Preserve the original first-pass values in the already-retained historical reports/TSVs. Do not modify the sealed readings.

### F3 — Scan 011 change row s011-18 quotes a final state that no longer matches the page

**Files/locus:** `reader_reports/145_scan011_reviewed.json`, `changes[id=s011-18]`; the corresponding row in `SP75_C13_145_changes.md` and `SP75_C13_145_collation.tsv`; `pages/145_scan011.tex`, continuation after the group definition.

**Observed problem:** The row's `final` is still:

```tex
à valeurs dans $\hat{\mathbb Z}$, et une autre \inserted{$\gamma$} à valeurs
```

The audited page has the first `à` inside `\inserted{à}`, and the second as `\unsure{à|:}`. The audit notes and inventory correctly describe the first insertion, but the quoted “Final” field gives both signs as unqualified baseline text.

**Suggested correction:** Either update the complete final quotation or narrow it to the actual gamma-placement locus, with the second `\unsure{à|:}` retained. Avoid counting the first-à correction twice if it already has its own audit/change entry; this is synchronization of the final quotation, not authorization to alter the C/H change flags indiscriminately.

### F4 — Page-grounded notation and abbreviation tables were not synchronized after audits

**Files/locus:** `reader_reports/145_scanNNN_reviewed.json`, `notation` / `abbreviations`; generated `SP75_C13_145_doubts.md`, “Page-grounded notation observations” and “Abbreviations”.

The builder republishes these fields as current observations, while the second-audit replacements generally update notes and hand observations but not notation or abbreviations.

| Scan / field | Stale statement | Current audited state / suggested correction |
| --- | --- | --- |
| 005 notation | “Case is unresolved in the title and subscripted occurrence.” | The title `\hat\Pi=\hat\Pi_{0,3}` and indexed `\Pi_{0,3}` are resolved. Restrict the remaining case uncertainty to the genuinely unresolved unindexed forms. |
| 006 notation | Both small interlinear pi occurrences are described as case-uncertain. | The Teichmüller insertion is now `\Pi_{0,3}`; `sur \unsure{\pi\|\Pi} lui-\bar m` remains uncertain. Distinguish those occurrences. |
| 007 notation | “The indexed witness disagreement is left as a local doubt.” | The opening indexed form is now `\Pi_{0,3}`. Update the scoped observation. |
| 012 notation | “The π forms are retained as in both witnesses.” | All three relevant lower unindexed forms now carry `\unsure{\pi\|\Pi}`. State the retained local case doubt. |
| 013 notation | “Retained as pi locally.” | The three unindexed forms now carry `\unsure{\pi\|\Pi}`. Update the observation rather than implying a settled lowercase reading. |
| 011 abbreviations, definition label | Written form is `def`. | The current preferred label is `dfn`, with `def` retained as an alternative. Record that uncertain written form; the proposed expansion can remain “définition”. |
| 012 abbreviations, element | One `él\textsuperscript{t}` entry covers both the cancelled multiplication clause and a separate lower cancellation. | In the multiplication clause the audit reads baseline `élt`; the lower cancelled form remains raised and uncertain. Split the entries by actual form and locus. |
| 012 abbreviations, p.ex. | `p.ex.` is assigned to both the cancelled and uncancelled occurrences. | The live occurrence is now `p.ex)` with no stop after x; the cancelled occurrence retains `p.ex.`. Distinguish them in the written-form column. |
| 018 abbreviations, i.e. / p.ex. | The written forms are still `i.e.` and `p.ex.`. | B04 and B06 deliberately remove their terminal stops: the audited forms are `i.e` and `(p.ex)`. The notes already explain these omissions; synchronize the abbreviation forms. |

**Suggested correction:** Update these current observation fields from accepted audit outcomes, or explicitly label the older entries as first-pass observations superseded by the audit. The shared working notation table's global warning against mechanically changing all pi forms is appropriate and need not be removed.

### F5 — Explicit inventory quotations still retain earlier sign alternatives

**Files/locus:** `reader_reports/145_scan013_reviewed.json`, inventory E23 and E24; `reader_reports/145_scan014_reviewed.json`, inventory I15; `reader_reports/145_scan018_reviewed.json`, inventory I19, I21, I24 and I33; generated inventory CSV.

- Scan 013 E23/E24 quote the inserted-and-struck inverse prefix as literal `(=)`, while the audited page at line 44 has `\unsure{(=)|(\Rightarrow)}`.
- Scan 014 I15 quotes the crossed exponent only as `\unsure{2}`, while the audited page at line 43 and its current doubts record have `\unsure{2|3}`.
- Scan 018 I19 still has `\text{i.e.}`; the final page and B04 decision have `\text{i.e}`.
- Scan 018 I21 and I24 still have `(p.ex.)`; the final page and B06 decision have `(p.ex)`.
- Scan 018 I33 presents the terminal punctuation after the ornate group symbol as literal `),`; the final page, B09 decision and inventory I32 instead retain `\unsure{),|,}`.


**Suggested correction:** Keep the inventory entries and element IDs, but synchronize these explicit quoted signs with the final local uncertainty. No source rereading or new crop is required.

### F6 — Two H doubt flags transfer neighboring textual uncertainty to a structural locus

**Files/locus:** `reader_reports/145_scan014_reviewed.json`, changes s014-09 and s014-15; their generated collation rows; compare the rule in `H_doubt_metadata_review.json`.

- **s014-09**, “Vertical connector between the two cancelled formulas”, is marked `yes`. The quoted H reading has `\ill{}` only in the final epsilon subscript; it does not express doubt about the omitted connector. The same epsilon-index uncertainty already has its own locus, s014-08.
- **s014-15**, “Vertical separator at left of right-margin comment”, is marked `yes`. The quoted H uncertainty concerns the words of the comment (`déduisent`, `conjugaison`, `des autres`), not the omitted vertical separator. The lexical dispute has its own locus, s014-14.

The stored rule explicitly says that a doubt on a different sign in a larger quotation must not be transferred to the actual differing locus. These two rows conflict with that scope rule on the evidence quoted in the reviewed report.

**Suggested correction:** Set the structural rows to `marked_in_H=no` unless a separate H editorial statement explicitly doubts those structural marks; retain `yes` on the corresponding genuinely uncertain lexical/index loci. If such an external H uncertainty statement is relied upon, quote it in the metadata review so the current `yes` is auditable.

## Optional concerns and safeguards

### O1 — The builder protects existing box files, rather than the sealed first file itself

**File/locus:** `scripts/build_edition.py`, lines 76–80.

The current guard is `if not boxespath.exists():`, followed by writes to both `_boxes.tsv` and `_first.tsv`. Thus deleting or losing only a boxes file permits the builder to overwrite an existing, sealed first TSV from the current report. This review has found no actual first-reading corruption; the concern is a concrete unguarded code path.

**Suggested safeguard:** Check the first path and the sealing manifest independently. If a seal exists, refuse to write any first TSV. If a boxes file is missing, fail with an explicit recovery request rather than regenerate the first reading. The ordinary rebuild path already preserves both files correctly.

### O2 — Mixed-scope change rows make a binary H doubt flag imprecise

**Examples:** s003-03 bundles an unmarked missing exponent, underline/case, and a placement that H explicitly doubts; s016-09 bundles dotted indices, insertion placement, prose expansion and an illegible passage.

These rows are not automatically wrong: their broad locus includes some H uncertainty. However, a single `yes` can be mistaken for H having marked every corrected sign. Splitting semantically distinct loci, or adding a short flag-scope explanation, would make that distinction explicit. Counts already state that they are documented loci rather than error rates, which limits the consequence.

### O3 — Scan 018 raw-difference coverage explanations retain older interpretations

**File/locus:** `reader_reports/145_scan018_reviewed.json`, `diff_coverage` rows 45 and 50–52.

The linked change records and final page were correctly updated, but these explanatory strings still describe the earlier interpretation:

| Coverage row | Existing explanation | Current linked outcome |
| --- | --- | --- |
| 45 | “Enfin, not autres.” | s018-35 now prefers `outre`, retaining `enfin` and `entre`: `\unsure{outre\|enfin\|entre}`. |
| 50 | “En faisant dans les is readable.” | s018-39 now reads “Comme on voit en faisant dans ces relations”. |
| 51 | “Crowded final group clause remains tentative rather than omitted.” | s018-40 now reads a qualified conjugation clause, not a groupe clause. |
| 52 | “The final sigma-index/group reading remains uncertain; H's extra rho is not independently supported.” | s018-40 now preserves the whole uncertain formula `\rho\sigma_0\rho^{-1}=\sigma_1`, with a clear role for two rho factors. |

If `diff_coverage.explanation` is intended to be a historical first-pass rationale, label that role explicitly. If it describes current handling of each raw row, synchronize these strings with the accepted audit. This cleanup does not require another ink decision. The material lower-note change is already consistent across the page, M0832, s018-39/40, inventory I38 and the notes; the affine countermodel remains explicitly independent of the reading.

## Verification results

The final read-only validation covered **15 completed pages: 003 and 005–018**. It inspected no images and executed no edition-writing or TeX-compilation scripts.

- **All 24 sealed first-reading TSV hashes match** `second/FIRST_READINGS_SHA256.tsv`. Checking the seal hashes does not evaluate the still-provisional later pages as editions.
- Across the 15 completed pages, **266 prescribed boxes** have matching ordered coverage in the first and second TSVs, stored report boxes and crop manifests. Their coordinates agree. Referenced crops exist; every crop hash supplied in a manifest matches its file.
- All first, second and boxes TSV hashes match their **pre-comparison reading receipts**. Each audited second reader differs from the first reader and agrees with the recorded assignment.
- The reports' retained `second_boxes.reading` values still match the sealed first TSVs exactly. Current uncertainty corrections were not written back into those historical first readings.
- Independent tokenization reproduces **223 differing boxes**, of which **93** have the explicit adjudication flag `changed=true`. Comparison records, report audit entries and their first/second/final strings agree; none is pending.
- **614 raw-difference coverage entries** are sequential and unique within their reports. Every single or list-valued `change_id` resolves to a current change entry. No duplicate change, inventory, listed-decision or unlisted-decision IDs were found within these pages.
- **325 H-change collation rows** match their reviewed-report source fields (`H`, `C`, `final`, `marked_in_H`, and locus). **74 listed decision rows** match `decisions.tsv` for decision, reading and confidence. This confirms faithful propagation; it does not cure the stale source fields or H-scope issues identified above.
- After root's scan017 repair, all 15 pages have even unescaped-dollar counts, balanced grouping braces and paired LaTeX environments in the non-compiling structural check. Every completed page occurs verbatim in the current combined transcription.

These checks establish file and record consistency for the stated snapshot. They are not an image-based endorsement of any new reading, a compilation result, or an independent reproof of the mathematical notes. Pages 019–027 are outside this final-content review. Only this review file was written by reader B during this assignment.
