#!/usr/bin/env python3
"""Exact six-strand inner bad-region braids, with a distinguished order-two cone.

The rational trajectories are 0,q,h_u(q)^2, h_u=1/T_u.  Nine filled
critical values carry six ordinary pair nodes and four cone contacts;
the q=0 lasso is retained.  Chronological push is art(reverse(word));
back transport is art(negate_each(word)).  No global gluing is inferred.
"""
from pathlib import Path
import sys,itertools,json,time,hashlib
ROOT=Path(__file__).resolve().parents[2]
DE=ROOT/'work_DE/next_marginal_source';sys.path.insert(0,str(DE))
import sympy as S
from quadratic_pencil_braid import (F,I,Q,X,ROT,u,EPS,frac,sy,red,
    ppoly,parts,pval,roots,lower_norm,ppoly_from_record,Segment as CoreSegment)
OUT=ROOT/'work_CE/next_symmetric_nodes'
N=6

def mul(*ws):return tuple(red(x for w in ws for x in w))
def inv(w):return tuple(-x for x in reversed(w))
def sub(w,A):return mul(*(A[x] if x>0 else inv(A[-x]) for x in w))
def art(w):
 A={i:(i,) for i in range(1,N+1)}
 for x in w:
  j=abs(x);a,b=A[j],A[j+1]
  A[j],A[j+1]=(mul(a,b,inv(a)),a) if x>0 else (b,mul(inv(b),a,b))
 return A
def push(w):return art(tuple(reversed(w)))
def back(w):return art(tuple(-x for x in w))
def comm(a,b):return mul(a,b,inv(a),inv(b))
def peel(w):
 a=list(w);c=[]
 while len(a)>1 and a[0]==-a[-1]:c.append(a.pop(0));a.pop()
 assert len(a)==1 and a[0]>0,('not positive peripheral',w)
 return tuple(c),a[0]
def l1(z):return abs(S.re(z))+abs(S.im(z))
def d2(c,a,b):
 d=b-a;dd=S.re(d)**2+S.im(d)**2;assert dd>0
 z=c-a;t=(S.re(z)*S.re(d)+S.im(z)*S.im(d))/dd
 t=max(S.Integer(0),min(S.Integer(1),t));z=z-t*d
 return S.cancel(S.re(z)**2+S.im(z)**2)
def rounded(z):
 z=S.cancel(z)
 return Q(S.floor(S.re(z)*10**6),10**6)+I*Q(S.floor(S.im(z)*10**6),10**6)
def square(c,h,base):
 cs=[c+h+I*h,c-h+I*h,c-h-I*h,c+h-I*h]
 j=min(range(4),key=lambda k:S.re(cs[k]-base)**2+S.im(cs[k]-base)**2)
 return [cs[(j+k)%4] for k in range(5)]

class Segment(CoreSegment):
 def __init__(self,a,b):
  self.a,self.b=a,b;q=S.expand(a+(b-a)*X)
  self.rational=[];self.records=[];self.candidates=[]
  assert S.re(a)**2+S.im(a)**2<Q(9,10) and S.re(b)**2+S.im(b)**2<Q(9,10)
  nd=[(S.Integer(0),S.Integer(1)),(q,S.Integer(1))]
  nd += [(S.expand((v*v+(1-2*v)*q)**2),S.expand((q+v*v-2*v)**2)) for v in u[1:]]
  self.derivative_bound=F(10**8)
  for num,den in nd:
   num=S.expand(ROT*num);dr,di=parts(den);lower_norm(dr,di,F(1,4))
   nr,ni=parts(num)
   nn=sum(abs(frac(c)) for p in (nr,ni) for c in p.all_coeffs())
   ndp=sum(abs(frac(c)) for p in (nr.diff(),ni.diff()) for c in p.all_coeffs())
   ddp=sum(abs(frac(c)) for p in (dr.diff(),di.diff()) for c in p.all_coeffs())
   assert 4*ndp+16*nn*ddp<self.derivative_bound
   R,J=parts(S.expand(num*S.conjugate(den)))
   D=ppoly(S.expand(den*S.conjugate(den)))
   self.rational.append((R,J,D))
 def point(self,i,x):
  R,J,D=self.rational[i];d=pval(D,x);assert d>0
  a,b=pval(R,x)/d,pval(J,x)/d
  return (a,a),(b,b)
 def order(self,x):
  a=[self.point(i,x)[0] for i in range(N)];o=sorted(range(N),key=lambda i:a[i][0])
  for i,j in zip(o,o[1:]):assert a[i][1]<a[j][0],('projection tie',x,i,j)
  return o
 def compute(self):
  for i,j in itertools.combinations(range(N),2):
   R,_,D=self.rational[i];T,_,E=self.rational[j]
   self.addpoly('rational',[i,j],R*E-T*D)
  self.candidates.sort(key=lambda e:e['lo']);groups=[]
  for e in self.candidates:
   if groups and e['lo']<=groups[-1]['hi']:
    groups[-1]['hi']=max(groups[-1]['hi'],e['hi']);groups[-1]['events'].append(e)
   else:groups.append({'lo':e['lo'],'hi':e['hi'],'events':[e]})
  for g in groups:
   for e,f in itertools.combinations(g['events'],2):
    assert e['record']!=f['record']
    p=ppoly_from_record(self.records[e['record']]);q=ppoly_from_record(self.records[f['record']])
    gg=S.gcd(p,q);assert gg.degree()>0 and gg.count_roots(sy(g['lo']),sy(g['hi']))>0
  initial=self.order(F(0));at=list(initial);word=[];events=[]
  for gi,g in enumerate(groups):
   left=F(0) if gi==0 else groups[gi-1]['hi'];right=F(1) if gi+1==len(groups) else groups[gi+1]['lo']
   ob=self.order((left+g['lo'])/2);oa=self.order((g['hi']+right)/2);assert at==ob
   pos={a:i for i,a in enumerate(oa)}
   pairs=[(a,b) for j,a in enumerate(ob) for b in ob[j+1:] if pos[a]>pos[b]]
   if not pairs:continue
   sample=g['lo']-max(g['hi']-g['lo'],frac(EPS));assert left<sample<g['lo']
   rad=self.derivative_bound*(g['hi']-sample);clusters=[]
   for a,b in pairs:
    touching=[c for c in clusters if a in c or b in c];merged={a,b}
    for c in touching:merged.update(c);clusters.remove(c)
    clusters.append(merged)
   for c in clusters:
    for a,b in itertools.combinations(sorted(c),2):
     ai=self.point(a,sample)[1];bi=self.point(b,sample)[1]
     gap=(ai[0]-bi[1]-2*rad,ai[1]-bi[0]+2*rad);assert gap[0]>0 or gap[1]<0
   crossings=[];remaining=len(pairs)
   while at!=oa:
    j=next(j for j in range(N-1) if pos[at[j]]>pos[at[j+1]])
    a,b=at[j],at[j+1];ai=self.point(a,sample)[1];bi=self.point(b,sample)[1]
    gap=(ai[0]-bi[1]-2*rad,ai[1]-bi[0]+2*rad);assert gap[0]>0 or gap[1]<0
    sign=-1 if gap[0]>0 else 1;letter=sign*(j+1);word.append(letter)
    at[j],at[j+1]=at[j+1],at[j];remaining-=1
    crossings.append({'physical_labels':[a,b],'generator':letter,'height_gap':[str(z) for z in gap]})
   assert remaining==0
   events.append({'interval':[str(g['lo']),str(g['hi'])],'records':[e['record'] for e in g['events']],
                  'crossings':crossings,'cluster_sizes':[len(c) for c in clusters]})
  assert at==self.order(F(1))
  return {'start':[str(S.re(self.a)),str(S.im(self.a))],'end':[str(S.re(self.b)),str(S.im(self.b))],
          'initial_order':initial,'final_order':at,'word':red(word),'crossing_count':len(word),
          'polynomials':self.records,'events':events,'denominator_norm_lower_bound':'1/4',
          'derivative_bound':'100000000','root_precision':str(EPS)}

def plan():
 base=Q(4,5)+I/2;h=Q(1,10000)
 specs=[('q0',S.Integer(0),[((0,1),2)],[])]
 pairs=[(i,j) for i in range(1,5) for j in range(i,5) if (i,j)!=(2,3)]
 for i,j in pairs:
  kind='alpha' if (i,j)==(1,4) else 'beta'
  val=u[i]+u[j]-u[i]*u[j] if kind=='alpha' else u[i]*u[j]/(u[i]+u[j]-1)
  node=[{'i':i,'j':j,'kind':kind}]
  link=[((0,i+1),4)] if i==j else [((i+1,j+1),2)]
  if (i,j)==(1,4):
   node.append({'i':2,'j':3,'kind':'beta'});link.append(((3,4),2))
  specs.append((f'{kind}_{i}{j}',S.cancel(val),link,node))
 rows=[]
 for name,v,link,nodes in specs:
  c=rounded(v);assert l1(v-c)<Q(1,10**5)
  cs=square(c,h,base);rows.append({'name':name,'center':c,'corners':cs,'link':link,'physical_nodes':nodes})
 margin=None
 for row in rows:
  pts=[base]+row['corners']
  for a,b in zip(pts,pts[1:]):
   for other in rows:
    dd=d2(other['center'],a,b);assert dd>Q(1,30000)**2,(row['name'],other['name'],dd)
    margin=dd if margin is None else min(margin,dd)
  # Straight radial lassos form a distinguished system. The small
  # corner-versus-center triangle avoids every other critical square.
  c=row['center'];corner=row['corners'][0]
  def cross(z,w):return S.re(z)*S.im(w)-S.im(z)*S.re(w)
  for other in rows:
   if other is row:continue
   p=other['center'];sg=[cross(y-x,p-x) for x,y in [(base,c),(c,corner),(corner,base)]]
   assert not(all(x>=0 for x in sg) or all(x<=0 for x in sg)),('critical in whisker triangle',row['name'],other['name'])
 for a,b in itertools.combinations(rows,2):
  z=a['center']-base;w=b['center']-base
  assert S.re(z)*S.im(w)-S.im(z)*S.re(w)!=0
 return base,rows,{'base':['4/5','1/2'],'square_halfside':str(h),
  'minimum_center_distance_squared':str(margin),'unit_parameter_norm_squared_upper_bound':'9/10',
  'centers':[{'name':r['name'],'center':[str(S.re(r['center'])),str(S.im(r['center']))],
              'physical_nodes':r['physical_nodes']} for r in rows]}

def run(indices):
 started=time.monotonic();base,planned,plan_record=plan();OUT.mkdir(exist_ok=True)
 (OUT/'inner_bad_orbifold_plan22.json').write_text(json.dumps(plan_record,indent=2)+'\n')
 cache={};loops=[];initial=None
 def segment(a,b):
  key=(a,b)
  if key not in cache:
   cache[key]=Segment(a,b).compute()
   print('SEGMENT',len(cache),'crossings',cache[key]['crossing_count'],'elapsed',round(time.monotonic()-started,3),flush=True)
  return cache[key]
 for idx in indices:
  row=planned[idx];pts=[base]+row['corners'];recs=[segment(a,b) for a,b in zip(pts,pts[1:])]
  if initial is None:initial=recs[0]['initial_order']
  assert recs[0]['initial_order']==initial
  W0=tuple(recs[0]['word']);local=mul(*(r['word'] for r in recs[1:]));beta=mul(W0,local,inv(W0))
  perm=list(initial);link={}
  for x in beta:
   j=abs(x)-1;a,b=perm[j],perm[j+1];key=tuple(sorted((a,b)))
   link[key]=link.get(key,0)+(1 if x>0 else -1);perm[j],perm[j+1]=perm[j+1],perm[j]
  assert perm==initial;link={k:v for k,v in link.items() if v}
  assert link==dict(row['link']),('linking mismatch',idx,link,row['link'])
  found=None
  for cut in range(len(local)+1):
   pre=local[:cut];rot=mul(local[cut:],pre);AA=art(rot)
   support=[i for i in AA if AA[i]!=(i,)]
   if len(support)!=2*len(link):continue
   blocks=[support[j:j+2] for j in range(0,len(support),2)]
   if any(b[1]!=b[0]+1 for b in blocks):continue
   # Each contact has exponent4; ordinary nodes exponent2.
   powers=[4 if row['name']!='q0' and len(row['physical_nodes'])==1 and row['physical_nodes'][0]['i']==row['physical_nodes'][0]['j'] else 2]*len(blocks)
   std=tuple(x for b,powr in zip(blocks,powers) for x in [b[0]]*powr)
   if AA==art(std):found=(pre,blocks,powers,std);break
  assert found,('no supported local normal form',idx,local)
  pre,blocks,powers,std=found;W=mul(W0,pre);B=back(W);P=push(W)
  for j in range(1,N+1):assert sub(B[j],P)==(j,)==sub(P[j],B)
  assert push(beta)==push(mul(W,std,inv(W)))
  nodes=[]
  for (j,k),power in zip(blocks,powers):
   a,b=B[j],B[k];ca,ga=peel(a);cb,gb=peel(b);labels=[initial[ga-1],initial[gb-1]]
   assert tuple(sorted(labels)) in link
   if power==4:
    cone,p=(a,b) if labels[0]==0 else (b,a)
    rel=comm(p,mul(cone,p,inv(cone)));kind='cone_contact'
   else:rel=comm(a,b);kind='retained_q0' if idx==0 else 'ordinary_node'
   nodes.append({'kind':kind,'local_positions':[j,k],'physical_labels':labels,
     'meridians':[a,b],'conjugators':[ca,cb],'cores':[ga,gb],'relation':rel})
  loop={'index':idx,'name':row['name'],'chronological_braid':beta,'whisker':W,'local_word':local,
    'absorbed_prefix':pre,'standard_local_braid':std,'nodes':nodes,
    'positive_push':push(beta),'negative_pull':back(beta),
    'pair_linking_twice':[{'labels':k,'value':v} for k,v in sorted(link.items())],
    'physical_nodes':row['physical_nodes'],'segments':recs}
  loops.append(loop)
  out={'status':'PARTIAL','scope':__doc__,'plan':plan_record,'initial_physical_order':initial,
    'cone_generator':initial.index(0)+1,'retained_branch_generator':initial.index(1)+1,
    'physical_labels':['cone0','branch_q','deleted1','deleted2','deleted3','deleted4'],
    'loops':loops,'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'elapsed_seconds':round(time.monotonic()-started,6)}
  (OUT/'inner_bad_orbifold_braids22.partial.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
  print('LOOP',idx,row['name'],'PASS','length',len(beta),'relations',[len(n['relation']) for n in nodes],flush=True)
 out['status']='PASS';(OUT/'inner_bad_orbifold_braids22.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
 compact={k:v for k,v in out.items() if k!='loops'}
 compact['loops']=[{k:v for k,v in r.items() if k!='segments'} for r in loops]
 (OUT/'inner_bad_orbifold_words22.json').write_text(json.dumps(compact,indent=2)+'\n')
 print('PASS',len(loops),'based lassos',len(cache),'exact segments',out['elapsed_seconds'],'seconds',flush=True)

if __name__=='__main__':
 import argparse
 ap=argparse.ArgumentParser();ap.add_argument('--indices',default='0,1,2,3,4,5,6,7,8,9')
 run([int(x) for x in ap.parse_args().indices.split(',')])
