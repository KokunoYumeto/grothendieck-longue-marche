#!/usr/bin/env python3
"""Exact reduced canonical obstruction on the binary affine source families.

The fixed central quotient has exponent two.  The section into the
class-two, exponent-four preimage of K makes the defect a quadratic
function of the sixteen affine parameters; all its values are enumerated.
"""
from pathlib import Path
import sys,json
import numpy as np
from flint import fmpz_mat

HERE=Path(__file__).resolve().parent
TOWER=HERE.parent/'tower_code';GHOST=HERE.parent/'ghost_code'
sys.path.insert(0,str(TOWER))
src=(TOWER/'test_fivepoint_cm_level.py').read_text()
ns={'__name__':'binary_family_prefix','__file__':str(HERE/'binary_family_prefix.py')}
exec(compile(src.split('records=[];base_records=[]',1)[0],str(TOWER/'test_fivepoint_cm_level.py'),'exec'),ns)
z=np.load(HERE/'check_modular_binary_central_obstruction.npz')
rel=z['central_relations'].astype(np.int64);kap=z['kappas'].astype(np.int64)
def rref(A,B=None):
    A=np.asarray(A,dtype=np.int64).copy()%2
    if B is None:B=np.empty((len(A),0),dtype=np.int64)
    else:
        B=np.asarray(B,dtype=np.int64).copy()%2
        if B.ndim==1:B=B[:,None]
    original_A=A.copy();original_B=B.copy();piv=[];row=0
    for col in range(A.shape[1]):
        nz=np.flatnonzero(A[row:,col])
        if not len(nz):continue
        j=row+int(nz[0]);A[[row,j]]=A[[j,row]];B[[row,j]]=B[[j,row]]
        nz=np.flatnonzero(A[:,col]);nz=nz[nz!=row]
        A[nz]^=A[row];B[nz]^=B[row]
        piv.append(col);row+=1
        if row==len(A):break
    assert not np.any(B[row:])
    point=np.zeros((A.shape[1],B.shape[1]),dtype=np.int64);point[piv]=B[:row]
    free=[i for i in range(A.shape[1]) if i not in piv]
    null=np.zeros((len(free),A.shape[1]),dtype=np.int64)
    for k,j in enumerate(free):null[k,j]=1;null[k,piv]=A[:row,j]
    assert not np.any(original_A@null.T%2)
    assert not np.any((original_A@point-original_B)%2)
    return point,null

full_snf=fmpz_mat(rel.tolist()).snf()
reduced_rel=np.vstack((rel,kap))
reduced_snf=fmpz_mat(reduced_rel.tolist()).snf()
full_diag=[int(full_snf[i,i]) for i in range(112)]
reduced_diag=[int(reduced_snf[i,i]) for i in range(112)]
assert full_diag.count(2)==16 and full_diag.count(1)==96
assert reduced_diag.count(2)==5 and reduced_diag.count(1)==107
_,dual=rref(reduced_rel)
assert dual.shape==(5,112)
assert not np.any(reduced_rel@dual.T%2)
selected_defect=z['defect']@dual.T%2
assert np.any(selected_defect)
hnf_full=fmpz_mat(rel.tolist()).hnf().tolist()
hnf_reduced=fmpz_mat(reduced_rel.tolist()).hnf().tolist()
np.savez_compressed(HERE/'modular_binary_central_smith.npz',
    central_relations=rel,kappas=kap,full_hnf=np.array(hnf_full,dtype=np.int64),
    reduced_hnf=np.array(hnf_reduced,dtype=np.int64),full_smith=np.array(full_diag),
    reduced_smith=np.array(reduced_diag),reduced_dual=dual,selected_defect=z['defect'],
    selected_obstruction=selected_defect)
print('PASS full Smith invariants C2^16; reduced invariants C2^5; selected defect',selected_defect.tolist(),flush=True)

bt=ns['btable'];bgs=(ns['bxq'],ns['byq']);binv=ns['binverses'];bstate=ns['bforder'];tree=ns['bftree']
ci={a:i for i,a in enumerate((q,k) for q in bstate for k,g in enumerate(bgs) if (q,k) not in tree)}
wi=ns['inverse'];subst=ns['subst'];SX=((2,),(1,));RX=((2,),(-2,-1))
pairs=[(i,j) for i in range(97) for j in range(i+1,97)];pi={a:i for i,a in enumerate(pairs)}
projection=z['wedge_projection']
coord=[sum(int(a)<<i for i,a in enumerate(row)) for row in projection]
def rewrite(w):
    q=0;out=[]
    for x in w:
        k=abs(x)-1
        if x>0:e=(q,k);q=int(bt[q,bgs[k]]);sign=1
        else:q=int(bt[q,binv[bgs[k]]]);e=(q,k);sign=-1
        if e in ci:out.append(sign*(ci[e]+1))
    assert q==0
    return out
def central(w):
    a=[0]*97;c=0
    for letter in rewrite(w):
        i=abs(letter)-1
        for j in range(i+1,97):
            if a[j]%2:c^=coord[pi[(i,j)]]
        a[i]+=1 if letter>0 else -1
    assert not any(t%2 for t in a)
    vec=np.array([t//2 for t in a]+[(c>>i)&1 for i in range(15)],dtype=np.int64)
    return vec@dual.T%2

archive=np.load(HERE/'census_common_mod6_frames.npz')
mod=np.load(GHOST/'check_fivepoint_binary_module.npz')
L=mod['projection_left_inverse'].astype(np.int64)
P=mod['common_projection'].astype(np.int64)
loops=ns['jloops'];paths=ns['jpaths'];ab=ns['abloops'].T.astype(np.int64)
def sourceword(v,b):
    raw=np.asarray(v,dtype=np.int64)@L%2
    return tuple(t for i in range(289) if raw[i] for t in loops[i])+paths[b]
def defect(beta,A,b,a):
    bw=sourceword(beta,b);aw=sourceword(A,a)
    word=bw+subst(wi(bw)+aw+subst(wi(aw),RX),SX)
    return central(word)
def bits(v):return sum(int(a)<<i for i,a in enumerate(v))

rows=[];saves={}
source_records=json.loads((HERE/'census_common_mod6_frames.json').read_text())['records']
for base in (0,255,256):
    key=f'b{base}_p2'
    N=archive[key+'_nullspace'].astype(np.int64);assert N.shape==(16,97)
    us=L@archive[key+'_SM']%2
    ur=L@np.hstack((archive[key+'_RM'],ab))%2
    bs,_=rref(us.T,N.T)
    ars,_=rref(ur.T,np.vstack((N.T,np.zeros((2,16),dtype=np.int64))))
    db=bs.T;da=ars.T
    for c in range(8):
        beta=archive[key+f'_beta_{c}'].astype(np.int64)
        A=archive[key+f'_A_{c}'].astype(np.int64)
        b,a=map(int,archive[key+'_base_frames'][c])
        def ev(mask):
            v=np.array([(mask>>i)&1 for i in range(16)],dtype=np.int64)
            return bits(defect((beta+v@db)%2,(A+v@da)%2,b,a))
        constant=ev(0)
        linear=[ev(1<<i)^constant for i in range(16)]
        cross={}
        for i in range(16):
            for j in range(i+1,16):cross[i,j]=ev((1<<i)|(1<<j))^constant^linear[i]^linear[j]
        def polynomial(mask):
            value=constant;active=[i for i in range(16) if (mask>>i)&1]
            for i in active:value^=linear[i]
            for ii,i in enumerate(active):
                for j in active[ii+1:]:value^=cross[i,j]
            return value
        for mask in (65535,21845,43690,12345,54321,4242):assert polynomial(mask)==ev(mask)
        counts=[0]*32;survivors=[]
        for mask in range(65536):
            value=polynomial(mask);counts[value]+=1
            if value==0:survivors.append(mask)
        rec=next(t for t in source_records if t['base']==base and t['beta_base']==b and t['A_base']==a)
        row={'base':base,'candidate':c,'parity':rec['parity'],'constant_defect':constant,
             'obstruction_counts':counts,'passing_count':len(survivors),
             'first_passing_parameter':survivors[0] if survivors else None}
        rows.append(row)
        saves[key+f'_c{c}_linear']=np.array(linear,dtype=np.int64)
        saves[key+f'_c{c}_cross']=np.array([cross[i,j] for i in range(16) for j in range(i+1,16)],dtype=np.int64)
        saves[key+f'_c{c}_survivors']=np.array(survivors,dtype=np.int64)
        print('FAMILY',base,c,'parity',rec['parity'],'canonical passes',len(survivors),'of65536',flush=True)
    saves[key+'_beta_variations']=db;saves[key+'_A_variations']=da
out={'scope':'Full reduced binary canonical cusp obstruction on the exact sixteen-dimensional affine families.',
     'full_multiplier_invariants':[2]*16,'reduced_multiplier_invariants':[2]*5,
     'selected_defect_coordinates':selected_defect.tolist(),'family_rows':rows,
     'all_assertions_passed':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
np.savez_compressed(Path(__file__).with_suffix('.npz'),**saves)
print('PASS complete binary canonical-family census',flush=True)
