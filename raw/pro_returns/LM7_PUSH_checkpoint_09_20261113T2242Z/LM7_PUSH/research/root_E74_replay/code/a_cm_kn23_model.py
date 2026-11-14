#!/usr/bin/env python3
"""Exact K_2/K_3 left-right actions in all frozen GL23/SL23 epikernels.

For a literal q:F=<x,y> -> H and a cyclic-cover Schreier section,
  (j,z).w = (j+k, q(delta_n(x^j w x^(-j-k)))^(-1) z q(w)).
The second coordinate is the actual left-right action on H. For f in
F-prime, K_n is the finite tuple condition (0,q(y)^c).f=(0,1),
together with the actual c_n mod24. No full-GT value is assigned.
"""
from pathlib import Path
from hashlib import sha256
from itertools import product
from math import lcm
import json
import time
import numpy as np

from de_ferrari_a6_source_data import load_data


HERE=Path(__file__).resolve().parent
NS=(2,3)
MODULUS=24


def permword(word,generators):
    value=np.arange(len(generators[0]),dtype=np.uint16)
    letters={1:generators[0],2:generators[1],
             -1:np.argsort(generators[0]),-2:np.argsort(generators[1])}
    for a in word:value=letters[a][value]
    return value


def delta_word(word,n,start=0):
    j=start;out=[]
    for a in word:
        if a==1:
            if j==n-1:out.append(1)
            j=(j+1)%n
        elif a==-1:
            if j==0:out.append(-1)
            j=(j-1)%n
        elif j==0:out.append(a)
    return j,out


def main():
    start=time.monotonic();groups={};quotients=[]
    for kind,prefix in [('GL23','GL2'),('SL23','SL2')]:
        filename='a_cm_'+kind.lower()+'_model.npz'
        data=np.load(HERE/filename)
        elements=[tuple(map(int,a)) for a in data[prefix+'_elements']]
        mul=data[prefix+'_multiplication'];inv=data[prefix+'_inverse'];one=int(data[prefix+'_one'])
        size=len(elements);assert size==(48 if kind=='GL23' else 24)
        for i,a in enumerate(elements):
            for j,b in enumerate(elements):
                literal=tuple(v%3 for v in (a[0]*b[0]+a[1]*b[2],a[0]*b[1]+a[1]*b[3],
                                            a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3]))
                assert elements[int(mul[i,j])]==literal
            assert mul[i,inv[i]]==one and mul[inv[i],i]==one
        assert elements[one]==(1,0,0,1)
        groups[kind]={'mul':mul,'inv':inv,'one':one,'size':size,'elements':elements}
        for index,(x,y) in enumerate(data['kernel_representatives']):
            x,y=map(int,(x,y));seen={one};todo=[one]
            for a in todo:
                for b in (x,y):
                    c=int(mul[a,b])
                    if c not in seen:seen.add(c);todo.append(c)
            assert len(seen)==size
            orders=[]
            for a in (x,y):
                c=one;order=0
                while True:
                    c=int(mul[c,a]);order+=1
                    if c==one:break
                    assert order<=size
                orders.append(order)
            quotients.append({'kind':kind,'kernel_index':index,'x':x,'y':y,
                              'x_matrix':elements[x],'y_matrix':elements[y],
                              'x_order':orders[0],'y_order':orders[1]})
    assert len(quotients)==34
    assert lcm(*(q['y_order'] for q in quotients))==MODULUS

    blocks=[];generators=[[],[]];offset=0;retained=[];targets=[]
    for n in NS:
        for qi,q in enumerate(quotients):
            g=groups[q['kind']];size=g['size'];one=g['one'];mul=g['mul'];inv=g['inv']
            blocks.append({'n':n,'kind':'matrix','quotient_index':qi,'start':offset,
                           'size':size,'identity':one,'unit_target_full':offset+one})
            retained.extend(range(offset,offset+size));targets.append(offset+one)
            for k in range(2):
                b=q['x'] if k==0 else q['y'];p=[]
                for j in range(n):
                    shift=1 if k==0 else 0
                    a=b if (k==0 and j==n-1) or (k==1 and j==0) else one
                    p.extend((offset+size*((j+shift)%n)+mul[inv[a],mul[np.arange(size),b]]).tolist())
                generators[k].extend(p)
            offset+=n*size
        blocks.append({'n':n,'kind':'coefficient','start':offset,'size':MODULUS,
                       'identity':0,'unit_target_full':offset})
        retained.extend(range(offset,offset+MODULUS));targets.append(offset)
        for k in range(2):
            p=[]
            for j in range(n):
                for z in range(MODULUS):
                    shift=1 if k==0 else 0
                    c=int(k==1 and j==0)
                    p.append(offset+MODULUS*((j+shift)%n)+(z+c)%MODULUS)
            generators[k].extend(p)
        offset+=n*MODULUS
    F=np.array(generators,dtype=np.uint16)
    assert F.shape==(2,6360)
    assert all(np.array_equal(np.sort(p),np.arange(offset)) for p in F)

    def qword(word,q):
        g=groups[q['kind']];v=g['one'];letters={1:q['x'],2:q['y'],
                                               -1:int(g['inv'][q['x']]),-2:int(g['inv'][q['y']])}
        for a in word:v=int(g['mul'][v,letters[a]])
        return v

    tests=[[]]+[list(w) for k in range(1,4) for w in product((1,-1,2,-2),repeat=k)]
    tests += [[1]*n for n in NS]
    tests += [[1]*j+[2]+[-1]*j for n in NS for j in range(n)]
    for w in tests:
        p=permword(w,F)
        for block in blocks:
            n=block['n'];off=block['start'];size=block['size']
            for j in range(n):
                end,dw=delta_word(w,n,j)
                if block['kind']=='matrix':
                    q=quotients[block['quotient_index']];g=groups[q['kind']]
                    a=qword(dw,q);b=qword(w,q)
                    expected=off+size*end+g['mul'][g['inv'][a],g['mul'][np.arange(size),b]]
                else:
                    c=sum(1 if a==2 else -1 if a==-2 else 0 for a in dw)
                    expected=off+size*end+(np.arange(size)+c)%size
                assert np.array_equal(p[off+size*j:off+size*(j+1)],expected)

    source=load_data();nwords=[list(source['fword'](w)) for w in source['Nwords']]
    N=np.array([permword(w,F) for w in nwords])
    e67=json.loads((HERE/'bc_orbifold_CM_export.json').read_text())
    assert nwords==e67['literal_N_basis_in_F']
    old=np.load(HERE/'a_cm_distribution_orbifold.npz')['common_N']
    assert old.shape==(97,5331)
    common=np.array([np.r_[a,5331+b] for a,b in zip(old,N)])
    assert common.shape==(97,11691)
    inverse=np.full(offset,-1,dtype=np.int64);inverse[retained]=np.arange(len(retained))
    unit_targets=[int(inverse[i]) for i in targets]
    assert len(unit_targets)==70 and len(retained)==2544
    out={'status':'PASS_LITERAL_UNIVERSAL_GL23_SL23_K2_K3_ACTION_MODEL',
         'N_values':NS,'coefficient_modulus':MODULUS,'literal_quotients':quotients,
         'group_orders':{k:v['size'] for k,v in groups.items()},
         'all_literal_matrix_multiplication_tables_checked':True,
         'all_kernel_representatives_generate_their_matrix_group':True,
         'actual_left_right_formula_tests':len(tests),
         'all_97_N_words_compared_with_E67_and_replayed':True,
         'new_full_source_degree':offset,'old_full_source_degree':5331,
         'common_full_source_degree':11691,'new_coordinate_zero_degree':len(retained),
         'fixed_target_count':len(targets),'blocks':blocks,
         'left_right_action':'(j,z).w=(j+k,q(delta_n(x^j w x^(-j-k)))^(-1) z q(w))',
         'finite_Kn_equation':'For f in F-prime, (0,q(y)^c).f=(0,1), and c_n(f)=c mod24.',
         'source_basis_words_in_F':nwords,
         'input_sha256':{name:sha256((HERE/name).read_bytes()).hexdigest() for name in
             ['a_cm_gl23_model.npz','a_cm_sl23_model.npz','de_ferrari_a6_source_data.py',
              'de_ferrari_sl2_5_N.json','bc_orbifold_CM_export.json','a_cm_distribution_orbifold.npz']},
         'scope':'Actual finite quotient model only. Its complete common correction image '
                 'and fixed-value fibres are not assigned by this stage.',
         'seconds':round(time.monotonic()-start,6)}
    np.savez_compressed(HERE/'a_cm_kn23_model.npz',F_generators=F,N_generators=N,common_N=common,
                        retained_projection_points=np.array(retained),
                        fixed_targets_in_projection=np.array(unit_targets))
    (HERE/'a_cm_kn23_model.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in {'literal_quotients','blocks','source_basis_words_in_F'}},indent=2))


if __name__=='__main__':main()
