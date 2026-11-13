#!/usr/bin/env python3
"""Exact braid-relation certificate for epsilon^3 = delta^4 in B4."""
from collections import deque
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
START = (1, 1, 2, 3) * 3
TARGET = (1, 2, 3) * 4


def neighbors(word):
    for j in range(len(word) - 1):
        a, b = word[j:j+2]
        if abs(a-b) >= 2:
            yield word[:j] + (b, a) + word[j+2:], {
                "position": j, "relation": "distant_commutation",
                "old": [a, b], "new": [b, a]}
    for j in range(len(word) - 2):
        a, b, c = word[j:j+3]
        if a == c and abs(a-b) == 1:
            yield word[:j] + (b, a, b) + word[j+3:], {
                "position": j, "relation": "adjacent_braid",
                "old": [a, b, c], "new": [b, a, b]}


def permutation(word, n=5):
    p = list(range(n))
    for letter in word:
        j = abs(letter)-1
        p[j], p[j+1] = p[j+1], p[j]
    return tuple(p)


def compose(a, b):
    return tuple(a[b[j]] for j in range(len(a)))


def inverse(a):
    return tuple(a.index(j) for j in range(len(a)))


def main():
    parent = {START: None}
    todo = deque([START])
    while TARGET not in parent:
        word = todo.popleft()
        for nxt, move in neighbors(word):
            if nxt not in parent:
                parent[nxt] = (word, move)
                todo.append(nxt)
    chain = []
    at = TARGET
    while parent[at] is not None:
        old, move = parent[at]
        assert any(nxt == at and m == move for nxt, m in neighbors(old))
        chain.append({"from": list(old), "to": list(at), **move})
        at = old
    chain.reverse()
    assert at == START
    ep = permutation((1, 1, 2, 3))
    fixed = [j+1 for j in range(5) if ep[j] == j]
    assert fixed == [1, 5]
    half_turn = (4, 1, 3, 2, 0)
    assert compose(half_turn, half_turn) == tuple(range(5))
    assert compose(compose(half_turn, ep), half_turn) == inverse(ep)
    units = [a for a in range(12) if a % 2 and a % 3]
    assert all((8*a) % 12 != 0 for a in units)
    result = {
        "identity": "(sigma1^2 sigma2 sigma3)^3 = (sigma1 sigma2 sigma3)^4",
        "proof_method": "literal finite sequence of defining positive braid relations",
        "number_of_moves": len(chain), "visited_positive_words": len(parent),
        "braid_relation_chain": chain,
        "epsilon_permutation_one_based": [j+1 for j in ep],
        "fixed_points": fixed,
        "pole_half_turn_permutation_one_based": [j+1 for j in half_turn],
        "abelianization_modulus": 12, "epsilon_abelianization": 4,
        "units_mod12": units,
        "pole_exchange_contradiction_residues": [(8*a) % 12 for a in units],
        "scope": "The spherical normalizer and full-GT comparison are proved in E.34."
    }
    HERE.joinpath("e_periodic_braid_root.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({k:v for k,v in result.items() if k != "braid_relation_chain"}, indent=2))
    for j, row in enumerate(chain, 1):
        print(j, row["from"], "->", row["to"], row["relation"], row["position"])
    print("PASS_PERIODIC_BRAID_RELATIONS_AND_POLE_PERMUTATIONS")


if __name__ == "__main__":
    main()
