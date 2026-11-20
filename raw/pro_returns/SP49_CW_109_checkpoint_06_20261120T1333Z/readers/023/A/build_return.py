from pathlib import Path
import json, re, difflib
P=Path('/workspace/scratch/6d55c8c3e5a7/work/readers/023/A')
I=Path('/workspace/scratch/6d55c8c3e5a7/work/inputs/023')
S='/workspace/scratch/6d55c8c3e5a7/source/SP49_CW_109_scans/'
whole=S+'H109-02_109_scan023.jpg'; a=S+'H109-02_109_scan023_a.jpg'; b=S+'H109-02_109_scan023_b.jpg'
original=(I/'C.tex').read_text()
reading=original
reading=reading.replace(r'\deleted{\unsure{8|9}}3',r'\deleted{8}3')
reading=reading.replace(r'\unsure{separable|squarable}',r'squarable')
reading=reading.replace(r'C^0\longrightarrow {C\prime}^0',r'C^{\unsure{0|o}}\longrightarrow {C\prime}^{\unsure{0|o}}') if False else reading
reading=reading.replace(r"C^0\longrightarrow {C'}^0",r"C^{\unsure{0|o}}\longrightarrow {C'}^{\unsure{0|o}}")
old_margin=r"\margin{\tikz[baseline=(a.base)]{\node[align=left,inner sep=2pt](a){l-3 don't\\$\times 2$}; \draw (a.west) -- (a.north west) -- (a.north east);}}"
new_margin=r"""\margin{\tikz[baseline=(a.base)]{
  \node[anchor=west,inner sep=0pt](a) at (0,0){l-3 don't};
  \node[anchor=north east,inner sep=0pt] at ([yshift=-1pt]a.south east){$\times 2$};
  \draw ([xshift=-3pt,yshift=-5pt]a.west)
    .. controls ([xshift=-6pt,yshift=0pt]a.west) and ([xshift=-3pt,yshift=6pt]a.north west)
    .. ([xshift=-1pt,yshift=7pt]a.north west)
    -- ([xshift=-.5cm,yshift=7pt]a.north east);
  \draw ([xshift=-.35cm,yshift=8pt]a.north east) -- ([xshift=.03cm,yshift=10pt]a.north east);
}}"""
assert old_margin in reading
reading=reading.replace(old_margin,new_margin)
old_arrow=r"\margin{\tikz[baseline]{\draw[->] (0,0) .. controls (-.5,.3) and (-.55,.8) .. (.32,.85);}}"
new_arrow=r"\reversemarginpar\margin{\tikz[baseline]{\draw[->] (0,0) .. controls (-.5,.3) and (-.55,.8) .. (.32,.85);}}\normalmarginpar"
assert old_arrow in reading
reading=reading.replace(old_arrow,new_arrow)
reading=reading.replace('% Arrow beside 184 points to the space before 185.','% Left-margin arrow beside 184 curves around 185 and points to the space above 185.')
reading=reading.replace(r'\deleted{\unsure{a}}whatever\deleted{\unsure{s}}',r'\raisebox{-.45ex}{\deleted{\unsure{a}}}whatever\raisebox{-.45ex}{\deleted{\unsure{s}}}')
reading=reading.replace(r'\unsure{``}is it',r'\unsure{``|`}is it')
reading=reading.replace(r'\deleted{\unsure{)|?}}',r'\deleted{)}')
# Retain the original paragraph blocks; encode the visible reference column.
refs=['p156','158','159','160','p161','162','163','164','p.165','166','p167','p.169','p.171','p.174','p177','p.180','181','185','184','p186','p.188','189','190']
paras=reading.split('\n\n')
out=[]
for para in paras:
    if para.startswith('\\scanpage'):
        out.append(para+'\n\\begingroup\n\\setlength{\\parindent}{0pt}')
        continue
    if para.startswith('% archive'):
        out.append(para)
        continue
    matched=False
    for ref in refs:
        if para.startswith(ref+' '):
            anchor=''
            if ref=='158': anchor=r'\tikz[remember picture,overlay]{\coordinate (scan23-rule-top) at (0,0);}'+'\n'
            para=anchor+r'\hangindent=1.2cm\hangafter=1 '+r'\makebox[1.2cm][l]{'+ref+'}'+para[len(ref)+1:]
            matched=True
            break
    if not matched:
        para=r'\hangindent=1.2cm\hangafter=1 \hspace*{1.2cm}'+para
    if '\n% archive sheet number:' in para:
        body, comment=para.split('\n% archive sheet number:',1)
        para=body+'\n% archive sheet number:'+comment
    out.append(para)
reading='\n\n'.join(out)
rule_drawing=r"""
% Long physical rules: the left rule separates the reference column from the text;
% the right rule crosses the long corrections near their right end.
\tikz[remember picture,overlay]{\coordinate (scan23-rule-bottom) at (0,0);}
\figure{\begin{tikzpicture}[remember picture,overlay]
  \coordinate (scan23-rule-bottom-left) at (scan23-rule-top |- scan23-rule-bottom);
  \draw ([xshift=1.08cm,yshift=1.6ex]scan23-rule-top)
    -- ([xshift=1.08cm,yshift=-1ex]scan23-rule-bottom-left);
  \draw ([xshift=.93\linewidth,yshift=1.6ex]scan23-rule-top)
    -- ([xshift=.93\linewidth,yshift=-1ex]scan23-rule-bottom-left);
\end{tikzpicture}}
\endgroup
"""
reading=reading.rstrip()+'\n'+rule_drawing
(P/'reading.tex').write_text(reading)

crops={n:(half,box,reason) for n,half,box,reason in json.loads((P/'unresolved_after_halves.json').read_text())}
def loc(crop=None,source=None,bbox=None):
    if crop:
        half,box,_=crops[crop]
        return {'crop':str(P/'crops'/f'{crop}.jpg'),'source':a if half=='a' else b,'bbox':box}
    return {'crop':None,'source':source,'bbox':bbox}
changes=[]
def change(id,place,c,read,kind,evidence,confidence='high',crop=None,source=None,bbox=None,code_reference=None):
    v={'id':id,'place':place,'c':c,'h':None,'reading':read,'diff_c':True,'diff_h':False,'kind':kind,'marked_in_H':False,'confidence':confidence,'evidence':evidence,**loc(crop,source,bbox)}
    if code_reference:v['code_reference']=code_reference
    changes.append(v)
change('first-reference-digit','p156, first reference',r'\deleted{\unsure{8|9}}3',r'\deleted{8}3','misread symbol or index','The older small sign has an upper loop remnant and a separately closed lower loop. The lower enclosure does not end as an open descending 9 tail. The larger 3 overwrites its upper right.','medium','01')
change('squarable','160 mid page',r'\unsure{separable|squarable}','squarable','misread word','After s there is a closed small q bowl with a long descender returning upward into u; there is no independent e followed by a p stem. The remaining a-r-a-b-l-e is clear.','high','03')
change('round-superscripts','p167 line 10, domain and codomain superscripts',r"f^{\unsure{0|o}}\colon C^0\longrightarrow {C'}^0",r"f^{\unsure{0|o}}\colon C^{\unsure{0|o}}\longrightarrow {C'}^{\unsure{0|o}}",'misread symbol or index','Each object has its own small closed, slightly oval superscript. Neither of these two outlines supplies an identifying feature separating handwritten zero from lowercase o. They are marked independently rather than inheriting an unmarked first candidate from the f occurrence.','medium','06')
change('right-note-geometry','right margin between p169 and p171',old_margin,new_margin,'drawing or diagram','The times 2 is below the right part of the first line, under don\'t. The upper-left enclosure has a rounded turn, its main horizontal ends before the right end of the text, and a detached short oblique rule follows after a gap.','high','07')
change('left-arrow','beside 184 and 185',old_arrow,new_arrow,'insertion or placement','The curve lies entirely in the left reference margin: it rises from the side of 184, bends around the left of 185, and ends with a rightward head in the gap above 185. Default right-margin placement would reverse its physical side.','high',source=b,bbox=[73,425,206,581])
change('lowered-cancelled-clusters','p188 l-9, immediately before and after whatever',r'\deleted{\unsure{a}}whatever\deleted{\unsure{s}}',r'\raisebox{-.45ex}{\deleted{\unsure{a}}}whatever\raisebox{-.45ex}{\deleted{\unsure{s}}}','insertion or placement','Both crossed clusters sit distinctly below the body of whatever. Their letters remain doubtful; the adjustment records their lowered positions and does not promote the buried readings.','high','12')
change('last-opener-alternatives','190 l-6, before is it',r'\unsure{``}',r'\unsure{``|`}','other','The heavy raised mark has a slight lower notch but is fused. A joined pair of quote strokes remains favored; a single thick curved quote cannot be excluded after the one crop.','low','15')
change('cancelled-parenthesis','190 l-6, after manyfold',r'\deleted{\unsure{)|?}}',r'\deleted{)}','misread symbol or index','A continuous right-bowing arc runs from the upper tip to the lower left turn. Angular oblique cancellation strokes cross it at the top and bottom. There is no separate surviving question-mark dot.','high','16')
left_rule=r'\draw ([xshift=1.08cm,yshift=1.6ex]scan23-rule-top) -- ([xshift=1.08cm,yshift=-1ex]scan23-rule-bottom-left);'
right_rule=r'\draw ([xshift=.93\linewidth,yshift=1.6ex]scan23-rule-top) -- ([xshift=.93\linewidth,yshift=-1ex]scan23-rule-bottom-left);'
change('long-left-rule','between the reference and correction columns, 158 through 190','',left_rule,'drawing or diagram','One long near-vertical line separates page references from the correction text. It begins below the first entry near 158 and runs nearly to the bottom. Paragraph text is retained; standard boxes and hanging indents make the observed reference column explicit.','high',source=whole,bbox=[226,90,244,2320],code_reference='reading.tex: scan23-rule-top anchor, reference-column boxes, and first draw in final figure')
change('long-right-rule','near right edge, from height of 158 through the final correction','',right_rule,'drawing or diagram','A second long near-vertical rule lies near the right edge and is crossed by several long text lines. It is separate from the small bracket belonging to the l-3 marginal note.','high',source=whole,bbox=[1505,90,1522,2325],code_reference='reading.tex: scan23-rule-top / scan23-rule-bottom anchors and second draw in final figure')

D=[]
def doubt(place,c,read,resolved,evidence,confidence='high',crop=None,source=None,bbox=None):
    D.append({'place':place,'c':c,'reading':read,'resolved':resolved,'confidence':confidence,'evidence':evidence,**loc(crop,source,bbox)})
doubt('p156 first reference',r'\deleted{\unsure{8|9}}3',r'\deleted{8}3',True,'The separate closed lower loop and upper loop remnant favor 8; overwritten state is certain, buried upper contour less complete.','medium','01')
doubt('160 mid page',r'? spelling of ``\unsure{separable|squarable}\'\'.',r'? spelling of ``squarable\'\'.',True,'A q bowl and descender followed by u decide the word; the question mark and spelling-of qualification remain literal.','high','03')
doubt('p167 line 10, superscript on f',r'f^{\unsure{0|o}}',r'f^{\unsure{0|o}}',False,'The small closed oval is compatible with both 0 and o; the surrounding partial assertion gives no written definition.','medium','06')
doubt('p167 line 10, superscript on first C',r'C^0',r'C^{\unsure{0|o}}',False,'This independently viewed small oval is not decisively numeric or alphabetic.','medium','06')
doubt('p167 line 10, superscript on primed C',r"{C'}^0",r"{C'}^{\unsure{0|o}}",False,'The round sign after a separate prime remains compatible with 0 and o.','medium','06')
doubt('p167 line 10, final cancelled sign',r'\deleted{\unsure{?}}',r'\deleted{\unsure{?}}',False,'Crossing strokes obscure the upper portion and lower continuation. A question mark remains the best attempted reading, but no independent dot is securely separable. Cancellation extent is clear.','low','06')
doubt('p188 l-9, first cancelled cluster',r'\deleted{\unsure{a}}',r'\raisebox{-.45ex}{\deleted{\unsure{a}}}',False,'A small closed loop survives but the crossing strokes do not allow a secure letter; a remains plausible. The cluster is lowered beside whatever.','low','12')
doubt('p188 l-9, second cancelled cluster',r'\deleted{\unsure{s}}',r'\raisebox{-.45ex}{\deleted{\unsure{s}}}',False,'The black zigzag cluster after the final r leaves s plausible but not securely legible. The full little cluster is cancelled and sits low.','low','12')
doubt('p188 line 5, raised cancelled mark',r'\deleted{\unsure{``}}',r'\deleted{\unsure{``}}',False,'Two upper peaks and lower lobes could belong to an opening quote pair, but the crossing and heavy fill prevent certainty.','low','13')
doubt('190 l-6, opening mark',r'\unsure{``}',r'\unsure{``|`}',False,'Raised fused curved patch; the shallow notch suggests two strokes but permits one heavy stroke.','low','15')
doubt('190 l-6, cancelled closing mark',r'\deleted{\unsure{)|?}}',r'\deleted{)}',True,'The continuous bow is a closing parenthesis; independent diagonal cancellation strokes account for the angular additions. No live replacement closer is supplied.','high','16')
doubt('p167 line 10, prime on codomain',r"{C'}^0",r"{C'}^{\unsure{0|o}}",True,'A distinct raised oblique stroke precedes the last round superscript; it is not part of the C body. The round sign itself remains separately doubtful.','high','06')
doubt('p167 line 10, arrow between objects',r'\longrightarrow',r'\longrightarrow',True,'A continuous shaft finishes in a clear rightward head.','high','06')
doubt('p186 reference 10 to 11',r'(10\mathord{\to}11)',r'(10\mathord{\to}11)',True,'The short mark after 10 has a rightward arrowhead before 11; round parentheses enclose the reference.','high',source=b,bbox=[356,591,475,666])
doubt('right marginal note, sign before 2',r'\times 2',r'\times 2',True,'Two oblique strokes cross before 2. The sign is neither a plus nor the first stroke of a word.','high','07')
doubt('p167 line 10, underline',r'\uuline{is}',r'\uuline{is}',True,'Two distinct horizontal rules lie below is.','high','06')
doubt('p186 line -2, underline',r"\uline{aren't}",r"\uline{aren't}",True,'One rule runs beneath the complete contraction from a through t.','high',source=b,bbox=[448,856,603,921])
doubt('189 l-6, underline',r'\uline{the}',r'\uline{the}',True,'One short rule is confined to the word the.','high',source=b,bbox=[1221,1037,1322,1109])
doubt('190 l-6, two different spellings','manyfold; manifold','manyfold; manifold',True,'The parenthetical form has the descending y; the later live form has i. They are deliberately distinct on the page.','high','16')
doubt('p169 line 7, recommendation',"better ``in all that follows''","better ``in all that follows''",True,'The qualifier better and all five quoted words are legible; no strengthening of the recommendation is made.','high',source=b,bbox=[449,26,925,88])
doubt('184 line -15, alternative wording',"``reserved for'' or ``restricted to''","``reserved for'' or ``restricted to''",True,'Both quoted wordings and the intervening or are legible. They remain alternatives.','high',source=b,bbox=[425,532,999,598])
doubt('p186 line -11, assessment and alternatives',"``is more than needed'' doesn't really seem right - do you mean ``is all that is needed'' or ``is more than is needed'' perhaps.","``is more than needed'' doesn't really seem right - do you mean ``is all that is needed'' or ``is more than is needed'' perhaps.",True,'The two-line note visibly retains doesn\'t really seem right, the question-form do you mean, both suggested formulations, and perhaps.','high',source=b,bbox=[328,668,1565,798])
doubt('p188 l-9, qualifier','presumably','presumably',True,'The word before the opening quotes ends in -bly with a descending y.','high',source=b,bbox=[1219,922,1382,989])
doubt('p188 line 5, missing-copy statement','end of line is missing on copy.','end of line is missing on copy.',True,'The line states this limitation; the low compact terminal mark after copy is retained as a period.','high','14')
doubt('190 l-6, spelling qualification and insertion',r'manifold is \inserted{the} more correct spelling',r'manifold is \inserted{the} more correct spelling',True,'The word the sits above the gap after is, and the lower caret locates it before more. The comparative more correct is retained.','high','17')

remaining=[
 {'place':'p167 line 10, f superscript','reading':r'f^{\unsure{0|o}}','alternatives':'0 | o','confidence':'medium','reason':'Closed oval does not independently identify numeric zero or lowercase o.'},
 {'place':'p167 line 10, first C superscript','reading':r'C^{\unsure{0|o}}','alternatives':'0 | o','confidence':'medium','reason':'This separate oval remains ambiguous after the formula crop.'},
 {'place':'p167 line 10, primed C superscript','reading':r"{C'}^{\unsure{0|o}}",'alternatives':'0 | o','confidence':'medium','reason':'The prime is clear, but the following round sign is not independently distinguishable.'},
 {'place':'p167 line 10, cancelled final sign','reading':r'\deleted{\unsure{?}}','alternatives':'? is the only attempted textual reading','confidence':'low','reason':'Cancellation obscures the interior; the visible hook is insufficient to resolve it.'},
 {'place':'p188 l-9 before whatever','reading':r'\raisebox{-.45ex}{\deleted{\unsure{a}}}','alternatives':'a is tentative','confidence':'low','reason':'Crossed loop remains buried.'},
 {'place':'p188 l-9 after whatever','reading':r'\raisebox{-.45ex}{\deleted{\unsure{s}}}','alternatives':'s is tentative','confidence':'low','reason':'A black zigzag cluster does not securely isolate the old letter.'},
 {'place':'p188 line 5 before end','reading':r'\deleted{\unsure{``}}','alternatives':'opening quote pair is tentative','confidence':'low','reason':'The raised double-lobed cluster is crossed and filled.'},
 {'place':'190 l-6 before is it','reading':r'\unsure{``|`}','alternatives':'double opening quotes | single opening quote','confidence':'low','reason':'The fused raised mark lacks a decisive separation.'}
]
inv=[]
def item(kind,pos,first,hand='unnamed handwritten hand'):
    inv.append({'sheet_kind':'list','hand':hand,'element':f'{len(inv)+1:02d}','kind':kind,'position':pos,'first_words_or_objects':first,'transcribed':'yes'})
item('text','top line, reference p156','p156 line 3 of §67; hadn\'t')
item('deletion','within first line reference, under/left of live 3','cancelled 8')
item('text','158 line 10','haven\'t; characterisation')
item('text','indented continuation below 158','replace for considering by to consider')
item('text','159 line 12','developing')
item('text','same row, 159 line -17','characterisation')
item('text','160 mid page','? spelling of squarable')
item('text','row below 160','l.-6 shouldn\'t')
item('text','p161 line 8','we had better change it now or never')
item('deletion','p161 line 8 before replacement','now or never, including quotation span')
item('text','indented line below p161','line 17 we\'ve got')
item('text','162 line -15','standard')
item('deletion','same row after standard','line')
item('text','163 line -1','won\'t')
item('text','164 line -11','waiting to get')
item('text','p165 line 5','developed')
item('text','same row, line -16','standard')
item('text','same row, line -8','its')
item('text','parenthetical continuation below p165','it\'s is only used as short for it is')
item('text','166, two-line general point','non usually takes a - after it; non-empty; non-abelian')
item('text','indented row below general point','line -12 isn\'t')
item('text','p167 line 10','so is, followed by the component map')
item('text','nested underline in p167 entry','double underline under is')
item('text','inline formula in p167 entry',r'f^{\unsure{0|o}}\colon C^{\unsure{0|o}}\longrightarrow {C\prime}^{\unsure{0|o}}')
item('deletion','after the primed codomain in p167 entry','tentative question mark')
item('text','p169 line 7','better in all that follows')
item('margin note','right margin beside p169 and above p171','l-3 don\'t, with times 2 below right')
item('drawing','around upper and left sides of right marginal note','rounded upper-left bracket/rule')
item('drawing','just beyond upper-right end of the note bracket','detached short rising rule')
item('text','p171 line 12','don\'t')
item('text','same row, l.13','standard')
item('text','same row, l-11','envisaged')
item('text','same row, l-5','isn\'t')
item('text','p174 line 4','commutes with')
item('text','p177 line 9','left hand side')
item('text','same row, line 11','proving')
item('text','same row, line -6 and also -5','isn\'t')
item('text','p180 line 7 and also -15','wasn\'t')
item('text','181 line 6','couldn\'t')
item('text','same row, line 8','inappropriateness.')
item('text','same row, line 9','losing')
item('text','181 continuation, line 14','developed')
item('text','same row, line -14','handful')
item('text','same row, line -5','doesn\'t')
item('text','185 line 9, physically preceding 184','couldn\'t')
item('text','same row, l.16','doesn\'t')
item('text','184 line -15','reserved for or restricted to')
item('drawing','left margin curving around 185 from near 184','upward and rightward curved arrow')
item('text','p186 reference line (10→11)','standard')
item('text','same row, l.13','wasn\'t')
item('text','same row, l18','isn\'t')
item('text','p186 line -11, two-line note','is more than needed; doesn\'t really seem right; two alternatives; perhaps')
item('text','p186 line -2, two-line correction','got around to defining what those homotopy intervals\' which aren\'t weak should be!')
item('deletion','p186 line -2 before live what','what')
item('text','nested underline in p186 line -2','aren\'t')
item('text','p188 line 2','isn\'t')
item('text','same row, line 10','weeks')
item('text','same row, l14','didn\'t')
item('text','same row, l-9','presumably; whatever for')
item('deletion','lowered immediately before whatever','tentative a')
item('deletion','lowered immediately after whatever','tentative s')
item('text','p188 line 5, next row','end of line is missing on copy.')
item('deletion','raised before end in p188 line 5','tentative opening quote pair')
item('text','189 l.17','isn\'t; doesn\'t')
item('text','same row, l-13','commuting with')
item('text','same row, l-6','the same objects')
item('text','nested underline in 189 l-6','the')
item('text','190 l-6 final note','end of line; is it manifold; manyfold; manifold is the more correct spelling')
item('deletion','after manyfold in final note','closing parenthesis')
item('insertion','above gap between is and more in final note','the, with caret below')
item('drawing','long left boundary from near 158 to below 190','vertical rule between references and main corrections')
item('drawing','long right boundary from height of 158 to below 190','near-vertical rule crossed by long entries')
item('margin note','lower-left archive corner; comment only','archive sheet number 22','another unnamed hand, apparently pencil')

notation=[
 {'sign':r'\S67','location':'first reference','reading':r'\S67','evidence':'Two vertically linked curls form the section sign before 67; crop 01.'},
 {'sign':'0 / o','location':'all three p167 superscripts','reading':r'f^{\unsure{0|o}}, C^{\unsure{0|o}}, {C\prime}^{\unsure{0|o}}','evidence':'Each separate small closed outline was inspected in crop 06; all three are explicitly marked.'},
 {'sign':"C'",'location':'p167 codomain','reading':"C'",'evidence':'Ordinary single-stroke C and a separate raised slant before the round superscript, crop 06.'},
 {'sign':r'\longrightarrow; \to','location':'p167 map and p186 line-number reference','reading':r'\longrightarrow; \to','evidence':'Both shafts end in right-pointing heads; formula crop 06 and lower half.'},
 {'sign':r'\times 2','location':'right marginal note','reading':r'\times 2','evidence':'Two crossed diagonal strokes before 2; crop 07; phrase is below the right side of don\'t.'},
 {'sign':'underlines','location':'p167, p186 line -2, 189 l-6','reading':r"\uuline{is}; \uline{aren't}; \uline{the}",'evidence':'Two strokes under is in crop 06; a single complete-word rule under each later phrase in the lower half.'},
 {'sign':'contraction apostrophes','location':'181 line 6 and 185 line 9 / l.16','reading':"couldn't; couldn't; doesn't",'evidence':'Crops 08–10 separately locate the apostrophe after n and before t; apparent short raised dashes at the close are quote components, not additional punctuation.'},
 {'sign':'cancelled parenthesis','location':'190 after manyfold','reading':r'\deleted{)}','evidence':'Crop 16 separates the long bowed closer from its angular crossing strokes. No live closing parenthesis is invented.'},
 {'sign':'opening quotation alternatives','location':'190 before is it','reading':r'\unsure{``|`}','evidence':'Fused heavy raised mark with a shallow lower notch; crop 15.'},
 {'sign':'l.-6','location':'below 160','reading':'l.-6','evidence':'Crop 04 shows a low point after the looped l; the short minus intersects the long vertical rule.'},
 {'sign':'cancelled words','location':'p161 line 8; p162 after standard; p186 line -2','reading':r"\deleted{``now or never''}; \deleted{line}; \deleted{what}",'evidence':'Crop 05 confirms now, or, never beneath a broad zigzag; half a confirms line; crop 11 preserves a w-like start, h ascender, a bowl and final t under the cancellation. Extents are clearer than some buried letter contours.'}
]
report={'scan':23,'reader':'A','model':'GPT-6 Astra Pro','effort':'not exposed','viewed':[whole,a,b],
'layout':'One densely written English correction list in a single unnamed black-ink hand. Page references form a narrow left column, separated from the main writing by a long vertical rule beginning near 158; a second long rule lies near the right edge. The first p156 entry sits above the starts of these rules. Most corrections occupy single rows, with continuations and longer two-line comments. There are no standalone mathematical displays or commutative diagrams. The p167 map is inline. A small bracketed note l-3 don\'t with times 2 is in the right margin between p169 and p171; its upper rule ends in a detached dash. A curved arrow is in the LEFT reference margin around 185 and 184. Physical order remains 185 then 184. Cancellations occur in the first reference, p161, p162, p167, p186, p188 and p190; the final the is interlinear with a caret. A pencilled archive 22 is at bottom left. Two circular right-edge impressions and clipped dark material at the scan edge carry no readable page text.',
'changes':changes,'c_doubts':D,'remaining_doubts':remaining,'inventory':inv,
'notes':[
'English corrections cite typescript pages 156 through 190 and line numbers. These are references, not pagination of the note itself. No title, date, signature or stated page count appears. The archive corner 22 is recorded only as a comment.',
'The list chiefly proposes spelling and phrasing changes, including characterisation, developing, standard and contractions. At 160 the literal queried spelling is squarable, introduced by ? spelling of.',
'The p166 general point says non usually takes a hyphen, giving non-empty and non-abelian. The qualified usually is retained.',
'The isolated p167 assertion begins so is and gives a component-map notation. Its antecedent is absent from this page, and the three round superscripts remain individually doubtful between zero and lowercase o.',
'At p169 the note says better in all that follows. At 184, reserved for and restricted to remain alternatives. The arrow is drawn in the left margin and no reordering of the physical entries is made.',
'At p186 line -11 the writer says is more than needed does not really seem right and asks whether either of two fuller formulations is intended, ending perhaps. The line -2 quotation contains a deleted what before live what, inner quotes around homotopy, and a single quote after intervals; the transcription preserves those asymmetric delimiters.',
'At p188, presumably qualifies whatever for, with two small lowered cancelled clusters; another entry says the end of a line is missing on the copy.',
'The final note asks is it manifold, contrasts manyfold, and says manifold is the more correct spelling. The the is inserted above the gap after is; the old closing parenthesis is cancelled, so no live replacement delimiter has been supplied.',
'Inventory coverage: each correction/list entry, multi-line explanatory block, inline formula, nested cancellation, underline, interlinear insertion, marginal note and authored rule/arrow has its own row. There are no omitted diagrams or displays.'
],
'math_checks':[],
'notation':notation,
'abbreviations':[
 {'form':'p / p.','expansion':'page (interpretation only)','place':'reference column'},
 {'form':'l / l.','expansion':'line (interpretation only)','place':'short line references, including the right marginal note'},
 {'form':'e.g','expansion':'for example (interpretation only)','place':'166 general point, both occurrences'},
 {'form':'i.e','expansion':'that is (interpretation only)','place':'190 parenthetical spelling note'},
 {'form':'§','expansion':'section (interpretation only)','place':'p156 first reference'}
],
'brief_feedback':'Whole image was displayed exactly once, then each supplied half exactly once. The unresolved list was written before cropping. Seventeen crops were generated with the supplied crop.py, logged and individually displayed once; no whole half was enlarged or reopened. No OCR, recognition library, external source, other page, other reader output, compilation or added agent was used. H is descriptive only: there are no H collation rows, and all change rows have h=null/diff_h=false. The isolated component map has no antecedent or assumptions here, so I make no substantive mathematical-check or proof claim; math_checks is intentionally empty. Reference-column boxes and two anchored rule strokes record visible layout without changing the paragraph order. Their TeX was checked statically only, not rendered.'}
(P/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
(P/'literal_diff.txt').write_text(''.join(difflib.unified_diff(original.splitlines(True),reading.splitlines(True),fromfile='C.tex',tofile='reading.tex')))
print(json.dumps({'changes':len(changes),'c_doubt_decisions':len(D),'remaining_doubts':len(remaining),'inventory':len(inv),'crops':len(crops)},indent=2))
