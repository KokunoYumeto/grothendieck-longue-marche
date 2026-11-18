# Structural inventory and doubt extraction

Checked 2026-11-18 02:36:18 UTC. This is a technical pass over saved TeX and CSV files;
no scan images or contextual sources were opened, and no source file was changed.

## Doubt extraction

369 literal doubt occurrences were extracted from 38 pages.
The JSON and TSV include page, exact TeX fragment line, exact body, and short
surrounding text. No confidence judgments have been assigned. TeX fragment line
numbers are not manuscript line numbers.

## Inventory structure

The CSV has 810 rows for 38 scan numbers.
Structural errors detected: 0. See inventory_coverage.json for any
invalid rows, missing pages, duplicate IDs, or transcribed values other than yes.

## Count differences for primary-reader review

Each entry below is macro: occurrences/inventory rows (difference).
A positive difference means more literal macro occurrences than rows of its
corresponding kind. A negative difference means more inventory rows. Neither
proves omission: inventory rows sometimes group several insertions or deletions,
and a drawing or diagram can occur inside a different container. The primary
reader should decide whether separate inventory rows are needed.

| Scan | Nonzero count differences |
| --- | --- |
| 006 | diagram: 1/2 (-1) |
| 007 | diagram: 1/2 (-1) |
| 012 | margin: 2/4 (-2) |
| 020 | diagram: 5/6 (-1); inserted: 0/1 (-1) |
| 021 | margin: 4/5 (-1) |
| 023 | figure: 0/1 (-1) |
| 025 | margin: 9/7 (+2) |
| 035 | figure: 0/2 (-2); margin: 0/2 (-2) |
Displays and prose are not matched one-to-one automatically. The inventory's
display category includes material inside arrays and other containers, whereas
the display-delimiter count includes only explicit display-math delimiters.
Text-block boundaries cannot be recovered reliably from blank lines. Counts
are review aids, not a certification of diplomatic completeness.

## Reproduce

    python3 MPL_118/records/technical_qa/static_checks.py
    python3 MPL_118/records/technical_qa/extract_doubts_and_inventory.py

Both JSON reports preserve the SHA-256 of the actual page versions inspected.
Rerun after final edits before using the extracted positions in a final table.
