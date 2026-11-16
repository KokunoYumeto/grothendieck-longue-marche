#!/usr/bin/env python3
"""Replay the actual finite359-face matrix, without importing its producer."""
from pathlib import Path
from collections import defaultdict
import json,hashlib,time
H=Path(__file__).resolve().parent;ROOT=H.parents[1];P=ROOT/'work_CE/next_symmetric_nodes'
path=P/'finite_even_boundary32.json';d=json.loads(path.read_text())
full=json.loads((P/'actual_full21_Fox.json').read_text())
odd=json.loads((P/'full21_opposite_sheet_nodes.json').read_text());start=time.monotonic()
for name,h in d['input_sha256'].items():assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==h
T=[tuple(x) for x in full['retained_word_DAG']+d['retained_word_DAG_append']]
R=[tuple(x) for x in full['R_word_DAG']+d['R_word_DAG_append']]
gens=[None]+[tuple(x) for x in full['common_R_generators'][1:]+d['common_R_generators_append']]
GG=[tuple(x) for x in full['group_elements']+d['group_elements_append']]
def validate(nodes,bound):
    assert nodes[0]==(0,0,0);idx={}
    for i,(p,x,l) in enumerate(nodes[1:],1):
        assert 0<=p<i and 0<abs(x)<bound and nodes[p][2]+1==l
        assert not p or nodes[p][1]!=-x
        assert (p,x) not in idx;idx[p,x]=i
    return idx
TI=validate(T,6);RI=validate(R,len(gens));GI={}
for i,(t,j) in enumerate(gens[1:],1):
    assert 0<=t<len(T) and j in (2,3,5,6,7,8,10,11) and (t,j) not in GI
    GI[t,j]=i
Gid={g:i for i,g in enumerate(GG)};assert len(Gid)==len(GG) and GG[0]==(0,0,0)
for a,b,t in GG:assert 0<=a<len(R) and 0<=b<len(R) and 0<=t<len(T)
def read(nodes,p):
    ans=[]
    while p:p,x,l=nodes[p];ans.append(x)
    return tuple(reversed(ans))
def put(nodes,idx,p,x):return nodes[p][0] if p and nodes[p][1]==-x else idx[p,x]
def locate(nodes,idx,w):
    p=0
    for x in w:p=put(nodes,idx,p,x)
    return p
beta={int(k):v[0] for k,v in full['retained_involution'].items()}
betac={0:0}
def bt(t):
    if t not in betac:betac[t]=locate(T,TI,((1 if x>0 else -1)*beta[abs(x)] for x in read(T,t)))
    return betac[t]
ret={j:i+1 for i,j in enumerate(full['retained_paired_indices'])}
def advance(g,x):
    a,b,t=GG[g];j=abs(x);s=1 if x>0 else -1
    if j in ret:t=put(T,TI,t,s*ret[j])
    elif j<12:a=put(R,RI,a,s*GI[t,j])
    else:b=put(R,RI,b,s*GI[bt(t),j-10])
    return Gid[a,b,t]
def evaluate(w):
    g=0
    for x in w:g=advance(g,x)
    return g
def add(out,k,n):
    out[k]+=n
    if not out[k]:del out[k]
def unpack(rows):
    out={}
    for j,g,s,n in rows:
        assert 1<=j<=32 and 0<=g<len(GG) and 0<=s<=11 and n and (j,g,s) not in out
        out[j,g,s]=n
    return out
source=[m for m in full['matrices'] if m['family']=='source' and m['direction']=='push']
assert [x['name'] for x in d['source_generators']]==[x['name'] for x in source]
assert d['source_word_table']==[[]]+[[-i] for i in range(1,12)]
assert len(source)==11
def bdy(c):
    out=defaultdict(int)
    for (j,g,s),n in c.items():
        if j<=21:
            if s==0:end=(advance(g,j),0)
            else:
                assert g==0
                end=(source[s-1]['generator_images_G'][j-1],s)
        else:
            assert s==j-21 and s
            end=(g,0)
        add(out,end,n);add(out,(g,s),-n)
    return dict(out)
f0={tuple(x['node_index']):x for x in full['node_cycles']}
f1={tuple(x['node_index']):x for x in odd['columns']}
oi={int(k):GI[locate(T,TI,v['retained_word']),v['paired_slot']] for k,v in odd['common_R_basis'].items()}
def orword(w):return locate(R,RI,((1 if x>0 else -1)*oi[abs(x)] for x in w))
checks=[]
for face in d['faces']:
    c=unpack(face['boundary32']);want=defaultdict(int)
    if face['type']=='source_rectangle':
        si=face['source_index'];j=face['paired_generator'];m=source[si-1]
        assert face['source_name']==m['name']
        for row,g,n in m['columns'][j-1]:add(want,(row,g,0),-n)
        add(want,(j,0,si),1)
        add(want,(21+si,m['generator_images_G'][j-1],si),1)
        add(want,(21+si,0,si),-1)
        label=['source',si,j]
    else:
        ix=tuple(face['node_index']);sheet=face['sheet'];n=(f0 if sheet==0 else f1)[ix]
        assert face['literal_F21_word']==n['literal_F21_word'] and evaluate(face['literal_F21_word'])==0
        if sheet==0:
            for row,g,coef in n['full21_cycle']:add(want,(row,g,0),coef)
        else:
            for row in n['full21_cycle']:
                h=row['G_coefficient'];g=Gid[orword(h['A_word']),orword(h['B_word']),locate(T,TI,h['retained_word'])]
                add(want,(row['row'],g,0),row['coefficient'])
        label=['node',sheet,*ix]
    assert c==dict(want) and not bdy(c),label
    checks.append({'face':label,'terms':len(c),'entire_column_and_next_boundary':True})
assert len(checks)==359
F=next(m for m in full['matrices'] if m['family']=='involution')['literal_F21_images']
Fchecks=[]
for a in d['source_face_F']:
    si=a['source_index'];j=a['paired_generator'];m=source[si-1]
    if j==1:
        w=m['literal_F21_images'][0];iw=[-x for x in reversed(w)]
        fw=[(1 if x>0 else -1)*F[abs(x)-1][0] for x in w]
        assert fw==iw
        assert a['target_paired_generator']==1 and a['sign']==-1 and a['coefficient_G_id']==evaluate(iw)
        # Actual word identity F(AB^-1)=B^-1(AB^-1)^-1B,
        # A=s^-1p1s, B=psi(p1), supplies the genuine rectangle map.
    else:assert a['target_paired_generator']==F[j-1][0] and a['sign']==1 and a['coefficient_G_id']==0
    Fchecks.append([si,j])
assert len(Fchecks)==231
assert sum(x['terms'] for x in checks)==319438
out={'input_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
     'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'canonical_all_appended_DAGs':True,'faces':checks,'source_F2_checks':Fchecks,
     'counts':d['counts'],'entire_next_boundary_checked':True,
     'F2_scope':'All231 actual cylinder coefficients independently checked against literal source words. Physical node-face equivariance comes from the actual geometric relative model, not an arbitrary lift of this matrix.',
     'claims_excluded':['kernel finiteness','kappa vanishing','CW type from relators alone'],
     'elapsed_seconds':time.monotonic()-start}
(H/'finite_even_boundary32_independent_review.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS all359 complete columns,319438 terms and next-boundaries; all231 genuine cylinder F coefficients')
print('COUNTS',d['counts'],'elapsed',round(out['elapsed_seconds'],3))
