# Final history preservation and individual supersessions

The earlier plan to nest raw checkpoint ZIP containers is superseded by the complete, verified content/version history in `checkpoint_history/HISTORY_INDEX.json`. The original saved checkpoints remain unchanged. Every historical file entry has an exact retained object, an exact current-restoration reference, or an individually stated numerical-encoding replacement. All historical proof text, notes, logs, failures, source, register and PDF versions remain covered.

## Checkpoint containers

These ZIP wrappers are individually superseded by the corresponding complete entry lists in the history index; their file contents are accounted for there.

| Checkpoint | Original bytes | Original SHA-256 | Replacement |
|---|---:|---|---|
| 01 | 1972413 | `b602010151fbcdf97d030e12acf8e2fdcfeee21b65447a1350d0f9abab1c005f` | History index snapshot 01 and exact objects/restoration recipes |
| 02 | 4353440 | `484fe20be3252694c19eb5a7d344fe78f1a1714dd2b7311413343eed8a51f1e9` | History index snapshot 02 and exact objects/restoration recipes |
| 03 | 6453217 | `c0a36120eb256152cae4e981fb1a6a0ad920957685e6f95824077744c17f0164` | History index snapshot 03 and exact objects/restoration recipes |
| 04 | 9339571 | `f3997bacb74ca03034e2e7d33aef074a5d78fe50e4ea965365dd71b88779a44f` | History index snapshot 04 and exact objects/restoration recipes |
| 05 | 13916217 | `123377a0238737e82761135fdb1ff3377fd30c960ab4c748850de0a5b8dacea9` | History index snapshot 05 and exact objects/restoration recipes |
| 06 | 21410815 | `6b0b58b1532aee2d92d2b041097bdc3d5f5d902216b4608038b4fc71a69364e9` | History index snapshot 06 and exact objects/restoration recipes |
| 07 | 42078859 | `c95a8bec1907a52f9815f968ec58e93636dae2524948efea261873c47ccae3ae` | History index snapshot 07 and exact objects/restoration recipes |
| 08 | 143199183 | `608b2c06a31ec7713622996007619c746effa40a5b971d7373e9bfd9fbc508fc` | History index snapshot 08 and exact objects/restoration recipes |
| 09 | 452819526 | `8912a8371107ea4f23539e7fca4787076b331cdcbf4df7302571c48a9d726d02` | History index snapshot 09 and exact objects/restoration recipes |
| 10 | 499265878 | `05a72e4c5d5a5bdffe0902c46139a6177e8f12c50db75958651001be56177a19` | History index snapshot 10 and exact objects/restoration recipes |
| 11 | 237927769 | `19ac75b6d2b24af2d878a51ac1effa87b43895d390f890747141f539bed7fcc3` | History index snapshot 11 and exact objects/restoration recipes |
| 12 | 379557914 | `447503322b6e3d00279d4ecddd4fe6f6e8c25e32ee78d7691c781d55214d9e6e` | History index snapshot 12 and exact objects/restoration recipes |
| 13 | 443420670 | `fe8606c86d1c6b28e57abdd14d3cfcbb36863a5c86e2b763c6c99bebf82617f2` | History index snapshot 13 and exact objects/restoration recipes |
| 14 | 517938719 | `1e12a53edf5b0e733a2cfe1d6b7723f9382e25de108491bbda11557f815b0f87` | History index snapshot 14 and exact objects/restoration recipes |
| 15 | 529720458 | `b9f6b9d1b03f1b225f96c933da1d38ad828d27dabfebba48bf0f824c41baae59` | History index snapshot 15 and exact objects/restoration recipes |
| 16 | 524505491 | `44fd62846677a6be21f430b92ff08309584c3aced847e171db47875134a71285` | History index snapshot 16 and exact objects/restoration recipes |

## Individually superseded numerical encodings

| Checkpoint and original path | Original bytes and SHA-256 | Retained exact decoded replacement |
|---|---|---|
| 09: `code/pbc_iterated_modular_boundary_trace.jsonl.pbcbin.xz` | 190738772; `fe81239f57faed0032fe5ae5d0fee3a519d0cd537ad593e859e257e41e29e90c` | `code/pbc_iterated_modular_boundary_trace.jsonl`; first 1234834123 decoded bytes, SHA-256 `53ebf2c3c193e971f6b4ee9cef86f7ee1c9a85abf0a555db8085b8e9b673bb1b`. Identical fully verified decoded payload. |
| 09: `code/pbc_native_modular_v5_iterated_trace.jsonl.gz.pbcbin.xz` | 54249840; `e74d6f76dd9ccdb2b166d6b62581628f239162a07917de7b0609472e0d236510` | `code/pbc_native_modular_v5_iterated_trace.jsonl.gz`; first 296319427 decoded bytes, SHA-256 `ca7f29a6f44a09981ce0e22880667f77caf5da43d5dde826bb34a31150bf7d35`. Every decoded prefix byte hashed; exact historical verified payload hash matches. |
| 10: `code/pbc_native_modular_v5_iterated_trace.jsonl.gz.pbcbin.xz` | 300851744; `bcef823f187bd50ed8b15eadebbf9201aed4a6f90a05c19061c85cfd2cb5c204` | `code/pbc_native_modular_v5_iterated_trace.jsonl.gz`; first 1695013300 decoded bytes, SHA-256 `58b8deedbdc07df5591b5b2455ee7d59f5a94cf78d01ddaa51bcc509acf68739`. Identical fully verified decoded payload. |

Only these compression representations and the named ZIP wrappers are omitted from the history materialization. Their mathematical records are retained exactly as specified. This does not promote any unresolved mathematical claim.

Materialization checked all 24074 historical ZIP entries, retained 3236 distinct exact content objects, and checked 173 exact current-restoration dependencies. The packager may deduplicate identical content objects against current archive bytes, with an explicit copy recipe.
