"""Exact finite-field Bass--Serre/Shapiro terms for the universal quotient.

This computes terms of the homology spectral sequence.  It does not identify
the entire Schur multiplier or discard any differential.
"""
import json
from collections import deque
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parent
data=json.loads((ROOT/'universal_relation_module_data.json').read_text())
edges=[(u-1,v-1) for u,v in data['edge_endpoints']]
nv=sum(data['vertex_counts']); ne=len(edges)
adj=[[] for _ in range(nv)]
for e,(u,v) in enumerate(edges):
    adj[u].append((v,e,1)); adj[v].append((u,e,-1))
paths=np.zeros((nv,ne),dtype=np.int64)
seen={0}; queue=deque([0]); tree=[]
while queue:
    v=queue.popleft()
    for w,e,sign in adj[v]:
        if w in seen: continue
        seen.add(w);queue.append(w);tree.append(e)
        paths[w]=paths[v];paths[w,e]+=sign
assert len(seen)==nv
non_tree=[e for e in range(ne) if e not in set(tree)]
cycles=[]
for e in non_tree:
    u,v=edges[e]
    row=paths[u]-paths[v];row=row.copy();row[e]+=1;cycles.append(row)
cycles=np.array(cycles,dtype=np.int64)
d=len(cycles)
boundary=np.zeros((ne,nv),dtype=np.int64)
for e,(u,v) in enumerate(edges): boundary[e,u]=-1;boundary[e,v]=1
assert d==25 and not np.any(cycles@boundary)
assert np.array_equal(cycles[:,non_tree],np.eye(d,dtype=np.int64))
matrices=[]
for action in data['left_inverse_actions']:
    perm=np.array(action,dtype=int)-1
    moved=np.zeros_like(cycles);moved[:,perm]=cycles
    assert not np.any(moved@boundary)
    matrix=moved[:,non_tree]
    assert np.array_equal(matrix@cycles,moved)
    matrices.append(matrix)
for i,inv in enumerate(data['inverse_indices']):
    assert np.array_equal(matrices[i]@matrices[inv-1],np.eye(d,dtype=np.int64))
print(f'Bass--Serre graph: vertices={nv}, edges={ne}, cycle rank={d}; all 144 integer actions checked.',flush=True)

def rank_mod(rows,p):
    """Bit-exact elimination, including a two-bit-plane GF(3) collector."""
    rows=np.asarray(rows,dtype=np.int64)%p
    n=rows.shape[1]; basis={}; mask=(1<<n)-1
    for row in rows:
        if p==2:
            bits=sum(1<<int(i) for i in np.flatnonzero(row))
            while bits:
                piv=bits.bit_length()-1
                if piv not in basis: basis[piv]=bits;break
                bits^=basis[piv]
        else:
            a=sum(1<<int(i) for i in np.flatnonzero(row==1))
            b=sum(1<<int(i) for i in np.flatnonzero(row==2))
            while a|b:
                piv=(a|b).bit_length()-1
                if piv not in basis:
                    if b>>piv&1: a,b=b,a
                    basis[piv]=(a,b);break
                c,e=basis[piv]
                # Add negative pivot for coefficient 1, positive for 2.
                if a>>piv&1: c,e=e,c
                az=mask^(a|b);cz=mask^(c|e)
                a,b=(az&c)|(a&cz)|(b&e),(az&e)|(b&cz)|(a&c)
    return len(basis)

def rref(rows,p):
    a=np.array(rows,dtype=np.int64)%p; i=0;pivots=[]
    for j in range(a.shape[1]):
        found=np.flatnonzero(a[i:,j])
        if not len(found): continue
        k=i+int(found[0]);a[[i,k]]=a[[k,i]]
        a[i]=a[i]*pow(int(a[i,j]),-1,p)%p
        for k in np.flatnonzero(a[:,j]):
            if k!=i: a[k]=(a[k]-a[k,j]*a[i])%p
        pivots.append(j);i+=1
        if i==a.shape[0]:break
    return a[:i],pivots

def pc_words(record):
    _,orders,powers,conjugates,_=record
    def tail(exps): return [i+1 for i,e in enumerate(exps) for _ in range(e)]
    def inverse(word): return [-i for i in reversed(word)]
    words=[]
    for i,o in enumerate(orders): words.append([i+1]*o+inverse(tail(powers[i])))
    for i,j,exps in conjugates: words.append([-j,i,j]+inverse(tail(exps)))
    return words

def one_homology(record,p):
    order,orders,powers,conjugates,targets=record
    # Right contragredient module: H^1(G,V*) is dual to H_1(G,V).
    mats=[matrices[data['inverse_indices'][k-1]-1].T%p for k in targets]
    invmats=[matrices[k-1].T%p for k in targets]
    n=len(mats);relations=pc_words(record); constraints=[]
    for word in relations:
        blocks=np.zeros((n,d,d),dtype=np.int64); suffix=np.eye(d,dtype=np.int64)
        for letter in reversed(word):
            k=abs(letter)-1
            if letter>0:
                blocks[k]=(blocks[k]+suffix)%p
                suffix=mats[k]@suffix%p
            else:
                blocks[k]=(blocks[k]-invmats[k]@suffix)%p
                suffix=invmats[k]@suffix%p
        assert np.array_equal(suffix,np.eye(d,dtype=np.int64))
        constraints.extend(blocks.transpose(2,0,1).reshape(d,n*d))
    cob=np.concatenate([m-np.eye(d,dtype=np.int64) for m in mats],axis=1)%p
    rank_z=rank_mod(constraints,p);rank_b=rank_mod(cob,p)
    z_dim=n*d-rank_z;h_dim=z_dim-rank_b
    assert h_dim>=0
    print(f'H1(group order {order}, H1(L,F{p})): unknowns={n*d}, relation rows={len(constraints)}, relation rank={rank_z}, coboundary rank={rank_b}, dimension={h_dim}',flush=True)
    return {'order':order,'prime':p,'unknowns':n*d,'relation_rows':len(constraints),'relation_rank':rank_z,'coboundary_rank':rank_b,'dimension':h_dim,'pc_relations_verified':len(relations)}

def matching_term(which,p):
    subgroup=data['T2_indices'] if which==2 else data['T3_indices']
    rel=np.concatenate([matrices[k-1]-np.eye(d,dtype=np.int64) for k in subgroup],axis=0)%p
    rr,piv=rref(rel,p);free=[i for i in range(d) if i not in piv]
    q=np.eye(d,dtype=np.int64)
    for row,j in zip(rr,piv):
        q=(q-q[:,j,None]*row[None,:])%p
    q=q[:,free]; n=len(free)
    assert not np.any(rel@q%p)
    ms=matrices[data['s_index']-1][free,:]@q%p
    mr=matrices[data['r_index']-1][free,:]@q%p
    mt=ms@mr%p
    # Here row module matrices represent source group multiplication.
    if which==2:
        pairs=[(ms,mt),(mt,ms)]
    else:
        minvr=mr@mr%p
        pairs=[(ms,ms),(mt,ms@minvr@ms%p)]
    flip=np.zeros((n*n,n*n),dtype=np.int64)
    for i in range(n):
        for j in range(n):
            if which==2: flip[i*n+j,j*n+i]=-1
            else:
                for k in range(n):flip[i*n+j,j*n+k]=-ms[i,k]
    ident=np.eye(n*n,dtype=np.int64)
    rel2=np.concatenate([np.kron(a,b)-ident for a,b in pairs]+[flip-ident],axis=0)%p
    rank=rank_mod(rel2,p); dim=n*n-rank
    # Independent ordinary finite-field elimination for these small matrices.
    _,piv2=rref(rel2,p);assert len(piv2)==rank
    print(f'Exceptional matching common {"S3" if which==2 else "A4"} over F{p}: factor quotient dimension={n}, tensor/flip coinvariant dimension={dim}',flush=True)
    return {'common':'S3' if which==2 else 'A4','prime':p,'factor_dimension':n,'rank':rank,'coinvariant_dimension':dim,'s_matrix':ms.tolist(),'r_matrix':mr.tolist(),'flip':(flip%p).tolist()}

out={'graph':{'vertices':nv,'edges':ne,'rank':d},'one_homology':[],'matching_coinvariants':[]}
for p in (2,3):
    for name in ('T_pc','J_pc'):out['one_homology'].append(one_homology(data[name],p))
    for which in (2,3):out['matching_coinvariants'].append(matching_term(which,p))
(ROOT/'check_universal_relation_module.json').write_text(json.dumps(out,indent=2)+'\n')
print('Spectral-sequence terms only. No differential or reduced Schur multiplier conclusion has been assumed.',flush=True)
