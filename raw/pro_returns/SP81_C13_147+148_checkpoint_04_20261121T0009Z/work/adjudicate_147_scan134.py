from pathlib import Path
import json
from datetime import datetime,timezone
root=Path(__file__).resolve().parents[1]; page='147_scan134'
p=root/'pages'/f'{page}.tex'; t=p.read_text()
t=t.replace(r'\unsure{se} décompose',r'\unsure{se|a|à} décompose')
t=t.replace('est déduite de',r'est \unsure{déduite|déduit} de')
assert 'décroissants, et celle' in t
t=t.replace('décroissants, et celle','décroiss. et celle')
p.write_text(t)
f=root/'work'/f'{page}_final.json'; r=json.loads(f.read_text())
for c in r['changes']:
 if c['id'].endswith('-12'):
  c['final']=c['final'].replace(r'\unsure{se}',r'\unsure{se|a|à}')
  c['evidence']+=' Blind audit retains se first and admits a/à: the compact loop and rising return do not securely separate these forms.'
 if c['id'].endswith('-15'):
  c['final']=c['final'].replace('est déduite de',r'est \unsure{déduite|déduit} de')
  c['evidence']+=' The final small return after t may represent e or merely its exit stroke; preferred déduite is retained with a local ending doubt.'
  c['confidence']='medium'
 if c['id'].endswith('-19'):
  c['final']=c['final'].replace('décroissants, et celle','décroiss. et celle')
  c['differs_C']=True
  c['evidence']+=' Blind audit restores the short form décroiss.: the word ends with two short s-curves and a separate dark point before et, without a following -ants group. Considération has a tall internal t; poudre has a descending p, and yeux a descending y. The original local doubts elsewhere in the note remain.'
  c['crop']=page+'_second_B18.png';c['box']=[22,1634,544,2338];c['confidence']='medium'
for d in r['doubts']:
 if d['reading']==r'\unsure{se}':
  d['reading']=r'\unsure{se|a|à}';d['alternatives']='se; a; à';d['reason']='A low loop and short rising return remain ambiguous on the independent crop; no accent can be isolated securely.'
r['doubts'].append(dict(place='main line 18, est déduite de',reading=r'\unsure{déduite|déduit}',alternatives='déduite; déduit',confidence='medium',reason='The tiny return following the terminal upright may be e or the exit stroke of t. Agreement does not decide the ending.'))
for d in r['decisions']:
 if d['id']=='M0013':
  d['reading']=r'\unsure{se|a|à}';d['evidence']+=' The blind audit supplied a/à as explicit alternatives admitted by the same loop and return.'
r['abbreviations'].append(dict(form='décroiss.',expansion='décroissants',place='diagonal marginal note'))
r['notes']+=' The blind audit restores the marginal abbreviation décroiss. from its terminal point and short outline. It retains the formula alpha(0)=0 above the cancelled homomorphisme and the literal separators in (220), and adds local alternatives for se/a/à and déduite/déduit. These are ink decisions; no mathematical statement was checked.'
f.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
comp=json.loads((root/'second'/f'{page}_comparison.json').read_text());ds={x['box']:x for x in comp['differences']}
ev={
'B01':('Both numerals have descending curved upper stems leading into lower loops; the first has an inward retrace, without a separate flat 5 cap. The reading 66 remains.', 'high'),
'B02':('The cancellation covers both small groups. Initial d-loop and low connected strokes survive, with a terminal descender whose attachment is uncertain. The original des cas remains expressly doubtful; neither donc/dans nor the second word is settled.', 'low'),
'B03':('The shaft ends in a blunt thickening with no two separate head arms. Alpha sits above it, and the final comma is present. Retain the drawn headless connector.', 'high'),
'B04':('A single underline extends below morphisme correspondant. The latter word has a joined corr- opening, descending p and tall d/t portions; no separate non is present.', 'high'),
'B05':('Two Pi objects, only the left with tilde, a rightward headed shaft labelled tilde-alpha-star, and the surrounding four frame strokes are visible. Both encodings give these objects and decorations.', 'high'),
'B06':('The looped descending g, compact accented middle and -risation continuation support générisation. Underlining begins below hom and continues through the phrase.', 'high'),
'B08':('The initial c, low joined anoni run, descending q and long terminal return are visible in canoniquement. The following en un hom surjectif agrees.', 'high'),
'B11':('Above the crossed l’homomorphisme the insertion shows on a, alpha, parenthesized zero, two equality strokes and terminal zero. These strokes support the formula alpha(0)=0 rather than the word alors.', 'high'),
'B12':('Donc is a separate initial d and low run. The cancelled correspondent-shaped word stays doubtful under its strike. The lower insertion has d-apostrophe, tall paired l forms and a low terminal run, supporting d’ailleurs.', 'medium'),
'B13':('The small loop and rising return after the full D-star arrow admit se/a/à, now displayed explicitly. The next baseline has décompose followed by separate en and des; the terminal punctuation retains its colon/semicolon doubt.', 'low'),
'B14':('The endpoint separators are literal short dashes, with a doubtful first small round component at the source. Dense raised crossing marks over the target d letters remain ambiguous between cancelled primes and stars. The whole formula, including source r-prime, was checked.', 'low'),
'B15':('The terminal d has its own prime, with clear paper after r before the closing parenthesis. The exit stroke of the t in déduite/déduit is too compressed to exclude the shorter ending; retain déduite first with doubt. Literal tuple separators remain.', 'medium'),
'B16':('The first word has several small accented/open strokes and a -crivant-like low run, without the long p descender plainly visible in répétant later on the same baseline. Réécrivant remains preferred and doubtful.', 'medium'),
'B17':('The same words, single cancelled les, long separator strokes, and underline from si alpha est un hom are represented in both readings. Only dash serialization differs.', 'high'),
'B18':('Considération has a tall internal t and a longer ending than coïncidence. The first monotonicity word ends in two s-curves and a dark separate point: décroiss. is restored without adding -ants. The lower lines show non (still doubtful), stricts croissants, est de, then la poudre aux yeux and simplement ! with distinct p/y descenders. Crossed upright body text is excluded from this diagonal note.', 'medium'),
'B20':('Two close, slightly curved vertical emphasis strokes are visible, with no arrowhead arms and no labels. Both TikZ encodings preserve these two strokes.', 'high')}
choices=[]
for b,d in ds.items():
 final=d['first']
 if b=='B13':final=final.replace(r'\unsure{se}',r'\unsure{se|a|à}')
 if b=='B15':final=final.replace('est déduite de',r'est \unsure{déduite|déduit} de')
 if b=='B18':final=final.replace('décroissants, et celle','décroiss. et celle')
 it=dict(box=b,choice='literal' if final!=d['first'] else 'first',changed=final!=d['first'],evidence=ev[b][0],confidence=ev[b][1])
 if it['choice']=='literal':it['final']=final
 choices.append(it)
(root/'work'/f'{page}_audit_choices.json').write_text(json.dumps(dict(reader='audit_c',choices=choices),ensure_ascii=False,indent=2)+'\n')
with (root/'work/root_views.tsv').open('a') as f:
 for b in ds:f.write(f'{datetime.now(timezone.utc).isoformat()}\t{page}_second_{b}.png\troot blind-audit adjudication\n')
