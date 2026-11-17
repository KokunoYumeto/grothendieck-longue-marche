#!/usr/bin/env python3
"""Genuine128 physical-node face involution for the finite even model.

The existing raw orientations are retained: sign=-epsilon_nu*epsilon_mate.
Each coefficient is forced by a literal free-fiber physical-mate conjugacy,
is unique in G, squares correctly, and matches the entire21-edge boundary.
No arbitrary lift of F from C1 is used.
"""
from pathlib import Path
from collections import defaultdict
from functools import lru_cache
import json,hashlib,time

ROOT=Path(__file__).resolve().parents[2];P=ROOT/'work_CE/next_symmetric_nodes'
FULL=P/'actual_full21_Fox.json';FINITE=P/'finite_even_boundary32.json'
MATCH=P/'symmetric_F_node_matching.json'
D=json.loads(FULL.read_text());C=json.loads(FINITE.read_text());M=json.loads(MATCH.read_text())
T=[tuple(x) for x in D['retained_word_DAG']+C['retained_word_DAG_append']]
R=[tuple(x) for x in D['R_word_DAG']+C['R_word_DAG_append']]
gens=[None]+[tuple(x) for x in D['common_R_generators'][1:]+C['common_R_generators_append']]
G=[tuple(x) for x in D['group_elements']+C['group_elements_append']]
Tindex={(a,x):i for i,(a,x,n) in enumerate(T) if i}
Rindex={(a,x):i for i,(a,x,n) in enumerate(R) if i}
gen_index={x:i for i,x in enumerate(gens) if i};Gindex={x:i for i,x in enumerate(G)}
base_sizes={'T':len(T),'R':len(R),'R_generators':len(gens),'G':len(G)}
retained={j:i+1 for i,j in enumerate(D['retained_paired_indices'])}
beta={int(k):v[0] for k,v in D['retained_involution'].items()}
Fimages=next(m for m in D['matrices'] if m['family']=='involution')['literal_F21_images']


def red(w):
    out=[]
    for x in w:
        if out and out[-1]==-x:out.pop()
        else:out.append(x)
    return tuple(out)
def inv(w):return tuple(-x for x in reversed(w))
def Fword(w):return red(y for x in w for y in(Fimages[x-1] if x>0 else inv(Fimages[-x-1])))
def append(nodes,index,p,x):
    if p and nodes[p][1]==-x:return nodes[p][0]
    k=(p,x)
    if k not in index:index[k]=len(nodes);nodes.append((p,x,nodes[p][2]+1))
    return index[k]
def read(nodes,p):
    out=[]
    while p:p,x,n=nodes[p];out.append(x)
    return tuple(reversed(out))
def concat(nodes,index,a,b):
    for x in read(nodes,b):a=append(nodes,index,a,x)
    return a
def gen(t,i):
    k=(t,i)
    if k not in gen_index:gen_index[k]=len(gens);gens.append(k)
    return gen_index[k]
def group(g):
    if g not in Gindex:Gindex[g]=len(G);G.append(g)
    return Gindex[g]
@lru_cache(None)
def bet(t):
    out=0
    for x in read(T,t):out=append(T,Tindex,out,(1 if x>0 else-1)*beta[abs(x)])
    return out
def right(g,x):
    a,b,t=G[g];j=abs(x);s=1 if x>0 else-1
    if j in retained:return group((a,b,append(T,Tindex,t,s*retained[j])))
    if j<12:return group((append(R,Rindex,a,s*gen(t,j)),b,t))
    return group((a,append(R,Rindex,b,s*gen(bet(t),j-10)),t))
def evaluate(w):
    g=0
    for x in w:g=right(g,x)
    return g
@lru_cache(None)
def shift(t,a):
    out=0
    for x in read(R,a):
        h,i=gens[abs(x)];head=concat(T,Tindex,t,h)
        out=append(R,Rindex,out,(1 if x>0 else-1)*gen(head,i))
    return out
@lru_cache(None)
def multiply(a,b):
    u,v,t=G[a];x,y,s=G[b]
    return group((concat(R,Rindex,u,shift(t,x)),
                  concat(R,Rindex,v,shift(bet(t),y)),concat(T,Tindex,t,s)))
def Fgroup(g):
    a,b,t=G[g];return group((b,a,bet(t)))
def add(d,k,n):
    d[k]+=n
    if not d[k]:del d[k]
def peel(w):
    w=tuple(w);a=[]
    while len(w)>1 and w[0]==-w[-1]:a.append(w[0]);w=w[1:-1]
    return tuple(a),w
def conjugator(w,v):
    a,c=peel(w);b,d=peel(v)
    assert len(c)==len(d) and c
    for k in range(len(c)):
        if c[k:]+c[:k]==d:
            g=red(a+c[:k]+inv(b));assert red(g+tuple(v)+inv(g))==tuple(w)
            return g
    raise AssertionError('physical mate not freely conjugate')
def not_power(w):
    c=peel(w)[1]
    for k in range(1,len(c)):
        if len(c)%k==0:assert c!=c[:k]*(len(c)//k),'proper power'
    return len(c)


started=time.monotonic()
matching={tuple(r['node_index']):r for r in M['rows']}
node_faces={(f['sheet'],tuple(f['node_index'])):(i,f)
            for i,f in enumerate(C['faces']) if f['type']=='node'}
records=[]
for key,(face_index,node) in node_faces.items():
    sheet,index=key;match=matching[index];mate_index=tuple(match['physical_F_mate_index'])
    mate_face_index,mate=node_faces[sheet,mate_index]
    en,em=match['A_first_orientation_signs'];sign=-en*em
    r=tuple(node['literal_F21_word']);m=tuple(mate['literal_F21_word'])
    fr=Fword(r);target=m if sign>0 else inv(m)
    h=conjugator(fr,target);hG=evaluate(h)
    cyclic_length=not_power(m)
    # Evaluate the FULL left boundary by the actual F1 map.
    left=defaultdict(int)
    for row,g,sw,n in node['boundary32']:
        assert sw==0 and row<=21
        fg=Fgroup(g)
        if row==1:add(left,(1,right(fg,-1)), -n)
        else:
            assert len(Fimages[row-1])==1 and Fimages[row-1][0]>0
            add(left,(Fimages[row-1][0],fg),n)
    right_side=defaultdict(int)
    for row,g,sw,n in mate['boundary32']:
        assert sw==0
        add(right_side,(row,multiply(hG,g)),sign*n)
    assert dict(left)==dict(right_side),('entire F2 boundary comparison',key)
    records.append({'sheet':sheet,'node_index':index,'face_index':face_index,
      'mate_index':mate_index,'mate_face_index':mate_face_index,
      'physical_labels':match['physical_labels'],
      'A_first_orientation_signs':[en,em],'raw_cell_sign':sign,
      'literal_F21_conjugator':h,'coefficient_G_id':hG,
      'literal_word_identity':'F(r_nu)=h*r_mate^raw_cell_sign*h^-1',
      'literal_identity_verified':True,'mate_cyclic_length':cyclic_length,
      'mate_not_a_proper_power':True,'entire_boundary_equal':True,
      'F_boundary21':[[row,g,n] for(row,g),n in sorted(left.items())]})

by_key={(r['sheet'],tuple(r['node_index'])):r for r in records}
for r in records:
    mate=by_key[r['sheet'],tuple(r['mate_index'])]
    assert r['raw_cell_sign']*mate['raw_cell_sign']==1
    c=red(Fword(r['literal_F21_conjugator'])+tuple(mate['literal_F21_conjugator']))
    assert evaluate(c)==0
    assert multiply(Fgroup(r['coefficient_G_id']),mate['coefficient_G_id'])==0
    word=tuple(node_faces[r['sheet'],tuple(r['node_index'])][1]['literal_F21_word'])
    assert red(c+word+inv(c))==word
    r['double_F_conjugator_F21']=c
    r['double_F_coefficient_identity']=True
assert len(records)==128
out={'scope':__doc__,'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'input_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in(FULL,FINITE,MATCH)},
 'shared_G_base':str(FULL.relative_to(ROOT)),'shared_G_first_extension':str(FINITE.relative_to(ROOT)),
 'combined_G_base_sizes':base_sizes,
 'retained_word_DAG_append':T[base_sizes['T']:],
 'common_R_generators_append':gens[base_sizes['R_generators']:],
 'R_word_DAG_append':R[base_sizes['R']:], 'group_elements_append':G[base_sizes['G']:],
 'shared_DAG_semantics':'First concatenate FULL with FINITE append arrays, then append these arrays. All prior indices stay unchanged.',
 'geometric_provenance':'F fixes the q-whisker. The actual local node disk maps to its physical mate over the same critical disk. Its comparison is in the regular free fiber, crossing no other node disks. Literal free conjugators differ only by the non-power relator centralizer, which projects trivially to G.',
 'raw_orientation_convention':'The finite32 matrix uses raw paired_relator orientations, while physical matching was A-first. Therefore the cell coefficient sign is -epsilon_nu*epsilon_mate, not uniformly -1.',
 'records':records,'counts':{'node_faces':128,'fixed_physical_faces':sum(r['node_index']==r['mate_index'] for r in records),
 'positive_face_signs':sum(r['raw_cell_sign']==1 for r in records),
 'negative_face_signs':sum(r['raw_cell_sign']==-1 for r in records),
 'full_F_boundary_terms':sum(len(r['F_boundary21']) for r in records)},
 'claims_excluded':['arbitrary algebraic lift of F from C1','kappa vanishing or whole kernel computation'],
 'elapsed_seconds':time.monotonic()-started}
(P/'finite_even_node_F2.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
print('PASS all128 literal raw physical-mate identities and non-power checks')
print('PASS all128 entire F2 boundary identities and double-F coefficients')
print('COUNTS',out['counts'])
print('APPEND',len(T)-base_sizes['T'],len(R)-base_sizes['R'],len(G)-base_sizes['G'])
print('DONE elapsed',round(out['elapsed_seconds'],3))
