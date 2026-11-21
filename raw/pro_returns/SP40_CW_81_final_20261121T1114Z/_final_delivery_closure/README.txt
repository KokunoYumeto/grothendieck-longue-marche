FINAL DELIVERY CLOSURE

All pre-existing selected-v2 members retain their order, bytes and ZIP metadata. The main CHECK_EVENTS.tsv remains exact.
Use ordinary unzip to access _final_delivery_closure/. RESTORE_CHECKPOINT.py restores/verifies only the raw snapshot entries in its unchanged manifest.
The v1 manifest is exact evidence. Every v1 /entries/{i}/storage/path resolves in the separately preserved v1 archive identified in reference_map.json; its WebP payloads are not added here.
The selected v2 manifest and payloads remain at their existing paths. Audit/event path strings are resolved explicitly by reference_map.json.
The cumulative supplemental CHECK_EVENTS.tsv begins with the exact original main table bytes, followed by the two completed events with explicit delegated attribution and one root packaging event. Exact raw per-version tables and reversible who-field changes are retained.
Original completed v1/v2 size/hash/gate fields describe their separately preserved original containers. The embedded root receipt describes completed pre-receipt comparisons. Finished delivery size/hash/gate results are external in out/checks/final_delivery_closed_file.json, measured after the last append.
Original raw/v1/v2 descriptors:
{
  "raw": {
    "path": "/workspace/scratch/94548b74fbe0/SP40_CW_81.zip",
    "bytes": 945737350,
    "sha256": "3892d7a09ac7209c7236e7760e12518ac9dcc9529be578746ddbe5b7d276cebb"
  },
  "v1": {
    "path": "/workspace/scratch/94548b74fbe0/persistent/SP40_CW_81.zip",
    "bytes": 618053120,
    "sha256": "1d4a59f6e0c51de93fea953d2f3ea33955f6b4025f670bae9952a9e192f17fbe"
  },
  "v2": {
    "path": "/workspace/scratch/94548b74fbe0/persistent_v2/SP40_CW_81.zip",
    "bytes": 521089588,
    "sha256": "cc297b0f7cafddfd6a7eea6326ed0ab0245486683167b0a2dd83c425421282ae"
  }
}
