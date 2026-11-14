#!/usr/bin/env python3
"""Independent focused D54 coefficient, matrix, and square-module audit.

This does not claim to rerun the three author's full-word programs.
It reads their frozen coefficient certificates, recomputes all stated
finite homology comparisons by separate algorithms, and checks the
square-module formula in a complete three-generator free group model.
"""
from pathlib import Path
from collections import deque
import json,hashlib,itertools

ROOT=Path(__file__).resolve().parents[2]
SRC=ROOT/'D54_EXPERIMENTS/code'
OUT=Path(__file__).resolve().parent
names=['d_cm_full_class2_search.json','d_cm_same_action_obstruction.json',
       'd_cm_reduced_invariant_equations.json','d_cm_invariant_zero_loci.json',
       'd_cm_doubled_class2.json','d_class2_diagnostic.json']
data={n:json.loads((SRC/n).read_text()) for n in names}
full,same,reduced,zeros,doubled,diagnostic=(data[n] for n in names)

def linear(cols,mask):
    out=0
    while mask:
        bit=mask&-mask;out^=cols[bit.bit_length()-1];mask^=bit
    return out

def echelon(cols):
    piv={};dependencies=[]
    for j,col in enumerate(cols):
        value=col;word=1<<j
        while value:
            p=value.bit_length()-1
            if p not in piv:piv[p]=(value,word);break
            a,b=piv[p];value^=a;word^=b
        if not value:dependencies.append(word)
    def reduce(value):
        word=0
        for p in sorted(piv,reverse=True):
            if value>>p&1:
                a,b=piv[p];value^=a;word^=b
        return value,word
    return reduce,len(piv),dependencies

def poly(mask,lin,quad):
    active=[i for i in range(len(lin)) if mask>>i&1]
    val=0
    for k,i in enumerate(active):
        val^=lin[i]
        for j in active[k+1:]:val^=quad[min(i,j)][max(i,j)]
    return val

ol=full['linear_obstruction_coefficients'];oq=full['quadratic_obstruction_coefficients']
K=[int(x,16) for x in same['s_fixed_parameter_basis']+same['r_fixed_parameter_basis']]
comp=[int(x,16) for x in reduced['homology_complement_parameter_masks']]
k_reduce,k_rank,_=echelon(K)
all_reduce,all_rank,_=echelon(K+comp)
assert len(K)==k_rank==102 and all_rank==120 and len(comp)==18
polar_checks=0
for k in K:
    for j in range(120):
        v=0
        for i in range(120):
            if i!=j and k>>i&1:v^=oq[min(i,j)][max(i,j)]
        assert v==0
        polar_checks+=1
Kobs=[poly(k,ol,oq) for k in K]
ko_reduce,ko_rank,_=echelon(Kobs)
assert ko_rank==4
lin=[ko_reduce(poly(c,ol,oq))[0] for c in comp]
quad=[[0]*18 for _ in range(18)]
for i in range(18):
    for j in range(i+1,18):
        quad[i][j]=ko_reduce(poly(comp[i]^comp[j],ol,oq))[0]^lin[i]^lin[j]
assert lin==reduced['reduced_linear_obstruction_coefficients']
assert quad==reduced['reduced_quadratic_obstruction_coefficients']
print('PASS 12240 kernel-polar equations, exact102/18 split and rank4 boundary image',flush=True)

n=181
Ds=[[int(x,16) for x in row] for row in reduced['full_homology_derivation_columns']]
Omega=[int(x,16) for x in diagnostic['pairing_columns_mod2']]
assert all(not(Omega[i]>>i&1) for i in range(n))
assert all((Omega[i]>>j&1)==(Omega[j]>>i&1) for i in range(n) for j in range(n))
offset=[i*(2*n-i-1)//2 for i in range(n)]
OD=[[linear(Omega,c) for c in d] for d in Ds]
def odd(a):return a.bit_count()&1
pl=[];pq=[[0]*18 for _ in range(18)]
for k in range(18):
    ans=0
    for i in range(n):
        for j in range(i+1,n):
            v=odd(Ds[k][i]&Omega[j])^odd(Omega[i]&Ds[k][j])^odd(Ds[k][i]&OD[k][j])
            if v:ans|=1<<(offset[i]+j-i-1)
    pl.append(ans)
for k in range(18):
    for l in range(k+1,18):
        ans=0
        for i in range(n):
            for j in range(i+1,n):
                if odd(Ds[k][i]&OD[l][j])^odd(Ds[l][i]&OD[k][j]):
                    ans|=1<<(offset[i]+j-i-1)
        pq[k][l]=ans
assert pl==[int(x,16) for x in reduced['pairing_linear_coefficients']]
assert pq==[[int(x,16) for x in row] for row in reduced['pairing_quadratic_coefficients']]
ocols=lin+[quad[i][j] for i in range(18) for j in range(i+1,18)]
pcols=pl+[pq[i][j] for i in range(18) for j in range(i+1,18)]
_,orank,ok= echelon(ocols)
psolve,prank,pk=echelon(pcols)
assert orank==prank==9
witness=next((k for k in ok if linear(pcols,k)),None)
if witness is None:
    witness=next(k for k in pk if linear(ocols,k));witness_side='pairing_relation'
else:witness_side='obstruction_relation'
plc=[psolve(v)[1] for v in pl]
pqc=[[psolve(v)[1] for v in row] for row in pq]
# Gray-code traversal uses the derivative at the preceding point.
old=vo=vp=0;oset={0};pset={0}
for counter in range(1,1<<18):
    current=counter^(counter>>1);flip=current^old;j=flip.bit_length()-1
    do=lin[j];dp=plc[j]
    rest=old&~flip
    while rest:
        bit=rest&-rest;i=bit.bit_length()-1
        do^=quad[min(i,j)][max(i,j)];dp^=pqc[min(i,j)][max(i,j)];rest^=bit
    vo^=do;vp^=dp
    if vo==0:oset.add(current)
    if vp==0:pset.add(current)
    old=current
assert oset==pset=={int(x,16) for x in reduced['exact_homology_solution_parameters']}
assert len(oset)==864
print('PASS all171 pairing coefficients, distinct coefficient spans and262144-point equal864 zero loci',flush=True)

flat=[sum(c<<(n*j) for j,c in enumerate(d)) for d in Ds]
dsolve,drank,_=echelon(flat);assert drank==18
matrices={}
repairs=reduced['all_corrected_full_pair_parameter_masks']
for m,r in zip(sorted(oset),repairs):
    r=int(r,16);assert poly(r,ol,oq)==0
    assert k_reduce(r^linear(comp,m))[0]==0
    T=[(1<<j)^linear([d[j] for d in Ds],m) for j in range(n)]
    assert echelon(T)[1]==n
    matrices[m]=T
gens=[int(x,16) for x in reduced['summary']['group_generators']]
assert gens==[0x368,0x37e,0x3c9,0x635,0x80a]
seen={0};todo=deque([0]);products=0
while todo:
    v=todo.popleft()
    for g in gens:
        cols=[linear(matrices[v],c)^(1<<j) for j,c in enumerate(matrices[g])]
        rem,mask=dsolve(sum(c<<(n*j) for j,c in enumerate(cols)))
        assert rem==0 and mask in oset
        products+=1
        if mask not in seen:seen.add(mask);todo.append(mask)
assert seen==oset and products==4320
selected=int(doubled['summary']['selected_doubled_parameter'],16)
rem,decomp=all_reduce(selected);assert rem==0
selected_hom=decomp>>102
Dsel=[linear([d[j] for d in Ds],selected_hom) for j in range(n)]
assert Dsel==[int(x,16) for x in doubled['selected_mod4_divided_homology_columns']]
assert echelon(Dsel)[1]==16
Aa=Ac=Ba=Bc=0
for record in doubled['all120_exact_square_module_lifts']:
    if selected>>record['basis_parameter']&1:
        Aa^=int(record['A_square_coordinates'],16);Ac^=int(record['A_central_coordinates'],16)
        Ba^=int(record['beta_square_coordinates'],16);Bc^=int(record['beta_central_coordinates'],16)
assert [Aa,Ac,Ba,Bc]==[int(doubled[k],16) for k in
    ['selected_A_square_coordinates','selected_A_central_coordinates',
     'selected_beta_square_coordinates','selected_beta_central_coordinates']]
print('PASS all864 repaired parameters/ranks,4320 actual matrix products and doubled rank16 transport',flush=True)

# Complete rank-three free class-two exponent-four group.
pairs=[(0,1),(0,2),(1,2)]
def gm(x,y):
    a,c=x;b,d=y;e=c^d
    for k,(i,j) in enumerate(pairs):
        if a[j]*b[i]%2:e^=1<<k
    return tuple((a[i]+b[i])%4 for i in range(3)),e
unit=((0,0,0),0)
generators=[(tuple(int(i==j) for i in range(3)),0) for j in range(3)]
def power(x,k):
    y=unit
    for _ in range(k):y=gm(y,x)
    return y
def comm(x,y):return gm(gm(gm(x,y),power(x,3)),power(y,3))
def ordered(v):
    ans=unit
    for i in range(3):
        if v>>i&1:ans=gm(ans,generators[i])
    return ans
def wedge3(a,b):
    return sum(((((a>>i)&1)*((b>>j)&1)^((a>>j)&1)*((b>>i)&1))<<k)
               for k,(i,j) in enumerate(pairs))
square_checks=0
for cols in itertools.product(range(8),repeat=3):
    if echelon(cols)[1]!=3:continue
    images=[ordered(v) for v in cols]
    wc=[wedge3(cols[i],cols[j]) for i,j in pairs]
    qc=[sum((((v>>i)&1)*((v>>j)&1))<<k for k,(i,j) in enumerate(pairs)) for v in cols]
    for v,c in itertools.product(range(8),repeat=2):
        actual=unit
        for i in range(3):
            if v>>i&1:actual=gm(actual,power(images[i],2))
        for k,(i,j) in enumerate(pairs):
            if c>>k&1:actual=gm(actual,comm(images[i],images[j]))
        target=(tuple(2*((linear(cols,v)>>i)&1) for i in range(3)),linear(wc,c)^linear(qc,v))
        assert actual==target
        square_checks+=1
assert square_checks==168*64
print('PASS10752 complete free-class-two square-module action identities',flush=True)

result={'status':'PASS','scope':'Complete proof/all three author programs read; independently recomputed frozen finite coefficient/matrix data and universal square-module formula. Root owns full three-program and long-word reruns.',
 'input_sha256':{name:hashlib.sha256((SRC/name).read_bytes()).hexdigest() for name in names},
 'same_action_rank':102,'homology_parameter_rank':18,'kernel_polar_checks':polar_checks,
 'kernel_obstruction_rank':4,'pairing_coefficients_checked':171,
 'different_coefficient_spans_witness':{'side':witness_side,'monomial_relation':hex(witness),
    'obstruction_value':linear(ocols,witness),'pairing_value':hex(linear(pcols,witness))},
 'zero_locus_points_checked':1<<18,'same_zero_locus_size':864,
 'repaired_full_parameters_checked':864,'invertible_homology_matrices_checked':864,
 'actual_group_products_checked':products,'doubled_transport_rank':16,
 'square_module_literal_group_checks':square_checks}
OUT.joinpath('a_d54_matrix_audit.json').write_text(json.dumps(result,indent=2)+'\n')
