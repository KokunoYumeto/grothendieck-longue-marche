"""Exact fixed-point and commutator-cocycle tests in the affine rank129 target.
Written by GPT-6 Astra, OpenAI, 16 November 2026.
"""
from pathlib import Path
import numpy as np,json
ROOT=Path(__file__).resolve().parent
D=np.load(ROOT/'ferrari_rank129_affine.npz');n=129;I=np.eye(n,dtype=np.int16);zero=np.zeros(n,dtype=np.int16)
def mul(g,h):return((g[0]+g[1]@h[0])%3,g[1]@h[1]%3)
def inverse(M):
    R=np.concatenate((M.copy(),I),axis=1)
    for j in range(n):
        k=j+int(np.flatnonzero(R[j:,j])[0]);R[[j,k]]=R[[k,j]]
        if R[j,j]==2:R[j]=2*R[j]%3
        ii=np.flatnonzero(R[:,j]);ii=ii[ii!=j]
        R[ii]=(R[ii]-R[ii,j,None]*R[j])%3
    return R[:,n:]
def inv(g):
    M=inverse(g[1]);return((-M@g[0])%3,M)
def prod(*gg):
    g=(zero,I)
    for h in gg:g=mul(g,h)
    return g
def comm(g,h):return prod(g,h,inv(g),inv(h))
def rowbasis(rows):
    R=np.array(rows,dtype=np.int16)%3;r=0;piv=[]
    for j in range(R.shape[1]):
        ix=np.flatnonzero(R[r:,j])
        if not len(ix):continue
        k=r+int(ix[0]);R[[r,k]]=R[[k,r]]
        if R[r,j]==2:R[r]=2*R[r]%3
        ii=np.flatnonzero(R[:,j]);ii=ii[ii!=r]
        R[ii]=(R[ii]-R[ii,j,None]*R[r])%3
        piv.append(j);r+=1
        if r==R.shape[0]:break
    return R[:r],piv
def constraints(g):return np.concatenate(((I-g[1])%3,g[0][:,None]),axis=1)
def report(R):
    R,p=rowbasis(R);consistent=129 not in p;h=np.zeros(n,dtype=np.int16)
    if consistent:
        for i,j in enumerate(p):h[j]=R[i,-1]
        assert not np.any((R[:,:n]@h-R[:,-1])%3)
    return {'coefficient_rank':sum(j<n for j in p),'augmented_rank':len(p),
            'has_common_fixed_point':consistent,'solution':h.tolist()if consistent else None}
abc=list(zip(D['generator_translations'],[D[k]for k in ('A','B','C')]))
XX=list(zip(D['Xi_translations'],D['X']))
cases=[('a,b',abc[0],abc[1]),('X1,X2',XX[0],XX[1]),('X2,X3',XX[1],XX[2]),('X3,X4',XX[2],XX[3]),('X4,X5',XX[3],XX[4])]
reports=[]
for name,g,h in cases:
    ordinary=report(np.concatenate((constraints(g),constraints(h)),axis=0))
    # The fixed point equations for the derived subgroup are the normal closure
    # of the single commutator. Conjugation transports affine equations.
    R,_=rowbasis(constraints(comm(g,h)))
    steps=[]
    generators=[g,h,inv(g),inv(h)]
    while True:
        steps.append(len(R));new=[R]
        for v,M in generators:
            Mi=inverse(M)
            # If E z=b, then on g(Fix) one has E M^-1 z=b+E M^-1 v.
            E=R[:,:n]@Mi%3;b=(R[:,-1]+E@v)%3
            new.append(np.concatenate((E,b[:,None]),axis=1))
        S,p=rowbasis(np.concatenate(new,axis=0))
        if len(S)==len(R):R=S;break
        R=S
        if n in p:break
    derived=report(R)
    reports.append({'pair':name,'whole_pair':ordinary,'derived_subgroup':derived,'derived_normal_closure_rank_steps':steps})
print(json.dumps({'dimension':129,'reports':reports,
 'scope':'Exact linear equations overF3; derived test closes the affine fixed-space equations under both generators and their inverses.'},indent=2))
