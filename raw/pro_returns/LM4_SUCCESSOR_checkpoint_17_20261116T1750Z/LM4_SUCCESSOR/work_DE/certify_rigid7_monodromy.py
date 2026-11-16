"""Exact seven-point braid monodromy certificate over Q(i).

The three polygonal paths and expected braid words are specified by exact
rational data. Every crossing is enumerated by exact real
root isolation of a rational polynomial; signs and ordering are exact.
No floating point arithmetic enters the certification or Artin identity.
"""
from pathlib import Path
import json,itertools,time
import sympy as s
HERE=Path(__file__).resolve().parent
u,t=s.symbols('u t',real=True)
I=s.I
pts=[u,-u,1/u,(u+I)/(u-I),-1/u,-(u+I)/(u-I),(u-I)/(u+I),-(u-I)/(u+I),(u+1)/(-I*u+I),(u+1)/(I*u-I),(u-1)/(I*u+I),(u-1)/(-I*u-I)]
S=[1,3,5,0,2,8,11]
fun=[s.cancel((pts[k]-pts[S[1]])/(pts[k]-pts[S[0]])*(pts[S[2]]-pts[S[0]])/(pts[S[2]]-pts[S[1]])) for k in S[1:]]
rotation=1+s.Rational(317,1000)*I
exceptional=u*(u**4-1)*(u**8+14*u**4+1)


def red(w):
 a=[]
 for b in w:
  if a and a[-1]==-b:a.pop()
  else:a.append(b)
 return tuple(a)
def inv(w):return tuple(-b for b in w[::-1])
def mul(*ws):return red(itertools.chain.from_iterable(ws))
def act(w):
 a=[(j+1,) for j in range(6)]
 for b in w:
  k=abs(b)-1;v,w=a[k:k+2]
  a[k:k+2]=[mul(v,w,inv(v)),v] if b>0 else [w,mul(inv(w),v,w)]
 return a

def poly(e):return s.Poly(e,t,domain=s.QQ)
def primitive(p):return p.clear_denoms()[1].primitive()[1]
def parts(e):
 e=s.expand(e)
 return poly(s.re(e).expand()),poly(s.im(e).expand())
def roots_in(p,a=0,b=1):
 if p.is_zero:raise AssertionError('identically zero polynomial')
 if p.degree()<=0:return 0
 return int(p.count_roots(a,b))
def nonzero_complex(e):
 re,im=parts(e);g=s.gcd(re,im)
 assert roots_in(g)==0,('complex zero on path',g)
def encode(p):return [str(x) for x in p.all_coeffs()]
def point_json(z):return [str(s.re(z)),str(s.im(z))]
def sgn(x):return 1 if x>0 else (-1 if x<0 else 0)

certificate={'description':__doc__,'labels':[i+1 for i in S],
             'normalization_labels':[2,4,6],
             'rotation':['1','317/1000'],
             'finite_functions':[str(f) for f in fun], 'loops':[]}
EXPECTED = {5: [-2, -4, -1, -2, -3, -2, -1, -2, -3, -2, 5, 2, 4, 5, 4, 3, 2, 5, 4, 3, 2, 1, -3, -2, 1, 2, 3, 4, 3, 3, -4, -3, -2, -1, 2, 3, -1, -2, -3, -4, -5, -2, -3, -4, -5, -4, -2, -5, 2, 3, 2, 1, 2, 3, 2, 1, 4, 2], 6: [-2, -4, -1, -2, -3, -1, -2, -1, -3, 5, 4, 5, 4, -1, -2, -3, -4, -5, 4, 3, 4, -5, -4, -3, -2, -1, -5, 3, 1, 2, 1, 3, 2, 1, 4, 2], 11: [-2, -1, -4, -2, -1, 4, 3, 3, -4, 1, 2, 4, 1, 2]}
EPS=s.Rational(1,10**22)
cache={}

def segment(a,b):
 key=(a,b)
 if key in cache:return cache[key]
 path=a+(b-a)*t
 nonzero_complex(exceptional.subs(u,path))
 values=[]
 for f in fun:
  n,d=s.fraction(s.cancel(f.subs(u,path)))
  nonzero_complex(d)
  values.append((n,d))
 events=[];records=[];sign0={};sign1={}
 for i,j in itertools.combinations(range(6),2):
  ni,di=values[i];nj,dj=values[j]
  numer=s.expand(rotation*(ni*dj-nj*di));denom=s.expand(di*dj)
  nr,ni=parts(numer);dr,di=parts(denom)
  # Denominator is |denom|^2 >0, so these numerators determine both signs.
  real=primitive(nr*dr+ni*di);imag=primitive(ni*dr-nr*di)
  # primitive() preserves the sign of content, which is positive over QQ.
  assert not real.is_zero
  assert roots_in(s.gcd(nr,ni))==0,('collision',i,j)
  assert real.eval(0)!=0 and real.eval(1)!=0,('endpoint crossing',i,j)
  sign0[i,j]=sgn(real.eval(0));sign1[i,j]=sgn(real.eval(1))
  rec={'pair':[i,j],'real_coefficients':encode(real),'imag_coefficients':encode(imag),'crossings':[]}
  intervals=real.intervals(eps=EPS,inf=0,sup=1)
  for interval,multiplicity in intervals:
   lo,hi=interval
   assert multiplicity==1,('nongeneric crossing',i,j,interval,multiplicity)
   assert 0<lo<=hi<1
   mid=(lo+hi)/2
   assert roots_in(imag,lo,hi)==0 and roots_in(real.diff(),lo,hi)==0
   sr=sgn(real.diff().eval(mid));si=sgn(imag.eval(mid));assert sr*si!=0
   braid_sign=1 if sr*si<0 else -1
   events.append((lo,hi,i,j,braid_sign))
   rec['crossings'].append({'interval':[str(lo),str(hi)],'derivative_sign':sr,'imaginary_sign':si,'braid_sign':braid_sign})
  records.append(rec)
 def less(i,j,signs):return signs[i,j]<0 if i<j else signs[j,i]>0
 def order(signs):
  return sorted(range(6),key=lambda i:sum(less(j,i,signs) for j in range(6) if j!=i))
 at=order(sign0);expected=order(sign1)
 events.sort(key=lambda z:z[0]);word=[]
 for n,event in enumerate(events):
  lo,hi,i,j,bs=event
  if n:assert events[n-1][1]<lo,('simultaneous/unseparated crossings',events[n-1],event)
  ii,jj=at.index(i),at.index(j);assert abs(ii-jj)==1,('nonadjacent',event,at)
  word.append(bs*(min(ii,jj)+1));at[ii],at[jj]=at[jj],at[ii]
 assert at==expected
 record={'start':point_json(a),'end':point_json(b),'word':word,'crossing_count':len(events),'polynomials':records}
 cache[key]=(word,record)
 return word,record

start=time.time()
base=s.Rational(371,100)+I*s.Rational(237,100)
epsilon=s.Rational(3,250)
centres={5:s.Integer(-1),6:s.Rational(36603,100000)*(1+I),11:s.Integer(1)}
for idx,c in centres.items():
 path=[base,c+epsilon*(1+I),c+epsilon*(-1+I),c-epsilon*(1+I),c+epsilon*(1-I),c+epsilon*(1+I),base]
 words=[];segs=[]
 for k,(a,b) in enumerate(zip(path,path[1:])):
  w,record=segment(a,b);words+=w;segs.append(record)
  print('loop',idx,'segment',k+1,'exact crossings',len(w),'elapsed',round(time.time()-start,2),flush=True)
 w=red(words)
 assert w==tuple(EXPECTED[idx]),('discovered word mismatch',idx,w,EXPECTED[idx])
 certificate['loops'].append({'source_index':idx,'path':[point_json(z) for z in path],'braid_word':w,'segments':segs})
 print('PASS exact monodromy for loop',idx,'braid length',len(w),flush=True)
byid={z['source_index']:z['braid_word'] for z in certificate['loops']}
relation=mul(byid[6],byid[11],inv(byid[6]),inv(byid[5]))
assert act(relation)==[(j+1,) for j in range(6)]
certificate['parameter_word']=[6,11,-6,-5]
certificate['relation_braid_word']=relation
certificate['artin_images']=act(relation)
(HERE/'rigid7_exact_certificate.json').write_text(json.dumps(certificate,indent=2)+'\n')
print('PASS exact Artin action: e6 e11 e6^-1 e5^-1 maps to identity in B6')
print('Parameter homology: [e11]-[e5], nonzero (distinct meridians at +1 and -1)')
print('ALL EXACT CHECKS PASS; elapsed',round(time.time()-start,2),'seconds')
