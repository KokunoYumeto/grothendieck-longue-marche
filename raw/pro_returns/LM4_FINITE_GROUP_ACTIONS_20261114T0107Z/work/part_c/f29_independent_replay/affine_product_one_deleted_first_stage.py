"""Actual product-one chart with the first deleted character nontrivial.

The coefficient tuple is (r,s,t,(r*s*t)^-1,1,1,1), and the
principal pivot is X4. This is the c=1 stratum of the four-parameter
continuation. No generator permutation or comparison with the
deleted-last locus is assumed.
"""
from pathlib import Path
from hashlib import sha256
import json
import sympy as sp

r,s,t,z=sp.symbols('r s t z');CHECKS={}


def check(x,k):
    assert x,k
    CHECKS[k]=CHECKS.get(k,0)+1


def simp(x):return sp.factor(sp.cancel(x))


def clean(x):return x.applyfunc(simp)


def verify(a,k):
    for x in a:check(sp.cancel(x)==0,k)


def spec(p):
    terms={}
    for a,e in p:
        key=tuple(e[j]-e[3] for j in range(3));terms[key]=terms.get(key,0)+a
    return sp.Add(*(a*r**i*s**j*t**k for (i,j,k),a in terms.items() if a))


def ser(a):return [[str(simp(a[i,j])) for j in range(a.cols)] for i in range(a.rows)]


def main():
    producer=Path(__file__).resolve();source=producer.with_name('affine_obstruction_stage_output.json')
    data=json.loads(source.read_text());c=r*s*t
    char=sp.Matrix([r,s,t,1/c,1,1,1]);delta=char-sp.ones(7,1);pivot=3;keep=[0,1,2,4,5,6]
    projection=sp.zeros(6,7);section=sp.zeros(7,6)
    for j,i in enumerate(keep):projection[j,i]=1;projection[j,pivot]=-delta[i]/delta[pivot];section[i,j]=1
    verify(projection*section-sp.eye(6),'principal_maps_inverse')
    e=sp.eye(6);boundary=sp.Matrix([[1,r,r*s,1,1,1]])
    basis=sp.Matrix.hstack(e[:,1]-r*e[:,0],e[:,2]-r*s*e[:,0],e[:,0],e[:,3]-e[:,0],e[:,4]-e[:,0],e[:,5]-e[:,0])
    inverse=sp.Matrix.vstack(e[1,:],e[2,:],boundary,e[3,:],e[4,:],e[5,:])
    verify(basis*inverse-sp.eye(6),'basis_inverse');verify(inverse*basis-sp.eye(6),'inverse_basis')
    core_section=basis[:,:2];records=[]
    for rec in [a for a in data['records'] if a['index']<11]:
        a=sp.Matrix([[spec(p) for p in row] for row in rec['action_matrix']]);verify(a*delta-delta,'principal_fixed')
        q=clean(projection*a*section);b=clean(inverse*q*basis);g=b[:2,:2]
        for i in range(2,6):
            for j in range(6):
                if i!=j:check(b[i,j]==0,'four_diagonal_quotients')
        verify(q*core_section-core_section*g,'actual_core_inclusion')
        correction=clean((a*section*core_section)[pivot,:]/delta[pivot])
        verify(a*section*core_section-section*core_section*g-delta*correction,'actual_principal_correction')
        records.append({'index':rec['index'],'label':rec['label'],'core_matrix':ser(g),
                        'core_characteristic_polynomial':str(simp(g.charpoly(z).as_expr())),
                        'quotient_labels':['boundary','X5','X6','X7'],
                        'quotient_characters':[str(b[j,j]) for j in range(2,6)],
                        'extension_matrix':ser(b[:2,2:]),'action_7':ser(a),'action_H1_6':ser(q),'block_action_6':ser(b)})
    output=producer.with_name('affine_product_one_deleted_first_stage_output.json')
    result={'status':'EXACT_DELETED_FIRST_PRODUCT_ONE_RESEARCH','producer_sha256':sha256(producer.read_bytes()).hexdigest(),
            'source_sha256':sha256(source.read_bytes()).hexdigest(),'character':[str(x) for x in char],
            'principal_pivot':4,'quotient_coordinate_original_indices':[i+1 for i in keep],
            'principal_projection':ser(projection),'principal_section':ser(section),'boundary_covector':ser(boundary),
            'basis':ser(basis),'inverse_basis':ser(inverse),'source_records':records,'checks':CHECKS,'check_total':sum(CHECKS.values()),
            'scope':'Literal deleted-first coefficient map and X4 principal pivot only. No unproved source-preserving permutation or marginal-image conclusion is asserted.'}
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'checks':result['check_total'],
                      'source_table':[{k:a[k] for k in ['index','core_matrix','core_characteristic_polynomial','quotient_characters']} for a in records],
                      'output_sha256':sha256(output.read_bytes()).hexdigest()},indent=2))


if __name__=='__main__':main()
