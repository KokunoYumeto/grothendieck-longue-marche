#!/usr/bin/env python3
"""Retain the literal full twists in every corrected SL2(F3) braid map."""
from pathlib import Path
import json,time
import numpy as np
from a_cm_sl23_model import FerrariSL23
from de_ferrari_a6_source_data import load_data
from de_ferrari_degree4_lift import InducedCombined

HERE=Path(__file__).resolve().parent

def main():
    started=time.time();H=FerrariSL23();d=load_data();W=InducedCombined(H,d)
    C=np.load(HERE/'a_cm_sl23_corrections.npz')['corrections']
    records=json.loads((HERE/'de_ferrari_fibres.json').read_text())['records']
    rows=json.loads((HERE/'a_cm_sl23_corrections.json').read_text())['records']
    twist3=H.power(H.mul(H.a,H.b),3)
    twist4=H.power(H.mul(H.mul(H.a,H.b),H.c),4)
    out=[]
    for ix,(rec,row) in enumerate(zip(records,rows)):
        base=H.word(rec['actual_commutator_word_f'])
        for ci in row['all_gentle_pentagon_braid_indices']:
            values=H.mul(base,C[ci,W.root])
            a,b,c=H.braid_images(values)
            ft3=H.power(H.mul(a,b),3)
            ft4=H.power(H.mul(H.mul(a,b),c),4)
            same3=np.array_equal(ft3,twist3);same4=np.array_equal(ft4,twist4)
            assert same3 and same4
            out.append({'base_index':ix,'correction_index':ci,
                        'three_strand_full_twist_fixed':bool(same3),
                        'four_strand_full_twist_fixed':bool(same4)})
    result={'status':'PASS_LITERAL_SL23_FULL_TWISTS','point_count':len(out),
            'three_strand_word':'(a b)^3','four_strand_word':'(a b c)^4',
            'records':out,'seconds':round(time.time()-started,3)}
    (HERE/'a_cm_sl23_periodic.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2),flush=True)

if __name__=='__main__':main()
