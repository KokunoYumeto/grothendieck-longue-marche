"""Exact conjugate-relator fillings in the closed genus-two presentation.

The fixed presentation has the ten Artin relations on B6, five [W,s_i],
W^2, and omega6.  Braid equalities retain every right/left word-reversing
cell.  Pure-braid combing then eliminates each A_i6 using the actual
spherical star W_i=t_i W t_i^-1.  The residual B5 central power is
converted by omega5=W^-1.  Every returned certificate is freely checked.

Primary reversing input: Dehornoy--Wiest, On word reversing in braid
groups, section1 Proposition4, Lemma5 and following Remark (pp3--4).
"""
from pathlib import Path
from functools import lru_cache
from itertools import combinations
import json,time
P=Path(__file__).resolve().parent
H={};exec((P/'b_genus_zero.py').read_text().split('\ndata={}')[0],H)
red,inv,A,full,comb,expand=map(H.get,['red','inv','A','full','comb','expand'])
def cat(*ws):return red(x for w in ws for x in w)
W=(1,2,3,4,5,5,4,3,2,1)
O5=full(5);O6=full(6)
PAIRS=list(combinations(range(1,6),2))
RULES=[((i,j,i),(j,i,j)) if j==i+1 else ((i,j),(j,i)) for i,j in PAIRS]
RELS=[cat(a,inv(b)) for a,b in RULES]
COMM={}
for i in range(1,6):COMM[i]=len(RELS);RELS.append(cat(W,(i,),inv(W),(-i,)))
W2=len(RELS);RELS.append(cat(W,W))
OMEGA=len(RELS);RELS.append(O6)
def conjugate(c,S):return tuple((cat(c,p),j,e) for p,j,e in S)
def inverse(S):return tuple((p,j,-e) for p,j,e in reversed(S))
def expanded(S):
 out=[]
 for c,j,e in S:
  for x in c+(RELS[j] if e>0 else inv(RELS[j]))+inv(c):
   if out and out[-1]==-x:out.pop()
   else:out.append(x)
 return tuple(out)
def reduce_sequence(S):
 out=[]
 for x in S:
  if out and out[-1][:2]==x[:2] and out[-1][2]==-x[2]:out.pop()
  else:out.append(x)
 return tuple(out)
def power(w,n):return w*n if n>=0 else inv(w)*(-n)

@lru_cache(maxsize=100)
def reverse_cell(i,j,right):
 """Return lhs,rhs and the exact conjugate of one Artin relator."""
 assert i!=j
 lhs=(-i,j) if right else (i,-j)
 if abs(i-j)>1:rhs=(j,-i) if right else (-j,i)
 else:rhs=(j,i,-j,-i) if right else (-j,-i,j,i)
 diff=cat(lhs,inv(rhs));rid=PAIRS.index(tuple(sorted((i,j))))
 for sign in (1,-1):
  rw=RELS[rid] if sign>0 else inv(RELS[rid])
  for k in range(len(rw)):
   c=inv(rw[:k])
   if cat(c,rw,inv(c))==diff:return lhs,rhs,(c,rid,sign)
 raise AssertionError(('unidentified local reversing cell',i,j,right,diff))

def reversing(w,right):
 w=list(red(w));out=[];i=0;steps=0
 while i+1<len(w):
  a,b=w[i:i+2]
  active=(a<0<b) if right else (a>0>b)
  if not active:i+=1;continue
  if a==-b:w[i:i+2]=[];i=max(0,i-1);continue
  lhs,rhs,C=reverse_cell(abs(a),abs(b),right)
  assert tuple(w[i:i+2])==lhs
  c,j,e=C;out.append((cat(w[:i],c),j,e))
  w[i:i+2]=rhs;i=max(0,i-1);steps+=1
  if steps>5000000:raise RuntimeError('reversing certificate exceeded 5M cells')
 return tuple(w),tuple(out)

@lru_cache(maxsize=20000)
def braid_fill(w):
 w=red(w)
 if not w:return ()
 v,S=reversing(w,True)
 z,T=reversing(v,False)
 if z:raise AssertionError(('nonidentity braid after two reversing passes',w,z))
 out=reduce_sequence(S+T)
 assert expanded(out)==w,('braid certificate expansion',w)
 return out

def commute_g_W(g):
 """Certificate for g W g^-1 W^-1 using the five fixed commutators."""
 out=[];g=tuple(g)
 for k in range(len(g)-1,-1,-1):
  x=g[k];C=(((),COMM[x],-1),) if x>0 else (((x,),COMM[-x],1),)
  out.extend(conjugate(g[:k],C))
 out=tuple(out)
 assert expanded(out)==cat(g,W,inv(g),inv(W))
 return out

# The six actual spherical star words and their compact certificates.
STARS={};STAR_CERT={};LAST_CERT={};LAST_REPLACE={}
for i in range(1,7):
 t=tuple(range(i-1,0,-1))
 star=cat(*(A(min(i,j),max(i,j)) for j in range(1,7) if j!=i))
 Wi=cat(t,W,inv(t));STARS[i]=star
 C=braid_fill(cat(star,inv(Wi)))+commute_g_W(t)
 C=reduce_sequence(C);assert expanded(C)==cat(star,inv(W))
 STAR_CERT[i]=C
 if i<=5:
  Li=cat(*(A(min(i,j),max(i,j)) for j in range(1,6) if j!=i))
  old=A(i,6);new=cat(inv(Li),W)
  Cp=conjugate(inv(Li),C)
  assert expanded(Cp)==cat(old,inv(new))
  LAST_CERT[i,1]=Cp
  LAST_CERT[i,-1]=conjugate(inv(old),inverse(Cp))
  # Letter6 here is only an internal abbreviation for W.
  LAST_REPLACE[i,1]=inv(Li)+(6,)
  LAST_REPLACE[i,-1]=(-6,)+Li

def untoken(w):return cat(*(W if x==6 else inv(W) if x==-6 else (x,) for x in w))
def collect_W(tokens):
 """Move the abbreviation W to the right, retaining each compact cell."""
 w=list(red(tokens));out=[];i=0
 while i+1<len(w):
  a,b=w[i:i+2]
  if abs(a)!=6 or abs(b)==6:i+=1;continue
  # Local difference is [W^sign(a), b].
  Cg=commute_g_W((b,))
  C=inverse(Cg) if a==6 else conjugate(inv(W),Cg)
  out.extend(conjugate(untoken(w[:i]),C))
  w[i:i+2]=[b,a]
  # Free token reductions may follow a swap; they need no 2-cell.
  w=list(red(w));i=max(0,i-1)
 V=tuple(x for x in w if abs(x)!=6)
 e=sum(1 if x==6 else -1 for x in w if abs(x)==6)
 assert tuple(w)==V+((6,)*e if e>=0 else (-6,)*(-e))
 out=tuple(out)
 assert expanded(out)==cat(untoken(tokens),inv(cat(V,power(W,e))))
 return V,e,out

# omega6=omega5*W6 in B6, and W6=W in the compact quotient.
OMEGA5_CERT=(conjugate(O5,inverse(STAR_CERT[6]))
             +braid_fill(cat(O5,STARS[6],inv(O6)))
             +(((),OMEGA,1),))
OMEGA5_CERT=reduce_sequence(OMEGA5_CERT)
assert expanded(OMEGA5_CERT)==cat(O5,W)
def omega5_power(k):
 if k>=0:g,h,C=O5,inv(W),OMEGA5_CERT
 else:g,h=inv(O5),W;C=conjugate(inv(O5),inverse(OMEGA5_CERT))
 out=[];prefix=()
 for _ in range(abs(k)):
  out.extend(conjugate(prefix,C));prefix=cat(prefix,h)
 out=tuple(out)
 assert expanded(out)==cat(power(O5,k),power(W,k))
 return out

@lru_cache(maxsize=20000)
def fill(w):
 w=red(w)
 if not w:return ()
 # Preserve the fixed open relators literally when possible.
 for j,r in enumerate(RELS):
  if w==r:return (((),j,1),)
  if w==inv(r):return (((),j,-1),)
 assert H['permutation'](6,w)==tuple(range(1,7)),('not pure',w)
 pure=comb(6,w);pure_expanded=expand(pure)
 out=list(braid_fill(cat(w,inv(pure_expanded))))
 tokens=[];prefix=()
 for i,j,sgn in pure:
  if j==6:
   out.extend(conjugate(prefix,LAST_CERT[i,sgn]))
   new=LAST_REPLACE[i,sgn]
  else:new=A(i,j) if sgn>0 else inv(A(i,j))
  tokens.extend(new);prefix=cat(prefix,untoken(new))
 assert expanded(out)==cat(w,inv(untoken(tokens)))
 V,e,C=collect_W(tokens);out.extend(C)
 k=H['link12'](5,V)
 out.extend(braid_fill(cat(V,inv(power(O5,k)))))
 out.extend(omega5_power(k))
 n=e-k
 assert n%2==0,('nontrivial remaining hyperelliptic involution',n,w)
 out.extend((((),W2,1 if n>0 else -1),)*abs(n//2))
 out=reduce_sequence(tuple(out))
 assert expanded(out)==w,('compact genus-two certificate expansion',w)
 return out

if __name__=='__main__':
 started=time.time();tests=[]
 for j,w in enumerate(RELS):
  C=fill(w);assert expanded(C)==w;tests.append({'name':'compact_'+str(j),'word':w,'certificate':C})
 for i in range(1,7):
  w=cat(STARS[i],inv(W));C=fill(w)
  tests.append({'name':'star_'+str(i),'word':w,'certificate':C})
 for k in (-3,-1,0,1,2):
  w=cat(power(O5,k),power(W,k));C=fill(w)
  tests.append({'name':'omega5_'+str(k),'word':w,'certificate':C})
 out={'relators':RELS,'star_words':STARS,'tests':tests,'elapsed_seconds':time.time()-started}
 (P/'b_genus2_fill.json').write_text(json.dumps(out,indent=2)+'\n')
 print('All',len(tests),'literal compact, star and central-power certificates passed.')
 print('Total factors:',sum(len(t['certificate']) for t in tests),'seconds:',time.time()-started)
