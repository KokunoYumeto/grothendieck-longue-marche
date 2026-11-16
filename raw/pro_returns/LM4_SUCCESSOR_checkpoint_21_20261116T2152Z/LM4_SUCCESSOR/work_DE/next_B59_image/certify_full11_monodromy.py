"""Exact twelve-point braid monodromy certificate over Q(i).

The thirteen polygonal free-basis meridians are specified by exact
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
S=[1,3,5]+[j for j in range(12) if j not in (1,3,5)]
N_STRANDS=11
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
 a=[(j+1,) for j in range(N_STRANDS)]
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
EXPECTED = {}
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
 for i,j in itertools.combinations(range(N_STRANDS),2):
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
  return sorted(range(N_STRANDS),key=lambda i:sum(less(j,i,signs) for j in range(N_STRANDS) if j!=i))
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
approx_a=s.Rational(36603,100000)
approx_b=1+approx_a
raw_centres=[('0',s.Integer(0)),('1',s.Integer(1)),('-1',s.Integer(-1)),
             ('i',I),('-i',-I)]
for name,c in [('a',approx_a),('b',approx_b)]:
 for sx,sy in itertools.product([-1,1],repeat=2):
  raw_centres.append((f'{sx}{name}+{sy}{name}i',sx*c+I*sy*c))
def xy(z):return s.re(z),s.im(z)
def slope(z):
 x,y=xy(z+epsilon*(1+I)-base)
 assert x<0 and y<0
 return y/x
centres=sorted(raw_centres,key=lambda item:slope(item[1]))
assert len(centres)==13 and len({slope(c) for name,c in centres})==13
assert centres[4][1]==-1 and centres[5][1]==approx_a*(1+I) and centres[10][1]==1

# Exact rectangular-intersection certificate for the embedded meridian tree.
def box(c):
 x,y=xy(c);return (x-epsilon,x+epsilon,y-epsilon,y+epsilon)
def box_hit(a,b,rect):
 lo=s.Integer(0);hi=s.Integer(1)
 for v,d,mn,mx in [(s.re(a),s.re(b-a),rect[0],rect[1]),(s.im(a),s.im(b-a),rect[2],rect[3])]:
  if d==0:
   if not mn<=v<=mx:return None
  else:
   aa=(mn-v)/d;bb=(mx-v)/d
   if aa>bb:aa,bb=bb,aa
   lo=max(lo,aa);hi=min(hi,bb)
   if lo>hi:return None
 return (lo,hi)
rects=[box(c) for name,c in centres]
for i,((name,c),rect) in enumerate(zip(centres,rects)):
 corner=c+epsilon*(1+I)
 assert box_hit(base,corner,rect)==(1,1)
 for j,rect2 in enumerate(rects):
  if i!=j:assert box_hit(base,corner,rect2) is None,('stem hits other petal',i+1,j+1)
 for j in range(i):
  q=rects[j]
  assert rect[1]<q[0] or q[1]<rect[0] or rect[3]<q[2] or q[3]<rect[2]
# sqrt(3) is bracketed by consecutive exact rationals; each irrational
# exceptional point is strictly inside the corresponding rational square.
root_lo=s.Rational(17320508075688772,10**16)
root_hi=s.Rational(17320508075688773,10**16)
assert root_lo**2<3<root_hi**2
for c,lo,hi in [(approx_a,(root_lo-1)/2,(root_hi-1)/2),(approx_b,(root_lo+1)/2,(root_hi+1)/2)]:
 assert c-epsilon<lo<hi<c+epsilon
certificate['basis_geometry']={'base':point_json(base),'epsilon':str(epsilon),
  'sqrt3_interval':[str(root_lo),str(root_hi)],
  'centres':[{'index':i+1,'name':name,'centre':point_json(c),'slope':str(slope(c)),'box':[str(v) for v in box(c)]} for i,(name,c) in enumerate(centres)],
  'checks':'thirteen pairwise disjoint squares; distinct fan slopes; each stem meets its own square only at its NE corner and misses every other square; each square contains its named exceptional point'}
print('PASS exact meridian-tree geometry:13 disjoint petals and noncrossing stems',flush=True)
print('PASS exceptional square contents from rational sqrt(3) brackets; infinity omitted',flush=True)
for i,(name,c) in enumerate(centres,1):print('basis',i,name,point_json(c),flush=True)


for idx,(name,c) in enumerate(centres,1):
 path=[base,c+epsilon*(1+I),c+epsilon*(-1+I),c-epsilon*(1+I),c+epsilon*(1-I),c+epsilon*(1+I),base]
 words=[];segs=[]
 for k,(a,b) in enumerate(zip(path,path[1:])):
  w,record=segment(a,b);words+=w;segs.append(record)
  print('loop',idx,'segment',k+1,'exact crossings',len(w),'elapsed',round(time.time()-start,2),flush=True)
 w=red(words)
 if idx in EXPECTED:assert w==tuple(EXPECTED[idx]),('earlier3-word consistency',idx,w)
 # Every labelled path is closed, so the resulting permutation is identity.
 perm=list(range(N_STRANDS))
 for j in w:
  k=abs(j)-1;perm[k],perm[k+1]=perm[k+1],perm[k]
 assert perm==list(range(N_STRANDS))
 certificate['loops'].append({'source_index':idx,'puncture_name':name,'path':[point_json(z) for z in path],'braid_word':w,'segments':segs,'permutation':perm})
 print('PASS exact monodromy for basis',idx,'pure braid length',len(w),flush=True)
 # Certificate stays in memory until all exact checks finish.


# The old six-strand words give an independent geometric restriction check.
previous=json.loads((HERE.parent/'next_B56/all13_braid_words.json').read_text())
old={row['index']:tuple(row['word']) for row in previous['basis']}
base_values=[s.re(s.cancel(rotation*f.subs(u,base))) for f in fun]
initial_order=sorted(range(N_STRANDS),key=lambda i:base_values[i])
initial_labels=[S[i+1]+1 for i in initial_order]
assert len(set(base_values))==N_STRANDS
keep=set(previous['finite_labels'])
def project(word):
 labels=initial_labels[:];out=[]
 for a in word:
  k=abs(a)-1
  if labels[k] in keep and labels[k+1] in keep:
   j=sum(x in keep for x in labels[:k])
   out.append((1 if a>0 else -1)*(j+1))
  labels[k],labels[k+1]=labels[k+1],labels[k]
 assert labels==initial_labels
 return red(out)
for row in certificate['loops']:
 assert project(row['braid_word'])==old[row['source_index']],('six-strand consistency',row['source_index'])
print('PASS every full11-strand word projects to the independently certified6-strand word',flush=True)

linking=json.loads((HERE.parent/'full_pair_linking_certificate.json').read_text())
pairs=[tuple(p) for p in linking['pair_rows']];pi={p:i for i,p in enumerate(pairs)}
M=linking['full_matrix_rows_pairs_columns_basis']
for row in certificate['loops']:
 labels=initial_labels[:];counts=[0]*55
 for a in row['braid_word']:
  k=abs(a)-1;pair=tuple(sorted((labels[k],labels[k+1])))
  counts[pi[pair]]+=1 if a>0 else -1
  labels[k],labels[k+1]=labels[k+1],labels[k]
 assert labels==initial_labels and all(x%2==0 for x in counts)
 links=[x//2 for x in counts]
 assert links==[r[row['source_index']-1] for r in M],('full pair linking',row['source_index'])
 row['pair_linking']=links
certificate['initial_geometric_order_labels']=initial_labels
certificate['rigid_restriction_labels']=sorted(keep)
certificate['rigid_restriction_verified']=True
certificate['all55_pair_linkings_verified']=True
certificate['completed']=True
(HERE/'full11_exact_certificate.json').write_text(json.dumps(certificate,indent=2)+'\n')
(HERE/'full11_braid_words.json').write_text(json.dumps({'base':point_json(base),'normalization':[2,4,6],
 'finite_labels':[j+1 for j in S[1:]],'initial_order_labels':initial_labels,
 'basis':[{'index':z['source_index'],'puncture':z['puncture_name'],'word':z['braid_word']} for z in certificate['loops']]},indent=2)+'\n')
print('PASS all13 full11-strand meridian images and all55 pair-linking vectors',flush=True)
print('ALL EXACT CHECKS PASS; elapsed',round(time.time()-start,2),'seconds',flush=True)
