"""Bounded actual-word search for the second degree-two direction.

Only short words with all five nonzero critical meridians once and zero
meridian insertions are tested.  A finite Burau quotient rejects them;
any survivor must then pass the faithful Artin check.  No presentation
or kernel-generation conclusion is inferred from this bounded search.
"""
from pathlib import Path
import json,itertools,sys
import numpy as np
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'next_B56'))
from membership_rigid7 import reduce_word as red,inverse as inv,multiply as mul,substitute as sub,artin
j=json.loads((HERE/'cyclic_rigid_braid_words.json').read_text())
braids={r['index']+1:tuple(r['braid']) for r in j['basis']}
p=101;eye=np.eye(6,dtype=np.int64);generators={}
for i in range(1,6):
    M=eye.copy();M[i-1:i+1,i-1:i+1]=[[-1,2],[1,0]]
    N=eye.copy();N[i-1:i+1,i-1:i+1]=[[0,1],[51,51]]
    generators[i]=M%p;generators[-i]=N%p
    assert np.array_equal(generators[i]@generators[-i]%p,eye)
for i in range(1,6):
    for k in range(1,6):
        if abs(i-k)>1:assert np.array_equal(generators[i]@generators[k]%p,generators[k]@generators[i]%p)
        if abs(i-k)==1:assert np.array_equal(generators[i]@generators[k]@generators[i]%p,generators[k]@generators[i]@generators[k]%p)
def braid_matrix(w):
    M=eye.copy()
    for x in w:M=M@generators[x]%p
    return M
matrices={i:braid_matrix(b) for i,b in braids.items()}
matrices.update({-i:braid_matrix(inv(b)) for i,b in braids.items()})
def source_matrix(w):
    M=eye.copy()
    for x in w:M=M@matrices[x]%p
    return M

seen=set();candidates=[];counts={}
for pattern in [(1,),(-1,),(1,1),(-1,-1),(1,-1),(-1,1)]:
    count=0;survivors=0
    for others in itertools.permutations(range(2,7)):
        for places in itertools.combinations(range(5+len(pattern)),len(pattern)):
            g=[];a=b=0
            for k in range(5+len(pattern)):
                if k in places:g.append(pattern[a]);a+=1
                else:g.append(others[b]);b+=1
            g=red(g)
            if g in seen:continue
            seen.add(g);count+=1
            M=source_matrix(g)
            if not np.array_equal(matrices[1]@M%p,M@matrices[1]%p):continue
            survivors+=1;candidates.append(g)
    counts[str(pattern)]={'new_words':count,'finite_survivors':survivors}
    print('Insertion',pattern,': new words',count,'finite survivors',survivors,flush=True)
found=[]
for g in candidates:
    w=mul((1,),g,(-1,),inv(g));b=sub(w,braids);A=artin(b,6)
    identity=A==tuple((i,) for i in range(1,7))
    print('Artin survivor',g,'braid length',len(b),'image lengths',list(map(len,A)),'identity',identity,flush=True)
    if identity:found.append({'g':g,'kernel_word':w,'braid':b,'Artin_images':A})
print('Exact second-direction witnesses:',len(found),flush=True)
(HERE/'second_direction_bounded_search.json').write_text(json.dumps({
    'counts':counts,'finite_survivors':candidates,'exact_witnesses':found,
    'scope':'Only the displayed bounded word family is tested; no general nonexistence or presentation inferred'
},indent=2)+'\n')
