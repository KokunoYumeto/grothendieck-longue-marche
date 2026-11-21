from pathlib import Path
from datetime import datetime, timezone
import json
root=Path(__file__).resolve().parents[1]; page='148_scan004'
f=root/'work'/f'{page}_final.json';r=json.loads(f.read_text());p=root/'pages'/f'{page}.tex';t=p.read_text()
subs=[(r'\unsure{$\mathbb Z_{n_i}$|$\mathbb Z/n_i$}',r'\unsure{$\mathbb Z_{n_i}$|$\mathbb Z/n_i$|$\mathbb Z n_i$}'),(r'\unsure{les groupes|de groupe}',r'\unsure{le groupe|les groupes|de groupe}'),(r'S_{\unsure{*|1}}T(\unsure{X}',r'S_{\unsure{*|1|g}}T(\unsure{X|\uline{X}}')]
for a,b in subs:
 assert a in t,a
 t=t.replace(a,b)
p.write_text(t)
for section in ('changes','doubts','decisions'):
 for row in r[section]:
  for key in ('final','reading'):
   if key in row:
    for a,b in subs:row[key]=row[key].replace(a,b)
for c in r['changes']:
 if c['id'].endswith('-01'):c['evidence']+=' The independent reading also places n_i beside Z; its height permits a baseline juxtaposition as well as the lowered reading, now retained as a third alternative.'
 if c['id'].endswith('-02'):
  c['differs_C']=True;c['evidence']='The tall initial loop joins one short low return; the terminal e-like hook of groupe has no separately exposed s. Le groupe is now preferred to les groupes and de groupe. The cancellation covers both words at mid-height, so the other readings remain in the doubt. The independent B05 crop shows two components in the adjacent i.e with an internal point and no terminal point; no third abbreviation component is securely visible.'
  c['crop']=page+'_second_B05.png';c['box']=[1025,445,1495,555]
for d in r['decisions']:
 if d['id']=='M0062':d['evidence']+=' Baseline juxtaposition Z n_i is now an additional candidate; the first lowered candidate remains preferred.'
 if d['id']=='M0064':d['reading']=r'\unsure{*|1|g}';d['evidence']+=' The blind reading sees g in the low loop and descending return; it is added without resolving the overlapping strokes.'
 if d['id']=='M0065':d['reading']=r'\unsure{X|\uline{X}}';d['evidence']+=' The separate low horizontal mark permits an underline, now retained as an alternative to the overworked plain X.'
for d in r['doubts']:
 if d['place']=='raised qualifier above principal line 4':d['alternatives']='lowered n_i; slash n_i; juxtaposed n_i'
 if d['place']=='cancelled phrase after the first inclusion':d['alternatives']='le groupe; les groupes; de groupe';d['reason']='The first tall loop and single low return, followed by the final hook without a separate s, favor le groupe. The cancellation still covers the word centres and possible endings.'
 if d['place']=='subscript in the first group name':d['reading']=r'S_{\unsure{*|1|g}}T';d['alternatives']='*; 1; g';d['reason']+=' The loop and descending return also permit the second reader’s g.'
 if d['place']=='first argument in the first group name':d['reading']=r'\unsure{X|\uline{X}}';d['alternatives']='overworked X; underlined X';d['reason']+=' The low horizontal mark is retained as a possible underline.'
r['notes']+=' The blind audit favors le groupe in the crossed phrase, while its covered endings retain alternatives. It leaves the raised Z/n_i grouping, first group subscript and low strokes beneath X unresolved. In the lower inclusion line, the short word after et begins with a nearly closed oval and is retained as on. The lower product’s separating point lies at the baseline. No mathematical claim was checked in this audit.'
f.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
ev={
'B01':('The word has the tall l and t, dotted i, descending q and final low age sequence. Multimarquage remains readable without adding a new doubt.','high'),
'B02':('The full baseline shows i in I, n with lower i, membership in double-struck N and a raised star; the surrounding chaque, un, et un agree. Only TeX grouping differs.','high'),
'B03':('The inserted Z has doubled oblique ink and lower return. The n_i sits lower to its right but close enough to allow juxtaposition, now added beside the existing lowered and slash alternatives. The curved leader attaches in the gap after sous-.','medium'),
'B05':('The exposed tall loop and one low return favor le; the final hook of groupe has no separate s. Le groupe is now preferred, with the crossed alternatives retained. The following abbreviation has two visible components, an internal point and no terminal point; i.e stays.','low'),
'B07':('The underlined s and separate right-hand curved relation are crossed. The relation’s upper part is covered, so the complete cancelled fragment keeps its existing doubt. Underline and math-wrapper syntax do not change the reading.','medium'),
'B08':('The full formula has underlined s, membership, product indexed i in I, T with lower i and raised wedge n_i, followed by a comma. Both readings give these same signs.','high'),
'B10':('A low angular loop with a descending return lies between S and T; g is added beside star/1 without choosing. The X has a separate low horizontal stroke and overlapping loop, allowing an underline alternative. The underlined s and closing punctuation agree.','low'),
'B11':('A closed small oval is raised above s, with i below it. Dans chaque and T_i(n_i), including the closing comma, agree. Extra braces do not change the reading.','high'),
'B12':('The lower line has two underlined s forms with raised zeros and ST without a separate lowered star. After the SRT(X) comma, et is followed by a nearly closed low oval and a connected n-like run; on is retained.','medium'),
'B13':('Both ST names have no lower subscript. The separator after the second parenthesis is a dark baseline point. The indexed product and fraction 1 over n_i precede Z_i; a nearby extra point stays unresolved as already recorded.','high'),
'B14':('The final baseline reads où Z_i est le ième facteur de and rises into the single Z^I inclusion SRT(X), ending with a point. There is no ordinal hyphen. Both readings preserve the same words and signs.','high')}
comp=json.loads((root/'second'/f'{page}_comparison.json').read_text());choices=[]
for d in comp['differences']:
 final=d['first']
 for a,b in subs:final=final.replace(a,b)
 choice=dict(box=d['box'],choice='literal' if final!=d['first'] else 'first',changed=final!=d['first'],evidence=ev[d['box']][0],confidence=ev[d['box']][1])
 if choice['choice']=='literal':choice['final']=final
 choices.append(choice)
(root/'work'/f'{page}_audit_choices.json').write_text(json.dumps(dict(reader='audit_c',choices=choices),ensure_ascii=False,indent=2)+'\n')
with (root/'work/root_views.tsv').open('a') as f:
 for d in comp['differences']:f.write(datetime.now(timezone.utc).isoformat()+'\t'+page+'_second_'+d['box']+'.png\tRoot personally inspected the enlarged crop successfully; decision recorded in audit choices.\n')
