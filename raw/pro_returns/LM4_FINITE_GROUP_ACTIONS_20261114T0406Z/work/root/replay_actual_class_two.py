#!/usr/bin/env python3
"""Independently replay the unchanged actual class-two coordinate certificate."""
from pathlib import Path
from hashlib import sha256
import json
import shutil
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[2]
DEST=ROOT/'work/root/actual_class_two_independent_replay'
DEST.mkdir(exist_ok=True)
metadata_path=ROOT/'work/part_d_attack/actual_transporter_class_two_and_gt0_result.json'
assert sha256(metadata_path.read_bytes()).hexdigest()=='b9b0d1a47c04a6a3994152d602a3d20c6d41fe8d4ffc40489da610ee5f2d9926'
metadata=json.loads(metadata_path.read_text())
def bind(path):
 p=Path(path);p=p if p.is_absolute() else ROOT/p
 return {'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':sha256(p.read_bytes()).hexdigest()}
for entry in metadata['files']+metadata['dependencies']:
 actual=bind(entry['path'])
 assert actual['sha256']==entry['sha256'] and actual['bytes']==entry['bytes'],entry['path']
program=ROOT/'work/part_d_attack/code/actual_transporter_class_two.py'
copied=DEST/program.name
shutil.copyfile(program,copied)
stdout,stderr=DEST/'stdout.txt',DEST/'stderr.txt'
with stdout.open('wb') as out,stderr.open('wb') as err:
 proc=subprocess.run([sys.executable,str(copied)],cwd=DEST,stdout=out,stderr=err)
assert proc.returncode==0 and not stderr.read_bytes()
original=program.with_name('actual_transporter_class_two_output.json')
replay=copied.with_name(original.name)
assert original.read_bytes()==replay.read_bytes()==stdout.read_bytes()
data=json.loads(replay.read_text())
assert data['status']=='PASS' and data['assertion_count']==len(data['checks'])==38
assert all(item['passed'] for item in data['checks'])
assert data['total_coordinate_formula_cases']==144824
assert data['total_sign_identity_cases']==17892
assert [row['modulus'] for row in data['rows']]==[2,3,5,7,8,9]
for row in data['rows']:
 n=row['modulus']
 assert row['group_order']==n**3
 assert row['parity_kernel_exponent']==(n if n%2 else 2*n)
 assert row['unit_parameter_modulus']==2*row['parity_kernel_exponent']
 assert row['square_test_modulus']==8*n
 assert len(row['class_two_root_rows'])==len(row['GT0_coefficient_rows'])==n
 assert all(item['T_unit_residues']==item['quadratic_unit_residues'] for item in row['class_two_root_rows'])
for entry in metadata['files']+metadata['dependencies']:
 assert bind(entry['path'])['sha256']==entry['sha256']
record={'status':'PASS','exit_code':0,'named_checks':38,
 'coordinate_formula_cases':144824,'sign_identity_cases':17892,
 'metadata':bind(metadata_path),'frozen_bindings':[bind(e['path']) for e in metadata['files']+metadata['dependencies']],
 'program':bind(copied),'original_output':bind(original),'replayed_output':bind(replay),
 'stdout':bind(stdout),'stderr':bind(stderr),'runner':bind(Path(__file__)),
 'raw_output_and_stdout_byte_identical':True,'all_frozen_files_unchanged':True,
 'scope':'Actual full-source class-two quotient identities and complete displayed finite arithmetic checks. Arbitrary finite h-coordinates have no asserted nonstandard full-group realization.'}
(DEST/'comparison.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'status':'PASS','checks':38,'coordinate_cases':144824,
 'sign_cases':17892,'raw_output_and_stdout_byte_identical':True},indent=2))
