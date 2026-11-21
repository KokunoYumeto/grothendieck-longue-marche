# Lossless crop storage

The upload service limits one file to 512 MiB. This ZIP therefore stores eligible PNG crops as lossless JPEG XL (`.jxl`). Every original crop is included; none was resized, discarded, sharpened again, or changed in colour. All text and all frozen reading TSVs are byte-for-byte unchanged. Earlier checkpoint ZIPs were not changed.

`CROP_COMPRESSION_MANIFEST.json` maps each original PNG name in the contemporary records to its archived image. It records both file hashes and the decoded pixel hash. Each converted crop was decoded and its original PNG regenerated; conversion was accepted only when the regenerated PNG matched the original PNG SHA-256 exactly. Any PNG that could not be reproduced exactly was retained as PNG. Thus this archive contains all data needed to recover every original crop file without the source scans.

To restore the PNG names used in the logs, from this extracted directory run:

```sh
python scripts/restore_crops.py
```

This requires Python, Pillow and FFmpeg with JPEG XL decoding. To restore one page or crop, append a filename fragment, for example `148_scan053`. Existing PNGs are checked and never overwritten with a different file. JPEG XL images can also be opened directly by compatible image viewers. The original PNG encodings were produced with Pillow; if another Pillow/zlib version produces different bytes, the restoration assertion deliberately stops instead of claiming a matching file. The JPEG XL pixels themselves remain exact and are independently verified.
