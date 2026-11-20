"""Root's crop-based consolidation of 123/020, after all three returns."""
from pathlib import Path
import json, copy

O=Path('out'); stem='C123-01_123_scan020'
R={r:json.loads((O/'readers'/stem/r/'report.json').read_text()) for r in ('R1','R2','R3')}
T={r:(O/'readers'/stem/r/'reading.tex').read_text() for r in R}
r1=f'readers/{stem}/R1/crops/'
r2=f'readers/{stem}/R2/crops/'
t=T['R2']
# R3's more detailed graphic preserves the two lower projections and upper point.
old=t[t.index('% The first cell has'):t.index(' réciproque n\'étant pas vraie sans doute.')]
new=T['R3'][T['R3'].index('% Serifed l contour'):T['R3'].index(' réciproque n\'étant pas vraie sans doute.')]
t=t.replace(old,new)
# Preserve five physical rows and left-margin anchoring beside the Borel clause.
oldmargin=t[t.index('\\margin{'):t.index('% archive sheet number:')]
margin=T['R3'][T['R3'].index('% slanted'):T['R3'].index('% archive sheet number:')]
margin=margin.replace('aux unipotents',r'aux \unsure{unipotents}')
margin=margin.replace('\\margin{','\\reversemarginpar\n\\margin{')+'\\normalmarginpar\n'
t=t.replace(oldmargin,'')
t=t.replace('est un Borel (la','est un Borel\n'+margin+'(la')

spec=dict(stem=stem,base_reader='R2',brief='reader_v08.md',main_new_crops=0,
          text_edits=[dict(old=T['R2'],new=t)],difference_overrides={},additional_differences=[])
def ov(n,**kw):spec['difference_overrides'].setdefault(f'R2-{n:02}',{}).update(kw)
cropnames={1:'insertion_ceux.png',2:'first_math.png',3:'set_end.png',4:'deleted_de.png',
5:'heading.png',6:'blank_before_1.png',7:'deleted_lhomomor.png',8:'f_Sl_G.png',
9:'principale.png',10:'principale.png',11:'Z_index.png',12:'last_la.png',
13:'margin.png',14:'margin.png',15:'margin.png',16:'margin.png'}
for n,name in cropnames.items():ov(n,crop=r1+name)
ov(3,confidence='low',evidence='A tiny detached oblique point lies before the inner closing parenthesis. No distinct descending comma tail is secure. The point/comma alternatives are retained; the much larger outer comma is separate.')
ov(6,kind='text not on the page')
ov(9,final='princi + two uncertain p/a and a/p overlays + le; no chronology assigned.',kind='drawing or diagram')
ov(12,final='Uncertain l-like initial with opposing loop contours, two lower projections, a short upper-right trace and a high point drawn; following a definite.',kind='drawing or diagram',
   evidence='The first cell retains l-like serifs and upright but also two opposing loops, two short downward projections and a small high point. Root preserves the more detailed R3 trace drawing. These features do not establish a unique companion glyph or a sequence of impressions. The following a is clear.')
ov(14,evidence='Opening u/n strokes, a detached i dot and the terminal sequence support unipotents, but the central p/o region is crowded by the descending trace from the preceding line. Root cannot separate every central contour and retains R2’s local uncertainty.')

agreed={1:'typed ceux raised above de with a connected unheaded curve',
2:r'first \unsure{\mathfrak{g}|\mathscr{G}}, same first candidate at later occurrences',
3:'an isolated point/comma doubt within the second Fil parentheses',
5:r'\uline{Cas principal}.',6:'unfilled interval before (1)=0',7:r"\deleted{l'homomor}",
8:'blank between Sl(2,k) and G; no arrow',10:'two quotation strokes at each end',
11:'Z_o',13:'no colon after A4',15:'paired quotation strokes around sous-réguliers'}
for n,reading in agreed.items():
    ov(n,readers='R1: '+reading+'; R2: '+reading+'; R3: '+reading+'. Root retains this reading from the cited crop.')
ov(4,readers=r'R1: \deleted{d\unsure{e}}; R2: \deleted{de}; R3: \deleted{de}. Root resolves de: the e middle bar and lower return survive the x strokes.',c_changed=False)
ov(9,readers='R1: pa/ap overlay with local doubt; R2: two separately drawn p/a cells with local doubt; R3: two p/a cells within a whole-word doubt. Root uses R2’s local scope: princi and le are definite; both mixed cells remain uncertain.')
ov(12,readers='R1: l plus an opposed curve and one vertical companion, whole la doubtful; R2: l plus opposed loops and two long companion strokes, a definite; R3: l plus opposed loops, short lower projections, upper-right trace and point, a definite. Root chooses the detailed R3 drawing with first-cell uncertainty only.')
ov(14,readers='R1: unipotents without doubt; R2: unsure unipotents; R3: unipotents without doubt. Root retains R2’s uncertainty in the compressed central cells.')
ov(16,readers='R1: Borels|borels; R2: borels|Borels; R3: borels|Borels. Root favours the long stem with a single lower bowl, retaining both candidates.')

d=copy.deepcopy(next(d for d in R['R3']['differences'] if d['id']=='D16'))
d.update(id='ROOT-01',final='Five slanted rows in the left margin, with separate underlined ex beside Cas A2,A4; anchored alongside the Borel clause.',
         crop=r1+'margin.png',marked_in_H='no',
         readers='R1: five slanted rows with left-margin command, beside Borel; R2: flattened margin prose at paragraph end; R3: five slanted rows at paragraph end. Root preserves five rows and the left-margin location beside Borel.')
d.pop('reading');spec['additional_differences'].append(d)

cd=copy.deepcopy(R['R2']['c_doubts'])
cd_crop=['first_math.png','principale.png','last_la.png','Z_index.png','margin.png','set_end.png','blank_before_1.png','f_Sl_G.png','deleted_lhomomor.png']
for item,crop in zip(cd,cd_crop):item['crop']=r1+crop
cd[2]['decision']='First cell uncertain, drawn with opposing loops and small projections; following a definite.'
cd[5]['confidence']='low'
spec['c_doubts']=cd
spec['remaining_doubts']=[
dict(place='First handwritten Lie-algebra glyph',reading=r'\mathfrak{g}',alternatives=r'\mathscr{G}; later occurrences use the first candidate',confidence='medium'),
dict(place='Internal mark in second Fil parentheses',reading='point',alternatives='comma; no secure descending tail',confidence='low'),
dict(place='Two middle cells in principale',reading='p/a and a/p contours superposed',alternatives='impression order undetermined; both full-word sequences remain possible',confidence='medium'),
dict(place='First cell of final la',reading='l-like body with looped overprint',alternatives='s-, section-sign- or dollar-like companion; identity and order unresolved',confidence='low'),
dict(place='Marginal unipotents',reading='unipotents',alternatives='central p/o contours crowded and incompletely separable',confidence='medium'),
dict(place='Marginal final noun',reading='borels',alternatives='Borels',confidence='medium')]

inv=copy.deepcopy(R['R3']['inventory'])
for item in inv:
    if item['hand'].startswith('pen'):item['hand']=item['hand'].replace('pen','unnamed handwritten annotation',1)
    if item['element']=='Slanted marginal example':
        item['first_words_or_objects']='ex Cas A_2,A_4 / les paraboliques associés / aux unsure unipotents / quoted sous-réguliers sont / des borels|Borels !'
    if 'overlapping cell' in item['element'] or item['element']=='Overprinted first cell of final la':item['kind']='drawing'
    if item['element']=='Overprinted first cell of final la':item['first_words_or_objects']='l-like body, opposing loops, two lower projections, upper-right trace and high point'
spec['inventory']=inv
spec['abbreviations']=copy.deepcopy(R['R3']['abbreviations'])
spec['notes']=(O/'decisions'/f'{stem}_notes.md').read_text()
spec['check_events']=[] # The ten actual root events were logged at the time of checking.
spec['consequential']=[
'Both mathematical intervals remain physically blank: no Lie-algebra letter before (1)=0 and no arrow between Sl(2,k) and G.',
'The interior Fil mark is preserved with point/comma doubt and the typed index is resolved as Z_o.',
'The conditional g(1)=0 criterion and the unqualified unit-stabilizer statement are discussed separately in the notes; their counterexamples never emend the source.']
spec['workflow_note']='Three fresh readers used v08 and each viewed the whole and both halves once. Their crop counts were 13, 11 and 13. Root compared all three complete texts and full reports, viewed all 13 existing R1 crops, R2’s margin crop and R3’s set-separator crop, and made no new crop. An initial multi-image output failed at a context boundary; its three files were successfully displayed once afterward, with no recropping or claim that the failed output had been seen. One overlong R3 report output was truncated; the omitted C-doubt section and current text were read separately. Root resolved R1’s tentative cancelled e, retained R2’s compressed-word doubt, favoured lowercase b with a capital alternative, and used R3’s detailed mixed-cell graphic and five-row margin. The text-only auxiliary audit found an empty final-la apparatus field in R2 and confirmed the 17-locus union; root supplied the final reading. H emph and missing handwriting wrappers were treated as macro-only, not inflated into changes. v09 will add a final field-content check for graphic apparatus rows and a check that slanted margin geometry is represented rather than only mentioned.'
(O/'decisions'/f'{stem}_spec.json').write_text(json.dumps(spec,ensure_ascii=False,indent=2)+'\n')
(O/'decisions'/f'{stem}_preview.tex').write_text(t)
print(json.dumps({'preview':str(O/'decisions'/f'{stem}_preview.tex'),'loci':len(R['R2']['differences'])+1,'inventory':len(inv)}))
