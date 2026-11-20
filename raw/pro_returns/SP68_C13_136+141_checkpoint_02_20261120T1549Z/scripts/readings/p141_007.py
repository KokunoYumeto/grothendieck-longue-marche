import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from workflow import Page
p=Page(141,7)
p.replace(r'\unsure{P. Gentil|A. Gentil}',r'P. Gentil')
p.decision('M1143','first','P. Gentil','Narrow upper-loop initial and connected surname, with a separate underline; the same signature form recurs on 141003 and 005, here more faintly.',confidence='medium')
p.extra_decision('faint stamp traces','first','TikZ traces without supplied letters','The crop shows only broken curved dots and two short stroke groups. No complete word can be recovered; C’s nonverbal approximation is retained rather than filling in the clearer stamp from 141005.',crop='141_scan007 (425,2130,615,2250)',confidence='high',original_mark='unmarked faint drawing')
for pos,words in [('top left letterhead','UNIVERSITE / DES SCIENCES ET TECHNIQUES / DU LANGUEDOC; twelve hyphens'),('top left office','Service de la Scolarité / MA/GJ / Diffusion : Liste A / N° : 5983'),('top right date','Montpellier, le 12 Novembre 1980'),('title','AVIS DE SOUTENANCE D’UNE THESE DE DOCTEUR INGENIEUR'),('discipline','SCIENCES ALIMENTAIRES Option GENIE ET TECHNOLOGIE ALIMENTAIRES - / FERMENTATIONS'),('separator','twenty-two typed hyphens'),('candidate','Nom et prénom du candidat : COMTE Francis'),('thesis title','Etude des isothermes d’adsorption de composés phénoliques.'),('defence','18 NOVEMBRE 1980 à 15 Heures 30 mn / Salle de cours n° 9 - U.S.T.L.'),('director','Monsieur le Professeur J. CROUZET'),('laboratory','Biochimie Appliquée'),('abstract heading','Résumé de la thèse'),('abstract first paragraph','Le tracé d’isothermes d’adsorption'),('abstract second paragraph','Parmi les différentes méthodes'),('abstract third paragraph','Par modélisation … En dépit des difficultés … ben-/zoïque … absorbant.'),('duration','Durée approximative … 3 ans'),('jury','MM. ROUZAUD J. / CROUZET J. / GOMA G. / COMBE P.'),('office signature block','P. le Secrétaire Général, / L’Attachée d’Administration Universitaire,')]: p.element('text',pos,words,sheet_kind='reused_typed',hand='typewriter')
p.element('text','below office block','P. Gentil, underlined signature',sheet_kind='reused_typed',hand='another unnamed hand')
p.element('text','below signature','A. GENTIL, underlined',sheet_kind='reused_typed',hand='typewriter')
p.element('drawing','lower left','faint broken stamp traces',sheet_kind='reused_typed',hand='print')
p.element('margin note','bottom left','6',sheet_kind='reused_typed',hand='another unnamed hand')
p.note('Reused university notice dated Montpellier, 12 Novembre 1980, announcing Francis COMTE’s engineering doctorate in food science, “Etude des isothermes d’adsorption de composés phénoliques.” Defence scheduled for 18 NOVEMBRE 1980, 15 Heures 30 mn, room 9 at U.S.T.L.; research duration 3 ans. The director, laboratory, abstract, four proposed jury members, official signature and faint stamp traces are transcribed. Pencil foliation 6.')
p.note('C agrees with the typed text, including salycilique, sujette à cautions, qui se sont liées, and absorbant, and the printed line-break ben-/zoïque. These are retained as written. The scientific claims of the abstract were not checked. No word is supplied for the nearly lost stamp.')
p.habit('The recurring signature form on 141003/005/007 supports the same P-shaped initial, with lower confidence where strokes have dropped out. Typed spellings on 007 remain independent of subject-matter expectations; no substantive C change was needed.')
p.notation('signature / faint stamp','Signature and typed A. GENTIL are separate elements; the nearly lost stamp is drawn as surviving strokes, not expanded from another leaf.')
p.abbr('mn','minutes');p.abbr('MM.','Messieurs');p.abbr('P. le','pour le')
p.save()
