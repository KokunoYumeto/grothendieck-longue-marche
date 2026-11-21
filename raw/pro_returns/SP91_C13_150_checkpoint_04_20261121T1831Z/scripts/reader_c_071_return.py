"""First-pass scan071 assembly. All returned files are replaced atomically."""
from pathlib import Path
import collections
import csv
import json
import os

EDITION = Path(__file__).resolve().parents[1]
ROOT = EDITION.parent
C = (ROOT / "input/SP91_C13_150_texts/pages/150_scan071.tex").read_text()
H = (ROOT / "input/SP91_C13_150_texts/hua/hua_150_scan071.tex").read_text()
CROPS = json.loads((EDITION / "scripts/reader_c_071_crop_manifest.json").read_text())
CP = {i+1: crop for i, crop in enumerate(CROPS)}

def atomic_text(path, text):
    temporary = path.with_name(path.name + ".tmp")
    with temporary.open("w", encoding="utf-8", newline="\n") as f:
        f.write(text)
        f.flush()
        os.fsync(f.fileno())
    os.replace(temporary, path)

TEX = r"""\scanpage{71}
\mspage{31}
satisfaisant les conditions a) c), \inserted{d)} de p. 28.
A-t-on aussi la condition b) de p. 28
\[
\Sigma_{ik}\cap\Sigma_{jk}=\varnothing\quad\hbox{si }i,j<k,\quad
i,j\ \hbox{non comparables ?}
\]
Si on avait $x\in\Sigma_{ik}\cap\Sigma_{jk}\inserted{\subset\Sigma_k}$,
alors on aurait deux éléments $\unsure{x_i}$ et $x_j$ de $\Sigma$,
au dessus de $i$ et $j$ respectivement, qui sont $<x$
(au dessus de $k$), donc (comme $\Sigma_{<x}$ est tot\textsuperscript{t} ordonné)
\deleted{\unsure{On aurait|on aurait}} $x$ et $y$ seraient comparables, donc aussi
$i$ et $j$, absurde.

\uline{Conséquence} \unsure{Les|les} structures ``déploiements
équisinguliers de stratifications, indexés par $I$'',
décrites \unsure{\deleted{dans}|dans} la p. 28, équivalent à la structure suivante :

\margin{\unsure{si|et} les comp. connexes des $\Sigma_i$ sont de dim finie...}

\textcircled{a} Un \deleted{$\Sigma$} espace top. ordonné $\Sigma$,
satisfaisant \unsure{aux|\deleted{aux}} conditions a) b) c) et 1°) de la page 27,
et \uline{de plus} : la condition que, \deleted{\unsure{pour tout}}
posant $\widetilde I=\pi_0(\Sigma)$, on ait, pour
$i,j\in\widetilde I$,
% Source-position: a detached dark point lies just above the tilde of this I; its role is unassigned.
$i<j$, que le morphisme d'immersion
propre \inserted{bordant} $\Sigma_{ij}\overset{b_{ij}}{\unsure{\longrightarrow|\mathrel{-}}}\Sigma_j$ soit
\uline{mono}

\textcircled{b} Une application strictement croissante
(pas néc. surjection)
\[
\widetilde I\longrightarrow I
\]
\margin{70}
"""

atomic_text(EDITION / "reader_returns/150_scan071.tex", TEX)

OUT = {
    "scan": "071", "reader": "reader_c", "line_count": 23,
    "changes": [], "decisions": [], "inventory": [], "doubts": [],
    "notes": [], "check_events": [], "notation": [], "abbreviations": [],
    "hand_log": [], "audit_boxes": [], "crops": CROPS, "unresolved": [],
}

def change(place, c, h, final, ac, ah, kind, category, crop, confidence, evidence,
           consequence="", marked=False, box=None):
    if c:
        assert c in C, ("C quotation absent", c)
    if h:
        assert h in H, ("H quotation absent", h)
    item = CP[crop] if crop else None
    OUT["changes"].append({
        "id": f"071-{len(OUT['changes'])+1:02d}",
        "place": place, "C": c, "H": h, "final": final,
        "against_C": ac, "against_H": ah, "kind": kind,
        "error_category": category, "marked_in_H": marked,
        "confidence": confidence, "evidence": evidence,
        "crop": item["file"] if item else "page",
        "box": box if box is not None else item["box"],
        "mathematical_consequence": consequence,
    })

change("first line, raised d) after c),",
       r"c), \inserted{d)} de p. 28.", r"c), d) de p.~28.",
       r"c), \inserted{d)} de p. 28.",
       False, True, "insertion or placement", "Insertions put in the wrong place", 1, "high",
       "The d has a closed lower oval and an ascending stem, followed by its own closing parenthesis. Both are above the c) baseline, after the surviving comma and before de. The comma below c) and the final point after 28 remain visible.")
change("second line, opening words",
       "A-t-on", "Montrons", "A-t-on",
       False, True, "misread word", "Words", 2, "high",
       "The initial letter has two tall sides and a crossbar. A detached short dash follows it, then a tall crossed t, another detached dash, and the low o/n run.")
change("opening displayed condition, terminal punctuation",
       r"non comparables ?", r"non comparables.", r"non comparables ?",
       False, True, "misread symbol or index", "Symbols and indices", 3, "high",
       "At the right edge, comparables continues onto a short lower baseline. After the final letters stands a curved upper hook with a separate dark point below it, forming the written question mark.",
       "The manuscript frames the displayed condition as a question.")
change("x-membership formula, raised subset expression",
       r"x\in\Sigma_{ik}\cap\Sigma_{jk}\subset\Sigma_k",
       r"x\in\Sigma_{ik}\cap\Sigma_{jk}\subset\Sigma_k",
       r"x\in\Sigma_{ik}\cap\Sigma_{jk}\inserted{\subset\Sigma_k}",
       True, True, "insertion or placement", "Insertions put in the wrong place", 4, "high",
       "The subset sign and smaller Sigma-k are above and to the right of the baseline Sigma-jk. The comma remains below them after Sigma-jk. The raised expression attaches before that comma. The written k forms have joined h-like arms here; the same page also supplies a more angular upright k in the opening inequality.")
change("after the x-membership formula",
       "alors on aurait", "donc on aurait", "alors on aurait",
       False, True, "misread word", "Words", 5, "high",
       "A small oval a precedes a tall closed l loop. The following o-shaped rise and low r/s return complete alors; on aurait follows on the same line.")
change("first au dessus, after de Sigma",
       "au dessus de", "au-dessus de", "au dessus de",
       False, True, "abbreviation expanded or spelling modernised", "Abbreviations expanded, spelling modernised", 7, "high",
       "The short low au run is followed by a blank interval before the looped d of dessus. There is no intervening hyphen. The following de is separately written.")
change("second au dessus, in the parenthesis after <x",
       "au dessus de", "au-dessus de", "au dessus de",
       False, True, "abbreviation expanded or spelling modernised", "Abbreviations expanded, spelling modernised", 8, "high",
       "The opening parenthesis is followed by the low au run, a blank gap and dessus. No separate hyphen appears in that gap. The words de k continue on the following main baseline.")
change("cancelled opening of the line before x et y",
       r"\deleted{on aurait}", r"\struck{on aurait}",
       r"\deleted{\unsure{On aurait|on aurait}}",
       True, True, "misread word", "Words", 10, "medium",
       "The first cancelled oval is tall and extends above and below the crossing line, favouring capital O. The following n and the low letters of aurait are partly masked by the long straight strike. The capital/lowercase alternative remains in place; the live x et y follows the strike.")
change("after the underlined Conséquence, initial letter",
       r"\uline{Conséquence} les structures", r"\emph{Conséquence} Les structures",
       r"\uline{Conséquence} \unsure{Les|les} structures",
       True, False, "misread word", "Words", 11, "medium",
       "The first letter has a long straight upright and a broad angular foot running right into the low e/s group. That contour favours capital L. The case alternative is retained because the tall cursive lowercase form is not wholly excluded by the stroke.")
change("before déploiements, opening quotation",
       "``déploiements", "« déploiements", "``déploiements",
       False, True, "misread symbol or index", "Symbols and indices", 11, "high",
       "Two small dark strokes stand high before the d of déploiements. They are preserved as the manuscript's paired high quotation marks.")
change("second line of the consequence, indexés",
       "indexés par", "indexées par", "indexés par",
       False, True, "misread word", "Words", 12, "high",
       "After the dotted initial i, the n run, tall d and crossed x, one accented e is followed by a low return and the long terminal s stroke. The crop does not expose a second e between that accented e and the terminal stroke.")
change("after I, closing quotation",
       r"$I$'',", r"$I$ »,", r"$I$'',",
       False, True, "misread symbol or index", "Symbols and indices", 13, "high",
       "Two short parallel raised strokes follow I. A separate low comma stands farther to the right before décrites.")
change("décrites dans la p. 28, state of dans",
       r"\deleted{dans}", "décrites dans la p.~28",
       r"\unsure{\deleted{dans}|dans}",
       False, True, "deletion state", "Struck text", 13, "low",
       "The d's oval and upright remain visible, followed by a long joined stroke along the low letters. That long stroke coincides with the word's baseline; its independence as a cancelling stroke cannot be securely isolated. The cancelled reading leads as in C, with the live state retained explicitly.")
change("oblique left margin, initial group M0624",
       r"\unsure{et|si}", r"\marginal{Si les",
       r"\unsure{si|et}",
       True, True, "misread word", "Words", 14, "medium",
       "The initial group has two short joined stems and no separately tall crossed t. It favours si, but the small joined shape leaves et open. Its case is kept lower in the tentative reading; H's note describes the whole marginal reading as uncertain.",
       marked=True)
change("oblique margin, first unread word of H",
       "les comp. connexes", r"les \ill{} \ill{}", "les comp. connexes",
       False, True, r"readable ink left as \ill{}", "Readable ink left as illegible", 14, "high",
       "After les, a low c/om run ends in a descending p and a separate dark stop. This row records comp.; the following word is recorded separately.",
       marked=True)
change("oblique margin, connexes",
       "connexes des", r"\ill{} \ill{} des", "connexes des",
       False, True, r"readable ink left as \ill{}", "Readable ink left as illegible", 14, "high",
       "The next marginal baseline begins with an open c, followed by low o/n/n runs, a visible crossing at x and a long e/s ending before the separate des. This row concerns H's second illegible word.",
       marked=True)
change("oblique margin, sont",
       r"$\Sigma_i$ sont de", r"$\Sigma_i$ \ill{} de", r"$\Sigma_i$ sont de",
       False, True, r"readable ink left as \ill{}", "Readable ink left as illegible", 14, "high",
       "After Sigma-i, a small curled s is followed by the joined o/n run and a tall angular terminal t; the following de has its own looped d.",
       marked=True)
change("oblique margin, dim without abbreviation point",
       "dim finie", r"dim.\ finie", "dim finie",
       False, True, "abbreviation expanded or spelling modernised", "Abbreviations expanded, spelling modernised", 14, "high",
       "The d/i/m strokes end in a low return. A blank interval separates that return from the tall f of finie; no point stands in the interval.",
       marked=True)
change("oblique margin, terminal points",
       "dim finie.", r"dim.\ finie\ldots", "dim finie...",
       True, False, "misread symbol or index", "Symbols and indices", 14, "high",
       "Three dark separated marks follow finie: a first compact point, an elongated middle mark and a final compact point. All three are retained; the dim punctuation is handled separately.",
       marked=True)
change("circled-a paragraph, cancelled Sigma after Un",
       r"\deleted{$\Sigma$}", r"\struck{\ill{}}",
       r"\deleted{$\Sigma$}",
       False, True, r"readable ink left as \ill{}", "Readable ink left as illegible", 15, "high",
       "The cancelled sign retains its upper horizontal stroke, angular middle turn and lower horizontal stroke. Additional oblique ink crosses that Sigma contour, which remains readable between Un and espace.",
       marked=True)
change("satisfaisant aux conditions, aux state",
       "satisfaisant aux conditions", r"satisfaisant \struck{aux} conditions",
       r"satisfaisant \unsure{aux|\deleted{aux}} conditions",
       False, True, "deletion state", "Struck text", 16, "medium",
       "The first small oval and the joined u/x run are visible. A heavy line follows that run, but no independently protruding cancelling stroke can be separated from the letter joins. The live word leads, while its struck state remains an explicit alternative.")
change("between la condition and que, H's extra cancellation",
       "la condition que", r"la condition \struck{\ill{}} que", "la condition que",
       False, True, "text not on the page", "Text that is not on the page", 17, "high",
       "The condition crop shows the complete final n return and clear space after it. The next line begins with que, followed by its comma and the actual pour tout cancellation (p18). No intervening cancelled group is visible at this source position.",
       marked=True)
change("membership in I-tilde, detached foreground point",
       r"$i,j\in\widetilde I$", r"$i,j\in\widetilde I$",
       r"$i,j\in\widetilde I$ % Source-position: a detached dark point lies just above the tilde of this I; its role is unassigned.",
       True, True, "omission", "Omissions", 20, "high",
       "A small dark point stands separately above the middle-right part of the tilde, within the whole membership-and-inequality crop. Its visible position is recorded in a TeX source-position comment, the inventory and the audit reading. No mathematical role is assigned to it.")
change("lower qualification, wording and position of d'immersion propre",
       "d'immersion\npropre bordant $\\Sigma_{ij}\\xrightarrow{b_{ij}}\\Sigma_j$ soit",
       r"\add{bordant} $\Sigma_{ij}\xrightarrow{b_{ij}}\Sigma_j$ soit une immersion propre",
       r"d'immersion propre \inserted{bordant} $\Sigma_{ij}\overset{b_{ij}}{\unsure{\longrightarrow|\mathrel{-}}}\Sigma_j$ soit",
       False, True, "insertion or placement", "Insertions put in the wrong place", 21, "high",
       "The main baseline writes d'immersion and then propre before the darker raised bordant and the map. The map is followed by soit, with mono on the following left baseline. H relocates the qualification after the map and gives une immersion propre there. This row concerns that wording and position; bordant's insertion state and the map's endpoint contour are recorded separately.")
change("raised bordant after propre",
       "propre bordant", r"\add{bordant}", r"propre \inserted{bordant}",
       True, False, "insertion or placement", "Insertions put in the wrong place", 21, "high",
       "The b, o, r, d, a, n and crossed t are in darker ink on a higher baseline after propre and before the Sigma expression. The raised addition attaches after propre; it is retained as an insertion.")
change("lower parenthesis M0625, short form néc.",
       r"\unsure{pas néc.}", "pas nécessairement", "pas néc.",
       False, True, "abbreviation expanded or spelling modernised", "Abbreviations expanded, spelling modernised", 24, "high",
       "Pas has its descending p and low a/s run. The next group has a low n, an e with a separate accent above it, an open c and a distinct stop. These visible short-form letters resolve M0625 without expanding the abbreviation.")
change("lower parenthesis, final word",
       "surjection", "surjective", "surjection",
       False, True, "misread word", "Words", 24, "high",
       "The word has the long j descender, e/c run, tall t and dotted i, then a rounded o and a terminal n-shaped return before the closing parenthesis. That ending supports surjection.")
change("extreme lower-left foliation",
       r"\mspage{70}", "", r"\margin{70}",
       False, True, "omission", "Omissions", None, "high",
       "The lower-left corner carries a thin pale 70 in another unnamed hand. The 7 has a long upper stroke and descending diagonal; the following 0 is closed. C records the same digits; the attribution is documented separately from textual comparison.",
       box=[23,2306,79,2357])

OUT["decisions"] = [
    {
        "id": "M0623", "decision": "undecided", "reading": r"\unsure{x_i}",
        "evidence": "The dotted lower i is clear. The first letter has crossed x-like strokes, but additional retraced loops and dark overlaps conceal its older contour. The leading x_i is retained with its doubt. The adjacent second label has an exposed x crossing and a connected long j, supporting x_j independently of the expected pair.",
        "crop": CP[6]["file"], "box": CP[6]["box"], "confidence": "medium",
    },
    {
        "id": "M0624", "decision": "undecided", "reading": r"\unsure{si|et}",
        "evidence": "The small first marginal group consists of two short joined stems, without a separately tall crossed t. This favours si over et, but the compact shape leaves both readings open. The rest of the marginal note is substantially readable on the rotated crop.",
        "crop": CP[14]["file"], "box": CP[14]["box"], "confidence": "medium",
    },
    {
        "id": "M0625", "decision": "first", "reading": "pas néc.",
        "evidence": "The descending p and low a/s run give pas. The following short group has a low n, accented e, open c and separate stop. The written abbreviation is retained without expansion.",
        "crop": CP[24]["file"], "box": CP[24]["box"], "confidence": "high",
    },
]

def inventory(kind, position, reading, hand="his hand"):
    OUT["inventory"].append({
        "element": f"E{len(OUT['inventory'])+1:02d}",
        "kind": kind, "position": position, "first_words_or_objects": reading,
        "sheet_kind": "text", "hand": hand, "transcribed": "yes",
    })

inventory("margin note", "upper-left corner, above the main text", r"\mspage{31}")
inventory("text", "first two main baselines",
          "satisfaisant les conditions a) c), d) de p. 28. / A-t-on aussi la condition b) de p. 28")
inventory("insertion", "raised after c), in the first line", r"\inserted{d)}")
inventory("display", "opening displayed question, with a short right-edge word continuation",
          r"\Sigma_{ik}\cap\Sigma_{jk}=\varnothing \quad\hbox{si }i,j<k,\quad i,j\ \hbox{non comparables ?}")
inventory("text", "main baselines 4–9, the paragraph beginning Si on avait",
          r"Si on avait $x\in\Sigma_{ik}\cap\Sigma_{jk}$")
inventory("insertion", "above/right of Sigma_jk in the x-membership expression, before the baseline comma",
          r"\inserted{\subset\Sigma_k}")
inventory("deletion", "start of main baseline 8, immediately before live x et y",
          r"\deleted{\unsure{On aurait|on aurait}}")
inventory("text", "middle paragraph headed by underlined Conséquence, four main baselines",
          r"\uline{Conséquence} \unsure{Les|les} structures")
inventory("deletion", "between décrites and la p. 28; strike state remains open",
          r"\unsure{\deleted{dans}|dans}")
inventory("margin note", "four oblique baselines in the lower-left margin beside the consequence and circled a",
          r"\unsure{si|et} les comp. connexes des $\Sigma_i$ sont de dim finie...")
inventory("text", "circled-a paragraph, main baselines 14–20 including its inline formulas",
          r"\textcircled{a} Un ... espace top. ordonné $\Sigma$")
inventory("deletion", "between Un and espace in circled a", r"\deleted{$\Sigma$}")
inventory("deletion", "aux before conditions; live/struck state remains open",
          r"\unsure{aux|\deleted{aux}}")
inventory("deletion", "after que, and before posant",
          r"\deleted{\unsure{pour tout}}")
inventory("drawing", "small detached point above the tilde of I in i,j membership",
          "One detached dark point; preserved by the exact source-position comment beside the membership formula, without an assigned role.")
inventory("insertion", "raised darker word between propre and the lower Sigma map",
          r"\inserted{bordant}")
inventory("text", "circled-b paragraph and following parenthesis",
          r"\textcircled{b} Une application strictement croissante (pas néc. surjection)")
inventory("display", "final centered map", r"\widetilde I\longrightarrow I")
inventory("margin note", "extreme lower-left foliation", r"\margin{70}", "another unnamed hand")

def doubt(place, reading, alternatives, confidence, reason):
    assert reading in TEX, ("Doubt not present in TeX", reading)
    OUT["doubts"].append({
        "place": place, "reading": reading, "alternatives": alternatives,
        "confidence": confidence, "reason": reason,
    })

doubt("element pair, first label M0623", r"\unsure{x_i}",
      "x_i, with the retraced older contour unresolved", "medium",
      "Crossed x-like strokes and a dotted lower i are visible, but the additional dark loops prevent a confident account of all older ink.")
doubt("cancelled opening before x et y", r"\unsure{On aurait|on aurait}",
      "On aurait; on aurait; low letters partly covered by the strike", "medium",
      "The tall initial oval favours capital O; the cancellation masks much of the n and the following low letter run.")
doubt("initial word after Conséquence", r"\unsure{Les|les}",
      "Les; les", "medium",
      "The tall straight upright and broad angular foot favour capital L, while the tall cursive lowercase alternative remains possible.")
doubt("dans after décrites", r"\unsure{\deleted{dans}|dans}",
      "cancelled dans; live dans", "low",
      "The long stroke coincides with the joined baseline and cannot be independently established as a strike.")
doubt("first marginal group M0624", r"\unsure{si|et}",
      "si; et", "medium",
      "Two short joined stems favour si, but the small shape remains insufficiently separated to resolve the alternatives.")
doubt("aux before conditions", r"\unsure{aux|\deleted{aux}}",
      "live aux; cancelled aux", "medium",
      "The heavy joined run can belong to the letters themselves; a distinct cancellation stroke is not isolated.")
doubt("cancelled phrase before posant", r"\unsure{pour tout}",
      "pour tout, with masked low letters", "medium",
      "The p descender and two t uprights survive, but the crossing hides portions of the low letters.")
doubt("detached point above the tilde in the membership formula",
      "% Source-position: a detached dark point lies just above the tilde of this I; its role is unassigned.",
      "visible point with unassigned role; no mathematical interpretation added", "low",
      "The point is separately visible in the formula crop, but the source does not establish its role. Its exact position is retained by a comment and audit record.")
doubt("lower map labelled b_ij, terminal contour",
      r"\unsure{\longrightarrow|\mathrel{-}}",
      "headed shaft; unheaded shaft with dark endpoint/stub", "medium",
      "The endpoint is a compact dark point or stub with no independently exposed two-sided V. The arrow reading leads as in both drafts; the unheaded contour remains explicit.")

OUT["notes"] = [
    {
        "id": "150-071-N01",
        "text": "The sheet carries the author's dark 31 at upper left and a thin pale foliation 70 in another unnamed hand at lower left. The main text continues with a reference to conditions a), c), and raised d) on p. 28. Two later references repeat p. 28, and circled a also names a), b), c), 1°) and page 27.",
    },
    {
        "id": "150-071-N02",
        "text": "The manuscript asks A-t-on aussi la condition b) and ends the displayed intersection condition with a question mark. It then gives an argument beginning Si on avait and ending absurde. The paragraph first writes the element labels x_i and x_j, with the first heavily retraced, and later writes x et y after a cancellation. Those local labels are retained as written; no identification or repair is supplied, and the argument has not been independently checked.",
    },
    {
        "id": "150-071-N03",
        "text": "The opening intersection expression has a raised subset-Sigma_k addition attached before its baseline comma. The main paragraph also writes Sigma_<x est tot with a raised t ordonné. The abbreviation remains literal. The k forms in the formulas sometimes have joined h-like arms; the same sheet supplies an angular k in i,j<k. This is a report of local letter shapes, without a mathematical substitution.",
    },
    {
        "id": "150-071-N04",
        "text": "Under Conséquence, the author calls the described déploiements équisinguliers de stratifications, indexés par I equivalent to the following structure. The first word after the heading has a capital-shaped L, and the state of dans later in that paragraph remains open. The marginal note reads si or et, then les comp. connexes des Sigma_i sont de dim finie, followed by three separate final marks. The note's introductory group remains unresolved.",
    },
    {
        "id": "150-071-N05",
        "text": "Circled a describes an espace top. ordonné Sigma, recalls conditions on page 27, and adds a condition introduced through I-tilde=pi_0(Sigma). The source places d'immersion propre before a darker raised bordant and the map from Sigma_ij to Sigma_j; mono is underlined on the next left baseline. The label b_ij has no separate underline: the short lower bar belongs to j's foot. The shaft's point-like endpoint leaves its head contour open.",
    },
    {
        "id": "150-071-N06",
        "text": "A detached dark point stands above the tilde of I in the i,j membership formula. Its position is recorded in a TeX source-position comment, an inventory entry and the whole-formula audit reading. The point has no assigned mathematical role. The live/struck state of aux is also left explicit, and no extra cancelled word is visible between condition and que.",
    },
    {
        "id": "150-071-N07",
        "text": "Circled b gives Une application strictement croissante, followed by the written parenthesis pas néc. surjection and a headed map from I-tilde to I. The abbreviation néc. is resolved from its letters, accent and point; surjection retains its visible ending. These are statements of what the manuscript writes. No proof check or conditional theorem has been supplied by this reading.",
    },
]
OUT["check_events"] = []

OUT["notation"] = [
    {
        "form": r"\Sigma_{ik},\Sigma_{jk},\Sigma_k",
        "meaning": "Indexed Sigma expressions in the author's opening condition and following membership formula.",
        "evidence": "The first-factor and raised-addition k forms have joined h-like arms; the opening i,j<k supplies a more angular upright k on the same sheet.",
        "places": "071: opening display and x-membership line, p03–p04",
    },
    {
        "form": r"\Sigma_{<x}",
        "meaning": "The object described by the author as tot with raised t ordonné.",
        "evidence": "A lowered left-angle sign and x follow the Sigma's lower stroke inside the parenthetical clause.",
        "places": "071: parenthesis in the first argument, p09",
    },
    {
        "form": r"\widetilde I=\pi_0(\Sigma)",
        "meaning": "The equality introduced after posant in circled a.",
        "evidence": "A wavy mark lies above capital I; a two-stroke equality follows, then pi with a small lowered closed zero and parenthesized Sigma.",
        "places": "071: circled-a definition, p19",
    },
    {
        "form": r"\Sigma_{ij}\overset{b_{ij}}{\unsure{\longrightarrow|\mathrel{-}}}\Sigma_j",
        "meaning": "The lower map expression named in the author's immersion qualification.",
        "evidence": "The label contains a looped b, dotted lower i and long j with a leftward foot. The shaft ends in a compact point/stub; no separate label underline or exposed V is isolated.",
        "places": "071: lower circled-a map, p22",
    },
    {
        "form": r"\widetilde I\longrightarrow I",
        "meaning": "The displayed map following the author's circled-b wording.",
        "evidence": "The source I carries a wave, and the right end of the shaft has an upper arm and a lower dark point. The target is plain I with a broad upper bar.",
        "places": "071: final display, p25",
    },
    {
        "form": "detached point above a tilde",
        "meaning": "Unassigned visible ink; no mathematical role inferred.",
        "evidence": "A small separate dark point lies above the middle-right part of the tilde in the i,j membership expression.",
        "places": "071: membership in I-tilde, p20",
    },
]

OUT["abbreviations"] = [
    {"written": "p.", "expansion": "page", "places": "071: three references to p. 28"},
    {"written": "comp.", "expansion": "composantes", "places": "071: oblique margin, p14"},
    {"written": "dim", "expansion": "dimension", "places": "071: oblique margin, p14; no written point after dim"},
    {"written": "top.", "expansion": "topologique", "places": "071: espace top. ordonné in circled a"},
    {"written": r"tot\textsuperscript{t}", "expansion": "totalement", "places": "071: first parenthetical ordering clause, p09"},
    {"written": "néc.", "expansion": "nécessairement", "places": "071: final parenthesis, p24"},
    {"written": "mono", "expansion": "monomorphisme or adjectival monomorphique; the short form itself does not fix the grammatical expansion", "places": "071: underlined end of circled a"},
]

OUT["hand_log"] = [
    {
        "habit": "Some mathematical k forms have joined h-like arms.",
        "places": "071: both factors in the opening question and the following membership expression; raised Sigma_k",
        "scope": "These compact k forms contrast locally with the more angular upright k in i,j<k; each occurrence was inspected.",
        "witness_errors": "No letter substitution is imposed on either witness from this shape alone.",
    },
    {
        "habit": "A long j descender can join the preceding x or Sigma and return far left.",
        "places": "071: second element label, i,j membership, b_ij label and Sigma indices",
        "scope": "At the second element label, the exposed four-arm x crossing remains distinct from the connected j; the earlier whole-page impression was less clear.",
        "witness_errors": "Both witnesses' x_j is supported by the crop. The first x_i stays doubtful because of retracing.",
    },
    {
        "habit": "Long low letter joins can resemble cancellation strokes.",
        "places": "071: dans and aux, p13 and p16",
        "scope": "The independent strike state remains open at these two places; the clear long strikes through On/on aurait and pour tout were separately inspected.",
        "witness_errors": "C cancels dans and leaves aux live; H leaves dans live and cancels aux. Both state doubts are retained in place.",
    },
    {
        "habit": "Large initial O/L contours leave local case questions.",
        "places": "071: cancelled On/on aurait and Les/les after Conséquence",
        "scope": "Only these two locally enlarged initial forms are covered by this observation; no general case substitution is made.",
        "witness_errors": "Both drafts give lowercase on in the cancellation; C has les and H Les after the heading.",
    },
    {
        "habit": "Small detached accents and abbreviation points must be counted separately.",
        "places": "071: indexés, néc., comp., dim and tot with raised t",
        "scope": "The accent in néc. and the three final marginal marks are explicit; dim has no separate stop; tot has a raised final t.",
        "witness_errors": "H expands néc. and supplies a point after dim; C gives only one final point after finie.",
    },
    {
        "habit": "A raised darker word can occupy the gap before an inline formula.",
        "places": "071: bordant after d'immersion propre, p21–p22",
        "scope": "The visible placement supports attachment after propre; the surrounding qualification is kept in its written order.",
        "witness_errors": "C prints bordant as ordinary baseline text; H records its insertion but relocates the immersion wording after the map.",
    },
    {
        "habit": "Endpoint thickenings vary from a compact point to a separable head.",
        "places": "071: b_ij shaft and final I-tilde-to-I map",
        "scope": "The b_ij endpoint remains ambiguous; the final map's upper arm and lower point support its head.",
        "witness_errors": "Both drafts give an arrow for b_ij without local contour doubt; their final headed map agrees with the crop.",
    },
    {
        "habit": "Letters can be retraced without a recoverable different predecessor.",
        "places": "071: first x_i and initial st of strictement",
        "scope": "The older contour at x_i is unresolved; strictement remains readable as a full word despite reworked initial strokes.",
        "witness_errors": "No additional deleted letter is invented at either place.",
    },
]

def audit(kind, reading, crop=None, box=None, comment=""):
    coords = box if box is not None else CP[crop]["box"]
    row = {
        "box": f"B{len(OUT['audit_boxes'])+1:02d}", "kind": kind,
        "x0": coords[0], "y0": coords[1], "x1": coords[2], "y1": coords[3],
        "reading": reading,
    }
    if comment:
        row["comment"] = comment
    OUT["audit_boxes"].append(row)

audit("handwritten number", r"\mspage{31}", box=[28,28,79,78])
audit("insertion", r"a) c), \inserted{d)} de p. 28.", crop=1)
audit("lexical disagreement", "A-t-on", crop=2,
      comment="The tiny upper clipped fragment belongs to the preceding main baseline.")
audit("handwritten number", "de p. 28", box=[1300,177,1538,261])
audit("lexical disagreement",
      r"$\Sigma_{ik}\cap\Sigma_{jk}=\varnothing\quad\hbox{si }i,j<k,\quad i,j\ \hbox{non comparables ?}$",
      crop=3,
      comment="Comparables wraps at the right edge. The small lower fragment belongs to the raised Sigma_k addition on the next baseline, separately boxed.")
audit("insertion",
      r"$x\in\Sigma_{ik}\cap\Sigma_{jk}\inserted{\subset\Sigma_k}$,",
      crop=4,
      comment="Whole expression with its raised addition and baseline comma. Upper clipped strokes belong to the preceding displayed condition; the right clipped al-like group begins alors.")
audit("insertion", r"$\inserted{\subset\Sigma_k}$",
      box=[1071,357,1179,424],
      comment="Individual raised addition. The small lower-right fragment is the top of the following alors, on the baseline below.")
audit("lexical disagreement", "alors on aurait", crop=5,
      comment="The upper-left fragment belongs to the raised Sigma_k addition.")
audit("doubtful formula", r"$\unsure{x_i}$ et $x_j$ de $\Sigma$,", crop=6)
audit("lexical disagreement", "au dessus de", crop=7)
audit("lexical disagreement", r"$<x$ (au dessus", crop=8)
audit("struck passage", r"\deleted{\unsure{On aurait|on aurait}} $x$ et $y$", crop=10)
audit("lexical disagreement", r"\unsure{Les|les} structures ``déploiements",
      box=[663,993,1640,1111],
      comment="The left underlined heading lies outside this targeted rectangle; its text is independently read on the full-resolution half.")
audit("lexical disagreement", "indexés par", crop=12,
      comment="The tiny lower fragment belongs to the following baseline.")
audit("struck passage",
      r"$I$'', décrites \unsure{\deleted{dans}|dans} la p. 28, équivalent",
      crop=13,
      comment="Upper clipped letters belong to équisinguliers on the preceding baseline; the lower tip belongs to suivante below.")
audit("struck passage", r"\unsure{\deleted{dans}|dans}",
      box=[835,1228,1016,1305])
audit("margin note",
      r"\margin{\unsure{si|et} les comp. connexes des $\Sigma_i$ sont de dim finie...}",
      crop=14,
      comment="Four oblique baselines; the first-pass evidence crop is rotated -43 degrees. Coordinates remain those of the original.")
audit("struck passage", r"\textcircled{a} Un \deleted{$\Sigma$} espace",
      crop=15,
      comment="Small upper and lower fragments belong to neighbouring main baselines.")
audit("struck passage", r"\unsure{aux|\deleted{aux}}",
      box=[608,1601,709,1648])
audit("handwritten number", "a) b) c) et 1°) de", box=[1099,1523,1637,1608])
audit("handwritten number", "la page 27,", box=[270,1691,667,1789],
      comment="Any small upper fragment belongs to satisfaisant on the preceding baseline.")
audit("lexical disagreement", ": la condition", crop=17,
      comment="The following main baseline begins que; no cancelled group intervenes at this source position.")
audit("struck passage", r"\deleted{\unsure{pour tout}}",
      box=[433,1787,736,1887],
      comment="Individual cancellation; que and posant lie outside this targeted rectangle.")
audit("handwritten number", r"$\widetilde I=\pi_0(\Sigma)$,", crop=19)
audit("doubtful formula",
      r"$i,j\in\widetilde I$, $i<j$, % Source-position: a detached dark point lies just above the tilde of this I; its role is unassigned.",
      crop=20,
      comment="Whole membership-and-inequality expression including the separate point. Lower clipped stems belong to the immersion qualification below.")
audit("lexical disagreement", r"d'immersion propre \inserted{bordant}",
      crop=21,
      comment="Upper clipped ait, pour and index fragments belong to the preceding main baseline.")
audit("insertion", r"\inserted{bordant}", box=[913,1954,1139,2028])
audit("doubtful formula",
      r"$\Sigma_{ij}\overset{b_{ij}}{\unsure{\longrightarrow|\mathrel{-}}}\Sigma_j$ soit",
      crop=22,
      comment="The upper clipped descender belongs to morphisme on the preceding baseline.")
audit("lexical disagreement", "(pas néc. surjection)", crop=24,
      comment="Upper clipped circled-b/application strokes belong to the preceding baseline; the lower-right I-tilde and partial shaft belong to the final map, separately boxed.")
audit("doubtful formula", r"$\widetilde I\longrightarrow I$", crop=25,
      comment="The upper curved fragment is the preceding parenthesis. A tiny detached point below the shaft is recorded by position; no role is assigned to it.")
audit("handwritten number", r"\margin{70}", box=[23,2306,79,2357])

OUT["unresolved"] = [
    "The retraced older contour of the first x_i label.",
    "The capital/lowercase initial in cancelled On/on aurait, with some low letters masked.",
    "Les/les after the underlined Conséquence.",
    "The live/struck state of dans.",
    "The initial si/et of the marginal note.",
    "The live/struck state of aux.",
    "Masked low letters in cancelled pour tout.",
    "The role of the detached point above the tilde in the membership formula remains unassigned.",
    "The head contour of the shaft labelled b_ij.",
]

with (EDITION / "packets/150_scan071/diffs.tsv").open(newline="") as f:
    DIFFERENCES = list(csv.DictReader(f, delimiter="\t"))
OUT["coverage"] = {
    "whole_image_viewed": True,
    "halves_viewed": ["top", "bottom"],
    "all_tokens_read": True,
    "all_C_insertions_deletions_checked": True,
    "differences_considered": len(DIFFERENCES),
    "macro_only_differences_ignored": (
        "Equivalent underline/emphasis wrappers, hbox/text, empty-set commands for the same drawn glyph, spacing and nonbreaking spaces, "
        "and the circled-letter note accompanying H's (a)/(b) notation. State/placement differences in struck/add wrappers are recorded substantively. "
        "H's editorial page synopsis and explanatory notes are not inserted into the transcription. Its quoted authorial 31 agrees with C and the ink. "
        "C's foliation digits 70 agree with the ink; their other-hand attribution is documented separately and the macro change alone is excluded from C's textual count. "
        "Certainty-only additions remain in the doubts rather than being counted as textual changes."
    ),
    "visual_pass_detail": (
        "The original whole image and each full-resolution premade half were explicitly viewed once. Every one of the 25 saved first-pass crops was emitted and read, "
        "and the root independently inspected all 25. No OCR, external research, compilation or proof check was performed."
    ),
    "line_count_method": (
        "23 principal main-text/display baselines. The small right-edge continuation of comparables is retained within its opening display; "
        "the four oblique marginal baselines and the two page numbers are inventoried separately."
    ),
    "audit_coverage": (
        "31 preliminary boxes cover every insertion, cancellation or open cancellation state, the margin, all lexical disagreements and each lower-confidence departure from C. "
        "Author 31, all three references to 28, page 27, 1°), pi-zero and foliation 70 are covered. "
        "The whole first-label expression, raised intersection expression, membership formula with the detached point and ambiguous b_ij map are boxed in full. "
        "Individual tight boxes isolate the subset addition, dans, aux, pour tout and bordant. Source-position comments identify clipped neighbouring ink."
    ),
}
OUT["comparison_counts"] = {
    "rows": len(OUT["changes"]),
    "against_C": sum(row["against_C"] for row in OUT["changes"]),
    "against_H": sum(row["against_H"] for row in OUT["changes"]),
    "by_confidence": dict(collections.Counter(row["confidence"] for row in OUT["changes"])),
    "against_C_by_confidence": dict(collections.Counter(row["confidence"] for row in OUT["changes"] if row["against_C"])),
    "against_H_by_confidence": dict(collections.Counter(row["confidence"] for row in OUT["changes"] if row["against_H"])),
    "counting_rule": "Leading proposed candidate compared with each draft; equivalent TeX syntax and certainty-only differences are excluded. A feature quoted as neighbouring context is not counted again in that row.",
}

# Structural checks only; no compilation or mathematical validation.
with (EDITION / "packets/150_scan071/marks.tsv").open(newline="") as f:
    MARKS = list(csv.DictReader(f, delimiter="\t"))
assert [m["id"] for m in MARKS] == [d["id"] for d in OUT["decisions"]]
assert len(CROPS) == 25 and all((EDITION/crop["file"]).is_file() for crop in CROPS)
assert all(0 <= b["x0"] < b["x1"] <= 1678 and 0 <= b["y0"] < b["y1"] <= 2364 for b in OUT["audit_boxes"])
assert TEX.count(r"\inserted{") == sum(item["kind"] == "insertion" for item in OUT["inventory"])
assert TEX.count(r"\deleted{") == sum(item["kind"] == "deletion" for item in OUT["inventory"])
assert TEX.count(r"\unsure{") == len(OUT["doubts"]) - 1  # one source-position point, without an assigned formula role
assert len(OUT["audit_boxes"]) == 31
atomic_text(EDITION / "reader_returns/150_scan071.json", json.dumps(OUT, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({
    "tex": str(EDITION / "reader_returns/150_scan071.tex"),
    "json": str(EDITION / "reader_returns/150_scan071.json"),
    "counts": OUT["comparison_counts"],
    "decisions": len(OUT["decisions"]), "inventory": len(OUT["inventory"]),
    "doubts": len(OUT["doubts"]), "audit_boxes": len(OUT["audit_boxes"]),
    "crops": len(CROPS), "packet_differences": len(DIFFERENCES),
}, ensure_ascii=False, indent=2))
