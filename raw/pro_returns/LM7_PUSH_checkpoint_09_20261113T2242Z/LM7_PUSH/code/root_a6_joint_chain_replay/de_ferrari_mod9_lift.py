#!/usr/bin/env python3
"""Complete elementary-abelian correction module for a mod-9 Ferrari test.

The six actual F2 evaluation maps are induced to B=C2*C3 through its
six cosets modulo F2.  Their joint kernel is consequently normal in B.
The kernel over G6 maps to the elementary abelian congruence kernel
of the Jacobi group modulo9.  We compute its entire F2-prime image,
retaining literal words, then impose the complete gentle norm equations
and the complete four-strand pentagon simultaneously.
"""
from contextlib import redirect_stdout
from pathlib import Path
from collections import deque
import io,json,runpy,time
import numpy as np

here=Path(__file__).resolve().parent

class Jacobi:
    def __init__(self,m):
        assert m%2 and m>=3
        self.m=m;self.half=pow(2,-1,m)
        self.one=np.array([1,0,0,1,0,0,0],dtype=np.int64)
        self.a=np.array([1,1,0,1,0,0,0],dtype=np.int64)
        self.b=np.array([1,0,-1,1,0,0,0],dtype=np.int64)%m
        self.c=np.array([1,1,0,1,1,0,self.half],dtype=np.int64)
        self.check_braids((self.a,self.b,self.c))
        sig={1:self.a,2:self.b,3:self.c}
        def pure(i,j):
            h=self.one.copy()
            for k in range(j-1,i,-1):h=self.mul(h,sig[k])
            return self.conj(h,self.power(sig[i],2))
        A12,A13,A23,A24,A34=(pure(i,j) for i,j in
                             ((1,2),(1,3),(2,3),(2,4),(3,4)))
        omega=self.power(self.mul(self.a,self.b),3)
        self.pairs=((A12,self.mul(A23,A24)),(self.mul(A13,A23),A34),
                    (A23,A34),(self.mul(A12,A13),self.mul(A24,A34)),
                    (A12,A23),(omega,A34))
        self.x=np.array([x for x,y in self.pairs]);self.y=np.array([y for x,y in self.pairs])
        xi1=self.mul(self.c,self.inv(self.a))
        xi2=self.mul(self.mul(self.mul(self.mul(self.mul(self.a,self.b),self.a),
                                              self.inv(self.c)),self.inv(self.b)),self.inv(self.a))
        assert np.array_equal(xi1,self.one+np.array([0,0,0,0,1,0,self.half]))
        expected=self.one+np.array([0,0,0,0,0,1,-self.half])
        assert np.array_equal(xi2,expected%m)
        assert np.array_equal(self.conj(self.a,xi1),xi1)
        assert np.array_equal(self.conj(self.a,xi2),self.mul(xi2,xi1))
        assert np.array_equal(self.conj(self.b,xi1),self.mul(xi1,self.inv(xi2)))
        assert np.array_equal(self.conj(self.b,xi2),xi2)

    def mul(self,x,y):
        a,b,c,d,u,v,z=np.moveaxis(x,-1,0)
        A,B,C,D,U,V,Z=np.moveaxis(y,-1,0)
        q=a*U+b*V;r=c*U+d*V
        return np.stack((a*A+b*C,a*B+b*D,c*A+d*C,c*B+d*D,
                         u+q,v+r,z+Z+self.half*(u*r-v*q)),axis=-1)%self.m

    def inv(self,x):
        a,b,c,d,u,v,z=np.moveaxis(x,-1,0)
        return np.stack((d,-b,-c,a,-d*u+b*v,c*u-a*v,-z),axis=-1)%self.m

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
        for t in w:out=self.mul(out,images[t])
        return out
    def pentagon(self,vals):
        return self.mul(self.mul(vals[0],vals[1]),self.inv(self.mul(self.mul(vals[2],vals[3]),vals[4])))
    def braid_images(self,vals):
        return self.a,self.conj(self.inv(vals[4]),self.b),self.conj(self.inv(vals[5]),self.c)
    def check_braids(self,images):
        a,b,c=images
        assert np.array_equal(self.mul(self.mul(a,b),a),self.mul(self.mul(b,a),b))
        assert np.array_equal(self.mul(self.mul(b,c),b),self.mul(self.mul(c,b),c))
        assert np.array_equal(self.mul(a,c),self.mul(c,a))

class Induced:
    def __init__(self,H,d):
        self.H=H;self.d=d
        self.Q=sorted(d['Q2']);self.ix={q:i for i,q in enumerate(self.Q)}
        self.root=self.ix[d['unit']];self.id=np.arange(6,dtype=np.int64)
        self.one=(self.id,np.broadcast_to(H.one,(6,6,7)).copy())
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
                fw=d['fword'](sect[q]+[t]+d['binv'](sect[qn]))
                values.append(H.word(fw))
            self.letters[t]=(np.array(perm,dtype=np.int64),np.array(values,dtype=np.int64))
        assert self.equal(self.power(self.letters[0],2),self.one)
        assert self.equal(self.power(self.letters[1],3),self.one)
        assert self.equal(self.inv(self.letters[1]),self.letters[-1])
        for fw,bw in (((1,),d['xword']),((2,),d['yword'])):
            el=self.word(bw)
            assert np.array_equal(el[0],self.id)
            assert np.array_equal(el[1][self.root],H.word(fw))

    def mul(self,x,y):return y[0][x[0]],self.H.mul(x[1],y[1][x[0]])
    def inv(self,x):
        q=np.argsort(x[0]);return q,self.H.inv(x[1][q])
    def conj(self,x,y):return self.mul(self.mul(x,y),self.inv(x))
    def comm(self,x,y):return self.mul(self.mul(self.mul(x,y),self.inv(x)),self.inv(y))
    def power(self,x,k):
        if k<0:return self.power(self.inv(x),-k)
        out=self.one
        while k:
            if k%2:out=self.mul(out,x)
            x=self.mul(x,x);k//=2
        return out
    def word(self,w):
        out=self.one
        for t in w:out=self.mul(out,self.letters[t])
        return out
    @staticmethod
    def equal(x,y):return np.array_equal(x[0],y[0]) and np.array_equal(x[1],y[1])
    def vector(self,x):
        assert np.array_equal(x[0],self.id)
        diff=(x[1]-self.H.one)%9;assert not np.any(diff%3)
        return (diff//3).ravel()
    def element(self,v):
        return self.id,(self.H.one+3*v.reshape(6,6,7))%9

class Span:
    def __init__(self,n):self.n=n;self.rows={};self.basis=[];self.words=[]
    def reduce(self,v):
        v=v.copy()%3;c=np.zeros(self.n,dtype=np.int64)
        for p,(r,b) in sorted(self.rows.items()):
            if v[p]:a=int(v[p]);v=(v-a*r)%3;c=(c+a*b)%3
        return v,c
    def add(self,v,w):
        r,c=self.reduce(v);nz=np.flatnonzero(r)
        if not len(nz):return False
        p=int(nz[0]);s=int(r[p]);k=len(self.basis)
        b=-s*c%3;b[k]=(b[k]+s)%3
        self.rows[p]=(s*r%3,b);self.basis.append(v.copy()%3);self.words.append(w)
        return True
    def coordinates(self,v):
        r,c=self.reduce(v);assert not np.any(r)
        return c[:len(self.basis)]
    def matrix(self):return np.array(self.basis,dtype=np.int64).T

def free_abelianization(w):
    return np.array([sum(1 if t==i else -1 if t==-i else 0 for t in w) for i in (1,2)],dtype=np.int64)

def build_module(H,W,d):
    start=time.time();N=[W.word(w) for w in d['Nwords']];dimension=6*6*7
    assert all(W.equal(W.power(n,9),W.one) for n in N)
    # Every image has elementary abelian reduction, so all generators
    # of ker(N -> N_ab/6) lie in this additive congruence kernel.
    C=Span(dimension)
    def bwinv(w):return d['binv'](w)
    for i in range(97):
        for j in range(i+1,97):
            v=W.vector(W.comm(N[i],N[j]))
            if np.any(C.reduce(v)[0]):
                wi,wj=d['Nwords'][i],d['Nwords'][j]
                C.add(v,wi+wj+bwinv(wi)+bwinv(wj))
    at=0
    while at<len(C.basis):
        e=W.element(C.basis[at]);w=C.words[at]
        for i in range(97):
            v=W.vector(W.conj(N[i],e))
            C.add(v,d['Nwords'][i]+w+bwinv(d['Nwords'][i]))
        at+=1
    comm_rank=len(C.basis)
    powers=[W.power(n,6) for n in N]
    power_vectors=np.array([W.vector(n) for n in powers],dtype=np.int64).T
    fab=np.column_stack([free_abelianization(w) for w in d['Nfwords']])
    assert not np.any(fab[1]%2) and not np.any((fab[0]-2*fab[1])%6)
    Hfab=np.vstack(((fab[0]-2*fab[1])//6,fab[1]//2))
    pivot=None
    for i in range(97):
        for j in range(i+1,97):
            det=int(Hfab[0,i]*Hfab[1,j]-Hfab[0,j]*Hfab[1,i])
            if abs(det)==1:pivot=(i,j,det);break
        if pivot is not None:break
    assert pivot is not None
    i,j,det=pivot
    Hinverse=det*np.array([[Hfab[1,j],-Hfab[0,j]],[-Hfab[1,i],Hfab[0,i]]])
    assert np.array_equal(Hinverse@Hfab[:,[i,j]],np.eye(2,dtype=np.int64))
    kernel=[]
    for k in range(97):
        if k in (i,j):continue
        vec=np.zeros(97,dtype=np.int64);vec[k]=1;vec[[i,j]]-=Hinverse@Hfab[:,k]
        assert not np.any(fab@vec);kernel.append(vec)
        v=power_vectors@vec%3
        if np.any(C.reduce(v)[0]):
            word=[]
            for ni,coef in enumerate(vec):
                if coef:word+=d['bpower'](d['Nwords'][ni],6*int(coef))
            assert not np.any(free_abelianization(d['fword'](word)))
            C.add(v,word)
    prime_rank=len(C.basis)
    for v,w in zip(C.basis,C.words):
        assert np.array_equal(W.vector(W.word(w)),v)
        assert not np.any(free_abelianization(d['fword'](w)))
        for t in (0,1):C.coordinates(W.vector(W.conj(W.letters[t],W.element(v))))
    Full=Span(dimension)
    for v,w in zip(C.basis,C.words):Full.add(v,w)
    for k in range(97):Full.add(power_vectors[:,k],d['bpower'](d['Nwords'][k],6))
    for v in Full.basis:
        for n in N:Full.coordinates(W.vector(W.conj(n,W.element(v))))
    metadata={'commutator_normal_image_dimension':comm_rank,
              'F_prime_kernel_image_dimension':prime_rank,
              'full_G6_kernel_image_dimension':len(Full.basis),
              'integral_F_abelianization_kernel_basis_rank':len(kernel),
              'primitive_F_abelianization_pivot':list(pivot),
              'all_N_ninth_powers_trivial':True,
              'module_build_seconds':round(time.time()-start,3)}
    print(json.dumps(metadata),flush=True)
    return C,metadata,{'N_congruence_power_images':power_vectors,
                       'N_F_abelianization':fab,
                       'N_primitive_F_abelianization':Hfab,
                       'integral_abelianization_kernel':np.array(kernel,dtype=np.int64).T,
                       'full_G6_kernel_image_basis':Full.matrix()}

def rref(A):
    A=np.array(A,dtype=np.int64)%3;rank=0;piv=[]
    for col in range(A.shape[1]):
        ix=np.flatnonzero(A[rank:,col])
        if not len(ix):continue
        k=rank+int(ix[0]);A[[rank,k]]=A[[k,rank]]
        A[rank]=A[rank]*int(A[rank,col])%3
        for j in range(A.shape[0]):
            if j!=rank and A[j,col]:A[j]=(A[j]-A[j,col]*A[rank])%3
        piv.append(col);rank+=1
        if rank==A.shape[0]:break
    return A,piv

def solve(A,b):
    n=A.shape[1];R,p=rref(np.column_stack((A,b)))
    if n in p:return None
    x=np.zeros(n,dtype=np.int64);x[p]=R[:len(p),n]
    free=[j for j in range(n) if j not in p];K=np.zeros((n,len(free)),dtype=np.int64)
    for k,j in enumerate(free):K[j,k]=1;K[p,k]=-R[:len(p),j]%3
    assert not np.any((A@x-b)%3) and not np.any(A@K%3)
    return x,K

def congruence_vector(H,x):
    d=(x-H.one)%9;assert not np.any(d%3)
    return d//3

def pentagon_braid_errors(H,values):
    aa,bb,cc=H.braid_images(values)
    residuals=[H.pentagon(values),
        H.mul(H.mul(H.mul(aa,bb),aa),H.inv(H.mul(H.mul(bb,aa),bb))),
        H.mul(H.mul(H.mul(bb,cc),bb),H.inv(H.mul(H.mul(cc,bb),cc))),
        H.comm(aa,cc)]
    return np.concatenate([congruence_vector(H,x) for x in residuals])

def lift_records(H,W,d,C,certificate):
    records=json.loads((here/'de_ferrari_fibres.json').read_text())['records']
    rows=[];rank=len(C.basis);I=np.eye(rank,dtype=np.int64)
    s,r=W.letters[0],W.letters[1];t=W.mul(s,r)
    x=W.word(d['xword']);u=W.word([-1,0]);vv=W.word([0,-1])
    fullbasis=certificate['full_G6_kernel_image_basis'];fullrank=fullbasis.shape[1]
    rng=np.random.default_rng(192026)
    start=time.time()
    for ix,rec in enumerate(records):
        beta=W.word(rec['base_beta_word_B']);S=W.conj(beta,s);R=W.mul(S,t)
        assert W.equal(W.power(S,2),W.one)
        E=C.coordinates(W.vector(W.power(R,3)))
        SM=np.column_stack([C.coordinates(W.vector(W.conj(S,W.element(v)))) for v in C.basis])
        RM=np.column_stack([C.coordinates(W.vector(W.conj(R,W.element(v)))) for v in C.basis])
        assert np.array_equal(SM@SM%3,I) and np.array_equal(RM@RM@RM%3,I)
        gentleA=np.vstack(((I+SM)%3,(I+RM+RM@RM)%3))
        gentleb=np.r_[np.zeros(rank,dtype=np.int64),E]
        g=rec['integral_cusp_gauge'];xg=W.power(x,g)
        fbase=W.mul(s,W.conj(xg,S));basevals=fbase[1][W.root]
        assert np.array_equal(basevals,H.word(rec['actual_commutator_word_f']))
        def corrected_values(z):
            correction=W.conj(xg,W.element(C.matrix()@z%3))
            return H.mul(basevals,correction[1][W.root])
        base_error=pentagon_braid_errors(H,basevals)
        J=np.column_stack([(pentagon_braid_errors(H,corrected_values(I[:,j]))-base_error)%3
                           for j in range(rank)])
        # There are only 27 possible F-prime correction values.  Evaluate
        # every one independently to certify the entire affine system.
        from itertools import product
        for bits in product(range(3),repeat=rank):
            z=np.array(bits,dtype=np.int64)
            assert np.array_equal(pentagon_braid_errors(H,corrected_values(z)),(base_error+J@z)%3)
        A=np.vstack((gentleA,J));b=np.r_[gentleb,-base_error%3]
        sol=solve(A,b);gentlesol=solve(gentleA,gentleb)
        row={'certificate_index':ix,'missing_coset':rec['missing_coset'],
             'F_prime_correction_dimension':rank,
             'gentle_norm_rank':len(rref(gentleA)[1]),
             'pentagon_and_braid_equation_rank':len(rref(J)[1]),
             'pentagon_equation_rank':len(rref(J[:7])[1]),
             'braid_equation_rank':len(rref(J[7:])[1]),
             'combined_equation_rank':len(rref(A)[1]),
             'gentle_lift_exists':gentlesol is not None,
             'simultaneous_lift_exists':sol is not None,
             'all_27_correction_values_exhaustively_checked':True}
        certificate[f'norm_matrix_{ix}']=gentleA;certificate[f'norm_rhs_{ix}']=gentleb
        certificate[f'pentagon_braid_matrix_{ix}']=J;certificate[f'pentagon_braid_constant_{ix}']=base_error
        if sol is not None:
            z,K=sol;kelem=W.element(C.matrix()@z%3)
            newS=W.mul(S,kelem);newR=W.mul(W.inv(kelem),R)
            assert W.equal(W.power(newS,2),W.one)
            assert W.equal(W.power(newR,3),W.one)
            assert W.equal(W.mul(newS,newR),t)
            kw=[]
            for coefficient,w in zip(z,C.words):kw+=w*int(coefficient)
            assert W.equal(W.word(kw),kelem)
            assert not np.any(free_abelianization(d['fword'](kw)))
            cg=d['bpower'](d['xword'],g)
            fword=d['fword']([0]+cg+rec['base_beta_word_B']+[0]+
                            d['binv'](rec['base_beta_word_B'])+kw+d['binv'](cg))
            assert not np.any(free_abelianization(fword))
            values=H.word(fword)
            assert np.array_equal(values,corrected_values(z))
            assert np.array_equal(H.pentagon(values),H.one)
            H.check_braids(H.braid_images(values))
            aa,bb,cc=H.braid_images(values)
            xi1=H.mul(cc,H.inv(aa))
            xi2=H.mul(H.mul(H.mul(H.mul(H.mul(aa,bb),aa),H.inv(cc)),H.inv(bb)),H.inv(aa))
            assert np.array_equal(xi1[:4],H.one[:4]) and np.array_equal(xi2[:4],H.one[:4])
            determinant=int((xi1[4]*xi2[5]-xi1[5]*xi2[4])%3)
            assert determinant
            def matrix_mul(x,y):
                a,b,c,d=x;A,B,C,D=y
                return ((a*A+b*C)%9,(a*B+b*D)%9,(c*A+d*C)%9,(c*B+d*D)%9)
            matrix_generators=[tuple(int(t) for t in aa[:4]),tuple(int(t) for t in bb[:4])]
            matrix_image={(1,0,0,1)};matrix_queue=[(1,0,0,1)]
            for xmatrix in matrix_queue:
                for ymatrix in matrix_generators:
                    product_matrix=matrix_mul(xmatrix,ymatrix)
                    if product_matrix not in matrix_image:matrix_image.add(product_matrix);matrix_queue.append(product_matrix)
            assert len(matrix_image)==648
            ff=W.mul(s,W.conj(xg,newS));fi=W.inv(ff)
            # These are the two complete multiplier-one braid hexagons.
            hex1=W.mul(W.mul(W.mul(W.mul(u,fi),vv),ff),W.inv(W.mul(fi,r)))
            hex2=W.mul(W.mul(W.mul(W.mul(fi,vv),ff),u),W.inv(W.mul(W.mul(vv,u),ff)))
            assert W.equal(hex1,W.one) and W.equal(hex2,W.one)
            # Directly compute the image of the entire kernel K6 from
            # all N commutators and sixth powers under the new generators.
            images={0:newS,1:newR,-1:W.inv(newR)}
            def image_word(word):
                out=W.one
                for letter in word:out=W.mul(out,images[letter])
                return out
            newN=[image_word(w) for w in d['Nwords']]
            image=Span(252)
            for n in newN:image.add(W.vector(W.power(n,6)),[])
            for i in range(97):
                for j in range(i+1,97):image.add(W.vector(W.comm(newN[i],newN[j])),[])
            at=0
            while at<len(image.basis):
                element=W.element(image.basis[at])
                for n in newN:image.add(W.vector(W.conj(n,element)),[])
                at+=1
            assert len(image.basis)==fullrank
            for v in fullbasis.T:image.coordinates(v)
            row.update({'correction_coefficients':z.tolist(),
                        'homogeneous_correction_basis':K.tolist(),
                        'literal_B_correction_word':kw,
                        'actual_F_commutator_word':list(fword),
                        'both_complete_hexagons_verified_in_full_core':True,
                        'complete_pentagon_directly_verified':True,
                        'all_three_braid_relations_directly_verified':True,
                        'Ferrari_homology_determinant_mod3':determinant,
                        'SL2_mod9_braid_image_order':len(matrix_image),
                        'four_strand_map_surjective_on_Jacobi_target':True,
                        'kernel_generation_rank':len(image.basis),
                        'source_map_surjective_on_combined_G6_core_quotient':True})
        rows.append(row)
        print(json.dumps({k:v for k,v in row.items() if k not in
                         ('literal_B_correction_word','actual_F_commutator_word','homogeneous_correction_basis')}),flush=True)
    return rows,round(time.time()-start,3)

def main():
    with redirect_stdout(io.StringIO()):d=runpy.run_path(str(here/'de_distribution_test.py'))
    H=Jacobi(9);W=Induced(H,d)
    C,meta,certificate=build_module(H,W,d)
    certificate['F_prime_kernel_image_basis']=C.matrix()
    np.savez_compressed(here/'de_ferrari_mod9_module.npz',**certificate)
    here.joinpath('de_ferrari_mod9_module.json').write_text(json.dumps({**meta,
        'literal_B_words_for_F_prime_basis':C.words,
        'coset_section':{str(k):w for k,w in W.section.items()},
        'core_definition':'intersection of all six B/F2 conjugates of each of the six Ferrari evaluation kernels, intersected with ker(B -> G6)',
        'kernel_image_complete':True},indent=2)+'\n')
    rows,seconds=lift_records(H,W,d,C,certificate)
    np.savez_compressed(here/'de_ferrari_mod9_lift_certificate.npz',**certificate)
    out={**meta,'coefficient_modulus':9,'six_F2_evaluations_induced_through_all_six_cosets':True,
         'records':rows,'pass_counts':[sum(r['simultaneous_lift_exists'] and r['missing_coset']==b for r in rows)
                                     for b in (False,True)],'lift_calculation_seconds':seconds,
         'scope':'Complete F-prime kernel correction image over each of the 24 retained E17 G6 points, with simultaneous full three-strand gentle hexagons, generation, and the actual finite four-strand pentagon and braid relations. This does not assert full profinite pentagon lifts.'}
    here.joinpath('de_ferrari_mod9_lift.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2),flush=True)

if __name__=='__main__':main()
