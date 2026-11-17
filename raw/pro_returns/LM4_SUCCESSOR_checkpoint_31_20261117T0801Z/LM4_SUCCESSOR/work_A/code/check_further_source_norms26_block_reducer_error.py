#!/usr/bin/env python3
"""Two specified actual regional norm tests in the proved infinite graph model.

No finite level truncation, quotient oracle or earlier evaluator is imported.
The model itself is the two-sided B112 graph presentation, not inferred here.
"""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
source=ROOT/'work_DE/next_marginal_source/annular_neck_reflection23.json'
data=json.loads(source.read_text())
def inv(w):return tuple(-i for i in reversed(w))
def red(w):
 out=[]
 for i in w:
  i=3 if abs(i)==3 else i
  if out and (out[-1]==-i or out[-1]==i==3):out.pop()
  else:out.append(i)
 return tuple(out)
def mul(*ws):return red(i for w in ws for i in w)
def sub(w,images):return mul(*(images[abs(i)] if i>0 else inv(images[abs(i)]) for i in w))
def conj(g,w):return mul(g,w,inv(g))
def comm(a,b):return mul(a,b,inv(a),inv(b))
def bar(w):return conj((3,),w)
# Y=(a,b,C,f,d,e), h=7,k=8; common K=(a,B,d,e,f).
K_to_Y={1:(1,),2:(3,2,3),3:(5,),4:(6,),5:(4,)}
eta={int(i):tuple(w) for i,w in data['eta_adapted_K_basis_a_barb_d_e_f'].items()}
def vertex(v,height,parity):
 fam,n,bit=v
 return (fam,0,bit^(height%2)^parity) if fam=='k' else (fam,n+height,bit^parity)
def commute(v,w):
 if v==w:return True
 f,n,b=v;g,m,c=w
 if f==g=='k':return False
 if f=='k':return b==((m%2)^c)
 if g=='k':return c==((n%2)^b)
 if f==g and n==m and b!=c:return True
 if n==m:
  p=frozenset((f,g))
  if p==frozenset(('a','b')):return b==c
  if p in (frozenset(('a','d')),frozenset(('a','e')),frozenset(('d','e'))):return b!=c
 if f=='b' and g in ('d','e') and m==n+1:return b==c
 if g=='b' and f in ('d','e') and n==m+1:return b==c
 return False
def graph_reduce(word):
 w=list(word)
 while True:
  removed=False
  for i,(v,s) in enumerate(w):
   for j in range(i+1,len(w)):
    u,t=w[j]
    if v==u and s==-t:
     del w[j];del w[i];removed=True;break
    if not commute(v,u):break
   if removed:break
  if not removed:return tuple(w)
def evaluate(word):
 expanded=[]
 for i in word:
  expanded.extend((7,-8) if i==4 else (8,-7) if i==-4 else (i,))
 h=c=0;out=[]
 names={1:'a',2:'b',5:'d',6:'e'}
 for i in expanded:
  if abs(i)==3:c^=1
  elif abs(i)==7:h+=1 if i>0 else -1
  else:
   v=('k',0,0) if abs(i)==8 else (names[abs(i)],0,0)
   out.append((vertex(v,h,c),1 if i>0 else -1))
 return graph_reduce(out),h,c
def diagonal(i):return mul((i,),bar((i,)))
# Detector-inverse source map: a->delta_a, B->delta_b, d/e->their diagonals, f->h.
source_map={1:diagonal(1),2:diagonal(2),3:diagonal(5),4:diagonal(6),5:(7,)}
rows=[]
for name,i in [('a',1),('d',3),('e',4)]:
 # Relative to the selected outer gap A, w=A^-1 eta(i) A.
 wK=tuple([-1,*eta[i],1])
 wY=sub(wK,K_to_Y)
 norm=mul(wY,bar(wY))
 test=comm(wY,bar(wY))
 value=evaluate(test)
 expected=sub(wK,source_map)
 comparison=evaluate(mul(norm,inv(expected)))
 rows.append({'common_generator':name,'outer_gap_rebased_K_word':wK,'rebased_Y_word':wY,
              'norm_Y_word':norm,'commutation_graph_normal_form':value,
              'is_fixed_in_actual_plus_regional_group':value==((),0,0),
              'predicted_source_Y_word':expected,'source_comparison_graph_normal_form':comparison,
              'equals_source_prediction':comparison==((),0,0)})
 print(name,'commutator graph length',len(value[0]),'fixed',value==((),0,0),'source comparison length',len(comparison[0]),'equal',comparison==((),0,0))
 if value!=((),0,0):print('nonempty complete graph word',value)
assert rows[0]['is_fixed_in_actual_plus_regional_group'] and rows[0]['equals_source_prediction']
out={'status':'EXACT_SPECIFIED_NORM_TESTS_COMPLETE','input':str(source.relative_to(ROOT)),'input_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'rows':rows,'scope':'Exact complete regional graph model only; a nonzero regional result is not a post-cross nonmembership assertion because regional survival is unproved.'}
(ROOT/'work_A/further_source_norms26.json').write_text(json.dumps(out,indent=2)+'\n')

# Explicit small full-subgraph projections, preserving the complete regional words.
def free_target(w):
 out=[]
 for j in w:
  if out and out[-1]==-j:out.pop()
  else:out.append(j)
 return tuple(out)
projections=[]
for row in rows[1:]:
 name=row['common_generator'];fam,n=('d',0) if name=='d' else ('e',2)
 kept=[('b',0,1),(fam,n,0),(fam,n,1)]
 assert not commute(kept[0],kept[1]) and not commute(kept[0],kept[2]) and commute(kept[1],kept[2])
 # First retain Z(B)*Z²(U,bar U); then identify U,bar U to the same free letterY.
 mp={kept[0]:1,kept[1]:2,kept[2]:2}
 def project(word):
  graph,h,c=evaluate(word);assert h==c==0
  return free_target(sign*mp[v] for v,sign in graph if v in mp)
 wy=tuple(row['rebased_Y_word']);left=project(wy);right=project(bar(wy))
 assert left==(1,-2,-1) and right==(-2,)
 comm_image=free_target((*left,*tuple(-j for j in reversed(right)),)) if False else free_target((*left,*right,*tuple(-j for j in reversed(left)),*tuple(-j for j in reversed(right))))
 assert comm_image==(1,-2,-1,-2,1,2,-1,2)
 projections.append({'name':name,'kept_vertices':kept,'projected_w':left,'projected_bar_w':right,'nonzero_free_commutator':comm_image})
 print(name,'exact coordinate free quotient gives',left,right,'and nonzero length8 commutator',comm_image)
out['small_coordinate_quotients']=projections
# The four complete inner k-centralizing neck generators, in the actual outer selected gauge.
neck_blocks={'a':(1,),'d':(3,),'e':(4,),'f_inverse_B_f':(-5,2,5)}
block=[]
# Keep B_0, d_0,bar d_0 distinctly, yielding Z*Z² rather than its free quotient.
keep3={('b',0,1):1,('d',0,0):2,('d',0,1):3}
def project3(word):
 graph,h,c=evaluate(word);assert h==c==0
 return tuple(sign*keep3[v] for v,sign in graph if v in keep3)
for label,vK in neck_blocks.items():
 iv=sub(vK,eta);rebased=mul((-1,),iv,(1,));wy=sub(rebased,K_to_Y)
 entry={'label':label,'rebased_K_word':rebased,'unbar_projection':project3(wy),'bar_projection':project3(bar(wy))}
 block.append(entry);print('inner block projection',entry)
out['d_three_vertex_projection_of_whole_k_neck_block']=block
(ROOT/'work_A/further_source_norms26.json').write_text(json.dumps(out,indent=2)+'\n')
