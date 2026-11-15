"""Post-freeze mathematical checks, never used to edit the transcription."""
import sympy as s
from pathlib import Path
out=[]
x=s.symbols('x'); f=s.Function('f')(x)
G=lambda h: -2*s.diff(h,x,3)/s.diff(h,x)+3*(s.diff(h,x,2)/s.diff(h,x))**2
out.append('Scan 036, on f-prime nonzero: G(exp(f))-G(f) = '+str(s.simplify(G(s.exp(f))-G(f))))
a1,a2,a3,a4,a6,r,t=s.symbols('a1 a2 a3 a4 a6 r t')
F=t*t+a1*r*t+a3*t-r**3-a2*r*r-a4*r-a6
out.append('Scan 008 diagnostic: -F_r(r,t) = '+str(s.expand(-s.diff(F,r))))
out.append('Scan 008 diagnostic: F_t(r,t) = '+str(s.diff(F,t)))
b2=a1*a1+4*a2;b4=a1*a3+2*a4;b6=a3*a3+4*a6
b8=a1*a1*a6+4*a2*a6-a1*a3*a4+a2*a3*a3-a4*a4
c4=b2*b2-24*b4;c6=-b2**3+36*b2*b4-216*b6
delta=-b2*b2*b8-8*b4**3-27*b6*b6+9*b2*b4*b6
assert s.expand(c4**3-c6**2-1728*delta)==0
out.append('Invariant identity c4^3-c6^2=1728 Delta: verified symbolically.')
for p,subs,label in [
 (3,{a1:0,a2:t,a3:0,a4:-1,a6:0},'y^2=x^3+t*x^2-x'),
 (2,{a1:t,a2:0,a3:1,a4:0,a6:0},'y^2+t*x*y+y=x^3')]:
 C=s.Poly(s.expand(c4.subs(subs)),t, modulus=p).as_expr()
 D=s.Poly(s.expand(delta.subs(subs)),t, modulus=p).as_expr()
 out.append(f'Equal characteristic {p}: {label}; c4={C}, Delta={D}, j={s.factor(C**3/D)}.')
def val(q,p):
 q=s.Rational(q); a,b=abs(int(q.p)),abs(int(q.q)); n=0
 while a and a%p==0:a//=p;n+=1
 while b%p==0:b//=p;n-=1
 return n
for p,subs,label in [
 (3,{a1:0,a2:0,a3:0,a4:1,a6:1},'y^2=x^3+x+1 over Z_3'),
 (2,{a1:2,a2:0,a3:1,a4:0,a6:0},'y^2+2*x*y+y=x^3 over Z_2')]:
 C=c4.subs(subs);D=delta.subs(subs);J=s.cancel(C**3/D)
 out.append(f'Mixed-characteristic caution: {label}; c4={C}, Delta={D}, j={J}, v_p(Delta)={val(D,p)}, v_p(j)={val(J,p)}.')
report='\n'.join(out)+'\n'
Path(__file__).with_name('calculation_results.txt').write_text(report)
print(report)
