import json
from pathlib import Path
r=Path('/workspace/scratch/94548b74fbe0/out/readers/006/B')
d=[]
def add(location,C,H,reading,evidence,confidence,kind,diff_C,diff_H,status,crop,bbox,math=None):
 item=dict(id=f'B006-{len(d)+1:02d}',location=location,C=C,H=H,reading=reading,evidence=evidence,confidence=confidence,kind=kind,diff_C=diff_C,diff_H=diff_H,C_doubt_status=status,readers_crop=('crops/'+crop+'.png') if crop else None,bbox=bbox)
 if math: item['mathematical_consequence']=math
 d.append(item)
add('Upright first quotient, last numerator',r"P'Q-Q'P",r"P'Q-PQ'",r"P'Q-Q'P",'After the minus, the round Q bowl and its detached prime precede the tall P. Read on half a.', 'high','misread symbol or index',False,True,None,None,[446,59,590,124])
add('Upright second derivative, overwritten predecessor before 2',r'\deleted{\unsure{+}}','omitted',r'\deleted{\unsure{+}}','A dense horizontal blot has a short downward projection. A former plus remains a supported candidate; its complete vertical stroke cannot be isolated.','low','omission',False,True,'retained','01_second_derivative',[313,215,355,247])
add('Upright second derivative, surviving sign before 2',r'\unsure{-|+}','-',r'\unsure{-|+}','A horizontal stroke survives the overworking; the downward projection leaves a plus alternative. H agrees with the primary minus candidate.','low','other',False,False,'retained','01_second_derivative',[313,215,355,247])
add('Upright second derivative, predecessor immediately before P(',r'\deleted{\unsure{2}}',r'\ill{}',r'\deleted{\unsure{2}}','A small curved descending form protrudes to the left of the live P and has been overworked. The candidate 2 remains qualified.','low','omission',False,True,'retained','01_second_derivative',[523,211,554,278])
add('Upright second derivative, unfinished live continuation',r'P\bigl(',r'\ill{}',r'P\bigl(','The tall P has a right-hand bowl, followed by a large opening parenthesis. No closing member is supplied.','high',r'readable ink left as \ill{}',False,True,None,'01_second_derivative',[539,207,618,298])
add('Upright separate logarithmic-derivative fragment',r"\frac{P'}{\deleted{\unsure{Q}}P}-\frac{Q'}{Q}",'omitted',r"\frac{P'}{\deleted{Q}P}-\frac{Q'}{Q}",'The first denominator contains an older round Q bowl and lower tail, with the new upright P stem and right bowl over it. Both numerator primes, both fraction strokes, the minus, and the second Q are visible.','high','omission',True,True,'resolved','02_log_derivative',[875,470,1067,586])
add('Product identity, exponent on (xy)',r"\unsure{2|''}","''",r"\unsure{2|''}",'The raised mark is one bent, joined shape with a rightward top and descending end. Two touching primes remain possible. H’s two-prime reading is retained as an alternative, not rejected conclusively.','low','misread symbol or index',False,True,'retained','03_product_rule',[118,571,140,595],'The visible primary candidate is 2 despite the derivative terms to its right; the written expression is not repaired.')
add('Product identity, exponent on first x',r"\unsure{x''|x^2}",r"x''",r"\unsure{x''|x^2}",'Two high strokes join at their upper/basal region; the double-prime candidate is stronger, with the joined 2-shaped alternative retained. H agrees with the primary candidate.','medium','other',False,False,'retained','03_product_rule',[164,579,196,608])
add('Product identity, middle y exponent',r'y^{\unsure{\prime}}',r"y'",r'y^{\unsure{\prime}}','A short raised stroke meets writing of the opposite layer. Its exact extent is not isolated; one prime remains the supported candidate.','low','other',False,False,'retained','03_product_rule',[279,579,314,620])
add('Product identity, last y exponent',r'y^{\unsure{\prime\prime|\prime}}',r"y''",r'y^{\unsure{\prime\prime|\prime}}','Two small raised components can be followed beside the last y, but the contrary-layer loop runs through them. The one-prime alternative remains. H agrees with the primary candidate.','low','other',False,False,'retained','03_product_rule',[324,584,369,637])
add('General quotient rule, overwritten numerator',r"\deleted{\unsure{P'}}f",'f',r"\deleted{\unsure{P'}}f",'A black upright and upper bowl precede the surviving long-looped f; the old prime-like upper curl is partly fused with the replacement. P prime remains a qualified predecessor.','low','omission',False,True,'retained','04_general_quotient',[95,1007,139,1082])
add('Expanded upright quotient, initial numerator and its two cancellations',r"(P''Q+\deleted{P'Q'}-\deleted{P'Q'}",'omitted',r"(P''Q+\deleted{P'Q'}-\deleted{P'Q'}",'Opening parenthesis, P double-prime Q, plus, and two P-prime Q-prime groups are visible. Separate oblique strokes cut the two latter groups; the intervening minus remains.','high','omission',False,True,None,'05_expanded_quotient',[27,1211,348,1290])
add('Expanded upright quotient, overwritten sign predecessor',r'\deleted{\unsure{+}}','omitted',r'\deleted{\unsure{+}}','At the next sign, a downward stem survives under two heavy horizontal strokes. The former plus is not completely separable from the overwriting.','low','omission',False,True,'retained','05_expanded_quotient',[342,1246,377,1279])
add('Expanded upright quotient, live sign before Q double-prime P',r'\unsure{-|+}','omitted',r'\unsure{-|+}','The surviving horizontal stroke is clear but its intersection with a downward stem leaves the live sign uncertain.','low','omission',False,True,'retained','05_expanded_quotient',[342,1246,377,1279])
add('Expanded upright quotient, end of parenthesized derivative',r"Q''P)",'omitted',r"Q''P)",'A large round Q, two small high ticks, a descending P, and the closing parenthesis are individually visible.','high','omission',False,True,None,'05_expanded_quotient',[390,1226,510,1289])
add('Expanded upright quotient, factor after the first closing parenthesis',r'\deleted{Q}^{\,2}','omitted',r'\unsure{Q^{\deleted{2}}|\deleted{Q}^{\,2}|Q^2}','The Q bowl remains readable. A long oblique cancellation line meets the raised 2 and the right edge of Q; a darker overworked area occupies the exponent. The local deletion target and the contribution of the contrary-layer diagonal remain unsettled. All glyphs are retained in each candidate.','low','deletion state (struck given live or live given struck)',True,True,None,'05_expanded_quotient',[507,1214,576,1296],'No cancellation is selected for algebraic convenience.')
add('Expanded upright quotient, second numerator term',r"-(P'Q-Q'P)2\deleted{Q}Q'",'omitted',r"-(P'Q-Q'P)2\deleted{Q}Q'",'The minus precedes a complete parenthesis pair; P prime Q minus Q prime P is followed by 2, a Q crossed by a short diagonal, and a final Q prime.','high','omission',False,True,None,'05_expanded_quotient',[559,1211,939,1302])
add('Expanded upright quotient, denominator exponent',r'Q^{\unsure{3|4}}','omitted',r'Q^3','The exponent has an upper right-hand curve, a narrowed middle, and a lower right-hand curve terminating to the left. The crossing long diagonal is separately traceable. These visible curves support 3.','medium','omission',True,True,'resolved','05_expanded_quotient',[439,1330,527,1384])
add('Following simplified quotient, coefficient before P prime',r'-\unsure{2}P\prime',r"-2P'",r"-2P'",'A small curved cap falls leftward into a lower curved foot immediately before the P stem. The coefficient 2 is readable despite contact with the fraction rule.','medium','other',True,False,'resolved','06_simplified_quotient',[294,1478,340,1536])
add('Following simplified quotient, second stroke beneath fraction bar','one fraction rule','one fraction rule','a fraction rule with a second lower stroke beneath its right portion','A second narrow ruled stroke begins below the bar near x=350 and approaches the bar toward the right. It is reproduced as a second line, without assigning emphasis or a mathematical role.','high','other',True,True,None,'06_simplified_quotient',[345,1525,667,1548])
add('Lowest upright fragment, first squared letter',r'2{\unsure{p|P}}^2Q^2\bigl(','omitted',r'2p^2Q^2\bigl(','On half b the p has a small round bowl close to the writing line and a short downward stem; the following Q is taller. Both raised 2s and the open parenthesis are visible.','medium','omission',True,True,'resolved',None,[437,1602,574,1659])
add('Lowest upright fragment, minus before the small quotient',r'\unsure{-}','omitted','-','The short dark horizontal has its own rounded right end, followed by a paper gap before the fraction bar begins.','high','omission',True,True,'resolved','07_final_minus',[561,1623,586,1648])
add('Lowest upright fragment, remaining quotient and terminal plus',r"\frac{Q'}{Q}+",'omitted',r"\frac{Q'}{Q}+",'The upper Q prime, lower Q, long fraction stroke, and separate plus are visible. The fragment ends at that plus.','high','omission',False,True,None,'07_final_minus',[581,1593,682,1658])
add('Rotated determinant, predecessor in first cell',r'a\deleted{\unsure{d|b}}','a',r'a\deleted{\unsure{d|b}}','A separate upright and oval-looped character follows a in the top left cell. Its reinforced upper stem admits d or b; local overworking marks its cancellation.','low','omission',False,True,'retained','08_determinant',[1012,1595,1050,1648])
add('Rotated determinant, sign after matrix',r'\unsure{-|=}','=','-','One short horizontal dash stands after the closing matrix parenthesis. The space immediately beneath it is blank in the enlargement.','high','misread symbol or index',True,True,'resolved','08_determinant',[878,1566,905,1592],'The single written dash is preserved without supplying an equality.')
add('Rotated determinant, following word','inversible','omitted','inversible','After ad-bc the low letter sequence, dotted i strokes, tall b/l strokes, and terminal loop remain readable through the contrary-layer denominator and rule.','medium','omission',False,True,None,'08_determinant',[335,1538,625,1599])
add('First rotated delta line, locally struck terminal expression',r'\deleted{\unsure{=e_d}}','omitted',r'\deleted{=e_d}','Two horizontal equality strokes precede a small e and a lowered d. A slanting strike runs through the equality and e; the final d remains legible.','high','omission',True,True,'resolved','09_first_delta',[210,1389,340,1445])
add('First rotated lower member, eta after a',r'\unsure{\eta|\gamma}',r'\eta',r'\eta','The letter begins with an upright shoulder, rises into a second shoulder, and descends into a long hooked return. The same shouldered form is readable after c and after delta on this page.','high','other',True,False,'resolved','10_aeta',[916,1275,967,1354])
add('First rotated pair, vertical equality',r'\rotatebox{90}{$=$}','omitted',r'\rotatebox{90}{$=$}','Two short parallel near-vertical strokes lie between the two left members, above delta(a eta).','high','omission',False,True,None,'10_aeta',[966,1337,992,1374])
add('Second rotated delta line, overwritten f under e',r'\deleted{\unsure{f}}e_1',r'e_1',r'\deleted{f}e_1','The predecessor has a tall loop and a long lower return. The live dark e crosses its shaft and upper loop; a small 1 stands beside the live e.','high','omission',True,True,'resolved','11_second_delta',[712,1116,768,1224])
add('Second rotated delta line, product point',r'e_1\cdot f_{d-3}',r'e_1f_{d-3}',r'e_1\cdot f_{d-3}','A distinct round point occupies the interval between e subscript 1 and the following f.','high','omission',False,True,None,'11_second_delta',[672,1165,691,1185])
add('Second rotated pair, equality placement',r'\rotatebox{90}{$=$} between vertically arranged members','horizontal = before b alpha',r'\rotatebox{90}{$=$} between the left member and the coefficient line','The two parallel vertical strokes are below the left delta expression; the coefficient line occupies the next line. Read on half b.','high','insertion or placement',False,True,None,None,[994,1090,1023,1129])
add('Third rotated pair, vertical equality',r'\rotatebox{90}{$=$}','omitted',r'\rotatebox{90}{$=$}','Two short parallel strokes lie between the left member delta(f1 e...) and delta(c eta). Read across the overlapping halves.','high','omission',False,True,None,None,[952,795,982,833])
add('After third rotated pair','etc','omitted','etc','A low e, tall crossed t, and terminal c lie immediately below the c-eta line. No abbreviation point is visible.','high','omission',False,True,None,'12_ceta',[837,674,930,720])
add('Rotated prose, initial letter','On en tire','on en tire','On en tire','The initial O is a larger closed loop followed by the low n; the word begins the prose block.','high','other',False,True,None,'13_prose_first',[878,598,944,654])
add('Rotated prose, second listed product and its predecessor',r'\deleted{\unsure{f}}e_1f_{d-3}','omitted',r'\deleted{\unsure{f}}e_1f_{d-3}','The second list member has a live e with small 1 and following tall f; an older loop descends beneath the e. The half shows its full extent. The one enlargement clips part of that descending context, so the predecessor f remains explicitly doubtful.','low','omission',False,True,'retained','13_prose_first',[277,552,426,666])
add('Rotated prose, abbreviated description',r'\unsure{comb. lin}','combinaisons linéaires','comb. lin','The first contracted group ends in a narrow tall b and a separate point; the following tall l continues into short i/n strokes. No full endings are written.','high','abbreviation expanded or spelling modernised',True,True,'resolved','15_prose_abbreviations',[784,376,1047,450])
add('Rotated prose, final basis index',r'f_{d-2}',r'f_{d-1}',r'f_{d-2}','The last subscript has a curved, rightward terminal 2 after d-minus. The preceding e index has a short straight 1 and remains e_{d-1}.','high','misread symbol or index',False,True,None,'15_prose_abbreviations',[291,370,383,458])
add('Rotated prose, coeff punctuation','coeff','coeff.','coeff','The two tall f strokes are followed by open page space at the physical line end; no terminal point is visible.','medium','other',False,True,None,'15_prose_abbreviations',[39,369,148,472])
add('Rotated prose, word following coeff','entiers',r'\ill{}','entiers','A low opening run, tall t, dotted short i, and final ers run are visible at the beginning of the next physical line.','high',r'readable ink left as \ill{}',False,True,None,'16_prose_last',[875,290,1076,356])
add('Rotated prose, fonctions',r'\unsure{fonctions}','fonctions','fonctions','The long initial f is followed by on, a crossed tall t, an i point, and the ending ons; the internal joined strokes support the whole word.','medium','other',True,False,'resolved','16_prose_last',[539,283,801,358])
add('Last rotated first line, predecessor before x subscript i-minus-1',r'\deleted{\unsure{\delta}}','omitted',r'\deleted{\unsure{\delta}}','An overworked loop and rising stem intervene between e subscript 1 and x. Contrary-layer strokes run through the form; delta remains a qualified predecessor.','low','omission',False,True,'retained','17_final_delta',[471,138,562,218])
add('Last rotated first line, unfinished bound',r'2\leq i\leq{}',r'2\leq i',r'2\leq i\leq{}','A second angled less-than form with its lower horizontal bar follows i. Open space follows the sign; no upper bound is supplied.','high','omission',False,True,None,'17_final_delta',[204,153,254,205])
add('Last rotated first line, parentheses around the bound','none',r'(2\leq i)','none','The inequality stands in open space after the formula; no enclosing curved strokes surround it.','high','text not on the page',False,True,None,'17_final_delta',[192,137,328,218])
add('Last rotated lower line, first coefficient and overwritten predecessor',r'\deleted{\unsure{S}}s',r'\alpha',r'\deleted{\unsure{S}}s','The reinforced coefficient has a low s-shaped live curve. An older taller double-curving form remains under it; S stays qualified. The separate s on the right provides a same-page shape comparison.','medium','misread symbol or index',False,True,'retained','18_final_coefficients',[979,51,1038,123])
add('Last rotated lower line, coefficient before f subscript i-plus-1','t',r'\beta','t','A single tall upright with a transverse cross-stroke stands before f.','high','misread symbol or index',False,True,None,'18_final_coefficients',[852,50,891,118])
add('Last rotated lower line, right member',r's e_i+t f_i',r'\ill{}',r's e_i+t f_i','The s, rounded e with dotted small i, plus, crossed t, tall-looped f, and its small i are visible on the half and enlarged line.','high',r'readable ink left as \ill{}',False,True,None,'18_final_coefficients',[549,31,751,119])
add('Last rotated pair, vertical equality',r'\rotatebox{90}{$=$}','omitted',r'\rotatebox{90}{$=$}','Two short thick parallel vertical strokes sit above the lower delta expression.','high','omission',False,True,None,'18_final_coefficients',[977,108,1008,140])
add('Detached point below-left of On in the rotated orientation','omitted','omitted',r'\underset{\unsure{\cdot}}{\phantom{O}}','A small dark round point is visible at approximately full-scan (968,603), separated from the prose letters and other ruled strokes. Its role, hand, and layer membership remain unresolved.','low','omission',True,True,None,'13_prose_first',[962,597,976,610])
# Literal punctuation in H that is not visible at the corresponding manuscript endpoint.
punctuation=[
('First rotated delta line, terminal comma',',','09_first_delta',[204,1383,252,1445]),
('First rotated lower member, terminal comma',',','10_aeta',[248,1265,337,1338]),
('Second rotated lower member, terminal comma',',',None,[650,950,733,1068]),
('Third rotated upper member, terminal comma',',',None,[47,842,128,923]),
('Third rotated lower member, terminal semicolon',';','12_ceta',[307,694,386,771]),
('Rotated prose, terminal semicolon',';','16_prose_last',[49,287,121,360]),
('Last rotated upper member, terminal semicolon',';','17_final_delta',[191,136,233,218]),
('Last rotated lower member, terminal semicolon',';','18_final_coefficients',[546,30,587,121]),
('Determinant after ad-bc, editorial full stop','.','08_determinant',[645,1545,795,1606]),
('Product identity, terminal comma',',','03_product_rule',[344,565,424,665]),
('General quotient identity, terminal comma',',','04_general_quotient',[348,1118,406,1194]),
('Opening quotient identity, terminal comma',',',None,[556,96,612,155]),
('Second derivative fragment, terminal comma',',','01_second_derivative',[581,209,624,300]),
('Simplified quotient, terminal full stop','.','06_simplified_quotient',[333,1547,406,1613]),
]
for loc,mark,crop,bbox in punctuation:
 add(loc,'no terminal punctuation',mark,'no terminal punctuation','No corresponding detached punctuation mark is visible at this endpoint. H uses the mark while joining its condensed formulas or prose. This is recorded separately from H’s explicitly descriptive captions.', 'medium','other',False,True,None,crop,bbox)

inv=[]
def inventory(element,kind,position,words,cancelled=False,hand='his hand'):
 inv.append(dict(sheet_kind='cancelled_draft' if cancelled else 'text',hand=hand,element=element,kind=kind,position=position,first_words_or_objects=words,transcribed='yes'))
inventory('006.B.01','display','upright top line',"(P/Q)'=P'/Q-PQ'/Q²")
inventory('006.B.02','display','upright second line',"(P/Q)''=P''/Q...")
inventory('006.B.03','deletion','second line before 2','overwritten candidate plus')
inventory('006.B.04','deletion','second line before P(','overwritten candidate 2')
inventory('006.B.05','display','upright middle right',"P'/P-Q'/Q")
inventory('006.B.06','deletion','first denominator of separate fragment','Q overwritten by P')
inventory('006.B.07','display','upright middle left','(xy) raised joined mark = ...')
inventory('006.B.08','display','upright lower left',"(f/g)'=(f'g-g'f)/g²")
inventory('006.B.09','deletion','general quotient numerator','candidate P prime beneath f')
inventory('006.B.10','display','upright expanded derivative quotient',"(P''Q+P'Q'-P'Q'...)/Q³")
inventory('006.B.11','deletion','expanded numerator first product','P prime Q prime')
inventory('006.B.12','deletion','expanded numerator second product','P prime Q prime')
inventory('006.B.13','deletion','expanded numerator before Q double-prime P','overwritten candidate plus')
inventory('006.B.14','deletion','factor after first closing parenthesis','uncertain target of diagonal on Q raised 2')
inventory('006.B.15','deletion','expanded numerator after coefficient 2','Q crossed locally')
inventory('006.B.16','display','upright lower fraction',"(P''Q²-Q''PQ-2P'QQ'+2PQ'²)/Q³")
inventory('006.B.17','drawing','under right-hand part of lower fraction rule','second ruled stroke')
inventory('006.B.18','display','upright lowest fragment',"2p²Q²(-Q'/Q+")
inventory('006.B.19','deletion','across complete opposite-direction layer','two long diagonal cancellation strokes',True)
inventory('006.B.20','display','top of opposite-direction layer','det matrix; dash; ad-bc; inversible',True)
inventory('006.B.21','deletion','determinant first cell','candidate d or b after a',True)
inventory('006.B.22','display','first opposite-direction pair','delta(e1 e(d-2)); vertical equals; delta(a eta)',True)
inventory('006.B.23','deletion','end of first opposite-direction upper line','=e_d',True)
inventory('006.B.24','display','second opposite-direction pair','delta(e1 f(d-2)); vertical equals; b alpha...',True)
inventory('006.B.25','deletion','after minus in second pair','f overwritten by e',True)
inventory('006.B.26','display','third opposite-direction pair','delta(f1 e(d-2)); vertical equals; delta(c eta)',True)
inventory('006.B.27','text','below third pair','etc',True)
inventory('006.B.28','text','four physical lines of opposite-direction prose','On en tire ... comb. lin ... entiers fonctions ...',True)
inventory('006.B.29','deletion','second listed product in prose','candidate f beneath e',True)
inventory('006.B.30','display','last opposite-direction pair','delta(e1 xi); incomplete 2≤i≤; lower coefficient line',True)
inventory('006.B.31','deletion','last upper line before x(i-1)','candidate delta',True)
inventory('006.B.32','deletion','first coefficient in final lower line','candidate S beneath s',True)
inventory('006.B.33','text','lower-left of On in rotated orientation; full-scan (968,603)','detached point candidate',False,'undetermined hand')
inventory('006.B.34','text','full scan lower-left corner; comment only','archive sheet number 5',False,'undetermined hand')

unresolved=[]
for item in d:
 if item['C_doubt_status']=='retained' or item['id'] in ['B006-16','B006-49']:
  unresolved.append(dict(location=item['location'],reading=item['reading'],alternatives=(['d','b'] if item['id']=='B006-24' else ['as explicitly delimited or qualified in reading.tex']),confidence=item['confidence'],reason=item['evidence'],crop=item['readers_crop']))
report=dict(scan=6,reader='B',start_utc='2026-11-20 10:24:11 UTC',end_utc='2026-11-20 10:40:47 UTC',full_image_viewed=True,halves_viewed=True,complete_visual_read=True,
 image_view_audit={'whole':1,'half_a':1,'half_b':1,'crop_views':18,'full_dimensions':[1231,1680],'half_dimensions':[1231,920],'half_a_origin':[0,0],'half_b_origin':[0,760],'order':'UTC start; packet, brief and notation; whole scan; half a; half b; eighteen single crop views. No image reopened.'},
 differences=d,doubts=unresolved,inventory=inv,
 notes=[
 'The sheet has upright quotient/product calculations and an opposite-direction calculation crossed by two long diagonals. There is no manuscript page number, title, or date visible. Archive 5 is recorded in a comment.',
 'H describes the two layers and overall crossed state in its note. Those descriptions and the headings Couche barrée... and Couche tête-bêche... are apparatus, not manuscript words. No difference is charged for the overall cancellation state or these captions.',
 'H emphasis/preamble macros and purely equivalent TeX syntax are not charged as reading differences. H’s literal terminal punctuation is listed separately because no corresponding endpoint marks are visible; the root can identify these as editorial connective punctuation if its collation policy so directs.',
 'The active expressions end at P( and at 2p²Q²(-Q′/Q+. The condition ends at 2≤i≤. Their open ends are retained.',
 'The prose has e_{d-1} and f_{d-2}. Both local terminal shapes were read from the enlargement, without changing either to the recurring d-2 of the preceding calculations.',
 'The product exponent remains qualified with primary 2 and alternative two primes. Derivative context prompted inspection but did not settle the joined written form.',
 'The second ruled stroke under the simplified fraction is reproduced as a line. No emphasis or mathematical meaning is assigned to it.',
 'A detached round point near full-scan (968,603) is retained as a qualified shape. Its semantic role, hand and layer membership remain unresolved.',
 'No author-written phrase expressing uncertainty was identified. The uncertainty markers in reading.tex are editorial readings of crowded ink.',
 'The individual local cancellations remain visible inside the transcription’s overall cancellation of the opposite-direction layer.',
 'The one crop of the first prose line clips part of the descending context at its right end; its target predecessor remains doubtful. The complete shape was visible in half a. Some neighboring tall strokes at crop edges are context belonging to the overlapping layer; no clipped form was treated as unreadable solely because of the crop edge.',
 'No OCR, recognition, external sources, other pages, other readers, or delegation were used. The complete page was read visually line by line; the whole and each supplied half were opened once each.'
 ],
 notation=[
 {'location':'upright quotient calculations','sign':'P, Q; separate raised prime strokes and bent raised 2 forms','latex':r'P,Q,P\prime,Q\prime,Q^2'},
 {'location':'product identity','sign':'joined raised form above (xy)','latex':r'(xy)^{\unsure{2|\prime\prime}}'},
 {'location':'lowest upright fragment','sign':'small p bowl before taller Q','latex':r'2p^2Q^2'},
 {'location':'opposite-direction pairs after a and c','sign':'shouldered eta with hooked long descender','latex':r'\eta'},
 {'location':'four opposite-direction pair connectors','sign':'two parallel short vertical strokes','latex':r'\rotatebox{90}{$=$}'},
 {'location':'opposite-direction prose','sign':'abbreviated comb. lin and coeff without a terminal point','latex':'comb. lin; coeff'},
 {'location':'final opposite-direction lower member','sign':'s and crossed t, indexed e and f','latex':r'se_i+tf_i'},
 {'location':'rotated determinant after matrix','sign':'single short horizontal stroke','latex':'-'},
 {'location':'detached point near On','sign':'small round point; role undetermined','latex':r'\unsure{\cdot}'}
 ],check_events=[],crops=json.loads((r/'crops.json').read_text()),
 brief_feedback=[
 'The status of a long whole-layer cancellation crossing a later Q raised 2 is genuinely ambiguous. The brief allows doubt but gives no dedicated syntax for uncertainty about the target or layer of a cancellation; alternatives in unsure were used.',
 'H’s terminal punctuation in condensed displays can be read as editorial connective punctuation. The brief explicitly exempts descriptive captions but does not specify this punctuation case; each visible reading comparison is reported so the root can classify it.',
 'The complete first prose line crosses the opposite-direction product formula. My single crop did not retain every descending contextual stroke at one edge; I did not make a prohibited second enlargement and retained the affected predecessor doubt.'
 ])
(r/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'differences':len(d),'C_actual_doubts':sum(x['C_doubt_status'] is not None for x in d),'C_resolved':sum(x['C_doubt_status']=='resolved' for x in d),'C_retained':sum(x['C_doubt_status']=='retained' for x in d),'inventory':len(inv),'unresolved':len(unresolved)},ensure_ascii=False))
