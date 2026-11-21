"""Blind second transcription of scan038, from its assigned fixed crops only.

No witnesses, first readings, comparison records, OCR, external research,
or TeX compilation were used. All 33 fixed crops were successfully viewed.
"""
import csv
import json
import os
from pathlib import Path

ROOT = Path('/workspace/scratch/8132fe1cca43/work/SP82_C13_148')
OUT = ROOT / 'second'
INPUTS = Path('/workspace/scratch/8132fe1cca43/work/blind_inputs/148_scan038')
DISPLAY = Path('/workspace/scratch/8132fe1cca43/work/blind_display/148_scan038')


title_addition = r'''\figure{\begin{tikzpicture}[x=.014cm,y=-.014cm,line cap=round,line join=round,>=stealth,font=\scriptsize]
\clip (0,0) rectangle (330,127);
\node at (39,32) {\inserted{$\Sigma$}};
\node[anchor=west] at (115,30) {\inserted{sur $K$ de}};
\node at (173,93) {\unsure{:|à}};
\node at (244,104) {$5$};
\draw[line width=.45pt] (16,50)
 .. controls (44,59) and (85,57) .. (102,89);
\draw[line width=.55pt] (102,89) -- (100,13);
\draw[line width=.45pt] (311,45)
 .. controls (339,56) and (268,62) .. (253,75);
\draw[->,line width=.6pt] (253,75)
 .. controls (246,78) and (243,85) .. (238,89);
\draw[line width=.45pt] (306,63)
 .. controls (269,43) and (213,49) .. (218,98);
\draw[line width=.45pt] (0,112) -- (186,112);
\end{tikzpicture}}'''


rows = [
    ('148038_title_line',
        r"\uline{Autom d'ordre deux d'une sphère holomorphe}"
        + '\n' + title_addition),
    ('148038_title_pts', r'\uline{pts marqués}'),
    ('148038_opening_autom',
        r"autom \inserted{$\unsure{\alpha|\sigma}$} d'ordre $2$,"),
    ('148038_fixed_point_exclusion',
        r'\inserted{$\unsure{\Sigma|I}$ en outre privée des pts fixes de $\unsure{\sigma|\alpha}$.}'),
    ('148038_Donc_cel', r'Donc cel. revient à la donnée'),
    ('148038_item_a_first',
        r"\unsure{a}) D'une sphère hol. $\Sigma$, \unsure{un|son} autom \inserted{$\unsure{g|\sigma}$} d'ordre $2$"),
    ('148038_appelant', r'et un pt fixe marqué --- Appelant celui-ci'),
    ('148038_fixed_points',
        r"$\infty$, et l'autre pt fixe $0$, cela revient à la"),
    ('148038_torseur_definition', r'$T_1(=\Sigma\setminus\{0,\infty\})$'),
    ('148038_vector_line',
        r"$\mathbb{C}^{*}$, i.e. d'une droite vectorielle complexe $L_1$ ($T_1=L_1^{*}$)"
        + '\n' + r'\inserted{(distinctes)}'),
    ('148038_distinctes', r'\inserted{(distinctes)}'),
    ('148038_involution_group', r'$\{\pm1\}\subset\mathbb{C}^{*}$ opérant'),
    ('148038_T1_line', r'$T_1=L_1^{*}$'),
    ('148038_square_identification',
        r'$T_1=L_1^{*}$' + '\n'
        + r'Introduisant $T_2=T^{\wedge2}$'
        + r'\inserted{$\unsure{\simeq|\cong}L_2^{*}$, et $L_2=L_1^{\otimes2}$,}'
        + r' cela revient à la donnée'
        + '\n' + r'\inserted{$\{\unsure{\xi|l},\eta\}$}'),
    ('148038_pair_coordinates', r'\inserted{$\{\unsure{\xi|l},\eta\}$}'),
    ('148038_pair_target', r'$T_{\unsure{2|1}}$.'),
    ('148038_product_display',
        r'$e=\xi\wedge\eta=\eta\wedge\xi\in T_4=T^{\wedge4}\simeq L_4^{*}$'
        + '\n' + r'(où $L_{\unsure{4|1}}=L_1^{\otimes4}$)'),
    ('148038_isomorphism', r'iso $T^{\wedge4}\simeq1_{\mathbb{C}^{*}}$'),
    ('148038_deT', r'\inserted{de $T$}'),
    ('148038_fourth_root_group',
        r'de $\mathbb{C}^{*}:\quad\mu_4(\mathbb{C}_{*})\simeq\mathbb{Z}/4\mathbb{Z}$.'),
    ('148038_product_membership',
        r'$e=\xi\wedge\eta$\inserted{$\in T_4$} \unsure{et}'),
    ('148038_sum_membership', r'$\xi+\eta\in\unsure{L_2|t_2}$,'),
    ('148038_condition', r'$(\xi+\eta)^{\unsure{2}}-4\xi\wedge\eta\ne0$'),
    ('148038_cancelled_un', r'\deleted{\unsure{un}}. . Notons'),
    ('148038_cancelled_expansion',
        r'\deleted{$\xi^2+\eta^2-2\xi\eta\unsure{\ne|+}$}'),
    ('148038_T2_reduction', r'$T_2$'),
    ('148038_sign_group', r'$\mathbb{C}^{*}:\{\pm1\}$,'),
    ('148038_bibase', r'\unsure{e} bibase $\pm\sqrt{e}$, \unsure{donne|donc}'),
    ('148038_elt', r'\unsure{elt|élém}'),
    ('148038_sign_qualification', r'au signe près,'),
    ('148038_dont', r'dont'),
    ('148038_cancelled_final_square', r'\deleted{$(\xi+\eta)^2$}'),
    ('148038_foliation', r'\mspage{37}'),
]

native_views = {
    '148038_title_line': 2,
    '148038_opening_autom': 3,
    '148038_fixed_point_exclusion': 2,
    '148038_item_a_first': 2,
    '148038_product_display': 2,
    '148038_fourth_root_group': 2,
    '148038_bibase': 2,
    '148038_elt': 3,
    '148038_cancelled_expansion': 3,
    '148038_sum_membership': 3,
}

observations = {
    '148038_title_line': 'Main title is underlined. Above its right end are Sigma and sur K de, connected by a bent insertion mark and curved strokes. The descending curved stroke has a dark arrow-like end directed towards the 5. The small lower mark before 5 may be colon or à; the geometry and labels are reproduced in TikZ. No text was supplied beyond the rectangle.',
    '148038_title_pts': 'Underline extends under the abbreviation pts and marqués, passing the descender. No expansion of pts.',
    '148038_opening_autom': 'Small symbol inserted above the gap before d\'ordre resembles alpha or sigma (also an a-like cursive form); local alternatives retained.',
    '148038_fixed_point_exclusion': 'Whole line is interlinear insertion. Initial capital is ambiguous between Sigma and serif I. Final automorphism symbol is uncertain. Small top/bottom border fragments from adjacent writing are not completed.',
    '148038_Donc_cel': 'Cel. is retained as an abbreviation. The small accented mark before la is read à.',
    '148038_item_a_first': 'List letter is clipped and only its lower mark is visible. Short word after Sigma is uncertain. Inserted automorphism letter has a descending stroke and is not silently harmonized with the other inserted symbol.',
    '148038_appelant': 'Reads Appelant; long dash is kept. Descenders intersect neighbouring line fragments at the lower border.',
    '148038_fixed_points': 'Infinity and 0 are both visible; final la is inside the right edge. Upper pieces of the previous line are clipped.',
    '148038_torseur_definition': 'T has subscript 1. Braces enclose 0 and infinity; set difference is one oblique stroke.',
    '148038_vector_line': 'The neighbouring insertion (distinctes) is visible beneath vectorielle and is recorded as a separate inserted line, without moving it into the vector-space phrase.',
    '148038_distinctes': 'Inserted parenthesized distinctes. Fragments of preceding and following main lines are cut at the top/bottom edges.',
    '148038_square_identification': 'Upper T_1=L_1^* is included. The base T on the right side of T_2=T^{wedge 2} has no discernible subscript. The added L_2 identification sits above a long bent insertion leader. Isomorphism glyph remains uncertain. Pair in braces at the bottom is the top of another insertion and has a doubtful first coordinate.',
    '148038_pair_coordinates': 'First coordinate is partly top-clipped and looks like xi or l; second resembles eta. Braces and comma retained.',
    '148038_pair_target': 'Subscript is heavily overwritten; 2 is leading reading, 1 retained as alternative. A following full stop is visible.',
    '148038_product_display': 'Both inter-coordinate products are wedge-shaped and the equality in reversed order is kept literally. Powers on T are wedge 4; power on L_1 is tensor 4. Lower L subscript is 4-like but could be 1; no mathematical repair. Small lower-left adjacent-word fragment is cropped.',
    '148038_isomorphism': 'Iso is an unexpanded abbreviation. Right side is a 1 with C-star subscript; no arrow is substituted for the written simeq.',
    '148038_deT': 'De T is above a broad insertion caret. Adjacent black mark at upper-right and lower-line tips are clipped.',
    '148038_fourth_root_group': 'First C has a high star. Star next to C inside mu_4 parentheses is visibly low and is recorded as a subscript rather than moved upwards. Faint blue reversed printing is reverse-side show-through and excluded.',
    '148038_product_membership': 'Membership in T_4 is written above the main product with a curved insertion mark. Only an et-like fragment is visible at the right border; it remains uncertain.',
    '148038_sum_membership': 'Target letter is unusually thick and overdrawn, with a top crossbar and L-like foot. L_2/t_2 alternatives retained rather than normalizing to the expected space. Correction order cannot be established from the strokes.',
    '148038_condition': 'Small power after the closing parenthesis is partly clipped; 2 is tentative. Wedge between xi and eta is retained.',
    '148038_cancelled_un': 'Short struck word tentatively un. Two distinct dark punctuation dots remain to its right before Notons; both recorded.',
    '148038_cancelled_expansion': 'Long strike crosses the full visible expansion. No wedge is clearly visible between the last xi and eta. Final crossed symbol could be ne or plus. No zero is visible in this rectangle. A following q-like fragment at right and upper V-shaped tip are clipped.',
    '148038_sign_group': 'C-star, colon, brace-enclosed plus/minus 1, and trailing comma are visible.',
    '148038_bibase': 'The first visible letter is a clipped e-like fragment and was not expanded to a complete word. Bibase has no clearly written hyphen. Final word is uncertain between donne and donc.',
    '148038_elt': 'Small cursive abbreviation remains uncertain; no confident expansion to élément is supplied.',
    '148038_sign_qualification': 'Au signe près and comma. A dark upper-border stroke overlaps the accent area but does not establish cancellation.',
    '148038_dont': 'Dont is visible with a heavy terminal t and retraced middle stroke; no definite deletion.',
    '148038_cancelled_final_square': 'Two heavy crossing strokes cancel the parenthesized sum and its raised 2. The raised numeral remains visible above the main strike.',
    '148038_foliation': 'Pencil foliation reads 37; middle crossbar of 7 is visible.',
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
    assert len(rows) == len(boxes) == 33
    assert [name for name, _ in rows] == [box['box'] for box in boxes]
    assert len(set(name for name, _ in rows)) == 33
    OUT.mkdir(parents=True, exist_ok=True)

    def write_tsv(stream):
        writer = csv.writer(stream, delimiter='\t')
        writer.writerow(['box', 'reading'])
        writer.writerows(rows)

    journal = {
        'page': '148_scan038',
        'protocol': 'Independent blind reading from assigned scan/box list only, via the fixed evidence crops. No OCR, outside research, other readings or comparison, and no TeX compilation.',
        'fixed_crops_created_once': True,
        'all_boxes_successfully_viewed': True,
        'box_count': 33,
        'failed_display_attempts': [],
        'rotation_degrees_ccw': [],
        'magnification_policy': 'All alternate displays resize the entire saved fixed crop. No new subrectangles.',
        'boxes': [],
    }
    for box, (name, reading) in zip(boxes, rows):
        views = [str(DISPLAY / (name + '.jpg'))]
        if name in native_views:
            views.append(str(DISPLAY / (name + '_native' + str(native_views[name]) + '.jpg')))
        journal['boxes'].append({
            'box': name,
            'rect': [int(box[key]) for key in ('x0', 'y0', 'x1', 'y1')],
            'native_evidence': str(ROOT / 'crops' / 'second' / '148_scan038' / (name + '.png')),
            'successfully_viewed': True,
            'successful_views': views,
            'local_uncertainty': r'\unsure{' in reading,
            'observation': observations.get(name, 'Successfully viewed in the fixed crop; no additional local observation.'),
        })
    atomic(OUT / '148_scan038_second.tsv', write_tsv)
    atomic(OUT / '148_scan038_blind_journal.json',
           lambda stream: json.dump(journal, stream, ensure_ascii=False, indent=2))
    print('Atomically wrote 33 independent readings and the procedural journal.')


if __name__ == '__main__':
    main()
