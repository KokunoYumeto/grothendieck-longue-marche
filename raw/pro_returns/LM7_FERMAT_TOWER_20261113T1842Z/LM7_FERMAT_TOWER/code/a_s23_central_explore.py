from pathlib import Path
import importlib.util,json,itertools
import sympy as s
import numpy as np

HERE=Path(__file__).resolve().parent
BASE=HERE.parents[1]/'LM7_FERMAT_TOWER/code'
def load(name,path):
 sp=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
def mat(v):return s.Matrix([[s.Rational(a)for a in row]for row in v])
def enc(v):return [[str(a)for a in v.row(i)]for i in range(v.rows)]
def integral(v):return all(s.Rational(a).q%3 for a in v)
def mod(a,n):
 a=s.Rational(a);return int(a.p)*pow(int(a.q),-1,n)%n
sm=load('e99central_smith',BASE/'e_cusp_local_smith.py')
hall=load('e99central_hall',BASE/'e_unramified_sections.py').Hall(2)
data=json.loads((HERE/'a_s23_explore.json').read_text())
J=mat(data['J']);F=mat(data['Frobenius']);I=s.eye(10)
U=s.Matrix([[0,-1],[2,-2],[1,0],[0,-2],[1,-1],[2,0],[1,-2],[2,-1]])
Z=s.Matrix([[0,-1],[1,-1]])
Pi=s.eye(2)+3*Z;Pibar=s.eye(2)+3*Z**2
E=Pi*Pibar.inv()
A=E.row_join(s.zeros(2,8)).col_join(((U*E-U)/3).row_join(s.eye(8)))
L=A*J;assert L*L==I and integral(A)
oldVp=mat(data['Vplus']);oldVm=mat(data['Vminus']);Wm=mat(data['Wminus'])
Lp=s.Matrix.hstack((I+L)*I[:,0]/2,I[:,3]-I[:,4],I[:,6]-I[:,7],I[:,8]-I[:,9])
Lm=((I-L)*I[:,1]/2).row_join(Wm)
SL=Lp.row_join(Lm);SLi=SL.inv()
assert integral(SLi) and L*Lp==Lp and L*Lm==-Lm
ii=[k for k,d in enumerate(hall.degree)if d==2];ri={k:i for i,k in enumerate(ii)}
def br(a,b):
 out=s.zeros(45,1)
 for i in range(10):
  for j in range(10):
   if a[i] and b[j]:
    for k,n in hall.bracket(i,j).items():out[ri[k]]+=a[i]*b[j]*n
 return out
def ext(A):return s.Matrix.hstack(*[br(A[:,hall.children[k][0]],A[:,hall.children[k][1]])for k in ii])
A2=ext(A);F2=ext(F);J2=ext(J);L2=A2*J2
pp=[(i,j)for i in range(10)for j in range(i)if(i<4)==(j<4)]
mm=[(i,j)for i in range(10)for j in range(i)if(i<4)!=(j<4)]
SML=s.Matrix.hstack(*[br(SL[:,i],SL[:,j])for i,j in pp+mm]);SMLi=SML.inv()
assert integral(SMLi)
MLp=SML[:,:21];MLm=SML[:,21:]
assert L2*MLp==MLp and L2*MLm==-MLm
Mp=mat(data['Mplus']);Mm=mat(data['Mminus']);SM=Mp.row_join(Mm);SMi=SM.inv()
Htop=SMi[:21,:]*(s.eye(45)-F2)*Mp
Hbottom=SMLi[21:,:]*(s.eye(45)-A2)*Mp
assert (I-J)*oldVp==s.zeros(10,4)
H=Htop.col_join(Hbottom)
HS=sm.local_smith(H.tolist())
print('central gauge Smith',HS['valuations'],'free',HS['free_rank'],flush=True)
assert HS['valuations']==[0]*7+[1]*9+[2]*5 and HS['free_rank']==24
# The free tame coordinate is the actual compact determinant class.
w=br(3*I[:,0]+I[:,2:]*U[:,0],3*I[:,1]+I[:,2:]*U[:,1])
assert F2*w==4*w and J2*w==-w
Dright=mat(data['tame_relation_smith']['right'])
km=Mm*Dright[:,23]
q=[s.cancel(w[i]/km[i])for i in range(45)if km[i]]
assert len(set(q))==1 and integral(s.Matrix(q)) and integral(s.Matrix([1/q[0]]))
print('compact kernel unit ratio',q[0],flush=True)
# Record and verify the cyclic inertia residue line in every Frobenius stratum.
cycles=[]
residue_array=np.asarray(list(itertools.product(range(9),repeat=5)),dtype=np.int64)
for rec in data['all_inertia_lattices']:
 X=mat(rec['inertia_HNF']);typ=rec['inertia_Smith']
 order=9 if typ[0]==0 else 3
 columns=[tuple(mod(a,9)for a in X[:,i])for i in range(5)]
 def ordv(v):
  for n in [1,3,9]:
   if all(n*a%9==0 for a in v):return n
 candidates=[v for v in columns if ordv(v)==order]
 assert candidates
 g=min(candidates)
 elements={tuple(k*a%9 for a in g)for k in range(order)}
 assert all(v in elements for v in columns) and len(elements)==order
 # All 9^5 residues are tested by the exact integer inverse, once per stratum.
 Xi=X.inv();assert integral(9*Xi)
 X9=np.asarray([[mod(a,9)for a in(9*Xi).row(i)]for i in range(5)],dtype=np.int64)
 mask=np.all((residue_array@X9.T)%9==0,axis=1)
 actual={tuple(int(a)for a in row)for row in residue_array[mask]}
 assert actual==elements
 accepted=len(actual)
 assert accepted==order
 cycles.append({'U_coordinates':rec['U_coordinates'],'order':order,'generator_mod9':list(g)})
print('inertia residue classes',sum(r['order']for r in cycles),'strata',len(cycles),flush=True)
out={'status':'PASS','rho_Kummer3':2,'rho_proper_scalar':enc(E),'rho_matrix':enc(A),'rho_J':enc(L),
 'rho_J_Vplus':enc(Lp),'rho_J_Vminus':enc(Lm),'rho_J_Vsplit_inverse':enc(SLi),
 'rho_wedge':enc(A2),'rho_J_Mplus':enc(MLp),'rho_J_Mminus':enc(MLm),'rho_J_Msplit_inverse':enc(SMLi),
 'central_gauge':enc(H),'central_gauge_smith':sm.encode(HS),'compact_w':enc(w),'compact_kernel_unit_ratio':str(q[0]),
 'inertia_cycles':cycles,'accepted_inertia_residues':sum(r['order']for r in cycles),
 'residue_checks':81*9**5}
(HERE/'a_s23_central_explore.json').write_text(json.dumps(out,indent=2)+'\n')
