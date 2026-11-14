"""Independent complete copied D55 reconstruction and elapsed-only comparison."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import shutil
import subprocess
import sys

HERE=Path(__file__).resolve().parent;SOURCE=HERE.parent/'D55_EXPERIMENTS'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
manifest_path=SOURCE/'ledger/d_arithmetic_boundary_norm_manifest.json'
manifest=json.loads(manifest_path.read_text())
for row in manifest['files']+manifest['runtime_inputs']:
    assert sha(SOURCE/row['path'])==row['sha256'],row['path']
code=HERE/'code';code.mkdir(exist_ok=True)
for row in manifest['runtime_inputs']:
    target=code/Path(row['path']).name;assert not target.exists()
    shutil.copyfile(SOURCE/row['path'],target)
for name in manifest['run_order']:
    assert not (code/name).exists();shutil.copyfile(SOURCE/'code'/name,code/name)
def run(name):
    target=code/name
    with target.with_suffix('.out').open('w') as out:
        result=subprocess.run([sys.executable,str(target)],cwd=HERE,stdout=out,stderr=subprocess.STDOUT,check=False)
    assert result.returncode==0,(name,result.returncode)
    return {'program':name,'source_sha256':sha(target),'returncode':result.returncode}
assert manifest['programs_independent']
with ThreadPoolExecutor(max_workers=2) as pool:
    stages=list(pool.map(run,manifest['run_order']))
comparisons=[]
for name in manifest['run_order']:
    assert sha(code/name)==sha(SOURCE/'code'/name)
    for ext in ['.json','.out']:
        original=(SOURCE/'code'/name).with_suffix(ext);fresh=(code/name).with_suffix(ext)
        texts=[p.read_text() for p in [original,fresh]]
        starts=[t.index('{') for t in texts]
        assert texts[0][:starts[0]]==texts[1][:starts[1]]
        a,b=[json.loads(t[i:]) for t,i in zip(texts,starts)]
        aa,bb=[x['summary'] if ext=='.json' else x for x in [a,b]]
        times=[aa.pop('elapsed_seconds'),bb.pop('elapsed_seconds')]
        assert a==b,original.name
        comparisons.append({'file':original.name,'source_sha256':sha(original),'fresh_sha256':sha(fresh),
                            'complete_prefix_equal':True,'all_remaining_fields_equal':True,
                            'only_excluded_field':'/summary/elapsed_seconds' if ext=='.json' else '/elapsed_seconds',
                            'actual_elapsed_values':times})
for row in manifest['runtime_inputs']:
    assert sha(SOURCE/row['path'])==sha(code/Path(row['path']).name)==row['sha256']
result={'status':'PASS','section_sha256':sha(SOURCE/'sections/D_arithmetic_boundary_norm.tex'),
        'frozen_manifest_sha256':sha(manifest_path),'stages':stages,
        'complete_comparisons':comparisons,'unchanged_runtime_inputs':manifest['runtime_inputs']}
(HERE/'comparison.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS both fresh D55 programs; all complete JSON/stdout fields agree except the named elapsed times.',flush=True)
