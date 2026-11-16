#!/usr/bin/env python3
"""Bounded exact free-word old-zero test on the 64 actual nodal seeds.
This tests literal conjugacy, not augmented incidence or truncated orbits.
"""
from pathlib import Path
import json,hashlib,time
ROOT=Path(__file__).resolve().parents[2]
P=ROOT/'work_CE/next_symmetric_nodes/symmetric_paired_fox_data.json'
raw=P.read_bytes();D=json.loads(raw)

def red(w):
    r=[]
    for a in w:
        if r and r[-1]==-a:r.pop()
        else:r.append(a)
    return tuple(r)
def inv(w):return tuple(-a for a in reversed(w))
def sub(w,A):return red(b for a in w for b in (A[a] if a>0 else inv(A[-a])))
def peel(w):
    n=0
    while len(w)-2*n>1 and w[n]==-w[-1-n]:n+=1
    return w[:n],w[n:len(w)-n] if n else w
def conjugator(u,v):
    a,c=peel(u);b,d=peel(v)
    if len(c)!=len(d):return None
    if not c:return () if not d else None
    enc=lambda w:''.join(chr(x+64) for x in w)
    j=(enc(c)+enc(c)).find(enc(d))
    if j<0 or j>=len(c):return None
    h=red(b+inv(c[:j])+inv(a))
    assert red(h+u+inv(h))==v
    return h
A={int(k):tuple(v) for k,v in D['old_actions'][0]['geometric_push_paired'].items()}
assert D['old_actions'][0]['index']==0
F={int(k):tuple(v) for k,v in D['paired_involution'].items()}
assert all(sub(A[j],F)==sub(F[j],A) for j in range(1,22))
old=D['retained_paired_indices']
fill={j:((j,) if j in old else ()) for j in range(1,22)}
start=time.monotonic();rows=[]
for row in D['node_columns']:
    r=tuple(row['paired_relator']);ar=sub(r,A);h=conjugator(r,ar)
    rec={'loop_index':row['loop_index'],'local_node_index':row['local_node_index'],
         'physical_labels':row['physical_labels'],'input_word_length':len(r),
         'translated_word_length':len(ar),'literal_fixed_word':ar==r,
         'conjugate':h is not None}
    if h is not None:
        deck=sub(h,fill);k=red(h+inv(deck))
        assert not sub(k,fill)
        rec.update({'exact_conjugator':h,'retained_deck_part':deck,
                    'kernel_part':k,'has_pure_E_coefficient':not deck,
                    'identity':'old0(r)=h*r*h^-1'})
        print('PASS literal orbit identity',row['loop_index'],row['local_node_index'],
              'fixed',ar==r,'h length',len(h),'deck length',len(deck),flush=True)
    rows.append(rec)
out={'scope':__doc__,'input_sha256':hashlib.sha256(raw).hexdigest(),
     'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'rows':rows,'literal_fixed_count':sum(r['literal_fixed_word'] for r in rows),
     'free_conjugacy_count':sum(r['conjugate'] for r in rows),
     'pure_E_coefficient_count':sum(r.get('has_pure_E_coefficient',False) for r in rows),
     'elapsed_seconds':time.monotonic()-start,
     'claims_excluded':['full orbit independence','nonzero H2 syzygy','kappa value','source equality']}
(ROOT/'work_A/old_zero_node_orbit_identities.json').write_text(json.dumps(out,indent=2)+'\n')
print('Completed64 exact checks: fixed',out['literal_fixed_count'],
      'free conjugate',out['free_conjugacy_count'],'pure E',out['pure_E_coefficient_count'])
print('Elapsed seconds',round(out['elapsed_seconds'],6))
