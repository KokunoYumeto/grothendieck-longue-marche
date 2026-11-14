#!/usr/bin/env python3
"""Seal the complete root/peer Haran comparison and unchanged finite replays."""
from pathlib import Path
from hashlib import sha256
import datetime,json

ROOT=Path(__file__).resolve().parents[2]
def binding(name):
    raw=(ROOT/name).read_bytes()
    return {'path':name,'bytes':len(raw),'sha256':sha256(raw).hexdigest()}
author_name='work/part_d_attack/haran_c2_c3_actual_map_comparison_result.json'
peer_name='work/part_c/review_haran_c2_c3_actual_map_comparison.json'
root_replay_name='work/root/haran_c2_c3_independent_replay/comparison.json'
peer_replay_name='work/part_c/haran_c2_c3_peer_replay/comparison.json'
expected={
 author_name:'fcac5535d5ba53ae9c67a4d09823c7c2970124466da6160abe6dbdb336d1d39d',
 peer_name:'a063cbc481b979a1f29c7af936ed207f20934d22c62e603f91d3ba988ec7d74b',
 root_replay_name:'1108847e6fcc8f85d30e9654973ac67fdb7f28ae325c989c1aedbad5feb0c479',
 peer_replay_name:'243148938e09c5a9164aa344f1bb753ef2823cc037535bd6f76481e12425a6c5',
 'work/part_d_attack/haran_c2_c3_actual_map_comparison.txt':'260c46a9370f05e4522a5f4e9f2c8920619690ec5abe65218a98fdc7cc8ac001',
 'work/part_c/review_haran_c2_c3_actual_map_comparison.txt':'04aaaf7e0aef030534008d57e96c2018a168c02713ca16b9478bdef098617ea7',
 'work/part_c/haran_c2_c3_peer_replay/primary_read_scope.json':'8b212aae55286ae665523dba8a89139f691664b7f1544dd9f2752fc6b347cc0b',
 'work/root/haran_c2_c3_primary_read_scope.json':'11600be54579d7f4c7945e590eea9a7c544c5e0aed9c661c902e2eb6c15e3f00',
 'work/part_d_attack/haran_closed_subgroups_1987_reference.bib':'8abd868b76f5423855f9b9d1de99a4777eddb5dbc834dc7435f9e7ae1bdcdf9f',
}
for name,digest in expected.items():assert binding(name)['sha256']==digest,name
author=json.loads((ROOT/author_name).read_text())
peer=json.loads((ROOT/peer_name).read_text())
root_replay=json.loads((ROOT/root_replay_name).read_text())
assert peer['status']=='PASS' and peer['correction_requested'] is None
assert not peer['author_files_modified'] and not peer['new_numbered_claim_assigned']
assert root_replay['named_checks']==11 and root_replay['S3_conjugator_pairs']==36
assert root_replay['source_copy_whole_bytes_identical'] and root_replay['all_four_output_and_stdout_whole_bytes_identical']
bound={};routes=0
def verify(value):
    global routes
    if isinstance(value,dict):
        if {'path','bytes','sha256'}<=set(value):
            p=Path(value['path']);name=str(p.relative_to(ROOT)) if p.is_absolute() else str(p)
            actual=binding(name)
            assert actual['bytes']==value['bytes'] and actual['sha256']==value['sha256'],name
            bound[name]=actual;routes+=1
        for child in value.values():verify(child)
    elif isinstance(value,list):
        for child in value:verify(child)
for name in [author_name,peer_name,root_replay_name,peer_replay_name,
             'work/root/haran_c2_c3_primary_read_scope.json',
             'work/part_c/haran_c2_c3_peer_replay/primary_read_scope.json']:
    verify(json.loads((ROOT/name).read_text()))
paths=[
 'work/part_d_attack/code/haran_c2_c3_marked_subgroup_witness_output.json',
 'work/part_d_attack/code/haran_c2_c3_marked_subgroup_witness_stdout.txt',
 'work/root/haran_c2_c3_independent_replay/haran_c2_c3_marked_subgroup_witness_output.json',
 'work/root/haran_c2_c3_independent_replay/stdout.txt',
 'work/part_c/haran_c2_c3_peer_replay/haran_c2_c3_marked_subgroup_witness_output.json',
 'work/part_c/haran_c2_c3_peer_replay/stdout.txt']
assert all((ROOT/name).read_bytes()==(ROOT/paths[0]).read_bytes() for name in paths)
for name in [*expected,*paths,
 'work/root/review_haran_c2_c3_actual_map_comparison.txt',
 'work/root/replay_haran_c2_c3_witness.py',
 'work/root/replay_haran_c2_c3_witness_stdout.json',
 'work/root/four_order_three_continuation_acceptance.json',
 'work/root/order_three_candidate_continuation_acceptance.json',
 'work/root/prior_271_snapshot/binding.json']:
    bound[name]=binding(name)
result={
 'status':'ACCEPTED_UNNUMBERED_HARAN_COMPARISON_ROOT_AND_PEER_PASS',
 'sealed_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'numbered_claim_registered':False,
 'root_complete_author_proof_lines_read':194,'root_complete_author_program_lines_read':123,
 'root_complete_mathematical_output_lines_read':87,'root_complete_peer_report_lines_read':249,
 'root_substantive_author_and_peer_metadata_read':True,
 'root_recursive_binding_routes_verified':routes,
 'root_actually_viewed_printed_primary_pages':[283],
 'peer_actually_viewed_printed_primary_pages':[283,297,298],
 'named_finite_checks':11,'S3_conjugator_pairs':36,
 'all_six_author_root_peer_output_stdout_files_whole_bytes_identical':True,
 'output_transport_both_directions':'Identity on all bytes.',
 'accepted_results':['Actual full relative intersection family for H3 and its finite embedding-problem conclusion.',
 'Compact minimal subgroup with an actual factor-conjugating epimorphism whose kernel is nontrivial.',
 'Explicit S4 quotient witnessing a proper conjugate-factor image and the literal standard J-star word defect.',
 'Original S3 quotient automorphism, coset homeomorphism with explicit inverse, and full-image-or-infinite-index result for this class.'],
 'accepted_new_bibliography_key':'D-HaranClosedSubgroups1987',
 'existing_paper_bibliography_modified':False,
 'retained_original_target':'The particular original H3, its j marking, full-unit coefficients and full cusp defects. No identification with Hstar or H1 and no nonemptiness of T are inferred.',
 'corrections_requested':[],'new_pdf_or_render_claimed':False,
 'binding_count':len(bound),'bindings':[bound[name] for name in sorted(bound)],
 'sealer':binding('work/root/seal_haran_c2_c3_review.py')}
target=ROOT/'work/root/haran_c2_c3_continuation_acceptance.json'
assert not target.exists()
target.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':result['status'],'binding_count':len(bound),
                  'acceptance':binding(str(target.relative_to(ROOT)))},indent=2))
