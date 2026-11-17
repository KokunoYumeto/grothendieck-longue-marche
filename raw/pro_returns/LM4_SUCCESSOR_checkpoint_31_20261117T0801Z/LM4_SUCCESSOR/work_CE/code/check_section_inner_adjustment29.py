#!/usr/bin/env python3
"""Exact cyclic-line division of the actual retained-section corrections.

Reads the parent's complete, separately verified coefficient extraction.
No new relation-orbit enumeration or quotient oracle is used.
"""
from pathlib import Path
from collections import Counter, defaultdict
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
INPUT = ROOT / 'records/root_coarse_corrections29.json'
D = json.loads(INPUT.read_text())

def red(w):
    out = []
    for x in w:
        if out and out[-1] == -x:
            out.pop()
        else:
            out.append(x)
    return tuple(out)

def inv(w):
    return tuple(-x for x in reversed(w))

def sub(w, images):
    return red(y for x in w for y in (images[x] if x > 0 else inv(images[-x])))

def clean(c):
    return Counter({k: v for k, v in c.items() if v})

def module(row):
    return Counter({(tuple(t['retained_word_T']), t['family_index_F11']): t['coefficient']
                    for t in row['module_coefficients']})

def shift(g, z):
    return Counter({(red((*g, *t)), i): n for (t, i), n in z.items()})

def difference(g, z):
    ans = shift(g, z)
    ans.subtract(z)
    return clean(ans)

def serial(z):
    return [{'retained_word_T': list(t), 'family_index_F11': i, 'coefficient': n}
            for (t, i), n in sorted(z.items()) if n]

rows = {(r['section'], r['operator'], r['retained_generator']): r for r in D['rows']}
names = ['m', 'm_inverse', 'v', 'v_inverse']
if set(r['operator'] for r in D['rows']) != set(names):
    raise AssertionError(sorted(set(r['operator'] for r in D['rows'])))
other = {'m': 'm_inverse', 'm_inverse': 'm', 'v': 'v_inverse', 'v_inverse': 'v'}
phi = {s: {i: tuple(rows['old_c_section', s, i]['coarse_head_T']) for i in (1, 2, 3)}
       for s in names}
for s in names:
    for i in (1, 2, 3):
        assert sub(phi[s][i], phi[other[s]]) == (i,)
        assert sub(phi[other[s]][i], phi[s]) == (i,)
        assert tuple(rows['local_C_section', s, i]['coarse_head_T']) == phi[s][i]

out = []
for section in ('old_c_section', 'local_C_section'):
    for s in names:
        ds = {i: module(rows[section, s, i]) for i in (1, 2, 3)}
        # Pull g=phi_s(f) back to the first free basis letter. Every word
        # has a unique decomposition f^n r with r not beginning in f^+-1.
        lines = defaultdict(Counter)
        for (t, i), value in ds[1].items():
            u = sub(t, phi[other[s]])
            n = 0
            j = 0
            while j < len(u) and abs(u[j]) == 1:
                n += u[j]
                j += 1
            lines[(u[j:], i)][n] += value
        bad = [(r, i, dict(line)) for (r, i), line in sorted(lines.items()) if sum(line.values())]
        result = {'section': section, 'operator': s,
                  'first_equation_has_finite_support_solution': not bad,
                  'cyclic_orbit_obstructions': [
                      {'pulled_coset_representative': list(r), 'family_index_F11': i,
                       'coefficient_by_exponent': line, 'sum': sum(line.values())}
                      for r, i, line in bad]}
        if not bad:
            solution = Counter()
            for (r, i), line in lines.items():
                cumulative = 0
                for n in range(min(line), max(line) + 1):
                    cumulative += line[n]
                    if cumulative:
                        power = (1,) * n if n >= 0 else (-1,) * (-n)
                        t = sub((*power, *r), phi[s])
                        solution[t, i] -= cumulative
                assert cumulative == 0
            solution = clean(solution)
            assert difference(phi[s][1], solution) == ds[1]
            residuals = {}
            for i in (1, 2, 3):
                res = ds[i].copy()
                res.subtract(difference(phi[s][i], solution))
                residuals[str(i)] = serial(clean(res))
            result.update({'unique_candidate': serial(solution),
                           'remaining_residuals': residuals,
                           'all_three_equations_hold': all(not v for v in residuals.values())})
        out.append(result)
        print(section, s, 'first_equation', not bad,
              'candidate_terms', len(result.get('unique_candidate', [])),
              'residual_supports', {k: len(v) for k, v in result.get('remaining_residuals', {}).items()})

result = {'status': 'PASS_EXACT_CYCLIC_LINE_DIVISION',
          'utc': datetime.now(timezone.utc).isoformat(),
          'input': str(INPUT.relative_to(ROOT)),
          'input_sha256': hashlib.sha256(INPUT.read_bytes()).hexdigest(),
          'operator_inverse_checks': 24, 'results': out,
          'equation': 'd_s(t)=(phi_s(t)-1) jbar for one common jbar in the actual J_ab',
          'scope': 'Exact obstruction to arbitrary J-valued source-lift adjustments preserving the named literal retained section. No exclusion of changing the fiber section; no completed conclusion without a separate continuity argument.'}
target = ROOT / 'work_CE/next_symmetric_nodes/section_inner_adjustment29.json'
assert not target.exists()
target.write_text(json.dumps(result, indent=2) + '\n')
print('SAVED', target.relative_to(ROOT))
