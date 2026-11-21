"""Independent scan047 second reading from the assigned fixed crops only.

The TSV is written atomically after all 24 fixed crops have been viewed.
No other reading, comparison, OCR, research, or TeX compilation is used.
"""
import csv
import hashlib
import json
import os
from pathlib import Path

ROOT = Path('/workspace/scratch/8132fe1cca43/work/SP82_C13_148')
INPUTS = Path('/workspace/scratch/8132fe1cca43/work/blind_inputs/148_scan047')
DISPLAY = Path('/workspace/scratch/8132fe1cca43/work/blind_display/148_scan047')
OUT = ROOT / 'second'


def picture(kind, width, height, ink, scale='.017'):
    return (
        '\\' + kind + r'{\begin{tikzpicture}[x=' + scale
        + 'cm,y=-' + scale
        + r'cm,line cap=round,line join=round,>=stealth,font=\scriptsize]'
        + '\n' + rf'\clip (0,0) rectangle ({width},{height});'
        + '\n' + ink.strip() + '\n' + r'\end{tikzpicture}}'
    )


rows = [
    ('B047-B01', r'\mspage{3)}'),
    ('B047-B02', r'''qui forme un groupoïde \deleted{\(\unsure{\mathrm{Gr}}\)}. \(\unsure{\mathrm{Grbip}|\mathrm{Grobip}}\) ou (\(\unsure{\mathrm{Grabip}\mathord{-}1|\mathrm{Grabip}\mathord{\sim}1}\))'''),
    ('B047-B03', r'''Objets : graphes \inserted{finis} \((S,\vec A,\sigma,\unsure{o|\sigma})\) \inserted{+ structure suppl.} (pouvant avoir des
sommets isolés, des boucles fermées, a fortiori'''),
    ('B047-B04', r'''plusieurs arêtes entre deux sommets, et \unsure{aussi|avoir}
des ``\uline{arêtes} libres'' \inserted{(``sommets'', ``\unsure{trous}'')} correspondant aux pts fixes de \(\sigma\))'''),
    ('B047-B05', r'''\(S,\inserted{\vec A}\) ens. finis, \(\sigma:\vec A\longrightarrow\vec A\) involution, \(o:\vec A\longrightarrow S\) appl.
``origine''. On se donne de plus'''),
    ('B047-B06', r'''\[S\xrightarrow{\deleted{\unsure{g}}\;\inserted{\gamma}}\mathbb N\]'''),
    ('B047-B07', picture('diagram', 437, 147, r'''
\node at (40,65) {$\deleted{\unsure{\vec A|\widetilde A}}$};
\node at (94,80) {$=$};
\node at (138,67) {$\unsure{\overset{\uparrow}{A}|\vec A}/\sigma$};
\draw[->,line width=.8pt] (211,80) -- (340,77);
\node at (386,79) {$\mathbb N$};
\node at (223,31) {$\unsure{\Gamma|\pi}$};
\node at (278,30) {$\deleted{\unsure{\rho|g}}$};
\node at (316,29) {$2$};
\draw[line width=.7pt] (8,104) -- (78,18) -- (27,127) -- (87,40) -- (40,141);
\draw[line width=.65pt] (19,57) -- (86,8) -- (54,50);
\node[anchor=north] at (92,126) {\deleted{``\unsure{poids}''}};
\node[anchor=north] at (225,125) {$\unsure{\mathrm{def}}$};
''', '.020')),
    ('B047-B08', r'''(application \deleted{\unsure{rigidité|rigidification}} \inserted{``indice de rigidification''})'''),
    ('B047-B09', picture('diagram', 1065, 163, r'''
\node[anchor=west] at (58,52) {\deleted{``\unsure{ens. des arêtes}''}};
\node at (181,91) {$\deleted{\unsure{\widetilde A|A}}$};
\node at (280,24) {$\unsure{\mathrm{def}}$};
\node at (277,77) {$\unsure{=|:=}$};
\node at (341,78) {$\vec A/\sigma$};
\node[anchor=west] at (635,77) {\deleted{``ens. des sommets \unsure{propres}''}};
\node at (847,119) {\inserted{``apparents''}};
\draw[line width=.65pt] (40,109) .. controls (200,108) and (265,92) .. (375,90)
 .. controls (515,92) and (581,92) .. (634,78)
 .. controls (741,83) and (854,55) .. (1065,52);
\draw[line width=.6pt] (59,109) -- (98,13) -- (76,104) -- (139,0)
 -- (109,108) -- (188,8) -- (141,104) -- (227,0)
 -- (184,102) -- (278,41) -- (248,126);
\draw[line width=.7pt] (0,144) -- (45,72);
\draw[line width=.7pt] (652,163) -- (745,53);
\draw (847,128) -- (880,163);
\node[anchor=south west] at (697,10) {\unsure{indice de rigidification}};
''', '.012')),
    ('B047-B10', r'''Objets :
\margin{pas assez précis comme \unsure{donnée|données}, la \unsure{pondération|condition} d'une arête doit être remplacée par celle d'un pol. comb. \(\unsure{\Gamma_a|\Pi_a}\) avec \(\omega(\unsure{t_a|T_a})\simeq\omega(a)\)}'''),
    ('B047-B11', '\\margin{' + picture('figure', 464, 217, r'''
\node[anchor=north west,align=left] at (8,42) {J'ai indiqué une pondé-\\
ration des sommets,\\
mais pas des arêtes};
\draw[line width=.55pt] (293,13) .. controls (345,7) and (414,5) .. (432,28)
 .. controls (447,51) and (450,70) .. (435,88)
 .. controls (405,125) and (344,131) .. (296,141)
 .. controls (219,160) and (121,159) .. (68,178)
 .. controls (40,188) and (29,200) .. (22,217);
\draw (34,26) .. controls (45,17) and (60,13) .. (68,0);
\node[anchor=south] at (90,31) {\unsure{d'}};
\node[anchor=south] at (209,29) {\unsure{d'}};
''', '.020') + '}'),
    ('B047-B12', picture('figure', 498, 351, r'''
\node[anchor=south west] at (0,24) {\unsure{mais p\ldots}};
\draw (0,57) .. controls (16,33) and (61,28) .. (129,22)
 .. controls (184,18) and (229,10) .. (267,0);
\coordinate (L) at (73,207);
\coordinate (M) at (226,207);
\coordinate (V) at (199,108);
\coordinate (U) at (300,109);
\coordinate (R) at (364,198);
\coordinate (E) at (469,182);
\coordinate (D) at (242,287);
\draw[line width=.7pt] (L) -- (M);
\draw[line width=.7pt] (L) .. controls (126,183) and (202,166) .. (M);
\draw[line width=.7pt] (L) .. controls (118,237) and (208,242) .. (M);
\draw[line width=.65pt] (L) .. controls (17,247) and (3,366) .. (40,336)
 .. controls (62,314) and (75,254) .. (L);
\draw[line width=.55pt] (L) .. controls (62,157) and (52,105) .. (49,67);
\draw[line width=.35pt] (L) .. controls (88,156) and (104,109) .. (119,59);
\draw[line width=.65pt] (V) .. controls (228,134) and (235,170) .. (M);
\draw[line width=.65pt] (V) -- (U);
\draw[line width=.65pt] (V) .. controls (219,87) and (287,81) .. (U);
\draw[line width=.65pt] (M) -- (U);
\draw[line width=.7pt] (U) -- (R);
\draw[line width=.65pt] (M) .. controls (272,215) and (318,209) .. (R);
\draw[line width=.65pt] (R) .. controls (401,174) and (429,191) .. (E);
\draw[line width=.65pt] (M) .. controls (238,232) and (241,255) .. (D);
\draw[line width=.6pt] (R) .. controls (354,245) and (330,291) .. (329,345);
\draw[line width=.65pt] (U) .. controls (318,74) and (324,27) .. (333,8);
\draw[line width=.65pt] (U) .. controls (329,93) and (366,65) .. (385,61);
\draw[line width=.65pt] (U) .. controls (335,116) and (364,119) .. (385,120);
\foreach \p in {L,M,V,U,R,E,D} {\fill (\p) circle[radius=1.8pt];}
\fill (130,306) circle[radius=1.8pt];
\node at (50,194) {$0$};
\node at (258,197) {$2$};
\node at (198,81) {$13$};
\node at (292,74) {$4$};
\node at (368,177) {$0$};
\node at (484,161) {$3$};
\node at (256,281) {$1$};
\node at (112,331) {$2$};
''', '.024')),
    ('B047-B13', picture('figure', 270, 237, r'''
\coordinate (T) at (126,83);
\draw[line width=.7pt] (T) .. controls (129,55) and (137,36) .. (132,18);
\draw[line width=.55pt] (T) .. controls (163,61) and (185,31) .. (199,0);
\draw[line width=.7pt] (T) .. controls (173,58) and (215,92) .. (252,99);
\fill (T) circle[radius=2.1pt];
\node at (95,88) {$0$};
\coordinate (L) at (46,181);
\draw[line width=.75pt] (L) .. controls (70,161) and (103,159) .. (137,159)
 .. controls (169,157) and (187,178) .. (186,192)
 .. controls (186,206) and (164,220) .. (143,216)
 .. controls (100,210) and (82,200) .. (L);
\fill (L) ellipse[x radius=2.5pt,y radius=1.8pt];
\node at (14,175) {$3$};
''', '.027')),
    ('B047-B14', r'''\deleted{Ou encore, posons \(\widetilde S=S\amalg A_\ell\), (\unsure{identifié}
à l'ens. de \uline{tous} les ``sommets'', \deleted{\unsure{propres}} et \inserted{\uline{``\unsure{marqués|impropres}''} (i.e. \(\in S\))} \inserted{apparents}
et ``libres'', \inserted{(i.e. correspondant aux \(a\in A_\ell\))} du graphe) \unsure{l'on|on} donne
\[\widetilde S\xrightarrow{\pi}\mathbb N\]}
(\uline{pondération} du graphe)'''),
    ('B047-B15', r'''\margin{\[\widetilde S=S\amalg\deleted{\unsure{\widetilde S_\ell|\vec A_\ell}}\;\underset{\inserted{A_\ell}}{\uparrow}\]\deleted{\unsure{sommets|apparents}}}'''),
    ('B047-B16', r'''\margin{\[\widetilde A=\vec A/\sigma=A\amalg A_\ell\]}'''),
    ('B047-B17', '\\margin{' + picture('diagram', 378, 348, r'''
\node at (45,56) {$\vec A$};
\node at (93,70) {$=$};
\node at (147,57) {$\unsure{\vec A_0|\vec A_o}$};
\node at (195,66) {$\amalg$};
\node at (247,54) {$\vec A_\ell$};
\draw (108,95) .. controls (105,107) and (121,109) .. (127,101)
 .. controls (134,117) and (154,108) .. (169,105);
\node at (151,133) {$\vec A\setminus\vec A^\sigma$};
\draw (222,89) -- (222,102) -- (276,102) -- (276,94);
\node at (248,132) {$\vec A^\sigma$};
\draw[->,line width=.8pt] (130,171) -- (127,246);
\node[anchor=west] at (139,197) {deg 2};
\draw[->,line width=.8pt] (232,172) -- (229,249);
\node[anchor=west] at (241,199) {deg 1};
\draw[->,line width=1pt] (64,133) -- (63,261);
\draw[->,line width=.55pt] (40,222) .. controls (49,168) and (46,133) .. (46,98);
\draw[line width=.8pt] (30,226) -- (51,192) -- (36,172) -- (48,120);
\draw[line width=.6pt] (36,170) -- (52,145);
\draw[line width=.6pt] (38,111) -- (54,97);
\node at (43,210) {$\deleted{\unsure{\sigma|A}}$};
\node at (38,299) {$\widetilde A$};
\node at (87,305) {$=$};
\node at (131,298) {$A$};
\node at (181,307) {$\amalg$};
\node at (238,301) {$A_\ell$};
''', '.026') + '}'),
    ('B047-B18', '\\margin{' + picture('diagram', 419, 294, r'''
\node[anchor=north west] at (8,8) {Ordre d'un sommet};
\node at (65,103) {$\sigma(s)=$};
\node at (167,104) {$\sigma_\ell(s)$};
\node at (229,105) {$+$};
\node at (302,104) {$\unsure{\sigma_0|\sigma_o}(s)$};
\draw (125,138) -- (123,148) -- (206,143) -- (203,135);
\node[anchor=north,align=center] at (198,155) {correspond\\aux ``trous''\\ou \unsure{cercles|cordes}\\de recollages};
\node[anchor=west] at (352,191) {\unsure{Fl\ldots}};
\draw (355,236) -- (419,231);
''', '.024') + '}'),
    ('B047-B19', r'''La donnée du \uline{graphe} sous-jacent à un
graphe \deleted{\(\unsure{\mathrm{MA}|\mathrm{MAP}}\)} \inserted{bip.} revient à celle du graphe
``ordinaire'' correspondant (\unsure{sans} arêtes libres,
i.e. où \(\sigma\) opère sans pts fixes), i.e.'''),
    ('B047-B20', r'''\[\bigl(S,(\vec A\setminus\vec A^\sigma),\ \sigma|(\vec A\setminus\vec A^\sigma),\ o|\vec A\setminus\vec A^\sigma)\bigr)\ ;\]
\inserted{fini}'''),
    ('B047-B21', r'''\uline{plus} un ensemble \inserted{fini} \(A_\ell\) (\uline{arêtes} \deleted{\(\unsure{\equiv|=}\)} libres)
\deleted{ou ``sommets-trous'')} et une application'''),
    ('B047-B22', r'''\[A_\ell\longrightarrow S\]'''),
    ('B047-B23', r'''\uline{Flèches} les iso. de telles structures'''),
    ('B047-B24', r'\mspage{46}'),
]


extra_views = {
    'B047-B02': ['B047-B02_native3.png'],
    'B047-B03': ['B047-B03_native3.png'],
    'B047-B04': ['B047-B04_native3.png'],
    'B047-B06': ['B047-B06_native3.png'],
    'B047-B07': ['B047-B07_native3.png'],
    'B047-B08': ['B047-B08_native3.png'],
    'B047-B09': ['B047-B09_native3.png'],
    'B047-B10': ['B047-B10_native3_cw45.png'],
    'B047-B14': ['B047-B14_native3.png'],
    'B047-B18': ['B047-B18_native3.png'],
}

observations = {
    'B047-B01': 'Small face number 3 with closing parenthesis. Lower-edge fragment is not expanded into a further word.',
    'B047-B02': 'One line with a heavily overwritten category name. Short category codes and the final relation/number remain local candidates.',
    'B047-B03': 'Interlinear finis and + structure suppl. have separate insertion scope. Last entry of the tuple is retained as o/sigma doubt.',
    'B047-B04': 'Only arêtes is underlined. The small parenthetic addition below it is retained with its separate quoted words and a local doubt.',
    'B047-B05': 'Raised arrowed A by S is retained as an insertion. Formula arrows point right; N is not present in this box. Upper edge touches the preceding insertion without supplying its clipped remainder.',
    'B047-B06': 'Rightward arrow from S to double-stroked N. Old label is scribbled out; gamma is above/right of it.',
    'B047-B07': 'Heavily deleted left letter, upward-looking arrow over the following A, overwritten arrow labels, and visible 2 are spatially retained. Bottom gloss is clipped and doubtful.',
    'B047-B08': 'Application remains legible. The cancelled old word and replacement lower phrase have distinct scopes; old word is uncertain.',
    'B047-B09': 'Long crossing stroke, cancelled gloss, doubtful left relation, right caption, and apparents beneath it are retained. Letter recovery under the dense cancellation remains uncertain.',
    'B047-B10': 'Whole fixed crop rotated 45 degrees clockwise for reading. The slanted note, its formula, and the complete adjacent Objets label are recorded; clipped adjacent fragments are not completed.',
    'B047-B11': 'Open curved enclosure is drawn. The note breaks pondé-/ration across lines. Small top-edge continuation fragments are retained as doubtful fragments.',
    'B047-B12': 'All graph nodes, multiple edges, loop, rays, isolated point, and numeric labels are drawn. Ray endpoints have no added arrowheads. Upper enclosure continuation is retained.',
    'B047-B13': 'Upper trivalent vertex with 0 and lower one-node loop with 3. Upper diagonal ray exits the fixed rectangle; no inferred continuation.',
    'B047-B14': 'The broad cancelled passage includes the bottom map. The pondération du graphe caption is outside that deletion. Several overwritten words and insertion order remain explicit doubts.',
    'B047-B15': 'Deleted summand and replacement A with cursive ell below are distinguished. The crossed wording to the right is doubtful.',
    'B047-B16': 'Tilde A, arrowed A quotient by sigma, and disjoint-union-shaped sign are copied literally.',
    'B047-B17': 'Three downward maps, deg 2/deg 1 labels, upper brackets, complement, fixed-set superscript sigma, and cancelled strokes on the left are drawn. Circular subscript has a 0/o alternative.',
    'B047-B18': 'Order formula and bracketed explanatory note retained with candidate readings. Right-edge Fl label is only a clipped beginning, not completed from another box.',
    'B047-B19': 'Deleted short code and bip. insertion kept separate. Final i.e. is copied; lower-edge formula fragments are not expanded here.',
    'B047-B20': 'Parentheses and restriction bars follow visible ink, including the final extra-looking closing parenthesis. The fully visible fini insertion below is also recorded. Other lower-edge fragments are not completed.',
    'B047-B21': 'Fini insertion, underlining, deleted symbol between arêtes and libres, and crossed lower ou/sommets-trous phrase are distinguished.',
    'B047-B22': 'Arrow from A with cursive ell subscript to S. Retracing of A is not treated as a deletion.',
    'B047-B23': 'Flèches is underlined; no colon or terminal period has been supplied.',
    'B047-B24': 'Handwritten face number 46, with the 4 lighter than the 6.',
}


def atomic(path, writer):
    tmp = path.with_name(path.name + '.tmp')
    with tmp.open('w', encoding='utf-8', newline='') as f:
        writer(f)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, path)


def main():
    with (INPUTS / 'boxes.tsv').open(encoding='utf-8', newline='') as f:
        boxes = list(csv.DictReader(f, delimiter='\t'))
    assert len(rows) == len(boxes) == 24
    assert [n for n, _ in rows] == [b['box'] for b in boxes]
    assert len({n for n, _ in rows}) == 24
    readings = dict(rows)
    records = []
    for b in boxes:
        n = b['box']
        views = [DISPLAY / (n + '.jpg')]
        views.extend(DISPLAY / x for x in extra_views.get(n, []))
        evidence = ROOT / 'crops' / 'second' / '148_scan047' / (n + '.png')
        assert evidence.is_file()
        assert all(p.is_file() for p in views)
        records.append({
            'box': n,
            'original_rectangle': [int(b[k]) for k in ('x0', 'y0', 'x1', 'y1')],
            'kind': b['kind'],
            'native_evidence': str(evidence),
            'successfully_viewed': True,
            'successful_whole_crop_views': [str(p) for p in views],
            'rotation_degrees_clockwise': 45 if n == 'B047-B10' else 0,
            'observation': observations[n],
            'has_local_uncertainty': r'\unsure{' in readings[n],
        })
    journal = {
        'page': '148_scan047',
        'role': 'independent blind second reader',
        'only_reading_inputs': [str(INPUTS / 'scan.jpg'), str(INPUTS / 'boxes.tsv')],
        'input_sha256': {
            name: hashlib.sha256((INPUTS / name).read_bytes()).hexdigest()
            for name in ('scan.jpg', 'boxes.tsv')
        },
        'native_crop_generation_count': 1,
        'display_policy': 'Only complete fixed crops; enlargement and one whole-crop rotation; no new subrectangles.',
        'unsuccessful_view_attempts': [{
            'boxes': ['B047-B01', 'B047-B02', 'B047-B03'],
            'reason': 'Initial batch output truncated; excluded from seen count and each viewed successfully afterward.',
        }],
        'all_24_boxes_seen_before_final_write': True,
        'final_reading_completed_before_any_comparison': True,
        'other_readings_or_comparisons_opened': False,
        'ocr_external_research_or_tex_compilation_used': False,
        'boxes': records,
    }
    OUT.mkdir(parents=True, exist_ok=True)

    def write_tsv(f):
        w = csv.writer(f, delimiter='\t')
        w.writerow(['box', 'reading'])
        w.writerows(rows)

    atomic(OUT / '148_scan047_second.tsv', write_tsv)
    atomic(OUT / '148_scan047_blind_journal.json',
           lambda f: json.dump(journal, f, ensure_ascii=False, indent=2))
    print('scan047: atomically wrote 24 readings and 24 successful-view records.')


if __name__ == '__main__':
    main()
