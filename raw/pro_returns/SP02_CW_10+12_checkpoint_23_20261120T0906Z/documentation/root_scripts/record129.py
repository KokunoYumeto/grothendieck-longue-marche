from pathlib import Path
import sys,json
sys.path.insert(0,str(Path('SP02_CW_10+12/scripts').resolve()))
from root_record import Record
r=Record('B10-09',10,129); ch=r.change
def hd(s):return r'\handwritten{\begin{tikzpicture}[x=.35cm,y=.35cm,baseline=-.2ex]'+s+r'\end{tikzpicture}}'
def guide(n):return hd(r'\draw (0,-.5) .. controls (-.1,-.15) and (0,.1) .. (.4,.1)--('+str(n)+r',.1) .. controls ('+str(n+.3)+r',.1) and ('+str(n+.4)+r',.2) .. ('+str(n+.3)+r',.5);')
qword=r'Que\unsure{\rlap{e}s|s}tion'
abbr=r'com\unsure{\rlap{d}p|\rlap{b}p|p}a\unsure{t\handwritten{b.}|t\handwritten{s.}|t.}'
HG=r'\unsure{\rlap{\(G\)}H|\mathbb H|\mathbb G}'
hat=hd(r'\draw[line width=.6pt] (0,0)--(.3,.3)--(.55,0)--cycle;\draw (.3,.3)--(.3,.65);\draw[line width=.6pt] (-.08,.62)--(.3,.86)--(.52,.64)--(.12,.64);')
tau=r"\unsure{\tau^{\scriptscriptstyle\cdot}|\tau'|\tau}"
indep=r'indépendam\unsure{\rlap{e}m|m}\unsure{\rlap{m}e|\rlap{n}e|e}\unsure{\rlap{e}n|n}\unsure{\rlap{n}t|t}'
# C is an editing base only. All changes below are root decisions after actual image views.
r.edit(r'\uline{Question}',r'\uline{'+qword+'}')
r.edit(r'\unsure{symé}','symé')
r.edit(r'\unsure{compat.|compa\handwritten{t.}}',abbr)
r.edit(r'\unsure{le foncteur|le torseur}','le foncteur')
r.edit(r'\unsure{\mathbb{H}|\mathbb{G}}',HG)
r.edit(r"F'=F\otimes_k k'",r"F'=F\unsure{\otimes|\Omega}_k k'")
r.edit(r'seu\deleted{\unsure{x}}lement',r'seu\deleted{e}lement')
r.edit(r"(s'en passer ?).}",r"(s'en passer ?).}"+guide(13.5))
r.edit(r'\unsure{ci-dessus}','ci-des')
r.edit(r'commutativité $\handwritten{\psi}$',r'commutativité $\handwritten{\unsure{\psi|\phi}}$')
r.edit('cela près','celà près')
r.edit(r'\unsure{dual.|aussi.}','dual.')
r.edit(r'\uuline{soit} dual.)}}',r'\uuline{soit} dual.)}}'+guide(7.5))
r.edit(r'L\overset{\handwritten{\scriptscriptstyle\wedge}}{\otimes}_U',r'L\overset{'+hat+r'}{\otimes}_U')
r.edit(r'\unsure{(donc de pro-objet de}','(donc de pro-objet de')
r.edit(r"\unsure{à l'aide de}","à l'aide de")
r.edit(r'\xrightarrow{a\otimes\mathrm{id}_U}',r'\xrightarrow{\underline a\otimes\mathrm{id}_U}')
r.edit(r'\margin{?}',r'\margin{\handwritten{?}}')
r.edit(r'intrinsèque à $C\otimes',r'intrinsèque : $C\otimes')
r.edit(r'\unsure{\otimes|\circ}',r'\unsure{\circ|\otimes}')
r.edit(r'Ceci\deleted{x}',r'Ceci\deleted{\unsure{s|x}}')
r.edit(r'\inserted{plus haut,}',r'\inserted{plus haut,}'+guide(4.5))
r.edit(r'isomorphismes de symétrie',r'isomorphismes de symétr\unsure{\rlap{t}i|i}e')
r.edit(r'dans $C$ défini',r'dans $C$ d\unsure{e|é}fini')
r.edit(r'\deleted{\unsure{montrer}}',r'\deleted{le montrer}')
r.edit(r'\deleted{\unsure{s}}action',r'\deleted{e}action')
r.edit(r'U^+ .\handwritten{\tau}=0',r'U^+ .\handwritten{'+tau+r'}=0')
r.edit(r'\inserted{\handwritten{[Vérifier dans le cas gradué ce qui en est !]}}',r'\inserted{\handwritten{[Vérifier dans le cas gradué ce qui en est !]}}'+guide(11.0))
r.edit('résultat souhaité',r'résultat souhai\deleted{t}té')
r.edit(r'(Mais cf exemples n\textsuperscript{o}12).',r'(Mais, cf exemples n\textsuperscript{o}1\unsure{2|1}).')
r.edit(r'b) Montrer que structure $\otimes$',r'b) Montrer que structure $\unsure{\ominus|\otimes}$')
r.edit(r'\unsure{ses axiomes}','ses axiomes')
r.edit(r'G:\unsure{C|\mathcal{C}}',r'G:C')
r.edit(r'\unsure{\check{X}|\check{\otimes}}',r'\check{X}')
r.edit(r'\handwritten{avec $\check{X}$}}',r'\handwritten{avec $\check{X}$}}'+guide(2.6))
r.edit(r'\unsure{indépendamment|indépendammment}',indep)
# Enclosing top marginal curve, with its relation to the full note retained.
C=Path('source/SP02_CW_10+12_witnesses/codex/B10-09/pages/B10-09_10_scan129.tex').read_text()
top=next(x for x in C.splitlines() if x.startswith(r'\margin{\handwritten{\uline{NB}}'))
# The replacement is applied after the earlier textual edits, with the same explicit edits reflected in this target.
for e in r.r['edits']:
 top=top.replace(e['old'],e['new'])
body=top[len(r'\margin{'):-1]
boxed=r'\margin{\begin{tikzpicture}[x=.35cm,y=.35cm,baseline=(n.base)]\node[anchor=north west,align=left,text width=12cm] (n) at (.6,0) {'+body+r'};\draw (.45,.2) .. controls (-.1,-.2) and (-.3,-2.6) .. (.2,-3.3) .. controls (.9,-4) and (2,-3.2) .. (4,-3.1);\end{tikzpicture}}'
r.edit(top,boxed)
# Every C uncertainty and every actual difference from H is recorded with root-viewed crop evidence.
ch('top NB','underlined handwritten NB','editorial mention only','underlined handwritten NB','The N strokes and B bowls form a separate hand addition with a short rule beneath them.','topNB','omission')
ch('top Question emphasis','underlined','italic','underlined','A distinct horizontal rule lies below Question.','topNB','other')
ch('top Question s cell','s','s',qword,'The s outline has an additional left/lower closed contour and middle bar compatible with an e overlap. The second Question supplies a separately enlarged ordinary s comparator. Order of strikes is not inferred.','Questioncell; Questioncompare; topNB','misread word','medium',True,True)
ch('top enclosing curve','omitted','omitted','long curved left bracket drawn','The stroke starts above NB, descends left of the four typed lines and returns right below comp. toward the main-text beginning.','topNB; base; topcomp','drawing or diagram','high',True,True)
ch('top canceled symé',r'\unsure{symé}','symé','symé','The s curves, y descender, m stems and é accent survive beneath the x cancellation. C doubt resolved.','topsyme','misread word','high',True,False)
ch('top final abbreviation',r'\unsure{compat.|compa\handwritten{t.}}','compat.',abbr,'After com, the p-like descending stem coexists with an upper d/b-like ascender. After a and t is a separate tall looped b-like trace and a period. The alternatives retain the uncertain overlap and terminal letter rather than normalize the abbreviation.','topend; topabbr','misread word','low',True,True)
ch('first-line deletion',r'\unsure{le foncteur|le torseur}',r'\ill{}','le foncteur','The l/e cells, tall f, o, n arch, open c, t and eur contours remain visible under the x strikes. C doubt resolved.','cancellet',r'readable ink left as \ill{}','medium',True,True,True)
ch('monoid capital',r'\unsure{\mathbb H|\mathbb G}','H',HG,'Two H uprights and a middle bar overlap a curved G-like outer return. Double-struck single-letter readings remain alternatives, because the ink is crowded; ordinary G comparators were enlarged separately.','Hcapital; firstG; torsionG','misread symbol or index','medium',True,True,False,True)
ch('typed tensor family first occurrence',r'\otimes',r'\otimes',r'first \unsure{\otimes|\Omega}; later \otimes','All fourteen typed signs were enlarged. Each has a high rounded outline and a low crossing/foot that can look Omega-like. The first F formula alone carries alternatives; later occurrences use the first candidate. Handwritten operators were examined separately.','Fformula; given1; Cformula; withtensor; Veq; pourTensor; Uo; via; compatotimes; given2; tauV; Uinvariance','misread symbol or index','medium',True,True,False,True)
ch('seulement canceled cell',r'seu\deleted{\unsure{x}}lement','seulement',r'seu\deleted{e}lement','Between u and l the underlying e upper bowl, middle bar and lower curve remain under a separate x strike.','seu','deletion state','high',True,True)
ch('antipodisme emphasis','underlined','italic','underlined','A separate rule runs beneath the typed word.','antipodisme','other')
ch('antipodisme added a',r'\inserted{\underline a}','omitted',r'\inserted{\handwritten{\underline a}}','A small hand a with an independent short underline stands above the word ending.','smalla; antipodisme','omission','high',False,True,False,True)
ch('On suppose insertion guide','omitted','omitted','long lower hooked guide drawn','The line starts down the left of Donnons, runs below the inserted sentence and turns upward at its right end.','antipodisme; given1','drawing or diagram','high',True,True)
ch('isolated left question mark','unmarked text ?','omitted','handwritten ?','A curved hand hook and detached lower point stand in the left margin.','questionmark','omission','high',True,True)
ch('first sigma formula hat','no hat',r'\widehat\otimes','no hat','The line above this first operator is the continuous sentence insertion guide. No separate hat occurs over the tensor sign.','given1; antipodisme','text not on the page','high',False,True,False,True)
ch('deleted ci-des',r'\unsure{ci-dessus}',r'\ill{}','ci-des','Six underlying cells c/i/hyphen/d/e/s are visible. There are no underlying sus letters after them. C doubt resolved to the visible fragment.','cides',r'readable ink left as \ill{}','high',True,True,True)
ch('first symmetry sign',r'\psi',r'\psi',r'\unsure{\psi|\phi}','The looped/forked body is cut by a slanting stem and has an outward upper-left arm. Psi is favored, phi remains possible. The two later main-text recurrences were also enlarged and use psi without repeated doubt marks.','psi1; symetrie; sigmapsiprime','misread symbol or index','medium',True,True,False,True)
ch('celà accent','cela','celà','celà','A separate downward-slanting grave stroke stands over the final a.','cela','abbreviation expanded or spelling modernised','high',True,False)
for place,crop,txt in [('C-prime in base extension','Cformula',"C'"),('C in base extension','Cformula','C'),('C after pro-anneau','Cbody','C'),('C after symétrie','Cmain','C'),('C-prime after psi-prime','Cprime',"C'"),('final category C','Cfinal','C')]:
 ch(place,txt,'underlined '+txt,txt,'The typed open C has no independent lower rule. Its prime, where present, is a separate raised stroke.',''+crop,'misread symbol or index','high',False,True,False,True)
ch('soit par interline',r"(soit par U', double-underlined soit, \unsure{dual.|aussi.})",r"\ill{} U', \ill{}",r"(soit par $U'$, \uuline{soit} dual.)",'The cursive d has a tall loop, followed by u cup, a bowl, l ascender and period. Both soit occurrences, par, U prime, comma and parentheses are readable; the second soit has two rules. C doubt resolved.','soit',r'readable ink left as \ill{}','high',True,True,True)
ch('soit par attachment','insertion after définie','margin note after proanneau','insertion after définie','The parenthesized addition lies above définie and has a hooked guide descending to the following par.','soit','insertion or placement')
ch('soit par guide','omitted','omitted','lower curved guide drawn','A long line follows the lower edge of the parenthesized addition and hooks downward before par.','soit','drawing or diagram','high',True,True)
ch('V equation placement','inline','display','inline','The equation begins the typed line and continues directly with comma and où on the same baseline.','Veq','insertion or placement')
ch('mark over L tensor','single wedge','single hat','two triangular levels joined by vertical stroke, drawn','A lower triangular/angle body is linked by a narrow upright to a second angle above. Collapsing the mark to a single hat loses visible ink.','hatV; Veq','drawing or diagram','high',True,True,False,True)
ch('deleted pro-object phrase',r'\unsure{(donc de pro-objet de}',r'\ill{}','(donc de pro-objet de','The opening parenthesis, donc, de, pro-objet and final de have identifiable contours beneath the x line. No closing parenthesis occurs in the canceled phrase. C doubt resolved.','cancelmodule',r'readable ink left as \ill{}','high',True,True,True)
ch('deleted à aide phrase',r"\unsure{à l'aide de}",r'\ill{}',"à l'aide de",'The grave on à, apostrophe, dotted i, d ascenders and final de are distinguishable beneath the cancellation. C doubt resolved.','delaide',r'readable ink left as \ill{}','high',True,True,True)
ch('second arrow label a',r'a\otimes id_U',r'g\otimes id_U',r'\underline a\otimes id_U','The first letter has an a bowl with a short independent underline and no g descender; the hand tensor cross, id and U subscript are clear.','via','misread symbol or index','high',True,True,False,True)
ch('Ceci canceled cell',r'Ceci\deleted{x}','Ceci',r'Ceci\deleted{\unsure{s|x}}','An s-like lower curve is visible below the crossing x, but dense ink prevents excluding an isolated x. The cell is canceled in either reading.','Ceci; Cecitail','deletion state','medium',True,True)
ch('plus haut placement',r'(1)\inserted{plus haut,}',r'\add{plus haut}, (1)',r'(1)\inserted{plus haut,}','The typed insertion lies above the space after (1), and its comma is on the inserted baseline.','plushaut','insertion or placement')
ch('plus haut guide','omitted','omitted','long hooked lower guide drawn','The line descends at the right of the parenthesized number, passes beneath plus haut and ends in a raised hook.','plushaut','drawing or diagram','high',True,True)
ch('symétrie i cell','i','i',r'\unsure{\rlap{t}i|i}','The dotted i is crossed by an extra mid-height bar and an upper-left ascender compatible with t. Plain i remains an alternative because the strokes overlap densely.','symetrieclose','misread word','medium',True,True)
ch('defini after C accent','défini','défini',r'd\unsure{e|é}fini','No independent typed acute can be isolated over the e; cursive marginal strokes cross the accent area. The presence of an obscured acute remains possible.','def; Borig; Corig','misread word','medium',True,True)
ch('canceled le montrer',r'\unsure{montrer}','les montrer','le montrer','Before montrer the first cell has an l ascender and the second an e bowl/bar. The next x crosses a blank cell, without an underlying s. All montrer cells remain readable.','delmontrer','misread word','medium',True,True)
ch('deleted letter before action',r'\unsure{s}',r'\ill{}','e','The upper closed bowl, horizontal bar and lower left curve form e under the x cancellation. C doubt resolved.','delaction; actiontail',r'readable ink left as \ill{}','high',True,True,True)
ch('point above-right of final tau','tau without extra mark','tau without extra mark',tau,'A separate small dark point sits above the right end of the tau bar. It is retained first as a raised point; prime and an incidental point remain alternatives. No mathematical function is assigned to it.','relation; tauaccent','misread symbol or index','medium',True,True,False,True)
ch('relation multiplication point','baseline period','centered multiplication dot','baseline period','The point between U and tau sits at the low text baseline, distinctly below the middle of the U body.','relation','misread symbol or index')
ch('verification brackets','[Vérifier ... !]','Vérifier ... !','[Vérifier dans le cas gradué ce qui en est !]','The left bracket is a separate upright with upper/lower turns; the right bracket follows the exclamation point.','verifier','omission')
ch('verification placement','inserted after relation','margin note','inserted after relation','The bracketed hand line lies immediately above the gap after the relation period and before the dash.','verifier','insertion or placement')
ch('verification insertion guide','omitted','omitted','long lower hooked guide drawn','A separate thin line descends to the left of the dash, runs below the bracketed note and turns upward after its closing bracket.','verifier','drawing or diagram','high',True,True)
ch('dash before Si','short dash','em dash','short dash','A single short typewriter hyphen stands before Si, not a full-width dash.','Marchait','other')
ch('souhaité internal canceled t','souhaité','souhaité',r'souhai\deleted{t}té','The edge cell after souhai has a t upright, crossbar and lower curl beneath x cancellation. The next line starts with a new t and acute e. Both layers are retained when joining the line-end word.','souhai; souhlast; souhjoin','deletion state','high',True,True)
ch('Mais comma','Mais cf','Mais, cf','Mais, cf','A detached curved comma follows Mais before cf.','Maiscf','omission','high',True,False)
ch('Mais cf period','cf','cf.','cf','The tall f ends without a detached abbreviation point before exemples.','Maiscf','text not on the page')
ch('Mais parenthesis and final period','(Mais ...).','Mais ...','(Mais ...).','Both curved parentheses enclose the hand note, with a detached final period after the right parenthesis.','Maiscf; exnum','omission')
ch('example number','12','11',r'1\unsure{2|1}','The second numeral has a hooked upper stroke, descending curved middle and short rightward foot, favoring 2. Its narrow shape still permits 1. The first numeral is a plain upright.','exnum2; Maiscf','misread symbol or index','medium',True,True,False,True)
ch('Mais placement','insertion after paragraph','margin note','insertion after paragraph','The parenthesized note sits below the paragraph ending and above the next paragraph, attached after après coup.','Maiscf','insertion or placement')
ch('margin a first clause','donner un sens intrinsèque','donner une ill intrinsèque','donner un sens intrinsèque','Rotated upright, un and the s/e/n/s sequence are readable; there is no extra final e on un.','marginA','misread word')
ch('margin a before formula','à',':',':','Two separate ink points precede C, without a joined a bowl and above-letter accent.','Acolon; marginA','misread word','high',True,False)
ch('margin a category','C','underlined C','C','The hand C is one open curve; no underline occurs beneath it.','marginA','misread symbol or index','high',False,True,False,True)
ch('margin a independently phrase','indépendamment de','indépendante ill','indépendamment de','The ending has m/e/n/t strokes followed by de, rather than the adjective ending.','marginA','misread word')
ch('margin a canceled circle',r'\deleted{\unsure{\otimes|\circ}}',r'\ill{}',r'\deleted{\unsure{\circ|\otimes}}','A round outline survives under several oblique cancellation bands. No independent internal cross can be securely separated from the deletion strokes; circle is therefore the first candidate.','Acancel; marginA',r'readable ink left as \ill{}','medium',True,True,True,True)
ch('margin a omitted connective','la donnée de F','ill de F','la donnée de F','La, donnée and de remain readable in the rotated line before the plain hand F.','marginA',r'readable ink left as \ill{}','high',False,True,True)
ch('margin a parenthesis',r"(underlined NB si k' n'est pas un corps, ce n'est pas une catégorie underlined abélienne, seulement additive)",r"(NB k, k' ill une catégorie abélienne uncertain additive)",r"(\uline{NB} si $k'$ n'est pas un corps, ce n'est pas une catégorie \uline{abélienne}, seulement additive)",'The complete rotated note supplies si, one k prime, the negative clauses, corps and seulement. Additive has distinct a/d/d/i/t/i/v/e strokes. Rules beneath NB and abélienne are separate.','marginA',r'readable ink left as \ill{}','high',False,True,True,True)
ch('margin b opening','Montrer que structure','Montrer ill','Montrer que structure','The q loop/descender and following u/e stroke group read que; no apostrophe or separate une is supported. Structure is readable on the following slanted line.','marginB; Bque',r'readable ink left as \ill{}','high',False,True,True)
ch('margin b structure sign',r'\otimes',r'\otimes',r'\unsure{\ominus|\otimes}','The oval encloses a broad near-horizontal bar. A separate crossing stroke is not secure at this locus, so the first candidate is barred-circle form, with tensor retained as an alternative.','Btensor; marginB','misread symbol or index','medium',True,True,False,True)
ch('margin b remainder',r"éventuellement avec données phi,psi,1,vee. se prolonge automatiquement à C', avec unsure ses axiomes",r'\ill{}',r"éventuellement avec données $\varphi,\psi,1,\vee$. se prolonge automatiquement à $C'$, avec ses axiomes",'Every word is readable after rotation, including ses axiomes, whose a/x/i/o/m/e/s sequence resolves C doubt. The listed looped phi, forked psi, 1, vee and C prime are visible.','marginB',r'readable ink left as \ill{}','high',True,True,True,True)
ch('margin c text surrounding formula','complete text','only G:C to Mod(k-prime), remainder ill','complete text','Rotated upright, c) généraliser, pour un foncteur comme, la description du numéro6, en description de C prime, en termes d\'un pro-anneau, et expliciter comment on a encore les diverses structures sur C are all legible.','marginC',r'readable ink left as \ill{}','high',False,True,True,True)
ch('margin c first C',r'\unsure{C|\mathcal C}','underlined C','C','The dark capital is an open C with no inner script stroke or detached underline. C doubt resolved.','marginC; Corig','misread symbol or index','high',True,True,False,True)
ch('margin c endomorphism formula',r"U'=End(G)",r'\ill{}',r"$U'=\mathrm{End}(G)$",'The hand U has a detached high prime, followed by two equality bars, E/n/d, parentheses and G.','Cend; marginC',r'readable ink left as \ill{}','high',False,True,True,True)
ch('margin c final structures',r'\otimes,\varphi,\psi,1,\vee',r'\ill{}',r'\otimes,\varphi,\psi,1,\vee','The final circle has two crossing diagonals; the phi loop/stem, psi fork, 1 and vee are separately visible.','Csymbols; marginC',r'readable ink left as \ill{}','high',False,True,True,True)
ch('intrinsèque emphasis','underlined','italic','underlined','A distinct lower rule spans the word, separate from the descending letter strokes.','intrins','other')
ch('final inserted X mark',r'\unsure{\check X|\check\otimes}','X',r'\check X','The lower glyph has two crossing diagonals without an enclosing circle, with a short V-shaped check above it. C doubt resolved.','avecX','misread symbol or index','medium',True,True,False,True)
ch('avec X insertion guide','omitted','omitted','lower hooked insertion line drawn','The line descends beside the preceding comma, passes under the handwritten addition and turns up at its right edge.','avecX; indep','drawing or diagram','high',True,True)
ch('indépendamment overlapping cells',r'\unsure{indépendamment|indépendammment}','indépendamment',indep,'After the first plain m, four crowded cells combine m/e, e/m-or-n, n/e and t/n-like contours. The overlaid strokes are retained with alternatives. No correction order or extra normalized m is inferred.','indep; independclose; indepcells','misread word','medium',True,True)
for word,crop in [('torseur','quote1'),('proanneau','quote2'),('pro-anneau','quote3'),('invariant','quote4')]:
 ch('quotation marks around '+word,'double quotation marks','guillemets','double quotation marks','Both ends consist of paired short upright quotation strokes, without angle-shaped guillemets.',crop,'other')
for place,crop in [('bimodule U superscript','Uo'),('last U in restriction chain','via')]:
 ch(place,r'U^o',r'U^{\circ}',r'U^o','The raised small round character has the typewriter o body; it is retained as the letter o rather than a mathematical circle glyph.',crop,'misread symbol or index','high',False,True)
# Surviving uncertainty register. Resolved C doubts are recorded in the changes above.
for a,b,c,d,e in [
 ('top Question s',r'\rlap{e}s','s','medium','Extra loop/bar contours favor unlike-letter overlap; compared with the second Question s.'),
 ('top abbreviation p cell',r'\rlap{d}p',r'\rlap{b}p; p','low','Upper ascender and lower p-like descender overlap.'),
 ('top abbreviation ending',r't\handwritten{b.}',r't\handwritten{s.}; t.','low','The terminal tall looped stroke is not securely identified.'),
 ('monoid capital',r'\rlap{\(G\)}H',r'\mathbb H; \mathbb G','medium','H stems and curved G-like return coexist in dense ink.'),
 ('fourteen typed tensor signs',r'\otimes',r'\Omega','medium','First occurrence qualified only; each later occurrence enlarged individually.'),
 ('three main-text symmetry signs',r'\psi',r'\phi','medium','The loop/fork and diagonal stem allow both; later recurrences use the first candidate.'),
 ('canceled margin a circle',r'\circ',r'\otimes','medium','Interior strokes cannot be separated securely from cancellation.'),
 ('Ceci canceled extra cell','s','x','medium','Lower s-like curve survives but is obscured.'),
 ('symétrie i overlap',r'\rlap{t}i','i','medium','Dotted i plus an extra bar/ascender; plain i remains possible.'),
 ('defini accent','e','é','medium','No independent acute visible; handwritten marginal strokes cross the area.'),
 ('raised point beside final tau',r'\tau^{\scriptscriptstyle\cdot}',r"\tau'; \tau",'medium','A distinct raised point is retained without assigning a role.'),
 ('Mais example numeral','12','11','medium','The second digit has an upper hook and rightward lower foot, but is narrow.'),
 ('margin b operator',r'\ominus',r'\otimes','medium','Oval with broad bar; crossing arm not separable.'),
 ('indépendamment four overprinted cells',indep,'simpler single-letter cells; e/n alternative in second mixed cell','medium','Mixed loop, bar, stem and arch traces are visible; strike order unknown.')]:r.doubt(a,b,c,d,e)
r.notation('typed tensor-like family',r'first \unsure{\otimes|\Omega}; thirteen later \otimes','10:129 F1; given1; C-base1; avec1; L1; pour1; Uo1; via2; compat1; given2 1; tauV1; invariance2','uncertain')
r.notation('overlapping monoid capital',HG,'10:129 monoïde','uncertain')
r.notation('main-text symmetry sign',r'first \unsure{\psi|\phi}; later psi and psi-prime','10:129 commutativité; symétrie; after sigma','uncertain')
r.notation('two-level mark over L tensor',hat,'10:129 V=G(U)=L tensor_U(U,int)','raw visible form')
r.notation('underlined antipode letter',r'\underline a','10:129 antipodisme addition and second arrow label')
r.notation('raised point at tau',tau,'10:129 U-plus relation','uncertain')
r.notation('hand margin b barred oval',r'\unsure{\ominus|\otimes}','10:129 structure in margin b','uncertain')
r.notation('hand margin c symbols',r"G:C\to Mod(k'); C'; U'=End(G); C: \otimes,\varphi,\psi,1,\vee",'10:129 margin c; each read after rotation')
r.notation('final checked X',r'\check X','10:129 avec X interline')
r.notation('ordinary typed capitals',r"A,B,C,C',F,F',G,L,U,U^o,V",'10:129 each occurrence inspected; weight alone not treated as double striking')
r.r['abbreviations']=[dict(abbreviation=a,expansion=b,attestations='10:129 '+c) for a,b,c in [('NB','nota bene','top, margin a, and main paragraph'),('comp.','compatibilité','top question'),('sym.','symétries','top question'),('prés.','présence','top question'),('com...atb./ats./at.','compatibilités (tentative expansion only)','top ending; overlapping letters unresolved'),('dual.','dualité / dualement','soit par interline'),('int','intérieur (notation, not expanded in transcription)','U structures'),('cf','confer','Mais note; no period visible'),('nº','numéro','Mais, margin c, final line')]]
o={}
def ov(i,s,**kw):o[f'129-E{i:03d}']=dict(first_words_or_objects=s,**kw)
ov(3,'symé');ov(4,abbr);ov(7,'le foncteur');ov(9,'e');ov(14,'ci-des');ov(15,r'\unsure{\psi|\phi}')
for i in (16,17):ov(i,r"(soit par U', double-underlined soit dual.)")
ov(18,'two triangular levels joined by vertical',kind='drawing');ov(19,'(donc de pro-objet de');ov(21,"à l'aide de");ov(24,r'\xrightarrow{\underline a\otimes id_U}');ov(26,'?',hand='his hand')
for i in (27,28):ov(i,r"a) donner un sens intrinsèque : C tensor_k k', indépendamment de [deleted uncertain circle] la donnée de F (underlined NB si k' n'est pas un corps, ce n'est pas une catégorie underlined abélienne, seulement additive)")
ov(29,r'\deleted{\unsure{\circ|\otimes}}');ov(31,r'\unsure{s|x}');ov(42,'le montrer');ov(47,'e');ov(48,tau)
for i in (51,52):ov(i,r'(Mais, cf exemples nº1\unsure{2|1}).')
for i in (53,54):ov(i,r"b) Montrer que structure uncertain ominus/tensor, éventuellement avec données phi,psi,1,vee. se prolonge automatiquement à C', avec ses axiomes")
for i in (55,56):ov(i,r"c) généraliser, pour un foncteur comme G:C to Mod(k'), la description du nº6 en description de C' en termes d'un pro-anneau U'=End(G), et expliciter comment on a encore les diverses structures sur C: tensor,phi,psi,1,vee")
for i in (58,59):ov(i,r'avec $\check X$')
r.r['inventory_overrides']=o
extras=[('top Question s/e overlap','text','top question first word','typewriter'),('long top left enclosing curve','drawing','top margin','his hand'),('overlapping monoid H/G-like capital','text','first paragraph','typewriter'),('On suppose insertion guide','drawing','above Donnons','his hand'),('soit par lower curved guide','drawing','above définie','his hand'),('plus haut lower hooked guide','drawing','after conditions (1)','his hand'),('symétrie i/t-like overlap','text','lower main paragraph','typewriter'),('raised point over-right of tau','drawing','U-plus relation','his hand'),('verification note lower hooked guide','drawing','above Si ceci marchait','his hand'),('canceled t at souhai line ending','deletion','right edge before next-line té','typewriter'),('avec X lower hooked guide','drawing','final interline','his hand'),('four overprinted cells of indépendamment','text','final line','typewriter')]
for i,(s,k,p,h) in enumerate(extras,1):r.r['inventory_extra'].append(dict(scan='10:129',sheet_kind='typescript',hand=h,element=f'129-R{i:03d}',kind=k,position=p,first_words_or_objects=s,transcribed='yes'))
r.r['crops']=json.loads(Path('work/crops129.json').read_text())
r.r['inspection_note']='Root alone viewed the whole image, both halves, C/H and all16 C doubt loci with all59 C inventory items, then all98 actual enlarged crop views. Margins a/b/c were rotated -32/-34/-37 degrees, with additional rotated detail crops. Every mathematical sign, disputed locus, insertion, deletion and marginal note was enlarged. All agreed prose was read from the whole/half images. All16 C doubts are resolved or explicitly retained with reasons. H exact ending is préli-, not prélim-; the ordinary line-end joining convention leaves préli% in the page. Archive128 remains only an archive comment. No OCR, parallel transcription, context access or mathematical checking occurred.'
r.save('work/record129.json')
