"""Fresh copied-source D53 executions; only named elapsed-time fields excluded."""
from pathlib import Path
import hashlib,json,shutil,subprocess,sys

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
SOURCE=ROOT/'D53_EXPERIMENTS'
digest=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
manifest=json.loads((SOURCE/'ledger/d_arithmetic_correction_space_manifest.json').read_text())
for row in manifest['files']+manifest['runtime_inputs']:
    assert digest(SOURCE/row['path'])==row['sha256'],row['path']
(HERE/'code').mkdir(exist_ok=True)
for row in manifest['runtime_inputs']:
    p=SOURCE/row['path'];shutil.copyfile(p,HERE/'code'/p.name)
stages=[];compared=[]
for name in manifest['run_order']:
    p=HERE/'code'/name;assert not p.exists()
    shutil.copyfile(SOURCE/'code'/name,p)
    with p.with_suffix('.out').open('w')as output:
        proc=subprocess.run([sys.executable,str(p)],stdout=output,stderr=subprocess.STDOUT,cwd=HERE,check=False)
    stages.append({'program':name,'exit_code':proc.returncode,'program_sha256':digest(p)})
    (HERE/'run_status.json').write_text(json.dumps(stages,indent=2)+'\n')
    assert proc.returncode==0,stages[-1]
    for suffix,field in [('.json','summary'),('.out',None)]:
        original=SOURCE/'code'/p.with_suffix(suffix).name;fresh=p.with_suffix(suffix)
        a=json.loads(original.read_text());b=json.loads(fresh.read_text())
        if field is None:
            oa=a.pop('elapsed_seconds');ob=b.pop('elapsed_seconds');excluded='/elapsed_seconds'
        else:
            oa=a[field].pop('elapsed_seconds');ob=b[field].pop('elapsed_seconds');excluded='/summary/elapsed_seconds'
        assert a==b,(name,suffix)
        compared.append({'file':fresh.name,'source_sha256':digest(original),
            'fresh_sha256':digest(fresh),'all_remaining_fields_equal':True,
            'only_excluded_field':excluded,'recorded_elapsed_values':[oa,ob]})
    print('PASS '+name+': complete JSON/stdout except only named elapsed fields',flush=True)
for row in manifest['runtime_inputs']:
    assert digest(HERE/row['path'])==row['sha256']
record={'status':'PASS','section_sha256':digest(SOURCE/'sections/D_arithmetic_correction_space.tex'),
        'frozen_manifest_sha256':digest(SOURCE/'ledger/d_arithmetic_correction_space_manifest.json'),
        'stages':stages,'complete_comparisons':compared,'inputs':manifest['runtime_inputs']}
(HERE/'comparison.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2),flush=True)
