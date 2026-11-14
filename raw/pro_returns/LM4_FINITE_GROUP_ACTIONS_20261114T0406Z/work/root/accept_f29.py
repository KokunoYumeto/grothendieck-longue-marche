#!/usr/bin/env python3
"""Bind completed independent mathematical reviews before registering F29."""
from pathlib import Path
from hashlib import sha256
import json
import re

ROOT=Path(__file__).resolve().parents[2]
expected={
 'work/part_a/f_four_parameter_product_one_images.tex':'8aa897e0df17844ff6fb538be5770aaace072afa25d14a378cfc934e06d557cd',
 'work/part_a/f_four_parameter_product_one_images_results.json':'04169bf3db2fca17bdbd7177726cc6bf7cacd1b2664b393f062e6c133911b3d2',
 'work/part_a/f_four_parameter_product_one_images_report.txt':'e181ae7861f84d0d06594e57b349a3f22959cc94ba8b54c6ba9074cc2c4de231',
 'work/part_a/f_four_parameter_product_one_images_evidence_manifest.json':'aef9ee3a646f1e65e448864f81b3586a9394149d807fcb4004e876d859d62734',
 'work/part_c/review_f29.txt':'d0379c73a1e79aafa3c270271727f4c68b12f021f9ec2ca3bd68a12f6ddb475b',
 'work/part_c/review_f29.json':'dca50aac722ceb317fa9e4d9609c0aa3cd0354939db92fb942bf2b417902d880',
 'work/part_c/f29_independent_replay/comparison.json':'bc051043575d69e97e01f0527824f17909776fcecaa58c0d636972d985bfe86e',
}
def bind(path):
 p=Path(path);p=p if p.is_absolute() else ROOT/p
 return {'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,
         'sha256':sha256(p.read_bytes()).hexdigest()}
for path,value in expected.items():assert bind(path)['sha256']==value,path
stem='work/part_a/f_four_parameter_product_one_images'
proof=(ROOT/(stem+'.tex')).read_text()
assert len(proof.splitlines())==795
assert re.findall(r'\\tag\{F\.29\.(\d+)\}',proof)==[str(x) for x in range(1,34)]
metadata=json.loads((ROOT/(stem+'_results.json')).read_text())
assert metadata['id']=='F.29' and metadata['status']=='Proved'
manifest=json.loads((ROOT/(stem+'_evidence_manifest.json')).read_text())
assert len(manifest['entries'])==63
verified=[]
for entry in manifest['entries']:
 actual=bind(entry['path'])
 assert actual['bytes']==entry['bytes'] and actual['sha256']==entry['sha256'],entry['path']
 verified.append(actual)
peer=json.loads((ROOT/'work/part_c/review_f29.json').read_text())
assert peer['status']=='PASS' and peer['complete_proof_read']
assert peer['manifest_entry_count_verified']==63 and not peer['mathematical_corrections_requested']
assert not peer['source_files_edited']
root_replay=json.loads((ROOT/'work/root/f29_independent_replay/comparison.json').read_text())
peer_replay=json.loads((ROOT/'work/part_c/f29_independent_replay/comparison.json').read_text())
assert root_replay['status']=='PASS' and root_replay['check_total']==4242
assert peer_replay['status']=='PASS' and peer_replay['main_verifier_check_total']==4242
assert peer_replay['exceptional_explicit_assertions']==20
assert peer_replay['all_63_manifest_bindings_unchanged']
result={'status':'PASS_ROOT_AND_PEER','claim':'F.29','proof_sha256':expected[stem+'.tex'],
        'proof_lines':795,'numbered_displays':33,'frozen_artifacts':[bind(p) for p in expected],
        'root_mathematical_audit':bind('work/root/review_f29.txt'),
        'root_read_peer_report_in_full':True,'peer_report_lines':453,
        'manifest_entries_verified':verified,'manifest_entry_count':63,
        'root_replay':bind('work/root/f29_independent_replay/comparison.json'),
        'root_independent_checks':4242,'peer_independent_checks':4242,
        'exceptional_named_checks_each':20,
        'source_changes_required':False,'pdf_gate_completed':False,
        'scope':'Complete stated four-parameter image and restriction theorem; no broader character or full marginal conclusion.'}
(ROOT/'work/root/final_new_claim_acceptance_268.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':result['status'],'claim':'F.29','manifest_entries':63,
                  'root_checks':4242,'peer_checks':4242,'exceptional_checks_each':20,
                  'proof_unchanged':True},indent=2))
