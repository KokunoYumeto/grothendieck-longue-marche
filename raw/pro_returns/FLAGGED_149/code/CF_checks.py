#!/usr/bin/env python3
"""Exact finite and symbolic checks for C and F9/F17. No numerical inference."""
import itertools
import json
from pathlib import Path
import sympy as sp

x, t, X, Y, V, W, z, lam = sp.symbols("x t X Y V W z lam")
out = {}

# F17.2: smooth generic sextic, two smooth elliptic components, chart identities.
sextic = (x**3-t**6)*(x**3-1)
disc = sp.factor(sp.discriminant(sextic, x))
assert sp.expand(disc-729*t**12*(1-t**6)**6) == 0
inner = sp.expand(sextic.subs(x,t**2*X)/t**6)
assert sp.expand(inner-(X**3-1)*(t**6*X**3-1)) == 0
inner_disc = sp.discriminant(1-X**3, X)
outer_disc = sp.discriminant(x*(x**3-1), x)
assert inner_disc != 0 and outer_disc != 0
out["genus2"] = {
    "generic_discriminant": str(disc),
    "inner_equation_rhs": str(sp.factor(inner)),
    "inner_component_discriminant": str(inner_disc),
    "outer_component_discriminant": str(outer_disc),
    "node_unit_A_at_origin": -1,
    "generic_genus_by_six_branch_points": 2,
    "component_genera": [1,1],
    "dual_graph_vertices_edges_betti": [2,1,0],
}

# F17.3: free nilpotent class-two exponent-p group on three generators.
# Coordinates a^u b^v c^w [a,b]^r [a,c]^s [b,c]^h.
p = 5
def mul(g,h):
    v,q = g[:3],h[:3]
    correction = (-v[1]*q[0],-v[2]*q[0],-v[2]*q[1])
    return tuple((v[i]+q[i])%p for i in range(3)) + tuple(
        (g[i+3]+h[i+3]+correction[i])%p for i in range(3))
def inv(g):
    v = g[:3]
    return tuple(-a%p for a in v) + tuple(
        (-g[i+3]-b)%p for i,b in enumerate((v[0]*v[1],v[0]*v[2],v[1]*v[2])))
def conj(g,h):
    return mul(mul(g,h),inv(g))
def comm(g,h):
    return mul(conj(g,h),inv(h))
one = (0,)*6
gens = [tuple(int(i==j) for i in range(6)) for j in range(3)]
a,b,c = gens
ab=mul(a,b)
target=[conj(ab,a),conj(ab,b),c]
expected=[(1,0,0,4,0,0),(0,1,0,1,0,0),(0,0,1,0,0,0)]
assert target == expected
for g in [a,b,c,ab,*target]:
    assert mul(g,inv(g)) == one and mul(inv(g),g) == one
inners=[]
for vv in itertools.product(range(p),repeat=3):
    g=vv+(0,0,0)
    if [conj(g,h) for h in gens] == target:
        inners.append(vv)
assert inners == []
# The two first generator equations force abelian coordinates (1,1,0).
first_two=[]
for vv in itertools.product(range(p),repeat=3):
    g=vv+(0,0,0)
    if [conj(g,h) for h in gens[:2]] == target[:2]:
        first_two.append(vv)
assert first_two == [(1,1,0)]
assert conj(ab,c) == (0,0,1,0,1,1)
out["four_punctures_class_two"] = {
    "prime":p,"group_order":p**6,
    "target_generator_images":target,
    "abelianization_identity":all(target[i][:3] == gens[i][:3] for i in range(3)),
    "possible_inner_abelian_coordinates_tested":p**3,
    "inner_matches":inners,
    "matches_first_two":first_two,
    "forced_inner_image_of_c":conj(ab,c),
}

# F17.4: five lines force five geometric cusps under nonlinear inertia recognition.
vectors=[sp.Matrix(v) for v in [(1,0,0),(0,1,0),(0,0,1),(-1,-1,-1),(1,1,0)]]
ranks=[sp.Matrix.hstack(vectors[i],vectors[j]).rank()
       for i in range(5) for j in range(i+1,5)]
assert ranks == [2]*10
out["five_cyclotomic_lines"]={"vectors":[list(v) for v in vectors],
                              "pairwise_ranks":ranks,"max_cusps_rank3":4}

# F17.5: quadratic twist substitution.
r=sp.symbols("r")
twist_identity=sp.expand((t*r*Y)**2-(t*X)**3+t**2*(t*X))
twist_identity=sp.expand(twist_identity.subs(r**2,t))
assert sp.expand(twist_identity-t**3*(Y**2-X**3+X)) == 0
out["elliptic_twist"]={"substitution":"x=tX, y=t*r*Y, r^2=t",
                       "equation_after_substitution":str(sp.factor(twist_identity)),
                       "involution_on_Y":"Y -> -Y"}

# F9.3: j invariants differ at transcendental lambda.
j=lambda q:256*(1-q+q*q)**3/(q*q*(1-q)**2)
jdiff=sp.factor(j(lam)-j(2*lam))
assert jdiff != 0
out["algebraically_closed_topos_counterexample"]={"j_difference":str(jdiff)}

# C3/C6: Kummer winding convention and tame indices.
mu=6
q=t**mu*(1+t)
assert min(sp.Poly(q,t).as_dict())[0] == mu
assert sp.residue(sp.diff(q,t)/q,t,0)==mu
normal_transition=1/z
conormal_transition=z
normal_winding=sp.residue(sp.diff(normal_transition,z)/normal_transition,z,0)
conormal_winding=sp.residue(sp.diff(conormal_transition,z)/conormal_transition,z,0)
assert (normal_winding,conormal_winding)==(-1,1)
out["kummer_sign_and_multiplicity"]={
    "q":str(q),"q_at_zero":int(q.subs(t,0)),
    "boundary_sections_0_and_q_collide":True,
    "ord_q":mu,"residue_dlog_q":int(sp.residue(sp.diff(q,t)/q,t,0)),
    "O_minus_one_normal_winding":int(normal_winding),
    "dual_conormal_winding":int(conormal_winding),
    "finite_cyclic_index_n60_mu6":int(sp.gcd(60,6)),
    "prime_to_2_index_n105_mu12":int(sp.gcd(105,12)),
}

# F9.4: sample the exact root-count inequality; the proof handles every fixed D.
degree_bounds={}
for D in [0,1,2,3,10,100,1000]:
    N=1
    while N*D+(3**N-1)//2 >= 3**N:
        N+=1
    degree_bounds[D]={"N":N,"bound":N*D+(3**N-1)//2,"field_size":3**N}
out["finite_field_root_count_samples"]=degree_bounds

# C7: the diagonal-cusp example really is a smooth genus-two curve.
out["diagonal_cusp"]={"discriminant_x5_minus_x":str(sp.discriminant(x**5-x,x)),
                      "normal_degree":-2,"class_mod_3":(-2)%3}
assert sp.discriminant(x**5-x,x) != 0

destination=Path(__file__).with_name("CF_checks_output.json")
destination.write_text(json.dumps(out,indent=2,default=str)+"\n")
print(json.dumps(out,indent=2,default=str))
