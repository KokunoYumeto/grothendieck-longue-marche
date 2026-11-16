"""Exact local proper images of the common cyclic seed's normal closure.

All six source peripheral markings and all character transports are kept.
This classifies actual finite images; it is not an independent-f-values
pentagon census.  The scalar trivial character is recorded separately.
"""
from pathlib import Path
import json
import numpy as np
from check_ferrari_d4_fox import ROOT, mm as nmm, orbits, characters

ADD=[[(a%3+b%3)%3+3*((a//3+b//3)%3) for b in range(9)] for a in range(9)]
MUL=[[((a%3)*(b%3)-(a//3)*(b//3))%3+3*(((a%3)*(b//3)+(a//3)*(b%3))%3) for b in range(9)] for a in range(9)]
NEG=[(-a%3)%3+3*(-(a//3)%3) for a in range(9)]
INV=[0]+[next(b for b in range(1,9) if MUL[a][b]==1) for a in range(1,9)]
I=(1,0,0,0,1,0,0,0,1)
def mm(a,b):
    return tuple(ADD[ADD[MUL[a[3*i]][b[j]]][MUL[a[3*i+1]][b[3+j]]]][MUL[a[3*i+2]][b[6+j]]]
                 for i in range(3) for j in range(3))
def mi(a):
    r=[list(a[3*i:3*i+3])+[int(i==j) for j in range(3)] for i in range(3)]
    for j in range(3):
        k=next(k for k in range(j,3) if r[k][j]);r[j],r[k]=r[k],r[j]
        r[j]=[MUL[INV[r[j][j]]][v] for v in r[j]]
        for k in range(3):
            if k!=j:
                f=r[k][j];r[k]=[ADD[x][NEG[MUL[f][y]]] for x,y in zip(r[k],r[j])]
    return tuple(v for row in r for v in row[3:])
def comm(a,b):return mm(mm(mm(a,b),mi(a)),mi(b))
def closure(gens,bound=300000):
    gens=list(dict.fromkeys(g for g in gens if g!=I));G=[I];seen={I}
    for h in G:
        for g in gens:
            z=mm(h,g)
            if z not in seen:seen.add(z);G.append(z)
        if len(G)>bound:raise RuntimeError('declared exact enumeration bound exceeded')
    return G,seen
def small_generators(candidates):
    gs=[];G=[I];seen={I}
    for g in candidates:
        if g not in seen:gs.append(g);G,seen=closure(gs)
    return gs,G,seen
def normal_closure(initial,ambient_generators):
    gs,G,seen=small_generators(initial);changed=True
    ag=[(g,mi(g)) for g in ambient_generators]
    while changed:
        changed=False
        for h in list(gs):
            for g,gi in ag:
                z=mm(mm(g,h),gi)
                if z not in seen:
                    gs.append(z);G,seen=closure(gs);changed=True
    return gs,G,seen
def derived(gs):return normal_closure([comm(g,h) for g in gs for h in gs],gs)

data=np.load(ROOT/'ferrari_d4_fox.npz');fil=np.load(ROOT/'ferrari_d4_filtration.npz')
seed=np.load(ROOT/'ferrari_d4_controlled_seed.npz')['seed_blocks'][24:30]
T,Ti=fil['basis'],fil['basis_inverse'];bd,hd=fil['boundary_dimensions'],fil['homology_dimensions']
P=data['X_permutations'][:2]
M=np.stack([nmm(Ti[p],nmm(m,T)) for p,m in zip(P,data['X_blocks'][:2])])
S=np.stack([nmm(Ti,nmm(m,T)) for m in seed])
reports=[];saved={}
for orb in orbits(list(P)):
    rep=orb[0];b,h=int(bd[rep]),int(hd[rep]);dim=h-b
    if rep==0 or dim!=3:continue
    if np.array_equal(S[:,orb,b:h,b:h],np.broadcast_to(np.eye(3,dtype=np.int16),S[:,orb,b:h,b:h].shape)):continue
    lookup={q:k for k,q in enumerate(orb)}
    p=[[lookup[int(v)] for v in row[orb]] for row in P]
    mats=[[tuple(map(int,z.ravel())) for z in row[orb,b:h,b:h]] for row in M]
    reps=[None]*len(orb);words=[None]*len(orb);reps[0]=I;words[0]=();queue=[0]
    for q in queue:
        for g in range(2):
            r=p[g][q]
            if reps[r] is None:
                reps[r]=mm(mats[g][q],reps[q]);words[r]=(g+1,)+words[q];queue.append(r)
    assert len(queue)==len(orb)
    sch=[]
    for q in range(len(orb)):
        for g in range(2):
            r=p[g][q];sch.append(mm(mm(mi(reps[r]),mats[g][q]),reps[q]))
    hg,H,hs=small_generators(sch)
    initial=[]
    for q,ch in enumerate(orb):
        for k in range(6):
            s=tuple(map(int,S[k,ch,b:h,b:h].ravel()))
            s=mm(mm(mi(reps[q]),s),reps[q]);assert s in hs
            initial.append(s)
    ng,NG,ns=normal_closure(initial,hg)
    dg,DG,ds=derived(ng);series=[len(NG),len(DG)]
    while len(DG)>1 and len(DG)!=series[-2]:
        dg,DG,ds=derived(dg);series.append(len(DG))
    report={'representative':rep,'character':characters[rep].tolist(),'orbit_size':len(orb),
      'proper_dimension':3,'stabilizer_order':len(H),'stabilizer_generator_count':len(hg),
      'normal_image_order':len(NG),'normal_image_generator_count':len(ng),'normal_image_derived_orders':series,
      'perfect':len(NG)>1 and series[1]==series[0],
      'abelian':series[1]==1}
    reports.append(report);print(json.dumps(report),flush=True)
    saved[str(rep)]={'stabilizer_generators':[list(g) for g in hg],
       'normal_generators':[list(g) for g in ng],'character_orbit':orb}
(ROOT/'d4_proper_seed_classification.json').write_text(json.dumps(reports,indent=2)+'\n')
(ROOT/'d4_proper_seed_generators.json').write_text(json.dumps(saved,indent=2)+'\n')
print('Completed all active primitive character orbits, with all six source core values.')
