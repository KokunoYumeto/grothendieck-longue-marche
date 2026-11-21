#!/usr/bin/env python3
"""Atomic first-reader return for scan 078; visual transcription only."""
from pathlib import Path
import csv
import json
import os

EDITION = Path(__file__).resolve().parents[1]
ROOT = EDITION.parent
RETURN = EDITION / "reader_returns"
RETURN.mkdir(exist_ok=True)
C = (ROOT / "input/SP91_C13_150_texts/pages/150_scan078.tex").read_text()
H = (ROOT / "input/SP91_C13_150_texts/hua/hua_150_scan078.tex").read_text()
CROPS = json.loads((EDITION / "scripts/reader_c_078_crop_manifest.json").read_text())

def atomic_text(path, value):
    tmp = path.with_name(path.name + ".reader_c.tmp")
    with tmp.open("w", encoding="utf-8") as f:
        f.write(value)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, path)

TEX = r"""\scanpage{78}
c'est un système inductif de \deleted{\unsure{espaces}} proespaces
sur l'ens ordonné opposé de celui des drapeaux de $I$
(\unsure{pour|avec} l'inclusion), dont le $\uline{\lim}$ est égalt $\approx X$.

Soit $Z$ \deleted{$X$} une partie (\inserted{loc\textsuperscript{t}} fermée)
de $X$, et posons, pour \deleted{$\unsure{\forall}$} un $i$ tel que
${\unsure{\deleted{{\unsure{V|\mathcal V}}}X|\deleted{X}{\unsure{V|\mathcal V}}}}_i^{\unsure{*}}
\subset\unsure{\deleted{X}Z|\deleted{Z}X}$
% The two overwritten base glyphs at each end remain in uncertain layer order.
% One shared low i and the crowded raised star-candidate are retained at the left.
\[
(55)\qquad {\unsure{V|\mathcal V}}_i^Z
={\unsure{V|\mathcal V}}_i\cap Z\qquad
\begin{gathered}
\text{provoisinage tubulaire}\\
\text{de }X_i^*\text{ dans }Z
\end{gathered}
\]
\deleted{\unsure{de|et}}
on a
\[
(56)\qquad X_i^*\hookrightarrow
{\unsure{V|\mathcal V}}_i^{\unsure{2|Z}}\hookrightarrow{\unsure{V|\mathcal V}}_i
\qquad\begin{gathered}
\text{équivalences}\\
\text{d'homotopie}
\end{gathered}
\]
Plus \unsure{généralt}, on pose (si $X_{i_n}\subset Z$)
\[
{\unsure{V|\mathcal V}}_{i_0-i_n}^Z
={\unsure{V|\mathcal V}}_{i_0-i_n}\cap Z
={\unsure{V|\mathcal V}}_{i_0}^Z\cap\cdot-\cap{\unsure{V|\mathcal V}}_{i_n}^Z
\]
C'est aussi le ${\unsure{V|\mathcal V}}_{i_0--i_n}$ relatif : le \deleted{\unsure{fil}}
stratificati\unsure{-}
% A short terminal baseline stroke reaches the right paper edge; no unseen ending is supplied.
de $Z$ induite par les
$Z_i\overset{\mathrm{def}}{=}X_i\cap Z$, pour le système d'indices
$i_0--i_n$. On a
\[
(57)\qquad {\unsure{V|\mathcal V}}_{i_0\cdot--i_n}^Z
\hookrightarrow{\unsure{V|\mathcal V}}_{i_0--i_n}
\qquad\text{\unsure{équiv.|équiv} d'homotopie}
\]
% Two tiny isolated points near the raised Z are recorded without an assigned role.
Soit $J$ une partie de $I$, posons
\[
(58)\qquad X_J^*=\bigcup_{i\in J}X_i^*,\qquad X_J=\bigcup_{i\in J}X_i
\]
\margin{77}
% Foliation in another unnamed hand at the lower left; no author number is visible.
"""

atomic_text(RETURN / "150_scan078.tex", TEX)

VGROUP = r"{\unsure{V|\mathcal V}}"
LEFTBASE = r"{\unsure{\deleted{" + VGROUP + r"}X|\deleted{X}" + VGROUP + r"}}"
LEFT = LEFTBASE + r"_i^{\unsure{*}}"
RIGHT = r"\unsure{\deleted{X}Z|\deleted{Z}X}"
CONDITION = LEFT + r"\subset" + RIGHT
DISPLAYS = [part.split(r"\]", 1)[0].strip() for part in TEX.split(r"\[")[1:]]
assert LEFT in TEX and RIGHT in TEX and len(DISPLAYS) == 5
OUT = {
    "scan": "078", "reader": "reader_c", "line_count": 20,
    "line_count_basis": "Twenty written baselines, including the two wrapped caption continuations and the separate cancelled prefix; the raised loc-t insertion and foliation are inventoried separately.",
    "changes": [], "decisions": [], "inventory": [], "doubts": [], "notes": [],
    "check_events": [], "notation": [], "abbreviations": [], "hand_log": [],
    "audit_boxes": [], "crops": CROPS, "unresolved": []
}

def change(place, c, h, final, ac, ah, kind, category, confidence, evidence,
           p=None, marked_h=False, consequence="", box=None):
    if c:
        assert c in C, ("C quote", place, c)
    if h:
        assert h in H, ("H quote", place, h)
    cp = CROPS[p-1] if p else None
    OUT["changes"].append({
        "id": f"078-{len(OUT['changes'])+1:02d}", "place": place,
        "C": c, "H": h, "final": final, "against_C": ac, "against_H": ah,
        "kind": kind, "error_category": category, "marked_in_H": marked_h,
        "confidence": confidence, "evidence": evidence,
        "crop": cp["file"] if cp else "page", "box": cp["box"] if cp else box,
        "mathematical_consequence": consequence
    })

def font(place, p, local):
    change(place, "V", r"\mathcal V", VGROUP, False, True,
           "misread symbol or index", "Symbols and indices", "low",
           local + " The rounded lower bowl and curled/flagged upper ends leave the alphabet assignment open. Plain V is the leading candidate and calligraphic V the retained alternative; the glyphs are not assigned a further mathematical interpretation.", p)

change("opening word, case", "C'est", "c'est", "c'est", True, False,
       "misread word", "Words", "high",
       "The initial open c is small, about the height of the neighbouring est. The later C'est in p14 begins with a substantially taller C. The apostrophe is a separate high stroke.", 1)
change("first line, live de before the cancellation", "de", r"\ill{}", "de", False, True,
       "omission", "Omissions", "high",
       "A live looped d and connected e stand before the thick cancellation, with a visible gap before the struck word. H leaves this region undifferentiated as an illegible group.", 2, marked_h=True)
change("first line, cancelled espaces-candidate", r"\deleted{\unsure{espaces}}", r"\ill{}",
       r"\deleted{\unsure{espaces}}", False, True, "deletion state", "Struck text", "low",
       "A thick horizontal crossing masks most of the low letter run; a long looped descender survives underneath. The candidate espaces supplied by C remains narrow and unresolved. H's illegible group does not mark this separate cancellation.", 2, marked_h=True)
change("first line, live word after the cancellation", "proespaces", "provoisinages",
       "proespaces", False, True, "misread word", "Words", "high",
       "The live word shows an initial p descender, r and o, a joined es run, a second p descender, then the compressed aces ending. The two long p strokes are especially distinct. This supports proespaces.", 2)
change("l'ens, abbreviation stop", "l'ens", r"l'ens.\ ordonné", "l'ens", False, True,
       "text not on the page", "Text that is not on the page", "high",
       "After the final downturned return of ens there is blank space before ordonné, with no detached point. The apostrophe before ens is separately high and clear.", 3)
change("opening parenthesis, pour/avec", "pour", "avec", r"\unsure{pour|avec}", False, True,
       "misread word", "Words", "medium",
       "The opening p/parenthesis contour is compact and has no separately exposed descender. The following rounded and joined low forms favour pour, but the crop does not settle that first join sufficiently to exclude the witness alternative.", 4)
change("article before the underlined lim", "dont le", "dont la", "dont le", False, True,
       "misread word", "Words", "high",
       "The final word has a tall looped l and a low open rightward e return. The preceding dont has its tall d loop and separate terminal t form.", 4)
change("underlined lim, written extent", r"$\uline{\lim}$", r"\emph{limite}",
       r"$\uline{\lim}$", False, True,
       "abbreviation expanded or spelling modernised", "Abbreviations expanded, spelling modernised", "high",
       "A large looped l is followed by a dotted i and a low m run. The word ends there, above a separate plain underline. There are no following ite letters and no arrowhead on the underline.", 5)
change("M0660, word before approx X", r"\unsure{égalt}", "égale", "égalt", False, True,
       "misread word", "Words", "medium",
       "The word has a descending g loop, a small a-like body, a tall l and a short terminal triangular t, comparable with the t of est. This t ends on the same baseline as the preceding run; it is not raised like the explicit t of loc-t in p07. The following two separate waves and X with a point are clear.", 5)
change("cancelled letter after Soit Z", r"Soit $Z$ \deleted{$X$}", r"Soit $Z$ \struck{\ill{}}",
       r"Soit $Z$ \deleted{$X$}", False, True,
       r"readable ink left as \ill{}", "Readable ink left as illegible", "high",
       "The two crossed diagonals of X remain exposed underneath two longer parallel cancellation slants. The preceding Z and following une are separate. A tiny isolated point below this region is observed without assigning a punctuation role.", 6, marked_h=True)
change("cancelled quantifier-like group before un i", r"\deleted{$\unsure{\forall}$}",
       r"pour \struck{\ill{}} un", r"\deleted{$\unsure{\forall}$}", False, True,
       "misread symbol or index", "Symbols and indices", "low",
       "Several crossing diagonals and a returning curved lower stroke survive in the cancelled group. They do not recover the original quantifier contour fully. The narrow forall candidate remains doubtful and is not expanded into words.", 8, marked_h=True)
change("pre-(55) condition, overwritten left base", r"X_i^*", r"\struck{$X_i\subset X$}",
       LEFTBASE + r"_i", True, True, "deletion state", "Struck text", "low",
       "A light rounded V/U-like bowl with curled upper end coexists with two darker X-shaped diagonals. The exposed low i is shared by the overdrawn base. Both layer orders are retained; the V-like form also retains its alphabet uncertainty. Neither a single clear live X nor a wholly cancelled simple X accounts for all surviving contours.", 9,
       consequence="Both visible base contours and their unresolved layer order are preserved at the left of the written condition.")
change("pre-(55) condition, raised star-like cluster", r"X_i^*", r"\struck{$X_i\subset X$}",
       r"^{\unsure{*}}", False, True, "omission", "Omissions", "low",
       "A dense raised group with crossing branches survives above the left base. Star remains a narrow candidate; the crossings do not establish any separate older raised letter. H's quoted condition contains no raised mark.", 9)
change("pre-(55) condition, exposed subset state", r"\subset", r"\struck{$X_i\subset X$}",
       r"\subset", False, True, "deletion state", "Struck text", "high",
       "The subset sign has exposed upper and lower curved arms and a clear open right side. No cancellation line crosses it; the heavy reworking is confined to the neighbouring base glyphs.", 9)
change("pre-(55) condition, overwritten right target", r"$X_i^*\subset Z$",
       r"\struck{$X_i\subset X$}", RIGHT, True, True, "deletion state", "Struck text", "low",
       "The target contains both X-shaped crossing diagonals and Z-shaped top, slant and bottom strokes. Their intersections do not establish which was written last. Both deleted-X/live-Z and deleted-Z/live-X orders remain explicit.", 9,
       consequence="The target retains both written contours and an unresolved order; no target is selected from the neighbouring mathematical wording.")
font("display (55), first V base", 10,
     "The first base has a hooked left upper end, a rounded lower turn and a short flag at upper right; its low i and raised Z are separate.")
font("display (55), second V base", 10,
     "The second base has the same rounded lower turn and two curled upper ends, followed by a low i and the exposed cap Z.")
change("cancelled prefix above on a", r"\deleted{de}", r"\struck{et}",
       r"\deleted{\unsure{de|et}}", False, True, "misread word", "Words", "medium",
       "A tall exposed loop favours d, but the long horizontal crossing masks the low joining strokes. De leads, with et retained as the witness alternative. The cancellation is separate from the following on a baseline.", 11)
change("on a before display (56), initial case", "On a", "on a", "on a", True, False,
       "misread word", "Words", "high",
       "The initial o is a small loop close in height to the low n run. The later On a in p17 has a visibly larger O. This local prefix therefore keeps lowercase on.", 11)
font("display (56), middle V base", 11,
     "The middle base has a broad rounded bowl and curved upper ends; the crowded raised contour is treated separately in the following row.")
change("display (56), raised contour on the middle V", "^Z", "^{Z}",
       r"^{\unsure{2|Z}}", True, True, "misread symbol or index", "Symbols and indices", "medium",
       "The raised contour begins with a fully rounded 2-like head, then descends to a short lower foot. Other raised Z forms in p10 and p13 have more extended upper bars and angular changes of direction. The shape-first reading is 2 with Z retained; no mathematical repair is made.", 11,
       consequence="The middle displayed superscript remains 2-leading with Z as an alternative.")
font("display (56), final V base", 11,
     "The final base has a rounded bowl and a prominent short upper-right flag; its low i remains clearly separate.")
change("Plus paragraph, shortened adverb", "généralement", "généralement",
       r"\unsure{généralt}", True, True,
       "abbreviation expanded or spelling modernised", "Abbreviations expanded, spelling modernised", "medium",
       "After the g descender and accented compressed middle run, the tall l leads to a flat run ending in a short t. The crop does not expose a separate -ement run. The literal short candidate généralt remains doubtful; the expanded word is recorded only in the abbreviation list.", 12)
font("middle chain, first V base", 13,
     "The first large base has a rounded bottom and short upper curls, with its raised Z and i_0-i_n index outside the body.")
font("middle chain, second V base", 13,
     "The second large base has the same open rounded bowl and upper-right flag, with no raised Z on this occurrence.")
font("middle chain, third V base", 13,
     "The smaller third base has a rounded lower bend, short upper curl, low i_0 and raised Z.")
font("middle chain, fourth V base", 13,
     "The fourth base has a narrow lower turn and short right flag, with low i_n and raised Z.")
change("middle chain, first continuation index", "i_0-i_n", r"i_0\ldots i_n",
       "i_0-i_n", False, True, "misread symbol or index", "Symbols and indices", "high",
       "Between the low 0 and the next dotted i there is exactly one short horizontal stroke. The following n is a separate low return farther to the right.", 13,
       consequence="The first continuation index keeps its single written dash.")
change("middle chain, second continuation index", "i_0-i_n", r"i_0\ldots i_n",
       "i_0-i_n", False, True, "misread symbol or index", "Symbols and indices", "high",
       "The second long index also contains one horizontal stroke between i_0 and i_n, with a visible blank interval on each side.", 13,
       consequence="The second continuation index also keeps one dash.")
change("middle chain, continuation between the last intersections", r"\cap\ldots\cap", r"\cap\cdots\cap",
       r"\cap\cdot-\cap", True, True, "misread symbol or index", "Symbols and indices", "high",
       "After the first cap there is one small round point followed by one short horizontal dash, then the next cap. The crop does not show a third point.", 13,
       consequence="The written point-plus-dash continuation replaces the witnesses' three-point ellipsis.")
font("inline V after C'est aussi le", 14,
     "The inline base has a narrow rounded/pointed bottom and short curled ends; the low continuation group is treated separately.")
change("inline V, continuation group", r"i_0\ldots i_n", r"i_0\ldots i_n",
       "i_0--i_n", True, True, "misread symbol or index", "Symbols and indices", "high",
       "Two detached short horizontal strokes stand between the round low 0 and the next dotted i. The two strokes have a clear gap.", 14,
       consequence="The inline index retains its pair of written dashes.")
change("punctuation after relatif", "relatif à", "relatif :", "relatif :", True, False,
       "misread word", "Words", "high",
       "After the final f there are two detached dark components arranged vertically: a small upper point and a short lower stroke. They form the visible colon; there is no letter body at that position.", 14)
change("article following the colon", "la", "la", "le", True, True,
       "misread word", "Words", "high",
       "The article has a looped l and a low rightward e return, matching the earlier le shape on this page. A closed a body is not exposed.", 14)
change("cancelled fil-like group", r"\deleted{fil}", r"\struck{\ill{}}",
       r"\deleted{\unsure{fil}}", False, True,
       r"readable ink left as \ill{}", "Readable ink left as illegible", "low",
       "A long f descender, a small raised i stroke and a tall final l-like stroke remain around a thick horizontal cancellation. Their low joins are masked, so fil remains a narrow candidate rather than a full resolution.", 15, marked_h=True)
change("right-edge stratification-shaped word", "stratification", "stratification",
       r"stratificati\unsure{-}", True, True,
       "text not on the page", "Text that is not on the page", "low",
       "The visible prefix supports stratificati. After the last short high stroke there is only a short lower horizontal trace running into the paper edge. Its character as a separate hyphen remains uncertain. No unseen on completion is supplied.", 15)
change("definition marker, accent", r"\mathrm{déf}", r"\text{déf}",
       r"\mathrm{def}", True, True,
       "abbreviation expanded or spelling modernised", "Abbreviations expanded, spelling modernised", "high",
       "The raised marker has a looped d, a low e and a long f descent. There is no isolated acute stroke over the e. The equality below has two separate horizontal bars.", 16)
change("prose system-of-indices continuation", r"i_0\ldots i_n", r"i_0\ldots i_n",
       "i_0--i_n", True, True, "misread symbol or index", "Symbols and indices", "high",
       "The index sequence has two detached horizontal strokes between i_0 and i_n. A separate full stop follows the sequence before the larger capital O of On a.", 17,
       consequence="The prose index sequence keeps its two written dashes.")
font("display (57), source V base", 18,
     "The source base is retraced along its curved lower turn and upper flag. The repeated strokes do not expose a separate earlier glyph; only the local alphabet uncertainty is retained.")
font("display (57), target V base", 18,
     "The target has a broad rounded lower bowl and a long upper-right flag, matching the family of forms elsewhere on this sheet.")
change("display (57), source continuation group", r"i_0\ldots i_n", r"i_0\ldots i_n",
       r"i_0\cdot--i_n", True, True, "misread symbol or index", "Symbols and indices", "high",
       "After the low 0 are a detached round point and two separate short horizontal strokes, before the next dotted i. All three components are visible, with gaps between them.", 18,
       consequence="The source index retains one point followed by two dashes.")
change("display (57), target continuation group", r"i_0\ldots i_n", r"i_0\ldots i_n",
       "i_0--i_n", True, True, "misread symbol or index", "Symbols and indices", "high",
       "The target index has two detached horizontal strokes and no corresponding additional point after the low 0. Its two-stroke cluster is read separately from the source cluster.", 18,
       consequence="The target index retains its two dashes.")
change("display (57), caption abbreviation stop", "équiv.", "équiv.",
       r"\unsure{équiv.|équiv}", False, False, "other", "Other", "medium",
       "A small terminal point is crowded against the return of v. The point-leading reading is retained with a no-stop alternative because its independence is not fully exposed. The rest of d'homotopie reaches the edge with its final low e return visible.", 18)
change("lower-left foliation", r"\mspage{77}", "", r"\margin{77}", False, True,
       "omission", "Omissions", "high",
       "The whole image and bottom half show two pale 7 digits at lower left in another unnamed hand. C already supplies the same digits; the wrapper change alone is excluded from its count. H omits the foliation.", box=[24, 2306, 77, 2342])

OUT["decisions"] = [{
    "id": "M0660", "decision": "first", "reading": "égalt",
    "evidence": "Descending g loop, tall l and a short terminal triangular t on the same baseline. The genuinely raised t of loc-t provides a local positional comparison. The word is kept literally unexpanded.",
    "crop": CROPS[4]["file"], "box": CROPS[4]["box"], "confidence": "medium"
}]

def inventory(kind, position, reading, hand="his hand"):
    OUT["inventory"].append({
        "element": f"E{len(OUT['inventory'])+1:02d}", "kind": kind,
        "position": position, "first_words_or_objects": reading,
        "sheet_kind": "text", "hand": hand, "transcribed": "yes"
    })

inventory("text", "opening four prose baselines",
          r"c'est un système inductif de \deleted{\unsure{espaces}} proespaces ... dont le \uline{\lim} est égalt \approx X.")
inventory("deletion", "first baseline, after live de", r"\deleted{\unsure{espaces}}")
inventory("text", "paragraph beginning Soit Z, above display (55)",
          r"Soit Z ... une partie (\inserted{loc\textsuperscript{t}} fermée) de X, et posons, pour ... un i tel que")
inventory("deletion", "after the first Soit Z", r"\deleted{$X$}")
inventory("insertion", "above fermée, with curved leader inside the opening parenthesis",
          r"\inserted{loc\textsuperscript{t}}")
inventory("deletion", "after pour and before un i", r"\deleted{$\unsure{\forall}$}")
inventory("display", "unnumbered condition on its own baseline before (55)", CONDITION)
inventory("deletion", "overwritten left base of that condition, layer order unresolved", LEFT)
inventory("deletion", "overwritten right target of that condition, layer order unresolved", RIGHT)
inventory("display", "display (55) with its two-line right caption", DISPLAYS[0])
inventory("deletion", "left of display (56), above on a", r"\deleted{\unsure{de|et}}")
inventory("text", "small left prefix beside the (56) map", "on a")
inventory("display", "display (56) with its two-line right caption", DISPLAYS[1])
inventory("text", "Plus paragraph above the middle chain",
          r"Plus \unsure{généralt}, on pose (si X_{i_n}\subset Z)")
inventory("display", "unnumbered middle chain", DISPLAYS[2])
inventory("text", "three prose baselines between the middle chain and (57)",
          r"C'est aussi le " + VGROUP + r"_{i_0--i_n} relatif : le \deleted{\unsure{fil}} stratificati\unsure{-} ... Z_i\overset{\mathrm{def}}{=}X_i\cap Z ... i_0--i_n. On a")
inventory("deletion", "after relatif : le, before the right-edge word", r"\deleted{\unsure{fil}}")
inventory("display", "display (57) with right caption", DISPLAYS[3])
inventory("text", "paragraph introducing J before the last display", "Soit J une partie de I, posons")
inventory("display", "last display (58)", DISPLAYS[4])
inventory("margin note", "pale lower-left foliation", "77", "another unnamed hand")

def doubt(place, reading, alternatives, confidence, reason):
    assert reading in TEX, ("doubt absent from TeX", reading)
    OUT["doubts"].append({
        "place": place, "reading": reading, "alternatives": alternatives,
        "confidence": confidence, "reason": reason
    })
    OUT["unresolved"].append(f"{place}: {reading}")

def font_doubt(place, reason):
    doubt(place, VGROUP, "plain V; calligraphic V", "low", reason)

doubt("first-line cancellation", r"\deleted{\unsure{espaces}}",
      "espaces is a narrow candidate; the hidden letters are unresolved", "low",
      "The long crossing masks the low letter run; only parts including a descender remain exposed.")
doubt("first parenthesis, preposition", r"\unsure{pour|avec}", "pour; avec", "medium",
      "The first p/parenthesis join has no separately exposed descender; the later low forms favour pour but do not settle the complete outline.")
doubt("cancelled quantifier-like group", r"\deleted{$\unsure{\forall}$}",
      "forall is a narrow candidate", "low",
      "Crossing diagonals and a curved lower return conceal the earlier contour.")
doubt("overwritten left condition base", LEFTBASE,
      "cancelled V-like base followed by X; cancelled X followed by V-like base; V/plain-calligraphic assignment also unresolved",
      "low", "Both rounded V-like and crossed X-like contours survive. Their intersections do not establish order.")
doubt("raised mark on the overwritten left condition base", r"^{\unsure{*}}",
      "star is a narrow candidate", "low",
      "The raised cluster has crossing branches but is too dense to isolate any earlier raised glyph.")
doubt("overwritten right condition target", RIGHT,
      "cancelled X followed by Z; cancelled Z followed by X", "low",
      "Both X diagonals and the top/slant/bottom of Z survive without secure layer order.")
font_doubt("(55), first base", "Rounded lower bowl and curled upper ends do not settle the alphabet assignment.")
font_doubt("(55), second base", "The second rounded base has the same unresolved plain/calligraphic assignment.")
doubt("cancelled prefix before on a", r"\deleted{\unsure{de|et}}", "de; et", "medium",
      "An exposed tall loop favours d, but the low joins are crossed through.")
font_doubt("(56), middle base", "A broad rounded bowl and curved upper ends leave the alphabet unresolved.")
doubt("(56), raised middle contour", r"^{\unsure{2|Z}}", "2; Z", "medium",
      "The contour has a fully rounded 2-like head, unlike the more extended upper bars of several other Z forms on the sheet.")
font_doubt("(56), target base", "The rounded target base and short upper-right flag do not determine a font alphabet.")
doubt("Plus paragraph, shortened adverb", r"\unsure{généralt}",
      "généralt is the literal short candidate; no unseen full ending is supplied", "medium",
      "After the tall l there is a flat run ending in a short t, without a separately exposed -ement run.")
font_doubt("middle chain, first base", "Large rounded base with short upper curls; plain/calligraphic assignment remains open.")
font_doubt("middle chain, second base", "The second rounded base has a prominent upper-right flag, but no decisive alphabet distinction.")
font_doubt("middle chain, third base", "The smaller rounded base remains an alphabet uncertainty.")
font_doubt("middle chain, fourth base", "The narrow curved base and short upper-right flag remain an alphabet uncertainty.")
font_doubt("inline base after C'est aussi le", "The inline form has short curls and a narrow lower turn, without a decisive alphabet feature.")
doubt("cancelled fil-like group", r"\deleted{\unsure{fil}}",
      "fil is a narrow candidate", "low",
      "The long f descent and raised i/final l-like strokes survive; the cancellation masks their lower joins.")
doubt("right paper edge after stratificati", r"stratificati\unsure{-}",
      "visible short terminal stroke; separate-hyphen status unresolved", "low",
      "The low stroke reaches the paper edge. No invisible on completion is included.")
font_doubt("(57), retraced source base", "The base is retraced, but the strokes do not identify a separate earlier glyph; its alphabet remains unresolved.")
font_doubt("(57), target base", "Broad lower bowl and long upper-right flag leave the alphabet assignment unresolved.")
doubt("(57), stop after équiv", r"\unsure{équiv.|équiv}", "équiv.; équiv", "medium",
      "The small terminal point is crowded against the return of v, so its independence remains uncertain.")

OUT["notes"] = [
    {"id": "150-078-N01",
     "text": "Scan 078 has no visible author number at its head. A pale 77 appears at the lower left in another unnamed hand. H's introductory comment about continuation from another leaf is editorial material and is not copied into the manuscript transcription."},
    {"id": "150-078-N02",
     "text": r"The author calls the opening object a système inductif de proespaces over the opposite ordering of the drapeaux of I and writes an underlined lim followed by est égalt and approximately X. He then introduces Z, writes the numbered expressions (55)–(58), and places homotopy-equivalence captions beside (56) and (57). This records the manuscript's statements. No proof, equality, implication or homotopy claim was checked."},
    {"id": "150-078-N03",
     "text": r"The condition before (55) is heavily reworked at both ends. The left base preserves V-like and X-like contours with one exposed low i and a crowded raised star-candidate; the target preserves both X and Z contours. Both layer orders remain in place. The intervening subset sign is exposed and live. No target or layer order is chosen from the subsequent mathematical wording."},
    {"id": "150-078-N04",
     "text": r"The eleven live V-like bases and the V-like layer in the overwritten condition retain plain/calligraphic alphabet uncertainty. These choices describe the written forms without assigning distinct mathematical roles. Every uncertain base preceding explicit indices/exponents has an outer TeX group because the uncertainty macro itself adds a raised question mark."},
    {"id": "150-078-N05",
     "text": r"The raised middle contour in (56) is kept as 2|Z, with 2 first because of its rounded head. The nearby Z forms are recorded as written at their own positions. This reading makes no algebraic adjustment to the displayed map."},
    {"id": "150-078-N06",
     "text": "Continuation marks vary locally. The first two indices in the middle chain each contain one dash. Between its final intersections there is a point then a dash. The inline V index and the prose index sequence each contain two dashes. The source index of (57) contains a point and two dashes; its target has two dashes. These components are retained individually instead of replacing them by a uniform ellipsis."},
    {"id": "150-078-N07",
     "text": "The short word after Plus is retained as the doubtful literal généralt. The terminal t in égalt is on the word baseline, while the t after the inserted loc is visibly raised. The right-edge word has the visible prefix stratificati and a short terminal stroke reaching the edge; no unseen ending is supplied. The possible expansions of short forms are confined to the abbreviation list."},
    {"id": "150-078-N08",
     "text": "A tiny isolated point below the cancelled X after Soit Z, near original x703 and y586, has no established textual role. Two tiny points near the raised Z of (57), around x748–753 and y1870–1879, are likewise left unassigned. They are source-position observations in the audit comments, with no added punctuation or counted textual difference."},
    {"id": "150-078-N09",
     "text": "The least secure readings are the struck first-line word, the cancelled quantifier, the two overwritten bases, alphabet assignments, the shortened adverb, the struck fil-like group and the word ending at the right edge. The two witnesses sometimes supply a fuller word or a conventional ellipsis where fewer individual strokes are exposed. All nineteen first crops were explicitly read, and the unresolved portions remain marked at their positions."}
]
OUT["notation"] = [
    {"form": VGROUP, "meaning": "Local alphabet candidates for the manuscript's V-like bases; no further role is assigned by the choice.",
     "evidence": "Rounded lower bowls and curled/flagged upper ends in p10, p11, p13, p14 and p18.",
     "places": "078 displays (55), (56), middle chain, inline reference and (57)"},
    {"form": LEFTBASE, "meaning": "The two observed base contours at the left of the author's overwritten condition, with unresolved layer order.",
     "evidence": "Light rounded V-like bowl beneath/through darker X-shaped diagonals in p09.",
     "places": "078 condition before (55)"},
    {"form": RIGHT, "meaning": "The two observed target contours of the same written condition, with unresolved layer order.",
     "evidence": "Both X diagonals and Z-shaped horizontal/slanting strokes survive in p09.",
     "places": "078 condition before (55), target"},
    {"form": r"\unsure{2|Z}", "meaning": "Shape-first candidates for the raised contour on the middle base of (56).",
     "evidence": "Rounded upper head and short lower foot in p11, compared locally with angular Z forms in p10 and p13.",
     "places": "078 display (56)"},
    {"form": r"i_0-i_n; i_0--i_n; i_0\cdot--i_n; \cap\cdot-\cap",
     "meaning": "Literal local continuation clusters written by the author; no uniform replacement is imposed.",
     "evidence": "One dash, two dashes, point plus two dashes, and point plus dash respectively in p13, p14, p17 and p18.",
     "places": "078 middle chain, inline reference, prose sequence and display (57)"},
    {"form": r"\uline{\lim}", "meaning": "The manuscript's short underlined form in its opening sentence.",
     "evidence": "Three-letter run with dotted i and a separate plain underline, p05.",
     "places": "078 opening paragraph"},
    {"form": r"\approx", "meaning": "The author's two-wave sign before X in the opening sentence.",
     "evidence": "Two separately exposed wavy strokes, p05.",
     "places": "078 opening paragraph"},
    {"form": r"\overset{\mathrm{def}}{=}", "meaning": "Unaccented raised definition marker over a two-bar equality.",
     "evidence": "Raised d/e/f contours without an isolated acute over e, p16.",
     "places": "078 inline Z_i definition"},
    {"form": r"\hookrightarrow", "meaning": "The three hooked connectors written in the two homotopy-captioned displays.",
     "evidence": "Each has a visible left curl/hook, horizontal shaft and right terminal head; two in p11 and one in p18.",
     "places": "078 displays (56) and (57)"}
]
OUT["abbreviations"] = [
    {"written": "ens", "expansion": "ensemble", "places": "078 opening paragraph; no written stop"},
    {"written": "lim", "expansion": "limite", "places": "078 opening paragraph; the written form is underlined"},
    {"written": "égalt", "expansion": "également, possible expansion only", "places": "078 M0660; terminal t stays on the baseline"},
    {"written": r"loc\textsuperscript{t}", "expansion": "localement", "places": "078 insertion before fermée"},
    {"written": r"\unsure{généralt}", "expansion": "généralement, possible expansion only", "places": "078 Plus paragraph"},
    {"written": "def", "expansion": "définition", "places": "078 inline equality; the written short form is unaccented"},
    {"written": r"\unsure{équiv.|équiv}", "expansion": "équivalence or équivalences; number is not settled by the short form", "places": "078 caption of (57)"}
]
OUT["hand_log"] = [
    {"habit": "Case is locally visible through relative size: the opening c is small, the later C of C'est is taller; the small on before (56) contrasts with the larger On before (57).",
     "places": "078 p01, p11, p14, p17", "scope": "These four occurrences on this sheet only.",
     "witness_errors": "C's opening C'est and on-prefix capital are revised to the smaller written forms."},
    {"habit": "V-like bases have rounded bowls and curled or flagged upper ends, leaving their plain/calligraphic alphabet assignment unresolved.",
     "places": "078 p09, p10, p11, p13, p14, p18", "scope": "Eleven live bases and one V-like contour in the overwritten condition.",
     "witness_errors": "C and H use different alphabet conventions; the transcription retains explicit local candidates."},
    {"habit": "Short continuation strokes vary in count and shape, even within one displayed formula.",
     "places": "078 p13, p14, p17, p18", "scope": "All continuation groups on this sheet were counted separately.",
     "witness_errors": "Both witnesses use ellipses at several places that show dashes or mixed point/dash clusters."},
    {"habit": "A short terminal t may be on the baseline or genuinely raised; the two positions are distinguished by exposed placement.",
     "places": "078 égalt, loc-t insertion, généralt candidate", "scope": "These three short forms only.",
     "witness_errors": "H's égale and both witnesses' full généralement are revised according to the locally exposed ending."},
    {"habit": "The raised contour in (56) has a rounded 2-like head, while several Z forms have a more extended upper bar and angular turn.",
     "places": "078 p10, p11, p13, p16, p18", "scope": "The locally rounded exponent retains 2|Z rather than forcing a uniform letter.",
     "witness_errors": "Both witnesses' Z-leading exponent is retained only as the alternative to the shape-first 2."},
    {"habit": "Overwriting can leave complete contours of two base glyphs without establishing their order.",
     "places": "078 p09", "scope": "Both ends of the pre-(55) condition; source V in (57) is merely retraced and is not assigned a second glyph.",
     "witness_errors": "C omits the extra base contours; H treats the full condition as a cancellation while the subset itself remains exposed."}
]

def audit(kind, box, reading, comment=""):
    x0, y0, x1, y1 = box
    assert 0 <= x0 < x1 <= 1681 and 0 <= y0 < y1 <= 2359, box
    item = {"box": f"B{len(OUT['audit_boxes'])+1:02d}", "kind": kind,
            "x0": x0, "y0": y0, "x1": x1, "y1": y1, "reading": reading}
    if comment:
        item["comment"] = comment
    OUT["audit_boxes"].append(item)

audit("lexical disagreement", CROPS[0]["box"], "c'est")
audit("struck passage", CROPS[1]["box"], r"de \deleted{\unsure{espaces}} proespaces")
audit("lexical disagreement", CROPS[2]["box"], "l'ens ordonné")
audit("lexical disagreement", CROPS[3]["box"], r"(\unsure{pour|avec} l'inclusion), dont le")
audit("doubtful formula", CROPS[4]["box"], r"$\uline{\lim}$ est égalt $\approx X$.")
audit("struck passage", CROPS[5]["box"], r"Soit $Z$ \deleted{$X$} une",
      "A tiny isolated point below the crossed X near original x703,y586 is recorded without an assigned textual role.")
audit("insertion", CROPS[6]["box"], r"partie (\inserted{loc\textsuperscript{t}} fermée) de $X$,",
      "The curved insertion leader ends inside the opening parenthesis before fermée.")
audit("struck passage", CROPS[7]["box"], r"\deleted{$\unsure{\forall}$} un $i$ tel",
      "The upper edge clips the lower return of the preceding fermée descender, whose full word is in B07.")
audit("doubtful formula", CROPS[8]["box"], "$" + CONDITION + "$")
audit("doubtful formula", CROPS[9]["box"], r"\[" + DISPLAYS[0] + r"\]",
      "Whole (55), both expression bases and the two-line right caption. The upper-left boundary clips the lower ends of the preceding overwritten condition, fully covered by B09.")
audit("doubtful formula", CROPS[10]["box"],
      r"\deleted{\unsure{de|et}} on a " + r"\[" + DISPLAYS[1] + r"\]",
      "The left prefix and cancelled word belong to the same rectangle as the complete (56) display and its two-line caption.")
audit("medium-confidence departure", CROPS[11]["box"],
      r"Plus \unsure{généralt}, on pose (si $X_{i_n}\subset Z$)")
audit("doubtful formula", CROPS[12]["box"], r"\[" + DISPLAYS[2] + r"\]",
      "Whole middle chain, including all four bases, three low 0 groups and each continuation cluster.")
audit("doubtful formula", CROPS[13]["box"],
      "C'est aussi le $" + VGROUP + r"_{i_0--i_n}$ relatif : le",
      "The lower edge clips the upper part of the following raised def marker, fully covered in B16.")
audit("struck passage", CROPS[14]["box"],
      r"\deleted{\unsure{fil}} stratificati\unsure{-}",
      "The final low stroke reaches the physical right paper edge. Its separate-hyphen status is unresolved; no unseen completion is supplied.")
audit("lexical disagreement", CROPS[15]["box"],
      r"$Z_i\overset{\mathrm{def}}{=}X_i\cap Z$, pour",
      "The upper-left edge clips the lower return of the preceding relatif descender. The complete definition and following comma/pour are inside this box.")
audit("handwritten number", CROPS[16]["box"], r"$i_0--i_n$. On a")
audit("doubtful formula", CROPS[17]["box"], r"\[" + DISPLAYS[3] + r"\]",
      "Whole (57), both indexed bases, hooked headed shaft and right caption. Two tiny points beside the raised Z, around x748–753,y1870–1879, remain unassigned observations.")
audit("handwritten number", CROPS[18]["box"], r"\[" + DISPLAYS[4] + r"\]",
      "Whole (58), both unions, both stars, all J/i indices and central comma. The upper boundary clips a descender from the preceding Soit J prose baseline.")
audit("handwritten number", [24,2306,77,2342], r"\margin{77}",
      "Two pale foliation digits in another unnamed hand at the lower left.")

OUT["coverage"] = {
    "whole_image_viewed": True,
    "halves_viewed": ["top", "bottom"],
    "all_tokens_read": True,
    "all_C_insertions_deletions_checked": True,
    "differences_considered": len(list(csv.DictReader(
        (EDITION / "packets/150_scan078/diffs.tsv").open(), delimiter="\t"))),
    "macro_only_differences_ignored": (
        "Scan/page metadata versus H's editorial header; equivalent deleted/struck and inserted/add wrappers; "
        "ordinary source line wrapping, spacing and subscript/superscript command ordering; "
        "H's emphasis wrapper as an acknowledgement of the visible underline; foot-foliation wrapper syntax. "
        "The plain/calligraphic V alternatives are retained as alphabet readings rather than silently equated. "
        "Differences in actual continuation strokes, word extent, case, accents and overwrite state are counted."
    ),
    "first_crop_count": 19,
    "all_crops_explicitly_emitted_and_read": True,
    "second_crops_created": False,
    "proof_check_performed": False,
    "C_revision_review": [
        {"reading": r"\deleted{\unsure{espaces}}", "crop": CROPS[1]["file"], "result": "Cancellation certain; hidden letters remain doubtful."},
        {"reading": r"\deleted{$X$}", "crop": CROPS[5]["file"], "result": "Both X diagonals recoverable under the longer cancellation slants."},
        {"reading": r"\inserted{loc\textsuperscript{t}}", "crop": CROPS[6]["file"], "result": "Raised word and t; leader attaches inside the opening parenthesis before fermée."},
        {"reading": r"\deleted{$\unsure{\forall}$}", "crop": CROPS[7]["file"], "result": "Crossed quantifier-like group retained without recovering its concealed contour."},
        {"reading": r"\deleted{\unsure{de|et}}", "crop": CROPS[10]["file"], "result": "Cancellation certain; tall loop favours de but low joins remain masked."},
        {"reading": r"\deleted{\unsure{fil}}", "crop": CROPS[14]["file"], "result": "Crossed group retained as the narrow fil candidate."}
    ],
    "additional_revision_review": [
        {"reading": LEFT, "crop": CROPS[8]["file"], "result": "Both left base contours preserved with shared i, doubtful star and unresolved layer/alphabet choices."},
        {"reading": RIGHT, "crop": CROPS[8]["file"], "result": "Both target contours preserved with unresolved order; the intervening subset stays live."}
    ],
    "numeral_audit_coverage": [
        {"place": "(55)", "boxes": ["B10"]},
        {"place": "(56) and the raised 2-leading contour", "boxes": ["B11"]},
        {"place": "three low 0 groups in the middle chain", "boxes": ["B13"]},
        {"place": "low 0 in the inline V index", "boxes": ["B14"]},
        {"place": "low 0 in the prose index sequence", "boxes": ["B17"]},
        {"place": "(57) and its two low 0 groups", "boxes": ["B18"]},
        {"place": "(58)", "boxes": ["B19"]},
        {"place": "other-hand foliation 77", "boxes": ["B20"]}
    ],
    "physical_revision_inventory": {
        "C_deleted_groups": C.count(r"\deleted{"),
        "C_inserted_groups": C.count(r"\inserted{"),
        "returned_deletion_loci": 7,
        "returned_insertion_loci": 1,
        "explanation": "Five C cancellation loci plus two overwritten condition bases. Alternative layer orders repeat deletion macros at one physical locus each."
    },
    "root_review_status": "Root has reported review of all nineteen crops and the full proposed TeX; grouped uncertainty bases were then applied as requested. The full record remains for acceptance."
}
OUT["comparison_counting_rule"] = (
    "Booleans compare the leading written candidate at each stated local place. "
    "Certainty-only changes and equivalent wrappers do not count. Eleven low-confidence H rows concern "
    "the explicitly retained plain/calligraphic alphabet alternatives. Overwrite bases, their raised mark, "
    "and the exposed relation are separate local readings. Expansions are confined to the abbreviation list."
)
OUT["comparison_counts"] = {
    witness: {
        "total": sum(row[f"against_{witness}"] for row in OUT["changes"]),
        "by_confidence": {level: sum(row[f"against_{witness}"] and row["confidence"] == level
                                   for row in OUT["changes"]) for level in ("high", "medium", "low")}
    } for witness in ("C", "H")
}
OUT["comparison_counts"]["rows_total"] = len(OUT["changes"])
OUT["comparison_counts"]["uncounted_documentation_rows"] = sum(
    not row["against_C"] and not row["against_H"] for row in OUT["changes"])
OUT["comparison_counts"]["H_alphabet_uncertainty_rows"] = 11

marks = list(csv.DictReader((EDITION / "packets/150_scan078/marks.tsv").open(), delimiter="\t"))
assert [row["id"] for row in OUT["decisions"]] == [row["id"] for row in marks]
assert len(CROPS) == 19 and all((EDITION / item["file"]).is_file() for item in CROPS)
assert len(OUT["changes"]) == 44
assert len(OUT["inventory"]) == 21
assert len(OUT["doubts"]) == 23
assert len(OUT["audit_boxes"]) == 20
assert OUT["coverage"]["differences_considered"] == 23
assert C.count(r"\deleted{") == 5 and C.count(r"\inserted{") == 1
assert OUT["comparison_counts"]["C"]["total"] == 15
assert OUT["comparison_counts"]["H"]["total"] == 40
assert r"\unsure{V|\mathcal V}_" not in TEX
assert not OUT["check_events"]
for collection in ("changes", "doubts", "audit_boxes"):
    for row in OUT[collection]:
        value = row.get("final", row.get("reading", ""))
        assert r"\unsure{V|\mathcal V}_" not in value, (collection, value)
atomic_text(RETURN / "150_scan078.json", json.dumps(OUT, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({
    "scan": OUT["scan"], "rows": len(OUT["changes"]), "decisions": len(OUT["decisions"]),
    "inventory": len(OUT["inventory"]), "doubts": len(OUT["doubts"]),
    "audit_boxes": len(OUT["audit_boxes"]), "crops": len(CROPS),
    "comparison_counts": OUT["comparison_counts"]
}, ensure_ascii=False))
