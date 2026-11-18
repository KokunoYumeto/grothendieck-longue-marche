# Final prefreeze mechanical validation

Final check: 2026-11-18 01:08:08 UTC, after the root corrected the six missing math wrappers and rebuilt the doubts table. This report supersedes the earlier snapshot of this same report.

Scope: saved page files, inventory, source doubts TSV, rendered doubts Markdown and progress events. No images, context-archive contents, mathematical interpretation, transcription edits, or further compilation attempts were involved.

## Outcome

**PASS: 0 actionable mechanical issue(s) detected.**

- **42/42** expected page files, scans 092–134 excluding 125; correct opening cote/scan marker and one matching scan marker per page.
- **42 done** and **42 audited** progress events, both in the expected order.
- **1,191 inventory rows**, all 42 scans covered, every `transcribed` value exactly `yes`. Required headers, column counts, element kinds, sheet kinds, required fields, per-page sheet-kind consistency and per-page identifier uniqueness pass.
- Sheet kinds by page: text: **42**.
- Inventory element counts: deletion: 256, diagram: 14, display: 308, drawing: 2, insertion: 159, margin note: 44, text: 408.
- **291 source doubt rows**, **291 rendered Markdown doubt rows**, with matching confidence distributions: high **8**, medium **88**, low **195**. All values are allowed and all rows have the required six columns.
- **447 `\unsure`** and **1 `\illegible`** occurrences in page files, excluding comments. `\illegible{2}` at scan 117, line 13, remains in prose outside math and diagrams.

## Syntax and annotation checks

- No unknown control sequence outside the inspected LaTeX/AMS/TikZ/TikZ-CD and allowed annotation command sets was detected. The command lexer consumes `\\` correctly; letters following a row break are not mistaken for command names.
- Unescaped braces and environments are balanced. Explicit math delimiters balance without crossing brace-group boundaries, ending mid-page-state, or containing blank paragraphs within inline math.
- No math-only commands, subscripts or superscripts remain outside recognized math contexts; no misplaced alignment tabs, unescaped parameter characters, or empty state-macro arguments were detected. Text-compatible `\quad`, `\qquad` and `\ldots` are accepted.
- No image/external inclusion, preamble commands, literal `[...]`/`[…]`, TODO or PLACEHOLDER marker was detected.
- The six earlier bare mathematical fragments in deletion/doubt markup at scans 112:18, 113:12, 113:17, 121:17, 124:24 and 129:7 now have math wrapping. The Markdown/source-TSV row-count discrepancy is also resolved.

## Actionable findings

| File | Line | Finding |
| --- | ---: | --- |
| — | — | None detected in this final snapshot. |

## Font-encoding variants for the root’s ink comparison

These are occurrences of the same Latin glyph under different font commands, not assertions that the objects or source glyphs are identical. They are recorded for the root’s visual comparison, and are not grounds for further automatic normalization.

| Glyph | Font command | Count | Representative scan:line locations |
| --- | --- | ---: | --- |
| `C` | `\mathbb` | 127 | 110:3, 110:6, 110:7, 110:8, 110:10, 110:14, 110:16, 111:3, 111:5, 111:7 |
| `C` | `\mathcal` | 2 | 118:40, 134:7 |
| `H` | `\mathcal` | 36 | 092:12, 092:14, 092:18, 092:20, 092:22, 094:24, 094:30, 095:25, 095:27, 096:5 |
| `H` | `\mathrm` | 2 | 127:9 |
| `P` | `\mathbb` | 48 | 097:71, 099:5, 101:8, 108:7, 109:41, 109:42, 109:43, 109:45, 110:3, 110:8 |
| `P` | `\mathcal` | 37 | 109:12, 117:35, 117:45, 118:3, 118:7, 118:9, 118:11, 118:18, 118:20, 118:28 |

At this snapshot no letter occurs under both `\mathbf` and `\mathbb`. Remaining multiple-font glyphs are script versus double-struck `C` and `P`, and script versus upright `H`; these may represent distinct objects. The source-reading decisions belong to the root’s notation reconciliation.

## Limits and concurrency

- Coverage checks establish the existence and asserted status of rows, not that every visible source element was captured or read accurately.
- This is static/lexical validation. No LaTeX compile was retried; the prior report documents the unavailable formats and packages, so compiler-level validation remains unavailable.
- The combined fragment and frozen hashes were not required during the initial prefreeze pass; the read-only verification below now covers both.
- Files detected changing during this final snapshot check: none. Subsequent edits can supersede counts and line references.

## Read-only verification after freeze

Verified 2026-11-18 01:08:32 UTC, after the root’s recorded freeze at 2026-11-18 01:07:16 UTC. All seven earlier findings (six missing math wrappers and the stale doubts-table projection) were already resolved in the final snapshot above.

The package validator passes with `documentation/frozen.sha256`: the combined fragment is the exact ordered byte concatenation of the 42 page files; the inventory has 1,191 rows covering all 42 scans; and all **43 SHA-256 entries** (42 pages plus the combined fragment) match. An additional direct SHA-256 comparison against every manifest entry also found no changed hash. No transcription file was modified during this verification.
