#!/usr/bin/env python3
"""Independent blind scan042 reading; only its image, boxes and fixed crops read."""
import csv
import json
import os
import tempfile
from pathlib import Path

BASE = Path('/workspace/scratch/8132fe1cca43/work/SP82_C13_148')
INPUT = Path('/workspace/scratch/8132fe1cca43/work/blind_inputs/148_scan042')
DISPLAY = Path('/workspace/scratch/8132fe1cca43/work/blind_display/148_scan042')

R = {
    'S42-heading': r'''opérations de recollage / \unsure{sommes}''',
    'S42-diamonds': r'''\diagram{
\begin{tikzpicture}[x=.015cm,y=-.015cm,>=stealth,inner sep=1pt]
  \node at (81,40) {$\deleted{\unsure{B}}$};
  \node at (140,42) {$\unsure{\mathbb C|\mathcal C}$};
  \node at (49,147) {$S\unsure{\mathbb C|\mathcal C}$};
  \node at (276,133) {$D\unsure{\mathbb C|\mathcal C}$};
  \node at (161,267) {$SD\unsure{\mathbb C|\mathcal C}$};
  \node at (548,49) {$\unsure{\mathbb E|\mathcal E}$};
  \node at (474,149) {$s\unsure{\mathbb E|\mathcal E}$};
  \node at (656,144) {$d\unsure{\mathbb E|\mathcal E}$};
  \node at (566,274) {$sd\unsure{\mathbb E|\mathcal E}$};
  \draw[line width=.9pt] (112,64)--(76,113);
  \draw[line width=.9pt] (179,64)--(222,107);
  \draw[line width=.9pt] (55,198)--(105,252);
  \draw[line width=.9pt] (254,182)--(214,246);
  \draw[line width=.9pt] (521,80)--(494,111);
  \draw[line width=.9pt] (582,79)--(616,130);
  \draw[line width=.9pt] (468,193)--(510,265);
  \draw[line width=.9pt] (660,197)--(614,259);
  \draw[->,line width=.55pt] (232,29)--(437,29);
  \draw[->,line width=.45pt] (248,269)--(459,267);
  \draw[->,line width=.35pt] (262,84).. controls (310,84) and (355,101)..(408,112);
  \draw[line width=.35pt] (102,130).. controls (134,122) and (156,118)..(172,120);
  \fill (102,130)--(108,123)--(112,128)--cycle;
  \draw[line width=.3pt,opacity=.48] (325,153).. controls (407,220) and (555,186)..(608,169);
  \fill (599,172).. controls (606,174) and (609,169)..(610,166)
    --(606,164)--(605,168)--cycle;
  \node[anchor=base west] at (449,358) {types combinatoires};
\end{tikzpicture}
}''',
    'S42-top-deleted': r'''$\deleted{\unsure{B}}$''',
    'S42-objects-braces': r'''\figure{
\begin{tikzpicture}[x=.015cm,y=-.015cm,inner sep=0pt]
  \node[anchor=base west] at (176,45) {objets; diagrammes};
  \node[anchor=base west] at (87,107) {cordes de raccord (ou de recollage)};
  \node[anchor=base west] at (86,146) {cordes de découpage};
  \node[anchor=base west] at (90,178) {Sommets de \uline{marquage}};
  \node[anchor=base west] at (560,161) {périphériques};
  \node[anchor=base west] at (566,195) {intérieurs};
  \node[anchor=base west] at (60,219) {cycles marqués et non marqués};
  \draw[line width=.6pt] (36,6).. controls (20,1) and (26,75)..(17,111)
    .. controls (14,121) and (10,120)..(7,120)
    .. controls (14,127) and (22,119)..(22,140)
    .. controls (20,187) and (21,231)..(39,235);
  \draw[line width=.5pt] (32,61)--(32,78);
  \draw[line width=.5pt] (32,164)--(32,178);
  \draw[line width=.5pt] (71,88).. controls (63,92) and (76,110)..(71,120)
    .. controls (67,124) and (66,120)..(66,120)
    .. controls (74,124) and (67,138)..(74,147);
  \draw[line width=.5pt] (551,149).. controls (545,168) and (545,182)..(553,197);
\end{tikzpicture}
}''',
    'S42-objects-heading': r'''objets; diagrammes''',
    'S42-parenthetical': r'''\figure{
\begin{tikzpicture}[x=1cm,y=1cm,inner sep=0pt]
  \node[anchor=base west] at (.24,.55) {périphériques};
  \node[anchor=base west] at (.36,0) {intérieurs};
  \draw[line width=.55pt] (.05,.9).. controls (-.03,.55) and (-.03,.16)..(.10,-.1);
\end{tikzpicture}
}''',
    'S42-sommets': r'''Sommets de \uline{marquage}''',
    'S42-condition-whole': r'''\figure{
\begin{tikzpicture}[x=1cm,y=1cm,inner sep=0pt]
  \node[anchor=base west] at (.28,.8) {condition \deleted{\unsure{de|D}} ``anabélienne''};
  \node[anchor=base west] at (1.18,0) {ou de ``Stabilité''};
  \draw[line width=.6pt] (.15,1.23)--(0,1.23)--(0,.5)--(.17,.5);
  \draw[line width=.6pt] (6.2,.39)--(6.35,.39)--(6.35,-.39)--(6.18,-.39);
\end{tikzpicture}
}''',
    'S42-types-note': r'''\margin{types combinatoires}''',
    'S42-catalogue-heading': r'''Catalogue opérations $+$ structures''',
    'S42-items123-whole': r'''\figure{
\begin{tikzpicture}[x=.013cm,y=-.013cm,inner sep=0pt,>=stealth]
  \node[anchor=base west] at (12,38) {1)};
  \node[anchor=base west] at (90,31) {\unsure{Somme|Sommes}};
  \node[anchor=base west] at (16,106) {2)};
  \node[anchor=base west] at (97,91) {gommage (partiel) du marquage};
  \node[anchor=base west] at (20,164) {3)};
  \node[anchor=base west] at (97,149) {Surmarquage};
  \draw[line width=.6pt] (66,13).. controls (53,45) and (68,115)..(69,150)
    .. controls (69,176) and (62,188)..(45,187)
    .. controls (54,188) and (59,190)..(60,197);
  \draw[<->,line width=.7pt] (835,76)--(835,123);
\end{tikzpicture}
}''',
    'S42-items45-whole': r'''\figure{
\begin{tikzpicture}[x=.012cm,y=-.012cm,inner sep=0pt,>=stealth]
  \node[anchor=base west] at (13,55) {4)};
  \node[anchor=base west] at (95,45) {découpage (partiel)};
  \node[anchor=base west] at (18,124) {5)};
  \node[anchor=base west] at (105,110) {amalgamation ou recollage};
  \node[anchor=base west] at (747,111) {\deleted{\unsure{avec} (\unsure{le} \illegible{1} \unsure{de}}};
  \node[anchor=base west] at (765,73) {\inserted{Sans gommage !}};
  \node[anchor=base west] at (1137,111) {)};
  \draw[line width=.6pt] (51,0).. controls (60,10) and (58,86)..(58,155);
  \draw[line width=.6pt] (85,138)--(308,135);
  \draw[<->,line width=.7pt] (1211,39)--(1211,100);
\end{tikzpicture}
}''',
    'S42-item6': r'''bouchage de trous ($=$ gommage de cycles de raccord)''',
    'S42-number-6': r'''6)''',
    'S42-number-7': r'''7)''',
    'S42-item7': r'''gommage de cordes intérieures''',
    'S42-functors-line': r'''foncteurs et iso ``twist'' ''',
    'S42-folio': r'''\mspage{41}''',
}

ENLARGED = {
    'S42-heading': 3,
    'S42-diamonds': 2,
    'S42-objects-braces': 3,
    'S42-parenthetical': 4,
    'S42-condition-whole': 3,
    'S42-items123-whole': 3,
    'S42-items45-whole': 3,
    'S42-item6': 3,
    'S42-item7': 3,
}

NOTES = {
    'S42-heading': 'Final heading word read as sommes, retained as doubtful.',
    'S42-diamonds': 'Two diamonds transcribed in actual TikZ. Double-stroked C/E letterforms remain uncertain between blackboard and calligraphic alphabets. Plain thick edges stay plain. Two ambiguous small endpoint patches are drawn as geometry, without assigning them an arrow direction. Pale lower connecting curve retained as a lighter solid line. Dense canceled symbol has best candidate B.',
    'S42-top-deleted': 'Dense cancellation; best doubtful symbol candidate B retained, not replaced by an illegible-word marker.',
    'S42-objects-braces': 'Large and small braces, two short adjacent strokes, open parenthesis and two-line parenthetical retained. Underlining treated as underlining, not cancellation. Faint background impressions were not used to invent text.',
    'S42-parenthetical': 'Both rows read, with the visible opening parenthesis only; no closing parenthesis added.',
    'S42-condition-whole': 'Canceled material after condition is doubtful between de and a D-like form. Quotes retained, and staggered left/right brackets drawn literally.',
    'S42-items123-whole': 'Somme/Sommes remains uncertain. Visible partial long-brace segment and bidirectional vertical arrow retained.',
    'S42-items45-whole': 'Correction above the struck baseline preserved as an insertion. Underlying phrase remains uncertain, with one physically unreadable canceled word. The visible opening parenthesis is in the canceled layer and the final closing parenthesis survives. The underline covers only the observed first part of amalgamation and is drawn to preserve that span. Long-brace fragment and vertical bidirectional arrow retained.',
    'S42-item6': 'Read from entire fixed crop; no text outside this rectangle supplied.',
    'S42-item7': 'Read from entire fixed crop; no text outside this rectangle supplied.',
    'S42-folio': 'Handwritten folio 41 is readable; clipped bottom-edge stroke is not completed as an unseen note.',
}

def atomic_text(path, writer):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=path.name + '.', suffix='.tmp', dir=path.parent)
    try:
        with os.fdopen(fd, 'w', encoding='utf-8', newline='') as stream:
            writer(stream)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    except BaseException:
        if os.path.exists(temporary):
            os.unlink(temporary)
        raise

with (INPUT / 'boxes.tsv').open(encoding='utf-8', newline='') as stream:
    boxes = list(csv.DictReader(stream, delimiter='\t'))
order = [row['box'] for row in boxes]
assert len(order) == 18 and len(set(order)) == 18
assert set(order) == set(R)

journal = {
    'page': '148_scan042',
    'reader': 'blind_c',
    'reading_inputs': [str(INPUT / 'scan.jpg'), str(INPUT / 'boxes.tsv')],
    'fixed_crop_helper_runs': 1,
    'fixed_crop_count': 18,
    'all_fixed_crops_successfully_inspected': True,
    'comparison_performed': False,
    'ocr_used': False,
    'external_research_used': False,
    'tex_compilation_used': False,
    'additional_subrectangles_created': False,
    'rotations_performed': False,
    'failed_display_attempts': [],
    'boxes': [],
}
for box in order:
    views = [{'path': str(DISPLAY / (box + '.jpg')), 'successful': True, 'scope': 'entire fixed crop', 'rotation_degrees': 0}]
    if box in ENLARGED:
        views.append({'path': str(DISPLAY / (box + '_native.png')), 'successful': True, 'scope': 'entire fixed native crop', 'scale': ENLARGED[box], 'rotation_degrees': 0})
    journal['boxes'].append({
        'box': box,
        'evidence_crop': str(BASE / 'crops' / 'second' / '148_scan042' / (box + '.png')),
        'successfully_inspected': True,
        'views': views,
        'note': NOTES.get(box, 'Entire assigned crop inspected independently; readable face ink retained.'),
    })

def write_tsv(stream):
    writer = csv.writer(stream, delimiter='\t', lineterminator='\n')
    writer.writerow(['box', 'reading'])
    writer.writerows((box, R[box].rstrip()) for box in order)

atomic_text(BASE / 'second' / '148_scan042_second.tsv', write_tsv)
atomic_text(BASE / 'second' / '148_scan042_blind_journal.json', lambda stream: json.dump(journal, stream, ensure_ascii=False, indent=2))
print('Wrote complete independent scan042 reading: 18 rows and 18 successfully inspected journal entries.')
