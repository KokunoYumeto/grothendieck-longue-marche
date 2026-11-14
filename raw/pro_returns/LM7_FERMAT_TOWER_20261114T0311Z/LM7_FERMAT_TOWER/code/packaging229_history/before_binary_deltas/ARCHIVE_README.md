# Extracting and verifying the complete archive

This is a standard ZIP using deflate, BZIP2 and LZMA. Python 3 extracts all
three methods with its standard library:

```sh
python -m zipfile -e LM7_FERMAT_TOWER.zip extracted
python extracted/LM7_FERMAT_TOWER/code/materialize_archive_files.py
```

The second command restores every original duplicate binary-data and
historical-image path. It copies exact original bytes from a verified ZIP
member, checks the original byte count and SHA-256, and refuses to overwrite
a different file or follow a symlink. It does no numerical conversion,
binary reserialization, image resampling or re-encoding. Running it again
verifies the same files. The optional `--verify-only` mode only checks an
already restored tree.

All source programs, text transcripts, JSON records, documents and current
paper page images are ordinary ZIP members. Complete byte-identical copies
of `.bin`, `.npz` and `.npy` certificates/inputs and historical QA images
are stored once, with every original logical path recorded in
`ledger/archive_binary_aliases.json` and `ledger/archive_image_aliases.json`.
Different binary serializations remain different complete byte strings.
The compatibility utility `materialize_archive_images.py` restores only
the image aliases; the command above restores both kinds.

`LM7_FERMAT_TOWER_manifest.json` describes every original logical file.
Its `storage_path` names the ordinary ZIP member carrying that exact file's
bytes. It equals `path` for every file except an explicitly listed duplicate.
The packaging program checks all physical CRCs and reconstructs every
logical file through this map, comparing its whole original byte string,
byte count and SHA-256. The local author and review trees remain unchanged.

The binary layout was independently exercised on all 296 binary records
in the preceding checked archive. All 93 duplicate paths were physically
restored and all 296 complete files were compared with their original
bytes. Both restoration and a second verification-only execution passed;
escaping paths, symlinks and nonmatching existing targets were rejected.
The retained records are `code/root_archive_format/binary_roundtrip229.json`
and the complete verifier source and actual outputs. The preceding image
round trip likewise restored all 237 duplicate paths among 999 images.

The whole-byte codec benchmark and exact archive read-back records are
retained. Earlier packaging versions remain in the recorded history.
No research source, execution output, mathematical certificate or original
logical file is removed by this storage representation.
