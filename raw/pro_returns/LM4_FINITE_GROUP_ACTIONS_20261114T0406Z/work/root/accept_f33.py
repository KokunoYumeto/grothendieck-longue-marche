#!/usr/bin/env python3
"""Seal F33 after complete root and peer reviews and exact-byte verification."""
from pathlib import Path
from hashlib import sha256
import json

ROOT=Path(__file__).resolve().parents[2]
def path_of(name):
    p=Path(name)
    p=p if p.is_absolute() else ROOT/p
    p.relative_to(ROOT)
    return p
def binding(name):
    p=path_of(name);b=p.read_bytes()
    return {'path':str(p.relative_to(ROOT)),'bytes':len(b),'sha256':sha256(b).hexdigest()}
stem='work/part_a/f_quadratic_sign_pair_restriction'
frozen={
 stem+'.tex':'8a2cd87d9139c6e2bccd99cc9bb8db53883d064da5653fd804e2e2457ab96037',
 stem+'_results.json':'46d8c1f968e0133ad46d23fb3c20960b444081b29364c267715a20b0db49d2f2',
 stem+'_report.txt':'5b1493d029d5700957aa13cb2776d46cb11168bc2ff11f7d58ae4f1228a04e7e',
 stem+'_preservation.json':'82da89dcaeea70dc9232f218124bd6020e38e240860565d761e1fdbfc18392aa',
 stem+'_evidence_manifest.json':'6e08ac16e40d12ac995500f3c0527f56c03d9277a954e1d666f719bd67208104',
 'work/root/review_f33.txt':'eaca5a602ccbd0c92f2e9541b448eea2f8407e9134e6c462e30dea19225653e2',
 'work/part_c/review_f33.txt':'feb43e955fb63be1a3a760c3fafe074115c31412974dbb3b2107d66ab74325e0',
 'work/part_c/review_f33.json':'d3c2da9e4ba0f452f337438004baed16bb49d836133c86bcd3a59c03f7ae1fbb',
 'work/part_c/review_f33_binding_audit.json':'cfeb9a5c85337f9ad37e3ecad2ad2640234842d813af1a20bea83259bae72cce'}
closure={}
for name,digest in frozen.items():
    b=binding(name);assert b['sha256']==digest,name;closure[b['path']]=b
def read(name):return json.loads(path_of(name).read_text())
def verify(value):
    if isinstance(value,dict):
        if {'path','bytes','sha256'}<=set(value):
            b=binding(value['path'])
            assert b['bytes']==value['bytes'] and b['sha256']==value['sha256'],value['path']
            if 'lines' in value:assert len(path_of(value['path']).read_bytes().splitlines())==value['lines'],value['path']
            closure[b['path']]=b
        for child in value.values():verify(child)
    elif isinstance(value,list):
        for child in value:verify(child)

manifest=read(stem+'_evidence_manifest.json')
assert len(manifest['entries'])==manifest['entry_count']==69
verify(manifest)
preservation=read(stem+'_preservation.json')
assert preservation['entry_count']==400
prior_routes=[];recorded_paths=set();workspace_paths={}
for m in preservation['manifests']:
    b=binding(m['manifest']);assert b['sha256']==m['manifest_sha256'];closure[b['path']]=b
    data=read(m['manifest']);entries=data['entries']
    assert len(entries)==m['entries']
    verify(entries)
    for e in entries:
        recorded_paths.add(e['path'])
        name=binding(e['path'])['path']
        workspace_paths.setdefault(name,set()).add(e['path'])
        prior_routes.append({'manifest':m['manifest'],'recorded_path':e['path'],
                             'workspace_path':name,'bytes':e['bytes'],'sha256':e['sha256']})
assert len(prior_routes)==400 and len(recorded_paths)==294 and len(workspace_paths)==291
duplicates={k:v for k,v in workspace_paths.items() if len(v)>1}
assert set(duplicates)=={
 'work/part_a/code/full_cross_source_stage/marginal_braids.json',
 'work/part_a/f_source_sign_and_marginal_images.tex',
 'work/part_a/f_source_sign_and_marginal_images_results.json'}
transports=[]
for relative,spellings in sorted(duplicates.items()):
    absolute=str(ROOT/relative)
    assert spellings=={relative,absolute}
    assert path_of(relative)==path_of(absolute)
    assert path_of(relative).read_bytes()==path_of(absolute).read_bytes()
    transports.append({'relative_path':relative,'absolute_path':absolute,
                       'forward':'Join the recorded relative path to the exact ROOT prefix.',
                       'inverse':'Remove that exact ROOT prefix and its following separator.',
                       'common_file':binding(relative)})

peer=read('work/part_c/review_f33.json');verify(peer)
audit=read('work/part_c/review_f33_binding_audit.json');verify(audit)
assert peer['status']=='PASS' and not peer['requested_corrections']
assert peer['prior_entry_routes_verified']==400
assert peer['prior_distinct_recorded_paths_verified']==294
assert peer['prior_distinct_workspace_files_verified']==291
assert path_of(peer['report']['path']).read_bytes().endswith(path_of(peer['mathematical_body']['path']).read_bytes())
assert len(path_of(peer['report']['path']).read_bytes().splitlines())==382
assert len(path_of(stem+'_report.txt').read_bytes().splitlines())==371
assert len(path_of(stem+'.tex').read_bytes().splitlines())==404

replay_records=[]
for name in ['work/root/f33_independent_replay/comparison.json',
             'work/part_c/f33_peer_replay/comparison.json']:
    data=read(name);verify(data)
    assert data['exit_code']==0 and data['checks']==252309
    assert len(data['input_copies'])==8
    for a,b in [('checker_original','checker_copy'),('author_output','output'),('author_stdout','stdout')]:
        assert path_of(data[a]['path']).read_bytes()==path_of(data[b]['path']).read_bytes(),(name,a,b)
    assert path_of(data['stderr']['path']).read_bytes()==b''
    closure[name]=binding(name);replay_records.append(binding(name))
for name,field,count in [
 ('work/root/check_nonproduct_sign_pair_rank_output.json','total_exact_checks',32427),
 ('work/root/check_f33_actual_tex_output.json','check_count',77),
 ('work/part_c/f33_peer_replay/printed_formula_crosscheck.json','checks',27737)]:
    data=read(name)
    assert data[field]==count,(name,field)
    verify(data);closure[name]=binding(name)
for name in ['work/root/nonproduct_sign_pair_actual_divisor_audit.json',
             'work/root/accept_f33.py','work/root/prior_271_snapshot/binding.json']:
    closure[name]=binding(name)

record={
 'status':'PASS_ROOT_AND_PEER','claim':'F.33','global_claim_number':272,
 'proof_sha256':frozen[stem+'.tex'],'proof_lines':404,'numbered_displays':19,
 'root_mathematical_review':binding('work/root/review_f33.txt'),
 'root_complete_author_report_lines_read':371,
 'root_read_final_author_and_peer_substantive_metadata':True,
 'root_complete_peer_report_lines_read':382,
 'peer_mathematical_body_exact_suffix':True,
 'manifest_entries_verified':manifest['entries'],'manifest_entry_count':69,
 'prior_evidence_routes':prior_routes,'prior_evidence_route_count':400,
 'prior_distinct_recorded_path_strings':294,'prior_distinct_workspace_files':291,
 'exact_path_transports':transports,
 'preservation_count_correction':'Earlier wording calling294 distinct files is corrected:294 recorded path strings map to291 workspace files through exactly the three explicit inverse path maps above. Frozen author and previous evidence bytes are preserved.',
 'root_independent_row_checks':32427,'root_actual_TeX_checks':77,
 'root_and_peer_unchanged_literal_word_checks_each':252309,
 'peer_printed_coordinate_and_divisor_checks':27737,
 'replay_records':replay_records,
 'root_recomputed_whole_output_and_stdout_byte_identity_each':True,
 'source_changes_required':False,'pdf_gate_completed':False,
 'scope':'All-field64x13 rank theorem, and exact opposite-first-character paired cocycle kernel plus summed H1 injection over finite odd-characteristic fields, including r^2=1; both original signs via the explicit F23 based inverse maps.',
 'many_factor_consequence_registered':False,
 'complete_bound_closure_count':len(closure),
 'complete_bound_closure':[closure[k] for k in sorted(closure)]}
target=ROOT/'work/root/final_new_claim_acceptance_272.json'
assert not target.exists()
target.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'status':record['status'],'claim':'F.33',
 'manifest_entries':69,'prior_routes':400,'prior_recorded_paths':294,
 'prior_workspace_files':291,'complete_bound_closure_count':len(closure),
 'acceptance':binding(str(target.relative_to(ROOT)))},indent=2))
