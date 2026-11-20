"""Exact block-matrix checks prompted by 123/020; no source text recognition."""
from pathlib import Path
import json
import sympy as s

def block(d):
    m=d-1
    E=s.zeros(d);F=s.zeros(d);H=s.diag(*[m-2*j for j in range(d)])
    for j in range(1,d):E[j-1,j]=j
    for j in range(d-1):F[j+1,j]=m-j
    return E,F,H

def centralizer_dimension(matrices,trace_zero=False):
    n=matrices[0].rows
    columns=[]
    for i in range(n):
        for j in range(n):
            X=s.zeros(n);X[i,j]=1
            c=[]
            for M in matrices:c.extend(list(X*M-M*X))
            if trace_zero:c.append(s.trace(X))
            columns.append(s.Matrix(c))
    A=s.Matrix.hstack(*columns)
    return n*n-A.rank()

out={'scope':'Explicit polynomial SL2 representations in characteristic zero. No orbit classification or identification of the source blank is asserted.','examples':[]}
for p in [(3,),(2,1),(4,),(3,1),(2,2),(5,),(4,1)]:
    B=[block(d) for d in p]
    E,F,H=[s.diag(*[b[i] for b in B]) for i in range(3)]
    n=sum(p)
    assert H*E-E*H==2*E and H*F-F*H==-2*F and E*F-F*E==H
    weights=[int(H[i,i]) for i in range(n)]
    multiplicities=[weights.count(w) for w in sorted(set(weights),reverse=True)]
    g1=sum(a-b==1 for a in weights for b in weights)
    nilindex=next(q for q in range(1,n+1) if E**q==s.zeros(n))
    centE=centralizer_dimension([E],True)
    centTriple=centralizer_dimension([E,F,H],True)
    row={'partition':list(p),'weights':sorted(weights,reverse=True),
         'ordered_weight_multiplicities':multiplicities,'full_flag':all(m==1 for m in multiplicities),
         'g1_dimension':g1,'nilpotency_index':nilindex,
         'centralizer_E_in_sl_dimension':centE,'conjugacy_orbit_dimension_in_sl':n*n-1-centE,
         'centralizer_triple_in_sl_dimension':centTriple,'sl2_relations_verified':True}
    out['examples'].append(row)
by={tuple(r['partition']):r for r in out['examples']}
assert by[(2,1)]['full_flag'] and by[(4,1)]['full_flag']
assert not by[(3,1)]['full_flag']
assert by[(2,2)]['g1_dimension']==0 and by[(2,2)]['nilpotency_index']==2
assert by[(3,1)]['g1_dimension']==0 and by[(3,1)]['nilpotency_index']==3
for n in [3,5]:
    regular=by[(n,)];subregular=by[(n-1,1)]
    assert regular['conjugacy_orbit_dimension_in_sl']-subregular['conjugacy_orbit_dimension_in_sl']==2
E,F,H=block(2)
minusI=-s.eye(2)
assert minusI.det()==1 and minusI!=s.eye(2)
assert all(minusI*M==M*minusI for M in [E,F,H])
out['SL2_central_element']={'matrix':[[-1,0],[0,-1]],'determinant':1,'distinct_from_identity_in_characteristic_zero':True,'commutes_with_every_matrix':True}
out['interpretations']={
 'conditional_blank_counterexample':'If the blank is interpreted as g, the condition g(1)=0 does not characterize a regular/principal block: partitions (2,2) and (3,1) in dimension 4 have g(1)=0 but smaller nilpotency index than (4). The blank remains blank.',
 'Borel_examples':'Distinct weights for (2,1) in SL3 and (4,1) in SL5 give full flags; their nilpotency indices are n-1 rather than n, and their conjugacy orbit dimensions are two below the regular block.',
 'unit_stabilizer_counterexample':'For the identity SL2 homomorphism into G=SL2, -I is a nontrivial centralizer element. Thus the unit-stabilizer and G-torsor statements require a hypothesis or modification beyond semisimple characteristic-zero G.',
 'adjoint_type_A_refinement':'For a single irreducible block, commuting with the distinct-weight diagonal and the consecutive nonzero E entries forces a matrix to be scalar. In SL_n this leaves mu_n; after quotienting scalars it is trivial.'
}
dest=Path(__file__).resolve().parents[1]/'math_checks/123_020_type_a_certificate.json'
dest.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
