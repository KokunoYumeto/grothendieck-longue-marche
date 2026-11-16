"""Actual full rigid-kernel words span the cyclic principal Lie lattice.

All matrices are recomputed from the original common-base eleven-strand
braids.  The only new group-theoretic input is B69's actual kernel word.
No completion of its abstract infinitely generated normal closure is used.
"""
from pathlib import Path
import json
import numpy as np
import sympy as s

HERE=Path(__file__).resolve().parent;BASE=HERE.parent
data=json.loads((BASE/'next_B59_image/common_base_braid_words.json').read_text())
old=json.loads((BASE/'next_finite_symplectic/matrices.json').read_text())
J=np.array(old['integral_symplectic_form'],dtype=np.int64)
Ji=np.array(s.Matrix(J).inv(),dtype=np.int64)
n=10;mod=9;p=3;I=np.eye(n,dtype=np.int64)
bg={}
for i in range(1,11):
    U=np.eye(11,dtype=np.int64)
    U[i-1:i+1,i-1:i+1]=[[2,-1],[1,0]]
    A=(U[:10,:10]-U[10,:10])%mod
    assert np.array_equal(A.T@J@A%mod,J%mod)
    bg[i]=A;bg[-i]=Ji@A.T@J%mod
    assert np.array_equal(bg[i]@bg[-i]%mod,I)
for i in range(1,11):
    for j in range(1,11):
        if abs(i-j)>1:
            assert np.array_equal(bg[i]@bg[j]%mod,bg[j]@bg[i]%mod)
        if abs(i-j)==1:
            assert np.array_equal(bg[i]@bg[j]@bg[i]%mod,bg[j]@bg[i]@bg[j]%mod)

def red(w):
    result=[]
    for a in w:
        if result and result[-1]==-a:result.pop()
        else:result.append(a)
    return tuple(result)
def inv_word(w):return tuple(-a for a in reversed(w))
def mul(*ws):return red(a for w in ws for a in w)
def eval_braid(w):
    A=I.copy()
    for a in w:A=A@bg[a]%mod
    return A
source_braids={int(k)+1:tuple(v) for k,v in data['C5'].items()}
generators={i:eval_braid(w) for i,w in source_braids.items()}
generators.update({-i:Ji@A.T@J%mod for i,A in list(generators.items())})
def evaluate(w):
    A=I.copy()
    for a in w:A=A@generators[a]%mod
    return A
def source_abelian(w):
    return [sum((1 if a==i else -1 if a==-i else 0) for a in w) for i in range(1,7)]

w0=(-6,-2,-1,-3,2,3,1,2,6,-2)
assert not any(source_abelian(w0))
W=evaluate(w0)
P=I.copy();projective_order=None
for i in range(1,21):
    P=P@W%mod
    if np.array_equal(P%p,I) or np.array_equal(P%p,(-I)%p):
        projective_order=i;break
assert projective_order==10
epsilon=1 if np.array_equal(P%p,I) else -1
P=epsilon*P%mod
X=((P-I)%mod)//p
assert np.any(X)
print('Actual B69 word: projective mod3 order10; sign of its tenth power:',epsilon,flush=True)

conjugators=[(),(1,),(2,),(3,),(4,),(6,),(1,1),(2,1),(5,3)]
seed=w0*20
records=[];vectors=[]
for u in conjugators:
    word=mul(u,seed,inv_word(u))
    assert not any(source_abelian(word))
    A=evaluate(word)
    assert np.array_equal(A%p,I)
    V=((A-I)%mod)//p
    G=evaluate(u);Gi=Ji@G.T@J%mod
    assert np.array_equal(V%p,(2*G@X@Gi)%p)
    assert not np.any((V.T@J+J@V)%p)
    records.append({'conjugator':u,'source_word':word,'matrix_mod9':A.tolist(),'Lie_residue':V.tolist()})
    vectors.append(V.reshape(-1))
    print('Conjugator',u,'actual word length',len(word),'; positive principal lift and exact zero source H1: PASS',flush=True)
M=np.array(vectors,dtype=np.int64).T%p

def rref(a):
    a=a.copy()%p;r=0;piv=[]
    for j in range(a.shape[1]):
        q=next((i for i in range(r,a.shape[0]) if a[i,j]),None)
        if q is None:continue
        a[[r,q]]=a[[q,r]]
        a[r]=a[r]*int(a[r,j])%p
        for i in range(a.shape[0]):
            if i!=r:a[i]=(a[i]-a[i,j]*a[r])%p
        piv.append(j);r+=1
        if r==a.shape[0]:break
    return a,piv
_,cols=rref(M)
assert len(cols)==9
_,rows=rref(M.T)
assert len(rows)==9
minor=M[rows,:]
det=int(s.Matrix(minor).det())
assert det%3!=0
print('Nine Lie residues independent in Mat10(F3): rank9; rows',rows,'minor determinant',det,flush=True)

# This comparison is an independent consistency check, not a required
# premise for the lower bound: B64 identifies the saturated Lie rank as9.
cached=json.loads((HERE/'C5_lift.json').read_text())
full=np.array(cached['full_basis'],dtype=np.int64)
assert len(rref(np.hstack([M,full]))[1])==9
print('Independent comparison with all cyclic Schreier congruence directions: equal rank9 spaces, PASS',flush=True)
print('PASS nine actual normal<w0> words span the full cyclic derived principal Lie lattice modulo3',flush=True)
(HERE/'actual_cyclic_rigid_kernel_certificate.json').write_text(json.dumps({
    'provenance':'Recomputed from actual common-base eleven-strand source braids; no discovery imports',
    'modulus':9,'prime':3,'dimension':10,'kernel_word':w0,
    'projective_mod3_order':projective_order,'tenth_power_sign':epsilon,
    'normalized_tenth_power_mod9':P.tolist(),'seed_Lie_residue':X.tolist(),
    'power':20,'source_generator_mod9_matrices':{str(i):A.tolist() for i,A in generators.items() if i>0},
    'actual_rigid_kernel_words':records,'rank':9,'pivot_rows':rows,
    'rank_minor':minor.tolist(),'rank_minor_integer_determinant':det,
    'scope':'Actual words in normal<w0> inside the full cyclic rigid kernel; all-level conclusion uses B64 saturated lattice and successive-cube proof. No ambient common lift or full completion of the abstract normal subgroup is used.'
},indent=2)+'\n')
