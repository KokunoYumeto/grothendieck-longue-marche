from pathlib import Path
import json,copy
O=Path(__file__).resolve().parents[1]
R={a:json.loads((O/f'readers/scan072/{a}/report.json').read_text()) for a in 'ABC'}
A,B,C=[R[a]['decisions'] for a in 'ABC']
ds=[]
for k,ai,ci in [(0,0,0),(1,1,1),(2,2,2),(3,4,4)]:
 d=copy.deepcopy(B[k]);d['id']=f'M072-{k+1:02}'
 d['readers']={'A':A[ai]['reading'],'B':B[k]['reading'],'C':C[ci]['reading']}
 d['marked_in_H']='no'
 d['crop']='readers/scan072/B/'+d['crop']
 if isinstance(d.get('alternatives'),list):d['alternatives']='; '.join(d['alternatives'])
 ds.append(d)
ds[0].update(reading=C[0]['reading'],scan_shows='The 7 has a curved upper stroke, descending leg and crossbar. A short oblique left dash sits higher than the longer, nearly horizontal right dash. All readers restore both strokes; main preserves the height difference shown in C’s rendering. The numeral value is settled.')
ds[1]['scan_shows']='A thin uneven pen line runs beneath the entire typed parenthesis, turns upward at the right end, and meets a pointed downward bend at the left. A separate upright branch enters that bend. Its low point lies immediately before une on the following main line. All three readers identify the connector; main adopts B’s anchored drawing, retaining the typed text inside the insertion marker.'
ds[2].update(confidence='low',scan_shows='The isolated form has an upper-left hook, a descending curved member with a low right turn, and an ascending diagonal crossing through the middle. These favor x; no independent terminal e loop can be recovered. The separate se at the end of généralise has a clearer e, but that comparison cannot exclude a compressed joined se here. All readers retain both candidates; main keeps the uncertainty and does not settle it from French grammar.',alternatives='x; compressed joined se')
ds[3].update(confidence='medium',scan_shows='Two irregular dark lobes rise diagonally from lower left to upper right. A smaller round dark satellite sits left of the upper lobe and is distinctly darker than the pale surrounding grain. A and C represent only the two main forms; B includes the satellite. Main preserves all three visible components using B’s drawing. Their material origin, deliberate status and any punctuation function remain unresolved.',alternatives='deliberate detached mark; incidental ink or scan trace; no punctuation value established')
s=(O/'readers/scan072/B/reading.tex').read_text().replace(B[0]['reading'],C[0]['reading'])
(O/'pages/B37-04_37_scan072.tex').write_text(s.rstrip()+'\n\\clearpage\n')
notes="""One typescript continuation with four entries on pages 25–28, a typed interlinear qualification, a handwritten insertion connector and a handwritten footnote. Its own number is - 7 -, with the left dash raised, and its archive number is 71; no title, date or signature is present. The number is not an explicit statement of a total page count. No cancellation, formal display or mathematical diagram is visible.

The author asks for a ‘hint pour’ ‘il n’est pas difficile de montrer ...’, questions ‘dont on peut penser que c’est le même ...’ with ‘y a-t-il ... une caractérisation d’un homomorphisme (7.17.4.1) ?’, and qualifies that question by ‘(dans la situation présente, i.e. S local régulier de pt fermé s)’. The handwritten question reads ‘Est-ce que 7.2 ne [x|se] généralise pas ?’; the square-bracket alternatives here report the transcription’s uncertainty, not marks supplied by the writer. The p.27 entry explicitly contrasts ‘au-dessus’ with ‘au dessus’, and ‘dans le normalisé’ with ‘du normalisé’. The p.28 entry reports the missing Abhyankar reference.

The one explicit C doubt, repeated in C’s context table, remains unresolved. The connector and the detached lower-right cluster are restored; the cluster’s two lobes and small satellite are represented without calling them punctuation or assigning an author. H supplies description only and has no collation rows. These are reports of the page’s questions and requests; no proof or mathematical computation was performed."""
notation=copy.deepcopy(R['B']['notation'])
out=dict(scan=72,decisions=ds,inventory=R['B']['inventory'],notes=notes,math_reading_decisions=R['C']['math_reading_decisions'],notation=notation,abbreviations=R['B']['abbreviations'],slips=[],check_events=[],main_crops=[],main_image_delivery={'requested_files':['B072_01_pagination.jpg','B072_03_footnote_x_se.jpg','B072_02_insertion_connector.jpg','B072_04_detached_pair.jpg'],'successfully_viewed':4,'delivery_issue':'The initial combined request for B072_02 and B072_04 returned only a context-truncation notice and no visible images. The same retained files were subsequently delivered separately for their first actual main-reader viewing. No new crop was made.'})
(O/'decisions/scan072.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
with (O/'workflow_assessment.txt').open('a') as f:f.write('\nScan 072: all readers returned four mandatory loci (A and C additionally logged the confirmed hyphen contrast). A made 3 crops, B 4 and C 4; main reused B’s four and made none. One main-reader two-image response was truncated before images were delivered; the same retained files were successfully delivered individually for first actual viewing. No settled locus was recropped. The small satellite in the detached cluster was present in B’s drawing and confirmed by main; A and C omitted it.\n')
print('Wrote scan 072: four mandatory records, three C differences, one explicit C doubt retained.')
