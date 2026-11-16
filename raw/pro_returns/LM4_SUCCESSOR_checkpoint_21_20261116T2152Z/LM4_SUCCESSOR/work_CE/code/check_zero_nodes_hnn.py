"""Exact zero-node reductions in the verified thirteen-value partial HNN.
Read-only use of DE's weighted folded-graph engine; outputs stay in CE.
"""
from pathlib import Path
import sys,json,hashlib
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[2];CE=ROOT/'work_CE';DE=ROOT/'work_DE/next_marginal_source'
sys.path.insert(0,str(DE))
p=DE/'reduce_other_triples_hnn.py';src=p.read_text().split('def art(w):',1)[0]
ns={'__file__':str(p),'__name__':'CE_readonly_hnn_prefix'}
exec(compile(src,str(p),'exec'),ns)
red,iv,mul,sub,britton=(ns[k] for k in ('red','iv','mul','sub','britton'))
D=json.loads((DE/'zero_double_relations.json').read_text());rows=[]
for row in D['relations']:
 k=tuple(row['normalized_U_conjugator']);u=(row['U_index'],);z=(row['zero_index'],)
 conjugate=mul(k,u,iv(k));rcon,steps=britton(conjugate)
 assert 11 not in rcon and -11 not in rcon
 original=mul(z,conjugate,iv(z),iv(conjugate));result=mul(z,rcon,iv(z),iv(rcon))
 direct,dsteps=britton(original)
 assert direct==result
 # Each certified pinch expression substitutes freely to its H word.
 for s in steps+dsteps:
  origbasis=ns['dimages'] if s['sign']==1 else ns['rimages']
  otherbasis=ns['rimages'] if s['sign']==1 else ns['dimages']
  assert sub(s['edge_basis_word'],origbasis)==tuple(s['H_word'])
  assert sub(s['edge_basis_word'],otherbasis)==tuple(s['replacement'])
 rows.append({'name':row['name'],'zero_index':z[0],'U_index':u[0],
  'original_U_conjugate':conjugate,'reduced_U_conjugate':rcon,
  'original_commutator':original,'reduced_H_relator':result,'steps':steps})
 print(row['name'],'U-conjugate length',len(conjugate),'->',len(rcon),
       'pinches',len(steps),'H relator length',len(result))
 if len(rcon)<50:print(' H-conjugate:',rcon)
out={'scope':'All eight actual zero-node relators reduce into H in the exact partial HNN. This alone does not prove edge-kernel compatibility after quotienting.',
 'input_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in
 [DE/'zero_double_relations.json',DE/'weighted_stallings.py',DE/'reduce_other_triples_hnn.py',CE/'discriminant_partial_hnn.json']},'rows':rows}
(CE/'zero_nodes_hnn_reductions.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: all eight U conjugates and commutators reduce to literal H words; every edge-basis substitution checked independently.')
