#!/usr/bin/env python3
"""Combine all affine witnesses and verify complete common-refinement shadows.

Retains literal CRT conjugator words and explicit factored central corrections.
Solves both complete gentle norm systems, imposes the exact commutator image,
then substitutes both hexagon words into an independent faithful collector
for the product of the exponent-four and exponent-three class-two groups.
"""
from contextlib import redirect_stdout
from pathlib import Path
import ctypes,io,json,runpy,time
import numpy as np
import sympy as sp

here=Path(__file__).resolve().parent
with redirect_stdout(io.StringIO()):g3=runpy.run_path(str(here/'de_class2_gentle.py'))
with redirect_stdout(io.StringIO()):g2=runpy.run_path(str(here/'de_class2_two_gentle.py'))
d3,d2=g3['d'],g2['d'];v=d3['v'];base=d3['d'];n=97;up=d3['upper'];m3=4656;m2=4753
r3=json.loads((here/'de_fibre_three.json').read_text())['records'];r2=json.loads((here/'de_fibre_two.json').read_text())['records']
assert all(r['replacement_found'] for r in r2+r3)
cert=[r for r in d3['cert'] if 'mod6_beta_cycles' in r];prepared=[]
def from_v(a):
    out=[]
    for c,w in zip(a,base['Nwords']):
        if c>=0:out+=w*int(c)
        else:out+=base['binv'](w)*int(-c)
    return out
for j,rec in enumerate(cert):
    db=(3*np.array(r2[j]['beta_change_mod2'])+4*np.array(r3[j]['beta_change_mod3']))%6
    da=(3*np.array(r2[j]['A_change_mod2'])+4*np.array(r3[j]['A_change_mod3']))%6
    bv=np.array([rec['mod6_beta_cycles'].get(str(i),0) for i in range(n)]);av=np.array([rec['mod6_A_cycles'].get(str(i),0) for i in range(n)])
    b=v['representative'](rec['beta']);a=v['representative'](rec['A'])
    wb=from_v(db)+from_v(bv)+base['Bpaths'][b];wa=from_v(da)+from_v(av)+base['Bpaths'][a]
    pb=v['P'][b]+v['C']@(bv+db);pa=v['P'][a]+v['C']@(av+da)
    gauge=int(np.array([-1,1])@v['fab'](pb))
    prepared.append({'wb':wb,'wa':wa,'pb':pb,'pa':pa,'gauge':gauge,'db':db,'da':da,'a':a,'b':b})

# Full three-primary norm system, independently rebuild all coefficients.
matrix3=np.zeros((m3,m3+24),dtype=np.uint8)
for col,(i,j) in enumerate(zip(*up)):
    vec=np.zeros(m3,dtype=np.int64)
    for a,sign in zip(g3['operators'],g3['signs']):vec+=sign*(np.outer(a[:,i],a[:,j])-np.outer(a[:,j],a[:,i]))[up]
    matrix3[:,col]=vec%3
errors3=[];errors2=[]
matrix2=np.zeros((2*m2+2,m2+48),dtype=np.uint8);matrix2[:,:m2]=g2['original']
for j,rec in enumerate(prepared):
    s0=rec['wb']+[0]+base['binv'](rec['wb'])
    err3=d3['class2']((s0+[0,1])*3);errors3.append(err3);matrix3[:,m3+j]=err3[up]
    for h in range(2):
        err2=d2['kernel_coordinate']((s0+[0,1]*(1+72*h))*3);errors2.append(err2);matrix2[m2:2*m2,m2+2*j+h]=err2
solutions=[]
for p,matrix,mw,gf in ((3,matrix3,m3,d3['gf']),(2,matrix2,m2,d2['gf'])):
    piv=np.zeros(min(matrix.shape),dtype=np.int32);rank=gf(matrix.ctypes.data_as(ctypes.POINTER(ctypes.c_uint8)),*matrix.shape,piv.ctypes.data_as(ctypes.POINTER(ctypes.c_int)))
    pp=piv[:rank].tolist();dom=[i for i in pp if i<mw];rr=len(dom);sols=[]
    for j in range(24):
        choices=[]
        for h in range(1 if p==3 else 2):
            column=mw+j if p==3 else mw+2*j+h
            if np.any(matrix[rr:,column]):continue
            x=np.zeros(mw,dtype=np.int64);x[dom]=matrix[:rr,column]
            if p==3:
                W=np.zeros((n,n),dtype=np.int64);W[up]=x;W=(W-W.T)%3;K=(W-d3['S']@W@d3['S'].T)%3
                assert not np.any((K+d3['S']@K@d3['S'].T)%3)
                assert np.array_equal((K+d3['R']@K@d3['R'].T+g3['R2']@K@g3['R2'].T)%3,errors3[j]);x=K[up]
            else:
                rhs=np.concatenate((np.zeros(m2,dtype=np.int64),errors2[2*j+h],np.zeros(2,dtype=np.int64)))
                assert np.array_equal(g2['original'].astype(np.int64)@x%2,rhs)
            choices.append((1+72*h,x))
        assert choices,('No complete gentle lift',p,j)
        sols.append(choices[0])
    solutions.append(sols);print('Complete norm systems passed at',p,'for all 24 CRT points.',flush=True)

# Explicit basis for the abelian image lattice, used to make f an actual
# commutator word by multiplying it by a fully specified word of J_*.
abel=g2['abel'];ac=g2['abel_coords'];pair_indices=None
for i in range(n):
    for j in range(i+1,n):
        M=sp.Matrix(ac[:,[i,j]].tolist())
        if abs(M.det())==1:pair_indices=(i,j);basis_inverse=np.array(M.inv().tolist(),dtype=np.int64);break
    if pair_indices is not None:break
assert pair_indices is not None

qact={};ci={v['Q'][e]:j for j,e in enumerate(v['chords'])}
def aq(q):
    if q not in qact:qact[q]=v['act'](q,v['C'])[v['chords']]
    return qact[q]
def token_inverse(w):return [('k',-a[1]) if isinstance(a,tuple) else -a for a in reversed(w)]
def word_power(w,k):return w*k if k>=0 else token_inverse(w)*(-k)
def collect(w,k2,k3):
    """Faithful common-quotient collector, including explicit central blocks."""
    q=v['unit'];a2=np.zeros(n,dtype=np.int64);z2=np.zeros((n,n),dtype=np.int64)
    a3=np.zeros(n,dtype=np.int64);z3=np.zeros((n,n),dtype=np.int64)
    K3=np.zeros((n,n),dtype=np.int64);K3[up]=k3;K3=(K3-K3.T)%3
    K2=np.zeros((n,n),dtype=np.int64);K2[up]=k2[n:];K2=(K2+K2.T)%2
    for token in w:
        if isinstance(token,tuple):
            A=aq(q);a2=(a2+2*(A@k2[:n]%2))%4
            zz=(A@(K2+np.diag(k2[:n]))@A.T)%2;z2[up]^=zz[up]
            z3=(z3+token[1]*(A@K3@A.T))%3
            continue
        qn=v['times'](q,v['ss'] if token==0 else v['rr'] if token==1 else v['inverse'](v['rr']))
        gen=[]
        if token:
            if q in ci:gen.append(ci[q]+1)
            if qn in ci:gen.append(-ci[qn]-1)
        for letter in gen:
            i=abs(letter)-1;sign=1 if letter>0 else -1
            z2[i,i+1:]^=a2[i+1:]%2;a2[i]=(a2[i]+sign)%4
            z3[:,i]=(z3[:,i]+2*sign*a3)%3;z3[i,:]=(z3[i,:]-2*sign*a3)%3;a3[i]=(a3[i]+sign)%3
        q=qn
    assert q==v['unit']
    return a2,z2[up],a3,z3[up]

u=[-1,0];vv=[0,-1];x=u*2;y=vv*2;records=[];start=time.time()
for j,(old,rec) in enumerate(zip(cert,prepared)):
    _,k3=solutions[0][j];lam,k2=solutions[1][j];m=(lam-1)//2
    lattice_coeff=ac@k2[:n];assert not np.any(lattice_coeff%2)
    jcoeff=basis_inverse@(-lattice_coeff//2)
    jvec=np.zeros(n,dtype=np.int64);jvec[list(pair_indices)]=12*jcoeff
    jword=from_v(jvec)
    assert not np.any(6*abel@k2[:n]+abel@jvec)
    s0=rec['wb']+[0]+base['binv'](rec['wb']);cg=word_power(x,rec['gauge'])
    f=[0]+cg+s0+[('k',1)]+token_inverse(cg)+jword;fi=token_inverse(f)
    hex1=word_power(u,lam)+fi+word_power(vv,lam)+f+token_inverse(fi+[1]+word_power(x,-m))
    hex2=fi+word_power(vv,lam)+f+word_power(u,lam)+token_inverse(vv+u+word_power(y,-m)+f)
    for w in (hex1,hex2):assert all(not np.any(a) for a in collect(w,k2,k3))
    # Independently verify the CRT base and its gauge in the graph model.
    beta=(rec['b'],rec['pb']%6);aa=(rec['a'],rec['pa']%6)
    ss=(v['ss'],np.zeros(576,dtype=np.int64));rr=(v['rr'],v['Pr']%6)
    assert v['equal'](v['gm'](v['gc'](beta,ss,6),v['gc'](aa,rr,6),6),v['gm'](ss,rr,6))
    edge=rec['pa']-rec['pb'];edge[v['index'][rec['a']]]+=1
    im=v['C'].T@np.stack([v['act'](q,edge) for q in v['Q']]);im=im[:,v['chords']]
    assert all(len(v['rref'](im,p)[1])==97 for p in (2,3))
    row={'certificate_index':j,'missing_coset':bool(old['missing_coset']),'A':old['A'],'beta':old['beta'],
         'lambda_mod144':lam,'m_mod72':m,'integral_cusp_gauge':rec['gauge'],
         'base_beta_word_B':rec['wb'],'base_A_word_B':rec['wa'],
         'beta_change_mod6':rec['db'].tolist(),'A_change_mod6':rec['da'].tolist(),
         'central_square_word_factors':[[i,6*int(c)] for i,c in enumerate(k2[:n]) if c],
         'central_commutator_word_factors':[[int(i),int(l),int(3*c2+4*c3)] for i,l,c2,c3 in zip(*up,k2[n:],k3) if c2 or c3],
         'commutator_adjustment_Jstar_word_factors':[[int(i),int(a)] for i,a in enumerate(jvec) if a],
         'generation_ranks':[97,97],'actual_F_abelianization_zero':True,'both_hexagons_directly_verified':True}
    records.append(row)
    print(json.dumps({k:row[k] for k in ('certificate_index','missing_coset','lambda_mod144','generation_ranks','both_hexagons_directly_verified')}),flush=True)
out={'refinement':'B/(J2 intersect J3)','all_24_CM_fibres_have_explicit_gentle_shadow':True,
     'number_of_hexagons_directly_verified':48,'factored_word_convention':'n_i are zero-indexed Nwords in de_distribution_test.py; [n_i,n_j]=n_i n_j n_i^-1 n_j^-1. k is the listed squares followed by the listed commutators. f=s*x^g*(beta*s*beta^-1)*k*x^-g*j. j is the listed Jstar word.',
     'elapsed_verification_seconds':round(time.time()-start,3),'records':records,
     'scope':'One newly verified finite gentle shadow in each whole admissible CM fibre, including all twelve extra fibres. No full profinite lift is asserted.'}
(here/'de_fibre_crt_verify.json').write_text(json.dumps(out,indent=2)+'\n')
