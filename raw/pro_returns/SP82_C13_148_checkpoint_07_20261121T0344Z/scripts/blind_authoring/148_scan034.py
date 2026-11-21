"""Independent blind second reading of the fixed rectangles for scan034.

Reading sources: only the assigned scan and its box list, through the fixed
crops and whole-crop displays. No recognition software or comparison input.
"""
import csv
import json
import os
from pathlib import Path

ROOT = Path('/workspace/scratch/8132fe1cca43/work/SP82_C13_148')
OUT = ROOT / 'second'
INPUTS = Path('/workspace/scratch/8132fe1cca43/work/blind_inputs/148_scan034')
DISPLAY = Path('/workspace/scratch/8132fe1cca43/work/blind_display/148_scan034')


def fig(width, height, ink, scale='.025'):
    return (
        r'\figure{\begin{tikzpicture}[x=' + scale + 'cm,y=-' + scale
        + r'cm,line cap=round,line join=round,>=stealth]' + '\n'
        + rf'\clip (0,0) rectangle ({width},{height});' + '\n'
        + ink.strip() + '\n' + r'\end{tikzpicture}}'
    )


sphere5 = fig(147, 145, r'''
\draw[line width=.75pt] (14,77)
 .. controls (15,46) and (39,9) .. (75,7)
 .. controls (113,2) and (132,25) .. (132,61)
 .. controls (133,84) and (125,114) .. (112,126)
 .. controls (101,138) and (78,137) .. (52,133)
 .. controls (29,132) and (13,108) .. (13,85)
 .. controls (11,80) and (12,78) .. (14,77);
\draw[line width=.8pt] (14,80)
 .. controls (24,96) and (75,99) .. (105,95)
 .. controls (115,94) and (122,92) .. (124,90);
\draw[line width=.55pt] (25,68)
 .. controls (32,66) and (37,68) .. (42,63)
 .. controls (47,60) and (56,66) .. (63,63)
 .. controls (68,60) and (78,62) .. (84,64);
\draw[line width=.5pt] (103,65) -- (106,64) -- (108,67);
\draw[line width=.45pt] (107,72) -- (107,74);
\draw[line width=.7pt] (29,114)
 .. controls (39,118) and (54,119) .. (65,117);
\fill (27,68) circle[radius=1.5pt];
\fill (73,62) circle[radius=1.6pt];
\fill (118,73) circle[radius=1.6pt];
\fill (40,94) circle[radius=1.5pt];
\fill (93,96) circle[radius=1.5pt];
''')

sphere4 = fig(207, 189, r'''
\draw[line width=.75pt] (102,14)
 .. controls (71,15) and (27,41) .. (19,80)
 .. controls (11,96) and (18,112) .. (18,128)
 .. controls (21,151) and (37,164) .. (55,169);
\draw[line width=.75pt] (59,169)
 .. controls (79,177) and (115,182) .. (144,171)
 .. controls (171,163) and (179,130) .. (179,104)
 .. controls (180,70) and (167,32) .. (143,22)
 .. controls (132,17) and (119,13) .. (109,12);
\draw[line width=.8pt] (17,104)
 .. controls (31,124) and (102,127) .. (146,121)
 .. controls (163,119) and (172,116) .. (179,110);
\draw[line width=.5pt] (36,82) -- (43,84);
\draw[line width=.5pt] (49,81)
 .. controls (56,76) and (62,82) .. (69,78);
\draw[line width=.5pt] (74,79) -- (79,80);
\draw[line width=.5pt] (88,79)
 .. controls (96,76) and (101,77) .. (105,79);
\draw[line width=.5pt] (147,81) -- (153,82);
\draw[line width=.45pt] (165,91) -- (171,94);
\fill (133,78) circle[radius=.5pt];
\fill (110,22) circle[radius=1.5pt];
\fill (67,79) circle[radius=1.5pt];
\fill (154,87) circle[radius=1.5pt];
\fill (47,114) circle[radius=1.5pt];
\fill (124,121) circle[radius=1.6pt];
\fill (111,0) circle[radius=.7pt];
\draw[line width=.6pt] (172,189)
 .. controls (178,184) and (180,173) .. (181,166)
 .. controls (184,181) and (181,187) .. (186,190);
''')

sphere3 = fig(218, 193, r'''
\draw[line width=.75pt] (104,16)
 .. controls (128,8) and (157,18) .. (173,35)
 .. controls (191,52) and (195,77) .. (193,102)
 .. controls (192,128) and (183,151) .. (167,166)
 .. controls (150,180) and (122,180) .. (99,175)
 .. controls (64,173) and (42,164) .. (31,145)
 .. controls (23,130) and (19,113) .. (22,98)
 .. controls (25,68) and (45,42) .. (72,25)
 .. controls (86,16) and (100,9) .. (104,16);
\draw[line width=.8pt] (23,116)
 .. controls (64,127) and (130,115) .. (193,101);
\draw[line width=.55pt] (35,88)
 .. controls (46,89) and (60,85) .. (68,79)
 -- (78,79);
\draw[line width=.45pt] (89,77) -- (93,76);
\draw[line width=.45pt] (109,75) -- (115,75);
\draw[line width=.45pt] (130,73) -- (136,71) -- (140,73);
\draw[line width=.5pt] (156,70)
 .. controls (166,68) and (170,74) .. (174,75)
 .. controls (181,77) and (185,81) .. (187,84);
\draw[line width=.45pt] (42,149)
 .. controls (55,159) and (68,160) .. (79,157);
\fill (106,24) circle[radius=1.6pt];
\fill (48,85) circle[radius=1.6pt];
\fill (174,74) circle[radius=1.6pt];
\fill (106,114) circle[radius=1.7pt];
\fill (118,166) ellipse[x radius=1.7pt,y radius=1.2pt];
''')

autom_d5 = fig(492, 133, r'''
\node[anchor=west] at (35,65) {autom.};
\node[anchor=west] at (275,64) {\unsure{est}};
\node at (421,66) {$D_5$};
\draw[line width=.5pt] (375,30)
 .. controls (393,4) and (444,7) .. (466,26)
 .. controls (493,48) and (489,97) .. (467,116)
 .. controls (443,139) and (398,139) .. (370,119)
 .. controls (344,102) and (341,65) .. (354,44);
\draw[line width=.65pt] (32,134)
 .. controls (57,91) and (113,86) .. (135,134);
''', scale='.015')

orbit_arc = fig(142, 103, r'''
\draw[line width=.55pt] (33,103)
 .. controls (52,91) and (81,91) .. (100,103);
''', scale='.018')


rows = [
    ('148034_top_number', r'\mspage{\unsure{1}}'),
    ('148034_title_abbrev', r'\unsure{gén.}\textsuperscript{t}'),
    ('148034_title_cancel', r'\deleted{\unsure{courbe}}'),
    ('148034_title_alg', r'alg clos'),
    ('148034_title_characteristic', r'\unsure{de} car. $0$'),
    ('148034_definition_count', r'Card $K=5$'),
    ('148034_definition_autom', r'autom.'),
    ('148034_definition_G', r'\inserted{$G$}'),
    ('148034_definition_identity', r'; \uline{$1$}.'),
    ('148034_cancelled_order', r"\deleted{l'ordre de $g\ne1$ est}"),
    ('148034_max_autom', r'autom.'),
    ('148034_cancelled_order5',
        r"\deleted{$\unsure{\forall|\exists}\,g$ d'ordre $5$}"
        + '\n' + r'\unsure{p.} ex. \unsure{tr}'),
    ('148034_cancelled_ilest', r"et \deleted{qu'il est}"),
    ('148034_order_condition',
        r"\deleted{il est}\inserted{si l'ordre est $\nu$},"),
    ('148034_quotient_display',
        r"$K=K^g\amalg$ orbites d'ordre $\nu$, donc $2\leq\nu\leq5$"),
    ('148034_operation_note',
        r"\margin{l'opération \unsure{usuelle} de $\mu_\nu$ sur $\widehat{\mathbb{G}_m}$}"),
    ('148034_case1_number_order', r'\textcircled{1} $\nu=5$'),
    ('148034_case1_orbit', r'$\mu_5$-\unsure{lib|Ens}' + '\n' + orbit_arc),
    ('148034_case1_action', r'de $\mu_5$ opérant sur $\mathbb{P}^{1}_{k}$'),
    ('148034_case1_autom_D5', autom_d5),
    ('148034_case1_isom',
        r'À isom près, $\unsure{\exists}$ un seul tel cas.'),
    ('148034_pentagon_note',
        r"\margin{\unsure{Structure|Struct.re} \unsure{pentagon.le|pentagonale} sur $I$ (``pentagone'')}"),
    ('148034_sphere5', sphere5),
    ('148034_case2_number_order', r'\textcircled{2} $\nu=4$'),
    ('148034_case2_deleted',
        r'\deleted{$K^{\unsure{g}}=\operatorname{Card}I^g=1,$}'),
    ('148034_case2_replacement', r'\inserted{$K^g=\{P\}$}'),
    ('148034_case2_mu4', r'$\mu_4$'),
    ('148034_case2_relative_action', r'laquelle $\mu_4$'),
    ('148034_case2_pole', r'pôle $\unsure{\infty|0}$'),
    ('148034_case2_group',
        r'autom. est $\mathbb{Z}/4\mathbb{Z}\simeq\mu_4(k)$'),
    ('148034_square_note', r"\margin{``pyramide carrée''}"),
    ('148034_sphere4', sphere4),
    ('148034_case3_number_order_Alors', r'\textcircled{3} $\nu=3$, Alors'),
    ('148034_case3_deleted_symbol', r'\deleted{$\unsure{\Sigma_2}$}'),
    ('148034_case3_fixed_count', r'Card $K^g=2$,'),
    ('148034_case3_donc', r'\inserted{donc $K^g=\Sigma^g$,}'),
    ('148034_case3_I', r'$\unsure{K|I}\setminus K^g$'),
    ('148034_case3_J', r'\inserted{$=J$}'),
    ('148034_case3_est', r'est un\unsure{e} \unsure{orbite},'),
    ('148034_case3_struck_group', r'\deleted{Le groupe des aut\unsure{o}}'),
    ('148034_case3_replacement',
        r'\inserted{\unsure{pris|fixé} \unsure{par} \unsure{symétries} $\mu_3$.}'),
    ('148034_case3_colon', r"l'\unsure{équivalent|équivalence} : elle"),
    ('148034_case3_Ens_count', r'$\operatorname{Ens}(B)$ des ens $J$ de Card $3$'),
    ('148034_association_A', r'À $J$ on associe'),
    ('148034_association_deleted_symbol',
        r'$\Sigma_J\ \deleted{\unsure{g|G}}\Omega$'),
    ('148034_association_inclusion', r'$(\Phi_J\subset\Sigma_{\unsure{5|g}}$'),
    ('148034_association_ens', r'ens des'),
    ('148034_association_pour', r'pour corr.'),
    ('148034_association_1to1', r'$1-1$'),
    ('148034_ending_omega', r"d'un $\omega(J)$"),
    ('148034_ending_field', r'$\unsure{k|K}=\mathbb{C}$'),
    ('148034_ending_group', r'autom. est $\unsure{D_3|B_3}$'),
    ('148034_partition_note',
        r'\margin{Une partition $2$ et $3$ (\unsure{par ordre} de richesse en symétries)}'),
    ('148034_bitetrahedron_note', r"\margin{``bitétraèdre''}"),
    ('148034_sphere3', sphere3),
    ('148034_folio', r'\mspage{33}'),
]

rotations = {
    '148034_operation_note': [-57, -43],
    '148034_pentagon_note': [-43],
    '148034_square_note': [-45],
    '148034_partition_note': [-48],
    '148034_bitetrahedron_note': [-48],
}
native3 = {
    '148034_title_abbrev', '148034_title_characteristic',
    '148034_order_condition', '148034_case1_isom',
    '148034_case3_replacement', '148034_case3_colon',
    '148034_case3_est', '148034_association_deleted_symbol',
}
repeat_original = {
    '148034_cancelled_order5', '148034_case1_orbit',
    '148034_case1_autom_D5', '148034_case2_pole',
}
observations = {
    '148034_top_number': 'A single thick vertical handwritten stroke; numeral 1 is probable.',
    '148034_title_abbrev': 'Initial g and raised terminal t; middle letters and accent are uncertain.',
    '148034_title_cancel': 'One word cancelled by a horizontal line. Courbe is a tentative recovery.',
    '148034_title_characteristic': 'Left-hand de-like strokes overlap vertically. Whether this is a cancelled/replaced de is unresolved; no unambiguous cancellation scope was invented. A descender from above is clipped at the top.',
    '148034_definition_count': 'The large set letter has prominent upper and lower bars and diagonal K-like branches.',
    '148034_definition_G': 'G above an insertion caret; neighbouring lower and right strokes are cut at the rectangle border.',
    '148034_cancelled_order': 'Horizontal cancellation extends through the full phrase. The inequality and 1 are above the baseline.',
    '148034_cancelled_order5': 'Initial quantified symbol is ambiguous between a handwritten forall and exists. A separate lower line is clipped; only the visible short fragments are supplied.',
    '148034_cancelled_ilest': 'Et precedes the cancelled qu\'il est. Top-edge fragments of the replacement are clipped.',
    '148034_order_condition': 'Replacement is above the crossed il est; its upper ascenders touch the crop boundary.',
    '148034_operation_note': 'Whole-crop clockwise rotations by 57 and 43 degrees. Usuelle remains tentative. Hat covers G_m.',
    '148034_case1_orbit': 'Letters after the hyphen remain uncertain; visible dot and loop favour lib but Ens is retained as an alternative. A partial circled outline at the bottom is reproduced.',
    '148034_case1_autom_D5': 'D_5 is encircled. The small intervening word is tentative. A separate lower circle/sphere outline is only partially in the rectangle and is reproduced as an arc.',
    '148034_case1_isom': 'The sign between près and un is uncertain. At the bottom edge, the upper strokes of a different insertion are clipped; no lower portions outside this rectangle were supplied.',
    '148034_pentagon_note': 'Whole-crop clockwise rotation 43 degrees. Structure abbreviation and pentagonale abbreviation are uncertain; set letter looks like serif I.',
    '148034_sphere5': 'Irregular enclosing outline; five dark points, three on the interrupted rear side and two on the solid front curve. Includes the short lower-left internal curve. No arrowheads.',
    '148034_case2_deleted': 'The cancelled line includes a partly top-clipped superscript at the first K; the letter after Card looks like serif I.',
    '148034_case2_pole': 'The terminal symbol is heavily superposed; infinity is the leading reading, zero an alternative. The ink does not establish a dependable cancellation order.',
    '148034_square_note': 'Whole-crop clockwise rotation 45 degrees. Both quotation marks and the accent in carrée are represented.',
    '148034_sphere4': 'Irregular sphere outline; four equatorial points and one upper point. Rear curve has distinct interrupted strokes; front curve is solid. A dot cut by the top border and part of an adjacent lower-right handwritten stroke are included. Faint interior grey marks were treated as show-through.',
    '148034_case3_deleted_symbol': 'Heavily crossed symbol; Sigma with subscript 2 is tentative.',
    '148034_case3_donc': 'Superscript on the right-hand Sigma appears g. A thin insertion leader exits the bottom/right boundary; no arrowhead is visible inside the box.',
    '148034_case3_I': 'First set letter has K-like diagonals but is close to the writer\'s serif I; alternative retained. Set difference is a single oblique stroke.',
    '148034_case3_est': 'Last word has its upper parts clipped at the top edge; orbite is tentative and no missing upper strokes are inferred.',
    '148034_case3_struck_group': 'Two cancellation strokes. Final word is cut at the right boundary; only aut plus tentative o is given.',
    '148034_case3_replacement': 'Very uncertain replacement words; first looks pris/fixé, next par, and the following long word is tentatively symétries. These are explicitly doubtful readings. Crossed text from the preceding line is also partly visible along the top border.',
    '148034_case3_colon': 'The central word may be équivalent or équivalence. Colon is visible. Upper tips of a separate lower line are clipped.',
    '148034_association_deleted_symbol': 'Sigma has subscript J. Crossed middle glyph and its exact relationship to the surviving Omega-shaped right part remain uncertain. Proposed cancelled g/G is tentative.',
    '148034_association_inclusion': 'Opening parenthesis, Phi with subscript J, inclusion, and Sigma with a subscript. Subscript resembles 5 but also the writer\'s g; alternative retained. No closing parenthesis is visible.',
    '148034_association_ens': 'First word is partly cut along the lower border.',
    '148034_ending_field': 'Left letter could be lowercase k or uppercase K. Right C has a doubled vertical stroke.',
    '148034_ending_group': 'The upper part of the group letter is clipped; D_3 and B_3 remain alternatives.',
    '148034_partition_note': 'Whole-crop clockwise rotation 48 degrees. Right end of the parenthesis phrase is close to the original border; par ordre is tentative. Small fragments from the next marginal note remain clipped at the bottom.',
    '148034_bitetrahedron_note': 'Whole-crop clockwise rotation 48 degrees. Main quoted word reads bitétraèdre; the previous margin note has clipped de/sym- fragments at the upper border.',
    '148034_sphere3': 'Irregular outline; two polar points and three equatorial points. Rear equatorial line is interrupted; front line is solid and rises rightwards. Short lower-left internal curve retained; no arrowheads.',
}


def atomic(path, writer):
    temporary = path.with_name(path.name + '.tmp')
    with temporary.open('w', encoding='utf-8', newline='') as stream:
        writer(stream)
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temporary, path)


def main():
    with (INPUTS / 'boxes.tsv').open(encoding='utf-8', newline='') as stream:
        boxes = list(csv.DictReader(stream, delimiter='\t'))
    assert len(rows) == len(boxes) == 56
    assert [name for name, _ in rows] == [box['box'] for box in boxes]
    assert len(set(name for name, _ in rows)) == 56
    OUT.mkdir(parents=True, exist_ok=True)

    def write_tsv(stream):
        writer = csv.writer(stream, delimiter='\t')
        writer.writerow(['box', 'reading'])
        writer.writerows(rows)

    journal = {
        'page': '148_scan034',
        'protocol': 'Independent blind reading; assigned scan and box list only. Fixed crops made once. No OCR, other readings, external research, or TeX compilation.',
        'all_boxes_successfully_viewed': True,
        'box_count': 56,
        'failed_display_attempts': [
            'Initial batch of the first eight image outputs was truncated; none was counted. All eight were subsequently viewed successfully in smaller batches.'
        ],
        'border_policy': 'Partial writing is noted without completing unseen portions beyond the original fixed rectangle. No new subrectangles were made.',
        'boxes': [],
    }
    for box, (name, reading) in zip(boxes, rows):
        views = [str(DISPLAY / (name + '.jpg'))]
        if name in repeat_original:
            views.append(str(DISPLAY / (name + '.jpg')))
        for angle in rotations.get(name, []):
            views.append(str(DISPLAY / (name + '_rot' + str(angle) + '.jpg')))
        if name in native3:
            views.append(str(DISPLAY / (name + '_native3.jpg')))
        journal['boxes'].append({
            'box': name,
            'rect': [int(box[key]) for key in ('x0', 'y0', 'x1', 'y1')],
            'native_evidence': str(ROOT / 'crops' / 'second' / '148_scan034' / (name + '.png')),
            'successfully_viewed': True,
            'successful_views': views,
            'rotation_degrees_ccw': rotations.get(name, []),
            'local_uncertainty': r'\unsure{' in reading,
            'observation': observations.get(name, 'Successfully inspected in the fixed crop; no additional local observation.'),
        })
    atomic(OUT / '148_scan034_second.tsv', write_tsv)
    atomic(OUT / '148_scan034_blind_journal.json',
           lambda stream: json.dump(journal, stream, ensure_ascii=False, indent=2))
    print('Wrote 56 independent readings and viewing journal atomically.')


if __name__ == '__main__':
    main()
