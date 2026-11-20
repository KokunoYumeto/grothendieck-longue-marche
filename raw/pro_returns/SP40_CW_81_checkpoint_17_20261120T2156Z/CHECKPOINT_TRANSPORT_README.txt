LOSSLESS CHECKPOINT TRANSPORT

Original snapshot: SP40_CW_81_checkpoint_17.zip
Original ZIP bytes: 637676806
Original ZIP SHA-256: 3fe194403ada1186217c3bbaab24fab7f48b3a712be563825a55e0f2c99d5aa4

This package contains every file from the identified original checkpoint. Ordinary non-PNG files retain their original paths and bytes. Some PNG files are represented by lossless WebP payloads and an exact-checked PNG restoration recipe. PNG files whose checks failed or whose payload did not shrink remain ordinary PNG files.

Restore all original files into an empty directory:
  python RESTORE_CHECKPOINT.py --archive SP40_CW_81_checkpoint_17.zip --destination restored_checkpoint

Verify all original file hashes without writing a restored tree:
  python RESTORE_CHECKPOINT.py --archive SP40_CW_81_checkpoint_17.zip --verify-only

The restoration script uses Python and Pillow. Creation and full byte-comparison verification used: {"libwebp": "1.6.0", "pillow": "13.0.0", "pillow_maxblock": 65536, "python": "3.12.14", "zlib_compile": "1.3.2", "zlib_runtime": "1.3.2"}
Each reconstructed file is checked against its recorded original size and SHA-256. A different software runtime is accepted only when those checks pass. The original ZIP container byte sequence is identified for provenance; restoration recreates the original file tree. The full entry manifest and compact finite byte comparison audit are in _checkpoint_transport/. No manuscript reading is performed by these scripts.

The original CHECK_EVENTS.tsv is preserved byte for byte with the other original files. The additional _checkpoint_transport/CHECK_EVENTS.tsv records this package's finite storage checks, which were completed after the original snapshot was fixed. Both event records belong to this delivery; the additional event does not alter the frozen transcription.
