"""Literal reverse-prime obstructions for S and its odd power S^3."""
import json
import numpy as np
from check_ferrari_d3_fox import *

D=np.load(ROOT/'ferrari_d3_fox.npz');F=np.load(ROOT/'ferrari_d3_filtration.npz')
saved=np.load(ROOT/'ferrari_d3_controlled_seed.npz')
X=list(zip(D['X_permutations'],D['X_blocks']));x,y=X[0],X[1]
def A(g,h):
    z=inv(mul(g,h));assert all(eq(power(v,12),ONE) for v in (g,h,z))
    g,h,z=[power(v,4) for v in (g,h,z)]
    return comm(comm(g,h),comm(h,z))
z=inv(mul(x,y));s=prod(A(y,z),A(x,y),A(z,x))
assert eq(s,(saved['seed_permutations'][24],saved['seed_blocks'][24]))
assert bounded_order(s)==12
t=power(s,4);two=power(s,9)
assert bounded_order(t)==3 and bounded_order(two)==4
mixed=comm(t,prod(x,two,inv(x)))
assert np.array_equal(mixed[0],IP) and not eq(mixed,ONE)
first=int(np.flatnonzero(np.any(mixed[1]!=IM,axis=(1,2)))[0]);assert first==10
assert int(np.count_nonzero(np.any(mixed[1]!=IM,axis=(1,2))))==52
mf=mm(F['basis_inverse'][first],mm(mixed[1][first],F['basis'][first]))
fb,fh=int(F['boundary_dimensions'][first]),int(F['homology_dimensions'][first])
assert np.array_equal(mf[fb:fh,fb:fh],np.eye(fh-fb,dtype=np.int16))
u=power(s,3);g=mul(y,x);v=prod(g,u,inv(g));w=mul(u,v)
assert bounded_order(u)==bounded_order(v)==4
assert np.array_equal(w[0],IP) and bounded_order(w)==12
k=37;assert characters[k].tolist()==[1,0,1,1,0] and int(u[0][k])==42
def matrix_order(M):
    I=np.eye(len(M),dtype=np.int16);p=I
    for n in range(1,100):
        p=mm(p,M)
        if np.array_equal(p,I):return n
    raise AssertionError('order bound')
ad=mm(F['basis_inverse'][k],mm(w[1][k],F['basis'][k]))
assert F['boundary_dimensions'][k]==1 and F['homology_dimensions'][k]==4
orders=[matrix_order(ad),matrix_order(ad[:4,:4]),matrix_order(ad[1:4,1:4])]
assert orders==[6,3,3]
out={'field':'F2[w], w^2+w+1=0; encoding a+2b',
 'same_actual_source_word_reconstructed':True,'seed_order':12,
 'seed_character_permutation_order':2,'moved_characters':216,
 'mixed_primary_test':'[S^4, x S^9 x^-1] !=1; primary orders3,4',
 'mixed_primary_first_character':characters[first].tolist(),'mixed_primary_first_index':first,
 'mixed_primary_5x5_commutator':mixed[1][first].tolist(),
 'odd_power_test':'u=S^3, v=(yx)u(yx)^-1; bothorder4',
 'product_global_order':12,'product_character_index':k,'product_character':characters[k].tolist(),
 'u_character_partner':42,'product_full5_matrix':w[1][k].tolist(),
 'adapted_product':ad.tolist(),'full_cycle_proper_product_orders':orders,
 'conclusion':'Both the normal closure of S and the normal closure of S^3 are nonnilpotent in this exact finite target.',
 'scope':'These are obstructions to two particular actual source seeds. No conclusion about every R2 seed or genuine GT is inferred.'}
(ROOT/'ferrari_d3_seed_obstruction.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
