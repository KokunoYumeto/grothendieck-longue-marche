#!/usr/bin/env python3
"""Fresh, portable replay of all final E123 mathematics; no BNF search is run."""
from pathlib import Path
import argparse,hashlib,json,shutil,subprocess,sys
R=Path(__file__).resolve().parents[1]
ap=argparse.ArgumentParser()
ap.add_argument('--gp',required=True)
ap.add_argument('--label',default='author_replay')
a=ap.parse_args();gp=str(Path(a.gp).resolve())
D=R/'audit'/a.label
assert not D.exists(),str(D)
F=D/'fresh';C=F/'code';C.mkdir(parents=True)
shutil.copytree(R/'inputs',F/'inputs')
sources=['e53_positional_unit.py','e53_positional_verify.gp',
 'e53_positional_genus_pivots.gp','e53_positional_presentation.gp',
 'e53_positional_lower_export.gp','e53_positional_make_ideals.py',
 'e53_positional_ideals.gp','e53_positional_maps.py']
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
before={n:sha(R/'code'/n) for n in sources}
for n in sources:shutil.copy2(R/'code'/n,C/n)
steps=[]
for name in sources:
 stem=Path(name).stem
 cmd=[gp,'-q','-f',name] if name.endswith('.gp') else [sys.executable,name]
 run=subprocess.run(cmd,cwd=C,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 (C/(stem+'.out')).write_bytes(run.stdout)
 (C/(stem+'.err')).write_bytes(run.stderr)
 expected=(R/'code'/(stem+'.out')).read_bytes()
 errref=R/'code'/(stem+'.err')
 expectederr=errref.read_bytes() if errref.exists() else b''
 row={'source':name,'exit_code':run.returncode,
      'stdout_byte_identity':run.stdout==expected,
      'stderr_byte_identity':run.stderr==expectederr,
      'stdout_sha256':sha(C/(stem+'.out')),'stderr_sha256':sha(C/(stem+'.err'))}
 steps.append(row)
 (D/'progress.json').write_text(json.dumps(steps,indent=2)+'\n')
 assert run.returncode==0 and row['stdout_byte_identity'] and row['stderr_byte_identity'],row
 for ext in ['.json']:
  ref=R/'code'/(stem+ext);fresh=C/(stem+ext)
  if ref.exists():
   assert fresh.exists() and fresh.read_bytes()==ref.read_bytes(),str(fresh)
assert all(sha(R/'code'/n)==h for n,h in before.items())
assert sha(C/'e53_positional_ideals.gp')==before['e53_positional_ideals.gp']
bins=['e53_positional_genus_pivots.bin','e53_positional_presentation.bin']
gptext=['check(a,s)=if(!a,error(s));','{']
for i,n in enumerate(bins):
 q=json.dumps(str(R/'code'/n));f=json.dumps(str(C/n))
 gptext+=['my(a'+str(i)+'=read('+q+'),b'+str(i)+'=read('+f+'));',
          'check(a'+str(i)+'===b'+str(i)+',"complete GEN equality");',
          'print("{\\"file\\":\\"'+n+'\\",\\"complete_GEN_identity\\":true,\\"components\\":",#a'+str(i)+',"}");']
gptext+=['print("{\\"status\\":\\"PASS\\",\\"scope\\":\\"whole decoded objects; no component exclusions\\"}");','}','quit;','']
(D/'compare_binary.gp').write_text('\n'.join(gptext))
run=subprocess.run([gp,'-q','-f','compare_binary.gp'],cwd=D,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
(D/'compare_binary.out').write_bytes(run.stdout);(D/'compare_binary.err').write_bytes(run.stderr)
assert run.returncode==0 and not run.stderr.strip(),(run.returncode,run.stderr)
rr=[json.loads(s) for s in run.stdout.decode().splitlines() if s.startswith('{')]
assert rr[-1]['status']=='PASS' and len(rr)==3
out={'status':'PASS','steps':steps,'source_hashes':before,
 'JSON_byte_identity':['e53_positional_unit.json','e53_positional_maps.json'],
 'generated_standalone_source_byte_identity':True,
 'complete_binary_comparisons':rr[:-1],
 'binary_serialization':{n:{'reference_sha256':sha(R/'code'/n),'fresh_sha256':sha(C/n),
       'raw_byte_identity':(R/'code'/n).read_bytes()==(C/n).read_bytes()} for n in bins},
 'excluded_fields':[],'costly_BNF_reconstruction_or_certification':False,
 'scope':'eight source-only final stages with complete stdout, stderr and JSON comparisons; two entire decoded PARI objects'}
s=json.dumps(out,indent=2)+'\n';(D/'verification.json').write_text(s)
(R/'code/e53_positional_replay.json').write_text(s);print(s,end='')

