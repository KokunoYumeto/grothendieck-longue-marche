"""Independent integral audit of all 24 negative-twist CM certificates.

Input: two explicit integral columns from each attached certificate, with
its source hash. We do NOT trust that these columns are a basis. We check
all Manin and Hecke equations exactly, compute the rank of the independent
system over F5, and check column rank 2 over F5. These three checks prove
that the input columns span the full 5-adic solution lattice.

Rational paths are decomposed by modular-inverse Farey neighbours, not by
the continued-fraction routine of the supplied programs. No supplied
program is imported or executed. All period values, measures and Mellin
specializations are recomputed. Arithmetic interpretation is separate.
"""
import json
from pathlib import Path
from fractions import Fraction
from functools import lru_cache
from math import comb

HERE=Path(__file__).resolve().parent
INPUT=json.loads((HERE/'de_cm_input.json').read_text())
EXPECTED={
 (1,0,1):(22,3),(1,0,6):(19,6),(1,1,1):(0,5),(1,1,6):(0,5),(1,2,1):(19,6),(1,2,6):(24,1),
 (2,0,1):(9,9),(2,0,6):(9,9),(2,1,1):(6,19),(2,1,6):(6,19),(2,2,1):(7,7),(2,2,6):(7,7),
 (3,0,1):(20,15),(3,0,6):(4,18),(3,1,1):(16,0),(3,1,6):(7,0),
 (4,0,1):(5,0),(4,0,6):(5,0),(4,1,1):(0,20),(4,1,6):(0,20),
 (5,0,1):(6,3),(5,0,6):(12,6),(6,0,1):(12,12),(6,0,6):(12,12)}

def mm(g,h):
 a,b,c,d=g;A,B,C,D=h
 return (a*A+b*C,a*B+b*D,c*A+d*C,c*B+d*D)
def adj(g):a,b,c,d=g;return (d,-b,-c,a)
def rational(a,b):return None if b==0 else Fraction(a,b)
def rankmod(rows,p):
 pivots={}
 for row in rows:
  row=[int(t)%p for t in row]
  for j,b in pivots.items():
   if row[j]:
    a=row[j];row=[(x-a*y)%p for x,y in zip(row,b)]
  j=next((j for j,t in enumerate(row) if t),None)
  if j is not None:
   a=pow(row[j],-1,p);pivots[j]=[a*t%p for t in row]
 return len(pivots)

def run(m):
 inp=INPUT[str(m)];w=m-1;N=inp['level'];a5=inp['a5']
 reps=[(1,d) for d in range(N)]+[(c,1) for c in range(0,N,2)]
 assert reps==[tuple(x) for x in inp['Manin_generators']]
 index={v:i for i,v in enumerate(reps)};D=len(reps)*(w+1)
 phi=inp['integral_period_dual_basis_columns'];assert len(phi)==D
 eps=lambda u:1 if w%2==0 or u%4==1 else -1
 @lru_cache(None)
 def substitute(poly,g):
  a,b,c,d=g;ans=[0]*(w+1)
  for i,z in enumerate(poly):
   for h in range(w-i+1):
    for k in range(i+1):
     ans[h+k]+=z*comb(w-i,h)*a**(w-i-h)*b**h*comb(i,k)*c**(i-k)*d**k
  return tuple(ans)
 def mono(i):return tuple(int(j==i) for j in range(w+1))
 def manin(poly,c,d):
  c%=N;d%=N
  if c%2:
   scale=c;pair=(1,d*pow(c,-1,N)%N)
  else:
   assert d%2;scale=d;pair=(c*pow(d,-1,N)%N,1)
  out=[0]*D;offset=index[pair]*(w+1)
  for i,t in enumerate(poly):out[offset+i]=eps(scale)*t
  return out
 @lru_cache(None)
 def path(poly,r):
  out=[0]*D
  while r is not None:
   n,d=r.numerator,r.denominator
   if d==1:
    g=(1,n,0,1);r=None
   else:
    b=pow(n,-1,d);a=(n*b-1)//d
    assert n*b-a*d==1 and 0<b<d
    g=(-a,n,-b,d);r=Fraction(a,b)
   term=manin(substitute(poly,g),g[2],g[3])
   out=[a+b for a,b in zip(out,term)]
  return tuple(out)
 def val(poly,r):
  v=path(tuple(poly),r)
  return [sum(x*p[j] for x,p in zip(v,phi)) for j in range(2)]
 def check(row):assert all(sum(x*p[j] for x,p in zip(row,phi))==0 for j in range(2))
 rows=[];S=(0,-1,1,0);R=(0,-1,1,-1);R2=mm(R,R)
 for c,d in reps:
  for i in range(w+1):
   poly=mono(i);a=manin(poly,c,d)
   def translated(h):
    return manin(substitute(poly,h),c*h[0]+d*h[2],c*h[1]+d*h[3])
   b=translated(S);row=[x+y for x,y in zip(a,b)];check(row);rows.append(row)
   b=translated(R);e=translated(R2);row=[x+y+z for x,y,z in zip(a,b,e)];check(row);rows.append(row)
 relation_rank=rankmod(rows,5)
 for ell in (3,5):
  matrices=[((1,t,0,ell),1) for t in range(ell)]+[((ell,0,0,1),eps(ell))]
  for ri,(c,d) in enumerate(reps):
   g=(0,-1,1,d) if c==1 else (1,0,c,1)
   for i in range(w+1):
    original=substitute(mono(i),adj(g));row=[0]*D
    for h,e in matrices:
     hg=mm(h,g);poly=substitute(original,adj(h))
     left=path(poly,rational(hg[1],hg[3]));right=path(poly,rational(hg[0],hg[2]))
     row=[x+e*(y-z) for x,y,z in zip(row,left,right)]
    if ell==5:row[ri*(w+1)+i]-=a5
    check(row);rows.append(row)
 eqrank=rankmod(rows,5);phirank=rankmod(list(zip(*phi)),5)
 assert eqrank==D-2 and phirank==2
 # Reflection z -> -conjugate(z), including polynomial coefficient action.
 reflected=[]
 for c,d in reps:
  g=(0,-1,1,d) if c==1 else (1,0,c,1)
  for i in range(w+1):
   pol=substitute(substitute(mono(i),adj(g)),(-1,0,0,1))
   left=val(pol,rational(-g[1],g[3]));right=val(pol,rational(-g[0],g[2]))
   reflected.append([a-b for a,b in zip(left,right)])
 minor=next((i,j) for i in range(D) for j in range(i+1,D)
            if (phi[i][0]*phi[j][1]-phi[i][1]*phi[j][0])%5)
 i,j=minor;aa,bb=phi[i];cc,dd=phi[j];det=aa*dd-bb*cc
 C=[[Fraction(dd*reflected[i][k]-bb*reflected[j][k],det) for k in range(2)],
    [Fraction(-cc*reflected[i][k]+aa*reflected[j][k],det) for k in range(2)]]
 assert all(sum(phi[r][h]*C[h][k] for h in range(2))==reflected[r][k]
            for r in range(D) for k in range(2))
 assert all(sum(C[i][h]*C[h][j] for h in range(2))==int(i==j) for i in range(2) for j in range(2))
 assert C[0][0]+C[1][1]==0
 C25=[[int(v.numerator)*pow(int(v.denominator),-1,25)%25 for v in row] for row in C]
 def linear(a,b):return tuple(comb(w,i)*a**(w-i)*b**i for i in range(w+1))
 # Primitive quadratic character of conductor 24, verified directly from
 # (24/v)=(3/v)*(8/v) for odd v prime to 3.
 chi={1:1,5:1,7:-1,11:-1,13:-1,17:-1,19:1,23:1}
 @lru_cache(None)
 def I(d,n,a):
  q=5**n
  if d==1 or m%2==0:return tuple(val(linear(q,-a),Fraction(a,q)))
  out=[0,0]
  for v,e in chi.items():
   z=val(linear(24*q,-24*a-q*v),Fraction(a,q)+Fraction(v,24))
   out=[x+e*y for x,y in zip(out,z)]
  return tuple(out)
 alpha=next(a for a in range(25) if a%5 and (a*a-a5*a+5**m)%25==0)
 cert=[]
 for d in (1,6):
  for a in range(1,5):
   assert all(sum(I(d,2,a+5*b)[i] for b in range(5))==a5*I(d,1,a)[i]-5**w*I(d,0,a)[i] for i in range(2))
  masses={a:tuple((pow(alpha,-2,25)*I(d,2,a)[i]-5**w*pow(alpha,-3,25)*I(d,1,a%5)[i])%25 for i in range(2)) for a in range(1,25) if a%5}
  for t in range((6-m)//2+1):
   j=tuple(sum(pow(a,-m-t,25)*mass[i] for a,mass in masses.items())%25 for i in range(2))
   assert j==EXPECTED[m,t,d],(m,t,d,j,EXPECTED[m,t,d])
   assert any(j)
   parity=(-1)**(t+1)
   assert all((sum(j[h]*C25[h][k] for h in range(2))-parity*j[k])%25==0 for k in range(2))
   cert.append({'m':m,'t':t,'d':d,'value_mod25':j,'valuation':0 if any(x%5 for x in j) else 1})
 result={'m':m,'dimension':D,'relations_rank_mod5':relation_rank,'equations_rank_mod5':eqrank,
  'basis_rank_mod5':phirank,'conjugation_matrix':[[str(v) for v in row] for row in C],
  'all_moments_in_expected_parity':True,'all_equations_checked_over_Z':True,'full_Z5_solution_lattice':True,
  'a5':a5,'unit_root_mod25':alpha,'distribution_checked_at_mod25':True,
  'certificates':cert,'input_sha256':inp['source_sha256']}
 print(json.dumps(result),flush=True)
 return result

if __name__=='__main__':
 results=[run(m) for m in range(1,7)]
 out={'method':'independent Farey-neighbour path reduction, integral equation audit and F5 rank proof',
  'number_of_certificates':sum(len(r['certificates']) for r in results),'results':results,
  'scope':'finite exact modular-symbol certificates; the Kato/Rubin Selmer comparison is separate'}
 assert out['number_of_certificates']==24
 (HERE/'de_cm_audit.json').write_text(json.dumps(out,indent=2)+'\n')
 print('PASS: 24 certificates, all nonzero modulo 25.')
