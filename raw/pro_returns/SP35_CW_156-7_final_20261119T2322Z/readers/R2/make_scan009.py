from pathlib import Path
from datetime import datetime, timezone
import json
root=Path('/workspace/scratch/2b715fe259c4/SP35_CW_156-7/readers/R2')
manifest=json.loads((root/'scan009_crops.json').read_text())
cm={Path(x['file']).stem.replace('scan009_',''):x for x in manifest}
comp=r'\mathrel{\tikz[baseline=-.4ex,x=.65em,y=.65em]{\draw (0,1.1)--(1,.5)--(0,-.1) (1,1.1)--(0,.5)--(1,-.1);}}'
hashsign=r'\mathrel{\tikz[x=.55em,y=.60em,line cap=round]{\draw (0,-.12)--(0,1) (.48,-.12)--(.48,1) (-.06,.30)--(.54,.47) (-.05,.51)--(.53,.65);}}'
rounded=r'\mathrel{\tikz[x=.55em,y=.55em,line cap=round]{\draw (0,.14)--(1.25,.14) (0,.39)--(1.25,.39);\draw (1.43,.57)..controls(1.64,.50)and(1.74,.10)..(1.71,-.02)..controls(1.64,-.11)and(1.50,-.11)..(1.39,-.09);}}'
tex=r'''\scanpage{9}\mspage{8}
J'explicite, à cause de son importance, la propriété suivante, bien qu'elle sera conséquence de diverses façons d'autres

% The upper At DC1 / Cor1 / Cor2 draft is cancelled globally. Local earlier
% alterations are separately represented inside that cancelled text.
\deleted{\uline{At} DC 1 : Soient $X,Y\in\unsure{M|\mathcal M}$ avec $X\deleted{\unsure{\parallel}}@COMP@Y\unsure{\text{\S}|?|.}$}
\deleted{\deleted{\unsure{Alors}} \inserted{Soient} $X'\ll X$, \deleted{$Y'\ll Y\Longrightarrow X'\parallel Y'$} \inserted{avec $X'\parallel X\cap Y=L$, (i.e. $X'\parallel Z$ pour $Z\leq X,Y$)} $Y'\ll Y$ avec $Y'\parallel L$. Alors $X'\parallel Y'$}

% Slanted left margin. A long cancellation stroke crosses the note's upper
% and middle lines; R2 reads the note as cancelled with the abandoned draft.
\reversemarginpar
\margin{\deleted{\uline{NB} La chose importante est $X'@COMP@Y'$, alors $X'\cap Y'=\varnothing$ immédiat. Car $Z\deleted{\ll}\leq X',\,Z\leq Y'$ $\Longrightarrow Z\ll\unsure{X'|X},\,\unsure{Z'|Z}\ll Y$ d'où $Z\ll X\cap Y=L$, or $Z\leq X'\parallel L\Longrightarrow Z\parallel L$, or $Z\ll L$ et $Z\parallel L$ \deleted{\unsure{impossible}} (d'où $Z@COMP@L$) $\Longrightarrow Z\leq L$ \deleted{absurde} car \uline{$Z\cap L=\varnothing$ !}}}%
\normalmarginpar

\deleted{\uline{Cor} 1 Soient $F,C\in\unsure{\mathscr F|\mathcal F}$ avec $F\parallel\unsure{C|G}$. Alors $F\ll F$, $C'\ll G\Longrightarrow F'\parallel G'$}
\deleted{\uline{Cor. 2} Soient $F,G\in\mathscr F$, $F@COMP@G$ \deleted{$\unsure{L}=\underset{Z\in\widetilde F\cap\widetilde G}{\mathrm{Sup}}\,Z$} \inserted{$L=F\cap G$}, $F'\ll F,G'\ll G$. Supposons $F'\parallel L,\ G'\parallel L$, alors $F'\parallel G'$.}

% Shallow enclosing contour below the abandoned At DC2 paragraph; the smaller
% rule under Y'<<Y, X'||K is an underline crossed by the written comma.
\figure{\begin{tikzpicture}[every node/.style={inner sep=0pt}]
\node[anchor=north west,text width=.96\linewidth] (draft) at (0,0) {\deleted{\uline{At DC} 2 \quad (Axiome des ateliers spacieux) \deleted{\unsure{Soit|Soient}} $X,Y\in M$, $\deleted{\unsure{L}}K=X\cap Y=\underset{Z\in\widetilde X\cap\widetilde Y}{\mathrm{Sup}}\,Z$. Supposons que pour tt $X',Y'$, avec $X'\ll X,\underline{Y'\ll Y,\ X'\parallel K},Y'\parallel K$, on ait $X'\parallel Y'$. Alors}};
\draw ([xshift=.6em,yshift=1.3ex]draft.south west)--([xshift=.05em,yshift=-.1ex]draft.south west) .. controls ([xshift=.8em,yshift=-.15ex]draft.south west) and ([xshift=-1.5em,yshift=-.5ex]draft.south east) .. ([xshift=-.6em,yshift=-.2ex]draft.south east) .. controls ([xshift=-.3em,yshift=.6ex]draft.south east) and ([xshift=.1em,yshift=1.2ex]draft.south east) .. ([xshift=.5em,yshift=1.4ex]draft.south east);
\end{tikzpicture}}

On voudra la

\uline{Propriété 1} Soient $F,G\in\mathscr F$, $F@COMP@G$, $L=F\cap G$. Soient $F'\ll F,\ G'\ll G$. Alors
\[
\begin{aligned}
 & F'@COMP@G'\\
\Longleftrightarrow\quad & F'_{L}@COMP@G'_{L}
\end{aligned}
\]

cf \deleted{p.} GF $\underline{\overline{\mathrm{VI}}}$, p.~\uline{73} -- On a en tous cas tjrs $@ROUNDED@$
\deleted{\unsure{Montrons} qu'on a bien \unsure{en} $\Rightarrow$. En effet,}

Ceci est équivalent (si on le voit de façon générale) à l'ancien At 12, qui prend le nom

% Lower slanted left margin, first portion.
\reversemarginpar
\margin{\uline{Critère} de \uline{compatibilité} pour les raffinements de \uline{sous-figures}\quad Mais c'est faux dans le cas simplicial, ex :}%
\figure{\begin{tikzpicture}[x=1em,y=1em,line cap=round,line join=round]
\draw[thick] (1.48,.04)--(0,1.12)--(1.48,2.25)--(3.03,1.13)--(1.57,0);
\draw[thick] (1.62,.61) .. controls (2.20,.68) and (2.20,1.76) .. (1.49,1.80) .. controls (.80,1.85) and (.76,.68) .. (1.52,.60);
\draw[thick] (1.48,2.25)--(1.52,.59)--(1.57,0);
\fill (1.49,1.80) circle (.074) (1.52,.61) circle (.085);
% Small internal x, then two larger external X-shaped marks.
\draw[thick] (.65,1.03)--(.85,1.32) (.65,1.29)--(.86,1.06);
\draw[thick] (-.39,-.10)--(.03,.29) (-.41,.25)--(.04,-.12);
\draw[thick] (2.37,-.26)--(2.82,.20) (2.39,.18)--(2.83,-.23);
\draw[thick] (2.44,-.28)--(2.84,.20);
\end{tikzpicture}}
\margin{Mais on aura $\unsure{x'|X'}_{L}\parallel Y'_{L}\Longrightarrow \unsure{x'|X'}@HASH@Y'$\\ C'est un \unsure{contre-exple|contre-exemple|contre exemple} à l' : At $\parallel$, et a fortiori à \deleted{ex} At 11 (cf GF $\underline{\overline{\mathrm{VI}}}$, p. 67,68)}%

% The thin vertical rule belongs beside the live axiom, not inside the title
% Critere. Ancien is an oblique interlinear word above/right of Soient;
% its verbal attachment remains uncertain although its letters are resolved.
\margin{\tikz[x=.5em,y=.5em]{\draw (0,0)--(0,4.25);}}%
\uline{At DD} 1 Soient \inserted{ancien} $X,Y\ \unsure{o|,}\ X',Y'\in M$, $X@COMP@Y,\ X'\ll X,Y'\ll Y$. Posons $K=X\cap Y=\underset{Z\in\widetilde X\cap\widetilde Y}{\mathrm{Sup}}\,Z$. Alors $X'_{L}@COMP@Y'_{L}$ implique $X'@COMP@Y'$ \quad (NB \unsure{l'énoncé|l'inverse} \deleted{\unsure{est}} est tjrs vrai)
\normalmarginpar

\uline{Corollaire} 1 \quad la ``propriété'' ci dessus

\[
F\parallel G,\ F'\ll F,\ G'\ll G\ \Longrightarrow\ F'\parallel G'
\tag*{\makebox[0pt][r]{\makebox[\displaywidth][l]{\uline{Corollaire} 2}}}
\]

Plus gén. \quad Si $F@COMP@G,\ F'\ll F,\ G'\ll G$, alors
\[
 F'\parallel G'\ \Longleftrightarrow\ F'_{L}\parallel G'_{L}
\]
'''
tex=tex.replace('@COMP@',comp).replace('@HASH@',hashsign).replace('@ROUNDED@',rounded)
(root/'scan009.tex').write_text(tex)
rows=[]
def add(place,C,H,reading,dc,dh,kind,confidence,evidence,crop=None,doubt='not applicable',marked=False,math=None):
 r={'id':f'R2-009-{len(rows)+1:02d}','place':place,'C':C,'H':H,'reading':reading,'diff_C':dc,'diff_H':dh,'kind':kind,'marked_in_H':marked,'confidence':confidence,'evidence':evidence,'crop':cm[crop]['file'] if crop else None,'crop_coordinates':cm[crop]['box'] if crop else None,'C_doubt_status':doubt,'math_consequence':math};rows.append(r);return r['id']
A={}
add('opening final words','d’autres',r'\ill{}','d’autres',False,True,r'readable ink left as \ill{}','high','A d, apostrophe and the connected autres group end the opening paragraph; no next word is supplied.')
add('whole upper At DC1 / Cor1 / Cor2 draft','all cancelled','only first line cancelled, later clauses and corollaries live; prose note says crossed','all cancelled, with local earlier changes separately represented',False,True,'deletion state (struck given live or live given struck)','high','Long oblique strokes run through the whole upper draft. The local horizontal deletions do not exhaust that global cancellation.')
add('old At DC1 label underline','At underlined','plain At DC1','At alone underlined',False,True,'omission','high','A short baseline rule sits directly beneath At and ends before DC.')
A['M']=add('first and recurring M alphabet',r'\unsure{M|\mathcal M}',r'\mathcal M',r'\unsure{M|\mathcal M}',False,True,'other','medium','Two tall stems and a bowed joining trough survive the horizontal cancellation. They do not settle a named font; the uncertainty itself is preserved.','M','retained')
A['oldparallel']=add('old relation inside first compatibility sign',r'\deleted{\unsure{\parallel}}','no old sign',r'\deleted{\unsure{\parallel}}',False,True,'omission','low','Two near-upright strokes survive inside the crossed angular replacement. They plausibly form old parallel bars, but the overlapping paths prevent certainty.','oldsign','retained')
A['oldend']=add('mark after first old Y',r'\unsure{\text{\S}|?|.}','omitted',r'\unsure{\text{\S}|?|.}',False,True,'omission','low','Two small stacked bent loops are cut at their waist by the horizontal cancellation; a section-like mark is preferred, but the original remains unclear.','oldsign','retained')
A['Alors']=add('old beginning before added Soient',r'\deleted{\unsure{Alors}}',r'\struck{At}',r'\deleted{\unsure{Alors}}',False,True,'misread word','low','A tall A and following upright l are visible above a dense horizontal strike; the following low letters are largely covered. The group is longer than the two-letter At.','oldAlors','retained')
add('Soient above the old beginning','inserted Soient','Soient presented on main baseline','inserted Soient',False,True,'insertion or placement','high','The small Soient sits above the local horizontal cancellation.','oldAlors')
add('avec X′ parallel X cap Y insertion anchor','after X′≪X, inside cancelled statement','detached after the first statement line','raised clause attached after X′≪X, within the globally cancelled draft',False,True,'insertion or placement','high','The added avec begins above the cancelled Y′≪Y segment and the following formula continues along that same raised writing level.')
A['L']=add('intersection name in added clause',r'\unsure{L|\mathcal L}','L','L',True,False,'other','medium','A plain rising stem turns into one horizontal foot; there is no extra loop or upper flourish.','L','resolved')
add('i.e. gloss in the raised insertion','(i.e. X′∥Z pour Z≤X,Y)','i.e. gloss without parentheses','parenthesized i.e. gloss',False,True,'other','high','Opening and closing curves enclose the gloss independently of the added formula.')
add('upper slanted NB cancellation state','live','live','cancelled with the abandoned upper draft',True,True,'deletion state (struck given live or live given struck)','medium','After rotation a long straight stroke crosses the La / importante / relation lines and continues into the upper draft below. R2 reads this as a global cancellation through the note, distinct from its two shorter erased words.','upperNB')
add('upper marginal NB underline','underlined NB','plain NB','underlined NB',False,True,'omission','high','A separate short rule lies beneath the two heading letters.','upperNB')
add('upper margin opening','La chose importante est','Il [ill.] choisi [ill.]','La chose importante est',False,True,r'readable ink left as \ill{}','high','The rotated lines show La, chose, importante and est in sequence; the visible last word is not choisi.','upperNB')
A['immediat']=add('upper margin after empty intersection',r'\unsure{immédiat}',r'\uncertain{immédiat}','immédiat',True,True,'other','medium','The initial i, double m run, accented middle, and final crossed t are readable upright; no final e is added.','upperNB','resolved',True)
add('upper margin proof connector','Car','opening parenthesis / unread','Car',False,True,r'readable ink left as \ill{}','high','The word begins with a capital open C and ends with the joined ar strokes.','upperNB')
add('upper margin overwritten relation after first Z',r'Z\deleted{\ll}\leq X′','Z≤X′',r'Z\deleted{\ll}\leq X′',False,True,'omission','medium','An extra angular layer remains under the reinforced live less-or-equal sign.','upperNB')
add('upper margin common-refinement line: small raised marks','Z≪X, Z≪Y','Z≪X, Z≪Y',r'Z\ll\unsure{X′|X},\ \unsure{Z′|Z}\ll Y',True,True,'misread symbol or index','low','Small raised strokes beside the first X and second Z can be read as primes; they are close to the neighbouring line and comma. They are recorded as uncertain rather than discarded to regularize the inference.','upperNB',math='If these are primes, the literal chain does not have exactly the repeated variable pattern expected by the prose proof. No algebraic repair is made.')
add('upper margin first or','or','semicolon','or',False,True,'misread word','high','A small rounded o and rising r follow L and the comma.','upperNB')
add('upper margin second or','or','et','or',False,True,'misread word','medium','The leftmost group before Z≪L has an o-like loop and short r, with no tall t.','upperNB')
A['impossible']=add('upper margin first erased word',r'\deleted{\unsure{impossible}}',r'\ill{}',r'\deleted{\unsure{impossible}}',False,True,'omission','low','A p-like descent and later tall strokes survive below the heavy horizontal line; impossible remains plausible but not fully separable.','upperNB','retained',True)
A['dou']=add('upper margin parenthetic connective',r'\unsure{d’où|comme}',r'\ill{}','d’où',True,True,r'readable ink left as \ill{}','medium','After the opening curve, the first letter has a tall d stroke and a separate apostrophe-like mark; the remaining low group fits où rather than the longer comme.','upperNB','resolved',True)
add('upper margin parenthetic compatibility','Z [compat] L','unread / omitted','Z [compat] L in parentheses',False,True,r'readable ink left as \ill{}','high','Z and L flank the angular compatibility mark inside a closing parenthesis. The macro used for the base compatibility sign is not itself counted as a difference.','upperNB')
add('upper margin final implication','⇒ Z≤L','⇒ Z overlined-parallel L = empty','⇒ Z≤L',False,True,'misread symbol or index','high','The implication is followed by Z, a less-or-equal angle and L; the intersection-equals-empty formula comes later on its own line.','upperNB')
A['absurde']=add('upper margin second erased word',r'\deleted{\unsure{absurde}}',r'\ill{}',r'\deleted{absurde}',True,True,r'readable ink left as \ill{}','medium','The initial a loop, tall b, joined sur and final de strokes remain visible under a local horizontal strike.','upperNB','resolved',True)
add('upper margin before final contradiction','car','omitted','car',False,True,'omission','medium','A small c/a/r group follows the crossed absurde.','upperNB')
add('upper margin final underlined formula','Z∩L=∅ !, underlined','Z overlined-parallel L=∅ !','Z∩L=∅ !, underlined',False,True,'misread symbol or index','high','The thick middle mark has an arched upper join and two descending sides. A separate long rule underlines the full final equation and exclamation mark.','upperNB')
A['CorC']=add('cancelled Cor1 second initial figure',r'\unsure{C|G}','G','C',True,True,'misread symbol or index','medium','The capital is an open C with a long lower arm and no inward crossbar or return. The nearby later G has a distinctly developed inward lower return.','cor1_initial','resolved')
A['family']=add('Cor1 and recurring figure-family alphabet',r'\unsure{\mathscr F|\mathcal F}',r'\mathfrak F',r'\unsure{\mathscr F|\mathcal F}',False,True,'misread symbol or index','medium','A looped/curving main stem and separate crossing arm recur. The handwriting is cursive, while exact mathscr versus mathcal representation remains uncertain.','cor1_initial','retained')
add('cancelled Cor1 disjointness premise','F∥G','F∥G',r'F\parallel\unsure{C|G}',True,True,'misread symbol or index','low','The right letter is a C-shaped outline with a tiny detached lower-right dash. That dash may supply an incomplete G return, but it is not decisive.','cor1_right')
add('cancelled Cor1 first refinement premise','F≪F','F′≪F','F≪F',False,True,'misread symbol or index','high','There is no detached prime after the first F; the following strokes belong to the double-angle relation.','cor1_right',math='The literal premise fails to constrain the F′ in the conclusion. It remains uncorrected.')
add('cancelled Cor1 second refinement premise','C′≪G','G′≪G','C′≪G',False,True,'misread symbol or index','high','The primed first letter is an open C; the following unprimed G has a returning lower stroke.','cor1_second',math='Literal C′ does not bind the G′ occurring in the conclusion.')
add('cancelled Cor1 final punctuation','period','period','no terminal period',True,True,'other','medium','After the final primed G the crop and supplied half show no separate baseline point.','cor1_second')
A['Cor2L']=add('cancelled Cor2 old equation initial',r'\deleted{\unsure{L}=Sup…}',r'\struck{\ill{}}',r'\deleted{\unsure{L}=Sup_{Z∈Ftilde∩Gtilde} Z}',False,True,r'readable ink left as \ill{}','low','The leading group is almost buried by zigzag cancellation; L remains uncertain. The Sup trace, lower Z/membership and two deployed-set indices survive in parts below the heavy line. The replacement L=F∩G is clearly above.','cor2_old','retained',True)
add('At DC2 title adjective','spacieux','spécieux','spacieux',False,True,'misread word','high','The title has a rounded a after sp and no acute accent.')
A['Soit']=add('At DC2 old word at end of title',r'\deleted{\unsure{Soit|Soient}}','live Soient',r'\deleted{\unsure{Soit|Soient}}',False,True,'deletion state (struck given live or live given struck)','low','So and a tall crossed terminal-like stem survive, but the long cancellation return obscures whether further low letters belonged to the original word.','DC2_Soit','retained')
A['oldL']=add('At DC2 old letter behind K',r'\deleted{\unsure{L}}K','K',r'\deleted{\unsure{L}}K',False,True,'omission','low','An extra short horizontal arm and lower stem curl remain with the K arms. An earlier L is possible but not independently secure.','DC2_K','retained')
A['tt']=add('At DC2 after pour',r'\unsure{tt}','tous','tt',True,True,'abbreviation expanded or spelling modernised','high','Two tall strokes share a crossbar and each has a curled lower exit. They spell the two-letter abbreviation tt, without ous.','tt','resolved')
add('At DC2 underline beneath middle hypotheses','underline Y′≪Y, X′∥K','no underline','underline Y′≪Y, X′∥K',False,True,'omission','high','A continuous low rule begins below Y′ and ends beneath K. The apparent central pointed bend is the written comma crossing that rule, not an additional implication sign.','DC2_rule')
add('At DC2 enclosing lower contour','not drawn','described as encadré','shallow lower contour with rising ends, drawn',True,True,'drawing or diagram','high','The entire unfinished draft has a long low border below its last line and rising oblique/curved ends. It is distinct from the long cancellation strokes.')
add('introduction to live property','On voudra la','On voudrait la','On voudra la',False,True,'misread word','high','The word ends in the low a stroke, with no terminal t.')
add('live property title','Propriété 1','Proposition 1','Propriété 1, underlined',False,True,'misread word','high','The title contains the short été ending after propri; it is not the longer position sequence. The underline runs through the numeral.')
add('reference and On a line state','live','whole reference and assertion struck','reference and On a assertion live; only next proof-start line cancelled',False,True,'deletion state (struck given live or live given struck)','high','The long strike follows the lower proof-start baseline. It passes below the reference letters and does not cross the upper assertion text.','citation')
A['cf']=add('reference initial abbreviation',r'\unsure{cf|Cf}','cf.','cf',True,True,'other','medium','The first c is distinctly lower than the adjacent GF capitals; the f descends. There is no dot after the abbreviation.','citation','resolved')
A['oldp']=add('reference small cancelled token',r'\deleted{\unsure{p.}}','omitted',r'\deleted{p.}',True,True,'omission','medium','A descender, crossed loop and separate small dot can be followed between cf and GF.','citation','resolved')
add('reference roman numeral decoration','VI with upper and lower rule','plain VI','VI with upper and lower rule',False,True,'omission','high','One line lies above VI and another below it.','citation')
A['73']=add('reference page number',r'\uline{\unsure{73|13}}','73, not underlined','underlined 73',True,True,'other','medium','The first digit has an angled top return before its descending stroke; the second has two curved lobes. A separate line underlines both digits.','citation','resolved')
add('On a assertion abbreviation','tjrs','omitted','tjrs',False,True,'omission','high','The tall t and descending j with short rs continuation occur before the final relation-shaped mark.')
A['arrow']=add('On a assertion terminal mark','uncertain rounded-return drawing or Rightarrow','Longrightarrow','two shafts plus a separate rounded right return, drawn literally',True,True,'drawing or diagram','high','Two horizontal shafts end before a separate larger curved cap. The cap descends and returns left at the bottom; it does not form a pointed arrowhead.','assertedarrow','resolved')
A['Montrons']=add('cancelled proof start first word',r'\unsure{Montrons}','omitted',r'\unsure{Montrons}',False,True,'omission','low','A large M and portions of the low n/t/r/o/n/s run survive, but the upper strike and marginal writing overlap the word.','crossedline','retained')
add('cancelled proof start middle prose','qu’on a bien','omitted','qu’on a bien',False,True,'omission','medium','The descending q and later a/bien groups can be followed along the struck baseline.','crossedline')
A['en']=add('cancelled proof start before arrow',r'\unsure{en}','omitted',r'\unsure{en}',False,True,'omission','low','Two short low joined strokes are partly effaced by the long cancellation; en remains tentative.','crossedline','retained')
add('Ceci est équivalent parenthetical qualification','(si on le voit de façon générale)','unread groups plus incomplete parentheses','(si on le voit de façon générale)',False,True,r'readable ink left as \ill{}','high','The whole parenthetical is readable across the lower line, including the tall f and cedilla-bearing façon. No extra editorial words are supplied.')
add('H supposed independent additions after cancelled proof start','no such extra added prose','add ill ill','no extra independent prose addition',False,True,'text not on the page','medium','The slanted writing intersecting the proof-start area belongs to the long marginal criterion note, not to an additional standalone body phrase.')
add('lower margin criterion wording','Critère de compatibilité pour les raffinements de sous-figures','Critère de compatibilité followed by unread struck/added fragments','Critère de compatibilité pour les raffinements de sous-figures',False,True,r'readable ink left as \ill{}','high','Rotation separates the words pour les raffinements de sous-figures from the body text crossing them.','criterion')
add('lower criterion underlines','Critère, compatibilité, sous-figures underlined','no comparable complete underline spans','Critère, compatibilité, sous-figures underlined',False,True,'omission','high','Each of those three groups has its own long baseline rule. The low rule overlaps the following Mais at an oblique angle; it is not taken as a separate deletion of Mais.','criterion')
add('thin vertical line beside live axiom','line embedded with criterion margin note','described as a border beside At CD1','thin vertical border beside the live At DD1 block',True,True,'drawing or diagram','high','The straight line stands just left of the live axiom/Posons/implique lines, separate from the slanted criterion. The fragment places it with that block.','criterion')
add('simplicial example drawing','TikZ drawing','description only','complete diamond, open oval, diameter, two filled vertices and three cross marks drawn',False,True,'drawing or diagram','high','The rotated crop shows a slightly open lower diamond corner, a nearly closed inner oval with a lower-right gap, a top-to-bottom diagonal through two filled oval intersections, one small inner cross and two larger outer crosses.','diagram',math='The figure is reproduced without assigning additional face/stratum identities absent from the page.')
A['innerx']=add('drawing inner small cross',r'\unsure{x|+}','small internal mark','x-shaped crossing',True,True,'drawing or diagram','high','Once rotated to the writing direction, both short strokes are diagonal; their crossing is x-shaped rather than horizontal/vertical.','diagram','resolved')
A['outerleft']=add('drawing external lower-left cross',r'\unsure{X|x}','a cross below the unrotated figure','larger X-shaped cross',True,True,'drawing or diagram','medium','Two long diagonal strokes cross, substantially larger than the internal mark.','diagram','resolved')
A['outerright']=add('drawing external lower-right cross',r'\unsure{X|Y}','a cross to the right of the unrotated figure','reinforced X-shaped cross',True,True,'drawing or diagram','medium','Four diagonal arms can be followed; the lower-left diagonal is reinforced. The thin lower-right arm remains, so the mark is not reduced to a three-armed Y.','diagram','resolved')
add('lower margin first variable case in premise and consequent','X′ in both places','X′ in both places',r'\unsure{x′|X′} in both places',True,True,'misread symbol or index','low','Both first crosses are noticeably small and low beside the tall Y′. The cramped slanted hand may account for the size, so lowercase x is preferred with uppercase retained.','lowernote')
A['hash']=add('lower margin consequent relation','drawn hash-like sign | # | notparallel | parallel','overlined parallel','literal two uprights with two transverse bars, drawn',True,True,'drawing or diagram','high','Two strong near-vertical strokes are crossed by two short oblique bars at distinct heights. This is not one bar drawn above parallel. Its logical interpretation is left open.','lowernote','resolved',True,math='The contour is resolved; identifying the mark with a particular negated relation is not independently justified.')
A['Cest']=add('lower margin article after C’est',r'\unsure{C’est un|C’est une}',"c’est un",'C’est un',True,True,'misread word','medium','The short group ends at n before the separate contre group. There is no extra e loop; the initial C is capital.','lowernote','resolved')
A['contre']=add('lower margin example word',r'\unsure{contre-exemple|contre-exple|contre exemple}','contre-ex.',r'\unsure{contre-exple|contre-exemple|contre exemple}',True,True,'abbreviation expanded or spelling modernised','low','The middle is crossed by writing in the main direction. A short exple-like sequence is preferred, but neither the full em group nor the exact hyphen/space can be certified. No abbreviation point is visible.','lowernote','changed')
A['colon']=add('lower margin before At',r'\unsure{:}','omitted',':',True,True,'omission','medium','Two separate small points occur vertically before the At group.','lowernote','resolved')
add('lower margin first axiom name','At parallel','At 11','At parallel',False,True,'misread symbol or index','high','The first pair consists of two plain parallel bars. The later numeral 11 has distinctly numeral-like top/foot strokes.','lowernote')
add('lower margin strengthening phrase','et a fortiori à','et ill','et a fortiori à',False,True,r'readable ink left as \ill{}','high','The long f descender and connected ortiori run are legible across the oblique line.','lowernote')
A['ex']=add('lower margin locally erased group',r'\deleted{\unsure{ex}}','omitted',r'\deleted{ex}',True,True,'omission','medium','A short e-like loop is followed by crossing x strokes beneath an additional local cancellation.','lowernote','resolved')
add('lower marginal reference','(cf GF VI with rules, p.67,68)','reference partly supplied in editorial notes','(cf GF VI with upper/lower rules, p.67,68) as marginal text',False,True,'insertion or placement','high','The reference is physically part of the slanted note. Its letters, ruled VI, page numbers and closing parenthesis are present.','lowernote')
add('lower note punctuation after consequent','comma before C’est','opening parenthesis before c’est','line break with no added comma or parenthesis',True,True,'other','medium','After the primed Y the line has no detached comma; the next line starts with the large C itself, without a separate opening parenthesis.','lowernote')
A['DD']=add('live axiom letters',r'\unsure{DD|DC}','CD (with editorial old DD/DC alternatives)','DD',True,True,'misread word','medium','Both current letters have a stem and closed right bowl. The retracing does not reveal an independently readable older CD or DC layer.','heading','resolved',True)
add('live axiom label underline extent','At DD underlined, 1 outside','At CD1 emphasized as one span','At DD underlined; 1 outside',False,True,'other','high','The rule ends beneath the second D before the separated numeral.','heading')
A['ancien']=add('oblique interlinear word',r'\unsure{ancien|ou bien|ou bien,}','ou uncertain ancien','ancien',True,True,'misread word','medium','The word has an initial rounded a/n run, then c and a dotted i followed by en. There is no tall b required by bien and no second word ou.','addedword','resolved',True)
add('oblique ancien position','inserted after Soient','addition after X,Y','above/right of Soient; verbal attachment uncertain',False,True,'insertion or placement','medium','The word rises obliquely above the right edge of Soient, between that line and the preceding ancien At12 line. No secure arrow fixes its intended grammatical attachment.','addedword')
A['separator']=add('small separator between Y and X′',r'\unsure{o|,}','et',r'\unsure{o|,}',False,True,'misread word','low','A narrow closed oval with a downward extension is visible. It is unlike a full written et; the shorter comma alternative remains only a possibility.','separator','retained')
add('live Posons meet operation','K=X cap Y','K=X wedge Y','K=X cap Y',False,True,'misread symbol or index','high','The operation has a rounded arch with two descending sides, matching intersection; it has no pointed wedge apex.')
A['noun']=add('live axiom NB noun',r'\unsure{l’énoncé|l’inverse}','l’inverse',r'\unsure{l’énoncé|l’inverse}',False,True,'misread word','low','The compressed run has possible accent-like marks above its beginning and ending. Those permit énoncé, while the lower joins can be read inverse. The apparent final points are not independently promoted to a colon.','NBbottom','retained')
A['est']=add('live axiom NB old word',r'\deleted{\unsure{est}}',r'\ill{}',r'\deleted{\unsure{est}}',False,True,'omission','low','An old tall/looped short group is crossed before the clean live est. Its individual e/s/t strokes cannot be securely separated.','NBbottom','retained',True)
add('live axiom NB abbreviation','tjrs','toujours','tjrs',False,True,'abbreviation expanded or spelling modernised','high','The tall t and long j descent are followed by only the short rs run.','NBbottom')
add('live axiom NB placement','after the implication/conclusion','before implique','aside beside the final implication/conclusion',False,True,'insertion or placement','high','The parenthetical occupies the right side of the final axiom lines, after the displayed compatibility condition rather than interrupting before implique.','NBbottom')
add('H inline reference after implique','no body reference here','(cf. GF VI)','no independent body reference',False,True,'text not on the page','high','The slanted GF VI reference belongs to the adjacent counterexample note; it is not an added parenthesis in the axiom sentence.','lowernote')
add('first final corollary label','Corollaire 1','Cor. Main 1','Corollaire 1',False,True,'abbreviation expanded or spelling modernised','high','The full Corollaire is written and underlined, followed by numeral1; no Main word is present.')
add('first final corollary content','la ``propriété’’ ci dessus','(cf. la « propriété » ci-dessus)','la ``propriété’’ ci dessus',False,True,'text not on the page','high','The line starts directly with la, has paired high quotation strokes, and separates ci and dessus with blank space. It contains neither cf nor outer parentheses nor a hyphen.')
add('second final corollary label and scope','Corollaire2 beside F∥G refinement implication','that implication placed under Cor.Main1; next Si given Cor.Main2','Corollaire2 labels the F∥G refinement implication',False,True,'insertion or placement','high','The underlined Corollaire2 stands at the left of the same line as F∥G, F′≪F, G′≪G ⇒ F′∥G′.')
add('final generalization introduction','Plus gén. Si …','Si … under Cor.Main2; editorial uncertain pour que','Plus gén. Si …',False,True,'abbreviation expanded or spelling modernised','high','The distinct P/l/u/s run is followed by gén. and the Si clause. It is not pour que, and the generalization is not assigned an additional numbered corollary.')

rowmap={r['id']:r for r in rows}
def audit(key,C,place):
 r=rowmap[A[key]]
 return {'C_reading':C,'place':place,'status':r['C_doubt_status'],'evidence':r['evidence'],'crop':r['crop'],'crop_coordinates':r['crop_coordinates'],'difference_id':r['id']}
checks=[('M','M|mathcal M','old At DC1 membership'),('oldparallel','old parallel','old At DC1 sign'),('oldend','section sign|?|.','old At DC1 after Y'),('Alors','old Alors','before inserted Soient'),('L','L|mathcal L','inserted intersection name'),('immediat','immédiat','upper NB'),('impossible','deleted impossible','upper NB'),('dou','d’où|comme','upper NB parenthesis'),('absurde','deleted absurde','upper NB'),('CorC','C|G','Cor1 initial second figure'),('family','mathscr F|mathcal F','Cor1 set alphabet'),('Cor2L','old L','Cor2 Sup equation'),('Soit','Soit|Soient','At DC2 old word'),('oldL','old L','At DC2 before K'),('tt','tt','At DC2 quantifier abbreviation'),('cf','cf|Cf','reference'),('oldp','deleted p.','reference'),('73','73|13','reference number'),('arrow','rounded-return drawing|Rightarrow','On a assertion'),('Montrons','Montrons','cancelled proof start'),('en','en','cancelled proof start'),('innerx','x|+','drawing inner mark'),('outerleft','X|x','drawing outer left'),('outerright','X|Y','drawing outer right'),('hash','drawn sign|#|notparallel|parallel','lower note consequent'),('Cest','C’est un|C’est une','lower note'),('contre','contre-exemple|contre-exple|contre exemple','lower note'),('colon',':','lower note before At'),('ex','deleted ex','lower note before At11'),('DD','DD|DC','live axiom label'),('ancien','ancien|ou bien|ou bien,','oblique insertion'),('separator','o|,','live variable list'),('noun','l’énoncé|l’inverse','live NB'),('est','deleted est','live NB')]
audits=[audit(*x) for x in checks]
end=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');model='GPT-6 Astra Pro; inherited effort setting not exposed; R2'
report={'reader':'R2','scan':9,'start_utc':'2026-11-19 22:54:12 UTC','end_utc':end,'model':model,
'images_viewed':['H156-01_156-7_scan009.jpg','H156-01_156-7_scan009_a.jpg','H156-01_156-7_scan009_b.jpg']+[x['file'] for x in manifest],
'workflow_note':'Whole image once, then supplied a and b halves once, followed by 23 once-only unresolved-locus crops. Slanted notes, oblique insertion and example drawing were rotated within their single crops. All images were actually viewed with view_image. C scan009, H page8 stopping before page9, all C scan009 doubts and relevant C notes were read. No other/main009 report was opened. No OCR, external research or compilation was performed for scan009. The separate macro audit contains an explicit disclosure of three earlier prohibited synthetic diagnostic compiler attempts; no blanket no-compilation claim is made for the run.',
'coverage':[
'page number8 and whole opening paragraph, including its unfinished final d’autres',
'global cancellation of upper AtDC1, full old/new relation layers, ambiguous end mark, all primed variables, interlinear Soient and avec clause and parenthesized gloss',
'entire upper slanted NB, its global crossing stroke and local erased words, every relation and possible prime, opening/closing parentheses and final underlined contradiction',
'cancelled Cor1: initial C, figure alphabet, C/G premise ambiguity, literal F≪F and C′≪G, both conclusion primes and terminal punctuation',
'cancelled Cor2: every figure variable, old Sup formula and its indices, replacement L=F∩G, refinements and disjointness assumptions and conclusion',
'cancelled AtDC2 title and old word, overwritten L/K, full Sup formula, literal tt, all four hypotheses, middle underline and separate lower enclosing contour, unfinished Alors',
'On voudra la and live Propriété1: all compatible figure/refinement hypotheses, L=F∩G, equivalence layout and both L subscripts',
'live cf/GFVI/p73 reference with all rules, cancelled small p., tjrs, literal rounded three-stroke implication-like sign',
'cancelled proof start Montrons qu’on a bien en ⇒. En effet, and full subsequent parenthetical Ceci est équivalent qualification',
'complete lower criterion and simplicial objection, all three underlines, vertical border beside live axiom rather than verbal title',
'example diagram: diamond gap, oval gap, diagonal extent, both filled intersections, interior and both exterior crosses; no semantic labels supplied',
'complete lower marginal counterexample claim, first-variable case doubt, literal double-crossed parallel-shaped sign, C’est un, unresolved example abbreviation, colon, At-parallel versus At11, erased ex, a fortiori and reference',
'live AtDD1: retraced letters, underline scope, oblique ancien and uncertain attachment, oval separator, all primes and membership, literal K introduction followed by L indices, compatibility implication and NB layers',
'Corollaire1 exact label and quoted cross-reference; Corollaire2 label tied to disjoint-refinement implication; Plus gén. and complete final equivalence with both L indices',
'all34 C doubt occurrences audited; equivalent between/TikZ base-glyph conversion was not counted as an H difference'
],
'notation':[
{'form':'compatibility','reading':'opposing angular paths as on preceding pages','evidence':'same undecorated mark; H between conversion is not an error row'},
{'form':'disjointness','reading':'two parallel bars','evidence':'the plain pair differs from the lower note’s two extra transverse bars'},
{'form':'upper NB small primes','reading':'X′|X and Z′|Z','evidence':'small raised strokes close to adjacent line and comma; explicitly unresolved'},
{'form':'lower note consequent','reading':'two uprights plus two transverse bars','evidence':'draw actual contour; do not choose a logical meaning from the counterexample claim'},
{'form':'On a assertion mark','reading':'two shafts with separate rounded right cap','evidence':'no pointed arrowhead'},
{'form':'live label','reading':'At DD1, At DD underlined','evidence':'two closed retraced bowls; numeral outside rule'},
{'form':'intersection names','reading':'K introduced, L used in following indices','evidence':'literal mismatch retained as also noticed by H'},
{'form':'abbreviations','reading':'tt; tjrs; gén.; cf without period','evidence':'literal short groups preserved, expansions only explanatory'},
{'form':'diagram labels','reading':'one small x-shaped crossing and two larger X-shaped crossings','evidence':'drawn strokes, with the outer right diagonal reinforced'}
],
'math_notes':[
{'type':'summary, not proof check','text':'The page abandons two disjointness/compatibility drafts and their corollaries, then proposes a locality criterion for compatibility under refinement. A marginal note explicitly says the criterion is false in the simplicial case and gives a drawing. The final named axiom and corollaries reuse the restriction indices L after introducing K.'},
{'type':'targeted proof check','statement_id':'R2-009-M1','text':'The final contradiction in the upper NB is valid under the stated local assumptions that Z is a nonempty stratum, Z≪L and Z is disjoint from L. Disjointness gives compatibility and Z∩L=empty. By At4, applied to the stratum Z itself, Z≪L yields a stratum U≤L with Z≪U. Compatibility of Z with L descends to U, so At5 for compatible strata gives Z≤U≤L. Hence Z∩L=Z, contradicting that a stratum is nonempty. This checks the final contradiction only; it does not prove the preceding Z≪X,Y⇒Z≪X∩Y step or resolve the possible primes.'},
{'type':'conditional targeted proof check','statement_id':'R2-009-M2','text':'The globally compatible ⇒ locally compatible direction follows if the subscript-L objects are subfigures of their parents. Indeed, if A≤F′ and B≤G′ and H is a common upper figure for compatible F′ and G′, then H is also an upper figure for A and B. This proves hereditary compatibility for those subfigures. A definition of F′_L is not established on this page, so the check is explicitly conditional on that subfigure property and does not prove the displayed equivalence or the final axiom.'},
{'type':'targeted counterexample to literal cancelled formula','statement_id':'R2-009-M3','text':'The literal cancelled Cor1 formula, with F≪F and C′≪G but conclusion F′∥G′, cannot be a universal theorem as written. In the two-element Boolean figure poset {empty,{a}}, take refinement=inclusion and all figures compatible. Set F=C=G=C′=empty and F′=G′={a}. The disjointness premise and the two written refinement premises hold, while F′∩G′={a}, so the conclusion fails. This diagnoses the missing/mismatched primed operands in an abandoned draft; no correction is inserted into its text.'},
{'type':'unverified author claim','text':'The simplicial counterexample is transcribed and drawn, but the restriction notation and identities of the parts of the drawing are insufficiently specified within the pages read to certify it independently. No external GFVI pages cited by H were consulted. The final hash-like relation is a contour reading, not an independently proved negation interpretation.'},
{'type':'literal mismatches retained','text':'The cancelled F≪F and C′≪G, the initial C and later C/G uncertainty, and live K with subsequent L indices are preserved. The oblique ancien is readable but its verbal attachment remains uncertain. No missing conclusion is supplied after the abandoned Alors.'}
],
'author_qualifications':['bien qu’elle sera conséquence de diverses façons d’autres','On voudra la','On a en tous cas tjrs [rounded two-shaft mark]','[cancelled] Montrons qu’on a bien en ⇒. En effet,','(si on le voit de façon générale)','Mais c’est faux dans le cas simplicial, ex :','C’est un contre-exple|contre-exemple|contre exemple à l’ : At ∥, et a fortiori à [deleted ex] At11','(NB l’énoncé|l’inverse [deleted est] est tjrs vrai)','la ``propriété’’ ci dessus'],
'author_explicit_verification_requests':[],
'unresolved':[
{'place':'M alphabet','reading':r'\unsure{M|\mathcal M}','confidence':'medium'},
{'place':'old first relation','reading':r'\deleted{\unsure{\parallel}}','confidence':'low'},
{'place':'old first statement end mark','reading':r'\unsure{\text{\S}|?|.}','confidence':'low'},
{'place':'old beginning before Soient','reading':r'\deleted{\unsure{Alors}}','confidence':'low'},
{'place':'upper margin old impossible','reading':r'\deleted{\unsure{impossible}}','confidence':'low'},
{'place':'upper margin common-refinement line','reading':r'Z\ll\unsure{X′|X},\ \unsure{Z′|Z}\ll Y','confidence':'low'},
{'place':'figure-family alphabet','reading':r'\unsure{\mathscr F|\mathcal F}','confidence':'medium'},
{'place':'Cor1 disjointness second operand','reading':r'\unsure{C|G}','confidence':'low'},
{'place':'Cor2 old equation initial','reading':r'\unsure{L}','confidence':'low'},
{'place':'AtDC2 old word','reading':r'\unsure{Soit|Soient}','confidence':'low'},
{'place':'AtDC2 old letter','reading':r'\deleted{\unsure{L}}','confidence':'low'},
{'place':'cancelled proof-start verb','reading':r'\unsure{Montrons}','confidence':'low'},
{'place':'cancelled proof-start short group','reading':r'\unsure{en}','confidence':'low'},
{'place':'lower note first variable case','reading':r'\unsure{x′|X′}, twice','confidence':'low'},
{'place':'lower note example word','reading':r'\unsure{contre-exple|contre-exemple|contre exemple}','confidence':'low'},
{'place':'live axiom separator','reading':r'\unsure{o|,}','confidence':'low'},
{'place':'live NB noun','reading':r'\unsure{l’énoncé|l’inverse}','confidence':'low'},
{'place':'live NB old word','reading':r'\deleted{\unsure{est}}','confidence':'low'},
{'place':'ancien attachment','reading':'ancien above/right of Soient; intended attachment uncertain','confidence':'low'}
],
'differences':rows,'C_doubt_audit':audits,
'new_omissions_from_both':[
{'place':'upper NB','reading':'global cancellation state and possible raised primes','confidence':'low'},
{'place':'Cor1 premise','reading':'C/G uncertainty at later disjointness operand','confidence':'low'},
{'place':'Cor1 end','reading':'no separate terminal period','confidence':'medium'},
{'place':'AtDC2','reading':'explicitly drawn enclosing lower contour','confidence':'high'},
{'place':'lower note','reading':'first-variable case doubt and no supplied comma/parenthesis before C’est','confidence':'low'}
],
'crop_manifest':manifest,
'check_events':[
{'statement_id':'R2-009-M1','date':end,'who':model,'type':'targeted proof check','outcome':'Verified the final NB contradiction for a nonempty stratum Z using At4/At5; preceding common-refinement-to-meet step and uncertain primes not certified.'},
{'statement_id':'R2-009-M2','date':end,'who':model,'type':'targeted proof check','outcome':'Verified hereditary compatibility under explicitly stated subfigure hypotheses; application to restriction notation remains conditional.'},
{'statement_id':'R2-009-M3','date':end,'who':model,'type':'targeted proof check','outcome':'Explicit two-element Boolean-poset counterexample to the literal cancelled Cor1 premises/conclusion; no textual emendation made.'}
]}
(root/'scan009.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
md=['# R2 — scan009 / manuscript page8','',f"Independent reading: {report['start_utc']} – {end}.",'',f"**{len(rows)} rows; {sum(x['diff_C'] for x in rows)} differences from C; {sum(x['diff_H'] for x in rows)} from H. All {len(audits)} C doubts audited; 23 crops.**",'', '## Principal findings','',
'- The upper abandoned draft and its slanted NB are marked cancelled. The note’s own smaller erased words are preserved separately.',
'- Cancelled Cor1 literally has **F≪F** and **C′≪G**. The initial second figure is **C**; its later disjointness operand remains **C|G**. No mathematical correction is inserted.',
'- The upper NB resolves **immédiat**, parenthetic **d’où**, and crossed **absurde**. The common-refinement line gains explicit low-confidence prime alternatives.',
'- AtDC2 has literal **tt**, a local underline through the middle hypotheses, and a separate shallow enclosing contour. The apparent point on the underline is the written comma crossing it.',
'- The live title is **Propriété1** after **On voudra la**. The reference and On a assertion are live; the next proof-start line is cancelled.',
'- The reference resolves **cf**, cancelled **p.**, and underlined **73**. Its final sign is two shafts and a separate curved right cap, without a pointed head.',
'- The diagram is fully drawn: slightly open diamond and oval, full diagonal, two filled points, small inner x-cross and two larger outer X-crosses. No additional semantic labels are invented.',
'- The lower note has a literal **two-upright/two-crossbar sign**, not an overline above parallel. **C’est un**, the colon before **At∥**, and crossed **ex** resolve. The example-word abbreviation and small first-variable case remain doubtful.',
'- The live label reads **At DD1**, and the oblique word reads **ancien**. Its attachment remains uncertain. The written **K** followed by **L** indices is retained.',
'- The last labels are **Corollaire1** and **Corollaire2**, without Main. Corollaire1 refers to the property; Corollaire2 labels the disjoint-refinement implication. The next line begins **Plus gén.**.',
'', '## Remaining uncertainties','']
for u in report['unresolved']:md.append(f"- {u['place']}: `{u['reading']}` ({u['confidence']}).")
md+=['','## Mathematics and limits','']
for n in report['math_notes']:md.append('**'+n['type']+'**'+(' ('+n['statement_id']+')' if 'statement_id'in n else '')+'. '+n['text']+'\n')
md+=['## Full collation','', '| ID | Place | C | H | R2 | Evidence / confidence |','|---|---|---|---|---|---|']
def esc(x):return str(x).replace('|','\\|').replace('\n',' ')
for r in rows:md.append('| '+' | '.join(esc(x) for x in [r['id'],r['place'],r['C'],r['H'],r['reading'],r['evidence']+' ['+r['confidence']+']'+(' Crop: '+r['crop'] if r['crop'] else ' From supplied half.')])+' |')
md+=['','## C doubt audit','', '| C reading | Place | Outcome | Row |','|---|---|---|---|']
for a in audits:md.append('| '+' | '.join(esc(x) for x in [a['C_reading'],a['place'],a['status'],a['difference_id']])+' |')
md+=['','## Inspection and protocol record','',report['workflow_note']]
(root/'scan009.md').write_text('\n'.join(md)+'\n')
(root/'scan009_inspection_manifest.json').write_text(json.dumps({'reader':'R2','scan':9,'start_utc':report['start_utc'],'end_utc':end,'whole_views':1,'half_a_views':1,'half_b_views':1,'crop_views':[{**m,'views':1} for m in manifest],'tools':'Every image inspected through view_image; crop creation only through PIL, with one crop per listed locus.','scope':'C009/Hpage8/Cdoubts009; no other or main009 outputs.'},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'rows':len(rows),'diff_C':sum(x['diff_C'] for x in rows),'diff_H':sum(x['diff_H'] for x in rows),'C_doubts':len(audits),'crops':len(manifest),'end_utc':end}))
