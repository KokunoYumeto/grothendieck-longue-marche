# Exact revision872 snapshot book authority — staged

This proposal admits exactly the seven PDFs preserved by the already completed revision872 snapshot. The full snapshot identity, complete seven PDF rows, and captured stable/build/source-freeze metadata are fixed in `SNAPSHOT_AUTHORITY.json` and embedded in the standalone recovery helper. No generic snapshot, basename, same-hash, or fallback authority is added.

The validator joins each PDF to its exact historical reader, original publication path, preserved path, byte count, SHA256 and page count. It reads the exact captured stable/build/freeze records and all sixteen captured source/assembly dependencies. Metadata names and actual bytes are verified. PDF content remains subject to the existing collection and reconstruction byte gates; this new validator supplies named-book authority, not a replacement content check.

The package hook runs before delta generation or image proof, adds only those seven validated rows to the existing named-book catalog, and stores the identical explicit descriptor declaration. The standalone restorer validates that declaration before admitting a matching delta target. Archives without the declaration retain their existing authority behavior. The qualifier, codec, primitive-base rules, target ceiling23,64MiB bounds, aliases and PNG/native/overview code remain unchanged.

This stage is separate from final-PDF exclusion policy. No active helper or registry is modified. Actual metadata controls use the immutable historical snapshot and its captured text/code records; no PDFs, rendering, generation, collection or restoration are run by the controls. The small gate fixture isolates authority admission and does not claim a complete archive execution.

After independent review, root may install only the exact two proposed helper copies if their active before hashes still match. A later actual checkpoint must repeat all existing privacy, collection, exact delta/PNG proofs, size and complete standalone-recovery gates.
