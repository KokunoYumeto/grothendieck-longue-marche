#!/usr/bin/env python3
"""Complete exponent-sixteen fibres over the E.11 affine G6 points.

At exponent eight the correction group is (Z/4)^4753.  Its homogeneous
solutions have 801 lower binary parameters and 827 upper ones.  Only 15
lower parameters affect homology.  At exponent sixteen all the other
parameters enter linearly, while those 15 enter quadratically.  This
program retains the entire linear system and enumerates all 2**15 choices.
"""
from contextlib import redirect_stdout
from pathlib import Path
import argparse,io,json,runpy,time
import numpy as np
from de_class2_two_power import TwoPowerCollector

parser=argparse.ArgumentParser()
parser.add_argument('--indices',default='all')
args=parser.parse_args()
here=Path(__file__).resolve().parent
with redirect_stdout(io.StringIO()):e=runpy.run_path(str(here/'de_class2_eight_fibres.py'))
g=e['g'];d=e['d'];base=e['base'];v=e['v'];n=97;m=4753;nw=m+1;nr=2*m+2
c=TwoPowerCollector(4,e['e']);up=c.up;mc=m-n
K=e['K'];A0=e['A0'];rank0=len(e['piv']);hrows=np.r_[np.arange(n),m]
saved8=np.load(here/'de_class2_eight_fibres_certificate.npz')
records=e['records'];indices=list(range(24)) if args.indices=='all' else list(map(int,args.indices.split(',')))
if globals().get('DE_LOAD_ONLY',False):indices=[]
start=time.time();literal_checks=c.literal_checks()

def mm(A,B,mod):
    # All entries are bounded integers and every dot product here is below
    # 2**24. Binary64 therefore computes the integer matrix product exactly.
    return np.rint(A.astype(np.float64)@B.astype(np.float64)).astype(np.int64)%mod

def coeff(pair):
    a,z=pair;assert not np.any(a%2)
    return 3*np.concatenate((a//2,z))%8

def block(x):
    return 6*x[:n]%16,3*x[n:m]%8

def mul(x,y):
    return np.concatenate(((x[:n]+y[:n])%8,
           (x[n:]+y[n:]-12*np.outer(y[:n],x[:n])[up])%8))

def inv(x):
    return np.concatenate((-x[:n]%8,(-x[n:]-12*np.outer(x[:n],x[:n])[up])%8))

def power(x,h):
    return np.concatenate((h*x[:n]%8,
           (h*x[n:]-12*(h*(h-1)//2)*np.outer(x[:n],x[:n])[up])%8))

r2=v['times'](v['rr'],v['rr'])
As,Ar,Ar2=[c.action(q)[0] for q in (v['ss'],v['rr'],r2)]
central=np.zeros((nr,mc),dtype=np.uint8)
for j,(a,b) in enumerate(zip(*up)):
    ws=(np.outer(As[:,a],As[:,b])-np.outer(As[:,b],As[:,a]))[up]
    wr=(np.outer(Ar[:,a],Ar[:,b])-np.outer(Ar[:,b],Ar[:,a])+
        np.outer(Ar2[:,a],Ar2[:,b])-np.outer(Ar2[:,b],Ar2[:,a]))[up]
    ws[j]+=1;wr[j]+=1
    central[n:m,j]=ws%8;central[m+n:2*m,j]=-wr%8
cusp=coeff(c.collect(e['e']['t']*72));H=g['abel_coords']

def setup(rec):
    wb=rec['base_beta_word_B'];S=wb+[0]+base['binv'](wb);R=S+e['e']['t']
    aS=c.ncollect(S+base['binv'](base['Bpaths'][v['ss']]))[0]
    aR=c.ncollect(R+base['binv'](base['Bpaths'][v['rr']]))[0]
    aR2=c.ncollect(R*2+base['binv'](base['Bpaths'][r2]))[0]
    E=coeff(c.collect(R*3))
    def act(q,a,x):
        aa,zz=c.acted(q,*block(x))
        zz=(zz+np.outer(a,aa)[up]-np.outer(aa,a)[up])%8
        return coeff((aa,zz))
    def F(x):
        x=np.asarray(x,dtype=np.int64)%8;k=x[:m];h=int(x[-1])
        es=mul(act(v['ss'],aS,k),k)
        w=mul(inv(k),act(v['rr'],aR,power(cusp,h)))
        er=mul(mul(mul(w,act(v['rr'],aR,w)),act(r2,aR2,w)),E)
        return np.concatenate((es,er,H@k[:n]%8))
    def direct(x):
        k=x[:m];h=int(x[-1]);kb=block(k)
        es=coeff(c.collect((S+[kb])*2))
        er=coeff(c.collect(([c.inverse(kb)]+S+e['e']['t']*(1+72*h))*3))
        return np.concatenate((es,er,H@k[:n]%8))
    return F,direct,S

results=[];certificates={};rng=np.random.default_rng(212026)
for ix in indices:
    rec=records[ix];M,rhs,S,gauge=e['system'](rec)
    MK=mm(M,K,4);assert not np.any(MK%2);B=MK//2
    rr,piv=d['rref'](np.column_stack((A0,B)))
    rank2=len(piv);obs=rr[rank0:rank2,nw:]
    Z=d['nullspace'](obs).astype(np.int64)
    Y=np.zeros((nw,Z.shape[1]),dtype=np.int64)
    Y[e['piv']]=mm(rr[:rank0,nw:],Z,2)
    V=(mm(K,Z,4)+2*Y)%4
    assert not np.any(mm(M,V,4))
    uh=V[hrows]%2;ur,selected=d['rref'](uh);hdim=len(selected)
    assert hdim==15 and Z.shape[1]==801
    other=[j for j in range(V.shape[1]) if j not in selected]
    small=V[:,selected]
    rest=(V[:,other]-small@ur[:hdim,other].astype(np.int64))%4
    assert not np.any(rest[hrows]%2)
    directions=np.column_stack((2*K,rest))
    assert not np.any(directions[hrows]%2)
    F,direct,S=setup(rec);zero=np.zeros(nw,dtype=np.int64);fzero=F(zero)
    x0=saved8[f'correction_{ix}'].astype(np.int64)
    fbase=F(x0);assert not np.any(fbase%4)
    for check in range(2):
        x=rng.integers(0,8,size=nw)
        assert np.array_equal(F(x),direct(x));literal_checks+=1
    D=np.zeros((nr,nw),dtype=np.uint8);D[:,n:m]=central
    for j in list(range(n))+[m]:
        x=zero.copy();x[j]=2;D[:,j]=(F(x)-fzero)%8
    coords=directions.copy();coords[hrows]//=2
    defects=mm(D,coords,8)
    assert not np.any(defects%4)
    linear=np.column_stack((A0,defects//4)).astype(np.uint8)
    npairs=hdim*(hdim-1)//2
    polys=np.zeros((nr,1+hdim+npairs),dtype=np.uint8)
    polys[:,0]=fbase//4
    vals=[]
    for j in range(hdim):
        fj=F(x0+small[:,j]);assert not np.any(fj%4)
        vals.append(fj);polys[:,1+j]=((fj-fbase)%8)//4
    pairs=[]
    for j in range(hdim):
        for k in range(j+1,hdim):
            f=F(x0+small[:,j]+small[:,k])
            delta=(f-vals[j]-vals[k]+fbase)%8;assert not np.any(delta%4)
            polys[:,1+hdim+len(pairs)]=delta//4;pairs.append((j,k))
    for check in range(3):
        t=rng.integers(0,2,size=hdim);mono=np.r_[1,t,[t[j]*t[k] for j,k in pairs]]
        lin=rng.integers(0,2,size=directions.shape[1])
        actual=F(x0+small@t+directions@lin)
        predicted=(polys@mono+linear[:,nw:].astype(np.int64)@lin)%2
        assert np.array_equal(actual,4*predicted)
    mat=np.column_stack((linear,polys));reduced,piv=d['rref'](mat)
    nc=linear.shape[1];dom=[j for j in piv if j<nc];ranklin=len(dom)
    obstruction=reduced[ranklin:len(piv),nc:].astype(np.int64)
    nums=np.arange(2**hdim,dtype=np.uint32)
    bits=((nums[:,None]>>np.arange(hdim,dtype=np.uint32))&1).astype(np.uint8)
    monomials=np.column_stack((np.ones(len(bits),dtype=np.uint8),bits,
                np.stack([bits[:,j]*bits[:,k] for j,k in pairs],axis=1)))
    obvalues=monomials@obstruction.T.astype(np.uint8)%2
    solutions=np.flatnonzero(~np.any(obvalues,axis=1));success=bool(len(solutions))
    row={'certificate_index':ix,'missing_coset':rec['missing_coset'],
         'complete_exponent_sixteen_fibre_nonempty':success,
         'lower_binary_parameters':Z.shape[1],'upper_binary_parameters':K.shape[1],
         'lower_homology_parameters':hdim,'linear_correction_rank':ranklin,
         'quadratic_obstruction_rank':len(piv)-ranklin,
         'lower_homology_choices_tested':len(bits),'lower_homology_choices_surviving':len(solutions)}
    if success:
        choice=int(solutions[0]);mono=monomials[choice].astype(np.int64)
        sol=np.zeros(nc,dtype=np.int64);sol[dom]=reduced[:ranklin,nc:].astype(np.int64)@mono%2
        x=(x0+small@bits[choice].astype(np.int64)+directions@sol[nw:]+4*sol[:nw])%8
        assert not np.any(F(x)) and not np.any(direct(x));literal_checks+=1
        row.update({'lambda_mod576':1+72*int(x[-1]),'integral_cusp_gauge':gauge,
                    'retained_lower_homology_bits':bits[choice].tolist(),
                    'correction_Z8_sparse':{str(j):int(a) for j,a in enumerate(x[:m]) if a},
                    'both_order_equations_directly_verified':True,
                    'commutator_image_rows_verified':True})
        certificates[f'correction_{ix}']=x
    results.append(row)
    print(json.dumps({k:v for k,v in row.items() if k not in ('correction_Z8_sparse','retained_lower_homology_bits')}),flush=True)
suffix='' if args.indices=='all' else '_'+args.indices.replace(',','_')
out={'refinement':'B/((gamma3(N) N^16) intersect (N-prime N^3))',
     'base_homology_points':'base conjugators in de_fibre_crt_verify.json',
     'indices_tested':indices,'block_and_order_checks_by_literal_words':literal_checks,
     'pass_counts':[sum(r['complete_exponent_sixteen_fibre_nonempty'] and r['missing_coset']==b for r in results) for b in (False,True)],
     'elapsed_seconds':round(time.time()-start,3),'records':results,
     'scope':'Complete exponent-sixteen gentle correction fibres above the specified affine G6 homology points, including all multiplier lifts and exact commutator-image rows. Further homology points in each CM matrix fibre are not enumerated.'}
if not globals().get('DE_LOAD_ONLY',False):
    (here/f'de_class2_sixteen_fibres{suffix}.json').write_text(json.dumps(out,indent=2)+'\n')
    np.savez_compressed(here/f'de_class2_sixteen_fibres_certificate{suffix}.npz',**certificates)
    print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2),flush=True)
