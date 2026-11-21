# Lossless crop encoding for delivery

The original scheduled ZIP exceeded the delivery service's 512 MiB file limit.
It was retained unchanged. This copy contains every artifact from that snapshot;
crop images use lossless WebP when that is smaller than PNG. Every converted
image was decoded and compared byte-for-byte in its original pixel mode, with
unchanged dimensions. CROP_ENCODING.tsv records file and pixel hashes.

All references to those specific crop filenames in reading records and reports
were updated. Sealed box lists, first-reading TSVs, their hashes, and all page and
combined transcription files remain byte-for-byte unchanged. The independent
readings and their actual observations have not been altered. WebP is an image
encoding, not a newly cropped, resized, sharpened or reinterpreted image.

For continuing the original PNG-based workflow, run scripts/restore_png_crops.py
once after extracting this archive. It restores the original pixel mode and
verifies the pixel digest, then reverses the filename references. Recreated PNG
container bytes may differ; their pixels do not. Do not rerun completed readings.
