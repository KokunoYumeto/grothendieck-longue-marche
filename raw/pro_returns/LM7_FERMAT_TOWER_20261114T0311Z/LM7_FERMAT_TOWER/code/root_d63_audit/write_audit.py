#!/usr/bin/env python3
"""Record the completed root D63 mathematical audit and actual complete replay."""
from pathlib import Path
import hashlib
import json

here = Path(__file__).resolve().parent
root = here.parent
author = root / 'D63_EXPERIMENTS'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
proof = author / 'sections/D_compact_orthogonal_cross.tex'
manifest = author / 'ledger/d_compact_orthogonal_cross_manifest.json'
assert sha(proof) == 'ee3649710aa1ec1bff151d9b8c9c5298f04cd6faa6815e0c93fc2264a1cbb789'
assert sha(manifest) == '91bace632be9d7fbad254e749e73b3c83e14165cd22bfaa847cc18c53a407786'
verification = json.loads((here / 'verification.json').read_text())
assert verification['status'] == 'PASS' and len(verification['complete_fresh_programs']) == 4
peer_file = root / 'bc_d63_audit/audit.json'
assert sha(peer_file) == '51c25b4865320f60cf89c4d9e8ee2925080e781843c2f6a46942629fd6581bbb'
peer = json.loads(peer_file.read_text())
assert peer['status'] == 'PASS' and peer['proof_sha256'] == sha(proof)
for name, value in peer['files'].items():
    assert sha(peer_file.parent / name) == value, name

review = '''# Root D.63 proof, source and full replay audit

**PASS.** Root read all 620 lines of the frozen section and all 617 lines of the four mathematical Python programs. The source-evidence and result/report ledgers, all four full replay records, and the independent peer's complete audit and exact execution scope were read. The frozen proof and author files remain unchanged.

## Integral compact comparison

The exact compact decomposition and its recorded order are essential. The old blocks are E0,E1,P0; the verifier checks that order against both actual affine embeddings and the small compact target before extracting matrices. The new embeddings and complements are checked by all stabilizer intertwiners. The full unordered Sylow calculations include coefficient conjugation. Independent norm vectors give an injective map from regular modules: every nonzero kernel has a two-group invariant, whereas the norm vectors are independent. Equality of dimensions then proves projectivity, and the odd-index trace and odd-character induction transport it to the full marked group.

Root checked the proof that the compact intersection form restricts perfectly to M. Multiplying its matrix by its actual inverse gives D'D=1-C'B. An invertible Fitting summand of C'B splits through the projective E*. Its occurrence contradicts the zero Sylow norm on the new complements or the disjoint projective top types on the old complements. Thus C'B is nilpotent modulo two; D is a unit on the integral free lattice. The displayed map psi(v)=v-i_M D^-1 C(v) is the precise isomorphism onto M-perp and has unchanged E coordinate.

All four Hom(P_*,E) coefficient systems have full rank128 over F4. Integral equivariant maps are repeatedly divisible by two, so separatedness proves their vanishing. The actual intersection adjoint therefore lands in M; its defining pairing identity proves theta_P(M-perp)=0. No unproved affine Hom vanishing is needed or used.

## Affine maps and the actual source

The literal cusp map sends a source loop of length36 to the cube of the target loop of length12. Every target cusp is reached and three is a unit over Z2. This gives the exact surjection ker(theta_U) -> ker(theta_P). Projectivity lifts each new compact inclusion inside L, the actual D.58 retained source kernel. Dual projectivity of the selected cusp lattice splits the affine sequence. The correction r'=r-sum(r j_a e_a pi) leaves the cusp retraction unchanged and makes its complementary section agree with the chosen extra inclusions.

The comparison Psi=1-e_old+j psi pi e_old has square-zero difference from identity: that difference factors through e_old and has image in its kernel. Hence Psi is invertible with inverse 1-(Psi-1). Its small-map image is unchanged, it fixes all cusp vectors, and it preserves the active moving module. Its exterior map transports each old selected image with precisely the same projector kernel. Consequently J62 is the same literal submodule.

The homology correction T63 has blocks diag(1,D) relative to eU and ker(e), retaining the actual small square. Inflation--restriction lifts the equivariant projection e to a continuous derivation because the coefficient lattice is projective over the finite group. The projective cyclic norm identity removes its t value and gives s and r coboundaries. The derivation factors through the full homology source J_infty and through Y. The formula beta_Y(g)=(A0 eta(g)) alpha62,Y(g) is a homomorphism with values in the actual abelian L kernel; its kernel and quotient maps in the D.58 fibre product are invertible. D.58.2 supplies actual S57 preimages of every conjugator change. Root freshly read the original onto-source proof D.58.1--10 and the full homology definitions D.50.1--7.

## Boundary and retained corrections

Root freshly read the unquotiented full cusp norm and punctured-surface orientation calculation D.55.10--12. It sums the actual length36 loops over all cusp cosets to give the whole group norm. The compactification kills the explicit cusp-factor errors. This calculation does not require a pre-existing compact-surface descent.

The new homology action is block diagonal on the proved orthogonal compact splitting. Both the orientation bivector and its image have zero extra/complement cross projection. The orientation identity therefore makes the compactified cross norm of the actual boundary zero. On each selected cross module compactification is injective and the complete norm map is an isomorphism. Its actual boundary class is consequently zero.

The D.62 source-involution and full length36 cusp corrections are transported through the equivariant graph. Their vectors stay in single extra summands, so their errors are self terms plus cusp factors and have zero new cross projection. The full wrap t^36 u t^-36 is retained. These exact D.62 identities were already fully root-audited and are reused with the displayed Psi transport. They remove all26 earlier self coordinates. The subsequent central augmentation correction is an actual source-conjugator change. The final action on Y is Int(b_t,Y) beta_Y, so the changed lower representative is expressly recorded. The D.57 action, its literal conjugators and the full W_h comparisons are retained through the original maps.

The identities e_i T63=e_i and mT63=D_c m give invariant cross-projector kernels and invertible image actions, including possible cusp terms in the affine complement. The class-two and full homology fibre products give the asserted actual X63 automorphism.

## Exact dimensions and independent execution

The four orbit contributions are8192/12,12288/16,12288/16,8192/8. Their sum is40960 central dimensions and52 coinvariants. Their first factor has zero small image, their second factor is killed by the previous extra projectors, and their support misses the D.59 support. Thus C63 lies in the literal J62 and J62=C63 direct-sum J63. The compact projectors separate the removed norm images, giving residual dimension284160, coinvariant dimension482, compact norm rank6 and kernel476. The source inverse image in R50 is explicitly given and remains nonzero. The original full profinite problem remains active.

Root ran all four complete sources in four fresh copied directories. Every complete stdout and JSON agrees after removing only the field elapsed_seconds. All source/input hashes are unchanged, all four actual exit codes are zero, and all stderr streams are empty. The frozen derived module input is copied exactly for dependent programs and its complete producer is independently replayed. No mathematical fields are excluded. Exact original/fresh hashes, commands, sources and outputs are retained in verification.json and fresh/.

The independent BC review covers the full proof and all four sources. Its separately written standard-library program checks all57 manifest entries, reconstructs four Hom systems as rank256 F2 systems, evaluates the full unordered Sylow norms, and reconstructs all245760 cross-action columns and all245760 norm-relation columns. Its whole execution and proof scope remains separate from root's full replay. Root verified the peer record and every artifact hash listed in it. Root does not claim to have rerun that peer program.

No new external theorem or bibliography status is introduced by D.63. Root makes no standalone D.63 PDF image-review claim here. The author reports six pages actually viewed; the integrated PDF will have its own actual visual review.
'''
(here / 'audit.md').write_text(review)
record = {'statement': 'D.63', 'status': 'PASS_FULL_PROOF_SOURCES_AND_ROOT_REPLAY',
          'proof_sha256': sha(proof), 'manifest_sha256': sha(manifest),
          'full_proof_lines_read': 620, 'all_four_source_lines_read': 617,
          'root_replay_record': {'path': 'verification.json', 'sha256': sha(here / 'verification.json')},
          'fresh_programs': 4, 'all_actual_exit_codes': [x['actual_exit_code'] for x in verification['complete_fresh_programs']],
          'only_replay_exclusion': 'elapsed_seconds',
          'peer_record': {'path': 'bc_d63_audit/audit.json', 'sha256': sha(peer_file),
                          'full_proof_and_source_scope': True, 'independent_focused_map_execution': True,
                          'root_reran_peer_program': False},
          'residual': {'central_dimension': 284160, 'coinvariant_dimension': 482,
                       'compact_norm_rank': 6, 'compact_norm_kernel_dimension': 476},
          'corrections_requested': [], 'original_D13_D19_remain_active': True,
          'root_standalone_visual_review_claimed': False,
          'audit_md_sha256': sha(here / 'audit.md')}
(here / 'audit.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps({'status': record['status'], 'audit_json_sha256': sha(here / 'audit.json'),
                  'audit_md_sha256': sha(here / 'audit.md')}, indent=2))
