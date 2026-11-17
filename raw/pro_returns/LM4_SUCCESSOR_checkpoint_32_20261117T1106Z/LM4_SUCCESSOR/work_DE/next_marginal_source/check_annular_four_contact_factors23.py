#!/usr/bin/env python3
"""Four prescribed actual source factors in the exact B112 infinite graph."""
from pathlib import Path
import json,hashlib
H=Path(__file__).resolve().parent
source=H/'annular_neck_reflection23.json';D=json.loads(source.read_text())
eta={int(j):tuple(w)for j,w in D['eta_adapted_K_basis_a_barb_d_e_f'].items()}
def inv(w):return tuple(-x for x in reversed(w))
def red(w):
 a=[]
 for x in w:
  if a and a[-1]==-x:a.pop()
  else:a.append(x)
 return tuple(a)
def sub(w,A):return red(x for z in w for x in(A[z]if z>0 else inv(A[-z])))
def U(name,n,bar=0):return(name,n,bar)
def K(n):return('k',n%2,0)
def flip(v):return K(v[1]+1)if v[0]=='k' else U(v[0],v[1],1-v[2])
def adjacent(v,w):
 if v==w:return False
 if v[0]=='k' and w[0]=='k':return False
 if v[0]=='k' or w[0]=='k':
  k,u=(v,w)if v[0]=='k'else(w,v)
  return k[1]==(u[1]+u[2])%2
 if v[0]==w[0] and v[1]==w[1] and v[2]!=w[2]:return True
 for n in {v[1],w[1]}:
  es=[(U('a',n),U('b',n)),(U('a',n,1),U('d',n)),(U('a',n,1),U('e',n)),(U('d',n),U('e',n,1)),
      (U('b',n),U('d',n+1)),(U('b',n),U('e',n+1))]
  es +=[(flip(a),flip(b))for a,b in es]
  if any((v==a and w==b)or(v==b and w==a)for a,b in es):return True
 return False
def reduce_graph(word):
 out=[];log=[]
 for v,sign in word:
  j=len(out)-1
  while j>=0 and adjacent(out[j][0],v):j-=1
  if j>=0 and out[j][0]==v and out[j][1]==-sign:
   # Exactly the intervening commuting suffix is passed, then inverse canceled.
   assert all(adjacent(v,x[0])for x in out[j+1:])
   log.append({'vertex':v,'passed':out[j+1:]});out.pop(j)
  else:out.append((v,sign))
 # No cancellable inverse pair can remain after moving through commuting letters.
 for i,(v,sign)in enumerate(out):
  for j in range(i+1,len(out)):
   if not adjacent(v,out[j][0]):
    assert not(out[j][0]==v and out[j][1]==-sign)
    break
 return out,log
def expand(w):
 level=0;out=[]
 for x in w:
  sign=1 if x>0 else -1;j=abs(x)
  if j==5:
   if sign>0:out.append((K(level+1),-1));level+=1
   else:out.append((K(level),1));level-=1
  else:
   nm,bar={1:('a',0),2:('b',1),3:('d',0),4:('e',0)}[j]
   out.append((U(nm,level,bar),sign))
 return out,level
seed={'eta(a_B_a^-1)':(1,2,-1),'eta(a)':(1,),
      'eta(a_d_a^-1)':(1,3,-1),'eta(a_e_a^-1)':(1,4,-1)}
rows=[]
for name,w in seed.items():
 value=sub(w,eta);raw,level=expand(value);assert level==0
 reduced,log=reduce_graph(raw)
 outside=sorted({v for v,s in reduced if v!=K(0)and not adjacent(K(0),v)})
 assert outside
 comm=[(K(0),1)]+reduced+[(K(0),-1)]+[(v,-s)for v,s in reversed(reduced)]
 cr,cl=reduce_graph(comm);assert cr
 rows.append({'name':name,'input_K_word':w,'actual_eta_K_word':value,'h_height':level,
  'raw_graph_word':raw,'reduced_graph_word':reduced,'cancellations':log,
  'vertices_outside_star_k0':outside,'commutator_reduced_graph_word':cr,'commutator_cancellations':cl})
# Exhaustively check symmetry on the finite vertex set touched by these FOUR words.
vertices={v for row in rows for v,s in row['raw_graph_word']}|{K(0),K(1)}
assert all(adjacent(v,w)==adjacent(w,v)for v in vertices for w in vertices)
assert all(adjacent(v,w)==adjacent(flip(v),flip(w))for v in vertices for w in vertices)
out={'status':'PASS_FOUR_NONCENTRAL_FACTORS_IN_ACTUAL_BAD_VERTEX','eta_input_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
 'normal_form_convention':'graph word followed by h^n; f=bar(k)^-1 h, f^-1=k h^-1',
 'actual_B112_graph':'all four infinite edge families, including barred and shifted edges',
 'rows':rows,'scope':'Exactly four prescribed factors, in the complete bad annular vertex before cross-relator quotient. No claim that these commutators survive in the actual one-neck quotient.'}
(H/'annular_four_contact_factors23.json').write_text(json.dumps(out,indent=2)+'\n')
for row in rows:print(row['name'],'outside star',row['vertices_outside_star_k0'],'reduced length',len(row['reduced_graph_word']))
print('PASS all four actual height-zero words have nonzero commutators with k0 in the complete B112 vertex')
print('No final one-neck quotient inference')
