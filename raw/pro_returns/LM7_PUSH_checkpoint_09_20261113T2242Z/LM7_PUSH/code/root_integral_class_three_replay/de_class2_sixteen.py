#!/usr/bin/env python3
"""Exact complete next fibres above the 24 actual E.13 exponent-eight words.

Both multiplier residues modulo 576 and the exact commutator-image rows
are tested. Negative output concerns only the specified E.13 witnesses.
"""
from contextlib import redirect_stdout
from pathlib import Path
import io,json,runpy,time
import numpy as np
from de_class2_two_power import TwoPowerCollector

here=Path(__file__).resolve().parent
with redirect_stdout(io.StringIO()):e=runpy.run_path(str(here/'de_class2_eight.py'))
g=e['g'];d=e['d'];base=e['base'];n=97;m=4753
c=TwoPowerCollector(4,e);checks=c.literal_checks()
print('Literal mixed-word action checks:',checks,flush=True)
records=json.loads((here/'de_fibre_eight_crt_verify.json').read_text())['records']
matrix=np.zeros((2*m+2,m+2*len(records)),dtype=np.uint8)
matrix[:,:m]=g['original'];prepared=[];start=time.time()
for j,rec in enumerate(records):
    a,z=c.zero()
    for i,v in rec['central_square_word_factors']:a[i]=v%c.mod
    for i,k,v in rec['central_commutator_word_factors']:
        pos=np.flatnonzero((c.up[0]==i)&(c.up[1]==k))[0];z[pos]=v%c.cmod
    ja,jz=c.zero()
    for i,v in rec['commutator_adjustment_common_kernel_word_factors']:ja[i]=v%c.mod
    b=rec['base_beta_word_B'];cg=c.bpower(e['x'],rec['integral_cusp_gauge'])
    s0=b+[0]+base['binv'](b)+[(a,z)]+c.invword(cg)+[(ja,jz)]+cg
    es=c.next_kernel(s0*2)
    er=[c.next_kernel((s0+e['t']*(1+288*h))*3) for h in range(2)]
    for h in range(2):matrix[:m,m+2*j+h]=es;matrix[m:2*m,m+2*j+h]=er[h]
    prepared.append((s0,es,er))
reduced,piv=d['rref'](matrix);dom=[i for i in piv if i<m];rank=len(dom);rows=[]
for j,(rec,(s0,es,er)) in enumerate(zip(records,prepared)):
    choices=[]
    for h in range(2):
        col=m+2*j+h;success=not np.any(reduced[rank:,col])
        row={'lambda_mod576':1+288*h,'passes':success}
        if success:
            k=np.zeros(m,dtype=np.int64);k[dom]=reduced[:rank,col]
            rhs=np.concatenate((es,er[h],np.zeros(2,dtype=np.int64)))
            assert np.array_equal(g['original'].astype(np.int64)@k%2,rhs)
            block=(8*k[:n],4*k[n:])
            assert all(not np.any(v) for v in c.collect((s0+[block])*2))
            assert all(not np.any(v) for v in c.collect(([block]+s0+e['t']*(1+288*h))*3))
            row.update({'correction_F2_sparse':{str(i):int(v) for i,v in enumerate(k) if v},
                        'both_order_equations_directly_verified':True})
        choices.append(row)
    row={'certificate_index':j,'missing_coset':rec['missing_coset'],
         'some_lift_exists':any(x['passes'] for x in choices),'multiplier_choices':choices}
    rows.append(row)
    print(json.dumps({k:v for k,v in row.items() if k!='multiplier_choices'}),flush=True)
out={'refinement':'B/((gamma3(N) N^16) intersect (gamma3(N) N^3))',
     'base_witnesses':'de_fibre_eight_crt_verify.json','coefficient_rank':rank,
     'augmented_rank':len(piv),'block_actions_checked_against_literal_words':checks,
     'pass_counts':[sum(r['some_lift_exists'] and r['missing_coset']==v for r in rows) for v in (False,True)],
     'elapsed_seconds':round(time.time()-start,3),'records':rows,
     'scope':'Complete gentle lifting fibres over the 24 specified E.13 words; these words do not exhaust their CM matrix fibres.'}
(here/'de_class2_sixteen.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2),flush=True)
