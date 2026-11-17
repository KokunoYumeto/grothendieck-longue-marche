"""Independently verify the raw B112/B119 six-source table in actual9 words."""
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
def comm(a, b): return mul(a, b, inv(a), inv(b))
eta = {int(i): tuple(w) for i,w in data['eta_in_common_K'].items()}
a, B, d, e, f = [eta[i] for i in range(1, 6)]
C = (7,)
b = mul(C, B, C)
h = mul(f, (9,))
bar = lambda word: mul(C, word, C)
Delta = lambda word: mul(word, bar(word))
E = conj(f, conj(d, e))
T = mul(C, b, C, b, C, E, C, inv(b), C, inv(b))
raw = [mul(bar(b), b),
       mul(T, T),
       mul(C, b, comm(d, bar(d)), inv(b), C, Delta(d)),
       mul(C, b, comm(a, bar(a)), inv(b), C, Delta(a)),
       h]
expected = [conj(a, word) for word in raw] + [(8,)]
rows = []
for index, (formula, stored) in enumerate(zip(expected, data['actual_six_source_words']), 1):
    actual = red(stored['word'])
    rows.append({'index': index, 'name': stored['name'],
                 'raw_formula_in_actual9': formula, 'stored_actual9': actual,
                 'literal_equality': formula == actual})
result = {
    'input': str(path.relative_to(root)),
    'input_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
    'comparison': 'Raw B112.5 words with the entire outer selected-gap conjugation; only free cancellation and cone-square reduction are used.',
    'rows': rows,
    'status': 'PASS' if all(r['literal_equality'] for r in rows) else 'FAIL',
    'previous_failure': 'check_B119_literal_source25 tested B112 simplified group images as if they were identical raw free words. Four require the already proved regional node relations. The failure and both scripts remain preserved; it is not a counterexample to the source-image equality.'
}
(root/'records/B119_raw_source25.json').write_text(json.dumps(result, indent=2)+'\n')
for row in rows: print(row['index'], row['name'], row['literal_equality'])
print(result['status'])
assert len(rows) == 6 and result['status'] == 'PASS'
