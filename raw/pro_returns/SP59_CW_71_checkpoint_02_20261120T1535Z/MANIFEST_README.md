# Archive manifest

MANIFEST.tsv lists each archived file's relative path, exact byte count, and SHA-256. The manifest itself is included in the ZIP but omitted from its own rows to avoid a circular hash. ZIP entries are written from the same captured bytes used to calculate the hashes.

ARCHIVE_HISTORY.tsv records capture names and UTC times. Earlier ZIPs are never embedded. It does not assert that a capture was durably saved; the primary reader verifies saving separately.

Source attachments, scans, crops, images, PDF files, old archives, JSON records, bytecode, caches, and hidden metadata are excluded. The archive contains the current deliverables, their tabular/Markdown records, and the scripts and documentation needed to continue from the supplied attachments.
