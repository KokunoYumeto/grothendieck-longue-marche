#!/usr/bin/env python3
"""Peer check of E122's literal fields, genus maps and unit-norm lattice.

No author executable is imported. Polynomial multiplication uses a two-stage
convolution and monic reduction; it does not use the author's multiplication
table. Genus maps are checked on full HNF residue sets before Smith transport.
"""
from pathlib import Path
from fractions import Fraction
from math import gcd, lcm, prod
from functools import reduce
import itertools, json, hashlib, time
import sympy as S

START = time.monotonic()
ROOT = Path(__file__).resolve().parents[1]
INP = ROOT / 'inputs'
W = json.loads((INP/'e122_literal_unit_witnesses.json').read_text())

def records(name):
    return [json.loads(s) for s in (INP/name).read_text().splitlines() if s.startswith('{')]

def record(name, kind):
    return next(r for r in records(name) if r['type'] == kind)

def integer(x):
    q = Fraction(str(x)); assert q.denominator == 1
    return q.numerator

def rational_matrix(M):
    out = [[str(M[i,j]) for j in range(M.cols)] for i in range(M.rows)]
    assert S.Matrix([[S.Rational(x) for x in row] for row in out]) == M
    return out

def rank_mod(M, p):
    a = [[integer(M[i,j]) % p for j in range(M.cols)] for i in range(M.rows)]
    row = 0
    for col in range(M.cols):
        k = next((i for i in range(row, M.rows) if a[i][col]), None)
        if k is None: continue
        a[row], a[k] = a[k], a[row]
        inv = pow(a[row][col], -1, p)
        a[row] = [(x*inv) % p for x in a[row]]
        for i in range(M.rows):
            if i != row:
                c = a[i][col]
                a[i] = [(x-c*y) % p for x,y in zip(a[i], a[row])]
        row += 1
        if row == M.rows: break
    return row

def mod_matrix(M, p):
    def f(x):
        q = Fraction(str(x)); assert gcd(q.denominator, p) == 1
        return q.numerator*pow(q.denominator, -1, p) % p
    return M.applyfunc(f)

class Field:
    """Q[b,z]/(b^9-53 z^3,z^6+z^3+1), 6*i+j order."""
    __slots__ = ('v','d')
    def __init__(self, v, d=1):
        v = tuple(map(int,v)); d = int(d); assert len(v)==54 and d
        if d < 0: v = tuple(-x for x in v); d = -d
        g = reduce(gcd, v, d)
        self.v = tuple(x//g for x in v); self.d = d//g
    @classmethod
    def scalar(cls, q):
        q = Fraction(q); v = [0]*54; v[0] = q.numerator
        return cls(v,q.denominator)
    @classmethod
    def coefficients(cls, vals):
        vals = list(map(Fraction, vals)); d = lcm(*(q.denominator for q in vals))
        return cls([q.numerator*(d//q.denominator) for q in vals], d)
    def __add__(self, other):
        return Field([self.v[i]*other.d+other.v[i]*self.d for i in range(54)],self.d*other.d)
    def __neg__(self): return Field([-x for x in self.v],self.d)
    def __sub__(self,other): return self+-other
    def __mul__(self,other):
        # First convolve in the unrestricted b,z polynomial ring.
        c = [[0]*14 for _ in range(17)]
        left = [(i//6,i%6,x) for i,x in enumerate(self.v) if x]
        right = [(i//6,i%6,x) for i,x in enumerate(other.v) if x]
        for i,j,x in left:
            for k,l,y in right: c[i+k][j+l] += x*y
        # Reduce b^9 first, then the literal cyclotomic polynomial.
        for i in range(16,8,-1):
            for j in range(11): c[i-9][j+3] += 53*c[i][j]
        for i in range(9):
            for j in range(13,5,-1):
                c[i][j-3] -= c[i][j]
                c[i][j-6] -= c[i][j]
        return Field([c[i][j] for i in range(9) for j in range(6)],self.d*other.d)
    def __pow__(self,n):
        assert n>=0
        a = ONE; b = self
        while n:
            if n%2: a = a*b
            n//=2
            if n: b = b*b
        return a
    def __eq__(self,other): return self.v==other.v and self.d==other.d
    def sigma(self,k):
        out = ZERO
        for i in range(9):
            for j in range(6):
                n = self.v[6*i+j]
                if n: out = out + Field.scalar(Fraction(n,self.d))*(B**i)*(Z**((j+3*k*i)%9))
        return out

ZERO=Field([0]*54); ONE=Field.scalar(1)
def monomial(i,j):
    v=[0]*54; v[6*i+j]=1; return Field(v)
B=monomial(1,0); Z=monomial(0,1)
assert B**9==Field.scalar(53)*Z**3
assert Z**6+Z**3+ONE==ZERO and Z**9==ONE
ELL=Z-(B**3)*(Z**8)
def evaluate(coeffs,x):
    value=ZERO
    for q in reversed(coeffs): value=value*x+Field.scalar(q)
    return value
lower=[evaluate(c,ELL) for c in W['lower_units']]
assert lower[0]==Z
upper=[evaluate(c,B*Z**j) for c in W['upper_candidates'] for j in range(3)]
units=lower+upper
roots=[Field.coefficients(c) for c in W['roots']]
checks=[]
for i,root in enumerate(roots):
    lhs=root**3; rhs=ONE
    for unit,e in zip(units,W['root_exponents'][i]):
        if e<0: lhs=lhs*unit**(-e)
        if e>0: rhs=rhs*unit**e
    assert lhs==rhs,('cube',i+1)
    norm=root*root.sigma(1)*root.sigma(2)
    assert norm.sigma(1)==norm
    lhs=norm; rhs=Field.scalar(W['lower_norm_signs'][i])
    for j,unit in enumerate(lower):
        e=W['lower_norm_coordinates'][j][i]
        if e<0: lhs=lhs*unit**(-e)
        if e>0: rhs=rhs*unit**e
    assert lhs==rhs,('norm',i+1)
    checks.append(i+1)
print('Exact independent polynomial cubes/norms:',len(checks),flush=True)

# Full genus maps in HNF coordinates.
old=record('e119_e53_genus_transition.out','next_genus_presentation')
new=record('e53_higher_genus.out','B3_over_B1_genus')
H0=S.Matrix(old['relation_HNF']); H1=S.Matrix(new['relation_HNF'])
def hnf_reduce(v,H):
    a=list(map(integer,v)); n=H.rows
    for j in reversed(range(n)):
        q=a[j]//integer(H[j,j])
        for i in range(j+1): a[i]-=q*integer(H[i,j])
    return tuple(a)
def residue_set(H):
    return list(itertools.product(*(range(integer(H[i,i])) for i in range(H.rows))))
def restr(v,rho,m): return sum(x*y for x,y in zip(v,rho))%m
all0=residue_set(H0); all1=residue_set(H1)
ker0=[v for v in all0 if not restr(v,old['restriction_row'],3)]
ker1=[v for v in all1 if not restr(v,new['restriction_row'],9)]
assert len(all0)==729 and len(all1)==2187 and len(ker0)==len(ker1)==243
assert all(S.denom(x)==1 for x in H0.inv()*H1)
actual_norm={v:hnf_reduce(v,H0) for v in ker1}
assert set(actual_norm.values())==set(ker0)
inverse_norm={w:v for v,w in actual_norm.items()}; assert len(inverse_norm)==243
smith_maps=[]
for data,H,kernel in [(old,H0,ker0),(new,H1,ker1)]:
    K=S.Matrix(data['kernel_lattice']); U=S.Matrix(data['kernel_smith_left'])
    V=S.Matrix(data['kernel_smith_right']); d=data['kernel_smith_diagonal']
    D=S.Matrix(d) if isinstance(d[0],list) else S.diag(*d)
    assert U*K.inv()*H*V==D and abs(U.det())==abs(V.det())==1
    forward=U*K.inv(); backward=K*U.inv()
    orders=[integer(D[i,i]) for i in range(9)]
    for v in kernel:
        w=forward*S.Matrix(v); assert all(S.denom(x)==1 for x in w)
        w=S.Matrix([integer(x)%m for x,m in zip(w,orders)])
        assert hnf_reduce(backward*w,H)==v
    smith_maps.append((forward,backward,orders))
    assert len(set(tuple(integer(x)%m for x,m in zip(forward*S.Matrix(v),orders)) for v in kernel))==243
F0,I0,ord0=smith_maps[0]; F1,I1,ord1=smith_maps[1]
active0=[i for i,x in enumerate(ord0) if x>1]; active1=[i for i,x in enumerate(ord1) if x>1]
N=F0*I1; small=N.extract(active0,active1)
assert small==S.eye(4)
for v,w in actual_norm.items():
    expected=hnf_reduce(3*S.Matrix(v),H1)
    assert hnf_reduce(3*S.Matrix(inverse_norm[w]),H1)==expected
    assert hnf_reduce(3*S.Matrix(w),H0)==hnf_reduce(expected,H0)

# Every local norm subgroup, with the actual calibrated character.
local_rows=records('e53_higher_local.out')
setup=next(r for r in local_rows if r['type']=='local_ninth_setup')
local_checks=[]
for row in (r for r in local_rows if r['type']=='local_ninth_norm'):
    H=S.Matrix(row['norm_HNF']); A=S.Matrix(row['norm_logs'])
    L=S.Matrix(row['smith_left']); R=S.Matrix(row['smith_right'])
    D=S.diag(*row['smith_diagonal']); chi=S.Matrix([row['positive_character']])
    assert L*H*R==D and abs(L.det())==abs(R.det())==1 and abs(H.det())==9
    assert all(S.denom(x)==1 for x in H.inv()*A)
    assert all(S.denom(x)==1 for x in H.inv()*9*S.eye(7))
    assert mod_matrix(chi*A,9)==S.zeros(1,55)
    assert integer((chi*S.Matrix(setup['four_log']))[0])%9==row['calibration_four']
    assert row['calibration_four']==4*(1+3*row['label'])%9
    local_checks.append(row['label'])
assert pow(4,-6,81)==37

# Reconstruct all upper characters from actual lower norm-coordinate columns.
C9=S.Matrix(record('e53_higher_genus.out','higher_complete_S_unit_characters')['matrix'])
NC=S.Matrix(W['lower_norm_coordinates'])
raw=C9*NC
assert all(integer(x)%3==0 for x in raw)
derived=mod_matrix(raw/3,3)
wr=record('e53_upper_witness_verify.out','literal_unit_witness_verification')
assert derived==S.Matrix(wr['root_character_matrix'])
included=mod_matrix(C9,3)
assert included==S.Matrix(wr['with_included_lower_characters'])[:,:15]
assert rank_mod(included,3)==2
five=included[:,[7,9]].row_join(derived[:,[7,13,19]])
assert five==S.Matrix([[0,1,2,0,2],[0,1,0,1,2],[0,1,1,2,1],[2,0,0,0,2],[2,0,1,0,1],[2,0,2,0,1]])
assert mod_matrix(S.ones(1,6)*five,3)==S.zeros(1,5)
assert five[:5,:].det()==-4 and rank_mod(five,3)==5
five_images={tuple(integer(x)%3 for x in five*S.Matrix(v)) for v in itertools.product(range(3),repeat=5)}
hyperplane={v for v in itertools.product(range(3),repeat=6) if sum(v)%3==0}
assert five_images==hyperplane and len(five_images)==243

# Exact completed unit-norm lattice, its congruence quotient and inverse.
H=S.Matrix(W['norm_lattice_HNF'])
idx=[0,7,8,9,10,11,13,14,19]; unitidx=[1,2,3,7,9,11]
M=NC[:,idx].row_join(3*S.eye(15)[:,unitidx]); MI=M.inv()
assert M.det()==94770 and abs(H.det())==729
assert M*MI==MI*M==S.eye(15)
assert all(S.denom(x)%3 for x in MI*H)
assert all(S.denom(x)%3 for x in H.inv()*M)
assert all(S.denom(x)==1 for x in H.inv()*NC)
assert all(S.denom(x)==1 for x in H.inv()*3*S.eye(15))
Q=mod_matrix(3*MI[9:,:],3); J=S.eye(15)[:,unitidx]
assert Q*J==S.eye(6)
assert mod_matrix(Q*NC,3)==S.zeros(6,22)
assert mod_matrix(Q*S.eye(15)[:,0]*9,3)==S.zeros(6,1)
quotients={tuple(integer(x)%3 for x in Q*J*S.Matrix(v)) for v in itertools.product(range(3),repeat=6)}
assert len(quotients)==729
ring=json.loads((INP/'e53_literal_unit_ring.json').read_text())
assert Q==S.Matrix(ring['norm_congruence_matrix_mod_three'])
assert MI==S.Matrix(ring['norm_basis_inverse'])

# The exact polynomial equalities used in the all-level induction.
t=S.symbols('t'); s=(1+t)**3-1
assert S.expand(s)==3*t+3*t**2+t**3
assert S.expand(1+(1+s)+(1+s)**2-(3+3*s+s**2))==0
assert S.rem(S.expand(1+(1+t)+(1+t)**2-3),t**2,t)==3*t
assert all(S.binomial(9,k)%3==0 for k in range(1,9))
assert (53**2-1)%27==0
result={
    'status':'PASS',
    'all_independent_cube_identities':checks,
    'all_independent_relative_norm_identities':checks,
    'full_HNF_genus_orders':[len(all0),len(all1)],
    'actual_kernel_orders':[len(ker0),len(ker1)],
    'actual_norm_checked_on_all_kernel_elements':len(actual_norm),
    'ambient_coordinate_map_before_kernel_transport':rational_matrix(S.eye(9)),
    'old_forward_exact_rational':rational_matrix(F0),
    'new_forward_exact_rational':rational_matrix(F1),
    'norm_in_full_Smith_coordinates':rational_matrix(N),
    'norm_in_active_Smith_coordinates':rational_matrix(small),
    'local_norm_characters_checked':local_checks,
    'local_norm_log_columns_checked':165,
    'derived_all_upper_character_columns':rational_matrix(derived),
    'five_character_matrix':rational_matrix(five),
    'five_character_determinant':-4,
    'all_product_formula_hyperplane_elements':len(hyperplane),
    'norm_basis':rational_matrix(M),
    'norm_basis_inverse_exact_rational':rational_matrix(MI),
    'HNF_to_norm_basis':rational_matrix(MI*H),
    'norm_basis_to_HNF':rational_matrix(H.inv()*M),
    'norm_quotient_matrix':rational_matrix(Q),
    'norm_quotient_right_inverse':rational_matrix(J),
    'norm_quotient_elements':len(quotients),
    'input_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(INP.glob('*')) if p.is_file()},
    'elapsed_seconds':time.monotonic()-START,
    'scope':'Independent full polynomial identities and finite-map checks from copied literal data; no author executable imported. Local residue logs and ideal support are also proof/source audited; the separate peer GP program checks every candidate principal ideal. This is not a replay of the author three-stage arithmetic construction.'
}
out=json.dumps(result,indent=2)+'\n'
(ROOT/'code/d_e122_maps.json').write_text(out)
print(out,end='')
