"""Exhaustive 1-cocycle check for GL2(F2) on its natural module."""
from itertools import product
from pathlib import Path
from datetime import datetime,timezone
import json
G=[m for m in product(range(2),repeat=4) if (m[0]*m[3]-m[1]*m[2])%2]
def multiply(m,n):
 a,b,c,d=m;e,f,g,h=n
 return ((a*e+b*g)%2,(a*f+b*h)%2,(c*e+d*g)%2,(c*f+d*h)%2)
def act(m,v):
 x,y=v%2,v//2;a,b,c,d=m
 return ((a*x+b*y)%2)+2*((c*x+d*y)%2)
index={g:i for i,g in enumerate(G)}
cochains=product(range(4),repeat=6)
cocycles=[f for f in cochains if all(f[index[multiply(g,h)]]==f[index[g]]^act(g,f[index[h]]) for g in G for h in G)]
coboundaries={tuple(act(g,v)^v for g in G) for v in range(4)}
assert set(cocycles)==coboundaries and len(cocycles)==4
out={'checked_at_utc':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),'group_order':len(G),'cochains_examined':4**6,'cocycles':len(cocycles),'coboundaries':len(coboundaries),'H1_cardinality':1,'complements_in_V_semidirect_G':4}
Path(__file__).with_name('complements_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
