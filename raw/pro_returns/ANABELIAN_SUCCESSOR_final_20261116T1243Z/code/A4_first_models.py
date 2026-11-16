"""Run rational relative-class-number tests on explicit genus-two models.

The normal-form families here have at least one rational branch point.
We do not claim they enumerate every curve over the field.
"""
import sys,json,csv,argparse,time
from pathlib import Path
from itertools import product
from finite_jacobian import *

def models(F):
    q=F.q;R=PolynomialRing(F);tw=next(x for x in range(q) if F.trace(x))
    # Rank zero: a single pole, of order five.
    for a,b,c,d in product(range(1,q),range(q),range(q),(0,tw)):
        yield f'rank0_{a}_{b}_{c}_{d}',(1,),(d,c,0,b,0,a)
    # Rank one: poles of orders three and one, hence both rational.
    for a,b,c,d in product(range(1,q),range(q),range(1,q),(0,tw)):
        yield f'rank1_{a}_{b}_{c}_{d}',(0,1),(0,c,d,b,0,a)
    # Ordinary with three rational simple poles at 0,1,infinity.
    h=(0,1,1);hh=R.sq(h)
    for a,b,c,d in product(range(1,q),range(1,q),range(1,q),(0,tw)):
        f=R.add(R.mul((d,a),hh),R.add(R.scale((0,1,0,1),b),R.scale((0,0,1,1),c)))
        yield f'split_{a}_{b}_{c}_{d}',h,f
    # Ordinary: infinity and a closed quadratic point.
    h=(tw,1,1);hh=R.sq(h)
    for a,b,c,d in product(range(1,q),range(q),range(q),(0,tw)):
        if b==c==0:continue
        f=R.add(R.mul((d,a),hh),R.mul((c,b),h))
        yield f'quadratic_{a}_{b}_{c}_{d}',h,f

def run(modulus,filename,stop_counterexample=False):
    F=BinaryField(modulus);summary=[];allrows=[];start=time.time()
    for idx,(name,h,f) in enumerate(models(F)):
        J=Jacobian(F,h,f);order=len(J.enumerate());N=len(J.points())
        factors=[ell for ell in prime_factors(order) if ell>2]
        if stop_counterexample and not any(ell>N and N>=2*(order//ell) for ell in factors):continue
        rows=genus2_characters(J)
        for row in rows:row.update(model=name,h=h,f=f)
        allrows.extend(rows)
        passed={str(row['point']) for row in rows if row['L1_passes']}
        summary.append({'model':name,'h':h,'f':f,'N':N,'J_order':order,'points_with_base_field_witness':len(passed),'rational_points':N,'characters_tested':len(rows)})
        if stop_counterexample:
            bad=[r for r in rows if not r['L1_passes'] and r['ell']>N and N>=2*r['kernel_order']]
            if bad:
                Path(filename).write_text(json.dumps({'claim':'L3 singleton without primitive-root hypothesis','counterexamples':bad,'summary':summary},indent=2)+'\n')
                print(json.dumps(bad,indent=2));return
        if (idx+1)%100==0:print(f'models={idx+1} elapsed={time.time()-start:.1f}s',flush=True)
    Path(filename).write_text(json.dumps({'q':F.q,'modulus':modulus,'scope':'Explicit models with rational branch point; duplicates retained; no completeness claim','summary':summary,'tests':allrows,'elapsed_seconds':time.time()-start},indent=2)+'\n')
    print(json.dumps({'q':F.q,'models':len(summary),'tests':len(allrows),'elapsed':time.time()-start},indent=2))

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--modulus',type=int,default=7);ap.add_argument('--output',required=True);ap.add_argument('--counterexample',action='store_true');args=ap.parse_args()
    run(args.modulus,args.output,args.counterexample)
