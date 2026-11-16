"""Exact mixed-character rational L1 search for F4 classes122/133.

Uses the proved Cartier-Mumford comparison, not finite-field point counting.
Every candidate is checked for exact order and the required Frobenius
eigencondition; all Frobenius coefficients and arithmetic are retained.
"""
import json,time,random,argparse
from pathlib import Path
from big_binary_field import *
from finite_jacobian import PolynomialRing,Jacobian
from cartier_mumford_probe import doubling_coefficient

HERE=Path(__file__).parent
def elliptic_order(t,m):
    a,b=2,t
    if m==0:return 0
    for _ in range(2,m+1):a,b=b,t*b-4*a
    return 4**m+1-b
def frob_div(F,D,r):return tuple(tuple(F.frob(c,r) for c in poly) for poly in D)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--ell',type=int,default=7);ap.add_argument('--m',type=int,default=24)
    ap.add_argument('--extension-factor',type=int,default=1);ap.add_argument('--attempts',type=int,default=8);args=ap.parse_args()
    ell,m=args.ell,args.m;d=2*m;n=d*args.extension_factor;start=time.time()
    output=HERE/f'bielliptic_mixed_ell{ell}_F4pow{m}.json';log=[]
    modfile=HERE/f'GF2_{n}_modulus.json'
    if modfile.exists():mod=json.loads(modfile.read_text())['modulus']
    else:
        mod=find_modulus(n);modfile.write_text(json.dumps({'degree':n,'modulus':mod,'irreducible':irreducible(mod)})+'\n')
    F=BigBinaryField(mod);R=PolynomialRing(F);alpha=F.embed_f4();h=(0,1,1);f=(0,alpha,alpha,1,0,1)
    J=Jacobian(F,h,f);N1=elliptic_order(-3,n//2);N2=elliptic_order(1,n//2);N=N1*N2
    cofactor=N;val=0
    while cofactor%ell==0:cofactor//=ell;val+=1
    assert val
    meta={'curve':'y^2+y=x+alpha/(x*(x+1)); Y=x*(x+1)*y','ell':ell,'base_field_degree_over_F4':m,
      'coefficient_field_degree_over_F2':n,'field_modulus':mod,'alpha':alpha,'h':h,'f':f,
      'elliptic_orders':[N1,N2],'J_order':N,'ell_valuation':val,'cofactor':cofactor,'candidates':log}
    rng=random.Random(2026111600+ell+m)
    print(json.dumps({'phase':'field_ready','n':n,'modulus':mod,'ell_valuation':val,'elapsed':time.time()-start}),flush=True)
    for attempt in range(args.attempts):
        while True:
            x=rng.getrandbits(n);hx=R.eval(h,x)
            if not hx:continue
            z=F.as_root(F.div(R.eval(f,x),F.mul(hx,hx)))
            if z is None:continue
            y=F.mul(hx,z);point=((x,1),(y,));assert J.valid(point);break
        print(json.dumps({'phase':'point','attempt':attempt,'elapsed':time.time()-start}),flush=True)
        D=J.scale(point,cofactor)
        if D==J.zero:
            log.append({'attempt':attempt,'sample_point':[x,y],'status':'zero ell-primary projection'});continue
        powers=0
        while True:
            E=J.scale(D,ell)
            if E==J.zero:break
            D=E;powers+=1
            assert powers<=val
        qmod=pow(2,d,ell)
        if args.extension_factor>1:
            D=J.add(frob_div(F,D,d),J.neg(D))
        if D==J.zero:
            log.append({'attempt':attempt,'sample_point':[x,y],'status':'zero q-eigenprojection'});continue
        assert J.scale(D,ell)==J.zero
        assert frob_div(F,D,d)==J.scale(D,qmod),('wrong Frobenius eigencondition',D,qmod)
        ds=[J.zero];E=J.zero
        for i in range(1,ell):E=J.add(E,D);ds.append(E)
        assert len(set(ds))==ell and J.add(ds[-1],D)==J.zero
        coeff=[0]*ell
        for i in range(1,ell):
            E,c=doubling_coefficient(J,ds[i]);assert E==ds[(2*i)%ell];coeff[i]=c
        As=[]
        for i in range(1,ell):
            a=1;j=i
            for _ in range(d):a=F.mul(F.sq(a),coeff[j]);j=(2*j)%ell
            assert j==(qmod*i)%ell;As.append(a)
        good=all(a!=1 for a in As)
        cand={'attempt':attempt,'sample_point':[x,y],'ell_multiplications_after_cofactor':powers,
              'torsion_divisor':D,'multiples':ds,'doubling_coefficients':coeff,'q_power_coefficients':As,
              'relative_class_number_mod2':int(good),'Frobenius_eigenvalue':qmod}
        log.append(cand);meta['elapsed_seconds']=time.time()-start;meta['witness_found']=good
        output.write_text(json.dumps(meta,indent=2)+'\n')
        print(json.dumps({'phase':'tested','attempt':attempt,'L1_passes':good,'ones':As.count(1),'elapsed':time.time()-start}),flush=True)
        if good:break
    meta['elapsed_seconds']=time.time()-start;meta['witness_found']=any(c.get('relative_class_number_mod2')==1 for c in log)
    output.write_text(json.dumps(meta,indent=2)+'\n')

if __name__=='__main__':main()
