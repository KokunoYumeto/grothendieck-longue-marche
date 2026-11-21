"""Assemble page 023's first-reader report; no image recognition or compilation."""
from pathlib import Path
import json
import re

ROOT = Path("/workspace/scratch/8759b8008681")
OUT = ROOT / "work/reports/150_scan023"
PACKET = ROOT / "packets/150_scan023"
C = (PACKET / "C.tex").read_text()
H = (PACKET / "H.tex").read_text()
F = (OUT / "draft.tex").read_text()
BOX = json.loads((OUT / "crop_boxes.json").read_text())
Q = chr(96) * 2

def norm(s):
    return re.sub(r"\s+", " ", s).strip()

def without_comments(s):
    return "\n".join(re.sub(r"(?<!\\)%.*", "", line) for line in s.splitlines())

LIVE = norm(without_comments(F))
CN, HN = norm(C), norm(H)
changes = []

def change(cid, crop, place, c, h, final, evidence, confidence="high",
           kind="misread word", against_c=False, against_h=True,
           marked_in_h=False, consequential=False, error_category=2):
    for witness, snippet, full in (("C", c, CN), ("H", h, HN)):
        if snippet and norm(snippet) not in full:
            raise ValueError(f"{cid}: {witness} excerpt is not exact: {snippet}")
    if norm(final) not in LIVE:
        raise ValueError(f"{cid}: final excerpt is not live in draft: {final}")
    changes.append(dict(
        id=cid, place=place, c=c, h=h, final=final, evidence=evidence,
        crop=f"crops/150_scan023_{crop}.png", box=BOX[crop],
        confidence=confidence, kind=kind, against_c=against_c,
        against_h=against_h, marked_in_h=marked_in_h,
        consequential=consequential, error_category=error_category,
        c_omission=(c == ""), h_omission=(h == "")
    ))

old_kind = "deletion state (struck given live or live given struck)"
ins_kind = "insertion or placement"
abbr_kind = "abbreviation expanded or spelling modernised"
illeg_kind = r"readable ink left as \ill{}"

change("P01", "P01", "Upper-left author's folio",
       r"\mspage{\unsure{6}}",
       r"\note{En haut à gauche, un chiffre surchargé, illisible ; la page continue le feuillet 6 (page 21).}",
       r"\mspage{\unsure{6}}",
       "The dense numeral has an ascending upper-right stroke and a rounded lower return, supporting 6 as a candidate. Overtracing prevents separation of the interior strokes. The doubt is retained; this row records H's lack of a source-number transcription, not a secure resolution or any invented overwritten digit.",
       confidence="low", kind="omission", marked_in_h=True, error_category=3)
change("P02", "P02", "L1 theorem heading and opening words",
       r"\uline{Thm} Considérons les", r"\ill{}",
       r"\uline{Thm} Considérons les",
       "Thm has the tall T/h bodies, low final m and a separate horizontal underline. The main baseline carries Considérons, with its d ascender and dotted i, followed by the tall loop of les. The oblique marginal writing crosses this baseline but does not replace these letters.",
       kind=illeg_kind, marked_in_h=True, error_category=5)
change("P03", "P03", "L1 cancelled words after catégories",
       r"\deleted{\unsure{définies ainsi}}", r"\struck{\ill{}}",
       r"\deleted{\unsure{ainsi définies|définies ainsi}}",
       "The first crossed group consists mainly of low joined loops and an i-like point. The second contains the conspicuous tall d/f-like uprights. This favors ainsi définies in that order. The cancellation covers joins and final letters, so the reversed C order remains an alternative rather than being silently discarded.",
       confidence="medium", against_c=True, marked_in_h=True)
change("P04", "P04", "L2 noun replaced by raised systèmes",
       r"\deleted{\unsure{triples|couples}}", r"\struck{couples}",
       r"\deleted{\unsure{couples|triples}}",
       "The old word has a rounded low initial group before the p descender and the following l-like ascender, favoring couples. A long independent strike crosses the word. Its joins are not all separable, so triples remains an alternative; the raised systèmes supplies the replacement but does not decide the old letters.",
       confidence="medium", against_c=True, against_h=False)
change("P05", "P05", "L2 entire five-object tuple and extra upper-right group on dotted X",
       r"$(\widetilde X^*,\dot X,\mathcal E,Y,f)$",
       r"$(\tilde X^{*},\dot X,\mathcal E,Y,f)$",
       r"$(\widetilde X^*,\dot X^{\unsure{}},\mathcal E,Y,f)$",
       "The second X has its own independent upper dot and, farther to its upper right, a separate dense black group. The latter is not paper noise and is not the ordinary dot. No token or cancellation state can be recovered. The empty-content doubt locates this present group; it does not mean absence of ink. The retraced X body itself is not assigned an invented previous letter.",
       confidence="low", kind="omission", against_c=True,
       consequential=True, error_category=3)
change("P06", "P06", "L3 full espace",
       "espace top.", "esp. top.", "espace top.",
       "After the p descender the word continues through low a/c/e strokes before the separate top. There is no abbreviation stop at the position where esp. would end; top. has its own visible stop.",
       kind="misread word")
change("P07", "P07", "L4 singular cylindrical-neighbourhood wording",
       "voisinage cylindrique", "voisinages cylindriques",
       "voisinage cylindrique",
       "Voisinage ends with the g loop and low e return; cylindrique ends with its q descender and low ue return. Neither ending has an additional terminal s.",
       kind="misread word")
change("P08a", "P08", "L5 top before the map",
       r"$Y$ esp. top.,", r"$Y$ esp. top.,", r"$Y$ esp. top,",
       "The esp. stop is separate and visible. After top the only following mark is the descending comma; there is no independent full stop between the p and that comma.",
       kind="text not on the page", against_c=True, error_category=9)
change("P08b", "P08", "L5 complete f map",
       r"$f:\dot X\longrightarrow Y$", r"$f:\dot X\to Y$",
       r"$f:\dot X\mathrel{\relbar\joinrel\relbar}Y$",
       "The connector is one horizontal shaft with a blunt right endpoint and no visible upper or lower arrowhead arm. The f, two colon points, dotted X and terminal Y are separately legible. Its semantic status as an application does not supply a drawn head.",
       kind="misread symbol or index", against_c=True,
       consequential=True, error_category=1)
change("P09", "P09", "L8 singular conical-neighbourhood wording",
       "voisinage cônique", "voisinages côniques",
       "voisinage cônique",
       "The two words end without an extra s. A distinct short arch stands above the o in cônique, so the local accented spelling is retained.",
       kind="misread word")
change("P10a", "P10", "L9 separate old le before live Alors",
       r"\deleted{\unsure{le}}", "", r"\deleted{\unsure{le}}",
       "A separate tall loop followed by a low terminal stroke stands before the live Alors and is traversed by its own cancellation stroke. The loop supports l, but the crossed ending leaves le doubtful. H omits this old item.",
       confidence="medium", kind="omission", error_category=3)
change("P10b", "P10", "L9 naturel and the attachment of ci-dessus",
       r"le foncteur naturel \inserted{ci-dessus} de a)",
       r"le foncteur \add{ci-dessus} \uncertain{naturel} de \emph{a)}",
       r"le foncteur naturel \inserted{ci-dessus} de a)",
       "Naturel is live on the main baseline after foncteur. The raised ci-dessus has its own hyphen and the curved leader descends into the gap after naturel and before de a), not before naturel.",
       kind=ins_kind, marked_in_h=True, error_category=6)

upper_c = r"""NB Il y a un énoncé \unsure{analogue} en termes de structures de
voisinages tubulaires \uline{stricts} (au lieu des germes
de voisinages tub.) \unsure{à} \uuline{voir !}"""
upper_f = r"""NB Il y a un énoncé \unsure{analogue} en termes de \unsure{structures} de
voisinages tubulaires \uline{stricts} (au lieu des germes
de voisinages tub.) \unsure{à} \uuline{voir !}"""
upper_h = H[H.index(r"\marginal{NB"):H.index(r"\note{Plusieurs")]
change("P11a", "P11", "Upper diagonal note, first sentence",
       upper_c, upper_h, upper_f,
       "In the rotated frame the marginal baselines can be followed separately from the diagonal main Thm and other main-text strokes. NB Il y a, un énoncé, en termes de, voisinages tubulaires, stricts, au lieu des germes and de voisinages tub. are readable. Stricts has one underline; voir ! has two. Analogue and the compact à remain masked at their crossings, and structures is locally doubtful. H's isolated voisinage cylindrique does not represent the tubulaires line.",
       confidence="medium", kind=illeg_kind, marked_in_h=True, error_category=5)
change("P11b", "P11", "Upper note, dense sign after Les catégories sont",
       r"\unsure{$\simeq$}.", "",
       r"\unsure{\deleted{$\simeq$}|$\simeq$}",
       "The compact group contains several overlaid horizontal/curved strokes and is denser than an ordinary equivalence sign. A cancelled earlier simeq-like sign is preferred, with a live sign retained as an alternative. It is followed by independent word ink; no separate full stop is established after the group. Neither the sign's exact body nor its cancellation state is forced.",
       confidence="low", kind=old_kind, against_c=True,
       marked_in_h=True, consequential=True, error_category=7)
change("P11c", "P11", "Upper note, word following the dense sign",
       "", r"catégories \ill{}", r"\unsure{équivalentes}",
       "After the dense sign there is an independent long word, with a pronounced q descender, a dotted i, and tall l/t strokes. These support équivalentes. Its final letters intersect transverse main-text ink, so the ending remains a local doubt. C's bare sign omits this word; H leaves the category statement unreadable.",
       confidence="medium", kind="omission", against_c=True,
       marked_in_h=True, consequential=True, error_category=3)
change("P11d", "P11", "Upper note, restriction on morphisms",
       "Les morphismes ici sont les isos, pour simplifier !", "",
       "Les morphismes ici sont les isos, pour simplifier !",
       "The lower marginal lines carry morphismes, then ici sont les, and the short form isos followed by pour simplifier. The s endings and comma after isos remain in the source wording. This restriction is not transcribed in H's short marginal residue.",
       confidence="medium", kind="omission", consequential=True, error_category=3)
change("P12", "P12", "Central pushout display",
       r"X=\widetilde X^*\amalg_{\dot X}Y",
       r"X=\tilde X^{*}\amalg_{\dot X}Y .",
       r"X=\widetilde X^*\amalg_{\dot X}Y",
       "The entire display has tilde and star on the first right-hand X, two uprights on a common base for amalg, and a separately dotted lowered X. The area immediately following Y is blank; H's terminal point is not on the page.",
       kind="text not on the page", error_category=9)

middle_c = r"$(\widetilde X^*,\dot X)$ joue le rôle d'un " + Q + r"découpage cônique'' de $X$"
middle_h = r"$(\tilde X^{*},\dot X)$, germe de \ill{} \uncertain{cônique} de \ill{} $X$"
change("P13a", "P13", "Middle marginal note, description of the pair",
       middle_c, middle_h, middle_c,
       "The j of joue descends in a long loop, followed by oue. Le rôle has the tall l and its upper accent; the next line has un and the separate d/p bodies of découpage. Double quotation marks enclose découpage cônique, whose o has an independent arch. These are words, not H's substituted germe de or illegible placeholders.",
       kind=illeg_kind, marked_in_h=True, error_category=5)
change("P13b", "P13", "Middle note, suivant",
       r"$X$ suivant $(Y,\mathcal T)$",
       r"$X$ \ill{} $(Y,\mathcal T)$",
       r"$X$ suivant $(Y,\mathcal T)$",
       "Before the parenthesized Y and calligraphic T, the short s opening, dotted i and joined v/ant strokes form suivant. The parenthesis is not part of that word.",
       kind=illeg_kind, marked_in_h=True, error_category=5)
change("P13c", "P13", "Middle note, cramped ending",
       r"\unsure{ci-dessus}",
       r"\note{note en travers dans la marge gauche ; lecture incertaine.}",
       r"\unsure{ci-dessus}",
       "The short initial strokes, hyphen-like gap and taller d support ci-dessus, but the small final strokes and their attachment remain crowded. The phrase is retained in the marginal note with C's doubt. H gives an editorial uncertainty note instead of these source words.",
       confidence="medium", kind="omission", marked_in_h=True, error_category=3)
change("P13d", "P13", "Middle note, terminal punctuation",
       r"\unsure{ci-dessus}.", r"$(Y,\mathcal T)$}",
       r"\unsure{ci-dessus}",
       "The dark point in the cramped ending precedes its final strokes and belongs inside the word area. There is no independent point following the complete ending. The draft therefore supplies no terminal period after ci-dessus.",
       kind="text not on the page", against_c=True, against_h=False,
       error_category=9)
change("P14a", "P14", "Lower NB opening, live Une partie and insertion scope",
       r"Une partie \inserted{$X'$}",
       r"\struck{Une} \add{Une partie fermée $X'$}",
       r"Une partie \inserted{$X'$}",
       "Only one Une is present. Its initial capital is retraced, but no independent stroke cancels the word; partie shares its live baseline. X-prime alone is raised before de X. The long curve is a leader, not a cancellation authorizing H's duplicate struck/live Une or an insertion of the whole phrase.",
       kind=old_kind, error_category=7)
change("P14b", "P14", "Lower NB opening, H's extra fermée",
       r"Une partie \inserted{$X'$}",
       r"\add{Une partie fermée $X'$}",
       r"Une partie \inserted{$X'$}",
       "The interval from partie through the raised X-prime to de X contains the symbol and its leader, with no f ascender or further letter sequence for fermée. H's word is absent here; it is not inferred from the later closedness statement.",
       kind="text not on the page", error_category=9)
change("P15a", "P15", "Lower NB, ambient X-star after de",
       r"de $X^*$", r"de $\tilde X^{*}$", r"de $X^*$",
       "The preceding primed X has an explicit tilde, prime and star. The next X after de has its raised star but no separate wave above the body. The missing tilde is retained literally despite the pushout notation.",
       kind="misread symbol or index", consequential=True, error_category=1)
change("P15b", "P15", "Lower NB, equals shorthand",
       r"ayant $=$", "ayant même", r"ayant $=$",
       "Two distinct horizontal strokes follow ayant, with the lower stroke slightly wavy. There is no written sequence of letters for même. The source shorthand is retained without expansion.",
       kind=abbr_kind, error_category=8)
change("P16a", "P16", "Lower NB, plural inverse images",
       "images inverses", "image inverse", "images inverses",
       "Both words continue past their e bodies to short terminal s strokes; inverses has a distinct final turned return. The plural is not normalized to H's singular image inverse.",
       kind="misread word")
change("P16b", "P16", "Lower NB, fermé before ssi",
       "est fermé ssi", "est fermée ssi", "est fermé ssi",
       "After the f descender and joined erm body, the word ends at the accented e. There is no second terminal e before the clearly separate ssi.",
       kind="misread word")
change("P18a", "P18", "Cancelled compatibility clause, old il f.",
       r"il \unsure{f.}", "il faut", "il f.",
       "The old f has a full looped upright, descending return and cross-stroke, plus an independent point to its right. These features settle the single-letter C doubt even though a cancellation crosses the line. The source uses f., not H's expanded faut.",
       kind=abbr_kind, against_c=True, error_category=8)
change("P18b", "P18", "Cancelled compatibility clause, old et",
       "", "et", r"\unsure{et}",
       "Between the old f. and the insertion area, a low open e-like loop joins a taller crossed t-like stroke. This supports et, but the cancellation masks the join. C omits this group; H already has et. The nearby short down-curved hook is treated as a leader, not an invented s. abbreviation.",
       confidence="medium", kind="omission", against_c=True,
       against_h=False, error_category=3)
change("P18c", "P18", "Raised une description and its own cancellation",
       r"\inserted{une description}", "une description",
       r"\inserted{\deleted{une description}}",
       "Une description occupies a separate raised baseline. A long stroke passes through those raised words, distinct from the lower strike through the old clause and its formula. C already places the insertion inside a deleted clause, so this row does not count an additional C state error; H does not mark the raised insertion. The nested deletion makes the separate physical cancellation scope explicit.",
       kind=ins_kind, error_category=6)
old_c = r"\deleted{il \unsure{f.} \inserted{une description} que $X'_{\unsure{*}}$}"
old_h = r"\struck{il faut et suffit qu'une description \ill{} que $X'$}"
old_f = r"\deleted{il f. \unsure{et} \inserted{\deleted{une description}} que $X'_{\unsure{*}}$}"
change("P18d", "P18", "Old clause, H's additional suffit qu' wording",
       old_c, old_h, old_f,
       "The legible old sequence is il f., a doubtful et, the raised separately struck une description, then que and X-prime with a dense lowered mark. No independent sequence of letters supplies H's suffit qu' before une description. The short hook there is not expanded into a word. Other changed components in this context are collated separately.",
       confidence="medium", kind="text not on the page",
       marked_in_h=True, error_category=9)
change("P18e", "P18", "Old clause, complete decorated X-prime formula",
       r"$X'_{\unsure{*}}$", r"$X'$", r"$X'_{\unsure{*}}$",
       "A separate high prime survives above-right of X. Below-right, under the crossing line, there is a multi-armed dense group compatible with a star but partly filled and overtraced. C's local star doubt remains; H omits the lowered group.",
       confidence="medium", kind="omission", consequential=True, error_category=3)
change("P18f", "P18", "Live replacement, f without a stop",
       r"\inserted{il f. et s. que l'on ait}",
       "il faut et suffit que l'on ait",
       r"\inserted{il f et s. que l'on ait}",
       "The new f is a single tall looped letter. Unlike the old f. immediately above-left, it has no independent dot in the gap before et. The later s has a separate dot. Thus the live source is il f et s. que l'on ait, retaining the short forms and the asymmetry of their punctuation.",
       kind=abbr_kind, against_c=True, error_category=8)
change("P18g", "P18", "Live replacement, s. short form",
       "et s. que", "et suffit que", "et s. que",
       "The single s-shaped body is followed by a separate dark point before que; no intervening letters spell suffit.",
       kind=abbr_kind, error_category=8)
change("P18h", "P18", "Placement of the live replacement clause",
       r"\inserted{il f. et s. que l'on ait}",
       "il faut et suffit que l'on ait",
       r"\inserted{il f et s. que l'on ait}",
       "The live abbreviated clause occupies the added lower baseline beneath the cancelled old wording. It is the replacement of that old clause, not a continuation at the same original baseline. C marks the addition; H does not distinguish it with an addition marker. P18f/P18g collate its literal abbreviations separately.",
       kind=ins_kind, error_category=6)
change("P19a", "P19", "Condition a), cylindrical germ label",
       r"cylindrique $\mathcal E$ de", "cylindrique de",
       r"cylindrique $\mathcal E$ de",
       "Between cylindrique and de, the source has the same two-lobed calligraphic E form used in the upper definition, written slightly high. H omits this mathematical label.",
       kind="omission", consequential=True, error_category=3)
change("P19b", "P19", "Condition a), punctuation after the pair",
       r"$(\widetilde X,\dot X)$.", r"$(\tilde X,\dot X)$.",
       r"$(\widetilde X,\dot X)$",
       "The closing parenthesis is complete, followed by open white space. No independent dot follows it. Both witnesses' full stop is removed; the next source line begins Il y a lieu.",
       kind="text not on the page", against_c=True, error_category=9)
change("P20", "P20", "Penultimate main line, completer",
       r"\unsure{remplacer|compléter}", "compléter",
       r"\unsure{completer|compléter}",
       "The initial co/m strokes precede a long p descender, then a tall l and compressed ter ending. This settles the lexeme in favor of completer/compléter rather than remplacer. No detached acute can be securely identified over the e; unaccented completer is preferred, with the accented spelling retained as a local alternative.",
       confidence="medium", kind="misread word", against_c=True)
last_h_note = H[H.rindex(r"\note{Au-dessus"):].strip()
change("P21", "P21", "Raised label above-left of the closure formula",
       r"$\inserted{\widetilde X'_1}\,\overline{X'\cap X^*}$",
       last_h_note,
       r"$\inserted{\widetilde X'_1}\,\overline{X'\cap X^*}$",
       "The annotation has a distinct tilde, an upright prime and a lowered 1, and sits above-left of the full closure bar over X-prime intersection X-star. There is no equals sign between annotation and formula. H relegates the label to an editorial note and describes its placement as above X-prime; the source placement and label are represented in the transcription and comment.",
       kind=ins_kind, consequential=True, error_category=6)
change("P22a", "P22", "Final parenthesis, où",
       r"(où $X^*=\widetilde X\setminus\dot X$)",
       r"($=X^{*}=\tilde X\setminus\dot X$)",
       r"(où $X^*=\widetilde X\setminus\dot X$)",
       "After the opening parenthesis there are the compact o/u bodies and a small upper accent mark, before X-star. These form où; they are not a second equals sign. The later two parallel bars between X-star and tilde X are the actual equality.",
       kind="misread word")
change("P22b", "P22", "End of the unfinished final line",
       "au vois.", "au voisinage", "au vois.",
       "The written short form ends after v/o/i/s and has a separate terminal stop. There is no nage sequence or continuation before the edge of this leaf.",
       kind=abbr_kind, error_category=8)
change("P23", "P23", "Thin lower-left foliation",
       r"\margin{22}", "", r"\margin{22}",
       "Two thin 2-shaped digits each have an upper curve, oblique descent and lower return. Their light narrow strokes differ from the main black writing. The page edge below them is not an underline.",
       kind="omission", error_category=3)

def decision(mid, crop, decision_value, reading, evidence, confidence):
    if norm(reading) not in LIVE:
        raise ValueError(f"{mid}: reading not in draft")
    return dict(id=mid, cote="150", scan="23", decision=decision_value,
                reading=reading, evidence=evidence,
                crop=f"crops/150_scan023_{crop}.png",
                box=BOX[crop], confidence=confidence)

decisions = [
    decision("M0353", "P01", "undecided", r"\unsure{6}",
             "The upper-right ascent and lower rounded return fit 6, but dense retracing prevents recovery of the internal path. No earlier digit is assigned.", "low"),
    decision("M0354", "P11", "undecided", r"\unsure{analogue}",
             "Low looped letters and a descending g-like element support analogue, but the centre is crossed by the oblique main Thm strokes, preventing a complete independent letter sequence.", "medium"),
    decision("M0355", "P11", "undecided", r"\unsure{à}",
             "A compact loop/hook occurs between the closing parenthesis after tub. and double-underlined voir !. Its upper/connecting ink meets transverse main text, so à and its accent are not fully separated.", "medium"),
    decision("M0356", "P11", "undecided",
             r"\unsure{\deleted{$\simeq$}|$\simeq$}",
             "Several dense overlaid curved/horizontal strokes support a cancelled earlier equivalence-like sign, but the original sign and cancellation state are not independently recoverable. A separate following word équivalentes is preserved outside this doubt.", "low"),
    decision("M0357", "P13", "undecided", r"\unsure{ci-dessus}",
             "The compact initial strokes, intervening short dash and d-like ascender support ci-dessus. The final crowded strokes and exact attachment remain uncertain. No independent terminal period is visible.", "medium"),
    decision("M0358", "P20", "other", r"\unsure{completer|compléter}",
             "Initial co/m, long p descender and tall following l decide the completer lexeme against remplacer. A separate acute is not securely visible, so the unaccented form is preferred while that single accent remains open.", "medium"),
]

inventory = []
def inv(element, kind, position, text, hand="his hand"):
    inventory.append(dict(scan="150_scan023", sheet_kind="text", hand=hand,
                          element=element, kind=kind, position=position,
                          first_words_or_objects=text, transcribed="yes"))

inv("E01", "text", "upper-left, P01", "Dense doubtful author folio 6")
inv("E02", "text", "upper main block, L1–L10", "Underlined Thm Considérons les; categories a) and b); equivalence claim")
inv("E03", "insertion", "above catégories, P03", "deux with curved attachment")
inv("E04", "deletion", "after catégories, P03", "ainsi définies | définies ainsi")
inv("E05", "deletion", "after celle des, P04", "couples | triples")
inv("E06", "insertion", "above the old noun, P04", "systèmes")
inv("E07", "text", "second entry of tuple, P05", "Dotted X plus independent unreadable upper-right group; no recovered state")
inv("E08", "deletion", "end of L8, P09", "Comme Alors; Comme remains doubtful")
inv("E09", "deletion", "start of L9, P10", "Separate doubtful le before live Alors")
inv("E10", "insertion", "above L9 after naturel, P10", "ci-dessus, leader into gap before de a)")
inv("E11", "margin note", "upper-left diagonal area, P11", "NB Il y a un énoncé analogue ... stricts ... voir !; categories and morphisms")
inv("E12", "text", "within upper note after catégories sont, P11", "Doubtful cancelled equivalence-like sign and independent équivalentes")
inv("E13", "text", "middle main line, L11", "Rappelons que")
inv("E14", "display", "middle, L12/P12", "X = tilde X-star amalg over dotted X with Y; no terminal point")
inv("E15", "margin note", "left of lower NB, P13", "Underlined NB, pair as a découpage cônique, suivant (Y,T), doubtful ci-dessus")
inv("E16", "text", "lower main block, L13–L22", "Underlined NB Une partie; compatible subsets; beginning of condition a)")
inv("E17", "insertion", "after partie and before de X, P14", "Raised X-prime with leader; live Une remains on baseline")
inv("E18", "deletion", "right end of lower closedness line, P17", "Pour que X-prime soit")
inv("E19", "insertion", "above the preceding old phrase, P17", "Repeated Pour que X-prime soit")
inv("E20", "deletion", "after cônique T, P18", "Old il f., doubtful et, que and X-prime with doubtful lowered star")
inv("E21", "insertion", "raised within old clause, P18", "une description, itself struck on its own baseline")
inv("E22", "deletion", "same raised baseline, P18", "Independent cancellation of une description")
inv("E23", "insertion", "below the old clause, P18", "il f et s. que l'on ait")
inv("E24", "insertion", "above-left of closure formula, P21", "tilde X-prime with lowered 1; no equals sign supplied")
inv("E25", "text", "lower-left, P23", "Thin 22", hand="another or undetermined hand")

audits = []
def audit(bid, kind, xyxy, reading, scope=None):
    if norm(reading) not in LIVE:
        raise ValueError(f"{bid}: audit reading is not a live draft substring")
    row = dict(box=bid, kind=kind, xyxy=xyxy, reading=reading)
    if scope:
        row["scope"] = scope
    audits.append(row)

audit("B01", "handwritten number", BOX["P01"], r"\mspage{\unsure{6}}")
audit("B02", "C/H different words", BOX["P02"], r"\uline{Thm} Considérons les",
      "Main horizontal heading and words only; diagonal marginal note is B11.")
audit("B03", "insertion | struck passage | C/H different words | less than high confidence departure",
      BOX["P03"], r"\inserted{deux} catégories \deleted{\unsure{ainsi définies|définies ainsi}} :")
audit("B04", "insertion | struck passage | C/H different words | less than high confidence departure",
      BOX["P04"], r"a) celle des \deleted{\unsure{couples|triples}}\inserted{systèmes}",
      "Main a) phrase and its raised replacement only; transverse note is B11.")
audit("B05", "doubtful formula | less than high confidence departure",
      [955, 178, 1435, 307],
      r"$(\widetilde X^*,\dot X^{\unsure{}},\mathcal E,Y,f)$")
audit("B06", "C/H different words", [428, 302, 778, 391], "espace top.,")
audit("B07", "C/H different words", [410, 398, 1060, 534], "voisinage cylindrique")
audit("B08", "C/H different words", BOX["P08"],
      r"$Y$ esp. top, $f:\dot X\mathrel{\relbar\joinrel\relbar}Y$ application continue ;")
audit("B09", "struck passage | C/H different words", BOX["P09"],
      r"de voisinage cônique de $Y$ dans $X$. \deleted{\unsure{Comme} Alors}",
      "Main baseline only; raised ci-dessus belongs to B10.")
audit("B10", "insertion | struck passage | C/H different words",
      [324, 878, 1620, 1038],
      r"\deleted{\unsure{le}} Alors le foncteur naturel \inserted{ci-dessus} de a)")
margin_start = F.index(r"\margin{NB Il y a")
margin_end = F.index("\n\nRappelons que", margin_start)
audit("B11", "margin note | struck passage | doubtful formula | C/H different words | less than high confidence departure",
      BOX["P11"], F[margin_start:margin_end].strip(),
      "The diagonal marginal note only; intersecting main-text words are separately audited.")
audit("B12", "C/H different words", BOX["P12"],
      "\\[\nX=\\widetilde X^*\\amalg_{\\dot X}Y\n\\]")
mid_start = F.index(r"\margin{\uline{NB}")
mid_end = F.index("\n\n\\uline{NB}", mid_start)
audit("B13", "margin note | C/H different words", BOX["P13"],
      F[mid_start:mid_end].strip(),
      "Middle marginal note only; lower main NB and its leader belong to B14.")
audit("B14", "insertion | struck passage | C/H different words", BOX["P14"],
      r"\uline{NB} Une partie \inserted{$X'$} de $X$ revient donc à une",
      "Main NB line; proposed strike on Une is rejected. Overlying marginal text is B13.")
audit("B15", "C/H different words", BOX["P15"],
      r"partie $\widetilde X'^*$ de $X^*$, $Y'$ de $Y$, ayant $=$")
audit("B16", "C/H different words", BOX["P16"],
      r"images inverses dans $\dot X$, et $X'$ est fermé ssi")
audit("B17", "struck passage | insertion", BOX["P17"],
      "\\deleted{Pour que $X'$ soit}\n\\inserted{Pour que $X'$ soit}")
audit("B18", "struck passage | insertion | doubtful formula | C/H different words | less than high confidence departure",
      BOX["P18"], old_f + "\n" + r"\inserted{il f et s. que l'on ait}")
audit("B19", "C/H different words", [712, 2127, 1040, 2217],
      r"$\mathcal E$ de $(\widetilde X,\dot X)$",
      "The raised germ label, de and complete pair; no terminal point is supplied.")
audit("B20", "C/H different words | less than high confidence departure", BOX["P20"],
      r"Il y a lieu alors de \unsure{completer|compléter} $\widetilde X'$ par")
audit("B21", "insertion | handwritten number", BOX["P21"],
      r"$\inserted{\widetilde X'_1}\,\overline{X'\cap X^*}$")
audit("B22", "handwritten number | C/H different words", BOX["P22"],
      r"(où $X^*=\widetilde X\setminus\dot X$), et le germe de $\widetilde X'_1$ au vois.")
audit("B23", "handwritten number", BOX["P23"], r"\margin{22}")

doubts = [
    dict(place="P01 author's folio", reading=r"\unsure{6}", alternatives="No reliable other digit", confidence="low", reason="Dense overwork masks the internal path; upper ascent/lower return merely favor 6."),
    dict(place="P03 cancelled heading words", reading=r"\deleted{\unsure{ainsi définies|définies ainsi}}", alternatives="définies ainsi", confidence="medium", reason="Low first group and tall second group favor the reversed order, but cancellation conceals joins and endings."),
    dict(place="P04 cancelled noun", reading=r"\deleted{\unsure{couples|triples}}", alternatives="triples", confidence="medium", reason="Rounded initial group favors couples, but crossed letter bodies cannot all be isolated."),
    dict(place="P05 tuple, upper-right of dotted X", reading=r"\dot X^{\unsure{}}", alternatives="No recoverable candidate; an earlier star is not established", confidence="low", reason="Separate dense mathematical ink is present. Empty payload means an unrecoverable group at this location, not absence, and asserts no cancellation state."),
    dict(place="P09 old Comme", reading=r"\deleted{\unsure{Comme} Alors}", alternatives="No better complete candidate", confidence="medium", reason="Large C-like opening and low joined bodies support Comme; the strike hides the medial joins. Alors is independently legible."),
    dict(place="P10 old le", reading=r"\deleted{\unsure{le}}", alternatives="No better complete candidate", confidence="medium", reason="Tall l loop is visible but the short crossed ending remains uncertain."),
    dict(place="P11 analogue", reading=r"\unsure{analogue}", alternatives="No better complete candidate", confidence="medium", reason="Main Thm strokes cross the middle of the marginal word."),
    dict(place="P11 structures", reading=r"\unsure{structures}", alternatives="No complete alternative supported", confidence="medium", reason="The word's tall and low body sequence is plausible on its marginal baseline, but intersects oblique main-text strokes. This is added uncertainty alone, not a collation row against C."),
    dict(place="P11 à before voir", reading=r"\unsure{à}", alternatives="Unresolved compact connecting/letter ink", confidence="medium", reason="Loop/hook and possible accent touch larger transverse ink."),
    dict(place="P11 dense equivalence-like sign", reading=r"\unsure{\deleted{$\simeq$}|$\simeq$}", alternatives="Live simeq-like sign; exact earlier sign unrecoverable", confidence="low", reason="Density suggests cancellation, but individual old sign and crossing strokes are not independent enough to force a state."),
    dict(place="P11 word after dense sign", reading=r"\unsure{équivalentes}", alternatives="Ending not independently recovered", confidence="medium", reason="q descender, i point and l/t support the lexeme; final letters are crossed by main-text writing."),
    dict(place="P13 final marginal wording", reading=r"\unsure{ci-dessus}", alternatives="No better whole candidate; attachment also uncertain", confidence="medium", reason="Short beginning, dash and taller d are supportable, but the ending is crowded. The interior point is not a terminal full stop."),
    dict(place="P18 old et", reading=r"\unsure{et}", alternatives="No complete alternative supported", confidence="medium", reason="Open e-like loop plus tall t-like stroke are traversed by the old cancellation."),
    dict(place="P18 old formula", reading=r"X'_{\unsure{*}}", alternatives="Other unrecoverable lowered crossed group", confidence="medium", reason="The separate prime is clear; lowered multi-armed mark is heavily filled and crossed."),
    dict(place="P20 completion word accent", reading=r"\unsure{completer|compléter}", alternatives="compléter", confidence="medium", reason="Lexeme completer is secure against remplacer; no detached acute is securely separable above the e."),
]

notes = [
    dict(id="N01", text="This leaf states a theorem identifying two categories: data (tilde X-star, dotted X, E, Y, f), with a germ of cylindrical neighbourhood, and data (X,Y,T), with a germ of conical neighbourhood. The marginal note proposes an analogue using strict tubular neighbourhood structures rather than germs and says 'à voir !' (the à remains uncertain). It restricts the morphisms to 'les isos, pour simplifier !'. The theorem is reported faithfully, not certified by this transcription."),
    dict(id="N02", text="The display is literally X = tilde X-star amalg_{dotted X} Y. The lower NB then discusses subsets with equal inverse images and their closedness, before an incomplete compatibility criterion beginning a). The page ends at the short form 'au vois.'; no continuation, missing condition, equals sign, accent or star is supplied from a later leaf."),
    dict(id="N03", text="Targeted set-theoretic proof of the subset correspondence. Write S=tilde X-star, B=dotted X, i:B→S for the inclusion, and q:S disjoint-union Y→X for the quotient generated by i(b)~f(b). For D⊂X, put A=q_S^{-1}(D), C=q_Y^{-1}(D). Then i^{-1}(A)=f^{-1}(C), since related generators have the same image. Conversely, assume this equality for A⊂S,C⊂Y. The indicator of A disjoint-union C has equal values on every generating pair i(b),f(b); equality propagates along every finite chain generating the equivalence relation. Thus A disjoint-union C is saturated, q^{-1}(q(A disjoint-union C))=A disjoint-union C. D=q(A disjoint-union C) is therefore the unique subset with these inverse images. This verifies precisely the source's matching-inverse-images statement for the displayed quotient; it does not use a collar, local triviality, compactness or separation."),
    dict(id="N04", text="Targeted topological proof of the closedness assertion. For the matched pair in N03, the quotient topology gives D closed in X iff q^{-1}(D) is closed in S disjoint-union Y (apply the definition to complements). A subset of a disjoint topological sum is closed iff its restrictions to both summands are closed. Hence D is closed iff A is closed in S and C is closed in Y. Saturation, proved in N03, is essential when starting from A,C. No claim that arbitrary images of closed sets under q are closed is used."),
    dict(id="N05", text="A further limited check of the stated gluing construction uses the hypotheses that B is closed in S and f is continuous. Because i is an inclusion, the generated equivalence relation does not identify two distinct points of the Y summand, so j=q_Y:Y→X is injective. If D⊂Y is closed, f^{-1}(D) is closed in B and therefore in S, and q^{-1}(j(D))=i(f^{-1}(D)) disjoint-union D is closed. By quotient topology j(D) is closed in X. Since j is continuous, it is a closed embedding. Also q restricts to a homeomorphism S\\B→X\\j(Y): it is bijective there, and any relatively open U⊂S\\B is open in S because B is closed; q^{-1}(q(U))=U, so q(U) is open in X. This checks the closed-subspace component of target data b), not the germ correspondence, fullness, faithfulness or essential surjectivity of the asserted equivalence."),
    dict(id="N06", text="Literal notation is not repaired by the proofs. In 'partie tilde X-prime-star de X-star' the second X-star has no tilde, although the displayed quotient uses S=tilde X-star. The later compatibility line uses tilde X-prime and the pair (tilde X,dotted X) without stars. The final parenthesis writes X-star=tilde X\\dotted X. These may reflect changes of notation or slips, but the assigned leaf does not determine a consistent replacement. N03–N05 explicitly use the displayed pushout interpretation and do not silently rewrite these prose formulas."),
    dict(id="N07", text="The source writes 'Pour que X′ soit compatibles' with a plural s and later 'fermé' before ssi; both literal endings remain. The final annotation tilde X-prime_1 stands above-left of the closure bar over X-prime intersection X-star, with no equals sign. The ambient space of that closure and the unfinished next assertion are not independently specified here, so no proof of the full compatibility criterion or completion assertion is claimed."),
    dict(id="N08", text="Present unreadable ink is explicitly retained: the independent upper-right mass in the tuple is represented by the empty-content mathematical doubt, with its location and unestablished state stated in the TeX comment. No previous glyph is invented under the overworked folio, dotted X body, initial Une, or germe. The dense equivalence-like sign in the upper margin has a preferred cancelled state but remains doubtful; the following word équivalentes is independent ink."),
    dict(id="N09", text="Reading record: the full original and the two supplied native halves were each inspected once, then all 23 stable saved crops were visually read. An early four-image tool response was truncated before any of P01–P04 was delivered to the reader; those four files were subsequently displayed singly for their actual first inspection. There was no OCR, external research, compilation, other-page access, or new crop of a decided place. line_count=22 counts the principal main-text baselines including the central display, excluding folia, raised replacements and the separately inventoried margins. No genuine diagram or drawing occurs on this leaf."),
    dict(id="N10", text="Collation metadata: an empty c or h string with the corresponding omission flag records that the witness does not represent the targeted ink; it is not a proposed empty source reading. Every final excerpt and every audit first reading is checked as a whitespace-normalized substring of the comment-stripped draft. C/H fragments are checked against their assigned-page files. These are textual consistency checks, not a TeX compilation or an additional image reading."),
]

check_events = [
    dict(statement_id="150_scan023.N03", type="targeted proof check",
         outcome="Verified the exact subset bijection through equality of indicators on generating gluing pairs, saturation under their equivalence closure, and the two inverse constructions."),
    dict(statement_id="150_scan023.N04", type="targeted proof check",
         outcome="Verified closedness iff both inverse-image subsets are closed directly from the quotient and disjoint-sum topologies, using the saturation result rather than an unjustified closed-map assertion."),
    dict(statement_id="150_scan023.N05", type="targeted proof check",
         outcome="Verified the canonical map from Y is a closed embedding when B is closed and f continuous, and verified the open-complement homeomorphism. No full equivalence-of-categories proof is claimed."),
]

notation = [
    dict(form=r"(\widetilde X^*,\dot X,\mathcal E,Y,f)", meaning="The five entries named in category a); a separate unrecoverable group also stands above-right of the dotted X in the written tuple.", evidence="P05 full tuple; P06–P08 describe the topological space, closed subset, cylindrical germ and continuous application."),
    dict(form=r"\mathcal E", meaning="Germ of cylindrical neighbourhood of dotted X in the initial starred ambient space; later germ label in condition a).", evidence="P06/P07 and P19 show the same two-lobed calligraphic form."),
    dict(form=r"\mathcal T", meaning="Germ of conical neighbourhood of Y in X.", evidence="Main category b) and the lower compatibility sentence; no independent ordinary T overbar is supplied."),
    dict(form=r"\mathrel{\relbar\joinrel\relbar}", meaning="Literal unheaded shaft in the f application.", evidence="P08 has a blunt right endpoint without head arms."),
    dict(form=r"\dot X^{\unsure{}}", meaning="Dotted X with present unrecoverable upper-right mathematical ink; no semantic decoration or cancellation state recovered.", evidence="P05: ordinary upper dot and separate dense upper-right group are distinct."),
    dict(form=r"X=\widetilde X^*\amalg_{\dot X}Y", meaning="Displayed gluing/pushout quotient recalled on the page.", evidence="P12: two uprights on common base and lowered dotted X."),
    dict(form=r"$=$ in ayant $=$ images inverses", meaning="Written shorthand for mêmes in this plural context.", evidence="P15 two separate bars; P16 plural images inverses."),
    dict(form=r"X'_{\unsure{*}}", meaning="Old cancelled primed-X formula with a doubtful lowered starred group; no definition is supplied on this leaf.", evidence="P18 separate high prime and dense low multi-armed mark."),
    dict(form=r"\inserted{\widetilde X'_1}\,\overline{X'\cap X^*}", meaning="Raised label above-left of a closure expression, with no written equality between them.", evidence="P21 complete formula, tilde, prime, lowered 1 and uninterrupted bar."),
]

abbreviations = [
    dict(form="Thm", expansion="théorème; no abbreviation stop supplied"),
    dict(form="esp.", expansion="espace"),
    dict(form="top.", expansion="topologique"),
    dict(form="top", expansion="topologique; locally without a stop before the map"),
    dict(form="NB", expansion="nota bene"),
    dict(form="tub.", expansion="tubulaires in the marginal parenthesis"),
    dict(form="isos", expansion="isomorphismes; source short plural without a stop"),
    dict(form="ssi", expansion="si et seulement si"),
    dict(form="f.", expansion="faut in the old cancelled clause"),
    dict(form="f", expansion="faut in the live replacement, without a stop"),
    dict(form="s.", expansion="suffit"),
    dict(form="vois.", expansion="voisinage; the source sentence continues beyond this leaf"),
    dict(form="=", expansion="mêmes in ayant = images inverses"),
]

hand = [
    dict(habit="Dotted X can carry a small point displaced toward its upper right.", places="150_scan023 P05–P08, P12, P13, P16, P19, P22", consistency="Locally repeated; the ordinary dot remains distinct from the extra dense group in the tuple.", witness_errors="Both witnesses omit the tuple's independent upper-right group; no ordinary dots are converted into stars."),
    dict(habit="Star strokes may be densely retraced, while tilde waves remain separately placed.", places="150_scan023 P05, P06, P07, P12, P15, P21, P22", consistency="The star is often compact; every tilde is checked separately, including its absence on the second X-star in P15.", witness_errors="H adds a tilde in P15; the lower old mark in P18 remains doubtful rather than being forced to a star."),
    dict(habit="Long descenders and transverse marginal writing intersect neighboring words without deleting them.", places="150_scan023 P02, P04, P11, P13, P14, P19", consistency="Main and marginal baselines can be traced independently; heavy retracing alone is not a cancellation.", witness_errors="H duplicates/cancels Une and leaves much of the two margins illegible; no invented older letter is assigned to germe or the tuple X."),
    dict(habit="Very compressed final loops do not license grammatical regularization.", places="150_scan023 P07, P09, P16 and main compatibles", consistency="Singular voisinage/cylindrique/cônique, masculine fermé, and literal plural compatibles are each retained locally.", witness_errors="H pluralizes both upper neighbourhood phrases and feminizes fermé."),
    dict(habit="Local abbreviated forms may differ in whether a stop is written.", places="150_scan023 P06, P08, P18, P22", consistency="top. and top both occur; old f. and live f are distinct; s. and vois. have points.", witness_errors="Both witnesses supply the P08 top. stop; C supplies the live f. stop; H expands f, s. and vois."),
    dict(habit="Cônique has a separate short arch over o on this leaf.", places="150_scan023 P09, P13 and the lower compatibility line", consistency="The local accent is retained; it is not inferred solely from normalized French spelling.", witness_errors="No additional accent is forced onto the ambiguous completer ending in P20."),
    dict(habit="Main text is broad black ink; lower foliation is a much thinner hand.", places="150_scan023 P01 and P23", consistency="Author folio remains an overworked candidate 6; thin lower 22 is legible.", witness_errors="H gives only editorial commentary for the upper numeral and omits thin22."),
]

coverage = {
    1: "P01: source folio candidate retained; editorial archive/page statements in H are not source text.",
    2: "P02 and P11a–P11d: heading and complete marginal note recovered; H's editorial descriptions are not transcribed as ink.",
    3: "P03: preferred cancelled ainsi définies with reverse-order alternative.",
    4: "P04: preferred couples, with triples retained under the strike.",
    5: "P06: full espace.",
    6: "P07: singular voisinage cylindrique.",
    7: "P09: singular voisinage cônique.",
    8: "P10a: separate cancelled doubtful le retained.",
    9: "P10b: naturel remains before the inserted ci-dessus.",
    10: "P10b: same placement difference, not a second occurrence of naturel.",
    11: "P11a–P11d: full marginal text, doubtful sign state and independent équivalentes; no empty placeholder used for readable lines.",
    12: "P12: no display terminal point.",
    13: "P13a: joue le rôle d'un découpage cônique, not H's germe de residue.",
    14: "P13b: suivant read from the ink.",
    15: "P13c/P13d: doubtful ci-dessus retained without an invented terminal stop; H's editorial note excluded.",
    16: "P14a: one live Une, with only X-prime raised; no duplicate old/new Une.",
    17: "P14b: fermée absent at this location.",
    18: "P15b/P16a: literal equals shorthand and plural images inverses.",
    19: "P16b: fermé, no extra final e.",
    20: "P18a–P18d: old f. resolved, old et added cautiously, raised description and its cancellation distinguished, H's extra wording not supplied.",
    21: "P18e: whole old decorated X-prime formula retained with lowered-mark doubt.",
    22: "P18f: live f, no stop and no expansion.",
    23: "P18g: literal s. retained.",
    24: "P19a: calligraphic E is present.",
    25: "P20: completer lexeme resolved over remplacer; only accent remains in doubt.",
    26: "P21: raised tilde X-prime_1 represented above-left of closure; no equals invented.",
    27: "P22a: où, not an initial equals sign.",
    28: "P22b: vois. retained; H's final editorial annotation belongs to P21.",
    29: "P23: thin22 retained.",
}
physical_diffs = (PACKET / "differences.tsv").read_text().splitlines()[1:]
assert len(physical_diffs) == len(coverage) == 29
assert all(line.split("\t")[0] == "150_scan023" for line in physical_diffs)

revision_review = [
    dict(text="deux", scope_attachment="Raised above the heading and attached before catégories.", evidence="P03 shows a curved leader under the raised word; no additional textual punctuation is made from the leader."),
    dict(text=r"\deleted{\unsure{ainsi définies|définies ainsi}}", scope_attachment="Both old heading words are struck; colon survives to their right.", evidence="P03 long crossing line passes through both groups; word order remains locally doubtful."),
    dict(text=r"\deleted{\unsure{couples|triples}}\inserted{systèmes}", scope_attachment="Old noun after celle des replaced by systèmes on the raised baseline.", evidence="P04 horizontal strike through old noun; raised new word has its own descender and accent."),
    dict(text=r"\deleted{\unsure{Comme} Alors}", scope_attachment="Old phrase after the period following X, at the end of the conical-definition line.", evidence="P09 one long independent stroke crosses Comme and Alors; Comme's centre remains uncertain."),
    dict(text=r"\deleted{\unsure{le}}", scope_attachment="Separate old item at the next line's start before live Alors.", evidence="P10 tall loop and low ending crossed independently; H omission is not treated as proof of absence."),
    dict(text="ci-dessus", scope_attachment="Raised insertion between naturel and de a).", evidence="P09/P10 curved leader descends to that gap; it does not precede naturel."),
    dict(text=r"\unsure{\deleted{$\simeq$}|$\simeq$}", scope_attachment="Possible cancelled old sign before the independent word équivalentes in the upper margin.", evidence="P11 dense overtracing; exact sign/state uncertain. Oblique main-text strokes are not counted as a blanket marginal cancellation."),
    dict(text=r"Une partie \inserted{$X'$}", scope_attachment="Une partie is live; X-prime alone is raised between partie and de X.", evidence="P14 only one Une, no independent cancellation through it; long curve is a leader. Main leader and uncertain marginal ci-dessus are kept separate."),
    dict(text=r"\deleted{Pour que $X'$ soit}\inserted{Pour que $X'$ soit}", scope_attachment="The old complete phrase is struck and repeated above it; the replacement continues into live compatibles on the next main line.", evidence="P17 shows both full phrases and a long independent lower strike."),
    dict(text=old_f, scope_attachment="Entire old clause cancelled; raised une description inside it has an additional separate cancellation on its own baseline.", evidence="P18 old f. point is clear, et remains crossed and doubtful, que and the whole decorated X-prime formula are included. The short down-curved hook is a leader, not a supplied s."),
    dict(text=r"\inserted{il f et s. que l'on ait}", scope_attachment="Added lower replacement baseline for the preceding old clause.", evidence="P18 single live f with no independent stop, clear et, s with point, que l'on ait. No full-word expansion."),
    dict(text=r"\inserted{\widetilde X'_1}", scope_attachment="Raised above-left of the following whole closure expression.", evidence="P21 separate tilde, prime and lowered 1; no equals sign in the intervening space."),
    dict(text="Overworked folio, dotted-X body, initial Une and germe", scope_attachment="No earlier textual state is asserted solely from retracing.", evidence="P01, P05, P14 and P19 have dense/repeated bodies but no recoverable earlier glyph; only the independent P05 upper-right group receives a new unreadable-ink marker."),
]

report = dict(
    page="150_scan023", reader="reader_c", line_count=22,
    changes=changes, decisions=decisions, inventory=inventory,
    audit_boxes=audits, doubts=doubts, notes=notes,
    check_events=check_events, notation=notation,
    abbreviations=abbreviations, hand=hand,
    diff_coverage=[dict(row=i, disposition=coverage[i]) for i in range(1, 30)],
    deletion_insertion_review=revision_review
)

marks = [line.split("\t")[0] for line in (PACKET / "marks.tsv").read_text().splitlines()[1:]]
assert [row["id"] for row in decisions] == marks
assert len({row["id"] for row in changes}) == len(changes)
assert all(row["against_c"] or row["against_h"] for row in changes)
for row in changes:
    assert (ROOT / "work" / row["crop"]).is_file()
for row in audits:
    x0, y0, x1, y1 = row["xyxy"]
    assert 0 <= x0 < x1 <= 1688 and 0 <= y0 < y1 <= 2366

text_only = without_comments(F)
depth = 0
for char in text_only:
    if char == "{":
        depth += 1
    elif char == "}":
        depth -= 1
        assert depth >= 0
assert depth == 0
assert text_only.count(r"\[") == text_only.count(r"\]") == 1
assert text_only.count("$") % 2 == 0
assert "\\illegible" not in text_only
(OUT / "report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
(OUT / "structural_checks.json").write_text(json.dumps({
    "page": "150_scan023",
    "changes": len(changes), "marks": len(decisions), "crops": len(BOX),
    "audit_boxes": len(audits), "physical_diff_rows": len(physical_diffs),
    "exact_witness_excerpts_checked": True,
    "final_excerpts_checked_against_comment_stripped_draft": True,
    "audit_readings_checked_against_comment_stripped_draft": True,
    "brace_balance": True, "math_delimiter_balance": True,
    "compiled": False, "ocr": False, "new_image_views": False
}, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"changes": len(changes), "marks": len(decisions), "crops": len(BOX),
                  "audit_boxes": len(audits), "diff_rows": len(physical_diffs)}))
