from pathlib import Path
import json
base=Path('/workspace/scratch/d27bd2a88bca');page='C123-01_123_scan016'
cb=json.loads((base/f'out/work/{page}_crop_boxes.json').read_text())
changes=[]
def add(line,c,h,final,shows,crop,confidence,kind,cc,ch,marked=False,cons=False,certainty=False):
 changes.append({'id':f'P016.{len(changes)+1:02d}','line':line,'c':c,'h':h,'final':final,'scan_shows':shows,'crop':str(base/f'out/crops/{page}_{crop}.png'),'box':cb[crop],'confidence':confidence,'kind':kind,'changed_C':cc,'changed_H':ch,'marked_in_H':marked,'consequential':cons,'certainty_only':certainty})
add('handwritten reference above body 3',r'\unsure{1.2|12}','4.2',r'\unsure{1.2|4.2}','There is a distinct low dot between the two digits. The first digit has a hooked horizontal entry and descending stroke; its incomplete upper form does not securely distinguish 1 from 4. 1.2 is retained first, while 12 is excluded by the dot.','01','medium','misread symbol or index',True,True)
add('body 2',r'\handwritten{\unsure{\mathfrak{g}|\mathscr{G}}}',r'\mathfrak{g}',r'\handwritten{\mathfrak{g}}','The letter has a small upper loop and a long descending right stem with a lower return, the minuscule g form repeated at every Lie-algebra occurrence on this leaf. It is not a separate capital script G.','02','high','misread symbol or index',True,False,False,False,True)
add('body 3','Lie.','Lie,','Lie,','The stop after Lie has a clear downward-left comma tail.','03','high','misread symbol or index',True,False)
add('body 4 and above',r'(avec $e\ne0$, $e$ nilpotent.) after Soient',r'avec $e\neq0$, $e$ nilpotent. after Lie',r'\inserted{avec $e\handwritten{\ne}0$, $e$ nilpotent.} after $x,e\in\mathfrak{g}$','The curved marks around the added clause join into a continuous bracket whose point meets the gap after x,e∈g and its comma. They are attachment strokes, not separately keyed parentheses. The clause is typed, with the inequality completed by hand.','03','high','insertion or placement',True,True)
add('body 4',r'\inserted{\handwritten{(i)}}','(i)',r'\inserted{\handwritten{(i)}}','The (i) is above the normal body baseline, accompanied by an oblique insertion stroke before Soient.','03','high','insertion or placement',False,True)
add('body 4','Soient','Soient',r'Soi\deleted{\unsure{t}}ent','The e position contains a high vertical remnant and cross stroke consistent with a t under the live e. The overtyping state is visible, but the old t remains provisional.','03','medium','deletion state (struck given live or live given struck)',True,True)
add('body 4',r'$x,e\in\mathfrak{g}$, Pour',r'$x,e\in\mathfrak{g}$; pour',r'$x,e\handwritten{\in\mathfrak{g}}$, Pour','The source has a comma after the completed formula and a capital typed P in Pour. The vertical connector descending before Pour belongs to the added clause, not a semicolon.','03','high','misread symbol or index',False,True)
add('body 5',r'propre de\hspace{1.5em} correspondant',r'propre de \ill{} correspondant',r'propre de\hspace{1.5em} correspondant','The machine left a blank after de; no handwritten symbol occupies it. H’s own editorial note acknowledges this blank. It must not be represented as unreadable ink.','04','high','text not on the page',False,True,True)
add('body 6',r'\deleted{décomposition}','(omitted)',r'\deleted{décomposition}','The complete typed word décomposition remains legible under a row of cancellation x characters, before the live composants.','05','high','omission',False,True)
add('body 8',r'\unsure{équivalentes}','équivalentes',r'équiva\deleted{\unsure{e}}lentes','There is a separate overstruck character between équiva and lentes. An e is the best provisional reading beneath the cancellation x; it is not safe to suppress the extra character and treat the word as an untouched équivalentes.','06','medium','deletion state (struck given live or live given struck)',True,True)
add('body 9, a)','est un isom','est un isom.','est un isom.','A terminal dot is visible just after the m, very near the paper’s right edge.','07','high','omission',True,False)
add('body 10, b)',r'\handwritten{\deleted{\unsure{et}}}','(omitted)',r'\handwritten{\deleted{\unsure{et}}}','A small handwritten word is scribbled out between e∈g(2), and ad(e). Lower e-like and t-like remnants support et, but the cancellation prevents every letter from being certain.','08','medium','omission',False,True)
add('addition to b)','par','pour','pour','After f(x_o), the pen clearly forms p followed by joined o and u and a final r: pour.','09','high','misread word',True,False)
add('addition to b)',r'f(x_{\unsure{o|0}})',r'f(x_0)',r'f(x_o)','The handwritten small round subscript matches the repeated o indices in the typed formulas below. It is encoded as lower-case o, with no remaining first-occurrence alternative.','09','high','misread symbol or index',True,True)
add('addition to b)',r'\operatorname{Sl}(2,\unsure{k\prime|k})',r'\operatorname{Sl}(2,k)',r'\operatorname{Sl}(2,k)','The short rising stroke belongs to k and the following larger curved stroke is the closing parenthesis; there is no separate prime mark between them.','09','high','misread symbol or index',True,False,False,True)
add('struck b′',r'\uline{\unsure{bijectif}}',r'\ill{}',r'\uline{\unsure{bijectif}}','The word under the heavy cancellation has a b ascender, i/j strokes and the terminal t/i/f structure of bijectif, together with an underline. Several middle strokes are masked, so the reading remains doubtful rather than wholly illegible.','10','medium',r'readable ink left as \ill{}',False,True,True)
add('body 13, d)',r'f^{\handwritten{\unsure{\prime\prime|\prime}}}(x_o)',r"f'(x_0)",r"f^{\handwritten{'}}(x_o)",'There is one dark handwritten prime beside the second f. A much paler offset smudge above it does not form a second dark prime of the same kind.','11','high','misread symbol or index',True,False,False,True)
add('body 13, d)',r'e_o, x_o',r'e_0, x_0',r'e_o, x_o','Both low indices are lower-case typewritten o forms, shorter and rounder than the body digit 0 in the same typeface.','11','high','misread symbol or index',False,True)
add('body 13, d)',r'x\deleted{\unsure{y}}','x',r'x\deleted{y}','The cancelled character after the final x has the fork and descending lower stroke of y, visible beneath the overtyped cancellation.','11','high','omission',True,True)
add('body 14',r'(x_o,e_o,f_o)',r'(x_0,e_0,f_0)',r'(x_o,e_o,f_o)','All three tuple indices are the same small typewritten o glyph used in d), not the taller digit 0.','12','high','misread symbol or index',False,True)
add('body 16',r'C\overset{\unsure{-}}{\underset{\text{\unsure{e}}}{\text{e}}}s','Ces',r'C\overset{-}{\underset{\text{\unsure{e}}}{\text{e}}}s','The baseline word Ces is clear. Above its e is a definite short horizontal dash; below it is a partly inked small e-like glyph. Neither extra mark is struck through. The lower glyph remains uncertain.','13','medium','omission',True,True)
add('body 16',r"\unsure{qu'il|qu'ib}","qu'il",r"qu'i\deleted{\unsure{o|b}}l",'The last character contains a tall l stem and top serif superposed on a closed round lower bowl. The bowl extends to the left of the l stem, favouring an old o; an old b remains possible. Retain the overtyping rather than select a single untouched word.','14','medium','deletion state (struck given live or live given struck)',True,True)
add('body 19',r'\unsure{homomorphisme}','homomorphisme','homomorphisme','The word is readable through homomorphism and the left curved portion and bar of the final e remain at the cut paper edge. The clipping does not leave another plausible reading.','15','high','misread word',True,False,False,False,True)
add('body 20',r'f(e_o)=e; f(u_o)=u',r'f(e_0)=e; f(u_0)=u',r'f(e_o)=e; f(u_o)=u','The two formula indices are lower-case typewritten o, matching the tuple and both formulas in d).','16','high','misread symbol or index',False,True)
add('body 21',r'u_o=\exp(e_o)',r'u_0=\exp(e_0)',r'u_o=\exp(e_o)','The index of u and the index inside exp are again the same small lower-case o glyphs. The enclosing parentheses and terminal semicolon are also visible.','17','high','misread symbol or index',False,True)
add('addition above body 21',r'x=f(x_o)\text{ i.e., par }i=f\circ i_o',r'x=f(x_0)\text{ i.e. par }i=f\circ i_0',r'x=f(x_o)\text{ i.e., par }i=f\circ i_o','The insertion uses the same round o subscripts after x and i. There is a small comma after i.e. before par. The earlier pale par following déterminé remains doubtful separately.','18','high','misread symbol or index',False,True)
add('body 21',r'\unsure{En}','En',r'\deleted{e}\handwritten{E}n','The first letter retains the rounded lower loop of a typed e, while darker freehand strokes supply the upper bar and left side of E. This is tentatively read as e corrected to E by pen.','18','medium','deletion state (struck given live or live given struck)',True,True)
add('body 21, before lorsque',r'\deleted{\unsure{(}}','(omitted)',r'\deleted{\unsure{(}}','A cancelled glyph occupies the space after the comma and before lorsque. A curved left-side remnant supports an opening parenthesis, but its middle is buried under cancellation strokes; retain the doubt.','19','medium','omission',False,True)
add('body 22',r'e=0',r'e\neq0',r'e=0','The typed equals sign consists of two horizontal strokes with no diagonal through it. The nearby handwritten diagonal is at i.e., not at this equals sign.','20','high','misread symbol or index',False,True,False,True)
add('body 22','i.e.','i.e.',r'i\handwritten{/}.e.','A distinct dark pen slash descends leftward through the vicinity of the first stop in i.e. It has no arrowhead and does not cross the equals sign at e=0. Its physical position is retained; its intended role is uncertain.','20','high','omission',True,True)
add('body 25',r'\deleted{sous les éléments de}\inserted{par $\handwritten{Z=}$}',r'par $Z=$',r'\deleted{sous les éléments de}\inserted{par $\handwritten{Z=}$}','The full typed phrase sous les éléments de is cancelled by overtyped x characters and a stroke. Typed par appears above it, while Z= is handwritten above the final part and before Cent(e). Both old phrase and replacement are retained.','21','high','omission',False,True)
add('body 26',r'\deleted{sous} par','par',r'\deleted{sous} par','All four letters sous remain readable below the cancellation x characters, followed by the live typed par.','22','high','omission',False,True)
add('body 26',r'\operatorname{Cent}(u)),',r'\operatorname{Cent}(u))',r'\operatorname{Cent}(u)),','A comma is plainly typed after the two closing parentheses at the right edge.','22','high','omission',False,True)
add('body 27',r'\deleted{\unsure{morphismes}\quad $g$\quad $\operatorname{int}(g)$}','(omitted)',r'\deleted{\unsure{morphismes}\quad $g$\quad $\operatorname{int}(g)$}','The old run contains a word consistent with morphismes, then g and int(g), all crossed out. Much of the word is readable but its last part remains covered enough to retain C’s doubt; g and int(g) are clear.','23','medium','omission',False,True)

doubts=[
 {'line':'reference above body 3','reading':'1.2','alternatives':['4.2'],'confidence':'medium','reason':'The decimal stop is certain; the initial hooked digit remains between 1 and 4. No bibliography lookup was used.'},
 {'line':'body 4','reading':r'Soi\deleted{\unsure{t}}ent','alternatives':['old letter not fully identifiable'],'confidence':'medium','reason':'A high stem and cross stroke appear beneath the live e; t is provisional.'},
 {'line':'body 8','reading':r'équiva\deleted{\unsure{e}}lentes','alternatives':['old letter not fully identifiable'],'confidence':'medium','reason':'The extra cancelled character is certain, but the e underneath x cannot be completely isolated.'},
 {'line':'body 10, b)','reading':r'\deleted{\unsure{et}}','alternatives':[],'confidence':'medium','reason':'The scribble leaves e-like and t-like remnants, not every original stroke.'},
 {'line':'struck b′','reading':r'\mathfrak{g}(\unsure{2|-2})','alternatives':[r'\mathfrak{g}(-2)'],'confidence':'low','reason':'The deletion crosses the position at which a minus could stand. The upper part of 2 is visible; absence of a minus cannot be established.'},
 {'line':'struck b′','reading':r'\uline{\unsure{bijectif}}','alternatives':[],'confidence':'medium','reason':'Ascenders, descenders and ending favour bijectif, but several middle strokes are masked. The doubt under deletion is retained.'},
 {'line':'body 16','reading':r'\underset{\text{\unsure{e}}}{\text{e}}','alternatives':['partially printed round glyph'],'confidence':'medium','reason':'Only the upper loop and a faint horizontal trace of the extra lower glyph survive clearly. The baseline e and upper dash are certain.'},
 {'line':'body 16','reading':r"qu'i\deleted{\unsure{o|b}}l",'alternatives':[r"qu'i\deleted{b}l"],'confidence':'medium','reason':'A round bowl remains below the live l. Its left extent favours o; b cannot be fully excluded.'},
 {'line':'addition above body 21','reading':r'déterminé \unsure{par} x=f(x_o)','alternatives':[],'confidence':'medium','reason':'The first par is extremely pale. Its descending first stroke and low following traces support the word but are not uniformly clear.'},
 {'line':'body 21','reading':r'\deleted{e}\handwritten{E}n','alternatives':['an E with irregular overinking, underlying letter uncertain'],'confidence':'medium','reason':'The rounded typed lower loop and freehand upper strokes favour e corrected to E. The state should receive root review.'},
 {'line':'body 21, before lorsque','reading':r'\deleted{\unsure{(}}','alternatives':[],'confidence':'medium','reason':'Curvature supports an opening parenthesis, but cancellation masks its centre.'},
 {'line':'body 22','reading':r'e=0\text{ i}\handwritten{/}\text{.e. }u\ne1','alternatives':['slash possibly intended as a displaced correction to the preceding equality'],'confidence':'high','reason':'The ink and its position are certain; the function of the pen slash is not. The mathematical inconsistency is retained, not emended.'},
 {'line':'body 27','reading':r'\deleted{\unsure{morphismes}}','alternatives':[],'confidence':'medium','reason':'The word is strongly suggested but the cancellation still covers part of its final letters.'}
]

inventory=[]
def inv(element,kind,position,first,hand='typewriter with handwritten mathematical completions'):
 inventory.append({'scan':16,'sheet_kind':'typescript','hand':hand,'element':element,'kind':kind,'position':position,'first_words_or_objects':first,'transcribed':'yes'})
inv('title','text','body 1, top of sheet','Résumé de quelques résultats de Kostant','typewriter')
inv('ambient group and Lie algebra','text','body 2–3','G est un groupe semi-simple')
inv('Kostant bibliographical reference','margin note','between body 2 and body 3, extending across upper text','The principal 3-dimensional subgroup....','handwritten annotation; author not independently identified on this leaf')
inv('nonzero nilpotent hypothesis','insertion','above body 4, connected to the comma after x,e∈g','avec e≠0, e nilpotent.','typewriter; inequality and attachment bracket in pen')
inv('theorem part marker','insertion','above body 4 before Soient','(i)','handwritten')
inv('theorem setup and graded spaces','text','body 4–8','Théorème 1. Soient x,e∈g')
inv('correction within Soient','deletion','body 4, e position','t beneath e, provisionally read','overtyping')
inv('cancelled decomposition noun','deletion','body 6 before composants','décomposition','typewriter, x cancellation')
inv('extra letter inside equivalence word','deletion','body 8 between équiva and lentes','e, provisionally read','typewriter, x cancellation')
inv('condition a','display','body 9','a) e∈g(2) i.e. [x,e]=2e')
inv('quantifier in condition a','insertion','above body 9, before ad(e)^k','pour tout entier k≥1,','typewriter with handwritten inequality and attachment stroke')
inv('condition b','display','body 10','b) e∈g(2), ad(e):g(0)→g(-2) est surjectif')
inv('cancelled connective in b','deletion','body 10 after e∈g(2),','et, doubtful','handwritten and scribbled out')
inv('Dynkin-element restriction in b','insertion','body 10 right end and following interline','et x est de la forme f(x_o), pour f:Sl(2,k)→G','handwritten, élément de Dynkin underlined')
inv('cancelled variant condition b prime','deletion','interline between body 10 and body 11','b′) Comme b), avec ad(e):g(0)→g(2|-2) bijectif','handwritten, heavy horizontal cancellation')
inv('condition c','display','body 11','c) e∈g(2), et x∈ad(e)(g)')
inv('condition c prime','display','body 12','c′) e∈g(2), et x∈ad(e)(g(-2))')
inv('condition d and standard basis','text','body 13–15','d) Il existe un homomorphisme f:Sl(2,k)→G')
inv('cancelled final y in d','deletion','body 13 after x','y','typewriter cancellation')
inv('consequences and uniqueness paragraph','text','body 16–18','Ces conditions impliquent qu’il existe')
inv('stray upper dash and lower partial letter','text','body 16 around the e of Ces','dash above e, uncertain e below','typewriter')
inv('overtyped ending of qu’il','deletion','body 16','o or b beneath l','typewriter')
inv('nilpotent-element existence and conjugacy paragraph','text','body 19–27, continuing off this sheet','(ii) Pour tout élément nilpotent e de g')
inv('uniqueness qualification in ii','insertion','above body 21, after the preceding semicolon','f est uniquement déterminé par x=f(x_o) i.e., par i=f∘i_o.','handwritten with attachment line')
inv('initial E correction','deletion','body 21 at En','e beneath handwritten E, tentative','typewriter and pen correction')
inv('cancelled opening sign','deletion','body 21 immediately before lorsque','opening parenthesis, doubtful','typewriter and cancellation')
inv('pen slash across i.e.','insertion','body 22, through the first stop of i.e.','/','pen stroke, function uncertain')
inv('cancelled conjugacy phrase','deletion','body 25','sous les éléments de','typewriter, x cancellation')
inv('replacement conjugating group prefix','insertion','above body 25 before Cent(e)','par Z=','par typed; Z= handwritten')
inv('cancelled preposition','deletion','body 26 before par Cent(u)','sous','typewriter, x cancellation')
inv('cancelled morphism phrase','deletion','body 27 before f en question','morphismes g int(g)','typewriter, x and line cancellation')
inv('archive sheet number','text','extreme lower left','15; recorded only as archive comment','pen archive numbering')

boxes=[]
def bx(num,kind,b,reading):
 boxes.append({'box':f'P016.B{num:02d}','kind':kind,'x0':b[0],'y0':b[1],'x1':b[2],'y1':b[3],'reading':reading})
bx(1,'handwritten formula',[1324,181,1368,239],r'$\handwritten{\mathfrak{g}}$')
bx(2,'margin note',[359,219,1466,266],r'\margin{\handwritten{(The principal 3-dimensional subgroup...., Am. Jour. Oct.1959, 3.4, 3.5, 3.6, \unsure{1.2|4.2}, 9.3)}}')
bx(3,'punctuation',[275,263,352,298],'Lie,')
bx(4,'insertion',[487,294,548,364],r'\inserted{\handwritten{(i)}}')
bx(5,'overtyping',[515,320,632,365],r'Soi\deleted{\unsure{t}}ent')
bx(6,'handwritten formula',[644,316,793,377],r'$x,e\handwritten{\in\mathfrak{g}}$,')
bx(7,'insertion',[733,250,1230,319],r'\inserted{avec $e\handwritten{\ne}0$, $e$ nilpotent.}')
bx(8,'handwritten formula',[1281,315,1371,378],r'$\handwritten{\mathfrak{g}}(k)$')
bx(9,'blank',[275,389,772,435],r'propre de\hspace{1.5em} correspondant')
bx(10,'handwritten formula',[275,449,479,503],r'$i:\underline{G}_m\handwritten{\longrightarrow}G$,')
bx(11,'handwritten formula',[594,445,686,516],r'$\handwritten{\mathfrak{g}}(k)$')
bx(12,'deletion',[864,448,1110,493],r'\deleted{décomposition}')
bx(13,'handwritten formula',[1376,438,1424,520],r'$\handwritten{\mathfrak{g}}$')
bx(14,'handwritten formula',[835,503,881,583],r'$\handwritten{\mathfrak{g}}$')
bx(15,'overtyping',[754,583,1019,631],r'équiva\deleted{\unsure{e}}lentes:')
bx(16,'formula and insertion',[349,600,1656,716],r'a) $e\handwritten{\in\mathfrak{g}}(2)$ i.e. $\handwritten{[}x,e\handwritten{]}=2e$, et \inserted{pour tout entier $k\handwritten{\geq}1$,} $\operatorname{ad}(e)^k:\handwritten{\mathfrak{g}}(-k)\handwritten{\longrightarrow\mathfrak{g}}(k)$ est un isom.')
bx(17,'formula and deletion',[349,707,1296,758],r'b) $e\handwritten{\in\mathfrak{g}}(2)$, \handwritten{\deleted{\unsure{et}}} $\operatorname{ad}(e):\handwritten{\mathfrak{g}}(0)\handwritten{\longrightarrow\mathfrak{g}}(-2)$ est surjectif,')
bx(18,'insertion',[1294,705,1641,751],r'\inserted{\handwritten{et $x$ est de la forme}}')
bx(19,'insertion',[1017,744,1651,796],r'\inserted{\handwritten{$f(x_o)$, pour $f:\operatorname{Sl}(2,k)\to G$ (\uline{élément de Dynkin}).}}')
bx(20,'deleted formula',[349,748,1020,795],r'\handwritten{\deleted{b′) Comme b), avec $\operatorname{ad}(e):\mathfrak{g}(0)\to\mathfrak{g}(\unsure{2|-2})$ \uline{\unsure{bijectif}}}}')
bx(21,'handwritten formula',[349,783,899,846],r'c) $e\handwritten{\in\mathfrak{g}}(2)$, et $x\handwritten{\in}\operatorname{ad}(e)(\handwritten{\mathfrak{g}})$.')
bx(22,'handwritten formula',[349,840,974,908],r'c′) $e\handwritten{\in\mathfrak{g}}(2)$, et $x\handwritten{\in}\operatorname{ad}(e)(\handwritten{\mathfrak{g}}(-2))$.')
bx(23,'formula and deletion',[930,894,1653,965],r'$f:\operatorname{Sl}(2,k)\handwritten{\longrightarrow}G$ tel que $f^{\handwritten{\prime}}(e_o)=e,f^{\handwritten{\prime}}(x_o)=x\deleted{y}$')
bx(24,'formula',[353,982,542,1042],r'$(x_o,e_o,f_o)$')
bx(25,'stray typed marks',[351,1104,422,1170],r'C$\overset{-}{\underset{\text{\unsure{e}}}{\text{e}}}$s')
bx(26,'overtyping',[847,1111,949,1157],r"qu'i\deleted{\unsure{o|b}}l")
bx(27,'handwritten formula',[1383,1110,1561,1174],r'$i:\underline{G}_m\handwritten{\longrightarrow}G$,')
bx(28,'word at paper edge',[1423,1324,1656,1370],'homomorphisme')
bx(29,'handwritten formula',[1112,1310,1167,1390],r'$\handwritten{\mathfrak{g}}$,')
bx(30,'handwritten formula',[283,1393,553,1446],r'$f:\operatorname{Sl}(2,k)\handwritten{\longrightarrow}G$')
bx(31,'formula',[706,1395,857,1446],r'$f(e_o)=e$,')
bx(32,'formula',[1500,1393,1642,1445],r'$f(u_o)=u$')
bx(33,'formula',[282,1456,765,1514],r'(où $u=\exp(e)$, $u_o=\exp(e_o)$);')
bx(34,'insertion',[773,1415,1538,1468],r'\inserted{\handwritten{$f$ est uniquement déterminé \unsure{par} $x=f(x_o)$ i.e., par $i=f\circ i_o$.}}')
bx(35,'overwriting',[784,1454,835,1501],r'\deleted{e}\handwritten{E}n')
bx(36,'deletion',[1446,1453,1607,1501],r'\deleted{\unsure{(}}lorsque')
bx(37,'formula and pen stroke',[284,1521,547,1575],r'$e=0$ i\handwritten{/}.e. $u\handwritten{\ne}1$,')
bx(38,'handwritten formula',[1002,1514,1070,1586],r'$x\handwritten{\in\mathfrak{g}}$')
bx(39,'handwritten formula',[1353,1584,1534,1644],r'$i:\underline{G}_m\handwritten{\longrightarrow}G$')
bx(40,'deletion and insertion',[469,1696,1144,1763],r'\deleted{sous les éléments de}\inserted{par $\handwritten{Z=}$}$\operatorname{Cent}(e)=\operatorname{Cent}(u)$')
bx(41,'handwritten formula',[1373,1716,1447,1765],r'$e\handwritten{\ne}0$,')
bx(42,'deletion',[1315,1782,1397,1830],r'\deleted{sous}')
bx(43,'formula and punctuation',[1480,1781,1654,1833],r'$\operatorname{Cent}(u)$),')
bx(44,'handwritten formula',[492,1850,567,1897],r'$e\handwritten{\ne}0$,')
bx(45,'deleted run',[633,1846,1084,1900],r'\deleted{\unsure{morphismes}\quad $g$\quad $\operatorname{int}(g)$}')
bx(46,'archive numeral',[38,2064,89,2123],'% archive sheet number: 15')

report={'page':page,'line_count':33,'changes':changes,'doubts':doubts,'inventory':inventory,
 'notes':[
 'Line references body 1–27 count the title and normal typewriter baselines. line_count 33 adds six interlinear text baselines: bibliography, avec clause, quantifier above a), shared b′ / b-addition interline, uniqueness insertion, and par/Z= line. The floating (i), prime marks, stray partial e and archive numeral are not additional text lines.',
 'Visual transcription audit: whole image viewed once for layout; each supplied half viewed once line by line against both C and H. Twenty-four tight context crops were saved with original pixel boxes, enlarged by LANCZOS to 2500 pixels wide, autocontrasted, sharpened and displayed. No OCR or recognition library, web lookup or TeX compilation was used.',
 'Visual transcription audit: every insertion, deletion, handwritten word and formula completion is represented in the inventory or the full-reading boxes. Boxes use original-image coordinates on the 1670 by 2143 image; crop boxes include context, while the second box set targets complete affected words or formulas.',
 'The subject is a summary of Kostant’s rank-one subgroup results: equivalent conditions on x,e, a homomorphism from Sl(2,k), nilpotent-element existence and conjugacy. This is a reading report, not a proof of the theorem.',
 'The source really has a blank after propre de. H editorially expects ad(x), but no such notation is on the paper; the blank is preserved.',
 'The b target g(-2) and the later e=0 i.e. u≠1 are retained as written. Their elementary consistency checks are separately recorded in check_events; neither prompted a silent correction.',
 'There is also a clear pen slash near the first point of i.e. in the latter phrase. It might be a displaced attempt at correcting the preceding equality, but no attachment or arrow establishes that intention. The draft records its actual location.',
 'The bracket enclosing the avec clause is an attachment device pointing after x,e∈g, not a pair of textual parentheses. H places the addition after Lie even though its editorial note describes its true attachment.',
 'The a) condition occupies a single main baseline; its quantifier is an addition above that line. The draft removes C’s artificial two-row formula layout.',
 'The underline beneath élément de Dynkin is distinct from the longer connector beneath the entire b addition. The cancelled b′ line remains separate.',
 'The small indices are consistently typewriter o rather than 0; the full-sized zero in e=0 and g(0) provides a same-page comparison. Handwritten indices are read consistently with these visually confirmed forms.',
 'The source has no manuscript page number at the head. The pen 15 in the lower-left corner is recorded only in the archive-sheet comment.',
 'No diagrams or drawings occur. Pen brackets and connecting strokes identify insertions and do not constitute independent figures.',
 'Witness H’s explanatory notes, page marker and enumerate/environment syntax are editorial and not transcribed. Thin-space commands are not commas. Its presentation of Théorème as bold is treated as emphasis markup; the actual source underline is retained.',
 'Four closely spaced points after subgroup are retained in the handwritten title reference; H’s ellipsis is treated as editorial punctuation representation rather than a new word. The ambiguous citation digit is not resolved from bibliographical knowledge.',
 'Newly identified layers at Soient, équivalentes, qu’il and En remain explicitly provisional where their underlying characters are not completely exposed. Root should inspect crops 03, 06, 14 and 18 before accepting those changes.'
 ],
 'check_events':[
 {'statement_id':'P016.b.target','type':'targeted proof check','outcome':'Local grading check only: with [x,e]=2e and [x,v]=0, Jacobi gives [x,[e,v]]=2[e,v]. Thus ad(e) carries g(0) into g(2), whereas the source b) prints g(-2). This flags a likely source sign slip and triggers visual confirmation; the source -2 is retained. No proof of the theorem’s equivalence is claimed.'},
 {'statement_id':'P016.ii.zero','type':'computation or formal certificate','outcome':'Elementary computation only: exp(0)=1, so the source phrase e=0 i.e. u≠1 conflicts with its definition u=exp(e). Crop 20 confirms an uncrossed equals sign and a separate nearby slash. The inconsistency is recorded without emending the ink; no software formal certificate was produced.'},
 {'statement_id':'P016.other_assertions','type':'carried as background without fault found','outcome':'The remaining equivalence, existence, uniqueness and conjugacy assertions were used only as reading context, excluding the two specifically flagged local slips. They were not independently re-proved or verified in full. Visual transcription checks are recorded in notes, not counted as mathematical proof checks.'}
 ],
 'notation':[
 r'$\mathfrak{g}$ is handwritten with a small upper loop, tall right stem and long returning descender; all occurrences inspected on scan 16 share this form. The first C ambiguity with script capital G is resolved to the minuscule Lie-algebra letter.',
 r'The typed indices in $(x_o,e_o,f_o)$, $f(e_o)$, $f(u_o)$ and $u_o=\exp(e_o)$ are lower-case o. Do not normalize them to digit 0. Handwritten $x_o$ and $i_o$ agree with this usage.',
 r'$\underline{G}_m$: G is typewritten and separately underlined; the m is a lowered typewriter character. Its handwritten map arrows are single shafts with ordinary right arrowheads.',
 r'$f^{\handwritten{\prime}}$: primes in condition d) are supplied by hand. Each f has one dark prime; the faint offset trace beside the second is not a second live prime.',
 r'$\operatorname{Sl}(2,k)$ is the source’s capital S, lower-case l; do not expand the group notation or introduce a prime on k.',
 'Abbreviations car., i.e., isom., Am. Jour. and the journal date are retained without expansion.'
 ],
 'hand_log':[
 'Scan 16: the handwritten g used for the Lie algebra has a minuscule upper loop and a long right descender; every inspected occurrence on this page agrees. C doubted the first occurrence as script G; H read fraktur g.',
 'Scan 16: in pour in the Dynkin insertion, the joined o/u sequence is compressed and can be mistaken for a. C read par, but the crop shows four letters. This is a local observation, not evidence that every u on the cote has the same misleading form.',
 'Scan 16: the first par in the uniqueness insertion is very pale; the later par on the same insertion is darker. The pale word remains unsure despite a strong contextual fit.',
 'Scan 16: the reference digit before .2 has a horizontal hooked entry; 1 and 4 remain possible. The point separating it from 2 is clearly present. C’s 12 alternative is excluded, while H’s 4.2 remains an alternative.',
 'Scan 16 typescript: old letters can remain below corrective strikes or new letters. Provisional t→e in Soient, extra cancelled e in équivalentes, o/b→l in qu’il and e→E at En should not be generalized beyond their crops until root review.',
 'Scan 16 typescript: lower-case o was used as a low index, visibly shorter and rounder than the normal digit 0. H consistently normalized these indices to 0.',
 'Scan 16: handwritten inequality slashes are darker and less mechanically regular than the typed parallel equality bars. One such slash stands at i.e., away from the uncrossed e=0 equality; its intended function is unresolved.'
 ],'boxes':boxes}
path=base/f'out/work/{page}_report.json'
path.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(path)
print('changes',len(changes),'doubts',len(doubts),'inventory',len(inventory),'second boxes',len(boxes))
