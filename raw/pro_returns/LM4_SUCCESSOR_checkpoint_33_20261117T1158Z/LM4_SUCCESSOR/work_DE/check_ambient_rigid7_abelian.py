"""Integral ambient H1 test for the twelve rigid-seven forgetful maps.

For the sphere pure mapping class group P_{0,n}, normalize three labels
a,b,c to infinity,0,1.  Its integral H1 has rank n(n-3)/2, with basis
given by the pair linkings of the n-1 finite normalized coordinates,
omitting the fixed pair(b,c).  A target pair-linking covector in the
original unordered-pair variables is
 e_ca-e_cb+e_ba+e_ij-e_ia-e_ja.
The explicit integral matrix below therefore computes the actual
forgetful maps, not the sphere braid group with its central Z/2.
"""
from pathlib import Path
import itertools,json,time
import sympy as s
from sympy.matrices.normalforms import smith_normal_form,hermite_normal_form

HERE=Path(__file__).resolve().parent
raw=json.loads((HERE/'rigid7_subsets.json').read_text())
subsets=raw['rigid7']
assert len(subsets)==12 and len({tuple(S) for S in subsets})==12
assert all(len(S)==7 and len(set(S))==7 for S in subsets)
labels=list(range(1,13));pairs=list(itertools.combinations(labels,2))
index={p:i for i,p in enumerate(pairs)}

def linking_covector(a,b,c,i,j):
    assert len({a,b,c})==3 and i!=j and a not in (i,j)
    row=[0]*len(pairs)
    for p,coefficient in [((c,a),1),((c,b),-1),((b,a),1),
                          ((i,j),1),((i,a),-1),((j,a),-1)]:
        assert p[0]!=p[1]
        row[index[tuple(sorted(p))]]+=coefficient
    return row

# Ambient integral coordinates: infinity=2,zero=4,one=6.
ambient_pairs=[p for p in pairs if 2 not in p and p!=(4,6)]
assert len(ambient_pairs)==54
ambient_indices=[index[p] for p in ambient_pairs]
A=s.Matrix([linking_covector(2,4,6,*p) for p in ambient_pairs])
assert A[:,ambient_indices]==s.eye(54)
vertex=s.Matrix([[int(i in pair) for pair in pairs] for i in labels])
assert A*vertex.T==s.zeros(54,12)
assert A*s.ones(66,1)==s.zeros(54,1)
rows=[];names=[]
for subset in subsets:
    a,b,c=subset[:3]
    finite=[i for i in subset if i!=a]
    for pair in itertools.combinations(finite,2):
        if pair==(b,c):continue
        rows.append(linking_covector(a,b,c,*pair))
        names.append({'subset':subset,'normalization':[a,b,c],'pair':list(pair)})
R=s.Matrix(rows)
assert R.shape==(168,66)
assert R*vertex.T==s.zeros(168,12)
M=R[:,ambient_indices]
assert M*A==R
start=time.time()
rank=M.rank()
print('Twelve rigid-seven subsets,14 target H1 coordinates each: PASS')
print('Ambient H1 basis uses54 normalized pair linkings (actual pure mapping classes): PASS')
print('Every target covector annihilates the twelve sphere vertex relations: PASS')
print('Exact change of coordinates M*A=R: PASS')
print('Ambient combined forgetful matrix shape:',M.shape)
print('Exact rational rank:',rank)
assert rank==54
S=smith_normal_form(M,domain=s.ZZ)
invariants=[abs(int(S[i,i])) for i in range(54)]
print('Smith invariant factors:',invariants)
assert invariants==[1]*54
H=hermite_normal_form(M.T)
assert H==s.eye(54)
print('Independent row-lattice Hermite check gives identity54: PASS')

# A square nonsingular minor is an additional small determinant witness.
_,independent_rows=M.T.rref()
assert len(independent_rows)==54
B=M[list(independent_rows),:]
det=int(B.det())
assert det!=0
print('First rationally independent54-row minor determinant:',det)
assert abs(det)==1
inverse=B.inv()
assert all(v.q==1 for v in inverse)
integer_B=[[int(x) for x in B.row(i)] for i in range(54)]
integer_inverse=[[int(x) for x in inverse.row(i)] for i in range(54)]
assert all(sum(integer_inverse[i][k]*integer_B[k][j] for k in range(54))
           ==int(i==j) for i in range(54) for j in range(54))
print('Independent integer arithmetic verifies the supplied54-by54 inverse: PASS')
print('Conclusion: split integral injection, and injection after reduction modulo every m.')
out={
 'description':__doc__,
 'ambient_normalization':[2,4,6],
 'ambient_pair_basis':[list(p) for p in ambient_pairs],
 'sphere_pair_variables':[list(p) for p in pairs],
 'ambient_covector_matrix':[[int(x) for x in A.row(i)] for i in range(A.rows)],
 'target_rows':names,
 'forgetful_matrix':[[int(x) for x in M.row(i)] for i in range(M.rows)],
 'rational_rank':rank,
 'smith_invariant_factors':invariants,
 'transpose_row_lattice_Hermite_form':'identity54',
 'independent_row_indices':list(independent_rows),
 'minor_determinant':det,
 'unimodular_minor_inverse':integer_inverse,
 'scope':'H1 and its completions only; neither injectivity on nonabelian groups nor triviality of K follows.'}
(HERE/'ambient_rigid7_abelian_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('ALL EXACT CHECKS PASS; elapsed seconds',round(time.time()-start,3))
