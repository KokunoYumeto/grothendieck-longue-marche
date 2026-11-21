import json
from pathlib import Path

BASE = Path('/workspace/scratch/15c7af26487b/edition')
PAGE = '148_scan006'
packet = (BASE/'packets'/f'{PAGE}.md').read_text(encoding='utf-8')
source_c = packet.split('## Witness C',1)[1].split('```tex',1)[1].split('```',1)[0].strip()
heading = 'ECOLOGIE GENERALE ET APPLIQUEE OPTION ECOLOGIE AQUATIQUE'
equals_row = '=' * 56
separator = heading + '\n\n' + r'\texttt{' + equals_row + '}'

signature = r'''\handwritten{\begin{tikzpicture}[x=.018cm,y=-.018cm,line cap=round,line join=round]
% The alphabetic candidate A. Gentil remains unresolved; only the exposed strokes are drawn.
\draw[line width=.55pt] (31,14) -- (29.6,18);
\draw[line width=.55pt] (22,44) .. controls (20.7,39) and (20.5,35) .. (22.1,33.7)
 .. controls (23.2,36) and (27.4,36.9) .. (30.3,37.7);
\draw[line width=.65pt] (34.4,30.3) -- (33.8,33.1);
\draw[line width=.55pt] (59.5,49.5) .. controls (45,46) and (29.2,51.2) .. (23.7,63.7)
 .. controls (18.4,74.4) and (33.5,81.1) .. (46.7,77.8)
 .. controls (58.4,75.4) and (55.2,69.7) .. (49.2,68.8)
 .. controls (42.1,67.4) and (37.6,69.4) .. (42.2,72.3)
 .. controls (48.9,76.4) and (57.8,75.1) .. (65.8,74.4)
 .. controls (83.2,71.2) and (96.4,76.7) .. (110.7,73.5)
 .. controls (123.8,71.3) and (128.8,66.8) .. (129.1,49.7)
 .. controls (129.3,60.1) and (132.9,68.9) .. (138.1,74.9);
\fill (62.3,52.4) circle[radius=.85];
\draw[line width=.48pt] (22.1,77.9) -- (21.4,86.3);
\draw[line width=.48pt] (21.2,88.4) .. controls (20.2,95.8) and (20.7,101.9) .. (21.5,105.1);
\draw[line width=.55pt] (72.1,88.4) -- (67.5,90.1) -- (73.2,91.7);
\draw[line width=.5pt] (79.3,88.1) .. controls (74.3,88.9) and (74.1,93.1) .. (81.6,92.2);
\draw[line width=.55pt] (84.4,92.9) .. controls (112.6,91.3) and (142.7,89.5) .. (170.1,88.6);
\node[anchor=west] at (176,69) {$\unsure{\phantom{A}}$};
\end{tikzpicture}}'''

old_head = source_c.split('Service de la Scolarité',1)[0]
new_head = r'''\cotefile{148}
\scanpage{6}

\noindent
\begin{minipage}[t]{.46\textwidth}
\begin{center}
U N I V E R S I T E\\
DES SCIENCES ET TECHNIQUES\\
DU LANGUEDOC\\
''' + r'\textasciicircum' * 13 + r'''
\end{center}
\end{minipage}\hfill
\begin{minipage}[t]{.50\textwidth}
\vspace{.9\baselineskip}
Montpellier, le 14 octobre 1983
\end{minipage}

'''
text = source_c.replace(old_head,new_head,1)
text = text.replace(r'''Diffusion : Liste A\\
MA/gs \hfill N° 4375''',r'''\begin{tabular}{@{}ll@{}}
Diffusion : & Liste A\\
MA/gs & N° 4375
\end{tabular}''')
text = text.replace(r'\uuline{'+heading+'}',separator,1)
text = text.replace(r'\unsure{A. Gentil}',signature,1)
(BASE/'work'/f'{PAGE}.tex').write_text(text+'\n',encoding='utf-8')

BOX = {
 'letterhead':[175,110,608,238], 'date':[848,145,1356,194],
 'reference':[184,290,550,365], 'degree':[448,426,1325,474],
 'ecology_separator':[432,489,1343,566], 'schedule':[231,883,1438,962],
 'duration':[229,1654,1326,1707], 'signature':[995,2037,1180,2158],
 'lower_number':[31,2268,91,2337]
}
R = dict(
 page=PAGE, reader='reader_b', line_count=46,
 layout='Upright typed notice. Forty-four typed text baselines are present, counting the separate right-hand date alongside the left letterhead; the caret row and equals row bring the typed-row count to 46. The university letterhead and service/reference block are upper left, with the date upper right. A centered two-line title is followed by the keyed equals row. Underlined field labels introduce the candidate, thesis title, schedule, director, laboratory, four abstract paragraphs, duration, and five-row jury list. The authorization block, handwritten signature, and separately typed A. GENTIL occupy the lower right. A lighter handwritten numeral is at lower left. The signature and marginal numeral are excluded from the typed-row count.',
 changes=[], decisions=[], unnumbered_decisions=[], inventory=[], doubts=[], notation=[],
 abbreviations=[],hand=[],legibility='',notes='',check_events=[],second_boxes=[],diff_coverage=[],deletion_insertion_check='')

R['changes'] = [
 dict(id=PAGE+'-01',place='Below the centered ecology heading',C=r'\uuline{'+heading+'}',H='[no witness H]',
      final=separator,
      evidence='The tight heading crop shows 56 separate pairs of horizontal bars, with a gap between each keyed character. They occupy the 56 typewriter columns below the heading. The actual equals row is recorded literally. Crop 148_scan006_ecology_separator.png, original box [432,489,1343,566].',
      crop=PAGE+'_ecology_separator.png',box=BOX['ecology_separator'],confidence='high',kind='other',error_sheet_kind='Other',differs_C=True,differs_H=False,marked_in_H=False,consequential=False),
 dict(id=PAGE+'-02',place='Handwritten signature above the separately typed A. GENTIL',C=r'\unsure{A. Gentil}',H='[no witness H]',
      final=signature,
      evidence='The crop exposes small detached strokes above a large open loop with an internal return, a long connected horizontal sweep ending in a tall narrow turn, a separate lower-left descending stroke, and a long lower flourish with two small left-end returns. These are graphically reproducible. The proposed full alphabetic name cannot be recovered letter by letter from them; the drawing carries an in-place doubt. Crop 148_scan006_signature.png, original box [995,2037,1180,2158].',
      crop=PAGE+'_signature.png',box=BOX['signature'],confidence='medium',kind='drawing or diagram',error_sheet_kind='Drawings and diagrams',differs_C=True,differs_H=False,marked_in_H=False,consequential=False)
]
R['decisions'] = [dict(id='M0075',decision='undecided',reading=r'\unsure{A. Gentil}; exposed signature strokes reproduced graphically',
      evidence='The large loop permits a G-like reading, but the initial cluster and the long contracted continuation do not expose the complete proposed A. Gentil. The printed A. GENTIL below is a separate source line and does not resolve the handwritten letters. All visible signature strokes, including its lower flourish, are retained in TikZ with a doubt marker.',
      crop='148_scan006_signature.png [995,2037,1180,2158]',confidence='low')]
R['doubts'] = [dict(place='Handwritten signature',reading=r'\unsure{A. Gentil}; graphic reproduction in the text',
      alternatives='A. Gentil is the unresolved C candidate; the complete alphabetic reading remains open.',confidence='low',
      reason='Detached initial strokes and a contracted, largely horizontal continuation prevent a letter-by-letter reading. The exposed loop and flourishes are clear enough to draw.')]

inventory = [
 ('text','University letterhead, upper left','U N I V E R S I T E; DES SCIENCES ET TECHNIQUES; DU LANGUEDOC','typed source'),
 ('text','Decorative row below the letterhead','Thirteen keyed carets','typed source'),
 ('text','Upper-right date','Montpellier, le 14 octobre 1983','typed source'),
 ('text','Service and diffusion/reference block','Service de la Scolarité; Diffusion : Liste A; MA/gs; N° 4375','typed source'),
 ('text','Centered first title baseline',"AVIS DE SOUTENANCE D'UNE THESE DE DOCTORAT DE 3e CYCLE",'typed source'),
 ('text','Centered ecology heading',heading,'typed source'),
 ('text','Separate keyed row below ecology heading','Fifty-six equals signs','typed source'),
 ('text','Candidate field','NOM et Prénom du candidat : MONTI Dominique','typed source'),
 ('text','Thesis-title field, four baselines','Titre de la thèse : opening quotation, Recherches sur l’optimisation','typed source'),
 ('text','Schedule field, two baselines','Date,-heure et lieu de soutenance prévus : Le 2 novembre 1983 à 15 heures; Salle de cours n° 9','typed source'),
 ('text','Director field','Nom du Directeur de thèse : M. AMANIEU','typed source'),
 ('text','Laboratory field, two baselines','Désignation du Laboratoire où la thèse est préparée : Laboratoire d’Hydrobiologie marine - U.S.T.L.','typed source'),
 ('text','Abstract first paragraph, three baselines','Analyse de l’ouvrage : Cette réflexion porte sur le problème du choix','typed source'),
 ('text','Abstract second paragraph, five baselines','Ce travail est basé sur la réalisation de différents sous-échantillonnages','typed source'),
 ('text','Abstract third paragraph, four baselines','Chaque sous-échantillonnage employé donnera naissance à une carte','typed source'),
 ('text','Abstract fourth paragraph, three baselines','Les résultats théoriques sont appliqués à l’étude de la macrofaune benthique','typed source'),
 ('text','Research-duration field','Durée approximative des recherches ayant abouti à la thèse : 3 ans','typed source'),
 ('text','Jury field and five-row list','Composition du jury Proposé : MM. AMANIEU M.; BLANC F.; FRONTIER S.; GRANDJOUAN G.; LASSERRE G.','typed source'),
 ('text','Lower-right authorization block, three baselines','P/ le Secrétaire Général,; L’Attachée Principale d’Administration; Scolaire et Universitaire,','typed source'),
 ('drawing','Handwritten signature below the authorization block','Detached initial strokes, large open loop and lower flourish','unattributed signature hand'),
 ('text','Typed name below the signature','A. GENTIL','typed source'),
 ('margin note','Lower-left corner','5','unattributed lighter hand')
]
for i,(kind,pos,first,hand) in enumerate(inventory,1):
    R['inventory'].append(dict(sheet_kind='typescript',hand=hand,element=f'E{i:02}',kind=kind,
                              position=pos,first_words_or_objects=first,transcribed='yes'))

R['notation'] = [
 dict(form='^^^^^^^^^^^^^',meaning='A separate keyed row below DU LANGUEDOC.',evidence='148_scan006 letterhead crop: thirteen individual carets.',scope='This row only.'),
 dict(form=equals_row,meaning='A separate keyed row below the ecology heading.',evidence='148_scan006 ecology_separator crop: 56 individual equals signs.',scope='This row only.'),
 dict(form='3e',meaning='The literal degree designation within the notice title.',evidence='148_scan006 degree crop: numeral and e occupy the same baseline.',scope='This occurrence only.')
]
R['abbreviations'] = [dict(form=a,expansion=b) for a,b in [
 ('N°','numéro (tentative)'),('n°','numéro (tentative)'),('3e','troisième (tentative)'),
 ('M.','Monsieur (tentative)'),('MM.','Messieurs (tentative)'),('P/','Pour (tentative)'),
 ('U.S.T.L.','Université des Sciences et Techniques du Languedoc (tentative, from this sheet’s letterhead)')]]
R['hand'] = [
 dict(habit='The signature contracts its continuation into a long nearly horizontal sweep with a narrow raised terminal turn, and adds a separate lower flourish.',
      places='Lower-right signature crop.',scope='One signature on this sheet; no identification of the writer or alphabetic expansion is established.',
      witness_errors='C offers A. Gentil as a doubt; that doubt remains, while the graphic strokes are retained.'),
 dict(habit='The lower-left numeral has a short upper bar, a descending left stroke, and a rounded lower return.',
      places='Lower-left marginal numeral crop.',scope='This numeral only; the lighter hand is unattributed.',witness_errors='C’s 5 is retained.')
]
R['legibility'] = ('The typed notice is sharply legible throughout both prepared halves. The horizontal paper crease crosses the first abstract '
 'paragraph without obscuring its letters. Field-label underlines are continuous; the two separate decorative rows expose individual typed '
 'characters. The letterhead crop confirms thirteen carets, and the heading crop exposes 56 equals signs. The date, reference number, degree '
 'designation, scheduled day/year/hour, room number, research duration, and lighter handwritten 5 were inspected on localized crops. The typed '
 'prose agrees with C, including Date,-heure, the opening quotation without a closing quotation at the end of the thesis title, the singular '
 'prélèvement in the first abstract paragraph, and the plural prélèvements in the next paragraph. C’s continuous double-underline rendering '
 'of the ecology separator is replaced with the keyed equals row. The handwritten signature has clear large contours and a separate lower '
 'flourish, but its compressed letters remain unresolved; its separately printed name is transcribed on its own line. No witness H is supplied '
 'for this page, so no comparison with H is claimed. Small isolated specks above the letterhead have no exposed textual sequence and are left '
 'outside the transcription.')
R['notes'] = ('This typed notice is dated 14 octobre 1983 and announces the thesis defense of MONTI Dominique in ECOLOGIE GENERALE ET APPLIQUEE '
 'OPTION ECOLOGIE AQUATIQUE. The title concerns sampling-plan optimization for mapping benthic communities and an application to the macrofauna '
 'of the étang de Pierre Blanche. The notice gives the proposed defense date and place, M. AMANIEU as thesis director, the laboratory, four '
 'abstract paragraphs, a duration of 3 ans, and a five-name jury. The abstract asks about sampling effort and precision, then describes different '
 'sub-samplings and comparisons of resulting maps with a reference map. These are reported as the wording of the notice; no mathematical '
 'verification or additional result is supplied. The literal Date,-heure, unaccented capital headings, baseline 3e, abbreviations, punctuation, '
 'and unmatched opening title quotation remain as printed. The signature is drawn without resolving its proposed name. The whole scan and '
 'both prepared halves were read once, and all nine crops were viewed. No OCR, outside research, other page source, or TeX compilation was used.')

def second(key,kind,reading):
    x0,y0,x1,y1=BOX[key]
    R['second_boxes'].append(dict(box=f'B{len(R["second_boxes"])+1:02}',kind=kind,
        x0=x0,y0=y0,x1=x1,y1=y1,reading=reading))
second('letterhead','Complete upper-left letterhead and separate keyed row',
       'U N I V E R S I T E\nDES SCIENCES ET TECHNIQUES\nDU LANGUEDOC\n'+'^'*13)
second('date','Complete upper-right dated baseline','Montpellier, le 14 octobre 1983')
second('reference','Complete two-line upper reference block',r'''Diffusion : Liste A\\MA/gs \qquad N° 4375''')
second('degree','Complete first centered title baseline',"AVIS DE SOUTENANCE D'UNE THESE DE DOCTORAT DE 3e CYCLE")
second('ecology_separator','Complete centered heading and separate keyed row',separator)
second('schedule','Complete two-line schedule and place field',
       r'''\uline{Date,-heure et lieu de soutenance prévus} : Le 2 novembre 1983 à 15 heures,\\
Salle de cours n° 9 - Université des Sciences et Techniques du Languedoc''')
second('duration','Complete lower field baseline',r'''\uline{Durée approximative des recherches ayant abouti à la thèse} : 3 ans''')
second('signature','Complete handwritten signature and its detached strokes',signature)
second('lower_number','Isolated lower-left marginal numeral',r'\margin{5}')
R['deletion_insertion_check'] = ('The typed text shows no readable cancellation, overwritten replacement, or inserted word. The unusual Date,-heure '
 'is typed as a comma followed by a hyphen and is retained without correction. The source field underlines and the two decorative keyed rows '
 'are preserved. The signature’s lower flourish lies beneath its connected writing and is reproduced with the rest of the signature. The '
 'separately typed A. GENTIL is retained beneath it. The lighter handwritten 5 is retained as a marginal number. The signature’s alphabetic '
 'reading stays doubtful; no omitted letters are supplied from the printed name.')

(BASE/'work'/f'{PAGE}_report.json').write_text(json.dumps(R,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(page=PAGE,changes=len(R['changes']),decisions=len(R['decisions']),
                     inventory=len(R['inventory']),doubts=len(R['doubts']),second_boxes=len(R['second_boxes']),
                     equals=len(equals_row),carets=13,crops=9),ensure_ascii=False))
