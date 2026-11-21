from pathlib import Path
from datetime import datetime, timezone
import json
import re

ROOT = Path("/workspace/scratch/ea90d891106a")
PACKET = ROOT / "runtime/packets/147_scan070"
WORK = ROOT / "SP78_C13_147_work"
OUT = WORK / "reader_returns/147_scan070"
OUT.mkdir(parents=True, exist_ok=True)
qopen = chr(96) * 2
qclose = "''"

loop = r"D_{\begin{tikzpicture}[x=1ex,y=1ex,baseline=-.2ex,line width=.3pt]\draw (0,0)..controls(-.35,.25)and(-.9,.3)..(-.95,0)..controls(-.9,-.3)and(-.35,-.25)..(0,0);\fill(0,0)circle(.6pt);\end{tikzpicture}}"
segment = r"D_{\bullet-\bullet}"

diagram = r"""\diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=18pt,row sep=28pt,
execute at end picture={
\draw ([xshift=9pt]scan070-codim-zero.east |- scan070-codim-zero.north) -- ([xshift=9pt,yshift=-10pt]scan070-codim-zero.east |- scan070-g-one.south);
\draw ([xshift=-9pt]scan070-p-one.west |- scan070-codim-zero.north) -- ([xshift=-9pt,yshift=-12pt]scan070-p-one.west |- scan070-p-one.south);
\path (scan070-g-zero.center) -- (scan070-g-one.center) coordinate[midway] (scan070-middle);
\node at (scan070-codim-zero.center |- scan070-middle) {\begin{tikzpicture}[baseline=-2pt]\fill(0,0)circle(1.5pt);\node[above]at(0,.15){$I(2)$};\node[below]at(0,-.08){$1$};\end{tikzpicture}};
\coordinate (scan070-brace-top) at ([xshift=-18pt,yshift=2pt]scan070-codim-zero.north west);
\coordinate (scan070-brace-bottom) at ([xshift=-18pt]scan070-codim-zero.west |- scan070-g-one.center);
\path (scan070-brace-top) -- (scan070-brace-bottom) coordinate[midway] (scan070-brace-middle);
\draw (scan070-brace-top) .. controls ([xshift=-5pt]scan070-brace-top) and ([xshift=-2pt,yshift=4pt]scan070-brace-middle) .. ([xshift=-9pt]scan070-brace-middle) .. controls ([xshift=-2pt,yshift=-4pt]scan070-brace-middle) and ([xshift=-5pt]scan070-brace-bottom) .. (scan070-brace-bottom);
\node[left=5pt]at([xshift=-9pt]scan070-brace-middle){$(83)$};
}]
|[alias=scan070-codim-zero]|\text{codim }0\&\text{codim }1\&\text{codim }2\\
\&|[alias=scan070-g-zero]|G_0=\text{\begin{tikzpicture}[baseline=-2pt]\draw(0,0)..controls(-.25,.55)and(-.9,.55)..(-1.15,.12)..controls(-1.45,-.4)and(-.3,-.42)..(0,0);\fill(0,0)circle(2pt);\node[above]at(.15,.12){$I(2)$};\end{tikzpicture}}\arrow[r,"2"]\arrow[dr,"1"']\&
\text{\begin{tikzpicture}[baseline=-2pt]\draw(0,0)..controls(.4,.38)and(1,.36)..(1.32,.06);\draw(0,0)..controls(.4,-.38)and(1,-.36)..(1.32,-.07);\fill(0,0)circle(1.5pt);\fill(1.4,0)circle(1.5pt);\node[above]at(0,.1){$\{a\}$};\node[above]at(1.4,.1){$\{b\}$};\end{tikzpicture}}=P_0\\
\&|[alias=scan070-g-one]|G_1=\text{\begin{tikzpicture}[baseline=-2pt]\draw(0,0)--(1.2,0);\fill(0,0)circle(1.5pt);\fill(1.2,0)circle(1.5pt);\node[below]at(0,0){$1$};\node[above]at(1.2,.1){$I(2)$};\end{tikzpicture}}\arrow[r,"1"]\&
|[alias=scan070-p-one]|\text{\begin{tikzpicture}[baseline=-2pt]\draw(0,0)..controls(-.2,.5)and(-.8,.25)..(-.7,-.1)..controls(-.55,-.65)and(.15,-.48)..(0,0);\draw(0,0)--(.9,0);\fill(0,0)circle(1.5pt);\fill(.9,0)circle(1.5pt);\node[above]at(.9,.1){$I(2)$};\end{tikzpicture}}=P_1
\end{tikzcd}}"""

C = (PACKET / "C.tex").read_text()
H = (PACKET / "H.tex").read_text()
proposed = re.sub(r"\\\[\s*\(83\).*?\\\]", lambda _: diagram, C, count=1, flags=re.S)
assert proposed != C
proposed = proposed.replace(r"D_\circ", loop)
proposed = proposed.replace(r"\mathbf Z", r"\mathbb Z").replace(r"\mathbf P", r"\mathbb P")
proposed = proposed.replace(r"\deleted{De façon plus intrinsèque,} (ceci correspond au choix",
                            r"\deleted{De \unsure{façon} plus \unsure{intrinsèque},} \inserted{(Ceci correspond au} choix")
proposed = proposed.replace(r"de $I$ comme $1$", r"de $I$ comme $\unsure{1|\underline 1}$")
proposed = proposed.replace("on trouve le " + qopen, "on trouve en " + qopen)
assert r"\inserted{(Ceci correspond au}" in proposed
assert "on trouve en " + qopen in proposed
assert proposed.count(loop) == 5
(OUT / "proposed.tex").write_text(proposed)

crop_boxes = {
    1: [348,26,1688,184], 2: [204,235,1597,625], 3: [22,603,391,891],
    4: [344,565,1680,839], 5: [339,823,1614,1053], 6: [331,1041,1665,1267],
    7: [322,1264,1688,1482], 8: [319,1465,1496,1595], 9: [324,1580,1618,1710],
    10: [319,1681,1687,1814], 11: [317,1795,1626,1916],
    12: [320,1872,1684,2112], 13: [321,2078,1663,2208],
    14: [318,2185,1677,2352], 15: [27,2283,88,2352],
}
changes = []
def change(place, c, h, final, evidence, crop, against_C=False, against_H=True,
           kind="misread word", err="words", confidence="high", marked=False, consequential=False):
    changes.append({
        "id": f"070-{len(changes)+1:02d}", "place": place, "C": c, "H": h, "final": final,
        "evidence": evidence, "crop": f"147_scan070_place{crop:02d}.png",
        "box": crop_boxes[crop], "confidence": confidence, "against_C": against_C,
        "against_H": against_H, "kind": kind, "marked_in_H": marked,
        "error_sheet_kind": err, "consequential": consequential,
    })

change("heading, exponent of the second M",
       r"\widehat M^{\deleted{\unsure{!}}}_{1,I}", r"\widehat M^\xi_{1,I}",
       r"\widehat M^{\deleted{\unsure{!}}}_{1,I}",
       "The raised group is crossed by oblique strokes. A short upright/dot-like remnant survives beneath them; it does not support a clean live xi. The underlying bang remains doubtful.",
       1, kind="deletion state", err="struck text", confidence="low", marked=True, consequential=True)
change("heading, after card I=2",
       r"2\deleted{\unsure{\}}},", "2, [the editorial note calls the rature a digit]",
       r"2\deleted{\unsure{\}}},",
       "Between 2 and the live comma there is crossed ink with an angular upper return and a lower outward arm, compatible with a closing brace. Its interior is too overworked to exclude a digit.",
       1, kind="omission", err="struck text", confidence="low", marked=False)
change("diagram (83), isolated codimension-zero object",
       "isolated point on the G_1 row", "single point in the first array cell",
       r"\path (scan070-g-zero.center) -- (scan070-g-one.center) coordinate[midway] (scan070-middle);",
       "The isolated point lies vertically between the G_0 and G_1 vertices, with I(2) above and 1 below. It is not horizontally aligned with the G_1 vertex as C's last-row placement makes it.",
       2, against_C=True, against_H=False, kind="drawing or diagram", err="drawings and diagrams")
change("diagram (83), both genus labels 1",
       r"\underline 1 in both positions", "1 in both positions", "1 in both positions",
       "Each 1 consists of the slanted head, upright and connected bottom foot. There is no independent lower stroke. The same ordinary feet occur on other 1s in the diagram.",
       2, against_C=True, against_H=False, kind="misread symbol or index", err="symbols and indices")
change("diagram (83), G_1 left-vertex weight",
       "1 below the left vertex", "1 above the left vertex", "1 below the left vertex",
       "The 1 is below the filled left endpoint of the horizontal G_1 segment; the segment and vertex are clearly above its head.",
       2, kind="drawing or diagram", err="drawings and diagrams")
change("diagram (83), arcs at P_0's right vertex",
       "both arcs joined to the right filled point", "two edges joining both points",
       r"\draw(0,0)..controls(.4,.38)and(1,.36)..(1.32,.06);\draw(0,0)..controls(.4,-.38)and(1,-.36)..(1.32,-.07);\fill(1.4,0)circle(1.5pt);",
       "Both arc ends stop short of the right black point, leaving a narrow white interval. The geometric gaps are preserved without imposing a different graph-theoretic interpretation.",
       2, against_C=True, kind="drawing or diagram", err="drawings and diagrams", consequential=True)
change("diagram (83), framing",
       "left brace and two column dividers", r"\begin{array}{c|c|c}...\hline...",
       "left brace, two vertical dividers, no horizontal header rule; three arrows cross the right divider",
       "The long strokes separating the columns are vertical. No horizontal line is drawn under the codimension headings. A tall left brace accompanies (83), ending near the lower vertex level.",
       2, kind="drawing or diagram", err="drawings and diagrams")
change("left-margin divisor names, graph subscripts",
       r"D_\circ,\ D_{\bullet-\bullet}", r"D_\circ,\ D_-",
       loop + r",\ " + segment,
       "The loop is an oval terminating in a rounded solid point at its right end. The segment has a black endpoint at each end. The loop point is larger than an ordinary closure thickening.",
       3, against_C=True, kind="misread symbol or index", err="symbols and indices", consequential=True)
change("left-margin divisor names, quoted wording",
       qopen+"D boucle"+qclose+"; "+qopen+"D segment"+qclose,
       r"\og D_\circ boucle\fg{}; \og D_- segment\fg{}",
       qopen+"D boucle"+qclose+"; "+qopen+"D segment"+qclose,
       "Each phrase starts with a separately written capital D after two quotation strokes. The graph-indexed D is outside the quoted name. The source uses paired quotation strokes, not guillemets.",
       3, kind="omission", err="omissions")
change("first prose sentence, inserted divisor names",
       r"\inserted{$D_\circ$ et $D_{\bullet-\bullet}$,}",
       r"$D_\circ$ et $D_-$,",
       r"\inserted{$"+loop+r"$ et $"+segment+r"$,}",
       "The raised pair has the same pointed loop and two-ended segment as the margin. Its curved connector joins the first prose line after l'infini and before et.",
       4, against_C=True, kind="misread symbol or index", err="symbols and indices", consequential=True)
change("first prose sentence, H's extra cf. P_0",
       "", r"\add{\uncertain{cf.} P_0}", "",
       "There is no cf. group between the divisor insertion and et deux points. The visible P_0 above l'un belongs later in the sentence and is separately accounted for there.",
       4, kind="text not on the page", err="text not on page", marked=True)
change("first prose sentence, canceled dont",
       r"\deleted{dont}", r"\struck{\ill{}}", r"\deleted{dont}",
       "Under the horizontal cancellation, the looped d, rounded o, low n and final tall t remain visible. The cancellation stops before the following live l'un.",
       4, kind=r"readable ink left as \ill{}", err="readable ink left as illegible", marked=True)
change("first prose sentence, added point names",
       r"\inserted{$P_0$ et $P_1$,}", r"$P_0$ et $P_1$,", r"\inserted{$P_0$ et $P_1$,}",
       "P_0 et P_1 is written above the canceled dont, with a connector into that gap. The raised placement is an actual addition, not continuation of the main baseline.",
       4, kind="insertion or placement", err="insertions put in wrong place", consequential=True)
change("first prose sentence, before l'un",
       r"l'un \inserted{$P_0$}", r"\add{\uncertain{dont} l'un P_0}",
       r"l'un \inserted{$P_0$}",
       "The only dont is the visibly canceled word to the left. The live baseline begins l'un, with the separate P_0 above it; there is no second live dont.",
       4, kind="text not on the page", err="text not on page", marked=True)
change("first prose sentence, verb after l'un P_0",
       "est contenu", "contenu", "est contenu",
       "After the P_0 insertion connector the main baseline has the small e, joined s and tall crossed t of est. The next line begins contenu.",
       4, kind="omission", err="omissions")
change("first prose sentence, two divisors containing the named point",
       r"D_\circ et D_{\bullet-\bullet}", r"D_\circ et D_-",
       loop + " et " + segment,
       "Here the loop is particularly thin and its right endpoint is distinctly filled. The following segment also has endpoint dots. These are repeated graph symbols, not plain circle/minus subscripts.",
       5, against_C=True, kind="misread symbol or index", err="symbols and indices", consequential=True)
change("first prose sentence, l'autre n'est",
       "l'autre n'est contenu", "l'autre contenu", "l'autre n'est contenu",
       "Between autre and contenu there is a low n, a detached apostrophe and the joined est group. This ink is live and on the main baseline.",
       5, kind="omission", err="omissions", consequential=True)
change("first prose sentence, H's bien",
       "contenu que", r"contenu \add{\uncertain{bien}} que", "contenu que",
       "The line proceeds directly from contenu to the descending q of que; no inserted bien is present above or within this interval.",
       5, kind="text not on the page", err="text not on page", marked=True)
change("first prose sentence, last segment divisor",
       segment, r"D_-", segment,
       "The last divisor subscript consists of a left dot, a short joining line and a thicker round right endpoint, followed by a period.",
       5, kind="misread symbol or index", err="symbols and indices")
change("Essayons sentence, verbal phrase",
       r"\inserted{bien} saisir", r"\uncertain{déterminer}", r"\inserted{bien} saisir",
       "The baseline word begins with the open joined s-a group, followed by i-s-i-r; there is no d ascender. Bien is above it, with a long curved connector after de.",
       6, marked=True)
change("Essayons sentence, adjective after multiplicité",
       "schématique", "", "schématique",
       "After multiplicité the long word has the initial sch group, accented e region, tall m/a/t strokes and the descending q of schématique before à l'infini.",
       6, kind="omission", err="omissions")
change("boundary formula, clause after the comma",
       "qui est la réunion amalgamée", r"\add{\uncertain{donc}} \uncertain{celle}",
       "qui est la réunion amalgamée",
       "The line has a descending q followed by ui, then the compact est and separate la. The next words show réunion and the tall l/g structure of amalgamée through the right edge.",
       7, marked=True, consequential=True)
change("next line, adjective after multiplicités",
       "lisses", r"\uncertain{\ill{}}", "lisses",
       "The live word begins with a tall looped l, followed by a dotted i and joined low s-s-e-s strokes. It ends before the separately crossed mathematical group.",
       7, kind=r"readable ink left as \ill{}", err="readable ink left as illegible", marked=True)
change("next line, canceled mathematical group",
       r"\deleted{\unsure{$\widehat M$}}", r"\struck{\ill{}}", r"\deleted{\unsure{$\widehat M$}}",
       "A wedge-like top and the remnants of a large M-shaped body can be followed through several crossing strokes. The body is not sufficiently exposed to remove the existing doubt.",
       7, kind=r"readable ink left as \ill{}", err="readable ink left as illegible", confidence="low", marked=True)
change("end of the multiplicités lisses line, divisor subscripts",
       r"D_\circ et D_{\bullet-\bullet}", r"D_\circ et D_-",
       loop + " et " + segment,
       "The loop ends in a solid right point; the neighboring segment has its two filled endpoints. The marks match the other local divisor subscripts.",
       7, against_C=True, kind="misread symbol or index", err="symbols and indices", consequential=True)
change("isomorphe sentence, initial divisor symbol",
       r"D_\circ", r"D_\circ", loop,
       "The thin oval under D ends in a visibly solid right point. Its prominence agrees with the margin and the earlier occurrences rather than an unpointed circle.",
       8, against_C=True, kind="misread symbol or index", err="symbols and indices", consequential=True)
change("isomorphe sentence, raised mark on the M in the pair",
       r"(\widehat M^{\unsure{!}}_{G_0},\Gamma^!_0)",
       r"(\widehat M_{G_0},\Gamma^!_0)",
       r"(\widehat M^{\unsure{!}}_{G_0},\Gamma^!_0)",
       "There is a heavy raised vertical black group on M, with a short lateral spur. It cannot be omitted, but no clean separate dot survives to identify a bang securely. The adjacent Gamma has a distinct upright and dot.",
       8, kind="omission", err="symbols and indices", confidence="low", consequential=True)
change("G_0 definition, attachment of MD-",
       r"le \inserted{MD-}graphe", r"est isomorphe \add{MD-} à", r"le \inserted{MD-}graphe",
       "The small capital M and D followed by a dash lie directly above graphe; their curved connector descends into the gap after le. They do not attach to isomorphe on the preceding line.",
       9, kind="insertion or placement", err="insertions put in wrong place", consequential=True)
change("after the small G_0 loop drawing",
       r"\Gamma_0 son groupe", r"\Gamma_0 \uncertain{le} groupe", r"\Gamma_0 son groupe",
       "The word has three low connected portions, beginning with the s-like hook and ending in n. There is no tall l loop as there is in le earlier on the same line.",
       9, marked=True)
change("kernel formula, target subscript",
       r"\mathfrak S_{I(G_0)}", r"\mathfrak S_{I(2)}", r"\mathfrak S_{I(G_0)}",
       "Inside the target's subscript parentheses there is a G-shaped body with a small lower zero. It occupies two levels and is not the single curved digit 2 written in the graph labels above.",
       10, kind="misread symbol or index", err="symbols and indices", consequential=True)
change("kernel formula, cyclic group",
       r"\mathbf Z/2", r"\mathbb Z/2", r"\mathbb Z/2",
       "The Z has a separate parallel diagonal/outline, visible between the upper and lower horizontal strokes. This is a double-struck form rather than an undifferentiated bold Z.",
       10, against_C=True, against_H=False, kind="misread symbol or index", err="symbols and indices")
change("D'ailleurs formula, projective space and base",
       r"\mathbf P^1_{\mathbf Z}", r"\mathbb P^1_{\mathbb Z}", r"\mathbb P^1_{\mathbb Z}",
       "P has two upright tracks; Z has two separated diagonal tracks. The superscript is the ordinary digit 1 and the Z lies as the base index under P.",
       11, against_C=True, against_H=False, kind="misread symbol or index", err="symbols and indices")
change("after sur lequel, H's dès lors",
       "", r"\uncertain{dès lors}", "",
       "The next main line starts directly with Gamma_0^! and its isomorphism. The small word to the right is the separate trois insertion over pts, not a phrase after sur lequel.",
       11, kind="text not on the page", err="text not on page", marked=True)
change("action formula, cyclic group",
       r"\mathbf Z/2", r"\mathbb Z/2", r"\mathbb Z/2",
       "The second Z repeats the doubled diagonal seen in the kernel formula. The slash and 2 are separate lower strokes and do not account for the internal doubling.",
       12, against_C=True, against_H=False, kind="misread symbol or index", err="symbols and indices")
change("action sentence, added count before pts",
       r"\inserted{trois}", "", r"\inserted{trois}",
       "Above pts is the small t-r-o-i-s group with a dotted i and final s; its descending connector lands between des and pts.",
       12, kind="omission", err="omissions", consequential=True)
change("action sentence, U subscript alphabet",
       r"U_{0,3\,\mathbf Z}", r"U_{0,3}\mathbb Z", r"U_{0,3\,\mathbb Z}",
       "The Z has doubled diagonal tracks. It is lowered beside 0,3: its lower edge aligns with or below the 3, while the following prose comma sits appreciably higher. No substitution of the written 3 is made.",
       12, against_C=True, kind="misread symbol or index", err="symbols and indices", confidence="medium", consequential=True)
change("action sentence, insertion soit 1",
       r"de $U_{0,3\,\mathbf Z}$, \inserted{soit $1$,} et",
       r"\add{soit $1$} de $U_{0,3}\mathbb Z$",
       r"de $U_{0,3\,\mathbb Z}$, \inserted{soit $1$,} et",
       "The curved insertion stroke ends after the U expression and its comma, just before et. The raised text is soit 1 followed by a separate comma.",
       12, kind="insertion or placement", err="insertions put in wrong place", consequential=True)
change("action sentence, transposition verb",
       "en transposant les", r"\uncertain{en} \uncertain{\ill{}} \uncertain{les}",
       "en transposant les",
       "After en, the tall crossed t, joined ran, descending p, round o and final sant are visible; the following les is separately spaced.",
       12, kind=r"readable ink left as \ill{}", err="readable ink left as illegible", marked=True)
change("action sentence, insertion soit {0,infinity}",
       r"deux autres, \inserted{soit $\{0,\infty\}$,}",
       r"$U_{0,3}\mathbb Z$ \add{\uncertain{soit} $\{0,\infty\}$}, et ... les deux autres",
       r"deux autres, \inserted{soit $\{0,\infty\}$,}",
       "The raised soit and braced pair sit above the gap following deux autres. Its sweeping connector returns to that comma, not to the U formula on the preceding line.",
       13, kind="insertion or placement", err="insertions put in wrong place", marked=True, consequential=True)
change("bottom, long canceled phrase",
       r"\deleted{De façon plus intrinsèque,}",
       r"\struck{(\uncertain{ceux correspondant} plus \ill{})}",
       r"\deleted{De \unsure{façon} plus \unsure{intrinsèque},}",
       "The beginning has the capital D and a small e; the next word has the long f, and plus retains its p descender and l ascender. The last word ends with a q descender and ue-like exit. The straight strike hides interior strokes, so façon and intrinsèque remain doubtful.",
       13, kind="misread word", err="struck text", confidence="medium", marked=True)
change("bottom, H's second canceled group",
       "", r"\struck{à D_-}", "",
       "The source has one continuous cancellation across De ... plus ... to the final comma. No separate à followed by a graph-indexed D occurs below or after it.",
       13, kind="text not on the page", err="text not on page")
change("bottom, opening of the live replacement",
       "(ceci correspond au", r"\ill{} \uncertain{sur} \ill{}",
       r"\inserted{(Ceci correspond au}",
       "Above the canceled phrase, the parenthesis is followed by a large capital C, then the smaller e-c-i. Correspond au is on that same upper run; the following choix continues on the next main baseline.",
       13, against_C=True, kind="insertion or placement", err="insertions put in wrong place", marked=True, consequential=True)
change("bottom, after the closing parenthesis",
       r"$\infty$) donc", r"$\infty$), donc", r"$\infty$) donc",
       "The closing parenthesis is followed directly by the initial stroke of donc. There is no detached comma between them.",
       14, kind="text not on the page", err="text not on page")
change("bottom, word before the quoted quotient",
       "on trouve le", r"on trouve en", "on trouve en",
       "The short word has a low e loop followed by a low n/exit stroke. It lacks the tall l ascender seen in le elsewhere on the sheet.",
       14, against_C=True, against_H=False, kind="misread word", err="words")
change("bottom, quotation marks",
       qopen+"quotient"+qclose, r"\og quotient\fg{}", qopen+"quotient"+qclose,
       "There are paired short quotation strokes above the word on each side, not inward-facing angle marks.",
       14, kind="other", err="other")
change("last words at foot",
       "De façon", r"\uncertain{Désignons}", "De façon",
       "The capital D is followed by a small separate e. A space precedes the tall crossed f and the remaining façon strokes; the source begins a new phrase that continues beyond this page.",
       14, marked=True)
change("lower-left pencil foliation",
       r"\margin{69}", "", r"\margin{69}",
       "The light pencil digits are a lower-loop 6 and an upper-loop 9 with descending tail. They are separate from the ink author number 34 at the head.",
       15, kind="omission", err="omissions")

notes = [
    "The manuscript treats the fourth case, written as hat M^!_{1,2} isomorphic to hat M_{1,I}, with a crossed doubtful exponent on the latter and card I=2, I={a,b}. Diagram (83) presents one codimension-zero object, two codimension-one graphs G_0/G_1, and two codimension-two points P_0/P_1. This is a manuscript classification claim; no construction or classification of the moduli object was proved here.",
    "The literal diagram and prose disagree on the common point. The diagram has G_0 -> P_0 of weight 2, G_0 -> P_1 of weight 1, and G_1 -> P_1 of weight 1. The prose inserts P_0 as the point contained in both divisors, and says the other lies only in the segment divisor. Both sets of labels are retained; the diagram's implications were compared with the prose without correcting either.",
    "The manuscript asks to grasp the schematic multiplicity at infinity, written hat M^infinity_{1,I} isomorphic to hat M^{!,infinity}_{1,2}, and calls it the amalgamated union of the two smooth multiplicities denoted by the pointed-loop and pointed-segment divisors. This geometric assertion was carried as background without proof.",
    "The manuscript identifies the loop divisor with the pair (hat M^{doubtful !}_{G_0}, Gamma_0^!), defines Gamma_0^! as the kernel of the action on I(G_0), asserts it is Z/2, and writes hat M_{G_0} isomorphic to hat M^!_{0,4} isomorphic to P^1_Z. These are recorded claims, not results proved in this reading. The heavy raised mark on the M remains M1058, undecided.",
    "The manuscript says the involution fixes the chosen infinity point 1 and exchanges the other two, {0,infinity}, then describes the quoted quotient by z -> 1/z. A direct integer-matrix computation in this run verified that the homogeneous-coordinate swap matrix [[0,1],[1,0]] squares to the identity, maps [0:1] to [1:0] and back, and fixes [1:1]. This verifies that displayed action on these three projective points only; it does not prove the moduli identifications, a quotient theorem, or uniqueness of the fixed point. The source's lowered U index is retained as 0,3 Z without repairing 3.",
    "Ink limitations: the heading's canceled exponent and canceled brace-like mark, the canceled hat-M group, M1058, parts of the long bottom cancellation, and the overworked choice numeral 1 remain doubtful. The main choice numeral is recorded as 1 with underline 1 as an alternative; the two diagram genus labels have only connected feet. Capital Ceci begins an interlinear replacement. The page ends with the incomplete continuation De façon.",
    "Reading count: 34 physical reading bands: 18 main prose baselines, 7 distinct interlinear-addition bands (some contain multiple additions), 2 margin-note baselines, 4 diagram bands (heading, G_0/P_0, the isolated object, G_1/P_1), the main heading, the ink page number and the pencil foliation. The complete scan and both native halves were read once before the crops. Fifteen unique crop places were saved and viewed; crop03 was rotated by -30 degrees. This was visual reading, without OCR, internet research or TeX compilation. Two tiny isolated diagram-area spots were not promoted to additional vertices or punctuation.",
    "The two small graph subscripts are reproduced as pointed loop and two-ended segment, including the right point of the loop in all five occurrences. The repeated double diagonal/outline of Z and doubled upright of P are rendered in blackboard-bold alphabet. The pencil foliation 69 remains margin text and is not attributed confidently to the author; the ink author number is 34.",
]

events = [
    (1, "carried as background without fault found", "Read the case heading and full diagram (83), including arrows, weights and small gaps. Did not prove the asserted classification of boundary strata."),
    (2, "used and rechecked in this run", "Compared the three drawn arrow endpoints with the inserted prose P_0. Confirmed the literal incidence-label mismatch; no geometric choice of the correct labeling was made."),
    (3, "carried as background without fault found", "Read the full infinity formula and amalgamated-union assertion. Did not establish smoothness, scheme structure or the claimed gluing."),
    (4, "carried as background without fault found", "Read the full doubtful quotient pair, kernel formula, target I(G_0), Z/2 and projective-space chain. Did not prove the moduli identifications or compute the automorphism kernel."),
    (5, "computation or formal certificate", "Executed exact integer arithmetic on M=((0,1),(1,0)): M^2=((1,0),(0,1)); M(0,1)=(1,0), M(1,0)=(0,1), M(1,1)=(1,1). This checks the involution and the stated three-point permutation only. No quotient construction, global fixed-locus claim or geometric identification was checked."),
]
date = datetime.now(timezone.utc).isoformat()
check_events = [{"statement_id":f"147-070-N{n}", "date":date,
                 "who":"reader_c, GPT-6 Astra Pro (effort setting not exposed)",
                 "type":typ, "outcome":outcome} for n,typ,outcome in events]

inventory = []
def inv(kind, position, first, hand="his hand"):
    inventory.append({"scan":70,"sheet_kind":"text","hand":hand,
                      "element":f"{len(inventory)+1:02d}","kind":kind,"position":position,
                      "first_words_or_objects":first,"transcribed":"yes"})
inv("text","top centre","34")
inv("text","heading","4°) Cas de; full two-M formula and cardinality")
inv("deletion","heading, second M exponent","crossed doubtful !")
inv("deletion","heading, after card I=2","crossed doubtful closing brace")
inv("diagram","upper quarter","(83), codim 0/1/2, all five objects and three arrows")
inv("margin note","left slanting margin","pointed-loop D: D boucle; segment D: D segment")
inv("text","four main baselines below diagram","Il y a deux diviseurs ... autre n'est contenu que ...")
inv("insertion","above first prose line","two divisor symbols")
inv("insertion","above deux points","critiques")
inv("deletion","after à l'infini in second main line","dont")
inv("insertion","above canceled dont","P_0 et P_1,")
inv("insertion","above l'un","P_0")
inv("text","next paragraph, two baselines","Essayons de ... la multiplicité schématique à l'infini")
inv("insertion","above saisir","bien")
inv("text","next two baselines","infinity formula, qui est la réunion amalgamée ...")
inv("deletion","after lisses","doubtful hat M")
inv("text","isomorphe line","pointed-loop divisor and full doubtful pair")
inv("text","next line","G_0 est le ... Gamma_0 son groupe d'")
inv("insertion","above graphe","MD-")
inv("drawing","in G_0 definition line","teardrop loop with filled right vertex and I(2)")
inv("text","automorphismes line","kernel formula with target I(G_0) and Z/2")
inv("text","D'ailleurs line","hat-M identifications and P^1_Z")
inv("text","remaining action/quotient paragraph","Gamma_0^! ... U_{0,3 Z} ... z maps to z^-1. De façon")
inv("insertion","above pts","trois")
inv("insertion","above et after U formula","soit 1,")
inv("insertion","above gap after deux autres","soit {0,infinity},")
inv("deletion","after deux autres","De doubtful façon plus doubtful intrinsèque,")
inv("insertion","above bottom cancellation","(Ceci correspond au")
inv("margin note","lower left","69","unattributed pencil hand")

doubts = [
    {"place":"heading, second M exponent","reading":r"\deleted{\unsure{!}}","alternatives":"crossed xi-like shape or an unidentifiable original raised mark","confidence":"low","reason":"Multiple crossing strokes partly expose an upright/dot-like remnant but do not identify the original exponent securely."},
    {"place":"heading, after card I=2","reading":r"\deleted{\unsure{\}}}","alternatives":"a canceled digit or another right-facing sign","confidence":"low","reason":"The brace-like upper/lower returns survive, but the interior is crossed and H's digit hypothesis cannot be excluded by stroke exposure alone."},
    {"place":"after multiplicités lisses","reading":r"\deleted{\unsure{$\widehat M$}}","alternatives":"another crossed mathematical group","confidence":"low","reason":"The top wedge and M-like body are plausible, but several independent strokes cross the whole group."},
    {"place":"M1058, first component of the quotient pair","reading":r"\widehat M^{\unsure{!}}_{G_0}","alternatives":"a cross-like raised mark; joined or overworked bang","confidence":"low","reason":"The raised ink is a solid vertical group with a lateral spur and lacks the distinct detached dot seen on Gamma's bang. It is not omitted or resolved through mathematical expectation."},
    {"place":"U formula, lowered Z attachment","reading":r"U_{0,3\,\mathbb Z}","alternatives":r"U_{0,3}\mathbb Z","confidence":"medium","reason":"The Z is larger than 0,3 but lowered beside them; the following comma sits higher. C's attachment is preferred from the relative baselines, without repairing the unusual written index."},
    {"place":"long bottom cancellation","reading":r"\deleted{De \unsure{façon} plus \unsure{intrinsèque},}","alternatives":"unrecoverable interior letters of the two doubtful words","confidence":"medium","reason":"De and plus are exposed; long f and q structures favor façon/intrinsèque, but the horizontal strike masks interior letters and the cedilla/medial accent region."},
    {"place":"choice numeral in comme 1","reading":r"\unsure{1|\underline 1}","alternatives":r"\underline 1","confidence":"medium","reason":"The upright is looped/overworked and its base is long and heavy. An underline could have merged with the ordinary foot; the surviving ink does not separate the two securely."},
]

head = proposed.split(diagram)[0].replace(r"\scanpage{70}"+"\n","").strip()
body_after_diagram = proposed.split(diagram,1)[1].strip()
margin_and_first = body_after_diagram.split("\n\nEssayons",1)[0]
essayons = "Essayons" + body_after_diagram.split("\n\nEssayons",1)[1]
essayons_open, rest = essayons.split(r"$\widehat M^\infty",1)
boundary, rest2 = (r"$\widehat M^\infty"+rest).split("\n"+r"$"+loop+r"$ est isomorphe",1)
isomorphe_and_after = r"$"+loop+r"$ est isomorphe"+rest2
pair_part, small_graph_after = isomorphe_and_after.split(r"$G_0$ est le",1)
small_graph_and_after = r"$G_0$ est le"+small_graph_after
graph_part, kernel_after = small_graph_and_after.split(r"$\Gamma_0$ son groupe d'automorphismes",1)
kernel_and_after = r"$\Gamma_0$ son groupe d'automorphismes"+kernel_after
kernel_part, lower_after = kernel_and_after.split("\nD'ailleurs",1)
graph_part += r"$\Gamma_0$ son groupe d'"
kernel_part = kernel_part.removeprefix(r"$\Gamma_0$ son groupe d'")
lower_part = "D'ailleurs"+lower_after
lower_part = lower_part.replace("\n"+r"\margin{69}","").strip()
second_boxes = []
def sb(kind, box, reading):
    second_boxes.append({"box":f"B{len(second_boxes)+1:02d}","kind":kind,
                         "x0":box[0],"y0":box[1],"x1":box[2],"y1":box[3],
                         "reading":reading.strip()})
sb("struck passage",[348,26,1688,184],head)
sb("handwritten number",[204,235,1597,625],diagram)
sb("margin note",[22,565,1688,1053],margin_and_first)
sb("word disagreement",[331,1025,1665,1267],essayons_open)
sb("struck passage",[322,1264,1688,1482],boundary)
sb("doubtful formula",[319,1465,1496,1595],pair_part)
sb("insertion",[324,1580,1618,1710],graph_part)
sb("handwritten number",[319,1681,1687,1814],kernel_part)
sb("word disagreement",[317,1778,1688,2352],lower_part)
sb("handwritten number",[27,2283,88,2352],r"\margin{69}")

report = {
    "scan":70, "reader":"reader_c", "physical_lines_read":34, "changes":changes,
    "decisions":[{
        "id":"M1058","cote":147,"scan":70,"decision":"undecided",
        "reading":r"\widehat M^{\unsure{!}}_{G_0}",
        "ink":"The complete pair was inspected: hat and G_0 are distinct; the M exponent is a heavily filled upright with a short lateral spur and no securely separate dot. The neighboring Gamma has a clear bang, which is not used to decide M's mark.",
        "crop":"147_scan070_place08.png (319,1465,1496,1595)","confidence":"low",
    }],
    "inventory":inventory, "doubts":doubts, "notes":notes, "check_events":check_events,
    "notation":[
        {"sign":"oval loop ending in a filled right point under D","reading":loop,"evidence":"The right end is rounded and filled in all five occurrences; crop05 exposes a thin oval and a distinct thick endpoint.","scope":"147 scan070, margin and four body occurrences"},
        {"sign":"line with a filled endpoint at each end under D","reading":segment,"evidence":"Two endpoint dots occur in the margin and body, sometimes with a small pen lift between the left dot and the segment.","scope":"147 scan070, all segment-divisor labels"},
        {"sign":"double diagonal Z and double upright P","reading":r"\mathbb Z,\mathbb P","evidence":"Separated tracks are visible in the kernel/action Z/2 groups and P^1_Z; the lowered Z after U has the same double outline.","scope":"147 scan070, four Z occurrences and one P"},
        {"sign":"large looped S in the kernel target","reading":r"\mathfrak S_{I(G_0)}","evidence":"The established looped symmetric-group form is followed by a subscript containing G with lower zero, distinct from the simple 2 in I(2) labels.","scope":"147 scan070, kernel formula"},
        {"sign":"short barred map arrow","reading":r"\longmapsto","evidence":"The map's initial end has a distinct upright bar and the right end a pointed arrowhead.","scope":"147 scan070, last line"},
    ],
    "hand_log":[
        {"habit":"A pointed-loop graph subscript can look like an ordinary circle when reduced.","pages":[70],"all_occurrences":"Confirmed locally at all five D-loop labels; the point is especially distinct in crops03,05,07,08.","witness_misreadings":"Both C and H reduce the loop to circ; H additionally reduces the segment to a minus."},
        {"habit":"The numeral 1 has a connected horizontal foot which is not automatically an underline.","pages":[70],"all_occurrences":"Both diagram genus labels have one connected foot; the prose choice 1 is overworked and remains a separate occurrence-specific underline/plain doubt.","witness_misreadings":"C underlines both diagram genus labels; neither witness marks the prose 1 as uncertain."},
        {"habit":"Reduced à can resemble two separate vertical dots.","pages":[70],"all_occurrences":"Repeated in à l'infini and est isomorphe à; lexical surroundings and each local stroke were compared, not a blanket colon substitution.","witness_misreadings":"H leaves the isomorphe à uncertain; no source colon was replaced solely by grammatical expectation."},
        {"habit":"Low e-n can be distinguished from le by the absence of the tall l loop.","pages":[70],"all_occurrences":"The last-line en is low; le before graphe has the tall loop for comparison.","witness_misreadings":"C gives le before the quoted quotient, while H's en fits the ink."},
    ],
    "abbreviations":[{"written":"card","expansion":"cardinal"},{"written":"codim","expansion":"codimension"},{"written":"pts","expansion":"points"}],
    "second_boxes":second_boxes,
    "unresolved":[
        "M1058 remains undecided; the M exponent must not be inferred from the clear bang on Gamma.",
        "The heading's canceled exponent and brace-like mark, canceled hat-M group, and two words of the long bottom strike remain doubtful.",
        "The choice numeral 1 may have an underline merged with its heavy foot; both readings are retained.",
        "The diagram's common point P_1 and the prose's common point P_0 remain inconsistent as written.",
        "The lowered Z attachment in U_{0,3 Z} is preferred at medium confidence; the visible 3 remains unchanged.",
    ],
    "witness_comparison":"C is much closer to the continuous prose, insertion contents and lower cancellation, and correctly preserves the diagram's arrow endpoints and source P_0 prose. H better preserves the double-struck alphabets and reads en before quotient. C adds underlines to two ordinary genus-1 feet, suppresses the pointed-loop dot, aligns the isolated diagram point with the wrong row and closes the visible P_0 arc gaps; H adds a header rule, moves a genus label above its vertex, loses graph endpoint dots, misattaches several additions and leaves readable prose as doubtful/illegible. Neither witness captures the capital inserted Ceci or the full local uncertainty of the heavy choice numeral."
}

assert [x["id"] for x in report["decisions"]] == ["M1058"]
assert len(report["changes"]) == len({x["id"] for x in report["changes"]})
for row in report["changes"]:
    assert row["against_C"] or row["against_H"]
    assert (WORK/"crops"/row["crop"]).is_file(), row
for event in report["check_events"]:
    n = int(event["statement_id"].split("-N")[-1])
    assert 1 <= n <= len(report["notes"])
for box in report["second_boxes"]:
    assert box["reading"] in proposed, box["box"]
assert all((WORK/"crops"/f"147_scan070_place{i:02d}.png").is_file() for i in range(1,16))
(OUT / "report.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
print(json.dumps({"scan":70,"physical_bands":34,"crops":15,"changes":len(changes),
                  "decisions":len(report["decisions"]),"inventory":len(inventory),
                  "doubts":len(doubts),"second_boxes":len(second_boxes),
                  "check_events":len(check_events),"out":str(OUT)},ensure_ascii=False))
