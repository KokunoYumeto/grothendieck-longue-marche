# Mechanical support report

Recorded: 2026-11-17 00:26:14 UTC

## Scope and current results

These checks inspect source syntax and package structure only. They do not inspect images, open either source archive, interpret manuscript content, certify readings, or establish visual completeness.

- Frozen-integrity and structural recheck at **2026-11-16 23:52:20 UTC** passed. All **47 files** in `frozen_sha256.json` (46 page fragments plus the combined transcription) matched their frozen SHA-256 values and the 47 hash records in `progress.log`. The manifest itself remained unchanged.
- All **46 expected pages** are present, and the combined transcription equals their ordered bytes. The inventory contains **1,177 rows, all marked yes**. The doubt register has **449 rows for 449 doubt macros**.
- The requested inventory correction is reflected: **scan 029 has 11 deletion rows for 11 deletion macros**, and **scan 031 has 14 deletion rows for 14 deletion macros**. The comparator treats the 11 pure visual margin wrappers under the drawing/diagram kinds of their contents.
- Timing checks are consistent: all first-pass completions precede the 46 second-audit records; every audit precedes the freeze; the manifest and log agree on **23:40:30 UTC** as the freeze time; context opening is logged afterward at **23:40:37 UTC**. Recorded source corrections and file modification times precede the freeze to the recorded second.
- The full pdfLaTeX run at **23:39:04–23:39:23 UTC** passed all 46 fragments. Their checked hashes match the frozen current pages, so no repeat compilation was needed.
- The research dossier subsequently received the generated-file structural review below. Mathematical content remains under the root agent's review; no original context or image was opened by these checks.

Machine-readable evidence: `frozen_integrity_check.json`, `mechanical_validation.json`, `latex_syntax_check.json`, and `macro_inventory_counts.json`. The earlier `latex_syntax_recheck_002.json` is retained as a historical record. These reports identify their checked versions and times; future changes to supporting files require their final package check.

## Research dossier structure

The generated dossier was mechanically reviewed at **2026-11-17 00:20:51 UTC**, then its current metadata, Markdown, and file hashes were refreshed at **2026-11-17 00:26:14 UTC** after the bibliography rebuild. The refresh passed. No original manuscript image or context file was opened; no transcription source inspection or recompilation was performed in this refresh.

- There remain **101 unique items: 94 N-items, including N071b, and 7 T-items**, with 101 matching rendered headings and 172 source locations. All 16 own-idea items retain confidence and reason fields.
- Query coverage remains 101 item records, 26 selected-register records, and 255 individual searches. Each selected register ID has a query record and a disposition; 22 entries carry 128 valid item links, and four are explicitly recorded without item links.
- All 37 primary-reference occurrences resolve to the 15 defined sources. The rebuilt notes now contain **37 valid internal anchor links and 16 structurally valid external URL links** (53 links in total), reflecting the added Tag 0A3K link. External URL reachability was not tested.
- All three Markdown tables retain consistent column counts across 90 body rows. No structural issue was found in the updated notes or metadata.
- The notes and all watched metadata hashes remained stable during this refresh. `research_structure_check.json` records their current hashes and identifies the files changed by the rebuild. Frozen-transcription byte verification and source-line upper bounds retain the prior full-review time of **00:20:51 UTC**; the frozen manifest itself is unchanged.
- No supplied archive, image, PDF, or prompt attachment is under the work directory. Keep the two existing Python cache files excluded by the final packaging filter.

Evidence: `records/research_structure_check.json`. Only that mechanical report and this report were updated. Notes, transcription, inventory, and progress-log content were not edited.

## Reproduce the checks

From the package directory:

```bash
python scripts/validate_package.py --phase checkpoint
python scripts/check_fragments.py
```

For selected scans:

```bash
python scripts/check_fragments.py 22 28 29 30 31
```

The TeX checker requires `pdflatex`, `kpsewhich`, and the article, AMS, mathrsfs, TikZ/tikz-cd, font/input encoding, and geometry resources. It derives the package path from the script location. It checks the normal resource lookup first; when an installed TeX tree lacks a working filename database, it uses the resource tree reported by `kpsewhich`. An explicit `--texmf-root PATH` is also supported.

Compiler products stay outside the package: an existing sibling `_latex_check` directory is reused; otherwise a system temporary cache is selected. `--cache-dir PATH` selects another external directory. Rebuild the cached format with:

```bash
python scripts/check_fragments.py --rebuild-format
```

No format binaries, PDFs, auxiliary files, or temporary compiler wrappers are included in the package. The copied Python script regenerates its wrappers and local format. Its long state-macro definitions accept paragraphs and nested text/math; diagram arguments are retokenized for TikZ matrix ampersands. These definitions serve parsing checks, without attempting the final appearance of editorial marks.

## Optional doubt-register inputs

`save_page.py` now reads an optional `records/doubt_confidence.json` object. Each key is:

```text
NNN:L<fragmentline>:<full macro argument>
```

The three-digit scan and original fragment line identify the occurrence; the complete argument retains its LaTeX, vertical-bar alternative, and any internal whitespace. Values are `high`, `medium`, or `low`. The default remains `medium` for `unsure` and `low` for `illegible`. An absent override file preserves those defaults.

An optional `records/legibility.md` supplies the final text beneath the existing “Legibility and limits” heading. An absent or empty file preserves the current provisional paragraph. The support edits did not call `rebuild()`, alter any page fragment or inventory row, or change any progress-log timestamp.
