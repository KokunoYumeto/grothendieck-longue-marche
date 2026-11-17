#!/usr/bin/env python3
"""Exact lower-collar cone whisker in the original positive cut marking."""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2];P=ROOT/'work_CE/next_symmetric_nodes'
def add(z,w):return (z[0]+w[0],z[1]+w[1])
def neg(z):return (-z[0],-z[1])
def minus(z,w):return add(z,neg(w))
def cmul(z,w):return (z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0])
def cdiv(z,w):
    d=w[0]*w[0]+w[1]*w[1]
    return cmul(z,(w[0]/d,-w[1]/d))
def scale(a,z):return (a*z[0],a*z[1])
def pt(x,y=0):return (F(x),F(y))
ROT=pt(1,F(371,1000));q=pt(F(4,5),F(1,2));den=10**30
u=[pt(F(309016994374947424102293417183,den),F(951056516295153572116439333379,den)),
   pt(F(-809016994374947424102293417183,den),F(587785252292473129168705954639,den)),
   pt(F(-809016994374947424102293417183,den),F(-587785252292473129168705954639,den)),
   pt(F(309016994374947424102293417183,den),F(-951056516295153572116439333379,den))]
ys=[pt(0),q]
for v in u:
    vv=cmul(v,v)
    h=cdiv(add(vv,cmul(minus(pt(1),scale(2,v)),q)),add(q,minus(vv,scale(2,v))))
    ys.append(cmul(h,h))
projected=[cmul(ROT,y) for y in ys]
order=sorted(range(6),key=lambda i:projected[i][0]);assert order==[2,0,5,3,4,1]
cuts=[projected[i] for i in order]
for i,p in enumerate(cuts):
    if i!=1:assert p[1]>F(1,4)
for i in range(5):assert cuts[i+1][0]-cuts[i][0]>F(1,100)
eps=F(1,1000)
assert cuts[0][0]<-2*eps and cuts[2][0]>2*eps
base=pt(10);entry=pt(-eps)
arc=[base,pt(10,-2),pt(-eps,-2),entry]
circle=[entry,pt(-eps,-eps),pt(eps,-eps),pt(eps,eps),pt(-eps,eps),entry]
path=arc+circle[1:]+list(reversed(arc))[1:]
events=[]
def red(w,c=0):
    out=[]
    for x in w:
        x=c if c and abs(x)==c else x
        if out and (out[-1]==-x or c and out[-1]==x==c):out.pop()
        else:out.append(x)
    return tuple(out)
def inv(w):return tuple(-x for x in reversed(w))
def segment(a,b):
    dx,dy=b[0]-a[0],b[1]-a[1];ee=[]
    for j,p in enumerate(cuts,1):
        for z in (a,b):
            if z[0]==p[0]:assert z[1]>p[1],('endpoint lies on cut',j)
        if dx:
            t=(p[0]-a[0])/dx
            if 0<=t<=1:assert a[1]+t*dy!=p[1],('puncture hit',j)
            if 0<t<1 and a[1]+t*dy<p[1]:
                ee.append((t,j if dx>0 else -j,p[1]-(a[1]+t*dy)))
        elif a[0]==p[0]:assert not min(a[1],b[1])<=p[1]<=max(a[1],b[1])
    ee.sort()
    events.append({'a':[str(x) for x in a],'b':[str(x) for x in b],
                   'events':[{'parameter':str(t),'letter':j,'height_gap':str(gap)} for t,j,gap in ee]})
    return [j for t,j,gap in ee]
word=red(j for a,b in zip(path,path[1:]) for j in segment(a,b))
M=(-6,-5,-4,-3)
expected=M+(2,)+inv(M)
assert word==expected
assert sum(a[0]*b[1]-a[1]*b[0] for a,b in zip(circle,circle[1:]))>0
# Except inside a tiny empty neighborhood of the cone, the path lies
# in the lower unrotated y half-plane. This supplies the geometric
# homotopy to the empty negative-real radial cone arc.
for z in [base,pt(10,-2),pt(-eps,-2),pt(-eps,-eps)]:
    assert cdiv(z,ROT)[1]<0
for p in ys[1:]:assert p[1]>F(1,100)

D=json.loads((P/'inner_q0_adapted_basis22.json').read_text())
Ji={int(k):tuple(w) for k,w in D['old_in_Y'].items()}
def subst(w,A,c=0):return red((y for x in w for y in (A[abs(x)] if x>0 else inv(A[-x]))),c)
MY=red(subst(M,Ji,3),3)
assert MY==(-6,-5,-4,-1) # e^-1 d^-1 f^-1 a^-1
Pold=(1,3,-2,3)
L=red(MY+Pold,3)
assert L==(-6,-5,-4,3,-2,3)
old_cone=tuple(D['old_in_Y']['2'])
coneY=red(MY+old_cone+inv(MY),3)
assert coneY==red(L+(3,)+inv(L),3)
out={'status':'PASS','base_q':['4/5','1/2'],'rotation':['1','371/1000'],
 'input_sha256':hashlib.sha256((P/'inner_q0_adapted_basis22.json').read_bytes()).hexdigest(),
 'initial_physical_order':order,'rational_projected_punctures':[[str(x) for x in z] for z in cuts],
 'path':[[str(x) for x in z] for z in path],'cut_events':events,
 'positive_cone_word':word,'M_in_old':M,'M_in_Y':MY,
 'old_cone_connector_P_in_Y':Pold,'combined_L_in_Y':L,'gap_cone_in_Y':coneY,
 'deformation_margin':'All ordinary heights exceed1/4, projection gaps exceed1/100; epsilon=1/1000. The existing actual-root displacement<1e-26 preserves every finite comparison.',
 'scope':'Exact original-cut word for the empty lower radial cone whisker at the actual base. Its use as a common-neck cone requires the simultaneous lower-collar transport described in the proof note.'}
(P/'annular_gap_cone23.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS all rational path segments, positive local cone square and full cut word')
print('gap cone = M x2 M^-1, M=',M)
print('PASS actual marked conversion: gap cone=L C L^-1, L=e^-1 d^-1 f^-1 (bar b)^-1')
print('PASS lower-half-plane corridor and actual-root comparison margins')
