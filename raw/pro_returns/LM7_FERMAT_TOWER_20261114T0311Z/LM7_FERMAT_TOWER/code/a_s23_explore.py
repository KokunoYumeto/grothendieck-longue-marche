from pathlib import Path
import json,importlib.util,itertools
import sympy as s
from sympy.matrices.normalforms import hermite_normal_form
BASE=Path(__file__).resolve().parents[2]/'LM7_FERMAT_TOWER/code'
HERE=Path(__file__).resolve().parent

def load(name,path):
 sp=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m

def mat(v):return s.Matrix([[s.Rational(a)for a in row]for row in v])
def enc(v):return [[str(a)for a in v.row(i)]for i in range(v.rows)]
def integral(v):return all(s.Rational(a).q%3 for a in v)
def mod(a,n):
 a=s.Rational(a);return int(a.p)*pow(int(a.q),-1,n)%n
hall=load('e99hall',BASE/'e_unramified_sections.py').Hall(2)
sm=load('e99smith',BASE/'e_cusp_local_smith.py')
hor=load('e99hor',BASE/'a_horizontal_full.py')
d=json.loads((BASE/'e_wild_layers.json').read_text())['layers']
path=json.loads((HERE.parents[1]/'research_e95/code/a_cusp_kummer.json').read_text())
J=mat(d['1']['input_c']);Id=s.eye(10);U=s.Matrix([[0,-1],[2,-2],[1,0],[0,-2],[1,-1],[2,0],[1,-2],[2,-1]])
F=(-2*s.eye(2)).row_join(s.zeros(2,8)).col_join((-2*U).row_join(4*s.eye(8)))
assert F*J==J*F
Vplus=s.Matrix.hstack((Id+J)*Id[:,0]/2,Id[:,3]-Id[:,4],Id[:,6]-Id[:,7],Id[:,8]-Id[:,9])
Wminus=s.Matrix.hstack(Id[:,2],Id[:,5],Id[:,3]+Id[:,4],Id[:,6]+Id[:,7],Id[:,8]+Id[:,9])
Vminus=((Id-J)*Id[:,1]/2).row_join(Wminus)
SV=Vplus.row_join(Vminus);SVI=SV.inv();assert integral(SVI)
assert J*Vplus==Vplus and J*Vminus==-Vminus
Fplus=(SVI*F*Vplus)[:4,:]
G=s.eye(4)-Fplus
GS=sm.local_smith(G.tolist());GL,GR,GD=(mat(GS[k])for k in ['left','right','diagonal_matrix'])
print('Vplus gauge=',G.tolist(),'smith',GS['valuations'],flush=True)
indices=[i for i,x in enumerate(hall.degree)if x==2];ri={k:i for i,k in enumerate(indices)}
def br(a,b):
 v=s.zeros(45,1)
 for i in range(10):
  for j in range(10):
   if a[i] and b[j]:
    for k,n in hall.bracket(i,j).items():v[ri[k]]+=a[i]*b[j]*n
 return v
# Every wedge basis is recorded as the literal bracket of two split columns.
pluspairs=[(i,j)for i in range(10)for j in range(i)if (i<4)==(j<4)]
minuspairs=[(i,j)for i in range(10)for j in range(i)if (i<4)!=(j<4)]
SM=s.Matrix.hstack(*[br(SV[:,i],SV[:,j])for i,j in pluspairs+minuspairs]);SMI=SM.inv();assert integral(SMI)
Mp=SM[:,:21];Mm=SM[:,21:];Minv=SMI[21:,:]
F2=s.Matrix.hstack(*[br(F[:,hall.children[k][0]],F[:,hall.children[k][1]])for k in indices])
J2=mat(d['2']['input_c']);assert J2*Mp==Mp and J2*Mm==-Mm
Fm=Minv*F2*Mm;D=Fm-4*s.eye(24)
DS=sm.local_smith(D.tolist());DL,DR,DD=(mat(DS[k])for k in ['left','right','diagonal_matrix'])
print('tame minus obstruction smith',DS['valuations'],'rank',len(DS['valuations']),flush=True)
K=[]
for lab in ['A0','A1','A2','B0','B1','B2','C1','C2']:
 co=path['global_cusp_coefficients'][lab]
 b=s.Matrix([s.Rational(a)for a in co['rational_coboundary']]);z=s.Matrix([s.Rational(a)for a in co['Kummer_zeta']])
 K.append((F-Id)*b+z)
KM=s.Matrix.hstack(*K);assert integral(KM)
print('actual cusp Frobenius2 K=',enc(KM),flush=True)
# Matrix in the five rational-inertia directions at a given fixed Frobenius value.
def omega(U0):
 return s.Matrix.hstack(*[4*sum((Wminus[d+2,j]*br(U0-K[d],Id[:,d+2])for d in range(8)),s.zeros(45,1))for j in range(5)])
for k in range(4):
 M=omega(Vplus[:,k]);assert J2*M==-M
rank=len(DS['valuations']);assert rank==23
select=[i for i,v in enumerate(DS['valuations'])if v]
mods=[3**DS['valuations'][i]for i in select]
print('finite moduli',mods,flush=True)
Rrep=mat(GS['left_inverse'])
coordmod=[3**v for v in GS['valuations']]
records=[]
for residues in itertools.product(*[range(v)for v in coordmod]):
 Uc=Rrep*s.Matrix(residues);U0=Vplus*Uc
 om=omega(U0);Fraw=DL*Minv*om
 assert Fraw[23:,:]==s.zeros(1,5)
 X=s.eye(5)
 for row,n in zip(select,mods):
  rr=s.Matrix([[mod(a,n)for a in Fraw.row(row)]])
  X=hermite_normal_form(X*hor.row_kernel(rr*X,n))
 assert integral(s.diag(*[3**v for v in DS['valuations']]).inv()*Fraw[:23,:]*X)
 ss=sm.local_smith(X.tolist())
 records.append({'U_coordinates':list(residues),'inertia_HNF':enc(X),'inertia_Smith':ss['valuations']})
from collections import Counter
ct=Counter(tuple(r['inertia_Smith'])for r in records)
print('all81 inertia lattices',ct,flush=True)
out={'status':'PASS','J':enc(J),'Frobenius':enc(F),'Vplus':enc(Vplus),'Wminus':enc(Wminus),'Vminus':enc(Vminus),'Vsplit_inverse':enc(SVI),
 'Frobenius_gauge':sm.encode(GS),'Mplus':enc(Mp),'Mminus':enc(Mm),'Mminus_inverse':enc(Minv),'tame_relation_smith':sm.encode(DS),'actual_cusp_Frobenius2':enc(KM),
 'finite_moduli':mods,'Frobenius_representative':enc(Rrep),'Frobenius_coordinate_moduli':coordmod,'all_inertia_lattices':records}
(HERE/'a_s23_explore.json').write_text(json.dumps(out,indent=2)+'\n')
