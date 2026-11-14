# Extracting and verifying the archive

The archive is a standard ZIP. Large JSON and binary computation records use
lossless LZMA compression (ZIP method 14); the other files use deflate.
Every file retains its original name and exact uncompressed bytes.

Python 3 can extract both methods with its standard library:

```sh
python -m zipfile -e LM7_FERMAT_TOWER.zip extracted
```

The file `LM7_FERMAT_TOWER_manifest.json` records each member's byte count and
SHA-256. The packaging program reads back every member, checks these hashes,
and runs the archive CRC check. The earlier deflate-only archive and its
successful validation are identified in
`code/checkpoint224_integration/history/deflate_size_limit/`; its upload failed
because it exceeded the service's size limit. That failure changed no research
result or source document. The present compression change preserves every
historical rendering, source, actual output and certificate.
