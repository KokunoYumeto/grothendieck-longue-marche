# Mechanical package validator

`validate_package.py` is a dependency-free Python 3 checker. It never opens the
scan images, the source archives, or the research context. It does not alter any
transcription, inventory, doubts, notes, or progress file. It writes a report only
when an explicit `--output` path is provided.

Run while work is ongoing:

```sh
python records/validate_package.py --partial
```

Run at completion and save a detailed report:

```sh
python records/validate_package.py --output records/mechanical_validation.json
```

The optional positional argument is the package directory. Its default is the
parent of `records/`. `--json` prints the full report, including the exact contents
and page/line location of every `\unsure` and `\illegible` occurrence. Exit status
is 1 if mechanical errors were found, and 0 otherwise. Partial mode treats absent
deliverables and missing completion events as informational, while preserving
structural errors in files that already exist.

The checks cover the 43 expected scans (90, 91, 93–133); per-page filenames and
markers; the combined fragment's ordered equality to each page after trimming
boundary whitespace; unwanted preamble and image/external-input commands; braces
and environments; possible literal omission placeholders; inventory columns,
element identifiers, categories, per-page coverage, and `yes` status; check-event
columns and event types; recorded completion/audit/freeze order; and current file
hashes against recognized logged SHA-256 values. Genuine `\ldots`, `\cdots`, and
other mathematical ellipsis commands are not flagged as placeholders.

For hashes, use an exact deliverable filename and its 64-digit SHA-256 on the same
log line. Standard `sha256sum` lines work, as do labelled lines such as
`SHA-256 pages/MPL_138_090-133_138_scan090.tex <digest>`. Hashes recorded before
`context opened` are the frozen references; the latest recognized value per file
is used. The validator reads files only beneath the explicitly supplied package
root, even if a log line includes an absolute source path.

## Limits

No success result certifies the readings, spelling, attribution, notation,
completeness of an inventory, placement of insertions, diagram fidelity, or the
truth of an audit or check event. These require the author's visual or mathematical
work. Literal `[...]` and similar tokens are review warnings rather than automatic
errors because an original manuscript could itself contain them. The TeX checker
is a lightweight lexical check, not a TeX engine; unusual verbatim constructions
or unconventional macros may require manual review. The doubts file's headings
are checked heuristically, but its table is not claimed to cover every uncertainty
without a human comparison.

## Apparatus arguments and compilation

The uncertainty parser accepts both braced arguments and legitimate unbraced
single-token arguments, including a control sequence or a digit.
`compile_harness.tex` is an optional separate compilation harness, with its input
list refreshed by `update_compile_harness.py`. See `structural_support_report.md`
for the actual compilation availability and limits observed in this environment.
