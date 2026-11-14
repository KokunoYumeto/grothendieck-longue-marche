"""Exploratory exact two-character row elimination; no theorem is asserted.

Characters are t1,...,t7 and t1*q1,t2*q2,t3*q3,t4,...,t7.
The two cocycles have the common-principal kernel.  Localizing t4-1
allows its gauge d_first(X4)=0.  This stage also inverts q1-1 and
searches for thirteen unit pivots in the exact source rows.
"""
from pathlib import Path
from math import comb
from hashlib import sha256
import json

N = 10
ZERO = (0,)*N
UNITS = [tuple(int(i == j) for i in range(N)) for j in range(N)]
ACTIVE = [3, 7]


def plus(p, q):
    out = dict(p)
    for e, c in q.items():
        new = out.get(e, 0)+c
        if new:
            out[e] = new
        else:
            out.pop(e, None)
    return out


def shift(p, e=ZERO, c=1):
    return {tuple(a+b for a, b in zip(v, e)): c*x for v, x in p.items() if c*x}


def times(p, q):
    if len(p) > len(q):
        p, q = q, p
    out = {}
    for e, c in p.items():
        out = plus(out, shift(q, e, c))
    return out


def divide(p, j):
    if not p:
        return {}
    groups = {}
    for e, c in p.items():
        other = e[:j]+e[j+1:]
        groups.setdefault(other, {})[e[j]] = c
    if any(sum(g.values()) for g in groups.values()):
        return None
    out = {}
    for other, g in groups.items():
        running = 0
        for k in range(min(g), max(g)):
            running -= g.get(k, 0)
            if running:
                out[other[:j]+(k,)+other[j:]] = running
    assert times({UNITS[j]: 1, ZERO: -1}, out) == p
    return out


def normalize(row):
    if not any(row):
        return row
    minimum = tuple(min(e[j] for p in row for e in p) for j in range(N))
    row = [shift(p, tuple(-e for e in minimum)) for p in row]
    for j in ACTIVE:
        while True:
            divided = [divide(p, j) for p in row]
            if any(p is None for p in divided):
                break
            row = divided
    return row


def unit(p):
    if not p:
        return None
    minimum = tuple(min(e[j] for e in p) for j in range(N))
    work = shift(p, tuple(-e for e in minimum))
    orders = []
    for j in ACTIVE:
        order = 0
        while True:
            quotient = divide(work, j)
            if quotient is None:
                break
            work = quotient
            order += 1
        orders.append(order)
    if work in ({ZERO: 1}, {ZERO: -1}):
        return {"monomial": list(minimum), "delta_powers": orders, "sign": work[ZERO]}
    return None


def lift(poly, second):
    return {tuple(e)+(tuple(e[:3]) if second else (0, 0, 0)): c
            for c, e in poly}


def main():
    producer = Path(__file__).resolve()
    source = producer.with_name("affine_rank_one_certificate_stage_output.json")
    data = json.loads(source.read_text())
    rows = []
    for source_row in data["source_rows"]:
        left = [lift(p, False) for p in source_row]
        right = [lift(p, True) for p in source_row]
        rows.append(normalize(left[:3]+left[4:]+right))
    used_rows = set()
    used_columns = set()
    pivots = []
    operations = []
    stopped = "NO_FURTHER_LOCALIZED_UNIT_PIVOT"
    while len(pivots) < 13:
        choices = []
        for i, row in enumerate(rows):
            if i in used_rows:
                continue
            for j, p in enumerate(row):
                if j in used_columns:
                    continue
                shape = unit(p)
                if shape is not None:
                    choices.append((sum(map(len, row)), sum(shape['delta_powers']), i, j, shape))
        if not choices:
            break
        _, _, i, j, shape = min(choices)
        pivots.append({"row": i, "label": data["source_row_labels"][i],
                       "column": j+1, "shape": shape})
        used_rows.add(i)
        used_columns.add(j)
        p = rows[i][j]
        for r, row in enumerate(rows):
            if r in used_rows or not row[j]:
                continue
            c = row[j]
            new = [plus(times(p, a), shift(times(c, b), c=-1)) for a, b in zip(row, rows[i])]
            assert not new[j]
            rows[r] = normalize(new)
            operations.append([i, j+1, r])
        terms = sum(sum(map(len, row)) for row in rows)
        print(json.dumps({"pivots": len(pivots), "monomials": terms,
                          "last_row": i, "last_column": j+1}), flush=True)
        if terms > 300000:
            stopped = "EXACT_POLYNOMIAL_SIZE_GUARD"
            break
    if len(pivots) == 13:
        stopped = "THIRTEEN_PIVOTS_NEEDS_INDEPENDENT_CERTIFICATE"
    remaining = []
    for i, row in enumerate(rows):
        if i not in used_rows:
            remaining.append({"row": i,
                              "coefficients": [[[c, list(e)] for e, c in sorted(p.items())]
                                               for p in row]})
    result = {"status": "UNREGISTERED_EXACT_PAIR_EXPLORATION", "stop_reason": stopped,
              "producer_sha256": sha256(producer.read_bytes()).hexdigest(),
              "input_sha256": sha256(source.read_bytes()).hexdigest(),
              "variables": ["t1", "t2", "t3", "t4", "t5", "t6", "t7", "q1", "q2", "q3"],
              "inverted_differences": ["t4-1", "q1-1"],
              "gauge_deleted_column": "first cocycle X4", "pivots": pivots,
              "elimination_steps": operations, "remaining_rows": remaining,
              "scope": "Research search for an exact paired-character restriction identity. The other character-difference charts, deleted-character strata, arbitrary family size and independent certificate are not supplied by this stage."}
    target = producer.with_name("affine_pair_rows_stage_output.json")
    target.write_text(json.dumps(result, separators=(',', ':'))+'\n')
    print(json.dumps({"status": result["status"], "pivots": len(pivots),
                      "stop_reason": stopped, "output_bytes": target.stat().st_size,
                      "output_sha256": sha256(target.read_bytes()).hexdigest()}, indent=2))


if __name__ == '__main__':
    main()
