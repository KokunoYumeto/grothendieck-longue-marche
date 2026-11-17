from collections import Counter

def red(w):
 o=[]
 for x in w:
  if o and o[-1]==-x:o.pop()
  else:o.append(x)
 return o
def inv(w):return [-x for x in w[::-1]]
def mul(*ws):return red(sum((list(w) for w in ws),[]))
def comm(a,b):return mul(a,b,inv(a),inv(b))
s=[5];si=[-5]
rel=[]
for i in range(1,5):
 x=[i]
 l=mul(si,x,si,x);rr=mul(x,si,x,si)
 rel.append(('R2_'+str(i),mul(l,inv(rr))))
for i in (1,2):
 for j in (3,4):rel.append(('R3_'+str((i,j)),comm(mul(si,[i],s),[j])))
for i,j in ((1,2),(3,4)):
 rel.append(('R4_'+str(i),mul(si,[i],si,[j],inv(mul([j],si,[i],s)))))
t=mul(comm([1],[-2]),comm([3],[-4]))
rel.append(('TR',mul(t,[-5,-5])))
# reps 1,s; generators x_i, y_i=s*x_i*s^-1, T=s^2

def rs(w):
 o=[];par=0
 for x in w:
  if abs(x)<5:o.append(x if par==0 else (1 if x>0 else -1)*(abs(x)+4))
  elif x==5:
   if par:o.append(9)
   par=1-par
  else:
   if not par:o.append(-9)
   par=1-par
 assert par==0
 return red(o)
def subst_t(w):return mul(*(t if x==9 else inv(t) if x==-9 else [x] for x in w))
def fmt(w):
 names=['a','b','c','d','A','B','C','D','t']
 return ' '.join(names[abs(x)-1]+('^-1' if x<0 else '') for x in w)
for nm,w in rel:
 for n,z in enumerate((w,mul(s,w,si))):
  q=rs(z)
  print(nm,n,fmt(q))
def apply(phi,w):return mul(*(phi[x] if x>0 else inv(phi[-x]) for x in w))
print('ACTION CHECKS')
for own in range(1,5):
 u=mul(t,[-own],t,[own],inv(t));w=mul(inv(u),t)
 phi={j:[j] for j in range(1,5)}
 phi[own]=mul(t,[own],inv(t))
 if own%2:
  phi[own+1]=mul(t,[own+1],inv(t),u)
 else:phi[own-1]=mul([own-1],inv(t))
 if own<=2:
  phi[3]=mul(w,[3],inv(w));phi[4]=mul(w,[4],inv(w))
 print(own,apply(phi,t)==u, len(apply(phi,t)),len(u))
 print({j:fmt(v) for j,v in phi.items()})
