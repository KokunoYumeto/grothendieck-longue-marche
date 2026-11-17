#!/usr/bin/env python3
"""Literal two-sheet correction. No target enumeration or orbit search."""
from pathlib import Path
import json

def red(w):
    a=[]
    for x in w:
        if a and a[-1]==-x: a.pop()
        else: a.append(x)
    return a
def inv(w): return [-x for x in reversed(w)]
def mul(*ws): return red(x for w in ws for x in w)
def sub(w,d): return mul(*(d[abs(x)] if x>0 else inv(d[abs(x)]) for x in w))
def conj(a,b): return mul(a,b,inv(a))
def comm(a,b): return mul(a,b,inv(a),inv(b))

# a,a1,k,k1,p(a),p(a1),p(k),p(k1),t
theta={1:[5],2:[6],3:[7],4:[8],5:[1],6:[2],7:[3],8:[4],9:[-9]}
v0=[5,-6]; w0=[1,-2]
s=conj(inv(v0),[3]); sp=conj(inv(w0),[7])
r0=mul(v0,[9,4,-9],inv(v0),[-3])
r1=mul([9,4,-9],inv(s))
r2=mul([9],sp,[-9,-8])
assert sub(v0,theta)==w0
assert r0==conj(v0,r1)
assert sub(r0,theta)==conj(mul(w0,[-9]),inv(r2))
for i in range(1,10): assert sub(theta[i],theta)==[i]

# Independent regional winding quotient: left k, right kprime, stable t.
q={1:[],2:[],3:[1],4:[1],5:[],6:[],7:[2],8:[2],9:[3]}
assert sub(r1,q)==comm([3],[1])
assert sub(r2,q)==comm([3],[2])
# Killing left winding as well leaves the second relation a reduced
# commutator in the ordinary free group on kprime,t.
q2={**q,3:[],4:[]}
assert sub(r1,q2)==[]
assert sub(r2,q2)==[3,2,-3,-2]

data={'status':'PASS','basis':['a','a1','k','k1','p(a)','p(a1)','p(k)','p(k1)','t'],'theta':theta,'v0':v0,'w0':w0,'s':s,'sprime':sp,'r0':r0,'first_cross_equation_relator':r1,'second_cross_equation_relator':r2,'theta_r0':sub(r0,theta),'quotient_first':sub(r1,q),'quotient_second':sub(r2,q),'free_two_omission_witness':sub(r2,q2),'scope':'The previous one-cross presentation omitted the second mirror sheet. Both relators are retained in the corrected actual pushout. The omission witness is a reduced free word, not a finite census.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(data,indent=2)+'\n')
print('PASS literal theta involution, both full conjugacy identities, and two distinct cross equations.')
print('PASS omission certificate: first cross dies after left winding is killed; mirror mate is the reduced word t kprime t^-1 kprime^-1 in F2.')
