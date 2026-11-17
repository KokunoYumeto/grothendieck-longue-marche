"""Independently compare B119's six printed source formulas with actual9 input."""
from pathlib import Path
import hashlib
import json

root = Path(__file__).resolve().parents[1]
path = root/'work_CE/next_symmetric_nodes/annular_neck_presentation23.json'
data = json.loads(path.read_text())
def red(word):
    out = []
    for x in word:
        if abs(x) in (6, 7): x = abs(x)
        if out and (out[-1] == -x or x in (6, 7) and out[-1] == x): out.pop()
        else: out.append(x)
    return tuple(out)
def inv(word): return red(-x for x in reversed(word))
def mul(*words): return red(x for word in words for x in word)
def conj(a, b): return mul(a, b, inv(a))
eta = {int(i): tuple(w) for i,w in data['eta_in_common_K'].items()}
a, B, d, e, f = [eta[i] for i in range(1, 6)]
C = (7,)
b = mul(C, B, C)
h = mul(f, (9,))
Delta = lambda word: mul(word, C, word, C)
expected = [
    conj(a, Delta(b)),
    conj(a, conj(mul(Delta(b), h, Delta(d)), Delta(e))),
    conj(a, Delta(d)),
    conj(a, Delta(a)),
    conj(a, h),
    (8,),
]
rows = []
for index, (formula, stored) in enumerate(zip(expected, data['actual_six_source_words']), 1):
    actual = red(stored['word'])
    rows.append({'index': index, 'name': stored['name'],
                 'printed_formula_in_actual9': formula, 'stored_actual9': actual,
                 'equal_after_free_and_cone_square_reduction': formula == actual})
result = {'input': str(path.relative_to(root)),
          'input_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
          'comparison': 'Independent printed B119 expressions, reduced only by free cancellation and the two cone squares.',
          'rows': rows, 'status': 'PASS' if all(r['equal_after_free_and_cone_square_reduction'] for r in rows) else 'FAIL'}
(root/'records/B119_literal_source25.json').write_text(json.dumps(result, indent=2)+'\n')
for row in rows: print(row['index'], row['name'], row['equal_after_free_and_cone_square_reduction'])
print(result['status'])
assert len(rows) == 6 and result['status'] == 'PASS'
