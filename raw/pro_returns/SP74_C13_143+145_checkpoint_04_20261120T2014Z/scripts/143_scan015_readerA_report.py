from pathlib import Path
import json
ROOT=Path("/workspace/scratch/8f839dff4bf0/SP74_C13_143+145_work")
KEY="143_scan015"
OUT=ROOT/"reviews"
OUT.mkdir(exist_ok=True)
P=json.loads(Path("/workspace/scratch/8f839dff4bf0/reader_packets/143_scan015.json").read_text())
TEX=r"""\scanpage{15}
\textcircled{7} Réconstruction des I-groupoïde fondamentaux $\Pi_1(\mathfrak X';J)$ de $\mathfrak X'$, et des opérations de $\mathcal G'$ dessus, en termes de l'extension $\unsure{\mathcal E|\Sigma}'$ de $\mathcal G'$ par $\pi_1$, et de l'opération de $\unsure{\mathcal E|\Sigma}'$ sur $\widetilde{\mathfrak X}'(J)$ et $\widetilde{\mathfrak X}'(J)\longrightarrow J$ [et des applications (7) (8)
\diagram{\begin{tikzcd}[ampersand replacement=\&]
\Psi^{\mathrm{ex}}:\widetilde{\mathfrak X}'(J) \arrow[r] \& \operatorname{Splitt}(\unsure{\mathcal E|\Sigma}'/\mathcal G')/\pi_1
\end{tikzcd}}
\diagram{\begin{tikzcd}[ampersand replacement=\&]
\Psi_{\unsure{j}}:\bigl(\widetilde{\mathfrak X}'(j) \arrow[r,dash] \& \operatorname{Splitt}(\unsure{\mathcal E|\Sigma}'_j/\mathcal G'_j)\bigr)].
\end{tikzcd}}
\margin{\begin{tikzpicture}[x=1cm,y=1cm]
\node[anchor=north west,align=left,font=\footnotesize] at (0,0) {inutile\\de se les donner,\\elles résultent des\\autres};
\draw (1.25,0.15) -- (1.05,-1.55);
\end{tikzpicture}}
\[
\operatorname{Ob}\Pi_1=J
\]
\deleted{\unsure{Soit} $j,j'\in J$}

\uline{NB} si $\widetilde\xi\in\widetilde{\mathfrak X}'(J)$, $\widetilde{\mathfrak X}'[j]$ (rev universel de $\mathfrak X'$ en $j$) s'identifie à $\widetilde{\mathfrak X}'$ (puisque $\widetilde\xi$ est un p\textsuperscript{t} marqué de $\widetilde{\mathfrak X}'$ au dessus de $j$
\diagram{\begin{tikzcd}[ampersand replacement=\&]
\widetilde{\mathfrak X}' \arrow[r,"\unsure{\varphi|\psi}_{\widetilde\xi}"] \& \widetilde{\mathfrak X}'[j]
\end{tikzcd}}
Si $\gamma\in\pi_1$, on aura
\[
\Psi_{\gamma\cdot\widetilde\xi}=\Psi_{\widetilde\xi}\circ\gamma_{\widetilde{\mathfrak X}'}^{\deleted{\unsure{-1}}}
\]
donc on peut dire, indépendamment du choix du p\textsuperscript{t} base $\widetilde\xi$
\diagram{\begin{tikzcd}[ampersand replacement=\&]
\widetilde{\mathfrak X}'[j] \& \underset{\text{torseur à dr sous }\pi_1}{\underbrace{\widetilde{\mathfrak X}'(j)}}\mathbin{\wedge}_{\pi_1}\widetilde{\mathfrak X}' \arrow[l,"\sim"']
\end{tikzcd}}
\mspage{14}
"""
(OUT/(KEY+"_readerA.tex")).write_text(TEX)
CR={
"title":("crops/143_scan015_A_title.png",[620,70,1600,195]),
"first":("crops/143_scan015_A_first-map.png",[570,775,1590,908]),
"second":("crops/143_scan015_A_second-map.png",[570,905,1655,1058]),
"margin":("crops/143_scan015_A_margin.png",[85,775,435,1150]),
"deletion":("crops/143_scan015_A_deletion.png",[292,1218,598,1324]),
"nb":("crops/143_scan015_A_nb-paragraph.png",[290,1270,1575,1595]),
"point":("crops/143_scan015_A_point-map.png",[565,1540,1095,1730]),
"eq":("crops/143_scan015_A_equivariance.png",[615,1830,1000,1955])
}
changes=[]
def add(place,C,H,final,against_C,against_H,kind,ink,confidence="high",where=None,marked=False,consequential=False):
    crop,box=CR[where] if where else ("page",None)
    changes.append(dict(place=place,C=C,H=H,final=final,against_C=against_C,against_H=against_H,kind=kind,ink=ink,confidence=confidence,crop=crop,box=box,marked_in_H=marked,consequential=consequential))
def alphabet(place,C,H,final,ink,where=None):
    add(place,C,H,final,True,False,"misread symbol or index",ink,"medium",where,False,False)
def action(place,C,H,final,ink,where=None):
    add(place,C,H,final,False,True,"misread symbol or index",ink,"low",where,False,False)
add("section number",r"\textcircled{7}","(7)",r"\textcircled{7}",False,True,"other","A continuous oval encloses the 7, not two separate parentheses.")
add("heading I-groupoïde",r"\unsure{I|1}-groupoïde",r"\uncertain{groupoïdes}","I-groupoïde",False,True,"omission","The initial upright has upper and lower horizontal bars, followed by a separate hyphen. The noun ends in a low e-like exit without a separate final s.","medium","title",True,True)
alphabet("heading Pi_1 expression",r"\Pi_1(X';J)",r"\Pi_1(\mathfrak{X}'; J)",r"\Pi_1(\mathfrak X';J)","The X has curled arms and a transverse crossing, with a separate prime; the delimiter before J is a semicolon.")
alphabet("heading de X-prime",r"$X'$",r"$\mathfrak{X}'$",r"$\mathfrak X'$","The X repeats the looped crossed construction with its own prime.")
for place in ["extension group in prose","acting group in prose"]:
    action(place,r"\mathcal E'",r"\Sigma'",r"\unsure{\mathcal E|\Sigma}'","The rounded upper return and lower turn admit E/Sigma. The prime is separate. Shared uncertainty is retained; the first Splitt occurrence gives a stronger E-shaped comparison.")
alphabet("sur lifted X-prime(J)",r"\widetilde X'(J)",r"\widetilde{\mathfrak{X}}'(J)",r"\widetilde{\mathfrak X}'(J)","The looped X has a separate wavy tilde and prime, with capital J in parentheses.")
alphabet("opening projection",r"\widetilde X'(J)\longrightarrow J",r"\widetilde{\mathfrak{X}}'(J) \to J",r"\widetilde{\mathfrak X}'(J)\longrightarrow J","The same accented X graph occurs; the short connector has a visible rightward head.")
add("first splitting-map exponent",r"\unsure{\mathrm{ex}|\mathrm{ext}}",r"\mathrm{ext}",r"\mathrm{ex}",False,True,"misread symbol or index","The raised letters have an e-like loop and angled x strokes. No additional t upright or crossbar follows.","high","first")
alphabet("first splitting-map domain",r"\widetilde X'(J)",r"\widetilde{\mathfrak{X}}'(J)",r"\widetilde{\mathfrak X}'(J)","The X has two curled arms, crossbar, tilde and prime.","first")
action("first Splitt numerator",r"\mathcal E'",r"\Sigma'",r"\unsure{\mathcal E|\Sigma}'","Two thick rounded bowls open to the right and join at a middle stroke, strongly favoring cursive E for Reader A. Candidate retains the current shared uncertainty. Prime is a separate tick.","first")
add("second splitting-map label index",r"\Psi:",r"\Psi_j :",r"\Psi_{\unsure{j}}:",True,False,"omission","Two tiny dark strokes lie below/right of Psi before the separately placed colon. An upper dot-like stroke and lower hook could make j, but identification remains uncertain.","low","second",False,True)
alphabet("second splitting-map domain",r"\widetilde X'(j)",r"\widetilde{\mathfrak{X}}'(j)",r"\widetilde{\mathfrak X}'(j)","The looped X has tilde and prime; lowercase j descends in a long hook.","second")
add("second splitting-map shaft",r"\arrow[r,dash]",r"\longrightarrow",r"\arrow[r,dash]",False,True,"drawing or diagram","The single thin shaft ends in a small thickening without returning sides or a triangular head, unlike the clear arrow in the line above.","high","second",False,True)
action("second Splitt numerator",r"\mathcal E'_j",r"\Sigma'_j",r"\unsure{\mathcal E|\Sigma}'_j","The letter is more flattened and cursive here; prime and descending j are separately visible. Shared E/Sigma uncertainty remains.","second")
add("margin first word","inutile","inutiles","inutile",False,True,"misread word","After the final l there is one low e-like return and no distinct additional s.","high","margin")
add("margin first clause","de se les donner",r"\uncertain{dans ces} \ill{}","de se les donner",False,True,"misread word","Separate de, se, les outlines precede the looped d and low joined letters of donner. The long separator crosses part of the word without canceling the note.","high","margin",True)
add("margin second clause","elles résultent des autres",r"\uncertain{elles résultent des précédentes}","elles résultent des autres",False,True,"misread word","Elles and résultent are readable; the last short word is on its own line and has the a/u opening and crossed t of autres, without the length or initial p of précédentes.","high","margin",True)
add("marginal separator","[no witness]","séparée du texte par un trait",r"\draw (1.25,0.15) -- (1.05,-1.55);",True,False,"drawing or diagram","A long straight oblique stroke stands beside and partly across the note. It is retained as a simple TikZ separator beside the upright marginal transcription.","high","margin")
add("canceled line before NB",r"\deleted{\unsure{Soit} $j,j'\in J$}",r"\struck{$\mathfrak{X}'_j$, $j \in J$}",r"\deleted{\unsure{Soit} $j,j'\in J$}",False,True,"deletion state","An S-like initial is heavily crossed. Two following long hooked j forms stand at the same writing level; a separate prime stands above the second, then membership and J. Initial Soit remains doubtful.","medium","deletion",False,True)
add("si after NB",r"\uline{NB} si",r"\emph{NB} Si",r"\uline{NB} si",False,True,"misread word","The s after the underlined NB is a small cursive form; the later Si gamma has a visibly larger capital S.")
alphabet("NB membership object",r"\widetilde X'(J)",r"\widetilde{\mathfrak{X}}'(J)",r"\widetilde{\mathfrak X}'(J)","The thickly traced X keeps its crossbar, separate tilde and prime.","nb")
alphabet("NB cover object",r"\widetilde X'[\unsure{j|\xi}]",r"\widetilde{\mathfrak{X}}'[j]",r"\widetilde{\mathfrak X}'[j]","Looped X with tilde and prime; bracketed j has one long stem and lower-left hook.","nb")
add("rev punctuation","rev universel",r"rev.\ universel","rev universel",False,True,"text not on the page","The v-like exit is followed by a blank interval before universel, without a dark period.","high","nb")
alphabet("rev universel de X-prime",r"de $X'$",r"de $\mathfrak{X}'$",r"de $\mathfrak X'$","The same looped X has its own prime.","nb")
add("cover en base point",r"en $\unsure{\xi|j}$",r"en $j$","en $j$",True,False,"misread symbol or index","The bare point has one long stem and a small head, without the successive xi bends seen in the first lifted point; it matches the bracketed j.","medium","nb",False,True)
alphabet("NB identification target",r"s'identifie à $\widetilde X'$",r"s'identifie à $\widetilde{\mathfrak{X}}'$",r"s'identifie à $\widetilde{\mathfrak X}'$","The identified target again has looped X, separate tilde and prime.","nb")
add("marked-point clause",r"est un pt marqué de $\widetilde X'$ au dessus de $\unsure{\xi|j}$","est un\npt au-dessus de $j$) \\ill{} des $\\widetilde{\\mathfrak{X}}'$ au dessus de $j$",r"est un p\textsuperscript{t} marqué de $\widetilde{\mathfrak X}'$ au dessus de $j$",True,True,"misread word","The t of pt is raised. Marqué has joined low letters and a long q descender; de directly precedes the lifted X, then au dessus de and one bare j. No earlier au-dessus de j or intervening parenthesis occurs.","high","nb",True,True)
add("cover-map connector",r"\arrow[r,dash,",r"\xrightarrow{\ \psi_{\widetilde{\xi}}\ }",r"\arrow[r,",True,False,"drawing or diagram","The shaft ends in a small raised triangular head with returning edges. This differs from the bare endpoint of the second splitting map.","high","point",False,True)
add("cover-map label",r"\unsure{\varphi|\Psi}_{\widetilde\xi}",r"\psi_{\widetilde{\xi}}",r"\unsure{\varphi|\psi}_{\widetilde\xi}",False,True,"misread symbol or index","The letter has an open left curl but an apparently closed right loop around its stem, favoring varphi. A looped psi remains possible. The subsequent equation's open forks are not imposed on this label.","low","point",False,True)
alphabet("cover-map source",r"\widetilde X'",r"\widetilde{\mathfrak{X}}'",r"\widetilde{\mathfrak X}'","Source X has the repeated looped graph, tilde and prime.","point")
alphabet("cover-map target",r"\widetilde X'[\unsure{j|\xi}]",r"\widetilde{\mathfrak{X}}'[j]",r"\widetilde{\mathfrak X}'[j]","Target X has tilde and prime; the point has a long hooked j stem.","point")
add("equivariance left map letter",r"\Psi_{\gamma\cdot\widetilde{\unsure{\xi|j}}}",r"\psi_{\gamma \cdot \widetilde{\xi}}",r"\Psi_{\gamma\cdot\widetilde\xi}",False,True,"misread symbol or index","The open fork and central stem match the upper capital-Psi labels at this formula's smaller scale. The subscript has gamma, a dot and the notched lifted xi.","medium","eq")
add("equivariance right map letter",r"\Psi_{\widetilde{\unsure{\xi|j}}}",r"\psi_{\widetilde{\xi}}",r"\Psi_{\widetilde\xi}",False,True,"misread symbol or index","The open fork and central stem repeat the left map letter; its xi subscript has an angular head and long descending stem.","medium","eq")
alphabet("equivariance action subscript",r"\gamma_{\widetilde X'}",r"\gamma_{\widetilde{\mathfrak{X}}'}",r"\gamma_{\widetilde{\mathfrak X}'}","The action subscript has looped X, wavy tilde and prime.","eq")
add("canceled inverse exponent",r"^{\deleted{\unsure{-1}}}","[no witness]",r"^{\deleted{\unsure{-1}}}",False,True,"deletion state","A raised canceled cluster stands after the action. Possible horizontal minus and upright 1 survive among crossed strokes, but the reading remains doubtful.","low","eq",False,True)
add("independence phrase","indépendamment du choix du pt base",r"indépendamment des choix \uncertain{d'un pt} base",r"indépendamment du choix du p\textsuperscript{t} base",True,True,"misread word","The first line ends with du; the next starts choix then another compact du. No final s in the first article or apostrophe/n in the second is visible. The t in pt is raised.","high",None,True)
alphabet("final left object",r"\widetilde X'[j]",r"\widetilde{\mathfrak{X}}'[j]",r"\widetilde{\mathfrak X}'[j]","Looped X with separate tilde, prime and bracketed long j.")
alphabet("final torsor factor",r"\widetilde X'(j)",r"\widetilde{\mathfrak{X}}'(j)",r"\widetilde{\mathfrak X}'(j)","The factor above the annotation has looped X, tilde, prime and parenthesized j.")
add("final wedge index",r"\mathbin{\wedge}_{\pi_1}",r"\wedge^{\pi_1}",r"\mathbin{\wedge}_{\pi_1}",False,True,"misread symbol or index","The pi_1 lies below and to the right of the wedge, beneath its vertex and the main baseline, not above it.",consequential=True)
alphabet("final last factor",r"\widetilde X'",r"\widetilde{\mathfrak{X}}'",r"\widetilde{\mathfrak X}'","The final X retains its looped graph, wavy tilde and distinct prime.")
add("torsor dr punctuation","torseur à dr sous ",r"torseur à dr.\ sous ","torseur à dr sous ",False,True,"text not on the page","The small dr is followed by sous without a distinct dark period.")
add("bottom numeral",r"\mspage{14}","[no witness]",r"\mspage{14}",False,True,"omission","A separate light handwritten 14 is present at the lower-left corner.")
decisions=[]
def dec(id,decision,reading,ink,confidence,where=None):
    crop,box=CR[where] if where else ("page",None)
    decisions.append(dict(id=id,decision=decision,reading=reading,ink=ink,crop=crop,box=box,confidence=confidence))
dec("M0674","first","des","Looped d followed by low e/s-like continuation rather than a compact u.","medium","title")
dec("M0675","first","I","Separate upper and lower bars on the central upright; hyphen follows.","high","title")
dec("M0676","first","fondamentaux","The ending is low and angled; no separate tall terminal l is visible.","medium","title")
dec("M0677","first",r"\mathrm{ex}","E-like loop and x strokes without a following t upright/crossbar.","high","first")
dec("M0678","first",r"\xi","Successive small bends at the head and a long descender distinguish lifted xi from bracketed j.","high","nb")
dec("M0679","first","j","Inside brackets: a single long stem with lower-left hook.","high","nb")
dec("M0680","alternative","j","Small head and one long stem, matching bracketed j rather than the initial notched xi.","medium","nb")
dec("M0681","first",r"\xi","Thin long stem and notched head with separate wavy tilde after puisque.","high","nb")
dec("M0682","alternative","j","A single narrow curved stem matches the bare j reference; no closing parenthesis follows.","medium","nb")
dec("M0683","undecided",r"\unsure{\varphi|\psi}","The apparently closed right loop favors varphi; a looped psi remains possible, unlike the clearly open forks in the equality.","low","point")
dec("M0684","first","j","The bracketed target has a pronounced descending j stem and hooked foot.","high","point")
dec("M0685","first",r"\xi","Angular head and long xi stem in the left subscript, with a small nearly flat accent.","high","eq")
dec("M0686","first",r"\xi","Right subscript repeats the angular head and long descending xi stem.","high","eq")
dec("M0687","first",r"\xi","Final base point has a tall narrow xi and clear wavy tilde, matching the lifted points above.","high")
assert [d["id"] for d in decisions]==[m["id"] for m in P["marks"]]
inventory=[]
for n,kind,pos,first in [
(1,"text","top paragraph, y 70–770","circled 7; Réconstruction des I-groupoïde fondamentaux; extension and actions; [et des applications (7) (8)"),
(2,"diagram","first splitting map, y 775–908","Psi^ex, lifted X-prime(J), right arrow, Splitt(E-prime/G-prime)/pi_1"),
(3,"diagram","second splitting map, y 905–1058","Psi with tiny doubtful index; parenthesized objects joined by bare shaft; closing bracket and period"),
(4,"margin note","oblique left margin, box [85,775,435,1150]","inutile de se les donner, elles résultent des autres"),
(5,"drawing","beside and partly across marginal note","long straight separator rule"),
(6,"display","y 1105–1190","Ob Pi_1 = J"),
(7,"deletion","box [292,1218,598,1324]","doubtful Soit, then j,j-prime in J"),
(8,"text","NB paragraph, y 1280–1590","underlined NB; lifted xi, cover at j, marked point; unclosed puisque parenthesis"),
(9,"diagram","box [565,1540,1095,1730]","lifted X-prime to lifted X-prime[j]; small arrowhead; phi/psi label"),
(10,"text","y 1750–1825","Si gamma in pi_1, on aura"),
(11,"display","box [615,1830,1000,1955]","Psi_(gamma dot lifted xi) = Psi_(lifted xi) composed with gamma_(lifted X-prime)"),
(12,"deletion","raised right edge of equality","canceled doubtful -1 exponent"),
(13,"text","y 1950–2145","donc on peut dire, indépendamment du choix du pt base lifted xi"),
(14,"diagram","bottom diagram, y 2140–2270","leftward isomorphism from lifted X-prime(j) wedge_(pi_1) lifted X-prime to lifted X-prime[j]"),
(15,"text","under first right-hand factor","torseur à dr sous pi_1, attached beneath a brace-like rule"),
(16,"text","bottom-left corner","14")
]:
    inventory.append(dict(sheet_kind="text",hand="his hand",element=f"E{n:02d}",kind=kind,position=pos,first_words_or_objects=first,transcribed="yes"))
cert=[]
for place,C,final,ink in [
("heading article",r"\unsure{des|du}","des","Looped d and low e/s-like continuation; title crop."),
("heading prefix",r"\unsure{I|1}","I","Upper and lower horizontal bars; title crop."),
("heading adjective",r"\unsure{fondamentaux|fondamental}","fondamentaux","Low angled ending without separate tall terminal l; title crop."),
("first exponent",r"\unsure{\mathrm{ex}|\mathrm{ext}}",r"\mathrm{ex}","No final t after the raised e/x strokes."),
("lifted point occurrences",r"\widetilde{\unsure{\xi|j}}",r"\widetilde\xi","The initial NB xi has successive head bends; all other lifted-point forms were compared individually."),
("bracketed points",r"\unsure{j|\xi}","j","One long stem with hooked foot, without xi head bends."),
("Ob line",r"\operatorname{Ob}\Pi_1=J",r"\operatorname{Ob}\Pi_1=J","Round O and looped b are readable; H uncertainty unnecessary.")
]:
    cert.append(dict(place=place,C=C,final=final,ink=ink))
report=dict(
key=KEY,reader="A",stage="first",image_views=["original","half1","half2"],
changes=changes,decisions=decisions,inventory=inventory,
remaining_doubts=[
dict(place="four extension-group letters",reading=r"\unsure{\mathcal E|\Sigma}",alternatives="cursive E; Sigma",confidence="low",reason="First Splitt has two rounded E-like bowls; the current shared notation still requires consistent unresolved encoding."),
dict(place="tiny second Psi index",reading=r"\Psi_{\unsure{j}}",alternatives="j; unidentified small correction/mark",confidence="low",reason="Two tiny strokes are present below/right of Psi before the colon, but are not securely identifiable."),
dict(place="initial canceled word",reading=r"\deleted{\unsure{Soit} $j,j'\in J$}",alternatives="Soit; another word under repeated strikes",confidence="low",reason="An S-like initial survives; middle letters lie under heavy hatching."),
dict(place="cover-map label",reading=r"\unsure{\varphi|\psi}_{\widetilde\xi}",alternatives="varphi; looped psi; capital Psi less favored by closed right loop",confidence="low",reason="An apparent closed right loop contrasts with open forks in the equality; possible source mismatch is preserved."),
dict(place="canceled exponent",reading=r"^{\deleted{\unsure{-1}}}",alternatives="-1; another overwritten short exponent",confidence="low",reason="Raised canceled cluster certain; only possible minus and 1 strokes survive.")
],
certainty_resolutions=cert,
notation=[
dict(form=r"\mathfrak X",meaning="Encoding of repeated looped, transversely crossed X.",evidence="Every X, prime and tilde inspected in prose and all displays. Alphabet-only rows are medium-confidence and non-consequential."),
dict(form=r"\unsure{\mathcal E|\Sigma}",meaning="Unsettled extension/action-group letter.",evidence="Two prose and two Splitt occurrences; first Splitt gives particularly strong two-bowl E-shaped evidence, second is flattened and cursive."),
dict(form=r"\widetilde\xi; j",meaning="Lifted point and bare point in cover references.",evidence="Initial xi has multiple head bends; bracketed j has one stem and hook. Bare j can have a tiny joined head rather than detached dot."),
dict(form=r"\Psi^{\mathrm{ex}};\Psi_{\unsure{j}}",meaning="Splitting-map labels.",evidence="First exponent contains e/x only; second tiny index remains doubtful. First connector is arrow, second is bare shaft."),
dict(form=r"\unsure{\varphi|\psi}_{\widetilde\xi};\Psi_{\widetilde\xi}",meaning="Doubtful cover-map label and open-forked equality notation.",evidence="Apparent closed right loop in cover-map label differs from open forks in equality."),
dict(form=r"\mathbin{\wedge}_{\pi_1}",meaning="Source contracted-product notation.",evidence="Pi_1 is lower-right of wedge; right-torsor annotation is beneath first factor. This entry is not a proof of the identification.")
],
abbreviations=[
dict(form="rev",expansion="revêtement"),dict(form=r"p\textsuperscript{t}",expansion="point"),
dict(form="dr",expansion="droite"),dict(form="NB",expansion="nota bene"),dict(form="Ob",expansion="objets"),
dict(form="ex",expansion="probably extérieur; not expanded by the source page")
],
hand_log=[
dict(habit="The extension letter has paired rounded bowls in a dark occurrence but a flattened form elsewhere.",places="143_scan015: four prose/Splitt occurrences.",scope="All four inspected; first Splitt is strongest E-shaped evidence.",misreadings="C E versus H Sigma remains provisionally unresolved."),
dict(habit="A small triangular endpoint can be an arrowhead, while a thickened dot alone is not.",places="143_scan015: first and second splitting maps and cover map.",scope="All three connectors compared; final left arrow separately inspected.",misreadings="C misses small head on cover map; H supplies a head on second splitting-map shaft."),
dict(habit="Xi has head bends and long descender; j may have a small joined head.",places="143_scan015 NB, map target, equality subscripts and final base point.",scope="Every packet xi/j doubt inspected; initial NB xi gives clearest comparison.",misreadings="C first alternatives at en xi and au dessus de xi change to j; lifted xi and bracketed j first readings otherwise stand."),
dict(habit="Small xi tildes flatten nearly to a short bar in subscripts.",places="143_scan015 cover-map label and equality, compared with NB and final base point.",scope="Qualified to this repeated lifted-point notation.",misreadings="No new barred-point variable inferred from flattened accent alone."),
dict(habit="Point abbreviation has raised t.",places="143_scan015 un pt marqué and du pt base.",scope="Both inspected.",misreadings="Both witnesses flatten t to baseline; candidate preserves superscript."),
dict(habit="Abbreviations need not have periods.",places="143_scan015 rev universel and torseur à dr sous.",scope="Both loci inspected for dark punctuation.",misreadings="H adds periods not visible after rev or dr."),
dict(habit="Looped X can be retraced thickly or simplified thinly.",places="143_scan015 all prose and displayed X expressions.",scope="Every X inspected with individual primes/tildes.",misreadings="C plain-X encoding changed to shared mathfrak-X encoding, not counted consequential.")
],
notes=[
dict(id=KEY+"-N1",text="Heading reads “Réconstruction des I-groupoïde fondamentaux”, preserving its accent and apparent number disagreement. The I has upper and lower bars; candidate does not silently change it to 1 or add s to groupoïde. The page names Pi_1(X-prime;J), the G-prime action and an extension by pi_1, then its action on the lifted point set and projection."),
dict(id=KEY+"-N2",text="The bracketed splitting maps have a clear first arrow and bare second shaft. First exponent is ex; the tiny possible j on second Psi remains doubtful. Margin says “inutile de se les donner, elles résultent des autres”. This is an account of the author's claim, not a proof that those data follow from the others."),
dict(id=KEY+"-N3",text="After Ob Pi_1=J and a canceled line, the underlined NB identifies the cover at j with the fixed lifted X using a marked lifted point. The parenthesis beginning “puisque” is not visibly closed at the prose end; none is supplied."),
dict(id=KEY+"-N4",text="The cover-map label appears phi-shaped, while the equality has open-forked Psi forms. The candidate leaves the former doubtful rather than harmonizing notation. A canceled possible inverse exponent is retained. The final text says “du choix du pt base” and gives the contracted product with lower pi_1 and a right-torsor annotation. These are source assertions, not verified theorems."),
dict(id=KEY+"-N5",text="Circled 7, bottom numeral 14, NB underline, both cancellations, marginal separator and lower torsor annotation are retained. No separate insertion was identified.")
],
check_events=[
dict(statement_id=KEY+"-splitting-data",type="carried as background without fault found",outcome="Read source maps and marginal claim. No proof of reconstruction from other data was attempted or used to settle labels or arrowheads."),
dict(statement_id=KEY+"-marked-cover",type="carried as background without fault found",outcome="Compared point letters with repeated visible forms and same-page bracketed references. No independent cover proof performed; map label not normalized from expected mathematics."),
dict(statement_id=KEY+"-equivariance-torsor",type="carried as background without fault found",outcome="Visually checked gamma dot, composition circle, action subscript, canceled exponent and lower wedge index. No proof of action formula or torsor identification performed.")
],
unresolved_for_main=[
"Recurring group letter: crops/143_scan015_A_first-map.png strongly favors cursive E for Reader A; candidate retains shared E/Sigma uncertainty.",
"Tiny second Psi index: crops/143_scan015_A_second-map.png; j possible but strokes uncertain.",
"Canceled initial Soit: crops/143_scan015_A_deletion.png; following j,j-prime in J is more secure.",
"Cover-map phi/psi label: crops/143_scan015_A_point-map.png; compare open forks in crops/143_scan015_A_equivariance.png without silently harmonizing.",
"Canceled possible -1: crops/143_scan015_A_equivariance.png."
],
raw_difference_disposition="All packet differences were inspected, including the malformed last raw-difference row concatenating later loci. Point letters, map label/head, canceled inverse, du/des and du/d’un, lower wedge index, dr punctuation and numeral 14 are accounted for separately. Every word, sign, accent, prime, underline, cancellation, marginal item and diagram was also inspected where C/H agree. Wrapper syntax, line breaks, H editorial sic and environment choices alone are excluded. Alphabet-only X rows are medium-confidence and non-consequential. Only this assigned page was inspected during this assignment; no web, OCR, text recognition or TeX compilation was used."
)
miss=[]
for i,row in enumerate(changes):
    for field,wit in [("C","witness_C"),("H","witness_H")]:
        if row[field]!="[no witness]" and row[field] not in P[wit]:
            miss.append([i+1,row["place"],field,row[field]])
(OUT/(KEY+"_readerA.json")).write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
print(json.dumps(dict(candidate=str(OUT/(KEY+"_readerA.tex")),report=str(OUT/(KEY+"_readerA.json")),changes=len(changes),decisions=len(decisions),inventory=len(inventory),non_exact_excerpts=miss),ensure_ascii=False))

