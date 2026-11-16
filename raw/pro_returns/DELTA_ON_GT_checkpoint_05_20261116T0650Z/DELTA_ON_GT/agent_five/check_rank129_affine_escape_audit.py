"""Independent actual-source cyclic seed audit for the affine129 target.
Written by GPT-6 Astra, OpenAI, 16 November 2026.
Uses independent inverse arithmetic and the literal residue e3=4mod12.
"""
from pathlib import Path
from itertools import permutations
import numpy as np,json
ROOT=Path(__file__).resolve().parent
D=np.load(ROOT/'ferrari_rank129_affine.npz');F=np.load(ROOT/'ferrari_rank129_blocks.npz');G=np.load(ROOT/'ferrari_rank129_boundary.npz')
n=129;I=np.eye(n,dtype=np.int16);zero=np.zeros(n,dtype=np.int16);one=(zero,I)
transfer=np.load(ROOT/'ferrari_rank129_transfer.npz')
E=(2*transfer['deck_projector_numerator'])%3;complement=(I-E)%3
assert np.array_equal(E@E%3,E)
T=F['basis']@G['basis']%3;Ti=G['basis_inverse']@F['basis_inverse']%3;bi=G['boundary_indices'];pi=G['proper_indices']
def mul(a,b):return((a[0]+a[1]@b[0])%3,a[1]@b[1]%3)
def eq(a,b):return np.array_equal(a[0],b[0])and np.array_equal(a[1],b[1])
def matrix_inverse(M):
    R=np.concatenate((M.copy(),I),axis=1)
    for j in range(n):
        k=j+int(np.flatnonzero(R[j:,j])[0]);R[[j,k]]=R[[k,j]]
        if R[j,j]==2:R[j]=2*R[j]%3
        ii=np.flatnonzero(R[:,j]);ii=ii[ii!=j]
        R[ii]=(R[ii]-R[ii,j,None]*R[j])%3
    return R[:,n:]
def inv(a):
    M=matrix_inverse(a[1]);return(-M@a[0]%3,M)
def prod(*gg):
    q=one
    for g in gg:q=mul(q,g)
    return q
def power(g,k):
    h=one
    while k:
        if k&1:h=mul(h,g)
        g=mul(g,g);k//=2
    return h
def comm(g,h):return prod(g,h,inv(g),inv(h))
def A(g,h):
    z=inv(mul(g,h));assert all(eq(power(v,12),one)for v in(g,h,z))
    g,h,z=[power(v,4)for v in(g,h,z)]
    return comm(comm(g,h),comm(h,z))
def S(g,h):
    z=inv(mul(g,h));return prod(A(h,z),A(g,h),A(z,g))
X=list(zip(D['Xi_translations'],D['X']));reports=[]
for i,j in ((2,3),(4,0),(1,2),(3,4),(0,1)):
    x,y=X[i],X[j];z=inv(mul(x,y));triple=(x,y,z);records=[]
    for p in permutations(range(3)):
        s=S(triple[p[0]],triple[p[1]]);s2=power(s,3);s3=power(s,4)
        assert eq(power(s,6),one)
        assert eq(power(s2,2),one)and eq(power(s3,3),one)
        assert eq(prod(s2,s3),s)
        assert all(eq(mul(s2,g),mul(g,s2))for g in(x,y))
        assert not np.any(complement@s2[0]%3)
        assert not np.any(complement@(s2[1]-I)%3)
        graded=Ti@s3[1]@T%3
        assert not np.any(graded[np.ix_(pi,bi)])
        assert np.array_equal(graded[np.ix_(bi,bi)],np.eye(63,dtype=np.int16))
        assert np.array_equal(graded[np.ix_(pi,pi)],np.eye(66,dtype=np.int16))
        records.append({'peripheral_permutation':p,'seed_is_identity':eq(s,one),
                        'two_part_central':True,'three_part_in_normal_unipotent_kernel':True,
                        'two_part_identity_on_all_nontrivial_deck_characters_including_translation':True})
    reports.append({'pair':[i+1,j+1],'core_checks':records})

# Independent literal signed level12 check.
def m2(a,b):return tuple(sum(a[2*i+k]*b[2*k+j]for k in range(2))%12 for i in range(2)for j in range(2))
i2=(1,0,0,1)
def p2(a,k):
    b=i2
    for _ in range(k):b=m2(b,a)
    return b
def iv2(a):return(a[3],-a[1]%12,-a[2]%12,a[0])
def c2(a,b):return m2(m2(m2(a,b),iv2(a)),iv2(b))
def a2(x,y):
    z=iv2(m2(x,y));x,y,z=p2(x,4),p2(y,4),p2(z,4)
    return c2(c2(x,y),c2(y,z))
x=(1,2,0,1);y=(1,0,10,1);z=iv2(m2(x,y))
s=m2(m2(a2(y,z),a2(x,y)),a2(z,x));assert s==(5,0,0,5)
print(json.dumps({'exact_source_seed':'S=A_e3(y,z) A_e3(x,y) A_e3(z,x), A_e3=[[x^e3,y^e3],[y^e3,z^e3]]',
 'signed_mod12_image':s,'all30_pair_core_checks':reports,
 'normal_closure_conclusion':'In each pair, all two-primary seed parts are central; all three-primary parts lie in one normal finite3-group. The full peripheral-core normal closure is therefore nilpotent.',
 'scope':'Independent arithmetic verification of the controlled R2 seed. The actual global lift follows from R2 and the stated nilpotent-image argument, not from a surviving finite f assignment.'},indent=2))
