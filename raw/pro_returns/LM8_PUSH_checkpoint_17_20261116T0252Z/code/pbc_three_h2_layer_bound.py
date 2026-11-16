#!/usr/bin/env python3
"""Exact original-presentation certificate for the C31 three-primary H2 bound.

No large search, old basis, or old output is modified.  The primary ranks use
NumPy arithmetic modulo 3; each selected independent minor is checked again by
a separate plain-Python elimination.  Every matrix row is extracted from an
actual original pc conjugation relation, not from an abstract module label.
"""
from __future__ import annotations
import hashlib
import itertools
import json
import math
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "pbc_iterated_shortcut_v2_original_source.json"
EXPECTED_SHA = "95fb384593bfaf97d468bbc51f11cd797484a08cb3ec3b954961085b520ffc88"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def truncate(word, n):
    return [a for i, e in zip(word[::2], word[1::2]) if i <= n for a in (i, e)]


def rank_plain(rows, width):
    """Independent implementation, using Python lists and modular integers."""
    basis = {}
    for row in rows:
        a = [int(v) % 3 for v in row]
        assert len(a) == width
        for p in sorted(basis):
            if a[p]:
                c = a[p]
                a = [(v - c * w) % 3 for v, w in zip(a, basis[p])]
        p = next((i for i, v in enumerate(a) if v), None)
        if p is not None:
            c = a[p]
            basis[p] = [(c * v) % 3 for v in a]
    return len(basis)


def rank_certificate(rows, width):
    basis = {}
    selected = []
    labels = []
    count = 0
    digest = hashlib.sha256()
    for label, row in rows:
        raw = [int(v) % 3 for v in row]
        digest.update(bytes(raw))
        count += 1
        a = np.asarray(raw, dtype=np.int64)
        for p in sorted(basis):
            if a[p]:
                a = (a - int(a[p]) * basis[p]) % 3
        nz = np.flatnonzero(a)
        if len(nz):
            p = int(nz[0])
            basis[p] = (int(a[p]) * a) % 3
            selected.append(raw)
            labels.append(label)
    assert rank_plain(selected, width) == len(basis)
    return dict(width=width, rows_checked=count, rank=len(basis),
                coinvariant_dimension=width-len(basis),
                all_rows_sha256=digest.hexdigest(),
                independent_original_row_labels=labels,
                independent_original_rows=selected,
                independent_plain_python_rank=len(basis))


def main():
    assert sha(SOURCE) == EXPECTED_SHA
    s = json.loads(SOURCE.read_text())
    orders, powers = s["relative_orders"], s["powers"]
    n = len(orders)
    assert n == 176 and len(powers) == n
    assert math.prod(orders) == s["order"] == 2**146 * 3**30
    conjugates = {(i, j): w for i, j, w in s["conjugates"]}
    assert len(conjugates) == len(s["conjugates"]) == n*(n-1)//2
    assert set(conjugates) == {(i, j) for i in range(2, n+1) for j in range(1, i)}
    # Normal-form syntax and the triangular power relations are checked in full.
    for i, w in enumerate(powers, 1):
        assert len(w) % 2 == 0
        assert w[::2] == sorted(set(w[::2]))
        assert all(i < k <= n and 0 < e < orders[k-1]
                   for k, e in zip(w[::2], w[1::2]))
    for (i, j), w in conjugates.items():
        assert len(w) % 2 == 0
        assert w[::2] == sorted(set(w[::2]))
        assert all(j < k <= n and 0 < e < orders[k-1]
                   for k, e in zip(w[::2], w[1::2]))
    cuts = [2, 4, 17, 26, 86, 104, 176]
    normal = []
    for cut in cuts:
        checked = 0
        for (i, j), w in conjugates.items():
            if i > cut:
                assert all(k > cut for k in w[::2]), (cut, i, j)
                checked += 1
        normal.append(dict(cut=cut, conjugation_relations_checked=checked,
                           all_original_powers_checked=n,
                           normal_suffix=True))
    layers = []
    for low, high in zip([4, 17, 26, 86, 104], [17, 26, 86, 104, 176]):
        primes = set(orders[low:high])
        assert len(primes) == 1
        prime = next(iter(primes))
        nonzero_powers = [i for i in range(low+1, high+1)
                          if truncate(powers[i-1], high)]
        nontrivial_conjugates = [(i, j) for i in range(low+2, high+1)
                                for j in range(low+1, i)
                                if truncate(conjugates[(i, j)], high) != [i, 1]]
        elementary = not nonzero_powers and not nontrivial_conjugates
        if prime == 3:
            assert elementary
        layers.append(dict(source=high, target=low, kernel_prime=prime,
                           kernel_order=prime**(high-low), elementary_abelian=elementary,
                           nonzero_power_count=len(nonzero_powers),
                           nontrivial_internal_conjugate_count=len(nontrivial_conjugates)))

    module_certificates = []
    for low, high, normal_two_start in [(17, 26, 5), (86, 104, 27)]:
        d = high-low
        matrices = []
        for g in range(1, low+1):
            M = np.zeros((d, d), dtype=np.int64)
            for i in range(d):
                w = truncate(conjugates[(low+i+1, g)], high)
                assert all(low < k <= high for k in w[::2])
                for k, a in zip(w[::2], w[1::2]):
                    M[i, k-low-1] = a % 3
            assert rank_plain(M.tolist(), d) == d
            matrices.append(M)
        def ordinary_rows():
            for g in range(normal_two_start, low+1):
                M = matrices[g-1]
                for i in range(d):
                    row = M[i].copy()
                    row[i] = (row[i]-1) % 3
                    yield [g, low+i+1], row
        ordinary = rank_certificate(ordinary_rows(), d)
        assert ordinary["coinvariant_dimension"] == 0
        pairs = list(itertools.combinations(range(d), 2))
        def wedge_rows():
            for g, M in enumerate(matrices, 1):
                for q, (i, j) in enumerate(pairs):
                    row = [(int(M[i,a])*int(M[j,b])-int(M[i,b])*int(M[j,a])) % 3
                           for a, b in pairs]
                    row[q] = (row[q]-1) % 3
                    yield [g, low+i+1, low+j+1], row
        wedge = rank_certificate(wedge_rows(), len(pairs))
        assert wedge["coinvariant_dimension"] == (1 if d == 9 else 0)
        module_certificates.append(dict(
            source=high, quotient=low, module_dimension=d,
            action_convention="rows record a -> a^g; inverse convention has identical coinvariants",
            all_quotient_generator_action_matrices=[M.tolist() for M in matrices],
            normal_two_subgroup_generator_indices=list(range(normal_two_start, low+1)),
            normal_two_coinvariants=ordinary, exterior_square_coinvariants=wedge,
            H1_quotient_module_zero=True,
            exponent_cost=3 if wedge["coinvariant_dimension"] else 1))

    # Base G_4: A=<g3,g4>=C3^2, quotient C6.  The action of g2 is -I.
    assert orders[:4] == [3, 2, 3, 3]
    assert all(not truncate(w, 4) for w in powers[:4])
    base_conj = {(i,j): truncate(conjugates[(i,j)],4)
                 for i in range(2,5) for j in range(1,i)}
    assert base_conj == {(2,1):[2,1,4,2], (3,1):[3,1],
                        (3,2):[3,2], (4,1):[3,1,4,1],
                        (4,2):[4,2], (4,3):[4,1]}
    U = [[1,0],[1,1]]
    minus_I = [[2,0],[0,2]]
    minus_U_minus_I = [[1,0],[2,1]]
    assert rank_plain(minus_U_minus_I, 2) == 2
    # Check that the retained, separately executed GAP base program is exactly
    # the original quotient in every power and conjugate clause.
    program = (HERE/"pbc_three_h2_layer_bound_base.g").read_text()
    compact = lambda x: json.dumps(x, separators=(",", ":"))
    assert "PBC_orders:="+compact(orders[:4])+";;" in program
    for i in range(1,5):
        assert f"SetPower(PBC_rws,{i},ObjByExtRep(PBC_family,{compact(truncate(powers[i-1],4))}));;" in program
    for (i,j),w in base_conj.items():
        assert f"SetConjugate(PBC_rws,{i},{j},ObjByExtRep(PBC_family,{compact(w)}));;" in program
    base_result=json.loads((HERE/"pbc_three_h2_layer_bound_base.json").read_text())
    assert base_result["base_order"] == 54
    assert base_result["base_integral_multiplier"] == [3]
    # The elementary argument alone proves exponent <=3.  GAP equality C3 is
    # corroboration and is not needed for the improved upper bound.
    result = dict(status="PASS", original_source=str(SOURCE.name),
                  original_source_sha256=sha(SOURCE), checker_sha256=sha(__file__),
                  original_generators=n, original_conjugates_checked=len(conjugates),
                  original_powers_checked=n, original_order=s["order"],
                  normal_suffix_checks=normal, layers=layers,
                  module_certificates=module_certificates,
                  base=dict(order=54, normal_A_order=9, quotient_order=6,
                            g1_action=U, g2_action=minus_I,
                            minus_U_minus_I=minus_U_minus_I,
                            H1_C6_A_zero=True, H2_C6_Z3_zero=True,
                            elementary_three_primary_annihilator=3,
                            independently_computed_integral_multiplier=[3],
                            gap_program_sha256=sha(HERE/"pbc_three_h2_layer_bound_base.g"),
                            gap_output_sha256=sha(HERE/"pbc_three_h2_layer_bound_base.out")),
                  full_three_primary_annihilator=9,
                  retained_two_primary_annihilator=2**14,
                  full_integral_annihilator=2**14*9,
                  scope="Homological upper bound only. C31 remains Open; no search modulus changed by this checker.")
    out=HERE/"pbc_three_h2_layer_bound.json"
    out.write_text(json.dumps(result,indent=2)+"\n")
    print("PASS: every original power/conjugation checked; all actual normal cuts verified")
    for m in module_certificates:
        print(f"A{m['module_dimension']}: normal-two coinvariants0; wedge coinvariants"
              f"{m['exterior_square_coinvariants']['coinvariant_dimension']}; H2 exponent cost{m['exponent_cost']}")
    print("BASE54: elementary H2 exponent<=3, independent GAP multiplier C3")
    print("FULL THREE-PRIMARY ANNIHILATOR 9; FULL INTEGRAL ANNIHILATOR 147456")
    print("C31 remains Open; positive gate still requires ORIGINAL source-row replay")


if __name__ == "__main__":
    main()
