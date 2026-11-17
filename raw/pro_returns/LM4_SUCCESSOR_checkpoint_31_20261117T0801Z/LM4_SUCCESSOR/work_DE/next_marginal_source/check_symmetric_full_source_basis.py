#!/usr/bin/env python3
"""Independent47-to19 Schreier filling and finite source-data audit."""
from pathlib import Path
import json
H=Path(__file__).resolve().parent;ROOT=H.parent.parent;P=ROOT/'work_CE/next_symmetric_nodes'
D=json.loads((P/'symmetric_full_source_data.json').read_text());B=json.loads((P/'symmetric_paired_fox_data.json').read_text())

def red(w):
 out=[]
 for x in w:
  if out and out[-1]==-x:out.pop()
  else:out.append(int(x))
 return tuple(out)
def inv(w):return tuple(-x for x in reversed(w))
def sub(w,A):return red(y for x in w for y in (A[abs(x)] if x>0 else inv(A[abs(x)])))
# Build the actual index-two cover graph of the24-punctured-plane rose.
# The sole spanning-tree edge is b=2 from vertex0 to1.
b=2;spec=[];edge={}
for state in (0,1):
 for j in range(1,25):
  nxt=state^(j==b);w=red(((b,) if state else ())+(j,)+((-b,) if nxt else ()))
  if w:spec.append(w);edge[state,j]=len(spec)
  else:edge[state,j]=0
assert len(spec)==47

def rewrite(w):
 state=0;out=[]
 for x in w:
  j=abs(x);nxt=state^(j==b);k=edge[(state if x>0 else nxt),j]
  if k:out.append(k if x>0 else -k)
  state=nxt
 assert not state
 ans=red(out);assert sub(ans,{i+1:w for i,w in enumerate(spec)})==red(w)
 return ans
for i,w in enumerate(spec,1):assert rewrite(w)==(i,)
old=[tuple(r['far_base_word']) for r in D['old_source_generators']]
nodal=[tuple(r['far_base_word']) for r in D['all36_returned_nodal_lifts']]
assert len(old)==11 and len(nodal)==36 and set(old+nodal)==set(spec)
oldids={rewrite(w)[0] for w in old};nodeids={rewrite(w)[0] for w in nodal}
filled={rewrite(r['far_base_word'])[0] for r in D['all36_returned_nodal_lifts'] if not r['is_source_puncture']}
seedids={rewrite(r['far_base_word'])[0] for r in D['source_peripheral_generators']}
assert len(filled)==28 and len(seedids)==8 and len(oldids)==11
assert filled|seedids==nodeids and not(filled&seedids) and not(oldids&nodeids)
assert len(set(range(1,48))-filled)==19
# These are basis deletions, not a quotient presentation inferred from counts.
Fauto={int(j):tuple(w) for j,w in B['paired_involution'].items()};expected=set()
for r in D['old_source_generators']:
 h=tuple(r['h_paired']);k=tuple(r['k_paired']);assert red(sub(h,Fauto)+inv(h))==k
 A={int(j):tuple(w) for j,w in r['source_push_F21'].items()}
 for j in range(1,22):assert sub(A[j],Fauto)==sub(Fauto[j],A)
for r in D['source_peripheral_generators']:
 ab={int(j):v for j,v in r['physical_abelianization'].items()};assert len(ab)==2 and set(ab.values())=={1}
 aa=[j for j in ab if 3<=j<11];bb=[j for j in ab if 11<=j<19];assert len(aa)==len(bb)==1 and bb[0]==aa[0]+8
 expected.add(aa[0]);w=tuple(r['positive_source_word_F13']);c=tuple(r['F13_conjugator']);assert w==red(c+(r['F13_positive_core'],)+inv(c))
assert expected==set(range(3,11))
for r in D['all36_returned_nodal_lifts']:
 if not r['is_source_puncture']:assert not r['h_F13']
(H/'symmetric_full_source_basis_review.json').write_text(json.dumps({'regular_source_rank':47,'explicit_Schreier_basis':[list(w) for w in spec],'retained_source_basis_indices':sorted(oldids),'actual_source_peripheral_basis_indices':sorted(seedids),'filled_regular_source_basis_indices':sorted(filled),'source_rank_after_regular_filling':19,'source_rank_after_all_filling':11,'exact_F_commutation_checks':231,'eight_distinct_A_peripheral_labels':sorted(expected),'scope':'actual free-cover basis and source filling; image subgroup is not asserted free or equal to R'},indent=2)+'\n')
print('PASS: explicit47-word Schreier basis, not just Euler/rank counting.')
print('PASS: the28 regular puncture basis deletions leave exactly11 old heads+8 actual source meridians.')
print('PASS: all231 old source/F commutation identities and all eight distinct positive A inertia labels.')
print('PASS:28 regular-source corrections die in actual F13; no free-F21 triviality assumed.')
