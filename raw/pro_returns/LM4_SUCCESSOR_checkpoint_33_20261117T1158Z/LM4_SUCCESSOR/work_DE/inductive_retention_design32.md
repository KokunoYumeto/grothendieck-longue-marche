# Reconstructed exact31-to32 retention induction

This is a newly reconstructed design and source pair after the execution
environment was lost. It is not a recovery of the old04a739/408e77 byte
versions. The old `code/preserve_checkpoint_versions.py` is unchanged.

## Trust base and scope

The immutable parent is checkpoint31,526709584 bytes,
SHA98f1a6b74ae43dc4d09a1177a79c5e149fdf7530df52bc593964778172611d41.
Root previously completed the full archive/native verifications, recording
9388 logical entries and123532 completely covered historical keys. Its
exact bytes were restored. The new anchor pins the archived retention CSV,
summary, README, logical manifest, reader source, per-checkpoint counts,
and ordered five-field historical identity tuples. This is an explicitly
trusted induction base; it is not a new claim to have reopened archives1-30.

## The complete induction

Let R31 map every historical logical key from checkpoints1-30 to its identical
payload in31. Construct a TOTAL map f from EVERY logical31 path, including
R31 itself, its summary, all earlier proofs/data, and the31 manifest, to an
identical active or historical payload in32. Old keys are retained separately
with targets f(R31(key)). Add one row for each logical31 key. Equal bytes may
share storage only after exact comparison; their logical keys are never merged.
The resulting row count is123532+9388=132920, with zero omissions.

The producer streams the raw parent hash, uses the pinned native logical
reader, checks exact manifest coverage and all three TAR identities, and
checks every inherited row against actual parent payload metadata. It then
checks each chosen future target BYTE FOR BYTE against its parent payload.
It opens no archive1-30. The three mutable records must still equal their
archived31 bytes before publication and again immediately before replacement.
Their parent bytes always receive historical paths. A differing unarchived
current record is an error, not permission to overwrite it.

The parent-entry map and resulting CSV/summary/README hashes are recorded.
The certificate is written LAST, so its hashes witness a complete publication.
Existing different historical copies or prior publication records cause a
failure rather than silent replacement. A failed run may leave exact new
historical copies, but those are harmless and never erase earlier payloads.

## Closed-child verification

The separate verifier reopens the immutable parent and CLOSED child32,
validates their entire logical manifest/bundle contents, and reads the new
map/index/certificate FROM THE CHILD ARCHIVE. It checks total parent coverage,
all132920 actual child target payloads, the unmodified historical identity
tuples and their exact composed targets, and the new31 rows. Current mutable
workspace retention records are not evidence. The exact archived anchor is
also required. It prints a genuine result only when actually executed.

## Invocation and execution status

Producer: `python code/preserve_checkpoint_versions_inductive.py --commit`

Closed verifier: `python code/verify_checkpoint_inductive_retention.py`

Both accept explicit parent/anchor paths; the producer also accepts project
root. This version is deliberately bound to31->32. Neither helper has been
imported or executed during reconstruction. Root owns scheduling, packaging,
native TAR/64MiB checks, final capture, verification and delivery. A raw hash
of an older ZIP alone would not replace the pinned historical coverage premise.
