#!/usr/bin/env python3
"""Exact factor labels for the certified Kn23 orders, with reconstruction."""
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent


def main():
    whole=json.loads((HERE/'a_cm_kn23_full.json').read_text())
    old=json.loads((HERE/'a_cm_kn23_source.json').read_text())
    def factors(n):
        original=int(n);n=original;answer={}
        for p in (2,3):
            e=0
            while n%p==0:n//=p;e+=1
            answer[str(p)]=e
        assert n==1 and 2**answer['2']*3**answer['3']==original
        return answer
    values={'P':whole['entire_correction_order'],
            'P0':old['projected_correction_source']['order'],
            'old_projection':whole['entire_old_projection_order'],
            'kernel':whole['kernel_over_old_order']}
    out={'status':'PASS_EXACT_CERTIFIED_ORDER_FACTORS',
         'orders':{k:{'decimal':int(v),'prime_factors':factors(v)} for k,v in values.items()}}
    (HERE/'a_cm_kn23_numeric_summary.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
