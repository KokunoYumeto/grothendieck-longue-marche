"""All base-field prime-cyclic L1 tests, for every genus-two F_q form and point.

This exhausts constant-deck prime-cyclic P-split covers over the displayed
base field. It does not claim least prime over all finite extensions.
The output gives every tested character and its exact twisted L-polynomial;
the relative class number modulo two is computed by a polynomial gcd.
"""
import argparse,json,csv,time,collections,concurrent.futures
from pathlib import Path
from itertools import product
from finite_jacobian import *
from even_jacobian import *
from genus2_normal_forms import representatives

def mod2gcd(a,b):
    while b:
        while a and a.bit_length()>=b.bit_length():a^=b<<(a.bit_length()-b.bit_length())
        a,b=b,a
    return a

def compute(task):
    modulus,index,model=task;F=BinaryField(modulus)
    if model.get('pointless'):
        return {'q':F.q,'index':index,'model':model,'rational_points':0,'tests':[],'status':'no rational points'}
    J=(EvenJacobian if model['even'] else Jacobian)(F,model['h'],model['f'])
    elts=J.enumerate();pts=J.points();N=len(pts);order=len(elts);groups=[];tests=[]
    for ell in prime_factors(order):
        if ell==2:continue
        coords,basis,H=J.quotient(ell);r=len(basis);groups.append({'ell':ell,'basis':basis,'ell_rank':r,'ellJ_order':len(H)})
        for v in product(range(ell),repeat=r):
            if not any(v) or next(a for a in v if a)!=1:continue
            chi=lambda D:sum(a*b for a,b in zip(v,coords[D]))%ell
            values=[chi(D) for _,D in pts];canonical=chi(getattr(J,'canonical_base_class',J.zero))
            for (P,D),pval in zip(pts,values):
                counts=collections.Counter((a-pval)%ell for a in values)
                theta=1
                for a,n in counts.items():
                    if n%2:theta^=1<<a
                gd=mod2gcd(theta,(1<<ell)-1).bit_length()-1
                kappa=(canonical-2*pval)%ell
                tests.append({'point':P,'point_Mumford':D,'ell':ell,'character':v,'L_constant':1,'L_linear':sorted(counts.items()),'L_quadratic':[kappa,F.q],'relative_class_number_mod2':1 if gd==0 else 0,'mod2_gcd_degree':gd})
    good={str(t['point']) for t in tests if t['relative_class_number_mod2']}
    return {'q':F.q,'index':index,'model':model,'rational_points':N,'J_order':order,'points_with_witness':len(good),'quotients':groups,'tests':tests,'status':'all base-field prime characters exhausted; least prime over extensions not asserted'}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--modulus',type=int,required=True);ap.add_argument('--workers',type=int,default=4);ap.add_argument('--prefix',required=True);args=ap.parse_args()
    F=BinaryField(args.modulus);models=list(representatives(F));start=time.time();prefix=Path(args.prefix)
    summary=collections.Counter();tasks=[(args.modulus,i,m) for i,m in enumerate(models)]
    with prefix.with_suffix('.jsonl').open('w') as out,prefix.with_suffix('.csv').open('w',newline='') as cs:
        writer=csv.writer(cs);writer.writerow(['q','model_id','type','point','L_q','ell','character','L_polynomial_coefficients_in_zeta','relative_class_number_mod2','least_prime_status'])
        with concurrent.futures.ProcessPoolExecutor(max_workers=args.workers) as pool:
            for n,res in enumerate(pool.map(compute,tasks,chunksize=1),1):
                out.write(json.dumps(res,separators=(',',':'))+'\n')
                for t in res['tests']:
                    writer.writerow([F.q,res['index'],res['model']['type'],json.dumps(t['point']),F.q,t['ell'],json.dumps(t['character']),json.dumps([1,t['L_linear'],t['L_quadratic']],separators=(',',':')),t['relative_class_number_mod2'],'not asserted; all base-field prime characters listed'])
                summary['models']+=1;summary['rational_points']+=res['rational_points'];summary['tests']+=len(res['tests']);summary['points_with_base_field_witness']+=res.get('points_with_witness',0)
                if n%25==0 or n==len(models):
                    out.flush();cs.flush();print(json.dumps({'q':F.q,'done':n,'total':len(models),'elapsed_seconds':round(time.time()-start,2),'totals':summary}),flush=True)
    prefix.with_suffix('.summary.json').write_text(json.dumps({'q':F.q,'modulus':args.modulus,'normal_form_count':len(models),'counts':summary,'elapsed_seconds':time.time()-start,'scope':'Every genus-two F_q-isomorphism class; every rational point; every base-field prime-cyclic P-split cover. Extension-field minima remain separate.'},indent=2)+'\n')

if __name__=='__main__':main()
