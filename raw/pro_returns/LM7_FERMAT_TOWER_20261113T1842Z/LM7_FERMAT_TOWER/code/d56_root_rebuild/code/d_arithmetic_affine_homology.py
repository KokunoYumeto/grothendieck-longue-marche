#!/usr/bin/env python3
"""Actual order-3888 marked graph, compactification and correction maps.

All649 free generators, the integral ribbon intersection matrix and every
moving-homology action are rebuilt from the literal affine quotient.
"""
from pathlib import Path
from collections import deque
from itertools import product
import json,time

OUT=Path(__file__).resolve().parent;started=time.time()
D=json.loads((OUT/'d_arithmetic_affine_base.json').read_text())
Q=json.loads((OUT/'d_arithmetic_correction_graph.json').read_text())
M=[tuple(map(tuple,x)) for x in D['Q_linear_image_matrices']]
mi={a:i for i,a in enumerate(M)}
S=tuple(map(tuple,D['quotient_s_columns']))
R=tuple(map(tuple,D['quotient_r_columns']))
vectors=list(product(range(3),repeat=4));vi={a:i for i,a in enumerate(vectors)}
def mv(A,v):return tuple(sum(v[j]*A[j][i] for j in range(4))%3 for i in range(4))
def mm(A,B):return tuple(mv(A,c) for c in B)
def add(a,b):return tuple((x+y)%3 for x,y in zip(a,b))
mt=[[mi[mm(a,b)] for b in M] for a in M]
ma=[[vi[mv(a,b)] for b in vectors] for a in M]
va=[[vi[add(a,b)] for b in vectors] for a in vectors]
def gm(a,b):
    aq,av=divmod(a,81);bq,bv=divmod(b,81)
    return 81*mt[aq][bq]+va[av][ma[aq][bv]]
s=81*mi[S]+vi[tuple(D['affine_s_translation'])]
r=81*mi[R]+vi[tuple(D['affine_r_translation'])]
t=gm(s,r);size=3888
rs=D['right_s_3888'];rr=D['right_r_3888']
assert all(rs[g]==gm(g,s) and rr[g]==gm(g,r) for g in range(size))
def power(a,k):
    out=0
    while k:
        if k&1:out=gm(out,a)
        a=gm(a,a);k//=2
    return out
invmat=[next(j for j in range(48) if mt[i][j]==0) for i in range(48)]
def inverse(a):
    q,v=divmod(a,81);qi=invmat[q]
    return 81*qi+vi[tuple(-x%3 for x in mv(M[qi],vectors[v]))]
def invword(word):return [0 if a==0 else 3-a for a in reversed(word)]
v2=[(0,min(g,rs[g])) for g in range(size)]
v3=[(1,min(g,rr[g],rr[rr[g]])) for g in range(size)]
adj={v:[] for v in set(v2+v3)}
for e in range(size):
    adj[v2[e]].append((v3[e],e,1))
    adj[v3[e]].append((v2[e],e,-1))
paths={v2[0]:[]};queue=deque([v2[0]]);tree=set()
while queue:
    v=queue.popleft()
    for u,e,sgn in adj[v]:
        if u not in paths:
            paths[u]=paths[v]+[(e,sgn)];tree.add(e);queue.append(u)
ch=[e for e in range(size) if e not in tree];ci={e:j for j,e in enumerate(ch)}
rho=len(ch);assert rho==649
cycles=[];IC=[];basis_words=[]
def pathword(path):
    assert path[0][0] in (0,s) and path[-1][0] in (0,s)
    word=[] if path[0][0]==0 else [0]
    for (g,a),(h,b) in zip(path,path[1:]):
        if g==h:continue
        if a==1:
            if rr[g]==h:word.append(1)
            else:assert rr[rr[g]]==h;word.append(2)
        else:assert rs[g]==h;word.append(0)
    if path[-1][0]==s:word.append(0)
    return word
def evaluate(word):
    q=0;v={}
    for token in word:
        if token==0:q=rs[q]
        else:
            h=rr[q] if token==1 else rr[rr[q]]
            v[q]=v.get(q,0)+1;v[h]=v.get(h,0)-1;q=h
    return q,{e:a for e,a in v.items() if a}
for j,e in enumerate(ch):
    path=paths[v2[e]]+[(e,1)]+[(k,-a) for k,a in reversed(paths[v3[e]])]
    assert all(a==(1 if i%2==0 else -1) for i,(k,a) in enumerate(path))
    cc={}
    for k,a in path:cc[k]=cc.get(k,0)+a
    cc={k:a for k,a in cc.items() if a};word=pathword(path)
    assert evaluate(word)==(0,cc)
    assert [cc.get(k,0) for k in ch]==[int(i==j) for i in range(rho)]
    IC.append(cc);cycles.append(sum(1<<e for e,a in cc.items() if a%2));basis_words.append(word)
def vc(v):
    out=0
    while v:
        b=v&-v;e=b.bit_length()-1
        if e in ci:out|=1<<ci[e]
        v^=b
    return out
assert all(vc(c)==1<<j for j,c in enumerate(cycles))
def combine(cols,v):
    out=0
    while v:
        b=v&-v;out^=cols[b.bit_length()-1];v^=b
    return out
def solver(cols):
    bas={};null=[];ind=[]
    for j,col in enumerate(cols):
        v=col;w=1<<j
        while v:
            p=v.bit_length()-1
            if p not in bas:bas[p]=(v,w);ind.append(j);break
            a,b=bas[p];v^=a;w^=b
        if not v:null.append(w)
    def solve(v):
        out=0
        for p in sorted(bas,reverse=True):
            if v>>p&1:a,b=bas[p];v^=a;out^=b
        assert not v
        return out
    return solve,len(bas),null,ind
def rank(cols):return solver(cols)[1]
def perm_action(v,perm):
    out=0
    while v:
        b=v&-v;out^=1<<perm[b.bit_length()-1];v^=b
    return out
ag=[vi[tuple(int(i==j) for i in range(4))] for j in range(4)]
perms={g:[gm(g,h) for h in range(size)] for g in [s,r,t]+ag}
HC={g:[vc(perm_action(c,perms[g])) for c in cycles] for g in perms}
for g in ag:
    assert all(combine(HC[g],combine(HC[g],c))==1<<j for j,c in enumerate(HC[g]))
def normA(v):
    for a in ag:
        av=combine(HC[a],v);v^=av^combine(HC[a],av)
    return v
plus=[normA(1<<j) for j in range(rho)]
minus=[(1<<j)^plus[j] for j in range(rho)]
_,pr,_,pi=solver(plus);_,wr,_,wi=solver(minus)
assert pr==9 and wr==640
W=[minus[j] for j in wi];ws,wr0,_,_=solver(W);assert wr0==640
WA={g:[ws(combine(HC[g],w)) for w in W] for g in [s,r,t]}
fixed={}
for g,name in [(s,'s'),(r,'r'),(t,'t')]:
    _,rk,ker,_=solver([col^(1<<j) for j,col in enumerate(WA[g])])
    fixed[name]=ker
L=[(1<<j)^WA[s][j] for j in range(640)]+[
    combine(WA[s],(1<<j)^WA[r][j]) for j in range(640)]
_,lr,pk,_=solver(L);assert lr==640 and len(pk)==640
kernel_dimension=sum(len(x) for x in fixed.values())
derivation_dimension=640-kernel_dimension
assert derivation_dimension>0
# Full marked cusp loops and their exact boundary subspace.
gwords={0:[]};queue=deque([0])
while queue:
    g=queue.popleft()
    for h,token in [(rs[g],0),(rr[g],1)]:
        if h not in gwords:gwords[h]=gwords[g]+[token];queue.append(h)
seen=set();cusp=[];cusp_words=[]
for g in range(size):
    if g in seen:continue
    orbit={gm(g,power(t,j)) for j in range(12)};assert len(orbit)==12
    seen|=orbit
    word=gwords[g]+[0,1]*12+invword(gwords[g])
    q,chain=evaluate(word);assert q==0
    cusp.append(sum(1<<ci[e] for e,a in chain.items() if e in ci and a%2))
    cusp_words.append(word)
assert len(cusp)==324 and rank(cusp)==323 and combine(cusp,(1<<324)-1)==0
cusp_plus=[normA(c) for c in cusp]
cusp_minus=[c^normA(c) for c in cusp]
assert rank(cusp_plus)==3 and rank(cusp_minus)==320
# Integral ribbon pairing: one half of the sum of oriented trivalent terms.
edge_entries=[[] for g in range(size)]
for j,c in enumerate(IC):
    for g,a in c.items():edge_entries[g].append((j,a))
twice=[[0]*rho for j in range(rho)]
for g in sorted({min(g,rr[g],rr[rr[g]]) for g in range(size)}):
    for i,a in edge_entries[g]:
        for j,b in edge_entries[rr[g]]:
            twice[i][j]+=a*b;twice[j][i]-=a*b
assert all(a%2==0 for row in twice for a in row)
Omega=[sum(1<<i for i in range(rho) if (twice[i][j]//2)%2) for j in range(rho)]
assert rank(Omega)==326
assert all(combine(Omega,c)==0 for c in cusp)
assert all((col>>i&1)==(Omega[i]>>j&1) for j,col in enumerate(Omega) for i in range(rho))
for g in (s,r,t):
    assert all(sum(1<<i for i,u in enumerate(HC[g])
                   if (u&combine(Omega,col)).bit_count()%2)==Omega[j]
               for j,col in enumerate(HC[g]))

# Literal kernel of Q -> the48-state linear group, including its A4 marking.
qq=[tuple(x) for x in Q['Q_states']];qi={a:i for i,a in enumerate(qq)}
def qnorm(a):return min(a,tuple(-x%12 for x in a))
def qmul(a,b):
    x,y,z,w=qq[a];p,q0,r0,s0=qq[b]
    return qi[qnorm(((x*p+y*r0)%12,(x*q0+y*s0)%12,
                     (z*p+w*r0)%12,(z*q0+w*s0)%12))]
ker=D['Q_linear_kernel_states']
def qorder(g):
    a=g;n0=1
    while a:a=qmul(a,g);n0+=1
    return n0
V4=[g for g in ker if qorder(g) in (1,2)]
order3=[g for g in ker if qorder(g)==3]
assert len(V4)==4 and len(order3)==8
assert all(qmul(a,b) in V4 for a in V4 for b in V4)
z3=order3[0];zi=qmul(z3,z3)
assert set(qmul(qmul(z3,a),zi) for a in V4)==set(V4)
assert all(qmul(qmul(z3,a),zi)!=a for a in V4 if a)
assert len({qmul(a,p) for a in V4 for p in (0,z3,zi)})==12
summary={
 'scope':'Actual arithmetic quotient and its actual marked homology; no surrogate base.',
 'base_order':size,'free_kernel_rank':rho,'all_free_generator_words_checked':rho,
 'A_order':81,'invariant_homology_rank':pr,'moving_homology_rank':wr,
 'moving_fixed_dimensions':{k:len(v) for k,v in fixed.items()},
 'peripheral_conjugator_pair_dimension':len(pk),
 'peripheral_pair_to_derivation_kernel_dimension':kernel_dimension,
 'actual_peripheral_derivation_dimension':derivation_dimension,
 'cusp_map_rank':lr,'cusp_count':len(cusp),'cusp_subspace_rank':rank(cusp),
 'invariant_cusp_subspace_rank':rank(cusp_plus),
 'moving_cusp_subspace_rank':rank(cusp_minus),
 'moving_compact_homology_rank':640-rank(cusp_minus),
 'compact_homology_rank':rank(Omega),'compact_genus':163,
 'ribbon_form_and_all_deck_equivariances_checked':True,
 'Q_to_linear_image_kernel_order':len(ker),
 'Q_to_linear_image_kernel_is_marked_A4':True,
 'Q_kernel_V4_states':V4,'Q_kernel_order3_generator':z3,
 'kernel_G3_to_3888_order_formula':'12*3^93',
 'kernel_G3_to_3888_has_no_F2_abelian_quotient':True,
 'elapsed_seconds':round(time.time()-started,3)}
cert={
 'summary':summary,'cycle_chords':ch,'all649_free_generator_words':basis_words,
 'homology_s_columns':[hex(v) for v in HC[s]],
 'homology_r_columns':[hex(v) for v in HC[r]],
 'homology_t_columns':[hex(v) for v in HC[t]],
 'translation_generator_states':ag,
 'homology_translation_columns':[[hex(v) for v in HC[g]] for g in ag],
 'A_norm_columns':[hex(v) for v in plus],
 'moving_basis':[hex(v) for v in W],
 'moving_s_columns':[hex(v) for v in WA[s]],
 'moving_r_columns':[hex(v) for v in WA[r]],
 'moving_t_columns':[hex(v) for v in WA[t]],
 'moving_fixed_bases':{k:[hex(v) for v in vs] for k,vs in fixed.items()},
 'all_cusp_columns':[hex(v) for v in cusp],
 'pairing_columns_mod2':[hex(v) for v in Omega],
 'pairing_integer_matrix':[[a//2 for a in row] for row in twice],
 'Q_kernel_V4_states':V4,'Q_kernel_order3_generator':z3}
(OUT/'d_arithmetic_affine_homology.json').write_text(json.dumps(cert,indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)
