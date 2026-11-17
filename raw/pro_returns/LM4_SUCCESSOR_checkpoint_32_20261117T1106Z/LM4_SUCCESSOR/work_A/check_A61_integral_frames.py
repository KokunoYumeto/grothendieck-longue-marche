"""Exact existential central-frame repair. The original A56 tuple is untouched."""
from pathlib import Path
import runpy,json
HERE=Path(__file__).resolve().parent
globals().update(runpy.run_path(str(HERE/'check_A59_integral_center.py')))
def half_new(z):
 central_kernel(z)
 out=[]
 for x,free in zip(z,zfree):
  if free:
   a=sum(((x>>(2*i+1))&1)<<i for i in range(3));out.append(TEICH[a])
  else:out.append(0)
 out=tuple(out);assert zs(2,out)==z
 return out
ZS=half_new(bn[1])
BGOOD=(BFRAME[0],za(BFRAME[1],ZS),BFRAME[2])
assert ph(SS)==ein(BGOOD,SS)
assert em(ei(BGOOD),na(ei(BGOOD)))==ONE
assert ein(ei(BGOOD),na(SS))==SS
rd=json.loads((HERE.parent/'work_CE/Q6_integral_rframe_data.json').read_text())
ja=tup(rd['r_frame_free_O'])+tup(rd['r_frame_binary_k'])
jhead=tup(rd['r_frame_head'])
oldj=old_to_new(tup(oldw['JFRAME']))
assert oldj[0]==reduce_a(ja) and oldj[2]==jhead
jz=tuple(TEICH[x]if free else x for x,free in zip(oldj[1],zfree))
JFRAME=(ja,jz,jhead)
assert na(RR)==ein(JFRAME,ei(RR))
jn=em(ei(JFRAME),na(ei(JFRAME)))
assert jn[0]==AA0 and jn[2]==HN0
JRANK=central_kernel(jn[1])
ZR=half_new(jn[1])
JGOOD=(JFRAME[0],za(JFRAME[1],ZR),JFRAME[2])
assert na(RR)==ein(JGOOD,ei(RR))
assert em(ei(JGOOD),na(ei(JGOOD)))==ONE
assert ein(ei(JGOOD),na(RR))==ei(RR)
assert ph(TT)==TT and na(na(SS))==SS and na(na(RR))==RR
assert BGOOD[0]==BFRAME[0] and BGOOD[2]==BFRAME[2]
assert JGOOD[0]==JFRAME[0] and JGOOD[2]==JFRAME[2]
out=dict(status='PASS: simultaneous actual scalar-quotient frames after central refinement of new A56 choices',
 scope='Original A56 JSON unchanged; old new-center frames may change; older C and retained-family frames unchanged.',
 WE=WE,PSHIFT=PSHIFT,BFRAME=BGOOD,JFRAME=JGOOD,
 s_old_square=bn[1],r_old_square=jn[1],s_half=ZS,r_half=ZR,
 s_changed_reduction=reduce_z(ZS),r_changed_reduction=reduce_z(ZR),
 all_direct_checks='PASS')
(HERE/'A61_integral_frame_solution.json').write_text(json.dumps(out,indent=2)+'\n')
print('Exact r-conjugacy before central correction: PASS')
print('Old s/r new-center square serializations:',central_kernel(bn[1]),JRANK)
print('Independent central halves solve BOTH normalizer squares without changing either conjugacy: PASS')
print('Literal cusp, quotient negative square, and old head projections: PASS')
print('The new A56 central frame coordinates are refined; the original stored tuple is not claimed retained.')
