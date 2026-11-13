#!/usr/bin/env python3
"""Literal old-source power relation and the first five-adic kernel layer.

This reads the complete signed Ferrari model, with the audited source
rewriting.  It never runs the older distribution script, whose main
module writes its output.  Integral symplectic identities are checked
over Q, including the signed modular quotient and odd-modulus target.
"""
from hashlib import sha256
from pathlib import Path
import json
import time
import numpy as np
import sympy as sp
from de_ferrari_a6_source_data import load_data
from de_ferrari_sl2_5_model import FerrariSL2Five
from de_ferrari_degree4_lift import InducedCombined
from e_symplectic_five_integral_residual_root import IntegralModel, enc

HERE = Path(__file__).resolve().parent
STEM = 'e_symplectic_integral_gl_comparison_root'


def modmatrix(a,m):
    return sp.Matrix(a).applyfunc(lambda v:int(v)%m)


def rank_mod(matrix,p):
    rows = [[int(v)%p for v in row] for row in matrix]
    rank = 0
    for col in range(len(rows[0])):
        pivot = next((i for i in range(rank,len(rows)) if rows[i][col]),None)
        if pivot is None:
            continue
        rows[rank],rows[pivot] = rows[pivot],rows[rank]
        scale = pow(rows[rank][col],-1,p)
        rows[rank] = [scale*v%p for v in rows[rank]]
        for i in range(len(rows)):
            if i!=rank:
                factor = rows[i][col]
                rows[i] = [(a-factor*b)%p for a,b in zip(rows[i],rows[rank])]
        rank += 1
    return rank


def main():
    start = time.time()
    protected_names = ['de_ferrari_sl2_5_model.py','de_ferrari_sl2_5_model.npz',
                       'de_ferrari_sl2_5_source.json','de_ferrari_a6_source_data.py',
                       'de_ferrari_sl2_5_N.json','e_symplectic_five_integral_probe_root.json',
                       'e_symplectic_five_integral_residual_root.json']
    hashes = {name:sha256((HERE/name).read_bytes()).hexdigest() for name in protected_names}
    data = load_data()
    signed = FerrariSL2Five()
    frozen = np.load(HERE/'de_ferrari_sl2_5_model.npz')
    for key in ('a','b','c','x','y'):
        assert np.array_equal(getattr(signed,key),frozen[key]),key
    source = InducedCombined(signed,data)
    relations = []
    for name,word in (('x',data['xword']),('y',data['yword'])):
        value = source.word(word)
        assert source.equal(source.power(value,120),source.one)
        order = 120
        for prime in (2,3,5):
            while order%prime==0 and source.equal(source.power(value,order//prime),source.one):
                order //= prime
        assert source.equal(source.power(value,order),source.one)
        for prime in sp.factorint(order):
            assert not source.equal(source.power(value,order//prime),source.one)
        relations.append({'generator':name,'exact_order':order,
                          'literal_B_relation':word*order,
                          'all_36_signed_coordinates_identity':True,
                          'prime_divisor_tests_nonidentity':list(map(int,sp.factorint(order)))})
    assert {row['exact_order'] for row in relations}=={60}
    old_order = json.loads((HERE/'de_ferrari_sl2_5_source.json').read_text())['lifted_group_order']
    factors = {str(k):int(v) for k,v in sp.factorint(old_order).items()}
    assert set(map(int,factors))=={2,3,5}

    # The canonical signed modular representative of a pure source word
    # has both diagonal entries1 modulo4; its sign is unique.
    model = IntegralModel()
    S = sp.Matrix([[0,1],[-1,0]])
    R = sp.Matrix([[0,-1],[1,-1]])
    P = sp.Matrix([[0,1],[1,0]])
    matrices = {0:S,1:R,-1:R.inv()}
    def signed_modular(word):
        value = sp.eye(2)
        for letter in word:
            value *= matrices[letter]
        assert int(value[0,0])%4 in (1,3)
        if int(value[0,0])%4==3:
            value = -value
        assert int(value[1,1])%4==1
        return value
    modular_records = []
    words = [('N'+str(i),word) for i,word in enumerate(data['Nwords'])]
    words += [('K2_'+str(i),r['B_word']) for i,r in enumerate(model.d['K2_full_Schreier_basis_factorizations'])]
    for name,word in words:
        theta,coordinate,_ = model.factor(word)
        value = signed_modular(word)
        assert value==P*theta*P, name
        fw = data['fword'](word)
        exponents = [sum((1 if a>0 else -1) for a in fw if abs(a)==j) for j in (1,2)]
        assert modmatrix(value,4)==modmatrix(sp.Matrix([[1,2*exponents[0]],[-2*exponents[1],1]]),4)
        modular_records.append({'source_word':name,'B_word':word,'F_exponents':exponents,
                                'theta':enc(theta),'canonical_signed_matrix':enc(value)})

    # x^60 is killed in the complete signed source. Its commutator with
    # a residual element having theta=E12(1) detects the whole first
    # principal-congruence layer by conjugation.
    h = sp.Matrix([[1,0],[120,1]])
    u = sp.Matrix([[1,1],[0,1]])
    commutator = h*u*h.inv()*u.inv()
    assert modmatrix(commutator,5)==sp.eye(2)
    first = modmatrix((commutator-sp.eye(2))/5,5)
    assert first != sp.zeros(2) and int(sp.trace(first))%5==0
    conjugators = [sp.Matrix([[1,0],[2,1]]),sp.Matrix([[1,-2],[0,1]])]
    basis, pending = [],[(first,[])]
    while pending:
        value,word = pending.pop(0)
        coordinates = [int(value[0,0])%5,int(value[0,1])%5,int(value[1,0])%5]
        if rank_mod([r['coordinates'] for r in basis]+[coordinates],5)==len(basis):
            continue
        basis.append({'F_conjugator_word':word,'matrix':enc(value),'coordinates':coordinates})
        for j,g in enumerate(conjugators,1):
            pending.append((modmatrix(g*value*g.inv(),5),[j]+word))
    assert len(basis)==3

    # Four chain transvections generate the standard plane transvections
    # over every ring with2 invertible, by the displayed exact identity.
    J = sp.Matrix(model.d['form'])
    vectors = [sp.eye(4)[:,i] for i in range(4)]
    a,b,c,d = vectors[0],vectors[1],vectors[0]+vectors[2],vectors[3]
    symplectic_basis = sp.Matrix.hstack(a,b,c,d)
    assert symplectic_basis.T*J*symplectic_basis==sp.diag(sp.Matrix([[0,1],[-1,0]]),sp.Matrix([[0,1],[-1,0]]))
    t = sp.Symbol('t')
    transvection = lambda v,z:sp.eye(4)+z*v*v.T*J
    half_turn = (transvection(a,1)*transvection(b,1)*transvection(a,1))**2
    assert half_turn*a==-a and half_turn*b==-b and half_turn*c==c and half_turn*d==d
    assert half_turn*(c-a)==c+a
    assert transvection(c+a,t)*transvection(c-a,t)==transvection(c,2*t)*transvection(a,2*t)
    assert transvection(c+a,t)*transvection(a,-t)*transvection(c,-t)==sp.eye(4)+t*(a*c.T*J+c*a.T*J)

    assert all(sha256((HERE/name).read_bytes()).hexdigest()==value for name,value in hashes.items())
    result = {'status':'PASS_SIGNED_COMMON_QUOTIENT_AND_FIRST_CONGRUENCE_LAYER',
              'scope':'Literal source relations and integral identities; the uniform closure and fibre proof is separate.',
              'input_sha256':hashes,'old_signed_source_order_factorization':factors,
              'complete_signed_source_power_relations':relations,
              'canonical_signed_modular_comparisons':modular_records,
              'all_102_modular_comparisons_exact':True,
              'level25_commutator':enc(modmatrix(commutator,25)),
              'level5_Lie_image':enc(first),'normal_conjugate_Lie_basis':basis,
              'normal_conjugate_Lie_rank':3,
              'symplectic_basis':enc(symplectic_basis),'half_turn_matrix':enc(half_turn),
              'exact_transvection_identity_verified':True,
              'original_artifacts_unchanged':True,'seconds':round(time.time()-start,3)}
    (HERE/(STEM+'.json')).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('status','old_signed_source_order_factorization',
                      'level25_commutator','level5_Lie_image','normal_conjugate_Lie_basis',
                      'symplectic_basis','half_turn_matrix','seconds')},indent=2),flush=True)


if __name__=='__main__':
    main()
