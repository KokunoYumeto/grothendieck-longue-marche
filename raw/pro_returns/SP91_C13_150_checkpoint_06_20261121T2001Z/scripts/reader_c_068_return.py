"""First-pass scan068 assembly. Outputs are replaced atomically."""
from pathlib import Path
import collections
import csv
import json
import os

EDITION = Path(__file__).resolve().parents[1]
ROOT = EDITION.parent
C = (ROOT / "input/SP91_C13_150_texts/pages/150_scan068.tex").read_text()
H = (ROOT / "input/SP91_C13_150_texts/hua/hua_150_scan068.tex").read_text()
CROPS = json.loads((EDITION / "scripts/reader_c_068_crop_manifest.json").read_text())
CP = {i+1: c for i,c in enumerate(CROPS)}

def atomic_text(path, value):
    temporary = path.with_name(path.name + ".tmp")
    with temporary.open("w", encoding="utf-8", newline="\n") as f:
        f.write(value)
        f.flush()
        os.fsync(f.fileno())
    os.replace(temporary, path)

DIAGRAM = r"""\diagram{\begin{tikzpicture}[x=1cm,y=1cm,line cap=round,line join=round]
\node at (0,1.35) {$X$};
\node at (2,1.35) {$X'$};
\node at (0,0) {$Y$};
\node at (2,0) {$Y'$};
\draw[<-] (0.30,1.35)--(1.69,1.35);
\node[above] at (0.98,1.38) {$f'$};
\draw[<-] (0.30,0)--(1.69,0);
\node[below] at (0.99,-0.02) {$g$};
\draw (0,1.03)--(0.01,0.47);
\fill (0.01,0.45) circle (0.052);
\node[left] at (-0.10,0.69) {$f$};
\draw (2,1.03)--(2.01,0.50);
\fill (1.965,0.53)--(2.055,0.48)--(2.015,0.405)--(1.975,0.445)--cycle;
\node[right] at (2.11,0.73) {$g'$};
\end{tikzpicture}}"""

I_READING = r"\unsure{$I$\inserted{$=\pi_0(\Sigma_0)$},|$I_0$\inserted{$=\pi_0(\Sigma_0)$}}"
REVISED_IMAGE = r"""\inserted{$=\text{image de }\pi_0(\Sigma_1)$
\deleted{dans $\unsure{\pi_0(\Sigma_1)\times I|\pi_0(\Sigma_0)\times\Sigma_1}$}
dans $\pi_0(\Sigma_0)\times\pi_0(\Sigma_0)=I$}"""
TEX = r"""\scanpage{68}
\deleted{\unsure{Cela posé}} Cette relation est évidemment \deleted{\unsure{symétrique}}\inserted{réflexive}, et
elle est transitive grâce au fait que
\[
\pi_0(\Sigma_{(2)})\longrightarrow
(\pi_0(\Sigma_{(1)}),\pi_0(\uline{b}))\times_{\pi_0(\Sigma_{(0)})}
(\pi_0(\Sigma_{(1)}),\pi_0(\uline{s}))
\]
est surjective, ce qui est facile à prouver,
grâce à l'hypothèse que $\uline{b}$ est fibrant, par le
\uline{Lemme} : Soit
""" + DIAGRAM + r"""
un carré
cartésien d'espaces top, avec $f$ fibrant,
alors $\pi_0(X')\longrightarrow\pi_0(X)\times_{\pi_0(Y)}\pi_0(Y')$ est surjectif
Ceci posé, considérons la catégorie top. discrète \unsure{associé|associée}
à l'ens \inserted{pré}ordonné """ + I_READING + r""" que par abus de langage
\inserted{[\unsure{anglicisme}\unsure{)|]}}
on \unsure{désignera|désigne} par $I$. On a alors un foncteur
\inserted{canonique} de catégories topologiques \deleted{\unsure{canoniques|canonique}}
\[
\uline{\Sigma}\xrightarrow{\uline{\varphi}}I
\]
qui est donc donné par des applications continues
\[
\left\{\begin{aligned}
\Sigma_{(0)}&\xrightarrow{\varphi_0}I_0=I\\
\Sigma_{(1)}&\xrightarrow{\varphi_1}I_1=\text{graphe de la relation d'ordre}
\end{aligned}\right.
\]
""" + REVISED_IMAGE + r"""
i.e. des décompositions en sommes directes
\[
\Sigma_{(0)}=\coprod_{i\in I}\Sigma_i
\]
\[
\Sigma_{(1)}=\deleted{\unsure{\Sigma}}\coprod_{\substack{i,\unsure{j|g}\in I\\i\leq j}}\Sigma_{ij}
\]
\margin{\uline{NB} on suppose \uline{les} comp. connexes des $\Sigma_0$ et $\Sigma_1$ ouvertes}
compatibles avec $\uline{s}\ \uline{b}$
i.e $\uline{s}:\Sigma_{ij}\mathrel{-}\Sigma_i$
$\uline{b}:\Sigma_{ij}\mathrel{-}\Sigma_j$
avec $\Sigma_{(0)}\xrightarrow{\delta}\Sigma_{(1)}$ ($\delta(x)=\deleted{\unsure{\operatorname{id}^{\uline{\Sigma}}_x}}\operatorname{id}^{\uline{\Sigma}}_x$)
appliquant $\Sigma_i$ dans $\Sigma_{ii}$, \deleted{\unsure{et ainsi}} (ce qui
implique déjà la compatibilité de $\uline{\varphi}=(\varphi_0,\varphi_1)$ avec
la composition). De plus, $\uline{\varphi}$ est un
\margin{67}
"""
atomic_text(EDITION / "reader_returns/150_scan068.tex", TEX)
OUT = {
    "scan": "068", "reader": "reader_c", "line_count": 26,
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
        "id": f"068-{len(OUT['changes'])+1:02d}",
        "place": place, "C": c, "H": h, "final": final,
        "against_C": ac, "against_H": ah, "kind": kind,
        "error_category": category, "marked_in_H": marked,
        "confidence": confidence, "evidence": evidence,
        "crop": CP[p]["file"], "box": CP[p]["box"],
        "mathematical_consequence": consequence,
    })

change("top cancellation, first phrase",
       r"\deleted{Ceci posé}", r"\struck{Cela posé}", r"\deleted{\unsure{Cela posé}}",
       True, False, "misread word", "Words", 1, "medium",
       "A tall closed l loop survives between the initial Ce run and a low a-shaped ending. Posé retains its p descent, low o/s/e contours and detached accent. The crossing masks portions of the low letters, so the whole cancelled phrase stays marked.")
change("opening display, source argument",
       r"\pi_0(\Sigma_{(2)})", r"\pi_0(\Sigma(2))", r"\pi_0(\Sigma_{(2)})",
       False, True, "misread symbol or index", "Symbols and indices", 3, "high",
       "The small parenthesized 2 begins below the top of the Sigma and extends below its baseline; its lower-right position is retained.",
       "The written parenthesized argument is kept in its lowered position.")
change("opening display, first target factor's Sigma argument",
       r"(\pi_0(\Sigma_{(1)}),\pi_0(\uline{b}))",
       r"\bigl(\pi_0(\Sigma(1)),\pi_0(\underline b)\bigr)",
       r"(\pi_0(\Sigma_{(1)}),\pi_0(\uline{b}))",
       False, True, "misread symbol or index", "Symbols and indices", 3, "high",
       "The first target's parenthesized 1 is smaller and shifted down/right of its Sigma. A separate short bar underlines b inside the second component.",
       "This Sigma retains its locally lowered parenthesized 1.")
change("opening display, fibre-product base's Sigma argument",
       r"\times_{\pi_0(\Sigma_{(0)})}", r"\times_{\pi_0(\Sigma(0))}",
       r"\times_{\pi_0(\Sigma_{(0)})}",
       False, True, "misread symbol or index", "Symbols and indices", 3, "high",
       "In the lowered base expression, the parenthesized 0 sits down/right of its Sigma. The pi subscript 0 and both enclosing parentheses remain visible.",
       "The lowered argument position is retained inside the written product subscript.")
change("opening display, second target factor's Sigma argument",
       r"(\pi_0(\Sigma_{(1)}),\pi_0(\uline{s}))",
       r"\bigl(\pi_0(\Sigma(1)),\pi_0(\underline s)\bigr)",
       r"(\pi_0(\Sigma_{(1)}),\pi_0(\uline{s}))",
       False, True, "misread symbol or index", "Symbols and indices", 3, "high",
       "The right factor again has a lowered parenthesized 1. A short independent underline is visible beneath s, and the final outer closing curve is present.",
       "This local occurrence retains its lowered parenthesized 1.")
change("lemma square, vertical terminal ink",
       C[C.index(r"\diagram{"):C.index("\nun carré")],
       H[H.index(r"\begin{tikzcd}"):H.index(r"\end{tikzcd}")+len(r"\end{tikzcd}")],
       DIAGRAM,
       True, True, "drawing or diagram", "Drawings and diagrams", 5, "high",
       "The horizontal connectors have exposed left-pointing heads. Each downward shaft ends in dense filled ink: the left endpoint is rounded and the right is more pointed. These terminal shapes are reproduced directly. X, X-prime, Y, Y-prime and labels f, f-prime, g, g-prime are all visible in their respective positions.")
change("lemma prose, top followed by comma",
       "top., avec", "top., avec", "top, avec",
       True, True, "text not on the page", "Text that is not on the page", 6, "high",
       "After the abbreviated top there is a single comma-shaped descending mark. A separate abbreviation point is not visible before it.")
change("lemma conclusion, end of surjectif",
       "est surjectif.", "est surjectif.", "est surjectif",
       True, True, "text not on the page", "Text that is not on the page", 7, "high",
       "The final f extends down close to the paper edge. No point follows it in the remaining visible strip.")
change("category paragraph, word at the right paper edge",
       "associée", "associée", r"\unsure{associé|associée}",
       True, True, "misread word", "Words", 8, "low",
       "The associ run and a detached accent over the ending are visible, but the final low stroke meets the cut right edge. A second separate e cannot be isolated. The shorter visible reading leads, while the two-e ending remains an explicit alternative.")
change("category paragraph, abbreviation ens",
       "l'ens", r"l'ens.\ ", "l'ens",
       False, True, "abbreviation expanded or spelling modernised",
       "Abbreviations expanded, spelling modernised", 9, "high",
       "The low joined ens run ends before the interlinear prefix. The space after it has no separate point.")
change("category paragraph, written prefix pré",
       r"\inserted{pré}ordonné", r"\supplied{pré}ordonné", r"\inserted{pré}ordonné",
       False, True, "insertion or placement", "Insertions put in the wrong place", 9, "high",
       "Pré is visibly written above ordonné, with p/r forms, a detached accent and a curved insertion leader. It is represented as manuscript ink rather than only an editorial supply.")
change("category paragraph, I and the small following mark",
       r"$I_0$\inserted{$=\pi_0(\Sigma_0)$}",
       r"$I$ \add{$=\pi_0(\Sigma_0)$},",
       I_READING,
       True, False, "misread symbol or index", "Symbols and indices", 10, "medium",
       "The small mark to the lower right of I has a dark head and a curved downward tail, without a securely open zero counter. The leading reading treats it as a comma surviving after the inserted equality. The I-zero reading is retained as a local shape alternative. The curved leader attaches the clear =pi_0(Sigma_0) insertion after I.",
       "The I versus I-zero reading remains explicit; no index is silently supplied.")
change("category paragraph, bracketed insertion M0615",
       r"\inserted{[\unsure{morphisme|anglicisme})}", r"\add{\ill{}}",
       r"\inserted{[\unsure{anglicisme}\unsure{)|]}}",
       True, True, r"readable ink left as \ill{}", "Readable ink left as illegible", 11, "medium",
       "The low initial an run is followed by a descending g and a tall l, strongly supporting anglicisme. Its compressed ending remains uncertain. The left delimiter has a vertical stem and two short horizontal arms; the right is curved with a short lower-left foot, retaining a parenthesis/bracket shape doubt.",
       marked=True)
change("category paragraph, désignera/désigne",
       "désignera", "désigne", r"\unsure{désignera|désigne}",
       False, True, "misread word", "Words", 12, "medium",
       "The accented dé, s, dotted i and large g descent are visible. The following low run has several small rises and a long terminal return; it supports désignera but does not separate the final ra securely enough to exclude désigne.")
change("category paragraph, cancelled final adjective",
       r"\deleted{canonique}", r"\struck{canoniques}",
       r"\deleted{\unsure{canoniques|canonique}}",
       True, False, "misread word", "Words", 14, "medium",
       "The crossed word has a dotted i and long q descent. After the ue-shaped ending is an additional short rightward/downturned run, favouring final s. The crossing and terminal join leave the singular form open.")
change("functor display, arrow label",
       r"\xrightarrow{\uline{\varphi}}", r"\xrightarrow{\ f\ }",
       r"\xrightarrow{\uline{\varphi}}",
       False, True, "misread symbol or index", "Symbols and indices", 15, "high",
       "The label has the open left bowl and closed right loop of the page's varphi, on a descending stem. A separate short horizontal underline crosses that descent below the bowl.",
       "The manuscript's underlined varphi label is retained.")
change("functor display, target underline",
       r"\xrightarrow{\uline{\varphi}}I",
       r"\xrightarrow{\ f\ }\underline I",
       r"\xrightarrow{\uline{\varphi}}I",
       False, True, "text not on the page", "Symbols and indices", 15, "high",
       "The target I has one top bar and one normal bottom foot. No second independent lower stroke underlines it. In the same crop, Sigma has a plainly separate underline.")
change("first application row, parenthesized source argument",
       r"\Sigma_{(0)}&\xrightarrow{\varphi_0}I_0=I",
       r"\Sigma(0)\xrightarrow{\ \varphi_0\ }I_0=I",
       r"\Sigma_{(0)}\xrightarrow{\varphi_0}I_0=I",
       False, True, "misread symbol or index", "Symbols and indices", 16, "high",
       "The small parenthesized 0 is shifted below/right of the Sigma body. The arrow's phi-zero label and the target I-zero=I are separately legible.",
       "The written source argument keeps its lowered placement.")
change("second application row, parenthesized source argument",
       r"\Sigma_{(1)}&\xrightarrow{\varphi_1}I_1=",
       r"\Sigma(1)\xrightarrow{\ \varphi_1\ }I_1=",
       r"\Sigma_{(1)}\xrightarrow{\varphi_1}I_1=",
       False, True, "misread symbol or index", "Symbols and indices", 17, "high",
       "The small parenthesized 1 descends below the Sigma baseline. The phi-one arrow label and I-one target are visible in the same row.",
       "The local lowered parenthesized 1 is retained.")
change("second application row, appended image explanation",
       r"\inserted{$=\text{image de }\pi_0(\Sigma_1)$",
       r"\qquad=\text{image de }\pi_0(\Sigma_1)\text{ dans }",
       r"\inserted{$=\text{image de }\pi_0(\Sigma_1)$",
       False, True, "insertion or placement", "Insertions put in the wrong place", 17, "medium",
       "The explanation begins at the far right after d'ordre and continues in cramped short lines below that right edge, including an intervening cancellation. It is kept as the appended manuscript addition rather than reset as an ordinary left-indented array row.")
change("right-edge addition, cancelled intermediate formula",
       r"dans $\unsure{\pi_0(\Sigma_1)\times I}$",
       r"dans $\pi_0(\Sigma_0)\times\Sigma_1$",
       r"\deleted{dans $\unsure{\pi_0(\Sigma_1)\times I|\pi_0(\Sigma_0)\times\Sigma_1}$}",
       False, True, "misread symbol or index", "Symbols and indices", 17, "low",
       "The strike crosses the whole short dans line. The pi/Sigma structure is discernible, but the small internal index and final factor are merged with the crossing near the edge. I is the stronger final-factor candidate locally; the complete C-leading and H-note readings remain alternatives. H's quoted reading here comes from its explicit note on the cancellation, so the same ink is not counted again as an omission.",
       "The cancelled formula remains unresolved and is not used to complete the live one.")
change("right-edge addition, terminal live equality",
       r"\pi_0(\Sigma_0)\times\pi_0(\Sigma_0)=I",
       r"\pi_0(\Sigma_0)\times\pi_0(\Sigma_0)=I\times I",
       r"\pi_0(\Sigma_0)\times\pi_0(\Sigma_0)=I",
       False, True, "text not on the page", "Text that is not on the page", 17, "high",
       "The live lower line ends with a single I immediately against the paper edge. No additional multiplication sign or following I is visible.",
       "Only the visible =I ending is transcribed.")
change("first lower coproduct display, source argument",
       r"\Sigma_{(0)}=\coprod", r"\Sigma(0)=\coprod",
       r"\Sigma_{(0)}=\coprod",
       False, True, "misread symbol or index", "Symbols and indices", 18, "high",
       "The parenthesized zero is small and lowered beside the source Sigma. The coproduct index i in I is clear below the operator.",
       "The lowered parenthesized zero is retained.")
change("first lower coproduct display, terminal punctuation",
       r"\coprod_{i\in I}\Sigma_i",
       r"\coprod_{i\in I}\Sigma_i,\qquad",
       r"\coprod_{i\in I}\Sigma_i",
       False, True, "text not on the page", "Text that is not on the page", 18, "high",
       "The expression ends at the summand's dotted i. No comma follows it.")
change("lower coproduct equalities, stacked placement",
       "\\Sigma_i\n\\]\n\\[\n\\Sigma_{(1)}",
       r"\Sigma_i,\qquad \Sigma(1)",
       "\\Sigma_i\n\\]\n\\[\n\\Sigma_{(1)}",
       False, True, "insertion or placement", "Insertions put in the wrong place", 19, "high",
       "The second equality lies on a lower baseline, with two lines of indexing below its operator. The two equalities are retained as stacked displays; source argument shapes and punctuation are recorded separately.")
change("second lower coproduct display, source argument",
       r"\Sigma_{(1)}=\deleted{\sum}\coprod",
       r"\Sigma(1)=\coprod",
       r"\Sigma_{(1)}=\deleted{\unsure{\Sigma}}\coprod",
       False, True, "misread symbol or index", "Symbols and indices", 19, "high",
       "The parenthesized 1 is visibly lowered beside the Sigma. The crossed/overwritten former operator is handled in its own row.",
       "The written lowered argument is retained.")
change("second lower coproduct display, former operator",
       r"\deleted{\sum}\coprod", r"\Sigma(1)=\coprod",
       r"\deleted{\unsure{\Sigma}}\coprod",
       False, True, "omission", "Struck text", 19, "low",
       "A Sigma-like former sign remains inside and behind the two uprights and long bottom bar of the coproduct. An old upper stroke and portions of an angular middle survive, but the crossing and overwrite conceal enough contour to leave the identification uncertain. The tentative capital Sigma reading remains marked in place; C's literal sum command is preserved in its quotation.")
change("slanted left marginal NB, complete text and underline",
       r"\margin{\uline{NB} on suppose les comp. connexes des $\Sigma_0$ et $\Sigma_1$ ouvertes}",
       r"\marginal{\emph{NB} \ldots\ \ill{} \ldots\ $\Sigma_0$ et $\Sigma_1$ \ldots}",
       r"\margin{\uline{NB} on suppose \uline{les} comp. connexes des $\Sigma_0$ et $\Sigma_1$ ouvertes}",
       True, True, r"readable ink left as \ill{}", "Readable ink left as illegible", 20, "high",
       "After rotation, the three lines read NB on suppose / les comp. connexes des / Sigma_0 et Sigma_1 ouvertes. Comp. has a visible final point; no point follows ouvertes. NB is underlined. A second short independent baseline under les extends left of the l foot and remains below the joined e/s run, supporting that underline.",
       marked=True)
change("right explanatory block, comma between the two labels",
       r"$\uline{s},\uline{b}$", r"$\underline s$, $\underline b$",
       r"$\uline{s}\ \uline{b}$",
       True, True, "text not on the page", "Text that is not on the page", 21, "high",
       "The separately underlined s and b are divided by a blank gap. No comma is visible between them.")
change("right explanatory block, punctuation after the paired labels",
       r"compatibles avec $\uline{s},\uline{b}$",
       r"compatibles avec $\underline s$, $\underline b$,",
       r"compatibles avec $\uline{s}\ \uline{b}$",
       False, True, "text not on the page", "Text that is not on the page", 21, "high",
       "After the second underlined label the line ends without a separate comma. The internal label separator is treated in the preceding row.")
change("right explanatory block, i.e ending",
       r"i.e. $\uline{s}", r"i.e.\ $\underline s",
       r"i.e $\uline{s}",
       True, True, "abbreviation expanded or spelling modernised",
       "Abbreviations expanded, spelling modernised", 21, "high",
       "There is a point between i and e, in addition to the dot above i. The e ends in an open low return with no following point.")
change("right explanatory block, s connector",
       r"\uline{s}:\Sigma_{ij}\longrightarrow\Sigma_i",
       r"\underline s : \Sigma_{ij}\to\Sigma_i",
       r"\uline{s}:\Sigma_{ij}\mathrel{-}\Sigma_i",
       True, True, "misread symbol or index", "Symbols and indices", 21, "high",
       "The upper short shaft ends in a downturned thickening with no separately exposed V head. The literal unheaded shaft is retained with the written source and target indices.")
change("right explanatory block, stop after the s expression",
       r"\longrightarrow\Sigma_i$", r"\to\Sigma_i$,",
       r"\mathrel{-}\Sigma_i$",
       False, True, "text not on the page", "Text that is not on the page", 21, "high",
       "No comma follows the upper target Sigma's small i-like index; the next expression starts on the lower baseline.")
change("right explanatory block, b connector",
       r"\uline{b}:\Sigma_{ij}\longrightarrow\Sigma_j",
       r"\underline b : \Sigma_{ij}\to\Sigma_j",
       r"\uline{b}:\Sigma_{ij}\mathrel{-}\Sigma_j",
       True, True, "misread symbol or index", "Symbols and indices", 21, "high",
       "The lower short shaft is horizontal with a compact downstub at its right end. No separate arrowhead arms are exposed.")
change("right explanatory block, stop after the b expression",
       r"\longrightarrow\Sigma_j$", r"\to\Sigma_j$,",
       r"\mathrel{-}\Sigma_j$",
       False, True, "text not on the page", "Text that is not on the page", 21, "high",
       "The long j descent of the lower target is followed by blank paper. No separate comma ends this line.")
change("delta expression, source argument",
       r"\Sigma_{(0)}\xrightarrow{\delta}",
       r"\Sigma(0)\xrightarrow{\ \delta\ }",
       r"\Sigma_{(0)}\xrightarrow{\delta}",
       False, True, "misread symbol or index", "Symbols and indices", 22, "high",
       "The source parenthesized zero sits below/right of Sigma. Delta is written above a headed rightward shaft.",
       "The source's lowered parenthesized zero is retained.")
change("delta expression, target argument",
       r"\xrightarrow{\delta}\Sigma_{(1)}",
       r"\xrightarrow{\ \delta\ }\Sigma(1)",
       r"\xrightarrow{\delta}\Sigma_{(1)}",
       False, True, "misread symbol or index", "Symbols and indices", 22, "high",
       "The target's small parenthesized 1 descends below the Sigma body. It precedes the larger parenthesis introducing delta(x).",
       "The target's lowered parenthesized 1 is retained.")
change("delta(x) expression, densely cancelled predecessor",
       r"\deleted{\unsure{\Sigma}}", "",
       r"\deleted{\unsure{\operatorname{id}^{\uline{\Sigma}}_x}}",
       True, True, "omission", "Struck text", 22, "low",
       "The cancelled cluster includes a raised Sigma above the dark baseline mass, possible id-like strokes at its left and an x-like low return at its right. Several heavy diagonal crossings hide the remaining structure. The whole identity-shaped predecessor is retained only as a tentative mathematical reading; no illegible-word marker replaces it.",
       "The cancelled formula's additional visible structure is preserved while its reading remains open.")
change("after the cancelled et ainsi, live opening delimiter",
       r"\deleted{\unsure{et ainsi}} ce qui",
       r"\struck{\ill{}} (ce qui",
       r"\deleted{\unsure{et ainsi}} (ce qui",
       True, False, "omission", "Omissions", 23, "high",
       "A tall curved opening parenthesis follows the end of the cancellation and stands immediately before ce qui. Its upper and lower portions extend beyond the cancelling baseline and remain live.")
change("cancelled words before ce qui",
       r"\deleted{\unsure{et ainsi}}", r"\struck{\ill{}}",
       r"\deleted{\unsure{et ainsi}}",
       False, True, r"readable ink left as \ill{}", "Readable ink left as illegible", 23, "medium",
       "The initial e/t group, intervening low letters, later tall stroke and dotted i-like ending support et ainsi. A long strike masks much of the low run; the existing uncertainty stays in place.",
       marked=True)
change("next line, implique",
       "implique", "indique", "implique",
       False, True, "misread word", "Words", 24, "high",
       "After the initial dotted i and low m run is a p descent, followed immediately by a tall closed l loop. A second dotted i and the q descent follow. These visible ascenders and descenders support implique.")
change("compatibility expression, underline on the leading phi",
       r"\varphi=(\varphi_0,\varphi_1)",
       r"\varphi=(\varphi_0,\varphi_1)",
       r"\uline{\varphi}=(\varphi_0,\varphi_1)",
       True, True, "omission", "Symbols and indices", 25, "high",
       "A separate short horizontal stroke crosses the leading phi's long descent below its bowl. The first tuple component is locally retraced but remains phi-zero; no underlying old letter is isolated.")
change("last line, underline on phi after De plus",
       r"De plus, $\varphi$", r"De plus, $\varphi$",
       r"De plus, $\uline{\varphi}$",
       True, True, "omission", "Symbols and indices", 27, "high",
       "The last phi again has a short independent horizontal bar below its bowl and across the descending stem, matching the underlined functor label and the preceding compatibility expression.")
change("last line, verb after phi",
       r"$\varphi$ est un", r"$\varphi$ \uncertain{a} une",
       r"$\uline{\varphi}$ est un",
       False, True, "misread word", "Words", 27, "high",
       "The first word has a looped e-like start followed by a compact s run and a tall crossed terminal t. The written word reads est. The separate underline difference and article ending are recorded independently.",
       marked=True)
change("last line, article ending",
       "est un", r"\uncertain{a} une", "est un",
       False, True, "misread word", "Words", 27, "high",
       "The final word consists of linked low u/n arches and a terminal return. No distinct final e is visible. The page ends with un; no continuation from another leaf was consulted.")
change("bottom-left foliation and hand",
       r"\mspage{67}", "", r"\margin{67}",
       True, True, "insertion or placement", "Other", 28, "high",
       "Thin pale 6 and 7 occur at the extreme lower-left edge in another unnamed hand. They are retained as foliation. The top of the sheet has no visible authorial page number.")

OUT["decisions"] = [{
    "id": "M0615", "decision": "undecided",
    "reading": r"\unsure{anglicisme}",
    "evidence": "The initial low an run, g descent and tall l strongly favour the listed alternative anglicisme. The later letters are compressed and not all independently separated, so the mark is narrowed but remains undecided. The opening square bracket and uncertain curved/footed closing delimiter are retained in place.",
    "crop": CP[11]["file"], "box": CP[11]["box"], "confidence": "medium",
}]

def inventory(kind, position, reading, hand="his hand"):
    OUT["inventory"].append({
        "element": f"E{len(OUT['inventory'])+1:02d}", "kind": kind,
        "position": position, "first_words_or_objects": reading,
        "sheet_kind": "text", "hand": hand, "transcribed": "yes",
    })

inventory("deletion", "upper-left opening, beneath the live first line",
          r"\deleted{\unsure{Cela posé}}")
inventory("text", "top, first two running lines",
          "Cette relation est évidemment réflexive, et elle est transitive")
inventory("deletion", "first line, right of évidemment",
          r"\deleted{\unsure{symétrique}}")
inventory("insertion", "above cancelled symétrique",
          r"\inserted{réflexive}")
inventory("display", "upper opening pi-zero formula",
          r"\pi_0(\Sigma_{(2)})\longrightarrow(\pi_0(\Sigma_{(1)}),\pi_0(\uline b))")
inventory("text", "below opening display, through Lemme : Soit",
          r"est surjective, ce qui est facile à prouver")
inventory("diagram", "upper square beside Soit and un carré",
          r"X\leftarrow X';\quad Y\leftarrow Y';\quad f,f',g,g'")
inventory("text", "lemma prose and conclusion around/below the square",
          r"un carré cartésien d'espaces top, avec $f$ fibrant")
inventory("text", "middle, category paragraph",
          r"Ceci posé, considérons la catégorie top. discrète")
inventory("insertion", "above ordonné in the category paragraph",
          r"\inserted{pré}")
inventory("insertion", "above/right of isolated I, with curved leader",
          r"\inserted{$=\pi_0(\Sigma_0)$}")
inventory("insertion", "right interline after abus de langage",
          r"\inserted{[\unsure{anglicisme}\unsure{)|]}}")
inventory("insertion", "above de catégories, curved leader ending before de",
          r"\inserted{canonique}")
inventory("deletion", "after topologiques",
          r"\deleted{\unsure{canoniques|canonique}}")
inventory("display", "middle, underlined-Sigma functor",
          r"\uline{\Sigma}\xrightarrow{\uline{\varphi}}I")
inventory("text", "line introducing the two application rows",
          "qui est donc donné par des applications continues")
inventory("display", "two rows grouped by a single left brace",
          r"\Sigma_{(0)}\xrightarrow{\varphi_0}I_0=I;\quad\Sigma_{(1)}\xrightarrow{\varphi_1}I_1")
inventory("insertion", "appended at far right of the second application row, continuing below",
          r"=\text{image de }\pi_0(\Sigma_1)")
inventory("deletion", "intermediate short line inside the appended image explanation",
          r"\deleted{dans $\unsure{\pi_0(\Sigma_1)\times I|\pi_0(\Sigma_0)\times\Sigma_1}$}")
inventory("text", "below the applications, above lower coproducts",
          "i.e. des décompositions en sommes directes")
inventory("display", "first lower coproduct equality",
          r"\Sigma_{(0)}=\coprod_{i\in I}\Sigma_i")
inventory("display", "second lower coproduct equality",
          r"\Sigma_{(1)}=\deleted{\unsure{\Sigma}}\coprod_{\substack{i,\unsure{j|g}\in I\\i\leq j}}\Sigma_{ij}")
inventory("deletion", "former operator overwritten in the second lower coproduct",
          r"\deleted{\unsure{\Sigma}}")
inventory("margin note", "slanted lower-left NB, three written lines",
          r"\uline{NB} on suppose \uline{les} comp. connexes des $\Sigma_0$ et $\Sigma_1$ ouvertes")
inventory("text", "three short explanatory lines to the right of the lower coproducts",
          r"compatibles avec $\uline{s}\ \uline b$; i.e $\uline s:\Sigma_{ij}\mathrel{-}\Sigma_i$")
inventory("text", "lower main line beginning avec, with delta map and parenthesis",
          r"avec $\Sigma_{(0)}\xrightarrow{\delta}\Sigma_{(1)}$")
inventory("deletion", "after delta(x)=, densely crossed mathematical predecessor",
          r"\deleted{\unsure{\operatorname{id}^{\uline{\Sigma}}_x}}")
inventory("text", "bottom three running lines, continuing beyond this sheet",
          r"appliquant $\Sigma_i$ dans $\Sigma_{ii}$")
inventory("deletion", "after Sigma_ii and its comma, before live opening parenthesis",
          r"\deleted{\unsure{et ainsi}}")
inventory("margin note", "extreme lower-left foliation",
          r"\margin{67}", "another unnamed hand")

def doubt(place, reading, alternatives, confidence, reason):
    assert reading in TEX, ("Doubt not present in TeX", reading)
    OUT["doubts"].append({
        "place": place, "reading": reading, "alternatives": alternatives,
        "confidence": confidence, "reason": reason,
    })

doubt("top cancellation", r"\unsure{Cela posé}",
      "Cela posé, with portions masked by the strike; C's Ceci considered", "medium",
      "The tall l is clear, but the low final a and parts of posé are crossed.")
doubt("top cancelled adjective", r"\unsure{symétrique}",
      "symétrique, with low letters under the crossing", "medium",
      "The y/q descenders and tall middle strokes survive; the long strike conceals portions of the low run.")
doubt("right edge of the category-paragraph opening", r"\unsure{associé|associée}",
      "associé; associée", "low",
      "The ending meets the cut paper edge after a visible accent and low stroke. A second independent e is not isolated.")
doubt("category paragraph, I and following small mark", I_READING,
      "I plus a comma after the inserted equality; I-zero without that comma", "medium",
      "The small glyph has a comma-like head and downward tail but can be construed as a compressed zero. Each alternative includes the same one physical equality insertion.")
doubt("bracketed insertion M0615", r"\unsure{anglicisme}",
      "anglicisme; the later letters remain compressed", "medium",
      "The initial an, descending g and tall l narrow the reading; the ending does not support removing the uncertainty.")
doubt("closing delimiter of the same insertion", r"\unsure{)|]}",
      "closing parenthesis; closing square bracket", "medium",
      "The stroke curves outward and returns left at its foot, leaving its delimiter form unresolved. The left bracket remains square.")
doubt("on désignera/désigne", r"\unsure{désignera|désigne}",
      "désignera; désigne", "medium",
      "The long joined post-g run does not independently separate the final ra.")
doubt("cancelled adjective after topologiques", r"\unsure{canoniques|canonique}",
      "canoniques; canonique", "medium",
      "An extra terminal short run favours s, but it merges with the cancellation and preceding return.")
doubt("cancelled intermediate right-edge formula",
      r"\unsure{\pi_0(\Sigma_1)\times I|\pi_0(\Sigma_0)\times\Sigma_1}",
      "pi-zero(Sigma-one) times I; pi-zero(Sigma-zero) times Sigma-one", "low",
      "The small internal index and last factor are covered by the long strike and crowded against the paper edge.")
doubt("second lower coproduct, cancelled former sign", r"\unsure{\Sigma}",
      "Sigma-like sign, with contour obscured by cancellation and overwrite", "low",
      "The old upper stroke and angular middle are partly visible beneath the coproduct, but the heavy shared strokes conceal the full outline.")
doubt("second lower coproduct, upper index line", r"\unsure{j|g}",
      "j; g-like looped form", "medium",
      "The letter after the comma has a closed/looped head and long descent. The leading j agrees with the root reader, while the local contour remains g-like to this first reader.")
doubt("cancelled predecessor of the final identity expression",
      r"\unsure{\operatorname{id}^{\uline{\Sigma}}_x}",
      "an id-like expression with raised underlined Sigma and lower x; whole reading tentative", "low",
      "Only the raised Sigma, possible left id strokes and a low x-like tail can be isolated through the dense cancellation.")
doubt("cancelled words before the final parenthesis", r"\unsure{et ainsi}",
      "et ainsi, with masked low letters", "medium",
      "Tall strokes and the dotted ending support the phrase, but the cancellation obscures the middle run.")

OUT["notes"] = [
    {
        "id": "150-068-N01",
        "text": "This sheet has no visible authorial page number. Pale foliation 67 at the lower left belongs to another unnamed hand. The main writing includes an opening relation paragraph, a passage headed Lemme with a four-object square, a topological-category paragraph, a functor display, two application rows, two lower coproduct displays, a slanted NB and a continuation at the bottom.",
    },
    {
        "id": "150-068-N02",
        "text": "The manuscript cancels Cela posé and later symétrique at the top, adding réflexive above the latter. It then writes a transitivity assertion and an opening pi-zero expression. The small parenthesized Sigma arguments are physically lowered at every inspected occurrence on this sheet. Those placements and the underlined b/s labels are retained from the ink.",
    },
    {
        "id": "150-068-N03",
        "text": "The passage headed Lemme contains the square X, X-prime, Y, Y-prime with labels f, f-prime, g, g-prime, followed by a pi-zero expression and the word surjectif. The manuscript calls the square cartésien and uses fibrant in the adjoining prose. These are descriptions of what the manuscript writes; no proof check is claimed. The two vertical terminal shapes are represented directly as filled ink, rounded on the left and more pointed on the right.",
    },
    {
        "id": "150-068-N04",
        "text": "The category paragraph has a written interlinear pré, an added equality =pi_0(Sigma_0), a bracketed word strongly favouring anglicisme and a relocated canonique. The small glyph beside I is comma-like, but I-zero is retained as a local alternative. Each branch of the marked I expression repeats the same one physical equality insertion so that its attachment and punctuation remain explicit.",
    },
    {
        "id": "150-068-N05",
        "text": "The manuscript writes an underlined-Sigma to I functor with an underlined varphi label, followed by phi-zero and phi-one application rows. The explanation of I-one is appended at the far right and contains a cancelled intermediate ending. Its live last line visibly stops at =I against the paper edge. No continuation beyond the edge is supplied. The cancellation's index and final factor remain unresolved.",
    },
    {
        "id": "150-068-N06",
        "text": "The lower displays contain two separate coproduct equalities; the second overwrites a former sign tentatively read as Sigma, whose contour remains partly concealed. In the slanted NB the author writes that the comp. connexes of Sigma_0 and Sigma_1 are ouvertes. The abbreviation and the underlines of NB and les are retained. This reports the author's marginal assumption without checking it.",
    },
    {
        "id": "150-068-N07",
        "text": "The right-hand explanatory block has two separately underlined labels and two short unheaded connectors. The following delta expression contains a densely cancelled mathematical predecessor, tentatively read as an identity-shaped expression with raised Sigma and lower x. Its structure remains marked as doubtful, while the rewritten identity expression to its right is readable.",
    },
    {
        "id": "150-068-N08",
        "text": "The bottom prose has a live opening parenthesis after cancelled et ainsi, the word implique, an underlined varphi in the compatibility expression and another underlined varphi after De plus. The last words on this sheet read est un. The transcription was made only from this assigned leaf and its two drafts; no following leaf was consulted to complete the phrase.",
    },
]
OUT["notation"] = [
    {
        "form": r"\Sigma_{(0)},\Sigma_{(1)},\Sigma_{(2)}",
        "meaning": "The author's locally lowered parenthesized arguments in the pi-zero, application, coproduct and delta expressions.",
        "evidence": "The smaller argument groups begin lower than the Sigma tops and extend below their baselines.",
        "places": "068: opening display; two application rows; lower coproducts; delta source and target",
    },
    {
        "form": r"\pi_0",
        "meaning": "The symbol repeatedly used in the manuscript's opening, lemma and image expressions.",
        "evidence": "A flat cap and two descending legs with a small lowered round zero; one right-edge occurrence is retraced.",
        "places": "068: opening display, lemma conclusion, inserted equality and right-edge explanation",
    },
    {
        "form": r"\uline{\Sigma}\xrightarrow{\uline{\varphi}}I",
        "meaning": "The functor expression written by the author.",
        "evidence": "Separate lower bars under Sigma and varphi; target I has its normal foot only.",
        "places": "068: middle functor display, p15",
    },
    {
        "form": r"\uline{\varphi}=(\varphi_0,\varphi_1)",
        "meaning": "The equality written in the author's final compatibility sentence.",
        "evidence": "Independent bar across the first phi descent, followed by equals, parentheses and lowered 0/1 labels.",
        "places": "068: lower compatibility expression, p25",
    },
    {
        "form": r"\uline{s}:\Sigma_{ij}\mathrel{-}\Sigma_i;\quad\uline{b}:\Sigma_{ij}\mathrel{-}\Sigma_j",
        "meaning": "The two short expressions written beside the lower coproducts.",
        "evidence": "Separate label underlines and horizontal shafts with downturned terminal thickenings, without exposed V heads.",
        "places": "068: lower right explanatory block, p21",
    },
    {
        "form": r"\operatorname{id}^{\uline{\Sigma}}_x",
        "meaning": "The readable rewritten expression following delta(x)= and the crossed predecessor.",
        "evidence": "Small id at baseline, Sigma with an independent bar above/right, and x below it.",
        "places": "068: delta parenthesis, p22",
    },
    {
        "form": r"\unsure{$I$\inserted{$=\pi_0(\Sigma_0)$},|$I_0$\inserted{$=\pi_0(\Sigma_0)$}}",
        "meaning": "The unresolved I/punctuation unit and its one physical equality insertion.",
        "evidence": "Dark small head with downward tail beside I and a distinct curved insertion leader.",
        "places": "068: category paragraph, p10",
    },
]
OUT["abbreviations"] = [
    {"written": "top", "expansion": "topologiques", "places": "068: d'espaces top, in the lemma"},
    {"written": "top.", "expansion": "topologique", "places": "068: catégorie top. discrète"},
    {"written": "ens", "expansion": "ensemble", "places": "068: category paragraph"},
    {"written": "NB", "expansion": "nota bene", "places": "068: slanted left margin"},
    {"written": "comp.", "expansion": "composantes", "places": "068: slanted left margin"},
    {"written": "i.e.", "expansion": "id est", "places": "068: line introducing the lower decompositions"},
    {"written": "i.e", "expansion": "id est", "places": "068: right explanatory block, no terminal point"},
    {"written": "id", "expansion": "identité", "places": "068: delta parenthesis"},
]
OUT["hand_log"] = [
    {
        "habit": "Small parenthesized numerical arguments are placed below/right of Sigma.",
        "places": "068: opening display, both applications, both lower coproducts and delta expression",
        "scope": "All ten locally inspected parenthesized Sigma arguments on this leaf.",
        "witness_errors": "H sets these argument groups at the main baseline; C retains the lowered placement.",
    },
    {
        "habit": "Short independent underlines can cross a descending letter stem.",
        "places": "068: functor varphi, compatibility varphi, final varphi, s/b labels and marginal les",
        "scope": "Each bar was distinguished from the letter body on its local crop.",
        "witness_errors": "Both drafts omit the two lower varphi underlines and the underline of les; H reads the functor label as f and adds an underline to the target I.",
    },
    {
        "habit": "Compact terminal returns obscure whether a final low letter is present.",
        "places": "068: clipped associé/associée, désignera/désigne and cancelled canoniques/canonique",
        "scope": "The three endings remain locally marked; no grammatical completion is made.",
        "witness_errors": "The two drafts disagree in the latter two places; both give a complete associée at the cut edge.",
    },
    {
        "habit": "A small zero-like mark can have a comma-shaped head and tail.",
        "places": "068: beside the category-paragraph I",
        "scope": "This one occurrence remains uncertain; other clear numerical zeros are retained.",
        "witness_errors": "C reads I-zero without a following comma; H reads I with a comma after the insertion.",
    },
    {
        "habit": "Crossing and retracing conceal small indices and former glyph groups.",
        "places": "068: cancelled right-edge formula, overwritten lower operator, cancelled identity predecessor and phi-zero in the final tuple",
        "scope": "Recoverable contours are retained. No old letter is invented beneath the retraced tuple component.",
        "witness_errors": "C/H-note readings differ in the cancelled right-edge formula; H omits the former lower operator and cancelled identity predecessor from the body.",
    },
    {
        "habit": "Some j-like index forms have looped heads.",
        "places": "068: upper index line below the second lower coproduct",
        "scope": "The leading j remains locally doubtful to this first reader despite the root reader's clearer j reading.",
        "witness_errors": "Both drafts give j; the added doubt is not counted as a textual change.",
    },
    {
        "habit": "Arrow endpoints range from exposed heads to filled end marks and simple downstubs.",
        "places": "068: lemma square, pi-zero maps, functor/applications and right explanatory block",
        "scope": "Both ends and all labels of every connector were inspected.",
        "witness_errors": "Both drafts regularise the two short right-hand connectors as arrows and the square's filled vertical tips as ordinary heads.",
    },
    {
        "habit": "Abbreviation stops and commas vary independently.",
        "places": "068: top followed by comma, later top., ens, comp. and the two i.e forms",
        "scope": "Punctuation is read at each occurrence.",
        "witness_errors": "Both drafts add a stop before the lemma's top comma and after the right-hand i.e; H adds a stop after ens and several commas in the right block.",
    },
]

def audit(p, kind, reading, box=None, comment=""):
    bounds = CP[p]["box"] if box is None else box
    row = {
        "box": f"B{len(OUT['audit_boxes'])+1:02d}", "kind": kind,
        "x0": bounds[0], "y0": bounds[1], "x1": bounds[2], "y1": bounds[3],
        "reading": reading,
    }
    if comment:
        row["comment"] = comment
    OUT["audit_boxes"].append(row)

audit(1, "struck passage", r"\deleted{\unsure{Cela posé}} Cette relation",
      comment="The principal target is the lower cancelled phrase; the upper live words are context.")
audit(2, "insertion", r"\deleted{\unsure{symétrique}}\inserted{réflexive},",
      comment="Lower fragments belong to the next baseline.")
audit(3, "handwritten number",
      r"$\pi_0(\Sigma_{(2)})\longrightarrow(\pi_0(\Sigma_{(1)}),\pi_0(\uline b))\times_{\pi_0(\Sigma_{(0)})}(\pi_0(\Sigma_{(1)}),\pi_0(\uline s))$",
      comment="Complete opening formula, including all four parenthesized Sigma arguments and every pi-zero index.")
audit(4, "doubtful formula", r"$\uline b$ est fibrant,",
      comment="Upper curved stroke is the descent from the previous line; lower clipped f-prime belongs to the diagram.")
audit(5, "doubtful formula", DIAGRAM,
      comment="Whole square, including both vertical terminal shapes and all four labelled connectors.")
audit(6, "lexical disagreement", r"cartésien d'espaces top, avec $f$ fibrant,",
      comment="Small g fragment at the upper edge belongs to the diagram above.")
audit(7, "handwritten number",
      r"alors $\pi_0(X')\longrightarrow\pi_0(X)\times_{\pi_0(Y)}\pi_0(Y')$ est surjectif",
      comment="Complete formula and right-edge word ending; small upper context is from the preceding line.")
audit(8, "medium-confidence departure", r"top. discrète \unsure{associé|associée}",
      comment="The final low letter run meets the cut right paper edge.")
audit(9, "insertion", r"à l'ens \inserted{pré}ordonné",
      comment="A small upper clipped descent belongs to the preceding line.")
audit(10, "doubtful formula", I_READING + " que",
      comment="Whole I/equality unit and leader. Upper clipped letters and the right-edge tall fragment are neighbouring text.")
audit(11, "insertion", r"\inserted{[\unsure{anglicisme}\unsure{)|]}}",
      comment="Upper loops belong to langage and the lower clipped stem belongs to foncteur.")
audit(12, "lexical disagreement", r"on \unsure{désignera|désigne} par",
      comment="The lower clipped word is the canonique insertion, separately boxed.")
audit(13, "insertion", r"\inserted{canonique} de",
      comment="The upper-right loop belongs to désignera; the lower-right partial word is catégories.")
audit(14, "struck passage", r"\deleted{\unsure{canoniques|canonique}}")
audit(15, "doubtful formula", r"$\uline{\Sigma}\xrightarrow{\uline{\varphi}}I$")
audit(16, "handwritten number", r"$\Sigma_{(0)}\xrightarrow{\varphi_0}I_0=I$",
      comment="The left brace continues into the next row; small lower fragments belong to that next row.")
audit(17, "doubtful formula",
      r"$\Sigma_{(1)}\xrightarrow{\varphi_1}I_1=\text{graphe de la relation d'ordre}$ " + REVISED_IMAGE,
      comment="Whole second application row and all its appended right-edge revisions; upper clipped fragments belong to the first row.")
audit(17, "struck passage",
      r"\deleted{dans $\unsure{\pi_0(\Sigma_1)\times I|\pi_0(\Sigma_0)\times\Sigma_1}$}",
      box=[1443,1573,1673,1620],
      comment="Individual tight cancellation region; the complete surrounding formula is B17.")
audit(18, "handwritten number", r"$\Sigma_{(0)}=\coprod_{i\in I}\Sigma_i$")
audit(19, "doubtful formula",
      r"$\Sigma_{(1)}=\deleted{\unsure{\Sigma}}\coprod_{\substack{i,\unsure{j|g}\in I\\i\leq j}}\Sigma_{ij}$",
      comment="Complete second lower equality, former operator and two index lines. The tiny lower-left fragment belongs to delta below.")
audit(19, "struck passage", r"\deleted{\unsure{\Sigma}}\coprod_{\substack{i,\unsure{j|g}\in I\\i\leq j}}",
      box=[717,1848,859,2003],
      comment="Individual overwritten-operator/index region; the complete equality is B20.")
audit(20, "margin note",
      r"\margin{\uline{NB} on suppose \uline{les} comp. connexes des $\Sigma_0$ et $\Sigma_1$ ouvertes}",
      comment="Original unrotated coordinates. The existing inspection crop was rotated −14 degrees.")
audit(21, "doubtful formula",
      r"compatibles avec $\uline{s}\ \uline b$ / i.e $\uline s:\Sigma_{ij}\mathrel{-}\Sigma_i$ / $\uline b:\Sigma_{ij}\mathrel{-}\Sigma_j$",
      comment="Three independent right-hand baselines; slash separators describe the recorded line divisions.")
audit(22, "doubtful formula",
      r"$\Sigma_{(0)}\xrightarrow{\delta}\Sigma_{(1)}$ ($\delta(x)=\deleted{\unsure{\operatorname{id}^{\uline{\Sigma}}_x}}\operatorname{id}^{\uline{\Sigma}}_x$)",
      comment="Whole map and parenthetical formula. Upper clipped i≤j belongs to the preceding coproduct.")
audit(22, "struck passage",
      r"\deleted{\unsure{\operatorname{id}^{\uline{\Sigma}}_x}}",
      box=[1137,1976,1293,2070],
      comment="Individual dense cancellation region; the entire formula is B24.")
audit(23, "struck passage", r", \deleted{\unsure{et ainsi}} (ce qui",
      comment="Lower clipped strokes belong to the following prose line.")
audit(24, "lexical disagreement", "implique",
      comment="Upper clipped descent belongs to appliquant on the preceding baseline.")
audit(25, "handwritten number", r"$\uline{\varphi}=(\varphi_0,\varphi_1)$",
      comment="Complete equality, including both numerical component indices.")
audit(26, "lexical disagreement", "la composition). De plus,",
      comment="Upper clipped descenders belong to the previous line.")
audit(27, "lexical disagreement", r"$\uline{\varphi}$ est un")
audit(28, "handwritten number", r"\margin{67}")

OUT["unresolved"] = [
    "Masked letters of the cancelled opening Cela posé and symétrique.",
    "The clipped associé/associée ending at the right edge.",
    "Comma versus zero-like mark beside I; the one inserted equality is retained in both local alternatives.",
    "Anglicisme's compressed ending (M0615) and the shape of its right closing delimiter.",
    "Désignera/désigne and cancelled canoniques/canonique endings.",
    "The cancelled intermediate right-edge formula's index and final factor.",
    "The Sigma-like cancelled sign obscured beneath the second lower coproduct.",
    "The looped j/g-like glyph in the upper index line under the second lower coproduct.",
    "The densely cancelled identity-shaped predecessor after delta(x)=, and masked low letters of et ainsi.",
]
with (EDITION / "packets/150_scan068/diffs.tsv").open(newline="") as f:
    DIFFERENCES = list(csv.DictReader(f, delimiter="\t"))
OUT["coverage"] = {
    "whole_image_viewed": True,
    "halves_viewed": ["top", "bottom"],
    "all_tokens_read": True,
    "all_C_insertions_deletions_checked": True,
    "differences_considered": len(DIFFERENCES),
    "macro_only_differences_ignored": (
        "Equivalent underline/emphasis wrappers where the source has a bar, braces, to/longrightarrow for visible heads, math spacing, "
        "aligned versus array, and inline/display wrappers without a material source-placement difference. "
        "H's editorial page synopsis and explanatory notes are not inserted into manuscript text. Its quoted reading of the cancelled right-edge formula is compared explicitly in one row. "
        "The packet's apparent extra i in the lower coproduct indexing is a token-alignment artefact: both source files give i,j in I and i≤j. "
        "Certainty-only additions are listed as doubts and are excluded from textual change totals."
    ),
    "visual_pass_detail": (
        "The original whole image and both premade halves were explicitly viewed once each. All 28 first-pass crops were emitted and read; "
        "the root independently reviewed all 28. The original dimensions are 1684×2361. No OCR, external source, compilation or mathematical proof check was used."
    ),
    "line_count_method": (
        "26 principal prose/display/right-explanation baselines: 23 main prose or displayed-expression baselines and the three short lines of the right explanatory block. "
        "Interlinear revisions, the slanted NB and the square's internal node rows are inventoried separately."
    ),
    "audit_coverage": (
        "The 31 preliminary boxes cover the complete opening formula, the whole revised right-edge formula, all other formulas carrying a doubt or written numeral, "
        "every insertion, cancellation, margin and lexical difference. Separate tight boxes are supplied for the right-edge cancellation, overwritten lower operator and cancelled identity predecessor. "
        "Comments identify clipped neighbouring baseline fragments without completing their text inside a narrow box."
    ),
}
OUT["comparison_counts"] = {
    "rows": len(OUT["changes"]),
    "against_C": sum(r["against_C"] for r in OUT["changes"]),
    "against_H": sum(r["against_H"] for r in OUT["changes"]),
    "by_confidence": dict(collections.Counter(r["confidence"] for r in OUT["changes"])),
    "against_C_by_confidence": dict(collections.Counter(r["confidence"] for r in OUT["changes"] if r["against_C"])),
    "against_H_by_confidence": dict(collections.Counter(r["confidence"] for r in OUT["changes"] if r["against_H"])),
    "counting_rule": "Leading proposed candidate compared with each draft; equivalent syntax and certainty-only additions are excluded. The same physical feature is not counted again for context included in a longer quotation.",
}

# Structural checks only. No compilation or mathematical validation.
with (EDITION / "packets/150_scan068/marks.tsv").open(newline="") as f:
    MARKS = list(csv.DictReader(f, delimiter="\t"))
assert [m["id"] for m in MARKS] == [d["id"] for d in OUT["decisions"]]
assert TEX.count(r"\unsure{") == len(OUT["doubts"])
assert len(CROPS) == 28 and all((EDITION/c["file"]).is_file() for c in CROPS)
assert all(0 <= b["x0"] < b["x1"] <= 1684 and 0 <= b["y0"] < b["y1"] <= 2361 for b in OUT["audit_boxes"])
# The I alternatives repeat a single physical equality insertion once.
assert TEX.count(r"\inserted{") - 1 == sum(i["kind"] == "insertion" for i in OUT["inventory"])
assert TEX.count(r"\deleted{") == sum(i["kind"] == "deletion" for i in OUT["inventory"])
assert len(OUT["audit_boxes"]) == 31
atomic_text(EDITION / "reader_returns/150_scan068.json", json.dumps(OUT, ensure_ascii=False, indent=2)+"\n")
print(json.dumps({
    "tex": str(EDITION / "reader_returns/150_scan068.tex"),
    "json": str(EDITION / "reader_returns/150_scan068.json"),
    "counts": OUT["comparison_counts"],
    "decisions": len(OUT["decisions"]), "inventory": len(OUT["inventory"]),
    "doubts": len(OUT["doubts"]), "audit_boxes": len(OUT["audit_boxes"]),
    "crops": len(CROPS), "packet_differences": len(DIFFERENCES),
}, ensure_ascii=False, indent=2))
