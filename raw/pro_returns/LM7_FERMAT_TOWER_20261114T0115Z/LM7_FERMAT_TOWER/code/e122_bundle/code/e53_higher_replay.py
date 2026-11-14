#!/usr/bin/env python3
"""Replay the complete E122 theorem certificate from literal inputs only."""
from pathlib import Path
import argparse,hashlib,json,shutil,subprocess,sys
R=Path(__file__).resolve().parents[1]
ap=argparse.ArgumentParser();ap.add_argument('--gp',required=True);ap.add_argument('--destination');a=ap.parse_args()
gp=str(Path(a.gp).resolve());dest=Path(a.destination).resolve() if a.destination else R/'audit/author_replay'
assert not dest.exists(),'Retain existing executions; choose a new destination.'
fresh=dest/'fresh';(fresh/'code').mkdir(parents=True);shutil.copytree(R/'inputs',fresh/'inputs')
names=['e53_higher_local','e53_higher_genus','e53_upper_witness_verify']
sources=['code/e53_higher_maps.py','code/e53_literal_unit_ring.py']+['code/'+n+'.gp' for n in names]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for rel in sources:shutil.copyfile(R/rel,fresh/rel)
run=subprocess.run([sys.executable,str(fresh/'code/e53_higher_maps.py'),'--gp',gp],cwd=fresh/'code',stdout=subprocess.PIPE,stderr=subprocess.PIPE)
(fresh/'code/e53_higher_maps.out').write_bytes(run.stdout);(fresh/'code/e53_higher_maps.err').write_bytes(run.stderr)
assert run.returncode==0,(run.returncode,run.stderr.decode()[-4000:])
texts=['code/e53_higher_maps.out','code/e53_higher_maps.json','code/e53_literal_unit_ring.out','code/e53_literal_unit_ring.json']+['code/'+n+'.out' for n in names]
tc={}
for rel in texts:
    assert (R/rel).read_bytes()==(fresh/rel).read_bytes(),rel
    tc[rel]={'byte_identical':True,'sha256':sha(R/rel)}
bs=['code/'+n+'.bin' for n in names]
lines=['default(parisizemax,2000000000);','allocatemem(256000000);']
bc={}
for rel in bs:
    lines+=['a=read('+json.dumps(str(R/rel))+');','b=read('+json.dumps(str(fresh/rel))+');',
            'if(!(a===b),error('+json.dumps('Complete object mismatch '+rel)+'));',
            'print('+json.dumps('PASS complete GEN '+rel)+');']
    bc[rel]={'author_sha256':sha(R/rel),'fresh_sha256':sha(fresh/rel),'raw_byte_identity':(R/rel).read_bytes()==(fresh/rel).read_bytes()}
lines+=['print("PASS all complete PARI objects");','quit(0);']
p=dest/'compare_binary.gp';p.write_text('\n'.join(lines)+'\n')
c=subprocess.run([gp,'-fq',str(p)],cwd=dest,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
(dest/'compare_binary.out').write_bytes(c.stdout);(dest/'compare_binary.err').write_bytes(c.stderr)
assert c.returncode==0 and b'PASS all complete PARI objects' in c.stdout
assert all('Warning:' in line for line in c.stderr.decode().splitlines() if line.strip()),c.stderr.decode()
for v in bc.values():v['complete_decoded_GEN_identity']=True
d={'statement':'E.122','status':'PASS','GP_stages':3,'independent_relative_ring_stage':True,
   'copy_scope':'Only the owned five mathematical sources and literal lower/witness inputs; no prior E122 result or upper NF/BNF is copied.',
   'texts':tc,'binary_objects':bc,'source_sha256':{f:sha(R/f) for f in sources},
   'excluded_fields':[],'excluded_GEN_components':[]}
t=json.dumps(d,indent=2)+'\n';(dest/'replay.json').write_text(t);(R/'code/e53_higher_replay.json').write_text(t);print(t,end='')
