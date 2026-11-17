from author import Page
p=Page('156-4',18)
p.replace('\\cotefile{156-4}\n','')
p.replace(r'\unsure{contrée}','contrée')
p.replace(r'\unsure{F_{el}|F_{\mathrm{el}}}',r'\mathcal{F}_{el}')
p.replace('$F_{el}$',r'$\mathcal{F}_{el}$')
p.replace(r'\unsure{réflexive} symétrique',r'\unsure{reflexive|réflexive} \unsure{symetrique|symétrique}')
p.replace(r'\unsure{R|\mathcal{R}}',r'\mathcal{R}')
p.replace(r'\unsure{familles|famés}',r'\unsure{formées|familles|famés}')
p.replace('deux à deux compatibles','deux : deux compatibles')
p.replace('Satisfaisant à des axiomes','Satisfaisant : des axiomes')
p.replace(r'\unsure{parmi|pour}','parmi')
p.replace(r'\deleted{\unsure{Z}}X',r'\deleted{\unsure{Z|F}}X')
p.replace(r'\unsure{pose}','pose')
p.replace(r'\unsure{Figs|Fig}','Fig')
p.replace(r'\Longleftrightarrow',r'\Longleftarrow')
p.replace(r"\unsure{X|X'},\unsure{X'|X''}","X,X'")
p.replace('sont compatibles à $X$','sont compatibles : $X$')
for old,new in [(r'\unsure{partie}','partie'),(r'\unsure{configuration}','configuration'),(r'\unsure{une}','une'),(r'\unsure{si}','si'),(r'\unsure{propriété}','propriété'),(r"\unsure{d'être}","d'être")]:
    p.replace(old,new)
p.change('opening noun','contrée?','contrée','contrée','Initial c, nt cluster, tall r/t and final ée; underlined as a unit.','top',dc=True,dh=False)
p.change('opening end','par','par la [donnée inserted] [ill]','par','The baseline ends with par; nearby small words follow the oblique margin baseline.','top',kind='insertion or placement')
for place,crop in [('1°, family alphabet','top'),('4°, family alphabet','mid')]:
    p.change(place,'F_el (first occurrence uncertain alphabet/index)','fraktur F_él',r'\mathcal{F}_{el}','Sweeping upper bar with lower hook; small el has no distinct acute.','top' if crop=='top' else 'mid',dc=True,kind='misread symbol or index',confidence='medium')
p.change('2°, purported deleted ≤','none in body','deleted ≤','≤ in oblique NB','The ≤ aligns with the rising small margin writing and is not struck; body has live <<.','slant',kind='insertion or placement',consequential='H relocates the margin ≤ into the refinement clause as a cancellation.')
p.change('2°, cancelled symbol',r'\deleted{\unsure{β|b}}','deleted ill',r'\deleted{\unsure{β|b}}','A tall looped stem and two overdrawn lobes remain under cancelling strokes.','top',kind='readable ink left as \\ill{}',confidence='low',marked='yes')
p.doubt('2°, cancelled symbol','β|b','Loops cannot securely distinguish the alternatives','top',confidence='low')
for word in ['reflexive','symetrique']:
    old={'reflexive':'réflexive?','symetrique':'symétrique'}[word]
    alt={'reflexive':'réflexive','symetrique':'symétrique'}[word]
    p.change('3°, '+word,old,alt,word+'|'+alt,'Letters readable; a distinct acute is not separated from adjacent strokes.','top',dc=True,kind='abbreviation expanded or spelling modernised',confidence='medium')
    p.doubt('3°, '+word,word+'|'+alt,'Accent state remains uncertain','top')
p.change('3°, relation alphabet','R|calligraphic R','calligraphic R',r'\mathcal{R}','Curved upper loop and long swash lower return.','top',dc=True,dh=False,confidence='medium')
p.change('3°, cancelled word','admissibles|admissibilité|constructibles','word biffé only','admissibles|admissibilité|constructibles, deleted','Long crossing stroke obscures medial letters; initial a-like loop and final rising strokes survive.','top',kind='omission',confidence='low')
p.doubt('3°, cancelled word','admissibles|admissibilité|constructibles','Cancellation prevents secure reading','top',confidence='low')
p.change('3°, article','parmi figures élémentaires','parmi [les inserted] figures élémentaires','parmi figures élémentaires','Gap after parmi contains no independent les insertion.','top',kind='text not on the page')
p.change('NB, initial clause','Il revient au = de se donner 4°), ou de se donner la notion de figure','ill fragments','Il revient au = de se donner 4°), ou de se donner la notion de figure','Rotated writing gives two-bar =, donner twice, and underlined figure.','margin',kind='readable ink left as \\ill{}',marked='yes')
p.change('NB, deletion before configuration','partie? deleted','omitted','partie deleted','Crossed p descender followed by artie; the cancellation lies through the word.','margin',dc=True,kind='omission',confidence='medium')
for word,crop in [('configuration','margin'),('une','marginwide'),('si','marginwide'),('propriété','margin'),("d'être",'margin')]:
    p.change('NB, '+word,word+'?','ill fragments',word,'Small oblique letters remain separable when rotated; surrounding body ink follows another baseline.','margin' if crop=='margin' else 'marginwide',dc=True,kind='readable ink left as \\ill{}',marked='yes',confidence='medium')
for word,crop in [('même','slant'),('chaque|toute','marginwide'),('contient (first)','marginwide'),('contient (second)','marginwide'),('aussi','marginwide'),('toute','slant'),('figure','slant'),('englobe|engendre|contient','slant')]:
    p.change('NB, '+word,word+'?','ill fragments',word+'?','Oblique word is crossed by the larger body writing; candidate retained without silently resolving the joins.','slant' if crop=='slant' else 'marginwide',kind='readable ink left as \\ill{}',marked='yes',confidence='low')
    p.doubt('NB, '+word,word,'Letter joins remain obscured by crossing body strokes',crop,confidence='low')
p.change('4°, item beginning','4°) Un ens de parties|partie','4°? [ill] un antifiltre dans? l’ens. des parties','4°) Un ens de parties|partie','Number 4 and degree loop are clear; line reads Un ens de with no antifiltre; final s of parties remains compressed.','mid',kind='misread word',marked='yes',confidence='medium')
p.doubt('4°, parties ending','parties|partie','Final small stroke does not settle the s','mid')
p.change('4°, name before finies','les ---? finies','loc. « finies? »','les ---? finies','After les a long horizontal dash precedes finies; no loc. or opening quotation marks are separable.','mid',kind='misread word',confidence='medium',marked='yes')
p.doubt('4°, blank name','---','Long line is retained as a doubtful blank or dash','mid')
p.change('4°, finite contrée','d’une contrée? finie','de nos contrées finies','d’une contrée finie','Single une and singular endings; contrée has tall t and final ée.','mid',dc=True,kind='misread word')
p.change('4°, after configurations','ou?','omitted','ou?','Small low joined strokes after closing quotation marks remain visible.','mid',kind='omission',confidence='low')
p.doubt('4°, connector','ou','Small mark adjoining the quotation marks remains ambiguous','mid',confidence='low')
p.change('4°, after i.e.','familles|famés','formées','formées|familles|famés','Long f loop followed by low joined humps and accented terminal ées; no clear pair of tall l stems.','familyword',dc=True,dh=False,confidence='medium')
p.doubt('4°, after i.e.','formées|familles|famés','Low internal joins retain some ambiguity','familyword')
p.change('4°, pairwise phrase','deux à deux','deux à deux','deux : deux','Two detached vertically placed dots stand between the two occurrences of deux.','mid',dc=True,kind='abbreviation expanded or spelling modernised')
p.change('axioms, connector','Satisfaisant à des','satisfaisant à des','Satisfaisant : des','Two detached marks and no a bowl after Satisfaisant.','lower',dc=True,kind='abbreviation expanded or spelling modernised')
p.change('axioms, noun','axiomes','conditions','axiomes','Initial a, x diagonals and final mes lie on the body baseline.','lower',kind='misread word')
p.change('axioms, pronoun','celui-ci','celle-ci','celui-ci','Low u/i sequence before hyphen, rather than double l/e.','lower',kind='misread word')
p.change('condition heading','Contr|Cond','Contr','Contr|Cond','Final letters overlap the following raised cancellation and numeral 1.','lower',dh=False,confidence='medium')
p.doubt('condition heading','Contr|Cond','Last heading strokes remain overlaid','lower')
p.change('condition, first Si','deleted Si then Si','Si','deleted Si then Si','Raised first Si is crossed; second Si on baseline remains live.','condition',kind='deletion state (struck given live or live given struck)')
p.change('condition, parmi','deleted p? parmi|pour','Soient inserted','deleted p? parmi','Initial p is overtraced; following armi ends in a dotted i; word follows baseline Si.','condition',dc=True,kind='misread word',confidence='medium')
p.doubt('condition, deleted p','p','Small overwritten initial remains uncertain','condition')
p.change('condition, first figure','deleted Z? X','bold X','deleted Z|F then X','Crossed diagonals overlie a short crossbar and upright; the abandoned letter remains uncertain.','lower',dc=True,kind='deletion state (struck given live or live given struck)',confidence='low')
p.doubt('condition, abandoned letter','Z|F','Overdrawing leaves both angular and F-like traces','lower',confidence='low')
p.change('condition, pose','pose?','pose?','pose','Long p descender followed by connected ose.','lower',dc=True,dh=False)
p.change('property label','Figs|Fig','Fig','Fig','The final descending loop is g; no independent s follows it.','bottom',dc=True,dh=False)
p.change('property insertion','et si X|X′, X′|X″','et Fig₂ or Fig₁,₂','et si X, X′','Small et si and two diagonal X glyphs sit above sont; first has no prime and second has one.','bottom',dc=True,kind='misread symbol or index',consequential='The inserted pair is X,X′, preserving the manuscript’s index sequence.')
p.change('bracket line, direction','Longleftrightarrow','Longleftrightarrow','Longleftarrow','Two parallel shafts meet a left head; right ends are blunt before a separate curved parenthesis.','arrow',dc=True,kind='misread symbol or index',consequential='The manuscript writes a leftward implication arrow; both witnesses give an equivalence arrow.')
p.change('bracket line, connector','compatibles à X','compatibles à X','compatibles : X','Two detached dots follow compatibles, without an a bowl.','bottom',dc=True,kind='abbreviation expanded or spelling modernised')
p.change('left emphasis strokes','three vertical strokes','double vertical stroke','three vertical strokes','Three separate slightly bowed strokes alongside the bracketed line.','bottom',kind='misread symbol or index')
p.change('small margin, compactness','contrée finie ou plutôt compacte : celle où toute figure est finie','contrée finie … plutôt configuration … figure …','contrée finie ou plutôt compacte : celle où toute figure est finie','Rotated note has compact c/o/m/pacte sequence and separate underline; full final clause is legible.','margin',kind='readable ink left as \\ill{}',marked='yes')
p.inventory([
('text','header','17'),('text','opening','Une contrée est définie par'),('text','1°','Un ensemble de figures élémentaires'),
('text','2°','Une relation d’ordre'),('deletion','2°, after <<','β|b'),('text','3°','Une relation reflexive symetrique'),
('deletion','3°, parenthesis','admissibles|admissibilité|constructibles'),('insertion','3°, above deletion','compatibilité'),
('margin note','oblique across upper half','NB Il revient au ='),('deletion','NB before configuration','partie'),
('text','4°','Un ens de parties'),('margin note','left of 4°','contrée finie ou plutôt compacte'),
('text','axioms paragraph','Satisfaisant : des axiomes'),('text','condition heading','Contr|Cond 1'),
('deletion','condition start raised','Si'),('text','condition premise','Si parmi deux fig. élémentaires'),('deletion','before parmi','p'),
('deletion','first figure glyph','Z|F'),('display','definition','X′ ≤ X ssi (déf) X′ << X'),
('text','after definition','alors on trouve une relation d’ordre'),('text','next paragraph','De plus, en termes de cette relation'),
('text','property label','Fig 1'),('margin note','left bracket line','three vertical strokes'),
('text','bracket clause','Longleftarrow Si X′,X″ << X'),('insertion','above sont','et si X,X′'),
('text','last line','Fig₂ (dim combinatoire finie) On va')])
p.notation('implication direction',r'\Longleftarrow','Two parallel shafts, left arrowhead only; closing parenthesis separate')
p.notation('two-dot abbreviation for à',':','Two detached vertical points in trois connectors; preserved literally')
p.r['abbreviations']=[{'abbreviation':a,'expansion':e,'evidence':'Visible on scan 018'} for a,e in [('ens','ensemble'),('él.','élémentaire(s)'),('tps','temps'),('fig.','figure(s)'),('ssi','si et seulement si'),('déf','définition'),('comp.','compatibles'),('dim','dimension')]]
p.save()
