#!/usr/bin/env python3
"""Exact second cube root and a complete pro-three unit detector for M.

Discovery PARI output supplies rational coefficients only.  Every field
identity and finite residue computation below is independent of PARI.
"""
from pathlib import Path
from fractions import Fraction as F
import json, re, runpy, sys
import sympy as S
sys.set_int_max_str_digits(0)
B = Path(__file__).resolve().parent
v = runpy.run_path(str(B/'two_inert_ninth_root_orbit_unit_certificate.py'))
rational, multiply, product = v['rational'], v['multiply'], v['product']
es, uv, roots, one = v['es'], v['uv'], v['roots'], v['one']
canonical = v['canonical']
d, rad = v['d'], v['rad']

def automorphism(a, k):
    av, den = a
    out = [0]*54
    for h, x in enumerate(av):
        i,j = divmod(h,6)
        e = (j+k*i)%9
        if e < 6: out[6*i+e] += x
        else:
            out[6*i+e-3] -= x
            out[6*i+e-6] -= x
    return canonical(out,den)

# The actual E2 coordinate is w=t^5/(d^3*(zeta-1)).
wc = [F(0)]*54
wc[30] = F(-2,3*d**3); wc[33] = F(-1,3*d**3)
w = rational(wc)
def evaluate_rational(cs, x):
    ans = ([0]*54,1)
    for c in reversed(cs):
        ans = multiply(ans,x)
        a,den = ans
        c = F(c)
        a = [q*c.denominator for q in a]
        a[0] += c.numerator*den
        ans = canonical(a,den*c.denominator)
    return ans
anti = [evaluate_rational(cs,w) for cs in roots]
raw = (B/'two_inert_ninth_root_cube27_coordinates_output.txt').read_text()
sr = [F(x.strip()) for x in re.search(r'^NATURAL_ROOT (.*)$',raw,re.M)[1][1:-1].split(',')]
assert len(sr)==54
ss = rational(sr)
# Read the paper's literal decimal blocks independently of the discovery file.
table=(B.parent/'sections/two_inert_ninth_root_second_unit_coefficients.tex').read_text()
blocks={}
for match in re.finditer(r'^(\d+)&([+-])&(\d+)&\\texttt\{(\d+)\}&\\texttt\{(\d*)\}\\\\$',table,re.M):
    h,sign,pos,a,b=match.groups()
    h,pos=int(h),int(pos)
    blocks.setdefault(h,[]).append((pos,sign,a,b))
assert set(blocks)==set(range(54))
printed=[]
for h in range(54):
    pieces=[]
    rows=sorted(blocks[h])
    for j,(pos,sign,a,b) in enumerate(rows):
        assert pos==2*j+1 and sign==rows[0][1]
        if pieces: assert len(a)==40
        if b: assert len(b)==40
        pieces.extend([a]+([b] if b else []))
    integer=int(''.join(pieces))*(-1 if rows[0][1]=='-' else 1)
    printed.append(F(integer,1036253459504241))
assert printed==sr
print('PASS: all54 literal printed coefficients reconstructed from the810 two-block table rows.')
# s^3 = e1 e2 e4 e8 r2 r4 g^2(u2) /
#                (e3 e5 u3 g(u3 r2 r4)).
denominator = [es[2],es[4],uv[2],automorphism(uv[2],1),
               automorphism(anti[0],1),automorphism(anti[2],1)]
numerator = [es[0],es[1],es[3],es[7],anti[0],anti[2],automorphism(uv[1],2)]
assert product([ss,ss,ss]+denominator)==product(numerator)
for j in range(9):
    assert automorphism(product([ss,ss,ss]),j)==product([automorphism(ss,j)]*3)
assert automorphism(ss,9)==ss
print('PASS: second exact 54-dimensional cube identity, all nine literal automorphisms, and g^9=1.')
print('PASS: the second root and its inverse are integral by their monic equations over certified units.')

fixed_rows = [(307,78,287),(307,78,93),(307,78,53),(307,78,168),
 (307,78,274),(307,78,46),(307,98,287),(307,98,93),(307,98,53),
 (307,98,168),(307,131,287),(307,131,93),(307,143,287),(307,143,93),
 (307,143,53),(307,189,287),(307,193,287),(523,20,468),(523,20,410),
 (523,20,217),(523,154,468),(523,154,410),(523,156,468),(523,156,410),
 (523,311,468),(523,311,410),(613,47,467)]
columns = [1,2,3,4,5,6,7,8,9,11,12,15,16,17,19,20,23,24,25,
           31,32,34,35,36,43,44,45]

def finite_value(a,p,t,z):
    av,den = a
    assert den%p
    return sum(x*pow(t,i,p)*pow(z,j,p) for i in range(9) for j in range(6)
               if (x:=av[6*i+j]))*pow(den,-1,p)%p

def base_units():
    result = es[:]
    # epsilon=(1+pi)/(1+pi^2) divided by its tau conjugate.
    # Reuse the separately checked A197 literal finite formula below.
    return result

matrix=[]; allvalues=[]
for p,t,z in fixed_rows:
    assert S.isprime(p) and pow(t,9,p)==rad%p and pow(z,9,p)==1 and pow(z,3,p)!=1
    om=pow(z,3,p)
    vals=[finite_value(e,p,t,z) for e in es]
    for j in range(3):
        tj=t*pow(z,j,p)%p
        aj=pow(tj,3,p)*pow(d*d,-1,p)%p
        pi=aj*aj*pow(om-1,-1,p)%p; taupi=-om*pi%p
        ev=(1+pi)*pow(1+pi*pi,-1,p)%p
        tv=(1+taupi)*pow(1+taupi*taupi,-1,p)%p
        vals += [finite_value(u,p,tj,z) for u in uv]
        vals += [ev*pow(tv,-1,p)%p]
        vals += [finite_value(a,p,tj,z) for a in anti]
    vals += [finite_value(v['rr'],p,t*pow(z,j,p)%p,z) for j in range(9)]
    vals += [finite_value(ss,p,t*pow(z,j,p)%p,z) for j in range(9)]
    assert len(vals)==51 and all(vals)
    for j in range(9):
        tj=t*pow(z,j,p)%p
        den=1;num=1
        for a in denominator:den=den*finite_value(a,p,tj,z)%p
        for a in numerator:num=num*finite_value(a,p,tj,z)%p
        assert pow(vals[42+j],3,p)*den%p==num
    logs={1:0,om:1,om*om%p:2}
    row=[logs[pow(a,(p-1)//3,p)] for a in vals]
    matrix.append(row);allvalues.append({'p':p,'t':t,'zeta9':z,'values':vals,'row':row})
minor=S.Matrix([[row[j-1]for j in columns]for row in matrix])
det=int(minor.det())
assert det == -16257696500 and det%3==1
rank=v['rank_mod_three']
assert rank([row[:33]for row in matrix])==21
assert rank([row[:42]for row in matrix])==24
assert rank(matrix)==27
print('PASS: all1377 fixed residue values; specified27-by-27 determinant -16257696500 = 1 mod3.')
print('PASS: full detector ranks old33=21, old33+first orbit=24, all51=27.')
print('PASS: compact Nakayama yields the full pro-three unit group; the subfield-unit quotient is exactly C3^6.')

data={'second_root_t_z_coefficients':[str(x)for x in sr],
      'second_cube_identity':'s^3 e3 e5 u3 g(u3 r2 r4)=e1 e2 e4 e8 r2 r4 g^2(u2)',
      'generator_order':'A194 old33; g^j(r),j0..8; g^j(s),j0..8',
      'rows':allvalues,'columns_1based':columns,'determinant':det,
      'full_detector_rank':27,'old33_rank':21,'first_orbit_rank':24,
      'subfield_quotient_dimension':6,'first_orbit_quotient_dimension':3,
      'scope':'Full pro-three unit completion; no ordinary fundamental-unit index is asserted.'}
(B/'two_inert_ninth_root_full_units_certificate_data.json').write_text(json.dumps(data,indent=2)+'\n')
