"""Independent copied-source D54 reconstruction and complete result comparison."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
SOURCE=ROOT/'D54_EXPERIMENTS'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
manifest_path=SOURCE/'ledger/d_doubled_class2_corrections_manifest.json'
manifest=json.loads(manifest_path.read_text())
for row in manifest['files']+manifest['runtime_inputs']:
    assert sha(SOURCE/row['path'])==row['sha256'],row['path']
code=HERE/'code';code.mkdir(exist_ok=True)
for row in manifest['runtime_inputs']:
    target=code/Path(row['path']).name
    assert not target.exists()
    shutil.copyfile(SOURCE/row['path'],target)
stages=[]
for name in manifest['run_order']:
    target=code/name
    assert not target.exists()
    shutil.copyfile(SOURCE/'code'/name,target)
    with target.with_suffix('.out').open('w') as output:
        run=subprocess.run([sys.executable,str(target)],cwd=HERE,stdout=output,
                           stderr=subprocess.STDOUT,check=False)
    assert run.returncode==0,(name,run.returncode)
    stages.append({'program':name,'sha256':sha(target),'exit_code':run.returncode})
comparisons=[]
for name in manifest['run_order']:
    for ext in ['.json','.out']:
        original=SOURCE/'code'/Path(name).with_suffix(ext)
        rebuilt=code/Path(name).with_suffix(ext)
        a,b=(json.loads(p.read_text()) for p in [original,rebuilt])
        aa,bb=(x['summary'] if ext=='.json' else x for x in [a,b])
        times=[aa.pop('elapsed_seconds'),bb.pop('elapsed_seconds')]
        assert a==b,original.name
        comparisons.append({'file':original.name,'source_sha256':sha(original),
                            'fresh_sha256':sha(rebuilt),'all_remaining_fields_equal':True,
                            'only_excluded_field':'/summary/elapsed_seconds' if ext=='.json' else '/elapsed_seconds',
                            'actual_elapsed_values':times})
for row in manifest['runtime_inputs']:
    assert sha(code/Path(row['path']).name)==row['sha256']
record={'status':'PASS','section_sha256':sha(SOURCE/'sections/D_doubled_class2_corrections.tex'),
        'frozen_manifest_sha256':sha(manifest_path),'stages':stages,
        'complete_comparisons':comparisons,'inputs':manifest['runtime_inputs']}
(HERE/'comparison.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2),flush=True)
