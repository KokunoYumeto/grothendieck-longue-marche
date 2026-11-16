#!/usr/bin/env python3
"""Actual16-row cycle coordinates and exact vertex Tate extraction.

All64 prescribed node words are compared with their previously audited
square boundaries. Four actual source anti-chains calibrate the extractor.
No CE producing module, large rectangle expansion or orbit search is used.
"""
from pathlib import Path
from collections import defaultdict
import json,hashlib,time
H=Path(__file__).resolve().parent;ROOT=H.parents[1];CE=ROOT/'work_CE/next_symmetric_nodes'
paths=[CE/'symmetric_paired_fox_data.json',CE/'symmetric_F_cycles_and_fixed_chains.json',CE/'symmetric_full_source_data.json']
data,fixed,source=[json.loads(p.read_text()) for p in paths]
start=time.monotonic()
def red(w):
 r=[]
 for x in w:
  if r and r[-1]==-x:r.pop()
  else:r.append(x)
 return tuple(r)
def inv(w):return tuple(-x for x in w[::-1])
def cat(*ws):return red(x for w in ws for x in w)
def sub(w,A):return red(y for x in w for y in(A[abs(x)] if x>0 else inv(A[-x])))
def mp(d):return {int(k):tuple(v) for k,v in d.items()}
def add(d,k,n):
 d[k]+=n
 if not d[k]:del d[k]
beta=mp(data['retained_involution']);F21=mp(data['paired_involution'])
ret={j:i+1 for i,j in enumerate(data['retained_paired_indices'])}
slots=(2,3,5,6,7,8,10,11)
meta={};index={}
def gen(head,slot):
 head=red(head);assert slot in slots;k=(head,slot)
 if k not in index:
  n=len(meta)+1;index[k]=n;meta[n]=k
 return index[k]
def tau(w,t):return red((1 if x>0 else -1)*gen(cat(t,meta[abs(x)][0]),meta[abs(x)][1]) for x in w)
ONE=((),(),())
def gm(g,h):
 a,b,t=g;c,d,s=h
 return cat(a,tau(c,t)),cat(b,tau(d,sub(t,beta))),cat(t,s)
def gi(g):
 a,b,t=g;s=inv(t)
 return tau(inv(a),s),tau(inv(b),sub(s,beta)),s
def gf(g):a,b,t=g;return b,a,sub(t,beta)
def Fedge(v):return {(1-side,slot,gf(g)):n for (side,slot,g),n in v.items()}
def scale(v,n):return {k:n*a for k,a in v.items() if n*a}
def shift(v,g):
 out=defaultdict(int)
 for (side,slot,h),n in v.items():add(out,(side,slot,gm(g,h)),n)
 return dict(out)
def letters(w):
 """Actual G-prefix states; returns semantic edge data and final state."""
 a=b=t=();events=[]
 for x in w:
  j=abs(x);sg=1 if x>0 else -1
  if j in ret:t=cat(t,(sg*ret[j],));continue
  side=0 if j<12 else 1;slot=j if side==0 else j-10
  before=(a,b,t)
  if side==0:a=cat(a,(sg*gen(t,slot),))
  else:b=cat(b,(sg*gen(sub(t,beta),slot),))
  after=(a,b,t);events.append((side,slot,before if sg>0 else after,sg))
 return events,(a,b,t)
def compile_word(w,closed=True):
 events,end=letters(w);v=defaultdict(int)
 for side,slot,g,n in events:add(v,(side,slot,g),n)
 if closed:assert end==ONE
 return dict(v),end
def vertex_boundary(v,only_side=None):
 out=defaultdict(int)
 for (side,slot,(a,b,t)),n in v.items():
  if only_side is not None and side!=only_side:continue
  if side==0:end=(cat(a,(gen(t,slot),)),b)
  else:end=(a,cat(b,(gen(sub(t,beta),slot),)))
  add(out,end,n);add(out,(a,b),-n)
 return dict(out)
def tate(v):
 assert Fedge(v)==scale(v,-1)
 assert not vertex_boundary(v)
 q=vertex_boundary(v,0)
 assert q=={(b,a):n for (a,b),n in q.items()} and sum(q.values())==0
 answer={a:n%2 for (a,b),n in q.items() if a==b and n%2}
 assert sum(answer.values())%2==0
 return answer,q
def dictionary(meta0):
 return {int(k):gen(v['retained_word'],v['paired_slot']) for k,v in meta0.items()}
def rw(w,ids):return red((1 if x>0 else -1)*ids[abs(x)] for x in w)
def square_boundary(cells,ids):
 out=defaultdict(int)
 for c in cells:
  a=rw(c['A_vertex'],ids);b=rw(c['B_vertex'],ids)
  i=ids[c['A_generator']];j=ids[c['B_generator']];n=c['coefficient']
  g,si=meta[i];h,sj=meta[j]
  aj=cat(a,(i,));bj=cat(b,(j,))
  add(out,(0,si,(a,b,g)),n);add(out,(0,si,(a,bj,g)),-n)
  add(out,(1,sj,(aj,b,sub(h,beta))),n);add(out,(1,sj,(a,b,sub(h,beta))),-n)
 return dict(out)
def encode(v):
 return [{'side':'A' if side==0 else 'B','slot':slot,
          'G_coefficient':{'A_word':a,'B_word':b,'retained_word':t},'coefficient':n}
         for (side,slot,(a,b,t)),n in sorted(v.items())]
original_ids=dictionary(data['finite_used_common_R_basis'])
columns=[];bykey={};total_letters=0
for row in data['node_columns']:
 key=(row['loop_index'],row['local_node_index']);w=tuple(row['paired_relator'])
 v,end=compile_word(w);assert v==square_boundary(row['fox_cells'],original_ids)
 assert not vertex_boundary(v)
 fw,_=compile_word(sub(w,F21));assert fw==Fedge(v)
 assert Fedge(Fedge(v))==v
 bykey[key]=v;total_letters+=len(w)
 columns.append({'node_index':key,'literal_word_length':len(w),'boundary_terms':encode(v),
                 'square_boundary_equal':True,'actual_F_word_equal':True})
print('PASS all64 full node boundaries, all square comparisons and actual F images;',total_letters,'letters',flush=True)
fixed_ids=dictionary(fixed['common_R_basis']);calibrations=[]
for row in fixed['fixed_cell_anti_chains']:
 key=tuple(row['node_index']);v=square_boundary(row['actual_anti_chain'],fixed_ids)
 half=(rw(row['E_half_translation']['A_word'],fixed_ids),rw(row['E_half_translation']['B_word'],fixed_ids),())
 translated=shift(bykey[key],half)
 assert v==translated or v==scale(translated,-1)
 orientation=1 if v==translated else -1
 result,q=tate(v)
 expected={rw(z['word'],fixed_ids):z['coefficient_F2'] for z in row['diagonal_group_ring']}
 assert result==expected
 witnesses=[]
 for wit in row['source_left_ideal_zero_witnesses']:
  src=next(s for s in source['source_peripheral_generators'] if s['sheet']==wit['source_sheet'] and s['critical_index']==wit['critical_index'])
  _,(a,b,t)=compile_word(src['positive_source_word_F21'],closed=False)
  assert not t and a==b
  expected_source=rw(wit['source_word_R'],fixed_ids);assert a==expected_source
  target=a if wit['power']==1 else inv(a)
  assert result==({():1,target:1} if target else {})
  witnesses.append({'sheet':src['sheet'],'critical_index':src['critical_index'],'actual_source_word_R':a,'power':wit['power']})
 calibrations.append({'node_index':key,'orientation':orientation,'half_translation':half,
   'boundary_terms':encode(v),'invariant_vertex_chain':[{'A_vertex':a,'B_vertex':b,'coefficient':n} for (a,b),n in sorted(q.items())],
   'Tate_diagonal':[{'R_word':a,'coefficient_F2':n} for a,n in sorted(result.items())],
   'actual_source_witnesses':witnesses})
 print('PASS16-row Tate extraction equals actual source diagonal:',key,'edge terms',len(v),flush=True)
# Exact tiny model, independent of any actual-node diagonal data.
x=gen((),2);y=gen((1,),3);a=(x,y,-x)
box=[{'A_vertex':[],'B_vertex':[],'A_generator':1,'B_generator':1,'coefficient':1}]
# Expand only this three-edge path square to its nine squares.
pv=[];at=()
for k in a:
 an=cat(at,(k,));pv.append((at if k>0 else an,abs(k),1 if k>0 else -1));at=an
toy=defaultdict(int)
for u,i,sg in pv:
 for v,j,tt in pv:
  g,si=meta[i];h,sj=meta[j];n=sg*tt
  add(toy,(0,si,(u,v,g)),n);add(toy,(0,si,(u,cat(v,(j,)),g)),-n)
  add(toy,(1,sj,(cat(u,(i,)),v,sub(h,beta))),n);add(toy,(1,sj,(u,v,sub(h,beta))),-n)
toy_value,_=tate(dict(toy));assert toy_value=={():1,a:1}
out={'scope':__doc__,'input_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
 'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'coefficient_group':'(R_A x R_B) semidirect T with B94 actual action',
 'edge_rows':[{'side':s,'slot':i} for s in('A','B') for i in slots],
 'common_R_basis':{i:{'retained_word':g,'paired_slot':s} for i,(g,s) in meta.items()},
 'columns':columns,'four_actual_source_calibrations':calibrations,
 'toy_root_path_square':{'R_word':a,'Tate_value':[{ 'R_word':w,'coefficient_F2':n} for w,n in toy_value.items()]},
 'counts':{'node_columns':len(columns),'total_literal_letters':total_letters,
           'boundary_terms':sum(len(r['boundary_terms']) for r in columns),'source_calibrations':len(calibrations)},
 'claims_excluded':['global orbit relation generation','field rank argument','automatic old16-row matrix','new kappa value','J_I membership without witness'],
 'elapsed_seconds':time.monotonic()-start}
(H/'boundary16_and_Tate_certificate.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
print('PASS exact16-row model, all4 actual source calibrations and pure root-path calibration; counts',out['counts'],'seconds',round(out['elapsed_seconds'],3),flush=True)
