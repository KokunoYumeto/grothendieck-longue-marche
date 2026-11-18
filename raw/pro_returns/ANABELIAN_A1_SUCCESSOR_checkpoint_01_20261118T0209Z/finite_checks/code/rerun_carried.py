"""Rerun supplied certificates without changing their source; record hashes.
The input files remain identified by their paths in the attached archive.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor,as_completed
import subprocess,os,sys,json,hashlib,time,shutil
root=Path(__file__).resolve().parent.parent
src=root.parents[1]/'background'/'A1_checkpoint03'/'code'
dst=root/'carried_reruns';dst.mkdir(exist_ok=True)
jobs=[('primitive_verify.py',[]),('criterion_r8_verify.py',[]),
 ('criterion_quartic13_verify.py',[]),('criterion_quartic5_verify.py',[]),
 ('criterion_quartic3_f5_verify.py',[]),('criterion_abelian_norm.py',[]),
 ('verify_abelian_norm.py',[]),('criterion_norm_module.py',[]),
 ('criterion_solvable_norm.py',[]),('criterion_nonabelian_norm_verify.py',[]),
 ('isolating_lang_covers.py',[]),('pointed_quartic_tests.py',[]),
 ('b5_char2_13_certificate.py',[]),('c0_cyclic13_verify.py',[]),
 ('r8_rational_witness.py',['191']),('r8_rational_witness.py',['229'])]
# Every job gets an isolated directory, so input certificates are not
# overwritten before another verifier can read them.
def run(job):
 name,args=job;tag=Path(name).stem+('_'+'_'.join(args) if args else '')
 d=dst/tag;d.mkdir(exist_ok=True)
 shutil.copy2(src/name,d/name)
 if name=='b5_char2_13_certificate.py':shutil.copy2(src/'b5_char2_probe.py',d/'b5_char2_probe.py')
 for f in src.glob('*.json'):shutil.copy2(f,d/f.name)
 if name=='primitive_verify.py':shutil.copytree(src/'primitive_certificates',d/'primitive_certificates',dirs_exist_ok=True)
 env=os.environ.copy();env['PYTHONPATH']=str(root/'runtime_deps')
 start=time.time()
 with (d/'run.out').open('w') as f:
  proc=subprocess.run([sys.executable,str(d/name),*args],stdout=f,stderr=subprocess.STDOUT,env=env)
 rec={'input_archive_path':'A1_checkpoint03/code/'+name,'args':args,
      'source_sha256':hashlib.sha256((src/name).read_bytes()).hexdigest(),
      'exit_code':proc.returncode,'seconds':time.time()-start,'output':str((d/'run.out').relative_to(root)),
      'type':'rerun of supplied program, not newly independently implemented'}
 print(json.dumps(rec),flush=True);return rec
ans=[]
with ThreadPoolExecutor(max_workers=3) as pool:
 fs={pool.submit(run,j):j for j in jobs}
 for f in as_completed(fs):
  ans.append(f.result());(dst/'RERUN_LEDGER.json').write_text(json.dumps(ans,indent=2)+'\n')
print('ALL JOBS FINISHED',len(ans),'FAILURES',sum(a['exit_code']!=0 for a in ans),flush=True)
