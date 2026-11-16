"""Identify the exact Prym blocks carrying the rank129 nonnilpotence witness.
Written by GPT-6 Astra, OpenAI, 16 November 2026.
"""
from pathlib import Path
import numpy as np,json
ROOT=Path(__file__).resolve().parent
F=np.load(ROOT/'ferrari_rank129.npz');D=np.load(ROOT/'ferrari_rank129_blocks.npz')
meta=json.loads((ROOT/'check_rank129_deck_blocks.out').read_text())
Q=F['Q'];right=F['right'];bs=D['deck_basis'];offset=D['offsets']
def qw(w):
    q=0
    for i in w:q=int(right[q,i])
    return q
coords={}
for m in range(32):
    v=0
    for j,b in enumerate(bs):
        if m&(1<<j):v^=int(b)
    coords[v]=m
w=(1,0,2);u=(1,0);v=(2,0)
cusp=[]
for q in ((),u,v,u+v):
    g=Q[qw(q+w+w+q[::-1])];assert g[1]==0;cusp.append(coords[int(g[0])])
assert len(set(cusp))==4
branch={m:sum((m&q).bit_count()%2 for q in cusp)for m in range(32)}
def mm(a,b):return a@b%3
def power(a,k):
    out=np.eye(a.shape[0],dtype=np.int16)
    while k:
        if k&1:out=mm(out,a)
        a=mm(a,a);k//=2
    return out
def inv(a):
    n=a.shape[0];I=np.eye(n,dtype=np.int16);R=np.concatenate((a.copy(),I),axis=1)
    for j in range(n):
        k=j+int(np.flatnonzero(R[j:,j])[0]);R[[j,k]]=R[[k,j]]
        if R[j,j]==2:R[j]=2*R[j]%3
        inds=np.flatnonzero(R[:,j]);inds=inds[inds!=j]
        R[inds]=(R[inds]-R[inds,j,None]*R[j])%3
    return R[:,n:]
def prod(*gg):
    out=np.eye(gg[0].shape[0],dtype=np.int16)
    for g in gg:out=mm(out,g)
    return out
def order(a,limit=256):
    n=a.shape[0];I=np.eye(n,dtype=np.int16);b=I
    for i in range(1,limit+1):
        b=mm(b,a)
        if np.array_equal(b,I):return i
    return None
def comm(a,b):return prod(a,b,inv(a),inv(b))
def rank(M):
    R=M.copy();r=0
    for j in range(R.shape[1]):
        ix=np.flatnonzero(R[r:,j])
        if not len(ix):continue
        k=r+int(ix[0]);R[[r,k]]=R[[k,r]]
        if R[r,j]==2:R[r]=2*R[r]%3
        inds=np.flatnonzero(R[:,j]);inds=inds[inds!=r]
        R[inds]=(R[inds]-R[inds,j,None]*R[r])%3
        r+=1
        if r==R.shape[0]:break
    return r
reports=[]
for orb in meta['full_L_character_orbits']:
    ix=[i for m in orb for i in range(*offset[m])]
    xx=[M[np.ix_(ix,ix)]for M in D['X']]
    x,y=xx[:2];c=comm(x,y);w=comm(c,prod(x,c,inv(x)));a=power(w,6);g=prod(x,inv(y));b=prod(g,a,inv(g));ab=mm(a,b)
    reports.append({'character_orbit':orb,'dimension':len(ix),
                    'branch_counts':sorted(set(branch[m]for m in orb)),
                    'w_order':order(w),'involution_minus_identity_rank':rank((a-np.eye(len(ix),dtype=np.int16))%3),
                    'involutions_product_order':order(ab)})
small=[]
for m in range(32):
    if branch[m]!=4:continue
    aa,bb=offset[m];ix=list(range(aa,bb))
    # These four characters are fixed by every pure Xi.
    assert all(not np.any(M[np.ix_([i for i in range(129)if i not in ix],ix)])for M in D['X'])
    xx=[M[np.ix_(ix,ix)]for M in D['X']]
    x,y=xx[:2];c=comm(x,y);w=comm(c,prod(x,c,inv(x)));a=power(w,6);g=prod(x,inv(y));b=prod(g,a,inv(g))
    row={'character':m,'Xi':[M.tolist()for M in xx],
         'w_order':order(w),'involution_rank':rank((a-np.eye(4,dtype=np.int16))%3),'product_order':order(mm(a,b)),
         'whole_L_invariant':all(int(p[m])==m for p in D['abc_permutations'])}
    if row['whole_L_invariant']:
        row['abc']=[D[k][np.ix_(ix,ix)].tolist()for k in ('A','B','C')]
        np.savez_compressed(ROOT/'ferrari_prym4.npz',A=np.array(row['abc'][0],dtype=np.int16),B=np.array(row['abc'][1],dtype=np.int16),C=np.array(row['abc'][2],dtype=np.int16),X=np.stack(xx),character=m)
    small.append(row)
out={'cusp_coordinates_in_deck_basis':cusp,
     'unramified_nontrivial_characters':[m for m in range(1,32)if branch[m]==0],
     'two_branch_characters':[m for m in range(32)if branch[m]==2],
     'four_branch_characters':[m for m in range(32)if branch[m]==4],
     'full_L_orbit_witness_reports':reports,'four_branch_blocks':small,
     'scope':'Exact literal common-source Prym blocks; geometric branch counts are computed from the four actual cusp words.'}
print(json.dumps(out,indent=2))
