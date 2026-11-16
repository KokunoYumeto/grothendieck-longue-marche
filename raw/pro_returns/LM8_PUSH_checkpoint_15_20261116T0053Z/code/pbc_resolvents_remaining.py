#!/usr/bin/env python3
"""Exact degree-seven/eleven orbifold fillings and finite domain tests.

The classical polynomial models are compared with Adrianov--Vatuzov,
arXiv:2401.00183, orbits7.2 and11.1, printed pages5--6 and9--10.
All polynomial identities, residual point fields, and the finite marked
coset tests used here are recomputed, rather than inferred from passports.
"""
from pathlib import Path
from itertools import product, permutations
import json
import sympy as sp

z,w,t=sp.symbols('z w t')
def red(f,d):return sp.rem(sp.Poly(sp.expand(f),w),sp.Poly(w*w-w+d,w)).as_expr().expand()

# Classical degree7 model, with w^2-w+2=0.
P7=z*z+28
L7=z+7*w
Q7=z*z+6*w*z+4
E7=(z*z-4*z-4*(1-w)*(1-6*w))*(z-w*(3+2*w))
c7=-64*27*w**14  # Corrects the sign in the printed orbit7.2 constant.
assert red(P7**3*L7-Q7**2*E7-c7,2)==0
assert red(sp.diff(P7**3*L7,z)-7*P7**2*Q7,2)==0
eta=1-2*w
b=(11+eta)/56
Pn=t*(t*t+t+b)**3
Qn=7*t*t+4*t+b
Rn=-sp.Rational(351,3294172)-sp.Rational(27,470596)*eta
cn=(-11+eta)/14
quad=t*t+(15+eta)*t/14+27*(3+eta)/392
assert red(Pn-Rn-Qn**2*(t-cn)*quad/49,2)==0
assert red((P7**3*L7).subs(z,-7*w*(2*t+1))*Rn-c7*Pn,2)==0
assert sp.expand((14-6*sp.Symbol('e'))*(14+6*sp.Symbol('e'))).subs(sp.Symbol('e')**2,-7)==448

# Classical degree11 model, with w^2-w+3=0.
P11=(z-(1+w))*(z*z+(2+w)*z-(1-w))
L11=z*z-3*z-2*w*w
Q11=(z-(1-w))*(z**3-(1+w)*z*z-(1+2*w)*z-3*(1-w))
E11=z**3+4*z*z+w**4*z+2*(5-6*w)
c11=-1728
assert red(P11**3*L11-Q11**2*E11-c11,3)==0
assert red(sp.diff(P11**3*L11,z)-11*P11**2*Q11,3)==0
for f in [P11,L11,Q11,E11]:
    assert red(sp.discriminant(f,z),3)!=0
for f,g in [(P11,L11),(Q11,E11),(L11,E11)]:
    assert red(sp.resultant(f,g,z),3)!=0
disc11=red(sp.discriminant(L11,z),3)
assert disc11==8*w-15
assert red(disc11*disc11.subs(w,1-w),3)==297
E11r=red(E11,3)
mod5=[int(E11r.subs({z:a,w:2}))%5 for a in range(5)]
assert mod5==[1,2,2,2,3]

def finite(p,bmat):
    def norm(a):
        a=tuple(v%p for v in a);first=next(v for v in a if v)
        return tuple(v*pow(first,-1,p)%p for v in a)
    def det(a):return (a[0]*a[3]-a[1]*a[2])%p
    def mul(a,b):return norm((a[0]*b[0]+a[1]*b[2],a[0]*b[1]+a[1]*b[3],a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3]))
    def inv(a):return norm((a[3],-a[1],-a[2],a[0]))
    one=norm((1,0,0,1));S=norm((0,-1,1,0));R=norm((0,-1,1,-1))
    def cj(a,b):return mul(mul(a,b),inv(a))
    def closure(gens):
        seen={one};todo=[one]
        for a in todo:
            for b in gens:
                c=mul(a,b)
                if c not in seen:seen.add(c);todo.append(c)
        return seen
    G=closure([S,R]);H=closure([S,norm(bmat)])
    PG={norm(a) for a in product(range(p),repeat=4) if det(a)}
    NH=[a for a in PG if {cj(a,h) for h in H}==H]
    assert set(NH)==H
    def order(a):
        b=one
        for k in range(1,p+2):
            b=mul(b,a)
            if b==one:return k
        raise AssertionError(a)
    cen=[a for a in PG if cj(a,S)==S]
    candidates={a for a in G if order(a)==3 and order(mul(S,a))==p}
    orbit={cj(a,R) for a in cen}
    assert candidates==orbit
    H_orbit={frozenset(cj(a,h) for h in H) for a in PG}
    H_candidates={frozenset(closure([S,a])) for a in G if order(a)==3 and order(mul(S,a))=={7:4,11:5}[p]}
    assert H_candidates<=H_orbit
    reps=[];index={}
    for a in sorted(G):
        if a in index:continue
        cos={mul(h,a) for h in H};i=len(reps);reps.append(a)
        for q in cos:index[q]=i
    factors=[]
    for inertia,e in [(S,2),(R,3)]:
        fixed=[i for i,g in enumerate(reps) if index[mul(g,inertia)]==i]
        C={one};v=inertia
        for k in range(1,e):C.add(v);v=mul(v,inertia)
        N=[g for g in G if {cj(g,a) for a in C}==C]
        rows=[]
        for i in fixed:
            g=reps[i]
            stab=[a for a in N if index[mul(g,a)]==i]
            orbit={index[mul(g,a)] for a in N}
            assert orbit<=set(fixed)
            rows.append({'left_coset_representative':g,'stabilizer_order':len(stab),'orbit_size':len(orbit),'stabilizer_matrices':sorted(stab)})
        assert sorted(row['orbit_size'] for row in rows)==({7:{2:[1,2,2],3:[1]},11:{2:[3,3,3],3:[2,2]}}[p][e])
        factors.append({'inertia_order':e,'normalizer_order':len(N),'points':rows})
    return {'prime':p,'PSL_order':len(G),'subgroup_order':len(H),'PGL_normalizer_order':len(NH),
            'standard_kernel_unique_for_generating_2_3_p_pairs':True,'fixed_S_pair_count':len(candidates),
            'PGL_subgroup_orbit_size':len(H_orbit),'all_triangle_subgroups_checked':len(H_candidates),
            'H_generators':[S,norm(bmat)],'S':S,'R':R,'factor_domains':factors}

def degree7_passport():
    identity=tuple(range(7))
    def mul(a,b):return tuple(b[i] for i in a)
    def inv(a):return tuple(a.index(i) for i in identity)
    def cycles(a):
        remaining=set(identity);out=[]
        while remaining:
            start=remaining.pop();n=1;i=a[start]
            while i!=start:remaining.remove(i);n+=1;i=a[i]
            out.append(n)
        return sorted(out)
    r=(1,2,0,4,5,3,6)
    transpositions=set()
    for a,b,c,d in permutations(identity,4):
        q=list(identity);q[a],q[b]=b,a;q[c],q[d]=d,c
        transpositions.add(tuple(q))
    valid={s for s in transpositions if cycles(mul(s,r))==[7]}
    centralizer=[a for a in permutations(identity) if mul(a,r)==mul(r,a)]
    rows=[]
    while valid:
        s=min(valid);orbit={mul(mul(inv(a),s),a) for a in centralizer}
        valid-=orbit;G={identity};todo=[identity]
        for a in todo:
            for b in [s,r]:
                q=mul(a,b)
                if q not in G:G.add(q);todo.append(q)
        rows.append({'orbit_size':len(orbit),'group_order':len(G),'s':s,'r':r})
    assert len(rows)==2 and all(row['group_order']==168 for row in rows)
    return rows

out={'degree7_passport_classes':degree7_passport(),
     'degree7':{'quadratic_field_relation':'eta^2=-7','b':'(11+eta)/56',
               'P':'t*(t^2+t+b)^3','Q':'7*t^2+4*t+b',
               'R':'-351/3294172-27*eta/470596','j':'1728*P/R',
               'order2_rational_point':'(-11+eta)/14',
               'order2_quadratic':'t^2+(15+eta)*t/14+27*(3+eta)/392',
               'quadratic_discriminant':'(14-6*eta)/49','discriminant_numerator_norm':448,
               'order3_point':'0','filling_coordinate':'1728*t/a'},
     'degree11':{'quadratic_field_relation':'w^2-w+3=0','P3':str(P11),'P1':str(L11),
                 'Q2':str(Q11),'Q1':str(E11r),'j':'-P3^3*P1',
                 'quadratic_discriminant':str(disc11),'quadratic_discriminant_norm':297,
                 'cubic_irreducibility_prime':5,'residue_w':2,'cubic_values_mod5':mod5,
                 'filling_coordinate':'1728*(z-b)/(a-b)','field':'Q(w,a,b), Q1(a)=P1(b)=0',
                 'field_degree_over_Q':12},
     'finite_domains':[finite(7,(2,4,1,6)),finite(11,(3,4,1,9))],
     'all_exact_checks_passed':True,
     'scope':'Explicit covers, fillings, fields and finite domain tests; no arbitrary-pentagon fixedness asserted'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
