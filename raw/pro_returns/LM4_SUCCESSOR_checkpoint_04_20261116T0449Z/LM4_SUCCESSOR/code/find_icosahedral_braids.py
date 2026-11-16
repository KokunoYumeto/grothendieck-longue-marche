"""Discover explicit braid words from rigid icosahedral rotations.

Floating point geometry is used ONLY to discover the words.  The separate
checker verifies their algebraic identities over free groups exactly.
"""
import itertools, math, json
from pathlib import Path
import numpy as np
from scipy.optimize import brentq

phi=(1+math.sqrt(5))/2
vertices=np.array([(0,a,b*phi) for a in (-1,1) for b in (-1,1)]+
                  [(a,b*phi,0) for a in (-1,1) for b in (-1,1)]+
                  [(a*phi,0,b) for a in (-1,1) for b in (-1,1)],dtype=float)
radius=np.linalg.norm(vertices[0])
q=np.array([1,phi+1,phi]);q=q/np.linalg.norm(q)
e1=np.cross(q,[1,2,3]);e1=e1/np.linalg.norm(e1)
e2=np.cross(q,e1)
def project(v):return (v@e1+1j*(v@e2))/(radius-v@q)
z0=project(vertices)
permutation=np.argsort(z0.real)
vertices=vertices[permutation];z0=z0[permutation]

def braid(axis,angle):
 axis=np.array(axis,dtype=float);axis/=np.linalg.norm(axis)
 def z(t):
  vs=vertices*np.cos(t)+np.cross(axis,vertices)*np.sin(t)+np.outer(vertices@axis,axis)*(1-np.cos(t))
  return project(vs)
 grid=np.linspace(0,angle,4001)
 samples=np.array([z(t) for t in grid])
 events=[]
 for i,j in itertools.combinations(range(12),2):
  f=samples[:,i].real-samples[:,j].real
  for k in np.where(f[:-1]*f[1:]<0)[0]:
   root=brentq(lambda t:(z(t)[i]-z(t)[j]).real,grid[k],grid[k+1],xtol=1e-14)
   zz=z(root);d=((z(root+1e-7)[i]-z(root+1e-7)[j])-(z(root-1e-7)[i]-z(root-1e-7)[j])).real
   sign=1 if d*(zz[i]-zz[j]).imag<0 else -1
   events.append((root,i,j,sign))
 events.sort()
 order=list(range(12));word=[]
 for t,i,j,sign in events:
  a,b=order.index(i),order.index(j)
  assert abs(a-b)==1,(t,i,j,a,b)
  word.append(sign*(min(a,b)+1));order[a],order[b]=order[b],order[a]
 assert order==list(np.argsort(z(angle).real))
 end=[int(np.argmin(abs(z0-zz))) for zz in z(angle)]
 assert max(abs(z0[end]-z(angle)))<1e-10
 return word,end

w2,p2=braid(q,math.pi)
w3,p3=braid([1,1,1],2*math.pi/3)
data={'beta2':w2,'beta3':w3,'permutation2':p2,'permutation3':p3,
      'discovery':'floating geometric search; see exact algebraic checker'}
path=Path(__file__).resolve().parents[1]/'data'/'icosahedral_braids.json'
path.write_text(json.dumps(data,indent=2)+'\n')
print('beta2:',w2,'length',len(w2),'exponent',sum(1 if x>0 else -1 for x in w2))
print('beta3:',w3,'length',len(w3),'exponent',sum(1 if x>0 else -1 for x in w3))
print('permutation2:',p2,'permutation3:',p3)
