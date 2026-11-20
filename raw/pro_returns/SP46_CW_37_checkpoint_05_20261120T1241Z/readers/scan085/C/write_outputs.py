from pathlib import Path
import json

root = Path('/workspace/scratch/006c0e32b2af')
out = root / 'out/readers/scan085/C'
source = root / 'source/SP46_CW_37_scans/B37-04_37_scan085.jpg'

margin_graphic = r'''\margin{\figure{\handwritten{\unsure{%
\begin{tikzpicture}[x=1mm,y=1mm]
\draw[line width=0.45pt]
 (-0.6,6.3) .. controls (0.5,6.6) and (1.6,7.0) .. (2.5,6.6)
 .. controls (3.7,6.2) and (3.6,5.4) .. (3.2,4.5)
 .. controls (3.1,3.0) and (2.5,1.8) .. (2.0,0.6)
 .. controls (1.6,-0.2) and (2.4,-0.4) .. (3.0,-0.2)
 .. controls (3.5,0.0) and (3.7,-0.1) .. (3.9,-0.2);
\fill (5.2,-3.1) ellipse[x radius=0.48,y radius=0.18];
\end{tikzpicture}%
}}}}'''

cancelled_rows = r'''\figure{%
\begin{tikzpicture}[x=0.115mm,y=0.115mm]
\node[anchor=base west,inner sep=0pt,outer sep=0pt,font=\ttfamily] (oldrow) at (0,0)
 {\deleted{2.4. Fonctions constructibles}\deleted{\mbox{............................}}};
\node[anchor=base west,inner sep=0pt,outer sep=0pt,font=\ttfamily] (oldnumber) at (0,-50)
 {\deleted{2.5.}};
\handwritten{\draw[line width=0.45pt]
 (35,36) .. controls (31,18) and (17,-19) .. (12,-40)
 .. controls (18,-30) and (45,13) .. (52,28)
 .. controls (48,7) and (41,-25) .. (34,-41)
 .. controls (45,-32) and (77,-3) .. (87,5)
 .. controls (84,-5) and (72,-24) .. (77,-30)
 .. controls (86,-33) and (110,1) .. (120,12)
 .. controls (117,2) and (108,-15) .. (114,-19)
 .. controls (123,-22) and (149,2) .. (158,13)
 .. controls (156,4) and (143,-11) .. (151,-15)
 .. controls (163,-20) and (199,11) .. (215,19)
 .. controls (211,11) and (204,-3) .. (212,-8)
 .. controls (226,-19) and (272,19) .. (292,24)
 .. controls (305,25) and (316,39) .. (332,34)
 .. controls (343,28) and (341,15) .. (355,18)
 .. controls (375,19) and (389,36) .. (406,37)
 .. controls (416,37) and (423,22) .. (435,18)
 .. controls (455,17) and (482,31) .. (499,31)
 .. controls (515,31) and (526,14) .. (542,14)
 .. controls (564,10) and (606,15) .. (641,12)
 .. controls (676,10) and (708,14) .. (738,13)
 .. controls (774,11) and (801,15) .. (836,13)
 .. controls (872,12) and (898,17) .. (927,16)
 .. controls (961,18) and (1001,12) .. (1036,13)
 .. controls (1074,12) and (1118,12) .. (1152,13);}
\end{tikzpicture}%
}'''

reading = r'''\scanpage{85}
\mspage{- 538 -}

\begin{center}
TABLE DES MATIERES
\end{center}

\noindent AVANT-PROPOS \dotfill

\noindent INTRODUCTION\dotfill

\noindent CHAPITRE \unsure{O|0} .- Préliminaires\dotfill

\noindent\quad \S\ 1. Foncteurs représentables\dotfill

\noindent\qquad 1.1. Foncteurs représentables\dotfill

\noindent\qquad 1.2. Produits fibrés dans une catégorie\dotfill

\noindent\qquad 1.3. Changement de base\dotfill

\noindent\qquad 1.4. Noyaux ; morphisme diagonal\dotfill

\noindent\qquad 1.5. Foncteurs adjoints\dotfill

\noindent\qquad 1.6. Structures algébriques dans les catégories\dotfill

\noindent\qquad 1.7. Morphismes fonctoriels représentables\dotfill

\noindent\quad \S\ 2. Compléments de topologie\dotfill

\noindent\qquad 2.1. Espaces irréductibles\dotfill

\noindent\qquad 2.2. Espaces localement noethériens\dotfill

\noindent\qquad 2.3. Ensembles quasi-constructibles et ensembles constructibles\dotfill

''' + margin_graphic + '\n' + cancelled_rows + r'''

\noindent\qquad 2.4. Ensembles constructibles dans les espaces noethériens

\noindent\qquad 2.5? Fonctions constructibles\dotfill

\noindent\qquad 2.6. Parties très denses d'un espace topologique\dotfill

\noindent\qquad 2.7. Quasi-homéomorphismes\dotfill

\noindent\qquad 2.8. Espaces de Jacobson\dotfill

\noindent\qquad 2.9. Espace sobre associé à un espace topologique\dotfill

\noindent\qquad 2.10.Applications ouvertes en un point \dotfill

\noindent\quad \S\ 3. Compléments sur les faisceaux\dotfill

\noindent\qquad 3.1. Faisceaux à valeurs dans une catégorie\dotfill

\noindent\qquad 3.2. Préfaisceaux sur une base d'ouverts\dotfill

\noindent\qquad 3.3. Recollement de faisceaux\dotfill

\noindent\qquad 3.4. Images directes de préfaisceaux\dotfill

\noindent\qquad 3.5. Images réci\deleted{r}p\deleted{p}roque\unsure{ss|\deleted{s}s|s} de préfaisceaux\dotfill

\noindent\qquad 3.6. Faisceaux simples et faisceaux localement simples\dotfill

\noindent\qquad 3.7. Images réciproques de faisceaux de groupes ou d'anneaux\dotfill

% archive sheet number: 84
'''
(out / 'reading.tex').write_text(reading)

decisions = []

def decide(id, place, c_reading, reading, diff_c, c_doubt, unresolved, alternatives,
           confidence, kind, scan_shows, bbox, crop=''):
    decisions.append(dict(id=id, place=place, c_reading=c_reading, h_reading=None,
                          reading=reading, diff_c=diff_c, diff_h=False,
                          c_doubt=c_doubt, unresolved=unresolved,
                          alternatives=alternatives, confidence=confidence,
                          kind=kind, scan_shows=scan_shows, crop=crop, bbox=bbox))

decide('C85-01', 'Typed pagination at top centre', r'\mspage{538}',
       r'\mspage{- 538 -}', True, False, False, [], 'high', 'omission',
       'A short horizontal typed stroke stands on each side of 538. The digits have the upper bar and lower bowl of 5, two right lobes of 3, and two closed bowls of 8. The two flanking strokes are absent from C’s pagination argument.',
       [791, 55, 944, 96])

decide('C85-02', 'Chapter character after CHAPITRE', r'\unsure{O|0}',
       r'\unsure{O|0}', False, True, True, ['O', '0'], 'medium',
       'misread symbol or index',
       'One closed, slightly vertically elongated oval has no slash, interior dot, or other distinguishing stroke. The enlarged shape does not settle letter O versus numeral 0. The following low point and horizontal dash are separate and retained.',
       [425, 329, 457, 369], 'C01_chapter_character.jpg')

decide('C85-03', 'Left margin beside the two cancelled subsection rows',
       r'\margin{\handwritten{?}}', margin_graphic, True, False, True,
       ['A question mark with an unusually long oblique stem and rightward foot',
        'A curved marginal grouping stroke with a separate lower point or short dash'],
       'medium', 'drawing or diagram',
       'The upper mark begins with a short rising rightward stroke, curves down, descends obliquely to the left, and turns right at its foot. A separate short horizontal dark mark lies appreciably below and to the right. The observed shape is secure; its reading as a question mark, rather than a grouping stroke plus detached mark, is not fixed by the strokes. Both components are reproduced, and their semantic uncertainty is explicit.',
       [244, 1116, 292, 1193], 'C02_left_marginal_sign.jpg')

decide('C85-04', 'Continuous cancellation over old 2.4 and old 2.5, extending along the leader',
       r'\noindent\qquad \deleted{2.4. Fonctions constructibles}\deleted{\mbox{............................}}' + '\n\n' + r'\noindent\qquad \deleted{2.5.}',
       cancelled_rows, True, False, False, [], 'high', 'drawing or diagram',
       'A continuous nonuniform stroke makes several steep down-and-up runs through the two number fields, then broad low loops through Fonctions, two shallower humps through constructibles, and a long nearly horizontal continuation across the dotted leader. C preserves deletion state but does not reproduce this linked graphic. No additional independent machine cancellation is securely separable from the pen stroke.',
       [333, 1097, 1493, 1188], 'C03_cancelled_rows_stroke.jpg')

decide('C85-05', 'Question character after the live 2.5', '2.5?', '2.5?',
       False, False, False, [], 'high', 'other',
       'A curved upper hook and short central descending stem stand over a round low dot. The regular character width, alignment, and ink texture match the adjacent typewritten number; no separate handwritten addition or independently recoverable underlying period is visible. The question character is retained as typed. This is a reviewed C-context target, not an explicit C unsure macro.',
       [330, 1256, 420, 1287], 'C04_live_2_5_punctuation.jpg')

decide('C85-06', '3.5, the two adjacent overtyped characters within réciproques',
       r'\deleted{\unsure{r}}p\deleted{p}r', r'\deleted{r}p\deleted{p}r',
       True, True, False, [], 'high', 'misread word',
       'At the first corrected position, a low r foot remains at the text baseline in addition to the live p’s descending stem and lower foot; the upper shoulder is merged with the p bowl. At the next position, the live r has its baseline foot, while a separate lower descender and foot from p remain below it. The separate baseline-versus-descender traces support the r/p underprints, so the explicit doubt on the first deleted r is removed.',
       [662, 1847, 711, 1878], 'C05_reciproques_overprint.jpg')

decide('C85-07', '3.5, final s-shaped traces of réciproques', 'roques',
       r'roque\unsure{ss|\deleted{s}s|s}', True, False, True,
       ['ss: two live s impressions', 'An underlying or erased s followed by the live s',
        'One s struck again with a substantial horizontal displacement'],
       'medium', 'omission',
       'After e there is a dark s with an upper curve, central turn and lower curve, and immediately to its right a paler second s-shaped outline with its own upper and lower curves. This additional outline becomes visible in the same retained whole-word crop used for the overprints. No distinct strike-through decides whether it is an extra live s, a residual cancelled s, or a displaced repeat impression of the same letter. The ambiguity is therefore marked rather than silently reduced to a single s.',
       [783, 1846, 817, 1873], 'C05_reciproques_overprint.jpg')

inventory = []
def inv(element, kind, position, first, hand='typewriter'):
    inventory.append(dict(sheet_kind='typescript', hand=hand, element=element,
                          kind=kind, position=position,
                          first_words_or_objects=first, transcribed='yes'))

inv('Pagination', 'text', 'Top centre, y55–96', '- 538 -')
inv('Title', 'text', 'Upper centre, y126–158', 'TABLE DES MATIERES')
inv('Contents entry', 'text', 'y203–232', 'AVANT-PROPOS; dotted leader')
inv('Contents entry', 'text', 'y270–300', 'INTRODUCTION; dotted leader')
inv('Chapter heading', 'text', 'y334–366', 'CHAPITRE O/0 .- Préliminaires; dotted leader')
inv('Section heading', 'text', 'y400–436', '§ 1. Foncteurs représentables; dotted leader')
for no, title, pos in [
    ('1.1.', 'Foncteurs représentables', 'y469–501'),
    ('1.2.', 'Produits fibrés dans une catégorie', 'y517–550'),
    ('1.3.', 'Changement de base', 'y569–601'),
    ('1.4.', 'Noyaux ; morphisme diagonal', 'y619–650'),
    ('1.5.', 'Foncteurs adjoints', 'y670–702'),
    ('1.6.', 'Structures algébriques dans les catégories', 'y720–752'),
    ('1.7.', 'Morphismes fonctoriels représentables', 'y771–804')]:
    inv('Subsection entry', 'text', pos, f'{no} {title}; dotted leader')
inv('Section heading', 'text', 'y838–874', '§ 2. Compléments de topologie; dotted leader')
inv('Subsection entry', 'text', 'y906–938', '2.1. Espaces irréductibles; dotted leader')
inv('Subsection entry', 'text', 'y955–988', '2.2. Espaces localement noethériens; dotted leader')
inv('Two-line subsection entry', 'text', 'y1006–1085', '2.3. Ensembles quasi-constructibles et ensembles constructibles; dotted leader')
inv('Marginal hook and detached low point', 'drawing', 'Left of cancelled rows, x244–292 y1116–1193', 'Long curved hook with a rightward foot and a separate low horizontal point; function uncertain', 'unnamed hand')
inv('Cancelled subsection entry', 'deletion', 'y1108–1140', '2.4. Fonctions constructibles; cancelled dotted leader')
inv('Cancelled bare number', 'deletion', 'y1157–1188', '2.5.')
inv('Linked cancellation stroke', 'drawing', 'x333–1493 y1097–1188, over both cancelled rows and the first leader', 'Steep diagonal runs, rounded loops, and a long horizontal continuation', 'unnamed hand')
inv('Replacement subsection entry', 'text', 'y1206–1240', '2.4. Ensembles constructibles dans les espaces noethériens; no leader')
inv('Replacement subsection entry', 'text', 'y1257–1290', '2.5? Fonctions constructibles; dotted leader')
for no, title, pos in [
    ('2.6.', "Parties très denses d'un espace topologique", 'y1308–1340'),
    ('2.7.', 'Quasi-homéomorphismes', 'y1358–1391'),
    ('2.8.', 'Espaces de Jacobson', 'y1409–1441'),
    ('2.9.', 'Espace sobre associé à un espace topologique', 'y1458–1493'),
    ('2.10.', 'Applications ouvertes en un point', 'y1509–1542')]:
    inv('Subsection entry', 'text', pos, f'{no} {title}; dotted leader')
inv('Section heading', 'text', 'y1580–1615', '§ 3. Compléments sur les faisceaux; dotted leader')
for no, title, pos in [
    ('3.1.', 'Faisceaux à valeurs dans une catégorie', 'y1645–1679'),
    ('3.2.', "Préfaisceaux sur une base d'ouverts", 'y1694–1728'),
    ('3.3.', 'Recollement de faisceaux', 'y1746–1778'),
    ('3.4.', 'Images directes de préfaisceaux', 'y1795–1828')]:
    inv('Subsection entry', 'text', pos, f'{no} {title}; dotted leader')
inv('Subsection entry with overprints', 'text', 'y1845–1880', '3.5. Images réciproques de préfaisceaux; terminal s traces uncertain; dotted leader')
inv('First overtyped letter', 'deletion', '3.5, x662–687 y1847–1878', 'r under p')
inv('Second overtyped letter', 'deletion', '3.5, x686–711 y1847–1878', 'p under r')
inv('Additional pale terminal letter impression, state uncertain', 'text', '3.5, x783–817 y1846–1873', 'Two overlapping s-shaped outlines; live/underprint/repeat-impression alternatives marked')
inv('Subsection entry', 'text', 'y1896–1929', '3.6. Faisceaux simples et faisceaux localement simples; dotted leader')
inv('Two-line subsection entry', 'text', 'y1947–2033', "3.7. Images réciproques de faisceaux de groupes ou d'anneaux; dotted leader")
inv('Archive number recorded in comment', 'text', 'Lower-left corner, x174–222 y2070–2114', '84', 'unnamed hand')

manifest = json.loads((out / 'crop_manifest.json').read_text())
for item in manifest:
    item['requested_deliveries'] = 1
    item['actual_visual_views'] = 1
(out / 'crop_manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')

report = dict(
    scan=85,
    reader='C',
    image_views=[str(source), str(source.with_name(source.stem + '_a.jpg')),
                 str(source.with_name(source.stem + '_b.jpg'))],
    reading_path=str(out / 'reading.tex'),
    crops=[{k: item[k] for k in ['file', 'bbox', 'rotation', 'reason']} for item in manifest],
    decisions=decisions,
    inventory=inventory,
    notes=(
        'One typescript page headed TABLE DES MATIERES, with typed pagination - 538 - and archive number 84. '
        'No date, signature, or named author appears. The contents list AVANT-PROPOS, INTRODUCTION, a chapter heading with an unresolved O/0 glyph, '
        'and three section headings. There are 24 live numbered subsection entries and two cancelled rows. '
        'The live 2.5? explicitly carries a question character; the separate marginal hook and low point may also express a question, but their function is not secure. '
        'The earlier 2.4. Fonctions constructibles and bare 2.5. are cancelled by a linked wavy stroke; the following live 2.4 and 2.5? remain in their observed order. '
        'The corrected r/p characters in 3.5 are preserved as deleted underprints immediately before their live replacements. A further pale s-shaped impression at that word’s end is newly marked as uncertain in textual/deletion status. '
        'H is description only: h_reading is null and diff_h is false in every decision. Its historical identification and speculative attribution were not used as image evidence. '
        'The whole page and each half were actually viewed once in that order; the lower-half offset is y=997. Five retained crops were then viewed once each in batches of three and two. '
        'Processing parameters and delivery/view counts are retained in crop_manifest.json; the initial open-locus list is retained in inspection_plan.json.'),
    math_reading_decisions=[
        'No mathematical assertion, proof, computation, or cited background result is stated or checked on this contents page; check_events is empty.',
        'The chapter O/0 ambiguity is retained from the closed oval’s strokes. The preferred O is not converted to the historically expected numeral.',
        'All three section signs, the 26 subsection number fields including the two cancelled fields, and their points were inspected individually. No numerical renumbering is supplied.',
        'The live 2.5? has a hook, stem, and low dot whose alignment and impression match the typed numbering. No separate deleted full stop is inferred.',
        'The title has no grave accent over MATIERES. The title’s unmarked capitals are ordinary typewriter letters.',
        'The semicolon in 1.4 has an upper point and a lower comma-shaped component. The chapter punctuation is a low point followed by a separate horizontal dash.',
        'The no-space join 2.10.Applications and the leader-free live 2.4 entry are preserved. The text wraps of 2.3 and 3.7 are paragraph-internal line breaks, not added hyphens.',
        'Both adjacent r/p overprint positions in 3.5 were read from their independent baseline and descending traces. No reconstruction of the typist’s temporal sequence beyond the visible live/underprint distinction was used.'
    ],
    check_events=[],
    notation=[
        dict(sign='Chapter character', latex=r'\unsure{O|0}',
             evidence='Closed upright oval without an internal or crossing discriminator.',
             place='Chapter heading'),
        dict(sign='Typed section sign and decimal numbering', latex=r'\S\ 1.; \S\ 2.; \S\ 3.; 2.10.',
             evidence='Paired section-sign curves; separate numerals and low full stops, with two digits after the final 2 point.',
             place='Section headings and final subsection of section 2'),
        dict(sign='Numbering question character', latex='2.5?',
             evidence='Curved hook and descending central stem over a distinct round point; typewriter alignment and texture.',
             place='Live Fonctions constructibles entry'),
        dict(sign='Marginal graphic of unresolved function', latex=margin_graphic,
             evidence='Upper bent stroke, long left-slanting descent, rightward foot, and detached low horizontal point.',
             place='Left of cancelled 2.4 and 2.5'),
        dict(sign='Uncertain terminal letter impressions', latex=r'roque\unsure{ss|\deleted{s}s|s}',
             evidence='Dark s plus paler right-shifted s-shaped outline; state cannot be fixed.',
             place='End of réciproques in 3.5')
    ],
    abbreviations=[],
    slips=[
        'Two r/p underprints are visible in the corrected réciproques of 3.5; both remain in deleted state in the reading.',
        'The live 2.5? is preserved with its actual question character, not replaced by the expected full stop.',
        'The extra pale s-shaped terminal impression in 3.5 is not silently removed or treated as a securely established typing error; its alternatives are explicit.'
    ],
    completion=(
        'Complete independent reading of scan 085: every typed word, accent, numbering field, punctuation mark, leader, correction and cancelled row, '
        'together with the handwritten cancellation, marginal graphic and archive number, was inspected. '
        'Every substantive C difference, both explicit C unsure loci, and each new uncertainty is reported with whole-image coordinates. '
        'No OCR, external text, other page, peer reading, or TeX compilation was used. All H collation fields are null/false.')
)
(out / 'report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'reading': str(out / 'reading.tex'), 'report': str(out / 'report.json'),
                  'decisions': len(decisions), 'inventory_rows': len(inventory),
                  'crops': len(manifest)}, ensure_ascii=False))
