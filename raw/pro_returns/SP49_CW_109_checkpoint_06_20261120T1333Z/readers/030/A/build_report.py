import json
from pathlib import Path

ROOT=Path('/workspace/scratch/6d55c8c3e5a7')
OUT=ROOT/'work/readers/030/A'
C=(ROOT/'work/inputs/030/C.tex').read_text()
meta=json.loads((ROOT/'work/inputs/030/metadata.json').read_text())
frozen=json.loads((OUT/'frozen_unresolved.json').read_text())
loc={r['id'][:2]:r for r in frozen['unresolved']}
Q=chr(96)*2
q=chr(96)
changes=[]
reading=C

def where(n):
 r=loc[n]
 return {'crop':str(ROOT/r['crop']),'source':str(ROOT/r['source']),'bbox':r['bbox']}

def change(ident,place,old,new,n,kind,evidence,confidence='high'):
 global reading
 if old not in reading:
  raise ValueError((ident,'old text absent',old))
 if reading.count(old)!=1:
  raise ValueError((ident,'old text not unique',old,reading.count(old)))
 reading=reading.replace(old,new,1)
 changes.append(dict(id=ident,place=place,c=old,h=None,reading=new,diff_c=True,diff_h=False,kind=kind,marked_in_H=False,confidence=confidence,evidence=evidence,**where(n)))

change('030-A-01-ref372','p372, first reference',
       'p 372 l.16','p 372 l 1.6','02','insertion or placement',
       'The small low point is visibly to the right of the upright1 and before6. The interval between the looped l and1 is blank. The transcription preserves the point at its observed position without assigning a numerical interpretation.')
change('030-A-02-word372','p372 l.17, final word',
       r'\unsure{inverse|unverse|universe}',r'\unsure{unverse|inverse|universe}',
       '03','other',
       'The undotted joined initial group most resembles un-, followed by the visible verse-like remainder. The joined minims do not securely distinguish unverse, inverse and universe. The order is changed to put the stroke-based preference first; none is supplied as a correction.','low')
change('030-A-03-p374','p374 page prefix',
       'p 374 l 10','p.374 l 10','06','omission',
       'A separate low gray-dark stop follows the p bowl and precedes the upper detached part of3.')
mark377=r'\tikz[overlay,x=1em,y=1ex]{\fill (7.0,.25) ellipse (.025 and .055);}'
change('030-A-04-mark377','right blank beside p377 entry',
       'p 377 l.-15 '+Q+"its'' \\quad l-7 "+Q+"won't'' \\quad l-3 "+q+"don't''",
       'p 377 l.-15 '+Q+"its'' \\quad l-7 "+Q+"won't'' \\quad l-3 "+q+"don't'' "+mark377,
       '21','drawing or diagram',
       'One distinct upright dark point stands in the blank to the right of the p377 corrections, near x1320,y534 of half_a. Its origin and punctuation function are unassigned; the dot is reproduced geometrically.')
old381=r'l.\deleted{\unsure{8}}\unsure{3|8}'
new381=r'l-\tikz[baseline=(old381A.base)]{\node[inner sep=0pt] (old381A) {\deleted{\unsure{8}}};\node[anchor=base west,inner sep=0pt] at (old381A.base west) {3};}'
change('030-A-05-ref381','p-381 line reference',old381,new381,
       '08','insertion or placement',
       'The low mark after l is a short horizontal dash. The final heavy digit has an open-left double-bowl3 outline over the old closed loops. Live3 is resolved; the old8 remains uncertain. The two forms occupy the same physical glyph space, so they are overlaid rather than printed consecutively.','high')
change('030-A-06-dots385','p385 l6, inside the parenthesis after the second with',
       r'(resp. with\ldots{})',r'(resp. with....)',
       '11','misread symbol or index',
       'Four separately discernible low marks follow with before the closing parenthesis: two close short dabs, then two more separated angular points. The first pair is close but has a pale gap.','medium')
change('030-A-07-ref387','p387 second reference',
       'l-3 '+q+"commuting with''",'l.-3 '+q+"commuting with''",
       '26','omission',
       'A distinct small point lies between the terminal foot of l and the separate horizontal minus stroke.')
change('030-A-08-punc388','p388 end of explanatory clause',
       "to'' is more usual.","to'' is more usual,",
       '25','misread symbol or index',
       'The detached terminal mark has a long oblique descending body and a hooked lower end, extending below the nearby baseline; it is comma-shaped.','medium')
mark394=r'\tikz[overlay,x=1em,y=1ex]{\fill (2.0,1.2) ellipse (.025 and .07);}'
change('030-A-09-mark394','blank after p394 correction',
       'p 394 l-7 '+Q+"commutes with''",
       'p 394 l-7 '+Q+"commutes with'' "+mark394,
       '22','drawing or diagram',
       'An isolated narrow dark point lies well to the right of the closing quote pair, at roughly their lower height and distinctly above the word baseline. It is reproduced without calling it a period.')
mark396=r'\margin{\raisebox{-1.4ex}[0pt][0pt]{\tikz[x=1ex,y=1ex]{\fill (0,0) circle (.045);\fill (.18,.25) circle (.045);}}}'
change('030-A-10-marks396','right margin between p396 and following entry',
       'p 396 l.-4 '+Q+"commute with'' again l-2.",
       'p 396 l.-4 '+Q+"commute with'' again l-2. "+mark396,
       '23','drawing or diagram',
       'Two dark points are separate and diagonally aligned, with the right point higher. They stand near the right edge below the p396 baseline. No line joins them, and no punctuation function is assigned.')
old401=Q+"$(k-M)$''"
q401=r'\unsure{'+Q+'|'+q+'}'
change('030-A-11-quote401','p401 l.-11, opening quotation',
       old401,q401+"$(k-M)$''",'19','misread symbol or index',
       'The high opening cluster is connected and has two short right-facing projections, but its filled left side also permits one retraced curved stroke. The original quote count is not secure; double and single are retained.','low')
formula401=r'\tikz[baseline=(f401A.base)]{\node[inner sep=0pt] (f401A) {$(k-M)$};\fill ([xshift=-.22em,yshift=1.0ex]f401A.base west) circle (.045ex);}'
change('030-A-12-mark401','p401 l.-11, point left of opening parenthesis',
       "$(k-M)$",formula401,'19','drawing or diagram',
       'A separate small dark point lies below and right of the opening quotation cluster, immediately left of the upper part of the opening parenthesis. It is not merged into the quote count and is reproduced geometrically.')
change('030-A-13-corner','lower-left archive numeral, comment only',
       '% archive sheet number: 29\n% The last figure can also be read as 3.',
       '% archive sheet number: 23 (possibly 29)\n% The final figure has an open-left upper turn and a broad lower arc; 9 is not excluded.',
       '20','other',
       'The last figure has an open-left upper turn and a much broader lower arc, visually favoring3. Blur and the nearly closing upper return still permit9. The numeral is kept only in a comment; the sequence on other sheets is not used.','medium')
(OUT/'reading.tex').write_text(reading)

c_doubts=[]
def doubt(place,c,rd,resolved,evidence,n=None,source=None,bbox=None,confidence='high'):
 ev=where(n) if n else {'crop':None,'source':meta[source],'bbox':bbox}
 c_doubts.append(dict(place=place,c=c,reading=rd,resolved=resolved,confidence=confidence,evidence=evidence,**ev))

# Six explicit uncertainty locations, treating the two381 digits independently.
doubt('p372 l.17, final word',r'\unsure{inverse|unverse|universe}',r'\unsure{unverse|inverse|universe}',False,
      'Undotted joined initial minims favor un-; the exact letter segmentation is not secure. All three supplied candidates remain possible.','03',confidence='low')
doubt('p-381, older line digit',r'\deleted{\unsure{8}}',r'\deleted{\unsure{8}}',False,
      'Closed-loop remnants survive beneath the heavy3. They support8 but are not sufficiently independent of the over-writing to resolve the old numeral. Deletion/overwrite state is certain.','08',confidence='low')
doubt('p-381, live line digit',r'\unsure{3|8}','3',True,
      'The heavy final contour has a top bar, two right-hand rounded turns and open left sides. The closed portions belong to the older underlying form.','08')
doubt('p385, opening mark after Formula (7)',r'\unsure{'+Q+'|'+q+'|$+$}',r'\unsure{'+Q+'|'+q+'|$+$}',False,
      'Two compact crossing strokes form a raised cross-like cluster. Fused double quotation, a retraced single quote and a small plus remain possible. The following relation and closing pair are independently clear.','12',confidence='low')
doubt('p387 l-17, cancelled ending after commute',r'\deleted{\unsure{s}}',r'\deleted{\unsure{s}}',False,
      'A small central curved/looped remnant remains, but two oblique cancelling strokes obscure its contour. The s reading is held uncertain; the cancellation extent is secure.','13',confidence='low')
doubt('page reference following396, final digit',r'p.39\unsure{7|1}',r'p.39\unsure{7|1}',False,
      'A short leftward top hook joins a descending stem. This favors7, but a hooked1 is not excluded. No ordering argument from neighboring page numbers is used.','18',confidence='medium')
doubt('archive corner, comment only','29; alternative23','23; alternative29',False,
      'Open-left upper turn and broad lower arc favor3; blur at the upper junction leaves9 possible.','20',confidence='medium')

# Page-specific context decisions.
doubt('context: p371 reference punctuation','p. 371 l.14','p. 371 l.14',True,
      'The low stop after p is present. The marker after the looped l has two touching lobes but is one compact point group; C punctuation is retained.','01')
doubt('context: p372 first line reference','l.16','l 1.6',True,
      'The separate low point sits after1 and before6; none is present in the gap immediately after l.','02')
doubt('context: p372 second line reference','l.17','l.17',True,
      'A separate low point is visible between the looped l and the numeral17.',source='half_a',bbox=[740,121,850,178])
doubt('context: p372 continuation reference','l.21','l.21',True,
      'The low stop between l and21 is distinct.',source='half_a',bbox=[242,182,345,239])
doubt('context: quotations of p372 l.17',Q+"with small \\ldots{} and finite \\unsure{inverse|unverse|universe}''",
      Q+"with small \\ldots{} and finite \\unsure{unverse|inverse|universe}''",True,
      'The opening pair is clear in half_a; crop03 independently shows two distinct closing strokes beyond the final e. The word itself is a separate unresolved doubt.','03')
doubt('context: p383 l-9 closing quotation',"bothering''","bothering''",True,
      'The connected high group has two downward legs, a shorter left leg and a longer right leg; the paired closer is retained.','09')
doubt('context: ellipsis after small, p372 l.17',r'small \ldots{} and',r'small \ldots{} and',True,
      'Three separated low points stand between small and and.',source='half_a',bbox=[1082,138,1215,176])
doubt('context: first ellipsis in p385 l6',r'with \ldots{} (resp.',r'with \ldots{} (resp.',True,
      'Three separate low dots follow the first with and precede the parenthesis.',source='half_b',bbox=[527,156,706,217])
doubt('context: second ellipsis in p385 l6',r'with\ldots{})',r'with....)',True,
      'Four separately discernible low marks occur before the closing parenthesis, the first two close together.','11',confidence='medium')
doubt('context: first101 reference in second p373 block','line 3 of 101','line 3 of 101',True,
      'There is no section mark before this101; the words of and the following numeral are distinct.',source='half_a',bbox=[442,306,738,369])
doubt('context: second101 reference in second p373 block',r'\S101 l.11',r'\S101 l.11',True,
      'Two joined turns give the section sign before101. The point in l.11 is separately visible.',source='half_a',bbox=[1207,301,1389,366])
doubt('context: underline at p379 l1',r'\uuline{with}',r'\uuline{with}',True,
      'Two strong, separate low strokes extend beneath with. The upper stroke attached to the preceding t in to is not an underline.',source='half_a',bbox=[477,621,720,695])
doubt('context: underline at386 l.-11',r'\uline{is}',r'\uline{is}',True,
      'One low returned stroke is confined to is and ends before well.',source='half_b',bbox=[451,295,514,357])
doubt('context: p374 internal punctuation','commutation :.. with','commutation :.. with',True,
      'The group has one upper point and three lower points, matching a colon followed by two periods.',source='half_a',bbox=[616,446,691,490])
doubt('context: p382 typing-slip parenthesis','(typing slip.)','(typing slip.)',True,
      'The words typing slip are readable, with a low stop before the closing parenthesis. No original erroneous form is given.',source='half_a',bbox=[614,940,832,1005])
doubt('context: relation after Formula (7)',r'\cong',r'\cong',True,
      'The symbol has one upper wave and two separate lower horizontal strokes. This is an ink identification only, not a mathematical proof.','12')
doubt('context: p388 cancelled with and quotation state',r'\deleted{with}'+"'' to''",r'\deleted{with}'+"'' to''",True,
      'The crossed word is with. Both high strokes immediately after it stand above and beyond the cancelling paths. The two high strokes after to are also live. No opening quotation before to is visible.','14')
doubt('context: p401 parenthesized expression',r'$(k-M)$',r'$(k-M)$',True,
      'Round parentheses, a lowercase k, one horizontal dash and an ordinary single-contour uppercase M are independently visible.','19')

remaining=[
 {'place':'p372 l.17 final word','reading':r'\unsure{unverse|inverse|universe}','alternatives':'unverse / inverse / universe','confidence':'low','reason':'Joined undotted minims do not decide the initial letter segmentation.'},
 {'place':'p-381 old line digit','reading':r'\deleted{\unsure{8}}','alternatives':'8 held uncertain; no other old numeral is independently readable','confidence':'low','reason':'The live3 covers the old upper and lower joins; overwrite state is secure.'},
 {'place':'p385 opening mark after Formula (7)','reading':r'\unsure{'+Q+'|'+q+'|$+$}','alternatives':'double quote / single quote / raised plus','confidence':'low','reason':'A compact crossed high group permits each interpretation; surrounding quotation practice does not settle it.'},
 {'place':'p387 cancelled ending after commute','reading':r'\deleted{\unsure{s}}','alternatives':'s held uncertain','confidence':'low','reason':'The surviving curve is crossed by oblique cancellation strokes.'},
 {'place':'page reference following396','reading':r'p.39\unsure{7|1}','alternatives':'397 /391','confidence':'medium','reason':'The short hooked top is compatible with7 and a hooked1.'},
 {'place':'p401 l.-11 opener','reading':q401,'alternatives':'paired opener /single opener','confidence':'low','reason':'The cluster is filled and connected, with two short projections but no securely separate strokes.'},
 {'place':'archive corner, comment only','reading':'23 (possibly29)','alternatives':'23 /29','confidence':'medium','reason':'Open-left upper turn favors3, but the blurred upper return may nearly close as9.'},
 {'place':'isolated points at p377, p394, p396 and beside the p401 formula','reading':mark377+' '+mark394+' '+mark396+' '+formula401,'alternatives':'geometric marks retained; physical origin and punctuation role unassigned','confidence':'high','reason':'Positions and separateness are clear, but the image does not establish intentional punctuation or another role.'}
]

inventory=[]
def inv(element,kind,position,first,hand='his hand'):
 inventory.append({'sheet_kind':'list','hand':hand,'element':element,'kind':kind,'position':position,'first_words_or_objects':first,'transcribed':'yes'})
entries=[
('01','top, first row','p.371 l.14 '+Q+"didn't''"),
('02','second row, left correction','p372 l 1.6 '+Q+"commutes with''"),
('03','second row, right correction','l.17 '+Q+'with small'),
('04','third row, left','l.21 '+Q+"commute with''"),
('05','third row, middle','l-12 '+Q+"commute with''"),
('06','third row, right','l-5 '+Q+"its''"),
('07','fourth row','p373 l-13 '+Q+"recommendation''"),
('08','next p.373 block, left start','l2 '+Q+"its''."),
('09','same p.373 block, middle','line 3 of101 '+Q+"no question of dealing''"),
('10','same p.373 block, right and continuation','\\S101 l.11 '+Q+"commuting with''"),
('11','continuation of second p.373 block','l-6 '+Q+"its''"),
('12','next main entry','p.374 l10 '+Q+"commutation :.. with''"),
('13','p377 row, left','l.-15 '+Q+"its''"),
('14','p377 row, middle','l-7 '+Q+"won't''"),
('15','p377 row, right','l-3 '+q+"don't''"),
('16','p378 row, left','l-7 '+Q+"interpret''"),
('17','p378 row, right','l-1 '+Q+"commuting with''"),
('18','p379 row, left','l1 not '+Q+"to'' "+Q+r'\uuline{with}'+"''"),
('19','p379 row, middle','l8 '+Q+"made up of''"),
('20','p379 row, right, no line numeral',''+Q+"commute with''"),
('21','p379 continuation','l.15 '+Q+"insufficient''"),
('22','p380 row','l.15 '+Q+"don't''"),
('23','p-381 row',new381+' '+Q+"commuting with''"),
('24','p382 row, left','l.1 '+Q+"haven't''"),
('25','p382 row, middle','l3 '+Q+"hadn't''"),
('26','p382 row, right','l.5 '+Q+"breathe''"),
('27','p382 continuation, left','l.7 '+q+"covered'' (typing slip.)"),
('28','p382 continuation, right','l14 '+Q+"out to prove''"),
('29','p383 first row, left','l.10 '+Q+"inaccurate''"),
('30','p383 first row, middle','l11 '+Q+"its''"),
('31','p383 first row, next','l-10 '+q+"doesn't''"),
('32','p383 first row right, continued next row','l-9 '+Q+"much sense in bothering''"),
('33','p383 second row, middle','l-8 '+Q+"invaluable''"),
('34','p383 second row right, continued next row','l-3 '+Q+"suggest simply dropping''"),
('35','p384 row','l8 '+Q+"made up of''"),
('36','p385 row, left','l6 '+Q+r'commutes with \ldots{} (resp. with....)'+"''"),
('37','p385 row, right','l-14 '+Q+"symmetrically''"),
('38','separate next row under p385','Formula (7) '+r'\unsure{'+Q+'|'+q+'|$+$}'+r'$\cong$'+"'' missing"),
('39','386 row, left','l.-11 '+Q+r'as \uline{is} well known too'+"''"),
('40','386 row, right','l-6 '+Q+"without''"),
('41','p387 row, left','l-17 '+Q+r'commute\deleted{\unsure{s}} with'+"''"),
('42','p387 row, right','l.-3 '+q+"commuting with''"),
('43','p388 row','l13 '+Q+r'equivalent \deleted{with}'+"'' to'' is more usual,"),
('44','p390 row','l16 '+Q+"interpret''"),
('45','p392 row, left','l8 '+Q+"its''"),
('46','p392 row, right','l-1 '+Q+"afraid''"),
('47','p393 row','l-10 '+Q+"didn't''"),
('48','p394 row','l-7 '+Q+"commutes with''"),
('49','p395 row, left','l1 '+Q+"interpreted as saying'' is more usual."),
('50','p395 row, right','l4 '+Q+"commute with''"),
('51','p395 continuation','l16 '+Q+"interpret''"),
('52','p396 row','l.-4 '+Q+"commute with'' again l-2."),
('53','page39[7|1] row','l-13 '+Q+"its'' also in l-12"),
('54','p399 row, left','l6 '+Q+"commutes with''"),
('55','p399 row, middle','l17 '+Q+"analogue''"),
('56','p399 row, right','l19 '+Q+"its''"),
('57','p400 row','l-8 '+Q+"developed''"),
('58','p401 last row, left','l.7 '+Q+"didn't''."),
('59','p401 last row, right','l.-11 '+q401+formula401+"''")
]
for e,p,t in entries:inv(e,'text',p,t)
inv('60','text','nested in18, under with',r'\uuline{with}')
inv('61','deletion','nested in23, underneath final line-reference digit',r'\deleted{\unsure{8}}')
inv('62','text','nested in23, final digit written over the old form','3')
inv('63','text','nested in39, under is',r'\uline{is}')
inv('64','deletion','nested in41, after commute and before with',r'\deleted{\unsure{s}}')
inv('65','deletion','nested in43, between equivalent and live closing quote pair',r'\deleted{with}')
inv('66','drawing','right blank beside p377, near whole x1320,y534','one dark point')
inv('67','drawing','right of p394 quoted correction, half_b x771,y681','one upright dark point')
inv('68','drawing','right margin below p396, half_b about x1460,y910','two separate diagonal points')
inv('69','drawing','nested in59, below opener and left of opening parenthesis','one small dark point')
inv('70','margin note','lower-left archive corner; comment only','23 (possibly29)','another unnamed hand (archive numeral)')

notation=[
 {'sign':'l and point position','location':'p371; p372; p381; p387','reading':'l.14; l 1.6; l.17; l.21; l-[overwritten3]; l.-3','evidence':'Crops01,02,08,26 and half_a separate looped reference letters, upright1s, dots and short minus strokes. The372 point is physically after1.'},
 {'sign':'quotation strokes','location':'p373 recommendation; p378 commuting; p383 bothering and suggest; p392 its; p395 saying and with','reading':Q+'...'+"''",'evidence':'Crops05,07,09,10,15,16,17 independently show paired legs/strokes. The third high mark before p392 its is the displaced dot of i, not a third quote.'},
 {'sign':'single openers','location':'p377 don\'t; p382 covered; p383 doesn\'t; p387 second commuting','reading':q+'...'+"''",'evidence':'Each local half view shows one high opening stroke at these four places; no uniform quotation pattern is imposed.'},
 {'sign':'section sign','location':'second p373 block, before second101','reading':r'\S101','evidence':'Half_a shows two joined turns. The earlier line3 of101 lacks such a mark.'},
 {'sign':'underlining','location':'p379 with;386 is','reading':r'\uuline{with}; \uline{is}','evidence':'Half_a shows two separated low lines under with; half_b shows one returned stroke confined to is.'},
 {'sign':'dot groups','location':'p372 after small; p374 inside commutation quote; p385 two with occurrences','reading':r'\ldots; :..; \ldots; ....','evidence':'The halves settle three low dots, one high plus three low dots, and three low dots respectively. Crop11 shows four separate low marks in the inner p385 group.'},
 {'sign':r'\cong','location':'p385 Formula (7)','reading':r'\cong','evidence':'Crop12 shows one wave over two straight horizontal bars. This is only an ink reading; H has no running-text transcription to collate.'},
 {'sign':'ordinary letters and delimiters','location':'p401 l.-11','reading':r'$(k-M)$','evidence':'Crop19 shows round brackets, a plain lowercase k, a single dash and ordinary M. No doubled alphabet or index is present.'},
 {'sign':'cancelled word and quote edges','location':'p388','reading':r'\deleted{with}'+"'' to''",'evidence':'Crop14: cancellation paths cross the letters and end below the first pair; both closing pairs are live.'},
 {'sign':'material traces','location':'near x212 and x1490 through page; bottom-right spot','reading':'No text or ink drawing supplied for these material features.','evidence':'Whole/halves and crops03,04,06,17,23 show narrow vertical light/dark bands with local fading and pale flanks. Crop24 shows a diffuse two-core spot with a light rim rather than a coherent pen path.'},
 {'sign':'reference prefix punctuation','location':'first p373 and p374','reading':'p373; p.374','evidence':'Crop04 shows no low stop after p; the detached upper stroke belongs to3. Crop06 separately shows a low gray stop after p.'},
 {'sign':'isolated marks','location':'p377; p394; right margin by p396; before p401 expression','reading':mark377+' '+mark394+' '+mark396+' '+formula401,'evidence':'Crops21,22,23,19 separately locate the dark points. Their geometry is retained; neither a letter nor punctuation role is assigned.'}
]

report={
 'scan':30,'reader':'A','model':'GPT-6 Astra Pro','effort':'not exposed',
 'viewed':[meta['whole'],meta['half_a'],meta['half_b']],
 'layout':'One portrait manuscript sheet, a dense correction list from cited p371 through p401 in one main hand. Page numbers occupy a narrow left column; corrections run in rows to the right, often with several entries across one row and continuations on the next. There is no title, date, signature, formal diagram, or separate mathematical derivation. Three corrected/cancelled loci are visible: an overwritten line-reference digit at381, a cancelled terminal letter at387, and cancelled with at388. With at379 is double underlined; is at386 is singly underlined. Four clusters of isolated dark marks are retained geometrically. A separate archive numeral sits in the lower-left corner in a lighter, different hand. Narrow near-vertical light/dark traces near x212 and x1490 begin around the first rows and continue toward the lower edge, with local fading; their pale flanks and texture are treated as material creases, not ink rules. The diffuse rimmed bottom-right spot is also treated as material. Black photographic borders surround the sheet.',
 'changes':changes,'c_doubts':c_doubts,'remaining_doubts':remaining,'inventory':inventory,
 'notes':[
  'The sheet gives English wording and spelling corrections for cited pages371–401, repeatedly specifying commute/commutes/commuting with and forms of interpret.',
  'At p379 l1 the writer says not "to" and gives double-underlined "with". At386 l.-11 only "is" is underlined.',
  'The p372 l.17 correction ends in a doubtful word after "and finite". The visible connected strokes do not justify completing or modernizing that word.',
  'At p382 l.7, "covered" is labelled "(typing slip.)". The erroneous form in the cited typescript is not given.',
  'The separate Formula (7) note under p385 supplies a wave-over-two-bars relation followed by "missing"; the formula itself is not reproduced.',
  'At p388, "with" is cancelled after "equivalent", and "to" is followed by "is more usual,". The two live closing quote pairs remain in their observed positions.',
  'At p395, "interpreted as saying" is followed by "is more usual."; at p396 the correction is repeated for l-2.',
  'The final cited correction is the parenthesized expression (k-M), with plain handwritten letters. No mathematical assertion is developed sufficiently on this page for a substantive proof check.',
  'The archive corner is read23 first, with29 retained as an alternative, and is recorded in a comment only.'
 ],
 'math_checks':[],
 'notation':notation,
 'abbreviations':[
  {'form':'p; p.','expansion':'page (interpretation only)','place':'left page-reference column throughout'},
  {'form':'l; l.','expansion':'line (interpretation only)','place':'line references throughout'},
  {'form':'resp.','expansion':'respectively (interpretation only)','place':'p385 l6'}
 ],
 'brief_feedback':'Read brief_v14, conventions, preamble, C, H, corrected C_context, C_context_addendum, metadata and notation snapshot. H status is desc, so h is null throughout and there are no H comparison rows. Whole, half_a and half_b were each viewed exactly once. A list of26 unresolved loci was frozen before cropping; each was cropped once through work/scripts/crop.py at width2400 and each resulting crop was actually displayed singly once. All visible body text was compared word by word and sign/state by sign/state. The inventory covers59 separate correction/list entries, nested underline and correction states, four geometric-mark clusters, and the archive corner. The erroneous scan033/031 context rows were disregarded after the supplied correction. No other page images, other reader outputs, OCR, recognition libraries, outside research or compilation were used. Material bands and the bottom-right spot were inspected without turning them automatically into ink drawings. Static checks are recorded separately in static_checks.json.'
}
(OUT/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
viewlog={'whole':{'path':meta['whole'],'count':1},'half_a':{'path':meta['half_a'],'count':1},'half_b':{'path':meta['half_b'],'count':1},'crops':[{'path':str(ROOT/r['crop']),'count':1,'displayed_singly':True} for r in frozen['unresolved']]}
(OUT/'view_log.json').write_text(json.dumps(viewlog,indent=2)+'\n')
print(json.dumps({'changes':len(changes),'c_doubts':len(c_doubts),'remaining_doubts':len(remaining),'inventory':len(inventory),'crops':len(frozen['unresolved'])}))
