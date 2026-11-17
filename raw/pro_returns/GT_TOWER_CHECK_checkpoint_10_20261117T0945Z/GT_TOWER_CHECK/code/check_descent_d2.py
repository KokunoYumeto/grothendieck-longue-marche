#!/usr/bin/env python3
"""Evaluate d2 on the 24 executed GAP source candidates, using exact affine markings.
This reads the actual finite census; it does not assert any profinite lift.
"""
from pathlib import Path
import ast, json
base=Path(__file__).resolve().parent
raw=(base/'check_descent_source_frames.out').read_text()
s=raw.split('Survivors [Delta,a mod2,j,e,l,C,H,finite automorphism]: ',1)[1].split('FINITE NECESSARY TEST COMPLETE',1)[0].strip()
rows=ast.literal_eval(s.replace('true','True').replace('false','False'))
def mm(a,b,n=3):return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2))%n for i in range(2) for j in range(2))
def mi(a,n=3):return(a[3]%n,-a[1]%n,-a[2]%n,a[0]%n)
def mp(a,k,n=3):
    if k<0:return mp(mi(a,n),-k,n)
    o=(1,0,0,1)
    for _ in range(k):o=mm(o,a,n)
    return o
def mob(a,z):
    if z is None:return None if a[2]%3==0 else a[0]*pow(a[2]%3,-1,3)%3
    d=(a[2]*z+a[3])%3
    return None if d==0 else (a[0]*z+a[1])*pow(d,-1,3)%3
# F4: 0,1,w,w^2 are encoded 0,1,2,3.
def fm(a,b):
    return (((a&1)*(b&1)+(a>>1)*(b>>1))%2)+2*(( (a&1)*(b>>1)+(a>>1)*(b&1)+(a>>1)*(b>>1))%2)
dictionary={None:0,0:2,1:1,2:3}
S=(0,1,2,0);U=(1,1,0,1);out=[]
for i,(delta,apar,j,e,l,C,H,automorphism) in enumerate(rows,1):
    a=next(a for a in range(6) if a%2==apar and a%3==l)
    beta=mm(mp(U,2*a),C)
    W=mm(mi(beta),mp(U,8*a))
    eps=next(k%2 for k in range(4) if mp(S,k)==W)
    translation=dictionary[mob(C,None)]
    # B.C24: C=f(s,tau) has translation -c*t_f; in F4 c=w, minus=plus.
    tf=fm(translation,3) # w^-1=w^2
    assert tf in (0,1)
    half_psi=tf # exact affine trace lemma: Psi3/2 = t_f modulo 2
    d2=(eps+half_psi)%2
    assert d2==0 and automorphism
    out.append(dict(candidate=i,Delta=delta,a_mod6=a,j=j,translation_C=translation,half_Psi3=half_psi,epsilon2_W=eps,d2=d2,C=C,H=H))
    print(i,'Delta=',delta,'j=',j,'trans(C)=',translation,'Psi3/2=',half_psi,'epsilon2(W)=',eps,'d2=',d2)
assert len(out)==24
assert sum(r['Delta']==0 for r in out)==12
(base/'check_descent_d2.json').write_text(json.dumps(out,indent=2)+'\n')
print('ALL 24 ACTUAL FINITE SOURCE CANDIDATES HAVE d2=0; 12 for each Delta bit.')
print('No full profinite lift is asserted.')
