#!/usr/bin/env python3
"""Record the root's completed D64 proof, source and replay review."""
from pathlib import Path
import hashlib,json

HERE=Path(__file__).resolve().parent
BASE=HERE.parent
AUTHOR=BASE/'D64_EXPERIMENTS'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
manifest_path=AUTHOR/'ledger/d_compact_isometry_source_manifest.json'
proof=AUTHOR/'sections/D_compact_isometry_source.tex'
assert sha(manifest_path)=='f83f88aa73247f28783661a5823f2ad08fb4479302ce61cf4d184f741e1fb357'
assert sha(proof)=='a08805a6e2d48e6f537f8bd0fc866ba80e91cf3605a305055b7638859ade2ab5'
m=json.loads(manifest_path.read_text())
for item in m['owned_files']+m['immutable_inputs']:
    p=AUTHOR/item['path']
    assert sha(p)==item['sha256'] and p.stat().st_size==item['bytes']
old=AUTHOR/'audit/pre_moving_repair/full_tree'
old_proof_lines=len((old/'sections/D_compact_isometry_source.tex').read_text().splitlines())
proof_line_delta=len(proof.read_text().splitlines())-old_proof_lines
old_manifest=old/'ledger/d_compact_isometry_source_manifest.json'
assert sha(old_manifest)=='9febb12df728919578ea892f7c76fdc20a6c31ec7da478d4e4ddba1dee7214b1'
om=json.loads(old_manifest.read_text())
for item in om['owned_files']+om['immutable_inputs']:
    p=old/item['path']
    assert sha(p)==item['sha256'] and p.stat().st_size==item['bytes']
unchanged=[]
for p in (old/'code').iterdir():
    if p.is_file() and p.suffix in ['.py','.out','.json']:
        assert p.read_bytes()==(AUTHOR/'code'/p.name).read_bytes()
        unchanged.append(p.name)
replay=json.loads((HERE/'replay.json').read_text())
assert replay['status']=='PASS_ROOT_SIX_COMPLETE_REPLAYS'
assert len(replay['programs'])==6
assert all(x['exit_code']==0 and x['stderr_bytes']==0 for x in replay['programs'])
peer=BASE/'bc_d64_audit'
peer_hashes={'audit.json':'e3c6a86f67f37bd8793d9824cb3ff3e09b96c4e4b1bed317a870319b0fe28552',
             'audit.md':'8b98d5806c16b534c378b71c3d1e3a41cc871ca478f3b40a980deeac2b935993',
             'code/focused_maps.py':'5234bd3d9f9680d0f79a15f5e8546e596df6b9dbc6971fcbcb05ff35b44ad3f1',
             'code/focused_maps.out':'937654404846c0317b5a414b1adb664c2d838d3f5a3b1c5ad808de1da4da5562',
             'code/focused_maps.json':'937654404846c0317b5a414b1adb664c2d838d3f5a3b1c5ad808de1da4da5562'}
for name,value in peer_hashes.items():assert sha(peer/name)==value
assert json.loads((peer/'audit.json').read_text())['result']=='PASS'
programs={str(p.relative_to(AUTHOR)):{'sha256':sha(p),'lines':len(p.read_text().splitlines())}
          for p in sorted((AUTHOR/'code').glob('*.py'))}
assert len(programs)==6 and sum(x['lines'] for x in programs.values())==1248
diff=AUTHOR/'audit/d64_post_word_moving_repair.diff'
assert sha(diff)=='613f4cdd303ec90f5c05da96eb0d115f7da473eb3ed172842f1e424c13a663df'
result={
 'statement':'D.64','status':'PASS_ROOT_FULL_PROOF_SOURCES_AND_REPLAY',
 'reviewer':'Root assistant; separate peer execution attributed to bc_d64_audit',
 'proof_path':'sections/D_compact_isometry_source.tex','proof_sha256':sha(proof),
 'proof_lines_read':len(proof.read_text().splitlines()),
 'proof_read_scope':f'All original {old_proof_lines} lines and the entire exact {proof_line_delta}-line-net post-word moving amendment; all final mathematical content read.',
 'manifest_sha256':sha(manifest_path),'owned_files_checked':len(m['owned_files']),
 'immutable_inputs_checked':len(m['immutable_inputs']),
 'mathematical_sources_read':programs,
 'dependency_read_scope':['D58 exact S57-to-L source surjection and both source-kernel inclusions',
                          'D58 full K=im(R50 intersect Lstar2) proof and augmentation equation D58.17',
                          'D63 exact moving and compact projector kernels, D63.8--11',
                          'Previously completed full D63 proof/source and four-program replay review'],
 'mathematical_review':[
   'The width36-to12 cusp map is multiplication by3 on the actual oriented loops. Its surjection and the affine exact sequence prove the saturated L-to-ker(theta_P) map, including reduction.',
   'The odd-averaged real wedge formulas give the Hermitian small comparison. Actual cusp-containing lifts prove the joint onto compact quotient; no splitting of J63 is required.',
   'The modulo4 incidence correction and signed half-ribbon pairing retain the original marked cycles. The degree3^93 normalized transfer supplies the exact pairing comparison with the arithmetic source.',
   'Both finite isometries have the actual small square and all stabilizer equations. Projectivity and saturated reduction lift their differences integrally, and the projective coefficient derivations give the literal peripheral source changes.',
   'All complete affine homology families and quadratic coefficients are retained. The two retractions intertwine every coefficient in both branches, proving stable kernels without choosing an unknown full homology action.',
   'Actual source-s words realize the eight correction columns and preserve Y. The full36 cusp word retains [t^36,u] and the actual affine translation of t^18.',
   'Root identified that the new source-s words can reintroduce moving terms. The amended proof cancels them afterward inside (1-e_Delta)K, using the actual R50 intersect Lstar2 source lifts, with all literal comparisons and new compact coordinates preserved.',
   'The unquotiented orientation identity, norm injections and actual augmentation corrections give boundary zero on the stated quotient. Exterior kernel preservation and the exact fibre product give its actual automorphism.',
   'The onto quotient has dimension1930 and14 coinvariants. The specified residual dimension is282230; the14 uncovered test coordinates are not asserted to be the residual coinvariant dimension.'
 ],
 'amendment':{'original_manifest_sha256':sha(old_manifest),
              'original_freeze_files_verified':len(om['owned_files'])+len(om['immutable_inputs']),
              'exact_diff_sha256':sha(diff),'unchanged_computational_files':unchanged,
              'effect':'Insert the necessary post-word moving-component correction through the proved exact source kernel.'},
 'root_execution':{'replay_json_sha256':sha(HERE/'replay.json'),
                   'complete_programs':6,'actual_exit_codes':[x['exit_code'] for x in replay['programs']],
                   'excluded_json_paths':['/summary/elapsed_seconds'],
                   'excluded_stdout_field':'elapsed_seconds','all_actual_outputs_retained':True},
 'peer_review':{'status':'PASS','hashes_verified':peer_hashes,
                'root_read_scope':'Complete peer audit, entire independently written324-line verifier, complete output and JSON; root did not rerun that peer program.',
                'scope':'Independent integral/marked pairings,288 semilinear equations,1024 norm columns,548 complete retraction coefficient matrices,576 source-basis wedges and integral source-word identities.'},
 'layout_scope':'Author final seven-page render and image evidence are retained. Root does not count author image review as root visual review; the integrated paper will have its own complete check.',
 'unresolved_original_scope':'D.13/D.19 full arithmetic boundary in the stated nonzero kernel and full profinite source realization remain active.'}
report=f'''# Root D.64 proof and execution review

**PASS for the amended frozen proof.** The root read every line of the
original{old_proof_lines}-line proof, the entire exact post-word moving amendment,
all1248 lines of the six mathematical programs, and the actual source
kernel and augmentation passages reopened in D.58 and D.63.

The marked compact quotient is onto through the actual cusp and homology
maps. The modulo-four cycle lifts compute the arithmetic intersection
form through its normalized odd transfer. The finite isometries lift
integrally through the saturated comparison kernel because the two
coefficient modules are projective. Their full-source derivations retain
the literal small and W_h conjugators. The two universal retractions
intertwine every coefficient of both complete affine action families,
which proves the required stable quotient kernels.

The root found a necessary ordering step in the original proof. The eight
source-involution words can introduce a moving central component before
odd averaging. The author preserved the complete original freeze and
inserted a correction immediately after those words. The exact moving
module is (1-e_Delta)K. Its coinvariants vanish, so the actual map
(b,d) -> (1-s)b+s(1-r)d is onto. D.58 identifies K with the image of
R50 intersect Lstar2; these same source lifts preserve Y, both literal
small conjugators, W_h, and every new compact quotient coordinate.
The final C1 augmentation correction then applies to the stated error.
The root read and checked this complete amendment against the original
source-kernel proof. All65 original frozen files and inputs are preserved;
all25 computational source/output/input files in that old code directory
remain byte-identical.

The root executed all six full mathematical programs in independent fresh
directories with exact copies of their immutable inputs. Every complete
stdout and complete JSON agrees with the author result after excluding
only the explicitly displayed elapsed_seconds values. All actual output
files remain unmodified. Every execution returned0 and every stderr was
empty. The127 final owned files and seven immutable inputs were checked
before and after these executions.

The separate peer independently reconstructed the integral incidence and
half-ribbon pairings, the actual649-dimensional small marking and branch
actions, four old isometries, all548 quadratic retraction coefficient
matrices,576 source-basis wedge images, and the integral involution and
full36 cusp-wrap identities. The root read the complete peer report,
its324-line program and full results and verified their hashes. This
peer execution is not described as a second root execution.

The reviewed theorem gives the actual1930-dimensional quotient,14 new
coinvariants, and the exact residual source kernel of specified dimension
282230. Its fourteen uncovered test coordinates retain their stated test
scope. The full arithmetic boundary and full profinite realization in
D.13/D.19 remain active. The author render is preserved separately from
the root's forthcoming integrated-paper visual review.
'''
(HERE/'audit.md').write_text(report)
result['audit_report_sha256']=sha(HERE/'audit.md')
(HERE/'audit.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':result['status'],'proof_lines_read':result['proof_lines_read'],
                 'source_lines_read':1248,'audit_sha256':sha(HERE/'audit.json'),
                 'report_sha256':sha(HERE/'audit.md')},indent=2))
