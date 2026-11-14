#!/usr/bin/env python3
"""Bind completed root and peer reviews without rewriting the frozen author note."""
from pathlib import Path
from hashlib import sha256
import json

ROOT=Path(__file__).resolve().parents[2]
expected={
 'work/part_d_attack/actual_transporter_single_parameter_reduction.txt':'7ba862392788a46b4fa92563ae0c5cea293897fd8d39ac9d27a17e2ab6826b49',
 'work/part_d_attack/actual_transporter_single_parameter_reduction_result.json':'cc281bb8abf4e351971891dc881106143449491d81abef5ce33d10cde632d4bf',
 'work/part_c/review_actual_transporter_single_parameter_reduction.txt':'3e336b601832d67c17fa52e228572018b529a397c3b24e25872475109a7e09e0',
 'work/part_c/review_actual_transporter_single_parameter_reduction.json':'7466c4e2655e388bd7db5609cc4a1796a8bef25fb340eedf8dd2027f69c4812d',
 'work/part_c/actual_transporter_independent_replay/comparison.json':'4d552dc69bf21ef94b4b743570f43f2780b99156d19483e8c635f976c50980a4',
}
def bind(name):
 p=ROOT/name
 return {'path':name,'bytes':p.stat().st_size,'sha256':sha256(p.read_bytes()).hexdigest()}
for name,digest in expected.items():assert bind(name)['sha256']==digest,name
metadata=json.loads((ROOT/'work/part_d_attack/actual_transporter_single_parameter_reduction_result.json').read_text())
verified=[]
for entry in metadata['files']+metadata['dependency_bindings']:
 actual=bind(entry['path'])
 assert actual['bytes']==entry['bytes'] and actual['sha256']==entry['sha256'],entry['path']
 verified.append(actual)
peer=json.loads((ROOT/'work/part_c/review_actual_transporter_single_parameter_reduction.json').read_text())
assert peer['verdict']=='PASS'
assert not peer['mathematical_corrections_requested'] and not peer['program_corrections_requested']
assert not peer['frozen_sources_modified']
root_replay=json.loads((ROOT/'work/root/actual_transporter_independent_replay/comparison.json').read_text())
peer_replay=json.loads((ROOT/'work/part_c/actual_transporter_independent_replay/comparison.json').read_text())
assert root_replay['status']=='PASS' and root_replay['named_checks']==24
assert root_replay['raw_output_byte_identical'] and root_replay['stdout_raw_byte_identical']
assert peer_replay['status']=='PASS' and peer_replay['named_assertions']==24
assert peer_replay['output_and_stdout_raw_bytes_equal_to_both_frozen_outputs']
assert peer_replay['retained_refined_conjugator_witnesses']==40
assert peer_replay['all_frozen_files_and_dependencies_unchanged']
record={'status':'PASS_ROOT_AND_PEER','numbered_claim_added':False,
 'proof_lines':391,'program_lines':361,'root_read_peer_report_in_full':True,
 'peer_report_lines':375,'frozen_artifacts':[bind(name) for name in expected],
 'source_and_dependency_entries_verified':verified,
 'root_review':bind('work/root/review_actual_transporter_single_parameter_reduction.txt'),
 'root_replay':bind('work/root/actual_transporter_independent_replay/comparison.json'),
 'peer_replay':bind('work/part_c/actual_transporter_independent_replay/comparison.json'),
 'named_checks_each':24,'retained_chain_witnesses_each':40,
 'raw_output_and_stdout_byte_identical_each':True,
 'author_pending_fields_preserved_as_historical':True,
 'scope':'Exact original and folded solution-space maps, one-parameter defect identities, actual finite refinement arrows and the completely executed standard homology-cover example. Nonemptiness and the original realization remain unresolved.'}
out=ROOT/'work/root/actual_transporter_acceptance_269.json'
out.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'status':record['status'],'named_checks_each':24,
 'numbered_claim_added':False,'sha256':sha256(out.read_bytes()).hexdigest()},indent=2))
