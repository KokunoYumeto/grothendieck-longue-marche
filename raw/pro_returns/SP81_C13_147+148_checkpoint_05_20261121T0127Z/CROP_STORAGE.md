# Crop storage

Every crop is included at its original dimensions and with exactly its original pixel values. To fit the upload service’s 512 MiB limit, most PNG crops are stored as lossless WebP files with `.webp` appended to their original filename. They can be viewed directly. The original PNG filenames in the reading records remain stable identifiers.

`crop_storage_manifest.json` maps each original filename to its stored file and records the SHA-256 of the original PNG, stored WebP and pixel bytes. Every WebP was decoded and re-encoded as PNG before packaging; its reconstructed bytes matched the original PNG exactly. Files that do not pass that exact test remain PNG. No crop was resampled, recoloured, recropped, sharpened again or otherwise altered for storage.

To restore every original PNG after extracting this ZIP, run `python scripts/restore_crops.py` with Pillow available. The script verifies the original SHA-256 before writing and leaves existing matching PNGs alone. It refuses to replace a different existing file. The complete reading records and transcriptions are stored directly, without a storage transform. Earlier ZIPs remain unchanged.
