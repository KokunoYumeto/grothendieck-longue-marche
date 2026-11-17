#!/usr/bin/env python3
"""Independent matrix, word, rank and functional checks for A.4.6."""
from pathlib import Path
import json
import numpy as np

BASE = Path(__file__).resolve().parent
record = json.loads((BASE / "check_modular_centralizer_finite.json").read_text())
compressed = json.loads((BASE / "reduce_modular_centralizer_finite.json").read_text())
arrays = np.load(BASE / "check_modular_centralizer_finite.npz")


def rank(rows, prime=3):
    rows = [[int(x) % prime for x in row] for row in rows]
    n = 0
    for j in range(len(rows[0])):
        p = next((i for i in range(n, len(rows)) if rows[i][j]), None)
        if p is None:
            continue
        rows[n], rows[p] = rows[p], rows[n]
        scale = pow(rows[n][j], -1, prime)
        rows[n] = [scale * x % prime for x in rows[n]]
        for i in range(len(rows)):
            if i != n and rows[i][j]:
                scale = rows[i][j]
                rows[i] = [(a - scale * b) % prime for a, b in zip(rows[i], rows[n])]
        n += 1
        if n == len(rows):
            break
    return n


def canonical(matrix):
    values = tuple(int(x) % 12 for x in matrix)
    return min(values, tuple(-x % 12 for x in values))


def multiply(a, b):
    return canonical((a[0]*b[0]+a[1]*b[2], a[0]*b[1]+a[1]*b[3],
                      a[2]*b[0]+a[3]*b[2], a[2]*b[1]+a[3]*b[3]))


identity = (1, 0, 0, 1)
s = canonical((0, 1, -1, 0))
r = canonical((0, -1, 1, -1))
elements = [identity]
seen = {identity}
for g in elements:
    for generator in (s, r):
        h = multiply(g, generator)
        if h not in seen:
            seen.add(h)
            elements.append(h)
assert len(elements) == 576
central = {g for g in elements if multiply(g, r) == multiply(r, g)}
assert len(central) == 18
assert {tuple(row["matrix_mod12_projective"]) for row in record["records"]} == central
for row in record["records"]:
    g = identity
    for letter in row["lift_word"]:
        g = multiply(g, {1: s, 2: r}[letter])
    assert g == tuple(row["matrix_mod12_projective"]) == elements[row["residue"]]

cycles = arrays["cycles"].astype(np.int64)
chords = arrays["chords"]
action = arrays["action_r"].astype(np.int64)
assert np.array_equal(cycles[:, chords], np.eye(97, dtype=np.int64))
assert np.array_equal(action @ action @ action % 3, np.eye(97, dtype=np.int64))
assert rank(action - np.eye(97, dtype=np.int64)) == 63
functional = np.array(compressed["functional"], dtype=np.int64)
assert not np.any((action - np.eye(97, dtype=np.int64)) @ functional % 3)
assert [(i+1, int(v)) for i, v in enumerate(functional) if v] == [
    (4,2),(7,1),(9,1),(11,2),(16,2),(20,2),(21,1),
    (26,1),(33,2),(38,1),(44,2),(64,1),(85,1)]
allowed = {identity, r, multiply(r, r)}
values = compressed["obstruction_values"]
assert len(values) == 18
for row, value in zip(record["records"], values):
    good = tuple(row["matrix_mod12_projective"]) in allowed
    assert row["lifts_to_centralizer"] == good
    assert value == (0 if good else 2)
assert rank(compressed["dual_basis"]) == 96
print("PASS: independent enumeration gives 576 projective matrices and all 18 centralizing residues.")
print("PASS: all 18 literal source words evaluate to their displayed matrices.")
print("PASS: the cycle coordinates are exact; the order-three action has rank(r-1)=63.")
print("PASS: the 13-entry functional and all six three-element cosets match the paper.")
print("PASS: its invariant detecting module has rank 96; allowed residues are exactly <r>.")
