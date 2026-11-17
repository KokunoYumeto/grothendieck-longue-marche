"""Actual normalized eight-row704 scalar model.
Research: preserve actual old36 center/C4 source; no full norm claim.
"""
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
import runpy,json,numpy as np
HERE=Path(__file__).resolve().parent;ROOT=HERE.parent
with redirect_stdout(StringIO()):O=runpy.run_path(str(HERE/'check_Q6_central_cover.py'))
def tup(x):return tuple(tup(v)for v in x)if isinstance(x,list)else x
w=json.loads((HERE/'A66_W0_local_compatible_partial.json').read_text())
O['phi0'].__globals__['WE']=tup(w['WE']);O['ph'].__globals__['PSHIFT']=tup(w['PSHIFT'])
fm,fp,flin,fva,fsm=[O[k]for k in('fm','fp','flin','fva','fsm')]
zero=(0,)*36;A0=(zero,)*8;M0=(0,)*36;H0=O['HN0']
slots=[(i,j)for i in range(8)for j in range(8)if i<4 or j<4];zi={ij:i for i,ij in enumerate(slots)}
triples=[(i,j,k)for i in range(8)for j in range(8)for k in range(8)if(i,j)in zi and(j,k)in zi];ti={t:i for i,t in enumerate(triples)}
closed=[i for i,t in enumerate(triples)if sum(x<4 for x in t)>=2]
openidx=[i for i in range(320)if i not in closed]
assert len(slots)==48 and len(triples)==320 and len(closed)==256 and len(openidx)==64
Z0=(zero,)*48;U0=(0,)*320;mpairs=O['zpairs'];mi={t:i for i,t in enumerate(mpairs)}
P=(0,1,2,3,5,4,7,6);C=(0,1,2,3,4,5,7,6)
FM=np.array([[fm(a,b)for b in range(8)]for a in range(8)],dtype=np.uint8)
POW2=np.array([fp(a,2)for a in range(8)],dtype=np.uint8);POW4=np.array([fp(a,4)for a in range(8)],dtype=np.uint8)
IX=np.array([t[0]for t in triples]);JX=np.array([t[1]for t in triples]);KX=np.array([t[2]for t in triples])
ZI=np.array([zi[i,j]for i,j,k in triples]);ZJ=np.array([zi[j,k]for i,j,k in triples])
pairs=O['vpairs']
def xor(vs):
 out=0
 for v in vs:out^=v
 return out
def sigma(u):
 out=[0]*320
 for j in closed:
  i,l,k=triples[j];out[ti[l,k,i]]=fp(u[j],2)
 return tuple(out)
def stem(u):
 s=sigma(u);ss=sigma(s);return tuple(u[j]if j in OPEN else s[j]^ss[j]for j in range(320))
OPEN=set(openidx)
def av(a,b):return tuple(fva(v,w)for v,w in zip(a,b))
def sym(a,b):return tuple(fm(a[i],b[j])^(fm(a[j],b[i])if i!=j else 0)for i,j in mpairs)
def weight(a,i):return tuple(row[i]for row in a)
def pcoc(a,b):
 out=M0
 for l,r in pairs:out=fva(out,sym(weight(a,l),weight(b,r)))
 return out
MD={}
def monodata(key):
 if key not in MD:
  cols=O['CV']if key=='c'else O['hcols'](key);dest=[];sc=[]
  for col in cols:
   i=next(i for i,v in enumerate(col)if v);assert sum(bool(v)for v in col)==1;dest.append(i);sc.append(col[i])
  assert all(O['partner'][dest[l]]==dest[r]and fm(sc[l],sc[r])==1 for l,r in pairs)
  MD[key]=(dest,sc)
 return MD[key]
def act(key,rows,degree=1):
 dest,sc=monodata(key);out=[]
 for row in rows:
  v=[0]*36
  for i,x in enumerate(row):v[dest[i]]=fm(fp(sc[i],degree),x)
  out.append(tuple(v))
 return tuple(out)
def monop(key,a,m):
 dest,_=monodata(key)
 for l,r in pairs:
  if dest[l]>dest[r]:m=fva(m,sym(weight(a,l),weight(a,r)))
 return act(key,a),m
ad=json.loads((ROOT/'work_CE/Q6_integral_affine_data.json').read_text());E=tup(ad['new_basis_columns_in_old_EB']);ag=tup(ad['cochain_coboundary_in_V8'])
ecols=[tuple(row[i]for row in E)for i in range(8)];mcols=[sym(ecols[i],ecols[j])for i,j in mpairs]
def oldm(m):return flin(mcols,m)
QS=oldm(O['QS'])
PONE=(A0,M0,H0)
def pm(g,h):
 a,m,q=g;b,n,r=h;b,n=monop(q,b,n);mm=fva(fva(m,n),pcoc(a,b))
 if O['eps'](q)and O['eps'](r):mm=fva(mm,QS)
 return av(a,b),mm,O['hmul'](q,r)
def pi(g):
 a,m,h=g;ih=O['hinv'](h);b=act(ih,a);_,carry=monop(h,b,M0);mm=fva(fva(m,carry),pcoc(a,a))
 if O['eps'](h):mm=fva(mm,QS)
 return b,mm,ih
def pin(g,h):return pm(pm(g,h),pi(g))
GAUGE=(ag,M0,H0)
def ungauged(g):return pin(GAUGE,(O['mix'](E,g[0]),oldm(g[1]),g[2]))
MS=ungauged(O['SS'])[1]
def old_project(g):
 a,m,h=ungauged(g);return a,fva(m,MS)if O['eps'](h)else m,h

def permrows(a,p):return tuple(a[p[i]]for i in range(8))
def permm(m,p):return tuple(m[mi[tuple(sorted((p[i],p[j])))]]for i,j in mpairs)
def permz(z,p):return tuple(z[zi[p[i],p[j]]]for i,j in slots)
def permu(u,p):return tuple(u[ti[p[i],p[j],p[k]]]for i,j,k in triples)
assert permm(QS,P)==permm(QS,C)==QS
for g in [O['ONE'],O['SS'],O['RR'],O['TT'],O['ei'](O['TT'])]:
 for h in [O['SS'],O['RR'],O['TT']]:assert old_project(O['em'](g,h))==pm(old_project(g),old_project(h))
print('Actual normalized full36 center and nonzero C4 source carry: PASS',flush=True)

def cup(a,b):return tuple(tuple(fm(fp(x,2),y)for x,y in zip(a[i],b[j]))for i,j in slots)
def fcoc(a,z,b,w):
 if (a==A0 and z==Z0)or(b==A0 and w==Z0):return U0
 aa=np.asarray(a,dtype=np.uint8);bb=np.asarray(b,dtype=np.uint8);zz=np.asarray(z,dtype=np.uint8);ww=np.asarray(w,dtype=np.uint8)
 vals=np.bitwise_xor.reduce(FM[zz[ZI],POW4[bb[KX]]]^FM[POW2[aa[IX]],POW4[ww[ZJ]]],axis=-1)
 return stem(tuple(int(x)for x in vals))
ONE=(A0,M0,Z0,U0,H0)
def gm(g,h):
 a,m,z,u,q=g;b,n,w,v,r=h;b,n=monop(q,b,n);w=act(q,w,3);mm=fva(fva(m,n),pcoc(a,b))
 if O['eps'](q)and O['eps'](r):mm=fva(mm,QS)
 return av(a,b),mm,av(av(z,w),cup(a,b)),fva(fva(u,v),fcoc(a,z,b,w)),O['hmul'](q,r)
def gi(g):
 a,m,z,u,h=g;ih=O['hinv'](h);b=act(ih,a);_,carry=monop(h,b,M0);mm=fva(fva(m,carry),pcoc(a,a))
 if O['eps'](h):mm=fva(mm,QS)
 w=act(ih,av(z,cup(a,a)),3);uu=fva(u,fcoc(a,z,a,av(z,cup(a,a))))
 return b,mm,w,uu,ih
def gin(g,h):return gm(gm(g,h),gi(g))
def project(g):return g[0],g[1],g[4]
sa,sm,sh=old_project(O['SS']);assert sm==M0 and all(not any(v)for v in sa[:4])
S=(sa,sm,Z0,U0,sh)
ra=act(O['HR'],old_project(O['RR'])[0]);R=gin((ra,M0,Z0,U0,H0),(A0,M0,Z0,U0,O['HR']));T=gm(S,R)
assert project(R)==old_project(O['RR'])
assert gm(S,S)==gm(gm(R,R),R)==ONE
assert gm(T,gi(T))==gm(gi(T),T)==ONE
print('Actual mixed704 source S²=R³=1, exact old projection: PASS',flush=True)

# Assemble the already solved actual ordinary actions on all48 slots.
free=json.loads((HERE/'A66_W0_local_ordinary_result.json').read_text())
d67=json.loads((HERE/'mixed_binary67_cubic_result.json').read_text());d45=json.loads((HERE/'mixed_binary45_cubic_result.json').read_text())
CC=[None]*48;PC=[None]*48;AC=[zero]*48
for d,ss in [(free,[(i,j)for i in range(4)for j in range(4)]),(d67,d67['mixed_slots']),(d45,d45['mixed_slots'])]:
 for jj,ij in enumerate(ss):
  k=zi[tuple(ij)];CC[k]=tup(d['canonical_c_corrections'][jj]);PC[k]=tup(d['positive_corrections'][jj])
  if 'inner_action_correction'in d:AC[k]=tup(d['inner_action_correction'][jj])
assert all(v is not None for v in CC+PC)
LC=tuple(row[:8]for row in CC);VC=tuple(row[8:]for row in CC)
LPpre=tuple(row[:8]for row in PC);VPpre=tuple(row[8:]for row in PC)
CW=av(av(O['mix'](E,O['WC']),ag),act('c',permrows(ag,C)))
PW=av(av(O['mix'](E,tup(w['WE'])[0]),ag),permrows(ag,P))
LP=tuple(tuple(row[P[i]]for i in range(8))for row in LPpre)
def j3(v):return tuple(fp(v[O['partner'][i]],4)for i in range(36))
VP=av(av(VPpre,tuple(flin(tuple(j3(v)for v in PW),row)for row in LP)),tuple(AC))
def shear(g,L):
 a,m,z,u,h=g;ja=tuple(j3(v)for v in a);zz=tuple(fva(v,flin(ja,row))for v,row in zip(z,L))
 Q=[[xor(fm(a[i][l],a[j][r])for l,r in pairs)^(m[mi[tuple(sorted((i,j)))]]if i!=j else 0)for j in range(8)]for i in range(8)]
 raw=tuple(xor(fm(L[zi[i,j]][l],fp(Q[k][l],4))^fm(fp(L[zi[j,k]][l],4),fp(Q[l][i],2))for l in range(8))for i,j,k in triples)
 return a,m,zz,fva(u,stem(raw)),h

def mono(g,p,phys=False):
 a,m,z,u,h=g;a=permrows(a,p);m=permm(m,p);z=permz(z,p);u=permu(u,p)
 if phys:a,m=monop('c',a,m);z=act('c',z,3);h=O['hc'](h)
 return a,m,z,u,h
WC=(CW,M0,Z0,U0,H0);WP=(PW,M0,Z0,U0,H0)
VVc=(A0,M0,VC,U0,H0);VVp=(A0,M0,VP,U0,H0)
def candidate_c(g):return gin(VVc,shear(gin(WC,mono(g,C,True)),LC))
def candidate_p(g):return gin(VVp,shear(gin(WP,mono(g,P)),LP))
cs=candidate_c(S);CM=fva(cs[1],S[1]);CU=fva(cs[3],S[3])
def ca(g):
 a,m,z,u,h=candidate_c(g)
 if O['eps'](g[4]):m=fva(m,CM);u=fva(u,CU)
 return a,m,z,u,h
assert ca(S)==S
assert ca(R)==gm(gm(S,gi(R)),S)
assert ca(T)==gi(T)
assert ca(ca(S))==S and ca(ca(R))==R
sample=[ONE,S,R,T,gi(T)]
for g in sample:
 assert project(ca(g))==old_project(O['ca'](next(og for og in[O['ONE'],O['SS'],O['RR'],O['TT'],O['ei'](O['TT'])]if old_project(og)==project(g))))
 for h in sample[:3]:
  assert shear(gm(g,h),LC)==gm(shear(g,LC),shear(h,LC))
  assert ca(gm(g,h))==gm(ca(g),ca(h))
print('Actual704 canonical c, lifted all8-center shear and source square: PASS',flush=True)
# The positive candidate has the specified ordinary action. Correct its
# globally central cusp value by the unique parity character.
pt=candidate_p(T);PM=fva(pt[1],T[1]);PU=fva(pt[3],T[3])
def ph(g):
 a,m,z,u,h=candidate_p(g)
 if O['eps'](g[4]):m=fva(m,PM);u=fva(u,PU)
 return a,m,z,u,h
assert ph(T)==T
for g,og in zip(sample,[O['ONE'],O['SS'],O['RR'],O['TT'],O['ei'](O['TT'])]):
 assert project(ph(g))==old_project(O['ph'](og))
 for h in sample[:3]:assert ph(gm(g,h))==gm(ph(g),ph(h))
def na(g):return ph(ca(g))
assert na(na(S))==S and na(na(R))==R
print('Positive literal cusp and negative action square on actual704 cover: PASS',flush=True)
# Retain the actual A69 center correction and the computed mixed frames.
a69=json.loads((HERE/'A69_integral_scalar_frame_solution.json').read_text());bf=tup(a69['corrected_full20_BFRAME']);bp=old_project(bf[0][0]);bz=[zero]*48
for jj,ij in enumerate([(i,j)for i in range(4)for j in range(4)]):bz[zi[ij]]=bf[1][4+jj]
for d in (d67,d45):
 for jj,ij in enumerate(d['mixed_slots']):bz[zi[tuple(ij)]]=tup(d['BFRAME'][1][jj])
B=(bp[0],bp[1],tuple(bz),U0,bp[2]);ps=ph(S);bs=gin(B,S)
assert ps[0]==bs[0]and ps[1]==bs[1]and ps[2]==bs[2]and ps[4]==bs[4]
SCLASS=fva(ps[3],bs[3]);bn=gm(gi(B),na(gi(B)))
assert bn[0]==A0 and bn[1]==M0 and bn[2]==Z0 and bn[4]==H0
print('Current fixed mixed32 frame scalar s-class nonzero:',any(SCLASS),'; scalar norm nonzero:',any(bn[3]),flush=True)
out=dict(scope='Actual704 scalar cover over normalized8-row source; fixed mixed32 action/frame. No exhaustion or full realization claim.',
 slots=slots,triples=triples,closed_indices=closed,source_C4=QS,source_center_shift=MS,
 source_S=S,source_R=R,canonical_inner=CW,positive_inner=PW,canonical_shear=LC,positive_shear=LP,
 canonical_center_shift=CM,canonical_scalar_shift=CU,positive_center_shift=PM,positive_scalar_shift=PU,
 source_and_action_checks='PASS',negative_square='PASS',fixed_frame=B,s_class_residue=SCLASS,s_norm=bn[3],
 s_class_nonzero=any(SCLASS),s_norm_nonzero=any(bn[3]))
(HERE/'mixed_scalar_action_result.json').write_text(json.dumps(out,indent=2)+'\n')
