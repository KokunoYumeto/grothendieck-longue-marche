"""Independent verifiers for S2 and S3; no producer module is imported.

S2: plain integer finite-field/polynomial arithmetic and integer Bareiss
determinants, independent of FLINT and SymPy used by the producer.
S3: full 55-square matrices and truncated tensor algebra for class-two
word evaluation, independent of the producer's (A,B) composition code.
"""
from pathlib import Path
import json,itertools,time
import numpy as np
out=Path(__file__).resolve().parent;tstart=time.time()
def binary_mul(a,b,mod):
 c=0
 while b:
  if b&1:c^=a
  b//=2;a*=2
  if a.bit_length()==mod.bit_length():a^=mod
 return c
mt=[[binary_mul(a,b,11) for b in range(8)] for a in range(8)]
def fi(a):return next(b for b in range(1,8) if mt[a][b]==1)
def trim(a):
 a=list(a)
 while a and a[-1]==0:a.pop()
 return tuple(a)
def pa(a,b):return trim([(a[i] if i<len(a) else 0)^(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])
def pm(a,b):
 c=[0]*max(0,len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]^=mt[x][y]
 return trim(c)
def scale(a,z):return trim([mt[x][z] for x in a])
def div(a,b):
 a=list(trim(a));b=trim(b);assert b
 q=[0]*max(0,len(a)-len(b)+1);ib=fi(b[-1])
 while len(a)>=len(b):
  d=len(a)-len(b);z=mt[a[-1]][ib];q[d]=z
  for i,x in enumerate(b):a[i+d]^=mt[z][x]
  a=list(trim(a))
 return trim(q),tuple(a)
def monic(a):return scale(a,fi(a[-1]))
def pgcd(a,b):
 aa,bb=(1,),();cc,dd=(),(1,)
 while b:
  q,r=div(a,b);a,b=b,r
  aa,cc=cc,pa(aa,pm(q,cc));bb,dd=dd,pa(bb,pm(q,dd))
 z=fi(a[-1]);return scale(a,z),scale(aa,z),scale(bb,z)
def quotient(a,b):
 q,r=div(a,b);assert not r;return q
h=(0,1,1);f=(1,0,0,0,0,1)
def ja(D,E):
 u,v=D;s,w=E;d0,e1,e2=pgcd(u,s);d,z1,z2=pgcd(d0,pa(pa(v,w),h))
 a1,a2,a3=pm(z1,e1),pm(z1,e2),z2
 U=quotient(pm(u,s),pm(d,d))
 V=quotient(pa(pa(pm(pm(a1,u),w),pm(pm(a2,s),v)),pm(a3,pa(pm(v,w),f))),d)
 V=div(V,U)[1]
 while len(U)>3:
  U=monic(quotient(pa(pa(pm(V,V),pm(h,V)),f),U));V=div(pa(h,V),U)[1]
 return monic(U),div(V,U)[1]

def bareiss(A):
 A=[row[:] for row in A];n=len(A);last=1;sign=1
 for k in range(n-1):
  if A[k][k]==0:
   s=next((s for s in range(k+1,n) if A[s][k]),None)
   if s is None:return 0
   A[k],A[s]=A[s],A[k];sign=-sign
  d=A[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):
    num=A[i][j]*d-A[i][k]*A[k][j];assert num%last==0;A[i][j]=num//last
  for i in range(k+1,n):A[i][k]=0
  last=d
 return sign*A[-1][-1]
def cyclonorm(coeff):
 cols=[]
 for j in range(18):
  a=[0]*j+list(coeff)
  for i in range(len(a)-1,17,-1):
   c=a[i]
   for d in range(1,19):a[i-d]-=c
   a[i]=0
  cols.append(a[:18])
 return bareiss(list(map(list,zip(*cols))))

def s2():
 a=json.loads((out/'s2_f8_witness.json').read_text())
 J=[tuple(tuple(z) for z in D) for D in a['Mumford_representatives']]
 ix={D:i for i,D in enumerate(J)};tab=a['addition_table'];ch=a['character_table'];assert len(ix)==76
 for i,D in enumerate(J):
  for j,E in enumerate(J):
   assert ix[ja(D,E)]==tab[i][j]
   assert ch[tab[i][j]]==(ch[i]+ch[j])%19
 for rec in a['certificates']:
  assert cyclonorm(rec['L_at_1_coefficients'])==int(rec['relative_class_number'])
  assert int(rec['relative_class_number'])%2
 return {'verified':True,'Mumford_additions_independently_recomputed':76**2,
         'integer_norm_determinants':len(a['certificates']),
         'P_Q_relative_class_number':a['certificates'][0]['relative_class_number']}

def mat_inv(A,p=5):
 n=len(A);B=np.column_stack((A,np.eye(n,dtype=np.int64)))%p
 for j in range(n):
  i=next(i for i in range(j,n) if B[i,j]);B[[i,j]]=B[[j,i]]
  B[j]=(B[j]*pow(int(B[j,j]),-1,p))%p
  for i in range(n):
   if i!=j:B[i]=(B[i]-B[i,j]*B[j])%p
 return B[:,n:]
def mr(A,p=5):
 A=A.copy()%p;r=0
 for j in range(A.shape[1]):
  i=next((i for i in range(r,len(A)) if A[i,j]),None)
  if i is None:continue
  A[[i,r]]=A[[r,i]];A[r]=(A[r]*pow(int(A[r,j]),-1,p))%p
  for i in range(r+1,len(A)):A[i]=(A[i]-A[i,j]*A[r])%p
  r+=1
  if r==len(A):break
 return r
def s3():
 d=json.loads((out/'s3_nonnilpotent.json').read_text());n=10;pairs=list(itertools.combinations(range(n),2))
 eye=np.eye(55,dtype=np.int64);Gs={};linears=[]
 for k,g in enumerate(d['automorphism_generators'],1):
  A=np.array(g['linear'],dtype=np.int64);B=np.array(g['central'],dtype=np.int64)
  E=np.array([[int(A[i,r]*A[j,s]-A[i,s]*A[j,r])%5 for r,s in pairs] for i,j in pairs],dtype=np.int64)
  M=np.block([[A,np.zeros((10,45),dtype=np.int64)],[B,E]])
  Gs[k]=M;Gs[-k]=mat_inv(M);assert np.array_equal(Gs[k]@Gs[-k]%5,eye)
  linears.append(A)
 def ev(w):
  M=eye
  for j in w:M=M@Gs[j]%5
  return M
 for r in d['pure_relators']:assert np.array_equal(ev(r['word']),eye)
 W=np.array(d['cusp_space_W'],dtype=np.int64);assert mr(W)==2
 Ns=[]
 for r in d['H_Schreier_generators']:
  M=ev(r['word']);N=(M[:10,:10]-np.eye(10,dtype=np.int64))%5
  assert M[:10,:10].tolist()==r['linear'] and M[10:,:10].tolist()==r['central']
  assert mr(np.column_stack([W,N]))==2 and not np.any(N@W%5);Ns.append(N)
 assert all(not np.any(N@M%5) for N in Ns for M in Ns)

 # Independently evaluate free class-two words in a truncated associative
 # algebra, where generator i is exp(X_i)=1+X_i+X_i^2/2.
 edges=[tuple(e) for e in d['K_edges']];ei={e:i for i,e in enumerate(edges)}
 def rewrite(word):
  state=0;ans=[]
  for j in word:
   if j>0:edge=(state,j)
   else:edge=((state-(j==-1))%3,-j)
   if edge in ei:ans.append((ei[edge]+1)*(1 if j>0 else -1))
   state=(state+(j==1)-(j==-1))%3
  assert state==0
  return ans
 def tensor(word):
  v=np.zeros(10,dtype=np.int64);B=np.zeros((10,10),dtype=np.int64)
  for j in word:
   u=np.zeros(10,dtype=np.int64);u[abs(j)-1]=1 if j>0 else -1
   B=(B+3*np.outer(u,u)+np.outer(v,u))%5;v=(v+u)%5
  skew=(B-3*np.outer(v,v))%5
  assert not np.any((skew+skew.T)%5)
  return v,np.array([skew[i,j] for i,j in pairs],dtype=np.int64)
 def inverse(w):return [-j for j in w[::-1]]
 def substitution(w,phi):return [j for x in w for j in (phi[x-1] if x>0 else inverse(phi[-x-1]))]
 first=[[[i,j,-i] for j in range(1,5)] for i in range(1,5)]
 for k,phi in enumerate(first+d['second_strand_F4_automorphisms']):
  vecs=[tensor(rewrite(substitution(w,phi))) for w in d['basis_F4_words']]
  A=np.column_stack([v for v,z in vecs]);B=np.column_stack([z for v,z in vecs])
  assert A.tolist()==d['automorphism_generators'][k]['linear']
  assert B.tolist()==d['automorphism_generators'][k]['central']
 S=np.array(d['deck_action_S']);assert np.array_equal(S@S@S%5,np.eye(2,dtype=np.int64))
 assert mr(np.array(d['Q_factor_map_lambda']))==2
 return {'verified':True,'full_55_by_55_matrix_relations':len(d['pure_relators']),
  'independent_truncated_tensor_word_images':80,'Schreier_shears':len(Ns),
  'shear_pair_products':len(Ns)**2,'shear_span_dimension':mr(np.column_stack([N.reshape(-1) for N in Ns]))}

res={'S2':s2(),'S3':s3(),'seconds':time.time()-tstart,'imports_no_producer_module':True}
(out/'verify_newcerts.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res,indent=2))
