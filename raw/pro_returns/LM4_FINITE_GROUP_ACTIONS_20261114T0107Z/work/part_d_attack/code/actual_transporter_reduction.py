#!/usr/bin/env python3
"""Actual standard pants quotient and its mod-two homology refinement.

All groups used here are quotients of P3=C2(a)*C2(b)*C2(d), with
x=ba, y=da, alpha=Inn(a), h=1. The large refinement is represented
by exact binary edge chains; it is never replaced by an arbitrary
semidirect-product element outside the indicated chain subgroup.
"""
from itertools import permutations
from math import gcd, lcm
from collections import deque
from pathlib import Path
import json

G = [p for p in permutations(range(5))
     if sum(p[i] > p[j] for i in range(5) for j in range(i+1, 5)) % 2 == 0]
index = {g: i for i, g in enumerate(G)}
one = index[tuple(range(5))]
T = [[index[tuple(p[q[i]] for i in range(5))] for q in G] for p in G]
inverse = [index[tuple(p.index(i) for i in range(5))] for p in G]

def cyc(*cycles):
    p = list(range(5))
    for cycle in cycles:
        for old, new in zip(cycle, cycle[1:] + cycle[:1]):
            p[old-1] = new-1
    return index[tuple(p)]

def generated(gens):
    seen, todo = {one}, [one]
    while todo:
        old = todo.pop()
        for g in gens:
            new = T[old][g]
            if new not in seen:
                seen.add(new); todo.append(new)
    return seen

def gpow(g, n):
    if n < 0:
        return gpow(inverse[g], -n)
    result = one
    while n:
        if n & 1:
            result = T[result][g]
        g = T[g][g]; n >>= 1
    return result

def order(g):
    n, value = 1, g
    while value != one:
        n += 1; value = T[value][g]
    return n

def conjugate(g, u):
    return T[T[u][g]][inverse[u]]

a = cyc([1, 2], [3, 4])
b = cyc([1, 3], [2, 5])
d = cyc([1, 4], [2, 3])
x, y = T[b][a], T[d][a]
z = inverse[T[x][y]]
checks = []

def check(name, condition):
    assert condition, name
    checks.append({'name': name, 'passed': True})

check('A5_and_both_actual_generating_sets', len(G) == 60 and
      len(generated([a, b, d])) == len(generated([x, y])) == 60)
check('base_involution_and_inversion_relations', all(order(t) == 2 for t in [a, b, d])
      and conjugate(x, a) == inverse[x] and conjugate(y, a) == inverse[y])
check('actual_z_endpoint_relations', conjugate(z, b) == inverse[z]
      and T[z][b] == conjugate(d, inverse[y]))
exponent = lcm(*(order(g) for g in range(60)))
check('base_exponent30', exponent == 30)

# Actual finite E quotient A=A5 x C2^3. Parity is the sum of the bits.
def pmul(first, second):
    return T[first[0]][second[0]], first[1] ^ second[1]

def pinv(element):
    return inverse[element[0]], element[1]

def ppow(element, n):
    if n < 0:
        return ppow(pinv(element), -n)
    value = (one, 0)
    while n:
        if n & 1:
            value = pmul(value, element)
        element = pmul(element, element); n >>= 1
    return value

def pconj(element, u):
    return pmul(pmul(u, element), pinv(u))

def pgenerate(gens):
    seen, todo = {(one, 0)}, [(one, 0)]
    while todo:
        old = todo.pop()
        for gen in gens:
            new = pmul(old, gen)
            if new not in seen:
                seen.add(new); todo.append(new)
    return seen

SA, SB, SD = (a, 1), (b, 2), (d, 4)
PX, PY = pmul(SB, SA), pmul(SD, SA)
PZ = pinv(pmul(PX, PY))
Hbase = pgenerate([PX, PY])
Abase = pgenerate([SA, SB, SD])
check('actual_full_finite_quotient_and_parity_kernel',
      len(Abase) == 480 and len(Hbase) == 240 and
      Hbase == {g for g in Abase if g[1].bit_count() % 2 == 0})
check('actual_endpoint_transporters_u1_and_u2',
      pconj(SB, (one, 0)) == SB and
      pconj(SD, pinv(PY)) == pmul(PZ, SB))
centralizer_sizes = [sum(pconj(t, g) == t for g in Hbase) for t in [SA, SB, SD]]
check('finite_section_centralizers_retain_sixteen_elements', centralizer_sizes == [16,16,16])
inverters = [g for g in Abase if g[1].bit_count() % 2 == 1 and pconj(PZ,g) == pinv(PZ)]
peripheral_image = pgenerate([PZ, SB])
check('exact_finite_cusp_and_inverter_image_sizes',
      len(peripheral_image) == 20 and len(inverters) == 20 and
      sum(g[1].bit_count()%2 == 1 for g in peripheral_image) == 10)

# An edge (g,j) goes from g to g*generator[j]; x edges precede y edges.
generators = [x, y]
edges = 120
edge_target = [T[g][generators[j]] for j in range(2) for g in range(60)]

def boundary(chain):
    out = 0
    while chain:
        low = chain & -chain; edge = low.bit_length()-1
        origin = edge % 60
        out ^= (1 << origin) ^ (1 << edge_target[edge])
        chain ^= low
    return out

shift_perms = [[j*60 + T[g][h] for j in range(2) for h in range(60)]
               for g in range(60)]

def shift(g, chain):
    out = 0
    perm = shift_perms[g]
    while chain:
        low = chain & -chain; edge = low.bit_length()-1
        out ^= 1 << perm[edge]; chain ^= low
    return out

def cmul(first, second):
    v, g = first; w, h = second
    return v ^ shift(g, w), T[g][h]

def cinv(element):
    v, g = element
    return shift(inverse[g], v), inverse[g]

def cpow(element, n):
    if n < 0:
        return cpow(cinv(element), -n)
    value = (0, one)
    while n:
        if n & 1:
            value = cmul(value, element)
        element = cmul(element, element); n >>= 1
    return value

X, Y = (1 << one, x), (1 << (60+one), y)
Z = cinv(cmul(X, Y))
paths = {one: 0}
todo = deque([one])
tree_edges = set()
while todo:
    g = todo.popleft()
    for j, gen in enumerate(generators):
        target = T[g][gen]
        if target not in paths:
            edge = 60*j+g
            paths[target] = paths[g] ^ (1 << edge)
            tree_edges.add(edge); todo.append(target)
cycle_basis = [paths[g] ^ (1 << (60*j+g)) ^ paths[T[g][gen]]
               for j, gen in enumerate(generators) for g in range(60)
               if 60*j+g not in tree_edges]

def binary_basis(vectors):
    pivots = {}
    for i, vec in enumerate(vectors):
        coeff = 1 << i
        while vec:
            pivot = vec.bit_length()-1
            if pivot not in pivots:
                pivots[pivot] = (vec, coeff)
                break
            vec ^= pivots[pivot][0]; coeff ^= pivots[pivot][1]
    return pivots

def solve(pivots, target):
    coeff = 0
    while target:
        pivot = target.bit_length()-1
        if pivot not in pivots:
            return None
        target ^= pivots[pivot][0]; coeff ^= pivots[pivot][1]
    return coeff

def combine(coeff, vectors):
    result = 0
    while coeff:
        low = coeff & -coeff; i = low.bit_length()-1
        result ^= vectors[i]; coeff ^= low
    return result

check('Schreier_tree_and_cycle_basis', len(paths) == 60 and len(tree_edges) == 59
      and len(cycle_basis) == len(binary_basis(cycle_basis)) == 61)
check('all_Schreier_chains_have_the_exact_boundary', all(
    boundary(paths[g]) == ((1 << one) ^ (1 << g)) for g in range(60)))
check('all_kernel_basis_chains_are_cycles', all(boundary(v) == 0 for v in cycle_basis))
check('cycle_space_is_the_whole_boundary_kernel',
      len(binary_basis([boundary(1 << i) for i in range(120)])) == 59)

# alpha=delta reverses each labelled edge and acts by Inn(a) on vertices.
alpha_g = [conjugate(g, a) for g in range(60)]
alpha_edges = [60*j+T[alpha_g[g]][inverse[gen]]
               for j, gen in enumerate(generators) for g in range(60)]

def alpha_chain(chain):
    result = 0
    while chain:
        low = chain & -chain; edge = low.bit_length()-1
        result ^= 1 << alpha_edges[edge]; chain ^= low
    return result

check('actual_alpha_on_chain_cover', len(set(alpha_edges)) == 120 and
      all(alpha_edges[alpha_edges[i]] == i for i in range(120)) and
      (alpha_chain(X[0]), alpha_g[X[1]]) == cinv(X) and
      (alpha_chain(Y[0]), alpha_g[Y[1]]) == cinv(Y))
check('alpha_preserves_every_kernel_cycle', all(boundary(alpha_chain(v)) == 0
                                              for v in cycle_basis))

def abelian_label(chain):
    return (chain & ((1 << 60)-1)).bit_count() % 2, (chain >> 60).bit_count() % 2

check('refinement_maps_onto_named_mod2_abelianization',
      len(binary_basis([abelian_label(v)[0] + 2*abelian_label(v)[1]
                        for v in cycle_basis])) == 2)

# The exponent is obtained from all 60 cosets and all 61 kernel directions.
refined_exponent = 1
for g in range(60):
    r = order(g)
    term = cpow((paths[g], g), r)[0]
    varying = any(cpow((paths[g] ^ v, g), r)[0] != 0 for v in cycle_basis)
    refined_exponent = lcm(refined_exponent, 2*r if term or varying else r)
check('refined_exponent60', refined_exponent == 60)

base_rows = []
for m in range(2*exponent):
    if gcd(m, 2*exponent) != 1:
        continue
    k = (m-1)//2
    defect = T[T[gpow(x, k)][gpow(z, k)]][gpow(y, k)]
    lhs, rhs = T[gpow(x, m)][gpow(y, m)], gpow(T[x][y], m)
    conjugators = [u for u in range(60) if conjugate(rhs, u) == lhs]
    base_rows.append({'m_mod60': m, 'k_mod30': k, 'defect_index': defect,
                      'T_member': defect == one,
                      'B_conjugator_count_in_A5_times_C2_squared': 4*len(conjugators),
                      'A5_conjugator_indices': conjugators})

base_units = [row['m_mod60'] for row in base_rows]
check('all_unit_distinguished_pairs_generate_the_same_actual_parity_kernel',
      all(pgenerate([ppow(PX,m),ppow(PY,m)]) == Hbase for m in base_units))
check('defect_changes_sign_by_actual_alpha', all(
      conjugate(T[T[gpow(x,(m-1)//2)][gpow(z,(m-1)//2)]][gpow(y,(m-1)//2)],a)
      == T[T[gpow(x,(-m-1)//2)][gpow(z,(-m-1)//2)]][gpow(y,(-m-1)//2)]
      for m in base_units))
reflection_checks = []
for row in base_rows:
    m,k = row['m_mod60'],row['k_mod30']
    old = pmul(pmul(ppow(PX,k),ppow(PZ,k)),ppow(PY,k))
    for j in range(exponent):
        u1 = ppow(PZ,j)
        u2 = pmul(ppow(PZ,j),pinv(PY))
        new = pmul(pmul(pmul(pmul(ppow(PX,k),pinv(u1)),ppow(PZ,k)),u2),ppow(PY,k+1))
        reflection_checks.append(new == old)
check('all_480_reflection_choice_comparisons_are_literal_equalities', all(reflection_checks))
check('every_T_residue_has_the_specified_normalized_conjugator', all(
      not row['T_member'] or
      pconj(ppow(pmul(PX,PY),row['m_mod60']),ppow(PX,row['k_mod30']))
      == pmul(ppow(PX,row['m_mod60']),ppow(PY,row['m_mod60']))
      for row in base_rows))

refined_rows = []
for m in range(2*refined_exponent):
    if gcd(m, 2*refined_exponent) != 1:
        continue
    lhs = cmul(cpow(X, m), cpow(Y, m))
    rhs = cpow(cmul(X, Y), m)
    linear = binary_basis([v ^ shift(lhs[1], v) for v in cycle_basis])
    solutions = []
    for g in range(60):
        if conjugate(rhs[1], g) != lhs[1]:
            continue
        target = lhs[0] ^ shift(g, rhs[0]) ^ paths[g] ^ shift(lhs[1], paths[g])
        coeff = solve(linear, target)
        if coeff is None:
            continue
        chain = paths[g] ^ combine(coeff, cycle_basis)
        u = (chain, g)
        assert boundary(chain) == ((1 << one) ^ (1 << g))
        assert cmul(cmul(u, rhs), cinv(u)) == lhs
        solutions.append({'g_index': g, 'chain_hex': hex(chain),
                          'abelian_label': abelian_label(chain)})
    k = (m-1)//2
    defect = cmul(cmul(cpow(X, k), cpow(Z, k)), cpow(Y, k))
    refined_rows.append({'m_mod120': m, 'base_residue_mod60': m % 60,
                         'B_nonempty': bool(solutions),
                         'solution_coset_count': len(solutions),
                         'solutions_per_base_coset': 1 << (61-len(linear)),
                         'one_chain_per_solution_coset': solutions,
                         'T_member': defect == (0, one),
                         'defect_chain_hex': hex(defect[0]),
                         'defect_group_index': defect[1]})

base_B = [r['m_mod60'] for r in base_rows if r['B_conjugator_count_in_A5_times_C2_squared']]
base_T = [r['m_mod60'] for r in base_rows if r['T_member']]
refined_B = [r['m_mod120'] for r in refined_rows if r['B_nonempty']]
refined_T = [r['m_mod120'] for r in refined_rows if r['T_member']]
check('exact_base_B_and_T_residues',
      base_B == [1,11,19,29,31,41,49,59] and base_T == [1,19,41,59])
check('exact_refined_B_and_T_residues',
      refined_B == [1,19,41,59,61,79,101,119] and refined_T == [1,41,79,119])
check('actual_homology_refinement_removes_all_four_extra_base_residues',
      sorted({m % 60 for m in refined_B}) == base_T)
check('all_refined_nonempty_B_fibres_have_40960_conjugators', all(
      not row['B_nonempty'] or row['solution_coset_count']*row['solutions_per_base_coset'] == 40960
      for row in refined_rows))

out = {'status': 'PASS', 'scope': 'Actual standard P3 quotient and actual homology-cover refinement',
       'base_group': 'A5 times C2^3; parity kernel A5 times C2^2',
       'base_group_A5_permutations': G,
       'a_b_d_x_y_z_indices': [a,b,d,x,y,z],
       'identity_index': one,
       'base_parity_exponent': exponent,
       'base_total_order': len(Abase), 'base_parity_order': len(Hbase),
       'base_section_centralizer_sizes_in_parity_kernel': centralizer_sizes,
       'base_original_cusp_image_order': len(peripheral_image),
       'base_outside_inverter_count': len(inverters),
       'refined_parity_group_order': 60*(1 << 61),
       'refined_parity_exponent': refined_exponent,
       'tree_edges': sorted(tree_edges),
       'tree_chains_hex': [hex(paths[g]) for g in range(60)],
       'Schreier_cycle_basis_hex': [hex(v) for v in cycle_basis],
       'base_rows': base_rows, 'refined_rows': refined_rows,
       'base_B_unit_residues': base_B, 'base_T_unit_residues': base_T,
       'refined_B_unit_residues': refined_B, 'refined_T_unit_residues': refined_T,
       'checks': checks, 'assertion_count': len(checks)}
target = Path(__file__).with_name('actual_transporter_reduction_output.json')
target.write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps(out, indent=2))
