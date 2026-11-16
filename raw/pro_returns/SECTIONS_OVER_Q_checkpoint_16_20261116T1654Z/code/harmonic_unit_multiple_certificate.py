#!/usr/bin/env python3
"""Independent literal finite orbits and actual cover images for A148.1."""
from fractions import Fraction
from pathlib import Path
import json
from harmonic_elliptic_rank_certificate import add_mod

K,N=573,1146
Q0=Fraction(325596479663,72962)
A=K*Q0*Q0
POINTS={'P':(2028,75348),'Q':(5202,365976)}
EXPECTED={('P',17):(10,[0,5]),('P',257):(16,[0,8]),
          ('Q',5):(2,[0]),('Q',769):(10,[0,5])}


def residue(f,p):
    f=Fraction(f)
    return f.numerator*pow(f.denominator,-1,p)%p


def phi(P,p):
    if P is None or P[0]==0:
        return None
    x,y=P
    ix=pow(x,-1,p)
    return ((x-N*N*ix)*pow(4,-1,p)%p,
            y*(1+N*N*ix*ix)*pow(8,-1,p)%p)


def encode(P):
    return 'O' if P is None else list(P)


records=[]
for (name,p),(order,expected) in EXPECTED.items():
    aa,qq,h=residue(A,p),residue(Q0,p),pow(2,-1,p)
    fourths={}
    for w in range(p):
        fourths.setdefault(aa*pow(w,4,p)%p,[]).append(w)
    image={None}
    affine=[]
    for t in range(p):
        for w in fourths.get(t*(t-1)*(t-h)%p,[]):
            P=(N*(2*t-1)%p,8*K*K*qq*w*w%p)
            target=phi(P,p)
            image.add(target)
            affine.append({'T':t,'W':w,'E':encode(P),'F':encode(target)})
    P=tuple(x%p for x in POINTS[name])
    R=phi(P,p)
    ep=fp=None
    orbit=[]
    allowed=[]
    for m in range(order):
        assert fp==phi(ep,p)
        if ep is None:
            square_value='infinity'
            chi=0
            square_test=True
        else:
            square_value=ep[1]*pow(8*K*K*qq,-1,p)%p
            power=pow(square_value,(p-1)//2,p)
            chi=-1 if power==p-1 else power
            square_test=chi>=0
        assert square_test==(fp in image)
        if square_test:
            allowed.append(m)
        orbit.append({'m':m,'E':encode(ep),'F':encode(fp),
                      'W_squared':square_value,'quadratic_character':chi,
                      'in_image':square_test})
        ep=add_mod(ep,P,p,-N*N)
        fp=add_mod(fp,R,p,K*K)
    assert fp is None
    assert all(row['F']!='O' for row in orbit[1:])
    assert allowed==expected
    if p==17:
        assert [(x['T'],x['W']) for x in affine]==[(0,0),(1,0),(9,0)]
        assert image=={None,(0,0)}
    if p==5:
        assert image=={None,(0,0),(4,0)}
        assert R==(1,0)
    record={'point':name,'p':p,'a':aa,'q0':qq,'k':K%p,'n':N%p,
            'R':encode(R),'order':order,'allowed':allowed,'orbit':orbit,
            'D_affine_points':affine,'D_image_size':len(image)}
    records.append(record)
    print(name,'p=',p,'order=',order,'allowed=',allowed,
          'D-points=',len(affine)+1,'D-image=',len(image))
    print('Full square-test row:',[x['quadratic_character'] for x in orbit])
    print('Full F-orbit:',[x['F'] for x in orbit])

path=Path(__file__).with_name('harmonic_unit_multiple_certificate_data.json')
path.write_text(json.dumps(records,indent=2)+'\n')
print('ALL FOUR EXACT UNIT-MULTIPLE DETECTORS PASSED.')
