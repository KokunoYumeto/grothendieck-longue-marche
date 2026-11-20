from pathlib import Path
import csv,json,hashlib

root=Path("/workspace/scratch/937907bd75d7/SP75_C13_145_work")
edition=root/"edition"
packet=root/"audit_packets/145_scan026"
out=edition/"second/145_scan026_second.tsv"
manifest_out=edition/"second/145_scan026_crop_manifest.json"
provisional=edition/"second/145_scan026_crop_manifest.provisional.json"
assert not out.exists() and not manifest_out.exists(), "Never overwrite a sealed submission"
with (packet/"boxes.tsv").open(encoding="utf-8",newline="") as f:
    boxes=list(csv.DictReader(f,delimiter="\t"))
manifest=json.loads(provisional.read_text(encoding="utf-8"))

readings={
"B01":r"""en associant à
$\bigl(g,(\unsure{\alpha^i|\alpha_i|\alpha'})_{i\in\{0,1,\infty\}}\bigr)$
le système""",
"B02":r"""\deleted{\unsure{de|des}}
$p=1,\quad(g_i)=
\deleted{(\unsure{l_i^{\alpha_i}})(\unsure{l_i^{\alpha_i}g})}
(gl_i^{\alpha_i})$""",
"B03":r"""\unsure{Il} faudrait expliciter les opérations
des éléments $\sigma_i$ ou $\varepsilon_i$
\deleted{\unsure{sur}}
$\bigl(\in S\overset{\unsure{\sim|\deleted{\sim}|\infty}}{\widehat{\widehat E}}^{!}\bigr)$
\unsure{sur}
$\unsure{\deleted{\widetilde u}|\widetilde u|E}\ \widetilde u
\in S\overset{\unsure{\sim|\deleted{\sim}|\infty}}{\widehat{\widehat E}}^{!}$,""",
"B04":r"""\deleted{\unsure{par la|de la}} conjugaison, et en particulier
\unsure{l'on|les} \unsure{trouve|termes} que \deleted{\unsure{(bien sûr)}}""",
"B05":r"""\unsure{les} $\gamma_i$ sont "covariants" par $\rho$, i.e.""",
"B06":r"""$\gamma_i(\rho\widetilde u\rho^{-1})
=\gamma_{i+1}\unsure{\bar u|\widetilde u})$
\deleted{\unsure{ici|où} $\widehat u$ est défini par}""",
"B07":r"""\margin{\uline{NB} Il y a lieu
d'introduire un
groupe $S\widehat E$ extension
de $E$ par $\unsure{\widehat{\mathbb Z}|\mathbb Z}^{\{0,1,\infty\}}$
(\unsure{déduite} d'une extension
canonique de
$\mathbb Z^{\{0,1,\infty\}}$) et d'étudier les
\begin{tikzpicture}[x=1ex,y=1ex,baseline=0ex]
\draw[line width=.8pt] (1.3,.25)--(0,0)--(1.1,-.18);
\draw[line width=.6pt] (.95,.4)--(.55,-.25);
\draw[line width=.6pt] (.15,.08)--(1.45,-.04);
\end{tikzpicture}
relèvements des
$\sigma_i,\rho$ et \unsure{ceux|cas} des
$\unsure{\operatorname{int}(l_i),\rho|\operatorname{int}(\sigma_i),\rho}$
....}""",
"B08":r"""\mspage{25}""",
}

observations={
"B01":"One live line. En associant a and le systeme are read. Outer tuple has g, a parenthesized alpha expression, the index i in {0,1,infinity}, and a final outer closing parenthesis. Short stroke after alpha is visibly raised; whether it is a raised i, an unusually high subscript i, or a prime is uncertain and not normalized. Both set braces and all three entries are preserved. No terminal stop established.",
"B02":"Crossed short word before p=1 is de/des-like. P has a descender and rounded right shoulder. The g_i tuple and equality precede two separately parenthesized, heavily hatched cancelled factors. Their proposed l_i/alpha/g readings remain uncertain at whole-factor scope; the hatching prevents a secure reconstruction of all internal strokes. The final uncancelled factor reads (g l_i^{alpha_i}), with i on l and a small i-like stroke following exponent alpha. No punctuation supplied at the end.",
"B03":"Two main-text lines intersect the angled marginal note. Possible initial Il is inseparable from marginal lettering and is explicitly uncertain. Faudrait expliciter les operations / des elements sigma_i ou epsilon_i is read. The short word before the opening parenthesis is crossed and sur-like. Inside the parentheses, S and E are followed by a raised exclamation-like pair; E has two separate circumflexes and an additional dark wavy/looped upper mass. Its tilde, cancelled-tilde or infinity-like reading remains uncertain. The same upper-mark issue recurs in the right-hand group. Following sur-like text, a dark retraced cluster precedes the clearer tilde-u; the cluster's glyph and deletion state are not settled. Final comma is a separate large curved stroke. No mathematical simplification used.",
"B04":"Main-text conjugaison, et en particulier is visible, with a short horizontal cancellation over a preceding two-word par la/de la-like phrase. Angled marginal ink runs through this area and is handled separately in B07. Next line favours l'on trouve que; les termes is retained as a local alternative because the contracted letter bodies overlap. The final horizontally struck parenthetic group favours (bien sur), with a raised accent over its u-like ending and a visible right parenthesis. It remains doubtful beneath the strike.",
"B05":"Gamma_i has an i dot and stem, not an additional prime. Sont and quoted covariants are read; both quotation groups remain. Par rho has a following comma. Final i.e. has small detached interletter/terminal marks, retained as written abbreviation punctuation. Initial les-like group overlaps angled marginal writing, so its attachment/readability is uncertain.",
"B06":"Complete displayed equality inspected. Left side is gamma_i(rho tilde-u rho^{-1}); inverse -1 and closing parenthesis are clear. RHS index reads i+1. The short upper mark on RHS u is flatter than the left tilde, bar/tilde alternatives retained. No separate opening parenthesis before RHS u is securely visible; the written closing parenthesis is preserved without adding its mate. In the lower line a long ascending stroke cancels the entire phrase; initial ici/ou-like segment is obscured, while hat-u est defini par is more legible. The lower u has a distinct chevron. No final punctuation established.",
"B07":"Entire prescribed marginal region viewed at -35 degrees. NB is singly underlined. Il y a lieu / d'introduire un / groupe S-hat-E extension / de E par the integer-set expression are read. Margin E has one separate hat, distinct from the double hats in the body. A compact upper trace on the first Z could be a hat or incidental dot; uncertainty retained. Both exponent sets contain literal 0,1,infinity in braces. The parenthetic prose favours deduite d'une extension canonique de; deduite remains uncertain. Et d'etudier les / relevements des is read. Final line begins sigma_i,rho et and continues with a contracted ceux/cas-like group, des, and an overlapping mathematical/operator-like expression; the int(l_i)/int(sigma_i),rho readings are tentative at full-expression scope. Four separate dark dots follow on a new lower line. An isolated black intersecting-stroke cluster near the middle is reproduced graphically without assigning it an arrow or cancellation function. Differently sloping main-body words/formula fragments are overlap with B03-B06, not additional margin sentences.",
"B08":"Footer handwritten 25, complete and clear. No punctuation.",
}

ids=[b["box"] for b in boxes]
assert list(readings)==ids and list(observations)==ids
assert [m["box"] for m in manifest]==ids
for b,m in zip(boxes,manifest):
    assert m["coords"]==[int(b[k]) for k in ("x0","y0","x1","y1")]
    p=edition/m["crop"]
    assert p.is_file()
    assert m["rotation_degrees"]==(-35 if b["box"]=="B07" else 0)
    assert readings[b["box"]].strip() and observations[b["box"]].strip()
    m["inspected"]=True
    m["observations"]=observations[b["box"]]
    m["crop_sha256"]=hashlib.sha256(p.read_bytes()).hexdigest()
    m["submission_status"]="COMPLETE AND IMMUTABLE"
with out.open("x",encoding="utf-8",newline="") as f:
    w=csv.DictWriter(f,fieldnames=["box","reading"],delimiter="\t",lineterminator="\n")
    w.writeheader()
    for box in ids:
        w.writerow({"box":box,"reading":readings[box]})
manifest_out.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
with out.open(encoding="utf-8",newline="") as f:
    r=csv.DictReader(f,delimiter="\t")
    assert r.fieldnames==["box","reading"]
    rows=list(r)
assert len(rows)==len(boxes)==8
assert [r["box"] for r in rows]==ids
assert all(r["reading"]==readings[r["box"]] for r in rows)
saved=json.loads(manifest_out.read_text(encoding="utf-8"))
assert len(saved)==8
assert all(m["inspected"] is True and m["submission_status"]=="COMPLETE AND IMMUTABLE" for m in saved)
assert len({m["crop"] for m in saved})==8
provisional.unlink()
print("COMPLETE AND IMMUTABLE")
print("8 prescribed boxes; 8 ordered nonempty readings; 8 original saved, inspected and hashed crops")
for p in (out,manifest_out):
    print(hashlib.sha256(p.read_bytes()).hexdigest(),p)

