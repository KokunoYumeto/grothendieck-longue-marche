# Final mechanical preflight

**PASS — 2026-11-15 19:37:01 UTC.** This report supersedes the earlier mechanical QA report and its open wrapper/foliation flags.

## Final-byte coverage

All **39 current page files** have a successful syntax compilation result whose SHA-256 equals the current file bytes. The full pass compiled every page successfully. Scans 028 and 035 changed during that pass; their updated versions were then compiled successfully in a focused pass. The two runs used the same harness bytes.

The combined file is **78,521 bytes** and equals the exact ordered concatenation of scans 003–032 and 034–042. It was rebuilt after the final 028/035 edits.

The complete structural validator passed: expected filenames, scan markers, first cote marker, brace balance, forbidden-command check, exact concatenation, inventory header, inventory scan coverage, and every `transcribed=yes` value.

## Resolved inventory checks

- Inventory: **696 rows**, all eight required columns, no blank cells, and consecutive element identifiers within each scan.
- All seven allowed kinds are represented: text, display, diagram, drawing, margin note, insertion, deletion.
- Scan 007 now has its insertion wrapper. Scans 028 and 035 now have their drawing wrappers. The earlier per-page wrapper-presence flags are resolved.
- Matching foliation text-row candidates and numeric `mspage` markers are present for all 39 pages. Manuscript numbers are 2–31 and 33–41, matching scan minus one and the prescribed scan-033 omission.
- Final validator totals: **282 `unsure` commands; zero `illegible` commands**. Per-page counts are retained in the structural-validation log.

## Literal notation census for the primary reader

`records/notation_form_census.json` records observed spellings, occurrence counts, and scan/line references from the notation-review snapshot. Counts include commands inside uncertainty arguments. Every observed form is retained; this census makes no mathematical identity or correction claim.

| Literal argument | Observed wrappers and counts |
|---|---|
| GL | `\mathrm{GL}` 3; `\operatorname{GL}` 3 |
| Hom | `\mathrm{Hom}` 1; `\operatorname{Hom}` 13 |
| PGL | `\mathrm{PGL}` 3; `\operatorname{PGL}` 8 |
| Pic | `\mathrm{Pic}` 2; `\operatorname{Pic}` 7 |
| SL | `\mathrm{SL}` 1; `\operatorname{SL}` 8 |
| diag | `\mathrm{diag}` 1; `\operatorname{diag}` 1 |
| id | `\mathrm{id}` 10; `\operatorname{id}` 9 |

Other recorded spellings include `\phi` 43, `\varphi` 55, `\Phi` 4; `\psi` 17, `\Psi` 4; `\ne` 8 and `\neq` 6; `^*` 254, `^{*}` 1, and `_*` 166. The recurring uncertainty arguments include `k|\kappa` (48) and `\Gamma|\Pi` (15), with all locations in the census.

## Freeze-helper review

Read-only inspection at **2026-11-15 19:34:27 UTC** confirmed 39 unique done records, 39 unique audited records, an exact combined file, and 40 hash targets. No real freeze was run by this mechanical-support task.

`manage_transcription.py --freeze` requires the complete page set, exact concatenation, all required done/audited lines with valid timestamps, and an absent frozen manifest. It writes 40 manifest hashes and appends 40 ordered `sha256 RELATIVE_PATH HEX_DIGEST` lines to `progress.log`, followed immediately by the exact `transcription frozen TIMESTAMP` line.

Verification requires the current hashes, exact file coverage, concatenation, valid freeze timestamp, and the matching contiguous 40-line hash block immediately before the freeze line. `--verify` appends its unchanged-hashes UTC entry after successful checks; `--check` remains read-only. Ten synthetic checks passed for this script revision, including malformed/missing/reordered hash blocks and failed verification logging.

## Evidence and rerun commands

- `records/final_syntax_results.json`: all 39 current page hashes, their successful syntax status, and the combined hash.
- `/workspace/scratch/eef0fdbf69f3/mpl_text_ready_syntax/`: full syntax and final structural logs.
- `/workspace/scratch/eef0fdbf69f3/mpl_text_ready_syntax_028_035/`: updated 028/035 syntax logs.

```bash
python -B records/validate_structure.py .
python -B records/compile_syntax.py .
```

Page fragments were not edited by mechanical support. Source images and the context archive were not opened. This work assessed TeX syntax and file/inventory structure; the primary reader performed the visual audit.
