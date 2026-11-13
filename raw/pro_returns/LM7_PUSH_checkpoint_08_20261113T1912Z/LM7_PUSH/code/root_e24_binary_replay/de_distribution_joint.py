#!/usr/bin/env python3
"""Simultaneous N=2,3,4,6,12 distribution test, with corrections in N_B'.
Uses exact permutation-group membership (Schreier--Sims), not independent
existence at the five stages. A pass only concerns the stated finite test.
"""
from contextlib import redirect_stdout
from pathlib import Path
from itertools import product
import io,json,runpy,time
from sympy.combinatorics import Permutation,PermutationGroup

here=Path(__file__).resolve().parent
with redirect_stdout(io.StringIO()):d=runpy.run_path(str(here/'de_distribution_more.py'))
base=d['d'];induced=d['induced'];amul=d['amul'];ainv=d['ainv']
times,unit,qy=base['times'],base['unit'],base['qy']
NVALUES=(2,3,4,6,12);degree=17;total=sum(NVALUES)*degree
V4=sorted({(1,0,0,1),(1,2,0,1),(1,0,2,1),(1,2,2,1)})
vectors=[v for v in product(range(3),repeat=2) if v!=(0,0)]
def aper(a):
    h,c=a;h=base['d']['lift'](h)
    four=tuple(x%4 for x in h);three=tuple(x%3 for x in h)
    def m4(x,y):return tuple(z%4 for z in (x[0]*y[0]+x[1]*y[2],x[0]*y[1]+x[1]*y[3],x[2]*y[0]+x[3]*y[2],x[2]*y[1]+x[3]*y[3]))
    return tuple([V4.index(m4(four,b)) for b in V4]+
                 [4+vectors.index(((three[0]*u+three[1]*v)%3,(three[2]*u+three[3]*v)%3)) for u,v in vectors]+
                 [12+(i+c)%2 for i in range(2)]+[14+(i+c)%3 for i in range(3)])
def wreathperm(vals):
    out=[];offset=0
    for n,(vec,shift) in zip(NVALUES,vals):
        for i in range(n):
            j=(i-shift)%n;p=aper(vec[j]);out.extend(offset+j*degree+k for k in p)
        offset+=n*degree
    return Permutation(out)
gens=[wreathperm([induced(w,n) for n in NVALUES]) for w in base['Nfwords']]
G=PermutationGroup(gens)
print('Computing the derived image of N_B on permutation degree',total,flush=True)
start=time.time();Gp=G.derived_subgroup()
print('Derived subgroup computed, generators:',len(Gp.generators),'seconds:',round(time.time()-start,3),flush=True)
projections=[]
for g in Gp.generators:
    out=[];offset=0;new_offset=0
    for n in NVALUES:
        p=[g(offset+i)-offset for i in range(degree)]
        assert sorted(p)==list(range(degree))
        out.extend(new_offset+i for i in p)
        offset+=n*degree;new_offset+=degree
    projections.append(Permutation(out))
cache=here/'de_distribution_joint_generators.json'
cache.write_text(json.dumps([g.array_form for g in projections])+'\n')
J=PermutationGroup(projections)
J.schreier_sims();jorder=J.order()
print('Joint correction image order:',jorder,flush=True)
out=[];counts=[0,0];additive_counts=[0,0]
for index,(fw,qf,miss) in enumerate(base['words_for_further_tests']):
    original=[induced(fw,n)[0][0] for n in NVALUES]
    choices=[]
    for value in original:
        cchoices=[];yc=unit
        for c in range(6):
            correction=amul(ainv(value),(times(yc,qf),c))
            cchoices.append(aper(correction));yc=times(yc,qy)
        choices.append(cchoices)
    witness=None;tested=0
    for coeff in product(range(6),repeat=len(NVALUES)):
        p=[]
        for j,c in enumerate(coeff):p.extend(j*degree+k for k in choices[j][c])
        tested+=1
        if J.contains(Permutation(p),strict=True):witness=coeff;break
    counts[int(miss)]+=witness is not None
    additive_witness=None
    for a,b in product(range(6),repeat=2):
        coeff=(a,b,2*a%6,(a+b)%6,(2*a+b)%6)
        p=[]
        for j,c in enumerate(coeff):p.extend(j*degree+k for k in choices[j][c])
        if J.contains(Permutation(p),strict=True):additive_witness=coeff;break
    additive_counts[int(miss)]+=additive_witness is not None
    row={'certificate_index':index,'missing_coset':miss,'passes':witness is not None,
         'witness_c_values':witness,'tuples_tested':tested,
         'passes_with_c_multiplicativity':additive_witness is not None,
         'multiplicative_c_witness':additive_witness}
    out.append(row);print(json.dumps(row),flush=True)
result={'N_values':NVALUES,'representation_degree':total,'joint_correction_group_order':int(jorder),
        'joint_correction_group_source':'image of [N_B,N_B]',
        'pass_counts_by_CM_coset':counts,'multiplicative_c_pass_counts':additive_counts,'records':out,
        'scope':'Simultaneous finite distribution identities in H and c_N mod6 only; full GT generation and pentagon at the refinement are not asserted.'}
(here/'de_distribution_joint.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS: exact simultaneous correction test completed. Counts:',counts)
