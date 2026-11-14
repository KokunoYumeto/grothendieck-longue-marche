#!/usr/bin/env python3
"""Joint mod9 / degree-four Ferrari pentagon with the full B-core.

The second factor is the actual characteristic-three degree-four truncated Magnus
Ferrari kernel, retaining cubic powers and the complete finite B3 action.
Corrections range over the entire F-prime image of ker(B->G6).
"""
from contextlib import redirect_stdout
from pathlib import Path
from collections import deque
import io,json,runpy,time
import numpy as np
from de_ferrari_truncated_model import FerrariTruncated
from de_ferrari_mod9_lift import Jacobi,Induced,Span,rref,solve,free_abelianization

here=Path(__file__).resolve().parent

class Combined:
    def __init__(self):
        self.H9=Jacobi(9);self.H3=FerrariTruncated(4)
        self.one=np.r_[self.H9.one,self.H3.one]
        self.a=np.r_[self.H9.a,self.H3.a];self.b=np.r_[self.H9.b,self.H3.b];self.c=np.r_[self.H9.c,self.H3.c]
        self.x=np.column_stack((self.H9.x,self.H3.x));self.y=np.column_stack((self.H9.y,self.H3.y))
        self.pairs=tuple(zip(self.x,self.y))
        self.check_braids((self.a,self.b,self.c))
    def mul(self,x,y):return np.concatenate((self.H9.mul(x[...,:7],y[...,:7]),self.H3.mul(x[...,7:],y[...,7:])),axis=-1)
    def inv(self,x):return np.concatenate((self.H9.inv(x[...,:7]),self.H3.inv(x[...,7:])),axis=-1)
    def power(self,x,k):
        if k<0:return self.power(self.inv(x),-k)
        out=np.broadcast_to(self.one,x.shape).copy()
        while k:
            if k%2:out=self.mul(out,x)
            x=self.mul(x,x);k//=2
        return out
    def conj(self,x,y):return self.mul(self.mul(x,y),self.inv(x))
    def comm(self,x,y):return self.mul(self.mul(self.mul(x,y),self.inv(x)),self.inv(y))
    def word(self,w,gens=None):
        x,y=(self.x,self.y) if gens is None else gens
        images={1:x,-1:self.inv(x),2:y,-2:self.inv(y)}
        out=np.broadcast_to(self.one,x.shape).copy()
        from itertools import groupby
        for t,letters in groupby(w):
            exponent=sum(1 for _ in letters)
            out=self.mul(out,images[t] if exponent==1 else self.power(images[t],exponent))
        return out
    def pentagon(self,vals):return self.mul(self.mul(vals[0],vals[1]),self.inv(self.mul(self.mul(vals[2],vals[3]),vals[4])))
    def braid_images(self,vals):return self.a,self.conj(self.inv(vals[4]),self.b),self.conj(self.inv(vals[5]),self.c)
    def check_braids(self,images):
        a,b,c=images
        assert np.array_equal(self.mul(self.mul(a,b),a),self.mul(self.mul(b,a),b))
        assert np.array_equal(self.mul(self.mul(b,c),b),self.mul(self.mul(c,b),c))
        assert np.array_equal(self.mul(a,c),self.mul(c,a))
    def project(self,x):
        a=x[...,:7]%3;b=self.H3.project(x[...,7:])
        assert np.array_equal(a,b)
        return a
    def kernel_vector(self,x):
        d=(x[...,:7]-self.H9.one)%9;assert not np.any(d%3)
        return np.concatenate((d//3,self.H3.kernel_vector(x[...,7:])),axis=-1)
    def kernel_element(self,v):
        return np.concatenate(((self.H9.one+3*v[...,:7])%9,self.H3.kernel_element(v[...,7:])),axis=-1)

class InducedCombined(Induced):
    def __init__(self,H,d):
        self.H=H;self.d=d;self.Q=sorted(d['Q2']);self.ix={q:i for i,q in enumerate(self.Q)}
        self.root=self.ix[d['unit']];self.id=np.arange(6,dtype=np.int64)
        self.one=(self.id,np.broadcast_to(H.one,(6,6,len(H.one))).copy())
        sect={d['unit']:[]};todo=deque(sect)
        while todo:
            q=todo.popleft()
            for t,g in ((0,d['s2']),(1,d['r2'])):
                qn=d['mul2'](q,g)
                if qn not in sect:sect[qn]=sect[q]+[t];todo.append(qn)
        self.section=sect;self.letters={}
        for t,g in ((0,d['s2']),(1,d['r2']),(-1,d['r22'])):
            perm=[];values=[]
            for q in self.Q:
                qn=d['mul2'](q,g);perm.append(self.ix[qn])
                values.append(H.word(d['fword'](sect[q]+[t]+d['binv'](sect[qn]))))
            self.letters[t]=(np.array(perm,dtype=np.int64),np.array(values,dtype=np.int64))
        assert self.equal(self.power(self.letters[0],2),self.one)
        assert self.equal(self.power(self.letters[1],3),self.one)
        assert self.equal(self.inv(self.letters[1]),self.letters[-1])
        for fw,bw in (((1,),d['xword']),((2,),d['yword'])):
            el=self.word(bw);assert np.array_equal(el[0],self.id)
            assert np.array_equal(el[1][self.root],H.word(fw))
    def vector(self,x):
        assert np.array_equal(x[0],self.id)
        return self.H.kernel_vector(x[1]).ravel()
    def element(self,v):return self.id,self.H.kernel_element(v.reshape(6,6,79))

def module(H,W,d):
    start=time.time();N=[W.word(w) for w in d['Nwords']];dimension=36*79;C=Span(dimension)
    assert all(W.equal(W.power(n,9),W.one) for n in N)
    for i in range(97):
        for j in range(i+1,97):
            v=W.vector(W.comm(N[i],N[j]))
            if np.any(C.reduce(v)[0]):
                wi,wj=d['Nwords'][i],d['Nwords'][j]
                C.add(v,wi+wj+d['binv'](wi)+d['binv'](wj))
    at=0
    while at<len(C.basis):
        element=W.element(C.basis[at]);word=C.words[at]
        for i in range(97):C.add(W.vector(W.conj(N[i],element)),d['Nwords'][i]+word+d['binv'](d['Nwords'][i]))
        at+=1
    comm_rank=len(C.basis)
    print('Complete normal commutator image rank:',comm_rank,flush=True)
    power_vectors=np.column_stack([W.vector(W.power(n,6)) for n in N])
    old=np.load(here/'de_ferrari_mod9_module.npz');kernel=old['integral_abelianization_kernel']
    fab=old['N_F_abelianization'];assert not np.any(fab@kernel)
    for vec in kernel.T:
        v=power_vectors@vec%3
        if np.any(C.reduce(v)[0]):
            word=[]
            for i,c in enumerate(vec):
                if c:word+=d['bpower'](d['Nwords'][i],6*int(c))
            C.add(v,word)
    for v,word in zip(C.basis,C.words):
        assert not np.any(free_abelianization(d['fword'](word)))
        assert np.array_equal(W.vector(W.word(word)),v)
        for t in (0,1):C.coordinates(W.vector(W.conj(W.letters[t],W.element(v))))
    Full=Span(dimension)
    for v,w in zip(C.basis,C.words):Full.add(v,w)
    for i in range(97):Full.add(power_vectors[:,i],d['bpower'](d['Nwords'][i],6))
    for v in Full.basis:
        for n in N:Full.coordinates(W.vector(W.conj(n,W.element(v))))
    rng=np.random.default_rng(212026)
    for _ in range(100):
        a=Full.matrix()@rng.integers(0,3,size=len(Full.basis))%3
        b=Full.matrix()@rng.integers(0,3,size=len(Full.basis))%3
        assert np.array_equal(W.vector(W.mul(W.element(a),W.element(b))),(a+b)%3)
    metadata={'commutator_normal_image_dimension':comm_rank,
              'F_prime_correction_image_dimension':len(C.basis),
              'full_G6_kernel_image_dimension':len(Full.basis),
              'all_N_ninth_powers_trivial':True,
              'module_build_seconds':round(time.time()-start,3)}
    certificate={'F_prime_correction_image_basis':C.matrix(),
                 'full_G6_kernel_image_basis':Full.matrix(),
                 'N_sixth_power_images':power_vectors,
                 'integral_F_abelianization_kernel':kernel}
    print(json.dumps(metadata),flush=True)
    return C,Full,metadata,certificate

def errors(H,values):
    aa,bb,cc=H.braid_images(values)
    residuals=[H.pentagon(values),
        H.mul(H.mul(H.mul(aa,bb),aa),H.inv(H.mul(H.mul(bb,aa),bb))),
        H.mul(H.mul(H.mul(bb,cc),bb),H.inv(H.mul(H.mul(cc,bb),cc))),
        H.comm(aa,cc)]
    return np.concatenate([H.kernel_vector(x) for x in residuals])

def lift(H,W,d,C,Full,certificate):
    records=json.loads((here/'de_ferrari_fibres.json').read_text())['records']
    rank=len(C.basis);I=np.eye(rank,dtype=np.int64);CM=C.matrix()
    s,r=W.letters[0],W.letters[1];t=W.mul(s,r)
    x=W.word(d['xword']);u=W.word([-1,0]);v=W.word([0,-1])
    rng=np.random.default_rng(212027);rows=[];start=time.time()
    for ix,rec in enumerate(records):
        beta=W.word(rec['base_beta_word_B']);S=W.conj(beta,s);R=W.mul(S,t)
        E=C.coordinates(W.vector(W.power(R,3)))
        SM=np.column_stack([C.coordinates(W.vector(W.conj(S,W.element(a)))) for a in C.basis])
        RM=np.column_stack([C.coordinates(W.vector(W.conj(R,W.element(a)))) for a in C.basis])
        assert np.array_equal(SM@SM%3,I) and np.array_equal(RM@RM@RM%3,I)
        gentleA=np.vstack(((I+SM)%3,(I+RM+RM@RM)%3));gentleb=np.r_[np.zeros(rank,dtype=np.int64),E]
        g=rec['integral_cusp_gauge'];xg=W.power(x,g)
        fbase=W.mul(s,W.conj(xg,S));basevals=fbase[1][W.root]
        assert np.array_equal(basevals,H.word(rec['actual_commutator_word_f']))
        def values(z):
            kk=W.conj(xg,W.element(CM@z%3))
            return H.mul(basevals,kk[1][W.root])
        error=errors(H,basevals)
        J=np.column_stack([(errors(H,values(I[:,j]))-error)%3 for j in range(rank)])
        # Affineness follows from the proved abelian kernel.  Basis-pair
        # checks and 100 further full substitutions audit implementation.
        for i in range(rank):
            for j in range(i,rank):
                z=(I[:,i]+I[:,j])%3
                assert np.array_equal(errors(H,values(z)),(error+J@z)%3)
        for _ in range(100):
            z=rng.integers(0,3,size=rank)
            assert np.array_equal(errors(H,values(z)),(error+J@z)%3)
        A=np.vstack((gentleA,J));b=np.r_[gentleb,-error%3]
        sol=solve(A,b);gentlesol=solve(gentleA,gentleb)
        row={'certificate_index':ix,'missing_coset':rec['missing_coset'],
             'correction_dimension':rank,'gentle_norm_rank':len(rref(gentleA)[1]),
             'pentagon_rank':len(rref(J[:79])[1]),'braid_equation_rank':len(rref(J[79:])[1]),
             'combined_equation_rank':len(rref(A)[1]),
             'gentle_lift_exists':gentlesol is not None,'simultaneous_lift_exists':sol is not None}
        certificate[f'norm_matrix_{ix}']=gentleA;certificate[f'norm_rhs_{ix}']=gentleb
        certificate[f'pentagon_braid_matrix_{ix}']=J;certificate[f'pentagon_braid_constant_{ix}']=error
        if sol is not None:
            z,K=sol;kelem=W.element(CM@z%3);newS=W.mul(S,kelem);newR=W.mul(W.inv(kelem),R)
            assert W.equal(W.power(newS,2),W.one) and W.equal(W.power(newR,3),W.one)
            assert W.equal(W.mul(newS,newR),t)
            kw=[]
            for coefficient,w in zip(z,C.words):kw+=w*int(coefficient)
            assert W.equal(W.word(kw),kelem)
            cg=d['bpower'](d['xword'],g)
            fw=d['fword']([0]+cg+rec['base_beta_word_B']+[0]+d['binv'](rec['base_beta_word_B'])+kw+d['binv'](cg))
            assert not np.any(free_abelianization(fw))
            vv=H.word(fw);assert np.array_equal(vv,values(z))
            assert np.array_equal(H.pentagon(vv),H.one);H.check_braids(H.braid_images(vv))
            ff=W.mul(s,W.conj(xg,newS));fi=W.inv(ff)
            hex1=W.mul(W.mul(W.mul(W.mul(u,fi),v),ff),W.inv(W.mul(fi,r)))
            hex2=W.mul(W.mul(W.mul(W.mul(fi,v),ff),u),W.inv(W.mul(W.mul(v,u),ff)))
            assert W.equal(hex1,W.one) and W.equal(hex2,W.one)
            images={0:newS,1:newR,-1:W.inv(newR)}
            def imword(word):
                out=W.one
                for letter in word:out=W.mul(out,images[letter])
                return out
            newN=[imword(w) for w in d['Nwords']];generation=Span(36*79)
            for ni in newN:generation.add(W.vector(W.power(ni,6)),[])
            for i in range(97):
                for j in range(i+1,97):generation.add(W.vector(W.comm(newN[i],newN[j])),[])
            at=0
            while at<len(generation.basis):
                element=W.element(generation.basis[at])
                for ni in newN:generation.add(W.vector(W.conj(ni,element)),[])
                at+=1
            assert len(generation.basis)==len(Full.basis)
            for v0 in Full.basis:generation.coordinates(v0)
            row.update({'correction_coefficients':z.tolist(),'homogeneous_correction_basis':K.tolist(),
                        'literal_B_correction_word':kw,'actual_F_commutator_word':list(fw),
                        'both_complete_hexagons_verified_in_combined_core':True,
                        'complete_pentagon_verified_in_both_targets':True,
                        'all_three_braid_relations_verified_in_both_targets':True,
                        'source_kernel_generation_rank':len(generation.basis),
                        'surjective_three_strand_shadow_map':True})
        rows.append(row)
        print(json.dumps({k:v for k,v in row.items() if k not in
                         ('literal_B_correction_word','actual_F_commutator_word','homogeneous_correction_basis')}),flush=True)
    return rows,round(time.time()-start,3)

def main():
    with redirect_stdout(io.StringIO()):d=runpy.run_path(str(here/'de_distribution_test.py'))
    H=Combined();W=InducedCombined(H,d)
    C,Full,metadata,certificate=module(H,W,d)
    np.savez_compressed(here/'de_ferrari_degree4_module.npz',**certificate)
    here.joinpath('de_ferrari_degree4_module.json').write_text(json.dumps({**metadata,
        'literal_B_words_for_F_prime_basis':C.words,'full_kernel_basis_words':Full.words,
        'coset_section':{str(k):w for k,w in W.section.items()}},indent=2)+'\n')
    rows,seconds=lift(H,W,d,C,Full,certificate)
    np.savez_compressed(here/'de_ferrari_degree4_lift_certificate.npz',**certificate)
    output={**metadata,'joint_target':'mod9 Jacobi target and the actual degree4 characteristic3 Ferrari target',
            'records':rows,'pass_counts':[sum(r['simultaneous_lift_exists'] and r['missing_coset']==b for r in rows) for b in (False,True)],
            'calculation_seconds':seconds,
            'scope':'Entire common F-prime kernel image over the retained E17 G6 points, with complete compatible three-strand norms and generation and simultaneous actual four-strand pentagons. No full profinite lifting inference.'}
    here.joinpath('de_ferrari_degree4_lift.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({k:v for k,v in output.items() if k!='records'},indent=2),flush=True)

if __name__=='__main__':main()
