from pathlib import Path
import json,csv,datetime,re
R=Path(__file__).resolve().parents[1]
d=json.loads((R/'review/scan009_review.json').read_text());d['scan']=9;d['status']='root initial adjudication complete; blind reading pending'
t=(R/'review/scan009_proposed.tex').read_text()
def conv(s):
 return s.replace(r'\unsure{M|\mathcal M}','M').replace(r'\unsure{\mathscr F|\mathcal F}',r'\mathscr F').replace(r'\varphi',r'\phi').replace(r'\unsure{Alors}',r'\unsure{Alors|At}').replace(r'X\prime',"X'").replace(r'Y\prime',"Y'").replace(r'F\prime',"F'").replace(r'G\prime',"G'").replace(r'C\prime',"C'")
t=conv(t)
cs=[]
removed={2,25,43}
for c in d['changes']:
 n=int(c['id'].split('-')[-1])
 if n in removed:continue
 c['crop']='crops/'+Path(c['crop']).name;c['final']=conv(c['final'])
 if n==5:c['scan_shows']+=' Root explicitly retains At as an alternative inside the deleted doubt rather than resolving the thick overwritten group.'
 if n in [11,23]:c['scan_shows']+=' Root uses the established phi mapping from006 for the long-stemmed form; the first local phi/slashed-oval ambiguity remains marked.'
 if n==54:c['confidence']='high';c['scan_shows']+=' Root distinguishes this as underlining: it follows the lower edge of sous-figures; the adjacent lower baseline is crowded but does not make the underlined title a cancelled replacement.'
 if n==56:c['scan_shows']+=' Root checked both filled points against the source diagonal and oval; the final vector paths pass through their centers.'
 if n==59:c['scan_shows']+=' The abbreviated spelling is not expanded into the expected complete word.'
 c['consequential']=n in {3,9,11,14,15,18,19,20,23,26,27,28,29,30,32,33,34,37,39,42,50,51,55,56,57,61,64,65,66,68,69,70,72,73,75,76,77,79}
 cs.append(c)
d['changes']=cs
for row in d['difference_review']:
 if 'change_ids' in row:row['change_ids']=[x for x in row['change_ids'] if int(x.split('-')[-1]) not in removed]
removed_doubts={'At DC 1 ambient family','Cor 1 family alphabet','Cor 1 authorial inconsistency','Cor 2 inconsistent letters','Lower live corollary authorial inconsistency','Criterion source state'}
d['doubts']=[q for q in d['doubts'] if q['place'] not in removed_doubts]
for q in d['doubts']:
 q['reading']=conv(q['reading']);q['alternatives']=[conv(x) for x in q.get('alternatives',[])]
d['root_adjudication']={'reader':'GPT-6 Astra Pro root; effort not exposed','viewed':'whole once, both halves once, all25 saved crops','decisions':['Literal C/C-prime operands and unprimed F retained; clear local returned G forms are not converted by a global substitution.','All nested corrections remain inside cancelled upper blocks; reference line remains live above the struck Montrons row.','Shared M/scriptF alphabet uncertainties consolidated at first defining occurrence; phi mapping follows006 with first local shape doubt retained.','Small mid-stroke arrowhead, source-shaped lower rule, separate axiom border and full drawing preserved.','First readings rebuilt from actual LaTeX spans, correcting oversized candidate spans and removing non-source comments.']}
for q in d['notes']:
 if q['id']=='009-N5':q['claim']='The initial reader performed visual checks only; root subsequently checked two limited conditional mathematical statements, recorded in notes and CHECK_EVENTS.'
# Inventory every nested cancellation separately, not only its enclosing block.
for element,pos,words in [
 ('Earlier AtDC1 relation','inside first cancelled formula','parallel sign below compatibility'),
 ('Earlier AtDC1 opening word','before inserted Soient','Alors / At'),
 ('Earlier AtDC1 implication','inside cancelled continuation','Y′≪Y ⇒ X′∥Y′'),
 ('NB earlier chevrons','first Z lower-bound premise','old ≪ below ≤'),
 ('NB cancelled impossibility word','penultimate marginal rows','impossible'),
 ('NB cancelled contradiction word','before final car','absurde'),
 ('AtDC2 earlier opening','after parenthetic title','Soit / Soient'),
 ('AtDC2 overwritten first symbol','under K in intersection definition','L'),
 ('Reference earlier page abbreviation','between cf and GF','p.'),
 ('Lower note cancelled abbreviation','before second At11','ex'),
 ('Lower axiom cancelled copula','between l’inverse and tjrs','est')]:
 d['inventory'].append(dict(element=element,kind='deletion',position=pos,first_words_or_objects=words))
lines=t.splitlines()
def line(p):return next(x for x in lines if x.startswith(p))
def block(a,b):return t[t.index(a):t.index(b)].strip()
cor1=line(r'\deleted{\uline{Cor} 1')
cor2=line(r'\deleted{\uline{Cor. 2}')
criterion=line(r'\margin{\uline{Critère}')
lastnote=line(r'\margin{Mais on aura')
oldformula=r'\deleted{$\unsure{L=\underset{Z\in\widetilde F\cap\widetilde G}{\mathrm{Sup}}\,Z}$}'
bs=d['second_boxes']
for i,b in enumerate(bs,1):
 b['source_box_id']=b['box'];b['box']=f'B{i:03d}';b['reading']=conv(b['reading'])
 if i==5:b['reading']=r'\deleted{\inserted{Soient}}'
 if i==6:b['reading']=r'\deleted{'+b['reading']+'}'
 if i==8:b['reading']=cor1
 if i==9:b['reading']=cor2
 if i==10:b['reading']=r'\deleted{'+oldformula+'}'
 if i==11:b['reading']=r'\deleted{'+b['reading']+'}'
 if i==14:b['reading']=r'\deleted{$'+b['reading']+r'$. Supposons que}'
 if i==15:b['reading']=r'\deleted{$'+b['reading']+'$}'
 if i==22:b['reading']=criterion
 if i==24:b['reading']=lastnote
 if i==28:b['reading']=r'\margin{'+b['reading']+'}'
 b['reading']=' '.join(re.sub(r'(?<!\\)%.*','',x) for x in b['reading'].splitlines()).strip()
 if i==1:b['kind']='central handwritten page numeral'
 elif i in [7,22,24]:b['kind']='whole slanted marginal note, including all formulas, corrections and punctuation; rotate upright'
 elif i==8:b['kind']='first complete two-line statement beginning near top of crop; exclude the separate smaller statement below'
 elif i==9:b['kind']='second complete two-line statement beginning in middle of crop; exclude preceding formula remnants'
 elif i in [16,23,28]:b['kind']='complete central graphic; reproduce all its strokes, points and any inscriptions'
 elif i in [5,6,10,11,26]:b['kind']='central correction group, including added or cancelled ink and its source state'
 elif i==19:b['kind']='upper complete reference line; exclude separate lower crossed text'
 elif i==20:b['kind']='lower complete crossed text row; exclude reference line above'
 elif i==21:b['kind']='two complete text lines in center; exclude crossed row above'
 elif i==25:b['kind']='lower complete main text line with its interlinear addition; exclude preceding paragraph above'
 else:b['kind']='complete central text or formula group, with all corrections, decorations and punctuation'
d['second_boxes']=bs
(R/'pages/H156-01_156-7_scan009.tex').write_text(t)
(R/'review/scan009_final.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
base=R/'second/H156-01_156-7_scan009'
for suffix,cols in [('_boxes.tsv',['box','kind','x0','y0','x1','y1']),('_first.tsv',['box','reading'])]:
 with Path(str(base)+suffix).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=cols,delimiter='\t',extrasaction='ignore');w.writeheader();w.writerows(bs)
now=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (R/'review/root_visual_log.tsv').open('a') as f:
 for p in sorted((R/'crops').glob('scan009_*.png')):f.write(f'9\tcrops/{p.name}\t{now}\troot direct crop inspection completed before adjudication\n')
 f.write(f'9\twhole + a + b\t{now}\troot continuous layout and line reading completed\n')
print(len(cs),'records;',len(bs),'blind boxes;',len(d['doubts']),'remaining doubts')
