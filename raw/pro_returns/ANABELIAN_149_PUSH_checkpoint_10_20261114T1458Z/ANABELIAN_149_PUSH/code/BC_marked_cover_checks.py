"""Finite group and small-type arithmetic checks for B.11d."""
import json
from fractions import Fraction
from pathlib import Path

p=5
one=(0,0,0)
def mul(x,y):
    return ((x[0]+y[0])%p,(x[1]+y[1])%p,(x[2]+y[2]+x[0]*y[1])%p)
def inv(x):
    return ((-x[0])%p,(-x[1])%p,(-x[2]+x[0]*x[1])%p)
def power(x,n):
    out=one
    for _ in range(n): out=mul(out,x)
    return out

checks=[]
def check(name,condition,detail):
    assert condition,name
    checks.append(dict(name=name,passed=True,detail=detail))
a=(1,0,0)
b=(0,1,0)
c=mul(mul(mul(a,b),inv(a)),inv(b))
check('Single cusp commutator survives',c==(0,0,1) and power(c,5)==one,
      {'commutator':c,'order':5})
seen={one}
todo=[one]
while todo:
    x=todo.pop()
    for y in (a,b,inv(a),inv(b)):
        z=mul(x,y)
        if z not in seen: seen.add(z);todo.append(z)
check('Two generators generate the Heisenberg group',len(seen)==125,{'order':len(seen)})
for g,nu,degree,expected in [(0,3,25,6),(0,4,125,76),(1,1,125,51),(2,0,1,2)]:
    twice=degree*(2*g-2+nu*(1-Fraction(1,5)))
    genus=1+twice/2
    check(f'Proper-cover genus for type ({g},{nu})',genus==expected and genus>=2,
          {'degree':degree,'ramification_at_each_cusp':5 if nu else None,'genus':int(genus),
           'scope':'Starting quotient before characteristic core; the proof establishes the general lower bound.'})
out=dict(script=Path(__file__).name,passed=len(checks),checks=checks)
Path(__file__).with_name('BC_marked_cover_checks_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'passed':len(checks),'all_passed':True}))
