#!/usr/bin/env python3
"""Append the finite-overlap acceptance after complete root and peer review."""
from pathlib import Path
from hashlib import sha256
import datetime,json

ROOT=Path(__file__).resolve().parents[2]
def binding(name):
    raw=(ROOT/name).read_bytes()
    return {'path':name,'bytes':len(raw),'sha256':sha256(raw).hexdigest()}
author_name='work/part_c/compact_family_finite_overlap_carriers_result.json'
peer_name='work/part_d_attack/review_compact_family_finite_overlap_carriers.json'
expected={
 author_name:'d8b3e83e17cb10438fdf643f2d16df2929db063013f348750200f35ea706df08',
 peer_name:'92b49773c5101abd99ecd2332524ae2f29085af8fc7226be222a008c841e0a14',
 'work/part_c/compact_family_finite_overlap_carriers.txt':'60926747d78481b27ef939cba440264f9574e40253fa660f4f7671b791a70795',
 'work/part_c/compact_family_finite_overlap_carriers_report.txt':'f4682844b1053efbb71decb7484013b2c41e4a5bfd4c7f63352b27568474b76e',
 'work/part_d_attack/review_compact_family_finite_overlap_carriers.txt':'269be4e79ae7ec41b15d54815c6a637e7fb70cb5575f1f777714c3d757abdec3'}
for name,digest in expected.items():assert binding(name)['sha256']==digest,name
author=json.loads((ROOT/author_name).read_text())
peer=json.loads((ROOT/peer_name).read_text())
assert len(author['dependencies'])==14 and len(peer['bound_inputs'])==17
assert peer['verdict']=='PASS' and not peer['correction_requested']
assert not peer['read_scope']['author_files_modified']
bound={};routes=0
def verify(value):
    global routes
    if isinstance(value,dict):
        if {'path','bytes','sha256'}<=set(value):
            p=Path(value['path']);name=str(p.relative_to(ROOT)) if p.is_absolute() else str(p)
            actual=binding(name)
            assert actual['bytes']==value['bytes'] and actual['sha256']==value['sha256'],name
            if value.get('lines') is not None:assert len((ROOT/name).read_bytes().splitlines())==value['lines'],name
            bound[name]=actual;routes+=1
        for child in value.values():verify(child)
    elif isinstance(value,list):
        for child in value:verify(child)
verify(author);verify(peer)
for name in [*expected,'work/root/review_compact_family_finite_overlap_carriers.txt',
             'work/root/initial_fixed_region_continuation_acceptance.json',
             'work/root/orbit_track_component_continuation_acceptance.json',
             'work/root/disjoint_trace_carrier_continuation_acceptance.json',
             'work/root/cyclic_carrier_continuation_acceptance.json',
             'work/root/prior_271_snapshot/binding.json']:
    bound[name]=binding(name)
record={
 'status':'ACCEPTED_UNNUMBERED_FINITE_OVERLAP_CARRIER_ROOT_AND_PEER_PASS',
 'sealed_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'numbered_claim_registered':False,
 'root_complete_author_proof_lines_read':356,'root_complete_author_report_lines_read':97,
 'root_complete_peer_report_lines_read':245,'root_substantive_author_and_peer_metadata_read':True,
 'recursive_binding_routes_verified':routes,
 'accepted_domain':'The original compact connected based finite-CW family after IFR, with its relative-X component witness, without an extra disjoint-trace or cyclic-overlap premise.',
 'accepted_maps':['Actual finite overlap set S and subgroup H, original parameter rose and endpoint multiplication.',
 'Exact components qHA, discrete Q/H labels, stabilizer H and the homeomorphism HA/H to pi(A).',
 'Exact overlap preservation under filling and small Jordan neighborhoods.',
 'Original subgroup-cover section over pi(int D1) through H int(D1)/H.',
 'Uniform local balls, explicit inverse iterations, Q-pastes and the ordered finite product.',
 'Correction G^-1 h, inverse h^-1 G, original inverse modulus and ordinary relative witness.'],
 'accepted_bound':'B=n diam_eQ(D1) with the actual n from mu(1/n)<r/3; D_e(G^-1 h,h)<=B+omega_P^-(B).',
 'accepted_counterexample':'Actual radial-cylinder traces have radius <=2/(n+1), overlap group Q=Z and saturated component e_Q-diameter exactly 2.',
 'unbounded_selected_subdivision_sequence_claimed':False,
 'accepted_tail':'Both directions agree outside the full lift of pi(D1) union all b_u^-1(pi(D1)).',
 'retained_target':'A general ambient bound tending to zero with the original tail, compatible edge/cycle stages and infinite deformation.',
 'corrections_requested':[],'new_code_or_numerical_experiment_claimed':False,
 'new_primary_theorem_imported':False,'new_pdf_or_render_claimed':False,
 'binding_count':len(bound),'bindings':[bound[name] for name in sorted(bound)],
 'sealer':binding('work/root/seal_finite_overlap_carrier_review.py')}
target=ROOT/'work/root/finite_overlap_carrier_continuation_acceptance.json'
assert not target.exists()
target.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'status':record['status'],'binding_count':len(bound),
                  'acceptance':binding(str(target.relative_to(ROOT)))},indent=2))
