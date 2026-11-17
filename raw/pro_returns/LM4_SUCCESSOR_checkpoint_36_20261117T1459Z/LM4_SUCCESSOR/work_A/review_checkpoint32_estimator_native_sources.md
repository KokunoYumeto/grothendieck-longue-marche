# Complete source review: checkpoint32 estimator and native TAR verifier

Reviewer: A/involutions. This is an entire-source read of both new helpers and both checkpoint31 predecessors. Neither helper was imported or executed. The current packager, data compressor and standard-TAR builder were also read in full to check their relevant selection and encoding contracts.

## Source bindings

- `code/estimate_checkpoint32_size.py`: `28711b1a2eac9fb0a773c68846244660016d917a79fc4133d3be37e741fb42ab`.
- `code/estimate_checkpoint31_size.py`: `6079bcc52568ec9a13f07f44e9da102696d7743771301ab74cfcb264a361319f`.
- `code/verify_checkpoint32_system_tars.py`: `10ac57ddd367e923361bc0add5b3dea4be330252138352a85c5bf411aa477085`.
- `code/verify_checkpoint31_system_tars.py`: `3dfeeb5391b5e863b6c564653de632ce50464dc5cc02d85ded73402e74a6b72a`.

## Estimator: PASS, with one nonfunctional prose correction requested

The actual baseline is checkpoint31, the output record is checkpoint32, and the manifest lookup, predicted history paths and report keys consistently use31. Every parent logical entry is accounted for, including its own digest manifest. The three records that will be rewritten are forcibly retained historically. Predicted historical collisions require exact equality.

The authored-file inclusion predicates match the current packager. The image, document and data buckets are disjoint and use the same data selector. The estimator rebuilds the full prospective standard-TAR contents with the same sorted paths and exact-content hardlinks. The image builder in the packager and the shared builder have equivalent headers/order/deduplication for those sorted inputs.

Compression counts actual incremental compressor output, including standard method14 framing. Images and data use the actual 64MiB DataLZMACompressor; documents use the default8MiB ZIP-LZMA compressor. Direct DEFLATE parameters match the packager's level6/raw stream; other direct text uses ordinary ZIP-LZMA. The current packager scopes the64MiB override separately to each image/data write and restores the original compressor in finally, leaving documents/direct text unaffected.

The arithmetic subtracts the three previous compressed containers and any former direct data payloads now migrated, adds the complete new buckets, and adds every new/changed direct payload. Retaining changed old direct costs and old headers is an intentional overcount. The previous main PDF is additionally retained in the historical document bucket. The5MB allowance is explicitly an allowance for new headers/manifests/retention growth/late text, not a theorem covering arbitrary later mutations; the final immutable archive size remains authoritative. The helper creates no ZIP and does not rewrite authored inputs, but writes its own estimate report and refuses blind overwrite.

One report-scope sentence still says `every changed30 logical version`; the actual algorithm and destination are correctly checkpoint31. Root has been asked to change that prose token to31 and bind a separate final diff. No calculation or path change is required.

## Native verifier: PASS

All archive, manifest, packaging and temporary-prefix identifiers are32. It uses the actual closed archive and does not import the packager, standard-TAR builder, or logical reader. It verifies all three method14 entries and reads their native ZIP local-header property bytes. Data and image dictionaries are exactly67108864; the document dictionary is exactly8388608, each compared with the archived packaging record. The normal ZipFile reads also validate the actual stream/header and CRC while decoding.

The independently spelled-out expected path selectors match the packager: all PNGs, every noncurrent PDF, and all non-PNG/PDF/TAR historical files plus JSON at least1000000bytes. Each container has exact expected coverage, no overlap with direct entries, the recorded raw-byte hash/length and the recorded logical-path count. Each TAR member is a regular file or a backward hardlink to an already validated regular member; absolute/parent-traversal names and duplicate/unexpected entries are rejected. No symlink or hardlink chain is accepted.

The helper then invokes ordinary system tar on each actual decoded bundle in a fresh temporary directory and checks every extracted logical path's type, length and SHA256 against the immutable manifest. This verifies ordinary restoration and every hardlinked logical path, not only the regular payloads. The current main PDF must remain a direct ZIP entry. The final report binds the full archive hash and all three dictionary sizes.

This source review makes no claim that the estimator has run, that a bound was met, that native extraction passed on a future archive, or that checkpoint32 exists. Those require their actual observed executions. The sole requested correction above is report wording, and needs a final-byte diff binding after root changes it.
