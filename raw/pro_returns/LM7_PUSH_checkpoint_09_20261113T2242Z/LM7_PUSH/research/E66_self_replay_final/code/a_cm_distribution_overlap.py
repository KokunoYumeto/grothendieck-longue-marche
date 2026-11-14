#!/usr/bin/env python3
"""The exact index-two E6/E62 overlap characters on their actual images."""
from pathlib import Path
from itertools import product
import json
import time
import numpy as np

from a_cm_distribution_e62 import Distribution
from a_cm_gl23_pc import ClassTwoCoordinates,Sifter
from de_a6_schreier_certificate import read_certificate,verify_words

HERE=Path(__file__).resolve().parent


def solve(rows,rhs,n):
    a=[sum(int(x)<<j for j,x in enumerate(row))|(int(y)<<n)
       for row,y in zip(rows,rhs)]
    pivots=[];at=0
    for j in range(n):
        hit=next((k for k in range(at,len(a)) if a[k]>>j&1),None)
        if hit is None:continue
        a[at],a[hit]=a[hit],a[at]
        for k in range(len(a)):
            if k!=at and a[k]>>j&1:a[k]^=a[at]
        pivots.append(j);at+=1
    if any(v==(1<<n) for v in a):return None,len(pivots)
    x=sum(((a[k]>>n)&1)<<j for k,j in enumerate(pivots))
    return x,len(pivots)


def main():
    start=time.monotonic();P=ClassTwoCoordinates('joint');D=Distribution()
    c=read_certificate(HERE/'a_cm_distribution_e62_projected.bin');verify_words(c)
    joint=Sifter(c);n0=P.n
    d=read_certificate(HERE/'a_cm_distribution_e62_distribution.bin');verify_words(d)
    ds=Sifter(d)
    assert 2*joint.order==2**24*ds.order
    oneD=np.arange(85,dtype=np.uint16)
    def chiC(v):return int(not joint.contains(np.r_[P.element(v),n0+oneD]))
    def chiD(v):return int(not joint.contains(np.r_[P.one,n0+v]))
    cbits=[chiC(1<<j) for j in range(P.r+P.k)]
    assert any(cbits) and not any(cbits[P.r:])
    cmask=sum(a<<j for j,a in enumerate(cbits))
    # All basis products are compared with the actual subgroup membership.
    for i in range(24):
        for j in range(24):
            assert chiC(P.product(1<<i,1<<j))==(cbits[i]^cbits[j])
    decoder={p.tobytes():a for a,p in D.perms.items()}
    dvalues=[];rows=[];dbits=[]
    for g in d['strong']:
        values=[decoder[(g[17*j:17*(j+1)]-17*j).astype(np.uint16).tobytes()] for j in range(5)]
        row=[]
        for h,c0 in values:
            h4=tuple(x%4 for x in D.H[h]);row += [h4[1]//2,h4[2]//2,c0%2]
        dvalues.append(values);rows.append(row);dbits.append(chiD(g))
    # This may legitimately fail: a subdirect product can have an extra
    # binary character not extending to the ambient abelianization.
    mask,rank=solve(rows,dbits,15)
    if mask is not None:
        for row,bit in zip(rows,dbits):
            assert (sum(v<<j for j,v in enumerate(row))&mask).bit_count()%2==bit
    for i,g in enumerate(d['strong']):
        for j,h in enumerate(d['strong']):
            assert chiD(h[g])==(dbits[i]^dbits[j])
    # The computed character equality is checked on every generator of
    # the actual common image, before it is used on all final fibres.
    for g in c['strong']:
        cc=P.coordinates(g[:n0]);dd=g[n0:]-n0
        assert (cc&cmask).bit_count()%2==chiD(dd)
    retained=json.loads((HERE/'a_cm_distribution_e62.json').read_text())
    bits=[(a['E62_actual_PC_coordinate']&cmask).bit_count()%2
          for r in retained['records'] for a in r['actual_single_source_correction_fibres']]
    out={'status':'PASS_EXACT_INDEX_TWO_DISTRIBUTION_OVERLAP',
         'E62_PC_coordinate_character_bits':cbits,'E62_PC_character_mask':cmask,
         'distribution_character_on_actual_strong_generators':dbits,
         'distribution_strong_generators_as_five_H_times_C6_values':dvalues,
         'extends_to_ambient_binary_abelianization':mask is not None,
         'ambient_binary_coordinate_order':['H_mod4_upper/2','H_mod4_lower/2','c_N_mod2']*5,
         'ambient_binary_character_mask':mask,'ambient_binary_coordinate_rank':rank,
         'all_actual_common_generators_satisfy_character_equality':True,
         'all_96_E62_final_correction_character_values':bits,
         'character_defining_map':'chi_C(c)=1 iff (c,1) is outside the actual index-two common image; chi_D(d)=1 iff (1,d) is outside it.',
         'scope':'Actual correction-image overlap character, not an assigned full-GT character.',
         'seconds':round(time.monotonic()-start,6)}
    (HERE/'a_cm_distribution_overlap.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in {
        'distribution_strong_generators_as_five_H_times_C6_values',
        'distribution_character_on_actual_strong_generators','all_96_E62_final_correction_character_values'}},indent=2))


if __name__=='__main__':main()
