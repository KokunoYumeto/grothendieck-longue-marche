# Mechanical validation tooling

`scripts/validate_package.py` performs read-only structural checks. It does not
access images or the research context and does not interpret or correct readings.
Its reports contain no manuscript excerpts.

## Commands

Run from any directory:

```sh
python /workspace/scratch/fce80d805cc4/MPL_136_142-188/scripts/validate_package.py --partial
python /workspace/scratch/fce80d805cc4/MPL_136_142-188/scripts/validate_package.py --final
```

`--root PATH` selects a relocated package. A nonzero exit status denotes a
structural error. Partial mode permits unfinished pages; final mode requires all
46 expected scans (142–188, excluding 161), both Markdown deliverables, audit
coverage, a freeze entry, and all transcription SHA-256 entries in `progress.log`.

The combined transcription must be the byte-for-byte concatenation of the
individual page files in numerical scan order. Any separating newlines therefore
belong to the page files themselves.

## Digest format

Use sha256sum-format lines relative to the package root, optionally prefixed by
`sha256 `, in `progress.log` and in an optional manifest:

```text
<64 hexadecimal characters>  pages/MPL_136_142-188_136_scan142.tex
<64 hexadecimal characters>  MPL_136_142-188_transcription.tex
```

The validator automatically checks `records/frozen.sha256`,
`records/frozen_hashes.sha256`, and `records/freeze.sha256` when present. Use
`--hash-manifest PATH` for another name. Hash entries in `progress.log` are always
checked when present.

## Scope and limits

Checks cover filenames and the prescribed sequential prefix; matching scanpage
markers; UTF-8; brace and environment balance with escaped symbols and comments;
inventory schema, supported kinds, element identifiers, and scan coverage;
done/audited log coverage; combined-file identity; and SHA-256 integrity.
Structural checks cannot establish textual accuracy or inventory completeness
against the handwriting. The TeX checks do not expand macros or parse verbatim
environments and do not replace a LaTeX compilation.

## Available TeX executables

Environment inspection found:

- `/usr/bin/pdflatex`
- `/usr/bin/xelatex`
- `/usr/bin/lualatex`

No scans, transcription content, or context contents were inspected by the
tooling author. Only one initial partial dry-run was made.
