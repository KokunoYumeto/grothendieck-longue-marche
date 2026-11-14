#!/usr/bin/env python3
"""Isolate and replay the unchanged full product-one original-word verifier."""
from pathlib import Path
from hashlib import sha256
import json
import shutil
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[2]
SOURCE=ROOT/'work/part_a/code'
DEST=ROOT/'work/root/f31_independent_replay'
DEST.mkdir(exist_ok=True)
program=SOURCE/'affine_full_product_one_independent_audit.py'
original=program.with_name('affine_full_product_one_independent_audit_output.json')
proof=ROOT/'work/part_a/f_full_product_one_affine_images.tex'
assert sha256(program.read_bytes()).hexdigest()=='ffa5e83b3f98750b5fa3621fb3c4799c28e1a6c99bcdfa3133adcb3f510e270d'
assert sha256(original.read_bytes()).hexdigest()=='1de63f7a2f40dc965623ed83272ca741b04e64c2455eff0539c39d53b4f6091f'
assert sha256(proof.read_bytes()).hexdigest()=='909cb42466354ecebfede5b5d27077381d13e87f9261ea62180dc507cf91c345'
data=json.loads(original.read_text())
assert data['total_exact_checks']==1603 and len(data['inputs'])==10
def bind(path):
 p=Path(path);p=p if p.is_absolute() else ROOT/p
 return {'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':sha256(p.read_bytes()).hexdigest()}
originals={str(program):sha256(program.read_bytes()).hexdigest(),str(original):sha256(original.read_bytes()).hexdigest(),str(proof):sha256(proof.read_bytes()).hexdigest()}
copied=[]
mapping={}
for name,digest in data['inputs'].items():
 source=Path(name)
 assert source.is_file() and sha256(source.read_bytes()).hexdigest()==digest
 relative=source.relative_to(SOURCE)
 target=DEST/relative
 target.parent.mkdir(parents=True,exist_ok=True)
 shutil.copyfile(source,target)
 assert target.read_bytes()==source.read_bytes()
 assert str(target) not in mapping
 mapping[str(target)]=str(source)
 originals[str(source)]=digest
 copied.append({'original':bind(source),'copy':bind(target)})
target_program=DEST/program.name
shutil.copyfile(program,target_program)
copied.append({'original':bind(program),'copy':bind(target_program)})
stdout,stderr=DEST/'stdout.txt',DEST/'stderr.txt'
with stdout.open('wb') as out,stderr.open('wb') as err:
 proc=subprocess.run([sys.executable,str(target_program)],cwd=DEST,stdout=out,stderr=err)
assert proc.returncode==0 and not stderr.read_bytes()
replay=DEST/original.name
replayed=json.loads(replay.read_text())
assert replayed['status']==data['status']
assert replayed['total_exact_checks']==1603
assert replayed['check_total']==977 and replayed['reviewed_word_and_parser_check_total']==626
assert len(replayed['charts'])==2 and len(replayed['sign_strata'])==15
assert all(chart['literal_words']==11 for chart in replayed['charts'])
assert set(replayed['inputs'])==set(mapping)
assert len(mapping)==len(set(mapping.values()))==10
assert replay.read_bytes()!=original.read_bytes()
transported=dict(replayed)
transported['inputs']={mapping[key]:value for key,value in replayed['inputs'].items()}
transported_bytes=(json.dumps(transported,indent=2)+'\n').encode()
assert transported_bytes==original.read_bytes()
inverse={value:key for key,value in mapping.items()}
restored=dict(transported)
restored['inputs']={inverse[key]:value for key,value in transported['inputs'].items()}
assert (json.dumps(restored,indent=2)+'\n').encode()==replay.read_bytes()
transport_path=DEST/'path_transport_output.json'
transport_path.write_bytes(transported_bytes)
for name,digest in originals.items():assert sha256(Path(name).read_bytes()).hexdigest()==digest,name
record={
 'status':'PASS','checks':1603,'module_checks':977,'reviewed_word_and_parser_checks':626,
 'literal_word_evaluations':22,'moving_annihilators_and_eigenrows':12,'row_determinants':5,'sign_strata':15,
 'original':bind(original),'replay':bind(replay),'raw_byte_identical':False,
 'exact_ten_input_path_bijection':mapping,'inverse_bijection':inverse,
 'path_transported_output_byte_identical':True,'inverse_transport_recovers_entire_replay':True,
 'path_transported_output':bind(transport_path),'copied_inputs_and_program':copied,
 'proof':bind(proof),'stdout':bind(stdout),'stderr':bind(stderr),'runner':bind(Path(__file__)),
 'all_original_inputs_unchanged_after_replay':True,
 'scope':'Both retained principal charts, all original source matrices, moving-root/eigenrow identities, exact determinants and all15 sign lifts/residuals. The full finite-field, source-module and affine-image arguments are separately reviewed.'}
(DEST/'comparison.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'status':'PASS','checks':1603,'ten_input_path_bijection':True,
 'complete_transported_output_byte_identical':True,'raw_replay_sha256':sha256(replay.read_bytes()).hexdigest()},indent=2))
