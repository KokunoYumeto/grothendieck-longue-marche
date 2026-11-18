"""Check both original finite frame tuples in the preserved source group law.

This supplements the fixed-action and fixed-s-frame detectors.  No witness
search result is trusted: each stored tuple is substituted into the law.
"""
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
import hashlib
import json
import runpy

ROOT = Path(__file__).resolve().parent
A = ROOT / 'lm4_source_verifiers/work_A'
with redirect_stdout(StringIO()):
    G = runpy.run_path(str(A / 'check_Q6_central_cover.py'))

def tup(x):
    return tuple(map(tup, x)) if isinstance(x, list) else x

out = {}
for name in ('Q6_actual_central_solution.json', 'A63_zero_t_A56_solution.json'):
    data = json.loads((A / name).read_text())
    G['phi0'].__globals__['WE'] = tup(data['WE'])
    G['ph'].__globals__['PSHIFT'] = tup(data['PSHIFT'])
    ph, ca, em, ei, ein = (G[k] for k in ('ph', 'ca', 'em', 'ei', 'ein'))
    def neg(g):
        return ph(ca(g))
    s, r, t, one = (G[k] for k in ('SS', 'RR', 'TT', 'ONE'))
    beta, jf = tup(data['BFRAME']), tup(data['JFRAME'])
    assert ph(t) == t and neg(t) == ei(t)
    assert neg(neg(s)) == s and neg(neg(r)) == r
    assert ph(s) == ein(beta, s)
    assert neg(r) == ein(jf, ei(r))
    assert em(ei(beta), neg(ei(beta))) == one
    assert em(ei(jf), neg(ei(jf))) == one
    out[name] = {
        'sha256': hashlib.sha256((A / name).read_bytes()).hexdigest(),
        'literal_cusp': True, 'negative_square': True,
        's_conjugacy_and_norm': True, 'r_conjugacy_and_norm': True,
    }
out['chosen_character'] = list(G['lam'])
out['all_checks'] = 'PASS'
ROOT.joinpath('check_symmetry_stored_frames.json').write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps(out, indent=2))
