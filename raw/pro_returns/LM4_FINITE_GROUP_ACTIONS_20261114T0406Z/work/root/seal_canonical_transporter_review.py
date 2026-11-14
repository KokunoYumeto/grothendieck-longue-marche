#!/usr/bin/env python3
"""Seal both complete audits of the original canonical transporter/cusp maps."""
from pathlib import Path
from hashlib import sha256
import json,datetime

ROOT=Path(__file__).resolve().parents[2]
def binding(name):
    raw=(ROOT/name).read_bytes();return {'path':name,'bytes':len(raw),'sha256':sha256(raw).hexdigest()}
author_name='work/part_d_attack/actual_canonical_transporter_and_cusp_membership_result.json'
peer_name='work/part_c/review_actual_canonical_transporter_and_cusp_membership.json'
root_replay='work/root/canonical_transporter_independent_replay/comparison.json'
peer_replay='work/part_c/canonical_transporter_peer_replay/comparison.json'
expected={
 author_name:'62c400ad942308fb77906084f4cbfbe70a9f9f42fbd5b3fff042a65076bfa08a',
 peer_name:'4d6838b93f20bd48fce923299ef581711cc8f5ee8570fc9700ef4d2bea1964bb',
 root_replay:'9e59004abcaa114015d366daa89c32fda02fb087787814a62154facbbf3f5853',
 peer_replay:'dc9669333965828eab6ae4ac7b8f2aa6e3a3a23abfaac0cc09f191f2f1ff44ff',
 'work/part_d_attack/actual_canonical_transporter_and_cusp_membership.txt':'fc0aec86ff68f3eb265b213ee81657a2397ca7eece6133eb985739962b317cd3',
 'work/part_c/review_actual_canonical_transporter_and_cusp_membership.txt':'5b3430238706432f2c655e01dad81b6996ec75c6e2e5744a7ab1cee4179eecad',
 'work/part_d_attack/code/actual_canonical_transporter_words.py':'ee354569eedce861e104647f9a190af227ff3e28a133d417b853b2f6bdaf4c33'}
for name,digest in expected.items():assert binding(name)['sha256']==digest,name
author=json.loads((ROOT/author_name).read_text())
peer=json.loads((ROOT/peer_name).read_text())
assert peer['status']=='PASS' and peer['requested_corrections']==[]
assert peer['all_frozen_author_files_unchanged'] and peer['binding_verification']['status']=='PASS'
assert peer['replay']['named_checks']==20 and peer['replay']['universal_odd_exponent_cases']==17
assert peer['replay']['integral_branch_cases']==19
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
for name in [author_name,peer_name,root_replay,peer_replay,
             'work/part_d_attack/actual_four_order_three_elements_and_cusp_comparison_result.json']:
    verify(json.loads((ROOT/name).read_text()))
outputs=[
 'work/part_d_attack/code/actual_canonical_transporter_words_output.json',
 'work/part_d_attack/code/actual_canonical_transporter_words_stdout.txt',
 'work/root/canonical_transporter_independent_replay/actual_canonical_transporter_words_output.json',
 'work/root/canonical_transporter_independent_replay/stdout.txt',
 'work/part_c/canonical_transporter_peer_replay/actual_canonical_transporter_words_output.json',
 'work/part_c/canonical_transporter_peer_replay/stdout.txt']
assert all((ROOT/name).read_bytes()==(ROOT/outputs[0]).read_bytes() for name in outputs)
for name in [*expected,*outputs,
 'work/root/review_actual_canonical_transporter_and_cusp_membership.txt',
 'work/root/replay_canonical_transporter_words.py','work/root/replay_canonical_transporter_words_stdout.json',
 'work/root/four_order_three_continuation_acceptance.json',
 'work/root/order_three_candidate_continuation_acceptance.json',
 'work/root/negative_transposition_continuation_acceptance.json',
 'work/root/marked_v4_continuation_acceptance.json','work/root/prior_271_snapshot/binding.json']:
    bound[name]=binding(name)
record={
 'status':'ACCEPTED_UNNUMBERED_CANONICAL_TRANSPORTER_ROOT_AND_PEER_PASS',
 'sealed_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'numbered_claim_registered':False,
 'root_complete_author_proof_lines_read':246,'root_complete_program_lines_read':193,
 'root_complete_output_lines_read':199,'root_complete_peer_report_lines_read':332,
 'root_substantive_author_and_peer_metadata_read':True,
 'root_recursive_binding_routes_verified':routes,
 'all_six_author_root_peer_output_stdout_files_whole_bytes_identical':True,
 'output_transport_both_directions':'Identity on all bytes.',
 'named_checks':20,'universal_odd_exponent_cases':17,'standard_integral_branch_cases':19,
 'accepted_unique_maps':'a in F-prime; ordered d=tau*a^-1*s; L*d*L^-1=j; kappa+=L*xi*L^-1; inverse d=L^-1*j*L and a=s*d*tau.',
 'accepted_full_cusp_maps':'r=xi^-1*s*xi; A=w*L*omega^2(L^-1); B=tprime*A*p^-1. C_kappa+=1 iff A in <z>; C_tkappa+t=1 iff B in <z> iff A in g^-1<z>.',
 'accepted_parameter_map':'k=3*chi_x(L), nu0=2k+1. R(k)=z^(-(k+1)/2) on odd k and g^-1*z^(-k/2) on even k; inverse on the two actual cosets is Sigma(A)-1.',
 'accepted_original_solution_set':'T={nu in {nu0,-nu0}: nu0 is a full profinite unit and A=R(k)}, with the four-row explicit inverse table into the original Z_K.',
 'retained_unproved_gates':author['retained_unproved_gates'],
 'new_primary_theorem_imported':False,'new_pdf_or_render_claimed':False,
 'corrections_requested':[],'binding_count':len(bound),
 'bindings':[bound[name] for name in sorted(bound)],
 'sealer':binding('work/root/seal_canonical_transporter_review.py')}
target=ROOT/'work/root/canonical_transporter_continuation_acceptance.json'
assert not target.exists()
target.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'status':record['status'],'binding_count':len(bound),
                  'acceptance':binding(str(target.relative_to(ROOT)))},indent=2))
