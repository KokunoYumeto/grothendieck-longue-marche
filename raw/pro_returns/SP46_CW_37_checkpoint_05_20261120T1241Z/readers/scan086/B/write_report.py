from pathlib import Path
import json

root = Path('/workspace/scratch/006c0e32b2af/out/readers/scan086/B')
reading = (root / 'reading.tex').read_text()

lower_point = reading.split("d'immersion .", 1)[1].split(' Schémas réduits', 1)[0]
vertical = reading.split(r'\noindent\makebox[0pt][l]', 1)[1].split(r'\qquad 4.1.', 1)[0]
vertical = r'\makebox[0pt][l]' + vertical
pair = reading.split('% Two unassigned points lie above the right-hand part of the 6.3 leaders.\n', 1)[1]
pair = r'\makebox[0pt][l]' + pair.split('\n\n', 1)[0].split(r'\makebox[0pt][l]', 1)[1]
correction_i = reading.split('6.10.Image ', 1)[1].split(" d'un schéma", 1)[0]
low_i = correction_i.split('}i', 1)[1].removesuffix('que')

decisions = []
def add(id, place, c, result, diff, cdoubt, unresolved, alternatives, confidence, kind, shows, crop, bbox):
    decisions.append(dict(id=id, place=place, c_reading=c, h_reading=None, reading=result,
                          diff_c=diff, diff_h=False, c_doubt=cdoubt, unresolved=unresolved,
                          alternatives=alternatives, confidence=confidence, kind=kind,
                          scan_shows=shows, crop=crop, bbox=bbox))

add('B086_D00', 'Top centred page number', r'\mspage{541}', r'\mspage{- 541 -}',
    True, False, False, [], 'high', 'omission',
    'A short horizontal dash stands on each side of the three typed digits 541. Both dashes are separate from the digit strokes.',
    '', [804, 52, 954, 87])
add('B086_D01', 'Section 4 heading, small mark below/right of the period',
    r'\unsure{\textsubscript{.}}', lower_point, True, True, True,
    ['Displaced typewriter impression', 'Incidental dark mark; no punctuation assigned'],
    'low', 'drawing or diagram',
    'The normal period is a hollow-edged round typewriter impression. The separate lower-right mark is much smaller, solid, and obliquely elongated. Its observed oval shape and offset are retained without identifying it as a subscript period.',
    'B086_01_s4_lower_mark.jpg', [1195, 340, 1225, 363])
add('B086_D02', 'Between section 4 heading leaders and the leaders of entry 4.1',
    '', vertical, True, False, True,
    ['Accidental ink trace', 'Surface scar or crease', 'Unassigned deliberate stroke'],
    'low', 'drawing or diagram',
    'A long weak irregular vertical trace has a darker triangular upper spot, a darker lower spot and short lower segment, and a much fainter parallel trace at its right. No arrowhead, letter or grouping function is established. The graphic remains explicitly unassigned, and is not asserted to be authored ink.',
    'B086_06_vertical_trace.jpg', [803, 405, 822, 479])
add('B086_D03', 'Entry 5.3, older character beneath d in de',
    r'\deleted{\unsure{a|e}}de', r'\deleted{\unsure{a|e}}de', False, True, True,
    ['a', 'e'], 'low', 'other',
    'The live d has a tall curled ascender and lower bowl. Extra rounded and transverse contours remain inside and to the left of its lower bowl, but their overlap does not decide the earlier a/e. The high curled stroke belongs to the live d, with no separately established older accent.',
    'B086_02_53_under_d.jpg', [617, 976, 647, 1010])
add('B086_D04', 'Entry 5.5, older character beneath f in valuatifs',
    r'valuati\deleted{\unsure{s|b}}fs', r'valuati\deleted{\unsure{s|b}}fs', False, True, True,
    ['s', 'b'], 'low', 'other',
    'The f has its own upper hook, crossbar and baseline foot. A rounded lower loop and extra curved middle contour survive under it; the hidden left and upper portions do not decide whether the older letter was s or b.',
    'B086_03_55_under_f.jpg', [758, 1129, 791, 1162])
add('B086_D05', 'Above the right-hand leaders in entry 6.3',
    '', pair, True, False, True,
    ['Unassigned ink points', 'Incidental surface marks'], 'low', 'drawing or diagram',
    'Two small solid marks lie on a rising left-to-right diagonal above the row of larger hollow typewriter leader dots. The lower-left mark is slightly triangular and the upper-right one is an oblique oval. They are preserved as shapes, with no colon or other punctuation assigned.',
    'B086_07_detached_pair.jpg', [1403, 1507, 1418, 1526])
add('B086_D06', 'Entry 6.10, corrected i and its low residual trace in schématique',
    r'schémat\deleted{\unsure{l|t}}ique', correction_i, True, True, True,
    ['Earlier l', 'Earlier t', 'Low trace may be an underprint foot or an incidental additional impression'],
    'low', 'omission',
    'At the i position, merged vertical, upper and lateral serif fragments do not decide the older l/t. Below the main baseline there is also a short broken dark horizontal trace, with a separated small left spot and a broader lobed right part. It is included with the inseparable correction cluster without assigning it to a particular older letter.',
    'B086_04_610_under_i.jpg', [690, 1869, 719, 1904])
add('B086_D07', 'Entry 6.10, punctuation after schéma',
    r'schéma\unsure{,|.}', r'schéma\unsure{,|.}', False, True, True,
    [',', '.'], 'low', 'other',
    'The mark has an angular dark upper part, a short darker downward-left member and a pale right side. The lower extension supports a comma but the degraded compact impression does not exclude a period. The following capital is not used to settle the ink.',
    'B086_05_610_punctuation.jpg', [1029, 1884, 1045, 1899])

inventory = []
def inv(element, kind, position, first, hand='typewriter'):
    inventory.append(dict(sheet_kind='typescript', hand=hand, element=element, kind=kind,
                          position=position, first_words_or_objects=first, transcribed='yes'))

inv('Typed page number', 'text', 'Top centre', '- 541 -')
inv('Contents entry 3.8', 'text', 'Upper body, two source lines', '3.8. Morphismes universellement ouverts')
inv('Contents entry 3.9', 'text', 'Upper body', '3.9. Morphismes générisants')
inv('Contents entry 3.10', 'text', 'Upper body', '3.10. Morphismes submersifs')
inv('Section 4 heading', 'text', 'Upper body, two source lines', "§ 4. Sous-schémas et morphismes d'immersion")
inv('Unassigned lower point', 'drawing', 'Below/right of the section 4 heading period', 'Small oblique solid oval', 'unnamed hand; writing/material status unresolved')
inv('Unassigned vertical trace', 'drawing', 'Between heading leaders and entry 4.1 leaders', 'Faint irregular vertical trace with darker ends', 'unnamed hand; writing/material status unresolved')
for n, text in [(1,'Sous-schémas'), (2,"Morphismes d'immersion"), (3,"Image réciproque d'un sous-schéma"),
                (4,'Immersions locales et isomorphismes locaux'), (5,'Schémas réduits'),
                (6,"Existence d'un sous-schéma d'espace sous-jacent donné")]:
    inv(f'Contents entry 4.{n}', 'text', 'Upper/middle body', f'4.{n}. {text}')
inv('Section 5 heading', 'text', 'Middle body', '§ 5. Morphismes séparés . Critères valuatifs')
inv('Contents entry 5.1', 'text', 'Middle body', "5.1. Diagonale d'un S-schéma")
inv('Contents entry 5.2', 'text', 'Middle body', '5.2. Morphismes et schémas séparés')
inv('Contents entry 5.3', 'text', 'Middle body', '5.3. Critères de séparation')
inv('Older letter under d', 'deletion', 'Entry 5.3, de', r'\deleted{\unsure{a|e}}')
inv('Contents entry 5.4', 'text', 'Middle body, two source lines', '5.4. Morphismes schématiquement dominants')
inv('Contents entry 5.5', 'text', 'Middle body', '5.5. Critères valuatifs')
inv('Older letter under f', 'deletion', 'Entry 5.5, valuatifs', r'\deleted{\unsure{s|b}}')
inv('Section 6 heading', 'text', 'Lower-middle body', '§ 6. Conditions de finitude relatives')
inv('Contents entry 6.1', 'text', 'Lower body, two source lines', '6.1. Morphismes quasi-compacts et morphismes quasi-séparés')
inv('Contents entry 6.2', 'text', 'Lower body, two source lines', '6.2. Morphismes localement de type fini')
inv('Contents entry 6.3', 'text', 'Lower body, two source lines', '6.3. Morphismes de type fini')
inv('Unassigned point pair', 'drawing', 'Above the right-hand part of entry 6.3 leaders', 'Small lower-left triangular point and upper-right oval', 'unnamed hand; writing/material status unresolved')
inv('Contents entry 6.4', 'text', 'Lower body', '6.4. Schémas de Jacobson et anneaux de Jacobson')
inv('Older d under first J', 'deletion', 'Entry 6.4, first Jacobson', r'\deleted{d}')
inv('Older j under second J', 'deletion', 'Entry 6.4, second Jacobson', r'\deleted{j}')
inv('Contents entry 6.5', 'text', 'Lower body', '6.5. Schémas algébriques et localement algébriques')
inv('Contents entry 6.6', 'text', 'Lower body', "6.6. Détermination locale d'un morphisme")
inv('Older j under n', 'deletion', 'Entry 6.6, Détermination', r'\deleted{j}')
inv('Contents entry 6.7', 'text', 'Lower body', "6.7. Image directe d'un faisceau quasi-cohérent")
inv('Contents entry 6.8', 'text', 'Lower body', '6.8. Prolongement de sections de faisceaux quasi-cohérents')
inv('Contents entry 6.9', 'text', 'Lower body', '6.9. Prolongement des faisceaux quasi-cohérents')
inv('Contents entry 6.10', 'text', 'Lower body, two source lines', "6.10.Image schématique d'un schéma")
inv('Older character under i', 'deletion', 'Entry 6.10, first schématique', r'\deleted{\unsure{l|t}}')
inv('Low residual trace at corrected i', 'drawing', 'Below the corrected i in entry 6.10', 'Broken short horizontal trace', 'typewriter vicinity; trace origin unresolved')
inv('Contents entry 6.11', 'text', 'Bottom body', '6.11.Morphismes quasi-finis')
inv('Archive number recorded only in comment', 'text', 'Bottom left corner', '85', 'unnamed hand')

crops = json.loads((root / 'crop_processing.json').read_text())
for crop in crops:
    crop['requested_deliveries'] = 1
    crop['actual_visual_views'] = 1
(root / 'crop_processing.json').write_text(json.dumps(crops, indent=2) + '\n')

report = dict(
    scan=86, reader='B',
    image_views=[
        '/workspace/scratch/006c0e32b2af/source/SP46_CW_37_scans/B37-04_37_scan086.jpg',
        '/workspace/scratch/006c0e32b2af/source/SP46_CW_37_scans/B37-04_37_scan086_a.jpg',
        '/workspace/scratch/006c0e32b2af/source/SP46_CW_37_scans/B37-04_37_scan086_b.jpg'],
    reading_path=str(root / 'reading.tex'),
    crops=[{k: c[k] for k in ['file','bbox','rotation','reason']} for c in crops],
    decisions=decisions, inventory=inventory,
    notes=(
        'Continuation of a typewritten contents list. The sheet has typed page number - 541 - and archive number 85 at bottom left, the latter recorded only as a comment. '
        'It contains 25 numbered contents entries: 3.8–3.10, 4.1–4.6, 5.1–5.5 and 6.1–6.11, and three section headings: Sous-schémas et morphismes d\'immersion . Schémas réduits; Morphismes séparés . Critères valuatifs; Conditions de finitude relatives. '
        'There is no date, independent chapter title, author signature, or explicit authorial doubt/question mark. Five explicit C doubts remain unresolved. '
        'Six overtyped letter positions are retained as deletions immediately before their live replacement. '
        'Four small graphic loci are represented without an asserted textual meaning: the lower mark at the section 4 period, a faint vertical trace by the leaders, the detached pair above 6.3, and the low trace beneath the 6.10 correction. '
        'These marks are not assumed to be authored handwriting or punctuation; material/accidental interpretations remain available. '
        'H supplies description only, so h_reading is null and diff_h is false throughout. No mathematical proof or computation was attempted. '
        'One whole-image view was followed by one half-a and one half-b view. Half b starts at whole-image y=995; the halves overlap by 160 pixels. '
        'Seven retained crops were each actually viewed once in batches of three, three, and one; no delivery was truncated and no locus was recropped. '
        'Detailed processing and the actual view ledger are saved beside this report. '
        'C-context confirmed, unmarked overprints are reported in math_reading_decisions.'
    ),
    math_reading_decisions=[
        'C-context §4 lower-dot target: the separate low-right oblique mark was inspected and remains unassigned. The normal period is retained; the extra mark is reproduced geometrically rather than asserted to be another period.',
        'C-context 5.3 target: live de is confirmed. The old rounded letter beneath d remains a/e; no older accent is established.',
        'C-context 5.5 target: live valuatifs is confirmed. The old letter beneath f remains s/b.',
        'C-context 6.4 first target: the low round bowl and tall stem of older d remain under the first J; the live reading is Jacobson. This was settled in the half view and not recropped.',
        'C-context 6.4 second target: the separate old dot and descending hooked stroke of j remain under the second J; the live reading is Jacobson. This was settled in the half view and not recropped.',
        'C-context 6.6 target: the old dot and descender beneath n support deleted j; the live word is Détermination. This was settled in the half view and not recropped.',
        'C-context 6.10 correction target: live schématique is retained, with the older l/t unresolved. The short detached low trace belonging to the crowded correction area is additionally preserved as an unassigned graphic.',
        'C-context 6.10 punctuation target: the comma/period remains unresolved, with comma first. Capital Adhérence is not used as proof of a period.',
        'Entry 5.1 has an ordinary typed capital S in S-schéma: one continuous outline, with no independent double strike, and a separate baseline hyphen.',
        'The section signs are ordinary typed §; the section numerals are 4, 5 and 6. All entry-number digits and decimal/full-stop separators were checked in order. The page number is 541 with two flanking horizontal dashes.',
        'The regular leaders are rows of typewriter points. Entries 3.10 and 6.8 end without leaders. The hyphen in quasi-séparés is retained when joining the source line break.'
    ],
    check_events=[],
    notation=[
        dict(sign='Ordinary typewritten S', latex='S', evidence='Single continuous typewriter curve; no separate doubled outline.', place='Entry 5.1, S-schéma'),
        dict(sign='Section signs', latex=r'\S\ 4.; \S\ 5.; \S\ 6.', evidence='Opposed curved section-sign lobes followed by a numeral and low point.', place='Three section headings'),
        dict(sign='Contents leaders', latex=r'\dotfill', evidence='Regularly spaced low, hollow-edged rounded typewriter impressions.', place='All entries except 3.10 and 6.8; all three section headings'),
        dict(sign='Unassigned lower point', latex=lower_point, evidence='Small slanted solid oval below and right of a normal typed period.', place='Section 4 heading'),
        dict(sign='Unassigned vertical trace', latex=vertical, evidence='Weak irregular upright with darker end marks and a faint right parallel trace.', place='Between §4 heading leaders and entry 4.1 leaders'),
        dict(sign='Unassigned point pair', latex=pair, evidence='Small lower-left triangular point and upper-right slanted oval, distinct from larger leader dots.', place='Above right-hand leaders in entry 6.3'),
        dict(sign='Unassigned low correction trace', latex=low_i, evidence='Small left spot and a short lobed right horizontal trace beneath the correction baseline.', place='Below i of first schématique in entry 6.10'),
        dict(sign='Uncertain punctuation', latex=r'\unsure{,|.}', evidence='Compact angular impression with a dark downward member, insufficient to decide comma versus period.', place='Entry 6.10 after schéma')
    ],
    abbreviations=[],
    slips=[
        'Overtyped letter positions are preserved, not silently normalized: a/e beneath d (5.3), s/b beneath f (5.5), d beneath first J and j beneath second J (6.4), j beneath n (6.6), and l/t beneath i (6.10).',
        'No space separates the final point of 6.10. or 6.11. from the following word; both joins are retained.'
    ],
    completion='Complete independent reading of the entire assigned page, including all 25 entries, three section headings, page number with flanking dashes, archive-number comment, six overtyped positions, all leaders, and four unassigned graphic loci. All five explicit C doubts and all confirmed C-context targets are recorded. No OCR, external source, other page, other reader, delegation, TeX compilation, repeated whole/half image view, or repeated crop view was used.'
)
(root / 'report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
