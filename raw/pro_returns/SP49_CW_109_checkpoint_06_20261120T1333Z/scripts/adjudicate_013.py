"""Root confirmation of unanimous scan 013 text, with actual mathematical checks."""
from common import *
from datetime import datetime,timezone
R=load_page(13)
texts={r:(W/f'readers/013/{r}/reading.tex').read_text() for r in 'ABC'}
assert len({normalized(t) for t in texts.values()})==1
assert normalized(texts['B'])==normalized((W/'inputs/013/C.tex').read_text())
assert all(not r['changes'] for r in R.values())
notes=R['B']['notes']+[
 '[S013-cartesian-closure; item 1] A and B separately checked cartesian closure by the exponential construction (Y^X)_n = Hom_sSet(Delta[n] × X,Y). Restriction is precomposition on Delta[n]. Evaluation at the identity simplex and the map induced by each simplex of Z give inverse correspondences between maps Z × X → Y and Z → Y^X. The main reader rechecked the evaluation/restriction compatibility and the inverse constructions. This verifies the stated closure claim at that level; it is not a check of the separate realisation or spectral-sequence claims.',
 '[S013-dold-kan-grading; item 3] A and C checked the unqualified phrase chain complexes. The ordinary normalization construction has no negative degrees. In particular, the complex with Z only in degree -1 cannot be isomorphic to a normalized simplicial abelian group. The main reader rechecked this degree obstruction. Thus the usual Dold–Kan reading presupposes a nonnegative grading convention; that convention may be implicit, so the page is not called refuted. The ink has no degree qualifier and none is inserted.',
 'The only supplied wording alternative concerns the abrupt satisfies … is homeomorphic junction. All three readers confirm the direct typed transition; it is an unchanged C-context decision, not a literal correction or removed uncertainty mark. No authorial question mark, à vérifier, or similar proof qualification appears on this sheet.'
]
events=[];date=datetime.now(timezone.utc).strftime('%Y-%m-%d')
for r in 'ABC':
 for x in R[r]['math_checks']:
  sid='S013-cartesian-closure' if 'cartesian' in x['statement_id'] else 'S013-dold-kan-grading'
  events.append({'statement_id':sid,'date':date,'who_model_effort_run':f'GPT-6 Astra Pro; effort not exposed; /root/scan013_{r.lower()}', 'type':x['type'],'outcome':x['outcome']+' Note N013.'+('5' if 'cartesian' in sid else '6')+'.','original_reader_statement_id':x['statement_id']})
events.extend([
 {'statement_id':'S013-cartesian-closure','date':date,'who_model_effort_run':'GPT-6 Astra Pro; effort not exposed; /root','type':'used and rechecked in this run','outcome':'Reviewed both readers’ explicit exponential constructions. Evaluation sends (e,x) to e_n(id_[n],x); precomposition makes evaluation simplicial. The simplexwise maps obtained from F: Z × X → Y reverse evaluation, since restriction along each beta recovers F(Z(beta)z,x). The two constructions are inverse. This supports the concise claim in N013.5, without checking the other numbered assertions.'},
 {'statement_id':'S013-dold-kan-grading','date':date,'who_model_effort_run':'GPT-6 Astra Pro; effort not exposed; /root','type':'used and rechecked in this run','outcome':'Reviewed A/C’s normalization-degree observation: all normalized groups below degree zero vanish, whereas the complex concentrated as Z in degree -1 does not. No isomorphism can identify their degree -1 groups. This is a scope qualification for the usual normalization interpretation, not a refutation of a possible implicit nonnegative convention. Used in N013.6; literal chain complexes retained.'}
])
rec=write_record(13,'B','brief_v04.md + clarification_scan013.md',texts['B'],[],doubt_decisions(R['A'],13,'A'),[],notes,
 'All three complete LaTeX readings agree with C apart from the cote wrapper. The root compared all full texts, change/context reports and inventories. There are eleven correction entries, the internal section heading, title and underline, opening p3 paragraph, three numbered paragraphs, both inline products, unfinished final paragraph and archive number. Reader B’s 23-row inventory includes the table container and both inline formulas. No disagreement required a main-reader crop; the readers’ 3/1/0 crops settled their individual open places. H has no transcription and contributes no rows.',events=events,
 equivalences=['C_context alternatives confirmed without changing literal C uncertainty markup are recorded as decisions only. No C reading or uncertainty mark changed.','The table is encoded by the supplied diagram macro around tabular; it is inventoried as a displayed table, not a mathematical arrow diagram.'],notation=R['A']['notation'])
print('Scan 013 confirmed unchanged; 23 inventory elements; 6 actual mathematical events.')
