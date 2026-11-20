from pathlib import Path
import json,csv,re,difflib
out=Path('work/readers/022/C'); c=Path('work/inputs/022/C.tex').read_text(); reading=c
meta=json.loads(Path('work/inputs/022/metadata.json').read_text()); a=meta['half_a']; b=meta['half_b']; whole=meta['whole']
logs=[json.loads(x) for x in (out/'crops/crops.jsonl').read_text().splitlines()]
cp={Path(x['output']).stem:x for x in logs}
changes=[]
def evidence(crop=None,source=None,bbox=None):
 if crop:
  p=cp[crop]
  return {'crop':str(Path(p['output']).resolve()),'source':str(Path(p['source']).resolve()),'bbox':p['box']}
 return {'crop':None,'source':source,'bbox':bbox}
def ch(id,place,old,new,kind,confidence,why,crop=None,source=None,bbox=None,replace=True):
 global reading
 if old: assert old in c,(id,'not literal C',old)
 if replace:
  assert reading.count(old)==1,(id,reading.count(old),old)
  reading=reading.replace(old,new,1)
 row={'id':id,'place':place,'c':old,'h':None,'reading':new,'diff_c':True,'diff_h':False,'kind':kind,'marked_in_H':False,'confidence':confidence,'evidence':why}
 row.update(evidence(crop,source,bbox));changes.append(row)
ch('C022-01','p.116 line -6, first inclusion',r'\unsure{R|K}_{\unsure{h|n}}\subset R_n',r'\unsure{R|K}_h\subset \unsure{R|K}_n','misread symbol or index','medium','The first subscript has a tall stem and low arch, deciding h. Both capitals have dark K-like strokes with pale upper bowl traces; the second occurrence independently remains R/K and must be marked too. The second subscript is a low n.','01_formula')
ch('C022-02','boundary between p.116 formula and p117 commutation entry',"'' should be $R_h\\subset\\Sigma_h$.\n\np117 line 11 \\& 12, ``commutation"," should be $R_h\\subset\\Sigma_h$.\n\np117 line 11 \\& 12, \\unsure{``}commutation",'insertion or placement','medium','Only one physical pair appears in the gap below/right of the first inclusion and above/left of commutation. C encodes a closer after R_n and another opener before commutation. I preserve one pair, provisionally as the commutation opener; attachment to the first formula remains possible. The final period after Sigma_h is already in C and is unchanged.','01_formula')
margin=r'''\reversemarginpar
\margin{\tikz[baseline=(m122.base)]{
\node[inner sep=0pt](m122){\deleted{? \unsure{*} p122 \unsure{?}}};
\draw ([xshift=-.25em,yshift=.1ex]m122.west) -- ([xshift=.3em,yshift=.45ex]m122.east);
\draw ([xshift=-.3em,yshift=-.4ex]m122.west) -- ([xshift=.05em,yshift=-.15ex]m122.east);
\draw ([xshift=.9em,yshift=-1ex]m122.west) -- ([xshift=-.05em,yshift=-.3ex]m122.east);
}}
\normalmarginpar'''
ch('C022-03','cancelled marginal reference left of p.123',r'\margin{\deleted{\unsure{?} \unsure{*} p122 \unsure{?}}}',margin,'drawing or diagram','medium','The left hook is a question mark; its lower end enters the cancellation. The middle star-like cluster and terminal hooked sign remain uncertain. Several long crossing strokes extend across and beyond the reference; they are drawn in addition to the deletion macro. Standard margin placement commands keep this note on the left.','04_left_cancelled_reference')
ch('C022-04','p132 line -14 opening quotation',"p132 line -14 ``wasn't''","p132 line -14 `wasn't''",'misread symbol or index','high','A single separate upright opening stroke precedes the word; the closing pair and internal apostrophe are distinct.','08_p132_open_quote')
ch('C022-05','p.146 line -1 conjunction',r"doesn't \unsure{or} shouldn't",r"doesn't or shouldn't",'misread word','high','The closed o and short following r with its rightward shoulder are visible independently of the surrounding words.','12_p146_or')
ch('C022-06','147 cancelled fragment before line 2',r'147 \deleted{\unsure{st}} line 2',r'147 \deleted{st} line 2','misread word','medium','The surviving first curved s and final upright crossed t remain readable under the diagonal cancellation. This reading was made on the isolated fragment, without using the later live word.','13_p147_cancelled_start')
ch('C022-07','147 line 20, punctuation and opening quotation',"line 20 ``with' not to''",r"line 20 \unsure{,|.} \unsure{``|`}with' not to''",'omission','medium','A separate low oblique mark precedes with; its small tail favours a comma but a stop remains possible. The high cap-shaped opener may be a fused pair or one curved stroke. The single closer after with and final double closer are clear.','14_p147_line20_quotes')
ch('C022-08','149 line 7, marks before line',r'149. \unsure{``}line 7',r'149. ``line 7','misread symbol or index','high','Two separately visible short upright strokes precede the large loop of line.','16_p149_quote')
ch('C022-09','circled151 continuation, live fragment after cancelled work/write',r'\unsure{in|n} in $(2)$',r'\unsure{n|in} in $(2)$','misread word','low','The surviving uncrossed fragment has a single n-like arch and no separately identifiable i-dot; in cannot be excluded. I reverse the preference without resolving the reading. The next line starts with a separate clear in.','19_p151_marginal_cancellation')
ch('C022-10','p.153 line 4, cancellation scope of handiness',r"\deleted{``handiness''}",r"``\deleted{handiness}''",'deletion state (struck given live or live given struck)','medium','The cancellation zigzags through the word. The opening quotation strokes stand free above/left, and the closing strokes remain at the right edge; they are retained live rather than placed wholly inside the deletion macro.','20_p153_handiness')
ch('C022-11','p.153 line 4, cancelled fragment after handy',r'\deleted{\unsure{n \&}}',r'\deleted{\unsure{n \&|n \& s}}','misread word','low','The old fragment contains a low n-like beginning, a looped crossed cluster, and a final curled/descending part. The last part could belong to the ampersand or a further s; the cancellation obscures segmentation. The candidate is based on these surviving strokes, not copied from the live replacement.','21_p153_n_amp_s')
ch('C022-12','p154 line 9, cancelled fragment and quotation before will',r'\deleted{\unsure{allo}} ``will',r'\deleted{allo} will','text not on the page','high','The old fragment shows a low a, two tall looped l strokes, and a final closed o. The gap before will contains no opening quotation strokes at that line height; the marks clipped at the top of the crop belong to the preceding line. The visible closing pair after handle is retained.','22_p154_cancelled_allo')
ch('C022-13','p154 line -6, cancelled terminal fragment',r'\deleted{\unsure{it}}',r'\deleted{\unsure{to|it}}','misread word','low','The fragment has an ascender with cross-stroke and a rounded final loop, favouring to; the crossing prevents exclusion of the earlier it reading.','23_p154_cancelled_it')
ch('C022-14','p154 line -2, opening and closing quotation marks',"line -2 ``standard''",r"line -2 \unsure{``|`}standard\unsure{''|'}",'misread symbol or index','medium','The opener is a joined loop with a descending leg; the closer is another joined upright/loop. Neither occurrence separates securely into two strokes, so each is marked independently as paired or single.','25_p154_standard_quote')
# Preserve the original running text and its existing arrow/circle drawing; add the otherwise omitted marginal marks.
reading=reading.replace('\\scanpage{22}\n','\\scanpage{22}\n\\tikz[remember picture,overlay]\\coordinate (s022top);\n% One physical quote pair between the first inclusion and commutation; attachment is uncertain.\n',1)
left=r'\draw[thin] ([xshift=.8em,yshift=.8ex]s022top) -- ([xshift=.8em,yshift=-.4ex]s022bottom);'
right=r'\draw[thin] ([xshift=\linewidth,yshift=.9ex]s022top) -- ([xshift=\linewidth,yshift=-.6ex]s022bottom);'
trace=r'\draw[gray,thin] ([xshift=-2.7em,yshift=-.5ex]s022top) .. controls +(.05em,-2em) and +(-.04em,2em) .. ([xshift=-2.75em,yshift=-7.7em]s022top);'
oval=r'\draw[gray,thin] ([xshift=-.7em,yshift=-1.5ex]s022top) ellipse[x radius=.43em,y radius=.62ex];'
tick=r'\draw[thin] ([xshift=.67em,yshift=.1ex]s022bottom) -- ++(.21em,-.2ex) -- ++(-.06em,.3ex);'
marks='\\tikz[remember picture,overlay]\\coordinate (s022bottom);\n% Visible marginal rules and faint traces; the faint oval is not read as a letter.\n\\figure{\\begin{tikzpicture}[remember picture,overlay]\n'+left+'\n'+tick+'\n'+right+'\n'+trace+'\n'+oval+'\n\\end{tikzpicture}}\n\n'
reading=reading.replace('% archive sheet number: 21',marks+'% archive sheet number: 21')
ch('C022-15','long vertical rule through the left reference column and terminal tick','',left+'\n'+tick,'drawing or diagram','high','A fine straight rule runs from near the first reference to the lower margin; a small angular tick crosses its lower end.',source=whole,bbox=[210,87,232,2277],replace=False)
ch('C022-16','long vertical rule at right','',right,'drawing or diagram','high','A second thin rule runs near x1501 from the top of the writing to the lower page; its lower portion is faint.',source=whole,bbox=[1490,83,1512,2305],replace=False)
ch('C022-17','far-left faint vertical trace in upper section','',trace,'drawing or diagram','medium','A narrow, irregular, pale vertical trace is visible farther left than the main reference-column rule. It is preserved without assigning editorial meaning.',source=a,bbox=[37,120,62,649],replace=False)
ch('C022-18','faint oval above/left of p117','',oval,'drawing or diagram','medium','The crop shows a pale broken oval with a darker short segment on its left. It does not support a reliable letter reading; the geometry is reproduced as a faint oval.','24_faint_left_marks',replace=False)
(out/'reading.tex').write_text(reading)
# C doubts and page-specific context confirmations.
doubts=[]
def doubt(place,old,new,resolved,confidence,why,crop=None,source=None,bbox=None):
 assert old in c,(place,'C doubt not literal',old)
 row={'place':place,'c':old,'reading':new,'resolved':resolved,'confidence':confidence,'evidence':why};row.update(evidence(crop,source,bbox));doubts.append(row)
doubt('p.116 first capital',r'\unsure{R|K}',r'\unsure{R|K}',False,'medium','Dark stem/diagonals and faint upper bowl trace still admit R or K.','01_formula')
doubt('p.116 first subscript',r'\unsure{h|n}','h',True,'high','Tall stem and low arch decide h.','01_formula')
doubt('p.116 second capital, C_context alternative',r'R_n',r'\unsure{R|K}_n',False,'medium','The second capital is independently faded at its top; K-like dark strokes and a pale bowl trace both survive.','01_formula')
doubt('p.116 replacement capitals and subscripts',r'R_h\subset\Sigma_h',r'R_h\subset\Sigma_h',True,'high','The replacement R has a closed upper bowl; the final capital has the sigma zigzag profile, and both subscripts have tall h stems.','01_formula')
doubt('p.116 first and replacement inclusion signs',r'\subset',r'\subset',True,'high','Each relation opens to the right with no lower equality stroke.','01_formula')
doubt('p.116/p117 quotation-pair attachment',r"R_n$''",r'\unsure{``}commutation',False,'medium','One pair is visible, positioned below/right of R_n and above/left of commutation. Its association remains uncertain; it is transcribed once.','01_formula')
doubt('p.119 line14 double underline',r'\uuline{one}',r'\uuline{one}',True,'high','Two low horizontal strokes lie under one.',source=a,bbox=[583,350,673,406])
doubt('p114 and115 section references',r'\S52 intended rather than \S51',r'\S52 intended rather than \S51',True,'high','Each number is preceded by a double-curved section sign.',source=a,bbox=[942,393,1545,463])
doubt('left of p.123, first question mark',r'\unsure{?}','?',True,'high','A distinct top hook and descending question-mark stem survive before the crossed reference.','04_left_cancelled_reference')
doubt('left of p.123, star-like sign',r'\unsure{*}',r'\unsure{*}',False,'low','Intersecting strokes are partly cancellation; a star remains the best candidate but is not isolated.','04_left_cancelled_reference')
doubt('left of p.123, terminal question-like sign',r'\unsure{?}',r'\unsure{?}',False,'low','A tall right hook is interwoven with the surrounding cancellation contour.','04_left_cancelled_reference')
doubt('p.123 cancelled initial',r'\deleted{\unsure{l}}',r'\deleted{\unsure{l}}',False,'low','Extra strokes lie beneath/left of the live initial l, but the old letter cannot be isolated.','05_p123_cancelled_initial')
doubt('p128 cancelled line number',r'\deleted{\unsure{16}}',r'\deleted{\unsure{16}}',False,'low','An upright and lower loop survive; upper joining strokes are inseparable from cancellation.','07_p128_cancelled_number')
doubt('133 handwritten parenthesis',r'(handwritten \unsure{?})',r'(handwritten \unsure{?})',False,'low','A small curved raised mark stands beside the parenthesis; the form does not decide an interrogative sign.','09_handwritten_question')
doubt('p140 overwritten digit',r'\deleted{\unsure{3}}4',r'\deleted{\unsure{3}}4',False,'low','The live 4 is clear; two buried right curves permit 3, but the old form is not fully recoverable.','10_p140_old_digit')
doubt('142 line15 equality',r's_1=\delta_0',r's_1=\delta_0',True,'high','The low 1 and 0 are separately placed below s and delta; the relation has two horizontal strokes.',source=b,bbox=[597,185,779,252])
doubt('p.146 cancelled word',r'\deleted{\unsure{does}}',r'\deleted{\unsure{does}}',False,'medium','A tall first ascender, small loops and final curl fit does; the middle crossings prevent a certain reading without borrowing from the live phrase.','11_p146_cancelled_word')
doubt('p.146 conjunction',r'\unsure{or}','or',True,'high','Closed o followed by a short r and rightward shoulder.','12_p146_or')
doubt('147 cancelled fragment',r'\deleted{\unsure{st}}',r'\deleted{st}',True,'medium','The s curves and final crossed t upright remain independently readable.','13_p147_cancelled_start')
doubt('149 opening pair before line',r'\unsure{``}',r'``',True,'high','The enlarged image separates two upright quote strokes.','16_p149_quote')
doubt('p.152 cancelled allow',r'\deleted{\unsure{allow}}',r'\deleted{\unsure{allow}}',False,'medium','The a and two l loops survive; the final segment lies on the cancellation and is not independently secure.','17_p152_cancelled_allow')
doubt('circled151 overwritten ending of whereas',r'\deleted{\unsure{as}}',r'\deleted{\unsure{as}}',False,'low','The crowded old and final strokes at the re/as junction cannot be partitioned securely; even the distinction from retracing remains uncertain. The live whereas is readable.','18_p151_whereas')
doubt('circled151 cancelled initial phrase',r'\deleted{\unsure{If th}}',r'\deleted{\unsure{If th}}',False,'low','An I-like upright and additional tall/looped forms survive under several strokes; the internal letters are not secure.','19_p151_marginal_cancellation')
doubt('circled151 cancelled fragment after target',r'\deleted{\unsure{of}}',r'\deleted{\unsure{of}}',False,'low','A small loop and ascender are covered by several oblique marks.','19_p151_marginal_cancellation')
doubt('circled151 cancelled work/write',r'\unsure{work|write}',r'\unsure{work|write}',False,'low','The beginning and final tall/looped forms survive, but crossings and the preceding line overlap the middle.','19_p151_marginal_cancellation')
doubt('circled151 live fragment after cancellation',r'\unsure{in|n}',r'\unsure{n|in}',False,'low','A single n-like arch is visible, with no clearly separate i; a joined in remains possible.','19_p151_marginal_cancellation')
doubt('circled151 hatted A',r'\widehat{A}',r'\widehat{A}',True,'high','Two roof strokes stand above an ordinary capital A.',source=b,bbox=[550,875,613,939])
doubt('p.153 cancelled fragment',r'\unsure{n \&}',r'\unsure{n \&|n \& s}',False,'low','The final curled/descending portion could be a component of the ampersand or a further s.','21_p153_n_amp_s')
doubt('p.153 final s/S and lower mark',r'\unsure{\uline{s}|S}',r'\unsure{\uline{s}|S}',False,'medium','The small s-shaped body has a short lower stroke and downward tail; the case and interpretation of that lower flourish remain uncertain.','21_p153_n_amp_s')
doubt('p154 cancelled allo',r'\unsure{allo}','allo',True,'high','A, two looped l strokes, and final closed o are visible beneath the diagonal stroke.','22_p154_cancelled_allo')
doubt('p154 cancelled terminal fragment',r'\unsure{it}',r'\unsure{to|it}',False,'low','Ascender/crossbar and rounded final loop favour to but do not securely exclude it.','23_p154_cancelled_it')
# Remaining doubts are occurrence-specific, including the new quotation and punctuation uncertainties.
remaining=[]
for d in doubts:
 if not d['resolved']:
  row={'place':d['place'],'reading':d['reading'],'alternatives':d['reading'],'confidence':d['confidence'],'reason':d['evidence']};row.update({k:d[k] for k in ['crop','source','bbox']});remaining.append(row)
for place,txt,why,key in [
 ('147 line20 low punctuation',r'\unsure{,|.}','Oblique low mark may be a comma or stop.','14_p147_line20_quotes'),
 ('147 line20 opening quote',r'\unsure{``|`}','High cap-shaped mark may be a fused pair or one stroke.','14_p147_line20_quotes'),
 ('p154 line-2 opening quote',r'\unsure{``|`}','Joined loop and long lower leg do not separate a pair securely.','25_p154_standard_quote'),
 ('p154 line-2 closing quote',r"\unsure{''|'}",'Joined upright and lower loop do not separate a pair securely.','25_p154_standard_quote')]:
  row={'place':place,'reading':txt,'alternatives':txt,'confidence':'medium','reason':why};row.update(evidence(key));remaining.append(row)
# Full element inventory, one row for every correction reference, nested editorial state and nontext mark.
inv=[]
def item(kind,position,text,hand='another unnamed hand (correction-list hand)'):
 inv.append({'sheet_kind':'list','hand':hand,'element':f'{len(inv)+1:02}','kind':kind,'position':position,'first_words_or_objects':text,'transcribed':'yes'})
entries=[
('top row','p.116 line -6; first inclusion should be replacement inclusion'),('row 2','p117 line 11 & 12; commutation .... with.'),('row 3','line -17; I\'d better assume ...'),('row 4','p.119 line 5; onto'),('row 5','line 14; allows one to'),('row 6','p114 & 115 handwritten comment: is §52 intended rather than §51.'),('row 7','p.121 line -17; endows'),('row 8','p.123 line 9; standard'),('row 9 left','line 13; with direct sums'),('row 9 right','line -1; commutes with'),('row 10','p.124 line 17; a long time ago'),('row 11','p128 line -12; standard'),('row 12 left','p131 line 16; commutes with'),('row 12 right','line 18; it is'),('row 13','p132 line -14; wasn\'t'),('row 14','133 line 13 (handwritten ?); commutes with'),('row 15','p.135 line 4; commas needed around ,of course,'),('row 16','137 line -13; wasn\'t'),('row 17 left','138 line -15; through'),('row 17 right','line -5; standard'),('row 18','p140 line 4; commutes with'),('row 19','141 line -1; standard'),('row 20 left','142 line 15; s_1=delta_0'),('row 20 right','line -15; allow one to'),('row 21 left','p.146 line -3; usual'),('row 21 right','line -1; doesn\'t or shouldn\'t'),('row 22 left','147 line 2; standard'),('row 22 middle','line 10; commutes with'),('row 22 right','line 18; doesn\'t'),('row 23','line 20; with not to'),('row 24 left','148 line 21; developed'),('row 24 right','line -1.; standard.'),('row 25 left','149. line 7; standard'),('row 25 right','line 12; isn\'t'),('row 26 left','p.151 line 8; isn\'t'),('row 26 middle','line 17; a long time ago'),('row 26 right and continuation below','line 18; putting off would be more usual.'),('row 28 left','p.152 line 17; developed'),('row 28 middle','line -10.; lead to develop'),('row 28 right and row 29','line -9; which will allow us to define'),('row 30 and31','circled151 line -4; whereas in the target category (Cat) of (2); the target ... in (2) is hatted A.'),('row 32','p.153 line 4; developed; handiness; handy n & s would be better'),('row 33','p154 line 9; will even allow us to handle'),('row 34 left','line -9; don\'t'),('row 34 right','line -6; wouldn\'t'),('bottom text row','line -2; standard')]
for x,y in entries:item('text',x,y)
item('insertion','p.119 line5, enclosed left of onto','not "unto"')
item('drawing','p.119 line5, surrounding insertion and curving to right of onto','rounded enclosure and curved rightward/upward arrow')
item('text','p.119 line14, beneath one','double underline under one')
item('margin note','left of p.123','? * p122 ?')
item('deletion','left of p.123, nested marginal reference','whole marginal reference and multiple crossing strokes')
item('deletion','p.123 before live line','uncertain l')
item('deletion','p128 before -12','uncertain 16')
item('deletion','p140 overwritten by live4','uncertain 3')
item('deletion','p.146 between usual and line-1','uncertain does')
item('deletion','147 before line2','st')
item('deletion','p.152 line-9','uncertain allow')
item('drawing','left of lower151 reference','circle around151')
item('drawing','from upper p.151 reference curving to lower circled151','curved downward arrow')
item('deletion','circled151, within whereas','uncertain earlier as; state/segmentation unresolved')
item('deletion','circled151 right continuation, before the target','uncertain If th')
item('deletion','circled151 right continuation, after the target','uncertain of')
item('deletion','circled151 right continuation, lower line','we\'ll work/write; following n/in remains live')
item('deletion','p.153 line4, within live quotation strokes','handiness')
item('deletion','p.153 line4, after handy','uncertain n & / n & s')
item('text','p.153 live final s/S','uncertain underline/lower flourish')
item('deletion','p154 line9 before will','allo')
item('deletion','p154 line-6 after wouldn\'t','uncertain to/it')
item('drawing','through left reference column from top to bottom','thin vertical rule and terminal angular tick','hand not independently attributable')
item('drawing','near right margin','thin vertical rule','hand not independently attributable')
item('drawing','far left upper section','faint irregular vertical trace','hand not independently attributable')
item('drawing','above/left of p117','faint broken oval','hand not independently attributable')
notes=[
 'English handwritten correction list referring to pages 114–154 of a separate typescript; the references are the subject text\'s pages, not pagination of this correction sheet.',
 'At p.116 line -6, an inclusion is corrected to R_h subset Sigma_h. The first pair of capitals remains R/K. The ink confirms the terminal period already present in C.',
 'At p114 &115 the writer asks whether §52 is intended rather than §51; the sentence visibly ends with a period.',
 'The p.119 suggestion distinguishes onto from unto in an enclosed insertion with an arrow, and the following one is doubly underlined.',
 'The p.151 line18 suggestion says putting off would be more usual. A separate circled151 entry, reached by a curved arrow, revisits the target category (Cat) of (2), with several cancellations, and states that the target in (2) is hatted A.',
 'At p.153, handiness is cancelled and handy n & s/S is proposed with would be better. The small final sign and the preceding cancelled fragment remain uncertain.',
 'No title, date, author signature, stated page count or independent sheet pagination appears. The lower-left archive number21 is preserved only as a TeX comment.',
 'No substantive mathematical proof, computation or refutation was possible from this page alone: its formulas are corrections to an absent source. Visual symbol verification is not recorded as a mathematical check.'
]
notation=[
 {'sign':r'\unsure{R|K}_h\subset\unsure{R|K}_n','location':'p.116 first inclusion','reading':'Both capitals remain separately uncertain; first subscript h, second n.','evidence':'Crop01: faded upper portions of each capital; first subscript has a tall stem.'},
 {'sign':r'R_h\subset\Sigma_h','location':'p.116 replacement inclusion','reading':r'R_h\subset\Sigma_h','evidence':'Crop01: clear R bowl, sigma zigzag and two tall h stems; no equality under either inclusion.'},
 {'sign':'single physical quotation pair','location':'between first inclusion and commutation','reading':r'\unsure{``}commutation','evidence':'Crops01–02 show one pair, with uncertain attachment; no second pair is added.'},
 {'sign':r'\S52;\S51','location':'p114 &115','reading':'section signs','evidence':'Half a: two curved lobes precede each number.'},
 {'sign':r's_1=\delta_0','location':'142 line15','reading':r's_1=\delta_0','evidence':'Half b: low1 after s and low0 after delta; two relation strokes.'},
 {'sign':r'\widehat{A}','location':'circled151 line-4 continuation','reading':r'\widehat{A}','evidence':'Half b: separate two-stroke roof above A.'},
 {'sign':r'\uuline{one}','location':'p.119 line14','reading':'double underline','evidence':'Half a: two horizontal low strokes.'},
 {'sign':r'\unsure{\uline{s}|S}','location':'p.153 last live sign','reading':'small s-shaped sign, lower flourish, case unresolved','evidence':'Crop21: short low stroke joins a downward tail; case remains uncertain.'},
 {'sign':'single/double quotation strokes','location':'p132; p140;149;p154','reading':r"p132 single opener; p140 paired;149 paired;p154 final entry independently uncertain opener and closer",'evidence':'Crops08,26,16,25 respectively; the p140 second mark is a small detached dark point.'}
]
report={'scan':22,'reader':'C','model':'GPT-6 Astra Pro','effort':'not exposed','viewed':[whole,a,b],
 'layout':'One handwritten correction-list sheet in another unnamed hand. Short page/line references run down a left reference area; several entries continue at the right or on the next line. At p119 an enclosed insertion has a long curved arrow. A crossed marginal p122 reference stands left of p123. Numerous small cancellations occur within references and wording. The lower circled151 note is reached by a curved arrow from the earlier p151 entry and has a crowded right continuation. Two long vertical rules, a faint far-left trace, a faint upper-left oval and a small terminal tick are reproduced. The archive corner number21 is only a comment. No displayed commutative diagram, title, date or new text hand is visible.',
 'changes':changes,'c_doubts':doubts,'remaining_doubts':remaining,'inventory':inv,'notes':notes,'math_checks':[],
 'notation':notation,'abbreviations':[{'form':'p. / p','expansion':'page (tentative interpretation only)','place':'reference labels throughout'},{'form':'Cat','expansion':'category/category notation; no expansion supplied by this page','place':'circled151 target-category quotation'}],
 'brief_feedback':'The single first/second-row quotation pair has uncertain attachment and appears duplicated in C. C\'s terminal period after Sigma_h was initially overlooked in working notes, then checked literally and excluded from changes. Several crossed forms remain genuinely unresolved; deletion extent is distinguished from recovery of letters. All26 logged crops were displayed once. A final quote check at p140 was added during literal comparison; it did not repeat any previously cropped locus. No OCR, web, other page/reader output, subagent or LaTeX compilation was used.'}
(out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
with (out/'inventory.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed'],delimiter='\t');w.writeheader();w.writerows(inv)
(out/'notes.md').write_text('# Scan 022 — independent reader C\n\n'+'\n\n'.join(notes)+'\n\n## Coverage and limits\n\nThe whole image and each supplied half were displayed exactly once. Every running-text word, punctuation mark, formula, reference, deletion, insertion and independent drawing was compared with literal C. H is descriptive only, so no H collation rows are manufactured. The inventory includes every correction reference and nested editorial state. The grey marginal traces are preserved as geometry without identifying their origin.\n\nNo substantive mathematical check was performed; the report has an empty math_checks list.\n')
(out/'literal_diff.patch').write_text(''.join(difflib.unified_diff(c.splitlines(True),reading.splitlines(True),fromfile='inputs/022/C.tex',tofile='readers/022/C/reading.tex')))
log=json.loads((out/'inspection_log.json').read_text()); log['crop_displayed_once']=[str(Path(x['output']).resolve()) for x in logs];log['follow_up_locus']={'crop':'26_p140_open_quote','reason':'Unsettled opener identified during literal audit; no repeat crop of this locus.','decision':'Two marks support C paired opener.'};log['terminal_period_audit']='Literal C already has the final period after Sigma_h; no change row.';log['coverage']='All reference entries, text, formulas, insertion/deletion states, circles/arrows and independent line marks are in reading.tex and inventory.tsv.';log['substantive_math_checks']=0
(out/'inspection_log.json').write_text(json.dumps(log,ensure_ascii=False,indent=2)+'\n')
# Static checks only.
stack=[]
for i,chx in enumerate(reading):
 if chx in '{}':
  n=0;j=i-1
  while j>=0 and reading[j]=='\\':n+=1;j-=1
  if n%2:continue
  if chx=='{':stack.append(i)
  else:
   assert stack,('unmatched closing brace',i)
   stack.pop()
assert not stack,('unclosed brace',stack)
assert len(re.findall(r'(?<!\\)\$',reading))%2==0
assert set(re.findall(r'\\begin\{([^}]+)\}',reading))==set(re.findall(r'\\end\{([^}]+)\}',reading))
assert all(x['h'] is None and x['diff_h'] is False for x in changes)
assert all(x['crop'] or (x['source'] and x['bbox']) for x in changes+doubts)
assert len(logs)==26
check={'json_valid':True,'balanced_braces':True,'even_dollar_delimiters':True,'environment_sets_match':True,'literal_C_fields_checked':True,'no_H_rows':True,'crop_count':len(logs),'changes':len(changes),'c_doubt_decisions':len(doubts),'remaining_doubt_occurrences':len(remaining),'inventory_rows':len(inv),'math_check_events':0,'latex_compilation_attempted':False}
(out/'static_checks.json').write_text(json.dumps(check,indent=2)+'\n')
print(json.dumps(check,indent=2))
