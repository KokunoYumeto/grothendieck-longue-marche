"""Exploratory exact minors of the actual q-orbit rows on ker(q)."""
from pathlib import Path
from hashlib import sha256
import json
import runpy
import sys
import sympy as sp


def main():
    script = Path(__file__).resolve()
    folder = script.parent
    source = folder/'affine_nonproduct_general_observability_stage_output.json'
    helper = folder/'affine_four_parameter_extension_independent_audit.py'
    product = folder/'affine_full_product_one_independent_audit.py'
    data = json.loads(source.read_text())
    old, sparse = runpy.run_path(str(helper)), runpy.run_path(str(product))
    names = ['r', 'h', 't', 'u', 'v', 'w', 'z']
    old['configure'](names, [[int(i == j) for i in range(7)] for j in range(7)])
    parse = old['parse']
    sys.setrecursionlimit(20000)
    variables = sp.symbols(' '.join(names))
    local = dict(zip(names, variables))
    r, h = variables[:2]
    rows = {rec['index']: [parse(x) for x in rec['qT_basis_first_five_divided_by_r_minus_one']]
            for rec in data['records']}

    def expression(poly):
        return sp.Add(*(coefficient*sp.prod(x**power for x, power in zip(variables, exponent))
                        for exponent, coefficient in poly.items()))

    cleared_pair = [sparse['plus'](a, sparse['times'](parse('r'), b)) for a, b in zip(rows[4], rows[9])]
    pair = []
    for entry in cleared_pair:
        value = sp.factor(sp.cancel(expression(entry)/(h*r-1)))
        polynomial = parse(str(value))
        assert sparse['times'](parse('h*r-1'), polynomial) == entry
        pair.append(polynomial)
    rows['pair4r9'] = pair
    selected = [9, 2, 'pair4r9', 6, 10]
    matrix = [rows[i] for i in selected]
    state = {0: parse('1')}
    counts = []
    for i, row in enumerate(matrix):
        new = {}
        for mask, coefficient in state.items():
            for j, entry in enumerate(row):
                if mask & (1 << j) or not entry:
                    continue
                term = sparse['times'](coefficient, entry)
                if sum(bool(mask & (1 << k)) for k in range(j+1, 5)) % 2:
                    term = sparse['neg'](term)
                target = mask | (1 << j)
                new[target] = sparse['plus'](new.get(target, {}), term)
        state = new
        counts.append(sum(len(p) for p in state.values()))
        print(json.dumps({'prefix_rows': i+1, 'minor_monomial_total': counts[-1]}), flush=True)
    determinant = state.get(31, {})
    factored = str(sp.factor(expression(determinant)))
    output = script.with_name('affine_nonproduct_q_orbit_minor_stage_output.json')
    result = {'status': 'EXACT_EXPLORATORY_Q_ORBIT_MINOR',
              'producer_sha256': sha256(script.read_bytes()).hexdigest(),
              'inputs': {str(p): sha256(p.read_bytes()).hexdigest() for p in [source, helper, product]},
              'variables': names, 'row_order': selected,
              'pair_definition': '(o4+r*o9)/(h*r-1), with exact cleared identity checked in every entry',
              'pair_row': [str(sp.factor(expression(p))) for p in pair],
              'prefix_monomial_counts': counts,
              'determinant': [[c, list(e)] for e, c in sorted(determinant.items())],
              'determinant_factored': factored,
              'scope': 'An exact q-orbit minor and the displayed cleared row operation. Its nonzero field strata remain to be proved; no general observability claim is inferred.'}
    output.write_text(json.dumps(result, separators=(',', ':'))+'\n')
    print(json.dumps({'status': result['status'], 'factored': factored,
                      'output_sha256': sha256(output.read_bytes()).hexdigest()}), flush=True)


if __name__ == '__main__':
    main()
