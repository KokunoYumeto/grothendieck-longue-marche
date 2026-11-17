"""Exact actual-prefix and final six-cone reflection comparison; no group search."""
from pathlib import Path
import json,hashlib,datetime
BASE=Path(__file__).resolve().parent

def red(w, invs=()):
    ans=[]
    for x in w:
        x=abs(x) if abs(x) in invs else x
        if ans and (ans[-1]==-x or x in invs and ans[-1]==x): ans.pop()
        else: ans.append(x)
    return tuple(ans)
def inv(w,invs=()): return red((-x for x in reversed(w)),invs)
def mul(*ws,invs=()): return red((x for w in ws for x in w),invs)
def sub(w,m,invs=()): return red((y for x in w for y in (m[abs(x)] if x>0 else inv(m[-x],invs))),invs)
# Actual K basis a,B,d,e,f from the unchanged common marking.
O=[(1,2,-1),(1,),(5,3,4,-3,-5),(3,),(-3,5,3)]
P=[];p=()
for o in O:
    p=mul(p,o);P.append(p)
assert P[-1]==(1,2,5,3,4)
zeta={1:(),2:(),3:(),4:(),5:(5,)}
images=[sub(p,zeta) for p in P]
assert images==[(),(),(),(),(5,)]
# All six r_i are literal involutions, encoded as 1,...,6.
cones=set(range(1,7)); pref={i:(1,i+1) for i in range(1,6)}
# Inverse actual prefix-to-K dictionary, expressed in P_1,...,P_5.
K_in_P={1:(-1,2),2:(-2,1,2),3:(-3,4),
        5:(-3,5,-4,3),4:(-5,3,-2,5)}
for i in range(1,6):
    assert sub(K_in_P[i],{j:P[j-1] for j in range(1,6)})==(i,)
K_Q={i:sub(w,pref,cones) for i,w in K_in_P.items()}
d=K_Q[3];f=K_Q[5]
t=mul(d,(5,),inv(d,cones),invs=cones)
assert mul(t,t,invs=cones)==()
assert mul(t,f,t,invs=cones)==inv(f,cones)
assert f==mul(d,(5,6),inv(d,cones),invs=cones)
for p in P:
    w=sub(p,K_Q,cones)
    assert mul((1,),w,(1,),w,invs=cones)==()
assert len(t)%2==1
out={'status':'PASS','time_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'K_basis':['a','B','d','e','f'],'actual_O':O,'actual_prefixes':P,
 'companion_prefix_images':images,'six_involution_ids':'r_i encoded i+1',
 'actual_K_in_prefixes':K_in_P,'actual_K_in_Q':K_Q,
 'explicit_t_in_Q':t,'t_square':[],'t_f_t_equals_f_inverse':True,
 'f_equals_d_r4_r5_d_inverse':True,'all_five_j_inversion_relations':True,
 'mirror_parity_t':1,'scope':'Exact actual-prefix/free-product identities supporting the full presentation proof; no unfilled cone-equivariance or source-centralizer assertion'}
(BASE/'final_neck_retraction25.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS all five actual prefixes and companion images 1,1,1,1,f.')
print('PASS five inverse prefix substitutions and all five mirror inversions.')
print('PASS exact t=d*r4*d^-1: t²=1, t*f*t=f^-1, mirror parity1.')
