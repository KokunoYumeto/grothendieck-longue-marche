# Mechanical delivery helpers

This folder contains no scan content or transcription content. No Library upload
or checkpoint is created by preparing these helpers.

## Small, single ZIP upload

For one new ZIP below 50 MiB, edit the two placeholder names in
create_one_library_file.exec.js and execute its entire contents in a single
functions.exec call. It confirms the path and byte size, calls the direct create
tool, then immediately invokes the maintained xattrs helper before yielding.

apply_library_writeback.py receives the full tool result, requires exactly one
Library identity, rejects conflicting metadata, sends the entire xattrs array
(or []) to library_file_transfer.py apply-xattrs, and saves a local JSON receipt.
If metadata parsing or writeback fails after upload, inspect the retained result
and repair metadata. Do not create another copy as a retry.

Use the returned file_name and path as authoritative. Keep the exact returned
library_file_id, file_id, and version. An edit of that item requires replacement
with its existing ID and retained concrete expected_current_version.

Final native file link:
https://chatgpt.com/library?file_id=EXACT_RETURNED_LIBRARY_FILE_ID&account_id=personal

## Larger ZIP or multiple independent files

The current maintained library_upload.py supports the prepared workflow and
applies returned local metadata itself. Supply one complete request and EOF:

python3 /workspace/scratch/b07ac00ff1ac/delivery_helpers_2a_fdpar/library_upload.py <<'JSON'
{"uploads":[{"local_path":"/absolute/path/ready.zip","purpose":"create_library_file","library_artifact_type":"other"}]}
JSON

Inspect every item in the ordered results array, including
local_metadata_applied. Do not call prepare_uploads/finalize_uploads manually
or switch a started helper operation to direct creation.

## TeX syntax check

Run:

python3 /workspace/scratch/b07ac00ff1ac/delivery_helpers_2a_fdpar/check_fragment.py /absolute/path/body_fragment.tex

The checker does not edit its input. It creates an isolated XeLaTeX format, a
wrapper, and logs under texqa. It bypasses the installed TeX tree's missing
filename database through a local TEXMF setting. It disables shell escape and
creates XDV instead of PDF; this avoids requiring PDF font-map configuration.

The wrapper loads amsmath, amssymb, tikz-cd, and geometry. Annotation commands
are neutral wrappers. diagram and figure do not pre-collect their arguments,
which lets tikz-cd change ampersand catcodes correctly. Metadata commands
cotefile, scanpage, and mspage discard their one argument.

This validates parsing and macro availability, not transcription correctness,
typography, or diagram fidelity. It does not validate that custom annotations
have the right semantic arguments.

synthetic_fragment.tex is artificial test content only. It compiled with exit 0.

## Provenance

library_file_transfer.py, library_hosted_apps.py, and library_upload.py were
downloaded completely and unchanged from the current c0/library skill resources
during this request. Their source directory is private (mode 0700).

