#!/usr/bin/env python3
"""Isolated unchanged-program replay of the F30 original-word certificate."""
from pathlib import Path
from hashlib import sha256
import json
import shutil
import subprocess

ROOT=Path(__file__).resolve().parents[2]
SOURCE=ROOT/'work/part_a/code'
TARGET=ROOT/'work/root/f30_independent_replay'
TARGET.mkdir(parents=True,exist_ok=True)
stem='affine_product_one_first_scalar_field_independent_audit'
names=[stem+'.py','affine_four_parameter_extension_independent_audit.py',
       'affine_product_one_first_scalar_field_stage.py',
       'affine_product_one_first_scalar_field_stage_output.json',
       'affine_obstruction_stage_output.json','full_cross_source_stage/marginal_braids.json']
def bind(path):
 return {'path':str(path.relative_to(ROOT)),'bytes':path.stat().st_size,
         'sha256':sha256(path.read_bytes()).hexdigest()}
copied=[]
for name in names:
 src,dst=SOURCE/name,TARGET/name
 dst.parent.mkdir(parents=True,exist_ok=True)
 shutil.copyfile(src,dst)
 assert src.read_bytes()==dst.read_bytes()
 copied.append({'original':bind(src),'copy':bind(dst)})
run=subprocess.run(['python',str(TARGET/(stem+'.py'))],cwd=TARGET,text=True,capture_output=True)
(TARGET/'stdout.txt').write_text(run.stdout)
(TARGET/'stderr.txt').write_text(run.stderr)
assert run.returncode==0,run.stderr
original_path=SOURCE/(stem+'_output.json');replay_path=TARGET/(stem+'_output.json')
original=json.loads(original_path.read_text());replay=json.loads(replay_path.read_text())
assert original['check_total']==replay['check_total']==45
mapping={key:str(SOURCE/Path(key).relative_to(TARGET)) for key in replay['inputs']}
assert len(mapping)==len(set(mapping.values()))==5
replay['inputs']={mapping[k]:v for k,v in replay['inputs'].items()}
assert replay==original
transported=(json.dumps(replay,indent=2)+'\n').encode()
assert transported==original_path.read_bytes()
mapped=TARGET/'path_transport_output.json';mapped.write_bytes(transported)
result={'status':'PASS','checks':45,'original':bind(original_path),'replay':bind(replay_path),
        'raw_byte_identical':replay_path.read_bytes()==original_path.read_bytes(),
        'exact_five_input_path_bijection':mapping,'path_transported_output_byte_identical':True,
        'path_transported_output':bind(mapped),'copied_inputs':copied,
        'proof':bind(ROOT/'work/part_a/f_product_one_first_scalar_field_images.tex'),
        'stdout':bind(TARGET/'stdout.txt'),'stderr':bind(TARGET/'stderr.txt'),
        'runner':bind(Path(__file__).resolve()),
        'scope':'Original sources0,2,7 and the exact X1-pivot scalar-core identities; mathematical F30 review is separate.'}
(TARGET/'comparison.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['status','checks','raw_byte_identical','path_transported_output_byte_identical']},indent=2))
