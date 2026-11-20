import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from workflow import Page
p=Page(141,5)
p.replace(r'\unsure{P. Gentil|A. Gentil}',r'P. Gentil')
p.decision('M1136','first','P. Gentil','Tall initial with one narrow upper loop, followed by the compressed surname and underlining flourish, matching the signature form on 141003. The typed A. GENTIL remains separate.',confidence='medium')
p.decision('M1137','undecided',r'\unsure{ACAD}','A and C are distinct beside the outer circle; the following two broken forms admit A and D, but parts of the impression are physically missing.',crop='141_scan005 (395,1840,625,2150)',confidence='low')
p.decision('M1138','undecided',r'\unsure{SCIENCES}','The diagonal stamped word has only disconnected edges and dots at several letters; SCIENCES remains a possible reading, not a resolution.',crop='141_scan005 (395,1840,625,2150)',confidence='low')
# Inventory follows the primary reader’s explicit top-to-bottom order.
for kind,pos,words,hand in [
 ('text', 'top left', 'UNIVERSITE / DES SCIENCES ET TECHNIQUES / DU LANGUEDOC; twelve hyphens', 'typewriter'),
 ('text', 'below letterhead', 'Service de la Scolarité / MA/GJ / Diffusion : Liste A / N° : 5890', 'typewriter'),
 ('text', 'top right', 'Montpellier, le 7 Novembre 1980', 'typewriter'),
 ('text', 'title', 'AVIS DE SOUTENANCE … DOCTORAT DE 3ème CYCLE', 'typewriter'),
 ('text', 'discipline', 'ECOLOGIE GENERALE ET APPLIQUEE Opt. ECOLOGIE TERRESTRE', 'typewriter'),
 ('drawing', 'under discipline', 'horizontal separator', 'another unnamed hand'),
 ('text', 'candidate', 'Nom et prénom … MICHELLAND Dominique', 'typewriter'),
 ('text', 'thesis title', 'SURVIE EN MILIEU INSULAIRE : QUELLE STRATEGIE ? LE CAS DES MESANGES EN CORSE.', 'typewriter'),
 ('text', 'defence', '17 NOVEMBRE 1980 à 15 Heures / Salle de cours n° 9 - USTL', 'typewriter'),
 ('text', 'directors', 'MM. LEGENDRE et BLONDEL', 'typewriter'),
 ('text', 'laboratory', 'Laboratoire de Systématique et d’Ecologie Méditerranéennes', 'typewriter'),
 ('text', 'abstract heading', 'Résumé de la thèse', 'typewriter'),
 ('text', 'abstract paragraph 1', 'En Corse les populations de mésanges', 'typewriter'),
 ('text', 'abstract paragraph 2', 'A la lumière de la théorie de la biogéographie insulaire', 'typewriter'),
 ('text', 'abstract paragraph 3', 'Ce travail montre les répercussions', 'typewriter'),
 ('text', 'duration', 'Durée approximative … 2 ans', 'typewriter'),
 ('text', 'jury', 'MM. AMANIEU / BLONDEL / BOURLIERE / THALER / ISENMANN', 'typewriter'),
 ('text', 'lower right office', 'P. le Secrétaire Général, / l’ Attachée d’Administration Universitaire,', 'typewriter'),
 ('text', 'above typed name', 'P. Gentil, underlined signature', 'another unnamed hand'),
 ('text', 'typed signature label', 'A. GENTIL', 'typewriter'),
 ('drawing', 'lower left', 'partial circular stamp and faint ACAD / SCIENCES', 'print'),
 ('margin note', 'bottom left', '4', 'another unnamed hand'),
]:
 p.element(kind,pos,words,sheet_kind='reused_typed',hand=hand)
p.doubt('stamp, curved rim',r'\unsure{ACAD}','Faint A/D and lost impression')
p.doubt('stamp, diagonal word',r'\unsure{SCIENCES}','Several letter edges absent')
p.note('Reused university notice dated Montpellier, 7 Novembre 1980, announcing Dominique MICHELLAND’s third-cycle ecology thesis, “SURVIE EN MILIEU INSULAIRE : QUELLE STRATEGIE ? LE CAS DES MESANGES EN CORSE.” The scheduled defence is 17 NOVEMBRE 1980 at 15 Heures, room 9 at USTL; research duration 2 ans. It records the directors, laboratory, abstract, five proposed jury members, official signature and faint stamp. Pencil foliation 4. The ecological assertions are transcribed, not independently checked.')
p.habit('The same narrow-loop signature initial appears on 141003 and 005. It is transcribed as P., distinct from the machine-typed A.; this is a reading of the mark, not an identification of a different person. No change to C’s typed words was needed on this leaf.')
p.notation('P. Gentil / A. GENTIL','Handwritten signature with P-shaped initial above an independently typed A. GENTIL.')
p.abbr('Opt.','option');p.abbr('P. le','pour le');p.abbr('MM.','Messieurs')
p.save()
