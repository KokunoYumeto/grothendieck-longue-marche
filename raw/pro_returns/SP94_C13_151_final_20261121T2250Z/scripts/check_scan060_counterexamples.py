"""Finite set certificates for the targeted checks on scan060.

These computations concern explicitly defined mathematical examples; they do
not read images or choose manuscript glyphs.
"""
from pathlib import Path
import json

WORK = Path(__file__).resolve().parents[1]

def union(sets):
    result = set()
    for value in sets:
        result.update(value)
    return result

def verify(indices, leq, pieces, i, j, k):
    assert all(leq(a, a) for a in indices)
    assert all(not (leq(a, b) and leq(b, a)) or a == b
               for a in indices for b in indices)
    assert all(not (leq(a, b) and leq(b, c)) or leq(a, c)
               for a in indices for b in indices for c in indices)
    assert all(not leq(a, b) or pieces[a] <= pieces[b]
               for a in indices for b in indices)
    assert all(not (leq(a, b) and a != b) or pieces[a] < pieces[b]
               for a in indices for b in indices)
    assert all(pieces[a] & pieces[b] ==
               union(pieces[l] for l in indices if leq(l, a) and leq(l, b))
               for a in indices for b in indices)
    dot = {a: union(pieces[l] for l in indices if leq(l, a) and l != a)
           for a in indices}
    rj = union(pieces[l] for l in indices if not pieces[j] <= pieces[l])
    rjk = rj & pieces[k]
    sjk = union(pieces[l] for l in indices
                if leq(j, l) and leq(l, k) and l != k)
    second_subset_union = union(pieces[l] for l in indices
                                if leq(l, k) and l != k and pieces[j] <= pieces[l])
    reflection = all(not pieces[a] <= pieces[b] or leq(a, b)
                     for a in indices for b in indices)
    return dict(
        number_of_indices=len(indices), ordered_pair_intersections_checked=len(indices)**2,
        poset=True, monotone=True, strict_comparisons_proper=True,
        common_lower_intersection_condition=True,
        finite_closed_cover_of_discrete_union=True,
        order_reflection=reflection,
        all_stars_nonempty=all(pieces[a] - dot[a] for a in indices),
        R_jk=sorted(rjk), S_jk=sorted(sjk),
        union_over_second_index_subset=sorted(second_subset_union),
        dot_X_i=sorted(dot[i]), dot_X_j=sorted(dot[j]), dot_X_k=sorted(dot[k]),
        R_union_S=sorted(rjk | sjk), R_intersection_S=sorted(rjk & sjk),
        second_union_identification_holds=(sjk == second_subset_union),
        union_assertion_holds=(rjk | sjk == dot[k]),
        literal_intersection_assertion_holds=(rjk & sjk == dot[i]),
        replacing_i_by_j_suffices=(rjk & sjk == dot[j]))

indices = ['o', 'a', 'b', 'j', 'l', 'k']
order = {(x, x) for x in indices} | {
    ('o', 'a'), ('o', 'b'), ('a', 'j'), ('a', 'l'),
    ('b', 'j'), ('b', 'l'), ('j', 'k'), ('l', 'k')}
while True:
    expanded = order | {(a, d) for a, b in order for c, d in order if b == c}
    if expanded == order:
        break
    order = expanded
pieces = {'o': set(), 'a': {'p'}, 'b': {'q'}, 'j': {'p', 'q'},
          'l': {'p', 'q', 'r'}, 'k': {'p', 'q', 'r', 's'}}
case1 = verify(indices, lambda a,b: (a,b) in order, pieces, 'a', 'j', 'k')
assert not case1['order_reflection']
assert not case1['second_union_identification_holds']
assert not case1['union_assertion_holds']

case2 = verify(list(range(3)), lambda a,b: a <= b,
               {a:set(range(a+1)) for a in range(3)}, 0, 1, 2)
assert case2['order_reflection'] and case2['all_stars_nonempty']
assert not case2['literal_intersection_assertion_holds']
assert case2['replacing_i_by_j_suffices']

case3 = verify(list(range(8)), lambda a,b: a & b == a,
               {a:{x for x in range(8) if x & a == x} for a in range(8)}, 0, 1, 7)
assert case3['order_reflection'] and case3['all_stars_nonempty']
assert not case3['replacing_i_by_j_suffices']
assert 2 in case3['R_intersection_S'] and 2 not in case3['dot_X_j']

result = {'description':'Exact finite-set checks; discrete topology makes every piece closed.',
          'case_1_nonreflecting_strict_family':case1,
          'case_2_successor_chain':case2,
          'case_3_boolean_downsets':case3,
          'boolean_encoding':'0=empty subset, 1={a}, 2={b}, 4={c}; bitwise union encodes subsets'}
out = WORK/'audit'/'scan060_counterexample_certificate.json'
out.write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
