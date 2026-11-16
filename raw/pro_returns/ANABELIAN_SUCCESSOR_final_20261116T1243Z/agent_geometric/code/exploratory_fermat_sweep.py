"""Reproduce the exploratory odd-n Cartier sweep; it asserts no universal result."""
from math import gcd
import csv
import sys

out = csv.writer(sys.stdout)
out.writerow(["n", "base_genus", "cover_genus", "cover_two_rank", "primitive_two_rank"])
for n in range(5, 102, 2):
    basis = {(a, b) for a in range(1, n) for b in range(1, n - a)}
    inv = (n + 1) // 2
    operator = {
        v: None if v[0] % 2 and v[1] % 2
        else ((inv * v[0]) % n, (inv * v[1]) % n)
        for v in basis
    }
    image = basis
    while True:
        next_image = {operator[v] for v in image if operator[v] is not None}
        if next_image == image:
            break
        image = next_image
    primitive = sum(gcd((b - a) % n, n) == 1 for a, b in image)
    out.writerow([n, (n - 1) // 2, len(basis), len(image), primitive])
