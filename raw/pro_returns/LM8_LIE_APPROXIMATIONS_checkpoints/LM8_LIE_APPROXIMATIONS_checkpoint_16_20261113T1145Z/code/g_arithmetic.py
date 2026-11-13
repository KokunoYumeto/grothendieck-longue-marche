#!/usr/bin/env python3
"""Exact certificates for the arithmetic hypotheses and character table.

The arithmetic generation theorem is a cited input; it is not proved by
enumerating formal Lie words.  Injectivity of the three ambient bracket
maps is read from the independently rerunnable exact g_special calculation.
"""
import json, math
from pathlib import Path
from collections import Counter
import sympy as s

def tensor(A,B):
 C=Counter()
 for (a,b),u in A.items():
  for (c,d),v in B.items():C[(a+c,b+d)]+=u*v
 return C

def exterior2(A):
 vs=[w for w,n in A.items() for _ in range(n)];C=Counter()
 for i,(a,b) in enumerate(vs):
  for c,d in vs[i+1:]:C[(a+c,b+d)]+=1
 return C

def main():
 root=Path(__file__).parent
 data=json.loads((root/'g_special_results.json').read_text())
 rows={r['degree']:r for r in data['even_degrees']}
 assert rows[10]['CM_lower_even_bracket_rank']==rows[4]['CM_invariant_dimension']*rows[6]['CM_invariant_dimension']==4
 assert rows[12]['CM_lower_even_bracket_rank']==rows[4]['CM_invariant_dimension']*rows[8]['CM_invariant_dimension']+math.comb(rows[6]['CM_invariant_dimension'],2)==11
 assert rows[14]['CM_lower_even_bracket_rank']==rows[4]['CM_invariant_dimension']*rows[10]['CM_invariant_dimension']+rows[6]['CM_invariant_dimension']*rows[8]['CM_invariant_dimension']==41
 generators={n:Counter({(a,n-a):1 for a in range(1,n) if (2*a-n)%4==0 and (a,n-a)!=(1,1)}) for n in range(2,15,2)}
 g={n:Counter(v) for n,v in generators.items()}
 g[10]+=tensor(g[4],g[6])
 g[12]+=tensor(g[4],g[8])+exterior2(g[6])
 g[14]+=tensor(g[4],g[10])+tensor(g[6],g[8])
 out={'input_theorem':'Ishii 2602.00615v2 Theorem1.2 and Lemma1.5; no freeness assumption',
      'ambient_bracket_injectivity_certificates':{'degree10':4,'degree12':11,'degree14':41},
      'rational_outer_arithmetic_characters':[{'degree':n,'dimension':sum(g[n].values()),'characters':{f'{a},{b}':v for (a,b),v in sorted(g[n].items())},'new_generator_count':sum(generators[n].values())} for n in range(2,15,2)]}
 z=s.symbols('z');f=s.cyclotomic_poly(20,z);disc=int(s.discriminant(f,z));norm=int(s.resultant(f,z**3-z+1,z))
 bound=(4/math.pi)**4*math.factorial(8)/8**8*math.sqrt(disc)
 assert disc==4000000 and norm==5 and 12<bound<13
 # Every prime ideal of norm <=Minkowski bound is above5.
 residue=[{'prime':q,'residue_degree':int(s.n_order(q,20)),'minimal_norm':int(q**s.n_order(q,20))} for q in [3,7,11]]
 # At2 the tame cyclotomic part has order ord_5(2)=4.
 residue.append({'prime':2,'residue_degree':4,'minimal_norm':16})
 assert all(r['minimal_norm']>bound for r in residue)
 units25=[a for a in range(1,25) if math.gcd(a,25)==1]
 roots4=[a for a in units25 if pow(a,4,25)==1]
 cosets={tuple(sorted((a*u)%25 for u in roots4)) for a in units25}
 pi=9 # 2+i modulo(2-i)^2, where i=7 modulo25.
 orbit={tuple(sorted((pow(pi,k,25)*u)%25 for u in roots4)) for k in range(5)}
 assert len(cosets)==len(orbit)==5 and orbit==cosets
 out['ray_class_hypotheses']={'K5':'Q(zeta20)','cyclotomic_polynomial':str(f),'discriminant':disc,'Minkowski_bound':bound,'norm5_element':'zeta20^3-zeta20+1','norm':norm,'other_small_primes':residue,'conclusion_class_number':1,'roots_of_unity_mod25':roots4,'pi_mod_conjugate_prime_squared':pi,'frobenius_orbit_in_units_mod_roots_of_unity':sorted([list(c) for c in orbit]),'number_of_primes_above5_in_K25':2}
 counts=[]
 for q in (5,13):
  points=1+sum(sum((y*y-x*x*x+x)%q==0 for y in range(q)) for x in range(q))
  counts.append({'prime':q,'points':points,'trace':q+1-points})
 assert [r['trace'] for r in counts]==[-2,6]
 out['separating_CM_Frobenius_point_counts']=counts
 (root/'g_arithmetic_results.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(out,indent=2))

if __name__=='__main__':main()
