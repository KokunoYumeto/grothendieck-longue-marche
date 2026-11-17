"""Reconstructed exact C41 graph certificate, 16 November 2026.
Uses the checkpoint06 A5 matrix enumeration, but no lost seventh-hour output.
The theorem is proved independently for every finite head.
"""
from contextlib import redirect_stdout
from io import StringIO
with redirect_stdout(StringIO()):
    import check_a5_duality_orbits as G
Q=G.Q;mul=G.qm;inv=G.qiv;one=G.qe
x,y=G.canon[4]
assert (G.order(x),G.order(y),G.order(mul[x][y]))==(3,5,2)
hs=[h for h in range(60) if G.qcon[h][x]==inv[x] and G.qcon[h][y]==inv[y]]
assert len(hs)==1
h=hs[0];kap=G.qcon[h]
assert all(kap[kap[g]]==g for g in range(60))
E=[(g,i) for g in range(60) for i in range(2)]
ei={a:i for i,a in enumerate(E)};gens=[x,y]
cp=[ei[(mul[kap[g]][inv[gens[i]]],i)] for g,i in E]
assert all(cp[cp[i]]==i for i in range(120))
bound=[(1<<g)^(1<<mul[g][gens[i]]) for g,i in E]
def basis(vs):
    piv={}
    for v in vs:
        while v:
            j=v.bit_length()-1
            if j not in piv:piv[j]=v;break
            v^=piv[j]
    return piv
def contains(piv,v):
    while v:
        j=v.bit_length()-1
        if j not in piv:return False
        v^=piv[j]
    return True
def boundary(v):
    out=0
    while v:
        b=v&-v;i=b.bit_length()-1;out^=bound[i];v^=b
    return out
orbits=[];seen=set()
for i in range(120):
    if i in seen:continue
    o={i,cp[i]};seen|=o;orbits.append(o)
invariant=[sum(1<<i for i in o) for o in orbits]
bb=[boundary(v) for v in invariant];bp=basis(bb)
fixed_vertices=[g for g in range(60) if kap[g]==g]
fixed_edges=[i for i in range(120) if cp[i]==i]
assert len(fixed_vertices)==4 and len(fixed_edges)==8
assert len(invariant)==64 and len(bp)==28
assert len(basis(bound))==59
for v in bb:
    assert all(not (v>>g)&1 for g in fixed_vertices)
for g in fixed_vertices:
    yes=contains(bp,(1<<g)^(1<<one))
    assert yes==(g==one)
    print('fixed head',Q[g],'identity' if g==one else 'excluded','boundary solvable',yes)
fake=G.qi[min((0,2,2,0),G.ng((0,2,2,0)))]
assert fake==h and fake in fixed_vertices and fake!=one
print('A5 generators:',Q[x],Q[y],'; inversion conjugator:',Q[h])
print('vertices60 edges120 cycle rank61')
print('fixed vertices4 fixed reversed edges8')
print('invariant chains64 boundary image28 invariant cycles36')
print('All3 nonidentity fixed head values excluded in the actual first relation module: PASS')
print('Scope: f must vanish in this enlarged quotient; f_Q=1 alone is insufficient.')
