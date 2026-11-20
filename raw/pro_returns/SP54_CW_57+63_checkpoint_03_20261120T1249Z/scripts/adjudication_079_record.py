#!/usr/bin/env python3
"""Root's completed visual adjudication of scan 079."""
from pathlib import Path
import copy,json
b=Path('/workspace/scratch/b9993b8b5640');o=b/'out';p='A57-02_57_scan079';rp=o/'readers'/p;ap=o/'adjudication'/p
r={n:json.loads((rp/n/'report.json').read_text()) for n in ['R1','R2','R3']}
m1=[0,1,2,3,None,4,5,6,7,14,8,9,10,11,12,13]
m2=[0,1,2,3,None,4,5,None,6,None,7,8,9,10,11,12]
paths=[str(rp/'R1/crops/01_solution.png'),str(rp/'R1/crops/02_any.png'),str(ap/'findin.png'),str(rp/'R3/crops/03_set.png'),str(rp/'R3/crops/03_set.png'),str(rp/'R3/crops/03_set.png'),str(rp/'R3/crops/03_set.png'),str(rp/'R1/crops/04_dimension.png'),str(rp/'R1/crops/05_local.png'),str(rp/'R1/crops/05_local.png'),str(rp/'R3/crops/06_analogous.png'),str(ap/'far_exclamation.png'),str(rp/'R1/crops/07_i.png'),str(rp/'R1/crops/07_i.png'),str(ap/'fact_comma.png'),str(ap/'closing_signature.png')]
shows=[
 'The eight-position cancelled word retains a tall l-like trace, a t crossbar and a dotted i amid the x overtype. The rounded bodies remain obscured; solution stays tentative.',
 'The final character after an has a y-shaped descender and a dense superposed upper body. The crossing and live letter shapes cannot be separated securely, so both cancellation states remain.',
 'The d overlaps the preceding n impression. The following i and n occupy the adjoining typed sequence, with no full blank character position before i. Root retains findin, at medium confidence because the shifted d makes the visible gap uneven.',
 'The cancelled three-position group retains a tall terminal t and its crossbar; the initial curved bodies are partly obscured. The proposed set remains tentative.',
 'The first open-set subscript has a broad foot and a short upright, with a detached upper horizontal flag-like mark. The flag favors 1, while its separation from the upright also permits i. Root retains 1/i rather than using the later indices to settle this occurrence.',
 'The product between X and S_1 is a lowercase serifed typewriter x at the baseline, with a lowered S. This is a visible-glyph distinction; no mathematical claim is changed.',
 'A blank typewriter position separates the final S with its lowered 1 from the following period.',
 'At the right edge only dime is visible before the dark cutoff; the next line starts sion. The intervening n in the proposed word dimension cannot be inspected. The C uncertainty remains, unlike H\'s unmarked whole word.',
 'The long pen stroke runs beneath the raised noetherian and connects to the curved ends surrounding that insertion. It touches the tops of local; its short downward hook is in the gap before local. Root follows R3 and C on live local, at medium confidence. The complete visible path is drawn so its contact is preserved.',
 'The correction has a left upcurved end, a shallow lower connecting line, a right upcurved end, and a small downward hook after general. These strokes and the interlinear noetherian are drawn with the baseline words at their visible relative positions. The figure is held inline to preserve the body paragraph.',
 'There are ten typed positions: a n a l o g, a crowded extra character, o u s. In the tighter existing R3 crop the extra character has a dark upper shoulder favoring n; the lower joined strokes still allow u. Root records analognous/analoguous, retaining both. C and R2 omit that extra position. Both existing reader crops were considered; no new crop of the place was made.',
 'A full blank character position separates the r of far from the exclamation mark; the closing parenthesis and period follow.',
 'The typed t retains its upright, crossbar and foot to the left of the heavy handwritten stroke. A rounded o with a pale interior remains beneath that stroke. The overwritten to is preserved.',
 'A leftward top bar meets the right-hand descending stroke, which turns deeply left into a rounded lower hook. The shape favors J, with I retained as an alternative. The sentence did not select the letter.',
 'A full blank character position stands between fact and the comma.',
 'The typed Sincerely yours stands on the left, with the autograph A Grothendieck to its right on the same horizontal band. The signature\'s tall and descending strokes do not make it a separate following line. The closing has a small left indentation.'
]
conf=['medium','low','medium','medium','low','high','high','medium','medium','high','low','high','medium','medium','high','high']
finals={4:r'S_{\unsure{1|i}}',10:r'\unsure{analognous|analoguous}',15:r'\noindent\hspace*{1cm}Sincerely yours\hfill\handwritten{A Grothendieck}\par'}
changes=[]
for i in range(16):
 reads={'R3':r['R3']['changes'][i]['reading']}
 for n,m in [('R1',m1),('R2',m2)]:
  if m[i] is not None:reads[n]=r[n]['changes'][m[i]]['reading']
  elif i==4:reads[n]='S_1'
  elif i==7:reads[n]=r'\unsure{dimension}'
  elif i==9:reads[n]=r'\inserted{noetherian}; attachment encoded by insertion macro, no explicit path'
 x={'source':['R3',i],'reader_readings':reads,'crop':paths[i],'evidence':paths[i],'scan_shows':shows[i],'confidence':conf[i],'mathematical_consequence':None}
 if i in finals:x['final']=finals[i]
 if i==10:
  x['differs_h']=True
  x['evidence']=str(rp/'R1/crops/06_analogous.png')+'; '+paths[i]
 if i==8:x['mathematical_consequence']='The baseline word local is retained live below the inserted noetherian; H gives local as cancelled.'
 if i==4:x['mathematical_consequence']='The first open-set subscript remains uncertain between 1 and i; both witnesses print a definite 1.'
 changes.append(x)
cd=copy.deepcopy(r['R3']['c_doubts'])
for d,i in zip(cd,[0,1,3,7,13]):d.update(evidence=shows[i],crop=paths[i],confidence=conf[i])
remaining=copy.deepcopy(r['R3']['remaining_doubts'])
for d,i in zip(remaining,[0,1,3,4,7,13]):d.update(reason=shows[i],crop=paths[i],confidence=conf[i])
remaining[3].update(reading=finals[4],alternatives=['S_1','S_i'])
remaining[4]['alternatives']=['dimension; letters at the right cutoff cannot be inspected']
remaining.insert(5,{'place':'L15, adjective after very','reading':finals[10],'alternatives':['analognous','analoguous'],'confidence':'low','reason':shows[10],'crop':paths[10]})
inv=copy.deepcopy(r['R3']['inventory']);inv[4]['first_words_or_objects']='S with uncertain 1/i subscript';inv[13]['kind']='text'
notes={'summary':r['R3']['notes']['summary'],'reading_decisions':[{'place':'L06–L07, open-set index and base-change expression','readings':r'S_1 versus S_i at first occurrence; later X_1 and S_1','reason':shows[4]+' The later indices have attached upper flags and remain 1. No expected indexing convention was used to remove the first doubt.'},{'place':'L12, general noetherian local ring','readings':r'local; \deleted{local}; \unsure{local|\deleted{local}}','reason':shows[8]}],
 'author_checks':copy.deepcopy(r['R1']['notes']['author_checks']),'titles_dates_pagination':copy.deepcopy(r['R2']['notes']['titles_dates_pagination']),
 'witness_boundary':r['R3']['notes']['witness_boundary'],
 'drawing_representation':'The complete noetherian correction is represented with its visible path and labels. A minipage holds this source fragment inline so the single main body paragraph continues through it. The local word remains live; the line\'s contact with its upper strokes is still visible in the reproduction.',
 'uncertain_spelling':'The ten-position adjective retains analognous/analoguous. C/R2\'s nine-position analogous was not adopted; the extra character is visible but its crowded shape remains unresolved.'}
notation=copy.deepcopy(r['R3']['notation']);notation[1].update(latex=finals[4],visible_shape=shows[4],alternatives=['1','i'])
prior=copy.deepcopy(r['R3']['prior_flags']);prior[1]['outcome']='L07 indices confirmed as 1; first L06 index retained as 1/i from the crop context.'
text=(rp/'R3/reading.tex').read_text()
oldfig=r['R3']['changes'][9]['reading'];newfig=oldfig.replace('  \\draw[line width=0.45pt] (1.07,0.72)','  \\handwritten{\n  \\draw[line width=0.45pt] (1.07,0.72)',1).replace('.. (1.74,-0.02);','.. (1.74,-0.02);\n  }',1)
newfig=r'\begin{minipage}[c]{4.7cm}'+'\n'+newfig+'\n'+r'\end{minipage}'
changes[9]['final']=newfig
repl=[(r'S_{\unsure{i|1}}',finals[4]),('very analoguous','very '+finals[10]),(oldfig,newfig),(r'\noindent Sincerely yours\hfill\handwritten{A Grothendieck}\par',finals[15])]
views=list(dict.fromkeys(paths));views.append(str(rp/'R1/crops/06_analogous.png'))
cfg={'base_reader':'R3','replacements':[{'old':a,'new':z} for a,z in repl],'changes':changes,'c_doubts':cd,'remaining_doubts':remaining,'inventory':inv,'notes':notes,'notation':notation,'prior_flags':prior,'adjudicated_crops':views,'reader_only_decisions':[],'rejected_difference_rows':[]}
(ap/'decision.json').write_text(json.dumps(cfg,ensure_ascii=False,indent=2))
with (o/'notation.md').open('a') as f:
 f.write('\n## Evidence added at cote 57, scan 079\n\n| Sign | Reading | Place | Visible form / residual alternatives |\n|---|---|---|---|\n')
 for n in notation:f.write('| '+n['sign']+' | `'+n['latex'].replace('|',r'\|')+'` | '+n['place']+' | '+n['visible_shape'].replace('|',r'\|')+' |\n')
brief=(o/'briefs/reader_brief_v08.md').read_text().replace('brief v08','brief v09',1).replace('First used: cote 57, scan 079.','First used: cote 63, scan 003.',1)
brief+='\n\n## Clarifications introduced in v09\n\n- A correction stroke can touch a baseline word while forming part of an insertion bracket. Record the complete path and any uncertain cancellation state; where its shape is material, reproduce the source fragment in TikZ without duplicating its words. Keep a prose paragraph continuous with an inline carrier when possible.\n- Report a newly exposed index or glyph uncertainty in a crop\'s immediate context even when it was not the crop\'s original target. Read that occurrence from its own strokes, without imposing nearby indices.\n- A witness extract may include a following section whose editorial note explicitly names a later page. Respect the assigned page_map boundary; following-page headings are not omissions on the assigned page, and no following image is to be opened.\n'
(o/'briefs/reader_brief_v09.md').write_text(brief)
f=o/'records/brief_changes.json';v=json.loads(f.read_text());v.append({'version':'v09','first_page':'H63-01_63_scan003','reasons':['Scan-079 readers differed on the interpretation and drawn representation of the noetherian correction. The complete path and paragraph continuity are now explicit.','R3 exposed a new small-index uncertainty in the cancelled-word crop; the brief emphasizes reporting such context findings.','The H extract included a section explicitly assigned to the following page. The boundary clarification sent to all three readers is retained as a general instruction.']});f.write_text(json.dumps(v,ensure_ascii=False,indent=2))
print('Page 079 decision specification: 16 rows; 7 doubts; 14 inventory elements; '+str(len(views))+' root-viewed crops.')
