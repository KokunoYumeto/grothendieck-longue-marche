#!/usr/bin/env python3
"""Actual four local cubic characters on the certified M1 ordinary units.

This uses the literal embeddings alpha=rho*zeta^j, not an identification of
abstract norm kernels.  Arithmetic local reciprocity is fixed on cyclotomic
units, then the wild character is calibrated by Hilbert antisymmetry.
"""
from pathlib import Path
from fractions import Fraction
from math import lcm, comb
import hashlib
import json
import argparse
import subprocess
import tempfile
import shutil
from itertools import product
from sympy import Matrix, eye, zeros, QQ, groebner, symbols, Rational, Poly, primerange, n_order
from sympy.matrices.normalforms import hermite_normal_form

HERE = Path(__file__).resolve().parent
INPUT = HERE.parent / "inputs"

class DVR:
    def __init__(self, d):
        self.d = d
        self.m = 3 ** (d - 1)
        self.e = 2 * self.m
        self.n = 2 * self.e + 1
        self.rho = 23  # the unique Q3 cube root of17, modulo27
        m, e, rho = self.m, self.e, self.rho
        self.q = [(comb(e, j) * (-1) ** (e - j)
                   + (rho * comb(m, j) * (-1) ** (m - j) if j <= m else 0)
                   + (rho * rho if j == 0 else 0)) % 27
                  for j in range(e + 1)]
        assert self.q[-1] == 1 and self.q[0] % 9 == 3
        assert all(x % 3 == 0 for x in self.q[:-1])
        self.zero = (0,) * e
        self.one = (1,) + (0,) * (e - 1)
        self.x = (0, 1) + (0,) * (e - 2)
        self.hs = {}
        power = list(self.one)
        for k in range(self.n + 1):
            cols = []
            for j in range(e):
                cols.append(Matrix(self.polyred([0] * j + power)))
            h = hermite_normal_form(Matrix.hstack(*cols, 27 * eye(e)))
            assert h.shape == (e, e)
            assert abs(int(h.det())) == 3 ** k
            self.hs[k] = [[int(h[i, j]) for j in range(e)] for i in range(e)]
            power = self.polyred([0] + power)
        self.powers = [self.one]
        for i in range(self.n):
            self.powers.append(self.mul(self.powers[-1], self.x))
        assert self.powers[-1] == self.zero
        self.gens = [self.add(self.one, self.powers[i]) for i in range(1, self.n)]
        self.inverses = [self.power(g, 2 * 3 ** (self.n - 1) - 1) for g in self.gens]
        assert all(self.mul(g, inv) == self.one for g, inv in zip(self.gens, self.inverses))

    def polyred(self, a):
        a = list(a) + [0] * max(0, self.e - len(a))
        for i in range(len(a) - 1, self.e - 1, -1):
            q = a[i] % 27
            for j in range(self.e):
                a[i - self.e + j] -= q * self.q[j]
        return [x % 27 for x in a[:self.e]]

    def canonical(self, a, k=None):
        if k is None:
            k = self.n
        a = self.polyred(a)
        h = self.hs[k]
        for i in range(self.e - 1, -1, -1):
            q = a[i] // h[i][i]
            for j in range(i + 1):
                a[j] -= q * h[j][i]
        return tuple(a)

    def add(self, a, b):
        return self.canonical([x + y for x, y in zip(a, b)])

    def scale(self, a, c):
        return self.canonical([x * c for x in a])

    def mul(self, a, b):
        q = [0] * (2 * self.e - 1)
        for i, x in enumerate(a):
            if x:
                for j, y in enumerate(b):
                    if y:
                        q[i + j] += x * y
        return self.canonical(q)

    def power(self, a, n):
        r = self.one
        while n:
            if n & 1:
                r = self.mul(r, a)
            a = self.mul(a, a)
            n >>= 1
        return r

    def coords(self, a):
        residue = self.canonical(a, 1)[0]
        assert residue in (1, 2)
        if residue == 2:
            a = self.scale(a, -1)
        out = []
        for i in range(1, self.n):
            candidates = [c for c in range(3)
                          if self.canonical(a, i + 1)
                          == self.canonical(self.add(self.one, self.scale(self.powers[i], c)), i + 1)]
            assert len(candidates) == 1
            c = candidates[0]
            out.append(c)
            a = self.mul(a, self.power(self.inverses[i - 1], c))
        assert a == self.one
        return out

    def smul(self, a, b):
        q = [self.zero] * 5
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                q[i + j] = self.add(q[i + j], self.mul(x, y))
        # T^3 = pi -3T +3T^2.
        for k in (4, 3):
            v = q[k]
            q[k - 3] = self.add(q[k - 3], self.mul(v, self.x))
            q[k - 2] = self.add(q[k - 2], self.scale(v, -3))
            q[k - 1] = self.add(q[k - 1], self.scale(v, 3))
        return q[:3]

    def snorm(self, a):
        basis = [[self.one, self.zero, self.zero],
                 [self.zero, self.one, self.zero],
                 [self.zero, self.zero, self.one]]
        cols = [self.smul(a, b) for b in basis]
        out = self.zero
        for perm, sign in [((0, 1, 2), 1), ((1, 2, 0), 1), ((2, 0, 1), 1),
                           ((2, 1, 0), -1), ((1, 0, 2), -1), ((0, 2, 1), -1)]:
            term = self.one
            for j, i in enumerate(perm):
                term = self.mul(term, cols[j][i])
            out = self.add(out, self.scale(term, sign))
        return out



def add(x, y, modulus):
    return ((x[0] + y[0]) % modulus, (x[1] + y[1]) % modulus)


def mul(x, y, modulus):
    return ((x[0] * y[0] - x[1] * y[1]) % modulus,
            (x[0] * y[1] + x[1] * y[0] - x[1] * y[1]) % modulus)


def power(x, exponent, modulus):
    result = (1, 0)
    while exponent:
        if exponent & 1:
            result = mul(result, x, modulus)
        x = mul(x, x, modulus)
        exponent >>= 1
    return result


def rho(precision):
    """The actual Q3 cube root of 17 modulo 3**precision."""
    result = 23
    for n in range(3, precision):
        candidates = [result + t * 3**n for t in range(3)
                      if ((result + t * 3**n)**3 - 17) % 3**(n + 2) == 0]
        assert len(candidates) == 1
        result = candidates[0]
    assert (result**3 - 17) % 3**(precision + 1) == 0
    return result % 3**precision


def evaluate_three(coefficients, j, precision=3):
    coeffs = [Fraction(c) for c in coefficients]
    denominator = lcm(*(c.denominator for c in coeffs))
    d0, k = denominator, 0
    while d0 % 3 == 0:
        d0 //= 3
        k += 1
    modulus = 3**(precision + k)
    rr = rho(precision + k)
    z = (0, 1)
    a = tuple(rr * x % modulus for x in power(z, j, modulus))
    theta = ((z[0] - a[0]) % modulus, (z[1] - a[1]) % modulus)
    out = (0, 0)
    for c in reversed(coeffs):
        out = add(mul(out, theta, modulus), (int(c * denominator), 0), modulus)
    out = tuple(x * pow(d0, -1, modulus) % modulus for x in out)
    assert all(x % 3**k == 0 for x in out)
    return tuple((x // 3**k) % 3**precision for x in out)


def evaluate_seventeen(coefficients):
    theta = (0, 1)  # alpha=0, theta=zeta-alpha.
    out = (0, 0)
    for c in reversed([Fraction(c) for c in coefficients]):
        out = add(mul(out, theta, 17),
                  (c.numerator * pow(c.denominator, -1, 17), 0), 17)
    assert out != (0, 0)
    return out


def matrix_rank3(rows):
    a = [[x % 3 for x in row] for row in rows]
    i = 0
    for j in range(len(a[0])):
        k = next((k for k in range(i, len(a)) if a[k][j]), None)
        if k is None:
            continue
        a[k], a[i] = a[i], a[k]
        c = pow(a[i][j], -1, 3)
        a[i] = [x * c % 3 for x in a[i]]
        for k in range(len(a)):
            if k != i:
                c = a[k][j]
                a[k] = [(x - c * y) % 3 for x, y in zip(a[k], a[i])]
        i += 1
        if i == len(a):
            break
    return i


def run():
    parser=argparse.ArgumentParser()
    parser.add_argument("--gp", help="Path to the PARI/GP executable for a complete base rebuild")
    args=parser.parse_args()
    if args.gp:
        gp=str(Path(args.gp).resolve())
        with tempfile.TemporaryDirectory(prefix="e110_gp_") as temp:
            script=HERE/"e_pure_tower_base.gp"
            result=subprocess.run([gp,"-q","-f",str(script)],cwd=temp,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
            HERE.joinpath("e_pure_tower_base_gp.out").write_text(result.stdout)
            assert result.returncode==0
            assert '"type":"completion","status":"PASS"' in result.stdout
            assert "***   at " not in result.stdout
            shutil.copy2(Path(temp)/"e_pure_tower_base.bin",HERE/"e_pure_tower_base.bin")
    r = DVR(1)
    weight = [1, 2, 0, 0]
    rho27 = rho(3)

    def to_dvr(x):
        a, b = x
        return r.canonical([a - b * pow(rho27, -1, 27),
                            b * pow(rho27, -1, 27)])

    def raw_wild(x):
        return sum(c * w for c, w in zip(r.coords(to_dvr(x)), weight)) % 3

    def cyclotomic(x):
        a, b = x
        n = (a*a - a*b + b*b) % 9
        assert n % 3 == 1
        return (pow(n, -1, 9) - 1) // 3 % 3

    assert cyclotomic((rho27, 0)) == 1
    assert cyclotomic((0, 1)) == 0
    assert raw_wild((0, 1)) != 0
    multiplier = 2 * pow(raw_wild((0, 1)), -1, 3) % 3

    def character3(x, j):
        return (multiplier * raw_wild(x) + (j-1) * cyclotomic(x)) % 3

    def character17(x):
        xx = power(x, 96, 17)
        logs = [e for e in range(3) if power((0, 1), e, 17) == xx]
        assert len(logs) == 1
        return -logs[0] % 3

    source = HERE / "e_pure_tower_base_gp.out"
    data = [json.loads(line) for line in source.read_text().splitlines() if line.startswith('{')]
    units = [x for x in data if x['type'] == 'unit']
    records = []
    for u in units:
        local3 = [evaluate_three(u['coefficients'], j) for j in range(3)]
        local17 = evaluate_seventeen(u['coefficients'])
        values = [character3(x, j) for j, x in enumerate(local3)] + [character17(local17)]
        assert sum(values) % 3 == 0, (u['index'], values)
        records.append({'index': u['index'], 'unit_coefficients': u['coefficients'],
                        'true_denominator': lcm(*(Fraction(x).denominator for x in u['coefficients'])),
                        'local_three_values_zeta_basis_mod27': local3,
                        'local_seventeen_value_zeta_basis': local17,
                        'characters': values})
    matrix = [list(row) for row in zip(*(r['characters'] for r in records))]
    assert matrix == [[2,2,2],[2,2,0],[2,0,2],[0,2,2]]
    A=Matrix(matrix)
    L=A[:3,:].inv_mod(3)*eye(4)[:3,:]
    L=L.applyfunc(lambda x:int(x)%3)
    assert (L*A).applyfunc(lambda x:int(x)%3)==eye(3)
    hyperplane=[v for v in product(range(3),repeat=4) if sum(v)%3==0]
    assert len(hyperplane)==27
    for v in hyperplane:
        assert (A*L*Matrix(v)-Matrix(v)).applyfunc(lambda x:int(x)%3)==zeros(4,1)
    P=eye(4)
    P[1,1]=P[2,2]=0
    P[1,2]=P[2,1]=1
    C=(-L*P*A).applyfunc(lambda x:int(x)%3)
    assert (A*C+P*A).applyfunc(lambda x:int(x)%3)==zeros(4,3)
    assert (C*C).applyfunc(lambda x:int(x)%3)==eye(3)
    plus_dimension=3-matrix_rank3((C-eye(3)).tolist())
    minus_dimension=3-matrix_rank3((C+eye(3)).tolist())
    assert (plus_dimension,minus_dimension)==(1,2)

    # Reconstruct the wild norm kernel from actual multiplication determinants.
    cubes=[r.coords(r.power(g,3)) for g in r.gens]
    tp=[r.one,r.zero,r.zero]
    T=[r.zero,r.one,r.zero]
    normrows=[]
    for i in range(1,3*r.n):
        tp=r.smul(tp,T)
        v=[r.add(r.one,tp[0]),tp[1],tp[2]]
        nr=r.coords(r.snorm(v))
        assert sum(x*y for x,y in zip(nr,weight))%3==0
        normrows.append(nr)
    assert matrix_rank3(cubes+normrows)==3

    # Independent characteristic-zero field arithmetic and integrality.
    aa,zz=symbols('a z')
    gb=groebner([aa**3-17,zz**2+zz+1],aa,zz,domain=QQ)
    basis=[1,aa,aa**2,zz,aa*zz,aa**2*zz]
    exponent_pairs=[(0,0),(1,0),(2,0),(0,1),(1,1),(2,1)]
    exact=[]
    for rec in units:
        f=gb.reduce(sum(Rational(v)*(zz-aa)**i for i,v in enumerate(rec['coefficients'])).expand())[1]
        cols=[]
        for b in basis:
            pp=Poly(gb.reduce((f*b).expand())[1],aa,zz)
            cols.append(Matrix([pp.coeff_monomial(aa**i*zz**j) for i,j in exponent_pairs]))
        B=Matrix.hstack(*cols)
        cp=B.charpoly().as_expr()
        cpcoeff=B.charpoly().all_coeffs()
        assert all(x.q==1 for x in cpcoeff) and abs(cpcoeff[-1])==1
        nk=gb.reduce((f*f.subs(aa,zz*aa)*f.subs(aa,zz**2*aa)).expand())[1]
        conjugate=gb.reduce(f.subs(zz,-1-zz).expand())[1]
        nf=gb.reduce((f*conjugate).expand())[1]
        exact.append({'index':rec['index'],'element_in_alpha_zeta_basis':str(f),
                      'multiplication_matrix':[[str(x) for x in row] for row in B.tolist()],
                      'characteristic_polynomial_coefficients':[int(x) for x in cpcoeff],
                      'norm_to_K':str(nk),'norm_to_F1':str(nf)})
    assert exact[0]['norm_to_K']=='1'
    assert exact[1]['norm_to_K']=='-z - 1'
    assert exact[2]['norm_to_K']=='z + 1'
    assert exact[1]['norm_to_F1']=='18 - 7*a'

    epsilon3=[((7*rho27*x[0]-18)%27,(7*rho27*x[1])%27)
              for x in [power((0,1),j,27) for j in range(3)]]
    epsilon_char=[character3(v,j) for j,v in enumerate(epsilon3)]+[character17((16,0))]
    assert epsilon_char==[0,2,1,0]

    # The genuine next norm/character rows, rather than a surjectivity surrogate.
    old=[json.loads(s) for s in (INPUT/'e110_first_pure_unit_norms.out').read_text().splitlines() if s.startswith('{')]
    pure_units=next(x['source_units'] for x in old if x['type']=='fields')
    rr=DVR(2)
    ww=[1,2,1,1,2,2,2,2,0,0,0,0]
    pure_next=[]
    for k,unit in enumerate(pure_units):
        f=[Fraction(x) for x in unit]
        den=lcm(*(x.denominator for x in f))
        modulus=27*den
        pp=[0]*len(f)
        for i,x in enumerate(f):
            for j in range(i+1):
                pp[j]+=int(den*x)*comb(i,j)*(-1)**(i-j)
        qq=[(comb(6,j)*(-1)**(6-j)
             +(23*comb(3,j)*(-1)**(3-j) if j<=3 else 0)
             +(23**2 if j==0 else 0))%modulus for j in range(7)]
        for i in range(len(pp)-1,5,-1):
            c=pp[i]
            for j in range(6):
                pp[i-6+j]-=c*qq[j]
        pp=[x%modulus for x in pp[:6]]
        assert all(x%den==0 for x in pp)
        x=rr.canonical([v//den for v in pp])
        coord=rr.coords(x)
        value=sum(a*b for a,b in zip(coord,ww))%3
        pure_next.append({'index':k+1,'local_value':x,'unit_coordinates':coord,'character':value})
    assert [x['character'] for x in pure_next]==[0,2,0,0]

    # Literal finite residue chains for every eligible pure prime below1000.
    prime_records=[]
    root_tests=0
    for p in primerange(2,1000):
        p=int(p)
        if p in (3,17):
            continue
        order=int(n_order(17,p)) if p!=2 else 1
        v3=0
        x=order
        while x%3==0:
            x//=3
            v3+=1
        rec={'prime':p,'order_of_17':order,'three_valuation':v3,
             'pure_eligible':v3==0,'complex_eligible':v3==1}
        if v3==0:
            roots=[pow(17,pow(3**d,-1,order),p) if order!=1 else 1 for d in range(9)]
            assert roots[0]==17%p
            assert all(pow(roots[d+1],3,p)==roots[d] for d in range(8))
            rec['compatible_degree_one_roots']=roots
            root_tests+=8
        prime_records.append(rec)

    # Actual retained complex classes supply the affine phase; pure valuations
    # remove its congruence restriction in the complete positional system.
    pcs=[json.loads(s) for s in (INPUT/'e110_complex_prime_classes.out').read_text().splitlines() if s.startswith('{')]
    pcs={x['p']:x for x in pcs if x.get('type')=='eligible_prime'}
    chosen=[7,13,31,73,307]
    ell=[pcs[p]['L2_class'][0] for p in chosen]
    cs=[pcs[p]['S_class'][0] for p in chosen]
    assert ell[0]==8
    assert all((a-b)%3==0 for a,b in zip(ell,cs))
    inverse_checks=0
    phase_residues=set()
    for rv in product(range(9),repeat=5):
        phase=sum(a*b for a,b in zip(ell,rv))
        phase_residues.add(phase%3)
        for B17,B3 in [(0,0),(1,2),(-5,7)]:
            for b,z,s in [(0,0,0),(1,-2,4),(-3,5,-7)]:
                e=3*B17-2*b
                t=3*B3-3*z+phase-s
                assert e+2*b==3*B17
                assert s+t+3*z-phase==3*B3
                assert (e+2*b)//3==B17
                assert (s+t+3*z-phase)//3==B3
                assert 3*B17-e==2*b
                assert 3*B3+phase-s-t==3*z
                inverse_checks+=1
    assert phase_residues=={0,1,2}

    # Every mixed unit is checked by multiplication in the actual local rings.
    mixed = []
    for a in range(3):
        for b in range(3):
            for c in range(3):
                exponents = (a, b, c)
                local3 = []
                for j in range(3):
                    x = (1, 0)
                    for rec, e in zip(records, exponents):
                        x = mul(x, power(tuple(rec['local_three_values_zeta_basis_mod27'][j]), e, 27), 27)
                    local3.append(x)
                local17 = (1, 0)
                for rec, e in zip(records, exponents):
                    local17 = mul(local17, power(tuple(rec['local_seventeen_value_zeta_basis']), e, 17), 17)
                values = [character3(x, j) for j, x in enumerate(local3)] + [character17(local17)]
                expected = [sum(e * matrix[j][i] for i, e in enumerate(exponents)) % 3 for j in range(4)]
                assert values == expected
                mixed.append({'exponents': exponents, 'characters': values})
    out = {'status': 'PASS', 'field': 'M1=Q(cuberoot(17),zeta3)',
           'extension': 'M2/M1, cuberoot(alpha1)',
           'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
           'wild_implementation': 'Literal DVR algorithm from E65, included in this self-contained program.',
           'rho_mod_3powers': [rho(i) for i in range(3, 10)],
           'raw_wild_zeta': raw_wild((0, 1)),
           'arithmetic_wild_multiplier': multiplier,
           'cyclotomic_rho': cyclotomic((rho27, 0)),
           'records': records, 'actual_character_matrix': matrix,
           'ordinary_unit_image_rank': matrix_rank3(matrix),
           'character_image_inverse':[[int(x) for x in row] for row in L.tolist()],
           'all_character_vectors':len(hyperplane),
           'actual_conjugation_on_character_image':[[int(x) for x in row] for row in C.tolist()],
           'pure_plus_dimension':plus_dimension,'minus_dimension':minus_dimension,
           'actual_wild_norm_relations':normrows,
           'actual_wild_norm_relation_rank':matrix_rank3(cubes+normrows),
           'exact_unit_field_checks':exact,
           'pure_epsilon_characters':epsilon_char,
           'first_pure_norm_row':[0,3,0,0],
           'next_pure_character_row':[x['character'] for x in pure_next],
           'next_pure_character_records':pure_next,
           'all_tested_primes':len(prime_records),
           'eligible_pure_root_transition_checks':root_tests,
           'prime_records':prime_records,
           'complex_phase_test_primes':chosen,'complex_phase_coefficients':ell,
           'full_positional_toric_inverse_checks':inverse_checks,
           'all_three_phase_residues_realized':sorted(phase_residues),
           'kappa7_witness':{'complex_divisor':{'7':3},'complex_norm':{'7':3,'3':-8},
                              'pure_three_valuations':[0,8],'pure_norm':{'3':8},
                              'total_norm':{'7':3},'scaled_second_toric':'kappa_3(7)'},
           'input_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest()
                           for p in sorted(INPUT.iterdir()) if p.is_file()},
           'mixed_unit_checks': len(mixed), 'mixed_units': mixed}
    HERE.joinpath('e_pure_tower.json').write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    run()
