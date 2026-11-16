"""Exact stabilizer image on the informative D4 proper three-space.

The target is the character orbit of (1,0,1,1,0).  This is a local
structural gate, not an assertion about all characters or an R2 lift.
"""
from pathlib import Path
from collections import deque
import json
import numpy as np

ROOT=Path(__file__).resolve().parents[2]
D=np.load(ROOT/'agent_five'/'ferrari_d4_proper16.npz')
ADD=[[(a%3+b%3)%3+3*((a//3+b//3)%3)for b in range(9)]for a in range(9)]
MUL=[[((a%3)*(b%3)-(a//3)*(b//3))%3+3*(((a%3)*(b//3)+(a//3)*(b%3))%3)for b in range(9)]for a in range(9)]
NEG=[(-a%3)%3+3*(-(a//3)%3)for a in range(9)]
INV=[0]+[next(b for b in range(1,9)if MUL[a][b]==1)for a in range(1,9)]
I=(1,0,0,0,1,0,0,0,1)
def mm(a,b):
    return tuple(ADD[ADD[MUL[a[3*i]][b[j]]][MUL[a[3*i+1]][b[3+j]]]][MUL[a[3*i+2]][b[6+j]]]
                 for i in range(3)for j in range(3))
def mi(a):
    r=[list(a[3*i:3*i+3])+[int(i==j)for j in range(3)]for i in range(3)]
    for j in range(3):
        k=next(i for i in range(j,3)if r[i][j]);r[j],r[k]=r[k],r[j]
        sc=INV[r[j][j]];r[j]=[MUL[sc][v]for v in r[j]]
        for i in range(3):
            if i==j:continue
            f=r[i][j]
            r[i]=[ADD[x][NEG[MUL[f][y]]]for x,y in zip(r[i],r[j])]
    out=tuple(v for row in r for v in row[3:]);assert mm(a,out)==I
    return out
def comm(a,b):return mm(mm(mm(a,b),mi(a)),mi(b))
def closure(gens,bound=300000):
    gens=list(dict.fromkeys(g for g in gens if g!=I))
    G=[I];seen={I}
    for g in G:
        for h in gens:
            z=mm(g,h)
            if z not in seen:seen.add(z);G.append(z)
        if len(G)>bound:raise RuntimeError('Exact declared group enumeration bound exceeded')
    return G,seen

p=D['permutations'].astype(int)
mat=[[tuple(map(int,b.ravel()))for b in blocks]for blocks in D['proper_blocks']]
reps=[None]*16;reps[0]=I;words=[None]*16;words[0]=();todo=[0]
for q in todo:
    for k in range(2):
        r=int(p[k,q])
        if reps[r]is None:
            reps[r]=mm(mat[k][q],reps[q]);words[r]=(k+1,)+words[q];todo.append(r)
assert len(todo)==16
schreier=[]
for q in range(16):
    for k in range(2):
        r=int(p[k,q]);m=mm(mm(mi(reps[r]),mat[k][q]),reps[q])
        word=tuple(-v for v in reversed(words[r]))+(k+1,)+words[q]
        schreier.append((m,word))
# Select a small generating subset without guessing the eventual group.
selected=[];G=[I];seen={I}
for m,w in schreier:
    if m not in seen:
        selected.append((m,w));G,seen=closure([a for a,b in selected])
        print(json.dumps({'step_generators':len(selected),'current_order':len(G)}),flush=True)

# Normal-closure seed is the genuine S, restricted to this proper block.
Sdata=np.load(ROOT/'agent_five'/'ferrari_d4_controlled_seed.npz')['seed_blocks'][24]
idx=int(D['character_indices'][0]);B=D['basis'][0];Bi=D['basis_inverse'][0]
def nmm(a,b):
    r=np.zeros((a.shape[0],b.shape[1]),dtype=np.int64)
    aa=np.array(ADD);mmul=np.array(MUL)
    for k in range(a.shape[1]):r=aa[r,mmul[a[:,k,None],b[None,k,:]]]
    return r
ad=nmm(nmm(Bi,Sdata[idx]),B)
# Basis order is boundary(1), proper(3), augmentation(1).
s=tuple(map(int,ad[1:4,1:4].ravel()))
assert s in seen
all_S=np.load(ROOT/'agent_five'/'ferrari_d4_controlled_seed.npz')['seed_blocks'][24:30]
for core in range(6):
    for q,index in enumerate(D['character_indices']):
        adapted=nmm(nmm(D['basis_inverse'][q],all_S[core,int(index)]),D['basis'][q])
        assert int(adapted[0,0])==1 and int(adapted[4,4])==1
        assert not np.any(adapted[1:,0])and not np.any(adapted[4,:4])
        proper=tuple(map(int,adapted[1:4,1:4].ravel()))
        transported=mm(mm(mi(reps[q]),proper),reps[q])
        assert transported in seen
orbit=[s];os={s};gi=[(g,mi(g))for g,w in selected]
for h in orbit:
    for g,g_inv in gi:
        z=mm(mm(g,h),g_inv)
        if z not in os:os.add(z);orbit.append(z)
normal_generators=[];NG=[I];ns={I}
for h in orbit:
    if h not in ns:
        normal_generators.append(h);NG,ns=closure(normal_generators)
        if len(NG)==len(G):break
derived_gens=[];DG=[I];ds={I}
for g in NG:
    for h in normal_generators:
        cc=comm(g,h)
        if cc not in ds:
            derived_gens.append(cc);DG,ds=closure(derived_gens)
            if len(DG)==len(NG):break
    if len(DG)==len(NG):break

# A direct simplicity certificate, avoiding an identification by order.
# Conjugacy orbits under the selected generators are the full classes.
unseen=set(G);classes=[]
while unseen:
    h=min(unseen);cl=[h];cs={h}
    for a in cl:
        for g,g_inv in gi:
            z=mm(mm(g,a),g_inv)
            if z not in cs:cs.add(z);cl.append(z)
    unseen.difference_update(cs)
    if h==I:
        classes.append({'size':1,'normal_closure_order':1});continue
    ncgens=[];NC=[I];ncs={I}
    for a in cl:
        if a not in ncs:
            ncgens.append(a);NC,ncs=closure(ncgens)
            if len(NC)==len(G):break
    classes.append({'size':len(cl),'normal_closure_order':len(NC)})
assert sum(c['size']for c in classes)==len(G)
assert all(c['normal_closure_order']==len(G)for c in classes if c['size']!=1)
assert len([c for c in classes if c['size']==1])==1

out={'character_orbit':D['character_indices'].tolist(),
     'character_stabilizer_proper_image_order':len(G),
     'selected_stabilizer_generator_words':[list(w)for m,w in selected],
     'seed_proper_conjugacy_orbit_size':len(orbit),
     'normal_closure_of_S_proper_image_order':len(NG),
     'normal_closure_derived_order':len(DG),
     'normal_closure_is_perfect':len(DG)==len(NG),
     'all_six_core_seeds_fix_boundary_and_augmentation_on_entire_orbit':True,
     'all96_proper_core_values_belong_to_transported_simple_stabilizer_groups':True,
     'conjugacy_class_normal_closure_certificate':classes,
     'proper_stabilizer_image_is_nonabelian_simple':True,
     'scope':'Local proper-space stabilizer structure only. Original orbifold cores, all character components, and the full-chain nilpotent kernel are separate requirements.'}
(ROOT/'agent_lifting'/'records'/'d4_proper_stabilizer.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
