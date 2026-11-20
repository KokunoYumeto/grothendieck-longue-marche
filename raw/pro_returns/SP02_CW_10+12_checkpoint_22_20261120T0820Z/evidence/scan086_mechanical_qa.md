# Scan086 bounded mechanical QA

Checked: 2026-11-19 21:10:14 UTC.

**All requested bounded metadata and syntax checks passed.**

| Item | Result |
| --- | ---: |
| Finalized page bytes | 5002 |
| Asserted edit entries | 18 |
| Change records | 46 |
| Loci against C / H | 19 / 45 |
| Crop recipes | 45 |
| Inventory rows, all transcribed=yes | 91 |
| Root-authored JSON fields matching final record | 16 |

The finalized page hash matches its record and root's byte/count declarations. Strengthened metadata checks pass, including inventory identities and allowed fields. Inventory, collation and count projections agree. Crop IDs/references, coordinate geometry, transformation parameters and safe paths pass. Python AST and TeX lexical checks pass.

Root's JSON matches the finalized record after identity-type normalization. Protected page, record, root JSON and root script bytes remained unchanged.

**Scope:** no source-witness prose or image file was opened, including image headers. Source-C edit replay and crop bounds against image dimensions were not repeated. The source-C hash field was checked for valid form. No visual or transcription judgment is made.

| Input | SHA256 |
| --- | --- |
| Final page | `e24d183fa52cf182bda1aebbf144a663e1708ad17a9ece99cc094f8a125e78f1` |
| Final record | `5193ed6eb059cc2068634ff8bd3601a316fe74f4e3b7bc244b2902adb575983f` |
| Root JSON | `b90e267f256b0e5b85f770090a0d6619da212879d4de8662c912c08d00c399a2` |
| Root script | `c3b1239656d29119e81e1adbfbc58d43ab4c55c4dc357018f2f7139a7d46a2ec` |

The companion JSON retains detailed scope, hashes and diagnostics. No existing page, record or derived transcription report was changed. No context access, TeX compilation, live audit/freeze, packaging or upload occurred.
