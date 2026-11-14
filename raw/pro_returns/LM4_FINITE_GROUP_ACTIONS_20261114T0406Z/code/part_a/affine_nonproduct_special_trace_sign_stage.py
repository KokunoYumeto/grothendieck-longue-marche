"""Exact rank-one special-projector traces and first-character sign parts.

For (r,h)->(-r,-h), the odd Laurent terms are obtained by exponent
parity. This is the half difference in odd characteristic; no division
by 2 is used to define the integer Laurent polynomial.
"""
from pathlib import Path
from hashlib import sha256
import json
import runpy
import sympy as sp


def main():
    script = Path(__file__).resolve()
    folder = script.parent
    vectors = folder/'affine_nonproduct_rank_one_special_roots_stage_output.json'
    outer = folder/'affine_nonproduct_source_zero_stage_output.json'
    helper = folder/'affine_four_parameter_extension_independent_audit.py'
    product = folder/'affine_full_product_one_independent_audit.py'
    data, factor = json.loads(vectors.read_text()), json.loads(outer.read_text())
    old, sparse = runpy.run_path(str(helper)), runpy.run_path(str(product))
    names = ['r', 'h', 't', 'u', 'v', 'w', 'z']
    old['configure'](names, [[1, 0, 0, 0, 0, 0, 0], [-1, 1, -1, -1, -1, -1, -1]]+[
        [int(i == j) for i in range(7)] for j in range(2, 7)])
    parse, pm = old['parse'], old['parse_matrix']
    parse.__globals__['UNITS']['s'] = parse('h/(r*t*u*v*w*z)')
    variables = sp.symbols(' '.join(names))

    def expression(poly):
        return sp.Add(*(a*sp.prod(x**n for x, n in zip(variables, e)) for e, a in poly.items()))

    def packed(poly):
        return [[a, list(e)] for e, a in sorted(poly.items())]

    q = pm([factor['row_q']])
    records = []
    for record in data['records']:
        column = [[{tuple(exponent): coefficient for coefficient, exponent in poly}] for poly in record['image']]
        trace = sparse['mm'](q, column)[0][0]
        odd = {e: c for e, c in trace.items() if (e[0]+e[1]) % 2}
        even = {e: c for e, c in trace.items() if (e[0]+e[1]) % 2 == 0}
        assert sparse['plus'](odd, even) == trace
        conjugate = {e: (-c if (e[0]+e[1]) % 2 else c) for e, c in trace.items()}
        assert sparse['plus'](trace, sparse['neg'](conjugate)) == sparse['times'](parse('2'), odd)
        out = {'index': record['index'], 'label': record['label'],
               'roots_of_P': record['base_roots'], 'special_root': record['special_root'],
               'trace_q_P_T_a': packed(trace), 'odd_part': packed(odd),
               'trace_factored': str(sp.factor(expression(trace))),
               'odd_part_factored': str(sp.factor(expression(odd)))}
        records.append(out)
        print(json.dumps({'index': record['index'], 'trace_monomials': len(trace),
                          'odd_monomials': len(odd), 'odd_part_factored': out['odd_part_factored']}), flush=True)
    output = script.with_name('affine_nonproduct_special_trace_sign_stage_output.json')
    result = {'status': 'PASS_EXACT_SPECIAL_TRACE_SIGN_PARTS',
              'producer_sha256': sha256(script.read_bytes()).hexdigest(),
              'inputs': {str(p): sha256(p.read_bytes()).hexdigest() for p in [vectors, outer, helper, product]},
              'variables': names, 'records': records,
              'scope': 'Exact structured rank-one trace and sign-parity identities. Their common nonvanishing locus and any all-field module consequence require separate proof.'}
    output.write_text(json.dumps(result, separators=(',', ':'))+'\n')
    print(json.dumps({'status': result['status'], 'output_sha256': sha256(output.read_bytes()).hexdigest()}), flush=True)


if __name__ == '__main__':
    main()
