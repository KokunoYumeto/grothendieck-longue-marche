#!/usr/bin/env python3
"""Exhaustive 432-element local mixed target, with literal normal forms.
Independent of GAP: enumerate matrix words, construct the Heisenberg
kernel and an actual commuting order-four complement, and check all
normal-form multiplication and conjugation rules.
"""
import numpy as np,json,itertools
from pathlib import Path
D=Path(__file__).parent;F=np.load(D/'local_mixed_quaternion_census.npz');dd,vv=F['mixed_matrices'].astype(np.int16);I=np.eye(52,dtype=np.int16)
def mul(A,B):return A@B%3
def pw(A,k):
 O=I.copy()
 for _ in range(k):O=mul(O,A)
 return O
def key(A):return A.astype(np.uint8).tobytes()
G=[I];gi={key(I):0};words=[()];ab=[(0,0)];edges=[]
for i,M in enumerate(G):
 row=[]
 for j,A in enumerate((dd,vv)):
  N=mul(M,A);k=key(N);lab=list(ab[i]);lab[j]=(lab[j]+1)%4;lab=tuple(lab)
  if k not in gi:gi[k]=len(G);G.append(N);words.append(words[i]+(j+1,));ab.append(lab)
  z=gi[k];assert ab[z]==lab;row.append(z)
 edges.append(row)
assert len(G)==432
nid=[i for i,a in enumerate(ab) if a==(0,0)];assert len(nid)==27
inv=[]
for i,M in enumerate(G):
 N=I.copy()
 for j in reversed(words[i]):N=mul(N,pw((dd,vv)[j-1],3))
 assert np.array_equal(mul(M,N),I) and np.array_equal(mul(N,M),I);inv.append(N)
def comm(A,B):
 ai=gi[key(A)];bi=gi[key(B)];return mul(mul(mul(A,B),inv[ai]),inv[bi])
for i in nid:assert np.array_equal(pw(G[i],3),I)
x=y=z=None
for i in nid:
 for j in nid:
  C=comm(G[i],G[j])
  if not np.array_equal(C,I):x,y,z=G[i],G[j],C;break
 if x is not None:break
assert x is not None
nforms={};nidx={}
for i,j,k in itertools.product(range(3),repeat=3):
 A=mul(mul(pw(x,i),pw(y,j)),pw(z,k));nforms[i,j,k]=A;nidx[key(A)]=(i,j,k)
assert len(nidx)==27 and set(nidx)=={key(G[i]) for i in nid}
for i in nid:assert np.array_equal(comm(G[i],z),I)
for a,A in nforms.items():
 for b,B in nforms.items():
  expected=((a[0]+b[0])%3,(a[1]+b[1])%3,(a[2]+b[2]-a[1]*b[0])%3)
  assert np.array_equal(mul(A,B),nforms[expected])
# A Sylow-two complement containing the actual first generator D.
u=dd;vi=next(i for i,a in enumerate(ab) if a==(0,1) and np.array_equal(pw(G[i],4),I) and np.array_equal(comm(u,G[i]),I));v=G[vi]
comp={(p,q):mul(pw(u,p),pw(v,q)) for p,q in itertools.product(range(4),repeat=2)}
assert len({key(M) for M in comp.values()})==16
coords={}
for a,A in nforms.items():
 for b,B in comp.items():
  k=key(mul(A,B));assert k not in coords;coords[k]=a+b
assert len(coords)==432 and set(coords)==set(gi)
act={}
for name,A in [('u',u),('v',v)]:
 ai=gi[key(A)];act[name]=[nidx[key(mul(mul(A,B),inv[ai]))] for B in (x,y,z)]
central=[i for i,M in enumerate(G) if np.array_equal(comm(M,dd),I) and np.array_equal(comm(M,vv),I)]
assert len(central)==12
Z={key(G[i]) for i in central};normal_z=pw(mul(dd,vv),2);assert gi[key(normal_z)] in central
assert np.array_equal(pw(normal_z,6),I) and not np.array_equal(pw(normal_z,3),I) and not np.array_equal(pw(normal_z,2),I)
# The center quotient's 36 actual cosets and exact generator transitions.
cosets=[];cidx={}
for i,M in enumerate(G):
 if i in cidx:continue
 cset={gi[key(mul(M,G[j]))] for j in central};k=len(cosets)
 for t in cset:cidx[t]=k
 cosets.append(sorted(cset))
assert len(cosets)==36
qedges=[]
for C in cosets:
 row=[]
 for j in range(2):
  vals={cidx[edges[i][j]] for i in C};assert len(vals)==1;row.append(vals.pop())
 qedges.append(row)
# Exact cusp swap D<->V descends, checked on every Cayley edge.
swap=[]
for w in words:
 i=0
 for j in w:i=edges[i][2-j]
 swap.append(i)
assert sorted(swap)==list(range(432)) and all(swap[swap[i]]==i for i in range(432))
for i in range(432):
 for j in range(2):assert swap[edges[i][j]]==edges[swap[i]][1-j]
swapN=[coords[key(G[swap[gi[key(A)]]])] for A in (x,y,z)]
assert [v[:2] for v in swapN[:2]]==[(2,0),(0,2)]
# Every source group element acts as a permutation on the conjugacy class D.
conjugates={};conj_labels=[]
for i,M in enumerate(G):
 A=mul(mul(M,dd),inv[i]);k=key(A)
 if k not in conjugates:conjugates[k]=len(conjugates)
 conj_labels.append(conjugates[k])
centralizer_d=[i for i,k in enumerate(conj_labels) if k==0]
# Since the first element is I, label zero is exactly the original D.
assert len(centralizer_d)*len(conjugates)==432
# All original d,V and both exact f evaluation pairs in normal coordinates.
evals=[(dd,pw(vv,2)),(pw(dd,2),vv)]
print('PASS exhaustive432 matrices, actual Heisenberg27 normal forms and all729 multiplication rules',flush=True)
print('PASS actual C4xC4 complement; normal form of D,V:',coords[key(dd)],coords[key(vv)],flush=True)
print('PASS complement actions on x,y,z:',act,flush=True)
print('PASS center12, z=(DV)^2 order6, center quotient36, conjugacy class D size',len(conjugates),flush=True)
print('PASS actual cusp swap on all432 Cayley vertices; normal generator images:',swapN,flush=True)
print('PASS exact f-evaluation pairs:',[[coords[key(A)],coords[key(B)]] for A,B in evals],flush=True)
np.savez_compressed(Path(__file__).with_suffix('.npz'),all_group_matrices=np.array(G),generator_edges=np.array(edges),abelian_labels=np.array(ab),
 normal_generators=np.array([x,y,z]),complement_generators=np.array([u,v]),center_indices=np.array(central),center_quotient_edges=np.array(qedges))
Path(__file__).with_suffix('.json').write_text(json.dumps({'scope':'Exhaustive actual local mixed image and exact normal-form isomorphism, including both ABR.4 evaluations',
 'order':432,'matrix_dimension':52,'generator_words':words,'all_normal_coordinates':[coords[key(A)] for A in G],'generator_edges':edges,'abelian_labels':ab,
 'normal_generator_words':[words[gi[key(A)]] for A in (x,y,z)],'complement_generator_words':[words[gi[key(A)]] for A in (u,v)],
 'normal_form_law':'(i,j,k)*(i2,j2,k2)=(i+i2,j+j2,k+k2-j*i2) modulo3',
 'complement_action':act,'source_generator_normal_forms':[coords[key(A)] for A in (dd,vv)],
 'central_z_normal_form':coords[key(normal_z)],'center_indices':central,'center_quotient_cosets':cosets,'center_quotient_edges':qedges,
 'D_conjugacy_class_size':len(conjugates),'D_centralizer_size':len(centralizer_d),'D_centralizer_indices':centralizer_d,
 'cusp_swap_permutation':swap,'cusp_swap_normal_generator_images':swapN,
 'finite_f_evaluation_normal_forms':[[coords[key(A)],coords[key(B)]] for A,B in evals]},indent=2)+'\n')
