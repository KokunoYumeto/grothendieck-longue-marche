"""Fresh root replay of the exact frozen E114 source and inputs."""
from pathlib import Path
import hashlib,json,shutil,subprocess,sys,time
R=Path(__file__).resolve().parents[1];A=Path(__file__).resolve().parent;S=R/"research_e114"
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
mf=S/'ledger'/"e_inert_tail_manifest.json"
assert sha(mf)=="48305f50a4b98dab82db936e7b3836c2694a9e60038cd41d79aa38d647817b07"
m=json.loads(mf.read_text())
for x in m['files']:
 p=S/x.get('path',x.get('file'))
 assert p.is_file() and sha(p)==x['sha256'],str(p)
 if 'bytes' in x:assert p.stat().st_size==x['bytes']
T=A/'replay';(T/'code').mkdir(parents=True,exist_ok=True);(T/'inputs').mkdir(exist_ok=True)
for name in ["e_inert_tail.py","e_inert_tail.gp","e_inert_tail_orbit.gp"]:
 p=S/'code'/name
 if p.exists():shutil.copy2(p,T/'code'/name)
for name in ["e114_cyclo9_base.bin"]:shutil.copy2(S/'inputs'/name,T/'inputs'/name)
gp=(R/'research_e52/vendor/pari-2.19.0/gp').resolve()
cmd=[sys.executable,str(T/'code'/"e_inert_tail.py"), '--gp',str(gp)]
p=subprocess.run(cmd,cwd=T,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
out=T/'code'/"e_inert_tail.out";out.write_bytes(p.stdout)
checks=[]
for name in ["e_inert_tail.json","e_inert_tail.out","e_inert_tail_orbit.out"]:
 a=S/'code'/name;b=T/'code'/name
 checks.append(dict(file=name,source_sha256=sha(a),replay_sha256=sha(b),complete_byte_equality=a.read_bytes()==b.read_bytes()))
result=dict(statement='E.114',status='PASS' if p.returncode==0 and all(x['complete_byte_equality'] for x in checks) else 'FAIL',actual_exit_code=p.returncode,command=cmd,author_manifest_sha256=sha(mf),manifest_files_verified=len(m['files']),checks=checks,exclusions=[],scope='Exact complete execution replay. Mathematical proof read and source-use audit are recorded separately.')
(A/'replay_result.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
assert result['status']=='PASS'

