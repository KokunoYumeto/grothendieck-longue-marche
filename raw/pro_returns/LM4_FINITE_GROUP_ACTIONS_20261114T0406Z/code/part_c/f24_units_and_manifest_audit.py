"""Independent F24 certificate-scope and intermediate-unit audit.

No producer or supplied verifier is imported.  The complete polynomial
replay is separately retained by root; this verifies every intermediate
elimination multiplier, its unchanged pivot row, source labels, and frozen
evidence-file hashes.
"""
from pathlib import Path
from hashlib import sha256
from math import comb
import json

ROOT = Path(__file__).resolve().parents[3]
COUNTS = {}


def check(value, category):
    assert value, category
    COUNTS[category] = COUNTS.get(category, 0) + 1


def polynomial(serialized):
    result = {}
    for coefficient, exponent in serialized:
        check(isinstance(coefficient, int) and coefficient != 0,
              "nonzero_integer_coefficient")
        check(len(exponent) == 7 and all(isinstance(e, int) for e in exponent),
              "integer_laurent_exponent")
        power = tuple(exponent)
        check(power not in result, "distinct_monomials")
        result[power] = coefficient
    return result


def is_localized_unit(p, j):
    check(bool(p), "nonzero_pivot")
    minimum = tuple(min(e[k] for e in p) for k in range(7))
    normalized = {tuple(e[k] - minimum[k] for k in range(7)): c
                  for e, c in p.items()}
    check(all(all(e[k] == 0 for k in range(7) if k != j)
              for e in normalized), "single_delta_variable")
    degree = max(e[j] for e in normalized)
    leading_power = tuple(degree if k == j else 0 for k in range(7))
    sign = normalized[leading_power]
    check(sign in (-1, 1), "unit_integer_coefficient")
    expected = {tuple(m if k == j else 0 for k in range(7)):
                sign * comb(degree, m) * (-1) ** (degree-m)
                for m in range(degree+1)}
    check(normalized == expected, "exact_monomial_delta_unit")
    return degree


def main():
    manifest_path = ROOT / "work/part_a/f_rank_one_marginal_obstruction_evidence_manifest.json"
    manifest = json.loads(manifest_path.read_text())
    for item in manifest["entries"]:
        p = ROOT / item["path"]
        check(p.stat().st_size == item["bytes"], "evidence_bytes")
        check(sha256(p.read_bytes()).hexdigest() == item["sha256"], "evidence_hash")
    code = ROOT / "work/part_a/code"
    derivation_path = code / "affine_obstruction_stage_output.json"
    certificate_path = code / "affine_rank_one_certificate_stage_output.json"
    derivation = json.loads(derivation_path.read_text())
    certificate = json.loads(certificate_path.read_text())
    check(certificate["source_automorphism_indices"] == [2,9,8,10,1,0,7],
          "exact_old_source_indices")
    seed_records = [r for r in derivation["records"] if r["index"] >= 11]
    expected_labels = [f"cross_{u}_-1_{sign}"
                       for u in (0,2,3,4) for sign in (1,-1)]
    check([r["label"] for r in seed_records] == expected_labels,
          "exact_negative_seed_order")
    check(len(certificate["source_rows"]) == 64, "sixty_four_rows")
    expected_pivots = [
        ([11,8,0,6,4,1], [5,4,1,7,6,3], 389, []),
        ([11,8,3,6,4,2,34], [5,4,1,7,6,2,3], 444, []),
        ([11,8,13,14,20,5,28], [5,4,6,7,2,1,3], 445, []),
        ([0,2,4,14,39,6,46], [4,5,6,7,2,1,3], 196, [4,5,6]),
    ]
    summaries = []
    for j, chart, expected in zip(range(3,7), certificate["charts"], expected_pivots):
        rows, columns, count, special = expected
        check(chart["localized_character"] == j+1, "chart_variable")
        check(chart["specialized_to_one"] == special, "exact_specialization")
        check([p["row"] for p in chart["pivots"]] == rows, "pivot_row_order")
        check([p["column"] for p in chart["pivots"]] == columns,
              "pivot_column_order")
        check(len(chart["operations"]) == count, "row_operation_count")
        pivots = {p["row"]: p for p in chart["pivots"]}
        final_polynomials = {i: polynomial(p["coefficient"]) for i,p in pivots.items()}
        for p in final_polynomials.values():
            is_localized_unit(p, j)
        frozen = set()
        eliminations = 0
        for op in chart["operations"]:
            check(op["row"] not in frozen, "used_pivot_never_modified")
            check(isinstance(op["delta_divisions"], int) and op["delta_divisions"] >= 0,
                  "only_localized_delta_division")
            check(len(op["shift"]) == 7 and all(isinstance(n,int) for n in op["shift"]),
                  "normalization_monomial_unit")
            if op["operation"] == "eliminate_then_normalize":
                i = op["pivot_row"]
                check(i in pivots, "declared_pivot_row")
                check(op["column"] == pivots[i]["column"], "same_pivot_column")
                p = polynomial(op["pivot_coefficient"])
                check(p == final_polynomials[i], "same_unchanged_pivot_value")
                is_localized_unit(p, j)
                frozen.add(i)
                eliminations += 1
            else:
                check(op["operation"] == "normalize", "normalization_operation")
        summaries.append({"chart":j+1,"specialized_to_one":special,
                          "operations":count,"elimination_unit_multipliers":eliminations,
                          "every_used_pivot_preserved":True})
    output = {"status":"PASS", "scope":"Every intermediate elimination pivot is an exact localized unit and is never modified after use; all original source labels, chart orders and frozen evidence hashes verified.",
              "manifest_sha256":sha256(manifest_path.read_bytes()).hexdigest(),
              "evidence_entries":len(manifest["entries"]),
              "derivation_sha256":sha256(derivation_path.read_bytes()).hexdigest(),
              "certificate_sha256":sha256(certificate_path.read_bytes()).hexdigest(),
              "producer_sha256":sha256(Path(__file__).read_bytes()).hexdigest(),
              "charts":summaries,"checks":COUNTS,"total_checks":sum(COUNTS.values())}
    target = Path(__file__).with_name("f24_units_and_manifest_audit_output.json")
    target.write_text(json.dumps(output,indent=2)+"\n")
    print(json.dumps(output,indent=2))


if __name__ == "__main__":
    main()
