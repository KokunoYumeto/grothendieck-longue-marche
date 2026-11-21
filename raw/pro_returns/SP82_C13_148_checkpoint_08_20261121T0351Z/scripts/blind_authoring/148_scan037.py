#!/usr/bin/env python3
"""Independent second reading of scan037, from its fixed image crops only."""
import csv
import json
import os
import tempfile
from pathlib import Path

BASE = Path('/workspace/scratch/8132fe1cca43/work/SP82_C13_148')
INPUT = Path('/workspace/scratch/8132fe1cca43/work/blind_inputs/148_scan037')
DISPLAY = Path('/workspace/scratch/8132fe1cca43/work/blind_display/148_scan037')

R = {
    '148037_folio': r'''\mspage{36}''',
    '148037_opening': r'''le cas est''',
    '148037_lambda_whole': r'''$\lambda=\frac{(\xi+\eta)^2}{\xi\wedge\eta}=\deleted{\unsure{\frac{\xi}{\eta}}}\frac{\xi}{\eta}+\frac{\eta}{\xi}+2$''',
    '148037_iso': r''': iso.''',
    '148037_underlined_word': r'''\uline{non}''',
    '148037_unique': r'''\uline{unique} près.''',
    '148037_condition': r'''La condition \unsure{à|:} \unsure{mettre|autre} sur $\lambda$''',
    '148037_lambda_minus4': r'''$\lambda-4\ne0$ i.e.''',
    '148037_lambda_prime_whole': r'''$\lambda'\overset{\mathrm{def}}{=}\lambda-2^{\unsure{+|4}}=\frac{\xi}{\eta}+\frac{\eta}{\xi}\ne2$''',
    '148037_basis_line': r'''En termes d'une base \deleted{\unsure{de}} $e_1$ de $L_1$,''',
    '148037_basis_fourth_power': r'''$e_1^4=e=\xi\wedge\eta$,''',
    '148037_donnant': r'''donnant une''',
    '148037_basis_square': r'''base $\unsure{\ddot e_1^2|e_1^2}$ de $L_2$,''',
    '148037_pair_inserted': r'''\inserted{paire d'\unsure{élémts|éléments} distincts}''',
    '148037_pair_coordinates': r'''\unsure{par} $\xi_0,\eta_0\in\mathbb C\quad(\xi=\xi_0e_1^2,\eta=\eta_0e_1^2)$,''',
    '148037_product_transition': r'''$\xi_0\eta_0=1$, \unsure{i.e.} en un''',
    '148037_mu_parameter': r'''$\mu=\xi_0+\eta_0\in\mathbb C$, \unsure{satisfais.} à''',
    '148037_mu_membership': r'''$\in\mathbb C$,''',
    '148037_mu_nondegeneracy': r'''$\mu^2-4\ne0$, $\xi_0$ et $\eta_0$ se récupèrent comme''',
    '148037_quadratic': r'''$z^2-\unsure{\mu'|\mu}z+1=0$,''',
    '148037_distinctness_formula': r'''\figure{
\begin{tikzpicture}[x=1cm,y=1cm]
  \node[anchor=base west,inner sep=0pt] at (0.25,0)
    {$\mu^2-4\ne0$ i.e. $\mu^{\deleted{\unsure{2}}}\ne\pm2$};
  \draw[line width=.45pt] (0,0.62) .. controls (-.02,0.14) and (0.01,-.34) .. (.12,-.46)
    .. controls (2.4,-.43) and (5.7,-.32) .. (7.36,-.27)
    .. controls (7.45,-.25) and (7.49,-.18) .. (7.52,-.13);
  \draw[line width=.45pt] (7.73,.67)--(7.69,.08);
\end{tikzpicture}
}''',
    '148037_sexprime': r'''s'exprime par''',
    '148037_inserted2': r'''\figure{
\begin{tikzpicture}[x=1cm,y=1cm]
  \node[inner sep=0pt] at (0,0) {\inserted{$2$}};
  \fill (-.03,.47) ellipse (.025 and .033);
  \fill (-.05,.68) ellipse (.023 and .045);
  \draw[line width=.8pt] (.22,-.57).. controls (.35,-.43) and (.46,-.39)..(.54,-.31);
\end{tikzpicture}
}''',
    '148037_nonzero': r'''\unsure{...ic!} non nulles''',
    '148037_product1': r'''car leur produit est $1$).''',
    '148037_cancelled_Les': r'''\deleted{Les}''',
    '148037_On_recupere': r'''On récupère''',
    '148037_lens_des': r'''l'ens des''',
    '148037_quartic': r'''$z^4-\mu z^2+1=0$''',
    '148037_radicals': r'''$\unsure{\Sigma|I}=\{\pm\sqrt{\frac12(\mu\pm\sqrt{\mu^2-4}}.\}=\{\pm\sqrt{\mu'\pm\sqrt{\mu'^2-1}}\}$''',
    '148037_muprime_margin': r'''\margin{\figure{
\begin{tikzpicture}[x=1cm,y=1cm]
  \node[anchor=base west,inner sep=0pt] at (.12,0) {où $\mu'=\frac12\mu$ i.e.};
  \draw[line width=.5pt] (0,.06)
    .. controls (.18,.55) and (2.62,.94) .. (3.65,.76)
    .. controls (4.28,.69) and (4.12,.03) .. (4.35,-.08)
    .. controls (4.55,-.2) and (5.03,-.18) .. (5.52,-.19);
\end{tikzpicture}
}}''',
}

ENLARGED = {
    '148037_lambda_whole': 3,
    '148037_underlined_word': 7,
    '148037_condition': 3,
    '148037_lambda_prime_whole': 3,
    '148037_basis_line': 2,
    '148037_pair_inserted': 3,
    '148037_pair_coordinates': 2,
    '148037_mu_parameter': 2,
    '148037_mu_nondegeneracy': 2,
    '148037_quadratic': 3,
    '148037_nonzero': 3,
    '148037_radicals': 2,
    '148037_muprime_margin': 4,
    '148037_distinctness_formula': 3,
}

NOTES = {
    '148037_lambda_whole': 'The canceled fraction after the second equality is dense; its proposed underlying reading remains uncertain. The wedge is preserved.',
    '148037_condition': 'The two small strokes following condition may form an accented a or a colon; the following word is also uncertain.',
    '148037_lambda_prime_whole': 'A small upper-right mark after the heavily retraced 2 is retained as an uncertain sign; the final unequal-to-2 is copied literally.',
    '148037_basis_line': 'A short canceled word before e_1 is retained with uncertainty.',
    '148037_basis_square': 'Two small dark strokes above e are visible; their affiliation with e is uncertain and is not silently discarded.',
    '148037_pair_inserted': 'Interlinear phrase and its insertion/callout scope retained. The abbreviation within elements is uncertain. Cropped neighboring baseline fragments are not completed.',
    '148037_pair_coordinates': 'Initial short word is uncertain. Curving material above the pair belongs to the interlinear insertion; no unseen continuation is supplied.',
    '148037_product_transition': 'The short transitional abbreviation has been retained with uncertainty.',
    '148037_mu_parameter': 'Abbreviated satisfais. is uncertain. Complete membership is also separately visible in its overlapping fixed box.',
    '148037_quadratic': 'A long prime-like stroke rises out of the top of the fixed box beside mu. Its affiliation is uncertain; no expected quadratic was substituted.',
    '148037_distinctness_formula': 'The dense small mark above the second mu is treated as a canceled uncertain 2. The visible open-topped, partly detached enclosure is drawn without inventing a top edge.',
    '148037_inserted2': 'The 2, two vertically separated dots, and lower-right stroke fragment are retained graphically without assigning meaning to the dots.',
    '148037_nonzero': 'Leftmost material is clipped and uncertain; non nulles is clear. The uncertain ending is not expanded to an unseen whole word.',
    '148037_radicals': 'Initial symbol is uncertain between Sigma and I. The opening parenthesis in the first radical has no readable closing mate inside this crop; no mate was supplied. Visible point after the first radical retained.',
    '148037_muprime_margin': 'Margin definition and surrounding curved ink stroke retained; no arrowhead is assigned to the curve.',
}

def atomic_text(path, writer):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp = tempfile.mkstemp(prefix=path.name + '.', suffix='.tmp', dir=path.parent)
    try:
        with os.fdopen(fd, 'w', encoding='utf-8', newline='') as stream:
            writer(stream)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temp, path)
    except BaseException:
        if os.path.exists(temp):
            os.unlink(temp)
        raise

with (INPUT / 'boxes.tsv').open(encoding='utf-8', newline='') as stream:
    manifest = list(csv.DictReader(stream, delimiter='\t'))
order = [row['box'] for row in manifest]
assert len(order) == 31 and len(set(order)) == 31
assert set(order) == set(R)

journal = {
    'page': '148_scan037',
    'reader': 'blind_c',
    'reading_inputs': [str(INPUT / 'scan.jpg'), str(INPUT / 'boxes.tsv')],
    'fixed_crop_helper_runs': 1,
    'fixed_crop_count': 31,
    'all_fixed_crops_successfully_inspected': True,
    'comparison_performed': False,
    'ocr_used': False,
    'external_research_used': False,
    'tex_compilation_used': False,
    'additional_subrectangles_created': False,
    'rotations_performed': False,
    'known_failed_display_attempts': [{
        'boxes': ['148037_mu_parameter', '148037_mu_membership', '148037_mu_nondegeneracy', '148037_quadratic'],
        'result': 'Combined image output exceeded context and was truncated; not counted as inspection.',
        'recovery': 'All four complete fixed crops were subsequently displayed successfully in smaller batches.',
    }],
    'boxes': [],
}
for box in order:
    views = [{'path': str(DISPLAY / (box + '.jpg')), 'successful': True, 'scope': 'entire fixed crop', 'rotation_degrees': 0}]
    if box in ENLARGED:
        views.append({'path': str(DISPLAY / (box + '_native.png')), 'successful': True, 'scope': 'entire fixed native crop', 'scale': ENLARGED[box], 'rotation_degrees': 0})
    journal['boxes'].append({
        'box': box,
        'evidence_crop': str(BASE / 'crops' / 'second' / '148_scan037' / (box + '.png')),
        'successfully_inspected': True,
        'views': views,
        'note': NOTES.get(box, 'Complete assigned crop inspected; face ink read independently.'),
    })

def write_tsv(stream):
    writer = csv.writer(stream, delimiter='\t', lineterminator='\n')
    writer.writerow(['box', 'reading'])
    writer.writerows((box, R[box]) for box in order)

atomic_text(BASE / 'second' / '148_scan037_second.tsv', write_tsv)
atomic_text(BASE / 'second' / '148_scan037_blind_journal.json', lambda stream: json.dump(journal, stream, ensure_ascii=False, indent=2))
print('Wrote complete independent scan037 reading: 31 rows and 31 successfully inspected journal entries.')
