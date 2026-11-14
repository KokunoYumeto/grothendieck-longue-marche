#!/usr/bin/env python3
"""Complete gentle fibres in the exact GL23 or GL23--SL23 common source.

The group has a proved class-two coordinate model, not a linear surrogate.
Only its quotient by its central derived subgroup is first solved linearly;
the full central equations are then evaluated for every surviving value.
"""
from pathlib import Path
import argparse,json,time
import numpy as np
from a_cm_gl23_pc import ClassTwoCoordinates,mul,inv,conj,power
from de_ferrari_a6_source_data import load_data

HERE=Path(__file__).resolve().parent

def linear_system(columns,target):
    piv={};kernel=[]
    for j,col in enumerate(columns):
        v=int(col);w=1<<j
        while v:
            k=v.bit_length()-1
            if k in piv:v^=piv[k][0];w^=piv[k][1]
            else:piv[k]=(v,w);break
        if not v:kernel.append(w)
    v=int(target);w=0
    while v:
        k=v.bit_length()-1
        if k not in piv:return None,kernel,len(piv)
        v^=piv[k][0];w^=piv[k][1]
    return w,kernel,len(piv)

def affine_values(point,basis):
    values=[point]
    for b in basis:values += [v^b for v in values]
    return values

def main():
    pa=argparse.ArgumentParser();pa.add_argument('mode',choices=['single','joint']);args=pa.parse_args()
    start=time.time();P=ClassTwoCoordinates(args.mode)
    if args.mode=='single':
        dd=np.load(HERE/'a_cm_gl23_induced.npz');s=dd['compressed_s'];r=dd['compressed_r']
    else:s,r=np.load(HERE/'a_cm_gl23_joint.npz')['joint_B_generators']
    s=s.astype(np.uint16);r=r.astype(np.uint16);r2=mul(r,r)
    data=load_data();one=np.arange(len(s),dtype=np.uint16)
    bletters={0:s,1:r,-1:r2}
    def beval(w):
        a=one.copy()
        for j in w:a=mul(a,bletters[j])
        return a
    x=beval(data['xword']);y=beval(data['yword'])
    fletters={1:x,2:y,-1:inv(x),-2:inv(y)}
    def feval(w):
        a=one.copy()
        for j in w:a=mul(a,fletters[j])
        return a
    basis=np.r_[P.q,P.z]
    records=json.loads((HERE/'de_ferrari_fibres.json').read_text())['records']
    rows=[];si=[];ri=[];constants=[];rng=np.random.default_rng(741)
    for ix,rec in enumerate(records):
        f0=feval(rec['actual_commutator_word_f']);S=mul(s,f0);R=mul(inv(f0),r)
        a=P.coordinates(power(S,2));b=P.coordinates(power(R,3))
        As=[P.coordinates(conj(S,g)) for g in basis]
        Ar=[P.coordinates(conj(R,g)) for g in basis]
        Ar2=[P.apply(Ar,g) for g in Ar]
        assert all((v&P.mask)==0 for v in As[P.r:]+Ar[P.r:])
        def norms(c):
            ss=P.product(P.product(P.apply(As,c),a),c)
            ci=P.inverse(c)
            rr=P.product(P.product(P.product(ci,P.apply(Ar,ci)),P.apply(Ar2,ci)),b)
            return ss,rr
        for _ in range(4):
            c=int(rng.integers(0,1<<(P.r+P.k)));cp=P.element(c)
            f=mul(f0,cp)
            exact=(P.coordinates(power(mul(s,f),2)),P.coordinates(power(mul(inv(f),r),3)))
            assert norms(c)==exact
        cols=[]
        for j in range(P.r):
            v=1<<j
            vs=(As[j]^v)&P.mask
            vr=(v^Ar[j]^Ar2[j])&P.mask
            cols.append(vs | (vr<<P.r))
        target=(a&P.mask)|((b&P.mask)<<P.r)
        point,ker,rank=linear_system(cols,target)
        assert point is not None
        zcols=[]
        for j in range(P.k):
            v=1<<(P.r+j)
            zs=(As[P.r+j]^v)>>P.r
            zr=(v^Ar[P.r+j]^Ar2[P.r+j])>>P.r
            zcols.append(zs|(zr<<P.k))
        good=[];abelian_values=affine_values(point,ker);central_dimensions=[]
        for v in abelian_values:
            ns,nr=norms(v)
            assert not ((ns|nr)&P.mask)
            zp,zk,zrank=linear_system(zcols,(ns>>P.r)|((nr>>P.r)<<P.k))
            if zp is None:continue
            central_dimensions.append(len(zk))
            for z in affine_values(zp,zk):
                c=v|(z<<P.r)
                assert norms(c)==(0,0)
                good.append(c)
        good.sort()
        # Every retained answer is independently checked in the actual source.
        for c in good:
            f=mul(f0,P.element(c))
            assert np.array_equal(power(mul(s,f),2),one)
            assert np.array_equal(power(mul(inv(f),r),3),one)
        rows.append({'index':ix,'missing_coset':rec['missing_coset'],
            'quotient_linear_rank':rank,'quotient_affine_dimension':len(ker),
            'quotient_affine_point':point,'quotient_affine_kernel':ker,
            'quotient_values_examined':len(abelian_values),
            'central_linear_rank':zrank,'surviving_central_dimensions':sorted(set(central_dimensions)),
            'whole_source_fibre_size':1<<(P.r+P.k),
            'exact_gentle_count':len(good),'all_gentle_coordinates':good})
        si.append(As);ri.append(Ar);constants.append([a,b])
        print(args.mode,'G6 point',ix,'abelian dimension',len(ker),'gentle',len(good),flush=True)
    out={'status':'PASS_COMPLETE_ACTUAL_GL23_GENTLE_FIBRES','mode':args.mode,
         'actual_correction_group_order':1<<(P.r+P.k),
         'quotient_dimension':P.r,'central_derived_dimension':P.k,
         'all_actual_norm_equations_retained':True,'all_answers_independently_checked_as_permutations':True,
         'records':rows,'seconds':round(time.time()-start,3)}
    prefix=HERE/f'a_cm_gl23_{args.mode}_gentle'
    prefix.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    np.savez_compressed(prefix.with_suffix('.npz'),S_actions=si,R_actions=ri,norm_constants=constants)
    print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2),flush=True)

if __name__=='__main__':main()
