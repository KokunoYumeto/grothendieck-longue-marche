#!/usr/bin/env python3
"""Apply AG.28 to already certified exact quartic class-number data.
Uses the rigorous exponent upper bound p^v_p(h_D), not an inferred group structure.
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


def run(q):
    curves={}
    src=HERE/f'plane_quartic_F{q}_tests.jsonl'
    with src.open() as f:
        for row in f:
            d=json.loads(row)
            curves[d['normalized_code']]={
                'h':d['Jacobian_order'],
                'least_L1':d['least_successful_base_field_prime'],
                'N':d[f'N{q}']}
    rows=[]
    best={}
    with (ROOT/'code'/f'A4_quartic_F{q}_exact_norms.csv').open() as f:
        for d in csv.DictReader(f):
            code=int(d['normalized_code']); ell=int(d['ell'])
            hrel=int(d['relative_class_number_exact'])
            base=curves[code]
            v=valuation(base['h'],q)+valuation(hrel,q)
            bound=q**v
            if (q-1)*bound<2*(ell-1):
                row=dict(normalized_code=code,field=q,ell=ell,
                    character=d['character'],Jacobian_order=base['h'],
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
