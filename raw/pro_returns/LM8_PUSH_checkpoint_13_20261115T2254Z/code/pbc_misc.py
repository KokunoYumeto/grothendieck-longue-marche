"""Exact elementary certificates for C.10, C.13 and C.15."""
import itertools,json
from pathlib import Path
import sympy as S

def mul(g,h):return tuple(g[h[i]] for i in range(len(g)))
def parity(g):return sum(g[i]>g[j] for i in range(len(g)) for j in range(i+1,len(g)))%2
def generated(gens,n):
 E={tuple(range(n))};Q=list(E)
 for g in Q:
  for h in gens:
   k=mul(g,h)
   if k not in E:E.add(k);Q.append(k)
 return E
S3=set(itertools.permutations(range(3)));A3={g for g in S3 if not parity(g)}
A4={g for g in itertools.permutations(range(4)) if not parity(g)}
V4=generated([(1,0,3,2),(2,3,0,1)],4)
assert len(S3)//len(A3)==2 and len(A4)//len(V4)==3
r=(1,2,3,0);s=(0,3,2,1);D4=generated([r,s],4)
r2=mul(r,r);rs=mul(r,s);B=generated([r2,rs],4)
assert len(D4)==8 and len(B)==4 and all(mul(a,b)==mul(b,a) for a in B for b in B)
assert mul(r,s)!=mul(s,r)
l,w=S.symbols('lambda w')
j=256*(1-l+l*l)**3/(l*l*(1-l)**2)
assert S.factor((64*(4-w)**3/w**2).subs(w,4*l*(1-l))-j)==0
out={'index_prime_small_cases':{'S3':len(S3),'A3':len(A3),'index':2,'A4':len(A4),'V4':len(V4),'second_index':3},'D4_order':len(D4),'subgroup_over_Qsqrt_minus3_order':len(B),'subgroup_abelian':True,'D4_nonabelian':True,'harmonic_j_factorization':True,'branch_derivative':str(S.diff(4*l*(1-l),l))}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
