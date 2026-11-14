"""Exact diagnostic trace-cocycle tests in several finite extension fields.

Every matrix comes from the retained F23 universal source data. The test
uses deterministic character samples and computes full source-invariant
linear closure, not only one source layer. Its finite samples are research
diagnostics and do not assert an unbounded field theorem.
"""
from pathlib import Path
from hashlib import sha256
from collections import Counter
import json
import random
import numpy as np


def finite_field(p, m, modulus):
    q = p**m
    digits = np.array([[i//p**j % p for j in range(m)] for i in range(q)], dtype=np.int16)
    weights = p**np.arange(m, dtype=np.int64)
    mul = np.zeros((q, q), dtype=np.int16)
    for a in range(q):
        for b in range(q):
            product = np.convolve(digits[a], digits[b]).astype(np.int64)
            for power in range(2*m-2, m-1, -1):
                coefficient = int(product[power] % p)
                for j in range(m):
                    product[power-m+j] -= coefficient*modulus[j]
            mul[a, b] = int((product[:m] % p)@weights)
    add = ((digits[:, None, :]+digits[None, :, :]) % p)@weights
    assert np.all(mul == mul.T)
    assert all(np.count_nonzero(mul[i] == 1) == 1 for i in range(1, q))
    # Complete finite associativity and distributivity checks.
    aa, bb, cc = np.indices((q, q, q))
    assert np.array_equal(mul[mul[aa, bb], cc], mul[aa, mul[bb, cc]])
    assert np.array_equal(mul[aa, add[bb, cc]], add[mul[aa, bb], mul[aa, cc]])
    powers = np.ones((q, q), dtype=np.int16)
    for exponent in range(1, q):
        powers[:, exponent] = mul[powers[:, exponent-1], np.arange(q)]
    assert np.all(powers[1:, q-1] == 1)
    trace = np.zeros(q, dtype=np.int16)
    for j in range(m):
        trace = add[trace, powers[:, p**j]]
    assert np.all(trace < p) and np.any(trace != 0)
    return digits, weights, mul, add, powers, trace


def rref(matrix, p):
    matrix = matrix.copy().astype(np.int16)
    n, rows, columns = matrix.shape
    ranks = np.zeros(n, dtype=np.int64)
    pivots = np.full((n, columns), -1, dtype=np.int64)
    inverse = np.array([0]+[pow(i, -1, p) for i in range(1, p)], dtype=np.int16)
    row_indices = np.arange(rows)[None, :]
    for column in range(columns):
        eligible = (row_indices >= ranks[:, None]) & (matrix[:, :, column] != 0)
        active = np.flatnonzero(np.any(eligible, axis=1))
        selected = np.argmax(eligible[active], axis=1)
        dest = ranks[active]
        pivot = matrix[active, selected].copy()
        previous = matrix[active, dest].copy()
        matrix[active, selected] = previous
        pivot = pivot*inverse[pivot[:, column], None] % p
        matrix[active, dest] = pivot
        coefficient = matrix[active, :, column].copy()
        coefficient[np.arange(len(active)), dest] = 0
        matrix[active] = (matrix[active]-coefficient[:, :, None]*pivot[:, None, :]) % p
        pivots[active, dest] = column
        ranks[active] += 1
    return matrix, ranks, pivots


def one_field(data, p, m, modulus, count):
    digits, weights, mul, add, powers, trace = finite_field(p, m, modulus)
    q = p**m
    generator = random.Random(17391+q)
    characters = set()
    # Include repeated/scalar-inverse triples and then deterministic samples.
    for a in range(p, q):
        for pattern in [(a, a, 1), (a, 1, a), (1, a, a), (a, a, a),
                        (a, int(powers[a, q-2]), 1)]:
            deleted = (p-1, 1, 1, 1)
            characters.add(pattern+deleted)
    while len(characters) < count:
        old = tuple(generator.randrange(1, q) for _ in range(3))
        deleted = tuple(generator.randrange(1, p) for _ in range(4))
        if all(c == 1 for c in deleted):
            continue
        characters.add(old+deleted)
    proper_degrees = [d for d in range(1, m) if m % d == 0]
    characters = [c for c in sorted(characters)
                  if not any(all(powers[x, p**d] == x for x in c)
                             for d in proper_degrees)]
    chars = np.array(characters, dtype=np.int16)
    n = len(chars)
    cache = {}

    def monomial(exponent):
        key = tuple(exponent)
        if key not in cache:
            value = np.ones(n, dtype=np.int16)
            for j, power in enumerate(key):
                value = mul[value, powers[chars[:, j], power % (q-1)]]
            cache[key] = value
        return cache[key]

    def polynomial(poly):
        result = np.zeros((n, m), dtype=np.int32)
        for coefficient, exponent in poly:
            result += (coefficient % p)*digits[monomial(exponent)]
        return (result % p)@weights

    old = [r for r in data["records"] if r["index"] < 11]
    seeds = [r for r in data["records"] if r["index"] >= 11]
    matrix = np.zeros((n, 11, 7, 7), dtype=np.int16)
    seedrows = np.zeros((n, 8, 7), dtype=np.int16)
    for i, record in enumerate(old):
        for j, row in enumerate(record["action_matrix"]):
            for k, poly in enumerate(row):
                matrix[:, i, j, k] = polynomial(poly)
    for i, record in enumerate(seeds):
        for j, poly in enumerate(record["u_derivation_row"]):
            seedrows[:, i, j] = polynomial(poly)
    dimension = 7*m
    actions = np.zeros((n, 11, dimension, dimension), dtype=np.int16)
    initial = np.zeros((n, 8, dimension), dtype=np.int16)
    for j in range(7):
        for a in range(m):
            initial[:, :, m*j+a] = trace[mul[seedrows[:, :, j], p**a]]
        for k in range(7):
            for a in range(m):
                product = digits[mul[matrix[:, :, j, k], p**a]]
                actions[:, :, m*j:m*(j+1), m*k+a] = product
    rows = np.concatenate((initial, np.zeros((n, dimension-8, dimension), dtype=np.int16)), axis=1)
    rows, rank, pivots = rref(rows, p)
    history = [{"round": 0, "rank_counts": dict(sorted(Counter(map(int, rank)).items()))}]
    for round_number in range(1, dimension+1):
        transformed = np.einsum('nrc,nicd->nird', rows.astype(np.int32),
                                actions.astype(np.int32)) % p
        combined = np.concatenate((rows, transformed.reshape(n, 11*dimension, dimension)), axis=1)
        reduced, new_rank, new_pivots = rref(combined, p)
        assert np.all(new_rank >= rank)
        history.append({"round": round_number,
                        "rank_counts": dict(sorted(Counter(map(int, new_rank)).items()))})
        print(json.dumps({"field_order": q, **history[-1]}), flush=True)
        stable = np.array_equal(new_rank, rank)
        rows, rank, pivots = reduced[:, :dimension], new_rank, new_pivots
        if stable:
            break
    else:
        raise AssertionError("source closure failed to stabilize")
    target_rank = 6*m+1
    assert np.all(rank <= target_rank)
    # Every trace-zero principal tuple must belong to the final kernel.
    trace_zero = [x for x in range(q) if trace[x] == 0]
    for center in trace_zero:
        differences = ((digits[chars]-digits[1]) % p)@weights
        principal = digits[mul[differences, center]].reshape(n, dimension)
        assert np.all(np.einsum('nrd,nd->nr', rows.astype(np.int32),
                                principal.astype(np.int32)) % p == 0)
    deficient = np.flatnonzero(rank < target_rank)
    examples = []
    for index in deficient[:25]:
        basis = []
        free = [i for i in range(dimension) if i not in pivots[index, :rank[index]]]
        for column in free:
            v = np.zeros(dimension, dtype=np.int64)
            v[column] = 1
            for r, pivot in enumerate(pivots[index, :rank[index]]):
                v[pivot] = -int(rows[index, r, column]) % p
            basis.append(v.tolist())
        examples.append({"characters": chars[index].tolist(), "rank": int(rank[index]),
                         "kernel_basis": basis})
    return {"prime": p, "extension_degree": m, "field_order": q,
            "modulus_coefficients": modulus, "characters_checked": n,
            "character_tuples": chars.tolist(), "rank_target": target_rank,
            "rounds": history, "deficient_count": len(deficient),
            "deficient_examples": examples,
            "scope": "Deterministic finite character diagnostics with full actual-source closure. A lower rank is a linear candidate needing independent finite-group audit; a full rank is only a result for these enumerated characters."}


def main():
    producer = Path(__file__).resolve()
    source = producer.with_name("affine_obstruction_stage_output.json")
    data = json.loads(source.read_text())
    specifications = [(3, 3, [2, 2, 0], 300), (5, 2, [3, 0], 300),
                      (7, 2, [4, 0], 300)]
    results = []
    output = producer.with_name("affine_trace_prime_base_stage_output.json")
    for specification in specifications:
        results.append(one_field(data, *specification))
        record = {"status": "UNREGISTERED_EXACT_FINITE_TRACE_DIAGNOSTICS",
                  "producer_sha256": sha256(producer.read_bytes()).hexdigest(),
                  "input_sha256": sha256(source.read_bytes()).hexdigest(), "results": results}
        output.write_text(json.dumps(record, indent=2)+'\n')
    print(json.dumps({"status": record["status"],
                      "fields": [{"q": r["field_order"], "characters": r["characters_checked"],
                                  "deficient": r["deficient_count"]} for r in results],
                      "output_sha256": sha256(output.read_bytes()).hexdigest()}, indent=2))


if __name__ == '__main__':
    main()
