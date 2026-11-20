from pathlib import Path
import json,csv,datetime
R=Path(__file__).resolve().parents[1]
d=json.loads((R/'review/scan008_review.json').read_text());d['scan']=8;d['status']='root initial adjudication complete; blind reading pending'
old=(R/'review/scan008_proposed.tex').read_text()
compat=r'\mathrel{\tikz[baseline=-.4ex,x=.65em,y=.65em]{\draw (0,1.1)--(1,.5)--(0,-.1) (1,1.1)--(0,.5)--(1,-.1);}}'
margin=r"Un atelier sera dit \uline{spacieux} s'il satisfait cette condition. Contre-ex. : les ateliers simpliciaux\ldots"
repls=[
(r'\unsure{\mathscr F|\mathcal F|F}',r'\mathscr F'),(r'\unsure{M|\mathcal M}','M'),
(r"``$F$ et $G$ \uline{disjoints}''",r"``$F$ et $\unsure{G|C}$ \uline{disjoints}''"),
(r'F\parallel G\ \overset',r'F\parallel\unsure{G|C}\ \overset'),
(r'F\cap G=\varnothing',r'F\cap C=\varnothing'),
(r'K=F\cap G=',r'K=F\cap\unsure{C|G}='),
(r'\deleted{\unsure{\widetilde Y|Y}}\widetilde G',r'\deleted{\unsure{\widetilde Y|Y}}\unsure{\widetilde G|\widetilde C}'),
(r'\text{Alors } F'+compat+'G',r'\text{Alors } F'+compat+'C'),
(r'Y\ll G,',r'Y\ll C,'),
(r'\margin{'+margin+'}',r'\margin{\unsure{'+margin+r'|\deleted{'+margin+'}}}')]
def conv(s):
 for a,b in repls:s=s.replace(a,b)
 return s
text=conv(old).replace('% First-reader proposal, scan 008; root adjudication pending.','% Root initial adjudication; blind second reading pending.')
removed={8,12,13,34,38,46,53}
cs=[]
for c in d['changes']:
 n=int(c['id'].split('-')[-1])
 if n in removed:continue
 c['crop']='crops/'+Path(c['crop']).name;c['final']=conv(c['final'])
 if n==27:c['scan_shows']+=' Root retains the live note as primary but marks the alternative whole-note deletion in place: one continuous block strike intersects it, without a distinct cancellation confined to its four lines. The scope is not certain.'
 if n==48:c['scan_shows']+=' The final rounded operand is also G/C uncertain because old strokes prevent isolating an internal G bar.'
 c['consequential']=n in {7,28,31,32,35,36,39,40,41,45,47,48,49,50,52,55}
 cs.append(c)
def add(i,place,final,obs,crop,box,confidence='medium'):
 cs.append(dict(id=f'008-{i:02d}',place=place,C='G',H='G',final=final,scan_shows=obs,confidence=confidence,kind='misread symbol or index',crop='crops/scan008_'+crop+'.png',box=box,against_C=True,against_H=True,marked_in_H=False,consequential=True,consequence='Literal C-shaped ink is retained even though the surrounding two-variable statement would require G.'))
add(57,'First definition, intersection operand',r'F\cap C','Root sees an open bowl with a flat outward lower arm and exterior downturn, without the interior returning bar clearly present in the preceding G after the compatibility sign. Both witnesses silently use G.','definition_formula',[510,770,1450,905])
add(58,'Cancelled Cor, K definition',r'K=F\cap\unsure{C|G}','The principal outline is open and C-shaped. An extra short stroke at the upper-left interior makes the exact letter doubtful; it is not the right-side G bar. Root preserves C first and G as the alternative, without using the expected formula to select G.','Cor_formula',[470,2025,1555,2175],'low')
add(59,'Cancelled Cor, compatibility assertion',r'F'+compat+'C','The open bowl has an outward lower arm and terminal downturn, with no separate returning internal bar. Root and the first reader on reinspection prefer literal C.','Cor_final',[565,2150,1510,2305])
add(60,'Cancelled Cor, second refinement premise',r'Y\ll C','The second operand is a particularly open C with a near-flat lower arm and short exterior downturn. No internal horizontal G bar is visible.','Cor_final',[565,2150,1510,2305])
d['changes']=cs
for item in d['difference_review']:
 item['change_ids']=[x for x in item.get('change_ids',[]) if int(x.split('-')[-1]) not in removed]
 if any(s in item.get('classification','') for s in ['alphabet','ambient M']):item['classification']+='; recurring alphabet rendering consolidated at first defining occurrence on003/004, not counted repeatedly as macro differences'
d['doubts']=[q for q in d['doubts'] if q['place'] not in ['Empty-set subscript','First ambient M']]
for q in d['doubts']:
 if q['place']=='Slanted margin, cancellation scope':q.update(reading='live complete note',alternatives=['whole note cancelled'],reason='One of the long diagonal block strikes crosses the slanted note; it does not independently establish the intended cancellation extent. The alternatives are now encoded in place, with the complete wording retained in both.',confidence='low')
d['doubts'] += [
 dict(place='Quoted definition, second named letter',reading='G',alternatives=['C'],confidence='low',reason='Open bowl with returning terminal but no distinct interior bar; local use of G supplies the primary candidate without making the stroke certain.'),
 dict(place='First definition, operand after parallel sign',reading='G',alternatives=['C'],confidence='medium',reason='More sharply inward lower return than the subsequent clear C-shaped intersection operand; still lacks the full internal bar of the next G.'),
 dict(place='Cancelled Cor, intersection operand',reading='C',alternatives=['G'],confidence='low',reason='Open C contour plus an additional upper-left interior stroke; neither certain G nor uncorrected simple C is established.'),
 dict(place='Cancelled Cor, surviving second Sup operand',reading=r'\widetilde G',alternatives=[r'\widetilde C'],confidence='low',reason='The wave is visible but older strokes interfere with the internal portion of the rounded letter.'),
]
d['root_adjudication']={'reader':'GPT-6 Astra Pro root; effort not exposed','viewed':'whole once, both halves once, all18 saved crops','decisions':['All local correction states preserved inside the common lower-block cancellation.','Margin cancellation scope is marked in place rather than merely relegated to a note.','C/G decisions distinguish the visible internal bar from open outlines, occurrence by occurrence; expected G never supplies missing ink.','M and script F alphabet doubt consolidated at first occurrences on003/004.','Literal ses and the upper-right gap of its oval retained.']}
for h in d['hand_log']:
 if 'G can' in h['habit']:h.update(habit='C-shaped and barred G forms need local discrimination',observation='The earlier categorical claim that all open forms are shortened Gs is withdrawn. Clear barred G occurs beside open C-shaped operands; several intermediate forms remain uncertain. This is not a universal all-C or all-G rule.')
for q in d['notes']:
 if q['id']=='008-N2':q['claim']='The first reader performed no mathematical proof check; root later checked the stratum criterion conditionally, as recorded in the page notes and CHECK_EVENTS.'
 if q['id']=='008-N3':q['claim']='The exact deletion scope of the slanted note remains uncertain and is explicitly marked in the transcription.'
bs=d['second_boxes']
for i,b in enumerate(bs,1):
 b['source_box_id']=b['box'];b['box']=f'B{i:03d}';b['reading']=conv(b['reading']).replace('\n',' ')
 k=b['kind']
 if k=='number':b['kind']='central handwritten numerical inscription, including any corrections and underlining'
 elif i==17:b['kind']='complete slanted marginal note, including all text, punctuation and crossing strokes; rotate upright'
 elif i==40:b['kind']='complete central lower text block, including all formulas, corrections and crossing strokes; exclude separate upper-right paragraph and left slanted note'
 elif k=='drawing':b['kind']='central inscription with its complete enclosing stroke; reproduce both'
 elif k=='formula':b['kind']='whole central formula or formula group, including corrections, indices, punctuation and graphic marks'
 elif k in ['insertion','deletion']:b['kind']='central correction group, including text, source state and attachment'
 else:b['kind']='complete central inscription, with punctuation and source state'
d['second_boxes']=bs
for e in d['inventory']:
 if e['element']=='Definition of disjoint F,G':e['first_words_or_objects']=r'F\parallel G/C; labelled equivalence; compatibility; F∩C=empty figure'
 if e['element']=='Cor heading and Sup formula':e['first_words_or_objects']=r'Cor Soient F,G∈script F, K=F∩C/G=Sup Z.'
 if e['element']=='Cor two-row assertion':e['first_words_or_objects']=r'Alors F compatibility C, circled ses, ∀X,...∈M; Y≪C in final implication'
 if e['element']=='Four-line diagonal note':e['position']+='; cancellation scope uncertain, both alternatives recorded'
(R/'pages/H156-01_156-7_scan008.tex').write_text(text)
(R/'review/scan008_final.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
base=R/'second/H156-01_156-7_scan008'
for suffix,cols in [('_boxes.tsv',['box','kind','x0','y0','x1','y1']),('_first.tsv',['box','reading'])]:
 with Path(str(base)+suffix).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=cols,delimiter='\t',extrasaction='ignore');w.writeheader();w.writerows(bs)
now=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (R/'review/root_visual_log.tsv').open('a') as f:
 for p in sorted((R/'crops').glob('scan008_*.png')):f.write(f'8\tcrops/{p.name}\t{now}\troot direct crop inspection completed before adjudication\n')
 f.write(f'8\twhole + a + b\t{now}\troot continuous layout and line reading completed; wholly truncated crop batch not counted\n')
print(len(cs),'records;',len(bs),'blind boxes;',len(d['doubts']),'remaining doubts')
