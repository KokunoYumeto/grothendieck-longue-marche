"""Exact local Artin action at the actual sum-pencil source T=1."""
from pathlib import Path
import itertools,json
CE=Path(__file__).resolve().parents[1]
def red(w):
 o=[]
 for x in w:
  if o and o[-1]==-x:o.pop()
  else:o.append(x)
 return tuple(o)
def iv(w):return tuple(-x for x in w[::-1])
def mul(*ws):return red(itertools.chain.from_iterable(ws))
def cj(h,w):return mul(h,w,iv(h))
def sub(w,A):return mul(*(A[x] if x>0 else iv(A[-x]) for x in w))
def art(w):
 A={i:(i,) for i in range(1,6)}
 for x in w:
  i=abs(x);a,b=A[i],A[i+1]
  A[i],A[i+1]=(cj(a,b),a) if x>0 else (b,cj(iv(b),a))
 return A
D5=(1,2,3,4,1,2,3,1,2,1);D3=(2,3,2);beta=D5+D3
A=art(beta);Ai=art(iv(beta));R=(1,2,3,4);C=(1,2,3,4,5)
assert art(D5+D3)==art(D3+D5)
expected={1:cj(R,(5,)),2:cj(R,(2,)),3:cj(R,(3,)),4:cj(R,(4,)),5:(1,)}
assert A==expected
for i in range(1,6):assert sub(A[i],Ai)==(i,)==sub(Ai[i],A)
assert sub(C,A)==C
perm=[]
for i in range(1,6):
 d={j:sum((1 if x==j else -1 if x==-j else 0) for x in A[i]) for j in range(1,6)}
 perm.append(next(j for j,n in d.items() if n))
assert perm==[5,2,3,4,1]
out={'scope':'Local five-point source cluster only; actual common global whisker remains to be constructed.',
 'delta5':D5,'inner_delta3':D3,'positive_local_beta':beta,'exponent':len(beta),
 'Artin_images':A,'inverse_images':Ai,'permutation':perm,'R':R,'source_boundary_C':C,
 'variation_quotient':'y5=y1; R=y1*y2*y3*y4 central. Hence quotient is Z(R) times F3(y1,y2,y3), with y4=(y1*y2*y3)^-1 R.',
 'source_boundary_image':'C=R*y1; its exponent vector in the four component meridians is(2,1,1,1).'}
(CE/'sum_pencil_five_point_monodromy.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: beta=Delta5*Delta3_inner, exponent13, outer permutation(1 5).')
print('PASS: Delta5 commutes with inner Delta3; exact Artin action and both inverses checked.')
print('beta(y1)=R*y5*R^-1; beta(yi)=R*yi*R^-1 fori2,3,4; beta(y5)=y1.')
print('Variation quotient: y5=y1 and R=y1*y2*y3*y4 central, hence Z times F3.')
print('Actual source boundary C=y1*y2*y3*y4*y5 maps to R*y1.')
