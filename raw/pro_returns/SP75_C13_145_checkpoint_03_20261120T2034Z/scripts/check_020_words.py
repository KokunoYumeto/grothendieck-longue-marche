"""Local word checks in <s,r | s^2=r^3=1>; no image reading is automated."""
from pathlib import Path
import json
E=Path(__file__).resolve().parents[1]
def red(word):
    out=[]
    for g,e in word:
        modulus=2 if g=='s' else 3
        e%=modulus
        if not e:continue
        if out and out[-1][0]==g:
            e=(out.pop()[1]+e)%modulus
        if e:out.append((g,e))
    return tuple(out)
def prod(*words):return red(x for w in words for x in w)
def inv(w):return red((g,-e) for g,e in reversed(w))
s=(('s',1),);r=(('r',1),);ri=inv(r)
s0=s;s1=prod(r,s,ri);si=prod(ri,s,r)
l0=prod(ri,s0,s1);l1=prod(ri,s1,si);li=prod(ri,si,s0)
checks=[]
for name,lhs,rhs in [
    ('l0=r^-1 s r s r^-1',l0,prod(ri,s,r,s,ri)),
    ('l1=(s r)^2',l1,prod(s,r,s,r)),
    ('linfinity=(r s)^2',li,prod(r,s,r,s)),
    ('relation4 linfinity l1 l0=1',prod(li,l1,l0),()),
    ('s l1 s=linfinity',prod(s,l1,s),li),
    ('s linfinity s=l1',prod(s,li,s),l1),
    ('s l0 s=linfinity^-1 l1^-1',prod(s,l0,s),prod(inv(li),inv(l1)))]:
    checks.append({'claim':name,'left_reduced':lhs,'right_reduced':rhs,'equal':lhs==rhs})
    assert lhs==rhs
candidate=prod(ri,s,ri,s)
checks.append({'claim':'C candidate linfinity=(r^-1 s)^2','left_reduced':li,'candidate_reduced':candidate,'equal':li==candidate,'scope':'Candidate comparison only; the ink must decide which exponent is actually written.'})
out={'encoding':'s=sigma0, r=rho. Each pair records a generator and exponent modulo2 for s or modulo3 for r. Only adjacent equal-generator syllables merge; zero exponents cancel. sigma1=r s r^-1 and sigmainfinity=r^-1 s r.','checks':checks}
(E/'reader_reports/145_scan020_word_check.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out))
