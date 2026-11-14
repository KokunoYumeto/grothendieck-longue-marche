"""Close the remaining F9 translation-line candidates under actual sources.

All source matrices and seed rows are the literal F23/F24 evaluations.
The algorithm computes the largest source-invariant translation subspace
whose seed images lie in Aff_1(F3), keeping the scalar characters fixed.
"""
from pathlib import Path
from hashlib import sha256
from collections import Counter
from collections import deque
import json
import numpy as np
import affine_f9_translation_obstruction_stage as f9


def main():
    producer = Path(__file__).resolve()
    folder = producer.parent
    candidate_source = folder/"affine_f9_translation_obstruction_stage_output.json"
    source = folder/"affine_obstruction_stage_output.json"
    candidates = json.loads(candidate_source.read_text())
    data = json.loads(source.read_text())
    chars = np.array(candidates["deficient_characters"], dtype=np.uint8)
    n = len(chars)
    mul, inverse, powers = f9.field_tables()
    cache = {}

    def monomial(exponent):
        key = tuple(exponent)
        if key not in cache:
            value = np.ones(n, dtype=np.uint8)
            for j, power in enumerate(key):
                value = mul[value, powers[chars[:, j], power % 8]]
            cache[key] = value
        return cache[key]

    def polynomial(poly):
        real = np.zeros(n, dtype=np.int32)
        imaginary = np.zeros(n, dtype=np.int32)
        for coefficient, exponent in poly:
            value = monomial(exponent)
            real += (coefficient % 3)*(value % 3)
            imaginary += (coefficient % 3)*(value // 3)
        return (real % 3)+3*(imaginary % 3)

    old = [r for r in data["records"] if r["index"] < 11]
    seeds = [r for r in data["records"] if r["index"] >= 11]
    matrices = np.zeros((n, 11, 7, 7), dtype=np.uint8)
    seedrows = np.zeros((n, 8, 7), dtype=np.uint8)
    for i, record in enumerate(old):
        for j, row in enumerate(record["action_matrix"]):
            for k, poly in enumerate(row):
                matrices[:, i, j, k] = polynomial(poly)
    for i, record in enumerate(seeds):
        for j, poly in enumerate(record["u_derivation_row"]):
            seedrows[:, i, j] = polynomial(poly)
    a, b = matrices % 3, matrices//3
    upper = np.concatenate((a, (3-b) % 3), axis=3)
    lower = np.concatenate((b, a), axis=3)
    actions = np.concatenate((upper, lower), axis=2)
    initial = np.concatenate((seedrows//3, seedrows % 3), axis=2)
    rows = np.concatenate((initial, np.zeros((n, 6, 14), dtype=np.uint8)), axis=1)
    rows, ranks, pivots = f9.batch_rref(rows)
    rounds = [{"round": 0, "rank_counts": dict(sorted(Counter(map(int, ranks)).items()))}]
    for round_number in range(1, 15):
        transformed = np.einsum('nrc,nicd->nird', rows.astype(np.int16),
                                actions.astype(np.int16)) % 3
        combined = np.concatenate((rows, transformed.reshape(n, 154, 14)), axis=1).astype(np.uint8)
        reduced, new_ranks, new_pivots = f9.batch_rref(combined)
        assert np.all(new_ranks >= ranks)
        rounds.append({"round": round_number,
                       "rank_counts": dict(sorted(Counter(map(int, new_ranks)).items()))})
        print(json.dumps(rounds[-1]), flush=True)
        stable = np.array_equal(new_ranks, ranks)
        rows, ranks, pivots = reduced[:, :14], new_ranks, new_pivots
        if stable:
            break
    else:
        raise AssertionError("source row closure did not stabilize")
    principal = np.concatenate(((chars % 3+2) % 3, chars//3), axis=1)
    assert np.all(np.einsum('nrd,nd->nr', rows.astype(np.int16),
                            principal.astype(np.int16)) % 3 == 0)
    survivors = np.flatnonzero(ranks < 13)

    def field_add(x, y):
        return (x % 3+y % 3) % 3+3*((x//3+y//3) % 3)

    def product_affine(g, h):
        return field_add(g[0], int(mul[g[1], h[0]])), int(mul[g[1], h[1]])

    def inverse_affine(g):
        x = int(mul[inverse[g[1]], g[0]])
        return ((-x % 3) % 3+3*((-(x//3)) % 3), int(inverse[g[1]]))

    def subgroup(generators):
        known = {(0, 1)}
        queue = deque(known)
        while queue:
            g = queue.popleft()
            for h in generators:
                z = product_affine(g, h)
                if z not in known:
                    known.add(z)
                    queue.append(z)
        return sorted(known)

    examples = []
    for index in survivors:
        basis = []
        free = [i for i in range(14) if i not in pivots[index, :ranks[index]]]
        for col in free:
            v = np.zeros(14, dtype=np.int64)
            v[col] = 1
            for r, p in enumerate(pivots[index, :ranks[index]]):
                v[p] = -int(rows[index, r, col]) % 3
            basis.append(v)
        principal_line = {tuple((c*principal[index]) % 3) for c in range(3)}
        vector = next(v for v in basis if tuple(v) not in principal_line)
        translation = vector[:7]+3*vector[7:]
        generators = [(int(translation[j]), int(chars[index, j])) for j in range(7)]
        H = subgroup(generators)
        normal_generators = [product_affine(product_affine(h, u), inverse_affine(h))
                             for h in H for u in generators[3:]]
        R = subgroup(normal_generators)
        orbit = {tuple(vector)}
        queue = deque(orbit)
        while queue:
            v = np.array(queue.popleft(), dtype=np.int64)
            for matrix in actions[index]:
                new = tuple(matrix.astype(np.int64)@v % 3)
                if new not in orbit:
                    orbit.add(new)
                    queue.append(new)
        seed_images = []
        for v in sorted(orbit):
            translations = np.array(v[:7])+3*np.array(v[7:])
            for r, seed in enumerate(seeds):
                value = 0
                for coefficient, tr in zip(seedrows[index, r], translations):
                    value = field_add(value, int(mul[coefficient, tr]))
                assert value < 3
                scalar = int(monomial(seed["u_character"])[index])
                seed_images.append((value, scalar))
        K = subgroup(seed_images)
        assert set(K).issubset(R)
        examples.append({"characters": chars[index].tolist(),
                         "translation_values": translation.tolist(),
                         "linear_rank": int(ranks[index]),
                         "translation_kernel_dimension": len(free),
                         "full_source_orbit": [list(v) for v in sorted(orbit)],
                         "ambient_image": [list(g) for g in H],
                         "R_image": [list(g) for g in R],
                         "K_image": [list(g) for g in K],
                         "orders": [len(H), len(R), len(K)],
                         "proper_marginal": len(K) < len(R)})
    result = {"status": "EXACT_SOURCE_CLOSURE_RESEARCH_STAGE",
              "producer_sha256": sha256(producer.read_bytes()).hexdigest(),
              "inputs": {str(p): sha256(p.read_bytes()).hexdigest()
                         for p in [candidate_source, source]},
              "candidate_characters": n, "rounds": rounds,
              "surviving_character_count": len(survivors),
              "examples": examples,
              "scope": "Every surviving example is evaluated using the complete finite source orbit in the fixed character's translation kernel. The group consequence requires independent audit of this exact affine representation and the retained F23 source maps before any claim is registered."}
    target = producer.with_name("affine_f9_source_closure_stage_output.json")
    target.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": result["status"], "survivors": len(survivors),
                      "image_order_counts": dict(Counter(str(e['orders']) for e in examples)),
                      "proper_marginal_examples": sum(e["proper_marginal"] for e in examples),
                      "output_sha256": sha256(target.read_bytes()).hexdigest()}, indent=2))


if __name__ == "__main__":
    main()
