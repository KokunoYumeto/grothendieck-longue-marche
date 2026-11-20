import json
from pathlib import Path

base = Path(__file__).resolve().parent
out = base.parents[2]
manifest = json.loads((base / "crop_manifest.json").read_text())
for item in manifest:
    item["inspected"] = True
(base / "crop_manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
crop_index = {int(x["id"].split("_")[0]): x for x in manifest}

findings = []

def add(place, c, h, final, evidence, confidence, kind, marked_in_H, diff_c,
        diff_h, bbox, crop_n=None, doubt_action="", math_note=""):
    findings.append({
        "id": f"R3-006-{len(findings)+1:02d}",
        "place": place, "c": c, "h": h, "final": final,
        "evidence": evidence, "confidence": confidence, "kind": kind,
        "marked_in_H": marked_in_H, "diff_c": diff_c, "diff_h": diff_h,
        "bbox": bbox,
        "crop": f"readings/scan006/R3/crops/{crop_index[crop_n]['id']}.png" if crop_n else "",
        "doubt_action": doubt_action, "s_id": "", "math_note": math_note
    })

add("Opening, H after sous-groupes",
    r"\inserted{$H$}", "$H$", r"\inserted{$H$}",
    "Settled on the first half: H is raised above the baseline, with its curved insertion stroke entering between sous-groupes and de.",
    "high", "insertion or placement", False, False, True, [1019,36,1147,139])
add("Opening, punctuation after the quotient parenthesis",
    ").....", ")…", ").....",
    "Settled on the first half: five separated small baseline points follow the closing parenthesis. H reduces their count to an ellipsis.",
    "high", "other", False, False, True, [660,143,803,222])
add("Heading tail after the colon",
    r"\deleted{\unsure{Ch.|En.}}", "déf.",
    r"\deleted{\unsure{Ch.|En.}}",
    "The crossed short abbreviation has a low loop, a tall right stem and a terminal point. The crossing still prevents a secure first-letter reading; no secure déf. can be recovered.",
    "low", "deletion state (struck given live or live given struck)", False, False, True,
    [1066,300,1158,350], 1, "retain")
add("Underlined proposition label",
    r"\uline{Prop}", r"\emph{Prop.}", r"\uline{Prop}",
    "Settled on the first half: the label has its underline but no separate abbreviation point after the final letter.",
    "medium", "other", False, False, True, [407,378,525,451])
add("Immediately after Soit",
    r"Soit\deleted{\unsure{s|x}}", "Soit",
    r"Soit\deleted{\unsure{s|x}}",
    "A separate small crossed terminal shape remains after the t of Soit. Its small bowl and superposed crossing do not decide s against x.",
    "low", "omission", False, False, True, [589,380,696,441], 2, "retain")
add("Raised cancelled adjective between contour and connexe",
    r"\deleted{\unsure{strict}}", r"\struck{\ill{}}",
    r"\inserted{\deleted{\unsure{strict}}}",
    "Two tall stems and an i-point survive, but the central letters are covered. The word is above the line and has a connector descending to the gap after contour; both its addition and its cancellation are retained.",
    "medium", "insertion or placement", True, True, True, [1331,340,1457,429], 3, "retain")
add("Left-margin pentagon, supplied H redraw",
    r"\draw ... (128,244)--(121,239)--(128,259) ... (376,243)--(391,252)--(388,242); \fill (201,366) ...",
    r"H_drawings/01-2.tex: \node[pt] at (74,-38), (82,-64), (46,-85), (33,-62)",
    "Pentagon with the visible angular corner strokes, heavier lower-right edge, short lower stroke and detached lower dot, as represented in C's TikZ.",
    "The crop shows angular directed-looking strokes at the left and right corners, a small angular top-right stroke and detached lower ink. H turns these into four uniform vertex dots. C's existing geometry already retains the substantive marks; coordinate and weight refinements are not counted.",
    "high", "drawing or diagram", False, False, True, [180,520,471,805], 21)
add("a), replacement of initial Un",
    r"a) \deleted{Un}\inserted{Soit $g$ un} autom. $g$ de $X$",
    r"a) Soit \struck{Un} $g$ un autom.\ $g$ de $X$.",
    r"a) \deleted{Un}\inserted{Soit $g$ un} autom. $g$ de $X$",
    "Settled on the first half: Soit g un is the raised replacement above the crossed Un; the second g on the original baseline remains live. There is no separate point immediately after X.",
    "high", "insertion or placement", False, False, True, [406,440,1123,535],
    math_note="The duplicate g is preserved; it has not been silently removed to improve the sentence.")
add("a), est dit direct and Conditions équiv.",
    r"\deleted{est dit \uline{\unsure{direct}}.}\inserted{Conditions équiv.}",
    r"\emph{Conditions équiv.} \struck{\ill{}} :",
    r"\deleted{est dit \uline{\unsure{direct}}.}\inserted{Conditions équiv.}",
    "The baseline est dit is readable; direct is partly obscured and remains doubtful, with a separate lower underline and terminal point. Conditions équiv. is above the cancellation, not independently underlined. H's final colon is not supported by separate ink.",
    "medium", r"readable ink left as \ill{}", True, False, True, [1137,438,1626,532], 4, "retain")
add("Separate d'orientation below the initial a) sentence",
    r"\deleted{\uline{d'orientation}}",
    "H note: « d'orientation » souligné deux fois; live continuation of the statement",
    r"\unsure{\uuline{d'orientation}|\deleted{\uline{d'orientation}}}",
    "Two sloping rules are visible. The upper rule starts below d'ori and rises into the latter letters; the lower rule stays below. The crop does not securely distinguish two underlines from an underline plus cancellation. Both states are explicitly retained, with the live double underline first.",
    "low", "deletion state (struck given live or live given struck)", False, True, True,
    [511,550,774,617], 5, "retain")
add("1 degree), short deleted word",
    r"\deleted{\unsure{si}}", r"\struck{\ill{}}", r"\deleted{si}",
    "The crop separates the s-shaped first stroke and the detached point of i from the heavier horizontal cancellation.",
    "high", r"readable ink left as \ill{}", True, True, True, [875,560,934,596], 6, "resolve")
add("2 degree), after A",
    r"\forall a\in A\quad ga", r"\forall a \in A, ga", r"\forall a\in A\quad ga",
    "Settled on the first half: a blank gap separates A and ga; there is no detached comma in that gap.",
    "high", "other", False, False, True, [985,626,1267,701])
add("Cancelled curled sign beside the second condition",
    r"\deleted{\unsure{$\{$|$f$}}", r"\struck{\ill{}}",
    r"\deleted{\unsure{$\{$|$f$}}",
    "A long curved spine survives beneath several smaller crossing loops. It still allows an opening brace or f; the ink is kept as a sign rather than discarded.",
    "low", "misread symbol or index", True, False, True, [540,646,590,722], 7, "retain")
add("Cancelled short marker immediately before On dit",
    r"\deleted{\unsure{b)|Si}}", r"\uncertain{Déf.}",
    r"\deleted{\unsure{Déf.|Def.|b)|Si}}",
    "The mark has a low medial loop, a long descending final stroke and a separate point at the right, permitting Déf./Def. as well as the C alternatives. The heavy diagonal crossing is secure; H's live state is not.",
    "low", "deletion state (struck given live or live given struck)", True, True, True,
    [455,741,530,810], 8, "retain")
add("Definition after une",
    r"\deleted{\unsure{autom.} d'}\uline{orientation}",
    r"\struck{\ill{}}\emph{d'orientation}",
    r"\deleted{\unsure{autom.}} d'\uline{orientation}",
    "The horizontal cancellation covers the compressed autom. and stops before the plainly formed d'. The d' is live; the lower underline begins under orientation, not under d'. The crossed word retains its doubt.",
    "high", "deletion state (struck given live or live given struck)", True, True, True,
    [1240,729,1657,797], 9, "retain",
    "The resulting une d'orientation is retained despite its grammatical awkwardness.")
add("b), first occurrence of the orientation-set letter",
    r"\unsure{\omega|w}(X)", r"\omega(X)", r"\omega(X)",
    "The crop shows two rounded bowls with inward-curving upper ends and a short central rise. This occurrence is read as omega rather than an angular Latin w.",
    "high", "misread symbol or index", False, True, False, [664,830,796,885], 10, "resolve")
add("b), subset inclusion and Aut(X)",
    r"\inserted{$\subset\operatorname{Aut}(X)$}", r"\subset \operatorname{Aut}(X)",
    r"\inserted{$\subset\operatorname{Aut}(X)$}",
    "Settled on the first half: the inclusion and group name sit above the baseline, with a long insertion connector opening after omega(X). H gives the words without the insertion state.",
    "high", "insertion or placement", False, False, True, [793,780,1034,884])
add("b), abbreviation l'ens",
    "l'ens des", r"l'ens.\ des", "l'ens des",
    "The crop shows the end of ens without a separate point. The detached point farther right is after des, not after ens.",
    "high", "abbreviation expanded or spelling modernised", False, False, True, [849,827,979,879], 11)
add("b), detached point after des",
    "des", "des", r"des\unsure{.}",
    "A small detached round point is level with the end of des. Its brownish appearance and small size leave punctuation versus a surface/stray mark unsettled; it is explicitly marked as doubtful rather than silently ignored or asserted.",
    "low", "omission", False, True, True, [996,828,1104,882], 11, "retain")
add("b), deleted prefix before orientation(s)",
    r"\deleted{autom. d'}", r"\struck{\ill{}}d'orientation",
    r"\deleted{\unsure{autom.} d'}",
    "The crossing continues across the d-shaped loop before orientation, so d' belongs to the deletion here, unlike the preceding definition. The heavily covered autom. is plausible but not fully visible, and gains a doubt mark.",
    "medium", "deletion state (struck given live or live given struck)", True, True, True,
    [1091,825,1414,877], 12, "retain")
add("b), orientation(s) ending",
    "orientations", "d'orientation", r"\unsure{orientation|orientations}",
    "The last letters run into one long low exit ending in a hook. The crop does not separate a final plural s. Singular is placed first from the visible exit, with plural retained; no grammatical correction decides it.",
    "low", "misread word", False, True, True, [1390,830,1597,884], 12, "retain")
add("b), inverse sentence in the interline",
    r"Si $g\in\omega(X)$, on a $g^{-1}\in\omega(X)$.",
    r"et si $g\in\omega(X)$, on a $g^{-1}\in\omega(X)$, $\omega(X)=\{g,g^{-1}\}$; note: $g^{-1}\in\omega(X)$ added",
    r"\inserted{Si $g\in\omega(X)$, on a $g^{-1}\in\omega(X)$.}",
    "The entire small sentence starts with Si and ends in a point above Alors. It is transcribed in that interlinear position before Alors. H merges it into the later et si clause and narrows the insertion to the last formula. C's words/order are retained, with the interlinear state added.",
    "high", "insertion or placement", False, True, True, [430,879,943,932], 13)
add("b), punctuation after card omega(X)=2",
    r"\unsure{;|,}", ",", r"\unsure{;|,}",
    "The small mark has a dark lower stroke and an adjacent upper component, but their overlap does not securely decide semicolon against comma.",
    "low", "other", False, False, True, [956,945,990,985], 14, "retain")
add("b), deleted et si clause",
    r"\deleted{et si $g\in\unsure{\omega|\omega(X)}$}", r"\struck{\ill{}}",
    r"\deleted{et si $g\in\unsure{\omega|\omega(X)}$}",
    "et si and the g stem remain readable beneath the horizontal deletion. The rightmost part is too heavily crossed to decide whether (X) followed omega.",
    "low", r"readable ink left as \ill{}", True, False, True, [1016,928,1527,980], 14, "retain")
add("b), c before the cardinality in the added qualification",
    r"\unsure{c|(}=\operatorname{card}S\ne2", r"\operatorname{card} S \neq 2",
    r"\unsure{c|(}=\operatorname{card}S\ne2",
    "There is an open curved sign followed by a distinct equals sign before card S. The curve still permits c or an opening parenthesis; H omits both the curve and equals sign.",
    "medium", "omission", False, False, True, [1241,876,1484,926], 14, "retain",
    "The c at the opening of the page does not settle this local glyph.")
add("b), attachment point of strictness qualification",
    r"\inserted{(si $X$ est strict i.e. si $\unsure{c|(}=\operatorname{card}S\ne2$)} after card omega(X)=2",
    r"de $X$ (si $X$ est strict i.e.\ si $\operatorname{card} S \neq 2$). Alors ...",
    r"card omega(X)=2 [deleted clause] \inserted{(si X est strict i.e. si c=card S ne 2)}, et si ...",
    "The long curved connector drops from the interlinear parenthesis to the position after the 2 of card omega(X)=2. It does not attach the parenthesis to the preceding de X, as H's running text does.",
    "high", "insertion or placement", False, False, True, [925,876,1603,1001], 14)
add("Cancelled c), subgroup abbreviation",
    "le ss-grpe de", "le s-groupe de", "le ss-grpe de",
    "The cancelled line has two short s strokes before the hyphen and the compressed grpe spelling; H expands and changes that abbreviation.",
    "high", "abbreviation expanded or spelling modernised", False, False, True, [1140,1045,1516,1110], 15)
add("Cancelled c), formé and g membership clause",
    r"formé par les $g\in\operatorname{Aut}X$",
    r"\ill{} par les \ill{} $\operatorname{Aut} X$",
    r"formé par les $g\in\operatorname{Aut}X$",
    "The second cancelled line retains formé, par les, the descending g, the membership sign and Aut X. Crossing strokes do not prevent those readings.",
    "high", r"readable ink left as \ill{}", True, False, True, [399,1108,849,1177], 15)
add("Cancelled c), abbreviated triv ending",
    r"\unsure{triv$^{\mathrm{lt}}$|triv$^{\mathrm{t}}$}", "trivialement",
    r"\unsure{triv$^{\mathrm{lt}}$|triv$^{\mathrm{t}}$}",
    "The baseline triv is followed by a raised looping ending. Cancellation strokes still prevent deciding lt against t; the full word trivialement is not written.",
    "low", "abbreviation expanded or spelling modernised", False, False, True,
    [905,1173,1083,1228], 15, "retain")
add("Cancelled c), terminal bracket",
    "[i.e.", "[i.e.]", "[i.e.",
    "The opening square bracket and i.e. are visible. At the right the enclosing cancellation stroke turns upward; there is no separate closing square bracket.",
    "high", "text not on the page", False, False, True, [1439,1178,1577,1235], 15)
add("Considérons, relation between automorphism groups",
    r"\unsure{-|\to}", r"\to", r"\unsure{-|\to}",
    "The short horizontal shaft has a thick, slightly forked right end. It does not show two unambiguous arrowhead wings; dash/weak right-arrow alternatives remain.",
    "low", "misread symbol or index", False, False, True, [1067,1252,1138,1291], 16, "retain",
    "The later word hom makes a map plausible but was not used to promote the mark to an arrow.")
add("Considérons, formula layout",
    r"Considérons $\operatorname{Aut}(X)...$.",
    r"Considérons \[ \operatorname{Aut}(X)... \]",
    r"Considérons $\operatorname{Aut}(X)\unsure{-|\to}\operatorname{Aut}(\omega(X))\simeq\mathbb{Z}/2\mathbb{Z}$.",
    "Settled on the second half: Considérons and the group expression occupy one baseline. H separates that formula into a display.",
    "high", "insertion or placement", False, False, True, [452,1239,1630,1303])
add("Surjectivity sentence, abbreviation hom",
    "un hom surjectif", r"un homom.\ surjectif", "un hom surjectif",
    "Settled on the second half: one tall h and the short remaining strokes give hom, without om repetition or an abbreviation point.",
    "high", "abbreviation expanded or spelling modernised", False, False, True, [704,1322,840,1383])
add("Index-two sentence, subgroup abbreviation",
    "un ss-grpe d'indice", "un s-groupe d'indice", "un ss-grpe d'indice",
    "Settled on the second half: two short initial s strokes and grpe are written. H's s-groupe expands and changes the form.",
    "high", "abbreviation expanded or spelling modernised", False, False, True, [887,1408,1126,1475])
add("After engendré par",
    r"\unsure{tt|tout}", r"\uncertain{tt}", "tt",
    "The crop shows only two joined tall t strokes, with no separate o and u bodies. C's doubt is resolved to the abbreviation tt; removal of H's uncertainty with the same reading is not counted as a substantive H difference.",
    "high", "abbreviation expanded or spelling modernised", True, True, False, [829,1604,880,1661], 17, "resolve")
add("Corollary, side-by-side baseline layout",
    r"\uline{Corollaire} $\operatorname{Aut}(X)\simeq...$, où $H$ est ...",
    r"\emph{Corollaire} \[ \operatorname{Aut}(X)\simeq... \quad\text{(...),} \] où $H$ ...",
    r"\uline{Corollaire} $\operatorname{Aut}(X)\simeq\mathbb{Z}/2\mathbb{Z}\cdot\mathbb{Z}/H$ ... , où $H$ est ...",
    "Settled on the second half: the underlined Corollaire, the group expression and the beginning où H est share one baseline. The gloss alone sits above it.",
    "high", "insertion or placement", False, False, True, [320,1729,1616,1832])
add("Corollary, inserted gloss",
    r"\inserted{(produit $\frac{1}{2}$ direct):}",
    "(produits ½ directs),",
    r"\inserted{(\unsure{produit|produits} $\frac{1}{2}$ direct):}",
    "The ending of produit is compressed enough to retain singular/plural alternatives. Direct ends in a clear tall t with no subsequent s. Two detached vertically placed points after the closing parenthesis give a colon. The curved connector places the whole gloss after the group product.",
    "medium", "insertion or placement", False, True, True, [1231,1676,1612,1803], 18, "retain",
    "The slash-stacked half and C's fraction are equivalent LaTeX representations; no difference is counted for that alone.")
add("Corollary, H est",
    "où $H$ est", r"où $H$ $\to$", "où $H$ est",
    "The reduced est has the same long low body and turned-up final t as other est occurrences on this page. It belongs to the sentence; H treats the cursive word as an arrow.",
    "medium", "misread word", False, False, True, [1437,1736,1585,1790], 18)
add("Corollary, final subgroup abbreviation",
    "le ss-grpe de", "le ss-groupe de", "le ss-grpe de",
    "Settled on the second half: the compressed spelling is grpe, not the expanded groupe.",
    "high", "abbreviation expanded or spelling modernised", False, False, True, [361,1873,677,1955])
add("Final parenthesis, word after g",
    r"\unsure{étant|étans|etant}", "dans",
    r"\unsure{etant|étant|etans|étans|dans}",
    "The crop shows a small initial curve rising into one tall stem and a low terminal loop. It neither secures a detached acute nor a final t. The same initial shape can also be read as the d of dans. No-accent etant is placed first; the other visible alternatives remain.",
    "low", "misread word", False, True, True, [444,1980,549,2031], 19, "retain")
add("Final adjective",
    r"\unsure{fixé|fixée}", "fixée", "fixé",
    "The crop shows f-i-x and one final e bearing the acute; there is no independent following e before the closing parenthesis.",
    "high", "misread word", False, True, True, [1041,1948,1170,2031], 20, "resolve",
    "The written masculine-looking ending is retained after une orientation; agreement has not been corrected.")

inventory = []
def inv(element, kind, position, first, hand="his hand"):
    inventory.append({"sheet_kind":"text", "hand":hand, "element":element,
                      "kind":kind, "position":position,
                      "first_words_or_objects":first, "transcribed":"yes"})

inv("Opening continuation", "text", "top, x 260–1651, y 52–220",
    "Ils correspondent aux sous-groupes ... (c=card Z/H).....")
inv("Inserted subgroup name", "insertion", "top line, x 1050–1136, y 39–134", "H")
inv("Underlined subject heading", "text", "x 313–1016, y 289–364", "Orientation d'un contour")
inv("Cancelled heading tail", "deletion", "x 1066–1158, y 300–350", "Ch.|En.")
inv("Proposition statement", "text", "x 405–1648, y 376–450", "Prop Soit X=(S,A,R) un contour ...")
inv("Cancelled terminal letter after Soit", "deletion", "x 661–695, y 398–439", "s|x")
inv("Raised strict with connector", "insertion", "x 1331–1457, y 340–429", "strict")
inv("Cancellation of raised strict", "deletion", "x 1331–1444, y 344–380", "strict")
inv("Two-edge lens with two black endpoint dots", "drawing", "left margin, x 67–199, y 418–565",
    "two curved edges and two filled endpoints")
inv("Pentagon with angular strokes and detached lower ink", "drawing", "left margin, x 180–471, y 520–805",
    "five sides, corner strokes, heavy lower-right side, short lower stroke and dot")
inv("Part a initial sentence and rewrite", "text", "x 407–1631, y 438–536",
    "a) ... autom. g de X")
inv("Initial Un cancellation", "deletion", "x 488–573, y 477–519", "Un")
inv("Raised replacement of Un", "insertion", "x 444–652, y 439–496", "Soit g un")
inv("Cancelled old predicate", "deletion", "x 1137–1626, y 476–532",
    "est dit direct.")
inv("Replacement condition label", "insertion", "x 1150–1516, y 437–489",
    "Conditions équiv.")
inv("Separate d'orientation and two sloping rules", "text", "x 511–774, y 550–617",
    "d'orientation; double underline versus underline plus deletion remains open")
inv("First equivalence condition", "display", "x 788–1588, y 546–620",
    "1 degree) ... forall s in S, s est lié à gs")
inv("Deleted si", "deletion", "x 875–934, y 560–596", "si")
inv("Second equivalence condition", "display", "x 789–1562, y 629–704",
    "2 degree) forall a in A ga est lié à a")
inv("Cancelled curled sign beside conditions", "deletion", "x 540–590, y 646–722", "opening brace|f")
inv("Cancelled marker before definition", "deletion", "x 455–530, y 741–810", "Déf.|Def.|b)|Si")
inv("Definition sentence", "text", "x 596–1657, y 725–822",
    "On dit que g est une ... d'orientation de X.")
inv("Cancelled word in definition", "deletion", "x 1240–1444, y 738–781", "autom.")
inv("Part b first line", "text", "x 393–1663, y 826–891",
    "b) Soit omega(X) l'ens des ... orientation(s) de X")
inv("Inserted inclusion in part b", "insertion", "x 793–1034, y 780–884",
    "subset Aut(X)")
inv("Deleted prefix in b", "deletion", "x 1091–1414, y 825–877", "autom. d'")
inv("Small inverse sentence", "insertion", "x 430–943, y 879–932",
    "Si g in omega(X), on a g^-1 in omega(X).")
inv("Cardinality and pair conclusion", "text", "x 422–1603, y 933–1041",
    "Alors card omega(X)=2 ... et si g in omega(X), on a omega(X)={g,g^-1}.")
inv("Cancelled old qualification", "deletion", "x 1016–1527, y 928–980", "et si g in omega|(omega(X))")
inv("Inserted strictness qualification and curved connector", "insertion", "x 925–1603, y 876–1001",
    "(si X est strict i.e. si c|(=card S ne 2)")
inv("Part c cancelled first formulation", "deletion", "x 357–1646, y 1040–1235",
    "c) Soit Aut+(X) subset Aut(X) le ss-grpe ... [i.e.")
inv("Replacement map sentence", "text", "x 452–1630, y 1239–1303",
    "Considérons Aut(X) -|to Aut(omega(X)) simeq Z/2Z.")
inv("Surjectivity and index statement", "text", "x 401–1582, y 1320–1475",
    "C'est un hom surjectif, i.e. le noyau Aut+(X) est un ss-grpe d'indice 2.")
inv("Cyclic generation statement", "text", "x 418–1593, y 1502–1675",
    "De plus, Aut+(X) est un groupe cyclique engendré par tt g in omega(X).")
inv("Underlined corollary and quotient expression", "text", "x 320–1616, y 1729–1832",
    "Corollaire Aut(X) simeq Z/2Z dot Z/H, où H est ...")
inv("Semidirect-product gloss with curved insertion connector", "insertion",
    "x 1231–1612, y 1676–1803", "(produit|produits 1/2 direct):")
inv("Description of subgroup H", "text", "x 361–1638, y 1840–1955",
    "le ss-grpe de Z formé des n in Z tels que g^n=1")
inv("Final parenthesis", "text", "x 354–1171, y 1948–2090",
    "(g etant|étant|etans|étans|dans une orientation fixé)")
inv("Archive foliation, retained only as comment", "margin note",
    "lower-left corner, x 39–76, y 2274–2319", "5", "unnamed hand")

notation = [
    {"sign":"Z", "reading":r"\mathbb{Z}", "ink":"Double diagonal/cross-stroke forms, including the small quotient denominators; H's declared bold encoding is equivalent.", "place":"opening, map sentence and corollary"},
    {"sign":"H, g", "reading":r"H,\ g,\ g^n", "ink":"H has two upright strokes and a crossbar; g has a pronounced curved descender. The exponent n is raised in the last equation.", "place":"opening and final two lines"},
    {"sign":"omega", "reading":r"\omega", "ink":"First occurrence has two rounded, inward-curving bowls; later occurrences can flatten into one low wave.", "place":"part b, first occurrence and repetitions"},
    {"sign":"1 degree, 2 degree", "reading":r"1^{\circ}),\ 2^{\circ})", "ink":"Small raised circular marks, followed by long closing parentheses.", "place":"two conditions in a)"},
    {"sign":"inverse exponent", "reading":r"g^{-1}", "ink":"Short raised horizontal minus followed by an upright one.", "place":"interlinear inverse sentence and pair formula"},
    {"sign":"Aut plus", "reading":r"\operatorname{Aut}^{+}(X)", "ink":"A small raised cross is above or immediately after the final t.", "place":"cancelled c), index sentence and cyclic-generation sentence"},
    {"sign":"nonemptiness", "reading":r"\ne\varnothing", "ink":"Inequality strokes followed by a slashed oval; no set cardinality is supplied.", "place":"end of proposition statement"},
    {"sign":"group-expression separator", "reading":r"\unsure{-|\to}", "ink":"Horizontal stroke with a slightly forked, thick right end, not enough to fix an arrowhead.", "place":"Considérons"},
    {"sign":"half and centered product dot", "reading":r"\frac{1}{2},\ \cdot", "ink":"A slash-stacked 1 and 2 in the gloss; a small separated centered dot between the quotients.", "place":"corollary"},
    {"sign":"equivalence", "reading":r"\simeq", "ink":"Short upper wave above a separate straight lower stroke.", "place":"map sentence and corollary"}
]
abbreviations = [
    {"written":"Prop", "expansion":"Proposition"},
    {"written":"autom.", "expansion":"automorphisme"},
    {"written":"équiv.", "expansion":"équivalentes"},
    {"written":"ens", "expansion":"ensemble"},
    {"written":"ss-grpe", "expansion":"sous-groupe"},
    {"written":"hom", "expansion":"homomorphisme"},
    {"written":"tt", "expansion":"tout"},
    {"written":"i.e.", "expansion":"id est"},
    {"written":"card", "expansion":"cardinal"},
    {"written":"triv with raised lt|t", "expansion":"trivialement (expansion only in this note; raised ending remains uncertain)"}
]

unresolved = [
    {"place":"Heading tail", "reading":r"\deleted{\unsure{Ch.|En.}}", "alternatives":"Ch.; En.", "confidence":"low"},
    {"place":"After Soit", "reading":r"\deleted{\unsure{s|x}}", "alternatives":"s; x", "confidence":"low"},
    {"place":"Raised cancelled adjective", "reading":r"\inserted{\deleted{\unsure{strict}}}", "alternatives":"strict; central letters obscured", "confidence":"medium"},
    {"place":"Cancelled old predicate", "reading":r"\deleted{est dit \uline{\unsure{direct}}.}", "alternatives":"direct; middle letters obscured", "confidence":"medium"},
    {"place":"Separate d'orientation", "reading":r"\unsure{\uuline{d'orientation}|\deleted{\uline{d'orientation}}}", "alternatives":"live, double underlined; cancelled, singly underlined", "confidence":"low"},
    {"place":"Curled sign beside second condition", "reading":r"\deleted{\unsure{$\{$|$f$}}", "alternatives":"opening brace; f", "confidence":"low"},
    {"place":"Cancelled marker before On dit", "reading":r"\deleted{\unsure{Déf.|Def.|b)|Si}}", "alternatives":"Déf.; Def.; b); Si", "confidence":"low"},
    {"place":"Definition after une", "reading":r"\deleted{\unsure{autom.}}", "alternatives":"autom.; body of word partly covered", "confidence":"medium"},
    {"place":"Point after des in b)", "reading":r"des\unsure{.}", "alternatives":"punctuation point; surface or stray mark", "confidence":"low"},
    {"place":"Deleted prefix in b)", "reading":r"\deleted{\unsure{autom.} d'}", "alternatives":"autom.; body of word partly covered", "confidence":"medium"},
    {"place":"b), orientation ending", "reading":r"\unsure{orientation|orientations}", "alternatives":"orientation; orientations", "confidence":"low"},
    {"place":"After card omega(X)=2", "reading":r"\unsure{;|,}", "alternatives":"semicolon; comma", "confidence":"low"},
    {"place":"Deleted et si clause", "reading":r"\unsure{\omega|\omega(X)}", "alternatives":"omega; omega(X)", "confidence":"low"},
    {"place":"Strictness qualification before equals", "reading":r"\unsure{c|(}", "alternatives":"c; opening parenthesis", "confidence":"medium"},
    {"place":"Cancelled c), triv ending", "reading":r"\unsure{triv$^{\mathrm{lt}}$|triv$^{\mathrm{t}}$}", "alternatives":"triv with raised lt; triv with raised t", "confidence":"low"},
    {"place":"Considérons relation", "reading":r"\unsure{-|\to}", "alternatives":"dash; weak right arrow", "confidence":"low"},
    {"place":"Inserted corollary gloss", "reading":r"\unsure{produit|produits}", "alternatives":"produit; produits", "confidence":"medium"},
    {"place":"Final word after g", "reading":r"\unsure{etant|étant|etans|étans|dans}", "alternatives":"etant; étant; etans; étans; dans", "confidence":"low"}
]

report = {
    "scan":"006", "reader":"R3",
    "start_utc":"2026-11-20T00:00:02Z",
    "end_utc":"PENDING",
    "images_viewed":[
        "/workspace/scratch/be39e9f81d6d/source/SP38_CW_75_scans/J75-01_75_scan006.jpg",
        "/workspace/scratch/be39e9f81d6d/source/SP38_CW_75_scans/J75-01_75_scan006_a.jpg",
        "/workspace/scratch/be39e9f81d6d/source/SP38_CW_75_scans/J75-01_75_scan006_b.jpg"
    ],
    "reading_file":"/workspace/scratch/be39e9f81d6d/out/readings/scan006/R3/reading.tex",
    "crop_count":21,
    "findings":findings,
    "inventory":inventory,
    "notation":notation,
    "abbreviations":abbreviations,
    "notes":[
        "Independent ink reading of scan 006 only. Original whole-image dimensions are 1690 by 2358 pixels. The whole page was viewed once for layout, then top half a once, then bottom half b once, in that order. Each half is 1690 by 1259 pixels; reported boxes are in original whole-image coordinates.",
        "The page continues a statement about proper subgroups of Z, then has the underlined heading Orientation d'un contour, one proposition with parts a), b), c), and one underlined Corollaire. There are two drawings in the left margin and no object-and-arrow diagram. No date or author's manuscript page number appears. The lower-left 5 is archive foliation and is only a TeX comment.",
        "The drawings were compared with H_drawings/01-2.tex. H's lens is substantively present and is not counted as an omission. For the pentagon, the original angular strokes and detached ink must not be replaced by uniform vertex dots.",
        "The proposition and corollary are claims read from the ink, not globally proved here. The duplicate g in a), the live d' in une d'orientation, the uncertain weak map separator, and the ending fixé are retained without grammatical or mathematical correction.",
        "No secure explicit question mark or verbal authorial doubt was observed. The editorial unsure marks in reading.tex describe this reader's uncertainty, not a claimed authorial query.",
        "There are no S rows: S.json is the empty array. All supplied C doubt loci have a finding with resolve or retain, including the retained alternatives. Added or removed C doubt marks count as diff_c.",
        "marked_in_H is true where H supplied an uncertainty/illegibility marker for the corresponding locus; ordinary struck-state markup alone is not treated as a doubt flag. H's page marker and declared bold number-field encoding are not collation differences.",
        "Twenty-one distinct enhanced crops were made, all with original bounding boxes and rotation 0 in crop_manifest.json. All were visually inspected. No crop was remade. The standalone curled-sign crop is intentionally tightly bounded around the cancelled sign; contextual placement was established on the half.",
        "A path typo prevented the first attempted display of crop 06; the existing file was then successfully displayed. A functions runtime replacement prevented the first combined display of crops 14 and 15; their existing files were then successfully displayed. No whole or half image was reopened. The independent task continued through the environment update using its existing context."
    ],
    "checks":[
        {
            "statement":"If g has order 2, the set {g,g^{-1}} has one element.",
            "event_type":"elementary consistency calculation",
            "reasoning":"From g^2=1, multiply by g^{-1} to obtain g=g^{-1}; hence the two displayed members coincide. This explains why a two-element assertion needs care when card S=2, conditional on g having that order.",
            "outcome":"The written exclusion of 2 is locally consistent with this elementary obstruction. This is not a proof that orientations on this page have order card S, and it was not used to settle the uncertain c-shaped sign or any deletion."
        }
    ],
    "unresolved":unresolved
}
(base / "report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
(base / "work_log.md").write_text(
    "# Scan 006 — R3 work log\n\n"
    "- First recorded UTC timestamp: 2026-11-20 00:00:02 UTC; preserved in report.json.\n"
    "- Read the assigned brief, conventions, preamble, notation snapshot, C, H, C_context, empty S, metadata and H drawing supplement only.\n"
    "- Viewed the whole page once, then top half once, then bottom half once.\n"
    "- Generated 21 unresolved-place crops with LANCZOS, autocontrast and sharpening, rotation 0.\n"
    "- Crop 05 reached context before an unrelated path typo stopped the next display. Retried only the existing crop 06 file.\n"
    "- A functions runtime replacement interrupted the attempted crop 14/15 display. Retried those existing files; both then reached context. No analysis was restarted and no whole/half image was reopened.\n"
    "- On the parent's resumption message, reported no current blockage and continued with existing independent context; no other reader files or findings were accessed.\n"
    "- All 21 crops have now been inspected. reading.tex and report.json assembled; final structural/TeX check pending.\n"
)
print(json.dumps({"findings":len(findings), "inventory":len(inventory),
                  "unresolved":len(unresolved), "crop_count":21}))
