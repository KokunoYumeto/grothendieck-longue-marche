from pathlib import Path
import json

out=Path('work/readers/030/B')
c_path=Path('work/inputs/030/C.tex')
c=c_path.read_text()
a='/workspace/scratch/6d55c8c3e5a7/source/SP49_CW_109_scans/H109-03_109_scan030_a.jpg'
b='/workspace/scratch/6d55c8c3e5a7/source/SP49_CW_109_scans/H109-03_109_scan030_b.jpg'
w='/workspace/scratch/6d55c8c3e5a7/source/SP49_CW_109_scans/H109-03_109_scan030.jpg'
frozen=json.loads((out/'unresolved_frozen.json').read_text())
loci={r['id']:r for r in frozen['loci']}

def ev(n=None,source=None,bbox=None):
    if n:
        r=loci[n]
        return {'crop':r['output'],'source':str(Path(r['source']).absolute()),'bbox':r['bbox']}
    return {'crop':None,'source':source,'bbox':bbox}

old381=r'\tikz[baseline=(old381B.base)]{\node[inner sep=0pt] (old381B) {\deleted{\unsure{8}}};\node[anchor=base west,inner sep=0pt] at ([xshift=.03em]old381B.base west) {3};}'
point377=r'\tikz[overlay,x=1em,y=1ex]{\fill[black!60] (7,.35) ellipse (.025 and .055);}'
point393=r'\tikz[overlay,x=1em,y=1ex]{\fill[black!65] (11.5,1.8) circle (.035);}'
stroke393=r'\tikz[overlay,x=1em,y=1ex]{\draw[black!55,line width=.25pt,line cap=round] (14.7,.85)--(14.75,.60);}'
point394=r'\tikz[overlay,x=1em,y=1ex]{\fill (1.6,.8) ellipse (.022 and .07);}'
points396=r'\normalmarginpar\margin{\tikz[x=1ex,y=1ex]{\fill (0,0) circle (.045);\fill (.2,.3) circle (.045);}}'
formula401=r'\tikz[baseline=(km401B.base)]{\node[inner sep=0pt] (km401B) {$(k-M)$};\fill ([xshift=-.20em,yshift=-.45ex]km401B.north west) circle (.045ex);}'

s=c
replacements=[
(r'p 372 l.16',r'p 372 l16'),
(r'\unsure{inverse|unverse|universe}',r'\unsure{unverse|inverse|universe}'),
("p 377 l.-15 ``its'' \\quad l-7 ``won't'' \\quad l-3 `don't''", "p 377 l.-15 ``its'' \\quad l-7 ``won't'' \\quad l-3 `don't''"+point377),
("p 380 l.15 ``don't''", "p 380 l.15 ``don't"),
(r'l.\deleted{\unsure{8}}\unsure{3|8}',r'l\unsure{-|.}'+old381),
("``much sense in bothering''",r"``much sense in bothering\unsure{''|'}"),
(r'(resp. with\ldots{})',r'(resp. with....)'),
("p 388 l 13 ``equivalent \\deleted{with}'' to'' is more usual.","p 388 l 13 ``equivalent \\deleted{with}'' to'' is more usual,"),
("p 393 l-10 ``didn't''","p 393 l-10 ``didn't''"+point393+stroke393),
("p 394 l-7 ``commutes with''","p 394 l-7 ``commutes with''"+point394),
("p 396 l.-4 ``commute with'' again l-2.",points396+"\np 396 l.-4 ``commute with'' again l-2."),
("l.-11 ``$(k-M)$''",r"l.-11 \unsure{`|``}"+formula401+"''"),
('% archive sheet number: 29\n% The last figure can also be read as 3.','% archive sheet number: 23 (possibly 29).\n% The final numeral remains doubtful; the open upper curve favours 3.')
]
for before,after in replacements:
    assert s.count(before)==1,(before,s.count(before))
    s=s.replace(before,after)
s=s.replace('\\scanpage{30}\n','\\scanpage{30}\n% The two long near-vertical traces are treated as material creases, not ink rules.\n% Small isolated dark marks are drawn at their observed sides; their origin is unassigned.\n')
(out/'reading.tex').write_text(s)

changes=[]
def change(i,place,cc,reading,kind,confidence,evidence,n=None,source=None,bbox=None):
    assert cc=='' or cc in c,(i,cc)
    changes.append({'id':i,'place':place,'c':cc,'h':None,'reading':reading,'diff_c':True,'diff_h':False,'kind':kind,'marked_in_H':False,'confidence':confidence,'evidence':evidence,**ev(n,source,bbox)})
change('030B-01','p372 l.17, final word',r'\unsure{inverse|unverse|universe}',r'\unsure{unverse|inverse|universe}','misread word','low','The initial joined troughs have no separately placed i dot and favour unverse; the crowded initial sequence still permits inverse and universe. The final looped e is readable across the vertical material trace. This reorders the candidates without claiming resolution.','01')
change('030B-02','blank area to the right of p377 l-3', '',point377,'drawing or diagram','high','One distinct small vertically oval dark point stands at approximately x1319,y533 in half a. It is separated from the wording and is preserved geometrically with no punctuation or authorship assignment.','23')
change('030B-03','p380 l.15, right edge of the quoted contraction',"p 380 l.15 ``don't''","p 380 l.15 ``don't",'text not on the page','medium','The opening has two separate curls. No independent closing pair is discernible after t: the two long strokes above/right continue down from the ff of insufficient in the preceding line. They are not duplicated as quotation marks.','06')
change('030B-04','p381 line reference and overwritten digit',r'l.\deleted{\unsure{8}}\unsure{3|8}',r'l\unsure{-|.}'+old381,'misread symbol or index','medium','The live digit has two open right-facing lobes and a heavy lower return, deciding 3. Loops from an older digit survive in the same character space; 8 remains tentative. The short low horizontal/curved mark after l is not securely distinguishable as a dash or an elongated period. Old and live digits are superposed rather than printed consecutively.','07')
change('030B-05','p383 l-9, closing quotation after bothering',"``much sense in bothering''",r"``much sense in bothering\unsure{''|'}",'misread symbol or index','low','The terminal raised patch has a long right descent and a shorter thickened left part joined at the top. A fused double closer is favoured, but a single complicated stroke cannot be excluded. The opening pair at much is independently clear in half a.','08')
change('030B-06','p385 l6, low marks after the second with',r'(resp. with\ldots{})',r'(resp. with....)','misread symbol or index','high','Four separate low dark groups follow with: the first two are close and elongated, followed by two more compact groups before the closing parenthesis.','12')
change('030B-07','p388 l13, terminal punctuation after usual','is more usual.','is more usual,','misread symbol or index','medium','The detached terminal mark is a curved stroke descending leftward to below the neighbouring baseline, so comma is read. The small broken exit at the foot of l is not a second punctuation mark.','17')
change('030B-08','blank area above/right of p393', '',point393,'drawing or diagram','high','A small separate dark round point is visible near x1098,y602 in half b. The crop shows its compact centre; origin remains unassigned.','24')
change('030B-09','blank area right of p393', '',stroke393,'drawing or diagram','high','A short isolated stroke near x1233,y631 descends slightly to the right; it is separate from the surrounding paper texture and from the point farther left. No line connecting them is drawn.','25')
change('030B-10','right of p394 l-7', '',point394,'drawing or diagram','high','The half shows a tiny isolated nearly vertical dark mark near x771,y679, beyond the closing quotation. It is preserved at that position without a punctuation interpretation.',source=b,bbox=[740,658,795,703])
change('030B-11','right margin at p396 level', '',points396,'drawing or diagram','high','Two distinct dark points lie diagonally, with the upper point to the right, near x1459–1465,y904–913 in half b. They remain on the right and are not joined.',source=b,bbox=[1434,884,1487,930])
change('030B-12','p401 l.-11, opening quotation before the parenthesised expression',"``",r'\unsure{`|``}','misread symbol or index','low','The opener is one tall connected curled body with a thickened lower branch. It can be a single curled stroke or two fused strokes; the single is placed first from the visible continuous body. The two closing strokes are separately clear.','21')
change('030B-13','p401 l.-11, isolated point just left of the opening parenthesis',r'$(k-M)$',formula401,'drawing or diagram','high','A separate dark point lies just left of the opening parenthesis below its top, around x771,y1113 in half b. It is not identified as a letter or punctuation sign and is not folded into the quotation. The formula itself is unchanged.','21')
change('030B-14','lower-left archive numeral, comment only','% archive sheet number: 29\n% The last figure can also be read as 3.','% archive sheet number: 23 (possibly 29).\n% The final numeral remains doubtful; the open upper curve favours 3.','misread symbol or index','medium','The final figure has a visibly open left side of its small upper curve and a long lower curve, favouring 3. Faintness and the small upper turning still permit 9. No inference from neighbouring scans is used.','22')
change('030B-15','p372 first line reference',r'p 372 l.16',r'p 372 l16','misread symbol or index','medium','The upper-half reading has the looped l followed by16 without a separately discernible intervening stop. The literal C period was identified as a difference during the final full-text collation.',source=a,bbox=[246,121,329,173])

c_doubts=[]
def doubt(place,cc,reading,resolved,confidence,evidence,n=None,source=None,bbox=None):
    c_doubts.append({'place':place,'c':cc,'reading':reading,'resolved':resolved,'confidence':confidence,'evidence':evidence,**ev(n,source,bbox)})
doubt('explicit C doubt: p372 l.17 final word',r'\unsure{inverse|unverse|universe}',r'\unsure{unverse|inverse|universe}',False,'low','Joined undotted initial troughs favour unverse, but they do not exclude inverse or universe; the final e is visible. The qualification small ... and finite is not used to force a word.','01')
doubt('explicit C doubt: p381 earlier overwritten digit',r'\deleted{\unsure{8}}',r'\deleted{\unsure{8}}',False,'low','Surviving closed portions above and below the middle crossing favour 8, but the heavy live 3 masks enough of the older path to retain the doubt. Overwriting state and one-character extent are secure.','07')
doubt('explicit C doubt: p381 live overwritten digit',r'\unsure{3|8}','3',True,'high','Two open lobes on the right and the heavy leftward lower return identify the live 3; residual closed contours belong to the earlier overlapped character.','07')
doubt('explicit C doubt: Formula (7) opening mark',r'\unsure{``|`|$+$}',r'\unsure{``|`|$+$}',False,'low','A short oblique body and transverse branches form a cross-like cluster. Double or single quotation and plus remain possible; its quotation-like position is only contextual support.','13')
doubt('explicit C doubt: p387 l-17 cancelled final letter',r'\deleted{\unsure{s}}',r'\deleted{\unsure{s}}',False,'low','The cancelled area is one trailing character after the clearly live commute. A small upper curve and lower oblique remainder favour s, but the two cancellation passes obscure its full contour. Deletion extent is high-confidence; letter identity is not.','15')
doubt('explicit C doubt: page reference after396',r'p.39\unsure{7|1}',r'p.39\unsure{7|1}',False,'medium','The last figure has a short leftward top hook and a descending stroke, favouring 7, but the top is too abbreviated to exclude 1 independently of page sequence.','20')
doubt('C context corner uncertainty: lower-left archive numeral','29 (possibly 23)','23 (possibly 29)',False,'medium','The upper curve is visibly open to the left; 3 is preferred. The faint small upper turning still allows 9. This remains a comment, not manuscript body text.','22')
doubt('C context: p371 line reference','l.14','l.14',True,'high','The looped line-reference letter has a distinct low point before 14.',source=a,bbox=[223,45,314,110])
doubt('C context: p372 first line reference','l.16','l16',True,'medium','The looped l is followed by16 without a separately discernible intervening stop; the extra literal C period is reported as change030B-15.',source=a,bbox=[246,121,329,173])
doubt('C context: p372 second line reference','l.17','l.17',True,'high','A separate low point stands between the looped l and17.',source=a,bbox=[741,123,852,181])
doubt('C context: p372 continuation reference','l.21','l.21',True,'high','The low stop after the looped l is visible before21.',source=a,bbox=[246,181,348,242])
doubt('C context: quotation framing at p372 l17',r"``with small \ldots{} and finite \unsure{inverse|unverse|universe}''",r"``with small \ldots{} and finite \unsure{unverse|inverse|universe}''",False,'high','The opening pair is visibly two separated small curved strokes in half a; the final pair is two independent upright strokes in crop01. The word doubt, separately recorded, is retained.','01')
doubt('C context: quotation framing at p383 l-9',"``much sense in bothering''",r"``much sense in bothering\unsure{''|'}",False,'low','Two opening strokes before much are clear in half a. The fused terminal cluster remains uncertain after crop08; the contraction apostrophes in nearby entries are not counted as outer quotation marks.','08')
doubt('C context: p372 l17 baseline dots',r'with small \ldots{} and finite',r'with small \ldots{} and finite',True,'high','Exactly three separated low dots stand between small and and in the half image.',source=a,bbox=[1093,143,1193,178])
doubt('C context: p385 l6 first baseline-dot group',r'commutes with \ldots{}',r'commutes with \ldots{}',True,'high','Exactly three separate low points occur after the first with and before the opening parenthesis.',source=b,bbox=[598,170,689,215])
doubt('C context: p385 l6 second baseline-dot group',r'with\ldots{}','with....',True,'high','Four low dark groups are separately visible; the first two are closer together than the latter gaps.','12')
doubt('C context: first101 in p373 row','line 3 of 101','line 3 of 101',True,'high','The earlier101 follows of directly; no section sign occurs in that gap.',source=a,bbox=[451,303,733,380])
doubt('C context: second101 in p373 row',r'\S101 l.11',r'\S101 l.11',True,'high','Two joined turns precede101 as a section sign; a separate low point follows the line-reference l before11.',source=a,bbox=[1208,297,1391,369])
doubt('C context: p379 underlined correction and t stroke in to',r"not ``to'' ``\uuline{with}''",r"not ``to'' ``\uuline{with}''",True,'high','Two low rules underline with only. The transverse upper stroke of to belongs to t and does not cancel that word.',source=a,bbox=[389,614,739,701])
doubt('C context: p386 underlined is',r'\uline{is}',r'\uline{is}',True,'high','One short low returned stroke lies beneath is and stops before well.',source=b,bbox=[451,289,502,356])
doubt('C context: p385 quoted mathematical sign',r'$\cong$',r'$\cong$',True,'high','A single wavy stroke stands above two distinct horizontal strokes. This is ink identification, not a mathematical proof check.','13')
doubt('C context: p401 expression',r'$(k-M)$',r'$(k-M)$',True,'high','The expression contains a low ordinary k, one horizontal minus, an ordinary single-contour capital M, and two round parentheses. The opener and separate point are recorded independently.','21')
doubt('C context: p374 interruption punctuation','commutation :.. with','commutation :.. with',True,'high','One higher point and three low points appear between commutation and with, preserving the colon-plus-two-points arrangement.',source=a,bbox=[625,446,690,495])
doubt('C context: p382 parenthetical qualification','(typing slip.)','(typing slip.)',True,'high','The two round delimiters, words typing slip and the low point before the closing parenthesis are visible.',source=a,bbox=[620,934,839,1010])
doubt('C context: p388 cancellation and quote placement',r"``equivalent \deleted{with}'' to'' is more usual.",r"``equivalent \deleted{with}'' to'' is more usual,",True,'high','The cancellation crosses with only; two high closing strokes remain outside its upper-right endpoint, and a separate closing pair follows to. The terminal punctuation is treated separately in change030B-07.','16')
doubt('Additional C punctuation check: p377 l.-15','l.-15','l.-15',True,'high','A separate low point after l precedes the short negative-reference dash. The two opening quote strokes before its are also separate.','03')
doubt('Additional C punctuation check: p381 line-reference separator','l.',r'l\unsure{-|.}',False,'low','The low separated mark is broad and curved; its geometry favours a short dash but an elongated point remains possible.','07')
doubt('Additional C punctuation check: p386 l.-11','l.-11','l.-11',True,'medium','A pale separate baseline point lies between the l foot and the higher minus. Its location supports retaining the literal period, while the broken entry stroke of l at the left is not counted as another point.','14')
# Keep all literal text fields literal; no escaped pseudo-quotes.
for d in c_doubts:
    d['c']=d['c'].replace(r'\x27',"'")
    d['reading']=d['reading'].replace(r'\x27',"'")

remaining=[
{'place':'p372 l.17 final word','reading':r'\unsure{unverse|inverse|universe}','alternatives':'unverse; inverse; universe','confidence':'low','reason':'Joined initial strokes and lack of an independently decisive dot do not determine the initial letter sequence.'},
{'place':'p381 old overwritten digit','reading':r'\deleted{\unsure{8}}','alternatives':'8 favoured; complete older contour hidden','confidence':'low','reason':'The live3 covers the joints between surviving old loops.'},
{'place':'p381 line-reference separator','reading':r'l\unsure{-|.}','alternatives':'short low dash; elongated period','confidence':'low','reason':'The detached low mark is wider and more curved than a point, but its low position prevents a firm distinction.'},
{'place':'p383 l-9 after bothering','reading':r"bothering\unsure{''|'}",'alternatives':'two fused closing strokes; one complex closing stroke','confidence':'low','reason':'The two apparent branches are joined in a compact dark patch.'},
{'place':'p385 Formula7 opener','reading':r'\unsure{``|`|$+$}','alternatives':'double quote; single quote; plus','confidence':'low','reason':'Cross-like connected geometry does not settle the sign identity.'},
{'place':'p387 l-17 cancelled ending','reading':r'commute\deleted{\unsure{s}} with','alternatives':'s favoured; interior path masked','confidence':'low','reason':'The cancellation strokes obscure the complete old character, although its one-character extent is secure.'},
{'place':'page reference after396','reading':r'p.39\unsure{7|1}','alternatives':'397;391','confidence':'medium','reason':'The final numeral has only a short top hook; sequence is not used to resolve it.'},
{'place':'p401 l.-11 opening quotation','reading':r'\unsure{`|``}','alternatives':'single curled opening stroke; fused double opening','confidence':'low','reason':'The compact body has a lower branch but no securely separate second stroke.'},
{'place':'archive corner','reading':'23 (possibly29)','alternatives':'23;29','confidence':'medium','reason':'An open upper curve favours3, but the light pencil contour does not exclude9.'}
]
for doubt_row,crop_id in zip(remaining,['01','07','07','08','13','15','20','21','22']):
    doubt_row.update(ev(crop_id))

entries=[
('p371 l.14','p.371 l.14 ``didn\x27t\x27\x27','upper left, first line'),
('p372 l16','commutes with','upper block, second physical line, left'),
('p372 l.17','with small ... and finite','upper block, second physical line, right'),
('p372 l.21','commute with','upper block, third physical line, left'),
('p372 l-12','commute with','upper block, third physical line, centre'),
('p372 l-5','its','upper block, third physical line, right'),
('p373 l-13','recommendation','upper block, fourth physical line'),
('p.373 l2','its','upper block, fifth physical line, left'),
('line3 of101','no question of dealing','upper block, fifth physical line, centre'),
('section101 l.11','commuting with','upper block, fifth line at right, wrapping to next line at left'),
('section101 l-6','its','upper block, sixth physical line after with'),
('p374 l10','commutation :.. with','upper third'),
('p377 l.-15','its','upper third, p377 row left'),
('p377 l-7','won\x27t','upper third, p377 row centre'),
('p377 l-3','don\x27t','upper third, p377 row right'),
('378 l-7','interpret','upper-middle, p378 row left'),
('378 l-1','commuting with','upper-middle, p378 row right'),
('379 l1','not to; with','upper-middle, p379 first row left'),
('379 l8','made up of','upper-middle, p379 first row centre'),
('379 following l8','commute with','upper-middle, p379 first row right'),
('379 l.15','insufficient','upper-middle, p379 continuation'),
('p380 l.15','don\x27t','middle-upper'),
('p-381 line reference','commuting with','middle-upper, one overwritten reference digit'),
('p382 l.1','haven\x27t','middle-upper, p382 first row left'),
('p382 l3','hadn\x27t','middle-upper, p382 first row centre'),
('p382 l.5','breathe','middle-upper, p382 first row right'),
('p382 l.7','covered (typing slip.)','middle-upper, p382 second row left'),
('p382 l14','out to prove','middle-upper, p382 second row right'),
('p383 l.10','inaccurate','middle, p383 first row left'),
('p383 l11','its','middle, p383 first row centre-left'),
('p383 l-10','doesn\x27t','middle, p383 first row centre-right'),
('p383 l-9','much sense in bothering','middle, starts at far right and continues on next physical line'),
('p383 l-8','invaluable','middle, second physical row centre'),
('p383 l-3','suggest simply dropping','middle, second row right, continuing at left on next line'),
('p384 l8','made up of','middle'),
('p385 l6','commutes with ... (resp. with....)','middle-lower, first p385 row left'),
('p385 l-14','symmetrically','middle-lower, first p385 row right'),
('p385 continuation','Formula (7) congruence sign missing','middle-lower, separate text line under p385'),
('386 l.-11','as is well known too','lower half, row below Formula7 left'),
('386 l-6','without','lower half, row below Formula7 right'),
('p387 l-17','commute [cancelled character] with','lower half, p387 row left'),
('p387 l-3','commuting with','lower half, p387 row right'),
('p388 l13','equivalent [with cancelled] to is more usual,','lower half'),
('p390 l16','interpret','lower half'),
('p392 l8','its','lower half, p392 row left'),
('p392 l-1','afraid','lower half, p392 row right'),
('p393 l-10','didn\x27t','lower half'),
('p394 l-7','commutes with','lower half'),
('p395 l1','interpreted as saying is more usual.','lower half, first p395 row left'),
('p395 l4','commute with','lower half, first p395 row right'),
('p395 l16','interpret','lower half, p395 continuation'),
('p396 l.-4','commute with again l-2.','bottom quarter'),
('p39[7|1] l-13','its also in l-12','bottom quarter'),
('p.399 l6','commutes with','bottom quarter, p399 row left'),
('p.399 l17','analogue','bottom quarter, p399 row centre'),
('p.399 l19','its','bottom quarter, p399 row right'),
('p400 l-8','developed','penultimate text row'),
('p401 l.7','didn\x27t','last text row, left'),
('p401 l.-11','(k-M)','last text row, centre')
]
inventory=[]
for i,(place,first,pos) in enumerate(entries,1):
    inventory.append({'sheet_kind':'list','hand':'his hand','element':f'{i:02d}','kind':'text','position':f'{place}; {pos}','first_words_or_objects':first.replace('\\x27',"'"),'transcribed':'yes'})
nested=[
('text','p379 l1; nested underline','with, double underline','his hand'),
('deletion','p381 line reference; old glyph overwritten at same place','old uncertain8','his hand'),
('text','p381 line reference; live glyph superposed on old glyph','live3','his hand'),
('text','p386 l.-11; nested underline','is, single underline','his hand'),
('deletion','p387 l-17; final one-character cancellation after commute','uncertain s','his hand'),
('deletion','p388 l13; cancellation within quoted wording','with; closing quote pair remains live','his hand'),
('drawing','right blank area at p377 level, half a x1319,y533','one small oval point','unassigned'),
('drawing','right blank area above p393, half b x1098,y602','one small dark point','unassigned'),
('drawing','right blank area at p393, half b x1233,y631','one short descending-right stroke','unassigned'),
('drawing','right of p394 wording, half b x771,y679','one tiny nearly vertical mark','unassigned'),
('drawing','right margin at p396, half b x1459–1465,y904–913','two separate points, upper one rightward','unassigned'),
('drawing','p401 expression, just left of opening parenthesis, half b x771,y1113','one separate dark point','unassigned'),
('margin note','lower-left corner, archive notation; comment only','23, possibly29','another unnamed hand, pencil')
]
for kind,pos,first,hand in nested:
    inventory.append({'sheet_kind':'list','hand':hand,'element':f'{len(inventory)+1:02d}','kind':kind,'position':pos,'first_words_or_objects':first,'transcribed':'yes'})

notation=[
{'sign':'l / l. / l- / l.-','location':'p381 reference; other line-reference punctuation handled occurrence by occurrence','reading':r'l\unsure{-|.}','evidence':'Halves settle ordinary looped l versus straight numeral1; crops03,07,14 address the small separated marks. The first p372 reference is l16, without the period in C.'},
{'sign':'joined initial strokes','location':'p372 l.17 final word','reading':r'\unsure{unverse|inverse|universe}','evidence':'Crop01 leaves the initial letter sequence unresolved; final e remains visible across the trace.'},
{'sign':'quotation strokes','location':'p373 l-13','reading':"``recommendation''",'evidence':'Crop02 separates two opening legs joined at the top and two independent closing strokes.'},
{'sign':'quotation strokes','location':'p377 l.-15','reading':"``its''",'evidence':'Crop03 separates two opening curls and two joined closing legs.'},
{'sign':'quotation strokes','location':'p378 l-1','reading':"``commuting with''",'evidence':'Crop04 separates the long left opening stroke and short right opening stroke; the half settles the closing pair.'},
{'sign':'quotation strokes','location':'p379 l.15','reading':"``insufficient''",'evidence':'Crop05 separates both opening and closing pairs.'},
{'sign':'quotation strokes','location':'p383 l-3','reading':"``suggest simply dropping''",'evidence':'Crop09 separates two opening legs joined at an arch; the half settles the closing pair.'},
{'sign':'quotation strokes','location':'p395 l1','reading':"``interpreted as saying''",'evidence':'Crop19 separates the two joined closing legs; the opening pair was settled in the half.'},
{'sign':'three raised marks before its','location':'p392 l8','reading':"``its''",'evidence':'Crop18 shows two opening quote strokes and a separate dot belonging to i; it does not justify a third quotation mark.'},
{'sign':'single opening quotes','location':'p377 dont; p382 covered; p383 doesnt; p387 commuting','reading':"`don't''; `covered''; `doesn't''; `commuting with''",'evidence':'Each occurrence is independently visible as a single raised opener in its supplied half; internal apostrophes remain separate.'},
{'sign':'closing-quote doubt','location':'p383 l-9 bothering','reading':r"bothering\unsure{''|'}",'evidence':'Crop08 shows an inseparable compact upper patch with unequal downward branches.'},
{'sign':'no independent closing quote pair','location':'p380 dont','reading':"``don't",'evidence':'Crop06 shows the upper-right stems continuing from the preceding insufficient descenders, with no separate closer after t.'},
{'sign':'three and four low marks','location':'p372 l17; p385 l6 first and second groups','reading':r'\ldots{}; \ldots{}; ....','evidence':'Half a has three after small; half b has three after the first with; crop12 gives four after the second with.'},
{'sign':':..','location':'p374 l10','reading':':..','evidence':'Half a separates one high point from three low points.'},
{'sign':r'\S','location':'p373 row, second101 only','reading':r'\S101','evidence':'Half a shows two linked turns before the second101; no such sign before the first.'},
{'sign':r'\uuline{with}; \uline{is}','location':'p379 l1; p386 l.-11','reading':r'\uuline{with}; \uline{is}','evidence':'Halves show two low rules beneath with and one short rule beneath is.'},
{'sign':'overwritten reference','location':'p381','reading':old381,'evidence':'Crop07 resolves live3 and retains old8 uncertainty within the same glyph position.'},
{'sign':r'\cong','location':'p385 Formula7','reading':r'\cong','evidence':'Crop13 has one wave over two independent horizontal bars.'},
{'sign':'cross-like opener','location':'p385 Formula7','reading':r'\unsure{``|`|$+$}','evidence':'Crop13 leaves the attached oblique and transverse parts compatible with the listed alternatives.'},
{'sign':'ordinary k and M, minus, round parentheses','location':'p401 l.-11','reading':r'$(k-M)$','evidence':'Crop21 shows single-contour ordinary letters, a single minus and both round delimiters; no doubled alphabet or added index.'},
{'sign':'isolated marks','location':'right of p377,p393,p394,p396; beside p401 opening parenthesis','reading':'\n'.join([point377,point393,stroke393,point394,points396,formula401]),'evidence':'Crops23–25 and21, and the lower half at p394/p396; these are the exact six TeX blocks in their page order. Marks are not connected and their origin is unassigned.'}
]

report={
'scan':30,'reader':'B','model':'GPT-6 Astra Pro','effort':'not exposed',
'viewed':[w,a,b],
'layout':'Single handwritten correction-list sheet, one main hand, filling nearly the full height and arranged by page references371–401. The first long rows span most of the width; later rows occupy mainly the left and centre. The p373 commuting with and two p383 quotations wrap onto following physical lines. There is a separate Formula(7) text row below p385, but no free-standing mathematical display or diagram. The sole overwritten numeral is at p381; one trailing character is cancelled at p387, and with is cancelled at p388. With at p379 is doubly underlined and is at p386 singly underlined. No independent insertion caret or interlinear inserted wording is visible. Two long narrow near-vertical traces, around x212–225 and x1487–1502, begin in the upper writing area near y100 and become much paler toward the foot; their grey/bright edges and uneven surface shading are treated as material creases, not added ink rules. Separate small points/short strokes at six locations are reproduced geometrically with origin unassigned. The lower-right round grey feature is treated as a material blemish. The lower-left pencil archive numeral is23 with29 retained as an alternative, recorded only as a comment. Inventory covers59 distinct correction entries, two nested underline spans, three deletion/overwriting states, the live overwritten numeral, six isolated-mark groups and the archive corner; no diagram or insertion is omitted.',
'changes':changes,'c_doubts':c_doubts,'remaining_doubts':remaining,'inventory':inventory,
'notes':[
'Correction list covering cited typescript pages371–401, retaining the manuscript page/line-reference forms and the repeated commute/commutes/commuting with corrections.',
'p379 l1 explicitly says not to and gives with with double underlining; the word to itself is not cancelled.',
'p382 l7 calls covered a (typing slip.); the original typescript wording is not supplied on this sheet.',
'p385 says the quoted congruence sign is missing from Formula(7); the formula itself is not reproduced.',
'p388 cancels with after equivalent, gives to, and calls it more usual; the visible terminal mark is comma-shaped.',
'p395 gives interpreted as saying and calls it more usual. P396 repeats commute with again at l-2; the following page reference, uncertain397/391, says its also in l-12.',
'p401 l.-11 supplies the parenthesised expression(k-M), with ordinary letters and a minus.',
'No title, date, salutation, signature or mathematical proof appears. Isolated marks have no assigned linguistic or mathematical role.'
],
'math_checks':[],
'notation':notation,
'abbreviations':[
{'form':'p / p. / p-','expansion':'page (interpretation only)','place':'page references throughout, including p.371,p-381'},
{'form':'l / l.','expansion':'line (interpretation only)','place':'line references throughout'},
{'form':'resp.','expansion':'respectively (interpretation only)','place':'p385 l6 parenthesis'}
],
'brief_feedback':'Read brief_v14, conventions, preamble, witnesses, notation snapshot, metadata and corrected C_context plus addendum. H status is desc; all changes therefore have h=null and diff_h=false, with no H collation rows. Whole and each supplied half were viewed exactly once. The25-locus list was frozen before cropping; each crop was created once by crop.py and viewed singly once. No other page image, other reader output, OCR, recognition library, external research, agent delegation or compilation was used. The main classification difficulties were distinguishing connected quotation strokes from nearby letter dots/descenders and distinguishing the vertical material traces from ink. Mathematical glyph identification is reported as notation, not inflated into proof checks.',
'crop_workflow':{'frozen_list':'work/readers/030/B/unresolved_frozen.json','generated_count':25,'viewed_count':25,'viewed_crops':[loci[f'{i:02d}']['output'] for i in range(1,26)],'crop_log':'work/readers/030/B/crops/crops.jsonl'},
'coverage':{'main_text_entries':len(entries),'inventory_rows':len(inventory),'explicit_c_doubt_locations':7,'c_and_context_decisions':len(c_doubts),'changes':len(changes),'remaining_reading_doubts':len(remaining),'h_status':'desc','h_rows':0}
}
(out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report['coverage'],indent=2))
