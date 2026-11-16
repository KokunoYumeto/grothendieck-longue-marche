"""Compare every arithmetic F4 form with the 64 geometric classes in R6.

The old primitive annihilator is transcribed from the attached paper and
explicitly marked as not rerun.  The arithmetic-to-geometric map and the
new rational-witness coverage are independently computed here.
"""
import json, csv, collections
from pathlib import Path
from finite_jacobian import BinaryField, PolynomialRing

P = Path(__file__).parent
F = BinaryField(4105)  # x^12+x^3+1; contains F4,F16,F64.
R = PolynomialRing(F)
alpha = F.embed_f4()
embed = lambda x: (x & 1) ^ (alpha if x & 2 else 0)
unembed = {embed(x): x for x in range(4)}

ordinary_rows = '''
001 7 133 15
002 27 201 3
003 27 202 23
011 5 211 3
012 7 212 9
013 7 213 5
021 13 221 3
022 15 222 9
023 5 223 7
031 13 231 3
032 5 232 19
033 15 233 11
101 3 301 3
102 49 303 23
103 49 311 3
111 3 312 5
112 7 313 9
113 7 321 3
121 3 322 11
122 15 323 19
123 11 331 3
131 3 332 7
132 11 333 9
'''
old = {}
for line in ordinary_rows.strip().splitlines():
    a, b, c, d = line.split(); old[a] = int(b); old[c] = int(d)
old['203'] = old['302'] = 7 * 31 * 2503 * 4519
rank1 = {(1, 0): 13, (1, 1): 5, (1, 2): 11,
         (2, 0): 39, (2, 1): 19, (2, 2): 7, (2, 3): 5}
small = BinaryField(7)
for (a, b), n in list(rank1.items()):
    rank1[(small.mul(a, a), small.mul(b, b))] = n
assert len(rank1) == 12 and len(old) == 48

def symkey(triple):
    a, b, c = triple
    s = [a ^ b ^ c, F.mul(a, b) ^ F.mul(a, c) ^ F.mul(b, c),
         F.mul(F.mul(a, b), c)]
    assert all(x in unembed for x in s)
    return ''.join(str(unembed[x]) for x in s)

def geometric_key(m):
    t = m['type']; p = m['parameters']
    if t == 'rank0':
        a, b, c, d = map(embed, p)
        invariant = F.div(F.power(b, 5), F.power(a, 3))
        return 'rank0_' + str(unembed[invariant])
    if t == 'rank1':
        a, b, c, d = map(embed, p)
        A, B = F.mul(a, F.power(c, 3)), F.mul(b, c)
        return f'rank1_{unembed[A]}{unembed[B]}'
    if t == 'ordinary_split':
        return 'ordinary_' + symkey(list(map(embed, p[:3])))
    if t == 'ordinary_quadratic':
        a, b, c, d = map(embed, p)
        h = tuple(map(embed, m['h']))
        roots = [x for x in range(F.q) if not R.eval(h, x)]
        assert len(roots) == 2 and roots[0] ^ roots[1] == 1
        return 'ordinary_' + symkey([a, F.mul(b, roots[0]) ^ c,
                                    F.mul(b, roots[1]) ^ c])
    assert t == 'ordinary_cubic'
    h = tuple(map(embed, m['original_h']))
    n = tuple(map(embed, m['original_n']))
    roots = [x for x in range(F.q) if not R.eval(h, x)]
    assert len(roots) == 3
    r0, r1, ri = roots
    derivative = tuple(h[i] if i % 2 else 0 for i in range(1, len(h)))
    residue = lambda r: F.div(R.eval(n, r), R.eval(derivative, r))
    K = F.div(r1 ^ ri, r1 ^ r0)
    A = F.div(residue(ri), F.mul(K, r0 ^ ri))
    B = F.div(F.mul(residue(r0), K), ri ^ r0)
    C = F.div(F.mul(residue(r1), 1 ^ K), ri ^ r1)
    return 'ordinary_' + symkey([A, B, C])

records = [json.loads(x) for x in (P / 'A4_genus2_F4.jsonl').read_text().splitlines()]
groups = collections.defaultdict(list)
modelkeys = {}
for rec in records:
    key = geometric_key(rec['model'])
    groups[key].append(rec); modelkeys[rec['index']] = key
assert len(groups) == 64, len(groups)
assert sum(k.startswith('ordinary') for k in groups) == 48
assert sum(k.startswith('rank1') for k in groups) == 12
assert sum(k.startswith('rank0') for k in groups) == 4
witnesses = collections.defaultdict(list)
with (P / 'A4_witnesses.csv').open() as stream:
    for row in csv.DictReader(stream):
        if row['q'] == '4':
            assert row['status'] == 'witness proved'
            witnesses[modelkeys[int(row['model_id'])]].append(row)

rows = []
for key, recs in sorted(groups.items()):
    ws = witnesses[key]
    if key.startswith('ordinary'):
        previous = str(old[key.split('_')[1]])
        source = 'AP-A.C2.22; AP-A.C2.25 for 203/302'
    elif key.startswith('rank1'):
        a, b = map(int, key.split('_')[1])
        previous = str(rank1[(a, b)]); source = 'AP-A.C2.26'
    else:
        previous = 'base Jacobian has geometric 2-rank zero'; source = 'AP-A.C2.26'
    rows.append(dict(geometric_class=key, arithmetic_model_ids=';'.join(str(r['index']) for r in recs),
        arithmetic_forms=len(recs), original_rational_points=sum(r['rational_points'] for r in recs),
        rational_witnesses=len(ws), witness_primes=';'.join(map(str, sorted({int(w['ell']) for w in ws}))),
        witness_fields=';'.join(sorted({w['L_q'] for w in ws}, key=int)),
        earlier_primitive_annihilator_or_argument=previous, earlier_source=source,
        earlier_certificate_reproduction='not asserted; earlier attached table transcribed for comparison',
        new_proof_scope='all original F4 points; finite extensions and other points require separate argument'))
    assert rows[-1]['original_rational_points'] == rows[-1]['rational_witnesses']
with (P / 'A4_R6_class_comparison.csv').open('w', newline='') as stream:
    writer = csv.DictWriter(stream, list(rows[0])); writer.writeheader(); writer.writerows(rows)
summary = dict(geometric_classes=64, arithmetic_forms=len(records), rational_points=sum(len(v) for v in witnesses.values()),
               distinguished={k: [r['index'] for r in groups[k]] for k in
                 ['ordinary_203', 'ordinary_302', 'ordinary_122', 'ordinary_133']},
               normalization_field_modulus=4105, normalization_alpha=alpha)
(P / 'A4_R6_class_comparison.summary.json').write_text(json.dumps(summary, indent=2) + '\n')
print(json.dumps(summary, indent=2))
