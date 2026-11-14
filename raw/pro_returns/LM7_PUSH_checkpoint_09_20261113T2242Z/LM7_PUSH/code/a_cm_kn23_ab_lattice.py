#!/usr/bin/env python3
"""Integral word basis for (K6 intersect F-prime)/N-prime = 6 ker(e).

All unimodular column operations and their integer inverse are retained.
The 95 actual N-words have exactly zero integral F-exponents, and their
sixth powers are the additional full-fibre correction generators.
"""
from pathlib import Path
from hashlib import sha256
from math import gcd
from functools import reduce
import json
import time
import numpy as np

from a_cm_kn23_model import permword


HERE=Path(__file__).resolve().parent


def red(word):
    ans=[]
    for a in word:
        if ans and ans[-1]==-a:ans.pop()
        else:ans.append(a)
    return ans


def wordpower(word,k):
    return word*k if k>=0 else [-a for a in word[::-1]]*(-k)


def egcd(a,b):
    aa,bb=abs(a),abs(b);s0,s1,t0,t1=1,0,0,1
    while bb:
        q=aa//bb;aa,bb=bb,aa-q*bb;s0,s1=s1,s0-q*s1;t0,t1=t1,t0-q*t1
    return aa,s0*(1 if a>=0 else -1),t0*(1 if b>=0 else -1)


def main():
    start=time.monotonic();meta=json.loads((HERE/'a_cm_kn23_model.json').read_text())
    data=np.load(HERE/'a_cm_kn23_model.npz')
    words=meta['source_basis_words_in_F'];n=len(words);assert n==97
    exponent=lambda w:[sum(1 if a==k else -1 if a==-k else 0 for a in w) for k in (1,2)]
    original=np.array([exponent(w) for w in words],dtype=object).T
    E=original.copy();U=np.eye(n,dtype=object);V=np.eye(n,dtype=object);steps=[]

    def swap(i,j):
        if i==j:return
        E[:,[i,j]]=E[:,[j,i]];U[:,[i,j]]=U[:,[j,i]];V[[i,j],:]=V[[j,i],:]
        steps.append({'operation':'swap','columns':[i,j]})

    def pivot(row,p):
        at=next(j for j in range(p,n) if E[row,j])
        swap(p,at)
        for j in range(p+1,n):
            if not E[row,j]:continue
            a,b=int(E[row,p]),int(E[row,j]);d,s,t=egcd(a,b)
            assert s*a+t*b==d and d>0
            cp,cj=E[:,p].copy(),E[:,j].copy()
            E[:,p]=s*cp+t*cj;E[:,j]=(-b//d)*cp+(a//d)*cj
            cp,cj=U[:,p].copy(),U[:,j].copy()
            U[:,p]=s*cp+t*cj;U[:,j]=(-b//d)*cp+(a//d)*cj
            rp,rj=V[p,:].copy(),V[j,:].copy()
            V[p,:]=(a//d)*rp+(b//d)*rj;V[j,:]=-t*rp+s*rj
            steps.append({'operation':'bezout','columns':[p,j],'row':row,
                          'a':a,'b':b,'gcd':d,'s':s,'t':t})
        if E[row,p]<0:
            E[:,p]*=-1;U[:,p]*=-1;V[p,:]*=-1
            steps.append({'operation':'negate','column':p})

    pivot(0,0);pivot(1,1)
    assert all(E[0,j]==0 for j in range(1,n))
    assert all(E[1,j]==0 for j in range(2,n))
    assert E[0,0]>0 and E[1,1]>0
    assert np.array_equal(original@U,E)
    assert np.array_equal(U@V,np.eye(n,dtype=object))
    assert np.array_equal(V@U,np.eye(n,dtype=object))
    g,h,b=int(E[0,0]),int(E[1,1]),int(E[1,0])
    d1=reduce(gcd,(abs(int(v)) for v in original.ravel()),0)
    assert d1==gcd(gcd(g,h),abs(b))
    d2=g*h//d1
    assert g*h==d1*d2 and d2%d1==0
    assert max(abs(int(v)) for v in U.ravel())<2**63
    assert max(abs(int(v)) for v in V.ravel())<2**63

    source=data['common_N'];fulln=source.shape[1]
    old=np.load(HERE/'a_cm_distribution_orbifold.npz')
    points=np.r_[old['retained_projection_points'],5331+data['retained_projection_points']]
    inverse=np.full(fulln,-1,dtype=np.int64);inverse[points]=np.arange(len(points))
    kernelwords=[];values=[];sixths=[];projected=[];projected_sixths=[]
    inverses=[np.argsort(p).astype(np.uint16) for p in source]
    for j in range(2,n):
        w=[];p=np.arange(fulln,dtype=np.uint16)
        coeff=[int(c) for c in U[:,j]]
        for i,k in enumerate(coeff):
            if not k:continue
            w=red(w+wordpower(words[i],k))
            q=source[i] if k>0 else inverses[i]
            for _ in range(abs(k)):p=q[p]
        assert exponent(w)==[0,0]
        assert np.array_equal(permword(w,data['F_generators']),p[5331:]-5331)
        p2=p[p];p4=p2[p2];p6=p2[p4]
        q=inverse[p[points]];q6=inverse[p6[points]]
        assert np.all(q>=0) and np.all(q6>=0)
        assert np.array_equal(q6,q[q[q[q[q[q]]]]])
        kernelwords.append({'kernel_basis_index':j-2,'N_abelian_column':coeff,
                            'literal_F_word':w,'exact_integral_F_exponents':[0,0]})
        values.append(p);sixths.append(p6);projected.append(q);projected_sixths.append(q6)
    out={'status':'PASS_EXACT_INTEGRAL_K6_FPRIME_LATTICE_WORD_MAP',
         'rank_N_abelianization':97,'rank_integral_exponent_image':2,'kernel_rank':95,
         'triangular_exponent_image':[[g,0],[b,h]],
         'integral_exponent_image_index':g*h,'cokernel_Smith_factors':[d1,d2],
         'all_unimodular_steps':steps,'integer_inverse_checked_in_both_orders':True,
         'all_kernel_columns_have_zero_exact_exponents':True,
         'all_95_literal_kernel_words_replayed':True,
         'all_sixth_powers_replayed_in_full_and_projected_sources':True,
         'exact_profinite_quotient':'(K6 intersect F-prime)/N-prime = 6 ker(e)',
         'profinite_torsion_gate':'Nonzero integers are injective on Zhat; the explicit '
                    'unimodular inverse identifies ker(e) with Zhat^95 at every prime.',
         'kernel_words':kernelwords,
         'input_sha256':{name:sha256((HERE/name).read_bytes()).hexdigest() for name in
                        ['a_cm_kn23_model.py','a_cm_kn23_model.json','a_cm_kn23_model.npz',
                         'a_cm_distribution_orbifold.npz']},
         'seconds':round(time.monotonic()-start,6)}
    np.savez_compressed(HERE/'a_cm_kn23_ab_lattice.npz',
                        integral_exponent_matrix=np.array(original,dtype=np.int64),
                        unimodular_columns=np.array(U,dtype=np.int64),
                        unimodular_inverse=np.array(V,dtype=np.int64),
                        transformed_exponent_matrix=np.array(E,dtype=np.int64),
                        kernel_basis_full_values=np.array(values),
                        kernel_basis_sixth_full_values=np.array(sixths),
                        kernel_basis_projected_values=np.array(projected),
                        kernel_basis_sixth_projected_values=np.array(projected_sixths))
    (HERE/'a_cm_kn23_ab_lattice.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in {'all_unimodular_steps','kernel_words'}},indent=2))


if __name__=='__main__':main()
