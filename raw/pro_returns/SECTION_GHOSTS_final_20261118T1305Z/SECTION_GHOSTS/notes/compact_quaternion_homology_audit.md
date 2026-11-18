# Exact faithful-homology reconstruction (E207)

The separate proof is in `sections/part_E_compact_quaternion_homology.tex`. The new independent script and its JSON/stdout are `code/check_compact_quaternion_homology.py`, `.json`, and `.out`. Full independent reviews are now positive as recorded below. E203–E204 remain stable.

The script first reruns the complete in-run compact detector in a temporary directory and verifies its exact digest, then constructs the actual72-sheet Cayley cover with rank73. It retains every Schreier word, rather than importing the historical basis. The exact Theta14×73 has rank12, and all brackets of its generator images vanish. The quaternion projectors have ranks37 and36. The actual augmentation-square image on the faithful36-space has rank24 and is precisely the kernel of its rank12 map. A literal primitive idempotent gives an18-space with rank12 kernel and rank6 image.

All36 peripheral words are reconstructed from the commutator's actual order-two deck label; their homology span has rank35 and is killed. Four complete surface-action intertwining equations are checked. The characteristic common source and its exact order288·3^36 are proved from the unique quaternion involution and the exponent lattice, and the epimorphism is induced by the identity of the free group.

Final payload SHA256: `e7c5ff2b43bcc8239a94c56b2b2fc04d7329a367c3c109c433d96549f6657ab5`. No historical matrix or program output is imported. All finite arithmetic uses exact F3 operations.

This closes the specific missing faithful-module certificate for A4.18. It does not supply the unavailable numerical BCV/HCF/KFU functions or their bounded same-parameter comparison. The broad historical A4.57 row remains pending, and this finite-input improvement is not recorded as a broad historical-row closure.

## Independent review

Ghost completed a full proof and complete code/dependency review and independently reran the exact copied program, reproducing both payload digests. Its two scoped events are already in `notes/ghost_audit_CHECK_EVENTS.tsv`; they are not duplicated in this subsection's event file. Root completed the full proof and complete program read, recorded in `notes/root_eighth_check_events.tsv`. That event is a proof/code reading and does not claim an additional root rerun. The earlier partial root-review event remains as a dated activity record.
