#!/usr/bin/env python3
"""Bind both completed reviews of the exact original/local norm comparison."""
from pathlib import Path
from hashlib import sha256
import json

ROOT=Path(__file__).resolve().parents[2]
def bind(name):
    p=Path(name);p=p if p.is_absolute() else ROOT/p
    return {'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,
            'sha256':sha256(p.read_bytes()).hexdigest()}
expected={
    'work/part_d_attack/actual_norm_branches_and_odd_local_coefficients_result.json':'595790a97214a62979cf8664f357a6d3bddada2389d686fc5eac26012ed266c6',
    'work/root/review_actual_norm_branches_and_odd_local_coefficients.txt':'c0376862b92c962eb34192913c45130ffeb76046376af2686a175d6d4fcef15b',
    'work/root/actual_odd_local_midpoint_independent_replay/comparison.json':'e18063332f8376058ceb4961003dd2f2e6e4baa5f3357e78dc9f189b27f39fc0',
    'work/part_a/review_d_norm_branches_and_odd_local_coefficients.txt':'9b9d2006790898936477f184ff771d8552ddd6fd303c9e3cc4585ab3972906c0',
    'work/part_a/review_d_norm_branches_and_odd_local_coefficients.json':'59acc0b945ea8a03ba35df01920304ae54365485e99773c33abe4ed1e3461e98',
    'work/part_a/review_d_norm_replay/comparison.json':'4e82f33058d385bb52ec5d461b2443245db57f1f0ebc4acb983793f55d4f6255',
}
for name,digest in expected.items():assert bind(name)['sha256']==digest,name
meta=json.loads((ROOT/'work/part_d_attack/actual_norm_branches_and_odd_local_coefficients_result.json').read_text())
peer=json.loads((ROOT/'work/part_a/review_d_norm_branches_and_odd_local_coefficients.json').read_text())
rr=json.loads((ROOT/'work/root/actual_odd_local_midpoint_independent_replay/comparison.json').read_text())
pr=json.loads((ROOT/'work/part_a/review_d_norm_replay/comparison.json').read_text())
assert peer['status']=='SEALED_INDEPENDENT_PEER_REVIEW_PASS'
assert not peer['corrections_requested'] and peer['author_and_dependencies_unchanged']
assert rr['status']=='PASS' and rr['raw_output_and_stdout_byte_identical'] and rr['all_frozen_files_unchanged']
assert pr['status']=='PASS_UNCHANGED_ISOLATED_D_NORM_MIDPOINT_REPLAY'
assert pr['whole_raw_output_and_stdout_bytes_identical'] and pr['all_author_and_dependency_bindings_unchanged']
for data in [rr,pr]:
    assert data['named_checks']==27 and data['actual_finite_image_order']==3125
    assert data['unit_parameter_rows']==20
checked={}
def verify_tree(value):
    if isinstance(value,dict):
        if all(k in value for k in ['path','bytes','sha256']):
            actual=bind(value['path'])
            assert all(actual[k]==value[k] for k in ['bytes','sha256']),value['path']
            checked[actual['path']]=actual
        for child in value.values():verify_tree(child)
    elif isinstance(value,list):
        for child in value:verify_tree(child)
for data in [meta,peer,rr,pr]:verify_tree(data)
record={'status':'PASS_ROOT_AND_PEER','numbered_claim_added':False,
    'proof_lines':287,'program_lines':195,
    'root_review':bind('work/root/review_actual_norm_branches_and_odd_local_coefficients.txt'),
    'root_read_peer_report_in_full':True,
    'peer_report_lines':len((ROOT/'work/part_a/review_d_norm_branches_and_odd_local_coefficients.txt').read_text().splitlines()),
    'frozen_review_and_replay_records':[bind(name) for name in expected],
    'source_program_output_dependency_and_replay_bindings_verified':list(checked.values()),
    'named_checks_each':27,'actual_finite_image_order':3125,
    'local_coefficients_each':5,'unit_parameter_rows_each':20,
    'raw_output_and_stdout_byte_identical_each':True,
    'both_reviewers_reopened_exact_primary_clauses':True,
    'author_pending_fields_preserved_as_historical':True,
    'scope':'Exact full C3 free-product maps and compact labelled norm branches homeomorphic to the original T; named original-to-pro-p maps, midpoint retraction, split coefficient homomorphism and continuous local H_r family through the original h_p, with actual finite coefficient-one obstruction. The original T nonemptiness, full norm zero and actual all-prime coefficient constraint remain unresolved.'}
out=ROOT/'work/root/norm_branch_acceptance_270.json'
out.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'status':record['status'],'named_checks_each':27,
                  'bound_files':len(checked),'sha256':sha256(out.read_bytes()).hexdigest()},indent=2))
