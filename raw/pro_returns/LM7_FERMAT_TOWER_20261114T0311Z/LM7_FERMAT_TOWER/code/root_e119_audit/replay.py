#!/usr/bin/env python3
"""Root replay of frozen E119 from eleven copied mathematical sources only."""
from pathlib import Path
import hashlib,json,shutil,subprocess,sys

HERE=Path(__file__).resolve().parent
AUTHOR=HERE.parent/'research_e119'
GP=HERE.parent/'research_e52/vendor/pari-2.19.0/gp'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
MANIFEST=AUTHOR/'ledger/e_lower_fiftythree_manifest.json'
assert sha(MANIFEST)=='79d424d7f19195b64260847b54544206615d0ed4c3f1011e8f88dc4392d6831d'
assert sha(AUTHOR/'sections/E_lower_fiftythree.tex')=='25d9250dabab99ca3848525d608ed6968323cdc58400f75b8d074a90d79759c0'
manifest=json.loads(MANIFEST.read_text())
def frozen_check():
    for name,item in manifest['files'].items():
        p=AUTHOR/name
        assert p.stat().st_size==item['bytes'] and sha(p)==item['sha256'],name
frozen_check()
FRESH=HERE/'fresh'
assert not FRESH.exists()
for sub in ('code','inputs'):(FRESH/sub).mkdir(parents=True)
expected=json.loads((AUTHOR/'code/e_lower_fiftythree_replay.json').read_text())
sources=[Path('code/e_lower_fiftythree.py')]+[Path(x) for x in expected['source_sha256'] if x!='code/e_lower_fiftythree.py']
assert len(sources)==11 and len(set(sources))==11
for name in sources:
    shutil.copy2(AUTHOR/name,FRESH/name)
    assert sha(FRESH/name)==sha(AUTHOR/name)
assert not list(FRESH.rglob('*.bin'))
command=[sys.executable,str(FRESH/'code/e_lower_fiftythree.py'),'--gp',str(GP)]
run=subprocess.run(command,cwd=FRESH/'code',stdout=subprocess.PIPE,stderr=subprocess.PIPE)
(FRESH/'code/e_lower_fiftythree.out').write_bytes(run.stdout)
(FRESH/'code/e_lower_fiftythree.err').write_bytes(run.stderr)
assert run.returncode==0,(run.returncode,run.stderr.decode()[-2500:])
text_checks={}
for name in expected['text_outputs']:
    a,b=AUTHOR/name,FRESH/name
    assert a.read_bytes()==b.read_bytes(),name
    text_checks[name]={'sha256':sha(a),'bytes':a.stat().st_size,'byte_identical':True}
assert len(text_checks)==12
lines=['default(parisizemax,1000000000);','allocatemem(256000000);']
binary_checks={}
for name in expected['binary_objects']:
    a,b=AUTHOR/name,FRESH/name
    assert b.is_file(),name
    lines.extend(['a=read('+json.dumps(str(a))+');','b=read('+json.dumps(str(b))+');',
        'if(!(a===b),error('+json.dumps('Complete GEN mismatch: '+name)+'));',
        'print('+json.dumps('PASS complete GEN: '+name)+');'])
    binary_checks[name]={'author_sha256':sha(a),'replay_sha256':sha(b),'raw_bytes_identical':a.read_bytes()==b.read_bytes()}
lines.extend(['print("PASS all complete PARI objects");','quit(0);'])
(HERE/'compare_binary.gp').write_text('\n'.join(lines)+'\n')
check=subprocess.run([str(GP),'-q','-f',str(HERE/'compare_binary.gp')],cwd=HERE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
(HERE/'compare_binary.out').write_bytes(check.stdout)
(HERE/'compare_binary.err').write_bytes(check.stderr)
assert check.returncode==0 and b'PASS all complete PARI objects' in check.stdout
allowed={'*** allocatemem: Warning: increasing stack size to 256000000.'}
bad=[x for x in check.stderr.decode().splitlines() if '***' in x and not (x.strip() in allowed or x.strip().startswith('***   Warning: new stack size = ') or x.strip().startswith('***   Warning: new maximum stack size = '))]
assert not bad,bad
for item in binary_checks.values():item['complete_decoded_GEN_identical']=True
assert len(binary_checks)==12
frozen_check()
result={'statement':'E.119','status':'PASS_ROOT_FROZEN_SOURCE_REPLAY','command':command,
    'GP_stages':10,'copied_mathematical_sources':11,'no_precomputed_binary_input':True,
    'main_exit_code':run.returncode,'main_stderr_bytes':len(run.stderr),
    'text_outputs':text_checks,'binary_objects':binary_checks,
    'source_sha256':{str(n):sha(AUTHOR/n) for n in sources},
    'manifest_sha256':sha(MANIFEST),'frozen_files_before_and_after':len(manifest['files']),
    'binary_comparison_exit_code':check.returncode,'binary_comparison_stderr_sha256':sha(HERE/'compare_binary.err'),
    'excluded_fields':[],'excluded_binary_components':[],
    'scope':'Root assistant actual ten-stage copied-source reconstruction. Full twelve text-output comparison and full twelve decoded PARI-object comparison; no author success is counted as a root run.'}
(HERE/'replay.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))

