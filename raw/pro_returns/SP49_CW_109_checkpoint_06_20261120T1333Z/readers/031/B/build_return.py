from pathlib import Path
import json, re, difflib

ROOT = Path('/workspace/scratch/6d55c8c3e5a7')
OUT = ROOT / 'work/readers/031/B'
INP = ROOT / 'work/inputs/031'
meta = json.loads((INP / 'metadata.json').read_text())
frozen = json.loads((OUT / 'unresolved_frozen.json').read_text())
loci = {r['id']: r for r in frozen['loci']}
C = (INP / 'C.tex').read_text()
body = C
changes = []

def evidence(crop=None, source=None, bbox=None):
    if crop:
        z = loci[crop]
        return {'crop': z['crop'], 'source': z['source'], 'bbox': z['bbox']}
    return {'crop': None, 'source': source, 'bbox': bbox}

def change(cid, place, old, new, kind, why, crop=None, source=None, bbox=None,
           confidence='high', apply=True):
    global body
    row = {'id': cid, 'place': place, 'c': old, 'h': None, 'reading': new,
           'diff_c': True, 'diff_h': False, 'kind': kind, 'marked_in_H': False,
           'confidence': confidence, 'evidence': why,
           **evidence(crop, source, bbox)}
    changes.append(row)
    if apply:
        n = body.count(old)
        assert n == 1, (cid, n, old)
        body = body.replace(old, new, 1)
    return row

ref403 = r"\tikz[baseline=(ref403B.base)]{\node[inner sep=0pt] (ref403B) {l.4};\fill ([xshift=-.15em,yshift=-.6ex]ref403B.base east) circle (.045ex);}"
old407 = r"\tikz[baseline=(old407B.base)]{\node[inner sep=0pt] (old407B) {\deleted{the}};\node[anchor=south west,inner sep=0pt] at ([xshift=.65em,yshift=.1ex]old407B.north west) {\inserted{its}};}"
as407 = r"\tikz[baseline=(as407B.base)]{\node[inner sep=0pt] (as407B) {\deleted{i}};\node[anchor=base west,inner sep=0pt] at (as407B.base west) {a};}s"
pp407 = r"\tikz[baseline=0pt,x=1ex,y=1ex]{\node[anchor=south,inner sep=0pt] at (.15,1.6) {\inserted{a p.p of}};\draw[line width=.45pt,line cap=round] (.15,.85)--(-.05,-.75) (-.02,-.35)--(.62,-.72);\path (-.25,0)--(.7,0);}"
ditto408 = r"\tikz[baseline=(ditto408B.base)]{\node[inner sep=0pt] (ditto408B) {''};\node[anchor=south,inner sep=0pt] at ([xshift=-.3em,yshift=.2ex]ditto408B.north) {$\uparrow$};}"
identical408 = r"\tikz[baseline=(identical408B.base)]{\node[inner sep=0pt] (identical408B) {``identical''};\fill ([xshift=3.3em,yshift=.5ex]identical408B.base east) circle (.045ex);}"
its409 = r"i\tikz[baseline=(old409B.base)]{\node[inner sep=0pt] (old409B) {\deleted{\unsure{s}}};\node[anchor=base west,inner sep=0pt] at (old409B.base west) {t};}s"
second410 = r"``\deleted{\unsure{Its|its}}\unsure{\deleted{''}|''}"
do412 = r"\tikz[baseline=(old412B.base)]{\node[inner sep=0pt] (old412B) {\deleted{\unsure{t}}};\node[anchor=base west,inner sep=0pt] at (old412B.base west) {d};}o"
line412 = r"l\tikz[baseline=(minus412B.base)]{\node[inner sep=0pt] (minus412B) {$-$};\fill ([xshift=.05em,yshift=-.7ex]minus412B.base) circle (.055ex);}14"
page416 = r"\tikz[baseline=(page416B.base)]{\node[inner sep=0pt] (page416B) {p 416};\fill ([xshift=.3em,yshift=.95ex]page416B.base east) circle (.045ex);}"
points420 = r"\hfill\tikz[baseline=0pt,x=1ex,y=1ex]{\fill (.12,.8) circle (.045);\fill (-.03,.48) circle (.035);}"
in422 = r"\tikz[baseline=0pt,x=1ex,y=1ex]{\node[anchor=south,inner sep=0pt] at (0,1.3) {\inserted{in}};\draw[line width=.4pt,line cap=round] (.12,.7)--(.08,-.8)--(.35,-.63);\path (-.15,0)--(.42,0);}"
its423 = r"\tikz[baseline=(its423B.base)]{\node[inner sep=0pt] (its423B) {``its''};\fill[black!55] ([xshift=4em,yshift=1.35ex]its423B.base east) circle (.035ex);}"

change('402-arrow6','402, second line, reference before hatted A',r'\unsure{$\downarrow$6|16}',r'$\downarrow$6','misread symbol or index','The sloping shaft ends in two upward-returning sides of a downward arrowhead; the following 6 is separate. The ordinary A has a roof and two lowered letters ab.',crop='01')
change('403-own','403 l.4, cancelled word after its',r'\deleted{\unsure{own}}',r'\deleted{own}','misread word','The cancelled word retains an initial closed o, the two low turns of w, and the final n shoulder. Both quotation groups stand outside this local cancellation.',crop='02',confidence='medium')
change('403-low-point','403 l.4, separate low point below numeral 4',r'l.4 ``its',ref403+r' ``its','omission','A small detached dark point lies below the 4, below its normal baseline. Its geometry is retained without calling it a stop.',crop='02')
change('404-sign5','404, reference before the last analogue',r'l.-5 ``analogue',r'l.\unsure{+|-}5 ``analogue','misread symbol or index','The reference contains a low point after l and a thick horizontal mark with a clear short downward central spur. Plus is the nearer shape; a hooked/retraced minus remains possible.',crop='04',confidence='medium')
change('405-didnt-opener','405 l-9, opener before didnt',r'l-9 ``didn\'t\'\''.replace('\\\'','\''),r'l-9 \unsure{``|`}didn\'t\'\''.replace('\\\'','\''),'misread symbol or index','The compact opener is one joined curved body with two rightward tips. Paired strokes and a single returned stroke cannot be separated securely; the closer is visibly paired.',crop='06',confidence='medium')
change('407-old-the','407 l-15, cancelled word and raised its',r'\deleted{\unsure{the|its}} \inserted{its}',old407,'misread word','A tall first upright and the following looped ascender support the under-word the. The replacement its is clear, higher and slightly right of the cancellation; that height is retained.',crop='08',confidence='medium')
change('407-overwritten-i','407 l-15, beginning of as',r'\deleted{\unsure{i}}as',as407,'deletion state (struck given live or live given struck)','The separate old i dot and short inner upright remain within the live a outline. The final s is shared. The old i and live a are therefore placed in one glyph space.',crop='09',confidence='medium')
change('407-raised-pp','407 l-15, a p.p of above the gap before relier',r'\inserted{a p.p of}',pp407,'insertion or placement','The small text is raised above the line. One period follows the first p, none follows the second. A long forked indicator descends at the gap between as and relier.',crop='09')
change('408-reference3','408 first reference',r'408 l.3 below',r'408 l 3 below','text not on the page','The gap between the l foot and the 3 is clear; no abbreviation point occurs there.',crop='10')
change('408-copy-comma','408 l 3, end of copy',r'last e missing in copy.',r'last e missing in copy,','misread symbol or index','The terminal mark has a narrow vertical body and a distinct bent descending tail, read as a comma.',crop='11',confidence='medium')
change('408-up-arrow','408 l.4, arrow above first ditto',r'\unsure{$\uparrow$|`} \'\''.replace('\\\'','\''),ditto408,'misread symbol or index','A triangular upward head, short shaft and curled foot are separate from the first pair of ditto strokes. The arrow is placed above and a little left of that pair.',crop='12')
change('408-isolated-point','408 l.4, blank area after identical',r'``identical\'\''.replace('\\\'','\''),identical408,'omission','The upper half shows a detached small dark point in the blank area to the right, above the word baseline. Its function is not assigned.',source=meta['half_a'],bbox=[765,964,983,1025])
change('409-overwritten-s','409 l-1, t of its',r'l-1 ``its\'\''.replace('\\\'','\''),r'l-1 ``'+its409+"''",'deletion state (struck given live or live given struck)','Two small old curved lobes survive through the live t stem and crossbar. They suggest s but remain partly buried; the live i, t and final s are readable. The old letter is overlaid beneath t, not printed as an extra live letter.',crop='13',confidence='medium')
change('410-first-opener-state','410, first cancelled reference and its',r'\deleted{l.\unsure{2} ``its\'\'}'.replace('\\\'','\''),r'\deleted{l.\unsure{2}} ``\deleted{its\'\'}'.replace('\\\'','\''),'deletion state (struck given live or live given struck)','The opening pair stands above the cancellation paths, whereas the terminal group is crossed at the right turn. The old numeral is still not securely legible through the diagonal strokes.',crop='14',confidence='medium')
change('410-being-closer','410 l 2, high mark after being',r"\unsure{`|''}",r"\unsure{''|`}",'misread symbol or index','Two touching descending parts favor a fused closing pair, but the continuous upper body leaves a single returned stroke possible. Three separate low points follow.',crop='15',confidence='medium')
change('410-second-cancellation','410 l 2, second cancelled quoted cluster',r'\deleted{``\unsure{its}\'\'}'.replace('\\\'','\''),second410,'deletion state (struck given live or live given struck)','The opener is visibly clear of the enclosing cancellation. The word has a broad upper/lower first-letter form favoring capital I, but the crossing strokes permit lowercase i. At the closer one stem meets a diagonal and the other lies clear; the group cancellation state remains uncertain.',crop='16',confidence='low')
change('410-shouldnt17-opener','410 l17, opener of shouldnt',"l 17 `shouldn't''","l 17 ``shouldn't''",'misread symbol or index','The opener contains a longer left stroke and a distinct short dark right stroke. Both are separate from the word.',crop='17')
change('411-copy-punctuation','411 l19, low terminal mark after copy',r'end of line in copy .',r'end of line in copy \unsure{,|.}','misread symbol or index','The low mark is angular and descends at its right end. A comma is favored, but an elongated stop cannot be excluded from the small surviving body.',crop='19',confidence='medium')
change('412-overwritten-t','412 l.12, initial of do',r'\deleted{\unsure{t}}do',do412,'insertion or placement','The broad old upper stroke overlaps the live d in one letter space; the following o is shared. The under-letter remains tentatively t because the overlap obscures its separate contour.',crop='21',confidence='medium')
change('412-reference-point','412, l.-14 reference',r'l.-14 ``formulary',line412+r' ``formulary','insertion or placement','The small low point is beneath the middle of the horizontal reference stroke, not at the l foot. It is retained once under that stroke; the prior sentence stop remains separate.',crop='22')
change('413-wont-closer','413 l-2, closing quotation group',"l-2 ``won't''",r"l-2 ``won't\unsure{'|''}",'misread symbol or index','The terminal group has one continuous upright with a rightward returned foot. A single closer is the nearer shape, while fused double strokes remain possible; the crop includes blank paper beyond the complete edge.',crop='24',confidence='medium')
change('416-raised-point','416, detached point after page number',r'p 416 l-1.',page416+r' l-1.','omission','A distinct small point lies just right of 416 and above the numeral baseline. It is separate from the vertical trace and is reproduced without a punctuation interpretation.',crop='25')
change('419-make-sense-opener','419 l.6, opening quotation group',"l.6 `make sense''",r"l.6 \unsure{`|``}make sense''",'misread symbol or index','The opener is a connected upright-and-branch shape. The joined body permits either a single returned stroke or fused double strokes; the closing pair is clear.',crop='27',confidence='medium')
change('419-dont-opener','419, final quoted dont',r"\quad `don't''",r"\quad ``don't''",'misread symbol or index','Two independent dark opening strokes are separated by a pale gap. The closing pair and the internal apostrophe are also separately visible.',crop='28')
change('420-right-points','420 level, blank area at right',r'p 420 l.10 ``made up of\'\' is more usual.'.replace('\\\'','\''),r'p 420 l.10 ``made up of\'\' is more usual. '.replace('\\\'','\'')+points420,'omission','Two distinct small dark marks stand diagonally in the right blank area. Their physical positions are retained without assigning a colon or other punctuation role.',source=meta['half_b'],bbox=[1445,884,1501,931])
change('422-raised-in','422 l13, raised in after again',r'again \inserted{in} l.14.',r'again '+in422+r' l.14.','insertion or placement','The lower half shows in above the gap after again, with a long downward indicator ending below the line. It is represented at that height and attachment.',source=meta['half_b'],bbox=[597,987,797,1078])
change('423-isolated-point','423, isolated point above and to right of its',r'423 l-4 above diagram 105 ``its\'\''.replace('\\\'','\''),r'423 l-4 above diagram 105 '+its423,'omission','The crop separates a small gray-black point from the text and from the paper texture. Its origin and punctuation function are left unassigned.',crop='36',confidence='medium')
change('425-its-opener','425 l.11, opening quotation group',"l.11 `its''",r"l.11 \unsure{`|``}its''",'misread symbol or index','The high opener has two touching downward legs with one continuous pointed top. A single returned stroke is favored, but a fused pair remains possible. The later dot belongs to i, and the closer is a separate pair.',crop='31',confidence='medium')

# The text is kept in its original list order. A local table locates each page
# reference to the left of the continuous traces; no inferred content is added.
body = body.replace('\\scanpage{31}\n\n', '', 1)
body = body.replace('% archive sheet number: 30', '').strip()
paras = body.split('\n\n')
page_starts = [
    'p.402 ', 'p 403 ', '404 ', '405 ', '407 ', '408 ', 'p 409. ',
    'p 410 ', 'p 411 ', 'p 412 ', 'p 413 ', 'p 415 ', page416+' ',
    'p 417 ', 'p 419 ', 'p 420 ', 'p 421 ', 'p 422 ', r'\unsure{p|l} 423 ', 'p 425 '
]
rows = []
for para in paras:
    matches = [p for p in page_starts if para.startswith(p)]
    if matches:
        start = matches[0]
        rows.append([start.rstrip(), [para[len(start):]]])
    else:
        assert rows, para
        rows[-1][1].append(para)
assert len(rows) == 20, len(rows)

left_trace = r'''\path (sheet031B.north west) -- (sheet031B.south west) coordinate[pos=.41] (trace031Bleftmid);
\draw[black!75,line width=.25pt] ([xshift=3.65em,yshift=-.7ex]sheet031B.north west) -- ([xshift=3.7em]trace031Bleftmid);
\draw[black!32,line width=.25pt] ([xshift=3.7em]trace031Bleftmid) -- ([xshift=3.85em,yshift=-2ex]sheet031B.south west);'''
right_trace = r'''\path (sheet031B.north east) -- (sheet031B.south east) coordinate[pos=.41] (trace031Brightmid);
\draw[black!75,line width=.25pt] ([xshift=-.6em,yshift=-.7ex]sheet031B.north east) -- ([xshift=-.5em]trace031Brightmid);
\draw[black!32,line width=.25pt] ([xshift=-.5em]trace031Brightmid) -- ([xshift=-.4em,yshift=1.4ex]sheet031B.south east);'''
lr = change('left-vertical-trace','Left vertical trace beside the references','',left_trace,'drawing or diagram','A narrow dark trace starts near whole-image (210,97), becomes pale lower down, and continues near (231,2340). The top and bottom were separately inspected; the geometric trace is preserved, with ink versus material origin unassigned.',crop='32',confidence='medium',apply=False)
lr['additional_evidence']=[evidence('33')]
rr = change('right-vertical-trace','Right vertical trace beside and behind text','',right_trace,'drawing or diagram','The upper endpoint is near whole-image (1486,97); the pale lower trace ends near (1507,2280), above the archive number and sheet edge. It is reproduced alongside the writing, with origin unassigned.',crop='34',confidence='medium',apply=False)
rr['additional_evidence']=[evidence('35')]

reading = r'''\cotefile{109}
\scanpage{31}
% One handwritten correction list. Two vertical traces are preserved geometrically;
% their ink/material origin is unassigned. Circular edge impressions are material.
\noindent\begin{tikzpicture}
\node[anchor=north west,inner sep=0pt] (sheet031B) {%
\begin{minipage}{\linewidth}
\begin{tabular}{@{}p{3.4em}@{\hspace{1em}}p{\dimexpr\linewidth-4.4em\relax}@{}}
'''
for label, ps in rows:
    reading += label+' & '+r'\par '.join(ps)+r' \\[.5ex]'+'\n\n'
reading += r'''\end{tabular}
\end{minipage}};
% BEGIN left-vertical-trace
'''+left_trace+r'''
% END left-vertical-trace
% BEGIN right-vertical-trace
'''+right_trace+r'''
% END right-vertical-trace
\end{tikzpicture}
% archive sheet number: 30
'''
(OUT/'reading.tex').write_text(reading)

c_doubts=[]
def doubt(place,old,new,resolved,why,crop=None,source=None,bbox=None,confidence='high'):
    c_doubts.append({'place':place,'c':old,'reading':new,'resolved':resolved,
                     'confidence':confidence,'evidence':why,**evidence(crop,source,bbox)})
doubt('402, first character before 6',r'\unsure{$\downarrow$6|16}',r'$\downarrow$6',True,'Two returning arrowhead sides meet the sloping shaft; 6 is separate.',crop='01')
doubt('403 l.4, cancelled own',r'\deleted{\unsure{own}}',r'\deleted{own}',True,'The o bowl, w turns and final n survive the cross-strokes.',crop='02',confidence='medium')
doubt('407 l-15, cancelled word before old French origin',r'\deleted{\unsure{the|its}}',r'\deleted{the}',True,'The first tall upright and following looped ascender favor t and h; the final low turn fits e, not an independently visible its.',crop='08',confidence='medium')
doubt('407 l-15, old letter under as',r'\deleted{\unsure{i}}as',as407,True,'A separate old dot and short inner upright remain under the live a; s is shared.',crop='09',confidence='medium')
doubt('408 l.4, high mark above first ditto',r'\unsure{$\uparrow$|`}',r'$\uparrow$',True,'A pointed upward head and shaft are distinct from the lower ditto pair.',crop='12')
doubt('410, numeral in first cancelled reference',r'\deleted{l.\unsure{2} ``its\'\'}'.replace('\\\'','\''),r'\deleted{l.\unsure{2}} ``\deleted{its\'\'}'.replace('\\\'','\''),False,'The old curved numeral remains compatible with 2 but its middle is buried beneath diagonal cancellation. The numeral uncertainty is retained; opener state is separately corrected.',crop='14',confidence='low')
doubt('410 l 2, high mark after being',r"\unsure{`|''}",r"\unsure{''|`}",False,'Two joined lower parts favor a closing pair, but a single returned stroke remains possible.',crop='15',confidence='medium')
doubt('410 l 2, second cancelled its',r'\deleted{``\unsure{its}\'\'}'.replace('\\\'','\''),second410,False,'The first letter resembles a capital I with broad upper and lower strokes, though cancellation prevents excluding i. The closing group state is also uncertain.',crop='16',confidence='low')
doubt('412 l.12, old initial beneath do',r'\deleted{\unsure{t}}do',do412,False,'The broad top and upright are compatible with old t; overlap prevents a secure independent outline. Old/new initials share one space.',crop='21',confidence='low')
doubt('417 l1, cancelled false start before (84)',r'\deleted{\unsure{l 1}}',r'\deleted{\unsure{l 1}}',False,'A tall loop and a second short upright are visible, but the crossing strokes still obscure the full old reference.',crop='26',confidence='low')
doubt('423, page-reference initial',r'\unsure{p|l}',r'\unsure{p|l}',False,'The long descender and upper right thickening favor p; no complete bowl survives, so l is retained as the supplied alternative.',crop='30',confidence='medium')

# Page-specific context confirmations, independently checked on this page.
doubt('C_context: 402 hatted A and index',r'$\hat{A}_{ab}$',r'$\hat{A}_{ab}$',True,'One ordinary A, a pointed roof attached to A, and two lowered lowercase letters a and b are visible. The b has an upright stem.',crop='01')
doubt('C_context: 407 raised replacement its',r'\inserted{its}',r'\inserted{its}',True,'The raised word is readable and stands above/right of the cancelled word.',crop='08')
doubt('C_context: 407 raised a p.p of',r'\inserted{a p.p of}',pp407,True,'The raised lettering and descending forked insertion indicator are visible before relier.',crop='09')
doubt('C_context: 422 raised in',r'\inserted{in}',in422,True,'The lower half shows the added word above the gap after again; its descending indicator attaches before l.14.',source=meta['half_b'],bbox=[597,987,797,1078])
doubt('C_context: 408 two ditto groups',r"'' \quad ''",r"'' \quad ''",True,'Two distinct pairs occupy the places beneath below and diagram; the upward arrow is a separate upper mark.',crop='12')
doubt('C_context: 411 reference ampersand',r'l-4 \& -3',r'l-4 \& -3',True,'The joining mark has a small loop and crossing arms, distinct from both minus signs.',source=meta['half_b'],bbox=[256,240,506,299])
doubt('C_context: 413 formula-reference e',r'$(75)e$',r'$(75)e$',True,'The small rounded e sits on the line following the closing parenthesis; it is not raised.',source=meta['half_b'],bbox=[661,425,893,507])
doubt('C_context: 417 first formula-reference e',r'$(84)e$',r'$(84)e$',True,'The rounded e is on the baseline after the closing parenthesis.',source=meta['half_b'],bbox=[255,687,487,766])
doubt('C_context: 411 c.f and page reference punctuation',r'c.f comment on p.407.',r'c.f comment on p.407.',True,'The half shows one internal point in c.f, no separate point after f, and the two visible stops associated with p.407.',source=meta['half_b'],bbox=[786,252,1236,304])
doubt('C_context: 402 missing-index comment','(the ab is missing.)','(the ab is missing.)',True,'The same two letters ab occur in the comment; its period is before the closing parenthesis.',source=meta['half_a'],bbox=[875,135,1303,216])
doubt('C_context: 407 missing-s wording',r'``categorie\uline{s}\'\' the s is missing on my copy.'.replace('\\\'','\''),r'``categorie\uline{s}\'\' the s is missing on my copy.'.replace('\\\'','\''),True,'The final s alone has a short underline; the note explicitly says on my copy.',source=meta['half_a'],bbox=[341,707,1088,782])
doubt('C_context: 408 missing-e wording','last e missing in copy.','last e missing in copy,',True,'The wording is unchanged, while the terminal mark is a hooked comma in the crop.',crop='11',confidence='medium')
doubt('C_context: 411 missing-e wording','e lost off end of line in copy .',r'e lost off end of line in copy \unsure{,|.}',False,'The wording is legible; only its terminal mark remains a comma/stop doubt.',crop='19',confidence='medium')
doubt('C_context: 407 qualification on around',r'perhaps ``on and around\'\''.replace('\\\'','\''),r'perhaps ``on and around\'\''.replace('\\\'','\''),True,'The word perhaps precedes the quoted proposal, within the however parenthesis; no stronger replacement instruction is supplied.',source=meta['half_a'],bbox=[256,579,1458,711])
doubt('C_context: 407 qualified translation',r'suggests a translation as ``binding\'\''.replace('\\\'','\''),r'suggests a translation as ``binding\'\''.replace('\\\'','\''),True,'The lower line explicitly reads suggests a translation as binding; its qualifying verb is preserved.',source=meta['half_a'],bbox=[527,839,1294,909])

remaining=[]
def remains(place,reading,alternatives,why,confidence='medium'):
    remaining.append({'place':place,'reading':reading,'alternatives':alternatives,'confidence':confidence,'reason':why})
remains('404 last reference',r'l.\unsure{+|-}5','+; -','A central downward spur is visible but may be a pen return on the thick horizontal.')
remains('405 l-9 opener',r'\unsure{``|`}',"``; `",'The two tips belong to one joined curved body.')
remains('409 l-1 overwritten letter',r'\deleted{\unsure{s}}','s','Two old lobes suggest s, but the live t obscures their junction.','low')
remains('410 first cancelled numeral',r'\unsure{2}','2','Cancellation buries the middle of the old numeral.','low')
remains('410 after being',r"\unsure{''|`}","''; `",'The two lower parts meet in a dense continuous upper body.')
remains('410 second cancelled word',r'\unsure{Its|its}','Its; its','Capital-like upper/lower strokes may include cancellation segments.','low')
remains('410 second cancelled closer',r"\unsure{\deleted{''}|''}","cancelled pair; live pair",'One stem meets a crossing diagonal while the other remains clear.','low')
remains('411 terminal mark after copy',r'\unsure{,|.}',',; .','The tiny angular body has a descending right end but does not conclusively separate comma from elongated stop.')
remains('412 old initial beneath d',r'\deleted{\unsure{t}}','t','The old upper stroke is visible but its independent contour is buried.','low')
remains('413 wont closer',r"\unsure{'|''}","'; ''",'A single upright and returned foot may also be fused double strokes.')
remains('417 cancelled false start',r'\deleted{\unsure{l 1}}','l 1','The loop and short upright survive only partially under the cancellation.','low')
remains('419 make sense opener',r'\unsure{`|``}',"`; ``",'Connected upright and oblique branch do not establish the original stroke count.')
remains('423 initial page-reference letter',r'\unsure{p|l}','p; l','The upper right thickening does not form a complete readable bowl.')
remains('425 its opener',r'\unsure{`|``}',"`; ``",'Two touching lower legs share one dense pointed top.')
remains('Left long vertical trace',left_trace,'drawn rule; material trace','The dark upper contour and pale lower continuation are certain, but the photographic evidence alone does not securely assign an ink or material origin.')
remains('Right long vertical trace',right_trace,'drawn rule; material trace','The upper and lower endpoints are observed; origin is not assigned.')

inventory=[]
def inv(element,kind,pos,words,hand='one unnamed handwritten hand'):
    inventory.append({'sheet_kind':'list','hand':hand,'element':element,'kind':kind,
                      'position':pos,'first_words_or_objects':words,'transcribed':'yes'})
items=[
('01','text','top, 402 l.3','p.402 l.3 analogue'),('02','text','top, 402 l7','commutes with'),('03','text','top right, 402 l14',"don't"),
('04','text','402 second line l.17',"didn't"),('05','text','402 second line arrow6',r'$\hat A_{ab}$ (the ab is missing.)'),
('06','text','403 l.2','analogue'),('07','text','403 l.4','its own'),('07a','deletion','inside 403 l.4','own'),('07b','drawing','below 403 reference 4','one detached low point'),
('08','text','403 l.8','its'),('09','text','403 l16','analogue'),
('10','text','404 l11',"wouldn't"),('11','text','404 l-12',"haven't"),('12','text','404 final reference','analogue'),
('13','text','405 l.11','commutes with'),('14','text','405 l-9',"didn't"),
('15','text','407 long paragraph','The word formulaire is not English; formulary; however; perhaps on and around'),
('16','text','407 l3','categories; the s is missing on my copy'),('16a','text','final letter of categories','single underline under s'),('17','text','407 short l-15 entry','its'),
('18','text','407 second l-15 entry','relying is not used in this sense; old French origin; relier; binding'),
('18a','deletion','407 before old French origin','the'),('18b','insertion','above 18a, slightly right','its'),
('18c','deletion','407 first letter of as','old i under a; final s shared'),('18d','insertion','above gap after as','a p.p of'),('18e','drawing','407 gap before relier','descending forked insertion indicator'),
('19','text','408 first entry','l 3 below diagram - see - last e missing in copy'),
('20','text','408 l.4','ditto groups; identical'),('20a','drawing','above first ditto','upward arrow'),('20b','text','under below','first ditto pair'),('20c','text','under diagram','second ditto pair'),('20d','drawing','408 right blank after identical','isolated raised point'),
('21','text','409 l12','its'),('22','text','409 l-12',"doesn't"),('23','text','409 l-3',"don't feel that I have understood"),('24','text','409 l-2',"hasn't"),('25','text','409 l-1','its'),('25a','deletion','409 t of its','tentative old s overlapped by t'),
('26','text','410 first entry','cancelled l.2 and its with live opening pair'),('26a','deletion','410 first reference','l. uncertain 2'),('26b','text','410 between cancelled reference and word','live opening pair'),('26c','deletion','410 first quoted word and closer','its and closing pair'),
('27','text','410 live l2','it before being; high group; three low points'),('27a','text','410 before','single underline beneath before'),
('28','text','410 after ellipsis','second cancelled quoted Its/its'),('28a','text','410 second cancelled cluster left edge','live opening pair'),('28b','deletion','410 second cancelled word','Its/its'),('28c','deletion','410 second cluster right edge','closing pair, cancellation state uncertain'),
('29','text','410 l17',"shouldn't"),('30','text','410 l19',"shouldn't"),('31','text','410 l-8','commuting with again in l-7'),
('32','text','411 l19','accurately; e lost off end of line in copy'),('33','text','411 l-4 & -3','formulary c.f comment on p.407'),
('34','text','412 l.9.','formulary again in l12'),('35','text','412 l.12','do replace forgetting by to get'),('35a','deletion','412 initial d','tentative old t under d; o shared'),('36','text','412 l-14','formulary'),('36a','drawing','412 line-reference mark','point directly under minus'),
('37','text','413 l6','formulary'),('38','text','413 formula reference','In (75)e commutes with'),('39','text','413 l-9','with small'),('40','text','413 l-7','commuting with'),('41','text','413 l-2',"won't"),
('42','text','415 l.-10','formula'),('43','text','416 l-1.','formulary'),('43a','drawing','right of page number 416','one raised point'),
('44','text','417 formula reference','In (84)e commutes with'),('45','text','417 l1','after cancelled false start (84) formulary doesnt'),('45a','deletion','before second (84)','tentative l 1'),
('46','text','419 l.6','make sense'),('47','text','419 l.8',"doesn't"),('48','text','419 final unreferenced word',"don't"),
('49','text','420 l.10','made up of is more usual'),('49a','drawing','420 right blank area','two small diagonal points'),
('50','text','421 l7','interpret'),('51','text','422 l13','formulary again in l.14'),('51a','insertion','above gap after again','in'),('51b','drawing','422 gap before l.14','descending insertion indicator'),
('52','text','423 l-4','above diagram 105 its'),('52a','drawing','above/right of 423 its','one isolated point'),('53','text','425 l.11','its also in l-7'),
('54','drawing','between reference column and text','long left vertical trace, origin unassigned'),('55','drawing','near right edge beside text','long right vertical trace, origin unassigned'),
]
for item in items: inv(*item)
inv('56','text','lower right corner, excluded from body text','archive sheet number 30, comment only','another unnamed hand, light archive numbering')

report={
 'scan':31,'reader':'B','model':'GPT-6 Astra Pro','effort':'not exposed',
 'viewed':[meta['whole'],meta['half_a'],meta['half_b']],
 'layout':'One densely handwritten correction list, with page references 402 through 425 in a narrow left column and English correction entries to their right. The longer 407 paragraph occupies the upper middle. Several entries contain small raised additions and overt cancellation or overwriting; all visible textual writing appears to be one hand. There are no displayed formulas, mathematical diagrams, drawings of objects, title, date, signature, or independent prose margin notes. Two long narrow vertical traces flank the central writing: their dark upper portions begin near y97 in the whole image; the left pale continuation reaches approximately (231,2340), while the right ends near (1507,2280). Their geometry is retained with origin unassigned. Circular impressions near the upper and lower right are material features, not ink circles. The light archive number 30 is recorded only as a comment. Textual list entries and every nested cancellation, insertion, underline, pointer, and retained detached point are individually inventoried.',
 'changes':changes,'c_doubts':c_doubts,'remaining_doubts':remaining,'inventory':inventory,
 'notes':[
  'The page covers manuscript references 402–425. No page 406, 414, 418 or 424 entry is present; none is supplied.',
  'At 402 the writer reproduces the hatted A with lowered ab and says that ab is missing. The preceding reference is read as a downward arrow followed by 6.',
  'At 407 formulaire is said not to be English; formulary is welcomed as a collection of formulae, compared with a list of magic spells. The parenthetical proposal says however and perhaps on and around; these qualifications remain intact.',
  'At 407 l-15 the writer says relying is not used in this sense and says the old French origin as a p.p of relier suggests a translation as binding. The additions and the earlier wording are both preserved.',
  'The copy is said to lack an s at 407 l3, the last e of see at 408, and an e off the end of a line at 411. The last note supplies no more exact position for that e.',
  "At 409 l-3 the quoted wording is don't feel that I have understood. No explanatory sentence accompanies this entry.",
  'The 412 instruction says do replace forgetting by to get. References In (75)e at 413 and In (84)e at 417 have baseline e, not superscripts.',
  'The visible formulas are an example notation and formula references; the page contains no mathematical theorem or proof.'
 ],
 'math_checks':[],
 'notation':[
  {'sign':r'$\downarrow$6','location':'402 after didnt','reading':r'$\downarrow$6','evidence':'Crop 01 shows a sloping shaft with a downward two-sided head, followed by separate 6.'},
  {'sign':r'$\hat A_{ab}$','location':'402','reading':r'$\hat A_{ab}$','evidence':'Crop 01 shows one ordinary A contour, roof above A, lowered a and b with b ascender.'},
  {'sign':r'\unsure{+|-}','location':'404 final line reference','reading':r'l.\unsure{+|-}5','evidence':'Crop 04 separates a central downward spur from the horizontal body.'},
  {'sign':'=','location':'407 after first formulary','reading':'=','evidence':'The upper half shows two parallel short horizontal strokes.'},
  {'sign':r'\uline{s}; \uline{before}','location':'407 categories; 410 it before being','reading':r'categorie\uline{s}; it \uline{before} being','evidence':'The halves show one short line under final s and one longer line confined to before.'},
  {'sign':r'$\uparrow$ and two ditto groups','location':'408 l.4','reading':ditto408+r" \quad ''",'evidence':'Crop 12 separates the arrow above the first paired marks and the second paired marks further right.'},
  {'sign':r'\&','location':'411 l-4 & -3','reading':r'l-4 \& -3','evidence':'Lower half: small loop crossed by two joining strokes.'},
  {'sign':'(75)e; (84)e','location':'413; 417','reading':r'$(75)e$; $(84)e$','evidence':'Each e was read separately in half b and sits on the formula-reference baseline.'},
  {'sign':'quotation groups','location':'405, 410, 413, 419, 422, 425','reading':r"\unsure{``|`}; \unsure{''|`}; \unsure{'|''}; \unsure{`|``}",'evidence':'Each edge was independently inspected in its one frozen crop. Definite double openers are restored at 410 l17 and 419 dont; fused local groups remain doubtful.'},
  {'sign':'old/new glyphs','location':'407 as; 409 its; 412 do','reading':as407+'; '+its409+'; '+do412,'evidence':'Crops 09, 13 and 21 preserve one physical glyph space for each overlap and print shared surviving letters only once.'},
  {'sign':'detached points','location':'403 l.4; 408 identical; 416 page number; 420 right blank; 423 right blank','reading':ref403+'; '+identical408+'; '+page416+'; '+points420+'; '+its423,'evidence':'Crops 02, 25, 36 and the two halves establish the listed distinct locations; no punctuation or origin is assigned.'},
  {'sign':'low reference point','location':'412 l-14','reading':line412,'evidence':'Crop 22 locates the point beneath the horizontal reference mark.'}
 ],
 'abbreviations':[
  {'form':'p. / p','expansion':'page, tentative conventional interpretation','place':'left page references, with punctuation as individually written'},
  {'form':'l. / l','expansion':'line, tentative conventional interpretation','place':'individual correction references throughout'},
  {'form':'c.f','expansion':'compare, tentative interpretation; spelling and missing final point preserved','place':'411 l-4 & -3'},
  {'form':'p.p','expansion':'past participle, tentative interpretation only','place':'407 raised a p.p of'}
 ],
 'brief_feedback':'Followed brief v15: whole once, each supplied half once; 36 unresolved loci were frozen before any crop, then exactly one enhanced crop per locus was generated with crop.py and each displayed singly. The four long-trace endpoint crops are separate frozen loci, not repeated crops of a settled place. A local TikZ/table wrapper was needed to preserve the relationship of the long traces to the reference column and text; confirmed wording and paragraph order are otherwise retained. H status is desc, so h is null and diff_h is false for every row. No OCR, recognition library, PDF extraction, outside research, other page image, other reader output, compilation, or agent delegation was used. Only static syntax, literal-difference and report-coverage checks are performed. The two long traces are the main material-versus-ink classification limit; they are drawn with their origin unassigned, while recognizable circular material impressions are not drawn.'
}
(OUT/'report.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
(OUT/'literal_diff.patch').write_text(''.join(difflib.unified_diff(C.splitlines(True),reading.splitlines(True),fromfile='C.tex',tofile='B/reading.tex')))
crop_outcomes = {
 '01':'Resolved down-arrow followed by 6; hat, ordinary A and lowered ab confirmed.',
 '02':'Cancelled own readable; opening and closing pairs live. Separate low point under 4 retained geometrically.',
 '03':'Two separate opening strokes and two closing strokes confirm C unchanged.',
 '04':'Period after l confirmed. Horizontal mark has central downward spur: plus favored, minus retained.',
 '05':'Paired opener and paired closer confirm C unchanged.',
 '06':'Compact branched opener remains double/single uncertain; paired closer confirmed.',
 '07':'Small low point just left of the lower serif of I supports the existing period after English. C retained.',
 '08':'Cancelled the read from surviving tall first stroke, looped next ascender and low ending. Raised its clear.',
 '09':'Old dotted i survives beneath a; final s shared. Raised a p.p of and forked indicator retained. One relier opener and two closer strokes confirmed.',
 '10':'No abbreviation point between l and 3; C point removed.',
 '11':'Terminal mark after copy read as a narrow hooked comma.',
 '12':'Upward arrow resolved independently of the two ditto pairs; both ditto locations retained.',
 '13':'Live its clear, with tentative older s-like lobes under t; old letter remains uncertain.',
 '14':'Cancelled numeral remains tentative 2. Opening pair is above the cancellation; closing group is crossed.',
 '15':'Double closer favored but single returned stroke remains possible; exactly three following low points.',
 '16':'Second cancelled word remains Its/its uncertain. Opener live; closer cancellation state uncertain.',
 '17':'Distinct longer left and shorter right opening strokes establish double opener.',
 '18':'Two openers and two closers confirm C unchanged.',
 '19':'Low angular terminal body remains comma/period uncertain.',
 '20':'Two opening strokes and two closing strokes confirm C unchanged.',
 '21':'Old t remains uncertain under d; shared o is not duplicated.',
 '22':'Reference point lies directly under the horizontal mark. Prior sentence stop is separately present.',
 '23':'Long left and short right closing strokes form a pair; C confirmed.',
 '24':'One continuous closing stem and returned foot; single favored, fused pair possible.',
 '25':'Point after 416 is raised and separate from the vertical trace; reproduced without assigning punctuation.',
 '26':'Cancelled l 1 remains uncertain; no extra old word supplied.',
 '27':'Opening upright-and-branch remains single/double uncertain; paired closer confirmed.',
 '28':'Two separate opener strokes and paired closer; C single opener corrected.',
 '29':'Two upper tips and distinct stems in the connected closer support paired quotation; C retained.',
 '30':'Long reference descender and upper thickening favor p, but bowl is incomplete; supplied p/l doubt retained.',
 '31':'Pointed joined opener remains single/double uncertain. Dot belongs to i; paired closer is clear.',
 '32':'Upper left narrow dark trace starts at approximately whole (210,97). Geometry certain, origin unassigned.',
 '33':'Pale left trace continues to near the lower sheet edge, approximately whole (231,2340); no invented further extension.',
 '34':'Upper right narrow dark trace starts near whole (1486,97). Geometry certain, origin unassigned. Circular impression is material.',
 '35':'Pale right trace ends near whole (1507,2280), above archive 30 and sheet edge. Circular impression is material.',
 '36':'A small detached gray-black point is visible above/right of the 423 its; reproduced with origin unassigned.'
}
(OUT/'crop_decisions.json').write_text(json.dumps({'scan':31,'reader':'B','all_36_crops_viewed_singly':True,'decisions':[
 {'id':z['id'],'name':z['name'],'crop':z['crop'],'status':'actually displayed once singly','outcome':crop_outcomes[z['id']],'related_changes':[r['id'] for r in changes if r.get('crop')==z['crop'] or any(e.get('crop')==z['crop'] for e in r.get('additional_evidence',[]))]}
 for z in frozen['loci']]},indent=2)+'\n')
with (OUT/'views.jsonl').open('w') as f:
    for k in ['whole','half_a','half_b']:
        f.write(json.dumps({'kind':k,'path':meta[k],'view_count':1,'status':'actually displayed singly'})+'\n')
    for z in frozen['loci']:
        f.write(json.dumps({'kind':'crop','path':z['crop'],'view_count':1,'status':'actually displayed singly'})+'\n')

# Static checks only; no TeX engine, document renderer, OCR or recognition.
clean = '\n'.join(line.split('%',1)[0] for line in reading.splitlines())
level=0
for i,ch in enumerate(clean):
    if ch in '{}':
        backslashes=0
        j=i-1
        while j>=0 and clean[j]=='\\':
            backslashes+=1; j-=1
        if backslashes%2: continue
        level += 1 if ch=='{' else -1
        assert level>=0, ('negative brace depth',i)
assert level==0, level
stack=[]
for op,env in re.findall(r'\\(begin|end)\{([^}]+)\}',clean):
    if op=='begin': stack.append(env)
    else: assert stack and stack.pop()==env, (op,env,stack)
assert not stack, stack
assert len(re.findall(r'(?<!\\)\$',clean))%2==0
assert all(p in reading for _,ps in rows for p in ps)
assert all(z.get('crop') or (z.get('source') and len(z.get('bbox',[]))==4) for z in changes+c_doubts)
assert all(z['h'] is None and not z['diff_h'] and not z['marked_in_H'] for z in changes)
assert not report['math_checks']
assert reading.startswith('\\cotefile{109}\n\\scanpage{31}')
assert not re.search(r'\\(?:newcommand|renewcommand|def)\b',clean)
crop_logs=[json.loads(line) for line in (OUT/'crops/crops.jsonl').read_text().splitlines()]
views=[json.loads(line) for line in (OUT/'views.jsonl').read_text().splitlines()]
assert len(crop_logs)==36 and len({z['output'] for z in crop_logs})==36
assert len(views)==39 and len({z['path'] for z in views})==39
known_macros = {'cotefile','scanpage','noindent','begin','end','node','linewidth','hspace','dimexpr','relax','quad','par','tikz','fill','deleted','unsure','inserted','draw','path','uparrow','downarrow','hat','uline','ldots','hfill'}
macro_names=set(re.findall(r'\\([A-Za-z]+)',clean))
assert macro_names<=known_macros, sorted(macro_names-known_macros)
static={
 'scan':31,'reader':'B','method':'static checks only; no LaTeX compilation',
 'brace_balance':'passed','environment_nesting':'passed','math_dollar_parity':'passed',
 'macro_allowlist':'passed; only supplied state macros and standard LaTeX/TikZ commands',
 'all_20_page_groups_and_all_collated_paragraphs_present':True,
 'literal_replacements':'28 uniquely matched literal replacements against supplied C; two additional geometric trace entries',
 'change_report_coverage':'every implemented literal edit has one corresponding report row; table wrapper only locates references and traces',
 'evidence_coverage':'every change and C doubt/context decision has a crop or source image and tight source-coordinate bbox',
 'H_status':'desc; no H text comparison rows',
 'unique_crop_count':36,'unique_view_count':39,'whole_and_each_half_once':True,
 'every_crop_displayed_singly_once':True,'unsure_macros_in_reading':reading.count('\\unsure{'),
 'mathematical_check_events':0,
 'limits':'Static TeX checks do not establish rendered appearance; compilation was expressly prohibited. Quotation mismatches and local uncertainty are intentional manuscript readings.'
}
(OUT/'static_checks.json').write_text(json.dumps(static,indent=2)+'\n')
print(json.dumps({'changes':len(changes),'c_doubts':len(c_doubts),'resolved_c_doubts':sum(r['resolved'] for r in c_doubts),'remaining_doubts':len(remaining),'inventory':len(inventory),'crops':len(frozen['loci'])}))
