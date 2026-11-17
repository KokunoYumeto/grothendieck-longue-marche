# Complete source-only review of the four checkpoint36 retention helpers

Reviewer: /root/involutions. Result: PASS at the explicit source scope below.

I read the ENTIRE four current sources and all four complete checkpoint35-to36 diffs, without importing or running any helper, opening an archive, or publishing retention. The final anchor source is the corrected 324e2b6f version, whose predecessor is preserved. No helper was edited by this review.

## 1. Producer and historical coverage

The retention producer is bound to immutable parent35 and child36. It requires explicit --commit, streams and checks the parent archive identity against the pinned anchor, verifies the exact reviewed reader source, and validates every logical parent manifest entry and each of the three actual TAR payload identities. Duplicate logical names, malformed or unsafe paths, unlisted entries and mismatched hashes fail.

The parent check retains every historical identity tuple, including its checkpoint number, original archive/path, byte count and hash. It checks every inherited target against actual parent payload metadata, the historical counts, tuple digest, summary and omission-free key set. The new total is correctly 163040 inherited rows plus 10746 parent35 logical entries, namely 173786.

For each parent payload the target is an identical active path or an exact checkpoint35 historical copy. Conflicting existing history fails. Every future retained target is compared byte-for-byte with its actual parent payload before publication. Most importantly, the three mutable records must still equal their archived35 versions both before preservation and again immediately before publication. Thus an unarchived version cannot silently be replaced.

The inherited map is composed with the complete parent-entry map, preserving original identity tuples and all distinct keys. The new map, three mutable records and final certificate have explicit hashes. Each file uses a temporary fsynced write and atomic replacement; the certificate is written last as the publication marker. A partially interrupted publication is not represented as a successful complete transaction and a blind rerun is refused.

## 2. Closed-child verifier

The verifier reads the actual immutable parent35 and closed child36, not the current mutable retention table. It independently validates the full logical manifests and three bundles, compares the archived anchor literally, and verifies that the parent-entry map is total on all 10746 logical parent entries.

It checks every inherited tuple against the pinned parent rows in order, every composed target, every one of the 10746 added parent keys, and every final retained byte count/hash in the closed child. It checks all published summary/readme/map/index hashes and the exact 173786 count. No archive1–34 is reopened or falsely described as freshly decoded.

## 3. Final parent anchor

The final anchor source pins the actual parent35 identity, 530938760 bytes and SHA256 33b0925ca3ba12d8944fc47243807a3c61ebb2a4f03ec47f7bb2ce1a5a83f121. Its three verifier references are the actual declared sessions/chunks 19472/3e985f, 60334/1a39d7 and 29713/43e040.

The source checks the report identities, empty error files, all required success flags and exact counts. It then reads the already-existing observed-verification record and compares every evidence field with that record. It does not manufacture or overwrite an observation record. The archived parent records and reader are pinned from the actual parent archive, and the new anchor is created exclusively.

The final wording correctly distinguishes the freshly established parent34-to35 composition from the inherited archive1–33 trust base. The correction from 1–32 to 1–33 changes only that explanation, not runtime cardinalities or identities.

## 4. Independent native TAR verifier

The native verifier has no packager, TAR-builder or logical-reader import. Its selectors preserve the exact disjoint image, historical/preview document, and historical/large-JSON data coverage, with the current main PDF retained directly in the ZIP.

It checks method14 framing and actual local-header LZMA properties, requiring image dictionary 128 MiB and document/data dictionaries 64 MiB. This is a requirement for the future checkpoint36 archive, not a claim that a measurement or packager change has already happened.

The TAR audit rejects unsafe paths, duplicate members, nonregular/nonhardlink types, and hardlinks not pointing to an already validated regular member. Each actual container is extracted by system tar in its own temporary directory; all selected original paths are then checked for nonsymlink regular-file status, exact size and digest. The container identities and selected-path counts are also checked. The generic closed-archive verifier retains responsibility for the remaining direct logical entries.

This native verifier intentionally has top-level execution and must not be imported as a source-inspection technique. It was read as text only here. The other imported shared retention routines have their mutations under main guards.

## Scope

This review approves the complete current source logic and the exact bounded adaptation. It does not assert a successful anchor run, retention commit, archive creation, size measurement, native extraction, or closed-child verification. Those require root's separately observed executions. The accompanying JSON binds every current source, every old source hash, all complete diffs and the generation manifest.
