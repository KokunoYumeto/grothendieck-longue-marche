"""Literal positive braid-word certificates for the E183 marking.

Every edge is one defining braid relation or one disjoint commutation.
No finite quotient of B4 is substituted for a word equality.
"""
from collections import deque
from hashlib import sha256
from pathlib import Path
import json


def neighbors(word):
    for i in range(len(word)-1):
        if abs(word[i]-word[i+1]) > 1:
            yield word[:i]+(word[i+1],word[i])+word[i+2:]
    for i in range(len(word)-2):
        a,b,c=word[i:i+3]
        if a==c and abs(a-b)==1:
            yield word[:i]+(b,a,b)+word[i+3:]


def certificate(start,finish):
    assert len(start)==len(finish)
    parents=[{start:None},{finish:None}]
    fronts=[{start},{finish}]
    meet=start if start==finish else None
    while meet is None:
        side=0 if len(fronts[0])<=len(fronts[1]) else 1
        new=set()
        for w in sorted(fronts[side]):
            for v in neighbors(w):
                if v in parents[side]:
                    continue
                parents[side][v]=w
                new.add(v)
                if v in parents[1-side]:
                    meet=v
                    break
            if meet is not None:
                break
        assert new or meet is not None,'No relation path found'
        fronts[side]=new
    left=[]; w=meet
    while w is not None:
        left.append(w);w=parents[0][w]
    left.reverse()
    right=[];w=parents[1][meet]
    while w is not None:
        right.append(w);w=parents[1][w]
    path=left+right
    assert path[0]==start and path[-1]==finish
    assert all(v in set(neighbors(w)) for w,v in zip(path,path[1:]))
    return [''.join(map(str,w)) for w in path]


a=(1,); b=(2,); c=(3,)
omega=(1,2)*3
Omega=(1,2,3)*4
y3=(2,1,1,2)
claims={
    'omega_times_c_squared_is_full_twist_times_a_squared':
        (omega+c+omega+c,Omega+a+a),
    'mixed_I2_4_relation':(c+omega+c+omega,omega+c+omega+c),
    'y3_is_omega_a_inverse_squared':(a+a+y3,omega),
    'omega_commutes_with_a':(omega+a,a+omega),
    'c_commutes_with_a':(c+a,a+c),
}
paths={key:certificate(*pair) for key,pair in claims.items()}
data={
    'scope':'Exact defining-relation paths in the positive braid monoid B4; no GT source enumeration.',
    'claims':len(paths),
    'total_relation_steps':sum(len(path)-1 for path in paths.values()),
    'paths':paths,
}
canonical=json.dumps(data,sort_keys=True,separators=(',',':')).encode()
data['sha256']=sha256(canonical).hexdigest()
Path(__file__).with_suffix('.json').write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps({k:v for k,v in data.items() if k!='paths'},indent=2))
