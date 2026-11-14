#!/usr/bin/env python3
"""Six complete root replays of frozen D64, with exact immutable inputs."""
from pathlib import Path
import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys

HERE=Path(__file__).resolve().parent
AUTHOR=HERE.parent/'D64_EXPERIMENTS'
MANIFEST=AUTHOR/'ledger/d_compact_isometry_source_manifest.json'
PROOF=AUTHOR/'sections/D_compact_isometry_source.tex'
arg=argparse.ArgumentParser()
arg.add_argument('--manifest-sha256',required=True)
arg.add_argument('--proof-sha256',required=True)
args=arg.parse_args()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(MANIFEST)==args.manifest_sha256
assert sha(PROOF)==args.proof_sha256
manifest=json.loads(MANIFEST.read_text())
def check_freeze():
    assert sha(MANIFEST)==args.manifest_sha256
    assert sha(PROOF)==args.proof_sha256
    for item in manifest['owned_files']+manifest['immutable_inputs']:
        p=AUTHOR/item['path']
        assert sha(p)==item['sha256'] and p.stat().st_size==item['bytes'],item['path']
check_freeze()
fresh=HERE/'fresh'
assert not fresh.exists()
fresh.mkdir()
names=['d_residual_compact_norm','d_residual_compact_pairing',
       'd_residual_compact_isometry','d_residual_compact_cusp',
       'd_residual_compact_coin_action','d_residual_compact_extension']
def without_elapsed(x):
    if isinstance(x,dict):return {k:without_elapsed(v) for k,v in x.items() if k!='elapsed_seconds'}
    if isinstance(x,list):return [without_elapsed(v) for v in x]
    return x
def elapsed_paths(x,prefix=''):
    out=[]
    if isinstance(x,dict):
        for k,v in x.items():
            at=prefix+'/'+k
            if k=='elapsed_seconds':out.append(at)
            else:out.extend(elapsed_paths(v,at))
    elif isinstance(x,list):
        for i,v in enumerate(x):out.extend(elapsed_paths(v,prefix+'/'+str(i)))
    return out
def stdout_without_elapsed(s):
    return re.sub(r'("elapsed_seconds"\s*:\s*)[0-9.eE+-]+',r'\1<elapsed_seconds>',s)
rows=[]
for name in names:
    code=AUTHOR/'code'
    expected=json.loads((code/(name+'.json')).read_text())
    inputs=expected['input_sha256']
    work=fresh/name
    work.mkdir()
    copied=[name+'.py']+list(inputs)
    for file in copied:
        shutil.copy2(code/file,work/file)
    before={file:sha(work/file) for file in copied}
    assert all(before[file]==value for file,value in inputs.items())
    run=subprocess.run([sys.executable,name+'.py'],cwd=work,
                       stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    (work/(name+'.out')).write_bytes(run.stdout)
    (work/(name+'.err')).write_bytes(run.stderr)
    assert run.returncode==0,(name,run.returncode,run.stderr.decode())
    actual=json.loads((work/(name+'.json')).read_text())
    assert actual['summary']['status']=='PASS'
    assert elapsed_paths(actual)==elapsed_paths(expected)==['/summary/elapsed_seconds']
    assert without_elapsed(actual)==without_elapsed(expected),name
    assert stdout_without_elapsed(run.stdout.decode())==stdout_without_elapsed((code/(name+'.out')).read_text()),name
    assert before=={file:sha(work/file) for file in copied}
    rows.append({'program':name,'exit_code':run.returncode,'stderr_bytes':len(run.stderr),
                 'source_sha256':before[name+'.py'],'copied_input_sha256':inputs,
                 'full_json_equal_except_elapsed_seconds':True,
                 'full_stdout_equal_except_elapsed_seconds':True,
                 'excluded_json_paths':elapsed_paths(actual),
                 'excluded_stdout_field':'elapsed_seconds',
                 'author_json_sha256':sha(code/(name+'.json')),
                 'root_json_sha256':sha(work/(name+'.json')),
                 'author_stdout_sha256':sha(code/(name+'.out')),
                 'root_stdout_sha256':sha(work/(name+'.out')),
                 'copied_inputs_and_source_unchanged':True})
    print('PASS complete isolated root replay: '+name,flush=True)
check_freeze()
result={'statement':'D.64','status':'PASS_ROOT_SIX_COMPLETE_REPLAYS',
        'manifest_sha256':sha(MANIFEST),'proof_sha256':sha(PROOF),
        'owned_files_checked_before_and_after':len(manifest['owned_files']),
        'immutable_inputs_checked_before_and_after':len(manifest['immutable_inputs']),
        'programs':rows,
        'scope':'Each of the six full mathematical sources was executed in its own fresh directory with exact copied immutable source inputs. All D64 producer programs were separately replayed. Whole stdout and whole JSON were compared after excluding only the displayed elapsed_seconds values; every actual unmodified output is retained.'}
(HERE/'replay.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
