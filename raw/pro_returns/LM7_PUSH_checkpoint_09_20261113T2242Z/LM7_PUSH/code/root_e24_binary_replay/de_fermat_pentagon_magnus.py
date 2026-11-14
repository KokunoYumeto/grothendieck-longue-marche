#!/usr/bin/env python3
"""Exact group pentagon through a prescribed Magnus degree, modulo any m.

There are no logarithms or denominators in this evaluator.  The source
is a literal word in x,y (letters +/-1,+/-2), or its Magnus expansion in
x-1,y-1.  Pure braids act by the actual Artin automorphisms of F3.
To detect the group pentagon through degree d, their action is computed
on the three free generators through degree d+1.

Public interface:
    E = PentagonMagnus(modulus=3, weight=7)
    answer = E.from_word(word)
    answer = E.from_series({tuple_of_0_1: coefficient, ...})
The answer is three sparse tensor polynomials giving the automorphism
residual on X,Y,Z.  The constant source coefficient must be one.
JSON output spells each tensor word using 'X','Y','Z'.
"""
from functools import cache
from pathlib import Path
import argparse,json,time

def reduce_word(w):
    out=[]
    for a in w:
        if out and out[-1]==-a:out.pop()
        else:out.append(a)
    return tuple(out)
def inverse_word(w):return tuple(-a for a in w[::-1])
def substitute_word(w,images):
    out=[]
    for a in w:
        z=images[abs(a)-1]
        for b in (z if a>0 else inverse_word(z)):
            if out and out[-1]==-b:out.pop()
            else:out.append(b)
    return tuple(out)
def compose_words(a,b):return tuple(substitute_word(w,a) for w in b)

class FreeAuto:
    """An exact free-group automorphism with its explicit inverse."""
    def __init__(self,images,inverse):
        self.images=tuple(map(tuple,images));self.inverse=tuple(map(tuple,inverse))
    def __mul__(self,other):
        return FreeAuto(compose_words(self.images,other.images),
                        compose_words(other.inverse,self.inverse))
    def inv(self):return FreeAuto(self.inverse,self.images)
    def power(self,n):
        if n<0:return self.inv().power(-n)
        ans=IDENTITY
        for _ in range(n):ans=ans*self
        return ans

IDENTITY=FreeAuto(((1,),(2,),(3,)),((1,),(2,),(3,)))
R1=FreeAuto(((2,),(-2,1,2),(3,)),((1,2,-1),(1,),(3,)))
R2=FreeAuto(((1,),(3,),(-3,2,3)),((1,),(2,3,-2),(2,)))
def inner(w):
    wi=inverse_word(w)
    return FreeAuto(tuple(reduce_word(w+(i,)+wi) for i in (1,2,3)),
                    tuple(reduce_word(wi+(i,)+w) for i in (1,2,3)))

def artin_model():
    a12=R1.power(2);a23=R2.power(2);a13=R2*a12*R2.inv()
    a14,a24,a34=(inner((i,)) for i in (1,2,3))
    A={(1,2):a12,(1,3):a13,(2,3):a23,(1,4):a14,(2,4):a24,(3,4):a34}
    pairs=((a12,a23*a24),(a13*a23,a34),(a23,a34),
           (a12*a13,a24*a34),(a12,a23))
    return A,pairs

def free_word_audit():
    A,pairs=artin_model()
    for r in (R1,R2,*A.values()):
        assert (r*r.inv()).images==IDENTITY.images
        assert (r.inv()*r).images==IDENTITY.images
    assert (R1*R2*R1).images==(R2*R1*R2).images
    assert A[(1,2)].inverse==((1,2,1,-2,-1),(1,2,-1),(3,))
    assert A[(2,3)].inverse==((1,),(2,3,2,-3,-2),(2,3,-2))
    checked=[]
    for i,j,k in ((1,2,3),(1,2,4),(1,3,4),(2,3,4)):
        a,b,c=A[i,j],A[i,k],A[j,k]
        assert (a*b*c).images==(b*c*a).images==(c*a*b).images
        checked.append([i,j,k])
    assert (A[1,2]*A[3,4]).images==(A[3,4]*A[1,2]).images
    assert (A[1,4]*A[2,3]).images==(A[2,3]*A[1,4]).images
    c3=A[1,2]*A[1,3]*A[2,3]
    assert c3.images==inner((-3,-2,-1)).images
    c4=c3*A[1,4]*A[2,4]*A[3,4]
    assert c4.images==IDENTITY.images
    return {'Artin_braid_relation':True,'all_inverse_maps_verified':True,
            'pure_triple_relations_checked':checked,
            'noncrossing_disjoint_relations_checked':2,
            'PB3_center_is_inner_XYZ_inverse':True,'PB4_center_is_identity':True,
            'A12_inverse_words':[list(w) for w in A[1,2].inverse],
            'A23_inverse_words':[list(w) for w in A[2,3].inverse],
            'pentagon_pairs_free_images':[[[list(w) for w in u.images],
                                           [list(w) for w in v.images]] for u,v in pairs]}

class Tensor:
    def __init__(self,prime,degree):self.p=prime;self.degree=degree
    def clean(self,a):return {w:c%self.p for w,c in a.items() if c%self.p and len(w)<=self.degree}
    def add(self,a,b,scale=1):
        out=dict(a)
        for w,c in b.items():
            value=(out.get(w,0)+scale*c)%self.p
            if value:out[w]=value
            elif w in out:del out[w]
        return out
    def mul(self,a,b):
        out={};p=self.p;degree=self.degree
        if not a or not b:return out
        amin=min(map(len,a));bmin=min(map(len,b))
        if amin+bmin>degree:return out
        bydegree=[[] for _ in range(degree+1)]
        for v,d in b.items():
            if len(v)<=degree-amin:bydegree[len(v)].append((v,d))
        for w,c in a.items():
            if len(w)+bmin>degree:continue
            for k in range(bmin,degree-len(w)+1):
                for v,d in bydegree[k]:
                    z=w+v;out[z]=(out.get(z,0)+c*d)%p
        return {w:c for w,c in out.items() if c}
    def word(self,w):
        out={():1}
        for a in w:
            i=abs(a)-1
            if a>0:g={():1,(i,):1}
            else:g={(i,)*k:(-1)**k%self.p for k in range(self.degree+1)}
            out=self.mul(out,g)
        return out
    def inverse(self,a):
        assert a.get((),0)%self.p==1
        h=self.add(a,{():1},-1);term={():1};out={():1}
        for _ in range(1,self.degree+1):
            term=self.mul(term,h)
            if not term:break
            out=self.add(out,term,-1 if _%2 else 1)
        assert self.mul(a,out)=={():1} and self.mul(out,a)=={():1}
        return out

class IAOperator:
    """The linear operator phi-Id, with exact cached monomial values."""
    def __init__(self,tensor,images):
        self.T=tensor;self.images=tuple(images)
        self.difference=tuple(tensor.add(q,{(i,):1},-1) for i,q in enumerate(images))
        assert all(all(len(w)>=2 for w in q) for q in self.difference)
        self.raising=min((len(w)-1 for q in self.difference for w in q),default=tensor.degree)
        self.bounded_difference=[tuple({w:c for w,c in q.items() if len(w)<=bound}
                                      for bound in range(tensor.degree+1)) for q in self.difference]
        self._monomial=cache(self._monomial_uncached)
    def _monomial_uncached(self,w):
        T=self.T
        if not w or len(w)+self.raising>T.degree:return {}
        prefix=w[:-1];last=w[-1];old=self._monomial(prefix)
        ans={a+(last,):c for a,c in old.items() if len(a)<T.degree}
        tail={prefix+a:c for a,c in self.bounded_difference[last][T.degree-len(prefix)].items()}
        return T.add(T.add(ans,tail),T.mul(old,self.difference[last]))
    def delta(self,q):
        out={};p=self.T.p
        for w,c in q.items():
            for v,d in self._monomial(w).items():out[v]=(out.get(v,0)+c*d)%p
        return {w:c for w,c in out.items() if c}
    def apply(self,q):return self.T.add(q,self.delta(q))

class PentagonMagnus:
    def __init__(self,prime=3,weight=7,modulus=None):
        # ``prime`` is retained for callers of the original interface.
        # No field operation is used: any coefficient modulus >=2 is valid.
        if modulus is not None:prime=modulus
        assert prime>=2
        self.p=prime;self.weight=weight;self.source=Tensor(prime,weight)
        self.target=Tensor(prime,weight+1);self.audit=free_word_audit()
        self.A,self.pairs=artin_model();self.variables=tuple({(i,):1} for i in range(3))
        self.operators=[]
        for pair in self.pairs:
            ops=[]
            for a in pair:
                images=tuple(self.target.add(self.target.word(w),{():1},-1) for w in a.images)
                ops.append(IAOperator(self.target,images))
            self.operators.append(tuple(ops))
        self.term_functions=[]
        for ops in self.operators:
            def make_term(ops):
                @cache
                def term(w,i):
                    if not w:return self.variables[i]
                    return ops[w[0]].delta(term(w[1:],i))
                return term
            self.term_functions.append(make_term(ops))
    def evaluate_series(self,f,index):
        assert f.get((),0)%self.p==1
        T=self.target;term=self.term_functions[index]
        result=[]
        for i in range(3):
            q=dict(self.variables[i])
            for w,c in f.items():
                if w:q=T.add(q,term(w,i),c)
            result.append(q)
        return tuple(result)
    def from_series(self,f):
        f=self.source.clean(f);assert f.get((),0)==1
        fi=self.source.inverse(f)
        factors=[self.evaluate_series(f,0),self.evaluate_series(f,1),
                 self.evaluate_series(fi,4),self.evaluate_series(fi,3),self.evaluate_series(fi,2)]
        ops=[IAOperator(self.target,images) for images in factors]
        result=[]
        for i in range(3):
            q=self.variables[i]
            for op in reversed(ops):q=op.apply(q)
            result.append(self.target.add(q,self.variables[i],-1))
        self.last_source_series=f;self.last_factors=factors
        return tuple(result)
    def from_word(self,w):return self.from_series(self.source.word(w))
    def variation_from_degree_five(self,new_series,base_series,base_factors):
        """Exact affine pentagon difference through group degree seven.

        All changes start in source degree5; products of two changes lie
        beyond degree7.  Base factors are IA of degree2, so only their
        degree3 generator images can transport the degree6 changes.
        """
        assert self.weight==7
        S,T=self.source,self.target
        change=S.add(new_series,base_series,-1)
        assert all(len(w)>=5 for w in change)
        inverse=S.inverse(new_series)
        new_factors=[self.evaluate_series(new_series,0),self.evaluate_series(new_series,1),
                     self.evaluate_series(inverse,4),self.evaluate_series(inverse,3),self.evaluate_series(inverse,2)]
        changes=[tuple(T.add(a,b,-1) for a,b in zip(new,old))
                 for new,old in zip(new_factors,base_factors)]
        assert all(all(len(w)>=6 for w in q) for D in changes for q in D)
        leading=[tuple({w:c for w,c in q.items() if len(w)==3} for q in old)
                 for old in base_factors]
        def deriv(q,D):
            out={}
            for w,c in q.items():
                for k,a in enumerate(w):
                    for v,b in D[a].items():
                        z=w[:k]+v+w[k+1:]
                        if len(z)<=T.degree:out[z]=(out.get(z,0)+c*b)%self.p
            return {w:c for w,c in out.items() if c}
        result=[{} for _ in range(3)]
        for j,D in enumerate(changes):
            D6=tuple({w:c for w,c in q.items() if len(w)==6} for q in D)
            pre=[{} for _ in range(3)];post=[{} for _ in range(3)]
            for k in range(j):
                for i in range(3):pre[i]=T.add(pre[i],leading[k][i])
            for k in range(j+1,5):
                for i in range(3):post[i]=T.add(post[i],leading[k][i])
            for i in range(3):
                value=T.add(T.add(D[i],deriv(post[i],D6)),deriv(D6[i],pre))
                result[i]=T.add(result[i],value)
        return tuple(result)
    def literal_factor(self,w,index):
        """Independent direct composition of the literal f-word."""
        T=self.target;pair=self.pairs[index]
        choices={}
        for letter,a in ((1,pair[0]),(2,pair[1])):
            for sign,images in ((1,a.images),(-1,a.inverse)):
                q=tuple(T.add(T.word(x),{():1},-1) for x in images)
                choices[sign*letter]=IAOperator(T,q)
        out=[]
        for i in range(3):
            q=self.variables[i]
            for letter in reversed(w):q=choices[letter].apply(q)
            out.append(q)
        return tuple(out)

def encode(residual):
    return [{''.join('XYZ'[a] for a in w):int(c) for w,c in sorted(q.items(),key=lambda z:(len(z[0]),z[0]))}
            for q in residual]
def summary(residual):
    degrees=sorted({len(w) for q in residual for w in q})
    return {'zero':not degrees,'first_automorphism_degree':degrees[0] if degrees else None,
            'coefficient_counts_by_degree':{str(d):sum(sum(len(w)==d for w in q) for q in residual) for d in degrees}}

def self_test():
    E=PentagonMagnus(prime=3,weight=4)
    assert all(not q for q in E.from_word(()))
    words=((1,2,-1,-2),(1,1,2,-1,-1,-2),(1,2,1,-2,-1,-1))
    checks=0
    for w in words:
        f=E.source.word(w)
        for i in range(5):
            assert E.evaluate_series(f,i)==E.literal_factor(w,i)
            checks+=1
    # The IA operator is independently checked against full tensor substitution.
    T=E.target;op=E.operators[0][0]
    for w in ((0,1),(1,0,2),(0,0,1),(2,1,0,2)):
        q={():1}
        for a in w:q=T.mul(q,op.images[a])
        assert op.apply({w:1})==q
    return {'literal_word_factor_checks':checks,'direct_tensor_substitution_checks':4,
            'identity_pentagon_verified':True,'free_word_model':E.audit}

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--input',help='JSON list of signed letters or object with word key')
    parser.add_argument('--output',default='code/de_fermat_pentagon_magnus.json')
    parser.add_argument('--prime',type=int,default=3)
    parser.add_argument('--modulus',type=int,help='coefficient modulus; overrides --prime')
    parser.add_argument('--weight',type=int,default=7)
    args=parser.parse_args();start=time.time();checks=self_test()
    w=(1,2,-1,-2)
    if args.input:
        value=json.loads(Path(args.input).read_text());w=value['word'] if isinstance(value,dict) else value
    coefficient_modulus=args.prime if args.modulus is None else args.modulus
    E=PentagonMagnus(modulus=coefficient_modulus,weight=args.weight);res=E.from_word(w)
    out={'coefficient_modulus':coefficient_modulus,'group_Magnus_degree':args.weight,
         'automorphism_Magnus_degree':args.weight+1,'source_word':list(w),
         'pentagon_residual_on_generators':encode(res),**summary(res),
         'verification':checks,'elapsed_seconds':round(time.time()-start,3),
         'scope':'Exact denominator-free truncated group pentagon for the supplied literal word. The pure-F3 pentagon remainder is tested through group degree d by its automorphism through degree d+1. Arithmetic constraints and the full kernel of any separate finite quotient are not imposed here.'}
    Path(args.output).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('pentagon_residual_on_generators','verification')},indent=2),flush=True)
    print(json.dumps({'literal_factor_checks':checks['literal_word_factor_checks'],
                      'Artin_model_all_checks_pass':True},indent=2),flush=True)

if __name__=='__main__':main()
