"""Executed exact D4 lantern conjugators for the (1,3) cut-sphere tail.
Uses the independently implemented classical D4 Garside normal form.
The geometric identification of the tail basis is Soroko Figure 2.
"""
from pathlib import Path
import importlib.util,json
P=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('d4',P/'d_artin_d4.py')
D=importlib.util.module_from_spec(spec);spec.loader.exec_module(D)
d0=(1,4)*6;d1=(2,4,3)*4;d2=(1,4,3)*4;d3=(1,4,2)*4
q2=(1,4,3,1,4,1);q3=(1,4,2,1,4,1)
t32=D.cat(d0,D.inv(d3),D.inv(d2));t23=D.cat(d0,D.inv(d2),D.inv(d3))
checks=[]
for name,u,rhs in [('q2',q2,t32),('q3',q3,t23),('q2_inverse',D.inv(q2),t23),('q3_inverse',D.inv(q3),t32)]:
 lhs=D.conj(u,d1);assert D.equal(lhs,rhs)
 checks.append(dict(name=name,conjugator=u,lhs=lhs,rhs=rhs,quotient_equal=True))
for name,u,leaf in [('q2',q2,3),('q3',q3,2)]:
 assert D.equal(D.conj(u,(leaf,)),(1,))
 assert D.equal(D.conj(u,(4,)),(4,))
 checks.append(dict(name=name+'_curve_transport',leaf=leaf,target=1,fixed_b=True))
q1=(2,4,3,2,4,2);h=(1,4)*3
for name,lhs,rhs in [
 ('N321',D.cat(q3,q1,D.inv(q2)),D.cat(h,D.inv(d2))),
 ('N231',D.cat(q2,q1,D.inv(q3)),D.cat(h,D.inv(d3))),
 ('S1',D.cat(D.inv(q2),D.inv(q3)),(-3,-4,-3,2,4,3))]:
 assert D.equal(lhs,rhs)
 checks.append(dict(name=name,lhs=lhs,rhs=rhs,quotient_equal=True))
out=dict(type=[1,3],source='Soroko2019 Figure2; d_artin_d4 exact normal form',D0=d0,D1=d1,D2=d2,D3=d3,checks=checks)
(P/'b_d4_tail.json').write_text(json.dumps(out,indent=2)+'\n')
print('Four exact lantern conjugators and four supporting curve-transport identities verified.')
print('q2 D1 q2^-1 = D0 D3^-1 D2^-1; q3 gives the reverse product.')
