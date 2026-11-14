"""Exact actual source matrices on the three-parameter product-one locus.

The coefficient map is (t1,...,t7)->(r,s,t,1,1,1,(r*s*t)^-1).
The boundary covector and the three character-one deleted coordinates
give a two-dimensional invariant submodule in H1. All basis maps and
source matrices here are literal specializations of the accepted F24
data; no rank or image assertion outside the recorded identities is made.
"""
from hashlib import sha256
from pathlib import Path
import json
import sympy as sp


r, s, t = sp.symbols('r s t')
CHECKS = {}


def check(test, category):
    assert test, category
    CHECKS[category] = CHECKS.get(category, 0) + 1


def simplify(x):
    return sp.factor(sp.cancel(x))


def specialized(poly):
    terms = {}
    for coefficient, exponent in poly:
        key = (exponent[0]-exponent[6], exponent[1]-exponent[6], exponent[2]-exponent[6])
        terms[key] = terms.get(key, 0)+coefficient
    return sp.Add(*(coefficient*r**a*s**b*t**c for (a,b,c),coefficient in terms.items() if coefficient))


def clean(a):
    return a.applyfunc(simplify)


def verify_zero(a, category):
    for x in a:
        check(sp.cancel(x) == 0, category)


def serialize(a):
    return [[str(simplify(a[i,j])) for j in range(a.cols)] for i in range(a.rows)]


def main():
    producer=Path(__file__).resolve()
    source=producer.with_name('affine_obstruction_stage_output.json')
    data=json.loads(source.read_text())
    old=[a for a in data['records'] if a['index']<11]
    seeds=[a for a in data['records'] if a['index']>=11]
    c=r*s*t
    character=sp.Matrix([r,s,t,1,1,1,1/c])
    delta=character-sp.ones(7,1)
    projection=sp.eye(6).row_join(-delta[:6,0]/delta[6])
    section=sp.eye(6).col_join(sp.zeros(1,6))
    boundary=sp.Matrix([[1,r,r*s,c,c,c]])
    e=sp.eye(6)
    basis=sp.Matrix.hstack(e[:,1]-r*e[:,0],e[:,2]-r*s*e[:,0],e[:,0],
                           e[:,3]-c*e[:,0],e[:,4]-c*e[:,0],e[:,5]-c*e[:,0])
    inverse=sp.Matrix.vstack(e[1,:],e[2,:],boundary,e[3,:],e[4,:],e[5,:])
    verify_zero(basis*inverse-sp.eye(6),'basis_inverse')
    verify_zero(inverse*basis-sp.eye(6),'inverse_basis')
    kernel_section=basis[:,:2]
    kernel_projection=inverse[:2,:]
    verify_zero(kernel_projection*kernel_section-sp.eye(2),'kernel_inverse')
    records=[];full=[];cores=[]
    for record in old:
        action=sp.Matrix([[specialized(p) for p in row] for row in record['action_matrix']])
        verify_zero(action*delta-delta,'principal_line_fixed')
        quotient=clean(projection*action*section)
        block=clean(inverse*quotient*basis)
        core=block[:2,:2]
        for i in range(2,6):
            for j in range(6):
                if i!=j: check(block[i,j]==0,'boundary_residue_quotient_diagonal')
        verify_zero(quotient*kernel_section-kernel_section*core,'actual_kernel_inclusion')
        correction=clean((action*section*kernel_section)[6,:]/delta[6])
        verify_zero(action*section*kernel_section-section*kernel_section*core-delta*correction,
                    'actual_core_principal_corrections')
        rec={'index':record['index'],'label':record['label'],
             'core_matrix':serialize(core),'core_trace':str(simplify(sp.trace(core))),
             'core_determinant':str(simplify(core.det())),
             'quotient_characters':[str(block[j,j]) for j in range(2,6)],
             'extension_matrix':serialize(block[:2,2:]),
             'principal_correction_row':serialize(correction),
             'action_7':serialize(action),'action_H1_6':serialize(quotient),
             'block_action_6':serialize(block)}
        records.append(rec);full.append(action);cores.append(core)
    seed_records=[];seed_rows={}
    for record in seeds:
        row=sp.Matrix([[specialized(p) for p in record['u_derivation_row']]])
        seed_rows[record['index']]=row
        seed_records.append({'index':record['index'],'label':record['label'],
                             'core_value_row':serialize(clean(row*section*kernel_section))})
    chosen=seed_rows[25]
    evaluation=[]
    for i,action in enumerate(full):
        kappa=clean(chosen*(action-sp.eye(7)))
        verify_zero(kappa*delta,'actual_character_one_evaluation')
        evaluation.append({'source_index':i,'word':'B_i(u_25)*u_25^-1',
                           'core_evaluation':serialize(clean(kappa*section*kernel_section))})
    commutators=[]
    for i in range(11):
        for j in range(i+1,11):
            matrix=clean(cores[i]*cores[j]-cores[j]*cores[i])
            if any(matrix):
                commutators.append({'source_pair':[i,j],'matrix':serialize(matrix),
                                     'determinant':str(simplify(matrix.det()))})
    output=producer.with_name('affine_product_one_three_parameter_stage_output.json')
    result={'status':'EXACT_THREE_PARAMETER_PRODUCT_ONE_SOURCE_RESEARCH',
            'producer_sha256':sha256(producer.read_bytes()).hexdigest(),
            'source_sha256':sha256(source.read_bytes()).hexdigest(),
            'coefficient_ring':'Z[r^+-1,s^+-1,t^+-1,(1-r*s*t)^-1]',
            'character':[str(x) for x in character],
            'principal_projection':serialize(projection),'principal_section':serialize(section),
            'boundary_covector':serialize(boundary),'basis':serialize(basis),'inverse_basis':serialize(inverse),
            'kernel_section':serialize(kernel_section),'kernel_projection':serialize(kernel_projection),
            'source_records':records,'seed_records':seed_records,
            'actual_character_one_core_evaluations':evaluation,'core_additive_commutators':commutators,
            'checks':CHECKS,'check_total':sum(CHECKS.values()),
            'scope':'The exact three-parameter locus only. The two-dimensional source submodule and all displayed maps are verified as symbolic identities. No irreducibility, essentiality, field separation or general affine image equality is inferred here.'}
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'checks':result['check_total'],
                      'source_cores':[{k:x[k] for k in ['index','core_matrix','core_trace','core_determinant','principal_correction_row']} for x in records],
                      'seed_core_values':seed_records,'character_one_core_evaluations':evaluation,
                      'core_commutators':commutators,'output_sha256':sha256(output.read_bytes()).hexdigest()},indent=2))


if __name__=='__main__':
    main()
