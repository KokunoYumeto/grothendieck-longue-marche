# Checkpoint23 archive verification

Result: **PASS**. Checked 2026-11-20T09:08:59.271638+00:00.

Archive: SP02_CW_10+12_checkpoint_23.zip; 4,765,404 bytes; 824 entries.

SHA-256: e5917ea1c0a3f1de59da18c61bfdc977e8468353db863e753bcf112ea4010c2a

CRC and every member size/SHA-256 agree with the packaging manifest. All106 canonical page/record pairs agree internally; the combined file exactly concatenates the ordered page bytes. All280 protected staging fingerprints and all146 scoped copy fingerprints match the archive.

Active audit040 is preserved as started, with its matching baseline page/record, two before-history files, and immutable image-first observation/text-open receipt. No completion, freeze, or context-open event was fabricated. The partial040 note and generic audit crop generator are included; 31 scoped audit-work files and 14 recipe JSONs were checked.

No input source/scan/witness/context directories, raster images, nested archives, unsafe paths, duplicate/case-colliding names, or symlink/special-file entries were found. New helpers, guide, schema, tests, and incomplete template are included.

All verification inputs stayed unchanged during this check. Live audit pages/progress were not compared after root resumed; this report verifies the archived staged snapshot. No live page, record, projection, audit state, or log was modified.
