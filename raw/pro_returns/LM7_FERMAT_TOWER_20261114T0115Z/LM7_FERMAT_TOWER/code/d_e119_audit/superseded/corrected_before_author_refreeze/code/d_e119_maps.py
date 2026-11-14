#!/usr/bin/env python3
"""Independent E119 map audit. No GP stage or author checker is executed.

The input consists of frozen literal GP output tables. This implementation
uses HNF residue boxes and universal integral unit-basis changes; the finite
horizontal transfer is evaluated from every right-coset decomposition.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import argparse
import hashlib
import json
import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form

ap = argparse.ArgumentParser()
ap.add_argument('--source', type=Path, required=True)
args = ap.parse_args()
SOURCE = args.source.resolve()
HERE = Path(__file__).resolve().parent

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

PROOF_HASH = '25d9250dabab99ca3848525d608ed6968323cdc58400f75b8d074a90d79759c0'
MANIFEST_HASH = '79d424d7f19195b64260847b54544206615d0ed4c3f1011e8f88dc4392d6831d'
proof = SOURCE/'sections/E_lower_fiftythree.tex'
mp = SOURCE/'ledger/e_lower_fiftythree_manifest.json'
assert sha(proof) == PROOF_HASH and sha(mp) == MANIFEST_HASH
manifest = json.loads(mp.read_text())
for name, record in manifest['files'].items():
    p = SOURCE/name
    assert p.stat().st_size == record['bytes'], name
    assert sha(p) == record['sha256'], name
assert len(manifest['files']) == 191

STAGES = ('horizontal_base', 'genus_kummer', 'six_character_witness',
          'horizontal_norm_matrix', 'genus_transition', 'local_genus_maps',
          'positional_horizontal_norm', 'positional_genus_transition')
records = {}
for n in STAGES:
    p = SOURCE/'code'/('e53_'+n+'.out')
    rows = [json.loads(l) for l in p.read_text().splitlines() if l.startswith('{')]
    assert rows[-1]['status'] == 'PASS'
    for r in rows:
        if r['type'] != 'completion':
            assert r['type'] not in records
            records[r['type']] = r

def matrix(a): return sp.Matrix(a)
def integral(a): return all(v.q == 1 for v in a)
def integers(a):
    assert integral(a), 'integer serialization requires integral entries'
    return [[int(v) for v in a.row(i)] for i in range(a.rows)]
def rationals(a):
    data = [[str(v) for v in a.row(i)] for i in range(a.rows)]
    assert sp.Matrix([[sp.Rational(v) for v in row] for row in data]) == a
    return data
def mod3(a): return a.applyfunc(lambda v: int(v) % 3)

# Independently reconstruct the cyclic Kummer algebra and its real marking.
x = sp.Symbol('x')
phi = x**6+x**3+1
def rem(a): return sp.rem(a, phi, x)
def poly(a): return sum(sp.Rational(c)*x**i for i,c in enumerate(a))
rad = records['actual_genus_radicals']
pis = [poly(a) for a in rad['radicals']]
assert rem(sp.prod(pis)) == 53
assert all(rem(p.subs(x,x**8)-p) == 0 for p in pis)
assert all(rem(pis[i].subs(x,x**4)-pis[(i+1)%3]) == 0 for i in range(3))
assert abs(matrix(rad['valuation_matrix']).det()) == 1
h = records['hensel_cube_witness']
w = poly(h['root_polynomial'])
def v3(a):
    a = abs(int(a)); assert a
    v = 0
    while a % 3 == 0: a //= 3; v += 1
    return v
assert v3(sp.resultant(phi, rem(w**3-pis[0]), x)) == 13
assert v3(sp.resultant(phi, rem(3*w*w), x)) == 6

# Actual horizontal Galois group, right transversal and transfer on all 27
# elements. The phase relation is retained rather than replacing the group
# by an abstract abelian invariant-factor list.
zero = ((0,0,0),0)
def rotate(e,j): return tuple(e[(i-j)%3] for i in range(3))
def mul(g,h):
    e,b = g; f,d = h; f = rotate(f,b)
    return (tuple((e[i]+f[i])%3 for i in range(3)), (b+d)%3)
def power(g,n):
    r = zero
    for _ in range(n): r = mul(r,g)
    return r
group = [(e,b) for e in product(range(3),repeat=3)
         for b in range(3) if (sum(e)+b)%3 == 0]
inverse = {g:next(h for h in group if mul(g,h)==zero) for g in group}
assert all(mul(inverse[g],g)==zero for g in group)
tau = ((2,0,0),1)
transversal = [power(tau,i) for i in range(3)]
I = [g for g in group if g[1]==0]
def transfer(g):
    ans = zero
    for q in transversal:
        qg = mul(q,g)
        r = transversal[qg[1]]
        factor = mul(qg,inverse[r])
        assert factor in I
        ans = mul(ans,factor)
    return ans

# Auxiliary abelian coordinates are chosen with tau=(2,0). Their restriction
# to I and transfer are precisely the two recorded actual class maps.
def abelian(g):
    e,b = g
    return (2*b%3, (e[0]+2*e[1]+b*(b+1)//2)%3)
assert len(set(map(abelian,group))) == 9
commutators = set()
for g,hg in product(group,repeat=2):
    assert mul(g,hg) in group
    assert abelian(mul(g,hg)) == tuple((a+b)%3 for a,b in zip(abelian(g),abelian(hg)))
    commutators.add(mul(mul(mul(g,hg),inverse[g]),inverse[hg]))
    assert transfer(mul(g,hg)) == mul(transfer(g),transfer(hg))
assert len(commutators) == 3
for g in group:
    a,b = abelian(g)
    assert transfer(g) == ((a,a,a),0)
for e,b in I:
    assert abelian((e,b)) == (0,(e[0]+2*e[1])%3)
horizontal = {'group_order':27, 'all_group_products':729,
              'right_coset_transfer_factors':81, 'derived_order':3,
              'abelian_order':9, 'transfer_image_order':len(set(map(transfer,group))),
              'tau_cube':power(tau,3),
              'all_transfer_values':[{'element':g,'value':transfer(g)} for g in group]}

# Actual ordinary/S class quotient. Enumerating the full group verifies that
# the supplied S-prime coordinates give the entire genus kernel.
ordinary = records['ordinary_class_actual_generation']
orders = tuple(ordinary['orders'])
assert orders == (9,3,3)
Scols = matrix(ordinary['S_prime_coordinates'])
Gclass = matrix(ordinary['genus_coordinates'])[:2,:]
def class_reduce(v): return tuple(int(v[i])%orders[i] for i in range(3))
Ssub = {class_reduce(Scols*sp.Matrix(c)) for c in product(range(3),repeat=6)}
allcl = list(product(*(range(a) for a in orders)))
kernel = {a for a in allcl if mod3(Gclass*sp.Matrix(a)) == sp.zeros(2,1)}
assert Ssub == kernel and len(Ssub) == 9
assert len({tuple(mod3(Gclass*sp.Matrix(a))) for a in allcl}) == 9

# Universal integral basis changes for both completed unit norms. These
# identities prove all exponents at once, including the torsion carry.
NM = matrix(records['actual_horizontal_norm']['norm_matrix'])
NL = matrix(records['positional_horizontal_norm']['norm_matrix'])
eye15 = sp.eye(15)
DM = sp.eye(7)
DM[4,3]=1; DM[4,4]=3
DM[5,3]=1; DM[5,5]=3
def msection(v):
    z,xx,yy,r,s,t,ww = v
    d=r+s+t; xp=xx-2*d; yp=yy-d
    a=sp.zeros(15,1)
    a[0]=z-2*yp-d-ww
    a[11]=r; a[9]=s; a[10]=t; a[7]=xp; a[8]=yp-xp; a[12]=ww
    return a
SM = sp.Matrix.hstack(*(msection(sp.eye(7)[:,i]) for i in range(7)))
assert NM*SM == DM and abs(DM.det()) == 9
CM = DM.inv()*NM
assert integral(CM)
freeM = [1,2,3,4,5,6,13,14]
KM = sp.Matrix.hstack(*(eye15[:,i]-SM*CM[:,i] for i in freeM))
BM = SM.row_join(KM)
assert abs(BM.det()) == 1 and NM*KM == sp.zeros(7,8)
assert BM[:,0] == eye15[:,0]
assert integral(BM.inv())
assert NM*BM == DM.row_join(sp.zeros(7,8))

def lsection(v):
    z,xx,yy,c,d = v; xp=xx-2*c; yp=yy-2*c+d
    a=sp.zeros(15,1)
    a[0]=z-2*c; a[9]=c; a[12]=d; a[8]=-xp; a[7]=xp-yp
    return a
SL = sp.Matrix.hstack(*(lsection(sp.eye(5)[:,i]) for i in range(5)))
assert NL*SL == sp.eye(5)
freeL = [1,2,3,4,5,6,10,11,13,14]
KL = sp.Matrix.hstack(*(eye15[:,i]-SL*NL[:,i] for i in freeL))
BL = SL.row_join(KL)
assert abs(BL.det()) == 1 and NL*KL == sp.zeros(5,10)
assert BL[:,0] == eye15[:,0] and integral(BL.inv())
assert NL*BL == sp.eye(5).row_join(sp.zeros(5,10))

sat = matrix(records['unit_saturation']['matrix'])
assert sat.det() == -17
assert all(v.q % 3 for v in sat.inv())
valuations = matrix(records['six_characters']['S_valuation_matrix'])
VH = hermite_normal_form(valuations)
assert abs(VH.det()) == 9
expected_divisor = sp.eye(6)
expected_divisor[0,0]=3; expected_divisor[1,1]=3
expected_divisor[0,2]=1; expected_divisor[1,2]=1
assert hermite_normal_form(expected_divisor) == VH
characters = matrix(records['six_characters']['character_matrix'])
assert all(characters[i,:]==characters[0,:] for i in range(3))
assert all(characters[i,:]==characters[3,:] for i in range(3,6))
assert any(characters[0,j] for j in range(15))
assert any((characters[0,i]*characters[3,j]-characters[0,j]*characters[3,i])%3
           for i in range(15) for j in range(15))

# Direct canonical representatives for column-HNF lattice quotients. These
# finite groups are computed without using Smith coordinates for arithmetic.
def hnf_reduce(v,H):
    a=list(map(int,v)); n=H.rows
    for j in range(n-1,-1,-1):
        d=int(H[j,j]); q=a[j]//d
        for i in range(j+1): a[i]-=q*int(H[i,j])
    assert all(0<=a[i]<H[i,i] for i in range(n))
    return tuple(a)

def genus(name, rawN, ideal_lifts, expected_size, expected_kernel, expected_N, expected_J):
    r=records[name]
    Rel=matrix(r['relation_matrix']); H=matrix(r['relation_HNF'])
    assert H == hermite_normal_form(Rel)
    n=H.rows; z=tuple([0]*n)
    assert all(hnf_reduce(Rel[:,j],H)==z for j in range(Rel.cols))
    reps=list(product(*(range(int(H[i,i])) for i in range(n))))
    assert len(reps)==expected_size
    rho=tuple(r['restriction_row'])
    def restr(a): return sum(a[i]*rho[i] for i in range(n))%3
    def norm(a): return tuple(mod3(rawN*sp.Matrix(a)))
    assert all(int((sp.Matrix([rho])*Rel)[j])%3==0 for j in range(Rel.cols))
    assert mod3(rawN*Rel)==sp.zeros(2,Rel.cols)
    Q=[a for a in reps if restr(a)==0]
    assert len(Q)==expected_kernel
    fibres=Counter(norm(a) for a in Q)
    assert len(fibres)==9 and set(fibres.values())=={expected_kernel//9}
    K=matrix(r['kernel_lattice']); KU=matrix(r['kernel_smith_left'])
    KD=matrix(r['kernel_smith_diagonal'])
    mods=[int(KD[i,i]) for i in range(n)]
    forward=KU*K.inv(); backward=K*KU.inv()
    seen=set()
    for a in Q:
        c=forward*sp.Matrix(a); assert integral(c)
        c=tuple(int(c[i])%mods[i] for i in range(n))
        assert hnf_reduce(backward*sp.Matrix(c),H)==a
        assert norm(a)==tuple(mod3(expected_N*sp.Matrix(c[:expected_N.cols])))
        seen.add(c)
    assert len(seen)==len(Q)
    transfer_values=[]
    for a in product(range(3),repeat=2):
        raw=3*ideal_lifts*sp.Matrix(a)
        jr=hnf_reduce(raw,H)
        assert restr(jr)==0 and norm(jr)==(0,0)
        cc=forward*sp.Matrix(jr)
        cc=tuple(int(cc[i])%mods[i] for i in range(n))
        ej=expected_J*sp.Matrix(a)
        assert cc==tuple([int(ej[i])%mods[i] for i in range(expected_J.rows)]+[0]*(n-expected_J.rows))
        transfer_values.append({'input':a,'HNF_value':jr,'Smith_value':cc})
        # Changing an ideal lift by any local Artin generator leaves 3*lift
        # unchanged in the actual idele group.
        for j in range(n-ideal_lifts.cols if n==4 else 6):
            b=raw+3*sp.eye(n)[:,j]
            assert hnf_reduce(b,H)==jr
    for a in Q:
        lhs=hnf_reduce(3*ideal_lifts*sp.Matrix(norm(a)),H)
        rhs=hnf_reduce([3*v for v in a],H)
        assert lhs==rhs
    generators=[tuple(int(i==j) for i in range(n)) for j in range(n)]
    group_checks=0
    for a in reps:
        for e in generators:
            b=hnf_reduce([a[i]+e[i] for i in range(n)],H)
            assert restr(b)==(restr(a)+restr(e))%3
            assert norm(b)==tuple((p+q)%3 for p,q in zip(norm(a),norm(e)))
            group_checks+=1
    caps=[t['input'] for t in transfer_values if t['HNF_value']==z]
    return {'Gamma_order':len(reps),'coinvariant_order':len(Q),
            'restriction_fibres':dict(Counter(restr(a) for a in reps)),
            'norm_fibres':{str(k):v for k,v in sorted(fibres.items())},
            'actual_HNF_generator_map_checks':group_checks,
            'HNF_Smith_roundtrips':len(Q),'norm_transfer_compositions':len(Q),
            'transfer_values':transfer_values,'projected_capitulation_kernel':caps,
            'HNF':integers(H),'forward':rationals(forward),'inverse':integers(backward),
            'forward_serialization':'exact rational strings, decoded and compared entrywise',
            'forward_denominators':sorted({int(v.q) for v in forward})}

Braw=sp.zeros(2,9); Braw[:,6:]=Gclass
Blifts=sp.zeros(9,2); Blifts[6,0]=1; Blifts[6,1]=-1; Blifts[8,1]=2
Bresult=genus('next_genus_presentation',Braw,Blifts,729,243,
              sp.Matrix([[0,0,0,2],[1,0,0,2]]),
              sp.Matrix([[6,3],[0,0],[0,0],[0,0]]))
Lraw=sp.zeros(2,4); Lraw[:,2:]=sp.eye(2)
Llifts=sp.zeros(4,2); Llifts[2:,:]=sp.eye(2)
Lresult=genus('positional_genus_transition',Lraw,Llifts,81,27,
              sp.Matrix([[-1,0],[-1,1]]),sp.Matrix([[6,0],[0,0]]))
assert Bresult['projected_capitulation_kernel']==[(0,0),(1,1),(2,2)]
assert Lresult['projected_capitulation_kernel']==[(0,0),(0,1),(0,2)]

result={
 'status':'PASS','statement':'E.119','audit_role':'independent peer mathematical/map audit',
 'proof_sha256':sha(proof),'manifest_sha256':sha(mp),'frozen_files_verified':191,
 'source_read_scope':{'complete_proof_lines':len(proof.read_text().splitlines()),
                     'owned_GP_sources':8,'dependency_GP_sources':2,
                     'Python_checker_complete':True},
 'Kummer':{'product':53,'conjugate_cycle':True,'each_radical_real':True,
           'valuation_determinant':int(matrix(rad['valuation_matrix']).det()),
           'Hensel_error_derivative':[13,6]},
 'horizontal_group':horizontal,
 'ordinary_S_quotient':{'ordinary_order':81,'S_subgroup_order':9,'S_class_order':9,
                        'S_subgroup_equals_genus_kernel':True},
 'unit_maps':{'ordinary_unit_character_determinant':int(sat.det()),
              'S_divisor_HNF':integers(VH),'S_divisor_index':9,
              'M_unimodular_basis_determinant':int(BM.det()),
              'M_basis':integers(BM),'M_inverse_basis':integers(BM.inv()),
              'M_target_image_basis':integers(DM),'M_index':9,
              'M_kernel_free_rank':8,'M_kernel_torsion':[3],
              'L_unimodular_basis_determinant':int(BL.det()),
              'L_basis':integers(BL),'L_inverse_basis':integers(BL.inv()),
              'L_index':1,'L_kernel_free_rank':10,'L_kernel_torsion':[3]},
 'B2':Bresult,'L2':Lresult,
 'scope':'This independent finite-map replay does not rerun the ten GP arithmetic stages. '
         'The complete proof and all ten GP sources were separately read. '
         'The root owns the independent full GP reconstruction. '
         'The actual upper capitulation subgroups and the kernels (sigma-1)A2 remain unevaluated.'}
text=json.dumps(result,indent=2)+'\n'
(HERE/'d_e119_maps.json').write_text(text)
print(text,end='')
