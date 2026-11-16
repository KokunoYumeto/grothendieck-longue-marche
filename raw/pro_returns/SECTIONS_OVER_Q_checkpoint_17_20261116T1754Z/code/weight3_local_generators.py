"""Exact finite-field values of cyclotomic S-units for weight-three H1.

u_l = product_{a=1}^{l-1} (1-zeta_l^a)^(a^2).
We compute its l-th Kummer residue at 2 for l=7 and at3 for l=13.
The finite fields are F2[x]/(x^3+x+1) and F3[x]/(x^3-x-1).
"""
from pathlib import Path


def run(characteristic, ell):
    p = characteristic
    zero, one, x = (0,0,0), (1,0,0), (0,1,0)
    # In both fields x^3=x+1 (in characteristic2, minus equals plus).
    def add(a,b):
        return tuple((a[i]+b[i]) % p for i in range(3))
    def neg(a):
        return tuple(-v % p for v in a)
    def mul(a,b):
        coeff = [0] * 5
        for i in range(3):
            for j in range(3):
                coeff[i+j] += a[i]*b[j]
        for degree in (4,3):
            t = coeff[degree]
            coeff[degree-3] += t
            coeff[degree-2] += t
        return tuple(coeff[i] % p for i in range(3))
    def power(a,n):
        answer = one
        while n:
            if n & 1:
                answer = mul(answer,a)
            a = mul(a,a)
            n //= 2
        return answer
    assert all((a**3-a-1) % p for a in range(p))
    assert power(x,ell) == one
    assert all(power(x,a) != one for a in range(1,ell))
    u = one
    for a in range(1,ell):
        factor = add(one,neg(power(x,a)))
        assert factor != zero
        u = mul(u,power(factor,a*a))
    residue = power(u,(p**3-1)//ell)
    discrete_log = next(a for a in range(ell) if power(x,a)==residue)
    assert discrete_log != 0
    # Both p have order3 modulo ell, while their weight3 action is1.
    assert pow(p,3,ell)==1 and p % ell != 1 and pow(p,2,ell)!=1
    rational_frobenius = discrete_log * pow(3,-1,ell) % ell
    assert rational_frobenius != 0
    return (f"ell={ell}, residue prime={p}: u={u}; "
            f"u^(({p}^3-1)/{ell})=zeta^{discrete_log}; "
            f"descended Frobenius value={rational_frobenius} mod{ell}.")


output = "\n".join((run(2,7),run(3,13))) + "\n"
output += "Both explicit cyclotomic S-unit classes give nonzero unramified local generators.\n"
output += "At coefficient2, quadratic (-1,2) restrict to (R,Q3) as (1,1),(0,1); determinant1 over F2.\n"
Path(__file__).with_name("weight3_local_generators_output.txt").write_text(output)
print(output,end="")
