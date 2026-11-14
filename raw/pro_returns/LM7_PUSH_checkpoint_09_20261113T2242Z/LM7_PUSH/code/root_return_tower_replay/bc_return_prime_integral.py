#!/usr/bin/env python3
"""Exact higher ell-adic affine return-cover and full centralizer replay.

The executed pairs have ord_p(ell)=p-1, so the integral coefficient ring
is literally (Z/ell^m)[zeta]/Phi_p(zeta).  No mod-ell matrix is silently
treated as an integral root of unity.
"""
from functools import lru_cache
from hashlib import sha256
from pathlib import Path
import argparse
import json
import time
import numpy as np
from bc_return_prime_model import ReturnModel,Element,matrix_power_mod

HERE = Path(__file__).resolve().parent


def solve_units(a,b,ell,modulus):
    a = np.asarray(a,dtype=np.int64)%modulus
    b = np.asarray(b,dtype=np.int64).reshape(a.shape[0],-1)%modulus
    aug = np.hstack([a,b]).copy()
    pivots=[]; r=0
    for c in range(a.shape[1]):
        nz = np.flatnonzero(aug[r:,c]%ell)
        if not len(nz):
            continue
        j=r+int(nz[0]); aug[[r,j]]=aug[[j,r]]
        aug[r]=aug[r]*pow(int(aug[r,c]),-1,modulus)%modulus
        ids=np.flatnonzero(aug[:,c]); ids=ids[ids != r]
        if len(ids):
            aug[ids]=(aug[ids]-aug[ids,c,None]*aug[r])%modulus
        pivots.append(c); r+=1
        if r == a.shape[0]:
            break
    assert not aug[r:,:a.shape[1]].any(), 'Nonunit Smith remainder must be retained.'
    assert not aug[r:,a.shape[1]:].any(), 'The exact integral equation is inconsistent.'
    ans=np.zeros((a.shape[1],b.shape[1]),dtype=np.int64)
    for i,c in enumerate(pivots):
        ans[c]=aug[i,a.shape[1]:]
    free=[j for j in range(a.shape[1]) if j not in pivots]
    kernel=np.zeros((a.shape[1],len(free)),dtype=np.int64)
    for k,j in enumerate(free):
        kernel[j,k]=1
        for i,c in enumerate(pivots):
            kernel[c,k]=-aug[i,j]%modulus
    assert np.array_equal(a@ans%modulus,b)
    assert not (a@kernel%modulus).any()
    return ans,kernel,len(pivots)


class IntegralReturnModel(ReturnModel):
    def __init__(self,ell,p,precision):
        base=ReturnModel(ell,p)
        self.__dict__.update(base.__dict__)
        self.precision=precision
        self.modulus=ell**precision
        assert self.f == p-1, 'This replay uses the full irreducible Phi_p polynomial.'
        self.zeta=np.zeros((self.f,self.f),dtype=np.int64)
        for j in range(self.f-1):
            self.zeta[j+1,j]=1
        self.zeta[:,-1]=-1%self.modulus
        self.zpowers=[np.eye(self.f,dtype=np.int64)]
        for _ in range(p):
            self.zpowers.append(self.zpowers[-1]@self.zeta%self.modulus)
        assert np.array_equal(self.zpowers[p],self.zpowers[0])
        assert np.array_equal(self.zeta%ell,base.zeta)
        self.local_x=self.local_identity(); self.local_x[0][0,0]=1; self.local_x[2][0]=1
        self.local_y=self.local_identity(); self.local_y[1][0]=1
        self.local_letters={1:self.local_x,2:self.local_y,
                            -1:self.local_inv(self.local_x),-2:self.local_inv(self.local_y)}
        self.letters={}
        for b in (0,1):
            vs=[]
            for i,row in enumerate(self.schreier_rows[str(b)]):
                h=self.local_word(tuple(row['F_word']))
                assert np.array_equal(h[1],base.letters[b].n[i])
                assert int(h[2][0]) == int(base.letters[b].c[i])
                vs.append(h[0])
            old=base.letters[b]
            self.letters[b]=Element(old.perm.copy(),old.c.copy(),old.n.copy(),np.array(vs))
        self.letters[-1]=self.inverse(self.letters[1])
        assert self.equal(self.power(self.letters[0],2),self.one)
        assert self.equal(self.power(self.letters[1],3),self.one)
        self.S,self.R=self.action(self.letters[0]),self.action(self.letters[1])
        self.T=self.S@self.R%self.modulus

    def local_act(self,n,c,v):
        v=np.roll(v,int(c),axis=0)
        return np.array([self.zpowers[int(a)]@b%self.modulus for a,b in zip(n,v)])

    def local_mul(self,a,b):
        av,an,ac=a; bv,bn,bc=b
        return ((av+self.local_act(an,ac[0],bv))%self.modulus,
                (an+np.roll(bn,int(ac[0])))%self.p,(ac+bc)%self.ell)

    def local_inv(self,a):
        v,n,c=a
        ci=-int(c[0])%self.ell
        ni=-np.roll(n,ci)%self.p
        return -self.local_act(ni,ci,v)%self.modulus,ni,np.array([ci])

    @lru_cache(None)
    def local_word(self,w):
        if not w:
            return self.local_identity()
        return self.local_mul(self.local_word(w[:-1]),self.local_letters[w[-1]])

    def mul(self,a,b):
        perm=b.perm[a.perm]
        c=(a.c+b.c[a.perm])%self.ell
        n=(a.n+np.array([np.roll(b.n[j],int(ci)) for j,ci in zip(a.perm,a.c)]))%self.p
        v=(a.v+np.array([self.local_act(ni,ci,b.v[j]) for j,ni,ci in zip(a.perm,a.n,a.c)]))%self.modulus
        return Element(perm,c,n,v)

    def inverse(self,a):
        perm=np.argsort(a.perm)
        c=-a.c[perm]%self.ell
        n=np.array([-np.roll(a.n[j],int(ci))%self.p for j,ci in zip(perm,c)])
        v=np.array([-self.local_act(ni,ci,a.v[j])%self.modulus for j,ni,ci in zip(perm,n,c)])
        return Element(perm,c,n,v)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--ell',type=int,default=5)
    parser.add_argument('--prime',type=int,default=7)
    parser.add_argument('--precision',type=int,default=2)
    args=parser.parse_args(); start=time.time()
    m=IntegralReturnModel(args.ell,args.prime,args.precision)
    ell,p,d,modulus=m.ell,m.p,m.dim,m.modulus
    oldstem=f'bc_return_prime_l{ell}_p{p}'
    stem=oldstem+f'_m{m.precision}'
    old=json.loads((HERE/(oldstem+'.json')).read_text())
    central=json.loads((HERE/(oldstem+'_centralizers.json')).read_text())
    oldnpz=np.load(HERE/(oldstem+'.npz'))
    wbasis=[]
    for w,v0 in zip(old['kernel_basis_B_words'],oldnpz['kernel_word_vectors']):
        h=m.word(w)
        assert m.in_kernel(h)
        v=h.v.reshape(d)
        assert np.array_equal(v%ell,v0)
        wbasis.append(v)
    wbasis=np.array(wbasis,dtype=np.int64)
    winv,_,wrank=solve_units(wbasis.T,np.eye(d,dtype=np.int64),ell,modulus)
    assert wrank == d
    eye=np.eye(d,dtype=np.int64)
    fixed=[]
    for a,expected in ((m.S,d//2),(m.R,d//3),(m.T,d//6)):
        _,kernel,rank=solve_units(eye-a,np.zeros(d,dtype=np.int64),ell,modulus)
        assert kernel.shape[1] == expected
        fixed.append(expected)
    tau=m.mul(m.letters[0],m.letters[1])
    assert m.equal(m.power(tau,2*ell**(m.precision+1)*p),m.one)
    assert not m.equal(m.power(tau,2*ell**m.precision*p),m.one)
    assert m.in_kernel(m.power(tau,2*ell*p))
    ci=matrix_power_mod(m.T,2*ell*p-1,modulus)
    assert np.array_equal(m.T@ci%modulus,eye)
    norm=np.hstack([eye-m.S,m.S@(eye-m.R)%modulus,(m.S@m.R)@(eye-ci)%modulus])%modulus
    right_inverse,_,nrank=solve_units(norm,eye,ell,modulus)
    assert nrank == d
    def comm(a,b):
        return m.mul(m.mul(m.mul(a,b),m.inverse(a)),m.inverse(b))
    source_elements={'s':m.letters[0],'r':m.letters[1],'tau':tau}
    lifted=[]; wcorrections=[]
    for row in central['centralizers']:
        name=row['element']; t=source_elements[name]; a=m.action(t)
        records=[]
        for rec in row['complete_base_centralizer_generators']:
            g=m.word(rec['base_B_word']); defect=comm(g,t)
            assert m.in_kernel(defect)
            solution,_,_=solve_units(eye-a,-defect.v.reshape(-1)%modulus,ell,modulus)
            v=solution[:,0]
            correction=Element(m.one.perm,m.one.c,m.one.n,v.reshape(6,ell,m.f))
            assert m.equal(comm(m.mul(correction,g),t),m.one)
            coefficients=winv@v%modulus
            assert np.array_equal(wbasis.T@coefficients%modulus,v)
            records.append({'base_B_word':rec['base_B_word'],
                            'actual_kernel_word_coefficients':coefficients.tolist()})
            wcorrections.append(v)
        lifted.append({'element':name,'projection_index':1,
                       'complete_base_centralizer_generators':records})
    rng=np.random.default_rng(460048+ell+p+m.precision)
    samples=[]
    for _ in range(12):
        v=rng.integers(0,modulus,size=d,dtype=np.int64)
        w=Element(m.one.perm,m.one.c,m.one.n,v.reshape(6,ell,m.f))
        wi=m.inverse(w)
        ss=m.mul(m.mul(w,m.letters[0]),wi)
        rr=m.mul(m.mul(w,m.letters[1]),wi)
        assert m.equal(m.power(ss,2),m.one) and m.equal(m.power(rr,3),m.one)
        tt=m.mul(ss,rr)
        assert m.equal(tt,m.mul(m.mul(w,tau),wi))
        samples.append(v)
    result={'status':'PASS_EXACT_INTEGRAL_RETURN_LAYER',
            'ell':ell,'prime':p,'precision':m.precision,'modulus':modulus,
            'integral_coefficient_polynomial':f'Phi_{p}',
            'primitive_root_identity_verified_mod_modulus':True,
            'actual_kernel_dimension':d,'literal_kernel_word_basis_is_invertible':True,
            's_r_tau_free_kernel_ranks':fixed,
            'all_nonzero_fixed_equation_Smith_factors_are_units':True,
            'peripheral_product_map_rank':nrank,
            'full_ordinary_peripheral_fibre_count':str(ell**(m.precision*d)),
            'tau_normalized_fibre_count':str(ell**(m.precision*d//6)),
            'base_tau_order':2*ell*p,'upper_tau_order':2*ell**(m.precision+1)*p,
            'full_base_centralizer_union':lifted,
            'all_centralizer_corrections_have_actual_word_preimages':True,
            'literal_inner_source_samples':len(samples),
            'input_sha256':{name:sha256((HERE/name).read_bytes()).hexdigest() for name in
                            ('bc_return_prime_model.py',oldstem+'.json',oldstem+'.npz',oldstem+'_centralizers.json')},
            'seconds':round(time.time()-start,3)}
    np.savez_compressed(HERE/(stem+'.npz'),S=m.S,R=m.R,T=m.T,
                        kernel_word_vectors=wbasis,kernel_word_inverse=winv,
                        peripheral_product_map=norm,peripheral_right_inverse=right_inverse,
                        centralizer_corrections=np.array(wcorrections),
                        inner_source_samples=np.array(samples))
    (HERE/(stem+'.json')).write_text(json.dumps(result,indent=2)+'\n')
    brief={k:v for k,v in result.items() if k != 'full_base_centralizer_union'}
    brief['centralizer_projection_indices']=[r['projection_index'] for r in lifted]
    brief['complete_centralizer_generator_counts']=[len(r['complete_base_centralizer_generators']) for r in lifted]
    print(json.dumps(brief,indent=2))


if __name__ == '__main__':
    main()
