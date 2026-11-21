# Exact crop transport, version 2

Every source-package entry is preserved. PNGs have one of four reversible
representations: their original bytes, lossless JPEG XL, a byte-identical alias,
or a verified deterministic derivation from another included canonical crop.
No crop is discarded, resized relative to its original delivered file, or
reconstructed from attached manuscript scans. Derivation recipes merely avoid
storing a second copy of information already present in an archived parent.

Run `python scripts/restore_crops.py` after extraction to restore every original
PNG path. Filename substrings select a subset; dependencies restore automatically.
Run `python scripts/compact_archive_v2.py --verify-all` to restore all images and
verify SHA256 for **every original file**, including all text and metadata.
Dependencies: Python, Pillow, ffmpeg with libjxl; NumPy for the two recorded
neutral-colour helper transforms. Exact versions used for verification are in
the manifest. Use those versions if a different image-library/zlib version gives
a byte mismatch. Restoration fails closed rather than writing a nonmatching PNG.

`CROP_COMPRESSION_MANIFEST_V2.json` records each original path and SHA256, encoded
payload SHA256 or full parent/transform recipe, PNG saving parameters, pixel hash,
and verification result. Every derivation was executed and its complete PNG bytes
compared with the original before this archive was written. Every encoded JXL was
also decoded and checked for exact pixels and exact PNG-byte reproduction by the
lossless encoder. Dependencies are acyclic. All source text files remain directly
readable without restoration; original ZIP checkpoints were not modified.
