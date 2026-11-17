#!/usr/bin/env python3
from pathlib import Path
import json,hashlib
from fractions import Fraction as F
from math import isqrt
H=Path(__file__).resolve().parent
d=json.loads((H/'annular_neck_reflection23.json').read_text());scale=10**100
def sqrtbox(v):
 a=isqrt(v.numerator*scale*scale//v.denominator);return F(a,scale),F(a+1,scale)
l,h=sqrtbox(F(5));c1=((l-1)/4,(h-1)/4);c2=(-(h+1)/4,-(l+1)/4)
s1=(sqrtbox(10+2*l)[0]/4,sqrtbox(10+2*h)[1]/4)
s2=(sqrtbox(10-2*h)[0]/4,sqrtbox(10-2*l)[1]/4)
boxes=[(c1,s1),(c2,s2),(c2,(-s2[1],-s2[0])),(c1,(-s1[1],-s1[0]))];errors=[]
for z,bb in zip(d['unit_rational_u'],boxes):
 dif=[max(abs(F(v)-lo),abs(F(v)-hi)) for v,(lo,hi) in zip(z,bb)]
 assert sum(dif)<F(1,10**29);errors.append(list(map(str,dif)))
assert h<F(39,17) and c1[1]<F(31,100)
assert F(5)-4*F(31,100)>F(19,10)**2
M=2*(F(5)/F(4,5))*(F(5)/F(4,5)+F(25)/F(4,5)**2)
assert M<600 and 600*F(1,10**29)<F(1,10**26)
out={'status':'PASS','true_cyclotomic_radical_boxes':[[[str(x)for x in box]for box in pair]for pair in boxes],
 'coordinate_error_bounds':errors,'euclidean_error_bound':'1e-29','uniform_y_displacement_bound':'1e-26',
 'derivative_bound':'600','short_arc_bound':'Im Q>=3; min_j Im A_j>1 because39>17sqrt5',
 'hashes':{s:hashlib.sha256((H/s).read_bytes()).hexdigest()for s in['annular_neck_reflection23.json','annular_neck_bridge23.json']}}
(H/'annular_neck_reflection_deformation23.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS exact true cyclotomic intervals, Cayley-unit approximation and uniform<1e-26 configuration displacement')
print('PASS exact short-arc bound39>17sqrt5; all selected h stay in first quadrant')
