#!/usr/bin/env python3
"""Complete Ferrari-homology pentagon test above the retained G6 points.

The actual B4 representation sends sigma1=(0,A), sigma2=(0,B),
sigma3=(e1,A) in F3^2 semidirect SL2(F3).  Its normal translation
subgroup is the homology of the Ferrari kernel.  We evaluate all five
pentagon factors and the sigma3 Drinfeld conjugator simultaneously.
The complete image of ker(B->G6)=N' N^6 in these auxiliary targets is
computed from the actual 97 Schreier generators, and all corrections
in that image are allowed.  A pass certifies these finite necessary
pentagon and homology-automorphism conditions only.
"""
from contextlib import redirect_stdout
from itertools import product
from pathlib import Path
import io,json,runpy,time
import numpy as np

here=Path(__file__).resolve().parent
with redirect_stdout(io.StringIO()):
    d=runpy.run_path(str(here/'de_distribution_test.py'))
records=json.loads((here/'de_fibre_sixteen_crt_verify.json').read_text())['records']
p=3;one=(1,0,0,1,0,0)

def mul(a,b):
    return ((a[0]*b[0]+a[1]*b[2])%p,(a[0]*b[1]+a[1]*b[3])%p,
            (a[2]*b[0]+a[3]*b[2])%p,(a[2]*b[1]+a[3]*b[3])%p,
            (a[4]+a[0]*b[4]+a[1]*b[5])%p,
            (a[5]+a[2]*b[4]+a[3]*b[5])%p)
def inv(a):
    b=(a[3],-a[1]%p,-a[2]%p,a[0],0,0)
    return b[:4]+(( -b[0]*a[4]-b[1]*a[5])%p,
                   (-b[2]*a[4]-b[3]*a[5])%p)
def power(a,k):
    if k<0:return power(inv(a),-k)
    out=one
    while k:
        if k%2:out=mul(out,a)
        a=mul(a,a);k//=2
    return out
def comm(a,b):return mul(mul(mul(a,b),inv(a)),inv(b))
def conj(a,b):return mul(mul(a,b),inv(a))
def word(w,gens):
    choices={1:gens[0],-1:inv(gens[0]),2:gens[1],-2:inv(gens[1])}
    out=one
    for a in w:out=mul(out,choices[a])
    return out
def manyword(w):return tuple(word(w,xy) for xy in pairs)
def mcomm(a,b):return tuple(comm(x,y) for x,y in zip(a,b))
def vector(a):
    assert all(x[:4]==one[:4] for x in a)
    return np.array([c for x in a for c in x[4:]],dtype=np.int64)
def corrected(a,v):
    return tuple(mul(x,one[:4]+tuple(int(c) for c in v[2*j:2*j+2]))
                 for j,x in enumerate(a))
def matrix(a):return np.array(a[:4],dtype=np.int64).reshape(2,2)
def rref(a):
    a=np.array(a,dtype=np.int64)%p;row=0;piv=[]
    for col in range(a.shape[1]):
        choices=np.flatnonzero(a[row:,col])
        if not len(choices):continue
        j=row+int(choices[0]);a[[row,j]]=a[[j,row]]
        a[row]=a[row]*pow(int(a[row,col]),-1,p)%p
        for k in range(a.shape[0]):
            if k!=row and a[k,col]:a[k]=(a[k]-a[k,col]*a[row])%p
        piv.append(col);row+=1
        if row==a.shape[0]:break
    return a,piv
def solve(a,b):
    a=np.array(a,dtype=np.int64)%p;b=np.array(b,dtype=np.int64)%p
    q=a.shape[1];rr,piv=rref(np.column_stack((a,b)))
    if q in piv:return None
    point=np.zeros(q,dtype=np.int64);point[piv]=rr[:len(piv),q]
    free=[j for j in range(q) if j not in piv]
    ker=np.zeros((q,len(free)),dtype=np.int64)
    for j,k in enumerate(free):ker[k,j]=1;ker[piv,j]=-rr[:len(piv),k]%p
    assert not np.any((a@point-b)%p) and not np.any(a@ker%p)
    return point,ker

a=(1,1,0,1,0,0);b=(1,0,2,1,0,0);c=(1,1,0,1,1,0)
sig={1:a,2:b,3:c}
assert mul(mul(a,b),a)==mul(mul(b,a),b)
assert mul(mul(b,c),b)==mul(mul(c,b),c)
assert mul(a,c)==mul(c,a)
def pure(i,j):
    h=one
    for k in range(j-1,i,-1):h=mul(h,sig[k])
    return conj(h,power(sig[i],2))
A12,A13,A23,A24,A34=(pure(i,j) for i,j in ((1,2),(1,3),(2,3),(2,4),(3,4)))
omega=power(mul(a,b),3)
pairs=((A12,mul(A23,A24)),(mul(A13,A23),A34),
       (A23,A34),(mul(A12,A13),mul(A24,A34)),
       (A12,A23),(omega,A34))
xi1=mul(c,inv(a));xi2=mul(mul(mul(mul(mul(a,b),a),inv(c)),inv(b)),inv(a))
assert xi1==one[:4]+(1,0) and xi2==one[:4]+(0,1)
# Literal Ferrari actions, including their signs, match NTY(4.15).
assert conj(a,xi1)==xi1 and conj(a,xi2)==mul(xi2,xi1)
assert conj(b,xi1)==mul(xi1,inv(xi2)) and conj(b,xi2)==xi2

# The actual pure finite quotient is obtained by adjoining the S4 map.
idperm=(0,1,2,3)
def pmul(a,b):return tuple(a[b[i]] for i in range(4))
adjacent=[]
for i in range(3):
    t=list(idperm);t[i],t[i+1]=t[i+1],t[i];adjacent.append(tuple(t))
gens4=list(zip((a,b,c),adjacent));joint={(one,idperm)};todo=[(one,idperm)]
for xh,xs in todo:
    for yh,ys in gens4:
        z=(mul(xh,yh),pmul(xs,ys))
        if z not in joint:joint.add(z);todo.append(z)
assert len(joint)==5184

N=[manyword(w) for w in d['Nfwords']]
assert all(power(x,3)==one for n in N for x in n)
comm_images=[];comm_words=[]
for i in range(97):
    for j in range(i+1,97):
        value=mcomm(N[i],N[j]);comm_images.append(vector(value));comm_words.append((i,j))
allcols=np.array(comm_images,dtype=np.int64).T
_,piv=rref(allcols);W=allcols[:,piv];basis_pairs=[comm_words[j] for j in piv]
for col in range(W.shape[1]):
    z=corrected((one,)*len(pairs),W[:,col])
    assert all(comm(u,v)==one for ng in N for u,v in zip(ng,z))
print(json.dumps({'auxiliary_pairs':len(pairs),'correction_image_dimension':W.shape[1],
                  'basis_commutator_pairs':basis_pairs}),flush=True)

def system(vals):
    lhs=mul(vals[0],vals[1]);rhs=mul(mul(vals[2],vals[3]),vals[4])
    residual=mul(lhs,inv(rhs));assert residual[:4]==one[:4]
    aa=a;bb=conj(inv(vals[4]),b);cc=conj(inv(vals[5]),c)
    u=mul(cc,inv(aa));v=mul(mul(mul(mul(mul(aa,bb),aa),inv(cc)),inv(bb)),inv(aa))
    assert u[:4]==v[:4]==one[:4]
    C=np.column_stack((u[4:],v[4:])).astype(np.int64)
    errors=np.r_[residual[4:],(C@matrix(a)-matrix(aa)@C).ravel(),
                             (C@matrix(b)-matrix(bb)@C).ravel()]%p
    return errors,C,(aa,bb,cc)

rows=[];start=time.time();rng=np.random.default_rng(232027)
for ix,rec in enumerate(records):
    beta=rec['base_beta_word_B'];g=rec['integral_cusp_gauge']
    cg=d['bpower'](d['xword'],g)
    fw=d['fword']([0]+cg+beta+[0]+d['binv'](beta)+d['binv'](cg))
    assert all(sum((1 if x==i else -1 if x==-i else 0) for x in fw)==0 for i in (1,2))
    vals=manyword(fw);res,C0,_=system(vals)
    J=np.column_stack([(system(corrected(vals,W[:,j]))[0]-res)%p
                       for j in range(W.shape[1])]) if W.shape[1] else np.zeros((10,0),dtype=np.int64)
    for _ in range(8):
        z=rng.integers(0,p,size=W.shape[1])
        assert np.array_equal(system(corrected(vals,W@z%p))[0],(res+J@z)%p)
    solution=solve(J,-res)
    row={'certificate_index':ix,'missing_coset':rec['missing_coset'],
         'retained_G6_f_word_length':len(fw),'correction_dimension':W.shape[1],
         'unadjusted_pentagon_residual':res[:2].tolist(),
         'unadjusted_intertwiner_residual':res[2:].tolist(),
         'unadjusted_Ferrari_homology_matrix':C0.tolist(),
         'linear_equation_rank':len(rref(J)[1]),
         'pentagon_and_intertwiner_solution_exists':solution is not None,
         'invertible_Ferrari_homology_action_found':False}
    if solution is not None:
        z0,K=solution;basevals=corrected(vals,W@z0%p);_,Cbase,_=system(basevals)
        ccols=np.column_stack([(system(corrected(vals,W@(z0+K[:,j])%p))[1]-Cbase).ravel()%p
                              for j in range(K.shape[1])]) if K.shape[1] else np.zeros((4,0),dtype=np.int64)
        _,selected=rref(ccols);row['remaining_matrix_parameter_dimension']=len(selected)
        row['all_matrix_choices_tested']=p**len(selected)
        success=[]
        for bits in product(range(p),repeat=len(selected)):
            zz=(z0+K[:,selected]@np.array(bits,dtype=np.int64))%p
            newvals=corrected(vals,W@zz%p);error,C,images=system(newvals)
            assert not np.any(error)
            det=int((C[0,0]*C[1,1]-C[0,1]*C[1,0])%p)
            if det:
                aa,bb,cc=images
                assert mul(mul(aa,bb),aa)==mul(mul(bb,aa),bb)
                assert mul(mul(bb,cc),bb)==mul(mul(cc,bb),cc)
                assert mul(aa,cc)==mul(cc,aa)
                success.append((zz,C,det))
        row['invertible_choices']=len(success)
        if success:
            zz,C,det=success[0]
            row.update({'invertible_Ferrari_homology_action_found':True,
                        'correction_basis_coefficients':zz.tolist(),
                        'Ferrari_homology_matrix':C.tolist(),'determinant_mod3':det,
                        'all_five_pentagon_factors_verified':True,
                        'three_braid_relations_verified':True})
    rows.append(row);print(json.dumps(row),flush=True)
out={'representation':'F3^2 semidirect SL2(F3), sigma1=(0,A), sigma2=(0,B), sigma3=(e1,A)',
     'pure_four_strand_quotient_order_after_adjoining_S4':len(joint),
     'pentagon_convention':'f(A12,A23*A24)*f(A13*A23,A34)=f(A23,A34)*f(A12*A13,A24*A34)*f(A12,A23)',
     'correction_image_dimension':W.shape[1],'correction_basis_commutator_pairs':basis_pairs,
     'all_N_generator_images_have_order_dividing3':True,
     'all_N_commutator_images_centralize_N':True,
     'pass_counts':[sum(r['invertible_Ferrari_homology_action_found'] and r['missing_coset']==b for r in rows) for b in (False,True)],
     'records':rows,'elapsed_seconds':round(time.time()-start,3),
     'scope':'Complete finite Ferrari-homology pentagon and homology-automorphism test over the retained G6 representatives, allowing the entire common N-prime correction image. This does not enumerate all compatible four-strand shadows or all CM matrix fibres.'}
(here/'de_ferrari_pentagon.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2),flush=True)
