#!/usr/bin/env python3
"""Integral first-moment torsor, actual coefficient map, and local theta classes.

This is a separate comparison subresult.  It does not assign a coefficient
to the unknown intrinsic arithmetic handle action.
"""
from pathlib import Path
from hashlib import sha256
from itertools import product
import json
import sympy as s

base=Path(__file__).resolve().parent
names=['a_elliptic_theta_pi.json','a_log_torsor_pairing_probe.json','a_elliptic_tor_symbol.json']
inputs={name:sha256((base/name).read_bytes()).hexdigest() for name in names}
theta_data=json.loads((base/names[0]).read_text())
pairing=json.loads((base/names[1]).read_text())
tor=json.loads((base/names[2]).read_text())
assert theta_data['status']==pairing['status']==tor['status']=='PASS'
R=s.Matrix(tor['Weil_marking']['R']).applyfunc(s.sympify)
S=s.Matrix(tor['Weil_marking']['S']).applyfunc(s.sympify)
CE=s.Matrix([[1,-1],[0,-1]])
u=s.Matrix(tor['proper_bockstein_numerator_u']).applyfunc(s.sympify).T
l=s.Matrix(tor['unit_character']).applyfunc(s.sympify)
t=s.Matrix(tor['peripheral_primitive_t']).applyfunc(s.sympify)
p=s.Matrix(tor['actual_filling_p']).applyfunc(s.sympify)
assert l==3*t+u.T*p
assert u==s.Matrix([0,1])
a,b,w=s.symbols('a b w')
A=(1+3*a)*s.eye(2)+3*b*R
chi=s.expand(A.det())
h0=s.Matrix([1/w,0])
kappa=(A-s.eye(2))*h0/3
Log=s.zeros(3);Log[0,0]=chi
Log[1:3,0]=chi*kappa;Log[1:3,1:3]=chi*A
proper=chi*A.adjugate().T
cross=chi*(s.eye(2)-A.adjugate().T)*u/3
Target=s.zeros(3);Target[0,0]=chi
Target[1:3,0]=cross;Target[1:3,1:3]=proper
Phi=s.diag(1,1,1);Phi[1:3,1:3]=-w*S
assert all(s.simplify(t)==0 for t in Phi*Log-Target*Phi)
assert Phi.det()==w*w
assert w*S*h0==u
Logc=s.diag(-1,1,1);Logc[1:3,1:3]=-CE
Targetc=s.diag(-1,1,1);Targetc[1:3,1:3]=CE.inv().T
assert Phi*Logc==Targetc*Phi

# Literal change of the whole Tate/intrinsic basis, with the actual Weil
# unit transformed by det(B).  No numerical original-to-finite B is assigned.
r0,r1=s.symbols('r0 r1')
B=(1+3*r0)*s.eye(2)+3*r1*R
wn=w*B.det()
hnew=s.Matrix([1/wn,0])
LogChange=s.zeros(3);LogChange[0,0]=1
LogChange[1:3,0]=(B.inv()*h0-hnew)/3
LogChange[1:3,1:3]=B.inv()
RowChange=s.zeros(3);RowChange[0,0]=1
RowChange[1:3,0]=(s.eye(2)-B.inv().T)*u/3
RowChange[1:3,1:3]=B.inv().T
PhiNew=s.diag(1,1,1);PhiNew[1:3,1:3]=-wn*S
assert all(s.simplify(t)==0 for t in RowChange*PhiNew*LogChange-Phi)
assert all(s.simplify(t)==0 for t in B.inv().T*wn*S*B.inv()-w*S)

# Ordered target coordinates are (peripheral coefficient, proper row1,row2).
F=s.Matrix([[4,0,0],[0,-8,0],[4,0,-8]])
C=F-s.eye(3)
quotient=s.Matrix([[0,1,0],[1,0,6]])
orders=[9,27]
assert all(int((quotient*C)[i,j])%orders[i]==0 for i in range(2) for j in range(3))
assert abs(int(C.det()))==9*27
inverse=s.Matrix([[0,1],[1,0],[0,0]])
assert quotient*inverse==s.eye(2)
reduction_boundary=[]
for j in range(3):
    delta=s.eye(3)[:,j]-inverse*quotient[:,j]
    lift=C.inv()*delta
    assert all(x.q==1 for x in lift)
    reduction_boundary.append([int(x) for x in lift])
period_lifts=[]
for j,m in enumerate(orders):
    lift=C.inv()*inverse[:,j]*m
    assert all(x.q==1 for x in lift)
    period_lifts.append([int(x) for x in lift])

# The exact finite module is L_n={(a,h):h mod3=a*A0}; its inverse
# moment coordinate z is modulo 3^(n-1), not modulo 3^n.
lattice_checks=[]
for n in range(1,5):
    m=3**n;d=m//3;omega=13%m
    invw=pow(omega,-1,m)
    images=set()
    for aa,z1,z2 in product(range(m),range(d),range(d)):
        hh=((aa*invw+3*z1)%m,(3*z2)%m)
        assert hh[0]%3==aa%3 and hh[1]%3==0
        xx=(omega*z2%d,-omega*z1%d)
        zz=((-pow(omega,-1,d)*xx[1])%d,(pow(omega,-1,d)*xx[0])%d) if d>1 else (0,0)
        assert zz==(z1,z2)
        images.add((aa,*hh))
        # Both the moment action and the actual V*(2) action at Frob4.
        an=4*aa%m;hn=tuple(-8*x%m for x in hh)
        zn=((hn[0]-an*invw)//3%d,hn[1]//3%d)
        xn=(omega*zn[1]%d,-omega*zn[0]%d)
        assert xn==((-8*xx[0])%d,(-8*xx[1]+4*aa)%d)
    assert len(images)==3**(3*n-2)
    lattice_checks.append({'n':n,'modulus':m,'module_order':len(images),
                           'invariant_orders':[m,d,d],
                           'ambient_reduction_kernel_orders':[3,3],
                           'next_level_to_full_target_kernel_order':3})

# Actual finite field operations on the retained supersingular model.
mod=theta_data['finite_field']['irreducible_modulus_bits']
q=theta_data['finite_field']['size']
def mul(x,y):
    out=0
    while y:
        if y&1:out^=x
        y>>=1;x<<=1
        if x>=q:x^=mod
    return out
def power(x,n):
    out=1
    while n:
        if n&1:out=mul(out,x)
        x=mul(x,x);n>>=1
    return out
def div(x,y):
    assert y
    return mul(x,power(y,q-2))
def add(P,Q):
    if P is None:return Q
    if Q is None:return P
    x,y=P;u0,v=Q
    if x==u0:
        if y!=v:return None
        slope=mul(x,x)
    else:slope=div(y^v,x^u0)
    xx=mul(slope,slope)^x^u0
    return xx,mul(slope,xx^x)^y^1
def scale(k,P):
    out=None
    if k<0:P=P[0],P[1]^1;k=-k
    while k:
        if k&1:out=add(out,P)
        P=add(P,P);k>>=1
    return out
P,Q=map(tuple,theta_data['actual_E27_basis'])
zeta=theta_data['finite_field']['zeta3']
roots={r['order']:r['root'] for r in pairing['pairings']}
omegas={r['order']:r['exponent'] for r in pairing['pairings']}
assert omegas=={3:1,9:4,27:13}
def theta(point):
    den=1^mul(power(zeta,2),power(point[0],3))
    assert den
    return power(den,q-2)
def exponent(x,m):
    exps=[i for i in range(m) if power(roots[m],i)==x]
    assert len(exps)==1
    return exps[0]

all_points={(i,j):add(scale(i,P),scale(j,Q)) for i,j in product(range(27),repeat=2)}
assert len(set(all_points.values()))==729
moment_records=[]
for t1,t2 in product(range(3),repeat=2):
    if (t1,t2)==(0,0):continue
    point=all_points[9*t1,9*t2]
    levels=[]
    for n in [1,2,3]:
        m=3**n;step=27//m
        candidates={(i,j) for i,j in product(range(m),repeat=2)
                    if i%3==t1 and j%3==t2}
        total=[0,0,0];orbits=[]
        while candidates:
            start=min(candidates);cur=start;orbit=[]
            while cur not in orbit:
                orbit.append(cur);cur=tuple(-2*x%m for x in cur)
            assert cur==start
            candidates.difference_update(orbit)
            f=len(orbit)
            value=theta(all_points[step*start[0],step*start[1]])
            assert power(value,4**f)==value and (4**f-1)%m==0
            k=exponent(power(value,(4**f-1)//m),m)
            term=(k,k*start[0]%m,k*start[1]%m)
            assert term[1]%3==term[0]*t1%3 and term[2]%3==term[0]*t2%3
            total=[(total[j]+term[j])%m for j in range(3)]
            orbit_changes=[]
            for r in range(1,len(orbit)):
                alt=orbit[r]
                av=theta(all_points[step*alt[0],step*alt[1]])
                ak=exponent(power(av,(4**f-1)//m),m)
                assert ak==4**r*k%m
                other=(ak,ak*alt[0]%m,ak*alt[1]%m)
                # F^r-1=(F-1)(1+...+F^(r-1)) on the actual L_n.
                pre=[sum((4 if j==0 else -8)**v for v in range(r))*term[j]%m for j in range(3)]
                assert pre[1]%3==pre[0]*t1%3 and pre[2]%3==pre[0]*t2%3
                assert [(other[j]-term[j])%m for j in range(3)]==[3*pre[0]%m,-9*pre[1]%m,-9*pre[2]%m]
                orbit_changes.append({'representative':alt,'term':other,'boundary_preimage':pre})
            orbits.append({'representative':start,'length':f,'theta':value,'kummer':k,
                           'term':term,'other_representatives':orbit_changes})
        assert total[1]%3==total[0]*t1%3 and total[2]%3==total[0]*t2%3
        levels.append({'n':n,'modulus':m,'augmentation_moment':total,'orbits':orbits})
    # The earlier full moments are an immutable independent input.
    old=next(r for r in theta_data['moments_at_Frob4'] if r['t']==[t1,t2])
    assert levels[0]['augmentation_moment'][1:]==old['level1']['moment']
    assert levels[1]['augmentation_moment'][1:]==old['level2']['moment']
    moment_records.append({'t':[t1,t2],'point':point,'levels':levels})

record=next(x for x in moment_records if x['t']==[1,0])
local=[]
for level in record['levels']:
    n=level['n'];m=level['modulus'];d=m//3;omega=omegas[m]
    aa,ee1,ee2=level['augmentation_moment']
    assert (omega*ee1-aa)%3==0 and ee2%3==0
    xx=[(omega*ee2//3)%d,((aa-omega*ee1)//3)%d] if d>1 else [0,0]
    # Change the simultaneous root choices so that augmentation is the
    # directly specified local root system of theta(A0)=-lambda.
    assert aa%3==2
    scalar=(2-aa)//3
    hh0=pow(omega,-1,m)
    ep=[(ee1-9*scalar*hh0)%m,ee2]
    assert (omega*ep[0]-2)%3==0
    xn=[omega*ep[1]//3%d,(2-omega*ep[0])//3%d] if d>1 else [0,0]
    assert xn==[xx[0],(xx[1]+4*scalar)%d]
    local.append({'n':n,'omega':omega,'raw_pair':[aa,ee1,ee2],
                  'raw_target':[aa,*xx],'scalar_root_change':scalar,
                  'root_change_lift':[scalar,scalar*hh0%m,0],
                  'normalized_pair':[2,*ep],'normalized_target':[2,*xn]})
    if n==3:
        target=s.Matrix([aa,*xx]);normal=s.Matrix([2,*xn])
        coords=[int((quotient*target)[i])%orders[i] for i in range(2)]
        coords2=[int((quotient*normal)[i])%orders[i] for i in range(2)]
        assert coords==coords2
        local[-1]['full_local_H1_coordinates_C9_C27']=coords

# Exact transition of local classes between successive finite lattices.
transition_checks=[]
for before,after in zip(local[1:],local[:-1]):
    n=after['n'];m=3**n;d=m//3
    x=before['raw_target'];y=after['raw_target']
    delta=[(x[0]-y[0])%m,(x[1]-y[1])%d,(x[2]-y[2])%d]
    choices=[aa for aa in range(m) if [3*aa%m,0,4*aa%d]==delta]
    assert choices
    transition_checks.append({'from_n':n+1,'to_n':n,'difference':delta,
                              'boundary_preimage':[min(choices),0,0]})

out={'status':'PASS','scope':'integral torsor coefficient map and actual finite local theta class; no intrinsic action value assigned',
     'input_sha256':inputs,
     'generic_action_square':{'A':str(A),'chi':str(chi),'h0':'omega^-1 e1',
                             'Phi':'diag(1,-omega*S)','determinant':'omega^2'},
     'actual_basis_transport':{'B':str(B),'new_Weil_unit':'omega*det(B)',
                               'intrinsic_basis':'[[B,0],[U(B-I)/3,I8]]',
                               'row_map':'C_B^-T','square':'RowChange*PhiNew*LogChange=Phi',
                               'scope':'B is defined by the actual division-point comparison and is not numerically assigned'},
     'Frob4_target_matrix':[list(map(int,F.row(i))) for i in range(3)],
     'full_local_quotient':{'orders':orders,'map':[list(map(int,quotient.row(i))) for i in range(2)],
                            'inverse':[list(map(int,inverse.row(i))) for i in range(3)],
                            'reduction_boundary_columns':reduction_boundary,'period_boundary_columns':period_lifts},
     'finite_lattice_checks':lattice_checks,'moments':moment_records,
     'A0_local_class':local,'local_transition_boundaries':transition_checks,
     'unresolved':'The constructed theta logarithm class has not been identified with the actual unknown intrinsic handle cocycle.'}
(base/'a_elliptic_log_torsor.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: integral first-moment lattice and generic arithmetic coefficient isomorphism')
print('PASS: 61,320 finite lattice inverses/actions; all eight theta classes through modulus27')
print('PASS: all orbit changes and both finite local transition boundaries')
print('A0 local normalized target:',local[-1]['normalized_target'])
print('A0 complete local H1 coordinates C9,C27:',local[-1]['full_local_H1_coordinates_C9_C27'])
