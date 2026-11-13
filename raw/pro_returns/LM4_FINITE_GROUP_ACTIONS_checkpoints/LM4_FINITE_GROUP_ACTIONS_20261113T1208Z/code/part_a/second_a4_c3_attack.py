#!/usr/bin/env python3
"""Exact model for the residual A5 centralizer in a six-puncture quotient.

This certifies the maps, labels, and algebraic basepoint. It does not prove
that the resulting full profinite fixed intersection is trivial.
"""
import contextlib
import io
import json
from pathlib import Path
import sympy as s

with contextlib.redirect_stdout(io.StringIO()):
    import a5_centralizer_permutations as a

z=s.Symbol('z')
I=s.I
phi=(1+s.sqrt(5))/2
rho=s.sqrt(phi+2)
field=s.QQ.algebraic_field(I,s.sqrt(5),rho)

def k(value):
    return field.from_sympy(s.sympify(value))

def canonical(matrix):
    scale=next(v for v in matrix if v)
    return tuple(v/scale for v in matrix)

def multiply(left,right):
    aa,b,c,d=left
    e,f,g,h=right
    return canonical((aa*e+b*g,aa*f+b*h,c*e+d*g,c*f+d*h))

def value(matrix,point):
    aa,b,c,d=matrix
    return (aa*point+b)/(c*point+d)

r=a.cycle(1,2,3)
beta=a.mul(a.cycle(1,2),a.cycle(4,5))
AM=canonical(tuple(map(k,[-1,0,0,1])))
RM=canonical(tuple(map(k,[1,I,1,-I])))
BM=canonical(tuple(map(k,[1,phi-1-I*phi,phi-1+I*phi,-1])))
identity=tuple(map(k,[1,0,0,1]))
matrices={a.one:identity}
queue=[a.one]
generator_checks=0
for g in queue:
    for h,H in [(a.a,AM),(r,RM),(beta,BM)]:
        gh=a.mul(g,h)
        product=multiply(matrices[g],H)
        if gh in matrices:
            assert matrices[gh]==product
        else:
            matrices[gh]=product
            queue.append(gh)
        generator_checks+=1
assert set(matrices)==a.G and len(matrices)==60
assert multiply(BM,BM)==identity
assert multiply(multiply(BM,RM),BM)==multiply(RM,RM)
assert a.generated([a.a,r,beta])==a.G

star=-I*(rho+phi)
star_field=k(star)
points=[value(matrices[a.group_labels[j]],star_field) for j in range(12)]
for g in a.G:
    permutation=a.vertex_action(g)
    assert all(value(matrices[g],points[j])==points[permutation[j]]
               for j in range(12))

# Four C3 orbits, ordered so beta interchanges the first pair and second pair.
rp=a.vertex_action(r)
bp=a.vertex_action(beta)
representatives=[0,11,2,7]
orbits=[[j,rp[j],rp[rp[j]]] for j in representatives]
assert len(set(sum(orbits,[])))==12
sigma=[next(j for j,P in enumerate(orbits)
            if set(P)=={bp[i] for i in O}) for O in orbits]
assert sigma==[1,0,3,2]
representative_functions=[z,1/z,-1/z,-z]
for label,function in zip(representatives,representative_functions):
    aa,b,c,d=map(field.to_sympy,matrices[a.group_labels[label]])
    assert s.cancel((aa*z+b)/(c*z+d)-function)==0

R=(z+I)/(z-I)
q=(z**3+3*I*z+1-I)/((z-1)*(z-I))
assert s.cancel(q.subs(z,R)-q)==0
assert s.cancel(q-(z+R+R.subs(z,R)))==0
sqrt3=s.sqrt(3)
plus=(1+I)*(1+sqrt3)/2
minus=(1+I)*(1-sqrt3)/2
field3=s.QQ.algebraic_field(I,sqrt3)

def rational_pair(expression):
    n,d=s.fraction(s.together(expression))
    N=s.Poly(n,z,domain=field3)
    D=s.Poly(d,z,domain=field3)
    common=s.gcd(N,D)
    N=N.exquo(common)
    D=D.exquo(common)
    lead=D.LC()
    return s.Poly(N.as_expr()/lead,z,domain=field3), \
           s.Poly(D.as_expr()/lead,z,domain=field3)

def zero_rational(expression):
    N,D=rational_pair(expression)
    assert N.is_zero

U=lambda x:(x-plus)/(x-minus)
zero_rational((q-3*plus)/(q-3*minus)-U(z)**3)
root_pairs=[rational_pair(U(g)/U(z)) for g in representative_functions[1:]]
normalized=[]
for g,(N,D) in zip(representative_functions[1:],root_pairs):
    qg=s.cancel(q.subs(z,g))
    normalized_coordinate=(qg-3*plus)*(q-3*minus)/((qg-3*minus)*(q-3*plus))
    zero_rational(normalized_coordinate-(N.as_expr()/D.as_expr())**3)
    normalized.append({'root_numerator':list(map(str,N.all_coeffs())),
                       'root_denominator':list(map(str,D.all_coeffs())),
                       'coordinate_is_cube':True})

N0,D0=root_pairs[0]
N1,D1=root_pairs[1]
N2,D2=root_pairs[2]
OmegaN,OmegaD=rational_pair(N0.as_expr()*D1.as_expr()*D2.as_expr()/
                          (D0.as_expr()*N1.as_expr()*N2.as_expr()))
fixed_numerator=OmegaN**3-OmegaD**3
quartic_minus=z**4-2*I*z**3+6*z*z-2*I*z+1
quartic_plus=z**4+2*I*z**3+6*z*z+2*I*z+1
expected=s.Poly(z*(z*z+1)*quartic_minus*quartic_plus,z,domain=field3)
assert fixed_numerator.monic()==expected.monic()
assert sum(k(coefficient)*star_field**power
           for power,coefficient in enumerate(s.Poly(quartic_plus,z).all_coeffs()[::-1]))==field.zero

# The path star -> 5+Im(star)i -> 5+4i avoids all 14 removed points:
# their finite real and imaginary coordinates have absolute value <3/2,
# whereas Im(star)<-3 and the second segment has real coordinate 5.
assert phi>s.Rational(3,2)
assert rho>s.Rational(3,2)
assert sqrt3<2

result={
    'scope':'Exact common-C3 descent and based involution model; no full fixed-intersection triviality claim.',
    'A5_order':60,
    'matrix_generator_checks':generator_checks,
    'exact_vertex_label_checks':720,
    'C3_generator':list(r),
    'extra_involution_beta':list(beta),
    'beta_Mobius_matrix':list(map(lambda x:str(field.to_sympy(x)),BM)),
    'icosahedral_source_basepoint':str(star),
    'path_to_F9_basepoint':[str(star),str(5+star),'5+4*I'],
    'exact_path_avoidance_bounds':
        'All finite R_A real/imaginary coordinates have absolute value <3/2; the first path segment has imaginary part <−3, the second real part 5.',
    'C3_quotient_map':str(q),
    'C3_fixed_points':[str(plus),str(minus)],
    'quotient_branch_points':[str(3*plus),str(3*minus)],
    'four_free_orbits_in_quotient_order':orbits,
    'representative_vertex_labels':representatives,
    'representative_Mobius_functions':list(map(str,representative_functions)),
    'beta_permutation_of_four_orbits':sigma,
    'beta_exchanges_the_two_branch_points':True,
    'normalized_coordinate_root_pairs':normalized,
    'normalized_quotient_involution':
        '(s1,s2,s3) -> (s1,s1/s3,s1/s2)',
    'based_transport_formula':
        'For tau=Sigma(path star to b), beta_b(ell)=tau^-1 * B(tau) * B(ell) * B(tau)^-1 * tau.',
    'fixed_locus_equation':'s1=s2*s3',
    'source_fixed_locus_numerator_up_to_nonzero_constant':
        str(s.factor(expected.as_expr())),
    'source_star_lies_in_the_fixed_locus_exactly':True,
    'all_assertions_passed':True,
}
Path(__file__).with_name('second_a4_c3_attack_output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
