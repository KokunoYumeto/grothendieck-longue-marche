# V2 R1–R4 source correction closure

Closure time: 2026-11-21 04:26:30 UTC. Author: `/root/codec_v2`.

Root authorized the four bounded v2-only corrections after reading the independent review. All four corrections are saved. Both changed scripts were read in full (pack: 442 lines; restore: 260 lines), followed by both complete before/after diffs. Validation was limited to source reading and hashing; neither script was imported, compiled, tested, or executed.

## Closed source findings

| Finding | Saved correction | Source locations |
| --- | --- | --- |
| R1: audit overwrite | Resolve the audit destination once, reject source/output aliases and existing audit paths before source processing, then use exclusive `xb` creation for the final audit. The report uses the same resolved path. | Pack 200–210, 408–411, 420 |
| R2: restoration target collisions | Shared validation rejects empty target tuples, duplicate tuples, and file/descendant conflicts. Pack validates source entry names; restore validates the manifest. Temporary names use UUID4, are excluded from the complete original-target/implicit-parent set, and are created exclusively with cleanup. | Pack 232–234; restore 108–143, 193–194, 210–228 |
| R3: cache metadata type | A parsed value must be a dictionary before `get` is called. Other JSON result types continue the cache lookup and leave fresh encoding reachable. | Pack 129–131 |
| R4: repeated execution IDs | One UUID4 `execution_id` is sampled per build, recorded in the byte audit, and included in the event statement ID alongside the source hash and codec variant. | Pack 199, 344, 376 |

For R1, both reviewed alias assignments now reach a preflight exception; exclusive final creation also refuses a path that already exists at write time. For R2, `a.bin` and `./a.bin` produce the same tuple and are rejected. The temporary-path selection no longer derives the path `a.bin.restore-part` from `a.bin`, and its reserved-set check covers explicit entries and implicit parent directories. For R3, JSON `null`, arrays, and scalars reach the cache-miss branch before field lookup. For R4, the event and audit receive the same per-run variable.

## Exact source identities

| Source | Before SHA-256 | After SHA-256 |
| --- | --- | --- |
| `checkpoint_transport_pack_v2.py` | `02cad84a6fe1eddc4d30c2d5ef2e10605146dfaf9b82986aeb113f66eca46a35` | `5081b5e1141599b44c0c40c4d6c7cf1b76dd77536b4a4f0ef054349109830d93` |
| `checkpoint_transport_restore_v2.py` | `cf721c734b4591c034ce6dab9a25df5f1ad1eb583bb4fb452e04d0403a559b12` | `94a07fcae8d1697b977f5bd8a1883eeb685308cc4161acbfb0b66651883454fe` |

Complete copies before and after correction are preserved in:

- `out/checks/checkpoint_transport_v2_r1_r4_before/`
- `out/checks/checkpoint_transport_v2_r1_r4_after/`

Each directory contains both versioned script filenames. Their hashes match the respective before/after columns above.

Exact diffs are saved as:

| Diff | SHA-256 |
| --- | --- |
| `out/checks/checkpoint_transport_v2_r1_r4_pack.diff` | `59d8631e19a3a42ec43c7bed2632e7e6e88c3e7d5e71955fc2890a5787c5c808` |
| `out/checks/checkpoint_transport_v2_r1_r4_restore.diff` | `a247234b9482fa5f3013cd3e15d0ce23a77213dddaa992ba983feb740c25c27f` |

The v1 files remain unchanged:

- Pack: `4ea2ab7e5feb12944eeb785084c507ae900882b889062e6176494744474e5620`.
- Restore: `e00367d3a524a5d3bf607db494976858b0d634a868d0de93f8741e1548a422c5`.

The earlier preparation, root review, and independent review remain historical records of their stated hashes. This closure records the approved subsequent source changes.

## Scope and handoff

The changes leave the existing codec settings, candidate pixel/PNG comparisons, complete original-entry byte comparisons, and source size/hash checks in place. The full changed-source read found no additional issue within the four authorized corrections.

No image or manuscript was inspected. No codec, compilation, test, archive, rendering, research, installation, or upload operation was performed. No manuscript check event was created. No compression, performance, codec equality, mathematical, or ink result is claimed.

V2 remains unexecuted and unselected until a completed later v1 transport actually exceeds the cap. The saved sources, before/after copies, exact diffs, and this closure form the coherent handoff before the requested 2026-11-21 04:29:40 UTC writing cutoff.

