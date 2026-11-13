#!/usr/bin/env python3
"""Literal induced-section comparison with both frozen finite sources."""
from hashlib import sha256
from pathlib import Path
import json
import time
import numpy as np
import sympy as sp
from de_ferrari_a6_source_data import load_data

HERE=Path(__file__).resolve().parent
STEM='bc_symplectic_integral_source_comparison'


def main():
    start=time.time(); data=load_data()
    d=json.loads((HERE/'e_symplectic_five_integral_probe_root.json').read_text())
    cosets=[tuple(q) for q in d['B_cosets']]
    ix={q:i for i,q in enumerate(cosets)}
    sections=d['B_coset_section']
    records=[]; protected={}
    for p,model_name,source_name in (
        (5,'e_symplectic_five_p5_model_root.npz','e_symplectic_five_p5_source_root_generators.npz'),
        (7,'bc_symplectic_five_p7_model.npz','bc_symplectic_five_p7_source_generators.npz')):
        for name in (model_name,source_name):
            protected[name]=sha256((HERE/name).read_bytes()).hexdigest()
        model=np.load(HERE/model_name); source=np.load(HERE/source_name)
        points=model['points']; degree=len(points)
        lookup={tuple(v):i for i,v in enumerate(points)}
        pairs=[(sp.Matrix(a),sp.Matrix(b)) for a,b in d['evaluation_pairs']]
        letters={1:np.array([np.array(a.tolist(),dtype=np.int64)%p for a,b in pairs]),
                 2:np.array([np.array(b.tolist(),dtype=np.int64)%p for a,b in pairs]),
                 -1:np.array([np.array(a.inv().tolist(),dtype=np.int64)%p for a,b in pairs]),
                 -2:np.array([np.array(b.inv().tolist(),dtype=np.int64)%p for a,b in pairs])}
        comparisons=[]
        for label,b,qb in (('s',0,data['s2']),('r',1,data['r2'])):
            out=[]; word_rows=[]
            for i,q in enumerate(cosets):
                j=ix[data['mul2'](q,qb)]
                word=data['fword'](sections[i]+[b]+data['binv'](sections[j]))
                matrices=np.array([np.eye(4,dtype=np.int64)]*8)
                for t in word:
                    matrices=matrices@letters[t]%p
                for k,matrix in enumerate(matrices):
                    local=np.array([lookup[tuple(v)] for v in points@matrix%p],dtype=np.int64)
                    out.extend((degree*(8*j+k)+local).tolist())
                word_rows.append(list(word))
            actual=np.array(out,dtype=np.int64)
            assert np.array_equal(actual,source[label]),(p,label)
            comparisons.append({'letter':label,'point_count':len(actual),
                                'literal_six_coset_words':word_rows,'array_equal':True})
        records.append({'prime':p,'same_BFS_section':True,'conjugating_gauge':'identity',
                        'source_generators':comparisons})
    assert all(sha256((HERE/n).read_bytes()).hexdigest()==h for n,h in protected.items())
    result={'status':'PASS_LITERAL_INDUCED_SOURCE_COMPARISON',
            'prime_records':records,'protected_input_sha256':protected,
            'all_frozen_originals_unchanged':True,'seconds':round(time.time()-start,3)}
    (HERE/(STEM+'.json')).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
