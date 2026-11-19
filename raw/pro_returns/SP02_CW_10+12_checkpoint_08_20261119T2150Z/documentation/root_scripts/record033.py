from pathlib import Path
import json
R={'folder':'B10-01','cote':'10','scan':33,'sheet_kind':'typescript','inventory_from_C':True,'inventory_overrides':{'replacement-note':{'first_words_or_objects':r'Les p\textsuperscript{ges} qui suivent'}},'edits':[],'changes':[],'remaining_doubts':[],'notation_updates':[]}
def edit(a,b): R['edits'].append({'old':a,'new':b})
edit(r'\unsure{pages|p\textsuperscript{ges}}',r'p\textsuperscript{ges}')
edit(r'\unsure{remplacent}',r'remplacent')
edit(r'\unsure{antérieur}',r'antérieur')
edit(r'\unsure{(pages|pages|p\textsuperscript{ges}}',r'\unsure{(p\textsuperscript{ges}|p\textsuperscript{ges}}')
edit(r'\unsure{aligner}',r'aligner')
edit(r'\deleted{\unsure{de}}',r'\deleted{de}')
def row(place,c,h,f,shows,crop,kind='other',conf='high',dc=False,dh=True,marked=False):
 R['changes'].append(dict(place=place,C=c,H=h,final=f,shows=shows,crop=crop,kind=kind,confidence=conf,against_C=dc,against_H=dh,marked_in_H=marked))
row('top centre','1','omitted','1','Handwritten upright 1 with base stroke.','page-number','omission')
row('upper left note, first line',r'\unsure{pages|p\textsuperscript{ges}}',r'\uncertain{11} pages',r'p\textsuperscript{ges}','One descending p followed by raised ges; no separate 11.','margin-upper','misread word','high',True,True,True)
row('upper left note, third line',r'\unsure{remplacent} le','sont le','remplacent le','Initial r-e-m-p-l followed by a-c-e-n-t; long descending p is visible.','margin-upper','misread word','high',True)
row('upper left note, fifth line',r'\unsure{antérieur}',r'aux \uncertain{anciennes}','antérieur','Single word with t accent and final r, no aux or final -nes.','margin-upper','misread word','medium',True,True,True)
row('upper left note, before 82',r'\unsure{(pages|pages|p\textsuperscript{ges}}','pages',r'\unsure{(p\textsuperscript{ges}|p\textsuperscript{ges}}','Descending p and raised ending; a separate opening parenthesis cannot be isolated reliably.','margin-upper','abbreviation expanded or spelling modernised','medium',True)
row('upper left note enclosure','oval in TikZ','description in note','oval in TikZ','Continuous enclosure round the slanted note.','margin-upper','drawing or diagram')
row('heading','underlined title','heading without underline','underlined title','Continuous rules under both lines of the title.','whole top','omission')
row('10.0 first base symbol','S_o','S_0','S_o','Small typed round index is the x-height o, shorter than the zeros of 10.0.','notation','misread symbol or index')
row('10.0 structure-sheaf base','O_{S_o}','O_{S_0}','O_{S_o}','Same small round typed index under S.','notation','misread symbol or index')
row('10.0 quasi-compact',r'qu\handwritten{/}asi-compact','quasi-compact',r'qu\handwritten{/}asi-compact','Dark oblique pen stroke between u and a is present; function uncertain.','notation','omission')
row('10.0 algebra symbols',r'\unsure{\mathscr{A}|\mathcal{A}} then \mathscr{A}',r'\mathcal{A}',r'\unsure{\mathscr{A}|\mathcal{A}} then \mathscr{A}','Rounded handwritten loop with right stroke; calligraphic/font distinction remains uncertain.','notation','misread symbol or index','medium',False)
row('10.0 after functor product',r'\deleted{\unsure{,}}','omitted',r'\deleted{\unsure{,}}','Compact overstruck punctuation cluster; underlying comma remains a low-confidence reading.','functors','omission','low')
row('10.0 between functor formula and relocated phrase',r'i\leqq j',r'i\leqslant j',r'i\leqq j','Left angle above TWO horizontal lower bars.','functors','misread symbol or index')
row('10.0 entre ces catégories','inserted after foncteurs','struck at old position, relocation described in note','inserted after foncteurs','Phrase is circled; continuous return line ends with arrowhead immediately after foncteurs.','functors','insertion or placement')
row('10.0 composition',r'\unsure{o|\circ}',r'\circ',r'\unsure{o|\circ}','Typed upright oval at x-height; o/circle glyph distinction not settled.','functors','misread symbol or index','medium')
row('10.0 cancelled transition',r'\deleted{Plus précisément,}',r'\struck{Plus précisément}',r'\deleted{Plus précisément,}','Terminal comma belongs to the struck phrase and remains visible.','functors','omission')
row('left middle note',r'\unsure{aligner}','omitted','aligner','After rotation, a-l-i-g-n-e-r with g descender is legible inside an oval.','aligner','omission','high',True)
row('left middle note enclosure','tilted oval in TikZ','omitted','tilted oval in TikZ','Thin elliptical pencil enclosure.','aligner','drawing or diagram')
row('middle margins','two ) and two (','omitted','two ) and two (','Two opening strokes on right, two closing strokes on left accompany alignment instruction.','aligner; then; whole middle','omission')
row('notation paragraph j comparison',r'j\leqq i',r'j\leqslant i',r'j\leqq i','Two separate horizontal bars below left angle.','j-le-i','misread symbol or index')
row('Alors and inserted citation',r'Alors :\inserted{(EGA \uline{IV} 8.8.2)}\unsure{;|:}','Alors (EGA IV 8.8.2) :',r'Alors :\inserted{(EGA \uline{IV} 8.8.2)}\unsure{;|:}','Typed colon remains BEFORE the added parenthesized citation; IV has a pencil underline; another two-part mark follows the closing parenthesis, its lower tail uncertain.','then','insertion or placement','medium')
row('i), Hom source',r'\operatorname{Hom} S_i(X_i,Y_i)',r'\mathrm{Hom}_{S_i}(X_i,Y_i)',r'\operatorname{Hom} S_i(X_i,Y_i)','Typed S sits on the SAME baseline as Hom; only i is lowered.','Hom','misread symbol or index')
row('i), entire assertion','underlined','no underline','underlined','Pencil horizontal rules run beneath both lines.','whole middle','omission')
row('ii), isomorphism',r'X\xrightarrow{\sim}X_j\times_{S_j}S',r'X\simeq X_j\times_{S_j}S',r'X\xrightarrow{\sim}X_j\times_{S_j}S','Small right arrow below a wavy mark, not a second wavy/equality stroke.','whole middle','misread symbol or index')
row('ii), entire assertion','underlined','no underline','underlined','Two continuous rules under the two lines.','whole middle','omission')
row('10.1 first line',r'\deleted{\unsure{de}}',r'\struck{\ill{}}',r'\deleted{de}','Printed d ascender and following e survive the deletion.','de','readable ink left as \\ill{}','high',True,True,True)
row('10.1 final comparison',r'j\leqq i',r'j\leqslant i',r'j\leqq i','Left angle with two lower horizontal bars.','j-le-i-bottom','misread symbol or index')
row('10.1 propriété ending',r'propriété\inserted{s}',r'propriété\supplied{s}',r'propriété\inserted{s}','Small pencil s attached to the printed singular ending, not an editorially supplied letter.','last-edit','insertion or placement')
row('10.1 immediately before être',r'\deleted{\unsure{d\'}}','omitted',r'\deleted{\unsure{d\'}}','Dark cancellation immediately after the colon; possible d and apostrophe cannot be separated securely.','last-edit','omission','low')
R['remaining_doubts']=[{'place':p,'reading':r,'alternatives':a,'confidence':c} for p,r,a,c in [
 ('upper left note before 82',r'(p\textsuperscript{ges}',r'p\textsuperscript{ges}','medium'),('first algebra symbol',r'\mathscr{A}',r'\mathcal{A}','medium'),('after functor product','deleted comma','unresolved cancelled punctuation','low'),('composition','o',r'\circ','medium'),('after EGA IV 8.8.2',';',':','low'),('before être',"deleted d'",'underlying cancelled text uncertain','low')]]
R['notation_updates']=[
 {'sign':'algebra A','reading':r'\mathscr{A} | \mathcal{A}','evidence':'10/033 §10.0; rounded handwritten loop with right stem; alternatives retained on first occurrence','status':'ambiguous'},
 {'sign':'structure sheaf O','reading':r'\mathcal{O}','evidence':'10/033 §10.0; loop with upper curl','status':'read'},
 {'sign':'base index','reading':'S_o','evidence':'10/033 §10.0; small typewriter o, below S','status':'read'},
 {'sign':'left comparison','reading':r'\leqq','evidence':'10/033 three occurrences, angle above TWO bars','status':'read'},
 {'sign':'typed composition glyph','reading':r'o | \circ','evidence':'10/033 transitivité; x-height typed oval','status':'ambiguous'},
 {'sign':'property P','reading':r'\mathbb{P}','evidence':'10/033 §10.1; hand-drawn doubled upright/bowl','status':'read'},
 {'sign':'transition functor','reading':r'\rho','evidence':'10/033 §10.0; loop and descender','status':'read'},
 {'sign':'page abbreviation','reading':r'p\textsuperscript{ges}','evidence':'10/033 upper left note, twice; descending p plus raised ending','status':'read'}]
R['crops']=[]
for name,box,rotation,scale in [('margin-upper',(15,135,360,657),-35,2),('functors',(360,599,1465,770),0,2),('aligner',(28,746,302,956),-38,2),('notation',(350,280,1654,480),0,2),('then',(1160,849,1618,931),0,2),('Hom',(703,1001,1068,1081),0,2),('de',(882,1598,1136,1667),0,2),('last-edit',(477,1940,1112,2031),0,2),('j-le-i',(569,853,745,919),0,3),('j-le-i-bottom',(439,1881,640,1953),0,3),('page-number',(811,14,904,70),0,3)]:
 R['crops'].append({'id':name,'source':'SP02_CW_10+12_scans/B10-01_10_scan033.jpg','box':box,'rotation':rotation,'scale':scale})
R['inspection_note']='Whole image, a and b halves viewed in order; all body prose and formulas compared against both witnesses; rotated upper and middle margin crops, formula and cancellation crops examined. C inventory read in full and matched to the page. Not a mathematical proof check.'
Path('work/record033.json').write_text(json.dumps(R,ensure_ascii=False,indent=2))
print('Recorded',len(R['changes']),'explicit collation decisions')
