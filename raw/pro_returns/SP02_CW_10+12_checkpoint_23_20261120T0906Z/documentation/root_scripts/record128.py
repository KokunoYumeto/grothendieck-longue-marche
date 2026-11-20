from pathlib import Path
import sys,json
sys.path.insert(0,str(Path('SP02_CW_10+12/scripts').resolve()))
from root_record import Record
r=Record('B10-09',10,128);ch=r.change
def hd(s):
 return r'\handwritten{\begin{tikzpicture}[x=.35cm,y=.35cm,baseline=-.2ex]'+s+r'\end{tikzpicture}}'
def guide(n):
 return hd(r'\draw (0,-.3) .. controls (.1,.05) and (.25,.12) .. (.45,.12)--('+str(n)+r',.12) .. controls ('+str(n+.2)+r',.12) and ('+str(n+.3)+r',.3) .. ('+str(n+.3)+r',.5);')
U=r'$\unsure{\rlap{\(\mathrm u\)}U|\mathbb U}$tilisant'
NBword=r'\unsure{Ce\rlap{c}t\rlap{i}t\deleted{e}|Cett\deleted{e}}'
Pr=r'\unsure{\mathrm{P}\rlap{\(\mathrm r\)}\mathrm o\rlap{\(\mathrm r\)}\mathrm o\mathrm{jf}|\mathrm{Poojf}}'
HG=r'\unsure{\rlap{\(G\)}H|H|G|\mathscr{H}|\mathscr{G}}'
HG2=r"{\rlap{\(G\)}H}_{k'}"
arr=r'\handwritten{\unsure{\overset{\sim}{\Longleftarrow}|\xleftarrow{\sim}}}'
co=r'\uline{b\deleted{i}}\deleted{m}\inserted{co}\uline{odules}'
raw=hd(r'\draw[line width=.4pt] (.08,.35)--(.06,.1) .. controls (.05,.02) and (.09,-.02) .. (.13,.01);')
nbtext=r"NB "+NBword+r" équivaut à dire que $B\handwritten{\to}B\otimes_{\unsure{k'|k}}A'$ est hom. d'alg."
nb=r'\begin{tikzpicture}[x=.35cm,y=.35cm,baseline=(n.base)]\node[anchor=north west,align=left,text width=2.7cm] (n) at (0,0) {'+nbtext+r'};\draw (5.0,.6) .. controls (8.3,.8) and (8.7,-.5) .. (8.7,-1.8)--(8.7,-5.5) .. controls (8.6,-6.8) and (7.4,-7.0) .. (5.8,-7.0);\end{tikzpicture}'
prec=r'\begin{tikzpicture}[x=.35cm,y=.35cm,baseline=(n.base)]\node[anchor=north west,align=left] (n) at (0,0) {A préciser};\draw (.2,.5)--(5.6,.5) .. controls (7.2,.5) and (7.5,-.5) .. (5.9,-.8)--(.9,-.8) .. controls (.4,-.8) and (.2,-.5) .. (.2,-.2);\end{tikzpicture}'
right=r'\begin{tikzpicture}[x=.35cm,y=.35cm,baseline=(n.base)]\node[anchor=north west,align=left,text width=5.6cm] (n) at (.6,0) {Sauf erreur, la donnée de\\(*) \uline{équivaut} \uline{à celle de}\\(**)};\draw[line width=.5pt] (0,.2)--(0,-2.9);\draw[line width=.5pt] (.22,.3)--(.22,-2.8);\end{tikzpicture}'
bottom=r'\begin{tikzpicture}[x=.35cm,y=.35cm,baseline=(n.base)]\node[anchor=north west,align=left,text width=3.0cm] (n) at (0,0) {\handwritten{voir si $C$ un groupe i.e. si $\exists$ antipodisme.}};\draw[line width=.2pt] (8.7,2.3) .. controls (8.8,.3) and (8.4,-2.0) .. (8.8,-4.5);\end{tikzpicture}'
# Exact root visual decisions, applied to C only after all whole/half/crop views.
r.edit(r'\unsure{les $B$}',r'les $B$')
r.edit(r'\inserted{\handwritten{$c$}}',r'\inserted{\handwritten{$c$}}'+hd(r'\draw (.15,-.5) .. controls (-.2,-.15) and (.4,.1) .. (.2,.4) .. controls (.1,.55) and (.1,.65) .. (.4,.7);'))
r.edit(r'\uline{\deleted{bi}\inserted{co}modules}',co)
r.edit(r"\unsure{B'|B|A'}\otimes_{\unsure{k'|k}}",r"\unsure{B'|A'}\unsure{\otimes|\Omega}_{k}")
r.edit(r"B\otimes_{k'}B\handwritten{\xleftarrow{\sim}}B\otimes_{k'}A'.\quad\deleted{\text{De}}\n\tag*{(*)}".replace('\\n','\n'),r"\begin{array}{l@{\qquad}l}(*)&B\otimes_{k'}B"+arr+r"B\otimes_{k'}A'.\quad\deleted{\text{\unsure{De|En}}}\end{array}")
r.edit('Utilisant',U)
r.edit(r"B\otimes_{k'}B\handwritten{\longrightarrow}B\n\tag*{(**)}".replace('\\n','\n'),r"\begin{array}{l@{\qquad}l}(**)&B\otimes_{k'}B\handwritten{\longrightarrow}B\end{array}")
r.edit(r"A^{\unsure{\mathrm{L}|'}}",r"A'")
r.edit(r"\margin{NB \unsure{Cette|Cettx} équivaut à dire que $B\handwritten{\to}B\otimes_{\unsure{k'|k}}A'$ est hom. d'alg.}",r'\margin{'+nb+'}')
r.edit(r'\margin{A préciser}',r'\margin{'+prec+'}'+r'\margin{'+hd(r'\draw[line width=.2pt] (0,0) .. controls (.15,-3) and (-.05,-8) .. (.1,-13);')+'}')
r.edit(r'\margin{\handwritten{$\Vert$}Sauf erreur, la donnée de (*) \uline{équivaut à celle de} (**)}',r'\margin{'+right+'}')
r.edit(r'\deleted{\unsure{est adme}\illegible{1}}',r'\deleted{est adme \illegible{1}}')
r.edit(r'\deleted{\unsure{(}}',r'\deleted{(}')
r.edit(r'\deleted{$\unsure{L}\otimes_',r'\deleted{$L\otimes_')
r.edit(r'une\deleted{élément de}',r'un\deleted{e élément de}')
r.edit(r"\inserted{Ceci implique aussi que $B$ est \uline{fidèlement} plat sur $k'$.}",r"\inserted{Ceci implique aussi que $B$ est \uline{fidèlement} plat sur $k'$.}"+guide(12.0)+hd(r'\draw[line width=.5pt] (0,.05) .. controls (1,-.15) and (1.4,.3) .. (1.3,.7);'))
r.edit(r'\inserted{si}',r'\inserted{si}'+hd(r'\draw (0,.5) .. controls (-.2,0) and (.1,-.4) .. (.4,-.2)--(1,-.2) .. controls (1.3,-.2) and (1.1,.2) .. (1.4,.35);'))
r.edit(r'\unsure{dxonnée|donnée}',r'd\deleted{t}onnée')
r.edit(r'\unsure{vérifi|vérifié}','vérifi')
r.edit(r'\unsure{\mathrm{Poojf}|\mathrm{Projf}}',Pr)
r.edit(r'\unsure{asso}','asso')
r.edit(r'\unsure{H|G|\mathscr{H}|\mathscr{G}}',HG)
r.edit(r'\inserted{\handwritten{$P:$}}',r'\inserted{\handwritten{$P:$}}'+hd(r'\draw (0,-.3)--(.4,-.15)--(1.3,.9);'))
r.edit(r"\handwritten{H_{k'}}",r'\handwritten{'+HG2+'}')
r.edit(r'\inserted{\handwritten{et $P$ est \unsure{form.|fibr.} princ. hom.}}',r'\inserted{\handwritten{et $P$ est form.\textsuperscript{'+raw+r'} princ. hom.}}'+guide(7.0))
r.edit(r'\margin{\handwritten{voir si $\unsure{C|G}$ un groupe i.e. si $\exists$ antipodisme.}}',r'\margin{'+bottom+'}')
r.edit('le changement','le changemen'+r'\unsure{t}')
# Every difference and every C doubt is supported by its actual crop(s).
ch('top canceled les B',r'\deleted{\unsure{les B}}',r'\struck{les B}',r'\deleted{les B}','The l upright, e bar, s curves and both B bowls remain visible below the cancellation. C doubt resolved.','lesB','misread word','high',True,False)
ch('c inserted after structure',r'\inserted c','omitted',r'\inserted{\handwritten c}','A small distinct c stands between structure and précédente, above the typed baseline.','cinsert','omission','high',False,True,False,True)
ch('c insertion guide','omitted','omitted','S-shaped hand guide drawn','A separate long curved stroke rises at the c insertion and turns twice; it is not punctuation.','cinsert','drawing or diagram','high',True,True)
ch('bimodules correction and underline',r'\uline{\deleted{bi}\inserted{co}modules}',r'\supplied{co}modules',co,'The cancellation starts after b and crosses i and m. Typed co stands above those two letters. Underlining runs under bi, has a gap at m, then resumes under odules. Both original and added layers are retained without composing a normalized word.','comodule; comoduleclose','deletion state','high',True,True,False,True)
ch('canceled formula initial capital',r"\unsure{B'|B|A'}",r'\ill{}',r"\unsure{B'|A'}",'The upper mark is a separate clear prime. Two bowed remnants favor B, but x cancellation still permits A. The unprimed B alternative is excluded.','cancelA; cancelAfull',r'readable ink left as \ill{}','medium',True,True,True,True)
ch('canceled formula subscript',r"\unsure{k'|k}",r'\ill{}','k','The wide view shows the complete k upright/branches and blank upper-right space; there is no separate prime. C doubt resolved.','cancelAfull',r'readable ink left as \ill{}','high',True,True,True,True)
ch('typed tensor family, first of nine',r'\otimes',r'\ill{}; later \otimes',r'first \unsure{\otimes|\Omega}, later \otimes','All nine signs were enlarged. The high rounded outline and crossing interior strokes favor tensor, but the Omega-like body remains an alternative. First occurrence lies in the canceled formula; later eight use the first candidate without repeated marks.','cancelAfull; firstdisplay; seconddisplay; marginformula; tensorX; cancelL; liveL; tensor2','misread symbol or index','medium',True,True,True,True)
ch('first display arrow',r'\xleftarrow{\sim}',r'\xleftarrow{\sim}',arr,'The left head is clear and two horizontal shafts separate toward the right, with a distinct tilde above. A retraced single shaft remains possible.','firstdisplay; arrowfull','misread symbol or index','medium',True,True,False,True)
ch('two display labels','right tag* labels','left labels','left (*) and (**)','Both parenthesized labels occur at the left of their displayed formulas.','firstlabel; secondlabel','insertion or placement','high',True,False)
ch('canceled word after first display','De','En',r'\deleted{\unsure{De|En}}','A curved right bowl favors D and a lower loop/bar favors e, but the crossing strokes obscure enough of both cells to retain En.','De','misread word','medium',True,True)
ch('position of canceled De/En','after first display on its baseline','before Utilisant','after first display on its baseline','The canceled two-letter word lies to the right of the formula, clearly above the Utilisant baseline.','firstdisplay; De; Utilisant','insertion or placement')
ch('Utilisant initial cell','U','U',U,'Tall U uprights and a low bowl coexist with mid-height u serif traces. A mixed u/U overlap is favored; repeated U is retained as the alternative. The remaining tilisant is ordinary type.','Utilisant','misread word','medium',True,True)
ch('homomorphisme de comodules underline','underlined','italic','underlined','A continuous independent rule spans the phrase beneath its baseline.','homunderline','other')
ch('A-prime in compatible phrase',r"A^{\unsure{\mathrm L|'}}",r"A'",r"A'",'The raised short mark matches the other typed primes. The apparent L foot is the following hyphen on the text baseline. C doubt resolved.','AL; textAprimes','misread symbol or index','high',True,False,False,True)
ch('NB first word',r'\unsure{Cette|Cettx}','Ceci',NBword,'After Ce, the next two cells combine c/t and i/t-like strokes; the final e has a separate crossing cancellation. The normalized whole-word readings lose those layers. The simpler Cett with canceled e remains an alternative.','Cette; marginNB','misread word','medium',True,True)
ch('NB tensor subscript',r"\unsure{k'|k}",'k',r"\unsure{k'|k}",'A high vertical trace beside k is crowded against the following A foot. It may be a prime but cannot be isolated securely, so C doubt is retained.','marginformula; marginSub','misread symbol or index','medium',False,True,False,True)
ch('NB enclosing curve','omitted','omitted','right curved bracket drawn','The line starts above the word, follows the right edge of the note and returns left below d\'alg.','marginNB','drawing or diagram','high',True,True)
ch('A préciser enclosing loop','omitted','omitted','elongated left-open loop drawn','The upper stroke extends over the words, turns around the right edge and returns beneath them to a short upturn.','preciser','drawing or diagram','high',True,True)
ch('thin marginal separator','omitted','omitted','long thin vertical rule drawn','A separate narrow line runs from above NB through the space beside A préciser, farther than either enclosing curve.','verticalrule','drawing or diagram','high',True,True)
ch('Sauf erreur note double rule','inline Vert','omitted','two full-height vertical hand rules','The two parallel strokes span the entire three-line marginal note, rather than one text-height symbol.','rightnote','drawing or diagram','high',True,True)
ch('Sauf erreur underline scopes','one continuous phrase underline','italic phrase','separate underlines under équivaut and à celle de','The first rule ends with équivaut and the second starts under à; a clear gap separates the segments.','rightnote','other','high',True,True)
ch('canceled est adme',r'\unsure{est adme}',r'\ill{}','est adme','The e/s/t and a/d/m/e contours remain distinguishable below typewriter x strokes. C doubt resolved for these two groups.','cancelEst',r'readable ink left as \ill{}','high',True,True,True)
ch('canceled next-line word',r'\illegible{1}',r'\ill{}',r'\illegible{1}','Three compressed letter cells are crossed repeatedly; their remaining stems do not support a whole word. C illegibility is retained, with approximate word count.','cancelNext','other','low',False,False)
ch('deleted opening parenthesis',r'\deleted{\unsure{(}}','omitted',r'\deleted{(}','A left-curving bow is visible under the separate cancellation immediately after the period. C doubt resolved.','delparen','omission','high',True,True)
ch('canceled L formula',r'\unsure L\otimes_U k',r'\ill{}',r'\deleted{L\otimes_{\handwritten U}k}','The L has a tall left stem and a rightward lower foot. The hand U is a rounded cup without a prime, and the typed k is plain. C L doubt resolved; H readable formula recovered.','cancelL',r'readable ink left as \ill{}','medium',True,True,True,True)
ch('live L formula U subscript',r"U'",'U',r"U'",'A detached raised prime follows the subscript U.','liveL','omission','high',False,True,False,True)
ch('live L formula relation',r'\simeq',r'\xrightarrow{\sim}',r'\simeq','The hand sign has a wave and lower straight bar, with no arrowhead at either end.','liveL','misread symbol or index','high',False,True,False,True)
ch('une final e cancellation',r'une\deleted{élément de}',r'une\struck{élément de}',r'un\deleted{e élément de}','The last e of une lies beneath its own x cancellation; un remains live.','element','deletion state','high',True,True)
ch('es t literal spacing','es t','est','es t','A visibly wide blank divides s and t, unlike the adjacent evenly spaced typed letters.','estspace','abbreviation expanded or spelling modernised')
ch('Ceci faithful-flat sentence position','interlinear insertion','margin note','interlinear insertion','The smaller typed line lies below bilatère and above the De même baseline, with a leader tied to the prose.','ceci','insertion or placement')
ch('fidèlement underline','underline','italic','underline','A distinct lower rule covers fidèlement alone.','ceci','other')
ch('Ceci insertion guides','omitted','omitted','long thin leader and heavier right curve drawn','A line begins after the preceding bilatère period and runs under the addition; a second heavier curved stroke rises beside its k-prime ending.','ceci','drawing or diagram','high',True,True)
ch('inserted si guide','omitted','omitted','hooked hand guide drawn','The small typed si is accompanied by a descending loop and lower stroke that turns toward on.','si','drawing or diagram','high',True,True)
ch('donnée correction',r'\unsure{dxonnée|donnée}','donnée',r'd\deleted{t}onnée','Between d and o, a t upright, crossbar and lower curl remain below an x cancellation. C word doubt resolves to the actual letter layers.','dxonnee','deletion state','high',True,True)
ch('canceled vérifi ending',r'\unsure{vérifi|vérifié}','vérifiées','vérifi','The last underlying letter is i with its dot. Later x strokes cross blank positions; no é/e/s body is present. C doubt resolved without completing the word.','cancelQuand; verifi','misread word','high',True,True)
ch('C before avec psi','plain C','underlined C','plain C','The open typed C has no detached rule below it.','Cpsi','misread symbol or index','high',False,True,False,True)
ch('Projf-like target',r'\unsure{\mathrm{Poojf}|\mathrm{Projf}}',r'\operatorname{Projf}',Pr,'After P, each of two cells has a rounded o contour and a separate r stem/shoulder; j and f are clear. Both layers are retained provisionally, with Poojf as the simpler alternative. No correction sequence is inferred.','Projf; projo1; projo2','misread symbol or index','medium',True,True,False,True)
ch('canceled asso',r'\unsure{asso}',r'\ill{}','asso','The a bowl, both s curves and final o remain readable under the x strikes. C doubt resolved.','asso',r'readable ink left as \ill{}','high',True,True,True)
ch('hand bracket before Mais','[','omitted','[','A separate hand vertical stroke with short end turns stands before the typed opening parenthesis.','bracket','omission')
ch('first monoid symbol',r'\unsure{H|G|\mathscr H|\mathscr G}','H',HG,'Two tall H stems and the middle bar coexist with a G-like oval/return. The overlap is the first candidate; single-letter and script alternatives remain because the strokes cross.','H','misread symbol or index','medium',True,True,False,True)
ch('P colon insertion',r'\inserted{P:}','omitted',r'\inserted{\handwritten{P:}}','A hand P and two vertically separated colon marks stand above/before Spec.','Pinsert','omission','high',False,True,False,True)
ch('P colon insertion guide','omitted','omitted','rising diagonal guide drawn','A fine stroke begins below the preceding de and rises across the Spec area toward the inserted P.','Pinsert','drawing or diagram','high',True,True)
ch('later monoid symbol',r"H_{k'}",r"H_{k'}",HG2,'Inside the two H stems is a separate rounded G-like contour with a mid-lower return; the hand k and detached prime are clear. This recurrence uses the first candidate from the earlier qualified symbol.','Hk','misread symbol or index','medium',True,True,False,True)
ch('et P est interline',r'\inserted{et P est \unsure{form.|fibr.} princ. hom.}','omitted','et P est form. princ. hom.','The second letter of form. is a round o, followed by short r/m arches, without i-dot or b ascender. The terminal mark after hom is a period. The whole interline is hand inserted. C abbreviation doubt resolved.','princhom; formclose; formcontext; hompunct','omission','high',True,True,False,True)
ch('short stroke above form period','omitted','omitted','short hooked vertical drawn','A separate short vertical with thick lower hook stands above-right of the period and below the typed r. Its lexical role, possibly an exclamation mark, is unresolved.','formclose; formcontext','drawing or diagram','low',True,True)
ch('principal homogeneous interline guide','omitted','omitted','long lower guide drawn','A thin line starts after the typed à droite comma, runs beneath the interline, then turns up at its right end.','princhom; hompunct','drawing or diagram','high',True,True)
ch('bottom slanted marginal note',r'voir si \unsure{C|G} un groupe i.e. si exists antipodisme.','omitted',r'\handwritten{voir si C un groupe i.e. si $\exists$ antipodisme.}','Rotated upright, the words and three-bar existential sign are readable. The capital is an open C with no inner G crossbar, resolving the C doubt. No est is present after C.','bottommargin; bottomwide; bottomletters','omission','high',True,True,False,True)
ch('bottom margin separator','omitted','omitted','thin vertical separator drawn','The rule extends above the hand note and passes beside/through its rightmost letters; it is distinct from their strokes and is not cancellation.','bottomwide; bottomletters','drawing or diagram','high',True,True)
ch('clipped final changement','changement','changement',r'changemen\unsure{t}','The right image border clips the final cell. A remnant of the t crossbar is visible, but its full stem/body cannot be checked. No continuation is supplied.','finaledge','misread word','medium',True,True)
# Remaining doubts, including graphical ink of unresolved identity.
for a,b,c,d,e in [
 ('canceled formula initial',"B'","A'",'medium','Crossing x strokes obscure the left contour; two bowls favor B, and the prime is clear.'),
 ('nine typed tensor signs',r'\otimes',r'\Omega','medium','First occurrence alone qualified. High rounded body and crossed center recur at all nine separately enlarged loci.'),
 ('first displayed arrow',r'\overset{\sim}{\Longleftarrow}',r'\xleftarrow{\sim}','medium','Two shafts separate at the right, but retracing cannot be excluded.'),
 ('deleted word right of display','De','En','medium','Curved bowl and e bar favor De; cancellation masks the competing strokes.'),
 ('Utilisant first cell',r'\rlap{\(\mathrm u\)}U',r'\mathbb U','medium','Upper and lower serif levels favor mixed-case overlap, without a secure order of strikes.'),
 ('NB first word',r'Ce\rlap{c}t\rlap{i}t\deleted e',r'Cett\deleted e','medium','The c/t and i/t contours are crowded; the last e is certainly canceled.'),
 ('NB tensor subscript',"k'",'k','medium','The possible prime touches the following A foot.'),
 ('canceled word after est adme',r'\illegible{1}','word count approximate','low','Repeated crossing strokes obscure three short underlying cells.'),
 ('Projf-like target',r'\mathrm P\rlap{\(\mathrm r\)}\mathrm o\rlap{\(\mathrm r\)}\mathrm o\mathrm{jf}',r'\mathrm{Poojf}','medium','Both rounded and stem/shoulder contours appear in each of two cells; no normalized category name is imposed.'),
 ('two monoid symbols',r'\rlap{\(G\)}H',r'H; G; \mathscr H; \mathscr G','medium','Overlapping oval/return and H stems are retained. Later recurrence uses the first candidate unmarked.'),
 ('short vertical above form period','raw hooked stroke','possible exclamation mark','low','The mark is separate from the typed line and handwritten word; its function is not settled.'),
 ('last clipped letter','t','','medium','Only part of its upper crossbar survives at the right border.')]:r.doubt(a,b,c,d,e)
r.notation('typed tensor-like family',r'first \unsure{\otimes|\Omega}; eight later \otimes','10:128 canceled top formula1; display(*)2; display(**)1; NB1; tensor on X1; canceled L1; live L1; tensor before donnée1','uncertain')
r.notation('first displayed left relation',arr,'10:128 (*)','uncertain')
r.notation('live L relation',r'\simeq','10:128 L tensor_U-prime k-prime simeq k-prime')
r.notation('Utilisant mixed case',U,'10:128 first prose after (*)','uncertain')
r.notation('Projf-like overprinted cells',Pr,'10:128 symmetry target','uncertain')
r.notation('H/G overlapping handwritten capitals',HG+'; '+HG2,'10:128 affine monoid and action below','uncertain')
r.notation('hand structure signs',r'\Delta;\Delta;\phi;\Delta;\psi','10:128 unit/associative/commutative paragraphs; individually checked')
r.notation('ordinary typed capitals',r'B,A,U,X,L,C,F,P','10:128 all occurrences separately inspected; no same-letter repeat inferred from darkness')
r.r['abbreviations']=[dict(abbreviation=a,expansion=b,attestations='10:128 '+c) for a,b,c in [('NB','nota bene','left margin and main paragraph'),('i.e.','id est','main text and bottom margin'),('sss','si et seulement si','associative and symmetry clauses'),('hom.','homomorphisme; or homogène in principal-space phrase','NB and final interline'),('alg.','algèbre','NB'),('form.','forme (expansion tentative)','final interline; the written abbreviation itself is clear'),('princ.','principal','final interline')]]
# Correct inventory descriptions explicitly; include every omitted physical element.
o={}
def ov(i,s,**kw):o[f'128-E{i:03d}']=dict(first_words_or_objects=s,**kw)
ov(5,r'\deleted{les B}');ov(10,r'\deleted{i} and \deleted{m}; b remains live');ov(11,'co typed above canceled i,m');ov(12,r"\deleted{\unsure{B'|A'}\unsure{\otimes|\Omega}_k}")
ov(13,r"left (*) B tensor_k' B, qualified left double arrow with tilde, B tensor_k' A'; deleted De/En")
ov(14,arr);ov(15,r'\deleted{\unsure{De|En}}');ov(16,r"left (**) B tensor_k' B hand arrow B")
ov(18,nbtext);ov(20,'A préciser with enclosing loop');ov(21,'Sauf erreur, la donnée de (*) with two distinct underline segments and (**)');ov(22,'two full-height parallel vertical hand rules',kind='drawing')
ov(25,r'\deleted{est adme \illegible{1}}');ov(26,r'\deleted{(}');ov(27,r'\deleted{L\otimes_{\handwritten U}k}');ov(30,r'\deleted{e élément de}')
ov(37,'Quand les deux conditions sont vérifi');ov(40,r'\deleted{asso}');ov(42,HG);ov(45,HG2)
for i in (46,47):ov(i,'et P est form. [short hooked stroke] princ. hom.')
for i in (48,49):ov(i,r'voir si C un groupe i.e. si $\exists$ antipodisme.')
r.r['inventory_overrides']=o
extras=[
 ('c hand insertion guide','drawing','top c insertion','his hand'),
 ('two separated underlines beneath corrected bimodules','drawing','top correction','typewriter'),
 ('NB c/t and i/t overlap, final e canceled','deletion','left NB first word','typewriter'),
 ('NB right curved bracket','drawing','upper left margin','his hand'),
 ('A préciser left-open enclosing loop','drawing','left margin','his hand'),
 ('long thin separator behind upper notes','drawing','left margin','unnamed hand'),
 ('separate équivaut and à celle de underlines','drawing','right marginal note','typewriter'),
 ('Utilisant u/U overlapping capital cell','text','after first display','typewriter'),
 ('long Ceci insertion leader','drawing','middle interline','his hand'),
 ('heavier right curve beside Ceci ending','drawing','middle interline right','his hand'),
 ('si insertion hooked guide','drawing','above on a pour','his hand'),
 ('deleted t inside d-t-onnée','deletion','after pour tensor une','typewriter'),
 ('two r/o overlapping cells in Projf-like target','text','symmetry target','typewriter'),
 ('P colon rising insertion leader','drawing','above Spec','his hand'),
 ('short hooked vertical above-right of form period','drawing','final hand interline','his hand'),
 ('long lower guide for et P est form. princ. hom.','drawing','final hand interline','his hand'),
 ('thin separator beside bottom slanted note','drawing','lower left margin','unnamed hand'),
 ('final clipped t in changement','text','right edge of last line','typewriter')]
for i,(s,k,p,h) in enumerate(extras,1):r.r['inventory_extra'].append(dict(scan='10:128',sheet_kind='typescript',hand=h,element=f'128-R{i:03d}',kind=k,position=p,first_words_or_objects=s,transcribed='yes'))
r.r['crops']=json.loads(Path('work/crops128.json').read_text())
r.r['inspection_note']='Root alone viewed the whole image, both halves, C/H, all C doubts/inventory, then all69 actual enlarged crop views. Bottom margin was rotated -22 degrees and final hand interline -2 degrees. Every difference, deleted/slanted/marginal locus and mathematical sign was enlarged. All17 original C uncertainty/illegibility loci are explicitly resolved or retained with ink reasons. Archive127 was separately enlarged and remains only an archive comment. No OCR, parallel reading, context opening or mathematical check occurred.'
r.save('work/record128.json')
