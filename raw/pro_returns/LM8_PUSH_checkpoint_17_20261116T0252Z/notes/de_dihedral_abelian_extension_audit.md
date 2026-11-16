# Independent DE audit: dihedral times odd abelian closure

Status: **PASS** for the complete notes-only candidate `notes/fgh_dihedral_abelian_extension_draft.tex`, SHA256 `e1eb0ad55f805e94e77d70b10e2eed8823edaf73f5acae4683e9bd6aaa5c45ae`. This remains an unregistered consequence pending the parent's integration process.

## Primary check

Freshly opened and read Dupuy–Rabinoff, *A rigid analytic proof that the Abel–Jacobi map extends to compact-type models*, Theorem1.1 and exact setup, https://arxiv.org/pdf/1705.03034 , ref `turn1163view0`. The theorem supplies the relative morphism from the full compact-type model to its good relative Picard scheme, explicitly including nodes. Rational components are allowed; no closed-immersion conclusion is used. The ramified nilpotent tree input is the exact Lehr–Matignon6.13 scope independently verified in `de_A69_audit.md`, and A70's actual-cover classification was independently audited in `de_A70_audit.md`.

## Complete proof gates

- Every subgroup of a direct product of coprime finite groups splits by taking appropriate powers of each of its elements. This applies to the actual quotient kernel and the covering subgroup. Dihedral quotients are dihedral or abelian; the abelian closure cases extend to elliptic isogenies.
- The odd abelian cover extends across the puncture because the peripheral commutator dies in abelianization. The actual function-field compositum is a field: its two-power normal closure is linearly disjoint from the odd Galois isogeny extension. This proves connectedness of the actual pullback, not just degree counting.
- The odd isogeny extends between good elliptic models and is finite étale because its finite-flat kernel has order invertible at residue characteristic two. The source map extends through the compact-type Abel map and the actual Jacobian homomorphism. The resulting fibre product is a genuine semistable model of the actual connected generic curve.
- The proof correctly does NOT infer compact type from a finite étale map of semistable curves. It separately applies Lehr–Matignon to the actual nilpotent total geometric Galois closure over the good elliptic base, whose only possible branch section is O, then takes the actual norm quotient to the intermediate Jacobian. This supplies the tree condition after a finite extension.
- Each rational joining subtree in the original marked model maps constantly to O on the good elliptic special fibre. Its pullback under the finite étale odd isogeny is literally a disjoint union of copies, since the geometric fibre above O is reduced and discrete. The selected mark and a mark above the original distinct companion lie on the same copy; prime-to-two kernel sections have distinct reductions. Stabilization contracts only rational components and cannot insert positive genus into that path.
- A42 therefore applies to every cusp with the required rational companion path and global tree. A59 supplies normalizers from the nilpotent closure. The arithmetic descent uses only finite definition of the covering data and marked points; arbitrary geometric paths are handled up to inner conjugacy.

No new assertion about the special two-rank of the pullback Jacobian is made. The result covers dihedral two-power factors with odd abelian factors and their quotient closures/intermediates; it does not cover a second nonabelian Sylow factor. The argument is structural and does not need a new illustrative finite computation.
