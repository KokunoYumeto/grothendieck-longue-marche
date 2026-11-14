"""Unregistered exact row-module exploration, retaining the F23 source.

Search for seven universally nonzero Gaussian pivots after inverting
one deleted-character difference t_j-1. No finite-field sampling is used.
"""
from pathlib import Path
from math import comb
import hashlib
import json
import affine_obstruction_stage as a


def parse(poly):
    return {tuple(e): c for c, e in poly}


def mul(p, q):
    return a.add(*[(c, e, q) for e, c in p.items()]) if p and q else {}


def dot(row, col):
    result = {}
    for p, q in zip(row, col):
        result = a.add((1, a.ZERO, result), (1, a.ZERO, mul(p, q)))
    return result


def row_times_matrix(row, matrix):
    return [dot(row, [r[j] for r in matrix]) for j in range(7)]


def divide_delta(poly, j):
    if not poly:
        return {}
    groups = {}
    for e, c in poly.items():
        other = e[:j]+e[j+1:]
        group = groups.setdefault(other, {})
        group[e[j]] = c
    result = {}
    for other, coefficients in groups.items():
        if sum(coefficients.values()):
            return None
        lo, hi = min(coefficients), max(coefficients)
        previous = 0
        for k in range(lo, hi):
            previous -= coefficients.get(k, 0)
            if previous:
                power = other[:j]+(k,)+other[j:]
                result[power] = previous
        assert previous == coefficients[hi]
    delta = {a.UNITS[j]: 1, a.ZERO: -1}
    assert mul(delta, result) == poly
    return result


def normalize(row, j):
    if not any(row):
        return row, {"shift": list(a.ZERO), "delta_divisions": 0}
    minimum = tuple(min(e[k] for p in row for e in p) for k in range(7))
    shift = a.char_neg(minimum)
    row = [a.add((1, shift, p)) for p in row]
    divisions = 0
    while True:
        quotient = [divide_delta(p, j) for p in row]
        if any(p is None for p in quotient):
            break
        row = quotient
        divisions += 1
    return row, {"shift": list(shift), "delta_divisions": divisions}


def unit_shape(poly, j):
    if not poly:
        return None
    minimum = tuple(min(e[k] for e in poly) for k in range(7))
    shifted = a.add((1, a.char_neg(minimum), poly))
    if any(any(e[k] for k in range(7) if k != j) for e in shifted):
        return None
    degree = max(e[j] for e in shifted)
    leading = shifted.get(tuple(degree if k == j else 0 for k in range(7)))
    if leading not in (-1, 1):
        return None
    expected = {tuple(k if m == j else 0 for m in range(7)):
                leading*((-1)**(degree-k))*comb(degree, k) for k in range(degree+1)}
    if shifted != expected:
        return None
    return {"sign": leading, "monomial": list(minimum), "delta_power": degree}


def eliminate(rows, labels, j):
    current = []
    operations = []
    for i, row in enumerate(rows):
        normalized, op = normalize(row, j)
        current.append(normalized)
        operations.append({"operation": "normalize", "row": i, **op})
    used_rows = set()
    used_columns = set()
    pivots = []
    while len(pivots) < 7:
        possibilities = []
        for i, row in enumerate(current):
            if i in used_rows:
                continue
            for k, p in enumerate(row):
                if k in used_columns:
                    continue
                shape = unit_shape(p, j)
                if shape is not None:
                    possibilities.append((sum(map(len, row)), shape["delta_power"], i, k, shape))
        if not possibilities:
            break
        _, _, i, k, shape = min(possibilities)
        p = current[i][k]
        pivots.append({"row": i, "label": labels[i], "column": k+1,
                       "coefficient": a.serialize(p), "unit_shape": shape,
                       "row_monomials": sum(map(len, current[i]))})
        used_rows.add(i)
        used_columns.add(k)
        for r, row in enumerate(current):
            if r in used_rows or not row[k]:
                continue
            coefficient = row[k]
            new = [a.add((1, a.ZERO, mul(p, v)),
                         (-1, a.ZERO, mul(coefficient, w)))
                   for v, w in zip(row, current[i])]
            assert not new[k]
            new, op = normalize(new, j)
            current[r] = new
            operations.append({"operation": "eliminate_then_normalize", "row": r,
                               "pivot_row": i, "column": k+1,
                               "pivot_coefficient": a.serialize(p),
                               "old_coefficient": a.serialize(coefficient), **op})
        print(json.dumps({"localized_character": j+1, "pivots": len(pivots),
                          "total_monomials": a.term_count(current),
                          "new_pivot_label": labels[i], "column": k+1}), flush=True)
        assert a.term_count(current) < 1500000
    return {"localized_character": j+1, "pivot_count": len(pivots),
            "pivots": pivots, "operations": operations,
            "remaining_rows": [{"row": i, "label": labels[i],
                                "coefficients": a.serialize_row(row)}
                               for i, row in enumerate(current) if i not in used_rows],
            "conclusion": "FULL_UNIVERSAL_ROW_RANK" if len(pivots) == 7 else "ROW_SEARCH_INCOMPLETE"}


def main():
    producer = Path(__file__).resolve()
    source = producer.with_name("affine_obstruction_stage_output.json")
    data = json.loads(source.read_text())
    old = {r["index"]: r for r in data["records"] if r["index"] < 11}
    seeds = [r for r in data["records"] if r["index"] >= 11]
    seedrows = [[parse(p) for p in r["u_derivation_row"]] for r in seeds]
    rows = list(seedrows)
    labels = [r["label"] for r in seeds]
    selected = [2, 9, 8, 10, 1]
    for index in selected:
        matrix = [[parse(p) for p in row] for row in old[index]["action_matrix"]]
        for seed, row in zip(seeds, seedrows):
            rows.append(row_times_matrix(row, matrix))
            labels.append(seed["label"]+" after "+old[index]["label"])
    print(json.dumps({"source_rows": len(rows), "monomials": a.term_count(rows)}), flush=True)
    results = [eliminate(rows, labels, j) for j in range(3, 7)]
    output = producer.with_name("affine_localized_rows_stage_output.json")
    result = {"status": "UNREGISTERED_EXACT_LOCALIZED_ROW_SEARCH",
              "coefficient_ring": "Z[t_1^+-1,...,t_7^+-1,(t_j-1)^-1] in chart j",
              "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
              "producer_sha256": hashlib.sha256(producer.read_bytes()).hexdigest(),
              "source_automorphism_indices": selected,
              "row_labels": labels, "source_rows": [a.serialize_row(row) for row in rows],
              "results": results,
              "scope": "Every row is an actual collision derivation or its precomposition by a named original source automorphism. Each row operation has a pivot equal to a signed Laurent monomial times a power of the one inverted deleted-character difference. A seven-pivot chart proves rank seven in every field on that chart. Any unfinished chart is recorded without a full-rank conclusion."}
    output.write_text(json.dumps(result, separators=(",", ":"))+"\n")
    print(json.dumps({"status": result["status"],
                      "pivot_counts": [r["pivot_count"] for r in results],
                      "output_sha256": hashlib.sha256(output.read_bytes()).hexdigest()}, indent=2))


if __name__ == "__main__":
    main()
