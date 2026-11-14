# Extracting and verifying the archive

This is a standard ZIP. Large JSON and binary computation records use
lossless LZMA compression (ZIP method 14); the other members use deflate.
All mathematical sources, inputs, actual outputs, certificates and the
current paper's page images are ordinary ZIP members.

Python 3 extracts both compression methods with its standard library:

```sh
python -m zipfile -e LM7_FERMAT_TOWER.zip extracted
```

Historical QA images with identical bytes are stored once. The explicit
map in `ledger/archive_image_aliases.json` retains every original logical
path, byte count and SHA-256. To restore those duplicate image paths:

```sh
python extracted/LM7_FERMAT_TOWER/code/materialize_archive_images.py
```

The program checks every stored image before copying it, checks every
restored image, and refuses to overwrite a different file. It neither
resamples nor re-encodes any image. Running it again verifies the same
bytes. The optional `--verify-only` flag verifies an already restored tree.

`LM7_FERMAT_TOWER_manifest.json` describes the complete logical file tree.
For each file, `storage_path` names the member carrying its exact bytes.
It equals `path` for every file except a duplicate QA image. The packaging
program checks all physical ZIP CRCs and reconstructs every logical file
through this explicit map, checking its original size and SHA-256.

The image layout was also tested on all 999 images in the preceding saved
archive: all 237 duplicate paths were physically restored and every one of
the 999 complete byte strings matched its original. Its exact records are
in `code/root_archive_format/image_roundtrip224.json`. This removes repeated
image storage while preserving the entire recorded visual history.

Earlier ordinary ZIP packaging and its service-size rejection remain
recorded under `code/checkpoint224_integration/history/deflate_size_limit/`.
No research result, source, actual execution output or certificate was
removed to change the archive layout.
