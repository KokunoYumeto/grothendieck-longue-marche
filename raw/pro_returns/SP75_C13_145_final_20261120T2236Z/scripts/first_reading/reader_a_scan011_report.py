from pathlib import Path
import json

base=Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work')
manifest=json.loads((base/'edition/reader_reports/145_scan011_crop_manifest.json').read_text())
crops={r['name']:r for r in manifest}
changes=[]

def ch(num,place,C,H,final,ink,kind,c_changed=False,h_changed=True,marked='no',crop='',confidence='high',cats=(10,),math=''):
    z=crops[crop]
    changes.append(dict(id=f's011-{num:02}',place=place,C=C,H=H,final=final,ink=ink,confidence=confidence,kind=kind,c_changed=c_changed,h_changed=h_changed,marked_in_H=marked,crop=z['crop'],box=z['box'],error_category=list(cats),math_consequence=math))

ch(1,'Head of sheet: manuscript number',r'\mspage{4}','',r'\mspage{4}','A short rising diagonal meets a crossbar and a hooked descending upright. The distinct header crop includes the entire numeral, unlike the opening-line crop. This is a handwritten 4, not an editorial scan label.','omission',crop='header4',cats=(3,))
ch(2,'Opening: cancelled words before the interlinear replacement',r'\deleted{\unsure{pour $g$}}',r'\struck{\ill{}}',r'\deleted{\unsure{pour $g$}}','The g has a descending stroke; parts of the preceding small loops are visible through the cancellation. They admit pour, but the strike obscures enough of the interior that every letter is not plain. The cancellation and its tentative contents are preserved.','deletion state',marked='yes',crop='opening_and_number4',confidence='medium',cats=(5,7))
ch(3,'Opening: abbreviation after savoir',r'correspond.',r'correspondant',r'\unsure{correspond.|correspond.\textsuperscript{t}}','The main letter sequence correspond and a detached terminal stop are visible. A small high trace after the stop cannot securely be separated from the adjacent cancelled writing; it is retained as a possible raised t. There is no full baseline ending ant.','abbreviation expanded or spelling modernised',crop='opening_and_number4',confidence='medium',cats=(2,8))
ch(4,'Opening: cancelled word before à',r'\deleted{\unsure{aux}}',r'\struck{\ill{}}',r'\deleted{\unsure{aux}}','The low initial loop, central shallow stroke, and final crossing allow aux. The cancellation traverses the letters, so the C doubt is retained rather than claiming that all three letters are plain.','deletion state',marked='yes',crop='opening_and_number4',confidence='medium',cats=(5,7))
ch(5,'System, first row: after p=-1',r'p=-1\qquad g',r'p = -1, \qquad g',r'p=-1\qquad g','The blank interval after -1 and before g contains no separate comma. The nearby ink belongs to the numeral and the g.','text not on the page',crop='opening_system',cats=(9,))
ch(6,'System, second row: prose before beta=-1',r'\text{ou mieux, }\beta=-1',r'\uncertain{au moins},\quad\beta=-1',r'\text{ou mieux, }\beta=-1','The first word has a rounded o followed by u. The second has the short i stroke and the consecutive e/u curves followed by crossed x; the ending is mieux, not the ins sequence required by moins.','misread word',marked='yes',crop='opening_system',cats=(2,))
ch(7,'Main paragraph heading',r'\uline{NB}',r'\textbf{NB}',r'\uline{NB}','A separate continuous horizontal stroke lies below both capital letters. The diplomatic emphasis is an underline.','other',crop='nb_heading',cats=(10,))
ch(8,'NB, third line: q et r',r'restant',r'restent',r'restant','After rest, the next loop opens into a low a and an n before the final t. The a/n sequence is legible in the enlarged word.','misread word',crop='restant',cats=(2,))
ch(9,'NB: description of chi',r'du caractère cyclotomique',r'de la \uncertain{fonction}',r'du caractère cyclotomique','The short article ends with a u turn. The following word has the repeated car/ac/tere sequence, and the next word extends through cyclotomique. Both full words are present; the manuscript does not read fonction at this locus.','misread word',marked='yes',crop='caractere_cyclotomique',cats=(2,5))
ch(10,'NB: cancelled numeral-word before fonction',r'\deleted{\unsure{deux}}',r'\struck{\ill{}}',r'\deleted{\unsure{deux}}','An initial d-like stroke and a terminal crossing survive, with smaller e/u traces beneath the horizontal cancellation. The middle letters remain partly masked, so deux stays tentative.','deletion state',marked='yes',crop='fonction_insertions',confidence='medium',cats=(5,7))
ch(11,'NB: interlinear replacement of deux',r'\inserted{une}',r'\ill{}',r'\inserted{une}','The raised u turn, n shoulder, and final e are separately legible above the cancelled word. This is an insertion replacing the struck numeral-word.','readable ink left as \\ill{}',marked='yes',crop='fonction_insertions',cats=(3,5,6))
ch(12,'NB: fonction numérique',r'fonction numérique',r'fonctions \ill{}',r'\unsure{fonction|fonctions} numérique','The word fonction is legible, but its terminal angular tail may be either the final n flourish or an additional s; singular remains the first reading without appeal to agreement with une. The next word has the n/um/er/ique sequence, including the descending q, and reads numérique.','misread word',marked='yes',crop='fonction_insertions',confidence='medium',cats=(2,5))
ch(13,'NB: inserted beta and punctuation',r'\inserted{$\beta$}',r'$\beta$,',r'\inserted{\uline{$\beta$},}','The beta has a short, separate, dark horizontal line below its body. A detached dark comma lies at its lower right. Both differ from the thinner oblique insertion guide. The underline and comma are retained with the insertion; H already has the comma.','insertion or placement',c_changed=True,crop='fonction_insertions',cats=(3,6,10))
ch(14,'Group definition: annotation over the indexed pi',r'\overset{\pi}{\overset{\Vert}{\hat\pi_{0,3}}}',r'\hat\pi_{0,3}',r'\overset{\pi}{\overset{\Vert}{\hat\pi_{0,3}}}','A small pi sits above two short near-vertical strokes, which in turn sit above the hat of the indexed pi. H describes the upper inscription only in an editorial note; the source annotation belongs in the transcription at its written position. Both feet of the indexed pi are curved.','insertion or placement',crop='group_definition',cats=(1,3,6))
ch(15,'Group definition: label over equality',r'\mathrm{def}',r'\text{déf}',r'\mathrm{def}','The label has d, a small e-like connector, and f. No separate accent stroke appears over the e position. The unaccented abbreviation is retained.','abbreviation expanded or spelling modernised',crop='group_definition',cats=(8,))
ch(16,'Group definition: name after equality',r'\Gamma',r'\Pi',r'\Gamma','The letter has two close, tall strokes forming the left stem, a long top bar, and only a short downturned tip on the right. There is no second full-height right leg.','misread symbol or index',crop='group_definition',cats=(1,),math='The author names the group Γ.')
ch(17,'After the group definition: cancelled donnée',r'\deleted{\unsure{donnée}}',r'\struck{\ill{}}',r'\deleted{\unsure{donnée}}','A leading rounded/ascending stroke and several small following humps remain under the cancellation. They support donnée tentatively, but the horizontal strike obscures the internal letters.','deletion state',marked='yes',crop='donnee_gamma',confidence='medium',cats=(5,7))
ch(18,'Continuation: gamma inserted after une autre',r'à valeurs dans $\hat{\mathbb Z}$, et une autre \inserted{$\gamma$} à valeurs',r'$\gamma$ à valeurs dans $\hat{\mathbb{Z}}$, et une autre à valeurs',r'à valeurs dans $\hat{\mathbb Z}$, et une autre \inserted{$\gamma$} à valeurs','The looped descending gamma is above the gap following autre, immediately before the second à valeurs. Its position does not attach it to the first à valeurs below the cancelled donnée.','insertion or placement',crop='donnee_gamma',cats=(3,6),math='The symbol γ labels the second function, with values in the quotient.')
ch(19,'Application display: domain',r'\Gamma',r'\Pi',r'\Gamma','The same doubled left stem and short downturned right tip occur as in the definition. The right tip does not extend down to the baseline.','misread symbol or index',crop='application_map',cats=(1,),math='The displayed application has domain Γ.')
ch(20,'Application display: after the codomain',r'\pi/\hat{\mathbb Z}\times\hat{\mathbb Z}^{*}',r'\pi/\hat{\mathbb{Z}}\times\hat{\mathbb{Z}}^{*},',r'\pi/\hat{\mathbb Z}\times\hat{\mathbb Z}^{*}','The star is the final ink of the upper display row. No comma follows it; the element map is written on a distinct lower row.','text not on the page',crop='application_map',cats=(9,))
ch(21,'Oblique margin: heading and map',r'\uline{NB} $\gamma_0:\mathcal E_0\longrightarrow\pi$',r'NB $\gamma:E_0\to\pi$',r'\uline{NB} $\gamma_0:\mathcal E_0\longrightarrow\pi$','A separate underline lies below NB. A small closed zero is below gamma. The source E has a curved calligraphic outline and its own zero. The rightward arrow has a single shaft and arrowhead.','misread symbol or index',crop='margin_nb',cats=(1,3,10),math='The marginal map is γ₀, not an unindexed γ.')
ch(22,'Oblique margin: words after the map',r'est un $1$-cocycle sur',r'\ill{} cocycle sur',r'est un $1$-cocycle sur','The est and un strokes are small but legible between the map and the next line. The initial numeral 1 precedes the cocycle word. The c/o/c/y/c/l/e sequence, including the long y descender, is visible.','readable ink left as \\ill{}',marked='yes',crop='margin_nb',cats=(3,5))
ch(23,'Oblique margin: group on which the cocycle is defined',r'$\mathcal E_0\unsure{=|\simeq}\operatorname{Aut}_{\mathrm{lac}}(\pi,L_0)$',r'\uncertain{$\Pi$} \ill{} $(\pi,L_0)$',r'$\mathcal E_0\unsure{=|\simeq}\operatorname{Aut}_{\mathrm{lac}}(\pi,L_0)$','The repeated curved E and its zero, the Aut letters and lower lac, and the arguments pi and L-zero are visible. The intervening relation is compressed and uneven; its upper trace is not plain enough to distinguish equality from the proposed isomorphism sign.','readable ink left as \\ill{}',marked='yes',crop='margin_nb',confidence='medium',cats=(1,3,5))
ch(24,'Oblique margin: cancelled group-word and raised replacement',r'\deleted{\unsure{groupe}} \inserted{\unsure{qui définit}} le ss-gr.',r'\ill{} \uncertain{1-cocycle} \ill{}',r'\deleted{\unsure{groupe}} \inserted{qui définit} le ss-gr.','The cancelled lower word has a g descender and subsequent rounded traces compatible with groupe, but several are crossed heavily. Above it, the q descender and the u/i strokes of qui are distinguishable, followed by the ascenders and dotted i strokes of définit. The live continuation reads le ss-gr.; no second separate 1-cocycle occurs here.','readable ink left as \\ill{}',marked='yes',crop='margin_nb',confidence='medium',cats=(3,5,6,7,8,9))
ch(25,'Oblique margin: final description of the subgroup',r'des éléments qui commutent ext. à $\unsure{\mathfrak S_3|\mathcal S_3}$',r'\ill{}',r'des éléments qui commutent ext. à $\unsure{\mathfrak S_3|\mathcal S_3}$','The low connected letters of des éléments qui and commutent are legible. The following abbreviation has ext and a stop, followed by à. The final ornate S has a small 3, but its exact font family remains unresolved.','readable ink left as \\ill{}',marked='yes',crop='margin_nb',confidence='medium',cats=(3,5,8))
ch(26,'Closing prose: cancellation after est injective',r'\deleted{\unsure{et}}',r'\struck{\ill{}}',r'\deleted{\unsure{et}}','A small loop and an upright survive inside heavy oblique cancellation strokes. They may be et, but the cancellation prevents a letter-by-letter certain reading.','deletion state',marked='yes',crop='closing_prose',confidence='medium',cats=(5,7))
ch(27,'Closing prose: connector before gamma prend',r'car',r'\ill{}',r'car','The short open c, low a connector and final r turn occur at the start of the next line before gamma. They form car.','readable ink left as \\ill{}',marked='yes',crop='closing_prose',cats=(5,))
ch(28,'Lower right: manuscript page number',r'\mspage{10}','',r'\mspage{10}','The lower-right inscription has a tall 1 with its rising entry stroke and a separate closed oval 0. It is handwritten source content and is absent from H.','omission',crop='footer10',cats=(3,))

# Every formal mark supplied in marks.tsv, in order.
def decision(mid,answer,reading,ink,crop,confidence):
    z=crops[crop]
    return dict(id=mid,decision=answer,reading=reading,ink=ink,crop=z['crop'],box=z['box'],confidence=confidence)
decisions=[
 decision('M0794','undecided',r'\unsure{\mathfrak S_3|\mathcal S_3}','The rounded outer sweep, top-right hook and inner curl are plain, as is the subscript 3. Their exact mathematical font family is not uniquely determined by this handwriting.','group_definition','medium'),
 decision('M0795','undecided',r'\unsure{=|\simeq}','The short upper relation trace is uneven and meets a curved lower trace. At this scale it cannot be classified confidently as two equality bars or the proposed isomorphism form.','margin_nb','low'),
 decision('M0796','first','qui définit','Above the cancelled word, qui has its descending q and small u/i strokes. The next word has distinct d and f ascenders, dotted i strokes, n and terminal t. The replacement itself is readable despite the cancellation below.','margin_nb','medium'),
 decision('M0797','undecided',r'\unsure{\mathfrak S_3|\mathcal S_3}','The final symbol repeats the rounded, hooked ornate S and a small subscript 3. The shape does not securely identify the font family.','margin_nb','medium'),
]

doubts=[
 dict(place='Opening cancellation',reading=r'\deleted{\unsure{pour $g$}}',alternatives=['pour g','partly obscured cancelled text'],confidence='low',reason='The g descender is clear; several strokes of pour remain crossed and faint.'),
 dict(place='Opening insertion, symbol after savoir',reading=r'\unsure{\tau|\zeta}',alternatives=[r'\tau',r'\zeta'],confidence='medium',reason='The small symbol combines a short upper stroke with a hooked or zigzag continuation. Tau remains the first reading, but the local shape alone leaves a zeta-like alternative.'),
 dict(place='Opening abbreviation',reading=r'\unsure{correspond.|correspond.\textsuperscript{t}}',alternatives=['correspond.',r'correspond.\textsuperscript{t}'],confidence='medium',reason='The stop is visible; a small raised adjoining trace is not securely separable from the nearby cancelled writing.'),
 dict(place='Opening cancelled word before à',reading=r'\deleted{\unsure{aux}}',alternatives=['aux','partly obscured cancelled text'],confidence='medium',reason='Three low letter traces support aux, but the strike prevents certainty for every letter.'),
 dict(place='NB cancelled word',reading=r'\deleted{\unsure{deux}}',alternatives=['deux','partly obscured cancelled text'],confidence='medium',reason='Initial d and terminal crossing are visible; the central e/u traces remain overlapped.'),
 dict(place='NB function word ending',reading=r'\unsure{fonction|fonctions}',alternatives=['fonction','fonctions'],confidence='medium',reason='The angular terminal tail can be a final n flourish or an additional s. The singular is retained first without grammatical normalization.'),
 dict(place='Group definition, ornate group symbol',reading=r'\unsure{\mathfrak S_3|\mathcal S_3}',alternatives=[r'\mathfrak S_3',r'\mathcal S_3'],confidence='medium',reason='The ink establishes the ornate S with index 3, but not an exact typographic alphabet.'),
 dict(place='Cancelled word following group definition',reading=r'\deleted{\unsure{donnée}}',alternatives=['donnée','partly obscured cancelled text'],confidence='low',reason='A leading ascending/rounded stroke and small humps support the proposed word; cancellation masks the interiors.'),
 dict(place='Oblique margin relation',reading=r'\unsure{=|\simeq}',alternatives=['=',r'\simeq'],confidence='low',reason='The compact uneven strokes do not settle equality versus the proposed isomorphism sign.'),
 dict(place='Oblique margin cancellation',reading=r'\deleted{\unsure{groupe}}',alternatives=['groupe','partly obscured cancelled text'],confidence='low',reason='The initial g-like descender and later rounded traces remain under a heavy strike; not every letter is plain.'),
 dict(place='Oblique margin final group symbol',reading=r'\unsure{\mathfrak S_3|\mathcal S_3}',alternatives=[r'\mathfrak S_3',r'\mathcal S_3'],confidence='medium',reason='The ornate S is legible, while the exact font family remains uncertain.'),
 dict(place='Closing cancellation',reading=r'\deleted{\unsure{et}}',alternatives=['et','partly obscured cancelled text'],confidence='low',reason='Dense diagonal strokes obscure much of the small loop and upright.'),
]

inventory=[]
def inv(i,kind,position,reading,box):
    inventory.append(dict(element=f'I{i:02}',kind=kind,position=position,first_words_or_objects=reading,box=box,sheet_kind='text',hand='his hand',transcribed='yes'))
inv(1,'text','Head, near the center','4',[790,0,940,65])
inv(2,'text','Opening baseline','plus haut, … correspond. … à',[220,21,1599,168])
inv(3,'deletion','Opening, after plus haut',r'\deleted{\unsure{pour $g$}}',[220,21,1599,168])
inv(4,'insertion','Above the first opening cancellation',r'\inserted{savoir $\unsure{\tau|\zeta}$}',[220,21,1599,168])
inv(5,'deletion','Opening, before à',r'\deleted{\unsure{aux}}',[220,21,1599,168])
inv(6,'display','Upper two-row system','p=-1; g=l_0^alpha l_1^beta; q=-1, r=1; ou mieux, beta=-1',[310,164,1608,408])
inv(7,'text','Main NB paragraph before the group definition','NB Si on remplace dans les calculs qui précèdent … sur le groupe',[221,490,1643,1201])
inv(8,'deletion','NB, before fonction',r'\deleted{\unsure{deux}}',[221,908,1457,1077])
inv(9,'insertion','NB, above cancelled deux',r'\inserted{une}',[221,908,1457,1077])
inv(10,'insertion','NB, after numérique',r'\inserted{\uline{$\beta$},}',[221,908,1457,1077])
inv(11,'display','Main group definition',r'\operatorname{Aut\,ext}_{\mathrm{lac}}(\overset{\pi}{\overset{\Vert}{\hat\pi_{0,3}}},\unsure{\mathfrak S_3|\mathcal S_3})\overset{\mathrm{def}}=\Gamma,',[500,1028,1283,1201])
inv(12,'insertion','Above indexed pi in group definition',r'\overset{\pi}{\Vert}',[500,1028,1283,1201])
inv(13,'deletion','After the group definition, above the following line',r'\deleted{\unsure{donnée}}',[1323,1080,1570,1164])
inv(14,'text','Continuation below group definition','à valeurs dans Zhat, et une autre … opération phi',[221,1170,1630,1515])
inv(15,'insertion','Over the gap after une autre',r'\inserted{$\gamma$}',[1240,1140,1400,1250])
inv(16,'display','Action defining phi',r'\varphi(\alpha)\cdot g=l_0^\alpha gl_1^{-\alpha}',[410,1530,1460,1695])
inv(17,'text','Caption over application','L’application',[220,1700,880,1810])
inv(18,'display','Application, upper row',r'(\gamma,\chi):\quad\Gamma\longrightarrow\pi/\hat{\mathbb Z}\times\hat{\mathbb Z}^{*}',[444,1843,1320,1985])
inv(19,'display','Application, lower row',r'u\longmapsto(\gamma(u),\chi(u))',[680,1965,1320,2090])
inv(20,'margin note','Long oblique note in the lower left margin','NB gamma_0:E_0 to pi est un 1-cocycle …',[21,1725,445,2344])
inv(21,'deletion','Inside oblique marginal note',r'\deleted{\unsure{groupe}}',[21,1725,445,2344])
inv(22,'insertion','Above cancelled groupe in marginal note',r'\inserted{qui définit}',[21,1725,445,2344])
inv(23,'text','Three closing baseline lines','est injective, … satisfaisant une relation',[279,2107,1615,2352])
inv(24,'deletion','Closing first line, after est injective',r'\deleted{\unsure{et}}',[279,2107,1615,2352])
inv(25,'text','Lower right footer','10',[1554,2274,1656,2354])

second=[]
def sb(num,kind,coords,reading):
    second.append(dict(box=f'B{num:02}',kind=kind,coords=coords,reading=reading))
sb(1,'Handwritten page number omitted by H',[790,0,940,65],r'\mspage{4}')
sb(2,'Opening insertions, cancellations, abbreviation disagreement and added symbol/ending doubts',[220,21,1599,168],r'plus haut, \deleted{\unsure{pour $g$}} \inserted{savoir $\unsure{\tau|\zeta}$}, \unsure{correspond.|correspond.\textsuperscript{t}} \deleted{\unsure{aux}} à')
sb(3,'Complete numerical system and ou mieux disagreement',[310,164,1608,408],r'\left\{\begin{aligned}p&=-1\qquad g=l_0^\alpha l_1^\beta\quad(\alpha+\beta=1),\ \alpha,\beta\in\mathbb Z)\\q&=-1,\ r=1\qquad\text{ou mieux, }\beta=-1\end{aligned}\right.')
sb(4,'NB underline, numeric subscripts and restant disagreement',[221,490,1643,829],r'\uline{NB} Si on remplace dans les calculs qui précèdent $L_0$ par $L_1$, alors $g$ est remplacé par $\rho(g)$, $q$ et $r$ restant inchangés. On trouve')
sb(5,'Character/function lexical differences, cancellation and une/beta insertions',[221,844,1643,1077],r'ainsi, en plus du caractère cyclotomique $\chi$, \deleted{\unsure{deux}} \inserted{une} \unsure{fonction|fonctions} numérique \inserted{\uline{$\beta$},} sur le')
sb(6,'Complete group definition with numeric indices, annotation, Greek-letter disagreement and ornate-S doubt',[500,1028,1283,1201],r'\operatorname{Aut\,ext}_{\mathrm{lac}}(\overset{\pi}{\overset{\Vert}{\hat\pi_{0,3}}},\unsure{\mathfrak S_3|\mathcal S_3})\overset{\mathrm{def}}=\Gamma,')
sb(7,'Cancelled word after definition',[1323,1080,1570,1164],r'\deleted{\unsure{donnée}}')
sb(8,'Gamma insertion and its attachment',[833,1140,1623,1302],r'et une autre \inserted{$\gamma$} à valeurs')
sb(9,'Complete action formula with numeric indices',[410,1530,1460,1695],r'\varphi(\alpha)\cdot g=l_0^\alpha gl_1^{-\alpha}')
sb(10,'Both application rows: Gamma disagreement, arrows and omitted/added punctuation',[444,1843,1320,2090],r'\[ (\gamma,\chi):\quad\Gamma\longrightarrow\pi/\hat{\mathbb Z}\times\hat{\mathbb Z}^{*} \]\[ u\longmapsto(\gamma(u),\chi(u)) \]')
sb(11,'Complete marginal note with all numbers, deletion, insertion and surviving formula doubts',[21,1725,445,2344],r'\margin{\uline{NB} $\gamma_0:\mathcal E_0\longrightarrow\pi$ est un $1$-cocycle sur $\mathcal E_0\unsure{=|\simeq}\operatorname{Aut}_{\mathrm{lac}}(\pi,L_0)$, \deleted{\unsure{groupe}} \inserted{qui définit} le ss-gr. des éléments qui commutent ext. à $\unsure{\mathfrak S_3|\mathcal S_3}$}')
sb(12,'Closing cancellation, car omission and uncertain H une',[279,2107,1615,2352],r'est injective, \deleted{\unsure{et}} $\beta$ étant défini par $\gamma$ car $\gamma$ prend ses valeurs dans les classes des $g\in\pi$ (mod $\varphi(\hat{\mathbb Z})$) satisfaisant une relation')
sb(13,'Handwritten footer number omitted by H',[1554,2274,1656,2354],r'\mspage{10}')

coverage=[]
def dc(row,status,ids=None,explanation=''):
    d=dict(row=row,status=status)
    if ids: d['change_id']=ids[0] if len(ids)==1 else ids
    if explanation:d['explanation']=explanation
    coverage.append(d)
dc(1,'substantive',['s011-01'],'The scan label 11 is editorial; the independently cropped handwritten 4 is a substantive omission from H.')
dc(2,'substantive',['s011-02'])
dc(3,'substantive',['s011-03','s011-04'])
dc(4,'macro/editorial',explanation='aligned versus cases implements the same handwritten left brace and two rows.')
dc(5,'substantive',['s011-05'])
dc(6,'macro/editorial',explanation='The comma token is the thin-space command \\, between factors in H, not a literal comma.')
dc(7,'substantive',['s011-06'])
dc(8,'macro/editorial',explanation='The aligned/cases difference and the dot of \\right. are TeX delimiters, not handwritten punctuation.')
dc(9,'macro/editorial',explanation='H editorial note about the opening insertion and difficult row; source text and placement are transcribed separately.')
dc(10,'substantive',['s011-08'])
dc(11,'substantive',['s011-09'])
dc(12,'substantive',['s011-10','s011-11','s011-12'])
dc(13,'substantive',['s011-13'],'The comma is present after the inserted beta; the same locus also restores its underline.')
dc(14,'macro/editorial',explanation='Aut\\,ext versus Autext is operator spacing alone; source letters are the same.')
dc(15,'substantive',['s011-14'])
dc(16,'macro/editorial',explanation='The alternative alphabet in C is a certainty notation, not extra source text. M0794 remains unresolved on its crop.')
dc(17,'substantive',['s011-15'])
dc(18,'substantive',['s011-16'])
dc(19,'substantive',['s011-17','s011-18'],'Separate the cancelled donnée from the gamma that H attaches to the wrong line.')
dc(20,'substantive',['s011-18'])
dc(21,'macro/editorial',explanation='H literal dot and C \\cdot encode the same visible multiplication point.')
dc(22,'macro/editorial',explanation='The comma tokens in H are \\, spacing between factors; no textual punctuation difference.')
dc(23,'substantive',['s011-14'],'The editorial wording is not source text, but the described upper pi and parallel strokes must be restored in position.')
dc(24,'substantive',['s011-19'])
dc(25,'substantive',['s011-20'],'Display separation is editorial; the literal comma added after the codomain is absent from the ink.')
dc(26,'substantive',['s011-21','s011-22','s011-23','s011-24','s011-25'],'H relocates the marginal block and gives a fragmentary reading. The complete note is transcribed in its marginal state; source differences are itemized.')
dc(27,'substantive',['s011-26'])
dc(28,'substantive',['s011-27'])
dc(29,'substantive',['s011-28','s011-21','s011-22','s011-23','s011-24','s011-25'],'The handwritten footer 10 is a separate omission; the marginal-note relocation and fragmentary text are accounted for in their own loci.')

report=dict(
 scan=11,reader='/root/reader_a',lines_read=27,
 layout='Upright handwritten sheet. A small 4 heads the page, followed by one opening baseline with an interlinear replacement and two cancellations, then a two-row braced system. A long NB paragraph contains a cancelled numeral-word, two replacements, an annotated group definition, a cancelled word and an inserted gamma; an action formula and a two-row application follow. Three closing body lines run beside an eight-line oblique left-margin NB with its own cancellation and replacement. The lower-right manuscript number is 10. The line count records nineteen main text/display baselines and eight marginal baselines; short interlinear additions and page numbers are inventoried separately. No drawing or diagram is present.',
 changes=changes,decisions=decisions,doubts=doubts,inventory=inventory,second_boxes=second,
 notation=[
  dict(observation='The two group-name glyphs are Gamma.',places=['Group definition','Application domain'],qualification='Both have a doubled tall left stem and only a short downturned tip at the right end of the top bar; the evidence is local to these two occurrences.'),
  dict(observation='The indexed hatted pi has curved feet; the upper annotation is a small pi over two near-vertical strokes.',places=['Group definition'],qualification='This local form supports lowercase pi. No uniform decision about other pages is inferred.'),
  dict(observation='The two permutation-group symbols have the same ornate rounded S form with subscript 3.',places=['Group definition','End of marginal note'],qualification='The exact font choice between fraktur and calligraphic remains doubtful.'),
  dict(observation='Gamma has a small high entry and a looped descender.',places=['Inserted gamma after une autre','Application pair','Oblique marginal gamma_0','Closing prose'],qualification='The inserted gamma is attached to the second function, and the marginal gamma has its own visible subscript zero.'),
  dict(observation='The upper application arrow has a single shaft and arrowhead; the lower element map has a left bar.',places=['Application display'],qualification='The ordinary arrow and mapsto distinction is visible at the endpoints.'),
  dict(observation='The operation is written phi(alpha) dot g = l_0^alpha g l_1^-alpha.',places=['Action formula'],qualification='The multiplication point and both numeric indices were read; no additional point between g and l_1 is transcribed.'),
 ],
 hand=[
  dict(habit='An outlined or doubled left stem can make Gamma resemble Pi.',places=['Group definition','Application domain'],universal_on_page='Yes, for these two group-name occurrences.',witness_effect='H reads both as Pi.'),
  dict(habit='A final connected flourish can resemble an added s or a raised abbreviation letter.',places=['fonction ending','correspond. ending'],universal_on_page='No; retained as local uncertainty.',witness_effect='H expands correspond. and reads fonctions; C readings remain first with local ending alternatives.'),
  dict(habit='Replacement letters may be written between baselines with a thin oblique guide.',places=['Inserted beta','Inserted gamma','une above cancelled deux'],universal_on_page='Observed locally; not every insertion uses a visible guide.',witness_effect='H loses une as illegible and attaches gamma to the wrong à valeurs; C omits the beta underline and comma.'),
  dict(habit='Heavy cancellation strokes leave only parts of small words visible.',places=['pour g','aux','deux','donnée','groupe','et'],universal_on_page='All six retain some uncertainty.',witness_effect='H gives illegible placeholders; C tentative readings are preserved without claiming full recovery.'),
 ],
 abbreviations=[
  dict(form='correspond.',expansion='correspondant',place='Opening; a possible raised t is retained only as an alternative.'),
  dict(form='NB',expansion='nota bene',place='Main paragraph and oblique margin.'),
  dict(form='Aut ext',expansion='automorphismes extérieurs',place='Group definition.'),
  dict(form='def',expansion='définition',place='Label over the equality defining Gamma; the source label is unaccented.'),
  dict(form='ss-gr.',expansion='sous-groupe',place='Oblique marginal note.'),
  dict(form='ext.',expansion='extérieurement',place='Oblique marginal note.'),
  dict(form='mod',expansion='modulo',place='Closing parenthesis; no stop is added.'),
 ],
 notes=[
  'The opening continues an earlier discussion and associates the inserted savoir-symbol with the displayed values p=-1, g=l_0^alpha l_1^beta, alpha+beta=1, q=-1 and r=1, followed by ou mieux, beta=-1. The extra closing parenthesis after alpha,beta in Z is visible and preserved. No algebraic correction or verification is claimed.',
  'The author says that replacing L_0 with L_1 in the preceding calculations replaces g by rho(g), with q and r unchanged. He introduces, in addition to the cyclotomic character chi, numerical and quotient-valued functions beta and gamma on a group named Gamma. The action phi(alpha) dot g = l_0^alpha g l_1^-alpha and the application (gamma,chi) are transcribed as written.',
  'The author states that this application is injective and that beta is determined by gamma, whose values are classes satisfying a relation continued beyond the sheet. The oblique marginal note calls gamma_0 a 1-cocycle and describes a subgroup through the inserted words qui définit. These are the author’s assertions, not checked results.',
  'Every C deletion and insertion has a separate inventory entry and second-pass coverage. The six cancelled-word doubts remain because the crossing strokes prevent a full letter-by-letter recovery. The unstruck marginal insertion qui définit is resolved on the saved crop. The word une in the final phrase satisfaisant une relation is legible despite H’s uncertainty.',
  'The main and marginal NB headings are underlined. The inserted beta has a distinct underline and a comma; the thinner oblique guide is separate. The comma is placed within the insertion in the proposed text. Root independently accepted these strokes and the separate header-4 crop.',
  'There is no date or explicit authorial uncertainty phrase such as peut-être or a question in this sheet. Ou mieux is an authorial reformulation and is retained. Handwritten numbers are 4 at the head and 10 at the lower right. Both have separate H-omission rows; the editorial scan identifier 11 is excluded from omission counting.',
  'No mathematical check, external research, OCR, recognition software or TeX compilation was used. The whole-page image and both original halves were read once; one enlarged crop was saved for each selected locus. The twelve original crops plus the distinct previously uncropped header numeral make thirteen saved crops. A batched display of three already-created crops was truncated by the tool before usable visual output, so those saved images were subsequently inspected individually without making additional crops.',
 ],
 check_events=[],diff_coverage=coverage
)
out=base/'edition/reader_reports/145_scan011.json'
out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'path':str(out),'changes':len(changes),'decisions':len(decisions),'doubts':len(doubts),'inventory':len(inventory),'second_boxes':len(second),'crops':len(manifest),'diff_rows':len(coverage)},ensure_ascii=False))
