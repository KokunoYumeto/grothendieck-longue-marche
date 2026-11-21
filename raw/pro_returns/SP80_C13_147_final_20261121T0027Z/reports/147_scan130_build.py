from pathlib import Path
import json

BASE = Path("/workspace/scratch/12caffedf246/edition")
PACKET = Path("/workspace/scratch/12caffedf246/packets/147_scan130")
OUT = BASE / "reports"
manifest = [json.loads(s) for s in (OUT / "147_scan130_crops.jsonl").read_text().splitlines()]
crops = {Path(x["crop"]).stem.removeprefix("147_scan130_"): x for x in manifest}
C = (PACKET / "C.tex").read_text()
H = (PACKET / "H.tex").read_text()

# These paths reproduce strokes. They do not assert complete arrowheads or words.
connector = r"\mathrel{\tikz[baseline=-.5ex,x=1em,y=1em]{\draw[line width=.45pt,line cap=round] (0,0)--(1.15,0)--(1.10,-.08);}}"
pair_one = r"\mathrel{\tikz[baseline=-.5ex,x=1em,y=1em]{\draw[line width=.45pt,line cap=round] (0,.07)--(.15,.14); \draw[line width=.45pt,line cap=round] (.27,0)--(1.05,0);}}"
pair_two = r"\mathrel{\tikz[baseline=-.5ex,x=1em,y=1em]{\draw[line width=.45pt,line cap=round] (0,.08)--(.14,.10); \draw[line width=.45pt,line cap=round] (.26,0)--(1.02,0);}}"
point_dash = r"{\cdot\, -}"

upper_margin = (
    r"du moins si les $\unsure{\Pi_2|\pi_2}$ de "
    r"$D_{d_0}^{\unsure{\circ|0}}$ et "
    r"$D^*_{d_0,\unsure{-,|-}d_r}$ sont nuls..."
)
lower_margin = r"du moins si $\unsure{\Pi_2|\pi_2}(D^*_{d_0,-d_r})=0\ldots$"
annotation = (
    r"\overbrace{T_{d_0}}^{\substack{\text{syst. loc.}\,\unsure{\text{?}}\quad"
    r"\inserted{(\overset{\mathrm{loc}}{\simeq}\mathbb Z^{d_0})}}}"
)
cancelled_t = r"\deleted{T^*_{d_0,\unsure{-},d_r}=}"
local_system = r"\simeq\text{syst. local des }\unsure{\Pi_1|\pi_1}\text{ (ou des }H_1\text{)}"
fibre_line = r"\text{des fibres de }P_{d_0-d_r}\text{ sur }D_{d_0-d_r}"
restriction = r"T^*_{d_0-d_r}=T_{d_0-d_r}\mid D^*_{d_0,-,d_r},"
cancelled_coproduct = r"\deleted{\unsure{\widetilde\Pi_{*\Delta_r}|\Pi_{\Delta_r}}=\coprod\Pi_{d_0,-,d_r}}"
cancelled_condition = r"\deleted{\unsure{d_r\geq-\geq d_0}}"
tuple_condition = r"(d_0,-,d_r)\in\mathbb N^{r+1}"
live_condition = r"d_0\geq d_1\," + point_dash + r"\,\geq d_r"
g_sum = (
    r"\unsure{G_{\Delta_r}|B_{\Delta_r}}="
    r"\coprod_{\substack{" + cancelled_condition + r"\\" + tuple_condition
    + r"\\" + live_condition + r"}}"
    r"\unsure{B_{d_0,-d_r}|G_{d_0,-d_r}}\qquad\text{groupe sur }D_{\Delta_r}"
)
p_sum = r"P_{\Delta_r}=\coprod P_{d_0,-,d_r}\qquad\text{torseur sous }G_{\Delta_r}"
t_sum = r"T_{\Delta_r}=\coprod T_{d_0,-,d_r}"
description_middle = r"\unsure{\Pi_1|\pi_1}\text{, }\unsure{\text{ou}}\ H_1\text{, de}"
description_last = r"G_{\Delta_r}\ " + pair_one + r"\ P_{\Delta_r},\ " + pair_two
final_word = r"\unsure{\text{dire}|\text{dira}|\text{dés}}"
final_group = r"G^*_{\Delta_r},\ P^*_{\Delta_r},\ T^*_{\Delta_r}"
final_restrictions = r"\text{les restrictions à }D^*_{\Delta_r}"

tex = r"""\scanpage{130}
\mspage{64}
les flèches verticales sont des morphismes
d'extensions par des noyaux qui sont des $\mathbb Z^{d_0}$
tordus -- en fait par les systèmes locaux
$T_{d_0}$, et son image inverse sur $D^*_{d_0,-,d_r}$ --
on pose donc
\margin{@@UPPER_MARGIN@@}
\[
\tag{\unsure{210}}
\left\{\begin{aligned}
T_{d_0,-,d_r}&=\text{image inverse de }@@ANNOTATION@@\text{ (sur }D_{d_0},\\
&\qquad\text{par }D_{d_0,-,d_r}@@CONNECTOR@@D_{d_0}\\
@@CANCELLED_T@@
&@@LOCAL_SYSTEM@@\\
&\qquad@@FIBRE_LINE@@\\
T^*_{d_0-d_r}&=T_{d_0-d_r}\mid D^*_{d_0,-,d_r},
\end{aligned}\right.
\]
de sorte que $\widetilde\Pi_{d_0,-,d_r}$ est une ext. de
$\Pi_{d_0,-,d_r}$ par $T^*_{d_0,-d_r}$.
\margin{@@LOWER_MARGIN@@}

On posera bien sûr
\[
@@CANCELLED_COPRODUCT@@
\]
\[
\tag{211}
\left\{\begin{aligned}
\unsure{G_{\Delta_r}|B_{\Delta_r}}&=
\coprod_{\substack{@@CANCELLED_CONDITION@@\\@@TUPLE_CONDITION@@\\@@LIVE_CONDITION@@}}
\unsure{B_{d_0,-d_r}|G_{d_0,-d_r}}\qquad\text{groupe sur }D_{\Delta_r}\\
P_{\Delta_r}&=\coprod P_{d_0,-,d_r}\qquad\text{torseur sous }G_{\Delta_r}\\
T_{\Delta_r}&=\coprod T_{d_0,-,d_r}\qquad\text{système local des}\\
&\hspace{4cm}@@DESCRIPTION_MIDDLE@@\\
&\hspace{4cm}@@DESCRIPTION_LAST@@\\
@@FINAL_GROUP@@&\qquad@@FINAL_WORD@@\\
&\qquad@@FINAL_RESTRICTIONS@@
\end{aligned}\right.
\]
\margin{129}
"""
for key, value in {
    "UPPER_MARGIN": upper_margin, "LOWER_MARGIN": lower_margin,
    "ANNOTATION": annotation, "CONNECTOR": connector,
    "CANCELLED_T": cancelled_t, "LOCAL_SYSTEM": local_system,
    "FIBRE_LINE": fibre_line, "CANCELLED_COPRODUCT": cancelled_coproduct,
    "CANCELLED_CONDITION": cancelled_condition, "TUPLE_CONDITION": tuple_condition,
    "LIVE_CONDITION": live_condition, "DESCRIPTION_MIDDLE": description_middle,
    "DESCRIPTION_LAST": description_last, "FINAL_GROUP": final_group,
    "FINAL_WORD": final_word, "FINAL_RESTRICTIONS": final_restrictions,
}.items():
    tex = tex.replace("@@" + key + "@@", value)
assert "@@" not in tex

rows = []
def row(place, c, h, final, ink, crop, confidence, kind, against_c, against_h,
        category, marked_h=False, consequential=False, box=None):
    n = len(rows) + 1
    item = {
        "row": f"R{n:02d}", "place": place, "C": c, "H": h, "final": final,
        "scan_shows": ink, "crop": crops[crop]["crop"] if crop else None,
        "box": crops[crop]["box"] if crop else box,
        "confidence": confidence, "kind": kind,
        "against_C": against_c, "against_H": against_h,
        "marked_in_H": marked_h, "math_consequential": consequential,
        "error_category": category,
    }
    if crop is None:
        item["source_image"] = str(PACKET / "top.jpg")
        item["evidence_scope"] = "Native top half read once; no new first-pass crop was made of this already settled boundary."
    rows.append(item)
    return item["row"]

row("opening prose, alphabet of the twisted kernel",
    r"\mathbf Z^{d_0}", r"\mathbb{Z}^{d_0}", r"\mathbb Z^{d_0}",
    "The Z has two separate oblique diagonal strokes between its upper and lower horizontals. The exponent is d with a low closed 0.",
    "opening_z", "high", "misread symbol or index", True, False, "Symbols and indices")
row("opening prose, image-inverse base",
    r"D^*_{d_0,\ldots,d_r}", r"D^{*}_{d_0,\dots,d_r}", r"D^*_{d_0,-,d_r}",
    "After d_0 there is a separate low comma, one continuous horizontal stroke, then a second separate comma before d_r. The star is separate above D.",
    "image_inverse_d", "high", "misread symbol or index", True, True, "Symbols and indices")
row("opening prose, the words before (210)",
    "on pose donc", r"\uncertain{posons} donc", "on pose donc",
    "The small leading on precedes the long descending p; pose ends before the separate d of donc. There is no terminal ns joined to pose.",
    "on_pose", "high", "misread word", False, True, "Words", marked_h=True)
row("upper slanted qualification, opening words",
    "du moins si les", r"dès \uncertain{qu'on suppose}", "du moins si les",
    "The first word has a d loop and connected u; moins has its separate i point; si is followed by the tall loop of les. The note does not begin dès and contains no qu'on suppose.",
    "upper_margin", "high", "misread word", False, True, "Words", marked_h=True)
row("upper slanted qualification, the two bases and plural conclusion",
    r"$\pi_2$ de $D_{d_0}^{\unsure{\circ|*|0}}$ et \unsure{$D^*_{d_0,-,d_r}$|$D_{d_0}^*$ etc.} sont nuls...",
    r"$\pi_2$ de $D_{d_0}$ \uncertain{nul} \ill{}…",
    r"$\unsure{\Pi_2|\pi_2}$ de $D_{d_0}^{\unsure{\circ|0}}$ et $D^*_{d_0,\unsure{-,|-}d_r}$ sont nuls...",
    "The homotopy sign has a straight top and two upright legs, hence a capital-Pi-leading local doubt. A closed high loop, not a secure star, sits over the first D. The conjunction et and a second D with a separate star and final d_r are visible. The middle dash/comma strokes overlap and cannot be stratified into a deletion. The lower line reads sont nuls followed by three points.",
    "upper_margin", "medium", "misread symbol or index", True, True, "Symbols and indices", marked_h=True, consequential=True)
row("opening baseline, H's extra illegible text before les",
    "(nothing)", r"\ill{}", "(nothing)",
    "The native top half begins the main prose with les; the neighboring slanted qualification and its separator belong to the margin. No separate main-baseline word precedes les.",
    None, "high", "text not on the page", False, True, "Text that is not on the page",
    marked_h=True, box=[395,65,1675,139])
row("(210), first defined T index",
    r"T_{d_0,\ldots,d_r}", r"T_{d_0,\dots,d_r}", r"T_{d_0,-,d_r}",
    "The low index contains comma, one solid horizontal dash, and another comma; the final d_r is separate. There are not three individually written dots.",
    "first_definition", "high", "misread symbol or index", True, True, "Symbols and indices")
row("(210), raised annotation attached to T_d0",
    r"\text{syst. loc.\ \inserted{$(\overset{\mathrm{loc}}{\simeq}\mathbf Z^{d_0})$}}",
    r"$T_{d_0}$ : syst. local \uncertain{de rang} $d_0$ ($\overset{\text{loc}}{\simeq} \mathbb{Z}^{d_0}$)",
    r"\text{syst. loc.}\,\unsure{\text{?}}\quad\inserted{(\overset{\mathrm{loc}}{\simeq}\mathbb Z^{d_0})}",
    "syst. and loc. both end in visible points. A separate raised curling glyph follows loc.; it favors a question mark but lacks a secure independent lower dot. There are no de rang letters or a separate rank d_0. The added parenthesis has loc above one wave and one bar, a double-diagonal Z, and exponent d_0. The leaders associate these annotations with the preceding T_d0; the second is written above the opening sur phrase.",
    "annotation", "medium", "omission", True, True, "Omissions", marked_h=True)
row("(210), punctuation after sur D_d0",
    r"\text{ (sur }D_{d_0},", r"\text{ (sur } D_{d_0}\text{)}", r"\text{ (sur }D_{d_0},",
    "At the far right there is a short low descending comma. It is much lower and shorter than the opening parenthesis; no full closing parenthesis is supplied.",
    "annotation", "high", "misread symbol or index", False, True, "Other")
row("(210), par D connector and its full index",
    r"\text{par }D_{d_0,\ldots,d_r}\unsure{\text{---}|\longrightarrow}D_{d_0}",
    r"\text{ par } D_{d_0,\dots,d_r} \to D_{d_0}",
    r"\text{par }D_{d_0,-,d_r}" + connector + r"D_{d_0}",
    "The source index has comma, single dash, comma. The connector is one shaft with a dark right cap and a tiny lower spur. A second head flank is not secure. The literal terminal-turn path preserves the strokes without asserting a complete arrowhead.",
    "relation", "medium", "drawing or diagram", True, True, "Drawings and diagrams", consequential=True)
row("(210), cancelled beginning of the local-system row",
    r"\deleted{\unsure{T^*_{d_0,\ldots,d_r}|D^*_{d_0,\ldots,d_r}}=}",
    r"T^{*}_{d_0,\dots,d_r} =",
    cancelled_t,
    "A broad top bar and central descending stem support T; there is no independent right bowl apart from the cancellation zigzag. The star, the two index commas, d_0, d_r, and the upper equality stroke survive. The central index dash is crossed and remains locally doubtful. H reports this cancellation in an editorial note; its deletion state is therefore not counted as an omission.",
    "cancelled_t", "medium", "misread symbol or index", True, True, "Symbols and indices", consequential=False)
row("(210), homotopy symbol in the local-system description",
    r"\pi_1", r"\pi_1", r"\unsure{\Pi_1|\pi_1}",
    "The sign is retraced, with straight upright legs and two close horizontal traces. Its visible capital-Pi outline leads; lowercase pi remains an alternative. The mathematical role does not settle the graphic case.",
    "local_system", "medium", "misread symbol or index", True, True, "Symbols and indices", consequential=True)
row("(210), fibre baseline and relative base",
    r"\text{des fibres de }P_{d_0- d_r}/D_{d_0- d_r}",
    r"\text{ des fibres de } P_{d_0 \dots d_r}",
    fibre_line,
    "The joining group after P has an s-like entrance followed by low connected u/r strokes before D: it is sur, not a single slash. Both P and D carry d_0-d_r with one dash and no separate commas; the small final D index reaches the page edge.",
    "fibres", "high", "misread word", True, True, "Words", consequential=True)
row("(210), final restriction row",
    r"T^*_{d_0- d_r}&=T_{d_0- d_r}\mid D^*_{d_0,\ldots,d_r},",
    r"T^{*}_{d_0 \dots d_r} = T_{d_0 \dots d_r} \mid D^{*}_{d_0,\dots,d_r} ,",
    restriction,
    "The two T indices have a single dash without independent commas. The restricted D index instead has comma-dash-comma. Both high stars and the restriction upright are visible; a final low comma is present.",
    "restriction", "high", "misread symbol or index", True, True, "Symbols and indices")
row("extension paragraph, introductory words",
    "de sorte que", "dès lors que", "de sorte que",
    "The initial de is followed by the separate s entrance, low or joins, and upright t of sorte. There is no l beginning a word lors.",
    "extension_upper", "high", "misread word", False, True, "Words")
row("extension paragraph, upper group index",
    r"\widetilde\Pi_{d_0,\ldots,d_r}", r"\widetilde{\Pi}_{d_0,\dots,d_r}",
    r"\widetilde\Pi_{d_0,-,d_r}",
    "The tilde is a separate wave above the capital Π. The index contains a low comma after 0, one horizontal stroke, then another comma before d_r.",
    "extension_upper", "high", "misread symbol or index", True, True, "Symbols and indices")
row("extension paragraph, lower group and kernel indices",
    r"$\Pi_{d_0,\ldots,d_r}$ par $T^*_{d_0- d_r}$.",
    r"$\Pi_{d_0,\dots,d_r}$ par $T^{*}_{d_0,\dots,d_r}$.",
    r"$\Pi_{d_0,-,d_r}$ par $T^*_{d_0,-d_r}$.",
    "The Π index has commas on both sides of a single dash. The T* index has a distinct low comma after d_0 and no separate comma after the dash. This differs from the two comma-free T indices in the restriction row. The sentence has a terminal point.",
    "extension_lower", "high", "misread symbol or index", True, True, "Symbols and indices")
row("second slanted qualification, words",
    "du moins si", r"dès \uncertain{qu'on suppose}", "du moins si",
    "The first line reads du moins si, with the d upright and low u, the dotted i in moins, and the separate si; there is no qu'on suppose group.",
    "second_margin", "high", "misread word", False, True, "Words", marked_h=True)
row("second slanted qualification, whole formula",
    r"\pi_2(D^*_{d_0,-d_r})=0\ldots",
    r"\pi_2(D^{*}_{d_0,\dots,d_r}) = 0",
    r"\unsure{\Pi_2|\pi_2}(D^*_{d_0,-d_r})=0\ldots",
    "The initial symbol has a straight cap and two long upright legs, giving the capital-Pi-leading case doubt. D has a separate star. Its index has a comma after d_0, one dash, then d_r without another comma. The closing parenthesis, equality, zero, and three terminal points are visible.",
    "second_margin", "medium", "misread symbol or index", True, True, "Symbols and indices", consequential=True)
row("prose immediately before the cancelled coproduct",
    "On posera bien sûr", "On pourra bien sûr", "On posera bien sûr",
    "After p and the small open o, the curved s/e joins lead into r and a; the word is posera. bien has an i point, and sûr has a separate circumflex.",
    "on_posera", "high", "misread word", False, True, "Words")
row("cancelled coproduct before (211), complete baseline",
    r"\deleted{\[\unsure{\widetilde\Pi_{*\Delta_r}|\Pi_{\Delta_r}}=\coprod\Pi_{d_0,\ldots,d_r}\]}",
    r"\text{\struck{$\Pi_{\Delta_r} = \coprod \Pi_{d_0,\dots,d_r}$}}",
    cancelled_coproduct,
    "Several long oblique and looping strokes cancel the entire equation. The left Π, Δ_r, equality, coproduct, and right Π survive. The high rough trace above the first Π and crowded lower star-like cluster remain ambiguous, so the old C doubt is retained. The right index plainly has comma-dash-comma. No extra high label is recovered from cancellation scribbles.",
    "cancelled_coproduct", "medium", "misread symbol or index", True, True, "Symbols and indices", consequential=True)
row("(211), first right-hand summand",
    r"\unsure{G_{d_0,-d_r}|B_{d_0,-d_r}}",
    r"G_{d_0,\dots,d_r}", r"\unsure{B_{d_0,-d_r}|G_{d_0,-d_r}}",
    "The right summand has an upright and two right-hand bowls, without the broad left loop of the clearer G elsewhere. B therefore leads, with G retained because of retracing. Its index has a comma after d_0, one dash, and d_r. This changes C's primary reading even though G is retained as an alternative.",
    "g_coproduct", "medium", "misread symbol or index", True, True, "Symbols and indices", consequential=True)
row("(211), all three lines under the first coproduct",
    r"\substack{\deleted{\unsure{d_r\geq\cdots\geq d_0}}\\(d_0,\ldots,d_r)\in\mathbf N^{r+1}\\d_0\geq d_1\cdots\geq d_r}",
    r"\substack{(d_0,\dots,d_r) \in \mathbb{N}^{r+1} \\ d_0 \geqslant d_1 \geqslant \dots \geqslant d_r}",
    r"\substack{" + cancelled_condition + r"\\" + tuple_condition + r"\\" + live_condition + "}",
    "The first condition is separately struck by a horizontal line; d_r and the inequality strokes are crowded, and the central short horizontal mark remains within a retained doubt. The live tuple has comma-dash-comma; N has a doubled oblique stroke and exponent r+1. The last live line has d_0≥d_1, then a point and short dash, then ≥d_r. There is no additional ≥ immediately after d_1. H's editorial note recognizes the struck condition; its strike state is not counted as omitted.",
    "g_coproduct", "medium", "misread symbol or index", True, True, "Symbols and indices", consequential=True)
row("(211), P summand index",
    r"P_{d_0,-d_r}", r"P_{d_0,\dots,d_r}", r"P_{d_0,-,d_r}",
    "A low comma follows d_0; a single horizontal dash is followed by another low comma before d_r.",
    "p_coproduct", "high", "misread symbol or index", True, True, "Symbols and indices")
row("(211), T summand index",
    r"T_{d_0,-d_r}", r"T_{d_0,\dots,d_r}", r"T_{d_0,-,d_r}",
    "Both commas are distinct below the single index dash. The visible last r is a low curved stroke.",
    "t_coproduct", "high", "misread symbol or index", True, True, "Symbols and indices")
row("(211), homotopy symbol in the T description",
    r"\pi_1", r"\pi_1", r"\unsure{\Pi_1|\pi_1}",
    "The sign has a nearly straight cap and two descending legs. The capital-Pi graphic form leads, while lowercase pi remains possible in this hand; the nearby H_1 is plainly an H.",
    "system_description", "medium", "misread symbol or index", True, True, "Symbols and indices", consequential=True)
row("(211), commas in the homotopy/homology description",
    r"\pi_1\text{, ou }H_1\text{, de}", r"\pi_1 \text{ ou } H_1 \text{ de}",
    description_middle,
    "There is a separate low comma after the first indexed symbol and another after H_1. The intervening extremely reduced ou is retained under local uncertainty; the commas themselves are secure.",
    "system_description", "high", "omission", False, True, "Other")
row("(211), marks between G and P and following P",
    r"G_{\Delta_r}\text{ -- }P_{\Delta_r}\text{, --}",
    r"G_{\Delta_r} \text{ ou } P_{\Delta_r} \text{ au choix}",
    description_last,
    "Each group consists of a short raised oblique or horizontal stroke followed by a longer horizontal stroke; the second follows a separate comma. Their interpretation as extremely reduced ou or as separators is left open. The actual paired strokes are drawn. There are no separate letters spelling choix.",
    "system_description", "medium", "drawing or diagram", True, True, "Drawings and diagrams")
row("(211), final compressed word and following les",
    r"\unsure{\text{dés}|\text{dire}}\ \text{les restrictions à }D^*_{\Delta_r}",
    r"leurs restrictions à $D^{*}_{\Delta_r}$",
    final_word + r"\ \text{les restrictions à }D^*_{\Delta_r}",
    "The word has a d loop/upright, a high point over a short central trace, and a small final loop or join. dire leads, with dira and dés retained; grammar does not decide it. The next baseline begins les, followed by restrictions à, rather than a single leurs. The final word change is counted against C's primary dés.",
    "final_restrictions", "medium", "misread word", True, True, "Words")
row("(211), absent terminal point",
    r"D^*_{\Delta_r}.", r"D^{*}_{\Delta_r}", r"D^*_{\Delta_r}",
    "The last D* and Δ_r end in clear blank paper. No secure terminal full stop is visible to their right.",
    "final_restrictions", "high", "text not on the page", True, False, "Text that is not on the page")
row("(211), scope of the large left brace",
    r"G^*_{\Delta_r},\ P^*_{\Delta_r},\ T^*_{\Delta_r}&\qquad\unsure{\text{dés}|\text{dire}}\ \text{les restrictions à }D^*_{\Delta_r}.\end{aligned}\right.",
    r"$G^{*}_{\Delta_r}$, $P^{*}_{\Delta_r}$, $T^{*}_{\Delta_r}$ leurs restrictions à $D^{*}_{\Delta_r}$",
    final_group + r"\qquad" + final_word + r"\\\qquad" + final_restrictions,
    "On the native bottom half the large left brace continues below both the starred row and les restrictions, ending near y2300. These two baselines remain inside that brace. The tight crop records their words and symbols; the brace extent was settled on the native half.",
    "final_restrictions", "high", "insertion or placement", False, True, "Insertions put in the wrong place")
row("lower-left pencil archive number",
    r"\margin{129}", "(nothing)", r"\margin{129}",
    "Three pencil digits read 129: an angled-top 1, a bent 2 with a long foot, and a looped 9 with a descending tail.",
    "archive_number", "high", "omission", False, True, "Omissions")

decisions = []
def decision(mid, result, reading, ink, crop, confidence):
    decisions.append({
        "id": mid, "decision": result, "reading": reading, "ink": ink,
        "crop": crops[crop]["crop"], "box": crops[crop]["box"],
        "confidence": confidence,
    })
decision("M1290", "undecided", r"\unsure{\circ|0}",
         "The high sign over the first D is a closed loop with a thick return. It has no secure star rays; degree-circle versus zero is not settled.",
         "upper_margin", "medium")
decision("M1291", "other", r"$D^*_{d_0,\unsure{-,|-}d_r}$",
         "D, its separate high star, d_0, and final d_r are visible. The internal dash/comma shape is crossed and crowded. It is not merely D_d0* followed by etc.; no distinct cancelled earlier symbol can be stratified.",
         "upper_margin", "medium")
decision("M1292", "other", connector,
         "One shaft, a thick right cap, and a tiny lower spur are visible. A complete second head flank is not secure, so the visible path is drawn and direction remains open.",
         "relation", "medium")
decision("M1293", "undecided", r"\unsure{B_{d_0,-d_r}|G_{d_0,-d_r}}",
         "An upright and two right bowls favor B; retracing prevents complete exclusion of G. B replaces C's primary G and is counted against C.",
         "g_coproduct", "medium")
decision("M1294", "undecided", final_word,
         "The high point and low central/final joins favor dire but admit dira or dés. No expansion or grammatical completion is used.",
         "final_restrictions", "medium")

nested_decisions = [
    {"place": "(210), cancelled T/D choice", "decision": "first", "reading": cancelled_t,
     "ink": "The upper bar and central stem are separately visible; an independent D bowl is absent. The crossed central index dash retains its own doubt.",
     "crop": crops["cancelled_t"]["crop"], "box": crops["cancelled_t"]["box"], "confidence": "medium"},
    {"place": "cancelled coproduct before (211)", "decision": "undecided", "reading": cancelled_coproduct,
     "ink": "The high rough trace and crowded star-like lower cluster cannot be cleanly separated from cancellation strokes. The whole original C choice remains.",
     "crop": crops["cancelled_coproduct"]["crop"], "box": crops["cancelled_coproduct"]["box"], "confidence": "low"},
    {"place": "(211), struck summation condition", "decision": "undecided", "reading": cancelled_condition,
     "ink": "The first r and inequality details meet the strike. A single short horizontal central mark is more literal than three dots, but the whole cancelled condition remains marked.",
     "crop": crops["g_coproduct"]["crop"], "box": crops["g_coproduct"]["box"], "confidence": "medium"},
    {"place": "first formula label", "decision": "undecided", "reading": r"\unsure{210}",
     "ink": "The middle digit has a tall upright and a low closed retraced loop joined to the preceding 2's foot. No definite earlier numeral or alternate numeral is recovered.",
     "crop": crops["formula_210"]["crop"], "box": crops["formula_210"]["box"], "confidence": "medium"},
]

inventory_data = [
    ("text", "upper edge near x805,y35", "64", "his hand"),
    ("text", "main opening, y70–530", "les flèches verticales sont des morphismes", "his hand"),
    ("margin note", "slanted upper-left qualification, x15–395,y15–477", "du moins si les", "his hand"),
    ("display", "upper brace, y540–960; label at left", r"\unsure{210}; T_{d_0,-,d_r}", "his hand"),
    ("insertion", "above the T_d0 at the end of the first definition row", r"syst. loc. \unsure{?}", "his hand"),
    ("insertion", "raised parenthesis to the right of syst. loc., above sur D_d0", r"(\overset{\mathrm{loc}}{\simeq}\mathbb Z^{d_0})", "his hand"),
    ("deletion", "beginning of the local-system row inside (210), x513–825,y716–816", cancelled_t, "his hand"),
    ("text", "two main baselines immediately below (210), y1000–1190", "de sorte que", "his hand"),
    ("margin note", "slanted middle-left qualification, x22–357,y864–1208", "du moins si", "his hand"),
    ("text", "main baseline at y1250–1320", "On posera bien sûr", "his hand"),
    ("deletion", "whole cancelled coproduct baseline, x441–1330,y1310–1503", cancelled_coproduct, "his hand"),
    ("display", "large lower brace, y1498–2300; label (211) at left", r"G_{\Delta_r}; P_{\Delta_r}; T_{\Delta_r}", "his hand"),
    ("deletion", "first line under the first coproduct, around y1590–1620", cancelled_condition, "his hand"),
    ("text", "right-hand three-line description beside the T sum, y1850–2065", "système local des", "his hand"),
    ("text", "last two baselines inside the lower brace, y2040–2240", final_group, "his hand"),
    ("margin note", "lower-left pencil number, x20–112,y2291–2350", "129", "pencil hand; attribution not determined"),
]
inventory = [
    {"element": f"E{i:02d}", "kind": kind, "position": position,
     "first_words_or_objects": start, "sheet_kind": "text", "hand": hand,
     "transcribed": "yes"}
    for i, (kind, position, start, hand) in enumerate(inventory_data, 1)
]

doubts = [
    {"place": "upper qualification, homotopy sign", "reading": r"\Pi_2", "alternatives": r"\pi_2", "confidence": "medium"},
    {"place": "upper qualification, first D high loop", "reading": r"\circ", "alternatives": "0", "confidence": "medium"},
    {"place": "upper qualification, middle of second D index", "reading": r"D^*_{d_0,\unsure{-,|-}d_r}", "alternatives": "Dash with or without a second comma; no secure deletion stratigraphy.", "confidence": "medium"},
    {"place": "raised annotation after syst. loc.", "reading": "?", "alternatives": "Unidentified raised curling sign; its independent lower dot is not secure.", "confidence": "medium"},
    {"place": "formula number (210)", "reading": "210", "alternatives": "Middle digit has an upright and merged low loop; 200/260 were considered but are not established.", "confidence": "medium"},
    {"place": "(210), connector", "reading": connector, "alternatives": "Short dash with terminal pen return; reduced rightward arrow. The drawing does not choose direction.", "confidence": "medium"},
    {"place": "(210), cancelled first index", "reading": r"T^*_{d_0,\unsure{-},d_r}=", "alternatives": "The central index dash meets the cancellation; the leading T itself has a recoverable top bar and stem.", "confidence": "medium"},
    {"place": "(210), local-system homotopy sign", "reading": r"\Pi_1", "alternatives": r"\pi_1", "confidence": "medium"},
    {"place": "second qualification, homotopy sign", "reading": r"\Pi_2", "alternatives": r"\pi_2", "confidence": "medium"},
    {"place": "cancelled coproduct, left-hand group", "reading": r"\widetilde\Pi_{*\Delta_r}", "alternatives": r"\Pi_{\Delta_r}; the tilde and star-like cluster overlap cancellation traces.", "confidence": "low"},
    {"place": "(211), left-hand retraced group letter", "reading": "G", "alternatives": "B; no separate earlier B or direction of correction is securely recovered.", "confidence": "medium"},
    {"place": "(211), right summand letter", "reading": "B", "alternatives": "G", "confidence": "medium"},
    {"place": "(211), cancelled summation condition", "reading": r"d_r\geq-\geq d_0", "alternatives": "The first index and inequality details are crossed; the whole condition remains uncertain.", "confidence": "medium"},
    {"place": "(211), description's homotopy sign", "reading": r"\Pi_1", "alternatives": r"\pi_1", "confidence": "medium"},
    {"place": "(211), reduced word between the first indexed sign and H_1", "reading": "ou", "alternatives": "Tiny point/short stroke plus long stroke could be a separator; no grammatical decision is forced.", "confidence": "medium"},
    {"place": "(211), pair after G and pair after P comma", "reading": description_last, "alternatives": "Highly reduced ou at either place versus literal separator marks; no choix letters are visible.", "confidence": "medium"},
    {"place": "(211), final compressed word", "reading": "dire", "alternatives": "dira; dés", "confidence": "medium"},
]

notes = [
    "S130-01. The opening says that the vertical arrows are morphisms of extensions by twisted copies of Z^{d_0}, more specifically by T_{d_0} and its inverse image. The upper margin qualifies this by vanishing of the second homotopy objects of two indicated bases. This records the manuscript assertion; no homotopy-exact-sequence proof was attempted.",
    "S130-02. Formula (210) identifies a local system by inverse image and by the first homotopy or homology of fibres, then defines a starred restriction. The following paragraph asserts an extension by that restriction and repeats a vanishing qualification in the margin. These claims are carried as background, not certified by a transcription check.",
    "S130-03. The lower brace (211) introduces coproduct families G, P, T and their starred restrictions. Its intended group/torsor terminology is recorded, but the B-leading right summand is not silently replaced by the mathematically expected G.",
    "S130-04. Single horizontal index strokes were compared occurrence by occurrence. Comma-dash-comma occurs in the opening D, the first T and source D of (210), its final restricted D, both extension Π indices, the cancelled coproduct's right Π, the live summation tuple, and the P/T summands. The two restriction-row T indices and fibre P/D indices have no separate commas. The extension-par T*, second margin D*, and right B/G summand have one comma before the dash. The upper margin's middle index remains doubtful.",
    "S130-05. The second-homotopy signs in both qualifications and the first-homotopy signs in the two local-system descriptions have Π-like graphic forms. All four use a capital-leading local doubt; the homotopy meaning does not by itself establish lowercase pi. The unambiguous groupoid Π symbols in the extension paragraph retain capitals and the visible tilde.",
    "S130-06. The (210) connector is reproduced as a shaft with its short terminal downward return. The cap and lower spur do not establish a full two-sided head. No direction or morphism property was inferred from mathematical need.",
    "S130-07. The first annotation consists of syst. loc., a separate question-mark-like raised curl, and the added parenthesized local-isomorphism formula. The leaders associate these with T_d0; the latter is physically above the sur phrase. H's de rang d_0 has no separate matching ink, and loc. is not expanded in the transcription.",
    "S130-08. Three cancelled passages were checked independently: the initial T* fragment inside (210), the whole coproduct before (211), and the short condition under the first live coproduct. Their full surviving baselines are preserved in both the proposal and second boxes. Crossing strokes do not justify extracting an earlier B from the left G/B or a definite earlier numeral from the label 210.",
    "S130-09. The right summand of the first (211) row has two right bowls, so B leads G; the left letter remains G-leading because its broad left curve and retracing differ. These are visual/notation consistency checks, not a proof or a mathematical correction.",
    "S130-10. The last live summation condition contains a point followed by a short dash after d_1, represented literally. No additional inequality after d_1 is supplied. N and both occurrences of Z have visible doubled oblique strokes.",
    "S130-11. In the local-system description the reduced ou and the two later paired marks have very similar minimal shapes. The later marks are drawn literally and their ou/separator interpretation remains open. There are no separately written choix letters. The low commas after the first homotopy symbol, H_1, and P_Δr remain.",
    "S130-12. The compressed final word is ranked dire, dira, dés from its visible joins; the following baseline begins les restrictions à. The entire starred passage lies within the continuing large brace. No final full stop is added after D*_Δr.",
    "S130-13. The manuscript page number is 64 and the pencil archive number is 129. The first display label remains unsure210 because its middle digit has a tall upright and a low retraced loop; a separate earlier numeral is not established. The lower label 211 is clear. Numbering sequence was not used to force the crowded digit.",
    "S130-14. Every supplied C uncertainty, including its three unindexed nested uncertainties, and every C deletion/insertion was checked against this page's images. All C/H word disagreements were inspected in the existing 24 first-pass crops. The extra H initial ill was judged at the already-read native top boundary; no new crop was made after root's instruction to stop first-pass cropping.",
    "S130-15. The line count is 32 physical reading baselines, including the manuscript and archive numbers, the margin lines, the annotation line, and the three summation-condition baselines. Subscripts and raised loc are not counted as independent baselines. The reconciliation list fixes the units explicitly.",
]
check_events = []
for i, note in enumerate(notes, 1):
    check_events.append({
        "statement_id": f"S130-{i:02d}",
        "type": "carried as background without fault found" if i <= 3 else "used and rechecked in this run",
        "outcome": (
            "Reported the page's assertion; no proof verification was claimed."
            if i <= 3 else
            "Checked the specified ink, notation, placement, or workflow against the assigned page and existing crops; unresolved details remain marked."
        ),
    })

hand_log = [
    {"habit": "A sequence can be shortened to one continuous index dash, with independently variable commas.",
     "places": "130: opening D; all rows of (210); extension indices; both margins; cancelled coproduct; summation tuple and P/T sums.",
     "scope": "Each occurrence on this page was checked separately; this is not a rule to regularize unseen indices.",
     "misreadings": "Both witnesses repeatedly replace one stroke by ellipsis; C also omits individual visible commas."},
    {"habit": "Homotopy signs can have a straight cap and two upright legs, graphically close to capital Π.",
     "places": "130: both Π2 qualifications and the Π1 descriptions in (210) and (211).",
     "scope": "Four local case doubts remain; the graphic observation does not establish a universal letter equivalence.",
     "misreadings": "Both witnesses give lowercase pi at all four places."},
    {"habit": "A retraced group letter can acquire B-like right bowls; compare its left boundary, not only its mathematical role.",
     "places": "130: left and right letters of the first (211) row; clearer G in torseur sous and the later description.",
     "scope": "Right summand B-leading; left G-leading. No reliable order of overwritten layers is claimed.",
     "misreadings": "C's G-primary choice and H's G conceal the more B-like right outline."},
    {"habit": "Very small ou may be reduced to a short point or slash and a longer low stroke.",
     "places": "130: (ou des H1) in (210), ou between the homotopy/homology signs in (211), and the later paired marks.",
     "scope": "The first word remains ou-leading; the later pair interpretations remain open.",
     "misreadings": "C gives later dashes, while H supplies ou and au choix; choix has no matching letters."},
    {"habit": "A shortened connector can end with a thick cap and only one lower spur.",
     "places": "130: par D...D in (210).",
     "scope": "One occurrence; a full two-sided head is not established.",
     "misreadings": "H makes a complete arrow; C's leading plain dash omits the terminal turn."},
    {"habit": "Z and N are drawn with an additional oblique stroke.",
     "places": "130: opening Z, annotation Z, and N^{r+1} under the first coproduct.",
     "scope": "All three occurrences on this page.",
     "misreadings": "C uses bold alphabets where H's blackboard alphabets better preserve the visible double stroke."},
]
notation = [
    {"notation": r"T_{d_0,-,d_r},\ T^*_{d_0-d_r}",
     "meaning_or_form": "Different literal index punctuation on this page; one continuous dash is preserved, not automatically changed into ellipsis or interpreted as subtraction.",
     "places": "130, (210), extension paragraph, (211)."},
    {"notation": r"D_{d_0}^{\unsure{\circ|0}}",
     "meaning_or_form": "First base in the upper qualification has a closed high loop; circle versus zero remains open.",
     "places": "130, upper margin."},
    {"notation": r"\unsure{\Pi_1|\pi_1},\ \unsure{\Pi_2|\pi_2}",
     "meaning_or_form": "Capital-like graphic forms in homotopy contexts, retained under local case doubt.",
     "places": "130, two margins and two local-system descriptions."},
    {"notation": r"\unsure{B_{d_0,-d_r}|G_{d_0,-d_r}}",
     "meaning_or_form": "Right-hand summand has B-like double bowls; the expected family name does not override the visible form.",
     "places": "130, first row of (211)."},
    {"notation": point_dash,
     "meaning_or_form": "Literal point plus short dash in the last summation condition; its expansion as an ellipsis is not put in the text.",
     "places": "130, last condition under the first coproduct."},
    {"notation": r"\mathbb Z,\ \mathbb N",
     "meaning_or_form": "Both letter forms have an extra diagonal stroke on this page.",
     "places": "130, opening, annotation, summation domain."},
]
abbreviations = [
    {"form": "syst.", "expansion": "système"},
    {"form": "loc.", "expansion": "local"},
    {"form": "loc above the isomorphism sign", "expansion": "localement"},
    {"form": "ext.", "expansion": "extension"},
]

second_boxes = []
def second(kind, coords, reading, scope=None):
    d = {"box": f"B{len(second_boxes)+1:02d}", "kind": kind, "coords": coords, "reading": reading}
    if scope:
        d["scope"] = scope
    second_boxes.append(d)

second("number", [793,15,887,73], "64")
second("different words", [395,65,1675,139], "les flèches verticales sont des morphismes")
second("number", [1410,137,1660,245], r"$\mathbb Z^{d_0}$")
second("number", [245,328,1680,463], r"$T_{d_0}$, et son image inverse sur $D^*_{d_0,-,d_r}$ --")
second("different words", [247,474,800,550], "on pose donc")
second("margin note", [15,15,395,477], upper_margin, "Complete slanted qualification; partial adjoining main-text strokes at the rectangle's boundary are outside the note.")
second("insertion", [512,472,1680,642],
       r"$T_{d_0,-,d_r}=\text{image inverse de }" + annotation + r"\text{ (sur }D_{d_0},$")
second("doubtful formula", [863,634,1427,716],
       r"$\text{par }D_{d_0,-,d_r}" + connector + r"D_{d_0}$")
second("struck passage", [513,707,1680,816],
       "$" + cancelled_t + r"\quad" + local_system + "$")
second("different words", [928,765,1688,886], "$" + fibre_line + "$")
second("number", [516,842,1445,967], "$" + restriction + "$")
second("number", [228,603,375,689], r"(\unsure{210})")
second("different words", [237,963,1606,1097],
       r"de sorte que $\widetilde\Pi_{d_0,-,d_r}$ est une ext. de")
second("number", [246,1091,1043,1210], r"$\Pi_{d_0,-,d_r}$ par $T^*_{d_0,-d_r}$.")
second("margin note", [22,864,357,1208], lower_margin, "Complete slanted qualification; partial adjoining main-text strokes at the rectangle's boundary are outside the note.")
second("different words", [247,1227,950,1340], "On posera bien sûr")
second("struck passage", [441,1310,1330,1503], "$" + cancelled_coproduct + "$")
second("doubtful formula", [540,1498,1669,1716], "$" + g_sum + "$")
second("number", [246,1702,393,1805], "(211)")
second("number", [542,1693,1680,1819], "$" + p_sum + "$")
second("doubtful formula", [550,1820,1666,2075],
       r"\[\begin{aligned}" + t_sum + r"&\qquad\text{système local des}\\&"
       + description_middle + r"\\&" + description_last + r"\end{aligned}\]")
second("different words", [572,2037,1507,2262],
       r"\[\begin{aligned}" + final_group + r"&\qquad" + final_word + r"\\&"
       + final_restrictions + r"\end{aligned}\]")
second("number", [20,2291,112,2350], "129")
second("struck passage", [704,1572,901,1628], "$" + cancelled_condition + "$")

deletion_insertion_checks = [
    {"span": r"\inserted{$(\overset{\mathrm{loc}}{\simeq}\mathbf Z^{d_0})$}",
     "finding": "This parenthesized formula is raised above the sur phrase and connected near T_d0 by a long curved leader. It is live and not struck. loc is above one wave plus bar; Z has a doubled diagonal. The adjacent syst. loc. and separate raised curl also belong to the annotation."},
    {"span": r"\deleted{\unsure{T^*_{d_0,\ldots,d_r}|D^*_{d_0,\ldots,d_r}}=}",
     "finding": "The zigzag crosses the initial letter, index, and equality fragment. It stops before the live simeq/local-system text to the right. The high star survives; T is favored by its independent top bar and stem. The crossed index dash keeps a local doubt."},
    {"span": r"\deleted{\[\unsure{\widetilde\Pi_{*\Delta_r}|\Pi_{\Delta_r}}=\coprod\Pi_{d_0,\ldots,d_r}\]}",
     "finding": "The long oblique and looping strokes cancel the whole displayed baseline, including both sides and the equality. The live On posera above and first G/B row below are outside this cancellation. Tilde/star-like clusters remain uncertain and no extra word is extracted from their rough traces."},
    {"span": r"\deleted{\unsure{d_r\geq\cdots\geq d_0}}",
     "finding": "A horizontal strike crosses only the short first condition immediately below the coproduct. The parenthesized tuple and final inequality line below it are live. All surviving struck characters, including the terminal d_0, remain represented and receive complete second-box coverage."},
]

recon_data = [
    ("manuscript page number", "64", "agrees", "editorial page note agrees"),
    ("opening main line", "les flèches verticales sont des morphismes", "agrees", "extra initial ill rejected"),
    ("opening second line", r"d'extensions par des noyaux qui sont des $\mathbb Z^{d_0}$", "double-stroked alphabet corrected", "agrees"),
    ("opening third line", "tordus -- en fait par les systèmes locaux", "agrees", "agrees"),
    ("opening fourth line", r"$T_{d_0}$, et son image inverse sur $D^*_{d_0,-,d_r}$ --", "index dash checked", "index dash checked"),
    ("opening fifth line", "on pose donc", "agrees", "posons rejected"),
    ("upper margin first line", "du moins si les", "agrees", "different words corrected"),
    ("upper margin formula line", r"$\unsure{\Pi_2|\pi_2}$ de $D_{d_0}^{\unsure{\circ|0}}$ et $D^*_{d_0,\unsure{-,|-}d_r}$", "case and local doubts recorded", "second base and high loop restored"),
    ("upper margin last line", "sont nuls...", "agrees", "plural phrase recovered"),
    ("raised annotation", annotation, "extra curl and blackboard Z recorded", "loc. retained and de rang rejected"),
    ("(210) first definition row", r"T_{d_0,-,d_r}=\text{image inverse de }T_{d_0}\text{ (sur }D_{d_0},", "single dash preserved", "comma retained"),
    ("(210) second row and label", r"\text{par }D_{d_0,-,d_r}" + connector + r"D_{d_0}\quad(\unsure{210})", "literal connector and local number doubt", "complete arrow not asserted"),
    ("(210) cancelled beginning and live local-system row", cancelled_t + r"\quad" + local_system, "strike boundary and Pi case checked", "editorial note accounts for strike; case checked"),
    ("(210) fibre baseline", fibre_line, "sur replaces slash", "relative base restored"),
    ("(210) restriction baseline", restriction, "literal D dash", "literal T and D indices"),
    ("extension upper baseline", r"de sorte que $\widetilde\Pi_{d_0,-,d_r}$ est une ext. de", "index checked", "words and index corrected"),
    ("extension lower baseline", r"$\Pi_{d_0,-,d_r}$ par $T^*_{d_0,-d_r}$.", "kernel comma restored", "literal indices retained"),
    ("second margin words", "du moins si", "agrees", "different words corrected"),
    ("second margin formula", r"$\unsure{\Pi_2|\pi_2}(D^*_{d_0,-d_r})=0\ldots$", "capital-leading local doubt", "index and literal dots preserved"),
    ("prose before cancelled coproduct", "On posera bien sûr", "agrees", "pourra rejected"),
    ("cancelled coproduct baseline", cancelled_coproduct, "nested doubt retained; index checked", "decorations remain uncertain; index corrected"),
    ("(211) first main row", r"\unsure{G_{\Delta_r}|B_{\Delta_r}}=\coprod\unsure{B_{d_0,-d_r}|G_{d_0,-d_r}}\quad\text{groupe sur }D_{\Delta_r}", "right primary becomes B", "right letter and index checked"),
    ("(211) cancelled condition", cancelled_condition, "doubt retained, central stroke literal", "editorial note acknowledges strike"),
    ("(211) live tuple condition", tuple_condition, "single dash and doubled N", "single dash retained"),
    ("(211) last condition", live_condition, "literal point plus dash", "no added inequality"),
    ("(211) P row and label", p_sum + r"\quad(211)", "second comma retained", "single dash retained"),
    ("(211) T row and first description baseline", t_sum + r"\quad\text{système local des}", "second comma retained", "single dash retained"),
    ("(211) homotopy/homology baseline", description_middle, "capital-leading and ou doubts", "commas retained"),
    ("(211) G/P description baseline", description_last, "paired marks drawn", "no choix letters"),
    ("(211) starred row and compressed word", final_group + r"\quad" + final_word, "primary dire counted", "inside brace; compressed word retained"),
    ("(211) last baseline", final_restrictions, "no added final point", "les and brace scope retained"),
    ("pencil archive number", "129", "agrees", "omission recorded"),
]
line_reconciliation = [
    {"line": f"L{i:02d}", "place": place, "reading": reading, "C_status": c, "H_status": h}
    for i, (place, reading, c, h) in enumerate(recon_data, 1)
]

report = {
    "scan": 130, "reader": "reader_a", "line_count": len(line_reconciliation),
    "rows": rows, "decisions": decisions, "nested_decisions": nested_decisions,
    "inventory": inventory, "doubts": doubts, "notes": notes,
    "check_events": check_events, "hand_log": hand_log, "notation": notation,
    "abbreviations": abbreviations, "second_boxes": second_boxes,
    "unresolved": [d["place"] + ": " + d["reading"] + " / " + d["alternatives"] for d in doubts],
    "deletion_insertion_checks": deletion_insertion_checks,
    "line_reconciliation": line_reconciliation,
    "viewing_record": {
        "whole_page": "Viewed once.",
        "native_top": "Viewed once.",
        "native_bottom": "Viewed once successfully; an earlier returned image was truncated before useful inspection.",
        "first_pass_crops": [x["crop"] for x in manifest],
        "crops_viewed_once": len(manifest),
        "root_review": "Root reported visual review of all 24 crops; adjudications incorporated.",
        "restrictions": "Only scan130 packet and generic rules/schema/helper were read. No OCR, outside research, compilation, other-page files, or other-reader results.",
    },
}

(OUT / "147_scan130_proposed.tex").write_text(tex)
(OUT / "147_scan130_report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({
    "scan": 130, "rows": len(rows), "against_C": sum(x["against_C"] for x in rows),
    "against_H": sum(x["against_H"] for x in rows), "decisions": len(decisions),
    "nested_decisions": len(nested_decisions), "crops": len(manifest),
    "inventory": len(inventory), "doubts": len(doubts),
    "second_boxes": len(second_boxes), "lines": len(line_reconciliation),
}, ensure_ascii=False))
