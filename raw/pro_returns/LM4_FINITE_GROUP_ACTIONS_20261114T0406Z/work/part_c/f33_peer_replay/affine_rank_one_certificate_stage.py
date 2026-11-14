"""Exact all-field rank-one obstruction certificate, unregistered staging.

The rows come from the literal negative F23 marginal source. Charts
t4!=1,t5!=1,t6!=1 have universal Laurent row certificates; the remaining
stratum t4=t5=t6=1,t7!=1 has its own exact specialization certificate.
"""
from pathlib import Path
import hashlib
import json
import affine_obstruction_stage as a
import affine_localized_rows_stage as r


def at_one(poly, indices):
    result = {}
    for power, coefficient in poly.items():
        key = tuple(0 if k in indices else value for k, value in enumerate(power))
        value = result.get(key, 0)+coefficient
        if value:
            result[key] = value
        elif key in result:
            del result[key]
    return result


def scalar_unit(poly, active):
    return r.unit_shape(poly, active)


def close_one_column(result):
    assert result["pivot_count"] == 6
    active = result["localized_character"]-1
    used = {p["column"]-1 for p in result["pivots"]}
    column = next(j for j in range(7) if j not in used)
    scalar_rows = []
    operations = []
    for row in result["remaining_rows"]:
        parsed = [r.parse(p) for p in row["coefficients"]]
        assert all(not p for j, p in enumerate(parsed) if j != column)
        if parsed[column]:
            scalar_rows.append({"id": len(scalar_rows), "origin_row": row["row"],
                                "coefficient": parsed[column]})
    initial = [{"id": s["id"], "origin_row": s["origin_row"],
                "coefficient": a.serialize(s["coefficient"])} for s in scalar_rows]
    known = {}
    unit = None
    for step in range(8):
        added = False
        for item in list(scalar_rows):
            p = item["coefficient"]
            original_id = item["id"]
            for j, reducer in known.items():
                reduced = at_one(p, {j})
                difference = a.add((1, a.ZERO, p), (-1, a.ZERO, reduced))
                quotient = r.divide_delta(difference, j)
                assert quotient is not None
                assert a.add((1, a.ZERO, p),
                             (-1, a.ZERO, r.mul(quotient, {a.UNITS[j]: 1, a.ZERO: -1}))) == reduced
                if reduced != p:
                    new_id = len(scalar_rows)
                    operations.append({"operation": "subtract_delta_multiple",
                                       "from_row": original_id, "to_row": new_id,
                                       "delta_row": reducer, "character": j+1,
                                       "quotient": a.serialize(quotient),
                                       "result": a.serialize(reduced)})
                    scalar_rows.append({"id": new_id, "coefficient": reduced})
                    p, original_id = reduced, new_id
            shape = scalar_unit(p, active)
            if shape is not None:
                unit = {"row": original_id, "coefficient": a.serialize(p),
                        "unit_shape": shape}
                break
            for j in range(7):
                if j in known or j == active:
                    continue
                shape = r.unit_shape(p, j)
                if shape is not None and shape["delta_power"] == 1:
                    multiplier = {a.char_neg(tuple(shape["monomial"])): shape["sign"]}
                    normalized = r.mul(multiplier, p)
                    assert normalized == {a.UNITS[j]: 1, a.ZERO: -1}
                    new_id = len(scalar_rows)
                    scalar_rows.append({"id": new_id, "coefficient": normalized})
                    operations.append({"operation": "normalize_delta",
                                       "from_row": original_id, "to_row": new_id,
                                       "character": j+1,
                                       "multiplier": a.serialize(multiplier)})
                    known[j] = new_id
                    added = True
            if unit is not None:
                break
        if unit is not None or not added:
            break
    assert unit is not None
    result["last_column_ideal_certificate"] = {
        "column": column+1, "initial_scalar_rows": initial,
        "delta_reducers": {str(j+1): i for j, i in known.items()},
        "operations": operations, "unit_row": unit}
    result["pivot_count"] = 7
    result["conclusion"] = "FULL_UNIVERSAL_ROW_RANK"
    print(json.dumps({"localized_character": active+1,
                      "last_column": column+1,
                      "delta_reducers": sorted(j+1 for j in known),
                      "last_unit": unit["coefficient"]}), flush=True)
    return result


def main():
    producer = Path(__file__).resolve()
    source = producer.with_name("affine_obstruction_stage_output.json")
    data = json.loads(source.read_text())
    old = {x["index"]: x for x in data["records"] if x["index"] < 11}
    seeds = [x for x in data["records"] if x["index"] >= 11]
    seedrows = [[r.parse(p) for p in x["u_derivation_row"]] for x in seeds]
    rows = list(seedrows)
    labels = [x["label"] for x in seeds]
    selected = [2, 9, 8, 10, 1, 0, 7]
    for index in selected:
        matrix = [[r.parse(p) for p in row] for row in old[index]["action_matrix"]]
        for seed, row in zip(seeds, seedrows):
            rows.append(r.row_times_matrix(row, matrix))
            labels.append(seed["label"]+" after "+old[index]["label"])
    results = []
    for j in (3, 4, 5):
        result = r.eliminate(rows, labels, j)
        if result["pivot_count"] == 6:
            result = close_one_column(result)
        assert result["pivot_count"] == 7
        result["specialized_to_one"] = []
        results.append(result)
    specialized = [[at_one(p, {3, 4, 5}) for p in row] for row in rows]
    last = r.eliminate(specialized, labels, 6)
    assert last["pivot_count"] == 7
    last["specialized_to_one"] = [4, 5, 6]
    results.append(last)
    output = producer.with_name("affine_rank_one_certificate_stage_output.json")
    result = {
        "status": "PASS_ALL_FIELD_RANK_ONE_OBSTRUCTION_PENDING_INDEPENDENT_AUDIT",
        "producer_sha256": hashlib.sha256(producer.read_bytes()).hexdigest(),
        "universal_derivation_input_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "row_arithmetic_helper_sha256": hashlib.sha256(Path(r.__file__).read_bytes()).hexdigest(),
        "source_automorphism_indices": selected,
        "source_row_labels": labels, "source_rows": [a.serialize_row(row) for row in rows],
        "charts": results,
        "scope": "For every field and every seven nonzero character values with at least one of t4,t5,t6,t7 different from one, these exact source-conjugated seed rows span the full seven-dimensional space. Three Laurent charts invert t4-1,t5-1,t6-1; the last exact stratum sets those three variables to one and inverts t7-1. Each pivot is a signed Laurent monomial times a power of an inverted difference; the one scalar-ideal closure has complete exact subtraction identities. No finite-field sample is used. The group/cohomology consequence and the comparison with arbitrary higher-dimensional solvable linear images require their separate proof.",
    }
    output.write_text(json.dumps(result, separators=(",", ":"))+"\n")
    print(json.dumps({"status": result["status"],
                      "chart_pivot_counts": [c["pivot_count"] for c in results],
                      "output_sha256": hashlib.sha256(output.read_bytes()).hexdigest()}, indent=2))


if __name__ == "__main__":
    main()
