#!/usr/bin/env python3
"""Exact multigraded special derivations and lower-bracket images through 14.

Every rank in this script is over Q (sympy exact rational arithmetic).
Character dimensions additionally follow from the integral split-surjection
(u,v) -> [u,y]+[x,v].  No finite-field rank is silently identified with a
Q-rank, and no ambient derivation dimension is called a Galois dimension.
"""
from g_lie_core import *
from collections import Counter
from math import gcd
from functools import reduce

x,y=gen(0),gen(1)
c=bracket(x,y)

def vec_coords(p,n):
 return coords(p,2,n)

def deriv_coords(D,n):
 k=len(lyndon(2,n+1)); out={}
 for i,p in enumerate(D):
  for j,v in coords(p,2,n+1).items(): out[i*k+j]=v
 return out

def mat(vectors,nrows):
 A=sp.zeros(nrows,len(vectors))
 for j,v in enumerate(vectors):
  for i,z in v.items():A[i,j]=z
 return A

def weight(D):
 ws=set()
 for i,p in enumerate(D):
  for w in p:
   a=w.count(0)-(i==0);b=w.count(1)-(i==1)
   ws.add((a,b))
 assert len(ws)==1,ws
 return next(iter(ws))

def normalize(v):
 den=sp.ilcm(*[sp.denom(a) for a in v])
 a=[int(q*den) for q in v]
 g=reduce(gcd,a)
 return [q//g for q in a]

@lru_cache(None)
def special(n):
 """An exact Q-basis, each vector with primitive integral coefficients."""
 out=[]; words=lyndon(2,n+1)
 for a in range(n+1):
  b=n-a
  ub=[expand(w) for w in words if w.count(0)==a+1]
  vb=[expand(w) for w in words if w.count(0)==a]
  cols=[coords(bracket(u,y),2,n+2) for u in ub]
  cols += [coords(bracket(x,v),2,n+2) for v in vb]
  if not cols: continue
  indices=sorted(set().union(*[set(v) for v in cols]))
  rows={v:i for i,v in enumerate(indices)}
  A=mat([{rows[i]:q for i,q in col.items()} for col in cols],len(rows))
  for v in A.nullspace():
   vv=normalize(v)
   D=(lincomb(vv[:len(ub)],ub),lincomb(vv[len(ub):],vb))
   assert not derivative(D,c)
   assert weight(D)==(a,b)
   out.append(D)
 return tuple(out)

def rank_by_weight(ds,n):
 groups={}
 for D in ds:
  if not any(D):continue
  groups.setdefault(weight(D),[]).append(deriv_coords(D,n))
 result={}
 for w,cs in groups.items():
  rows=sorted(set().union(*[set(v) for v in cs])); rr={j:i for i,j in enumerate(rows)}
  A=mat([{rr[j]:q for j,q in v.items()} for v in cs],len(rows))
  result[f'{w[0]},{w[1]}']=A.rank()
 return result

def characters(n):
 L1=Counter(w.count(0) for w in lyndon(2,n+1))
 L2=Counter(w.count(0) for w in lyndon(2,n+2))
 ans={}
 for a in range(n+1):
  v=L1[a+1]+L1[a]-L2[a+1]
  if v:ans[f'{a},{n-a}']=v
 return ans

def descriptor(p,n):
 return {''.join('xy'[j] for j in lyndon(2,n)[i]):int(q) for i,q in coords(p,2,n).items()}

def main():
 out={'conventions':'derivation degree m sends length 1 to length m+1; character (a,b) is psi^a psibar^b',
      'free_lie':[],'even_degrees':[],'degree4':{}}
 for n in range(1,17):
  words=lyndon(2,n)
  wit=sum(int(sp.mobius(d))*2**(n//d) for d in sp.divisors(n))//n
  assert len(words)==wit
  # Exact triangularity certificate for all words through 14.
  if n<=14:
   for w in words:
    p=expand(w);assert p[w]==1 and min(p)==w
  out['free_lie'].append({'degree':n,'dimension':wit,'checked_Lyndon_triangularity':n<=14})
  print('free_lie',n,wit,flush=True)
 for n in range(2,15,2):
  start=time.time();ch=characters(n)
  candidates=[];cm_candidates=[]
  # ad(c) is central; omit its identically zero brackets.
  for a in range(4,n//2+1,2):
   b=n-a
   A,B=special(a),special(b)
   for i,D in enumerate(A):
    for j,E in enumerate(B):
     if a==b and i>=j:continue
     Z=dbracket(D,E)
     if any(Z):
      assert not derivative(Z,c)
      candidates.append(Z)
      wd,we=weight(D),weight(E)
      if (wd[0]-wd[1])%4==0 and (we[0]-we[1])%4==0:cm_candidates.append(Z)
  br=rank_by_weight(candidates,n);cmbr=rank_by_weight(cm_candidates,n)
  cm={w:v for w,v in ch.items() if (int(w.split(',')[0])-int(w.split(',')[1]))%4==0}
  row={'degree':n,'dimension':sum(ch.values()),'characters':ch,
       'CM_invariant_dimension':sum(cm.values()),'CM_invariant_characters':cm,
       'lower_even_bracket_rank':sum(br.values()),'lower_even_bracket_characters':br,
       'CM_lower_even_bracket_rank':sum(cmbr.values()),'CM_lower_even_bracket_characters':cmbr}
  out['even_degrees'].append(row)
  print(json.dumps(row), 'seconds',round(time.time()-start,3),flush=True)
  Path(__file__).with_name('g_special_results.json').write_text(json.dumps(out,indent=2)+'\n')
 eps=(bracket(x,bracket(x,bracket(x,bracket(x,y)))),
      add(bracket(y,bracket(x,bracket(x,bracket(x,y)))),bracket(c,bracket(x,c)),-1))
 mid=dbracket((y,{}),eps)
 for name,D in [('epsilon4',eps),('middle',mid)]:
  assert not derivative(D,c)
  out['degree4'][name]={'x':descriptor(D[0],5),'y':descriptor(D[1],5),'weight':weight(D)}
 # Conjugacy obstruction: D(x) is not in [x,L4_(2,2)].
 cols=[coords(bracket(x,expand(w)),2,5) for w in lyndon(2,4) if w.count(0)==2]
 rank0=mat(cols,len(lyndon(2,5))).rank()
 rank1=mat(cols+[coords(mid[0],2,5)],len(lyndon(2,5))).rank()
 out['degree4']['middle_conjugacy_obstruction']={'rank_inner':rank0,'rank_augmented':rank1}
 assert rank1==rank0+1
 # The degree-two derivation is central in all special derivations.
 inn=(bracket(c,x),bracket(c,y))
 for n in range(2,11,2):
  assert len(special(n))==sum(characters(n).values())
  for D in special(n):assert not any(dbracket(inn,D))
 out['verification']={'arithmetic':'exact_Q','central_ad_c_checked_through':10,
                      'Q_basis_checked_through':10,'basis_vectors_are_not_claimed_Z5_saturated':True}
 Path(__file__).with_name('g_special_results.json').write_text(json.dumps(out,indent=2)+'\n')
 print('degree4',json.dumps(out['degree4']),flush=True)

if __name__=='__main__':main()
