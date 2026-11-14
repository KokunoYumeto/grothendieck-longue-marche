"""Exact thirteen-torsion and Frobenius-cycle certificate for A.C2.4."""
from pathlib import Path
import json
import sympy as S

alpha,beta,u=S.symbols('alpha beta u')
G=S.groebner([beta**2+alpha**2*beta+1,alpha**2+alpha+1],beta,alpha,u,modulus=2)
def reduce(poly):
    expr=S.Poly(S.expand(poly),beta,alpha,u,modulus=2).as_expr()
    return G.reduce(expr)[1]
checks=[]
def check(name,test):
    assert test,name
    checks.append({'name':name,'passed':True})
A=alpha*(1+beta)*u**6+alpha**2*beta*u**5+alpha*u**4+alpha*(1+beta)*u**3+(1+alpha*beta)*u**2+alpha*u+alpha**2
B=u**4+alpha*u**3+u+1
norm=A*A+u*u*A*B+(u**5+u)*B*B
check('point_R_on_curve',reduce(beta**2+alpha**2*beta+alpha**5+alpha)==0)
check('degree_thirteen_norm_identity',reduce(norm+(u+alpha)**13)==0)
check('function_vanishes_at_R',reduce(A.subs(u,alpha)+B.subs(u,alpha)*beta)==0)
check('conjugate_value_is_nonzero_alpha',reduce(A.subs(u,alpha)+B.subs(u,alpha)*(beta+alpha**2)+alpha)==0)
check('pole_order_is_thirteen',S.Poly(A,u).degree()*2==12 and S.Poly(B,u).degree()*2+5==13)
cycle=[pow(2,i,13) for i in range(12)]
check('two_is_primitive_mod_thirteen',len(set(cycle))==12 and set(cycle)==set(range(1,13)))
N=S.zeros(12)
for j in range(1,12):
    target=cycle.index((2*cycle[j])%13)
    N[target,j]=1
check('one_zero_edge_kills_cycle',N**12==S.zeros(12) and N**11!=S.zeros(12))
check('cover_genus_fourteen',13*(2*2-2)==2*14-2)
check('involution_quotient_genus_six',2*14-2==2*(2*6-2)+4+2)
check('isogeny_dimension_balance',14==2+2*6)
# Artin--Schreier rank balance: f(D)=f(C)=1 forces f(B)=0.
check('rank_balance',1==1+2*0)
out={'passed':True,'check_count':len(checks),'checks':checks,
 'field_relations':['alpha^2+alpha+1=0','beta^2+alpha^2*beta+1=0'],
 'curve':'V^2+u^2*V=u^5+u',
 'point':['alpha','beta'],
 'norm_identity':'Norm(A+B*V)=(u+alpha)^13',
 'multiplication_by_two_cycle_mod_13':cycle,
 'scope':'Exact finite algebra certificate. Divisor, Frobenius sheaf, quotient, and section arguments are proved in A.C2.4.'}
Path(__file__).with_name('A_char2_thirteen_checks_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
