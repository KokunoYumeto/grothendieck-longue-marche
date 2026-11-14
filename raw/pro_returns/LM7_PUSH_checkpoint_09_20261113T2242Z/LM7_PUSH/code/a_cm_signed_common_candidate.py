#!/usr/bin/env python3
"""Actual six-coset SL2(F5) epikernel-4 source with ordinary Fab/30.

This constructs a candidate finite common quotient with its literal
projection to the old Q30. No factorization through either large source
is asserted here.
"""
from pathlib import Path
from collections import deque
from hashlib import sha256
import json,time,subprocess
import numpy as np
from de_ferrari_sl2_5_model import FerrariSL2Five
from de_ferrari_a6_source_data import load_data
from de_a6_schreier_certificate import read_certificate,verify_words

HERE=Path(__file__).resolve().parent


def certify(stem,gens,derived=False):
    p=HERE/stem
    with p.with_suffix('.input').open('w') as f:
        f.write(f'{len(gens[0])} {len(gens)}\n')
        for g in gens:f.write(' '.join(map(str,g))+'\n')
    cmd=[str(HERE/'de_a6_schreier_fast')]
    if derived:cmd.append('--derived')
    cmd += [str(p.with_suffix('.input')),str(p.with_suffix('.bin'))]
    with p.with_suffix('.out').open('w') as out,p.with_suffix('.err').open('w') as err:
        subprocess.run(cmd,stdout=out,stderr=err,check=True)
    info=json.loads(next(s for s in reversed(p.with_suffix('.out').read_text().splitlines()) if s.startswith('{')))
    d=read_certificate(p.with_suffix('.bin'));verify_words(d)
    assert np.array_equal(d['original'],gens)
    with Path(str(p)+'_replay.out').open('w') as out,Path(str(p)+'_replay.err').open('w') as err:
        subprocess.run([str(HERE/'de_a6_schreier_fast'),'--replay',str(p.with_suffix('.bin'))],stdout=out,stderr=err,check=True)
    return info,d


def main():
    start=time.monotonic();H=FerrariSL2Five();data=load_data()
    pair=H.lifts[4];Q=data['Q2'];ix={q:i for i,q in enumerate(Q)}
    paths={data['unit']:[]};todo=deque(paths)
    while todo:
        q=todo.popleft()
        for a,g in ((0,data['s2']),(1,data['r2'])):
            qg=data['mul2'](q,g)
            if qg not in paths:paths[qg]=paths[q]+[a];todo.append(qg)
    def slword(w):
        a=H.sid
        for c in w:
            z=int(pair[abs(c)-1]);a=int(H.sm[a,z if c>0 else H.si[z]])
        return a
    allps=[];transitions=[]
    for a,g in ((0,data['s2']),(1,data['r2'])):
        sp=np.empty(720,dtype=np.uint16);ap=np.empty(180,dtype=np.uint16);tr=[]
        for q in Q:
            qg=data['mul2'](q,g)
            w=data['fword'](paths[q]+[a]+data['binv'](paths[qg]))
            z=slword(w);e=sum((c==1)-(c==-1) for c in w)
            sp[120*ix[q]:120*(ix[q]+1)]=120*ix[qg]+H.sm[:,z]
            ap[30*ix[q]:30*(ix[q]+1)]=30*ix[qg]+(np.arange(30)+e)%30
            tr.append({'F_word':list(w),'SL2_value':z,'x_exponent':e})
        allps.append(np.r_[sp,720+ap]);transitions.append(tr)
    one=np.arange(900,dtype=np.uint16);s,r=allps
    assert np.array_equal(s[s],one) and np.array_equal(r[r[r]],one)
    def bw(w):
        a=one.copy();letters={0:s,1:r,-1:np.argsort(r)}
        for c in w:a=letters[c][a]
        return a
    x,y=bw(data['xword']),bw(data['yword'])
    old=np.load(HERE/'de_a6_gl_common_quotient.npz')
    # Right translation z -> z*g descends to the inverse natural action
    # v -> q(g)^-1(v), exactly the old epikernel convention.
    sl_to_five=np.array([H.old.permutations[int(H.old.si[H.qsl[z]])][0]
                        for z in range(120)],dtype=np.uint16)
    pointmap=np.r_[np.concatenate([5*j+sl_to_five for j in range(6)]),30+np.arange(180)]
    for p,label in zip(allps,('s','r')):
        assert np.array_equal(pointmap[p],old['m30_'+label][pointmap])
    info={}
    info['B'],bcert=certify('a_cm_signed_common_B',np.array(allps))
    info['F'],fcert=certify('a_cm_signed_common_F',np.array([x,y]))
    info['Fprime'],ecert=certify('a_cm_signed_common_Fprime',np.array([x,y]),True)
    info['Fsecond'],eecert=certify('a_cm_signed_common_Fsecond',ecert['strong'],True)
    assert int(info['Fprime']['order'])==int(info['Fsecond']['order'])
    assert all(np.array_equal(g[720:],np.arange(720,900)) for g in ecert['strong'])
    kernels=list(map(int,old['induced_coset_epikernel_indices']))
    selected=[kernels.index(j) for j in (4,12,18)]
    points=np.concatenate([np.arange(120*j,120*(j+1)) for j in selected])
    inverse=np.full(900,-1,dtype=np.int64);inverse[points]=np.arange(360)
    eg=inverse[ecert['strong'][:,points]];assert np.all(eg>=0)
    info['Fprime_three_SL_factors'],pcer=certify('a_cm_signed_common_three_factors',eg)
    assert int(info['Fprime_three_SL_factors']['order'])==int(info['Fprime']['order'])==120**3
    assert int(info['F']['order'])==120**3*30**2
    assert int(info['B']['order'])==6*120**3*30**2
    oldorder=int(json.loads((HERE/'de_a6_gl_common_quotient.json').read_text())['quotients'][1]['actual_B_image_order'])
    assert int(info['B']['order'])==8*oldorder
    # Identify the F map by three literal SL coordinates and ordinary
    # exponent sums; equal actual orders prove this map injective too.
    purepoints=np.r_[points,np.arange(720,900)]
    inverse2=np.full(900,-1,dtype=np.int64);inverse2[purepoints]=np.arange(len(purepoints))
    fg=inverse2[np.array([x,y])[:,purepoints]];assert np.all(fg>=0)
    info['F_three_SL_and_abelian'],fpc=certify('a_cm_signed_common_F_typed_product',fg)
    assert int(info['F_three_SL_and_abelian']['order'])==int(info['F']['order'])
    out={'status':'PASS_LITERAL_SIGNED_COMMON_QUOTIENT_CANDIDATE',
         'literal_SL2_epikernel_index':4,'literal_SL2_generating_pair':pair.tolist(),
         'six_induced_A5_epikernel_indices':kernels,'selected_cosets_for_three_SL_factors':selected,
         'actual_B_over_F_section':[paths[q] for q in Q],
         'actual_B_transition_words_and_SL_values':transitions,
         'groups':info,'actual_F_map':'three displayed SL2(F5) projections times ordinary Fab/30',
         'actual_F_image':'SL2(F5)^3 times (Z/30)^2',
         'all_six_induced_global_binary_signs_retained':True,
         'projection_to_existing_Q30':'the saved literal equivariant point map',
         'projection_kernel_order':8,
         'projection_kernel_in_pure_source_is_central':True,
         'factorization_through_either_large_source_asserted':False,
         'input_sha256':{n:sha256((HERE/n).read_bytes()).hexdigest() for n in (
             'de_ferrari_sl2_5_model.py','de_ferrari_a5_model.py','de_ferrari_a6_source_data.py',
             'de_ferrari_sl2_5_N.json','de_a6_gl_common_quotient.npz','de_a6_gl_common_quotient.json',
             'de_a6_schreier.cpp')},'seconds':round(time.monotonic()-start,6)}
    np.savez_compressed(HERE/'a_cm_signed_common_candidate.npz',s=s,r=r,x=x,y=y,
                        actual_Q30_point_map=pointmap,three_SL_points=points,
                        typed_F_product_points=purepoints,
                        Fprime_generators=ecert['strong'])
    (HERE/'a_cm_signed_common_candidate.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
