from pathlib import Path
import csv,json,hashlib
root=Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work')
edition=root/'edition'
rows=[
('B01',r"""\mspage{\unsure{4|9}}""",
"""Isolated upper handwritten numeral. Its triangular upper part joins a transverse stroke and a long hooked right leg; 4 is the first visual reading, with 9 retained as an alternative. The lower edge clips a trace from the following line."""),
('B02',r"""plus haut, \deleted{\unsure{en fonction de} $g$}
\inserted{\unsure{savoir} $\unsure{g}$ correspond. à}
\deleted{\unsure{deux}} \unsure{d'|$\alpha'$}""",
"""The baseline phrase after plus haut is crossed by a long horizontal stroke. Its low first cluster, tall medial f/t-like stem, and final de-like cluster support en fonction de only provisionally; the terminal descending g is visible. Above it is a separate addition, tentatively savoir g correspond. à. The final word correspond. has an abbreviated terminal stop. A later short word with x-like ending is separately cancelled and tentatively read deux. The last detached d'/alpha-prime-like inscription is left unresolved. The header numeral appears incidentally at the upper edge and is handled in B01. No syntactic continuation is supplied."""),
('B03',r"""\[
\left\{\begin{array}{l}p=-1\\q=-1,\ r=1\end{array}\right.
\qquad
\begin{array}{l}
g=l_0^\alpha l_1^\beta\quad(\alpha+\beta=1),\ \alpha,\beta\in Z)\\
\text{ou mieux, }\beta=-1
\end{array}
\]""",
"""Two rows of conditions with a left brace. All numerical values and the alpha/beta exponents are included. The first right-hand line visibly closes a parenthesis after alpha+beta=1, then continues with a comma and alpha,beta in Z, followed by another close; the unmatched final parenthesis is preserved. Z is retraced but has no separate hat. No terminal stop after the second row."""),
('B04',r"""\uline{NB} Si on remplace dans les calculs qui
précèdent $L_0$ par $L_1$, alors $g$ est remplacé par
$\rho(g)$, $q$ et $r$ restant inchangés. On trouve""",
"""Complete three-line prose passage. NB is singly underlined and has no supplied abbreviation stops. Both L symbols are angular capitals, with subscripts 0 and 1. The commas and stop after inchangés are visible. The final phrase continues beyond this box without a supplied continuation. The lower edge touches the rho/g/q descenders."""),
('B05',r"""ainsi, en plus du caractère cyclotomique $\chi$,
\deleted{\unsure{deux}}\inserted{une} fonction \unsure{monographique} \inserted{\uline{$\beta$}}, sur le""",
"""The lower initial word is cancelled by a dark horizontal stroke; deux remains doubtful. Une is written above it. The long adjective after fonction has a clear g-like descender, but its compressed ending leaves the reading monographique tentative. A large dark beta is added between that word and the comma, and is separately underlined. Faint overlapped traces beside/beneath beta do not permit a secure earlier glyph or layer sequence. The upper chi is distinct. The bottom edge clips parts of the next formula's annotation, handled in B06."""),
('B06',r"""$\operatorname{Aut\,ext}_{\mathrm{lac}}\bigl(\overset{\substack{\inserted{\unsure{\Pi|\pi}}\\\vee}}{\hat\pi_{0,3}},\mathcal S_3\bigr)\overset{\mathrm{\unsure{dfn|déf}}}{=}\Gamma,$""",
"""Complete formula. Aut ext has a low lac inscription beneath its right part. The first argument is a hatted pi with subscript 0,3. Above it is a small capped Pi/pi sign with a downward V-shaped guide; both are retained as an addition with local case uncertainty. The second argument is a large looped S with low 3. The small writing above equals reads dfn or déf, without a certain stop. The final large sign has a doubled left stem and a short downturned right tip, supporting Gamma rather than a full two-leg Pi. A comma follows. Clipped upper-line fragments are incidental."""),
('B07',r"""\deleted{\unsure{savoir}}\inserted{\unsure{à}}""",
"""A single cancelled word has an initial s-shaped sweep, low medial loops, a dotted upright toward the right, and a final hooked stroke; savoir remains tentative because the crossing line obscures several letters. Above it is a small a-like body with a partly clipped upper accent, tentatively à. The lower-left diagonal fragment belongs to the following interlinear gamma."""),
('B08',r"""et une autre \inserted{$\gamma$} \unsure{à|:} valeurs""",
"""Complete baseline fragment with gamma added above the gap after autre. Two small dark marks between gamma and valeurs can be an extremely compressed à or a colon-like inscription; that distinction remains open. The final plural s in valeurs is visible. Upper-edge formula fragments are clipped and not completed."""),
('B09',r"""$\varphi(\alpha)\cdot g=l_0^\alpha g l_1^{-\alpha}$""",
"""Complete action formula. There is a distinct point after the closing parenthesis on the left, but no extra points between right-hand factors. Both numerical subscripts and the negative alpha exponent are included. No terminal stop. The left phi descender touches the lower edge; upper-edge strokes belong to the preceding line."""),
('B10',r"""\[
\begin{aligned}
(\gamma,\chi):\ \Gamma&\underset{\unsure{\cdot\,\cdot}}{\longrightarrow}\Pi/\hat Z\times\hat Z^{*}\\
u&\longmapsto(\gamma(u),\chi(u))
\end{aligned}
\]""",
"""Complete two-row mapping. The source sign has a doubled left stem and short right downstroke (Gamma); the quotient's first sign has two full legs (Pi). Both Z signs have separate hats; the final raised mark has several rays and is read as a star. The upper arrow has no tail bar; the lower arrow has a definite tail bar. Two detached small dark points lie on a slight diagonal below the upper arrow shaft; they are represented as an uncertain graphic, not assigned a mathematical label. No terminal stop is supplied."""),
('B11',r"""\margin{\uline{NB}
\inserted{$\gamma_0:\mathcal E_0\longrightarrow\Pi$}
est un $1$. cocycle sur
$\unsure{\mathcal E_0}\ \unsure{\simeq}\ \operatorname{Aut}_{\mathrm{lac}}(\Pi,L_0)$,
[\deleted{\unsure{fixant|plein}}\inserted{\unsure{caractérisé|caractérisés}}
\illegible{3}
des éléments qui commutent ext. à $\mathcal S_3$}""",
"""Rotated -45 degrees. This is the crowded marginal note, not the incidental main text visible at its right and bottom edges. NB is underlined. A gamma with low 0, colon, curly E with low 0, plain right arrow, and two-leg Pi are visible at the upper right; a broad curved connector wraps from this addition toward the following est un. The next line has a handwritten 1 followed by a low point before cocycle; a hyphen is not silently supplied. The next E_0-like sign is heavily retraced, followed by an uncertain equivalence-like mark and Aut_lac(Pi,L_0), with a terminal comma. A square opening bracket precedes a crossed word (fixant/plein uncertain) and an interlinear word tentatively caractérisé(s). The following roughly three overlapping prose clusters cannot be read physically through the crossing inscriptions and are represented as illegible; the estimate counts visible word-sized clusters, not a reconstructed phrase. The lower continuation des éléments qui commutent ext. à and the large looped S_3 are visible. No closing square bracket is established. Incidental main-text fragments at the edges are not invented or completed."""),
('B12',r"""est injective, \deleted{\unsure{et|$\beta$}} $\beta$ étant définie par $\gamma$
car $\gamma$ prend ses valeurs dans les classes des
$g\in\Pi$ (mod $\varphi(\hat Z)$ satisfaisant une relation""",
"""Complete three-line main-text continuation. A small, densely cancelled cluster after the comma remains et versus beta-like. The following live beta, étant définie par gamma, and the subsequent prose are clear. The last line begins g in Pi and contains a parenthetic mod phrase with phi(hatted Z); only the close of the phi argument is established before satisfaisant, so an additional outer close is not supplied. Descenders meet the physical lower page edge. No final stop is established after relation. Marginal fragments at upper left and a partial footer numeral at the far right are incidental; the footer is handled in B13."""),
('B13',r"""\mspage{10}""",
"""Isolated lower-right handwritten page number 10. The upper-left clipped stroke belongs to the adjacent main line, not the numeral.""")
]

out=edition/'second'/'145_scan011_second.tsv'
if out.exists(): raise SystemExit('Refusing to overwrite existing second reading')
with out.open('w',encoding='utf-8',newline='') as f:
    w=csv.writer(f,delimiter='\t',lineterminator='\n')
    w.writerow(['box','reading'])
    w.writerows((box,reading) for box,reading,note in rows)
mp=edition/'second'/'145_scan011_crop_manifest.json'
manifest=json.loads(mp.read_text(encoding='utf-8'))
notes={box:note for box,reading,note in rows}
for item in manifest: item['observations']=notes[item['box']]
mp.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
with (root/'audit_packets'/'145_scan011'/'boxes.tsv').open(encoding='utf-8',newline='') as f:
    expected=list(csv.DictReader(f,delimiter='\t'))
with out.open(encoding='utf-8',newline='') as f:
    actual=list(csv.DictReader(f,delimiter='\t'))
assert len(actual)==len(expected)==len(manifest)==13
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

