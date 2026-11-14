#!/usr/bin/env python3
"""Reproduce the exact GL23 and joint structural subgroup certificates.

This orchestrates the commands used in the original computation.  The
--check-existing mode independently verifies every retained word map and
input identity without replacing any original output.
"""
from pathlib import Path
import argparse,json,subprocess,time
import numpy as np
from de_a6_schreier_certificate import read_certificate,verify_words

HERE=Path(__file__).resolve().parent

def info(path):
    return json.loads(next(x for x in reversed(path.read_text().splitlines()) if x.startswith('{')))

def write_input(path,gs,check):
    value=f'{len(gs[0])} {len(gs)}\n'+''.join(' '.join(map(str,g))+'\n' for g in gs)
    if check:assert path.read_text()==value
    else:path.write_text(value)

def main():
    pa=argparse.ArgumentParser();pa.add_argument('mode',choices=['single','joint']);pa.add_argument('--check-existing',action='store_true')
    args=pa.parse_args();start=time.time();checks=[]
    def run(stem,input_stem=None,mode=None):
        inp=HERE/((input_stem or stem)+'.input');p=HERE/stem
        if not args.check_existing:
            cmd=[str(HERE/'de_a6_schreier_fast')]
            if mode:cmd.append(mode)
            cmd += [str(inp),str(p.with_suffix('.bin'))]
            with p.with_suffix('.out').open('w') as out,p.with_suffix('.err').open('w') as err:
                subprocess.run(cmd,stdout=out,stderr=err,check=True)
        d=read_certificate(p.with_suffix('.bin'));verify_words(d)
        with inp.open() as f:
            n,m=map(int,f.readline().split());gs=np.array([list(map(int,f.readline().split())) for _ in range(m)],dtype=np.uint16)
        assert n==d['degree'] and np.array_equal(gs,d['original'])
        it=info(p.with_suffix('.out'));checks.append({'stem':stem,'order':it['order'],
            'complete_final_Schreier_relations':it['complete_final_Schreier_relations'],
            'all_original_and_strong_words_checked':True})
        return d,it
    if args.mode=='single':
        run('a_cm_gl23_B_source')
        _,greedy=run('a_cm_gl23_N_source',mode='--greedy')
        run('a_cm_gl23_N_derived','a_cm_gl23_N_source',mode='--derived')
        allN=np.load(HERE/'a_cm_gl23_induced.npz')['N_generators']
        small='a_cm_gl23_N_small'
    else:
        run('a_cm_gl23_joint_SL23_N_derived','a_cm_gl23_joint_SL23_N',mode='--derived')
        _,greedy=run('a_cm_gl23_joint_SL23_N_greedy','a_cm_gl23_joint_SL23_N',mode='--greedy')
        allN=np.load(HERE/'a_cm_gl23_joint.npz')['joint_N_generators']
        small='a_cm_gl23_joint_N_small'
    inds=greedy['selected_original_indices'];gs=allN[inds]
    write_input(HERE/(small+'.input'),gs,args.check_existing)
    mp={'actual_original_N_indices':inds,'map':'each retained generator is the literal indicated N_B basis word'}
    path=HERE/(small+'_map.json')
    if args.check_existing:assert json.loads(path.read_text())==mp
    else:path.write_text(json.dumps(mp,indent=2)+'\n')
    d,it=run(small+'_derived',small,mode='--derived')
    if args.mode=='single':
        write_input(HERE/'a_cm_gl23_C.input',d['strong'],args.check_existing)
        values={'actual_permutations':d['strong'],'N_small_word_nodes':d['words'],'N_small_word_DAG':d['nodes']}
        p=HERE/'a_cm_gl23_C_generators.npz'
        if args.check_existing:
            old=np.load(p);assert set(old.files)==set(values)
            for key,value in values.items():assert np.array_equal(old[key],value)
        else:np.savez_compressed(p,**values)
        run('a_cm_gl23_C_derived','a_cm_gl23_C',mode='--derived')
    out={'status':'PASS_EXACT_GL23_STRUCTURE_REPLAY','mode':args.mode,
         'existing_artifacts_read_only':args.check_existing,'checks':checks,
         'seconds':round(time.time()-start,3)}
    print(json.dumps(out,indent=2),flush=True)

if __name__=='__main__':main()
