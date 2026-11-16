"""Exploratory exact Whitehead reduction of B67's full last-fiber word.

This supplies word/action data only. No topological filling or stabilizer
theorem is inferred without a separate proof and primary-source check.
"""
from pathlib import Path
import json,sys,itertools,time
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'next_B56'))
from membership_rigid7 import artin,substitute as sub,multiply as mul,inverse as inv,reduce_word as red
j=json.loads((HERE/'cyclic_rigid_braid_words.json').read_text());tau=(3,4,5)
ims={r['index']+1:mul(inv(tau),r['braid'],tau) for r in j['basis']}
w=(-5,-1,6,1,5,3,-5,-1,-6,1,5,-3)
v=list(artin(sub(w,ims),6)[-1]);q=[]
while len(v)>1:
    assert v[0]==-v[-1]
    q.append(v.pop(0));v.pop()
assert v==[6]
p=red(z for z in q if abs(z)!=6)
def cyclic(w):
    w=red(w)
    while len(w)>1 and w[0]==-w[-1]:w=w[1:-1]
    return w
initial=p;p=cyclic(p);steps=[];letters=tuple(range(1,6))+tuple(range(-5,0))
print('Initial fiber and cyclic lengths:',len(initial),len(p),flush=True)
while True:
    best=None;length=len(p)
    for a in letters:
        others=[b for b in letters if abs(b)!=abs(a)]
        for mask in range(1<<len(others)):
            A={a}|{b for i,b in enumerate(others) if mask>>i&1}
            phi={}
            for x in range(1,6):
                if x==abs(a):phi[x]=(x,)
                else:phi[x]=((-a,) if -x in A else ())+ (x,) + ((a,) if x in A else ())
            new=cyclic(sub(p,phi))
            if len(new)<length:best=(a,sorted(A),phi,new);length=len(new)
    if best is None:break
    a,A,phi,p=best
    steps.append({'multiplier':a,'set':A,'images':phi,'word':p})
    print('Reduced length',len(p),'support',sorted({abs(x) for x in p}),flush=True)
V=set(letters);edges=[(-a,b) for a,b in zip(p,p[1:]+p[:1])]
def components(drop=None):
    left=V-{drop};out=[]
    while left:
        todo=[left.pop()];c=set(todo)
        while todo:
            x=todo.pop()
            for a,b in edges:
                y=b if a==x else a if b==x else None
                if y in left:left.remove(y);c.add(y);todo.append(y)
        out.append(sorted(c))
    return out
cuts=[a for a in letters if len(components(a))>len(components())]
print('Final word:',p,flush=True)
print('Final Whitehead components:',components(),'cut vertices:',cuts,flush=True)
cert={'source':w,'fiber_word':initial,'initial_cyclic_word':cyclic(initial),
      'Whitehead_reductions':steps,'final_word':p,'final_components':components(),'final_cut_vertices':cuts,
      'scope':'Exact algebraic reduction only; no unverified geometric filling or stabilizer inference'}
(HERE/'full_Q_word_Whitehead_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
