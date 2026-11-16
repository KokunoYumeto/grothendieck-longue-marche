"""Extract explicit central C2 refinements of the replayed D.32/D.45 bases.

The inherited obstruction solvers have already been rerun by
c_replay_obstructions.py.  This separate verifier reconstructs the relevant
degree-eight/degree-nine restricted Lie bases, constructs the rank-four
quotient graph directly from Q576, and checks invariance of the separating
characters under both actual modular generators.  It also rechecks their
values on every stored lower-centralizer defect and on the target.

The output character defines B / ker(Lambda on D_n(U)); it is an actual
central C2 extension of B/D_n(U), not a character of a chosen vector-space
approximation.  The chosen homogeneous layers are faithful Magnus models
by the restricted Hall basis theorem cited in C.12.
"""
from collections import deque
from contextlib import redirect_stdout
from functools import lru_cache
from itertools import product
import hashlib
import importlib.util
import io
import json
from pathlib import Path

import numpy as np

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[1]
REPLAY = ROOT / "work/c_obstruction_replay"


def read(name):
    return json.loads((OUT / ("c_replay_" + name + ".json")).read_text())


def parity(functional, vector):
    return (functional & vector).bit_count() % 2


def is_lyndon(word):
    return all(word < word[k:] + word[:k] for k in range(1, len(word)))


def product_polynomials(a, da, b, db, rank, little=False):
    answer = 0
    aa = a
    while aa:
        bit = aa & -aa
        i = bit.bit_length() - 1
        aa ^= bit
        bb = b
        while bb:
            bit = bb & -bb
            j = bit.bit_length() - 1
            bb ^= bit
            position = i + j * rank**da if little else i * rank**db + j
            answer ^= 1 << position
    return answer


def restricted_basis(rank, degree, little=False):
    @lru_cache(None)
    def bracket_word(word):
        if len(word) == 1:
            return 1 << word[0]
        k = next(k for k in range(1, len(word)) if is_lyndon(word[k:]))
        a, b = bracket_word(word[:k]), bracket_word(word[k:])
        return (product_polynomials(a, k, b, len(word) - k, rank, little)
                ^ product_polynomials(b, len(word) - k, a, k, rank, little))

    basis = []
    power = 1
    while degree % power == 0:
        length = degree // power
        for word in product(range(rank), repeat=length):
            if not is_lyndon(word):
                continue
            value = bracket_word(word)
            current_degree = length
            for _ in range(power.bit_length() - 1):
                value = product_polynomials(value, current_degree, value,
                                            current_degree, rank, little)
                current_degree *= 2
            basis.append(value)
        power *= 2
    # Independence of all homogeneous elements, checked on the actual tensors.
    pivots = {}
    for value in basis:
        while value:
            pivot = value.bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = value
                break
            value ^= pivots[pivot]
        assert value
    return basis


def dual_tensor_action(functional, matrix, rank, degree):
    """Return f composed with M^(tensor degree), with exact mod-two arithmetic."""
    size = rank**degree
    raw = functional.to_bytes((size + 7) // 8, "little")
    values = np.unpackbits(np.frombuffer(raw, dtype=np.uint8),
                           bitorder="little")[:size].reshape((rank,) * degree)
    for axis in range(degree):
        values = np.moveaxis(np.tensordot(matrix.T, values, axes=(1, axis)),
                             0, axis) % 2
    return int.from_bytes(np.packbits(values.reshape(-1), bitorder="little").tobytes(),
                          "little")


# Reuse only the independently constructed Q576 graph/matrix group, not the
# inherited rank-four obstruction implementation.
spec = importlib.util.spec_from_file_location("c_graph", OUT / "c_g3_frame_test.py")
graph = importlib.util.module_from_spec(spec)
with redirect_stdout(io.StringIO()):
    spec.loader.exec_module(graph)
Q = graph.qgroup
multiply = graph.multiply
identity = graph.identity
s, r = graph.s0, graph.r0
pure = [q for q in Q if tuple(z % 2 for z in q) == identity]
O = []
for q in pure:
    a, b, c, d = [z % 3 for z in q]
    square = ((a*a+b*c) % 3, (a*b+b*d) % 3,
              (c*a+d*c) % 3, (c*b+d*d) % 3)
    if square in ((1, 0, 0, 1), (2, 0, 0, 2)):
        O.append(q)
assert len(O) == 32
q0 = {q: min(multiply(q, o) for o in O) for q in Q}
Q0 = sorted(set(q0.values()))
assert len(Q0) == 18
mul0 = lambda a, b: q0[multiply(a, b)]
e0, s0, r0 = q0[identity], q0[s], q0[r]
r20 = mul0(r0, r0)
index = {q: j for j, q in enumerate(Q0)}
v2 = {q: (0, min(q, mul0(q, s0))) for q in Q0}
v3 = {q: (1, min(q, mul0(q, r0), mul0(q, r20))) for q in Q0}
adj = {v: [] for v in set(v2.values()) | set(v3.values())}
for q in Q0:
    adj[v2[q]].append((v3[q], q))
    adj[v3[q]].append((v2[q], q))
seen = {v2[e0]}
queue = deque(seen)
tree = set()
while queue:
    v = queue.popleft()
    for w, edge in adj[v]:
        if w not in seen:
            seen.add(w)
            tree.add(edge)
            queue.append(w)
chords = {q: j for j, q in enumerate(q for q in Q0 if q not in tree)}
assert len(chords) == 4


def abelianize(word):
    q = e0
    value = np.zeros(4, dtype=np.uint8)
    for letter in word:
        if letter == 0:
            q = mul0(q, s0)
        else:
            nxt = mul0(q, r0 if letter == 1 else r20)
            for edge in (q, nxt):
                if edge in chords:
                    value[chords[edge]] ^= 1
            q = nxt
    assert q == e0
    return value


Kwords = json.loads((REPLAY / "d_cm_rank4_refine.json").read_text())["K_basis_words"]
assert np.array_equal(np.array([abelianize(w) for w in Kwords]), np.eye(4, dtype=np.uint8))
Ms = np.array([abelianize([0] + w + [0]) for w in Kwords], dtype=np.uint8).T
Mr = np.array([abelianize([1] + w + [2]) for w in Kwords], dtype=np.uint8).T
assert np.array_equal(Ms @ Ms % 2, np.eye(4, dtype=np.uint8))
assert np.array_equal(Mr @ Mr @ Mr % 2, np.eye(4, dtype=np.uint8))

rank4 = read("d_cm_degree8_centralizer")
seed4 = read("d_cm_degree8_seed")
f4 = int(rank4["separating_functional"], 16)
basis4 = restricted_basis(4, 8)
assert len(basis4) == 8230
for matrix in (Ms, Mr):
    difference = f4 ^ dual_tensor_action(f4, matrix, 4, 8)
    assert all(parity(difference, value) == 0 for value in basis4)
target4 = int(seed4["degree8_target"], 16)
assert parity(f4, target4) == 1
assert parity(f4, int(seed4["t48_degree8_column"], 16)) == 0
assert all(parity(f4, int(v, 16)) == 0 for v in rank4["full_degree8_defects"])
assert len(rank4["full_degree8_defects"]) == 1666

rank2 = read("d_cm_rank2_centralizers")
central2 = read("d_cm_rank2_degree9")
f2 = int(rank2["certificates"][0]["annihilating_functional"], 16)
basis2 = restricted_basis(2, 9, little=True)
assert basis2 == [int(v, 16) for v in central2["Lie_basis_polynomials"]]
assert len(basis2) == 56
c2 = central2["certificates"][0]
for columns in (c2["s_H1_columns"], c2["r_H1_columns"]):
    matrix = np.array([[(columns[j] >> i) & 1 for j in range(2)]
                       for i in range(2)], dtype=np.uint8)
    difference = f2 ^ dual_tensor_action(f2, matrix, 2, 9)
    assert all(parity(difference, value) == 0 for value in basis2)
assert parity(f2, int(c2["target"], 16)) == 1
assert all(parity(f2, int(v, 16)) == 0 for v in c2["correction_columns"])
assert all(parity(f2, int(v, 16)) == 0
           for v in rank2["certificates"][0]["centralizer_degree9_defects"])
positions = [j for j in range(512) if f2 >> j & 1]
assert positions == [432, 464, 484, 488]

records = []
for name, rank, degree, functional, dimension, lower_count in (
        ("D32", 4, 8, f4, 8230, 1666), ("D45", 2, 9, f2, 56, 38)):
    hex_text = hex(functional) + "\n"
    path = OUT / ("c_" + name.lower() + "_central_character.hex")
    path.write_text(hex_text)
    records.append({
        "record": name, "free_rank": rank, "homogeneous_degree": degree,
        "kernel_dimension_before_central_pushout": dimension,
        "central_kernel_after_pushout": "C2",
        "functional_support": functional.bit_count(),
        "functional_file": path.name,
        "functional_file_sha256": hashlib.sha256(hex_text.encode()).hexdigest(),
        "s_invariant_on_entire_restricted_layer": True,
        "r_invariant_on_entire_restricted_layer": True,
        "complete_lower_centralizer_generators_annihilated": lower_count,
        "recorded_target_value": 1,
        "definition": "B / {w in D_n(U) : Lambda(Magnus_n(w)) = 0}",
    })
summary = {"records": records,
           "D45_four_tensor_positions_little_endian": positions,
           "D32_s_H1_matrix": Ms.tolist(), "D32_r_H1_matrix": Mr.tolist(),
           "scope": "Explicit central C2 refinements of the exact recorded bases. The preceding full replay certifies completeness of lower changes; this verifier independently proves the character is invariant under the whole modular group."}
(OUT / "c_central_refinements.json").write_text(json.dumps(summary, indent=2) + "\n")
print(json.dumps(summary, indent=2))
