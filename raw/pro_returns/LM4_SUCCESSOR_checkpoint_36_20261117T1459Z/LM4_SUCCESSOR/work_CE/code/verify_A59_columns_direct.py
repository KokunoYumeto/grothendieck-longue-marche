"""Independent direct group-law verification of the A59 correction columns.
The A59 source is read-only; its one JSON destination is redirected here.
Only this CE directory is written. No full obstruction is inferred.
"""
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
import json,runpy
HERE=Path(__file__).resolve().parent;root=HERE.parents[1]
src=root/'work_A/check_A59_integral_center.py'
s=src.read_text().replace("(HERE/'A59_integral_center_baseline.json')",'Path('+repr(str(HERE.parent/'A59_baseline_independent.json'))+')')
A={'__file__':str(src),'__name__':'_independent_A59_columns'}
with redirect_stdout(StringIO()):exec(compile(s,str(src),'exec'),A)
with redirect_stdout(StringIO()):V=runpy.run_path(str(HERE/'check_Q6_new_center_variation.py'))
G=A['G'];fm=G['fm'];ZA=A['ZA'];AA0=A['AA0'];HN0=A['HN0'];ONE=A['ONE'];em=A['em'];ei=A['ei'];ein=A['ein'];za=A['za'];zn=A['zn'];eps=A['eps'];SS=A['SS'];TT=A['TT'];B=A['BFRAME'];ph=A['ph'];ca=A['ca'];na=A['na'];TEICH=A['TEICH'];MUL=A['MUL']
def doubled(row,vec,scalar):
 a=list(AA0);a[row]=tuple(MUL[2][TEICH[fm(scalar,x)]]for x in vec);return(tuple(a),ZA,HN0)
def unpack(z):
 p=A['central_kernel'](z);return tuple((p>>(3*i))&7 for i in range(6))
def scale(c,v):return tuple(fm(c,x)for x in v)
base=em(ei(B),na(ei(B)))[1]
count=0
for row in range(4):
 for j,u in enumerate(V['JF']):
  for scalar in (1,2,4):
   Q=doubled(row,u,scalar);BQ=em(B,Q)
   assert ein(BQ,SS)==ph(SS)
   val=em(ei(BQ),na(ei(BQ)))
   assert val[0]==AA0 and val[2]==HN0
   diff=unpack(za(val[1],zn(base)))
   assert diff==scale(scalar,V['cols'][row*12+j]),('s-column',row,j,scalar,diff)
   count+=1
print('Direct original-law s-frame columns checked over all binary scalar directions:',count)
countp=0
for row in range(4):
 for j,w in enumerate(V['TFk']):
  for scalar in(1,2,4):
   P=doubled(row,w,scalar);BP=em(P,B)
   tc=em(ein(P,TT),ei(TT));assert tc[0]==AA0 and tc[2]==HN0
   chi=zn(tc[1]);assert za(chi,chi)==ZA
   def phw(g):
    a,z,h=ein(P,ph(g))
    if eps(g[2]):z=za(z,chi)
    return(a,z,h)
   def naw(g):return phw(ca(g))
   assert phw(TT)==TT
   assert naw(naw(SS))==SS and naw(naw(A['RR']))==A['RR']
   cl=em(phw(SS),ei(ein(BP,SS)))
   assert cl[0]==AA0 and cl[2]==HN0
   assert unpack(cl[1])==scale(scalar,V['cuspcols'][row*4+j]),('cusp-column',row,j,scalar)
   val=em(ei(BP),naw(ei(BP)));assert val[0]==AA0 and val[2]==HN0
   diff=unpack(za(val[1],zn(base)))
   assert diff==scale(scalar,V['pcols'][row*4+j]),('positive-column',row,j,scalar,diff,scale(scalar,V['pcols'][row*4+j]))
   countp+=1
print('Direct original-law positive/cusp/s-class columns checked over all binary scalar directions:',countp)
print('Baseline central square vector:',unpack(base))
print('Restricted combined image rank5 and annihilator residue:',unpack(base)[0]^unpack(base)[1])
print('Scope: exact fixed-witness correction families; no claim of a universal norm obstruction.')
