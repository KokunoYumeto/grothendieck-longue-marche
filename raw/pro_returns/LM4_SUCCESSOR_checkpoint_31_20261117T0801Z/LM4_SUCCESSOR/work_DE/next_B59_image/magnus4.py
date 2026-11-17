"""Integral degree-four Magnus expansions of the Artin action.

The returned homogeneous logarithmic derivations are D1,2D2,24D3.
Conjugation is expanded symbolically through degree4; no floating-point
arithmetic or truncated braid representation faithfulness is assumed.
"""
from nilpotent_derivations import *

def mul(p,q):
 out=defaultdict(int)
 for a,x in p.items():
  for b,y in q.items():out[a+b]+=x*y
 return clean(out)
def mul3(a,b,c):return mul(mul(a,b),c)
def mul4(a,b,c,d):return mul(mul3(a,b,c),d)

def magnus_artin4(word,n):
 images=[(i,{}, {}, {}) for i in range(n)]
 def conjugate(a,b,negative=False):
  i,U2,U3,U4=a;j,B2,B3,B4=b
  xi={(i,):1};B1={(j,):1}
  if negative:
   A1=scale(xi,-1)
   A2=add({(i,i):1},scale(U2,-1))
   A3=add(scale(U3,-1),prefix(i,U2),suffix(U2,i),{(i,i,i):-1})
  else:A1=xi;A2=U2;A3=U3
  two=add(B2,mul(A1,B1),scale(mul(B1,A1),-1))
  three=add(B3,mul(A1,B2),mul(A2,B1),scale(mul(B1,A2),-1),scale(mul(B2,A1),-1),
            mul3(B1,A1,A1),scale(mul3(A1,B1,A1),-1))
  four=add(B4,mul(A1,B3),mul(A2,B2),mul(A3,B1),
           scale(mul(B1,A3),-1),scale(mul(B2,A2),-1),scale(mul(B3,A1),-1),
           mul3(B1,A1,A2),mul3(B1,A2,A1),mul3(B2,A1,A1),
           scale(mul3(A1,B1,A2),-1),scale(mul3(A1,B2,A1),-1),scale(mul3(A2,B1,A1),-1),
           mul4(A1,B1,A1,A1),scale(mul4(B1,A1,A1,A1),-1))
  return j,two,three,four
 for a in word:
  k=abs(a)-1;u,v=images[k:k+2]
  images[k:k+2]=[conjugate(u,v),u] if a>0 else [v,conjugate(v,u,True)]
 return images

def log_parts4(word,n):
 im=magnus_artin4(word,n)
 assert [x[0] for x in im]==list(range(n))
 D1=[x[1] for x in im]
 twice=[];Y4num=[]
 for i,(_,M2,M3,M4) in enumerate(im):
  dup2=defaultdict(int)
  for (a,b),c in M2.items():dup2[(a,a,b)]+=c;dup2[(a,b,b)]+=c
  tw=add(scale(M3,2),clean(dup2),scale(prefix(i,M2),-1),scale(suffix(M2,i),-1),scale(apply(D1,M2),-1))
  twice.append(tw)
  p1={(i,):1}
  p2=add(scale(M2,2),{(i,i):1})
  p3=add(scale(M3,6),scale(clean(dup2),3),{(i,i,i):1})
  dup3=defaultdict(int)
  for w,c in M3.items():
   for j,a in enumerate(w):dup3[w[:j]+(a,)+w[j:]]+=c
  ext2=defaultdict(int)
  for (a,b),c in M2.items():
   ext2[(a,a,a,b)]+=4*c;ext2[(a,b,b,b)]+=4*c;ext2[(a,a,b,b)]+=6*c
  p4=add(scale(M4,24),scale(clean(dup3),12),clean(ext2),{(i,i,i,i):1})
  y4=add(p4,scale(mul(p1,p3),-2),scale(mul(p3,p1),-2),scale(mul(p2,p2),-3),
         scale(mul3(p1,p1,p2),4),scale(mul3(p1,p2,p1),4),scale(mul3(p2,p1,p1),4),
         {(i,i,i,i):-6})
  Y4num.append(y4)
 third=[]
 for i in range(n):
  z=add(Y4num[i],scale(apply(D1,twice[i]),-6),scale(apply(twice,D1[i]),-6),
        scale(apply(D1,apply(D1,D1[i])),-4))
  third.append(z)
 return D1,twice,third

def product_log_parts4(parts):
 n=len(parts[0][0]);one=deriv_zero(n);two=deriv_zero(n);three=deriv_zero(n)
 for x,y,z in parts:
  c=bracket(one,x)
  three=deriv_add(three,z,deriv_scale(bracket(one,y),6),deriv_scale(bracket(two,x),6),
                  deriv_scale(bracket(one,c),2),deriv_scale(bracket(x,deriv_scale(c,-1)),2))
  two=deriv_add(two,y,c);one=deriv_add(one,x)
 return one,two,three

def self_test4():
 n=3;identity=magnus_artin4([],n)
 for i in [1,2]:
  assert magnus_artin4([i,-i],n)==identity
  assert magnus_artin4([-i,i],n)==identity
 assert magnus_artin4([1,2,1],n)==magnus_artin4([2,1,2],n)
 examples=[[1,1],[2,2],[2,1,1,-2],[1,1,2,2],[-2,-2,1,1,2,2]]
 for w in examples:
  im=magnus_artin4(w,n)
  assert [(a,b,c) for a,b,c,d in im]==magnus_artin(w,n)
  a,b,c=log_parts4(w,n);assert (a,b)==log_parts(w,n)
  neg=log_parts4([-x for x in w[::-1]],n)
  assert neg==(deriv_scale(a,-1),deriv_scale(b,-1),deriv_scale(c,-1))
 a=log_parts4([1,1],n);b=log_parts4([2,2],n)
 assert log_parts4([1,1,2,2],n)==product_log_parts4([a,b])
 # A weight-three group commutator has exactly the predicted leading derivation.
 x=[1,1];y=[2,2];comm=x+y+[-i for i in x[::-1]]+[-i for i in y[::-1]]
 word=comm+x+[-i for i in comm[::-1]]+[-i for i in x[::-1]]
 p,q,r=log_parts4(word,n)
 assert not any(p) and not any(q)
 expected=bracket(bracket(a[0],b[0]),a[0])
 assert r==deriv_scale(expected,24)
 print('PASS degree4 Artin relations/inverses, degree3 consistency, full BCH, and weight3 commutator sign')

if __name__=='__main__':self_test4()
