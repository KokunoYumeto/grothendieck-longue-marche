"""Independent second reading of scan041: assigned image/boxes only.

All 28 fixed crops were inspected. Whole saved crops only were resized or
rotated. No OCR, witnesses, other readings, research, or TeX compilation.
"""
import csv
import json
import os
from pathlib import Path

ROOT = Path('/workspace/scratch/8132fe1cca43/work/SP82_C13_148')
OUT = ROOT / 'second'
INPUTS = Path('/workspace/scratch/8132fe1cca43/work/blind_inputs/148_scan041')
DISPLAY = Path('/workspace/scratch/8132fe1cca43/work/blind_display/148_scan041')


def picture(kind, width, height, ink, scale='.017'):
    return (
        '\\' + kind + r'{\begin{tikzpicture}[x=' + scale + 'cm,y=-' + scale
        + r'cm,line cap=round,line join=round,>=stealth,font=\scriptsize]' + '\n'
        + rf'\clip (0,0) rectangle ({width},{height});' + '\n'
        + ink.strip() + '\n' + r'\end{tikzpicture}}'
    )


date_frame = picture('figure', 400, 145, r'''
\node[font=\large] at (205,61) {Oct.\ $\unsure{4|9}$\ $83$.};
\draw[line width=.65pt] (19,11) -- (14,127)
 .. controls (22,142) and (83,132) .. (167,123)
 -- (372,112)
 .. controls (381,101) and (379,68) .. (378,14);
''', '.022')

diagram04 = picture('diagram', 730, 630, r'''
\node[font=\normalsize] at (251,25) {$\sigma_0,\sigma_1$};
\node[font=\normalsize] at (88,105) {$R=RR/\sigma_1$};
\node[font=\Large] at (237,105) {$\unsure{RR|\mathcal R\mathcal R}$};
\draw[->,line width=.5pt] (176,109) -- (155,109);
\draw[->,line width=.55pt] (60,177) -- (59,277);
\draw[->,line width=1.05pt] (236,173) -- (237,267);
\node[anchor=west,font=\normalsize] at (263,201) {suppr};
\node[font=\normalsize] at (83,330) {$A=\vec A/\sigma$};
\node[font=\Large] at (239,328) {$\vec A$};
\draw[->,line width=.45pt] (180,335) -- (162,336);
\node[font=\Large] at (410,325) {$\vec A_0$};
\draw[->,line width=1.1pt] (333,312)
 .. controls (371,308) and (382,322) .. (357,330)
 -- (281,333);
\node[font=\normalsize] at (237,393) {$\sigma$};
\draw[->,line width=.6pt] (399,381) -- (397,532);
\node[font=\normalsize] at (431,436) {$\sigma$};
\node[font=\Large] at (394,590) {$S$};
\draw[->,line width=.55pt] (458,599) -- (614,601);
\node[font=\Large] at (516,567) {$g$};
\node[font=\Large] at (667,590) {$\mathbb N$};
\node[anchor=west] at (647,74) {a) $\unsure{\sigma}$};
\node[anchor=west] at (651,145) {b)};
\node[anchor=west] at (658,219) {c)};
\node[anchor=west] at (665,367) {d)};
''')

operations12 = picture('figure', 1430, 230, r'''
\node[anchor=west] at (65,65) {6) Bouchage des trous (gommage des cercles de raccord)};
\node[anchor=west] at (70,144) {7) gommage des cercles de découpage};
\draw[line width=.55pt] (5,21) -- (202,4);
\draw[line width=.55pt] (13,37) -- (209,19);
\draw[line width=.65pt] (26,211) -- (256,184);
\draw[line width=.65pt] (38,229) -- (270,198);
''', '.013')

headings17 = picture('figure', 540, 260, r'''
\draw[line width=.5pt] (18,34) -- (25,250);
\node[anchor=west,font=\normalsize] at (47,60) {\uline{graphes} \uline{pondérés}};
\node[anchor=west] at (58,136) {graphes bipondérés \deleted{\uuline{marqués}}};
\node[anchor=west] at (50,205) {graphes pondérés marqués};
''', '.020')

notation19 = picture('figure', 830, 610, r'''
\node[font=\Large] at (130,112) {$\deleted{\unsure{\mathcal T|\mathcal C}S}$};
\node[font=\Large] at (411,111) {$\deleted{\unsure{\mathcal T|\mathcal C}D}$};
\node[font=\Large] at (315,251) {$\deleted{\unsure{\mathcal T|\mathcal C}SD}$};
\draw[line width=.55pt] (35,183) -- (264,26)
 .. controls (286,10) and (316,0) .. (313,24);
\draw[line width=.55pt] (131,229) -- (329,44);
\draw[line width=.5pt] (310,193) -- (494,58);
\draw[line width=.5pt] (168,321) -- (300,195);
\draw[line width=.5pt] (311,319) -- (481,174);
\node[font=\Large] at (165,420) {$\deleted{\unsure{\mathcal T|\mathcal C}^{*}(\unsure{P|\Gamma})}$};
\draw[line width=.55pt] (34,463) -- (184,328);
\draw[line width=.6pt] (549,68) -- (539,274);
\node[anchor=west] at (558,188) {avec $\unsure{\omega^t|\omega^L}=I$};
\node[font=\Large] at (550,320) {$\unsure{\mathcal T|\mathcal C}$};
\draw[line width=.6pt] (638,370) -- (645,602);
\node[font=\Large] at (531,410) {$S\unsure{\mathcal T|\mathcal C}$};
\node[font=\Large] at (548,491) {$SD\unsure{\mathcal T|\mathcal C}$};
\node[font=\Large] at (568,566) {$D\unsure{\mathcal T|\mathcal C}$};
\node[font=\Large] at (720,405) {$ST$};
\node[font=\Large] at (725,488) {$SDT$};
\node[font=\Large] at (739,559) {$DT$};
\node[font=\Large] at (176,549) {$\unsure{\mathcal T|\mathcal C}$};
\node[anchor=west,align=left] at (246,564) {graphes pond.\\discrets};
\draw[line width=.45pt] (132,593) -- (120,611);
\draw[line width=.45pt] (228,581) -- (248,612);
''', '.018')

diagram20 = picture('diagram', 890, 335, r'''
\node[font=\Large] at (386,42) {$\unsure{\mathcal T|\mathcal C}$};
\node[anchor=west,align=left] at (453,51) {graphes pond.\\discrets};
\node[font=\Large] at (281,151) {$S\unsure{\mathcal T|\mathcal C}$};
\node[anchor=west] at (31,172) {graphes b};
\node[font=\Large] at (519,146) {$D\unsure{\mathcal T|\mathcal C}$};
\node[anchor=west] at (595,152) {graphes pondérés};
\node[font=\Large] at (421,271) {$SD\unsure{\mathcal T|\mathcal C}$};
\node[anchor=west] at (531,291) {graphes};
\draw[line width=.6pt] (345,80) -- (323,114);
\draw[line width=.6pt] (438,75) -- (460,116);
\draw[line width=.6pt] (313,194) -- (351,261);
\draw[line width=.6pt] (513,191) -- (476,251);
\node[font=\Large] at (768,-6) {$SD\unsure{\mathcal T|\mathcal C}$};
\node[font=\Large] at (783,53) {$D\unsure{\mathcal T|\mathcal C}$};
\draw[line width=.55pt] (851,0) -- (854,93);
''', '.017')

diagram21 = picture('diagram', 210, 255, r'''
\node[font=\Large] at (101,43) {$\unsure{\ell|t}$};
\node[font=\Large] at (44,139) {$s\unsure{\ell|t}$};
\node[font=\Large] at (160,143) {$d\unsure{\ell|t}$};
\node[font=\Large] at (98,215) {$sd\unsure{\ell|t}$};
\draw[line width=.55pt] (67,62) -- (37,93);
\draw[line width=.55pt] (119,69)
 .. controls (126,82) and (138,83) .. (138,94);
\draw[line width=.55pt] (26,177)
 .. controls (40,180) and (43,183) .. (40,191);
\draw[line width=.55pt] (159,180) -- (139,200) -- (139,207);
''', '.025')

boxed23 = picture('diagram', 1200, 295, r'''
\node[anchor=west,font=\normalsize] at (9,39) {$(\Gamma\in Q)$};
\draw[line width=.5pt] (0,55) -- (1148,25)
 .. controls (1184,25) and (1187,33) .. (1178,76);
\draw[line width=.5pt] (23,88) -- (23,258)
 -- (1128,228)
 .. controls (1145,229) and (1140,191) .. (1145,100);
\node[font=\normalsize] at (201,143) {$S_1\unsure{\mathcal T|\mathcal C}_{g,\nu}^{\pm1}$};
\node[font=\normalsize] at (510,140) {$\unsure{\mathcal T|\mathcal C}_{g,\nu}^{\pm1}$};
\node[font=\normalsize] at (903,145) {$\operatorname{Ens}(\unsure{\omega|0})\times[\pm1]$};
\draw[->,line width=1pt] (342,149) -- (419,148);
\draw[->,line width=.55pt] (595,145) -- (695,145);
\node[anchor=west] at (106,277) {$\tau_r=\mathrm{id}$ si $r\in\mathbb Z$};
''', '.014')

partial_box22 = picture('diagram', 420, 335, r'''
\node[anchor=west] at (0,25) {$(\Gamma\in Q)$};
\draw[line width=.45pt] (15,60) -- (18,230) -- (420,221);
\draw[line width=.45pt] (0,30) -- (420,18);
\node at (169,122) {$S_1\unsure{\mathcal T|\mathcal C}_{g,\nu}^{\pm1}$};
\draw[->,line width=.85pt] (335,128) -- (419,128);
\node[anchor=west] at (88,249) {$\tau_r=\mathrm{id}$ si $r\in\mathbb Z$};
\node[anchor=west] at (175,312) {$\deleted{\unsure{\mathcal T|T}_{g,\nu}^{\pm1}}$};
\draw[line width=.5pt] (181,297) -- (326,270);
''', '.015')


rows = [
    ('041-SB01',
        r'\texttt{/*JOB=CRAY2;ACCT=*********,ALL=}\unsure{\texttt{M06}|\texttt{MO6}}'
        + '\n' + r'\texttt{// JOB MSGLEVEL=(0,0),MSGCLASS=Z}'
        + '\n' + r'\texttt{// EXEC CSSBATCH}'
        + '\n' + r'\texttt{//CRAYIN DD *}'),
    ('041-SB02', r'\unsure{\texttt{J0231CNU}|\texttt{JO231CNU}}'),
    ('041-SB03', date_frame),
    ('041-SB04', diagram04),
    ('041-SB05',
        r'a) $\sigma^2=\mathrm{id}$, $\sigma$ ss pt fixe'
        + '\n' + r'b) suppr compatible avec $D_\infty\longrightarrow\{\pm1\}$'),
    ('041-SB06',
        r'c) $\unsure{RR|\mathcal R\mathcal R}/D_\infty'
        + r'\underset{\unsure{\mathrm{bij}|1-1}}{\longleftrightarrow}'
        + r'A=\vec A/\{\pm1\}$'),
    ('041-SB07',
        r'd) (\unsure{60!|bo!}) condition aux dimensions'
        + '\n' + r'(ou hyperbolique) : $\forall s\in S$,'
        + '\n' + r'on a \deleted{$\unsure{\nu_s+2g(s)|\mathrm{val}(s)}$}. '
        + r'$2g(s)+\nu_s\ge3$'),
    ('041-SB08',
        r'\margin{$3\unsure{g_\rho|g_s}-3+\nu_s\ge0$'
        + '\n' + r'$2\unsure{g_\rho|g_s}-2+\nu_s\ge1$'
        + '\n' + r'$2g_s+\nu_s\ge3$}'),
    ('041-SB09', r'1) \unsure{Sommes|Sommet}'),
    ('041-SB10',
        r'$\begin{array}{c}4)\\5)\end{array}'
        + r'\left\{\begin{array}{l}'
        + r'\text{amalgamation (\uline{sans} gommage)}\\'
        + r'\text{découpage (en gardant \unsure{donnée|données} de recollement)}'
        + r'\end{array}\right.$'),
    ('041-SB11',
        r'$\begin{array}{c}2)\\3)\end{array}'
        + r'\left\{\begin{array}{l}'
        + r'\text{gommage des \deleted{\unsure{points}} sommets de marquage.}\\'
        + r'\text{surmarquage}'
        + r'\end{array}\right.$'),
    ('041-SB12', operations12),
    ('041-SB13',
        r"\margin{\unsure{2|V}. inverses l'une de l'autre"
        + '\n' + r'Conditions pour les \unsure{découpages|on découpe}'
        + '\n' + r'\unsure{que sur} des cercles \uline{marqués}}'),
    ('041-SB14', r'\uline{Cercles de découpage}' + '\n' + r'\uline{cercles de raccord}'),
    ('041-SB15',
        r'Sommets de marquage \inserted{\unsure{ou de|et} rigidification}'
        + r' $\left\{\begin{array}{l}\text{périphériques}\\\text{intérieurs}\end{array}\right.$'),
    ('041-SB16', r'cercles marqués (\unsure{non|ou} marqués)'),
    ('041-SB17', headings17),
    ('041-SB18',
        r"type combinatoire d'un objet de \deleted{$\unsure{\mathcal G|\mathcal C}$} "
        + r'$SD\unsure{\mathcal T|\mathcal C}_{dp}\unsure{,}$'
        + '\n' + r'Catégorie des types combinatoires'),
    ('041-SB19', notation19),
    ('041-SB20', diagram20),
    ('041-SB21', diagram21),
    ('041-SB22',
        r'Le \uline{foncteur-twist} $\tau_\Gamma$'
        + '\n' + r'\deleted{\unsure{relatif}} \unsure{aux|un}'
        + '\n' + r'cercles de découpage'
        + '\n' + r'marqués, est défini'
        + '\n' + r'en termes de $4)5)$, avec'
        + '\n' + partial_box22),
    ('041-SB23', boxed23),
    ('041-SB24',
        r'\deleted{$\mathcal T_{g,\nu}^{\pm1}$}\quad'
        + r'\deleted{$\unsure{\mathcal T^*_{k\ell}|T^*_{k\ell}}$}\quad'
        + r'\deleted{$(TSR)_{g,\nu}$}\qquad $T_{g,\nu}S_\alpha$'),
    ('041-SB25',
        r"Mais l'\uline{\unsure{isom|idée}} de \unsure{un}"
        + '\n' + r'\deleted{\unsure{absolu}}\inserted{relatif} \unsure{des}'),
    ('041-SB26',
        r'\uline{twist}'
        + '\n' + r'cercles (de découpage'
        + '\n' + r'raccord, marqués ou pas)'
        + '\n' + r'\inserted{\unsure{ou de} relatif $\tau_r$}'),
    ('041-SB27',
        r'\unsure{pas}) : un'
        + '\n' + r'\inserted{relatif} $\tau_r$ (sur un cercle'
        + '\n' + r'de découpage \unsure{non} marqué) est'
        + '\n' + r'\uline{une nouvelle} \uline{structure}'
        + '\n' + r'\unsure{importante|imposée}'),
    ('041-SB28', r'\mspage{40}'),
]

native_views = {
    '041-SB01', '041-SB07', '041-SB09', '041-SB15', '041-SB16',
    '041-SB22', '041-SB23', '041-SB24', '041-SB25',
}
rotations = {'041-SB13': [-7], '041-SB26': [-16], '041-SB27': [-20]}

observations = {
    '041-SB01': 'Typed front-face job-control lines, not reverse-side material. Nine stars follow ACCT=. Zero/O distinction in terminal M06 remains local uncertainty. Punctuation and abbreviated tokens retained. Printer striping/ruling is background, not text.',
    '041-SB02': 'Typed J0231CNU; the second glyph is zero/O-shaped and alternatives are explicit.',
    '041-SB03': 'Date in open-top U-shaped handwritten frame. Middle numeral resembles 4 or 9; frame is represented with its sloping lower edge rather than a closed rectangle.',
    '041-SB04': 'All directions recorded. Main R-to-A arrow is thick and labelled suppr; A_0-to-A has a hooked right tail and left-pointing head. Right vertical arrow points downward to S; g-labelled arrow points right to N. Top has sigma_0,sigma_1. Right-edge a/b/c/d fragments are included. RR may use a script alphabet; alternative retained. Printed stripes are omitted.',
    '041-SB05': 'Ss pt fixe is retained without expansion. B) contains suppr and a right-pointing arrow from D-infinity to brace-enclosed plus/minus one.',
    '041-SB06': 'Two R-like letters precede the quotient. Horizontal arrow has heads at both ends. Lower handwritten annotation is uncertain between bij and 1-1.',
    '041-SB07': 'Parenthetic short token before condition is uncertain. The crossed expression is dense; candidate formula readings are given, never illegible. Live inequality is kept literally.',
    '041-SB08': 'First coefficient is visibly 3 and was not corrected to 2. First two g subscripts are rho/s-like and differ in appearance from the last clear s. Lower bounds 0, 1, and 3 are retained.',
    '041-SB09': 'Final letters of Sommes/Sommet remain uncertain; initial item numeral is 1.',
    '041-SB10': 'Numbers appear in the order 4 then 5, with a left brace grouping the two operations. Sans is underlined. Singular/plural of donnée is uncertain.',
    '041-SB11': 'Numbers appear 2 then 3, under one left brace. The deleted word has a descender and could read points. Live sommets de marquage and lower surmarquage retained.',
    '041-SB12': 'Partial double underline from preceding material appears at the top-left. The double line under item 7 reaches only the beginning of the following word; drawn geometrically rather than assigning it to the whole sentence. Raccord is visible as the same word in this page\'s circle heading.',
    '041-SB13': 'Whole crop rotated clockwise 7 degrees. Inverses l\'une de l\'autre and Conditions ... des cercles marqués are readable. Initial short glyph and middle phrases remain uncertain. Marqués is underlined. Clipped neighbours at far left/right are not completed.',
    '041-SB14': 'Two separate underlined heading lines; lower one reads cercles de raccord.',
    '041-SB15': 'Interlinear addition appears ou de rigidification, with et retained as an alternative for the first part. A left brace groups périphériques and intérieurs. Upper-border line is the previous heading underline.',
    '041-SB16': 'Parenthetical first word looks non, with ou retained as alternative. The repeated marqués wording is not repaired.',
    '041-SB17': 'Left vertical boundary, first heading underlines, and cancellation plus double underline on marqués retained. Black circles on extreme right are paper perforations, not symbols.',
    '041-SB18': 'Object-category abbreviation ends in the recurring script T/C-like glyph. Cancelled preceding symbol is uncertain. Possible comma after the subscript is explicitly doubtful. Last prose line is clipped at the bottom but identifiable.',
    '041-SB19': 'Entire notation column retained, including diagonally cancelled candidate names, star and argument of the lower deleted expression, right-side short formula, divider, and paired script/plain columns. Repeated script glyph is ambiguous between calligraphic T and C. Lower argument resembles P or Gamma. Bottom connectors exit the crop.',
    '041-SB20': 'Diamond consists of plain strokes without arrowheads. Labels and adjacent graph descriptions are included. Upper-right notation fragments/divider belong to the overlap with the notation column. Dark bottom edge is the sheet boundary, not a connector.',
    '041-SB21': 'Repeated lower-case glyph resembles ell or t. All four labels are represented with the same stated alternatives. Connector strokes are short and partly curved, without evident arrowheads. Right-hand black circles are punch holes and excluded.',
    '041-SB22': 'Heading reads foncteur-twist and is underlined; tau has Gamma subscript. Deleted relatif and following short word uncertain. Operation numbers are literally 4)5). The portion of the boxed formula and lower deleted notation visible at right are retained separately as a clipped diagram excerpt.',
    '041-SB23': 'Frame is irregular and partly interrupted. First arrow is much heavier than second, both point right. Script glyph and Ens argument remain uncertain; plus/minus-one superscripts and bracketed target retained. Under-frame statement reads tau_r=id si r in Z.',
    '041-SB24': 'Three cancelled formula groups precede the live expression. Small indices/exponent in middle crossed group are uncertain. The live initial T is visibly plain rather than the script glyph used elsewhere; S has alpha-like subscript.',
    '041-SB25': 'Underlined word isom/idée remains uncertain. Cancelled lower word tentatively absolu, replacement relatif. Upper/lower adjoining line fragments are clipped and not completed.',
    '041-SB26': 'Whole crop rotated clockwise 16 degrees. Twist is underlined. Parenthesis includes cercles de découpage, raccord, marqués ou pas; no unseen conjunction was added across the line break. Added lower phrase and its exact scope remain uncertain.',
    '041-SB27': 'Whole crop rotated clockwise 20 degrees. The small word before marqué looks non but is dense and uncertain. Une nouvelle and structure have separate underlines. Final word remains uncertain between importante and imposée. Left/top context is clipped, so preserved as fragments.',
    '041-SB28': 'Pencil foliation 40 over printed striping; bottom black region is page edge.',
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
    assert len(rows) == len(boxes) == 28
    assert [name for name, _ in rows] == [box['box'] for box in boxes]
    assert len(set(name for name, _ in rows)) == 28
    OUT.mkdir(parents=True, exist_ok=True)

    def write_tsv(stream):
        writer = csv.writer(stream, delimiter='\t')
        writer.writerow(['box', 'reading'])
        writer.writerows(rows)

    journal = {
        'page': '148_scan041',
        'protocol': 'Blind independent reading from assigned scan and boxes only. Fixed crops created once. No OCR, comparison material, other pages, external research, or TeX compilation.',
        'all_boxes_successfully_viewed': True,
        'box_count': 28,
        'failed_display_attempts': [],
        'magnification_policy': 'Every display contains the entire fixed saved crop; no new subrectangles.',
        'boxes': [],
    }
    for box, (name, reading) in zip(boxes, rows):
        views = [str(DISPLAY / (name + '.jpg'))]
        if name in native_views:
            views.append(str(DISPLAY / (name + '_native2.jpg')))
        for angle in rotations.get(name, []):
            views.append(str(DISPLAY / (name + '_rot' + str(angle) + '.jpg')))
        journal['boxes'].append({
            'box': name,
            'rect': [int(box[key]) for key in ('x0', 'y0', 'x1', 'y1')],
            'native_evidence': str(ROOT / 'crops' / 'second' / '148_scan041' / (name + '.png')),
            'successfully_viewed': True,
            'successful_views': views,
            'rotation_degrees_ccw': rotations.get(name, []),
            'local_uncertainty': r'\unsure{' in reading,
            'observation': observations[name],
        })
    atomic(OUT / '148_scan041_second.tsv', write_tsv)
    atomic(OUT / '148_scan041_blind_journal.json',
           lambda stream: json.dump(journal, stream, ensure_ascii=False, indent=2))
    print('Atomically wrote 28 independent readings and a complete viewing journal.')


if __name__ == '__main__':
    main()
