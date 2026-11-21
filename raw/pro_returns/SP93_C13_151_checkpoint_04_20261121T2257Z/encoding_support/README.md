# Lossless evidence encoding for SP93_C13_151_checkpoint_04.zip

This is an encoding migration of the supplied snapshot. No later working reports or readings were added.
Original ZIP SHA256: `07029dee522585aca1fa41cd31a2dea78a24ba7fbd7091713ff520b9306b3d23`; original bytes: 694387210.
Original scheduled checkpoint time: 2026-11-21T22:36:58Z.

## Pixel and text integrity

All 743 RGB PNG evidence crops are represented by lossless WebP counterparts. Every image was decoded and compared byte for byte in RGB, with unchanged dimensions. There was no resampling, grayscale conversion, quantization, or lossy encoding. The input crops had no ancillary Pillow metadata fields. The mapping, original PNG byte hashes, delivered WebP hashes, and decoded RGB hashes are recorded in `manifest.json`.

All 93 frozen first-reading, second-reading, box TSVs, and the first-reading manifest are byte-identical to the input. Original provenance scripts and TeX files are preserved byte for byte. Known crop filenames in 90 nonfrozen JSON/Markdown/CSV/TSV copies were changed to their delivered WebP counterparts. Recognized absolute crop paths were made relative to the archive root. Historical paths outside the converted crop inventory were retained. The exact original bytes of every reference-bearing file changed for delivery are retained under `reference_originals/`; their historical wording is recoverable exactly.

## View or continue the checkpoint

Evidence files are under `crops/` relative to the extracted archive root. Viewing them requires a WebP-capable image decoder. The encoder and verifier used Pillow 13.0.0 with libwebp 1.6.0. The transcription has not acquired an image-format dependency.

To verify a fully extracted checkpoint, run from its root:

```sh
python3 encoding_support/restore_png.py --root .
```

To recreate the original PNG filenames and restore the original reference text before continuing workflows that construct `.png` paths:

```sh
python3 encoding_support/restore_png.py --root . --restore
```

The restore helper requires Pillow with WebP support. It validates all files before changes, preserves the WebP files, and verifies the recreated PNG dimensions and exact RGB hashes. Recreated PNG compressed bytes may differ from the original PNG encoding; their pixel values are identical. Existing frozen reading files are never rewritten. Run the helper before editing the delivered reference-bearing reports; it rejects unexpected modifications to avoid replacing later work.

## Archive-level receipt

The adjacent `SP93_C13_151_checkpoint_04_encoding_receipt.json` records the original and delivered archive SHA256 hashes, sizes, verification counts, and frozen file hashes. A ZIP cannot contain its own final SHA256 without a self-reference, so that final digest is retained in the separate receipt and upload record.
