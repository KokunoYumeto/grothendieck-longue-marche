#!/usr/bin/env python3
"""Literal-word certificate for the common exponent-eight/exponent-three level.

Combines the complete Z/4 lifts with the retained three-primary witnesses,
constructs an actual F' word using twenty-fourth powers in the common
kernel, and substitutes both complete braid hexagons in both collectors.
"""
from contextlib import redirect_stdout
from pathlib import Path
import io,json,runpy,time
import numpy as np
import sympy as sp

here=Path(__file__).resolve().parent
with redirect_stdout(io.StringIO()):e=runpy.run_path(str(here/'de_class2_eight.py'))
g=e['g'];d=e['d'];base=e['base'];v=e['v'];n=97;m=4753;up=e['up'];ci=e['ci']
old=e['records'];new=json.loads((here/'de_class2_eight_fibres.json').read_text())['records']
ac=g['abel_coords'];abel=g['abel'];pair=None
for i in range(n):
    for j in range(i+1,n):
        M=sp.Matrix(ac[:,[i,j]].tolist())
        if abs(M.det())==1:pair=(i,j);inverse=np.array(M.inv().tolist(),dtype=np.int64);break
    if pair is not None:break
assert pair is not None
def invert(w):return [(x[0],-x[1]) if isinstance(x,tuple) else -x for x in reversed(w)]
def collect3(w,K):
    q=v['unit'];a=np.zeros(n,dtype=np.int64);z=np.zeros((n,n),dtype=np.int64)
    for token in w:
        if isinstance(token,tuple):
            if token[0]=='k':
                A=v['act'](q,v['C'])[v['chords']];z=(z+token[1]*(A@K@A.T))%3
            continue
        qn=v['times'](q,v['ss'] if token==0 else v['rr'] if token==1 else v['inverse'](v['rr']))
        gen=[]
        if token:
            if q in ci:gen.append(ci[q]+1)
            if qn in ci:gen.append(-ci[qn]-1)
        for letter in gen:
            i=abs(letter)-1;s=1 if letter>0 else -1
            z[:,i]=(z[:,i]+2*s*a)%3;z[i,:]=(z[i,:]-2*s*a)%3;a[i]=(a[i]+s)%3
        q=qn
    assert q==v['unit'];return a,z[up]
rows=[];start=time.time()
for j,(oldrec,newrec) in enumerate(zip(old,new)):
    assert newrec['complete_exponent_eight_fibre_nonempty'] and newrec['lambda_mod288']==1
    k=np.zeros(m,dtype=np.int64)
    for i,c in newrec['correction_Z4_sparse'].items():k[int(i)]=c
    c3=np.zeros(m-n,dtype=np.int64)
    for i,l,c in oldrec['central_commutator_word_factors']:
        q=np.flatnonzero((up[0]==i)&(up[1]==l))[0];c3[q]=c%3
    K3=np.zeros((n,n),dtype=np.int64);K3[up]=c3;K3=(K3-K3.T)%3
    coeff=ac@k[:n];assert not np.any(coeff%4)
    jcoeff=inverse@(-coeff//4);jvec=np.zeros(n,dtype=np.int64);jvec[list(pair)]=24*jcoeff
    assert not np.any(6*abel@k[:n]+abel@jvec)
    gauge=newrec['integral_cusp_gauge'];assert gauge==oldrec['integral_cusp_gauge']
    cg=e['bpower'](e['x'],gauge);b=oldrec['base_beta_word_B']
    f=[0]+cg+b+[0]+base['binv'](b)+[('k',1)]+base['binv'](cg)+[('j',1)];fi=invert(f)
    u=[-1,0];vv=[0,-1]
    words=[u+fi+vv+f+invert(fi+[1]), fi+vv+f+u+invert(vv+u+f)]
    for w in words:
        w2=[]
        for token in w:
            if not isinstance(token,tuple):w2.append(token)
            elif token[0]=='k':w2.append((token[1]*6*k[:n],token[1]*3*k[n:]))
            else:w2.append(e['zero']())
        assert all(not np.any(c) for c in e['collect'](w2))
        assert all(not np.any(c) for c in collect3(w,K3))
    row={'certificate_index':j,'missing_coset':oldrec['missing_coset'],'A':oldrec['A'],'beta':oldrec['beta'],
         'lambda_mod288':1,'integral_cusp_gauge':gauge,'base_beta_word_B':b,
         'central_square_word_factors':[[i,6*int(c)] for i,c in enumerate(k[:n]) if c],
         'central_commutator_word_factors':[[int(i),int(l),int(3*c2+4*c_3)] for i,l,c2,c_3 in zip(*up,k[n:],c3) if c2 or c_3],
         'commutator_adjustment_common_kernel_word_factors':[[i,int(c)] for i,c in enumerate(jvec) if c],
         'actual_F_abelianization_zero':True,'generation_ranks':[97,97],
         'both_hexagons_directly_verified_at_both_primes':True}
    rows.append(row);print(json.dumps({k:row[k] for k in ('certificate_index','missing_coset','both_hexagons_directly_verified_at_both_primes')}),flush=True)
out={'common_refinement':'B/((gamma3(N_B) N_B^8) intersect (gamma3(N_B) N_B^3))',
     'all_24_CM_fibres_have_verified_gentle_shadows':True,'complete_hexagon_checks':96,
     'factored_word_convention':'Zero-indexed n_i are Nwords of de_distribution_test.py. k is the listed powers followed by commutators. f=s*x^g*(beta*s*beta^-1)*k*x^-g*j; j is the listed product of twenty-fourth powers.',
     'elapsed_seconds':round(time.time()-start,3),'records':rows,
     'scope':'Explicit common-refinement shadows for every whole admissible CM matrix fibre, including all twelve extra fibres. This does not assert a full profinite lift.'}
(here/'de_fibre_eight_crt_verify.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2),flush=True)
