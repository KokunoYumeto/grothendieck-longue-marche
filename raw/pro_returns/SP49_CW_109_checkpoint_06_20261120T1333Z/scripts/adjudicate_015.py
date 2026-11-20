"""Root confirmation of scan 015 and the bounded groupoid-classifier check."""
from common import *
from datetime import datetime,timezone
R=load_page(15);texts={r:(W/f'readers/015/{r}/reading.tex').read_text() for r in 'ABC'}
assert len({normalized(t) for t in texts.values()})==1
assert normalized(texts['B'])==normalized((W/'inputs/015/C.tex').read_text())
assert all(not r['changes'] and not r['remaining_doubts'] for r in R.values())
notes=R['B']['notes']+[
 '[S015-groupoids-subobject-classifier; p13 question] The main reader and each independent reader checked the proposed obstruction for the ordinary category of small groupoids and functors. A subgroup inclusion BH → BG is monic. If true:1 → Omega classified it, its characteristic functor would send the sole object to the truth object, and the pullback arrows would form the kernel of G → Aut_Omega(truth), a normal subgroup. Taking G=S_3 and H={e,(12)} contradicts this, since conjugation by (123) takes (12) to (23), outside H. Thus this ordinary category has no subobject classifier, which is a sufficient obstruction to being a topos. This supports the printed question under that interpretation; its repeated is and question mark remain. The detailed main-reader argument is retained in records/math_scan015_root.md. No computation of the separately proposed pi_3(S^2) test was attempted.'
]
date=datetime.now(timezone.utc).strftime('%Y-%m-%d');events=[]
for r in 'ABC':
 for x in R[r]['math_checks']:
  events.append({'statement_id':x['statement_id'],'date':date,'who_model_effort_run':f'GPT-6 Astra Pro; effort not exposed; /root/scan015_{r.lower()}','type':x['type'],'outcome':x['outcome']+' Note N015.7.'})
events.append({'statement_id':'S015-groupoids-subobject-classifier','date':date,'who_model_effort_run':'GPT-6 Astra Pro; effort not exposed; /root','type':'targeted proof check','outcome':'Developed the subgroup/kernel obstruction during reading and retained it in records/math_scan015_root.md before the final returns. Checked monicity of BH → BG, the nonempty pullback condition on the truth object, the resulting normal kernel, and the explicit nonnormal subgroup {e,(12)} of S_3. Later compared the three independent arguments, which agree. This supports N015.7 only for the ordinary category of groupoids and functors; the requested pi_3(S^2) experiment was not performed.'})
write_record(15,'B','brief_v05.md',texts['B'],[],doubt_decisions(R['A'],15,'A'),[],notes,
 'All three full readings agree with literal C after removing the optional cote wrapper. All eight contextual loci, twelve correction entries and mathematical indices were confirmed. B’s 20-row inventory separately includes K, the italic span, both inline mathematical expressions, handwritten note and archive number. A and B settled all ink in the halves; C inspected two unresolved capital/index loci. Root compared every report and full text; no disagreement required a main crop. The handwritten commenter is left unnamed because identity is not established by this sheet.',events=events,notation=R['A']['notation'])
print('Scan 015 confirmed unchanged; 20 inventory elements; 4 actual mathematical events.')
