# Strict read-only freeze verification

`freeze_verify.py` checks a freeze already recorded by the primary transcriber. It never creates a freeze, changes a source file, adds a log entry, opens an image or context source, or uploads anything.

Run immediately after recording the freeze:

```sh
python scripts/freeze_verify.py --json
```

Run the final integrity check after opening and using context:

```sh
python scripts/freeze_verify.py --require-context --json
```

The default root is the script directory's parent. `--root /absolute/work/path` selects another work directory. All output goes to stdout; exit status is 0 for a passing integrity check and 1 for a failure. There is no output-file option or log-write action.

## Required status records

The first line of `progress.log` must be the actual start timestamp. Use the following exact shapes, substituting actual UTC values:

```text
YYYY-MM-DD HH:MM:SS UTC
scan 035 audited YYYY-MM-DD HH:MM:SS UTC
transcription frozen YYYY-MM-DD HH:MM:SS UTC
context opened YYYY-MM-DD HH:MM:SS UTC
```

There must be exactly 47 audit entries: one for every scan from 035 through 081, all before the single freeze entry. Extra or repeated audit entries fail the check. All status timestamps must be valid calendar values in the displayed UTC format and must not go backwards in log order. The context-open entry is optional for the immediate post-freeze check; `--require-context` requires exactly one. A recorded context-open entry must follow the freeze by both line order and timestamp.

## Hash record formats

Exactly 48 unique transcription entries are required: the 47 files under `pages/`, plus `MPL_72_035-081_transcription.tex`. The following forms are accepted, where `DIGEST` means the actual 64 hexadecimal characters:

```text
DIGEST  pages/MPL_72_035-081_72_scan035.tex
DIGEST *pages/MPL_72_035-081_72_scan035.tex
SHA256 pages/MPL_72_035-081_72_scan035.tex DIGEST
SHA-256 pages/MPL_72_035-081_72_scan035.tex DIGEST
SHA256 DIGEST pages/MPL_72_035-081_72_scan035.tex
pages/MPL_72_035-081_72_scan035.tex: DIGEST
```

Hash keyword spelling is case-insensitive. Hash letters may be upper or lower case. The hash path may be the shown relative path, a bare expected page filename, or its exact absolute path under the selected root. Parent-directory components and paths outside the selected root are rejected.

Hash entries may precede or follow the freeze line, but every transcription hash entry must precede the context-open line. A repeated final listing would introduce duplicate records and fail the exact-count check: perform final verification against the original 48 entries, then record the unchanged-hashes statement separately in the progress log. This helper itself adds no statement.

Recognized hashes of non-TeX files, such as a checkpoint ZIP, are reported separately and excluded from the transcription-manifest count. An extra `.tex` hash, a duplicate expected path, or a malformed hash line mentioning a TeX path fails verification.

## Byte checks and limits

The verifier reads the 48 expected files, computes their SHA-256 digests, and compares each with the unique recorded value. It requires the combined file to equal the **direct byte concatenation** of page files in scan order, with no extra separator bytes. It rejects unexpected `.tex` fragments in `pages/` and symlinked expected files.

These checks establish consistency of the recorded manifest and the present files. They do not prove that the images were audited, that every manuscript element was transcribed, or that the research notes are complete. The helper does not inspect notes or context and does not verify the meaning of prose such as a final “hashes unchanged” statement.

The helper was tested only on synthetic fixtures outside the deliverable work directory. Tests covered a valid 47-page/48-hash freeze, a later context record, duplicate and missing audits, duplicate and extra hashes, changed file bytes, inconsistent combined bytes with an updated hash, invalid UTC dates, and incorrect audit/freeze/context order. It was not used to create or execute the actual transcription freeze.
