"""Check only a literal family inclusion on scan032, not figure theory.

The primes were read in the ink before this check. This computation does not
authorize changing them. The finite example satisfies the construction and
support equality, but the script makes no claim to verify all figure axioms.
"""
import json
from pathlib import Path

A = frozenset({0, 1})
F = {A}
G = {A}
Gp = {frozenset({0}), frozenset({1})}
Fp = Gp | (F - G)
support = lambda family: set().union(*family) if family else set()
assert G <= F
assert support(Gp) == support(G)
assert A in F and A not in Gp
assert A not in Fp
assert not (F - Gp <= Fp)
assert F - G <= Fp

result = {
    'statement_id': 'TXT032-literal-F-minus-Gprime',
    'scope': 'Set families under Fprime=Gprime union (F minus G), G subset F, and equal G/Gprime supports only.',
    'F': [[0, 1]], 'G': [[0, 1]], 'Gprime': [[0], [1]],
    'Fprime': [[0], [1]],
    'A': [0, 1],
    'F_minus_Gprime_subset_Fprime': False,
    'refined_statement_id': 'TXT032-F-minus-G-subset-Fprime',
    'refined_statement': 'F minus G is a subfamily of Fprime directly by its defining union.',
    'limitation': 'No verification of the full figure/subdivision axioms and no alteration of the literal Gprime ink.'
}
print(json.dumps(result, ensure_ascii=False, indent=2))
Path(__file__).resolve().parents[1].joinpath('documentation/check032_inclusion.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
