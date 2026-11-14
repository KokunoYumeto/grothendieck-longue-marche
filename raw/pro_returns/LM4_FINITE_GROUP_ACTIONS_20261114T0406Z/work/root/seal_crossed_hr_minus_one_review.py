#!/usr/bin/env python3
"""Seal the two exact crossed sign branches after complete root/peer review."""
from pathlib import Path
from hashlib import sha256
import datetime,json

ROOT=Path(__file__).resolve().parents[2]
def locate(name):
    p=Path(name);p=p if p.is_absolute() else ROOT/p;p.relative_to(ROOT);return p
def binding(name):
    p=locate(name);b=p.read_bytes()
    return {'path':str(p.relative_to(ROOT)),'bytes':len(b),'sha256':sha256(b).hexdigest()}
expected={
 'work/root/nonproduct_hr_minus_one_crossed_sign_strata.txt':'c59f6e89ccf77ae8c3f97386e1c641ebff6f5a20c535759ea624b38f7696e17a',
 'work/root/check_nonproduct_hr_minus_one_crossed.py':'424bf7d123d6553080908a41bf8e90b677c642c0e426913018c72241adde23c3',
 'work/root/check_nonproduct_hr_minus_one_crossed_output.json':'39325de6ea08b8b13d658a06fe147cb59852062a0a296b781355a927b638dd95',
 'work/root/check_nonproduct_hr_minus_one_crossed_stdout.json':'16ba8be0541ea536693d1714e9e0bd308045e6b8f5bb17059e1eec1c94b7d987',
 'work/part_a/review_root_hr_minus_one_crossed_sign_strata.txt':'115716c30cd7515a4ef0ae0bf0cafdf25a8862a3c4dbee9d4ae036cc6118d899',
 'work/part_a/review_root_hr_minus_one_crossed_sign_strata.json':'11921ec306237449fa81d06c782cdaadffd137c589896c2bebd3dd291019e28d',
 'work/part_a/nonproduct_hr_minus_one_crossed_peer_replay/comparison.json':'b92c3d1c07d5eec72985f888d03d2ff2b27c6ab9e5c59cd8e09ded79a810ccbe'}
bound={};routes=0
for name,digest in expected.items():
    b=binding(name);assert b['sha256']==digest,name;bound[b['path']]=b
def verify(value):
    global routes
    if isinstance(value,dict):
        if {'path','bytes','sha256'}<=set(value):
            b=binding(value['path']);assert b['bytes']==value['bytes'] and b['sha256']==value['sha256'],value['path']
            if 'lines' in value:assert len(locate(value['path']).read_bytes().splitlines())==value['lines']
            bound[b['path']]=b;routes+=1
        for x in value.values():verify(x)
    elif isinstance(value,list):
        for x in value:verify(x)
peer=json.loads(locate('work/part_a/review_root_hr_minus_one_crossed_sign_strata.json').read_text())
assert peer['status']=='PASS_INDEPENDENT_PEER_REVIEW_CROSSED_HR_MINUS_ONE_SIGN_STRATA'
assert not peer['mathematical_corrections_requested'] and peer['isolated_replay_checks']==52
verify(peer)
output=json.loads(locate('work/root/check_nonproduct_hr_minus_one_crossed_output.json').read_text())
assert output['check_count']==52 and all(x['passed'] for x in output['checks'])
verify(output)
comparison=json.loads(locate('work/part_a/nonproduct_hr_minus_one_crossed_peer_replay/comparison.json').read_text())
assert comparison['returncode']==0 and comparison['checks']==52 and comparison['stderr_empty']
for key in ['output','stdout']:
    item=comparison[key]
    assert locate(item['author']).read_bytes()==locate(item['copy']).read_bytes()
for name in ['work/root/hr_minus_one_uw_one_continuation_acceptance.json',
             'work/root/prior_271_snapshot/binding.json']:
    b=binding(name);bound[b['path']]=b
record={
 'status':'ACCEPTED_UNNUMBERED_CROSSED_SIGN_STRATA_ROOT_AND_PEER_PASS',
 'sealed_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'numbered_claim_registered':False,
 'root_complete_proof_lines_read':162,'root_complete_program_lines_read':151,
 'root_complete_peer_report_lines_read':166,'root_substantive_peer_metadata_read':True,
 'recursive_binding_routes_verified':routes,'exact_checks_each':52,
 'whole_output_and_stdout_byte_identity_recomputed':True,
 'accepted_domain':'Odd-characteristic quadratic sign extension K/L, hr=-1, d=r/h, r^2=-d nonsquare, either (u,w)=(1/d,1) or(1,1/d), and nonzero source-zero rank-one action on the specified common simple source submodule; d=1 uses the separately accepted u=w=1 proof.',
 'accepted_maps':'Both exact Laurent transports, original-matrix rank-one trace and its source-intertwiner equality, complete branch substitutions, integral Sylvester cofactors and integer Bezout combination equal to4.',
 'exact_source_scope':'The three bound original-matrix/factor/pairing files. No fresh original group-word reconstruction is claimed in this local certificate.',
 'retained_target':'The broader independently audited nonproduct source classification and full marginal/interaction targets.',
 'corrections_requested':[],'new_pdf_or_render_claimed':False,
 'binding_count':len(bound),'bindings':[bound[k] for k in sorted(bound)],
 'sealer':binding('work/root/seal_crossed_hr_minus_one_review.py')}
target=ROOT/'work/root/crossed_hr_minus_one_continuation_acceptance.json';assert not target.exists()
target.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'status':record['status'],'binding_count':len(bound),
 'acceptance':binding(str(target.relative_to(ROOT)))},indent=2))
