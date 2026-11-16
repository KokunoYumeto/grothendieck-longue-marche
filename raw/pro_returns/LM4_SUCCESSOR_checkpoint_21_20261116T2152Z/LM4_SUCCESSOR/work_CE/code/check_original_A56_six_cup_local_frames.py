"""Exhaust all local free right-frame values for the ORIGINAL A56 action.

This is a necessary local gate. Global old-center/frame equations remain
separate. The polynomial is independently checked in the exact six-cup law.
"""
from pathlib import Path
import itertools,json,random
HERE=Path(__file__).resolve().parent
M=json.loads((HERE.parent/'next_cup_cocycle_matrices.json').read_text())
A=json.loads((HERE.parent/'Q6_integral_affine_data.json').read_text())
CC=json.loads((HERE.parent/'A63_cross_cup_independent_square.json').read_text())
def mul(a,b):
 out=0
 while b:
  if b&1:out^=a
  b>>=1;a<<=1
  if a&8:a^=11
 return out
def pw(a,n):
 out=1
 for _ in range(n):out=mul(out,a)
 return out
def add(a,b):return tuple(x^y for x,y in zip(a,b))
def va(a,b):return tuple(add(x,y)for x,y in zip(a,b))
def apply(cs,v):
 out=[0]*36
 for a,col in zip(v,cs):
  if a:
   for i,b in enumerate(col):out[i]^=mul(a,b)
 return tuple(out)
def rows(cs,aa):return tuple(apply(cs,v)for v in aa)
def red(a):return(a&1)|(((a>>2)&1)<<1)|(((a>>4)&1)<<2)
def redrows(aa):return tuple(tuple(red(x)for x in row)for row in aa)
B=[tuple(pw(x,4)for x in col)for col in M['BETA2']]
C=[tuple(pw(x,4)for x in col)for col in M['C2']]
S=[tuple(pw(x,4)for x in col)for col in M['S2']]
B2=[tuple(col)for col in M['BETA2']]
C2=[tuple(col)for col in M['C2']]
wc=redrows(A['new_c_inner_free_O'])
ww=redrows(A['positive_inner_free_O'])
q=redrows(A['negative_inner_free_O'])
p=redrows(A['s_frame_free_O'])
assert va(wc,ww)==q
assert p==tuple(tuple(row)for row in A['literal_old_s_frame_after_change_mod2'][:4])
aeff=rows(B,va(q,p))
pairs=[(i,j)for i in range(4)for j in range(i+1,4)]
CO=CC['canonical_c_corrections'];PO=CC['positive_corrections']
assert all(not any(row[4:8])for row in CO+PO)
L=[add(c[:4],d[:4])for c,d in zip(CO,PO)]
v=tuple(add(c[8:],d[8:])for c,d in zip(CO,PO))
zero=(0,)*36;AZ=(zero,)*4;TZ=(zero,)*6
def cup(a,b):return tuple(tuple(mul(x,y)for x,y in zip(a[i],b[j]))for i,j in pairs)
def gm(g,h):
 a,z,e=g;b,t,f=h
 if e:b,t=rows(B,b),rows(B2,t)
 return(va(a,b),va(va(z,t),cup(a,b)),e^f)
ONE=(AZ,TZ,0)
def gi(g):
 a,z,e=g;out=(a,va(z,cup(a,a)),e)
 if e:out=(rows(B,out[0]),rows(B2,out[1]),e)
 assert gm(g,out)==gm(out,g)==ONE
 return out
def inner(g,h):return gm(gm(g,h),gi(g))
def lin_cup(aa):
 out=[]
 for row in L:
  z=[0]*36
  for c,a in zip(row,aa):
   for i,x in enumerate(a):z[i]^=mul(c,mul(x,x))
  out.append(tuple(z))
 return tuple(out)
def neg(g):
 a,z,e=g
 # c first, then positive h. Both source cochain corrections are evaluated
 # at c(g); their binary-s coefficients are exactly zero.
 cg=inner((wc,TZ,0),(rows(C,a),rows(C2,z),e))
 out=inner((ww,TZ,0),cg)
 cor=lin_cup(cg[0])
 if e:cor=va(cor,va(v,rows(B2,v)))
 return(out[0],va(out[1],cor),e)
beta=(p,TZ,1)
baseline=gm(gi(beta),neg(gi(beta)))
assert baseline[0]==AZ and baseline[2]==0
sp=[next(i for i,x in enumerate(col)if x)for col in S]
weights=(8,11,20,23)
for w in weights:
 assert tuple(row[w]for row in baseline[1])==tuple(row[w]for row in CC['s_initial_square'])
print('Actual canonical/positive cochains and original baseline agree at all four Tate coordinates: PASS',flush=True)

def vv(w,u):
 aa=[[0]*36 for _ in range(4)]
 for i,x in enumerate(u):
  aa[i][w]=x;aa[i][sp[w]]=mul(S[w][sp[w]],x)
 aa=tuple(map(tuple,aa))
 assert rows(S,aa)==aa and rows(B,rows(C,aa))==aa
 return aa
def values(w,u):
 out=[]
 for k,(i,j)in enumerate(pairs):
  t=baseline[1][k][w]^mul(u[i],u[j])^mul(aeff[i][w],u[j])^mul(u[i],aeff[j][w])
  for c,x in zip(L[k],u):t^=mul(c,mul(x,x))
  out.append(t)
 return tuple(out)
def direct(w,u):
 beta2=gm(beta,(vv(w,u),TZ,0))
 z=gm(gi(beta2),neg(gi(beta2)))
 assert z[0]==AZ and z[2]==0
 return tuple(row[w]for row in z[1])
records=[];rng=random.Random(15663)
for w in weights:
 # Check basis, every binary quadratic cross term, and independent samples
 # against original multiplication, not only against interpolation.
 bs=[tuple((1<<b)if i==j else 0 for i in range(4))for j in range(4)for b in range(3)]
 tests=[(0,)*4]+bs+[add(x,y)for i,x in enumerate(bs)for y in bs[i+1:]]
 tests += [tuple(rng.randrange(8)for _ in range(4))for _ in range(25)]
 for u in tests:assert direct(w,u)==values(w,u)
 allowed=[u for u in itertools.product(range(8),repeat=4)if not any(values(w,u))]
 for u in allowed:assert not any(direct(w,u))
 print('Weight',w,'S mate',sp[w],'allowed',len(allowed),'of4096; original-law checks',len(tests)+len(allowed),flush=True)
 records.append(dict(weight=w,S_mate=sp[w],baseline=[row[w]for row in baseline[1]],
                     affine_effective=[row[w]for row in aeff],allowed_right_free_values=allowed,
                     exhaustive_count=4096,direct_law_checks=len(tests)+len(allowed)))
out=dict(scope='Necessary local six-cup frame equations for fixed ORIGINAL A56 positive action; no global-frame existence conclusion',
         convention='beta_new=beta*Q; values are normalized free cusp coordinates of Q itself, relative to the original beta',
         field='F2[zeta]/(zeta^3+zeta+1), binary encoding0..7',
         formula='Kij+ui*uj+aeff_i*uj+ui*aeff_j+sum_r Lijr*ur^2',
         L=L,records=records,all_checks='PASS')
(HERE.parent/'original_A56_six_cup_local_frames.json').write_text(json.dumps(out,indent=2)+'\n')
print('All four local complete enumerations: PASS',flush=True)
