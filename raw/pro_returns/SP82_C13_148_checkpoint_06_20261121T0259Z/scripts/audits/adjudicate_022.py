"""Main-reader decisions entered after viewing all ten differing audit crops."""
from pathlib import Path
from datetime import datetime,timezone
import csv,json

B=Path(__file__).resolve().parents[2]
rp=B/'reviews/148_scan022.json'
p=json.loads(rp.read_text())
with (B/'second/148_scan022_comparison.tsv').open() as f:
    comparison={r['box']:r for r in csv.DictReader(f,delimiter='\t')}
boxes={r['box']:r for r in p['second_boxes']}

abbr=r'lab \unsure{cl.|\(\varphi\).} des liquides'
submission=r'''\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\node[anchor=west] at (0.03,0.11) {- Soumission};
\draw[line width=.6pt] (0.45,0.62) -- (0.52,0.65);
\draw (1.16,0.56) -- (1.22,0.57);
\draw[line width=.6pt] (2.60,0.53) -- (2.74,0.87);
\end{tikzpicture}}'''
entries=[]
def decide(box,ink,confidence='high',final=None):
    r=dict(box=box,choice='revised' if final is not None else 'first',
           viewed_by_main=True,ink=ink,confidence=confidence)
    if final is not None:r['final']=final
    entries.append(r)

decide('B022-01','Both readings give5400–5420. The blind reading includes the surrounding frame; that frame is already present around the range in the approved page. No numeral or frame is omitted from the page.')
decide('B022-02','The middle digit has a closed upper loop followed by a descending right stem and a leftward foot, matching the earlier9 in(93); it lacks a closed lower bowl. Read91, not81. The separators after51 and91 descend as commas. The isolated point after00 sits above the numeral baseline and remains unassigned; the baseline point after411 is retained. Wrapper syntax does not affect the reading.','medium',r'(93) 51, 91, 00 \quad 411.')
decide('B022-03','The final small honorific stroke has an r-like shoulder and no separately bounded e loop. It rests with the following name rather than being demonstrably a superscript. Retain Mr BEZOT; the leading short stroke is already drawn on the page.','medium')
decide('B022-04','An initial open low curve is joined to a tall loop and long descending return. The first-pass cl reading is possible, but the single looped phi-like form proposed independently cannot be excluded. Reopen the resolution as local doubt; do not expand it from an assumed laboratory name.','low',abbr)
decide('B022-05','The initial letter has a low bowl and a long descending stem, supporting the lowercase p retained in parc. The remaining arc and Valrose strokes agree.','medium')
decide('B022-06','The fourth digit has one upper arch and a lower loop with a long rightward exit, like the2 in the range and bottom foliation. It is not a pair of open lobes forming3. The final4 has an angled left stroke, cross stroke and long right stem; retouching does not establish a different earlier digit. Retain06024 Nice.','medium')
decide('B022-07','The initial S rises above the following o/u body and has the larger descending return of a capital. Three detached dark strokelets above the word have discernible lengths and directions and are reproduced without inventing a word or cancellation underform. The isolated round fleck included by the blind drawing has no stable textual alignment and is not adopted as punctuation.','medium',submission)
decide('B022-10','A small separate dark point stands to the right of the numeral1 foot and before A, with a visible gap from the foot. Retain PLN1.A. The heavier P is retraced; no additional earlier letter is inferred.','medium')
decide('B022-12','The same looped2 and upright1 are read in both versions. The page already places21 in a margin macro; the blind nested page-marker wrapper introduces no different numeral or attribution.')
decide('B022-13','The two short strokes beside the address lines agree. The blind crop also contains part of the neighboring curly brace, which is already drawn in full in the page. The first excerpt selected only the two strokes; neither the brace nor a stroke needs adding.')
assert {r['box'] for r in entries}=={k for k,v in comparison.items() if v['different']=='yes'}
(B/'second/148_scan022_adjudications.json').write_text(json.dumps(entries,ensure_ascii=False,indent=2)+'\n')

page=B/'pages/148_scan022.tex'
t=page.read_text().replace('(93) 51, 81, 00','(93) 51, 91, 00')
t=t.replace(r'lab cl. des liquides',abbr).replace(r'{\handwritten{- soumission}}',r'{\handwritten{- Soumission}}')
needle=r'\node at (900,107) {\handwritten{- Soumission}};'
assert needle in t
marks=r'''% Detached dark strokelets above the annotation; no word is inferred.
\draw[line width=.55pt] (935,64)--(940,61);
\draw[line width=.35pt] (1012,70)--(1022,69);
\draw[line width=.55pt] (1134,75)--(1152,46);'''
t=t.replace(needle,marks+'\n'+needle)
page.write_text(t)

p['changes']=[r for r in p['changes'] if r['place']!='Address, laboratory abbreviation; resolution M0237']
def change(place,c,final,box,ink,kind,confidence):
    b=boxes[box]
    p['changes'].append(dict(place=place,c=c,h='',final=final,ink=ink,
        crop=f'crops/second/148_scan022/{box}.png',box=[b[k] for k in ('x0','y0','x1','y1')],
        confidence=confidence,kind=kind,against_c=True,against_h=False,math=False))
change('Blind audit: middle phone pair','81','91','B022-02',entries[1]['ink'],'misread symbol or index','medium')
change('Blind audit: submission initial','soumission','Soumission','B022-07','The initial S is taller than the following lowercase body, with a full descending return.','misread word','medium')
change('Blind audit: detached strokes above submission','',marks,'B022-07','Three dark detached strokelets, including a longer oblique one at the right, are visible above the word. They are copied as strokes without assigning an erased word; the isolated round fleck is not adopted.','drawing or diagram','medium')
for r in p['decisions']:
    if r['id']=='M0237':
        r.update(decision='undecided',reading=r'\unsure{cl.|\(\varphi\).}',
                 ink=entries[3]['ink'],crop='crops/second/148_scan022/B022-04.jxl',
                 box=[402,278,960,389],confidence='low')
p['unresolved'].append(dict(id='U022-B04',place='Laboratory abbreviation, blind audit',
    reading=r'\unsure{cl.|\(\varphi\).}',alternatives=['cl.',r'\(\varphi\).'],
    issue=entries[3]['ink'],confidence='low',crop='crops/second/148_scan022/B022-04.jxl',box=[402,278,960,389]))
p['unresolved'].append(dict(id='U022-B07',place='Detached strokes above submission',
    reading='three literal strokelets',alternatives=[],
    issue='The dark strokelets are copied without assigning them an earlier word or punctuation function. Their intended significance is not established.',
    confidence='low',crop='crops/second/148_scan022/B022-07.jxl',box=[1025,205,1378,302]))
for r in p['inventory']:
    r['first_words_or_objects']=r['first_words_or_objects'].replace('51, 81','51, 91').replace('soumission /','Soumission /').replace('lab cl. des liquides',abbr)
p['inventory'].append(dict(element='Detached strokes above submission annotation',kind='drawing',
    position='upper centre, above Soumission',first_words_or_objects='three unassigned dark strokelets',
    sheet_kind='reused_typed',hand='unnamed hand (attribution uncertain)',transcribed='yes'))
p.setdefault('notes',[]).append(dict(id='148-022-BLIND',text='The blind audit changed81 to91 by comparison with the visibly similar9 in(93), capitalized Soumission, and preserved three detached strokelets without assigning words to them. It reopened the laboratory abbreviation as cl./phi-like uncertainty; the original resolution of M0237 is withdrawn. The postcode06024 and the internal point in PLN1.A remain supported.'))
p.setdefault('hand_log',[]).append(dict(habit='The9 has an upper loop, a long descending right stem and a leftward foot; thick retracing can mimic a second bowl.',pages=[22],holds_at_every_observed_occurrence=True,witness_effect='The two9 forms in the phone annotation support91 where C and the first pass had81. This observation is confined to these two occurrences.'))
rp.write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (B/'reviews/visual_log.tsv').open('a') as f:
    for r in entries:f.write(f'{now}\t022\tcrops/second/148_scan022/{r["box"]}.png\tMain reader viewed differing blind box; {r["ink"]}\n')
print('022 page, witness records and ten visual adjudications written; original first reading unchanged.')
