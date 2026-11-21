from pathlib import Path
import csv,json
from datetime import datetime,timezone
R=Path(__file__).resolve().parents[1];p='148_scan057'
C={x['box']:x for x in json.loads((R/'second'/f'{p}_comparison.json').read_text())}
boxes={x['box']:[int(x[k]) for k in ('x0','y0','x1','y1')] for x in csv.DictReader((R/'second'/f'{p}_boxes.tsv').open(),delimiter='\t')}
E={
'B02':'The preposition after ou ends at de; surmarquage ends at e before the comma, with no separate s. The lower word has two c openings and the longer erné sequence with accent and final s: concernés, not connus. The insertion chacun attaches between sur and des. The first wording is retained.',
'B03':'The live quotient has the same short shoulder r as the clearer later r(a) occurrences, not a newly introduced nu. Under the cancellation a Z-like group and a long division-like stroke favour the old quotient Z/r(a), but the following rounded group also admits the independent Z(omega(a)) reading. Both old candidates remain doubtful. The parenthetical definition begins above the cancelled group and is a raised replacement; its insertion state is now recorded. Its doubled Z diagonals, wedge, omega(a) and brace-enclosed plus/minus 1 are visible.',
'B04':'The initial word is de; contraction ends with n and its terminal return, without an added s. After it des and groupes have separate terminal s hooks. The plural belongs to the groups, not to contraction, so the first reading is retained.',
'B05':'The quotient labels and single prime agree. The separator between the source and target consists of a small upper mark and a reduced lower oval, leaving à versus colon explicit. Gommage and partiel each have their own separate underline stroke; the TeX is adjusted to preserve the gap without counting a new lexical witness error. The raised underlined uniforme and its curved insertion leader agree.',
'B06':'The phrase has des groupes, with a final s after the low e of groupe. The two target primes are separate strokes. As in the contraction line the compact source/target separator admits à/colon. In the raised multiplier identity the a lies below d and a nearby curved mark may be an opening parenthesis: d_a/d(a) stays unresolved. Est is present, though the upper contextual ascenders are trimmed.',
'B07':'The old closing parenthesis is crossed at its upper curve. The word at the right continues as teur at the start of the next row; it is multiplicateur, not an abbreviated multiplic. plus a new word. The raised ici has a short dotted i, open c and another dotted i, with an angular insertion leader into the gap before que. Its letters are retained without new doubt.',
'B08':'Two separate strokes underline partiel. After structure, the word begins with the long p descender and ends with a downward s turn; there is no r shoulder. Pas is retained, not par.',
'B09':'Le ends after its low e. Surmarquage and uniforme end before the dash without extra s hooks. The later short verb has s/e/r/a strokes before the separate défini, whose final i has no added s. The singular future wording sera défini is retained, not se définit or définissent.',
'B11':'The pale annotation shows a 5 with upper bar and lower bowl, followed by a tall curved 6 with a closed lower loop. The mspage wrapper records the same 56.'}
D={b:dict(choice='keep_first',viewed=True,evidence=e) for b,e in E.items()}
definition=r'$(\mathbb Z_a=\mathbb Z\mathbin{\wedge}_{\{\pm1\}}\omega(a))$'
repls={
'B03':[(r'\unsure{\mathbb Z/r(a)}',r'\unsure{\mathbb Z/r(a)|\mathbb Z(\omega(a))}'),(definition,r'\inserted{'+definition+'}')],
'B05':[(r'$ à $',r'$ \unsure{à|:} $'),(r'\uline{gommage partiel}',r'\uline{gommage} \uline{partiel}')],
'B06':[(r'$ à $',r'$ \unsure{à|:} $')]}
pp=R/'pages'/f'{p}.tex';s=pp.read_text()
for b,rs in repls.items():
 v=C[b]['first']
 for a,z in rs:
  assert a in v,(b,a);v=v.replace(a,z)
  if a in s:s=s.replace(a,z)
  else:assert z in s,(b,a)
 D[b].update(choice='reading',reading=v)
pp.write_text(s)
(R/'second'/f'{p}_main_decisions.json').write_text(json.dumps(D,ensure_ascii=False,indent=2)+'\n')
rp=R/'records'/f'{p}.json';r=json.loads(rp.read_text())
for x in r['changes']:
 if x['id']==p+'-07':x.update(final=r'\deleted{\unsure{\mathbb Z/r(a)|\mathbb Z(\omega(a))}}',evidence=E['B03'],crop=f'crops/{p}_second_B03.png',box=boxes['B03'])
 if x['id'] in (p+'-09',p+'-14'):x['final']=x['final'].replace('$ à $',r'$ \unsure{à|:} $')
 if x['id']==p+'-11':x['final']=x['final'].replace(r'\uline{gommage partiel}',r'\uline{gommage} \uline{partiel}')
r['changes'].append(dict(id=p+'-28',place='Raised parenthetical definition of Z_a',c=definition,h=r'\bigl(\mathbf{Z}_a=\mathbf{Z}\wedge_{\lbrace\pm1\rbrace}\omega(a)\bigr)',final=r'\inserted{'+definition+'}',diff_c=True,diff_h=True,kind='insertion or placement',error_kind='Insertions put in the wrong place',evidence=E['B03'],crop=f'crops/{p}_second_B03.png',box=boxes['B03'],confidence='medium',marked_in_h=False,consequential=False))
for x in r['doubts']:
 if x['place']=='Cancelled quotient after the first live group':x.update(reading=r'\deleted{\unsure{\mathbb Z/r(a)|\mathbb Z(\omega(a))}}',alternatives='Z/r(a); Z(omega(a)); cancelled alphabet and internal signs unresolved',reason=E['B03'])
r['doubts'].append(dict(place='Source/target separator in contraction and extension lines',reading=r'\unsure{à|:}',alternatives='à; colon',confidence='medium',reason='Both compact marks have a separate upper point/stroke and small lower body, leaving the letter versus punctuation distinction unresolved.'))
for x in r['inventory']:
 if x['element']=='E04':x['first_words_or_objects']=r'$\mathbb Z_a/r(a)$'
 if x['element']=='E05':x['first_words_or_objects']=r'\unsure{\mathbb Z/r(a)|\mathbb Z(\omega(a))}'
r['inventory'].insert(5,dict(element='E15',sheet_kind='text',hand='his hand',kind='insertion',position='Raised over cancelled old quotient and continuing right',first_words_or_objects=definition,transcribed='yes'))
r['notes'].append(dict(id=p+'-N-audit',text='The independent comparison retains the singular surmarquage phrases, plural operator groups, negative pas, future sera défini, and the raised ici. It records the parenthetical Z_a definition as a raised insertion over the old crossed formula, whose quotient and omega-parenthesis readings both remain possible. The two reduced source/target à/colon marks stay explicit, and the visibly separate gommage and partiel underline strokes are represented separately without a new lexical error count. The lowered multiplier a is not regularized from the later clear d(a).'))
r['second_main_review']={'viewed_boxes':list(E),'reviewed_at':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),'decisions':f'second/{p}_main_decisions.json'}
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
