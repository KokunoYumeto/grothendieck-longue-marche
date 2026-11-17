# Checkpoint16 save recovery

The first bundled upload-helper invocation exited with status1. Its
observed tool stderr was exactly:

library upload failed: hosted apps tools/call request failed with HTTP status 401

Its stdout file was empty and is preserved separately. No successful
creation receipt was returned. The authenticated Library metadata list
and exact-title search returned no checkpoint16 item. The current helper
and all companion sources were fetched again in full; their contents
matched the earlier versions, so an identical blind helper retry was not
performed. No credentials were read, changed, or bypassed.

We completed the user-authorized hourly save through the available
authenticated native prepared-upload operations, preserving the same
prepared flow and exact archive bytes. Preparation returned the actual
workspace path as already transferred; the returned upload object was
passed unchanged to finalization. One creation succeeded. Complete native
result, returned xattrs, successful metadata-helper output and independent
Library metadata are preserved. This recovered a failed helper transport;
it did not switch to a direct-create write or create a second checkpoint.

LibraryID: libfile_fde3_f-2450cf07f61481918c5df39a003dbdc4_c6789dc4b4d481919ad633aabe6d84d0
FileID: file_00000000e7d482128db30ced65f425ef
Version: 0
Bytes: 443961139

The local identity/version attributes were checked against the returned
values. The archive SHA256 is still
d40f45ec4343ab3bfe1b6f428aba55d2e3cbee6b082412ece2fa0fff075f5c71.
The normalized receipt in checkpoint16_upload_result.json explicitly
records this recovery route; it is not misrepresented as helper stdout.
All these records are post-capture and enter17.
Recorded at 2026-11-16T16:56:20.102216+00:00.
