#!/usr/bin/env python3
"""Generation and actual F-prime preimages for the complete joint fibres.

Each source point and each final four-strand target point gets a complete
Schreier certificate.  Its strong words are independently evaluated by the
NumPy certificate reader.  The preimages are finite word DAGs in the exact
N_B basis, followed by the saved literal embedding of that basis in F.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import argparse,json,subprocess,time
import numpy as np
from a_cm_gl23_pc import ClassTwoCoordinates,mul,inv,power
from a_cm_gl23_model import FerrariGL23
from a_cm_sl23_model import FerrariSL23
from de_ferrari_a6_source_data import load_data
from de_a6_schreier_certificate import read_certificate,verify_words

HERE=Path(__file__).resolve().parent

def abelian_DAG(nodes,original):
    values=[]
    for i,(op,a,b) in enumerate(nodes):
        op,a,b=map(int,(op,a,b))
        if op==0:assert i==0;v=np.zeros(2,dtype=np.int64)
        elif op==1:v=original[a]
        elif op==2:v=values[a]+values[b]
        elif op==3:v=-values[a]
        elif op==4:v=np.zeros(2,dtype=np.int64)
        elif op==5:v=values[b]
        else:raise AssertionError('word operation')
        values.append(v)
    return values

def main():
    pa=argparse.ArgumentParser();pa.add_argument('--workers',type=int,default=2);args=pa.parse_args()
    start=time.time();P=ClassTwoCoordinates('joint');d=load_data()
    folder=HERE/'a_cm_gl23_generation_certificates';folder.mkdir(exist_ok=False)
    pc=np.load(P.prefix.with_suffix('.npz'))
    ni=json.loads((HERE/'a_cm_gl23_joint_N_small_map.json').read_text())['actual_original_N_indices']
    nwords=[list(d['fword'](d['Nwords'][j])) for j in ni]
    def ab(w):return np.array([sum((a==j)-(a==-j) for a in w) for j in (1,2)])
    cv=abelian_DAG(pc['C_strong_Nsmall_word_DAG'],np.array([ab(w) for w in nwords]))
    cs=np.array([cv[int(j)] for j in pc['C_strong_Nsmall_word_nodes']]);assert not np.any(cs)
    zv=abelian_DAG(pc['Cprime_strong_C_word_DAG'],cs)
    zs=np.array([zv[int(j)] for j in pc['Cprime_strong_C_word_nodes']]);assert not np.any(zs)
    preimage={'status':'PASS_ACTUAL_F_PRIME_WORD_DAG_PREIMAGES',
        'original_N_basis_indices':ni,'literal_N_basis_F_words':nwords,
        'C_word_DAG':pc['C_strong_Nsmall_word_DAG'].tolist(),
        'C_strong_word_nodes':pc['C_strong_Nsmall_word_nodes'].tolist(),
        'quotient_basis_C_strong_indices':pc['quotient_basis_C_strong_indices'].tolist(),
        'Cprime_word_DAG_in_C_strong':pc['Cprime_strong_C_word_DAG'].tolist(),
        'Cprime_strong_word_nodes':pc['Cprime_strong_C_word_nodes'].tolist(),
        'derived_basis_Cprime_strong_indices':pc['derived_basis_Cprime_strong_indices'].tolist(),
        'operation_codes':{'0':'identity','1':'original generator a','2':'a b','3':'a inverse',
                           '4':'a b a inverse b inverse','5':'a b a inverse'},
        'PC_word_rule':'ascending quotient basis indices, then ascending derived basis indices',
        'all_PC_basis_words_have_integral_F_abelianization_zero':True}
    (HERE/'a_cm_gl23_preimages.json').write_text(json.dumps(preimage,indent=2)+'\n')
    inp=np.load(HERE/'a_cm_gl23_joint.npz');s,r=inp['joint_B_generators'].astype(np.uint16)
    one=np.arange(len(s),dtype=np.uint16);bletters={0:s,1:r,-1:mul(r,r)}
    def beval(w):
        a=one.copy()
        for j in w:a=mul(a,bletters[j])
        return a
    x=beval(d['xword']);y=beval(d['yword']);letters={1:x,2:y,-1:inv(x),-2:inv(y)}
    def feval(w):
        a=one.copy()
        for j in w:a=mul(a,letters[j])
        return a
    models={'gl23':FerrariGL23(),'sl23':FerrariSL23()}
    gentle=json.loads((HERE/'a_cm_gl23_joint_gentle.json').read_text())['records']
    pent=json.loads((HERE/'a_cm_gl23_joint_pentagon.json').read_text())['records']
    pv=np.load(HERE/'a_cm_gl23_joint_pentagon.npz')
    base=json.loads((HERE/'de_ferrari_fibres.json').read_text())['records']
    common=json.loads((HERE/'a_cm_gl23_joint.json').read_text())['exact_groups']
    expected_source=int(common['joint_SL23_B']['order'])
    expected_target=int(common['joint_SL23_target']['order'])
    jobs=[]
    for row,pr,rec in zip(gentle,pent,base):
        i=row['index'];assert not np.any(ab(rec['actual_commutator_word_f']))
        f0=feval(rec['actual_commutator_word_f'])
        for j,c in enumerate(row['all_gentle_coordinates']):
            f=mul(f0,P.element(c));S=mul(s,f);R=mul(inv(f),r)
            assert np.array_equal(power(S,2),one) and np.array_equal(power(R,3),one)
            jobs.append((f'source_{i:02d}_{j:02d}',i,c,[S,R],expected_source))
        good=set(pr['all_surviving_correction_coordinates'])
        for j,c in enumerate(row['all_gentle_coordinates']):
            if c not in good:continue
            blocks=[]
            for label,H in models.items():
                vals=pv[f'point_{i:02d}_{label}_all_gentle_values'][j]
                images=H.braid_images(vals)
                H.check_braids(images)
                blocks.append([np.array(H.permutation(g).array_form,dtype=np.uint16) for g in images])
            off=len(blocks[0][0]);gs=[np.r_[a,off+b] for a,b in zip(*blocks)]
            jobs.append((f'target_{i:02d}_{j:02d}',i,c,gs,expected_target))
    def run(job):
        name,i,c,gs,expected=job;prefix=folder/name;n=len(gs[0])
        with prefix.with_suffix('.input').open('w') as f:
            f.write(f'{n} {len(gs)}\n')
            for g in gs:f.write(' '.join(map(str,g))+'\n')
        with prefix.with_suffix('.out').open('w') as out,prefix.with_suffix('.err').open('w') as err:
            subprocess.run([str(HERE/'de_a6_schreier_fast'),str(prefix.with_suffix('.input')),
                            str(prefix.with_suffix('.bin'))],stdout=out,stderr=err,check=True)
        info=json.loads(next(x for x in reversed(prefix.with_suffix('.out').read_text().splitlines()) if x.startswith('{')))
        cert=read_certificate(prefix.with_suffix('.bin'));verify_words(cert)
        assert np.array_equal(cert['original'],np.array(gs))
        return {'name':name,'G6_index':i,'actual_correction_coordinate':c,
                'order':int(info['order']),'expected_full_order':expected,
                'generates_whole_actual_group':int(info['order'])==expected,
                'all_strong_generator_words_independently_replayed':True,
                'complete_final_Schreier_relations':info['complete_final_Schreier_relations']}
    results=[]
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        for j,answer in enumerate(pool.map(run,jobs)):
            results.append(answer)
            if j%32==0:print('Exact source/target generation certificates',j+1,'of',len(jobs),flush=True)
    rows=[]
    for i in range(24):
        source=[r for r in results if r['G6_index']==i and r['name'].startswith('source')]
        target=[r for r in results if r['G6_index']==i and r['name'].startswith('target')]
        rows.append({'G6_index':i,'all_gentle_source_count':len(source),
            'generating_source_count':sum(r['generates_whole_actual_group'] for r in source),
            'all_final_target_count':len(target),
            'generating_target_count':sum(r['generates_whole_actual_group'] for r in target)})
    out={'status':'PASS_COMPLETE_JOINT_GL23_GENERATION_CHECK','whole_source_order':expected_source,
        'whole_target_order':expected_target,'all_exact_certificates':results,
        'records':rows,'all_source_points_generate':all(r['generates_whole_actual_group'] for r in results if r['name'].startswith('source')),
        'all_final_target_points_generate':all(r['generates_whole_actual_group'] for r in results if r['name'].startswith('target')),
        'actual_F_prime_preimages':'a_cm_gl23_preimages.json','seconds':round(time.time()-start,3)}
    (HERE/'a_cm_gl23_generation.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='all_exact_certificates'},indent=2),flush=True)

if __name__=='__main__':main()
