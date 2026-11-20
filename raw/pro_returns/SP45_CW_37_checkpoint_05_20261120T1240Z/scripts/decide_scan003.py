#!/usr/bin/env python3
"""Encode main-reader adjudication after inspecting the scan-003 crops."""
from pathlib import Path
from datetime import datetime,timezone
import copy,json,shutil
root=Path(__file__).resolve().parents[1]
rs=[json.loads((root/f'readers/scan003/r{i}/report.json').read_text()) for i in [1,2,3]]
d=copy.deepcopy(rs[0]);now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
d.update(folder='B37-01',their_page=2,hua_has='text',filename='B37-01_37_scan003.tex',decided_utc=now,brief_version='v001',reader_crop_counts=[13,15,14],main_crop_count=11)
# The main reader independently inspected all 13 r1 crops and the eleven
# additional main crops. Its selected reading matches r1's full page.
shutil.copyfile(root/'readers/scan003/r1/reading.tex',root/'pages'/d['filename'])
r2map=[0,16,1,2,18,3,4,5,[19,20],21,22,24,17,6,7,8,9,9,23,None,10,11,12,13,14,15]
r3map=[0,1,2,3,4,5,6,7,10,11,12,13,14,15,16,17,8,9,18,19,20,21,22,23,24,25]
mainmap={0:0,1:1,4:4,8:10,9:11,10:12,11:13,12:14,14:16,18:18}
for i,c in enumerate(d['changes']):
    j=r2map[i]
    r2='; '.join(rs[1]['changes'][k]['reading'] for k in j) if isinstance(j,list) else (rs[1]['changes'][j]['reading'] if j is not None else 'Separate 30 and 70 frames; lower frame retraced (reading.tex).')
    if i==16:r2=r'\unsure{tel|Cl}'
    if i==17:r2=r'\unsure{Saarbach}'
    c['readers']={'r1':rs[0]['changes'][i]['reading'],'r2':r2,'r3':rs[2]['changes'][r3map[i]]['reading']}
    c['evidence']='Main reader inspected the indicated crop. '+c['evidence']
    if i in mainmap:c['crop']=f'crops/scan003/main_{mainmap[i]:02d}.jpg'
    if 'readable ink left' in c['kind']:c['kind']=r'readable ink left as \ill{}'
    if i==3:c['evidence']+=' Decision among the three: the flat top, left vertical and lower bowl establish 5. The internal rounded trace does not securely establish an earlier 3, so retain r1’s underprint alternative rather than r2’s unqualified 50 or r3’s two chronological alternatives.'
    if i==6:c['evidence']+=' The broad 1 foot and straight stem motivate listing 1 first; both orders remain marked, so no chronology is asserted.'
    if i==7:c['evidence']+=' Keep C/r1/r2 candidate order: a heavy X is directly visible; a distinct earlier I is possible but not established. R3 reverses only the preference.'
    if i==17:
        c['confidence']='medium';c['evidence']+=' R1 and r3 resolve the surname; r2 retains doubt. The main crop supports the full letter sequence, although the cursive joins justify medium confidence.'
    if i==19:c['evidence']+=' The main reader selects r1’s continuous retraced outer contour and internal divider. R2/r3 retain C’s two separately closed rectangles; that misses the continuity and retracing of the outer top edge.'
    if i==21:c['evidence']+=' R2 resolves r, whereas r1/r3 retain doubt. The cancelling x masks the shoulder enough that the main reader retains the r doubt.'
    if i==24:c['evidence']+=' All three recognize the same ei/ie superposition; their grouped versus character-by-character encodings are equivalent. The selected grouped encoding does not assert which sequence was typed last.'
    c['mathematical_consequence']=''
    assert c['crop'],(i,c['locus'])
# This accurate H description still substitutes prose for the actual mark.
d['changes'].insert(12,{'locus':'SGA 5 right bracket joining Exp XII and Exp XIV','c':'Right bracket drawn beside counts 100 and 20','h':'un crochet réunit « Exp XII » et « Exp XIV » de SGA 5 (description only)','reading':'Right square bracket drawn beside counts 100 and 20','diff_c':False,'diff_h':True,'kind':'drawing or diagram','marked_in_H':False,'confidence':'high','evidence':'Main crop shows a vertical pencil stroke with leftward horizontal ends beside 100 and 20. H describes its correct span but provides no drawing; the consolidated page retains the visible bracket.','crop':'crops/scan003/main_sga5_bracket.jpg','readers':{'r1':'Right bracket joins 100 and 20 (reading/inventory).','r2':'Same bracket (reading/inventory).','r3':'Same bracket (reading/inventory).'},'mathematical_consequence':''})
# C questions that were not actual in-place doubts remain documented, but are
# not counted as transcription changes.
for q in d['c_doubts']:
    if q['locus']=='SGA 7 first count':q['crop']='crops/scan003/main_16.jpg'
d['notes']=[
 {'id':'s003-note01','text':'Undated, unsigned typing plan headed “SGA : Manuscripts à frapper”. The four-column table lists SGA 1, an overtyped 4/2 label, SGA 5, SGA 6, and SGA 7. The entire SGA 1 row and SGA 6 block are cancelled. The page has no own page number; the pencilled archive 2 is retained only in a comment.','basis':'Scan 3 heading, nineteen table rows, cancellations and lower margin; three independent readings, with main crops for differing loci'},
 {'id':'s003-note02','text':'The NB assigns a precise meaning to its marks: underlined counts identify manuscripts already available, while counts followed by ? concern texts whose drafting is uncertain (“il n’est pas certain qu’ils seront rédigés”). The 80 for Exp V is not underlined.','basis':'Scan 3 NB and table; main_04 and main_10 crops'},
 {'id':'s003-note03','text':'The final paragraph reports about 250 pages ready, hopes for another “env.” 200/300 pages for SGA 4 in two or three months, and projects 450 à 500 pages in five or six months. The 2/3 is visibly overtyped; arithmetic was not used to infer which strike came last. The writer qualifies the forecast: “J’espère”, then “Cependant je ne peux le garantir”; it depends on Mr. Verdier at Brandeis “cette année”. No date is inferred from that wording.','basis':'Scan 3 final paragraph; three line-by-line readings and r1 crop 12'},
 {'id':'s003-note04','text':'The table carries source question marks beside the SGA 5 Exp IV author and 100, the cancelled Ferrand 70, and the first SGA 7 author and 120. Other listed counts are: cancelled SGA 1 10 p; SGA 4/2 50 (possible underprint), 80, 50, overtyped 10/50, 30, 10; SGA 5 50, 70, 100, 20, 15 after its 100 ?; cancelled SGA 6 10 after 70 ?; SGA 7 30, 70, 15 after 120 ?. These are documentary counts, not a checked sum.','basis':'Scan 3 table, all nineteen rows; r1 inventory cross-compared with r2 and r3'},
 {'id':'s003-note05','text':'The NB proposes a forfait for each seminar after discussing correction work with the secretary. The typed forms “rénumération” and “sécrétaire” are preserved, together with “rédigés” in the later phrase about pages. The overtyped ei/ie slots in the first viennent are retained with both orders.','basis':'Scan 3 NB and final paragraph; r1 crops 09–11 and the three readers’ unchanged-word checks'},
 {'id':'s003-note06','text':'The three pencil notes read tel/Cl Saarbach (first cluster unresolved), écrire Bucur, and écr. Deligne. The hand is not identified from this sheet alone. The main reader selected a retraced outer frame divided between the SGA 7 counts, after comparing all three drawings. No mathematical proposition or proof was checked on this administrative page.','basis':'Scan 3 margins and frame; r1 crops 07 and 13; main_13'}]
d['check_events']=[{'statement_id':x['id'],'date':now,'who':'GPT-6 Astra Pro; effort inherited, not independently exposed; main scan003 adjudication','type':'used and rechecked in this run','outcome':'Documentary/source-content observation checked against the three independent ink readings and the cited main-reader crops. This does not assert a mathematical proof or verification of the historical forecast.'} for x in d['notes']]
d['workflow_observation']='All three agree on Manuscripts, sécrétaire and the cancelled Roman letters. They differ on underprint certainty, preferred order, surname confidence and frame geometry; main crop decisions retain nine unresolved loci. Half-settled differences needed source bboxes for main review.'
d['adjudication_note']='The complete main reading is r1’s reading after independent crop adjudication, not a majority selection. Every witness discrepancy was inspected on a retained crop. The three readers differ materially at the first underlined count, preferred VI B overprint order, Appendice undertrace preference, Saarbach certainty, the cancelled r after mise, and frame geometry; the rows above preserve their alternatives. The three encodings of the ei/ie transposition convey the same ink. Changes in doubt state are included in the counts and are not all categorical witness errors.'
d['main_viewed_crops']=[f'readers/scan003/r1/crops/{p.name}' for p in sorted((root/'readers/scan003/r1/crops').glob('*.png'))]+[str(p.relative_to(root)) for p in sorted((root/'crops/scan003').glob('*.jpg'))]
# Top-to-bottom inventory, with corrections/notes next to their source rows.
order=['heading','table','row01','delete-sga1','margin-saarbach','row02','over-label','over-iv-count','leader-iv','row03','brace-sga4','bracket-sga4','row04','row05','over-saint','over-vib','row06','row07','over-appendix','row08','row09','leader-vii','row10','leader-xi','row11','bracket-sga5','margin-bucur','row12','row13','row14','delete-sga6','row15','row16','over-range','row17','over-v','frames','margin-deligne','row18','leader-vi','row19','nb','delete-mise','over-correction','last-paragraph','over-viennent','over-200']
rank={f's003-{k}':i for i,k in enumerate(order)};d['inventory'].sort(key=lambda x:rank[x['element']])
(root/'decisions/scan003.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
with (root/'progress.log').open('a') as f:f.write('scan 003 done '+now+'\n')
print('Scan 003 adjudicated and page written.')
