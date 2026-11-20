from pathlib import Path
import json,re,difflib
root=Path('/workspace/scratch/6d55c8c3e5a7')
out=root/'work/readers/029/B'
C=(root/'work/inputs/029/C.tex').read_text()
reading=C
q=chr(96)*2
qq="''"
freeze=json.loads((out/'audit/frozen_loci.json').read_text())
loci={r['id']:r for r in freeze['unresolved_loci']}
changes=[]
def edit(cid,place,old,new,kind,evidence,crop,confidence='high',report_c=None,report_r=None):
 global reading
 assert old in reading,(cid,old)
 assert reading.count(old)==1,(cid,'not unique',reading.count(old))
 reading=reading.replace(old,new,1)
 loc=loci[crop]
 changes.append({'id':cid,'place':place,'c':report_c if report_c is not None else old,'h':None,'reading':report_r if report_r is not None else new,'diff_c':True,'diff_h':False,'kind':kind,'marked_in_H':False,'confidence':confidence,'evidence':evidence,'crop':loc['output'],'source':loc['source'],'bbox':loc['bbox']})
# Geometric marks are deliberately not interpreted as letters or punctuation.
topmark=r'\makebox[0pt][r]{\raisebox{2.5ex}{\tikz[x=1ex,y=1ex]{\fill (0,0)--(.17,-.07)--(.30,.60)--(.16,.88)--(.02,.65)--cycle;}}\hspace{.35em}}'
uppertrace=r'\margin{\tikz[x=1ex,y=1ex]{\draw[black!55,line width=.35pt,line cap=round] (.12,.75) .. controls (.06,.47) and (.08,.21) .. (.15,0);}}'
paren=r'\tikz[baseline=0pt,x=1ex,y=1ex]{\draw[line width=.08ex,line cap=round] (.10,1.6) .. controls (.53,.8) and (.52,.05) .. (-.12,-.48);\draw[line width=.08ex,line cap=round] (.46,.04)--(.92,.04);}'
overlap=r'\tikz[baseline=(aold29B.base)]{\node[inner sep=0pt] (aold29B) {\deleted{\unsure{a|o}}};\node[anchor=base west,inner sep=0pt] at (aold29B.base west) {a};}'
commword=r'co\tikz[baseline=(comm29B.base)]{\node[inner sep=0pt] (comm29B) {m};\fill ([xshift=.05em,yshift=1.05ex]comm29B.north) circle (.32pt);}mutes'
refmarks=r'\tikz[baseline=(ref360B.base),x=1em,y=1ex]{\node[anchor=base west,inner sep=0pt] (ref360B) at (0,0) {l-17};\fill (.67,3.1) circle (.42pt);\fill (.62,2.66) circle (.44pt);\fill (.48,1.75) circle (.40pt);\fill (1.50,2.39) circle (.28pt);}'
openpoint=r'\tikz[baseline=(quote360B.base),x=1em,y=1ex]{\node[inner sep=0pt] (quote360B) {'+q+r'};\fill ([xshift=-.05em,yshift=-.55ex]quote360B.south) circle (.25pt);}'
rightdots=r'\margin{\tikz[x=1ex,y=1ex]{\fill (.23,.42) circle (.35pt);\fill (0,0) circle (.35pt);}}'
edit('top-mark','Above-left of first p335 entry',"' p335",topmark+'p335','other','The dark mark has an irregular filled vertical outline and a brown/orange upper surround. It is not securely an apostrophe. Its dark geometry is retained at the observed raised position, with origin unassigned; the coloured surround is a material observation.','01','medium')
edit('upper-right-trace','Right margin beside p336', 'p.336 l.-8 '+q+'skilful'+qq,'p.336 l.-8 '+q+'skilful'+qq+'\n'+uppertrace,'omission','A short, faint, slightly bowed vertical trace is distinct from the long pale vertical paper feature. It is preserved geometrically without a letter or punctuation interpretation.','30','medium',report_c='',report_r=uppertrace)
edit('perhaps-stop','p338 final perhaps','perhaps.','perhaps','text not on the page','The final s ends in a curved terminal stroke. The tight crop includes the blank area to its right and below; there is no separate full stop.','02')
edit('better-mark','p341 l.2 after better','better.','better'+r'\unsure{,|.}','misread symbol or index','The low terminal mark is an oblique, filled shape with a lower-left extension. A comma is favoured, but the broad pen shape does not exclude a period.','04','medium')
edit('doesnt-opener','p341 l7 opening quotation',"l7 'doesn't"+qq,'l7 '+r'\unsure{'+"'|"+q+r'}doesn\'t'+qq if False else 'l7 '+r'\unsure{'+"'|"+q+r"}doesn't"+qq,'misread symbol or index','The high opening cluster is one curved body with a short intersecting upper projection; a single bent tick and fused pair remain possible. The final two quote strokes are separate.','04','low')
edit('342-reference-point','342 second line reference','l-8 '+q+"couldn't"+qq,'l.-8 '+q+"couldn't"+qq,'omission','A distinct low point lies between the foot of l and the horizontal minus, separate from both.','05')
edit('again-terminal','p345 l.7 closing parenthesis','(again).','(again'+paren,'other','The closing curve has a joined rightward horizontal bar at baseline height. No detached period follows it. The curve and bar are reproduced together.','06')
edit('also-short-word','p350 after also','also in l.15.','also '+r'\unsure{in|on} l.15.','misread word','The first low body is closed and triangular, with a detached high point above the short word. It permits a looped i or o; the following n is clear.','07','low')
edit('overwritten-a','p351 l-11 inadequacies',r'in\deleted{\unsure{a|o}}adequacies',r'in'+overlap+'dequacies','insertion or placement','The old oval and the live a occupy one glyph space immediately after in. The current a is certain; the surviving older oval does not decide a versus o. Sequential printing would introduce a second physical glyph space.','09')
edit('353-opener','p353 l.9 its opener','p353 l.9 '+q+'its'+qq,'p353 l.9 '+r'\unsure{'+q+"|'}its"+qq,'misread symbol or index','The opener is a narrow joined loop with two top tips and a common lower turn. A fused pair is favoured, but a single looped tick remains possible.','10','low')
edit('from-opener','p355 l-3 from opener','do you mean '+q+'from $(*)$'+qq,'do you mean '+r'\unsure{'+q+"|'}from $(*)$"+qq,'misread symbol or index','The opener has two short legs joined at a pointed apex. Two joined quotation strokes are favoured; a single bent stroke cannot be securely excluded. The closing pair is clear.','12','medium')
edit('formulae-ending','p356 cancelled sentence first word',r'\unsure{Formulae|Formulæ}','Formulae','misread word','The ending shows a low a body with its return followed by a separately shaped e. Their joins are crossed by the cancellation, but the two letter bodies remain distinguishable.','13','medium')
edit('formula-reference-B','p356 cancelled second reference',r'(\unsure{B|3})','(B)','misread symbol or index','The glyph has a continuous upright left stem with two closed right bowls. Those surviving strokes decide capital B rather than an open-left 3.','13')
edit('page-357','Page reference p357',r'p\unsure{357}','p357','misread symbol or index','The last digit retains a short rightward top and a downward stroke; the pale vertical paper feature interrupts its middle but does not erase the characteristic 7 contour.','15','medium')
edit('f-star','p357 cancelled expression superscript',r'f^{\unsure{*|+}}','f^{*}','misread symbol or index','The raised mark has a central crossing plus separate short oblique upper branches. These are narrower than the broad cancellation and support an asterisk rather than a simple plus.','16','medium')
edit('been-opener','p358 l.9 opening quotation',"l.9 'been wasting my time"+qq,'l.9 '+r'\unsure{'+q+"|'}been wasting my time"+qq,'misread symbol or index','The opening group has two downward legs joined by a dark top bridge. A joined pair is favoured; the connecting ink prevents a secure stroke count.','17','medium')
edit('commutes-opener','p358 continuation l-4 opener',"l-4 'commutes with"+qq,'l-4 '+q+'commutes with'+qq,'misread symbol or index','A dark upright and a separate small high point form two spatially distinct opening quotation marks.','18','medium')
edit('commutes-point','p358 continuation, above first m of commutes','l-4 '+q+'commutes with'+qq,'l-4 '+q+commword+' with'+qq,'omission','A distinct small dark point lies above the first m, well to the right of the quotation group. It is preserved as an isolated mark with no assigned textual function.','18','medium',report_c='commutes',report_r=commword)
edit('page-359','Page reference p359',r'p\unsure{359}','p359','misread symbol or index','The surviving last numeral has an upper rounded bowl and a right-hand descending tail below it. Fading at the vertical paper feature interrupts the closure but the 9 contour is readable.','19','medium')
edit('360-reference-marks','p360 around l-17','p360 l-17','p360 '+refmarks,'omission','Four separate dark points are visible: two stacked above the l, a third lower and just to its right, and a smaller fourth above the 1. Their geometry is recorded without calling them a colon or abbreviation point.','20','high',report_c='l-17',report_r=refmarks)
edit('360-opening-point','p360 beneath opening quote before than',q+r'\unsure{than|then} looking'+qq,openpoint+r'\unsure{than|then} looking'+qq,'omission','The two opening quotation strokes stand above a distinct small low point. That point is retained once, with no assigned punctuation role.','21','medium',report_c=q,report_r=openpoint)
edit('361-opener','p361 l16 opening quotation',"p361 l16 'didn't"+qq,'p361 l16 '+r'\unsure{'+q+"|'}didn't"+qq,'misread symbol or index','The opening mark has two upper branches with a fused lower portion. A joined pair is favoured but a single branched tick is not excluded.','22','low')
edit('362-opener','p362 l.7 opening quotation',"p362 l.7 'interpret"+qq,'p362 l.7 '+r'\unsure{'+"'|"+q+r'}interpret'+qq,'misread symbol or index','One long upright with a shorter right branch is visible. It may be a single bent quotation tick or two fused strokes.','23','low')
edit('right-margin-dots','Right margin beside p363/p365','p363 l-8 '+q+"shouldn't"+qq,'p363 l-8 '+q+"shouldn't"+qq+'\n'+rightdots,'omission','Two separate dark points lie outside the right pale vertical feature, the upper point slightly farther right. They have no connector and are preserved as two points only, without naming an intentional sign.','31','high',report_c='',report_r=rightdots)
edit('369-opener','p369 l.4 opening quotation',"p369 l.4, 'suggests that one views"+qq,'p369 l.4, '+r'\unsure{'+q+"|'}suggests that one views"+qq,'misread symbol or index','The high opener has a long curved left limb and a shorter right limb joining it near the bottom. A fused pair is favoured but stroke count is not fully decided.','25','low')
reading=reading.replace('% archive sheet number: 28','% The two long pale vertical features are treated as paper creases, not drawn ink rules.\n% Isolated dark marks are reproduced geometrically without assigning their origin.\n% archive sheet number: 28 (upper right)')
(out/'reading.tex').write_text(reading)
# Every C uncertainty and page-specific interpretative alternative is recorded.
c_doubts=[]
def doubt(place,c,r,resolved,conf,evidence,crop=None,source=None,bbox=None):
 if crop:
  loc=loci[crop]; source=loc['source'];bbox=loc['bbox'];cp=loc['output']
 else: cp=None
 c_doubts.append({'place':place,'c':c,'reading':r,'resolved':resolved,'confidence':conf,'evidence':evidence,'crop':cp,'source':source,'bbox':bbox})
a=freeze['sequence'][1]['view'];b=freeze['sequence'][2]['view']
doubt('p339 cancelled glyph',r'\deleted{\unsure{\&|l}}',r'\deleted{\unsure{\&|l}}',False,'low','Crossing strokes clearly cancel the whole small glyph. A low loop and tail favour ampersand, but the superimposed upper loops prevent exclusion of looped l.','03')
doubt('p350 independent initial underline',r'\unsure{\uuline{i}|\uline{i}}',r'\unsure{\uuline{i}|\uline{i}}',False,'medium','Several returned pen passes sit below the i; the upper and lower dark levels touch through a dense return. Double underline and retracing of a single underline remain distinguishable interpretations, not resolved by the available strokes.','08')
doubt('p351 older a/o',r'\unsure{a|o}',r'\unsure{a|o}',False,'low','Only the older oval and an oblique internal remnant can be separated from the live a. No securely independent old tail decides a versus o. Overlapping placement is corrected separately.','09')
doubt('p356 Formulae ending',r'\unsure{Formulae|Formulæ}','Formulae',True,'medium','Separate a and e bodies remain visible across the cancellation; no ligature glyph needs to be posited.','13')
doubt('p356 second formula reference',r'\unsure{B|3}','B',True,'high','A vertical left stem joins both closed bowls. This is affirmative evidence for B, independent of the preceding (2).','13')
doubt('p357 page number',r'\unsure{357}','357',True,'medium','The last numeral retains its 7 top and descent across fading; adjacent page numbers are not used to supply the reading.','15')
doubt('p357 raised f mark',r'f^{\unsure{*|+}}','f^{*}',True,'medium','Small oblique branches survive above the main crossing and are independent of the broad zigzag cancellation.','16')
doubt('p357 argument letter',r'\unsure{\beta|g|S}',r'\unsure{\beta|g|S}',False,'low','Two right-hand rounded portions and a downward stroke favour beta. The scribble crosses the left junctions, so g and S cannot be excluded from surviving ink.','16')
doubt('p357 low argument index',r'\unsure{M|m}',r'\unsure{M|m}',False,'low','Two low humps are visible, but their left entry and the case-defining height are masked by the cancellation.','16')
doubt('p357 relation',r'\unsure{=|-}',r'\unsure{=|-}',False,'low','A short lower horizontal and a nearly parallel segment may be two equality strokes; one may instead belong to a returned deletion line.','16')
doubt('p357 rightmost mark',r'\unsure{s|?}',r'\unsure{s|?}',False,'low','A small curved body and a separate point below survive at the right. The overwritten upper area prevents a secure choice between s and question mark.','16')
doubt('p359 page number',r'\unsure{359}','359',True,'medium','The upper rounded bowl and lower right tail decide the last digit as 9 despite a faded gap along the paper feature.','19')
doubt('p360 than/then',r'\unsure{than|then}',r'\unsure{than|then}',False,'medium','The middle vowel is a very compact closed loop joined into the following n. The crop does not securely distinguish cursive a from e; the quoted fragment supplies no decisive context.','21')
doubt('Bottom-right cancelled word',r'\deleted{\unsure{end|ed}}',r'\deleted{\unsure{end|ed}}',False,'low','The left e-like loop and final tall d are distinguishable. Faint intervening strokes permit n but do not require it. The diagonal cancels the small word; some lowest traces meet the physical image edge.','26')
doubt('p355 asterisk in parentheses','$(*)$','$(*)$',True,'high','Three crossing directions form six projecting arms at the centre of the parentheses; this independently confirms the asterisk.','12')
doubt('p341 underline got me',r'\uline{got me}',r'\uline{got me}',True,'high','A single continuous low rule begins under g and extends through me, ending before back.',source=a,bbox=[635,415,890,490])
doubt('p351 quotation edges',q+r'in\deleted{\unsure{a|o}}adequacies'+'\'',q+'in'+overlap+'dequacies'+'\'',True,'high','The opening pair has two separate high components. Only one terminal high tick follows the word. The old/live a placement is separately reported; quotation counts are confirmed.','09')
doubt('p353 quotation opener from context',q+'its'+qq,r'\unsure{'+q+"|'}its"+qq,False,'low','The context calls the opener a joined pair; the current crop shows joined tips and an enclosed narrow slot but does not securely determine original stroke count.','10')
doubt('p338 manuscript question and qualification','l-8 ? '+q+'and even'+qq+' perhaps.','l-8 ? '+q+'and even'+qq+' perhaps',True,'high','The question mark, quoted proposal, and perhaps are visible and retained. Only the final period is rejected; no answer to the manuscript question is inferred.',source=a,bbox=[530,210,1160,290])
doubt('p341 manuscript better qualification','is perhaps better.','is perhaps better'+r'\unsure{,|.}',False,'medium','The qualification is certain; the low terminal mark remains comma/period. This is a reading decision, not resolution of the author\'s stylistic proposal.','04')
doubt('p350 reservation concerning from','('+q+'from'+qq+' can also be used but is less usual.)','('+q+'from'+qq+' can also be used but is less usual.)',True,'high','Both the permissive alternative and less usual reservation are present across the physical line break, with period before the closing parenthesis.',source=a,bbox=[330,795,1575,925])
doubt('p355 do you mean question','do you mean '+q+'from $(*)$'+qq,'do you mean '+r'\unsure{'+q+"|'}from $(*)$"+qq,False,'medium','The words do you mean and the parenthesized asterisk are readable; the opening quote remains a stroke-count doubt. There is no terminal question mark to add.','12')
doubt('p356 indistinct-copy qualification','(indistinct in my copy)','(indistinct in my copy)',True,'high','The parenthesis and all words are plainly visible after the quoted isn\'t. The manuscript\'s statement of indistinctness is preserved.',source=b,bbox=[415,270,790,340])
remaining=[]
def remain(place,r,alternatives,conf,reason):remaining.append({'place':place,'reading':r,'alternatives':alternatives,'confidence':conf,'reason':reason})
for d in c_doubts:
 if not d['resolved']:
  remain(d['place'],d['reading'],d['reading'],'low' if d['confidence']=='low' else 'medium',d['evidence'])
for c in changes:
 if c['id'] in ['doesnt-opener','also-short-word','been-opener','361-opener','362-opener','369-opener']:
  remain(c['place'],c['reading'],c['reading'],c['confidence'],c['evidence'])
# Inventory covers each list block and all nested page-state/graphic elements.
inventory=[]
def inv(element,kind,position,first,hand='another unnamed hand'):
 inventory.append({'sheet_kind':'list','hand':hand,'element':element,'kind':kind,'position':position,'first_words_or_objects':first,'transcribed':'yes'})
items=[
('01','text','top line','p335 l.7.'),('02','drawing','raised above-left of p335','isolated irregular dark mark; origin unassigned'),
('03','text','second line','p.336 l.-8'),('04','drawing','upper right margin, near p336','short faint vertical trace; origin unassigned'),
('05','text','third line','p.338 l12'),('06','text','fourth line','p.339 l-12'),('07','deletion','after shouldnt on p339 entry','cancelled ampersand/l'),
('08','text','fifth line','340 l.18'),('09','text','p341 long line','p341 l.2 and alongside'),('10','text','nested underline in p341','got me, single underline'),
('11','text','342 line','342 l13'),('12','text','first 344 line','344 l.17 commutes with'),('13','text','344 continuation line','l.23 commutes with'),
('14','text','345 line','p.345 l.5'),('15','drawing','nested after again on p345','closing parenthesis with joined horizontal bar'),
('16','text','348 line','p.348 l-2'),('17','text','350 two-line entry','p350 l.14 its'),('18','text','nested below initial i at p350 l-10','returned underline passes'),
('19','text','351 line','p351 l12'),('20','deletion','inside inadequacies, first a position','older a/o under live a'),('21','text','same glyph space as old a/o','overwritten live a'),
('22','text','352 line','p.352 l8'),('23','text','353 line','p353 l.9'),('24','text','last full entry above date','p354 l8'),
('25','text','above divider, near centre-right','Sent 6/2/84'),('26','drawing','between two p354 entries','long slightly wavering horizontal divider'),
('27','text','first entry below divider','p354 l.-10'),('28','text','next entry','p.355 l.-4'),
('29','text','p356 two-line entry','p356 l1 isnt (indistinct in my copy)'),
('30','deletion','p356 right-hand end of first physical line','Formulae (2) and (B)'),('31','deletion','p356 continuation at left','are unreadable. Are they'),
('32','text','p357 line','p357 l.1 weve got'),('33','deletion','p357 middle of entry','(2) f with raised asterisk and obscured argument/relation'),
('34','text','p358 first line','p358 l.1. didnt'),('35','text','p358 continuation','l-4 commutes with'),('36','drawing','above first m of p358 continuation','one isolated point'),
('37','text','p359 line','p359 l16 its'),('38','text','p360 line','p360 l-17 than/then looking'),('39','drawing','above and right of p360 l-17','four separated points'),('40','drawing','below opening quote of p360 than/then','one separated point'),
('41','text','p361 line','p361 l16 didnt'),('42','text','p362 line','p362 l.7 interpret'),('43','text','p363 line','p363 l-8 shouldnt'),
('44','drawing','right margin beside p363/p365','two isolated points, upper farther right'),
('45','text','p365 line','p365 l.4 its'),('46','text','p367 line','p367 l-13, its'),('47','text','p369 line','p369 l.4, suggests that one views'),
('48','text','penultimate line','p370 l6 its'),('49','text','last full line','p371 l14 its'),('50','margin note','bottom-right, below foot of last line','end/ed'),('51','deletion','nested bottom-right margin note','whole small end/ed cluster cancelled')]
for row in items:inv(*row)
for r in inventory:
 if r['kind']=='drawing' and r['element']!='26':r['hand']='unassigned origin; distinct dark trace'
notes=[
'Handwritten English correction list covering cited typescript pages 335 through 371. There is no title, own pagination or stated page count on this sheet; 28 at the upper right is the archive sheet number.',
'The first set ends with p354 l8. Sent 6/2/84 is written above a long horizontal divider; a second set then starts with another p354 entry.',
'At p338 l-8 the author writes a question mark, proposes and even, and adds perhaps. At p341 l.2 the proposal and alongside got me back is qualified by is perhaps better; only got me is underlined.',
'At p350 l-10 the independent of proposal is followed by the explicit reservation that from can also be used but is less usual.',
'At p355 l-3 the author asks do you mean from (*) without adding a terminal question mark. At p356 the contraction isnt is qualified by indistinct in my copy.',
'The p356 sentence Formulae (2) and (B) are unreadable. Are they is cancelled, and a heavily cancelled mathematical expression follows on the p357 line. Its uncertain argument, low index, relation and last mark are retained as reading alternatives.',
'The last entry is p371, including in which I was working and wasnt. A small cancelled end/ed cluster lies at the bottom-right edge; its lowest traces touch the physical image boundary.'
]
notation=[
{'sign':'(*)','location':'p355 l-3','reading':'$(*)$','evidence':'Crop12 shows three crossing directions and six arms within round parentheses.'},
{'sign':'B','location':'p356 cancelled second formula reference','reading':'$(B)$','evidence':'Crop13: left vertical stem and two closed right bowls; ordinary capital alphabet.'},
{'sign':'f superscript star','location':'p357 cancelled expression','reading':'f^{*}','evidence':'Crop16: central crossing plus independent short diagonal upper branches.'},
{'sign':'cancelled argument and index','location':'p357 cancelled expression','reading':r'(\unsure{\beta|g|S}_{\unsure{M|m}})','evidence':'Crop16: two rounded right portions with a descent; two low humps. Crossings prevent further resolution.'},
{'sign':'cancelled relation and terminal mark','location':'p357 cancelled expression','reading':r'\unsure{=|-}\unsure{s|?}','evidence':'Crop16: a short lower horizontal and a parallel segment, followed by a small curved body and separate point.'},
{'sign':'underline','location':'p341 got me; p350 initial i','reading':r'\uline{got me}; \unsure{\uuline{i}|\uline{i}}','evidence':'Upper half clearly limits one line to got me. Crop08 shows touching returned underline passes beneath i.'},
{'sign':'overlap','location':'p351 inadequacies','reading':'in'+overlap+'dequacies','evidence':'Crop09: older oval and current a share one space; older a/o remains doubtful.'},
{'sign':'quotation counts','location':'p341, p353, p355, p358, p361, p362, p369','reading':'Local alternatives are marked at each occurrence in reading.tex.','evidence':'Crops04,10,12,17,18,22,23,25 judged independently. Clear pairs elsewhere were not made doubtful by analogy.'},
{'sign':'single terminal tick','location':'p351 inadequacies','reading':q+'in'+overlap+'dequacies'+'\'','evidence':'Crop09 independently shows two opening components and one terminal component.'},
{'sign':'l.-8','location':'342 second line reference','reading':'l.-8','evidence':'Crop05: separate low abbreviation point before minus.'},
{'sign':'joined parenthesis bar','location':'p345 after again','reading':'(again'+paren,'evidence':'Crop06: horizontal short stroke physically joins the closing parenthesis; no separate period.'}
]
report={
'scan':29,'reader':'B','model':'GPT-6 Astra Pro','effort':'not exposed',
'viewed':[x['view'] for x in freeze['sequence']],
'layout':'One portrait sheet, entirely in one main unnamed handwriting, containing two sequential blocks of English correction-list entries. A handwritten date sits just above a long wavy horizontal separator. Archive number 28 is in the upper-right corner in a paler hand. The page has two long pale vertical creases, near x211 and x1491 in the whole image, running from the upper region nearly to the foot; their broad grey/white paired appearance and local fading of crossing writing support a material explanation, so they are not redrawn as ink. The black/brown mark above-left of the first line is preserved only by its dark geometry; origin remains unassigned. Small isolated right-margin and interlinear points are separately inventoried. There are several cancellations and an overwritten a but no securely evidenced caret insertion, no diagram, no separate mathematical display and no letterhead. The bottom-right cancelled cluster touches the image edge.',
'changes':changes,'c_doubts':c_doubts,'remaining_doubts':remaining,'inventory':inventory,'notes':notes,'math_checks':[],
'notation':notation,
'abbreviations':[{'form':'p / p.','expansion':'page (interpretation only)','place':'page references throughout'},{'form':'l / l.','expansion':'line (interpretation only)','place':'line references throughout'},{'form':'&','expansion':'and (interpretation only)','place':'p341 l7 and possibly cancelled p339 glyph'}],
'brief_feedback':'Whole image viewed once, then each supplied half once. Thirty-one local candidates were frozen before crop generation; each logged enhanced crop was viewed once. No OCR, recognition, compilation, external research, other-page image or other-reader output was used. H is description-only, so all H fields are null and no H comparison changes are asserted. The nomenclature his hand cannot be established from this page alone; the main list is recorded as another unnamed hand. All fourteen explicit C uncertainty macros have decisions. Page-specific context qualifications and quotation/underline alternatives are also recorded. The full inventory has one row for each list block and nested deletion, overwrite, underline and discrete mark group. No actual mathematical proof, computation or substantive verification was possible from this editorial list, hence math_checks is empty. The pale vertical features are a material-interpretation decision supported by crops27/28, not an inferred intentional rule.'
}
(out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
(out/'audit/literal_diff.txt').write_text(''.join(difflib.unified_diff(C.splitlines(True),reading.splitlines(True),fromfile='C.tex',tofile='B/reading.tex')))
# Record crops actually displayed, not merely generated.
inspection={'view_sequence':freeze['sequence'],'cropping_rule':'one crop per frozen unresolved place','viewed_crops':[{'id':r['id'],'path':r['output'],'count':1} for r in freeze['unresolved_loci']], 'material_decisions':[{'crop':'27','decision':'left long pale feature treated as paper crease, not ink; endpoints observed in whole/halves, not extrapolated from crop'},{'crop':'28','decision':'right long pale feature treated as paper crease, not ink; endpoints observed in whole/halves, not extrapolated from crop'}], 'confirmed_extra_loci':[{'crop':'11','decision':'C l.-10 confirmed by visible low point beneath the minus'},{'crop':'14','decision':'C are unreadable. Are they and full-phrase deletion retained'},{'crop':'24','decision':'C double quote opener of p367 its confirmed by separate limbs'},{'crop':'29','decision':'C p358 without abbreviation point confirmed; low dark portions belong to p and 3'}]}
(out/'audit/inspection.json').write_text(json.dumps(inspection,ensure_ascii=False,indent=2)+'\n')
# Static structural checks only; this does not compile TeX.
level=0
for ln in reading.splitlines():
 ln=ln.split('%',1)[0]
 for m in re.finditer(r'(?<!\\)[{}]',ln):
  level+=1 if m.group()=='{' else -1
  assert level>=0,'negative brace level'
assert level==0,level
assert reading.count('\\scanpage{29}')==1
assert all(c['h'] is None and c['diff_h'] is False for c in changes)
assert all(c['crop'] and Path(root/c['crop']).exists() for c in changes)
assert all(d['crop'] or (d['source'] and d['bbox']) for d in c_doubts)
assert len({r['element'] for r in inventory})==len(inventory)
assert len(inspection['viewed_crops'])==31
stats={'changes':len(changes),'diff_c':len(changes),'diff_h':0,'c_doubt_decisions':len(c_doubts),'c_doubt_resolved':sum(d['resolved'] for d in c_doubts),'remaining_doubt_rows':len(remaining),'inventory':len(inventory),'crops_generated_and_viewed':31,'math_checks':0,'static_braces_balanced':True,'compiled':False}
(out/'audit/static_check.json').write_text(json.dumps(stats,indent=2)+'\n')
print(json.dumps(stats,indent=2))
