# Administrative TSV serialization correction — 151_scan047

Agent: /root/reader_c

UTC correction time: 2026-11-21 22:02:12 UTC

The parent requested this correction after a default TSV/CSV parser returned 14 records and no separate b08. Only my own saved second TSV, own independent notes, and this page's neutral boxes TSV were inspected. No source image, witness, first reading, or other reader was consulted; no reading was revised.

## Byte-level cause

The original was raw tab-delimited text. The b07 reading starts with literal quotation byte 0x22, immediately after delimiter byte 0x09. A default quote-aware CSV parser treated that quotation as a field opener, then consumed the line-feed byte 0x0A and the b08 row until the literal quotation in b08. Thus b08's physical line was present but absorbed into b07's parsed field. Parsed record count was 14 instead of 15.

## Correction

The exact original bytes are preserved at `/workspace/scratch/27306e6fcc57/SP94_C13_151_work/audit/151_scan047_second_serialization_original.tsv`.

All 15 original readings were parsed with QUOTE_NONE and checked against the already-written independent notes. The TSV was then serialized with a tab delimiter, minimal standard field quoting, doublequote escaping, and LF record terminators. Literal 0x22 bytes in quoted fields are represented by doubled 0x22 bytes inside enclosing quotation bytes. A standard parser therefore returns the exact original reading strings, including quotation marks and literal TikZ quotes. The only physical rows changed are b07, b08, b13. There is no reading/content change.

Original byte count: 875. Corrected byte count: 887.

Original SHA-256: `0ddc10d877c12e12977989ce435151022bca353b19f3d4102d266106cb7f7233`

Corrected SHA-256: `f9b99065d9d18ba0863bc7f9520a48453ad9d20189fddf233d992df249e3507e`

Validation: standard csv.DictReader with delimiter tab now returns all 15 boxes in neutral-box order; every parsed reading equals its original raw TSV value; the audit copy is byte-identical to the original.
