#!/usr/bin/env python3
"""Exact ninth-symbol image of E101's COMPLETE ordinary norm lattice."""
from pathlib import Path
from itertools import product
from collections import Counter
import argparse,hashlib,json,shutil,subprocess,tempfile
from sympy import Matrix,eye,zeros

HERE=Path(__file__).resolve().parent
INPUT=HERE.parent/'inputs'
ap=argparse.ArgumentParser();ap.add_argument('--gp');args=ap.parse_args()
if args.gp:
 gp=str(Path(args.gp).resolve())
 with tempfile.TemporaryDirectory(prefix='e106_') as td:
  stage=Path(td)
  for p in INPUT.glob('*.bin'):shutil.copy2(p,stage/p.name)
  proc=subprocess.run([gp,'-q',str(HERE/'e_next_prime_maps.gp')],cwd=stage,
                      stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
  (HERE/'e_next_prime_maps.out').write_text(proc.stdout)
  assert proc.returncode==0 and '***   at top-level' not in proc.stdout and '***   user error' not in proc.stdout
  assert '"type":"completion","status":"PASS"' in proc.stdout
def records_at(path):return [json.loads(l) for l in path.read_text().splitlines() if l.startswith('{')]
records=records_at(INPUT/'e106_e76_export.out')
coords={r['name']:r['value'] for r in records_at(INPUT/'e106_e101_coordinates.out') if 'name' in r}
field=next(r for r in records if r.get('type')=='field')
assert field['unit_basis']==coords['B1_generators'][:9]
rec=next(r for r in records if r.get('type')=='global_unit_characters' and r.get('n')==9)
M=Matrix(rec['matrix'])
P=eye(9)
for i in [0,4,7,8]:P[i,i]=3
P[0,1]=P[0,3]=1;P[4,5]=2
oldP=Matrix(coords['ordinary_B_unit_kernel_hnf'])
change=P.inv()*oldP
assert all(x.q==1 for x in change) and abs(change.det())==1
assert all(x.q==1 for x in change.inv())
MP=M*P
assert all(x%3==0 for x in MP)
D=(MP/3).applyfunc(lambda x:int(x)%3)
def rref3(A):
 a=[list(map(lambda x:int(x)%3,A.row(i))) for i in range(A.rows)]
 h=0;ps=[]
 for j in range(A.cols):
  k=next((k for k in range(h,A.rows) if a[k][j]),None)
  if k is None:continue
  a[h],a[k]=a[k],a[h];v=pow(a[h][j],-1,3);a[h]=[(x*v)%3 for x in a[h]]
  for k in range(A.rows):
   if k!=h and a[k][j]:
    v=a[k][j];a[k]=[(x-v*y)%3 for x,y in zip(a[k],a[h])]
  ps.append(j);h+=1
 return Matrix(a),ps
R,piv=rref3(D)
assert len(piv)==4
normdata={r.get('name'):r.get('value') for r in json.loads((INPUT/'e106_e94_comparison.json').read_text())['complete_export_records']}
assert [r[:9] for r in normdata['radical_S_characters']]==M.tolist()
assert normdata['actual_radical_weights']==[5,5,5,8,5,4]
scale=Matrix.diag(*normdata['actual_radical_weights'])
actual=(scale*D).applyfunc(lambda x:int(x)%3)
assert all(x%9==0 for x in (Matrix([[5,5,5,8,5,4]])*M))
assert all(sum(actual[i,j] for i in range(6))%3==0 for j in range(9))
# Full finite row/column decomposition, with both inverse maps.
def minv3(A):return A.inv_mod(3).applyfunc(int)
_,cp=rref3(actual);Cb=actual[:,cp]
_,rp=rref3(Cb.T);L=Cb[rp,:].inv_mod(3)*eye(6)[rp,:]
L=L.applyfunc(lambda x:int(x)%3);assert (L*Cb).applyfunc(lambda x:x%3)==eye(4)
full=Cb
for j in range(6):
 if len(rref3(full.row_join(eye(6)[:,j]))[1])>full.cols:full=full.row_join(eye(6)[:,j])
assert full.cols==6
U=minv3(full)
rr,pp=rref3(actual);free=[j for j in range(9) if j not in pp]
null=[]
for j in free:
 c=zeros(9,1);c[j]=1
 for i,p in enumerate(pp):c[p]=-rr[i,j]%3
 null.append(c)
V=eye(9)[:,pp].row_join(Matrix.hstack(*null))
UI=minv3(U);VI=minv3(V)
Tgt=zeros(6,9)
for i in range(4):Tgt[i,i]=1
assert (U*actual*V).applyfunc(lambda x:x%3)==Tgt
hist=Counter()
aa=[list(map(int,actual.row(i))) for i in range(6)]
for y in product(range(3),repeat=9):
 hist[tuple(sum(x*z for x,z in zip(row,y))%3 for row in aa)]+=1
assert len(hist)==81 and set(hist.values())=={243}

# Actual full ideal norm from the original ray maps, retaining both bases.
G3=next(r for r in records if r.get('type')=='genus_smith' and r['n']==3)
G9=next(r for r in records if r.get('type')=='genus_smith' and r['n']==9)
maps=next(r for r in records if r.get('type')=='actual_maps')
inc=zeros(16,3);inc[:4,:]=Matrix([[-2,2,3],[1,0,0],[0,1,0],[0,0,1]])
pr=zeros(3,16);pr[:,:4]=Matrix([[1,-3,-3,-3],[0,1,0,0],[0,0,1,0]])
rawN=pr*Matrix(G3['left'])*Matrix(maps['genus_restriction'])*Matrix(G9['left_inverse'])*inc
oldmods=[9,3,3];newmods=[9,9,3]
def red(v,mods):return tuple(int(v[i])%m for i,m in enumerate(mods))
N=Matrix(3,3,lambda i,j:int(rawN[i,j])%oldmods[i]);assert N==Matrix([[2,3,6],[2,0,2],[0,1,0]])
space=list(product(*(range(m) for m in newmods)))
images={x:red(N*Matrix(x),oldmods) for x in space}
assert len(set(images.values()))==81
kn=[x for x in space if images[x]==(0,0,0)];assert kn==[(0,0,0),(0,3,0),(0,6,0)]
J=Matrix.hstack(*(3*Matrix(next(x for x in space if images[x]==tuple(int(j==i) for j in range(3)))) for i in range(3)))
J=Matrix(3,3,lambda i,j:int(J[i,j])%newmods[i]);assert J==Matrix([[6,0,0],[0,0,3],[0,0,0]])
for x in space:assert red(J*N*Matrix(x),newmods)==red(3*Matrix(x),newmods)
for y in product(*(range(m) for m in oldmods)):assert red(N*J*Matrix(y),oldmods)==red(3*Matrix(y),oldmods)

# The actual horizontal class maps use literal prime Frobenii, not an
# arbitrary lift through the vertical norm matrix.
prime_records=records_at(HERE/'e_next_prime_maps.out')
p7=next(r for r in prime_records if r.get('name')=='prime7')
p73=next(r for r in prime_records if r.get('name')=='prime73')
assert p7['relative_class']==[6,0,1] and p73['relative_class']==[1,8,2]
HH=Matrix([[4,3,0],[8,7,6],[1,0,1]]);trace=eye(3)+HH+HH**2
jb=Matrix(red(trace*Matrix(p73['relative_class']),newmods))
ja=Matrix(red(jb-Matrix(p7['relative_class']),newmods));JH=ja.row_join(jb)
NHraw=Matrix([[3,3,6],[2,0,0]])*N
NH=Matrix(2,3,lambda i,j:int(NHraw[i,j])%[9,3][i])
assert NH==Matrix([[3,6,6],[1,0,0]]) and JH==Matrix([[3,0],[3,3],[2,0]])
for x in space:assert red(JH*NH*Matrix(x),newmods)==red(trace*Matrix(x),newmods)
ljker=[]
for x in product(range(9),range(3)):
 assert red(NH*JH*Matrix(x),[9,3])==red(3*Matrix(x),[9,3])
 if red(JH*Matrix(x),newmods)==(0,0,0):ljker.append(x)
assert ljker==[(0,0),(3,0),(6,0)]

# Exact S-prime subgroup, with a full integral principal-divisor basis.
SC=Matrix([[6,6,6,6,3,0],[0,6,3,5,8,5],[2,2,2,1,1,1]])
oldSC=Matrix([[6,6,6,6,0,3],[1,1,1,2,2,2],[0,0,0,2,2,2]])
assert all((N*SC-oldSC)[i,j]%oldmods[i]==0 for i in range(3) for j in range(6))
SP=Matrix([[3,1,-3,2,2,0],[0,1,0,0,0,0],[0,-2,3,-2,-2,0],
           [0,0,0,3,0,1],[0,0,0,0,3,1],[0,0,0,0,0,1]])
assert abs(SP.det())==81 and all((SC*SP)[i,j]%newmods[i]==0 for i in range(3) for j in range(6))
sub={(0,0,0)}
for j in range(6):sub={red(Matrix(x)+a*SC[:,j],newmods) for x in sub for a in range(9)}
assert len(sub)==81
assert sub=={(y,z,t) for y,z,t in space if y%3==0}
assert red(SC*Matrix([1,1,1,0,0,0]),newmods)==(0,0,0)
assert all(red(3*SC[:,j],newmods)==(0,0,0) and red(SC[:,j],newmods)!=(0,0,0) for j in range(3))
SI=SP.inv();assert SI*SP==SP*SI==eye(6)
for j in range(6):
 assert all(x.q==1 for x in SI*(3*eye(6)[:,j])) if j<3 else True
out={'status':'PASS','ninth_unit_character_matrix':rec['matrix'],'ordinary_norm_lattice_columns':P.tolist(),
     'exact_ninth_character_product':MP.tolist(),'divided_cubic_character_matrix':D.tolist(),
     'image_rank':len(piv),'image_generator_columns':piv,'rref':R.tolist(),
     'actual_character_scales':[5,5,5,8,5,4],
     'actual_cubic_character_matrix':actual.tolist(),
     'finite_left_map':U.tolist(),'finite_left_inverse':UI.tolist(),
     'finite_right_map':V.tolist(),'finite_right_inverse':VI.tolist(),
     'image_basis':Cb.tolist(),'image_coordinate_inverse':L.tolist(),
     'finite_input_count':3**9,'finite_image_count':len(hist),'each_finite_fiber_count':243,
     'literal_B1_unit_basis_equality':True,
     'E101_norm_lattice_unimodular_basis_change':change.tolist(),
     'E101_norm_lattice_basis_change_inverse':change.inv().tolist(),
     'B2_class_number_3part':81,'B3_ambiguous_class_number_3part':81*3**(5-len(piv)),
     'B3_entire_class_group':[9,9,3],'E91_transvection_W_order':1,
     'vertical_ordinary_norm':N.tolist(),'vertical_ordinary_extension':J.tolist(),'vertical_norm_kernel':kn,
     'horizontal_ordinary_norm':NH.tolist(),'horizontal_ordinary_extension':JH.tolist(),'horizontal_capitulation_kernel':ljker,
     'horizontal_ordinary_unit_norm_index':1,
     'prime7_class':p7['relative_class'],'prime73_class':p73['relative_class'],
     'S_prime_class_matrix':SC.tolist(),'S_prime_class_image_order':len(sub),
     'principal_S_divisor_basis':SP.tolist(),'principal_S_divisor_inverse':[[[int(x.p),int(x.q)] for x in SI.row(i)] for i in range(6)],
     'L3_entire_class_group':[9,3],'original_q3_order':3,'finite_projection_exponent_a3':1,
     'B3_to_B2_ordinary_unit_norm_quotient':[3]*5,
     'B3_to_B2_ordinary_norm_kernel':'C3 plus Z3^54',
     'inputs':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(INPUT.iterdir()) if p.is_file()},
     'scope':'Entire next ordinary class groups and actual maps; eventual h is not evaluated.'}
(HERE/'e_next_unit_characters.json').write_text(json.dumps(out,indent=2,default=int)+'\n')
print(json.dumps(out,indent=2,default=int))
