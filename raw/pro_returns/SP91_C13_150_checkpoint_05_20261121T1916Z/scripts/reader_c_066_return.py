"""Assemble reader C's scan066 return from the individually inspected images.

This is a first-pass record, not a global page finalization or proof check.
All output replacements are atomic so checkpoints never capture partial files.
"""
from pathlib import Path
import collections
import csv
import json
import os

EDITION = Path(__file__).resolve().parents[1]
ROOT = EDITION.parent
C = (ROOT / "input/SP91_C13_150_texts/pages/150_scan066.tex").read_text()
H = (ROOT / "input/SP91_C13_150_texts/hua/hua_150_scan066.tex").read_text()
CROPS = json.loads((EDITION / "scripts/reader_c_066_crop_manifest.json").read_text())
CP = {i + 1: c for i, c in enumerate(CROPS)}

def atomic_text(path, text):
    temporary = path.with_name(path.name + ".tmp")
    with temporary.open("w", encoding="utf-8", newline="\n") as f:
        f.write(text)
        f.flush()
        os.fsync(f.fileno())
    os.replace(temporary, path)

TEX = r"""\scanpage{66}
d) \deleted{\unsure{a}} Les $\Sigma_j\hookrightarrow\Sigma_{ji}$ sont bordants, et si
$x\in\Sigma_i$, \deleted{les} \unsure{dans|donc} les $\Sigma_{ji}\ni x$ (\deleted{pour $j<i$}\inserted{indices}
\deleted{\unsure{tels que}}\deleted{$\Sigma$}\inserted{par l'ens}. $I_{<i,x}\overset{\mathrm{def}}{=}\{j\in I\mid j<i,\ \Sigma_{ji}\ni x\}$,
qui est totalement ordonné par b) sont
des sous-espaces-bords transversaux en $x$
--- i.e. les $\Sigma_{ji}$ $(j\in I_{<i})$ sont des
sous-espaces bords de $\Sigma_i$ \unsure{mutuell\({}^t\)}
transversaux.

e) $\Sigma_{\unsure{i|j}j}\xrightarrow{s_{ij}}\Sigma_i$ est transversal p.r. au système \unsure{trans}-
versal des morphismes bordants
$b_{\unsure{ik|ki}}:\Sigma_{\unsure{k}i}\longrightarrow\Sigma_i$

Si on pose
\[
\Sigma=\coprod_{i\in I}\Sigma_i
\]
\[
\Sigma^{<}(1)=\coprod_{\substack{i,j\in I\\i<j}}\Sigma_{ij}
\]
et $\uline{s},\uline{b}:\Sigma^{<}(1)\mathrel{-}\Sigma$ induits par les
$s_{ij},b_{ij}$, alors les conditions a) b) c)
signifient que $(\uline{s},\uline{b}):\Sigma^{<}(1)\longrightarrow\Sigma\unsure{\times|<}\Sigma$ est
inj. et a comme \deleted{\unsure{graphe}}\inserted{image} le graphe d'une
relation d'ordre \unsure{stricte|strict}, avec $\uline{b}:\Sigma^{<}(1)\longrightarrow\Sigma$
\inserted{immersion} propre, \deleted{et} que l'application \inserted{continue évidente} $\varphi:\Sigma^{\unsure{*}}\unsure{\ell|\deleted{\ell}}\longrightarrow\unsure{\deleted{\Sigma}I|I}$
est strict\({}^t\) croissante, et que pour \unsure{tt|$\forall$} $x\in\Sigma$,
l'application induite $\varphi:\Sigma_{<x}\mathrel{-}I_{<i}$ $(i=\varphi(x))$ est
injective, enfin que $\Sigma_{<x}$ est \unsure{tot.|tt.} ordonné.
\margin{65}
"""
atomic_text(EDITION / "reader_returns/150_scan066.tex", TEX)

OUT = {
    "scan": "066", "reader": "reader_c", "line_count": 23,
    "changes": [], "decisions": [], "inventory": [], "doubts": [],
    "notes": [], "check_events": [], "notation": [], "abbreviations": [],
    "hand_log": [], "audit_boxes": [], "crops": CROPS, "unresolved": [],
}

def change(place, c, h, final, ac, ah, kind, category, p, confidence, evidence,
           consequence="", marked=False):
    if c:
        assert c in C, ("C quotation absent", c)
    if h:
        assert h in H, ("H quotation absent", h)
    OUT["changes"].append({
        "id": f"066-{len(OUT['changes']) + 1:02d}", "place": place,
        "C": c, "H": h, "final": final,
        "against_C": ac, "against_H": ah, "kind": kind,
        "error_category": category, "marked_in_H": marked,
        "confidence": confidence, "evidence": evidence,
        "crop": CP[p]["file"], "box": CP[p]["box"],
        "mathematical_consequence": consequence,
    })

change("line 1, cancelled glyph before Les",
       r"\deleted{\unsure{a}}", "", r"\deleted{\unsure{a}}",
       False, True, "omission", "Struck text", 1, "low",
       "A separate compact a-like loop lies between d) and Les and is crossed by a dark stroke. The cancellation is visible; the underlying letter remains doubtful.")
change("line 2, word after cancelled les",
       "donc", "dans", r"\unsure{dans|donc}",
       True, False, "misread word", "Words", 3, "medium",
       "The word has an initial d loop, a low joined middle, and an angular descending return at the end. That ending favours s, as in the adjacent les, but the compressed middle and terminal return do not exclude donc.")
change("line 2, inserted word above cancelled pour j<i",
       r"\inserted{indices}", r"\add{indexés}", r"\inserted{indices}",
       False, True, "misread word", "Words", 4, "medium",
       "The interlinear word begins with dotted i, then n/d-like joined strokes, and ends with a low c/e/s-shaped run. Its short written form supports indices; there is no separate accent stroke over an e.")
change("line 2, cancelled range of pour j<i",
       r"\deleted{pour $j<i$}", r"\struck{pour $j$} \add{indexés} $j<i$",
       r"\deleted{pour $j<i$}\inserted{indices}",
       False, True, "deletion state", "Struck text", 4, "high",
       "One long crossing stroke passes through pour, j and the comparison group. Only one j occurs in this cancelled phrase; the final i remains at its right edge. The replacement word is written above this whole phrase.")
change("line 3, cancelled words before Sigma",
       r"\deleted{tels que}\deleted{$\unsure{\Sigma}$}",
       r"\struck{tels que l'on $\Sigma$}",
       r"\deleted{\unsure{tels que}}\deleted{$\Sigma$}",
       False, True, "text not on the page", "Text that is not on the page", 5, "medium",
       "The crossed baseline contains the tels-que group and then the angular Sigma. The l-apostrophe-ens-shaped material is above the baseline in the replacement; a separate underlying l'on group cannot be isolated. The crossing conceals some letters of tels que, so their reading remains marked.")
change("line 3, replacement above cancelled tels que/Sigma",
       r"\inserted{par l'ens}", "", r"\inserted{par l'ens}",
       False, True, "omission", "Omissions", 5, "medium",
       "Above the cancellation are a descending p-like initial with joined ar return, followed by a tall l, a small apostrophe and a low ens run. These words belong to the interlinear replacement and are kept in their short form.")
change("line 3, cancelled Sigma; certainty-only decision",
       r"\deleted{$\unsure{\Sigma}$}", r"\struck{tels que l'on $\Sigma$}",
       r"\deleted{$\Sigma$}",
       False, False, "other", "Other", 5, "high",
       "The upper horizontal, central diagonal bend and lower horizontal of capital Sigma are all visible around the crossing stroke. This resolves the local C uncertainty without changing its leading glyph; the surrounding word difference is recorded separately.")
change("line 3, stop to the right of the cancellation, before I",
       r"\inserted{par l'ens} $I", r"}. $I",
       r"\inserted{par l'ens}. $I",
       True, False, "omission", "Omissions", 5, "high",
       "A distinct dark rounded point stands to the right of the cancelled Sigma, beyond the end of its crossing stroke and before I. It survives outside the cancellation; no comma shape is visible.")
change("line 3, definition label",
       r"\mathrm{def}", r"\text{déf}", r"\mathrm{def}",
       False, True, "abbreviation expanded or spelling modernised",
       "Abbreviations expanded, spelling modernised", 6, "high",
       "The small raised label reads d-e-f. The area above its e has no separate accent stroke; the three-letter unaccented label is retained.")
change("line 4, closing parenthesis after b",
       "par b)) sont", "par b)) sont", "par b) sont",
       True, True, "text not on the page", "Text that is not on the page", 7, "high",
       "There is a single curved closing stroke between b and sont. Both drafts supply an additional close; the transcription retains the single written stroke without completing the earlier delimiter.")
change("line 7, short form before transversaux",
       "mutuellement", "mutuellement", r"\unsure{mutuell\({}^t\)}",
       True, True, "abbreviation expanded or spelling modernised",
       "Abbreviations expanded, spelling modernised", 8, "medium",
       "After the mutu/e run there are two tall l ascenders, a low compressed movement and a small raised terminal t-like loop. A full -ement sequence is not separately supported. The retained short form and its ending remain uncertain.")
change("lines 9–10, right-edge trans- and continuation",
       "trans-\nversal", "transversal", "\\unsure{trans}-\nversal",
       False, True, "abbreviation expanded or spelling modernised",
       "Abbreviations expanded, spelling modernised", 10, "medium",
       "The first line ends with the densely retraced trans group and a separate short horizontal stroke to its right. The next line begins versal. The local letter group stays doubtful, and the visible end-of-line hyphen is retained.")
change("line 10, des morphismes",
       "des morphismes", "de morphismes", "des morphismes",
       False, True, "misread word", "Words", 11, "high",
       "After the looped d there is a low joined ending that extends through e and an s-like return before morphismes. The final s is visible.")
change("line 10, state of bordants",
       "morphismes bordants", r"morphismes \struck{bordants}",
       "morphismes bordants",
       False, True, "deletion state", "Struck text", 11, "high",
       "The first b is heavily retraced, but the subsequent o/r/d/a/n/t/s forms are live. No separate cancellation stroke crosses the word.")
change("line 11, subscript of the b label",
       r"b_{ik}", r"b_{ki}", r"b_{\unsure{ik|ki}}",
       False, True, "misread symbol or index", "Symbols and indices", 12, "medium",
       "Immediately after b is a small detached dot and a low short stroke, followed by the k-like group. This favours i then k; the joined, retraced subscript is not sufficiently separated to suppress ki as an alternative.",
       "The leading written label is b_ik; the two drafts give opposite orders to its subscript.")
change("line 11, terminal punctuation of the b map",
       r"\longrightarrow\Sigma_i$", r"\to\Sigma_i$.",
       r"\longrightarrow\Sigma_i$",
       False, True, "text not on the page", "Text that is not on the page", 12, "high",
       "After the target Sigma and its dotted i there is blank paper. No separate terminal point is visible.")
change("display 1, punctuation after Sigma_i",
       r"\Sigma=\coprod_{i\in I}\Sigma_i",
       r"\Sigma=\coprod_{i\in I}\Sigma_i,",
       r"\Sigma=\coprod_{i\in I}\Sigma_i",
       False, True, "text not on the page", "Text that is not on the page", 13, "high",
       "The display ends at the dotted subscript i of the summand. Its dot belongs above the i; no comma follows the expression.")
change("displays 1 and 2, vertical disposition",
       "\\Sigma_i\n\\]\n\\[\n\\Sigma^{<}(1)",
       r"\Sigma_i,\qquad \Sigma^{*}(1)",
       "\\Sigma_i\n\\]\n\\[\n\\Sigma^{<}(1)",
       False, True, "insertion or placement", "Insertions put in the wrong place", 14, "high",
       "The second equality occupies a separate lower display baseline, with its two-line coproduct index below. The first equality is above it; the transcription keeps two stacked displays. The differing superscript is recorded separately.")
change("display 2, raised sign on Sigma",
       r"\Sigma^{<}(1)=\coprod", r"\Sigma^{*}(1)=\coprod",
       r"\Sigma^{<}(1)=\coprod",
       False, True, "misread symbol or index", "Symbols and indices", 14, "high",
       "The raised mark has a left-pointing junction and two rightward arms. Its lower arm joins the following opening parenthesis; no independent crossing arm is exposed.",
       "The displayed source notation retains the manuscript's locally angular superscript.")
change("line 15, raised sign in the s,b expression",
       r"\uline{s},\uline{b}:\Sigma^{<}(1)",
       r"\underline s,\underline b : \Sigma^{*}(1)",
       r"\uline{s},\uline{b}:\Sigma^{<}(1)",
       False, True, "misread symbol or index", "Symbols and indices", 15, "high",
       "A small two-arm left angle is visible immediately above the opening parenthesis. The lower arm is joined to that parenthesis, with no separate crossing diagonal.",
       "The same local angular source form is retained at this written occurrence.")
change("line 15, shaft from Sigma^<(1) to Sigma",
       r"\uline{s},\uline{b}:\Sigma^{<}(1)\longrightarrow\Sigma",
       r"\underline s,\underline b : \Sigma^{*}(1)\to\Sigma",
       r"\uline{s},\uline{b}:\Sigma^{<}(1)\mathrel{-}\Sigma",
       True, True, "misread symbol or index", "Symbols and indices", 15, "high",
       "The connector is one horizontal stroke ending in a small blunt/downturned thickening. There is no independently exposed upper-and-lower arrowhead; the literal unheaded shaft is preserved.")
change("line 17, raised sign in the (s,b) map",
       r"(\uline{s},\uline{b}):\Sigma^{<}(1)",
       r"(\underline s,\underline b) : \Sigma^{*}(1)",
       r"(\uline{s},\uline{b}):\Sigma^{<}(1)",
       False, True, "misread symbol or index", "Symbols and indices", 16, "high",
       "The superscript has the left vertex and two rightward arms seen in the preceding display. Its right-lower arm continues into the opening parenthesis. The connector farther right has a visible terminal head.",
       "The written source remains Sigma with a raised left-angle sign and argument 1.")
change("line 19, ending of ordre stricte",
       "stricte", "strict", r"\unsure{stricte|strict}",
       False, True, "misread word", "Words", 18, "medium",
       "The final tall t-like stroke has a long low rightward return. That return may carry the final e, but a separate e loop is not securely isolated. The leading stricte reading is retained with strict as an explicit alternative.")
change("line 19, word after the comma",
       "avec", "", "avec",
       False, True, "omission", "Omissions", 18, "medium",
       "After the comma and before the underlined b expression is a distinct low joined word group, with a small initial a-like component and a final open return. It reads avec; it is separate from the interlinear continue évidente below.")
change("line 19, raised sign in the lower b map",
       r"\uline{b}:\Sigma^{<}(1)", r"\underline b : \Sigma^{*}(1)",
       r"\uline{b}:\Sigma^{<}(1)",
       False, True, "misread symbol or index", "Symbols and indices", 19, "high",
       "Two short arms meet at a left vertex above the source Sigma. The lower arm is joined to the following parenthesis. The map's right endpoint has a solid pointed head, which is retained.",
       "This local source occurrence keeps the raised angle rather than replacing it by the draft's star.")
change("line 20, et after propre",
       r"\deleted{et}", "propre, et que", r"\deleted{et}",
       False, True, "deletion state", "Struck text", 20, "medium",
       "A rising dark stroke crosses the low e loop and the t group, extending across the word independently of its upright. The t bar joins the crossing, but the crossed extent supports the cancelled state; the following que is live.")
change("line 20, interlinear qualification of application",
       r"\inserted{continue évidente}", r"\add{\ill{}}",
       r"\inserted{continue évidente}",
       False, True, r"readable ink left as \ill{}", "Readable ink left as illegible", 21, "high",
       "The insertion has the co/n/t/i/n/u/e run followed by an accented initial e, v/i/d/e/n/t/e. A long curved leader ends after l'application, before phi, attaching the two words there.", marked=True)
change("line 20, raised material on the source Sigma, M0610",
       r"\unsure{\Sigma|\Sigma^{*}}", r"\varphi : \Sigma\to I",
       r"\Sigma^{\unsure{*}}",
       True, True, "misread symbol or index", "Symbols and indices", 21, "low",
       "A dark multiarmed or star-like blot is attached to the upper right of Sigma, at the end of its upper stroke. Its individual arms are merged. The ink establishes raised material but does not settle its exact glyph; the local star reading remains doubtful.",
       "The source's raised material remains explicit and unresolved, rather than being removed from the formula.", marked=True)
change("line 20, looped glyph between source Sigma and arrow",
       r"\unsure{\Sigma|\Sigma^{*}}\longrightarrow",
       r"\Sigma\to I", r"\Sigma^{\unsure{*}}\unsure{\ell|\deleted{\ell}}\longrightarrow",
       True, True, "omission", "Omissions", 21, "low",
       "Between the source Sigma and the arrow is a tall separate looped glyph, with a small upper loop, a narrow middle loop and a hooked lower foot. Ell is a tentative reading. Retracing obscures whether the added strokes cancel it, so both live and cancelled states are retained explicitly.",
       "The extra written source-side glyph is included without assigning it a mathematical role.")
change("line 20, overdrawn target",
       r"\longrightarrow I", r"\to I",
       r"\longrightarrow\unsure{\deleted{\Sigma}I|I}",
       True, True, "omission", "Struck text", 21, "low",
       "The target has a strong upright with top and bottom bars, together with a distinct diagonal Z-like path passing behind or through it. An underlying Sigma overwritten by I is the leading account, but the layer order is not secure; the plain-I alternative remains explicit.",
       "The target's underlying diagonal ink is preserved as a doubtful overwrite rather than silently regularised.")
change("line 21, written short form strict raised-t",
       "strict" + "$" + r"{}^t$", "strictement", r"strict\({}^t\)",
       False, True, "abbreviation expanded or spelling modernised",
       "Abbreviations expanded, spelling modernised", 22, "high",
       "The word has the strict group and a small raised terminal t-like form. There is no written -ement sequence. The abbreviation is preserved without expansion.")
change("line 21, short form or quantifier after pour",
       "pour tt", "pour tout", r"pour \unsure{tt|$\forall$}",
       False, True, "abbreviation expanded or spelling modernised",
       "Abbreviations expanded, spelling modernised", 23, "medium",
       "Two tall strokes are joined by a diagonal/low return and crossed by a horizontal bar. They may be the writer's compact tt, or a quantifier-shaped sign. No ou sequence is written, and both literal readings remain in place.")
change("line 22, induced map shaft",
       r"\varphi:\Sigma_{<x}\longrightarrow I_{<i}",
       r"\varphi : \Sigma_{<x}\to I_{<i}",
       r"\varphi:\Sigma_{<x}\mathrel{-}I_{<i}",
       True, True, "misread symbol or index", "Symbols and indices", 24, "high",
       "The connector is a single slightly curved horizontal stroke with a blunt right endpoint and no independent head. Source Sigma_<x, target I_<i and the adjoining parenthetical equation are legible.")
change("line 23, state and placement of injective",
       "injective,", r"\add{injective},", "injective,",
       False, True, "insertion or placement", "Insertions put in the wrong place", 25, "high",
       "Injective begins the last running-text baseline and is followed on that baseline by a comma and enfin. There is no insertion leader or separate interlinear placement for this word.")
change("line 23, enfin",
       "enfin", r"\ill{} que", "enfin que",
       False, True, r"readable ink left as \ill{}", "Readable ink left as illegible", 25, "high",
       "The low en run, tall f stem and joined in ending are visible before que. The word is legible despite the crowding at the lower edge.", marked=True)
change("line 23, final short form before ordonné",
       "tot" + "$" + r"{}^t$", r"tot.\ ordonné", r"\unsure{tot.|tt.} ordonné",
       True, False, "abbreviation expanded or spelling modernised",
       "Abbreviations expanded, spelling modernised", 26, "medium",
       "There are two tall t-like uprights sharing a long horizontal bar, a low loop/return between them, and a separate point at right. That low return favours tot. but can be read as the join in tt. No third raised t is separately visible; C's raised-t reading was considered and is not completed in the text.")
change("lower left edge, foliation and hand",
       r"\mspage{65}", "", r"\margin{65}",
       True, True, "insertion or placement", "Other", 27, "high",
       "Pale thin numerals 6 and 5 sit at the extreme lower left, in a different hand and medium from the black running text. They are recorded as other-hand foliation. No authorial page number is visible at the top of the sheet.")

OUT["decisions"] = [
    {
        "id": "M0609", "decision": "undecided",
        "reading": r"\Sigma_{\unsure{k}i}",
        "evidence": "In the source of the b map, Sigma and the final dotted i are visible. The first subscript glyph has a densely retraced, looped k-like body whose underlying strokes cannot all be separated. The uncertainty is narrowed to that first subscript, not removed.",
        "crop": CP[12]["file"], "box": CP[12]["box"], "confidence": "medium",
    },
    {
        "id": "M0610", "decision": "undecided",
        "reading": r"\Sigma^{\unsure{*}}",
        "evidence": "The source Sigma has a dark raised star-like cluster attached to its upper-right stroke. The cluster is written, but its merged arms do not fix the exact sign. The whole formula was inspected; the additional looped glyph and target overwrite are separately retained in place.",
        "crop": CP[21]["file"], "box": CP[21]["box"], "confidence": "low",
    },
]

def inventory(kind, position, reading, hand="his hand"):
    OUT["inventory"].append({
        "element": f"E{len(OUT['inventory']) + 1:02d}",
        "kind": kind, "position": position, "first_words_or_objects": reading,
        "sheet_kind": "text", "hand": hand, "transcribed": "yes",
    })

inventory("text", "top, lines 1–8, paragraph d)",
          r"d) Les $\Sigma_j\hookrightarrow\Sigma_{ji}$ sont bordants")
inventory("deletion", "line 1, between d) and Les", r"\deleted{\unsure{a}}")
inventory("deletion", "line 2, after x in Sigma_i", r"\deleted{les}")
inventory("deletion", "line 2, opening parenthesis at right", r"\deleted{pour $j<i$}")
inventory("insertion", "above the cancelled phrase at the right of line 2",
          r"\inserted{indices}")
inventory("deletion", "line 3, first cancelled words", r"\deleted{\unsure{tels que}}")
inventory("deletion", "line 3, after the cancelled words", r"\deleted{$\Sigma$}")
inventory("insertion", "above the cancelled line-3 phrase", r"\inserted{par l'ens}")
inventory("text", "lines 9–11, paragraph e)",
          r"e) $\Sigma_{\unsure{i|j}j}\xrightarrow{s_{ij}}\Sigma_i$ est transversal")
inventory("text", "line 12, above the two displays", "Si on pose")
inventory("display", "line 13, first centred equality",
          r"\Sigma=\coprod_{i\in I}\Sigma_i")
inventory("display", "line 14, lower equality with two-level index",
          r"\Sigma^{<}(1)=\coprod_{\substack{i,j\in I\\i<j}}\Sigma_{ij}")
inventory("text", "lines 15–19, running prose around three map expressions",
          r"et $\uline{s},\uline{b}:\Sigma^{<}(1)\mathrel{-}\Sigma$ induits par les")
inventory("deletion", "line 18, between comme and le graphe", r"\deleted{\unsure{graphe}}")
inventory("insertion", "above the cancelled graphe in line 18", r"\inserted{image}")
inventory("text", "lines 20–23, continuation at the bottom",
          r"propre, que l'application $\varphi:\Sigma^{\unsure{*}}$")
inventory("insertion", "left of and above propre in line 20, with a curved leader",
          r"\inserted{immersion}")
inventory("deletion", "line 20, after propre and its surviving comma", r"\deleted{et}")
inventory("insertion", "above l'application in line 20, leader ending before phi",
          r"\inserted{continue évidente}")
inventory("deletion", "line 20, possible cancelled/reworked glyph between Sigma and arrow",
          r"\unsure{\ell|\deleted{\ell}}")
inventory("deletion", "line 20, possible underlying Sigma in the overdrawn target I",
          r"\unsure{\deleted{\Sigma}I|I}")
inventory("margin note", "extreme lower-left edge, pale foliation",
          r"\margin{65}", "another unnamed hand")

def doubt(place, reading, alternatives, confidence, reason):
    assert reading in TEX, ("Doubt is not in place in TeX", reading)
    OUT["doubts"].append({
        "place": place, "reading": reading, "alternatives": alternatives,
        "confidence": confidence, "reason": reason,
    })

doubt("line 1, cancelled initial glyph", r"\unsure{a}",
      "a-like letter; the underlying outline remains obscured", "low",
      "The separate glyph is crossed through, with only a compact loop and small upright readable.")
doubt("line 2, following the cancelled les", r"\unsure{dans|donc}",
      "dans; donc", "medium",
      "The terminal return favours s, but the joined middle and dark ending do not decide every letter.")
doubt("line 3, cancelled first words", r"\unsure{tels que}",
      "tels que, with middle letters under the cancellation", "medium",
      "Tall and descending strokes fit the proposed words, while the heavy crossing masks parts of their low run.")
doubt("line 7, short form before transversaux", r"\unsure{mutuell\({}^t\)}",
      "mutuell with a raised t-like ending; the exact shortened ending is unresolved", "medium",
      "Two l ascenders are visible, followed by low movement and a small raised loop; the full letters of -ement are not available.")
doubt("line 9, first source subscript of the labelled s map", r"\unsure{i|j}",
      "i; j", "medium",
      "The first subscript is looped and retraced, with a descender-like extension. The following j is clearer.")
doubt("line 9, right-edge word before the hyphen", r"\unsure{trans}",
      "trans, with the initial run densely retraced", "medium",
      "The word group is crowded; the separate end-of-line horizontal hyphen is secure.")
doubt("line 11, b-label subscript", r"\unsure{ik|ki}",
      "ik; ki", "medium",
      "The small dot immediately after b favours initial i, but the adjoining low forms are merged.")
doubt("line 11, source subscript M0609", r"\unsure{k}",
      "k-like overwritten glyph; no fully separated alternate letter", "medium",
      "The first lowered glyph is blackened by retracing, while the final i and the main Sigma remain legible.")
doubt("line 17, sign between the target Sigmas", r"\unsure{\times|<}",
      "times; left angle", "medium",
      "The small dark sign has a leftward junction and a rightward return; the two crossing diagonals are not independently secure.")
doubt("line 18, cancelled word", r"\unsure{graphe}",
      "graphe, with some low letters masked by the strike", "medium",
      "The g and p descenders and h-like upright survive, but the cancellation merges with the middle letters.")
doubt("line 19, final e of stricte", r"\unsure{stricte|strict}",
      "stricte; strict", "medium",
      "The rightward return of the last tall stroke may include e; an independent final loop is not isolated.")
doubt("line 20, raised source mark M0610", r"\unsure{*}",
      "star-like raised sign, exact glyph unresolved", "low",
      "The raised cluster is heavily merged with the Sigma's upper-right stroke.")
doubt("line 20, extra looped source-side glyph", r"\unsure{\ell|\deleted{\ell}}",
      "live ell-like glyph; cancelled ell-like glyph; the letter itself is tentative", "low",
      "Upper and middle loops and a lower hooked foot support ell, but reworking obscures the letter and cancellation state.")
doubt("line 20, target overwrite", r"\unsure{\deleted{\Sigma}I|I}",
      "underlying cancelled Sigma followed by I; reworked I alone", "low",
      "The diagonal Z-like path and bold upright coexist; their layering is not fully recoverable.")
doubt("line 21, after pour", r"\unsure{tt|$\forall$}",
      "tt; forall-shaped sign", "medium",
      "Two tall uprights share a horizontal bar and a joining diagonal/return. The image does not fully separate a letter abbreviation from a quantifier.")
doubt("line 23, final short form", r"\unsure{tot.|tt.}",
      "tot.; tt.", "medium",
      "A low loop/return between two uprights may be o or the join between two t forms. A separate final point is secure; a third raised t is not isolated.")

OUT["notes"] = [
    {
        "id": "150-066-N01",
        "text": "The sheet has no visible authorial page number. A pale 65 at the extreme lower left belongs to another unnamed hand and is recorded as foliation. The body consists of paragraphs d) and e), two stacked coproduct displays and a final prose paragraph with interlinear revisions.",
    },
    {
        "id": "150-066-N02",
        "text": "In d), the manuscript writes the opening hooked map as Sigma_j to Sigma_ji, then introduces the index expression I_<i,x by a displayed-in-line definition. It describes bordant subspaces and their transversality, with a reference to b). The literal source and target of the opening hook are retained from their visible indices. H's editorial expectation of a different map is not part of the manuscript text.",
    },
    {
        "id": "150-066-N03",
        "text": "In e), the manuscript describes the displayed s_ij map as transversal to the stated system of bordant morphisms. The b-label subscript locally favours ik and remains marked against ki; the first source subscript is overdrawn. No mathematical interpretation was used to replace those written indices.",
    },
    {
        "id": "150-066-N04",
        "text": "The lower paragraph gives coproduct notation for Sigma and the locally angular Sigma(1), then connects conditions a), b), c) with an injective pair map and the graph of a strict order relation. The manuscript subsequently calls the b map an immersion propre and describes the phi expressions using the words strictement croissante, injective and totally ordered in written short forms. These are reports of the manuscript's assertions; this transcription supplies no proof check or new theorem.",
    },
    {
        "id": "150-066-N05",
        "text": "The cancellation at the top preserves a readable Sigma and a distinct stop to its right. The stop is outside the cancelling stroke. The replacement par l'ens is written above the cancelled tels-que/Sigma phrase; indices is a separate insertion above the preceding crossed range. Only one closing parenthesis is visible after b in the next line.",
    },
    {
        "id": "150-066-N06",
        "text": "Four local raised signs—in the lower coproduct display, the s,b expression, the pair-map source and the lower b-map source—show left-angle contours joined to opening parentheses. The lower phi source has a different, crowded star-like cluster whose reading remains open. A separate tall looped glyph between that Sigma and its arrow is included with both its letter and live/struck state uncertain. The target's bold upright and diagonal Z-like path are retained as an uncertain Sigma/I overwrite.",
    },
    {
        "id": "150-066-N07",
        "text": "The s,b connector following the two displays and the final induced-phi connector are plain shafts in the image. The other inspected maps retain their visible heads, including the solid terminal head in the lower b expression. Underlines below the s and b labels are separate written strokes.",
    },
    {
        "id": "150-066-N08",
        "text": "The short form before transversaux has two l ascenders and a small raised ending, retained as uncertain mutuell with raised t. The final abbreviation has two tall uprights, a low return and a separate stop; tot. and tt. remain open. C's extra raised t was considered against the crop and was not separately visible. Injective and enfin occupy the final ordinary baseline; enfin is readable despite H's illegible marker. All expansions are confined to the abbreviations list.",
    },
]

OUT["notation"] = [
    {
        "form": r"\Sigma_j\hookrightarrow\Sigma_{ji}",
        "meaning": "The opening hooked map as written by the author in condition d).",
        "evidence": "Dotted/descending j beside the source and joined ji beside the target; a continuous left hook and right head.",
        "places": "066: line 1, p02",
    },
    {
        "form": r"I_{<i,x}\overset{\mathrm{def}}{=}\{j\in I\mid j<i,\ \Sigma_{ji}\ni x\}",
        "meaning": "The index expression explicitly defined by the manuscript.",
        "evidence": "Two-part <i,x subscript, unaccented def, paired braces, vertical separator and reversed membership sign are visible.",
        "places": "066: line 3, p06",
    },
    {
        "form": r"\Sigma^{<}(1)",
        "meaning": "The manuscript's locally angular Sigma notation in the second coproduct display and three subsequent expressions.",
        "evidence": "Each of the four raised marks has a left junction and two rightward arms; the lower arm joins the opening parenthesis.",
        "places": "066: display 2; lines 15, 17, 19; p14, p15, p16, p19",
    },
    {
        "form": r"\uline{s},\uline{b}",
        "meaning": "The separately underlined labels used in the manuscript's coproduct and graph expressions.",
        "evidence": "A short horizontal stroke lies under each letter, apart from the longer connector shafts.",
        "places": "066: lines 15, 17, 19",
    },
    {
        "form": r"\mathrel{-}",
        "meaning": "Literal unheaded horizontal connectors preserved in two written expressions.",
        "evidence": "Single shafts with blunt endpoints and no separately visible heads.",
        "places": "066: lines 15 and 22, p15 and p24",
    },
    {
        "form": r"\Sigma\unsure{\times|<}\Sigma",
        "meaning": "The pair-map target as written, with the small intervening sign unresolved.",
        "evidence": "The dense left junction and rightward return do not expose two independent crossing diagonals.",
        "places": "066: line 17, p16",
    },
    {
        "form": r"\Sigma^{\unsure{*}}\unsure{\ell|\deleted{\ell}}",
        "meaning": "The source-side ink in the lower phi expression; the extra glyph has no assigned mathematical role.",
        "evidence": "Raised dark cluster at the Sigma's upper right, followed by a separate tall looped and reworked glyph.",
        "places": "066: line 20, p21, M0610 and adjacent ink",
    },
    {
        "form": r"\unsure{\deleted{\Sigma}I|I}",
        "meaning": "The overdrawn target of the lower phi expression.",
        "evidence": "A strong I-like upright and bars coexist with a diagonal Z-like path; layer order stays uncertain.",
        "places": "066: line 20, p21",
    },
]
OUT["abbreviations"] = [
    {"written": "ens", "expansion": "ensemble", "places": "066: line-3 insertion par l'ens"},
    {"written": "def", "expansion": "définition", "places": "066: definition label in line 3"},
    {"written": "i.e.", "expansion": "id est", "places": "066: line 6"},
    {"written": r"\unsure{mutuell\({}^t\)}", "expansion": "mutuellement; written ending uncertain", "places": "066: line 7"},
    {"written": "p.r.", "expansion": "par rapport", "places": "066: line 9"},
    {"written": "inj.", "expansion": "injectif or injective according to the author's intended construction", "places": "066: line 18"},
    {"written": r"strict\({}^t\)", "expansion": "strictement", "places": "066: line 21"},
    {"written": r"\unsure{tt|$\forall$}", "expansion": "tout, for the tt reading; the alternate reading is a quantifier sign", "places": "066: line 21"},
    {"written": r"\unsure{tot.|tt.}", "expansion": "totalement is the apparent intended expansion in this phrase; literal short form remains open", "places": "066: line 23"},
]
OUT["hand_log"] = [
    {
        "habit": "Compact raised left angles can join their lower arm directly to the following opening parenthesis.",
        "places": "066: display 2 and lines 15, 17, 19",
        "scope": "All four locally inspected angular occurrences on this sheet; the phi-source cluster remains separately uncertain.",
        "witness_errors": "H prints stars at all four angular occurrences.",
    },
    {
        "habit": "Dotted i and descending j are clear in several formulas, while retracing can merge the small source indices.",
        "places": "066: opening hook, definition, e) first map and b map",
        "scope": "Clear examples remain literal; first source index in e), b-label order and the following source k-like glyph stay doubtful.",
        "witness_errors": "C and H give different b-label index order; C marks the source Sigma_ki doubtful.",
    },
    {
        "habit": "A cancellation can merge with the low letter run while leaving tall stems and descenders visible.",
        "places": "066: initial a-like group; tels que; graphe; et",
        "scope": "The local uncertain cancelled words keep in-place marks. The crossed Sigma retains all three defining strokes and can be read.",
        "witness_errors": "H omits the initial cancelled group and leaves et live; both drafts give graphe without local uncertainty.",
    },
    {
        "habit": "Long final returns and raised terminal t-like forms compress adverbial short forms.",
        "places": "066: mutuell with raised ending; strict raised-t; final tot./tt.",
        "scope": "Each ending was inspected independently; no common full-word completion was applied.",
        "witness_errors": "Both drafts expand mutuellement; H expands strictement; C supplies a third raised t in the final abbreviation.",
    },
    {
        "habit": "Connector endpoints vary between exposed heads, filled compact heads and blunt unheaded shafts.",
        "places": "066: p02, p09, p12, p15, p16, p19, p21, p24",
        "scope": "All written connectors on this sheet were inspected at both ends.",
        "witness_errors": "Both drafts give headed arrows at the plainly unheaded line-15 and line-22 connectors.",
    },
    {
        "habit": "Interlinear additions use curved leaders that remain distinct from cancellations.",
        "places": "066: immersion and continue évidente",
        "scope": "Leaders were traced to before propre and after l'application respectively.",
        "witness_errors": "H leaves the two-word qualification illegible; C gives its readable text.",
    },
    {
        "habit": "The pale bottom-left foliation has thinner strokes and different spacing from the author's dark text.",
        "places": "066: lower-left 65",
        "scope": "Only this assigned sheet is assessed here.",
        "witness_errors": "C uses its authorial page-number macro for the other-hand foliation; H's body omits it.",
    },
]

def audit(p, kind, reading, box=None):
    bounds = CP[p]["box"] if box is None else box
    OUT["audit_boxes"].append({
        "box": f"B{len(OUT['audit_boxes']) + 1:02d}", "kind": kind,
        "x0": bounds[0], "y0": bounds[1], "x1": bounds[2], "y1": bounds[3],
        "reading": reading,
    })

audit(1, "struck passage", r"d) \deleted{\unsure{a}}")
audit(2, "doubtful formula", r"$\Sigma_j\hookrightarrow\Sigma_{ji}$")
audit(3, "lexical disagreement", r"\deleted{les} \unsure{dans|donc} les")
audit(4, "insertion", r"(\deleted{pour $j<i$}\inserted{indices}")
audit(5, "struck passage", r"\deleted{\unsure{tels que}}\deleted{$\Sigma$}\inserted{par l'ens}.")
audit(6, "lexical disagreement", r"$I_{<i,x}\overset{\mathrm{def}}{=}\{j\in I\mid j<i,\ \Sigma_{ji}\ni x\}$,")
audit(7, "lexical disagreement", "par b) sont")
audit(8, "lexical disagreement", r"\unsure{mutuell\({}^t\)}")
audit(9, "doubtful formula", r"$\Sigma_{\unsure{i|j}j}\xrightarrow{s_{ij}}\Sigma_i$")
audit(10, "lexical disagreement", r"\unsure{trans}-")
audit(11, "lexical disagreement", "versal des morphismes bordants")
audit(12, "doubtful formula", r"$b_{\unsure{ik|ki}}:\Sigma_{\unsure{k}i}\longrightarrow\Sigma_i$")
audit(13, "lexical disagreement", r"$\Sigma=\coprod_{i\in I}\Sigma_i$")
audit(14, "handwritten number", r"$\Sigma^{<}(1)=\coprod_{\substack{i,j\in I\\i<j}}\Sigma_{ij}$")
audit(15, "handwritten number", r"et $\uline{s},\uline{b}:\Sigma^{<}(1)\mathrel{-}\Sigma$ induits par les")
audit(16, "doubtful formula", r"$(\uline{s},\uline{b}):\Sigma^{<}(1)\longrightarrow\Sigma\unsure{\times|<}\Sigma$")
audit(17, "struck passage", r"\deleted{\unsure{graphe}}\inserted{image}")
audit(18, "lexical disagreement", r"\unsure{stricte|strict}, avec")
audit(19, "handwritten number", r"$\uline{b}:\Sigma^{<}(1)\longrightarrow\Sigma$")
audit(20, "insertion", r"\inserted{immersion} propre, \deleted{et} que")
audit(21, "doubtful formula", r"l'application \inserted{continue évidente} $\varphi:\Sigma^{\unsure{*}}\unsure{\ell|\deleted{\ell}}\longrightarrow\unsure{\deleted{\Sigma}I|I}$")
audit(22, "lexical disagreement", r"est strict\({}^t\) croissante,")
audit(23, "doubtful formula", r"pour \unsure{tt|$\forall$} $x\in\Sigma$,")
audit(24, "doubtful formula", r"$\varphi:\Sigma_{<x}\mathrel{-}I_{<i}$ $(i=\varphi(x))$ est")
audit(25, "lexical disagreement", "injective, enfin que")
audit(26, "doubtful formula", r"$\Sigma_{<x}$ est \unsure{tot.|tt.} ordonné.")
audit(27, "handwritten number", r"\margin{65}")

OUT["unresolved"] = [
    "Cancelled initial a-like glyph; masked letters of cancelled tels que and graphe.",
    "Dans leads over donc, but the short word remains open.",
    "The shortened mutuell raised ending and the crowded trans group remain locally uncertain.",
    "First source subscript in e), b-label ik/ki order and the overwritten source k-like subscript (M0609).",
    "The compact sign between the graph-map target Sigmas, and the final e of stricte.",
    "The star-like raised source cluster (M0610), the separate ell-like source glyph and its state, and the Sigma/I target overwrite.",
    "The tt/forall-shaped sign after pour and the final tot./tt. short form.",
]
with (EDITION / "packets/150_scan066/diffs.tsv").open(newline="") as f:
    DIFFERENCES = list(csv.DictReader(f, delimiter="\t"))
OUT["coverage"] = {
    "whole_image_viewed": True,
    "halves_viewed": ["top", "bottom"],
    "all_tokens_read": True,
    "all_C_insertions_deletions_checked": True,
    "differences_considered": len(DIFFERENCES),
    "macro_only_differences_ignored": (
        "Equivalent underline wrappers, inserted/deleted wrappers, text/math spacing, braces, to versus longrightarrow where an actual head is present, "
        "and en-dash/em-dash TeX spellings for the single written dash. H's editorial notes and page synopsis are excluded from manuscript text. "
        "The packet's apparent extra I in the coproduct subscript is a token-alignment artefact: both literal files contain i,j in I. "
        "Certainty-only changes are recorded as doubts or mark decisions; the cancelled-Sigma resolution has an explicitly uncounted row."
    ),
    "visual_pass_detail": (
        "Original whole image and both premade halves were each explicitly viewed once in the first-pass workflow. "
        "All 27 saved crops were explicitly emitted and read. The p13–p19 image batch whose output was truncated was not credited; "
        "those crops were subsequently emitted in smaller batches. Existing p04, p05 and p11 were reused to verify audit quotation extent; no second crop was made."
    ),
    "audit_coverage": (
        "The preliminary 27 boxes include every insertion, every cancellation or uncertain overwrite state, the full formulas containing C or proposed doubts, "
        "all four written argument-1 numerals and the foliation65, the lexical differences, and every medium/low-confidence departure. "
        "Foreground readings quote the complete target phrase/formula inside each box; adjacent clipped line fragments are contextual."
    ),
}
OUT["comparison_counts"] = {
    "rows": len(OUT["changes"]),
    "against_C": sum(row["against_C"] for row in OUT["changes"]),
    "against_H": sum(row["against_H"] for row in OUT["changes"]),
    "by_confidence": dict(collections.Counter(row["confidence"] for row in OUT["changes"])),
    "against_C_by_confidence": dict(collections.Counter(row["confidence"] for row in OUT["changes"] if row["against_C"])),
    "against_H_by_confidence": dict(collections.Counter(row["confidence"] for row in OUT["changes"] if row["against_H"])),
    "counting_rule": "Compare the leading proposed reading with each witness, ignoring equivalent macros and certainty-only changes; retain undecided status for unresolved new readings.",
}

# Structural verification only: there is no TeX compilation or mathematical test.
with (EDITION / "packets/150_scan066/marks.tsv").open(newline="") as f:
    MARKS = list(csv.DictReader(f, delimiter="\t"))
assert [m["id"] for m in MARKS] == [d["id"] for d in OUT["decisions"]]
assert len(OUT["doubts"]) == TEX.count(r"\unsure{")
assert len(CROPS) == 27
assert all((EDITION / c["file"]).is_file() for c in CROPS)
assert all(0 <= b["x0"] < b["x1"] <= 1683 and 0 <= b["y0"] < b["y1"] <= 2363 for b in OUT["audit_boxes"])
assert TEX.count(r"\inserted{") == sum(i["kind"] == "insertion" for i in OUT["inventory"])
assert TEX.count(r"\deleted{") == sum(i["kind"] == "deletion" for i in OUT["inventory"])
assert [int(x) for x in __import__("re").findall(r"\((\d+)\)", TEX)] == [1, 1, 1, 1]
atomic_text(EDITION / "reader_returns/150_scan066.json", json.dumps(OUT, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({
    "tex": str(EDITION / "reader_returns/150_scan066.tex"),
    "json": str(EDITION / "reader_returns/150_scan066.json"),
    "counts": OUT["comparison_counts"],
    "marks": len(OUT["decisions"]), "inventory": len(OUT["inventory"]),
    "doubts": len(OUT["doubts"]), "audit_boxes": len(OUT["audit_boxes"]),
    "crops": len(CROPS), "packet_differences": len(DIFFERENCES),
}, ensure_ascii=False, indent=2))
