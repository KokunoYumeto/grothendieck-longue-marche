"""Independent dense Hermitian and integral Magnus checks for frozen D.62.

No author program is imported or executed.  The four marked input certificates
are read, and dense F_2 linear algebra is used in place of the author's packed
exterior implementation.  Group word identities are checked over Z in the
degree-two Magnus algebra before either exponent reduction.
"""
from pathlib import Path
from itertools import combinations
import hashlib
import json
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "D62_EXPERIMENTS"
OUT = Path(__file__).resolve().parent


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


manifest_path = SRC / "ledger/d_self_wedge_actual_corrections_manifest.json"
manifest = json.loads(manifest_path.read_text())
assert digest(manifest_path) == "66a05d0534733dc7f6002488f20b45644fefe10c6adae1ad4168497d0ad3c68c"
for record in manifest["files"] + manifest["immutable_inputs"]:
    assert digest(SRC / record["path"]) == record["sha256"], record["path"]


def read(stem):
    return json.loads((SRC / "code" / (stem + ".json")).read_text())


rawq = read("d_arithmetic_A4_twisted")
old = read("d_arithmetic_A4_projective")
new = read("d_orbit12_projective_kernel")
affine = read("d_arithmetic_affine_base")
author_cusp = read("d_self_wedge_cusp_correction")
author_s = read("d_self_wedge_torsion_correction")
author_blocks = read("d_self_wedge_coordinate_blocks")
author_words = read("d_self_wedge_word_identities")


def fmul(a, b):
    # Polynomial arithmetic in F_2[z]/(z^2+z+1).
    v = 0
    for i in range(2):
        if (a >> i) & 1:
            v ^= b << i
    if v & 4:
        v ^= 7
    return v


FM = np.array([[fmul(a, b) for b in range(4)] for a in range(4)],
              dtype=np.uint8)
BAR = np.array([fmul(a, a) for a in range(4)], dtype=np.uint8)
QT = np.array(rawq["Q_multiplication"], dtype=np.int16)
QI = np.array([int(np.flatnonzero(QT[g] == 0)[0]) for g in range(576)])
QL0 = [np.array(v, dtype=np.int16).T
       for v in affine["Q_linear_image_matrices"]]
QL = np.array([QL0[k] for k in affine["Q_to_linear_image"]])


def canon(v):
    a = tuple(x % 12 for x in v)
    return min(a, tuple(-x % 12 for x in a))


qlookup = {tuple(v): i for i, v in enumerate(rawq["Q_states"])}
s = qlookup[canon((0, 1, -1, 0))]
r = qlookup[canon((0, -1, 1, -1))]
tq = int(QT[s, r])
vr = np.array(affine["affine_r_translation"], dtype=np.int16)
vt = QL[s] @ vr % 3
assert (s, tq, vt.tolist()) == (1, 4, [1, 1, 0, 1])
for g in range(576):
    for h in (s, r):
        assert np.array_equal(QL[g] @ QL[h] % 3, QL[QT[g, h]])
g18, a18 = 0, np.zeros(4, dtype=np.int16)
for _ in range(18):
    a18 = (a18 + QL[g18] @ vt) % 3
    g18 = int(QT[g18, tq])
assert (g18, a18.tolist()) == (314, [0, 2, 1, 0])
source_s_class = {int(QT[QT[g, s], QI[g]]) for g in range(576)}
other_class = {int(QT[QT[g, 314], QI[g]]) for g in range(576)}
assert len(source_s_class) == 36 and len(other_class) == 3
assert source_s_class.isdisjoint(other_class)


def span_group(gens):
    ans = {0}
    todo = [0]
    for a in todo:
        for b in gens:
            v = int(QT[a, b])
            if v not in ans:
                ans.add(v)
                todo.append(v)
    return sorted(ans)


def rref(a):
    a = np.array(a, dtype=np.uint8, copy=True) & 1
    row = 0
    pivots = []
    for col in range(a.shape[1]):
        candidates = np.flatnonzero(a[row:, col])
        if not len(candidates):
            continue
        k = row + int(candidates[0])
        a[[row, k]] = a[[k, row]]
        targets = np.flatnonzero(a[:, col])
        targets = targets[targets != row]
        a[targets] ^= a[row]
        pivots.append(col)
        row += 1
        if row == a.shape[0]:
            break
    return a, pivots


def rank(a):
    return len(rref(a)[1])


def nullspace(a):
    red, pivots = rref(a)
    free = [j for j in range(a.shape[1]) if j not in pivots]
    out = np.zeros((a.shape[1], len(free)), dtype=np.uint8)
    for j, f in enumerate(free):
        out[f, j] = 1
        for i, p in enumerate(pivots):
            out[p, j] = red[i, f]
    assert not np.any((a @ out) & 1)
    return out


def inverse(a):
    n = len(a)
    red, pivots = rref(np.concatenate([a, np.eye(n, dtype=np.uint8)], axis=1))
    assert pivots[:n] == list(range(n))
    inv = red[:, n:]
    assert np.array_equal((a @ inv) & 1, np.eye(n, dtype=np.uint8))
    assert np.array_equal((inv @ a) & 1, np.eye(n, dtype=np.uint8))
    return inv


def pack_columns(a):
    return [hex(sum(int(a[i, j]) << i for i in range(a.shape[0])))
            for j in range(a.shape[1])]


def real_matrix(m, conjugate=False, scalar=1):
    cols = []
    for j in range(len(m)):
        for b in (1, 2):
            value = FM[scalar, FM[BAR[b] if conjugate else b, m[:, j]]]
            cols.append([bit for a in value for bit in (int(a) & 1, int(a) >> 1)])
    return np.array(cols, dtype=np.uint8).T


HB = []
for i in range(8):
    a = np.zeros((8, 8), dtype=np.uint8)
    a[i, i] = 1
    HB.append(a)
for i, j in combinations(range(8), 2):
    for z in (1, 2):
        a = np.zeros((8, 8), dtype=np.uint8)
        a[i, j], a[j, i] = z, BAR[z]
        HB.append(a)
HB = np.array(HB, dtype=np.uint8)


def hcoordinates(h):
    assert np.array_equal(h, BAR[h.T])
    assert np.all(h.diagonal() < 2)
    v = list(h.diagonal())
    for i, j in combinations(range(8), 2):
        v.extend([h[i, j] & 1, h[i, j] >> 1])
    return np.array(v, dtype=np.uint8)


def haction(m, conjugate):
    hs = BAR[HB] if conjugate else HB
    left = np.bitwise_xor.reduce(FM[m[None, :, :, None], hs[:, None, :, :]], axis=2)
    out = np.bitwise_xor.reduce(
        FM[left[:, :, :, None], BAR[m.T][None, None, :, :]], axis=2)
    return np.array([hcoordinates(h) for h in out], dtype=np.uint8).T


# Direct Hermitian formula for the odd-average exterior map:
# x wedge y -> x*bar(y)^T + y*bar(x)^T.
real_basis = []
for i in range(8):
    for z in (1, 2):
        v = np.zeros(8, dtype=np.uint8)
        v[i] = z
        real_basis.append(v)
pair = np.zeros((64, 16, 16), dtype=np.uint8)
for i, x in enumerate(real_basis):
    for j, y in enumerate(real_basis):
        pair[:, i, j] = hcoordinates(
            FM[x[:, None], BAR[y][None, :]] ^ FM[y[:, None], BAR[x][None, :]])
assert not np.any(np.diagonal(pair, axis1=1, axis2=2))
assert np.array_equal(pair, pair.transpose(0, 2, 1))


def coefficient_maps(central, selected_reps):
    n = next(iter(central.values())).shape[0]
    identity = np.eye(n, dtype=np.uint8)
    # Calculate the entire dual fixed space, then put its values on the
    # author's literal quotient representatives into the identity matrix.
    equations = np.concatenate([(v ^ identity).T for v in central.values()])
    dual = nullspace(equations).T
    assert len(dual) == len(selected_reps)
    projection = (inverse(dual[:, selected_reps]) @ dual) & 1
    for v in central.values():
        assert np.array_equal((projection @ v) & 1, projection)
    norm = np.bitwise_xor.reduce(np.array(list(central.values())), axis=0)
    assert not np.any(norm @ equations.T & 1)
    return projection, norm[:, selected_reps]


def quadratic_map(action, projection, n):
    tensor = np.einsum("ak,kij->aij", projection.astype(np.int32),
                       pair.astype(np.int32)) & 1
    polar = np.zeros((len(projection), n, n), dtype=np.uint8)
    for block in range(n // 16):
        start = 16 * block
        polar[:, start:start+16, :] = (
            tensor @ action[start:start+16, :]) & 1
    assert np.array_equal(polar, polar.transpose(0, 2, 1))
    columns = np.diagonal(polar, axis1=1, axis2=2).copy()
    return columns, n * (n - 1) // 2


cases = []
b = old["blocks"][0]
cases.append({
    "character": b["character"],
    "matrices": {int(g): np.array(v, dtype=np.uint8).T[8:, 8:]
                 for g, v in b["all_second_actions"].items()},
    "oriented": span_group(b["normal_V4_states"] + b["odd_complement_generators"]),
    "multiplicity": 1})
for b in new["blocks"]:
    full = {int(g): np.array(v, dtype=np.uint8).T
            for g, v in b["all_projective_actions"].items()}
    for m in full.values():
        for j in range(4):
            assert np.array_equal(m[:8, :8], m[8*j:8*j+8, 8*j:8*j+8])
    cases.append({
        "character": b["character"],
        "matrices": {g: m[:8, :8] for g, m in full.items()},
        "oriented": span_group(b["V4_states"] + [b["C3_generator"], b["normalizing_involution"]]),
        "multiplicity": 4})

records = []
all_polar = 0
all_coordinate_blocks = []
for case_no, case in enumerate(cases):
    mats, orient = case["matrices"], set(case["oriented"])
    hstates = sorted(mats)
    reps = sorted({min(int(QT[g, h]) for h in hstates) for g in range(576)})
    loc = {int(QT[g, h]): (j, h) for j, g in enumerate(reps) for h in hstates}
    assert len(loc) == 576
    n = 16 * len(reps)
    central = {g: haction(m, g not in orient) for g, m in mats.items()}
    reference = author_cusp["cases"][case_no]
    projection, norm = coefficient_maps(central, reference["coinvariant_representatives"])
    assert pack_columns(norm) == reference["ordinary_norm_columns_on_coinvariants"]
    assert rank(norm) == reference["ordinary_norm_rank"]

    def induced(g, translation=(0, 0, 0, 0)):
        result = np.zeros((n, n), dtype=np.uint8)
        ell = np.array(case["character"], dtype=np.int16)
        for a, representative in enumerate(reps):
            b, h = loc[int(QT[g, representative])]
            phase = int(ell @ QL[QI[reps[b]]] @ np.array(translation) % 3)
            result[16*b:16*b+16, 16*a:16*a+16] = real_matrix(
                mats[h], h not in orient, (1, 2, 3)[phase])
        return result

    sm, rm, tm = induced(s), induced(r, vr), induced(tq, vt)
    ident = np.eye(n, dtype=np.uint8)
    assert np.array_equal((sm @ sm) & 1, ident)
    assert np.array_equal((rm @ rm @ rm) & 1, ident)
    assert np.array_equal((sm @ rm) & 1, tm)
    current, nm = ident.copy(), np.zeros((n, n), dtype=np.uint8)
    for k in range(36):
        if k == 18:
            assert np.array_equal(current, induced(g18, a18))
        nm ^= current
        current = (tm @ current) & 1
        if k == 11:
            assert np.array_equal(current, ident)
    assert np.array_equal(current, ident)
    assert np.array_equal((tm @ nm) & 1, nm)
    for mat, key in [(sm, "actual_source_s_columns"), (rm, "actual_source_r_columns"),
                     (tm, "actual_cusp_columns"), (nm, "actual_cusp_norm36_columns")]:
        assert pack_columns(mat) == reference[key], key
    sc, count = quadratic_map(sm, projection, n)
    tc, count2 = quadratic_map(nm, projection, n)
    all_polar += count + count2
    assert pack_columns(sc) == reference["s_correction_columns"]
    assert pack_columns(tc) == reference["cusp_correction_columns"]
    # Check genuine factoring through each norm, not merely the cyclic
    # coinvariant condition tested by multiplication with t-1.
    assert not np.any((sc @ nullspace(sm ^ ident)) & 1)
    assert not np.any((tc @ nullspace(nm)) & 1)
    joint = np.concatenate([sc, tc], axis=1)
    assert not np.any((norm @ joint) & 1)
    assert rank(joint) == len(projection) - rank(norm)
    assert [rank(sc), rank(tc), rank(joint)] == [
        reference["s_correction_rank"], reference["cusp_correction_rank"],
        reference["joint_correction_rank"]]
    selected = reference["independent_correction_source_indices"]
    assert pack_columns(joint[:, selected]) == reference["independent_correction_images"]
    assert rank(joint[:, selected]) == len(selected)
    # Exhaust the tiny coinvariant norm kernel and the displayed inverse.
    inverse_table = {}
    for word in range(1 << len(selected)):
        coefficients = np.array([(word >> i) & 1 for i in range(len(selected))],
                                dtype=np.uint8)
        image = (joint[:, selected] @ coefficients) & 1
        image_integer = sum(int(v) << i for i, v in enumerate(image))
        assert image_integer not in inverse_table
        inverse_table[image_integer] = coefficients.tolist()
    norm_kernel = []
    for word in range(1 << len(projection)):
        v = np.array([(word >> i) & 1 for i in range(len(projection))],
                     dtype=np.uint8)
        if not np.any((norm @ v) & 1):
            norm_kernel.append(word)
    assert sorted(inverse_table) == norm_kernel
    if case_no == 0:
        for a in range(2):
            for b in range(2):
                assert inverse_table[4*a + 8*b] == [a ^ b, b]

    diagnostic_records = []
    for diag in author_s["cases"][case_no]["diagnostics"]:
        matrix = induced(diag["involution"])
        assert np.array_equal((matrix @ matrix) & 1, ident)
        columns, count = quadratic_map(matrix, projection, n)
        all_polar += count
        assert pack_columns(matrix) == diag["all_involution_columns"]
        assert pack_columns(columns) == diag["all_correction_columns"]
        assert rank(columns) == diag["correction_rank"]
        diagnostic_records.append([diag["involution"], rank(columns)])

    block_records = []
    if case["multiplicity"] == 4:
        block_ref = author_blocks["cases"][case_no - 1]
        for block in block_ref["coordinate_blocks"]:
            support = block["hermitian_support"]
            complement = [j for j in range(64) if j not in support]
            for cm in central.values():
                assert not np.any(cm[np.ix_(support, complement)])
                assert not np.any(cm[np.ix_(complement, support)])
            restricted = {g: cm[np.ix_(support, support)] for g, cm in central.items()}
            local_reps = [support.index(j) for j in block["coinvariant_basis_indices"]]
            qp, nn = coefficient_maps(restricted, local_reps)
            global_qp = np.zeros((len(qp), 64), dtype=np.uint8)
            global_qp[:, support] = qp
            correction, count = quadratic_map(sm, global_qp, n)
            all_polar += count
            assert pack_columns(correction) == block["all_correction_columns"]
            actual = [len(reps)*len(support), len(qp), rank(nn), rank(correction)]
            expected = [block["global_dimension"], block["coinvariant_dimension"],
                        block["ordinary_norm_rank"], block["actual_s_correction_rank"]]
            assert actual == expected
            block_records.append(actual)
        assert sorted(v[0] for v in block_records) == [96, 96, 288, 288]
        all_coordinate_blocks.append(block_records)

    records.append({
        "character": case["character"], "multiplicity": case["multiplicity"],
        "full_real_dimension": n, "global_self_dimension": 64*len(reps),
        "coinvariant_dimension": len(projection), "norm_rank": rank(norm),
        "s_rank": rank(sc), "cusp_rank": rank(tc), "joint_rank": rank(joint),
        "literal_independent_images": pack_columns(joint[:, selected]),
        "literal_source_indices": selected, "diagnostic_involution_ranks": diagnostic_records,
        "full_coinvariant_inverse_table": inverse_table,
        "coordinate_block_dimensions_coinvariants_norm_s_ranks": block_records,
        "actual_norm_kernel_factorizations_checked": True})
    print(json.dumps(records[-1], sort_keys=True), flush=True)


# Independent word computation in the integral truncated tensor algebra.
dim = 37
zero = (np.zeros(dim, dtype=np.int64), np.zeros((dim, dim), dtype=np.int64))


def multiply(x, y):
    a, b = x
    c, d = y
    return a+c, b+d+np.outer(a, c)


def inv(x):
    a, b = x
    return -a, np.outer(a, a)-b


def products(xs):
    result = zero
    for x in xs:
        result = multiply(result, x)
    return result


def comm(x, y):
    return products([x, y, inv(x), inv(y)])


def conj(x, y):
    return products([x, y, inv(x)])


def equal(x, y):
    return all(np.array_equal(a, b) for a, b in zip(x, y))


generators = []
for i in range(dim):
    a = zero[0].copy()
    a[i] = 1
    generators.append((a, zero[1].copy()))
u, c = generators[:36], generators[36]
bword = products(u)
shifted = products(u[1:] + [conj(c, u[0])])
delta = multiply(bword, inv(shifted))
expected = multiply(comm(u[0], products(u[1:])), inv(comm(c, u[0])))
assert equal(delta, expected)
assert not np.any(delta[0])
desired = np.zeros((dim, dim), dtype=np.int64)
for j in range(1, 37):
    desired[0, j], desired[j, 0] = 1, -1
assert np.array_equal(delta[1], desired)
sdelta = multiply(products(u[:2]), inv(products(u[:2][::-1])))
assert equal(sdelta, comm(u[0], u[1]))
for rec in author_words["cases"]:
    mod = rec["commutator_exponent"]
    for word, key in [(delta, "actual_cusp_correction"), (sdelta, "actual_s_correction")]:
        upper = [int(word[1][i, j]) % mod for i, j in combinations(range(dim), 2)]
        assert upper == rec[key]["commutator"]
        assert word[0].tolist() == rec[key]["abelian"]

assert sum(v["multiplicity"] * v["global_self_dimension"] for v in records) == 6656
assert sum(v["multiplicity"] * v["coinvariant_dimension"] for v in records) == 28
assert sum(v["multiplicity"] * v["joint_rank"] for v in records) == 26
result = {
    "status": "PASS",
    "scope": "Independent dense finite-field/Hermitian maps and integral Magnus identities; no author program import or replay.",
    "manifest_sha256": digest(manifest_path),
    "proof_sha256": manifest["section_sha256"],
    "all_frozen_file_hashes_verified": True,
    "affine_cusp": {"state": tq, "translation": vt.tolist()},
    "affine_cusp18": {"state": g18, "translation": a18.tolist()},
    "source_s_and_other_involution_class_sizes": [len(source_s_class), len(other_class)],
    "source_s_and_other_involution_classes_disjoint": True,
    "cases": records,
    "full_polar_equations_checked": all_polar,
    "retained_self_dimension": 6656,
    "retained_coinvariant_dimension": 28,
    "joint_correction_dimension": 26,
    "integral_Magnus_rank": 37,
    "integral_Magnus_word_identities": 2,
    "full_signed_tensor_identity_before_reduction": True,
    "all_author_mod4_and_mod8_word_coordinates_matched": True,
    "remaining_small_character_dimension": 331776-6656,
    "remaining_small_character_coinvariants": 562-28,
}
(OUT / "check.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({"status": "PASS", "all_polar_equations": all_polar,
                  "dimension": 6656, "coinvariants": 28, "correction": 26,
                  "integral_word_identities": 2}, sort_keys=True))
