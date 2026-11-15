"""Audited independent EK certificates for all 24 CM characters.

Run after, or together with, de_ek_explore.py and de_ek_twist_explore.py.
No modular-symbol data are read. Every output residue is an exact residue
modulo 25 in the indicated algebra. See E.1 for the measure, ray-orbit,
period-unit, precision and Rubin specialization proofs.
"""
from pathlib import Path
import json, subprocess, sys
from sympy import kronecker_symbol
root=Path(__file__).resolve().parent
for name in ('de_ek_explore.py','de_ek_twist_explore.py'):
 p=subprocess.run([sys.executable,str(root/name)],text=True,capture_output=True,check=True)
 (root/name).with_suffix('.out').write_text(p.stdout+p.stderr)
U=[(1,0),(0,1),(-1,0),(0,-1)]
def mul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def primary(z):return z[0]%2==1 and z[1]%2==0 and (z[0]+z[1]-1)%4==0
def eps6(z):
 us=[u for u in U if primary(mul(u,z))]
 assert len(us)==1
 c=int(kronecker_symbol(24,z[0]**2+z[1]**2))
 assert c in (-1,1)
 return tuple(c*x for x in us[0])
def mr(a,b):return tuple(x%12 for x in mul(a,b))
units=[(a,b) for a in range(12) for b in range(12) if (a+b)%2 and (a%3 or b%3)]
ker=[z for z in units if eps6(z)==(1,0)]
assert len(units)==64 and len(ker)==16
assert all(eps6(mr(a,b))==mul(eps6(a),eps6(b)) for a in units for b in units)
assert all(mr(a,b) in ker for a in ker for b in ker)
assert eps6((7,6))==(-1,0) # 1 modulo (6+6i), excludes conductor (1+i)^3(3)
assert eps6((1,4))==(-1,0) # 1 modulo (4), excludes omission of (3)
assert all(eps6(u)==(u[0],-u[1]) for u in U)
a=json.loads((root/'de_ek_explore.json').read_text())['rows']
b=json.loads((root/'de_ek_twist_explore.json').read_text())['rows']
mapb={(r['m'],r['t']):r for r in b}
rows=[]
for d in (1,6):
 for r in a:
  m,t=r['m'],r['t'];s=mapb[m,t] if d==6 and m%2 else r
  key='trace_restricted_moment_without_unit_period_mod25' if d==6 and m%2 else 'unit_restricted_moment_without_period_mod25'
  val=s[key];assert val%25
  z={'d':d,'m':m,'t':t,'A':19-t,'B':m+t,'residue_mod25':val,'exact_5_adic_valuation':int(val%5==0)}
  rows.append(z);print(json.dumps(z))
out={'precision':25,'exponent_congruence':20,
 'error_bound':'25 times the ring of integers; period, ray multiplicity and N(f)^B are units',
 'finite_character':{'unit_group_order':64,'kernel_order':16,'kernel':ker,
 'conductor_P4_witness':[7,6],'conductor_3_witness':[1,4]},
 'character_at_moment':'psi^(-t) barpsi^(-m-t), conjugate of the requested character',
 'rows':rows}
(root/'de_ek_certificates.json').write_text(json.dumps(out,indent=2)+'\n')
