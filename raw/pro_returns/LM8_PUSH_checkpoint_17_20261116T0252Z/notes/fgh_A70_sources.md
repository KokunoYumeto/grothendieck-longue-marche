# A70 source and proof ledger — registered

Registered as A.70 after full root and DE proof/source/exact-certificate audits PASS. Canonical section sections/A_all_dihedral_two_power.tex; code code/a_all_dihedral_two_power.py/.json/.out. Original audited draft and code remain preserved. The misleading automorphism-check comment was corrected before canonical copying, without changing executable mathematics; notes/fgh_A70_comment_precision.json records both hashes.

## Historical source ledger (preserved scope)

The proof and exact certificate are notes/fgh_A70_draft.tex and notes/fgh_A70_certificate.py/.json/.out. The exact certificate returned PASS. No frozen canonical section, bibliography or registered row was changed.

## Proved dependencies and actual maps

A4 gives the actual 2-isogeny formula from E_(a,b), its coordinates on the fixed E, and the geometric rank-two fundamental group comparison. A70 repeats these maps at every two-power m and independently checks all three polynomial identities in the certificate. Their dual-kernel images are computed directly by reducing t+a+b/t modulo t²+at+b. The stable map is precisely A44's actual cover; the two nonstable intrinsic marked curves satisfy A69. Their distinct dual kernels, rather than source-curve isomorphism classes, distinguish covering kernels over the identity of E.

The only external identity reused is dual-isogeny composition with multiplication by2: **verified:** Silverman, Arithmetic of Elliptic Curves, III.6.1–6.2, primary book https://www.math.ens.psl.eu/~obenoist/refs/Silverman.pdf , previously opened at the exact statements for A62/A64 and used in the independently proved A4. The new all-m generating-pair and Frattini arguments are proved algebraically in the draft. A44 gives potential good rank-zero reduction and actual4m-primary cusp divisors; A41/A42 and A59 give the final fixed and normalizer implications, with their finite-field-extension scope preserved.

## Exact support and limitations

The program verifies the universal degree2 isogeny and kernel translation as rational identities, all three target-E equations and dual kernels, and the three explicit automorphism orbits for m=4,8,16,32,64,128. It treats V4 separately. The proof gives the unbounded argument, so the finite orbit tests are support rather than an extrapolation. Norm maps, residue-degree-one point pushforward, characteristic rotation subgroup and actual intermediate comparisons are all written. This proves only dihedral two-power closures, not arbitrary nilpotent closures or products of two nonabelian Sylow factors.
