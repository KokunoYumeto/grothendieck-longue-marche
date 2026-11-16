# Exact encoded-leaf prefix patch

**PASS**, 2026-11-15, after checkpoint12 was saved. This is storage work only; C31 remains Open.

The checkpoint11 leaf payload has28,897,004 encoded bytes, SHA2567502d8796b075d439203e87edc4cae3734547f04b66ba7f4125c67cfe4560021. Its first28,879,072 bytes are byte-identical to the encoded checkpoint12 payload. The remaining17,932 bytes are retained verbatim in code/pbc_checkpoint11_leaf_prefix_tail.bin.

The patch therefore copies an exact encoded prefix and appends the exact old tail. It reconstructs the original XZ wrapper and payload byte for byte, with no recompression, numerical approximation or dependency on a future LZMA implementation. The immutable old and new files remain unchanged.

The first verification constructed the result while comparing every prefix block and the complete retained tail against the old encoded file, and checked the final length/hash. The second verification copied the helper, recipe, tail and new source into a separate self-contained archive layout, executed code/pbc_restore_encoded_prefix_patch.py there, and compared every resulting byte with the old file again. Both passed. The exact command, original and reconstructed hashes, helper hash and recipe hash are in code/pbc_checkpoint11_leaf_prefix_patch_verification.json.

The helper resolves inputs relative to its extracted archive, verifies the full source and tail hashes before restoration, refuses to overwrite its target, and verifies the restored hash/count. Its only runtime dependency is standard Python. The recipe and retained tail are included in the project.

The generic transform entries in code/pbc_checkpoint11_leaf_prefix_patch_transforms.json cover both old operational aliases. They have kind=raw_bytes because the byte object being restored is itself the original encoded leaf XZ file. A package preparer must apply the same verified representation to any historical content object identified by that old hash, and must retain the checkpoint12 source payload. No prior checkpoint is modified by this new representation.

