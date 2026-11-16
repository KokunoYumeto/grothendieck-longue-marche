"""Sharpness of the order-two trigonal ramification lemma in characteristic2.

E:y²+xy=x³+1 overF4 and f=(y+alpha)/x have three simple wild
ramification points whose differences have orders8,8,4. The cubic
resolvent is the known split genus-two quadratic twist. This does not
assert a collision; it rules out strengthening the elementary lemma
from order2 to every two-primary difference.
"""
import sys,json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'code'))
from finite_jacobian import BinaryField,PolynomialRing,Jacobian,genus2_characters
F=BinaryField(7);R=PolynomialRing(F);alpha=2;beta=3
E=Jacobian(F,(0,1),(1,0,0,1),g=1)
pts=dict(E.points());assert len(pts)==8
ram=[(0,1),(3,0),(3,3)]
residual=['infinity',(1,1),(1,0)]
branch_values=['infinity',3,2]
def order(D):
 n=1
 while E.scale(D,n)!=E.zero:n+=1
 return n
def differences(names):
 out=[]
 for i in range(len(names)):
  for j in range(i):
   D=E.add(pts[names[i]],E.neg(pts[names[j]]))
   out.append({'points':[names[j],names[i]],'order':order(D)})
 return out
rd=differences(ram);sd=differences(residual)
assert [a['order'] for a in rd]==[8,8,4]
assert [a['order'] for a in sd]==[4,4,2]
# f has pole divisor2T+infinity. At the other points its finite value is literal.
values={'infinity':'infinity'}
for name in pts:
 if name=='infinity':continue
 x,y=name;values[str(name)]='infinity' if x==0 else F.div(y^alpha,x)
assert values[str(ram[1])]==values[str(residual[1])]==3
assert values[str(ram[2])]==values[str(residual[2])]==2
# df=(x²+alpha)/x*omega. Zeros at x=beta are simple as points
# of x but doubled by x²+alpha; atT the pole multiplicities give
# different exponent2. This yields three ramification points exactly.
assert F.mul(beta,beta)==alpha
# Cubic x³+a x²+b x+c from y=t x+alpha; t-polynomial a=t²+t,b=c=alpha.
a=(0,1,1);b=(alpha,);c=(alpha,)
num=R.add(R.add(R.mul(R.mul(b,b),b),R.mul(R.mul(R.mul(a,a),a),c)),R.sq(c))
den=R.sq(R.add(R.mul(a,b),c))
# Berlekamp AS resolvent is beta*(a+1/(a+1)).
target_num=R.scale(R.add(R.mul(a,R.add(a,(1,))),(1,)),beta)
target_den=R.add(a,(1,))
assert R.mul(num,target_den)==R.mul(den,target_num)
# Remove beta*t² using an AS shift alpha*t, and put t=z+alpha.
# Result: y²+y=z+alpha+beta/(z²+z).
h=(0,1,1);f=R.add(R.mul((alpha,1),R.sq(h)),R.scale(h,beta))
C=Jacobian(F,h,f);assert len(C.points())==3 and len(C.enumerate())==12
chars=[r for r in genus2_characters(C) if r['ell']==3]
assert len(chars)==3 and all(r['point_counts']==[3,0,0] for r in chars)
assert all(r['relative_class_number']==64 for r in chars)
print(json.dumps({'field_modulus':7,'alpha':alpha,'beta':beta,
 'elliptic_curve':'y^2+x*y=x^3+1','map':'f=(y+alpha)/x',
 'elliptic_group_order':8,'elliptic_point_orders':[[name,order(D)] for name,D in E.points()],
 'ramification_points':ram,'residual_unramified_points':residual,'branch_values':branch_values,
 'ramification_difference_orders':rd,'residual_difference_orders':sd,
 'cubic_resolvent_numerator':num,'cubic_resolvent_denominator':den,
 'genus_two_resolvent':'y^2+y=z+beta/(z^2+z)+alpha','genus_two_h':h,'genus_two_f':f,
 'genus_two_points':3,'genus_two_J_order':12,'all_pointed_cubic_character_counts':[3,0,0],
 'twisted_L_polynomial':[1,3,4],'relative_class_number':64,
 'no_collision_asserted':True},indent=2))
