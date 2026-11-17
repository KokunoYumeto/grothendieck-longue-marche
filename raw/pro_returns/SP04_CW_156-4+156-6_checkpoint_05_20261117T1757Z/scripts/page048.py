from author import Page
p=Page('156-4',48)
p.replace("\\deleted{\\unsure{F'}}","\\deleted{F'}")
p.replace(r'\unsure{deux|des}','deux')
p.replace('% Irregular ink blots in the blank space below the marginal formula.',r'''\figure{\begin{tikzpicture}[x=1cm,y=1cm,scale=.8]
\fill (0,0) .. controls (.1,.2) and (.16,.2) .. (.19,.55) -- (.3,.65) -- (.5,.6) .. controls (.48,.3) and (.7,.25) .. (.45,-.15) -- (.34,-.2) -- (.37,.38) -- (.12,.44) -- cycle;
\fill (1.9,.15) -- (1.85,.3) -- (2.1,.35) -- (2.35,.35) -- (2.35,.5) -- (2.55,.3) -- (2.65,.63) -- (3.35,.65) -- (3.35,.55) -- (3.5,.53) -- (3.35,.45) -- (3.45,.35) -- (3.25,.18) -- (2.7,.1) -- cycle;
\foreach \x/\y in {.6/.55,.7/.4,.4/-.28,2.1/.05,2.3/.7,2.5/-.02,3.4/.02,3.3/-.08}{\fill (\x,\y) circle(.025);}
\end{tikzpicture}}''')
p.replace(r'\deleted{\unsure{hors de $G$}}',r'\deleted{hors de $G$}')
p.replace('% the two strokes beside C 4 extend to the boxed formula',r'''\margin{\begin{tikzpicture}[x=1cm,y=1cm]\draw (0,0)--(.04,1.8);\draw (.12,-.03)--(.13,1.82);\end{tikzpicture}}''')
p.replace(r'\unsure{par exemple|faux pour}',r'\unsure{par exemple}')
p.replace(r'\unsure{orbites|strates}','strates')
p.replace(r'et strates \unsure{augmentées}',r'et str. augmentées')
p.replace("F\\to\\subset|F'\\subset|F\\subset","F^{\\to}\\subset|F'\\subset|F\\subset")
p.replace(r'est induite par une subdivision de $F$',r"est induite par une ``subdivision de $F$")
p.replace('% A long curved stroke groups the two lines.',r'''\margin{\begin{tikzpicture}\draw (.18,0) .. controls (-.15,.25) and (-.12,.85) .. (.1,1.2);\end{tikzpicture}}''')
p.replace(r'\margin{\unsure{OK}.}',r'\margin{OK.}')
p.replace(r'\in\unsure{\mathcal M|M}',r'\in M')
p.replace(r'\deleted{\unsure{F}}G\in\unsure{\mathcal F|\mathscr F}',r'\deleted{F}G\in\mathcal F')
p.replace(r'X\unsure{\in|\notin}',r'X\in')
p.replace(r'F_X\subset\unsure{F_Y|F_X}',r'F_X\subset F_Y')
p.replace(r'F=F_X\cup',r'F\equiv F_X\cup')
p.replace(r'\deleted{\unsure{Condition}} \inserted{\unsure{définition}}',r'\deleted{Condition} \inserted{définition}')
p.replace(r'et \unsure{R}',r'et $R$')
p.replace(r'$\unsure{F|G}$ compatibles',r'$F$ compatibles')
p.replace(r'X\unsure{,|\in}Y',r'X\unsure{\text{et}|,|\in}Y')
p.change('Definition, first old letter',"\\unsure{F'} overwritten by G",'G',"\\deleted{F'}G",'A straight stem and two horizontal bars remain inside G; a separate raised prime is visible.','definition',dc=True,kind='omission',confidence='medium')
p.change('Definition, deux',r'\unsure{deux|des}','deux','deux','The final crossing strokes form x after deu.','definition',dc=True,dh=False)
p.change('Definition, second old letter',"\\unsure{F'} overwritten by G",'G',"\\deleted{F'}G",'The previous F stem, middle bar and raised prime survive under the round G.','definition',dc=True,kind='omission',confidence='medium')
p.change('Definition, cancelled word',r'\unsure{raffinée|raffin}','raffinement',r'\deleted{\unsure{raffinée|raffin}}','The cancellation crosses the final low strokes; ra, double f and the i-dot survive, but the ending cannot be secured.','cancel_refine',confidence='low',kind='misread word')
p.change('Definition, marginal formula',r'F\ll G',r'F\ll G, with a note doubting its direction',r'F\ll G','Two left-pointing chevrons stand between the upright F and rounded G.','topmargin',kind='misread symbol or index',marked='yes',consequential='The written refinement direction F ≪ G is retained.')
p.change('Blank space below definition','Ink blots described in comment','omitted','TikZ approximation of ink blots','Two separated dark irregular forms and surrounding dots occupy the blank area; no letters can be distinguished inside them.','blots',dc=True,kind='drawing or diagram')
p.change('C4, inserted membership',r'G\unsure{\subset|\in}F',r'G\subset F',r'G\unsure{\subset|\in}F','The curved sign overlaps the descending stroke of figure; its possible middle bar cannot be separated.','insert_subset',kind='misread symbol or index',confidence='medium')
p.change('C4, cancelled phrase',r'\unsure{hors de G}',r'\ill{}','hors de G, deleted','The h loop, ors strokes and the separate de G remain visible through the line.','box_deleted',dc=True,kind=r'readable ink left as \ill{}',marked='yes',confidence='medium')
p.change('C4, double marginal rule','described in comment','described in note','two vertical rules in TikZ','Two parallel strokes extend from the C4 text toward the boxed display.','c4',dc=True,kind='drawing or diagram')
p.change('C4, donc','deleted donc','live donc','deleted donc','A cancelling stroke runs through the small word before the equality.','box',kind='deletion state (struck given live or live given struck)')
p.change('First left note, opening',r"C'est \unsure{démenti|évidemment}",'omitted',r"C'est \unsure{démenti|évidemment}",'The initial d-like upstroke is visible but an ink patch obscures adjoining letters.','leftnote_upright',kind='omission',confidence='low')
p.change('First left note, next words',r'\unsure{par exemple|faux pour}','omitted',r'\unsure{par exemple}','An initial descending p and the exemple sequence can be followed; the intervening small strokes remain damaged.','leftnote_upright',dc=True,kind='omission',confidence='medium')
p.change('First left note, strates',r'\unsure{orbites|strates}','omitted','strates fermées','The tall t strokes and intervening r-shaped shoulder support strates; fermées follows intact.','leftnote_upright',dc=True,kind='omission')
p.change('First left note, abbreviation','et strates','omitted','et str.','Only the short str group and a point precede the next word.','leftnote_upright',dc=True,kind='omission')
p.change('First left note, end',r'\unsure{augmentées} … cf plus bas','omitted','augmentées … cf plus bas','The g descender, mentées ending, following dots and underlined cf plus are visible after rotation.','leftnote_upright',dc=True,kind='omission',confidence='medium')
p.change('Second left note, opening',r'i.e \unsure{toute} multistrate',r'\ill{} multistrates',r'i.e \unsure{toute} multistrate','The i.e opening and singular multistrate are legible; the short word between them is compressed.','leftnote2',kind=r'readable ink left as \ill{}',marked='yes',confidence='medium')
p.change('Second left note, middle',r"d'une subdivision de G qui est compatible avec F",r'\ill{}',r"d'une subdivision de G qui est compatible avec F",'The small rising lines read d’une subdivision de G, qui est, then compatible avec F; compatible is underlined.','leftnote2',kind=r'readable ink left as \ill{}',marked='yes')
p.change('Second left note, ending','est dans G. OK','qui sont dans G','est dans G. OK','The short est precedes dans G on the underlined final line; OK follows to the right.','leftnote2',kind='misread word')
p.change('Right correction, symbol after F',"F\\to\\subset|F'\\subset|F\\subset",r'F\subset',"\\unsure{F^{\\to}\\subset|F'\\subset|F\\subset}",'A small raised hook follows the F before the inclusion curve. Its shape permits an arrow-like mark or prime.','rightcorrect',dc=True,kind='misread symbol or index',confidence='low',consequential='The extra raised mark in the correcting intersection is retained as a doubt.')
p.change('Cor1, inserted subdivision','inserted subdivision','subdivision without addition mark','inserted subdivision','The word is above the baseline and above the cancelled raffinement.','cor1',kind='insertion or placement')
p.change('Cor1, sous figure','sous figure','sous-figure','sous figure','There is a blank space between the two words; no joining hyphen is visible.','cor1',kind='abbreviation expanded or spelling modernised')
p.change('Cor1, quotation mark','subdivision','« subdivision »',"``subdivision",'Small opening quotation strokes occur below the word’s beginning; no separate closing pair is distinguishable at its end.','cor_quotes',dc=True,kind='misread symbol or index',confidence='medium')
p.change('Cor1, grouping curve','described in comment','omitted','curved grouping stroke in TikZ','A long curved stroke groups the two written lines at their left.','cor1',dc=True,kind='drawing or diagram')
p.change('Cor2, marginal OK',r'\unsure{OK}.','OK.','OK.','The oval O and two branches of K remain clear when enlarged.','cor2',dc=True,dh=False)
p.change('Cancelled proposition, former heading',r'\unsure{C 5}',r'(\ill{})',r'\unsure{C 5}','The opening C curve and 5-like lower strokes survive under a zigzag cancellation.','prop1',kind=r'readable ink left as \ill{}',confidence='medium',marked='yes')
p.change('Cancelled proposition, added title','inserted Proposition','Proposition without addition mark','inserted Proposition','The underlined title sits above the cancelled C5 heading.','prop1',kind='insertion or placement')
p.change('Cancelled proposition, old Y after X',r'\deleted{\unsure{Y}}','omitted',r'\deleted{\unsure{Y}}','A forked old letter and its downstroke are crossed by a thick zigzag.','prop1',kind='omission',confidence='low')
p.change('Cancelled proposition, M alphabet',r'\unsure{\mathcal M|M}',r'\mathcal M','M','Two pointed humps form a plain capital M; no separate ornamental swash is present.','prop1',dc=True,dh=False)
p.change('Cancelled proposition, added G clause',r'\inserted{\deleted{\unsure{F}}G\in\unsure{\mathcal F|\mathscr F}}',r'G\in\mathfrak F',r'\inserted{\deleted{F}G\in\mathcal F}','The raised clause has an old straight F with two bars under G, followed by a hooked family F.','cor2',dc=True,kind='insertion or placement',confidence='medium')
p.change('Cancelled proposition, membership',r'\unsure{\in|\notin}',r'\in',r'\in','The membership curve and three bars are intact. The long diagonal belongs to the cancellation of the entire paragraph and continues well above and below the sign.','prop_membership',dc=True,dh=False)
p.change('Cancelled proposition, old FY under first G',r'\deleted{\unsure{F_Y}}','G only',r'\deleted{\unsure{F_Y}}G','An earlier tall F is visible under G, with a lower stroke whose Y reading remains uncertain.','prop_membership',kind='omission',confidence='low')
p.change('Cancelled proposition, deleted equivalence phrase',r'i.e. F_X\subset\unsure{F_Y|F_X}',r'F_X\subset F',r'i.e. F_X\subset F_Y','The dotted i and low e remain before the cancellation; the final subscript has a fork and descending tail.','prop_membership',dc=True,kind='misread symbol or index',confidence='medium')
p.change('Cancelled proposition, old Y before G compatibles',r'\deleted{\unsure{Y}}G','G',r'\deleted{\unsure{Y}}G','Several old forked strokes persist under the round replacement G.','prop1',kind='omission',confidence='low')
p.change('Cancelled proposition, relation after F',r'F=F_X\cup G',r'F=F_X\cup G',r'F\equiv F_X\cup G','Three short horizontal bars, vertically separated, stand between F and F_X.','prop_equals',dc=True,kind='misread symbol or index',consequential='The relation is the written triple bar ≡, rather than the two bars printed in both drafts.')
for place,crop in [('after union','prop_equals'),('after inserted double chevron','prop2'),('after final raffine','prop2')]:
 p.change('Cancelled proposition, old FY '+place,r'\deleted{\unsure{F_Y}}G','G',r'\deleted{\unsure{F_Y}}G','The older F bars and a low overwritten stroke remain inside and below the replacement G; the old subscript remains uncertain.',crop,kind='omission',confidence='low')
p.change('Cancelled proposition, deleted raffine','deleted raffine; inserted double chevron','double chevron only','deleted raffine; inserted double chevron','The letters raffine are crossed on the baseline and the double chevron is inserted nearby.','prop2',kind='omission')
p.change('Proposition margin, revision',r'\deleted{\unsure{Condition}} \inserted{\unsure{définition}}',r'\uncertain{définition}',r'\deleted{Condition} \inserted{définition}','Condition has a large opening C and the remaining ndition strokes under a cancellation; définition is written above it.','prop_margin',dc=True,kind='omission',confidence='medium',marked='yes')
p.change('Proposition margin, relations',r'de \leq via \ll et \unsure{R}',r'\ill{} en \ll et \mathcal R',r'de \leq via \ll et R','The small de and less-than-with-lower-bar precede via; the final R has a round bowl and a straight diagonal leg.','prop_margin',dc=True,kind=r'readable ink left as \ill{}',confidence='medium',marked='yes')
p.change('Cancelled proof, first old word',r'\deleted{\unsure{On}}',r'\struck{\ill{}}',r'\deleted{\unsure{On}}','An oval and an adjoining short hump remain under the heavy local stroke.','proof',kind=r'readable ink left as \ill{}',confidence='low',marked='yes')
p.change('Cancelled proof, X et F',r'\unsure{F|G}','F','F','The letter has a straight vertical stem and two horizontal bars.','proof',dc=True,dh=False)
p.change('Cancelled proof, inner deleted clause',r'il \unsure{faut} X\unsure{,|\in}Y\in F','omitted',r'il \unsure{faut} X\unsure{\text{et}|,|\in}Y\in F','The long local line crosses il, a word with an f ascender, X, a small loop-and-stem mark, Y and the membership sign before F. The joining mark remains uncertain.','proof_cancel',dc=True,kind='omission',confidence='low')
p.change('Cancelled proof, F figure','F figure','omitted','F figure','After the locally cancelled clause a comma and F figure stand on the same baseline.','proof',kind='omission')
p.change('Cancelled proof, old equality',r'\deleted{\unsure{=}}','live =',r'\deleted{\unsure{=}}','Short bars after F_Y are crossed by a local diagonal; the relation beneath it remains doubtful.','proof',kind='deletion state (struck given live or live given struck)',confidence='low')
p.change('Cancelled proof, old G',r'\deleted{\unsure{G.}}',r'\ill{}',r'\deleted{\unsure{G.}}','The heavy horizontal cancellation covers a rounded G-like curve and a terminal dark point.','proof',kind=r'readable ink left as \ill{}',confidence='low',marked='yes')
for place,reading,why,crop in [
 ('Definition, cancelled word','raffinée|raffin','Final strokes are crossed; retain uncertainty.','cancel_refine'),
 ('C4 inserted condition',r'\subset|\in','The possible middle stroke overlaps the preceding descender.','insert_subset'),
 ('First left note, opening','démenti|évidemment','An ink patch obscures the small middle letters.','leftnote_upright'),
 ('First left note, example','par exemple','Some short strokes between the first and second words are damaged.','leftnote_upright'),
 ('Second left note','toute','The compact high word is partly crossed by adjacent strokes.','toute'),
 ('Right correction',"F^{\\to}\\subset|F'\\subset|F\\subset",'The small raised hook admits several readings.','rightcorrect'),
 ('Cancelled heading','C 5','The former label is heavily crossed.','prop1'),
 ('Cancelled proposition, old letters Y','Y','Both old Y forms are overwritten and crossed.','prop1'),
 ('Cancelled proposition, former FY at four positions','F_Y','The old subscript cannot be separated securely from the replacement G.','prop2'),
 ('Cancelled proof, old first word','On','Heavy local cancellation crosses its letters.','proof'),
 ('Cancelled proof, old verb','faut','Only the f ascender and low following strokes survive.','proof_cancel'),
 ('Cancelled proof, joining mark',r'\text{et}|,|\in','A small loop and stem are crossed by the horizontal cancellation.','proof_cancel'),
 ('Cancelled proof, former relation','=','A local oblique stroke crosses the short bars.','proof'),
 ('Cancelled proof, final cancelled symbol','G.','The rounded remnant and point are partly covered.','proof')]:p.doubt(place,reading,why,crop)
p.inventory([
 ('text','top','Définition Soient F,G deux figures'),('deletion','definition, two sites','old F prime under G'),('deletion','definition','raffinée|raffin'),('insertion','definition end','sous-figure'),('margin note','upper left','On écrit F ≪ G'),('drawing','blank below definition','two ink blots and spots'),('text','upper middle','On veut que ce soit une relation'),('text','middle','C 4 Soient F une figure'),('insertion','C4 above line','i.e. G figure et G subset/in F'),('deletion','C4','il existe une subdivision F prime de F'),('insertion','C4','G prime union (F minus G) est une'),('insertion','C4','de F'),('deletion','before box','hors de G'),('display','centre','boxed G prime intersection F subset G'),('drawing','left of C4','double vertical rule'),('deletion','below box','donc'),('text','below box','G prime intersection F equals G prime intersection G'),('margin note','left of C4','C’est démenti … strates fermées'),('margin note','left below box','i.e toute multistrate d’une subdivision'),('margin note','beside box','OK arrow'),('margin note','right below box','Corriger : exists subdivision'),('text','lower middle','Cor. 1 Toute'),('deletion','Cor1','raffinement'),('insertion','Cor1 above line','subdivision'),('drawing','Cor1 left','curved grouping stroke'),('text','below Cor1','Cor 2 La relation de raffinement'),('display','Cor2','F double-chevron G'),('margin note','Cor2 left','OK'),('deletion','lower quarter','C5 Proposition …'),('insertion','cancelled proposition','Proposition'),('insertion','cancelled proposition top','G in family F'),('deletion','cancelled proposition, local','old Y and FY letters; i.e. F_X subset F_Y; raffine'),('insertion','cancelled proposition','double chevron'),('margin note','lower left','C’est la Condition définition de ≤ via ≪ et R'),('deletion','bottom','On Supposons en effet'),('deletion','bottom local','il faut X et/comma/in Y in F; old equals; G')])
p.notation('equivalence sign',r'\equiv','Three separately visible short horizontal bars in the cancelled F ≡ F_X union G formula.')
p.notation('opening quotation marks','``','Two short upright marks low at the start of subdivision in Cor1; no separate closing pair is legible.')
p.r['abbreviations']=[dict(abbreviation='str.',expansion='strates',evidence='left marginal note before augmentées'),dict(abbreviation='il f. et s.',expansion='il faut et suffit',evidence='cancelled proposition'),dict(abbreviation='subd.',expansion='subdivision',evidence='last line')]
p.save()
