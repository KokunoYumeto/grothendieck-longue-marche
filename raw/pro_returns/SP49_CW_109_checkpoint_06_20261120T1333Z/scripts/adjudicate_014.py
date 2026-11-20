"""Main-reader confirmation of scan 014 after full-return comparison."""
from common import *
from datetime import datetime,timezone
R=load_page(14);texts={r:(W/f'readers/014/{r}/reading.tex').read_text() for r in 'ABC'}
assert len(set(texts.values()))==1
assert texts['B']==(W/'inputs/014/C.tex').read_text()
assert all(not r['changes'] and not r['remaining_doubts'] for r in R.values())
notes=R['A']['notes']+[
 '[S014-Hom-construction; p4 ell8] All three readers performed limited checks of the printed Hom expression. Interpreting C_N Delta^n as normalized chains and C as nonnegative, chain maps in degree 0 give C_0. In degree 1, an edge image b and initial vertex image a force the other vertex to a+d b, giving C_0 direct-sum C_1. A simplex map Delta^m → Delta^n induces a chain map in that direction and hence, by precomposition, a map from the n-th Hom group to the m-th. The main reader rechecked these two degrees and variance. This confirms local consistency of the written argument order and superscript; it does not prove Dold–Kan, settle the general-additive-category extension, or verify historical claims. No change to the ink follows.'
]
date=datetime.now(timezone.utc).strftime('%Y-%m-%d');events=[]
for r in 'ABC':
 for x in R[r]['math_checks']:
  events.append({'statement_id':'S014-Hom-construction','date':date,'who_model_effort_run':f'GPT-6 Astra Pro; effort not exposed; /root/scan014_{r.lower()}', 'type':x['type'],'outcome':x['outcome']+' Note N014.8.','original_reader_statement_id':x['statement_id']})
events.append({'statement_id':'S014-Hom-construction','date':date,'who_model_effort_run':'GPT-6 Astra Pro; effort not exposed; /root','type':'used and rechecked in this run','outcome':'Recomputed the vertex/edge equations under the stated nonnegative normalized-chain interpretation: f(v_0)=a, f(e)=b, f(v_1)=a+d b. Thus degree 1 has precisely the independent parameters C_0 and C_1; degree 0 has C_0. Rechecked precomposition from a simplex map to obtain the simplicial restriction direction. This supports N014.8 only, not the entire theorem or historical claims. The formula and surrounding qualifications remain as written.'})
write_record(14,'B','brief_v05.md',texts['B'],[],doubt_decisions(R['A'],14,'A'),[],notes,
 'All three full LaTeX returns are byte-identical to C. The root compared the three reports, all context decisions, mathematical checks and inventories. Reader B’s 16-row inventory includes the Hom group and both Cat occurrences separately, every correction entry, the typed page number, underline and archive number. Three/four/four reader crops settled local alphabet and impression questions; no disagreement required a main crop. No briefing defect appeared and version 05 remains in force.',events=events,notation=R['B']['notation'])
print('Scan 014 confirmed unchanged; 16 inventory elements; 4 actual mathematical events.')
