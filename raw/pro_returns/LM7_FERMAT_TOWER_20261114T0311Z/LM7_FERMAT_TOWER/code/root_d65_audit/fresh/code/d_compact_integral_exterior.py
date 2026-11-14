#!/usr/bin/env python3
"""Independent literal real-exterior check for the integral Hermitian model.

No field-action helper from the construction is imported. Matrices are
ordinary integer matrices modulo four on the basis (1,omega), with
omega squared equal to -1-omega. Every basis vector of the invariant
exterior summand is checked for every retained stabilizer element.
"""
from pathlib import Path
from itertools import combinations
import json,hashlib,time
import numpy as np
OUT=Path(__file__).resolve().parent;start=time.time()
paths=[OUT/'d_compact_integral.json',OUT/'d_arithmetic_A4_twisted.json']
Data,D=[json.loads(p.read_text()) for p in paths]
N=16;pairs=list(combinations(range(2*N),2));pi={p:i for i,p in enumerate(pairs)}
herm=[(i,i,1) for i in range(N)]+[(i,j,z) for i in range(N) for j in range(i+1,N) for z in [1,4]]
def coeff(a):return (a&3).astype(np.int64),(a>>2).astype(np.int64)
def mm(a,b):
 x,y=coeff(a);u,v=coeff(b)
 return ((x@u-y@v)%4+4*((x@v+y@u-y@v)%4)).astype(np.uint8)
def bar(a):
 x,y=coeff(a);return ((x-y)%4+4*((-y)%4)).astype(np.uint8)
def neg(a):
 x,y=coeff(a);return ((-x)%4+4*((-y)%4)).astype(np.uint8)
def real(a,flip=False):
 x,y=coeff(a);out=np.zeros((2*N,2*N),dtype=np.int64)
 out[0::2,0::2]=x;out[0::2,1::2]=-y
 out[1::2,0::2]=y;out[1::2,1::2]=x-y
 if flip:
  c=np.kron(np.eye(N,dtype=np.int64),np.array([[1,-1],[0,-1]],dtype=np.int64));out=out@c
 return out%4
def wedge(x,y):return np.array([(x[i]*y[j]-x[j]*y[i])%4 for i,j in pairs],dtype=np.int64)
def embed(a):
 x,y=coeff(a);out=np.zeros(len(pairs),dtype=np.int64)
 assert np.array_equal(a,bar(a.T)) and not np.any(y.diagonal())
 for i in range(N):out[pi[(2*i,2*i+1)]]=x[i,i]
 for i in range(N):
  for j in range(i+1,N):
   aa=x[i,j];bb=y[i,j]
   out[pi[(2*i,2*j+1)]]+=aa
   out[pi[(2*i+1,2*j)]]+=-aa+bb
   out[pi[(2*i,2*j)]]+=bb
   out[pi[(2*i+1,2*j+1)]]+=bb
 return out%4
basis=[];embedding=[]
for i,j,z in herm:
 a=np.zeros((N,N),dtype=np.uint8);a[i,j]=z;a[j,i]=bar(np.array(z,dtype=np.uint8))
 basis.append(a);embedding.append(embed(a))
embedding=np.array(embedding,dtype=np.int64).T
# Explicit coordinate left inverse proves this is a primitive rank256
# sublattice, and supplies exact decoding for every checked image.
def decode(w):
 a=np.zeros((N,N),dtype=np.uint8)
 for i in range(N):a[i,i]=w[pi[(2*i,2*i+1)]]%4
 for i in range(N):
  for j in range(i+1,N):
   aa=int(w[pi[(2*i,2*j+1)]]);bb=int(w[pi[(2*i,2*j)]])
   z=(aa%4)+4*(bb%4);a[i,j]=z;a[j,i]=bar(np.array(z,dtype=np.uint8))
 assert np.array_equal(embed(a),w%4);return a
assert all(np.array_equal(decode(v),a) for v,a in zip(embedding.T,basis))
scalar=np.eye(N,dtype=np.uint8)*4;sr=real(scalar);sr2=sr@sr%4
assert np.array_equal(sr2@sr%4,np.eye(2*N,dtype=np.int64))
scalar_projection_checked=0
for u,v in pairs:
 e=np.zeros(len(pairs),dtype=np.int64);e[pi[(u,v)]]=1
 projected=3*(e+wedge(sr[:,u],sr[:,v])+wedge(sr2[:,u],sr2[:,v]))%4
 decode(projected);scalar_projection_checked+=1
for b in basis:assert np.array_equal(mm(mm(scalar,b),bar(scalar.T)),b)
rows=[]
for rec in Data['cases']:
 B=next(b for b in D['character_blocks'] if b['character']==rec['character'])
 flips={a['q_state']:a['flip'] for a in B['all_stabilizer_actions']};checked=0
 for g,cols in rec['all_integral_complement_actions'].items():
  a=np.array(cols,dtype=np.uint8).T;flip=flips[int(g)];ar=real(a,flip)
  for k,b in enumerate(basis):
   image=np.zeros(len(pairs),dtype=np.int64)
   for j in np.flatnonzero(embedding[:,k]):
    u,v=pairs[int(j)];image+=embedding[j,k]*wedge(ar[:,u],ar[:,v])
   image%=4
   expected=mm(mm(a,bar(b) if flip else b),bar(a.T))
   if flip:expected=neg(expected)
   assert np.array_equal(image,embed(expected)) and np.array_equal(decode(image),expected)
   checked+=1
 row={'character':rec['character'],'stabilizer_elements':len(rec['all_integral_complement_actions']),
      'invariant_exterior_rank':256,'ambient_exterior_rank':len(pairs),
      'literal_basis_images_checked':checked,'signed_exchange_action_verified':True}
 rows.append(row);print(json.dumps(row),flush=True)
result={'summary':{'status':'PASS','primitive_embedding_and_exact_left_inverse_checked':True,'full_odd_scalar_projector_columns_checked':scalar_projection_checked,'elapsed_seconds':time.time()-start},
 'cases':rows,'input_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
(OUT/'d_compact_integral_exterior.json').write_text(json.dumps(result,separators=(',',':'))+'\n')
print(json.dumps(result['summary'],indent=2),flush=True)
