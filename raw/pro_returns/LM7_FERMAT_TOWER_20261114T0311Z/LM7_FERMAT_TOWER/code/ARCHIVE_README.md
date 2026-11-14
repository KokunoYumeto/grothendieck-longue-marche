# Extracting and verifying the complete archive

This is a standard ZIP using deflate, BZIP2 and LZMA. Python 3 extracts all
three methods with its standard library:

```sh
python -m zipfile -e LM7_FERMAT_TOWER.zip extracted
python extracted/LM7_FERMAT_TOWER/code/materialize_archive_files.py
```

The second command first reconstructs the explicitly listed binary files,
then restores every original duplicate binary-data and historical-image
path. It checks each complete original byte count and SHA-256 and refuses
to overwrite a different file or follow a symlink. It does no numerical
conversion, binary object reserialization or image resampling. Running it again
verifies the same files. The optional `--verify-only` mode only checks an
already restored tree.

All source programs, text transcripts, JSON records, documents and current
paper page images are ordinary ZIP members. Complete byte-identical copies
of `.bin`, `.npz` and `.npy` certificates/inputs and historical QA images
are stored once, with every original logical path recorded in
`ledger/archive_binary_aliases.json` and `ledger/archive_image_aliases.json`.
Selected distinct binary byte strings are represented by the exact
invertible transform in `ledger/archive_binary_deltas.json`. For a target
of length `n` and its nonempty complete base `b`, the stored delta is

```text
delta[i] = target[i] XOR b[i modulo length(b)]    (0 <= i < n)
target[i] = delta[i] XOR b[i modulo length(b)]    (0 <= i < n)
```

The delta has exactly the target's length. Each original target, complete
base and complete delta has its own byte count and SHA-256. Every base is
an ordinary ZIP member; delta chains are forbidden. The `.xor` payloads
are ordinary members under `archive_data/binary_deltas/`, compressed with
standard ZIP LZMA. Recovery applies the displayed inverse to the whole
original byte string. Distinct binary serializations retain all their
original bytes, including their headers and record boundaries.

The compatibility utility `materialize_archive_images.py` restores only
the image aliases; the command above restores all three representations.

`LM7_FERMAT_TOWER_manifest.json` describes every original logical file.
Its `storage_kind` explicitly selects `ordinary`, `alias`, or
`xor-repeated-base-v1`. For an ordinary file, `storage_path` equals `path`.
For an alias, it names the logical file with identical whole bytes. For a
delta, it names the physical delta; the record also gives the complete
base and all three byte counts and hashes. An alias can name a recovered
delta target. The packaging program checks all physical CRCs and
reconstructs every logical file through this typed map, comparing its
whole original byte string, byte count and SHA-256. The local author and
review trees retain their exact original content.

The delta benchmark checks all 86 selected targets by reconstructing and
comparing their complete original bytes; each compressed delta is also
round-tripped through ZIP LZMA. `code/root_archive_format/test_delta229.py`
executes the standalone decoder in a fresh tree, verifies every restored
target and alias against its entire original byte string, runs a second
verification-only pass, and exercises sixteen rejection cases. The
complete record is `code/root_archive_format/delta229_roundtrip.json`.

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
