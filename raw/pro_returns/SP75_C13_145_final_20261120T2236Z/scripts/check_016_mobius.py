"""Exact local checks of the rational maps written in scan016's margin."""
from fractions import Fraction
from pathlib import Path
import json,math
E=Path(__file__).resolve().parents[1]
def mul(A,B):
 a,b,c,d=A;e,f,g,h=B
 return (a*e+b*g,a*f+b*h,c*e+d*g,c*f+d*h)
def canonical(M):
 g=0
 for x in M:g=math.gcd(g,abs(x))
 M=tuple(x//g for x in M)
 sign=next(x for x in M if x)
 return M if sign>0 else tuple(-x for x in M)
def value(M,z):
 a,b,c,d=M
 if z=='infinity':return 'infinity' if c==0 else str(Fraction(a,c))
 z=Fraction(z)
 return 'infinity' if c*z+d==0 else str((a*z+b)/(c*z+d))
S0=(1,0,1,-1);S1=(0,1,1,0);Si=(-1,1,0,1);R=(0,1,-1,1)
rows=[]
for name,M,fixed in [('sigma0',S0,['0','2']),('sigma1',S1,['1','-1']),('sigmainfty',Si,['infinity','1/2'])]:
 square=canonical(mul(M,M));assert square==(1,0,0,1)
 vals={x:value(M,x) for x in ['0','1','infinity']}
 f={x:value(M,x) for x in fixed};assert all(x==y for x,y in f.items())
 rows.append({'name':name,'matrix':M,'marked_point_images':vals,'fixed_points':f,'square_projectively_identity':True})
R2=canonical(mul(R,R));R3=canonical(mul(mul(R,R),R))
assert R2==(1,-1,1,0) and R3==(1,0,0,1)
assert [value(R,x) for x in ['0','1','infinity']]==['1','infinity','0']
out={'scope':'Only the rational formulas, marked-point permutations, fixed pairs and rho square/cube are checked. No assertion about the uniqueness of an oriented spherical metric is checked.','involutions':rows,'rho':{'matrix':R,'marked_point_images':{x:value(R,x) for x in ['0','1','infinity']},'square_matrix':R2,'square_formula':'(z-1)/z = 1-1/z','cube_projectively_identity':R3==(1,0,0,1)}}
(E/'reader_reports/145_scan016_mobius_check.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out))
