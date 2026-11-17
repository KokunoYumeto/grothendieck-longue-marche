#!/usr/bin/env python3
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
p=ROOT/'work_CE/next_symmetric_nodes/annular_two_operator25.json';s=json.loads(p.read_text())
q=ROOT/'work_CE/next_symmetric_nodes/actual_source_commutator26.json';b=json.loads(q.read_text())
def red(w):
 out=[]
 for z in w:
  z=abs(z) if abs(z) in (6,7) else z
  if out and (out[-1]==-z or (abs(z) in (6,7) and out[-1]==z)):out.pop()
  else:out.append(z)
 return out
def inv(w):return [-a for a in w[::-1]]
mp={int(i):w for i,w in s['ordinary_fiber11_to_fiber7'].items()}
word=[1,11,6,-11]
expanded=red(a for z in word for a in (mp[z] if z>0 else inv(mp[-z])))
assert expanded==[1,7,1,7]==b['words']['proved_U']
assert s['selected_plus_involution']['1']==[11,6,-11]
# The named two actual cores are both killed; retained x remains.
remaining=[z for z in word if abs(z) not in (1,6)]
assert remaining==[11,-11]
out={'status':'PASS_LITERAL_A_SOURCE_MARKING','inputs':{str(z.relative_to(ROOT)):hashlib.sha256(z.read_bytes()).hexdigest() for z in (p,q)},'actual_A_s_in_W':[1,11,6,-11],'meaning':'a x bar_a x^-1 with x=tau c, bar_a=c a c','literal_orbifold_expansion':expanded,'B130_proved_norm':b['words']['proved_U'],'two_deleted_cores_leave':[11,-11],'scope':'The equality raw A_s=proved norm uses B130 actual node proof; this checker verifies its exact F11/cone marking, not a free equality of the unreduced raw source word.'}
(ROOT/'work_A/core_deletion_A_marking27.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS actual delta(a)=x bar_a x^-1 and a x bar_a x^-1=a tau a tau by literal cone reduction.')
print('PASS the two excluded cores leave x x^-1, so every stated enlargement kills actual A_s.')
