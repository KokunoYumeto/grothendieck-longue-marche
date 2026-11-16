#!/usr/bin/env python3
"""Exact finite frame detector for multiplier-one actual gentle pairs.

The finite arithmetic input is in the temporary marking x=tau^-2,y=s*x*s.
A supplied finite-compatible residue is NOT asserted to lift to a full pair.
Default execution verifies the finite base, coset modules and frame solver.
Use --word-json FILE for signed x/y letters (1,2,-1,-2), or
--residue-json FILE for {v2:[288 entries],v3:[192 entries],base:[4 entries]}.
"""
from pathlib import Path
import argparse
import hashlib
import json
from collections import deque

MOD=12
I=(1,0,0,1)
S=(0,1,11,0)
U=(1,1,0,1)

def mm(a,b):
    return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2))%MOD
                 for i in range(2) for j in range(2))
def inv(a):
    return (a[3],-a[1]%MOD,-a[2]%MOD,a[0])
def canon(a):
    a=tuple(x%MOD for x in a)
    return min(a,tuple(-x%MOD for x in a))
def mul(a,b):return canon(mm(a,b))
def power(a,n):
    if n<0:return power(canon(inv(a)),-n)
    z=I
    while n:
        if n&1:z=mul(z,a)
        a=mul(a,a);n//=2
    return z

def generated(gens):
    gens=list(gens)+[canon(inv(x)) for x in gens]
    found={I};todo=[I]
    while todo:
        a=todo.pop()
        for b in gens:
            c=mul(a,b)
            if c not in found:found.add(c);todo.append(c)
    return found

def derived(group):
    return generated([mul(mul(mul(a,b),canon(inv(a))),canon(inv(b)))
                      for a in group for b in group])

class Detector:
    def __init__(self):
        self.s=canon(S);self.r=mul(self.s,canon(inv(U)))
        self.tau=mul(self.s,self.r)
        self.Q=sorted(generated([self.s,self.r]));self.index={q:i for i,q in enumerate(self.Q)}
        assert len(self.Q)==576
        self.x=power(self.tau,-2);self.y=mul(mul(self.s,self.x),self.s)
        self.pure=sorted(generated([self.x,self.y]))
        assert len(self.pure)==96
        assert set(self.pure)=={q for q in self.Q if tuple(a%2 for a in q)==I}
        self.subgroups=[[I,self.s],[I,self.r,power(self.r,2)]]
        self.reps=[];self.coset_of=[];self.perm_cache={}
        for H in self.subgroups:
            coset_of={};reps=[]
            for q in self.Q:
                if q in coset_of:continue
                i=len(reps);reps.append(q)
                for h in H:coset_of[mul(q,h)]=i
            self.reps.append(reps);self.coset_of.append(coset_of)
        assert list(map(len,self.reps))==[288,192]
        self.zero=(tuple([0]*288),tuple([0]*192),I)
        ds=[0]*288;dr=[0]*192
        ds[self.coset_of[0][I]]=1;dr[self.coset_of[1][I]]=1
        self.shat=(tuple(ds),self.zero[1],self.s)
        self.rhat=(self.zero[0],tuple(dr),self.r)
        self.tauhat=self.gmul(self.shat,self.rhat)
        self.xhat=self.gpow(self.tauhat,-2)
        self.yhat=self.gmul(self.gmul(self.shat,self.xhat),self.shat)
        assert self.gpow(self.shat,2)==self.zero
        assert self.gpow(self.rhat,3)==self.zero

    def permutation(self,q,part):
        key=(q,part)
        if key not in self.perm_cache:
            self.perm_cache[key]=tuple(self.coset_of[part][mul(q,a)] for a in self.reps[part])
        return self.perm_cache[key]
    def act(self,q,v,part):
        out=[0]*len(v)
        for i,j in enumerate(self.permutation(q,part)):out[j]=v[i]
        return tuple(out)
    def gmul(self,a,b):
        out=[]
        for part,p in enumerate((2,3)):
            bv=self.act(a[2],b[part],part)
            out.append(tuple((x+y)%p for x,y in zip(a[part],bv)))
        return (out[0],out[1],mul(a[2],b[2]))
    def ginv(self,a):
        qi=canon(inv(a[2]));out=[]
        for part,p in enumerate((2,3)):
            out.append(tuple(-x%p for x in self.act(qi,a[part],part)))
        return (out[0],out[1],qi)
    def gpow(self,a,n):
        if n<0:return self.gpow(self.ginv(a),-n)
        z=self.zero
        while n:
            if n&1:z=self.gmul(z,a)
            a=self.gmul(a,a);n//=2
        return z
    def word(self,letters):
        images={1:self.xhat,2:self.yhat,-1:self.ginv(self.xhat),-2:self.ginv(self.yhat)}
        z=self.zero
        for a in letters:
            if a not in images:raise ValueError('Letters must be 1,2,-1,-2.')
            z=self.gmul(z,images[a])
        return z
    def solve_difference(self,q,d,part):
        """Solve (1-q)a=d by exact permutation-cycle elimination."""
        p=(2,3)[part];perm=self.permutation(q,part)
        a=[0]*len(d);seen=set()
        for first in range(len(d)):
            if first in seen:continue
            cycle=[];j=first
            while j not in seen:seen.add(j);cycle.append(j);j=perm[j]
            assert j==first
            if sum(d[i] for i in cycle)%p:return None
            for prev,j in zip(cycle,cycle[1:]):a[j]=(a[prev]+d[j])%p
        aq=self.act(q,tuple(a),part)
        assert all((a[i]-aq[i])%p==d[i]%p for i in range(len(d)))
        return tuple(a)
    def frame_base(self,h,target):
        bases=[]
        for b in self.pure:
            if mul(mul(b,h[2]),canon(inv(b)))!=target[2]:continue
            solutions=[]
            for part,p in enumerate((2,3)):
                bv=self.act(b,h[part],part)
                rhs=tuple((x-y)%p for x,y in zip(target[part],bv))
                a=self.solve_difference(target[2],rhs,part)
                if a is None:break
                solutions.append(a)
            if len(solutions)==2:
                candidate=(solutions[0],solutions[1],b)
                assert self.gmul(self.gmul(candidate,h),self.ginv(candidate))==target
                bases.append(b)
        if len(bases)!=1:raise ValueError(f'Expected one pure frame base, obtained {len(bases)}.')
        return bases[0]
    @staticmethod
    def signed_mod3(q):
        for a in (q,tuple(-x%12 for x in q)):
            if tuple(x%4 for x in a)==I:return tuple(x%3 for x in a)
        raise ValueError('CM coordinate has no signed lift equal to I modulo4.')
    @staticmethod
    def mm3(a,b):
        return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2))%3
                     for i in range(2) for j in range(2))
    def evaluate(self,f):
        sp=self.gmul(self.shat,f);rp=self.gmul(sp,self.tauhat)
        if self.gpow(sp,2)!=self.zero or self.gpow(rp,3)!=self.zero:
            raise ValueError('Residue fails the finite torsion relations.')
        beta=self.frame_base(self.shat,sp);A=self.frame_base(self.rhat,rp)
        possible=[]
        for t in range(12):
            V=canon((1,t,0,1))
            if (mul(mul(V,self.s),canon(inv(V)))==sp[2] and
                mul(mul(V,self.r),canon(inv(V)))==rp[2]):possible.append((t,V))
        if len(possible)!=1:raise ValueError('No unique normalized unipotent intertwiner.')
        t,V=possible[0]
        T=mul(canon(inv(A)),V);W=mul(canon(inv(beta)),V)
        T3=self.signed_mod3(T);W3=self.signed_mod3(W)
        cube=self.mm3(self.mm3(T3,T3),T3);square=self.mm3(W3,W3)
        if cube not in (I,(2,0,0,2)) or square not in (I,(2,0,0,2)):
            raise ValueError('Residue fails the CM sign conditions.')
        bit3=int(cube!=(1,0,0,1));bit4=int(square!=(1,0,0,1))
        return {'status':'FINITE_FRAME_COMPATIBLE','delta':bit3^bit4,
                'r_frame_base':A,'s_frame_base':beta,'intertwiner_t_mod12':t,
                'T_signed_mod3':T3,'W_signed_mod3':W3,
                'eisenstein_bit':bit3,'gaussian_bit':bit4,
                'scope':'This is Delta for every actual multiplier-one gentle residue. Finite compatibility alone is not a full lifting assertion.'}

    def synthetic_parity_one(self):
        """Finite frame-solver test only; no full lift is inferred."""
        part=1;n=len(self.reps[part]);p=3
        ps=self.permutation(self.s,part);pr=self.permutation(self.r,part)
        z=canon((5,0,0,5));pz=self.permutation(z,part)
        origin=self.coset_of[part][I]
        start=ps[origin];end=ps[pz[origin]]
        graph=[[] for _ in range(n)]
        for j in range(n):
            for kind,u,v in [('b',j,ps[j]),('a',ps[j],ps[pr[j]])]:
                graph[u].append((v,kind,j,1));graph[v].append((u,kind,j,-1))
        prev={start:None};todo=deque([start])
        while todo and end not in prev:
            u=todo.popleft()
            for v,kind,j,sgn in graph[u]:
                if v not in prev:
                    prev[v]=(u,kind,j,sgn);todo.append(v)
        assert end in prev
        a=[0]*n;b=[0]*n;node=end;steps=0
        while node!=start:
            old,kind,j,sgn=prev[node]
            row=a if kind=='a' else b;row[j]=(row[j]+sgn)%p
            node=old;steps+=1
        beta=(self.zero[0],tuple(b),I)
        A=(self.zero[0],tuple(a),z)
        sp=self.gmul(self.gmul(beta,self.shat),self.ginv(beta))
        rp=self.gmul(self.gmul(A,self.rhat),self.ginv(A))
        assert self.gmul(sp,rp)==self.tauhat
        f=self.gmul(self.shat,sp)
        result=self.evaluate(f)
        assert result['delta']==1 and result['r_frame_base']==z and result['s_frame_base']==I
        return {'classification':'FINITE_FRAME_TEST_ONLY_NOT_A_FULL_LIFT',
                'graph_path_length':steps,'evaluation':result}

    def verify(self):
        deriv=[set(self.pure)]
        while len(deriv[-1])>1:deriv.append(derived(deriv[-1]))
        assert list(map(len,deriv))==[96,8,2,1]
        centralizers=[]
        for part,(h,H) in enumerate(zip((self.s,self.r),self.subgroups)):
            cs=[b for b in self.Q if mul(b,h)==mul(h,b)]
            surviving=[]
            identity_coset=self.coset_of[part][I]
            for b in cs:
                # At the h-fixed identity coset, (1-h)a is always zero.
                moved=self.permutation(b,part)[identity_coset]
                if moved==identity_coset:surviving.append(b)
            assert set(surviving)==set(H)
            assert set(surviving).intersection(self.pure)=={I}
            centralizers.append({'torsion_order':len(H),'base_centralizer_order':len(cs),
                                 'surviving_projection':sorted(surviving),
                                 'pure_surviving_projection':[I]})
        identity=self.evaluate(self.zero);assert identity['delta']==0
        # An actual common inner conjugation by tau^6: the outer class is
        # identity. It is a frame/gauge test, not a normalized nontrivial pair.
        b=self.gpow(self.tauhat,6)
        sp=self.gmul(self.gmul(b,self.shat),self.ginv(b))
        f=self.gmul(self.shat,sp)
        gauge=self.evaluate(f);assert gauge['delta']==0
        return {'status':'PASS','base_group_order':len(self.Q),'pure_base_order':len(self.pure),
                'pure_derived_orders':list(map(len,deriv)),
                'coset_module_dimensions':[288,192],
                'ambient_pure_group_order':str(96*2**288*3**192),
                'ambient_pure_group_order_factorization':'2^293 * 3^193',
                'affine_torsion_relations':[2,3],'centralizer_tests':centralizers,
                'identity_test':identity,'common_pure_inner_frame_test':gauge,
                'synthetic_nonzero_frame_test':self.synthetic_parity_one(),
                'scope':'Exact finite base/coset/action/frame computation. Full-pair factorization and the fourth-derived bound require the accompanying proof. No enumeration of the entire affine group or actual gentle residue image is claimed.'}

if __name__=='__main__':
    parser=argparse.ArgumentParser();inputs=parser.add_mutually_exclusive_group()
    inputs.add_argument('--word-json',type=Path);inputs.add_argument('--residue-json',type=Path)
    args=parser.parse_args();detector=Detector()
    if args.word_json:
        result=detector.evaluate(detector.word(json.loads(args.word_json.read_text())))
    elif args.residue_json:
        data=json.loads(args.residue_json.read_text())
        v2=tuple(data['v2']);v3=tuple(data['v3']);base=canon(tuple(data['base']))
        if len(v2)!=288 or len(v3)!=192 or any(x not in (0,1) for x in v2) or any(x not in (0,1,2) for x in v3) or base not in detector.pure:
            raise ValueError('Invalid ambient pure affine residue.')
        result=detector.evaluate((v2,v3,base))
    else:
        result=detector.verify()
        result['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
        Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
