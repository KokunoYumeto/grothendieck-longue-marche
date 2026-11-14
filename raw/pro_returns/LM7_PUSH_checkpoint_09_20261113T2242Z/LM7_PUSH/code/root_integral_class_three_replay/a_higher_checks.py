#!/usr/bin/env python3
"""Integral line-exclusion certificates for A.17--A.18.

The coordinate certificates establish that the mixed O+P vector stays
outside every cusp line before and after filling Q_c. The metabelian
and good-reduction arguments themselves are proved in the paper.
"""


def line_certificates(labels):
    n = len(labels)
    vectors = {"O": [-1]*n}
    for i, name in enumerate(labels):
        vectors[name] = [int(j == i) for j in range(n)]
    w = [vectors["O"][i]+vectors["P"][i] for i in range(n)]
    print("basis:", labels)
    print("e_O+e_P:", w)
    for name, v in vectors.items():
        candidates = [(i, j, w[i]*v[j]-w[j]*v[i])
                      for i in range(n) for j in range(i+1, n)]
        certificate = next((i, j, m) for i, j, m in candidates if abs(m) == 1)
        print("cusp", name, "unit 2x2 minor (row_i,row_j,value):", certificate)
    print("All cusp lines are independent of the mixed vector over Z3 and Q3.")


def main():
    print("Original nine-cusp curve")
    line_certificates(["P", "Q", "A", "Abar", "B", "Bbar", "C", "Cbar"])
    print("Filled Q_c: eight-cusp curve")
    line_certificates(["P", "A", "Abar", "B", "Bbar", "C", "Cbar"])
    print("Nonzero scalar multiplication preserves these Q3-rank-two certificates.")
    print("PASS")


if __name__ == "__main__":
    main()
