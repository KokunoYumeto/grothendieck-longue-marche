from pathlib import Path
import json,csv,datetime
R=Path(__file__).resolve().parents[1]
d=json.loads((R/'review/scan006_review.json').read_text());t=(R/'review/scan006_proposed.tex').read_text()
t=t.replace(r'\unsure{\mathscr F|\mathcal F}',r'\mathscr F').replace(r'\unsure{M|\mathcal M}','M')
# Root reinspection confirms the underline ends before the live numeral; keep At only.
t=t.replace(r'\unsure{intrinsèq.|intrinsèque}',r'\unsure{extrinsèq.|intrinsèq.}')
# New root reading of a compressed abbreviation remains explicitly uncertain.
if r'\unsure{relation|rel.}' not in t:
 t=t.replace(r'\text{ (relation réflexive sym)}',r'\text{ (\unsure{relation|rel.} réflexive sym)}')
cs=d['changes']
for c in cs:
 c['crop']=c['crop'].removeprefix('out/')
 if c['id'] in ['006-11','006-17','006-23','006-37','006-47','006-49','006-50','006-56','006-61']:c['against_C']=False
 c['consequential']=c['id'] in ['006-11','006-13','006-17','006-20','006-23','006-24','006-28','006-30','006-40','006-43','006-46','006-49','006-50','006-56','006-57','006-61','006-62','006-63','006-67','006-68','006-69']
 if c['id']=='006-01':c['final']=r'\mathscr F; first-occurrence script/calligraphic doubt retained on004';c['scan_shows']+=' The repeated font doubt is consolidated at the defining occurrence on004.'
 if c['id']=='006-02':c['final']='M; first-occurrence M/mathcal M doubt retained on003';c['scan_shows']+=' The repeated font doubt is consolidated at the first occurrence on003.'
 if c['id']=='006-70':
  c.update(final=r'\uline{At} \deleted{\unsure{5}}6',against_C=False,against_H=True,confidence='high',scan_shows='Root reinspection of the same saved crop shows the low underline stopping to the left of the live 6 body. Its extension through the whole numeral is unsupported. Keep At underlined and the digit outside.')
 if c['id']=='006-46':
  c.update(place='Crowded At5 marginal caption, qualifier',final=r'\unsure{extrinsèq.|intrinsèq.}',against_C=True,confidence='low',scan_shows='Root reads an e-like loop followed by a crossing stroke before the tall t, favouring extrinsèq. over the initial reader’s intrinsèq. The ending is abbreviated with a point. Crowding prevents a certain onset; intrinsèq. remains an explicit alternative. H’s autonomes does not match the tall t/r/i/n sequence.')
# Record physical underlines missing from, or extending beyond, H's marked text.
manifest={Path(x['filename']).stem.removeprefix('scan006_'):x for x in json.loads((R/'review/scan006_crop_manifest.json').read_text())}
# Some manifests name the file rather than path.
def add(id,place,C,H,final,evidence,key,kind='other',against_C=False,against_H=True,confidence='high'):
 m=manifest[key]
 cs.append(dict(id=id,place=place,C=C,H=H,final=final,scan_shows=evidence,confidence=confidence,kind=kind,crop='crops/'+Path(m['filename']).name,box=m.get('box',m.get('original_box')),against_C=against_C,against_H=against_H,marked_in_H=False,consequential=False))
if not any(c['id']=='006-70' for c in cs):
 add('006-70','At6 underline extent',r'\uline{At} followed by overwritten digit',r'\emph{At 6}',r'\uline{At} \deleted{\unsure{5}}6','The continuous low stroke starts below A and extends beyond the body of the live 6. Unlike At4/5/7, this label underlines its numeral.','at6_number',against_C=True,against_H=False)
for num,word,key in [('71','compatibilité','compat_margin'),('72','par strates','compat_margin'),('73','raffinement','refinement_margin'),('74','par strates','refinement_margin'),('75','Corollaire','refinement_margin'),('76','raffinement interne','minimum_margin'),('77','Transitivité','transitive_margin')]:
 add('006-'+num,'Marginal underline: '+word,r'\uline{'+word+'}',word,r'\uline{'+word+'}','A separate continuous underline is visible below this phrase; H leaves it unmarked.',key)
add('006-78','Notation heading', 'Notation',r'\emph{Notation}','Notation','No horizontal underline lies below the heading.','definition')
add('006-79','At5 marginal caption underline','underlined caption','unmarked caption','underlined Critère du raffinement ... de figures','The caption has a long low underline and a separate continuation underline beneath figures. These are not cancellation strokes.','at5_note')
for num,n,key in [('80',4,'at4_formula'),('81',5,'at5_number'),('82',7,'at7_number')]:
 add('006-'+num,'At'+str(n)+' underline extent',r'\uline{At} '+str(n),'whole At '+str(n)+' emphasized',r'\uline{At} '+str(n),'The underline stops below At, before the numeral.','at'+str(n)+'_number' if n!=4 else key)
for num,n,key in [('83',0,'atM01'),('84',1,'atM01'),('85',2,'atM2'),('86',3,'atM3')]:
 add('006-'+num,'At_M '+str(n)+' underline',r'\text{\uline{At}}_M '+str(n),'unmarked At_M '+str(n),r'\text{\uline{At}}_M '+str(n),'A short underline lies under At, ending before the small M and numeral.',key)
# A new doubt alone goes only in the doubts file, not in the collation counts.
d['doubts']=[q for q in d['doubts'] if q['place'] not in ['Opening collection alphabet, recurring throughout','Opening M alphabet, recurring throughout','Definition after the arrow','At_M 2, order sign','At 6 underline scope']]
for q in d['doubts']:
 if q['place']=='At 5 marginal caption, intrinsic qualifier':q.update(place='At5 marginal caption, qualifier',reading='extrinsèq.',alternatives=['intrinsèq.'],confidence='low',reason='The e-like loop and crossing at the onset favour extrinsèq.; crowding leaves the first letters uncertain.')
if not any('relation' in q['place'] for q in d['doubts']):
 d['doubts'].append(dict(place='Opening tuple, compressed first relation word',reading='relation',alternatives=['rel.'],confidence='low',reason='After the tall l, the compressed marks do not securely distinguish the full word from abbreviation; both drafts give the full word.'))
for e in d['inventory']:
 if e['element']=='I20':e['first_words_or_objects']='Earlier doubtful 5 overwritten by clear 6; underline ends below At before the live numeral.'
 if e['element']=='I26':e['first_words_or_objects']='équivaut à : inserted Si G,H above cancellation; crowded subfigure phrase; formula; underlined extrinsèq./intrinsèq. caption continues as de figures.'
d['S_decisions']=[dict(id='SA21-K7-01',decision='Confirmed as an observation of the literal triangular hypothesis; the mathematical replacement is kept out of the transcription and qualified in N006-At6 below',evidence='scan006_at6_formula.png, original box [419,1144,1637,1295], shows a closed left-pointing triangle in X triangleleft F and the explicit parenthetical X∈tilde F. It also shows the universal quantifier struck. The final live numeral is6 above uncertain5 (scan006_at6_number.png [266,1139,399,1246]). A nontrivial intended version needs X∈M, F∈the figure set, X≪F; merely replacing the relation while leaving arbitrary X∈the figure set loses the stratum typing.')]
d['root_adjudication']={'reader':'GPT-6 Astra Pro root; effort not exposed','viewed':'whole once, halves once, all33 saved crops','decisions':['Literal X triangleleft F and X est plus petit élément preserved; S literal observation confirmed, mathematical repairs restricted to notes.','Root reconsidered underline extent on the saved crop: it ends before the live6, so retain At only.','At5 marginal qualifier now extrinsèq.|intrinsèq. after independent root letter reading.','Unprimed Phi at both lower occurrences, M above union and phi empty-set glyph confirmed.','Repeated alphabet uncertainty consolidated at first occurrence on003/004.']}
lines=t.splitlines()
def line(prefix):return next(x for x in lines if x.startswith(prefix))
def between(a,b):return t[t.index(a):t.index(b)].strip().replace('\n',' ')
compat=r'\mathrel{\tikz[baseline=-.4ex,x=.65em,y=.65em]{\draw (0,1.1)--(1,.5)--(0,-.1) (1,1.1)--(0,.5)--(1,-.1);}}'
a=line('a) ');a_deleted=a[:a.index('Toute partie')].strip();a_live=a[a.index('Toute partie'):]
at6=line(r'\uline{At} \deleted{\unsure{5}}6')
atM=[x for x in lines if x.startswith(r'\text{\uline{At}}_M') or x.startswith(r'\text{\uline{At}}_{M}')]
reads={1:r'\mspage{5}',2:r'\uline{At 3}',3:r'\uline{At} 4',4:r'\uline{At} \deleted{\unsure{5}}6',5:r'\uline{At} \deleted{\unsure{6}}5',6:r'\uline{At} \deleted{\unsure{6}}7',7:r'\text{\uline{At}}_M 0',8:r'\text{\uline{At}}_M 1',9:r'\text{\uline{At}}_M 2',10:r'\text{\uline{At}}_M 3',11:r'\unsure{1}',12:r'$(\mathscr F,\leq)$',13:'équivaut :',14:line('Donc ')[line('Donc ').index('$(M,'):].removesuffix(' satisfaisant'),15:a_deleted,16:r'\inserted{\unsure{posant}}',17:a_live,18:r'\deleted{\unsure{$\exists$}}',19:line(r'\margin{On aura'),20:line(r'\text{b)}'),21:line(r'\uline{At 3}'),22:r'\deleted{\unsure{x}}',23:line(r'\margin{Critère de \uline{compatibilité}'),24:r'\deleted{\unsure{At}}',25:r'entre $\leq$ et $\ll$. \unsure{1}',26:between(r'\uline{At}~4', 'Ramène'),27:line(r'\margin{Critère de \uline{raffinement}'),28:line('Ramène'),29:line(r'\margin{Axiome de la plus petite'),30:at6[at6.index(r'\quad')+5:].strip(),31:r'\deleted{\forall}',32:r'\deleted{\unsure{\leq}}\ll',33:between('Notation',r'(\text{ou }'),34:between(r'(\text{ou }',r'\end{aligned}'),35:line(r'\margin{\tikz'),36:r'\inserted{Si $G,H$,}',37:r'\deleted{\illegible{2}}',38:r'\uline{de figures})',39:line(r'\uline{At} \deleted{\unsure{6}}5')[line(r'\uline{At} \deleted{\unsure{6}}5').index(r'\quad')+5:].strip(),40:between('ou encore, dans', '% slanted\n'+r'\margin{\uline{Transitivité}'),41:line(r'\margin{\uline{Transitivité}'),42:line(r'\uline{At} \deleted{\unsure{6}}7')[line(r'\uline{At} \deleted{\unsure{6}}7').index(r'\quad')+5:].strip(),43:line('Traduction'),44:' '.join(atM[:2]),45:between(atM[2],atM[3]),46:r'$\Psi\ \deleted{\text{\unsure{pa}}}\text{partie}$',47:between(atM[3],r'\end{aligned}'),48:r'\deleted{\unsure{\{X,Y\}}}',49:r'$\exists\Phi\in\widetilde{\mathscr F},\ X,Y\in\Phi)$',50:r'$(\text{i.e. }\Phi\mathbin{\overset{M}{\cup}}\Psi\in\widetilde{\mathscr F}).$'}
reads[51]=r'\uline{At} \deleted{\unsure{5}}6'
bs=[]
for i,b in enumerate(d['second_boxes'],1):
 b['source_box_id']=b['box'];b['box']=f'B{i:03d}';b['reading']=reads[i]
 if i<=11:b['kind']='central handwritten numerical inscription; include its visible corrections and underline'
 elif i in [19,23,27,29,35,41]:b['kind']='whole marginal note with all corrections, formulae and graphic marks'
 elif i in [16,18,22,24,31,32,36,37,48]:b['kind']='central correction: include cancelled and added ink'
 elif i in [13,38]:b['kind']='central complete word group and punctuation'
 else:b['kind']='complete central text block or formula; include corrections, decorations and punctuation'
 bs.append(b)
d['second_boxes']=bs
d['changes']=cs
(R/'pages/H156-01_156-7_scan006.tex').write_text(t)
(R/'review/scan006_final.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
base=R/'second/H156-01_156-7_scan006'
for suffix,cols in [('_boxes.tsv',['box','kind','x0','y0','x1','y1']),('_first.tsv',['box','reading'])]:
 with Path(str(base)+suffix).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=cols,delimiter='\t',extrasaction='ignore');w.writeheader();w.writerows(bs)
now=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (R/'review/root_visual_log.tsv').open('a') as f:
 for p in sorted((R/'crops').glob('scan006_*.png')):f.write(f'6\tcrops/{p.name}\t{now}\troot direct crop inspection completed before adjudication\n')
 f.write(f'6\twhole + a + b\t{now}\troot layout and continuous reading completed before adjudication\n')
print(len(cs),'records;',len(bs),'blind boxes;',len(d['doubts']),'remaining doubt entries')
