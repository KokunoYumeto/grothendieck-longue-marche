from author import Page
p=Page('156-4',57)
p.replace(r'\unsure{\mathcal M|\mathscr M}',r'M')
p.replace(r'\mathcal M',r' M')
p.replace(r'\unsure{\mathcal F|\mathscr F}',r'\mathcal F')
p.replace(r'\unsure{quelc.|qelc.}','quelc.')
p.replace(r'\unsure{Un|Une}','Un')
p.replace(r"\unsure{qu'elles-même|qu'elles-mêmes|qu'elle-même}","qu'elles-même")
p.replace(r'\unsure{courante|courte}','courante')
p.replace(r'\unsure{(quand les|(quand la}','(quand les')
p.replace(r"\unsure{en boules''|en boules}","en boules''")
p.replace(r'\unsure{par morceaux|ponctuées}','par morceaux')
p.replace(r'\unsure{Car dans|Car chez}','Car dans')
p.replace(r'\unsure{cas|cat.}','cas')
p.replace(r'\unsure{ordre|données}','ordre')
p.replace(r'\unsure{quelconq.|quelconques}','quelconq.')
p.replace(r'\unsure{un|une}','un')
p.replace(r'\unsure{réduite|discrète|vide réelle}',r'\unsure{vide réel|vide réelle}')
p.replace(r'\unsure{bloque|bloquer}','bloque')
p.replace(r"\unsure{F'|F'_{a}}",r"F'_{a}")
p.replace(r'\unsure{ens|ens.}','ens')
p.replace(r'\uuline{$I\neq\varnothing$}',r'\begin{tikzpicture}[baseline=(f.base)]\node[inner sep=0] (f) {$I\neq\varnothing$};\draw ([yshift=-2pt]f.south west)--([yshift=-2pt]f.south east);\draw ([yshift=-4pt]f.south west)--([yshift=-4pt]f.south east);\draw ([yshift=-6pt]f.south west)--([yshift=-6pt]f.south east);\end{tikzpicture}')
p.replace('% margin note written sideways',r'''% Two marginal callout strokes, reproduced beside the associated additions.
\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw[->] (1.4,0) .. controls (.7,.05) and (.2,.45) .. (0,1.2);
\draw (1.5,-.1) .. controls (.55,.25) and (.85,.75) .. (.7,.7) .. controls (.4,.35) and (.75,.1) .. (1.5,-.1);
\end{tikzpicture}}
% margin note written sideways''')
p.replace('% slanted\n\\margin{bloque',r'''% Long curved separator beside the lower margin and proposition.
\figure{\begin{tikzpicture}[x=1cm,y=1cm]\draw (.6,3) .. controls (.2,2.3) and (.05,1.3) .. (.15,.9) .. controls (.2,.3) and (.4,.05) .. (.65,0);\end{tikzpicture}}
% slanted
\margin{bloque''')
p.change('a), cancelled verb',r'\deleted{\unsure{est|était}}',r'\struck{\ill{}}',r'\deleted{\unsure{est|était}}','Initial low e and tall joined strokes remain visible under the cancellation; the ending is not separable.','prop',kind=r'readable ink left as \ill{}',confidence='low',marked='yes')
p.doubt('a), cancelled verb','est|était','The stroke crossing the ascenders obscures the ending','prop','low')
p.change('a), figures',r'figures',r'\emph{figures}',r'figures','The low return is the descender of g; no independent underline runs beneath the word.','prop',kind='other')
p.change('a) and Lieux, ambient M',r'\unsure{\mathcal M|\mathscr M}; \mathcal M',r'\mathcal M',r'M','The two tall humps and plain downstrokes match the recurring plain M.','prop',dc=True,dh=False,confidence='high')
p.change('b), intersection formula',r'\overline{F\cap G}',r'\overline{F\wedge G}',r'\overline{F\cap G}','The sign under the overbar has a rounded crown and two descending sides; the preceding existence clause has a separately visible angular wedge.','b',kind='misread symbol or index',consequential='The bar formula contains F∩G, while the preceding existence statement writes F∧G.')
p.change('b), following sentence','Même pour','Même chose pour','Même pour','Only Même followed directly by pour is written.','b',kind='text not on the page')
p.change('b), abbreviation',r'\unsure{quelc.|qelc.}','quelc.','quelc.','The q descender is followed by a low u/e sequence, tall l, open c and terminal point.','b',dc=True,dh=False)
p.change('b), cancelled word and position',r'et \deleted{\unsure{on|en}}',r'et \struck{\ill{}} [Lieux',r'et \deleted{\unsure{on|en}} before the bar formula','The et and short struck word sit at the left of the compressed b) formula, above the opening bracket of Lieux.','b',kind='insertion or placement',confidence='medium',marked='yes')
p.doubt('b), cancelled word','on|en','The initial oval is crossed and may be open','b','low')
p.change('b), marginal designation',r'\inserted{\uuline{figure intersection}}','note: figures irréductibles',r'\inserted{\uuline{figure intersection}}','The rotated note has singular figure, then the i-n-t-e-r-s-e-c-t-i-o-n sequence with crossed t; two underline strokes are visible.','insertion',kind='misread word',consequential='The inserted name reads figure intersection.')
p.change('b), nonempty index insertion','avec I≠∅, double underline','avec I≠∅, no underline','avec I≠∅, three underline strokes','Three separate horizontal rules lie beneath I≠∅. The neq stroke and the slashed oval are clear.','insertion',dc=True,kind='other')
p.change('upper additions, leaders','not drawn','described in note','two curved callout strokes in TikZ','A long curved arrow rises toward the upper marginal warning; the second curve loops beside the lower addition.','insertion',dc=True,kind='drawing or diagram',confidence='medium')
p.change('upper vertical margin',r'\uline{Mais attention} il vaut mieux ne pas les noter $F\cap G$, car quand il y a une notion de support, ça ne correspond pas à l\textquoteright intersection des supports, sauf si $F,G$ compatibles.','Mais attention, il n\textquoteright y a ill F∧G ill','Mais attention il vaut mieux ne pas les noter F∩G, car quand il y a une notion de support, ça ne correspond pas à l’intersection des supports, sauf si F,G compatibles.','After rotation, mieux has its final x; noter has tall t; the formula has a rounded cap; notion, support, intersection, supports and sauf si are individually visible. No comma follows attention.','margin_top',kind='omission')
p.change('Lieux, family alphabet',r'\unsure{\mathcal F|\mathscr F}',r'\mathfrak F',r'\mathcal F','The family sign has the recurring hooked/slanting stem and curved top.','lieux',dc=True,dh=False)
p.change('Lieux, cancelled short word',r'\deleted{\unsure{pas|pet}}',r'\struck{figures}',r'\deleted{\unsure{pas|pet}}','Only a p descender and two short low strokes occupy the cancelled space; no tall f or g descender is present.','lieux',kind='misread word',confidence='low')
p.doubt('Lieux, cancelled word','pas|pet','The low letters are merged into the strike','lieux','low')
p.change('Lieux, first cancelled opening',r'\deleted{\unsure{Un|Une},}','omitted',r'\deleted{Un,}','A capital U, low n and separate downward comma survive the short strike at the left.','lieux_old',dc=True,kind='omission',confidence='medium')
p.change('Lieux, longer cancelled sentence',r'Un lieux est de \unsure{ce nom|nom}','Un lieux est donc',r'Un lieux est de \unsure{ce nom|nom}','After est there is a looped d with a low e; farther right the strike merges with the low letters. The x of lieux is visible.','lieux_old',kind='misread word',confidence='low')
p.doubt('Lieux, cancelled ending','ce nom|nom','The long rule merges with the low humps after de','lieux_old','low')
p.change('Lieux, Tout lieu est irréductible','no inserted donc',r'\add{\uncertain{donc}}','no inserted donc','The slanted strokes crossing the gap belong to the oblique marginal note; no horizontal donc sequence appears between est and irréductible.','lieux_old',kind='text not on the page',marked='yes')
p.change('Lieux, final pronoun and ending',r"\unsure{qu'elles-même|qu'elles-mêmes|qu'elle-même}","qu'elle-même","qu'elles-même",'After the two l loops the terminal low s turns downward; même ends before the separate point without another s.','lieux_last',dc=True,kind='misread word',confidence='medium')
p.change('Lieux, cancelled continuation','Si F est une figure, les','Si F ill','Si F est une figure, les','The upper struck fragment reads Si F est une; below it figure has a tall f and descending g, followed by comma and les.','lieux_last',kind=r'readable ink left as \ill{}',marked='yes')
p.change('long oblique margin, complete note','full note with doubts','fragmentary descriptive note','full marginal text, with individually retained doubts','The oblique writing runs from Définition through the final exclamation; its line direction separates it from the main horizontal prose. The full note is retained, including both struck spans and the raised addition.','margin_full',kind='omission',confidence='medium',marked='yes')
for place,old,new,evidence,crop in [
('opening adjective',r'\unsure{courante|courte}','courante','The long word has c-o-u-r-a-n followed by tall t and e.','margin_a'),
('first cancellation',r'\unsure{(quand les|(quand la}','(quand les','The opening parenthesis and q descender survive; the last short group has tall l and low e/s.','margin_a'),
('first example',r"\unsure{en boules''|en boules}","en boules''",'The b and l ascenders frame ou; two separate raised closing quotation strokes follow the low ending.','margin_b'),
('second example',r'\unsure{par morceaux|ponctuées}','par morceaux','The two words begin with descending p and a separate low m; the remaining low strokes run to the closing parenthesis.','margin_b'),
('transition',r'\unsure{Car dans|Car chez}','Car dans','Capital C-a-r is followed by a looped d and low a/n/s.','margin_b'),
('noun after les',r'\unsure{cas|cat.}','cas','The small group has open c, oval a and final low s; no t ascender or separate terminal point.','margin_full'),
('after types d\textquoteright',r'\unsure{ordre|données}','ordre','The apostrophe follows d; the following group has round o and the repeated r/d humps without the long n-n sequence.','margin_middle'),
('abbreviated qualifier',r'\unsure{quelconq.|quelconques}','quelconq.','The terminal descending q is followed by a separate point; no u-e-s continuation.','margin_middle'),
('article before modèle',r'\unsure{un|une}','un','Only two low linked strokes form u-n before the next word.','margin_full')]:
 p.change('long margin, '+place,old,'omitted',new,evidence,crop,dc=True,dh=False,confidence='medium')
for place,reading,reason,crop in [
('model word','modèle|modélé','The low final letters and the accent position are not distinct enough to settle the two readings','margin_middle'),
('after barred E','de str.|de structure','Several short strokes are overlapped by the main text; the extent of the abbreviation remains uncertain','margin_middle'),
('semi- and following word','semi-','The low sequence is compatible with semi-; the following crossed word remains physically unreadable','margin_middle'),
('raised addition','univers vides|univers vide','The final low stroke after vide may be s or a joining stroke','margin_last'),
('cancelled phrase after forme','peut être une|peut être un','The dark rule crosses the word endings and hides the last e or its absence','margin_last'),
('multistrate qualifier','minimale|minime','The flattened humps and the short terminal ascender do not settle the ending','margin_last'),
('negative verb',"l'appelle|appelle",'The small initial mark is crossed by the main-text diagonal; its status as l-apostrophe remains uncertain','margin_full')]:
 p.change('long margin, '+place,r'\unsure{'+reading+'}','omitted',r'\unsure{'+reading+'}',reason+'.',crop,dh=False,confidence='low')
 p.doubt('long margin, '+place,reading,reason,crop,'low')
p.change('long margin, final words',r'\unsure{réduite|discrète|vide réelle}','omitted',r'\unsure{vide réel|vide réelle}','A v-shaped opening, dot, looped d and low e are followed, beyond the crossing, by a short r/e sequence and tall l-like ending. The final e remains unclear.','margin_finalword',dc=True,dh=False,confidence='low')
p.doubt('long margin, final words','vide réel|vide réelle','The crossing obscures the beginning and ending of the second word; neither grammatical repair nor contextual interpretation is used','margin_finalword','low')
p.change('Figures disjointes, quote mark',r"\unsure{,,|''}",'omitted',r"\unsure{,,|''}",'Two close short angular marks follow disjointes, at an ambiguous height relative to the sloping baseline.','disjoint',kind='omission',confidence='low')
p.doubt('Figures disjointes, quote',",,|''",'The marks are below the word top but the baseline slopes','disjoint','low')
p.change('Figures disjointes, F and G','separately underlined','no emphasis','separately underlined','Short independent horizontal lines lie directly below F and G.','disjoint',kind='other')
p.change('disjointness a), alternative wording','ou encore {F,G} majoré pour ≤','inserted i.e. {F,G} majoré pour ≤','ou encore {F,G} majoré pour ≤','The continuation begins with low ou and a separate encore on the same writing line; no insertion caret or interlinear placement.','disjoint',kind='misread word')
p.change('disjointness a), cancelled text','et b)','et b) on a ill','et b)','The strike covers et and b); the following ou encore is live. No on a sequence lies under this short strike.','disjoint',kind='text not on the page')
p.change('disjointness b), cancelled continuation',r'\unsure{ou|et} Cela signifie \unsure{donc|que}','ill',r'\unsure{ou|et} Cela signifie \unsure{donc|que}','Capital C, tall l, and the long g/f descenders remain visible beneath the rules. The first and last short groups remain merged with cancellation.','disjoint',kind=r'readable ink left as \ill{}',confidence='low',marked='yes')
p.doubt('disjointness b), cancelled conjunction','ou|et','The two low shapes are crossed','disjoint','low')
p.doubt('disjointness b), cancelled final word','donc|que','The upper and lower cancellation rules merge with its letters','disjoint','low')
p.change('disjointness b), inserted equivalence','inserted (i.e. barF∩barG=∅)','struck (i.e. ill F∩G=∅)','inserted (i.e. barF∩barG=∅)','The small parenthetical formula is written above the cancelled words; the horizontal rules pass below its letters. Separate bars stand over both F and G.','disjoint',kind='deletion state (struck given live or live given struck)',consequential='The parenthetical condition barF∩barG=∅ is a live insertion.')
p.change('lower marginal note',r'\unsure{bloque|bloquer} mes ``\unsure{coproduits|composantes}\textquoteright\textquoteright','omitted',r'bloque mes ``\unsure{coproduits|composantes}\textquoteright\textquoteright','After rotation, b-l-o-q-u-e ends in a low e without a further r; mes and the two quotation marks are visible. The interior of the quoted noun is crossed by the long leader.','margin_low',dc=True,kind='omission',confidence='medium')
p.doubt('lower margin, quoted noun','coproduits|composantes','The middle strokes overlap the curved separator and are not fully distinguishable','margin_low','low')
p.change('lower margin, curved separator','omitted','omitted','TikZ curve beside note and proposition','The long continuous curved stroke runs down beside the lower main text and turns toward the beginning of application.','prop_end',dc=True,kind='drawing or diagram')
p.change('last Prop, indexed figure',r"\unsure{F'|F'_{a}}",r"F'",r"F'_{a}",'A distinct small closed oval with right/upward exit lies below and to the right of F, separate from its foot; the prime is above.','prop_end',dc=True,kind='misread symbol or index',confidence='medium',consequential='The last proposition writes F′ with a small subscript a at this occurrence.')
p.change('last Prop, sous figure','sous figure','sous-figure','sous figure','A clear blank separates the two words, with no hyphen.','prop_end',kind='abbreviation expanded or spelling modernised')
p.change('last Prop, before application',"l'application","et l'application","l'application",'The new line begins directly with the l-apostrophe; the separate et above belongs before F′∪G′.','prop_end',kind='text not on the page')
p.change('last Prop, ordered pair',r"(F';G')",r"(F',G')",r"(F';G')",'The separator has a distinct upper point and lower comma stroke between the primed letters.','prop_end',kind='misread symbol or index')
p.change('last cancellation, abbreviation',r'\unsure{ens|ens.}','ens.','ens','The abbreviated word has a low terminal s immediately followed by the space before de; no separate point is visible.','prop_end',dc=True,kind='abbreviation expanded or spelling modernised',confidence='medium')
p.change('last cancellation, family letter',r'\unsure{\mathcal F|F}',r'\mathfrak F',r'\unsure{\mathcal F|F}','The tall stem and two cross strokes remain visible, but the lower cancellation obscures the alphabet-defining foot.','prop_end',dh=False,confidence='low')
p.doubt('last cancellation, family letter',r'\mathcal F|F','The foot is merged with a heavy overstrike','prop_end','low')
p.inventory([
('text','top','Proposition a) Si F'),('deletion','a), after F','est/était'),('insertion','a), relation','≤'),
('text','compressed b)','Si F et G sont deux figures'),('display','b)','F∧G existe; bar(F∩G)=barF∩barG'),('deletion','b), after et','on/en'),
('insertion','left of b)','figure intersection'),('insertion','left of b), above designation','avec I≠∅'),('drawing','beside upper marginal additions','two callout strokes'),
('margin note','upper left, vertical','Mais attention'),('text','middle, bracketed','Lieux de F'),('deletion','Lieux, after les','pas/pet'),('deletion','left before Tout','Un,'),('deletion','before Tout','Un lieux est de'),('deletion','after bracket, two lines','Si F est une figure, les'),
('margin note','left, oblique','Définition courante'),('deletion','oblique margin, first','(quand les'),('deletion','oblique margin, lower','peut être une/un'),('insertion','oblique margin, raised','univers vide(s),'),('insertion','oblique margin','une'),
('text','lower middle','Figures disjointes F et G'),('display','disjointness a)','F∪G; {F,G} majoré'),('deletion','a), before ou encore','et b)'),('display','disjointness b)','F∩G=∅_F'),('deletion','b), after formula','ou/et Cela signifie donc/que'),('insertion','b), above cancellation','(i.e. barF∩barG=∅)'),
('margin note','lower left, oblique','bloque mes'),('drawing','lower left separator','long curved stroke'),('deletion','above final Prop','Si F et G sont'),('text','bottom','Prop Si F et G sont disjointes'),('display','last Prop','F′≤F, G′≤G; (F′;G′)↦F′∪G′'),('deletion','last line','de l’ens de F')])
p.notation('triple emphasis underline',r'\begin{tikzpicture}...\end{tikzpicture}','Three parallel rules beneath the nonempty-index formula.')
p.notation('literal subscript a',r"F'_{a}",'Small closed oval and exit stroke, below the primed F in the final proposition.')
p.r['abbreviations']=[dict(abbreviation='quelc.',expansion='quelconque',evidence='b), terminal point visible'),dict(abbreviation='quelconq.',expansion='quelconque',evidence='oblique margin, final descending q and point'),dict(abbreviation='ens',expansion='ensemble',evidence='cancelled final line'),dict(abbreviation='Prop',expansion='Proposition',evidence='underlined final heading'),dict(abbreviation='str.',expansion='structure or strate',evidence='uncertain oblique marginal abbreviation')]
p.save()
