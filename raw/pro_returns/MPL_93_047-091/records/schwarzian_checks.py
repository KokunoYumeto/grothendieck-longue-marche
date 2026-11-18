"""Targeted research checks only. Does not read or alter the transcription.

Run: python MPL_93_047-091/records/schwarzian_checks.py
Uses exact SymPy arithmetic and exhaustive small finite rings; not a Lean proof.
"""
from itertools import product
from math import comb
import json
import sympy as S

out = {}
a1, a2, a3, b1, b2, b3 = S.symbols('a1 a2 a3 b1 b2 b3')
Q = lambda j1, j2, j3: -j3/j1 + (j2/j1)**2
c1 = a1*b1
c2 = a1*b2 + a2*b1**2
c3 = a1*b3 + 2*a2*b1*b2 + a3*b1**3
chain = S.cancel(Q(c1,c2,c3) - Q(b1,b2,b3) - b1**2*Q(a1,a2,a3))
assert chain == 0
out['integral_three_jet_chain_law'] = str(chain)
factor = S.expand((-2*6*a3/a1 + 3*(2*a2/a1)**2) - 12*Q(a1,a2,a3))
assert factor == 0
out['G_minus_12G0'] = str(factor)

t = S.symbols('t')
def hasse(f, k):
    return S.diff(f,t,k)/S.factorial(k)
def qfun(f):
    return S.factor(Q(hasse(f,1),hasse(f,2),hasse(f,3)))
out['G0_t_t2_coefficient'] = str(qfun(t**2))
out['G0_t_t3_coefficient'] = str(qfun(t**3))
assert qfun(t**2) == 1/(4*t**2)
assert qfun(t**3) == 2/(3*t**2)
a,b,c,d = S.symbols('a b c d')
assert qfun((a*t+b)/(c*t+d)) == 0
out['mobius_Q'] = '0 (rational identity; integral jet proof in supporting record)'

n,r = S.symbols('n r', nonzero=True)
u,v,w = S.symbols('u v w', nonzero=True)
cn = lambda k,x,y,z: -2*z/(k*x) + (2*k+1)*y**2/(k*k*x*x)
lamprime = -(w/u-v*v/u**2)/n
assert S.cancel(2*lamprime+(v/(n*u))**2-cn(n,u,v,w)) == 0
power = S.cancel(cn(n*r,u**r,r*u**(r-1)*v,
                          r*(r-1)*u**(r-2)*v*v+r*u**(r-1)*w)-cn(n,u,v,w))
assert power == 0
out['c_n_from_connection'] = str(cn(n,u,v,w))
out['c_nr_of_power_minus_c_n'] = str(power)
out['delta_n2_square_coefficient'] = str(S.Rational(5,4))
f,g = t,t**2
true_ratio = S.cancel((S.diff(g,t)/g)/(S.diff(f,t)/f))
printed_ratio = S.cancel((S.diff(g,t)/S.diff(f,t))*(g/f))
out['scan077_ratio_true_and_printed'] = [str(true_ratio),str(printed_ratio)]
correct_first = cn(2,g,S.diff(g,t),S.diff(g,t,2))
correct_second = cn(1,f,S.diff(f,t),S.diff(f,t,2))
printed_second = -2*S.diff(f,t,2)/f+3*(S.diff(g,t)/g)**2
out['scan080_correct_G_1_2'] = str(S.cancel(correct_first-correct_second))
out['scan080_printed_G_1_2'] = str(S.cancel(correct_first-printed_second))
assert out['scan080_correct_G_1_2'] == '0'
assert out['scan080_printed_G_1_2'] == '-9/t**2'

def derivative(poly,k,p,q):
    ans=[0]*q
    for i in range(k,q): ans[i-k]=(comb(i,k)*poly[i])%p
    return ans
def mul(x,y,p,q):
    ans=[0]*q
    for i,a in enumerate(x):
        for j,b in enumerate(y[:q-i]): ans[i+j]=(ans[i+j]+a*b)%p
    return ans
def numerator(poly,p,q):
    d1,d2,d3=[derivative(poly,k,p,q) for k in (1,2,3)]
    sq,pr=mul(d2,d2,p,q),mul(d1,d3,p,q)
    return [(a-b)%p for a,b in zip(sq,pr)]

finite=[]
for p,q in [(2,4),(3,9),(5,5)]:
    considered=zero=matches=0
    first_bad=None
    for coeff in product(range(p),repeat=q):
        if coeff[1]==0: continue
        considered+=1
        if any(numerator(coeff,p,q)): continue
        zero+=1
        rat=coeff[2]*pow(coeff[1],-1,p)%p
        mob=[coeff[0]]+[coeff[1]*pow(rat,i-1,p)%p for i in range(1,q)]
        if list(coeff)==mob: matches+=1
        elif first_bad is None: first_bad=list(coeff)
    assert first_bad is None
    assert zero==matches==p*p*(p-1)
    finite.append(dict(p=p,q=q,unit_derivative_elements=considered,
                       zero_numerator=zero,mobius_matches=matches,counterexample=first_bad))
out['nilpotent_model_exhaustive_checks'] = finite
out['binomial_units'] = {f'p={p},q={q}':[comb(k,3)%p for k in range(3,q)]
                         for p,q in [(2,4),(3,9),(5,5),(7,7)]}
small=[]
for p,k,q in [(2,2,4),(3,3,9)]:
    coeff=[0]*q
    coeff[1]=coeff[k]=1
    num=numerator(coeff,p,q)
    assert num[0]==(-1 if p==3 else 1)%p and not any(num[1:])
    small.append(dict(p=p,s=f't+t^{k}',Q_constant=num[0]))
out['level_p_insufficient_examples'] = small
print(json.dumps(out,indent=2))
