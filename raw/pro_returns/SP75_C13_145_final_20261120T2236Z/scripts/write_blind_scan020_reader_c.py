from pathlib import Path
import csv, json, hashlib

root = Path("/workspace/scratch/937907bd75d7/SP75_C13_145_work")
edition = root / "edition"
packet = root / "audit_packets/145_scan020"
out = edition / "second/145_scan020_second.tsv"
manifest_out = edition / "second/145_scan020_crop_manifest.json"
provisional = edition / "second/145_scan020_crop_manifest.provisional.json"
assert not out.exists(), "Do not overwrite an existing submission"
assert not manifest_out.exists(), "Do not overwrite an existing manifest"
with (packet / "boxes.tsv").open(encoding="utf-8", newline="") as f:
    boxes = list(csv.DictReader(f, delimiter="\t"))
manifest = json.loads(provisional.read_text(encoding="utf-8"))

readings = {
"B01": r"""8""",
"B02": r"""Il revient au $=$ de dire que $\sigma_0,\sigma_1,\sigma_\infty,\rho$ sont des
générateurs, avec relations de définition""",
"B03": r"""$(4)\quad
(\overbrace{\rho^{-1}\sigma_\infty\sigma_0\deleted{\unsure{\rho}}}^{l_\infty})
(\overbrace{\rho^{-1}\sigma_1\sigma_\infty\deleted{\unsure{\rho}}}^{l_1})
(\overbrace{\rho^{-1}\sigma_0\sigma_1\deleted{\unsure{\rho}}}^{l_0})
=1$""",
"B04": r"""$(5)\quad \sigma_0^2=\sigma_1^2=\sigma_\infty^2=1$""",
"B05": r"""$(6)\quad \rho^3=1$""",
"B06": r"""\margin{Il faut
ajouter les relations
$\rho\sigma_0\rho^{-1}=\sigma_1$ \unsure{etc}
On a deux gén.
$\sigma_0,\rho$ en fait
avec relations
$\sigma_0^2=\rho^3=1$, la}""",
"B07": r"""\margin{avec relations $\sigma_0^2=\rho^3=1$, la
\deleted{$[\rho^{-1}\sigma_0\rho\sigma_0\rho^{-1}
\rho\sigma_0\rho^{-1}\rho\sigma_0\unsure{\rho\sigma_0|\rho}\rho^{-1}]$}
$\underbrace{\qquad}_{\sigma_\infty}\quad
\underbrace{\qquad}_{\sigma_1}\quad
\underbrace{\qquad}_{\sigma_\infty}$
relation (4) \unsure{est}}""",
"B08": r"""\margin{relation (4) \unsure{est}
\unsure{conséquence|conséquences} des
\unsure{relations|par définition}
en fait
$\unsure{(}\sigma_1=\rho\sigma_0\unsure{\rho^{-1}},
\ \sigma_\infty=\rho^{-1}\sigma_0\rho)$. Noter}""",
"B09": r"""\margin{$\sigma_\infty=\rho^{-1}\sigma_0\rho)$. Noter
que
$l_0=\deleted{\unsure{(\sigma_0\rho)^2}}
\rho^{-1}(\sigma_0\rho)^2\rho
=\boxed{\rho^{-1}\sigma_0\rho\sigma_0\rho^{\unsure{-1}}}$}""",
"B10": r"""\margin{$l_1=(\deleted{\unsure{\rho}}\sigma_0\rho)^2$
$l_\infty=(\rho^{\unsure{-1}}\sigma_0\deleted{\unsure{\rho}})^2$}""",
"B11": r"""\margin{$\operatorname{int}(\sigma_0)l_1=l_\infty$
$\operatorname{int}(\sigma_0)l_\infty=l_1$
$\operatorname{int}(\sigma_0)(l_0)=l_\infty^{-1}l_1^{-1}$}""",
"B12": r"""\margin{\uline{NB}
$\sigma_0(l_0)=l_{\unsure{\infty|0}}^{-1}l_1^{-1}$
$\sigma_0(l_1)=l_\infty$
$\sigma_0(l_\infty)=l_1^{\deleted{\unsure{-1}}}
\deleted{\unsure{l_\infty^{-1}|l_0^{-1}}}$
et idem pour $\sigma_1,\sigma_\infty$}""",
"B13": r"""\uline{NB} Si on y fait \inserted{de plus} $\sigma_0,\sigma_1,\sigma_\infty=1$, on trouve \unsure{comme}
relation de définition $\rho^3=1$ \deleted{\illegible{1}} sans plus, ce qui prouve
que $\rho$ n'est pas un mot \unsure{p.r.} aux $\sigma_i$...""",
"B14": r"""\deleted{\unsure{évident}, \unsure{et alors|alors} ces dernières \unsure{restent|seraient} \unsure{les} \unsure{plus|primés}
\unsure{primés}, de \unsure{gén.} \unsure{indépendts|correspondts}
$l'_i=l_i^{-1},\ \sigma'_i=\unsure{\sigma_i}$\unsure{,|)}}""",
"B15": r"""\inserted{\deleted{\unsure{i.e.} $\sigma_{\unsure{i}}$}}
\deleted{de sorte que $\sigma^{\unsure{\prime|1}}$}""",
"B16": r"""si on y remplace les $l_i$ par les $l_i^{-1}$""",
"B17": r"""Ici on a, comme $\sigma_i=\sigma^{\unsure{\prime|1}}_{\rho^{-1}(i)}$""",
"B18": r"""$(7)\quad\left\{
\begin{aligned}
\operatorname{int}(\sigma_i):\ &\text{échange }l_j\text{ et }l_{\unsure{k|h}}\\
\operatorname{int}(\rho)l_i&=l_{\dot{\rho}(i)}
\end{aligned}\right.$
\inserted{$(i,j,\unsure{k|h})$ distincts)\ \unsure{et}}
\deleted{(et \unsure{la valeur de|les ordres de} $l_{\unsure{i|\rho^{-1}(i)}}$ \unsure{s'en}
déduit par (1))}""",
"B19": r"""On voudrait maintenant expliciter les $\varepsilon_i$
avec $\varepsilon_i^2=l_i\quad(i=0,1,\infty)$, $\varepsilon_i$ étant \unsure{donc un|des}
\unsure{générateur|générateurs} \unsure{du|des} \unsure{centralisateur|centralisateurs} (ou \unsure{normalisateur|normalisateurs}, c'est
idem) des $l_i$ dans $E^+$\unsure{.|,} (ou \unsure{le|les} \unsure{centralisateur|centralisateurs} dans
$E$). Les calculs faits plus haut, avec les""",
"B20": r"""chgts de notations indiqués, donnent""",
"B21": r"""$\unsure{\deleted{(8)}|(8)}\quad\left\{
\begin{aligned}
\unsure{\deleted{\varepsilon_0}|\varepsilon_0}
&=l_0^{\unsure{\deleted{\unsure{-1|4}}|\unsure{-1|4}}}\sigma_1
l_{\unsure{0}}^{\unsure{\deleted{\unsure{-1|4}}|\unsure{-1|4}}}\\
\unsure{\deleted{\varepsilon_1}|\varepsilon_1}
&=\unsure{\deleted{l_\infty^{-1}}|l_\infty^{-1}}\sigma_\infty
\deleted{\unsure{l_1^{-1}}}\inserted{l_1}\\
\varepsilon_\infty&=l_0^{-1}\sigma_0l_\infty
\end{aligned}\right.$""",
"B22": r"""\mspage{19}""",
}

observations = {
"B01": "Top handwritten 8, complete and without punctuation. Black scan border is not an inscription.",
"B02": "Two lines independently read. Initial Il is supported by the same local form in the margin's Il faut, not by any external text. The two short horizontal strokes after au are retained literally as an equals sign. Four undotted Greek letters have their visible indices. No final stop is securely established.",
"B03": "Relation (4), all three factors, three overbraces and labels, and final =1 were inspected. Each leading rho inverse is live and clear. Three terminal rho-like signs are separately scribble-cancelled; obscured heads remain doubtful. Upper labels read l_infinity, l_1, l_0. Overbrace spans in the reading are schematic: first and second left ends begin to the right of the leading rho heads, approximately above the following sigma, while the third starts near the leading inverse exponent. Their exact algebraic inclusion is visually imprecise. No terminal stop.",
"B04": "Relation (5), all three squared sigmas, all equality signs and final 1 read. Indices 0,1,infinity and exponents 2 are visible. A tiny grey speck near the first equality is not promoted to punctuation. No dots over the sigma heads.",
"B05": "Relation (6), rho cubed equals 1. Superscript has a two-lobed/upcurving 3 shape, not a repaired 2. No final punctuation.",
"B06": "Left margin rotated -45 degrees. Il faut / ajouter les relations and the conjugation formula read. Compact word after sigma_1 is tentatively etc; its terminal stop is not established. On a deux gen. has its visible abbreviation point; sigma_0,rho en fait and the square/cube relation follow. The following cancelled long product is clipped at this box edge and is transcribed in B07. Main-body fragments at the rotated right edge are incidental.",
"B07": "Left margin rotated -45 degrees. The square-bracketed product is covered by a long zigzag cancellation. Several rho heads, the crowded right sequence, and exact group boundaries remain uncertain. Reading preserves the observed factor sequence with a local alternative rather than algebraic completion. Three lower grouping marks and labels sigma_infinity, sigma_1, sigma_infinity remain visible; the three empty underbraces reproduce their separate position schematically and do not assert exact spans. The next prose reaches relation (4) est; further words are clipped/overlapped and continued independently in B08.",
"B08": "Left margin rotated -45 degrees. Dense prose crosses crop boundaries. Consequence/consequences, the next relations/par definition group, and the opening parenthesis remain uncertain. En fait is visible. The first definition's final inverse is near the right edge; the second sigma_infinity=rho^{-1} sigma_0 rho and closing parenthesis/point are more legible. Noter begins the subsequent passage. The crossed product at top and the next derivation below are overlap with B07/B09; no unseen connecting prose is supplied.",
"B09": "Left margin rotated -45 degrees. Upper overlap preserves the end of the preceding definition and Noter que. Initial (sigma_0 rho)^2 is cancelled and partly obscured. The live rho^{-1}(sigma_0 rho)^2 rho follows. Rounded rectangular enclosure surrounds the final product; its last inverse exponent is small and crowded by the outline. Following separate l_1 and l_infinity rows are clipped here and transcribed in B10. Large loop and prose at the differently oriented right edge belong to main body, not a marginal label.",
"B10": "Left margin rotated -45 degrees. Two separate rows read. First row has a cancelled initial rho inside parentheses; second row has a cancelled terminal rho. Both obscured heads remain doubtful. Second row's initial inverse exponent is jagged/retraced, with -1 favoured. Both outer powers 2 are visible. Prior and following formulas are incidental clipped overlaps handled in B09/B11.",
"B11": "Left margin rotated -45 degrees. All three conjugation rows complete. The first two l arguments are bare; the third l_0 is explicitly parenthesized. Both final inverse exponents are visible. No row-end punctuation and no dots over sigma heads.",
"B12": "Right margin rotated -20 degrees. NB has one underline. First RHS initial l subscript is tangled/retraced, infinity favoured over 0. Third RHS preserves a possibly cancelled -1 on l_1 and a subsequent crossed factor whose subscript is uncertain infinity/0. Cancellation attachment is less secure than the live l_1 body. Et idem pour sigma_1,sigma_infinity has no established final stop. Main-body fragment at top left is incidental.",
"B13": "Three-line NB paragraph. NB is singly underlined. De plus is interlinear with a curved guide before the sigma list. End of first line comme is faint/contracted. A short cancelled word after rho^3=1 cannot be read securely from its overlapping loops and strike. Third line reads n'est pas un mot; abbreviation p.r. remains doubtful. Three separated terminal dots follow sigma_i. The far upper-right angled traces belong to the overlapping margin note, not a continuation of the prose. The view attempt before context compaction yielded only a truncated-output message; this saved crop was actually inspected on the subsequent successful display, without recropping.",
"B14": "Two lines are crossed by long almost horizontal strokes. Lexical alternatives are retained for the weak/crossed prose, including the first clipped-left word, verbal group and abbreviated words before the formulas. These candidate words are not normalized into a grammatical sentence. The displayed l'_i=l_i^{-1} and sigma'_i=... are visible; the last sigma/index is heavily retraced and the closing comma/parenthesis is uncertain. Cancellation covers both prose lines and formulas.",
"B15": "Upper short line and lower de sorte que line are separately cancelled. Upper line reads i.e. tentatively and sigma_i; it is physically interlinear but its exact insertion attachment is uncertain. Lower final raised vertical stroke can be a prime or 1, so both are retained. Zigzag cancellation obscures portions of sorte; the transcription is a local reading, not supplied from context.",
"B16": "Live phrase si on y remplace les l_i par les l_i^{-1}, with no terminal stop. Both l indices and final inverse are visible. Lower formula fragments are clipped overlap, covered in B17.",
"B17": "Ici on a, comme and the full sigma formula inspected. RHS subscript contains rho^{-1}(i) with parentheses around i. The raised mark on the RHS sigma is a short almost upright prime/1-shaped stroke, left uncertain. No terminal stop. Surrounding partial cancelled text and the left marginal bracket fragment are incidental.",
"B18": "Relation (7) has a two-row brace. First row int(sigma_i): echange l_j et l_k/h; final l index is retraced. Above it is inserted (i,j,k/h) distincts) plus a compact et-like trace; written closing-parenthesis structure is preserved without balancing it. The crossed parenthesis has uncertain wording and l subscript, then clearer deduit par (1)). Second row int(rho)l_i=l_{dot-rho(i)}: a separate dark dot stands above the RHS rho head; parentheses around i are visible. Top edge overlaps B17.",
"B19": "Five-line live paragraph, including epsilon_i^2=l_i and index list i=0,1,infinity. The small words after etant and singular/plural endings in generateur, centralisateur and normalisateur are faint/contracted and retained as alternatives. No grammatical harmonization. Dark mark after E^+ could be period or comma. Final E). and Les calculs faits plus haut, avec les are visible; sentence continues into B20.",
"B20": "Abbreviated chgts retained without expansion or a supplied abbreviation point. De notations indiques, donnent is visible, with the comma after indiques. Formula fragments at the lower edge belong to B21.",
"B21": "Bottom three-row display reaches the physical page edge. Label resembles (8) and is crossed by long diagonal strokes. Additional long diagonals cross the first two epsilon heads and first l of row two; whether these cancel individual items or a larger part of the display remains uncertain, and local state alternatives are explicit. Two tiny top-row exponents have dark angular 4-like masses compatible with cancelled -1, but glyph and state remain uncertain. Top RHS indices read 0, second retraced. Row two final l_1^{-1} is crossed; a larger l_1 is placed lower/right as replacement, though guide versus deletion strokes are entangled. Last row epsilon_infinity=l_0^{-1}sigma_0l_infinity remains live and legible. No final punctuation. Black strip is scan boundary.",
"B22": "Bottom handwritten page numeral 19. The first digit has a retraced/sloping entry, second has an upper loop and curved descending 9 stroke. No punctuation.",
}

ids = [b["box"] for b in boxes]
assert list(readings) == ids and list(observations) == ids
assert [m["box"] for m in manifest] == ids
for b, m in zip(boxes, manifest):
    expected = [int(b[k]) for k in ("x0", "y0", "x1", "y1")]
    assert m["coords"] == expected
    crop = edition / m["crop"]
    assert crop.is_file()
    m["inspected"] = True
    m["observations"] = observations[b["box"]]
    m["submission_status"] = "COMPLETE AND IMMUTABLE"
    m["crop_sha256"] = hashlib.sha256(crop.read_bytes()).hexdigest()
    assert readings[b["box"]].strip() and m["observations"].strip()

with out.open("x", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["box", "reading"], delimiter="\t", lineterminator="\n")
    w.writeheader()
    for box in ids:
        w.writerow({"box": box, "reading": readings[box]})
manifest_out.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

with out.open(encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f, delimiter="\t")
    assert reader.fieldnames == ["box", "reading"]
    rows = list(reader)
assert len(rows) == len(boxes) == 22
assert [r["box"] for r in rows] == ids
assert all(r["reading"] == readings[r["box"]] for r in rows)
loaded = json.loads(manifest_out.read_text(encoding="utf-8"))
assert len(loaded) == 22 and all(m["inspected"] is True for m in loaded)
assert all(m["submission_status"] == "COMPLETE AND IMMUTABLE" for m in loaded)
assert len({m["crop"] for m in loaded}) == 22
provisional.unlink()
print("COMPLETE AND IMMUTABLE")
print("22 boxes; 22 nonempty readings; 22 saved, inspected, hashed crops")
for path in (out, manifest_out):
    print(hashlib.sha256(path.read_bytes()).hexdigest(), path)

