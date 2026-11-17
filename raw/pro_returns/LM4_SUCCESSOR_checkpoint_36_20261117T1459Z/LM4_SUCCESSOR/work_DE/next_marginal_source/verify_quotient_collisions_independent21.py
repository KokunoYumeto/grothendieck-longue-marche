#!/usr/bin/env python3
"""Independent rational four-coordinate arithmetic for all quotient nodes."""
from fractions import Fraction as F
from pathlib import Path
import json,time
start=time.monotonic()
zero=(F(0),)*4;one=(F(1),F(0),F(0),F(0));x=(F(0),F(1),F(0),F(0))
def add(a,b):return tuple(u+v for u,v in zip(a,b))
def neg(a):return tuple(-u for u in a)
def sub(a,b):return add(a,neg(b))
def mul(a,b):
    c=[F(0)]*7
    for i,u in enumerate(a):
        for j,v in enumerate(b):c[i+j]+=u*v
    for k in range(6,3,-1):
        for j in range(1,5):c[k-j]-=c[k]
    return tuple(c[:4])
def inv(a):
    cols=[mul(a,tuple(F(int(i==j)) for i in range(4))) for j in range(4)]
    rows=[[cols[j][i] for j in range(4)]+[one[i]] for i in range(4)]
    for j in range(4):
        p=next(i for i in range(j,4) if rows[i][j])
        rows[j],rows[p]=rows[p],rows[j]
        c=rows[j][j];rows[j]=[v/c for v in rows[j]]
        for i in range(4):
            if i!=j:
                c=rows[i][j];rows[i]=[u-c*v for u,v in zip(rows[i],rows[j])]
    result=tuple(rows[i][-1] for i in range(4));assert mul(a,result)==one
    return result
powers=[one]
for i in range(1,6):powers.append(mul(powers[-1],x))
assert powers[5]==one and add(add(add(add(one,powers[1]),powers[2]),powers[3]),powers[4])==zero
def conj(a):
    out=zero
    for i,v in enumerate(a):out=add(out,tuple(v*t for t in powers[(-i)%5]))
    return out
def sign_surd(a,b):
    if b==0:return (a>0)-(a<0)
    if a==0:return (b>0)-(b<0)
    if (a>0)==(b>0):return 1 if a>0 else -1
    difference=a*a-5*b*b
    assert difference
    return (1 if a>0 else -1)*(1 if difference>0 else -1)
def norm_minus_one_sign(a):
    c=sub(mul(a,conj(a)),one)
    assert c[1]==0 and c[2]==c[3]
    return sign_surd(c[0]-c[2]/2,-c[2]/2)
def enc(a):return [str(v) for v in a]
nodes={};pairs=[]
for i in range(1,5):
    for j in range(i,5):
        u,v=powers[i],powers[j]
        alpha=sub(add(u,v),mul(u,v))
        beta=mul(mul(u,v),inv(sub(add(u,v),one)))
        assert mul(beta,conj(alpha))==one
        pair={'i':i,'j':j,'alpha':enc(alpha),'beta':enc(beta)};pairs.append(pair)
        for kind,value in [('alpha',alpha),('beta',beta)]:
            assert value!=zero and value not in powers[:5]
            s=norm_minus_one_sign(value);assert s in (-1,1)
            entry=nodes.setdefault(value,{'q':enc(value),'region':'inner' if s<0 else 'outer','occurrences':[],'physical_nodes':0})
            entry['occurrences'].append([i,j,kind]);entry['physical_nodes']+=1 if i==j else 2
assert len(nodes)==18
regions={side:{'base_values':sum(n['region']==side for n in nodes.values()),
               'physical_nodes':sum(n['physical_nodes'] for n in nodes.values() if n['region']==side)} for side in ['inner','outer']}
assert regions=={'inner':{'base_values':9,'physical_nodes':16},'outer':{'base_values':9,'physical_nodes':16}}
duplicates=[n['occurrences'] for n in nodes.values() if len(n['occurrences'])>1]
assert sorted(sorted(v) for v in duplicates)==sorted([[[1,4,'alpha'],[2,3,'beta']],[[1,4,'beta'],[2,3,'alpha']]])
out={'result':'PASS','method':'Independent Fraction arithmetic in basis1,x,x2,x3; x4=−1−x−x2−x3. No producer imports or symbolic cyclotomic routines.',
     'pairs':pairs,'critical_values':list(nodes.values()),'regions':regions,'only_duplicate_occurrences':duplicates,'elapsed_seconds':time.monotonic()-start}
(Path(__file__).resolve().parent/'quotient_collisions_independent_review21.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS all20 exact candidates, only2 duplicate pairs,18 distinct critical values')
print('PASS',regions);print('duplicates',duplicates);print('elapsed',out['elapsed_seconds'])
