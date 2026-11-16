"""Integral affine transfer from the256-vertex D-cover to the8-vertex C'-cover.
Written by GPT-6 Astra, OpenAI, 16 November 2026.
"""
from pathlib import Path
import numpy as np,json
ROOT=Path(__file__).resolve().parent
F=np.load(ROOT/'ferrari_rank129.npz');D=np.load(ROOT/'ferrari_rank129_integral.npz')
Q=F['Q'];edges=F['edges'];cycles=D['cycles'];idx={tuple(map(int,q)):i for i,q in enumerate(Q)}
base_edges=sorted({(min(v,v^(1<<i)),max(v,v^(1<<i)))for v in range(8)for i in range(3)})
bei={e:i for i,e in enumerate(base_edges)}
sections={v:tuple(i for i in range(3)if v&(1<<i))for v in range(8)}
tree=set();paths=np.zeros((12,8),dtype=np.int64)
for v,w in sections.items():
    q=0
    for i in w:
        r=q^(1<<i);e=(min(q,r),max(q,r));tree.add(e);paths[bei[e],v]+=1 if q<r else-1;q=r
base_chords=[bei[e]for e in base_edges if e not in tree];assert len(base_chords)==5
bc=np.zeros((12,5),dtype=np.int64)
for j,k in enumerate(base_chords):
    q,r=base_edges[k];bc[:,j]=paths[:,q]-paths[:,r];bc[k,j]+=1
assert np.array_equal(bc[base_chords],np.eye(5,dtype=np.int64))
P=np.zeros((12,384),dtype=np.int64)
for k,(q,r,i)in enumerate(edges):
    v=int(Q[q,1]);w=v^(1<<int(i));P[bei[(min(v,w),max(v,w))],k]=1 if v<w else-1
J=(P@cycles)[base_chords];assert np.array_equal(bc@J,P@cycles)
words=(((0,1,0),(0,),(2,)),((2,),(1,),(2,0,2)),((1,),(1,0,1),(1,0,2,0,1)))
u8_num=-np.sum(paths,axis=1);baseM=[];baseR=[]
for ii,images in enumerate(words):
    phi=[]
    for v in range(8):
        out=0
        for i in range(3):
            if v&(1<<i):
                for j in images[i]:out^=1<<j
        phi.append(out)
    chain=np.zeros((12,12),dtype=np.int64)
    for k,(q,r)in enumerate(base_edges):
        i=(q^r).bit_length()-1;v=phi[q]
        for j in images[i]:
            w=v^(1<<j);chain[bei[(min(v,w),max(v,w))],k]+=1 if v<w else-1;v=w
        assert v==phi[r]
    M=(chain@bc)[base_chords];assert np.array_equal(bc@M,chain@bc)
    assert np.array_equal(P@D['chainmaps'][ii],chain@P)
    assert np.array_equal(J@D[('A','B','C')[ii]],M@J)
    r=(u8_num-chain@u8_num)[base_chords];baseM.append(M);baseR.append(r)
delta_num=(P@D['edge_gauge_numerator']-32*u8_num)[base_chords]
for ii,M in enumerate(baseM):
    assert np.array_equal(J@D['translation_numerators'][ii],32*baseR[ii]+(np.eye(5,dtype=np.int64)-M)@delta_num)

# Literal averaging projector for the32-element deck group C'/D.
direct={}
for k,(q,r,i)in enumerate(edges):direct[(int(q),int(i))]=(k,1);direct[(int(r),int(i))]=(k,-1)
E=np.zeros((129,129),dtype=np.int64)
deck_elements=[int(v)for v,b in Q if b==0];assert len(deck_elements)==32
for v in deck_elements:
    perm=[idx[(int(q[0])^v,int(q[1]))]for q in Q]
    image=np.zeros_like(cycles)
    for k,(q,r,i)in enumerate(edges):
        l,s=direct[(perm[q],int(i))];image[l]=s*cycles[k]
    M=image[F['chords']];assert np.array_equal(cycles@M,image);E+=M
assert np.array_equal(E@E,32*E)
assert np.array_equal(J@E,32*J)
for name in('A','B','C'):assert np.array_equal(E@D[name],D[name]@E)
assert np.trace(E)==32*5

# The central two-part in the rank5 affine model is an exact dyadic matrix.
I6=np.eye(6,dtype=np.int64)
aug=[]
for M,r in zip(baseM,baseR):
    a=I6.copy();a[:5,:5]=M;a[:5,5]=r;aug.append(a)
AB=aug[0]@aug[1];Z=AB@AB@AB;N=Z@Z-I6
assert not np.any(N@N)
J2_num=Z@(2*I6-N) # twice the central involution
assert np.array_equal(J2_num@J2_num,4*I6)
assert all(np.array_equal(J2_num@g,g@J2_num)for g in aug[:2])

np.savez_compressed(ROOT/'ferrari_rank129_transfer.npz',homology_pushforward=J,
                    deck_projector_numerator=E,deck_projector_denominator=np.array(32),
                    affine_gauge_difference_numerator=delta_num,affine_gauge_difference_denominator=np.array(256),
                    base_A=baseM[0],base_B=baseM[1],base_C=baseM[2],
                    base_translation_numerators=np.stack(baseR),base_translation_denominator=np.array(8),
                    base_central_involution_numerator=J2_num,base_central_involution_denominator=np.array(2))
print(json.dumps({'high_cover_vertices':256,'base_cover_vertices':8,
 'pushforward_dimensions':[5,129],
 'edge_pushforward_equivariance_verified_over_Z':True,
 'homology_pushforward_equivariance_verified_over_Z':True,
 'deck_average_projector_rank':5,'deck_average_denominator':32,
 'projector_commutes_with_all_L_generators_over_Z':True,
 'affine_gauge_difference':'delta=(p_*(u_D numerator)-32*(u_Cprime numerator))/256',
 'exact_affine_comparison':'J*r_D=r_Cprime+(I−M_Cprime)*delta',
 'all_three_affine_comparison_identities_verified_over_Z':True,
 'rank5_central_braid_two_part_is_exact_central_involution_over_Z_one_half':True,
 'scope':'Integral transfer and affine gauge comparison, valid over every odd-adic coefficient ring.'},indent=2))
