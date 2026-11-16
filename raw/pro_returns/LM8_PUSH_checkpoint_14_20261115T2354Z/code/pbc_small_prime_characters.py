"""Exact dimensions for the repeated-tame-weight character argument."""
from pathlib import Path
import hashlib
import json
import sympy as sp

HERE = Path(__file__).resolve().parent
formula_path = HERE/"pbc_gentle_dimension_formula.json"
direct_path = HERE/"pbc_gentle_even_fast.json"
formula = {r["weight"]: r for r in json.loads(formula_path.read_text())["weights"]}
direct = {r["weight"]: r for r in json.loads(direct_path.read_text())["weights"]}
out = []
for p, top in [(5,12),(7,12),(11,20)]:
    invariant_weights = list(range(p-1, top+1, p-1))
    rank = sum(formula[n]["gentle_dimension"] for n in invariant_weights)
    bracket_bound = sum(formula[n]["possible_bracket_count"] for n in invariant_weights)
    lower = []
    for n in invariant_weights[:-1]:
        row = direct[n]
        vectors = row["bracket_coordinates"]
        actual_rank = sp.Matrix.hstack(*(sp.Matrix(v) for v in vectors)).rank() if vectors else 0
        assert actual_rank == row["gentle_dimension"]
        lower.append({"weight":n,"dimension":row["gentle_dimension"],
                      "independently_recomputed_bracket_rank":actual_rank})
    assert top//3 < p and rank-bracket_bound > 0
    out.append({
        "prime":p,
        "top_conjugator_degree":top,
        "operator_nilpotency_class_bound":top//3,
        "tame_invariant_weights":invariant_weights,
        "invariant_lattice_rank":rank,
        "bracket_rank_upper_bound":bracket_bound,
        "integral_character_rank_lower_bound":rank-bracket_bound,
        "lower_invariant_grades_are_all_bracketed":lower,
    })
result = {
    "scope":"exact finite-rank inputs; full character assertion uses the repeated-weight group proof",
    "formula_sha256":hashlib.sha256(formula_path.read_bytes()).hexdigest(),
    "direct_lie_sha256":hashlib.sha256(direct_path.read_bytes()).hexdigest(),
    "primes":out,
}
Path(__file__).with_suffix(".json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2))
