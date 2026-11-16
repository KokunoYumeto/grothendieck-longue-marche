#!/usr/bin/env python3
"""Apply AG.28 to already certified exact quartic class-number data.
Uses the exact cyclotomic annihilator bound from the constant prime cyclic action.
"""
import csv, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
HERE=Path(__file__).resolve().parent


def valuation(n,p):
    e=0
    while n%p==0:
        n//=p
        e+=1
    return e


def order(a,n):
    r=a%n; f=1
    while r!=1:
        r=r*a%n; f+=1
    return f


def rank_mod(matrix,p):
    a=[list(r) for r in matrix]; rank=0
    for col in range(len(a[0])):
        pivot=next((i for i in range(rank,len(a)) if a[i][col]%p),None)
        if pivot is None: continue
        a[rank],a[pivot]=a[pivot],a[rank]
        z=pow(a[rank][col],-1,p);a[rank]=[(x*z)%p for x in a[rank]]
        for i in range(len(a)):
            if i!=rank:
                z=a[i][col];a[i]=[(x-z*y)%p for x,y in zip(a[i],a[rank])]
        rank+=1
    return rank


def hasse_witt_rank(coeff,p,zeta):
    mons=[(i,j,4-i-j) for i in range(5) for j in range(5-i)]
    poly={m:c%p for m,c in zip(mons,coeff) if c%p}
    power={(0,0,0):1}
    for _ in range(p-1):
        temp={}
        for a,c in power.items():
            for b,d in poly.items():
                e=tuple(x+y for x,y in zip(a,b));temp[e]=temp.get(e,0)+c*d
        power={e:c%p for e,c in temp.items() if c%p}
    basis=[(2,1,1),(1,2,1),(1,1,2)]
    M=[[power.get(tuple(p*x-y for x,y in zip(source,target)),0)
        for source in basis] for target in basis]
    tr=sum(M[i][i] for i in range(3))
    c2=sum(M[i][i]*M[j][j]-M[i][j]*M[j][i] for i in range(3) for j in range(i+1,3))
    det=sum(M[0][i]*(M[1][(i+1)%3]*M[2][(i+2)%3]-M[1][(i+2)%3]*M[2][(i+1)%3]) for i in range(3))
    cp=[1,(-tr)%p,c2%p,(-det)%p]
    assert cp==[x%p for x in zeta[:4]],(p,coeff,M,cp,zeta)
    r=3-rank_mod([[(M[i][j]-(i==j))%p for j in range(3)] for i in range(3)],p)
    return r,M


def run(q):
    curves={}
    src=HERE/f'plane_quartic_F{q}_tests.jsonl'
    with src.open() as f:
        for row in f:
            d=json.loads(row)
            a=valuation(d['Jacobian_order'],q)
            r,M=hasse_witt_rank(d['quartic_coefficients'],q,d['zeta_numerator']) if a>1 else (a,None)
            assert 0<=r<=a and (a==0)==(r==0)
            base_exp=0 if a==0 else a-r+1
            curves[d['normalized_code']]={
                'base_rank':r,'base_exp':base_exp,'Hasse_Witt':M,
                'h':d['Jacobian_order'],
                'least_L1':d['least_successful_base_field_prime'],
                'N':d[f'N{q}'],
                'gcds':{(t['ell'],tuple(t['character'])):t[f'mod{q}_gcd_degree'] for t in d['tests']}}
    rows=[]
    best={}
    with (ROOT/'code'/f'A4_quartic_F{q}_exact_norms.csv').open() as f:
        for d in csv.DictReader(f):
            code=int(d['normalized_code']); ell=int(d['ell'])
            hrel=int(d['relative_class_number_exact'])
            base=curves[code]
            f=order(q,ell)
            vbase=valuation(base['h'],q); vrel=valuation(hrel,q)
            assert vrel%f==0
            gcddeg=base['gcds'][(ell,tuple(json.loads(d['character'])))]; assert gcddeg%f==0
            assert (vrel==0)==(gcddeg==0) and vrel>=gcddeg
            new_exp_bound=0 if vrel==0 else 1+(vrel-gcddeg)//f
            v=max(base['base_exp'],new_exp_bound)
            bound=q**v
            if (q-1)*bound<2*(ell-1):
                row=dict(normalized_code=code,field=q,ell=ell,
                    character=d['character'],Jacobian_order=base['h'],
                    order_of_p_mod_ell=f,base_p_valuation=vbase,relative_p_valuation=vrel,
                    base_rational_p_rank=base['base_rank'],base_exponent_log_p_bound=base['base_exp'],
                    Hasse_Witt_matrix=json.dumps(base['Hasse_Witt']),
                    mod_p_gcd_degree=gcddeg,new_exponent_log_p_bound=new_exp_bound,
                    relative_class_number_exact=hrel,
                    rational_p_primary_exponent_upper_bound=bound,
                    left_side=(q-1)*bound,right_side=2*(ell-1),
                    base_L1_exists=bool(base['least_L1']),
                    base_least_L1=base['least_L1'],
                    same_cover_L1=(hrel%q!=0),
                    rational_points=base['N'])
                rows.append(row)
                if code not in best or ell<best[code]['ell']:
                    best[code]=row
    added=[r for r in best.values() if not r['base_L1_exists']]
    out=HERE/f'plane_quartic_F{q}_rational_exponent_certificates.csv'
    if rows:
        with out.open('w') as f:
            w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    l1=sum(bool(d['least_L1']) for d in curves.values())
    summary=dict(field=q,classes=len(curves),successful_AG28_tests=len(rows),
        classes_with_AG28_witness=len(best),classes_already_L1=l1,
        classes_added_beyond_every_base_field_L1_test=len(added),
        total_classes_with_either_criterion=l1+len(added),
        remaining_classes=len(curves)-l1-len(added),
        same_cover_L1_failures_with_AG28_success=sum(not r['same_cover_L1'] for r in rows),
        added_classes=added,
        status='Proved pointed no-collision over this base field only; no all-extension L1 minimum claim')
    (HERE/f'plane_quartic_F{q}_rational_exponent_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps({k:v for k,v in summary.items() if k!='added_classes'},indent=2))

if __name__=='__main__':
    run(3);run(5)
