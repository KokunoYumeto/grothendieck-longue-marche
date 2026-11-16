"""Actual mod2->mod4 free-center frame gate for the full128 scalar cover.

Uses the existing GR(4,3) source/monomial model read-only. All outputs are
owned CE artifacts. The calculation retains W_free=0 and allows doubled
joint-fixed affine frame corrections before taking central halves.
"""
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
import runpy,json,itertools
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]
with redirect_stdout(StringIO()):
 J=runpy.run_path(str(ROOT/'work_A/check_A59_integral_center.py'),run_name='_CE_integral_review')
ADD,MUL,NEG,TEICH,red=[J[k]for k in('ADD','MUL','NEG','TEICH','red')]
fm=J['fm'];mpairs=list(itertools.combinations_with_replacement(range(4),2))
free=[i!=j for i,j in mpairs];sel=[J['zpairs'].index(v)for v in mpairs]
AZ=((0,)*36,)*4;MZ=(0,)*10;H0=J['HN0'];ONE=(AZ,MZ,H0)
HS,HR,HB=J['HS'],J['HR'],J['HB'];VP=J['vpairs']
def av(a,b):return tuple(tuple(ADD[x][y]for x,y in zip(v,w))for v,w in zip(a,b))
def an(a):return tuple(tuple(NEG[x]for x in v)for v in a)
def ma(a,b):return tuple(ADD[x][y]if f else x^y for x,y,f in zip(a,b,free))
def mn(a):return tuple(NEG[x]if f else x for x,f in zip(a,free))
def tensor(a,b):
 return tuple(ADD[MUL[a[i]][b[j]]][NEG[MUL[a[j]][b[i]]]]if i!=j
              else fm(red(a[i]),red(b[i]))for i,j in mpairs)
def at_weight(a,j):return tuple(v[j]for v in a)
def coc(a,b):
 out=MZ
 for l,r in VP:out=ma(out,tensor(at_weight(a,l),at_weight(b,r)))
 return out
def monop(mon,a,m=MZ):
 pp,ww=mon;out=[]
 for row in a:
  v=[0]*36
  for i,x in enumerate(row):v[pp[i]]=MUL[ww[i]][x]
  out.append(tuple(v))
 for l,r in VP:
  if pp[l]>pp[r]:m=ma(m,mn(tensor(at_weight(a,l),at_weight(a,r))))
 return tuple(out),m
def act(mon,a):return monop(mon,a)[0]
def gm(g,h):
 a,m,q=g;b,n,r=h;b,n=monop(J['hmon'](q),b,n)
 return av(a,b),ma(ma(m,n),coc(a,b)),J['hmul'](q,r)
def gi(g):
 a,m,h=g;hh=J['hinv'](h);b=act(J['hmon'](hh),an(a))
 _,carry=monop(J['hmon'](h),b)
 out=(b,mn(ma(ma(m,carry),coc(a,an(a)))),hh)
 assert gm(g,out)==gm(out,g)==ONE
 return out
def inner(g,h):return gm(gm(g,h),gi(g))
SS=(AZ,MZ,HS)
RR=(J['RR'][0][:4],tuple(J['RR'][1][i]for i in sel),HR)
TT=gm(SS,RR)
assert gm(SS,SS)==ONE and gm(gm(RR,RR),RR)==ONE
wc=J['WC'][:4];WC=(wc,MZ,H0)
def c0(g):
 a,m,h=g;a,m=monop(J['I']['C'],an(a),m)
 return inner(WC,(a,m,J['hc'](h)))
cs=gm(c0(SS),gi(SS));assert cs[0]==AZ and cs[2]==H0
CS=mn(cs[1])
def ca(g):
 a,m,h=c0(g)
 return(a,ma(m,CS)if J['eps'](g[2])else m,h)
assert ca(SS)==SS and ca(RR)==gm(gm(SS,gi(RR)),SS)
assert ca(TT)==gi(TT)and ca(ca(RR))==RR
raw=json.loads((ROOT/'records/full_cubic_scalar_frame_lift.json').read_text())
mb=raw['full20_frame_projection'][1];ab=raw['full20_frame_projection'][0]
t=[[x^red(y)for x,y in zip(a,b)]for a,b in zip(ab,wc)]
I=J['I'];Smon=J['hmon'](HS);Bmon=J['hmon'](HB)
Dmon=I['compose'](Bmon,I['C'])
group=[I['ID'],Smon,Dmon,I['compose'](Smon,Dmon)]
assert I['compose'](Dmon,Dmon)==I['ID']
def lift_fixed(v):
 out=[None]*36
 for i in range(36):
  if out[i]is not None:continue
  a=TEICH[v[i]]
  for pp,ww in group:
   k=pp[i];value=MUL[ww[i]][a]
   assert out[k]is None or out[k]==value
   out[k]=value
 assert all(x is not None for x in out)
 assert [red(x)for x in out]==list(v)
 return tuple(out)
tlift=tuple(lift_fixed(row)for row in t)
assert act(Smon,tlift)==tlift and act(Dmon,tlift)==tlift
p=av(wc,tlift)
m=tuple(TEICH[x]if f else x for x,f in zip(mb,free))
BFRAME=(p,m,HB)
assert inner(BFRAME,SS)==SS
def half_norm(B):
 n=gm(gi(B),ca(gi(B)))
 assert n[0]==AZ and n[2]==H0
 out=[]
 for x,f in zip(n[1],free):
  if f:
   assert red(x)==0
   out.append(sum(((x>>(2*j+1))&1)<<j for j in range(3)))
  else:assert x==0;out.append(0)
 return tuple(out)
initial=half_norm(BFRAME)
# Obtain the already verified scalar shear formula and Z-only image.
source=(HERE/'verify_full_scalar_norm_formula.py').read_text()
env={'__file__':str(HERE/'verify_full_scalar_norm_formula.py')}
exec(compile(source.split("oldm=p['old_center_projection_columns']")[0],
             str(HERE/'verify_full_scalar_norm_formula.py'),'exec'),env)
scalar_m=env['mnorm'];pack=env['pack'];scalar_z=env['znorm']
def field_rows(v):return tuple(tuple(TEICH[x]for x in row)for row in v)
fixed=raw['correction_joint_fixed_weight_basis']
# These stored fixed vectors are cubic coefficients. Undo cubic intertwiner
# j3(v)_lambda=v_partner^4 to obtain the positive degree-one joint invariants.
partner=J['partner']
joint1=[tuple(J['G']['fp'](v[partner[i]],2)for i in range(36))for v in fixed]
for v in joint1:
 vv=lift_fixed(v)
 assert act(Smon,(vv,)*4)[0]==vv and act(Dmon,(vv,)*4)[0]==vv
columns=[];labels=[];halves=[]
for i in range(4):
 for j,v in enumerate(joint1):
  for scalar in(1,2,4):
   q=[(0,)*36 for _ in range(4)]
   q[i]=tuple(MUL[2][TEICH[fm(scalar,x)]]for x in v)
   Q=(tuple(q),MZ,H0)
   assert inner(Q,SS)==SS
   BB=gm(BFRAME,Q);hh=half_norm(BB)
   delta=tuple(x^y for x,y in zip(hh,initial))
   columns.append(pack(scalar_m(delta)));halves.append(delta);labels.append((i,j,scalar))
zcols=[]
for i in range(16):
 for weight in(8,11):
  for scalar in(1,2,4):
   zz=[[0]*36 for _ in range(16)];zz[i][weight]=scalar
   zcols.append(pack(scalar_z(zz)))
def solve(cols,target):
 piv={}
 for i,x in enumerate(cols):
  mask=1<<i
  while x:
   k=x.bit_length()-1
   if k not in piv:piv[k]=(x,mask);break
   x^=piv[k][0];mask^=piv[k][1]
 mask=0;x=target
 for k in sorted(piv,reverse=True):
  if x>>k&1:x^=piv[k][0];mask^=piv[k][1]
 return(None if x else mask),len(piv)
_,rz=solve(zcols,0)
target=pack(scalar_m(initial));solution,rr=solve(zcols+columns,target)
print('Actual free GR(4,3) source/canonical-c and joint affine lift: PASS')
print('Initial forced half-center modulo2:',initial)
print('Z-only scalar rank:',rz,'; with144 doubled affine variations:',rr)
print('Initial integral half-shift lies in combined image:',solution is not None)
out=dict(scope='Exact first integral frame compatibility gate; source free-center normalized literally',
 initial_half_center=initial,initial_scalar_half_shift=target,
 doubled_joint_labels=labels,half_center_variation_columns=halves,
 scalar_variation_columns=columns,Z_only_rank=rz,combined_rank=rr,
 compatibility_solvable=solution is not None,solution_mask=solution,
 initial_affine_frame=p,initial_center_frame=m,integral_joint_t=tlift)
if solution is not None:
 # In this witness the canonical lift requires no affine variation.
 zsolution,zrank=solve(zcols,target)
 assert zsolution is not None
 halfO=tuple(TEICH[x]if f else 0 for x,f in zip(initial,free))
 B4=gm(BFRAME,(AZ,halfO,H0))
 assert inner(B4,SS)==SS and gm(gi(B4),ca(gi(B4)))==ONE
 # Lift the normalized half-center into the complete old norm-zero center.
 oldcols=[];oldlabels=[]
 for i,v in enumerate(raw['old_center_norm_kernel_basis']):
  for scalar in(1,2,4):
   q=[fm(scalar,x)for x in v]
   oldcols.append(pack(env['apply'](raw['old_center_projection_columns'],q)))
   oldlabels.append((i,scalar))
 oldsol,oldrank=solve(oldcols,pack(initial));assert oldsol is not None
 old36=[0]*36
 for i,(j,scalar)in enumerate(oldlabels):
  if oldsol>>i&1:
   old36=[a^fm(scalar,b)for a,b in zip(old36,raw['old_center_norm_kernel_basis'][j])]
 assert env['apply'](raw['old_center_projection_columns'],old36)==list(initial)
 # Repair the original scalar norm plus this forced half-center shift.
 combined=pack(raw['scalar_frame_square'])^target
 zs,zrank=solve(zcols,combined);assert zs is not None
 zz=[[0]*36 for _ in range(16)];index=0
 for i in range(16):
  for weight in(8,11):
   for scalar in(1,2,4):
    if zs>>index&1:zz[i][weight]^=scalar
    index+=1
 assert pack(scalar_z(zz))==combined
 Jmat=json.loads((HERE.parent/'A66_UT4_frame_surjection.json').read_text())['J']
 ux=[[env['xor'](fm(Jmat[i][j],zz[j][k])for j in range(16))for k in range(36)]for i in range(4)]
 pairs6=list(itertools.combinations(range(4),2));pi6={x:i for i,x in enumerate(pairs6)}
 triples4=list(itertools.combinations(range(4),3));tc=[[0]*36 for _ in range(6)]
 def tmap(a,t):return [fm(a[i],t[pi6[j,k]])^fm(t[pi6[i,j]],a[k])for i,j,k in triples4]
 for weight in(8,11):
  a=[row[weight]for row in env['avec']];ct=[];tl=[]
  for i in range(6):
   for scalar in(1,2,4):
    v=[0]*6;v[i]=scalar;ct.append(pack(tmap(a,v)));tl.append((i,scalar))
  ts,trank=solve(ct,pack([row[weight]for row in ux]));assert trank==12 and ts is not None
  for j,(i,scalar)in enumerate(tl):
   if ts>>j&1:tc[i][weight]^=scalar
  assert tmap(a,[row[weight]for row in tc])==[row[weight]for row in ux]
 out.update(corrected_mod4_free_frame=B4,mod4_free_norm='PASS',
            old_complete_center_correction=old36,old_center_projection_rank=oldrank,
            scalar_ordinary_correction=zz,UT4_lower_T_correction=tc,
            corrected_mod2_free_center=[red(x)if f else x for x,f in zip(B4[1],free)],
            scalar_equation_after_integral_half=True,UT4_equation=True,
            affine_variation_needed=False)
 print('Corrected actual mod4 free frame has literal conjugacy and norm1: PASS')
 print('Forced center lifts to the complete old norm-zero center; combined Z/T equations: PASS')
(HERE.parent/'full_scalar_integral_frame_gate.json').write_text(json.dumps(out,indent=2)+'\n')
