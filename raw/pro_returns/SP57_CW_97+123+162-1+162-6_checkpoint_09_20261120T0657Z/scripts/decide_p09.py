"""Root consolidation from the three independent readings and viewed local crops."""
from pathlib import Path
import json, copy

O=Path('out'); stem='C123-02_123_scan022'
R={r:json.loads((O/'readers'/stem/r/'report.json').read_text()) for r in ('R1','R2','R3')}
T={r:(O/'readers'/stem/r/'reading.tex').read_text() for r in R}
r1=f'readers/{stem}/R1/'; r2=f'readers/{stem}/R2/'; r3=f'readers/{stem}/R3/'
root=f'decisions/rootcrops/{stem}/'
t=T['R3'].replace('\\cotefile{123}\n','')
t=t.replace('\\handwritten{\\unsure{Massy}',r'\hfill\handwritten{\unsure{Massy}',1)
old=t[t.index('\\margin{'):t.index('% Bottom margin note')]
footer=T['R2'][T['R2'].index('\\margin{'):T['R2'].index('% Bottom margin note:')]
footer=footer.replace(r'exten\unsure{s}ion',r'ext\unsure{e|a}n\unsure{s}ion')
footer=footer.replace(r'\node at (8.97,-.02) {$\mathbb{Z}/h\mathbb{Z}$};',r'\node at (8.97,-.02) {$\mathbb{Z}/h\unsure{Z|\mathbb{Z}}$};')
footer=footer.replace(r'hen\unsure{ce} of order',r'hen\unsure{ce} of ord\unsure{er}')
footer=footer.replace(r'\node at (11.92,-.02)',r'\node[rotate=-3] at (11.92,-.02)')
footer=footer.replace(r'\node at (13.23,-.42)',r'\node[rotate=-3] at (13.23,-.42)')
t=t.replace(old,footer)
# The bottom note is anchored as a margin object in the continuing paragraph.
t=t.replace('(they\n\n\n\\margin{','(they\n\\margin{')
t=t.replace('% Bottom margin note,', '% The thin interrupted trace through the multiplication sign is reproduced without a mathematical function; ink versus surface origin remains uncertain.\n% Bottom margin note,')

spec=dict(stem=stem,base_reader='R3',brief='reader_v09.md',main_new_crops=5,
 text_edits=[dict(old=T['R3'],new=t)],difference_overrides={},exclude_difference_ids=['D29','D30'],additional_differences=[])
def ov(n,**kw):spec['difference_overrides'].setdefault(f'D{n:02}',{}).update(kw)
mapping={1:'01_date.png',2:'02_journal_title.png',3:'02_journal_title.png',5:'03_polynomail.png',
6:'03_polynomail.png',7:'04_appeared.png',8:'05_alg.png',9:'06_first_quadruples.png',
11:'07_first_count_W.png',12:'07_first_count_W.png',13:'07_first_count_W.png',14:'08_insertions_euler.png',
15:'08_insertions_euler.png',16:'08_insertions_euler.png',17:'08_insertions_euler.png',18:'08_insertions_euler.png',
19:'09_stability.png',23:'10_automorphisms.png',24:'11_last_quadruples.png',25:'12_note_left.png',
26:'13_note_ratios_cancel.png',27:'13_note_ratios_cancel.png',28:'14_note_tail.png'}
for n,c in mapping.items():ov(n,crop=r1+c)
for n,c in {4:'title_join.png',10:'apposition_quotes.png',20:'rigid_quotes.png',21:'general_position_quotes.png',22:'opposite_quotes.png'}.items():ov(n,crop=root+c)
ov(4,evidence=R['R3']['differences'][3]['evidence']+' Root also viewed R1/02_journal_title.png for the opening and root title_join.png for the closing.')
ov(6,crop=root+'title_join.png',evidence='Root title_join.png shows the two opening pen strokes before Lie; R1/03_polynomail.png shows the two closing strokes after rings. Both are paired strokes, not guillemets.')
ov(7,readers='R1: r-like body with two oblique strokes, no correction chronology; R2: r-like body with one continuous pen curve and k alternative; R3: r body with two oblique surviving strokes, no chronology. Root retains R3’s local uncertain graphic; a definite deleted predecessor is not established.')
ov(11,crop=r2+'07_first_card.jpg',readers='R1: definite 2, inventory leaves medium unresolved; R2: handwritten 2; R3: definite 2 with typed/handwritten medium unresolved. Root retains the glyph with medium unresolved; H explicitly calls it handwritten.',final='2; typed versus handwritten medium unresolved (comment and inventory).')
ov(13,confidence='low',readers='R1: H|W under pen W; R2: H|W under pen W, low confidence; R3: H|W under pen W. Root retains both lower candidates at low confidence.')
ov(14,readers='R1: words raised with an insertion macro; report notices but text omits curve. R2: raised words and curve beside baseline comma drawn. R3: same geometry, with different drawing coordinates. Root uses R3’s drawing, preserving the live comma.')
ov(18,readers='R1: raised typed generating, curve mentioned but not drawn; R2: typed generating with curved leader; R3: typed generating with curved leader. Root uses R3’s drawing. All three reject H’s explicit handwritten-medium description.')
ov(23,readers='R1: uncertain k/i overlay; R2: uncertain k/i overlay, glyph contours high confidence but order unresolved; R3: uncertain k/i overlay. Root keeps both contours without a chronology, at medium overall confidence.')
ov(25,final=r'ext\unsure{e|a}n\unsure{s}ion',crop=r3+'16_note_left.jpg',
 evidence='The letter after ext is a compressed rounded loop without a secure e cross-stroke; the s-region is a short merged stroke before dotted i. The two local doubts remain, while the surrounding letters are definite.',
 readers=r'R1: extension; R2: exten\unsure{s}ion; R3: ext\unsure{e|a}nsion. Root retains both local uncertainties: ext\unsure{e|a}n\unsure{s}ion.')
ov(26,readers=r'R1: \unsure{Z|\mathbb{Z}}; R2: \mathbb{Z}; R3: \unsure{Z|\mathbb{Z}}. Root retains plain Z first: the weak secondary trace does not securely establish a doubled diagonal.')
ov(28,final=r'hen\unsure{ce} of ord\unsure{er}',crop=r2+'18_note_right.jpg',
 evidence='The initial hen strokes and initial ord contours are identifiable; final ce and er are compressed joined traces. The doubt is limited to those endings.',
 readers=r'R1: hence of order; R2: hen\unsure{ce} of order; R3: \unsure{hence} of \unsure{order}. Root keeps hen and ord definite and doubts the compressed endings only.')

for i,n in enumerate([25,26],1):
 d=copy.deepcopy(next(d for d in R['R1']['differences'] if d['id']==f'R1-{n}'))
 d.update(id=f'ROOT-{i:02}',final=('center of G-tilde below-left of final Z, with an oblique leader' if n==25 else r'hen\unsure{ce} of ord\unsure{er} above a separate lower-right hz\varphi(h) formula'),marked_in_H='no',
  readers='R1: lower annotation and lower-right formula drawn in separate inline pictures; R2: both reproduced within a full footer layout; R3: both drawn within a full footer layout. Root uses R2’s relative-position layout, with the separately adjudicated local doubts.')
 d.pop('reading');spec['additional_differences'].append(d)
d=copy.deepcopy(next(d for d in R['R2']['differences'] if d['id']=='R2-D27'))
d.update(id='ROOT-03',final=d.pop('reading'),confidence='low',marked_in_H='no',
 evidence='A thin interrupted vertical trace crosses the multiplication sign. Its segments are visible, but ink/surface origin and function are unresolved. It is drawn without converting it into a mathematical operator.',
 readers='R1: omitted; R2: interrupted vertical trace drawn; R3: omitted. Root retains R2’s visible segments with the origin/function qualification.')
spec['additional_differences'].append(d)
spec['additional_differences'].append(dict(id='ROOT-04',place='Upper-right location of place/date',C=r'\handwritten{\unsure{Massy} 22. 10. 1969}\\',H='Massy 22.10.1969, without a placement command',
 final=r'\hfill\handwritten{\unsure{Massy} 22. 10. 1969}\\',evidence='The heading crop occupies whole-page x1230–1562 near the right edge, above the salutation. The transcription retains that right alignment.',confidence='high',kind='insertion or placement',marked_in_H='no',c_changed=True,h_changed=True,crop=r1+'01_date.png',
 readers='R1: right-aligned heading; R2: unpositioned heading although inventory says upper right; R3: unpositioned heading although inventory says upper right. Root keeps R1’s explicit right alignment.'))

cd=copy.deepcopy(R['R3']['c_doubts'])
cd_crops=['01_date.png','02_journal_title.png','05_alg.png','06_first_quadruples.png','11_last_quadruples.png','04_appeared.png','07_first_count_W.png','10_automorphisms.png','13_note_ratios_cancel.png','03_polynomail.png',None,'08_insertions_euler.png']
for item,c in zip(cd,cd_crops):
 if c:item['crop']=r1+c
cd[6]['confidence']='low'
spec['c_doubts']=cd
spec['remaining_doubts']=copy.deepcopy(R['R3']['remaining_doubts'])
for d in spec['remaining_doubts']:
 if d['place']=='where W predecessor':d['confidence']='low'
 if d['place']=='Bottom note extension':d.update(reading=r'ext\unsure{e|a}n\unsure{s}ion',alternatives=['e/a after ext; short merged s trace'])
 if d['place']=='Bottom note right-hand prose':d.update(reading=r'hen\unsure{ce} of ord\unsure{er}',alternatives=['compressed ce and er endings'])
spec['remaining_doubts'].append(dict(place='Interrupted vertical trace through footer multiplication',reading='four thin vertical segments drawn',alternatives='ink or surface trace; function unresolved',confidence='low'))
inv=copy.deepcopy(R['R3']['inventory'])
for item in inv:
 if item['hand'].startswith('pen'):item['hand']=item['hand'].replace('pen','unnamed handwritten annotation',1)
 if item['element']=='automorphisms overprinted cell':item['kind']='drawing'
 if item['element']=='Bottom note main row':item['first_words_or_objects']=r'* NB: ... ext\unsure{e|a}n\unsure{s}ion ... hen\unsure{ce} of ord\unsure{er}'
trace=copy.deepcopy(next(i for i in R['R2']['inventory'] if i['element']=='Separate vertical trace at multiplication'))
trace['hand']='thin trace; ink or surface origin unresolved'
inv.insert(next(i for i,x in enumerate(inv) if x['element']=='Bottom note center annotation'),trace)
inv.append(copy.deepcopy(R['R2']['inventory'][-1]))
spec['inventory']=inv
spec['abbreviations']=copy.deepcopy(R['R2']['abbreviations'])
spec['notes']=(O/'decisions'/f'{stem}_notes.md').read_text()
spec['consequential']=[
'The body has underlined plain Z letters and crossed-oval phi glyphs; the footer’s integer alphabet and open varphi are read separately.',
'The first exponent 2 is secure, its medium is not; the footer’s second denominator Z retains a local plain/double-struck doubt.',
'Both insertion curves and the lower-row footer geometry are restored; no solidus grouping or unit-group star placement is mathematically repaired.']
spec['check_events']=[dict(statement_id='123-022-reader-factor-product',who='GPT-6 Astra Pro; inherited effort (not exposed); fresh R3 page 9',type='targeted proof check',outcome='Reader reported multiplying the indicated cyclic/kernel/quotient orders to hz phi(h), conditional on the stated extension; did not prove that extension.'),dict(statement_id='123-022-reader-count-ratio',who='GPT-6 Astra Pro; inherited effort (not exposed); fresh R2 page 9',type='targeted proof check',outcome='Reader reported the symbolic product hz phi(h) and cancellation of phi(h) between the two proposed class counts; no Lie-theoretic classification proof.')]
spec['workflow_note']='Three fresh readers used v09, with 14, 18 and 18 crops. Root read all three complete texts and reports, viewed all fourteen R1 crops plus R2 07/08/17/18 and R3 16, and made five quotation crops where none existed. Two attempted image outputs failed at a context boundary and were subsequently displayed individually from the same files; no failed display was treated as an observation. A long text output was truncated and its omitted sections were read in bounded outputs. The text-only auxiliary audit compared the witness/reader union without viewing images and corrected the readers’ over-specific attribution of the C question’s article alternative to H. Main disagreements concerned local footer uncertainty, the first exponent’s medium, the thin vertical footer trace and graphic descriptions not actually drawn. Root kept the visible trace with origin/function unresolved, combined local letter doubts, and used both drawn insertion curves. The footer spelling doubts are reading uncertainties, not demonstrated source errors. The next brief adds an explicit report-to-text check for each claimed curve and a distinction between glyph certainty and medium certainty.'
(O/'decisions'/f'{stem}_spec.json').write_text(json.dumps(spec,ensure_ascii=False,indent=2)+'\n')
(O/'decisions'/f'{stem}_preview.tex').write_text(t)
print(json.dumps({'loci':len(R['R3']['differences'])-2+len(spec['additional_differences']),'inventory':len(inv),'remaining':len(spec['remaining_doubts'])}))
