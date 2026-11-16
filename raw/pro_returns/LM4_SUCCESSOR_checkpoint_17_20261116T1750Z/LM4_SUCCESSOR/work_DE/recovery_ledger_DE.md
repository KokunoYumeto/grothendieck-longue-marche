# DE seventh-hour recovery ledger

Recovery date: 16 November 2026. The execution environment failed at approximately 07:43 UTC. Checkpoint 07 had not yet been archived. Root restored the verified checkpoint-06 archive into a replacement environment and released work on the restored tree. This ledger distinguishes exact restored data from mathematical reconstruction and fresh evaluation.

## Exactly restored inputs

All material present in the verified checkpoint-06 tree is retained unchanged unless an explicit later update is recorded. For the present recovery, the decisive exact inputs are:

- `work_DE/next_B59_image/common_base_braid_words.json`: the original common-base eleven-strand tetrahedral and cyclic words, whose geometry was certified in B61.
- `work_DE/rigid7_subsets.json`: all tetrahedral permutations, the chosen cyclic permutation and all rigid subsets.
- `work_DE/next_joint_rigid_symplectic/rigid_restrictions.json`: the previously computed plus/minus six-strand deletions and finite homology matrices.
- `work_DE/next_B56/membership_rigid7.py`: the exact free-word and faithful Artin-action implementation.
- B46--B64, all D/E statements, their checkpoint-06 register and primary bibliography, and the earlier Birman-stage programs present in the restored archive.

No seventh-hour file is described as byte-restored merely because its contents were retained in conversation.

## Reconstructed formal material

| Material | Present replacement | Recovery basis and verification |
|---|---|---|
| Complete B65 proof | `B_dihedral_rigid.tex` | Reconstructed from the accepted proof retained in conversation. Exact finite statements freshly re-evaluated against the original checkpoint-06 inputs. Source comment records reconstruction. |
| Complete B66 proof | `B_prounipotent_persistence.tex` | Reconstructed from the accepted strict-pointed Galois/eigenprojection proof. The primary Stacks and Hain--Matsumoto passages were reopened after recovery. Source comment records reconstruction. |
| B65/B66 register rows | `B_separability_results.csv` | Rewritten through the schema-preserving `recovery_update_DE.py`; no earlier rows discarded. |
| B66 bibliography | `B_separability_references.bib` | `DE_HainMatsumoto2003` and `DE_Stacks2026` restored with explicit Verified notes and freshly checked metadata. |
| Source/progress reports | `B_separability_source_log.md`, `report_DE.md` | Appended recovery-specific provenance and mathematical scope; existing checkpoint-06 records preserved. |
| Standalone review source | `B_separability_review.tex` | B65 and B66 inputs restored. The old PDF remains checkpoint-six output until a new build succeeds; the prior seventh-hour render is not represented as recovered. |

Root owns insertion into `sections/part_B.tex`, global bibliography assembly, independent review, the combined build, and archive retention. Those shared files were not edited here.

## Fresh executable certificates

The following programs were newly written and actually executed in the replacement environment. Their `.out` files are genuine new standard output. All three exited zero.

1. `next_joint_rigid_symplectic/check_B65_reconstructed.py` verifies the actual involution, its membership in T, both finite generated groups and their intersection, all 2+10 rigid sets and transports, the omitted-point comparison, all six exact braid deletions, purity, fixed-pair linking zero, and full-twist linking one. The six deletion words agree literally with the archived checkpoint-06 data. Complete output: `B65_reconstructed_certificate.json`, `cyclic_rigid_braid_words.json`, and `.out`.
2. `next_joint_rigid_symplectic/reconstruct_Q_birman.py` recomputes the simple filled meridian, both nonempty exact PB5 relations, the Nielsen coordinate change, both PB4 base-kernel images, the four-generator fiber basis, all three actual action automorphisms, and the antihomomorphism convention. It also checks all nine cross-collision multiplicities. Complete output: `Q_birman_reconstructed_certificate.json` and `.out`.
3. `next_joint_rigid_symplectic/reconstruct_final_fiber.py` recomputes the full six-strand last-fiber observations: the f1 push is conjugate to inverse total boundary; the [a,t] push survives killing that boundary. Its [c,f] row is explicitly a **new post-recovery calculation**: the corresponding original command failed before execution and had no old stdout to recover. Complete output: `final_fiber_reconstructed_certificate.json` and `.out`.

The fresh final-fiber lengths are respectively `(7,0)`, `(36,32)`, `(24,30)`, where each pair is `(push length, length after boundary filling)`. These are not a group-injectivity certificate.

## Unavailable original seventh-hour versions

The following original working files and outputs were not present in checkpoint 06. Their mathematical role is now covered by the replacements above, but their exact bytes and old timestamps are not claimed to survive:

- B65/B66's original `.tex` versions and their old standalone 37-page PDF, old build logs, page rasterizations and `qa_B65_B66.md`.
- `check_dihedral_labels.py/.out`, `dihedral_labels_certificate.json`, `verify_cyclic_kernel_comparison.py/.out`, `cyclic_kernel_comparison_certificate.json`, and the original format of `cyclic_rigid_braid_words.json`.
- `check_partial_root_arrangement.py/.out`, `partial_root_arrangement_certificate.json`.
- `single_collision_birman.py/.out`, `single_collision_birman_certificate.json`.
- `two_moving_action.py/.out`, `two_moving_action_certificate.json`, `simplify_two_moving_action.py/.out`, `two_moving_simplified_action.json`.
- `single_collision_fiber.py/.out`, `single_collision_fiber_certificate.json`.
- The post-checkpoint-six changes to the old `next_joint_rigid_symplectic/notes.md`; the restored file contains its checkpoint-six state. The new complete replacement research note is `Q_Birman_reconstructed_note.md`.
- Original independent B65/B66 review records written by other agents after checkpoint six, unless root or those agents separately reconstruct them. Their earlier acceptance is retained in conversation, but the old review-file bytes are not certified by this ledger.

## Remaining limits

The reconstructed proofs retain their accepted scopes. B65 does not prove theta5 injective or identify the completed kernel as an embedded closure. B66 does not construct a compact pro-ell or full profinite common element. The Q/Birman note supplies exact relations and actions; Q-to-PB5 injection and the final free-fiber/profinite comparisons remain open. The broader residual centralizer problem is unchanged by the recovery.

The replacement files require a fresh combined LaTeX build and visual QA. Old successful render statements refer only to the old environment and are not substituted for the fresh build.
