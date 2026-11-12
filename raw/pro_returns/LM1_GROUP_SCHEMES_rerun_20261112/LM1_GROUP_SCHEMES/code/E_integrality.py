"""Exact rational computations for LM §50, C4 scans 6 and 9--16.

Run with Python 3 and SymPy.  No floating point arithmetic is used.
The degree-12 search is finite and its universe is explicitly recorded.
"""
from fractions import Fraction
from itertools import product
from math import factorial, prod
import json
from pathlib import Path
import sympy as s

OUT = Path(__file__).resolve().parent

def integral(M, p=None):
    if p is None:
        return all(x.q == 1 for x in M)
    return all(int(x.q) % p for x in M)

def log_unipotent(N):
    return sum(((-1)**(j+1)*N**j/s.Integer(j) for j in range(1,N.rows)),s.zeros(N.rows))

def exp_nilpotent(X):
    return sum((X**j/s.factorial(j) for j in range(X.rows)),s.zeros(X.rows))

def jordan(n, weights=None):
    M=s.zeros(n)
    for i,w in enumerate(weights or [1]*(n-1)):
        M[i,i+1]=w
    return M

def vp(n,p):
    e=0
    while n and n%p==0:
        e+=1; n//=p
    return e

def flatten(M): return [[str(x) for x in M.row(i)] for i in range(M.rows)]

results={}

# The actual exponential hypothesis (9), without an extra assumption X integral.
N=jordan(3); X=log_unipotent(N)
assert exp_nilpotent(X)==s.eye(3)+N
assert integral(exp_nilpotent(X)) and integral(exp_nilpotent(-X))
assert not integral(X)
results['rank3_exponential_counterexample']={
    'X':flatten(X),'exp_X':flatten(exp_nilpotent(X)),
    'exp_minus_X':flatten(exp_nilpotent(-X)), 'failure':'X[0,2]=-1/2'}

# The literal signed hypothesis (11), whose dropped ±X changes the problem.
# Search upper-triangular matrices in an explicit finite rational grid.
found=None; tested=0
for a,d,f,e in product([s.Rational(1,2),s.Integer(1),s.Integer(2)],
                       range(1,25),[s.Rational(1,2),s.Integer(1),s.Integer(2)],range(0,5)):
    X=s.zeros(4);X[0,1]=a;X[1,2]=d;X[2,3]=f;X[1,3]=e
    A=X**2/2;B=X**3/6;tested+=1
    if integral(A+B) and integral(A-B) and not(integral(A) and integral(B)):
        found=X;break
assert found is not None
X=found;A=X**2/2;B=X**3/6
assert X**4==s.zeros(4)
results['rank4_literal_signed_counterexample']={
    'universe':'a,f in {1/2,1,2}; d in 1..24; e in 0..4; other upper entries 0',
    'tested_until_first':tested,'X':flatten(X),'A':flatten(A),'B':flatten(B),
    'A_plus_B':flatten(A+B),'A_minus_B':flatten(A-B)}

# Exhaust every degree d <= 12 in two specified integer-valued polynomial families.
# Family J: X=log(1+J_{d+1}); family W_p: truncate excess p valuations of
# weights i, so all geometric fibres have p-order while degree p^2 is obstructed.
rows=[]
for p in (2,3,5):
  for d in range(1,13):
    for family in ('J','W'):
      weights=([1]*d if family=='J' else
               [i//(p**max(vp(i,p)-1,0)) for i in range(1,d+1)])
      N=jordan(d+1,weights);X=log_unipotent(N)
      assert exp_nilpotent(X)==s.eye(d+1)+N
      assert integral(exp_nilpotent(X)) and integral(exp_nilpotent(-X))
      bad=[j for j in range(1,d+1) if not integral(X**j/s.factorial(j),p)]
      local_order_p=all(int(x)%p==0 for x in N**p)
      rows.append({'prime':p,'degree':d,'family':family,'weights':weights,
                   'X_p_integral':integral(X,p),
                   'N_power_p_divisible_by_p':local_order_p,
                   'failed_divided_powers':bad})
results['degree12_search']=rows

# Explicit genuine fibrewise-unipotent section over Z, not merely in GL_n(Q).
weights=[1,2,3,2];N=jordan(5,weights);X=log_unipotent(N)
assert integral(X)
assert all(int(x)%2==0 for x in N**2)
assert all(int(x)%3==0 for x in N**3)
assert X**4/s.factorial(4)==s.Rational(1,2)*s.SparseMatrix(5,5,{(0,4):1})
results['rank5_genuine_fibrewise_counterexample']={
    'weights':weights,'N':flatten(N),'X':flatten(X),'X4_over_24':flatten(X**4/24),
    'all_fibres_Ga_values':'N^2=0 mod2; N^3=0 mod3; N^5=0 in every other characteristic'}

# Integer-valued polynomial expansion: coefficients in binomial basis vs monomial.
t=s.symbols('t')
binom=[]
for d in range(13):
    P=prod((t-i) for i in range(d))/s.factorial(d)
    vals=[int(P.subs(t,n)) for n in range(-12,13)] if hasattr(P,'subs') else [int(P)]*25
    binom.append({'degree':d,'polynomial':str(s.expand(P)),
                  'denominator':int(s.ilcm(*[int(c.q) for c in s.Poly(P,t).all_coeffs()])) if d else 1,
                  'integer_values_checked':len(vals)})
results['binomial_basis']=binom

# Witt vectors: W_2(F_p) is Z/p^2 on F_p points. Addition formulas are checked
# by integer Teichmuller coordinates using the Witt ghost polynomials.
witt=[]
for p in (2,3,5):
    elems=list(product(range(p),repeat=2))
    def add(a,b):
        x=(a[0]+b[0])%p
        C=((a[0]+b[0])**p-a[0]**p-b[0]**p)//p
        y=(a[1]+b[1]-C)%p
        return (x,y)
    cur=(0,0);order=0
    while True:
        cur=add(cur,(1,0));order+=1
        if cur==(0,0):break
        assert order<=p*p
    assert order==p*p
    assert all(add(add(a,b),c)==add(a,add(b,c)) for a,b,c in product(elems,repeat=3))
    witt.append({'p':p,'order_of_1_0':order,'associativity_triples':len(elems)**3})
results['Witt_vectors']=witt

# Z/4 deformed additive group law F(x,y)=x+y+2xy.
law=lambda x,y:(x+y+2*x*y)%4
assert all(law(law(x,y),z)==law(x,law(y,z)) for x,y,z in product(range(4),repeat=3))
assert law(1,1)==0
# Finite search all polynomials degree <= 6 with f(0)=0, f(1)=1; test the
# POLYNOMIAL group identity, not only the 16 evaluations on Z/4 points.
successful=[];count=0
for coeff in product(range(4),repeat=6):
    if sum(coeff)%4!=1: continue
    count+=1
    ok=True
    from math import comb
    for i in range(1,7):
      for j in range(1,7):
        lhs=(comb(i+j,i)*coeff[i+j-1]) if i+j<=6 else 0
        rhs=2*coeff[i-1]*coeff[j-1]
        if (lhs-rhs)%4:ok=False;break
      if not ok:break
    if ok:successful.append(coeff)
assert not successful
results['Z4_deformed_group']={'polynomials_tested':count,'degree_bound':6,
                            'solutions':successful,'g_order':2,
                            'special_fibre':'Ga over F2; g=1'}

# The same smooth counterexample exists over Z/p^2 for every prime:
# F_p(x,y)=x+y+p*C_p(x,y), C_p=((x+y)^p-x^p-y^p)/p.
from math import comb
deformations=[]
for p in (2,3,5):
    q=p*p
    def Cp(x,y):return ((x+y)**p-x**p-y**p)//p
    def Fp(x,y):return (x+y+p*Cp(x,y))%q
    assert all(Fp(Fp(x,y),z)==Fp(x,Fp(y,z)) for x,y,z in product(range(q),repeat=3))
    cur=0
    for k in range(1,p+1):
        cur=Fp(cur,1)
        assert (cur==0)==(k==p)
    obstructions=[]
    for r in range(4):
        d=p**r
        assert vp(comb(p*d,d),p)==1
        assert (p*comb(p*d,d))%(p*p)==0
        obstructions.append({'d':d,'valuation_binomial':vp(comb(p*d,d),p),
                             'lhs_if_a_pd_multiple_p':0,'rhs_if_a_d_1':p})
    deformations.append({'p':p,'associativity_triples':q**3,'order_g':p,
                         'leading_term_obstructions':obstructions})
results['Zp2_deformed_groups']=deformations

# Scan 13 equation (20): the A reading makes its conclusion tautological;
# with K in its initial membership, a square-zero rank-five matrix refutes it.
squarezero=s.zeros(5);squarezero[0,1]=s.Rational(1,2)
assert squarezero**2==s.zeros(5) and not integral(squarezero)
assert all(integral(squarezero**j/s.factorial(j)) for j in range(2,5))
# The first-pass 6! in the cubic exponential term cannot be an exponential:
# its t^2*u coefficient fails the addition law already on J_4.
u=s.symbols('u');J=jordan(4)
def cubic(z,denom):return s.eye(4)+z*J+z*z*J**2/2+z**3*J**3/denom
good=(cubic(t+u,6)-cubic(t,6)*cubic(u,6)).applyfunc(s.expand)
bad=cubic(t+u,720)-cubic(t,720)*cubic(u,720)
assert good==s.zeros(4)
badcoeff=s.expand(bad[0,3]).coeff(t,2).coeff(u,1)
assert badcoeff==s.Rational(-119,240)
results['scan13_readings']={'equation20_K_counterexample':flatten(squarezero),
    'equation20_A_reading':'conclusion X integral is already assumed',
    'cubic_3_factorial_addition_identity':True,
    'cubic_6_factorial_t2_u_failure':str(badcoeff)}

(OUT/'E_integrality.json').write_text(json.dumps(results,indent=2)+'\n')
print('Exact matrix and polynomial checks: PASS')
print('Literal signed rank-4 search tested',tested,'matrices before first counterexample.')
print('Actual exponential hypothesis fails already in rank 3 over Z_(2).')
print('Genuine fibrewise-unipotent section over Z: rank 5, weights 1,2,3,2; no Ga lift.')
for p in (2,3,5):
    for fam in ('J','W'):
        failed=[r['degree'] for r in rows if r['prime']==p and r['family']==fam and r['failed_divided_powers']]
        print('p =',p,'family',fam,'first failed degree <= 12:',min(failed) if failed else 'none')
print('Witt vector orders:',witt)
print('Z/4 deformation: tested',count,'polynomials degree <= 6; zero solutions.')
print('Z/p^2 smooth deformations:',[(z['p'],z['associativity_triples'],z['order_g']) for z in deformations])
print('Scan 13 alternatives: K reading refuted by square-zero X; 3! valid; 6! fails with coefficient',badcoeff)
