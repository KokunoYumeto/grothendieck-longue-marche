#!/usr/bin/env python3
"""Exact kernel tests for the first CM-permitted non-inner derivation.
These finite tests are evidence only, not a proof of its full constants.
"""
from g_special import *

def main():
 eps=(bracket(x,bracket(x,bracket(x,bracket(x,y)))),
      add(bracket(y,bracket(x,bracket(x,bracket(x,y)))),bracket(c,bracket(x,c)),-1))
 D=dbracket((y,{}),eps)
 out={'kernel_tests':[]}
 for n in range(1,11):
  start=time.time();r=0
  for a in range(n+1):
   ws=[w for w in lyndon(2,n) if w.count(0)==a]
   cols=[coords(derivative(D,expand(w)),2,n+4) for w in ws]
   if not cols:continue
   inds=sorted(set().union(*[set(v) for v in cols]));rr={j:i for i,j in enumerate(inds)}
   A=mat([{rr[j]:q for j,q in v.items()} for v in cols],len(inds))
   r+=A.rank()
  row={'degree':n,'dimension':len(lyndon(2,n)),'rank_D4_middle':r,'kernel_dimension':len(lyndon(2,n))-r}
  out['kernel_tests'].append(row);print(row,'seconds',round(time.time()-start,3),flush=True)
  Path(__file__).with_name('g_kernel_results.json').write_text(json.dumps(out,indent=2)+'\n')
 # Add the only odd-odd lower bracket possible through even degree 14.
 candidates=[]
 for a in range(4,8):
  b=14-a
  A,B=special(a),special(b)
  for i,D0 in enumerate(A):
   for j,E0 in enumerate(B):
    if a==b and i>=j:continue
    candidates.append(dbracket(D0,E0))
 ranks=rank_by_weight(candidates,14)
 out['all_lower_brackets_degree14']={'rank':sum(ranks.values()),'characters':ranks}
 Path(__file__).with_name('g_kernel_results.json').write_text(json.dumps(out,indent=2)+'\n')
 print(out['all_lower_brackets_degree14'],flush=True)

if __name__=='__main__':main()
