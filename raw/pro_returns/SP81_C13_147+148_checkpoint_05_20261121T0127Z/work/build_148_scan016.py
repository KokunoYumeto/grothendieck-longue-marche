import json
from pathlib import Path

BASE = Path('/workspace/scratch/15c7af26487b/edition')
PAGE = '148_scan016'
coords = {
    'letterhead': [145, 83, 580, 211],
    'issue_date': [893, 119, 1410, 165],
    'reference': [157, 264, 520, 330],
    'degree': [450, 418, 1331, 461],
    'subject_rule': [454, 482, 1329, 566],
    'date_place': [234, 777, 1465, 884],
    'reproductive_sentence': [229, 1129, 1555, 1197],
    'midright_marks': [1217, 945, 1467, 1073],
    'authorization': [976, 1789, 1582, 1901],
    'signature': [1175, 1945, 1363, 2055],
    'lower_numeral': [35, 2277, 104, 2329],
}

carets = r'\texttt{' + r'\textasciicircum' * 13 + '}'
equals = r'\texttt{' + '=' * 54 + '}'

midmark = r'''\begin{tikzpicture}[x=.022cm,y=-.022cm,line cap=round,line join=round,baseline={(0,24.8)}]
\draw[line width=.65pt] (0,0)--(1.2,2.5)--(2.3,4.8)--(3.9,7.4)--(4.7,10.8)--(6.4,13.5)--(8.2,14.2)--(8.1,17.6)--(9.3,20.5)--(10.4,24.8);
\node[anchor=west] at (15,15) {\unsure{}};
\end{tikzpicture}'''

signature = r'''\begin{tikzpicture}[x=.020cm,y=-.020cm,line cap=round,line join=round,baseline={(0,70)}]
% Detached left fleck and its point.
\fill (10.8,70)--(12.8,70.2)--(12.7,72.1)--(15.6,76.1)--(13.1,74.5)--(10.6,74.5)--(10,72.4)--cycle;
\fill (14.8,68.1) circle[radius=.013cm];
% Upper-left upright and separate short appendages.
\draw[line width=.50pt] (30.5,23.8) .. controls (29.3,25) and (31,27) .. (30.5,30)
 .. controls (30.2,37) and (30.2,47) .. (32.8,51.4);
\draw[line width=.48pt] (34.0,32.0)--(35.1,32.7);
\draw[line width=.48pt] (36.1,33.1) .. controls (38.0,36.7) and (40.3,38.0) .. (42.1,36.6)
 .. controls (44.5,34.9) and (45.3,32.7) .. (47.4,32.7);
\draw[line width=.45pt] (34.5,38.2) .. controls (36.7,40.7) and (35.7,43.7) .. (35.1,47.7)
 .. controls (34.7,49.7) and (33.5,50.4) .. (32.4,50.6);
% Long central descending upright.
\draw[line width=.65pt] (47.5,14.5) .. controls (49,20) and (47.5,29) .. (47.8,37.0)
 .. controls (48.1,45.0) and (46.3,53.0) .. (46.8,61.0)
 .. controls (44.7,70.0) and (44.3,77.0) .. (45.1,84.8)
 .. controls (44.4,88.9) and (47.0,93.2) .. (48.1,95.4);
% Broad left return, rising across the central upright.
\draw[line width=.60pt] (75.0,39.5) .. controls (72.1,32.1) and (59.4,35.0) .. (48.0,40.4)
 .. controls (40.0,44.6) and (28.4,48.1) .. (25.8,58.1)
 .. controls (22.4,67.7) and (31.4,69.5) .. (41.8,68.7);
% Low oval, with the small gap and point at its upper edge.
\draw[line width=.55pt] (46.9,61.2) .. controls (51.7,57.6) and (55.0,55.5) .. (57.3,54.7);
\fill (61.4,54.3) circle[radius=.0104cm];
\draw[line width=.55pt] (65.1,54.3) .. controls (68.6,53.7) and (71.0,56.5) .. (69.8,59.3)
 .. controls (68.1,63.8) and (60.7,65.3) .. (53.0,64.8)
 .. controls (50.1,64.6) and (48.3,63.7) .. (46.8,62.7);
\draw[line width=.52pt] (58.0,64.5)--(72.4,64.4);
% Upper horizontal sweep and its rising right return.
\fill (74.1,61.1)--(80.4,60.6)--(77.2,63.0)--(74.2,63.8)--cycle;
\draw[line width=.57pt] (77.7,60.9) .. controls (99.2,60.2) and (122.2,59.7) .. (133.2,59.5)
 .. controls (139.4,59.3) and (143.5,56.7) .. (145.8,52.8);
% Lower left curl and the second long horizontal sweep, with its small gap.
\draw[line width=.57pt] (72.4,66.5) .. controls (63.4,67.0) and (59.2,69.0) .. (67.6,70.0)
 .. controls (71.7,70.0) and (75.1,70.3) .. (78.2,70.6);
\draw[line width=.62pt] (82.8,70.6) .. controls (116.8,71.0) and (151.0,68.7) .. (177.0,67.1);
% Detached upper-right hook.
\draw[line width=.52pt] (142.3,37.4) .. controls (140.6,35.7) and (138.7,35.2) .. (138.2,35.3)
 .. controls (137.8,39.5) and (138.4,42.5) .. (139.4,44.2);
% Short upper segment and the attached diagonal descent at the right.
\draw[line width=.38pt] (145.8,46.5) .. controls (146.6,48.3) and (146.2,51.2) .. (145.4,53.4);
\draw[line width=.60pt] (142.5,48.6) .. controls (143.6,52.3) and (144.8,55.2) .. (147.2,58.6)
 --(152.8,68.0);
\node[anchor=west] at (181,70) {\unsure{}};
\end{tikzpicture}'''

tex = r'''\cotefile{148}
\scanpage{16}

\noindent
\begin{minipage}[t]{.42\linewidth}
\centering
U N I V E R S I T E\\
DES SCIENCES ET TECHNIQUES\\
DU LANGUEDOC\\
CARETS
\end{minipage}\hfill
\begin{minipage}[t]{.54\linewidth}
\raggedleft
\vspace*{.8\baselineskip}
Montpellier, le 14 octobre 1983
\end{minipage}

\medskip
Service de la Scolarité

Diffusion : Liste A\\
MA/gs \qquad N° 4469

\begin{center}
AVIS DE SOUTENANCE D'UNE THESE DE DOCTORAT DE 3e CYCLE

`` SCIENCES AGRONOMIQUES option PHYTOTECHNIE ''

EQUALS
\end{center}

\uline{NOM et Prénom du candidat} : LECONTE Antoine

\uline{Titre de la Thèse} : ``LA REPRODUCTION SEXUEE DE L'HEVEA BRASILIENSIS
(UNE APPROCHE HISTOLOGIQUE ET EXPERIMENTALE)''

\uline{Date, heure et lieu de soutenance prévus} : 27 octobre 1983 à 9h.30 - Salle
de cours n°9 - (Bât. administratif ) Université des Sciences et Techniques du
Languedoc.

\uline{Nom du Directeur de thèse} : MM. Charles HEBANT - BONNET

\uline{Désignation du laboratoire où la thèse est préparée} : Laboratoire de
Biologie végétale - U.S.T.L.

\noindent\hspace*{.77\linewidth}%
MIDMARK

\uline{Analyse de l'ouvrage} : L'amélioration génétique de l'Hévéa est entravée par un
très mauvais taux de réussite des pollinisations contrôlées.

L'étude histologique montre que le processus reproducteur
(gaméto-génèse, fécondation et développement embryonnaire) se déroule normalement.
Une exception est signalée : le cas du clone GT 1 dont la stérilité mâle est
décrite. La fécondation a lieu moins de 24 heures après la pollinisation.

L'étude expérimentale, menée en Côte d'Ivoire, porte sur
les modalités de la floraison et de la fructification en conditions naturelles
et artificielles. La majorité des fleurs subissent une élimination naturelle
dans un délai de 5 à 15 jours après la pollinisation. Des traitements hormonaux
(ANA, chlorure de cobalt) peuvent augmenter significativement le taux de
fructification.

Une explication physiologique de la faible fertilité
de l'Hévéa est proposée.

\uline{Durée approximative des recherches ayant abouti à la thèse} : 2 ans

\uline{Composition du jury proposé} : \begin{tabular}[t]{ll}
MM. & BONNET\\
& D'AUZAC\\
& HALLE\\
& NICOLAS D.
\end{tabular}

\begin{flushright}
P/ le Secrétaire Général,\\
l'Attachée Principale d'Adminis-\\
tration scolaire et universitaire,

\medskip
SIGNATURE

\medskip
\uline{A. GENTIL}
\end{flushright}

\margin{15}
'''.replace('CARETS', carets).replace('EQUALS', equals).replace('MIDMARK', midmark).replace('SIGNATURE', signature)

changes = [
    {
        'id': f'{PAGE}-01', 'place': 'L10–L11, subject heading and separate keyed row',
        'C': "\\uuline{`` SCIENCES AGRONOMIQUES option PHYTOTECHNIE ''}",
        'H': '[no witness H]',
        'final': "`` SCIENCES AGRONOMIQUES option PHYTOTECHNIE ''\n" + equals,
        'evidence': 'A separate row consists of fifty-four repeated equals glyphs with visible inter-column gaps, counted visually as nine groups of six. It extends beyond both ends of the quoted heading. A continuous double underline does not preserve the keyed marks or their count. Crop 148_scan016_subject_rule.png, original box [454,482,1329,566].',
        'crop': f'{PAGE}_subject_rule.png', 'box': coords['subject_rule'],
        'confidence': 'high', 'kind': 'other', 'error_sheet_kind': 'Other',
        'differs_C': True, 'differs_H': False, 'marked_in_H': False, 'consequential': False,
    },
    {
        'id': f'{PAGE}-02', 'place': 'Right-middle area between the laboratory entry and the analysis paragraph',
        'C': '', 'H': '[no witness H]', 'final': midmark,
        'evidence': 'One isolated strong stroke descends towards the right through several small bends, at approximately [1255,1035,1267,1063]. Its contour is exposed, but its function and status are not established; no letters are assigned to it. It is directly traced with an adjacent doubt marker. The much paler surrounding broken pattern is not comparably dark and does not expose a continuous surface inscription; its probable transfer/show-through status is recorded in notes without settled provenance. Full-region crop 148_scan016_midright_marks.png, original box [1217,945,1467,1073].',
        'crop': f'{PAGE}_midright_marks.png', 'box': coords['midright_marks'],
        'confidence': 'medium', 'kind': 'omission', 'error_sheet_kind': 'Omissions',
        'differs_C': True, 'differs_H': False, 'marked_in_H': False, 'consequential': False,
    },
    {
        'id': f'{PAGE}-03', 'place': 'Handwritten signature above the typed name, M0118',
        'C': r'\unsure{A. Gentil}', 'H': '[no witness H]', 'final': signature,
        'evidence': 'The graphic exposes a detached small left fleck and its point, upper-left appendages, a long central descending upright, a broad left return, a low oval with a small gap and point, two long horizontal sweeps, a detached upper-right hook, and a right diagonal descent. These contours do not separately expose the complete letters of A. Gentil. The strokes are directly reproduced with a visible local uncertainty marker. The typed A. GENTIL below remains transcribed as typed text; it does not settle the autograph letters. Crop 148_scan016_signature.png, original box [1175,1945,1363,2055].',
        'crop': f'{PAGE}_signature.png', 'box': coords['signature'],
        'confidence': 'medium', 'kind': 'drawing or diagram', 'error_sheet_kind': 'Drawings and diagrams',
        'differs_C': True, 'differs_H': False, 'marked_in_H': False, 'consequential': False,
    },
]
inventory_specs = [
    ('text', 'L01, top left', 'U N I V E R S I T E', 'typewriter'),
    ('text', 'L02, top left', 'DES SCIENCES ET TECHNIQUES', 'typewriter'),
    ('text', 'L03, top left', 'DU LANGUEDOC', 'typewriter'),
    ('text', 'L04, separate row below the letterhead', '^' * 13, 'typewriter'),
    ('text', 'L05, upper right', 'Montpellier, le 14 octobre 1983', 'typewriter'),
    ('text', 'L06, upper left below the letterhead', 'Service de la Scolarité', 'typewriter'),
    ('text', 'L07, upper administrative block', 'Diffusion : Liste A', 'typewriter'),
    ('text', 'L08, upper administrative block', 'MA/gs; N° 4469', 'typewriter'),
    ('text', 'L09, centred notice title', "AVIS DE SOUTENANCE D'UNE THESE DE DOCTORAT DE 3e CYCLE", 'typewriter'),
    ('text', 'L10, centred quoted subject', 'SCIENCES AGRONOMIQUES option PHYTOTECHNIE', 'typewriter'),
    ('text', 'L11, separate keyed row', '=' * 54, 'typewriter'),
    ('text', 'L12, first labelled field', 'NOM et Prénom du candidat : LECONTE Antoine', 'typewriter'),
    ('text', 'L13–L14, thesis title field', "Titre de la Thèse : LA REPRODUCTION SEXUEE DE L'HEVEA BRASILIENSIS", 'typewriter'),
    ('text', 'L15–L17, date and place field', 'Date, heure et lieu de soutenance prévus : 27 octobre 1983 à 9h.30', 'typewriter'),
    ('text', 'L18, director field', 'Nom du Directeur de thèse : MM. Charles HEBANT - BONNET', 'typewriter'),
    ('text', 'L19–L20, laboratory field', 'Désignation du laboratoire où la thèse est préparée : Laboratoire de Biologie végétale - U.S.T.L.', 'typewriter'),
    ('drawing', 'right-middle, below the laboratory field and above L21', 'isolated short dark stroke; status uncertain', 'unidentified hand or mark'),
    ('text', 'L21–L22, analysis opening', "Analyse de l'ouvrage : L'amélioration génétique de l'Hévéa", 'typewriter'),
    ('text', 'L23–L26, histological paragraph', "L'étude histologique montre que le processus reproducteur", 'typewriter'),
    ('text', 'L27–L32, experimental paragraph', "L'étude expérimentale, menée en Côte d'Ivoire", 'typewriter'),
    ('text', 'L33–L34, final analysis paragraph', "Une explication physiologique de la faible fertilité de l'Hévéa", 'typewriter'),
    ('text', 'L35, duration field', 'Durée approximative des recherches ayant abouti à la thèse : 2 ans', 'typewriter'),
    ('text', 'L36–L39, jury field and list', "Composition du jury proposé : MM. BONNET; D'AUZAC; HALLE; NICOLAS D.", 'typewriter'),
    ('text', 'L40–L42, lower-right authorization block', "P/ le Secrétaire Général, l'Attachée Principale d'Adminis-/tration scolaire et universitaire,", 'typewriter'),
    ('drawing', 'lower right, above the typed name', 'handwritten signature, alphabetic sequence unresolved', 'signature hand; alphabetic attribution unresolved'),
    ('text', 'L43, lower-right typed name with underline', 'A. GENTIL', 'typewriter'),
    ('margin note', 'lower left margin', '15', 'lighter hand; attribution unestablished'),
]
inventory = [
    {'sheet_kind': 'typescript', 'hand': hand, 'element': f'E{i:02d}', 'kind': kind,
     'position': pos, 'first_words_or_objects': first, 'transcribed': 'yes'}
    for i, (kind, pos, first, hand) in enumerate(inventory_specs, 1)
]

second_boxes = []

def blind(kind, name, reading):
    x0,y0,x1,y1=coords[name]
    second_boxes.append({'box': f'B{len(second_boxes)+1:02d}', 'kind': kind,
                         'x0': x0, 'y0': y0, 'x1': x1, 'y1': y1, 'reading': reading})

blind('complete letterhead block and separate keyed decoration', 'letterhead',
      r'''U N I V E R S I T E\\
DES SCIENCES ET TECHNIQUES\\
DU LANGUEDOC\\
''' + carets)
blind('complete dated line at the upper right', 'issue_date', 'Montpellier, le 14 octobre 1983')
blind('two complete administrative baselines including the reference', 'reference',
      r'''Diffusion : Liste A\\
MA/gs \qquad N° 4469''')
blind('complete main notice title', 'degree', "AVIS DE SOUTENANCE D'UNE THESE DE DOCTORAT DE 3e CYCLE")
blind('complete quoted subject heading and separate keyed row', 'subject_rule',
      "`` SCIENCES AGRONOMIQUES option PHYTOTECHNIE ''\n" + equals)
blind('complete date and venue field across its three coherent baselines', 'date_place',
      r'''\uline{Date, heure et lieu de soutenance prévus} : 27 octobre 1983 à 9h.30 - Salle
de cours n°9 - (Bât. administratif ) Université des Sciences et Techniques du
Languedoc.''')
blind('localized marks in the full right-middle region only; typescript is context', 'midright_marks', midmark)
blind('two complete prose baselines including the parenthetical terms', 'reproductive_sentence',
      "L'étude histologique montre que le processus reproducteur\n(gaméto-génèse, fécondation et développement embryonnaire) se déroule normalement.")
blind('complete authorization block with its visible line-end division', 'authorization',
      r'''P/ le Secrétaire Général,\\
l'Attachée Principale d'Adminis-\\
tration scolaire et universitaire,''')
blind('complete handwritten graphic in the lower right, including its detached marks', 'signature', signature)
blind('lower marginal handwritten number only', 'lower_numeral', r'\margin{15}')

report = {
    'page': PAGE, 'reader': 'reader_b', 'line_count': 43,
    'layout': 'Upright typescript notice. The four-line university letterhead is at upper left, with the issue date at upper right and the service, distribution and reference block below the letterhead. A centred notice title and quoted subject are followed by a separate keyed row. The main body consists of underlined field labels, a fourteen-baseline analysis, the duration field and a four-name jury list. The authorization block, autograph and underlined typed name occupy the lower right. One isolated dark stroke appears in the right-middle region between the laboratory entry and the analysis. A lighter handwritten 15 is at bottom left. The line count covers forty-three typed or decorative baselines, with the independent upper-right date counted separately; the autograph, isolated mark and marginal number are additional graphic elements.',
    'changes': changes,
    'decisions': [{
        'id': 'M0118', 'decision': 'undecided', 'reading': r'\unsure{}',
        'evidence': 'The adjacent marker is the actual retained uncertainty in the direct signature drawing. Its individual strokes are graphically exposed, including the detached left fleck and point, upper appendages, descending central upright, broad return, low oval, parallel long sweeps, detached upper-right hook and right diagonal. The complete alphabetic sequence A. Gentil is not separately readable from those strokes. C’s candidate is retained only as a candidate in this report; the typed A. GENTIL below is transcribed independently.',
        'crop': f'{PAGE}_signature.png {coords["signature"]}', 'confidence': 'low',
    }],
    'unnumbered_decisions': [], 'inventory': inventory,
    'doubts': [
        {'place': 'Right-middle isolated stroke', 'reading': r'\unsure{}',
         'alternatives': 'Visible graphic stroke with unestablished function/status; no alphabetic reading proposed.',
         'confidence': 'medium',
         'reason': 'The dark contour is exposed, but neither a verbal attachment nor a settled marking function can be read. The pale surrounding pattern is recorded in notes, with its provenance left open.'},
        {'place': 'Lower-right autograph, M0118', 'reading': r'\unsure{}',
         'alternatives': 'A. Gentil is C’s candidate; the complete autograph letter sequence remains unresolved.',
         'confidence': 'low',
         'reason': 'The visible looped and sweeping strokes do not individually expose all the proposed letters. The nearby typed name is legible but does not settle the autograph’s alphabetic transcription.'},
    ],
    'notation': [
        {'form': '^' * 13, 'meaning': 'Literal separate keyed decoration below DU LANGUEDOC.',
         'evidence': 'L04; letterhead crop [145,83,580,211] exposes thirteen individual peaked glyphs, counted visually.', 'scope': 'This one row only.'},
        {'form': '=' * 54, 'meaning': 'Literal separate keyed decoration below the quoted subject heading.',
         'evidence': 'L11; subject_rule crop [454,482,1329,566] exposes fifty-four repeated double-bar glyphs, visually counted as nine groups of six.',
         'scope': 'This one row only; no mathematical meaning is assigned.'},
        {'form': '3e', 'meaning': 'The literal degree designation within the notice title.',
         'evidence': 'L09; degree crop [450,418,1331,461]: the numeral and lowercase e occupy the same baseline.', 'scope': 'This occurrence only.'},
    ],
    'abbreviations': [
        {'form': 'N°; n°', 'expansion': 'numéro, tentative expansion only; the written forms are retained.'},
        {'form': 'Bât.', 'expansion': 'bâtiment, tentative expansion only.'},
        {'form': 'MM.', 'expansion': 'Messieurs, tentative expansion only; retained in both the director and jury fields.'},
        {'form': 'U.S.T.L.', 'expansion': 'Université des Sciences et Techniques du Languedoc, tentative expansion from the name printed on this page; the abbreviation remains unchanged.'},
        {'form': 'P/', 'expansion': 'pour, tentative expansion only.'},
        {'form': 'MA/gs; GT 1; ANA', 'expansion': 'No expansion supplied by this leaf; all three written strings are retained.'},
    ],
    'hand': [
        {'habit': 'The autograph combines separately exposed short marks, loops and long sweeps without separately readable complete letter forms.',
         'places': 'Lower-right signature, M0118.', 'scope': 'This signature only; its contours were traced from its own crop.',
         'witness_errors': 'C gives a doubtful alphabetic candidate but does not preserve the graphic contours. The candidate remains unresolved and the drawing is supplied.'},
        {'habit': 'The lower marginal numerals are lighter than the typescript and have broad soft edges.',
         'places': 'Bottom-left 15.', 'scope': 'Both handwritten digits on this leaf.',
         'witness_errors': 'C’s 15 is retained; the ascending/descending first digit and the capped curved second digit were inspected separately.'},
        {'habit': 'A dark isolated short stroke coexists with a much paler broken surrounding pattern.',
         'places': 'Right-middle region beneath and around the final words of the laboratory entry.',
         'scope': 'The full region was cropped; the stronger contour alone is reproduced, with uncertainty of status.',
         'witness_errors': 'C omits the stronger stroke. No words are supplied for it or for the pale traces.'},
    ],
    'legibility': 'The typescript is clear, with distinct letter shapes and stable character spacing. Every typed baseline was compared with C, including names, capitalization, punctuation, abbreviations, dates and quantities; the typed prose matches C. The horizontal fold crosses the analysis but does not obscure its words. The reproductive-sentence crop confirms the literal gaméto-génèse, including its hyphen and the written accents. The keyed decoration is individually legible: thirteen carets and fifty-four equals signs. The signature is graphically clear but alphabetically unresolved, so its contours are reproduced with a local marker. The isolated dark stroke in the right-middle area is also visible, while its purpose is uncertain. The much paler surrounding broken pattern exposes no continuous surface writing and is provisionally treated as probable transfer or show-through, without settled provenance. No witness H is supplied for this page. The whole scan, both supplied halves and all eleven tight crops were actually inspected.',
    'notes': 'This typed notice is dated 14 octobre 1983 and carries reference N° 4469 (L05, L08). It announces a 3e-cycle thesis defence in SCIENCES AGRONOMIQUES option PHYTOTECHNIE for LECONTE Antoine (L09–L12). Its title is printed as LA REPRODUCTION SEXUEE DE L’HEVEA BRASILIENSIS (UNE APPROCHE HISTOLOGIQUE ET EXPERIMENTALE), with the unaccented capitals retained (L13–L14). The notice schedules the defence for 27 octobre 1983 at 9h.30 in Salle de cours n°9, in the administrative building of the named university (L15–L17). The director field reads MM. Charles HEBANT - BONNET and the laboratory field names Biologie végétale - U.S.T.L. (L18–L20). In its analysis, the notice says genetic improvement is impeded by poor success of controlled pollination; it describes a histological study, the exception of male sterility in clone GT 1, and fertilization occurring less than 24 hours after pollination (L21–L26). It then describes an experimental study in Côte d’Ivoire, elimination of most flowers within 5 to 15 days and proposed hormonal treatments, followed by a proposed physiological explanation of low fertility (L27–L34). These are the notice’s statements, not findings independently evaluated during transcription. The duration field gives 2 ans and the jury lists BONNET, D’AUZAC, HALLE and NICOLAS D. (L35–L39). The lower authorization block preserves P/ le and the physical Adminis-/tration division; this is a layout feature, not a word replacement (L40–L42). The typed underlined A. GENTIL is preserved below the graphic signature (L43). The full right-middle mark region remains a blind-reading target: its one strong stroke is traced, and its very pale broken surroundings are omitted from the transcription as probable transfer/show-through with provenance still unsettled. No alphabetic content or attachment is invented for that region. The source has no exposed typed-over replacement, cancelled word or inserted verbal passage. No mathematical, botanical or experimental verification was performed; the check-events list remains empty.',
    'check_events': [], 'second_boxes': second_boxes, 'diff_coverage': [],
    'deletion_insertion_check': 'C contains no deleted or inserted word on this page. Every typewritten baseline was inspected for overstrikes and no legible underlying replacement letter was found. The field-label strokes and the line beneath A. GENTIL are underlines, retained as such. The separate subject-row marks are individually keyed equals signs, not a continuous double underline. The isolated right-middle stroke crosses no word and has no readable insertion leader or alphabetic content; its status is kept uncertain. The autograph’s crossing strokes are preserved as part of its graphic form without assigning deletion or insertion states. The pale surrounding right-middle pattern is discussed in notes and remains within the blind target.',
}

(BASE/'work'/f'{PAGE}.tex').write_text(tex,encoding='utf-8')
(BASE/'work'/f'{PAGE}_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'page':PAGE,'lines':report['line_count'],'changes':len(changes),
                  'decisions':len(report['decisions']),'inventory':len(inventory),
                  'doubts':len(report['doubts']),'boxes':len(second_boxes),'crops':len(coords)},ensure_ascii=False))
