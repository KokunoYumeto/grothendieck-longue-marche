#!/usr/bin/env python3
"""Isolated, hash-protected complete replay of E.62.

The destination must not exist.  Frozen E.59 comparison inputs are copied
read-only; no E.59 generation program is run.  Every new mathematical JSON
field and NPZ array is compared, and all generated Schreier certificates
are fully replayed.  Only elapsed-time fields are ignored.
"""
from pathlib import Path
import argparse,hashlib,json,shutil,subprocess,sys,time
import numpy as np

ROOT=Path(__file__).resolve().parent.parent
MANIFEST=ROOT/'research/E62_authoritative_manifest.json'

def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def stable(value):
    if isinstance(value,dict):return {k:stable(v) for k,v in value.items() if not k.endswith('seconds')}
    if isinstance(value,list):return [stable(v) for v in value]
    return value
def final_json(path):
    return json.loads(next(s for s in reversed(path.read_text().splitlines()) if s.startswith('{')))

def main():
    pa=argparse.ArgumentParser();pa.add_argument('--destination',type=Path);pa.add_argument('--check-only',action='store_true')
    args=pa.parse_args();start=time.time();m=json.loads(MANIFEST.read_text())
    for name,row in m['files'].items():assert digest(ROOT/name)==row['sha256'],('protected hash',name)
    if args.check_only:
        print(json.dumps({'status':'PASS_E62_MANIFEST','protected_files':len(m['files']),
                          'input_files':len(m['input_files'])},indent=2));return
    if args.destination is None:pa.error('--destination is required unless --check-only')
    dest=args.destination.resolve()
    if dest.exists():raise SystemExit('Destination exists; choose a fresh isolated directory.')
    code=dest/'code';code.mkdir(parents=True)
    for name in m['input_files']:
        to=dest/name;to.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(ROOT/name,to)
    commands=[]
    def run(name,argv):
        before=time.time()
        with (code/(name+'.out')).open('w') as out,(code/(name+'.err')).open('w') as err:
            p=subprocess.run(argv,cwd=code,stdout=out,stderr=err)
        commands.append({'name':name,'argv':list(map(str,argv)),'exit_code':p.returncode,
                         'seconds':round(time.time()-before,3)})
        (dest/'commands.json').write_text(json.dumps(commands,indent=2)+'\n')
        if p.returncode:raise RuntimeError(f'{name} failed; read its isolated stderr')
        print(name,'PASS',commands[-1]['seconds'],'s',flush=True)
    run('compile_schreier',['g++','-std=c++17','-O3','de_a6_schreier.cpp','-o','de_a6_schreier_fast'])
    for name in ('group','model','source','induced'):
        run('a_cm_gl23_'+name,[sys.executable,'a_cm_gl23_'+name+'.py'])
    run('a_cm_gl23_structure_single',[sys.executable,'a_cm_gl23_structure.py','single'])
    run('a_cm_gl23_joint',[sys.executable,'a_cm_gl23_joint.py'])
    run('a_cm_gl23_structure_joint',[sys.executable,'a_cm_gl23_structure.py','joint'])
    for name in ('pc','gentle','pentagon'):
        for mode in ('single','joint'):
            run(f'a_cm_gl23_{mode}_{name}',[sys.executable,'a_cm_gl23_'+name+'.py',mode])
    for name in ('generation','single_generation','projections'):
        run('a_cm_gl23_'+name,[sys.executable,'a_cm_gl23_'+name+'.py'])
    complete=[]
    for cert in sorted(code.rglob('a_cm_gl23*.bin')):
        # Files inside the certificate directories do not carry the prefix.
        complete.append(cert)
    for folder in ('a_cm_gl23_single_pc_certificates','a_cm_gl23_joint_pc_certificates',
                   'a_cm_gl23_generation_certificates','a_cm_gl23_single_generation_certificates'):
        complete += sorted((code/folder).glob('*.bin'))
    assert len(complete)==len(set(complete))
    generation=[p for p in complete if 'generation_certificates' in str(p.parent)]
    assert len(generation)==960
    replays=[]
    for i,cert in enumerate(complete):
        proc=subprocess.run([str(code/'de_a6_schreier_fast'),'--replay',str(cert)],
                            capture_output=True,text=True,check=True)
        cert.with_suffix('.replay.out').write_text(proc.stdout)
        cert.with_suffix('.replay.err').write_text(proc.stderr)
        result=json.loads(next(s for s in reversed(proc.stdout.splitlines()) if s.startswith('{')))
        assert result['status']=='PASS'
        replays.append({'certificate':str(cert.relative_to(code)),'order':result['order'],
                        'complete_final_Schreier_relations':result['complete_final_Schreier_relations']})
        if i%128==0:print('Full certificate replay',i+1,'of',len(complete),flush=True)
    compared=[]
    for name in m['semantic_json_outputs']:
        assert stable(json.loads((ROOT/name).read_text()))==stable(json.loads((dest/name).read_text())),('JSON',name)
        compared.append(name)
    for name in m['semantic_npz_outputs']:
        old=np.load(ROOT/name);new=np.load(dest/name)
        assert set(old.files)==set(new.files),('NPZ keys',name)
        for key in old.files:assert np.array_equal(old[key],new[key]),('NPZ',name,key)
        compared.append(name)
    for name in m['semantic_chain_outputs']:
        assert stable(final_json(ROOT/name))==stable(final_json(dest/name)),('chain',name)
        compared.append(name)
    for name,row in m['files'].items():assert digest(ROOT/name)==row['sha256'],('original changed',name)
    result={'status':'PASS_ISOLATED_COMPLETE_E62_REPLAY','manifest_sha256':digest(MANIFEST),
        'all_mathematical_outputs_identical':True,'protected_original_files_unchanged':True,
        'compared_outputs':compared,'complete_certificates_replayed':replays,
        'complete_generation_certificate_count':len(generation),'seconds':round(time.time()-start,3)}
    (dest/'result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('compared_outputs','complete_certificates_replayed')},indent=2),flush=True)

if __name__=='__main__':main()
