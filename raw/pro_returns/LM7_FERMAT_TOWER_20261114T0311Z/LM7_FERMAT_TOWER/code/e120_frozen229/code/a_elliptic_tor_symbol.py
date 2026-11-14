#!/usr/bin/env python3
"""Literal Tor symbol, proper regulator and the residual three-torsion.

No value of the unknown intrinsic handle action is assigned.  This
certificate constructs an actual arithmetic symbol whose regulator is
the generator of its retained C3 ambiguity, in the original marking.
"""
from pathlib import Path
from itertools import combinations
import hashlib
import json
import sympy as s
from a_e120_exact import QZ

base = Path(__file__).resolve().parent
input_names = ['a_handle_comparison.json', 'a_cusp_unit_symbols.json',
               'a_handle_torsion_gauge.json', 'a_e120_exact.py']
handles = json.loads((base/input_names[0]).read_text())
units = json.loads((base/input_names[1]).read_text())
gauge = json.loads((base/input_names[2]).read_text())
mat = lambda a: s.Matrix([[s.Rational(v) for v in row] for row in a])
enc = lambda a: [[str(v) for v in a.row(i)] for i in range(a.rows)]
T = mat(handles['actual_V_actions']['tau'])
J = mat(handles['actual_V_actions']['c'])
Tp = J*T*J
H = mat(handles['residual_handle_actions']['tau'])
HJ = mat(handles['residual_handle_actions']['c'])
AE = T[:2, :2]
CE = J[:2, :2]
R = s.Matrix([[0,-1],[1,-1]])
S = s.Matrix([[0,-1],[1,0]])
Sinv = S.inv()
j = mat(handles['V_basis_with_j'])[:, :2]
p = s.eye(10)[:2, :]
U = j[2:, :]
assert p*j == 3*s.eye(2)
assert T*j == j*AE and J*j == j*CE

# Independently evaluate the literal two-line function in every retained
# tangent, using the exact cubic expansions rather than copied values.
zeta = QZ(0,1)
labels = ['C0','A0','A1','A2','B0','B1','B2','C1','C2']
def leading(line, label):
    a,b,c = line
    zz = zeta**int(label[1])
    terms = {'A': [(0,c-b*zz),(1,a),(3,-b*zz/3)],
             'B': [(0,c-a*zz),(1,b),(3,-a*zz/3)],
             'C': [(0,a-b*zz),(1,c),(3,-b*zz/3)]}[label[0]]
    return next((n,v) for n,v in terms if v)

numerator = (QZ(0),QZ(1),QZ(1))
denominator = (QZ(1),QZ(1),QZ(0))
frames = []
for label, old in zip(labels, units['normalized_units'][1]['frames']):
    rn,an = leading(numerator,label)
    rd,ad = leading(denominator,label)
    order, value = rn-rd, an/(3*ad)
    assert order == old['order'] and value.key() == old['leading']
    boundary = zeta**order
    assert boundary == 1
    frames.append({'cusp':label,'order':order,'leading':value.key(),
                   'symbol_tame_boundary':boundary.key()})
assert sum(leading(numerator,d)[0] for d in labels) == 3
assert sum(leading(denominator,d)[0] for d in labels) == 3
assert [d['order'] for d in frames] == [-3,3,0,0,0,0,0,0,0]
assert frames[0]['leading'] == ['1','0']

l = mat(handles['V_basis_inverse'])[3,:]
t = s.zeros(1,10); t[0,2] = 1
u = s.Matrix([[0,1]])
assert l == s.Matrix([[0,1,3,0,0,0,0,0,0,0]])
assert l*j == s.zeros(1,2)
assert l-3*t == u*p
assert l*T == 7*l and l*J == -l and t*J == -t

# The exact cup/cross comparison.  If B_t(n,g)=t(v_n), then its
# differential is dt_g(A_g v_n').  Thus cup(zeta,f)=cross(beta-dt)+dB_t.
# Verify the arbitrary CM formula after multiplying by the invertible A.
a,b = s.symbols('a b')
A = (1+3*a)*s.eye(2)+3*b*R
q = s.expand(A.det())
AV = s.zeros(10)
AV[:2,:2] = A
AV[2:,2:] = q*s.eye(8)
AV[2:,:2] = U*(A-q*s.eye(2))/3
assert all(s.expand(x).is_polynomial(a,b) for x in AV)
assert all(s.expand(x)==0 for x in l*AV-q*l)
kappa = s.expand((q-1)/3)
three_beta_times_A = s.expand(3*kappa)*l*AV-3*q*q*t+3*t*AV
three_reg_times_A = q*q*u*p-u*p*AV
assert all(s.expand(x)==0 for x in three_beta_times_A-three_reg_times_A)

records=[]
F4 = s.zeros(10)
F4[:2,:2] = -2*s.eye(2)
F4[2:,2:] = 4*s.eye(8)
F4[2:,:2] = -2*U
for name,M,chi in [('tau',T,7),('tau_prime',Tp,7),('Frob_K_2',F4,4)]:
    beta = s.Rational(chi-1,3)*l
    dt = chi**2*t*M.inv()-t
    corrected = beta-dt
    proper = corrected[:,:2]
    assert corrected == proper*p
    assert 3*proper == chi**2*u*M[:2,:2].inv()-u
    transported = R*Sinv*proper.T
    records.append({'element':name,'actual_V_matrix':enc(M),
                    'kappa_zeta':str(s.Rational(chi-1,3)),
                    'raw_cross_beta':enc(beta),'peripheral_boundary_dt':enc(dt),
                    'proper_regulator':enc(proper),
                    'residual_handle_coordinates_at_Weil_unit_1':enc(transported)})
assert records[0]['proper_regulator'] == [['-7','2']]
k = s.Matrix([-7,-5])
hp = s.Matrix([0,1])
assert R*Sinv*u.T == hp
assert s.Matrix(records[0]['residual_handle_coordinates_at_Weil_unit_1']) == k
assert s.Matrix(records[1]['residual_handle_coordinates_at_Weil_unit_1']) == HJ*k
assert s.Matrix(records[2]['residual_handle_coordinates_at_Weil_unit_1']) == -3*hp
assert (H-s.eye(2))*hp == 3*k and HJ*hp == hp

# Exact Q/K twist square, written in columns for the proper dual.
dualT = 49*AE.inv().T
dualC = CE.inv().T
Kmap = R*Sinv
assert H*Kmap == Kmap*dualT
assert HJ*Kmap == Kmap*(-dualC)
assert Kmap.det()==1 and Kmap*Kmap.inv()==s.eye(2)
assert S*(7*AE) == dualT*S
assert (-CE)*Sinv == Sinv*dualC
assert R*CE*R.inv() == HJ  # Tate(1) and chi_K both contribute -1 at c.

# Integral torsion coordinate and inverse, including the unassigned full
# Weil-pairing unit omega in 1+3Z3.  Only its mod3 value is fixed by E37.
coordinates = s.Matrix([[5,-7],[2,-3]])
inverse = s.Matrix([[3,-7],[2,-5]])
assert coordinates*inverse == inverse*coordinates == s.eye(2)
assert coordinates*k == s.Matrix([0,1])
assert coordinates*(H-s.eye(2))*hp == s.Matrix([0,3])
z = s.Symbol('z')
omega = 1+3*z
carry = -z/(1+3*z)
assert s.simplify(carry-(1/omega-1)/3)==0
assert all(s.simplify(v)==0 for v in k/omega-k-(H-s.eye(2))*(carry*hp))
assert all(s.simplify(v)==0 for v in HJ*(carry*hp)-carry*hp)
weil_tests=0
for n in range(1,7):
    modulus=3**n
    for zi in range(3**(n-1)):
        oi=1+3*zi; oi_inv=pow(oi,-1,modulus)
        ci=(-zi*oi_inv)%modulus
        left=(oi_inv-1)*k-(H-s.eye(2))*(ci*hp)
        assert all(int(v)%modulus==0 for v in left)
        assert (int((coordinates*(oi_inv*k))[1])-1)%3==0
        weil_tests+=1

# The marked residual class survives the full integral central IA module.
# Recheck the retained primitive obstruction instead of assuming it from
# the abstract rank-two cohomology calculation.
D = [mat(v).row_join(s.zeros(45,8)) for v in handles['residual_handle_basis']]
assert D[1][19,0] == -2
assert mat(gauge['rational_c_fixed_primitive']) == D[1]/3
assert mat(gauge['torsion_normalized_cocycle_tau']) == -7*D[0]-5*D[1]
assert mat(gauge['determinant_line'])[19] == 0

# Actual filling maps to the two conjugate three-punctured elliptic curves.
# The original O-tangent is retained; only the other six punctures are filled.
pairs=list(combinations(range(10),2))
smallpairs=list(combinations(range(4),2))
def wedge_rect(Q):
    return s.Matrix([[Q[i,a]*Q[j,b]-Q[i,b]*Q[j,a]
                      for a,b in pairs] for i,j in smallpairs])
selectors=[]; probes=[]; filled_actions=[]
for label,cols in [('O_A0_A1',[0,1,2,3]),('O_A0_A2',[0,1,2,4])]:
    Q=s.eye(10)[cols,:]
    I=s.eye(10)[:,cols]
    Q2=wedge_rect(Q)
    Td=Q*T*I
    assert Q*T==Td*Q
    image=[Q2*d*I for d in D]
    # Only the last exterior coordinate, e_A0 wedge e_Aj, can survive.
    assert all(v[:5,:] == s.zeros(5,4) and v[:,2:] == s.zeros(6,2) for v in image)
    probe=s.Matrix.hstack(*[v[5,:2].T for v in image])
    assert probe.det()==1
    assert probe*H == dualT*probe
    selectors.append(Q); probes.append(probe); filled_actions.append(Td)
J21=selectors[1]*J*selectors[0].T
J12=selectors[0]*J*selectors[1].T
assert selectors[1]*J == J21*selectors[0]
assert selectors[0]*J == J12*selectors[1]
assert J21*J12 == J12*J21 == s.eye(4)
assert probes == [S,s.Matrix([[1,-1],[0,1]])]
assert probes[1]*HJ == dualC*probes[0]
assert probes[0]*HJ == dualC*probes[1]

out={
 'status':'PASS',
 'scope':'an actual Tor symbol represents the residual C3 class; no coefficient of the unknown intrinsic arithmetic action is assigned',
 'input_sha256':{name:hashlib.sha256((base/name).read_bytes()).hexdigest() for name in input_names},
 'literal_symbol':'{zeta3,(y+z)/(3(x+y))}',
 'all9_frames_and_tame_boundaries':frames,
 'no_other_horizontal_boundary':'both literal lines have total cusp intersection multiplicity three',
 'unit_character':enc(l),'peripheral_primitive_t':enc(t),
 'proper_bockstein_numerator_u':enc(u),
 'actual_filling_p':enc(p),'actual_j':enc(j),'p_j':enc(p*j),
 'full_cochain_identity':'cup(zeta3,f_A0)=Inf(cross(beta-dt))+d(B_t), B_t(n,g)=t(v_n)',
 'proper_identity':'beta-dt=p^*(d(u/3)); 3(beta-dt)=p^*du',
 'arbitrary_CM_polynomial_identity_verified':True,
 'actual_elements':records,
 'Q_K_twist_square':{'proper_dual_tau':enc(dualT),'proper_dual_c':enc(dualC),
    'anti_twisted_c':enc(-dualC),'residual_tau':enc(H),'residual_c':enc(HJ),
    'map_R_S_inverse':enc(Kmap),'inverse':enc(Kmap.inv()),
    'symbol_conjugation':'c(zeta3)=zeta3^-1 and c(f_A0)=f_A0, so c(Xi_Tor)=-Xi_Tor'},
 'Weil_marking':{'mod3_pairing':'e3(A0,A2)=zeta3',
    'full_pairing_matrix':'omega*S, omega in 1+3 Z3; omega is retained, not assigned',
    'S':enc(S),'S_inverse':enc(Sinv),'R':enc(R),'R_inverse':enc(R.inv()),
    'exact_coboundary':'k/omega-k=d(((omega^-1-1)/3)h_plus)',
    'finite_carry_tests':weil_tests},
 'residual_cohomology':{'c_fixed_basis':enc(hp),'relation_column':enc(3*k),
    'coordinates_free_and_mod3':enc(coordinates),'inverse':enc(inverse),
    'Tor_generator_tau':enc(k),'Tor_generator_coordinates':[0,1],
    'bockstein_point':'h_plus/3 mod H; under R^-1 this is A0 tensor zeta3 in H/3 with the chi_K twist',
    'exact_order':3,'local_Frob4_value':enc(-3*hp),'local_Frob4_quotient_modulus':9},
 'full_IA_nonintegrality_witness':gauge['nonintegrality_witness'],
 'conjugate_three_puncture_maps':{
    'curves':['E minus {O,A0,A1}','E minus {O,A0,A2}'],
    'abelian_filling_matrices':[enc(Q) for Q in selectors],
    'exterior_filling_matrices':[enc(wedge_rect(Q)) for Q in selectors],
    'actual_tau_matrices':[enc(A) for A in filled_actions],
    'c_from_first_to_second':enc(J21),'c_from_second_to_first':enc(J12),
    'residual_to_handle_commutator_maps':[enc(P) for P in probes],
    'inverse_maps':[enc(P.inv()) for P in probes],
    'all_integral_intertwining_squares_verified':True},
 'primary_source':{'url':'https://arxiv.org/pdf/alg-geom/9508008',
    'location':'Theorems 3.7-3.8 and proof, printed pages 14-15, equation (21)',
    'used_scope':'the constant-symbol Tor construction; the arithmetic nonzero C3 regulator is proved by the displayed cochains, not imported from rational descent'}
}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS literal {zeta3,f_A0}: all nine tangent frames and all tame boundaries.')
print('PASS exact proper cochain beta-dt, arbitrary CM polynomial identity, and actual tau/tau-prime/Frob4 values.')
print('PASS Q/K twist and Weil/R inverse maps; full Weil-unit carry retained in',weil_tests,'finite tests.')
print('PASS residual generator (0,1) in Z3 plus C3 and its full-IA nonintegrality witness.')
print('PASS both actual conjugate three-puncture filling maps and unimodular residual inverses.')
