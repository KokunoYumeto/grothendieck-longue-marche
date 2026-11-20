from pathlib import Path
import json, re, csv

ROOT = Path('/workspace/scratch/ddf8babdc42e')
OUT = ROOT / 'out/review'
C = (ROOT/'packets/scan009/C.tex').read_text()
H = (ROOT/'packets/scan009/H.tex').read_text()
MAN = json.loads((OUT/'scan009_crop_manifest.json').read_text())
CROPS = {x['name']: x for x in MAN['crops']}
REL = r'\mathrel{\tikz[baseline=-.4ex,x=.65em,y=.65em]{\draw (0,1.1)--(1,.5)--(0,-.1) (1,1.1)--(0,.5)--(1,-.1);}}'
HASH = r'\mathrel{\tikz[x=.55em,y=.60em,line cap=round]{\draw (0,-.12)--(0,1) (.48,-.12)--(.48,1) (-.06,.30)--(.54,.47) (-.05,.51)--(.53,.65);}}'
HOOK = r'\mathrel{\tikz[x=.5em,y=.28em]{\draw (0,.08)--(1.2,.08) (0,.42)--(1.2,.42) .. controls (1.35,.42) and (1.38,.23) .. (1.28,.2);}}'
UNDERARROW = r"\underset{\tikz[x=1em,y=.35em,baseline=0pt]{\draw (0,0) .. controls (1,-.05) and (2,-.05) .. (3.4,.40);\draw (1.66,.16)--(1.85,.01)--(1.67,-.13);}}{Y'\ll Y,\ X'\parallel K}"
LOWER_RULE = r'''% Editing stroke beneath the preceding cancelled draft, with rising right end.
\noindent\tikz[x=1em,y=1em]{\draw (0,.03) .. controls (2,.15) and (4,.18) .. (6,.12) .. controls (8,-.04) and (10,-.10) .. (11.1,-.08) .. controls (11.45,.55) and (11.55,.95) .. (12.2,1.18);}
'''
DRAW = r'''\figure{\begin{tikzpicture}[x=.035em,y=-.035em,line cap=round,line join=round]
\draw[thick] (30,10)--(106,10)--(85,76);
\draw[thick] (30,10)--(11,83)--(77,79)--(77,73);
\draw[thick] (30,10)--(46,26)--(70,56)--(85,76);
\draw[thick] (76,51) .. controls (84,41) and (76,25) .. (58,21)
 .. controls (52,20) and (48,22) .. (46,26)
 .. controls (34,35) and (34,50) .. (44,59)
 .. controls (53,66) and (64,64) .. (70,56);
\fill (46,26) circle (2.2) (70,56) circle (2.6);
\draw (26,60)--(38,66) (31.5,49)--(33,69);
\draw[thick] (103,52)--(134,56) (123,35)--(129,68);
\draw (123,39)--(122,67);
\draw (17,116)--(46,114) (33,98)--(33,131);
\end{tikzpicture}}'''

T=C
def replace(old,new,count=1):
    global T
    assert T.count(old)>=count, repr(old)
    T=T.replace(old,new,count)

replace(r'\unsure{L|\mathcal L}', 'L')
replace(r"X'\cap Y'=\varnothing", r"X'\cap Y'=\unsure{\varphi|\varnothing}")
replace(r'\unsure{immédiat}', 'immédiat')
replace(r'Z\ll X,\,Z\ll Y', r"Z\ll\unsure{X'|X},\,\unsure{Z'|Z}\ll\unsure{Y'|Y}")
replace(r"\unsure{d'où|comme}", r"\unsure{comme|d'où}")
replace(r'\Longrightarrow Z\leq L', r'\Longrightarrow\unsure{Z^{+}\leq L|Z+\leq L|Z\leq L}')
replace(r'Z\cap L=\varnothing', r'Z\cap L=\varphi')
replace(r'F,\unsure{C|G}\in', r'F,C\in')
replace(r"avec $F\parallel G$. Alors $F\ll F$", r"avec $F\parallel C$. Alors $F\ll F$")
replace(r'$\unsure{L}=\underset{Z\in\widetilde F\cap\widetilde G}{\mathrm{Sup}}\,Z$', r'$\unsure{L=\underset{Z\in\widetilde F\cap\widetilde G}{\mathrm{Sup}}\,Z}$')
replace(r"$F'\ll F,G'\ll G$. Supposons $F'\parallel L,\ G'\parallel L$", r"$F'\ll F,C'\ll G$. Supposons $F'\parallel L,\ C'\parallel L$")
replace('ateliers spacieux)', r'ateliers \unsure{spacieux|spécieux})')
replace(r'\unsure{tt}', 'tt')
replace(r"\underline{Y'\ll Y,\ X'\parallel K}", UNDERARROW)
replace("Alors}\n\nOn voudra", "Alors}\n\n"+LOWER_RULE+"\nOn voudra")
replace(r'\unsure{cf|Cf}', 'cf')
replace(r'\tikz[x=.5em,y=.5em]{\draw (0,0)--(0,4.25);}\enspace', '')
start=T.index(r'\figure{\begin{tikzpicture}')
end=T.index(r'\end{tikzpicture}}',start)+len(r'\end{tikzpicture}}')
T=T[:start]+DRAW+T[end:]
replace(r'\unsure{'+HASH+r'|\mathrel{\#}|\nparallel|\parallel}',HASH)
replace(r"\unsure{C'est un|C'est une}", "C'est un")
replace(r'\unsure{contre-exemple|contre-exple|contre exemple}', 'contre-exple')
replace(r"à l' \unsure{:}", "à l' :")
replace(r'\uline{At \unsure{DD|DC}}', r'% Vertical rule bordering the axiom on its left.'+'\n'+r'\margin{\tikz[x=.5em,y=.5em]{\draw (0,0)--(0,4.25);}}'+'\n'+r'\uline{At \unsure{DD|CD|DC}}')
replace(r'\inserted{\unsure{ancien|ou bien|ou bien,}}', r'\inserted{ou bien}')
replace(r'\unsure{o|,}', r'\unsure{o|et|,}')
replace(r"\unsure{l'énoncé|l'inverse} \deleted{\unsure{est}} est tjrs", r"l'inverse \deleted{\unsure{est}} tjrs")
replace(r'\uline{Corollaire}', r'\uline{Cor. Main}', 2)
replace(r"F\parallel G,\ F'\ll F,\ G'\ll G", r"F\parallel G,\ F'\ll F,\ C'\ll G")
replace(r"G,\ F'\ll F,\ G'\ll G$, alors", r"G,\ F'\ll F,\ C'\ll G$, alors")
(OUT/'scan009_proposed.tex').write_text(T)

changes=[]
def ch(id,place,c,h,final,shows,kind,crop,ac=False,ah=True,conf='high',marked=False,conseq=False):
    cp=CROPS[crop]
    changes.append(dict(id='009-'+id,place=place,C=c,H=h,final=final,scan_shows=shows,
      confidence=conf,kind=kind,crop=cp['file'],box=cp['box'],against_C=ac,against_H=ah,
      marked_in_H=marked,consequential=conseq))

ch('01','Opening paragraph, final words',"d'autres",r'\ill{}',"d'autres",'The apostrophe and linked a-u-t-r-e-s are visible after façons; no additional completion is supplied.',r'readable ink left as \ill{}','intro_end')
ch('02','At DC 1, ambient alphabet',r'\unsure{M|\mathcal M}',r'\mathcal M',r'\unsure{M|\mathcal M}','Two high outer strokes and low inner valley favour plain M; its alphabet remains doubtful under the cancellation. This governs the later ambient M forms.', 'misread symbol or index','atdc1',conf='medium',conseq=True)
ch('03','At DC 1, overwritten relation',r'\deleted{\unsure{\parallel}}'+REL,r'\between',r'\deleted{\unsure{\parallel}}'+REL,'The compatibility chevrons contain additional near-upright strokes of an earlier sign. Keep the cancelled parallel reading doubtful; the chevrons themselves are not a separate semantic difference from H.', 'deletion state (struck given live or live given struck)','atdc1',marked=True,conf='medium',conseq=True)
ch('04','At DC 1, mark following Y',r'\unsure{\text{\S}|?|.}','',r'\unsure{\text{\S}|?|.}','A compact dark curled terminal sign survives after Y; its components are too crowded to distinguish section mark, question mark or punctuation securely.', 'omission','atdc1',conf='low')
ch('05','At DC 1 follow, overwritten first word',r'\deleted{\unsure{Alors}}',r'\struck{At}',r'\deleted{\unsure{Alors}}','The beginning is A with a following tall/looped continuation, but a dense strike masks the remaining letters. Neither Alors nor At is fully certified.', 'misread word','atdc1_follow',conf='low',marked=True)
ch('06','At DC 1 follow, Soient above line',r'\inserted{Soient}','Soient',r'\inserted{Soient}','Soient stands above the crossed old opening, not on the old baseline.', 'insertion or placement','atdc1_follow',marked=False)
ch('07','At DC 1 added condition, L',r'\unsure{L|\mathcal L}','L','L','The final letter is a plain upright joined to a flat right foot; all of this letter is exposed in the inserted condition.', 'other','atdc1_follow',ah=False)
ch('08','At DC 1 added condition, parentheses',r"(i.e. $X'\parallel Z$ pour $Z\leq X,Y$)",r"i.e.\ $X'\parallel Z$ pour $Z\leq X,Y$",r"(i.e. $X'\parallel Z$ pour $Z\leq X,Y$)",'Both enclosing curved strokes are present around the i.e. clause.', 'other','atdc1_follow')
ch('09','At DC 1 follow, whole source state',r'\deleted{...Soient...Alors $X\prime\parallel Y\prime$}',r'Soient ... Alors $X\prime\parallel Y\prime$',r'\deleted{...Soient...Alors $X\prime\parallel Y\prime$}','Long oblique cancellation strokes cross this continuation as well as the upper statement. H mentions the cancellation editorially but does not mark the continuation as deleted.', 'deletion state (struck given live or live given struck)','upper_cancellation_scope',marked=True,conseq=True)
ch('10','NB marginal opening','La chose importante est',r'Il \ill{} choisi \ill{}','La chose importante est','La has a tall L and low a; chose has initial ch and final se; importante and est continue on the next slanted rows.', 'misread word','margin_nb')
ch('11','NB first empty-set glyph',r'\varnothing',r'\varnothing',r'\unsure{\varphi|\varnothing}','The oval has a long oblique stem extending below it. A separate long cancellation stroke also crosses this area, so the first occurrence retains a phi/empty-set-shape doubt.', 'misread symbol or index','margin_nb',ac=True,conf='medium',conseq=True)
ch('12','NB immédiat',r'\unsure{immédiat}',r'\uncertain{immédiat}','immédiat','All letters are visible on the slanted live row, with the accented ending and final t.', 'other','margin_nb',ah=False,marked=True)
ch('13','NB causal connective','Car',r'(\ill{}','Car','An open C, low a and final r precede the first Z formula; there is no independent opening parenthesis here.',r'readable ink left as \ill{}','margin_nb')
ch('14','NB first relation on Z',r'Z\deleted{\ll}\leq X\prime',r'Z\leq X\prime',r'Z\deleted{\ll}\leq X\prime','Two old chevron-like strokes are overwritten by the less-than-or-equal form. The cancelled component remains distinct from the live relation.', 'deletion state (struck given live or live given struck)','margin_nb',conseq=True)
ch('15','NB implication following the two Z hypotheses',r'Z\ll X,\,Z\ll Y',r'Z\ll X,\,Z\ll Y',r"Z\ll\unsure{X'|X},\,\unsure{Z'|Z}\ll\unsure{Y'|Y}",'Raised short strokes follow X and Y; there is also a short raised mark following the second Z. They favour primes, but the crowded oblique note leaves their attachment less than certain. No mathematical normalization is used.', 'misread symbol or index','margin_nb',ac=True,conf='low',conseq=True)
ch('16','NB two connectives after L and after parallel conclusion','or ... or','; ... ; et','or ... or','Each small connective consists of a low oval followed by a short r-like rise, not merely punctuation; the second precedes Z≪L.', 'misread word','margin_nb')
ch('17','NB cancelled impossible',r'\deleted{\unsure{impossible}}',r'\ill{}',r'\deleted{\unsure{impossible}}','The horizontal strike crosses a long word with visible initial im and ending strokes; the interior letters are not all plain, so the C doubt stays.', 'deletion state (struck given live or live given struck)','margin_nb',marked=True,conf='low')
ch('18','NB parenthetic connective',r"\unsure{d'où|comme}",r'\ill{}',r"\unsure{comme|d'où}",'The opening looks c-o and the continuation forms successive small humps; comme is favoured, but compression beside the cancelled word prevents a confident resolution.', 'misread word','margin_nb',ac=True,conf='medium',marked=True)
ch('19','NB parenthetic compatibility formula',r'Z'+REL+'L',r'\ill{}',r'Z'+REL+'L','The Z and L flank the opposed chevrons; a closing parenthesis is visible immediately after L.',r'readable ink left as \ill{}','margin_nb',marked=True,conseq=True)
ch('20','NB last implication, raised cross',r'\Longrightarrow Z\leq L',r'\Rightarrow Z\mathrel{\overline{\parallel}}L=\varnothing',r'\Longrightarrow\unsure{Z^{+}\leq L|Z+\leq L|Z\leq L}','A dark cross with a tall upright and transverse bar stands after Z, raised relative to the Z baseline; the following sign has the ≤ outline. Superscript +, baseline +, or an unattached correction stroke remain possible.', 'misread symbol or index','margin_nb',ac=True,conf='low',conseq=True)
ch('21','NB cancelled absurde',r'\deleted{\unsure{absurde}}','',r'\deleted{\unsure{absurde}}','A short heavily altered word before car retains the general outline but not every letter; preserve the cancelled doubt.', 'omission','margin_nb',conf='low')
ch('22','NB final causal word','car','','car','Three low linked letters c-a-r precede the final underlined formula.', 'omission','margin_nb')
ch('23','NB final underlined formula',r'\uline{$Z\cap L=\varnothing$ !}',r'$Z\mathrel{\overline{\parallel}}L=\varnothing$ !',r'\uline{$Z\cap L=\varphi$ !}','The intersection is an inverted U between Z and L; the final oval has a long slanting stem. A separate underline runs beneath the entire formula and exclamation point.', 'misread symbol or index','margin_nb',ac=True,conseq=True)
ch('24','Cor 1, first named second figure',r'\unsure{C|G}','G','C','The lower right foot is flat and open, with no inward/downward G return; the letter itself is fully visible despite the surrounding cancelled draft.', 'misread symbol or index','cor1',conseq=True)
ch('25','Cor 1, family alphabet',r'\unsure{\mathscr F|\mathcal F}',r'\mathfrak F',r'\unsure{\mathscr F|\mathcal F}','The large curled family letter is of the recurring script form. A diagonal cancellation crosses it, so the local script/calligraphic doubt is retained; it is not a Gothic letter.', 'misread symbol or index','cor1',conf='medium',conseq=True)
ch('26','Cor 1, avec F parallel second letter',r'F\parallel G',r'F\parallel G',r'F\parallel C','The second letter has the same open, flat-ended lower foot as the first C of this sentence, contrasting with the G in C′≪G below.', 'misread symbol or index','cor1',ac=True,conseq=True)
ch('27','Cor 1, Alors first refinement',r'F\ll F',r"F'\ll F",r'F\ll F','The space above and to the right of the first F is blank; the upper framing includes the place where a prime would stand.', 'misread symbol or index','cor1',conseq=True)
ch('28','Cor 1, second refinement',r"C'\ll G",r"G'\ll G",r"C'\ll G",'The first letter is the open C; the following G has a visible downward return, providing a direct same-line comparison.', 'misread symbol or index','cor1',conseq=True)
ch('29','Cor 1 whole state',r'\deleted{Cor 1 ...}',r'Cor 1 ...',r'\deleted{Cor 1 ...}','The same long oblique cancellations cross the first corollary; it is part of the cancelled upper draft.', 'deletion state (struck given live or live given struck)','upper_cancellation_scope',marked=True,conseq=True)
ch('30','Cor 2 old supremum formula',r'\deleted{$\unsure{L}=\underset{Z\in\widetilde F\cap\widetilde G}{\mathrm{Sup}}\,Z$}',r'\struck{\ill{}}',r'\deleted{$\unsure{L=\underset{Z\in\widetilde F\cap\widetilde G}{\mathrm{Sup}}\,Z}$}','Dense loops cross the whole former formula. Fragments support C’s suggested supremum expression but do not expose every token; the whole expression, rather than only L, is explicitly doubtful.',r'readable ink left as \ill{}','cor2',conf='low',marked=True,conseq=True)
ch('31','Cor 2, inserted L definition',r'\inserted{$L=F\cap G$}',r'\add{$L=F\cap G$}',r'\inserted{$L=F\cap G$}','The replacement stands above the obliterated supremum expression. Retained identically in content and insertion state.', 'other','cor2',ah=False,marked=True,conseq=True)
ch('32','Cor 2, second refinement',r"G'\ll G",r"G'\ll G",r"C'\ll G",'The prime follows an open C with a flat foot; the G after ≪ has a lower return. The writer’s inconsistency is preserved.', 'misread symbol or index','cor2',ac=True,conseq=True)
ch('33','Cor 2, second parallel hypothesis',r"G'\parallel L",r"G'\parallel L",r"C'\parallel L",'The left letter is the same open C form as the preceding C′≪G, not the returned G in the conclusion.', 'misread symbol or index','cor2',ac=True,conseq=True)
ch('34','Cor 2 whole state',r'\deleted{Cor. 2 ...}',r'Cor. 2 ...',r'\deleted{Cor. 2 ...}','The oblique cancellation strokes continue through the second corollary; H’s editorial description does not supply its missing source-state wrapper.', 'deletion state (struck given live or live given struck)','upper_cancellation_scope',marked=True,conseq=True)
ch('35','At DC 2 epithet','spacieux','spécieux',r'\unsure{spacieux|spécieux}','After sp the small round letter favours a and the ending is cieux. The crossing/crowding leaves a/e less than fully secure.', 'misread word','atdc2_header',conf='medium')
ch('36','At DC 2 old opening',r'\deleted{\unsure{Soit|Soient}}','Soient',r'\deleted{\unsure{Soit|Soient}}','A local strike crosses the opening independently of the large oblique cancellation; the ending is not fully exposed.', 'deletion state (struck given live or live given struck)','atdc2_header',conf='low')
ch('37','At DC 2 overwritten L before K',r'\deleted{\unsure{L}}K','K',r'\deleted{\unsure{L}}K','The heavy K contains an older upright/foot-like component. It is not legible enough to remove the underlying-letter doubt.', 'deletion state (struck given live or live given struck)','atdc2_formula',conf='low',conseq=True)
ch('38','At DC 2 quantifier abbreviation',r'\unsure{tt}','tous','tt','Two short t staves share a cross-stroke; there is no following ous sequence. These letter strokes are exposed.', 'abbreviation expanded or spelling modernised','atdc2_assumptions')
ch('39','At DC 2 graphic beneath two assumptions',r"\underline{Y'\ll Y,\ X'\parallel K}",r"Y'\ll Y,\ X'\parallel K",UNDERARROW,'A shallow curved stroke has two short arms meeting as a right-pointing head near its middle, beneath Y′≪Y, X′∥K. The rising right end continues under K.', 'misread symbol or index','atdc2_assumptions',ac=True,conseq=True)
ch('40','At DC 2 lower editing stroke','',r'\note{...encadré...}',LOWER_RULE.strip(),'A long lower stroke runs under on ait ... Alors and bends upward at the right; it is reproduced as an editing graphic, not as a mathematical conclusion.', 'other','atdc2_end',ac=True,marked=True)
ch('41','Transition before live property','voudra','voudrait','voudra','The final round a closes the word; no i and t follow it.', 'misread word','onvoudra')
ch('42','Live heading','Propriété 1','Proposition 1',r'\uline{Propriété 1}','The central letters read prié and the ending té, with no posit sequence. The underline extends through the numeral.', 'misread word','propriete')
ch('43','Live family-letter occurrences',r'\mathscr F',r'\mathfrak F',r'\mathscr F','The recurring family sign is the script F form already introduced on this page; the live occurrence in Propriété 1 confirms its curling outline. One alphabet entry covers the repetitions.', 'misread symbol or index','propriete',conf='medium',conseq=True)
ch('44','Reference opening',r'\unsure{cf|Cf}',r'cf.','cf','The first c is a small open curve, followed by tall f. No independent live full stop follows f; the following cancelled p. is separately retained.', 'other','reference')
ch('45','Reference cancelled p.',r'\deleted{\unsure{p.}}','',r'\deleted{\unsure{p.}}','A small locally cancelled letter/dot group lies between cf and GF; preserve C’s doubt because the strike masks part of it.', 'omission','reference',conf='low')
ch('46','Reference Roman volume',r'\underline{\overline{\mathrm{VI}}}',r'VI',r'\underline{\overline{\mathrm{VI}}}','Two separate horizontal strokes enclose VI, one above and one below.', 'misread symbol or index','reference')
ch('47','Reference page digits',r'\uline{\unsure{73|13}}','73',r'\uline{\unsure{73|13}}','The first digit favours 7 by its upper stroke and descending leg, but the short upper part does not make 1 impossible. A separate underline is present.', 'other','reference',conf='medium')
ch('48','Reference sentence abbreviation','tjrs','','tjrs','Four compact letter movements stand between cas and the double-shaft arrow.', 'omission','reference')
ch('49','Reference sentence arrow',r'\unsure{'+HOOK+r'|\Rightarrow}',r'\Longrightarrow',r'\unsure{'+HOOK+r'|\Rightarrow}','Both shafts are visible; the right end curls downward rather than showing a fully exposed angular head. The existing explicit-shape primary is retained with its arrow alternative.', 'misread symbol or index','reference',conf='medium',conseq=True)
ch('50','Reference sentence source state','cf ... On a ... tjrs [arrow]',r'\struck{cf ... On a ... [arrow]}','cf ... On a ... tjrs [arrow]','The long horizontal strike belongs to the lower Montrons row. The reference and On a row remains live above it.', 'deletion state (struck given live or live given struck)','reference',conseq=True)
ch('51','Separate cancelled Montrons row',r"\deleted{\unsure{Montrons} qu'on a bien \unsure{en} $\Rightarrow$. En effet,}",r'\struck{... [arrow]. En effet,}',r"\deleted{\unsure{Montrons} qu'on a bien \unsure{en} $\Rightarrow$. En effet,}",'Montrons, qu’on a bien, the small en candidate, implication arrow and En effet occupy their own struck row; C’s two lexical doubts remain because the crossing ink obscures letters.', 'omission','cancelled_montrons',conf='medium',conseq=True)
ch('52','Ceci parenthetical explanation','(si on le voit de façon générale)',r'\ill{} (\ill{} \ill{})','(si on le voit de façon générale)','Both parentheses and each of the seven words are readable; the accent strokes in façon/générale are retained normally.',r'readable ink left as \ill{}','ceci_equivalent')
ch('53','H insertion after cancelled En effet','',r'\add{\ill{} \ill{}}','','No separate interlinear word pair occurs here: the next visible row begins Ceci est équivalent. H’s two added illegible words are not independently supported.', 'text not on the page','ceci_equivalent')
ch('54','Slanted criterion heading','pour les raffinements de sous-figures',r'\struck{\ill{}} \add{\ill{}}',r'pour les raffinements de \uline{sous-figures}','The phrase can be read across the crowded slanted rows. The long line follows beneath sous-figures, favouring underlining rather than a new deleted-and-replaced phrase; the crowded scope remains in the doubts.',r'readable ink left as \ill{}','margin_criterion',conf='medium')
ch('55','Vertical border rule placement',r'\margin{[vertical rule] Critère ...}',r'\note{Un trait vertical le borde à gauche}',r'\margin{\tikz[x=.5em,y=.5em]{\draw (0,0)--(0,4.25);}}','The original near-vertical rule lies immediately left of the main At DD block, from its heading through its conclusion, not before the slanted word Critère.', 'insertion or placement','atdd1_rest',ac=True,marked=True)
ch('56','Simplicial example drawing',r'Rotated quadrilateral; \unsure{x|+}, \unsure{X|x}, \unsure{X|Y} nodes',r'H_drawing.tex: closed oval; quadrilateral and graphical crosses',DRAW,'Four skew boundary sides, one upper-left/lower-right diagonal, two heavy points, an irregular oval with a small lower-right gap, and three graphical crosses. The bottom edge stops short and turns upward. The crosses are strokes, not alphabetic labels; the right upright is retraced.', 'drawing or diagram','drawing',ac=True,conseq=True)
ch('57','Lower margin conclusion relation',r'\unsure{'+HASH+r'|\mathrel{\#}|\nparallel|\parallel}',r'\mathrel{\overline{\parallel}}',HASH,'Two near-uprights are crossed by two separate short ascending bars. C’s explicit drawn primary reproduces the visible sign; one overbar would omit a bar and its placement.', 'misread symbol or index','margin_after_figure',marked=True,conseq=True)
ch('58','Lower margin C’est un',r"\unsure{C'est un|C'est une}","(c'est un","C'est un",'The noun article is un with no final e. The large initial curve is C itself, followed by its apostrophe; there is no additional opening parenthesis before it.', 'misread word','margin_after_figure')
ch('59','Lower margin counterexample abbreviation',r'\unsure{contre-exemple|contre-exple|contre exemple}',r'contre-ex.','contre-exple','After contre-ex the visible tall p/l sequence and small ending support exple; no intervening em sequence is visible. This short spelling is preserved.', 'abbreviation expanded or spelling modernised','margin_after_figure',ac=True,conf='medium')
ch('60','Lower margin à l’ and colon',r"à l' \unsure{:}",'à',"à l' :",'The small l with apostrophe follows à; two dark separated dots precede At on the next slanted row.', 'omission','margin_after_figure')
ch('61','Lower margin first axiom label',r'At $\parallel$','At 11',r'At $\parallel$','The first pair are two simple unheaded parallel strokes. The later At 11 has headed digit strokes, which are preserved separately.', 'misread symbol or index','margin_after_figure',conseq=True)
ch('62','Lower margin strengthening','et a fortiori à',r'et \ill{}','et a fortiori à','The linked a, tall f, ortiori sequence and accented terminal à are visible across the slanted row.',r'readable ink left as \ill{}','margin_after_figure')
ch('63','Lower margin deleted ex',r'\deleted{\unsure{ex}}','',r'\deleted{\unsure{ex}}','An altered small group before the second At has an e/x-like outline; crossing ink prevents full certification.', 'omission','margin_after_figure',conf='low')
ch('64','Lower margin GF VI reference location',r'(cf GF $\underline{\overline{\mathrm{VI}}}$, p. 67,68)',r'Main axiom: (cf. GF VI); margin: p.67,68',r'(cf GF $\underline{\overline{\mathrm{VI}}}$, p. 67,68)','The cf GF VI inscription shares the slant and continuation of the marginal counterexample note; p.67,68 is its next row. Both VI bars are present. It is not inserted between implique and X′ in the main axiom.', 'insertion or placement','margin_after_figure',conseq=True)
ch('65','Live axiom altered label',r'\unsure{DD|DC}','CD',r'\unsure{DD|CD|DC}','Both letters are overwritten/retraced. DD best matches the visible closed uprights and bowls, but the order of overwriting cannot be recovered; CD and DC remain alternatives without inventing a legible earlier state.', 'misread word','atdd1_first',conf='low',marked=True,conseq=True)
ch('66','Live axiom interlinear addition',r'\inserted{\unsure{ancien|ou bien|ou bien,}}',r'\add{ou \uncertain{ancien}}',r'\inserted{ou bien}','The slanted addition separates into ou and a b-i-e-n sequence; the initial lower oval and u are distinct from the upper word. It rises from just after Soient. The crop framing was extended before deciding this previously clipped phrase.', 'misread word','atdd1_first',ac=True,conf='medium',marked=True)
ch('67','Live axiom separator between pairs',r'\unsure{o|,}','et',r'\unsure{o|et|,}','A small oval crossed by a short return lies between Y and X′. Its compact shape does not securely distinguish o from compressed et or punctuation.', 'misread word','atdd1_first',conf='low')
ch('68','Live axiom intersection definition',r'K=X\cap Y',r'K=X\wedge Y',r'K=X\cap Y','The sign is a rounded inverted U, with the same local shape as the intersection in the supremum index.', 'misread symbol or index','atdd1_rest',conseq=True)
ch('69','Live axiom NB word',r"\unsure{l'énoncé|l'inverse}","l'inverse","l'inverse",'After l’ the short i and n are followed by a v-like joining stroke and the erse ending; the word is not énoncé.', 'misread word','atdd1_rest',ac=True,ah=False)
ch('70','Live axiom NB cancelled est and extra live est',r'\deleted{\unsure{est}} est',r'\ill{}',r'\deleted{\unsure{est}}','Only one locally cancelled word stands between l’inverse and tjrs. Its suggested est remains doubtful under the crossing; no second independent live est is visible.', 'text not on the page','atdd1_rest',ac=True,conf='medium')
ch('71','Live axiom NB abbreviation','tjrs','toujours','tjrs','The initial tall t, descending j and short rs are the written abbreviation; the expanded form is absent.', 'abbreviation expanded or spelling modernised','atdd1_rest')
ch('72','Live axiom NB placement','After implique X′ [compatibility] Y′','Before implique','After implique X′ [compatibility] Y′','The parenthetic note sits to the right of the concluding lower line. It does not interrupt the preceding X′_L compatibility Y′_L hypothesis.', 'insertion or placement','atdd1_rest')
ch('73','First live corollary label','Corollaire 1','Cor. Main 1',r'\uline{Cor. Main} 1','After the short Cor. the next word begins with a tall M and continues a-i-n. The underline runs beneath the label; numeral 1 follows it.', 'misread word','cor_main1',ac=True,ah=False)
ch('74','First live corollary wording and grouping',r'la ``propriété\textquotesingle\textquotesingle ci dessus',r'(cf. la « propriété » ci-dessus) [first implication formula]',r"la ``propriété'' ci dessus",'The line contains la, the high paired quotation ticks, propriété and ci dessus. There is no cf. or enclosing parenthesis. The implication formula begins on the next row beside the second numbered label.', 'text not on the page','cor_main1',conseq=True)
ch('75','Second live corollary label','Corollaire 2','Cor. Main 2',r'\uline{Cor. Main} 2','The same Cor. Main letter forms recur, followed by the hooked digit 2.', 'misread word','cor_main2',ac=True,ah=False)
ch('76','Second live corollary formula alignment','Formula beside Corollaire 2','Formula assigned to Cor. Main 1','Formula beside Cor. Main 2','The horizontal formula F∥G ... ⇒F′∥G′ begins immediately to the right of the second label, on its baseline.', 'insertion or placement','cor_main2',conseq=True)
ch('77','Second live corollary second refinement',r"G'\ll G",r"G'\ll G",r"C'\ll G",'The prime follows a flat-ended open C, contrasting with the returned G immediately after ≪ and with the conclusion’s G′.', 'misread symbol or index','cor_main2',ac=True,conseq=True)
ch('78','Generalization opening','Plus gén.','','Plus gén.','The two words and the terminal abbreviation dot are visible at the left of the Si row; this is a continuation below Cor. Main 2, not a fresh numbered corollary.', 'omission','plus_gen')
ch('79','Generalization second refinement',r"G'\ll G",r"G'\ll G",r"C'\ll G",'The second refinement again starts with an open flat-footed C′. The following G and both G′ forms in the final equivalence retain short returned feet.', 'misread symbol or index','plus_gen',ac=True,conseq=True)
ch('80','At DC 1 heading underline',r'\uline{At} DC 1','At DC 1',r'\uline{At} DC 1','A short underline runs below At and stops before DC; it remains distinct from the cancellation line above.', 'other','atdc1')
ch('81','Cor 1 heading underline scope',r'\uline{Cor} 1',r'\emph{Cor 1}',r'\uline{Cor} 1','The short source underline stops beneath Cor, before the numeral 1.', 'other','cor1')
ch('82','At DC 2 heading underline scope',r'\uline{At DC} 2',r'\emph{At DC 2}',r'\uline{At DC} 2','The line ends below DC and does not continue under the raised numeral 2.', 'other','atdc2_header')
ch('83','Live axiom heading underline scope',r'\uline{At \unsure{DD|DC}} 1',r'\emph{At CD 1}',r'\uline{At \unsure{DD|CD|DC}} 1','The underline ends under the altered letters, before the following numeral 1.', 'other','atdd1_first',conf='medium')
ch('84','Lower corollary heading underline scopes',r'\uline{Corollaire} 1; \uline{Corollaire} 2',r'\emph{Cor. Main 1}; \emph{Cor. Main 2}',r'\uline{Cor. Main} 1; \uline{Cor. Main} 2','Each source rule is below the lettered label; the following numeral lies beyond its right endpoint. The lexical correction is recorded separately.', 'other','cor_main2')
ch('85','NB label underline',r'\uline{NB}','NB',r'\uline{NB}','A separate short stroke lies immediately beneath the two label letters.', 'other','margin_nb')
ch('86','Criterion heading underlines',r'\uline{Critère} de \uline{compatibilité}','Critère de compatibilité',r'\uline{Critère} de \uline{compatibilité}','Separate lines follow under Critère and compatibilité; these are distinct from the crowded sous-figures line discussed separately.', 'other','margin_criterion')

doubts=[]
def doubt(place,reading,alts,reason,conf='medium'):
    doubts.append(dict(place=place,reading=reading,alternatives=alts,confidence=conf,reason=reason))
doubt('At DC 1 ambient family',r'M',[r'\mathcal M'],'Alphabet ambiguity retained at first occurrence; later M forms follow that primary.')
doubt('At DC 1 overwritten relation',r'\deleted{\parallel}',[],'Not every underlying stroke is recoverable beneath the compatibility sign.','low')
doubt('At DC 1 terminal mark',r'\text{\S}',['?','.'],'Small crowded curled sign under the upper cancellation.','low')
doubt('At DC 1 old opening','Alors',['At'],'Dense horizontal strike masks the middle and ending; C doubt must stay.','low')
doubt('NB empty-set-shaped sign',r'\varphi',[r'\varnothing'],'Long stem and oval favour phi, with a separate cancellation stroke complicating the first occurrence.')
doubt('NB first Z refinement',r"Z\ll X'",[r'Z\ll X'],'A raised short mark follows X; its small scale leaves attachment less than certain.','low')
doubt('NB second Z refinement',r"Z'\ll Y'",[r"Z\ll Y'",r"Z'\ll Y",r'Z\ll Y'],'Two short raised strokes favour primes after Z and Y. Preserve the visible candidates without a mathematical repair.','low')
doubt('NB cancelled word','impossible',[],'Cancellation crosses the internal letters; not all are exposed.','low')
doubt('NB parenthetic word','comme',["d'où"],'Low initial c/o and small humps favour comme but the word is crowded.')
doubt('NB final implication',r'Z^{+}\leq L',[r'Z+\leq L',r'Z\leq L'],'A tall cross follows Z above its baseline; its status as exponent, ordinary plus, or correction stroke remains open.','low')
doubt('NB cancelled word','absurde',[],'The local alteration obscures several internal strokes.','low')
doubt('Cor 1 family alphabet',r'\mathscr F',[r'\mathcal F'],'Script family F crossed by a long deletion stroke; retained first-page occurrence doubt.')
doubt('Cor 1 authorial inconsistency',r'F,C;\ F\parallel C;\ F\ll F;\ C\prime\ll G;\ F\prime\parallel G\prime',[],'The C and missing first prime are source readings, even though later terms use G and F′. No normalization.','high')
doubt('Cor 2 cancelled old formula',r'L=\underset{Z\in\widetilde F\cap\widetilde G}{\mathrm{Sup}}\,Z',[],'Heavy scribbling prevents certification of the whole expression; the original C sequence is only a candidate.','low')
doubt('Cor 2 inconsistent letters',r'C\prime\ll G;\ C\prime\parallel L;\ F\prime\parallel G\prime',[],'The two antecedent letters are open C′; the final letter has a returned G′ foot. Retain this inconsistency.','high')
doubt('At DC 2 epithet','spacieux',['spécieux'],'Small a/e shape in cancelled heading remains somewhat compressed.')
doubt('At DC 2 old opening','Soit',['Soient'],'Local strike prevents every letter being read.','low')
doubt('At DC 2 underlying letter','L',[],'Overwritten by heavy K; original foot/stem only partly available.','low')
doubt('Reference cancelled p.','p.',[],'Local stroke partly masks the small letter and dot.','low')
doubt('Reference page number','73',['13'],'A 7 is favoured, but the upper stroke is short.')
doubt('Reference arrow',HOOK,[r'\Rightarrow'],'Two shafts clear; the curled end remains unlike a fully exposed ordinary arrowhead.')
doubt('Cancelled Montrons row','Montrons',[],'Several letters intersect the strike.','low')
doubt('Cancelled Montrons row small word','en',[],'Very short word under the strike; C doubt retained.','low')
doubt('Criterion source state',r'\uline{sous-figures}',[r'\deleted{sous-figures}'],'The stroke lies under most of the phrase but crowds the next row. Live underlining is favoured; root should adjudicate the scope.')
doubt('Lower margin cancelled abbreviation','ex',[],'Overwriting prevents full recovery.','low')
doubt('Live axiom altered label','DD',['CD','DC'],'Retraced bowls and uprights do not securely expose overwriting order.','low')
doubt('Live axiom separator','o',['et',','],'Compact oval and crossing/return stroke between the two variable pairs.','low')
doubt('Live axiom cancelled copula','est',[],'One word is crossed; it cannot be certified letter by letter.','low')
doubt('Lower live corollary authorial inconsistency',r'C\prime\ll G',[],r'Both lower assumptions use an open C′ while their conclusions retain G′.','high')

inventory=[
 dict(element='Manuscript page number',kind='text',position='top centre, x≈640 y≈70',first_words_or_objects='8'),
 dict(element='Opening explanation',kind='text',position='upper main column',first_words_or_objects="J'explicite, à cause de son importance"),
 dict(element='First cancelled axiom',kind='deletion',position='y≈460–660',first_words_or_objects='At DC 1 : Soient X,Y'),
 dict(element='Replacement opening',kind='insertion',position='above old first word of continuation',first_words_or_objects='Soient'),
 dict(element='Added first-axiom condition',kind='insertion',position='between upper axiom rows',first_words_or_objects="avec X′∥X∩Y=L"),
 dict(element='Oblique NB proof',kind='margin note',position='left margin, y≈620–1465',first_words_or_objects='NB La chose importante est'),
 dict(element='First upper corollary',kind='deletion',position='y≈670–800',first_words_or_objects='Cor 1 Soient F,C'),
 dict(element='Second upper corollary',kind='deletion',position='y≈780–895',first_words_or_objects='Cor. 2 Soient F,G'),
 dict(element='Cancelled old supremum definition',kind='deletion',position='inside Cor 2, before replacement L definition',first_words_or_objects='L=Sup Z'),
 dict(element='Replacement L definition',kind='insertion',position='above old Cor 2 definition',first_words_or_objects='L=F∩G'),
 dict(element='Second cancelled axiom',kind='deletion',position='y≈890–1235',first_words_or_objects='At DC 2 (Axiome des ateliers spacieux)'),
 dict(element='Curved assumption arrow',kind='drawing',position='under Y′≪Y, X′∥K',first_words_or_objects='one curved stroke, one mid-stroke right-pointing head'),
 dict(element='Lower editing boundary',kind='drawing',position='beneath cancelled At DC 2',first_words_or_objects='long shallow stroke and rising right end'),
 dict(element='Transition',kind='text',position='y≈1265',first_words_or_objects='On voudra la'),
 dict(element='Live property',kind='text',position='y≈1325–1415',first_words_or_objects='Propriété 1 Soient F,G'),
 dict(element='Two-line equivalence',kind='display',position='y≈1430–1530',first_words_or_objects='F′ [compatibility] G′; ⇔ F′_L [compatibility] G′_L'),
 dict(element='Live reference and implication remark',kind='text',position='y≈1540–1610',first_words_or_objects='cf GF VI, p.73 — On a en tous cas tjrs'),
 dict(element='Cancelled attempted demonstration',kind='deletion',position='separate row below reference',first_words_or_objects="Montrons qu'on a bien en"),
 dict(element='Equivalence explanation',kind='text',position='y≈1640–1745',first_words_or_objects='Ceci est équivalent (si on le voit de façon générale)'),
 dict(element='Slanted criterion and counterexample introduction',kind='margin note',position='left margin, y≈1570–2125',first_words_or_objects='Critère de compatibilité pour les raffinements de sous-figures'),
 dict(element='Simplicial counterexample',kind='drawing',position='lower left, x≈46–199 y≈2125–2268',first_words_or_objects='skew quadrilateral, diagonal, two dots, gapped oval, three crosses'),
 dict(element='Counterexample continuation',kind='margin note',position='lower slanted margin y≈1900–2348',first_words_or_objects='Mais on aura X′_L∥Y′_L'),
 dict(element='Live replacement axiom',kind='text',position='main column y≈1750–2020',first_words_or_objects='At DD 1 Soient'),
 dict(element='Slanted axiom addition',kind='insertion',position='above/right of Soient in live axiom',first_words_or_objects='ou bien'),
 dict(element='Axiom left rule',kind='drawing',position='x≈297, y≈1830–2015',first_words_or_objects='single vertical rule'),
 dict(element='First live corollary',kind='text',position='main column y≈2050–2120',first_words_or_objects='Cor. Main 1 la “propriété” ci dessus'),
 dict(element='Second live corollary',kind='display',position='main column y≈2120–2200',first_words_or_objects='Cor. Main 2 F∥G, F′≪F, C′≪G ⇒ F′∥G′'),
 dict(element='Generalization',kind='text',position='y≈2200–2260',first_words_or_objects='Plus gén. Si F [compatibility] G'),
 dict(element='Final equivalence',kind='display',position='y≈2260–2340',first_words_or_objects='F′∥G′ ⇔ F′_L∥G′_L'),
]

notation=[
 dict(form=REL,reading='compatibility relation',place='At DC 1 and throughout',observation='Opposed open chevrons cross to form a central diamond. Equivalent H between rendering is not counted repeatedly as a semantic correction.'),
 dict(form=r'\ll',reading='refinement',place='all axiom/corollary assumptions',observation='Two distinct left chevrons; not ≤. Full formulas and indices were checked.'),
 dict(form=r'\leq',reading='inclusion/order sign',place='NB and inserted i.e. clause',observation='Single chevron with separate lower bar; distinguish overwritten ≪ in NB.'),
 dict(form=r'\varphi',reading="l'ensemble vide",place='NB first and final empty-set expressions',observation='Written oval with a long oblique stem; first occurrence retains phi/varnothing shape doubt because of crossing ink.'),
 dict(form=HASH,reading='crossed parallel-like conclusion sign',place='counterexample marginal implication',observation='Two upright strokes crossed by two short bars. The explicit source-shaped graphic is retained without assigning a normalized relation.'),
 dict(form=r'\underline{\overline{\mathrm{VI}}}',reading='Roman VI enclosed above and below',place='both GF references',observation='Separate overbar and underline, not a plain numeral.'),
 dict(form='tt; tjrs; gén.; contre-exple',reading='written abbreviations',place='At DC 2; both NB/reference remarks; generalization; counterexample',observation='Short forms remain unexpanded in the page text.'),
 dict(form=r'K / L',reading='distinct letters kept',place='live At DD 1',observation='Definition uses K while the compatibility hypothesis uses subscript L. This is left as written.'),
]
hand_log=[
 dict(habit='C and G distinguished by lower return',place='Cor 1, Cor 2, both lower corollaries',observation='Open flat feet identify C; a short inward/downward return identifies G. Clear mismatches with the surrounding argument are preserved. The first L comma was checked against the upper baseline, not treated as a prime.'),
 dict(habit='Small raised strokes can belong to the row above',place='Cor 2 first L in Supposons',observation='The apparent prime lies after the upper family symbol and is its comma; the lower L stays unprimed.'),
 dict(habit='Slanted compressed prose',place='both left-margin notes',observation='Words have variable slope even after a -45° rotation; visual rows are separate from the main-column text visible behind them.'),
 dict(habit='Closely retraced relation strokes',place='At DC 1 and live At DD 1',observation='The central diamond may look heavier from retracing. Only additional source decorations are separate corrections.'),
 dict(habit='Crosses as drawing marks',place='simplicial example',observation='Three crosses are made of intersecting strokes; no alphabetic labels are legible. The outside right upright is retraced.'),
 dict(habit='Cancellation over interlinear material',place='upper draft',observation='Local replacement words and formulas remain inside the later global cancellation. A separate live NB margin should not be globally struck merely because long strokes cross nearby.'),
]

notes=[
 dict(id='009-N1',claim='The cancelled upper material and live reference line have independent source-state scopes.',source='scan009 upper_cancellation_scope, reference and cancelled_montrons crops',reasoning_if_any='The sloping strokes run through both upper corollaries and At DC 2; the horizontal Montrons strike is below the live reference row.'),
 dict(id='009-N2',claim='Clear source inconsistencies are retained.',source='scan009 cor1, cor2, atdd1_rest, cor_main2, plus_gen crops',reasoning_if_any='C/G substitutions and K/L mismatch are not repaired from the intended argument. No external or mathematical consistency premise decided a letter.'),
 dict(id='009-N3',claim='The main axiom has no additional cf GF VI phrase between implique and its conclusion.',source='scan009 atdd1_rest and margin_after_figure crops',reasoning_if_any='That reference follows the marginal note’s slanted baseline; moving it into the main statement duplicates/misplaces ink.'),
 dict(id='009-N4',claim='H editorial notes and prior drawing comments are excluded as text and as independent authority.',source='packets/scan009/H.tex and H_drawing.tex',reasoning_if_any='Only their actual readings were compared with the image; external manuscript references and earlier-machine assertions were not used to supply ink.'),
 dict(id='009-N5',claim='No mathematical identity was checked by calculation or external reference.',source='actual first-reader workflow',reasoning_if_any='The checks here are visual, source-state, and structural output checks. They are not mathematical validation events.'),
 dict(id='009-N6',claim='The small source-shaped lower rule and mid-stroke arrow are retained as graphics.',source='scan009 atdc2_end and atdc2_assumptions crops',reasoning_if_any='The first is an editing boundary, the second has a distinct right-pointing head; neither is replaced with added prose.'),
]

def extract_macro(s,name):
    out=[]
    for m in re.finditer(r'\\'+name+r'\{',s):
        i=m.end(); depth=1
        while depth:
            depth += (s[i]=='{')-(s[i]=='}'); i+=1
        out.append(s[m.end():i-1])
    return out

audit=[]
deleted_specs=[
 ('At DC 1 whole first statement','retain deleted','atdc1','The first statement is horizontally crossed and belongs to the large cancelled block.'),
 ('At DC 1 old relation','retain deleted and unsure','atdc1','Underlying near-uprights are not fully recoverable beneath the live compatibility sign.'),
 ('At DC 1 continuation whole','retain deleted','upper_cancellation_scope','Oblique strokes cross the continuation including its inserted replacement content.'),
 ('At DC 1 old opening','retain deleted and unsure','atdc1_follow','Local horizontal strike masks the word; Alors versus At is unresolved.'),
 ('At DC 1 old Y′ formula','retain deleted','atdc1_follow','A local long strike crosses precisely the old Y′≪Y⇒X′∥Y′ expression.'),
 ('NB overwritten ≪','retain deleted','margin_nb','Old chevrons lie beneath the corrected ≤ sign; the NB as a whole stays live.'),
 ('NB impossible','retain deleted and unsure','margin_nb','Horizontal strike through the long word; internal letters not all plain.'),
 ('NB absurde','retain deleted and unsure','margin_nb','Local alteration obscures several letters before car.'),
 ('Cor 1 whole','retain deleted','upper_cancellation_scope','Long oblique source strokes include the whole corollary.'),
 ('Cor 2 whole','retain deleted','upper_cancellation_scope','Long oblique source strokes include the whole corollary and replacement definition.'),
 ('Cor 2 old Sup expression','retain deleted; broaden doubt to whole formula','cor2','Dense scribbles cover all tokens, not only the first L.'),
 ('At DC 2 whole','retain deleted','upper_cancellation_scope','Diagonal cancellation crosses the complete draft through its unfinished Alors.'),
 ('At DC 2 Soit/Soient','retain local deleted and unsure','atdc2_header','Separate local crossing remains visible under the global cancellation.'),
 ('At DC 2 old L','retain deleted and unsure','atdc2_formula','Older letter under the heavy K is incompletely visible.'),
 ('Reference p.','retain deleted and unsure','reference','Small local strike after cf; the remainder of reference row is live.'),
 ('Montrons row','retain deleted with lexical doubts','cancelled_montrons','Independent horizontal strike through that row, ending with En effet.'),
 ('Counterexample ex','retain deleted and unsure','margin_after_figure','Altered small group before second At; not all letter strokes plain.'),
 ('Live axiom est','retain deleted and unsure; remove duplicated live est','atdd1_rest','One cancelled word only occurs before tjrs.'),
]
for span,(place,decision,cp,evidence) in zip(extract_macro(C,'deleted'),deleted_specs):
    audit.append(dict(C_span=r'\deleted{'+span+'}',decision=decision,place=place,evidence=evidence+' Crop: '+CROPS[cp]['file']))
insert_specs=[
 ('At DC 1 replacement opening','retain insertion','atdc1_follow','Soient is above the cancelled old opening and later cancelled with the whole draft.'),
 ('At DC 1 added avec/i.e. condition','retain insertion; plain L resolved','atdc1_follow','The entire condition occupies an interlinear row above the old Y′ formula; both parentheses remain.'),
 ('Cor 2 replacement L definition','retain insertion','cor2','L=F∩G is above the heavily cancelled old Sup definition, inside the globally cancelled corollary.'),
 ('Live At DD 1 slanted addition','read ou bien; retain insertion after Soient','atdd1_first','Two short slanted words rise from just after Soient; the complete phrase was included before resolution.'),
]
for span,(place,decision,cp,evidence) in zip(extract_macro(C,'inserted'),insert_specs):
    audit.append(dict(C_span=r'\inserted{'+span+'}',decision=decision,place=place,evidence=evidence+' Crop: '+CROPS[cp]['file']))
assert len(audit)==22

# Raw token-difference rows are an index to source places, not themselves semantic changes.
ROW_MAP={
401:('metadata only: source page 8 retained; scan9 wrapper is editorial',[]),
402:('actual readable-word difference',['01']),403:('alphabet uncertainty',['02']),
404:('equivalent compatibility rendering plus underlying deletion state',['03','80']),
405:('mixed relation syntax, terminal mark, insertion and source state',['03','04','05','06','08','09']),
406:('same-primary doubt resolution',['07']),407:('source punctuation',['08']),408:('punctuation and source-state/content difference',['05','06','08','09']),
409:('moved marginal note plus actual words/formulas/states',['10','11','12','13','14','15','16','17','18','19','20','21','22','23','29']),
410:('symbol reading and C doubt resolution',['24','81']),411:('alphabet uncertainty',['25']),412:('prime present only in H',['27']),413:('C/G difference',['28']),
414:('compatibility syntax alone for relation; cancelled formula separately covered',['30']),
415:('cancelled/replacement formulas, agreed wrong antecedent letters and source state',['30','31','32','33','34']),
416:('H editorial prose excluded; its described source states checked independently',['09','29','34','35','36','37']),
417:('actual different word and heading underline; uncertainty retained',['35','82']),418:('locally cancelled old opening',['36']),419:('overwritten earlier letter',['37']),
420:('Sup subscript syntax only',[]),421:('Sup subscript syntax only',[]),422:('abbreviation expanded in H',['38']),
423:('editorial note excluded; source graphic and state examined',['39','40']),424:('actual word difference',['41']),425:('actual heading difference',['42']),
426:('compatibility rendering only; recurring alphabet addressed once',['43']),427:('display line-break syntax, C physical two rows retained',[]),
428:('compatibility rendering only; two-row source display retained',[]),429:('compatibility syntax and following live reference scope',['44','45','46','47','48','49','50']),
430:('aligned environment syntax only',[]),431:('case, punctuation and locally cancelled p.',['44','45']),432:('nonbreaking-space syntax only',[]),
433:('retained digit doubt and source underline',['47']),434:('abbreviation, source-shaped arrow and separate cancellation',['48','49','50','51']),
435:('readable parenthetical clause left illegible in H',['52','53']),436:('editorial synopsis excluded; real marginal heading and rule placement',['54','55']),
437:('large mixed drawing/marginal-note stretch; editorial external references excluded',['54','55','56','57','58','59','60','61','62','63','64','86']),
438:('67 is source; H 73–74 belongs to editorial note, not variant source digits',['64']),439:('68 is source; H external-reference narrative is editorial',['64']),
440:('altered source label retains uncertainty; underline scope',['65','83']),441:('interlinear words and attachment',['66']),442:('insertion position and uncertain separator',['66','67']),
443:('equivalent compatibility rendering only',[]),444:('intersection versus wedge',['68']),445:('Sup subscript syntax only',[]),446:('Sup subscript syntax only',[]),
447:('compatibility syntax plus NB placement/content',['69','70','71','72']),448:('NB placement',['72']),449:('marginal reference misplaced into main text',['64']),
450:('relation macro and editorial label-history prose; source alteration retained unsure',['65']),451:('editorial prose versus TikZ tokens, no independent source words',[]),
452:('editorial prose versus TikZ tokens; source K/L mismatch retained',[]),453:('editorial synopsis excluded; rule and lower label checked',['55','73']),
454:('NB actual content and displaced first-corollary text',['69','70','71','72','74']),455:('label wording and source first-corollary line',['73','74']),
456:('lower label and formula assignment',['75','76','77','84']),457:('real omitted abbreviation',['78']),458:('relation macro only plus agreed wrong C′ premise',['79']),
459:('editorial notes/descriptive drawing prose excluded; actual source margin/drawing covered',['54','56','57','58','59','60','61','62','63','64','78']),
}
raw=list(csv.DictReader((ROOT/'packets/scan009/differences.tsv').open(),delimiter='\t'))
difference_review=[dict(source_row=int(r['source_row']),classification=ROW_MAP[int(r['source_row'])][0],change_ids=['009-'+q for q in ROW_MAP[int(r['source_row'])][1]]) for r in raw]

# Full LaTeX readings for neutral blind-box candidates.
second=[]
def box(name,kind,coords,reading):
    x0,y0,x1,y1=coords
    second.append(dict(box='scan009_'+name,kind=kind,x0=x0,y0=y0,x1=x1,y1=y1,reading=reading))
def cb(name,kind,crop,reading): box(name,kind,CROPS[crop]['box'],reading)
def paragraph_containing(needle): return next(p for p in T.split('\n\n') if needle in p)
box('page8','number',[602,33,678,112],r'\mspage{8}')
cb('opening_end','text','intro_end',"de diverses façons d'autres")
cb('atdc1_whole','deletion','atdc1',next(p for p in T.splitlines() if p.startswith(r'\deleted{\uline{At} DC 1')))
cb('atdc1_follow_whole','deletion','atdc1_follow',next(p for p in T.splitlines() if p.startswith(r'\deleted{\deleted{\unsure{Alors}}')))
box('atdc1_soient','insertion',[285,510,525,597],r'\inserted{Soient}')
box('atdc1_avec','insertion',[732,495,1683,596],r"\inserted{avec $X'\parallel X\cap Y=L$, (i.e. $X'\parallel Z$ pour $Z\leq X,Y$)}")
cb('nb_whole','margin note','margin_nb',paragraph_containing(r'\margin{\uline{NB}'))
cb('cor1_whole','deletion','cor1',paragraph_containing(r'\deleted{\uline{Cor} 1'))
cb('cor2_whole','deletion','cor2',paragraph_containing(r'\deleted{\uline{Cor. 2}'))
box('cor2_old_formula','deletion',[1034,784,1465,877],r'\deleted{$\unsure{L=\underset{Z\in\widetilde F\cap\widetilde G}{\mathrm{Sup}}\,Z}$}')
box('cor2_new_definition','insertion',[1125,761,1335,824],r'\inserted{$L=F\cap G$}')
box('atdc2_whole','deletion',[261,861,1671,1246],paragraph_containing(r'\deleted{\uline{At DC} 2'))
cb('atdc2_header','text','atdc2_header',r'\deleted{\uline{At DC} 2 (Axiome des ateliers \unsure{spacieux|spécieux}) \deleted{\unsure{Soit|Soient}}}')
cb('atdc2_definition','formula','atdc2_formula',r'X,Y\in M,\quad \deleted{\unsure{L}}K=X\cap Y=\underset{Z\in\widetilde X\cap\widetilde Y}{\mathrm{Sup}}\,Z')
cb('atdc2_assumptions','formula','atdc2_assumptions',r"\text{pour tt }X',Y',\ \text{avec }X'\ll X,"+UNDERARROW+r",Y'\parallel K")
cb('atdc2_lower_rule','drawing','atdc2_end',LOWER_RULE.strip())
cb('transition','text','onvoudra','On voudra la')
cb('property1','formula','propriete',paragraph_containing(r'\uline{Propriété 1}'))
cb('reference_whole','text','reference',next(p for p in T.splitlines() if p.startswith(r'cf \deleted{\unsure{p.}}')))
cb('montrons_row','deletion','cancelled_montrons',r"\deleted{\unsure{Montrons} qu'on a bien \unsure{en} $\Rightarrow$. En effet,}")
cb('ceci_and_at12','text','ceci_equivalent',paragraph_containing('Ceci est équivalent'))
cb('criterion','margin note','margin_criterion',paragraph_containing(r'\margin{\uline{Critère}'))
cb('simplicial_drawing','drawing','drawing',DRAW)
cb('counterexample_note','margin note','margin_after_figure',paragraph_containing(r'\margin{Mais on aura'))
axiom_line=next(p for p in T.splitlines() if p.startswith(r'\uline{At \unsure{DD|CD|DC}}'))
cb('atdd1_first','formula','atdd1_first',axiom_line.split('. Posons ',1)[0]+'.')
box('atdd1_addition','insertion',[610,1713,723,1822],r'\inserted{ou bien}')
cb('atdd1_rest','formula','atdd1_rest','Posons '+axiom_line.split('. Posons ',1)[1])
box('atdd1_rule','drawing',[282,1820,322,2026],r'\tikz[x=.5em,y=.5em]{\draw (0,0)--(0,4.25);}')
cb('cor_main1','text','cor_main1',paragraph_containing(r'\uline{Cor. Main} 1'))
box('cor_main2','formula',[342,2055,1652,2220],paragraph_containing(r'\uline{Cor. Main} 2'))
box('generalization','formula',[349,2145,1620,2344],paragraph_containing('Plus gén.'))
# Local number groups remain inside these complete inscribed boxes: At DC1, Cor1,
# Cor2, At DC2, Propriété1, VI/p73, At12, AtDD1, Cor.Main1/2, At parallel/At11/VI/67/68.

check_events=[
 dict(event='whole-layout',source='scan009 whole image',actual='Viewed the whole sheet once to locate all main, marginal, inserted, cancelled, displayed and graphical material.'),
 dict(event='upper-half-reading',source='scan009_a.jpg',actual='Read upper half once line by line against C/H, including all agreed tokens, accents, primes, source-state scopes and the manuscript number.'),
 dict(event='lower-half-reading',source='scan009_b.jpg',actual='Read lower half once line by line against C/H, including the final equivalence, both marginal continuations and all visible drawing strokes.'),
 dict(event='saved-crop-reading',source='scan009_crop_manifest.json',actual='Personally viewed every saved crop; mandatory different-word and resolved-C-doubt places have a saved original-coordinate crop. A few initially clipped unresolved places were reframed before deciding; manifest records these changes.'),
 dict(event='state-audit',source='22 C source-state spans',actual='Audited all 18 deleted and 4 inserted spans, retaining local deletion scopes inside later global cancellation.'),
 dict(event='whole-formula-reading',source='upper axioms, NB, both upper corollaries, property, live axiom and lower corollaries',actual='Checked adjacent letters, all indices, primes, arrow ends and relation decorations rather than only marked symbols.'),
 dict(event='drawing-count',source='saved drawing crop and explicit TikZ',actual='Counted four boundary sides with a bottom gap, one diagonal, two filled points, one gapped oval, three crosses; compared the source components with the drawn path list a second time.'),
 dict(event='raised-mark-baseline-check',source='cor2 crop',actual='Checked the apparent prime over the first L of Supposons against the upper row: it is the comma after the family symbol, not an L prime.'),
 dict(event='assumption-arrow-check',source='atdc2_assumptions crop',actual='Confirmed two arms on the curved underline-like stroke form a right-pointing mid-stroke arrowhead and reproduced it explicitly.'),
 dict(event='raw-difference-coverage',source='59 rows 401–459 of differences.tsv',actual='Mapped every supplied raw row, distinguishing real reading/source-state differences from relation, Sup and wrapper syntax or H editorial prose.'),
]

review=dict(scan='scan009',
 lines_read=dict(count=64,convention='Count independent physical writing baselines, including manuscript number, separate interlinear additions and struck rows; a mathematical subscript or superscript is not a separate line. Main-column and interlinear material: 36; upper slanted NB: 13; crowded criterion/introduction: 7; lower slanted continuation: 8. For the crowded criterion, short staggered baselines are counted separately even when their horizontal ranges overlap. Graphic paths are inventoried separately.'),
 changes=changes,doubts=doubts,inventory=inventory,notation=notation,hand_log=hand_log,notes=notes,
 check_events=check_events,deletion_insertion_audit=audit,difference_review=difference_review,second_boxes=second,
 crop_manifest='out/review/scan009_crop_manifest.json',generation_script='out/scripts/scan009_build_review.py')

allowed={'misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised',r'readable ink left as \ill{}','drawing or diagram','other'}
assert all(x['kind'] in allowed for x in changes)
assert all(x['kind'] in {'text','display','diagram','drawing','margin note','insertion','deletion'} for x in inventory)
assert {x['source_row'] for x in difference_review}==set(range(401,460))
assert all((ROOT/x['crop']).is_file() for x in changes)
assert len({x['id'] for x in changes})==len(changes)
assert all(0<=b['x0']<b['x1']<=1685 and 0<=b['y0']<b['y1']<=2361 for b in second)
assert T.count('{')==T.count('}')
assert T.count(r'\[')==T.count(r'\]')
assert T.count(r'\begin{')==T.count(r'\end{')
assert r'\newcommand' not in T
check_events.append(dict(event='output-structure-check',source='proposed TeX and JSON',actual='Checked brace/display/environment balance without TeX compilation; verified allowed kind values, all crop paths, unique change IDs, all 59 raw rows, all 22 source-state audits and in-bounds blind boxes.'))
(OUT/'scan009_review.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n')
(OUT/'scan009_second_boxes.json').write_text(json.dumps(second,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(changes=len(changes),against_C=sum(x['against_C'] for x in changes),against_H=sum(x['against_H'] for x in changes),doubts=len(doubts),blind_boxes=len(second),state_audits=len(audit),raw_rows=len(difference_review),crops=len(CROPS)),ensure_ascii=False))
