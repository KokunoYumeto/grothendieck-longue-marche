import json,re
from pathlib import Path
ROOT=Path("/workspace/scratch/8f839dff4bf0/SP74_C13_143+145_work")
pkt=json.loads(Path("/workspace/scratch/8f839dff4bf0/reader_packets/145_scan002.json").read_text())
Csrc,Hsrc=pkt["witness_C"],pkt["witness_H"]
candidate=(ROOT/"reviews/145_scan002_readerB.tex").read_text()
boxes={
"cancelled_header":[262,24,1555,150],"cancelled_diagram":[480,134,1165,407],
"triangle_cancel":[390,385,671,493],"h_definition":[742,526,1584,782],
"square":[880,797,1250,1013],"nb1":[256,1043,1655,1365],
"margin_u":[29,1144,357,1424],"nb2":[238,1362,1605,1775],
"margin_pi":[123,1625,341,1855],"margin_equations":[300,1848,903,2187],
"h_paragraph":[690,1691,1642,2079],"hn_definition":[716,2075,1657,2240],
"last_line":[362,2221,1658,2345]}
def crop(n):return "page" if n=="page" else f"crops/145_scan002_readerB_{n}.png"
changes=[]
def row(place,C,H,final,ac,ah,kind,ink,confidence="high",loc="page",marked=False,consequential=False):
    assert C=="[no witness]" or C in Csrc,("C",place,C)
    assert H=="[no witness]" or H in Hsrc,("H",place,H)
    assert not final or final in candidate,("final",place,final)
    assert ac or ah
    changes.append(dict(place=place,C=C,H=H,final=final,against_C=ac,against_H=ah,kind=kind,
        ink=ink,confidence=confidence,crop=crop(loc),box=None if loc=="page" else boxes[loc],
        marked_in_H=marked,consequential=consequential))

row("Cancelled opening: verb",r"\unsure{distinguer|déterminé}","déterminé",r"\unsure{distinguer|déterminé}",False,True,
 "misread word","The reduced d/i/t sequence and ending are crossed by the large cancellation strokes. Distinguer remains the preferred tentative reading, but déterminé is not excluded by the surviving ink.",
 "low","cancelled_header",True)
row("Cancelled opening: no extra word before first D",r"$\bar D_{J,\alpha}$",r"\ill{} $\overline{D}_{J,\alpha}$",
 r"$\bar D_{J,\alpha}$",False,True,"text not on the page",
 "There is blank space between the doubtful verb and the first barred D; no independent word corresponding to H's extra illegibility placeholder is visible.",
 "medium","cancelled_header",True)
row("Cancelled opening: reference",r"\unsure{cf. 9}",r"cf. \ill{}",r"cf. \unsure{9}",False,True,
 "readable ink left as \\ill{}","The joined c,f and stop are visible; a final loop and descending stroke favor 9, but brown damage and crossing strokes obscure its upper portion.",
 "low","cancelled_header",True)
row("Live triangle: cancelled continuation after tilde U(C)",r"\deleted{\unsure{\ne U}}","un signe biffé",
 r"\deleted{\unsure{\ne U|=U}}",False,True,"omission",
 "Two short parallel bars and a U-shaped letter survive under heavy crossing/looping cancellation. A small slash may belong to a written not-equal sign, but an equals sign crossed by deletion remains possible.",
 "low","triangle_cancel",True)
row("Definition of H: cancelled low character",r"H_{\deleted{\unsure{u}}}",r"H = \Bigl\{",r"H_{\deleted{\unsure{u}}}",
 False,True,"omission","A small dark overwritten character lies below/right of the H. Its u-like shape is retained as cancelled and doubtful; the live H itself is unindexed after cancellation.",
 "low","h_definition")
row("First underbrace: separator inside abbreviation",r"\text{ss-gr.}",r"\text{ss-gr.}",r"\text{\unsure{ss=gr.|ss-gr.}}",
 True,True,"misread symbol or index",
 "Between the two reduced s graphs and gr. are two short near-parallel pencil strokes. They may be an equals-shaped separator or a retraced hyphen; the local ambiguity is retained.",
 "low","h_definition")
row("Square: lower map's v label",r'\arrow[r,"v","\sim"'+"']",r'\arrow[r, "\sim"'+"']",r"\substack{v\\\sim}",
 False,True,"omission","A rounded v-shaped letter stands above the separate wave in the center of the square. It is a visible label, not part of the wave.",
 "high","square",True,True)
row("Square: wave above lower shaft",r'"\sim"'+"'",r'"\sim"'+"'",r"\substack{v\\\sim}",
 True,True,"insertion or placement","Both the v and the wave are above the lower horizontal arrow shaft, one above the other; the wave is not below the shaft.",
 "high","square",True)
row("Square: commutatif at the right", "commutatif","commutatif",r"\text{commutatif}",True,True,"insertion or placement",
 "The word commutatif is written to the right of the square at about the upper-row height, rather than on a following line below the square.")
row("First NB: underline",r"\uline{NB}",r"\textbf{NB}",r"\uline{NB}",False,True,"insertion or placement",
 "A distinct horizontal rule lies below NB; the label is not merely heavier lettering.",loc="nb1")
row("First NB: order of the four data",r"$\unsure{u},\pi',\pi'',v$",r"$v$, $\pi'$, $\pi''$, $u$",r"$u,\pi',\pi'',v$",
 False,True,"misread symbol or index",
 "The first reduced letter has the cupped u form with a returning right stroke; the last is the simple rounded v used in the square. The primes on the two pi terms are one and two respectively.",
 "medium","nb1",consequential=True)
row("First NB: punctuation after comme dessus","comme dessus un iso","comme dessus, un iso","comme dessus un iso",
 False,True,"text not on the page","No detached comma is visible after the reduced final s of dessus before un iso on the following source line.",
 "medium","nb1")
row("First NB: starred induced map",r"$u_*:\pi'\longrightarrow\pi''$",r"v_* : \pi' \longrightarrow \pi''",
 r"$u_*:\pi'\longrightarrow\pi''$",False,True,"misread symbol or index",
 "The map letter has two upright sides joined by a lower cup, followed by a separate low star and a two-dot colon. It is u_*, not the simpler v graph.",
 "high","nb1",consequential=True)
row("First NB: parenthetic insertion",r"\inserted{(induit par $u$)}",r"(induit par $u$ \uncertain{on aura d'ailleurs}",
 r"\inserted{(induit par $u$)}",False,True,"insertion or placement",
 "The small parenthetic induit par u sits above the subsequent line. Its right curved closing area extends into the guide that returns toward the space after the displayed induced map.",
 "high","nb1",True)
row("First NB: curved insertion guide",r"\inserted{(induit par $u$)}",r"(induit par $u$",
 r"\draw ([xshift=.08cm]ins.east) .. controls (6.9,.2) and (3.9,.5) .. (4,-.15);",
 True,True,"drawing or diagram",
 "A long thin curve runs beneath the inserted parenthesis and bends down/left at the gap before On aura d'ailleurs, after the induced-map expression. The candidate records the curve and its neighboring text attachment.",
 "high","nb1",True)
row("First NB: no comma after insertion",r"(induit par $u$)},",r"(induit par $u$",r"(induit par $u$)}",
 True,False,"text not on the page","No independent comma follows the inserted parenthesis; the long returning stroke is the insertion guide.",
 "medium","nb1")
row("First NB: new sentence starts On", "On aura d'ailleurs",r"on aura d'ailleurs","On aura d'ailleurs",
 False,True,"misread word","The main-line On begins with a tall looped capital O below the insertion guide. It is not a continuation inside the small parenthesis.",
 "high","nb1",True)
row("First NB: literal two-bar shorthand",r"de $=$ indice","de même indice",r"de $=$ indice",False,True,
 "abbreviation expanded or spelling modernised",
 "Two short horizontal bars occur between de and indice. The candidate retains that written equals sign instead of expanding it to même.",
 "high","nb1")
row("First marginal note: alleged deleted de",r"\deleted{\unsure{de}} par $v$",r"par} $v_*$",r"par $v_*$",
 True,False,"deletion state",
 "The dark graph after par consists of a v-shaped letter and a low star, matching the page's starred-map notation. No independent strike establishes C's proposed deleted de.",
 "high","margin_u",True)
row("First marginal note: star after v",r"par $v$",r"par} $v_*$",r"par $v_*$",
 True,False,"omission","A dark star sits below/right of the final v. It is part of the live formula v_*, not deleted text between déterminé and par.",
 "high","margin_u",True,True)
row("Second NB: underline",r"\uline{NB}",r"\textbf{NB}",r"\uline{NB}",False,True,"insertion or placement",
 "A separate underline is visible immediately below the second NB.",loc="nb2")
row("Second NB: parenthetical words",r"\uline{\unsure{ces conditions|cas connexe}}",r"cas \uncertain{connexe} \ill{}",
 r"\uline{ces conditions}",False,True,"misread word",
 "The parenthesis contains ces followed by the longer conditions sequence, with its d ascender and i marks. An underline extends beneath the end of ces and conditions; there is no connexe ending.",
 "high","nb2",True)
row("Second NB: known u clause",r"$u$ est connu",r"on ne \uncertain{connaît} \ill{}",r"$u$ est connu",False,True,
 "misread word",
 "After the comma following the preceding connu, the source has a short u graph, est and the reduced connu. It has no independent on ne connaît sequence.",
 "high","nb2",True,True)
row("Second NB: cancelled word before mod",r"\deleted{\unsure{aux}}",r"qu'à \ill{}",r"\deleted{\unsure{aux}}",
 False,True,"deletion state",
 "A short aux-like fragment is crossed by a zigzag after u est connu. Its letters remain uncertain, but its cancelled state and position are distinct from the following live mod.",
 "low","nb2",True)
row("Second NB: mod without a stop", "mod. multiplication",r"qu'à \ill{} multiplication","mod multiplication",
 True,True,"abbreviation expanded or spelling modernised",
 "The live word has the reduced m,o and a tall final d. No detached grey/black punctuation follows d; the nearby yellow spot is not transcribed as a period.",
 "medium","nb2",True)
row("Second NB: one reduced a/colon graph and underline scope",
 r"à \uline{gauche}",r": \uncertain{à gauche}",r"\uline{\unsure{à|:} gauche}",
 True,True,"insertion or placement",
 "There is one two-dot graph before gauche, not a colon plus a second written à. The underline begins beneath this graph and continues under gauche. A similarly reduced graph recurs in classes à droite, so à/colon is left explicit.",
 "medium","nb2",True)
row("Second NB: literal gamma membership expression",
 r"\gamma\in\pi''",r"\uncertain{élt} de $\pi''$",r"\gamma\unsure{\in|+}\pi''",
 False,True,"misread symbol or index",
 "A looped gamma is followed by an angular membership-like sign and pi with two high prime strokes. The short middle sign can also resemble a plus and stays doubtful; the words élt de are not written.",
 "medium","nb2",True,True)
row("Small marginal diagram: left diagonal inclusion mark",r"\arrow[ur,hook]",r"\cup",
 r'\arrow[ur,phantom,"\tikz[baseline=-.5ex]{\node[rotate=-35,inner sep=0pt] {$\cup$};}" description]',
 True,False,"drawing or diagram",
 "The left connector is a short open cup-like curve tilted upward/right. There is no separate long shaft or arrowhead of a hooked arrow.",
 "high","margin_pi",consequential=True)
row("Small marginal diagram: right diagonal inclusion mark",r"\arrow[ul,hook']",r"\cup",
 r'\arrow[ul,phantom,"\tikz[baseline=-.5ex]{\node[rotate=15,inner sep=0pt] {$\cup$};}" description]',
 True,False,"drawing or diagram",
 "The right connector is another open cup-like curve between the lower pi double-prime and upper pi. It likewise has no shaft or pointed head.",
 "high","margin_pi",consequential=True)
row("Small marginal diagram: full central relation",r'"\sim",draw=none',r"\pi' \simeq \pi''",
 r'\arrow[rr,phantom,"\simeq" description]',True,False,"misread symbol or index",
 "Between pi prime and pi double-prime are an upper wave and a separate lower stroke. C retains only the upper wave.",
 "high","margin_pi",consequential=True)
row("Small marginal lower relation: absent terminal stop",r"\pi_i'\simeq\pi_i''.",r"\pi'_i \simeq \pi''_i",
 r"\pi_i'\simeq\pi_i''",True,False,"text not on the page",
 "The high prime strokes and low dotted i are distinct. No separate stop occurs after the right i; its own dot is not terminal punctuation.",
 "high","margin_pi")
row("Equational marginal note: placement",r"\margin{\["+"\n"+r"p''u=vp'",r"p'' u = v p',",r"\margin{\["+"\n"+r"p''u=vp'",
 False,True,"insertion or placement",
 "The calculation occupies a separate left-margin block beside the H paragraph. It is not inserted into the paragraph's main reading order.",
 "high","margin_equations")
row("Equational marginal note: final unmatched parenthesis",
 r"p''(\gamma u)=(p''\gamma)u=p''u=vp'",r"p''(\gamma u) = (p''\gamma) u = p'' u = v p'",
 r"p''(\gamma u)=(p''\gamma)u=p''u=vp')",
 True,True,"omission",
 "A large closing curved stroke follows the last p prime at the right of the calculation. There is no matching opening parenthesis before the line's initial p double-prime; the written final stroke is retained.",
 "high","margin_equations")
row("H paragraph: sous-ens de l'ens/l'un",
 r"sous-\unsure{ens de l'ens}",r"sous-\ill{} \uncertain{de} l'un",
 r"sous-ens de \unsure{l'ens|l'un}",False,True,"readable ink left as \\ill{}",
 "The short ens after the line-ending sous- and the following de are readable. The following l-apostrophe word repeats a very reduced ens/un-shaped sequence; l'ens is favored but not settled.",
 "medium","h_paragraph",True)
row("H paragraph: quoted germes",r"\unsure{germes|groupoïdes}","groupoïdes","germes",False,True,
 "misread word",
 "The word has one large initial g descender and a short reduced ermes continuation across the stain. No additional p descender, d ascender or diaeresis supports groupoïdes.",
 "high","h_paragraph",True,True)
row("H paragraph: quotation marks",chr(96)*2+r"\unsure{germes|groupoïdes}''","« groupoïdes »",chr(96)*2+"germes''",
 False,True,"misread symbol or index",
 "Pairs of short high strokes stand on each side of the word. They are quote ticks, not drawn guillemets.",
 "high","h_paragraph")
row("H paragraph: underlined abbreviation without a stop",r"\uline{d'isom}","d'isom.",r"\uline{d'isom}",
 False,True,"abbreviation expanded or spelling modernised",
 "The d'isom abbreviation has a separate underline. There is no detached period after the reduced final m before the crossed word.",
 "high","h_paragraph")
row("H paragraph: crossed word after d'isom",r"\deleted{\unsure{des}}",r"\struck{\ill{}}",r"\deleted{\unsure{des}}",
 False,True,"readable ink left as \\ill{}",
 "A short d/e/s-like fragment survives beneath a horizontal/oblique crossing immediately after d'isom. Its reading remains tentative, with the deletion explicit.",
 "low","h_paragraph",True)
row("H paragraph: literal H-groupes",r"\unsure{$H$-groupes|$H$-groupoïdes}",r"\uncertain{H-groupoïde}",r"$H$-groupes",
 False,True,"misread word",
 "The prefix has two short stems joined by a crossbar, followed by a separate hyphen. It is an H-shaped graph, not the page's ss abbreviation. The following shorter groupes sequence lacks an oïde ending.",
 "medium","h_paragraph",True,True)
row("H paragraph: finite-index ending", "d'indice finis",r"d'indice \ill{}",r"d'indice \unsure{finis|fini}",
 False,True,"readable ink left as \\ill{}",
 "The tall f and reduced ini sequence are readable. A final joined return may be s; the source's plural-looking ending is not silently corrected to the grammatical singular.",
 "low","h_paragraph",True)
row("H paragraph: equals shorthand before final indice",r"de $=$ indice",r"\ill{} indice",r"de $=$ indice",
 False,True,"misread symbol or index",
 "Two horizontal bars cross the stained area before the final indice; they repeat the literal two-bar shorthand in the first NB.",
 "high","h_paragraph",True)
row("H paragraph: absent final period",r"de $=$ indice.",r"\ill{} indice",r"de $=$ indice",
 True,False,"text not on the page",
 "The final e/return stroke of indice ends the line without a separately written stop before the next paragraph.",
 "medium","h_paragraph",True)
row("H_n definition: sous-ens without abbreviation stop","sous-ens de","sous-ens. de","sous-ens de",
 False,True,"abbreviation expanded or spelling modernised",
 "After the last reduced s of ens there is a blank interval before de, with no detached dot. The source's written hyphen is retained.",
 "high","hn_definition")
row("Final line: ss-groupe underline",r"\uline{ss-groupe}","ss-groupe",r"\uline{ss-groupe}",
 False,True,"insertion or placement",
 "A long separate rule runs from beneath the ss abbreviation to the end of groupe; the following comma is outside the underline.",
 "high","last_line")
row("Pencil footer pagination",r"\mspage{1}","[no witness]",r"\mspage{1}",False,True,"omission",
 "A separate light pencil 1 sits at the lower-left page edge. Its hand is not attributed to the main writer.")

decisions=[
dict(id="M0753",decision="first",reading="u",ink="The first datum has a cupped u with returning right stroke; the final datum is the simpler v also used in the square.",crop=crop("nb1"),box=boxes["nb1"],confidence="medium"),
dict(id="M0754",decision="first",reading="déterminé",ink="The long word has the initial d loop, tall t and reduced erminé continuation; the rotated crop makes the word outline legible.",crop=crop("margin_u"),box=boxes["margin_u"],confidence="medium"),
dict(id="M0755",decision="first",reading="ces conditions",ink="The second word is the longer conditions sequence, with its d ascender and i marks, underlined inside the parentheses.",crop=crop("nb2"),box=boxes["nb2"],confidence="high"),
dict(id="M0756",decision="undecided",reading=r"ens de \unsure{l'ens|l'un}",ink="The first ens and de are readable; the final l-apostrophe word has a very reduced repeated ens/un graph and remains unresolved.",crop=crop("h_paragraph"),box=boxes["h_paragraph"],confidence="medium"),
dict(id="M0757",decision="first",reading="germes",ink="One initial g descender and short ermes continuation; no extra p/d or diaeresis supports groupoïdes.",crop=crop("h_paragraph"),box=boxes["h_paragraph"],confidence="high"),
dict(id="M0758",decision="first",reading=r"$H$-groupes",ink="The prefix has two H stems and a crossbar, then a separate hyphen; the following word has the shorter groupes ending. No semantic normalization to ss-groupes is made.",crop=crop("h_paragraph"),box=boxes["h_paragraph"],confidence="medium"),
]

inventory=[]
def inv(kind,position,first,hand="his hand"):
 inventory.append(dict(sheet_kind="text",hand=hand,element=f"E{len(inventory)+1:02d}",kind=kind,position=position,first_words_or_objects=first,transcribed="yes"))
inv("deletion","top line","bien ... barred D_J,alpha de barred D_J, cf. 9; crossed by large diagonal strokes")
inv("diagram","upper block, wholly cancelled","six U objects; barred upper row; J',alpha' and J,alpha indices; seven directed links")
inv("deletion","across upper diagram","large diagonal cancellation strokes across the six-object diagram")
inv("diagram","upper-left live block below cancellation","D=U(C)^sim to tilde U(C), both down to U(C), labels pi and hat pi")
inv("deletion","after upper-right object of live triangle","cancelled not-equal/equals plus U fragment")
inv("display","upper-right beside live triangle","pi subset G")
inv("display","right-middle definition block","H={u in G | exists pi' subset pi, pi'' subset pi, iso v... avec; no closing brace")
inv("deletion","low/right of defining H","small overwritten u-like subscript")
inv("drawing","beneath the two subgroup inclusions","two underbraces labelled ss=gr./ss-gr., d'indice fini; id.")
inv("diagram","beneath H definition","four-object square D,D,D/pi',D/pi'', with u,p',p'',v and wave")
inv("text","right of square at upper-row height","commutatif")
inv("text","first NB across page below square","On aura, pour u,pi',pi'',v comme dessus un iso")
inv("display","second line of first NB","u_*:pi' to pi''")
inv("insertion","above continuation On aura d'ailleurs","(induit par u)")
inv("drawing","beneath insertion, returning to gap after the map","long thin curved insertion guide")
inv("text","continuation of first NB","On aura d'ailleurs pi' et pi'' de = indice dans pi.")
inv("margin note","slanting left margin beside first NB","u est déterminé par v_*")
inv("text","second underlined NB","v est connu ... (ces conditions) ... u est connu ... mod multiplication à/colon gauche")
inv("deletion","second NB before mod","short crossed aux-like fragment")
inv("diagram","left margin below second NB","pi over pi' and pi''; two open cup-like inclusion marks; central simeq")
inv("display","under small pi diagram","pi_i' simeq pi_i'' with no separate period")
inv("margin note","left margin beside H paragraph","three calculation lines and a final cancelled inclusion")
inv("display","first line of calculation note","p''u=vp'")
inv("deletion","second line of calculation note","p''u gamma =, crossed horizontally")
inv("display","third line of calculation note","p''(gamma u)=(p''gamma)u=p''u=vp'), ending with unmatched closing parenthesis")
inv("deletion","last line of calculation note","pi subset H crossed by a long rule")
inv("text","main lower-right paragraph","H est un groupe superset pi, et H/pi ... sous-ens ... germes d'isom H-groupes")
inv("deletion","within lower-right paragraph after d'isom","short crossed des-like fragment")
inv("text","penultimate paragraph","H_n = sous-ens de H formé des u ... d'indice n.")
inv("text","bottom main line","H_n est un underlined ss-groupe, et pi d'indice; unfinished")
inv("text","bottom-left pencil footer","1",hand="unknown (pencil pagination)")

remaining_doubts=[
dict(place="Cancelled opening verb",reading=r"\unsure{distinguer|déterminé}",alternatives="distinguer / déterminé",confidence="low",reason="Large diagonal cancellations cross the reduced middle and ending; crop cancelled_header."),
dict(place="Cancelled opening reference digit",reading=r"\unsure{9}",alternatives="9 / obscured digit",confidence="low",reason="A loop and descender favor 9, but the upper portion is covered by brown damage and a crossing stroke; crop cancelled_header."),
dict(place="Cancelled continuation after tilde U(C)",reading=r"\deleted{\unsure{\ne U|=U}}",alternatives="not-equal U / equals U with cancellation slash",confidence="low",reason="The not-equal slash cannot be completely separated from the crossing cancellation; crop triangle_cancel."),
dict(place="Deleted low character on H",reading=r"H_{\deleted{\unsure{u}}}",alternatives="u / overwritten small graph",confidence="low",reason="The small character is dark and heavily overwritten; crop h_definition."),
dict(place="Subgroup abbreviation under first underbrace",reading=r"\unsure{ss=gr.|ss-gr.}",alternatives="two-bar separator / retraced hyphen",confidence="low",reason="Two short near-parallel strokes are visible between ss and gr.; crop h_definition."),
dict(place="Cancelled word before mod",reading=r"\deleted{\unsure{aux}}",alternatives="aux / partially recoverable crossed word",confidence="low",reason="A zigzag passes through the short fragment; crop nb2."),
dict(place="Reduced graph before gauche",reading=r"\unsure{à|:}",alternatives="à / colon",confidence="medium",reason="Two separated dot-like strokes; its recurrence before droite supports a very reduced à, but the physical colon-like shape remains open. Crop nb2."),
dict(place="Sign between gamma and pi double-prime",reading=r"\gamma\unsure{\in|+}\pi''",alternatives="membership / plus-shaped sign",confidence="medium",reason="The small angular sign has a short upright and cross-stroke; no fully rounded epsilon outline is secure. Crop nb2."),
dict(place="Reduced graph in classes à droite",reading=r"classes \unsure{à|:} droite",alternatives="à / colon",confidence="medium",reason="Two dot-like strokes repeat the graph before gauche, independently confirmed on this cote's own page. Crop h_paragraph."),
dict(place="M0756 final l-apostrophe word",reading=r"ens de \unsure{l'ens|l'un}",alternatives="ens de l'ens / ens de l'un",confidence="medium",reason="The reduced last word can be read either way; its resemblance to the preceding ens favors the first. Crop h_paragraph."),
dict(place="Crossed word after d'isom",reading=r"\deleted{\unsure{des}}",alternatives="des / partially recoverable crossed word",confidence="low",reason="Small d/e/s-like strokes remain below the crossing; crop h_paragraph."),
dict(place="Finite-index ending",reading=r"\unsure{finis|fini}",alternatives="finis / fini",confidence="low",reason="The final joined return may be an s. The candidate does not normalize the grammatical number; crop h_paragraph."),
]
certainty_resolutions=[
dict(place="Cancelled header cf.",C=r"\unsure{cf. 9}",final=r"cf. \unsure{9}",ink="c,f and the stop are readable; the uncertainty is confined to the damaged digit."),
dict(place="M0753 first datum",C=r"\unsure{u}",final="u",ink="Cupped u with returning right stroke; distinct from final rounded v."),
dict(place="M0754 déterminé",C=r"\unsure{déterminé}",final="déterminé",ink="The rotated note exposes the d loop, tall t and reduced continuation."),
dict(place="M0755 ces conditions",C=r"\unsure{ces conditions|cas connexe}",final="ces conditions",ink="The longer conditions graph, with d/i features, is visible inside the underline."),
dict(place="M0756 partial resolution",C=r"\unsure{ens de l'ens}",final=r"ens de \unsure{l'ens|l'un}",ink="ens de is readable; only the final word remains doubtful."),
dict(place="M0757 germes",C=r"\unsure{germes|groupoïdes}",final="germes",ink="Short word with a single g descender and no oïde features."),
dict(place="M0758 H-groupes",C=r"\unsure{$H$-groupes|$H$-groupoïdes}",final=r"$H$-groupes",ink="Literal H prefix and shorter groupes ending."),
]
notation=[
dict(form=r"D=U(\mathbb C)^{\sim}",meaning="The page's initial covering-space notation",evidence="Upper-left live triangle; the first tilde is physically an upper-right exponent, while the right object's tilde is centered above U."),
dict(form=r"u,v,u_*,v_*",meaning="Distinct map letters and starred induced-map notation",evidence="The square, first NB and left marginal note were checked independently; u and v are not harmonized by expected mathematical roles."),
dict(form=r"$=$",meaning="Literal two-bar shorthand in de = indice",evidence="First NB and H paragraph each have two horizontal bars; no expansion to même in the transcription."),
dict(form="open cup-like inclusion marks",meaning="The source's short curves linking pi' and pi'' toward pi",evidence="Small left-margin diagram: no long shafts or pointed heads. Their orientation is reproduced graphically; cup is not asserted as a union operation."),
dict(form=r"\pi_i',\pi_i''",meaning="Low i indices with high prime strokes",evidence="Both lower formula objects have a dotted low i; the prime strokes are high on pi. C and H's alternate TeX ordering of prime and subscript is not a material difference."),
dict(form=r"$H$-groupes",meaning="Literal prefix and word used in the quotient/germs paragraph",evidence="Two H stems and a crossbar followed by a hyphen. It is deliberately not regularized to ss-groupes from mathematical expectation."),
dict(form=r"\mathbb C",meaning="Rendering of the complex-number graph",evidence="All three objects of the live triangle use the same C-like graph; ordinary/blackboard typography alone is not a material correction."),
]
abbreviations=[
dict(form="cf.",expansion="confer / compare"),
dict(form="ss=gr. / ss-gr.",expansion="sous-groupe, with separator uncertain"),
dict(form="id.",expansion="idem"),
dict(form="iso",expansion="isomorphisme"),
dict(form="NB",expansion="nota bene"),
dict(form="mod",expansion="modulo"),
dict(form="ens",expansion="ensemble"),
dict(form="d'isom",expansion="d'isomorphismes"),
dict(form="ss-groupe",expansion="sous-groupe"),
]
hand_log=[
dict(habit="Cupped u versus rounded v, with small low stars",places="145_scan002 square labels, first NB and slanting marginal note",scope="All these occurrences inspected on this page; no inference from cote143's vocabulary",misreadings="H swaps the first/last NB data and reads v_* for the main u_*; C reads the live marginal v_* as a cancelled de plus unstarred v."),
dict(habit="Short arrowheads may be small bent/filled terminals",places="145_scan002 cancelled six-object diagram, live triangle and square",scope="Every arrow endpoint inspected; the separate marginal cup marks are visibly different",misreadings="C supplies hooked arrows for the short open marginal curves."),
dict(habit="Two-dot reduced à-like graph",places="145_scan002 before gauche and before droite",scope="Both occurrences verified independently on this cote's sheet; retained as à/colon uncertainty",misreadings="H duplicates the first graph as a colon plus a written à."),
dict(habit="Reduced ens/un and finite-word endings",places="145_scan002 H/pi paragraph",scope="Ambiguity remains local to l'ens/l'un and finis/fini",misreadings="C and H choose different l-apostrophe words; no grammatical normalization is applied."),
dict(habit="Dark retracing is not automatically cancellation",places="145_scan002 marginal v_* versus genuine crossed Hu, aux, des and formulas",scope="Strike strokes were distinguished individually from the letter/star structure",misreadings="C labels the marginal v_* graph as deleted de."),
dict(habit="Brown vertical damage and yellow spots are not writing",places="145_scan002 near right-hand prose and diagrams",scope="The stain is kept out of the transcription; obscured letters remain doubtful where needed",misreadings="No punctuation is supplied from the yellow spot after mod."),
dict(habit="Pencil pagination attribution unknown",places="145_scan002 lower-left 1",scope="Only this source footer observed",misreadings="H omits the source number."),
]
notes=[
dict(id="145_scan002-N1",text="This is a new cote's own sheet, not presumed to continue cote143. A crossed opening sentence distinguishes or determines two barred D notations, followed by a wholly cancelled six-object U diagram. The small reference after cf. remains damaged. The page's brown vertical stain is physical damage, not a deletion stroke or marginal notation."),
dict(id="145_scan002-N2",text="A live triangle relates D=U(C)^sim, tilde U(C) and U(C), with pi and hat pi on its descending maps. The right object has a cancelled continuation. Separately, pi is written as a subgroup of G and H is defined by the existence of two finite-index subgroups and an isomorphism v compatible with a square. No closing set brace is written."),
dict(id="145_scan002-N3",text="The square labels its upper map u, vertical maps p' and p'', and lower map v with a wave; v and the wave are both above the lower shaft. The word commutatif is beside the square. The first NB gives data in the order u,pi',pi'',v and writes u_*:pi' to pi'', with an interlinear parenthesis induit par u and a long curved guide. It then says the two subgroups have de = indice, retaining the source shorthand."),
dict(id="145_scan002-N4",text="The slanting marginal note reads u est déterminé par v_*. The dark final v/star does not show an independent cancellation. The second NB contains underlined ces conditions and says that once v is known, u is known mod multiplication on the indicated side by an element written gamma followed by a membership-like sign and pi double-prime. Cancelled aux and the reduced à/colon graph remain uncertain."),
dict(id="145_scan002-N5",text="The small left-margin diagram uses open cup-like inclusion curves, not arrows with shafts, and a full wave-plus-bar relation between pi' and pi''. Its lower line has low i indices and high primes. A separate calculation shows p''u=vp', a crossed attempted continuation, and the expanded composition calculation ending in an unmatched closing curved parenthesis. A final pi subset H is crossed."),
dict(id="145_scan002-N6",text="The lower paragraph states that H is a group containing pi and describes H/pi, with classes on the written right-hand side, through a subset of an ensemble of germes d'isom. The source literally has H-groupes; the prefix is not regularized from mathematical expectation. The last l-apostrophe word and finis/fini remain doubtful, as does the crossed short word after d'isom. The two-bar = shorthand recurs before indice."),
dict(id="145_scan002-N7",text="H_n is defined using pairs of subgroups of index n. The final line calls H_n an underlined ss-groupe and stops after et pi d'indice; no completion is supplied. Pencil footer 1 is included with unknown hand attribution."),
]
check_events=[
dict(statement_id="145_scan002-N2",type="carried as background without fault found",outcome="Visually checked objects, bars, primes, arrowheads and the written definition. No covering-space theorem, subgroup existence claim or exactness statement was independently proved."),
dict(statement_id="145_scan002-N3",type="carried as background without fault found",outcome="Collated the u/v and starred labels from their strokes and positions. Did not use an expected induced-map identity to replace a source letter."),
dict(statement_id="145_scan002-N4",type="carried as background without fault found",outcome="Transcribed the source's determination claims and side-of-multiplication phrase. No uniqueness/lifting theorem was independently verified."),
dict(statement_id="145_scan002-N5",type="carried as background without fault found",outcome="Read all factors, prime counts, cancellations and parentheses in the marginal calculation. No independent algebraic proof was used to reconstruct obscured signs."),
dict(statement_id="145_scan002-N6",type="carried as background without fault found",outcome="Recorded the source's group/quotient/germs description, preserving literal H-groupes and local doubts. No commensurator or quotient identification was proved."),
dict(statement_id="145_scan002-N7",type="carried as background without fault found",outcome="Checked the index n definition and unfinished final subgroup assertion as written; no proof or attempted completion was made."),
]
report=dict(key="145_scan002",reader="B",stage="first",image_views=["original","half1","half2"],
 changes=changes,decisions=decisions,inventory=inventory,remaining_doubts=remaining_doubts,
 certainty_resolutions=certainty_resolutions,notation=notation,abbreviations=abbreviations,
 hand_log=hand_log,notes=notes,check_events=check_events,
 unresolved_for_main=[dict(place=d["place"],reading=d["reading"],reason=d["reason"]) for d in remaining_doubts],
 raw_difference_disposition="All packet differences and every C/H agreement were checked against the original once and both native halves once, then one color-preserving crop per unresolved block/locus. All thirteen unique crops were successfully viewed once. This first pass read only the assigned page plus the contract, guidelines and current notation; no OCR, web research, TeX compilation or second reading was performed. Markup-only differences, alternate prime/subscript TeX ordering, ordinary/blackboard C font convention, and H's editorial notes are excluded as source changes. Certainty-only decisions are separate. Every original MARKS id is present in order; new doubts have no invented ids.")

assert [d["id"] for d in decisions]==[m["id"] for m in pkt["marks"]]
for d in decisions:assert d["reading"] in candidate,("decision",d)
for d in remaining_doubts:assert d["reading"] in candidate,("doubt",d)
for d in certainty_resolutions:
 assert d["C"] in Csrc
 assert d["final"] in candidate
for c in changes:
 if c["crop"]!="page":assert (ROOT/c["crop"]).is_file()
allowed={"misread word","misread symbol or index","omission","text not on the page","deletion state","insertion or placement","abbreviation expanded or spelling modernised","readable ink left as \\ill{}","drawing or diagram","other"}
assert all(c["kind"] in allowed for c in changes)
depth=0
for m in re.finditer(r"(?<!\\)[{}]",candidate):
 depth += 1 if m.group()=="{" else -1
 assert depth>=0
assert depth==0
env=[]
for m in re.finditer(r"\\(begin|end)\{([^{}]+)\}",candidate):
 if m.group(1)=="begin":env.append(m.group(2))
 else:assert env.pop()==m.group(2)
assert not env
out=ROOT/"reviews/145_scan002_readerB.json"
out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
print(json.dumps(dict(tex=str(ROOT/"reviews/145_scan002_readerB.tex"),json=str(out),changes=len(changes),marks=len(decisions),inventory=len(inventory),doubts=len(remaining_doubts),crops=len(boxes),validation="literal excerpts, original marks, retained doubts, brace groups and environments passed; no compilation"),ensure_ascii=False))
