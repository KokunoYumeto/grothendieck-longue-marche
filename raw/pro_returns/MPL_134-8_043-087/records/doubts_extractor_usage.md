# Raw doubt-macro extractor

**Final status:** after the principal reader authorized live extraction, the helper ran on all 44 page files and was refreshed after the final scan 073 notation edit. `records/doubts_extracted.json` contains 457 complete raw occurrences and no extraction errors. `records/doubts_extraction_integrity.json` independently verifies all 44 source hashes, all 457 character and UTF-8 byte slices, and all locations. No reading or confidence was assigned and no source or doubt-register Markdown was altered by the helper. The earlier 19 synthetic checks remain preparation evidence.

## Read-only source extraction

From the package’s parent directory:

```sh
python MPL_134-8_043-087/scripts/extract_doubts.py
```

This invocation selects the `.tex` files in the package’s `pages/` directory and writes a separate `records/doubts_extracted.json`. Explicit `.tex` paths may be supplied as positional arguments, and `--output` selects another separate JSON file. Markdown outputs, per-scan inventory filenames, input-file collisions, and existing JSON artifacts from another schema are refused.

## What is recorded

Every literal `\unsure` and `\illegible` control-word occurrence receives a record, including nested occurrences. Each record includes the filename, scan number derived from its filename, macro name, source location, exact raw argument, exact intervening whitespace/comments before its argument, and source spans. No confidence, preferred reading, alternative split, word-count interpretation, or notation-table change is assigned.

Files are read as bytes and decoded as UTF-8 without universal-newline conversion. Raw arguments preserve all original newlines, escaped braces, control symbols, comments, nested groups, and math tokens. Commented braces and escaped braces are ignored only for structural matching; their original text remains in the raw slice. A doubled backslash is consumed as one control symbol, so a brace after it retains its structural role.

Locations use **1-based lines and columns**. LF, CRLF, and bare CR each advance one line, while their characters remain intact in the raw source. Columns and `character_offset` values count Unicode code points. Character and UTF-8-byte offsets are **0-based**, and every span end is exclusive. Both forms of span identify the same exact raw source slice. Source SHA-256 values tie the records to the bytes that were read.

## Malformed arguments

An unclosed target argument retains all available raw text through EOF and is marked `unclosed_argument`. A target without an explicitly braced argument is marked `missing_braced_argument`. The lexical scan continues through the file, so earlier records and nested target occurrences are retained.

The output JSON contains both records and an error list. Malformed arguments or source-read errors produce visible diagnostics on standard error and exit status **2**, after all available records have been written. Successful extraction returns **0**.

This is a lexical extractor for explicitly braced task macros. It does not expand TeX, execute catcode changes, or interpret verbatim-like environments. Its raw argument field is authoritative; it supplies no editorial reconstruction.

## Synthetic validation

```sh
python MPL_134-8_043-087/scripts/test_extract_doubts_synthetic.py
```

The validation script parses the extractor’s Python syntax, exercises fixed in-memory examples, and creates temporary synthetic `.tex` files beneath `records/`. It tests nested targets, ordinary and escaped braces, control symbols, comments, whitespace before arguments, math groups, Unicode/byte spans, CRLF preservation, malformed arguments, source-read errors, visible nonzero failure, preservation of earlier records, and output guards. It writes only `records/doubts_extractor_synthetic_validation.json`; its temporary fixtures are removed. It never selects or reads the live page directory.
