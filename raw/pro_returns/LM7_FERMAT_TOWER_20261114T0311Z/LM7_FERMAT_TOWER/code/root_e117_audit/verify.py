#!/usr/bin/env python3
"""Reconstruct the complete frozen E117 arithmetic from copied source and inputs."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys

root=Path(__file__).resolve().parent;work=root.parent
author=work/'research_e117'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
manifest=author/'ledger/e_quartic_three_manifest.json'
assert sha(manifest)=='73e6772cd5c31a6e609d42e80903c2f16ed5388124c8e7b760ff4af0e293287b'
m=json.loads(manifest.read_text());rows=m['files']
if isinstance(rows,dict):rows=[dict(path=k,**v) for k,v in rows.items()]
for row in rows:
    p=author/row['path'];assert sha(p)==row['sha256'],str(p)
    if 'bytes' in row:assert p.stat().st_size==row['bytes']
assert sha(author/'sections/E_quartic_three.tex')=='de1d67c7ae1e6e52850e57f51c6fa10a904e14eb1d8092471ee2a0002073da59'
fresh=root/'fresh';assert not fresh.exists();(fresh/'code').mkdir(parents=True);(fresh/'inputs').mkdir()
for name in ['a_quartic_three.py','a_quartic_three_fields.gp']:
    shutil.copy2(author/'code'/name,fresh/'code'/name)
deps=json.loads((author/'ledger/e_quartic_three_dependencies.json').read_text())
for row in deps['inputs']:
    p=author/row['path'];assert sha(p)==row['sha256'];shutil.copy2(p,fresh/'inputs'/p.name)
gp=work/'research_e52/vendor/pari-2.19.0/gp'
command=[sys.executable,str(fresh/'code/a_quartic_three.py'),'--gp',str(gp)]
run=subprocess.run(command,cwd=fresh,capture_output=True)
(fresh/'code/a_quartic_three.out').write_bytes(run.stdout)
(fresh/'code/a_quartic_three.err').write_bytes(run.stderr)
assert run.returncode==0,run.stderr.decode()
assert run.stderr==b'',run.stderr.decode()
comparisons=[]
for name in ['a_quartic_three.py','a_quartic_three_fields.gp','a_quartic_three.out','a_quartic_three.json','a_quartic_three_fields.out']:
    a=author/'code'/name;b=fresh/'code'/name
    assert a.read_bytes()==b.read_bytes(),name
    comparisons.append({'file':name,'byte_equal':True,'sha256':sha(a),'bytes':a.stat().st_size})
a=author/'code/a_quartic_three_fields.bin';b=fresh/'code/a_quartic_three_fields.bin'
comparison=root/'compare_binary.gp'
comparison.write_text('default(parisize,128000000);\n'
    +'a=read('+json.dumps(str(a))+');\n'
    +'b=read('+json.dumps(str(b))+');\n'
    +'if(a!=b,print("FAIL complete GEN equality");quit(1));\n'
    +'for(k=1,#a,if(a[k]!=b[k],print("FAIL component ",k);quit(1)));\n'
    +'print("PASS complete GEN equality; all ",#a," field records and every nested BNF component equal");\nquit(0);\n')
check=subprocess.run([str(gp),'-q','-f',str(comparison)],cwd=root,capture_output=True)
comparison.with_suffix('.out').write_bytes(check.stdout);comparison.with_suffix('.err').write_bytes(check.stderr)
assert check.returncode==0 and check.stdout.startswith(b'PASS complete GEN equality'),check.stdout+check.stderr
for row in rows:assert sha(author/row['path'])==row['sha256'],row['path']
result={'status':'PASS','statement':'E.117','manifest_sha256':sha(manifest),'manifest_files_verified':len(rows),
        'proof_sha256':sha(author/'sections/E_quartic_three.tex'),'actual_exit_code':run.returncode,
        'command':command,'whole_file_comparisons':comparisons,'excluded_fields':[],
        'binary':{'raw_byte_equal':a.read_bytes()==b.read_bytes(),'author_sha256':sha(a),'fresh_sha256':sha(b),
                  'complete_deserialized_GEN_equal':True,'comparison_source_sha256':sha(comparison),
                  'comparison_output_sha256':sha(comparison.with_suffix('.out')),'comparison_exit_code':check.returncode},
        'all_frozen_author_files_unchanged':True,
        'scope':'Actual complete copied-source/input execution and whole-output comparisons; mathematical proof inspection is recorded separately.'}
(root/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
