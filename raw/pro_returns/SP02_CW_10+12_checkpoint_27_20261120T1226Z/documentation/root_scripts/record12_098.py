from pathlib import Path
import sys,json
sys.path.insert(0,str(Path('SP02_CW_10+12/scripts').resolve()))
from root_record import Record
r=Record('B12-01',12,98,'text')
par=r'''\mbox{\begin{tikzpicture}[baseline=(base.base)]
\node[inner sep=0] (base) {Nous pensons cependant\deleted{,}};
\node[anchor=south west,inner sep=0,xshift=10em,yshift=.5ex] (added) at (base.north west) {\inserted{Par expérience personnelle,}};
\draw ([xshift=-.3em,yshift=-.3ex]base.south west) .. controls +(-.1,.3) and +(-.2,0) .. ([yshift=.1ex]base.north west) -- (added.south east) .. controls +(.7,0) and +(.5,.5) .. ([yshift=.7ex]added.north east) .. controls +(-2,.3) and +(.3,.3) .. ([xshift=.3em,yshift=1ex]added.north west) -- ([xshift=-1.2em]added.south west);
\end{tikzpicture}}'''
r.edit(r'\inserted{Par expérience personnelle,} Nous pensons cependant\deleted{,}',par)
r.edit(r'\deleted{\unsure{est et}}',r'\deleted{est et}')
r.edit(r'\unsure{remar|rem} \unsure{les|las}',r'remar les')
recent=r'ré\rlap{\deleted{\unsure{a|c}}}\handwritten{c}ent'
r.edit('le récent et',f'le {recent} et')
general=r'''\mbox{\begin{tikzpicture}[baseline=(base.base)]
\node[inner sep=0] (base) {Hodge des variétés};
\node[anchor=south west,inner sep=0,xshift=3.7em,yshift=.4ex] (added) at (base.north west) {\inserted{généralisée}};
\draw ([xshift=4.8em,yshift=-.3ex]base.south west) .. controls +(0,.3) and +(-.3,0) .. (added.south west) -- (added.south east) .. controls +(.3,0) and +(0,-.2) .. ([xshift=.3em]added.east);
\end{tikzpicture}}'''
r.edit(r'Hodge\inserted{généralisée} des variétés',general)
maint=r'''\mbox{\begin{tikzpicture}[baseline=(base.base)]
\node[inner sep=0] (base) {justifie par voie};
\node[anchor=south west,inner sep=0,xshift=2.5em,yshift=.4ex] (added) at (base.north west) {\inserted{dès maintenant}};
\draw ([xshift=-.4em]added.west) .. controls +(-.5,-.1) and +(-.5,0) .. (added.south west) -- (added.south east) .. controls +(.3,0) and +(0,-.2) .. ([xshift=.4em]added.east);
\draw ([xshift=6em,yshift=-.5ex]base.south west) .. controls +(0,.3) and +(-.3,0) .. ([xshift=2.5em]added.south west);
\end{tikzpicture}}'''
r.edit(r'justifie\inserted{dès maintenant} par voie',maint)
r.edit(r'Rham\handwritten{,}',r'Rham\handwritten{\unsure{,}}')
enchar=r'''\mbox{\begin{tikzpicture}[baseline=(base.base)]
\node[inner sep=0] (base) {des variétés algébriques};
\node[anchor=south west,inner sep=0,xshift=-.3em,yshift=.2ex] (added) at (base.north west) {\inserted{en caractéristique nulle}};
\draw ([xshift=5em,yshift=1ex]added.north west) .. controls +(-1.5,.3) and +(-.5,.3) .. (added.west) .. controls +(-.5,-.3) and +(-.2,0) .. ([xshift=-.4em,yshift=-.3ex]base.north west) -- ([yshift=-.3ex]base.north east) -- ([xshift=.1em,yshift=-.4ex]base.south east) -- ([xshift=.5em]added.east) .. controls +(.2,.3) and +(.4,.2) .. ([xshift=-3em,yshift=.7ex]added.north east);
\end{tikzpicture}}'''
r.edit(r'des variétés algébriques\inserted{en caractéristique nulle}',enchar)
semble=r'''\mbox{\begin{tikzpicture}[baseline=(old.base)]
\node[inner sep=0] (old) {\deleted{est}};
\node[anchor=south west,inner sep=0,xshift=-.7em,yshift=.2ex] (added) at (old.north west) {\inserted{semble}};
\draw ([xshift=.1em,yshift=-.6ex]old.south east) .. controls +(0,.3) and +(-.3,0) .. (added.south east) .. controls +(.4,.1) and +(0,-.2) .. ([xshift=.9em,yshift=.5ex]added.east);
\end{tikzpicture}}'''
r.edit(r'\deleted{est}\inserted{semble}',semble)
algeb=r'alg\rlap{\deleted{b}}\handwritten{é}\rlap{\deleted{\unsure{é|b}}}\handwritten{b}\rlap{\deleted{\unsure{u|r}}}\handwritten{ri}qu\deleted{p}es'
r.edit(r'algé\deleted{\unsure{bu|br}}\handwritten{br}iques',algeb)
preuve=r'''\mbox{\begin{tikzpicture}[baseline=(old.base)]
\node[inner sep=0] (old) {\deleted{résolution}};
\node[anchor=south west,inner sep=0,yshift=.1ex] at (old.north west) {\inserted{preuve}};
\end{tikzpicture}}'''
r.edit(r'\deleted{\unsure{résolution|resolution}}\inserted{preuve}',preuve)
r.edit(r'\deleted{signaler}',r'\deleted{signaler c}')
r.edit(r'relié\deleted{\unsure{s}}\handwritten{es}',r'relié\rlap{\handwritten{e}}\deleted{\unsure{s}}\handwritten{s}')
donnant=r'''\mbox{\begin{tikzpicture}[baseline=(old.base)]
\node[inner sep=0] (old) {\deleted{donnant}};
\node[anchor=base west,inner sep=0,xshift=.4em] (base) at (old.base east) {en particulier};
\node[anchor=south west,inner sep=0,xshift=-.5em,yshift=.2ex] (added) at (old.north west) {\inserted{et doivent donner}};
\draw ([yshift=-.4ex]old.south east) .. controls +(0,.3) and +(-.3,0) .. (added.south) -- (added.south east) .. controls +(.4,0) and +(0,-.2) .. ([xshift=.4em,yshift=.5ex]added.east);
\end{tikzpicture}}'''
r.edit(r'\deleted{donnant}\inserted{et doivent donner} en particulier',donnant)
r.edit(r'\handwritten{d}ont',r'\rlap{\deleted{e}}\handwritten{d}ont')
r.edit(r'\deleted{\unsure{ran|rang}}',r'\deleted{ran}')
adiq=r'ad\rlap{\deleted{\unsure{d|l}}}\handwritten{i}\rlap{\deleted{\unsure{é|e}}}\handwritten{q}\rlap{\deleted{i}}\handwritten{u}\rlap{\deleted{\unsure{a|p}}}\handwritten{e}s'
descoho=r'''\mbox{\begin{tikzpicture}[baseline=(base.base)]
\node[inner sep=0] (base) {et de niveau};
\node[anchor=base west,inner sep=0,xshift=.4em] (old) at (base.base east) {\deleted{se placent}};
\node[anchor=south west,inner sep=0,xshift=-.2em,yshift=.5ex] (added) at (base.north west) {\inserted{des cohomologies $\handwritten{\ell}$-'''+adiq+r''' se placent déjà}};
\draw ([xshift=-.5em]added.west) .. controls +(-.4,-.2) and +(-.3,0) .. (added.south west) -- ([xshift=.2em]base.north east) -- ([xshift=.2em,yshift=-.2ex]base.south east) .. controls +(0,.3) and +(-.2,0) .. (old.north west) -- (added.south east) .. controls +(.4,0) and +(0,-.2) .. ([xshift=.5em]added.east);
\end{tikzpicture}}'''
r.edit(r'et de niveau\deleted{se placent}\inserted{des cohomologies $\handwritten{\ell}$-adi\handwritten{ques} se placent déjà}',descoho)
r.edit(r'\deleted{\unsure{s motifs|motifs} déjà}',r'\deleted{\unsure{s motifs|motifs} déjà,}')
point=r'''\mbox{\begin{tikzpicture}[baseline=(old.base)]
\node[inner sep=0] (old) {\deleted{et qui Dans la}};
\node[anchor=base west,inner sep=0,xshift=.4em] (base) at (old.base east) {théorie de Deligne,};
\node[anchor=south west,inner sep=0,yshift=.2ex] (added) at (old.north west) {\inserted{Cet\deleted{te} point de vue est en tous cas en accord avec la}};
\draw ([xshift=-.4em]added.west) .. controls +(-.4,-.1) and +(-.2,.2) .. ([xshift=.3em,yshift=-.3ex]old.south west);
\draw ([xshift=-.3em]added.south west) -- (added.south east) .. controls +(.5,0) and +(.3,0) .. ([xshift=.6em]added.north east) -- ([xshift=-.6em,yshift=.6ex]added.north east);
\draw ([xshift=.2em,yshift=-.4ex]old.south east) .. controls +(0,.3) and +(-.2,0) .. ([xshift=.8em]old.north east);
\end{tikzpicture}}'''
r.edit(r'\deleted{ce qui dans la}\inserted{Cet\deleted{\unsure{te|t}} point de vue est en tous cas en accord avec la} théorie de Deligne,',point)
def ch(place,C,H,final,shows,crop,kind='other',confidence='high',against_C=False,against_H=True,marked_in_H=False,consequential=False):
 r.change(place,C,H,final,shows,crop,kind,confidence,against_C,against_H,marked_in_H,consequential)
ch('Par expérience personnelle, and its enclosing stroke',r'inline \inserted{Par expérience personnelle,}','inline Par expérience personnelle,',par,'The phrase is typed above the first line, beginning over the cependant area, well to the right of Nous. A long pen outline starts before Nous, runs above the base text and under the addition, curls around its right end and arches back over it, leaving an open upper-left segment. The double impression at P does not establish another letter.','paradd;parplace;Parcell','insertion or placement',against_C=True)
ch('initial Nous','Nous','nous','Nous','The first letter has two full-height uprights joined by a descending diagonal; a hand retracing darkens it but does not make it a lowercase n.','Nous','misread word')
ch('cancelled comma after cependant',r'\deleted{,}','omitted',r'\deleted{,}','A distinct curved comma tail descends to the left below the x overstrike; it is not just the diagonal of that x.','cependant;cependantcomma','deletion state')
ch('cancelled heuristique clause, bounding commas',r'\deleted{, heuristique quoique pour le moment largement heuristique,}',r'\struck{heuristique quoique pour le moment largement heuristique},',r'\deleted{, heuristique quoique pour le moment largement heuristique,}','The initial comma after compréhension and the final comma after heuristique are both beneath the cancellation row. All the intervening words remain readable through the typed crosses. H omits the first comma and places the second outside the cancellation.','comprehensionend;quoique;moment;heuristiquedel','deletion state')
ch('cancelled est et',r'\deleted{\unsure{est et}}','omitted',r'\deleted{est et}','The e bowls and bars, s upper/lower turns, two t ascenders/crossbars, and interword gap can be followed independently through the x row. C doubt is resolved without completing a sentence.','estet','omission',against_C=True)
ch('cancelled même si',r'\deleted{même si}','omitted',r'\deleted{même si}','The circumflex over the first e, the m arches and terminal s/i remain under the row of x strokes.','memesi','omission')
ch('cancelled travaux clause, partial word and les',r'\unsure{remar|rem} \unsure{les|las}','remarquables les','remar les','The a lower bowl and final r shoulder extend beyond rem; the following les has an e bar/bowl and open lower right, not an a upright. No ink for quables stands between remar and les. Both C alternatives are resolved from these surviving contours.','destravaux;recents;remar;lesmagnifiques;lesfine','misread word',against_C=True)
ch('cancelled travaux clause, final isolated t','magnifiques t','magnifiques','magnifiques t','After the final s there is a separate t ascender and crossbar before the unstruck le. H drops this abandoned letter.','lesmagnifiques','omission')
ch('overprinted c in récent','récent','récent',recent,'The black hand c covers a grey machine impression with a right upright, upper curve and right foot. It is a-like but fused with the retracing; a/c remains qualified rather than replaced by a clean c. A normal c/e impression elsewhere was compared directly.','recent;recentcell;bcontrol','deletion state','medium',True)
ch('généralisée and its leader',r'Hodge\inserted{généralisée} des variétés','Hodge généralisée des variétés',general,'The added word is typed above des variétés, starting near the end of Hodge; all its accents are visible. A pen line rises from the Hodge/des gap, runs below the word and curls up at the right.','generalisee;generalplace','insertion or placement',against_C=True)
ch('complex coefficient letter',r'\underline{C}',r'\mathbb{C}',r'\underline{C}','A separate horizontal stroke is directly below the single typed C; there is no double-stem alphabet.','Cunder','misread symbol or index',consequential=True)
ch('comma after complexes',r'\deleted{,}',', live',r'\deleted{,}','The comma at the end of complexes is covered by a compact black cancellation. Its downward original tail remains visible below the crossing ink. H gives it live.','complexcomma','deletion state')
ch('dès maintenant and its leader',r'justifie\inserted{dès maintenant} par voie','justifie dès maintenant par voie',maint,'The added words are on a raised typed line over the end of justifie and par voie. A curved pen underline curls at both ends and has a descending attachment after justifie.','desmaintenant;desmaintplace','insertion or placement',against_C=True)
ch('mark after first De Rham',r'Rham\handwritten{,}','Rham with no mark',r'Rham\handwritten{\unsure{,}}','At the clipped right edge there is dark hand ink descending after the last letter, with a comma-like lower turn; the end of the retraced m and a lower grey/brown blot cannot be separated completely. A mark is retained, qualified as comma rather than silently omitted or assigned an additional letter.','Rhamcomma;Rhamlow','omission','low',True)
ch('typed cohomoligue','cohomoligue','cohomologique','cohomoligue','The machine letters read c-o-h-o-m-o-l-i-g-u-e. The expected o/q sequence is not on the page and is not supplied.','cohomoligue','abbreviation expanded or spelling modernised')
ch('en caractéristique nulle and live old words',r'des variétés algébriques\inserted{en caractéristique nulle}',r'en caractéristique nulle \struck{des variétés algébriques}',enchar,'The new phrase is typed above des variétés algébriques. Its enclosing pen outline is open along the upper middle, runs across the tops of the old type, and drops after algébriques; the old words are live, with no x row or independent cancellation. The insertion belongs after them. H moves it before them and wrongly cancels them.','enchar;encharplace','deletion state',against_C=True)
ch('semble over est',r'\deleted{est}\inserted{semble}',r'\struck{est} semble',semble,'Typed semble begins slightly to the left above cancelled est. The old letters have both typewriter crosses and a pen line; a curved leader rises from the right of the old word toward the right of the addition.','semblest','insertion or placement',against_C=True)
ch('algébriques, overwritten middle cells',r'algé\deleted{\unsure{bu|br}}\handwritten{br}iques','algébriques',algeb,'After alg, a typed b ascender/left serif survives under handwritten é with its loop/bar and acute. The next cell has an é-like old impression and acute beside the new b but is fused enough to retain é/b. In the third, old u/r remains under the compressed handwritten ri, including a separate dot before the typed q. The three superpositions are recorded without asserting their chronological order.','algebriques;algebleft;algebmain;algebearlier','deletion state','medium',True)
ch('algébriques, cancelled p before es','omitted','omitted',r'qu\deleted{p}es','Between typed qu and es, an extra p has its own bowl, descender and lower foot beneath an x. Both witnesses omit this cancelled letter.','algebright;algebmain','omission',against_C=True)
ch('résolution accent',r'\deleted{\unsure{résolution|resolution}}',r'\struck{résolution}',r'\deleted{résolution}','A distinct short rising diagonal stands above the cancelled e and below the r of raised preuve. The acute is separate from both words and resolves C’s accent doubt.','resolution;resacute','other',against_C=True,against_H=False)
ch('preuve placement',r'inline \inserted{preuve}','inline preuve',preuve,'The replacement is typed directly above the beginning of résolution, sharing its left edge. No separate leader is visible.','resolution;preuve','insertion or placement',against_C=True)
ch('cancelled signaler c',r'\deleted{signaler}',r'\struck{signaler}',r'\deleted{signaler c}','After signaler and a space, a further c survives under x: an upper-right terminal, curved left side and lower return. Both drafts omit this abandoned letter.','signaler;signalend','omission',against_C=True)
ch('reliées old and new endings',r'relié\deleted{\unsure{s}}\handwritten{es}','reliées',r'relié\rlap{\handwritten{e}}\deleted{\unsure{s}}\handwritten{s}','The hand e overlaps an old type impression compatible with s, but its original curves cannot be fully separated. The following s is also handwritten. C’s old-letter doubt is retained and the overlap restored; H drops the old impression.','reliees','deletion state','medium',True)
ch('et doivent donner placement',r'\deleted{donnant}\inserted{et doivent donner}',r'et doivent donner \struck{donnant}',donnant,'The new typed phrase stands above donnant en particulier, beginning slightly before the old d. The pen leader rises from the right of cancelled donnant and runs beneath the new words, curling on the right. H reverses their serial order and neither draft reproduces this relative level and line.','donnant;etdoivent;donnantplace','insertion or placement',against_C=True)
ch('rational coefficient and lowered ell',r'\underline{Q}_{\handwritten{\ell}}',r'\mathbb{Q}_{\ell}',r'\underline{Q}_{\handwritten{\ell}}','The Q has a separate underline; its hand-modified ell is lower and to the right. No second Q stem occurs.','Qell','misread symbol or index',consequential=True)
ch('old e under dont',r'\handwritten{d}ont','dont',r'\rlap{\deleted{e}}\handwritten{d}ont','Inside the heavy handwritten d, a grey machine e keeps an independent horizontal middlebar and upper bowl. The new d supplies the tall right ascender and broad oval. The old impression omitted by both is retained beneath it.','dont;dontcell;econtrol','deletion state','medium',True)
ch('cancelled ran at the right edge',r'\deleted{\unsure{ran|rang}}','omitted',r'\deleted{ran}','The r shoulder, a bowl and n uprights/arch are visible under x before the dark page edge. No g is visible beyond them; the following line’s live rang is not used to restore an unseen letter. C’s alternative is removed for the visible fragment.','rangdel','omission',against_C=True)
ch('des cohomologies addition and leader',r'inline insertion after cancelled se placent',r'inline addition before \struck{se placent}',descoho,'The typed addition begins above et de niveau, well to the left of cancelled se placent. Its pen underline has a left curl, descends between niveau and the old phrase, rises again and curls at the right. Relative placement and attachment are retained.','niveau;seplacentdel;descoho1;descoho2;descoho3;descohoplace','insertion or placement',against_C=True)
ch('old letters under inserted adiques',r'-adi\handwritten{ques}','-adiques','-'+adiq,'After typed ad, the hand i/q/u/e cover four old cells, while final s remains typed. The first old cell has tall stem/serifs and a possible bowl (d/l); the second has an e bar/counter and possible acute (é/e); the third has a separate i dot and narrow upright; the fourth retains only an upper curve/left projection (a/p). Fused cells stay qualified instead of being restored from the expected word.','descoho2;adiqleft;adiqright','deletion state','low',True)
ch('cancelled s motifs déjà,',r'\deleted{\unsure{s motifs|motifs} déjà}',r'\struck{motifs déjà}',r'\deleted{\unsure{s motifs|motifs} déjà,}','The first possible s is merged with the pen loop and x row, so C’s alternative remains. After déjà, an independent comma tail descends below the final cancellation stroke; both witnesses omit it.','smotifs;smotifsfirst;dejacomma','deletion state','medium',True)
ch('cancelled et qui Dans la',r'\deleted{ce qui dans la}',r'\struck{\ill{} Dans la}',r'\deleted{et qui Dans la}','The first e has a middlebar/open lower bowl; the following t has an ascender, crossbar and lower hook. qui follows in separate cells. The D is full height with a vertical left and right bowl. C reverses the first pair and lowers D; H leaves readable et qui as ill.','cequidans;cequifirst;Dans;pointplace',r'readable ink left as \ill{}',against_C=True,marked_in_H=True)
ch('Cet and cancelled te',r'Cet\deleted{\unsure{te|t}}','Ce',r'Cet\deleted{te}','After the live Cet, a second t has its own ascender/crossbar under x and is followed by an e with a surviving upper counter and bar. C doubt is resolved; H drops both the live t and the cancelled te.','Cetdel','deletion state',against_C=True)
ch('point de vue addition and leader',r'inline \inserted{Cet...en accord avec la}','inline Ce...en accord avec la',point,'The entire typed phrase is above old et qui Dans la and the theory line. A long pen line runs beneath it, curls/drops at the left, branches down between old la and théorie and curls around the right end. Its raised position is reproduced rather than treating it as ordinary baseline prose.','pointphrase1;pointphrase2;pointplace','insertion or placement',against_C=True)
ch('cancelled car before puisque',r'\deleted{\unsure{car}}',r'\struck{car}',r'\deleted{\unsure{car}}','The cancellation crosses all three cells heavily. Parts compatible with c/a/r remain, but do not make the full old word independently certain. C’s qualification remains; H gives it without doubt.','cardel','other','low')
ch('four sets of quotation marks',r"``yoga''; ``conjectures standart'' twice; ``filtration par le poids''",'guillemets at all four loci',r"``yoga''; ``conjectures standart'' twice; ``filtration par le poids''",'Each opening and closing pair consists of two short high typewriter strokes. None has the angular shape of guillemets.','yogaquotes;standartquotes1;standartquotes2;filtrationquotes','misread symbol or index')
for place,reading,shows,crops in [
 ('cependant, C table decision','cependant','The p has a narrow descending stem beneath its rounded upper part, separate from the preceding e. C’s table resolution is independently confirmed; ceendant is rejected.','cependant'),
 ('cancelled abandoned sentence',r'\deleted{Pour terminer cette introduction}','The entire phrase remains readable under the row of typed x, including capital P and the full ending introduction. No omitted continuation is supplied.','Pourter;cetteintro'),
 ('five modified ell signs',r'\handwritten{\ell}','Each l-like type cell has an added diagonal handwritten stroke. Four body/coefficient occurrences and the raised addition were inspected; the coefficient sign is lowered.','ell1;ell2;Qell;ell3;descoho2'),
 ('empty reference brackets',r'\handwritten{[\quad]}','Two pen square brackets enclose blank paper. The following parenthesis and period belong to the surrounding typed sentence.','refbrackets'),
 ('standart, niveau and motivique comma','standart; niveau; motivique,','Both standart endings have t stems/crossbars, niveau has no final x, and motivique has a separate descending comma. The unexpected forms and punctuation remain.','standart1;standart2;niveau;motivcomma'),
 ('underlined words and cancelled des',r'\uline{cohomologie} \deleted{des} \uline{motivique}; \uline{rationnels}','Separate pen lines underline each of the three words. The intervening des has a cancellation through its letters and is retained.','cohodes;motivcomma;rationnels'),
 ('page ending',r'\handwritten{.}\deleted{(et non seulement}','A separate pen point follows rationnels. A continuous horizontal pen stroke cancels the opening parenthesis and words; the final t reaches the right edge, and no closing parenthesis is visible.','rationnels;etnon')]:
 ch(place,reading,reading,reading,shows,crops,against_H=False)
for line,reading,alternatives,confidence,comment in [
 ('old cell in récent','a','c','medium','Grey machine contours are fused with the hand c; right upright and foot favour a but do not settle it.'),
 ('after first Rham',',','unseparated pen mark at clipped edge','low','Pen retracing, a descending curve and a lower blot merge at the dark edge; comma remains qualified.'),
 ('algébriques, old second altered cell','é','b','medium','Acute-like trace and old bowl remain beside the new b, but lower parts are fused.'),
 ('algébriques, old third altered cell','u','r','medium','Hand ri covers most of the old cell; remaining bottom/side strokes do not decide u/r.'),
 ('reliées, overwritten ending','s','no secure alternative','medium','The hand e obscures the old type impression; C doubt is retained.'),
 ('inserted adiques, old first altered cell','d','l','low','Tall old serifed stem survives; possible left bowl is obscured by hand i.'),
 ('inserted adiques, old second altered cell','é','e','low','Old bar/counter visible; upper accent cannot be isolated fully from the hand q.'),
 ('inserted adiques, old fourth altered cell','a','p','low','Only an upper curve/projection remains distinct from the hand e.'),
 ('cancelled phrase after niveau de','s motifs','motifs','medium','Initial s-like trace merges with the hand loop and x cancellation.'),
 ('cancelled word before puisque','car','no secure alternative','low','Heavy cancellation leaves only partial compatible contours.')]:r.doubt(line,reading,alternatives,confidence,comment)
r.notation('underlined coefficient alphabet',r'\underline{C}; \underline{Q}_{\ell}','12:098 separate underlines beneath single typed capitals, with lowered coefficient ell.')
r.notation('typewriter l modified to ell',r'\handwritten{\ell}','12:098 five occurrences checked, including lowered Q coefficient and raised cohomologies addition.')
r.notation('typewriter double quotes',r"``yoga''; ``conjectures standart''; ``filtration par le poids''",'12:098 high double strokes at all four pairs, not guillemets.')
r.notation('handwritten overprints on typed letters',r'alg b/é, (é|b)/b, (u|r)/ri; e/d in dont; -ad(d|l)/i(é|e)/q i/u(a|p)/e s','12:098 original traces kept under overlapping hand replacements; fused old cells qualified and no chronological order inferred.')
r.r['inventory_overrides']={
 '098-04':dict(first_words_or_objects=', heuristique quoique pour le moment largement heuristique, including both commas'),
 '098-11':dict(first_words_or_objects='comma-like hand mark, qualified at clipped edge'),
 '098-16':dict(first_words_or_objects='b, qualified é/b and u/r beneath handwritten é,b,ri'),
 '098-17':dict(first_words_or_objects='handwritten é,b,ri superposed on old type'),
 '098-22':dict(first_words_or_objects='signaler c'),
 '098-26':dict(position='hand e overlapping old s-like cell, hand s following'),
 '098-30':dict(first_words_or_objects='hand d over old e'),
 '098-31':dict(first_words_or_objects='ran, no following g visible'),
 '098-36':dict(first_words_or_objects='hand i,q,u,e over old type; final s typed'),
 '098-37':dict(first_words_or_objects='qualified s motifs/motifs déjà, with cancelled comma'),
 '098-39':dict(first_words_or_objects='et qui Dans la'),
 '098-40':dict(position='raised above et qui Dans la and theory line'),
 '098-41':dict(first_words_or_objects='te')}
extras=[
 ('long enclosing/connecting outline for Par expérience personnelle,','drawing','above first line, attached before Nous','his hand'),
 ('old a/c beneath hand c in récent','deletion','le récent et','typewriter'),
 ('hand c over old cell in récent','insertion','le récent et','his hand'),
 ('leader for généralisée','drawing','after Hodge, beneath raised word','his hand'),
 ('curved underline and attachment for dès maintenant','drawing','above justifie/par voie','his hand'),
 ('outline around en caractéristique nulle','drawing','above live des variétés algébriques','his hand'),
 ('leader for semble','drawing','right of cancelled est','his hand'),
 ('cancelled p before es','deletion','corrected algébriques near end of first paragraph','typewriter'),
 ('leader for et doivent donner','drawing','above donnant en particulier','his hand'),
 ('old e under handwritten d','deletion','dont le','typewriter'),
 ('four old cells under handwritten i,q,u,e, three qualified','deletion','raised des cohomologies addition','typewriter'),
 ('leader with central downward step for des cohomologies','drawing','above et de niveau/se placent','his hand'),
 ('long underline with left/right curls and attachment branch','drawing','raised Cet...point de vue addition','his hand'),
 ('archive folio97 retained as comment','margin note','bottom left','another unnamed hand')]
for i,(s,k,p,h) in enumerate(extras,1):r.r['inventory_extra'].append(dict(scan='12:098',sheet_kind='text',hand=h,element=f'098-R{i:03d}',kind=k,position=p,first_words_or_objects=s,transcribed='yes'))
r.r['crops']=json.loads(Path('work/crops12_098.json').read_text())
r.r['inspection_note']='Root alone viewed the whole supplied image and both actual supplied halves before reading complete C/H, all ten C macro doubts/eleven doubt-table rows, the five slips and all44 inventory rows. All88 crop recipes were viewed in full; two initially truncated fine crops (cequifirst and Dans) were explicitly viewed separately and counted only then. The final two crops cover both complete standart quotation pairs. Both actual halves were reread line by line after the local decisions. Every cancellation, insertion and mathematical letter/index was enlarged; raised additions are horizontal typed text, with no slanted verbal margin requiring rotation. The first Rham edge mark remains qualified. Archive97 is retained as comment. This is first-pass collation, not the ordered second reading or a mathematical check. Context remains sealed.'
r.save('work/record12_098.json')
