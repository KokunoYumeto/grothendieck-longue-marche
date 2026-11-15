"""Materialize the responsible reader's reviewed locators/confidence decisions.
This reads only the already transcribed page files. The maps below were supplied
by the reader after the two image-reading passes; they are not OCR positions.
"""
from pathlib import Path
from datetime import datetime,timezone
import json,re
from build_deliverables import extract_doubts
ROOT=Path(__file__).resolve().parents[1]
PREFIX='MPL_15_195-228+18_002-017'
LOC={
(15,195):[(3,'top opening 2° paragraph'),(5,'upper crossed paragraph'),(7,'crossed label above (i)'),(9,'upper (i) display'),(15,'middle Connexions paragraph after (ii)'),(17,'lower cancelled paragraph above (iii)'),(18,'left of lower cancellation, Vérifier'),(20,'bottom (iii) paragraph'),(22,'left vertical marginal note')],
(15,197):[(2,'top continuation paragraph'),(4,'middle paragraph before (b)'),(6,'middle comparison formula'),(9,'lower (b) paragraph'),(11,'bottom NB')],
(15,198):[(15,'final typed n° 4 paragraph, last sentence')],
(15,199):[(2,'top continuation'),(7,'upper (iv) formula'),(9,'upper-middle cancelled paragraph'),(18,'middle D’ailleurs paragraph'),(24,'lower valuation paragraph'),(25,'last incomplete line')],
(15,200):[(3,'typed header, roman sheet reference')],
(15,201):[(2,'upper continuation paragraph and bracket'),(4,'left marginal definition of a'),(6,'above central comparison diagram'),(10,'central diagram, lower-left overwritten object'),(17,'bottom paragraph on operations')],
(15,203):[(2,'upper paragraph and insertions'),(10,'middle real comparison formula'),(15,'middle labels beneath tau product'),(19,'lower paragraph with inserted real-case explanation'),(23,'bottom bracket on real Frobenius')],
(15,204):[(7,'typed § 1, n° 2 paragraph')],
(15,205):[(2,'top opening paragraph'),(4,'upper transition to filtration'),(6,'middle filtration formula'),(13,'bottom paragraph and crossed final continuation')],
(15,207):[(8,'left circled correction faux'),(11,'middle paragraph Quant aux'),(13,'middle crossed clauses'),(21,'left marginal question beside characteristic-p paragraph'),(30,'lower paragraph on the fibre category')],
(15,209):[(5,'upper paragraph on principal homogeneous fibrations'),(10,'central table, first two point types')],
(15,210):[(14,'typed Example 2, first lattice occurrence'),(16,'typed Example 2, remaining lattice occurrences')],
(15,211):[(12,'upper characteristic-p branch'),(15,'upper circled F,V'),(21,'upper-middle generalized-points branch'),(50,'lower heading car p'),(62,'bottom finite-field branch')],
(15,213):[(12,'upper NB, added surname'),(14,'upper question on places'),(18,'middle category membership'),(25,'middle fundamental-group definitions'),(29,'lower comparison with topological point'),(33,'last Hodge-structure paragraph')],
(15,215):[(2,'top continuation on Hodge and Tate'),(9,'upper line preceding Serre example'),(13,'middle bracket: real base field'),(18,'middle bracket with cancellations and real-point involution'),(29,'lower fibre-functor display'),(34,'bottom Pb on varying Hodge structure')],
(15,217):[(3,'top modular-variety paragraph'),(12,'upper-middle possible characterization paragraph'),(18,'middle inserted bubble on motivic pointing')],
(15,219):[(5,'top two places and fibre functors'),(10,'upper-middle cancelled line Soient'),(12,'middle reduction paragraph'),(15,'middle field-definition correction'),(17,'inserted numbered condition before (a)'),(21,'middle (a) comparison'),(33,'lower descent and field-of-definition argument'),(39,'lower-left crossed diagram'),(42,'transition before (b)'),(45,'lower (b) condition and comparison'),(49,'bottom cancellations and appended argument')],
(15,221):[(4,'top revised countable-field opening'),(19,'lower inserted condition before 2)'),(21,'lower 2) paragraph'),(25,'lower comparison of restrictions'),(27,'left lower crossed marginal formula'),(30,'bottom cancelled continuation')],
(15,223):[(3,'top proposed integral cohomology rings'),(13,'middle places and principal homogeneous fibrations'),(22,'middle continuation and deletions'),(24,'lower discrete-group formula'),(27,'lower naming sentence'),(32,'bottom/right marginal compatibility warning')],
(15,225):[(2,'top crossed marginal note'),(4,'top opening on places'),(8,'upper crossed expectation and added theorem reference'),(18,'large central cancelled proof attempt'),(26,'left marginal warning and diagram'),(32,'bottom punctured-line example')],
(15,227):[(6,'upper inserted parenthesis'),(18,'lower moduli paragraph and corrections')],
(18,2):[(3,'cover, parenthesized attribution')],
(18,5):[(2,'top heading'),(10,'upper numbered descriptions 1–4'),(20,'middle local-field bracket'),(23,'middle 3-prime insertion'),(26,'lower 2-prime description'),(31,'lower 6-prime description and bracket')],
(18,6):[(6,'left main extension diagram'),(12,'upper-right explanatory paragraph'),(37,'lower-left splitting identity'),(41,'bottom item 1°'),(43,'bottom item 2°, quotient group'),(45,'bottom character map')],
(18,7):[(10,'typed Remarque 7.13.11 with handwritten corrections'),(15,'lower square (7.13.12), right vertical arrow'),(18,'bottom unfinished typed paragraph')],
(18,9):[(4,'upper definition of mixed Hodge structure'),(7,'upper twist definition and correction'),(10,'middle first weight-shift formula'),(15,'middle introductory line to graded quotient'),(22,'lower iteration paragraph')],
(18,11):[(33,'upper-left Fil/Big definitions'),(39,'upper-right unipotent-radical note'),(47,'upper-right central cocharacter annotation'),(50,'central-right NB and quotient components'),(55,'right NB on epsilon and j-prime'),(63,'middle Big-to-Fil fibration paragraph'),(67,'right boxed Dynkin/Weyl marginal note'),(72,'middle commutative square'),(89,'lower field diagram, bottom labels'),(91,'small footer beneath field diagram'),(93,'crossed field inclusion below the diagram')],
(18,12):[(2,'top cancelled continuation'),(4,'upper cancelled conjecture'),(6,'upper degree-of-transcendence formula'),(8,'line below formula and its insertion'),(10,'left upper slanted marginal note'),(12,'middle cancelled corollary'),(14,'left middle cancelled marginal note'),(19,'lower period tuple, four factors'),(24,'lower Schneider paragraph and determinant relation'),(26,'last paragraph on transcendental j')],
(18,13):[(4,'upper motivic-group description'),(6,'question a)'),(8,'question b) and its deletions'),(10,'question c), overwritten opening line')],
(18,14):[(4,'cover subtitle, middle line')],
(18,15):[(4,'top X-definition, crossed word'),(13,'upper comparison diagram, scalar line and crossed annotation'),(14,'upper comparison diagram, crossed lower object and arrow'),(19,'right marginal local Poincare construction'),(24,'middle reduction paragraph'),(26,'lower NB on the multiplier')],
(18,17):[(2,'top-left oblique marginal note'),(4,'upper opening paragraph'),(6,'upper integral identity'),(7,'annotation beneath the integrals'),(21,'crossed heading before last diagram'),(23,'last diagram, upper-left object'),(24,'last diagram, upper-middle object'),(25,'last diagram, upper-right object'),(26,'last diagram, lower-left object'),(27,'last diagram, lower-middle object and comparison label'),(28,'last diagram, lower-right object'),(30,'bottom unfinished sentence')]
}
# Additional local low-confidence decisions from the reader's second pass.
LOW_RANGES={
(15,195):[(5,7),(15,18),(22,22)], (15,199):[(9,9),(25,25)],
(15,205):[(13,13)],(15,207):[(8,8),(21,21)],
(15,219):[(10,15),(31,49)],(15,221):[(3,3),(20,30)],
(15,223):[(26,27),(32,32)],(15,225):[(2,2),(7,18),(26,26)],
(15,227):[(17,18)],(18,11):[(50,50),(67,67),(87,93)],
(18,12):[(2,26)],(18,13):[(8,10)],(18,15):[(13,14),(26,26)],
(18,17):[(6,7),(21,30)]}
rows=[]
for e in json.loads((ROOT/'records/expected_pages.json').read_text()):
 key=(e['cote'],e['scan']);p=ROOT/'pages'/f'{PREFIX}_{key[0]}_scan{key[1]:03d}.tex';s=p.read_text()
 for d in extract_doubts(s):
  options=LOC[key];position=next((v for last,v in options if d['tex_line']<=last),None);assert position,(key,d)
  low=(d['macro']=='illegible' or bool(d['alternatives']) or any(a<=d['tex_line']<=b for a,b in LOW_RANGES.get(key,[])))
  rows.append({'cote':key[0],'scan':key[1],'offset':d['offset'],'argument':d['argument'],'confidence':'low' if low else 'medium','source_location':position})
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
result={'reviewed_by':'responsible reader','reviewed_utc':now,'basis':'Local readings reviewed against the images during the first reading, second audit and notation comparison. Explicit alternatives remain low; individually identified weak cancellations and marginal text are low; other single doubtful readings are medium. No reading is elevated to certainty by context.','rows':rows}
(ROOT/'records/doubt_review.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print('Reviewed doubt rows:',len(rows))
print('Confidence:',{v:sum(x['confidence']==v for x in rows) for v in ['high','medium','low']})
