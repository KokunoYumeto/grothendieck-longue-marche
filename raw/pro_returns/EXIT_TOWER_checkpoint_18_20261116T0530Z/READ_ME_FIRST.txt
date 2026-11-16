Complete exact checkpoint, resumable transfer format 3.
Extract all files, then run python3 restore_resumable_checkpoint.py . restored_checkpoint
Verify only: python3 restore_resumable_checkpoint.py . --verify-only
All original paths and bytes are restored, including duplicate files.
Independent XZ chunks and global exact PNG-row IDs are verified in their recorded order.
