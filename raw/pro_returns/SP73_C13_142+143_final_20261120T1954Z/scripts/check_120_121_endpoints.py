"""Conditional formal endpoint diagnostic for the literal displayed definitions.

This is not a proof that the intended geometric assertion is false. Distinct
formal labels r and tau_0(r) are kept distinct, and no unstated identifications
of objects or equality of sigma and tau are imposed. Composition is read in
the usual right-to-left order. The visible inverse is never edited by this
script.
"""
import json

r = 'r'
tr = 'tau_0(r)'

def a(label):
    return ((label, '0,1'), (label, '1,0'))

def inverse(edge):
    return (edge[1], edge[0])

lambda_prime = ((r, '1,0'), (tr, '1,0'))
factors_in_application_order = [
    ('a_r^infinity', a(r)),
    ('(Lambda_r^prime1)^-1', inverse(lambda_prime)),
    ('(a_tau0r^infinity)^-1', inverse(a(tr))),
]
joins = []
for (first_name, first), (second_name, second) in zip(
        factors_in_application_order, factors_in_application_order[1:]):
    joins.append({'after': first_name, 'before': second_name,
                  'target': first[1], 'source': second[0],
                  'matches_as_formal_labels': first[1] == second[0]})
assert len(joins) == 2
assert all(not item['matches_as_formal_labels'] for item in joins)
print(json.dumps({'assumptions': 'Distinct formal r/tau_0(r) objects; right-to-left composition; no extra identifications',
                  'literal_formula': '142_scan121 (21), using 142_scan120 (18)',
                  'joins': joins}, indent=2))
