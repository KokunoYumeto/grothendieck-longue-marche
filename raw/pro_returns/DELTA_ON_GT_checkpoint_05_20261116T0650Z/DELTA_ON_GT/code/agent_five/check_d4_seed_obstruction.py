"""Short literal certificate: the cyclic S seed has nonnilpotent D4 image.

The obstruction already survives the three-dimensional proper quotient
of one nontrivial-character chain block. It is not a GT counterexample.
"""
import json
import numpy as np
from check_ferrari_d4_fox import *

D=np.load(ROOT/'ferrari_d4_fox.npz')
F=np.load(ROOT/'ferrari_d4_filtration.npz')
X=list(zip(D['X_permutations'],D['X_blocks']))
x,y=X[0],X[1]

def seedA(g,h):
    z=inv(mul(g,h))
    assert all(eq(power(t,24),ONE) for t in (g,h,z))
    # 16=0 mod8 and 1 mod3 is the exact e3 residue at all these orders.
    gp,hp,zp=[power(t,16) for t in (g,h,z)]
    return comm(comm(gp,hp),comm(hp,zp))

z=inv(mul(x,y));s=prod(seedA(y,z),seedA(x,y),seedA(z,x))
saved=np.load(ROOT/'ferrari_d4_controlled_seed.npz')['seed_blocks'][24]
assert np.array_equal(s[0],IP) and np.array_equal(s[1],saved)
assert eq(power(s,6),ONE) and not eq(power(s,3),ONE) and not eq(power(s,2),ONE)
u=power(s,3);g=mul(y,x);v=prod(g,u,inv(g));w=mul(u,v)
assert eq(power(u,2),ONE) and eq(power(v,2),ONE)
k=81;assert characters[k].tolist()==[1,0,1,1,0]
orbit={k};queue=[k]
for h in queue:
    for q in (x[0],y[0]):
        j=int(q[h])
        if j not in orbit:orbit.add(j);queue.append(j)
orbit=sorted(orbit);assert len(orbit)==16
T,Ti=F['basis'][k],F['basis_inverse'][k]
assert F['boundary_dimensions'][k]==1 and F['homology_dimensions'][k]==4
adapted=[mm(Ti,mm(h[1][k],T)) for h in (u,v,w)]

def matrix_order(M,cap=100):
    I=np.eye(len(M),dtype=np.int16);P=I
    for j in range(1,cap+1):
        P=mm(P,M)
        if np.array_equal(P,I):return j
    raise AssertionError('declared matrix order bound exceeded')

def matrix_rank(M):
    a=M.copy();r=0
    for j in range(a.shape[1]):
        nz=np.flatnonzero(a[r:,j])
        if not len(nz):continue
        k=r+int(nz[0]);a[[r,k]]=a[[k,r]];a[r]=MUL[INV[a[r,j]],a[r]]
        for k in range(len(a)):
            if k!=r:a[k]=ADD[a[k],NEG[MUL[a[k,j],a[r]]]]
        r+=1
        if r==len(a):break
    return r

orders={};nilpotent_ranks={}
for name,sl in [('full_chain',slice(None)),('cycle',slice(0,4)),('proper',slice(1,4))]:
    orders[name]=[matrix_order(M[sl,sl]) for M in adapted]
    m=adapted[2][sl,sl];eye=np.eye(len(m),dtype=np.int16);n=ADD[m,NEG[eye]];q=eye
    nilpotent_ranks[name]=[]
    for j in range(1,len(m)+1):
        q=mm(q,n);nilpotent_ranks[name].append(matrix_rank(q))
assert orders=={'full_chain':[2,2,9],'cycle':[2,2,9],'proper':[2,2,3]}
assert nilpotent_ranks=={'full_chain':[4,3,2,1,0],'cycle':[3,2,1,0],'proper':[2,1,0]}
assert bounded_order(w)==18
report={'field':'F3[i], i^2=-1; a+3b encodes a+b*i',
 'source_seed':'S=A_e3(y,z) A_e3(x,y) A_e3(z,x); A_e3=[[x^e3,y^e3],[y^e3,z^e3]]; z=(xy)^-1',
 'exact_exponent_residue':16,'seed_order':6,
 'involutions':'u=S^3; v=(yx)u(yx)^-1',
 'character_index':k,'character':characters[k].tolist(),
 'cusp_exponents':[0,1,1,2],'minimal_harmonic_character_orbit':orbit,
 'orbit_size':16,'whole_product_order':18,
 'u_raw_5x5':u[1][k].tolist(),'v_raw_5x5':v[1][k].tolist(),
 'product_raw_5x5':w[1][k].tolist(),'adapted_basis':T.tolist(),
 'adapted_u':adapted[0].tolist(),'adapted_v':adapted[1].tolist(),
 'adapted_product':adapted[2].tolist(),'orders_u_v_product':orders,
 'ranks_of_powers_of_product_minus_identity':nilpotent_ranks,
 'conclusion':'The normal closure of this S image contains involutions whose product has order3 in a proper3-dimensional quotient. It is not nilpotent.',
 'scope':'This refutes the nilpotent-normal-image condition for this exact seed at D4. It does not exclude another source seed or settle Delta on genuine GT.'}
(ROOT/'ferrari_d4_seed_obstruction.json').write_text(json.dumps(report,indent=2)+'\n')
np.savez_compressed(ROOT/'ferrari_d4_obstruction_orbit.npz',character_indices=orbit,
 characters=characters[orbit],generator_permutations=np.stack([x[0][orbit],y[0][orbit]]),
 generator_blocks=np.stack([x[1][orbit],y[1][orbit]]),basis=F['basis'][orbit],
 basis_inverse=F['basis_inverse'][orbit],boundary_dimensions=F['boundary_dimensions'][orbit])
print(json.dumps(report,indent=2))
