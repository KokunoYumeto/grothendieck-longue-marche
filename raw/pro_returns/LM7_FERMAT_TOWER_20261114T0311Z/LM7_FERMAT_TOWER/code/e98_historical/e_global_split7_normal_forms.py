"""Exact cusp-lattice tests, complete mod-nine image, and all anti-fixed layer ranks."""
from pathlib import Path
from itertools import combinations, product
from collections import Counter
import hashlib
import importlib.util
import json
import sympy as s
from sympy.matrices.normalforms import hermite_normal_form

HERE = Path(__file__).resolve().parent
BASE = HERE.parents[1] / 'LM7_FERMAT_TOWER/code'
def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
smith = load('e98_smith_normal_forms', BASE / 'e_cusp_local_smith.py')
horizontal = load('e98_horizontal_kernel', BASE / 'a_horizontal_full.py')
mat = lambda rows: s.Matrix([[s.Rational(x) for x in row] for row in rows])
enc = lambda A: [[str(x) for x in row] for row in A.tolist()]
integral = lambda A: all(s.Rational(x).q % 3 for x in A)
read = lambda name: json.loads((BASE / name).read_text())
data = json.loads((HERE / 'e_global_split7_explore.json').read_text())
residues = json.loads((HERE / 'e_global_split7_residues.json').read_text())
layers = read('e_wild_layers.json')['layers']
T, J = (s.Matrix(layers['1'][key]) for key in ['input_tau', 'input_c'])
paths = read('a_cusp_kummer.json')['c_equivariant_cusp_tau_Kummer']
labels = ['A0', 'A1', 'A2', 'B0', 'B1', 'B2', 'C1', 'C2']
E = s.eye(10)
pairs = list(combinations(range(10), 2))
wedge = lambda a,b: s.Matrix([a[i]*b[j]-a[j]*b[i] for i,j in pairs])
ext = lambda A: s.Matrix([[A[i,k]*A[j,l]-A[i,l]*A[j,k]
                          for k,l in pairs] for i,j in pairs])
Q, S, D, Di = (mat(data[key]) for key in
              ['quotient_map', 'quotient_section', 'local_matrix', 'local_inverse'])
w = s.Matrix(data['primitive_w'])
assert Q*S == s.eye(44) and Q*w == s.zeros(44, 1)
assert D*Di == Di*D == s.eye(44)
keep_rows = list(range(1, 45))
B, J2 = ext(T), ext(J)
assert B*w == 7*w and J2*w == -w
differential = B/7-s.eye(45)
R1 = mat(data['horizontal_representative'])
G = (s.eye(10)-T)*(s.eye(10)+J)
assert G.rank() == 4
moduli = data['moduli']
coefficients = [mat(data['coefficient_blocks'][d]) for d in labels]
def residue(value, modulus):
    value = s.Rational(value)
    assert value.q % 3
    return int(value.p)*pow(int(value.q), -1, modulus) % modulus
def correction(U, v):
    defect = sum((v[j]*wedge(U-s.Matrix(paths[d]), E[:,j+2])
                  for j,d in enumerate(labels)), s.zeros(45,1))
    assert defect[0] == 0
    c = -S*Di*defect.extract(keep_rows,[0])
    assert differential*c == -defect
    return c

# Recover the actual full set, then prove equality with the nine displayed rays.
digits = list(product(range(3), repeat=8))
actual = set()
for record in residues['relative_image']:
    v0 = record['first_digit']
    for index,p in zip(record['admissible_second_digits'],
                       record['all_horizontal_witnesses']):
        v = tuple((a+3*b)%9 for a,b in zip(v0,digits[index]))
        C = sum((v[j]*coefficients[j] for j in range(8)),s.zeros(30,10))
        value = C*s.Matrix([1]+p)
        assert all(residue(value[i],moduli[i])==0 for i in range(30))
        assert integral(correction(R1*s.Matrix(p),v))
        actual.add(v)
rays = {label: [int(i==j) for i in range(8)] for j,label in enumerate(labels)}
rays['O'] = [-1]*8
expected = {tuple(r*a%9 for a in ray) for ray in rays.values() for r in range(9)}
assert actual == expected and len(actual)==73
assert sum(1 for v in actual if all(x%3==0 for x in v)) == 19
print('PASS all73 exact inverse witnesses and equality with all nine cusp rays modulo9',flush=True)

# At every cusp the projected compact wedge remains primitive after filling
# that one toric direction. Retain an explicit unimodular comparison basis.
cusp_records = []
for label,ray in rays.items():
    e = s.Matrix([0,0]+ray)
    change = s.eye(10)
    if label=='O':
        change[:,9]=e
        removed=9
    else:
        removed=2+labels.index(label)
    change_inverse = change.inv()
    assert abs(change.det()) == 1 and integral(change_inverse)
    moved_w = ext(change_inverse)*w
    witness = next(i for i,pair in enumerate(pairs)
                   if removed not in pair and s.Rational(moved_w[i]).p%3)
    assert s.Rational(moved_w[witness]).q%3
    H = (T-s.eye(10)).row_join(e)
    hs = smith.local_smith(H.tolist())
    assert hs['valuations'] == [0]*3+[1]*5+[2]*2 and hs['free_rank']==0
    L, Li, R, Ri, DD = (mat(hs[k]) for k in
                       ['left','left_inverse','right','right_inverse','diagonal_matrix'])
    assert L*H*R==DD and L*Li==Li*L==s.eye(10)
    assert R*Ri==Ri*R==s.eye(11)
    lift = R[:,:10]*s.diag(*[s.Rational(1,3**a) for a in hs['valuations']])*L
    assert H*lift==s.eye(10)
    assert integral(lift*H)
    assert integral(s.diag(*[s.Rational(1,3**a) for a in hs['valuations']])*L*G)
    # The actual inverse differential equals the wedge formula on every
    # generator of this complete local lattice.
    origin = s.zeros(10,1) if label=='O' else s.Matrix(paths[label])
    origin_c = correction(origin,ray)
    assert integral(origin_c)
    for i in range(11):
        shifted=correction(origin+H[:,i],ray)-origin_c
        h=lift*H[:,i]
        assert shifted == -S*Q*wedge(h[:10,:],e)
        assert integral(shifted)
    # Primitive and triple cusp coefficients have horizontal indices 3^9
    # and 3^2 respectively. The first three P1 coordinates have order3.
    finite=L*R1[:,:3]
    torsion=[]
    for multiplier in [1,3]:
        surviving=[]
        for a in product(range(3),repeat=3):
            value=multiplier*finite*s.Matrix(a)
            if all(residue(value[i],3**hs['valuations'][i])==0 for i in range(10)):
                surviving.append(list(a))
        torsion.append(surviving)
    assert len(torsion[0])==1 and len(torsion[1])==27
    cusp_records.append({'cusp':label,'inertia_vector':list(e),
                         'primitive_quotient_basis':enc(change),
                         'primitive_quotient_basis_inverse':enc(change_inverse),
                         'primitive_wedge_witness':{'pair':pairs[witness],
                                                    'coefficient':str(moved_w[witness])},
                         'local_lattice_generators':enc(H),
                         'local_lattice_smith':smith.encode(hs),
                         'exact_lattice_preimage':enc(lift),
                         'cusp_origin_correction':enc(origin_c),
                         'finite_horizontal_kernels':torsion})
print('PASS all nine C3^5 + C9^2 local quotients, primitive wedge maps, and exact lattice inverses',flush=True)

# Intersect every constant and horizontal coefficient condition, without
# enumerating the continuous horizontal input.
universal=s.eye(8)
for row,modulus in enumerate(moduli):
    for coordinate in range(10):
        coefficients_row=s.Matrix([[int(coefficients[d][row,coordinate]) for d in range(8)]])
        universal=hermite_normal_form(universal*horizontal.row_kernel(coefficients_row*universal,modulus))
assert universal==9*s.eye(8)
print('PASS exact universal-inertia Hermite basis 9I8',flush=True)

# The central parameter is the complete fixed-gauge quotient, and the
# primitive w gives the remaining one-dimensional tame kernel.
central=(s.eye(45)-B)*(s.eye(45)+J2)
cs=smith.local_smith(central.tolist())
assert cs['valuations']==[0]*7+[1]*9+[2]*5 and cs['free_rank']==24
assert differential.rank()==44 and differential*w==s.zeros(45,1)
v=9*s.Matrix([1,0,0,1,0,0,0,0])
nonlifting=correction(s.zeros(10,1),v)
assert integral(nonlifting)
assert differential*nonlifting == -sum((v[j]*wedge(-s.Matrix(paths[d]),E[:,j+2])
                                       for j,d in enumerate(labels)),s.zeros(45,1))
assert all(s.Matrix.hstack(v,s.Matrix(ray)).rank()==2 for ray in rays.values())
print('PASS central quotient Z3^24 + C3^9 + C9^5 and literal global nonlifting inertia',flush=True)

# These exact character formulae give all coordinates of the full,
# metabelian and full-to-metabelian anti-fixed spaces.
t=s.Symbol('t')
sym_trace=[s.expand(s.series((1-t)**-4*(1+t)**-6,t,0,15).removeO()).coeff(t,k)
           for k in range(15)]
rank_table=[]
for m in range(1,15):
    full_dim=sum(s.mobius(d)*10**(m//d) for d in s.divisors(m))/m
    full_trace=sum(s.mobius(d)*((-2 if d%2 else 10)**(m//d)) for d in s.divisors(m))/m
    meta_dim=10 if m==1 else (m-1)*s.binomial(m+8,m)
    meta_trace=-2 if m==1 else -2*sym_trace[m-1]-sym_trace[m]
    full_minus=(full_dim-full_trace)/2
    meta_minus=(meta_dim-meta_trace)/2
    fibre_minus=full_minus-meta_minus
    assert all(s.Rational(x).q==1 and x>=0 for x in [full_dim,meta_dim,full_minus,meta_minus,fibre_minus])
    assert m>=4 or fibre_minus==0
    rank_table.append({'degree':m,'full_rank':int(full_dim),'full_trace':int(full_trace),
                       'metabelian_rank':int(meta_dim),'metabelian_trace':int(meta_trace),
                       'full_negative_rank':int(full_minus),
                       'metabelian_negative_rank':int(meta_minus),
                       'comparison_fibre_negative_rank':int(fibre_minus)})
assert rank_table[0]['full_negative_rank']==6
assert rank_table[3]['comparison_fibre_negative_rank']==504
print('PASS all14 integral character rows for the explicit anti-fixed coordinate products',flush=True)
result={'status':'PASS','relative_image_size':73,'exact_cusp_ray_set_equality':True,
        'complete_inverse_witness_count':73,'cusp_local_lattices':cusp_records,
        'universal_inertia_kernel':enc(universal),'central_gauge_smith':smith.encode(cs),
        'fixed_abelian_fibre':{'free_rank':25,'C3':9,'C9':5},
        'fixed_inertia_fibre':{'free_rank':31,'C3_primitive':9,'C3_divisible_by3':12,'C9':5},
        'explicit_nonlifting_class':{'horizontal':[0]*10,'inertia':list(v),
                                     'central_inertia':enc(nonlifting)},
        'negative_layer_ranks':rank_table,
        'input_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in
                       [HERE/'e_global_split7_explore.json',HERE/'e_global_split7_residues.json',
                        BASE/'e_cusp_local_smith.py',BASE/'a_horizontal_full.py',
                        BASE/'e_wild_layers.json',BASE/'a_cusp_kummer.json']}}
(HERE/'e_global_split7_normal_forms.json').write_text(json.dumps(result,indent=2,default=int)+'\n')
print('ALL E98 NORMAL-FORM CHECKS PASS',flush=True)
