"""Exploratory finite-field orbit check; not a transitivity proof.

The tested permutations of F_p minus {0,1} are a -> a^3 and
a -> a/(a-1), for p == 2 mod 3. A full geometrically pro-3
point/cusp-zero collision would be invariant under both maps.
Every computed orbit is recorded through its size and whether it
contains -1. No conclusion for untested primes is asserted.
"""

from math import isqrt


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def orbits(p):
    unseen = set(range(2, p))
    answer = []
    while unseen:
        root = min(unseen)
        seen = {root}
        todo = [root]
        while todo:
            a = todo.pop()
            for b in (pow(a, 3, p), a * pow(a - 1, -1, p) % p):
                assert b not in (0, 1)
                if b not in seen:
                    seen.add(b)
                    todo.append(b)
        unseen.difference_update(seen)
        answer.append(seen)
    return answer


if __name__ == "__main__":
    checked = 0
    failures = []
    for p in range(5, 10001, 3):
        if not prime(p):
            continue
        pieces = orbits(p)
        checked += 1
        if len(pieces) > 1:
            failures.append((p, [len(x) for x in pieces],
                             [min(x) for x in pieces]))
        if p <= 101:
            print(p, [len(x) for x in pieces],
                  [p-1 in x for x in pieces])
    print("Tested primes:", checked)
    print("Nontransitive cases:", failures)
    print("Scope: finite exploratory output only; no all-prime theorem.")
