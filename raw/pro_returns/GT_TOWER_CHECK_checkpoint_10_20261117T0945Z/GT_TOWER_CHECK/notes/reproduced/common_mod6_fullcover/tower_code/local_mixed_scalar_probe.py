#!/usr/bin/env python3
"""Exact sample commutator words for the remaining local scalar.
These are formal words, not assertions of gentle or pentagon lifts.
"""
import json
from pathlib import Path
D=Path(__file__).parent;j=json.loads((D/'local_mixed_normal_form.json').read_text());edges=j['generator_edges'];co=j['all_normal_coordinates'];words=j['generator_words']
def orig(w):
 i=0
 for k in w:
  for _ in range(1 if k>0 else 3):i=edges[i][abs(k)-1]
 return i
def inverse(w):return tuple(-k for k in reversed(w))
def comm(a,b):return a+b+inverse(a)+inverse(b)
def ev(w,pair):
 return orig(tuple(t for k in w for t in (pair[k-1] if k>0 else inverse(pair[-k-1]))))
def c2(w):
 state=0;c=0
 for k in w:
  if abs(k)==1:state^=1
  elif state==0:c+=1 if k>0 else -1
 assert state==0
 return c%3
xy=comm((1,),(2,));tests=[xy,xy*2,comm((1,),xy),comm((2,),xy),comm(xy,comm((1,),xy))]
records=[]
for w in tests:
 a=co[ev(w,((1,),(2,2)))];b=co[ev(w,((1,1),(2,)))];c=c2(w)
 rec={'word':w,'c2_mod3':c,'first':a,'second':b,'scalar':(a[2]-b[2]-2*c)%3};records.append(rec);print(rec,flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps({'scope':'Formal commutator-word samples only; no gentle/pentagon membership asserted','records':records},indent=2)+'\n')
