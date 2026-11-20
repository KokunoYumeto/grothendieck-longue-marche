import json
from pathlib import Path

BASE = Path("/workspace/scratch/88012a0a2bcc")
WORK = BASE / "SP77_C13_147_work"
SCAN = 53
specs = json.loads((WORK / "records/147_scan053_crop_specs.json").read_text())
spec_by_name = {s["name"]: s for s in specs}
source = (BASE / "inputs/SP77_C13_147_texts/pages/147_scan053.tex").read_text()

def dq(text):
    return chr(96) * 2 + text + "''"

old_deleted_formula = r"\deleted{$\unsure{3(h_1(G)-1)+\nu}$ \quad $\unsure{\nu}=\operatorname{card}I$}"
deleted_formula = r"\deleted{$\unsure{3\leq2h_1(G)+\underset{\substack{\Vert\\\operatorname{Card}I}}{\unsure{\nu}}}$}"
old_eq63 = r"\text{(63)}\qquad\dim\operatorname{tot}(G)=3(g-1)+\underset{\substack{\Vert\\\operatorname{card}I}}{\nu}=3(h_1(G)-1)+\nu."
eq63 = r"\text{(63)}\qquad\dim\operatorname{tot}(G)=3(g-1)+\underset{\substack{\Vert\\\operatorname{Card}I}}{\nu}=3(h_1(G)-1)+\nu."
old_margin = r"\margin{puisque $g=\underbrace{\sum_\alpha g_\alpha}_{0}+h_1$}"
margin = r"\margin{puisque $g=\sum_\alpha\underbrace{g_\alpha}_{0}+h_1$}"
old_deleted_case = r"\deleted{a) $\unsure{\dim\operatorname{tot}(G)}=0$}"
deleted_case = r"\deleted{a) $\unsure{\dim\operatorname{tot}(G)|\operatorname{dimmod}(G)}=0$}"
draft = source
for old, new in [
    (r"\unsure{égal|égale}", "égal"),
    (old_deleted_formula, deleted_formula),
    (old_eq63, eq63),
    (old_margin, margin),
    (old_deleted_case, deleted_case),
]:
    assert draft.count(old) == 1, old
    draft = draft.replace(old, new)
(WORK / "drafts/147_scan053.tex").write_text(draft)

eq62 = r"\text{(62)}\qquad(M_{[G]},\Gamma^!)\simeq B(\Gamma^!_{S_0})"
figure = draft[draft.index(r"\figure{"):draft.index(r"\margin{52}")]
right_fig = figure[figure.index(r"\draw (8.2,.15)"):figure.index(r"\end{tikzpicture}")]
changes = []

def change(place, C, H, final, name, diff_C=False, diff_H=True,
           kind="misread word", evidence="", confidence="high",
           consequential=False, category="Words"):
    spec = spec_by_name[name]
    changes.append({
        "id": f"053-{len(changes)+1:02d}",
        "place": place, "C": C, "H": H, "final": final,
        "diff_C": diff_C, "diff_H": diff_H, "kind": kind,
        "evidence": evidence, "crop": f"crops/147_scan053_{name}.jpg",
        "box": spec["box"], "confidence": confidence,
        "consequential": consequential, "error_category": category,
    })

phrase = dq(r"dimension modulaire \inserted{ambiante}")
change(
    "opening sentence, quotation marks surrounding the dimension phrase",
    phrase, r"« dimension modulaire \add{ambiante} »", phrase, "02_dimension",
    kind="other", category="Other",
    evidence="The opening and closing marks are paired short high strokes. They are not angle-shaped guillemets. The closing pair follows the raised ambiante insertion; C's paired-quote convention is retained.",
)
change(
    "opening sentence, after d'un",
    "tel", "MD", "tel", "02_dimension",
    evidence="The word has a joined initial t stroke, low e and final tall l. There are no two capital letter bodies. The following underlined G is a separate symbol.",
)
change(
    "opening sentence, agreement word before à (M1025)",
    r"\unsure{égal|égale}", "égale", "égal", "03_egal",
    evidence="An accented e, the g body and long descender, a small a, and a terminal tall l are visible. After the l there is a gap before the separately accented à. There is no intervening final e. The masculine form is retained as written.",
)
change(
    "cancelled formula after égal à, including the definition below its terminal sign",
    old_deleted_formula,
    r"\struck{$\ldots\leqslant2h_1(G)+\nu$}; note: sous le nu biffé, = card I; followed by :",
    deleted_formula, "04_deletedformula",
    diff_C=True, kind="misread symbol or index", category="Struck text",
    confidence="low", consequential=True,
    evidence="The cancelled cluster before h has the descending curve and low return of a 2, followed by h with a low 1, then (G), a plus and a retraced terminal nu-like sign. The space from G's closing parenthesis to plus does not show a separate -1. The initial crossed cluster and comparison sign are not securely recoverable: 3 and the proposed inequality are tentative, and the whole formula remains unsure. Two short vertical identification strokes lead down from the terminal sign to a capital-height C and ard I; there is no independent second horizontal nu. The annotation is cancelled with the formula. H already reports the annotation's existence. No separate terminal colon is visible in this crop.",
)
change(
    "formula (63), operator name and the annotation beneath the first nu",
    old_eq63,
    r"(63)\quad\operatorname{dimmod}(G)=3(g-1)+\nu=3(h_1(G)-1)+\nu.; note: sous nu, = card I",
    eq63, "05_eq63", diff_C=True,
    kind="misread symbol or index", category="Symbols and indices",
    consequential=True,
    evidence="After dim, a tall initial t, rounded o and separate final t support tot, not mod. Beneath the first nu are two upright identification strokes and Card I. The initial C is open and capital-height relative to the low ard; the I has upper and lower bars. Both witnesses' lower-case card is changed to Card. H quotes the annotation but places it in an editorial note; its existence is not treated as omitted.",
)
change(
    "slanted left margin beside (63), extent of the bracket labelled zero",
    old_margin,
    r"note: puisque g=\sum_\alpha g_\alpha+h_1, g_\alpha=0",
    margin, "06_margin", diff_C=True,
    kind="insertion or placement", category="Insertions put in the wrong place",
    evidence="The rotated crop shows puisque followed by g=sum-alpha g-alpha+h-one. The lower bracket begins beneath the g after the summation sign and ends after its alpha, before plus. Its zero is centred below that g-alpha term. It does not extend under the summation sign or its index. H's note gives the intended zero condition but not the written bracketed layout.",
)
change(
    "cancelled preliminary case a), before the live h1=0 case",
    old_deleted_case,
    r"\struck{a) $\operatorname{dimmod}(G)=0$}",
    deleted_case, "09_deletedcase", diff_C=True,
    kind="misread symbol or index", category="Struck text",
    confidence="low", consequential=True,
    evidence="The horizontal strike crosses the central operator letters. Initial dim, the following parenthesized G and =0 are readable. The short intervening cluster has a terminal upright but its lower loops are obscured; it cannot securely distinguish C's tot from H's mod. Both candidates are retained under an explicit doubt. This is not resolved from the clear live operator in (63).",
)
change(
    "live case a), punctuation between h1=0 and i.e.",
    r"a) $h_1=0$ i.e.", r"a) $h_1=0$, i.e.", r"a) $h_1=0$ i.e.",
    "10_caseh0", kind="text not on the page", category="Text that is not on the page",
    evidence="The zero is followed by blank space and then the dotted i.e. abbreviation. No comma is inked in that interval.",
)
change(
    "live case a), after nu minus three",
    "donc on doit avoir", "dans ce cas", "donc on doit avoir", "12_donc",
    evidence="Four separated word groups are visible: donc with an initial looped d, on, doit with its tall crossed final t, and avoir. The word count and tall final t exclude dans ce cas.",
)
change(
    "cancelled word before sommet in the final paragraph",
    r"\deleted{\unsure{arbre}}", r"\struck{\ill{}}",
    r"\deleted{\unsure{arbre}}", "16_deletedarbre",
    kind="misread word", category="Struck text", confidence="low",
    evidence="Dense oblique and horizontal cancellation strokes cross the word. Some ar/br-like loops and a final low e-shaped return survive, supporting arbre only as a tentative reading. The initial and middle letters are not all plain. C's doubt is retained; this is not counted as a fully deciphered cancelled word.",
)
change(
    "final paragraph, l'arbre est / un sommet",
    "l'arbre est un sommet", r"l'arbre est \uncertain{réduit} à un sommet",
    "l'arbre est un sommet", "18_noreduit",
    kind="text not on the page", category="Text that is not on the page",
    evidence="The line ends with l'arbre est, and the next begins un sommet, ou un segment. There are no intervening réduit or à bodies, either in the line ending or as an insertion above the next line. The earlier réduit à in the paragraph is a separate occurrence and remains.",
)
change(
    "right-hand configurations beside the three cases of (64)",
    right_fig,
    "A prose drawing description: une droite portant a,b,c; deux droites sécantes; une chaîne de trois droites.",
    right_fig, "19_fig64", kind="drawing or diagram",
    category="Drawings and diagrams",
    evidence="The first stroke is gently curved and rising, with three transverse marks labelled a,b,c above it. The second drawing has two crossing strokes and four marks: a,b on the lower-left branch and c,d on the lower-right branch. The third has one nearly horizontal middle stroke crossing two oblique strokes, with a,b below the left crossing, c on the middle stroke and d,e below the right crossing. C's drawn geometry and tick marks are retained. H describes the topological content, but calls the first curved stroke a droite and does not reproduce the actual geometry. All strokes, marks and labels were counted on the native view and again on this crop.",
)
change(
    "lower-left handwritten footer",
    r"\margin{52}", "[absent]", r"\margin{52}", "20_footer",
    kind="omission", category="Omissions",
    evidence="A separate pale handwritten 52 stands at the lower-left edge: the 5 has an upper bar and lower sweep, and the 2 has a curved head and low rightward foot. Both digits are retained.",
)

decisions = [{
    "id": "M1025", "cote": "147", "scan": "53", "decision": "first",
    "reading": "égal",
    "what the ink shows": "Accented e, g with a descender, a and a final tall l; after l a clear gap leads to the separate à. No final e is present. This preserves the written masculine form.",
    "crop": "crops/147_scan053_03_egal.jpg (260,365,445,465)",
    "confidence": "high",
}]
supplemental = [
    {
        "id": "U053-01", "cote": "147", "scan": "53",
        "C_mark": r"\unsure{3(h_1(G)-1)+\nu}",
        "decision": "undecided", "reading": deleted_formula,
        "what the ink shows": "The visible central cluster favours 2h_1(G)+nu, but severe crossing prevents a secure reading of the initial cluster and comparison. The initial 3 in the draft is only a tentative candidate; a g-like letter is also possible. C's -1 is not discernible after the closing parenthesis. The whole replacement candidate remains unsure.",
        "crop": "crops/147_scan053_04_deletedformula.jpg (600,300,1115,470)",
        "confidence": "low",
    },
    {
        "id": "U053-02", "cote": "147", "scan": "53",
        "C_mark": r"\unsure{\nu}",
        "decision": "undecided", "reading": r"\underset{\substack{\Vert\\\operatorname{Card}I}}{\unsure{\nu}}",
        "what the ink shows": "The terminal sign is retraced and crossed. A nu-like body is possible but not fully plain. Its definition lies vertically below it. C's second inline nu is not a separate occurrence in the ink; the source has one annotated terminal sign, still doubtful.",
        "crop": "crops/147_scan053_04_deletedformula.jpg (600,300,1115,470)",
        "confidence": "low",
    },
    {
        "id": "U053-03", "cote": "147", "scan": "53",
        "C_mark": r"\unsure{\dim\operatorname{tot}(G)}",
        "decision": "undecided",
        "reading": r"\unsure{\dim\operatorname{tot}(G)|\operatorname{dimmod}(G)}",
        "what the ink shows": "The strike crosses the operator's low letter bodies. The tall terminal stroke admits t/d, and the middle letters do not decide tot/mod. The surrounding a), parenthesized G and =0 are readable.",
        "crop": "crops/147_scan053_09_deletedcase.jpg (330,865,800,960)",
        "confidence": "low",
    },
    {
        "id": "U053-04", "cote": "147", "scan": "53",
        "C_mark": r"\unsure{arbre}", "decision": "undecided",
        "reading": r"\deleted{\unsure{arbre}}",
        "what the ink shows": "Partial loops and a final low return fit arbre, but heavy cancellation crosses several essential letter bodies. Not every letter is plain, so the C doubt remains.",
        "crop": "crops/147_scan053_16_deletedarbre.jpg (275,1390,465,1485)",
        "confidence": "low",
    },
]

inventory_data = [
    ("display", "top", "(62), (M_[G], Gamma!) and B(Gamma!_S0)"),
    ("text", "upper main text", "La dimension modulaire ... d'un tel G ... égal à"),
    ("insertion", "above the opening phrase, before its closing quotation marks", "ambiante"),
    ("deletion", "after égal à", "cancelled formula with a vertical Card I definition"),
    ("display", "upper main display", "(63), dim tot(G)=3(g-1)+nu=3(h1(G)-1)+nu"),
    ("display", "under the first nu in (63)", "vertical identification, Card I"),
    ("margin note", "slanted left margin beside (63)", "puisque g=sum-alpha g-alpha+h1, with zero under g-alpha"),
    ("text", "three main baselines following (63)", "Nous allons faire l'énumération ... h1 in {0,1}"),
    ("deletion", "between the enumeration introduction and case a)", "a) dim ... (G)=0"),
    ("text", "middle case paragraph", "a) h1=0 i.e. G est un arbre ... 3<=nu<=5"),
    ("text", "lower paragraph", "Un arbre qui n'est pas réduit ... On trouve les cas"),
    ("deletion", "above/before sommet in the lower paragraph", "arbre, uncertain under dense cancellation"),
    ("drawing", "lower-left grouped case rows", "(64), three weighted graphs with nu and ambient-dimension labels"),
    ("drawing", "upper of the three right-hand configurations", "one rising curved stroke, ticks a,b,c"),
    ("drawing", "middle right-hand configuration", "two crossing strokes, ticks a,b and c,d"),
    ("drawing", "lower right-hand configuration", "three strokes in a chain, ticks a,b / c / d,e"),
    ("margin note", "lower-left footer", "52"),
]
inventory = [{
    "scan": SCAN, "sheet_kind": "text", "hand": "his hand",
    "element": f"053-E{i:02d}", "kind": kind, "position": pos,
    "first_words_or_objects": first, "transcribed": "yes",
} for i, (kind, pos, first) in enumerate(inventory_data, 1)]

box_readings = [
    ("01_eq62", "full formula; handwritten formula number and subscript zero", eq62),
    ("02_dimension", "insertion and its attachment; disputed word; quotation marks",
     "La " + phrase + r" d'un tel $\underline G$ est"),
    ("03_egal", "C doubt and disputed agreement ending", "égal à"),
    ("04_deletedformula", "entire cancelled doubtful formula and annotation; handwritten numerals", deleted_formula),
    ("05_eq63", "entire formula; disputed operator and capitalisation; all handwritten numerals", eq63),
    ("06_margin", "complete slanted margin formula; underbrace placement; handwritten zero and one", margin),
    ("07_le2", "handwritten numeral", r"$\leq2$,"),
    ("08_hconditions", "full inline formulas; every handwritten subscript and digit", r"$h_1\leq1$, i.e. $h_1\in\{0,1\}$"),
    ("09_deletedcase", "entire cancelled doubtful formula; handwritten zero", deleted_case),
    ("10_caseh0", "handwritten one and zero; disputed punctuation", r"a) $h_1=0$ i.e."),
    ("11_nminus3", "full numerical expression", r"$\nu-3$,"),
    ("12_donc", "C/H word difference", "donc on doit avoir"),
    ("13_nge3", "full numerical inequality", r"$\nu\geq3$."),
    ("14_dimle2", "handwritten numeral in inequality", r"soit $\leq2$,"),
    ("15_range", "entire numerical range", r"$3\leq\nu\leq5$."),
    ("16_deletedarbre", "cancelled word with C doubt", r"\deleted{\unsure{arbre}}"),
    ("17_weights", "both numerical bounds", r"$\geq2$, donc $\nu\geq6$"),
    ("18_noreduit", "handwritten five; disputed absent words at line break",
     r"donc si $\nu\leq5$, on voit que l'arbre est un sommet, ou un segment. On trouve"),
    ("19_fig64", "complete case display and drawings; every written number and label", "les cas\n" + figure),
    ("20_footer", "handwritten footer number", r"\margin{52}"),
]
boxes = []
for i, (name, kind, reading) in enumerate(box_readings, 1):
    x0, y0, x1, y1 = spec_by_name[name]["box"]
    boxes.append({
        "box": f"053-B{i:02d}", "kind": kind,
        "x0": x0, "y0": y0, "x1": x1, "y1": y1, "reading": reading,
    })

doubts = [
    {
        "place": "cancelled formula following égal à",
        "reading": deleted_formula,
        "alternatives": "The initial crossed cluster may be 3, a g-like letter or another obscured form. The inequality is also tentative. C proposes 3(h1(G)-1)+nu; H supplies an editorial ellipsis before <=2h1(G)+nu. No literal ellipsis is introduced as source ink.",
        "confidence": "low",
        "reason": "Crossing strokes obscure the beginning and retrace the terminal sign. The central 2h1(G)+ cluster is more visible, but the formula as a whole and its cancelled annotation are not certified.",
    },
    {
        "place": "terminal nu and vertical definition in the same cancelled formula",
        "reading": r"\underset{\substack{\Vert\\\operatorname{Card}I}}{\unsure{\nu}}",
        "alternatives": "Retraced terminal sign; no separate second nu.",
        "confidence": "low",
        "reason": "Cancellation obscures the exact terminal sign. The vertical attachment is clearer than the underlying glyph and replaces C's duplicated inline construction without resolving that glyph.",
    },
    {
        "place": "cancelled a) formula",
        "reading": r"\unsure{\dim\operatorname{tot}(G)|\operatorname{dimmod}(G)}",
        "alternatives": "tot / mod",
        "confidence": "low",
        "reason": "The strike crosses the central low bodies and leaves a terminal t/d-like upright. The live tot occurrence does not decide this separate cancellation.",
    },
    {
        "place": "cancelled word before sommet",
        "reading": r"\deleted{\unsure{arbre}}",
        "alternatives": "Underlying word not completely recoverable.",
        "confidence": "low",
        "reason": "Dense strokes obscure initial and middle letters; only portions support arbre. The reading remains tentative.",
    },
]
notation = [
    {
        "form": r"\Gamma^!",
        "meaning": "Gamma bearing an exclamation-mark superscript in (62).",
        "evidence": "Both superscripts in the complete formula crop 01_eq62 have an upright and a separate low dot.",
        "scope": "The two occurrences on this page; neither is changed to a prime.",
    },
    {
        "form": r"\dim\operatorname{tot}(G)",
        "meaning": "The author's live dimension label in (63).",
        "evidence": "Full formula crop 05_eq63: tall first t, low o and separate last t after dim.",
        "scope": "Only the live formula is confirmed; the cancelled preliminary case remains doubtful between tot and mod.",
    },
    {
        "form": r"\underset{\substack{\Vert\\\operatorname{Card}I}}{\nu}",
        "meaning": "The cardinality identification written vertically beneath nu.",
        "evidence": "Full formula crop 05_eq63; two uprights and capital-height Card followed by barred I.",
        "scope": "The live occurrence is confirmed. The earlier cancelled terminal sign and annotation remain within the doubtful whole formula.",
    },
    {
        "form": r"\sum_\alpha\underbrace{g_\alpha}_{0}",
        "meaning": "The margin marks the g-alpha term zero.",
        "evidence": "Rotated crop 06_margin: bracket begins after the Sigma and ends before plus.",
        "scope": "This local attachment replaces C's underbrace over the whole sum.",
    },
    {
        "form": r"\nu",
        "meaning": "The marked-point count used in the bounds and the three cases.",
        "evidence": "Live formula (63), case paragraph, final bounds and all three case labels.",
        "scope": "The live v-shaped signs are read locally; the cancelled terminal sign is not inferred from them.",
    },
]
abbreviations = [
    {"form": "dim.", "expansion": "dimension"},
    {"form": "dim", "expansion": "dimension"},
    {"form": "amb", "expansion": "ambiante"},
    {"form": "tot", "expansion": "totale (contextual expansion of the live operator label; not inserted into the text)"},
    {"form": "Card", "expansion": "cardinal"},
    {"form": "i.e.", "expansion": "id est"},
]
hand_log = [
    {
        "habit": "A terminal l can finish an agreement word without an expected final e; the gap before the next accented word is decisive.",
        "pages": "053", "scope": "égal à in the opening sentence only.",
        "misread_places": "C M1025 offered égal/égale; H regularised to égale. The crop supports égal.",
    },
    {
        "habit": "Small prose words can be stretched into low horizontal joins while retaining tall distinctive final letters.",
        "pages": "053", "scope": "tel and donc on doit avoir.",
        "misread_places": "H MD instead of tel and dans ce cas instead of donc on doit avoir.",
    },
    {
        "habit": "The 2 can be written as a compact curved hook with a very short or absent-looking lower foot.",
        "pages": "053", "scope": "The live <=2 and >=2 bounds, compared with the clearer 2s in the cases.",
        "misread_places": "No correction of these live numerals was needed; they were all boxed for independent reading.",
    },
    {
        "habit": "Card has a capital-height open C; vertical identification bars can be displaced below the identified symbol rather than read as a second inline equality.",
        "pages": "053", "scope": "The live annotation in (63), with the cancelled annotation separately qualified.",
        "misread_places": "Both witnesses lower-case card; C repeats the cancelled nu as a second inline definition.",
    },
]
notes = [
    {
        "id": "147-053-N01",
        "text": "On the sheet numbered 52 at the lower left, the author writes (62), an equivalence between (M_[G], Gamma!) and B(Gamma!_S0). This is a reading of the written statement only; no equivalence was proved or checked.",
    },
    {
        "id": "147-053-N02",
        "text": "The live formula (63) gives dim tot(G)=3(g-1)+nu=3(h1(G)-1)+nu, with Card I beneath nu. A slanted margin writes g=sum-alpha g-alpha+h1 and puts zero under a bracket attached to g-alpha. The earlier cancelled formula is not reliably recoverable and remains explicitly tentative, including its initial 3/comparison and terminal nu. The opening prose has the masculine égal as written.",
    },
    {
        "id": "147-053-N03",
        "text": "The author proceeds to enumerate ambient dimension at most two and says this forces h1 in {0,1}. In case h1=0 he writes that G is a tree, the dimension is nu-3, and 3<=nu<=5. He argues that a tree other than one vertex or one segment has at least three ends of marked weight at least two, hence nu>=6. He then draws three cases with weights 3; 2,2; and 2,1,2, and nu/dimension pairs 3/0, 4/1 and 5/2. The right-hand line configurations and all labels are reproduced. These claims were transcribed, not subjected to a proof or completeness check.",
    },
]
check_events = [{
    "statement_id": n["id"], "date": "2026-11-20",
    "who": "GPT-6 Astra Pro; inherited effort; SP77_C13_147 reader_b",
    "type": "carried as background without fault found",
    "outcome": "Reading only, no proof claim. Complete page ink was compared with C and H, and the relevant formulas/drawings were inspected in saved crops. The author's mathematical assertions were not independently validated.",
} for n in notes]

record = {
    "scan": SCAN, "reader": "reader_b", "line_count": 31,
    "changes": changes, "decisions": decisions,
    "supplemental_unindexed_C_doubts": supplemental,
    "inventory": inventory, "boxes": boxes, "doubts": doubts,
    "notation": notation, "abbreviations": abbreviations, "hand_log": hand_log,
    "notes": notes, "check_events": check_events,
    "coverage": {
        "whole_viewed": True, "halves_viewed": ["top", "bottom"],
        "all_tokens_read": True, "all_deletions_insertions_checked": True,
        "differences_accounted": "All 53 physical difference rows in tasks/053/differences.tsv were compared with the page. Substantive places are recorded in 13 collation rows. Inequality macro variants, spacing, array/TikZ syntax and the scanpage number are not source differences. H's explanatory notes about Card I and the margin were recognised as reports of existing ink, not counted as complete omissions. The actual capitalisation/vertical placement, margin bracket extent, cancelled candidate differences, word differences, quotation shapes, absent comma/reduit a and footer are accounted for. H's right-hand drawing description preserves the topology but does not reproduce its geometry; the curved first stroke and all transverse marks are explicitly accounted for.",
        "line_count_basis": "31 physical written baselines/annotation rows: 20 main or cancelled text/display baselines through les cas, 3 case/figure rows, the footer 52, the raised ambiante insertion, the slanted margin formula and its lower zero, plus the two vertical-identification rows and the two Card I annotation rows. The cancelled arbre is counted as its own interlinear baseline. Pure drawn graph strokes and braces do not count as extra text lines.",
        "main_baselines": [
            "(62)", "La ... d'un tel G est", "égal à with the cancelled formula",
            "(63)", "Nous allons ... cas où", "cette dimension ... déjà",
            "h1<=1, i.e. h1 in {0,1}", "cancelled a) operator(G)=0",
            "a) h1=0 ... la dim.", "modulaire ... doit avoir",
            "nu>=3 ... dim soit <=2", "cela signifie ... 3<=nu<=5",
            "Un arbre ... à un", "cancelled arbre",
            "sommet, ni à un segment, a au", "moins trois bouts ... avoir",
            "un poids marqué ... nu>=6", "donc si nu<=5 ... l'arbre est",
            "un sommet ... On trouve", "les cas",
        ],
        "numeral_coverage": "All handwritten digits, including formula labels 62,63,64; S0; all h-one subscripts; the cancelled formula's tentative digits; all 0/1/2/3/5/6 inequalities and ranges; the margin zero; every graph weight, nu value and dimension value; and footer 52 are included in the 20 contextual blind boxes.",
        "crop_reading_note": "All 20 saved crops were actually viewed. A batch requesting crops 06-08 returned a context-truncation message rather than images; those crops were then actually viewed in smaller batches and are counted only after that. Existing crops 04 and 05 were revisited during completion of still-open readings after context compaction; neither was recropped. The whole original and native halves were not repeated. Crop 06 is rotated -30 degrees; coordinates remain original-image coordinates.",
        "drawing_count": "Both readings of the figure counted 1/2/3 filled graph vertices and 0/1/2 graph edges on the left, and 1/2/3 curve strokes with 3/4/5 transverse marked positions on the right. The corresponding labels and all numerical values were read individually.",
        "main_review": "pending root visual review",
        "independent_second_read": "not begun; only first-reading boxes and readings prepared",
    },
    "unresolved": [
        "Cancelled formula after égal à: initial glyph, comparison and full original expression remain tentative.",
        "The cancelled terminal nu is not fully readable; its definition is vertical, not a second inline nu.",
        "Cancelled preliminary case operator: tot/mod unresolved.",
        "Cancelled word before sommet: arbre remains tentative.",
    ],
    "crop_files": [f"crops/147_scan053_{s['name']}.jpg" for s in specs],
}

for s in specs:
    assert (WORK / f"crops/147_scan053_{s['name']}.jpg").is_file()
for b in boxes:
    assert 0 <= b["x0"] < b["x1"] <= 1688
    assert 0 <= b["y0"] < b["y1"] <= 2362
assert [d["id"] for d in decisions] == ["M1025"]
assert len(changes) == 13
assert len(boxes) == 20
assert draft.count("{") == draft.count("}")
assert draft.count("$") % 2 == 0
assert r"\illegible" not in draft
assert r"\drawing{" not in draft
(WORK / "records/147_scan053.json").write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({
    "draft": str(WORK / "drafts/147_scan053.tex"),
    "record": str(WORK / "records/147_scan053.json"),
    "changes": len(changes), "boxes": len(boxes),
    "crops": len(specs), "indexed_decisions": len(decisions),
    "supplemental_doubts": len(supplemental), "line_count": record["line_count"],
}, ensure_ascii=False))
