# Lossless historical-PDF encoding for checkpoint24

Checkpoint23 is immutable:520257467 bytes, SHA-256
6986909bd5d014a6c006736635de97032490273d4548562b57792aa7ffd90dd1.
The next delivery cap is536870912 bytes. We measured a standard TAR
container of all56 historical/preview PDFs actually present in23, plus
the exact current main PDF under its prospective checkpoint23 historical
path. The current main PDF of24 will remain directly accessible in its ZIP.

The57 measured PDF paths contain86313911 original bytes. Their standard
TAR has86364160 bytes; its ZIP-LZMA payload has33342689 bytes, compared
with82493648 compressed bytes for the56 individually stored old PDFs.
The resulting baseline estimate, including the additional historical main
PDF, is471106508 bytes. A30000000-byte next-interval allowance gives
501106508 bytes, below the cap. This is a measurement and an allowance,
not a prediction that replaces the final pre-capture total estimate.

The exact compressor/decompressor round trip and independent native-TAR
restoration of every original path and byte both passed. No additional
checkpoint ZIP was created. Code, genuine output and exact input hashes
are in code/measure_checkpoint24_pdf_bundle.py and
records/checkpoint24_pdf_bundle_measurement.out/.err/.json.

The packager, logical reader and manifest verifier now support the second
container from checkpoint24 onward. Version retention automatically sees
the same original logical paths through that reader. The dedicated
code/verify_checkpoint24_system_tars.py does not import any of these
implementations; after the one scheduled capture it will independently
restore both actual containers with system tar and verify every archived
path, size and digest. README.md gives both restoration commands.

No earlier archive has been rewritten, renamed or deleted. All source,
current deliverable, historical PDF and verification-image bytes remain
part of the logical checkpoint manifest. The two TAR files are only
storage containers, each separately hashed in the packaging record.
