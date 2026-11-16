"""Notes-only exploration: no theorem or section-existence claim."""
from pathlib import Path
import hashlib
import json
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form


def invariants(matrix):
    D = smith_normal_form(matrix, domain=sp.ZZ)
    free = 0
    torsion = []
    for i in range(D.rows):
        a = abs(int(D[i, i]))
        if not a:
            free += 1
            continue
        v = 0
        while a % 5 == 0:
            v += 1
            a //= 5
        if v:
            torsion.append(v)
    return free, torsion


def run():
    rows = []
    for r, N in [(1, 2), (1, 3), (2, 3)]:
        n = 5**N
        eye = sp.eye(n)
        T = sp.Matrix(n, n, lambda i, j: int(i == (j+1) % n))
        perm = sp.Matrix(n, n, lambda i, j: int(i == (2*j) % n))
        source = (eye + T**(5**r)) * (eye + T)**3 * perm
        target = (eye + T)**3 * perm
        natural = T**(5**r) - eye
        assert natural * source == target * natural
        free, torsion = invariants(source-eye)
        rows.append({
            "r": r, "N": N, "dimension": n,
            "source_free_rank": free,
            "source_five_torsion_valuations": torsion,
            "actual_map_intertwining": True,
            "scope": "Literal finite matrix result only; no all-depth classification asserted.",
        })
    return {
        "status": "EXPLORATION",
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "rows": rows,
    }


if __name__ == "__main__":
    result = run()
    Path(__file__).with_suffix(".json").write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(result, indent=2, sort_keys=True))
