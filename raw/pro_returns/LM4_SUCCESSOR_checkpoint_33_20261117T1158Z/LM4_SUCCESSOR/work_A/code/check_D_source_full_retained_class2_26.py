#!/usr/bin/env python3
"""One exact D-source test retaining all three retained mod-two coordinates.

The finite closure is the entire affine permutation orbit of the actual
40 node pairs, not a source-word-depth truncation.  No old evaluator is
imported.  Nonlinear source words are retained when evaluating the defect.
"""
from pathlib import Path
from collections import deque, defaultdict
import hashlib
import json

ROOT=Path(__file__).resolve().parents[2]
fp=ROOT/'work_CE/next_symmetric_nodes/family_kernel_schreier25.json'
sp=ROOT/'work_CE/next_symmetric_nodes/annular_two_operator25.json'
F=json.loads(fp.read_text()); S=json.loads(sp.read_text())
colors=(1,2,3,4,6,7,8,9)
ci={a:i for i,a in enumerate(colors)}
ret={5:0,10:1,11:2}

def red(w):
    ans=[]
    for a in w:
        if ans and ans[-1]==-a: ans.pop()
        else: ans.append(a)
    return ans
def inv(w): return [-a for a in w[::-1]]
def mul(*ws): return red(a for w in ws for a in w)
def sub(w,im): return mul(*(im[abs(a)] if a>0 else inv(im[abs(a)]) for a in w))
def bits3(w):
    out=0
    for a in w: out^=1<<(abs(a)-1)
    return out
def bits11(w):
    out=0
    for a in w:
        if abs(a) in ret: out^=1<<ret[abs(a)]
    return out
def vertex(i,t): return 8*ci[i]+t
def pair(a,b): return (a,b) if a<b else (b,a)

perms={}
for name,op in F['all_four_signed_source_operators'].items():
    linear=[bits3(op['retained_images'][str(i)]['retained_head']) for i in (5,10,11)]
    def act(t):
        ans=0
        for j in range(3):
            if t&(1<<j): ans^=linear[j]
        return ans
    p=list(range(64))
    for i in colors:
        r=op['family_images'][str(i)]
        assert r['signed_core']==i
        h=bits3(r['retained_head'])
        for t in range(8): p[vertex(i,t)]=vertex(i,act(t)^h)
    assert sorted(p)==list(range(64))
    perms[name]=p
for name in ('m','v'):
    p=perms[name];q=perms[name+'_inverse']
    assert all(p[q[i]]==q[p[i]]==i for i in range(64))
for j in range(3):
    perms['deck_'+str(j)]=[vertex(i,t^(1<<j)) for i in colors for t in range(8)]

seeds=[]
for row in F['all40_node_factor_pairs']:
    a,b=row['first_factor'],row['second_factor']
    va=vertex(abs(a['signed_core']),bits3(a['retained_head']))
    vb=vertex(abs(b['signed_core']),bits3(b['retained_head']))
    assert va!=vb
    seeds.append(pair(va,vb))
assert len(seeds)==40
edges=set(seeds); todo=deque(sorted(edges)); parents={p:None for p in edges}
while todo:
    a,b=todo.popleft()
    for name,p in perms.items():
        q=pair(p[a],p[b])
        if q not in edges:
            edges.add(q);todo.append(q);parents[q]=[name,[a,b]]
assert all(pair(p[a],p[b]) in edges for a,b in edges for p in perms.values())

def scan(word):
    """Literal F11 word in the free fiber of F64 semidirect (C2)^3."""
    t=0;out=[]
    for a in word:
        if abs(a) in ret: t^=1<<ret[abs(a)]
        else: out.append((vertex(abs(a),t),1 if a>0 else -1))
    assert t==0
    return out
def degree2(word):
    v=defaultdict(int);q=defaultdict(int)
    for i,sign in scan(word):
        for j,n in tuple(v.items()):
            if n:q[j,i]+=sign*n
        if sign==-1:q[i,i]+=1
        v[i]+=sign
    v={i:n for i,n in v.items() if n}
    q={ij:n for ij,n in q.items() if n}
    if not v:
        assert all(i!=j and q.get((j,i),0)==-n for (i,j),n in q.items())
    surviving={(i,j):n for (i,j),n in q.items() if i<j and (i,j) not in edges}
    return v,q,surviving

raw=[r['fiber11'] for r in S['actual_six_source_normal_forms'][:4]]
Ds=mul(raw[1],raw[0],inv(raw[2]),inv(raw[0]),inv(raw[1]))
Us=mul(raw[0],inv(raw[3]),inv(raw[0]))
results=[]
for label,w in [('D_s',Ds),('U_known',Us)]:
    for name in ('m','m_inverse'):
        im={int(k):v for k,v in S['source_ordinary_actions'][name].items()}
        defect=mul(sub(w,im),inv(w))
        ab,q,surv=degree2(defect)
        assert not ab,(label,name,'unexpected nonzero abelian defect',ab)
        if label=='U_known':assert not surv,(name,surv)
        row={'word':label,'operator':name,'defect_F11':defect,
             'raw_length':len(defect),'abelian_defect':ab,
             'all_degree2_upper_coordinates':[[i,j,n] for (i,j),n in sorted(q.items()) if i<j],
             'surviving_upper_coordinates':[[i,j,n] for (i,j),n in sorted(surv.items())]}
        results.append(row)
        print(label,name,'raw length',len(defect),'degree2 upper',sum(i<j for i,j in q),'surviving',len(surv))

out={'status':'EXACT_ONE_TARGET_COMPLETE','inputs':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (fp,sp)},
     'vertices':[{'id':vertex(i,t),'color_F11':i,'retained_bits_f_g_x':[(t>>j)&1 for j in range(3)]} for i in colors for t in range(8)],
     'all_seven_permutations':perms,'forty_seed_pairs':seeds,'complete_allowed_pairs':sorted(edges),
     'orbit_parent_certificate':[{'pair':p,'parent':parents[p]} for p in sorted(edges)],
     'results':results,
     'scope':'One complete finite retained-residue orbit quotient of the actual class-two family kernel. All source-word and deck orbits are included by exact permutation closure. Whole F11 source words are evaluated; no source action on the free-fiber target is presumed. A zero result is no actual commutation assertion.'}
(ROOT/'work_A/D_source_full_retained_class2_26.json').write_text(json.dumps(out,indent=2)+'\n')
print('Complete allowed edge orbit:',len(edges),'of',64*63//2,'unordered pairs.')
print('Signed source/deck invariance and inverse permutations PASS.')
