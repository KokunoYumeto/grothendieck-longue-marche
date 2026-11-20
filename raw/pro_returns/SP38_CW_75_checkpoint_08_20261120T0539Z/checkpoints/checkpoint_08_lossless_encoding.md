# Checkpoint 08: lossless encoding retry

This archive is the **same 2026-11-20 05:00:26 UTC snapshot** as
`SP38_CW_75_checkpoint_08.zip`. Its first save failed because its 562,042,425 bytes exceeded
the native file limit of 536,870,912 bytes. This packaging retry does
not introduce a new checkpoint, reading, transcription, or content revision.

Every original member path is retained. Every original nonimage member remains
byte-identical except `checkpoints/checkpoint_08_manifest.json`, which now records the actual packaged
file bytes. The original current manifest is retained, byte-for-byte, as
`checkpoints/checkpoint_08_manifest_original.json`. All historical checkpoint manifests remain unchanged.

All 840 crop images remain ordinary PNG files at their original
paths, in their original image modes and dimensions. Their PNG compression was
selected from the original encoding and level-9 zlib recompression of the
original filtered scanlines (default or filtered strategy). Pillow PNG
optimization was additionally evaluated for 53 images, as recorded
individually in the report; representative testing found same-filter zlib9
recompression smaller, so the remaining images did not repeat the Pillow step.
The smallest resulting DEFLATE payload was selected. For every image, the chosen
PNG was decoded and its mode, dimensions, and complete decoded pixel byte array
were compared directly with the original. There are **zero changed pixels**,
resizes, color conversions, quantization steps, or lossy encodings.

PNG encoded-file hashes may differ; decoded pixels do not. The encoding report
`checkpoints/checkpoint_08_lossless_encoding.json` maps every PNG's original and packaged SHA-256 hashes, original
and packaged byte lengths, exact decoded-pixel hash, mode, dimensions, selected
encoding, and candidate sizes. Historical image-byte hashes describe their
original snapshots; use the current manifest for this archive's encoded bytes.
The original binary ZIP was not altered, renamed, or removed.

## Verification and reproduction

`scripts/checkpoint_08_reencode.py` contains the complete script. It requires Python 3 and Pillow.
To verify this archive without the source ZIP:

```bash
python scripts/checkpoint_08_reencode.py --verify /path/to/SP38_CW_75_checkpoint_08.zip --checkpoint 08
```

To reproduce a retry from the original source ZIP, use distinct, nonexistent
destination and work paths:

```bash
python scripts/checkpoint_08_reencode.py --source /path/to/original/SP38_CW_75_checkpoint_08.zip --destination /path/to/new/SP38_CW_75_checkpoint_08.zip --work-dir /path/to/new/work --checkpoint 08 --skip-pillow
```

The script refuses overwrites, verifies source manifest hashes, compares all
decoded PNG pixels directly, verifies every packaged file hash and every PNG
pixel hash after ZIP creation, and exposes the final ZIP only after verifying
that it is below the native file-size limit. The archive uses standard DEFLATE,
so no additional decompressor or image-restoration step is needed.

Source ZIP SHA-256: `b70d88999edb522dd623664d86d6e888eaa09c926ad2d8df080dab7239130f2c`.
Encoding performed: 2026-11-20 05:39:38 UTC.
