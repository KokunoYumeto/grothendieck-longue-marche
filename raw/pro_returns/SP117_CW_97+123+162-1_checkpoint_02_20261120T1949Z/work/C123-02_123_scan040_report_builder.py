from pathlib import Path
import json
root=Path('/workspace/scratch/d27bd2a88bca')
page='C123-02_123_scan040'
packet=root/'packets'/page
out=root/'out/work'
c=(packet/'C.tex').read_text()
d=c
layers=r'ind\unsure{\deleted{c}u|u}\unsure{\deleted{u}c|c}tive\unsure{\deleted{s}s|s}'
assert d.count('limites inductives)')==1
d=d.replace('limites inductives)','limites '+layers+')',1)
assert d.count('(telles les structures de groupe')==1
d=d.replace('(telles les structures de groupe',r'(telles les str\deleted{i}uctures de groupe',1)
assert d.count(r'\deleted{2}\handwritten{3}.1.3.')==1
d=d.replace(r'\deleted{2}\handwritten{3}.1.3.',r'\deleted{2}\handwritten{3}.1.\handwritten{3}.',1)
(out/f'{page}_draft.tex').write_text(d)
m=json.loads((out/f'{page}_crop_manifest.json').read_text())
mb={x['id']:x for x in m}
# Exact connected body blocks; the handwritten additions are separately inventoried.
starts=['sent en termes','Quant au foncteur','à droite i.e.',r'\deleted{2}', 'compréhension de la', 'morphisme de topos']
ends=[r'\inserted{\handwritten{De plus', 'à droite i.e.',r'\inserted{\handwritten{Par suite', 'compréhension de la', 'morphisme de topos', None]
blocks=[]
for a,b in zip(starts,ends):
 x=d.index(a)
 y=d.index(b,x) if b else len(d)
 blocks.append(d[x:y].strip())
# First two large body crops begin/end in the middle of normal lines. They are evidence for the connected omissions,
# with the neighboring crop supplying the small continuation. The prose is kept whole in the report.
changes=[]
def change(ident,line,cv,hv,final,bid,shows,kind='other',conf='high',cc=False,ch=True,marked=False,cons=False,support=()):
 z=dict(id=ident,line=line,c=cv,h=hv,final=final,scan_shows=shows,crop=mb[bid]['crop'],box=mb[bid]['box'],confidence=conf,kind=kind,changed_C=cc,changed_H=ch,marked_in_H=marked,consequential=cons,certainty_only=False)
 if support:
  z['supporting_crops']=[mb[k]['crop'] for k in support]
  z['supporting_boxes']=[mb[k]['box'] for k in support]
 changes.append(z)
# The omissions are recorded as connected stretches, not as hundreds of artificial token rows.
for i,(line,bid,btxt,extra) in enumerate(zip(['L01–L03 opening','L03–L08','L09–L14','L15–L19','L20–L24','L24–L27'],['b36','b37','b38','b39','b40','b41'],blocks,[['b44'],['b11','b12','b13','b14','b15','b43'],['b16','b17','b18'],['b19','b20','b21','b22','b23','b24'],['b25','b26','b27'],['b27','b28','b29','b30']]),1):
 # Use the original C text as the comparison field where the candidate contains a new local layer reading.
 cv=btxt.replace(layers,'inductives').replace(r'str\deleted{i}uctures','structures').replace(r'\deleted{2}\handwritten{3}.1.\handwritten{3}.',r'\deleted{2}\handwritten{3}.1.3.')
 change(f'r{i:02}',line,cv,'Not transcribed as source text; H supplies only an editorial synopsis and selected mentions.',btxt,bid,'The typed source passage is present. H’s introductory synopsis is not a literal transcription and omits this connected wording, including its source punctuation and corrections. Specific newly proposed C changes are separately recorded below.','omission',support=extra,cons=True)
change('r07','top note, first line','fonctorielles','fonctionnelles','fonctorielles','b03','The middle sequence has c–t–o–r–i; no n-n sequence is present after the t. The full word is fonctorielles.','misread word')
change('r08','top note, first/second lines',r'fonctorielles \deleted{\illegible{1}} habituelles ... qui \inserted{peuvent}',r'fonctionnelles habituelles ... qui \struck{\ill{}} peuvent',r'fonctorielles \deleted{\illegible{1}} habituelles ... qui \inserted{peuvent}','b03','The heavily canceled word lies immediately after fonctorielles. The separate peuvent is above the second line after qui. No complete reading of the canceled word survives; H places the cancellation at the wrong point.','insertion or placement',marked=True,support=['b05'])
change('r09','top note, second line',r"s'exprime\deleted{nt}\unsure{r}","s'exprimer",r"s'exprime\deleted{nt}\unsure{r}",'b05','The original final nt is heavily canceled/retouched; the replacement r remains uncertain. H prints only a clean infinitive. The inserted peuvent does not by itself settle the final pen strokes.','deletion state (struck given live or live given struck)',conf='low')
change('r10','insertion after L03',r"``\uline{commute}''",'« commute »',r"``\uline{commute}''",'b09','The handwritten word has two short quotation strokes at each end and a distinct underline. The ink contains no guillemets.','other')
change('r11','left margin instruction','à la ligne après : Quant au...','à la ligne, puis : Quant au …','à la ligne après : Quant au...','b10','The second-line word has a p descender followed by r, accented è and final s; it reads après. There is no comma after ligne. The existing saved crop is rotated clockwise 15 degrees for reading.','misread word')
change('r12','L04',"``respecte''",'« respecte »',"``respecte''",'b12','The typed delimiters are paired upright strokes. H’s mention uses guillemets; the source form is retained.','other')
change('r13','L07',r'\deleted{dans}\inserted{parmi}','parmi replaces an unnamed mot biffé',r'\deleted{dans}\inserted{parmi}','b14','All four underlying letters d-a-n-s survive the machine x cancellation; parmi is typed above them.','omission')
change('r14','handwritten continuation after L14',r"\deleted{transforme pas}\inserted{s'étend pas}","s'étend pas above an unnamed mot biffé",r"\deleted{transforme pas}\inserted{s'étend pas}",'b18','The canceled lower wording is transforme pas, in the same pen line as Par suite, il ne; the live s’étend pas is written above it.','omission',conf='medium')
change('r15','L15 and insertion above it',r"\deleted{se donne}\inserted{est \inserted{\handwritten{en}} présenced'}",r"Par suite, il ne s'étend pas, en général, en présence d'",r"\deleted{se donne}\inserted{est \inserted{\handwritten{en}} présenced'}",'b19','Typed est présenced’ with pen en is linked to the deleted se donne in section 3.1.3. H incorrectly appends en présence d’ to the preceding pen sentence. The absence of a machine space before d’ is preserved.','insertion or placement',cons=True,support=['b18','b39'])
change('r16','bottom note, opening','en un foncteur','ou un foncteur','en un foncteur','b31','The first word has the open entry-loop of e followed by n. The later ou forms in this note have a different, closed o and u; the ink reads en un.','misread word',support=['b32'])
change('r17','bottom note, before quoted module libre',r'\deleted{\unsure{le|de}}','nothing',r'\deleted{\unsure{le|de}}','b34','A short word is visibly canceled before the opening quotes. A loop and short upright survive, but le/de cannot be decided. H omits the canceled word.','omission',conf='low',support=['b33'])
change('r18','bottom note',"``module libre engendré''",'« module libre engendré »',"``module libre engendré''",'b34','Both delimiters are pairs of short pen strokes, not guillemets. The closing pair is crowded by the descender from the line above.','other')
change('r19','bottom note, end of first line','groupe, et','groupe et','groupe, et','b32','A distinct low comma follows groupe before the continuation et on the next line.','other',support=['b33'])
change('r20','L06','structures','not transcribed',r'str\deleted{i}uctures','b43','A separate i dot and narrow stem remain under the first u. The dot cannot belong to the live u or to the adjacent r/c. The readable replaced i is now preserved.','deletion state (struck given live or live given struck)',cc=True)
change('r21','L03','inductives','not transcribed',layers,'b44','The adjacent u/c cells each contain superposed contours, and the final s has a composite impression. The proposed c→u, u→c and repeated-s layers remain local alternatives to plain live letters; no clean correction sequence is asserted.','deletion state (struck given live or live given struck)',conf='low',cc=True)
change('r22','own page number',r'\mspage{\handwritten{23}}','not transcribed',r'\mspage{\handwritten{23}}','b02','A handwritten 23 is present at the upper right. It is distinct from the inverted archive foliation 39 at upper left.','omission')
change('r23','top continuation and its call', 'two loop-at-bottom linking marks and the open top-note frame retained in TikZ','editorial description of a frame and link, without a transcription of their shapes','C’s two loop-at-bottom linking marks and top-note frame retained in TikZ','b09','The call after toutes and the matching mark before les opérations have long stems ending in loops below. The top note has a left/bottom boundary with a small step; these graphic source marks are retained.','drawing or diagram',support=['b03','b08'])
change('r24','before Quant au','opposed pen brackets','editorial paragraph instruction only','opposed pen brackets','b11','The source has a closing bracket to the left and an opening bracket around the start of Quant au. They are distinct from the typed close and the extra close-shaped pen curve.','drawing or diagram',support=['b10'])
change('r25','lower continuation and its call','two loop-at-top linking marks and lower-note upper boundary retained in TikZ','editorial note call description only','C’s two loop-at-top linking marks and lower-note upper boundary retained in TikZ','b18','The mark after en général and the bottom note’s matching mark have loops at the top, unlike the top note’s pair. The bottom note is separated by a long pen rule with a raised left step.','drawing or diagram',support=['b31','b41'])
change('r26','L24','two open formula frames and the curved mark at est un retained in TikZ','formulas summarized without their graphic marks','C’s two open formula frames and curved est un mark retained in TikZ','b27','Separate open-bottom frames surround f=u* and u:F→E; a two-branched curve touches the beginning of est un. The mathematical arrow has an ordinary right head.','drawing or diagram')

# Every remaining uncertain reading stays in place or is described as uncertainty of a physical role/layer.
doubts=[
 dict(line='top note after fonctorielles',reading=r'\deleted{\illegible{1}}',alternatives=['trial expresses','trial explicites'],confidence='low',reason='Dense crossing strokes leave no complete letter sequence. The trials are diagnostic only, not supplied as source words.'),
 dict(line='top note ending s’emploie? / actual s’exprime',reading=r"s'exprime\deleted{nt}\unsure{r}",alternatives=['replacement r not securely separable from the cancellation'],confidence='low',reason='The final nt is retouched. The inserted peuvent favors an infinitive grammatically but does not make r readable. The source word before the ending is s’exprime; no s’emploie reading is proposed.'),
 dict(line='L03 after inductives',reading=r')\handwritten{)}.',alternatives=['the pen close-shaped curve is part of the insertion boundary rather than sentence punctuation'],confidence='medium',reason='The typed close and a separate long pen curve are both visible; their graphic distinction is preserved without importing an opening parenthesis from another page.'),
 dict(line='L03 word inductives',reading=layers,alternatives=['plain u/c/s letters with overlapping mechanical impressions','unestablished earlier letters in the two adjacent u/c cells or final s'],confidence='low',reason='Superposed contours are visible, but the layer order and the identity of every older glyph are not established. The candidate contains local alternatives rather than a clean correction.'),
 dict(line='L11 after second épimorphisme',reading=r'\handwritten{\unsure{;|,}}',alternatives=[',','overwritten punctuation'],confidence='low',reason='An upper short mark and a lower loop/tail survive; their joining and any older punctuation cannot be securely separated.'),
 dict(line='L11 deleted phrase after c’est d’ailleurs',reading=r'\deleted{\unsure{comme} nous le verrons au}',alternatives=['first word obscured; no other complete reading established'],confidence='medium',reason='Nous le verrons au can be followed letter by letter through the x strokes. Comme is more heavily obscured and remains doubtful.'),
 dict(line='bottom note before module libre',reading=r'\deleted{\unsure{le|de}}',alternatives=['de'],confidence='low',reason='The short cancellation leaves a loop and terminal stroke, without deciding the initial l/d.'),
]
# Remove the diagnostic wording from the line label; retain only the actual source place.
doubts[1]['line']='top note, ending of s’expriment'
doubts[1]['reason']='The final nt is retouched. The inserted peuvent favors an infinitive grammatically but does not make the replacement r readable.'

inv=[]
def inventory(element,kind,hand,pos,first,y):
 inv.append(dict(scan=40,sheet_kind='typescript',hand=hand,element=element,kind=kind,position=pos,first_words_or_objects=first,transcribed='yes',_y=y))
# Marginal material in physical top-to-bottom order, plus each principal typewritten baseline.
inventory('A01','text','separate pencil/pen foliation','upper left, inverted','39; archive comment only',75)
inventory('P01','text','pen','upper right','23; own page number',111)
inventory('M01','insertion','pen','top margin, line 1; continuation of De plus','les opérations fonctorielles [canceled word] habituelles faites en termes de telles structures, plus précisément',36)
inventory('D01','drawing','pen','left and bottom of top note','open frame with a small step along its lower boundary',38)
inventory('D02','drawing','pen','before les opérations','stem with loop at bottom, matching the call after toutes',39)
inventory('X01','deletion','pen cancellation','top-note line 1 after fonctorielles','one unreadable word',35)
inventory('I01','insertion','pen','above top-note line 2 after qui','peuvent',54)
inventory('M02','insertion','pen','top margin, line 2','à toutes les opérations qui peuvent s’exprime[nt canceled, r doubtful] en termes de lim→ et de lim← finies: constructions',70)
inventory('X02','deletion','pen retouch/cancellation','end of s’expriment','nt',73)
inventory('I02','insertion','pen','end of s’exprime after canceled nt','doubtful r',73)
inventory('F01','text','pen','top-note line 2','varinjlim and varprojlim, both arrows below lim',75)
inventory('M03','insertion','pen','top margin, line 3','d’objets libres (groupes ou modules libres, p.ex.) engendrés par un objet, produits',100)
inventory('M04','insertion','pen','top margin, line 4','tensoriels (cf. § 6 plus bas) etc.',126)
line_text=[
'sent en termes de limites projectives finies exclusivement, tandis que',
'les autres notions impliquent implicitement des constructions faisant',
'appel également à des limites inductives)). Quant au foncteur image',
'directe u_* ... qui commute aux limites projectives, il “respecte” ... toute',
'structure algébrique sur un objet (ou une famille d’objets) de E,',
'définissable en termes de limites projectives ... (telles les structures',
'de groupe, d’anneau ou de module sur un anneau, [dans/parmi] les exemples',
'précédents). Par [f/c]contre, le foncteur u_* n[e canceled]’est en général pas exact',
'à droite i.e. il ne commute pas en général aux limites inductives',
'finies, et même ne transforme pas en général épimorphisme en épimorphis-',
'me; (c’est d’ailleurs [comme nous le verrons au canceled] ce défaut d’exactitude',
'du foncteur u_* qui est à la source de ces propriétés cohomologiques,',
'qui seront étudiées (du point de vue de l’algèbre homologique commutati-',
've) dans l’exposé suivant).',
'3.1.3. En pratique, lorsqu’on [se donne/est en présenced’] un foncteur f:E→F d’un',
'U-topos dans un autre, il y a lieu d’en expliciter toutes les propriétés',
'd’exactitude, [y compris et de déterminer s’il admet un foncteur exact canceled]',
'y compris l’existence éventuelle de foncteurs adjoints à gauche ou à',
'droite (cf. la note de bas de page précédente), pour parvenir à une',
'compréhension de la “nature géométrique” de f, [qui canceled] compréhension qui',
'sera généralement un guide indispensable pour [l’ canceled / une inserted] intuition géométrique',
'correcte de la situation. Ainsi, s’il s’avère que f commute aux',
'limites inductives quelconques et aux limites projectives finies, il',
'y a lieu d’écrire f sous la forme f=u*, où u:F→E est un morphis-',
'me de topos, i.e. d’interpréter f comme un foncteur “image inverse”',
'par une ““application continue” de topos. Lorsque f commute aux limi-',
' tes projectives quelconques, donc qu’il admet un adjoint à gauche, [g canceled]'
]
ys=[157,228,299,369,439,509,579,650,720,790,860,931,1001,1072,1142,1213,1284,1355,1426,1497,1568,1639,1710,1781,1852,1923,1994]
for i,(t,y) in enumerate(zip(line_text,ys),1):
 inventory(f'L{i:02}','text','typewriter with separately inventoried pen additions',f'principal body line {i}',t,y)
for args in [
('I03','insertion','pen','above L03 after inductives','De plus, le foncteur u* “commute” à toutes',250),
('D03','drawing','pen','after toutes','stem with loop at bottom, matching top note',258),
('M05','margin note','pen','left margin beside L03/L04','à la ligne après : Quant au...',331),
('D04','drawing','pen','around left-margin instruction','three-sided frame, open on left',329),
('I04','insertion','pen','after typed close following inductives','extra close-shaped curve, role uncertain',298),
('D05','drawing','pen','immediately before Quant au','opposed bracket marks for paragraph break',299),
('I05','insertion','typewriter with pen arrow and leader','above L04 after u_*',': E→E′',333),
('I06','insertion','typewriter with pen leader','above L04 after respecte','par suite',328),
('I07','insertion','pen','L04 under u','subscript star',378),
('I08','insertion','typewriter with pen leader','above L06 after projectives','exclusivement',471),
('X03','deletion','typewriter overstrike','L06, first u cell of structures','i beneath u',507),
('I09','insertion','typewriter','above L07 replacing dans','parmi',557),
('X04','deletion','typewriter x cancellation','L07 before les exemples','dans',578),
('X05','deletion','typewriter overstrike','L08 start of contre','f beneath c',647),
('X06','deletion','typewriter x cancellation','L08 n[e]’est','e',648),
('I10','insertion','pen','L08 under u','subscript star',656),
('X07','deletion','typewriter impressions, state uncertain','L03 inductives','possible c/u, u/c and repeated-s layers, locally doubtful',298),
('I11','insertion','pen','L11 after second épimorphisme','semicolon/comma, uncertain',855),
('X08','deletion','typewriter x cancellation with pen stroke','L11 after c’est d’ailleurs','comme [uncertain] nous le verrons au',862),
('I12','insertion','pen','L12 under u','subscript star',942),
('I13','insertion','pen or pen retouch','L12 before la source','à',930),
('I14','insertion','pen','L14 after suivant','closing parenthesis',1072),
('I15','insertion','pen','after L14','Par suite, il ne [transforme pas canceled / s’étend pas inserted], en général,',1063),
('X09','deletion','pen strike','inside I15','transforme pas',1064),
('I16','insertion','pen','above canceled transforme pas','s’étend pas',1044),
('D06','drawing','pen','after en général','loop at top with descending stem, bottom-note call',1065),
('I17','insertion','typewriter with pen leader','above L15 replacing se donne','est présenced’',1106),
('I18','insertion','pen','above I17 between est and présenced’','en',1089),
('X10','deletion','typewriter x cancellation','L15 after lorsqu’on','se donne',1142),
('X11','deletion','typewriter digit overwritten in pen','L15 section initial','2 beneath 3',1140),
('I19','insertion','pen','L15 section initial','3 replacing 2',1140),
('I20','insertion','pen','L15 last section numeral','final 3 in 3.1.3.',1141),
('I21','insertion','pen','L15 f:E→F','right arrow',1140),
('I22','insertion','pen','above L16 before les propriétés','toutes',1182),
('X12','deletion','typewriter overstrikes','L16 propriétés','t beneath é and é beneath t',1211),
('X13','deletion','typewriter x cancellation','L17 after d’exactitude','y compris et de déterminer s’il admet un foncteur exact',1283),
('X14','deletion','typewriter x cancellation','L20 after de f,','qui',1495),
('I23','insertion','typewriter with pen leader','above L21 before intuition','une',1530),
('X15','deletion','typewriter and pen cancellation','L21 before intuition','l’',1567),
('I24','insertion','pen','L24 f=u*','superscript star',1764),
('I25','insertion','pen','L24 u:F→E','right arrow',1777),
('D07','drawing','pen','L24 around f=u*,','open-bottom formula frame with outward feet',1780),
('D08','drawing','pen','L24 around u:F→E','separate open-bottom frame',1780),
('D09','drawing','pen','L24 at est un','two-branched curved enclosure/mark',1780),
('X16','deletion','typewriter x cancellation','L27 after gauche,','g',1994),
('D10','drawing','pen','above bottom note','long boundary with raised left step',2020),
('D11','drawing','pen','before bottom-note en','loop at top with descending stem',2060),
('M06','insertion','pen','bottom margin, line 1','en un foncteur sur des objets du type comodule, ou bigèbre, ou torseur sous un groupe,',2066),
('M07','insertion','pen','bottom margin, line 2','et ne commute pas en général à des opérations telles que [canceled le/de] “module libre engendré”, produit',2098),
('X17','deletion','pen cancellation','bottom line 2 before quoted module','le/de, uncertain',2098),
('M08','insertion','pen','bottom margin, line 3','tensoriel de modules, etc.',2119),
]: inventory(*args)
inv.sort(key=lambda z:z['_y'])
for z in inv: del z['_y']

# Full target readings for every neutral evidence box; larger boxes document H’s connected omissions.
readings={
'b01':r'% archive sheet number: 39 (inverted)',
'b02':r'\handwritten{23}',
'b03':r'\handwritten{[loop-at-bottom link] les opérations fonctorielles \deleted{\illegible{1}} habituelles}',
'b04':r'\handwritten{faites en termes de telles structures, plus précisément}',
'b05':r"\handwritten{à toutes les opérations qui \inserted{peuvent} s'exprime\deleted{nt}\unsure{r}}",
'b06':r'\handwritten{en termes de $\varinjlim$ et de $\varprojlim$ finies: constructions}',
'b07':r"\handwritten{d'objets libres (groupes ou modules libres, p.ex.) engendrés par un objet, produits}",
'b08':r'\handwritten{tensoriels (cf. \S 6 plus bas) etc. [lower frame with step]}',
'b09':r"\inserted{\handwritten{De plus, le foncteur $u^{*}$ ``\uline{commute}'' à toutes [loop-at-bottom link]}}",
'b10':r'\margin{\handwritten{à la ligne après : Quant au... [three-sided frame, open left]}}',
'b11':r"...es)\handwritten{)}. \handwritten{[opposed paragraph brackets]} Quant au",
'b12':r"directe $\mathrm{u}_{\handwritten{*}}$\inserted{$:\mathrm{E}\handwritten{\longrightarrow}\mathrm{E}'$}, qui commute aux limites projectives, il ``respecte'' \inserted{par suite} toute",
'b13':r'projectives \inserted{exclusivement} (telles les',
'b14':r'\deleted{dans}\inserted{parmi} les',
'b15':r"\deleted{f}contre, le foncteur $\mathrm{u}_{\handwritten{*}}$ n\deleted{e}'est en",
'b16':r"me\handwritten{\unsure{;|,}} (c'est d'ailleurs \deleted{\unsure{comme} nous le verrons au}",
'b17':r'$\mathrm{u}_{\handwritten{*}}$ qui est \handwritten{à} la',
'b18':r"...nt\handwritten{)}. \inserted{\handwritten{Par suite, il ne \deleted{transforme pas}\inserted{s'étend pas}, en général, [loop-at-top link]}}",
'b19':r"\deleted{se donne}\inserted{est \inserted{\handwritten{en}} présenced'}un",
'b20':r'\deleted{2}\handwritten{3}.1.\handwritten{3}.',
'b21':r"$\mathrm{f}:\mathrm{E}\handwritten{\longrightarrow}\mathrm{F}$ d'un",
'b22':r'$\underline{\mathrm{U}}$-topos',
'b23':r'\inserted{\handwritten{toutes}} les propri\deleted{t}é\deleted{é}tés',
'b24':r"\deleted{y compris et de déterminer s'il admet un foncteur exact}",
'b25':r"``nature géométrique'' de $\mathrm f$, \deleted{qui}",
'b26':r"pour \deleted{l'}\inserted{une}intuition",
'b27':r'$\mathrm{f}=\mathrm{u}^{\handwritten{*}}$, [open frame] où $\mathrm{u}:\mathrm{F}\handwritten{\longrightarrow}\mathrm{E}$ [separate open frame] est un [two-branched curved mark]',
'b28':r"``image inverse''",
'b29':r"````application continue''",
'b30':r'gauche,\deleted{$\mathrm{g}$}',
'b31':r'\handwritten{[loop-at-top link] en un foncteur sur des objets du type comodule,}',
'b32':r'\handwritten{ou bigèbre, ou torseur sous un groupe,}',
'b33':r'\handwritten{et ne commute pas en général à des opérations telles que \deleted{\unsure{le|de}}}',
'b34':r"\handwritten{\deleted{\unsure{le|de}} ``module libre engendré'', produit}",
'b35':r'\handwritten{tensoriel de modules, etc.}',
'b36':blocks[0], 'b37':blocks[1], 'b38':blocks[2], 'b39':blocks[3], 'b40':blocks[4], 'b41':blocks[5],
'b42':'implicitement', 'b43':r'str\deleted{i}uctures', 'b44':layers,
}
kinds={k:'text' for k in readings}
for k in ['b03','b05','b14','b15','b16','b19','b20','b23','b24','b25','b26','b30','b34','b43','b44']: kinds[k]='deletion'
for k in ['b04','b06','b07','b08','b09','b12','b13','b17','b18','b21','b31','b32','b33','b35']: kinds[k]='insertion'
kinds['b10']='margin note'; kinds['b11']='drawing'; kinds['b27']='drawing'
boxes=[]
for z in m:
 x0,y0,x1,y1=z['box']
 boxes.append(dict(box=z['id'],kind=kinds[z['id']],x0=x0,y0=y0,x1=x1,y1=y1,reading=readings[z['id']]))
# Replace prose placeholders for graphic marks with the actual candidate TikZ shapes in box readings.
loop_bottom=r'\tikz[baseline=-0.3ex,scale=.18]{\draw (0,1.3)--(0,.15) .. controls (-.4,-.2) and (.4,-.2) .. (0,.15);}'
loop_top=r'\tikz[baseline=-.3ex,scale=.18]{\draw (0,0)--(.05,1.3) .. controls (-.35,1.65) and (.45,1.65) .. (.05,1.3);}'
opp=r'\tikz[baseline=-.6ex,scale=.18]{\draw (0,1.5)--(.5,1.4)--(.6,0)--(0,-.15);\draw (1.4,1.4)--(.9,1.35)--(.9,-.1)--(1.5,-.15);}'
for z in boxes:
 z['reading']=z['reading'].replace('[loop-at-bottom link]',loop_bottom).replace('[loop-at-top link]',loop_top).replace('[opposed paragraph brackets]',opp)
# Exact graphic-rich snippets from C/candidate rather than invented descriptions.
left_start=d.index(r'\margin{\handwritten{\figure{')
left_end=d.index('\n%',left_start)
next(x for x in boxes if x['box']=='b10')['reading']=d[left_start:left_end]
frame_start=d.index(r'\begin{tikzpicture}[baseline=(n.base)]')
frame_end=d.index('\nmorphisme de topos',frame_start)
next(x for x in boxes if x['box']=='b27')['reading']=d[frame_start:frame_end]
# The two envelope boxes allow the later blind reader to audit the full graphic boundary and attachment.
fig1_start=d.index(r'\figure{\begin{tikzpicture}')
fig1_end=d.index(r'\end{tikzpicture}}}}',fig1_start)+len(r'\end{tikzpicture}}}}')
fig2_start=d.index(r'\figure{\begin{tikzpicture}',fig1_end)
fig2_end=d.index(r'\end{tikzpicture}}}}',fig2_start)+len(r'\end{tikzpicture}}}}')
boxes.append(dict(box='b45',kind='drawing',x0=236,y0=13,x1=1669,y1=147,reading=d[fig1_start:fig1_end],second_box_only=True))
boxes.append(dict(box='b46',kind='drawing',x0=23,y0=2007,x1=1668,y1=2135,reading=d[fig2_start:fig2_end],second_box_only=True))
# b08's complete boundary is supplied by b45; there is no prose drawing substitution in the candidate.
next(x for x in boxes if x['box']=='b08')['reading']=r'\handwritten{tensoriels (cf. \S 6 plus bas) etc.}'
report=dict(
 page=page,line_count=27,changes=changes,doubts=doubts,inventory=inv,
 notes=[
  'Only this page packet, shared ERRORS/CONVENTIONS and PREAMBLE were used. Whole page viewed once for layout; both halves viewed once against C and H. All 44 saved evidence crops were displayed and inspected. No OCR, recognition library, web lookup or TeX compilation was used.',
  'H contains mainly transcriptions of selected handwritten additions and a synopsis of the typescript. Its synopsis, attribution and cross-page references are editorial; they were not imported as source text. The omitted typed wording is recorded in six connected blocks, with crops b36–b41 and targeted correction crops as supporting evidence.',
  'The word and its placement were decided separately: fonctorielles is clear; the unreadable canceled word follows it, not qui. Peuvent is above the following line; nt is canceled at the end of s’expriment and the replacement r remains doubtful.',
  'The top loop-at-bottom markers join De plus ... à toutes to the upper continuation. The lower loop-at-top markers join Par suite ... en général to the bottom note beginning en un. They are graphic calls, not letters. The marginal instruction reads après, not puis.',
  'Typed est présenced’ and pen en belong above section 3.1.3 and replace se donne. H’s attachment of en présence d’ to the preceding pen sentence is rejected from the visible leader and baseline. The source’s missing machine space before d’ is retained.',
  'Every deletion was audited: top unreadable word; nt; original i in structures; possible overlapping layers in inductives; dans; f in contre; e in n[e]’est; comme nous le verrons au; transforme pas; se donne; section 2; two cells in propriétés; y compris et de déterminer s’il admet un foncteur exact; qui; l’; final g; and bottom le/de. Uncertain older glyphs remain uncertain.',
  'Crop b42 shows adjacent e/m crowded together in implicitement, but no independently identifiable replaced glyph. The word remains plain implicitement; no speculative old layer is inserted. In b44 the u/c cells and final s are composite; local layer alternatives remain explicit. In b43 the i dot and narrow stem under the first u are independently visible.',
  'The first section numeral is a typed 2 changed by pen to 3, and the final 3 is also handwritten. The added wrapper around the final 3 is hand attribution only, not a new content-change row. The own page number 23 and archive foliation 39 are distinct; the latter stays comment-only.',
  'The close-shaped pen curve after inductives may be sentence punctuation or part of the insertion boundary. Both the typed close and the separate pen curve are retained, without supplying an opening parenthesis from another sheet. The source’s ces, omitted articles before épimorphisme, and two opening quote pairs before application continue are preserved.',
  'No mathematical inconsistency was used to force a reading. No local calculation or proof was performed. The source assertions carried in reading_notes receive only the exact background label in check_events; visual checking is separately recorded.',
  'Original coordinates refer to the 1684×2141 source. All evidence crops are LANCZOS upscaled to about 2500 pixels across and autocontrasted/sharpened. The inverted archive numeral was rotated 180 degrees, and the margin instruction 15 degrees clockwise. B35’s final box was expanded upward once before completion to include its ascenders. B45 and b46 are full-envelope second-reading boxes, not extra duplicate first-reading crops.'
 ],
 reading_notes=[
  'The sheet has its own handwritten page number 23 and begins section 3.1.3, with the first numeral changed from 2 to 3. There is no date, title sheet or total page count. Inverted 39 is archival foliation. The opening sent is a continuation fragment, and the final typed sentence ends after a canceled g without completion on this sheet.',
  'The upper addition says that the inverse-image functor u* commutes with customary functorial operations expressible in terms of the displayed inductive and finite projective limits. Its examples include free groups/modules, tensor products and a reference to § 6. The canceled word after fonctorielles is unreadable and the infinitive ending remains doubtful.',
  'The main paragraph says that direct image u_* preserves structures definable solely through projective limits, but is generally not right exact and need not take an epimorphism to an epimorphism. It links this lack of exactness with cohomological properties to be studied in the following exposé. These are source assertions carried without proof here.',
  'The lower addition says that u_* generally does not extend to objects such as comodules, bialgebras or torsors under a group, and does not generally commute with forming a free module or a tensor product. Its opening is en un foncteur. The short canceled word before module libre remains le/de.',
  'Section 3.1.3 advises recording a functor’s exactness properties and possible adjoints to understand its geometric nature. If f preserves arbitrary inductive limits and finite projective limits, the source writes f=u* for a morphism of topoi u:F→E. The next sentence starts from preservation of arbitrary projective limits and asserts the existence of a left adjoint, but continues beyond the sheet.',
  'The source qualifications en général, exclusivement, finies and quelconques are retained in their respective places. The word ces, the absence of articles before épimorphisme, the crowded typed présenced’, doubled opening quotation pair and canceled final g are transcription facts, not mathematical repairs or inferred completions.'
 ],
 check_events=[dict(statement_id='040-source-functorial-exactness-and-adjoints',type='carried as background without fault found',outcome='Background only: the source claims about u* and functorial constructions, u_* and projective-limit structures/non-right-exactness, the lower-note failures of extension/commutation, and the geometric/adjoint interpretation of f are carried in reading_notes. No calculation or proof was performed, and this label is not a verification of those assertions. Source slips and uncertain ink are excluded from the asserted background claims.')],
 visual_audit_events=[
  dict(statement_id='040-layout-and-lines',type='used and rechecked in this run',outcome='Visual transcription check only: whole once and both halves once against C/H; 27 principal typewritten baselines and all marginal/interlinear material inventoried.'),
  dict(statement_id='040-cancellations-and-insertions',type='used and rechecked in this run',outcome='Visual transcription check only: every canceled/inserted span inspected on saved crops; typewriter layers and leaders retained. No mathematical proof check is claimed.'),
  dict(statement_id='040-symbols-and-numbers',type='used and rechecked in this run',outcome='Visual transcription check only: all five functor stars, all three map arrows, both limit arrows, underlined U, page/section/archive numerals and the two pairs of link symbols inspected.'),
  dict(statement_id='040-late-crowded-type',type='used and rechecked in this run',outcome='Visual transcription check only: new crops b42–b44 examined after crowded impressions were noticed. Implicitement remains plain; structures retains its replaced i; inductives keeps local layer uncertainty.')
 ],
 notation=[
  '123/040: In U-topos the U is a single typewritten upright capital with a separate underline. H’s synopsis uses mathcal U, but the candidate retains the keyed form. The E/F capitals and f/u letters in all three map/formula sites are ordinary machine letters, without a demonstrated double strike.',
  '123/040: All five functor stars are pen: superscript u* in the upper insertion; the three subscripts on direct-image u_* in the body; and the superscript in f=u*. Their positions are preserved.',
  '123/040: The three map arrows (:E→E′, f:E→F, u:F→E) are hand-added ordinary right arrows. The top-note varinjlim and varprojlim have respectively right- and left-pointing arrows below lim.',
  '123/040: The two upper linking signs have loops at the bottom of their stems; the two lower signs have loops at the top. Reproduce them as graphic calls, not as letters, and preserve the two note boundaries and local formula frames.',
  '123/040: Quotes are paired pen strokes around commute and module libre engendré and paired machine strokes around respecte, nature géométrique and image inverse. Application continue has two opening pairs and one closing pair. No guillemets are drawn.',
  '123/040: Keep cf., p.ex., i.e., § 6, finies/quelconques, and the visible crowded présenced’ construction. Do not expand abbreviations or normalize the underlying typed slips.'
 ],
 hand_log=[
  'Scope is scan040 only. All 44 evidence crops, the full page and both halves were inspected. Every visible handwritten text span, numeral, mathematical addition and cancellation has an inventory entry and neutral second-reading box. No hand identity is inferred from H’s editorial attribution or another sheet.',
  'Fonctorielles at top note/b03 has a c–t–o–r–i sequence. This is the sole handwritten occurrence of this word on the sheet; H’s fonctionnelles is rejected. Other handwritten foncteur occurrences in b09 and b31 have the same joined ct construction, and were inspected without extending the spelling decision beyond this sheet.',
  'En at the lower note’s start/b31 has an open e entry-loop followed by n, contrasting with the closed o in both ou occurrences at b32. The pen en above présenced’ at b19 was also inspected. H’s initial ou un and the misplacement of en présence d’ are corrected; C’s readings/attachments stand.',
  'Après in the margin/b10 has a p descender, r, accented è and final s. It is the sole occurrence of that instruction. C’s après is retained against H’s puis. The saved crop is upright after 15-degree clockwise rotation.',
  'All five star additions were checked individually: b09 (upper u*), b12/b15/b17 (three body u_*), and b27 (f=u*). C/H symbolic values agree; C’s hand wrappers and the differing super/subscript positions are retained. All three ordinary map arrows are also pen and checked in b12/b21/b27; both limit arrows are checked in b06.',
  'All penned numerals are covered: archive 39/b01, own page 23/b02, § 6/b08, new first 3 and final 3 in the section number/b20. The old first numeral 2 is typed and overwritten. C’s content agrees, but the candidate adds a handwritten wrapper to the final 3. H does not transcribe the own page number or the old 2.',
  'All six quoted spans were inspected at b09, b12, b25, b28, b29 and b34. Paired strokes, including the doubled opening before application continue, are preserved. H uses guillemets for the three spans it mentions/transcribes (commute, respecte, module libre engendré); the other source spans fall in its omitted typescript.',
  'All mixed-layer sites were inspected. The i dot/stem beneath u in structures/b43 is new against C; the crowded e/m in implicitement/b42 does not establish a replaced glyph. Inductives/b44 retains uncertainty on the two u/c cells and composite final s. The existing visible f/c, n[e]’est and t/é–é/t layers in propriétés are kept from C, without silently regularizing them.',
  'All retained uncertain canceled readings were checked on their own saved spans: top unreadable word/b03, final r after canceled nt/b05, comme and punctuation/b16, lower le/de/b34. The pen emphasis/cancellation does not make their covered strokes recoverable. C’s doubts remain; H’s cleaner wording is not treated as evidence.',
  'The two pairings of loop-and-stem calls and all boundary marks were inspected: top calls b03/b09, lower calls b18/b31, margin/paragraph marks b10/b11, and formula frames/est un mark b27. Their differing loop positions are consistent within each pair; C’s graphic representations are retained. The reinforced à at b17 is kept without inventing a distinct old letter.'
 ],
 boxes=boxes,
 crop_transforms=[dict(crop=z['crop'],box_id=z['id'],original_box=z['box'],rotation_clockwise_degrees=z['rotation_clockwise_degrees'],resampling='BICUBIC',expanded_canvas=True,fill='white',purpose='upright reading of inverted/slanted source') for z in m if z['rotation_clockwise_degrees']],
 crop_processing=dict(source_size=[1684,2141],width_pixels=2500,resize='LANCZOS',autocontrast_cutoff=.2,sharpen='UnsharpMask radius 1.2 percent 110 threshold 3',displayed_crop_ids=[z['id'] for z in m])
)
# Validate actual evidence links and coordinates, without compilation.
for z in changes:
 assert Path(z['crop']).is_file()
 for p in z.get('supporting_crops',[]): assert Path(p).is_file()
for z in boxes:
 assert 0<=z['x0']<z['x1']<=1684 and 0<=z['y0']<z['y1']<=2141,z
assert len({z['id'] for z in changes})==len(changes)
assert len({z['box'] for z in boxes})==len(boxes)
assert d.count('{')==d.count('}')
assert d.count('$')%2==0
assert all(z['kind'] in ['text','display','diagram','drawing','margin note','insertion','deletion'] for z in inv)
(out/f'{page}_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(page=page,changes=len(changes),doubts=len(doubts),inventory=len(inv),boxes=len(boxes),evidence_crops=len(m),draft=str(out/f'{page}_draft.tex'),report=str(out/f'{page}_report.json')),indent=2))
