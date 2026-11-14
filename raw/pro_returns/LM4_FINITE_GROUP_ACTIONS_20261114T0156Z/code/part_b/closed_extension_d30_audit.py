#!/usr/bin/env python3
"""Exact word and finite-cochain certificates for the closed D.30 extension.

The profinite existence and surface-cohomology inputs are proved/cited in
D.30.  This program checks the free-group presentation isomorphism and
every possible reduced 2x2 abelianization matrix at p=3 and p=5.  It does
not replace the chosen Galois automorphism by a guessed integral lift.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import json

OUT=Path(__file__).resolve().parent

def red(word):
 out=[]
 for x in word:
  if out and out[-1]==-x:out.pop()
  else:out.append(x)
 return tuple(out)
def inverse(word):return tuple(-x for x in reversed(word))
def substitute(word,images):
 return red(y for x in word for y in
   (images[abs(x)-1] if x>0 else inverse(images[abs(x)-1])))
def compose(f,g):return tuple(substitute(w,f) for w in g)
def notation(word,names=('x','y','t')):
 return ' '.join(names[abs(x)-1]+('^-1' if x<0 else '') for x in word) or '1'

def words():
 identity=((1,),(2,),(3,))
 # phi: free(x,y,t) -> free(a,b,c), and its exact inverse psi.
 phi=((1,-3,-2,-1),(1,2,3,1,2,-1),(1,2,3))
 psi=((1,3),(-3,-1,-3,2,1,3),(-3,-1,-2,3,3))
 assert compose(phi,psi)==compose(psi,phi)==identity
 comm=(1,2,-1,-2);R=comm+(3,3);N3=(1,1,2,2,3,3)
 assert substitute(R,phi)==N3 and substitute(N3,psi)==R
 # The actual elimination gives t^2 [x,y]; it is conjugate to R by t^-2.
 actual=(3,3)+comm
 assert red((-3,-3)+actual+(3,3))==R
 # Upon t^2=l the remaining relation t l t^-1=l is redundant.
 assert red((3,3,3,-3,-3,-3))==()
 # The quotient character x,y ->0, t->1 sends every new crosscap to1.
 parity=[sum(abs(x)==3 for x in w)%2 for w in psi]
 assert parity==[1,1,1]
 # Three explicit elementary automorphisms produce phi.
 steps=[((1,-3),(3,2),(3,)),((1,),(2,),(2,3)),
        ((1,),(1,2,-1),(1,3))]
 inverse_steps=[((1,3),(-3,2),(3,)),((1,),(2,),(-2,3)),
                ((1,),(-1,2,1),(-1,3))]
 f=identity
 for a,b in zip(steps,inverse_steps):
  assert compose(a,b)==compose(b,a)==identity
  f=compose(a,f)
 assert f==phi
 # The closed genus-two presentation admits actual retractions onto each
 # free vertex group; these also certify the required vertex injections.
 surface_relation=(1,2,-1,-2,3,4,-3,-4)
 retract_P1=((1,),(2,),(2,),(1,))
 retract_P2=((4,),(3,),(3,),(4,))
 assert substitute(surface_relation,retract_P1)==substitute(surface_relation,retract_P2)==()
 return {'letter_encoding':'1=x/a, 2=y/b, 3=t/c; negative numbers mean inverses',
  'initial_pro2_relator':actual,'cyclically_conjugate_relator':R,
  'phi_images':phi,'inverse_psi_images':psi,'target_relator':N3,
  'phi_images_in_a_b_c':[notation(w,('a','b','c')) for w in phi],
  'psi_images_in_x_y_t':[notation(w) for w in psi],
  'both_composites_identity':True,'both_relator_substitutions_exact':True,
  'elementary_automorphisms':steps,'elementary_inverse_automorphisms':inverse_steps,
  'parity_on_three_crosscaps':parity,'redundant_conjugation_relation_checked':True,
  'vertex_retraction_certificate':{'letter_encoding':'1=x,2=y,3=u,4=v',
    'closed_genus_two_relator':surface_relation,
    'retraction_onto_P1_images':retract_P1,'retraction_onto_P2_images':retract_P2,
    'both_relator_images_trivial':True}}

def eye(n):return [[int(i==j) for j in range(n)] for i in range(n)]
def transpose(A):return [list(a) for a in zip(*A)]
def matrix_product(A,B,p):
 return [[sum(a*b for a,b in zip(row,col))%p for col in zip(*B)] for row in A]
def matrix_sum(A,B,p,s=1):
 return [[(x+s*y)%p for x,y in zip(a,b)] for a,b in zip(A,B)]
def scale(A,k,p):return [[k*x%p for x in row] for row in A]
def rank(A,p):
 a=[list(row) for row in A];i=0
 if not a:return 0
 for j in range(len(a[0])):
  pivot=next((k for k in range(i,len(a)) if a[k][j]%p),None)
  if pivot is None:continue
  a[i],a[pivot]=a[pivot],a[i]
  a[i]=[x*pow(a[i][j],-1,p)%p for x in a[i]]
  for k in range(len(a)):
   if k!=i:
    c=a[k][j];a[k]=[(x-c*y)%p for x,y in zip(a[k],a[i])]
  i+=1
  if i==len(a):break
 return i
def inv2(A,p):
 a,b=A[0];c,d=A[1];delta=pow((a*d-b*c)%p,-1,p)
 return scale([[d,-b],[-c,a]],delta,p)
def symplectic4(p):return [[0,1,0,0],[-1%p,0,0,0],[0,0,0,1],[0,0,-1%p,0]]
def periodic_cochains(T,p):
 n=len(T);I=eye(n);D=matrix_sum(T,I,p,-1);N=matrix_sum(T,I,p)
 assert matrix_product(T,T,p)==I
 assert rank(matrix_product(D,N,p),p)==rank(matrix_product(N,D,p),p)==0
 rd,rn=rank(D,p),rank(N,p)
 assert rd+rn==n
 P=scale(N,pow(2,-1,p),p)
 assert matrix_product(P,P,p)==P
 assert rank(P,p)==n-rd
 return {'dimension':n,'action':T,'difference_T_minus_I':D,'norm_I_plus_T':N,
  'rank_difference':rd,'rank_norm':rn,'invariant_dimension':n-rd,
  'positive_degree_periodic_cohomology_dimensions':[n-rn-rd,n-rd-rn],
  'averaging_projection':P}

def cochains_at_prime(p,epsilon):
 lam=(-epsilon)%p;J=symplectic4(p);allrows=[]
 for a,b,c,d in product(range(p),repeat=4):
  if (a*d-b*c)%p!=lam:continue
  A=[[a,b],[c,d]];Ai=inv2(A,p)
  M=[[0]*4 for _ in range(4)]
  for i,j in product(range(2),repeat=2):M[i][j+2]=Ai[i][j];M[i+2][j]=A[i][j]
  assert matrix_product(M,M,p)==eye(4)
  assert matrix_product(matrix_product(transpose(M),J,p),M,p)==scale(J,lam,p)
  T=transpose(M)
  assert matrix_product(matrix_product(transpose(T),J,p),T,p)==scale(J,lam,p)
  modules=[periodic_cochains([[1]],p),periodic_cochains(T,p),periodic_cochains([[lam]],p)]
  dims=[q['invariant_dimension'] for q in modules]
  assert dims==[1,2,1 if p==3 else 0]
  allrows.append({'tau_abelianization_matrix':A,'alpha_on_H1_homology':M,
    'alpha_on_H1_cohomology':T,'cup_multiplier':lam,'degree_0_1_2_C2_modules':modules,
    'LHS_surviving_column_dimensions':dims})
 assert len(allrows)==p*(p*p-1)
 # Ordinary nonorientable genus-three cellular coboundary is (2,2,2).
 # This is recorded separately from E: its two odd-prime H2 groups vanish.
 n3_boundary=[[2%p,2%p,2%p]]
 assert rank(n3_boundary,p)==1
 return {'prime':p,'epsilon':epsilon%p,'lambda':lam,
  'all_determinant_lambda_matrices_checked':len(allrows),
  'all_periodic_C2_complexes_exact_in_positive_degrees':True,
  'H0_H1_H2_of_E_dimensions':[1,2,1 if p==3 else 0],
  'ordinary_N3_augmented_Fox_coboundary':n3_boundary,
  'ordinary_N3_H2_dimension':0,'matrix_and_cochain_certificates':allrows}

def exponent_cases():
 rows=[]
 for p in (2,3,5):
  for k in range(1,5):
   modulus=p**k;e=-1 if p==3 else 1;kap=1 if p==2 else 0;lam=-e
   assert (e*e-1)%modulus==(lam*lam-1)%modulus==0
   assert (e*kap-kap)%modulus==0
   # l=w1^-1=w2: the two vertex definitions have the same edge image.
   first=-lam%modulus;second=-pow(lam%modulus,-1,modulus)%modulus
   assert first==second==e%modulus
   rows.append({'p':p,'power':k,'modulus':modulus,'epsilon':e%modulus,
    'lambda':lam%modulus,'kappa':kap,'edge_exponent_from_P1':first,
    'edge_exponent_from_P2':second,'alpha_c_exponent':e*kap%modulus})
 return rows

def main():
 out={'claim':'D.30','word_certificate':words(),'edge_exponent_checks':exponent_cases(),
  'finite_cochain_certificates':[cochains_at_prime(3,-1),cochains_at_prime(5,1)],
  'H2_dimensions_at_3_and_5':[1,0],
  'source_inputs':[
   {'source':'H. Nakamura, Publ. RIMS 49 (2013), 413-496, DOI10.4171/PRIMS/110',
    'url':'https://ems.press/content/serial-article-files/41205',
    'location':'Section2.5 p.424; also Theorem5.2.4 pp.449-450',
    'input':'Full profinite tangential Galois action stabilizes chosen inertia and acts by the cyclotomic character.'},
   {'source':'G. Wilkes, arXiv:1711.02953v2, Section1.4, Theorem1.9',
    'input':'The rank-three pro-2 word t^2[x,y] is the infinite nonorientable surface Demushkin presentation, of cohomological dimension2.'},
   {'source':'A.2/A.7 and D.30',
    'input':'The genus-two profinite surface has cohomology dimensions1,4,1 and its standard nondegenerate cup pairing; odd-order coefficient characteristic makes C2 invariants exact.'}],
  'scope':'Exact finite linear-algebra and free-word certificates; the profinite construction, gluing, and torsion-freeness arguments are supplied in D.30.'}
 (OUT/'closed_extension_d30_audit.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({'claim':out['claim'],'word_certificate':out['word_certificate'],
  'edge_exponent_checks':len(out['edge_exponent_checks']),
  'prime_checks':[{'prime':r['prime'],'matrices':r['all_determinant_lambda_matrices_checked'],
    'H0_H1_H2':r['H0_H1_H2_of_E_dimensions']} for r in out['finite_cochain_certificates']]},indent=2))

if __name__=='__main__':main()
