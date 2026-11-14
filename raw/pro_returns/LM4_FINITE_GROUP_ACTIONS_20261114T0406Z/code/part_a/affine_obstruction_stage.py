"""Universal rank-one crossed-homomorphism data for the actual F23 source.

Unregistered research staging.  The coefficient ring is
Z[t_1^+-1,...,t_7^+-1].  The retained negative marginal Artin coordinates
are used literally.  Every calculation is exact sparse Laurent arithmetic.
No larger finite target scan or full marginal-equality claim is made.
"""
from pathlib import Path
import hashlib
import json

N = 7
ZERO = (0,)*N
UNITS = [tuple(int(j == i) for j in range(N)) for i in range(N)]


def char_add(a, b):
    return tuple(x+y for x, y in zip(a, b))


def char_neg(a):
    return tuple(-x for x in a)


def add(*terms):
    result = {}
    for scale, shift, value in terms:
        for power, coefficient in value.items():
            key = char_add(power, shift)
            new = result.get(key, 0)+scale*coefficient
            if new:
                result[key] = new
            elif key in result:
                del result[key]
    return result


def vector_add(*terms):
    return [add(*[(scale, shift, value[i]) for scale, shift, value in terms])
            for i in range(N)]


def basis_vector(i):
    return [{ZERO: 1} if i == j else {} for j in range(N)]


def zero_vector():
    return [{} for _ in range(N)]


def fundamental(row):
    result = {}
    for i in range(N):
        result = add((1, ZERO, result), (1, UNITS[i], row[i]),
                     (-1, ZERO, row[i]))
    return result


def serialize(poly):
    return [[value, list(power)] for power, value in sorted(poly.items())]


def serialize_row(row):
    return [serialize(p) for p in row]


def term_count(rows):
    return sum(len(poly) for row in rows for poly in row)


def record_braid(word):
    chars = UNITS[:]+[ZERO]
    vectors = [basis_vector(i) for i in range(N)]+[zero_vector()]
    conjugator_chars = [ZERO]*(N+1)
    conjugator_vectors = [zero_vector() for _ in range(N+1)]
    order = list(range(N+1))
    max_terms = 0
    for crossing in word:
        j = abs(crossing)-1
        a, b = chars[j], chars[j+1]
        x, y = vectors[j], vectors[j+1]
        ca, cb = conjugator_chars[j], conjugator_chars[j+1]
        cx, cy = conjugator_vectors[j], conjugator_vectors[j+1]
        if crossing > 0:
            vectors[j] = vector_add((1, ZERO, x), (-1, b, x), (1, a, y))
            vectors[j+1] = x
            conjugator_vectors[j] = vector_add((1, ZERO, x), (1, a, cy))
            conjugator_vectors[j+1] = cx
            conjugator_chars[j], conjugator_chars[j+1] = char_add(a, cb), ca
        else:
            minus_b = char_neg(b)
            vectors[j] = y
            vectors[j+1] = vector_add((1, minus_b, x),
                                      (1, char_add(a, minus_b), y),
                                      (-1, minus_b, y))
            conjugator_vectors[j] = cy
            conjugator_vectors[j+1] = vector_add((1, minus_b, cx), (-1, minus_b, y))
            conjugator_chars[j], conjugator_chars[j+1] = cb, char_add(minus_b, ca)
        chars[j], chars[j+1] = b, a
        order[j], order[j+1] = order[j+1], order[j]
        max_terms = max(max_terms, term_count(vectors)+term_count(conjugator_vectors))
    assert order == list(range(N+1))
    assert chars == UNITS+[ZERO]
    assert vectors[N] == zero_vector()
    u_char = char_neg(conjugator_chars[N])
    u_vector = vector_add((-1, u_char, conjugator_vectors[N]))
    target = add((1, u_char, {ZERO: 1}), (-1, ZERO, {ZERO: 1}))
    assert fundamental(u_vector) == target
    action = [vector_add((1, ZERO, u_vector), (-1, UNITS[i], u_vector),
                         (1, u_char, vectors[i])) for i in range(N)]
    for i, row in enumerate(action):
        assert fundamental(row) == {UNITS[i]: 1, ZERO: -1}
    return u_char, u_vector, action, max_terms


def main():
    producer = Path(__file__).resolve()
    source = producer.with_name("full_cross_source_stage")/"marginal_braids.json"
    data = json.loads(source.read_text())
    rows = []
    for record in data["records"]:
        label = record["label"]
        is_old = record["index"] < 11
        if not is_old and int(label.split("_")[2]) != -1:
            continue
        word = record["negative_braid"]
        char, seed, action, maximum = record_braid(word)
        if not is_old:
            exponent = int(label.split("_")[1])
            old_index = {0: 3, 2: 4, 3: 5, 4: 6}[exponent]
            assert char == UNITS[old_index]
        item = {"index": record["index"], "label": label, "braid_length": len(word),
                "u_character": list(char), "u_derivation_row": serialize_row(seed),
                "action_matrix": [serialize_row(row) for row in action] if is_old else None,
                "peak_intermediate_monomials": maximum,
                "output_monomials": term_count(action) if is_old else term_count([seed])}
        rows.append(item)
        print(json.dumps({k: item[k] for k in ("index", "label", "braid_length",
                                               "peak_intermediate_monomials", "output_monomials")}),
              flush=True)
    output = producer.with_name("affine_obstruction_stage_output.json")
    result = {
        "status": "EXACT_UNIVERSAL_DERIVATION_DATA_UNREGISTERED",
        "coefficient_ring": "Z[t_1^+-1,...,t_7^+-1]",
        "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "producer_sha256": hashlib.sha256(producer.read_bytes()).hexdigest(),
        "coordinate": "The actual negative marginal V_- Artin coordinates of F22/F23.",
        "meaning": "X_i has multiplicative character t_i and universal derivation e_i. A seed row evaluates its crossed-homomorphism value. An old-source matrix evaluates the actual precomposition action on derivation tuples. Every stored row satisfies the exact Fox fundamental identity. No module-span or full-image conclusion is claimed.",
        "records": rows,
    }
    output.write_text(json.dumps(result, separators=(",", ":"))+"\n")
    print(json.dumps({"status": result["status"], "records": len(rows),
                      "bytes": output.stat().st_size,
                      "output_sha256": hashlib.sha256(output.read_bytes()).hexdigest()}, indent=2))


if __name__ == "__main__":
    main()
