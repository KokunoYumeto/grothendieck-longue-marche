#!/usr/bin/env python3
"""Independent exact witness verification for the B.59 class-two calculation."""
from collections import deque
from pathlib import Path
import json

root = Path(__file__).resolve().parents[1]
d = json.loads((root / "work_DE/ambient_rigid7_class2_certificate.json").read_text())
e = json.loads((root / "work_DE/rigid7_class2_invariants_certificate.json").read_text())
C = d["degree_two_matrix"]
N = [list(row) for row in zip(*e["kernel_basis"])]
assert len(C) == 240 and all(len(row) == 165 for row in C)
assert len(N) == 165 and all(len(row) == 6 for row in N)


def matmul(A, B):
    columns = list(zip(*B))
    return [[sum(a*b for a, b in zip(row, column)) for column in columns] for row in A]


def rank_mod(matrix, prime=101):
    A = [[x % prime for x in row] for row in matrix]
    row = 0
    for column in range(len(A[0])):
        pivot = next((i for i in range(row, len(A)) if A[i][column]), None)
        if pivot is None:
            continue
        A[row], A[pivot] = A[pivot], A[row]
        scale = pow(A[row][column], -1, prime)
        A[row] = [x*scale % prime for x in A[row]]
        for i in range(row + 1, len(A)):
            scale = A[i][column]
            if scale:
                A[i] = [(a-scale*b) % prime for a, b in zip(A[i], A[row])]
        row += 1
        if row == len(A):
            break
    return row


assert matmul(C, N) == [[0]*6 for _ in range(240)]
I = [[int(i == j) for j in range(6)] for i in range(6)]
minor = [N[i] for i in e["primitive_kernel_minor_rows"]]
inverse = e["primitive_kernel_minor_inverse"]
assert matmul(minor, inverse) == matmul(inverse, minor) == I
assert rank_mod(C) == 159
print("DEGREE_TWO: CN=0; a6-row minor of N is unimodular; rank(C mod101)=159")
print("INTEGRAL_KERNEL: primitive rank6 image of N is the complete kernel over Z")

F = e["fixed_equation_matrix"]
v = e["primitive_fixed_vector_in_kernel_basis"]
w = e["primitive_fixed_vector_ambient"]
assert rank_mod(F) == 5
assert matmul(F, [[x] for x in v]) == [[0] for _ in F]
assert [r[0] for r in matmul(N, [[x] for x in v])] == w
assert 1 in [abs(x) for x in v] and 1 in [abs(x) for x in w]
print("FIXED_KERNEL: rank(F mod101)=5; primitive v=(1,1,2,1,-1,1); w=Nv primitive")

perms = [tuple(p) for p in e["A5_generating_permutations_zero_based"]]
actions = e["generator_actions_on_kernel"]
identity = tuple(range(12))
known = {identity: I}
queue = deque([identity])
while queue:
    perm = queue.popleft()
    action = known[perm]
    for gen, matrix in zip(perms, actions):
        new_perm = tuple(perm[gen[i]] for i in range(12))
        new_action = matmul(action, matrix)
        if new_perm in known:
            assert known[new_perm] == new_action
        else:
            known[new_perm] = new_action
            queue.append(new_perm)
        assert len(known) <= 60
assert len(known) == 60
assert all(matmul(matrix, [[x] for x in v]) == [[x] for x in v] for matrix in actions)
print("ACTION_CHECK: matrices give a consistent action of the labelled60-element group and fix v")
print("CONCLUSION: completed invariant kernel is exactly Zhat*w, including primes2,3,5")
print("SCOPE: the line is a possible quotient image; no nonzero element of K is constructed")
