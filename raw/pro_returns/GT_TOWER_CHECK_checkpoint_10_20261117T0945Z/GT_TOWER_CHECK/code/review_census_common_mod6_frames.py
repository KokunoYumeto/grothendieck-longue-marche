#!/usr/bin/env python3
"""Exact necessary finite census in the actual eight-map common source.

Full source torsion-frame equations are imposed, including A^ab=0.
Survival is not asserted to be a full profinite gentle lift.
"""
from pathlib import Path
import json
import sys
from collections import Counter
import numpy as np

HERE=Path(__file__).resolve().parent.parent/'centralizer_code'
TOWER=HERE.parent/'tower_code'
GHOST=HERE.parent/'ghost_code'
sys.path.insert(0,str(TOWER))
src=(TOWER/'test_fivepoint_cm_level.py').read_text()
ns={'__name__':'common_mod6_prefix','__file__':str(HERE/'common_mod6_prefix.py')}
exec(compile(src.split('records=[];base_records=[]',1)[0],str(TOWER/'test_fivepoint_cm_level.py'),'exec'),ns)

jt=ns['jtable']; jgen=ns['jgens']; jp=ns['jpaths']; jl=ns['jloops']
jch=ns['jchords']; jci={tuple(e):i for i,e in enumerate(jch)}
jinv=ns['jinverse']; inverse=ns['inverse']; subst=ns['subst']
ab=ns['abloops'].T.astype(np.int64)
assert ab.shape==(289,2)
SX=((2,),(1,)); RX=((2,),(-2,-1))

def chain(w):
    q=0;v=np.zeros(289,dtype=np.int64)
    for a in w:
        k=abs(a)-1
        if a>0:
            e=(q,k);q=int(jt[q,jgen[k]]);sign=1
        else:
            q=int(jt[q,jinv[jgen[k]]]);e=(q,k);sign=-1
        if e in jci:v[jci[e]]+=sign
    return q,v

def exponents(w):
    return np.array([sum((1 if j==k else -1 if j==-k else 0) for j in w)
                     for k in (1,2)],dtype=np.int64)

def proj(rows,p):
    # This routine returns an exact right annihilator of the row space.
    return ns['row_space_projection'](np.asarray(rows,dtype=np.int64),p)

def affine_solve(A,B,p):
    A=np.asarray(A,dtype=np.int64).copy()%p
    B=np.asarray(B,dtype=np.int64).copy()%p
    if B.ndim==1:B=B[:,None]
    original_A=A.copy();original_B=B.copy()
    piv=[];row=0
    for col in range(A.shape[1]):
        nz=np.flatnonzero(A[row:,col])
        if not len(nz):continue
        k=row+int(nz[0]);A[[row,k]]=A[[k,row]];B[[row,k]]=B[[k,row]]
        u=pow(int(A[row,col]),-1,p);A[row]=A[row]*u%p;B[row]=B[row]*u%p
        nz=np.flatnonzero(A[:,col]);nz=nz[nz!=row]
        c=A[nz,col,None].copy();A[nz]=(A[nz]-c*A[row])%p;B[nz]=(B[nz]-c*B[row])%p
        piv.append(col);row+=1
        if row==A.shape[0]:break
    good=~np.any(B[row:],axis=0)
    points=np.zeros((A.shape[1],B.shape[1]),dtype=np.int64)
    points[piv]=B[:row]
    free=[j for j in range(A.shape[1]) if j not in piv]
    basis=np.zeros((len(free),A.shape[1]),dtype=np.int64)
    for i,col in enumerate(free):
        basis[i,col]=1;basis[i,piv]=-A[:row,col]%p
    assert not np.any(original_A@basis.T%p)
    assert not np.any((original_A@points[:,good]-original_B[:,good])%p)
    return row,good,points,basis

data={}
archive={}
for p,name in [(2,'binary'),(3,'signed')]:
    z=np.load(GHOST/f'check_fivepoint_{name}_module.npz')
    P=z['common_projection'].astype(np.int64)
    assert P.shape==(289,97)
    assert np.array_equal(z['source_table'],jt)
    assert np.array_equal(z['source_generators'],jgen)
    assert np.array_equal(z['source_chords'],jch)
    for mat,images in [(z['source_s'],SX),(z['source_r'],RX)]:
        check=np.array([chain(subst(w,images))[1] for w in jl])%p
        assert np.array_equal(check,mat%p)
    data[p]={'P':P,'L':z['projection_left_inverse'].astype(np.int64),
             'S':z['source_s'].astype(np.int64),
             'R':z['source_r'].astype(np.int64),
             'bs':z['base_s'],'br':z['base_r']}
print('PASS exact common-source matrices and all578 source automorphism words per prime',flush=True)

def base_q(i):
    q,_=ns['b_eval'](subst(jp[i],(ns['bx'],ns['by'])),2)
    return q

baseQ=[base_q(i) for i in range(288)]
records=[];summaries=[]
for base in sorted(ns['derived']):
    qf=ns['Q'][ns['JQ'][base][4]]
    frames=[f for f in ns['frames'] if f['qf']==qf]
    if not frames:continue
    candidates=[]
    for fr in frames:
        bs=[];ars=[]
        for b in range(288):
            if baseQ[b]!=fr['qb']:continue
            if int(data[2]['bs'][b])!=int(jt[base,b]):continue
            eb=exponents(jp[b])
            # beta^ab=(-rho,-rho), and rho is even on the full H.
            if np.any(eb%2) or np.any((eb+fr['rho'])%3):continue
            bs.append(b)
        for a in range(288):
            if baseQ[a]!=fr['qa']:continue
            if int(data[2]['br'][a])!=int(jt[base,a]):continue
            if np.any(exponents(jp[a])%6):continue
            ars.append(a)
        for b in bs:
            for a in ars:candidates.append((fr,b,a))
    if not candidates:continue
    per_prime={}
    all_good=np.ones(len(candidates),dtype=bool)
    for p in (2,3):
        d=data[p];P=d['P']
        # Literal conjugation by the fixed base word, on all source loops.
        Ad=np.array([chain(jp[base]+w+inverse(jp[base]))[1] for w in jl])%p
        SM=(d['S']-Ad)@P%p
        RM=(d['R']-Ad)@P%p
        _,Ps=proj(SM,p)
        _,Pr=proj(np.hstack((RM,ab)),p)
        Ap_s=(P@Ps%p).T
        Ap_r=(np.hstack((P,np.zeros((289,2),dtype=np.int64)))@Pr%p).T
        matrices=[];rhs=[];valid=True
        for name,tokens in ns['expressions'].items():
            eq=ns['expression_matrix'](base,tokens,p)
            if eq is None:valid=False;break
            matrices.append(eq[0]);rhs.append(eq[1])
        if not valid:break
        matrices.append(ab.T%p)
        rhs.append(-ns['abelian_base_coordinates'](base)%p)
        fixed=np.concatenate(rhs)
        matrices.extend((Ap_s,Ap_r))
        AA=np.vstack(matrices).astype(np.int64)%p
        BB=[]
        for fr,b,a in candidates:
            qb,vs=chain(subst(jp[b],SX));qc,cs=chain(jp[base]+jp[b])
            assert qb==qc
            ds=(vs-cs)@P%p
            qa,vr=chain(subst(jp[a],RX));qd,cr=chain(jp[base]+jp[a])
            assert qa==qd
            dr=(vr-cr)@P%p
            ea=exponents(jp[a]);assert not np.any(ea%6)
            b_s=ds@Ps%p
            b_r=np.concatenate((dr,ea//6))@Pr%p
            BB.append(np.concatenate((fixed,b_s,b_r)))
        BB=np.array(BB,dtype=np.int64).T
        A97=AA@d['L'].T%p
        assert np.array_equal(A97@P.T%p,AA)
        rank,good,points,kernel=affine_solve(A97,BB,p)
        rawrank,rawgood=ns['solve_many'](AA,BB,p)
        assert rank==rawrank and np.array_equal(good,rawgood)
        assert kernel.shape==(97-rank,97)
        key=f'b{base}_p{p}'
        archive[key+'_A97']=A97
        archive[key+'_rhs']=BB
        archive[key+'_particular']=points
        archive[key+'_nullspace']=kernel
        archive[key+'_base_frames']=np.array([[b,a] for _,b,a in candidates])
        archive[key+'_SM']=SM
        archive[key+'_RM']=RM
        for i,(fr,b,a) in enumerate(candidates):
            if not good[i]:continue
            ds=(chain(subst(jp[b],SX))[1]-chain(jp[base]+jp[b])[1])@P%p
            dr=(chain(subst(jp[a],RX))[1]-chain(jp[base]+jp[a])[1])@P%p
            us=d['L']@SM%p
            ur=d['L']@np.hstack((RM,ab))%p
            _,gs,ps,_=affine_solve(us.T,points[:,i]-ds,p)
            _,gr,pr,_=affine_solve(ur.T,np.concatenate((points[:,i]-dr,-exponents(jp[a])//6)),p)
            assert gs[0] and gr[0]
            archive[key+f'_beta_{i}']=ps[:,0]
            archive[key+f'_A_{i}']=pr[:,0]
        all_good &=good
        per_prime[p]={'rank':rank,'free_raw_dimensions':289-rank,
                      'free_common_dimensions':97-rank,
                      'rows':len(AA),'passing':int(np.count_nonzero(good)),
                      's_frame_image_rank':97-Ps.shape[1],
                      'r_frame_augmented_rank':99-Pr.shape[1]}
    if not valid:continue
    for okay,(fr,b,a) in zip(all_good,candidates):
        if okay:
            rec=dict(fr);rec.update(base=base,beta_base=b,A_base=a)
            rec['free_raw_dimensions']={str(p):per_prime[p]['free_raw_dimensions'] for p in (2,3)}
            rec['free_common_dimensions']={str(p):per_prime[p]['free_common_dimensions'] for p in (2,3)}
            records.append(rec)
    summaries.append({'base':base,'candidate_count':len(candidates),
                      'passing_count':int(np.count_nonzero(all_good)),
                      'prime_constraints':per_prime})
    print('BASE',base,'actual base-frame candidates',len(candidates),
          'ranks',[per_prime[p]['rank'] for p in (2,3)],
          'passes',int(np.count_nonzero(all_good)),flush=True)

hist=dict(Counter(r['parity'] for r in records))
out={'scope':'Complete necessary actual common-source frame census; no full profinite lift is inferred.',
     'source':'B/((Kprime K^6) intersection Fprime F^36)',
     'pure_source_order':'288*6^97','full_source_order':'1728*6^97',
     'target':'Gamma05/(Nprime N^6)','target_order':'192*6^102',
     'base_summaries':summaries,'records':records,'parity_counts':hist,
     'all_assertions_passed':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
np.savez_compressed(Path(__file__).with_suffix('.npz'),**archive)
print('COMPLETE actual common-source frame parity counts',hist,flush=True)
print('Surviving records are not asserted to lift to a full profinite gentle element.',flush=True)
