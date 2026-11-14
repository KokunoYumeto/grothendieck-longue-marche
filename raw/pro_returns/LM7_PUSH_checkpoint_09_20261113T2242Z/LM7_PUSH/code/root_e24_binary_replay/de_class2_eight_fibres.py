#!/usr/bin/env python3
"""All exponent-eight gentle lifts over the 24 affine G6 homology points.

The image of N' N^6 in the class-two exponent-eight quotient is abelian,
isomorphic to (Z/4)^4753 with basis n_i^6 and [n_i,n_j]^3. Therefore the
complete order equations, commutator-image rows and multiplier freedom
are a single exact linear system over Z/4. This tests the whole fibre over
each fixed homology shadow, not one chosen exponent-four correction.
"""
from contextlib import redirect_stdout
from pathlib import Path
import ctypes,io,json,runpy,time
import numpy as np

here=Path(__file__).resolve().parent
with redirect_stdout(io.StringIO()):e=runpy.run_path(str(here/'de_class2_eight.py'))
g=e['g'];d=e['d'];base=e['base'];v=e['v'];n=97;m=4753;mc=m-n;up=e['up'];records=e['records']
ss,rr=v['ss'],v['rr'];r2=v['times'](rr,rr);nw=m+1;nr=2*m+2;start=time.time()
def coeff(w):
    a,z=e['collect'](w);assert not np.any(a%2)
    return 3*np.concatenate((a//2,z))%4
def offblock(q,a):
    A,tau=e['action'](q)
    return (2*tau-A[up[0]]*A[up[1]]+
            2*(a[up[0],None]*A[up[1]]-a[up[1],None]*A[up[0]]))%4
def exterior(A):
    W=np.zeros((mc,mc),dtype=np.uint8)
    for k,(i,j) in enumerate(zip(*up)):
        W[:,k]=(np.outer(A[:,i],A[:,j])-np.outer(A[:,j],A[:,i]))[up]%4
    return W
As,Ar,Ar2=[e['action'](q)[0] for q in (ss,rr,r2)]
Ws,Wr,Wr2=[exterior(A) for A in (As,Ar,Ar2)]
common=np.zeros((nr,nw),dtype=np.uint8)
common[:n,:n]=(np.eye(n,dtype=np.int64)+As)%4
common[m:m+n,:n]=(np.eye(n,dtype=np.int64)+Ar+Ar2)%4
common[n:m,n:m]=Ws
common[m+n:2*m,n:m]=(Wr.astype(np.int64)+Wr2)%4
common[n:m,n:m]=(common[n:m,n:m]+np.eye(mc,dtype=np.uint8))%4
common[m+n:2*m,n:m]=(common[m+n:2*m,n:m]+np.eye(mc,dtype=np.uint8))%4
common[2*m:,:n]=g['abel_coords']%4
def system(rec):
    wb=rec['base_beta_word_B'];fw=base['fword'](wb)
    ab=np.array([sum((1 if c==t else -1 if c==-t else 0) for c in fw) for t in (1,2)])
    gauge=int(ab[1]-ab[0]);cg=e['bpower'](e['x'],gauge)
    # Work before the cusp gauge, so the actions on N_ab are S and R.
    # Conjugating both torsion generators by x^g restores the displayed
    # integral gauge and fixes t; the correction's F^ab is unchanged.
    S=wb+[0]+base['binv'](wb);R=S+e['t']
    aS=e['ncollect'](S+base['binv'](base['Bpaths'][ss]))[0]
    aR=e['ncollect'](R+base['binv'](base['Bpaths'][rr]))[0]
    aR2=e['ncollect'](R*2+base['binv'](base['Bpaths'][r2]))[0]
    mat=common.copy();mat[n:m,:n]=offblock(ss,aS)
    mat[m+n:2*m,:n]=(offblock(rr,aR)+offblock(r2,aR2))%4
    err=coeff(R*3);dlam=(coeff((S+e['t']*73)*3)-err)%4
    assert np.array_equal(coeff((S+e['t']*145)*3),(err+2*dlam)%4)
    mat[m:2*m,-1]=(-dlam)%4;rhs=np.concatenate((np.zeros(m,dtype=np.int64),err,np.zeros(2,dtype=np.int64)))
    return mat,rhs,S,gauge
mat0,rhs0,_,_=system(records[0]);A0=mat0%2
RR,piv=d['rref'](A0);free=[i for i in range(nw) if i not in piv];K=np.zeros((nw,len(free)),dtype=np.int64)
for j,i in enumerate(free):K[i,j]=1;K[piv,j]=RR[:len(piv),i]
print('Z/4 system: binary rank',len(piv),'binary kernel dimension',K.shape[1],flush=True)
# Floating matrix products below are exact integer products: all operands
# are integers of absolute value at most three and every dot product is
# below 2^16, far below the exact-integer range of binary64.
prod=np.rint(mat0.astype(np.float64)@K.astype(np.float64)).astype(np.int64)%4
assert not np.any(prod%2);B0=prod//2
print('Computed the full second-layer obstruction matrix.',flush=True)
result=[];certificate={}
for j,rec in enumerate(records):
    mat,rhs,S,gauge=system(rec);assert np.array_equal(mat%2,A0)
    dif=((mat[:,:n].astype(np.int64)-mat0[:,:n])%4)//2
    dl=((mat[:,-1].astype(np.int64)-mat0[:,-1])%4)//2
    assert not np.any((mat[:,n:m]-mat0[:,n:m])%4)
    B=(B0+np.rint(dif.astype(np.float64)@K[:n].astype(np.float64)).astype(np.int64)+np.outer(dl,K[-1]))%2
    first,pp=d['rref'](np.column_stack((A0,rhs%2)));assert nw not in pp
    x0=np.zeros(nw,dtype=np.int64);x0[pp]=first[:len(pp),-1]
    ax=np.rint(mat.astype(np.float64)@x0.astype(np.float64)).astype(np.int64)%4
    residual=(rhs-ax)%4;assert not np.any(residual%2);residual//=2
    # The variables are y (the even correction) and z (the arbitrary
    # binary nullspace parameter), so this is an exhaustive lifting test.
    lifted=np.column_stack((A0,B,residual));reduced,pp=d['rref'](lifted)
    success=nw+K.shape[1] not in pp
    row={'certificate_index':j,'missing_coset':rec['missing_coset'],'complete_exponent_eight_fibre_nonempty':success,
         'second_system_coefficient_rank':len([i for i in pp if i<lifted.shape[1]-1]),'second_system_augmented_rank':len(pp)}
    if success:
        sol=np.zeros(nw+K.shape[1],dtype=np.int64);sol[pp]=reduced[:len(pp),-1]
        z=sol[nw:];x=(x0+K@z+2*sol[:nw])%4
        assert not np.any((np.rint(mat.astype(np.float64)@x.astype(np.float64)).astype(np.int64)-rhs)%4)
        k=x[:m];h=int(x[-1]);block=(6*k[:n],3*k[n:]);inverse=(-6*k[:n],-3*k[n:])
        assert all(not np.any(c) for c in e['collect']((S+[block])*2))
        assert all(not np.any(c) for c in e['collect'](([inverse]+S+e['t']*(1+72*h))*3))
        row.update({'lambda_mod288':1+72*h,'integral_cusp_gauge':gauge,
                    'correction_Z4_sparse':{str(i):int(c) for i,c in enumerate(k) if c},
                    'both_order_equations_directly_verified':True,'commutator_image_rows_verified':True})
        certificate[f'correction_{j}']=x
    result.append(row);print(json.dumps({k:row[k] for k in ('certificate_index','missing_coset','complete_exponent_eight_fibre_nonempty')}),flush=True)
out={'refinement':'B/((gamma3(N_B) N_B^8) intersect (N_B-prime N_B^3))','base_homology_points':'base conjugators in de_fibre_crt_verify.json',
     'binary_system_rank':len(piv),'binary_kernel_dimension':K.shape[1],
     'pass_counts':[sum(r['complete_exponent_eight_fibre_nonempty'] and r['missing_coset']==c for r in result) for c in (False,True)],
     'elapsed_seconds':round(time.time()-start,3),'records':result,
     'scope':'Exhaustive exact Z/4 linear lifting calculation over each of the 24 fixed affine G6 homology shadows. The entire CM matrix fibres have further homology freedoms not exhausted here.'}
(here/'de_class2_eight_fibres.json').write_text(json.dumps(out,indent=2)+'\n')
np.savez_compressed(here/'de_class2_eight_fibres_certificate.npz',**certificate)
print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2),flush=True)
