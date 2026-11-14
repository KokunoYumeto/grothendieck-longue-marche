#!/usr/bin/env python3
"""Run each complete D62 source in a fresh copied directory and compare all output."""
from pathlib import Path
import hashlib
import json
import re
import shutil
import subprocess
import sys

here=Path(__file__).resolve().parent
work=here.parent
author=work/'D62_EXPERIMENTS'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
manifest=author/'ledger/d_self_wedge_actual_corrections_manifest.json'
assert sha(manifest)=='66a05d0534733dc7f6002488f20b45644fefe10c6adae1ad4168497d0ad3c68c'
m=json.loads(manifest.read_text())
for row in m['files']+m['immutable_inputs']:
    p=author/row['path']
    assert p.stat().st_size==row['bytes'] and sha(p)==row['sha256'],row['path']
fresh=here/'fresh'
assert not fresh.exists()
fresh.mkdir()

def without_elapsed(obj):
    if isinstance(obj,dict):
        return {k:without_elapsed(v) for k,v in obj.items() if k!='elapsed_seconds'}
    if isinstance(obj,list):
        return [without_elapsed(v) for v in obj]
    return obj

def stdout_without_elapsed(raw):
    return re.sub(rb'("elapsed_seconds"\s*:\s*)[0-9.eE+-]+',rb'\1<elapsed_seconds>',raw)

runs=[]
for name in m['run_order']:
    dest=fresh/Path(name).stem
    dest.mkdir()
    source=author/'code'/name
    shutil.copy2(source,dest/name)
    inputs=[]
    for dep in m['replay_dependencies'][name]:
        p=author/'code'/dep
        shutil.copy2(p,dest/dep)
        inputs.append({'file':dep,'sha256':sha(p)})
    command=[sys.executable,str(dest/name)]
    run=subprocess.run(command,cwd=dest,capture_output=True)
    out=dest/Path(name).with_suffix('.out')
    err=dest/Path(name).with_suffix('.err')
    out.write_bytes(run.stdout)
    err.write_bytes(run.stderr)
    assert run.returncode==0 and not run.stderr,(name,run.returncode,run.stderr.decode())
    baseline=author/'code'/Path(name).with_suffix('.json')
    reproduced=dest/Path(name).with_suffix('.json')
    a=json.loads(baseline.read_text());b=json.loads(reproduced.read_text())
    assert without_elapsed(a)==without_elapsed(b),name+' complete JSON'
    original_out=source.with_suffix('.out')
    assert stdout_without_elapsed(original_out.read_bytes())==stdout_without_elapsed(run.stdout),name+' complete stdout'
    assert source.read_bytes()==(dest/name).read_bytes()
    record={'program':name,'actual_exit_code':run.returncode,'source_sha256':sha(source),
            'inputs':inputs,'full_JSON_equal_except_elapsed_seconds':True,
            'full_stdout_equal_except_elapsed_seconds':True,'stderr_bytes':len(run.stderr),
            'author_json_sha256':sha(baseline),'fresh_json_sha256':sha(reproduced),
            'author_stdout_sha256':sha(original_out),'fresh_stdout_sha256':sha(out),
            'excluded_field':'elapsed_seconds'}
    runs.append(record)
    print(json.dumps(record),flush=True)
for row in m['files']+m['immutable_inputs']:
    assert sha(author/row['path'])==row['sha256'],row['path']
result={'status':'PASS','statement':'D.62','manifest_sha256':sha(manifest),
        'proof_sha256':m['section_sha256'],'owned_manifest_files_verified':len(m['files']),
        'immutable_inputs_verified':len(m['immutable_inputs']),
        'all_frozen_author_files_unchanged':True,'complete_fresh_programs':runs,
        'only_excluded_field':'elapsed_seconds',
        'scope':'Actual full copied replay of four author programs. Separate root mathematical proof/source inspection and separate peer independent-map execution are recorded in their own audits.'}
(here/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':'PASS','programs':len(runs),'record_sha256':sha(here/'verification.json')},indent=2),flush=True)
