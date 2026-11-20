import sys,json
from pathlib import Path
sys.path.insert(0,'SP02_CW_10+12/scripts')
from root_record import Record
r=Record('B10-04',10,68);ch=r.change
r.edit(r'\geq',r'\geqslant',count=2)
r.edit(r'M^{\handwritten{\sigma}}',r"M^{\handwritten{\unsure{\sigma|\sigma'}}}",count=2)
# The second exponent has a different local ambiguity: two visible sigma impressions.
r.edit(r"M^{\handwritten{\unsure{\sigma|\sigma'}}}=M",r'M^{\handwritten{\unsure{\deleted{\sigma}\sigma|\sigma}}}=M')
r.edit(r'\deleted{cr}',r'\deleted{\unsure{cr|er}}')
r.edit(r'\operatorname{FCriso}(\unsure{k|h})',r'\operatorname{FCriso}(\unsure{\deleted{h}k|\deleted{k}h})')
r.edit(r'\deleted{\unsure{teur}}',r'\deleted{te\unsure{u}}')
r.edit(r'\unsure{\div|:|=}',r'\unsure{\deleted{=}:|\deleted{:}=|\div}')
r.edit('isogénie i.e.',r'isogénie \unsure{\deleted{n}i|\deleted{i}n|i}.e.')
r.edit(r'\mathrm{Fc}\handwritten{ri}\mathrm{s}(k)',r'\mathrm{Fc}\unsure{\deleted{\mathrm{ir}}\handwritten{ri}|\handwritten{ri}}\mathrm{s}(k)')
r.edit(r'le cristal \uline{unité}',r'le c\unsure{\deleted{i}r|\deleted{r}i}\unsure{\deleted{r}i|\deleted{i}r}stal \uline{unité}')
r.edit(r'\uline{isocristaux} \handwritten{(}',r'\uline{\unsure{\deleted{c}i|\deleted{i}c}\unsure{\deleted{r}s|\deleted{s}r}ocristaux} \handwritten{(}')
curve=r'\begin{tikzpicture}[x=1cm,y=1cm,baseline=-.05cm]\draw[thick] (.12,.3).. controls (-.1,.1) and (-.12,-.1)..(.12,-.26);\end{tikzpicture}'
r.edit(r'\handwritten{\unsure{(}}',r'\handwritten{'+curve+'}')
r.edit(r'$F$\handwritten{(}-cristal',r'$F$\handwritten{'+curve+'}-cristal',count=2)
slash=r'\begin{tikzpicture}[x=1cm,y=1cm,baseline=-.05cm]\draw[thin] (-.1,-.4)--(.14,.45);\end{tikzpicture}'
r.edit(r'\inserted{\handwritten{\ }}',r'\handwritten{'+slash+'}')
hook=r'\begin{tikzpicture}[x=1cm,y=1cm,baseline=-.1cm]\draw[thin] (0,.15).. controls (.05,-.1) and (-.2,-.1)..(-.7,-.1).. controls (-1,-.1) and (-1.3,-.2)..(-1.3,-.5);\end{tikzpicture}'
for t in [r'$K(-1)$',r'$W(-1)$']:r.edit(r'\inserted{'+t+'}',r'\inserted{'+t+r'}\handwritten{'+hook+'}')
pluscurve=r'\begin{tikzpicture}[x=1cm,y=1cm,baseline=-.05cm]\draw[thin] (-.4,.6).. controls (-.45,.2) and (.1,.4)..(.1,.05).. controls (.1,-.25) and (-.6,-.05)..(-.62,-.4);\end{tikzpicture}'
r.edit(r'\operatorname{FCriso}^{\inserted{\handwritten{+}}}(k)',r'\operatorname{FCriso}^{\inserted{\handwritten{+}}}\handwritten{'+pluscurve+'}(k)')
marks=r'\mathord{\begin{tikzpicture}[x=1cm,y=1cm,baseline=0cm]\draw[thick] (0,0)--(.15,.015);\draw[thick] (.23,.025)--(.31,.005);\end{tikzpicture}}'
r.edit(r'\unsure{\cdot\ \cdot}',marks)
ch('opening and definition emphasis','underlines','italic','underlines on Hom, non dégénéré, isocristaux effectifs, selected Tate words, unité and final category phrase','Separate horizontal pen rules are visible; F and its hyphens are excluded from the relevant rules.','top; hom; tate; middle','other','high',False,True)
ch('two nonnegative inequalities','geq','geq','geqslant','Both lower strokes rise to the right parallel to the lower arm of the greater-than sign.','ge1; ge2','misread symbol or index','high',True,True)
ch('first sigma exponent','sigma','sigma',r"\unsure{\sigma|\sigma'}",'A pale ascending stroke rises above the long dark tail. It may be a prime or an incidental part of the pen motion.','firstsigma','misread symbol or index','low',True,True)
ch('first category name','FCriso plus','FCris double dagger','FCriso plus','The final typed o is a complete closed bowl; the raised pen sign has one horizontal and one vertical stroke.','cat1','misread symbol or index','high',False,True,False,True)
ch('first category curved mark','omitted','omitted','curved mark around o and plus in TikZ','A fine curve begins above the o, runs to its right and turns below it with a descending left end.','cat1','drawing or diagram','high',True,True)
ch('cancelled category phrase','des isocristaux',r'\ill{}','des isocristaux','The complete letters remain visible under the repeated x row and central horizontal line.','canceliso','readable ink left as \\ill{}','high',False,True,True)
ch('short cancelled fragment','cr',r'\ill{}',r'\unsure{cr|er}','The second letter is r; the first has a c-shaped outer curve with a dense middle trace that may belong either to e or the cancellation.','cancelcr','readable ink left as \\ill{}','low',True,True,True)
ch('cancelled extra z','z','omitted','z','The cell between i and s has a z-like diagonal and top/bottom strokes beneath the overtyped x.','cancelz','omission','high',False,True)
ch('Tate separator','inserted blank','ordinary space','oblique pen separator drawn in TikZ','A fine slash crosses the underline between the tightly adjacent typed Tate and inverse.','tatesep','drawing or diagram','high',True,True)
ch('K(-1) attachment','omitted','omitted','curved insertion bracket in TikZ','The pen line below the raised K(-1) descends before est.','Kinsert','drawing or diagram','high',True,True)
ch('W(-1) placement','after F-cristal','after p.id','after F-cristal','The raised W(-1) sits above défini; its bracket lands between cristal and défini.','Winsert; tate','insertion or placement','high',False,True,False,True)
ch('W(-1) attachment','omitted','omitted','curved insertion bracket in TikZ','The bracket bends upward at its right end and drops just before défini.','Winsert','drawing or diagram','high',True,True)
ch('three F-hyphen curves','parenthesis glyph, first uncertain','omitted','three bowed pen curves drawn in TikZ','Each curve crosses the hyphen after F, with its concavity opening right. Their shape is copied without assigning a punctuation function.','Fcurve1; Fcurve2; Fcurve3','drawing or diagram','high',True,True)
ch('cristal unité two middle cells','cristal','cristal',r'c\unsure{\deleted{i}r|\deleted{r}i}\unsure{\deleted{r}i|\deleted{i}r}stal','Both cells after c have an r shoulder and an i dot/stem. The two overtyped impressions are visible, but their temporal order is not.','cristal','misread word','low',True,True)
ch('p-id separator','baseline period','centered multiplication dot','baseline period','The round point between p and id sits on the typed baseline.','tate','misread symbol or index','high',False,True)
ch('second category name','two r positions, upper uncertain dots, terminal o','FCris plus','two r positions, two short upper strokes, terminal o, plus','A second r lies beneath the baseline r. The upper marks are short horizontal strokes, and a separate o follows s.','cat2','misread symbol or index','high',True,True,False,True)
ch('cancelled des','des',r'\ill{}','des','The d ascender, e bar and s outline survive beneath the three cancellation cells.','des','readable ink left as \\ill{}','high',False,True,True)
ch('comma after inverse K(-1)','comma','omitted','comma','A long pen comma lies below the closing parenthesis before alors.','Kminus','omission','high',False,True)
ch('base ring font','plain underlined Q','double-struck underlined Q','plain underlined Q','The letter has one bowl and a short tail; the horizontal rule is separate below it.','tate','misread symbol or index','high',False,True)
ch('third category argument',r'\unsure{k|h}','k',r'\unsure{\deleted{h}k|\deleted{k}h}','The same cell contains a tall h-like arch and k-like diagonal arms. Both impressions are present; their order is uncertain.','cat3','misread symbol or index','low',True,True,False,True)
ch('isocristaux overwritten first cells','isocristaux','isocristaux',r'\unsure{\deleted{c}i|\deleted{i}c}\unsure{\deleted{r}s|\deleted{s}r}ocristaux','The first cell has both a c curve and dotted i; the second has both an r shoulder and s curves. Their correction order is not established by the ink.','isocr','misread word','low',True,True)
ch('cancelled pa and placement','cancelled pa before a','cancelled pas after a','cancelled pa before a','Two crossed cells p and a stand before the live a. No third s cell follows them.','pa; middle','misread word','high',False,True)
ch('risque clause','a pas risque','a pas de risque','a pas risque','The live words pas and risque are adjacent with no de.','middle','text not on the page','high',False,True)
ch('cancelled foncteur fragment',r'\unsure{teur}','omitted',r'te\unsure{u}','The clipped line end retains t and e, followed by part of a u-like cell. The proposed final r falls beyond the visible edge and is not supplied.','teur','omission','medium',True,True)
ch('sans iso clause',r'live iso and uncertain close parenthesis','deleted isogénie and closing parenthesis',r'live iso and uncertain close parenthesis','The visible i, s and clipped o have no x cancellation. Curved traces at the edge support, but do not fully disclose, a closing parenthesis. No génie is visible.','sansiso','deletion state (struck given live or live given struck)','medium',False,True)
ch('display label separator',r'\unsure{\div|:|=}',':',r'\unsure{\deleted{=}:|\deleted{:}=|\div}','Two horizontal bars coexist with one upper and one lower round mark. Colon/equality overtyping in either order is possible; the earlier division-sign candidate is retained.','formcolon','misread symbol or index','low',True,True,False,True)
ch('display sigma layering','sigma','sigma',r'\unsure{\deleted{\sigma}\sigma|\sigma}','A pale lower loop/tail and a dark higher loop/tail are both visible. An earlier sigma overwritten by another versus one retraced sigma remains unresolved.','sigmasup','misread symbol or index','low',True,True)
ch('i.e. first cell','i','i',r'\unsure{\deleted{n}i|\deleted{i}n|i}','The dotted cell has a second right upright and upper arch; n/i overtyping versus a doubled i impression is unresolved.','ie','misread word','low',True,True)
ch('last cancelled category','Fiso','omitted','Fiso','The F and i-s-o cells remain readable through the overtyped x cancellation.','lastcat','omission','high',False,True)
ch('last live category','Fcris with handwritten ri','FCris plus','Fcris with handwritten ri and possible cancelled typed ir; no plus','The c is lowercase. Pen ri overlaps typed stems that may spell ir; no raised plus is present.','lastcat','misread symbol or index','medium',True,True,False,True)
for a,b,c,d in [('first sigma exponent','sigma','sigma-prime','low'),('short cancelled fragment','cr','er','low'),('cristal unité cells','i/r and r/i corrections','reverse correction orders','low'),('third category argument','old h then k','old k then h','low'),('isocristaux first two cells','old cr then is','reverse orders in either cell','low'),('cancelled clipped foncteur fragment','teu','last u partly clipped; no r visible','medium'),('sans iso close parenthesis',')','only parts of curved edge trace visible','medium'),('display separator','colon over equality','equality over colon; division sign','low'),('display sigma','old sigma then sigma','single retraced sigma','low'),('i.e. first cell','old n then i','old i then n; doubled i','low'),('last category underlayer','typed ir below pen ri','no separable earlier word','medium')]:r.doubt(a,b,c,d)
r.notation('nonnegative inequality','geqslant','10/068 i and m')
r.notation('F-hyphen pen curves','left-parenthesis-shaped drawn strokes','10/068 three F-cristal occurrences','shape clear; punctuation function unspecified')
r.notation('first sigma exponent',r"\sigma | \sigma'",'10/068 nondegeneracy definition','unresolved pale upper tick')
r.notation('display label separator',r'colon over equality | equality over colon | division sign','10/068 final display','unresolved layered sign')
r.notation('coefficient ring','single-stroke underlined Q','10/068 tannakian-category clause')
r.r['inventory_overrides']={}
for id in ['068-002','068-011','068-013','068-014','068-020','068-025','068-026']:
 r.r['inventory_overrides'][id]={'kind':'drawing','first_words_or_objects':'pen underline beneath typed words'}
for id in ['068-018','068-029','068-041']:r.r['inventory_overrides'][id]={'kind':'drawing','first_words_or_objects':'bowed curve crossing F-hyphen'}
r.r['inventory_overrides'].update({'068-003':{'first_words_or_objects':'geqslant'},'068-031':{'first_words_or_objects':'geqslant'},'068-009':{'first_words_or_objects':r'\unsure{cr|er}'},'068-015':{'kind':'drawing','first_words_or_objects':'oblique separator between Tate and inverse'},'068-016':{'kind':'drawing','first_words_or_objects':'same oblique separator'},'068-021':{'kind':'drawing','first_words_or_objects':'two short upper horizontal strokes'},'068-032':{'first_words_or_objects':r'te\unsure{u}, clipped after partial u'},'068-037':{'first_words_or_objects':'two bars and two dots; colon/equality overtype or division'},'068-043':{'first_words_or_objects':'handwritten ri over possible typed ir'}})
for id,pos,txt,hand,kind in [('cat1-hook','first category','curved mark around o and plus','his hand','drawing'),('K-hook','K(-1) addition','curved insertion bracket','his hand','drawing'),('W-hook','W(-1) addition','curved insertion bracket','his hand','drawing'),('cristal-layers','cristal unité','two i/r composite cells','typewriter','deletion'),('kh-layer','FCriso argument','h/k composite cell','typewriter','deletion'),('isocr-layers','isocristaux first cells','c/i and r/s overlapping impressions','typewriter','deletion'),('display-sigma','M superscript','possible earlier sigma','his hand','deletion'),('ie-layer','i.e. initial','possible n/i overtyping','typewriter','deletion'),('last-ri-layer','last category','possible typed ir beneath handwritten ri','typewriter','deletion')]:r.r['inventory_extra'].append(dict(scan='10:068',sheet_kind='typescript',hand=hand,element='068-'+id,kind=kind,position=pos,first_words_or_objects=txt,transcribed='yes'))
r.r['abbreviations']=[dict(abbreviation='sss',expansion='si et seulement si',attestations='10/068 final paragraph'),dict(abbreviation='i.e.',expansion='id est',attestations='10/068 final paragraph'),dict(abbreviation='iso',expansion='isogénie-related qualifier; literal abbreviated form retained',attestations='10/068 terminology and sans iso')]
r.r['crops']=json.loads(Path('work/crops068.json').read_text())
r.r['inspection_note']='Whole then both halves read before witnesses. Every text line, mathematical capital, index, relation and repeated category spelling was read in enlarged blocks. All C doubts, C/H differences, deleted fragments, inserted symbols, pen curves and new composite letter cells were separately magnified. No slanted prose occurs; slashes and curves are represented as drawings. Right-edge completions not visible are not supplied. No OCR, later page or sealed context used.'
r.save('work/record068.json')
