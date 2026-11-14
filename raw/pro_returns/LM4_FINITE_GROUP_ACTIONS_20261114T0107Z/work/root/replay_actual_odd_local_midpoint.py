#!/usr/bin/env python3
"""Replay the frozen actual finite pro-5 image with unchanged source bytes."""
from pathlib import Path
from hashlib import sha256
import json
import shutil
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[2]
DEST=ROOT/'work/root/actual_odd_local_midpoint_independent_replay'
DEST.mkdir(exist_ok=True)
metadata_path=ROOT/'work/part_d_attack/actual_norm_branches_and_odd_local_coefficients_result.json'
assert sha256(metadata_path.read_bytes()).hexdigest()=='595790a97214a62979cf8664f357a6d3bddada2389d686fc5eac26012ed266c6'
metadata=json.loads(metadata_path.read_text())
def bind(path):
    p=Path(path);p=p if p.is_absolute() else ROOT/p
    return {'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':sha256(p.read_bytes()).hexdigest()}
for entry in metadata['files']+metadata['dependencies']:
    actual=bind(entry['path'])
    assert actual['sha256']==entry['sha256'] and actual['bytes']==entry['bytes'],entry['path']
program=ROOT/'work/part_d_attack/code/actual_odd_local_midpoint.py'
copied=DEST/program.name
shutil.copyfile(program,copied)
stdout,stderr=DEST/'stdout.txt',DEST/'stderr.txt'
with stdout.open('wb') as out,stderr.open('wb') as err:
    proc=subprocess.run([sys.executable,str(copied)],cwd=DEST,stdout=out,stderr=err)
assert proc.returncode==0 and not stderr.read_bytes()
original=program.with_name('actual_odd_local_midpoint_output.json')
replay=copied.with_name(original.name)
assert original.read_bytes()==replay.read_bytes()==stdout.read_bytes()
data=json.loads(replay.read_text())
assert data['status']=='PASS' and data['assertion_count']==len(data['checks'])==27
assert all(row['passed'] for row in data['checks'])
assert data['prime']==5 and data['actual_image_order']==3125
assert [row['chosen_local_coefficient'] for row in data['rows']]==list(range(5))
unit_rows=[]
for row in data['rows']:
    tests=row['unit_parameter_tests']
    assert [v['mu_mod_10'] for v in tests]==[1,3,7,9]
    for v in tests:
        k=(v['mu_mod_10']-1)//2
        assert v['k_mod_5']==k%5
        coefficient=(-3*row['chosen_local_coefficient']-k*(k+1)//2)%5
        assert v['D_commutator_coefficient']==coefficient
        assert v['square_equation_mod_5']==(coefficient==0)
    unit_rows.extend(tests)
assert len(unit_rows)==20
assert all(not v['full_finite_D_is_identity'] and not v['square_equation_mod_5'] for v in data['rows'][1]['unit_parameter_tests'])
assert data['rows'][0]['h_truncated_Magnus_coordinates']==[1]+[0]*14
for entry in metadata['files']+metadata['dependencies']:
    assert bind(entry['path'])['sha256']==entry['sha256']
record={'status':'PASS','exit_code':0,'named_checks':27,'actual_finite_image_order':3125,
    'local_coefficient_rows':5,'unit_parameter_rows':20,
    'metadata':bind(metadata_path),'frozen_bindings':[bind(e['path']) for e in metadata['files']+metadata['dependencies']],
    'program':bind(copied),'original_output':bind(original),'replayed_output':bind(replay),
    'stdout':bind(stdout),'stderr':bind(stderr),'runner':bind(Path(__file__)),
    'raw_output_and_stdout_byte_identical':True,'all_frozen_files_unchanged':True,
    'scope':'The actual finite image of the standard free pro-5 quotient and the explicitly constructed local coefficient family. The original full simultaneous solution remains h=1; no alternate local point is asserted to be its image.'}
(DEST/'comparison.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'status':'PASS','named_checks':27,'actual_image_order':3125,
                  'unit_rows':20,'raw_output_and_stdout_byte_identical':True},indent=2))
