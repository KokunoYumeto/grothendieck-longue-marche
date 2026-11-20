from pathlib import Path
import csv,json,hashlib

root=Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work')
edition=root/'edition'
rows=[
('B01',r"""choisi — si on \deleted{\unsure{multiplie}} remplace $g$ par $\operatorname{int}(\lambda)u$
avec $\lambda=l_0^\alpha\in L_0$ $(\alpha\in\hat Z^{\unsure{*|\times}})$, alors $g$ est""",
"""Two complete lines beginning with the continuation choisi. The long horizontal cancellation covers multiplie; medial and terminal overlap leaves that cancelled word doubtful. The next word reads remplace. The first symbol after it has a descending g outline; the final symbol after int(lambda) has a short u-like outline and no comparable descender. The raised mark beside the hatted Z is angular and remains star versus cross. The lower edge touches the final g descender. No unseen continuation is supplied."""),
('B02',r"""$\lambda g\rho(\lambda)^{-1}=\underline{l_0^\alpha g l_1^{-\alpha}}$.""",
"""Complete equation, including the live raised -1, both alpha exponents, the two numerical subscripts, and the terminal stop. One continuous underline lies beneath the right-hand product. The first right-hand l stem is retraced but its loop and index remain legible."""),
('B03',r"""\deleted{\unsure{la|les}} les relations""",
"""The first short word is heavily overwritten/cancelled, with a tall loop and baseline cluster; la and les remain possible. The following les relations is live and clear. No punctuation follows within this box."""),
('B04',r"""les relations $(*)$ et $(**)$ déterminent $u$ en termes
$p\in\hat Z^{\unsure{*|\times}}$ et de $g\in\unsure{\Pi}$, par""",
"""The two relation labels contain one and two star-like crosses, respectively, in parentheses. The mathematical group sign after g is a compact capped form without an established separate hat; its legs are crowded, so Pi remains marked doubtful. The raised angular mark on Z remains star/cross. The lower line begins at p in this crop: its preceding word is outside the left boundary and is not supplied. The lower edge clips the ends of descenders."""),
('B05',r"""\[
\left\{\begin{aligned}
u(l_0)&=l_0^p\\
u(l_1)&=u\rho(l_0)=\operatorname{int}(g)\rho\underbrace{u(l_0)}_{l_0^p}=\operatorname{int}(g)l_1^p
\end{aligned}\right.
\]""",
"""The first two complete rows of a larger brace display. The left brace continues below the crop. The underbrace in the second row covers u(l_0), with l_0^p written below. All visible exponents p and indices 0/1 are included; no product dots or terminal punctuation are supplied. A fragment of the next row is clipped at the bottom."""),
('B06',r"""\[
u(l_\infty)=u\rho(l_1)
=\operatorname{int}(g)\rho\underbrace{u(l_1)}_{\operatorname{int}(g)l_1^p}
=\operatorname{int}(g)\underbrace{\rho\operatorname{int}(g)\rho^{-1}}_{\operatorname{int}(\rho(g))}
\underbrace{(\rho l_1^p)}_{l_\infty^p}
=\deleted{\unsure{\operatorname{int}(g\rho(g))l_\infty}}
\]
\inserted{$\operatorname{int}(g\rho(g))l_\infty^p$}""",
"""Complete third row with three lower underbrace annotations. The first brace covers u(l_1); the second covers rho int(g) rho^{-1}; the third covers the parenthesized rho l_1^p. The terminal baseline term is crossed through and reaches the physical right edge: its crowded argument and last l/index remain doubtful, and no unseen terminal exponent is supplied. A live alternative int(g rho(g)) l_infty^p sits above it, with a broad curved guide at its left and a bent guide below/right; these are represented as an insertion, without forcing an extra lexical parenthesis from the guide. The top edge clips the preceding formula row, which is not duplicated as a complete passage."""),
('B07',r"""\margin{\uline{NB} On voit que $u_{\unsure{g}}$ \unsure{automatiquement|automatique} respecte la structure \unsure{à|en} lacets avec le multiplicateur $p$}""",
"""Rotated -25 degrees. NB is singly underlined, without supplied abbreviation stops. A small dark looped form below u is retained as a doubtful subscript g. The long word after u has the body automatique..., but its ending is compressed and remains automatiquement/automatique. The tiny preposition before lacets is uncertain. No est is supplied between u and the following word, and no final stop is established after p. Main-text fragments at the lower edge are incidental and clipped."""),
('B08',r"""Il faut vérifier, pour qu'on ait bien un endom.
de $\Pi$, \uline{la relation $l'_0l'_1l'_\infty=1$} i.e.""",
"""Two-line passage, including the abbreviation endom. The continuous underline begins beneath la relation and runs beneath the entire relation, ending before i.e. All three primes and the terminal numeral 1 are visible. The group sign is capped, without a separate hat. The left edge touches the first stroke of Il. Both points in i.e. are retained."""),
('B09',r"""\begin{tikzpicture}[baseline=(m.base)]
\node[inner sep=3pt] (m) {$l_0^p\cdot\operatorname{int}(g)l_1^p\cdot\operatorname{int}(g\rho(g))l_\infty^p=1$};
\draw (m.north west)--(m.south west)--([xshift=-.18cm]m.south east);
\draw (m.north east)--(m.south east);
\end{tikzpicture}""",
"""Complete equation and enclosure. Product points occur after l_0^p and l_1^p. A left vertical joins a lower horizontal; a separate right vertical closes the right side, with a small lower gap. No independent new top edge is established: the visible line above belongs to the preceding underlined passage. The enclosure is therefore drawn with three sides rather than silently converted to a four-sided box. Upper-edge fragments of the preceding line are clipped."""),
('B10',r"""$l_0^p\unsure{(g l_1^p g^{-1})|(g l_1^p g)^{-1}}(g\rho(g)l_\infty^p\rho(g)^{-1}g^{-1})=1$""",
"""Full expanded product. The first raised -1 lies very close to the first closing parenthesis: attachment to the last g versus the entire parenthesized product is left explicit. The subsequent rho(g)^{-1} and final g^{-1} have clear attachments. The upper edge touches the tall exponent-p stems, but their looped bodies are visible. No terminal stop is supplied."""),
('B11',r"""$l_0^p g l_1^p\rho(g)l_\infty^p\rho(g)^{-1}g^{-1}=1$""",
"""Complete displayed relation. All three exponent p forms, subscripts 0/1/infinity, both live inverse exponents, and the final numeral 1 are included. No extra product points or punctuation are present."""),
('B12',r"""soit encore, en faisant passer le $g^{-1}$ à gauche""",
"""Complete prose line and the single inverse exponent. The comma after encore is retained; no final stop is visible."""),
('B13',r"""\deleted{$l_0^p\cdot\operatorname{int}(g)(l_1^p\cdot\operatorname{int}(\unsure{\rho(g)})(l_\infty^p))=1$}
$\operatorname{int}(g^{-1})l_0^p\cdot l_1^p\cdot\operatorname{int}(\rho(g)(l_\infty^p)=1$""",
"""The entire upper equation is crossed through by a long line, including its final 1. Its central rho(g) is partially obscured and remains doubtful. The lower equation is live. In the lower int(rho(g)(l_infty^p) expression, I can establish the close after the inner g and the close after l_infty^p, but no additional close between them for int(rho(g)); the apparent unmatched parenthesis is preserved instead of repaired. Product points in each row are recorded locally. No final stop."""),
('B14',r"""Le\unsure{s} relation\unsure{s} $(*)_2$ et $\unsure{(**)|(***)}$ sont vérifiées par""",
"""The final s strokes of the article and noun are compressed, so their presence is left explicit rather than inferred from agreement. A small 2 stands low to the right of the first parenthetic star label. The second star cluster is retraced and the count remains two versus three; its outer parentheses are visible. The rest of the line reads sont vérifiées par, without final punctuation."""),
('B15',r"""construction (pour $**$, il suffit \unsure{=} de \unsure{le|la} vérifier""",
"""Complete continuation line, with an opening parenthesis left unclosed at this line's end. Two separate star-like marks follow pour without extra parentheses. Immediately after suffit are two short, roughly parallel dark strokes: retained as an uncertain equals-like graphic; a cancelled remnant or compressed pen trace is not excluded. The article after de is compressed, leaving le/la uncertain. No terminal punctuation is supplied."""),
('B16',r"""pour \unsure{la|les} valeur\unsure{s} aux deux membres en $l_0\ l_1$).""",
"""Complete final line. The article and possible plural ending on valeur are compressed and remain uncertain. The following word is read literally as aux. The two l symbols have subscripts 0 and 1; no distinct comma is established between them, so none is supplied. The closing parenthesis and external stop are both visible."""),
('B17',r"""\mspage{7}""",
"""Isolated handwritten footer numeral 7 with its crossing stroke, enlarged from the small source box.""")
]

out=edition/'second'/'145_scan008_second.tsv'
if out.exists(): raise SystemExit('Refusing to overwrite an existing second reading')
with out.open('w',encoding='utf-8',newline='') as f:
    writer=csv.writer(f,delimiter='\t',lineterminator='\n')
    writer.writerow(['box','reading'])
    writer.writerows((box,reading) for box,reading,obs in rows)

mp=edition/'second'/'145_scan008_crop_manifest.json'
manifest=json.loads(mp.read_text(encoding='utf-8'))
obs={box:note for box,reading,note in rows}
for item in manifest: item['observations']=obs[item['box']]
mp.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

with (root/'audit_packets'/'145_scan008'/'boxes.tsv').open(encoding='utf-8',newline='') as f:
    expected=list(csv.DictReader(f,delimiter='\t'))
with out.open(encoding='utf-8',newline='') as f:
    actual=list(csv.DictReader(f,delimiter='\t'))
assert len(actual)==len(expected)==len(manifest)==17
assert [r['box'] for r in actual]==[r['box'] for r in expected]==[r['box'] for r in manifest]
assert all(r['reading'].strip() for r in actual)
for item,box in zip(manifest,expected):
    assert item['coords']==[int(box[k]) for k in ('x0','y0','x1','y1')]
    assert (edition/item['crop']).is_file()
    assert item['observations'].strip()
print(json.dumps({
    'boxes':len(actual),'crops':len(manifest),'tsv':str(out),'manifest':str(mp),
    'tsv_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),
    'manifest_sha256':hashlib.sha256(mp.read_bytes()).hexdigest(),
    'status':'complete; independent image-only submission'
},ensure_ascii=False,indent=2))

