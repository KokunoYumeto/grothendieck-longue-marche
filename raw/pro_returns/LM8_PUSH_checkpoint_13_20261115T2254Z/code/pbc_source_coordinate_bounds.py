"""Independently derive diagonal power bounds from an original pc source."""
import math


def extended_gcd(a,b):
    if b==0:
        return abs(a), (1 if a>0 else -1), 0
    g,x,y=extended_gcd(b,a%b)
    return g,y,x-(a//b)*y


def coordinate_bounds(source):
    orders=source['relative_orders'];n=len(orders);N=math.prod(orders)
    con=source.get('conjugates_nested')
    if con is None:
        con=[[] for _ in orders]
        for i,j,w in source['conjugates']:
            assert len(con[i-1])==j-1
            con[i-1].append(w)
    bounds=[N]*(n*(n+1)//2)
    proofs={}
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            if con[j-1][i-1]!=[j,1]:
                continue
            idx=j*(j-1)//2+1+i
            rows=[]
            if source['powers'][j-1]==[]:
                rows.append({'meta':[3,i,j],'value':orders[j-1]})
            if source['powers'][i-1]==[]:
                rows.append({'meta':[4,i,j],'value':-orders[i-1]})
            if not rows:
                continue
            d=abs(rows[0]['value']);coeff=[1 if rows[0]['value']>0 else -1]
            for row in rows[1:]:
                g,u,v=extended_gcd(d,row['value'])
                coeff=[u*c for c in coeff]+[v];d=g
            assert d>0 and N%d==0
            assert sum(c*r['value'] for c,r in zip(coeff,rows))==d
            bounds[idx-1]=d
            if d<N:
                proofs[idx]={'bound':d,'rows':[
                    dict(r,coefficient=c) for c,r in zip(coeff,rows) if c]}
    return bounds,proofs
