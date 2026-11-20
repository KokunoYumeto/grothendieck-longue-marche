from pathlib import Path
import sys,json
sys.path.insert(0,str(Path('SP02_CW_10+12/scripts').resolve()))
from root_record import Record
r=Record('B12-01',12,68,'cancelled_draft')
H='[No H text supplied.]'
def ch(place,C,final,shows,crop,kind='other',confidence='high',against_C=False,consequential=False):
 r.change(place,C,H,final,shows,crop,kind,confidence,against_C,False,False,consequential)
paren=r'y=f\rlap{\(x\)}(x)'
ordinaire=r'\unsure{o|\rlap{r}o}\unsure{\rlap{u}r|r}dinaire'
local=r'loc\unsure{\rlap{q}a|a}l'
plausible=r'p\rlap{o}lausible'
mais=r'M\rlap{i}a\rlap{a}is'
r.edit('y=f(x)',paren)
r.edit('ordinaire',ordinaire)
stacklocal=r'''\mbox{\begin{tikzpicture}[baseline=(base.base)]
\node[inner sep=0] (base) {loc\unsure{\rlap{q}a|a}l \uline{complet}};
\path (base.north west) -- coordinate[pos=.43] (ins) (base.north east);
\node[anchor=south,inner sep=0,yshift=.08cm] at (ins) {\inserted{intègre}};
\end{tikzpicture}}'''
r.edit(r'local \inserted{intègre} \uline{complet}',stacklocal)
r.edit(r'\inserted{A=}\text{\uuline{R}}',r'\overset{\textstyle\inserted{A=}}{\text{\uuline{R}}}')
r.edit(r'A\otimes_{\text{\uuline{R}}}',r'A\otimes_{\underline{R}}')
r.edit('plausible',plausible)
r.edit('N°',r'N\textsuperscript{\uline{o}}')
r.edit(r'\deleted{\unsure{x}}',r'\deleted{é}')
stackdans=r'''\mbox{\begin{tikzpicture}[baseline=(base.base)]
\node[inner sep=0] (base) {même lorsque l'extension};
\node[anchor=south west,inner sep=0,yshift=.08cm,xshift=.08cm] at (base.north west) {\inserted{dans le cas général,}};
\end{tikzpicture}}'''
r.edit(r"Mais \inserted{dans le cas général,} même lorsque l'extension",mais+' '+stackdans)
r.edit(r'\unsure{la technique dévis}',r'la technique \unsure{dévis}')
hooks=r'''% Two isolated nonalphabetic dark hook-like marks in the left margin, below point; function/origin uncertain.
\margin{\figure{\begin{tikzpicture}[x=.8cm,y=.8cm]
\draw[line width=.55pt] (0,0) .. controls (.12,-.02) and (.25,-.01) .. (.33,.02) -- (.29,.19);
\draw[line width=.75pt] (1.35,-.10) -- (1.64,-.13) -- (1.56,.15);
\end{tikzpicture}}}
'''
r.edit(r'\deleted{La condition supplémentaire',hooks+r'\deleted{La condition supplémentaire')
ch('curve example, opening parenthesis of f(x)','y=f(x)',paren,'The opening parenthesis has its own tall curved stroke; at x height a separate left serif, right upper tip, crossing diagonal and two basal feet match the following lower-case x. Both impressions occupy the parenthesis cell. No typing order is inferred.','yfx; yparenA','misread symbol or index','high',True)
ch('point double ordinaire, first two cells','ordinaire',ordinaire,'The first cell has a complete oval with dense extra upper ink, but the long diagonal cancellation hides its left side; an r/o overlap is only an alternative. The next cell has an r shoulder plus a low bowl/right upright suggestive of u; their fused contours leave u/r qualified. The remaining dinaire is clear.','ordinaire; ordfirstA','misread word','low',True)
ch('after normalisé, right edge',r'\unsure{d|de}',r'\unsure{d|de}','A complete d reaches the right edge. The tiny following dark projection does not expose a complete e; C macro/table doubt is retained, and no lost word or Y is supplied.','dedge','other','low')
ch('local, a cell','local',local,'Below the a, a separate right-side descender with a horizontal foot is visible. It suggests a q impression sharing the a cell, but its upper contour is fused with a; the q/a reading is qualified and no chronology is assigned.','integreplaceB; localA','misread word','medium',True)
ch('intègre insertion above local complet',r'local \inserted{intègre} \uline{complet}',stacklocal,'Intègre is typed between lines above the right half of local and the beginning of complet, with its grave accent visible. There is no insertion leader. Its vertical placement and the single underline under complet are retained.','integre; complet; integreplaceB','insertion or placement','high',True)
ch('A= addition above the real-coefficient formula',r'\inserted{A=}\text{\uuline{R}}',r'\overset{\textstyle\inserted{A=}}{\text{\uuline{R}}}','A and the two equality strokes are typed on the line above R, centered slightly to its left, without a leader. They are not a baseline prefix. R has two separate underlines.','Ainsert; RXformula; RcontrolB','insertion or placement','high',True)
ch('subscript R in Alors A tensor R C',r'A\otimes_{\text{\uuline{R}}}\underline{C}',r'A\otimes_{\underline{R}}\underline{C}','The lowered R has one separate horizontal underline below its serif feet, and the extended supplied-half crop shows clear paper below it. In contrast, the coefficient R above has two distinct lines. C also has one underline.','Acomplex; RsubB; RcontrolB','misread symbol or index','high',True)
ch('plausible, l cell','plausible',plausible,'The full-height l stem/foot is crossed by a closed x-height oval visible on both sides. Both o and l are retained in the same cell, without choosing a typing chronology.','plausible','misread word','high',True)
ch('last paragraph, N reference','N°',r'N\textsuperscript{\uline{o}}','The small raised o has its own horizontal underline, separate from the N and following 7.9.; C omits that underline.','Nref','omission','high',True)
ch('last paragraph, canceled character after la',r'\deleted{\unsure{x}}',r'\deleted{é}','An acute is clear above the canceled cell; the e has an upper/right curve, horizontal middle stroke and lower curve surviving the x overstrike. C macro/table doubt is resolved to deleted é.','laextra; laeB','misread word','high',True)
ch('Mais, two middle typewriter cells','Mais',mais,'The second cell has the bowl/shoulder of a and the dot, stem and foot of i. The third has another a bowl/shoulder under an i dot/stem/foot. Both a/i overlaps are retained without a claim about which impression came first.','Mais; MaisB','misread word','high',True)
ch('dans le cas général insertion',r"\inserted{dans le cas général,} même lorsque l'extension",stackdans,'The phrase is typed above même lorsque and the beginning of extension, starting nearly above the first m. There is no caret or leader; the two vertical levels are preserved.','dansinsert; dansplaceB','insertion or placement','high',True)
ch('canceled extra cell after final A',r'\deleted{\unsure{s|x}}',r'\deleted{\unsure{s|x}}','A small curved impression remains under a heavy x. Its right curves favor s but do not isolate a full underlying letter; C macro/table doubt is retained.','Aextra; AextrasB','other','low')
ch('last line canceled words',r'\deleted{\unsure{la technique dévis}}',r'\deleted{la technique \unsure{dévis}}','La technique is recoverable through the x row: l ascender, a bowl, t crossbar, e/c curves, h stem, n arch, dotted i, q descender, u bowl and final e. The following d and acute are visible, but the final letters remain fused with overstrikes; the tentative fragment dévis remains qualified, with no completion.','techcancel; techendB','misread word','medium',True)
ch('left margin, beneath point','[not represented]',hooks,'Two isolated dark hook-like marks occur between the point line and en x. They are reproduced by their angular/curved strokes. No alphabetic value, relation to the prose, or definite author is inferred; faint surrounding transfer-like traces are not promoted into letters.','leftmarks; leftmarksA','drawing or diagram','low',True)
for loc,s,desc,crop in [
 ('condition paragraph','où il est en défaut','The two letters il are distinct; the typed gender is retained.','il'),
 ('example paragraph','resert','One s is followed directly by e-r-t; no second s occurs.','resert'),
 ('question and final paragraph openings','reponse; reponse; réponse','No accent is present over the first two e letters; a distinct acute is present in the final réponse.','reponse1; reponse2; reponsebottom'),
 ('A et B complet','complet','The t is followed by a comma without an s.','Bcomplet'),
 ('real-coefficient example',r'\text{\uuline{R}}\ X,Y\quad/(X^2+Y^2)','No brackets surround X,Y. Both raised handwritten 2s, plus, slash and parentheses are clear. The blank and absence of brackets are retained.','RXformula; RcontrolB')]:
 ch(loc,s,s,desc,crop)
r.doubt('ordinaire, first two cells',ordinaire,'dense overprints unresolved','low','Long page-cancellation line obscures the first left contour; possible r/o and u/r overlaps remain qualified.')
r.doubt('right edge after normalisé','d','de; content beyond scan edge','low','Complete d; no secure following e; no Y supplied.')
r.doubt('local, a cell',r'\rlap{q}a','a','medium','Extra right descender and foot favor q/a overlap; the upper contour cannot be separated completely.')
r.doubt('last paragraph, cell after A','s','x','low','Curves survive but the heavy overstrike prevents a secure full underlying letter.')
r.doubt('last line canceled fragment','dévis','abandoned/overtyped final letters','low','La technique is clear; the following fragment remains tentative and is not completed.')
r.doubt('two left-margin hooks','two nonalphabetic hook-like strokes','origin or function undetermined','low','Shapes reproduced, without attributing words or a textual insertion.')
r.notation('typed R underlines',r'\uuline{R}; subscript \underline R','12:068 display/condition/coefficient R have two lines; the R below the later A tensor C has one line, verified against the actual bottom half.')
r.notation('typed tensor sign',r'\otimes; \otimes_A; \otimes_{\underline R}','12:068 three tensor cells separately enlarged, including base A and underlined base R; the crossing diagonals within the rounded typewriter form are preserved.')
r.notation('blank arrow and condition slots',r'a) b) \quad) \quad); f:X\quad Y; A\quad B','12:068 no missing letters or arrows supplied in the visibly blank positions; blank reference also retained.')
r.notation('raised underlined abbreviation o',r'N\textsuperscript{\uline{o}}','12:068 reference 7.9.; raised small o and separate underline.')
r.notation('typewriter overprints without chronology',paren+'; '+plausible+'; '+mais,'12:068 x/parenthesis, o/l, and two a/i overlaps; local q/a and ordinaire overlaps separately qualified.')
r.notation('handwritten exponents and separators',r'X^{\handwritten{2}}+Y^{\handwritten{2}}; \handwritten{/}','12:068 two exponent 2s and three slash separators individually enlarged.')
for a,e in [('car','caractéristique'),(r'N\textsuperscript{\uline{o}}','numéro'),('NB','nota bene'),('réf','référence')]:r.r.setdefault('abbreviations',[]).append(dict(abbreviation=a,expansion=e,attestations='12:068'))
r.r['inventory_overrides']={'068-18':dict(first_words_or_objects='deleted é after la, resolved'), '068-21':dict(first_words_or_objects='la technique; qualified dévis')}
for i,(s,k,p,h) in enumerate([
 ('x over opening parenthesis in f(x)','text','curve example','typewriter'),
 ('qualified overprints in ordinaire','text','point double ordinaire','typewriter'),
 ('qualified q/a overlap in local','text','anneau local','typewriter'),
 ('o/l overlap in plausible','text','right edge above question','typewriter'),
 ('a/i overlaps in Mais','text','last paragraph','typewriter'),
 ('two isolated hook-like marks, function/origin uncertain','drawing','left margin beneath point','another unnamed hand'),
 ('archive sheet number 67 retained as comment','margin note','bottom-left corner','another unnamed hand')],1):
 r.r['inventory_extra'].append(dict(scan='12:068',sheet_kind='cancelled_draft',hand=h,element=f'068-R{i:03d}',kind=k,position=p,first_words_or_objects=s,transcribed='yes'))
r.r['crops']=json.loads(Path('work/crops12_068.json').read_text())+json.loads(Path('work/fine12_068.json').read_text())
r.r['inspection_note']='Root alone viewed whole068 and both actual supplied halves before C/H, then all four macro doubts and four doubts-table rows, all five slips, two abbreviation entries and all21 inventory elements. H has no text; no H collation rows are made. All82 crop recipes were viewed; refblank/Mais from a truncated call were re-viewed before counting. Every mathematical sign/index, cancellation, insertion, dense overprint and margin mark was enlarged. Both long global cancellation strokes were followed to their endpoints; no slanted verbal note occurs. Both actual supplied halves were reread line by line after the crops. Line-break splits are joined; no missing arrows, brackets or references supplied. Archive67 remains a comment only. The hooks are recorded as shapes with uncertain function/origin. Context remains sealed. This is first-pass collation, not the ordered audit or a mathematical check.'
r.save('work/record12_068.json')
