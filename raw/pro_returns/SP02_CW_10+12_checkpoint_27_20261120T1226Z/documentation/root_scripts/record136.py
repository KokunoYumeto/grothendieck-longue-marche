from pathlib import Path
import sys,json
sys.path.insert(0,str(Path('SP02_CW_10+12/scripts').resolve()))
from root_record import Record
r=Record('B10-10',10,136);ch=r.change
r.edit(r'G\unsure{\times|x}V',r'G\mathrm{x}V')
r.edit(r'V\times V',r'V\mathrm{x}V')
r.edit(r'W\times G',r'W\mathrm{x}G')
r.edit('péries',r'\rlap{p}séries')
r.edit(r'coc\deleted{\unsure{c}}omplète',r'coc\deleted{c}omplète')
r.edit(r'\geq\unsure{2|1}',r'\geq\unsure{\rlap{\(1\)}2|2|1}')
r.edit(r'g_{2}\ldots g_{n}',r'g_{2}\cdots g_{n}')
r.edit(r'\unsure{varaables|variables}',r'var\rlap{a}i\rlap{a}ibles')
r.edit(r'\unsure{car|car.}',r'car')
r.edit(r'\draw (n.center) ellipse [x radius=1.05cm,y radius=0.33cm];',r'\draw (1.01,.10) arc[start angle=18,end angle=342,x radius=1.06cm,y radius=.38cm];')
r.edit('entraîner',r'entrai\rlap{t}ner')
r.edit('nom plus','non plus')
r.edit(r'\unsure{profini et|profini}',r'profini et')
r.edit('pas néc. comm.',r'pas \unsure{néc,|néc.} comm.')
def leader(text,width):
 return r'''\begin{tikzpicture}[baseline=-.6ex,x=1cm,y=1cm]
\node[anchor=west,inner sep=0] at (0,.42) {'''+text+r'''};
\draw (.08,-.22) .. controls (.15,.16) and (.55,.18) .. (.82,.2) -- ('''+str(width-.25)+r''',.2) .. controls ('''+str(width)+r''',.23) and ('''+str(width)+r''',.4) .. ('''+str(width-.03)+r''',.51);
\end{tikzpicture}'''
for txt,w in [(r'\inserted{affine}',1.7),(r'\inserted{\handwritten{de car $p>0$}}',3.5),(r'\inserted{\handwritten{unipotent}}',2.9)]:r.edit(txt,leader(txt,w))
r.edit(r'$n\inserted{\handwritten{\geq\unsure{\rlap{\(1\)}2|2|1}}}$',r'$n$'+leader(r'\inserted{$\handwritten{\geq\unsure{\rlap{\(1\)}2|2|1}}$}',1.6))
# Reproduce the stepped outline and five descending cancellation strokes around its actual text.
old=r'''\deleted{point isolé, donc,\deleted{si $G$ est un} \deleted{les arguments \unsure{suffirien|suffirion|suffiront}} comme $G$ est un groupe, que \deleted{groupe, que} $G$ est fini sur $k$. \deleted{Dans dans le cas général, que $G$ est profini sur $k$.} Si $G$ est commutatif (i.e. $\handwritten{\Delta}_{A}$ commutatif), alors le dual de Cartier de $A$ doit être purement infinitésimal, i.e. $G$ doit être unipotent (et réciproquement). On peut conjecturer que \deleted{la con} la condition en question, pour $G$ de type fini pas \unsure{néc,|néc.} comm., équivaut à $G$ fini unipotent.}'''
rows=[(7.8,0,r'point isolé, donc, \deleted{si $G$ est un}'),(0,-.55,r'\deleted{les arguments \unsure{suffirien|suffirion|suffiront}} comme $G$ est un groupe, que'),(0,-1.10,r'\deleted{groupe, que} $G$ est fini sur $k$. \deleted{Dans dans le cas général, que $G$ est profini}'),(0,-1.85,r'\deleted{sur $k$.} Si $G$ est commutatif (i.e. $\handwritten{\Delta}_{A}$ commutatif), alors le dual de Cartier'),(0,-2.60,r'de $A$ doit être purement infinitésimal, i.e. $G$ doit être unipotent (et'),(0,-3.35,r'réciproquement). On peut conjecturer que \deleted{la con} la condition en question,'),(0,-4.10,r'pour $G$ de type fini pas \unsure{néc,|néc.} comm., équivaut à $G$ fini unipotent.')]
fig=r'\figure{\begin{tikzpicture}[x=1cm,y=1cm,every node/.style={anchor=base west,inner sep=0,font=\scriptsize}]'+'\n'
for x,y,t in rows:fig+=r'\node at ('+str(x)+','+str(y)+r') {\deleted{'+t+'}};\n'
fig+=r'''\draw (7.8,.12) -- (14.2,.12) .. controls (14.55,.12) and (14.35,-2.8) .. (14.1,-3.4) -- (12.8,-3.4) .. controls (12.65,-3.6) and (12.65,-3.9) .. (12.65,-4.12) -- (-.06,-4.12) -- (-.02,-.48) -- (7.8,-.42) -- cycle;
\draw (.9,-.50) .. controls (1.5,-1.8) and (1.9,-3.4) .. (2.4,-4.10);
\draw (3.1,-.54) .. controls (3.5,-1.8) and (4.0,-2.8) .. (4.5,-3.55);
\draw (6.6,-.25) .. controls (7.0,-1.6) and (7.7,-2.7) .. (8.1,-3.45);
\draw (9.2,-.22) .. controls (9.6,-1.6) and (10.0,-2.8) .. (10.4,-3.52);
\draw (11.8,-.17) .. controls (12.3,-1.5) and (12.7,-2.7) .. (13.2,-3.13);
\end{tikzpicture}}'''
r.edit(old,fig)
ch('opening first product',r'G\unsure{\times|x}V',r'G\times V',r'G\mathrm{x}V','The central typed glyph has the upper and lower serifs of lowercase x. C doubt resolves to x; the hand right arrow is clear.','openingformula; firstproduct','misread symbol or index','high',True,True)
ch('opening second product',r'V\times V',r'V\times V',r'V\mathrm{x}V','The second product likewise uses the serifed typewriter x, not an unadorned cross.','openingformula; secondproduct','misread symbol or index','high',True,True)
ch('first canceled words','V est un',r'\ill{}','V est un, canceled','The V and each letter of est un remain readable below the series of typed x strikes.','cancelVest','readable ink left as \\ill{}','high',False,True,True)
ch('canceled objects after avec',r'W\quad V',r'\ill{}',r'W\quad V, canceled','A W and a V stand at the ends of the canceled interval. No independent arrow is visible in the intervening spaces under the repeated x strikes.','cancelWV','readable ink left as \\ill{}','high',False,True,True)
ch('product after V isomorphism',r'W\times G',r'W\times G',r'W\mathrm{x}G','The product cell has four distinct typewriter serifs; the preceding hand isomorphism sign has a wave and lower straight stroke.','Visom','misread symbol or index','high',True,True)
ch('canceled noun before section','isomorphisme',r'\ill{}','isomorphisme, canceled','The sequence i-s-o-m-o-r-p-h-i-s-m-e is readable through the x cancellation.','cancelisom','readable ink left as \\ill{}','high',False,True,True)
ch('initial cell before éries','péries','séries',r'\rlap{p}séries','The cell has the descender and foot of p together with the reversed curves and medial stroke of s. Both impressions are retained without inferring which was typed first.','peries; periescell; peries_half','misread word','high',True,True)
ch('punctuation at right edge after générateurs','closing parenthesis without comma','closing parenthesis plus comma','closing parenthesis; no added comma','The closing parenthesis meets the black cropped page edge. No comma is visible after it. Nothing beyond that edge is supplied.','generateursend','text not on the page','medium')
ch('Exemple underline','only Exemple underlined','Exemple 2. emphasized','only Exemple underlined','A single line lies below the word Exemple; it ends before the numeral and its period.','exemple','insertion or placement','high')
ch('affine insertion leader','affine inserted','affine inserted','same text with curved leader','A curved stroke rises from the gap between monoïdes and G to the right of the interlinear word affine. It is reproduced.','affineinsert','drawing or diagram','high',True,True)
ch('canceled extra c',r'coc\deleted{\unsure{c}}omplète','cocomplète',r'coc\deleted{c}omplète','The canceled cell has the open right side and curved upper and lower ends of c beneath an x strike. C doubt is resolved; H omits the cell.','cocomplete; coccell','deletion state','high',True,True)
ch('nulle en e cancellation','nulle en e',r'\ill{}','nulle en e, canceled','The n-u-l-l-e, en and final e remain discernible under the typed x series and hand stroke.','cancnulle','readable ink left as \\ill{}','high',False,True,True)
ch('inserted lower bound',r'\geq\unsure{2|1}',r'\geq1',r'\geq\unsure{\rlap{\(1\)}2|2|1}','The inequality has a right-facing angle and separate lower bar. The numeral combines a curved 2-like left part with a tall straight 1-like stem and upper sloping lead; an overlap is the leading reading but the dense ink does not settle the separate impressions.','ngreater; ngreaterfine; digit_half','misread symbol or index','medium',True,True,False,True)
ch('lower-bound insertion leader','insertion only','insertion only','same qualified bound with curved leader','A curved stroke descends to the gap immediately after n and ends up to the right of the inserted bound.','ngreater; digit_half','drawing or diagram','high',True,True)
ch('canceled cell after n',r'\deleted{\unsure{s|x}}','omitted',r'\deleted{\unsure{s|x}}','A crossed extra cell remains after n. Its right horizontal curve suggests s but cannot be isolated securely from the x cancellation; both C alternatives remain.','nextra','omission','medium',False,True)
ch('dots in f product',r'g_2\ldots g_n',r'g_2\dots g_n',r'g_2\cdots g_n','The three typed points sit at the center level of the g bodies, clearly above their lowered indices.','fproduct','misread symbol or index','high',True,True)
ch('overtyped cells in variables',r'\unsure{varaables|variables}','variables',r'var\rlap{a}i\rlap{a}ibles','Two successive cells each retain a round a bowl and a dotted i impression; the second i is visibly offset to the right. The raw overlapping impressions replace the choice between normalized complete words.','varaables; varcells; var_half','misread word','high',True,True)
ch('oval marginal wording',r'\unsure{car|car.} k>0 !','(car car. k>0 !','car k>0 !','After rotation only one c-a-r group is visible, followed by k, a right-facing angle, zero and exclamation mark. No point follows r. The apparent opening parenthesis is part of the surrounding oval.','ovalnote','misread word','high',True,True)
ch('oval outline','closed ellipse','described marginal text with opening parenthesis','oval open at right','The curved outline runs above and below the note and around its left end; its two ends remain separated at the right. The opening is reproduced.','ovalnote','drawing or diagram','high',True,True)
ch('de car p>0 punctuation','de car p>0','de car. p>0','de car p>0','The r ends in an upturned hook, with blank space before p and no abbreviation point. The p descends and the strict greater-than angle is clear.','kins','other','high')
ch('de car p>0 leader','insertion only','insertion only','insertion after k with curved leader','The long lower stroke begins at the gap after k before its comma, extends beneath the inserted note, and curls up at its right end.','kins','drawing or diagram','high',True,True)
ch('fully struck line after je pense que',"dès qu'on y remplace une des variables par 1, mais alors, faisant tous",'omitted',"same complete canceled line",'Repeated x strokes cross the whole line; the accents, apostrophe, numeral 1, both commas and the words through tous remain readable in four overlapping close crops.','cancelline1; cancel1a; cancel1b; cancel1c; cancel1d','omission','high',False,True,False,True)
ch('word after cela doit','entraîner','entraîner',r'entrai\rlap{t}ner','The i has a simple dot, with no circumflex. The next cell has an n arch overlapped by the tall stem and crossbar of t; both type impressions are preserved.','celalive; entrainer; entrain_half','misread word','high',True,True)
ch('live beginning before outlined cancellation','cela doit entraîner que G est live, l-unité de canceled','entire sentence canceled','cela doit entrai(t/n overlap)ner que G est live; l-unité de separately canceled','The long hand outline begins at point isolé. It does not cross cela doit, the following words, G or est. A distinct horizontal stroke cancels only l-unité de in this part.','celalive; unitdelete; Glive; bigcancel','deletion state','high',False,True,False,True)
ch('canceled si G est un','si G est un canceled','omitted','si G est un canceled inside outlined passage','The typed s-i, G, est and un remain readable below the x strikes at the end of the first outlined line.','siGdelete','omission','high')
ch('canceled les arguments and suffix',r'les arguments \unsure{suffirien|suffirion|suffiront}','omitted',r'les arguments \unsure{suffirien|suffirion|suffiront}, canceled','The words les arguments and suffi-like beginning are visible, but typed x strikes and a blue horizontal stroke merge with the final letter sequence. The final n-like arch and preceding rounded remnant do not securely settle the suffix; C alternatives are retained.','arguments; argleft; argright; suffix; suffix_half','omission','low',False,True)
ch('second canceled groupe que','groupe, que canceled','omitted','groupe, que canceled','The lower g loop, r, o, u, p descender, e, comma and que are visible under the typed x series.','groupedelete','omission','high')
ch('Dans dans sentence','Dans dans le cas général, que G est profini sur k. canceled',r'\ill{}','same complete canceled sentence','Both Dans and dans are present. The two acute accents in général, comma, G and final profini sur k are visible despite the overstrikes.','Dansline; Dans1; Dans2; Dans3; Danstail','readable ink left as \\ill{}','high',False,True,True,True)
ch('extent and geometry of large cancellation','whole passage point isolé through G fini unipotent canceled; no outline geometry','only earlier sentence and pas néc. comm. canceled; later Cartier passage live','whole passage canceled, stepped outline and five long strokes reproduced','The left boundary drops beside the canceled arguments line. The right boundary descends past Cartier to question and steps inward above unipotent. Its lower stroke runs through the entire last conjecture line. Five oblique lines cross the enclosed text; the later Cartier and conjecture clauses lie inside, not outside, this canceled region.','bigcancel; Gfinik; Gcomm; DeltaA; Cartier; Acartier; Guni; néccomm; unitail','deletion state','high',True,True,False,True)
ch('canceled la con','la con canceled',r'\ill{}','la con canceled inside large cancellation','The l, a, c, o and n are still readable under the typed x strikes immediately before the repeated live-in-the-undertext la.','lacon','readable ink left as \\ill{}','high',False,True,True)
ch('punctuation after néc','néc.','néc.',r'\unsure{néc,|néc.}','The dark punctuation has a descending two-lobed tail below the blue border. It looks comma-like, but the crossing stroke obscures its top and a damaged full stop remains possible.','necfine; necpunct; necpunct_half','other','medium',True,True)
ch('hand unipotent insertion and position','inserted at end of canceled passage','marginal unipotent appended at page end','inserted after canceled passage and before donc, with leader','The hand u-n-i-p-o-t-e-n-t sits just above donc, outside the stepped cancellation. A separate curved line below it descends immediately before donc.','unitail; bigcancel','insertion or placement','high',True,True,False,True)
ch('left question mark','?','omitted','?','A long curved hook and separate lower dot stand to the left of the final outlined line.','question','omission','high')
ch('non plus','nom plus','non plus','non plus','The final letter has one arch and two stems, matching the first n. The supplied half enlargement confirms n rather than the two arches of m.','nomplus; nonplusfull; nonhalf','misread word','high',True,False)
ch('last canceled words',r'\unsure{profini et|profini}','profini et','profini et, canceled','The final two cells retain the open e and the tall t with crossbar and curved foot. Both words lie beneath the heavy hand cancellation, so C doubt resolves to profini et.','profinicancel','other','high',True,False)
r.doubt('inserted lower bound',r'\geq\rlap{\(1\)}2','2; 1','medium','Dense overlapping numeral; no correction order asserted.')
r.doubt('extra canceled cell after n','s','x','medium','x strike obscures its underlying curves.')
r.doubt('canceled les arguments suffix','suffirien','suffirion; suffiront','low','Typed x series and hand strike merge with the ending.')
r.doubt('abbreviation punctuation in large cancellation','néc,','néc.','medium','Descending dark mark crosses blue border.')
r.notation('typed product sign','serifed lowercase x, retained as mathrm{x}','10:136 opening twice and V isomorphism')
r.notation('typed tensor sign','O with overlaid diagonal cross; otimes','10:136 A tensor_k Mbar')
r.notation('typed raw overlap','p/s; a/i in two adjacent cells; t/n','10:136 péries cell; variables cells; entrainer cell')
r.notation('large cancellation','stepped outline and five descending oblique strokes','10:136 point isolé through G fini unipotent')
r.r['abbreviations']=[dict(abbreviation='nb',expansion='nombre',scan='10:136'),dict(abbreviation='car',expansion='caractéristique',scan='10:136'),dict(abbreviation='néc.',expansion='nécessairement',scan='10:136'),dict(abbreviation='comm.',expansion='commutatif',scan='10:136')]
r.r['crops']=sum((json.loads(Path(p).read_text()) for p in ['work/crops136.json','work/crops136_extra.json','work/crops136_halves.json']),[])
for i,(pos,first,kind,hand) in enumerate([('upper paragraph','raw p/s cell','text','typewriter'),('after monoïdes','affine curved leader','drawing','his hand'),('after n','bound curved leader','drawing','his hand'),('lower paragraph','two a/i overlaps','text','typewriter'),('after k','de car p>0 leader','drawing','his hand'),('cela doit','t/n overlap','text','typewriter'),('lower paragraph','stepped cancellation outline and five diagonals','drawing','his hand'),('right above donc','unipotent curved leader','drawing','his hand')],1):
 r.r['inventory_extra'].append(dict(scan='10:136',sheet_kind='typescript',hand=hand,element=f'136-R{i:03d}',kind=kind,position=pos,first_words_or_objects=first,transcribed='yes'))
r.r['inspection_note']='Root inspected whole then both supplied halves before witnesses and all C doubts/inventory. All 98 enlargement recipes were viewed; the earlier Adonc/affineinsert truncated result was re-viewed. Gbottom2 initially captured e, so bottomphrase supplies the actual second G. Both supplied halves were read again line by line; seven close crops from those halves confirm difficult type cells. No OCR or parallel reading. No mathematical check event. Archive 135 retained only as comment. All eight C doubt locations decided and logged.'
r.save('work/record136.json')
