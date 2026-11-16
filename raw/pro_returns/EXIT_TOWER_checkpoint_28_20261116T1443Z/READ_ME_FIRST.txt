Complete frozen original file tree, including all historical member paths and bytes.
python this_checkpoint.zip --verify-only
python this_checkpoint.zip --destination EMPTY_DIRECTORY
python this_checkpoint.zip --members-tar emits all verified original members for future preservation.
The original packager exclusions are recorded in package_manifest_*.json and the portable manifest.
All base chunks are contained here; no earlier checkpoint is required.
