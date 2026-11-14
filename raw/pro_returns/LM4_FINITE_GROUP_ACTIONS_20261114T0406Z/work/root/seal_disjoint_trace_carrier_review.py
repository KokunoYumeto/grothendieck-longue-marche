#!/usr/bin/env python3
"""Seal the original disjoint-trace carrier proof after complete root/peer review."""
from pathlib import Path
from hashlib import sha256
import datetime,json

ROOT=Path(__file__).resolve().parents[2]
def binding(name):
    raw=(ROOT/name).read_bytes()
    return {'path':name,'bytes':len(raw),'sha256':sha256(raw).hexdigest()}
author_name='work/part_c/compact_family_disjoint_trace_carriers_result.json'
peer_name='work/part_d_attack/review_compact_family_disjoint_trace_carriers.json'
expected={
 author_name:'928c900d0976aff87d7cea51a7ab4a09459a2f284cb10d1323cecd9cf5d48614',
 peer_name:'58b790e25eeb4199e216a6c1e8f5a97712160e36ce02d2cc36138fb659531011',
 'work/part_c/compact_family_disjoint_trace_carriers.txt':'796455fe1a9f1f1c5a424971f019f45ec4d6b7dfeefd8610cf9c287c0aa8d9eb',
 'work/part_c/compact_family_disjoint_trace_carriers_report.txt':'eb6aca2899ffcdb04c1a303c7f13e448a940b8ca209cbfaec8e72838301522a0',
 'work/part_d_attack/review_compact_family_disjoint_trace_carriers.txt':'c7987a4173fc6e94b755cf5fc96186d89ff37bd7da039630eaa2161076e89dab'}
for name,digest in expected.items():assert binding(name)['sha256']==digest,name
author=json.loads((ROOT/author_name).read_text())
peer=json.loads((ROOT/peer_name).read_text())
assert len(author['dependencies'])==13 and len(peer['bound_inputs'])==16
assert peer['verdict']=='PASS' and not peer['correction_requested']
assert not peer['verification']['author_sources_modified']
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
for name in [*expected,'work/root/review_compact_family_disjoint_trace_carriers.txt',
             'work/root/initial_fixed_region_continuation_acceptance.json',
             'work/root/prior_271_snapshot/binding.json']:
    bound[name]=binding(name)
record={
 'status':'ACCEPTED_UNNUMBERED_DISJOINT_TRACE_CARRIER_ROOT_AND_PEER_PASS',
 'sealed_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'numbered_claim_registered':False,
 'root_complete_author_proof_lines_read':293,'root_complete_author_report_lines_read':97,
 'root_complete_peer_report_lines_read':202,'root_substantive_author_and_peer_metadata_read':True,
 'recursive_binding_routes_verified':routes,
 'accepted_domain':'The original compact connected based finite-CW family after IFR, with its relative-X component witness and its actual evaluation trace disjoint from all nonidentity original Q-translates.',
 'accepted_maps':['Exact disjoint fills and finite shrinking of the actual translated neighborhoods.',
 'Nested original Jordan carriers and the literal retraction of the original lifted track.',
 'Explicit bump translations and their uniformly convergent inverse iteration.',
 'One-carrier finite product, actual Q-paste and original-circle extension.',
 'Correction H=G^-1 h, inverse h^-1 G, and ordinary relative witness k=g^-1 Bprime.'],
 'accepted_bound':'Both full correction displacements <=B_v=diam_eQ(D1)<2eta(pi(v)), independent of subdivision count; D_e(H,h)<=B_v+omega_P^-(B_v) with the original inverse modulus.',
 'accepted_tail':'Both input directions agree exactly outside the full lift of pi(D1) union all b_u^-1(pi(D1)).',
 'retained_target':'General actual overlap-subgroup carriers, compatible edge/cycle stages and the global infinite deformation.',
 'corrections_requested':[],'new_code_or_numerical_experiment_claimed':False,
 'new_primary_theorem_imported':False,'new_pdf_or_render_claimed':False,
 'binding_count':len(bound),'bindings':[bound[name] for name in sorted(bound)],
 'sealer':binding('work/root/seal_disjoint_trace_carrier_review.py')}
target=ROOT/'work/root/disjoint_trace_carrier_continuation_acceptance.json'
assert not target.exists()
target.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'status':record['status'],'binding_count':len(bound),
                  'acceptance':binding(str(target.relative_to(ROOT)))},indent=2))
