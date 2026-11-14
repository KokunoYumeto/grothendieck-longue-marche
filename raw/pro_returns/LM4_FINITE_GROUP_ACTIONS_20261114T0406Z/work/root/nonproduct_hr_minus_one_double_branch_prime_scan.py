#!/usr/bin/env python3
"""Finite prime-field diagnostic for the remaining double deleted-coordinate branch."""
from pathlib import Path
from hashlib import sha256
import json

ROOT=Path(__file__).resolve().parents[2]
path=ROOT/'work/root/nonproduct_hr_minus_one_trace_branches.json'
raw=path.read_bytes()
data=json.loads(raw)
rows=next(x['records'] for x in data['records'] if x['branch']=={'u':'1/d','w':'1/d'})
polys={x['index']:x['coefficients'] for x in rows}
primes=[3,5,7,11,13,17,19,23,29,31,37,41,43]
records=[]
def evaluate(poly,values,p):
    return sum(c*pow(values[0],e[0],p)*pow(values[1],e[1],p)*pow(values[2],e[2],p)*pow(values[3],e[3],p) for c,e in poly)%p
for p in primes:
    counts={'d_t_z_cases':0,'nonzero_v_denominator':0,'source1_zero':0,'source10_zero':0,'all_single_traces_zero':0}
    solutions=[]
    for d in range(1,p):
        if d in [1,p-1] or pow((-d)%p,(p-1)//2,p)!=p-1:continue
        A=(d*d-1)%p
        for t in range(1,p):
            for z in range(1,p):
                counts['d_t_z_cases']+=1
                P=(z*((2*A-d)*t*t+1)-A*t*t)%p
                if not P:continue
                counts['nonzero_v_denominator']+=1
                v=A*t*t*z*pow(P,-1,p)%p
                assert v
                if ((z-t)*(d*t*z+1)*v-t*(z-1)*(d*z+1))%p:continue
                counts['source1_zero']+=1
                assert evaluate(polys[1],[d,t,v,z],p)==0 and evaluate(polys[2],[d,t,v,z],p)==0
                if evaluate(polys[10],[d,t,v,z],p):continue
                counts['source10_zero']+=1
                if any(evaluate(polys[i],[d,t,v,z],p) for i in [3,5,7,8]):continue
                assert all(evaluate(poly,[d,t,v,z],p)==0 for poly in polys.values())
                counts['all_single_traces_zero']+=1
                solutions.append({'d':d,'t':t,'v':v,'z':z,'u':pow(d,-1,p),'w':pow(d,-1,p)})
    row={'prime':p,'counts':counts,'solutions':solutions}
    records.append(row)
    print(json.dumps(row),flush=True)
result={'status':'COMPLETED_SPECIFIED_PRIME_FIELD_DIAGNOSTIC',
 'producer_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
 'input':{'path':str(path.relative_to(ROOT)),'bytes':len(raw),'sha256':sha256(raw).hexdigest()},
 'domain':'Exactly the listed prime fields, d!=1,-1, -d nonsquare, and nonzero t,v,z; u=w=1/d.',
 'v_elimination':'Source2 implies v=(d^2-1)*t^2*z/(z*((2*(d^2-1)-d)*t^2+1)-(d^2-1)*t^2). A zero denominator is impossible because its right-hand numerator is nonzero.',
 'records':records,
 'scope':'Finite diagnostic only. No conclusion for unlisted primes, extensions of these fields, common modules, or all-character affine images.'}
output=Path(__file__).with_suffix('.json')
output.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'output':str(output.relative_to(ROOT)),'sha256':sha256(output.read_bytes()).hexdigest()}),flush=True)
