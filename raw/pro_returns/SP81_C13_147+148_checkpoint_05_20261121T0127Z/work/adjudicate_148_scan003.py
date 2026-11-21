from pathlib import Path
import json
root=Path(__file__).resolve().parents[1];page='148_scan003'
f=root/'work'/f'{page}_final.json';r=json.loads(f.read_text());p=root/'pages'/f'{page}.tex';t=p.read_text()
comp=json.loads((root/'second'/f'{page}_comparison.json').read_text());diff={d['box']:d for d in comp['differences']}
subs=[(r'et que \unsure{vu pour}',r'\unsure{et que vu pour|et en tant que}'),(r"l'image inverse de",r"l'image \unsure{inverse|\deleted{d'}inverse} de"),(r'relève $u$) on trouve',r'relève $u$\unsure{,|)} on trouve'),(r'\unsure{\mathbb U^I}',r'\unsure{\mathbb U^I|\mathbb M^I}'),(r'\unsure{une classe}',r'\unsure{une classe|un des}'),(r'suppl.$\bigr\}$',r'suppl.$\unsure{\bigr\}|\bigr]}$'),(r'\unsure{coïncid.|coïncidant}',r'\unsure{coïncid.|coïncidant|coincident}')]
for a,b in subs:
 assert a in t,a
 t=t.replace(a,b)
start=t.index('\\begin{tikzcd}');end=t.index('\\end{tikzcd}',start)+len('\\end{tikzcd}')
old_diagram=t[start:end]
new_diagram=diff['B12']['second'].removeprefix('\\diagram{')[:-1].replace(r'S\unsure{K|R}T(X)',r'S\unsure{R|K}T(X)')
t=t[:start]+new_diagram+t[end:];p.write_text(t)
for section in ('changes','decisions','doubts'):
 for row in r[section]:
  for key in ('final','reading'):
   if key in row:
    for a,b in subs:row[key]=row[key].replace(a,b)
for c in r['changes']:
 if c['id'].endswith('-01'):
  c['confidence']='low';c['evidence']+=' Blind comparison leaves the whole compressed connective after ci-dessus open between et que vu pour and et en tant que. The initial strokes of inverse are also overworked; a possible canceled d-prime is recorded without asserting its deletion state.'
 if c['id'].endswith('-05'):
  c['differs_C']=True;c['final']=r'relève $u$\unsure{,|)} on trouve';c['confidence']='medium';c['crop']=page+'_second_B06.png';c['box']=[210,1190,1266,1395]
  c['evidence']='The only mark after u is a short curved descent starting around the letter baseline, much lower than the opening parenthesis. Comma is now preferred, with a short closing parenthesis retained as an alternative. The scan does not show two separate marks there. The possibly unclosed opening parenthesis is preserved.'
 if c['id'].endswith('-15'):c['evidence']+=' The second independent reading un des is added; the final groups remain too compressed to choose.'
 if c['id'].endswith('-19'):c['evidence']+=' The closing delimiter has a thin upper return and lower bend; a bracket alternative is now retained beside the first curly brace.'
 if c['id'].endswith('-20'):
  c['final']=new_diagram;c['confidence']='medium';c['crop']=page+'_second_B12.png';c['box']=[1172,2114,1595,2340]
  c['evidence']+=' Three objects and two connector shafts were recounted. The upper arrow’s terminal region has an additional curved pass and a dark retraced kink, reproduced directly. The target’s middle letter has an open upper return, permitting K beside the preferred R. This local letter doubt does not change the other page occurrences.'
 if c['id'].endswith('-21'):c['evidence']+=' Coincident is retained as a third candidate from the blind reading; the isolated end strokes and single secure upper dot still leave both ending and diaeresis unsettled.'
for d in r['decisions']:
 if d['id']=='M0050':d['reading']=r'\unsure{et que vu pour|et en tant que}';d['evidence']+=' The blind reader supplies a different segmentation of the whole connective; neither is secure enough to resolve the mark.'
 if d['id']=='M0055':d['evidence']+=' The exposed internal diagonal also permits an M-like form, added as a local candidate.'
 if d['id']=='M0056':d['evidence']+=' Un des is added from the independent reading without settling the word centres.'
 if d['id']=='M0061':d['evidence']+=' The longer coincident candidate and its single dotted i are also retained in the unresolved reading.'
for d in r['doubts']:
 if d['place']=='line 3, M0050':d['reading']=r'\unsure{et que vu pour|et en tant que}';d['alternatives']='et que vu pour; et en tant que';d['reason']='Two independent segmentations of the compressed low groups and tall crossing remain unresolved; no connective is supplied from mathematical syntax.'
 if d['place']=='line 18, M0055':d['alternatives']='overworked double-struck U; overworked double-struck M'
 if d['place']=='line 18, M0056':d['alternatives']='une classe; un des'
 if d['place']=='line 22, M0061':d['alternatives']='coïncid.; coïncidant; coincident; ending and diaeresis unresolved'
r['doubts'] += [dict(place='line 5, overwritten start of inverse',reading=r"\unsure{inverse|\deleted{d'}inverse}",alternatives='overworked live inverse; possible canceled d-prime before inverse',confidence='low',reason='A loop, high detached stroke and horizontal overlap occupy the word’s beginning; their separate textual states are not secure.'),dict(place='line 11, after relève u',reading=r'\unsure{,|)}',alternatives='comma; short closing parenthesis',confidence='medium',reason='One curved descent starts low beside u; there is no separate pair of marks.'),dict(place='line 21, after suppl.',reading=r'\unsure{\bigr\}|\bigr]}',alternatives='closing curly brace; closing square bracket',confidence='medium',reason='The thin upright delimiter has short upper and lower returns whose curvature is compressed.'),dict(place='lower diagram, target middle letter',reading=r'S\unsure{R|K}T(X)',alternatives='R; K',confidence='medium',reason='The upper return is open, while the stem and lower oblique are clear; the first R reading is retained locally.')]
r['notes']+=' Blind audit preserves the compressed opening connective as two whole-span alternatives and marks the possible canceled d-prime at inverse. The single short punctuation stroke after relève u is now read first as a comma, leaving the opening parenthesis possibly unclosed. The target in the lower diagram has a local R/K doubt, and the extra terminal pass at the upper arrowhead is drawn explicitly. There are three diagram objects and two connecting shafts. Other SRT occurrences keep their own visible R. The source’s dépend un choix and literal SUR(X) remain. No mathematical statement was checked in this audit.'
f.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
ev={
'B01':('The two upper baselines and raised phi with underlined-s subscript agree. Its interlinear attachment follows scindage; math wrapper syntax differs only.','high'),
'B02':('The enclosed extension mark has a central crossing, retained as star. The short groups after ci-dessus have compressed low runs and a tall crossing; the two independent connective segmentations remain whole-span alternatives.','low'),
'B03':('The group subscripts remain single uprights, and the formula/prose order agrees. At the start of inverse a loop, detached upper stroke and horizontal overwork permit an earlier d-prime; its deletion state is now explicitly doubtful.','low'),
'B04':('The source label is SUR(X), with U followed by a loop and oblique R. The short connector ends in a tiny thickening without two secure head arms, so the existing plain-shaft/arrow alternatives remain.','medium'),
'B05':('Le chgt has the compact written contraction, and both underlined s forms, the prime, baseline dot and phi subscript agree. Differences are math and underline serialization.','high'),
'B06':('After relève u there is one short low curved descent, now read first as comma, with closing parenthesis an alternative. The complete equality has two upright 1 subscripts, the prime and tilde. Its final dark point has a short tail and keeps the period/comma doubt.','medium'),
'B07':('The X overstroke is horizontal with a short terminal bend; the bar/vector doubt remains. After dépend the short word has low u-n strokes without a separate initial tall d. Un choix and underlined non-anodin are retained. The s inside the S_1T argument is underlined.','high'),
'B08':('The full lower passage reads S_1RT(X), a single upright 1, followed by ne dépend que d’un choix anodin, celui de la famille des. Whitespace and math delimiters account for the difference.','high'),
'B09':('The t_i family, product and parenthetical insertion agree. The overwritten U-shaped letter also has an internal diagonal permitting M; both are retained. The two compressed final groups remain une classe/un des alternatives.','low'),
'B10':('The baseline begins de with a low ending; ext. has a separate dark point. Autom. and int. retain their own points. Déduits ends in a tall t and short descending return; avec les structures retains the tall l visible before es.','medium'),
'B11':('Suppl. has its terminal point. The thin following closing delimiter permits a curly brace or square bracket. Savoir and les inclusions agree; the existing faint parenthesis/comma after savoir remains unresolved.','medium'),
'B12':('There are three labeled objects and two shafts, each directed to the right-hand target. The upper shaft curves and has an extra terminal pass and heavy kink, now drawn. The target’s open middle-letter return permits R/K, with R retained first. The lower ! has a distinct stroke and dot.','medium'),
'B13':('Coïncid. remains first, but the low separated ending strokes also permit the longer candidates. A second diaeresis dot is not independently secure. Coincident is added as an alternative, without choosing the expected verbal form. The Z^I and final point are clear.','low')}
choices=[]
for d in comp['differences']:
 final=d['first']
 for a,b in subs:final=final.replace(a,b)
 if d['box']=='B12':final=new_diagram
 it=dict(box=d['box'],choice='literal' if final!=d['first'] else 'first',changed=final!=d['first'],evidence=ev[d['box']][0],confidence=ev[d['box']][1])
 if it['choice']=='literal':it['final']=final
 choices.append(it)
(root/'work'/f'{page}_audit_choices.json').write_text(json.dumps(dict(reader='audit_a',choices=choices),ensure_ascii=False,indent=2)+'\n')
