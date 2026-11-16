Complete exact original source ZIP member set.
python this_checkpoint.zip --verify-only
python this_checkpoint.zip --destination EMPTY_DIRECTORY
python this_checkpoint.zip --members-tar emits every original source member.
This self-contained wrapper carries complete validated parent chunks, including unreferenced internal blobs.
Every carried raw blob, encoded blob, row/counter, chunk and runtime file is checked before verification succeeds.
Unreferenced internal blobs create no additional restored source paths. No parent checkpoint is required.
The original byte-for-byte source ZIP comparison is pinned in CHECKPOINT_RESUME.json.
