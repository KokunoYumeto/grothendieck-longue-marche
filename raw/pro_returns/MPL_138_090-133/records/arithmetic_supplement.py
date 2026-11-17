"""Additional exact checks for AR03, AR15 and AR18; never mutates source."""
from pathlib import Path
from datetime import datetime, timezone
from itertools import permutations
import hashlib
import json
import sympy as s

root=Path(__file__).resolve().parent.parent
frozen=json.loads((root/'records/frozen_hashes.json').read_text())['sha256']
def hashes():
    return {p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in frozen}
assert hashes()==frozen

z,c=s.symbols('z c')
alpha=(5*c+4)/6
beta=-c/2
H=z**3*(z-1)**2*(z-c)
g=z**2-alpha*z-beta
delta=25*c*c-32*c+16
R=25*c**3-12*c*c-24*c-16
P=-delta*R/s.Integer(7776)
Q=c*(5*c-8)*(25*c**3-6*c*c+8)/s.Integer(2592)
A=(alpha-2)*(alpha-c)+beta+1
D=(alpha-2)*beta-(beta+1)*c
reconstructed=((alpha**3+2*alpha*beta)*A+(alpha**2+beta)*D)*z+beta*(alpha**2+beta)*A+alpha*beta*D
assert s.expand(s.rem(H,g,z)-reconstructed)==0
assert s.expand(A+(5*c*c-10*c-4)/36)==0
a=s.Rational(8,5)
assert Q.subs(c,a)==0
assert P.subs(c,a)==-s.Rational(8,125)
assert delta.subs(c,a)==s.Rational(144,5)
assert s.gcd(R,delta*c*(c-1)*Q)==1

# Cubic-star labelings: right quotient S3/C3; inversion on mu3 switches cosets.
def comp(a,b):
    return tuple(a[b[k]] for k in range(len(a)))
group=list(permutations(range(3)))
C3=[(0,1,2),(1,2,0),(2,0,1)]
cosets={frozenset(comp(a,b) for b in C3) for a in group}
assert len(cosets)==2
conjugation=(0,2,1)
assert all(frozenset(comp(conjugation,a) for a in co)!=co for co in cosets)
assert hashes()==frozen
out={
 'generated_utc':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
 'who':'GPT-6 Astra Pro; inherited effort not exposed; run MPL_138_090-133/arithmetic_research',
 'AR03':{'S3_cardinality':len(group),'C3_cardinality':len(C3),'co_pinning_classes':len(cosets),'conjugation_switches_classes':True},
 'AR15':{'c':'8/5','Q(c)':'0','P(c)':'-8/125','delta(c)':'144/5','gcd_R_localization_denominator':'1'},
 'AR18':{'A':str(s.factor(A)),'D':str(s.factor(D)),'reconstructed_remainder_equals_H_mod_g':True},
 'frozen_source_hashes_unchanged':True,'frozen_file_count':len(frozen)
}
(root/'records/arithmetic_supplement.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False,indent=2))
