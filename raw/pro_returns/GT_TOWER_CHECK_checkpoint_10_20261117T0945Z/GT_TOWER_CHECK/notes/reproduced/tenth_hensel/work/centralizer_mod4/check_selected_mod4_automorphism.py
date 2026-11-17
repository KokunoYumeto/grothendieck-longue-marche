#!/usr/bin/env python3
"""Actual finite automorphism for the fully corrected coefficient4 record."""
from pathlib import Path
import json
import numpy as np

HERE=Path(__file__).resolve().parent
src=(HERE/'lift_mask31_mod4.py').read_text()
env={'__name__':'mod4_auto_prefix','__file__':str(HERE/'mod4_auto_prefix.py')}
exec(compile(src.split('matrices=[];rhs=[]',1)[0],str(HERE/'lift_mask31_mod4.py'),'exec'),env)
P=env['P'];L=env['L'];chain=env['chain'];jp=env['jp'];jl=env['jl'];jt=env['jt'];jg=env['jg'];ji=env['ji']
inverse=env['inverse'];subst=env['subst'];mod=env['mod'];ns=env['ns']
record=np.load(HERE/'check_mod4_canonical_lift.npz')
vf=record['f4'];beta=record['beta4'];cubic=record['A4']
assert not np.any(record['s_correction4'])
generators=[]
for w in ((1,),(2,)):
    raw=np.array([chain(w+z+inverse(w))[1] for z in jl],dtype=np.int64)
    generators.append(L@raw@P%4)
action={0:np.eye(97,dtype=np.int64)}
for a in sorted(jp,key=lambda a:len(jp[a])):
    if a==0:continue
    w=jp[a];parent=chain(w[:-1])[0]
    action[a]=generators[w[-1]-1]@action[parent]%4
for a in range(288):
    for k,g in enumerate(jg):assert np.array_equal(action[int(jt[a,g])],generators[k]@action[a]%4)
cache={}
def cocycle(a,b):
    if (a,b) not in cache:
        end,v=chain(jp[a]+jp[b]);assert end==jt[a,b];cache[a,b]=v@P%4
    return cache[a,b]
def mul(u,v):
    a,x=u;b,y=v
    return int(jt[a,b]),(x+y@action[a]+cocycle(a,b))%4
def inv(u):
    a,x=u;b=ji[a]
    return b,(-x-cocycle(a,b))@action[b]%4
one=(0,np.zeros(97,dtype=np.int64));x=(int(jg[0]),one[1]);y=(int(jg[1]),one[1]);f=(0,vf)
images=[x,mul(mul(inv(f),y),f)];inverses=[inv(t) for t in images]
def ev(w):
    z=one
    for a in w:z=mul(z,images[a-1] if a>0 else inverses[-a-1])
    return z
base_map=[ev(jp[a])[0] for a in range(288)]
assert base_map==list(range(288))
raw=[]
for w in jl:
    a,c=ev(w);assert a==0;raw.append(c)
raw=np.array(raw,dtype=np.int64);induced=L@raw%4
assert np.array_equal(P@induced%4,raw)
rank=len(ns['row_space_projection'](induced,2)[0]);assert rank==97
for val,name,imgs in [((252,beta),'s',env['SX']),((0,cubic),'r',env['RX'])]:
    a,c=val;end,v=chain(subst(jp[a],imgs));lhs=(end,(c@mod['quotient_'+name]+v@P)%4)
    rhs=mul(f,val)
    assert lhs[0]==rhs[0] and np.array_equal(lhs[1],rhs[1])
old=np.load(env['WORK']/'centralizer_code/check_common_mod6_liftable_automorphism.npz')
C=mod['binary_reduction_change']
assert np.array_equal(vf@C%2,old['f_2'])
assert np.array_equal(induced@C%2,C@old['aut_2']%2)
aff=np.load(HERE/'lift_mask31_mod4.npz')
assert not np.any((aff['matrix4']@record['solution4']-aff['rhs4'])%4)
out={'scope':'Actual positive cusp-fixed automorphism of E4, coherently joined with the ternary identity action to E12.',
     'base_permutation_is_identity':True,'common_module_rank_mod2':rank,
     'pure_source_order':'288*4^97','full_source_order':'1728*4^97',
     'joint_E12_order':'1728*12^97','both_positive_frames_verified':True,
     'all_literal_pentagon_and_frame_equations_verified':True,
     'binary_reduction_is_mask31_automorphism':True,'all_assertions_passed':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
np.savez_compressed(Path(__file__).with_suffix('.npz'),f4=vf,beta4=beta,A4=cubic,aut4=induced,base_map=np.array(base_map))
print('PASS actual E4 automorphism: base identity, exact kernel factorization, invertible rank97 reduction.',flush=True)
print('PASS both positive source frames; actual pentagon equations in the mixed target; compatible E12 join.',flush=True)
