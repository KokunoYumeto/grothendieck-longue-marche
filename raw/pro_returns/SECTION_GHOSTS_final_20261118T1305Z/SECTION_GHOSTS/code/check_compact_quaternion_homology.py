#!/usr/bin/env python3
"""Reconstruct the actual rank-73 faithful homology map and its exact kernel.

The in-run E203 reconstruction is rerun in a temporary directory.  No
historical matrix file is used, and the stable detector output is not edited.
"""
from pathlib import Path
from collections import deque
from tempfile import TemporaryDirectory
from contextlib import redirect_stdout
import io, runpy, shutil, json, hashlib
import numpy as np

with TemporaryDirectory(prefix='compact-quaternion-homology-') as td:
    cp=Path(td)/'detector.py'
    shutil.copyfile(Path(__file__).with_name('check_compact_quaternion_detector.py'),cp)
    with redirect_stdout(io.StringIO()):state=runpy.run_path(str(cp))
    prior=json.loads(cp.with_suffix('.json').read_text())
assert prior['sha256']=='868ede05a7e14876221494203a607efef6a1d3e982d93207feeac268bdac5d6f'
qmul=state['qmul'];QGEN=state['QGEN'];red=state['red'];invword=state['invword']
mulword=state['mulword'];subst=state['subst'];logword=state['logword']
rref=state['rref'];rank=state['rank'];proj=state['proj'];AUT=state['AUT']
AUTWORDS=state['AUTWORDS'];bracket=state['bracket']

def step(g,a):
    q,x,y=g
    return (qmul(q,QGEN[a]),(x+(1 if a==1 else -1 if a==-1 else 0))%3,(y+(1 if a==2 else -1 if a==-2 else 0))%3)

def groupword(w):
    g=(0,0,0)
    for a in w:g=step(g,a)
    return g

trans={(0,0,0):()};todo=deque([(0,0,0)])
while todo:
    g=todo.popleft()
    for a in (1,2,-1,-2):
        h=step(g,a)
        if h not in trans:trans[h]=trans[g]+(a,);todo.append(h)
assert len(trans)==72
sch=[];edge={}
for g in sorted(trans):
    for a in (1,2):
        h=step(g,a);w=mulword(trans[g],(a,),invword(trans[h]))
        if w:edge[g,a]=len(sch);sch.append(w)
        else:edge[g,a]=None
assert len(sch)==73

def homology(w):
    g=(0,0,0);v=np.zeros(73,dtype=np.int16)
    for a in w:
        h=step(g,a);j=edge[g,a] if a>0 else edge[h,-a]
        if j is not None:v[j]=(v[j]+(1 if a>0 else -1))%3
        g=h
    assert g==(0,0,0)
    return v

for j,w in enumerate(sch):assert np.array_equal(homology(w),np.eye(73,dtype=np.int16)[j])

theta=np.column_stack([proj@logword(w)%3 for w in sch]);assert theta.shape==(14,73)
assert rank(theta)==12
for i in range(73):
    for j in range(i):assert not np.any(bracket(theta[:,i],theta[:,j]))

def conjugation_matrix(w):
    return np.column_stack([homology(mulword(w,t,invword(w))) for t in sch])

dz=conjugation_matrix((1,)*6)
di=conjugation_matrix((1,)*9);dj=conjugation_matrix((2,)*9)
h1=conjugation_matrix((1,)*4);h2=conjugation_matrix((2,)*4)
E=np.eye(73,dtype=np.int16)
assert np.array_equal(dz@dz%3,E)
assert np.array_equal(di@di%3,dz) and np.array_equal(dj@dj%3,dz)
assert np.array_equal(di@dj%3,dz@dj%3@di%3)
assert np.array_equal(h1@h1%3@h1%3,E) and np.array_equal(h2@h2%3@h2%3,E)
assert np.array_equal(h1@h2%3,h2@h1%3)
for a in (h1,h2):
    for b in (dz,di,dj):assert np.array_equal(a@b%3,b@a%3)

pminus=2*(E-dz)%3;pplus=2*(E+dz)%3
assert np.array_equal(pminus@pminus%3,pminus) and np.array_equal(pplus@pplus%3,pplus)
cm=pminus[:,rref(pminus)[1]];cp=pplus[:,rref(pplus)[1]]
assert cm.shape==(73,36) and cp.shape==(73,37)
assert not np.any(theta@(E+dz)%3)
assert np.array_equal(theta@pminus%3,theta)

x=(h1-E)%3;y=(h2-E)%3
aug=np.column_stack([x@x%3@cm%3,x@y%3@cm%3,y@y%3@cm%3])
assert rank(aug)==24 and not np.any(theta@aug%3)
assert rank(theta@cm%3)==12
assert rank(np.column_stack([cp,aug]))==61

# A literal primitive quaternion idempotent, commuting with H.
ep=2*(E+di+dj)%3@pminus%3
assert np.array_equal(ep@ep%3,ep)
cb=ep[:,rref(ep)[1]];assert cb.shape==(73,18)
augm=np.column_stack([x@x%3@cb%3,x@y%3@cb%3,y@y%3@cb%3])
assert rank(augm)==12 and not np.any(theta@augm%3)
assert rank(theta@cb%3)==6

c=(1,2,-1,-2);qc=groupword(c);assert qc==(1,0,0)
seen=set();boundary_words=[]
for g in sorted(trans):
    if g in seen:continue
    partner=(qmul(g[0],qc[0]),g[1],g[2]);seen|={g,partner}
    boundary_words.append(mulword(trans[g],c,c,invword(trans[g])))
assert len(boundary_words)==36
peripheral=np.column_stack([homology(w) for w in boundary_words])
assert rank(peripheral)==35 and not np.any(theta@peripheral%3)

surface_aut=[]
for im,m in zip(AUTWORDS,AUT):
    a=np.column_stack([homology(subst(w,im)) for w in sch]);surface_aut.append(a)
    assert np.array_equal(theta@a%3,m@theta%3)
    assert rank(a)==73

payload={
 'status':'PASS','prior_detector_sha256':prior['sha256'],
 'T_index':72,'T_rank':73,'theta_rank':12,'boundary_lifts':36,'boundary_homology_rank':35,
 'quaternion_plus_dimension':37,'quaternion_minus_dimension':36,
 'augmentation_square_rank_on_minus':24,'theta_rank_on_minus':12,
 'primitive_multiplicity_dimension':18,'augmentation_square_rank_on_primitive':12,
 'theta_rank_on_primitive':6,'kernel_dimension':61,'actual_covariance_maps':4,
 'T_schreier_words':[list(w) for w in sch],'boundary_words':[list(w) for w in boundary_words],
 'theta_14_by_73':theta.tolist(),'deck_z':dz.tolist(),'deck_i':di.tolist(),'deck_j':dj.tolist(),
 'translation_h1':h1.tolist(),'translation_h2':h2.tolist(),
 'minus_basis_73_by_36':cm.tolist(),'primitive_basis_73_by_18':cb.tolist(),
 'augmentation_square_image':aug.tolist(),'primitive_augmentation_square_image':augm.tolist(),
 'peripheral_73_by_36':peripheral.tolist(),'actual_surface_actions':[a.tolist() for a in surface_aut],
}
raw=json.dumps(payload,sort_keys=True,separators=(',',':')).encode()
payload['sha256']=hashlib.sha256(raw).hexdigest()
Path(__file__).with_suffix('.json').write_text(json.dumps(payload,indent=2)+'\n')
print(json.dumps({k:v for k,v in payload.items() if not isinstance(v,list)},indent=2))
