#!/usr/bin/env python3
"""Minimal two-equation, one-color certificate from the complete actual input."""
from pathlib import Path
import json
ROOT = Path(__file__).resolve().parents[2]
D = json.loads((ROOT/'records/root_coarse_corrections29.json').read_text())
rows = {(r['section'], r['operator'], r['retained_generator']): r for r in D['rows']}
for section in ('old_c_section', 'local_C_section'):
    first = rows[section, 'v', 1]
    second = rows[section, 'v', 2]
    b1 = {tuple(t['retained_word_T']): t['coefficient']
          for t in first['module_coefficients'] if t['family_index_F11'] == 2}
    b2 = {tuple(t['retained_word_T']): t['coefficient']
          for t in second['module_coefficients'] if t['family_index_F11'] == 2}
    assert b1 == {(): 1, (3, -2, -3): -1}
    assert b2.get(()) == 1
    assert first['coarse_head_T'] == [3, 2, -3]
    assert second['coarse_head_T'] == [-1, 2, -3, 1, 3, -2, 1]
    print(section, 'PASS exact B-color first equation and nonzero second residual')
print('PASS: d_v(f)_B=1-xg^-1x^-1; q_B=xg^-1x^-1 is the unique candidate; coefficient_1 of the second residual equals1.')
