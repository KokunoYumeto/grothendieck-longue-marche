#!/usr/bin/env python3
"""Independent reconstruction of the entire actual finite annular neck input."""
from pathlib import Path
import json,hashlib
H=Path(__file__).resolve().parent;ROOT=H.parents[1];CE=ROOT/'work_CE/next_symmetric_nodes'
p=CE/'annular_neck_presentation23.json';d=json.loads(p.read_text())
src=json.loads((CE/'annular_source_detector_independent23.json').read_text())
e0=json.loads((H/'annular_neck_reflection23.json').read_text())
eta={int(j):tuple(w)for j,w in e0['eta_adapted_K_basis_a_barb_d_e_f'].items()}
def reduce(w,cones=()):
 s=[]
 for a in w:
  a=abs(a) if abs(a)in cones else a
  if s and(s[-1]==-a or a in cones and s[-1]==a):s.pop()
  else:s.append(a)
 return tuple(s)
def inverse(w):return tuple(-x for x in reversed(w))
def cat(*w):return reduce((x for v in w for x in v),(6,7))
def subst(w,A,cones=()):return reduce((z for x in w for z in(A[abs(x)]if x>0 else inverse(A[-x]))),cones)
def con(g,w):return cat(g,w,inverse(g))
def comm(g,w):return cat(g,w,inverse(g),inverse(w))
for j in range(1,6):assert subst(eta[j],eta)==(j,)
expected=[];maps={};sources=[]
for side,cc,kk,Z in[('minus',6,8,{j:(j,)for j in range(1,6)}),('plus',7,9,eta)]:
 a,B,dd,ee,f=[Z[j]for j in range(1,6)];C=(cc,);k=(kk,);b=con(C,B);h=cat(f,k)
 bar=lambda w:con(C,w)
 loc={1:a,2:b,3:C,4:f,5:dd,6:ee,7:h};maps[side]=loc
 assert [a,bar(b),dd,ee,f]==[Z[j]for j in range(1,6)]
 # The common edge relation is correct on all five generators in both directions.
 if side=='plus':assert all(subst(eta[j],Z,(6,7))==(j,)for j in range(1,6))
 rel=[comm(h,C),cat(con(h,k),inverse(bar(k)))]
 rel.extend(comm(k,x)for x in(a,b,dd,ee))
 rel.extend(comm(x,bar(x))for x in(a,b,dd,ee))
 rel.extend([comm(a,b),comm(bar(a),dd),comm(bar(a),ee),comm(dd,bar(ee)),comm(b,con(h,dd)),comm(b,con(h,ee))])
 assert len(rel)==16
 actual=[tuple(r['word'])for r in d['regional_relators']if r['side']==side]
 assert rel==actual
 expected+=rel
 if side=='plus':
  for row in src['source_reconstructed_from_original_positive_push']:
   sources.append(con(a,subst(tuple(row['Y_word']),loc,(6,7))))
  sources.append(con(a,h))
cminus=con((1,),(6,));cplus=con(eta[1],(7,))
cross=[comm(cplus,(8,)),comm(cminus,(9,))]
assert cross==[tuple(r['word'])for r in d['cross_relators']]
assert [list(cminus),list(cplus)]==[d['actual_gap_cones']['minus'],d['actual_gap_cones']['plus']]
sources.append((8,))
assert sources==[tuple(x['word'])for x in d['actual_six_source_words']]
assert d['cone_squares']==[[6,6],[7,7]] and d['total_relator_count_in_free_group']==36
assert d['total_generator_count']==9
base={j:()for j in range(1,10)};base[8]=(1,);base[9]=(2,)
for r in expected+cross:assert not subst(r,base)
assert [subst(w,base)for w in sources]==[(),(),(),(),(2,),(1,)]
height=lambda w:sum((-1 if x>0 else 1)for x in w if abs(x)==5)
assert all(height(w)==0 for w in expected+cross)
assert [height(w)for w in sources]==[0,0,0,0,1,0]
assert all(sum(abs(x)in(6,7)for x in w)%2==0 for w in sources)
# Invertible local substitutions: b=C B C, h=fk, and inverses B=C b C,k=f^-1h.
# Their group-theoretic equivalence is B112's actual annular presentation;
# no claim about reducing the final quotient follows from these reconstructions.
out={'status':'PASS','input_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
 'all_regional_relators_checked':32,'all_cross_relators_checked':2,'cone_squares_checked':2,
 'all_source_words_checked':6,'both_common_edge_directions_checked':True,
 'source_lengths':list(map(len,sources)),'scope':'Complete actual finite presentation and marked source input, not a quotient/centralizer solution.'}
(H/'annular_presentation_independent23.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS all32 regional relations, both cross relations and two cone squares')
print('PASS both literal common-K edge directions and all six whole-conjugated source words')
print('PASS every relation/source base image, parity and height; no final-quotient inference')
