# Final readiness publisher and exact size-accounting review

Reviewer A (`/root/involutions`): **PASS**.

I read all 253 lines of the final publisher in bounded, untruncated reads,
the entire exact predecessor-to-final diff, the entire reconciliation source,
the entire unchanged size estimator and data-selection helper, the complete
correction JSON and its independent CE review JSON, the genuine accounting
stdout, and the preserved estimator traceback. No reviewed helper was
imported, executed, or rerun by me. No new compression or ZIP was created.

The final publisher is `code/publish_checkpoint34_readiness.py`, SHA256
`55a67ef2d672560272a8b982506d57b5e776aa935caeddb219ef203875772124`,
15335 bytes. Its original e283ab7c source is preserved separately, and my
earlier complete source review and JSON remain unchanged.

## Exact accounting proof

The estimator retains the whole parent ZIP baseline except its three
container payloads and direct entries selected by the data-bundle predicate.
The previous direct main PDF is neither a container nor a data member:
the data selector explicitly excludes PDF files. The changed previous main
PDF is also a predicted historical entry and, as a non-main PDF, is included
in the actually measured document TAR. The new current main PDF is counted
separately as a new direct payload. Thus the old main PDF's direct compressed
payload remains a duplicate in that particular estimate.

The reconciliation verifies the parent archive identity, reads that exact
old main-PDF member, checks its bytes and hash against the predicted history
row, and deducts only its actual compressed payload size, 4177417 bytes.
It removes no ZIP header, logical file, historical version, or part of the
5000000-byte allowance. The exact arithmetic is
537725722 - 4177417 = 533548305, below 536870912 by 3322607 bytes.
All three prospective bundle records remain identical. The old source,
report, stdout, and stderr are preserved byte-for-byte before the corrected
report is written. This is a reconciliation of completed measurements,
not a rerun, a changed compression assumption, or a new archive.

The estimator's actual session 55851 and chunk 15fae9 remain recorded with
exit code 1. Its retained traceback is precisely the final conservative
cap assertion after the report was written. The genuine accounting stdout
records PASS_EXACT_DUPLICATE_ACCOUNTING and zero omitted files; its stderr
is empty. This review does not recast the failed estimator as successful.

## Final publication checks

The six successful final roles now contain the separate successful accounting
operation, with its own observed chunk and four required accounting evidence
files. The source explicitly rejects session 55851 in that success role.
It separately requires the failed measurement record, its exact session,
exit code and chunk, and all preserved report/log/source evidence. The
operational bindings and final readiness record retain both events with
their correct statuses.

The publisher checks the correction's exact arithmetic, unchanged bundle
measurements and allowance, zero omitted files and header deductions, the
correction-file hash, and every preserved precursor hash/byte count. It
requires the independent entire-source reconciliation review and binds its
actual source hash. All earlier producer-role, three-writer pause, final
PDF/metrics/visual, no-existing-ZIP, and ready-last exclusive-publication
checks remain unchanged. The successful operation still needs the root's
actual exit-zero observation; this source audit does not fabricate one.

The final source and its accounting change pass. The original full publisher
review supplies the unchanged interface analysis; the final complete read
confirms those checks remain present. No source correction is requested.
The final immutable archive size and later complete-byte/native-restore
verification remain subsequent obligations, not results of this audit.
