"""Exact marked comparison of the failed edge relation and source word.

Free-word identities retain the regional [k,a] factor explicitly.  The
actual HNN edge map is invoked only where its full marked relation is
known; no edge enlargement is assumed.
"""
from pathlib import Path
import json
import hashlib

ROOT = Path(__file__).resolve().parents[2]
checks = []

def red(w, cones=()):
    s=[]
    for x in w:
        x=abs(x) if abs(x) in cones else x
        if s and (s[-1]==-x or (x in cones and s[-1]==x)): s.pop()
        else: s.append(x)
    return s
def inv(w): return [-x for x in w[::-1]]
def mul(*ws): return red([x for w in ws for x in w])
def cj(u,v): return mul(u,v,inv(u))
def com(u,v): return mul(u,v,inv(u),inv(v))
def eq(name,l,r,cones=()):
    assert red(l,cones)==red(r,cones),(name,red(l,cones),red(r,cones))
    checks.append(name)

# First: all selected-cone and stable-letter identities in F(a)*C2(C)*C2(j).
a,C,j=[1],[2],[3]
a1=mul(C,a,C)
j1=mul(C,j,C)
t=mul(j,j1)
v0=mul(j,a,inv(a1),j)
t0=mul(j,a,inv(a1),j1)
tau=mul(j,a,C,inv(a),j)
eq('t0=v0t',t0,mul(v0,t),(2,3))
eq('tau=t0C',tau,mul(t0,C),(2,3))
eq('tau a tau=t0 a1 t0^-1',mul(tau,a,tau),cj(t0,a1),(2,3))
eq('N_tau(a)=a v0 (t a1 t^-1) v0^-1',mul(a,tau,a,tau),mul(a,cj(v0,cj(t,a1))),(2,3))

# Second: universal free identities, before imposing [k,a]=1.
# Basis: a,A,q,k,y; q=p(a1), y=p(CvC), sigma(a1)=q y q^-1.
a,A,q,k,y=[[i] for i in range(1,6)]
v0=mul(A,inv(q)); sig=cj(q,y); s=cj(inv(v0),k)
N=mul(a,cj(v0,sig))
failure=com(s,sig)
eq('source commutator retains exact [k,a] factor',com(k,N),mul(com(k,a),cj(mul(a,v0),failure)))
reduced=com(cj(inv(A),k),y)
eq('failed edge relation q-conjugacy',cj(inv(q),failure),reduced)
eq('source relation is specified conjugate after [k,a]',com(k,N),mul(com(k,a),cj(mul(a,A),reduced)))

source=ROOT/'work_CE/next_symmetric_nodes/annular_neck_presentation23.json'
data=json.loads(source.read_text())
eta_a=data['eta_in_common_K']['1']
a=[1]; B=[2]
eq('actual v=a^-1 eta(a) a',mul(inv(a),eta_a,a),mul(B,inv(a),inv(B)))

out={'status':'PASS','checks':checks,'count':len(checks),
     'input':str(source.relative_to(ROOT)),'input_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
     'actual_eta_a':eta_a,
     'scope':'Literal selected-cone identities and universal commutator comparison. In the actual pre-cross star [k,a]=1, giving the exact conjugacy; no enlarged edge homomorphism or post-cross injection is asserted.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(f'PASS {len(checks)} exact edge/source identities; the regional [k,a] factor is retained before quotienting.')
