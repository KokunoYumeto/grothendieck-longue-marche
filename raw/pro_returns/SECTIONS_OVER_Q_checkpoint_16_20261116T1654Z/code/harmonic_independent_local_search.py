#!/usr/bin/env python3
"""Actual quartic-cover local tests for independent descent candidates."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import json
from harmonic_tripod_obstruction_search import fourth_roots_units, hilbert, primes, is_square

base=Path(__file__).resolve().parent
data=json.loads((base/'harmonic_descent_direction_candidates.json').read_text())
lines=[]
def emit(s):
    lines.append(str(s));print(s,flush=True)

trials=points=nonzero=0
witnesses=[]
for rec in data['candidates']:
    R,c,r=map(F,(rec['R'],rec['c'],rec['r']))
    char=2*r
    if is_square(char):
        emit(f'd={rec["d"]}: character is a rational square; exact symbol zero.')
        continue
    D=[c/R,(c-1)/(R-1),(c-F(1,2))/(R-F(1,2))]
    assert D[0]*D[1]*D[2]==-r*r
    boundary=[(1/(1-R),1/(1-2*R)),(1/R,1/(2*R-1)),(1/(2*R),1/(2*(1-R)))]
    assert not any(is_square(-a) or is_square(-b) or is_square(-a*b) for a,b in boundary)
    S={2,3}
    for value in [R,R-1,R-F(1,2),c,c-1,c-F(1,2),R-c,char]:S|=primes(value)
    used=[];localnz=0
    for p in sorted(S):
        if p>10000:continue
        used.append(p)
        limit=4096 if p==2 else min(p*p,2000)
        candidates=[F(x) for x in range(1,limit+1)]
        candidates += [F(x,p**h) for h in (1,2) for x in range(1,min(p*p,2000)) if x%p]
        for X in candidates:
            T=R*X**4
            if T in (0,F(1,2),1,c):continue
            trials+=1
            Ys=fourth_roots_units((T-1)/(R-1),p)
            if not Ys:continue
            Zs=fourth_roots_units((T-F(1,2))/(R-F(1,2)),p)
            if not Zs:continue
            points+=1
            f=(T-c)/(R-c)
            if not hilbert(f,char,p):continue
            nonzero+=1;localnz+=1
            for Y,Z in product(Ys,Zs):
                symbols=[[hilbert(W,a,p),hilbert(W,b,p)] for W,(a,b) in zip((X,Y,Z),boundary)]
                if any(any(row) for row in symbols):continue
                witness={**rec,'p':p,'X':str(X),'T':str(T),'Y_root_representative':str(Y),
                         'Z_root_representative':str(Z),'normalized_function':str(f),
                         'boundary_symbols':symbols,'D':list(map(str,D))}
                witnesses.append(witness)
                emit('EXACT LOCAL WITNESS '+json.dumps(witness))
                break
            if witnesses:break
        if witnesses:break
    emit(f'd={rec["d"]}: tested primes={used}; nonzero evaluations={localnz}.')
    if witnesses:break
emit(f'trials={trials}; actual local points={points}; nonzero evaluations={nonzero}; compatible witnesses={len(witnesses)}')
emit('Finite exact search only; no general vanishing or nonexistence assertion.')
(base/'harmonic_independent_local_search_output.txt').write_text('\n'.join(lines)+'\n')
(base/'harmonic_independent_local_witnesses.json').write_text(json.dumps(witnesses,indent=2)+'\n')
