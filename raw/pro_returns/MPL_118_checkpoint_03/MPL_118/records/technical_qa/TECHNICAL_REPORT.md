# MPL_118 current technical QA

Static syntax snapshot: 2026-11-18 02:33:06 UTC.
Doubt/inventory snapshot: 2026-11-18 02:33:06 UTC.
These snapshots may differ while the primary reader continues auditing; each
JSON stores its actual page hashes. Rerun after final edits.

## Results

- 38 page fragments examined.
- 89 TikZ-CD matrices and 434 arrows checked for endpoints within matrix bounds.
- 0 current static syntax findings.
- 366 literal doubt occurrences extracted; no confidence judgments added.
- 781 inventory rows; 0 structural inventory errors.

No brace, environment, dollar-parity, paired-math-delimiter, left/right-group,
or custom-command issue remains unless listed in static_report.json. The
standard command list includes tikz-cd's exposed internal name
\tikzcdmatrixname and the standard commands \vert, \coordinate, and \path.

The formerly invalid off-grid arrows on scans 005 and 034 have been corrected
by the primary reader. This technical agent has made no page edits and has not
read any image or contextual source.

## Doubts and inventory review

The extractor is extract_doubts_and_inventory.py. It records every literal
balanced-brace \unsure or \illegible argument, including exact body and fragment,
page, exact TeX fragment line, short surrounding text, and source hashes.
TeX line numbers are not manuscript line numbers. JSON retains exact content;
TSV JSON-encodes text fields so each occurrence occupies one physical TSV line.

See STRUCTURAL_REVIEW.md and inventory_coverage.json/tsv for count differences.
Macro counts and inventory counts need not match one-to-one; grouped rows and
different containers require primary-reader review. Counts alone do not prove
an omission or certify completeness.

## Compile limitation retained from the first pass

No further compile or installation attempts were made. The first attempt
failed before reading the document because pdflatex.fmt is unavailable. TeX
engine binaries exist, but kpsewhich could not find the LaTeX package tree,
article.cls, formats, and fonts. Details remain in runtime_manifest.json and
compile_attempt.txt. No successful compilation or visual layout verification
is claimed.

The diagnostic validation_wrapper.tex is outside pages and is not a
publication style. Its rendering choices could not be validated because the
format failed to load.

## Reproduce after final corrections

    python3 MPL_118/records/technical_qa/static_checks.py
    python3 MPL_118/records/technical_qa/extract_doubts_and_inventory.py

The primary reader's visual audit and frozen-transcription hashes remain
independent requirements.

## Rerun after all second image audits

At 2026-11-18 02:33:06 UTC, the extractor found 366 unsure occurrences and 0 illegible occurrences. All page hashes agree across the static, doubt-extraction, and inventory snapshots: True. No compile attempt was repeated.
