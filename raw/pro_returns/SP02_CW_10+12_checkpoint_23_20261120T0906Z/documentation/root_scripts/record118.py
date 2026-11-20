from pathlib import Path
import sys,json
sys.path.insert(0,str(Path('SP02_CW_10+12/scripts').resolve()))
from root_record import Record
r=Record('B10-08',10,118);ch=r.change
r.edit(r'\scanpage{118}',r'\scanpage{118}'+'\n'+r'\mspage{117}')
r.edit('% archive sheet number: 117','')
r.edit(r'$\otimes$-\uline{catégories}',r'$\unsure{\otimes|\Omega}$-\uline{catégories}')
r.edit(r'\deleted{(ne dépend pas de la structure additive)}',r'\deleted{(ne dépend pas de la structure additive),}')
r.edit(r'\mathrm{id}_{X\otimes X}',r'\mathrm{id}_{\unsure{\rlap{Y}X|X}\otimes X}')
r.edit(r"\handwritten{: axiome de l'hexagone}",r"\handwritten{; axiome de l'hexagone}")
r.edit(r'\draw (-.6,.05) .. controls (-.4,-.45) and (.75,-.4) .. (.85,0) .. controls (.95,.6) and (1.5,.7) .. (1.85,.3);',r'''\draw (-.6,.05) .. controls (-.4,-.45) and (.75,-.4) .. (.85,0) .. controls (.95,.6) and (1.5,.7) .. (1.85,.3);
\draw[line width=.15pt] (1.12,.57)--(1.48,.28);
\draw[line width=.15pt] (.03,-.49) .. controls (.29,-.63) and (.56,-.52) .. (.69,-.43);''')
r.edit('(donc par b','(donc, par b')
r.edit('\\[\nu(\\underline{1})=v(\\underline{1})',r'''\[
\makebox[0pt][r]{\begin{tikzpicture}[x=1em,y=1em]\fill (0,0) circle (.045);\end{tikzpicture}\hspace{3em}}
u(\underline{1})=v(\underline{1})''')
r.edit(r'''\begin{tikzpicture}
\node[draw,rounded corners,align=left] {de plus on veut};
\end{tikzpicture}''',r'''\begin{tikzpicture}[x=1cm,y=1cm]
\node[align=left] at (0,0) {de plus on veut};
\draw (-1.23,-.23) .. controls (-1.8,.03) and (-1.62,.62) .. (-1.16,.65) -- (1.22,.81) .. controls (1.61,.83) and (1.77,.08) .. (1.53,-.03) -- (-.82,-.25) .. controls (-1.3,-.35) and (-1.5,-.76) .. (-1.25,-1.09);
\end{tikzpicture}''')
r.edit(r'$\unsure{\varphi|\phi}$',r'$\phi$')
r.edit(r'$X,Y$ \unsure{ou} $Z$ est',r'$X,Y$ \unsure{,-|ou} $Z$ \unsure{est}')
r.edit(r'$\unsure{\psi|\mu}$ quand $X$ \unsure{ou}',r'$\mu$ quand $X$ \unsure{,-|ou}')
r.edit(r"\unsure{d'ensemble|d'ensembles}",'éventuelle')
r.edit(r'\unsure{relation|relations}','relation')
r.edit(r'$X^\vee\otimes Y$',r'$\check{X}\otimes Y$')
r.edit('sont indépendant de fait',r'sont indépendant d\unsure{\rlap{u}e|e} fait')
r.edit(r"\underline{1}',u',\inserted{v'}",r"\underline{1}',u',\inserted{v'\handwritten{\begin{tikzpicture}[x=.4cm,y=.4cm,baseline=-.2ex]\draw (0,-.2) .. controls (-.28,.4) and (.1,.65) .. (.53,1.01);\end{tikzpicture}}}")
r.edit(' , compatible en un sens',r' , compati\unsure{\rlap{v}b|b}le en un sens')
r.edit(r"\unsure{v'(1)|v(1)}",r"v'(\underline{1})")
r.edit(r"\unsure{u(\underline{1}')|\underline{1}\otimes u'}",r"\unsure{\rlap{\(\underline{1}\otimes u'\)}u(\underline{1}')|u(\underline{1}')}")
r.edit(r'\arrow[r,phantom,"{\deleted{\longrightarrow}}" description]',r'\arrow[r,phantom,"{\deleted{\longrightarrow}}" description,"{\deleted{\handwritten{\unsure{u}}}}"]')
cluster=r'''\deleted{\unsure{\mbox{\begin{tikzpicture}[x=.5em,y=.5em,baseline=-.2ex]
\draw (.17,.57) ellipse (.16 and .21);
\draw (.08,-.25) .. controls (.28,.05) and (.17,.76) .. (.13,1.02);
\draw (.13,1.02) .. controls (.18,.91) and (.3,.91) .. (.38,1.04);
\draw (.23,.73)--(.43,.79);
\draw (.81,.61)--(.48,.24)--(.79,.24) .. controls (1,.08) and (.76,-.08) .. (.68,-.05);
\end{tikzpicture}}|,}}'''
r.edit(r'\deleted{\unsure{,}}',cluster)
r.edit(r'\inserted{ni $\handwritten{\mu}$,}',r'\inserted{ni $\handwritten{\mu}$,\handwritten{\begin{tikzpicture}[x=.4cm,y=.4cm,baseline=-.2ex]\draw (0,-.2) .. controls (-.18,.36) and (.2,.46) .. (.42,.48) .. controls (.93,.5) and (1.34,.62) .. (1.27,.79);\end{tikzpicture}}}')
r.edit(r"n'y\inserted{a}",r"n'y\inserted{a\handwritten{\begin{tikzpicture}[x=.4cm,y=.4cm,baseline=-.2ex]\draw (0,-.2) .. controls (.05,.21) and (.31,.65) .. (.53,.94);\end{tikzpicture}}}")
# Root's decisions, including all fifteen C uncertainty loci.
ch('heading underline',r'\uline{catégories}','plain catégories',r'\uline{catégories}','A separate baseline stroke runs under catégories and stops before the terminal point.','title','omission')
ch('first typed tensor sign','otimes','otimes',r'\unsure{\otimes|\Omega}','The rounded upper arch, crossing interior and extended lower feet recur through the typed formulas. The first occurrence remains qualified; subsequent occurrences use the first candidate.','tensor-title; etensor; assoc; du; dv; diagram','misread symbol or index','medium',True,True,False,True)
ch('Définition typography','plain Définition','italic Définition','plain Définition','The typed word has the same upright bodies as the surrounding text and no added underline.','definition','other')
ch('canceled first adjective','deleted additiv','deleted ill','deleted additiv','The a-d-d-i-t-i-v bodies can be followed beneath the separate x cancellation; no final e is present in this canceled run.','additivdel','readable ink left as \\ill{}','high',False,True,True)
ch('commutor letter first occurrence',r'\unsure{\mu|\psi}','psi',r'\unsure{\mu|\psi} retained','A short left upright and rounded low connection meet a taller right stem with a foot; an oblique through-stroke leaves the mu/psi identity unresolved.','mu1; commformula','misread symbol or index','medium',False,True,False,True)
ch('a canceled parenthesis final punctuation','deleted closing parenthesis only','deleted closing parenthesis only','deleted closing parenthesis and comma','A small descending punctuation tail survives at the right of the canceled closing parenthesis and the final x.','adel2','omission','medium',True,True)
ch('b two commutor letters','mu at both factors','psi at both factors','mu at both factors, using first qualified candidate','Both signs repeat the short-left/tall-right form and oblique added stroke of the first commutor sign. The page-first uncertainty applies to these later tokens.','b','misread symbol or index','medium',False,True,False,True)
ch('b identity first subscript letter','X','Y',r'\unsure{\rlap{Y}X|X}','Two diagonals establish X, while an additional central upright and upper fork are visible in the same cell. A physical Y/X overlap is the qualified first reading; no composition-based correction decides it.','bsub; bsubfirst','misread symbol or index','medium',True,True,False,True)
ch('c commutor letter','mu','psi','mu using first qualified candidate','The same slashed short-left/tall-right form is visible after et.','c','misread symbol or index','medium',False,True,False,True)
ch('c separator before handwritten axiom','colon','colon','semicolon','The lower point has a distinct descending leftward tail below its round body.','c-separator; hexnote','misread symbol or index','high',True,True)
ch('d unit name','1_C equals underlined1','underlined1_sub_underlinedC equals underlined1','1_C equals underlined1','The first 1 and the lowered C have no separate underline. The second 1 has a separate lower bar.','oneC','misread symbol or index','high',False,True,False,True)
ch('d canceled character after u(X):',r'\deleted{\unsure{x}}','omitted',r'\deleted{\unsure{x}} retained','Crossed diagonals and a horizontal bar remain, but the original body cannot be separated securely from the cancellation.','uxtdel','omission','low',False,True)
ch('d inserted v(X)= position','above second term','above whole display','above second term','The typed insertion sits directly above the commutor factor, to the right of d’où; its guide curves around that factor.','dvfull','insertion or placement')
ch('d second map commutor letter','mu','psi','mu using first qualified candidate','The short-left/tall-right sign with an oblique stroke repeats the earlier form.','dvfull','misread symbol or index','medium',False,True,False,True)
ch('d second map two ones','plain1 in mu(X,1) and X tensor1','underlined1 at both places','plain1 at both places','The long horizontal strokes under these numerals are their typed baseline feet; no detached lower bars occur.','dvfull','misread symbol or index','high',False,True,False,True)
ch('d factor enclosure drawing','two major curves only','omitted','two major curves plus two faint short strokes','Besides the principal transposition curves, a faint short diagonal lies inside the upper arch and a shallow arc lies under the first factor. The typed factor order is retained.','dvfull','drawing or diagram','medium',True,True)
ch('donc punctuation','donc par b','donc par b)','donc, par b','A low comma follows donc. There is no closing parenthesis after b; the parenthesis closes at the formula end.','donc','other','high',True,True)
ch('donc parenthesis deletion state','live parenthesis','whole parenthesis struck','live parenthesis','No cancellation crosses the parenthetical sentence. The nearby horizontal typed marks belong to the following line and ordinary character feet.','donc; avec','deletion state','high',False,True,False,True)
ch('donc formula commutor and argument','mu(1,X)','psi(underlined1,X)','mu(1,X), first sign candidate','The numeral has its baseline foot without a second bar; the filled commutor form repeats the first qualified sign.','donc','misread symbol or index','medium',False,True,False,True)
ch('small isolated mark before unit display','omitted','omitted','small point drawn','A detached black point is visible to the left of u(1), separate from the expression and with no secure mathematical role.','u1','drawing or diagram','medium',True,True)
ch('ce qui formula commutor','mu','psi','mu using first qualified candidate','The filled short-left/tall-right letter is again visible before the two underlined1 arguments.','ce','misread symbol or index','medium',False,True,False,True)
ch('de plus on veut enclosure','closed rounded rectangle','parentheses only','open loop with descending connector','The left end stops short of the lower edge. The lower/right outline continues leftward and bends down before Compatibilité; the path is reproduced.','bubblefull; bubble','drawing or diagram','high',True,True)
ch('compatibility addition capital and position','inserted Compatibilité','marginal compatibilité','inserted Compatibilité','The large open C begins at the right below the bubble, with the next line continuing leftward across the page; the connecting curve belongs to the bubble.','compatright; bubblefull; compatall','insertion or placement')
ch('compatibility addition associator',r'\unsure{\varphi|\phi}','varphi','phi','The cup/loop and through-stem identify the same associator family already written in the upper formulas. The phi/varphi rendering variant does not require a second letter reading.','compat1','other','high',True,False)
ch('compatibility addition between Y and Z',r'\unsure{ou}','ill',r'\unsure{,-|ou}','A small separate dark point and a short nearly horizontal stroke are visible; a contracted ou remains an alternative, without silently expanding it.','compat-axes1','misread word','low',True,True,True)
ch('compatibility addition Z and est','Z est','2 and ill',r'Z \unsure{est}','The angular top/diagonal/lower stroke identifies Z. The next word is compressed into a long low stroke and a final upstroke, allowing est but not settling all its letters.','compat-egal','misread word','medium',True,True,True)
ch('compatibility addition equality wording',r'\unsure{égal|ég.} à1','i.e.2=1',r'\unsure{égal|ég.} à1 retained','A raised accent, a g-like descender and a tall final stroke are visible; the small medial mark could be a letter or abbreviation point. A separate accented à precedes plain1.','compat-egal; compat2','misread word','low',False,True,False,True)
ch('compatibility addition commutor',r'\unsure{\psi|\mu}','psi','mu using first qualified candidate','The loopier hand form has the same competing cup and descending-stem features as the first commutor. The uncertainty is recorded at the first occurrence on this page, with mu used thereafter.','compat2','misread symbol or index','medium',True,True,False,True)
ch('compatibility addition quand','quand','ill','quand','The long q descender, joined low u/a/n and raised d are visible after the commutor sign.','compat2','readable ink left as \\ill{}','high',False,True,True)
ch('compatibility addition between X and Y',r'\unsure{ou}','dash',r'\unsure{,-|ou}','A distinct small point precedes the short horizontal stroke. Its interpretation as punctuation or a very contracted ou remains unsettled.','compat-axes2','misread word','low',True,True)
ch('compatibility addition last unit','plain1','underlined1','plain1','The numeral has one bottom foot joined to its stem and no separate underline.','compat-axes2','misread symbol or index','high',False,True,False,True)
ch('left note disputed adjective',r"\unsure{d'ensemble|d'ensembles}",'éventuelle','éventuelle','The rotated enlargement shows the low v/e/n sequence, a taller crossed t, then u/e and two adjacent l loops before the final e. No independent apostrophe is established.','leftword; leftnote','misread word','medium',True,False)
ch('left note relation ending',r'\unsure{relation|relations}','relation','relation','The final joined n ends the run; no additional s-shaped return follows it.','leftnote','misread word','high',True,False)
ch('left note dual mark',r'X^\vee',r'\check{X}',r'\check{X}','The small two-stroke check is centered directly above X after rotation, rather than placed at its upper right.','leftmath','misread symbol or index','high',True,False,False,True)
ch('left note outline','angular outline and pointer','omitted','angular outline and pointer','The long upper and lower strokes and notched right-side pointer surround the note. Their open left side is retained.','leftnote','drawing or diagram')
ch('NB punctuation','NB','N.B.','NB','The N and B are adjacent, with no separate points after them.','NB1','abbreviation expanded or spelling modernised')
ch('NB independent ending','indépendant plus deleted s','live indépendants','indépendant plus deleted s','An x crosses only the final s cell. The preceding t is uncanceled.','NBs','deletion state')
ch('NB commutor','mu','psi','mu using first qualified candidate','The low left stem, tall right stem and crossing oblique stroke match the earlier filled commutor letters.','NBmu','misread symbol or index','medium',False,True,False,True)
ch('NB de/du overlap','de','du',r'd\unsure{\rlap{u}e|e}','The cell contains an e-like central bar and rounded counter as well as a left upright and right baseline foot resembling u. The physical overlap remains qualified.','de-over; NBdeC','misread word','medium',True,True)
ch('NB C alphabet','plain C','underlined C','plain C','The lower curve belongs to the C body; no detached lower stroke occurs.','NBdeC','misread symbol or index','high',False,True,False,True)
ch('NB canceled tall letter',r'additiv\deleted{\unsure{t}}e','additive',r'additiv\deleted{\unsure{t}}e retained','A crossed tall stem remains between v and final e. The cancellation obscures the original lower part, so t remains tentative.','NBadd','omission','low',False,True)
ch('Soit live va','live va','deleted va','live va','The two cancellation strokes begin within définir, leaving va untouched.','soit; deletedphrase','deletion state')
ch('Soit replacement first word','voir','voit','voir','The last letter rises and turns into a rightward hook, without an independent crossbar; it is read as r.','insertphrase','misread word','medium',False,True)
ch('Soit compatible overlapping cell','compatible','compatible',r'compati\unsure{\rlap{v}b|b}le','The b has its high stem and lower bowl, with an additional short horizontal projection and internal descending stroke resembling a superposed v. The extra letter identification remains qualified.','compatible-over','misread word','medium',True,True)
ch('composite first label',r"\unsure{v'(1)|v(1)}",r"v'(\underline{1})",r"v'(\underline{1})",'A separate raised stroke after v establishes the prime. A short lower bar lies beneath the numeral within the parentheses; no inverse exponent is visible.','label1','misread symbol or index','high',True,False,False,True)
ch('composite second label',r"\unsure{u(\underline{1}')|\underline{1}\otimes u'}",r"u(\underline{1}')",r"qualified overlap of typed underlined1 tensor u prime and hand u(underlined1 prime)",'A typed1 with detached bar, the crossed rounded tensor cell and a typed u/prime remain beneath the handwritten curves and upright strokes. Both layers are represented in one qualified overlap, without assigning a correction chronology.','label2; diagram','misread symbol or index','low',True,True,False,True)
ch('composite canceled tensor factor',r'\deleted{\otimes\unsure{\underline{1}}}','omitted; editorial description',r'\deleted{\otimes\unsure{\underline{1}}} retained','The tensor contour and portions of the next numeral/low bar survive beneath dense oblique hatching. The numeral remains qualified.','tail','drawing or diagram','low',False,True)
ch('composite canceled last arrow and object',r'canceled right arrow and qualified underlined1 prime','omitted; editorial description','canceled right arrow and qualified underlined1 prime','A horizontal shaft with a right tip and a terminal numeral with a lower bar are visible under the blue hatching; the final raised/curved stroke remains uncertain.','tail','drawing or diagram','low',False,True)
ch('composite canceled small label','omitted','omitted','deleted qualified u above last arrow','A small cup with a returning right upright appears above the canceled tail, crossed by the oblique hatch. It is preserved as a qualified u-shaped label.','tail; diagram','omission','medium',True,True,False,True)
ch('verification insertion commutor','mu','psi','mu using first qualified candidate','The sign beside ni repeats the filled low-left/tall-right form and its oblique through-stroke.','ni','misread symbol or index','medium',False,True,False,True)
ch('verification last u underline','underlined u','plain u','underlined u','A detached horizontal bar is clearly below the u before the first parenthesis.','underu','misread symbol or index','high',False,True,False,True)
ch('verification canceled cluster',r'\deleted{\unsure{,}}','omitted','deleted qualified graphic cluster, comma alternative','Two cancellation x cells cover more than a low comma: a loop with a tall stem and a separate bent/zigzag stroke survive. Their visible shapes are drawn without assigning an unsupported letter or operator.','lastcancel; commadel','drawing or diagram','low',True,True)
ch('three insertion guides','omitted','omitted','curved guides beside v prime and ni mu; rising stroke beside a','The v-prime guide bends around the following c, the ni-mu guide curves down before mais, and the a insertion has a rising slanted guide between y and pas. All three are drawn in their page order.','vprime; ni; ainsert','drawing or diagram','high',True,True)
ch('folio','comment only','administrative page117','mspage117','The lower-left pencil figures read117.','folio','insertion or placement','high',True,True)
# Remaining in-place uncertainty, plus page-recurring symbol scope.
for args in [
 ('first typed tensor',r'\otimes',r'\Omega','medium','Crossed rounded arch with lower feet; later typed occurrences use first candidate.'),
 ('commutor first and later occurrences',r'\mu',r'\psi','medium','Short left stem, taller right stem, low cup and oblique crossing; first occurrence marked, later first candidate used.'),
 ('b identity first subscript',r'\rlap{Y}X','X','medium','Additional central stem is visible within the X diagonals.'),
 ('d canceled character','x','','low','Original body obscured by cancellation.'),
 ('compatibility first connector',',-','ou','low','Point and low stroke; contracted word remains possible.'),
 ('compatibility word after Z','est','','medium','Very compressed low stroke and final upright.'),
 ('compatibility equality adjective','égal','ég.','low','Medial letter/point and terminal tall stroke remain difficult.'),
 ('compatibility second connector',',-','ou','low','Separate point and horizontal stroke.'),
 ('NB de/du cell',r'\rlap{u}e','e','medium','e counter and extra u-like stem/foot coexist.'),
 ('NB canceled tall letter','t','','low','Tall tip visible above x cancellation.'),
 ('Soit compatible cell',r'\rlap{v}b','b','medium','Additional internal stroke and left projection at b.'),
 ('composite second label','overlap of underlined1 tensor u prime and u(underlined1 prime)','u(underlined1 prime)','low','Typed bodies remain under handwritten strokes; no correction chronology asserted.'),
 ('composite canceled factor',r'\underline{1}','','low','Numeral and low bar partly under hatching.'),
 ('composite canceled last object',r"\underline{1}'",'','low','Final curved/raised stroke covered by hatching.'),
 ('composite canceled small label','u','','medium','Cup and return upright under diagonal hatch.'),
 ('verification canceled cluster','graphic reproduction',',','low','Loop/stem and separate bent stroke cannot be reduced securely to punctuation.')]:r.doubt(*args)
r.notation('typed tensor sign','crossed arch with feet; first tensor/Omega marked','10/118','unresolved')
r.notation('associator and commutor','associator phi; commutor first mu/psi, later mu; loopier note forms included','10/118','partly unresolved')
r.notation('physical typed overlaps','qualified Y/X subscript, u/e and v/b cells; overlapping diagram label retained','10/118','unresolved')
r.notation('dual check placement','check centered above X in left note','10/118','read')
r.r['abbreviations']=[dict(abbreviation=a,expansion=b,attestations='10/118') for a,b in [('NB','nota bene'),('id','identité'),('ég.','égal (alternative only)')]]
r.r['inventory_overrides']={
 '017':{'first_words_or_objects':'canceled parenthesis including terminal comma'},
 '018':{'first_words_or_objects':'commutor product; identity with qualified Y/X overlap in first subscript'},
 '021':{'first_words_or_objects':'phi, mu and semicolon before axiome de l’hexagone'},
 '027':{'first_words_or_objects':'two major enclosure curves and two faint short strokes'},
 '028':{'first_words_or_objects':'live (donc, par b on aura aussi...)'},
 '036':{'first_words_or_objects':'open loop with descending connector before Compatibilité'},
 '037':{'first_words_or_objects':'Compatibilité; point-dash/ou alternatives; qualified est and égal/ég.; recurring commutor'},
 '039':{'first_words_or_objects':'Envisager aussi la structure éventuelle; relation; check above X tensor Y'},
 '041':{'first_words_or_objects':'NB; canceled s; qualified u/e overlap in de/du fait'},
 '047':{'first_words_or_objects':'Soit 1 prime; live va; compatible with qualified v/b overlap'},
 '054':{'first_words_or_objects':'v prime(underlined1), qualified overlapping second label'},
 '055':{'first_words_or_objects':'canceled tensor1, arrow with qualified u label, terminal qualified1 prime'},
 '059':{'first_words_or_objects':'canceled loop/stem and bent stroke reproduced graphically; comma alternative'} }
extras=[('dot','left of unit display','isolated small point','drawing','unnamed hand'),('label-tail','above canceled last arrow','qualified u-shaped label, canceled','deletion','his hand'),('guide-v','beside inserted v prime','curved guide','drawing','his hand'),('guide-ni','beside inserted ni mu','curved guide','drawing','his hand'),('guide-a','beside inserted a','rising guide stroke','drawing','his hand'),('folio','lower left','117','margin note','unnamed hand')]
for ident,pos,txt,kind,hand in extras:r.r['inventory_extra'].append(dict(scan='10:118',sheet_kind='typescript',hand=hand,element='118-extra-'+ident,kind=kind,position=pos,first_words_or_objects=txt,transcribed='yes'))
r.r['crops']=json.loads(Path('work/crops118.json').read_text())
r.r['inspection_note']='Whole image, both halves, C/H, all15 C uncertainty loci and60 inventory rows read in order. All81 crop recipes were viewed, including the compatibility rows whose initial three-image output was truncated and repeated individually. Every formula, deletion, insertion and marginal note was enlarged; the left note and slanted additions were rotated. A transient image transport error after de-over was retried for the two remaining images. No OCR, parallel transcription, context, compilation or mathematical check. No subsequent whole page opened before finalization. Greek rendering aliases alone are not H collation rows; physical extra strokes remain qualified where their identity is insecure.'
r.save('work/record118.json')
