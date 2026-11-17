#!/usr/bin/env python3
"""Independent Schreier/character audit; no producer imports or search.

The input actions are certified actual tangent-bundle actions.  This checker
independently rewrites their index-two restrictions and verifies every inverse
as well as the exact way the omitted alpha1^2 destroys the restricted gate.
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
INPUT = ROOT / "work_DE/next_marginal_source/tangent_ordered_family.json"
data = json.loads(INPUT.read_text())

def reduce_word(word):
    stack = []
    for x in word:
        if stack and stack[-1] == -x:
            stack.pop()
        else:
            stack.append(x)
    return stack

def inverse(word):
    return [-x for x in reversed(word)]

def substitute(word, images):
    return reduce_word([y for x in word for y in
                        (images[abs(x)] if x > 0 else inverse(images[abs(x)]))])

basis = {int(k): v for k, v in data["ordered_basis_in_V"].items()}
positive_schreier = {
    (0, 1): [1], (0, 2): [2], (0, 4): [3], (0, 6): [4], (0, 7): [9],
    (1, 1): [5], (1, 2): [6], (1, 4): [7], (1, 6): [8], (1, 7): [10],
    (0, 3): [], (1, 3): [11], (0, 5): [12], (1, 5): [13],
}

def schreier(word):
    state, result = 0, []
    for x in word:
        j = abs(x)
        next_state = state ^ (j in (3, 5))
        result += (positive_schreier[state, j] if x > 0
                   else inverse(positive_schreier[next_state, j]))
        state = next_state
    assert state == 0, "Input must belong to the ordered index-two subgroup"
    result = reduce_word(result)
    assert substitute(result, basis) == reduce_word(word)
    return result

def ell(word):
    return sum((1 if x == 10 else -1 if x == -10 else 0) for x in word)

def peripheral_conjugator(word, peripheral):
    core, conjugator = reduce_word(word), []
    while len(core) > 1 and core[0] == -core[-1]:
        conjugator.append(core[0])
        core = core[1:-1]
    assert core == [peripheral], (peripheral, core)
    assert reduce_word(conjugator + core + inverse(conjugator)) == word
    return conjugator

actual = {int(k): {int(j): w for j, w in a.items()}
          for k, a in data["V_basis_actions"].items()}
actual_inverse = {int(k): {int(j): w for j, w in a.items()}
                  for k, a in data["V_basis_inverse_actions"].items()}
for i in range(6):
    for j in range(1, 8):
        assert substitute(actual[i][j], actual_inverse[i]) == [j]
        assert substitute(actual_inverse[i][j], actual[i]) == [j]

review = {"input_sha256": hashlib.sha256(INPUT.read_bytes()).hexdigest(),
          "actual_inverse_checks": 84,
          "ordered_action_checks": 0, "restricted_conjugator_ell": {},
          "alpha1_squared": {}}
for label, item in data["Gamma0_actions"].items():
    label = int(label)
    action = (actual if label > 0 else actual_inverse)[abs(label)-1]
    shifts = {}
    for j, word in basis.items():
        rewritten = schreier(substitute(word, action))
        assert rewritten == item["ordered_action"][str(j)]
        assert ell(rewritten) == int(j == 10)
        review["ordered_action_checks"] += 1
    for j in (1, 2, 4, 6):
        conjugator = peripheral_conjugator(action[j], j)
        shifts[j] = ell(schreier(conjugator))
        assert shifts[j] == 0
    review["restricted_conjugator_ell"][label] = shifts

alpha1_squared = {j: substitute(actual[1][j], actual[1]) for j in range(1, 8)}
for j in (1, 2, 4, 6):
    conjugator = peripheral_conjugator(alpha1_squared[j], j)
    rewritten = schreier(conjugator)
    assert ell(rewritten) == -1
    review["alpha1_squared"][j] = {
        "conjugator_in_V_basis": conjugator,
        "conjugator_in_ordered_basis": rewritten,
        "ell": ell(rewritten),
    }
review["D_squared"] = schreier([5, 7, 5, 7])
assert review["D_squared"] == [12, 10, 13, 9]
assert ell(review["D_squared"]) == 1
review["scope"] = (
    "The restricted Gamma0 family has an ell=0 support obstruction. "
    "The actual even-source generator alpha1^2 shifts every selected "
    "peripheral by ell=-1, so this is not an obstruction for the full source."
)
destination = ROOT / "work_CE/tangent_restricted_character_independent.json"
destination.write_text(json.dumps(review, indent=2) + "\n")
print("PASS: 84 actual inverse identities; 130 independent ordered rewrites.")
print("PASS: all 40 restricted peripheral conjugators have ell=0.")
print("PASS: all four alpha1^2 peripheral conjugators have ell=-1.")
print("PASS: D^2 = (12,10,13,9), ell(D^2)=1.")
print("SCOPE: restricted family obstruction only; not a full-source separator.")
