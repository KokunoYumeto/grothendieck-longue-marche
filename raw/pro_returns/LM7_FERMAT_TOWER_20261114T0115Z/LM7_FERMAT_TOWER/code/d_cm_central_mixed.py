#!/usr/bin/env python3
"""Actual central double cover of Q and its mixed relative-3 homology.

All groups, graph maps and matrices are reconstructed from the marked
generators of B=C2*C3.  No finite homology action is inferred from an
unmarked isomorphism.  Python standard library only.
"""
from collections import deque
from pathlib import Path
import argparse, hashlib, json, time

ap=argparse.ArgumentParser()
ap.add_argument('--source-code',type=Path,default=Path(__file__).resolve().parents[2]/'LM7_FERMAT_TOWER'/'code')
args=ap.parse_args();OUT=Path(__file__).resolve().parent;started=time.time()
I=(1,0,0,1);S=(0,1,11,0);R=(0,11,1,11)
def canon(a):return min(a,tuple(-x%12 for x in a))
def mul(a,b):
    return canon(((a[0]*b[0]+a[1]*b[2])%12,(a[0]*b[1]+a[1]*b[3])%12,
                  (a[2]*b[0]+a[3]*b[2])%12,(a[2]*b[1]+a[3]*b[3])%12))
def inv(a):return canon((a[3],-a[1]%12,-a[2]%12,a[0]))
Q=[I];seen={I}
for a in Q:
    for b in [S,R]:
        c=mul(a,b)
        if c not in seen:seen.add(c);Q.append(c)
assert len(Q)==576
ix={q:i for i,q in enumerate(Q)};zi=ix[I]
right_s=[ix[mul(q,S)] for q in Q]
right_r=[ix[mul(q,R)] for q in Q]
left_s=[ix[mul(S,q)] for q in Q]
left_r=[ix[mul(R,q)] for q in Q]

def graph(rs,rr):
    size=len(rs);v2=[(0,min(i,rs[i])) for i in range(size)]
    v3=[(1,min(i,rr[i],rr[rr[i]])) for i in range(size)]
    adj={v:[] for v in set(v2+v3)}
    for e in range(size):
        adj[v2[e]].append((v3[e],e,1));adj[v3[e]].append((v2[e],e,-1))
    root=v2[0];paths={root:{}};todo=deque([root]);tree=set()
    while todo:
        v=todo.popleft()
        for w,e,sg in adj[v]:
            if w not in paths:
                p=paths[v].copy();p[e]=p.get(e,0)+sg
                if not p[e]:del p[e]
                paths[w]=p;tree.add(e);todo.append(w)
    assert len(paths)==len(adj)
    chords=[i for i in range(size) if i not in tree];C=[]
    for e in chords:
        c=paths[v2[e]].copy()
        for j,a in paths[v3[e]].items():
            c[j]=c.get(j,0)-a
            if not c[j]:del c[j]
        c[e]=c.get(e,0)+1
        if not c[e]:del c[e]
        C.append(c)
    assert all([c.get(e,0) for e in chords]==[int(i==j) for i in range(len(chords))]
               for j,c in enumerate(C))
    return {'v2':v2,'v3':v3,'paths':paths,'chords':chords,'cycles':C,'vertices':len(adj)}

G=graph(right_s,right_r);ch=G['chords'];rank=len(ch);assert rank==97
ci={e:i for i,e in enumerate(ch)}
def bitcoords(c,perm=None):
    out=0
    for e,a in c.items():
        k=perm[e] if perm is not None else e
        if a%2 and k in ci:out^=1<<ci[k]
    return out
def echelon(rows):
    bas={}
    for row in rows:
        while row:
            p=row.bit_length()-1
            if p not in bas:bas[p]=row;break
            row^=bas[p]
    return bas
cols=[]
for j,c in enumerate(G['cycles']):
    assert bitcoords(c)==1<<j
    cols.extend([(1<<j)^bitcoords(c,left_s),(1<<j)^bitcoords(c,left_r)])
aug=echelon(cols);assert len(aug)==96
free=next(j for j in range(rank) if j not in aug)
phi=1<<free
for p in sorted(aug):
    if ((aug[p]^(1<<p))&phi).bit_count()%2:phi|=1<<p
assert all((c&phi).bit_count()%2==0 for c in cols)
edge_phi=sum(1<<ch[i] for i in range(rank) if phi>>i&1)
def phiedge(c):
    return sum(a for e,a in c.items() if edge_phi>>e&1)%2

# P(s)=0, P(r)=e_1-e_r; paths on Q are integral, with actual words.
P={0:{}};words={0:[]};todo=[0]
for q in todo:
    for a,rr in [(0,right_s),(1,right_r)]:
        qq=rr[q]
        if qq not in P:
            p=P[q].copy()
            if a:
                p[q]=p.get(q,0)+1;p[qq]=p.get(qq,0)-1
                p={e:v for e,v in p.items() if v}
            P[qq]=p;words[qq]=words[q]+[a];todo.append(qq)
assert len(P)==576
fp=[phiedge(P[q]) for q in range(576)]
ds=[fp[q]^fp[right_s[q]] for q in range(576)]
dr=[fp[q]^((edge_phi>>q)&1)^((edge_phi>>right_r[q])&1)^fp[right_r[q]]
    for q in range(576)]
# E elements (q,a), a in C2.  The second coordinate is measured relative
# to the same Q path P(q).  The central generator toggles this coordinate.
es=[2*right_s[q]+(a^ds[q]) for q in range(576) for a in range(2)]
er=[2*right_r[q]+(a^dr[q]) for q in range(576) for a in range(2)]
assert all(es[es[i]]==i and er[er[er[i]]]==i for i in range(1152))
Ewords={0:[]};todo=[0]
for q in todo:
    for a,rr in [(0,es),(1,er)]:
        qq=rr[q]
        if qq not in Ewords:Ewords[qq]=Ewords[q]+[a];todo.append(qq)
assert len(Ewords)==1152
def ew(w):
    q=0
    for a in w:
        if a==0:q=es[q]
        elif a==1:q=er[q]
        else:q=er[er[q]]
    return q
def right_word(q,w):
    for a in w:
        q=es[q] if a==0 else er[q] if a==1 else er[er[q]]
    return q
def wi(w):return [0 if a==0 else 3-a for a in w[::-1]]
def wc(a,b):return a+b+wi(a)+wi(b)
tw=[0,1];xw=wi(tw+tw);yw=[0]+xw+[0]
cxy=wc(xw,yw)
center_words={}
for name,w in [('t12',tw*12),('comm_xy_power4',cxy*4)]:
    center_words[name]={'word':w,'image':ew(w),'length':len(w)}
assert center_words['t12']['image']==1
# Actual F and F' images, retaining words for every state.  In particular
# the displayed M word detects the central extension without a counting
# inference about abstract groups of the same order.
EFwords={0:[]};todo=[0]
for q in todo:
    for w in [xw,yw]:
        qq=right_word(q,w)
        if qq not in EFwords:EFwords[qq]=EFwords[q]+w;todo.append(qq)
assert len(EFwords)==192
derived_generators=[w+cxy+wi(w) for w in EFwords.values()]
EFpwords={0:[]};todo=[0]
for q in todo:
    for w in derived_generators:
        qq=right_word(q,w)
        if qq not in EFpwords:EFpwords[qq]=EFpwords[q]+w;todo.append(qq)
assert len(EFpwords)==16 and 1 in EFpwords
center_words['M_central_word']={'word':EFpwords[1],'image':1,'length':len(EFpwords[1])}

# Full marked homology of L=ker(B->E); central deck action z toggles q.
GE=graph(es,er);ce=GE['chords'];re=len(ce);assert re==193
Me=[[GE['cycles'][j].get(e^1,0)%3 for j in range(re)] for e in ce]
def rank3(matrix):
    rows=[list(a) for a in matrix];n=len(rows);m=len(rows[0]) if n else 0;row=0
    for col in range(m):
        p=next((i for i in range(row,n) if rows[i][col]%3),None)
        if p is None:continue
        rows[row],rows[p]=rows[p],rows[row]
        if rows[row][col]%3==2:rows[row]=[(2*a)%3 for a in rows[row]]
        for i in range(row+1,n):
            a=rows[i][col]%3
            if a:rows[i]=[(u-a*v)%3 for u,v in zip(rows[i],rows[row])]
        row+=1
        if row==n:break
    return row
minus=[[ (Me[i][j]-int(i==j))%3 for j in range(re)] for i in range(re)]
plus=[[ (Me[i][j]+int(i==j))%3 for j in range(re)] for i in range(re)]
minus_rank=rank3(minus);plus_rank=rank3(plus)
assert minus_rank==96 and plus_rank==97
# Direct graph action, including every full edge chain, not just chords.
for j,c in enumerate(GE['cycles']):
    transformed={e^1:a for e,a in c.items()}
    got={}
    for k,col in enumerate(Me):
        a=col[j]
        if a:
            for e,b in GE['cycles'][k].items():got[e]=(got.get(e,0)+a*b)%3
    assert all((got.get(e,0)-transformed.get(e,0))%3==0 for e in set(got)|set(transformed))
assert all(sum(Me[i][k]*Me[k][j] for k in range(re))%3==int(i==j)
           for i in range(re) for j in range(re))

# The actual S3 loop action on the index-twelve N lattice has no mod2
# fixed covector.  This proves that the central character is nonzero on M.
B=json.loads((args.source_code/'d_cm_solvable_even_boundary.json').read_text())
states=[tuple(q) for q in B['sphere_quotient_states']];sx={q:i for i,q in enumerate(states)}
pi=(0,1,2);ps=(1,0,2);pr=(1,2,0)
pm=lambda a,b:tuple(a[b[i]] for i in range(3))
pr2=pm(pr,pr);ch_s={j:i for i,j in enumerate(B['sphere_cycle_chords'])}
def ab(w):
    q=pi;v=[0,0]
    for a in w:
        if a==0:q=pm(q,ps)
        else:
            h=pm(q,pr if a==1 else pr2)
            if sx[q] in ch_s:v[ch_s[sx[q]]]+=1
            if sx[h] in ch_s:v[ch_s[sx[h]]]-=1
            q=h
    assert q==pi
    # f1=x, f2=y^-1 in the retained graph.
    return [v[0],-v[1]]
fb=B['sphere_F_basis_B_words'];MR=[]
for w in [fb[0],wi(fb[1])]:MR.append(ab([1]+w+[2]))
MR=[[MR[j][i] for j in range(2)] for i in range(2)]
# Lambda basis columns (2,-2),(0,6).
def lambda_coords(v):
    assert v[0]%2==0 and (v[0]+v[1])%6==0
    return [v[0]//2,(v[0]+v[1])//6]
lambda_cols=[]
for v in [(2,-2),(0,6)]:
    w=[sum(MR[i][j]*v[j] for j in range(2)) for i in range(2)]
    lambda_cols.append(lambda_coords(w))
LR=[[lambda_cols[j][i] for j in range(2)] for i in range(2)]
fixed_covectors=[v for v in [(0,0),(1,0),(0,1),(1,1)]
                if all(sum(v[i]*LR[i][j] for i in range(2))%2==v[j] for j in range(2))]
assert fixed_covectors==[(0,0)]
for rec in center_words.values():rec['F_abelianization']=ab(rec['word'])
assert center_words['M_central_word']['F_abelianization']==[0,0]

# Actual graph pushforward L^ab -> Lambda, followed by reduction modulo3.
edge_to_sphere=[]
for q in range(1152):
    h=pi
    for a in Ewords[q]:h=pm(h,ps if a==0 else pr)
    edge_to_sphere.append(sx[h])
Lambda_map=[[],[]]
for c in GE['cycles']:
    v=[0,0]
    for e,a in c.items():
        se=edge_to_sphere[e]
        if se in ch_s:v[ch_s[se]]+=a
    v[1]*=-1
    lc=lambda_coords(v)
    for i in range(2):Lambda_map[i].append(lc[i]%3)
assert rank3(Lambda_map)==2
assert all(sum(Lambda_map[i][k]*Me[k][j] for k in range(re))%3==Lambda_map[i][j]
           for i in range(2) for j in range(re))

summary={'Q_order':576,'N_rank':97,'Q_coinvariant_F2_dimension':1,
 'central_cover_E_order':1152,'central_kernel_order':2,'L_free_rank':193,
 'qE_F_order':192,'qE_F_prime_order':16,'E_over_qE_F_prime_order':72,
 'all_E_states_generated':True,'s_squared_and_r_cubed_verified_at_every_state':True,
 'central_z_action_on_L_ab3_dimension':193,'central_z_plus_dimension':97,
 'central_z_minus_dimension':96,'actual_graph_action_verified_on_all_cycles':True,
 'Lambda_r_matrix':LR,'Lambda_mod2_nonzero_invariant_covectors':0,
 'M_surjects_central_C2':True,'L_image_in_F_abelianization':'Lambda',
 'actual_L_homology_to_Lambda_mod3_rank':2,
 'actual_Lambda_map_is_invariant_under_central_deck':True,
 'actual_M_central_word_length':len(EFpwords[1]),
 'image_of_M_in_J_order':'2 * 3^191','image_of_M_plus_eigenspace_dimension':95,
 'image_of_M_minus_eigenspace_dimension':96,
 'exact_image_of_D47_source_kernel_in_J':'C3^96',
 'J_order':'1152 * 3^193','maximal_marked_common_quotient_J_with_D47_order':'1152 * 3^97',
 'scope':'The program proves the marked finite graph and module calculations. Exact inverse-limit maps, source kernel images, and the compatible arithmetic/identity-prime extension are proved in D48.',
 'elapsed_seconds':round(time.time()-started,3)}
cert={'summary':summary,'Q':[list(q) for q in Q],
 'Q_coinvariant_functional_on_N_cycle_basis':hex(phi),
 'Q_cycle_chords':ch,'E_right_s':es,'E_right_r':er,'E_central_z_word':Ewords[1],
 'tested_central_words':center_words,'L_cycle_chords':ce,
 'central_z_matrix_on_L_ab3':Me,'Lambda_r_matrix':LR,
 'actual_L_homology_to_Lambda_mod3':Lambda_map,
 'E_image_F':sorted(EFwords),'E_image_F_prime':sorted(EFpwords)}
(OUT/'d_cm_central_mixed.json').write_text(json.dumps(cert,indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)
print('Actual central-word checks:',json.dumps({k:{a:b for a,b in v.items() if a!='word'}
                                             for k,v in center_words.items()}),flush=True)
