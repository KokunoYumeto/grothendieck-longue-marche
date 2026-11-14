"""Exact word traces on the original exceptional quadratic sign family.

Original character: (r,t^-1,t,1,1,1,t^2), r^2=-t^-2.
Every coefficient is retained in Z[t^+-1] + r Z[t^+-1].
"""
from pathlib import Path
from hashlib import sha256
import json
import runpy
import sympy as sp


def main():
    script = Path(__file__).resolve()
    folder = script.parent
    source = folder/'affine_nonproduct_boundary_quotient_stage_output.json'
    outer = folder/'affine_nonproduct_source_zero_stage_output.json'
    traces = folder/'affine_nonproduct_general_rank_one_pairings_stage_output.json'
    helper = folder/'affine_four_parameter_extension_independent_audit.py'
    data, factor, trace_data = [json.loads(p.read_text()) for p in [source, outer, traces]]
    old = runpy.run_path(str(helper))
    old['configure'](['r', 'h', 't', 'u', 'v', 'w', 'z'],
                     [[1, 0, 0, 0, 0, 0, 0], [-1, 1, -1, -1, -1, -1, -1]]+[
                         [int(i == j) for i in range(7)] for j in range(2, 7)])
    parse = old['parse']
    parse.__globals__['UNITS']['s'] = parse('h/(r*t*u*v*w*z)')

    def add(a, b):
        out = dict(a)
        for exponent, coefficient in b.items():
            out[exponent] = out.get(exponent, 0)+coefficient
            if not out[exponent]:
                del out[exponent]
        return out

    def monomial(a, b, coefficient):
        parity = a % 2
        half = (a-parity)//2
        return {(parity, b-2*half): coefficient*(-1 if half % 2 else 1)} if coefficient else {}

    def mul(a, b):
        out = {}
        for (ar, at), aa in a.items():
            for (br, bt), bb in b.items():
                out = add(out, monomial(ar+br, at+bt, aa*bb))
        return out

    def mm(a, b):
        out = [[{} for _ in b[0]] for _ in a]
        for i, row in enumerate(a):
            for k, coefficient in enumerate(row):
                for j, other in enumerate(b[k]):
                    out[i][j] = add(out[i][j], mul(coefficient, other))
        return out

    def original(poly):
        out = {}
        for coefficient, (a, b, c, d, e, f, g) in poly:
            out = add(out, monomial(a, -b+c+2*g, coefficient))
        return out

    def chart(poly):
        out = {}
        for (a, b, c, d, e, f, g), coefficient in poly.items():
            out = add(out, monomial(a-b, c+2*g, coefficient*(-1 if b % 2 else 1)))
        return out

    matrices = {rec['index']: [[original(poly) for poly in row]
                              for row in rec['boundary_quotient_matrix_6']]
                for rec in data['records']}
    q = [[chart(parse(x)) for x in factor['row_q']]]
    column = [[chart(parse(x))] for x in factor['column_a']]
    one = {(0, 0): 1}
    ratio = {(0, -2): 1}
    outer_matrix = mm(column, q)
    for i in range(6):
        for j in range(6):
            expected = add(outer_matrix[i][j], ratio if i == j else {})
            assert matrices[0][i][j] == expected
    assert mm(q, column)[0][0] == {(0, 0): 1, (0, -2): -1}
    r, t = sp.symbols('r t')

    def expression(poly):
        return sp.Add(*(coefficient*r**ar*t**at for (ar, at), coefficient in poly.items()))

    q_orbits = {index: mm(q, matrix) for index, matrix in matrices.items()}
    a_orbits = {index: mm(matrix, column) for index, matrix in matrices.items()}
    single = {}
    for record in trace_data['records']:
        index = record['index']
        value = mm(q_orbits[index], column)[0][0]
        expected = chart({tuple(exponent): coefficient for coefficient, exponent in record['exact_laurent_coefficients']})
        assert value == expected
        assert all(ar == 0 for ar, at in value)
        single[str(index)] = str(sp.factor(expression(value)))
    pairs = []
    for i in range(11):
        for j in range(11):
            value = mm(q_orbits[i], a_orbits[j])[0][0]
            odd = {(ar, at): coefficient for (ar, at), coefficient in value.items() if ar == 1}
            if odd:
                pairs.append({'sources_zero_based': [i, j], 'odd_part': str(sp.factor(expression(odd))),
                              'odd_monomial_count': len(odd),
                              'full_value': str(sp.factor(expression(value)))})
    pairs.sort(key=lambda rec: (rec['odd_monomial_count'], rec['sources_zero_based']))
    # Exact cyclic a-module at t=2 in F7[r]/(r^2-5).
    def fadd(a, b):
        return ((a[0]+b[0]) % 7, (a[1]+b[1]) % 7)

    def fneg(a):
        return (-a[0] % 7, -a[1] % 7)

    def fmul(a, b):
        return ((a[0]*b[0]+5*a[1]*b[1]) % 7, (a[0]*b[1]+a[1]*b[0]) % 7)

    def finverse(a):
        denominator = pow((a[0]*a[0]-5*a[1]*a[1]) % 7, -1, 7)
        return (a[0]*denominator % 7, -a[1]*denominator % 7)

    def feval(poly):
        value = [0, 0]
        for (ar, at), coefficient in poly.items():
            value[ar] = (value[ar]+coefficient*pow(2, at % 6, 7)) % 7
        return tuple(value)

    def fbasis(vectors):
        answer, pivots = [], []
        for original_vector in vectors:
            vector = list(original_vector)
            for prior, pivot in zip(answer, pivots):
                scalar = vector[pivot]
                vector = [fadd(a, fneg(fmul(scalar, b))) for a, b in zip(vector, prior)]
            pivot = next((j for j, value in enumerate(vector) if value != (0, 0)), None)
            if pivot is None:
                continue
            scalar = finverse(vector[pivot])
            vector = [fmul(scalar, value) for value in vector]
            answer.append(vector)
            pivots.append(pivot)
        return answer, pivots

    def fimage(matrix, vector):
        out = []
        for row in matrix:
            value = (0, 0)
            for a, b in zip(row, vector):
                value = fadd(value, fmul(a, b))
            out.append(value)
        return out

    finite_matrices = {index: [[feval(poly) for poly in row] for row in matrix]
                       for index, matrix in matrices.items()}
    finite_a = [feval(row[0]) for row in column]
    cyclic, finite_pivots = fbasis([finite_a])
    cyclic_ranks = [len(cyclic)]
    while True:
        generated = cyclic+[fimage(matrix, vector) for matrix in finite_matrices.values() for vector in cyclic]
        new_cyclic, finite_pivots = fbasis(generated)
        cyclic_ranks.append(len(new_cyclic))
        stable = len(cyclic) == len(new_cyclic)
        cyclic = new_cyclic
        if stable:
            break
        assert len(cyclic_ranks) <= 7
    assert all(vector[j] == (0, 0) for vector in cyclic for j in [2, 3, 4])
    result = {
        'status': 'PASS_EXACT_EXCEPTIONAL_SIGN_FAMILY_WORD_TRACES',
        'producer_sha256': sha256(script.read_bytes()).hexdigest(),
        'inputs': {str(p): sha256(p.read_bytes()).hexdigest() for p in [source, outer, traces, helper]},
        'coefficient_ring': 'Z[t,t^-1,r]/(r^2+t^-2)',
        'original_character': ['r', '1/t', 't', '1', '1', '1', 't**2'],
        'chart': {'h': '-1/r', 'd': '1/t**2', 'r_squared': '-1/t**2'},
        'original_exponent_map': '(a,b,c,d,e,f,g) -> r^a*t^(-b+c+2g), reduced by r^2=-t^-2',
        'chart_exponent_map': '(a,b,c,d,e,f,g) -> (-1)^b*r^(a-b)*t^(c+2g), with the same reduction',
        'all_eleven_single_traces': single,
        'nonzero_pair_word_odd_parts': pairs,
        'f49_cyclic_a_module': {'field': 'F7[r]/(r^2-5)', 't': 2,
                               'a': finite_a, 'ranks_by_round': cyclic_ranks,
                               'dimension_over_F49': len(cyclic), 'basis': cyclic,
                               'pivots_zero_based': finite_pivots,
                               'zero_coordinates_zero_based': [2, 3, 4]},
        'scope': 'Exact actual-source algebra on this specified family. The displayed odd word traces require an explicit nonzero-factor argument at a finite-field specialization.'}
    output = script.with_name('affine_nonproduct_exceptional_sign_word_traces_output.json')
    output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': result['status'], 'nonzero_pair_count': len(pairs),
                      'shortest_pairs': pairs[:8], 'f49_cyclic_a_module': result['f49_cyclic_a_module'],
                      'output_sha256': sha256(output.read_bytes()).hexdigest()}, indent=2), flush=True)


if __name__ == '__main__':
    main()
