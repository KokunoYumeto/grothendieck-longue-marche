#!/usr/bin/env python3
"""Exact whole-operator basis conversion, with no orbit truncation."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[2]
P=ROOT/'work_DE/next_marginal_source/one_sided_source_detector26.json'
D=json.loads(P.read_text())
def red(w):
 out=[]
 for x in w:
  if out and out[-1]==-x:out.pop()
  else:out.append(x)
 return out
def inv(w):return [-x for x in w[::-1]]
def sub(w,m):
 return red([z for x in w for z in (m[abs(x)] if x>0 else inv(m[abs(x)]))])
old_to_new={int(k):v for k,v in D['old_free7_in_source_basis'].items()}
new_to_old={int(k):v for k,v in D['source_contact_plus_retained_basis'].items()}
for i in range(1,8):
 assert sub(new_to_old[i],old_to_new)==[i]
 assert sub(old_to_new[i],new_to_old)==[i]
maps={}
for sign,mp in D['all_four_signed_free7_source_actions'].items():
 mp={int(k):v for k,v in mp.items()}
 maps[sign]={i:sub(sub(new_to_old[i],mp),old_to_new) for i in range(1,8)}
for s,t in [('m','m_inverse'),('v','v_inverse')]:
 for i in range(1,8):
  assert sub(maps[s][i],maps[t])==[i]
  assert sub(maps[t][i],maps[s])==[i]
names=['s1','s2','s3','s4','f','g','x']
def show(w):
 return ' '.join(names[abs(z)-1]+('^-1' if z<0 else '') for z in w) or '1'
for s,mp in maps.items():
 print(s)
 for i,w in mp.items():print(' ',names[i-1],'->',show(w),'[length',len(w),']')
out={'status':'PASS','input':str(P.relative_to(ROOT)),'input_sha256':hashlib.sha256(P.read_bytes()).hexdigest(),
 'basis':names,'new_to_old':new_to_old,'old_to_new':old_to_new,
 'all_four_signed_operators':maps,'checks':{'basis_inverse_compositions':14,'signed_operator_inverse_compositions':28},
 'scope':'Complete finite operator input in the actual one-sided quotient; every signed source word remains. No source-kernel equality or lift to the unfilled group is asserted.'}
Q=ROOT/'work_CE/next_symmetric_nodes/one_sided_source_operators26.json'
Q.write_text(json.dumps(out,indent=2)+'\n')
print('PASS all 14 basis and 28 operator inverse compositions.')
