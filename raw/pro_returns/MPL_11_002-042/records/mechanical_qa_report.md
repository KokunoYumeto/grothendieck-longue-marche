> Historical snapshot. Superseded by `final_preflight_report.md`: all current page bytes pass syntax and structural checks; the earlier wrapper, foliation, and compilation flags are resolved.

# Mechanical QA report

Structural snapshot: **2026-11-15 19:15:21 UTC**. Full syntax pass completed: **2026-11-15 19:15:29 UTC**. This report records the checked versions while the primary reader continues the visual audit.

## Syntax compilation

**37 of 39 page snapshots compiled successfully** with the supplied syntax-only harness. Two page diagnostics remain for the primary reader's source-preserving correction:

| Scan | Fragment line | Compiler diagnostic |
|---|---:|---|
| 036 | 12 | `Missing $ inserted`; math syntax occurs inside nested `deleted` / `unsure` wrappers without a math delimiter. |
| 039 | 40 | TikZ refers to missing matrix cell `tikz@f@1-4-1` (row 4, column 1). The error is reported at the diagram's end. |

Scan 021 changed during the full pass. A focused compile of its updated version passed at **2026-11-15 19:16:17 UTC**, with its source hash unchanged during that focused check.

The harness supplies the prescribed editorial macros and uses identity wrappers. Editorial groups and diagram bodies stay in the TeX input stream so nested `tikz-cd` matrices can establish their ampersand category before tokenization. This resolved the harness-only errors from the initial passes, including scan 027.

The installed pdfTeX engine and existing AMS/TikZ packages were used with a process-local `TEXMF` search path and a temporary format. Compilation used `-draftmode`, disabled shell escape, and stopped at the first error on each page. No final PDF was produced. TeX drivers, copied page snapshots, formats, compiler logs, and JSON results remain outside the deliverable.

## Structure and inventory

- All **39 expected fragments** are present: scans 003–032 and 034–042.
- Every fragment has its expected `scanpage`; the first has `cotefile{11}`. There are 39 `mspage` markers. Their numeric values equal scan minus one: 2–31 and 33–41, corresponding to the prescribed omission of scan 033.
- Basic brace balance passed. No `documentclass` or `includegraphics` command was found in a fragment.
- The inventory has **691 rows**, the exact eight required columns, every expected scan, no blank cells, and `transcribed=yes` throughout. Element identifiers are consecutive from 1 within every scan.
- Its seven kinds exactly match the allowed vocabulary: text, display, diagram, drawing, margin note, insertion, deletion.
- Uncertainty-command counts at the structural snapshot: **273 `unsure`**, **0 `illegible`**. The validator prints the per-page counts.
- The structural validator's sole failure is the combined transcription, which has not yet been built. No frozen manifest was present.

### Inventory review flags

These checks compare wrapper presence with inventory metadata; they do not establish source fidelity.

| Scan | Mechanical observation |
|---|---|
| 007 | An insertion inventory row exists, but no `inserted` macro occurs. |
| 028 | A drawing inventory row exists, but no `figure` macro occurs. |
| 035 | A drawing inventory row exists, but no `figure` macro occurs. |
| 038–042 | No distinct foliation `text` row was identified by the numeric-only or explicit-foliation-label check. The corresponding numeric `mspage` marker is present on each page. |

Distinct foliation-row candidates matching the numeric `mspage` were identified on the other 34 pages. Numbering or emphasis does not require an extra inventory kind; the prescribed seven-kind vocabulary is preserved.

## Reproduce

From the deliverable root:

```bash
python -B records/validate_structure.py .
python -B records/compile_syntax.py .
python -B records/compile_syntax.py . --scans 036,039
```

The reusable preamble is `records/syntax_harness.tex`. The compile runner writes all generated files into a new scratch directory and reports that directory. Its JSON results identify every checked page by SHA-256 and report changes during compilation.

Evidence for this pass: `/workspace/scratch/eef0fdbf69f3/mpl_tex_syntax_qa_final_harness/` and the focused scan-021 result in `/workspace/scratch/eef0fdbf69f3/mpl_tex_syntax_qa_scan021/`.

No manuscript image or context archive was consulted. No page content was edited by this mechanical QA work, and no mathematical or source-fidelity assessment was performed.
