from pathlib import Path
import csv,json,hashlib

root=Path("/workspace/scratch/937907bd75d7/SP75_C13_145_work")
edition=root/"edition"
packet=root/"audit_packets/145_scan023"
out=edition/"second/145_scan023_second.tsv"
manifest_out=edition/"second/145_scan023_crop_manifest.json"
provisional=edition/"second/145_scan023_crop_manifest.provisional.json"
assert not out.exists() and not manifest_out.exists(), "Do not overwrite a sealed submission"
with (packet/"boxes.tsv").open(encoding="utf-8",newline="") as f:
    boxes=list(csv.DictReader(f,delimiter="\t"))
manifest=json.loads(provisional.read_text(encoding="utf-8"))

readings={
"B01":r"""\unsure{10|20}
Le sous-groupe $E_\tau$ de $E$ image inverse de $\mathbb Z/2$""",
"B02":r""""\unsure{tri-angle|triangle} profini" de \unsure{Malgoire|Melgoire}, ayant comme
\unsure{gén.|gén} $\tau_0,\tau_1,\tau_\infty$
\deleted{\unsure{relat.|relati.}} avec""",
"B03":r"""$(17)\quad\left\{
\begin{aligned}
\deleted{\unsure{\tau_1}\tau_\infty=}\quad l_0
&=\tau_\infty\tau_{\unsure{\deleted{\unsure{\infty|0}}\inserted{1}|1}}\\
\deleted{\tau_\infty\tau_0=}\quad l_1
&=\tau_{\unsure{0|\infty}}\tau_\infty\\
l_\infty&=\tau_1\tau_0
\end{aligned}\right.$""",
"B04":r"""\margin{\uline{NB}\quad
\begin{tikzpicture}[x=1ex,y=1ex,baseline=0ex]
\draw[line width=.45pt] (0,.50)--(1,.65);
\fill (.55,.36) circle (.065);
\end{tikzpicture}}""",
"B05":r"""$E_\tau$ peut être considéré comme le groupe
ayant comme \inserted{gén. les $\tau_i$, avec les} seules relations (16) — on a \unsure{un|une}
hom signature évident $\tau_i\to-1$ de $E_\tau$ dans""",
"B06":r"""$\pm1$, dont le noyau est $\pi$ engendré par les
$l_i$ décrits par (17) ... .""",
"B07":r"""\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
\draw[line width=.5pt] (0,0)--(1.5,.06);
\end{tikzpicture}
\end{center}""",
"B08":r"""\margin{On a les
relations
$\unsure{\rho|\ell}$}""",
"B09":r"""Revenons à une description plus symétrique
des autom. extérieurs à lacets de $E$. On
\unsure{désignera|désigne} par $\widehat E$ le complété profini de $E$,""",
"B10":r"""extension de $\unsure{\widehat{\mathcal T}_{0,3}|\widehat{\Gamma}_{0,3}}
\unsure{=|:}\unsure{\mathcal T_{0,3}|\Gamma_{0,3}}
=\mathfrak S_3\unsure{\times|\ast}\mathbb Z/2$
par $\widehat\pi$,
et par $\widehat{\widehat E}$ le groupe des autom. \deleted{extérieurs}""",
"B11":r"""lacets de $\widehat\pi$, extension de
$\widehat{\widehat\Gamma}=\operatorname{Aut\,ext}_{\mathrm{lac}}(\widehat\pi)$
par $\widehat\pi$""",
"B12":r"""$(18)\quad
1\longrightarrow\widehat\pi
\longrightarrow\widehat{\widehat E}
\longrightarrow
\underset{\substack{\Vert\\\operatorname{Aut\,ext}_{\mathrm{lac}}(\widehat\pi)}}{\widehat{\widehat\Gamma}}
\longrightarrow1$""",
"B13":r"""\mspage{22}""",
}

observations={
"B01":"Header numeral is isolated above the first prose line; first digit is angular and hooked, 10 favoured but 20 retained as a visual alternative. Le sous-groupe has a visible hyphen. Group subscript is tau. Image inverse de Z/2 is read literally without adding omitted punctuation or a copula. The Z has doubled strokes; the final numeral reads 2.",
"B02":"Quoted opening expression is tri-angle/triangle profini; a short horizontal trace between the initial tri-like group and angle-like group may be a written hyphen. Proper-name initial vowel is uncertain a/e, with Malgoire favoured. Both quotation marks, name comma and tau list commas are visible. Gen abbreviation point is uncertain. A short relat.-like word on the following line is crossed horizontally, with live avec to its right; it is not silently expanded to relations.",
"B03":"All three rows of relation (17) and their left brace inspected. The two products before l_0 and l_1, with their following equality signs, are cancelled by a broad zigzag. First cancelled tau body is especially overwritten. First live row's final index has a black 1-like vertical over/next to a lighter loop, possibly an earlier infinity or 0; glyph and correction-state alternatives are explicit. Second live row's first index is a heavy retraced oval, 0 favoured over infinity. Third row is clear l_infinity=tau_1 tau_0. No terminal stop.",
"B04":"Isolated NB has one underline. To its upper right is a short slightly rising horizontal dash and a separate small point below it. The two-stroke graphic is reproduced without assigning a conventional punctuation value.",
"B05":"Three-line passage and interlinear addition inspected. Gen. les tau_i, avec les is above seules relations, with a long curved attachment line; the connector is not an underline. Relation number reads (16). The clause after a long dash reads on a un/une, with the ending uncertain. Hom is unexpanded and has no secure abbreviation point here. Signature has a large g descender sweeping underneath; this is not an underline. Evident is retained in the written masculine form. Tau_i arrow has no visible bar at its tail, hence plain right arrow. A small low speck after initial E_tau is not securely an inscription.",
"B06":"Continuation begins plus/minus 1 and comma. Dont le noyau est pi engendre par les / l_i decrits par (17) is read. Pi has two legs and a curved right foot; represented lowercase locally. After (17), three close dark points are followed by a more distant fourth point; all four are retained rather than normalized to a three-dot ellipsis. Paper fold is not text.",
"B07":"A short isolated divider line, slightly rising to the right, occupies the middle of an otherwise blank interval. Reproduced as a centered graphic, not interpreted as an algebraic minus.",
"B08":"Left marginal note rotated -45 degrees for reading. On a les / relations is clear and has no terminal stop. A separate loop-headed descender stands considerably below/left, rho favoured with cursive ell retained as an alternative; no missing formula is supplied around it. Margin placement and separation are retained in the reading/observation.",
"B09":"Three live prose lines inspected. Autom. remains abbreviated with its point. Exterieurs a lacets de E. On is visible. Final letters of the verb after On are contracted; designera/design e uncertainty is retained as des ignera/designe without grammatical replacement. The E in this line has ONE separate circumflex; its upper curved body stroke is not counted as another hat. Complete profini and final comma after E are visible.",
"B10":"The first group sign has a separate hat and subscript 0,3; its cursive body is calligraphic-T-like, with Gamma retained as a glyph alternative. The following unhatted group sign is similarly cursive. Tiny relation between them has two short marks, equals favoured over colon. Following S_3 has a large looped/fraktur-like body and visible 3. Product sign is cross/star-like and remains uncertain; no algebraic interpretation used to decide it. Z/2 and hat-pi follow. In the next line E has TWO separate circumflexes. Autom. has its point. The final word exterieurs is horizontally struck and retained.",
"B11":"Lacets de hat-pi, extension de double-hat-Gamma=Aut ext_lac(hat-pi), then par hat-pi. Gamma has a straight tall left stem and short rightward top, unlike the cursive group signs in B10. Two hats are distinct. Operator subscript reads lac; parentheses around hat-pi are present. No terminal stop. The clipped descender above and next display's hat tips below are overlap only.",
"B12":"Relation number (18), initial/final 1, four right arrows and all three group symbols inspected. Pi has one hat; E and Gamma have two each. Beneath Gamma stand two short nearly vertical strokes, reproduced as a vertical parallel/equality-like mark above Aut ext_lac(hat-pi). This spatial label is not silently converted to an extra horizontal equation. No terminal punctuation. Top partial par hat-pi repeats B11; black strip below is scan boundary.",
"B13":"Bottom handwritten numeral 22 is complete and unambiguous. No punctuation.",
}

# Clean only observation wording; transcriptions are the independent readings above.
observations["B09"]="Three live prose lines inspected. Autom. remains abbreviated with its point. Extérieurs à lacets de E. On is visible. Final letters of the verb after On are contracted; désignera/désigne uncertainty is retained without grammatical replacement. The E in this line has ONE separate circumflex; its upper curved body stroke is not counted as another hat. Complété profini and final comma after E are visible."

ids=[b["box"] for b in boxes]
assert list(readings)==ids and list(observations)==ids
assert [m["box"] for m in manifest]==ids
for b,m in zip(boxes,manifest):
    assert m["coords"]==[int(b[k]) for k in ("x0","y0","x1","y1")]
    p=edition/m["crop"]
    assert p.is_file()
    m["inspected"]=True
    m["observations"]=observations[b["box"]]
    m["submission_status"]="COMPLETE AND IMMUTABLE"
    m["crop_sha256"]=hashlib.sha256(p.read_bytes()).hexdigest()
    assert readings[b["box"]].strip() and m["observations"].strip()
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
assert len(rows)==len(boxes)==13
assert [r["box"] for r in rows]==ids
assert all(r["reading"]==readings[r["box"]] for r in rows)
saved=json.loads(manifest_out.read_text(encoding="utf-8"))
assert len(saved)==13 and all(m["inspected"] is True for m in saved)
assert len({m["crop"] for m in saved})==13
assert all(m["submission_status"]=="COMPLETE AND IMMUTABLE" for m in saved)
provisional.unlink()
print("COMPLETE AND IMMUTABLE")
print("13 prescribed boxes; 13 nonempty ordered readings; 13 saved, inspected, hashed crops")
for p in (out,manifest_out):
    print(hashlib.sha256(p.read_bytes()).hexdigest(),p)

