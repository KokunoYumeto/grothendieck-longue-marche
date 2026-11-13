#!/usr/bin/env python3
"""Direct rank-ten Fermat Schreier collector and arbitrary Ihara action.

F=<x,y>, N=ker(F -> (Z/3)^2), section c(a,b)=x^a y^b (0<=a,b<3).
N/(gamma3(N) N^3) has BCH coordinates F3^10 + Lambda^2(F3^10).
A coordinate z_ij=1 is the commutator [n_i,n_j], with convention aba^-1b^-1.
Literal F words use 1=x, 2=y and their negatives. Mixed words may include
N-blocks (a,z). The alpha action is x->x^chi, y->f^-1 y^chi f.
"""
from pathlib import Path
from functools import cache
from itertools import product
import json,time
import numpy as np
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form,hermite_normal_form
from sympy.polys.domains import ZZ

HERE=Path(__file__).resolve().parent
Q=list(product(range(3),repeat=2)); ONE=(0,0)
UP=np.triu_indices(10,1)

def free_reduce(w):
    out=[]
    for a in w:
        if out and out[-1]==-a:out.pop()
        else:out.append(a)
    return out

def inverse_word(w):
    return [-a for a in reversed(w)]

def section(q):return [1]*q[0]+[2]*q[1]

def step(q,l):
    a=list(q);a[abs(l)-1]=(a[abs(l)-1]+(1 if l>0 else -1))%3
    return tuple(a)

EDGES={};NWORDS=[];EDGE_LABELS=[]
for q in Q:
    for l in (1,2):
        w=free_reduce(section(q)+[l]+inverse_word(section(step(q,l))))
        if w:
            EDGES[q,l]=len(NWORDS)+1;NWORDS.append(w);EDGE_LABELS.append((q,l))
        else:EDGES[q,l]=0
assert len(NWORDS)==10

def schreier(word):
    q=ONE;out=[]
    for l in word:
        qn=step(q,l)
        a=EDGES[q,l] if l>0 else -EDGES[qn,-l]
        if a:out.append(a)
        q=qn
    assert q==ONE
    return out

for i,w in enumerate(NWORDS):assert free_reduce(schreier(w))==[i+1]

def zero():return np.zeros(10,dtype=np.int64),np.zeros(45,dtype=np.int64)

def multiply(g,h):
    a,z=g;b,w=h
    return (a+b)%3,(z+w+2*(np.outer(a,b)-np.outer(b,a))[UP])%3

def inverse(g):return tuple(-a%3 for a in g)

def collect_nword(word):
    out=zero()
    for l in word:
        a,z=zero();a[abs(l)-1]=1 if l>0 else -1
        out=multiply(out,(a,z))
    return out

def literal(word):return collect_nword(schreier(word))

def exterior(A):
    return np.stack([(np.outer(A[:,i],A[:,j])-np.outer(A[:,j],A[:,i]))[UP]%3
                     for i,j in zip(*UP)],axis=1)

@cache
def action(q):
    w=section(q);a=[];z=[]
    for n in NWORDS:
        aa,zz=literal(w+n+inverse_word(w));a.append(aa);z.append(zz)
    A=np.stack(a,axis=1);tau=np.stack(z,axis=1)
    return A,tau,exterior(A)

def acted(q,g):
    a,z=g;A,tau,W=action(q)
    return A@a%3,(tau@a+W@z)%3

def collect(word):
    q=ONE;out=zero()
    for token in word:
        if isinstance(token,tuple):out=multiply(out,acted(q,token));continue
        qn=step(q,token)
        a=EDGES[q,token] if token>0 else -EDGES[qn,-token]
        if a:
            b,z=zero();b[abs(a)-1]=1 if a>0 else -1
            out=multiply(out,(b,z))
        q=qn
    assert q==ONE
    return out

def mixed_inverse(word):
    return [inverse(t) if isinstance(t,tuple) else -t for t in reversed(word)]

def alpha_word(word,fa,fz,chi=7):
    assert chi>0 and chi%3
    f=(np.asarray(fa,dtype=np.int64)%3,np.asarray(fz,dtype=np.int64)%3)
    images={1:[1]*chi,2:[inverse(f)]+[2]*chi+[f]}
    images[-1]=mixed_inverse(images[1]);images[-2]=mixed_inverse(images[2])
    out=[]
    for l in word:out+=images[l]
    return out

def generator_images(fa,fz,chi=7):
    values=[collect(alpha_word(w,fa,fz,chi)) for w in NWORDS]
    return np.stack([a for a,z in values],axis=1),np.stack([z for a,z in values],axis=1)

def rank(A,p=3):
    A=np.asarray(A,dtype=np.int64).copy()%p;r=0
    for j in range(A.shape[1]):
        ids=np.flatnonzero(A[r:,j])
        if not len(ids):continue
        a=r+int(ids[0]);A[[r,a]]=A[[a,r]];A[r]=A[r]*pow(int(A[r,j]),-1,p)%p
        for a in range(A.shape[0]):
            if a!=r:A[a]=(A[a]-A[a,j]*A[r])%p
        r+=1
        if r==A.shape[0]:break
    return r

def integral_abel(word):
    out=np.zeros(10,dtype=np.int64)
    for l in schreier(word):out[abs(l)-1]+=1 if l>0 else -1
    return out

CUSP_WORDS={}
for b in range(3):CUSP_WORDS[f'x{b}']=[2]*b+[1]*3+[-2]*b
for a in range(3):CUSP_WORDS[f'y{a}']=[1]*a+[2]*3+[-1]*a
for a in range(3):CUSP_WORDS[f'z{a}']=[1]*a+[-2,-1]*3+[-1]*a
CUSP_LABELS=list(CUSP_WORDS)
CUSP_VECTORS=np.stack([integral_abel(w) for w in CUSP_WORDS.values()],axis=1)
assert not np.any(CUSP_VECTORS.sum(axis=1))
SM=smith_normal_form(sp.Matrix(CUSP_VECTORS.tolist()),domain=ZZ)
assert [abs(int(SM[i,i])) for i in range(9)]==[1]*8+[0]
left=sp.Matrix(CUSP_VECTORS.T.tolist()).nullspace()
B=sp.Matrix.vstack(*[(v*sp.ilcm(*[a.q for a in v])).T for v in left])
HNF=hermite_normal_form(B);TT=HNF.inv()*B
assert all(a.q==1 for a in TT)
TATE_QUOTIENT=np.array(TT.tolist(),dtype=np.int64)
assert not np.any(TATE_QUOTIENT@CUSP_VECTORS)
ST=smith_normal_form(TT,domain=ZZ)
assert [abs(int(ST[i,i])) for i in range(2)]==[1,1]
F_AB_DIV3=np.array([[sum((1 if l==j else -1 if l==-j else 0) for l in w)//3
                     for w in NWORDS] for j in (1,2)],dtype=np.int64)

def polynomial_data(chi=7):
    fa,fz=zero();a0,z0=generator_images(fa,fz,chi)
    ah=[];zh=[];zs=[];diag=[];ones=[]
    for i in range(10):
        u=fa.copy();u[i]=1;a1,z1=generator_images(u,fz,chi)
        u[i]=2;a2,z2=generator_images(u,fz,chi)
        assert np.array_equal((a2-a0)%3,2*(a1-a0)%3)
        ah.append((a1-a0)%3);zh.append((z2-z1)%3)
        diag.append((2*z1-z2-z0)%3);ones.append(z1)
    cross=[];pairs=[]
    for i in range(10):
        for j in range(i+1,10):
            u=fa.copy();u[i]=u[j]=1;aa,zz=generator_images(u,fz,chi)
            cross.append((zz-ones[i]-ones[j]+z0)%3);pairs.append((i,j))
    for i in range(45):
        z=fz.copy();z[i]=1;aa,zz=generator_images(fa,z,chi)
        assert np.array_equal(aa,a0);zs.append((zz-z0)%3)
    return {'chi':np.array(chi),'constant_ab':a0,'constant_central':z0,
            'homology_linear':np.stack(ah),'central_linear_homology':np.stack(zh),
            'central_square_homology':np.stack(diag),'central_cross_homology':np.stack(cross),
            'central_linear_central':np.stack(zs),'cross_pairs':np.array(pairs)}

def polynomial_evaluate(data,fa,fz):
    fa=np.asarray(fa);fz=np.asarray(fz)
    a=data['constant_ab']+np.einsum('i,ijk->jk',fa,data['homology_linear'])
    z=data['constant_central']+np.einsum('i,ijk->jk',fa,data['central_linear_homology'])
    z+=np.einsum('i,ijk->jk',fa*fa,data['central_square_homology'])
    z+=np.einsum('i,ijk->jk',fz,data['central_linear_central'])
    pairs=data['cross_pairs'];z+=np.einsum('i,ijk->jk',fa[pairs[:,0]]*fa[pairs[:,1]],data['central_cross_homology'])
    return a%3,z%3

def main():
    start=time.time();rng=np.random.default_rng(222026);checks=0
    for q in Q:
        for trial in range(3):
            w=[]
            for i in rng.choice(10,size=4,replace=False):w+=NWORDS[int(i)]
            a,z=literal(w);path=section(q)
            assert all(np.array_equal(b,c) for b,c in zip(literal(path+w+inverse_word(path)),collect(path+[(a,z)]+inverse_word(path))))
            checks+=1
    data=polynomial_data(7)
    complex_images=[literal([-l for l in w]) for w in NWORDS]
    ca,cz=generator_images(*zero(),chi=8)
    assert np.array_equal(ca,np.stack([a for a,z in complex_images],axis=1))
    assert np.array_equal(cz,np.stack([z for a,z in complex_images],axis=1))
    complex_integral=np.stack([integral_abel([-l for l in w]) for w in NWORDS],axis=1)
    cusp_permutation={}
    for label,w in CUSP_WORDS.items():
        typ=label[0];a=int(label[1]);b=(-a-1 if typ=='z' else -a)%3
        image=f'{typ}{b}';cusp_permutation[label]=image
        k=(-a-1-b)//3 if typ=='z' else (-a-b)//3
        generator=1 if typ in ('y','z') else 2
        conjugator=[generator]*(3*k) if k>=0 else [-generator]*(-3*k)
        target=conjugator+inverse_word(CUSP_WORDS[image])+inverse_word(conjugator)
        assert free_reduce([-l for l in w]+inverse_word(target))==[]
        assert np.array_equal(complex_integral@integral_abel(w),-integral_abel(CUSP_WORDS[image]))
    for trial in range(25):
        fa=rng.integers(0,3,size=10);fz=rng.integers(0,3,size=45)
        a,z=generator_images(fa,fz,7);ap,zp=polynomial_evaluate(data,fa,fz)
        assert np.array_equal(a,ap) and np.array_equal(z,zp) and rank(a)==10
    extra={'N_basis_words':np.array(NWORDS,dtype=object),'cusp_vectors':CUSP_VECTORS,
           'proper_T_quotient':TATE_QUOTIENT,'F_abelianization_divided_by_3':F_AB_DIV3,
           'complex_conjugation_integral_ab':complex_integral,'complex_conjugation_central':cz}
    for label,q in (('x',(1,0)),('y',(0,1))):
        A,tau,W=action(q);extra[f'action_{label}_ab']=A;extra[f'action_{label}_central_cochain']=tau;extra[f'action_{label}_wedge']=W
    # Words are stored in JSON, so the NPZ contains only ordinary integer arrays.
    extra.pop('N_basis_words')
    np.savez_compressed(HERE/'de_fermat_schreier_certificate.npz',**data,**extra)
    out={'free_generators':'1=x,2=y; negative integers are inverse letters',
         'coset_section':'c(a,b)=x^a y^b for a,b in {0,1,2}',
         'N_rank':10,'class_two_coordinate_dimensions':[10,45],
         'BCH_product':'(a,z)*(b,w)=(a+b,z+w+(1/2) a wedge b), 1/2=2 in F3',
         'basis_words':NWORDS,'basis_positive_edges':[[list(q),l] for q,l in EDGE_LABELS],
         'cusp_words':CUSP_WORDS,'cusp_labels':CUSP_LABELS,'cusp_vectors':CUSP_VECTORS.tolist(),
         'cusp_Smith_factors':[1]*8,'proper_T_quotient':TATE_QUOTIENT.tolist(),
         'F_abelianization_divided_by_3':F_AB_DIV3.tolist(),
         'chosen_omitted_cusp_for_eight_column_basis':'x0=O for t=-z^3/x^3, u=-z/x, v=-y/x',
         'geometric_cusp_comparison':{'x_b':'[1:-zeta^b:0]',
             'y_a':'[1:0:-zeta^a]',
             'named_points':{'x0':'O','x1':'C','x2':'Cbar','y0':'Qc','y1':'Bbar','y2':'B','z0':'A','z1':'P','z2':'Abar'}},
         'based_map':'t=-s^3 at O, s=z/x; comparison of tangents -1 and +1 uses compatible rational odd roots of -1',
         'complex_conjugation_cusp_permutation':cusp_permutation,
         'infinity_alignment_proof':'c acts x->x^-1,y->y^-1. Exactly c(z_a)=x^(3k) z_b^-1 x^(-3k), b=-a-1 mod3, 3k=-a-1-b. Thus z1 is the rational infinity cusp P; the deck x gives the remaining named points.',
         'complex_conjugation_checks':'All9 cusp conjugacy identities checked as literal free words; chi8,f1 agrees on all10 full class2 generator images with letterwise inversion.',
         'chi':7,'literal_block_action_checks':checks,'polynomial_and_generation_random_checks':25,
         'central_parameter_influence_rank':rank(data['central_linear_central'].reshape(45,-1)),
         'elapsed_seconds':round(time.time()-start,3),
         'scope':'Exact finite Ihara substitution for arbitrary f in N/(gamma3 N N^3). GT equations and arithmetic identification of f_sigma are not imposed by this module.'}
    (HERE/'de_fermat_schreier.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('basis_words','basis_positive_edges','cusp_words','cusp_vectors')},indent=2))

if __name__=='__main__':main()
