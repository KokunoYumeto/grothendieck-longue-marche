#!/usr/bin/env python3
"""Actual common exponent-sixteen/three words and full hexagon substitution."""
from contextlib import redirect_stdout
from pathlib import Path
import io,json,runpy,time
import numpy as np
from de_class2_two_power import TwoPowerCollector

here=Path(__file__).resolve().parent
with redirect_stdout(io.StringIO()):h=runpy.run_path(str(here/'de_fibre_eight_crt_verify.py'))
e=h['e'];base=h['base'];n=97;m=4753;up=e['up'];c=TwoPowerCollector(4,e)
old=e['records'];new=json.loads((here/'de_class2_sixteen_fibres.json').read_text())['records']
ac=h['ac'];abel=h['abel'];pair=h['pair'];inverse=h['inverse']
rows=[];start=time.time();checks=c.literal_checks()
for j,(oldrec,newrec) in enumerate(zip(old,new)):
    assert newrec['complete_exponent_sixteen_fibre_nonempty'] and newrec['lambda_mod576']==1
    k=np.zeros(m,dtype=np.int64)
    for i,a in newrec['correction_Z8_sparse'].items():k[int(i)]=a
    c3=np.zeros(m-n,dtype=np.int64)
    for i,l,a in oldrec['central_commutator_word_factors']:
        q=np.flatnonzero((up[0]==i)&(up[1]==l))[0];c3[q]=a%3
    K3=np.zeros((n,n),dtype=np.int64);K3[up]=c3;K3=(K3-K3.T)%3
    coeff=ac@k[:n];assert not np.any(coeff%8)
    jcoeff=inverse@(-coeff//8);jvec=np.zeros(n,dtype=np.int64);jvec[list(pair)]=48*jcoeff
    assert not np.any(6*abel@k[:n]+abel@jvec)
    gauge=newrec['integral_cusp_gauge'];assert gauge==oldrec['integral_cusp_gauge']
    cg=c.bpower(e['x'],gauge);b=oldrec['base_beta_word_B']
    f=[0]+cg+b+[0]+base['binv'](b)+[('k',1)]+base['binv'](cg)+[('j',1)]
    fi=h['invert'](f);u=[-1,0];vv=[0,-1]
    words=[u+fi+vv+f+h['invert'](fi+[1]),fi+vv+f+u+h['invert'](vv+u+f)]
    kb=(6*k[:n]%16,3*k[n:]%8);ki=c.inverse(kb)
    for w in words:
        w2=[]
        for token in w:
            if not isinstance(token,tuple):w2.append(token)
            elif token[0]=='k':w2.append(kb if token[1]==1 else ki)
            else:w2.append(c.zero())
        assert all(not np.any(a) for a in c.collect(w2))
        assert all(not np.any(a) for a in h['collect3'](w,K3))
    row={'certificate_index':j,'missing_coset':oldrec['missing_coset'],
         'A':oldrec['A'],'beta':oldrec['beta'],'lambda_mod576':1,
         'integral_cusp_gauge':gauge,'base_beta_word_B':b,
         'central_square_word_factors':[[i,6*int(a)] for i,a in enumerate(k[:n]) if a],
         'central_commutator_word_factors':[[int(i),int(l),int(3*a2+16*a3)]
                  for i,l,a2,a3 in zip(*up,k[n:],c3) if a2 or a3],
         'commutator_adjustment_common_kernel_word_factors':[[i,int(a)] for i,a in enumerate(jvec) if a],
         'actual_F_abelianization_zero':True,'generation_ranks':[97,97],
         'both_hexagons_directly_verified_at_both_primes':True}
    rows.append(row)
    print(json.dumps({k:row[k] for k in ('certificate_index','missing_coset','both_hexagons_directly_verified_at_both_primes')}),flush=True)
out={'common_refinement':'B/((gamma3(N_B) N_B^16) intersect (gamma3(N_B) N_B^3))',
     'all_24_CM_fibres_have_verified_gentle_shadows':True,'complete_hexagon_checks':96,
     'block_actions_checked_against_literal_words':checks,
     'factored_word_convention':'Zero-indexed n_i are Nwords of de_distribution_test.py. k is the listed powers followed by commutators. f=s*x^g*(beta*s*beta^-1)*k*x^-g*j; j is the listed product of forty-eighth powers.',
     'elapsed_seconds':round(time.time()-start,3),'records':rows,
     'scope':'Actual common-refinement commutator-word shadows for all24 CM matrix fibres; no full profinite lifting assertion.'}
(here/'de_fibre_sixteen_crt_verify.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2),flush=True)
