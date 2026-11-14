#!/usr/bin/env python3
"""Actual E.1 matrix labels of the 24 retained E.17 base words."""
from pathlib import Path
import json,time
from de_ferrari_a6_source_data import load_data

HERE=Path(__file__).resolve().parent

def main():
    started=time.time();d=load_data();I=d['unit'];s,r=d['ss'],d['rr']
    V4={(1,0,0,1),(1,2,0,1),(1,0,2,1),(1,2,2,1)}
    def lift(a):
        options=[a,tuple(-z%12 for z in a)]
        kept=[b for b in options if tuple(z%4 for z in b) in V4]
        assert len(kept)==1
        return kept[0]
    records=json.loads((HERE/'de_ferrari_fibres.json').read_text())['records']
    assert [r['certificate_index'] for r in records]==list(range(24))
    rows=[]
    for ix,rec in enumerate(records):
        A=d['bvalue'](rec['base_A_word_B']);beta=d['bvalue'](rec['base_beta_word_B'])
        assert d['times'](A,r)==d['times'](r,A)
        assert d['times'](beta,s)==d['times'](s,beta)
        gauge=d['bvalue'](d['bpower'](d['xword'],rec['integral_cusp_gauge']))
        assert gauge==I
        assert d['bvalue'](d['to_B'](rec['actual_commutator_word_f']))==I
        T=d['inverse'](A);W=d['inverse'](beta)
        At=lift(T);Bt=lift(W);v=(1,2)
        Av=((At[0]*v[0]+At[1]*v[1])%3,(At[2]*v[0]+At[3]*v[1])%3)
        assert Av in ((1,2),(2,1))
        bitT=int(Av==(2,1));B3=tuple(a%3 for a in Bt)
        assert B3 in ((1,0,0,1),(2,0,0,2),(0,1,2,0),(0,2,1,0))
        bitW=int(B3 in ((0,1,2,0),(0,2,1,0)))
        assert rec['missing_coset']==(bitT!=bitW)
        rows.append({'base_index':ix,'qA':A,'qbeta':beta,'qV':I,'qT':T,'qW':W,
                     'positive_CM_bits':[bitT,bitW],'extra_coset':bitT!=bitW,
                     'integral_cusp_gauge_has_trivial_Q_image':True})
    assert len({(tuple(row['qT']),tuple(row['qW'])) for row in rows})==24
    assert sum(row['extra_coset'] for row in rows)==12
    out={'status':'PASS_EXACT_CM_MATRIX_COVERAGE','retained_base_points':24,
         'distinct_matrix_pairs':24,'extra_CM_matrix_pairs':12,
         'all_literal_frames_and_positive_E1_bits_checked':True,
         'records':rows,'seconds':round(time.time()-started,3)}
    (HERE/'a_cm_sl23_cm_labels.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2),flush=True)

if __name__=='__main__':main()
