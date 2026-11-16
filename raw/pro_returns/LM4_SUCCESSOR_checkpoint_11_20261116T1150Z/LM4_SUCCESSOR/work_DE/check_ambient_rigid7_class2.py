"""Exact degree-two lower-central map of the twelve rigid-seven forgettings.

For PB_m modulo its central full twist, gr_2 has the integral basis
t_ijk=[A_ij,A_ik], i<j<k.  The degree-two braid relations give
[A_ij,A_jk]=-t_ijk and [A_ik,A_jk]=t_ijk, with disjoint pairs commuting.
The map is calculated from the exact integral degree-one matrix of B.58.
"""
from pathlib import Path
import itertools,json,time
import sympy as s
from sympy.matrices.normalforms import smith_normal_form,hermite_normal_form

HERE=Path(__file__).resolve().parent
d=json.loads((HERE/'ambient_rigid7_abelian_certificate.json').read_text())
M=s.Matrix(d['forgetful_matrix'])
ambient_pairs=[tuple(p) for p in d['ambient_pair_basis']]
ambient_labels=[j for j in range(1,13) if j!=2]
source_triples=list(itertools.combinations(ambient_labels,3))
assert len(source_triples)==165
pair_to_column={p:j for j,p in enumerate(ambient_pairs)}

def generator_image(pair,matrix):
    if pair==(4,6):return [-sum(matrix.row(i)) for i in range(matrix.rows)]
    return list(matrix.col(pair_to_column[pair]))

def bracket(v,w,finite,target_pairs):
    target_indices={p:j for j,p in enumerate(target_pairs)}
    def get(vector,p):
        return vector[target_indices[p]] if p in target_indices else 0
    result=[]
    for i,j,k in itertools.combinations(finite,3):
        a,b,c=(i,j),(i,k),(j,k)
        va,vb,vc=(get(v,p) for p in (a,b,c))
        wa,wb,wc=(get(w,p) for p in (a,b,c))
        result.append(va*wb-vb*wa-va*wc+vc*wa+vb*wc-vc*wb)
    return result

# Check the chosen basis and the omitted central pair on the identity map.
identity=s.eye(54)
cols=[]
for i,j,k in source_triples:
    cols.append(bracket(generator_image((i,j),identity),
                        generator_image((i,k),identity),
                        ambient_labels,ambient_pairs))
assert s.Matrix(cols).T==s.eye(165)
print('Degree-two basis and full-twist quotient verified on the identity map: PASS',flush=True)

blocks=[];target_names=[]
for block in range(12):
    rows=d['target_rows'][14*block:14*(block+1)]
    subset=rows[0]['subset'];a,b,c=rows[0]['normalization']
    finite=[x for x in subset if x!=a]
    target_pairs=[tuple(x['pair']) for x in rows]
    assert len(finite)==6 and len(target_pairs)==14
    D=M[14*block:14*(block+1),:]
    columns=[]
    for i,j,k in source_triples:
        columns.append(bracket(generator_image((i,j),D),
                               generator_image((i,k),D),finite,target_pairs))
    blockmatrix=s.Matrix(columns).T
    assert blockmatrix.shape==(20,165)
    blocks.append(blockmatrix)
    target_names += [{'subset':subset,'triple':list(T)}
                     for T in itertools.combinations(finite,3)]
C=s.Matrix.vstack(*blocks)
assert C.shape==(240,165)
start=time.time()
rank=C.rank()
print('Combined degree-two matrix shape:',C.shape,flush=True)
print('Exact rational rank:',rank,flush=True)
S=smith_normal_form(C,domain=s.ZZ)
invariants=[abs(int(S[i,i])) for i in range(min(C.shape))]
print('Nonzero Smith factors:',[x for x in invariants if x],flush=True)
print('Number of zero Smith factors:',invariants.count(0),flush=True)
_,independent_rows=C.T.rref()
selected=list(independent_rows)
record={'description':__doc__,
        'source_triples':[list(T) for T in source_triples],
        'target_rows':target_names,
        'degree_two_matrix':[[int(x) for x in C.row(i)] for i in range(C.rows)],
        'rank':rank,'smith_invariants':invariants,
        'independent_row_indices':selected}
if rank==165:
    H=hermite_normal_form(C.T)
    assert H==s.eye(165)
    B=C[selected,:]
    determinant=int(B.det())
    record['minor_determinant']=determinant
    print('First165 independent-row minor determinant:',determinant,flush=True)
    if abs(determinant)==1:
        inverse=B.inv();assert all(v.q==1 for v in inverse)
        inv=[[int(x) for x in inverse.row(i)] for i in range(165)]
        bb=[[int(x) for x in B.row(i)] for i in range(165)]
        # Sparse multiplication in ordinary Python integers.
        for i,row in enumerate(inv):
            nonzero=[(k,a) for k,a in enumerate(row) if a]
            assert all(sum(a*bb[k][j] for k,a in nonzero)==int(i==j)
                       for j in range(165))
        record['unimodular_minor_inverse']=inv
        print('Supplied integer inverse independently checked: PASS',flush=True)
    print('Conclusion: split integral injection on degree-two lower central quotients.',flush=True)
else:
    null=C.nullspace()
    record['rational_kernel_basis']=[[str(x) for x in v] for v in null]
    _,pivot_columns=C.rref()
    B=C[selected,list(pivot_columns)]
    determinant=int(B.det())
    assert determinant==-1
    inverse=B.inv(method='DM')
    assert all(x.q==1 for x in inverse)
    assert B*inverse==s.eye(rank) and inverse*B==s.eye(rank)
    record['rank_minor_rows']=selected
    record['rank_minor_columns']=list(pivot_columns)
    record['rank_minor_determinant']=determinant
    record['rank_minor_inverse']=[[int(x) for x in inverse.row(i)] for i in range(rank)]
    print('Certified159x159 minor determinant:',determinant,flush=True)
    print('Supplied integer minor inverse checked in both orders: PASS',flush=True)
    print('Conclusion: ambient degree-two detection fails; retain precise kernel.',flush=True)
(HERE/'ambient_rigid7_class2_certificate.json').write_text(json.dumps(record,indent=2)+'\n')
print('ALL EXACT CHECKS PASS; elapsed seconds',round(time.time()-start,3),flush=True)
