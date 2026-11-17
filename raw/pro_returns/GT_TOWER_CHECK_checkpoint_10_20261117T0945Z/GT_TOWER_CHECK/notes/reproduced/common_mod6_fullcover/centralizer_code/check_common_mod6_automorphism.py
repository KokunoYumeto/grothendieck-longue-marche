#!/usr/bin/env python3
"""Test a literal surviving finite record as an automorphism of the common source.

This stops before the full canonical central-cover lifting problem.
"""
from pathlib import Path
import json
import numpy as np

HERE=Path(__file__).resolve().parent
src=(HERE/'census_common_mod6_frames.py').read_text()
env={'__name__':'common_mod6_automorphism_prefix','__file__':str(HERE/'common_mod6_automorphism_prefix.py')}
exec(compile(src.split('records=[];summaries=[]',1)[0],str(HERE/'census_common_mod6_frames.py'),'exec'),env)
archive=np.load(HERE/'census_common_mod6_frames.npz')
data=env['data'];ns=env['ns'];jt=env['jt'];jp=env['jp'];jl=env['jl']
chain=env['chain'];inverse=env['inverse'];jinv=env['jinv'];jgen=env['jgen']
rankproj=env['proj']
base=0;candidate=1
results=[];save={}

for p in (2,3):
    P=data[p]['P'];L=data[p]['L']
    vf=archive[f'b{base}_p{p}_particular'][:,candidate].astype(np.int64)
    beta=archive[f'b{base}_p{p}_beta_{candidate}'].astype(np.int64)
    cubic=archive[f'b{base}_p{p}_A_{candidate}'].astype(np.int64)
    beta_base,A_base=map(int,archive[f'b{base}_p{p}_base_frames'][candidate])
    action={}
    generators=[]
    for w in [(1,),(2,)]:
        raw=np.array([chain(w+z+inverse(w))[1] for z in jl],dtype=np.int64)
        generators.append(L@raw@P%p)
    action[0]=np.eye(97,dtype=np.int64)
    for a in sorted(jp,key=lambda a:len(jp[a])):
        if a==0:continue
        w=jp[a];parent=chain(w[:-1])[0]
        action[a]=generators[w[-1]-1]@action[parent]%p
    for a in range(288):
        for k,g in enumerate(jgen):
            dest=int(jt[a,g])
            assert np.array_equal(action[dest],generators[k]@action[a]%p)
    cc={}
    def cocycle(a,b):
        key=(a,b)
        if key not in cc:
            end,v=chain(jp[a]+jp[b]);assert end==jt[a,b]
            cc[key]=v@P%p
        return cc[key]
    def mul(u,v):
        a,x=u;b,y=v
        return int(jt[a,b]),(x+y@action[a]+cocycle(a,b))%p
    def inv(u):
        a,x=u;b=jinv[a]
        return b,(-x-cocycle(a,b))@action[b]%p
    one=(0,np.zeros(97,dtype=np.int64))
    x=(int(jgen[0]),np.zeros(97,dtype=np.int64))
    y=(int(jgen[1]),np.zeros(97,dtype=np.int64))
    f=(base,vf)
    images=[x,mul(mul(inv(f),y),f)]
    inverses=[inv(v) for v in images]
    def ev(w,gs=images,gsi=inverses):
        z=one
        for j in w:z=mul(z,gs[j-1] if j>0 else gsi[-j-1])
        return z
    base_map=[ev(jp[a])[0] for a in range(288)]
    assert len(set(base_map))==288
    for a in range(288):
        for k,g in enumerate(jgen):
            assert base_map[int(jt[a,g])]==jt[base_map[a],images[k][0]]
    raw=[]
    for w in jl:
        a,c=ev(w);assert a==0;raw.append(c)
    raw=np.array(raw,dtype=np.int64)
    induced=L@raw%p
    assert np.array_equal(P@induced%p,raw)
    rank=len(rankproj(induced,p)[0])
    assert rank==97

    # Check the two positive frames in the same exact source product law.
    def source_aut(value,which):
        a,c=value
        imgs=env['SX'] if which=='S' else env['RX']
        end,v=chain(env['subst'](jp[a],imgs))
        return end,(c@(data[p]['L']@data[p][which]@P%p)+v@P)%p
    bv=(beta_base,beta);av=(A_base,cubic)
    sb=source_aut(bv,'S');fb=mul(f,bv)
    ra=source_aut(av,'R');fa=mul(f,av)
    assert sb[0]==fb[0] and np.array_equal(sb[1],fb[1])
    assert ra[0]==fa[0] and np.array_equal(ra[1],fa[1])
    results.append({'prime':p,'module_rank':rank,'base_permutation_order':len(set(base_map)),
                    'beta_base':beta_base,'A_base':A_base,
                    'f_is_identity':base==0 and not np.any(vf),
                    'positive_frames_verified':True})
    save[f'f_{p}']=vf;save[f'beta_{p}']=beta;save[f'A_{p}']=cubic
    save[f'aut_{p}']=induced;save[f'base_map_{p}']=base_map
    print('PASS prime',p,'literal full-source frames and induced module automorphism rank97',flush=True)

out={'scope':'An actual finite positive tau-fixed automorphism of E6; a full canonical-cover lift remains to be proved.',
     'source':'B/((Kprime K^6) intersection Fprime F^36)',
     'base':base,'candidate':candidate,'rho_mod3':0,'T_sign':1,'T_R_power':0,'W_power':1,
     'formal_CM_parity':1,'prime_checks':results,'all_assertions_passed':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
np.savez_compressed(Path(__file__).with_suffix('.npz'),**save)
print('PASS actual finite positive automorphism with parity-one frame record; no full profinite lift is asserted.',flush=True)
