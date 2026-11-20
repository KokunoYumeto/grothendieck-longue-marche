from pathlib import Path
import sys,json
sys.path.insert(0,str(Path('SP02_CW_10+12/scripts').resolve()))
from root_record import Record
r=Record('B10-09',10,124);ch=r.change
# Archive folio 123 remains a comment under the base PROMPT convention.
def guide(body):
 return r'\handwritten{\begin{tikzpicture}[x=.4cm,y=.4cm,baseline=-.2ex]'+body+r'\end{tikzpicture}}'
gtop=guide(r'\draw (0,-.55) .. controls (-.12,.02) and (.12,.28) .. (.42,.30)--(6.8,.30) .. controls (7.04,.30) and (7.18,.36) .. (7.18,.54);')
ggrade=guide(r'\draw (0,-.30) .. controls (-.18,.06) and (0,.28) .. (.28,.29)--(3.25,.29) .. controls (3.40,.29) and (3.58,.55) .. (3.68,.48) .. controls (3.80,.28) and (4.15,.30) .. (4.60,.20)--(4.72,-.30);')
gR=guide(r'\draw (0,-.48) .. controls (-.12,.0) and (.15,.12) .. (.42,.14)--(1.38,.14) .. controls (1.56,.16) and (1.64,.24) .. (1.65,.43);')
glong=guide(r'\draw (0,-.42) .. controls (-.12,.05) and (.12,.18) .. (.40,.20)--(4.80,.12) .. controls (5.04,.14) and (5.15,.22) .. (5.16,.42);')
gsuff=guide(r'\draw (0,-.34) .. controls (-.03,.10) and (.22,.21) .. (.50,.22)--(1.64,.20) .. controls (1.94,.23) and (2.12,.41) .. (2.11,.60) .. controls (2.10,.35) and (2.35,.18) .. (2.68,.16)--(3.28,.18);')
gCela=guide(r'\draw (0,-.40) .. controls (-.08,.05) and (.17,.16) .. (.46,.13)--(2.72,.06) .. controls (2.98,.07) and (3.10,.17) .. (3.11,.42);')
gpairs=guide(r'\draw (0,-.20)--(2.20,-.26) .. controls (2.42,-.26) and (2.58,-.12) .. (2.57,.04);')
gent=guide(r'\draw (0,-.30) .. controls (.15,.08) and (.35,.14) .. (.53,.14)--(1.92,.12) .. controls (2.12,.13) and (2.23,.25) .. (2.20,.42);')
gou=guide(r'\draw (0,.15) .. controls (.35,.21) and (.56,.13) .. (.64,-.18) .. controls (.70,-.36) and (.91,-.40) .. (1.14,-.40);')
gedge=guide(r'\draw (.18,.42) .. controls (-.05,.46) and (-.08,.25) .. (.01,.02) .. controls (.13,-.30) and (.44,-.34) .. (.68,-.27);')
gsemi=guide(r'\draw (0,-.40) .. controls (-.05,.06) and (.16,.17) .. (.45,.18)--(2.63,.15) .. controls (2.88,.16) and (3.03,.29) .. (3.02,.49);')
gcoh=guide(r'\draw (0,-.34) .. controls (-.05,.05) and (.16,.14) .. (.42,.14)--(2.90,.14) .. controls (3.08,.13) and (3.15,-.12) .. (3.26,-.21) .. controls (3.38,.03) and (3.40,.25) .. (3.36,.40);')
r.edit(r'aux $\otimes$',r'aux $\unsure{\otimes|\Omega}$')
r.edit(r'\unsure{f. et s.|f. et p.}',r'f. et \unsure{p.|s.}')
r.edit(r'\unsure{Géométriquement|biométriquement}','Géométriquement')
r.edit("''}} Lorsqu'il", "''}"+gtop+r"} Lorsqu'il")
r.edit(r'\uuline{dans le cas gradué anticomm.}}}',r'\uuline{dans le cas gradué anticomm.}}'+ggrade+'}')
r.edit(' la situation',r' \rlap{k}la situation')
r.edit(r'\deleted{\unsure{son}}',r'\deleted{son}')
r.edit(r'\inserted{$R_k(G)$}',r'\inserted{$R_k(G)$'+gR+'}')
overnote=r'\unsure{cela \rlap{est}vérifié|\deleted{cela est} vérifié|cela est vrai}'
r.edit(r'cela est \unsure{vérifié|vrai}',overnote)
r.edit(r'\unsure{(car $k\ne2$, i.e.)|(car $k\ne2$, c.à.d.)}',r'(car $k\ne2$, \unsure{c.c.|i.e.|c.à.d.})')
r.edit(r'\unsure{que cela implique}','que cela implique')
r.edit(r'donc $A^*$ commutatif !}}',r'donc $A^*$ commutatif !}'+glong+'}')
r.edit(r'\inserted{\handwritten{il suffit}}',r'\inserted{\handwritten{il suffit}'+gsuff+'}')
punc=r'\unsure{\handwritten{,}|\handwritten{.}\deleted{,}}\deleted{i.e.}'
r.edit(r'\handwritten{.}\deleted{,i.e.}',punc)
r.edit(r'\inserted{Cela signifie}',r'\inserted{Cela signifie'+gCela+'}')
r.edit("la décomposition d'un",r"la décomp\rlap{i}o\unsure{\rlap{o}s|\rlap{e}s}\rlap{t}ition d'un")
r.edit(r'\inserted{pairs et impairs}',r'\inserted{pairs et impair\handwritten{\unsure{s}}'+gpairs+'}')
r.edit('$C$,resp.',r'$C$,\rlap{e}resp.')
r.edit(r'\inserted{\handwritten{entiers}}',r'\inserted{\handwritten{entiers}'+gent+'}')
r.edit(r'\deleted{\unsure{x|s}}',r'\deleted{\unsure{f|s|x}}')
circ=r'\inserted{\handwritten{\begin{tikzpicture}[x=.4cm,y=.4cm,baseline=-.2ex]\node at (0,0) {si car. $k\ne2$};\draw (0,0) ellipse (2.5 and .46);\end{tikzpicture}}}'
r.edit(r'\inserted{\handwritten{si car. $k\ne2$}}',circ)
r.edit(r'\inserted{\handwritten{où}}',r'\inserted{\handwritten{où}'+gou+'}')
overest=r'\unsure{\rlap{\handwritten{es}}soit|soit|est}'
r.edit(r'\unsure{est}',overest)
r.edit(r'\margin{\deleted{\handwritten{et on \unsure{voit}}}}',r'\margin{'+gedge+'}\n'+r'\margin{\deleted{\handwritten{et on \unsure{voit}}}}')
r.edit(r'\handwritten{10)}',r'\handwritten{1\unsure{\rlap{-}0|0})}')
r.edit(r'\inserted{semi-simples}',r'\inserted{s\rlap{m}emi-simples'+gsemi+'}')
r.edit(r'\inserted{cohomologiques}',r'\inserted{cohomologiques'+gcoh+'}')
r.edit('On respire',r'On \rlap{e}respire')
r.edit('pas nécessairement',r'pas nécess\rlap{i}airement')
ch('typed tensor signs','otimes at four places','otimes at four places',r'first \unsure{\otimes|\Omega}; three later occurrences otimes','The first operator and both Koszul operators and the structure operator share an arch, crossed interior and low feet. The first occurrence carries the recurring visual alternative.','tensor1; Koszul; tensor2','misread symbol or index','medium',True,True,False,True)
ch('initial category C','plain C','underlined C','plain C','The open typed C has no detached horizontal line below it.','C1','misread symbol or index','high',False,True,False,True)
ch('top insertion abbreviation',r'\unsure{f. et s.|f. et p.}',r'\uncertain{f. d. p.}',r'f. et \unsure{p.|s.}','The f is looped and tall, then e and t are joined. The last abbreviation has a narrow upper loop and descending stem favoring p, while a cursive s remains possible; the doubt is localized.','topstart; fets','misread word','low',True,True,True)
ch('quoted top insertion word',r'\unsure{Géométriquement|biométriquement}','géométriquement','Géométriquement','The initial open capital has a lower inward return and no b ascender; the following éo and the long métriquement sequence are readable.','topend; topnote-upright','misread word','medium',True,True)
ch('top quotation shapes','paired double quotes','guillemets','paired double quotes','Two separate upper strokes at each side enclose the handwritten word; no angular guillemets are drawn.','topend','other')
ch('top insertion position','after canceled Alors','margin after action de G','after canceled Alors','The guide descends between the canceled Alors and the L of Lorsqu\'il, far above the action-de-G line.','topnote; topguide','insertion or placement','high',False,True,False,True)
ch('top insertion guide','omitted','omitted','local curved guide drawn','A left descending bend leads into a long nearly horizontal line beneath the addition and an upward curl at its right.','topguide','drawing or diagram','high',True,True)
ch('graded insertion abbreviation','anticomm.','anticommutatif','anticomm.','The word ends in two m bodies and a point, without the expanded utatif.','gradednote','abbreviation expanded or spelling modernised')
ch('graded insertion emphasis','double underline','no underline','double underline','Two distinct horizontal strokes lie beneath the added phrase.','gradednote','other')
ch('graded insertion position','after ainsi','margin after action de G','after ainsi','The pointer loops upward at the gap before la on the Lorsqu\'il line.','gradednote; la','insertion or placement')
ch('graded insertion frame','omitted','omitted','frame and pointer drawn locally','The left turn, upper line, small upward loop at the insertion point and right descending end surround the note.','gradednote','drawing or diagram','high',True,True)
ch('la situation first cell','la','la',r'\rlap{k}la','The tall l stem shares a cell with two diagonal k arms. The blue loop nearby belongs to the insertion frame and is not a typed letter.','la; topguide','misread word','medium',True,True)
ch('canceled son',r'\unsure{son}','son','son, canceled','All three letter cells survive under the x strokes, including the final n arch. C doubt resolved.','son','other','high',True,False)
ch('canceled category C','plain C','underlined C','plain C, canceled','An open C body is visible under the cancellation but no separate underline is present.','Rinsert','misread symbol or index','high',False,True,False,True)
ch('replacement representation name','R_k(G)','Rep_k(G)','R_k(G)','Only one large R precedes the low k and parenthesized G; there are no e or p cells.','Rinsert','misread symbol or index','high',False,True,False,True)
ch('replacement guide','omitted','omitted','curved guide drawn','The hand line starts beside the canceled C, bends upward beneath R_k(G), and rises at the right.','Rinsert','drawing or diagram','high',True,True)
ch('deux représentation ending','représentation','représentations','représentation','The final typed n is followed by a blank before M, with no s.','representation','abbreviation expanded or spelling modernised')
ch('long hand addition overwritten phrase',r'cela est \unsure{vérifié|vrai}',r'\struck{cela est} \ill{}',overnote,'Cela is partly separable at the left; est-like and vérifié-like strokes occupy the same following zone. Heavy lower and transverse passes do not securely establish the entire cancellation boundary asserted by H. The overlap and deletion alternatives remain explicit.','note1; overlap-note','deletion state','low',True,True,True,True)
ch('long hand parenthesis',r'\unsure{(car k ne 2, i.e.)|(car k ne 2, c.à.d.)}',r'\ill{}',r'(car $k\ne2$, \unsure{c.c.|i.e.|c.à.d.})','The opening parenthesis, car, k, two horizontal strokes crossed diagonally, 2 and comma are clear. The abbreviation comprises two small right-open curves and separated dots, visually c.c.; the alternative readings remain.','uppernote; upper-abbr','readable ink left as \\ill{}','low',True,True,True,True)
ch('long hand implication words',r'\unsure{que cela implique}',r'\ill{} implique','que cela implique','The q descender, u/e, c/e/l/a sequence and implique are traceable in the rotated view. C whole-phrase doubt resolved.','note2; longnote-upright','readable ink left as \\ill{}','medium',True,True,True,True)
ch('first A exponent',r'\unsure{*|\#}',r"A'",r'A^{\unsure{*|\#}}','A small cluster has intersecting upright and oblique branches, not a single prime. It remains uncertain whether the additional short bar makes a hash.','note2; Aexponents','misread symbol or index','low',False,True,False,True)
ch('second A exponent',r'\unsure{\oplus|0}',r'A^{\circ}',r'A^{\unsure{\oplus|0}}','An oval has interior crossing strokes; a circled cross is favored, with 0 retained because the surrounding pen strokes overlap its edge. C doubt retained.','note2; Aexponents','misread symbol or index','low',False,True,False,True)
ch('end of long hand addition','donc A-star commutatif !',r'\ill{}','donc A-star commutatif !','Donc, the ordinary capital A with a branched superscript, commutatif and the exclamation mark are readable on the lower line. The star uses the first candidate of the earlier qualified occurrence.','notelower; longnote-upright','readable ink left as \\ill{}','medium',False,True,True,True)
ch('long addition position','after first central','margin after second central','after first central','The guide rises from the space after the first central semicolon and passes below the hand addition before à fortiori.','longnote; longguide','insertion or placement','high',False,True,False,True)
ch('long addition guide','omitted','omitted','curved guide drawn','The long lower line has a left rising bend and a right upward curl beneath commutatif.','longguide','drawing or diagram','high',True,True)
ch('after à fortiori','il suffit inserted','omitted','il suffit inserted','The two-word hand phrase lies below the line, with two tall f stems and a final t.','notesuffit; suffit-guide','omission','high',False,True,False,True)
ch('il suffit guide','omitted','omitted','curved insertion guide drawn','The line curls up in the gap after fortiori and continues to the right over the hand phrase.','suffit-guide','drawing or diagram','high',True,True)
ch('second central punctuation',r'hand period then deleted ,i.e.',r'period then deleted i.e.',punc,'The large mark immediately after central has a low hooked tail, suggesting a comma; an added point over a deleted comma cannot be separated securely. The i.e. cells are visibly crossed.','centralpunct','deletion state','low',True,True)
ch('Cela signifie guide','omitted','omitted','curved guide drawn','A hand curve rises from the canceled abbreviation region, runs beneath the added typed words, and curls up at their right.','Cela; Cela-guide','drawing or diagram','high',True,True)
ch('first décomposition overlapping cells','décomposition','décomposition',r'décomp\rlap{i}o\unsure{\rlap{o}s|\rlap{e}s}\rlap{t}ition','After p the first cell has an o oval with a high i dot/stem; the second has the s bends and an enclosing o/e-like body; the third has an i and a t crossbar. The middle underlying letter stays qualified.','decomposition; decomp-over','misread word','medium',True,True)
ch('impairs final letter','typed impairs','impairs',r'impair\handwritten{\unsure{s}}','After the typed r is a blue s-shaped curved mark whose lower tail meets the guide; no typewriter s is present. The possibility of guide-only ink keeps the hand letter qualified.','pairs; impairs-end','other','medium',True,True)
ch('pairs et impairs guide','omitted','omitted','curved guide drawn','A hand line passes below the added phrase and turns upward at its right near the s-shaped mark.','pairs; impairs-end','drawing or diagram','high',True,True)
ch('C after se fasse dans','plain C','underlined C','plain C','The C has no separate lower line.','C2resp','misread symbol or index','high',False,True,False,True)
ch('resp. first cell','resp.','resp.',r'\rlap{e}resp.','The first cell combines the r upright/shoulder and the curved e with its middle bar; a separate ordinary e follows.','C2resp; resp-over','misread word','high',True,True)
ch('degrés insertion','entiers','quelconques','entiers','The hand sequence e-n-t-i-e-r-s is readable, with a tall t, dotted i and final s; there is no long quelconques sequence.','entiers','misread word','high',False,True,False,True)
ch('entiers guide','omitted','omitted','curved guide drawn','A line rises after degrés, runs beneath the added word and curls at the right.','entiers','drawing or diagram','high',True,True)
ch('C after termes de','plain C','underlined C','plain C','The typed open C has an ordinary lower terminal, not an underline.','C3','misread symbol or index','high',False,True,False,True)
ch('canceled extra cell after gradué',r'\unsure{x|s}','omitted',r'\deleted{\unsure{f|s|x}}','The cell is physically present under an x-shaped strike. A tall curled stem and low return favor f, but s or an unseparated x cannot be ruled out. No grammatical ending is supplied.','gradx; grad-end','omission','low',True,True)
ch('C in C to Grdf','plain C','underlined C','plain C','The typed C is not underlined; the independent hand arrow points right toward Grdf(k).','Cgrdf','misread symbol or index','high',False,True,False,True)
ch('nested espère correction','deleted espère plus inserted voit','espère within outer deletion','deleted espère plus inserted hand voit, all within outer deletion','Espère has its own cancellation, and voit is legible immediately above it under the later long cancellation.','voit; cancel1; cancelall','deletion state','high',False,True,False,True)
ch('characteristic insertion contents','si car. k ne 2','si car. ne 2','si car. k ne 2','The small k body lies between the abbreviation point and the unequal sign.','carcircle','misread symbol or index','high',False,True,False,True)
ch('characteristic insertion position','after second suffisante','margin following paragraph','after second suffisante within canceled claim','The hand oval is immediately below the parenthetic nécessaire et suffisante and before pour, within the crossed block.','carcircle; cancel2','insertion or placement')
ch('characteristic insertion oval','omitted','omitted','oval drawn around note','A continuous hand oval encloses all four groups of the note.','carcircle','drawing or diagram','high',True,True)
ch('où insertion','où','omitted','où','The hand o/u sequence has a grave accent above u and lies after favorable, before the category formula.','ou','omission','high',False,True,False,True)
ch('où guide','omitted','omitted','curved guide drawn','A curved stroke beside où drops toward the space before the category formula.','ou; CR','drawing or diagram','high',True,True)
ch('C in canceled equivalence formula','plain C','underlined C','plain C','The line across the C continues through the whole clause as cancellation, not as an isolated underline.','CR; cancel3','misread symbol or index','high',False,True,False,True)
ch('canceled equivalence verb',r'\unsure{est}','soit',overest,'Four typed cells support soit, while e/s-like handwriting crosses the first three. The heavy horizontal cancellation obscures exact allocation; the overlap and both plain readings remain qualified.','est; cancel3','misread word','low',True,True,False,True)
ch('right margin flourish','omitted','omitted','curved stroke drawn','A separate L-like curved hand stroke lies at the right edge of the canceled block, with no recoverable letter label.','edgeflourish','drawing or diagram','high',True,True)
ch('left margin canceled words',r'et on \unsure{voit}','omitted',r'\margin{\deleted{\handwritten{et on \unsure{voit}}}} retained','Et on is visible through the strike; the last word has a v-like cup and final upright, but its inner joins and i dot are not secure. C doubt retained.','marginleft','omission','low',False,True)
ch('paragraph number 10','10)','10)',r'hand 1\unsure{\rlap{-}0|0})','The 1 and final parenthesis are clear; the oval 0 has a horizontal interior pass and the 1 has retraced loops. The bar may be an older stroke; no earlier numeral is invented.','ten; ten-under','other','medium',True,True)
ch('semi-simples first e','semi-simples','semi-simples',r's\rlap{m}emi-simples','The first e cell contains an m with two arches and feet beneath the e curve/bar; the next m remains a separate cell.','semisimple; semi-over','misread word','high',True,True)
ch('semi-simples guide','omitted','omitted','curved guide drawn','A hand line descends after motifs, passes beneath the typed addition, and curls upward at the right.','semisimple','drawing or diagram','high',True,True)
ch('canceled foncteurs','foncteurs',r'\ill{}','foncteurs, canceled','The f ascender, following o-n-c-t-e-u-r-s sequence and cancellation crosses are separable.','foncteurs','readable ink left as \\ill{}','high',False,True,True)
ch('dash after motifs comma','short hyphen','em dash','short hyphen','A single short typewriter horizontal stroke follows the comma; it is not a long dash.','dash','other','high',False,True)
ch('cohomologiques placement','after correspondances','after Künneth','after correspondances, before de Kunneth','The insertion guide originates at the end of correspondances and before de on the following line.','coh','insertion or placement','high',False,True,False,True)
ch('cohomologiques guide','omitted','omitted','guide with insertion cusp drawn','A lower line runs under the added word and turns toward the insertion point before de.','coh','drawing or diagram','high',True,True)
ch('Kunneth spelling','Kunneth','Künneth','Kunneth','No two dots or accent lie above the u cell.','Kunneth','abbreviation expanded or spelling modernised')
ch('respire first cell','respire','respire',r'\rlap{e}respire','The initial cell has r upright/shoulder plus an enclosing e curve and crossbar; the separate following e is ordinary.','respire','misread word','high',True,True)
ch('nécessairement a cell','nécessairement','nécessairement',r'nécess\rlap{i}airement','The a contains a distinct i upright with a dot above it. A second, ordinary i occupies the next cell.','necessairement; necess-over','misread word','high',True,True)
# Remaining doubts and notation are independent of mathematical plausibility.
r.doubt('first typed tensor sign',r'\otimes',r'\Omega','medium','Four matching typed arch-and-cross forms; first marked, later three use first candidate.')
r.doubt('top insertion abbreviation','f. et p.','f. et s.','low','Final loop and descending stem favor p; the joined hand can also form s.')
r.doubt('long hand addition overwritten phrase',r'cela \rlap{est}vérifié',r'\deleted{cela est} vérifié; cela est vrai','low','Physical overlap and possible deletion boundary remain unresolved.')
r.doubt('parenthetical abbreviation','c.c.','i.e.; c.à.d.','low','Two open curves with points; neither semantic expansion is substituted.')
r.doubt('first A superscript','*',r'\#','low','Branched cluster has a possibly extra short bar; later matching form uses star.')
r.doubt('second A superscript',r'\oplus','0','low','Oval and crossing traces are crowded.')
r.doubt('after second central','hand comma','hand point with deleted typed comma','low','The visible mark has a low hook; ink layers cannot be isolated.')
r.doubt('first décomposition, second overlapped cell',r'\rlap{o}s',r'\rlap{e}s','medium','S bends and an enclosing round body overlap; underlying middle bar is uncertain.')
r.doubt('impairs ending','hand s','guide-only curved trace','medium','The s-shaped end meets the hand guide; no typed s body is visible.')
r.doubt('extra canceled cell after gradué','f','s; x','low','Tall curled stem favors f but the x strike covers its body.')
r.doubt('canceled equivalence verb',r'\rlap{\handwritten{es}}soit','soit; est','low','Typed four-cell body with hand loops and a heavy cancellation.')
r.doubt('left margin canceled final word','voit','','low','Cup and upright remain, but inner joins and dot are obscured.')
r.doubt('paragraph 10 second numeral',r'\rlap{-}0','0','medium','Oval with an interior horizontal pass; no previous numeral identified.')
r.notation('typed tensor glyph',r'\unsure{\otimes|\Omega} first, later \otimes','10:124 first line; Koszul pair; structure clause','uncertain')
r.notation('mu with looped long stem',r'\mu_2','10:124 centrality clause; left parallel passes form the long looped stem, not positive evidence of a doubled alphabet')
r.notation('graded multiplicative monoid',r'\underline{G}_m','10:124 two occurrences; underline on G, m subscript, hand arrows')
r.notation('hand A superscript branched sign',r'\unsure{*|\#} first; later *','10:124 long hand insertion, two occurrences','uncertain')
r.notation('hand A circled superscript',r'\unsure{\oplus|0}','10:124 long hand insertion','uncertain')
r.notation('archive pencil folio','comment only','10:124 lower-left pencil 123; base PROMPT rule 4')
r.r['abbreviations']=[{'abbreviation':'f. et p. / s.','expansion':'final abbreviated letter unresolved; f. et s. may stand for faut et suffit','attestations':'10:124 top insertion'},{'abbreviation':'anticomm.','expansion':'anticommutatif / anticommutative','attestations':'10:124 graded insertion'},{'abbreviation':'car / car.','expansion':'caractéristique','attestations':'10:124 body and hand notes'},{'abbreviation':'c.c. / i.e. / c.à.d.','expansion':'unresolved abbreviation; no expansion assigned to c.c.','attestations':'10:124 long hand parenthesis'},{'abbreviation':'resp.','expansion':'respectivement','attestations':'10:124 decomposition clause'},{'abbreviation':'i.e.','expansion':'id est','attestations':'10:124 body and canceled abbreviation'}]
r.r['crops']=json.loads(Path('work/crops124.json').read_text())
r.r['inventory_overrides']={
 '124-E003':{'hand':'his hand','first_words_or_objects':r'il f. et \unsure{p.|s.} que A soit commutatif! "Géométriquement"'},
 '124-E004':{'hand':'his hand','first_words_or_objects':r'il f. et \unsure{p.|s.} que A soit commutatif! "Géométriquement"'},
 '124-E007':{'first_words_or_objects':'son'},
 '124-E015':{'hand':'his hand','first_words_or_objects':'et on voit que; overlapped cela est/vérifié; si (car k ne 2, c.c./i.e./c.à.d.); que cela implique A-star/hash=A-circled-cross/0 donc A-star commutatif !'},
 '124-E016':{'hand':'his hand','first_words_or_objects':'et on voit que; full two-level hand addition, with localized doubts'},
 '124-E020':{'hand':'his hand','first_words_or_objects':'comma / point over canceled comma, unresolved'},
 '124-E021':{'first_words_or_objects':'i.e.; preceding comma cancellation uncertain'},
 '124-E024':{'first_words_or_objects':'pairs et impair, hand final s uncertain'},
 '124-E028':{'first_words_or_objects':r'\unsure{f|s|x}'},
 '124-E043':{'hand':'his hand','first_words_or_objects':'10), interior pass through 0 retained with doubt'},
 '124-E044':{'first_words_or_objects':r's\rlap{m}emi-simples'}
}
# Author's hand is identified from its continuous correction layer, not the inherited unknown label.
for n in [5,6,10,11,13,14,17,18,19,25,26,29,30,32,33,34,35,36,37,38,39,40,41]:
 r.r['inventory_overrides'].setdefault(f'124-E{n:03d}',{})['hand']='his hand'
r.r['inventory_overrides']['124-E042']={'hand':'typewriter','first_words_or_objects':'Ce résultat s\'appliquera alors; paragraph 10 through pas nécessairement'}
extras=[
 ('guide-top','drawing','above line 3','long curved guide attached after canceled Alors','his hand'),
 ('guide-grade','drawing','above line 4','frame and upward insertion loop around graded note','his hand'),
 ('over-la','text','line 3','k/l overlap in la','typewriter'),
 ('guide-R','drawing','above line 5','guide from canceled C to R_k(G)','his hand'),
 ('guide-long','drawing','above line 11','curved guide for long two-level hand addition','his hand'),
 ('guide-suffit','drawing','below line 11','guide around il suffit','his hand'),
 ('guide-Cela','drawing','above line 12','guide below Cela signifie','his hand'),
 ('over-decomp','text','line 12','o/i; s with o/e; i/t overlaps in décomposition','typewriter'),
 ('hand-s','insertion','above line 12 right','uncertain hand s at end of impair','his hand'),
 ('guide-pairs','drawing','above line 12 right','guide below pairs et impairs','his hand'),
 ('over-resp','text','line 13','r/e overlap in resp.','typewriter'),
 ('guide-entiers','drawing','line 14','guide beneath entiers','his hand'),
 ('oval-car','drawing','within canceled final assertion','oval enclosing si car. k ne 2','his hand'),
 ('guide-ou','drawing','above final canceled line','curved guide beside où','his hand'),
 ('over-soit','text','last canceled line','typed soit with uncertain hand es overlay','his hand'),
 ('edge-flourish','drawing','right margin beside canceled block','separate L-like curved stroke','his hand'),
 ('over-semi','text','semi-simples insertion','m/e overlap','typewriter'),
 ('guide-semi','drawing','below motifs','curved guide beneath semi-simples','his hand'),
 ('guide-coh','drawing','above de Kunneth','guide and cusp locating cohomologiques after correspondances','his hand'),
 ('over-respire','text','On respire','r/e overlap in initial cell','typewriter'),
 ('over-necess','text','last line','a/i overlap in nécessairement','typewriter'),
 ('archive-folio','text','lower-left corner','123; archival folio retained as comment only','unnamed hand')]
for suffix,kind,pos,words,hand in extras:
 r.r['inventory_extra'].append(dict(scan='10:124',sheet_kind='typescript',hand=hand,element='124-'+suffix,kind=kind,position=pos,first_words_or_objects=words,transcribed='yes'))
r.r['inspection_note']='Root alone inspected whole then both supplied halves before reading witnesses; all agreed words/signs and all differences checked in ink. All 82 recorded crops actually viewed, including individual repeats of truncated batches. Slanted top/long notes rotated upright. All eleven C doubt loci decided or explicitly retained; glyphs, indices, hand arrows, deletions and insertion guides checked. Dense overlapping corrections retain localized uncertainty. Reinspection identifies the long parallel mu strokes as its looped stem, without a separate alphabet claim. The crowded ce remains two readable letters; ordinary capitals and H-bullet forms have no positive repeated-strike evidence. Archive pencil 123 retained as a comment under PROMPT rule 4. No context, second-pass audit, or mathematical check has been undertaken.'
leftmargin=r'\margin{\deleted{\handwritten{et on \unsure{voit}}}}'
r.edit(leftmargin,'')
# The guide has already been inserted into this phrase by the earlier edit.
r.edit(r'\inserted{Cela signifie\handwritten{',leftmargin+r'\inserted{Cela signifie\handwritten{')
ch('left margin note placement','after final canceled sentence','omitted','beside second central / Cela signifie line','The short cancelled note is in the left margin at the height of the Cela signifie insertion, above the final cancellation block.','marginleft; Cela-guide','insertion or placement','high',True,False)
ch('Cela signifie relative to canceled abbreviation','deleted i.e. then insertion','insertion then deleted i.e.','deleted i.e. then insertion','The added words are above the canceled abbreviation, whose former place is replaced before que; the deletion is retained before its replacement.','centralpunct; Cela','insertion or placement','high',False,True)
r.r['inspection_note']+=' Final dash enlargement confirmed the short mark. A first motifs-m crop clipped the left edge and was replaced by motifs-m-full; both recipes remain documented. The expanded view shows one m body with a weak right-side trace, insufficient positive evidence for a repeated-strike alphabet.'
r.save('work/record124.json')
