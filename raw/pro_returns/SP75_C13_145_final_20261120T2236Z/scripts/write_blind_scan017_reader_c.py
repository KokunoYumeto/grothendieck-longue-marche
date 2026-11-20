from pathlib import Path
import csv,json,hashlib
root=Path("/workspace/scratch/937907bd75d7/SP75_C13_145_work")
edition=root/"edition"
packet=root/"audit_packets/145_scan017"
out=edition/"second/145_scan017_second.tsv"
provisional=edition/"second/145_scan017_crop_manifest.provisional.json"
final_manifest=edition/"second/145_scan017_crop_manifest.json"
rows=[
("B01",r"""7""",
"Handwritten top numeral 7, with a transverse stroke. Uppermost stroke meets the physical upper paper edge. No second numeral or adjacent punctuation is established."),
("B02",r"""\deleted{\unsure{comprenant|correspondant}}""",
"Single long cancelled word. Opening com-/comp- and terminal tall stroke remain visible; horizontal cancellation obscures central letter junctions, so the complete lexical reading remains doubtful."),
("B03",r"""$(\gamma,l)$ d'un $\gamma\in\Gamma$""",
"Both gamma heads, pair comma and closing parenthesis, and capital Gamma are visible. Gamma has one full left leg and a short downturned right tip. Looped l is darkly retraced but no separate cancellation is securely established."),
("B04",r"""$l$ \unsure{/|)} de $P$ dans $\gamma^{-1}(P)$,""",
"Initial l stands higher than following de. Adjacent long curved oblique stroke may be an insertion guide or parenthesis-like stroke; retained as a graphic doubt. Both characters of inverse exponent are distinct. Final comma follows formula. No missing left context supplied."),
("B05",r"""$(\gamma,l)(\gamma',l')=(\inserted{\gamma\gamma',}\gamma'^{-1}(\unsure{l})\circ l')$""",
"Product gamma gamma-prime and its comma are raised inside large right-hand parenthesis. Action factor has prime and inverse -1. Argument has overlapping pale and dark strokes, so l remains doubtful. Circle composition sign and final l-prime are clear. No final stop."),
("B06",r"""i.e. “composant les chemins comme des fonctions”""",
"Complete quoted explanation, with both double quotation marks visible. Short isolated dark dash lies below opening portion of comme; it is not a continuous underline and its role is uncertain. Upper edge clips preceding formula."),
("B07",r"""\uline{\unsure{à|:} gauche}""",
"Long single underline spans initial sign and gauche. First sign has detached upper mark and lower hook: à favoured, but two-stroke appearance leaves colon-like alternative. The g descender crosses underline. No terminal punctuation."),
("B08",r"""d'un rev. étale \inserted{$U'$}, à""",
"Raised U-prime joined to gap after étale by oblique insertion guide; baseline comma separate. rev. copied without supplying absent accent. Upper edge contains incidental les groupoïdes and clipped beginning of following word, not completed from context."),
("B09",r"""$l_{\unsure{\bullet|*}}:U'_{\unsure{x|a}}\longrightarrow U'_y\,\ldots)$""",
"Lower-right mark after l is solid point without secure star arms. First U subscript has closed/angular body, leaving x versus a doubtful. Both U primes and y descender visible. Arrow has no tail bar. Three dots and closing parenthesis present; no opening supplied."),
("B10",r"""On choisit des éléments
$\sigma_0,\sigma_1,\sigma_\infty\quad\text{sur}\quad\dot\sigma_0,\dot\sigma_1,\dot\sigma_\infty$
comme les couples d'un $\sigma_i$, et des chemins \inserted{$\unsure{\lambda_i|l_i}$} de""",
"Lists distinguish undotted and dotted sigma heads; all 0, 1, infinity and i indices copied. Small raised path label at lower right has curved lambda/l-like head and short index, with guide before final de. Lower row and upper ascenders meet boundaries; visible wording not extended beyond de. Isolated speck well left of display is not sigma dot."),
("B11",r"""$P:\bar P=\sigma_iP$ qui se fait sur \deleted{\unsure{l'équateur|l'hémisphère}} \inserted{celui des} \unsure{demi-|deux-}""",
"Bar over second P and colon after first P distinct. Word after sur horizontally cancelled; body descender and lettering overlapped, hence two uncertain candidates. Raised celui des retained. Following live word has terminal horizontal continuation stroke: demi- favoured, deux- alternative. Lower-edge raised wording belongs to B12."),
("B12",r""", \deleted{\unsure{stable} par $\unsure{\dot\tau|à}$ la \unsure{symétrie}}
\inserted{\unsure{passant|en un} \unsure{aux|au} \unsure{pts|pt} \unsure{fixes|fixe}}""",
"Lower line crossed by long horizontal stroke. Initial word favours stable; final symétrie has descender and tall t-like stroke. Dotted/accented small sign between par and la unresolved. Four raised groups difficult: third resembles pt/pts abbreviation and last fixe/fixes; no grammatical completion imposed. Upper edge clips earlier cancelled word."),
("B13",r"""\deleted{$\unsure{\tau\sigma_i}$} de la symétrie $\dot\tau\dot\sigma_i=\dot\sigma_i\dot\tau$ (symétrie\unsure{,|:}""",
"Initial crossed product has uncertain exact heads/dot state. Live equality has separate upper points distinguishing dotted tau and sigma factors; i subscripts remain lower. Opening parenthesis precedes second symétrie. Tiny terminal marks leave comma versus colon uncertain. Next line clipped below; no closing parenthesis supplied."),
("B14",r"""p.r. à un plan, fixant $P,\bar P,a_i$ $(=0,1\,.\!-\!\,\infty)$ et""",
"Abbreviation p.r. literal. P-bar and commas between fixed objects visible. No independent i before equals securely established inside parenthesis. Between 1 and infinity is point followed by short horizontal stroke, copied literally without three-dot normalization. Ending et live."),
("B15",r"""\unsure{échangeant} les deux autres $a_j,a_k$) et en passant
par $a_i$. \deleted{\unsure{A\ldots|On}} Désignant par $l_0,l_1,l_\infty$ les
\inserted{\margin{(pour $\unsure{\lambda_i|1}\unsure{\in\Gamma|(-\Gamma)}$)}}""",
"Both main lines and small right insertion retained. Cancelled compact word before Désignant has capital-like initial and oval terminal trace but no secure expansion. Stroke below Désignant is g descender, not underline. Marginal insertion starts pour; tiny later glyphs/delimiters unresolved. Long curved right-margin guide passes beside final l-infinity/les, attachment uncertain, not treated as factor parenthesis. a_j,a_k and closing parenthesis visible."),
("B16",r"""lacets en sens direct\unsure{:|;} autour de $0,1,\infty$ à partir""",
"Complete main line. Two small vertically separated marks beneath end of direct retained as punctuation uncertainty. Three puncture numerals plain and comma-separated. Final partir compressed at right edge but readable. Upper-edge strokes are clipped neighbours."),
("B17",r"""de $P$, en allant vers $\unsure{a_0|0},\unsure{a_1|1},\unsure{a_\infty|\infty}$ suivant des""",
"Three destination signs heavily joined/retraced; possible a heads attached to numeral-like lower bodies retained as alternatives rather than omitted. Commas separate all three. en allant vers and suivant des visible. No terminal punctuation supplied."),
("B18",r"""des quarts de grands cercles, on trouve""",
"Complete prose phrase. Comma after cercles clear. Upper portions of trouve meet boundary but lower sequence readable. Bottom edge clips tops of numbered equation covered in B19."),
("B19",r"""$(1)\quad\big|\quad l_\infty l_1^{\unsure{\prime|\text{trace}}}l_0=1$""",
"Equation label (1), three l factors and final 1 included. Long isolated vertical rule precedes product, with no matching right rule. Small detached raised stroke between l1 and l0 may be prime or pen trace, explicitly retained. Rule not interpreted as absolute value. Lower edge clips following comment."),
("B20",r"""(et non $l_0l_1l_\infty=1$ ! \unsure{\}|)} On peut l'écrire $l_0^{-1}l_1^{-1}l_\infty^{-1}=1$)""",
"Complete lower parenthetical passage. Exclamation distinct. Immediately after it unusual tall closing graphic has small upper loop/trace and lower hooked foot: brace versus parenthesis uncertain. All three inverse -1 exponents and final closing parenthesis visible. Upper numbered relation covered in B19, not substituted for lower line."),
("B21",r"""\mspage{16}""",
"Clear handwritten footer 16. Large enlargement reflects small original box. No punctuation or additional numeral.")
]
with (packet/"boxes.tsv").open(encoding="utf-8",newline="") as f:
    expected=list(csv.DictReader(f,delimiter="\t"))
manifest=json.loads(provisional.read_text(encoding="utf-8"))
assert len(rows)==len(expected)==len(manifest)==21
assert [r[0] for r in rows]==[r["box"] for r in expected]==[r["box"] for r in manifest]
assert not out.exists() and not final_manifest.exists()
for (box,reading,observations),prescribed,entry in zip(rows,expected,manifest):
    assert reading.strip() and observations.strip()
    assert entry["coords"]==[int(prescribed[k]) for k in ("x0","y0","x1","y1")]
    assert (edition/entry["crop"]).is_file()
    entry.update(inspected=True,observations=observations,submission_status="COMPLETE AND IMMUTABLE")
with out.open("w",encoding="utf-8",newline="") as f:
    writer=csv.writer(f,delimiter="\t",lineterminator="\n")
    writer.writerow(["box","reading"])
    writer.writerows((box,reading) for box,reading,_ in rows)
with out.open(encoding="utf-8",newline="") as f:
    reread=list(csv.DictReader(f,delimiter="\t"))
assert [(r["box"],r["reading"]) for r in reread]==[(b,r) for b,r,_ in rows]
assert all(e["inspected"] and e["observations"].strip() for e in manifest)
provisional.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
provisional.rename(final_manifest)
print("Validated 21 ordered independent readings and 21 inspected crop records. No comparisons performed.")
for path in (out,final_manifest):
    print(str(path))
    print("SHA256 "+hashlib.sha256(path.read_bytes()).hexdigest())

