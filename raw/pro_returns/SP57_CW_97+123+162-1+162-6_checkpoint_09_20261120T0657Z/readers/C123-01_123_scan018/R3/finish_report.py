from pathlib import Path
import json
base=Path('out/readers/C123-01_123_scan018/R3')
r=json.loads((base/'report.json').read_text())
C=Path('packets/C123-01_123_scan018/C.tex').read_text()
crops={name:dict(bbox=box,crop='readers/C123-01_123_scan018/R3/crops/'+name+'.jpg') for name,box,width in json.loads((base/'unresolved_loci.json').read_text())}
Q=[]
def q(place,c,decision,evidence,confidence='high',crop=None,bbox=None):
 loc=crops[crop] if crop else dict(crop=None,bbox=bbox)
 Q.append(dict(place=place,C=c,decision=decision,evidence=evidence,crop=loc['crop'],bbox=loc['bbox'],bbox_source='whole image',confidence=confidence))
q('Exactes insertion: dernière',r'\unsure{dernière}','Retain uncertainty.','The final impressions overlap; no alternative word can be securely separated.','medium','01_exactes')
q('After rat/k); il',r'\unsure{il}','Represent initial i, an o/l overlay with unresolved chronology, and a tentative cancelled n.','Both oval and l contours survive, followed by an x-filled cell.','low','02_il')
q('Deleted Hom expression: arrow',r'\underline{G}_m\unsure{\to}T','Retain uncertain rightward arrow.','The shaft partly survives but the head meets cancellation and T.','medium','05_deleted_hom')
q('After stable par: Gamma prime',r"\unsure{\Gamma'|\Gamma}",'Retain both candidates.','The right downward hook joins the top bar; prime versus terminal remains unresolved.','medium','07_gamma')
q('First filtration scheme',r'\unsure{\underline{\phi}|\underline{\varnothing}}','Read underlined varnothing without glyph doubt.','The oval and rising diagonal slash are distinct from a vertical phi stem.','high','09_phi_il_est')
q('Right-edge schéma',r'\unsure{schéma}','Retain word with doubt.','The last a is partly outside the right edge.','medium','08_schema_edge')
q('On a: deleted un homo',r'\deleted{\unsure{un homo}}','Remove lexical doubt and retain deletion.','Letter contours are recoverable beneath the x overstrikes.','high','13_un_homo')
q('Before foncteurs: da/du',r'\unsure{da|du}',r'Use \unsure{da|de}.','The closed upper area and middle bar admit a/e, while an open u is not secure.','low','15_da_foncteurs')
q('Deuxième: deleted d',r'\deleted{\unsure{d}}','Read deleted d without doubt.','Tall ascender, top serif and lower bowl remain under the x.','high','16_deuxieme_en')
q('Round subscripts, first G',r'G_{\unsure{o|0}}','Retain first o/0 doubt and use o subsequently.','The small lowered ring resembles lowercase o; numerical identity is not determined by form.','medium','03_first_round_index')
q('Three rationelle occurrences',r'rationelle','Retain one n at all three places.','The conjugaison line, inserted orbite line and ST body each have one n between o and e; first and third were settled on half a.','high','10_insertion_tail')
q('Supposons fixé une classe',r'Supposons fixé une classe','Retain fixé without a final e.','The acute-accented é is followed directly by blank space before une; half a evidence.','high',bbox=[1095,253,1563,291])
q('Exactes quotation',"et ``exactes',cette",'Retain two opening strokes, one closing stroke, comma.','Only one separated high stroke follows exactes.','high','01_exactes')
q('Automorphism name',r'\operatorname{Auext}','Retain Auext.','Five typed cells read A-u-e-x-t; half a evidence.','high',bbox=[1279,516,1388,553])
q('Before display: morphismesde',r'morphismesde','Retain no space.','s and d occupy adjacent cells.','high','13_un_homo')
q('After display: article, plural and accents',r'\unsure{da|du} foncteurs fibres',r'Use \unsure{da|de} foncteurs fibres.','The final s in foncteurs is visible and neither word is accented. des and fibrés are not ink readings.','low','15_da_foncteurs')
q('Lévi alternative: où',r'où un sous-groupe','Retain grave accent.','A detached sloping accent lies above u; half b evidence.','high',bbox=[1350,1103,1484,1149])
q('Repeated C audit: preferred da candidate',r'\unsure{da|du}','Keep da first, allow de, do not assert du.','Same unresolved glyph and same single crop as the earlier article question; no additional view.','low','15_da_foncteurs')
q('First tensor/circled-x doubt',r'\unsure{\otimes|\mathbin{\text{\textcircled{x}}}}',r'Read \mathbin{\text{\textcircled{x}}}.','The typewriter x has a projecting low serif within and across the oval.','high','04_first_tensor')
r['c_doubts']=Q
I=[]
def inv(element,kind,pos,words,hand='typed with handwritten corrections',sheet='typescript'):
 I.append(dict(sheet_kind=sheet,hand=hand,element=element,kind=kind,position=pos,first_words_or_objects=words,transcribed='yes'))
inv('Underlined heading','text',[267,126,1656,170],'Interprétations en termes de filtrations du foncteur oubli','typed')
inv('Heading deletion','deletion',[1355,126,1656,170],'sur la catégorie','typed x overstrikes')
inv('Opening body and filtration hypothesis','text',[266,191,1648,424],'des représentations linéaires ... Supposons fixé une classe ... rat/k')
inv('Exactness interlinear sentence','insertion',[579,210,1486,250],"et ``exactes',cette dernière cond. aut. si car.k=0",'typed')
inv('Exactness joined enclosure','drawing',[577,222,1490,300],'two lower curved runs joining at tensoriel','handwritten')
inv('Raised class c','insertion',[1547,226,1585,263],'c','handwritten')
inv('Class c V-shaped leader','drawing',[1535,227,1599,286],'curved left descent and rising right stroke','handwritten')
inv('Conjugacy/rationality sentence','insertion',[268,293,889,327],'conjugaison, rationelle sur k, de','typed')
inv('Conjugaison enclosure','drawing',[258,307,901,361],'curve returning before telles','handwritten')
inv('Overlapping letters after rat/k','text',[414,389,477,424],'i followed by o/l overlap','typed overlapping impressions')
inv('Cancelled cell after overlap','deletion',[449,390,478,424],'tentative n','typed x overstrike and dense further ink')
inv('Chevalley and quotient interpretation body','text',[267,387,1640,622],'il revient au même ... Hom(G_m,T_o)/W=M/W')
inv('Deleted un','deletion',[1018,389,1071,424],'un','typed x overstrikes')
inv('Deleted first homomorphisme','deletion',[414,454,684,491],'homomorphisme','typed x overstrikes')
inv('Inserted Galois subgroup Gamma','insertion',[1203,486,1247,522],'Gamma','handwritten')
inv('Gamma insertion curve','drawing',[1210,496,1266,562],'curved return before de','handwritten')
inv('Algebraic-closure bar','insertion',[393,578,420,597],'bar over k in Gal','handwritten')
inv('Deleted second homomorphisme and map','deletion',[743,578,1125,632],'homomorphisme G_m arrow T','typed letters and x strikes; partly handwritten formula')
inv('Weyl chamber and filtration-scheme body','text',[267,646,1656,818],'la chambre de Weyl ... stabilisateur des points des paraboliques')
inv('Stable-par Gamma fill','text',[1191,650,1230,678],'Gamma with possible prime','handwritten')
inv('First filtration-scheme glyph and class c fill','text',[266,716,836,774],'underlined slashed oval with c; classe c','handwritten formula fills')
inv('Subscheme orbit sentence','insertion',[266,745,1605,785],"il est ~ un sous-schéma ouvert de Par(G), orbite rationelle sous G, soit c',",'typed body; handwritten il, similarity sign and soit c-prime')
inv('Small similarity-sign leader','drawing',[355,739,401,784],'bent line near est and un','handwritten')
inv('Long subscheme enclosure','drawing',[1024,764,1604,820],'curved return after paraboliques;','handwritten')
inv('ST and Levi-pair identification body','text',[267,848,1653,1014],'ST_c des homomorphismes ... couples de Lévi (P,L)')
inv('Arrow in i:G_m to G','text',[827,857,872,876],'rightward arrow','handwritten')
inv('Lévi explanatory parenthesis body','text',[267,983,1654,1229],"(En d'autres termes ... à i étant associé . Cent(i).)")
inv('Ou encore addition','insertion',[970,996,1190,1035],'ou encore underlined slashed oval','typed ou encore; handwritten glyph and underline')
inv('Ou encore enclosure','drawing',[952,1008,1221,1091],'curve to gap after P in pour P de classe','handwritten')
inv('Arrow in i:G_m to P','text',[753,1118,805,1140],'rightward arrow','handwritten')
inv('Isolated point before Cent','text',[911,1193,922,1206],'doubtful point','small dark mark; medium uncertain')
inv('Closing explanatory parenthesis','insertion',[1077,1165,1105,1234],')','handwritten')
inv('Two-morphisms lead-in body','text',[269,1178,1601,1279],'On a ... morphismesde schémas canoniquement isomorphes','typed')
inv('Cancelled un homo','deletion',[1227,1183,1370,1215],'un homo','typed x overstrikes')
inv('Raised deux','insertion',[1250,1163,1327,1190],'deux','typed')
inv('Two-map display','display',[615,1304,1252,1361],"ST_c arrow underlined slashed oval_c, (CL)_c' arrow Par_c'",'typed objects and punctuation; handwritten arrows and slashed oval')
inv('Interpretation of the two maps body','text',[269,1376,1589,1478],'le premier en termes ... le deuxième ...','typed')
inv('Cancelled d before en','deletion',[435,1444,463,1476],'d','typed x overstrike')
inv('Characteristic-zero assumption body','text',[268,1508,1645,1607],"Supposons maintenant que k soit de car. nulle (j'ignore ...)",'typed')
inv('Dynkin homomorphism and class body','text',[269,1632,1650,1745],'Dyn_c des homomorphismes f:Sl(2,k) arrow G ... classe de Dynkin','typed with handwritten arrow')
inv('Non-point hypothesis addition','insertion',[587,1673,933,1707],'et non réduit à un point,','handwritten')
inv('Non-point hypothesis enclosure','drawing',[599,1690,957,1757],'curved return to non vide,','handwritten')
inv('Not-equal-one addition','insertion',[1120,1672,1173,1696],'not equal 1','handwritten')
inv('Not-equal-one leader','drawing',[1134,1680,1191,1754],'curve descending before live period after Dynkin','handwritten')
inv('Homogeneous-space assertion body','text',[269,1706,1639,1812],'Alors Dyn_c est un ... sous G','typed')
inv('Underlined cancelled torseur','deletion',[266,1705,1640,1817],'tor-/seur','typed underline with handwritten cancellation')
inv('Replacement espace homogène','insertion',[245,1683,1637,1778],'espace at right; homogène at next line left','handwritten')
inv('Stabilizer and structure note','insertion',[267,1742,1643,1850],'de stabilisateur Z_o (il faudrait regarder ... dimension, semi-simplicité).','handwritten')
inv('Paired oblique separator/leader','drawing',[486,1767,515,1821],'two oblique strokes after G','handwritten')
inv('Cancelled torsor explanation','deletion',[268,1775,1644,1880],'(en fait, il est can. is. au torseur Isom(G_1,G) ...).','typed text with handwritten long cancellation')
inv('Unipotent-scheme body, unfinished sentence','text',[269,1838,1643,1949],'Soit Un_c le schéma des éléments unipotents ... par la correspondance','typed')
inv('De G addition','insertion',[440,1878,506,1915],'de G','handwritten')
inv('De G curved line','drawing',[462,1903,523,1945],'curve entering gap before dont','handwritten')
inv('Final celle de deletion','deletion',[1014,1906,1164,1947],'celle de','typed x overstrikes')
inv('Archive sheet number','margin note',[44,2059,107,2110],'17, recorded only in a comment','archival handwritten number')
r['inventory']=I
r['remaining_doubts']=[
 dict(place='Exactness addition',reading=r'\unsure{dernière}',alternatives=['dernière; terminal impressions incompletely separated'],confidence='medium'),
 dict(place='After rat/k);',reading='i + overlapping o/l + cancelled tentative n',alternatives=['o/l impression order undetermined','cancelled cell may be unreadable rather than n'],confidence='low'),
 dict(place='First G index and recurring round indices',reading=r'G_{\unsure{o|0}}',alternatives=['o','0'],confidence='medium'),
 dict(place='Deleted cocharacter arrow',reading=r'\unsure{\to}',alternatives=['rightward arrow with obscured tip','line/arrow contour partly hidden by cancellation'],confidence='medium'),
 dict(place='After stable par',reading=r"\unsure{\Gamma'|\Gamma}",alternatives=['Gamma with prime','Gamma with joined terminal'],confidence='medium'),
 dict(place='Right edge before first scheme glyph',reading=r'\unsure{schéma}',alternatives=['schéma, final letter partly cropped'],confidence='medium'),
 dict(place='Between associé and Cent(i)',reading=r'\unsure{.}',alternatives=['intentional point','incidental mark'],confidence='low'),
 dict(place='After display before foncteurs',reading=r'\unsure{da|de}',alternatives=['da','de','order of possible overlapping impressions undetermined'],confidence='low')]
r['notes']=[
 'Corrected typescript with an underlined heading about filtrations of the forgetful functor on finite-dimensional representations of G. No date or authorial page number appears. The lower-left 17 is archival and is represented only by a comment.',
 'The first paragraph describes tensor-compatible exact filtrations, a rational conjugacy class which need not have a rational representative, the quotient Hom(G_m,T_o)/W=M/W, and a Galois-stable Weyl-chamber element. These are source assertions read, not independently proved here.',
 'The filtration scheme is described as homogeneous with parabolic stabilizers and as an open rational orbit in Par(G). ST_c is identified with Levi pairs. Two isomorphic scheme morphisms and the prose explaining them are separately inventoried.',
 'The next paragraph assumes characteristic zero, defines the Dynkin-homomorphism scheme, adds nontriviality conditions, replaces torseur by espace homogène, and begins an unfinished sentence about the unipotent scheme Un_c.',
 'Explicit hesitation: "j\'ignore dans quelle mesure c\'est vraiment nécessaire" qualifies the characteristic-zero assumption. The added stabilizer question reads "il faudrait regarder la structure de ces Z_o; dimension, semi-simplicité".',
 'Several interlinear additions are typed, with handwritten curves and smaller handwritten fills. H explicitly describes all marked additions as handwritten; that statement is inaccurate for their typed portions.',
 'All cancellations are retained, including the heading ending, un, both homomorphisme passages, un homo, the small d, torseur with its underline, the long torsor explanation, and final celle de.',
 'Expected mathematical meaning did not decide the slashed-oval filtration glyph or the ambiguous article da/de. The overlapping letters after rat/k are represented without imposing a predecessor/successor chronology.',
 'The small point before Cent was rechecked because both witnesses omit it; its textual status remains doubtful. The baseline comma after non vide is distinct from the added phrase\'s final comma.',
 'An interruption/resume message arrived during this same page task. Context was retained. No whole-page, half-page or crop image was reloaded.'
]
r['notation']=[
 dict(place='Round indices',form='small lowered round rings',transcription=r'first \unsure{o|0}; later o',caution='Typed G, T, E and i indices and handwritten Z indices were not normalized from mathematical convention.'),
 dict(place='Three filtration-scheme glyphs',form='closed oval crossed by rising diagonal slash, with independent low rule',transcription=r'\underline{\varnothing}',caution='Graphic reading only; no claim that the author semantically intended the empty set rather than a filtration symbol.'),
 dict(place='Two products',form='typewriter oval containing serifed x',transcription=r'\mathbin{\text{\textcircled{x}}}',caution='Each occurrence was inspected in its own crop.'),
 dict(place='Weyl-space Z and R',form='ordinary typed capitals with separate lower rules',transcription=r'\underline{Z}, \underline{R}',caution='No separable double strike was established. Underlining is not bold.'),
 dict(place='Typed operator capitals',form='typewriter Hom, Auext, Gal, Homgr, ST, CL, Par, Cent, Dyn, Sl, Un, Isom',transcription='upright operators; Homgr, inserted Par and cancelled Isom underlined locally',caution='No definite double-struck capital was identified; mere heaviness was not taken as separable doubled contours.'),
 dict(place='Stable-par Gamma',form='top bar with joined right downward hook',transcription=r"\unsure{\Gamma'|\Gamma}",caution='A detached prime is not established.'),
 dict(place='Overprints after rat/k and before foncteurs',form='superposed or ambiguous typewriter contours',transcription='o/l overlay; da/de uncertainty',caution='No chronological order is inferred from grammar.')]
r['abbreviations']=[
 dict(form='NB',expansion='Editorial expansion: nota bene.'),
 dict(form='cond.',expansion='Editorial expansion: condition.'),
 dict(form='aut.',expansion='Editorial expansion: automatique.'),
 dict(form='car.',expansion='Editorial expansion: caractéristique.'),
 dict(form='rat/k',expansion='Editorial expansion: rationnel sur k.'),
 dict(form='i.e.',expansion='Editorial expansion: id est.'),
 dict(form='can. is.',expansion='Editorial expansion: canoniquement isomorphe.')]
r['math_checks']=[
 dict(type='reading_only',place='Hom quotient and maximal-torus/Weyl formulas',event='Read each object, index, product sign and equality against the ink.',proof_or_computation_performed=False,result='No identity or theorem verification is claimed.'),
 dict(type='reading_only',place='ST and Levi-pair morphisms',event='Followed the source comparison to locate the ou encore addition and the two displayed targets.',proof_or_computation_performed=False,result='Attachment was decided by the curved leader, not by a mathematical derivation.'),
 dict(type='reading_only',place='Dynkin/unipotent paragraph',event='Read the characteristic-zero caveat, non-point and not-equal-one additions, and stabilizer question.',proof_or_computation_performed=False,result='No group-theoretic proof or dimension computation was performed.')]
r['workflow_feedback']=dict(
 dimensions=dict(whole=[1670,2143],a=[1670,1151],b=[1670,1152],b_origin_in_whole=[0,991]),
 views='Whole once for layout; each half once line by line against both witnesses, including agreements. Each of 18 prepared unresolved-locus crops viewed once. No repeated whole, half, or crop view; no OCR, web, external edition, other page, reader or root decision used.',
 crop_method='out/scripts/crop.py, Pillow LANCZOS, autocontrast and sharpening. Manifest stored beside the crops.',
 saving='Complete reading.tex was saved before the report. No TeX compilation performed.',
 marked_in_H_definition='True means an explicit H note covers the locus; bare source-state add/struck markers are not expressions of doubt.',
 counting='Apparatus-only differences are distinguished in the evidence. Equivalent macro syntax and missing handwriting wrappers alone are excluded. Connected graphic marks are listed because linear insertion macros lose their shapes.',
 context_loss='None.')
(base/'report.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
print('Completed report:',len(r['differences']),'differences;',len(Q),'C questions;',len(I),'inventory elements;',len(r['remaining_doubts']),'remaining doubts;',r['crop_count'],'crops.')
for v in Q:
 if v['C'] not in C: print('Exact C quotation review:',v['place'],repr(v['C']))
