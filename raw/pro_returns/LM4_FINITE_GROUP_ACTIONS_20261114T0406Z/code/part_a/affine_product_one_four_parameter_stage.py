"""Exact exploratory source data with one nontrivial deleted parameter.

The literal coefficient map is (r,s,t,u,1,1,(r*s*t*u)^-1).
The boundary and the two remaining trivial deleted coordinates define
an actual three-dimensional invariant submodule. No field-separation
or marginal-image assertion is made by this research calculation.
"""
from pathlib import Path
from hashlib import sha256
import json
import sympy as sp

r,s,t,u=sp.symbols('r s t u')
z=sp.symbols('z')
CHECKS={}


def check(condition,category):
    assert condition,category
    CHECKS[category]=CHECKS.get(category,0)+1


def simp(a):
    return sp.factor(sp.cancel(a))


def clean(a):
    return a.applyfunc(simp)


def verify(a,category):
    for v in a:check(sp.cancel(v)==0,category)


def spec(poly):
    terms={}
    for coeff,e in poly:
        key=tuple(e[j]-e[6] for j in range(4))
        terms[key]=terms.get(key,0)+coeff
    return sp.Add(*(coef*r**a*s**b*t**c*u**d for (a,b,c,d),coef in terms.items() if coef))


def ser(a):
    return [[str(simp(a[i,j])) for j in range(a.cols)] for i in range(a.rows)]


def main():
    producer=Path(__file__).resolve();source=producer.with_name('affine_obstruction_stage_output.json')
    data=json.loads(source.read_text());c=r*s*t*u
    char=sp.Matrix([r,s,t,u,1,1,1/c]);delta=char-sp.ones(7,1)
    projection=sp.eye(6).row_join(-delta[:6,0]/delta[6])
    section=sp.eye(6).col_join(sp.zeros(1,6));e=sp.eye(6)
    boundary=sp.Matrix([[1,r,r*s,r*s*t,c,c]])
    basis=sp.Matrix.hstack(e[:,1]-r*e[:,0],e[:,2]-r*s*e[:,0],
                          e[:,3]-r*s*t*e[:,0],e[:,0],e[:,4]-c*e[:,0],e[:,5]-c*e[:,0])
    inverse=sp.Matrix.vstack(e[1,:],e[2,:],e[3,:],boundary,e[4,:],e[5,:])
    verify(basis*inverse-sp.eye(6),'basis_inverse');verify(inverse*basis-sp.eye(6),'inverse_basis')
    kernel_section=basis[:,:3]
    records=[];old_actions=[]
    for record in [x for x in data['records'] if x['index']<11]:
        action=sp.Matrix([[spec(p) for p in row] for row in record['action_matrix']])
        verify(action*delta-delta,'principal_fixed')
        quotient=clean(projection*action*section);block=clean(inverse*quotient*basis);core=block[:3,:3]
        for i in range(3,6):
            for j in range(6):
                if i!=j:check(block[i,j]==0,'three_diagonal_quotients')
        verify(quotient*kernel_section-kernel_section*core,'actual_core_inclusion')
        correction=clean((action*section*kernel_section)[6,:]/delta[6])
        verify(action*section*kernel_section-section*kernel_section*core-delta*correction,'actual_principal_correction')
        item={'index':record['index'],'label':record['label'],'core_matrix':ser(core),
              'core_characteristic_polynomial':str(simp(core.charpoly(z).as_expr())),
              'quotient_characters':[str(block[j,j]) for j in range(3,6)],
              'extension_matrix':ser(block[:3,3:]),'principal_correction':ser(correction),
              'action_7':ser(action),'action_H1_6':ser(quotient),'block_action_6':ser(block)}
        records.append(item);old_actions.append(action)
    seed_records=[];chosen=None
    for record in [x for x in data['records'] if x['index']>=11]:
        row=sp.Matrix([[spec(p) for p in record['u_derivation_row']]])
        seed_records.append({'index':record['index'],'label':record['label'],
                             'core_values':ser(clean(row*section*kernel_section))})
        if record['index']==25:chosen=row
    evaluations=[]
    for i,a in enumerate(old_actions):
        row=clean(chosen*(a-sp.eye(7)));verify(row*delta,'actual_character_one_evaluation')
        evaluations.append({'source_index':i,'core_values':ser(clean(row*section*kernel_section))})
    output=producer.with_name('affine_product_one_four_parameter_stage_output.json')
    result={'status':'EXACT_FOUR_PARAMETER_PRODUCT_ONE_RESEARCH','producer_sha256':sha256(producer.read_bytes()).hexdigest(),
            'source_sha256':sha256(source.read_bytes()).hexdigest(),'character':[str(x) for x in char],
            'coefficient_ring':'Z[r^+-1,s^+-1,t^+-1,u^+-1,(1-r*s*t*u)^-1]',
            'basis':ser(basis),'inverse_basis':ser(inverse),'kernel_section':ser(kernel_section),
            'boundary_covector':ser(boundary),'source_records':records,'seed_records':seed_records,
            'actual_character_one_core_evaluations':evaluations,'checks':CHECKS,'check_total':sum(CHECKS.values()),
            'scope':'Exact source identities on this four-parameter locus. No universal factor separation, invariant simplicity, or finite affine marginal theorem is inferred.'}
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'checks':result['check_total'],
                      'source_cores':[{k:a[k] for k in ['index','core_matrix','core_characteristic_polynomial','quotient_characters']} for a in records],
                      'seed_core_values':seed_records,'source_core_evaluations':evaluations,
                      'output_sha256':sha256(output.read_bytes()).hexdigest()},indent=2))


if __name__=='__main__':main()
