from author import Page
import re
p=Page('156-4',21)
p.replace(r'\unsure{L|\mathcal{L}}','L')
p.text=re.sub(r'(?<![A-Za-z])L(?![A-Za-z])',lambda m:r'\mathcal{L}',p.text)
p.replace(r'\widehat \mathcal{L}',r'\widehat{\mathcal{L}}')
p.replace(r'\unsure{\mathcal P|P}',r'\mathcal P')
p.replace(r'\unsure{Itou|Alors}','Itou')
p.replace(r'\unsure{\mathcal F|F}',r'\mathcal F')
p.replace(r'\unsure{,|.|{}_{e}}\subset',r'\unsure{,|.|{}_{e}}\in')
p.replace(r'\unsure{en|on} \unsure{posant|poserait}','en posant')
p.replace(r'\unsure{\subset|\in}',r'\in')
p.replace(r'\unsure{Soient|tout}','Soient')
p.replace(r'\unsure{soient}',r'\unsure{faut-il|soient}')
p.replace(r'\unsure{Si}','Si')
p.change('opening, agreement','Pour toute','Pour tout','Pour toute','Final e-like return after the tall t remains before multistrate.','top',kind='misread word',confidence='medium')
p.change('opening L alphabet','L|calligraphic L','calligraphic L',r'\mathcal{L}_X','Curved tall stem and looped lower return.','top',dc=True,dh=False,confidence='medium')
p.change('inserted powerset','calligraphic P|P','fraktur P',r'\mathcal P','Straight stem with broad flag-shaped bowl and a small lower return.','top',dc=True,kind='misread symbol or index',confidence='medium')
p.change('opening abbreviation/deletion','l’ens live','l’ens. deleted','l’ens live','Curved leader attaches the insertion above l’ens; it does not cancel the low ens letters, and no terminal dot follows.','top',kind='deletion state (struck given live or live given struck)')
for place,crop in [('insertion, ambient L','top'),('left margin hat L','leftmark'),('first body hat L','top'),('second body hat L','top'),('L_Y in family','top'),('first map image','maps'),('figure definition L_F','figures'),('union L_F','figures'),('union L_X','figures'),('union target L','figures'),('family hat L_F','figures'),('family member L_X','figures'),('family powerset target L','figures'),('iterated powerset L','figures'),('last map image','lower')]:
    p.change(place,'L alphabet','calligraphic L',r'\mathcal{L} with source indices/decorations','Stem curves into a lower loop; indices and hat positions remain those visible in the cited crop.','leftmark' if crop=='leftmark' else crop,dc=True,dh=False,confidence='medium')
p.change('cancelled glyph before L_Y','X|Y?','ill','X|Y?, deleted','Angular crossing strokes remain beneath a scribbled cancellation.','top',kind='readable ink left as \\ill{}',confidence='low',marked='yes')
p.doubt('cancelled glyph before L_Y','X|Y','Crossing obscures the original angular letter','top',confidence='low')
p.change('reconstitution verb','réconstituer','reconstituer','réconstituer','Small detached stroke is visible over the initial e area.','maps',kind='abbreviation expanded or spelling modernised',confidence='medium')
for place,crop in [('prose ambient M','maps'),('first map domain M','maps'),('figures ambient M','figures')]:
    p.change(place,'M','calligraphic M','M','Two pointed humps and an initial curved entry; retained as the recurring M glyph.','maps' if crop=='maps' else 'figures',kind='misread symbol or index',confidence='medium')
for place,crop in [('first powerset X','top'),('first iterated powerset','top'),('map iterated powerset','maps'),('figures powerset M','figures'),('family powerset L','figures'),('family iterated powerset L','figures'),('last iterated powerset X','lower')]:
    p.change(place,'calligraphic P','fraktur P',r'\mathcal P','Repeated broad angular bowl/flag on a long straight stem; recorded consistently with the inserted occurrence.','top' if crop=='top' else crop,kind='misread symbol or index',confidence='medium')
p.change('first cancelled condition heading','Contr|Cond','Contr','Contr|Cond, deleted','Underlined heading has a tall crossed final stem but the cancellation obscures its ending.','figures',confidence='low')
p.doubt('first cancelled condition heading','Contr|Cond','Ending remains hidden by diagonal scribbling','figures',confidence='low')
p.change('figure paragraph opening','Itou|Alors','Notons que','Itou','Tall I loop and t crossbar precede low ou; one word only.','figures',dc=True,kind='misread word')
p.change('figure family alphabet','calligraphic F|F','calligraphic F',r'\mathcal F','Long upper bar and hooked base, matching the family-form F.','figures',dc=True,dh=False,confidence='medium')
p.change('mark after figure family','comma|dot|subscript e','omitted','comma|dot|subscript e','Small low filled hook between F and the relation; retained without assigning a secure function.','figures',kind='omission',confidence='low')
p.doubt('mark after figure family',',|.|subscript e','Tiny low loop remains ambiguous','figures',confidence='low')
p.change('figure-family relation','subset','subset','in','Thick open curved sign contains an interior middle bar as well as top and bottom strokes.','figures',dc=True,kind='misread symbol or index',confidence='medium',consequential='The figure-family line reads membership in P(M), with the small preceding mark still doubtful.')
p.change('figure parenthesis','(ens des figures)','sous-ens.? figures','(ens des figures)','Opening parenthesis followed by short ens and des; figures continues on next baseline.','figures',kind='misread word',marked='yes')
p.change('definition introduction','en|on posant|poserait','on pose','en posant','Low open e/n and p/o/s/a/n/t with final tall t, before the display.','figures',dc=True,kind='misread word',confidence='medium')
p.change('cancelled assignment','hat F mapsto|F mapsto','ill','hat F mapsto|F mapsto, deleted','Tall F-like stem and curling rightward arrow survive; small mark above stem is overdrawn.','figures',kind='readable ink left as \\ill{}',confidence='low',marked='yes')
p.doubt('cancelled assignment','hat F mapsto|F mapsto','Overdrawn upper mark remains uncertain','figures',confidence='low')
p.change('cancelled mark above L_F','wedge?','omitted','wedge?, deleted','Small angled mark directly above the L stem is scribbled across.','figures',kind='omission',confidence='low')
p.doubt('cancelled mark above L_F','wedge','Small crossed angular mark cannot be fully recovered','figures',confidence='low')
for place in ['first L_F subscript','definition ending F','union L_F subscript','union index X in F','family L_F subscript','family membership X in F','last map source F','last map image subscript F']:
    p.change(place,'F','calligraphic F','F','Straight central stem and two short bars, retained as the figure-form F; no extra index is supplied.','lower' if place.startswith('last') else 'figures',kind='misread symbol or index',confidence='medium')
p.change('union result relation','subset|in','in','in','Curved left stroke contains a clear middle bar.','figures',dc=True,dh=False,consequential='Union line retains the written membership sign before L.')
p.change('first powerset membership state','in P(L), live; then i.e. in P(P(L))','in P(L) described as corrected','in P(L), live; then i.e. in P(P(L))','First membership and P(L) have no cancelling stroke; the next line begins i.e.','figures',kind='deletion state (struck given live or live given struck)',consequential='Both written target formulas remain live in the consolidated text.')
p.change('isolated cancelled word before lower heading','Soient|tout','omitted','Soient, deleted','Long initial S stroke and low oient sequence under a horizontal cancellation.','lower',dc=True,kind='omission',confidence='medium')
p.change('lower condition label','a)|i)','a)','a)|i), deleted','Small curved label is traversed by two long cancellation lines.','lower',confidence='low')
p.doubt('lower condition label','a)|i)','Cancellation conceals the small first character','lower',confidence='low')
p.change('lower condition auxiliary','soient?','faut-il, deleted','faut-il|soient, deleted','Tall f-like stem followed by low au/t and a later upright under the strike; word remains partly obscured.','oldword',dc=True,dh=False,confidence='medium')
p.doubt('lower condition auxiliary','faut-il|soient','Horizontal cancellation and the descender of que cross the word','oldword')
p.change('last cancelled block, Si','Si?','Si, deleted','Si, deleted with block','S-shaped loop and short following i remain under the diagonal stroke.','lower',dc=True,dh=False,confidence='medium')
p.change('last cancelled block, label','a)','omitted','a)','Small a bowl and closing parenthesis at the left before Supposons.','lower',kind='omission')
p.change('last cancelled word','consi|aussi|on','ill','consi|aussi|on, deleted','Several low rounded letters ending in an i-like stroke survive but are heavily overwritten.','lower',kind='readable ink left as \\ill{}',confidence='low',marked='yes')
p.doubt('last cancelled word','consi|aussi|on','Double tracing and oblique cancellation hide the first letters','lower',confidence='low')
p.inventory([
('text','header','20'),('deletion','opening above Pour','toute'),('text','opening','Pour toute multistrate X'),('insertion','above l’ens','in P(L)'),('margin note','left of hat definition','hat L_X'),
('display','first hat definition','hat L_X subset P(X), i.e. in P(P(X))'),('text','family description','l’ensemble des L_Y'),('deletion','before L_Y','X|Y'),('deletion','end parenthesis','Considérons'),('deletion','next line beginning','les'),
('text','reconstitution','J’aimerais réconstituer les structures'),('display','first map','X mapsto hat L_X; M to P(P(X))'),('deletion','before Itou','Contr|Cond 3'),('text','figure paragraph','Itou pour family F'),
('deletion','before L_F definition','hat F mapsto|F mapsto'),('deletion','above L_F','wedge'),('display','figure definition','L_F = ens des lieux'),('display','union','L_F = union L_X in L'),('display','family','hat L_F = {L_X | X in F} in P(L)'),
('text','family qualification','i.e. in P(P(L))'),('text','mapping introduction','qui nous donne'),('display','last map','F mapsto hat L_F; family F to P(P(X))'),
('deletion','isolated word below map','Soient'),('deletion','lower heading and premise','Contr₃ a)|i) Pour que X << Y faut-il|soient X,Y in'),('deletion','last abandoned block','Soient X,Y deux multistrates; a) Supposons')])
p.notation('lieux glyph',r'\mathcal{L}','Tall curved stem, looped base; hat drawn separately and often thickly retraced')
p.notation('powerset glyph',r'\mathcal P','Long stem with broad angular flag-shaped bowl and short lower return')
p.r['abbreviations']=[{'abbreviation':a,'expansion':e,'evidence':'Visible on scan 021'} for a,e in [('ens','ensemble'),('i.e.','id est'),('comp.','compatibilité')]]
p.save()
