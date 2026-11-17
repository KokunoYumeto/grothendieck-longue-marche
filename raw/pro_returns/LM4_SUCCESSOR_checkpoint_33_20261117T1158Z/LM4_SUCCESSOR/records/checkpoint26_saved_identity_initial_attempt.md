# Preserved saved-identity verification attempt

The upload and the absolute-path apply-xattrs helper succeeded. A subsequent
inline verification used root=Path('.') followed by root.parent, which is
still a relative '.' rather than the project parent's absolute path. Its
first getxattr therefore raised FileNotFoundError for the basename
LM4_SUCCESSOR_checkpoint_26.zip. No archive byte or receipt was changed by
that failed verification.

The following delivery-record invocation then raised KeyError for
local_metadata_applied, since successful verification had not yet added
that field. Its original output/error files are retained under the suffix
initial_metadata_failure. No delivery record was appended by that attempt.

The repair is code/verify_checkpoint26_saved_identity.py, which derives the
absolute project root from its own file path, verifies every actual xattr
and the immutable archive size/hash, and only then normalizes the receipt.
The successful verification and delivery outputs are retained separately.
The failed relative-path attempt is not counted as a check.
