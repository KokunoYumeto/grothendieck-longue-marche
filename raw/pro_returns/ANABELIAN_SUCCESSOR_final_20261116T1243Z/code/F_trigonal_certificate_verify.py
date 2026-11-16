"""Independent check of every trigonal genus-one lifting certificate.

The quotient S4 -> S3 is computed by conjugation on the three nonidentity
double transpositions, independently of the producer's pair-partition action.
The exhaustive base tuple set and the supplied witnesses are compared exactly.
"""
from itertools import permutations, product
from collections import deque, Counter
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
S3 = tuple(permutations(range(3)))
S4 = tuple(permutations(range(4)))

def mul(a, b):
    return tuple(a[b[i]] for i in range(len(a)))

def inv(a):
    return tuple(a.index(i) for i in range(len(a)))

V4 = ((1, 0, 3, 2), (2, 3, 0, 1), (3, 2, 1, 0))

def quotient(a):
    return tuple(V4.index(mul(mul(a, v), inv(a))) for v in V4)

def cycle_index(a):
    unseen = set(range(len(a)))
    cycles = 0
    while unseen:
        x = min(unseen)
        cycles += 1
        while x in unseen:
            unseen.remove(x)
            x = a[x]
    return len(a) - cycles

def multiply_tuple(t, n):
    ans = tuple(range(n))
    for a in t:
        ans = mul(ans, a)
    return ans

def group_size(t, n):
    identity = tuple(range(n))
    seen = {identity}
    queue = deque([identity])
    while queue:
        a = queue.popleft()
        for b in t:
            c = mul(a, b)
            if c not in seen:
                seen.add(c)
                queue.append(c)
    return len(seen)

for a, b in product(S4, repeat=2):
    assert quotient(mul(a, b)) == mul(quotient(a), quotient(b))
assert len({a for a in S4 if quotient(a) == tuple(range(3))}) == 4

records = json.loads((ROOT / 'agent_F/F_recillas_certificates.json').read_text())
record_map = {}
for record in records:
    cubic = tuple(map(tuple, record['cubic_tuple']))
    quartic = tuple(map(tuple, record['quartic_tuple']))
    assert cubic not in record_map
    record_map[cubic] = quartic
    assert tuple(map(quotient, quartic)) == cubic
    assert multiply_tuple(cubic, 3) == tuple(range(3))
    assert multiply_tuple(quartic, 4) == tuple(range(4))
    assert group_size(cubic, 3) == 6
    assert group_size(quartic, 4) == 24
    assert tuple(map(cycle_index, cubic)) == tuple(map(cycle_index, quartic))
    assert sum(map(cycle_index, cubic)) == 6

nonidentity = tuple(a for a in S3 if cycle_index(a))
expected = set()
lift_counts = Counter()
for length in (4, 5, 6):
    for cubic in product(nonidentity, repeat=length):
        if sum(map(cycle_index, cubic)) != 6:
            continue
        if multiply_tuple(cubic, 3) != tuple(range(3)):
            continue
        if group_size(cubic, 3) != 6:
            continue
        expected.add(cubic)
        choices = [tuple(a for a in S4 if quotient(a) == c
                         and cycle_index(a) == cycle_index(c)) for c in cubic]
        assert len(tuple(product(*choices))) == 64
        good = sum(multiply_tuple(lift, 4) == tuple(range(4))
                   and group_size(lift, 4) == 24 for lift in product(*choices))
        assert good == 12
        lift_counts[good] += 1

assert expected == set(record_map)
by_length = Counter(map(len, expected))
assert dict(by_length) == {4: 72, 5: 270, 6: 240}
out = {
    'status': 'PASS',
    'quotient_realization': 'conjugation on the three nonidentity elements of V4',
    'quotient_products_checked': 576,
    'nonidentity_tuples_exhausted': sum(5**n for n in (4, 5, 6)),
    'complete_certificate_count': len(records),
    'counts_by_branch_number': dict(sorted(by_length.items())),
    'number_of_good_lifts': dict(lift_counts),
    'cubic_source_genus': 1,
    'quartic_source_genus': 0,
    'all_source_tuples_and_every_supplied_witness_checked': True,
}
destination = ROOT / 'code/F_trigonal_certificate_verify.json'
destination.write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out, indent=2))
