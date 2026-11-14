#!/usr/bin/env python3
"""Independent read-only audit of E44's Magnus and integral word comparisons."""
from pathlib import Path
from itertools import combinations
import hashlib,json,time
import numpy as np
import bc_fermat_class_three_burnside as q
from de_ferrari_mod9_lift import rref

HERE=Path(__file__).resolve().parent

def tmul(a,b):
    out={}
    for u,x in a.items():
        for v,y in b.items():
            if len(u)+len(v)<=3:out[u+v]=(out.get(u+v,0)+x*y)%3
    return {w:c for w,c in out.items() if c}

def tensor_word(word):
    out={():1}
    for letter in word:
        i=abs(letter)-1
        factor={():1,(i,):1} if letter>0 else {():1,(i,):2,(i,i):1,(i,i,i):2}
        out=tmul(out,factor)
    return out

def project(a):
    v=np.array([a.get((i,),0) for i in range(10)],dtype=np.int64)
    z=np.array([(a.get((i,j),0)-2*v[i]*v[j])%3 for i,j in q.PAIRS],dtype=np.int64)
    t=np.array([(a.get((i,j,k),0)-a.get((j,i,k),0))%3 for i,j,k in q.TRIPLES],dtype=np.int64)
    return np.r_[v,z,t]

def main():
    start=time.time()
    protected=list(HERE.glob('bc_fermat_class_three_*.py'))+list(HERE.glob('bc_fermat_class_three_*.json'))+list(HERE.glob('bc_fermat_class_three_*.npz'))
    hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in protected}
    rng=np.random.default_rng(45044)
    for _ in range(36):
        a=rng.choice(np.r_[np.arange(1,11),-np.arange(1,11)],size=30).tolist()
        b=rng.choice(np.r_[np.arange(1,11),-np.arange(1,11)],size=30).tolist()
        A=tensor_word(a);B=tensor_word(b)
        assert np.array_equal(project(A),q.collect_signed(a))
        assert np.array_equal(project(B),q.collect_signed(b))
        assert np.array_equal(project(tmul(A,B)),q.multiply(project(A),project(B)))
        assert not np.any(project(tmul(tmul(A,A),A)))
    cube=q.cube_span_certificate()
    assert (cube['ordinary_Lie_dimension'],cube['restricted_cubes_dimension'],cube['complete_cube_span_dimension'])==(330,10,220)
    old=np.load(HERE/'bc_fermat_class_two_fibres.npz');K=old['central_norm_kernel']
    saved=np.load(HERE/'bc_fermat_class_three_norms.npz')
    metadata=json.loads((HERE/'bc_fermat_class_three_norms.json').read_text())
    rows=np.r_[np.arange(55,175),np.arange(230,350)]
    normranks=[]
    for record in metadata['target_records']:
        j=record['target_index'];origin=np.r_[record['abelianization'],record['E33_particular_central'],np.zeros(120,dtype=np.int64)]
        error=q.norm_errors(origin)[rows];columns=[]
        for v in K.T:
            moved=origin.copy();moved[10:55]+=v;moved%=3
            columns.append((q.norm_errors(moved)[rows]-error)%3)
        for i in range(120):
            moved=origin.copy();moved[55+i]+=1;moved%=3
            columns.append((q.norm_errors(moved)[rows]-error)%3)
        A=np.stack(columns,axis=1)
        assert np.array_equal(A,saved[f'target_{j}_norm_matrix'])
        normranks.append(len(rref(A)[1]));assert normranks[-1]==103
        particular=saved[f'target_{j}_norm_particular'];kernel=saved[f'target_{j}_norm_kernel']
        assert not np.any((A@particular+error)%3) and not np.any(A@kernel%3)
        assert kernel.shape==(130,27) and len(rref(kernel)[1])==27
        for _ in range(2):
            v=rng.integers(0,3,size=130)
            moved=origin.copy();moved[10:55]+=K@v[:10];moved[55:]+=v[10:];moved%=3
            assert np.array_equal(q.norm_errors(moved)[rows],(error+A@v)%3)
    integral=np.load(HERE/'bc_cm_fermat_kernel_boundary.npz')
    kb=integral['kernel_boundary_basis'];R=integral['original_relation_boundary_matrix']
    rels=json.loads((HERE/'bc_fermat_class_two_integral_kernel.json').read_text())['basis_preimages']
    assert len(rels)==45
    for rec in rels:
        assert rec['kind']=='adjusted_normal_relator'
        assert np.array_equal(R[:,rec['normal_relator_index']],kb@np.array(rec['integral_K_coordinates']))
    centre=np.load(HERE/'bc_fermat_class_two_integral_kernel.npz')['central_basis']
    comp=np.load(HERE/'bc_fermat_class_three_tower_comparison.npz')
    assert np.array_equal(centre@comp['integral_central_preimage_coefficients']%3,np.eye(45,dtype=np.int64))
    functional=comp['nonlifting_norm_functional'];target=comp['nonlifting_class_three_target']
    assert not np.any(functional@saved['triple_norm_matrix']%3)
    assert int(functional@q.norm_errors(target)[rows]%3)==1
    assert hashes=={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in protected}
    out={'status':'PASS','independent_associative_Magnus_word_pairs':36,
         'complete_cube_span_dimensions':[330,10,220,120],
         'nine_full_affine_norm_ranks':normranks,
         'all45_adjusted_relators_have_exact_zero_integral_H_abelianization':True,
         'all45_actual_central_preimage_columns_verified':True,
         'explicit_full_tower_nonlift_annihilator_value':1,
         'protected_files_unchanged':True,'protected_hashes':hashes,
         'seconds':round(time.time()-start,3)}
    (HERE/'de_boundary_class_three_audit.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='protected_hashes'},indent=2),flush=True)

if __name__=='__main__':main()
