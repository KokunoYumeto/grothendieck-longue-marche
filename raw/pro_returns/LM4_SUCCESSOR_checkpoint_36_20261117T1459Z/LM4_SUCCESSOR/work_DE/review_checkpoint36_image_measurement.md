# Complete source-only review: one image-dictionary measurement

**PASS.** I read the entire 209-line helper and its complete source manifest. I did not import or execute it. The archive identity is pinned to the actual immutable closed checkpoint35; the measurement creates no ZIP, TAR, extracted image or packaging change.

The actual archived 64MiB member payload is the baseline, not a re-encoding. The literal 30-byte native ZIP local-header structure is correctly indexed; its method, flags, CRC, compressed size, decoded size, filename and zero extra length are checked. The nine-byte method14 LZMA header supplies the actual dictionary. Exactly the archived compressed payload is hashed.

The same member is decoded once through ZipFile and fed directly, block for block, to one 128MiB standard-framed compressor. Independent decoded input and candidate round-trip SHA256, CRC32 and byte counts must match the pinned TAR identity. The candidate decoder must reach EOF without unused bytes, and its actual header must report the specified dictionary. Counts include the complete method14 prefix and flush output. No candidate stream or duplicate container is stored.

Before/after full archive hashing and compressor-helper/packager/source identities detect mutation. The output report is exclusively created after all checks; an earlier report blocks a rerun. The report explicitly limits the measured saving to the closed35 image member, with no assertion about future36 additions. The separate manifest records a read-only header observation; I do not represent that as my own observed run.

This is permission-neutral independent source review. Root/CE retain ownership of run authorization, genuine exit/output observation and any later packaging decision. No mathematical producer, measurement or private build/render was executed by this reviewer.
