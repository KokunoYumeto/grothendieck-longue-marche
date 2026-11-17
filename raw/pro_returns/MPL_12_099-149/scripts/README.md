# Structural validation

`validate_structure.py` checks packaging and transcription syntax. It neither
opens images or archives nor assesses reading accuracy, omissions, the fidelity
of diagrams, the adequacy of inventory granularity, or the research conclusions.
Those remain the sole reader's visual and scholarly responsibilities.

Run from any directory:

```bash
python3 /workspace/scratch/1e5f3f82ab2e/work/MPL_12_099-149/scripts/validate_structure.py
python3 /workspace/scratch/1e5f3f82ab2e/work/MPL_12_099-149/scripts/validate_structure.py --final --json
```

An optional positional directory selects a different unpacked bundle. Exit
status is 0 when structural checks pass and 1 on errors. Warnings require human
review but do not change the exit status. The default partial mode checks only
saved pages and existing files; it does not require the combined transcription
or the final audit/freeze records. Final mode requires all 36 retained scan IDs,
all five requested deliverables, inventory coverage, audit records, and matching
SHA-256 hashes.

## Conventions used by the validator

- The retained scans are 099, 101, 104–109, 111–116, 118–120, 122, 125, 127,
  129, 131, 133, 135, 137, and 139–149. There are 36, not 48.
- Each page is `pages/MPL_12_099-149_12_scanNNN.tex`. Its `scanpage` argument may
  be padded or unpadded. Only the first page contains `cotefile{12}`. Concatenate
  page bytes in scan order, with no additional separators, to make the combined
  transcription. Give individual files their intended terminal newline.
- Inventory columns and kinds follow the prompt verbatim. `typed` is accepted,
  because the earlier explicit typescript instruction adds that value to the
  later list. Element identifiers must be unique within a page; `sheet_kind`
  must be consistent across the page's rows. Every saved page must have at
  least one inventory row and each row must say `yes`.
- The validator checks balanced TeX braces outside comments, nonempty braced
  doubt arguments, and positive integer arguments to `illegible`. It does not
  parse all TeX, compile fragments, or decide whether a symbol belongs to a
  particular alphabet.
- It flags obvious editorial placeholders (`TODO`, `TBD`, `PLACEHOLDER`,
  `[omitted]`, `[transcription pending]`, `[insert transcription]`). It warns
  about literal `[...]`; ordinary ellipses and `etc.` are not automatically
  rejected because those can belong to the source.
- Use `YYYY-MM-DD HH:MM:SS UTC` for all progress timestamps. The first log line
  is the start timestamp alone. Completion and audit records follow the
  prompt's forms: `12 scan 099 done TIMESTAMP` and `scan 099 audited TIMESTAMP`.
- Record frozen hashes in standard `sha256sum` format, with relative paths:

  ```text
  <64 hexadecimal characters>  pages/MPL_12_099-149_12_scan099.tex
  <64 hexadecimal characters>  MPL_12_099-149_transcription.tex
  transcription frozen YYYY-MM-DD HH:MM:SS UTC
  context opened YYYY-MM-DD HH:MM:SS UTC
  transcription hashes unchanged YYYY-MM-DD HH:MM:SS UTC
  ```

  Every page and the combined transcription require a pre-freeze hash. Final
  validation recomputes each hash independently and compares it to that record.
  Audit records must follow completion of all pages; context opening must follow
  the freeze; the unchanged record must follow context opening. Hash records
  must follow the last audit. Page-completion records must be in scan order,
  and milestone timestamps must not run backwards. Image-inclusion commands
  are rejected because the transcription must contain no embedded scan images.

This script was prepared administratively without inspecting manuscript images,
manuscript text, or the context archive. Passing it is not a claim that the
transcription is complete or correct.
