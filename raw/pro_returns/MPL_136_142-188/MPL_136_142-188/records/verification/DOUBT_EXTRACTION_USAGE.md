# Lossless doubt extraction

Run the extractor after the visual reader’s last changes:

```sh
python /workspace/scratch/fce80d805cc4/verification/extract_doubt_table.py
```

It writes only under `verification/doubt_extraction/` by default:

- `doubt_occurrences.json`: every balanced `unsure` and `illegible` occurrence, with exact raw macro and argument, filename, TeX source line, containing wrappers, SHA-256, and pipe-split candidates.
- `doubt_occurrences.csv`: the same data in CSV; exact raw strings are checked by a CSV round trip.
- `confidence_assignments_blank.csv`: occurrence IDs and page hashes for the visual reader’s confidence assignments.
- `summary.json`: counts and integrity results.

The shared parser is `verification/tex_macro_extract.py`. It skips TeX comments, respects escaped braces and control symbols, retains nested macros as separate occurrences, and preserves source offsets. No OCR, images, context archives, or interpretation of readings are involved.

## Alternatives and vertical bars

Every raw argument is retained without modification. Unescaped pipes at brace depth zero are recorded as candidate separators. The candidate parts satisfy the checked identity `"|".join(parts) == raw_argument`, including repeated/empty segments. Pipes inside braces or escaped control symbols remain inside their parts.

The extractor does not decide whether a literal pipe is an alternative separator or mathematical notation. All automatic separator candidates are marked for review. The reader can set `split_pipes=no` for an occurrence whose raw argument must remain one reading, or `split_pipes=yes` to accept the candidate split. Exact raw strings remain available in both cases.

## Confidence assignments and an optional table draft

Copy the blank assignments file to a separate working CSV before filling it. Its columns are:

```csv
id,confidence,split_pipes,source_sha256
```

Confidence values are `high`, `medium`, `low`, or blank. No confidence is inferred by the extractor. Page hashes protect assignments against subsequent source changes.

Example rerun after the reader has filled `verification/confidence_assignments.csv`:

```sh
python /workspace/scratch/fce80d805cc4/verification/extract_doubt_table.py \
  --confidence-map /workspace/scratch/fce80d805cc4/verification/confidence_assignments.csv \
  --markdown /workspace/scratch/fce80d805cc4/verification/doubt_table_preview.md
```

The optional Markdown table has separate file, scan, TeX line, reading, alternatives, confidence, and occurrence columns. Code cells encode literal pipes as `&#124;`, preventing Markdown column splitting while displaying the original pipe. JSON and CSV retain authoritative unescaped source strings. Empty confidence assignments are explicitly marked `unassigned` in the preview.

No final doubts deliverable is created or changed by the default command. The notation table, abbreviation list, and the visual reader’s legibility assessment remain separate authorial work.
