#!/usr/bin/env python3
"""Actual full two-annulus/one-neck finite presentation and marked source.
No quotient solver or finite census: all maps are explicit Tietze substitutions.
"""
from pathlib import Path
from fractions import Fraction as Q
import json,hashlib
ROOT=Path(__file__).resolve().parents[2];CE=ROOT/'work_CE/next_symmetric_nodes';DE=ROOT/'work_DE/next_marginal_source'
files=[DE/'annular_neck_reflection23.json',DE/'annular_neck_bridge23.json',CE/'annular_source_detector_independent23.json',CE/'annular_upper_gap_cone23.json']
R,B,S,G=[json.loads(p.read_text()) for p in files]
def red(w,cones=()):
 o=[]
 for x in w:
  if abs(x)in cones:x=abs(x)
  if o and(o[-1]==-x or x in cones and o[-1]==x):o.pop()
  else:o.append(x)
 return tuple(o)
def inv(w,cones=()):return red((-x for x in reversed(w)),cones)
def mul(*words,cones=()):return red((x for w in words for x in w),cones)
def sub(w,A,cones=()):return red((z for x in w for z in(A[abs(x)] if x>0 else inv(A[-x],cones))),cones)
def comm(u,v,cones=()):return mul(u,v,inv(u,cones),inv(v,cones),cones=cones)
#Independent literal left-base reflection calibration using actual xi polygons.
pts=[Q(x) for x in R['xi_punctures']]
def cut_read(poly):
 out=[]
 for a,b in zip(poly,poly[1:]):
  dx,dy=b[0]-a[0],b[1]-a[1];hits=[]
  for j,p in enumerate(pts,1):
   for z in(a,b):assert z[0]!=p or z[1]>0
   if dx:
    t=(p-a[0])/dx
    if 0<=t<=1:assert a[1]+t*dy!=0
    if 0<t<1 and a[1]+t*dy<0:hits.append((t,j if dx>0 else -j))
  hits.sort();out.extend(j for _,j in hits)
 return red(out)
etaO={int(j):tuple(w) for j,w in R['eta_ordinary_cuts'].items()}
for j,raw in enumerate(R['xi_paths'],1):
 poly=[tuple(map(Q,z)) for z in raw]
 assert cut_read(poly)==(j,)
 assert cut_read([(x,-y) for x,y in poly])==etaO[j]
 prefix=tuple(range(1,j));assert etaO[j]==prefix+(-j,)+inv(prefix)
#Both literal O/K Nielsen directions, typed from displayed actual table.
OinK={1:(1,2,-1),2:(1,),3:(5,3,4,-3,-5),4:(3,),5:(-3,5,3)}
KinO={1:(2,),2:(-2,1,2),3:(4,),4:(-5,-4,3,4,5),5:(4,5,-4)}
for j in range(1,6):
 assert sub(OinK[j],KinO)==(j,)
 assert sub(KinO[j],OinK)==(j,)
eta={j:sub(sub(KinO[j],etaO),OinK) for j in range(1,6)}
assert eta=={int(j):tuple(w) for j,w in R['eta_adapted_K_basis_a_barb_d_e_f'].items()}
for j in range(1,6):assert sub(eta[j],eta)==(j,)
#Actual bridge ordinary-system comparison, not merely permutation labels.
push={int(j):tuple(w)for j,w in B['positive_push'].items()};back={int(j):tuple(w)for j,w in B['back_transport'].items()}
for j in range(1,7):assert sub(push[j],back)==sub(back[j],push)==(j,)
assert [push[j]for j in(1,3,4,5,6)]==[(j,)for j in(1,2,4,5,6)]
assert G['upper_cone_in_Y']==[1,3,-1]
#GLOBAL labels:1 a,2 B=bar b,3 d,4 e,5 f,6 Cminus,7 Cplus,8 kminus,9 kplus.
cones=(6,7)
def cn(w):return red(w,cones)
def cm(*ws):return mul(*ws,cones=cones)
def ci(w):return inv(w,cones)
def cc(u,v):return comm(u,v,cones)
def conj(g,w):return cm(g,w,ci(g))
regional=[];localmaps={};source=[]
for side,C,k,Z in [('minus',(6,),(8,),{j:(j,)for j in range(1,6)}),('plus',(7,),(9,),eta)]:
 a,Bb,d,e,f=[Z[j]for j in range(1,6)];b=conj(C,Bb);h=cm(f,k)
 loc={1:a,2:b,3:C,4:f,5:d,6:e,7:h};localmaps[side]=loc
 bar=lambda u:conj(C,u)
 rels=[('h_fixes_cone',cc(h,C)),('h_swaps_k',cm(conj(h,k),ci(bar(k))))]
 rels += [('k_fixes_'+nm,cc(k,u))for nm,u in [('a',a),('b',b),('d',d),('e',e)]]
 rels += [('diagonal_'+nm,cc(u,bar(u)))for nm,u in [('a',a),('b',b),('d',d),('e',e)]]
 rels += [('pair_ab',cc(a,b)),('pair_bara_d',cc(bar(a),d)),('pair_bara_e',cc(bar(a),e)),('pair_d_bare',cc(d,bar(e))),('pair_b_hdh',cc(b,conj(h,d))),('pair_b_heh',cc(b,conj(h,e)))]
 assert len(rels)==16
 regional.extend({'side':side,'name':nm,'word':w}for nm,w in rels)
 if side=='plus':
  #Raw actual four source words, reconstructed independently from original positive lassos.
  gap=a
  for row in S['source_reconstructed_from_original_positive_push']:
   w=conj(gap,sub(tuple(row['Y_word']),loc,cones))
   source.append({'name':row['name'],'word':w,'raw_Y_word':row['Y_word']})
  source.append({'name':'outer_annular_source','word':conj(gap,h)})
cmn=conj((1,),(6,));cpl=conj(eta[1],(7,))
cross=[{'name':'opposite_cone_inner_loop','word':cc(cpl,(8,))},{'name':'opposite_cone_outer_loop','word':cc(cmn,(9,))}]
source.append({'name':'inner_good_source','word':(8,)})
rels=regional+cross
assert len(rels)==34 and len(source)==6
#Actual projection to F2 of geometric annular base loops; both cone/edge systems lie in fiber.
base={j:()for j in range(1,10)};base[8]=(1,);base[9]=(2,)
for r in rels:assert sub(r['word'],base)==()
for row in source:row['base_F2_image']=sub(row['word'],base)
assert [r['base_F2_image']for r in source]==[(),(),(),(),(2,),(1,)]
#Compatible source unfolding height: common f has -1, all other global generators0.
height={j:0 for j in range(1,10)};height[5]=-1
def ht(w):return sum((1 if j>0 else -1)*height[abs(j)]for j in w)
for r in rels:assert ht(r['word'])==0
assert [ht(r['word'])for r in source]==[0,0,0,0,1,0]
for row in source:
 assert sum(abs(j)in cones for j in row['word'])%2==0
 row['unfolding_height']=ht(row['word'])
#The source conjugacy table from B112 is retained separately from its literal raw representatives.
loc=localmaps['plus'];a,b,C,f,d,e,h=[loc[j]for j in range(1,8)]
delta=lambda u:cm(u,C,u,C)
da,db,dd,de=map(delta,[a,b,d,e]);prefix=cm(db,h,dd)
simple=[db,conj(prefix,de),dd,da,h]
simple=[conj(a,w)for w in simple]
#No arbitrary quotient-normal-form equality is asserted by this producer:
#raw-to-simple equality is precisely the already proved B112 regional source theorem.
out={'status':'PASS_ACTUAL_FINITE_PRESENTATION_AND_SOURCE','input_hashes':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()for p in files},
 'generators':{'1':'a','2':'B=bar_b','3':'d','4':'e','5':'f','6':'Cminus','7':'Cplus','8':'kminus','9':'kplus'},
 'base_free_product':'F7(a,B,d,e,f,kminus,kplus) * C2(Cminus) * C2(Cplus)',
 'eta_in_common_K':eta,'local_Y_h_maps':localmaps,
 'cone_squares':[[6,6],[7,7]],'regional_relators':regional,'cross_relators':cross,
 'total_generator_count':9,'total_relator_count_in_free_group':36,
 'actual_gap_cones':{'minus':cmn,'plus':cpl},'actual_six_source_words':source,
 'B112_simplified_outer_five_source_words':simple,
 'source_word_lengths':[len(s['word'])for s in source],
 'projections':{'geometric_base_F2':base,'source_unfolding_height':height},
 'scope':'Whole actual two-annuli/one-neck presentation, via invertible regional/common-K substitutions and categorical gluing. No source injectivity, quotient centralizer, additional-neck or main conclusion.'}
(CE/'annular_neck_presentation23.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS all five literal reflected xi polygons; actual bridge and ten K inverse substitutions')
print('PASS actual eta involution and all five common-K images')
print('PASS complete 9-generator /36-relator actual one-neck presentation')
print('PASS all six actual source words, lengths',out['source_word_lengths'])
print('PASS geometric F2, parity and compatible height checks on every relation/source')
