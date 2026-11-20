LOSSLESS CHECKPOINT TRANSPORT

Original snapshot: SP40_CW_81_checkpoint_13.zip
Original ZIP bytes: 570084149
Original ZIP SHA-256: 9d4b81369836f36021ae58df11937f3a96ef361505facaba12e07d83f4bb97b4

This package contains every file from the identified original checkpoint. Ordinary non-PNG files retain their original paths and bytes. Some PNG files are represented by lossless WebP payloads and an exact-checked PNG restoration recipe. PNG files whose checks failed or whose payload did not shrink remain ordinary PNG files.

Restore all original files into an empty directory:
  python RESTORE_CHECKPOINT.py --archive SP40_CW_81_checkpoint_13.zip --destination restored_checkpoint

Verify all original file hashes without writing a restored tree:
  python RESTORE_CHECKPOINT.py --archive SP40_CW_81_checkpoint_13.zip --verify-only

The restoration script uses Python and Pillow. Creation and full byte-comparison verification used: {"libwebp": "1.6.0", "pillow": "13.0.0", "pillow_maxblock": 65536, "python": "3.12.14", "zlib_compile": "1.3.2", "zlib_runtime": "1.3.2"}
Each reconstructed file is checked against its recorded original size and SHA-256. A different software runtime is accepted only when those checks pass. The original ZIP container byte sequence is identified for provenance; restoration recreates the original file tree. The full entry manifest and compact finite byte comparison audit are in _checkpoint_transport/. No manuscript reading is performed by these scripts.
