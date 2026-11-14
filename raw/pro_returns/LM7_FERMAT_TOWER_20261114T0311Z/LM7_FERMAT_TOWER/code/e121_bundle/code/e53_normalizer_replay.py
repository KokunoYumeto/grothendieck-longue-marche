#!/usr/bin/env python3
"""Replay all five E121 stages from sources and immutable E119 lower objects."""
from pathlib import Path
import argparse,hashlib,json,shutil,subprocess,sys

ROOT=Path(__file__).resolve().parents[1]
arg=argparse.ArgumentParser()
arg.add_argument('--gp',required=True)
arg.add_argument('--destination')
args=arg.parse_args()
GP=str(Path(args.gp).resolve())
DEST=Path(args.destination).resolve() if args.destination else ROOT/'audit/author_replay'
assert not DEST.exists(),'Retain previous executions and choose a new directory.'
FRESH=DEST/'fresh'
(FRESH/'code').mkdir(parents=True)
shutil.copytree(ROOT/'inputs',FRESH/'inputs')
names=['e53_order_nine_genus','e53_normalizer_actions',
       'e53_horizontal_upper_norm','e53_horizontal_upper_extension',
       'e53_cyclic_nine_comparison']
sources=[Path('code/e53_normalizer_module.py')]
sources += [Path('code')/(n+'.gp') for n in names]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for rel in sources:
    shutil.copy2(ROOT/rel,FRESH/rel)
run=subprocess.run([sys.executable,str(FRESH/'code/e53_normalizer_module.py'),
                    '--gp',GP],cwd=FRESH/'code',stdout=subprocess.PIPE,
                   stderr=subprocess.STDOUT)
(FRESH/'code/e53_normalizer_module.out').write_bytes(run.stdout)
assert run.returncode==0,(run.returncode,run.stdout.decode()[-4000:])
texts=[Path('code/e53_normalizer_module.out'),Path('code/e53_normalizer_module.json')]
texts += [Path('code')/(n+'.out') for n in names]
text_checks={}
for rel in texts:
    a,b=ROOT/rel,FRESH/rel
    assert a.read_bytes()==b.read_bytes(),str(rel)
    text_checks[str(rel)]={'byte_identical':True,'sha256':sha(a)}
binaries=sorted(p.relative_to(ROOT) for p in (ROOT/'code').glob('*.bin'))
lines=['default(parisizemax,1000000000);','allocatemem(256000000);']
binary_checks={}
for rel in binaries:
    a,b=ROOT/rel,FRESH/rel
    assert b.exists(),str(rel)
    lines += ['a=read('+json.dumps(str(a))+');',
              'b=read('+json.dumps(str(b))+');',
              'if(!(a===b),error('+json.dumps('Complete GEN mismatch '+str(rel))+'));',
              'print('+json.dumps('PASS complete GEN '+str(rel))+');']
    binary_checks[str(rel)]={'author_sha256':sha(a),'replay_sha256':sha(b),
                            'raw_bytes_identical':a.read_bytes()==b.read_bytes()}
lines += ['print("PASS all complete PARI objects");','quit(0);']
cp=DEST/'compare_binary.gp'
cp.write_text('\n'.join(lines)+'\n')
check=subprocess.run([GP,'-q','-f',str(cp)],cwd=DEST,stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE)
(DEST/'compare_binary.out').write_bytes(check.stdout)
(DEST/'compare_binary.err').write_bytes(check.stderr)
assert check.returncode==0 and b'PASS all complete PARI objects' in check.stdout
errors=[s for s in check.stderr.decode().splitlines() if '***' in s and not (
    s.strip().startswith('***   Warning: new stack size = ') or
    s.strip().startswith('***   Warning: new maximum stack size = ') or
    s.strip()=='*** allocatemem: Warning: increasing stack size to 256000000.')]
assert not errors,errors
for item in binary_checks.values():
    item['complete_decoded_GEN_identical']=True
result={'statement':'E.121','status':'PASS','GP_stages':5,
        'rebuild_exit_code':run.returncode,
        'copy_scope':'Owned mathematical sources and exact certified E119 lower data objects; no prior E121 output or upper object copied.',
        'text_outputs':text_checks,'binary_objects':binary_checks,
        'source_sha256':{str(r):sha(ROOT/r) for r in sources},
        'input_sha256':{p.relative_to(ROOT).as_posix():sha(p)
                        for p in sorted((ROOT/'inputs').glob('*')) if p.is_file()},
        'excluded_fields':[],'excluded_binary_components':[]}
text=json.dumps(result,indent=2)+'\n'
(DEST/'replay.json').write_text(text)
(ROOT/'code/e53_normalizer_replay.json').write_text(text)
print(text,end='')
