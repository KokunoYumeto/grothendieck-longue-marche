"""Independent section-47 test on the characteristic S4 envelope.

Enumerates necessary finite cycle residues, not asserted liftable residues
of the full profinite GT0 or GT groups. Permutations use zero-based arrays.
"""
from itertools import permutations
from collections import Counter
from pathlib import Path
import json,time

t0=time.time()
perms=list(permutations(range(4))); ind={p:i for i,p in enumerate(perms)}
e=ind[tuple(range(4))]
mul=[[ind[tuple(p[q[i]] for i in range(4))] for q in perms] for p in perms]
inv=[next(j for j in range(24) if mul[i][j]==e) for i in range(24)]
def closure(a,b):
    seen={e};todo=[e]
    for v in todo:
        for g in (a,b):
            w=mul[v][g]
            if w not in seen:seen.add(w);todo.append(w)
    return seen
def conj(g,a):return mul[mul[g][a]][inv[g]]
reps=[];pairclass={}
for a in range(24):
    for b in range(24):
        if (a,b) in pairclass or len(closure(a,b))<24:continue
        i=len(reps);reps.append((a,b))
        for g in range(24):pairclass[conj(g,a),conj(g,b)]=i
assert len(reps)==9 and len(pairclass)==216
X=bytes(a for a,b in reps);Y=bytes(b for a,b in reps);E=bytes([e]*9)
def tm(a,b):return bytes(mul[i][j] for i,j in zip(a,b))
def ti(a):return bytes(inv[i] for i in a)
def tp(a,n):
    n%=12;z=E
    for _ in range(n):z=tm(z,a)
    return z
H=[E];index={E:0};parent=[-1];letter=[-1];ab=[0]
for v in H:
    vi=index[v]
    for j,g in enumerate((X,Y)):
        w=tm(v,g)
        if w not in index:
            index[w]=len(H);H.append(w);parent.append(vi);letter.append(j)
            ab.append(ab[vi]^(1<<j))
        else:
            assert ab[index[w]]==ab[vi]^(1<<j)
print('envelope',len(H),'derived',ab.count(0),'seconds',round(time.time()-t0,2),flush=True)
assert len(H)==442368 and ab.count(0)==110592
Z=ti(tm(X,Y))
def substitution(a,b):
    values=[E]*len(H)
    for i in range(1,len(H)):values[i]=tm(values[parent[i]],(a,b)[letter[i]])
    result=[index[v] for v in values]
    # Characteristic automorphism check on all directed Cayley edges.
    for i,v in enumerate(H):
        for g,im in ((X,a),(Y,b)):
            assert values[index[tm(v,g)]]==tm(values[i],im)
    assert len(set(result))==len(H)
    return result
theta=substitution(Y,X);omega=substitution(Y,Z)
print('substitutions checked',round(time.time()-t0,2),flush=True)

# PSL2(Z/4), with a fixed explicit isomorphism to the permutation S4
# supplied by its regular conjugation action on its four Sylow-3 groups.
def mm(a,b):return ((a[0]*b[0]+a[1]*b[2])%4,(a[0]*b[1]+a[1]*b[3])%4,
                    (a[2]*b[0]+a[3]*b[2])%4,(a[2]*b[1]+a[3]*b[3])%4)
def canon(a):return min(a,tuple(-x%4 for x in a))
M=sorted({canon((a,b,c,d)) for a in range(4) for b in range(4)
          for c in range(4) for d in range(4) if (a*d-b*c)%4==1})
MI=(1,0,0,1)
def mi(a):return canon((a[3],-a[1]%4,-a[2]%4,a[0]))
cyc3=sorted({tuple(sorted((MI,a,canon(mm(a,a))))) for a in M if a!=MI and canon(mm(mm(a,a),a))==MI})
assert len(cyc3)==4
mtop={}
for a in M:
    p=[]
    for C in cyc3:
        image=tuple(sorted(canon(mm(mm(a,c),mi(a))) for c in C))
        p.append(cyc3.index(image))
    mtop[a]=ind[tuple(p)]
assert len(set(mtop.values()))==24
for a in M:
    for b in M:assert mtop[canon(mm(a,b))]==mul[mtop[a]][mtop[b]]
s=mtop[canon((0,1,3,0))];r=mtop[canon((0,1,3,1))];ee=mul[s][r]
jx=mtop[(1,0,2,1)];jy=mtop[(1,2,0,1)]
phi_pair=(s,ee);phi_coord=pairclass[phi_pair]
ra,rb=reps[phi_coord]
transport=next(g for g in range(24) if conj(g,ra)==s and conj(g,rb)==ee)
phi=[conj(transport,v[phi_coord]) for v in H]
def j_eval(i):
    z=e
    if ab[i]&1:z=mul[z][jx]
    if ab[i]&2:z=mul[z][jy]
    return z
# Check both evaluations on every generator edge; this is essential.
for i,v in enumerate(H):
    for g,im,jim in ((X,s,jx),(Y,ee,jy)):
        k=index[tm(v,g)]
        assert phi[k]==mul[phi[i]][im]
        assert j_eval(k)==mul[j_eval(i)][jim]
print('two evaluations checked',round(time.time()-t0,2),flush=True)
xp=[tp(X,n) for n in range(12)];yp=[tp(Y,n) for n in range(12)];zp=[tp(Z,n) for n in range(12)]
def pp(a,n):
    z=e
    for _ in range(n%12):z=mul[z][a]
    return z
rows=[];counts=Counter()
for lam in (1,5,7,11,13,17,19,23):
    nu=(lam-1)//2
    for i,f in enumerate(H):
        if ab[i] or tm(f,H[theta[i]])!=E:continue
        val=E
        for a in (H[omega[omega[i]]],zp[nu],H[omega[i]],yp[nu],f,xp[nu]):val=tm(val,a)
        if val!=E:continue
        ax=xp[lam%12];ay=tm(tm(ti(f),yp[lam%12]),f)
        classes=[pairclass.get((a,b),-1) for a,b in zip(ax,ay)]
        if -1 in classes or len(set(classes))!=9:continue
        # A permutation of all epimorphism coordinates gives an actual
        # automorphism of H, rather than merely a generating pair in S4.
        gauges=[];defects=[]
        for t in range(12):
            xi=tm(tm(yp[(nu+t)%12],f),xp[-t%12]);k=index[xi]
            q=phi[k];rhs=mul[mul[mul[mul[q][s]][inv[q]]][inv[s]]][pp(jx,nu)]
            defects.append(perms[mul[inv[j_eval(k)]][rhs]])
            if j_eval(k)==rhs:gauges.append(t)
        counts[(lam,bool(gauges))]+=1
        rows.append(dict(multiplier_mod_24=lam,f_index=i,f=list(f),
                         compatible_gauges= gauges,defects=defects))
    print('lambda',lam,'counts',str({str(k):v for k,v in counts.items() if k[0]==lam}),flush=True)
out=dict(envelope_order=len(H),derived_order=ab.count(0),exponent=12,
         source_pair_orbits=[[list(perms[a]),list(perms[b])] for a,b in reps],
         total_cycle_automorphisms=len(rows),passing=sum(bool(row['compatible_gauges']) for row in rows),
         failing=sum(not row['compatible_gauges'] for row in rows),
         counts={str(k):v for k,v in counts.items()},
         interpretation='Necessary finite cycle solutions; full profinite extendability is not asserted.',
         solutions=rows,elapsed_seconds=round(time.time()-t0,2))
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('solutions','source_pair_orbits')},indent=2))
