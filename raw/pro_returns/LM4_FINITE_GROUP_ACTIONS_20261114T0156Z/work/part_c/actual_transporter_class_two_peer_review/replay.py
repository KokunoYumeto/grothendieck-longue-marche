#!/usr/bin/env python3
"""Bounded isolated peer replay, outside checkpoint269 selected code."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json
import shutil
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[3]
OUT=Path(__file__).resolve().parent
META=ROOT/'work/part_d_attack/actual_transporter_class_two_and_gt0_result.json'
def bind(p):
    p=ROOT/p if isinstance(p,str) else p
    b=p.read_bytes()
    return {'path':str(p.relative_to(ROOT)),'bytes':len(b),'sha256':sha256(b).hexdigest()}
meta=json.loads(META.read_text())
frozen=[]
for entry in meta['files']+meta['dependencies']:
    row=bind(entry['path'])
    assert row['sha256']==entry['sha256'] and row['bytes']==entry['bytes']
    frozen.append(row)
frozen.append(bind(META))
src=ROOT/'work/part_d_attack/code/actual_transporter_class_two.py'
dst=OUT/'actual_transporter_class_two.py'
shutil.copyfile(src,dst)
assert src.read_bytes()==dst.read_bytes()
run=subprocess.run([sys.executable,str(dst)],cwd=OUT,capture_output=True)
(OUT/'replay_stdout.txt').write_bytes(run.stdout)
(OUT/'replay_stderr.txt').write_bytes(run.stderr)
assert run.returncode==0 and not run.stderr
generated=OUT/'actual_transporter_class_two_output.json'
original=ROOT/'work/part_d_attack/code/actual_transporter_class_two_output.json'
original_stdout=ROOT/'work/part_d_attack/code/actual_transporter_class_two_stdout.txt'
assert generated.read_bytes()==run.stdout==original.read_bytes()==original_stdout.read_bytes()
data=json.loads(run.stdout)
assert data['status']=='PASS' and data['assertion_count']==38
assert len(data['checks'])==38 and all(r['passed'] for r in data['checks'])
assert data['total_coordinate_formula_cases']==144824
assert data['total_sign_identity_cases']==17892
for row in frozen:
    assert bind(row['path'])==row
record={'status':'PASS','reviewer':'/root/c89_review_and_general_c',
        'created_utc':datetime.now(timezone.utc).isoformat(),'exit_code':0,
        'named_checks':38,'coordinate_formula_cases':144824,'sign_identity_cases':17892,
        'whole_output_and_stdout_raw_bytes_identical':True,'path_transport_used':False,
        'frozen_files_unchanged':frozen,
        'replay_files':[bind(dst),bind(generated),bind(OUT/'replay_stdout.txt'),bind(OUT/'replay_stderr.txt')],
        'modulus_summary':[{k:v for k,v in r.items() if k not in ('class_two_root_rows','GT0_coefficient_rows')} for r in data['rows']],
        'checks':data['checks'],'runner':bind(Path(__file__).resolve())}
target=OUT/'comparison.json'
target.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'status':'PASS','named_checks':38,'comparison':bind(target),'metadata':bind(META)},indent=2))
