#!/usr/bin/env python3
"""Isolated, hash-protected replay of the complete E.59 finite batch.

No authoritative file is written.  The destination must not exist.  All
mathematical JSON data and NPZ arrays are compared exactly; only elapsed
times and the independently recompiled executable's hash are disregarded.
"""
from pathlib import Path
import argparse,hashlib,json,shutil,subprocess,sys,time
import numpy as np

ROOT=Path(__file__).resolve().parent.parent
MANIFEST=ROOT/'research/E59_authoritative_manifest.json'

def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def stable(x):
    if isinstance(x,dict):
        return {k:stable(v) for k,v in x.items()
                if not k.endswith('seconds') and k!='Schreier_executable_sha256'}
    if isinstance(x,list):return [stable(v) for v in x]
    return x
def final_json(p):
    return json.loads(next(line for line in reversed(p.read_text().splitlines()) if line.startswith('{')))

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--destination',type=Path)
    parser.add_argument('--check-only',action='store_true')
    args=parser.parse_args();manifest=json.loads(MANIFEST.read_text());started=time.time()
    for name,row in manifest['files'].items():
        assert digest(ROOT/name)==row['sha256'],('protected hash mismatch',name)
    if args.check_only:
        print(json.dumps({'status':'PASS_E59_MANIFEST','protected_files':len(manifest['files']),
                          'input_files':len(manifest['input_files'])},indent=2));return
    if args.destination is None:parser.error('--destination is required unless --check-only')
    dest=args.destination.resolve()
    if dest.exists():raise SystemExit('Destination already exists; use a fresh isolated directory.')
    code=dest/'code';code.mkdir(parents=True)
    for name in manifest['input_files']:
        target=dest/name;target.parent.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(ROOT/name,target)
    commands=[]
    def run(name,argv,cwd=code):
        before=time.time();out=code/(name+'.out');err=code/(name+'.err')
        with out.open('w') as fo,err.open('w') as fe:
            p=subprocess.run(argv,cwd=cwd,stdout=fo,stderr=fe)
        commands.append({'name':name,'argv':list(map(str,argv)),'exit_code':p.returncode,
                         'seconds':round(time.time()-before,3)})
        (dest/'commands.json').write_text(json.dumps(commands,indent=2)+'\n')
        if p.returncode:raise RuntimeError(f'{name} failed; see {err}')
        print(name,'PASS',commands[-1]['seconds'],'s',flush=True)
    run('compile_schreier',['g++','-std=c++17','-O3','de_a6_schreier.cpp','-o','de_a6_schreier_fast'])
    for name in ('model','source','induced'):
        run('a_cm_sl23_'+name,[sys.executable,'a_cm_sl23_'+name+'.py'])
    for group,mode in (('B',[]),('N',['--greedy'])):
        stem='a_cm_sl23_'+group+'_source'
        run(stem+'_chain',['./de_a6_schreier_fast',*mode,stem+'.input',stem+'.bin'])
        run(stem+'_replay',['./de_a6_schreier_fast','--replay',stem+'.bin'])
        run(stem+'_word_replay',[sys.executable,'de_a6_schreier_certificate.py',stem+'.bin','--output-prefix',stem])
    run('a_cm_sl23_N_derived_chain',['./de_a6_schreier_fast','--derived',
        'a_cm_sl23_N_source.input','a_cm_sl23_N_derived.bin'])
    run('a_cm_sl23_N_derived_replay',['./de_a6_schreier_fast','--replay','a_cm_sl23_N_derived.bin'])
    run('a_cm_sl23_N_derived_word_replay',[sys.executable,'de_a6_schreier_certificate.py',
        'a_cm_sl23_N_derived.bin','--output-prefix','a_cm_sl23_N_derived'])
    for name in ('corrections','generation','periodic','cm_labels'):
        run('a_cm_sl23_'+name,[sys.executable,'a_cm_sl23_'+name+'.py'])
    replays=[]
    for cert in sorted((code/'a_cm_sl23_generation_certificates').glob('*.bin')):
        proc=subprocess.run([str(code/'de_a6_schreier_fast'),'--replay',str(cert)],
                            capture_output=True,text=True,check=True)
        cert.with_suffix('.replay.out').write_text(proc.stdout)
        cert.with_suffix('.replay.err').write_text(proc.stderr)
        result=json.loads(next(s for s in reversed(proc.stdout.splitlines()) if s.startswith('{')))
        assert result['status']=='PASS'
        replays.append({'certificate':cert.name,'order':result['order'],
                        'complete_final_Schreier_relations':result['complete_final_Schreier_relations']})
    assert len(replays)==144
    compared=[]
    for name in manifest['semantic_json_outputs']:
        original=json.loads((ROOT/name).read_text());new=json.loads((dest/name).read_text())
        assert stable(original)==stable(new),('JSON mismatch',name)
        compared.append(name)
    for name in manifest['semantic_npz_outputs']:
        old=np.load(ROOT/name);new=np.load(dest/name)
        assert set(old.files)==set(new.files),('NPZ key mismatch',name)
        for key in old.files:assert np.array_equal(old[key],new[key]),('NPZ array mismatch',name,key)
        compared.append(name)
    for stem in ('a_cm_sl23_B_source','a_cm_sl23_N_source','a_cm_sl23_N_derived'):
        name='code/'+stem+'_chain.out'
        assert stable(final_json(ROOT/name))==stable(final_json(dest/name)),('chain mismatch',name)
        compared.append(name)
    for name,row in manifest['files'].items():
        assert digest(ROOT/name)==row['sha256'],('authoritative file changed during replay',name)
    result={'status':'PASS_ISOLATED_COMPLETE_E59_REPLAY','manifest_sha256':digest(MANIFEST),
            'all_mathematical_outputs_identical':True,'protected_original_files_unchanged':True,
            'compared_outputs':compared,'complete_generation_certificates_replayed':replays,
            'seconds':round(time.time()-started,3)}
    (dest/'result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in
        ('compared_outputs','complete_generation_certificates_replayed')},indent=2),flush=True)

if __name__=='__main__':main()
