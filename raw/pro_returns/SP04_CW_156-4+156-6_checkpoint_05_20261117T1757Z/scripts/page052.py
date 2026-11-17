from author import Page
p=Page('156-4',52)
p.replace(r'\unsure{dans|ds}','dans');p.replace(r'\unsure{ens}','ens')
p.replace(r'\unsure{relation|notion}','notion')
p.replace(r'\unsure{toute|tt}',r'\unsure{tout|toute|tt}')
p.replace(r'\unsure{\Phi|Q|\varphi}',r'\Phi')
# The cancelled draft has a pair of prime strokes at both right-hand barred nodes.
first,rest=p.text.split('On utilise que',1)
first=first.replace(r"\deleted{\overline{F}'}",r"\deleted{\unsure{\overline{F}'}}")
first=first.replace(r'\deleted{\overline F}',r"\deleted{\overline{F''}}")
first=first.replace(r'\deleted{\overline G}',r"\deleted{\overline{G''}}")
first=first.replace(r"\deleted{G'}",r"\deleted{\deleted{F}G'}")
first=first.replace('\n\n\\diagram',r'\figure{\begin{tikzpicture}\draw (0,0)--(0,1.8);\end{tikzpicture}}'+'\n\n\\diagram',1)
p.text=first+'On utilise que'+rest
p.replace(r"\unsure{F|F'}\subset\overline{F''}",r"F\subset\overline{F'}")
p.replace(r'\unsure{donc|dont}',r'\unsure{dont|donc}')
p.replace(r'\unsure{\overrightarrow F|\overline F}',r'\overrightarrow F')
p.replace(r'\unsure{pour|i.e.|or}',r'i.e.')
p.replace(r'\unsure{tt}','tt')
p.replace(r"\overline F'$ est \uline{induite par une}",r"\overline F'$ \uline{est \unsure{induite|induit} par une}")
p.replace(r"\unsure{\widetilde F'|\overline F'}",r"\widetilde F'")
p.replace(r'\deleted{\unsure{$\Phi$}}',r'\deleted{$\Phi$}')
p.replace(r'\unsure{Cont|Const|Compt}','Cont')
p.replace(r"\deleted{\unsure{F'|G'}}",r"\deleted{F'}")
# Reproduce the long U-ended vertical signs in the enclosed drawing as ink-shaped paths.
start=p.text.rfind(r'\diagram{')
cube=p.text[start:]
cube=cube.replace(r'\arrow[dd,hook]','').replace(r'\arrow[d,hook]','')
extra=r'''\draw (\tikzcdmatrixname-2-2.south) -- ([xshift=-3pt,yshift=8pt]\tikzcdmatrixname-4-2.north) .. controls ([xshift=-3pt,yshift=2pt]\tikzcdmatrixname-4-2.north) and ([xshift=2pt,yshift=2pt]\tikzcdmatrixname-4-2.north) .. ([xshift=5pt,yshift=9pt]\tikzcdmatrixname-4-2.north);
\draw (\tikzcdmatrixname-2-4.south) -- ([xshift=-3pt,yshift=8pt]\tikzcdmatrixname-4-4.north) .. controls ([xshift=-3pt,yshift=2pt]\tikzcdmatrixname-4-4.north) and ([xshift=2pt,yshift=2pt]\tikzcdmatrixname-4-4.north) .. ([xshift=5pt,yshift=9pt]\tikzcdmatrixname-4-4.north);
\draw (\tikzcdmatrixname-3-3.south) -- ([xshift=-3pt,yshift=8pt]\tikzcdmatrixname-4-3.north) .. controls ([xshift=-3pt,yshift=2pt]\tikzcdmatrixname-4-3.north) and ([xshift=2pt,yshift=2pt]\tikzcdmatrixname-4-3.north) .. ([xshift=5pt,yshift=9pt]\tikzcdmatrixname-4-3.north);
\draw (\tikzcdmatrixname-3-5.south) -- ([xshift=-3pt,yshift=8pt]\tikzcdmatrixname-4-5.north) .. controls ([xshift=-3pt,yshift=2pt]\tikzcdmatrixname-4-5.north) and ([xshift=2pt,yshift=2pt]\tikzcdmatrixname-4-5.north) .. ([xshift=5pt,yshift=9pt]\tikzcdmatrixname-4-5.north);
\draw ([yshift=-5pt]\tikzcdmatrixname-3-5.south) .. controls ([xshift=0pt,yshift=-12pt]\tikzcdmatrixname-3-5.south) and ([xshift=2pt,yshift=-12pt]\tikzcdmatrixname-3-5.south) .. ([xshift=5pt,yshift=-7pt]\tikzcdmatrixname-3-5.south);
\draw (\tikzcdmatrixname-1-1.south west)--(\tikzcdmatrixname-1-2.north east);
'''
cube=cube.replace('execute at end picture={','execute at end picture={'+extra,1)
cube=cube.replace(r'\& G \\',r'\& \substack{\unsure{\deleted{G}|G}\\G} \\')
cube=cube.replace(r'"\subset" description] \& \widetilde G',r'"\rotatebox{35}{$\subset$}" description] \& \widetilde G')
cube=cube.replace(r'\arrow[ur,phantom,"\subset" description]',r'\arrow[ur,phantom,"\rotatebox{40}{$\subset$}" description]')
p.text=p.text[:start]+cube

p.change('Corollaire, article','le Inf','la Inf','le Inf','The article ends in a low e loop before the tall I.','cor',kind='misread word')
p.change('Corollaire, preposition',r'\unsure{dans|ds}','dans','dans','A tall d is followed by low a/n strokes and a final s.','cor',dc=True,dh=False)
p.change('Corollaire, abbreviation',r'\unsure{ens}','ens.','ens','Three low letter movements appear without a separate following point.','cor',dc=True,kind='abbreviation expanded or spelling modernised')
p.change('Corollaire, cancelled noun',r'\unsure{relation|notion}',r'\ill{}','notion','The low n/o opening, tall t, dotted i and on ending remain beneath the strike.','cor_old',dc=True,kind=r'readable ink left as \ill{}',marked='yes',confidence='medium')
p.change('Corollaire, cancelled quantifier',r'\deleted{\unsure{toute|tt}}','toute live',r'\deleted{\unsure{tout|toute|tt}}','A cancellation crosses the tall initial t and low following strokes; the last letter is obscured.','cor_old',dc=True,kind='deletion state (struck given live or live given struck)',confidence='low')
p.change('Corollaire, inserted letter',r'\unsure{\Phi|Q|\varphi}',r'\Phi',r'\Phi','The loop is crossed by a vertical stem with a horizontal base, matching the other Phi forms on this sheet.','cor_insert',dc=True,dh=False,confidence='medium')
p.change('Corollaire, old letter under G',r'\deleted{\unsure{F}}G','G',r'\deleted{\unsure{F}}G','Straight older strokes remain under the rounded G, although their full form is hidden.','cor_old',kind='omission',confidence='low')
p.change('Corollaire, left rule','omitted','described','TikZ vertical rule','A long single vertical line stands to the left of the statement.','cor',dc=True,kind='drawing or diagram')
p.change('Cancelled first diagram, first barred node',r"\overline F'",r'\ill{}',r"\unsure{\overline F'}",'Dense zigzags cover the upright letter and raised mark; the bar and portions of an F remain, but the whole label is not secure.','cancel_diagram',dc=True,kind=r'readable ink left as \ill{}',marked='yes',confidence='low')
p.change('Cancelled first diagram, right barred top node',r'\overline F',r"\overline F'",r"\overline{F''}",'Two short downward tips are visible immediately under the right end of the bar.','cancel_bars',dc=True,kind='misread symbol or index',confidence='medium')
p.change('Cancelled first diagram, lower middle letter',r"G'",r"\overline G'",r"\deleted{F}G'",'The round replacement G crosses the straight upright and two bars of an older F; there is a prime and no separate overbar.','cancel_diagram',dc=True,kind='misread symbol or index',confidence='medium')
p.change('Cancelled first diagram, right barred bottom node',r'\overline G',r'\overline G',r"\overline{G''}",'Two separate short vertical ticks stand to the right of G below the end of the bar.','cancel_bars',dc=True,kind='misread symbol or index')
p.change('Cancelled first diagram, complete drawing','tikzcd','description','tikzcd with cancellation strokes','The two rows, U-shaped vertical signs, horizontal arrows, tildes, inclusions and four oblique cancellation strokes have been checked individually.','cancel_diagram',kind='drawing or diagram')
p.change('Proof opening, first inclusion',r"\unsure{F|F'}\subset\overline{F''}",r"F'\subset\overline F'",r"F\subset\overline F'",'The first F has blank space at upper right; the barred F has one separate raised tick.','proof_top',dc=True,kind='misread symbol or index',consequential='The first inclusion is literally unprimed F subset barred F prime.')
p.change('Proof opening, following subdivision',r"F''",r"\overline F'",r"F''",'There is no overbar above F; two raised tips follow it.','proof_top',kind='misread symbol or index')
p.change('Proof opening, Phi inclusion and following subdivision',r"\overline F'",r"\overline F''",r"\overline F'",'Both barred F occurrences in this clause show one prime.','proof_top',kind='misread symbol or index')
p.change('Proof opening, cancelled end','et que',r'\ill{}','et que','The short et and the q descender with ue remain readable beneath the line.','proof_top',kind=r'readable ink left as \ill{}',marked='yes')
p.change('Second diagram, arrow above F',r'\unsure{\overrightarrow F|\overline F}',r'\vec F in corrected note',r'\overrightarrow F','The raised horizontal stroke ends in a distinct rightward arrowhead.','diagram2',dc=True,dh=False)
p.change('Second diagram, full reproduction','tikzcd','descriptions, including corrected reading','tikzcd','Each live node and connector is visible; the upper tilde F and nearby connector are cancelled. The first horizontal sim connector has no secure terminal head.','diagram2',kind='drawing or diagram')
p.change('Proof, opening verb','prouver que',r'\ill{}','prouver que','The p descender, rou movement, v and er ending continue directly into que.','proof_mid',kind=r'readable ink left as \ill{}',marked='yes')
p.change('Proof, parenthetical insertion',r"(\deleted{\unsure{donc|dont}}\Phi\ll G')",r"(d'où\Phi\ll G')",r"(\deleted{\unsure{dont|donc}}\Phi\ll G')",'The old word is crossed; its final tall stroke favours dont but is covered by the deletion. A curved leader attaches the parenthesis after the inclusion in barred G prime.','proof_mid',dc=True,kind='insertion or placement',confidence='low')
p.change('Proof, transition abbreviation',r'\unsure{pour|i.e.|or}','i.e.','i.e.','The first short vertical has a dot; a second low e-like stroke follows the intervening point.','ie',dc=True,dh=False,confidence='medium')
p.change('Proof, cancelled element before que',r"\deleted{\unsure{\overline F'|G'}}",r'\ill{}',r"\deleted{\unsure{\overline F'|G'}}",'The straight stem and middle bar suggest F; the surrounding cancellation and curved lower trace prevent a secure reading.','old_element',kind=r'readable ink left as \ill{}',marked='yes',confidence='low')
p.change('Proof, relative clause opening','que tt élément','pour tt élément','que tt élément','The q descender and low ue precede two tall t stems.','proof_across',dc=True,kind='misread word',marked='yes')
p.change('Proof, underline of relative clause',r'\uline{qui raffine} G',r'\uline{qui raffine G}',r'\uline{qui raffine} G','The underline ends below raffine before the separate G.','proof_across',kind='other')
p.change('Proof, later preposition',r'\unsure{dans|ds}','dans','dans','A looped d and low ans sequence stand between est and the barred G.','proof_across',dc=True,dh=False)
p.change('Proof, induced adjective and underline',r'est \uline{induite par une}',r'\uline{est induit par une subd.}',r'\uline{est \unsure{induite|induit} par une} subd.','The underline begins beneath est and stops after une. The crowded terminal strokes of the adjective leave a possible e unresolved.','induite',dc=True,kind='other',confidence='low')
p.change('Proof, reference after corrigé','cf son cor.','cf. ci-con.','cf son cor.','After cf there is no separate point; the following s/on and separate cor with a final point are visible.','proof_across',kind='misread word')
p.change('Proof, intermediate formula',r"\overline F'\subset\widetilde F\xrightarrow{\sim}\overrightarrow F",'omitted',r"\overline F'\subset\widetilde F\xrightarrow{\sim}\overrightarrow F",'The full inclusion and arrow formula occupies the line between donc and the next donc.','formula_line',kind='omission',consequential='The proof explicitly writes barred F prime subset tilde F followed by a sim arrow to arrowed F.')
p.change('Proof, cancelled membership',r"X\in\unsure{\widetilde F'|\overline F'}",r'\ill{}',r"X\in\widetilde F'",'The crossed X, membership curve, straight F stem and middle bar remain; a small curved tilde is above F and one prime stands at the right.','cancel_membership',dc=True,kind=r'readable ink left as \ill{}',marked='yes',confidence='medium')
p.change('Proof, first subd. after tilde G','subd.',r'\struck{subd.} subd.','subd.','Only one run of the word is present; its opening strokes are retraced, without a separate cancelled occurrence.','proof_end',kind='text not on the page')
p.change('Proof, second subdivision abbreviation',r'\unsure{subd.}','subd.',r'\unsure{subd.}','The initial sub strokes survive but paper damage crosses the final letter and point.','subd_damage',confidence='low')
p.change('Third diagram','tikzcd','description','tikzcd','The four top nodes, three bottom nodes, horizontal sim arrows and three U-shaped vertical signs are visible.','diagram3',kind='drawing or diagram')
p.change('Final equation, cancelled opening letter',r'\deleted{\unsure{\Phi}}','omitted',r'\deleted{\Phi}','A loop with a vertical stem and horizontal base is crossed by an oblique line.','before_qed',dc=True,kind='omission',confidence='medium')
p.change('Final reference, l’ancien',r"l'ancien",r"\uncertain{l'ancien}",r"l'ancien",'The tall l and apostrophe are followed by ancien, whose last n is visible before Cont.','proof_end',dh=False)
p.change('Final reference, abbreviation',r'\unsure{Cont|Const|Compt}','Cont','Cont','The C opening, o/n group and final tall t are visible without a further s or mp group.','proof_end',dc=True,dh=False)
p.change('Enclosed cube, first cancelled node',r"\unsure{F'|G'}",'omitted',r"F'",'A straight stem and two rightward bars precede the raised prime.','cube',dc=True,kind='omission')
p.change('Enclosed cube, cancelled connector','single dash','omitted','dash plus oblique crossing line','Two distinct oblique lines join and cross the two abandoned top-left F labels.','cube',dc=True,kind='drawing or diagram')
p.change('Enclosed cube, vertical relations','hook arrows','vertical arrows','long U-ended lines','Four downward stems terminate in upward-curving right arms; the far-right stem has a second higher U-like ending. Their shape is retained in drawn paths.','cube',dc=True,kind='drawing or diagram')
p.change('Enclosed cube, lower right overwritten label','G','G',r'\substack{\unsure{\deleted{G}|G}\\G}','Two G-shaped curves occur one above the other. The upper curve is crossed by the lower stroke, but its deletion state is unresolved.','cube_g',dc=True,kind='omission',confidence='low')
p.change('Enclosed cube, full drawing','tikzcd','description','tikzcd with surrounding arc','The main nodes, sim arrows, hooked sloping connectors, partial vertical stroke, lower oblique inclusion signs, abandoned nodes and enclosing arc have been reproduced.','cube',kind='drawing or diagram')

for place,reading,why,crop in [
 ('Corollaire, cancelled quantifier','tout|toute|tt','The cancellation hides the final letter.','cor_old'),
 ('Corollaire, old letter','F','Older straight strokes lie under G.','cor_old'),
 ('Cancelled draft, preliminary labels',r'\Phi\subset\Phi|G\subset\Phi','Several letters overlap and are heavily crossed.','cancel_diagram'),
 ('Cancelled draft, first barred node',r"\overline F'",'Dense zigzag cancellation hides much of the letter and raised mark.','cancel_diagram'),
 ('Second diagram, cancelled connector',r'\subset|\swarrow','The sloping strokes overlap its curved end.','diagram2'),
 ('Inserted parenthesis, cancelled word','dont|donc','The last tall stroke and cancellation overlap.','proof_mid'),
 ('Before que tt élément',r"\overline F'|G'",'Straight and curved earlier traces survive beneath the strike.','old_element'),
 ('Induced adjective','induite|induit','The last low stroke may belong to t or to a following e.','induite'),
 ('Second subd. abbreviation','subd.','Paper damage covers the final letter and point.','subd_damage'),
 ('Cube, upper G at lower right',r'\deleted{G}|G','Two overlapping G shapes are visible but deletion is not secure.','cube_g')]:p.doubt(place,reading,why,crop)
p.inventory([
 ('text','top','Corollaire Sous les conditions précédentes'),('deletion','top statement','notion'),('insertion','above notion','relation'),('deletion','before figure','tout/toute/tt'),('insertion','above figure','Phi'),('deletion','under G','F'),('drawing','left of statement','vertical rule'),
 ('diagram','upper left','cancelled Phi and F/G diagram'),('deletion','first diagram','whole draft and preliminary labels'),('deletion','first diagram lower row','old F beneath G prime'),
 ('text','upper right','On utilise que F subset barred F prime'),('deletion','after subdivision hypotheses','et que'),
 ('diagram','middle left','Phi subset barred F prime; F prime; arrowed F; F'),('deletion','above second diagram','tilde F and connector'),
 ('text','right middle','On va prouver que'),('insertion','above Phi subset barred G prime','parenthesis Phi double chevron G prime'),('deletion','within inserted parenthesis','dont/donc'),('deletion','before il faut','et X'),('deletion','before que tt élément','barred F prime/G prime'),
 ('text','middle across','Mais barred F prime est induit(e)'),('display','below reference C4','barred F prime subset tilde F to arrowed F'),('deletion','after donc','X in tilde F prime'),('text','lower right','X in tilde G subd. de G'),
 ('diagram','lower left above cube','barred F prime subset tilde F to arrowed F to F'),('deletion','before final equation','Phi'),('display','lower right','X in barred F prime intersection tilde G equals barred G prime'),('text','right foot','qed ouf C’était l’ancien Cont 8'),
 ('diagram','bottom left','enclosed cube of relations'),('deletion','cube upper left','two F prime labels and connector'),('drawing','cube right lower label','upper G with uncertain deletion state'),('drawing','around cube','large arc')])
p.notation('U-ended vertical relation',r'\cup','A long vertical left stem turns upward at the right end; the cube stretches this same visible shape across rows.')
p.notation('barred double-prime labels in cancelled draft',r"\overline{F''},\overline{G''}",'Two small vertical tips lie immediately under the right end of each overbar.')
p.r['abbreviations']=[dict(abbreviation='ens',expansion='ensemble',evidence='Corollaire'),dict(abbreviation='subd.',expansion='subdivision',evidence='proof'),dict(abbreviation='tt',expansion='tout',evidence='que tt élément'),dict(abbreviation='cf',expansion='confer',evidence='C4 reference'),dict(abbreviation='cor.',expansion='corollaire',evidence='C4 reference'),dict(abbreviation='Cont',expansion='contrée / numbered condition label',evidence='l’ancien Cont 8')]
p.save()
