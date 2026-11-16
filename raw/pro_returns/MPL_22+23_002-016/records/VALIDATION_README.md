# Mechanical validation

`validate_package.py` is a read-only structural checker until an explicit
`--json-report` path is supplied. It was created without opening the scans,
transcription pages, or context archive. The transcription owner chooses when
to run it; it has not been run against the package during its creation.

From the package directory, after the final hash check has been recorded:

```sh
python3 records/validate_package.py --json-report records/validation.json
```

The checker covers the required 44 page filenames; cote and scan marker order;
brace balance with TeX comments and escaped braces; required deliverable names;
the CSV header, page coverage, row identifiers, kinds, sheet kinds (including
`typed`), and `transcribed=yes`; verbatim page content in the combined fragment;
the done/audit sequences; UTC timestamps; freeze/context marker order; and
SHA-256 records compared with the present page and combined-file bytes.

For hash records it recognizes either of these forms, using package-relative
paths or absolute paths within the package:

```text
SHA256 DIGEST pages/FILENAME.tex
SHA256 pages/FILENAME.tex DIGEST
```

Conventional `sha256sum` output, `DIGEST  PATH`, is also accepted. Record the
44 page hashes and combined-fragment hash. The log's audit entries may carry
the cote (`22 scan 002 audited TIMESTAMP`) or omit it in the required overall
page order (`scan 002 audited TIMESTAMP`). The first log line and action
timestamps use `YYYY-MM-DD HH:MM:SS UTC`.

Unrecognized LaTeX commands are review warnings. The script recognizes the
specified custom macros and a broad, explicit standard/TikZ command list;
it cannot prove that every possible package command is standard. After checking
a reported command, add `--allow-macro COMMAND` (repeatable). Use
`--strict-macros` to make remaining command-review warnings fail validation.

Exit code 0 means no mechanical errors were found. Warnings remain visible.
Exit code 1 means one or more mechanical checks failed. Neither result certifies
that every mark of ink was transcribed, that readings are correct, that the
inventory reflects every visual element, or that the recorded reading/audit
work actually occurred. Those require the transcription owner's visual checks.
No OCR, image access, context access, external lookup, or LaTeX rendering occurs.
