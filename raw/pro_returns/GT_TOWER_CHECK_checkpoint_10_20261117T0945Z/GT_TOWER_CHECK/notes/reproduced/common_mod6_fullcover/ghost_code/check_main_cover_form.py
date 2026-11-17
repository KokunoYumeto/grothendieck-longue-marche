#!/usr/bin/env python3
"""Compute the actual compact-cover intersection form from its 36 boundaries.

All boundary words are rewritten from the literal index-eight quaternion
cover. Their product in the class-two quotient with central boundaries
recovers the compact symplectic bivector, then the specified multiplicity
form is compared to the retained orthogonal form.
"""
from pathlib import Path
import json
import runpy
import numpy as np

here=Path(__file__).resolve().parent
s=runpy.run_path(str(here/'check_main_faithful_detector.py'))
D=s['D'];H=s['H'];peripheral=s['peripheral'];rewrite=s['rewrite73']
cover=s['cover'];sections=s['sections73'];invword=s['inverse_word']


def inverse(a):
    n=len(a);r,p=s['rref'](np.hstack((a,np.eye(n,dtype=np.int64))))
    assert p[:n]==list(range(n))
    return r[:,n:]


r,pivots=s['rref'](peripheral)
r=r[:len(pivots)]
free=[j for j in range(73) if j not in pivots]
assert len(pivots)==35 and len(free)==38
P=np.zeros((38,73),dtype=np.int64)
P[:,free]=np.eye(38,dtype=np.int64)
P[:,pivots]=-r[:,free].T%3
assert not np.any(P@peripheral.T%3)
S=np.zeros((73,38),dtype=np.int64)
S[free]=np.eye(38,dtype=np.int64)
assert np.array_equal(P@S%3,np.eye(38,dtype=np.int64))
pairs=[(i,j) for i in range(38) for j in range(i+1,38)]
left=np.array([i for i,j in pairs]);right=np.array([j for i,j in pairs])
boundary_words=[];boundary_centers=[]
for c in cover['peripheral_words']:
    for q in range(4):
        word=rewrite(sections[q]+tuple(c)+tuple(c)+invword(sections[q]))
        ab=np.zeros(38,dtype=np.int64);center=np.zeros(len(pairs),dtype=np.int64)
        for letter in word:
            v=P[:,abs(letter)-1]*(1 if letter>0 else -1)
            center=(center+2*(ab[left]*v[right]-ab[right]*v[left]))%3
            ab=(ab+v)%3
        assert not np.any(ab)
        boundary_words.append(word);boundary_centers.append(center)
assert len(boundary_words)==36
omega_coefficients=-sum(boundary_centers)%3
omega=np.zeros((38,38),dtype=np.int64)
omega[left,right]=omega_coefficients
omega[right,left]=-omega_coefficients%3
assert s['rank'](omega)==38
J=inverse(omega)
assert np.array_equal(J.T%3,-J%3)
print('NEW PASS 36 literal boundary words recover a nondegenerate compact bivector of rank38')

all_generators=H['actual_integral_generators'].astype(np.int64)
compact=[]
for a in all_generators:
    b=P@a%3@S%3
    assert np.array_equal(b@P%3,P@a%3)
    assert np.array_equal(b@omega%3@b.T%3,omega)
    assert np.array_equal(b.T@J%3@b%3,J)
    compact.append(b)
print('NEW PASS all15 actual source generators preserve the recovered compact intersection form')

C=H['quaternion_component_basis'].astype(np.int64)
CB=H['multiplicity_basis'].astype(np.int64)
deck=H['deck_matrices'].astype(np.int64)
faithful=P@C%3;primitive=P@CB%3
J36=faithful.T@J@faithful%3
assert s['rank'](faithful)==36 and s['rank'](J36)==36
assert not np.any(primitive.T@J@primitive%3)
B=primitive.T@J@(P@deck[1]@CB%3)%3
assert np.array_equal(B,B.T) and s['rank'](B)==18
F=np.load(D/'translation_quaternion_image.npz')['form'].astype(np.int64)
positions=np.argwhere(F!=0);i,j=positions[0]
scalar=int(B[i,j]*F[i,j]%3)
assert scalar and np.array_equal(B,scalar*F%3)
print('NEW PASS faithful36 is symplectic and contains no boundary radical')
print('NEW PASS actual symmetric multiplicity form equals',scalar,'times the certified F')
for a in H['quaternion_kernel_generators'].astype(np.int64):
    assert np.array_equal(a.T@B%3@a%3,B)
print('NEW PASS all360 kernel generators preserve this boundary-derived multiplicity form')

# Exact dyadic compact quotient used to retain determinant modulo four.
def dyadic_product(a,b):
    return ((a[0]+b[0])%8,(a[1]+b[1])%8,(a[2]+b[2]+a[0]*b[1])%4)
def dyadic_power(a,n):
    z=(0,0,0)
    for _ in range(n):z=dyadic_product(z,a)
    return z
elements=[(i,j,k) for i in range(8) for j in range(8) for k in range(4)]
assert len(elements)==256
assert all(dyadic_power(a,8)==(0,0,0) for a in elements)
aa=(1,0,0);bb=(0,1,0)
comm=dyadic_product(dyadic_product(dyadic_product(aa,bb),dyadic_power(aa,7)),dyadic_power(bb,7))
assert comm==(0,0,1) and dyadic_power(comm,4)==(0,0,0) and dyadic_power(comm,2)!=(0,0,0)
print('NEW PASS dyadic compact class-two quotient has256 elements, exponent8, commutator order4')

record={
 'scope':'Actual finite peripheral class-two recovery of the genus19 compact cover form',
 'T_rank':73,'boundary_count':36,'boundary_homology_rank':35,'compact_rank':38,
 'centralized_boundary_quotient_exponent':73+38*37//2,
 'centralized_boundary_quotient_order':'3^776','Pi_extension_order':'8*3^776',
 'faithful_rank':36,'multiplicity_rank':18,'multiplicity_form_scalar':scalar,
 'actual_boundary_words_T73':[list(w) for w in boundary_words],
 'boundary_product_bivector':omega_coefficients.tolist(),
 'compact_basis_free_columns':free,
 'characteristic_input_degree_bound':'128*3^1172',
 'dyadic_compact_quotient_order':256,'dyadic_generator_exponent':8,
 'dyadic_commutator_order':4,
}
Path(__file__).with_suffix('.json').write_text(json.dumps(record,indent=2)+'\n')
np.savez_compressed(Path(__file__).with_suffix('.npz'),
 compact_projection=P,compact_section=S,boundary_centers=np.array(boundary_centers),
 compact_bivector=omega,compact_intersection=J,faithful_intersection=J36,
 multiplicity_form=B,compact_generator_matrices=np.array(compact))
