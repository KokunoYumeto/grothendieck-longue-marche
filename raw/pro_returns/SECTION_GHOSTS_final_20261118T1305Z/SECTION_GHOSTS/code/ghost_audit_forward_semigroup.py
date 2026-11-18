#!/usr/bin/env python3
"""Exploratory forward cube/complement orbit, superseded by E192.

This was an attempted route to point/cusp separation.  These finite
observations are not a proof of an orbit theorem or of section separation.
"""
from collections import deque

for p in [5,11,17,23,29,41,47,53,59,71,83,107,131,167,191,227]:
    def mul(a,b):
        x,y=a
        z,w=b
        return ((x*z-y*w)%p,(x*w+y*z-y*w)%p)

    # F_p[z]/(z²+z+1), with z a primitive cube root.
    seen={(0,0),(1,0),(0,1),(-1%p,-1%p)}
    todo=deque(seen)
    while todo:
        a=todo.popleft()
        for b in [mul(mul(a,a),a),((1-a[0])%p,-a[1]%p)]:
            if b not in seen:
                seen.add(b)
                todo.append(b)
    prime=[a for a in range(p) if (a,0) in seen]
    print(p,len(seen),len(prime),prime if len(prime)<p else 'all')

print('Exploratory only. E192 proves separation by a different elliptic representation.')
