from pathlib import Path
import csv, json, hashlib

root = Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work')
edition = root / 'edition'
readings = [
('B01', r"""[C]\quad\textcircled{1}\quad\mspage{1}""",
 """Header inscriptions [C], circled 1, and page 1. The lower edge clips upper strokes of the title; those fragments are not treated as complete text."""),
('B02', r"""Automorphismes extérieurs du groupe à lacets \unsure{\deleted{$\Pi$}p|p}rofini $\hat\Pi=\hat\Pi_{0,3}$""",
 """The initial p of profini coincides with a dense Pi/P-like retraced or crossed trace; an earlier cancelled Pi overwritten by p and a simply retraced p remain alternatives. The two group signs have separate hats and two full legs. No terminal stop. The upper-left edge clips an incidental portion of the circled header numeral."""),
('B03', r"""\margin{\uline{et structure}\\\uline{d'extension}\\\uline{de $\mathcal E=\mathcal E_{\unsure{03|0,3}}$}}""",
 """Rotated -45 degrees. Three marginal lines, each separately underlined. The subscript has visible 0 and 3; no distinct intervening comma can be established. The broad curly mathematical letters are rendered as calligraphic E without inferring their function."""),
('B04', r"""\margin{$\unsure{\delta}$}""",
 """Isolated looped marginal sign: a lower oval and rising hooked stroke give a delta-like outline, but identity and function are not secure."""),
('B05', r"""du $\Pi_{\unsure{0,3|03}}$""",
 """The leading word is du. The tall group sign is retraced but has a cap and two legs; no separate hat is visible. The low 0 and 3 are visible, while the possible separating comma is compressed."""),
('B06', r"""\unsure{même} relation — \unsure{si $f$|s'ils} \unsure{envoie|engendrent} ce sera un autom.""",
 """The complete line is transcribed with unresolved alternatives for its compressed opening word and the cluster after the dash. The tall central form has a crossing stroke and descending return; I cannot securely separate si f from a contracted s'ils, nor establish all letters of the following low word. These are provisional visual alternatives, not a mathematical reconstruction. Incidental strokes from adjacent lines are clipped at top and bottom."""),
('B07', r"""(donc on a $\rho^3=\mathrm{id}$).
\deleted{On \unsure{s'intéresse} aux}""",
 """The parenthesis and external stop after id are distinct. The lower sentence is crossed through by one long horizontal stroke; s'intéresse is retained as a doubtful cancelled reading because some medial letters are covered. Descenders of the preceding formula are clipped at the top."""),
('B08', r"""$\sigma_\infty(l_\infty)=(l_1l_0)^{-1}=l_{\unsure{0|\infty}}^{-1}l_1^{-1}$
\inserted{$(=\operatorname{int}(\unsure{l_0}^{\unsure{-1|\deleted{-1}|+1}})\cdot l_\infty)$}""",
 """The full upper formula and lower parenthetic addition are recorded. The first right-hand subscript has an open rounded/looped outline and is left as 0 versus infinity. In the addition, the argument stem/index is heavily retraced; the raised minus/extra upright stroke and 1 do not securely settle whether the exponent is live -1, cancelled -1, or +1. A distinct dot lies after the inner closing parenthesis. No missing cancellation layer is reconstructed. The bottom edge clips strokes of the following line."""),
('B09', r"""\unsure{en} $\sigma_{\unsure{0}},\sigma_\infty$\inserted{(échangeant $l_1$ et $l_0$ resp. $l_\infty$ et $l_0$)}, de sorte qu'on a""",
 """The small leading two-stroke cluster remains uncertain. The first sigma index is blackened, with an oval consistent with 0. The complete parenthetic passage is interlinear and joined to the baseline by a long bent connector ending under its right edge. The baseline comma following the addition is retained. The top edge clips the preceding main line; the main sentence continues beyond the right extent without a supplied continuation."""),
('B10', r"""du groupe \inserted{$\mathcal S_3$} des""",
 """A large looped S with low 3 is added above the gap between groupe and des, with a bent insertion guide. It is rendered as calligraphic S without assigning a typographic convention. The upper edge contains only a clipped fragment of the preceding main line, including rho; no beginning or continuation is invented."""),
('B11', r""", \unsure{rien} de propre dans le""",
 """The opening comma is visible. The first word's long initial descending stroke makes rien less secure than the following de propre dans le. This is a continuation fragment; no left or right continuation is supplied. Adjacent-line fragments are clipped at the top and bottom."""),
('B12', r"""faire opérer sur $\Pi\unsure{'}$, en respectant la structure \unsure{en|de}
lacets (avec \inserted{\unsure{caractère}} multiplicateur $1$). On a bien une""",
 """The group sign has a tall cap and two legs, with no separate hat established. Tiny detached dark marks at its upper right are retained as an uncertain prime/pen trace rather than silently discarded; their status is unresolved. The short word after structure is compressed (en/de). The small interlinear word before multiplicateur is tentatively caractère and is attached by a curved guide. The closing parenthesis and following stop after 1 are distinct. No continuation after une is supplied."""),
('B13', r"""\inserted{vraie} représentation du ss-groupe $\mathcal S_3^+\simeq Z/3Z$ engendré""",
 """The small vraie is inserted before représentation by a bent guide. The abbreviation ss-groupe is preserved. The large looped S has low 3 and raised +; the relation has a wavy upper stroke and one straight lower stroke. The rightmost engendré reaches the crop edge; the accent is visible and no continuation or terminal punctuation is supplied."""),
('B14', r"""\mspage{4}""",
 """Isolated handwritten footer numeral 4, enlarged from a small source box."""),
('B15', r"""On prend la présentation par les générateurs
$l_0,l_1,l_\infty$ liés par
\[l_0l_1l_\infty=1\]""",
 """Complete introductory passage and product relation. All three subscripts and the terminal numeral 1 are recorded. No punctuation follows the displayed relation."""),
('B16', r"""Un endomorphisme du $\Pi_{\unsure{0,3|03}}$ est donc donné
par des éléments $l'_0,l'_1,l'_\infty$ satisfaisant la""",
 """Complete two-line passage. Each of the three l symbols has a distinct prime. The group-sign subscript is compressed; the separator between 0 and 3 remains uncertain. The sentence continues below the box after la; no continuation is supplied here."""),
('B17', r"""$\rho(l_0)=l_1,\quad\rho(l_1)=l_\infty,\quad\rho(l_\infty)=l_0$""",
 """Three complete cyclic-image equations. The two separating commas are visible; no final stop. No detached dot is present over any rho. Lower-edge fragments belong to the following line."""),
('B18', r"""$\sigma_\infty(l_0)=l_1,\quad\sigma_\infty(l_1)=l_0,$""",
 """Both complete image equations are recorded, including the comma at the far right. The sigma subscripts have two-lobed infinity outlines."""),
('B19', r"""on a évidemment $\sigma_\infty^2=\mathrm{id}$.""",
 """The initial on is small and read in lowercase. The raised 2 and terminal stop after id are clear. At the far right, the next On begins but is cut off; it is not completed here. The bottom edge contains clipped strokes from the following interlinear passage."""),
('B20', r"""$\rho\sigma_i\rho^{-1}=\sigma_{\rho(i)}$""",
 """Complete conjugation formula. The first rho head is heavily retraced, but no separate cancellation line is established. The left i dot, the right nested rho(i), and live raised -1 are visible. No terminal punctuation. An incidental descender is clipped at the upper right."""),
('B21', r"""en désignant par $\rho$ aussi la permutation circulaire
sur $0,1,\infty$. On considère $\rho$ et les $\sigma_i$""",
 """The full two-line passage is recorded, including the three numerical/index values and the stop after infinity. The lower edge touches the bottoms of the second line, including the final i stem; no extra continuation is supplied."""),
('B22', r"""de l'ens. $\{0,1,\infty\}$""",
 """The abbreviation ens. and its stop are visible. The set has curly delimiters and two separating commas. No stop follows the closing brace. Only incidental preceding-line strokes are clipped at the top."""),
]

out = edition / 'second' / '145_scan005_second.tsv'
if out.exists():
    raise SystemExit('Refusing to overwrite an existing second reading')
with out.open('w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f, delimiter='\t', lineterminator='\n')
    writer.writerow(['box','reading'])
    writer.writerows((box, reading) for box, reading, obs in readings)

manifest_path = edition / 'second' / '145_scan005_crop_manifest.json'
manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
obs_by_box = {box:obs for box,reading,obs in readings}
for item in manifest:
    item['observations'] = obs_by_box[item['box']]
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')

with (root / 'audit_packets' / '145_scan005' / 'boxes.tsv').open(encoding='utf-8', newline='') as f:
    expected = list(csv.DictReader(f, delimiter='\t'))
with out.open(encoding='utf-8', newline='') as f:
    actual = list(csv.DictReader(f, delimiter='\t'))
assert len(actual) == len(expected) == len(manifest) == 22
assert [r['box'] for r in actual] == [r['box'] for r in expected]
assert [r['box'] for r in actual] == [r['box'] for r in manifest]
assert all(r['reading'].strip() for r in actual)
assert all((edition / r['crop']).is_file() and r['observations'].strip() for r in manifest)
for item, box in zip(manifest, expected):
    assert item['coords'] == [int(box[k]) for k in ('x0','y0','x1','y1')]
print(json.dumps({
    'boxes':len(actual),
    'crops':len(manifest),
    'tsv':str(out),
    'manifest':str(manifest_path),
    'tsv_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),
    'manifest_sha256':hashlib.sha256(manifest_path.read_bytes()).hexdigest(),
    'status':'complete; independent image-only submission'
},ensure_ascii=False,indent=2))

