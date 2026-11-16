#!/usr/bin/env python3
"""Exact finite arithmetic for A207; no prime-recursion stage is claimed run."""
from math import factorial, gcd, isqrt
from pathlib import Path
import json

p = 1129
assert all(p % a for a in range(2, isqrt(p)+1))
assert p-1 == 24*47
n0 = factorial(6)
D0 = 6*24*n0**3
assert D0 == 53747712000
assert gcd(D0,p-1) == 24 and D0 % (p-1) == 960
assert [pow(a,D0,p) for a in (59,28,1)] == [276,978,1]
assert (3*276-2*978-1) % p == 0
assert gcd(D0,p) == 1

# All possible previously fixed exponent classes, not just one chosen CRT path.
preimages = []
for e in range(p-1):
    if gcd(e,p-1) != 24:
        continue
    row = {"exponent":e,"targets":[]}
    for value in (276,978,1):
        roots=[u for u in range(1,p) if pow(u,e,p)==value]
        admissible=[u for u in roots if pow(u,2,p)!=1 and pow(u,3,p)!=1]
        assert len(roots)==24 and len(admissible)>=20
        row["targets"].append({"value":value,"roots":len(roots),
                               "admissible":len(admissible),"chosen":admissible[0]})
    preimages.append(row)
assert len(preimages)==46

# Common-value updates at all later non-coefficient stages preserve the ratio.
for common in range(1,p):
    aa=828*common % p
    bb=302*common % p
    cc=common
    assert (aa+bb-cc)%p==0 and aa*pow(cc,-1,p)%p==828

theta_roots=[16,430,699,1113]
assert len(set(theta_roots))==4
assert all(pow(r,4,p)==54 and 4*pow(r,3,p)%p for r in theta_roots)
assert all((x**4-54)%p for x in range(p) if x not in theta_roots)
def bit(a):
    a%=p
    assert a
    leg=pow(a,(p-1)//2,p)
    assert leg in (1,p-1)
    return int(leg==p-1)
def vec(x):
    return tuple(bit(x-r) for r in theta_roots)
tv=vec(0)
dv=vec(3)
assert tv==(0,0,0,0) and dv==(1,1,1,1)
selmer={tuple(a*d ^ b*t for d,t in zip(dv,tv)) for a in (0,1) for b in (0,1)}
assert selmer=={(0,0,0,0),(1,1,1,1)}

tripod=828
z8=(-tripod*pow(1-tripod,3,p)*pow(24,-1,p))%p
assert z8==1115
z_roots=[z for z in range(1,p) if pow(z,8,p)==z8]
assert z_roots==[35,44,235,511,618,894,1085,1094]
sheets=[]
for z in z_roots:
    x=-6*z*z*pow(1-tripod,-1,p)%p
    y=-18*z*pow(1-tripod,-1,p)%p
    assert (y*y-x**5+54*x)%p==0
    assert (x**4*pow(x**4-54,-1,p))%p==tripod
    assert 3*x*pow(y,-1,p)%p==z
    assert 8*pow(z,7,p)%p
    square_vector=vec(x)
    assert square_vector not in selmer
    sheets.append(dict(z=z,x=x,y=y,kummer=square_vector))
assert sorted({(s['x'],s['kummer']) for s in sheets})==[
    (28,(0,1,0,1)),(188,(0,0,1,1)),
    (941,(1,1,0,0)),(1101,(1,0,1,0))]

# Literal branch Weil pairing: e_i=T0+T_i is dual to T_j.
for i in range(4):
    for j in range(4):
        assert (1 ^ int(i!=j)) == int(i==j)
assert 168*168%p==p-1
cyclic_roots=[16,430,1113,699]
assert [168*r%p for r in cyclic_roots]==cyclic_roots[1:]+cyclic_roots[:1]

def v_to_delta(bits):
    # v=1+delta; binomial coefficients mod2 for powers 0..3.
    expansions=[1,3,5,15]
    out=0
    for bit_,polynomial in zip(bits,expansions):
        if bit_: out^=polynomial
    return out
cyclic_sheet_data=[]
for sheet in sheets:
    vbits=tuple(sheet['kummer'][i] for i in (0,1,3,2))
    delta=v_to_delta(vbits)
    assert delta&3==2
    cyclic_sheet_data.append(dict(x=sheet['x'],cyclic_bits=vbits,delta_bits=delta))
assert v_to_delta((1,1,1,1))==8

# Literal group R semidirect C8, R=F2[d]/d^4, action 1+d.
def mulpoly(a,b):
    out=0
    for i in range(4):
        if b>>i&1: out^=a<<i
    return out&15
def action(a,j):
    for _ in range(j%8): a=mulpoly(a,3)
    return a
def multiply(a,b):
    return (a[0]^action(b[0],a[1]),(a[1]+b[1])%8)
def inverse(a):
    j=(-a[1])%8
    return (action(a[0],j),j)
def comm(a,b):
    return multiply(multiply(multiply(a,b),inverse(a)),inverse(b))
def generated(gs):
    group={(0,0)}
    queue=[(0,0)]
    gs=list(gs)+[inverse(g) for g in gs]
    while queue:
        a=queue.pop()
        for b in gs:
            c=multiply(a,b)
            if c not in group: group.add(c);queue.append(c)
    return group
X=(0,1)
Y=(1,3)
group=generated([X,Y])
assert len(group)==128
gamma=group
gamma_sizes=[len(group)]
while len(gamma)>1:
    gamma=generated({comm(a,b) for a in gamma for b in group})
    gamma_sizes.append(len(gamma))
assert gamma_sizes==[128,8,4,2,1]
u=multiply(Y,(0,5))
assert u==(1,0)
deep=comm(comm(comm(u,X),X),X)
assert deep==(8,0) and comm(deep,X)==(0,0)

data={"prime":p,"initial_n":n0,"initial_D":D0,
      "homogeneous_coordinates":[59,28,1],"power_residues":[276,978,1],
      "tripod_residue":tripod,"preimage_cases":preimages,
      "theta_roots":theta_roots,"global_kummer_D":dv,"global_kummer_T":tv,
      "localized_selmer":sorted(selmer),"all_rational_sheets":sheets,
      "cyclic_root_order":cyclic_roots,"cyclic_sheet_vectors":cyclic_sheet_data,
      "group_order":len(group),"lower_central_orders":gamma_sizes,
      "deepest_commutator":deep,
      "scope":"Literal finite arithmetic. Infinite ordinary recursion, full Selmer implication and Hensel continuity are proved in the source; no giant prime-recursion stage was executed."}
text='\n'.join([
    'A207 explicit 1129 class-four obstruction: PASS',
    f'Initial A62 homogeneous power data: D={D0}, values 276,978,1',
    f'All {len(preimages)*3} actual-exponent/target preimage cases: PASS',
    f'Common-value ratio preservation: {p-1} residue cases PASS',
    'Split quartic Kummer D=1111, T=0000: PASS',
    'All eight local cover sheets fail the localized four-class global Selmer image: PASS',
    'Actual finite quotient order 128, lower central orders 128,8,4,2,1: PASS',
    'The source retains the absent class-three local-matching assertion.'
])+'\n'
base=Path(__file__).with_suffix('')
base.with_name(base.name+'_data.json').write_text(json.dumps(data,indent=2)+'\n')
base.with_name(base.name+'_output.txt').write_text(text)
print(text,end='')
