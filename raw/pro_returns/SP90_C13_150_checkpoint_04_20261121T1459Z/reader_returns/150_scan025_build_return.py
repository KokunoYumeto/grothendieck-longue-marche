from pathlib import Path
import json
import re

ROOT = Path("/workspace/scratch/481648fc487b/SP90_C13_150_work")
PACKET = Path("/workspace/scratch/481648fc487b/reader_packets/150_scan025")
OUT = ROOT / "reader_returns" / "150_scan025.json"
TEX = ROOT / "reader_returns" / "150_scan025.tex"

crop_names = [
    "top_diagram", "definitions", "struck_symmetry", "b_struck_boundary",
    "b_subspaces", "b_noter", "b_espaces", "b_a_products", "c_commutent",
    "c_struck_lambda", "c_identity_operation", "c_arrow_etque",
    "c_second_lambda", "compat_formula", "struck_compatible",
    "inducing_formula", "tels_que", "induite", "T_E_Y_E",
    "bottom_replacement", "product_insertion", "lastline", "margin24",
    "et_si", "c_a_punctuation", "isolated_stroke",
]
crop_meta = {}
for name in crop_names:
    meta = json.loads((ROOT / "crops" / f"150_scan025_{name}.json").read_text())
    assert (ROOT / "crops" / meta["file"]).is_file()
    crop_meta[name] = meta

data = {
    "scan": 25,
    "reader": "reader_a",
    "line_count": 25,
    "changes": [],
    "marks": [],
    "inventory": [],
    "doubts": [],
    "notes": [],
    "check_events": [],
    "notation": [],
    "abbreviations": [],
    "hand_log": [],
    "second_boxes": [],
}

def change(place, C, H, final, evidence, crop, confidence, kind, error_kind,
           marked_in_H=False, change_C=False, change_H=False, consequential=""):
    meta = crop_meta[crop]
    data["changes"].append({
        "place": place, "C": C, "H": H, "final": final,
        "evidence": evidence, "crop": meta["file"], "box": meta["box"],
        "confidence": confidence, "kind": kind, "error_kind": error_kind,
        "marked_in_H": marked_in_H, "change_C": change_C,
        "change_H": change_H, "consequential": consequential,
    })

change(
    "opening diagram / two oblique inclusion relations",
    r'\arrow[dr,phantom,"\subset" sloped]',
    r'\cap',
    r'\arrow[dr,phantom,"\subset" sloped]',
    "The upper relation is an obliquely written open inclusion sign between the upper-left and middle-right expressions. The lower relation is likewise oblique, from the lower-left expression toward the middle-right one. H's vertically stacked cap/cup presentation does not preserve these relative positions. C's two sloping inclusion labels are retained. This is a diagram-placement finding, not a difference of TeX wrappers.",
    "top_diagram", "high", "drawing or diagram", "drawings and diagrams",
    change_H=True,
)
change(
    "opening diagram / cancelled words left of middle row",
    r'\deleted{\unsure{et où|i.e.}}',
    r'\uncertain{i.e.}',
    r'\deleted{\unsure{et si|et où}}',
    "The left entry curl and high t resemble the clear live 'et' below. A surviving dot above the last short upright resembles the dot in the live 'si'. The cancellation masks the intervening strokes, especially the s; 'et si' is therefore only the preferred doubtful reading. The initial tall stem is poor support for H's i.e. The mark is not resolved.",
    "top_diagram", "medium", "misread word", "struck text",
    marked_in_H=True, change_C=True, change_H=True,
)
change(
    "opening diagram / mark after Y cap E",
    r'Y\cap E\unsure{\}}\simeq Y_0\cap E',
    r'Y\cap E\simeq Y_0\times\mathbf{I}',
    r'Y\cap E\unsure{\}}\simeq Y_0\cap E',
    "There is a separate dark, vertically curled mark immediately after E and before the equivalence sign. It is not absent as in H. Its identification as a closing brace remains uncertain; the original C mark is retained.",
    "top_diagram", "medium", "omission", "omissions",
    change_H=True,
)
change(
    "opening diagram / lower right-hand expression",
    r'Y_0\cap E',
    r'Y_0\times\mathbf{I}',
    r'Y_0\cap E',
    "After Y with a small zero, the ink is an arch open downward and then a three-stroke E. It is not a cross followed by a barred I. C's unexpected intersection is retained without mathematical correction.",
    "top_diagram", "high", "misread symbol or index", "symbols and indices",
    change_H=True,
    consequential="The written expression is Y_0 cap E, although the product Y_0 times I appears in the lower compatibility display. No correction is imported from that later display.",
)
change(
    "opening definitions / first left-hand symbol",
    r'\unsure{\dot T_0|T_0}=\dot T\cap X_0',
    r'\dot T_0=\dot T\cap X_0',
    r'\dot T_0&=\dot T\cap X_0',
    "A distinct round ink dot stands above the first T, separated from its cap. The same line also has a separate dot above the T after the equals sign. Both are plain on the crop.",
    "definitions", "high", "misread symbol or index", "symbols and indices",
    change_C=True,
)
change(
    "opening definitions / punctuation after the three formulas",
    r'\unsure{\dot T_0|T_0}=\dot T\cap X_0,\qquad T_0=T\cap X_0,\qquad Y_0=Y\cap X_0.',
    r'\dot T_0=\dot T\cap X_0\\ T_0=T\cap X_0\\ Y_0=Y\cap X_0',
    r'\dot T_0&=\dot T\cap X_0\\ T_0&=T\cap X_0\\ Y_0&=Y\cap X_0',
    "The three definitions occupy separate lines to the right of the opening diagram. The dark terminal small loops or blobs are the zero subscripts of X; no following commas or final full stop are visible. C supplied punctuation is removed.",
    "definitions", "high", "text not on the page", "text not on page",
    change_C=True,
)
change(
    "below opening diagram / isolated vertical ink stroke",
    "[absent]", "[absent]", r'\unsure{\vert|1}',
    "A separate short near-vertical black pen stroke is present at approximately x=595, y=315, below the lower expression. It has no established numeral, punctuation, or diagram function. The literal vertical-stroke reading is placed first, with 1 only an alternative; no mathematical role is assigned.",
    "isolated_stroke", "low", "omission", "other",
    change_C=True, change_H=True,
)
change(
    "line 5 / initial et si",
    "Et si, symétriquement,",
    "et si, symétriquement,",
    "et si, symétriquement,",
    "The first e is a low entry curl joined to the tall t; it has the lowercase form rather than a capital E. The dot of i and both commas are visible.",
    "et_si", "high", "misread word", "abbreviation/spelling",
    change_C=True,
)
change(
    "line 5 / lower member of cancelled symmetry list and preceding separator",
    r'X_0\quad\unsure{T\cap E}',
    r'$X_0$, $T\cap E$',
    r'X_0\quad T\cap E',
    "The lower repeated T cap E has a clear T stem and cap, a distinct downward-open arch, and the surviving upright and bars of E, despite the zigzag cancellation. C's doubt on this lower repetition can be resolved. No comma is visible after X_0 at the end of the upper row; H's separator is not supplied.",
    "struck_symmetry", "high", "misread symbol or index", "struck text",
    change_C=True, change_H=True,
)
change(
    "line 6 / small cancelled identification below dotted E cap T",
    r'\deleted{\simeq T_0\times\{1\}}',
    r'\struck{$\simeq T_0\times\partial\mathbf{I}$}',
    r'\deleted{\simeq T_0\times\{1}',
    "Below dotted E cap T, the cancelled formula contains an equivalence sign, T with zero, a cross, a left curly brace with upper and lower hooks, and a plain short upright 1. No secure right curly brace survives before the end of the horizontal cancellation. The left brace is unlike a partial sign, and the following upright lacks the separate top and bottom bars of I elsewhere.",
    "b_struck_boundary", "high", "misread symbol or index", "symbols and indices",
    change_C=True, change_H=True,
    consequential="The cancelled endpoint expression is left unclosed as written; the missing right brace is not completed.",
)
change(
    "line 7 / sous-espaces",
    "sous-espaces",
    r'\uncertain{ensembles}',
    "sous-espaces",
    "A compact initial sous is followed by a detached short hyphen. In espaces the descending p is visible; there are no tall b/l stems that would support ensembles. The same compressed espaces shape recurs in the next sentence.",
    "b_subspaces", "high", "misread word", "words",
    marked_in_H=True, change_H=True,
)
change(
    "line 8 / Noter",
    "Noter que",
    "Notons que",
    "Noter que",
    "After N-o and the tall t, the short raised r shoulder runs directly into the terminal stroke. There is no additional rounded o and n/s sequence. The next word que is separate.",
    "b_noter", "high", "misread word", "words",
    change_H=True,
)
change(
    "line 9 / espaces",
    "espaces précédents",
    "ensembles précédents",
    "espaces précédents",
    "The word has the same low initial trace, conspicuous descending p, and compact ending as the espaces in sous-espaces above. No b or l ascender is present.",
    "b_espaces", "high", "misread word", "words",
    change_H=True,
)
change(
    "line 10 / before product list",
    r'à $T_0\times I$',
    r'à : $T_0\times\mathbf{I}$',
    r'à $T_0\times I$',
    "Only one small accented-letter cluster stands at the left before the product list. There is no separate colon after it. Its upper short stroke and lower compact body support the ordinary compressed à; H's extra colon is not present.",
    "b_a_products", "high", "text not on the page", "text not on page",
    change_H=True,
)
change(
    "line 11 / raised commutent",
    "commutent",
    r'\add{commutent}',
    r'\inserted{commutent}',
    "Commutent is written distinctly higher than the two lambda expressions at the right end of the c) line. Its attachment after lambda_T and before the following dans is clear. The raised placement is represented as an insertion, with medium confidence because there is no explicit caret and the author's lines also rise toward the right.",
    "c_commutent", "medium", "insertion or placement", "insertion placement",
    change_C=True,
)
change(
    "line 13 / cancelled lambda before induite",
    r'\deleted{$\unsure{\lambda}$}',
    "[absent]",
    r'\deleted{$\lambda_T$}',
    "The upper curved/slanting lambda stroke is visible. At its lower right, beneath the cancellation, a short T has a horizontal cap and a distinct downward stem. The surviving subscript is not merely the endpoint of the crossing stroke.",
    "c_struck_lambda", "high", "omission", "struck text",
    change_C=True, change_H=True,
)
change(
    "line 14 / à une = and position of cancelled homothétie",
    r"s'identifie à une $=$ \deleted{homothétie} opération de",
    r"s'identifie, via \struck{homothétie} une opération de",
    r"s'identifie à une $=$ \deleted{homothétie} opération de",
    "After s'identifie, a short à-like mark precedes a distinct low une and two separate horizontal strokes forming =. The cancelled homothétie follows that equals sign and precedes opération. There is no written via and no basis for moving une after the cancelled word. The equals sign is retained as a verbal abbreviation.",
    "c_identity_operation", "high", "misread word", "abbreviation/spelling",
    change_H=True,
)
change(
    "line 15 / T_0-T_0",
    r'T_0-T_0',
    r'T_0\to T_0',
    r'T_0-T_0',
    "The connector is a single almost horizontal stroke, with only a tiny terminal pen return. It has no pair of converging arrowhead strokes. The dash is transcribed as written.",
    "c_arrow_etque", "high", "misread symbol or index", "symbols and indices",
    change_H=True,
    consequential="The context suggests a map from T_0 to itself, but that interpretation is not substituted for the written dash.",
)
change(
    "line 15 / cancelled et que",
    r'\deleted{et que}',
    r'\struck{\ill{}}',
    r'\deleted{et que}',
    "The left entry and tall t remain above the strike; the q has a conspicuous long descender and is followed by the compact ue trace. These support et que, although the crossing stroke obscures parts of the low joins.",
    "c_arrow_etque", "medium", r'readable ink left as \ill{}', "readable ink left as illegible",
    marked_in_H=True, change_H=True,
)
change(
    "line 16 / punctuation after s'identifie",
    "s'identifie à",
    "s'identifie à :",
    r"s'identifie \unsure{à|:}",
    "There is one compact cluster consisting of an upper bent mark and a lower dark mark. It can be a very compressed à or colon-like punctuation; it does not support both à and a separate colon. The ambiguity is retained.",
    "c_a_punctuation", "medium", "text not on the page", "text not on page",
    change_H=True,
)
change(
    "line 16 / cancelled expression before lambda_T0 times id_I",
    r'\deleted{$\unsure{\lambda_{T_0}}$}',
    r'\struck{\ill{}}',
    r'\deleted{$\unsure{\lambda_{T_0}}$}',
    "The small T and its zero at the right of the cancelled expression are discernible. The leading lambda is heavily crossed and not sufficiently separable to resolve C's doubt. The partial reading is preserved rather than replaced by an unrestricted illegibility marker.",
    "c_second_lambda", "low", r'readable ink left as \ill{}', "readable ink left as illegible",
    marked_in_H=True, change_H=True,
)
change(
    "line 19 / unclosed compatibility parenthesis",
    r'\qquad\text{(compatible avec }E\simeq X_0\times I',
    r'\qquad(\text{compatible avec } E\simeq X_0\times\mathbf{I})',
    r'\qquad\text{(compatible avec }E\simeq X_0\times I',
    "The opening parenthesis is plain. The line continues to a barred I at the right paper edge, with no visible closing parenthesis after it. H's closing parenthesis is not supplied.",
    "compat_formula", "high", "text not on the page", "text not on page",
    change_H=True,
)
change(
    "line 20 / cancelled compatible aux structures",
    r'\deleted{compatible aux structures}',
    r'\struck{compatible avec structure}',
    r'\deleted{compatible \unsure{aux structures|avec structure}}',
    "Compatible and most of structure(s) are traceable, but the short intervening word lies directly beneath the cancellation. The brief low trace favors aux, while the last plural stroke cannot be securely separated from the cancellation/terminal return. The C and H alternatives remain explicitly doubtful.",
    "struck_compatible", "low", "misread word", "struck text",
    change_H=True,
)
change(
    "line 22 / tels or tel",
    "tels que",
    "tel que",
    r'\unsure{tels|tel} que',
    "The t-e-l sequence is clear. After the high l, a curved exit could include a terminal s but is not securely distinguishable from the pen return of l. Grammar is not used to force the singular. C's plural remains the first doubtful option.",
    "tels_que", "medium", "misread word", "words",
    change_H=True,
)
change(
    "line 23 / overwritten verb before sur T_E",
    r"\unsure{s'identifie|induite|standarde}",
    r'\add{induite}',
    r"\unsure{induite|s'identifie}",
    "The legible ending resembles d-u-i-t-e, with a looped d and one late tall t; it does not show the clear f descender of s'identifie elsewhere on this page. The beginning is heavily overwritten and includes strokes that may belong to a prior reading. Induite is favored but kept doubtful. No fully legible deleted precursor or separate insertion layer can be reconstructed.",
    "induite", "medium", "misread word", "words",
    change_C=True, change_H=True,
    consequential="The exact grammar of the final compatibility condition remains uncertain at this overwritten verb.",
)
change(
    "line 23 / T_E",
    r'\overline T_E',
    r'T_E',
    r'$T_E$',
    "Only one horizontal cap is present, detached from the short downstroke of T. There is no second horizontal stroke that would form an overbar. The ordinary T form agrees with other separated-cap T's on this page.",
    "T_E_Y_E", "high", "misread symbol or index", "symbols and indices",
    change_C=True,
    consequential="The proposed reading does not introduce closure notation absent from the ink.",
)
change(
    "line 23 / cancellation after Y_E",
    r'\deleted{avec \unsure{de} la}',
    r'\struck{soit} \add{soit} la',
    r'\deleted{avec \unsure{de} la}',
    "The cancelled lower span begins with a low loop and a long compact word trace compatible with avec. A crowded middle cluster remains compatible with de but not securely legible. The final tall loop and adjoining small body support la, and the cancellation continues across them. H's shorter soit followed by live la does not account for the full span. C's uncertainty on de is retained.",
    "bottom_replacement", "low", "misread word", "struck text",
    change_H=True,
)
change(
    "line 23 / interlinear replacement une",
    r'\inserted{une}',
    r'\add{soit}',
    r'\inserted{une}',
    "The small added word above the cancelled span consists of low connected u/n/e humps and a terminal sweep. The tall stroke meeting its right end descends from the q of cônique in the line above; it is not a t belonging to the insertion. There is no dotted i sequence of soit. The insertion attaches between Y_E and the following structure.",
    "bottom_replacement", "high", "misread word", "insertion placement",
    change_H=True,
)
change(
    "lines 23-24 / underlined structure cônique produit",
    r'\uline{structure cônique produit}',
    r'structure \emph{cônique produit}',
    r'\uline{structure cônique produit}',
    "A separate underline is present beneath structure at the end of the upper line, and another beneath cônique produit on the next line. The start of the first underline is late beneath the word, but it plainly marks that word as well.",
    "bottom_replacement", "high", "other", "other",
    change_H=True,
)
change(
    "line 24 / inserted par I, and its attachment",
    r'\inserted{par $I$}',
    r'\add{par $\mathbf{I}$,}',
    r'\inserted{par $I$,}',
    "The interlinear words par I have a separate small comma immediately after I. A curved leader descends to the gap after produit and before d'une; that leader is distinct from the comma and is not a parenthesis. The comma omitted by C is restored.",
    "product_insertion", "high", "omission", "omissions",
    change_C=True,
)
change(
    "line 25 / terminal T_0 after subset",
    r'Y_0\subset\overline T_0',
    r'Y_0\subset T_0',
    r'Y_0\subset T_0',
    "After the subset sign, T has one detached curved cap and one short stem, followed by zero. There is no independent overbar above that cap. This is the same form as the ordinary T_E immediately above.",
    "lastline", "high", "misread symbol or index", "symbols and indices",
    change_C=True,
)
change(
    "line 25 / after final cancelled par I",
    r'\deleted{par $I$}.',
    r'\struck{par $\mathbf{I}$}',
    r'\deleted{par $I$}',
    "The cancellation runs through par I and terminates in a tapering stroke. No separate full stop follows it. C's final full stop is removed.",
    "lastline", "high", "text not on the page", "text not on page",
    change_C=True,
)
change(
    "bottom-left margin / foliation",
    r'\margin{24}',
    "[absent]",
    r'\margin{24}',
    "The lower-left margin has an open-curved 2 and a distinct angular 4 in thinner, lighter writing than the main text. The number is transcribed as a margin item. Its attribution is uncertain, so it is not labeled as the author's own page number.",
    "margin24", "high", "omission", "omissions",
    change_H=True,
)

def mark(mark, context, decision, reading, evidence, crop, confidence):
    meta = crop_meta[crop]
    data["marks"].append({
        "mark": mark, "context": context, "decision": decision,
        "reading": reading, "evidence": evidence,
        "crop": meta["file"], "box": meta["box"], "confidence": confidence,
    })

mark(
    r'\unsure{et où|i.e.}',
    r'\deleted{\unsure{et où|i.e.}} & T\cap E',
    "undecided", r'\unsure{et si|et où}',
    "The left tall t and final dot favor et si when compared with the live et si below, but the cancellation hides the s and joins. The doubt remains, with revised alternatives.",
    "top_diagram", "medium",
)
mark(
    r'\unsure{\}}',
    r'Y\cap E\unsure{\}}\simeq Y_0\cap E',
    "undecided", r'\unsure{\}}',
    "A separate vertically curled ink mark is present; its precise function and identification as a closing brace remain uncertain.",
    "top_diagram", "medium",
)
mark(
    r'\unsure{\dot T_0|T_0}',
    r'\unsure{\dot T_0|T_0}=\dot T\cap X_0',
    "first", r'\dot T_0',
    "A separate round dot is plainly visible above the T cap, like the dot on the T after the equals sign.",
    "definitions", "high",
)
mark(
    r'\unsure{T\cap E}',
    r'\deleted{$\unsure{T\cap E},T\cap\dot E,X_0',
    "undecided", r'\unsure{T\cap E}',
    "T and E are recognizable, but the putative intersection arch is directly covered by the dense first zigzag of the cancellation. The full first formula is not secure enough to remove the mark.",
    "struck_symmetry", "medium",
)
mark(
    r'\unsure{T\cap E}',
    r'X_0\quad\unsure{T\cap E}$}',
    "first", r'T\cap E',
    "On the lower repeated formula, the T, the independent intersection arch, and E's upright and bars are individually visible below and between the cancellation strokes.",
    "struck_symmetry", "high",
)
mark(
    r'\unsure{\lambda}',
    r'\deleted{$\unsure{\lambda}$} induite',
    "other", r'\lambda_T',
    "The lambda is readable, and a small T with its own downward stem survives at the lower right beneath the strike. The reading therefore includes the subscript omitted from C's proposed lambda.",
    "c_struck_lambda", "high",
)
mark(
    r'\unsure{\lambda_{T_0}}',
    r'\deleted{$\unsure{\lambda_{T_0}}$} $\lambda_{T_0}\times',
    "undecided", r'\unsure{\lambda_{T_0}}',
    "T and zero are discernible at the lower right. The leading glyph is crossed too densely to resolve it as lambda without a doubt mark.",
    "c_second_lambda", "low",
)
mark(
    r"\unsure{s'identifie|induite|standarde}",
    r"sur $Y$ \unsure{s'identifie|induite|standarde} sur",
    "undecided", r"\unsure{induite|s'identifie}",
    "The exposed d-u-i-t-e-like ending favors induite, but the initial strokes are overwritten and may preserve part of a previous wording. The mark is narrowed and retained, not resolved.",
    "induite", "medium",
)
mark(
    r'\unsure{de}',
    r'\deleted{avec \unsure{de} la}',
    "undecided", r'\unsure{de}',
    "The middle knot has a possible looped d and a low continuation, but the cancellation prevents a secure separation of both letters. The original doubt is retained.",
    "bottom_replacement", "low",
)

def inv(element, kind, position, first, hand="his hand"):
    data["inventory"].append({
        "element": element, "kind": kind, "position": position,
        "first_words_or_objects": first, "sheet_kind": "text",
        "hand": hand, "transcribed": "yes",
    })

inv("D01", "diagram", "top left / lines 1-3",
    r"\dot T\cap E\simeq\dot T_0\times I; T\cap E\simeq T_0\times I; Y\cap E\unsure{\}}\simeq Y_0\cap E; two sloping inclusions")
inv("D02", "display", "top right / beside opening diagram",
    r"où \dot T_0=\dot T\cap X_0; T_0=T\cap X_0; Y_0=Y\cap X_0")
inv("X01", "deletion", "top left / left of middle diagram row",
    r"\deleted{\unsure{et si|et où}}")
inv("P01", "text", "below opening diagram / x approximately 595, y approximately 315",
    r"\unsure{\vert|1}, isolated pen stroke with no assigned function")
inv("T01", "text", "line 5", "et si, symétriquement,")
inv("X02", "deletion", "line 5 / upper row of cancelled symmetry list",
    r"\unsure{T\cap E}, T\cap\dot E, X_0")
inv("X03", "deletion", "line 5 / lower row of cancelled symmetry list",
    r"T\cap E")
inv("T02", "text", "lines 6-10",
    "b) E cap T ... sous-espaces côniques ... Noter que les trois espaces précédents ... On suppose enfin")
inv("X04", "deletion", "interlinear below dotted E cap T in line 6",
    r"\simeq T_0\times\{1; small identification cancelled before completion")
inv("X05", "deletion", "line 8 / before Noter que",
    "Le fait que")
inv("T03", "text", "lines 11-16",
    "c) Les homothéties ... commutent ... une = ... opération ... lambda_T0 times id_I")
inv("X06", "deletion", "line 11 / after homothéties", "par")
inv("A01", "insertion", "raised at right end of line 11",
    "commutent; insertion status less secure than its attachment")
inv("X07", "deletion", "line 13 / before induite", r"\lambda_T")
inv("X08", "deletion", "line 14 / after une =", "homothétie")
inv("X09", "deletion", "line 15 / between T_0-T_0 and soit", "et que")
inv("X10", "deletion", "line 16 / before retained product formula",
    r"\unsure{\lambda_{T_0}}")
inv("T04", "text", "line 17", "Donc les conditions a) b) c) équivalent à celle-ci :")
inv("T05", "text", "line 18",
    "Underlined Condition de compatibilité; existential sign; homéomorphisme")
inv("D03", "display", "line 19",
    r"T\cap E\simeq T_0\times I (compatible avec E\simeq X_0\times I; unclosed parenthesis; several retraced glyphs")
inv("X11", "deletion", "line 20",
    r"compatible \unsure{aux structures|avec structure}")
inv("T06", "text", "left of line 21", "induisant")
inv("D04", "display", "line 21",
    r"\dot T\cap E\simeq\dot T_0\times I, Y\cap E\simeq Y_0\times I; retraced initial letters")
inv("T07", "text", "lines 22-25",
    r"\unsure{tels|tel} que la structure cônique de T sur Y ... structure cônique produit ... T_0 sur Y_0\subset T_0")
inv("O01", "text", "line 23 / overwritten beginning",
    r"\unsure{induite|s'identifie}; no securely separable precursor")
inv("X12", "deletion", "line 23 / after Y_E",
    r"avec \unsure{de} la")
inv("A02", "insertion", "above cancelled span after Y_E", "une")
inv("A03", "insertion", "above gap after produit in line 24",
    "par I, with a curved insertion leader into the gap before d'une")
inv("X13", "deletion", "line 25 / after comma following T_0", "par I")
inv("M01", "margin note", "bottom-left margin", "24",
    "thin, lighter hand/pen; attribution uncertain")

data["doubts"] = [
    {"place": "opening diagram / cancelled words", "reading": r"\unsure{et si|et où}",
     "alternatives": "et si favored by comparison with the live words below; et où remains possible; i.e. is disfavored but the cancellation is not fully recoverable",
     "confidence": "medium"},
    {"place": "opening diagram / curled mark after E", "reading": r"\unsure{\}}",
     "alternatives": "closing brace-like mark; function not established", "confidence": "medium"},
    {"place": "below opening diagram", "reading": r"\unsure{\vert|1}",
     "alternatives": "literal near-vertical pen stroke; numeral 1; incidental pen stroke", "confidence": "low"},
    {"place": "line 5 / first cancelled T cap E", "reading": r"\unsure{T\cap E}",
     "alternatives": "T and E are recognizable; the intervening cap is occluded by the cancellation", "confidence": "medium"},
    {"place": "line 11 / commutent placement", "reading": r"\inserted{commutent}",
     "alternatives": "raised insertion after the two lambda expressions; possibly an unusually raised continuation of the same line", "confidence": "medium"},
    {"place": "line 16 / compact punctuation after s'identifie", "reading": r"\unsure{à|:}",
     "alternatives": "compressed à; colon-like punctuation; there is not a separate à plus colon", "confidence": "medium"},
    {"place": "line 16 / cancelled lambda expression", "reading": r"\unsure{\lambda_{T_0}}",
     "alternatives": "T and zero discernible; leading lambda remains obscured", "confidence": "low"},
    {"place": "line 20 / cancelled phrase", "reading": r"compatible \unsure{aux structures|avec structure}",
     "alternatives": "short preposition and final plural ending remain obscured by the strike", "confidence": "low"},
    {"place": "line 22 / adjective before que", "reading": r"\unsure{tels|tel}",
     "alternatives": "terminal s versus l pen return", "confidence": "medium"},
    {"place": "line 23 / overwritten verb", "reading": r"\unsure{induite|s'identifie}",
     "alternatives": "induite favored by the exposed ending; initial overwriting prevents secure reconstruction of the word or its precursor",
     "confidence": "medium"},
    {"place": "line 23 / middle of cancelled phrase", "reading": r"\unsure{de}",
     "alternatives": "de is plausible but the two letters cannot be separated securely beneath the crossing stroke",
     "confidence": "low"},
]

data["notes"] = [
    "The page is an upright handwritten mathematical note, not a typescript or a reused printed sheet. No watermark or reverse-face text is transcribed.",
    "The line_count of 25 counts the principal horizontal writing bands, including the opening display bands, the isolated stroke, and the cancelled compatible phrase. The three right-hand definitions share the opening region; interlinear material is separately inventoried.",
    "The opening material defines dotted T_0, T_0, and Y_0 by intersection with X_0 and places three intersection expressions in a two-inclusion diagram. The lower diagram expression actually reads Y_0 cap E. That unexpected reading is retained even though Y_0 times I appears in the later compatibility display.",
    "Statement 150.025.N1: Condition b) says that E cap T, dotted E cap T, and X_0 cap T are conical subspaces of T, stable under its homotheties, and identifies them using condition a) with T_0 times I, T_0 times {1}, and T_0 times {0}. This is a description of the manuscript's claim, not a checked theorem.",
    "Statement 150.025.N2: Condition c) requires the E- and T-homotheties to commute on T cap E and describes the induced operation as lambda_T0 times id_I. The page writes a dash in T_0-T_0 and an equals sign in the verbal phrase une = opération; neither is silently expanded or normalized.",
    "Statement 150.025.N3: The manuscript asserts that a), b), and c) are equivalent to a compatible product homeomorphism preserving the displayed dotted-T and Y subsets and a product conical structure over I. Condition a) and earlier definitions are not in the assigned packet, and the overwritten final-clause verb remains doubtful.",
    "No targeted proof check, independent re-proof, computation, or formal verification was performed by this reader. The check_events list is intentionally empty; a reading of the assertion is not reported as a proof check.",
    "The cancelled small identification under dotted E cap T visibly has a left brace and 1 without a secure right brace. The compatible avec parenthesis at the right edge likewise has no closing parenthesis on this leaf. Neither is completed.",
    "Several T/E-shaped letters in the lower displays and a T_0 are densely retraced or overwritten. The final intended glyphs are readable as transcribed, but the time order and underlying old characters are not securely separable. No invented deleted precursor is supplied. These complete formulas are included among the second-reading boxes.",
    "The plain T_E and the final T_0 have one detached cap, not a cap plus an overbar. C's overline wrappers at these two places are removed on the ink evidence.",
    "A separate vertical ink stroke below the opening diagram is preserved with a literal vertical-stroke first reading and 1 as an alternative. Its function is not established, and it is not assigned an equation number or a mathematical meaning.",
    "The bottom-left 24 is in finer/lighter writing than the main text. It is retained as margin foliation with attribution uncertain, not as an established authorial manuscript page number. No date is visible on this page.",
    "Witness H's editorial opening note and explanatory note about the cancelled words are excluded as commentary. Its source-word reading i.e. was nevertheless collated against the actual cancellation.",
    "The raised commutent is represented as an insertion at medium confidence. The reading and attachment are secure; the absence of a caret and the rising baseline mean its insertion status deserves second review.",
    "The first-pass inspection used the whole image once, both native-resolution halves once, and 26 unique crop-helper outputs, all viewed. No OCR, external research, or TeX compilation was used.",
]

data["notation"] = [
    {"form": r"\dot T,\dot E,\dot T_0",
     "meaning_or_shape": "The dot is a distinct small ink dot above the letter. The mathematical definition of the dotted operation is not given on this leaf.",
     "places": "opening diagram, first right-hand definition, cancelled symmetry list, condition b), lower induced-identifications display"},
    {"form": r"T_0=T\cap X_0,\quad Y_0=Y\cap X_0",
     "meaning_or_shape": "Explicit definitions on this page; the small zero may be filled and look like a dot.",
     "places": "right of opening diagram"},
    {"form": r"\lambda_E,\lambda_T,\lambda_{T_0}",
     "meaning_or_shape": "The page calls lambda_E and lambda_T homotheties and names the induced operation lambda_T0. T_0 is a nested subscript in the latter.",
     "places": "condition c), including cancelled occurrences"},
    {"form": r"I",
     "meaning_or_shape": "A capital I with top and bottom bars; distinct from the plain upright digit 1 in the endpoint sets.",
     "places": "product expressions throughout; inserted and deleted par I"},
    {"form": r"=",
     "meaning_or_shape": "Two horizontal ink strokes used verbally in une = opération; retained as written, with même as the likely expansion.",
     "places": "line 14"},
    {"form": r"T_0-T_0",
     "meaning_or_shape": "A literal horizontal dash appears between the two T_0's. A map interpretation is suggested by the prose but no arrowhead is drawn.",
     "places": "line 15"},
    {"form": r"\operatorname{id}_I",
     "meaning_or_shape": "Written id with the barred capital I below/right; identity notation in the product operation.",
     "places": "end of condition c)"},
    {"form": r"T_E,\quad T_0",
     "meaning_or_shape": "The long horizontal T cap can be detached from its short stem. There is no extra overbar in these lower occurrences.",
     "places": "line 23 T_E; line 25 T_0 after the subset sign"},
]
data["abbreviations"] = [
    {"form": "=", "expansion": "même, in the verbal phrase une = opération; the sign itself is retained in the transcription"},
    {"form": "id", "expansion": "identity, in id_I; mathematical abbreviation retained"},
]
data["hand_log"] = [
    {"habit": "The cap of T can be long and detached from a much shorter downstroke, giving a false visual impression of an overbar.",
     "places": "scan 025, T_E in line 23 and final T_0 after the subset sign in line 25; comparable separated caps elsewhere on the sheet",
     "consistent": "Both disputed lower occurrences show only one horizontal cap. Other T's on the sheet may have the cap attached or heavily retraced.",
     "witness_errors": "C supplied an overline at T_E and at the final T_0; H's ordinary T is supported."},
    {"habit": "In rapid prose, p may be an open V-like stroke with a long descender, while surrounding short letters flatten into low strokes.",
     "places": "scan 025, espaces in sous-espaces and in les trois espaces précédents",
     "consistent": "The two seen occurrences agree in the distinguishing p descender.",
     "witness_errors": "H read ensembles at both places; the absent b/l ascenders and visible p favor C's espaces."},
    {"habit": "The short word une can be a low series of joined humps with a long exit and no tall ascender.",
     "places": "scan 025, une = opération and interlinear une above the final cancellation",
     "consistent": "Both seen occurrences have low undulating forms.",
     "witness_errors": "H read the inserted une as soit. The vertical stroke meeting its right end is the q descender from cônique above, not a t of the added word; no dotted-i sequence is present."},
    {"habit": "A very compressed à may resemble a two-mark punctuation cluster.",
     "places": "scan 025, before the b) product list and after s'identifie in the last line of c)",
     "consistent": "The first is accepted as à; the latter remains ambiguous between à and colon-like punctuation.",
     "witness_errors": "H supplied à plus a separate colon at both places. Only one cluster is present at each."},
    {"habit": "Digit zero is often a very small loop and can be completely filled.",
     "places": "scan 025, X_0 in the opening definitions, T_0 throughout, Y_0 in the opening and lower displays",
     "consistent": "All inspected zero subscripts are small round or filled forms; no digit interchange is established.",
     "witness_errors": "No C/H digit error established from this habit on this sheet."},
    {"habit": "The capital I has horizontal top and bottom bars, whereas numerical 1 in braces is a short plain upright.",
     "places": "scan 025, b) product list, cancelled identification under dotted E cap T, inserted par I",
     "consistent": "The distinction is visible in the live endpoint products and the disputed cancellation.",
     "witness_errors": "H's partial-I reading in the small cancelled identification is unsupported; the visible characters favor left brace followed by 1."},
    {"habit": "A surviving small subscript T can merge its cap with a cancellation line while leaving its downstroke visible.",
     "places": "scan 025, cancelled lambda before induite in condition c)",
     "consistent": "One disputed example; not generalized beyond this page.",
     "witness_errors": "C's proposed cancelled lambda lacked the visible T subscript, while H omitted the entire cancelled expression."},
    {"habit": "A final low return can imitate an extra letter, so endings cannot be inferred from grammatical agreement.",
     "places": "scan 025, tels/tel before the final compatibility clause",
     "consistent": "This example remains unresolved; no stable plural-ending rule is asserted.",
     "witness_errors": "C and H disagree on the final s; neither reading is adopted without a doubt mark."},
]

def second(box_id, kind, coords, reading, reason):
    data["second_boxes"].append({
        "box": box_id, "kind": kind, "coords": coords,
        "reading": reading, "reason": reason,
    })

second("b01", "handwritten number", [375, 10, 715, 88],
       r"\dot T\cap E\simeq\dot T_0\times I",
       "Complete upper expression, including handwritten zero subscript.")
second("b02", "struck passage|C/H word difference|low-confidence departure", [300, 73, 455, 132],
       r"\deleted{\unsure{et si|et où}}",
       "All cancelled opening words; revised but unresolved C doubt and C/H word difference.")
second("b03", "handwritten number", [470, 75, 925, 197],
       r"\subset\quad T\cap E\simeq T_0\times I",
       "Upper oblique inclusion and complete middle expression with zero.")
second("b04", "doubt formula|handwritten number", [390, 155, 740, 275],
       r"Y\cap E\unsure{\}}\simeq Y_0\cap E",
       "Whole formula containing C's uncertain curly mark; Y_0 and lower oblique inclusion also lie in this box.")
second("b05", "doubt formula|handwritten number", [1070, 110, 1495, 315],
       r"\dot T_0=\dot T\cap X_0;\ T_0=T\cap X_0;\ Y_0=Y\cap X_0",
       "All three right-hand formulas, including the resolved dotted-T doubt and every zero. Semicolons here separate inventory items, not manuscript punctuation.")
second("b06", "handwritten number|low-confidence departure", [540, 270, 650, 345],
       r"\unsure{\vert|1}",
       "The isolated vertical pen stroke is preserved without assigning a numeral role; 1 is only an alternative.")
second("b07", "C/H word difference", [260, 345, 800, 445],
       "et si, symétriquement,",
       "Capitalization disagreement and same-page comparison for the upper cancelled phrase.")
second("b08", "struck passage|doubt formula|handwritten number", [835, 330, 1340, 480],
       r"\deleted{\unsure{T\cap E},T\cap\dot E,X_0\quad T\cap E}",
       "Entire two-row cancelled list, including the unresolved first formula, resolved lower repetition, and X_0.")
second("b09", "handwritten number", [835, 465, 1350, 555],
       r"X_0\cap T\ (=T\cap X_0=T_0)",
       "Complete live formula in b), covering every zero in this expression.")
second("b10", "struck passage|handwritten number", [630, 465, 825, 590],
       r"\dot E\cap T\deleted{\simeq T_0\times\{1}",
       "Full interlinear cancelled identification and its attachment; zero, 1, and unclosed endpoint brace.")
second("b11", "C/H word difference", [260, 565, 1015, 665],
       "sous-espaces côniques de",
       "Every letter of the sous-espaces/ensembles disagreement, including the separate hyphen.")
second("b12", "struck passage", [1025, 620, 1395, 735],
       r"\deleted{Le fait que}",
       "Entire cancelled phrase before Noter, including the q descender.")
second("b13", "C/H word difference", [1370, 615, 1650, 720],
       "Noter que",
       "Noter/Notons disagreement.")
second("b14", "C/H word difference", [475, 725, 1015, 820],
       "espaces précédents",
       "Second espaces/ensembles disagreement.")
second("b15", "handwritten number", [250, 805, 1135, 905],
       r"à T_0\times I,\ T_0\times\{1\},\ T_0\times\{0\}.",
       "Complete b) product list, all zero/one digits, and the disputed punctuation before it.")
second("b16", "insertion|low-confidence departure", [1230, 895, 1645, 980],
       r"\inserted{commutent}",
       "Raised word after the two homotheties; its insertion status is medium confidence.")
second("b17", "struck passage", [810, 935, 925, 1010],
       r"\deleted{par}",
       "Cancelled par before lambda_E.")
second("b18", "struck passage|doubt formula", [245, 1115, 590, 1230],
       r"\deleted{\lambda_T}\ \text{induite}",
       "Complete cancelled formula containing C's lambda doubt and the neighboring word establishing its attachment.")
second("b19", "handwritten number", [695, 1095, 1130, 1200],
       r"\lambda_T\ (\lambda\in[0,1])",
       "The complete interval formula with zero and one.")
second("b20", "handwritten number", [1260, 1085, 1665, 1185],
       r"T_0\times\{0\}\ \text{et}\ T_0\times\{1\}",
       "Both endpoint-product expressions, including all zero/one digits.")
second("b21", "struck passage|C/H word difference", [255, 1180, 1180, 1300],
       r"s'identifie à une = \deleted{homothétie}",
       "The disputed à une = / via wording and full cancelled homothétie.")
second("b22", "struck passage|C/H word difference|handwritten number", [255, 1270, 1080, 1395],
       r"T_0-T_0,\ \deleted{et que}\ \text{soit}\ \lambda_{T_0},",
       "Dash/arrow disagreement, complete cancelled et que, and all zero subscripts in the local passage.")
second("b23", "handwritten number", [245, 1365, 845, 1485],
       r"\lambda_T\ \text{sur}\ T\cap E\simeq T_0\times I",
       "Complete live product expression in the last line of c), including zero.")
second("b24", "low-confidence departure", [845, 1350, 1245, 1460],
       r"s'identifie \unsure{à|:}",
       "Single compact punctuation/à cluster; doubtful added qualification of C and conflict with H's à plus colon.")
second("b25", "struck passage|doubt formula|handwritten number", [1255, 1330, 1655, 1455],
       r"\deleted{\unsure{\lambda_{T_0}}}\ \lambda_{T_0}\times\operatorname{id}_I.",
       "Whole cancelled doubtful formula and adjacent retained formula, with both zero subscripts.")
second("b26", "handwritten number", [590, 1670, 1680, 1800],
       r"T\cap E\simeq T_0\times I\quad(\text{compatible avec }E\simeq X_0\times I",
       "Complete compatibility formula including all zero subscripts, retraced glyphs, and absent closing parenthesis at the page edge.")
second("b27", "struck passage|C/H word difference|low-confidence departure", [260, 1780, 945, 1895],
       r"\deleted{compatible \unsure{aux structures|avec structure}}",
       "All cancelled words and the added narrow doubt.")
second("b28", "handwritten number", [600, 1850, 1465, 1985],
       r"\dot T\cap E\simeq\dot T_0\times I,\quad Y\cap E\simeq Y_0\times I",
       "Both complete induced-identification formulas, all zeros, and the retraced T/E-shaped letters.")
second("b29", "C/H word difference|low-confidence departure", [255, 1980, 605, 2095],
       r"\unsure{tels|tel} que",
       "Plural-ending disagreement; uncertainty concerns a terminal s versus a pen return.")
second("b30", "C/H word difference|low-confidence departure", [250, 2080, 650, 2180],
       r"\unsure{induite|s'identifie}\ \text{sur}",
       "Entire heavily overwritten verb, including any possible underlying strokes, and its attachment.")
second("b31", "doubt formula", [665, 2055, 1000, 2170],
       r"T_E\ \text{sur}\ Y_E",
       "Complete local expression for rechecking C's added T overbar; the proposed ordinary T is high confidence.")
second("b32", "struck passage|insertion|C/H word difference|low-confidence departure", [995, 2020, 1560, 2150],
       r"\deleted{avec \unsure{de} la}\ \inserted{une}\ \uline{structure}",
       "Every word of the cancellation, C's de doubt, the inserted replacement une, and the underline under structure.")
second("b33", "insertion", [500, 2110, 985, 2270],
       r"\text{produit}\ \inserted{par I,}\ \text{d'une}",
       "Inserted par I, including comma and complete curved leader into the gap after produit.")
second("b34", "struck passage|handwritten number", [275, 2255, 1040, 2345],
       r"T_0\ \text{sur}\ Y_0\subset T_0,\ \deleted{\text{par }I}",
       "Entire final line: all zero subscripts, disputed extra bar on final T_0, complete struck par I, and no terminal full stop.")
second("b35", "margin note|handwritten number", [15, 2280, 90, 2345],
       "24",
       "Entire bottom-left foliation in thinner writing; attribution uncertain.")

data["crops"] = [
    {"file": crop_meta[name]["file"], "box": crop_meta[name]["box"],
     "phase": "first", "viewed": True}
    for name in crop_names
]

# Local consistency checks only; no TeX compiler or OCR is invoked.
tex = TEX.read_text()
def norm(s):
    return re.sub(r"\s+", "", s)
for entry in data["changes"]:
    assert norm(entry["final"]) in norm(tex), (
        "Final reading missing from proposed TeX", entry["place"], entry["final"]
    )
for entry in data["marks"]:
    assert norm(entry["reading"]) in norm(tex), (
        "Mark reading missing from proposed TeX", entry["context"]
    )

def macro_marks(source):
    """Read literal unsure/illegible macros, honoring escaped literal braces."""
    found = []
    rx = re.compile(r"\\(?:unsure|illegible)\{")
    for m in rx.finditer(source):
        depth, i = 1, m.end()
        while depth and i < len(source):
            if source[i] == "\\" and i + 1 < len(source) and source[i+1] in "{}":
                i += 2
                continue
            if source[i] == "{":
                depth += 1
            elif source[i] == "}":
                depth -= 1
            i += 1
        assert depth == 0
        found.append(source[m.start():i])
    return found

c_marks = macro_marks((PACKET / "C.tex").read_text())
assert sorted(c_marks) == sorted(entry["mark"] for entry in data["marks"]), (
    c_marks, [entry["mark"] for entry in data["marks"]]
)

depth = 0
i = 0
while i < len(tex):
    if tex[i] == "\\" and i + 1 < len(tex) and tex[i+1] in "{}":
        i += 2
        continue
    if tex[i] == "{":
        depth += 1
    elif tex[i] == "}":
        depth -= 1
        assert depth >= 0, i
    i += 1
assert depth == 0, depth
allowed_kinds = {
    "misread word", "misread symbol or index", "omission", "text not on the page",
    "deletion state (struck given live or live given struck)", "insertion or placement",
    "abbreviation expanded or spelling modernised", r"readable ink left as \ill{}",
    "drawing or diagram", "other",
}
assert all(x["kind"] in allowed_kinds for x in data["changes"])
assert len(data["crops"]) == 26
assert len(data["marks"]) == 9
OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({
    "output": str(OUT), "changes": len(data["changes"]), "marks": len(data["marks"]),
    "inventory": len(data["inventory"]), "doubts": len(data["doubts"]),
    "second_boxes": len(data["second_boxes"]), "crops": len(data["crops"]),
    "tex_braces_balanced": True, "all_final_readings_present": True,
}, ensure_ascii=False))
