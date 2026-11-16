#!/usr/bin/env python3
"""Attempt/certificate of an individually specified A6 parameter.

Uses python-flint 0.9.0, installed in ../native.  All polynomial operations
are exact.  A completed gcd equal to one excludes every nonzero theta
point killed by n, which is stronger than the required conductor test.
"""
from functools import cache
import json
import hashlib
from pathlib import Path
import struct
import sys
import time

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "native"))
from flint import fq_default_ctx, fq_default_poly_ctx, nmod_poly, fmpz_mod_poly_ctx

start = time.monotonic()


def report(message):
    print(f"{time.monotonic()-start:.3f}s {message}", flush=True)


x = nmod_poly([0, 1], 2)


@cache
def psi(n):
    """Standard division polynomials specialized to y^2+y=x^3.

    Here a1=a2=a4=a6=0, a3=1; psi2=psi4=1.  Minus equals
    plus, and division by psi2 is trivial.  Both recurrences are exact.
    """
    if n == 0:
        return nmod_poly([], 2)
    if n in (1, 2, 4):
        return nmod_poly([1], 2)
    if n == 3:
        return x**4 + x
    m = n // 2
    if n % 2:
        return psi(m+2) * psi(m)**3 + psi(m-1) * psi(m+1)**3
    # Doubling on E is purely inseparable: x([2]P)=x(P)^4.
    return psi(m)**4


def main():
    ns = list(map(int, sys.argv[1:])) or [13, 191]
    # Explicit polynomial, with irreducibility checked by the FLINT context.
    modulus = nmod_poly([1 if i in (0, 1, 2, 5, 8, 9, 10, 14, 38)
                         else 0 for i in range(39)], 2)
    factor_unit, factors = modulus.factor()
    assert factors == [(modulus, 1)]
    fp_modulus = fmpz_mod_poly_ctx(2)([int(c) for c in modulus.coeffs()])
    F = fq_default_ctx(modulus=fp_modulus, var="t", fq_type="FQ_NMOD")
    R = fq_default_poly_ctx(F)
    t = F.gen()
    u = R.gen()
    d = t**3 + 1
    assert d != 0 and t**4 != t
    A = (u*u + t*t*u + t) / d
    B = (t*u*u + u + t*t) / d
    assert B + t*A == u
    assert B*B + t*t*B + t*t*A*A + A + t == 0
    result = {
        "field_characteristic": 2,
        "field_degree": 38,
        "irreducible_modulus_exponents": [0, 1, 2, 5, 8, 9, 10, 14, 38],
        "parameter": "t, the residue class of the indeterminate",
        "completed_tests": [],
        "scope": "No global primitive-cover conclusion until every remaining conductor is certified.",
    }
    target = Path(__file__).with_suffix(".json")
    target.write_text(json.dumps(result, indent=2) + "\n")
    def division_evaluator(argument):
        @cache
        def evaluate(n):
            if n == 0:
                return R.zero()
            if n in (1, 2, 4):
                return R.one()
            if n == 3:
                return argument**4 + argument
            m = n // 2
            if n % 2:
                return evaluate(m+2)*evaluate(m)**3 + evaluate(m-1)*evaluate(m+1)**3
            return evaluate(m)**4
        return evaluate
    evaluate_a = division_evaluator(A)
    evaluate_b = division_evaluator(B)
    for n in ns:
        report(f"starting n={n}")
        p = psi(n)
        assert p.degree() == (n*n-1)//2
        assert p.gcd(p.derivative()).degree() == 0
        report(f"division polynomial degree={p.degree()}, squarefree")
        pa = evaluate_a(n)
        if n <= 13:
            assert pa == R(p).compose(A)
        report(f"first composition degree={pa.degree()}")
        pb = evaluate_b(n)
        if n <= 13:
            assert pb == R(p).compose(B)
        report(f"second composition degree={pb.degree()}")
        g, bezout_a, bezout_b = pa.xgcd(pb)
        report(f"gcd degree={g.degree()}")
        assert bezout_a*pa + bezout_b*pb == g
        report("exact Bezout identity checked")
        row = {"n": n, "division_polynomial_degree": p.degree(),
               "first_composition_degree": pa.degree(),
               "second_composition_degree": pb.degree(),
               "gcd_degree": g.degree(),
               "gcd_is_one": g == R.one(),
               "elapsed_seconds": time.monotonic()-start}
        certificates = {}
        for name, poly in (("pa", pa), ("pb", pb),
                           ("bezout_a", bezout_a), ("bezout_b", bezout_b)):
            values = [sum(int(bit) << i for i, bit in enumerate(c.to_list()))
                      for c in poly.coeffs()]
            raw = struct.pack("<" + "Q"*len(values), *values)
            cert_path = Path(__file__).with_name(f"primitive_parameter_n{n}_{name}.bin")
            cert_path.write_bytes(raw)
            certificates[name] = {"file": cert_path.name, "degree": poly.degree(),
                                  "encoding": "ascending coefficients, uint64 little-endian; bits are powers of t",
                                  "sha256": hashlib.sha256(raw).hexdigest()}
        row["exact_polynomial_certificates"] = certificates
        result["completed_tests"].append(row)
        target.write_text(json.dumps(result, indent=2) + "\n")
        del pa, pb, g, bezout_a, bezout_b, poly
    evaluate_a.cache_clear()
    evaluate_b.cache_clear()
    report("all exact assertions completed; native memoization cleared")


if __name__ == "__main__":
    main()
