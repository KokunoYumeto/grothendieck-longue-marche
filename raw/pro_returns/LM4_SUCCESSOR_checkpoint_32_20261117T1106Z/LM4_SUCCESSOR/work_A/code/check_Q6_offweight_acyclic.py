"""Exact bounded search for off-weight acyclic monomial coefficients.

The input is the actual Q6 cycle module and its already retained 36-weight
orbit.  This enumerates Q6-orbits of sums of two weights in the three
Frobenius orbits.  It does NOT enumerate arbitrary irreducible little-group
representations, or construct a source extension/action.
"""
from pathlib import Path
import contextlib
import io
import json
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
source = (ROOT / 'check_Q6_forced_frame.py').read_text()
ns = {'__file__': str(ROOT / 'check_Q6_forced_frame.py')}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(source.split('# The c-fixed character')[0], ns['__file__'], 'exec'), ns)

Q, NC, CC = ns['Q'], ns['NC'], ns['CC']
s, r, beta, ee = (ns[x] for x in ('s', 'r', 'beta', 'e'))
inv, mul = ns['inv'], ns['mul']
dualrow, sm, va = (ns[x] for x in ('dualrow', 'sm', 'va'))
lam = ns['chosen_characters']['c-fixed']
reps = [q[0] for q in ns['AC']]
chars = [dualrow(lam, NC[inv[g]]) for g in reps]
weights = sorted({sm(a, w) for a in (1, 2, 4) for w in chars})
assert len(weights) == 108
weights_set = set(weights)
pair_by_sum = {}
for i, u in enumerate(weights):
    for j in range(i, len(weights)):
        v = weights[j]
        pair_by_sum.setdefault(va(u, v), []).append((i, j))

remaining = set(pair_by_sum)
remaining.discard((0,) * 13)
orbits = []
which = {}
while remaining:
    w = min(remaining)
    orbit = sorted({dualrow(w, NC[g]) for g in range(72)})
    assert set(orbit) <= set(pair_by_sum)
    oi = len(orbits)
    for v in orbit:
        which[v] = oi
    remaining.difference_update(orbit)
    fixed_s = sum(dualrow(v, NC[s]) == v for v in orbit)
    fixed_r = sum(dualrow(v, NC[r]) == v for v in orbit)
    ds = (len(orbit) + fixed_s) // 2
    dr = (len(orbit) + 2 * fixed_r) // 3
    assert 2 * ds == len(orbit) + fixed_s
    assert 3 * dr == len(orbit) + 2 * fixed_r
    cohom = ds - dr
    assert cohom >= 0
    # This formula applies to the induced module with trivial stabilizer
    # character. Fixed monomial scalars have order dividing both 7 and 2/3.
    orbits.append(dict(index=oi, representative=w, dimension_over_k=len(orbit),
                       fixed_s_weights=fixed_s, fixed_r_weights=fixed_r,
                       s_invariant_dimension=ds, r_invariant_dimension=dr,
                       source_h1_dimension=cohom,
                       pair_multiplicity_at_representative=len(pair_by_sum[w])))

for rec in orbits:
    w = tuple(rec['representative'])
    rec['frobenius_orbit'] = sorted({which[sm(a, w)] for a in (1, 2, 4)})
    rec['negative_orbit'] = which[sm(6, w)]
    rec['c_orbit'] = which[dualrow(w, CC)]
    rec['binary_self_dual'] = rec['negative_orbit'] in rec['frobenius_orbit']
    rec['binary_c_stable'] = rec['c_orbit'] in rec['frobenius_orbit']
    rec['same_old_simple'] = w in weights_set

candidates = [rec for rec in orbits if rec['source_h1_dimension'] == 0
              and rec['binary_self_dual'] and rec['binary_c_stable']]
distribution = Counter((rec['dimension_over_k'], rec['fixed_s_weights'],
                        rec['fixed_r_weights'], rec['source_h1_dimension'])
                       for rec in orbits)
print('Actual retained weight count:', len(weights))
print('Distinct pair sums including zero:', len(pair_by_sum))
print('Nonzero Q6 pair-sum orbits:', len(orbits))
print('Distribution (orbit size, fixed s, fixed r, source H1):')
for key, count in sorted(distribution.items()):
    print(' ', key, ':', count)
print('Acyclic monomial orbit count:', sum(rec['source_h1_dimension'] == 0 for rec in orbits))
print('Self-dual c-stable acyclic candidates:', len(candidates))
for rec in candidates:
    print(' candidate', rec)
print('Classification PASS; no source extension or norm conclusion is asserted.')

result = dict(input='actual Q6 cycle module; 108 full binary weights',
              scope='trivial little-group monomial modules for pair-weight sums only',
              weights=weights, distinct_pair_sums=len(pair_by_sum),
              orbits=orbits, candidates=candidates)
(ROOT / 'Q6_offweight_acyclic_classification.json').write_text(json.dumps(result, indent=2) + '\n')
