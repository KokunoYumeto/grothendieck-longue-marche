"""A (4,4,4) perfect peripheral head with a nonsplit negative outer action."""
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import json
src=Path(__file__).with_name('check_M10_reflection_obstruction.py')
s=src.read_text().split("out=dict(scope=")[0]
g={'__file__':str(src),'__name__':'_M10_readonly'}
with redirect_stdout(StringIO()):exec(compile(s,str(src),'exec'),g)
pm,pi,LP,order,generated,hp=[g[k]for k in ('pm','pi','LP','order','generated','hp')]
fours=sorted(x for x in LP if order(x)==4)
witness=None
for x in fours:
 for y in fours:
  if order(pm(x,y))==4 and len(generated([x,y]))==360:
   witness=x,y;break
 if witness:break
assert witness is not None
x,y=witness;z=pi(pm(x,y))
beta=lambda a:pm(pm(hp,a),pi(hp))
frames=[]
for a in (x,y,z):
 frame=next((v for v in LP if pm(pm(v,pi(a)),pi(v))==beta(a)),None)
 assert frame is not None;frames.append(frame)
# Its order in Out(L) is two; all representatives of that outer coset
# are exactly the conjugations by elements of the M10 outer coset.
assert pm(hp,hp)in LP and hp not in LP
assert all(order(pm(a,hp))in (4,8)for a in LP)
print('Actual free pair generates PSL2(9): 360; cusp passport (4,4,4): PASS')
print('x=',x,'\ny=',y,'\nz=',z)
print('All three negative peripheral conjugators are literal kernel elements: PASS')
print('Negative outer involution has no involutory representative: PASS')
out=dict(scope='Peripheral-class-compatible finite outer action only; no full GT0 or actual source-specific central-lifting conclusion',x=x,y=y,z=z,negative_outer_representative=hp,negative_frames=frames,orders=[4,4,4],generated_order=360,outer_order=2,involutory_representatives=0)
Path(__file__).with_name('M10_peripheral_head.json').write_text(json.dumps(out,indent=2)+'\n')
# Audit the actual source central gate too: this particular (4,4,4)
# head already fails it, so it cannot be promoted to a full P action.
A,M,det,matmul,pw,perm,ALL=[g[k]for k in ('A','M','det','matmul','pw','perm','ALL')]
neg=g['N'];pinv=g['inv'];norm=g['norm']
def mi(a):
 u=pinv[det(a)];return tuple(M(u,v)for v in (a[3],neg(a[1]),neg(a[2]),a[0]))
def sl_lift(p):
 a=next(a for (a,e),pp in ALL.items()if e==0 and pp==p)
 t=next(t for t in range(1,9)if M(M(t,t),det(a))==1)
 return tuple(M(t,v)for v in a)
X,Y=sl_lift(x),sl_lift(y);Z=mi(matmul(X,Y));D=g['h'][0]
betasl=lambda a:matmul(matmul(D,tuple(pw(v,3)for v in a)),mi(D))
trs=[]
for Q in (X,Y,Z):
 tr=A(Q[0],Q[3]);b=betasl(Q);itr=A(mi(Q)[0],mi(Q)[3]);btr=A(b[0],b[3])
 assert tr and btr==neg(tr) and itr==tr and btr!=tr
 trs.append([tr,btr,itr])
print('Additional source-central audit: every cusp lift has trace changed to its negative.')
print('A multiplier -1 source lift would require central signs(-,-,-), contradicting xyz=1.')
print('Thus this finite peripheral head itself cannot be a full negative peripheral action; same spin gate as A28.')
out.update(central_double_cover_gate='FAIL: three required central signs multiply to -1',SL2_cusp_matrices=[X,Y,Z],trace_comparison=trs)
Path(__file__).with_name('M10_peripheral_head.json').write_text(json.dumps(out,indent=2)+'\n')
