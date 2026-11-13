"""Complete relative mod9 image for E98, with exact inverse digit witnesses."""
from pathlib import Path
from itertools import product
from collections import Counter
import hashlib,json
import numpy as np

HERE=Path(__file__).resolve().parent
source=HERE/'e_global_split7_explore.json'
data=json.loads(source.read_text())
labels=['A0','A1','A2','B0','B1','B2','C1','C2']
blocks=np.array([[[int(x)for x in row]for row in data['coefficient_blocks'][d]]for d in labels],dtype=np.int64)
moduli=np.array(data['moduli'],dtype=np.int64);high=np.flatnonzero(moduli==9)
assert list(moduli)==[3]*18+[9]*12
def solve(A,b):
    m,n=A.shape;E=np.column_stack((A%3,b%3)).copy();piv=[];r=0
    for c in range(n):
        rows=np.flatnonzero(E[r:,c])
        if not len(rows):continue
        k=r+int(rows[0]);E[[r,k]]=E[[k,r]];E[r]=E[r]*int(E[r,c])%3
        for i in range(m):
            if i!=r and E[i,c]:E[i]=(E[i]-int(E[i,c])*E[r])%3
        piv.append(c);r+=1
        if r==m:break
    yes=not np.any(E[r:,-1]);x=np.zeros(n,dtype=np.int64)
    if yes:
        for i,c in enumerate(piv):x[c]=E[i,-1]
    return yes,r,x,E,piv
def kernel(A):
    yes,r,x,E,piv=solve(A,np.zeros(A.shape[0],dtype=np.int64));assert yes
    free=[c for c in range(A.shape[1])if c not in piv]
    N=np.zeros((A.shape[1],len(free)),dtype=np.int64)
    for k,c in enumerate(free):
        N[c,k]=1
        for i,q in enumerate(piv):N[q,k]=-E[i,c]%3
    assert not np.any(A@N%3)
    return N
digits=np.array(list(product(range(3),repeat=8)),dtype=np.int64)
nextblocks=np.tensordot(digits,blocks,axes=(1,0))
records=[];total=0;witnesses=0;hist=Counter()
for v0list in data['eligible_first_digits']:
    v0=np.array(v0list,dtype=np.int64)
    block=np.tensordot(v0,blocks,axes=1)
    yes,rank,x0,_,_=solve(block[:,1:],-block[:,0]);assert yes
    N=kernel(block[:,1:]);F0=block[high,1:];c0=block[high,0]
    Z=kernel(F0.T).T
    assert not np.any((F0@x0+c0)%3) and not np.any((F0@N)%3)
    t0=(F0@x0+c0)//3;Q=F0@N//3
    AA=(np.einsum('am,kmn,nr->kar',Z,nextblocks[:,high,1:],N)+(Z@Q)[None,:,:])%3
    bb=(np.einsum('am,kmn,n->ka',Z,nextblocks[:,high,1:],x0)
        +np.einsum('am,km->ka',Z,nextblocks[:,high,0])+(Z@t0)[None,:])%3
    indices=[];checks=[];ranks=Counter()
    for k in range(len(digits)):
        okay,r,xx,_,_=solve(AA[k],-bb[k]);ranks[(okay,r)]+=1
        if not okay:continue
        indices.append(k)
        p0=x0+N@xx
        defect=t0+Q@xx+nextblocks[k,high,1:]@p0+nextblocks[k,high,0]
        okay2,_,p1,_,_=solve(F0,-defect);assert okay2
        pp=p0+3*p1;full=block+3*nextblocks[k]
        assert not np.any((full[:,1:]@pp+full[:,0])%moduli)
        witnesses+=1
        # Retain an exact horizontal solution for every admissible residue.
        checks.append(pp.tolist())
    finite=block[:,1:4].copy();assert not np.any(finite[high]%3)
    finite[high]//=3
    tor=3-solve(finite,np.zeros(len(moduli),dtype=np.int64))[1]
    rec={'first_digit':v0list,'admissible_second_digits':indices,
         'all_horizontal_witnesses':checks,'horizontal_torsion_dimension':tor,
         'first_solution':x0.tolist(),'first_kernel':N.tolist(),
         'high_rows':block[high,:].tolist(),'high_left_kernel':Z.tolist(),
         'divided_constant':t0.tolist(),'divided_kernel':Q.tolist(),
         'rank_counts':{str(k):v for k,v in ranks.items()}}
    records.append(rec);total+=len(indices);hist[(len(indices),tor)]+=1
    print('first digit',v0list,'second digits',len(indices),'torsion',tor,flush=True)
assert witnesses==total
print('PASS all relative residues modulo9, with',total,'actual inverse witnesses',flush=True)
print('relative first/second/torsion table',dict(hist),flush=True)
out={'status':'PASS','input_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
     'all_first_digits_tested':6561,'admissible_first_digits':len(records),
     'all_second_digits_per_first_digit':6561,'total_relative_mod9_image':total,
     'all_reconstructed_witnesses_checked':witnesses,'relative_image':records,
     'summary':[{'number_of_first_digits':n,'second_digits_each':key[0],
                 'horizontal_torsion_dimension':key[1]}for key,n in sorted(hist.items())]}
HERE.joinpath('e_global_split7_residues.json').write_text(json.dumps(out,indent=2)+'\n')
