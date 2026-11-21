from pathlib import Path
import json

root = Path('/workspace/scratch/15c7af26487b/edition')
page = '148_scan008'
packet = (root/'packets'/f'{page}.md').read_text()
source_C = packet.split('## Witness C', 1)[1].split('```tex', 1)[1].split('```', 1)[0].strip()

def dashes(n):
    return r'\texttt{' + '{}'.join('-' for _ in range(n)) + '}'

def keyed_heading(text, n):
    return '\\begin{tabular}{@{}l@{}}\n\\texttt{' + text + '}\\\\[-.6ex]\n' + dashes(n) + '\n\\end{tabular}'

head12 = keyed_heading('DU LANGUEDOC', 12)
head52 = keyed_heading("AVIS DE SOUTENANCE D'UNE THESE DE DOCTEUR INGENIEUR", 52)
head11 = keyed_heading('AUTOMATIQUE', 11)
signature = r'''\figure{\begin{tikzpicture}[x=.014cm,y=-.014cm,line cap=round,line join=round]
\draw[line width=.6pt] (48.6,8.7) .. controls (50.7,16.1) and (50.4,26.6) .. (48.8,32.9)
  .. controls (49.7,44.2) and (51.3,61.7) .. (51.1,73.8)
  .. controls (51.5,83.0) and (53.9,96.0) .. (56.1,102.5);
\draw[line width=.55pt] (36.5,30.7) .. controls (38.0,31.7) and (40.3,29.2) .. (40.6,29.8)
  .. controls (39.7,32.8) and (41.4,35.7) .. (43.4,36.0)
  .. controls (46.8,36.8) and (48.8,36.2) .. (49.4,33.0);
\draw[line width=.5pt] (36.5,30.7) .. controls (35.3,36.5) and (38.9,44.8) .. (41.4,52.5)
  .. controls (41.8,46.6) and (40.2,39.8) .. (40.6,33.7);
\draw[line width=.55pt] (62.9,40.0) .. controls (50.2,43.1) and (42.0,49.3) .. (40.0,58.2)
  .. controls (38.7,65.0) and (41.6,70.3) .. (48.7,73.5)
  .. controls (51.6,75.0) and (55.0,75.2) .. (57.0,74.8);
\draw[line width=.55pt] (66.4,39.9) .. controls (74.5,39.8) and (79.8,41.6) .. (80.3,44.8);
\draw[line width=.55pt] (64.9,64.2) .. controls (58.8,64.4) and (58.3,70.0) .. (67.6,71.5);
\draw[line width=.55pt] (75.8,62.9) .. controls (80.7,63.0) and (85.7,67.6) .. (81.4,71.2)
  .. controls (78.2,72.5) and (73.4,72.9) .. (70.7,73.4)
  .. controls (82.8,71.8) and (89.5,73.6) .. (99.0,70.5)
  .. controls (102.3,70.9) and (103.5,69.0) .. (106.7,69.7)
  .. controls (110.7,71.3) and (117.8,68.6) .. (124.5,70.2)
  .. controls (131.0,71.0) and (133.3,73.8) .. (140.4,72.8)
  .. controls (150.8,73.0) and (155.6,70.9) .. (160.7,66.3);
\draw[line width=.5pt] (157.5,46.7) -- (159.7,49.4);
\draw[line width=.5pt] (157.4,52.3) .. controls (158.1,56.2) and (159.6,53.5) .. (160.4,53.8)
  .. controls (163.0,55.1) and (161.1,58.4) .. (160.2,59.7)
  .. controls (159.1,60.3) and (160.5,63.9) .. (161.0,66.5)
  .. controls (162.8,72.3) and (166.0,77.4) .. (167.1,79.9);
\draw[line width=.5pt] (29.4,71.2) -- (32.4,70.3);
\draw[line width=.4pt] (26.6,72.9) -- (27.3,74.0);
\fill (66.0,75.2) circle[radius=.55];
\fill (79.6,88.3) circle[radius=.8];
\draw[line width=.6pt] (84.7,90.2) .. controls (96.1,91.7) and (107.2,91.2) .. (116.4,90.8)
  .. controls (128.7,91.5) and (139.7,90.3) .. (150.2,91.0)
  .. controls (160.7,90.2) and (169.1,91.3) .. (178.1,91.6);
\node[anchor=west] at (184,78) {\unsure{}};
\end{tikzpicture}}'''

text = source_C
text = text.replace(r'\uline{DU LANGUEDOC}', head12)
text = text.replace(r"\uline{AVIS DE SOUTENANCE D'UNE THESE DE DOCTEUR INGENIEUR}", head52)
text = text.replace(r'\uline{AUTOMATIQUE}', head11)
text = text.replace(r'\unsure{A. Gentil}', signature)
# Maintain the source's two upper blocks, without altering their words.
first_start = text.index(r'\begin{center}')
first_end = text.index(r'\end{center}', first_start) + len(r'\end{center}')
left_header = text[first_start:first_end].replace(r'\begin{center}', r'\begin{minipage}[c]{.43\linewidth}\centering', 1).replace(r'\end{center}', r'\end{minipage}', 1)
date_line = 'Montpellier, le 20 octobre 1983'
text = text[:first_start] + left_header + '\\hfill\n\\begin{minipage}[c]{.54\\linewidth}\\raggedleft\n' + date_line + '\n\\end{minipage}\n' + text[first_end:]
text = text.replace('\n\n' + date_line + '\n', '\n', 1)
text = r'\cotefile{148}' + '\n' + text + '\n'
(root/'work'/f'{page}.tex').write_text(text)

coords = {
 'letterhead':[145,108,585,222], 'reference':[285,311,460,352],
 'date':[855,192,1380,241], 'notice_heading':[572,440,1418,496],
 'subject_heading':[807,522,1010,575], 'schedule':[145,785,1398,835],
 'item_one':[146,1145,1492,1280], 'item_two':[145,1301,1545,1409],
 'item_three':[145,1428,1533,1508], 'duration':[140,1525,1210,1580],
 'signature':[910,1940,1110,2056], 'lower_numeral':[23,2287,90,2347]
}

def crop(name):
    return f'{page}_{name}.png'

changes=[]
def change(place, C, final, name, evidence, kind='other', sheet='Other', confidence='high'):
    changes.append({
      'id':f'{page}-{len(changes)+1:02d}', 'place':place, 'C':C,
      'H':'[no witness H]', 'final':final,
      'evidence':evidence + f' Crop {crop(name)}, original box {coords[name]}.',
      'crop':crop(name), 'box':coords[name], 'confidence':confidence,
      'kind':kind, 'error_sheet_kind':sheet, 'differs_C':True,
      'differs_H':False, 'marked_in_H':False, 'consequential':False
    })
change('Upper-left letterhead, DU LANGUEDOC and the keyed row immediately below',
       r'\uline{DU LANGUEDOC}', head12, 'letterhead',
       'The row contains twelve separately keyed horizontal dashes, each separated by white space. Both word cells and the intervening space are covered. The literal row retains their number and separate form.')
change('Main notice heading and its following keyed row',
       r"\uline{AVIS DE SOUTENANCE D'UNE THESE DE DOCTEUR INGENIEUR}", head52, 'notice_heading',
       'Fifty-two distinct horizontal dashes can be counted along the row; the last is one character column beyond the final R above. The heading has no accented capitals. The row is retained as individual keyed characters.')
change('Subject heading AUTOMATIQUE and its following keyed row',
       r'\uline{AUTOMATIQUE}', head11, 'subject_heading',
       'Eleven separated horizontal dashes occupy the eleven letter columns beneath AUTOMATIQUE. The gaps are visible even beneath the descending part of Q.')
change('Handwritten signature between the authorization and the typed name',
       r'\unsure{A. Gentil}', signature, 'signature',
       'The exposed ink comprises a tall left stroke, a narrow loop at its upper-left side, a broad left curve, two small open middle curves, a long low sweep, a short raised mark and descending stroke at the right, and a separate dotted lower flourish. These contours are reproduced directly. C proposes A. Gentil, but the connected strokes do not securely expose the complete alphabetic sequence; the adjacent in-place doubt remains.',
       'drawing or diagram','Drawings and diagrams','medium')

inventory=[]
def inv(kind, position, first, hand='typed source'):
    inventory.append({'sheet_kind':'typescript','hand':hand,
      'element':f'E{len(inventory)+1:02d}','kind':kind,'position':position,
      'first_words_or_objects':first,'transcribed':'yes'})
inv('text','Upper left, first three text lines and keyed row','U N I V E R S I T E / DES SCIENCES ET TECHNIQUES / DU LANGUEDOC; twelve dashes')
inv('text','Upper left, administrative block','Service de la Scolarité / MA/GJ / Diffusion : Liste A / N° : 4679')
inv('text','Upper right','Montpellier, le 20 octobre 1983')
inv('text','Upper central-right heading','AVIS DE SOUTENANCE D’UNE THESE DE DOCTEUR INGENIEUR; fifty-two dashes')
inv('text','Below the notice heading','AUTOMATIQUE; eleven dashes')
inv('text','First form line','Nom et prénom du candidat : SITOHANG Benhard')
inv('text','Following two typed baselines','Titre de la thèse : LINAIRE : SYSTEME DE GESTION DE BASES DE DONNEES RELATIONNELLES / SUR MICRO-ORDINATEUR.')
inv('text','Schedule line','Date, heure et lieu de soutenance prévus: 28 OCTOBRE 1983 à 14h30 - CRIG USTL')
inv('text','Director line','Nom du Directeur de thèse : Monsieur le Professeur B. FILLIATRE')
inv('text','Laboratory line','Désignation du laboratoire où la thèse est préparée : CRIG USTL')
inv('text','Abstract label','Résumé de la thèse :')
inv('text','First abstract paragraph, three source baselines',"La conception et la réalisation d'un Système de Gestion de Bases de Données Relationnelles")
inv('text','Abstract lead-in',"Nous mettons l'accent sur trois points principaux :")
inv('text','First numbered paragraph, four source baselines',"1. BOUCLE MULTI-NIVEAUX ; c'est une technique du traitement de données, permettant")
inv('text','Second numbered paragraph, three source baselines','2. STRUCTURE INTERNE DE LA BASE ; elle est multiple, afin de préserver au mieux les')
inv('text','Third numbered paragraph, two source baselines',"3. L'adaptation sur un micro-ordinateur du langage de manipulation de QUERY-BY-EXAMPLE")
inv('text','Research duration line','Durée approximative des recherches ayant abouti à la thèse : 2 ans')
inv('text','Jury label','Composition du jury proposé :')
inv('text','Jury list, five source baselines','MM. FILLIATRE B. / CHEIN M. / PICHAT E. / PIROTTE A. / PRUNET F.')
inv('text','Lower right authorization, three source baselines',"P. le Secrétaire Général, / l'Attachée Principale d'Administration Scolaire / et Universitaire,")
inv('drawing','Below the authorization and above the typed name','Tall crossing stroke, looped left cluster, long connected sweep, right rising marks, separate lower flourish with dot','unattributed signature hand')
inv('text','Below the signature','A. GENTIL')
inv('margin note','Extreme lower-left margin','7','unattributed lighter hand')

second_boxes=[]
def second(kind, box, reading):
    second_boxes.append({'box':f'B{len(second_boxes)+1:02d}', 'kind':kind,
       'x0':box[0],'y0':box[1],'x1':box[2],'y1':box[3],'reading':reading})
second('Final letterhead line and its separate keyed decoration; two complete baselines only',
       [260,175,477,222], head12)
second('Upper-left administrative reference line only; preceding line excluded',
       [285,316,460,352], 'N° : 4679')
second('Upper-right typed date line; complete baseline', coords['date'], 'Montpellier, le 20 octobre 1983')
second('Main notice heading and separate keyed decoration; both complete baselines',coords['notice_heading'],head52)
second('Subject heading and separate keyed decoration; both complete baselines',coords['subject_heading'],head11)
second('Schedule field; complete underlined label and typed entry',coords['schedule'],r'\uline{Date, heure et lieu de soutenance prévus:} 28 OCTOBRE 1983 à 14h30 - CRIG USTL')
second('First numbered paragraph, first baseline only; later baselines excluded',
       [146,1145,1492,1183], "1. BOUCLE MULTI-NIVEAUX ; c'est une technique du traitement de données, permettant")
second('Second numbered paragraph, first baseline only; later baselines excluded',
       [145,1301,1545,1341], '2. STRUCTURE INTERNE DE LA BASE ; elle est multiple, afin de préserver au mieux les')
second('Third numbered paragraph; both complete baselines',coords['item_three'],
       "3. L'adaptation sur un micro-ordinateur du langage de manipulation de QUERY-BY-EXAMPLE\n(langage de haut niveau, interactif, et tabulaire).")
second('Duration field; complete underlined label and typed entry',coords['duration'],r'\uline{Durée approximative des recherches ayant abouti à la thèse} : 2 ans')
second('Complete handwritten signature and lower flourish only; surrounding typescript excluded',coords['signature'],signature)
second('Lower-left handwritten marginal numeral only; page border is context',coords['lower_numeral'],r'\margin{7}')

report={
 'page':page,'reader':'reader_b','line_count':44,
 'layout':'Upright typescript notice. A left university letterhead and administrative block stand opposite the date at upper right. A notice heading with its own keyed dash row and a separate subject heading precede the form entries. The abstract has a lead-in and three numbered paragraphs. Duration and jury follow; a lower-right authorization block, handwritten signature and typed name end the notice. A lighter handwritten numeral sits at the extreme lower-left corner. Reading follows these blocks from top to bottom. The 44-line count includes the three keyed decoration rows and the separate date baseline, and excludes the signature drawing and marginal numeral.',
 'changes':changes,
 'decisions':[{'id':'M0088','decision':'undecided','reading':r'\unsure{}',
    'evidence':'The exact retained marker is attached to the directly drawn signature. The tall stem and connected curves are graphically legible; their contracted joins leave the complete letter sequence unresolved. C\'s candidate is A. Gentil. The typed A. GENTIL below has been transcribed separately and has not supplied missing signature letters.',
    'crop':f"{crop('signature')} {coords['signature']}",'confidence':'low'}],
 'unnumbered_decisions':[],
 'inventory':inventory,
 'doubts':[{'place':'Handwritten signature above the typed A. GENTIL',
    'reading':r'\unsure{}', 'alternatives':'C proposes A. Gentil; no complete alternative alphabetic reading is secured by the connected strokes.',
    'confidence':'low', 'reason':'Contour visibility is good, but the signature contracts several possible letter joins into long strokes. The whole visible shape and a doubt marker are retained in the text and B11.'}],
 'notation':[
    {'form':dashes(12),'meaning':'Literal separated keyed decoration beneath the final letterhead line','evidence':f"{crop('letterhead')} {coords['letterhead']}: twelve individually visible dashes",'scope':'This one row only'},
    {'form':dashes(52),'meaning':'Literal separated keyed decoration beneath the notice heading','evidence':f"{crop('notice_heading')} {coords['notice_heading']}: fifty-two dashes, final column extending beyond R",'scope':'This one row only'},
    {'form':dashes(11),'meaning':'Literal separated keyed decoration beneath the subject heading','evidence':f"{crop('subject_heading')} {coords['subject_heading']}: eleven dashes",'scope':'This one row only'}
 ],
 'abbreviations':[
    {'form':'N°','expansion':'numéro (tentative)'},
    {'form':'USTL','expansion':'Université des Sciences et Techniques du Languedoc (tentative, using this page’s letterhead)'},
    {'form':'MA/GJ','expansion':'No expansion established by this page.'},
    {'form':'CRIG','expansion':'No expansion established by this page.'},
    {'form':'h','expansion':'heure(s) (tentative)'},
    {'form':'MM.','expansion':'Messieurs (tentative)'},
    {'form':'P.','expansion':'Pour (tentative)'}
 ],
 'hand':[
    {'habit':'The typed headings use separated, evenly spaced dash characters; the form labels have continuous underlining. Capitals lack added accents, and names, abbreviations and wording are kept as visibly typed.',
     'places':'Three heading rows and the body fields','scope':'This page’s inspected typescript','witness_errors':'C represents each keyed heading row by an underline macro; changes 01–03 retain the individual keys and counts.'},
    {'habit':'The signature combines a tall stem, a narrow upper loop, broad lower curves, a long near-horizontal sweep and an independent lower dotted flourish.',
     'places':'Signature between authorization and typed name','scope':'This signature only','witness_errors':'M0088 stays unresolved; change 04 supplies the visible contours and an in-place doubt.'},
    {'habit':'The lighter marginal numeral has a short curved top, a descending stem and a crossing middle stroke.',
     'places':'Extreme lower-left corner','scope':'This single numeral','witness_errors':'C reading 7 confirmed from its own crop.'}
 ],
 'legibility':'The typescript is dark and well separated throughout this page. A horizontal paper crease runs near the first numbered paragraph, but its four text baselines remain readable in the prepared half and tight crop. The three heading rows resolve into individually keyed dashes, and all dates, reference digits, numbered items and duration are exposed. The lighter lower-left numeral retains a visible top, stem and cross stroke and reads 7. The signature’s contours are exposed clearly; its compressed letter joins retain alphabetic uncertainty. Line-by-line comparison found C’s typed prose, personal names, abbreviations, capitalization and punctuation supported by this page. The substantive departures are the three keyed rows and the direct reproduction of the unresolved signature. No witness H is supplied for this page.',
 'notes':'This is an administrative notice rather than a manuscript mathematical development. The upper date is 20 octobre 1983. The candidate field reads SITOHANG Benhard and the subject is AUTOMATIQUE. The title and opening abstract call the system LINAIRE; the notice gives the defense as 28 OCTOBRE 1983 à 14h30 - CRIG USTL. Its abstract describes design and realization of a relational database management system on a microcomputer, then identifies BOUCLE MULTI-NIVEAUX, a multiple internal database structure, and adaptation of QUERY-BY-EXAMPLE as three areas of emphasis. These are statements reported from the notice; no technical performance or proof claim has been independently checked. The source spelling équi-joint and all visible capitals are preserved. The notice states 2 ans, names Monsieur le Professeur B. FILLIATRE as director and gives the five-person jury exactly as typed. The authorization retains P. le and the lower-case initial l of l’Attachée. The graphic signature stays alphabetically doubtful; the typed A. GENTIL below is clear. The whole scan and both prepared halves were inspected, followed by all twelve tight crops. Second-reading targets are localized to complete heading/entry baselines, the numbered paragraph starts, the complete signature and the marginal numeral; they do not use a broad central-page target. In the item_one crop, the final letter of a later context baseline reaches the crop boundary; the independent second-reading target is confined to the fully exposed first baseline. The three dash counts are transcription observations and are not mathematical check events.',
 'check_events':[],
 'second_boxes':second_boxes,
 'diff_coverage':[],
 'deletion_insertion_check':'C contains no deletion or insertion wrappers on this page. Whole-page and half-page review shows no cancelled text, overtyped textual correction or interlinear insertion. The signature’s long crossing strokes and independent lower flourish are retained as drawing contours; the keyed heading rows and body underlines are retained at their respective headings and labels. The separate lower-left 7 is retained as a marginal note. No source text has been suppressed or silently expanded.'
}
(root/'work'/f'{page}_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(f'Wrote {page}.tex and report: {len(changes)} changes, {len(inventory)} inventory entries, {len(second_boxes)} second boxes, {len(coords)} crops.')
