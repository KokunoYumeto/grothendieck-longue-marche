import json
from pathlib import Path

root = Path("/workspace/scratch/8f839dff4bf0")
work = root / "SP74_C13_143+145_work"
packet = json.loads((root / "reader_packets/143_scan029.json").read_text())
candidate = (work / "reviews/143_scan029_readerA.tex").read_text()
key = "143_scan029"
boxes = {
    "opening_M": [410, 270, 590, 410],
    "deleted_un": [1080, 455, 1285, 545],
    "associated_clause": [540, 770, 1650, 1000],
    "first_formula": [315, 1000, 1645, 1205],
    "explanation": [310, 1170, 1630, 1515],
    "diagonal_margin": [15, 1490, 400, 2265],
    "second_formula": [385, 1925, 1655, 2045],
    "structure": [700, 2005, 1655, 2155],
    "stricts_orientes": [330, 2065, 705, 2190],
    "last_formula": [375, 2150, 1665, 2300],
}

def crop(name):
    return "page" if name == "page" else f"crops/{key}_A_{name}.png"

changes = []
def add(place, C, H, final, against_C, against_H, kind, ink,
        confidence="high", locus="page", marked=False, consequential=False):
    changes.append({
        "place": place, "C": C, "H": H, "final": final,
        "against_C": against_C, "against_H": against_H, "kind": kind,
        "ink": ink, "confidence": confidence, "crop": crop(locus),
        "box": boxes.get(locus), "marked_in_H": marked,
        "consequential": consequential,
    })

add("Heading: circled 9 and underlined title",
    r"\textcircled{9} \uline{Une conjecture arithmético-géométrique}",
    "[no witness]",
    r"\textcircled{9} \uline{Une conjecture} \uline{arithmético-géométrique}",
    False, True, "omission",
    "A tall 9 is enclosed by a drawn oval. Two rules run beneath Une conjecture and the compound title; the words between them are legible.")
add("Opening: des entiers",
    "des entiers", "deux entiers", "des entiers",
    False, True, "misread word",
    "The short word after the inequality has a looped d, a low continuation and final s; there is no x-shaped termination.")
add("Opening modular letter: M in surcharge over a prior graph",
    r"M_{g,\nu}",
    "le $M$ est écrit en surcharge sur une première lettre, qui semble être\nun $\\mathcal{T}$",
    r"\deleted{\unsure{\mathcal T}}M_{g,\nu}",
    True, False, "deletion state",
    "Black, heavy M strokes cover a thinner blue transverse cap and a curved lower return. The prior graph can be T-like, but its central stroke is covered; the candidate explicitly keeps that earlier-letter doubt.",
    "medium", "opening_M")
add("Interlinear sur Q",
    r"\inserted{sur $\mathbf Q$}", r"(sur $\mathbb{Q}$)",
    r"\inserted{sur $\mathbf Q$}",
    False, True, "insertion or placement",
    "sur Q sits above the modulaire/pour line and is attached by a hooked guide. No pair of enclosing textual parentheses is present at this opening occurrence.")
add("Interlinear relatives",
    r"\inserted{relatives}", "(relatives)", r"\inserted{relatives}",
    False, True, "insertion or placement",
    "relatives is written above lisses, with a curved attachment at the left of the lower word; the outer curve is an insertion guide.")
add("Underline on munies",
    r"\uline{munies}", "munies", r"\uline{munies}",
    False, True, "other",
    "A short straight rule lies immediately beneath munies, stopping before de.")
add("Deleted material after de and before nu-uple",
    r"de \deleted{\unsure{un}} $\nu$-uple",
    r"d'un $\nu$-uple",
    r"de \deleted{\unsure{un}} $\nu$-uple",
    False, True, "deletion state",
    "After the live de are two dark, crossed clusters before nu-uple. The underlying short reading un is still only provisional; the deletion itself is distinct from the live words.",
    "low", "deleted_un")
add("No ordonne between nu-uple and de",
    r"$\nu$-uple de $\nu$ sections",
    r"$\nu$-uple \uncertain{ordonné}" + "\n" + r"de $\nu$ sections",
    r"$\nu$-uple de $\nu$ sections",
    False, True, "text not on the page",
    "The first line ends with nu-uple and the next begins de nu sections. No additional word is written in that interval.",
    marked=True)
add("Disjoint sections: sur chaque fibre",
    "sur chaque fibre", "deux à deux fibre par fibre", "sur chaque fibre",
    False, True, "misread word",
    "The three written words have a short sur, a looped chaque with a descending q, and the tall f of fibre; there is no repeated deux or fibre.")
add("End of first paragraph: no distinct full stop after fibre",
    "fibre.", "fibre.", "fibre\n\nSauf",
    True, True, "text not on the page",
    "The final e continues into a short terminal stroke; the native half shows no detached point after that stroke before the new paragraph.",
    "medium")
add("Exception paragraph: associe, reduced a/colon, une",
    "associé à une étendue",
    r"\uncertain{associé} : \ill{} étendue",
    r"associé \unsure{à|:} une étendue",
    False, True, "readable ink left as \\ill{}",
    "associe has the sequence of separated short loops and an accented ending; une follows as a low continuous group. Between them are two very short vertically separated marks, allowing reduced a-with-grave or a colon. Preferred a is retained with the alternative, not asserted as certain.",
    "low", "associated_clause", True)
add("Exception paragraph: notion proche = schemable",
    r"\unsure{notion proche = schémable}",
    r"\ill{} $=$ \ill{}",
    r"\unsure{notion proche = schémable}",
    False, True, "readable ink left as \\ill{}",
    "The native half shows notion and a short proche-like group; the crop confirms two parallel bars and a long initial descending stroke followed by an -able-like ending. Several interior strokes remain compressed. The crop starts within proche, so the earlier words were judged from the native half.",
    "low", "associated_clause", True)
add("hom has no stop",
    "hom", "hom.", "hom",
    False, True, "abbreviation expanded or spelling modernised",
    "The m's final stroke is followed by a clear gap before naturel, without a separate dot.",
    locus="first_formula")
add("Deleted exterior abbreviation",
    r"\deleted{\unsure{extér.}}", r"\struck{extérieur}",
    r"\deleted{\unsure{extér.}}",
    False, True, "abbreviation expanded or spelling modernised",
    "The crossed word has a short exte-like body with a visible high accent and a final reduced stroke/point. Its length does not display the full sequence exterieur; the precise abbreviated ending remains covered.",
    "low", "first_formula")
add("First display label",
    r"\tag{1}", "(*)", r"\tag{1}",
    False, True, "misread symbol or index",
    "Inside the left parentheses a long upright stroke with a small upper hook remains visible through heavy retracing. The label is retained as 1; earlier underlying strokes are not separately recoverable.",
    "medium", "first_formula")
add("First display: overwritten modular capital",
    r"M_{g,\nu};\xi", r"M_{g,\nu;\xi}",
    r"\deleted{\unsure{\mathcal T}}M_{g,\nu};\xi",
    True, True, "deletion state",
    "The live M has the same strong pair of verticals and central valley as the opening M; a thinner cap and curved return remain visible behind it. This is recorded separately from the opening surcharge.",
    "medium", "first_formula")
add("First display: xi is the exterior basepoint, not an M subscript",
    r"M_{g,\nu};\xi", r"M_{g,\nu;\xi}", r"M_{g,\nu};\xi",
    False, True, "misread symbol or index",
    "g and nu sit low to the right of M. After their separator the looped xi rises to the height of M and descends past the subscript line; it is not a reduced third subscript.",
    locus="first_formula", consequential=True)
add("First display: lac stays on the operator baseline",
    r"\operatorname{Autextlac}^{\circ}",
    r"\mathrm{Autext}_{\mathrm{lac}}^{\circ}",
    r"\operatorname{Autextlac}^{\circ}",
    False, True, "insertion or placement",
    "The l of lac is tall and its a/c continue the same writing line as Autext. The one small ring is raised above the end of that line.",
    "medium", "first_formula")
add("First display: inner Pi/pi graph independently inspected",
    r"\pi_1(\overline X\setminus",
    r"\pi_1(\overline{X} \smallsetminus",
    r"\unsure{\Pi|\pi}_1(\overline X\setminus",
    True, True, "misread symbol or index",
    "The inner graph has a broad cap and two almost straight legs. Its right leg is straighter than the compact left-domain pi. Capital Pi is therefore preferred with explicit lower-case alternative; this alphabet identification is not counted as an established consequential correction.",
    "medium", "first_formula")
add("First display: puncture-list continuation and comma",
    r"x_1,\ldots,x_\nu", r"x_1, \ldots, x_\nu",
    r"x_1,\mathbin{-},x_\nu",
    True, True, "misread symbol or index",
    "Between the first and last x is one short continuous horizontal stroke, not separate dots. A low comma follows x_1 and another distinct low comma occurs after the stroke before the final x_nu.",
    "high", "first_formula")
add("Explanatory tuple: continuation stroke and no last comma",
    r"(X;x_1,\ldots,x_\nu)", r"(X; x_1, \ldots, x_\nu)",
    r"(X;x_1,\mathbin{-}x_\nu)",
    True, True, "misread symbol or index",
    "A comma follows the first x_1. The continuation is one thin horizontal stroke immediately before the last x; no separate comma is visible between that stroke and the final x_nu.",
    "high", "explanation")
add("Inserted sur Qbar belongs after correspondant",
    r"\inserted{(sur $\overline{\mathbf Q}$)}",
    r"(sur $\overline{\mathbb{Q}}$) $\to$ le pt" + "\n" + "correspondant",
    r"$\longrightarrow$ le pt correspondant \inserted{(sur $\overline{\mathbf Q}$)}",
    False, True, "insertion or placement",
    "The tuple is followed by a separate rightward arrow and le pt correspondant. The parenthesized sur Qbar is above the following gap, with a long hooked guide to the position just before de genre.",
    locus="explanation")
add("Genus glyph after de genre",
    r"\unsure{0|g}", r"de genre $g$",
    r"de genre $\unsure{g|0}$",
    True, False, "misread symbol or index",
    "The sloping oval has a small upper compartment or head attached above its long lower loop. That favors a looped g, but a retraced zero cannot be excluded; no mathematical expectation was used to settle it.",
    "low", "explanation", consequential=True)
add("avec nu pts marques associee a xi",
    r"avec $\nu$ pts marqués associée à $\xi$",
    r"avec" + "\n" + r"$\nu$ pts marqués associé à $\xi$",
    r"avec $\nu$ pts marqués associée à $\xi$",
    False, True, "misread word",
    "The sentence continues on the next main line with avec nu pts marques. After the accent in associee there is a separate low final e-like wave before a xi. The feminine ending is kept even though le pt preceded it.",
    locus="explanation")
add("Membership insertion attached to xi",
    r"\inserted{$\in M_{g,\nu}(\overline{\mathbf Q})$}",
    r"\ill{} $M_{g,\nu}(\overline{\mathbb{Q}})$ \ldots\ avec",
    r"\inserted{$\in M_{g,\nu}(\overline{\mathbf Q})$}",
    False, True, "insertion or placement",
    "A small epsilon-shaped membership sign precedes the raised M expression; a hooked guide descends after xi. g, comma and nu are below this M, and a short upper stroke is retained over the Q within its parentheses.",
    "medium", "explanation", True, True)
add("Deleted On before L'exposant",
    r"\deleted{\unsure{On}}", "[no witness]", r"\deleted{On}",
    False, True, "omission",
    "A rounded O-like loop and short n-like continuation are crossed by a heavier horizontal stroke immediately before the live capital L.",
    "medium", "explanation")
add("L'exposant begins a main sentence",
    "L'exposant", r"(\uncertain{l'exposant}", "L'exposant",
    False, True, "misread word",
    "The capital L and apostrophe stand after the deletion. The curved stroke to their left belongs to the membership insertion, not an opening parenthesis for the following sentence.",
    locus="explanation", marked=True)
add("Exposant sentence: marque le fait",
    "marque le fait", "indique", "marque le fait",
    False, True, "misread word",
    "The line contains a long marque group, the separate looped le, and a tall f crossed near its upper third in fait.")
add("Exposant sentence: prend les autom de",
    "qu'on prend les autom de", "qu'on\nse borne aux automorphismes du",
    "qu'on prend les autom de",
    False, True, "abbreviation expanded or spelling modernised",
    "prend begins with a long descending p, followed by les. The next line has the short autom group and de; there are no strokes for the expanded automorphismes.")
add("Exposant sentence: nonexchange condition",
    "qui n'échangent pas entre eux les classes",
    r"qui \ill{} les classes",
    "qui n'échangent pas entre eux les classes",
    False, True, "readable ink left as \\ill{}",
    "After qui, the line carries n'e with an apostrophe and accent, the long echangent body and pas entre; the next line starts eux les classes. The negative condition is written out.",
    marked=True, consequential=True)
add("Exposant sentence: de lacets associes",
    "de lacets associés aux", r"\uncertain{d'inertie} aux",
    "de lacets associés aux",
    False, True, "misread word",
    "A separate de precedes lacets, with a tall l and crossed t. The following associes has its own accented ending before aux.",
    marked=True, consequential=True)
add("Exposant sentence has no trailing explanatory parenthesis",
    r"aux $x_i$.", r"aux $x_i$ \ldots).", r"aux $x_i$.",
    False, True, "text not on the page",
    "The main line ends at the indexed x and a small terminal mark. No closing parenthesis or series of suspension points follows it; this row addresses those unsupported additions rather than settling the terminal mark's shape.")
add("Diagonal margin opening: peut-etre etre",
    "il faut peut-être être plus", r"il faut \ill{} \uncertain{plus strict}",
    "il faut peut-être être plus",
    False, True, "readable ink left as \\ill{}",
    "The rotated crop shows peut-etre on the first line after il faut, then a separate etre at the start of the next line before plus.",
    "medium", "diagonal_margin", True)
add("Diagonal margin: commutation and first colon",
    r"et exiger la commutation \unsure{:}",
    "et exiger la \\ill{} aux\n\\ill{} ---",
    "et exiger la commutation :",
    False, True, "readable ink left as \\ill{}",
    "The long commutation group has a crossed t and a dotted i near its end. At the start of the following short line there are two distinct vertically separated points; no aux or long dash is written.",
    "medium", "diagonal_margin", True)
add("Diagonal margin: des operations and second colon",
    r"des opérations \unsure{:}", r"des \ill{} \ill{}",
    "des opérations :",
    False, True, "readable ink left as \\ill{}",
    "des is followed by a long operations group, including the descending p and crossed t. Another pair of distinct points starts the next line.",
    "medium", "diagonal_margin", True)
add("Diagonal margin: definies",
    r"\unsure{définies}", "définition", "définies",
    False, True, "misread word",
    "The word has d, an accented e, a long descending f, dotted short strokes, and a low -ies ending; there is no second tall t to support definition.",
    "medium", "diagonal_margin")
add("Diagonal margin: S-like indexed graph and sur le",
    r"de $\mathfrak S_\nu$ sur le $\pi_1$",
    r"\ill{} $\pi_1$",
    r"de $\unsure{\mathfrak S_\nu}$ sur le $\pi_1$",
    False, True, "readable ink left as \\ill{}",
    "After de is a very large looped graph with an inner horizontal return and a small low nu at its right. The following sur le is legible before pi with a low 1. The graph is provisionally S-like but cannot be named confidently from its flourishes.",
    "low", "diagonal_margin", True, True)
add("Diagonal margin: instruction to examine a case",
    r"Il faut regarder surtout le cas $g=0,\nu=3$",
    r"?? \ldots\ $g = 0$," + "\n" + r"$\nu = 3$ \ldots",
    r"Il faut regarder surtout le cas $g=0,\nu=3$",
    False, True, "omission",
    "Following the two question marks are Il faut regarder, then surtout le cas on a fresh line, followed by the two written equalities.",
    "high", "diagonal_margin", True)
add("Diagonal margin: four suspension points",
    r"$g=0,\nu=3$\ldots", r"$\nu = 3$ \ldots",
    r"$g=0,\nu=3$....",
    True, True, "other",
    "Four separate dark points are visible below the final marginal line. The slanting stroke at its right belongs to the adjacent main-text capital, not a fifth punctuation sign.",
    "high", "diagonal_margin")
add("Introduction to second display",
    "Notons qu'on a aussi", r"\uncertain{Notations} \ill{}",
    "Notons qu'on a aussi",
    False, True, "readable ink left as \\ill{}",
    "The capital N is followed by the short -otons group, then qu'on, a and aussi as four separated word groups.",
    marked=True)
add("Second display label",
    r"\tag{2}", "(**)", r"\tag{2}",
    False, True, "misread symbol or index",
    "A curled upper stroke and heavy lower return form a retraced 2 at the left of this display; the surrounding parentheses are crowded into the same small area.",
    "medium", "second_formula")
add("Second display: exterior basepoint shape and placement",
    r"\overline M_{g,\nu};\unsure{\xi|j}",
    r"\overline{M}_{g,\nu;\xi}",
    r"\overline M_{g,\nu};\unsure{j|\xi}",
    True, True, "misread symbol or index",
    "The second basepoint is a tall, nearly straight, undotted stem with a small upper turn, not the two-loop xi in display (1). The native half also shows its lower leftward curve, partly beyond this crop's lower edge. Its height matches the main letters, while g and nu are reduced and lower.",
    "low", "second_formula", consequential=True)
add("Second display: operator baseline",
    r"\operatorname{Autextlac}^{\circ\circ}",
    r"\mathrm{Autext}_{\mathrm{lac}}^{\circ\circ}",
    r"\operatorname{Autextlac}^{\circ\circ}",
    False, True, "insertion or placement",
    "The tall l and low a/c are continuous on the Autext baseline. Two separate small rings are raised over the final letters.",
    "medium", "second_formula")
add("Second display: X is unbarred",
    r"X\setminus",
    r"\overline{X} \smallsetminus",
    r"X\setminus",
    False, True, "misread symbol or index",
    "The two oblique X strokes have clear empty space immediately above them. Unlike the first display's X, there is no upper bar here.",
    "high", "second_formula", consequential=True)
add("Second display: inner Pi/pi graph independently inspected",
    r"\pi_1(X\setminus",
    r"\pi_1(\overline{X} \smallsetminus",
    r"\unsure{\Pi|\pi}_1(X\setminus",
    True, True, "misread symbol or index",
    "This separate inner graph again has a wide cap and straight-legged capital-sized outline; an oblique retracing crosses its left leg. Capital Pi is preferred, but the covered leg prevents a settled case identification.",
    "medium", "second_formula")
add("Second display: puncture-list continuation and no last comma",
    r"x_1,\ldots,x_\nu", r"x_1, \ldots, x_\nu",
    r"x_1,\mathbin{-}x_\nu",
    True, True, "misread symbol or index",
    "There is one comma after x_1, then a single horizontal stroke. No separate low comma occurs between that stroke and the final x_nu.",
    "high", "second_formula")
add("Double-circle explanation: prend des autom",
    "qu'on prend des autom",
    r"qu'on se borne aux \ill{} \uncertain{pour des}" + "\n" + r"\ill{}",
    "qu'on prend des autom",
    False, True, "readable ink left as \\ill{}",
    "A long p-descender starts prend, then des and the short autom group occupy the remainder of the line.",
    "high", "structure", True)
add("Underlined stricts at the beginning of the continuation",
    r"\inserted{\uline{stricts}}",
    r"\uncertain{strictement}",
    r"\inserted{\uline{stricts}}",
    False, True, "misread word",
    "The short stricts word ends after its crossed t and low s; the rule is directly below it. No -ement sequence follows. It occupies the space before compatibles and is retained as the added qualification recorded by C.",
    "high", "stricts_orientes", True)
add("Continuation: compatibles avec la structure",
    "compatibles avec la structure",
    r"\ill{} \ldots\ \uncertain{strictement} \ill{}",
    "compatibles avec la structure",
    False, True, "readable ink left as \\ill{}",
    "The continuation has the long compatibles group with tall b/l strokes, then separate avec, la and structure, whose tall t strokes stand above the line.",
    "medium", "structure", True)
add("After structure: written colon and doubtful following word",
    r"structure \unsure{locale}",
    r"\ill{}",
    r"structure : \unsure{locale|lacets}",
    True, True, "omission",
    "Two distinct points stand between structure and the next word. That word begins with a high stroke, has several low connected letters, and a late high return; locale is retained first, but lacets is a visible alternative. The word is not settled by the Tate explanation.",
    "low", "structure", True)
add("Before induisant: i.e. and possible opening parenthesis",
    "i.e.", r"\ill{} induisant",
    r"\unsure{(i.e.|i.e.} induisant",
    True, True, "omission",
    "The short i.e. is visible at the beginning of the final explanatory line. A small left-facing curved stroke precedes its first dotted stem; it may be an opening parenthesis. No closing prose parenthesis is supplied beyond the written mathematical parenthesis.",
    "low", "structure", True)
add("End of Tate equality: suspension",
    r"$T=\operatorname{Tate}(\overline{\mathbf Q})$\ldots",
    r"$T = \mathrm{Tate}(\overline{\mathbb{Q}})$.",
    r"$T=\operatorname{Tate}(\overline{\mathbf Q})$\ldots",
    False, True, "other",
    "Small separated points continue after the closing mathematical parenthesis toward the right edge, rather than a single terminal point.",
    "medium", "structure")
add("Marginal Aut. orientes; rule belongs to stricts",
    r"\margin{Aut. \uline{\unsure{orientés}}}",
    "[no witness]",
    r"\margin{Aut. \unsure{orientés}}",
    True, True, "omission",
    "Aut. and the small following word are below and left of the main continuation. Only one horizontal rule is present: it lies between stricts and this small word, directly under stricts. There is no separate rule beneath orientes. The reduced letters still leave the word provisional.",
    "low", "stricts_orientes")
add("Third display label",
    r"\tag{2 bis}", "(***)", r"\tag{2 bis}",
    False, True, "misread symbol or index",
    "The label has an upper curved 2 and a lower compact bis-like continuation inside parentheses; it is not a row of three separated asterisks.",
    "medium", "last_formula")
add("Third display: analytic superscript on M",
    r"\unsure{M_{g,\nu}^{an}|\overline M_{g,\nu}}",
    r"M_{g,\nu;\xi}",
    r"M_{g,\nu}^{an}",
    False, True, "misread symbol or index",
    "Two small raised strokes stand to the upper right of M: a short a-like mark and a low n-shaped return. They are not a continuous line over M. The separate lower g, comma and nu remain visible.",
    "high", "last_formula", consequential=True)
add("Third display: basepoint independently inspected",
    r"\unsure{\xi|j}", r"M_{g,\nu;\xi}",
    r"M_{g,\nu}^{an};\unsure{j|\xi}",
    True, True, "misread symbol or index",
    "The third basepoint again has an undotted long stem, a short top turn and a bottom leftward hook, with no closed upper loop. It stands at full main-letter height after a semicolon; this physical occurrence is kept independently uncertain.",
    "low", "last_formula", consequential=True)
add("Third display: lac is not a subscript",
    r"\operatorname{Autextlac}^{\circ\circ}",
    r"\mathrm{Autext}_{\mathrm{lac}}^{\circ\circ}",
    r"\mathrm{Aut}\underbrace{\mathrm{extlac}^{\circ\circ}",
    False, True, "insertion or placement",
    "All the operator letters occupy the same baseline, including the tall l. The split of Aut/extlac in the candidate is solely the encoding of where the shorter physical underbrace starts.",
    "medium", "last_formula")
add("Third display: Pi versus pi before the final argument",
    r"\Pi_1", r"\pi_1(X \smallsetminus",
    r"\unsure{\Pi|\pi}_1",
    False, True, "misread symbol or index",
    "The heavily retraced graph has a wide horizontal cap and two almost straight legs, slightly larger and more upright than the left-hand pi. Capital Pi is preferred but the lower-case reading is explicitly retained because the left leg is overdrawn.",
    "medium", "last_formula")
add("Third display: puncture-list continuation and no last comma",
    r"x_1,\ldots,x_\nu", r"x_1, \ldots, x_\nu",
    r"x_1,\mathbin{-}x_\nu",
    True, True, "misread symbol or index",
    "The lower list has a comma after x_1 and a short single horizontal continuation stroke before the last x_nu. A second comma is not separately visible.",
    "high", "last_formula")
add("Third display: analytic superscript on X",
    r"\unsure{X^{an}|\overline X}", r"X \smallsetminus",
    r"X^{an}\setminus",
    False, True, "misread symbol or index",
    "Above and to the right of X are two separate short raised a/n strokes, with a gap between them. They do not form the broad centered bar visible on X in display (1).",
    "high", "last_formula", consequential=True)
add("Third display: underbrace's physical horizontal extent",
    r"\underbrace{\operatorname{Autextlac}^{\circ\circ}\Pi_1(\unsure{X^{an}|\overline X}\setminus\{x_1,\ldots,x_\nu\})}_{\deleted{\illegible{1}}=\mathcal T_{g,\nu}\ (\text{Teichmüller})}",
    r"\underbrace{\pi_1(X \smallsetminus \{x_1, \ldots, x_\nu\})}_{=\ \mathcal{T}_{g,\nu}\ (\text{Teichmüller})}",
    r"\mathrm{Aut}\underbrace{\mathrm{extlac}^{\circ\circ}\unsure{\Pi|\pi}_1(X^{an}\setminus\{}_{\overset{\deleted{\illegible{1}}}{=}\mathcal T_{g,\nu}\ (\text{Teichmüller})}x_1,\mathbin{-}x_\nu\})",
    True, True, "drawing or diagram",
    "The brace begins beneath the middle of Autextlac, approximately at ext, and turns upward near the opening set brace, before x_1. It therefore spans neither the entire right side nor the whole pi_1 argument as the witnesses typeset it. The candidate deliberately reproduces that shorter visible span without interpreting it as a mathematically distinct subgroup.",
    "medium", "last_formula")
add("Third display: crossed item lies on brace above equals",
    r"\deleted{\illegible{1}}=",
    "le signe\nsous l'accolade de $(***)$ est précédé d'un mot biffé illisible",
    r"\overset{\deleted{\illegible{1}}}{=}",
    True, True, "insertion or placement",
    "The crossed short item intersects the left portion of the brace, directly above the equals sign on the annotation line. Its individual letters are not recoverable. The fragment puts it over the equals rather than in a flat label sequence.",
    "medium", "last_formula")
add("Last line opening: dont on sait",
    "dont on sait (théorie top.)", "(théorie top.)",
    "dont on sait (théorie top.)",
    False, True, "omission",
    "The bottom line begins with the three written groups dont, on and sait before the parenthesized phrase; the first d is a round loop with a high return.")
add("Last line: que c'est un",
    "que c'est un", "qui induit un", "que c'est un",
    False, True, "misread word",
    "After the closing parenthesis are a descending q-group, then the compact c'est group with a high t, and the last un. The sentence remains unfinished at the page edge.")
add("Lower-left pencil number",
    r"\mspage{28}", "[no witness]", r"\mspage{28}",
    False, True, "omission",
    "Two pale pencil digits 2 and 8 sit at the lower left, distinct in weight from the ink text. Their writer is not identified on this page.")

decisions = []
def decide(mid, decision, reading, ink, confidence, locus):
    decisions.append({
        "id": mid, "decision": decision, "reading": reading, "ink": ink,
        "crop": crop(locus), "box": boxes.get(locus), "confidence": confidence,
    })

decide("M0716", "undecided", r"\unsure{notion proche = schémable}",
       "notion/proche are most plausible in the native half; the crop confirms the double bar and an -able-like ending but does not expose all interior strokes or the start of the phrase.", "low", "associated_clause")
decide("M0717", "first", r"$\longrightarrow$ le pt correspondant",
       "A separate shaft with a raised right-pointing tip follows the tuple, then le, a crossed pt abbreviation and the long correspondant group. No est la courbe is written.", "high", "explanation")
decide("M0718", "undecided", r"\unsure{g|0}",
       "A small upper compartment joins a long lower oval, favoring the looped g; the overtraced shape still permits zero. The preference is graphic, not supplied from genus convention.", "low", "explanation")
decide("M0719", "first", "strict",
       "After plus, the word has tall st strokes, a dotted short i and a crossed final t-like form, followed by a comma; its reduced middle is consistent with strict.", "medium", "diagonal_margin")
decide("M0720", "first", ":",
       "At the following marginal line's start are two detached, vertically aligned points with no connecting bowl. They are preserved literally as a colon.", "medium", "diagonal_margin")
decide("M0721", "first", ":",
       "A second pair of separate points starts the line before definies. Its shape is independently visible in the rotated crop.", "medium", "diagonal_margin")
decide("M0722", "first", "définies",
       "A looped d, accented short e, long f-descender and the low dotted -inies sequence can be followed; no second tall t appears.", "medium", "diagonal_margin")
decide("M0723", "undecided", r"\unsure{j|\xi}",
       "The second display's undotted stem and lower hook are j-like; they differ from the explicitly looped first xi. The simplified-xi possibility remains.", "low", "second_formula")
decide("M0724", "undecided", r"\unsure{locale|lacets}",
       "The high initial and late ascending return enclose a run of flattened letters. Both locale and lacets fit portions of those strokes; neither can be secured from the ink alone.", "low", "structure")
decide("M0725", "undecided", r"\unsure{orientés}",
       "The marginal group begins with an o-like point/loop and has reduced central strokes and a final accented-looking mark, but the entire letter sequence is not secure. The nearby rule belongs to stricts above.", "low", "stricts_orientes")
decide("M0726", "first", r"M_{g,\nu}^{an}",
       "The two short raised a/n strokes are right of M, while a true M bar would be centered; g and nu remain independently low.", "high", "last_formula")
decide("M0727", "undecided", r"\unsure{j|\xi}",
       "This separate basepoint has a long straight shaft, slight upper turn and a lower left hook, without the first display's closed loops. Preferred j remains uncertain.", "low", "last_formula")
decide("M0728", "first", r"X^{an}",
       "The raised marks are two separated a/n components to the upper right of X, not one broad stroke across its top.", "high", "last_formula")

inventory = []
def item(element, kind, position, words, hand="his hand"):
    inventory.append({
        "sheet_kind": "text", "hand": hand, "element": element,
        "kind": kind, "position": position,
        "first_words_or_objects": words, "transcribed": "yes",
    })
item("E01", "margin note", "top right, pencil", "15", "unnamed pencil hand")
item("E02", "text", "top, x190-1475 y45-155", "circled 9; Une conjecture arithmético-géométrique, two underline segments")
item("E03", "text", "upper paragraph, y215-655", "Soient g,nu >=0 des entiers ... sur chaque fibre")
item("E04", "deletion", "within opening modular letter, x430-500 y300-360", "prior T-like graph covered by live M; prior graph retained unsure")
item("E05", "insertion", "above modulaire/pour, x1130-1450 y250-350", "sur Q and hooked attachment")
item("E06", "insertion", "above lisses, x460-680 y375-450", "relatives and curved guide")
item("E07", "deletion", "between de and nu-uple, x1110-1250 y475-525", "crossed short clusters, unsure un")
item("E08", "text", "exception paragraph, y700-985", "Sauf pour g=0 ... notion proche = schémable")
item("E09", "text", "y1010-1095", "On a un hom naturel")
item("E10", "deletion", "after naturel, x1130-1300 y1015-1065", "crossed exterior abbreviation")
item("E11", "display", "first map, y1100-1210", "(1), pi_1(M;xi) arrow Autextlac circle pi_1(Xbar minus marked points)")
item("E12", "deletion", "first map M, x605-665 y1110-1170", "second physically separate overwritten prior capital")
item("E13", "text", "main explanatory paragraph, y1240-1785", "où (X;x_1,...,x_nu) arrow le pt correspondant ... aux x_i")
item("E14", "insertion", "above de genre, x1230-1530 y1170-1290", "(sur Qbar), with hooked guide")
item("E15", "insertion", "above/after associated xi, x1225-1520 y1270-1405", "in M_{g,nu}(Qbar), guide to xi")
item("E16", "deletion", "before L'exposant, x1350-1420 y1340-1380", "On crossed out")
item("E17", "margin note", "lower left, diagonal, x15-400 y1490-2265", "il faut peut-être ... g=0,nu=3; two colons, two question marks, four terminal dots")
item("E18", "text", "y1840-1910", "Notons qu'on a aussi")
item("E19", "display", "second map, y1930-2045 and basepoint descender below", "(2), Mbar with exterior doubtful basepoint; two operator circles; X without bar")
item("E20", "text", "y2020-2155", "où le double circle indique ... structure : doubtful locale/lacets ... Tate(Qbar)")
item("E21", "insertion", "left of compatibles, x485-660 y2080-2130", "stricts with its underline")
item("E22", "margin note", "x340-665 y2115-2170", "Aut. doubtful orientés; no separate underline below it")
item("E23", "display", "last map and annotation, y2165-2295", "(2 bis), M^{an}; doubtful j/xi, operator with two circles, doubtful Pi/pi, X^{an}, physically short underbrace, T_{g,nu} (Teichmüller)")
item("E24", "deletion", "on left part of last underbrace, about x1215-1270 y2220-2250", "one unreadable crossed item above equals")
item("E25", "text", "bottom line, y2295-2350", "dont on sait (théorie top.) que c'est un; sentence continues off-page")
item("E26", "margin note", "bottom left, pencil", "28", "unnamed pencil hand")

remaining = []
def doubt(place, reading, alternatives, reason, locus, confidence="low"):
    remaining.append({
        "place": place, "reading": reading, "alternatives": alternatives,
        "confidence": confidence, "reason": reason,
        "crop": crop(locus), "box": boxes.get(locus),
    })
doubt("Opening overwritten prior capital", r"\deleted{\unsure{\mathcal T}}M",
      "T-like prior graph; another covered letter remains possible",
      "The black replacement M obscures the thin blue middle of the older graph; the visible cap/return support but do not settle T.", "opening_M")
doubt("Deleted word before nu-uple", r"\deleted{\unsure{un}}",
      "un, or unreadable short deletion; the two clusters may contain more than one word",
      "Crossing and overwriting cover the internal connections. No second crop was made.", "deleted_un")
doubt("Reduced sign after associe", r"\unsure{à|:}", "à or :",
      "Two separated small marks permit either a severely reduced accented a or literal colon.", "associated_clause")
doubt("Exception paragraph's final phrase", r"\unsure{notion proche = schémable}",
      "notion proche = schémable; uncertain interior letters",
      "The phrase is plausible from the native half, but the long final word's central strokes remain compressed; the existing crop begins within proche.", "associated_clause")
doubt("Crossed exterior abbreviation", r"\deleted{\unsure{extér.}}",
      "extér. or another short exté- abbreviation",
      "The cancellation crosses the abbreviation's ending, so the last letter and final point remain provisional.", "first_formula")
doubt("First display overwritten capital", r"\deleted{\unsure{\mathcal T}}M",
      "T-like prior graph, or indeterminate covered graph",
      "The second surcharge was inspected separately; cap/return fragments survive but are partly covered.", "first_formula")
doubt("First display inner Pi case", r"\unsure{\Pi|\pi}_1", "capital Pi or lower-case pi",
      "Broad cap and nearly straight legs favor capital Pi, but a handwriting-size distinction alone does not settle the alphabet.", "first_formula", "medium")
doubt("Genus glyph", r"\unsure{g|0}", "g or 0",
      "A tiny upper compartment favors g, but the enlarged lower oval can still be read as a retraced zero.", "explanation")
doubt("Diagonal margin's large indexed group graph", r"\unsure{\mathfrak S_\nu}",
      "S-like capital, possibly another highly flourished capital; low nu is visible",
      "The large outside loop and inside return do not securely name the alphabet. The expected group is not used to settle it.", "diagonal_margin")
doubt("Second display basepoint", r"\unsure{j|\xi}", "j or simplified xi",
      "The long undotted stem lacks the first xi's upper loops; full lower hook was seen in the native half.", "second_formula")
doubt("Second display inner Pi case", r"\unsure{\Pi|\pi}_1", "capital Pi or lower-case pi",
      "The inner two-legged graph is broad and upright, but oblique retracing obscures its left-leg shape.", "second_formula", "medium")
doubt("Word after structure colon", r"\unsure{locale|lacets}", "locale or lacets",
      "Flattened interior letters and the late rising stroke permit both readings.", "structure")
doubt("Possible prose parenthesis before i.e.", r"\unsure{(i.e.|i.e.}", "(i.e. or i.e.",
      "A separate leading curved stroke is visible but may belong to the compressed abbreviation. No closing parenthesis is invented.", "structure")
doubt("Marginal word following Aut.", r"\unsure{orientés}", "orientés, or a compressed related form",
      "Only the beginning and reduced accented ending are fairly apparent; the central sequence remains insecure.", "stricts_orientes")
doubt("Third display basepoint", r"\unsure{j|\xi}", "j or simplified xi",
      "This separate stem has the same broad j-like outline but is retained as its own unresolved physical occurrence.", "last_formula")
doubt("Third display Pi case", r"\unsure{\Pi|\pi}_1", "capital Pi or lower-case pi",
      "The two nearly straight legs favor Pi, but overtracing obscures the left leg's original curvature.", "last_formula", "medium")

certainty = [
    {"place": "Tuple continuation", "C": r"\unsure{$\longrightarrow$ le pt correspondant|est la courbe}", "final": r"$\longrightarrow$ le pt correspondant", "ink": "Shaft and right-pointing tip, followed by le pt correspondant, are visible."},
    {"place": "Deleted On", "C": r"\deleted{\unsure{On}}", "final": r"\deleted{On}", "ink": "O loop and n continuation remain under the crossing stroke."},
    {"place": "Diagonal strict", "C": r"\unsure{strict}", "final": "strict", "ink": "The dotted and crossed short word follows plus and precedes a comma."},
    {"place": "Diagonal first colon", "C": r"\unsure{:}", "final": ":", "ink": "Two detached vertically arranged points."},
    {"place": "Diagonal second colon", "C": r"\unsure{:}", "final": ":", "ink": "A separately inspected second pair of points before definies."},
    {"place": "Diagonal definies", "C": r"\unsure{définies}", "final": "définies", "ink": "Long f-descender and dotted short strokes with the reduced -ies ending."},
    {"place": "Diagonal S-like graph: confidence lowered", "C": r"\mathfrak S_\nu", "final": r"\unsure{\mathfrak S_\nu}", "ink": "The large looping outline is genuine but its alphabet name is not secure."},
    {"place": "Structure word: alternative added without changing preferred C reading", "C": r"\unsure{locale}", "final": r"\unsure{locale|lacets}", "ink": "Late high return also permits a t-like component."},
    {"place": "Third M superscript", "C": r"\unsure{M_{g,\nu}^{an}|\overline M_{g,\nu}}", "final": r"M_{g,\nu}^{an}", "ink": "Two separate small upper-right strokes, not a centered bar."},
    {"place": "Third X superscript", "C": r"\unsure{X^{an}|\overline X}", "final": r"X^{an}", "ink": "Distinct raised a/n components to the right of X."},
    {"place": "Third Pi: confidence lowered", "C": r"\Pi_1", "final": r"\unsure{\Pi|\pi}_1", "ink": "The cap and straight legs favor capital Pi, but left-leg overtracing leaves case uncertain."},
]

# These are physical occurrences, not deductions from repeated notation.
index_checks = []
def idx(place, form, evidence, confidence="high", locus="page"):
    index_checks.append({"place": place, "form": form, "evidence": evidence,
                         "confidence": confidence, "crop": crop(locus), "box": boxes.get(locus)})
idx("Opening M: first lower index", "g", "Lower hooked g, physically below the live M.", locus="opening_M")
idx("Opening M: second lower index", r"\nu", "Small curved nu after a low comma; independent of g.", locus="opening_M")
idx("Map (1): left pi index", "1", "A short separate downstroke lies low and right of pi.", locus="first_formula")
idx("Map (1): M first index", "g", "Hooked descending g is visibly low.", locus="first_formula")
idx("Map (1): M second index", r"\nu", "Curved nu follows the low comma.", locus="first_formula")
idx("Map (1): exterior basepoint", r"\xi", "Full-height upper and lower loops after the semicolon.", locus="first_formula")
idx("Map (1): Autextlac exponent", r"\circ", "One raised open ring.", locus="first_formula")
idx("Map (1): inner fundamental-group graph", r"\unsure{\Pi|\pi}", "Broad cap and nearly straight legs; case retained uncertain independently of the other maps.", "medium", "first_formula")
idx("Map (1): right pi index", "1", "Low short upright to the right of the right-hand pi.", locus="first_formula")
idx("Map (1): X upper mark", r"\overline X", "A centered horizontal upper mark, heavily retraced.", locus="first_formula")
idx("Map (1): first marked-point index", "1", "Short low 1 under first x.", locus="first_formula")
idx("Map (1): last marked-point index", r"\nu", "Curved low nu under last x; dark but separately visible.", confidence="medium", locus="first_formula")
idx("Explanatory tuple: first x index", "1", "Short lower upright after first x.", locus="explanation")
idx("Explanatory tuple: final x index", r"\nu", "Reduced final curved index attached to last x.", confidence="medium", locus="explanation")
idx("Interlinear sur Q: upper field mark", r"\overline{\mathbf Q}", "Short horizontal stroke centered above Q.", locus="explanation")
idx("Explanatory line: genus glyph", r"\unsure{g|0}", "Small upper compartment above sloping lower oval.", "low", "explanation")
idx("Explanatory line: associated basepoint", r"\xi", "Two-loop tall graph after reduced accented a.", locus="explanation")
idx("Membership insertion: first M index", "g", "Low hooked g beneath the inserted capital.", locus="explanation")
idx("Membership insertion: second M index", r"\nu", "Low curved nu after comma.", locus="explanation")
idx("Membership insertion: field upper mark", r"\overline{\mathbf Q}", "Short upper stroke retained above Q, distinct from its oval; close to the preceding line.", "medium", "explanation")
idx("L'exposant sentence: standalone circle", r"\circ", "One open small ring on the prose baseline.")
idx("L'exposant sentence: pi index", "1", "Separate short low 1 after pi.")
idx("L'exposant sentence: final x index", "i", "Small lower i with its own point at the end of the prose line.")
idx("Diagonal margin: large graph's index", r"\nu", "Small low nu at right of the large looped capital.", "medium", "diagonal_margin")
idx("Diagonal margin: pi index", "1", "Separate low upright at right of pi.", locus="diagonal_margin")
idx("Map (2): left pi index", "1", "Low short stroke separately visible.", locus="second_formula")
idx("Map (2): M upper mark", r"\overline M", "Single continuous centered bar above M.", locus="second_formula")
idx("Map (2): M first index", "g", "Low hooked g after the capital.", locus="second_formula")
idx("Map (2): M second index", r"\nu", "Small curved nu after the comma.", locus="second_formula")
idx("Map (2): basepoint", r"\unsure{j|\xi}", "Full-height undotted stem, lower hook in native half; not reduced to M-subscript height.", "low", "second_formula")
idx("Map (2): first operator exponent", r"\circ", "First distinct small raised ring.", locus="second_formula")
idx("Map (2): second operator exponent", r"\circ", "Second distinct small raised ring immediately to its right.", locus="second_formula")
idx("Map (2): inner fundamental-group graph", r"\unsure{\Pi|\pi}", "Broad cap and upright legs with oblique overtracing on the left; separately uncertain.", "medium", "second_formula")
idx("Map (2): right pi index", "1", "Low short stroke independent of the retraced pi graph.", locus="second_formula")
idx("Map (2): X upper space", "X", "No overbar or raised letter in the clear space above X.", locus="second_formula")
idx("Map (2): first marked-point index", "1", "Low upright after the first point symbol.", locus="second_formula")
idx("Map (2): last marked-point index", r"\nu", "Low curved final nu.", "medium", "second_formula")
idx("Double-circle prose: circle", r"\circ", "One quoted small circle after double, not numeric zero.")
idx("Tate equality: field upper mark", r"\overline{\mathbf Q}", "Separate bar over the enclosed Q.", locus="structure")
idx("Map (2 bis): left pi index", "1", "Separate low upright after the compact left pi.", locus="last_formula")
idx("Map (2 bis): M first lower index", "g", "Long low hooked g.", locus="last_formula")
idx("Map (2 bis): M second lower index", r"\nu", "Small curved nu after low comma.", locus="last_formula")
idx("Map (2 bis): M exponent first letter", "a", "Short detached raised mark right of M.", locus="last_formula")
idx("Map (2 bis): M exponent second letter", "n", "Small raised low arch following that mark.", locus="last_formula")
idx("Map (2 bis): basepoint", r"\unsure{j|\xi}", "Tall undotted hooked stem independently inspected after the semicolon.", "low", "last_formula")
idx("Map (2 bis): first operator circle", r"\circ", "Small open ring above final operator letters.", locus="last_formula")
idx("Map (2 bis): second operator circle", r"\circ", "Second separate open ring to the right.", locus="last_formula")
idx("Map (2 bis): right fundamental-group symbol", r"\unsure{\Pi|\pi}", "Wide cap and nearly straight legs; retraced left leg leaves case open.", "medium", "last_formula")
idx("Map (2 bis): right group index", "1", "One low upright to the right of that graph.", locus="last_formula")
idx("Map (2 bis): X exponent first letter", "a", "Short raised mark above the upper-right arm of X.", locus="last_formula")
idx("Map (2 bis): X exponent second letter", "n", "Separate small upper arch further right.", locus="last_formula")
idx("Map (2 bis): first marked-point index", "1", "Short low upright following the first x-like point.", locus="last_formula")
idx("Map (2 bis): last marked-point index", r"\nu", "Small curved low nu after final x; near right edge.", "medium", "last_formula")
idx("Underbrace T: first index", "g", "Low hooked g beneath the large curved capital.", locus="last_formula")
idx("Underbrace T: second index", r"\nu", "Small curved nu following the low comma.", locus="last_formula")

raw_actions = [
    "Scan metadata 29 is C apparatus, not an extra ink number; pencil 15 is inventoried without accepting H's author attribution.",
    "Circled 9 and both underlined title portions are supplied; H's editorial attribution is excluded.",
    "Both witnesses encode the visible inequality (geq/geqslant); macro-only raw mismatch excluded.",
    "des, not deux, retained from the short written ending.",
    "Opening sur Q is an interlinear insertion with a hooked guide, not an opening prose parenthesis.",
    "Same sur Q insertion: no closing textual parenthesis at this occurrence.",
    "relatives is interlinear; the curved guide is not a textual opening parenthesis.",
    "No textual closing parenthesis after the interlinear relatives.",
    "Live de followed by crossed material retained; underlying un remains unsure.",
    "H's ordonne has no ink at the end of nu-uple or start of the next line.",
    "sur chaque fibre retained; H's repeated deux/fibre wording rejected.",
    "H's editor note is not copied as source prose; both insertion states and the opening surcharge are accounted for explicitly.",
    "associe and une recovered; preferred reduced a retains colon alternative.",
    "notion proche remains part of one explicitly doubtful phrase.",
    "schemable remains part of that doubtful phrase; literal double bar retained.",
    "No detached stop after hom.",
    "Short crossed exterior abbreviation retained unsure; not expanded to exterieur.",
    "First left label retained as retraced 1 rather than star.",
    "Autextlac has one baseline; lac is not subscripted.",
    "Same physical first label; mathematical tag syntax is rendering only.",
    "Parenthesized sur Qbar is inserted after correspondant with a visible attachment.",
    "Visible arrow/le pt correspondant selected; est la courbe has no corresponding strokes.",
    "Genus remains doubtful, with graphic preference g over 0 explicitly reversed from C's order.",
    "avec nu pts marques associee a xi is main-line text; membership is a separate insertion.",
    "Membership placement, feminine associee, crossed On and following capital L are separately recorded.",
    "marque le fait is read, not indique.",
    "prend les autom de is literal; expanded automorphismes is excluded.",
    "n'echangent pas entre eux is recovered from the line and continuation.",
    "de lacets associes replaces d'inertie.",
    "No enclosing prose parenthesis after x_i.",
    "Diagonal note is independently inventoried and recovered, then Notons qu'on a aussi in the main text; order in H is not treated as proof of placement.",
    "Second label retained as 2 rather than two stars.",
    "Second basepoint physically j-like; explicit xi alternative remains.",
    "Second Autextlac is one baseline; two circles separately inspected.",
    "Same physical second label.",
    "qu'on prend des autom recovered from short written words.",
    "stricts, compatibles avec la structure, literal colon, doubtful locale/lacets and i.e. trace each recorded; no strictement expansion.",
    "Marginal Aut. recovered with its visible final point.",
    "Small marginal orientes remains unsure; no extra underline is invented under it.",
    "Third label retained as 2 bis rather than three stars.",
    "M's two raised an components selected over an overbar; lower g and nu separately checked.",
    "Third basepoint independently remains j/xi, at full height outside M's subscript.",
    "Third Autextlac remains on one baseline; split in TeX only locates the partial underbrace.",
    "H's backslash-comma is spacing syntax, not manuscript punctuation; excluded.",
    "X's raised an components selected; Pi/pi case separately remains uncertain.",
    "Crossed unreadable item retained in its higher position on/near the brace above equals; the 1 in illegible{1} is an apparatus count.",
    "Same physical label 2 bis.",
    "dont on sait recovered at the start of the last line.",
    "que c'est un retained, not qui induit un; continuation left incomplete.",
    "Pencil 28 separately inventoried; H's moved diagonal note is treated at its actual marginal position, not as bottom main text.",
]

report = {
    "key": key, "reader": "A", "stage": "first",
    "image_views": ["original", "half1", "half2"] + [crop(k) for k in boxes],
    "changes": changes, "decisions": decisions, "inventory": inventory,
    "remaining_doubts": remaining, "certainty_resolutions": certainty,
    "notation": [
        {"form": r"M_{g,\nu}", "meaning": "Live modular-topos notation on this page", "evidence": "Opening and first-display M overwrite thinner prior graphs; second M is barred, third has an. Those separate states are retained."},
        {"form": r"\mathcal T_{g,\nu}", "meaning": "Name written beneath the last brace beside Teichmüller", "evidence": "Large curved capital with a looped cap and lower return, followed by low g, comma, nu. Retained under the shared modular-topos T convention; not automatically changed to the object-set tau."},
        {"form": r"X,\overline X,X^{an}", "meaning": "Curve letters as physically marked on this page", "evidence": "Plain crossed X in tuple and second map, centered bar in first map, two raised an strokes in last map. These X forms lack the full ornate looped shape required for mathfrak X."},
        {"form": r"\xi;\ \unsure{j|\xi}", "meaning": "Basepoint graphs", "evidence": "First display and explanatory prose have looped xi; second and third displays have separately inspected tall undotted stems with hooks."},
        {"form": r"\operatorname{Autextlac}^{\circ},\operatorname{Autextlac}^{\circ\circ}", "meaning": "Literal right-side operator lettering and circle exponents", "evidence": "lac stays on the operator baseline in all three occurrences; exponent counts are one, two and two."},
        {"form": r"\unsure{\mathfrak S_\nu}", "meaning": "Large indexed graph in diagonal note, identification unresolved", "evidence": "Large outer loop and inner horizontal return with a distinct low nu; not named by expectation about a permutation group."},
    ],
    "abbreviations": [
        {"form": "hom", "expansion": "homomorphisme; no expansion or added stop in transcription"},
        {"form": "pt", "expansion": "point; written abbreviation retained"},
        {"form": "pts", "expansion": "points; written plural abbreviation retained"},
        {"form": "autom", "expansion": "automorphismes; written short form retained"},
        {"form": "Aut.", "expansion": "automorphismes, probable; source capitalization and point retained"},
        {"form": "extér.", "expansion": "extérieur, provisional reading of the crossed abbreviation"},
        {"form": "i.e.", "expansion": "id est; preceding curved mark remains unsure"},
        {"form": "top.", "expansion": "topologique; written point retained"},
        {"form": "an", "expansion": "analytique; the two raised letter components are not replaced by a bar"},
    ],
    "hand_log": [
        {"habit": "Thin earlier modular graph with heavy replacement M", "places": "Opening M and M in display (1)", "scope": "Both physical surcharges inspected separately", "misreadings": "Prior letter remains explicitly unsure; no T is inferred solely from the modular role."},
        {"habit": "Plain versus looped X", "places": "First-map Xbar, explanatory tuple X, second-map X, last-map Xan", "scope": "All four capital X occurrences inspected", "misreadings": "No automatic mathfrak conversion; every upper mark separately recorded."},
        {"habit": "Full-height basepoint versus low genus/marking indices", "places": "All three displayed domains and inserted membership expression", "scope": "Every g, nu and basepoint occurrence individually checked in physical_indices", "misreadings": "H groups the basepoint inside the M subscript; source basepoints rise to main-letter height."},
        {"habit": "Looped xi versus undotted straight hooked stem", "places": "Display (1), prose xi, displays (2) and (2 bis)", "scope": "Each occurrence inspected independently", "misreadings": "Later j-like graphs remain unsure instead of normalized to the earlier xi."},
        {"habit": "Same-baseline operator tail lac", "places": "All three Autextlac expressions", "scope": "All occurrences inspected", "misreadings": "H subscript lac is not supported by a low/reduced placement in the handwriting."},
        {"habit": "Inner Pi/pi graphs differ in outline from compact domain pi", "places": "Inner graph in (1), inner graph in (2), and graph in (2 bis)", "scope": "All three separately retained as preferred capital Pi with lower-case alternative", "misreadings": "C/H lowercase agreement in the first two maps is not automatically accepted; no case doubt is called a settled consequential mathematical correction."},
        {"habit": "Single continuation stroke and varying list commas", "places": "First puncture list, explanatory tuple, second puncture list, third puncture list", "scope": "All four lists inspected individually", "misreadings": "All four have a single horizontal stroke rather than discrete dots. Only the first map has a separate comma between that stroke and the last x_nu; the other three do not."},
        {"habit": "Distinct bars, two-letter superscripts and small circles", "places": "Xbar in (1), Mbar in (2), Man and Xan in (2 bis), Qbar insertions/equality, all operator circles", "scope": "Every physical upper mark inspected; exponent counts listed separately", "misreadings": "Neither analytic pair is read as an overbar; circles are not zero."},
        {"habit": "Reduced accented a may look like a colon", "places": "After associe in exception paragraph; two separate diagonal colons; colon after structure", "scope": "Each local shape inspected", "misreadings": "Only the associe sign retains a/colon alternatives; the two marginal pairs and structure pair are preserved literally as points."},
        {"habit": "Single rule between stacked words", "places": "stricts above small marginal orientes", "scope": "One local rule inspected in crop", "misreadings": "The same line is not duplicated into an underline beneath both words."},
        {"habit": "Short physical underbrace and overwritten annotation", "places": "Display (2 bis)", "scope": "Brace endpoints, central cusp, crossed item and lower equals/T label inspected in one crop", "misreadings": "Source extent retained even though it does not cover an entire conventional expression."},
        {"habit": "Pencil pagination without identifying signature", "places": "15 top right; 28 bottom left", "scope": "Both numbers inspected in page/halves", "misreadings": "No identification of the pencil hand as the author is inferred from H's note."},
    ],
    "notes": [
        {"id": f"{key}-N1", "text": "The page is headed 'Une conjecture arithmético-géométrique', circled 9. It introduces a modular topos for relative smooth proper connected curves of genus g with marked disjoint sections, and lists the displayed small (g,nu) exceptions. The phrase 'notion proche = schémable' remains a reading doubt. The live source grammar de [crossed item] nu-uple is retained without repair."},
        {"id": f"{key}-N2", "text": "It writes a natural homomorphism with a single circle on Autextlac and explains that the automorphisms do not exchange the classes of loops associated with the marked points. The tuple is followed by an arrow and le pt correspondant; the source's associee ending and the uncertain genus glyph are not reconciled mathematically."},
        {"id": f"{key}-N3", "text": "The diagonal note asks whether one should be stricter and require commutation with written operations; it contains two literal colon-like point pairs, a large unresolved S-like indexed graph, two question marks, and a request to examine g=0,nu=3, ending with four points. Its wording is transcribed as a marginal query, not a proved condition."},
        {"id": f"{key}-N4", "text": "The second and third maps carry double circles. The following prose adds underlined stricts, a doubtful locale/lacets word and the identity on T=Tate(Qbar). The third map has analytic an superscripts and a short physical underbrace annotated by T_{g,nu} (Teichmüller). Its final claim begins 'dont on sait (théorie top.) que c'est un' and remains unfinished on this page."},
        {"id": f"{key}-N5", "text": "Reader encoding decisions are literal: later basepoints remain j/xi, all three inner group graphs remain preferred Pi with pi alternatives, bars and an pairs are separate, the underbrace spans only the written middle portion, and no missing matching prose parenthesis or continuation is supplied. Each puncture list has a single horizontal continuation stroke; only the first map has a comma before its last x_nu. The overwritten prior modular capitals remain doubtful T-like graphs."},
    ],
    "check_events": [
        {"statement_id": f"{key}-N1", "type": "carried as background without fault found", "outcome": "Source definition and listed exceptions were read for transcription only. No proof or classification check was performed, and no expected genus value selected the doubtful ink."},
        {"statement_id": f"{key}-N2", "type": "carried as background without fault found", "outcome": "The written map and automorphism condition were inspected as ink. No construction or proof of the map was used to repair its notation."},
        {"statement_id": f"{key}-N3", "type": "carried as background without fault found", "outcome": "The marginal question was transcribed without checking the proposed commutation condition or identifying its group by expectation."},
        {"statement_id": f"{key}-N4", "type": "carried as background without fault found", "outcome": "The Tate and Teichmuller statements were not proved or computationally checked. Physical superscripts and brace geometry were retained without mathematical normalization."},
    ],
    "unresolved_for_main": [
        {"place": x["place"], "reading": x["reading"], "crop": x["crop"], "box": x["box"], "question": x["reason"]}
        for x in remaining
    ] + [
        {"place": "Third underbrace geometry", "reading": "Starts under extlac and ends near opening set brace; crossed item above equals", "crop": crop("last_formula"), "box": boxes["last_formula"], "question": "Please review the deliberately partial brace span and the vertical annotation placement. The candidate does not expand it to cover the entire expression."}
    ],
    "raw_difference_disposition": "All 50 packet differences were checked against the original/native halves and the relevant one-pass crops. Each has a packet-order disposition in raw_difference_checks. Agreements were also read, and extra source differences (overwriting, basepoint height, three inner Pi/pi doubts, four literal continuation strokes and their individual commas, the unbarred second X, short brace extent, a shared underline, the structure colon and four marginal dots) are recorded. Macro-only field fonts, geq/geqslant, setminus/smallsetminus, spacing and apparatus counts are excluded from substantive rows.",
    "raw_difference_checks": [{"number": n + 1, "disposition": text} for n, text in enumerate(raw_actions)],
    "physical_indices": index_checks,
    "workflow": {
        "original_views": 1, "native_half_views": {"half1": 1, "half2": 1},
        "crop_method": "One original-image crop per open locus, LANCZOS enlargement, autocontrast, UnsharpMask. Diagonal note rotated -45 degrees before enlargement. No recrop, OCR, external research or TeX compilation.",
        "crop_rotations_degrees": {name: (-45 if name == "diagonal_margin" else 0) for name in boxes},
        "notation_read": "Current shared notation.md reread after root's update through scan027; the modular T convention is kept distinct from object-set tau.",
    },
}

allowed = {
    "misread word", "misread symbol or index", "omission", "text not on the page",
    "deletion state", "insertion or placement", "abbreviation expanded or spelling modernised",
    "readable ink left as \\ill{}", "drawing or diagram", "other",
}
for n, row in enumerate(changes, 1):
    assert row["C"] == "[no witness]" or row["C"] in packet["witness_C"], (n, "C", row["place"], row["C"])
    assert row["H"] == "[no witness]" or row["H"] in packet["witness_H"], (n, "H", row["place"], row["H"])
    assert row["final"] in candidate, (n, "final", row["place"], row["final"])
    assert row["kind"] in allowed
    assert row["against_C"] or row["against_H"], (n, "certainty-only row")
assert [r["id"] for r in decisions] == [r["id"] for r in packet["marks"]]
for row in decisions:
    assert row["reading"] in candidate
assert len(raw_actions) == len(packet["differences"]) == 50
for row in certainty:
    assert row["C"] in packet["witness_C"], ("certainty C", row)
    assert row["final"] in candidate, ("certainty final", row)
path = work / "reviews/143_scan029_readerA.json"
path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"path": str(path), "changes": len(changes), "marks": len(decisions),
                  "inventory": len(inventory), "doubts": len(remaining),
                  "physical_indices": len(index_checks), "raw_differences": len(raw_actions)}, ensure_ascii=False))
