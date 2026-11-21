"""Compare written first and blind second readings without deciding any reading.

Whitespace is not a token. TeX commands, words, numbers, and punctuation are
tokens; no spelling, index, accent, prime, or mathematical sign is normalized.
Every differing box requires a human/model image adjudication recorded separately.
"""
from pathlib import Path
import csv, json, re, sys, difflib, hashlib, datetime

ROOT = Path(__file__).resolve().parents[1]
page = sys.argv[1]

def read(suffix):
    path = ROOT / 'second' / f'{page}_{suffix}.tsv'
    with path.open(newline='') as f:
        rows = list(csv.DictReader(f, delimiter='\t'))
    assert len({r['box'] for r in rows}) == len(rows), f'Duplicate box: {path}'
    return {r['box']: r for r in rows}

def tokens(text):
    return re.findall(r'\\[A-Za-z]+|\\.|[^\W\d_]+|\d+|[^\s]', text, re.UNICODE)

first, second, boxes = read('first'), read('second'), read('boxes')
assert first.keys() == second.keys() == boxes.keys(), 'Missing or extra box'
results = []
for box in boxes:
    a, b = first[box]['reading'], second[box]['reading']
    ta, tb = tokens(a), tokens(b)
    differences = []
    for op, i, j, k, l in difflib.SequenceMatcher(None, ta, tb, autojunk=False).get_opcodes():
        if op != 'equal':
            differences.append({'operation': op, 'first_range': [i,j],
                                'second_range': [k,l], 'first': ta[i:j], 'second': tb[k:l]})
    results.append({'box': box, 'kind': boxes[box]['kind'],
                    'coordinates': [int(boxes[box][k]) for k in ('x0','y0','x1','y1')],
                    'first': a, 'second': b, 'identical_tokens': not differences,
                    'token_differences': differences})

out = ROOT / 'second' / f'{page}_comparison.json'
assert not out.exists(), 'Do not overwrite a recorded blind comparison.'
hashes={suffix:hashlib.sha256((ROOT/'second'/f'{page}_{suffix}.tsv').read_bytes()).hexdigest()
        for suffix in ('boxes','first','second')}
out.write_text(json.dumps({'page': page, 'tokenization': 'TeX commands, words, digits, punctuation; whitespace ignored only',
                           'compared_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
                           'input_sha256': hashes,
                           'boxes': len(results), 'differing_boxes': sum(not r['identical_tokens'] for r in results),
                           'results': results}, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'page': page, 'boxes': len(results),
                  'differing_boxes': sum(not r['identical_tokens'] for r in results), 'output': str(out)}))
