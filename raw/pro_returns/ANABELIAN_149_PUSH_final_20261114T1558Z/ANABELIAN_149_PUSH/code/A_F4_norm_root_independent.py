#!/usr/bin/env python3
"""Independently verify the fixed F4 moduli witnesses using SymPy GF(2) rings.

No scan, binary-mask field engine, jet solver, or author verifier is imported.
We check the complete norm identity as a multivariate polynomial modulo the
two defining field polynomials, and verify their irreducibility separately.
"""
from pathlib import Path
import hashlib
import json
import math
import time
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'code/A_theta_F4_moduli_witnesses.json'
x, T, w = sp.symbols('x T w')

def binary(n):
    return sp.Add(*(w**j for j in range(n.bit_length()) if (n >> j) & 1))

def subgroup(n):
    found = {1}
    todo = [1]
    while todo:
        a = todo.pop()
        for b in (2*a % n, -a % n):
            if b not in found:
                found.add(b)
                todo.append(b)
    return found

def verify(record):
    e = record['coefficient_field_degree']
    modulus = binary(record['coefficient_field_binary_modulus'])
    assert sp.Poly(modulus, w, modulus=2).is_irreducible
    base = sp.groebner([modulus], T, w, modulus=2)
    q = sum(binary(c)*T**j for j,c in enumerate(record['coordinate_minimal_polynomial']))
    degree = record['coordinate_field_extension_degree']
    assert sp.degree(q,T) == degree and 1 <= degree <= 3
    if degree > 1:
        # A quadratic or cubic over a field is irreducible iff it has no root.
        assert all(base.reduce(q.subs(T,binary(c)))[1] != 0 for c in range(1 << e))
    basis = sp.groebner([q, modulus], T, w, x, modulus=2)
    def decoded(n):
        assert 0 <= n < (1 << (e*degree))
        mask = (1 << e)-1
        return sum(binary((n >> (j*e)) & mask)*T**j for j in range(degree))
    def reduced(expr):
        return basis.reduce(sp.Poly(expr,T,w,x,modulus=2).as_expr())[1]
    def poly(expr):
        return sp.Poly(expr,T,w,x,modulus=2)
    a,b,c = [decoded(n) for n in record['curve_coefficients']]
    t = decoded(record['coordinate_t'])
    delta = decoded(record['beta_relation_constant'])
    A = poly(sum(decoded(v)*x**j for j,v in enumerate(record['A_coefficients'])))
    B = poly(sum(decoded(v)*x**j for j,v in enumerate(record['B_coefficients'])))
    n = record['n']
    d = (n-3)//2
    assert A.degree(x) <= d and B.degree(x) == d
    assert reduced(B.as_expr().coeff(x,d)-1) == 0
    u = poly(x*x+x)
    F = poly(a*x**3+a*x**2+(b+c)*x+b)
    norm = u*(A*A+A*B) + B*B*(F+poly(delta)*u)
    target = poly(a)*poly(x+t)**n
    assert reduced((norm-target).as_expr()) == 0
    assert reduced(t*(t+1)) != 0
    assert reduced((F-poly(delta)*u).as_expr().subs(x,t)) == 0
    assert reduced(A.as_expr().subs(x,t)) == 0
    values = {}
    for name,point in [('t',t),('0',0),('1',1)]:
        value = reduced(B.as_expr().subs(x,point))
        assert value != 0
        assert reduced(value-decoded(record['B_at_'+name])) == 0
        values[name] = str(value)
    assert subgroup(n) == {j for j in range(1,n) if math.gcd(j,n)==1}
    # Recover the F4 key directly from symmetric functions in the base field.
    alpha_choices = [j for j in range(1 << e) if base.reduce(binary(j)**2+binary(j)+1)[1] == 0]
    assert len(alpha_choices) == 2
    alpha = {2:2,4:6,6:58}[e]
    assert alpha in alpha_choices
    def symbol_of(value):
        choices = [0,1,binary(alpha),binary(alpha)+1]
        matches = [str(i) for i,v in enumerate(choices) if reduced(value-v)==0]
        assert len(matches)==1
        return matches[0]
    key = ''.join(symbol_of(z) for z in (a+b+c,a*b+a*c+b*c,a*b*c))
    assert key == record['moduli_key']
    return {'moduli_key':key,'annihilator':n,'coordinate_degree':degree,
            'coefficient_field_irreducible':True,'coordinate_field_irreducible':True,
            'full_norm_identity':True,'local_values_checked':True,
            'unit_group_generated_by_two_and_minus_one':True}

def main():
    start=time.time()
    raw=SOURCE.read_bytes()
    data=json.loads(raw)
    rows=[]
    for record in data['witnesses']:
        rows.append(verify(record))
    keys={r['moduli_key'] for r in rows}
    allkeys={f'{a}{b}{c}' for a in range(4) for b in range(4) for c in range(1,4)}
    assert len(rows)==len(keys)==46 and allkeys-keys=={'203','302'}
    result={'status':'PASS','method':'SymPy multivariate GF(2) quotient-ring reduction',
            'source_sha256':hashlib.sha256(raw).hexdigest(),'verified_count':len(rows),
            'remaining_keys':sorted(allkeys-keys),'records':rows,
            'runtime_seconds':time.time()-start}
    output=ROOT/'code/A_F4_norm_root_independent.json'
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='records'},indent=2))

if __name__=='__main__':
    main()
