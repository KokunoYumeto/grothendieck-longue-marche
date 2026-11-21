"""Fixed polynomial computations and the explicit q=2 marginal example; no general theorem claim."""
from pathlib import Path
from datetime import datetime,timezone
from math import comb,gcd
import json,sympy as sp
R=Path(__file__).resolve().parents[1]
A,V=sp.symbols('A V');cases=[]
for q in [2,3,5,7]:
 inner=[comb(q,i) for i in range(1,q)]
 bracket=sp.expand(sum(comb(q,i)*A**i*(q*V)**(q-i-1) for i in range(1,q))+(q*V)**(q-1))
 delta=sp.Poly(sp.expand(bracket-q*A**(q-1)),A,V)
 mod=sp.Integer(0)
 for powers,coefficient in delta.terms():mod+=(int(coefficient)%(q*q))*A**powers[0]*V**powers[1]
 cases.append({'q':q,'inner_binomial_coefficients':inner,'remainders_mod_q':[v%q for v in inner],'substituted_bracket':str(bracket),'bracket_minus_qA_mod_q_squared':str(sp.expand(mod))})
assert all(all(v==0 for v in c['remainders_mod_q']) for c in cases)
assert [c['bracket_minus_qA_mod_q_squared'] for c in cases]==['2*V','0','0','0']
example={'q':2,'a0':1,'b0':1,'gamma':1,'zeta':0,'a':3,'b':4,'c':5,'a_prime':1,'b_prime':2,'a_double_prime':3,'b_double_prime':4}
assert example['b_prime']==2**1*1**2 and example['a_prime']==1**2
assert 5==4+1**2==3+2**1*1**2
assert gcd(1,4)==1 and gcd(1,3)==1 and 0*1==0
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
intro='''# Scan008 — fixed polynomial certificates and marginal example

These calculations concern the supplied page formulas and do not establish their general implications. Each q below is one of the four explicit values2,3,5,7.

For these calculations, each manuscript coefficient symbol C_q^i is assigned the integer in the corresponding finite coefficient row below, computed by the integer function comb(q,i), with the assigned values printed below. This assignment extends the specified polynomial evaluation on those coefficient symbols.

For the binomial coefficients, the coefficient map Z[X,Y] → (Z/qZ)[X,Y] reduces each integer modulo that specified q and fixes X,Y. Addition and multiplication are carried to their coefficientwise residue operations, so these generator assignments define the stated morphism. Every internal coefficient in the four listed rows reduces to0.

For the lower bracket, use S_q(A,B)=sum(i=1,…,q−1) binom(q,i) A^i B^(q−i−1)+B^(q−1), with each listed q substituted before computation. The substitution map σ_q:Z[A,B] → Z[A,V] sends A to A and B to qV, and fixes integers; evaluation respects sums and products. The quotient map ρ_q:Z[A,V] → (Z/q²Z)[A,V] reduces integer coefficients modulo q² and fixes A,V. The composition is explicit. Direct coefficient calculation gives ρ_q(σ_q(S_q)−qA^(q−1))=2V for q=2, and0 for each of q=3,5,7. All unreduced bracket polynomials are below. These are four finite polynomial identities, with no conclusion asserted for other q.

The page's marginal values q=2,a0=b0=1,gamma=1,b=4,a=3,c=5 agree with the parameter values in the previous page's certificate. Direct evaluation gives b′=2, a′=1 and c=4+1=3+2=5. The two accompanying gcd values for the factorizations a=1·3 and b=1·4 are1. These computations check that written example and those concrete factorizations only. The previous event is007-arithmetic-instance.

Executed: NOW

'''.replace('NOW',now)
(R/'checks/scan008_polynomials.md').write_text(intro+'```json\n'+json.dumps({'cases':cases,'example':example},ensure_ascii=False,indent=2)+'\n```\n')
who='GPT-6 Astra Pro; effort inherited, separately verifiable setting not exposed; run /root'
events=[
 {'statement_id':'008-binomial-fixed-coefficients','date':now,'who':who,'type':'computation or formal certificate','outcome':'For q=2,3,5,7, every listed internal binomial coefficient has remainder0 modulo that q. Explicit coefficient-reduction morphisms and complete finite rows are recorded in checks/scan008_polynomials.md. This does not verify the writer’s hypothesis for all primes.'},
 {'statement_id':'008-bracket-fixed-residues','date':now,'who':who,'type':'computation or formal certificate','outcome':'Under B→qV and coefficient reduction modulo q², the written bracket minus q*A^(q−1) has residue2V for q=2 and0 for q=3,5,7. All four concrete substitution and quotient morphisms and exact polynomials are in checks/scan008_polynomials.md. No general implication or handwritten correction is inferred.'},
 {'statement_id':'008-marginal-example','date':now,'who':who,'type':'computation or formal certificate','outcome':'The written q=2,a0=b0=1,gamma=1,a=3,b=4,c=5 values give b-prime=2, a-prime=1 and c=4+1=3+2=5. The associated concrete factorizations a=1*3,b=1*4 have gcd values1. Values from007-arithmetic-instance are explicitly re-evaluated here; scope is this example only. Source checks/scan008_polynomials.md.'}]
(R/'checks/scan008_check_events.json').write_text(json.dumps(events,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'executed':now,'cases':cases,'example_verified':True}))
