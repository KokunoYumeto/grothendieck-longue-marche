#!/usr/bin/env python3
"""Exact actual third product-one strip; no whole-kernel normality claim."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
source = ROOT / 'work_DE/next_marginal_source/w_source_adapted_basis.json'
A = json.loads(source.read_text())

def red(word):
    result = []
    for letter in word:
        if result and result[-1] == -letter:
            result.pop()
        else:
            result.append(letter)
    return result

def inv(word):
    return [-letter for letter in word[::-1]]

def subst(word, action):
    return red(y for x in word for y in
               (action[str(abs(x))] if x > 0
                else inv(action[str(abs(x))])))

def conj(h, word):
    return red(h + word + inv(h))

# Actual adapted basis: z,c1,c2,c3,c4,p1,p2,p3,p4,a,d,b.
b = [12]
cprime = [-5, -4, 5]
k = [-12, 5, 12]
pminus = A['all_source_words_in_new']['17']
assert pminus == [12, 2, 6, -2, -12]
v = red(inv(pminus) + inv(k) + pminus + k)
pair_inner = red(cprime + b)
actual_inner = red(v + pair_inner)
gamma = A['actions_in_new']['3']
gamma_inv = A['inverse_actions_in_new']['3']
checks = []
for word in (b, cprime):
    actual = subst(word, gamma)
    assert actual == conj(actual_inner, word)
    assert conj(inv(v), actual) == conj(pair_inner, word)
    # eta = Inn(v^-1) gamma; eta^-1 = gamma^-1 Inn(v).
    assert subst(conj(v, word), gamma_inv) == conj(inv(pair_inner), word)
    checks.append({'word': word, 'actual_image': actual,
                   'corrected_image': conj(pair_inner, word)})
print('PASS actual positive2 action equals Inn(v Cprime b) on b,Cprime.')
print('PASS both corrected action and literal inverse equal pair inner actions.')
print('PASS v is the explicit commutator of source17 with k=b^-1 c4 b.')
print('Scope: k lies in the proved c4 strip, hence v lies in J_c by source normality.')
print('Conclusion: every b^n c3 b^-n lies in actual J_c, and likewise its closed image.')
print('No whole-J_c b-normality or full marginal equality is asserted.')
result = {
    'description': __doc__,
    'input_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
    'action_index': 3,
    'b': b, 'Cprime': cprime, 'k': k, 'source_p1minus': pminus,
    'v': v, 'pair_inner': pair_inner, 'checks': checks,
    'status': 'PASS',
    'scope': 'Whole two-generator filling-kernel image and the third b-strip only.'
}
(ROOT / 'work_CE/w_third_product_strip_certificate.json').write_text(
    json.dumps(result, indent=2) + '\n')
