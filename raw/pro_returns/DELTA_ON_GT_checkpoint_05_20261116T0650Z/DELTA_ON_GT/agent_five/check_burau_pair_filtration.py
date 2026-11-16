"""Exact projective Burau pair certificates at a mixed coefficient modulus.
AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 16 November 2026.
Run: python -I -B check_burau_pair_filtration.py 4 (or 8).
"""
from collections import Counter
import json,sys
N=int(sys.argv[1]) if len(sys.argv)>1 else 2
els=range(N*N)
def ab(x):return x%N,x//N
def enc(a,b):return a%N+N*(b%N)
ADD=[[enc(ab(x)[0]+ab(y)[0],ab(x)[1]+ab(y)[1])for y in els]for x in els]
MUL=[[enc(ab(x)[0]*ab(y)[0]-ab(x)[1]*ab(y)[1],ab(x)[0]*ab(y)[1]+ab(x)[1]*ab(y)[0]-ab(x)[1]*ab(y)[1])for y in els]for x in els]
NEG=[enc(-ab(x)[0],-ab(x)[1])for x in els]
INV={x:next(y for y in els if MUL[x][y]==1)for x in els if any(MUL[x][y]==1 for y in els)}
I=(1,0,0,0,1,0,0,0,1)
w=N

def mm(a,b):
    return tuple(ADD[ADD[MUL[a[3*i]][b[j]]][MUL[a[3*i+1]][b[3+j]]]][MUL[a[3*i+2]][b[6+j]]]for i in range(3)for j in range(3))
def norm(a):
    for x in a:
        if x in INV:return tuple(MUL[INV[x]][y]for y in a)
    raise RuntimeError('no unit')
def pm(a,b):return norm(mm(a,b))
def power(a,n):
    out=I
    for _ in range(n):out=pm(out,a)
    return out
def mi(a):
    m=[list(a[3*i:3*i+3])+[int(i==j)for j in range(3)]for i in range(3)]
    for j in range(3):
        ii=next(i for i in range(j,3)if m[i][j]in INV)
        m[j],m[ii]=m[ii],m[j]
        z=INV[m[j][j]];m[j]=[MUL[z][x]for x in m[j]]
        for i in range(3):
            if i!=j:
                z=m[i][j];m[i]=[ADD[x][NEG[MUL[z][y]]]for x,y in zip(m[i],m[j])]
    return norm(tuple(x for row in m for x in row[3:]))
def order(a):
    out=I
    for n in range(1,10000):
        out=pm(out,a)
        if out==I:return n
    raise RuntimeError('large order')
def group(gens,bound=100000):
    seen={I};todo=[I]
    while todo:
        a=todo.pop()
        for b in gens:
            c=pm(a,b)
            if c not in seen:
                seen.add(c);todo.append(c)
                if len(seen)>bound:return seen,False
    return seen,True

gens=(norm((ADD[1][NEG[w]],w,0,1,0,0,0,0,1)),norm((1,0,0,0,ADD[1][NEG[w]],w,0,1,0)),norm((1,0,NEG[1],0,1,NEG[1],0,0,NEG[w])))
a,b,c=gens
assert pm(pm(a,b),a)==pm(pm(b,a),b)
assert pm(pm(b,c),b)==pm(pm(c,b),c)
assert pm(a,c)==pm(c,a)
assert power(pm(pm(a,b),c),4)==I
X=(power(a,2),power(b,2),power(c,2),power(pm(pm(a,b),a),2),power(pm(pm(c,b),c),2))

def comm(a,b):return pm(pm(pm(a,b),mi(a)),mi(b))
def derived(H,hgens):
    candidates=sorted({comm(g,h)for g in H for h in hgens})
    dg=[];D={I}
    for z in candidates:
        if z not in D:
            dg.append(z);D,ok=group(dg)
            assert ok
    assert all(pm(pm(h,d),mi(h))in D for h in hgens for d in D)
    return D,dg
def series(hgens):
    H,ok=group(hgens);assert ok
    chain=[H];gens0=list(hgens)
    while len(chain[-1])>1:
        D,gens0=derived(chain[-1],gens0)
        chain.append(D)
    return chain

# Check the original linear central word, before projectivization.
raw=((ADD[1][NEG[w]],w,0,1,0,0,0,0,1),
     (1,0,0,0,ADD[1][NEG[w]],w,0,1,0),
     (1,0,NEG[1],0,1,NEG[1],0,0,NEG[w]))
linear_full_twist=I
for g in raw*4:linear_full_twist=mm(linear_full_twist,g)
assert linear_full_twist==(w,0,0,0,w,0,0,0,w)

Delta=pm(pm(pm(pm(pm(a,b),c),a),b),a)
assert power(Delta,2)==I
assert pm(pm(Delta,a),Delta)==c and pm(pm(Delta,b),Delta)==b

edges=((2,3),(4,0),(1,2),(3,4),(0,1))
records=[];chains=[]
for i,j in edges:
    chain=series((X[i],X[j]));chains.append(chain)
    rec={'pair':[i+1,j+1],'derived_series_orders':[len(H)for H in chain],
         'generator_orders':[order(X[i]),order(X[j])],
         'product_order':order(pm(X[i],X[j]))}
    if len(chain)>4:
        rec['third_derived_matrices']=[list(g)for g in sorted(chain[3])]
    records.append(rec)

result={'modulus':N,'ring':'(Z/N)[w]/(w^2+w+1)',
        'matrix_encoding':'entry a+N*b represents a+b*w; tuples are row-major',
        'linear_full_twist':linear_full_twist,
        'centre_killed_after_projectivization':True,
        'braid_and_distant_commutation_relations_verified':True,
        'pair_certificates':records,
        'scope':'The map is defined on the label-five stabilizer B4/<z4>; induction gives a genuine five-point quotient. No direct B5 representation or GT lifting assertion is made.'}
if N==4:
    G,ok=group(gens);assert ok and len(G)==55296
    def red2(g):return tuple(ab(z)[0]%2+2*(ab(z)[1]%2)for z in g)
    kernel=[g for g in G if red2(g)==I]
    assert len({red2(g)for g in G})==216 and len(kernel)==256
    assert all(power(g,2)==I for g in kernel)
    result['whole_image_order']=len(G)
    result['mod2_image_order']=216
    result['elementary_abelian_reduction_kernel_dimension']=8
    assert [r['derived_series_orders']for r in records]==[
       [144,12,4,1],[144,12,4,1],[192,64,4,1],[48,12,4,1],[192,64,4,1]]
    result['actual_lift_obstruction']='The LI.8 actual gentle pair has f in F third derived and Delta=1. Its f-value is therefore identity in every displayed pair group; its entire pentagon image is identity here. This is a global lift, not a finite shadow.'
print(json.dumps(result,indent=2))
