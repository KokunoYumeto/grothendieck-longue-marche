"""Independent direct check of B63's displayed words and upper bound.

No imports from the discovery programs. Use the invariant-covector
hyperplane, read original geometric braids, and directly evaluate the
six rigid-normal words, nine cyclic commutators, and three matched pairs.
"""
from pathlib import Path
from collections import deque
import json,itertools
import numpy as np
import sympy as s

HERE=Path(__file__).resolve().parent;BASE=HERE.parent
data=json.loads((BASE/'next_B59_image/common_base_braid_words.json').read_text())
p=3;m=9;n=10;I=np.eye(n,dtype=np.int64)
eps=np.array([(-1)**i for i in range(11)],dtype=np.int64)
inc=np.vstack([I,-eps[:10]])
braid={}
for j in range(1,11):
    B=np.eye(11,dtype=np.int64);B[j-1:j+1,j-1:j+1]=[[2,-1],[1,0]]
    R=(B@inc)[:10]%m
    Ri=np.array(s.Matrix(R).inv_mod(m),dtype=np.int64)
    assert np.array_equal(R@Ri%m,I)
    braid[j]=R;braid[-j]=Ri
def norm(A):
    A=A%m;v=next(int(x)%p for x in A.flat if x%p)
    return A if v==1 else -A%m
def key(A):return (norm(A)%p).astype(np.int8).tobytes()
def evaluate(word,generators):
    A=I.copy()
    for j in word:A=A@generators[j]%m
    return norm(A)
def rank(A):
    A=np.array(A,dtype=np.int64,copy=True)%p;r=0
    for j in range(A.shape[1]):
        k=next((k for k in range(r,A.shape[0]) if A[k,j]),None)
        if k is None:continue
        A[[r,k]]=A[[k,r]];A[r]=A[r]*int(A[r,j])%p
        f=A[:,j].copy();f[r]=0;A=(A-f[:,None]*A[r])%p
        r+=1
        if r==A.shape[0]:break
    return r
G={}
for name in ('T','C5'):
    G[name]={}
    for index,(_,word) in enumerate(sorted(data[name].items(),key=lambda t:int(t[0])),1):
        A=evaluate(word,braid);G[name][index]=A
        G[name][-index]=np.array(s.Matrix(A).inv_mod(m),dtype=np.int64)

def inverse(word):return[-j for j in word[::-1]]
def comm(a,b):return a+b+inverse(a)+inverse(b)
def conjugate(a,b):return a+b+inverse(a)
def reduce(word):
    out=[]
    for j in word:
        if out and out[-1]==-j:out.pop()
        else:out.append(j)
    return out

h=[6,11,-6,-5]
nw=[comm([1],h),comm([3],h),
    conjugate([7],h)+inverse(conjugate([5],h)),
    conjugate([1,2],h)+inverse(conjugate([2],h)),
    conjugate([2],conjugate([7],h)+inverse(conjugate([5],h))),
    conjugate([5,5],h)+inverse(conjugate([2,5],h))]
# Integer+1 encodes f_0,...,f_5.
cw=[comm([1],[4]),comm([1]*3,[2]),comm([1]*3,[3]),
    comm([2]*3,[3]),comm([2]*3,[4]),comm([2]*3,[5]),
    comm([2]*3,[6]),comm([2],[3]*3),comm([2],[4])*2]
nw=[reduce(w) for w in nw];cw=[reduce(w) for w in cw]
L={}
for name,words in [('T',nw),('C5',cw)]:
    vectors=[]
    for word in words:
        A=evaluate(word,G[name]);assert np.array_equal(A%p,I)
        vectors.append((((A-I)%m)//3).reshape(-1))
    L[name]=np.array(vectors).T
    assert rank(L[name])==len(words)
print('PASS displayed rigid-normal6 and cyclic-commutator9 words have independent congruence images')

# Full congruence image upper bounds by all Schreier generators.
for name,expected in [('T',144),('C5',1440)]:
    gens=[G[name][j] for j in range(1,len(G[name])//2+1)]
    reps=[I.copy()];seen={key(I):0};q=deque([0]);edges=[]
    while q:
        i=q.popleft()
        for j,A in enumerate(gens):
            B=norm(reps[i]@A);k=key(B)
            if k not in seen:seen[k]=len(reps);reps.append(B);q.append(seen[k])
            edges.append((i,j,seen[k]))
    assert len(reps)==expected
    inv=[np.array(s.Matrix(A).inv_mod(m),dtype=np.int64) for A in reps]
    vectors=[]
    for i,j,k in edges:
        A=norm(reps[i]@gens[j]@inv[k]);assert np.array_equal(A%p,I)
        vectors.append((((A-I)%m)//3).reshape(-1))
    full=np.array(vectors).T
    assert rank(full)==L[name].shape[1]
    assert rank(np.hstack([full,L[name]]))==L[name].shape[1]
    print('PASS full',name,'congruence image dimension',rank(full),'from',len(edges),'Schreier edges')

aw=[nw[1]+nw[3]*2,
    nw[0]+nw[1]*2+nw[2]+nw[3]*2+nw[4]*2,
    nw[0]*2+nw[2]+nw[3]*2+nw[4]+nw[5]]
bw=[cw[1]+cw[2],
    cw[1]+cw[3]*2+cw[4]*2+cw[5]+cw[6],
    cw[1]+cw[3]*2+cw[5]*2+cw[7]+cw[8]]
X=[]
for i,(a,b) in enumerate(zip(aw,bw)):
    a,b=reduce(a),reduce(b)
    A,B=evaluate(a,G['T']),evaluate(b,G['C5'])
    assert np.array_equal(A,B)
    X.append((((A-I)%m)//3).reshape(-1))
    print('PASS matched pair',i,'source lengths',len(a),len(b))
X=np.array(X).T
assert rank(X)==3
assert rank(np.hstack([L['T'],L['C5']]))==12
for i,j,coeff in [(0,1,[1,0,0]),(0,2,[2,0,0]),(1,2,[0,1,1])]:
    a=X[:,i].reshape(n,n);b=X[:,j].reshape(n,n)
    assert np.array_equal((a@b-b@a).reshape(-1)%p,X@np.array(coeff)%p)
print('PASS exact3-dimensional common module and displayed solvable Lie brackets')

normal_witness=None
for j in range(1,14):
    A=G['T'][j]%p;Ai=G['T'][-j]%p
    for k in range(3):
        z=(A@X[:,k].reshape(n,n)@Ai).reshape(-1)%p
        if rank(np.column_stack([X,z]))==4:
            normal_witness={'tetrahedral_generator':j,'common_basis_index':k}
            break
    if normal_witness:break
assert normal_witness is not None
print('PASS common module is not normal under T image; witness',normal_witness)
record={'normalization':'invariant-covector hyperplane, independent of discovery quotient basis',
        'T_normal_words':nw,'C5_commutator_words':cw,
        'T_common_words':[reduce(w) for w in aw],'C5_common_words':[reduce(w) for w in bw],
        'T_congruence_basis':L['T'].tolist(),'C5_congruence_basis':L['C5'].tolist(),
        'common_basis':X.tolist(),'nonnormality_witness':normal_witness,
        'factor_indices':[144*3**3,1440*3**6],
        'scope':'Exact quotient-level statement. No common lift to the actual residual K is asserted.'}
(HERE/'independent_short_word_certificate.json').write_text(json.dumps(record,indent=2)+'\n')
print('PASS all independent B63 word, module and nonnormality checks')
