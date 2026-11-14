#!/usr/bin/env python3
"""Independent D64 marked-pairing, isometry, retraction and word checks.

No author Python is imported. Frozen arithmetic matrices are input data.
The field operations below use polynomial coefficients, not the author's
lookup tables; binary quotient coordinates are reconstructed by low pivots.
"""
from pathlib import Path
import hashlib,json,itertools
import numpy as np

HERE=Path(__file__).resolve().parent
BASE=HERE.parents[1]/'D64_EXPERIMENTS'
CODE=BASE/'code'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda name:json.loads((CODE/name).read_text())
manifest=json.loads((BASE/'ledger/d_compact_isometry_source_manifest.json').read_text())
for item in manifest['owned_files']+manifest['immutable_inputs']:
    assert sha(BASE/item['path'])==item['sha256'],item['path']

def fbar(a):
    a=np.asarray(a,dtype=np.int64)
    return ((a&1)^((a>>1)&1))|(a&2)
def fmul(a,b):
    a=np.asarray(a,dtype=np.int64);b=np.asarray(b,dtype=np.int64)
    a0,a1=a&1,(a>>1)&1;b0,b1=b&1,(b>>1)&1
    return (a0*b0+a1*b1)%2+2*((a0*b1+a1*b0+a1*b1)%2)
def mat(a,b):
    a=np.asarray(a,dtype=np.int64);b=np.asarray(b,dtype=np.int64)
    a0,a1=a&1,(a>>1)&1;b0,b1=b&1,(b>>1)&1
    return (a0@b0+a1@b1)%2+2*((a0@b1+a1@b0+a1@b1)%2)
def reduce4(a):
    a=np.array(a,dtype=np.int64,copy=True);p=[];r=0
    for c in range(a.shape[1]):
        nz=np.flatnonzero(a[r:,c])
        if not len(nz):continue
        j=r+int(nz[0]);a[[r,j]]=a[[j,r]]
        a[r]=fmul(a[r],fbar(a[r,c]))
        for j in range(len(a)):
            if j!=r and a[j,c]:a[j]^=fmul(a[j,c],a[r])
        p.append(c);r+=1
        if r==len(a):break
    return a,p
def rank4(a):return len(reduce4(a)[1])
def inv4(a):
    n=len(a);m,p=reduce4(np.column_stack((a,np.eye(n,dtype=int))))
    assert p[:n]==list(range(n))
    out=m[:,n:];assert np.array_equal(mat(a,out),np.eye(n,dtype=int))
    return out
def small_section(cusp):
    _,p=reduce4(cusp.T)
    free=[i for i in range(cusp.shape[0]) if i not in p]
    return np.eye(cusp.shape[0],dtype=int)[:,free]
def binary_map(columns,images):
    piv={}
    for v,z in zip(columns,images):
        v=int(v);z=int(z)
        while v:
            k=(v&-v).bit_length()-1
            if k not in piv:piv[k]=(v,z);break
            a,b=piv[k];v^=a;z^=b
        if not v:assert z==0
    def apply(v):
        z=0;v=int(v)
        while v:
            k=(v&-v).bit_length()-1
            assert k in piv,('outside domain',k)
            a,b=piv[k];v^=a;z^=b
        return z
    return apply,len(piv)
def rank2(columns):return binary_map(columns,[0]*len(columns))[1]
def lin(columns,x):
    z=0
    for i,c in enumerate(columns):
        if x>>i&1:z^=int(c)
    return z
def pack_h(a):
    a=np.array(a,dtype=int)
    assert np.array_equal(a,fbar(a.T)) and np.all(a.diagonal()<2)
    out=sum(int(a[i,i])<<i for i in range(len(a)));at=len(a)
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            out|=int(a[i,j])<<at;at+=2
    return out
def unpack_h(x,n=16):
    a=np.zeros((n,n),dtype=int)
    for i in range(n):a[i,i]=(x>>i)&1
    at=n
    for i in range(n):
        for j in range(i+1,n):
            a[i,j]=(x>>at)&3;a[j,i]=int(fbar(a[i,j]));at+=2
    assert pack_h(a)==x
    return a
def exterior(x,b):return pack_h(mat(mat(x,unpack_h(b)),fbar(x.T)))
def mask_matrix(x):return np.array([(x>>(2*i))&3 for i in range(256)]).reshape(16,16)
def pack_matrix(a):return sum(int(x)<<(2*i) for i,x in enumerate(a.ravel()))
def unpack_vector(x,n):return np.array([(x>>(2*i))&3 for i in range(n)],dtype=int)
def pack_vector(a):return sum(int(x)<<(2*i) for i,x in enumerate(a))
def hexes(a):return [int(x,16) for x in a]
def entry(cases,char):return next(x for x in cases if x['character']==char)

N=read('d_residual_compact_norm.json')
P=read('d_residual_compact_pairing.json')
I=read('d_residual_compact_isometry.json')
C=read('d_residual_compact_cusp.json')
R=read('d_residual_compact_coin_action.json')
X=read('d_residual_compact_extension.json')
D=read('d_arithmetic_A4_twisted.json')
Split=read('d_compact_splitting_maps.json')
Aff=read('d_arithmetic_affine_base.json')
Small=read('d_arithmetic_affine_homology.json')
Boundary=read('d_arithmetic_affine_boundary.json')
table=np.array(D['Q_multiplication'],dtype=int)
qlinear=[np.array(a,dtype=int).T for a in Aff['Q_linear_image_matrices']]
ql=np.array([qlinear[i] for i in Aff['Q_to_linear_image']])
vectors=np.array(list(itertools.product(range(3),repeat=4)),dtype=int)
omega=np.array([[(int(x,16)>>i)&1 for x in Small['pairing_columns_mod2']] for i in range(649)],dtype=int)

# Reconstruct the exact integral cycle incidence and half-ribbon form.
def zbar(a):
    a=np.asarray(a,dtype=int)
    return ((a&3)-(a>>2))%4+4*(-(a>>2)%4)
def zmat(a,b):
    a=np.asarray(a,dtype=int);b=np.asarray(b,dtype=int)
    a0,a1=a&3,a>>2;b0,b1=b&3,b>>2
    return (a0@b0-a1@b1)%4+4*((a0@b1+a1@b0-a1@b1)%4)
def zmul(a,b):
    a=np.asarray(a,dtype=int);b=np.asarray(b,dtype=int)
    a0,a1=a&3,a>>2;b0,b1=b&3,b>>2
    return (a0*b0-a1*b1)%4+4*((a0*b1+a1*b0-a1*b1)%4)
def zsub(a,b):return ((a&3)-(b&3))%4+4*(((a>>2)-(b>>2))%4)
def half(a):
    assert not np.any((a&1)|((a>>2)&1))
    return (a&3)//2+2*((a>>2)//2)

pairing_checks=[]
quotient_maps={}
for nr in N['cases']:
    char=nr['character'];pr=entry(P['cases'],char);cr=entry(C['cases'],char)
    src=entry(D['character_blocks'],char);ell=np.array(char,dtype=int)
    u4=np.array(pr['integral_cycle_lifts_mod4_columns'],dtype=int).T
    u0=np.array(src['source_basis_columns'],dtype=int).T
    assert np.array_equal((u4&1)+2*((u4>>2)&1),u0)
    s,r=C['summary']['actual_source_s_state'],C['summary']['actual_source_r_state']
    v2=[min(g,int(table[g,s])) for g in range(576)]
    v3=[min(g,int(table[g,r]),int(table[table[g,r],r])) for g in range(576)]
    rows2=sorted(set(v2));rows3=sorted(set(v3))
    idx2={g:i for i,g in enumerate(rows2)};idx3={g:i+len(rows2) for i,g in enumerate(rows3)}
    phase={};vr=np.array(Aff['affine_r_translation'])
    for g in rows3:
        at=g;ex=0
        for k in range(3):
            phase[at]=[1,4,15][ex%3]
            ex-=int(ell@ql[at]@vr)%3;at=int(table[at,r])
        assert at==g and ex%3==0
    incidence=np.zeros((len(rows2)+len(rows3),576),dtype=int)
    for g in range(576):incidence[idx2[v2[g]],g]=1;incidence[idx3[v3[g]],g]=phase[g]
    assert not np.any(zmat(incidence,u4))
    left=u4[rows3];right=u4[[int(table[g,r]) for g in rows3]]
    powers=np.array([int(ell@ql[g]@vr)%3 for g in rows3])
    first=zmat(left.T,zmul(np.array([1,4,15])[powers,None],zbar(right)))
    second=zmat(right.T,zmul(np.array([1,4,15])[(-powers)%3,None],zbar(left)))
    h=half(zsub(first,second))
    assert np.array_equal(h,np.array(pr['affine_pairing']))
    # The actual 649-dimensional marked small curve, not a chosen isometric model.
    ub=np.array(src['target_basis_columns'],dtype=int).T
    embed=np.zeros((649,8),dtype=int)
    for i,g in enumerate(Small['cycle_chords']):
        q,v=divmod(g,81);z=[1,2,3][-int(ell@vectors[v])%3]
        embed[i]=fmul(z,ub[q])
    assert rank4(embed)==8
    hsmall=mat(mat(embed.T,omega),fbar(embed))
    cusp=np.array(src['target_cusp_columns'],dtype=int).T
    section=small_section(cusp)
    assert np.array_equal(mat(mat(section.T,hsmall),fbar(section)),pr['small_pairing'])
    branch_count=0
    for branch in Boundary['all_cases']:
        ac=branch['solutions'][0]['homology_columns']
        assert all(a['homology_columns']==ac for a in branch['solutions'])
        big=np.array([[(int(x,16)>>i)&1 for x in ac] for i in range(649)],dtype=int)
        expected=next(x for x in pr['small_actions'] if x['branch']==branch['quarter_turn_branch'])
        small=np.array(expected['affine_action_columns'],dtype=int).T
        assert np.array_equal(mat(big,embed),mat(embed,small))
        branch_count+=len(branch['solutions'])
    kn=hexes(nr['kernel_basis']);assert rank2(kn)==240
    target=np.array(pr['M_to_small'],dtype=int)
    assert target.shape==(4,16) and rank4(target)==4
    assert all(pack_h(mat(mat(target,unpack_h(k)),fbar(target.T)))==0 for k in kn)
    relations=[]
    for cols in nr['all_action_columns'].values():
        cols=hexes(cols)
        relations += [lin(cols,k)^k for k in kn]
    free=cr['coinvariant_representatives_in_kernel_basis']
    qmap,domain_rank=binary_map(relations+[kn[j] for j in free],
        [0]*len(relations)+[1<<j for j in range(len(free))])
    assert domain_rank==240 and len(free)==240-rank2(relations)
    quotient_maps[tuple(char)]=qmap
    norms=hexes(nr['all_norm_columns'])
    summed=[0]*256
    for cols in nr['all_action_columns'].values():summed=[a^b for a,b in zip(summed,hexes(cols))]
    assert summed==norms
    assert all(lin(norms,v)==0 for v in relations)
    assert rank2([lin(norms,k) for k in kn])==nr['kernel_self_norm_rank']
    pairing_checks.append({'character':char,'incidence_rows':len(incidence),
        'cycle_columns':u4.shape[1],'all_integral_incidence_and_half_ribbon_entries':True,
        'actual_649_marking_and_all_framings':branch_count,
        'kernel_rank':domain_rank,'coinvariant_dimension':len(free),
        'norm_rank':nr['kernel_self_norm_rank']})

old_checks=[]
for ir in I['cases']:
    char=ir['character'];pr=entry(P['cases'],char);nr=entry(N['cases'],char)
    spl=entry(Split['cases'],char);src=entry(D['character_blocks'],char)
    hm=np.array(pr['M_pairing']);target=np.array(pr['M_to_small'])
    orientation=pack_h(fbar(inv4(hm)))
    flips={x['q_state']:x['flip'] for x in src['all_stabilizer_actions']}
    nk=hexes(nr['kernel_basis']);norms=hexes(nr['all_norm_columns'])
    for case in ir['cases']:
        x=np.array(case['isometry_columns'],dtype=int).T
        small=np.array(next(y for y in pr['small_actions'] if y['branch']==case['branch'])['compact_action_columns']).T
        assert rank4(x)==16
        assert np.array_equal(mat(mat(x.T,hm),fbar(x)),hm)
        assert np.array_equal(mat(target,x),mat(small,target))
        for state,cols in spl['all_complement_actions'].items():
            a=np.array(cols,dtype=int).T
            assert np.array_equal(mat(a,fbar(x) if flips[int(state)] else x),mat(x,a))
        assert exterior(x,orientation)==orientation
        induced=[exterior(x,1<<i) for i in range(256)]
        assert all(lin(norms,v)==lin(induced,norms[i]) for i,v in enumerate(induced))
        assert rank2([lin(induced,k) for k in nk])==240
        old_checks.append({'character':char,'branch':case['branch'],
            'full_semilinear_equations':len(spl['all_complement_actions']),
            'small_square':True,'actual_intersection_and_orientation':True,
            'norm_intertwining_columns':256,'kernel_automorphism_rank':240})

retraction_checks=[]
for rec in R['cases']:
    char=rec['character'];nr=entry(N['cases'],char);pr=entry(P['cases'],char)
    cr=entry(C['cases'],char);qmap=quotient_maps[tuple(char)]
    nk=hexes(nr['kernel_basis']);free=cr['coinvariant_representatives_in_kernel_basis']
    reps=[nk[i] for i in free]
    inclusion=hexes(rec['actual_correction_image_basis'])
    retraction=hexes(rec['retraction_columns'])
    icoord,irank=binary_map(inclusion,[1<<i for i in range(4)])
    assert irank==4 and [lin(retraction,v) for v in inclusion]==[1,2,4,8]
    basis=[mask_matrix(v) for v in hexes(rec['homogeneous_homology_parameter_masks'])]
    assert rank2(hexes(rec['homogeneous_homology_parameter_masks']))==16
    coeffs_checked=0;reconstructed_columns=0
    for case in rec['cases']:
        seed=mask_matrix(int(case['linear_seed_mask'],16))
        def act(x):return [qmap(exterior(x,k)) for k in reps]
        constant=act(seed)
        linear=[[u^v for u,v in zip(act(seed^b),constant)] for b in basis]
        quad=[]
        for i,j in itertools.combinations(range(16),2):
            quad.append((i,j,[a^b^c^d for a,b,c,d in zip(act(seed^basis[i]^basis[j]),constant,linear[i],linear[j])]))
        assert constant==hexes(case['constant_coinvariant_action'])
        assert linear==[hexes(v) for v in case['linear_coinvariant_action_coefficients']]
        assert quad==[(i,j,hexes(v)) for i,j,v in case['quadratic_coinvariant_action_coefficients']]
        for coeff in [constant]+linear+[v for i,j,v in quad]:
            restricted=[icoord(lin(coeff,v)) for v in inclusion]
            assert all(lin(retraction,v)==lin(restricted,retraction[j]) for j,v in enumerate(coeff))
            coeffs_checked+=1;reconstructed_columns+=len(coeff)
    assert coeffs_checked==274
    source=hexes(cr['source_s_correction_columns'])
    retained=[lin(retraction,v) for v in source]
    assert rank2(retained)==4 and all(v==0 for v in hexes(cr['full36_cusp_correction_columns']))
    chosen=next(x for x in X['new_source_s_components'] if x['character']==char)['independent_source_s_correction_indices']
    assert [retained[i] for i in chosen]==[1,2,4,8]
    # On every actual source basis vector, reconstruct the averaged self-wedge.
    inputs=hexes(cr['actual_homology_kernel_basis_columns'])
    s_cols=hexes(cr['actual_source_s_columns']);norm36=hexes(cr['actual_full36_norm_columns'])
    orbit=cr['orbit_size'];mask=(1<<32)-1
    for i,v in enumerate(inputs):
        sv=lin(s_cols,v);nv=lin(norm36,v);sout=tout=0
        for j in range(orbit):
            a=unpack_vector((v>>(32*j))&mask,16)
            b=unpack_vector((sv>>(32*j))&mask,16)
            c=unpack_vector((nv>>(32*j))&mask,16)
            wh=pack_h(fmul(a[:,None],fbar(b[None,:]))^fmul(b[:,None],fbar(a[None,:])))
            th=pack_h(fmul(a[:,None],fbar(c[None,:]))^fmul(c[:,None],fbar(a[None,:])))
            sout^=qmap(wh);tout^=qmap(th)
        assert sout==source[i] and tout==0
    retraction_checks.append({'character':char,'retraction_columns':[hex(v) for v in retraction],
        'all_action_coefficients_independently_reconstructed':coeffs_checked,
        'coefficient_columns':reconstructed_columns,'right_inverse':True,
        'simultaneous_kernel_invariance':True,'kernel_dimension':6,
        'actual_source_basis_wedges_reconstructed':len(inputs),
        'selected_actual_indices':chosen,'selected_images':[1,2,4,8]})

# Full class-two word identities, in the degree-two integral Magnus algebra.
def gen(n,i):
    a=np.zeros(n,dtype=object);a[i]=1
    return a,np.zeros((n,n),dtype=object)
def multiply(x,y):return x[0]+y[0],x[1]+y[1]+np.outer(x[0],y[0])
def inverse(x):return -x[0],-x[1]+np.outer(x[0],x[0])
def product(xs):
    n=len(xs[0][0]);z=(np.zeros(n,dtype=object),np.zeros((n,n),dtype=object))
    for x in xs:z=multiply(z,x)
    return z
def commutator(x,y):return product([x,y,inverse(x),inverse(y)])
u=[gen(37,i) for i in range(36)];c=gen(37,36)
b=product(u);shift=product(u[1:]+[product([c,u[0],inverse(c)])])
lhs=multiply(b,inverse(shift))
rhs=multiply(commutator(u[0],product(u[1:])),inverse(commutator(c,u[0])))
assert all(np.array_equal(a,b) for a,b in zip(lhs,rhs))
a,b=gen(2,0),gen(2,1)
lhs=multiply(multiply(a,b),inverse(multiply(b,a)))
assert all(np.array_equal(x,y) for x,y in zip(lhs,commutator(a,b)))

result={'status':'PASS','scope':'Independent marked comparison, all simultaneous retraction coefficients and actual source-word checks; no author Python imports and no full six-program replay claimed.',
 'frozen_proof_sha256':sha(BASE/manifest['section']),
 'manifest_sha256':sha(BASE/'ledger/d_compact_isometry_source_manifest.json'),
 'manifest_hashes_checked':len(manifest['owned_files'])+len(manifest['immutable_inputs']),
 'integral_pairing_and_marking':pairing_checks,
 'old_projective_isometries':old_checks,
 'simultaneous_retractions':retraction_checks,
 'integral_Magnus_source_s_identity':True,'integral_Magnus_full36_wrap_identity':True,
 'new_quotient_dimension':1920+4+4+2,'new_quotient_coinvariants':4+4+4+2,
 'remaining_specified_dimension':284160-1930,
 'post_word_moving_correction':'Requires the explicit reviewed post-word augmentation step in (1-e_Delta)K; independent proof audit records the actual source lift through R50 intersect Lstar2.'}
text=json.dumps(result,indent=2)+'\n'
(HERE/'focused_maps.json').write_text(text)
print(text,end='')
