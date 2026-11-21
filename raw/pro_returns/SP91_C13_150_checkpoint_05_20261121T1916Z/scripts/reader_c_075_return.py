#!/usr/bin/env python3
"""Atomic first-reader return for scan 075; no OCR or proof check."""
from pathlib import Path
import csv
import json
import os
from collections import Counter

EDITION = Path(__file__).resolve().parents[1]
ROOT = EDITION.parent
RETURN = EDITION / "reader_returns"
RETURN.mkdir(exist_ok=True)
C = (ROOT / "input/SP91_C13_150_texts/pages/150_scan075.tex").read_text()
H = (ROOT / "input/SP91_C13_150_texts/hua/hua_150_scan075.tex").read_text()
CROPS = json.loads((EDITION / "scripts/reader_c_075_crop_manifest.json").read_text())

def atomic_text(path, value):
    tmp = path.with_name(path.name + ".reader_c.tmp")
    with tmp.open("w", encoding="utf-8") as f:
        f.write(value)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, path)

TEX = r"""\scanpage{75}
\mspage{33}
On choisit un voisinage tubulaire \unsure{standard|standart} $T_{(0)}$ de
$X_{(0)}$ dans $X$, et on pose
\[
\begin{aligned}
\deleted{(\unsure{48})}\qquad&
\left\{\begin{aligned}
X^{(1)}_{\deleted{\unsure{i}}}&=X\setminus\mathring T_{(0)}\\
X^{(1)}_{(d)}&=X^{(1)}\cap X_{(d)}\qquad(=\varnothing\text{ si }d\leq0)
\end{aligned}\right.\\
&\quad X^{(1)}_i=X^{(1)}\cap X_i
\qquad\text{de sorte que}\quad
X^{(1)}_{(d)}=\bigcup_{\substack{i\in I\\\delta(i)\leq d}}X^{(1)}\cap X_i
\end{aligned}
\]
% The brace ends above the body of the third row; that row and its right continuation are unbraced.

On \deleted{pose}\inserted{prend} alors un voisinage tubulaire
standart \deleted{de} $T_1^{\unsure{\deleted{1}|1}}$ de $X_{(1)}$ dans $X$
(petit par rapport au choix de $T_0$), soit $T_1^{(1)}$ sa trace dans
$X^{(1)}$, qui est un vois. tub. standart de $X^{(1)}_{(1)}$ dans
$x^{(1)}$. On pose
\[
\deleted{(\unsure{49})}\qquad
\begin{aligned}
X^{(2)}&=X^{(1)}\setminus\mathring T^{(1)}_{(1)}
=X^{(1)}\cap(X\setminus\mathring T_1)\\
&=X^{\deleted{\unsure{2}}}\setminus(\mathring T_0\cup\mathring T_1)
\end{aligned}
\]
\margin{OPS $T_d=\displaystyle\bigcup_{\substack{i\in I\\\delta(i)\leq d}}T_i$,
où $T_i$ est un vois. tub. de $X_i$ dans $X$}
% The oblique note lies to the left of the second display and the following paragraph.

On prend un voisinage tubulaire $T_d$ de $X_{(d)}$ dans $X$,
petit p.r. aux vois. tubulaires $T_{d'}$ ($d'<d$) déjà construits,
et on pose
\[
(48)\qquad X^{(d)}=X-\bigcup_{\alpha<d}\mathring T_\alpha.
\]
% Two tiny isolated points below the equality are recorded as unassigned marks in the audit record.
Ceci posé, on pose, pour $i\in I$, $d=\delta(i)$
\[
(\unsure{49|41})\qquad|\quad
\begin{aligned}
\Sigma_i&=X_i\cap X_{(d)}
=X_i\setminus\deleted{\unsure{\{}}\bigcup_{\underline{\alpha}<d}X_i\cap
\unsure{\dot T_\alpha|\mathring T_\alpha}
\qquad\deleted{\unsure{\subset X_i|\cap X_i}}\\
&=X_i\setminus\bigcup_{\underset{\sim}{j}<i}X_i\cap\mathring T_j
\qquad\subset X_i^*
\end{aligned}
\]
% The isolated upright before Sigma has no assigned mathematical function here.
\margin{74}
% Foliation in another, unnamed hand at the lower left.
"""

atomic_text(RETURN / "150_scan075.tex", TEX)

OUT = {
    "scan": "075", "reader": "reader_c", "line_count": 22,
    "line_count_basis": "Nineteen main text/display baselines and three lines of the oblique marginal note; author number and later foliation are inventoried separately.",
    "changes": [], "decisions": [], "inventory": [], "doubts": [], "notes": [],
    "check_events": [], "notation": [], "abbreviations": [], "hand_log": [],
    "audit_boxes": [], "crops": CROPS, "unresolved": []
}
DISPLAYS = [part.split(r"\]", 1)[0].strip() for part in TEX.split(r"\[")[1:]]
MARGIN = r"""\margin{OPS $T_d=\displaystyle\bigcup_{\substack{i\in I\\\delta(i)\leq d}}T_i$,
où $T_i$ est un vois. tub. de $X_i$ dans $X$}"""

def change(place, c, h, final, ac, ah, kind, category, confidence, evidence, p=None,
           marked_h=False, consequence="", box=None):
    if c:
        assert c in C, ("C quote", place, c)
    if h:
        assert h in H, ("H quote", place, h)
    crop = CROPS[p-1] if p else None
    OUT["changes"].append({
        "id": f"075-{len(OUT['changes'])+1:02d}", "place": place,
        "C": c, "H": h, "final": final, "against_C": ac, "against_H": ah,
        "kind": kind, "error_category": category, "marked_in_H": marked_h,
        "confidence": confidence, "evidence": evidence,
        "crop": crop["file"] if crop else "page",
        "box": crop["box"] if crop else box,
        "mathematical_consequence": consequence
    })

change("opening prose, first spelling after tubulaire",
       "standart", "standard", r"\unsure{standard|standart}", True, False,
       "misread word", "Words", "medium",
       "The last letter has a large closed oval and a lower return; it resembles the internal looped d. The later two occurrences have shorter angular terminal uprights. This local closed loop favours standard, with standart retained because the joined terminal contour is not fully decisive.", 1)
change("first display, cancelled number",
       r"\deleted{(\unsure{48})}", "(48)", r"\deleted{(\unsure{48})}", False, False,
       "other", "Other", "low",
       "Several diagonal strokes cross the parenthesized digits. Parts of a 4-like upright/crossbar and an 8-like doubled contour survive, but the crossing masks them. The narrow 48 candidate remains doubtful. H separately states that the two upper numbers are biffés; no deletion-state discrepancy is counted against that acknowledged observation.", 2)
change("first display, cancelled low group after the first X",
       r"X^{(1)}_{\deleted{\unsure{i}}}", r"X^{(1)}=X\setminus\mathring T_{(0)}",
       r"X^{(1)}_{\deleted{\unsure{i}}}", False, True,
       "omission", "Omissions", "low",
       "A dense, low group sits after the first X, beneath its raised (1), and is crossed/retraced. The surviving looped strokes do not establish an earlier letter securely; i remains only the supplied narrow candidate under an in-place doubt. H's expression omits this low cancelled material.", 2,
       consequence="A cancelled low mark is preserved after the first displayed X, without assigning it a secure mathematical identity.")
change("first display, lower end and scope of the left brace",
       C.split(r"\[", 1)[1].split(r"\]", 1)[0].strip(),
       H.split(r"\[", 1)[1].split(r"\]", 1)[0].strip(),
       DISPLAYS[0], True, True,
       "misread symbol or index", "Symbols and indices", "high",
       "The brace descends from the first row and ends at about original y503, at the upper edge of the third row. The third X_i^(1) and its low index extend below that tip, to about y553. The first two rows are enclosed; the third is below the brace. Both drafts extend the enclosure to three rows.", 2,
       consequence="The written brace groups the first two rows. The third displayed equality is retained on a separate unbraced row.")
change("first display, right continuation beginning de sorte que",
       r"\margin{de sorte que $X^{(1)}_{(d)}=\displaystyle\bigcup_{\substack{i\in I\\\delta(i)\leq d}}X^{(1)}\cap X_i$}",
       r"\text{de sorte que}\quad X^{(1)}_{(d)}=\bigcup_{\substack{i\in I\\ \delta(i)\le d}}X^{(1)}\cap X_i",
       r"\text{de sorte que}\quad X^{(1)}_{(d)}=\bigcup_{\substack{i\in I\\\delta(i)\leq d}}X^{(1)}\cap X_i",
       True, False, "insertion or placement", "Insertions put in the wrong place", "high",
       "The words and equality continue to the right of the third row on its baseline. They are not an oblique marginal note. Under the union, i in I occupies the upper bound line and delta(i) <= d the lower line; the relation has a separate lower stroke.", 2)
change("prose after the first display, replacement of pose by prend",
       r"\deleted{pose}\inserted{prend}", r"\struck{pose} \add{prend}",
       r"\deleted{pose}\inserted{prend}", False, False,
       "other", "Other", "high",
       "A horizontal crossing passes through pose; the p descender, o counter, upper s contour and final e return remain readable. Above it, prend has a long initial p, compressed middle letters and a final tall d, with no additional terminal s. The insertion replaces pose between On and alors.", 3)
change("second spelling, before the cancelled de",
       "standart", "standard", "standart", False, True,
       "abbreviation expanded or spelling modernised", "Abbreviations expanded, spelling modernised", "high",
       "The one live word has its internal d loop, a long joined lower run, and a short angular terminal upright. The ending supports the written standart. It is followed immediately by the independently crossed de.", 4)
change("cancelled de after the second spelling; H's additional cancelled word",
       r"\deleted{de}", r"\struck{standard de}", r"\deleted{de}", False, True,
       "text not on the page", "Text that is not on the page", "high",
       "Only de lies under the short cancellation between the live spelling and T_1. There is one live spelling on the left and no second struck standard/standart before it. The stroke crosses the d/e group alone.", 4)
change("raised reworked mark on the prose T_1",
       r"T_1^{\deleted{\unsure{1}}}", r"T_1",
       r"T_1^{\unsure{\deleted{1}|1}}", False, True,
       "omission", "Omissions", "low",
       "The lower index is a clear 1. A separate raised mark has a bent, thick 1-like head and a returning shaft. It is reworked, but no independent crossing line can be isolated, so both cancelled and live states remain explicit. The leading cancelled 1 candidate agrees with C's leading reading; only the omitted raised material is counted against H.", 4)
change("third spelling at the right edge, after vois. tub.",
       "standart", "standard", "standart", False, True,
       "abbreviation expanded or spelling modernised", "Abbreviations expanded, spelling modernised", "high",
       "The terminal stroke is a short upright at the right paper edge, following the long connected ar run; the earlier internal d is taller. The separate stops after vois. and tub. are visible. This later occurrence supports literal standart.", 5)
change("M0645, small x after dans",
       r"\unsure{x^{(1)}|X^{(1)}}", r"dans $X^{(1)}$. On pose",
       r"x^{(1)}", False, True,
       "misread symbol or index", "Symbols and indices", "medium",
       "The second crossed letter is only about 32 original pixels high and has a curved lower return. The preceding capital X is about 53 pixels high. Its raised (1), the following full stop and On pose are clear. The crop supports the first, lowercase reading of C's mark.", 6,
       consequence="The manuscript's lowercase x^(1) is retained in this prose occurrence.")
change("second display, cancelled number",
       r"\deleted{(\unsure{49})}", "(49)", r"\deleted{(\unsure{49})}", False, False,
       "other", "Other", "low",
       "The numeral group is crossed by several slanting strokes. The final digit's head is especially masked; 49 remains a candidate, not a recovery from the neighbouring numbers. H's separate note explicitly acknowledges that the two upper numbers are cancelled, so its displayed omission of the strike wrapper is not counted as an additional reading difference.", 7)
change("second display, raised cancelled group after the final X",
       r"X^{\deleted{\unsure{2}}}",
       r"Dans la dernière égalité, $X$ est écrit par-dessus une autre lettre.",
       r"X^{\deleted{\unsure{2}}}", False, True,
       "insertion or placement", "Insertions put in the wrong place", "low",
       "The large X has two exposed crossing diagonal strokes. A separate dense reworked group is raised just to its right; the 2 candidate is not fully recoverable through the overdrawn contour. It is preserved as a cancelled superscript. H locates an unidentified predecessor underneath the body X instead.", 7,
       consequence="The uncertain cancelled material is represented in the raised position where it survives on the sheet.")
change("oblique left note, opening capitals",
       "OPS", "Ops", "OPS", False, True,
       "misread word", "Words", "high",
       "After rotation, O is rounded, P has a tall stem with an upper bowl, and the following angular S has capital proportions. All three are uppercase; there is no separate stop after S.", 8, marked_h=True)
change("oblique note, est un after the second T_i",
       r"où $T_i$ est un vois. tub.", r"où $T_i$ vois.\ tub.",
       r"où $T_i$ est un vois. tub.", False, True,
       "omission", "Omissions", "high",
       "Between the second T_i and vois. there is a compressed est group ending in a small upright and then the linked low arches of un. Both words are present. The comma after the first T_i and the stops after vois. and tub. are separate dark marks.", 8, marked_h=True)
change("oblique note, X_i after de",
       r"de $X_i$ dans $X$", r"de $X_i^{*}$ dans $X$",
       r"de $X_i$ dans $X$", False, True,
       "misread symbol or index", "Symbols and indices", "high",
       "The X is followed by the short lower i with its dot. The surrounding space supplies no independent crossed or multiarmed raised star. The next line reads dans X.", 8, marked_h=True,
       consequence="The marginal sentence names the written X_i, with no additional star supplied.")
change("position of the oblique OPS note",
       MARGIN,
       "en travers dans la marge gauche, en face de (48)",
       MARGIN, False, True,
       "insertion or placement", "Insertions put in the wrong place", "high",
       "The slanting note occupies original x20–548, y1194–1656 beside the second, cancelled-number display and the beginning of the next prose paragraph. The later live (48) is lower, at y1795–1957. The note is placed after the second display in the return.", 8, marked_h=True)
change("final display, live parenthesized number",
       "(49)", "(49)", r"(\unsure{49|41})", False, False,
       "other", "Other", "low",
       "The first digit has the open angular 4 contour. The terminal digit has a long downward stem and a crowded tiny head, without a separately secure open counter in this crop. A collapsed 9 head and a 1-like head remain possible. The leading 49 reading is preserved under doubt; no textual difference is counted solely for adding this uncertainty.", 10)
change("M0646, isolated upright before Sigma_i",
       r"\unsure{|}", r"(49)\qquad",
       "|", False, True,
       "omission", "Omissions", "high",
       "A disconnected near-vertical stroke stands at original x456, y2093–2141, before Sigma_i. Its ends are exposed and it has no crossing arm. The literal upright is secure; the return assigns no mathematical function to it.", 10,
       consequence="The standalone upright is retained as a visible sign before the formula, without assigning an operation to it.")
change("final display, cancelled brace-like mark before the first union",
       r"\deleted{\unsure{\{}}",
       r"X_i\setminus\bigcup_{\alpha<d}",
       r"\deleted{\unsure{\{}}", False, True,
       "omission", "Omissions", "low",
       "Between the slanting subtraction mark and the first union there is a narrow overdrawn glyph with a small upper turn and a curved lower hook. The brace candidate remains doubtful because crossing/retracing obscures its central contour. H omits the surviving cancelled glyph.", 10)
change("final display, decoration beneath alpha in the first union bound",
       r"\underset{\sim}{\alpha}<d", r"\alpha<d",
       r"\underline{\alpha}<d", True, True,
       "misread symbol or index", "Symbols and indices", "high",
       "A short nearly straight horizontal stroke runs under alpha alone. It has a small upturned entry and lacks the alternating bend of the separate wave under j in the next row. The following < and d are clear.", 10,
       consequence="The first union bound carries the written underline beneath alpha.")
change("final display, decoration on the first T_alpha",
       "T̊_α", r"\mathring T_\alpha",
       r"\unsure{\dot T_\alpha|\mathring T_\alpha}", True, True,
       "misread symbol or index", "Symbols and indices", "medium",
       "Above the first T_alpha is a compact dark oval, predominantly filled, with a tiny internal glint. The later ring above T_j has a clearly open centre. Dot is the local leading reading; ring remains possible because that small centre is not settled. Neither algebra nor C's added English assertion is used to choose the decoration.", 10,
       consequence="The first T_alpha decoration is retained as dot-leading with a ring alternative; no equality is altered to accommodate either reading.")
change("final display, English editorial material embedded in C",
       ": (48) removes the interiors; with Ṫ_α the first equality of (49) fails",
       "", "", True, False,
       "text not on the page", "Text that is not on the page", "high",
       "After the first T_alpha, the manuscript has blank space and then a cancelled relation with X_i at the far right. There are no English words or colon at that position. C's editorial sentence is excluded. Its mathematical assertion has not been checked or adopted.", 10)
change("final display, cancelled right-hand relation on the first row",
       r"\deleted{\subset X_i}",
       r"En fin de première ligne, un « $\cap X_i$ » est biffé",
       r"\deleted{\unsure{\subset X_i|\cap X_i}}", False, True,
       "misread symbol or index", "Symbols and indices", "medium",
       "The initial cancelled sign has a leftward curved/pointed return and two right-going arms, favouring subset, but the long cancellation crosses its upper contour and continues through X_i. The X and low i remain legible. H's cap reading is retained as an alternative, not silently discarded.", 10,
       consequence="The cancelled relation is left locally uncertain between the two visible-candidate readings.")
change("final display, wave below j in the second union bound",
       r"\underset{\sim}{j}<i",
       r"sous « $j<i$ », un trait ondulé.",
       r"\underset{\sim}{j}<i", False, False,
       "other", "Other", "high",
       "The lower stroke beneath the long-tailed j rises, dips and runs right, forming a wave. It is centred under j rather than under the complete j<i expression. H explicitly reports a wavy stroke in its note, so its absence from H's formula wrapper is not counted as an omitted reading.", 10)
change("lower-left foliation",
       r"\mspage{74}", "", r"\margin{74}", False, True,
       "omission", "Omissions", "high",
       "The whole image and lower half show a pale 74 at the lower left in a different unnamed hand. C already supplies the same digits; changing its page-number wrapper is not counted as a textual change. H provides no foliation reading.", box=[25, 2297, 86, 2350])

OUT["decisions"] = [
    {"id": "M0645", "decision": "first", "reading": r"x^{(1)}",
     "evidence": "A small crossed letter with a curved lower return, about 32 pixels high, contrasts with the preceding 53-pixel capital X. The raised (1) is clear.",
     "crop": CROPS[5]["file"], "box": CROPS[5]["box"], "confidence": "medium"},
    {"id": "M0646", "decision": "first", "reading": "|",
     "evidence": "The isolated upright has two exposed ends, no crossing arm, and a clear gap before Sigma_i; it is preserved literally with no assigned function.",
     "crop": CROPS[9]["file"], "box": CROPS[9]["box"], "confidence": "high"}
]

def inventory(kind, position, reading, hand="his hand"):
    OUT["inventory"].append({
        "element": f"E{len(OUT['inventory'])+1:02d}", "kind": kind,
        "position": position, "first_words_or_objects": reading,
        "sheet_kind": "text", "hand": hand, "transcribed": "yes"
    })

inventory("text", "upper-left author number", "33")
inventory("text", "opening prose above the first display",
          r"On choisit un voisinage tubulaire \unsure{standard|standart} T_{(0)} de X_{(0)} dans X, et on pose")
inventory("display", "first display, three rows, first two enclosed by a brace",
          DISPLAYS[0])
inventory("deletion", "left of the first display", r"\deleted{(\unsure{48})}")
inventory("deletion", "low after the first displayed X", r"_{\deleted{\unsure{i}}}")
inventory("text", "prose between the first and second displays",
          r"On \deleted{pose}\inserted{prend} alors un voisinage tubulaire ... dans x^{(1)}. On pose")
inventory("deletion", "after On, beneath the raised replacement", r"\deleted{pose}")
inventory("insertion", "above the cancelled pose, attached between On and alors", r"\inserted{prend}")
inventory("deletion", "after the second live spelling standart", r"\deleted{de}")
inventory("deletion", "raised reworked mark after the prose T_1; deletion state remains open",
          r"T_1^{\unsure{\deleted{1}|1}}")
inventory("display", "second display, two physical rows", DISPLAYS[1])
inventory("deletion", "left of the second display", r"\deleted{(\unsure{49})}")
inventory("deletion", "raised after X in the last equality of the second display",
          r"X^{\deleted{\unsure{2}}}")
inventory("margin note", "oblique at left beside the second display and the following prose", MARGIN)
inventory("text", "paragraph introducing the general T_d",
          r"On prend un voisinage tubulaire T_d de X_{(d)} dans X, petit p.r. aux vois. tubulaires T_{d'} (d'<d) déjà construits, et on pose")
inventory("display", "live (48) in the lower half", DISPLAYS[2])
inventory("text", "prose immediately above the last display",
          r"Ceci posé, on pose, pour i\in I, d=\delta(i)")
inventory("display", "last two-row display, including its standalone upright", DISPLAYS[3])
inventory("deletion", "before the first union in the last display",
          r"\deleted{\unsure{\{}}")
inventory("deletion", "right end of the first row of the last display",
          r"\deleted{\unsure{\subset X_i|\cap X_i}}")
inventory("margin note", "lower-left foliation", "74", "another unnamed hand")

def doubt(place, reading, alternatives, confidence, reason):
    assert reading in TEX, ("doubt absent from TeX", reading)
    OUT["doubts"].append({
        "place": place, "reading": reading, "alternatives": alternatives,
        "confidence": confidence, "reason": reason
    })
    OUT["unresolved"].append(f"{place}: {reading}")

doubt("first spelling in the opening prose", r"\unsure{standard|standart}",
      "standard; standart", "medium",
      "The local terminal closed loop favours d; its connected lower return leaves the t alternative open. Later occurrences are read individually.")
doubt("cancelled first display number", r"\deleted{(\unsure{48})}",
      "48 is a narrow candidate; crossed portions are not securely recoverable", "low",
      "Diagonal hatching masks parts of both digits. No sequence-based recovery is used.")
doubt("cancelled low group after the first displayed X", r"_{\deleted{\unsure{i}}}",
      "i is a narrow candidate; no second letter can be identified securely", "low",
      "The low group is looped and heavily overdrawn; the cancellation conceals its earlier contour.")
doubt("raised mark on the prose T_1", r"T_1^{\unsure{\deleted{1}|1}}",
      "cancelled 1-candidate; live 1-candidate", "low",
      "A bent 1-like raised mark is visible. Its top is reworked and no independent strike can be separated from the returning stroke.")
doubt("cancelled second display number", r"\deleted{(\unsure{49})}",
      "49 is a narrow candidate; final digit partly concealed", "low",
      "The final digit is crossed through its head; its full contour remains unavailable.")
doubt("raised cancelled mark in the second display", r"X^{\deleted{\unsure{2}}}",
      "2 is a narrow candidate under the reworking", "low",
      "The group is clearly raised after X, but the earlier glyph cannot be recovered completely.")
doubt("live number of the last display", r"(\unsure{49|41})",
      "49; 41", "low",
      "The terminal digit's long stem is clear, but its tiny crowded head does not expose a secure counter. Numbering sequence is not used to decide it.")
doubt("cancelled mark before the last display's first union", r"\deleted{\unsure{\{}}",
      "left brace is a narrow candidate", "low",
      "A curved lower hook and reworked upper turn survive, while the middle of the glyph is concealed.")
doubt("first T_alpha in the last display", r"\unsure{\dot T_\alpha|\mathring T_\alpha}",
      "dot above T_alpha; ring above T_alpha", "medium",
      "The small raised oval looks filled except for a tiny glint. Other T decorations on this page have exposed open centres.")
doubt("cancelled relation at the right of the last display's first row",
      r"\deleted{\unsure{\subset X_i|\cap X_i}}",
      "cancelled subset X_i; cancelled cap X_i", "medium",
      "The leftward curved return favours subset, but the long crossing line masks the upper contour. X_i itself remains readable.")

OUT["notes"] = [
    {"id": "150-075-N01",
     "text": "Scan 075 bears the author's upper-left number 33 and the pale lower-left foliation 74 in another unnamed hand. The foliation is kept separate from his own number. This is a handwritten text sheet with four displayed groups and one oblique marginal note."},
    {"id": "150-075-N02",
     "text": r"The manuscript introduces tubular neighbourhoods T_{(0)}, T_1 and T_d and writes successive expressions for X^{(1)}, X^{(2)} and X^{(d)}. Its final display writes expressions for \Sigma_i. The oblique note records T_d=\bigcup_{i\in I,\delta(i)\leq d}T_i and describes T_i as a vois. tub. de X_i dans X. These statements are attributed to the manuscript; no proof, implication, or equality has been checked in this reading."},
    {"id": "150-075-N03",
     "text": r"The opening brace ends after the second row; the third equality and its de sorte que continuation stand below it. The prose occurrence after dans is the small x^{(1)} supported by p06. The last display writes X_{(d)} with a lowered parenthesized d. These positions and cases are retained without changes prompted by the argument. The isolated upright preceding \Sigma_i is also retained without an assigned operation."},
    {"id": "150-075-N04",
     "text": "Witness C contains an English editorial sentence inside the last formula, beginning '(48) removes the interiors'. The entire p10 region contains the mathematical handwriting, its cancellations and blank intervening space, but no such sentence. That addition is excluded and logged as absent from the source. Its mathematical assertion was neither used to choose a reading nor checked."},
    {"id": "150-075-N05",
     "text": r"The first T_\alpha in the last display has a predominantly filled raised oval with a tiny internal glint. The dot-leading reading and ring alternative are both preserved. The seven other ringed T occurrences on the page show open centres. The first final union bound has a short almost straight underline beneath \alpha; the second has a wavy stroke beneath j. The manuscript's written decorations are kept separately, without an inferred interpretation."},
    {"id": "150-075-N06",
     "text": "The live (48) crop shows two tiny isolated points below its equality, near original x676–682 and y1880–1890. Their function and provenance are not established. They are recorded as source-position observations in the audit comment and are not supplied as punctuation or a new formula sign. The clear final point after that display is transcribed."},
    {"id": "150-075-N07",
     "text": "The first spelling has a large closed terminal loop, supporting standard with standart as an alternative. The later two occurrences have short angular terminal uprights and are transcribed standart. This decision is local to the strokes at each occurrence. The replacement prend is raised above cancelled pose; only de, rather than a duplicate spelling, is crossed after the second occurrence."},
    {"id": "150-075-N08",
     "text": "The least secure material consists of the two cancelled display numbers, the first cancelled low group, the raised reworked marks, the last cancelled brace/relation, and the head of the final live number's terminal digit. All remain doubtful at their exact positions. Both witnesses' supplied numbers were compared with their contours rather than recovered by sequence. The two marked choices M0645 and M0646 are resolved from their whole-expression crops."}
]

OUT["notation"] = [
    {"form": r"X^{(1)}, X^{(2)}, X^{(d)}; X_{(d)}",
     "meaning": "Positional forms used by the manuscript in its successive displays; the last first-row X_(d) is explicitly lowered.",
     "evidence": "Raised and lowered parenthesized groups are separately visible in p02, p07, p09 and p10.",
     "places": "075 first, second, live (48), and last displays"},
    {"form": r"\mathring T_{(0)}, \mathring T^{(1)}_{(1)}, \mathring T_1, \mathring T_0, \mathring T_\alpha, \mathring T_j",
     "meaning": "The open raised circles written on the seven clear ringed T occurrences; no additional mathematical interpretation is asserted.",
     "evidence": "The centres are open in p02, all four T occurrences in p07, p09, and the second row of p10.",
     "places": "075 displayed formulas"},
    {"form": r"\unsure{\dot T_\alpha|\mathring T_\alpha}",
     "meaning": "The locally unresolved raised decoration on the first T_alpha of the last display.",
     "evidence": "Predominantly filled oval with a tiny inner glint in p10.",
     "places": "075 last display, first row"},
    {"form": r"\underline{\alpha}<d; \underset{\sim}{j}<i",
     "meaning": "The distinct under-markings written beneath the two union indices in the last display.",
     "evidence": "An almost straight short stroke under alpha; a separately bent wave under j.",
     "places": "075 last display"},
    {"form": "|",
     "meaning": "Standalone upright with no function assigned by this transcription.",
     "evidence": "Exposed disconnected vertical stroke before Sigma_i in p10.",
     "places": "075 last display, opening"},
    {"form": "OPS",
     "meaning": "Literal uppercase heading of the oblique marginal note; expansion unestablished.",
     "evidence": "Rounded capital O, tall capital P and angular capital S in the rotated p08 crop.",
     "places": "075 left marginal note"}
]
OUT["abbreviations"] = [
    {"written": "vois.", "expansion": "voisinage or voisinages, according to the written phrase", "places": "075 middle prose, oblique note and lower prose"},
    {"written": "tub.", "expansion": "tubulaire", "places": "075 middle prose and oblique note"},
    {"written": "p.r.", "expansion": "par rapport", "places": "075 lower prose; the earlier phrase is written in full"},
    {"written": "OPS", "expansion": "unestablished; kept unexpanded", "places": "075 oblique note"}
]
OUT["hand_log"] = [
    {"habit": "Terminal letters in the three standard/standart-shaped words must be read locally: the first ends in a large closed loop, the next two in short angular uprights.",
     "places": "075 p01, p04, p05",
     "scope": "Only these three observed occurrences; no general spelling normalization.",
     "witness_errors": "C's first leading spelling is revised under doubt; H's later two standard endings are revised to the observed standart."},
    {"habit": "A small crossed x with a curved lower return can contrast with the writer's much larger crossed capital X.",
     "places": "075 p06, before On pose",
     "scope": "The two adjacent letters compared on this page, approximately 32 and 53 pixels high.",
     "witness_errors": "C's M0645 first reading is resolved; H's capital is revised."},
    {"habit": "The manuscript's raised T circles have exposed open centres in seven occurrences; one small final decoration is much darker and remains locally unresolved.",
     "places": "075 p02, p07, p09, p10",
     "scope": "All eight raised T decorations on this sheet, with the first final T_alpha explicitly excepted from certainty.",
     "witness_errors": "Both witnesses' ring-leading final T_alpha is changed to a dot-leading uncertainty; C's prose assertion is not evidence."},
    {"habit": "Dense cancellation and retracing can hide a numeral's head while leaving a long stem exposed.",
     "places": "075 crossed first and second display numbers, raised reworked marks, and live last number",
     "scope": "Each numeral was read separately; neither a regular sequence nor neighbouring notation supplies concealed strokes.",
     "witness_errors": "Additional uncertainty is retained where witness readings do not settle the visible contours."},
    {"habit": "The first final union index has a straight under-stroke, whereas the second has a wavy under-stroke.",
     "places": "075 last display, both union bounds",
     "scope": "These two under-markings only.",
     "witness_errors": "C's tilde under alpha is revised to an underline; H omits that underline, while its note acknowledges the wave below the second bound."}
]

def audit(kind, box, reading, comment=""):
    x0, y0, x1, y1 = box
    assert 0 <= x0 < x1 <= 1680 and 0 <= y0 < y1 <= 2363, box
    item = {
        "box": f"B{len(OUT['audit_boxes'])+1:02d}", "kind": kind,
        "x0": x0, "y0": y0, "x1": x1, "y1": y1, "reading": reading
    }
    if comment:
        item["comment"] = comment
    OUT["audit_boxes"].append(item)

audit("handwritten number", [15, 30, 78, 83], r"\mspage{33}",
      "Author's number in the upper-left field, left of the opening prose.")
audit("lexical disagreement", [267, 55, 1668, 239],
      r"On choisit un voisinage tubulaire \unsure{standard|standart} $T_{(0)}$ de $X_{(0)}$ dans $X$, et on pose",
      "Opening prose block; includes both written 0 groups and the first disputed spelling.")
audit("doubtful formula", CROPS[1]["box"], r"\[" + DISPLAYS[0] + r"\]",
      "Entire first display and its right continuation. The lower edge clips the raised prend of the following paragraph; that insertion and its cancelled baseline are fully covered by B04.")
audit("insertion", CROPS[2]["box"],
      r"On \deleted{pose}\inserted{prend} alors",
      "Raised prend is above the struck pose within this same small phrase box.")
audit("doubtful formula", CROPS[3]["box"],
      r"standart \deleted{de} $T_1^{\unsure{\deleted{1}|1}}$ de",
      "The complete prose T_1 and its raised reworked mark, with the adjacent live spelling and the struck de.")
audit("handwritten number", [887, 726, 1668, 834],
      r"$X_{(1)}$ dans $X$",
      "Remainder of the same prose baseline to the right of B05; a clipped end of the preceding de at the left edge is already covered by B05.")
audit("handwritten number", [267, 833, 1668, 945],
      r"(petit par rapport au choix de $T_0$), soit $T_1^{(1)}$ sa trace dans",
      "The following prose baseline containing T_0 and T_1^(1). Any upper part of the next line's X^(1) touched by the lower boundary belongs to B08.")
audit("lexical disagreement", [267, 925, 1668, 1041],
      r"$X^{(1)}$, qui est un vois. tub. standart",
      "This baseline contains the third spelling at the right edge and a complete raised (1) at the left. The upper boundary may touch the end of the preceding prose baseline, recorded in B07.")
audit("doubtful formula", CROPS[5]["box"],
      r"de $X^{(1)}_{(1)}$ dans $x^{(1)}$. On pose",
      "Both complete expressions surrounding M0645 are included. A clipped descender at the upper edge comes from the preceding prose baseline.")
audit("doubtful formula", CROPS[6]["box"], r"\[" + DISPLAYS[1] + r"\]",
      "Entire second display, both rows and its cancelled number. The left edge includes only part of the oblique OPS note, whose complete reading is in B11.")
audit("margin note", CROPS[7]["box"],
      r"\deleted{(\unsure{49})}" + "\n" + MARGIN,
      "The rectangular margin box also contains the complete crossed number from the second display at its upper right. Adjacent main-text fragments clipped along its right and lower boundaries belong to the paragraph beginning On prend un voisinage tubulaire.")
audit("handwritten number", CROPS[8]["box"], r"\[" + DISPLAYS[2] + r"\]",
      "Whole live (48). Two tiny isolated points below the equality, near x676–682 and y1880–1890, are observed without an assigned textual role. The clear terminal point after T_alpha belongs to the formula and is included.")
audit("doubtful formula", CROPS[9]["box"], r"\[" + DISPLAYS[3] + r"\]",
      "Entire last display, including the live doubtful number, isolated upright, both cancellations, and both union bounds. The top boundary clips lower ends of letters from the preceding Ceci posé baseline.")
audit("handwritten number", [25, 2297, 86, 2350], r"\margin{74}",
      "Pale lower-left foliation in another unnamed hand, to the left of the final display's second row.")

OUT["coverage"] = {
    "whole_image_viewed": True,
    "halves_viewed": ["top", "bottom"],
    "all_tokens_read": True,
    "all_C_insertions_deletions_checked": True,
    "differences_considered": len(list(csv.DictReader(
        (EDITION / "packets/150_scan075/diffs.tsv").open(), delimiter="\t"))),
    "macro_only_differences_ignored": (
        "Scan/page metadata versus H's editorial notes; equivalent deleted/struck and inserted/add wrappers; "
        "aligned/array syntax, spacing commands and ordinary line wrapping; emptyset/varnothing encoding; "
        "equivalent ordering of a common subscript and superscript; margin wrapper syntax; "
        "Unicode versus TeX encoding of the same glyph. The brace's actual scope and the de sorte que/OPS "
        "placement are counted separately because their source positions differ. H's explicit acknowledgement "
        "of the upper number cancellations and the lower wave is included when counting its readings."
    ),
    "first_crop_count": 10,
    "all_crops_explicitly_emitted_and_read": True,
    "second_crops_created": False,
    "proof_check_performed": False,
    "C_revision_review": [
        {"reading": r"\deleted{(\unsure{48})}", "crop": CROPS[1]["file"], "result": "Strike certain; digits retained doubtful."},
        {"reading": r"_{\deleted{\unsure{i}}}", "crop": CROPS[1]["file"], "result": "Low cancelled material certain; candidate letter unresolved."},
        {"reading": r"\deleted{pose}", "crop": CROPS[2]["file"], "result": "All four letters recoverable around the crossing."},
        {"reading": r"\inserted{prend}", "crop": CROPS[2]["file"], "result": "Raised replacement attached to pose; no final s."},
        {"reading": r"\deleted{de}", "crop": CROPS[3]["file"], "result": "Crossing covers de alone; no duplicate preceding spelling."},
        {"reading": r"T_1^{\unsure{\deleted{1}|1}}", "crop": CROPS[3]["file"], "result": "Raised 1-like mark visible; its strike state remains open in place."},
        {"reading": r"\deleted{(\unsure{49})}", "crop": CROPS[6]["file"], "result": "Strike certain; final digit masked."},
        {"reading": r"X^{\deleted{\unsure{2}}}", "crop": CROPS[6]["file"], "result": "Raised reworked group retained; earlier glyph incomplete."},
        {"reading": r"\deleted{\unsure{\{}}", "crop": CROPS[9]["file"], "result": "Cancelled brace-like group retained."},
        {"reading": r"\deleted{\unsure{\subset X_i|\cap X_i}}", "crop": CROPS[9]["file"], "result": "Crossed right-end relation retained with local relation doubt."}
    ],
    "numeral_audit_coverage": [
        {"place": "author 33", "boxes": ["B01"]},
        {"place": "initial T_(0), X_(0)", "boxes": ["B02"]},
        {"place": "first cancelled number, seven raised (1) groups, T_(0), and condition d<=0", "boxes": ["B03"]},
        {"place": "prose T_1 and raised 1-like mark", "boxes": ["B05"]},
        {"place": "following X_(1)", "boxes": ["B06"]},
        {"place": "prose T_0 and T_1^(1)", "boxes": ["B07"]},
        {"place": "next prose X^(1)", "boxes": ["B08"]},
        {"place": "X^(1)_(1) and lowercase x^(1)", "boxes": ["B09"]},
        {"place": "second cancelled number, all displayed 0/1/2 indices and exponents, including the raised cancelled 2 candidate", "boxes": ["B10"]},
        {"place": "live (48)", "boxes": ["B12"]},
        {"place": "last live (49|41)", "boxes": ["B13"]},
        {"place": "other-hand foliation 74", "boxes": ["B14"]}
    ],
    "physical_revision_inventory": {"C_deleted_groups": C.count(r"\deleted{"), "C_inserted_groups": C.count(r"\inserted{"),
                                    "returned_deletion_elements": 9, "returned_insertion_elements": 1},
    "root_review_status": "Root has reported review of all ten crops and the complete proposed TeX. The full record remains for root acceptance."
}

OUT["comparison_counting_rule"] = (
    "Booleans count changes to the leading candidate's words, glyphs, omission, placement or state. "
    "Adding or removing an uncertainty marker alone is excluded. C's first cancelled i/1/2/number "
    "candidates remain its leading readings. H's expressly reported cancelled upper numbers and "
    "wave below the second final bound are acknowledged from its notes. Each row represents its stated local place."
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

mark_ids = [row["id"] for row in csv.DictReader(
    (EDITION / "packets/150_scan075/marks.tsv").open(), delimiter="\t")]
assert [row["id"] for row in OUT["decisions"]] == mark_ids
assert len(CROPS) == 10
assert all((EDITION / crop["file"]).is_file() for crop in CROPS)
assert len(OUT["inventory"]) == 21
assert len(OUT["doubts"]) == 10
assert len(OUT["audit_boxes"]) == 14
assert len(OUT["changes"]) == 26
assert OUT["comparison_counts"]["C"]["total"] == 6
assert OUT["comparison_counts"]["H"]["total"] == 18
assert C.count(r"\deleted{") == 9 and C.count(r"\inserted{") == 1
assert not OUT["check_events"]
atomic_text(RETURN / "150_scan075.json", json.dumps(OUT, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({
    "scan": OUT["scan"], "rows": len(OUT["changes"]), "decisions": len(OUT["decisions"]),
    "inventory": len(OUT["inventory"]), "doubts": len(OUT["doubts"]),
    "audit_boxes": len(OUT["audit_boxes"]), "crops": len(CROPS),
    "comparison_counts": OUT["comparison_counts"]
}, ensure_ascii=False))
