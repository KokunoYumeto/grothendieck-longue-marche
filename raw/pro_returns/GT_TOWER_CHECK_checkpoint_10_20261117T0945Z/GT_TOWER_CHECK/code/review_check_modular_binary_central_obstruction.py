#!/usr/bin/env python3
"""Canonical central cusp obstruction above B/(K' K^2).

Uses the exact module (K' K^2)/[K,K' K^2] = Z^97 + (C2)^4656,
then the literal s,r coinvariants.  The selected finite automorphism
is the separately certified common-mod6 candidate0/1.
"""
from pathlib import Path
import sys,json,math
import numpy as np
from sympy import Matrix
from sympy.matrices.normalforms import hermite_normal_form,smith_normal_form
from sympy.polys.domains import ZZ
from flint import fmpz_mat

def column_hnf(A):
    """Exact FLINT row HNF, transposed to a column lattice basis."""
    rows=fmpz_mat([[int(x) for x in row] for row in A.T.tolist()]).hnf().tolist()
    rows=[row for row in rows if any(row)]
    return Matrix(rows).T

HERE=Path(__file__).resolve().parent.parent/'centralizer_code'
TOWER=HERE.parent/'tower_code';GHOST=HERE.parent/'ghost_code'
sys.path.insert(0,str(TOWER))
text=(TOWER/'test_fivepoint_cm_level.py').read_text()
ns={'__name__':'binary_central_prefix','__file__':str(HERE/'binary_central_prefix.py')}
exec(compile(text.split('records=[];base_records=[]',1)[0],str(TOWER/'test_fivepoint_cm_level.py'),'exec'),ns)
bt=ns['btable'];bgs=(ns['bxq'],ns['byq']);binv=ns['binverses']
bpaths=ns['bfpaths'];bstate=ns['bforder'];tree=ns['bftree'];loops=ns['bfloops']
chords=[(q,k) for q in bstate for k,g in enumerate(bgs) if (q,k) not in tree]
ci={a:i for i,a in enumerate(chords)}
n=len(loops);assert n==97
wi=ns['inverse'];subst=ns['subst']
SX=((2,),(1,));RX=((2,),(-2,-1))

def rewrite(w):
    q=0;out=[]
    for x in w:
        k=abs(x)-1
        if x>0:e=(q,k);q=int(bt[q,bgs[k]]);sign=1
        else:q=int(bt[q,binv[bgs[k]]]);e=(q,k);sign=-1
        if e in ci:out.append(sign*(ci[e]+1))
    assert q==0
    return tuple(out)

for i,w in enumerate(loops):assert rewrite(w)==(i+1,)
images={}
actions={}
for name,t in [('s',SX),('r',RX)]:
    words=[rewrite(subst(w,t)) for w in loops]
    A=np.zeros((n,n),dtype=np.int64)
    for i,w in enumerate(words):
        for x in w:A[i,abs(x)-1]+=1 if x>0 else -1
    images[name]=words;actions[name]=A
assert np.array_equal(actions['s']@actions['s'],np.eye(n,dtype=np.int64))
assert np.array_equal(actions['r']@actions['r']@actions['r'],np.eye(n,dtype=np.int64))
print('PASS exact integral actions on the97 modular Schreier generators',flush=True)

pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
pi={a:i for i,a in enumerate(pairs)}
d=len(pairs);assert d==4656
piv={}
def insert(v):
    while v:
        j=(v&-v).bit_length()-1
        if j not in piv:piv[j]=v;return True
        v^=piv[j]
    return False
def wedge(a,b):
    bits=0
    ia=np.flatnonzero(a%2);ib=np.flatnonzero(b%2)
    for i in ia:
        for j in ib:
            if i!=j:bits^=1<<pi[(min(int(i),int(j)),max(int(i),int(j)))]
    return bits
for name,A in actions.items():
    for k,(i,j) in enumerate(pairs):insert(wedge(A[i],A[j])^(1<<k))
    print('WEDGE relations after',name,'rank',len(piv),flush=True)
free=[i for i in range(d) if i not in piv];q=len(free)
coord=[0]*d;fi={a:i for i,a in enumerate(free)}
for i in range(d-1,-1,-1):
    if i not in piv:coord[i]=1<<fi[i];continue
    row=piv[i]^(1<<i);v=0
    while row:
        bit=row&-row;j=bit.bit_length()-1;v^=coord[j];row^=bit
    coord[i]=v
def project(v):
    out=0
    while v:
        bit=v&-v;out^=coord[bit.bit_length()-1];v^=bit
    return out
for name,A in actions.items():
    for k,(i,j) in enumerate(pairs):assert project(wedge(A[i],A[j]))==coord[k]
print('PASS full wedge coinvariant quotient dimension',q,flush=True)

def bitvector(v):return [(v>>i)&1 for i in range(q)]
def quadratic(a):
    ids=np.flatnonzero(a%2);v=0
    for ii,i in enumerate(ids):
        for j in ids[ii+1:]:v^=coord[pi[(int(i),int(j))]]
    return v
relations=[]
for A in actions.values():
    for i,row in enumerate(A):
        rel=row.copy();rel[i]-=1
        relations.append(rel.tolist()+bitvector(quadratic(row)))
for i in range(q):
    rel=[0]*(n+q);rel[n+i]=2;relations.append(rel)
Rmat=Matrix(relations).T
np.savez_compressed(Path(__file__).with_name('modular_binary_central_presentation.npz'),
    s_action=actions['s'],r_action=actions['r'],
    wedge_projection=np.array([bitvector(c) for c in coord],dtype=np.int8),
    central_relations=np.array(relations,dtype=np.int64))
H=column_hnf(Rmat)
assert H.shape==(n+q,n+q)
detM=abs(int(H.det()))
print('PASS full canonical multiplier relation lattice; order',detM,flush=True)
Hinv=H.inv(method='DM')
def member(v,inv=Hinv):return all(z.q==1 for z in inv*Matrix(v))

def collect(w):
    a=np.zeros(n,dtype=np.int64);c=0
    for letter in w:
        i=abs(letter)-1
        for j in range(i+1,n):
            if a[j]%2:c^=coord[pi[(i,j)]]
        a[i]+=1 if letter>0 else -1
    return a,c
def central(w):
    a,c=collect(w);assert not np.any(a%2)
    return (a//2).tolist()+bitvector(c)

# The full pure finite s-centralizer lies in K/K'K^2 by MIF.7.
# Its vectors are the kernel of the actual s-I action.
S=actions['s']
_,nullproj=ns['row_space_projection']((S-np.eye(n,dtype=np.int64)).T,2)
fixed=nullproj.T.astype(np.int64)
assert fixed.shape==(52,97)
assert not np.any(fixed@(S-np.eye(n,dtype=np.int64))%2)
kappas=[]
for v in fixed:
    w=tuple(i+1 for i in range(n) if v[i])
    sw=tuple(z for i in range(n) if v[i] for z in images['s'][i])
    k=central(w+wi(sw));assert member([2*z for z in k])
    kappas.append(k)
Hr=column_hnf(Matrix(relations+kappas).T)
assert Hr.shape==H.shape
detRed=abs(int(Hr.det()))
print('PASS all52 pure s-centralizer corrections; reduced multiplier order',detRed,flush=True)

record=np.load(HERE/'check_common_mod6_automorphism.npz')
mod=np.load(GHOST/'check_fivepoint_binary_module.npz')
L=mod['projection_left_inverse'].astype(np.int64)
src_loops=ns['jloops'];src_paths=ns['jpaths']
def sourceword(v,base):
    raw=np.asarray(v,dtype=np.int64)@L%2
    return tuple(z for i in range(len(raw)) if raw[i] for z in src_loops[i])+src_paths[base]
beta=sourceword(record['beta_2'],252)
Aword=sourceword(record['A_2'],0)
delta=beta+subst(wi(beta)+Aword+subst(wi(Aword),RX),SX)
dk=central(rewrite(delta))
in_full=member(dk)
redcoords=Hr.inv(method='DM')*Matrix(dk)
in_reduced=all(z.q==1 for z in redcoords)
two_primary_zero=all(int(z.q)%2==1 for z in redcoords)
print('CUSP defect zero in full multiplier:',in_full,flush=True)
print('CUSP defect killed by actual pure s-centralizer corrections:',in_reduced,flush=True)
print('TWO-PRIMARY cusp defect killed by those corrections:',two_primary_zero,flush=True)
out={'scope':'Exact full canonical central obstruction at the binary modular source for the fixed finite record.',
     'rank_K':n,'wedge_dimension':d,'wedge_coinvariant_dimension':q,
     'canonical_multiplier_order':detM,'reduced_by_s_multiplier_order':detRed,
     's_centralizer_dimension':52,'defect_zero':in_full,'defect_killed_by_s_corrections':in_reduced,
     'two_primary_defect_killed_by_s_corrections':two_primary_zero,
     'defect_vector':dk,'reduced_coordinates':[str(z) for z in redcoords],
     'source_word_lengths':{'beta':len(beta),'A':len(Aword),'defect':len(delta)},
     'all_assertions_passed':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
np.savez_compressed(Path(__file__).with_suffix('.npz'),s_action=actions['s'],r_action=actions['r'],
    wedge_projection=np.array([bitvector(c) for c in coord],dtype=np.int8),
    central_relations=np.array(relations,dtype=np.int64),kappas=np.array(kappas,dtype=np.int64),
    defect=np.array(dk,dtype=np.int64))
