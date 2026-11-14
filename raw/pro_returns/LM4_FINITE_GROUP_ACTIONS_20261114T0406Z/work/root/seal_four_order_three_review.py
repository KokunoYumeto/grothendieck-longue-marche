#!/usr/bin/env python3
"""Seal the complete root and peer review of the actual four-candidate maps."""
from pathlib import Path
from hashlib import sha256
import datetime
import json

ROOT=Path(__file__).resolve().parents[2]
def binding(name):
    p=ROOT/name
    raw=p.read_bytes()
    return {'path':name,'bytes':len(raw),'sha256':sha256(raw).hexdigest()}

author_name='work/part_d_attack/actual_four_order_three_elements_and_cusp_comparison_result.json'
peer_name='work/part_c/review_actual_four_order_three_elements_and_cusp_comparison.json'
root_replay_name='work/root/actual_four_order_three_standard_independent_replay/comparison.json'
peer_replay_name='work/part_c/four_order_three_standard_peer_replay/comparison.json'
expected={
 author_name:'c1c043d263c17c78528df0db18fef9c6e57f0c47c438053345d427a2d667b00b',
 peer_name:'0fa93c5364199e235436fec971f20f8871757581b06946b05048f81287d9f867',
 'work/part_d_attack/actual_four_order_three_elements_and_cusp_comparison.txt':'f13a351257b3ab7d0ee1320adc2eae4fcb307bc9e7c2ff65c126b2a1ee87359a',
 'work/part_c/review_actual_four_order_three_elements_and_cusp_comparison.txt':'666baab54e0e97e2450b0ab6706f76dc67a04b4f9c5487e6f524e08619543a5d',
 root_replay_name:'61f7f0f58e14ea041caa2825098da77d520cc7fa2e91565d3e5a661d7da07074',
 peer_replay_name:'32b5a2d0110f55b23396775b5c21da42ee69d84bb4948e3dd3c9cb46455dbdd5',
 'work/part_c/four_order_three_standard_peer_replay/primary_read_scope.json':'bff13b8f4a07e769d8f28c24136a22fe711d19518895b37e6d4aef3a3586f127',
}
for name,digest in expected.items():
    assert binding(name)['sha256']==digest,name
author,peer,replay,peer_replay=[json.loads((ROOT/name).read_text()) for name in
                              [author_name,peer_name,root_replay_name,peer_replay_name]]
assert peer['status']=='PASS' and peer['correction_requested'] is None
assert not peer['author_files_modified'] and not peer['new_numbered_claim_assigned']
assert len(author['files'])+len(author['mathematical_dependencies'])+len(author['primary_copies'])==22
assert peer['binding_review']['direct_author_binding_routes_count']==22
assert peer['binding_review']['prior_author_binding_routes_count']==20
assert peer['binding_review']['unique_frozen_files_including_current_metadata_count']==29
assert all(value=='PASS' for key,value in peer['mathematical_review'].items()
           if key!='original_objects_retained')
assert replay['status']=='PASS_UNCHANGED_ISOLATED_ROOT_REPLAY'
assert replay['named_checks']==peer['replay']['named_checks']==22
assert replay['actual_standard_finite_image_order']==peer['replay']['actual_standard_image_order']==1080
assert peer['replay']['exit_code']==0 and peer['replay']['stderr_bytes']==0
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
for value in [author,peer,replay,peer_replay]:
    verify(value)
for name in expected:
    bound[name]=binding(name)
for name in [
 'work/root/review_actual_four_order_three_elements_and_cusp_comparison.txt',
 'work/root/replay_actual_four_order_three_standard.py',
 'work/root/replay_actual_four_order_three_standard_stdout.json',
 'work/root/order_three_candidate_continuation_acceptance.json',
 'work/root/marked_v4_continuation_acceptance.json',
 'work/root/negative_transposition_continuation_acceptance.json',
 'work/root/full_profinite_recognition_literature_20261114.txt',
 'work/root/four_order_three_primary_page-27.png',
 'work/root/four_order_three_primary_page-28.png',
 'work/root/prior_271_snapshot/binding.json']:
    bound[name]=binding(name)
outputs=[
 'work/part_d_attack/code/actual_four_order_three_standard_output.json',
 'work/part_d_attack/code/actual_four_order_three_standard_stdout.txt',
 'work/root/actual_four_order_three_standard_independent_replay/actual_four_order_three_standard_output.json',
 'work/root/actual_four_order_three_standard_independent_replay/stdout.txt',
 'work/part_c/four_order_three_standard_peer_replay/actual_four_order_three_standard_output.json',
 'work/part_c/four_order_three_standard_peer_replay/stdout.txt']
raw=(ROOT/outputs[0]).read_bytes()
assert sha256(raw).hexdigest()=='10af2c129561226b60ee444abf5dc5270428686fbf3bdb8d0ce36912cbdf8497'
assert all((ROOT/name).read_bytes()==raw for name in outputs)
result=json.loads(raw)
assert result['assertion_count']==22 and all(row['passed'] for row in result['checks'])
assert [row['epsilon_in_M_over_F'] for row in result['rows']]==[1,-1,-1,1]
assert [row['sigma_in_M_abelianization'] for row in result['rows']]==[1,-1,1,-1]
assert [row['original_cusp_word_is_identity_in_this_image'] for row in result['rows']]==[False,False,True,True]
record={
 'status':'ACCEPTED_UNNUMBERED_CONTINUATION_ROOT_AND_PEER_PASS',
 'sealed_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'numbered_claim_registered':False,
 'root_full_author_proof_lines_read':331,'root_full_program_lines_read':137,
 'root_full_output_lines_read':234,'root_full_author_metadata_read':True,
 'root_primary_comparison_note_lines_read':33,'root_full_peer_report_lines_read':316,
 'root_peer_metadata_substantive_fields_read':True,
 'root_primary_read_scope':{
   'primary_url':'https://webusers.imj-prg.fr/~pierre.lochak/textes/inventiones.pdf',
   'retrievals':['turn1298view0','turn1299view0','turn1299view1'],
   'printed_pages_actually_viewed':[597,598],
   'read_clauses':'Appendix definitions(H),(A1)-(A3), Proposition(a), complete finite-subgroup corollary and its proof.',
   'bound_pngs':[binding('work/root/four_order_three_primary_page-27.png'),
                binding('work/root/four_order_three_primary_page-28.png')]},
 'mathematical_corrections_requested':[],
 'current_author_binding_routes':22,'preceding_author_binding_routes':20,
 'root_recursive_binding_routes_verified':routes,
 'named_checks_each':22,'actual_standard_finite_image_order':1080,
 'six_author_root_peer_output_stdout_files_whole_bytes_identical':True,
 'forward_and_inverse_output_maps':'Identity on each entire output byte string.',
 'accepted_scope':'Actual four-point set with complete inverse parametrization; four original coproduct maps and common closed image; explicit source-amalgam comparison; both original involution intertwinings; exact epsilon/sigma maps and unit coordinates at2,3; original cusp-space homeomorphism and finite four-candidate defect identity.',
 'retained_target':'Full H3 generation, remaining prime-unit coordinates of nu0, an original full cusp zero, original full-unit m, W=1 and T nonemptiness.',
 'binding_count':len(bound),'bindings':[bound[name] for name in sorted(bound)],
 'published_pdf_preserved':binding('work/root/prior_271_snapshot/binding.json'),
 'sealed_by':binding('work/root/seal_four_order_three_review.py')}
out=ROOT/'work/root/four_order_three_continuation_acceptance.json'
assert not out.exists()
out.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'status':record['status'],'binding_count':len(bound),
                  'acceptance':binding(str(out.relative_to(ROOT)))},indent=2))
