from pathlib import Path
import csv, json, hashlib

root = Path("/workspace/scratch/937907bd75d7/SP75_C13_145_work")
edition = root / "edition"
target = root / "audit_packets/145_scan013"
out = edition / "second/145_scan013_second.tsv"
manifest_path = edition / "second/145_scan013_crop_manifest.json"

rows = [
("B01", r"""Comme $\operatorname{int}(l_0)\sigma_\infty$ fixe $\overset{\unsure{6|\sigma}}{l_\infty}$ (mais n'est peut-être
pas de carré $l_\infty$) donc \unsure{en} \unsure{multipliant|multiplions} à droite par un $\operatorname{int}(l_\infty^\alpha)$
$(\alpha\in\hat Z)$.
\deleted{$\varepsilon_\infty(l_\infty)=l_\infty,\quad\varepsilon_\infty(l_0)=$}""",
"""Complete opening passage and overlapping cancelled equation. Small detached upper curved mark lies above the end of 'fixe'/before l-infinity; its glyph and attachment are unresolved, so the overset position is approximate. The faint words 'en multipliant' overlap the lower material. The final int expression is raised; insertion status is not established. Hat over Z is visible. The cancelled final equality has no right-hand term."""),
("B02", r"""\deleted{$\varepsilon_\infty(l_\infty)=l_\infty,\quad\varepsilon_\infty(l_0)=$}""",
"""Horizontal strike crosses this entire unfinished equation. All written indices are included; no term follows the final equals sign. Upper-edge prose and lower-edge raised material are incidental clipped neighbours."""),
("B03", r"""$\varepsilon_\infty=(\operatorname{int}(l_0)\sigma_\infty)^{\inserted{\operatorname{int}(l_\infty^\alpha)}}\quad i.e.\quad
\varepsilon_\infty\unsure{(}l_0)=l_0l_1l_0^{-1},\quad
\varepsilon_\infty(l_1)=l_0\unsure{,}\quad
\varepsilon_\infty(l_\infty)=l_{\unsure{\infty}}$
\begin{tikzpicture}[x=1cm,y=1cm,baseline]\draw (0,.35) .. controls (.5,.05) and (.8,-.2) .. (1,-.35); \draw (.89,-.35)--(1,-.35)--(.98,-.23);\end{tikzpicture}""",
"""Raised int(l-infinity^alpha) addition belongs to the exponent of the parenthesized definition. First image formula lacks a securely visible opening parenthesis; its closing parenthesis is plain. A long arcing connector descends from the upper constraint region through/near the second image's final l0; the apparent following comma may belong to its hooked end. The small TikZ records that connector schematically, without assigning an algebraic role. Final right-hand index is partly clipped at the physical page edge. Top edge includes clipped preceding cancellation."""),
("B04", r"""\deleted{$\varepsilon_0=\operatorname{int}(l_{\unsure{1}})\sigma_0$}
\deleted{$\varepsilon_1=\operatorname{int}(l_\infty)\sigma_1$}""",
"""Two definitions cancelled by long oblique strokes. First inner l index is crossed and compressed, with 1 favoured. The second inner index has the two-loop infinity form. Fragments from the preceding connector/line occur at the upper edge; they are not an additional complete equation in this box."""),
("B05", r"""On \deleted{aura \unsure{donc}} \inserted{doit écrire $\varepsilon_\infty^2=l_\infty\unsure{..|:}$}""",
"""Baseline 'aura donc' has horizontal cancellation; 'doit écrire' and the square equation are above it. The two small terminal points are retained as a punctuation/count doubt rather than normalized to three ellipsis points. The next baseline word begins at the right edge and is covered by B06."""),
("B06", r"""Écrivons $\unsure{\times|\triangleright}\ \unsure{g|\dot g}\unsure{.}$ au lieu de $\operatorname{int}(g)$ pour $g\in\Pi$, """,
"""The central notation has a looped descending g-like head. A detached angular trace precedes it and a low point follows it; the exact special mark/dot convention is not securely established from ink, hence explicit alternatives. 'au lieu de int(g) pour g in Pi' is read directly. Final comma is visible. The top edge clips the preceding square equation."""),
("B07", r"""i.e. identifiant $\Pi$ à un ss-groupe de $\operatorname{Aut}(\Pi)$, \unsure{je|les} \deleted{\unsure{form\ldots}} \inserted{\unsure{peux|pour\ldots}}""",
"""The main clause through Aut(Pi) is faint but readable. The short following word and the cancelled/replacement word at the extreme right remain unresolved; the upper replacement and lower struck body are both recorded. Their endings meet the physical page edge. No continuation is supplied from another source."""),
("B08", r"""\deleted{\unsure{comme} $\varepsilon_\infty=l_0\sigma_\infty$}. $\varepsilon_\infty=l_0\sigma_\infty l_\infty^\alpha$\unsure{.}""",
"""Long horizontal cancellation traverses the opening word and first epsilon definition. A separate point after the cancelled definition is visible. The live definition has a clear alpha exponent. A small dark terminal fleck after the live formula may be punctuation or a pen trace; retained doubtful."""),
("B09", r"""\deleted{$\varepsilon_\infty^2=l_0\sigma_\infty l_0\sigma_\infty=l_0\sigma_\infty l_0\sigma_\infty^{-1}=l_0\sigma_\infty(l_0)$}""",
"""Entire line has one horizontal strike. The square exponent and inverse exponent are individually visible. Complete three-equality chain, including final argument and closing parenthesis, is recorded. No terminal stop is established."""),
("B10", r"""\unsure{donc|de} $\varepsilon_\infty^2=l_0\underbrace{\sigma_\infty l_\infty^\alpha\unsure{l_0|\deleted{l_0}}\sigma_\infty}\underbrace{l_\infty^\alpha}$""",
"""The short initial prose word is compressed. The middle l0 has a heavy crossing/retracing, with cancellation versus retraced live state unresolved. Below the formula the first grouping line is predominantly straight with upturned ends, spanning approximately first sigma-infinity through second sigma-infinity; the second underbrace has a downward cusp under the final l-infinity^alpha. No label is included in this box. The underbrace notation is schematic for these two differently shaped grouping marks."""),
("B11", r"""$=l_0\sigma_\infty(l_\infty^\alpha l_0)l_\infty^\alpha
=l_0(l_0^{-1}l_{\unsure{1}}^{-1})^\alpha l_1(l_1^{-1}l_0^{-1})^\alpha$""",
"""Complete live equality chain. Every alpha, minus sign, inverse 1, and l index is included. The second index inside the first right-hand parenthesis is heavily retraced but 1 is favoured. No stop is visible at the line end."""),
("B12", r"""$\deleted{=}\underbrace{\deleted{l_{\unsure{0}}\sigma_\infty(l_\infty)}}_{l_0l_\infty.}\deleted{\sigma_\infty(l_\infty)^{\alpha-1}\sigma_\infty(l_{\unsure{0}})l_\infty^\alpha}$""",
"""Large zigzag strike cancels the full upper equality. The under-grouping line below the first l0 sigma-infinity(l-infinity) is comparatively straight; its label l0 l-infinity followed by a point remains individually legible and is not directly crossed. Two l indices intersect the cancelling stroke and retain doubts. The large terminal curved stroke is part of the zigzag, not confidently an extra parenthesis. Bottom edge clips the next raised cancellation."""),
("B13", r"""et la relation $\varepsilon_\infty^2=l_\infty$ \inserted{\deleted{$\unsure{(=)|(\Rightarrow)}l_1^{-1}l_0^{-1}$}} s'écrit ainsi, en multipliant
par $l_0l_1$""",
"""Main prose and the relation are live. A raised expression with two inverse factors is obliquely cancelled above the gap before 's'écrit'; its leading parenthesized equality/arrow-like sign remains uncertain. Lower 'par l0 l1' is included. Top edge contains a clipped earlier bracket label, not repeated here."""),
("B14", r"""\deleted{$l_0l_\infty\underbrace{\sigma_\infty\unsure{(|l(}l_\infty)^{\alpha-1}}_{(l_0^{-1}l_1^{-1})^{\alpha-1}}\underbrace{\sigma_\infty(l_0)}_{l_1}l_\infty^{\alpha-1}=1$}""",
"""Oblique cancelling strokes traverse the upper formula and the left lower annotation. An extra upright trace before the first parenthesis cannot securely be separated from an overwritten l. First grouping is curly, second nearly a square bracket. The lower l1 under the second group is individually unstruck; the outer deleted wrapper represents the surrounding cancelled calculation, not a claimed stroke through that label. All alpha-minus-one powers and inverse signs are copied."""),
("B15", r"""i.e. \deleted{$l_\infty^{-1}l_1$} \deleted{$l_0^{1-\alpha}l_1^{2-\alpha}l_\infty^\alpha=1$}""",
"""The first two factors have an additional horizontal cancellation. Longer oblique strokes continue through the remaining computation from the cancelled block above. The exponent 2-alpha is visibly 2 rather than inferred. All factors and the result 1 are retained; the prefatory i.e. is not crossed."""),
("B16", r"""$l_{\unsure{0}}l_1l_0(l_0^{-1}l_1^{-1})^\alpha l_1(l_1^{-1}l_{\unsure{0|\infty}}^{-1})^\alpha=1$""",
"""Live product. The initial index is dark and compressed; 0 is favoured. The last l index is open and double-curved enough to leave 0 versus infinity unresolved independently. Both alpha powers, four inverse exponents, and result 1 are included. No terminal punctuation is established."""),
("B17", r"""\margin{pour $\alpha\unsure{=|\ge}\unsure{2|1}$ ?}""",
"""Right-margin question. 'pour' has a dark retraced ending. Alpha is angular; the relation sign has a curved upper stroke and straight lower stroke. The numeral is strongly overwritten with a rightward foot, favouring 2 but retaining 1. The separate question mark and its point are plain."""),
("B18", r"""\deleted{$l_0l_1l_0l_{\unsure{0}}^{-1}l_1^{-1}l_0^{-1}l_1^{-1}l_1l_1^{-1}l_0^{-1}l_1^{-1}l_0^{-1}=1$ ? Non !}""",
"""Twelve factors are transcribed before the equals sign. Oblique cancellation strokes pass through the first factors; a long rising horizontal stroke begins around the eighth factor and continues across the later factors, result, question mark, and Non to the far right. Fourth factor's index is partially struck. The terminal exclamation mark is separate. Clipped strokes at the bottom belong to the next product."""),
("B19", r"""\deleted{$l_0l_1l_0l_0^{-1}l_1^{-1}l_1l_1^{-1}l_0^{-1}$}$=1$\quad OK\quad donc""",
"""Eight factors carry individual diagonal cancellation marks. The equals sign, result 1, OK, and final 'donc' are not horizontally cancelled and are therefore kept live. All four inverse exponents are included. The upper edge shows tails of previous diagonal strokes."""),
("B20", r"""$\left\{\begin{aligned}
\varepsilon_\infty&=l_0\sigma_\infty l_\infty\quad\text{(ou encore }\operatorname{int}(l_{\unsure{0}})\sigma_\infty\operatorname{int}(l_{\unsure{\infty|0}})\text{)}\\
\varepsilon_{\unsure{0}}&=l_1\sigma_0l_0\\
\varepsilon_1&=l_\infty\sigma_1l_1
\end{aligned}\right.$""",
"""Three definitions joined by one large left brace. The parenthetical 'ou encore' is followed by two int expressions; the small indices are compressed/overlapping and remain explicitly doubtful. The middle epsilon index is a heavily filled oval, favouring 0 with an earlier layer indeterminate. Main-row factors and their indices are recorded; no final stop is supplied."""),
("B21", r"""\mspage{12}""",
"""Handwritten footer 12. Enlargement is large because the source box is small; both numerals are clear despite scan softness. No adjacent punctuation."""),
]

with (target / "boxes.tsv").open(encoding="utf-8", newline="") as fh:
    expected = list(csv.DictReader(fh, delimiter="\t"))
manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
assert len(rows) == len(expected) == len(manifest) == 21
assert [r[0] for r in rows] == [r["box"] for r in expected] == [r["box"] for r in manifest]
assert not out.exists(), "Never overwrite a submitted reading"
for (box, reading, observations), boxrow, entry in zip(rows, expected, manifest):
    assert reading.strip() and observations.strip()
    assert entry["coords"] == [int(boxrow[k]) for k in ("x0","y0","x1","y1")]
    assert (edition / entry["crop"]).is_file()
    entry["observations"] = observations
    entry["inspected"] = True
with out.open("w", encoding="utf-8", newline="") as fh:
    writer = csv.writer(fh, delimiter="\t", lineterminator="\n")
    writer.writerow(["box", "reading"])
    writer.writerows((box, reading) for box, reading, _ in rows)
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
with out.open(encoding="utf-8", newline="") as fh:
    reread = list(csv.DictReader(fh, delimiter="\t"))
assert [(r["box"], r["reading"]) for r in reread] == [(b, r) for b, r, _ in rows]
assert all(e["inspected"] and e["observations"].strip() for e in manifest)
print("Validated 21 ordered readings and 21 complete crop records; no comparisons performed.")
for path in (out, manifest_path):
    print(f"{path}\nSHA256 {hashlib.sha256(path.read_bytes()).hexdigest()}")

