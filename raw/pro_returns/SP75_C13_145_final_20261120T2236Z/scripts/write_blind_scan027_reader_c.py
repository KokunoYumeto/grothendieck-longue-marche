from pathlib import Path
import csv,json,hashlib

root=Path("/workspace/scratch/937907bd75d7/SP75_C13_145_work")
edition=root/"edition"
packet=root/"audit_packets/145_scan027"
out=edition/"second/145_scan027_second.tsv"
manifest_out=edition/"second/145_scan027_crop_manifest.json"
provisional=edition/"second/145_scan027_crop_manifest.provisional.json"
assert not out.exists() and not manifest_out.exists(), "No sealed submission may be overwritten"
with (packet/"boxes.tsv").open(encoding="utf-8",newline="") as f:
    boxes=list(csv.DictReader(f,delimiter="\t"))
manifest=json.loads(provisional.read_text(encoding="utf-8"))

readings={
"B01":r"""12""",
"B02":r"""L'extension $E=E_{0,3}$ de
$\Gamma=\Gamma_{0,3}\simeq
\underbrace{\mathfrak S_{\unsure{[0,1,\infty]|\{0,1,\infty\}}}}_{\unsure{\simeq|=}\mathfrak S_3}
\times\mathbb Z/2\mathbb Z$
\margin{engendré par $\tau$:
$z\mapsto\bar z$}
par $\Pi=\Pi_{0,3}
=\{l_0,l_1,l_\infty\mid l_\infty l_1l_0=1\}
=\Pi_1\left(
\underbrace{\mathbb P^1_{\mathbb C}\setminus\{0,1,\infty\}}_{U=\unsure{X_{0,3}|U_{0,3}}},
-\bar{\jmath}\right\}$. """,
"B03":r"""Les classes de conjugaison de scindages partiels
\deleted{au \unsure{dessus} des}""",
"B04":r"""maximaux correspondent aux points fixes de
$\dot\rho,\dot\sigma_0,\dot\sigma_1,\dot\sigma_\infty$
opérant sur $X_{0,3}$, et \inserted{(\unsure{éventuelles})} aux comp.
connexes des ens. d'invariants de""",
"B05":r"""$\unsure{\dot\rho|\rho}^{\deleted{\unsure{2}}}\tau,
\dot\sigma_0\tau,\dot\sigma_1\tau,\dot\sigma_\infty\tau$.
Les p\textsuperscript{ts} fixes de $\rho$
\inserted{\unsure{(}\unsure{savoir|soit} $\varphi(\mathfrak S_3)$)}
sont $P$ et $\bar P$ (dont le stabilisateur est d'ordre $6$,""",
"B06":r"""formé de $1,\dot\rho,\dot\rho^2,\dot\sigma_1\tau,\dot\sigma_2\tau,\dot\sigma_3\tau$.
On a étudié
le relèvement correspondant \inserted{à $P$} (de $\varphi(\mathfrak S_3)$), on trouve
des relèvements ($\Pi$-conjugués \inserted{entre eux}) relatifs à""",
"B07":r"""$\bar P$ s'obtiennent en \deleted{\unsure{conj}} prenant un élément de
$E$ \deleted{\unsure{et|qui}} qui \unsure{soit} en dessus d'un élément de
$\Gamma$ envoyant $P$ en $\bar P$
(savoir $\dot\sigma_0,\dot\sigma_{\unsure{1}},\dot\sigma_\infty,\tau,\tau\rho,\tau\rho^2$)""",
"B08":r"""et en conjuguant par cet élément
on peut donc prendre \deleted{\unsure{$\sigma_0,\tau$}} un des élé-
ments $\sigma_0,\sigma_1,\sigma_\infty$ (ou $\varepsilon_0,\varepsilon_1,\varepsilon_\infty$)
ou $\tau_0,\tau_1,\tau_\infty$ ou""",
"B09":r"""\unsure{les|leurs} produits des précédents par \deleted{\unsure{ou|un}}
$\rho$ ou $\rho^2$... .""",
"B10":r"""Le\deleted{\unsure{s}} \inserted{seul}
p\textsuperscript{\unsure{t\deleted{s}|t}} fixe de $\sigma_0$ est $2$, dont le
stabilisateur est le groupe $\simeq\mathbb Z/2\times\mathbb Z/2$ engendré
par $\sigma_0$ et $\tau$. On a un relèvement de ce sous-groupe""",
"B11":r"""\mspage{26}""",
}

observations={
"B01":"Top handwritten numeral 12 is clear. No punctuation.",
"B02":"Both full display lines and their annotations inspected. E and Gamma have literal subscripts 0,3. Before the permutation-group symbol, the relation has a wavy upper and straight lower stroke, represented simeq. Its set-like index has a heavy straight right end; square brackets versus braces remain uncertain. A lower brace labels the same group with S_3; the tiny preceding relation mark is uncertain simeq/equals. Right annotation reads engendre par tau: z maps-to bar-z, with a visible tail bar on the arrow. All three Pi signs have tall two-leg forms, locally represented capital Pi. Presentation has l_0,l_1,l_infinity and product l_infinity l_1 l_0=1. Projective-line source and set entries are complete. Under-source label begins U=; its next capital is retraced, X_0,3 favoured over U_0,3. Base point has a separate minus and a bar above a j-shaped descender. Final delimiter is visibly brace-like despite an opening round parenthesis; preserved as such. Final stop is visible.",
"B03":"Live line Les classes de conjugaison de scindages partiels. Below conjugaison is a separately placed au dessus des-like phrase crossed by a long rising stroke; dessus remains uncertain under the crossing. No hyphen was supplied within au dessus. The long g descender belongs to conjugaison and intersects the deletion.",
"B04":"All prose and four dotted generators inspected. Dots above rho and all three sigmas are separate. Commas follow rho, sigma_0 and sigma_1; no comma supplied after sigma_infinity. X_0,3 and following comma are clear. The interlinear parenthetic word favours eventuelles, with two l ascenders. Its long curved attachment starts near et / aux comp.; the reading places it at that insertion site, while exact syntactic attachment remains uncertain. Comp. and ens. keep their abbreviation points. D'invariants is read literally.",
"B05":"First rho head is dark/retraced and its dot cannot be separated securely; dot-rho/rho alternatives remain. A small raised 2-like mark above/right is crossed/retraced and retained as a doubtful cancelled exponent. The three following dot-sigma tau products and their indices 0,1,infinity are clear. Final list stop is visible. Pts has raised ts. Main upper-right word favours sont. A lower annotation with a broad connector/bracket contains savoir/soit and phi(S_3); its initial outer opening parenthesis is uncertain, while the final closing curve is visible. P and bar-P are distinct. The following dont parenthesis opens visibly; no closing mate is supplied before the comma after 6.",
"B06":"All six members of the stabilizer list read. The written sigma indices are 1,2,3, not changed to 0,1,infinity. Dots above both rhos and all sigmas are distinct, and rho squared has a visible 2. There is a stop after the list and no secure closing parenthesis there for the earlier dont passage. A P with an accented a-like word is interlinear and connected after correspondant; rendered inserted a P. Phi(S_3) has the surrounding prose parenthesis and comma. Entre eux is inserted above the end of Pi-conjugues before its closing parenthesis. Long j/g/f descenders are not underlines.",
"B07":"Three-line continuation read. Bar-P is explicit. Conj-like abandoned word after en is horizontally struck; no certain abbreviation point. Another compact crossed word between E and qui is uncertain et/qui. Soit-like word is faint/retraced but lacks a distinct full deletion stroke, so is retained live and uncertain. En dessus is kept as written. Gamma has a single tall left leg. P en bar-P is visible. Parenthetic savoir list has three dotted sigmas, followed by bare tau, tau-rho and tau-rho squared. Middle sigma index is blackened, 1 favoured but marked uncertain. No final stop.",
"B08":"Live prose et en conjuguant par cet element / on peut donc prendre. Small deleted formula-like cluster after prendre favours sigma_0,tau; cancellation obscures both heads. Un des ele- / ments has a visible line-end hyphen, preserved rather than silently joining. Subsequent sigma list is undotted, unlike earlier dotted list. Parenthetic epsilon list and following tau list have literal indices 0,1,infinity and visible commas. Final ou continues into B09.",
"B09":"First short word has a heavily retraced ending, les/leurs retained. Produits des precedents par is read. A short crossed ou/un-like word occurs before the live rho. Rho ou rho squared follows; exponent 2 is clear. Three close points are followed by a separated final point; preserved as three-dot ellipsis plus another stop rather than reduced.",
"B10":"Final paragraph complete. Seul is interlinear above the article/point abbreviation. Article ending is blackened and is represented as a doubtful cancelled s after Le. Superscript abbreviation has a retraced t/s-like mass, with t plus cancelled s versus t alternatives; no clean plural s is asserted. Fixe de sigma_0 est 2, dont le / stabilisateur est le groupe is visible. Sigma_0 is undotted. Both quotient denominators read 2 and multiplication is a cross; relation before them has wavy upper and straight lower stroke. Engendre continues into par sigma_0 et tau. with a visible stop. Last sentence ends with de ce sous-groupe at the right edge; no final stop is supplied.",
"B11":"Bottom handwritten numeral 26 is clear, without punctuation.",
}

ids=[b["box"] for b in boxes]
assert list(readings)==ids and list(observations)==ids
assert [m["box"] for m in manifest]==ids
for b,m in zip(boxes,manifest):
    assert m["coords"]==[int(b[k]) for k in ("x0","y0","x1","y1")]
    assert m["rotation_degrees"]==0
    p=edition/m["crop"]
    assert p.is_file()
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
assert len(rows)==len(boxes)==11
assert [r["box"] for r in rows]==ids
assert all(r["reading"]==readings[r["box"]] for r in rows)
saved=json.loads(manifest_out.read_text(encoding="utf-8"))
assert len(saved)==11
assert all(m["inspected"] is True and m["submission_status"]=="COMPLETE AND IMMUTABLE" for m in saved)
assert len({m["crop"] for m in saved})==11
provisional.unlink()
print("COMPLETE AND IMMUTABLE")
print("11 prescribed boxes; 11 ordered nonempty readings; 11 original saved, inspected and hashed crops")
for p in (out,manifest_out):
    print(hashlib.sha256(p.read_bytes()).hexdigest(),p)

