"""Restrict the exact six-dimensional degree-two test kernel to A5 invariants.

This uses only labelled permutation actions on the degree-one/degree-two
pure sphere braid Lie algebra. Inner pure corrections act trivially on
these graded quotients. No averaging by the order60 is used.
"""
from pathlib import Path
import itertools,json,time
import sympy as s
from sympy.matrices.normalforms import smith_normal_form

HERE=Path(__file__).resolve().parent
h1=json.loads((HERE/'ambient_rigid7_abelian_certificate.json').read_text())
data=json.loads((HERE/'ambient_rigid7_class2_certificate.json').read_text())
geom=json.loads((HERE/'rigid7_subsets.json').read_text())
A=s.Matrix(h1['ambient_covector_matrix'])
pairs=[tuple(p) for p in h1['sphere_pair_variables']]
pair_indices={p:i for i,p in enumerate(pairs)}
ambient_pairs=[tuple(p) for p in h1['ambient_pair_basis']]
ambient_index={p:i for i,p in enumerate(ambient_pairs)}
finite=[i for i in range(1,13) if i!=2]
triples=[tuple(T) for T in data['source_triples']]
C=s.Matrix(data['degree_two_matrix'])
N=s.Matrix([[s.Rational(x) for x in row] for row in data['rational_kernel_basis']]).T
assert N.shape==(165,6) and C*N==s.zeros(240,6)
assert all(x.q==1 for x in N)
_,pivot_rows=N.T.rref();assert len(pivot_rows)==6
PN=N[list(pivot_rows),:]
assert abs(PN.det())==1
left=PN.inv()
assert all(x.q==1 for x in left)

def compose(p,q):return tuple(p[q[i]] for i in range(len(p)))
def closure(gens):
    identity=tuple(range(12));seen={identity};todo=[identity]
    while todo:
        x=todo.pop()
        for g in gens:
            y=compose(x,g)
            if y not in seen:seen.add(y);todo.append(y)
    return seen
gens=[tuple(geom['T_permutations'][1]),tuple(geom['T_permutations'][3]),
      tuple(geom['D_permutation'])]
group=closure(gens);assert len(group)==60
assert len(closure(gens[:2]))==12

def first_action(permutation):
    columns=[pair_indices[tuple(sorted((permutation[i-1]+1,permutation[j-1]+1)))]
             for i,j in ambient_pairs]
    return A[:,columns]

def gen_image(pair,D):
    if pair==(4,6):return [-sum(D.row(i)) for i in range(54)]
    return list(D.col(ambient_index[pair]))
def bracket(v,w):
    def get(vector,p):return vector[ambient_index[p]] if p in ambient_index else 0
    result=[]
    for i,j,k in triples:
        a,b,c=(i,j),(i,k),(j,k)
        va,vb,vc=(get(v,p) for p in (a,b,c))
        wa,wb,wc=(get(w,p) for p in (a,b,c))
        result.append(va*wb-vb*wa-va*wc+vc*wa+vb*wc-vc*wb)
    return result
def second_action(permutation):
    D=first_action(permutation)
    return s.Matrix([bracket(gen_image((i,j),D),gen_image((i,k),D))
                     for i,j,k in triples]).T

start=time.time();actions=[]
for i,g in enumerate(gens):
    G=second_action(g)
    GN=G*N
    Q=left*GN[list(pivot_rows),:]
    assert all(x.q==1 for x in Q) and N*Q==GN
    actions.append(Q)
    print('Generator',i+1,'six-dimensional kernel action:')
    print(Q)
assert actions[0]**2==s.eye(6)
assert actions[1]**3==s.eye(6)
assert actions[2]**5==s.eye(6)
F=s.Matrix.vstack(*[Q-s.eye(6) for Q in actions])
rank=F.rank()
smith=smith_normal_form(F,domain=s.ZZ)
invariants=[abs(int(smith[i,i])) for i in range(6)]
print('Geometric generators produce A5order60 and Torder12: PASS')
print('Kernel basis is primitive; every action preserves it integrally: PASS')
print('Fixed-equation matrix rank:',rank)
print('Fixed-equation Smith factors:',invariants)
assert rank==5 and invariants==[1,1,1,1,1,0]
fixed=F.nullspace();assert len(fixed)==1
v=fixed[0]
denominator=s.ilcm(*[x.q for x in v]);v=v*denominator
divisor=s.igcd(*[int(x) for x in v]);v=v/divisor
assert all(x.q==1 for x in v) and F*v==s.zeros(18,1)
full=N*v
assert all(x.q==1 for x in full)
assert s.igcd(*[int(x) for x in full])==1
unit_positions=[i for i,x in enumerate(full) if abs(x)==1]
assert unit_positions
assert C*full==s.zeros(240,1)
for Q in actions:assert Q*v==v
print('Primitive fixed vector in the6-dimensional kernel basis:',list(v))
print('Nonzero ambient triple coefficients:')
for T,x in zip(triples,full):
    if x:print(T,int(x))
print('Primitive ambient fixed vector has',len([x for x in full if x]),'nonzero entries.')
print('Conclusion: completed invariant test kernel is exactly one primitive Zhat direction.')
record={
 'description':__doc__,
 'A5_generating_permutations_zero_based':[list(g) for g in gens],
 'kernel_basis':[[int(x) for x in N.col(i)] for i in range(6)],
 'primitive_kernel_minor_rows':list(pivot_rows),
 'primitive_kernel_minor_inverse':[[int(x) for x in left.row(i)] for i in range(6)],
 'generator_actions_on_kernel':[[[int(x) for x in Q.row(i)] for i in range(6)] for Q in actions],
 'fixed_equation_matrix':[[int(x) for x in F.row(i)] for i in range(F.rows)],
 'fixed_rank':rank,'fixed_smith_factors':invariants,
 'primitive_fixed_vector_in_kernel_basis':[int(x) for x in v],
 'primitive_fixed_vector_ambient':[int(x) for x in full],
 'ambient_unit_coordinate':unit_positions[0],
 'ambient_nonzero_terms':[{'triple':list(T),'coefficient':int(x)}
                          for T,x in zip(triples,full) if x],
 'scope':'The completed A5-invariant test kernel is a primitive rank-one Zhat module, including primes2,3,5. Whether the actual K realizes a nonzero element of that line remains open.'}
(HERE/'rigid7_class2_invariants_certificate.json').write_text(json.dumps(record,indent=2)+'\n')
print('ALL EXACT CHECKS PASS; elapsed seconds',round(time.time()-start,3))
