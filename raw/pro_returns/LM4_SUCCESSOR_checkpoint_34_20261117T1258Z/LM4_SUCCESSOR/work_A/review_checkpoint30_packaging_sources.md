# Independent checkpoint30 packaging source review

**Verdict: PASS at the complete source-and-record review scope.** Reviewer: agent A (`/root/involutions`). No packager, measurement producer, compression, extraction, test ZIP, or new archive was executed or created for this review. The actual checkpoint30 capture and native restoration verification remain the parent's separate executed gates.

## Material read in full

I read all of `checkpoint_data_tar.py`, `package_checkpoint.py`, `checkpoint_archive_io.py`, `verify_checkpoint_snapshot.py`, `checkpoint_standard_tar.py`, and `measure_checkpoint30_data_tar.py`; the complete saved `checkpoint30_data64_measurement.json`; and the entire preserved-before/current diffs of the packager, reader, and verifier. I also read the installed Python standard-library implementations of `zipfile.LZMACompressor`, `LZMADecompressor`, and `_get_compressor` using source inspection. The accompanying JSON binds every repository source and the preserved predecessors by exact SHA-256.

## 1. Complete logical path and byte coverage

The packager still first reads each included original file exactly once into the `contents` list, and uses those same bytes for both the logical SHA-256 manifest and physical packaging. Existing explicit exclusions are unchanged except for recognizing the new root-level storage-only `historical_data.tar`, alongside the prior image/document storage containers. This exclusion prevents re-including an already-restored container; it does not exclude its unpacked original logical files.

For checkpoint numbers at least30, the new selector takes precisely non-PNG/PDF/TAR files under `checkpoint_history/`, together with JSON files of at least1,000,000 bytes. Suffix comparison is case-insensitive. PNGs remain in the image container, historical/preview PDFs in the document container, and the current main PDF remains a direct ZIP entry. Data selection excludes both image and document types and is explicitly checked against the document path set. TAR files are not recursively repacked into the data TAR. Every selected path is skipped exactly once in the direct ZIP loop and appears in the data TAR; all remaining included paths stay direct or use their existing image/document container. The logical manifest continues to enumerate original names and bytes, rather than storage containers. The new current packaging record is replaced deliberately, appended once, and included in that manifest.

The deterministic standard TAR helper sorts names, rejects duplicate or unsafe relative paths, emits regular entries or ordinary backward hardlinks, and compares complete bytes before reusing a same-length/SHA-256 entry. Thus hash lookup does not by itself authorize deduplication. Every hardlink points to an earlier regular entry, not to a chain. All original names survive, and no decoding-specific data transformation is introduced.

## 2. Standard ZIP method14 and scoped dictionary change

`DataLZMACompressor` retains the standard-library compressor interface and inherited `compress`/`flush` behavior. Its only change is the encoded LZMA1 dictionary size. The prefix is the same standard method14 framing used by the installed `zipfile` implementation: bytes9,4, a little-endian two-byte property-length field, then ordinary LZMA filter properties, followed by the raw LZMA1 stream. The saved properties `5d00000004` specify the64 MiB dictionary. The installed unchanged `LZMADecompressor` reads those properties and initializes its decoder from them; no custom reader is required.

The context manager saves the original module class, substitutes the new compressor for the one synchronous data-TAR `writestr`, and restores the original in a `finally` block. The inspected `_get_compressor` performs the relevant module-global lookup, so the temporary replacement is effective. In this single-threaded packager there is no concurrent unrelated compressor creation inside the scope. The two preceding TAR writes and all direct entries retain their prior compressor settings. Exceptional exit also restores the original class. Checkpoints below30 do not select or write the third container.

## 3. Reader and verifier compatibility

The reader accepts legacy direct archives and archives with zero, one, two, or three optional standard TAR containers. It exposes every regular/hardlinked member under its original logical path. It rejects absolute/traversing names, duplicate ZIP names, duplicate logical paths, cross-container collisions, unexpected TAR types, forward/missing hardlink targets, and hardlink chains. Data-member reads use `tarfile.extractfile`, including standard hardlinks. Closing the reader closes all containers.

The verifier still checks physical ZIP CRCs, exact equality of logical names with the manifest plus the manifest itself, every file's declared length and SHA-256, and every required historical-retention row. It additionally verifies the data-TAR byte length, SHA-256, and logical member count against the current packaging record. The direct-main-PDF assertion remains. Hence the third container does not bypass complete file validation or version retention, and previous archive formats remain accepted.

## 4. Exact scope of the genuine measurement

The measurement producer reads immutable checkpoint29 directly and applies the same selection predicate to entries that were direct there. It constructs the same deterministic TAR, streams it through ordinary raw LZMA1 with the standard method14 header, and feeds the resulting bytes immediately to the unchanged standard-library decoder. It creates no ZIP. The saved record reports876 logical paths,851 unique contents and25 hardlinks; a525,649,920-byte standard TAR; an18,730,014-byte method14 stream replacing43,328,507 bytes of prior compressed payload. The exact payload saving is24,598,493 bytes. The full decoder output length and SHA-256 equal the TAR, with EOF observed.

The record correctly binds the actual525,162,412-byte checkpoint29 and reports the equivalent500,563,919-byte size only before header adjustment and before new work. It explicitly does not predict checkpoint30's eventual size, claim a new archive, or modify the input. The measurement's original output record is evidence of that earlier genuine run; this review did not rerun it.

## 5. Result and limits

No coverage, standard-format, hardlink, dictionary-restoration, or reader-compatibility defect was found in the reviewed changes. All requested changes are storage representation only. This PASS is bound to the exact sources below and does not substitute for the parent's forthcoming actual checkpoint30 write/read/native-restoration verification. No frozen mathematical source, previous archive, prior review, or central register was changed by this audit.
