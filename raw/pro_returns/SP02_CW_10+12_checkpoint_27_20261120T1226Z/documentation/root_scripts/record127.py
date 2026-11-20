from pathlib import Path
import sys,json,csv
sys.path.insert(0,str(Path('SP02_CW_10+12/scripts').resolve()))
from root_record import Record
r=Record('B10-09',10,127);ch=r.change
def hd(body):
 return r'\handwritten{\begin{tikzpicture}[x=.4cm,y=.4cm,baseline=-.2ex]'+body+r'\end{tikzpicture}}'
def guide(n):
 return hd(r'\draw (0,-.35) .. controls (.05,-.02) and (.2,.17) .. (.4,.18)--('+str(n)+r',.18) .. controls ('+format(n+.2,'.2f')+r',.18) and ('+format(n+.32,'.2f')+r',.3) .. ('+format(n+.3,'.2f')+r',.45);')
U=r'\unsure{\rlap{\(\mathrm u\)}U|\mathbb U}'
A=r'\unsure{\rlap{\(\mathrm a\)}A|\mathbb A}'
M=r'\unsure{\rlap{\(X\)}M|\mathbb M}'
M2=r'\rlap{\(X\)}M'
plets=r'p\rlap{r}l\rlap{e}ats'
daut=r"$\mathbb{D}$'$\mathbb{a}\mathbb{u}\mathbb{t}$re"
coa=r'coa\deleted{g}l\`{g}èbre'
par=r'\unsure{$U\to$|par}'
rawmark=hd(r'\draw[line width=.3pt] (.08,.28)--(.07,.02) .. controls (.15,-.11) and (.3,.02) .. (.35,.2)--(.43,-.06);\draw[line width=.55pt] (0,-.14)--(.32,.19);\fill[gray] (.08,.4) circle (.025);')
caret=hd(r'\draw (0,.23)--(.14,0)--(.3,.21);')
separating=r'\begin{tikzpicture}[x=.35cm,y=.35cm,baseline=(n.base)]\node[anchor=north west,align=left,text width=3cm] (n) at (0,0) {séparer les conditions, commencer par exactitude = platitude \handwritten{sur les $U_\alpha$}};\draw (8.1,.2) .. controls (9.3,-.8) and (9.0,-2.2) .. (8.4,-3.0) .. controls (8.1,-3.5) and (7.7,-3.9) .. (7.4,-4.0)--(6.3,-4.0);\end{tikzpicture}'
lowtext=r'Commençons '+par+r' tout exprimer du côté de $U,L$, et ne '+rawmark+r" dualisons qu'à la fin"
lower=r'\begin{tikzpicture}[x=.35cm,y=.35cm,baseline=(n.base)]\node[anchor=north west,align=left,text width=3.4cm] (n) at (0,0) {\handwritten{'+lowtext+r'}};\draw (7.2,.8) .. controls (9.2,.7) and (8.8,-1.6) .. (9.7,-2.7) .. controls (10.2,-4.3) and (9.5,-5.8) .. (8.6,-6.8);\draw[line width=.2pt] (10.2,3.5) .. controls (10.1,1.0) and (10.6,-3.0) .. (10.4,-7.2);\end{tikzpicture}'
# Exact, root-decided edits to C. No context has been opened.
r.edit(r"\handwritten{\sigma'}",r"\handwritten{\sigma}'",2)
r.edit(r'\overset{\handwritten{\scriptscriptstyle\wedge}}{\otimes}_kU\handwritten{\longrightarrow}',r'\overset{\handwritten{\scriptscriptstyle\wedge}}{\unsure{\otimes|\Omega}}_kU\handwritten{\longrightarrow}')
r.edit(r'\unsure{\mathbb{U}|U}',U)
r.edit(r'\unsure{\mathbb{A}|A}',A)
r.edit(r'de\deleted{\unsure{algèbres}}',r"d\rlap{'}e\deleted{algèbre}")
r.edit(r"\inserted{(modules proj de t f sur $k'$)}",r"\inserted{(modules proj de t f sur $k'$)"+guide(4.7)+'}')
r.edit(r'G^{\unsure{k}}',r'G^{\deleted{k}}')
r.edit(r"\inserted{$C\handwritten{\to}\mathrm{Mod}(k')$}",r"\inserted{$C\handwritten{\to}\mathrm{Mod}(k')$}"+guide(2.5))
r.edit(r'un $L=(L_',r'un $\rlap{(}L=(L_')
r.edit(r'\inserted{à droite}',r'\inserted{à droite'+guide(1.4)+'}')
r.edit(r'\unsure{S|s}',r'\unsure{s|S}')
r.edit(r'G(\mathbb{M})=L\otimes_U\mathbb{M}',r'G('+M+r')=L\otimes_U'+M2)
r.edit(r"d'un\deleted{\unsure{e}}",r"d'un\deleted{e}")
r.edit(r"L\otimes_{U'}X'",r"L\otimes_{\mathbb U'}X'")
r.edit(r"où $X'=X\otimes_kk'$.}",r"où $X'=X\otimes_kk'$."+guide(8.6)+'}')
r.edit(r'\unsure{\mu|\alpha}',r'\unsure{\alpha|\mu}')
r.edit(r'\unsure{plets|plats} sur \uline{les}',plets+r' s\uline{ur les}')
r.edit(r'\margin{séparer les conditions, commencer par exactitude = platitude\handwritten{sur les $U_\alpha$}}',r'\margin{'+separating+'}')
r.edit("D'autre part",daut+' part')
r.edit(r'\inserted{\handwritten{\unsure{c}}}',r'\inserted{\handwritten{\unsure{c}}'+caret+'}')
r.edit(r'\unsure{comp.tibles}',r'comp.tibles')
r.edit(r'\inserted{(\unsure{contravariété|contravariants})}',r'\inserted{(\unsure{contravariété|contravariants})}'+guide(3.1))
r.edit(r"\unsure{antipodisme} $U'$",r"\unsure{antipodisme} $\unsure{U'}$")
r.edit(r'\quad(\handwritten{\simeq}L',r'\quad(\handwritten{\unsure{\simeq|\xrightarrow{\sim}}}L')
r.edit(r'\unsure{[|(}\unsure{grâce|voir}',r'[grâce')
r.edit(r"à l'antipodisme:\unsure{)|]}",r"à l'antipodisme:)")
r.edit(r'$x\otimes u\longrightarrow x\otimes(u\otimes1)$]}}',r'$x\otimes\unsure{U|u}\longrightarrow x\otimes(u\otimes1)$]}'+guide(3.2)+'}')
r.edit(r'\inserted{\handwritten{il est}}',r'\inserted{\handwritten{il est}'+guide(1.4)+'}')
r.edit('coargèbre',coa)
r.edit(r"\margin{\handwritten{Commençons \unsure{par} tout exprimer du côté de $U,L$, et ne dualisons qu'à la fin}}",r'\margin{'+lower+'}')
r.edit(r"\unsure{k'|U'}",r"\unsure{U'|k'}")
r.edit(r'\otimes a.',r'\otimes\underline{a}.')
# Full collation and every original C doubt, including retained doubts.
ch('opening nested s deletion',r'de\deleted{s}','de',r'de\deleted{s}','The final s is separately crossed inside the larger cancellation; its two curved lobes remain visible.','dels','omission')
for place,crop in [('first sigma-prime','topprime1'),('second sigma-prime','topprime2')]:
 ch(place,'prime inside handwritten scope','prime','typed prime beside handwritten sigma','The prime is a dense typewriter mark with the same head and tail as typed apostrophes. The sigma itself is a thinner hand stroke.',''+crop,'other','high',True,False)
ch('typed tensor family, first of fifteen',r'\otimes',r'\otimes',r'\unsure{\otimes|\Omega}; later occurrences use \otimes','All fifteen typed signs were enlarged. Their high rounded outline and crossed inner strokes favor tensor; the Omega-like body warrants the alternative at the first occurrence. The hats and all subscripts are separate visible marks.','topformula; deltatensor; cformula; GMM; Xinsert; Ldisplayfull; formula2; formula3','misread symbol or index','medium',True,True,False,True)
ch('initial U prime',r'\unsure{\mathbb U|U}',r"U'",U+"'",'The cell has upper and lower serif levels on each side and a shared baseline. A smaller u overlapping a capital U is favored; a repeated U strike remains possible. C doubt is revised rather than silently resolved.','Uprime; Uclose','misread symbol or index','medium',True,True,False,True)
ch('initial A prime',r'\unsure{\mathbb A|A}',r"A'",A+"'",'The capital triangle/crossbar coexists with lower rounded bowl/foot traces. Lowercase a over uppercase A is favored; a repeated A remains possible.','Aprime; Aclose','misread symbol or index','medium',True,True,False,True)
ch('structures, live d/e and apostrophe',r'de\deleted{\unsure{algèbres}}',r"\struck{d'algèbre}",r"d\rlap{'}e\deleted{algèbre}",'The d remains live; the next cell contains a full e and a raised apostrophe. The cancellation begins with algèbre, whose final visible letter is e, with no plural s. C doubt is resolved to the singular and both overlapping impressions retained.','algebres; algebresclose','deletion state','high',True,True)
ch('category in first functor','C','underlined C','plain C','There is no separate lower rule beneath the typed C.','Gfun','misread symbol or index','high',False,True,False,True)
ch('canceled target of first functor',r'\mathrm{Modtf}(',r'\operatorname{Modf}',r'\deleted{\mathrm{Modtf}(}','The t upright/crossbar and the opening parenthesis remain beneath typewriter x strikes. The closing traces do not establish an additional k.','Gfun','omission')
ch('modules explanatory insertion placement','inserted parenthesis','marginal parenthesis','parenthesis inserted below functor with guide','A hand leader connects the parenthetical typed explanation to the functor line. It is not an independent margin paragraph.','modules','insertion or placement')
ch('modules insertion guide','omitted','omitted','long curved guide drawn','The line turns upward at the insertion point and follows the explanatory parenthesis before rising at its far end.','modules','drawing or diagram','high',True,True)
ch('exacts et and linéaires underlining',r'\uline{exacts et} k-\uline{linéaires}','italic exacts et k-linéaires','two separate underlines, excluding k and hyphen','Two detached rules span exacts et and linéaires; neither k nor the intervening hyphen lies over the rule.','Gfun; cformula','other')
ch('c formula relation',r'\simeq',r'\xrightarrow{\sim}',r'\simeq','The hand mark is a wave over a straight bar with no arrowhead.','cformula','misread symbol or index','high',False,True,False,True)
ch('c formula second tensor subscript','no subscript','k','no subscript','The lower space beneath the second typed operator is blank.','cformula','text not on the page','high',False,True,False,True)
ch('canceled word before Tout',r'\unsure{son}',r'\ill{}',r'\deleted{\unsure{son}}','The o and n are visible beneath the x strikes; the first cell is more heavily covered and only favors s. C doubt retained.','son',r'readable ink left as \ill{}','low',False,True,True)
ch('raised k at G',r'G^{\unsure{k}}','G',r'G^{\deleted{k}}','The small k has a visible upright and diagonal branches, with independent crossing x strokes through it. Its identity is resolved and its canceled state restored.','Gk; Gkclose','deletion state','high',True,True,False,True)
ch('second category C','C','underlined C','plain C','The typed open curve has no detached underline.','Cmod','misread symbol or index','high',False,True,False,True)
ch('C to Mod insertion placement','inserted','marginal','interlinear insertion with guide','The smaller line stands between the prose lines and is tied to exact à droite by its hand leader.','Cmod','insertion or placement')
ch('C to Mod insertion guide','omitted','omitted','long guide drawn','A separate thin hand line runs under the added functor and bends into the insertion point.','Cmod','drawing or diagram','high',True,True)
ch('initial L of L=(L_alpha)','L','L',r'\rlap{(}L','An opening-parenthesis curve extends above and below the ordinary L upright and foot in the same cell.','L1; Lparen','misread symbol or index','high',True,True,False,True)
ch('à droite insertion guide','omitted','omitted','guide drawn','A thin separate line marks the insertion before sur U and curls around the typed à droite.','droite','drawing or diagram','high',True,True)
ch('canceled sur k',r'\deleted{sur k}',r'\struck{\ill{}}',r'\deleted{sur k}','The s, u, r and k remain legible under separate x strikes.','surk',r'readable ink left as \ill{}','high',False,True,True)
ch('extra NB subscript',r'\unsure{S|s}','omitted',r'\unsure{s|S}','A small curved s-shaped letter stands beside alpha and overlaps the parenthesis. Its height favors lowercase s, but case remains uncertain.','NBformula; NBsclose','omission','medium',True,True,False,True)
for i,crop in [(1,'Mclose1'),(2,'Mclose2')]:
 ch('M in G(M) display, occurrence '+str(i),r'\mathbb M','M',M if i==1 else M2,'Alongside the M verticals and central V, diagonal strokes cross down toward both feet, favoring X/M overlap. A double M remains the alternative at the first occurrence; the identical second cell uses the first candidate.','GMM; '+crop,'misread symbol or index','medium',True,True,False,True)
ch('k canceled prime',r"k^{\deleted{\unsure{'}}}",'k',r"k^{\deleted{\unsure{'}}}",'A faint raised oblique mark remains beneath the cancellation, favoring a prime but not settling it. C doubt retained.','kprime','omission','low',False,True)
ch('linéarite ending','linéarite','linéarité','linéarite','The final e has no accent above it.','linearite','abbreviation expanded or spelling modernised')
ch('dune canceled e',r"d'un\deleted{\unsure e}","d'un",r"d'un\deleted e",'The e loop and horizontal middle bar are visible under the x. C doubt resolved.','dune','omission','high',True,True)
ch('U prime subscript in inserted G(X) formula',r"U'",r"U'",r"\mathbb U'",'Closely offset parallel U uprights and two lower curves establish two strikes of the same capital, unlike the mixed-case ambiguity in the opening U.','Xinsert; Usubinsert','misread symbol or index','high',True,True,False,True)
ch('On peut alors insertion guide','omitted','omitted','long insertion guide drawn','The hand leader runs below the long typed addition and returns toward the insertion point.','Xinsert','drawing or diagram','high',True,True)
ch('Le fait que clause deletion state','live through Projf(k prime); only s exprime canceled','whole clause canceled','live clause; only s exprime canceled','The x strikes are confined to the two cells/groups of s\'exprime. The preceding words and displayed target have clear uncanceled bodies.','Le','deletion state','high',False,True,False,True)
ch('et que le foncteur clause state','live body text','insertion','live body text','The clause follows the cancellation on the same typed baseline, without an insertion mark around it.','etG','insertion or placement')
ch('sur k prime underline','sur only','sur k prime','sur only','The underline ends before the space preceding k prime.','suruline','other')
ch('L index before plets',r'\unsure{\mu|\alpha}',r'\alpha',r'\unsure{\alpha|\mu}','The lower closed loop and rightward tail favor alpha, while the crowded middle stroke still permits mu. C candidates are reordered from the ink.','mu','misread symbol or index','medium',True,True,False,True)
ch('plets overprints',r'\unsure{plets|plats}','plats',plets,'The second cell has both an r shoulder and an l ascender; the next has an e middle bar and an a bowl. Both layers are retained, resolving the competing normalized whole-word readings.','plets','misread word','high',True,True)
ch('sur les underline after plets','les','plats sur les U alpha',r's\uline{ur les}','The rule starts under the right part of u, after s, and ends after les. No underline lies under the overprinted word or the following U.','lesuline; surleswide','other','high',True,True)
ch('summary sentence emphasis','five separate word underlines','whole phrase italic including formulas','five separate word underlines retained','The rules span modules; sur; tels que les; soient plats sur; et proj de tf sur. The intervening formulas have no separate lower rule.','summaryl; summaryplat','other')
ch('séparer conditions enclosing bracket','omitted','omitted','right curved bracket drawn','The long hand curve encloses the marginal typed instructions and the hand line sur les U_alpha.','marginsep','drawing or diagram','high',True,True)
ch('D autre initial cells',"D'autre","D'autre",daut,'The D, a, u and t each have closely offset duplicate contours of the same letter. The r and e have single contours. Only the four repeated cells are encoded with mathbb.','dautre','misread word','high',True,True)
ch('Conditions correction',r'\deleted C\inserted{\unsure c}','conditions',r'\deleted C\inserted{\unsure c}','A large typed C is crossed; a small curved hand glyph above it favors c but remains cramped. The C doubt is retained.','cond; handc','deletion state','medium',False,True)
ch('Conditions insertion caret','omitted','omitted','small v-shaped caret drawn','Two short hand strokes form a pointed insertion mark beside the small replacement letter.','handc','drawing or diagram','high',True,True)
ch('si dans placement','interlinear insertion','marginal note','interlinear insertion','The long hand sentence runs above the platitude/isomorphism prose and is tied to that location.','siinsertion','insertion or placement')
ch('si dans C alphabet','plain C','underlined C','plain C','The open hand C has no separate lower stroke.','Csi','misread symbol or index','high',False,True,False,True)
ch('vee position','baseline vee','superscript vee','baseline vee','The vee occupies the same writing baseline as 1 and the surrounding words.','siinsertion','misread symbol or index','high',False,True,False,True)
ch('comp.tibles',r'\unsure{comp.tibles}','compatibles','comp.tibles','A clear point follows p, with t immediately after the point. There is no a between them. C doubt resolved without expansion.','compatible','abbreviation expanded or spelling modernised','high',True,True)
ch('avec and inner parenthesis',r'avec\inserted{(\unsure{contravariété|contravariants})}',r'\ill{}',r'avec\inserted{(\unsure{contravariété|contravariants})}','Avec and both parentheses are visible. The small inner word favors the accented té ending, but its compressed middle and ending remain ambiguous. The C word doubt is retained.','compatible; innerparenthesis',r'readable ink left as \ill{}','low',False,True,True)
ch('inner parenthesis guide','omitted','omitted','curved guide drawn','A thin line beneath the comp.tibles/avec area links the smaller parenthetical addition to its insertion point; it is not a word underline.','compatible; innerparenthesis','drawing or diagram','high',True,True)
ch('Delta subscript in si insertion',r'\Delta_U',r'\Delta u',r'\Delta_U','The U is a distinct lowered capital beside Delta.','unitaire','misread symbol or index','high',False,True,False,True)
ch('U avec antipodisme state','U avec live',r'\struck{\ill{}} antipodisme','U avec antipodisme live','The capital U has redrawn contours but no independent cancellation through it; avec is readable and uncanceled.','unitaire',r'readable ink left as \ill{}','high',False,True,True,True)
ch('à droite footnote reference','(*)','omitted','(*)','A star enclosed by two curved parentheses follows à droite.','adroite','omission')
ch('crossed diagonal margin, first phrase',r'\unsure{en le dualisant}','omitted',r'\deleted{\unsure{en le dualisant}}','The rotated line shows en, a looped le and strokes favoring dualisant, but the first and middle connections remain crossed. C doubt retained.','crossmarginwide; crossline1; crossline2','omission','low',False,True)
ch('crossed diagonal margin, second phrase',r'\unsure{faisant intervenir}','omitted',r'\deleted{\unsure{faisant intervenir}}','The descending opening and subsequent low joins/tall strokes favor the supplied phrase; cancellation and typed Conditions obscure several connections. C doubt retained.','crossmarginwide; crossline2; crossline3','omission','low',False,True)
ch('crossed diagonal margin, obscured words',r'\illegible{2}','omitted',r'\deleted{\illegible{2}}','Two short word spaces are physically obscured by intersecting cancellation, typed letter bodies and a vertical rule. No replacement words are inferred. The count is approximate.','crossmarginwide; crossline2','omission','low',False,True)
ch('crossed diagonal margin, antipodisme',r"d'un \unsure{antipodisme}",'omitted',r"\deleted{d'un \unsure{antipodisme}}",'The d, apostrophe and un remain legible; the following long word has strokes consistent with antipodisme, but the typed donnée/Conditions overlap prevents certainty. C doubt retained.','crossline3; cancelend','omission','low',False,True)
ch('crossed diagonal margin, terminal symbol',r"U'",'omitted',r"\deleted{\unsure{U'}}",'A low rounded U-like join and a detached high stroke at the right of the canceled note favor U prime, but their separation from the compressed word ending is not secure. This is distinct from the dark mark on the lower Commençons line.','crossmarginwide; cancelend','misread symbol or index','low',True,True,False,True)
ch('first completed tensor subscript in L display',r"k'",r"\uncertain{k'}",r"k'",'The small hand k has an upright and two branches; a separate raised prime follows it.','Ldisplay; Ldisplayfull','misread symbol or index','high',False,True,True,True)
ch('first relation inside parenthesis',r'\simeq',r'\simeq',r'\unsure{\simeq|\xrightarrow{\sim}}','There is a wave over a horizontal bar and an additional short slanted tick at its right. No clean arrowhead can be separated, so simeq is favored but the arrow alternative is retained.','formula2; firstrel','misread symbol or index','medium',True,True,False,True)
ch('canceled relation in long display',r'\deleted{\unsure{\simeq}}','omitted',r'\deleted{\unsure{\simeq}}','The underlying wave/bar-like traces are crowded beneath several crossing strokes. C doubt remains; the canceled precursor is not omitted.','deletedrel','omission','low',False,True)
ch('following live relation in long display',r'\simeq',r'\xrightarrow{\sim}',r'\simeq','The live sign has a wave and single bar without a terminal arrowhead.','formula3','misread symbol or index','high',False,True,False,True)
ch('bracket before grâce',r'\unsure{[|(}','(',r'[','Short rightward top and bottom returns connect to the vertical left side. C doubt resolved to a square bracket.','bracketinsert; firstbracket','other','high',True,True)
ch('grâce word',r'\unsure{grâce|voir}','grâce','grâce','The initial g descender, r, circumflex over a, c and e are distinguishable. C doubt resolved.','bracketinsert','misread word','high',True,False)
ch('punctuation after antipodisme',r':\unsure{)|]}',')',r':)','Two separate points precede a curved closing parenthesis. C bracket doubt resolved; the colon omitted in H is retained.','bracketinsert','omission','high',True,True)
ch('first u-shaped map operand','u','u',r'\unsure{U|u}','The first operand has a tall left stem and broad flat low return, unlike the smaller u inside the target parenthesis. Capital U is favored, with lowercase retained because of the variable hand size.','mapformula; mapu1; mapu2','misread symbol or index','medium',True,True,False,True)
ch('map arrow',r'\longrightarrow',r'\mapsto',r'\longrightarrow','The shaft begins without a perpendicular tail and ends in a right-pointing head.','mapformula','misread symbol or index','high',False,True,False,True)
ch('final bracket of map addition',']','omitted',']','A vertical line with short leftward returns closes the complete addition after the formula.','mapformula','omission')
ch('map addition placement and guide','inserted, guide omitted','marginal','inserted with guide drawn','The hand text is over the long display and a leader connects its left edge to the first parenthetical expression.','bracketinsert; formula2','insertion or placement','high',True,True)
ch('il est insertion guide','omitted','omitted','guide drawn','A short slanting hand leader ties il est to the a fortiori phrase.','ilest','drawing or diagram','high',True,True)
ch('coalgèbre physical correction','coargèbre','coalgèbre',coa,'The fourth cell has a g bowl and descender beneath an x cancellation. The next cell is a live l. The following live g bears a separate grave stroke, and the following è also has its grave accent. Both impressions and both accents are retained.','coarg; coalgcorrection','deletion state','high',True,True)
ch('lower Commençons note','full note with unsure par','unreadable second diagonal note','full note retained with revised mark and drawings','The enlarged note reads Commençons, tout exprimer du côté de U,L, et ne, dualisons qu\'à la fin; it remains live. The one compressed mark and an extra small stroke cluster are treated separately.','marglower; marglowerclose',r'readable ink left as \ill{}','high',False,True,True)
ch('mark after Commençons',r'\unsure{par}','omitted',par,'Two tall strokes join in a U-shaped low turn, followed by a short right-pointing angular form. U-to best describes the visible shape; the compressed prose reading par remains an alternative. The bracket crosses its right side.','parclose','misread word','low',True,True)
ch('small mark before dualisons','omitted','omitted','raw stroke cluster reproduced','A small grey upper point/stub lies over two darker intersecting oblique/curved strokes. No lexical identity or deletion state is imposed.','marglowerclose; margrawmark','drawing or diagram','low',True,True)
ch('lower margin bracket and separator','omitted','omitted','curved bracket and separate thin vertical line drawn','The dark enclosing curve and the straighter thin rule are distinct; the rule extends upward past the canceled diagonal note.','separator; marglowerclose; parclose','drawing or diagram','high',True,True)
ch('footnote dans','dans','sur','dans','A looped d, low a, n connection and final s are visible.','footerintro; footerwhole','misread word')
ch('footnote tensor subscript',r"\unsure{k'|U'}",'U',r"\unsure{U'|k'}",'The subscript has a rounded low U-like turn, with a separate short raised stroke. Its tall left stroke touches the tensor sign; no clean k branch is visible, but that alternative cannot be excluded.','footertensor','misread symbol or index','medium',True,True,False,True)
ch('first footnote law',r'à droite des \unsure{mult.} de U prime',r'déduite de celle de \uncertain{U prime}',r'à droite des \unsure{mult.} de U prime','The opening reads à droite des, followed by a compressed looped word favoring mult. and then de U prime. The abbreviation remains uncertain; the final U and prime are clear.','footerlaw1; multclose; footerwhole','misread word','low',False,True,True)
ch('second footnote law de','de','du','de','The second letter has an e loop and low exit, not a u trough.','footerlaw2','misread word')
ch('second law mod punctuation','mod :','mod. :','mod :','Only two vertically separated points follow mod; there is no additional baseline dot.','footerlaw2','other')
ch('second law droit','droit',"d'abord",'droit','The word has the low r-o-i sequence and terminal t; there is no apostrophe or b ascender.','footerlaw2; footerwhole','misread word')
for place in ['U superscript o after tensor','U superscript o in bracket']:
 ch('third footnote line '+place,r'U^o',r"U'^{\circ}",r'U^o','The upper o/circle is present, but no independent prime stands between U and that superscript.','footerlaw3; law3full','text not on the page','high',False,True,False,True)
ch('fourth footnote line operator',r'a.','g',r'\underline{a}.','The letter is a closed a bowl with right downstroke, followed by a dot; a short independent line lies below the letter. No g descender is visible.','footerlaw4; law4full; aoperator','misread symbol or index','high',True,True,False,True)
ch('fourth footnote line Delta subscript',r'\Delta_U',r'\Delta u',r'\Delta_U','The lowered U has its own two uprights and rounded bottom beside Delta.','law4full','misread symbol or index','high',False,True,False,True)
ch('footnote brace','left brace only','left and right braces in quoted note','left brace only','A long left brace groups the four hand lines; the right edge has no matching brace. H\'s quoted closing brace has no ink counterpart.','brace; footerwhole','text not on the page')
# Remaining uncertainty register.
for line,reading,alt,conf,why in [
 ('fifteen typed operators',r'\otimes',r'\Omega','medium','Only the first occurrence is marked; the same high rounded crossed shape recurs fourteen times. Six hand tensor signs have separately visible crossed circles.'),
 ('initial U prime',r'\rlap{\(\mathrm u\)}U',r'\mathbb U','medium','Different upper/lower serif levels favor mixed case, but same-letter repetition is not excluded.'),
 ('initial A prime',r'\rlap{\(\mathrm a\)}A',r'\mathbb A','medium','Lower bowl traces favor a/A overlap; duplicated A remains possible.'),
 ('canceled word before Tout','son','','low','The first cell is obscured by x cancellation; o and n are clearer.'),
 ('NB extra subscript','s','S','medium','Small height favors s; overlap with the parenthesis blurs its ends.'),
 ('two M cells in G(M)',r'\rlap{\(X\)}M',r'\mathbb M','medium','Crossing low diagonals favor X/M; both occurrences share this doubt, marked at the first.'),
 ('k in k-linearite',"'",'','low','A tiny raised trace beneath cancellation favors a prime.'),
 ('L index before plets',r'\alpha',r'\mu','medium','Low loop/tail favors alpha; central strokes remain crowded.'),
 ('hand replacement for Conditions','c','','medium','A short curved trace is present beside the insertion caret.'),
 ('inner parenthesis after avec','contravariété','contravariants','low','Compressed lettering and guide overlap prevent a secure full reading.'),
 ('canceled diagonal margin, first phrase','en le dualisant','','low','The cancellation and typed baseline obscure joins despite upright enlargements.'),
 ('canceled diagonal margin, second phrase','faisant intervenir','','low','Tall and low strokes support the phrase only provisionally.'),
 ('canceled diagonal margin, two words',r'\illegible{2}','word count approximate','low','The relevant ink is physically masked by several intersecting lines and typed letters.'),
 ('canceled diagonal margin, last word','antipodisme','','low','Middle letters are obscured by the typescript.'),
 ('canceled diagonal margin, terminal symbol',"U'",'terminal letters of preceding word','low','The low rounded join and high stroke cannot be fully separated from the compressed ending.'),
 ('first parenthetical relation',r'\simeq',r'\xrightarrow{\sim}','medium','A short right-side tick accompanies wave and bar, without a secure head.'),
 ('canceled relation',r'\simeq','','low','Underlying two-part sign is crossed repeatedly.'),
 ('first operand after x tensor in hand map','U','u','medium','Height and low flat return favor U; hand size varies.'),
 ('mark after Commençons',r'U\to','par','low','The U-shaped turn and angular right-pointing mark are visible, but their intended lexical identity is unresolved.'),
 ('small mark before dualisons','raw stroke cluster','unassigned letter/deletion','low','Reproduced graphically without imposing a word or cancellation state.'),
 ('footnote tensor subscript',"U'","k'",'medium','Rounded low shape favors U prime; left stroke touches the tensor sign.'),
 ('first footnote law abbreviation','mult.','','low','Two tall strokes follow compressed low loops; the end is blotted.')]:
 r.doubt(line,reading,alt,conf,why)
r.notation('typed tensor-like family',r'first \unsure{\otimes|\Omega}, fourteen later \otimes','10:127 opening four; c formula two; G(M) one; X insertion two; long display six','uncertain')
r.notation('hand tensor signs',r'\otimes','10:127 hand map three; footer intro, third and fourth lines one each')
r.notation('category letters','plain C','10:127 both typed functors and hand si insertion; no independent underline')
r.notation('mixed-case opening overprints',U+'; '+A,'10:127 opening U prime and A prime','uncertain')
r.notation('same-letter repeated U',r'\mathbb U','10:127 inserted L tensor subscript U prime')
r.notation('two M overprints',M+'; '+M2,'10:127 G(M) display','uncertain')
r.notation('typed text repeated letters',daut,'10:127 D autre; only D,a,u,t repeated')
r.notation('physical letter overlaps',r"d\rlap{'}e; \rlap{(}L; "+plets,'10:127 structures; first L; plets')
r.notation('hand map relation and operands',r'x\otimes\unsure{U|u}\longrightarrow x\otimes(u\otimes1)','10:127 antipodisme insertion','uncertain')
r.notation('live isomorphism signs',r'\simeq; \xleftarrow{\sim}; \unsure{\simeq|\xrightarrow{\sim}}; \simeq','10:127 c formula; long display in reading order','locally uncertain')
r.notation('footnote opposite exponent and operator',r'U^o; \underline a.','10:127 footer lines three/four; no primes on U^o')
r.notation('archive pencil folio','comment only','10:127 lower-left pencil 126; base PROMPT rule 4')
r.r['abbreviations']=[dict(abbreviation=a,expansion=b,attestations='10:127 '+p) for a,b,p in [('comm.','commutative','opening k algebra'),('ass.','associative','opening k algebra'),('resp.','respectivement','opening and bigèbre clause'),('proj','projectifs','module explanation and summary'),('t f / tf','type fini','module explanation, summary and B paragraph'),('NB','nota bene','opening and module explanation'),('i.e.','id est','k-linearity and si insertion'),('comp.tibles','compatibles','hand si insertion'),('bim.','bimodule','footer introduction'),('mult.','multiplications (tentative)','first law, uncertain'),('mod','module','second law')]]
r.r['crops']=json.loads(Path('work/crops127.json').read_text())
inv=Path('source/SP02_CW_10+12_witnesses/codex/B10-09/B10-09_inventory.csv')
rows=[x for x in csv.DictReader(inv.open()) if x['scan']=='127']
ov={x['element']:{'hand':'his hand'} for x in rows if x['hand']=='unknown'}
ov.update({
 '127-E004':{'first_words_or_objects':'hand sigma; following prime typed','hand':'his hand'},
 '127-E007':{'first_words_or_objects':'hand sigma; following prime typed','hand':'his hand'},
 '127-E020':{'first_words_or_objects':'algèbre','hand':'typewriter'},
 '127-E028':{'hand':'typewriter','first_words_or_objects':'C to Mod(k prime), mixed typed line with hand arrow and guide'},
 '127-E036':{'first_words_or_objects':'G(X/M overlap)=L tensor_U X/M overlap','hand':'typewriter'},
 '127-E039':{'first_words_or_objects':'e','hand':'typewriter'},
 '127-E043':{'first_words_or_objects':r"On peut alors écrire G(X)=L\otimes_{\mathbb U'}X', où X'=X tensor_k k prime; with long hand guide"},
 '127-E048':{'first_words_or_objects':r'\unsure{\alpha|\mu}','hand':'his hand'},
 '127-E053':{'first_words_or_objects':'séparer les conditions, commencer par exactitude = platitude; hand sur les U_alpha; enclosing right bracket','hand':'typewriter'},
 '127-E056':{'first_words_or_objects':'qualified c and v-shaped insertion caret','hand':'his hand'},
 '127-E058':{'first_words_or_objects':'si dans C il y a 1 et vee comp.tibles avec (qualified contravariété/contravariants) F, i.e. Delta_U unitaire et U avec antipodisme','hand':'his hand'},
 '127-E059':{'first_words_or_objects':'si dans C il y a 1 et vee comp.tibles avec (qualified contravariété/contravariants) F, i.e. Delta_U unitaire et U avec antipodisme','hand':'his hand'},
 '127-E063':{'first_words_or_objects':'canceled diagonal note: qualified en le dualisant / faisant intervenir; two obscured words; d un qualified antipodisme and terminal U prime','hand':'his hand'},
 '127-E064':{'first_words_or_objects':'three-line canceled diagonal note, all uncertain words retained; terminal U prime qualified','hand':'his hand'},
 '127-E065':{'first_words_or_objects':'three-line canceled diagonal hand note, with terminal symbol qualified','hand':'his hand'},
 '127-E066':{'hand':'typewriter','first_words_or_objects':'mixed long L tensor display; hand hats, subscripts, relations and canceled precursor'},
 '127-E072':{'hand':'his hand','first_words_or_objects':r'\unsure{\simeq|\xrightarrow{\sim}}'},
 '127-E080':{'hand':'his hand','first_words_or_objects':r"[grâce à l'antipodisme:) x tensor qualified U/u -> x tensor (u tensor 1)]; leader"},
 '127-E081':{'hand':'his hand','first_words_or_objects':r"[grâce à l'antipodisme:) x tensor qualified U/u -> x tensor (u tensor 1)]"},
 '127-E087':{'hand':'his hand','first_words_or_objects':lowtext},
 '127-E088':{'hand':'his hand','first_words_or_objects':lowtext},
 '127-E089':{'hand':'his hand','first_words_or_objects':r"(*) La loi de bim. dans L tensor_{qualified U prime/k prime} U prime est donnée par"},
 '127-E090':{'hand':'his hand','first_words_or_objects':'four laws grouped by left brace; final underlined a.'},
 '127-E091':{'hand':'his hand','first_words_or_objects':'four lines of laws; U^o without prime; underlined a followed by dot; Delta_U'}
})
r.r['inventory_overrides']=ov
extra=[
 ('typewriter','text','opening','two typed primes beside hand sigma letters'),
 ('typewriter','text','opening U/A','qualified mixed-case or repeated-capital overprints'),
 ('typewriter','text','structures','live d and e with overlapping apostrophe'),
 ('his hand','drawing','module explanatory insertion','long guide'),
 ('typewriter','deletion','raised beside G','canceled k'),
 ('his hand','drawing','C to Mod insertion','long guide'),
 ('typewriter','text','L=(L_alpha)','opening parenthesis overlapping first L'),
 ('his hand','drawing','à droite insertion','curved guide'),
 ('his hand','text','NB subscript','qualified extra s/S'),
 ('his hand','drawing','On peut alors insertion','long guide'),
 ('typewriter','text','plets cells','r/l and e/a overlaps'),
 ('his hand','drawing','séparer conditions margin','enclosing right bracket'),
 ('typewriter','text','D autre','same-letter repeated D a u t'),
 ('his hand','drawing','Conditions correction','v-shaped insertion caret'),
 ('his hand','drawing','inner parenthetical addition','curved guide beneath comp.tibles/avec'),
 ('his hand','drawing','antipodisme map addition','leader into parenthetical display'),
 ('his hand','drawing','il est insertion','short slanted leader'),
 ('typewriter','deletion','coalgèbre correction','g canceled between coa and l'),
 ('typewriter','text','coalgèbre correction','live l followed by g with grave and then è'),
 ('his hand','drawing','lower margin before dualisons','unassigned small point/stub and crossing strokes'),
 ('his hand','drawing','lower margin','curved bracket and separate thin vertical rule'),
 ('his hand','text','footer final operator','underlined a followed by dot')]
r.r['inventory_extra']=[dict(scan='10:127',sheet_kind='typescript',hand=h,element=f'127-E{i:03d}',kind=k,position=p,first_words_or_objects=t,transcribed='yes') for i,(h,k,p,t) in enumerate(extra,92)]
r.r['inspection_note']='Root alone viewed the whole page and both halves before C/H, all C doubts and the 91-element inventory. All 101 recorded crops were actually viewed, including rotated upright versions of the diagonal notes and close enlargements of every differing, doubtful, marginal, struck and mathematically significant locus. The footertensor/multclose output lost at compaction was repeated before a reading was made. Crossline1 clips part of its targeted diagonal note, so the overlapping crossline2/3, crossmarginwide and cancelend enlargements were used as well. The canceled diagonal note retains explicit uncertainty; its terminal U-prime and the separate dark mark on the lower Commençons line are not conflated. All graphic guide lines, enclosing brackets and the small unassigned lower-margin mark are reproduced. Both agreed and differing words, indices, signs and correction states were checked in the ink. The archival pencil 126 remains a comment only. No OCR, parallel transcription, mathematical checking, context access, ordered audit or freeze occurred.'
r.save('work/record127.json')
print('record127 saved:',len(r.r['changes']),'change rows;',len(r.r['edits']),'edits;',len(r.r['crops']),'viewed crops')
