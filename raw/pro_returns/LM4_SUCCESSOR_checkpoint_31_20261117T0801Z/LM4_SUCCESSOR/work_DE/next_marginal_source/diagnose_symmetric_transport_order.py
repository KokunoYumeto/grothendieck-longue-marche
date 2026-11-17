from pathlib import Path
import json
H=Path(__file__).resolve().parent
source=(H/'check_symmetric_old_actions.py').read_text().split('outputs=[]')[0]
exec(compile(source,'old_action_checker_prefix','exec'))
End=json.loads((H/'symmetric_fixed_basis.json').read_text());Fe={int(k):tuple(v) for k,v in End['involution_images'].items()}
Bridge=json.loads((ROOT/'work_CE/next_symmetric_nodes/symmetric_source_bridge.json').read_text());W=Bridge['nodal_base_to_pairing_base_braid']
for wlabel,ww in [('W',W),('W_inverse',inv(W)),('W_reverse',list(reversed(W))),('W_reverse_inverse',inv(tuple(reversed(W))))]:
 T=art(ww);Ti=art(inv(ww));Fn={j:sub(sub(Ti[j],Fe),T) for j in range(1,22)}
 for mode in ('chronological_art','reversed_art'):
  passed=[]
  for row in B['loops']:
   word=row['word'] if mode=='chronological_art' else list(reversed(row['word']))
   A=art(word);Ai=art(inv(word));J={j:sub(sub(sub(Ai[j],Fn),A),Fn) for j in range(1,22)}
   try:k=inner_word(J);passed.append(len(k))
   except AssertionError:passed.append(None)
  print(wlabel,mode,passed,flush=True)
