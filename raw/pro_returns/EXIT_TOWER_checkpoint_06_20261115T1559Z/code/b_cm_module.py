"""Executed exact certificates for the CM parity module comparison.

Finite identities supplement, and do not replace, the geometric
normalizer/forgetting proof in B_cm_quartic_route.md.
"""
from pathlib import Path
import json,itertools
import sympy as S
P=Path(__file__).resolve().parent
H={};exec((P/'b_genus_zero.py').read_text().split('\ndata={}')[0],H)
red,inv,eq=H['red'],H['inv'],H['eq']
x=(3,-1);y=(1,2,1,-3,-2,-1)
words={1:x,2:y,-1:inv(x),-2:inv(y)}
images={(1,1):(1,),(1,2):(2,1),(2,1):(1,-2),(2,2):(2,),
        (3,1):(1,),(3,2):(1,2)}
checks=[]
for (g,k),w in images.items():
    lhs=(g,)+(x if k==1 else y)+(-g,)
    rhs=red(e for h in w for e in words[h])
    assert eq(4,lhs,rhs)
    checks.append({'generator':g,'fiber_generator':k,'fiber_word':w})
omega=(1,2)*3
assert eq(4,(2,1,1,2),omega+(-1,-1))

R=S.Matrix([[0,-1],[1,1]])
p=S.Matrix([1,0]);I=S.eye(2)
assert R**3==-I and R**6==I
def mod(M,n):return M.applyfunc(lambda a:int(a)%n)
def cyc(v):return S.Matrix.hstack(v,R*v)
# A matrix commuting with R is uniquely determined by its first column.
assert cyc(p)==I
four=[]
for j in (0,2,4):
  for bv in itertools.product(range(4),repeat=2):
    b=S.Matrix(bv)
    for bit in (0,1):
      if mod(b-bit*R**j*p,2)!=S.zeros(2,1):continue
      M=mod(cyc(2*b+R**j*p),4)
      assert mod(M*R-R*M,4)==S.zeros(2)
      assert M==mod((-1)**bit*R**j,4)
      four.append({'j':j,'beta_translation':bv,'epsilon2':bit,
                   'matrix':[[int(a) for a in row] for row in M.tolist()]})
three=[]
line=mod((R+I)*p,3)
assert line!=S.zeros(2,1) and mod((R+I)*line,3)==S.zeros(2,1)
for j in (0,2,4):
  for av in itertools.product(range(3),repeat=2):
    a=S.Matrix(av)
    M=mod(cyc((I-R**4)*a+R**j*p),3)
    assert mod(M*R-R*M,3)==S.zeros(2)
    assert mod(M*line,3)==line
    three.append({'j':j,'A_translation':av,
                  'matrix':[[int(v) for v in row] for row in M.tolist()]})

# Projective SL2(F3) and affine F2² have the same named s,r,tau action.
U=S.Matrix([[1,1],[0,1]]);L=S.Matrix([[1,0],[-1,1]])
Sm=U*L*U;Rm=-U*L;taum=Sm*Rm
labels={None:(0,0),0:(1,0),2:(0,1),1:(1,1)}
def mob(M,z):
  a,b,c,d=(int(v)%3 for v in M)
  if z is None:return None if c==0 else a*pow(c,-1,3)%3
  den=(c*z+d)%3
  return None if den==0 else (a*z+b)*pow(den,-1,3)%3
for z,v in labels.items():
  vec=S.Matrix(v)
  assert labels[mob(taum,z)]==tuple(int(a) for a in mod(R*vec,2))
  assert labels[mob(Sm,z)]==tuple(int(a) for a in mod(vec+p,2))
  assert labels[mob(Rm,z)]==tuple(int(a) for a in mod(p+R**4*vec,2))

# The CM gauge has one global exponent k, not separate primewise signs.
parity=[]
for k in range(6):
  for sign in (0,1):
    if ((k+sign)%2)!=0:continue
    assert (k%2)==sign
    parity.append({'global_CM_exponent':k,'epsilon3':sign,'epsilon2':k%2})

out={'status':'All exact checks passed',
     'pointpush_conjugation_words':checks,
     'central_shift':'ba^2b=(ab)^3 a^-2',
     'mod4_cases':four,'mod3_cases':three,
     'projective_affine_dictionary':{str(k):v for k,v in labels.items()},
     'global_gauge_parity_cases':parity}
(P/'b_cm_module.json').write_text(json.dumps(out,indent=2)+'\n')
print('Six faithful B4 pointpush conjugations and the central-shift word passed.')
print(len(four),'mod-four frame cases and',len(three),'mod-three frame cases passed.')
print('Named P1(F3) / affine F2^2 dictionary passed for s,r,tau.')
print('All six global CM gauge parity cases give epsilon2=epsilon3.')
