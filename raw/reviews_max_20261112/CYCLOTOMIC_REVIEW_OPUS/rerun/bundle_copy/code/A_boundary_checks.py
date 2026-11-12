"""Finite checks of the two elementary calculations used in Statement A5.
These computations verify finite instances; the profinite proof is in A5.
"""
from itertools import permutations


def compose(p, q):
    return tuple(p[q[i]] for i in range(len(p)))


def boundary_class(a, b, modulus):
    # Z/m^3 modulo its diagonal: subtract the third coordinate.
    return (a % modulus, b % modulus)


def inertia_lines(modulus):
    return ({(t, 0) for t in range(modulus)} |
            {(0, t) for t in range(modulus)} |
            {(t, t) for t in range(modulus)})


def main():
    for degree in (2, 3, 4, 5, 6):
        group = list(permutations(range(degree)))
        counts = [sum(p[i] == i for i in range(degree)) for p in group]
        assert sum(counts) == len(group)
        assert 0 in counts
        print(f"S_{degree}: order={len(group)}, sum_fixed={sum(counts)}, "
              f"derangements={counts.count(0)}")
    for modulus in (3, 5, 7, 9, 15, 25):
        lines = inertia_lines(modulus)
        exceptions = []
        for a in range(1, modulus):
            for b in range(1, modulus):
                if (boundary_class(a,b,modulus) in lines and
                    boundary_class(2*a,b,modulus) in lines):
                    exceptions.append((a,b))
        assert not exceptions
        print(f"three_cusps mod {modulus}: checked={(modulus-1)**2}, "
              f"two_product_exceptions={len(exceptions)}")
    # The order-two quotient illustrates why one finite quotient alone
    # cannot replace the torsion-free integral boundary calculation.
    lines = inertia_lines(2)
    assert boundary_class(1,1,2) in lines
    assert boundary_class(2,1,2) in lines
    print("mod 2: both products can be inertia classes; integral torsion-free proof required")


if __name__ == "__main__":
    main()
