import sys
sys.path.insert(0,'out/scripts');from work import commit
R=[
(r'une $A$-algèbre, \inserted{de type fini} et soit',r'une $A$-algèbre\unsure{ \inserted{de type fini},|, \inserted{de type fini}} et soit'),
(r'et soit $\operatorname{Mod}(R,C)$',r'et soit $\operatorname{Mod}\unsure{\deleted{f}(|(}R,C)$'),
(r'\unsure{A\'est|C\'est}',r'\unsure{\deleted{C}A|\deleted{A}C}\'est'),
(r'\draw[gray] (-.03,.02) ellipse [x radius=.14,y radius=.49,rotate=-8];',r'\draw[gray] (.17,.50) .. controls (.37,.51) and (.27,.20) .. (.10,.01) .. controls (.02,-.16) and (.05,-.39) .. (-.13,-.47) .. controls (-.30,-.52) and (-.38,-.32) .. (-.23,-.17) .. controls (-.04,.02) and (.01,.13) .. (-.01,.30) .. controls (-.05,.43) and (.04,.50) .. (.17,.50);'),
(r'$R$\unsure{n|.}',r'$R$\unsure{\deleted{n}.|n}'),
(r'\draw[gray] (.08,.04) ellipse [x radius=.15,y radius=.43,rotate=-12];',r'\draw[gray] (.23,.43) .. controls (.45,.42) and (.30,.12) .. (.11,-.01) .. controls (.03,-.16) and (.05,-.29) .. (-.01,-.40) .. controls (-.13,-.35) and (-.24,-.23) .. (-.19,-.08) .. controls (-.14,.16) and (.03,.44) .. (.23,.43);'),
(r'\unsure{\mathbb{C}|\mathbb{A}}',r'\unsure{\deleted{C}|\mathbb{C}|\mathbb{A}}'),
(r'\inserted{sur $S$}',r'\inserted{s\unsure{\deleted{e}u|\deleted{u}e}r $S$}'),
(r'Deux objets \unsure{de} $\unsure{X,Y|X;Y}$ de $C$ \unsure{tels que}',r'Deux objets de $\unsure{X\',Y|X;Y}$ de $C$ tels que'),
(r'\unsure{du|de}',r'd\unsure{\deleted{e}u|\deleted{u}e}'),
(r'(ou $A$-apparentés)',r'(ou $A$-\unsure{\deleted{p}a|\deleted{a}p}pparentés)'),
(r'\unsure{C\'est|D\'est}',r'\unsure{\deleted{D}C|\deleted{C}D}\'est'),
('déquivalence',"d'équivalence")]
# Use ordinary strings where an apostrophe is part of a raw source fragment.
R[2]=(r"\unsure{A'est|C'est}",r"\unsure{\deleted{C}A|\deleted{A}C}'est")
R[8]=(r'Deux objets \unsure{de} $\unsure{X,Y|X;Y}$ de $C$ \unsure{tels que}',r"Deux objets de $\unsure{X',Y|X;Y}$ de $C$ tels que")
R[11]=(r"\unsure{C'est|D'est}",r"\unsure{\deleted{D}C|\deleted{C}D}'est")
L=[]
def a(p,c,h,f,s,v='high',C=False,H=True,k='other',m='no',q=None):
 d=dict(place=p,c=c,h=h,final=f,ink=s,kind=k,confidence=v,against_c=C,against_h=H,marked_in_H=m)
 if q:d['consequential']=q
 L.append(d)
a('de type fini insertion and comma','comma before insertion','insertion before comma','uncertain placement before/after comma','insert_type and cstart: the raised words begin above the last part of algèbre and continue over the comma and et; no caret settles the comma attachment.','low',True,k='insertion or placement')
a('first Mod opening parenthesis','Mod(R,C)','Mod(R,C)','Mod unsure deleted f then opening parenthesis / opening parenthesis','Mod_f: a tall hooked stem and horizontal shoulder overlap the opening parenthesis; both witnesses omit the f-like impression. Its status is not fully secure.','low',True,k='omission')
a('objets de R in c)','R','uncertain R','R','cstart: full upper bowl and oblique lower leg identify R clearly; the semantic suggestion C in H is not adopted.',k='misread symbol or index',m='yes',q='The category is literally described as objets de R; R is clear despite the mathematical expectation.')
a('A/C at start of next sentence','unsure A est/C est','C est','unsure deleted C then A / deleted A then C, followed by apostrophe est','Aest: an A apex, legs and crossbar overlap a rounded C outline. Both letters are present, with typing order uncertain.','low',True,k='deletion state (struck given live or live given struck)')
a('A-linear adjective','li unsure néé/né aire','linéaire','li unsure néé/né aire retained','lineaire and lineaire2: two accents and overlapping n/e bodies are visible in adjacent positions. The number and sequence of impressions remain uncertain.','low',k='misread word')
a('la correction','unsure deleted d then l / deleted l then d, followed by a','la','same uncertainty retained','la_corr: rounded d bowl and tall l stem share one type position, with neither correction order securely recoverable.','low',k='omission')
a('first fibrée category underline','double-underlined C','single-underlined C','double-underlined C','oval1: two separate black horizontal rules lie under C.',k='misread symbol or index')
a('first pencil loop','tilted ellipse','absent','closed bent loop drawn in TikZ','oval1 and cmiddle: upper rounded end lies between comma and R; lower end lies below C, with an inward bend beside the comma. Replaced a regular ellipse by a curved path.','medium',True,k='drawing or diagram')
a('punctuation after first Mod subscript','no comma','comma','no comma','cmiddle: only the lowered A and its raised prime occur after the closing parenthesis; no separate comma precedes the next opening parenthesis.',k='text not on the page')
a('cancelled anneau','anneau','ill{}','deleted anneau','deleted_anneau: all six letter bodies remain visible beneath the typed x row.',k='readable ink left as \\ill{}',m='illegible')
a('cancelled affine phrase closing parenthesis','closing outer parenthesis cancelled; replacement includes closing parenthesis','closing outer parenthesis live outside replacement','old and replacement closing parentheses respectively cancelled and inserted','deleted_affine and cmiddle: the old line ends Spec(A)) under the x row; a separate closing parenthesis follows the interlinear algèbre.',k='deletion state (struck given live or live given struck)')
a('mark after R before En','unsure n/period','period','unsure deleted n then period / n','Rpunct: an n-shaped arch and stem are plainly present; dark lower overtyping can be a period over n. A bare period loses visible ink.','low',True,k='omission')
a('En/Bn','unsure En/Bn','En','unsure En/Bn retained','En: upper square E arms coexist with a rounded lower loop; the superposed impressions do not securely establish the initial letter.','low',k='misread word')
a('second cancelled site','unsure site/sitd','site','unsure site/sitd retained, deleted','site_old: the last impression has a tall d-like hook under the crosses, unlike a securely plain e.','low',k='misread word')
a('second pencil loop','tilted ellipse','absent','bent tapering loop drawn in TikZ','oval2 and cend: rounded upper arc lies above comma/R; lower end tapers below the underlined C and bends inward.','medium',True,k='drawing or diagram')
a('C in final Mod of c)','unsure mathbb C/mathbb A','C','unsure deleted C/mathbb C/mathbb A','ModCA compared with deleted_Cest: a C outline carries crossing diagonals resembling a typed x cancellation; doubling or A overtyping cannot be excluded.','low',True,k='deletion state (struck given live or live given struck)',q='The final category letter in c) may be cancelled, rather than plain live C.')
a('sur insertion overtyping','sur S','sur S','s unsure deleted e then u / deleted u then e r S','sur_u: a closed middle crossbar/eye overlaps the u body. The relative order of the e-like and u-like impressions remains uncertain.','low',True,k='omission')
a('cancelled letter inside localisable','deleted unsure r/i','absent','deleted unsure r/i retained','local_r: an upper rounded shoulder survives under the x, but the dense central impression prevents a secure r/i decision.','low',k='omission')
a('de in cancelled sentence d)','unsure de','absent','deleted de','d_deleted_de and d_deleted: d has a visible tall ascender and lower bowl; e follows before the first X.','medium',True,k='omission')
a('objects in cancelled sentence d)','unsure X,Y/X;Y','X, X prime','unsure X prime,Y / X;Y','d_deleted_XY and d_deleted: after first X a high black mark precedes a lower comma-shaped trace; the following letter has the upper fork of Y. Crossing x strokes leave the prime/separator doubtful.','low',True,k='misread symbol or index')
a('tels que in cancelled sentence d)','unsure tels que','absent','deleted tels que','d_deleted_tels and d_deleted: t, e, tall l, s, then q descender/u/e can be followed through the cancellation.','medium',True,k='omission')
a('cancelled ouvert in d)','ouvert','ill{}','deleted ouvert','deleted_ouvert: rounded o, u, v and e, r shoulder and tall t are legible beneath the crosses.',k='readable ink left as \\ill{}',m='illegible')
a('du/de before champ','unsure du/de','du','d unsure deleted e then u / deleted u then e','du_de: the second position has both an e crossbar/eye and u-shaped outer strokes, as in sur above; order is not recoverable.','low',True,k='deletion state (struck given live or live given struck)')
a('first letter after A-hyphen in e)','apparentés','apparentés','unsure deleted p then a / deleted a then p, followed by pparentés','A_apparentes: a clear p descender and foot lie under the first a; both impressions occupy one position.','low',True,k='omission')
a('C/D in e) C est','unsure C est/D est','C est','unsure deleted D then C / deleted C then D, followed by apostrophe est','Cest: the C curve is overlapped by a distinct vertical stem and round right contour; relative order cannot be established.','low',True,k='deletion state (struck given live or live given struck)')
a('apostrophe in équivalence','déquivalence',"d'équivalence","d'équivalence",'dequivalence: a separate upright black apostrophe is overtyped at the upper-left of é, distinct from its acute accent.','high',True,False,k='omission')
I=[]
def i(k,p,t,h='typewriter'):I.append(dict(kind=k,position=p,text=t,hand=h))
i('text','opening continuation','de la catégorie de ces modules … X prime … sur S … X to n')
i('text','NB following opening','La conclusion de b) … stable par facteurs directs (=karoubienne) … P projectifs … R')
i('deletion','NB after et','en fait P')
i('text','c opening','Soit toujours R une A-algèbre … Mod(R,C) … objets de R … R-linéaire …')
i('insertion','above A-algèbre comma','de type fini; comma attachment uncertain')
i('deletion','overprinted first Mod parenthesis','f-like mark, uncertain')
i('deletion','sentence initial before est','C/A overlapping impressions, order uncertain')
i('text','c linearity and fibration','A-li(néé/né)aire … la catégorie fibrée des Mod …')
i('deletion','before a catégorie fibrée','d/l overlap, order uncertain')
i('drawing','first Mod expression','double-underlined C, R, subscript A prime with bent pencil loop','typewriter and his hand')
i('deletion','after pour A prime','anneau')
i('deletion','following line','affine d’un ouvert affine de S=Spec(A))')
i('insertion','above deleted affine phrase','une A-algèbre)')
i('text','c equivalence and restriction','est équivalente … sections de underlined C munis … R(n/period) … En/Bn … petit site zariskien affine …')
i('deletion','after opération de R','possible n under period')
i('deletion','before petit site','site')
i('deletion','after affine de S','unsure site/sitd')
i('drawing','second Mod expression','underlined C, R with bent pencil loop','typewriter and his hand')
i('text','c conclusion','c’est donc un champ … Mod(R, deleted C/mathbb C/mathbb A) … localisable … si C l’est')
i('deletion','last Mod category letter','possible cancelled C; double-struck C/A alternatives')
i('insertion','above localisable si','s(e/u)r S; pencil insertion guide')
i('deletion','inside inserted sur','e/u overtyping, order uncertain')
i('text','NB on commutativity','Si R est commutatif … même R-linéaire … ne prouve pas … localisable sur R i.e. sur Spec(R) … S=Spec(A)')
i('deletion','NB before live Mod','C est')
i('deletion','NB inside localisable','unsure r/i')
i('deletion','d first sentence','Deux objets de X prime,Y / X;Y de C tels que sont dits')
i('text','d restriction paragraph','Si C est localisable sur A … A prime … C_Aprime … champ associé sur U … restriction d(u/e) champ …')
i('deletion','d after A prime','ouvert')
i('insertion','d above second affine','U')
i('deletion','d before champ','u/e overtyping, order uncertain')
i('text','e full paragraph','Deux objets … apparentés … relation d’équivalence … catégorie A-linéaire … Deuring,')
i('deletion','e after A-hyphen','a/p overtyping, order uncertain')
i('deletion','e initial letter before est','C/D overtyping, order uncertain')
i('deletion','e before A-linéaire','de')
commit(15,82,dict(replace=R,changes=L,inventory=I,sheet_kind='typescript',hand='typewriter',observations='Whole image, both halves and broad bands personally read before and against witnesses. All C doubts, deletions, interlinear additions, mathematical letters and shared suspect overprints enlarged. Two pencil loops redrawn as bent closed paths; no textual meaning inferred from them. The overtyped paragraph bodies remain diplomatic, including munis for sections and objets de R. Archive pencil number 81 is comment only. No context consulted.'))
