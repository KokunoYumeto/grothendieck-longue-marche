# Lossless crop encoding for delivery

The original scheduled ZIP exceeded the delivery service's 512 MiB file limit.
It was retained unchanged. This copy contains every artifact from that snapshot;
crop images use lossless WebP or JPEG XL when that is smaller than PNG. Every converted
image was decoded and compared byte-for-byte in its original pixel mode, with
unchanged dimensions. CROP_ENCODING.tsv records file and pixel hashes.

Qualified crops/<filename> references in reading records and reports were updated.
Exact bare filenames are updated only under the JSON keys viewed_crops and
crops_viewed, which identify files in the evidence crops directory. Historical
non-crops display paths remain exactly as recorded; those scratch previews were
not re-encoded. Sealed box lists, first- and second-reading TSVs, their hashes,
and all page and combined transcription files remain byte-for-byte unchanged.
The independent readings and their actual observations have not been altered.
These are image encoding changes, not newly cropped, resized, sharpened or
reinterpreted images. JPEG XL width and height were checked with ffprobe in
addition to the decoded RGB byte comparison.

Reader-record crop_sha256 fields retain the SHA256 of the original PNG container
bytes observed when the record was sealed. They are provenance hashes, even if a
live crops/ path now names a different lossless encoding; they are not hashes of
the stored WebP or JPEG XL bytes. CROP_ENCODING.tsv supplies original_file_sha256,
stored_file_sha256, and pixel_sha256 separately. Those original provenance hashes
are never replaced with a hash of a delivery encoding or a reconstructed PNG.

For continuing the original PNG-based workflow, run scripts/restore_png_crops.py
once after extracting this archive (Python/Pillow, ffprobe and FFmpeg with libjxl support
for any .jxl images). It restores the original pixel mode and
verifies the pixel digest, then reverses the filename references. Recreated PNG
container bytes may differ; their pixels do not. Do not rerun completed readings.
