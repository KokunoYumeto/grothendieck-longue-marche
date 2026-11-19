import sys
sys.path.insert(0,'out/scripts')
from work import commit
R=[
('Vanishing theorem. Cas',r'Vanishing theorem.\tikz[overlay,x=1em,y=1ex]{\fill (-.75,-1.1) circle (.45pt);} Cas'),
(r'\inserted{\unsure{coh.|ch.} étale}',r'\tikz[baseline=(et.base)]{\node[inner sep=1pt] (et) {\inserted{ch. étale}};\draw (et.south west) .. controls +(0,-.1) and +(-.15,0) .. ([yshift=-3pt]et.south) -- ([yshift=-7pt]et.south) -- ([xshift=2pt,yshift=-3pt]et.south) .. controls +(.15,0) and +(0,-.1) .. (et.south east);}'),
(r'A/\unsure{I|J}', 'A/J'),
(r'$I$-adique',r'$J$-adique'),
(r'\unsure{Saavedra}', 'Saavedra'),
(r'\unsure{le|la}', 'le'),
(r'\unsure{memoire|mémoire}', 'memoire'),
(r'\unsure{Résolution|Résoluton}', 'Résolution'),
(r'\unsure{th|ths}', 'th'),
(r'\text{th de finitude pour morphisme}',r'\text{th de finitude pour \unsure{morphisme|morphismes}}'),
(r'\text{\inserted{de type fini}}',r'\text{\tikz[baseline=(fin.base)]{\node[inner sep=2pt] (fin) {\inserted{de type fini}};\draw ([yshift=-2pt]fin.north east) .. controls +(-.2,.05) and +(.2,0) .. (fin.north west) .. controls +(-.15,-.1) and +(-.1,0) .. (fin.south west) -- ([xshift=-8pt]fin.south east) .. controls +(.2,0) and +(0,-.1) .. (fin.north east);}}'),
(r'\text{Pureté cohomologique.}\\[.8ex]'+'\n'+r'\text{Changement de base régu}\overset{\text{\scriptsize\unsure{?}}}{\text{li}}\text{er}\\[-.3ex]'+'\n'+r'\qquad\text{\inserted{en cohomologie.}}',r'\text{Pureté cohomologique.}'),
(r'\end{tikzcd}}}',r'\end{tikzcd}}}'+'\n\n'+r'Changement de base régu\(\overset{\text{\scriptsize ?}}{\text{li}}\)er \inserted{en cohomologie.}'),
(r'\unsure{morphismes} affines.', 'morphismes affines.'),
(r'\unsure{1961|1962}', '1962'),
(r'\scriptsize$\unsure{\times|*}$',r'\scriptsize$\times$'),
(r'f:\unsure{X\'|X}',r'f:X'),
(r'\hspace{.4em}Sur une',r'\hspace{.4em}\inserted{1\textsuperscript{o}} Sur une'),
(r'\unsure{clos|clés}', 'clos'),
(r'\unsure{\tau|t}',r'\tau'),
]
# A raw quoted apostrophe is not wanted in the source-match string.
R=[(a.replace("X\\'|X", "X'|X"),b) for a,b in R]
L=[]
def a(p,c,h,f,ink,conf='high',ac=False,ah=True,k='other',mh='no',cons=None):
 d=dict(place=p,c=c,h=h,final=f,ink=ink,confidence=conf,against_c=ac,against_h=ah,kind=k,marked_in_H=mh)
 if cons:d['consequential']=cons
 L.append(d)
a('below theorem in item 20','omitted','omitted','small isolated dot below-left of the sentence point','dot20x16: separate black spot below and left of the brown full stop, with a clear paper gap; reproduced without assigning punctuation or mathematical meaning.','medium',True,True,'drawing or diagram')
a('item-number circles','circles 20,21,24','parenthesized numbers','circles 20,21,24, with cross at lower edge of 24','twenty4x, formula10x and margin24_upright8x/−20 degrees: closed loops around the numerals; the lower mark at 24 joins the boundary.','high',False,True,'drawing or diagram')
a('item 21 second exponent',r'\unsure{*|x}','*',r'\unsure{*|x}','secondstar22x: crossing legs are clear; the rightward stroke joins the opening parenthesis, preventing a secure count of the asterisk arms.','low',False,True,'misread symbol or index')
a('item 21 added abbreviation',r'\unsure{coh.|ch.}','coh.','ch.','cohetale14x: open c bowl followed directly by tall h stem and point; no independent o body.','medium',True,True,'abbreviation expanded or spelling modernised')
a('item 21 addition leader','addition without its leader','addition without its leader','ch. étale with curved lower brace and downward point before closing parenthesis','parenthesis7x/cohetale14x: line below the added words bends to a descending point in the gap after X and before the closing parenthesis.','high',True,True,'drawing or diagram')
a('item 21 closing parenthesis','closing ) present','closing ) omitted','closing ) present','parenthesis7x: long right-curving stroke beyond X, distinct from the lower leader and followed by a comma.','high',False,True,'omission')
a('item 21 second spectrum notation',r'\unsure{Spe|Spec|Sp}','Spec',r'\unsure{Spe|Spec|Sp}','specsecond14x: S and long p descender are clear, but the compressed horizontal continuation does not securely separate e and c. First Spec independently read in firstspec13x.','low',False,True,'misread word')
a('item 21 quotient ideal',r'\unsure{I|J}','J','J','specsecond14x: long vertical stroke has an upper bar and a lower hook curling to the left.','high',True,False,'misread symbol or index',cons='The written quotient ideal is J, also used in the following adic adjective.')
a('item 21 adic ideal','I','J','J','adique14x: upper bar, descending stem and left-curving foot match the quotient J.','high',True,False,'misread symbol or index',cons='C’s unmarked I-adique is changed to the ink’s J-adique.')
a('item 21 adic adjective','adique','adiquement','adique','adique14x: a/d/i/q/u/e ends in a long exit; no following m/e/n/t.','high',False,True,'abbreviation expanded or spelling modernised')
a('item 22 noun','catégorielles','catégories','catégorielles','categorielles15x: two consecutive tall l strokes follow the short ri/e bodies, then e/s.','high',False,True,'misread word')
a('item 22 first representation ending',r'\unsure{représentation|représentations}','représentations',r'\unsure{représentation|représentations}','rep1x14: the final n exit and a possible compressed s cannot be separated securely.','low',False,True)
a('item 22 group article','des groupes','de groupes','des groupes','twentytwo2x5: small terminal curl after e before the distinct gap and g descender supports the written s.','medium',False,True,'misread word')
a('item 22 proalgébriques deletion state','live','struck','live','proalg12x/fence3x: line near the lower letter strokes continues across almost the entire sheet as the section separator; no local cancellation of the word.','high',False,True,'deletion state (struck given live or live given struck)')
a('item 22 second representation ending',r'\unsure{représentation|représentations}','représentations',r'\unsure{représentation|représentations}','rep2x14: final n/possible s shares a compressed horizontal exit, so singular/plural remains unresolved.','low',False,True)
a('item 22 after gerbes','....','…','....','twentytwo3x6: four separate descending points before the smaller parenthetical addition.','high',False,True,'misread symbol or index')
a('item 22 added article',r'\unsure{le|la}','la','le','le22x: tall l followed by an open rightward e loop; no returning a oval. The literal phrase is à le théorie.','medium',True,True,'misread word')
a('item 22 addition placement','inserted parenthesis','ordinary inline parenthesis','inserted parenthesis','motifs9x/fence3x: smaller two-line writing occupies the lower right below gerbes; its closing parenthesis and point are visible.','high',False,True,'insertion or placement')
a('item 22 margin name',r'\unsure{Saavedra}','Saavedra','Saavedra','margin22_upright9x/−39 degrees: S/aa/v/e/d/r/a can be distinguished between travail and en train.','medium',True,False)
a('separator and Pour memoire','long open separator and underlined Pour memoire','Encadré : Pour mémoire','long open separator and underlined Pour memoire','fence3x/memoire9x: separator crosses above the heading, bends down at mid-page and continues beneath the right addition; no four-sided frame around the heading.','high',False,True,'drawing or diagram')
a('Pour memoire accent',r'\unsure{memoire|mémoire}','mémoire','memoire','memoire9x: clear paper over the first e beneath the separate upper rule; no acute accent.','medium',True,True,'abbreviation expanded or spelling modernised')
a('first two Pour memoire marks',r'\otimes twice','generic list bullets',r'\otimes twice','resol6x/purete8x: both initial marks have crossed diagonals within small ovals.','high',False,True,'drawing or diagram')
a('first Pour memoire noun',r'\unsure{Résolution|Résoluton}','Résolution','Résolution','resolword15x: short i stroke and its dot are visible between t and o.','medium',True,False)
a('scope and rendering of brace/arrows','brace includes Résolution, Pureté, and Changement de base','described brace joining first two items, two arrows','brace joins only Résolution and Pureté; two right double arrows drawn','brace12x/bracecontext3x: lower hook ends above Changement de base, touching the upper-right final r region; it does not descend beside that line. Each arrow has two shafts and a right head.','high',True,True,'drawing or diagram',cons='C incorrectly groups Changement de base inside the brace feeding the two conclusions; the brace covers the first two entries only.')
a('duality article','la top','le top.','la top','dual8x: after tall l the second letter closes as a; no point follows p before étale.','high',False,True,'misread word')
a('after étale','no punctuation','semicolon','no punctuation','dual8x: writing ends at étale without a separate point or descending semicolon mark.','high',False,True,'text not on the page')
a('finitude abbreviation',r'\unsure{th|ths}','th.','th','th25x: t and h with a terminal hook only, no independent s or abbreviation point.','medium',True,True,'abbreviation expanded or spelling modernised')
a('finitude noun','morphisme','morphismes',r'\unsure{morphisme|morphismes}','morphend18x: final m/e and the terminal return at the right edge are compressed; an independent final s cannot be ruled in or out.','low',True,True)
a('de type fini enclosure','addition without enclosure','addition without enclosure','added de type fini in a long rounded enclosure','finiinsert14x/bracecontext3x: long top line, rounded left descent, lower horizontal return and upturned right hook enclose the added phrase.','high',True,True,'drawing or diagram')
a('finitude continuation','etc etc','etc. etc.','etc etc','finitude9x: both etc groups end with letter exits, without separate points.','high',False,True,'text not on the page')
a('above régulier',r'\unsure{?}','omitted','raised ?','basemark15x/bracecontext3x: upper curved hook and lower point stand above the li region, distinct from the word body.','medium',True,True,'omission')
a('Dimension cohomologique noun',r'\unsure{morphismes}','morphismes','morphismes','dimension5x: m/o/r/p/h/i/s/m/e/s recognizable, including p descender and h ascender before the dotted i.','medium',True,False)
a('Grauert entry noun',r'\unsure{Théorème|Théorèmes}','Théorèmes',r'\unsure{Théorème|Théorèmes}','theoreme14x: last m/e strokes and a possible s are confluent; cannot settle number from the ending.','low',False,True)
a('Grauert and rigid-analytic initial marks',r'\otimes twice','generic list bullets',r'\otimes twice','grauert6x/rigid7x: small circles contain two crossing diagonals.','high',False,True,'drawing or diagram')
a('rigid-analytic cancelled fragment',r'\deleted{\unsure{rig|rigide}}',r'\struck{\ill}',r'\deleted{\unsure{rig|rigide}}','oldrig24x: r shoulder, dotted i and g descender remain visible; the continuation under hatching is uncertain.','low',False,True,r'readable ink left as \ill{}','yes')
a('SGA year',r'\unsure{1961|1962}','1962','1962','date20x: final numeral has upper arch and long curved lower foot continuing right; not a straight 1.','high',True,False)
a('rule below SGA heading','drawn curved rule','omitted','drawn curved rule','lowerline3x: continuous long stroke runs left to right and rises gradually toward its right endpoint.','high',False,True,'drawing or diagram')
a('item 23 lower mark',r'\unsure{\times|*}','omitted',r'\times','mark23x20: four distinguishable diagonal arms; no extra asterisk ray.','medium',True,True,'drawing or diagram')
a('item 23 Schémas capitalization','Schémas','schémas','Schémas','twentythree1x5: tall upper and lower S curves rise above the following lowercase c.','high',False,True,'abbreviation expanded or spelling modernised')
a('item 23 cancelled abbreviation',r'\deleted{\unsure{qq|qcq}}','omitted',r'\deleted{\unsure{qq|qcq}}','oldreg16x: lower q descenders are visible beneath several local strike lines; intervening c cannot be securely distinguished.','low',False,True,'omission')
a('item 23 article',r'\unsure{des|de}','des',r'\unsure{des|de}','descycles12x: a horizontal terminal stroke may include s or simply extend e; the difference remains unresolved.','low',False,True)
a('item 23 before cycles',r'\unsure{,}','no comma',r'\unsure{,}','descycles12x: pale small curve below the interval after the article may be a comma; kept as a single-reading doubt.','medium',False,True,'misread symbol or index')
a('item 23 domain symbol',r'\unsure{X\prime|X}','X','X','fmap14x: upper-right arch is continuous with the descending right arm of X; no independent prime stroke.','medium',True,False,'misread symbol or index')
a('item 24 initial subdivision','omitted',r'1\textsuperscript{o}',r'\inserted{1\textsuperscript{o}}','order22x/all24x5: gray sloping 1 with a separate small raised o before Sur, written in the same faint hand as the margin note.','high',True,False,'omission')
a('item 24 dimension','3',r'\ill','3','all24x5/dim3x18: upper and lower right-facing numeral curves at the edge are visible; lower part supplied by the uncropped all24 view.','high',False,True,r'readable ink left as \ill{}','yes')
a('item 24 abbreviated adjective',r'\unsure{algébriqmt|algébriquemt|algébriquement}','algébriquement',r'\unsure{algébriqmt|algébriquemt|algébriquement}','algclos14x/all24x5: middle q descends clearly; following strokes form an unusually compressed horizontal run, leaving the amount of abbreviation unresolved.','low',False,True,'abbreviation expanded or spelling modernised')
a('item 24 field adjective',r'\unsure{clos|clés}','clos','clos','algclos14x: open c, tall l, round o and final s; no accent above o.','medium',True,False)
a('item 24 equivalence symbol',r'\unsure{\tau|t}',r'\ill',r'\tau','tau_actual20x: flat long top bar with short downward stem and curved right foot, no ascender above the bar.','medium',True,True,r'readable ink left as \ill{}','yes')
a('item 24 small addition placement','inserted En dim 4 …','ordinary continuation','inserted En dim 4 …','note24x12/all24x5: two small lines beneath the main num. équiv. text at the lower right.','high',False,True,'insertion or placement')
a('item 24 added cycle ending','cycle','cycles','cycle','note24x12: looped final e exits directly into the gap before de; no separate s body.','medium',False,True,'misread word')
a('item 24 after dim 2','no comma','comma','no comma','note24x12: numeral 2 ends before the next line without an independent comma.','high',False,True,'text not on the page')
a('item 24 equality','= ',r'\approx','= ','note24x12: two straight horizontal strokes, without the undulating shapes of approximation.','high',False,True,'misread symbol or index',cons='The added question writes equality of numerical and homological equivalence, not an approximation sign.')
a('item 24 abbreviated equivalences','num and hom without points','num. and hom.','num and hom without points','note24x12/end24x22: after each final m, only the ordinary exit and then the next sign; points occur after équiv., not after num or hom.','high',False,True,'abbreviation expanded or spelling modernised')
a('item 24 question marks','??','?','??','end24x22: two separate upper hooks, each with its own lower point.','high',False,True,'omission')
a('item 24 last small mark',r"\unsure{,|'}",'omitted',r"\unsure{,|'}",'end24x22: short curved mark to the right of both question hooks; its punctuation position is ambiguous.','low',False,True,'omission')
a('item 24 margin ending',r'question 1\textsuperscript{o}',r'\ill',r'question 1\textsuperscript{o}','margin24_upright8x/−20 degrees and margin24end_upright12x/−31 degrees: q descender, compressed u/e/s across the circle, t stem, dotted i and o/n return, then separate 1 with raised o.','medium',False,True,r'readable ink left as \ill{}','yes')
I=[]
def i(k,p,t):I.append(dict(kind=k,position=p,text=t))
i('drawing','upper left','circle around 20')
i('text','item 20','Vanishing theorem. Cas des espaces homogènes.')
i('drawing','below theorem','isolated black dot')
i('drawing','left item 21','circle around 21')
i('display','item 21 opening','H^*(X,F) → H^{*|x}(X_0,F_0)')
i('text','item 21',"X_0 fermé dans X … quand est-ce un isom ? Suffit-il que ce soit vrai en dim 0 ? Cas X=Spec A … J-adique séparé complet … localisation étale … X affine.")
i('insertion','above end of item 21 parenthesis','ch. étale')
i('drawing','under ch. étale','curved brace with downward insertion point after X')
i('text','item 22','Structure des catégorielles abéliennes … représentations? … groupes proalgébriques … gerbes....')
i('margin note','left item 22, slanted','travail Saavedra en train')
i('insertion','lower right item 22','(préliminaire algébrique à le théorie des motifs).')
i('drawing','below item 22','long curved section separator with central downward bend')
i('text','below separator','underlined Pour memoire')
i('diagram','Pour memoire, first two rows','⊗ Résolution des singularités.; ⊗ Pureté cohomologique.; shared right brace and two double right arrows to dualité locale = bidualité, pour la top étale and th de finitude pour morphisme|morphismes, etc etc')
i('insertion','beneath finitude clause','de type fini')
i('drawing','around de type fini','long rounded enclosure with bent right hook')
i('text','below brace','Changement de base régulier')
i('insertion','above li of régulier','?')
i('insertion','below Changement de base','en cohomologie.')
i('text','next line','Dimension cohomologique des morphismes affines.')
i('text','middle lower entry','⊗ Théorème|Théorèmes de finitude genre Grauert.')
i('text','next entry','⊗ Théories type rigide-analytiques.')
i('deletion','between Théories and type','rig|rigide')
i('text','lower heading','Questions dans SGA 1962')
i('drawing','below SGA heading','long rule rising to the right')
i('text','item 23','Théorie de Chow pour Schémas … ayant un faisceau inversible ample … L’image inverse par f:X→Y doit être définie, sous seule condition que Y soit régulier.')
i('drawing','below numeral 23','small cross')
i('deletion','after Schémas','qq|qcq réguliers')
i('drawing','left item 24','circle around 24 and cross at lower edge')
i('margin note','left/below item 24, slanted','Réponse négative Griffiths pour question 1°')
i('insertion','before Sur in item 24','1°')
i('text','item 24','Sur une variété projective lisse connexe de dim 3 … k corps algébriqmt|algébriquemt|algébriquement clos … 1-cycle num. équiv. à 0 … τ-équivalent à zéro ?')
i('insertion','bottom right','En dim 4, cycle de dim 2 équiv. num = équiv. hom ?? followed by uncertain comma/apostrophe')
commit(66,4,dict(replace=R,changes=L,inventory=I,sheet_kind='text',hand='his hand',observations='Whole then both halves personally viewed before C/H. All base decision crops and the three rotated margin crops personally viewed, with adaptive firstspec, all24, bracecontext, dot20, tau_actual and dim3. The first tau crop was misplaced and superseded. The narrow dim3 crop cuts its bottom, read fully in all24. All agreed text, accents, numbers, plain mathematical letters and zero indices, the arrow and inclusion, cancellations, additions, punctuation and rules checked. No watermark visible; archive numeral 3 stays comment only. H editorial historical note is not manuscript text. Not a second audit or mathematical check.'))
