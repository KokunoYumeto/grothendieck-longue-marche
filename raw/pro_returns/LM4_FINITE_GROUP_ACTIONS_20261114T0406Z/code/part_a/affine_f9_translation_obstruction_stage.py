"""Research stage: nonzero translation intersections over F_9.

The input consists of the exact F24 rows. Characters on deleted variables
are in F_3^* and at least one is nontrivial; some retained character lies
outside F_3. For a possible proper intersection U=F_3 in translations,
the imaginary parts of all source-row values must vanish. These are exact
linear equations over F_3 on fourteen translation coordinates.
No general scalar-affine fullness theorem is asserted by this test.
"""
from pathlib import Path
from itertools import product
from collections import Counter
from hashlib import sha256
import json
import numpy as np


def field_tables():
    # a+3*b encodes a+b*i, with i^2=-1=2 in F_3.
    mul = np.zeros((9, 9), dtype=np.uint8)
    for a in range(9):
        for b in range(9):
            ar, ai, br, bi = a % 3, a // 3, b % 3, b // 3
            mul[a, b] = (ar*br-ai*bi) % 3 + 3*((ar*bi+ai*br) % 3)
    inverse = np.array([0]+[next(j for j in range(1, 9) if mul[i, j] == 1)
                            for i in range(1, 9)], dtype=np.uint8)
    powers = np.ones((9, 8), dtype=np.uint8)
    for exponent in range(1, 8):
        powers[:, exponent] = mul[powers[:, exponent-1], np.arange(9)]
    assert np.all(mul[np.arange(1, 9), inverse[1:]] == 1)
    assert np.all(mul[powers[1:, 7], np.arange(1, 9)] == 1)
    return mul, inverse, powers


def batch_rref(matrix):
    matrix = matrix.copy()
    n, m, d = matrix.shape
    ranks = np.zeros(n, dtype=np.int64)
    pivot_columns = np.full((n, d), -1, dtype=np.int64)
    rr = np.arange(m)[None, :]
    for col in range(d):
        eligible = (rr >= ranks[:, None]) & (matrix[:, :, col] != 0)
        active = np.flatnonzero(np.any(eligible, axis=1))
        piv = np.argmax(eligible[active], axis=1)
        dst = ranks[active]
        new = matrix[active, piv].copy()
        old = matrix[active, dst].copy()
        matrix[active, piv] = old
        factor = np.where(new[:, col] == 1, 1, 2).astype(np.uint8)
        new = (new*factor[:, None]) % 3
        matrix[active, dst] = new
        coefficients = matrix[active, :, col].copy()
        coefficients[np.arange(len(active)), dst] = 0
        matrix[active] = (matrix[active]+6-coefficients[:, :, None]*new[:, None, :]) % 3
        pivot_columns[active, dst] = col
        ranks[active] += 1
    return matrix, ranks, pivot_columns


def main():
    producer = Path(__file__).resolve()
    source = producer.with_name("affine_rank_one_certificate_stage_output.json")
    data = json.loads(source.read_text())
    chars = np.array([r+d for r in product(range(1, 9), repeat=3)
                      if any(x >= 3 for x in r)
                      for d in product((1, 2), repeat=4) if 2 in d], dtype=np.uint8)
    assert len(chars) == (8**3-2**3)*(2**4-1) == 7560
    mul, inverse, powers = field_tables()
    cache = {}

    def monomial(exponent):
        key = tuple(exponent)
        if key not in cache:
            value = np.ones(len(chars), dtype=np.uint8)
            for j, power in enumerate(key):
                value = mul[value, powers[chars[:, j], power % 8]]
            cache[key] = value
        return cache[key]

    rows = np.zeros((len(chars), 64, 7), dtype=np.uint8)
    for r, row in enumerate(data["source_rows"]):
        for j, polynomial in enumerate(row):
            real = np.zeros(len(chars), dtype=np.int32)
            imaginary = np.zeros(len(chars), dtype=np.int32)
            for coefficient, exponent in polynomial:
                value = monomial(exponent)
                real += (coefficient % 3)*(value % 3)
                imaginary += (coefficient % 3)*(value // 3)
            rows[:, r, j] = (real % 3)+3*(imaginary % 3)
    linear = np.concatenate((rows//3, rows % 3), axis=2)
    principal = np.concatenate(((chars % 3+2) % 3, chars//3), axis=1)
    assert np.all(np.einsum('nrd,nd->nr', linear.astype(np.int16),
                            principal.astype(np.int16)) % 3 == 0)
    reduced, rank, pivots = batch_rref(linear)
    assert np.all(rank <= 13)
    counts = dict(sorted(Counter(map(int, rank)).items()))
    deficient = np.flatnonzero(rank < 13)
    examples = []
    for index in deficient[:20]:
        free = [i for i in range(14) if i not in pivots[index, :rank[index]]]
        basis = []
        for col in free:
            v = np.zeros(14, dtype=np.int64)
            v[col] = 1
            for r, p in enumerate(pivots[index, :rank[index]]):
                v[p] = (-int(reduced[index, r, col])) % 3
            assert np.all(linear[index].astype(np.int64)@v % 3 == 0)
            basis.append(v.tolist())
        examples.append({"character_index": int(index), "characters": chars[index].tolist(),
                         "rank": int(rank[index]), "kernel_basis_over_F3": basis})
    result = {"status": "EXACT_RESEARCH_STAGE",
              "producer_sha256": sha256(producer.read_bytes()).hexdigest(),
              "source_sha256": sha256(source.read_bytes()).hexdigest(),
              "field": "F3[i]/(i^2+1), code a+3b means a+b*i",
              "characters_checked": len(chars), "rank_counts": counts,
              "cached_monomials": len(cache),
              "deficient_character_count": len(deficient),
              "deficient_characters": chars[deficient].tolist(),
              "deficient_examples": examples,
              "scope": "The 64 exact source rows tested for translation values in the fixed F3 line. Rank13 means only the principal translation tuples with center in F3 survive these necessary conditions. Any lower rank remains an actual-source linear candidate and requires further source orbit closure. No general affine-image equality is claimed."}
    target = producer.with_name("affine_f9_translation_obstruction_stage_output.json")
    target.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": result["status"], "characters_checked": len(chars),
                      "rank_counts": counts, "deficient": len(deficient),
                      "output_sha256": sha256(target.read_bytes()).hexdigest()}, indent=2))


if __name__ == "__main__":
    main()
