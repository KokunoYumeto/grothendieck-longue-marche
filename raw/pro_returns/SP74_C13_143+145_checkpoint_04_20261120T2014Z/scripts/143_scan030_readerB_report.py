import json
from pathlib import Path

ROOT = Path("/workspace/scratch/8f839dff4bf0/SP74_C13_143+145_work")
pkt = json.loads(Path("/workspace/scratch/8f839dff4bf0/reader_packets/143_scan030.json").read_text())
Csrc, Hsrc = pkt["witness_C"], pkt["witness_H"]
candidate = r"""
\scanpage{30}
\uline{isomorphisme}, et dont (2) se déduit en passant au profini. On a ainsi un \inserted{hom de} suites exactes
\margin{sauf si $g=0,\nu=0,1,2$\quad\figure{\begin{tikzpicture}\node[draw,ellipse] {$g=1,\nu=0$};\end{tikzpicture}}?}
\diagram{(4)\quad\begin{tikzcd}[ampersand replacement=\&,column sep=small,row sep=large]
1 \arrow[r,dash] \& \pi_1(\overline M_{g,\nu};\unsure{\xi|j}) \arrow[r,dash] \arrow[d,"\unsure{\tikz[baseline=-.5ex]{\node[rotate=90,inner sep=0pt] {$\simeq$};}|\wr}"',"\deleted{\unsure{\mathcal T_{g\nu}^{\wedge}}}"] \& \pi_1(M_{g,\nu};\unsure{\xi|j}) \arrow[r] \arrow[d] \& \Gamma \arrow[r,dash] \arrow[d,bend left=20] \& 1\\
1 \arrow[r] \& \mathcal T_{g,\nu}^{\wedge} \arrow[r] \& \operatorname{Autextlac}^{\circ}(\pi_1(X_{\unsure{\xi|j}}\setminus\{x_1,-x_\nu)) \arrow[r] \& \operatorname{Out}\unsure{T} \arrow[d,phantom,"\unsure{\vert|\downarrow}" description]\\
\&\&\&1
\end{tikzcd}}
\unsure{admettons} que $\mathcal T_{g,\nu}^{\wedge}\to$
\unsure{est invariant|injective} dans $\operatorname{Autextlac}^{\circ}(\ ?\ )$.
\margin{Version corrigée éventuelle : $\pi_1(M_{g,\nu};\unsure{\xi|j})\simeq$ Normalisateur de $\mathcal T_{g,\nu}^{\wedge}$ dans $\operatorname{Autextlac}^{\circ}(\pi_1(X_{\unsure{\xi|j}}\setminus\{x_1-x_\nu\unsure{\})|\}))}$ induisant des \unsure{autom} de $\mathcal T_{g,\nu}^{\wedge}$ commutant à $\mathfrak S_\nu$ et préservant une structure
\figure{\begin{tikzpicture}
\node[inner sep=1pt] (loc) at (0,0) {@DQOPEN@locale''};
\draw (-.85,.28)--(-.85,-.28)--(.85,-.28);
\draw (-.85,.28)--(.5,.28);
\end{tikzpicture}}
éventuelle\ldots $*$
\figure{\begin{tikzpicture}\draw (0,0)--(3.7,0);\end{tikzpicture}}}

On \deleted{\unsure{a}} aimerait que la flèche (1) (la flèche verticale centrale de (5)) soit un \uline{iso}. Cela donnerait une caractérisation de $\Gamma$ comme
\[
\operatorname{Autextlac}^{\circ}\left(\pi_1\underbrace{(X^{an}\setminus\{x_1,-x_\nu\})^{\wedge}}_{\substack{\text{groupe standard}\\\text{bien connu}}}\right)/\mathcal T_{g,\nu}^{\wedge}
\]
\margin{Pour $(g,\nu)$ sauf $g=0,\nu=0,1,2$\quad $g=1,\nu=0$ (cas où $\pi_1(X_{\unsure{\overline{\mathbf Q}|\mathbf Q}}\setminus S_\nu)$ \unsure{est un gr|est un groupe} abélien).
\deleted{\unsure{(cas} \illegible{1} \unsure{abélien} $*$ \unsure{est} \illegible{1}}}
\margin{Pour le cas $g=0,\nu=3$, il convient aussi d'être prudent et d'exiger des conditions de commutations avec \unsure{op|op.} ext. de $\mathfrak S_3$\ldots}

\uline{Ex} Pour $g=0,\nu=3$ celà donnerait l'expression déjà envisagée de $\Gamma$ comme
\[
\operatorname{Autextlac}^{\circ}(\pi_1(\mathbf P^1\setminus\{0,1,\infty\}).
\]
\mspage{29}
""".lstrip().replace("@DQOPEN@", chr(96)*2)

boxes = {
 "opening_clause":[715,56,1626,150],
 "upper_exception":[23,45,273,293],
 "diagram_upper_row":[384,357,1585,488],
 "diagram_left_link":[570,470,859,718],
 "diagram_right":[896,485,1681,796],
 "invariance":[333,747,1493,1047],
 "margin_normalizer":[17,577,646,1186],
 "cancelled_a":[495,1097,974,1178],
 "quotient":[362,1548,1553,1848],
 "margin_exception":[13,1168,511,1850],
 "margin_prudence":[15,1583,511,2348],
 "example_cela":[1094,1879,1621,1983],
 "example_formula":[347,2111,1214,2245],
}

def crop(name):
    return "page" if name == "page" else f"crops/143_scan030_readerB_{name}.png"

changes = []
def row(place, C, H, final, ac, ah, kind, ink, confidence="high", loc="page", marked=False, consequential=False):
    assert C == "[no witness]" or C in Csrc, ("C", place, C)
    assert H == "[no witness]" or H in Hsrc, ("H", place, H)
    assert not final or final in candidate, ("final", place, final)
    assert ac or ah, place
    changes.append(dict(place=place,C=C,H=H,final=final,against_C=ac,against_H=ah,
        kind=kind,ink=ink,confidence=confidence,crop=crop(loc),
        box=None if loc=="page" else boxes[loc],marked_in_H=marked,consequential=consequential))

row("Opening word: underline", r"\uline{isomorphisme}", r"\uncertain{isomorphisme}", r"\uline{isomorphisme}",
 False,True,"insertion or placement","A separate straight rule runs under isomorphisme; it is not part of the word's descending letters.")
row("Opening continuation", "et dont (2) se déduit en passant au profini.", r"et dans ces cas on \ill{} \ill{} un \ill{} \ill{}.",
 "et dont (2) se déduit en passant au profini.",False,True,"misread word",
 "The source has dont, a parenthesized curled 2, se déduit, and en passant au profini; these are successive written words rather than the clause supplied in H.",
 loc="opening_clause",marked=True)
row("Insertion above suites exactes", r"\inserted{hom de}", r"On a ainsi un \ill{} :", r"\inserted{hom de}",
 False,True,"insertion or placement","The small hom de is above the main baseline and has a curved attachment to suites exactes; it is an insertion of two short words.",
 loc="opening_clause",marked=True)
row("Opening baseline after un", "suites exactes", r"On a ainsi un \ill{} :", "suites exactes",False,True,
 "readable ink left as \\ill{}","The two baseline words end with the written plural s; no separate colon follows exactes.",loc="opening_clause",marked=True)
row("Upper-left exception: separation of cases", r"$g=0,\nu=0,1,2$\quad", r"$g = 0$, $\nu = 0, 1, 2$ ;",
 r"$g=0,\nu=0,1,2$\quad",False,True,"text not on the page",
 "The cases occupy separate source positions. There is no semicolon between 2 and the lower circled case.",loc="upper_exception")
row("Upper-left exception: circled scope", r"\node[draw,ellipse] {$g=1,\nu=0$};", "en haut à gauche, entouré",
 r"\node[draw,ellipse] {$g=1,\nu=0$};",False,True,"drawing or diagram",
 "The oval encloses only g=1, nu=0. The g=0 line is outside it and the author's question mark is outside to its right.",
 loc="upper_exception")
row("Diagram tag on the left", r"\hfill(4)", "le diagramme suivant est numéroté (4) par l'auteur",
 r"\diagram{(4)\quad",True,True,"insertion or placement",
 "The handwritten (4) lies at the left of the diagram between its two principal rows, not at the far right after it.")
row("Diagram: first upper link", r"1 \arrow[r,dash]", r"1 \arrow[r]", r"1 \arrow[r,dash]",
 False,True,"drawing or diagram","The right end of the first short horizontal link is rounded; it has no pair of converging arrowhead strokes.",
 loc="diagram_upper_row",consequential=True)
row("Diagram: first upper object, physical basepoint placement",
 r"\pi_1(\overline M_{g,\nu};\unsure{\xi|j})",r"\pi_1(\overline{M}_{g,\nu;\xi})",
 r"\pi_1(\overline M_{g,\nu};\unsure{\xi|j})",False,True,"misread symbol or index",
 "The g,nu are below M. The semicolon and tall basepoint graph are full height after M, and the bar belongs over M. The basepoint's letter remains uncertain.",
 "medium","diagram_upper_row",consequential=True)
row("Diagram: second upper link",
 r"\pi_1(\overline M_{g,\nu};\unsure{\xi|j}) \arrow[r,dash]",r"\pi_1(\overline{M}_{g,\nu;\xi}) \arrow[r]",
 r"\pi_1(\overline M_{g,\nu};\unsure{\xi|j}) \arrow[r,dash]",False,True,"drawing or diagram",
 "The second upper link also has a bare terminal, with only a small pen turn and no distinct pointed head.",
 loc="diagram_upper_row",consequential=True)
row("Diagram: second upper object, physical basepoint placement",
 r"\pi_1(M_{g,\nu};\xi)",r"\pi_1(M_{g,\nu;\xi})",r"\pi_1(M_{g,\nu};\unsure{\xi|j})",
 False,True,"misread symbol or index","Here too the semicolon/basepoint is at object height, outside the lower g,nu indices. The basepoint repeats the tall curled graph and has no secure detached dot.",
 "medium","diagram_upper_row",consequential=True)
row("Diagram: paired vertical strokes beside left vertical map",
 r"\simeq",r"\wr",r"\unsure{\tikz[baseline=-.5ex]{\node[rotate=90,inner sep=0pt] {$\simeq$};}|\wr}",
 True,True,"drawing or diagram","There are two separate vertically bent/wavy strokes. A rotated approximate sign records this orientation; the exact conventional name remains open. No detached question-mark dot is secure.",
 "low","diagram_left_link",True,True)
row("Diagram: H's question mark beside the left vertical map",
 r"\simeq", "un point\nd'interrogation", r"\unsure{\tikz[baseline=-.5ex]{\node[rotate=90,inner sep=0pt] {$\simeq$};}|\wr}",
 False,True,"text not on the page","The adjacent curved stroke is one of the paired vertical strokes. No distinct detached dot establishes an author question mark.",
 "medium","diagram_left_link",True)
row("Diagram: cancelled label at right of left vertical map",
 r"\deleted{\unsure{\mathcal T_{g\nu}}}",r"\mathcal{T}_{g\nu}",r"\deleted{\unsure{\mathcal T_{g\nu}^{\wedge}}}",
 True,True,"misread symbol or index","Blue zigzag cancellation crosses the label. A small angular completion mark seems to survive above/right of the T; the whole reading remains doubtful and the cancelled lower index is not regularized with a comma.",
 "low","diagram_left_link",True)
row("Diagram: last upper link",
 r"\Gamma \arrow[r,dash]",r"\Gamma \arrow[r]",r"\Gamma \arrow[r,dash]",
 False,True,"drawing or diagram","The last upper shaft ends in a short upright cap without a pointed arrowhead, unlike the preceding clear arrow into Gamma.",
 loc="diagram_upper_row",consequential=True)
row("Diagram: curved descending map from Gamma",
 r"\arrow[d,bend left=20]",r"\arrow[drr]",r"\arrow[d,bend left=20]",
 False,True,"drawing or diagram","The source connector curves outward to the right, then down to Out; its pointed head belongs to that same lower-right object.",
 loc="diagram_right")
row("Diagram: live lower T completion mark",
 r"\widehat{\mathcal T}_{g,\nu}",r"\widehat{\mathcal{T}}_{g,\nu}",r"\mathcal T_{g,\nu}^{\wedge}",
 True,True,"insertion or placement","The wedge is above and to the right of the T, horizontally over the lower g,nu area, rather than centered over the T body.",
 loc="diagram_left_link")
OPC=r"\operatorname{Autextlac}^{\circ}"
OPH=r"\mathrm{Autext}_{\mathrm{lac}}^{\circ}"
row("Diagram: lac on the operator baseline",OPC,OPH,OPC,False,True,"misread symbol or index",
 "The l ascender and joined a,c follow Autext on one baseline; only the small circle is raised.",loc="diagram_right")
row("Diagram: basepoint subscript under X omitted in both witnesses",
 r"\pi_1(X\setminus",r"\pi_1(X \smallsetminus",r"\pi_1(X_{\unsure{\xi|j}}\setminus",
 True,True,"omission","A separate long descending graph lies below/right of X before the set-minus stroke. Its presence as an index is secure; xi versus j is not.",
 "medium","diagram_right",consequential=True)
row("Diagram: written continuation stroke in puncture list",
 r"\{x_1,\ldots,x_\nu\}",r"\{x_1, \ldots, x_\nu\}",r"\{x_1,-x_\nu",
 True,True,"misread symbol or index","After x_1 and one comma there is a connected short horizontal stroke, then x_nu. There are not three detached continuation dots or a second comma.",
 "high","diagram_right")
row("Diagram: absent separate right set brace",
 r"x_\nu\}))",r"x_\nu\})\bigr)",r"x_\nu))",
 True,True,"text not on the page","Two closing parentheses are visible after x_nu, but no separate right curly brace precedes them. The candidate preserves the unmatched written opening brace.",
 "medium","diagram_right")
row("Diagram: clipped terminal group after Out",
 r"\unsure{\operatorname{Out}|\operatorname{Aut}}T",r"\mathrm{Out}\ldots",r"\operatorname{Out}\unsure{T}",
 False,True,"omission","Out begins with a broad closed O and is readable. The following T-shaped fragment reaches the cropped right edge and cannot be treated as a fully secure letter.",
 "low","diagram_right",True)
row("Diagram: final vertical connector to 1",
 r"T \arrow[d]",r"\ldots \arrow[d]",r'\arrow[d,phantom,"\unsure{\vert|\downarrow}" description]',
 True,True,"drawing or diagram","The descending shaft has a rounded terminal blot rather than a securely pointed head. The candidate explicitly retains bare-shaft versus downward-arrow alternatives.",
 "low","diagram_right",consequential=True)
row("Invariance line: opening word",
 r"\unsure{admettons}",r"\ldots\ que",r"\unsure{admettons}",
 False,True,"omission","The reduced beginning is overlapped by the diagonal marginal writing; the remaining main-line strokes permit admettons but do not settle it.",
 "low","invariance",True)
row("Invariance line: completion wedge",r"\widehat{\mathcal T}_{g,\nu}",r"\widehat{\mathcal{T}}_{g,\nu}",
 r"\mathcal T_{g,\nu}^{\wedge}\to",True,True,"insertion or placement",
 "This T again has its completion wedge above/right, with the g,nu low to the right.",loc="invariance")
row("Invariance line: arrow after completed T",
 r"\widehat{\mathcal T}_{g,\nu}$ est",r"\to",r"\mathcal T_{g,\nu}^{\wedge}\to",
 True,False,"omission","A short shaft with a raised, pointed right terminal follows T. It is retained in place even though the surrounding words are crowded.",
 "medium","invariance",consequential=True)
row("Invariance line: predicate",
 "est invariant dans",r"\uncertain{injective} \ill{}",r"\unsure{est invariant|injective} dans",
 False,True,"misread word","The lower main line ends with the separated word dans; the preceding joined letters look closer to invariant but are crossed/overlapped. The predicate remains explicitly uncertain rather than being reconstructed from a desired group statement.",
 "low","invariance",True,True)
row("Invariance line: lac placement",OPC,OPH,OPC,False,True,"misread symbol or index",
 "The three lac letters are on the Autext baseline, with the circle above them.",loc="invariance")
row("Invariance line: author's question mark argument",
 r"(\ ?\ )",r"(\ill{})",r"(\ ?\ )",False,True,"misread symbol or index",
 "Inside the large round parentheses is the author's curved question-mark stroke; it is not an editorial illegibility placeholder. A period follows the closing parenthesis.",
 loc="invariance",marked=True)
row("First diagonal margin: heading",
 "Version corrigée éventuelle :", "Vérifier conjecture :", "Version corrigée éventuelle :",
 False,True,"misread word","The first word ends in the long reduced sion sequence. The next line has corrigée followed by éventuelle, and two stacked dots supply the colon.",
 loc="margin_normalizer")
row("First diagonal margin: M object and basepoint placement",
 r"\pi_1(M_{g,\nu};\unsure{\xi|j})",r"\pi_1(M_{g,\nu;\xi})",r"\pi_1(M_{g,\nu};\unsure{\xi|j})",
 False,True,"misread symbol or index","The M has only g,nu below it. The semicolon and tall curled basepoint follow at full height; the letter remains xi/j.",
 "medium","margin_normalizer",consequential=True)
row("First diagonal margin: Normalisateur capital",
 "Normalisateur", "normalisateur", "Normalisateur",False,True,"misread word",
 "The initial has a tall two-stem N form before the reduced remainder of the word.",loc="margin_normalizer")
row("First diagonal margin: T after Normalisateur de",
 r"\widehat{\mathcal T}_{g,\nu}",r"\widehat{\mathcal{T}}_{g,\nu}",r"Normalisateur de $\mathcal T_{g,\nu}^{\wedge}$",
 True,True,"insertion or placement","The wedge is to the upper right of this T and separate from the lower genus/marking indices.",loc="margin_normalizer")
row("First diagonal margin: operator lac placement",OPC,OPH,OPC,False,True,"misread symbol or index",
 "The written operator has a looped l and low a,c continuing on its main baseline, not below it.",loc="margin_normalizer")
row("First diagonal margin: puncture list and closing signs",
 r"X_{\unsure{\xi|j}}\setminus\{x_1,\ldots,x_\nu\}))",r"X_\xi \smallsetminus \{x_1,",
 r"X_{\unsure{\xi|j}}\setminus\{x_1-x_\nu\unsure{\})|\}))}",
 True,True,"misread symbol or index",
 "The puncture separator is one connected horizontal continuation stroke. The ending shows a curly return and a parenthesis; a second nearby parenthesis is not securely separable in the crowded writing and remains an explicit alternative. The low X basepoint remains uncertain.",
 "low","margin_normalizer",True)
row("First diagonal margin: induisant des autom de",
 r"induisant des \unsure{autom} de",r"\ldots\ commutant",r"induisant des \unsure{autom} de",
 False,True,"omission","The line begins induisant des, followed by a reduced autom-shaped abbreviation and de. The abbreviation stays doubtful; it is not expanded.",
 "medium","margin_normalizer",True)
row("First diagonal margin: second T, after autom de",
 r"\widehat{\mathcal T}_{g,\nu}$ commutant",r"\ldots\ commutant",
 r"\mathcal T_{g,\nu}^{\wedge}$ commutant",True,True,"insertion or placement",
 "A second T with low g,nu and upper-right completion wedge appears before commutant. The long nearby divider is not treated as a strike through the formula.",
 "medium","margin_normalizer",True)
row("First diagonal margin: commutation datum",
 r"commutant à $\mathfrak S_\nu$",r"commutant \ill{} et",r"commutant à $\mathfrak S_\nu$",
 False,True,"readable ink left as \\ill{}","The word commutant is followed by à and a large looped S graph with a separate low nu, then et.",
 "medium","margin_normalizer",True,True)
row("First diagonal margin: structural condition",
 "et préservant une structure",r"et structure \ill{}", "et préservant une structure",
 False,True,"omission","Between et and structure are the distinct reduced words préservant une; the line is not just et structure.",
 "medium","margin_normalizer",True)
row("First diagonal margin: framed locale",
 chr(96)*2+"locale''",r"\uncertain{locale}",
 r"\node[inner sep=1pt] (loc) at (0,0) {"+chr(96)*2+"locale''};",
 True,True,"drawing or diagram","In addition to the quote ticks, an angular frame has a left vertical, a lower segment and an upper segment around locale. The candidate reproduces these three visible sides.",
 "high","margin_normalizer",True)
row("First diagonal margin: ending",
 r"éventuelle\ldots $*$",r"\uncertain{locale} \ldots",r"éventuelle\ldots $*$",
 False,True,"omission","After the framed locale comes éventuelle, a short suspension ending and a separate star.",loc="margin_normalizer",marked=True)
row("First diagonal margin: long divider",
 r"éventuelle\ldots $*$",r"\uncertain{locale} \ldots",r"\draw (0,0)--(3.7,0);",
 True,True,"drawing or diagram","A long separate straight divider lies beneath/along the marginal note and passes near the final T indices. It is recorded as a rule, not as deletion of the live T or locale.",
 "high","margin_normalizer",True)
row("Main paragraph: cancelled letter after On",
 r"On \deleted{\unsure{a}} aimerait",r"On \uncertain{aimerait} \ill{} que",
 r"On \deleted{\unsure{a}} aimerait",False,True,"deletion state",
 "The thick triangular cancellation is before aimerait, immediately after On. An a-like loop and stem survive inside it, but the letter is still doubtful.",
 "low","cancelled_a",True)
row("Main paragraph: no extra unreadable word after aimerait",
 "aimerait que",r"\uncertain{aimerait} \ill{} que","aimerait que",False,True,"text not on the page",
 "The live aimerait runs directly to que; the cancelled material belongs before aimerait, not in this position.",loc="cancelled_a",marked=True)
row("Main paragraph: underlined iso",
 r"\uline{iso}",r"\uncertain{iso}",r"\uline{iso}",False,True,"insertion or placement",
 "A separate line lies beneath iso; the letters i,s,o and the following full stop are visible.")
row("Main paragraph: caractérisation",
 "caractérisation", "construction", "caractérisation",False,True,"misread word",
 "After donnerait une, the source has the longer caractère-based letter sequence, including the accented e and final isation.")
row("Quotient display: lac placement",OPC,OPH,OPC,False,True,"misread symbol or index",
 "The lac letters continue on the operator baseline, with a small round superscript above.",loc="quotient")
row("Quotient display: analytic superscript on X",
 r"\unsure{X^{an}|\overline X}",r"\pi_1(X \smallsetminus",r"X^{an}\setminus",
 False,True,"omission","Above/right of X are two tiny letters, a rounded a and a reduced n; no overbar spans X.",
 "high","quotient",consequential=True)
row("Quotient display: continuation stroke",
 r"\{x_1,\ldots,x_\nu\}",r"\{x_1, \ldots, x_\nu\}",r"\{x_1,-x_\nu\}",
 True,True,"misread symbol or index","There is one comma after the low 1 and one short continuous stroke before x_nu, with no second comma. Here a separate right curly brace is present.",
 "high","quotient")
row("Quotient display: underbrace physical span",
 r"\underbrace{\pi_1",r"\underbrace{\mathrm{Autext}",
 r"\pi_1\underbrace{(X^{an}\setminus\{x_1,-x_\nu\})^{\wedge}}",
 True,True,"insertion or placement",
 "The left end is around the low 1/following opening parenthesis, not the left of the operator or even the left edge of pi. The right end lies under the completed inner argument. Autextlac, the outer parenthesis and the denominator are outside its span.",
 "high","quotient")
row("Quotient display: underbrace label",
 r"\text{groupe standard}\ \text{bien connu}",r"\text{groupe \ill{} bien connu}",
 r"\substack{\text{groupe standard}\\\text{bien connu}}",False,True,"readable ink left as \\ill{}",
 "The first annotation line reads groupe standard; a separate line below reads bien connu. The tall initial of standard and its ending are visible.",
 "medium","quotient",True)
row("Quotient display: denominator completion",
 r"/\widehat{\mathcal T}_{g,\nu}",r"\big/ \widehat{\mathcal{T}}_{g,\nu}",r"/\mathcal T_{g,\nu}^{\wedge}",
 True,True,"insertion or placement","The denominator T has its small angular completion mark at the upper right, aligned above the low g,nu indices.",loc="quotient")
row("Second diagonal margin: introductory words",
 r"Pour $(g,\nu)$ sauf",r"p.\ ex.\ $(g, \nu)$ \ldots",r"Pour $(g,\nu)$ sauf",
 False,True,"misread word","A tall P begins Pour, followed by the parenthesized g,nu and the separately written sauf with its long final f.",
 loc="margin_exception",marked=True)
row("Second diagonal margin: exceptional cases",
 r"$g=0,\nu=0,1,2$\quad $g=1,\nu=0$",r"$g = 0$, $\nu = 0, 1, 2$ ; $g = 1$",
 r"$g=0,\nu=0,1,2$\quad $g=1,\nu=0$",False,True,"omission",
 "The two rows give g=0,nu=0,1,2 and g=1,nu=0. The final nu=0 is written, and no semicolon separates the source rows.",
 loc="margin_exception",marked=True,consequential=True)
row("Second diagonal margin: parenthetic cas où",
 "(cas où",r"\ldots\ il conviendrait", "(cas où",False,True,"omission",
 "Below the cases, a live opening parenthesis and cas où introduce the fundamental-group formula, above the framed cancellation.",
 "medium","margin_exception",True)
row("Second diagonal margin: fundamental-group formula",
 r"\unsure{\pi_1(X_{\overline{\mathbf Q}}\setminus S_\nu)|\pi_1(X\setminus S_\nu)}",
 "[no witness]",r"\pi_1(X_{\unsure{\overline{\mathbf Q}|\mathbf Q}}\setminus S_\nu)",
 False,True,"omission",
 "A low closed Q-like graph is definitely present after X; the short bar above it is entangled with nearby ink and stays uncertain. The separate set-minus and S with low nu are retained. Bold/blackboard Q is only a rendering convention.",
 "medium","margin_exception",True,True)
row("Second diagonal margin: abelian-group phrase",
 r"\unsure{est un groupe abélien}","[no witness]",r"\unsure{est un gr|est un groupe} abélien",
 True,True,"abbreviation expanded or spelling modernised",
 "The live phrase to the right of the cancelled block ends with abélien. The preceding reduced group word looks like gr, without secure remaining oupe letters; the competing full-word reading remains explicit.",
 "low","margin_exception",True,True)
row("Second diagonal margin: framed cancellation and surviving first-line fragment",
 r"\deleted{\unsure{abélien} $*$ \unsure{est} \illegible{1}}",
 "un bloc de la\nseconde, encadré, est raturé en zigzag et n'a pas été lu",
 r"\deleted{\unsure{(cas} \illegible{1} \unsure{abélien} $*$ \unsure{est} \illegible{1}}",
 True,True,"deletion state",
 "A rectangle and repeated zigzag strokes cancel several lines. A possible initial (cas survives above the clearer abélien/star line; est-like strokes remain at the bottom. The unrecoverable stretches are marked physically illegible, and no sentence is supplied.",
 "low","margin_exception",True)
row("Third diagonal margin: separate case and prudence clause",
 r"Pour le cas $g=0,\nu=3$, il convient aussi d'être prudent",
 r"il conviendrait d'être \ill{} l'exigence \ill{} \ldots",
 r"Pour le cas $g=0,\nu=3$, il convient aussi d'être prudent",
 False,True,"misread word",
 "This is a separate lower note beginning Pour le cas, with g=0 and nu=3. The verb has the source ending convient, followed by aussi, d'être and prudent.",
 loc="margin_prudence",marked=True,consequential=True)
row("Third diagonal margin: conditions",
 "et d'exiger des conditions de commutations",r"l'exigence \ill{} \ldots",
 "et d'exiger des conditions de commutations",False,True,"omission",
 "The next words are et d'exiger des conditions de commutations; the reduced final plural ending is retained rather than replacing this by l'exigence.",
 "medium","margin_prudence",True,True)
row("Third diagonal margin: op abbreviation stop",
 "op. ext.",r"\ldots",r"\unsure{op|op.} ext.",True,True,"abbreviation expanded or spelling modernised",
 "The short op ends at the line's right without a securely detached stop. ext. begins the following source line and has a visible stop; the op punctuation remains an explicit local alternative.",
 "medium","margin_prudence",True)
row("Third diagonal margin: exterior operations and group",
 r"avec op. ext. de $\mathfrak S_3$\ldots","[no witness]",
 r"avec \unsure{op|op.} ext. de $\mathfrak S_3$\ldots",
 False,True,"omission",
 "The note continues avec, the two abbreviated words, de, and a large ornate S with a separate low 3, followed by suspension marks. The S's encompassing loop is part of its graph, not a separate circle around a different label.",
 "medium","margin_prudence",True,True)
row("Example: celà",
 "celà donnerait", "cela donnerait", "celà donnerait",False,True,"abbreviation expanded or spelling modernised",
 "There is a separate short accent stroke above/right of the reduced final a area of celà; the source spelling is retained.",
 "medium","example_cela")
row("Final display: lac placement",OPC,OPH,OPC,False,True,"misread symbol or index",
 "The final display again keeps lac on the operator baseline, with its circle above.",loc="example_formula")
row("Final display: incomplete parentheses",
 r"\operatorname{Autextlac}^{\circ}\bigl(\pi_1(\mathbf P^1\setminus\{0,1,\infty\})\bigr).",
 r"\{0, 1, \infty\})\bigr).",
 r"\operatorname{Autextlac}^{\circ}(\pi_1(\mathbf P^1\setminus\{0,1,\infty\}).",
 True,True,"text not on the page",
 "Two opening round parentheses are written, one after the operator and one after pi_1. After the curly brace there is only one closing parenthesis, then a period. The absent second closing parenthesis is not supplied.",
 "high","example_formula")
row("Pencil footer pagination",
 r"\mspage{29}","[no witness]",r"\mspage{29}",False,True,"omission",
 "The light pencil digits at the bottom-left read 29. Their hand is not attributed to the main writer.",loc="margin_prudence")

decisions = [
 dict(id="M0729",decision="undecided",reading=r"\unsure{\xi|j}",ink="The first top-row basepoint is a tall curled descending graph without a secure detached dot; xi versus j remains open.",crop=crop("diagram_upper_row"),box=boxes["diagram_upper_row"],confidence="low"),
 dict(id="M0730",decision="first",reading=r"\operatorname{Out}",ink="The initial is a large closed O followed by u,t, not an A. The clipped following T is a separate new doubt.",crop=crop("diagram_right"),box=boxes["diagram_right"],confidence="high"),
 dict(id="M0731",decision="undecided",reading=r"\unsure{admettons}",ink="Main-line letters are partially overlapped by diagonal marginal text; admettons is possible but not fully separable.",crop=crop("invariance"),box=boxes["invariance"],confidence="low"),
 dict(id="M0732",decision="undecided",reading=r"\unsure{\xi|j}",ink="The marginal M basepoint has the same tall curl/stem, physically full height after the semicolon, with no secure independent dot.",crop=crop("margin_normalizer"),box=boxes["margin_normalizer"],confidence="low"),
 dict(id="M0733",decision="undecided",reading=r"\unsure{\xi|j}",ink="The low index under marginal X is present, but the curved descending graph cannot be uniquely named xi or j.",crop=crop("margin_normalizer"),box=boxes["margin_normalizer"],confidence="low"),
 dict(id="M0734",decision="undecided",reading=r"\unsure{autom}",ink="The compressed word between des and de has an autom-like sequence; some joined strokes remain inseparable. No expansion is made.",crop=crop("margin_normalizer"),box=boxes["margin_normalizer"],confidence="low"),
 dict(id="M0735",decision="first",reading=r"X^{an}",ink="Two small upper-right letters have a rounded a and a reduced n; no bar spans X.",crop=crop("quotient"),box=boxes["quotient"],confidence="high"),
 dict(id="M0736",decision="other",reading=r"\pi_1(X_{\unsure{\overline{\mathbf Q}|\mathbf Q}}\setminus S_\nu)",ink="The X definitely has a low Q-like index, excluding the no-index alternative; only its small overbar remains open under neighboring ink.",crop=crop("margin_exception"),box=boxes["margin_exception"],confidence="medium"),
 dict(id="M0737",decision="other",reading=r"\unsure{est un gr|est un groupe} abélien",ink="The live ending abélien is readable; the reduced group word looks abbreviated gr, although the overwritten word boundaries do not settle the full phrase.",crop=crop("margin_exception"),box=boxes["margin_exception"],confidence="low"),
]

inventory = []
def inv(kind,position,first,hand="his hand"):
    inventory.append(dict(sheet_kind="text",hand=hand,element=f"E{len(inventory)+1:02d}",kind=kind,position=position,first_words_or_objects=first,transcribed="yes"))
inv("text","top main line","isomorphisme, et dont (2) se déduit en passant au profini")
inv("insertion","above suites exactes","hom de")
inv("margin note","upper left","sauf si g=0,nu=0,1,2")
inv("drawing","upper left, within preceding note","ellipse around g=1,nu=0; question mark outside")
inv("diagram","upper-middle page","two principal rows of (4), plus terminal lower 1")
inv("text","left of diagram, between rows","(4)")
inv("text","left of the first vertical map","paired vertical bent/wavy strokes")
inv("deletion","right of the first vertical map","cancelled T with possible completion wedge and gnu")
inv("text","below diagram","admettons que ... est invariant dans ...")
inv("margin note","first long diagonal note at left","Version corrigée éventuelle :")
inv("display","inside first diagonal note","pi_1(M...) ~= Normalisateur de completed T dans Autextlac...")
inv("text","continuation of first diagonal note","induisant des autom ... commutant à S_nu")
inv("drawing","near end of first diagonal note","angular three-sided frame around quoted locale")
inv("drawing","beneath/along first diagonal note, near final T indices","long straight divider")
inv("text","main paragraph below invariance line","On ... aimerait que la flèche (1) ... de (5) ... iso")
inv("deletion","between On and aimerait","cancelled a-shaped graph")
inv("text","continuation before quotient display","Cela donnerait une caractérisation de Gamma comme")
inv("display","main middle-lower display","Autextlac circle applied to completed pi_1 argument / completed T")
inv("drawing","under the inner completed argument","underbrace with two-line groupe standard / bien connu")
inv("margin note","second long diagonal note at left","Pour (g,nu) sauf g=0... g=1...")
inv("display","within second diagonal note","pi_1(X with low Q-like index minus S_nu)")
inv("deletion","framed zigzag cancellation beneath exception formula","partial (cas..., abélien, star, est..., unreadable remnants")
inv("margin note","third long diagonal note down to lower-left edge","Pour le cas g=0,nu=3, il convient aussi d'être prudent")
inv("text","main bottom example","underlined Ex; Pour g=0,nu=3 celà donnerait...")
inv("display","bottom main line","Autextlac circle (pi_1(P^1 minus {0,1,infinity}) with only one closing parenthesis")
inv("text","bottom-left pencil footer","29",hand="unknown (pencil pagination)")

remaining_doubts = [
 dict(place="Top diagram first basepoint, M0729",reading=r"\unsure{\xi|j}",alternatives="xi / j",confidence="low",reason="Tall curl/stem with no secure detached dot; crop diagram_upper_row."),
 dict(place="Top diagram second basepoint, newly marked",reading=r"\pi_1(M_{g,\nu};\unsure{\xi|j})",alternatives="xi / j",confidence="low",reason="Same source graph as first basepoint; neither witness marked this occurrence. Crop diagram_upper_row."),
 dict(place="Diagram left vertical-map label",reading=r"\unsure{\tikz[baseline=-.5ex]{\node[rotate=90,inner sep=0pt] {$\simeq$};}|\wr}",alternatives="rotated approximate sign / paired vertical wr-like graph",confidence="low",reason="Two separate vertical bent strokes are visible; their conventional name remains open. No author question-mark dot is supplied. Crop diagram_left_link."),
 dict(place="Cancelled right label of left vertical map",reading=r"\deleted{\unsure{\mathcal T_{g\nu}^{\wedge}}}",alternatives="completed T with gnu / T with obscured upper strokes",confidence="low",reason="Blue zigzag cancellation entangles the T, the possible upper-right wedge and the lower indices. Crop diagram_left_link."),
 dict(place="New lower-diagram X index",reading=r"X_{\unsure{\xi|j}}",alternatives="xi / j",confidence="low",reason="The index is securely present but its letter remains uncertain; crop diagram_right."),
 dict(place="Clipped group after Out",reading=r"\operatorname{Out}\unsure{T}",alternatives="T / incomplete unidentified continuation",confidence="low",reason="Out is settled; the following T-shaped fragment runs into the scan edge. Crop diagram_right."),
 dict(place="Final vertical connector to lower 1",reading=r"\unsure{\vert|\downarrow}",alternatives="bare vertical shaft / downward arrow",confidence="low",reason="Terminal blot is rounded rather than securely pointed; crop diagram_right."),
 dict(place="Invariance opening, M0731",reading=r"\unsure{admettons}",alternatives="admettons / unreadable reduced opening",confidence="low",reason="Diagonal marginal ink overlaps the main word; crop invariance."),
 dict(place="Invariance predicate",reading=r"\unsure{est invariant|injective}",alternatives="est invariant / injective with unclear connecting text",confidence="low",reason="The line is crowded and only the final dans is secure. The short arrow after T is preserved independently; crop invariance."),
 dict(place="Normalizer M basepoint, M0732",reading=r"\unsure{\xi|j}",alternatives="xi / j",confidence="low",reason="Tall curled graph, full height after semicolon; crop margin_normalizer."),
 dict(place="Normalizer X basepoint, M0733",reading=r"X_{\unsure{\xi|j}}",alternatives="xi / j",confidence="low",reason="Low descending index lacks a decisive distinguishing stroke; crop margin_normalizer."),
 dict(place="Normalizer puncture formula closing signs",reading=r"\unsure{\})|\}))}",alternatives="right brace and one parenthesis / right brace and two parentheses",confidence="low",reason="Crowding at the end does not securely separate a possible second parenthesis; crop margin_normalizer."),
 dict(place="Normalizer autom abbreviation, M0734",reading=r"\unsure{autom}",alternatives="autom / incompletely separable reduced abbreviation",confidence="low",reason="Joined strokes between des and de remain cramped; crop margin_normalizer."),
 dict(place="Cancelled a before aimerait",reading=r"\deleted{\unsure{a}}",alternatives="a / overwritten triangular graph",confidence="low",reason="Some loop/stem ink survives but a thick cancellation covers it; crop cancelled_a."),
 dict(place="Exception X low index, M0736",reading=r"X_{\unsure{\overline{\mathbf Q}|\mathbf Q}}",alternatives="barred Q / Q",confidence="medium",reason="Presence of Q-like index is secure; its short overbar is entangled. Crop margin_exception."),
 dict(place="Exception phrase, M0737",reading=r"\unsure{est un gr|est un groupe} abélien",alternatives="est un gr abélien / est un groupe abélien",confidence="low",reason="A shortened group word is favored, but the live line intersects other ink. Crop margin_exception."),
 dict(place="Framed cancellation",reading=r"\deleted{\unsure{(cas} \illegible{1} \unsure{abélien} $*$ \unsure{est} \illegible{1}}",alternatives="partial (cas / other cancelled beginning; abélien and est tentative",confidence="low",reason="Rectangle plus repeated zigzag strikes physically obliterate substantial text. The star is present; no complete sentence is reconstructed. Crop margin_exception."),
 dict(place="Third margin op punctuation",reading=r"\unsure{op|op.} ext.",alternatives="op / op.",confidence="medium",reason="No securely detached stop after op; ext. has one. Crop margin_prudence."),
]

certainty_resolutions = [
 dict(place="M0730: Out",C=r"\unsure{\operatorname{Out}|\operatorname{Aut}}",final=r"\operatorname{Out}",ink="Closed initial O, then u,t. The following clipped T remains a separate doubt."),
 dict(place="M0735: upper-right an",C=r"\unsure{X^{an}|\overline X}",final=r"X^{an}",ink="Two small letters above/right of X, rather than a bar spanning X."),
 dict(place="M0736: index present",C=r"\unsure{\pi_1(X_{\overline{\mathbf Q}}\setminus S_\nu)|\pi_1(X\setminus S_\nu)}",final=r"\pi_1(X_{\unsure{\overline{\mathbf Q}|\mathbf Q}}\setminus S_\nu)",ink="The no-index alternative is excluded by a definite low closed graph. Uncertainty is localized to its bar."),
]

notation = [
 dict(form=r"\mathcal T_{g,\nu}^{\wedge}",meaning="Completion notation for the modular/Teichmüller T with genus and marking indices",evidence="Individually seen in lower diagram, invariance line, both normalizer occurrences and quotient denominator; the wedge is physically upper-right, not centered above T."),
 dict(form=r"\operatorname{Autextlac}^{\circ}",meaning="The page's exterior-automorphism operator notation",evidence="lac remains on the baseline in the diagram, invariance, normalizer, quotient and final example; the small circle is raised."),
 dict(form=r"\xi / j",meaning="Basepoint graph, unresolved alphabet identification",evidence="Tall curled descending graph in top diagram objects, lower-diagram X and both first-margin basepoints; placement is checked separately at every occurrence."),
 dict(form=r"x_1,-x_\nu; x_1-x_\nu",meaning="Literal connected continuation stroke in puncture lists",evidence="Diagram and quotient have a comma after x_1; the crowded first margin has no secure comma. This is a transcription of a continuation mark, not an assertion of algebraic subtraction."),
 dict(form=r"\tikz[baseline=-.5ex]{\node[rotate=90,inner sep=0pt] {$\simeq$};}",meaning="Preferred physical rendering of paired vertical bent strokes",evidence="Left vertical-map label; conventional identity remains locally unsure against wr. No detached question-mark dot is secure."),
 dict(form=r"\mathbf Q,\mathbf P",meaning="Retained source-witness rendering convention for field/projective-space graphs",evidence="Ordinary/bold/blackboard typeface alone is not a material reading change. Q's physical low index and possible overbar, and P's exponent 1, were checked independently."),
]
abbreviations = [
 dict(form="hom",expansion="homomorphisme; expansion is explanatory only"),
 dict(form="autom",expansion="automorphismes, if the doubtful abbreviation is correct"),
 dict(form="gr",expansion="groupe, if the preferred short reading is correct"),
 dict(form="op",expansion="opérations"),
 dict(form="ext.",expansion="extérieures"),
 dict(form="Ex",expansion="Exemple"),
]
hand_log = [
 dict(habit="Small angular completion wedge placed after the letter at upper-right",places="143_scan030 lower T, invariance T, both marginal T's, quotient denominator; possible cancelled T",scope="Every live occurrence inspected separately; cancelled instance remains doubtful",misreadings="Both witnesses center a widehat over each live T."),
 dict(habit="Reduced xi/j-like graph with a long descender",places="143_scan030 top row and X basepoints in lower diagram and normalizer note",scope="All visible occurrences checked; alphabet remains unresolved",misreadings="H lowers semicolon and basepoint into M indices; both witnesses omit the lower-diagram X index."),
 dict(habit="Short connected stroke used for a puncture-list continuation",places="143_scan030 diagram, normalizer margin, quotient",scope="All three inspected; punctuation differs locally",misreadings="C and H normalize the stroke to three dots and often supply a second comma."),
 dict(habit="Very reduced word endings and overlap of diagonal notes with main lines",places="143_scan030 invariance opening/predicate, autom, exception phrase",scope="These loci remain explicitly doubtful",misreadings="H reconstructs several clauses; no grammar or expected group statement is used to supply letters."),
 dict(habit="Two vertical bent strokes beside a vertical map",places="143_scan030 diagram left link",scope="This occurrence compared to the established paired-wave notation convention without reopening other pages",misreadings="C makes the label horizontal; H adds a question-mark dot that is not secure here."),
 dict(habit="Pencil pagination separate from main ink",places="143_scan030 lower-left 29",scope="Hand attribution unknown",misreadings="H omits the source number."),
]
notes = [
 dict(id="143_scan030-N1",text="The page continues a preceding discussion with an underlined isomorphisme and states that (2) is obtained by passage to the profinite. It inserts hom de before suites exactes and displays a two-row diagram labelled (4) at the left. The upper-left exception note lists g=0, nu=0,1,2 and circles only g=1,nu=0, followed by the author's question mark."),
 dict(id="143_scan030-N2",text="The diagram's first, second and last upper links are bare shafts; the middle map to Gamma and the other main map heads are pointed. Gamma curves down/right to the clipped Out term. The paired vertical left-map label, its cancelled right label, the last vertical tip and the clipped continuation after Out remain local doubts. A source X basepoint is present in the lower middle object even though both witnesses omitted it."),
 dict(id="143_scan030-N3",text="The crowded line below the diagram appears to begin admettons. A short arrow is written after completed T, independently of the doubtful predicate est invariant / injective. Its operator argument contains the author's literal question mark. The candidate keeps the crowded wording uncertain instead of repairing its grammar."),
 dict(id="143_scan030-N4",text="The first diagonal note is headed Version corrigée éventuelle and gives a normalizer formulation with additional automorphism, symmetric-group and local-structure conditions. The word locale has quotation marks plus a three-sided angular frame; a separate divider passes beneath the note near the final T indices. The frame and divider are not treated as cancellations. Crowded closing signs and autom remain uncertain."),
 dict(id="143_scan030-N5",text="The main paragraph asks that the arrow (1), described as the central vertical arrow of (5), be an iso. The source references (1) and (5) are retained although the displayed diagram is numbered (4). The consequence is called a caractérisation of Gamma. In the quotient, the underbrace begins around the low 1/following opening parenthesis and ends under the completed inner argument; it does not cover Autextlac or the denominator."),
 dict(id="143_scan030-N6",text="The second diagonal note lists exceptional (g,nu) and refers to pi_1 of an X with a genuine low Q-like index, followed by a partially reduced abelian-group phrase. A separate rectangle and zigzag cancel several lines; only their surviving fragments are transcribed, with physically illegible spans. The lower diagonal note cautions about g=0,nu=3 and adds commutation conditions with exterior operations of S_3."),
 dict(id="143_scan030-N7",text="The example retains the source spelling celà. Its final Autextlac expression has two opening round parentheses and only one closing parenthesis before the period; this incomplete punctuation is preserved. The lower diagram similarly lacks a separately visible closing set brace. These observations are source-graph decisions, not mathematical corrections."),
 dict(id="143_scan030-N8",text="Pencil footer 29 is included with unknown hand attribution. The ordinary/bold/blackboard rendering of Q or P is not treated as a new symbol. All physical lower indices, superscripts, bars, wedges and circle marks were inspected individually."),
]
check_events = [
 dict(statement_id="143_scan030-N1",type="carried as background without fault found",outcome="Visually collated the profinite statement and exact-sequence diagram; no independent proof or exactness check was attempted."),
 dict(statement_id="143_scan030-N3",type="carried as background without fault found",outcome="Recorded the uncertain source predicate and arrow without using a mathematical expectation to resolve their order."),
 dict(statement_id="143_scan030-N4",type="carried as background without fault found",outcome="Visually collated the normalizer and additional structural conditions. No normalizer theorem was proved or applied to choose letters."),
 dict(statement_id="143_scan030-N5",type="carried as background without fault found",outcome="Checked the physical formula references, argument, completion marks and underbrace placement; not an independent proof of the proposed characterization."),
 dict(statement_id="143_scan030-N6",type="carried as background without fault found",outcome="Read the exceptional cases and caution as source assertions. No classification of abelian fundamental groups or symmetric-group commutation theorem was used to reconstruct obscured text."),
 dict(statement_id="143_scan030-N7",type="carried as background without fault found",outcome="Counted the written delimiters and source punctures 0,1,infinity. Mathematical balancing of the displayed formula was intentionally not imposed."),
]

report = dict(key="143_scan030",reader="B",stage="first",image_views=["original","half1","half2"],
 changes=changes,decisions=decisions,inventory=inventory,remaining_doubts=remaining_doubts,
 certainty_resolutions=certainty_resolutions,notation=notation,abbreviations=abbreviations,
 hand_log=hand_log,notes=notes,check_events=check_events,
 unresolved_for_main=[dict(place=d["place"],reading=d["reading"],reason=d["reason"]) for d in remaining_doubts],
 raw_difference_disposition="All packet differences and all C/H agreements were visually checked against the original once and each native half once. Thirteen unique color-preserving crops were each successfully viewed once; a truncated first emission of the invariance crop was re-emitted and does not count as an inspection. No OCR, web research, TeX compilation, unassigned-page view, or audit was performed. Literal excerpts are asserted against the packet and candidate. Editorial H notes and pure macro/layout settings are not source text. Certainty-only changes are separate; ordinary/bold/blackboard Q/P and ordinary/calligraphic G rendering alone create no material rows. All original MARKS are kept in packet order; new doubts have no invented MARKS IDs.")

assert [d["id"] for d in decisions] == [m["id"] for m in pkt["marks"]]
for d in decisions:
    assert d["reading"] in candidate, ("decision reading",d)
for d in remaining_doubts:
    assert d["reading"] in candidate, ("doubt reading",d)
for r in certainty_resolutions:
    assert r["C"] in Csrc
    assert r["final"] in candidate
allowed = {"misread word","misread symbol or index","omission","text not on the page","deletion state","insertion or placement","abbreviation expanded or spelling modernised","readable ink left as \\ill{}","drawing or diagram","other"}
assert all(c["kind"] in allowed for c in changes)
assert all(Path(ROOT/c["crop"]).is_file() for c in changes if c["crop"]!="page")
assert len(boxes)==13
outtex=ROOT/"reviews/143_scan030_readerB.tex"
outjson=ROOT/"reviews/143_scan030_readerB.json"
outtex.write_text(candidate)
outjson.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
print(json.dumps({"tex":str(outtex),"json":str(outjson),"changes":len(changes),"marks":len(decisions),"inventory":len(inventory),"doubts":len(remaining_doubts),"crops":len(boxes)},ensure_ascii=False))
