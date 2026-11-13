#!/usr/bin/env python3
"""Exact small/lower-A6 controls for the independent C++ certificate engine."""
from pathlib import Path
import json,subprocess,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup

HERE=Path(__file__).resolve().parent

def run(tag,generators,order,derived=False):
    p=HERE/('de_a6_schreier_control_'+tag)
    a=np.array([g.array_form if isinstance(g,Permutation) else g for g in generators],dtype=np.int64)
    p.with_suffix('.input').write_text(f'{a.shape[1]} {len(a)}\n'+'\n'.join(' '.join(map(str,g)) for g in a)+'\n')
    cmd=[str(HERE/'de_a6_schreier_fast')]+(['--derived'] if derived else [])+[str(p.with_suffix('.input')),str(p.with_suffix('.bin'))]
    result=subprocess.run(cmd,text=True,capture_output=True,check=True)
    p.with_suffix('.out').write_text(result.stdout+result.stderr)
    record=json.loads(result.stdout.splitlines()[-1]);assert int(record['order'])==order
    replay=subprocess.run([str(HERE/'de_a6_schreier_fast'),'--replay',str(p.with_suffix('.bin'))],text=True,capture_output=True,check=True)
    Path(str(p)+'_replay.out').write_text(replay.stdout+replay.stderr)
    second=json.loads(replay.stdout.splitlines()[-1]);assert int(second['order'])==order
    assert record['complete_final_Schreier_relations']==second['complete_final_Schreier_relations']
    return {'tag':tag,'order':order,'derived':derived,'relations':record['complete_final_Schreier_relations'],
            'seconds':record['seconds'],'replay_seconds':second['seconds']}

def main():
    start=time.time();rows=[]
    s4=[Permutation([1,2,3,0]),Permutation([1,0,2,3])]
    rows.append(run('S4',s4,24));rows.append(run('S4derived',s4,12,True))
    a5=[Permutation([1,2,3,4,0]),Permutation([1,2,0,3,4])]
    rows.append(run('A5derived',a5,60,True))
    abelian=[Permutation([1,0,2,3]),Permutation([0,1,3,2])]
    rows.append(run('abelian_derived',abelian,1,True))
    for kind in ('perm','outer'):
        prefix=HERE/('de_ferrari_a6_'+kind)
        info=json.loads(Path(str(prefix)+'_corrections.json').read_text())
        source=np.load(Path(str(prefix)+'_source_compressed.npz'))
        cert=np.load(Path(str(prefix)+'_corrections.npz'))
        rows.append(run(kind+'_source',[source['s'],source['r']],info['source_order']))
        n=[cert['N_images'][i] for i in info['N_selected_generator_indices']]
        rows.append(run(kind+'_Nderived',n,info['N_derived_image_order'],True))
        rows.append(run(kind+'_Cderived',cert['compact_prime_generators'],info['F_prime_K6_image_order'],True))
    out={'status':'PASS','all_controls':rows,'seconds':round(time.time()-start,3)}
    (HERE/'de_a6_schreier_control.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2),flush=True)

if __name__=='__main__':main()
