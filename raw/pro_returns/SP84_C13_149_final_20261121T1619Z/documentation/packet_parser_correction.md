# Literal TSV parsing correction

At 2026-11-21 12:40:12 UTC, reader_b noticed later scan rows embedded in scan017’s difference packet. The supplied TSV has exactly five tab-separated fields on each of its 547 physical lines, including its header. It is not CSV-quoted. Default quote handling wrongly joined some quote-initial fields across rows. The corrected parser uses `csv.QUOTE_NONE` only for the supplied literal TSV files, while generated CSV-quoted TSVs retain the corresponding default reader.

The correct number of supplied difference rows is 546. Counts and content for scans005–016 were unchanged. Scan017’s packet was corrected to its own 18 rows before the return; scans018 onward had not been assigned. Reader_b was instructed to ignore the unintentionally included later rows and will not independently audit scans018–022, preserving the independent-reading scope. No manuscript page reading was changed by this parser repair.
