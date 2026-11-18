"""Post-freeze mathematical computations; never reads or writes transcription."""
import sympy as S
from pathlib import Path
from datetime import datetime,timezone
out=[]
def record(key,expr,expected=0):
    residual=S.factor(S.cancel(expr-expected))
    assert residual==0,(key,residual)
    out.append(f'{key}\tPASS\tresidual = {residual}')
t=S.symbols('t',nonzero=True)
f=S.Function('f')(t)
lam=-S.diff(f,t,2)/S.diff(f,t)
G=lambda x1,x2,x3:-2*x3/x1+3*(x2/x1)**2
record('RICCATI_TO_SCHWARZIAN',2*S.diff(lam,t)+lam**2,G(S.diff(f,t),S.diff(f,t,2),S.diff(f,t,3)))
u1,u2,u3,v1,v2,v3=S.symbols('u1 u2 u3 v1 v2 v3',nonzero=True)
record('CHAIN_RULE',G(v1*u1,v2*u1**2+v1*u2,v3*u1**3+3*v2*u1*u2+v1*u3),G(u1,u2,u3)+u1**2*G(v1,v2,v3))
a,b,c,d=S.symbols('a b c d')
h=(a*f+b)/(c*f+d)
record('POSTCOMPOSITION_HOMOGRAPHY',G(S.diff(h,t),S.diff(h,t,2),S.diff(h,t,3)),G(S.diff(f,t),S.diff(f,t,2),S.diff(f,t,3)))
r,k,e=S.symbols('r k e')
la=r/t+k+e*t
expr=S.expand(2*S.diff(la,t)+la**2)
record('LAURENT_DOUBLE_POLE',expr.coeff(t,-2),r*r-2*r)
record('LAURENT_SIMPLE_POLE',expr.coeff(t,-1),2*r*k)
w=S.Function('w')(t)
la2=2*S.diff(w,t)/w
record('RICCATI_LINEARIZATION',2*S.diff(la2,t)+la2**2,4*S.diff(w,t,2)/w)
record('FINAL_SHEAF_COUNTEREXAMPLE',G(S.diff(t*t,t),S.diff(t*t,t,2),S.diff(t*t,t,3)),3/t**2)
record('BAD_WEIGHT_COUNTEREXAMPLE_t_to_t2_s_t',G(1/(2*t),-1/(4*t**3),3/(8*t**5)),-S.Rational(3,4)/t**4)
# For s=t, G_t(s)=0. For tau=t^2, derivatives in tau of sqrt(tau) are the three arguments above.
record('INVERSION_AFFINE_CONNECTION_DIFFERENCE',-S.diff(1/t,t,2)/S.diff(1/t,t),2/t)
x,y,dx,dy=S.symbols('x y dx dy')
record('AFFINE_SHIFT_TRANSITIVITY',2*dx+x*x+2*(dy+x*y)+y*y,2*(dx+dy)+(x+y)**2)
text='UTC '+datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')+'\nSymPy '+S.__version__+'\n'+'\n'.join(out)+'\n\nScope: exact rational symbolic identities in characteristic zero; denominators must be units. Not a proof of global descent, existence of uniformization, or small-characteristic statements.\n'
Path(__file__).with_suffix('.txt').write_text(text)
print(text)
