"""Exact finite evaluations of the two supplied Hom argument orders.

These are explicitly assigned finite sets and all set functions between them.
They do not identify the manuscript's undefined P or looped E with a structure.
No general or conditional theorem is asserted by this computation.
"""
from itertools import product
from pathlib import Path
from datetime import datetime, timezone
import json

R = Path(__file__).resolve().parents[1]
X = ('x',)
Z = ('z0','z1')
E = ('e0','e1','e2')
ZX = tuple(product(Z,X))
# Function values are tuples in the displayed domain order.
A = tuple(product(E, repeat=len(ZX)))
EZ = tuple(product(E, repeat=len(Z)))
B = tuple(product(EZ, repeat=len(X)))
ZE = tuple(product(Z, repeat=len(E)))
C = tuple(product(ZE, repeat=len(X)))

def transpose(a):
    return (a,)

def untranspose(b):
    return b[0]

def projection(a):
    n = A.index(a) % 8
    values = tuple(Z[(n >> shift) & 1] for shift in (2,1,0))
    return (values,)

rows = [{'a':a, 'T(a)':transpose(a), 'R(a)':projection(a)} for a in A]
results = {
    'sets': {'X':X,'Z':Z,'E':E,'Z_times_X_order':ZX},
    'spaces': {'A':'Hom(Z × X,E)','B':'Hom(X,Hom(Z,E))','C':'Hom(X,Hom(E,Z))'},
    'sizes': {'A':len(A),'B':len(B),'C':len(C)},
    'T_definition':'T(a)=(a,), with T(a)(x)(z)=a(z,x)',
    'T_inverse_definition':'T_inv(b)=b[0], with T_inv(b)(z,x)=b(x)(z)',
    'T_image_equals_B':set(map(transpose,A))==set(B),
    'T_inverse_after_T':all(untranspose(transpose(a))==a for a in A),
    'T_after_inverse':all(transpose(untranspose(b))==b for b in B),
    'R_definition':'Lexicographic index n of a in A; use the three binary digits of n mod 8 as indices into Z, in E order, and wrap the resulting inner function in the single X-tuple.',
    'R_image_equals_C':set(map(projection,A))==set(C),
    'R_collision':{'first':A[0],'last':A[8],'common_image':projection(A[0]),'verified':projection(A[0])==projection(A[8])},
    'rows':rows,
}
assert results['sizes']=={'A':9,'B':9,'C':8}
assert all(results[k] for k in ['T_image_equals_B','T_inverse_after_T','T_after_inverse','R_image_equals_C'])
assert results['R_collision']['verified']
now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
results['executed_utc']=now
(R/'checks/scan011_finite_functions.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
who='GPT-6 Astra Pro; effort inherited, separately verifiable setting not exposed; run /root'
events=[
 {'statement_id':'81-011-N1','date':now,'who':who,'type':'computation or formal certificate','outcome':'With X={x}, Z={z0,z1}, E={e0,e1,e2}, enumerate all set functions. A=Hom(Z×X,E) and B=Hom(X,Hom(Z,E)) each have9 elements. T(a)(x)(z)=a(z,x), inverse b→((z,x)→b(x)(z)); all9 elements satisfy both inverse equations and T(A)=B. Exact tables in checks/scan011_finite_functions.json.'},
 {'statement_id':'81-011-N2','date':now,'who':who,'type':'computation or formal certificate','outcome':'For the same assigned finite sets, C=Hom(X,Hom(E,Z)) has8 elements. The explicitly computed map R:A→C converts the lexicographic index n modulo8 to three Z-values in E order. Its image is all8 elements of C; the first and last elements of A have the same image. This finite computation leaves the manuscript structures and ink readings unassigned.'}
]
(R/'checks/scan011_check_events.json').write_text(json.dumps(events,ensure_ascii=False,indent=2)+'\n')
lines=['# Scan011 — finite Hom argument-order computation','',
f'Executed: {now}.','',
'Assign X={x}, Z={z0,z1}, E={e0,e1,e2}. Hom here is the explicitly enumerated set of all functions between these finite sets. A function is recorded by its ordered tuple of values. This calculation does not assign a meaning to the manuscript’s P or looped E; it selects no ink reading.','',
'A=Hom(Z×X,E) has9 elements. B=Hom(X,Hom(Z,E)) has9 elements. The exact map T(a)(x)(z)=a(z,x) and inverse T⁻¹(b)(z,x)=b(x)(z) were enumerated over every element; both compositions returned the input.','',
'C=Hom(X,Hom(E,Z)) has8 elements. The additional exact map R:A→C is given in the table: number A lexicographically from0 through8, reduce that index modulo8, and read its three binary digits as indices into Z in the order e0,e1,e2. Its image equals C. Its first and last input have the same image.','',
'| a, values on (z0,x),(z1,x) | T(a), the single inner function’s values on z0,z1 | R(a), the single inner function’s values on e0,e1,e2 |',
'| --- | --- | --- |']
for row in rows:lines.append(f"| {row['a']} | {row['T(a)'][0]} | {row['R(a)'][0]} |")
lines+=['','The records N1 and N2 report these finite computations. They provide no general certification of the manuscript expressions and no reason to replace a written argument by an expected one.']
(R/'checks/scan011_finite_functions.md').write_text('\n'.join(lines)+'\n')
print(json.dumps({'executed_utc':now,'sizes':results['sizes'],'inverse_checks':True,'explicit_projection_image':8,'events':2}))
