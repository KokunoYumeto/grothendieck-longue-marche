"""Exact research checks of frozen cote138, scans104--112.

No image access and no transcription mutation. SymPy performs exact polynomial
arithmetic; the finite permutation enumeration uses plain Python tuples.
"""
from pathlib import Path
from datetime import datetime, timezone
from itertools import permutations
import hashlib,json,csv
import sympy as s

ROOT=Path(__file__).resolve().parent.parent
PREFIX='MPL_138_090-133'
frozen=json.loads((ROOT/'records/frozen_hashes.json').read_text())['sha256']
before={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in frozen}
assert before==frozen
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
z,c,x,y,t=s.symbols('z c x y t',real=True)
H=z**3*(z-1)**2*(z-c)
g=z**2-(5*c+4)*z/6+c/2
delta=25*c**2-32*c+16
R=25*c**3-12*c**2-24*c-16
P=-delta*R/s.Integer(7776)
Q=c*(5*c-8)*(25*c**3-6*c**2+8)/s.Integer(2592)
B=z**2+(2*c-2)*z/3+(5*c**2-4*c-4)/12
T=(-5*c**2-30*c*z**2+36*c*z-4*c+24*z**3-24*z**2)/s.Integer(2592)
assert s.expand(s.diff(H,z)-6*z**2*(z-1)*g)==0
assert s.expand(s.rem(H,g,z)-P*z-Q)==0
assert s.expand(H-Q-g*g*B-R*T)==0
assert s.gcd(P,Q)==1
assert s.gcd(R,delta)==1
assert s.gcd(R,Q)==1
assert s.gcd(R,c*(c-1))==1
assert s.expand(P).coeff(c,5)==-s.Rational(1,6)*s.Rational(5,6)**4
assert P.subs(c,0)==s.Rational(8,243)
assert P.subs(c,1)==s.Rational(1,32)
assert s.discriminant(delta,c)==-576
delta_roots=[s.Rational(16,25)+e*s.Rational(12,25)*s.I for e in [-1,1]]
written_roots=[s.Rational(16,25)+e*s.Rational(24,25)*s.I for e in [-1,1]]
assert all(s.simplify(delta.subs(c,a))==0 for a in delta_roots)
assert all(s.simplify(delta.subs(c,a))!=0 for a in written_roots)
# At each discarded delta-root, one extra critical point has multiplicity2,
# and therefore ramification index3. It is not a valid pair of simple critical
# points u,v, even though P=0 and Q!=0 hold there.
degenerate=[]
for a in delta_roots:
 u=s.simplify((5*a+4)/12)
 f=s.cancel(H.subs(c,a)/Q.subs(c,a))
 assert s.simplify(f.subs(z,u)-1)==0
 assert s.simplify(s.diff(f,z).subs(z,u))==0
 assert s.simplify(s.diff(f,z,2).subs(z,u))==0
 assert s.simplify(s.diff(f,z,3).subs(z,u))!=0
 degenerate.append({'c':str(a),'u=v':str(u),'third_derivative':str(s.simplify(s.diff(f,z,3).subs(z,u))),
                    'passport':[[3,2,1],[3,1,1,1],[6]]})
discB=s.factor(s.discriminant(B,z)); resBg=s.factor(s.resultant(B,g,z))
assert s.resultant(R,discB,c)==-256
assert s.resultant(R,resBg,c)==91125
residues_mod7=[int(R.subs(c,k))%7 for k in range(7)]
assert 0 not in residues_mod7
assert s.discriminant(R,c)==-3*1296**2
cp=(4+18*t+6*t*t)/25
tp=-25*c*c/36+31*c/18+s.Rational(2,9)
assert s.rem(R.subs(c,cp),t**3-2,t)==0
assert s.rem(tp.subs(c,cp)-t,t**3-2,t)==0
assert s.rem(cp.subs(t,tp)-c,R,c)==0
assert s.rem(tp**3-2,R,c)==0
assert s.expand(s.rem(Q,R,c)+(c*c+52*c-32)/1500)==0

def fiber_partition(f,value):
 num,den=s.fraction(s.cancel(f))
 degree=max(s.degree(num,z),s.degree(den,z))
 p=den if value=='infinity' else s.expand(num-value*den)
 part=[]
 for fac,m in s.factor_list(p,z)[1]:part += [int(m)]*int(s.degree(fac,z))
 at_infty=degree-s.degree(p,z)
 if at_infty:part.append(int(at_infty))
 assert sum(part)==degree
 return sorted(part,reverse=True)
small_maps=[('identity',z,[[1],[1],[1]]),('square',z*z,[[2],[1,1],[2]]),
 ('quadratic_segment',-4*z*(z-1),[[1,1],[2],[2]]),
 ('quadratic_loop',z*z/(4*(z-1)),[[2],[2],[1,1]]),
 ('cubic_star',z**3,[[3],[1,1,1],[3]]),
 ('cubic_loop_tail',4*z**3/(27*(z-1)),[[3],[2,1],[2,1]]),
 ('cubic_dual',27*z*(z-1)**2/4,[[2,1],[2,1],[3]])]
small_results=[]
for name,f,expected in small_maps:
 actual=[fiber_partition(f,k) for k in [0,1,'infinity']]
 assert actual==expected
 small_results.append({'name':name,'f':str(f),'passport_0_1_infty':actual,
                       'derivative':str(s.factor(s.diff(f,z))), 'f_minus_one':str(s.factor(f-1))})
fc=4*z**3/(27*(z-1))
imag=s.factor(s.im(fc.subs(z,x+s.I*y)))
expected_imag=4*y*(2*x*(x*x+y*y)-3*x*x+y*y)/(27*((x-1)**2+y*y))
assert s.simplify(imag-expected_imag)==0

# Convention: (a*b)(i)=a(b(i)), on labels1,...,6 stored at indices0,...,5.
def comp(a,b):return tuple(a[b[i]] for i in range(len(a)))
def inv(a):return tuple(a.index(i) for i in range(len(a)))
def conj(a,b):return comp(comp(a,b),inv(a))
def cycletype(a):
 seen=set();out=[]
 for i in range(len(a)):
  if i in seen:continue
  j=i;n=0
  while j not in seen:seen.add(j);n+=1;j=a[j]
  out.append(n)
 return sorted(out,reverse=True)
def cycles(a):
 seen=set();out=[]
 for i in range(len(a)):
  if i in seen:continue
  j=i;part=[]
  while j not in seen:seen.add(j);part.append(j+1);j=a[j]
  out.append(part)
 return out
def generated(*gens):
 unit=tuple(range(len(gens[0])));known={unit};todo=[unit]
 while todo:
  a=todo.pop()
  for b in gens:
   ab=comp(a,b)
   if ab not in known:known.add(ab);todo.append(ab)
 return known
rho=(1,2,0,4,3,5)
sigmaI=(3,1,5,0,4,2)
sigmaII=(3,1,2,0,5,4)
phiI=(4,0,5,2,3,1)
phiII=(4,0,1,2,5,3)
assert comp(inv(rho),sigmaI)==phiI
assert comp(inv(rho),sigmaII)==phiII
assert cycletype(phiI)==[6] and cycletype(phiII)==[6]
assert comp(comp(rho,rho),rho)==(0,1,2,4,3,5)
G_I=generated(rho,sigmaI);G_II=generated(rho,sigmaII)
assert len(G_I)==len(G_II)==720
all_perms=list(permutations(range(6)))
centralizer=[a for a in all_perms if comp(a,rho)==comp(rho,a)]
assert len(centralizer)==6
valid=[sig for sig in all_perms if cycletype(sig)==[2,2,1,1] and cycletype(comp(inv(rho),sig))==[6]]
def canonical(sig):return min(conj(a,sig) for a in centralizer)
classes={canonical(sig) for sig in valid}
assert len(valid)==18 and len(classes)==3
theta=(0,2,1,3,4,5)
assert conj(theta,inv(rho))==rho
assert canonical(conj(theta,sigmaI))!=canonical(sigmaI)
assert canonical(conj(theta,sigmaII))==canonical(sigmaII)
assert classes=={canonical(sigmaI),canonical(sigmaII),canonical(conj(theta,sigmaI))}
ambiguous_bad=(1,2,0,4,1,5)
assert len(set(ambiguous_bad))<6

beza,bezb,bezc=s.gcdex(P,Q,c)
assert s.expand(beza*P+bezb*Q)==1
certificate={
 'generated_utc':now,'model':'GPT-6 Astra Pro; inherited effort not exposed; run MPL_138_090-133/arithmetic_research',
 'sympy_version':s.__version__,'source_hashes_before':before,
 'definitions':{str(k):str(v) for k,v in {'H':H,'g':g,'P_remainder':s.factor(P),'Q_remainder':s.factor(Q),'delta':delta,'R_admissible':R,'B_residual':B,'T_division_error':T}.items()},
 'identities':['H_prime=6*z^2*(z-1)*g','rem_z(H,g)=P*z+Q','H-Q=g^2*B+R*T','P=-delta*R/7776'],
 'endpoint_checks':{'P(0)':str(P.subs(c,0)),'P(1)':str(P.subs(c,1)),'gcd(P,Q)':'1','bezout_A':str(beza),'bezout_B':str(bezb)},
 'delta_roots':[str(a) for a in delta_roots],'literal_written_root_values_in_delta':[str(s.simplify(delta.subs(c,a))) for a in written_roots],
 'degenerate_delta_locus':degenerate,
 'admissible_checks':{'R_mod7_values':residues_mod7,'disc_R':str(s.discriminant(R,c)),'res_R_delta':str(s.resultant(R,delta,c)),
   'res_R_Q':str(s.resultant(R,Q,c)),'disc_B':str(discB),'res_R_discB':'-256','res_R_resBg':'91125','Q_mod_R':str(s.factor(s.rem(Q,R,c))),
   'c_in_t':str(cp),'t_in_c':str(tp),'R_at_c_in_t':str(s.factor(R.subs(c,cp)))},
 'small_maps':small_results,'barycentric_imaginary_part':str(imag),
 'permutations':{'convention':'a*b applies b first','rho_s':cycles(rho),'sigma_I':cycles(sigmaI),'sigma_II':cycles(sigmaII),
   'rho_f_I':cycles(phiI),'rho_f_II':cycles(phiII),'group_orders':[len(G_I),len(G_II)],'centralizer_rho_order':len(centralizer),
   'admissible_involutions':len(valid),'simultaneous_conjugacy_classes':len(classes),'orbit_sizes':[sum(canonical(sig)==cl for sig in valid) for cl in sorted(classes)],
   'class_representatives':[cycles(cl) for cl in sorted(classes)],'I_mirror_distinct':True,'II_mirror_fixed':True,
   'table_II_alternative_r5_to_r2_not_bijective':True},
}
after={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in frozen}
assert after==before==frozen
certificate['frozen_source_hashes_unchanged']=True
(ROOT/'records/arithmetic_certificate.json').write_text(json.dumps(certificate,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:certificate[k] for k in ['generated_utc','definitions','endpoint_checks','delta_roots','admissible_checks','permutations','frozen_source_hashes_unchanged']},ensure_ascii=False,indent=2))
