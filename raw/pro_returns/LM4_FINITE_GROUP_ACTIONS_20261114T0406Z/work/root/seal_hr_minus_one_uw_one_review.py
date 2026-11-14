#!/usr/bin/env python3
"""Freeze the completed local sign-stratum proof and its independent peer replay."""
from pathlib import Path
from hashlib import sha256
import datetime
import json

ROOT=Path(__file__).resolve().parents[2]
def binding(name):
    data=(ROOT/name).read_bytes()
    return {'path':name,'bytes':len(data),'sha256':sha256(data).hexdigest()}

peer_name='work/part_a/review_root_hr_minus_one_uw_one_sign_stratum.json'
expected={
 'work/root/nonproduct_hr_minus_one_uw_one_sign_stratum.txt':'5a164a3841a75b612751a1bc1145d81d38efe3bbdfccdd68e896cf92ef8befb8',
 'work/root/check_nonproduct_hr_minus_one_uw_one.py':'a1534014d59f1fba3af677e49f52f77c371c8412e91e74c3b51cbec639c55a48',
 'work/root/check_nonproduct_hr_minus_one_uw_one_output.json':'5a18f2e0768fcc1f4e115cdbac7009d21597347cb3868852000b041a008f8112',
 'work/root/check_nonproduct_hr_minus_one_uw_one_stdout.json':'148ae0af49f671281492725496701511db086260a298da3dee35ae4e301a4fbb',
 'work/part_a/review_root_hr_minus_one_uw_one_sign_stratum.txt':'f8a83ce1f209a739588cca1ee85a28e6925f0691917f31664375f5f5eae7e9c5',
 peer_name:'fd2566955b5efe22b6bc4329bf769bdb54df3c03d5bdedf76a3dac6eaec5e410',
}
for name,digest in expected.items():
    assert binding(name)['sha256']==digest,name
peer=json.loads((ROOT/peer_name).read_text())
output=json.loads((ROOT/'work/root/check_nonproduct_hr_minus_one_uw_one_output.json').read_text())
assert peer['status']=='PASS_FULL_PEER_REVIEW_AND_UNCHANGED_REPLAY'
assert peer['corrections_requested']==[]
assert peer['raw_replay_output_byte_equal'] and peer['raw_replay_stdout_byte_equal']
assert output['check_count']==33 and len(output['checks'])==33
assert all(row['passed'] for row in output['checks'])
bound={}
routes=0
def verify(value):
    global routes
    if isinstance(value,dict):
        if all(k in value for k in ['path','bytes','sha256']):
            path=Path(value['path'])
            name=str(path.relative_to(ROOT)) if path.is_absolute() else str(path)
            actual=binding(name)
            assert actual['bytes']==value['bytes'] and actual['sha256']==value['sha256'],name
            bound[name]=actual
            routes+=1
        for child in value.values(): verify(child)
    elif isinstance(value,list):
        for child in value: verify(child)
verify(peer)
verify(output)
comparison_name='work/part_a/nonproduct_hr_minus_one_uw_one_peer_replay/comparison.json'
verify(json.loads((ROOT/comparison_name).read_text()))
for name in [*expected,'work/root/prior_271_snapshot/binding.json']:
    bound[name]=binding(name)
record={
 'status':'ACCEPTED_UNNUMBERED_LOCAL_SIGN_STRATUM_ROOT_AND_PEER_PASS',
 'sealed_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'numbered_claim_registered':False,
 'root_complete_proof_lines_read':131,
 'root_complete_check_output_lines_read':194,
 'root_complete_peer_proof_and_metadata_read':True,
 'peer_complete_proof_lines_read':131,
 'peer_complete_program_lines_read':156,
 'exact_checks':33,
 'recursive_binding_routes_verified':routes,
 'accepted_domain':output['domain'],
 'accepted_common_module_scope':'A common simple submodule for the two original source actions with nonzero restriction of T0-dI. The rank-one intertwiner gives qW(T)a=sigma(qW(T)a) for every original source word.',
 'accepted_computation':'The eleven single traces force the exact exceptional character (r,t^-1,t,1,1,1,t^2), r^2=-t^-2, t^2!=1. The actual word T2*T5 has odd scalar part -r*(t-1)*(t+1)*(t^2+1)/t^4, which is nonzero on the stated domain.',
 'source_matrix_scope':'Hash-bound six-dimensional boundary-quotient matrices and rank-one factorization. A fresh independent derivation from all original group words is not asserted by this local certificate.',
 'independent_replay':'Unchanged peer program copy with complete-byte equality for mathematical output and stdout, each compared separately.',
 'corrections_requested':[],
 'remaining_target':'Other sign strata, the zero-rank-one case and the complete all-character affine statement.',
 'new_pdf_or_render_claimed':False,
 'binding_count':len(bound),
 'bindings':[bound[name] for name in sorted(bound)],
 'sealer':binding('work/root/seal_hr_minus_one_uw_one_review.py')}
target=ROOT/'work/root/hr_minus_one_uw_one_continuation_acceptance.json'
assert not target.exists()
target.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'status':record['status'],'binding_count':len(bound),
                  'acceptance':binding(str(target.relative_to(ROOT)))},indent=2))
