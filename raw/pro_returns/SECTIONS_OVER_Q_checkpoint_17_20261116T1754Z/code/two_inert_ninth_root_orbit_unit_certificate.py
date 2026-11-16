#!/usr/bin/env python3
"""Fixed exact certificate for A197: a literal unit, its orbit, and rank 24.

The original 54-coordinate root remains an independent rational input.  The
compact formula is checked separately, including its actual K2 factor.
No number-field discovery routine or bounded search runs in this certificate.
"""
from pathlib import Path
from fractions import Fraction as F
from math import lcm, gcd
from functools import reduce
import json, re, sys
import sympy as S
sys.set_int_max_str_digits(0)
B = Path(__file__).resolve().parent
d = 649
rad = 3*d**6

def canonical(v, den):
    g = reduce(gcd, [den]+v)
    if den < 0: g = -g
    return [x//g for x in v], den//g

def rational(cs):
    cs = list(map(F, cs))
    den = lcm(*(x.denominator for x in cs))
    return canonical([x.numerator*(den//x.denominator) for x in cs], den)

def multiply(a, b, degree=9, constant=rad):
    av, ad = a; bv, bd = b
    c = [[0]*11 for _ in range(2*degree-1)]
    for i, x in enumerate(av):
        if x:
            for j, y in enumerate(bv):
                if y: c[i//6+j//6][i%6+j%6] += x*y
    for i in range(2*degree-1):
        for j in range(10, 5, -1):
            c[i][j-3] -= c[i][j]
            c[i][j-6] -= c[i][j]
    for i in range(2*degree-2, degree-1, -1):
        for j in range(6): c[i-degree][j] += constant*c[i][j]
    return canonical([c[i][j] for i in range(degree) for j in range(6)], ad*bd)

one = ([1]+[0]*53, 1)
def product(vs):
    out = one
    for v in vs: out = multiply(out, v)
    return out

def embed_Fprime(cs):
    out = [F(0)]*54
    for k, x in enumerate(cs):
        i, j = divmod(k, 6)
        out[18*i+j] = F(x)/d**(2*i)
    return rational(out)

raw = (B/'two_inert_ninth_root_cube13_coordinates_output.txt').read_text()
root = [F(x.strip()) for x in re.search(r'^NATURAL_ROOT (.*)$', raw, re.M)[1][1:-1].split(',')]
assert len(root) == 54
rr = rational(root)
nat = json.loads((B/'two_inert_zeta9_base_units_certificate_data.json').read_text())['natural_unit_numerators']
es = [embed_Fprime([F(x, 3) for x in row]) for row in nat]
us = [[F(x) for x in u['candidate']] for u in json.loads((B/'two_inert_relative_unit_repair_certificate_data.json').read_text())['units']]
roots = [[F(x) for x in row] for row in json.loads((B/'two_inert_level2_anti_cube_root_certificate_data.json').read_text())['roots']]
uv = []
for row in us:
    v = [F(0)]*54
    for i, x in enumerate(row): v[6*i] = x
    uv.append(rational(v))
assert product([rr,rr,rr,es[2],es[5],es[8]]) == product([es[0],es[4],es[7],uv[1],uv[3]])
print('PASS: original 54-dimensional rational cube identity, with both sides evaluated exactly.')

# c=(-1+z^3)/3 + alpha(1+z+z^4)/3
#       -alpha^2(2+2z+2z^2+z^3+z^4+z^5)/9.
c18 = list(map(F, ['-1/3','0','0','1/3','0','0',
                   '1/3','1/3','0','0','1/3','0',
                   '-2/9','-2/9','-2/9','-1/9','-1/9','-1/9']))
cc = embed_Fprime(c18)
alpha18 = [F(0)]*18; alpha18[6] = 1
u18 = [F(0)]*18; u18[0] = -2; u18[12] = 1
alpha, uu = embed_Fprime(alpha18), embed_Fprime(u18)
assert product([cc,cc,cc,alpha,es[2],es[5],es[8]]) == product([uu,es[0],es[4],es[7]])
print('PASS: the printed compact c satisfies c^3*alpha*e3*e6*e9=U*e1*e5*e8.')

# Invert c in the small field F', then identify the literal pure-field root.
csmall = rational(c18)
cols = []
for j in range(18):
    unit = ([int(i == j) for i in range(18)], 1)
    v, den = multiply(csmall, unit, 3, 3)
    cols.append([S.Rational(x, den) for x in v])
cinv = S.Matrix.hstack(*(S.Matrix(col) for col in cols)).inv()[:,0]
cinv = [F(int(x.p), int(x.q)) for x in cinv]
assert multiply(csmall, rational(cinv), 3, 3) == ([1]+[0]*17, 1)
quotient = multiply(rr, embed_Fprime(cinv))
zeta = ([int(i == 3) for i in range(54)], 1)
phase = None
for j in range(3):
    candidate = product([quotient]+[zeta]*j)
    if all(x == 0 for i, x in enumerate(candidate[0]) if i % 6):
        phase, pure = j, candidate
        break
assert phase == 2
assert product([pure,pure,pure,uu]) == product([alpha,uv[1],uv[3]])
print('PASS: zeta^%d*r/c lies literally in K2 and its cube is alpha*u2*u4/U.' % phase)
print('PASS: r and its inverse are integral by monic cubic equations over the certified global units.')

fixed_rows = [(307,78,287),(307,78,93),(307,78,53),(307,78,168),
 (307,78,274),(307,78,46),(307,98,287),(307,98,93),(307,98,53),
 (307,131,287),(307,143,287),(307,143,93),(307,143,53),(307,189,287),
 (523,20,468),(523,20,410),(523,20,217),(523,154,468),(523,154,410),
 (523,156,468),(523,156,410),(523,311,468),(523,311,410),(613,47,467)]
columns = [1,2,3,4,5,6,7,8,9,11,12,15,16,17,19,20,23,24,25,31,32,34,35,36]

def reduce_coeff(cs, p):
    return [x.numerator*pow(x.denominator,-1,p)%p for x in cs]
def evaluate(cs, x, p):
    out = 0
    for c in reversed(cs): out = (out*x+c)%p
    return out

matrix = []
residues = []
for p,t,z in fixed_rows:
    assert S.isprime(p) and (p-1)%9 == 0
    assert pow(t,9,p) == rad%p and pow(z,9,p)==1 and pow(z,3,p)!=1
    om = pow(z,3,p)
    al = pow(t,3,p)*pow(d*d,-1,p)%p
    mon = [pow(al,i,p)*pow(z,j,p)%p for i in range(3) for j in range(6)]
    vals = [sum(x*y for x,y in zip(row,mon))*pow(3,-1,p)%p for row in nat]
    ur = [reduce_coeff(row,p) for row in us]
    ar = [reduce_coeff(row,p) for row in roots]
    for j in range(3):
        tj = t*pow(z,j,p)%p
        aj = pow(tj,3,p)*pow(d*d,-1,p)%p
        w = pow(tj,5,p)*pow(d**3*(om-1),-1,p)%p
        pi = aj*aj*pow(om-1,-1,p)%p
        taupi = -om*pi%p
        v = (1+pi)*pow(1+pi*pi,-1,p)%p
        tauv = (1+taupi)*pow(1+taupi*taupi,-1,p)%p
        vals += [evaluate(row,tj,p) for row in ur]+[v*pow(tauv,-1,p)%p]+[evaluate(row,w,p) for row in ar]
    reduced_root = reduce_coeff(root,p)
    orbit = []
    for j in range(9):
        tj = t*pow(z,j,p)%p
        value = sum(reduced_root[6*i+k]*pow(tj,i,p)*pow(z,k,p) for i in range(9) for k in range(6))%p
        assert value
        orbit.append(value)
    vals += orbit
    assert len(vals)==42 and all(vals)
    powers = [1,om,om*om%p]
    row = [powers.index(pow(v,(p-1)//3,p)) for v in vals]
    matrix.append(row)
    residues.append({'p':p,'t':t,'zeta9':z,'values':vals,'row':row})
minor = S.Matrix([[row[j-1] for j in columns] for row in matrix])
det = int(minor.det())
assert det == 181379512 and det%3 == 1
def rank_mod_three(a):
    a = [row[:] for row in a]
    r = 0
    for j in range(len(a[0])):
        k = next((k for k in range(r,len(a)) if a[k][j]%3),None)
        if k is None: continue
        a[r],a[k] = a[k],a[r]
        inv = pow(a[r][j],-1,3)
        a[r] = [inv*x%3 for x in a[r]]
        for k in range(len(a)):
            if k != r:
                q = a[k][j]
                a[k] = [(x-q*y)%3 for x,y in zip(a[k],a[r])]
        r += 1
        if r == len(a): break
    return r
assert rank_mod_three([row[:33] for row in matrix]) == 21
assert rank_mod_three([row[:36] for row in matrix]) == 24
print('PASS: all 1008 literal residue values and the specified 24-by-24 determinant 181379512 = 1 mod3.')
print('PASS: the full old33-column rank is21, and the first three actual new orbit classes increase it to24.')
print('PASS: the actual g orbit supplies rank at least24; A194 gives an elementary quotient of order at most27.')

out = {'compact_c_alpha_z_coefficients':[str(x) for x in c18],
       'phase_to_unique_real_root':phase,
       'pure_root_t_coefficients':[str(F(pure[0][6*i],pure[1])) for i in range(9)],
       'cube_identity':'r^3*e3*e6*e9=e1*e5*e8*u2*u4',
       'rows':residues,'columns_1based':columns,'determinant':det,
       'old33_residue_rank':21,'old33_plus_first3_residue_rank':24,
       'rank_lower_bound':24,'quotient_dimension_upper_bound':3,
       'scope':'Exact actual unit and conjugates; the full image dimension is not determined.'}
(B/'two_inert_ninth_root_orbit_unit_certificate_data.json').write_text(json.dumps(out,indent=2)+'\n')
