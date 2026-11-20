from audit import *
k='120_scan007'
replace_text(k,[(r'\unsure{\Sigma}',r'\unsure{E|\Sigma}')])
revise_change(k,'parenthetic revision',diff_C='no')
rows=readtsv('CHANGE_LEDGER.tsv')
for r in rows:
 if r['page']==k and r['place']=='lower diagonal note, first paragraph':
  r['final']=r['final'].replace(r'\unsure{\Sigma}',r'\unsure{E|\Sigma}')
  r['scan_shows']='The rotated note visibly begins Quand on n’a pas (M0), mais que l’on suppose (M5), alors la réunion des A∈M1, fait que. Later joins overlap the baseline formula and remain doubtful; the isolated double-curved letter is more like E, with Sigma retained as an alternative.'
rewrite_tsv('CHANGE_LEDGER.tsv',rows)
ds=readtsv('DOUBTS.tsv')
for r in ds:
 if r['page']==k and r'\Sigma' in r['reading']:
  r['reading']=r'\unsure{E|\Sigma}';r['alternatives']='double-curved E-like letter; Sigma less likely';r['confidence']='low'
rewrite_tsv('DOUBTS.tsv',ds)
add_certainty(k,[
 ('deleted products adjective',r'\unsure{fibrés|finis}','fibrés','The tall f, low ibr and final accent and s remain visible in the deleted phrase.','page','high'),
 ('nested parenthetic revision',r'\unsure{\deleted{(de deux objets}|(de deux objets}',r'\deleted{(de deux objets}','The extra horizontal strike crosses the opening words of the inserted parenthesis; the first alternative is retained.','120_scan007 (990,830,1660,995)','medium'),
 ('last deleted article',r'\unsure{le}','le','The l ascender and low e survive at the end of the larger cancelled passage.','page','medium'),
 ('last deleted noun',r'\unsure{foncteur}','foncteur','The long f and subsequent joined letters are still readable under the cancellation.','page','medium')
])
finish(k,'Reread both pagination marks, the transport diagram, the nested cancellations, live finite-limit replacement, second proposition and both long slanted notes. Re-inspected the existing lower-note crop: the isolated letter is better represented as uncertain E with Sigma as alternative, in light of its two curved lobes. Its uncertainty is preserved. Corrected the parenthetic-revision C flag to certainty-only; the H insertion/deletion difference remains. The true formula quantifiers are retained, distinct from tt on other leaves.')
