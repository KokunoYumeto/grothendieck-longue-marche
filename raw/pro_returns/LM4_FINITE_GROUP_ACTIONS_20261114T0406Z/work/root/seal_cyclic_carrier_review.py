#!/usr/bin/env python3
"""Bind the complete root and peer audits of the cyclic-carrier construction."""
from pathlib import Path
from hashlib import sha256
import datetime
import json

ROOT=Path(__file__).resolve().parents[2]
def binding(name):
    raw=(ROOT/name).read_bytes()
    return {'path':name,'bytes':len(raw),'sha256':sha256(raw).hexdigest()}

author_name='work/part_c/compact_family_cyclic_carrier_control_result.json'
peer_name='work/part_d_attack/review_compact_family_cyclic_carrier_control.json'
scope_name='work/part_c/part_c_finite_group_and_discrete_quotient_scope.json'
expected={
 author_name:'6bf2058502bc5861a11c209bf51c160b71009681a65fec820cc4ebfed62190d6',
 peer_name:'87ebc8c1bf988d320366caacf28972d6d8f087e4766832d2a38d3e55beb61f43',
 'work/part_c/compact_family_cyclic_carrier_control.txt':'831ddb143a601a661107ca4f32c103d577267a8a9af330812f977684e6f46875',
 'work/part_c/compact_family_cyclic_carrier_control_report.txt':'6946da0ca7b80e519a08fc55adce057e7198e811839ba44b90046fa543449e76',
 'work/part_d_attack/review_compact_family_cyclic_carrier_control.txt':'27321fcc424bd5caa727dfb667ab5fd5b4f1bfd7d6d0d4dcb97e21b19869fbad',
 'work/part_c/part_c_finite_group_and_discrete_quotient_scope.txt':'55d8c9e63cbbbec1617a50eae1fbbee204ca6fb33322f773c0f9879a4805c1ad',
 scope_name:'22cc88acd4097b2aceae5dd2cceb9c07854db460f92f5306b12a24e1ce746589',
}
for name,digest in expected.items():
    assert binding(name)['sha256']==digest,name
author,peer,scope=[json.loads((ROOT/name).read_text()) for name in [author_name,peer_name,scope_name]]
assert len(author['dependencies'])==8
assert peer['result']=='PASS' and not peer['correction_requested']
assert not peer['author_files_modified'] and not peer['prior_frozen_files_modified']
assert len(peer['reviewed_author_files'])==3 and len(peer['matched_dependency_bindings'])==8
assert not peer['new_computational_test_claimed'] and not peer['new_render_review_claimed']
bound={}
routes=0
def verify(value):
    global routes
    if isinstance(value,dict):
        if all(key in value for key in ['path','bytes','sha256']):
            p=Path(value['path'])
            p=p if p.is_absolute() else ROOT/p
            name=str(p.relative_to(ROOT))
            actual=binding(name)
            assert actual['bytes']==value['bytes'] and actual['sha256']==value['sha256'],name
            bound[name]=actual
            routes+=1
        for child in value.values():
            verify(child)
    elif isinstance(value,list):
        for child in value:
            verify(child)
for value in [author,peer,scope]:
    verify(value)
for name in expected:
    bound[name]=binding(name)
for name in [
 'work/root/review_compact_family_cyclic_carrier_control.txt',
 'work/root/orbit_track_component_continuation_acceptance.json',
 'work/root/initial_fixed_region_continuation_acceptance.json',
 'work/root/prior_271_snapshot/binding.json']:
    bound[name]=binding(name)
record={
 'status':'ACCEPTED_UNNUMBERED_CONTINUATION_ROOT_AND_PEER_PASS',
 'sealed_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'numbered_claim_registered':False,
 'root_full_author_proof_lines_read':339,
 'root_full_author_report_lines_read':112,
 'root_full_author_metadata_read':True,
 'root_full_peer_report_lines_read':208,
 'root_full_peer_metadata_read':True,
 'root_scope_note_read':True,
 'mathematical_corrections_requested':[],
 'root_recursive_binding_routes_verified':routes,
 'accepted_domain':'The given compact connected based family in the original Q-centralizer, whose chosen actual evaluations lie on specified lifted cores of actual embedded annular or Mobius bands with infinite-order deck generator. Countable assembly retains pairwise disjoint bands and escaping chosen quotient points.',
 'accepted_maps':'Original band-cover coordinates and inverse; large-range shear and inverse; short-range interval maps and inverse; literal based correction; countable uniform paste and its full inverse.',
 'accepted_bounds':'Correction displacement <4eta, independent of winding count, and <2eta on the short interval; disjoint-band product tail <=8sup_tail eta; corrected-family tail B+omega_P^-(B) with the original inverse modulus.',
 'retained_target':'Controlled domain construction for arbitrary orbit traces, crossing carriers, remaining edges/cycles and a general noncompact cutoff for C.12.',
 'new_computational_test_claimed':False,
 'new_pdf_or_render_claimed':False,
 'binding_count':len(bound),'bindings':[bound[name] for name in sorted(bound)],
 'published_pdf_preserved':binding('work/root/prior_271_snapshot/binding.json'),
 'sealed_by':binding('work/root/seal_cyclic_carrier_review.py')}
out=ROOT/'work/root/cyclic_carrier_continuation_acceptance.json'
assert not out.exists()
out.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'status':record['status'],'binding_count':len(bound),
                  'acceptance':binding(str(out.relative_to(ROOT)))},indent=2))
