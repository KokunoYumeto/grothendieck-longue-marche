from pathlib import Path
import sys,json
sys.path.insert(0,str(Path('SP02_CW_10+12/scripts').resolve()))
from root_record import Record
r=Record('B10-09',10,125);ch=r.change
# The lower-corner archival folio stays in C's comment, as base PROMPT rule 4 requires.
def handdraw(body):
 return r'\handwritten{\begin{tikzpicture}[x=.4cm,y=.4cm,baseline=-.2ex]'+body+r'\end{tikzpicture}}'
def guide(length):
 return handdraw(r'\draw (0,-.35) .. controls (-.08,.0) and (.13,.18) .. (.40,.20)--('+str(length)+r',.18) .. controls ('+format(length+.20,'.2f')+r',.19) and ('+format(length+.30,'.2f')+r',.24) .. ('+format(length+.29,'.2f')+r',.46);')
gfun=guide(4.6);ggrad=guide(3.9);gavec=guide(4.7)
gnon=handdraw(r'\draw (0,-.40) .. controls (.18,-.12) and (.28,.02) .. (.54,.07)--(2.70,.38) .. controls (2.86,.40) and (2.99,.45) .. (2.96,.63);')
small=r'\begin{tikzpicture}[x=.4cm,y=.4cm,baseline=-.2ex]\draw (.12,.45) .. controls (-.04,.23) and (.01,.24) .. (.20,.28) .. controls (.34,.36) and (.36,.34) .. (.18,.12) .. controls (.10,-.03) and (.21,-.10) .. (.33,-.10);\draw (.02,.27)--(.35,.38);\draw (.18,.17)--(.11,-.11)--(.32,-.09);\end{tikzpicture}'
divider=handdraw(r'\draw (.08,-.75) .. controls (.04,-.20) and (.25,.50) .. (.32,.74);\draw (.28,-.72) .. controls (.24,-.10) and (.36,.40) .. (.47,.78);\fill (0,.34) circle (.025);')
ginit=r'\unsure{\rlap{\(\mathrm E\)}G|\mathbb{G}|G|E}'
cat=r'\unsure{\rlap{\(\mathrm N\)}C|\handwritten{\mathfrak{C}}|\handwritten{\mathscr{C}}|\mathbb{C}}'
sant=r'factori\unsure{s\rlap{n}ant|s\rlap{r}ant|s\rlap{e}ant}'
soi=r'so\rlap{n}i\unsure{\rlap{e}\rlap{t}n|\rlap{t}n}\rlap{t}nt'
args=r'\unsure{\rlap{r}a\rlap{a}r|$\mathbb{a}\mathbb{r}$}guments'
multi=r'm\unsure{\rlap{u}l|\rlap{b}l|b}tigradué'
pp=r'\unsure{\rlap{r}p|p|$\mathbb{p}$}\rlap{r}p\unsure{\rlap{u}o|o}uv\rlap{q}ant'
r.edit('semi-simples, on','semi-simples, '+r'\rlap{,}on')
r.edit(r'\deleted{\unsure{I}}',r'\deleted{I}')
r.edit(r'\unsure{présumée|pvrésumée}',r'\rlap{a}p\rlap{v}résumée')
r.edit(r'1º)\handwritten{\deleted{\unsure{(}}}',r'1º\rlap{)}\handwritten{)}\handwritten{\unsure{'+small+r'|\deleted{(}}}')
r.edit(r'\unsure{\mathbb{G}|G|E}',ginit)
r.edit(r'\handwritten{;}\quad',divider+r'\quad')
r.edit(r'\text{)},',r'\text{)}\handwritten{,}')
r.edit('factorisant',sant)
r.edit(r'\deleted{$M$. \unsure{On impose}}',r'\deleted{$M$. Ceci impose}')
r.edit(r'\inserted{des foncteurs sur $M$. On voudra}',r'\inserted{des foncteurs sur $M$. On voudra'+gfun+'}')
r.edit(r'\unsure{soinnt|sointnt|soient}',soi)
r.edit(r'\inserted{\handwritten{(non tordus)}}',r'\inserted{\handwritten{(non tordus)}'+gnon+'}')
r.edit(r'\inserted{\handwritten{car}}',r'\inserted{\handwritten{\unsure{Car|car}}}')
r.edit(r'\inserted{la catégorie graduée $M$}',r'\inserted{la catégorie graduée $M$'+ggrad+'}')
r.edit(r'\unsure{arguments}',args)
r.edit(r'\handwritten{\unsure{\mathscr{C}|\mathfrak{C}|\mathbb{C}}}',cat)
r.edit(r'\inserted{avec $k=\mathrm{End}(\underline{1})$ un corps donné.}',r'\inserted{avec $k=\mathrm{End}(\underline{1})$ un corps donné.'+gavec+'}')
r.edit(r'\unsure{tordu|toodu}',r't\rlap{r}o\rlap{o}rdu')
r.edit('mltigradué',multi)
r.edit(r'\unsure{ggnéral|ggénéral|général}',r'g\rlap{g}énéral')
r.edit('ppuvant',pp)
r.edit(r"qu'\unsure{ip|il}",r"qu'i\rlap{p}l")
ch('first on','on','on',r'\rlap{,}on','The o bowl contains a separate low comma head and hooked descending tail. The next n is ordinary.','on','misread word','medium',True,True)
ch('after filtrée','comma','period','comma','The mark has a rounded head and a clear tail below the baseline.','filtrecomma','other','high',False,True)
ch('canceled I',r'\deleted{\unsure{I}}','omitted',r'\deleted{I}','An upright capital stem with upper and lower horizontal serifs remains beneath the diagonal x. C doubt resolved.','I','omission','high',True,True)
ch('category V in Si V','plain V','underlined V','plain V','The two typed oblique arms meet at a low point, with no detached underline.','V1','misread symbol or index','high',False,True,False,True)
ch('first category M','plain M','underlined M','plain M','The M has ordinary typewriter stems and a low central junction; no independent lower rule is present.','M1','misread symbol or index','high',False,True,False,True)
ch('présumée opening',r'\unsure{présumée|pvrésumée}','présumée',r'\rlap{a}p\rlap{v}résumée','The first cell has a p descender and an a lower bowl; the second contains the r upright/shoulder and two v arms. These are overlapping cells, not an extra sequential v. The following accented é and sumée are legible.','presumee; presumee-first','misread word','high',True,True)
ch('parenthesis after first 1º','ordinary closing parenthesis','ordinary closing parenthesis',r'\rlap{)}\handwritten{)}','A short black typed closing curve is retraced by a longer blue hand curve extending above and below it.','onepar; par-small','other','high',True,True)
ch('small canceled mark after parenthesis',r'\handwritten{\deleted{\unsure{(}}}','omitted','qualified raw drawing; canceled opening parenthesis alternative','The small blue mark has a short rising curve, crossed horizontal/oblique passes and a lower angular return. These strokes do not securely resolve the canceled underlying character; the shape is drawn.','onepar; par-small','omission','low',True,True)
ch('canceled capital after foncteur',r'\deleted{\unsure{$V$|$Y$}}','omitted',r'\deleted{\unsure{$V$|$Y$}}','Two upper diagonal arms and a low point favor V. Crossing x strokes obscure the lower center, so a Y stem cannot be excluded. C doubt retained.','Vdelete','omission','medium',False,True)
ch('canceled de','deleted de','omitted','deleted de','Both d and e remain readable under separate typewriter x strikes.','de','omission','high',False,True)
ch('V in displayed h','plain V','underlined V','plain V','The capital has no lower rule. The separate long handwritten arrow points right.','hformula','misread symbol or index','high',False,True,False,True)
ch('first Grad initial',r'\unsure{\mathbb{G}|G|E}','ordinary G',ginit,'A straight left stem and upper/lower serif traces coexist with a curved G body and inward return. An E/G overprint is favored, while repeated G and single-letter alternatives remain qualified. This is not inferred from the functor name.','Ginit; hformula; Grad2','misread symbol or index','low',True,True,False,True)
ch('M in displayed h','plain M','underlined M','plain M','The ordinary M feet are visible without a detached line underneath.','hformula','misread symbol or index','high',False,True,False,True)
ch('mark after displayed h formula','hand semicolon','omitted','two curved strokes and upper-left dot, drawn','The mark comprises two long near-parallel hand strokes, each leaning right at the top, with a small detached dot at the upper left; it is not a conventional semicolon.','semi','drawing or diagram','high',True,True)
ch('M in display explanatory parenthesis','plain M','underlined M','plain M','The second Grad has an ordinary single G and an M without an underline; both closing parentheses survive.','Grad2','misread symbol or index','high',False,True,False,True)
ch('display terminal comma','unmarked comma','unmarked comma','handwritten comma','The final comma is a long continuous descending hand stroke with a leftward lower hook, unlike the nearby typewriter commas.','Grad2-comma','other','medium',True,True)
ch('V in cohomological functors clause','plain V','underlined V','plain V','The typed V has no detached lower line.','V2','misread symbol or index','high',False,True,False,True)
ch('factorisant ending','factorisant','factorisent',sant,'The line ends factori and the next begins sant. The a cell also has an upright with top and bottom serif traces, favoring n/a or r/a overlap; an e/a alternative is retained. The a lower bowl is visible, so H\'s unqualified sent is not used.','factoriright; sant; sant-a','misread word','low',True,True)
ch('M after factorisant par','deleted M.','live underlined M.','deleted plain M.','The M and its period are covered by x strikes. There is no separate underline.','cancelMon','deletion state','high',False,True,False,True)
ch('canceled words following M',r'\unsure{On impose}','Ceci impose','Ceci impose, canceled','Four separate letter cells C-e-c-i precede impose. The open capital C and the dot of the fourth i remain visible under the strikes; the p descender in impose is also visible. C doubt resolved in favor of H\'s words.','cancelMon; Ceci','misread word','high',True,False)
ch('full typed replacement','des foncteurs sur M. On voudra','On voudra only','des foncteurs sur M. On voudra, inserted','The addition contains all five groups before que, including the plain M and its full stop. H omits des foncteurs sur M.','insertfoncs','omission','high',False,True,False,True)
ch('guide for typed replacement','omitted','omitted','curved guide drawn beneath replacement','A rising left bend leaves the canceled phrase and runs below the addition to an upward curl at the far right.','insertfoncs','drawing or diagram','high',True,True)
ch('M after obtenus sur','plain M','underlined M','plain M','The typed M has separate ordinary feet and no underline.','M2','misread symbol or index','high',False,True,False,True)
ch('soinnt complex overprint',r'\unsure{soinnt|sointnt|soient}','soient',soi,'After so, an i dot/stem overlaps an n-shaped body; the next cell has n/t outlines and a possible e middle bar; the following n cell also carries a t ascender and crossbar, followed by an ordinary final t. The dense middle cell remains explicitly uncertain.','soinnt; soi-middle','misread word','low',True,True)
ch('underline inside canceled tordus seulement','underline on tordus','no underline','underline on tordus, within deletion','The independent lower rule stops after the six letters of tordus, while x strikes continue through seulement.','torduscancel','other','high',False,True)
ch('non tordus placement guide','omitted','omitted','curved guide drawn','The blue line rises after véritables, passes below the parenthesized hand addition and curls upward at the right. The slightly slanted words were also inspected rotated upright.','nontordus; nontordus-upright','drawing or diagram','high',True,True)
ch('canceled typed car','deleted car','omitted','deleted typed car','The c/a/r cells remain beneath x strokes and a hand cancellation, below the replacement.','car; car-upright','omission','high',False,True)
ch('hand replacement car case','car','car',r'\handwritten{\unsure{Car|car}}','The initial open curve is approximately twice the height of a and r, favoring capital C; variable hand letter height leaves lower-case c possible. The hand phrase was rotated upright.','car; car-upright','misread word','medium',True,True)
ch('M after symétrie de Koko','plain M','underlined M','plain M','The M within this third Grad has no independent underline.','Grad3','misread symbol or index','high',False,True,False,True)
ch('torsion quotation marks','paired double quotes','guillemets','paired double quotes','Two separate high vertical quote strokes occur on each side of torsion, with a full stop after the closing pair.','torsionquote','other','high',False,True)
ch('géométrique quotation marks','paired double quotes','guillemets','paired double quotes','The word is enclosed by pairs of high strokes, not angular guillemets.','geoquote','other','high',False,True)
ch('M in deleted Grad','plain M','underlined M','plain M, canceled','The M is crossed with x strokes like the rest of Grad(M), without a detached lower rule.','Graddel','misread symbol or index','high',False,True,False,True)
ch('M in la catégorie graduée insertion','plain M','underlined M','plain M','The M has ordinary stems and feet. The long curved line below belongs to the guide for the full insertion, rather than an underline on M.','gradedinsert','misread symbol or index','high',False,True,False,True)
ch('guide for la catégorie graduée M','omitted','omitted','curved guide drawn','The guide rises beside the canceled Grad, runs under the entire inserted phrase and curls upward at the right.','Graddel; gradedinsert','drawing or diagram','high',True,True)
ch('arguments initial cells',r'\unsure{arguments}','arguments',args,'The first two cells are heavily overprinted. A left serif and upright overlap the a bowl in the first, and an a-like curved right foot survives under the r in the second. Repeated-strike a/r remain an alternative because the internal strokes are dense; guments is clear.','args; args-first','misread word','low',True,True)
ch('category symbol in paragraph 11',r'\handwritten{\unsure{\mathscr{C}|\mathfrak{C}|\mathbb{C}}}','underlined C',cat,'The glyph has a C-like outer curve, a long straight upper serif and a diagonal internal stem resembling a typed N/C overlap. The cursive/fraktur and doubled-C alternatives remain qualified. No detached underline is present; C\'s hand attribution is not secure.','C; C-context','misread symbol or index','low',True,True,False,True)
ch('guide for avec k=End(1)','omitted','omitted','curved guide drawn','A hand line rises after the first paragraph-11 comma, runs beneath the added typed sentence and curls at its right. The underline directly beneath 1 is distinct and retained.','avecguide; kEnd','drawing or diagram','high',True,True)
ch('first tordu',r'\unsure{tordu|toodu}','tordu',r't\rlap{r}o\rlap{o}rdu','The second cell has an o oval with an r stem/foot, and the third has an r shoulder/stem and a complete low o curve. The physical overlapping letters are retained.','tordu','misread word','high',True,True)
ch('mltigradué opening','mltigradué','multigradué',multi,'The second cell has a tall l stem and an additional low bowl with a right upright, favoring u/l overlap. A b-like body cannot be excluded. There is only one occupied cell between m and t, not H\'s two separate u/l cells.','multi; multi-l','misread word','low',True,True)
ch('général opening',r'\unsure{ggnéral|ggénéral|général}','général',r'g\rlap{g}énéral','Two g descender loops occupy adjacent positions. In the second position the acute accent and an e body overlap the g; néral follows. The first two cells cannot be reduced to a plain gé sequence.','general','misread word','medium',True,True)
ch('supposer emphasis','underlined','italic','underlined','A continuous blue line runs beneath the typed word.','supp','other','high',False,True)
ch('ppuvant cluster','ppuvant','prouvant',pp,'Eight occupied positions are visible. The first two have p descenders and extra baseline-foot/shoulder traces favoring r/p overlaps; single or repeated p remain possible at the first, with the same selected reading used at the second. The next closed o-like body has u-like side/foot traces, and the a later in the word shares a cell with a q descender. The uncertain layers are not regularized to a grammatical word.','ppuvant; pp-prefix; pp-ending','misread word','low',True,True)
ch('qu\'ip / qu\'il',r"qu'\unsure{ip|il}","qu'il",r"qu'i\rlap{p}l",'The final cell has both the long l ascender with top serif and a p bowl/descender; these occupy the same cell. C\'s letter choice is replaced by the visible overlap.','quip','misread word','high',True,True)
# Remaining doubts are localized physical uncertainties, not grammatical emendations.
r.doubt('first parenthesis, small adjacent canceled mark','raw drawn strokes','canceled opening parenthesis','low','The crossing passes obscure the underlying curved character; raw geometry is retained.')
r.doubt('after un foncteur','canceled V','canceled Y','medium','The cancellation hides the possible lower Y stem.')
r.doubt('first displayed Grad initial',r'\rlap{\(\mathrm E\)}G',r'\mathbb G; G; E','low','Straight serif-bearing traces and a G curve coexist; layer identification remains uncertain.')
r.doubt('factorisant, a cell',r's\rlap{n}ant',r's\rlap{r}ant; s\rlap{e}ant','low','The a is legible; the extra serif-bearing body is not uniquely separable.')
r.doubt('soinnt middle cluster',r'so\rlap{n}i\rlap{e}\rlap{t}n\rlap{t}nt',r'so\rlap{n}i\rlap{t}n\rlap{t}nt','low','An e-like middle bar may belong to the overlapping n/t strokes; the separate final t remains.')
r.doubt('hand car replacement','Car','car','medium','Tall initial curve favors a capital, but hand letter size varies.')
r.doubt('arguments first two cells',r'\rlap{r}a\rlap{a}r',r'\mathbb a\mathbb r','low','Opposite-letter overlaps are favored by the left serif and curved foot, with repeated strikes still possible.')
r.doubt('paragraph 11 category symbol',r'\rlap{\(\mathrm N\)}C',r'hand \mathfrak C; hand \mathscr C; \mathbb C','low','The straight top and diagonal internal stroke favor typed overlapping capitals; alphabet and production method remain uncertain.')
r.doubt('mltigradué second cell',r'\rlap{u}l',r'\rlap{b}l; b','low','A tall stem and a low closed body coexist; the latter may be u or b.')
r.doubt('ppuvant first two cells',r'\rlap{r}p at both positions',r'p; \mathbb p','low','The baseline-foot/shoulder traces suggest r over p but cannot be separated with certainty. First occurrence qualified, second uses the same first candidate.')
r.doubt('ppuvant third cell',r'\rlap{u}o','o','low','The closed oval and extra side/foot traces favor overlap, but a damaged single impression remains possible.')
r.notation('ordinary typed V and M','V, M without underline','10:125 V in opening/display/body; M in opening, display twice, canceled phrase, replacement, body, Grad twice and graded replacement')
r.notation('overworked initial of displayed Grad',ginit,'10:125 first h display','uncertain')
r.notation('paragraph-11 category glyph',cat,'10:125 des catégories before munies','uncertain')
r.notation('sign of graded interchange',r'(-1)^{ij}','10:125 paragraph 10 continuation; typed raised i and j, no separator')
r.notation('ground field and unit',r'k=\mathrm{End}(\underline{1})','10:125 paragraph-11 insertion; all three k letters ordinary, unit explicitly underlined')
r.notation('typed versus drawn punctuation','typed comma after filtrée; drawn double stroke after h; hand comma after display','10:125 opening and display')
r.notation('overprinted p/r cells',r'first \unsure{\rlap{r}p|p|$\mathbb p$}; later \rlap{r}p','10:125 ppuvant opening two adjacent cells','uncertain')
r.notation('archive pencil folio','comment only','10:125 lower-left pencil 124; base PROMPT rule 4')
r.r['abbreviations']=[{'abbreviation':'i.e.','expansion':'id est','attestations':'10:125 second paragraph'}]
r.r['crops']=json.loads(Path('work/crops125.json').read_text())
r.r['inventory_overrides']={
 '125-E001':{'first_words_or_objects':r'semi-simples, \rlap{,}on a une catégorie; complete first text block'},
 '125-E002':{'first_words_or_objects':'I'},
 '125-E003':{'hand':'his hand','kind':'drawing','first_words_or_objects':'small crossed curved mark; raw drawing with canceled-parenthesis alternative'},
 '125-E004':{'hand':'his hand','first_words_or_objects':'cancellation within small curved mark; underlying opening parenthesis uncertain'},
 '125-E007':{'first_words_or_objects':'h:V to overworked Grad(M); double curved hand mark; parenthetic Koko structure and hand comma'},
 '125-E008':{'hand':'his hand','first_words_or_objects':r'\longrightarrow'},
 '125-E009':{'hand':'his hand','kind':'drawing','first_words_or_objects':'two tall near-parallel curves and a small upper-left point'},
 '125-E010':{'first_words_or_objects':'M. Ceci impose'},
 '125-E017':{'hand':'his hand','first_words_or_objects':r'\unsure{Car|car}'},
 '125-E018':{'hand':'his hand','first_words_or_objects':r'\unsure{Car|car}'},
 '125-E022':{'first_words_or_objects':'11) Bien sûr; complete paragraph through extension convenable de k'},
 '125-E023':{'hand':'unnamed hand','kind':'text','first_words_or_objects':'qualified N/C overlap; cursive/fraktur/doubled-C alternatives; production method unresolved'}
}
for n in [14,15]:r.r['inventory_overrides'].setdefault(f'125-E{n:03d}',{})['hand']='his hand'
extras=[
 ('over-on','text','line 1','comma/o overlap in on','typewriter'),
 ('over-presumee','text','line 3','a/p and v/r overlapping cells in présumée','typewriter'),
 ('hand-parenthesis','insertion','line 4 after 1º','long hand closing curve over typed parenthesis','his hand'),
 ('hand-final-comma','text','display right end','long hand comma','his hand'),
 ('over-sant','text','line 7 beginning','a overlapped by n/r/e-like body in factorisant','typewriter'),
 ('guide-functors','drawing','above line 7','curved guide below des foncteurs sur M. On voudra','his hand'),
 ('over-soinnt','text','line 7 end','three overlapping letter cells after so, before final t','typewriter'),
 ('guide-nontordus','drawing','above line 8 right','curved guide for (non tordus)','his hand'),
 ('guide-graded','drawing','above line 14','curved guide below la catégorie graduée M','his hand'),
 ('over-arguments','text','line 15','qualified a/r and r/a overlaps in arguments','typewriter'),
 ('guide-avec','drawing','above paragraph 11 third line','curved guide for avec k=End(underlined 1) un corps donné.','his hand'),
 ('over-tordu','text','paragraph 11 first fibre tordu','r/o and o/r overlaps','typewriter'),
 ('over-multi','text','paragraph 11 parenthesis','qualified u/l or b-like overlap in mltigradué','typewriter'),
 ('over-general','text','paragraph 11 théorème de structure','second g overlapped with é in ggénéral','typewriter'),
 ('over-ppuvant','text','penultimate line','qualified p/r and o/u layers; a/q overlap in eight-cell word','typewriter'),
 ('over-quip','text','last line','p/l overlap after qu\'i','typewriter'),
 ('archive-folio','text','lower-left corner','124; archival folio retained as comment only','unnamed hand')]
for suffix,kind,pos,words,hand in extras:r.r['inventory_extra'].append(dict(scan='10:125',sheet_kind='typescript',hand=hand,element='125-'+suffix,kind=kind,position=pos,first_words_or_objects=words,transcribed='yes'))
r.r['inspection_note']='Root alone viewed the whole and both supplied halves before C/H, then checked every agreed word and sign and all differences in the ink. All 65 recorded crops were actually viewed; the truncated insertfoncs/fibrescancel/M2 batch was repeated individually, and slanted hand additions were rotated upright. All twelve C doubt loci were resolved or explicitly retained with reasons. The display, every category letter, k/End/unit, sign (-1)^ij, i/j, cancellations and all four insertion guides were enlarged. Unusual spellings symmétrie, canulée, débarassé and the visible factorisant ending were checked without grammatical correction. The right-edge e of catégorie is partly occluded but its bowl and crossbar remain identifiable. Dense de at a later line start has insufficient positive evidence for a second letter and remains plain; ordinary M letters likewise are not called repeated strikes on darkness alone. Archive pencil 124 stays a comment. No context, second-pass audit or mathematical checking has occurred.'
r.save('work/record125.json')
