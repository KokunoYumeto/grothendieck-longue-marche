"""Independently recompute the exact e=19 theta-packet necessary conditions.

Every tentative union is checked from its full ordered-pair difference list;
this does not reuse the other certificate's incremental difference arrays.
A compatible union establishes only that this necessary test is inconclusive.
"""
from collections import Counter
from math import gcd
from pathlib import Path
import json

def generated(n, generators):
    result = {1}
    while True:
        enlarged = result | {x*y % n for x in result for y in generators}
        if enlarged == result:
            return result
        result = enlarged

def quotient_cosets(n, subgroup, ambient):
    remaining = set(ambient)
    answer = []
    while remaining:
        representative = min(remaining)
        part = {representative*x % n for x in subgroup}
        assert part <= remaining
        answer.append(part)
        remaining -= part
    return answer

def check(n, values):
    counts = Counter((a-b) % n for a in values for b in values if a != b)
    return max(counts.values(), default=0) <= 2, counts

def solve(n):
    units = {a for a in range(1, n) if gcd(a,n) == 1}
    packet = generated(n, [pow(2,19,n), n-1])
    initial = packet | {0}
    valid, counts = check(n, initial)
    result = {'n': n, 'packet': sorted(packet),
              'single_packet_max_multiplicity': max(counts.values())}
    if not valid:
        d = min(d for d,v in counts.items() if v > 2)
        result.update(excluded=True, reason='single packet', difference=d,
                      ordered_pairs=[[a,b] for a in sorted(initial)
                                     for b in sorted(initial) if (a-b)%n == d])
        return result
    signed_doubling = generated(n, [2, n-1])
    assert packet <= signed_doubling
    orbits = quotient_cosets(n, signed_doubling, units)
    assert orbits[0] == signed_doubling
    choices = [quotient_cosets(n, packet, orbit) for orbit in orbits[1:]]
    tested = [0]*len(choices)
    accepted = [0]*len(choices)
    def search(depth, current):
        if depth == len(choices):
            return current
        for part in choices[depth]:
            tested[depth] += 1
            candidate = current | part
            valid, _ = check(n, candidate)
            if valid:
                accepted[depth] += 1
                answer = search(depth+1, candidate)
                if answer is not None:
                    return answer
        return None
    answer = search(0, initial)
    result.update(excluded=answer is None, reason='full required packet union',
                  tested_by_depth=tested, accepted_by_depth=accepted,
                  orbit_count=len(orbits), packet_size=len(packet))
    if answer is not None:
        result['compatible_union'] = sorted(answer)
        result['compatible_union_max_multiplicity'] = max(check(n,answer)[1].values())
    if n == 1257:
        result['direct_mod_three_check'] = {
            'occupancies': [1,22,22],
            'ordered_nonzero_differences_divisible_by_three': 22*21*2,
            'maximum_allowed': 2*(1257//3-1)}
        assert 22*21*2 > 2*(1257//3-1)
    return result

def main():
    candidates = [191,229,361,419,457,571,573,647,687,955,1083,1257,1371]
    result = [solve(n) for n in candidates]
    remaining = [r['n'] for r in result if not r['excluded']]
    assert remaining == [191,229]
    out = {'scope':'Exact finite necessary-condition audit; not itself a curve witness.',
           'remaining_conductors':remaining, 'results':result}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'remaining_conductors':remaining,
                      'excluded_conductors':[r['n'] for r in result if r['excluded']],
                      '457_counts':next(r for r in result if r['n']==457)},indent=2))

if __name__ == '__main__':
    main()
