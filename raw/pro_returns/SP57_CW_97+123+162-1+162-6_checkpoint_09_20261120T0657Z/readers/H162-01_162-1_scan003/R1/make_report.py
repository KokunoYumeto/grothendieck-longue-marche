import json
from pathlib import Path
BASE=Path('out/readers/H162-01_162-1_scan003/R1')
C=(Path('packets/H162-01_162-1_scan003/C.tex').read_text())
H=(Path('packets/H162-01_162-1_scan003/H.tex').read_text())
manifest=[json.loads(s) for s in (BASE/'crops/crop_manifest.jsonl').read_text().splitlines()]
crops={int(x['dest'][:2]):x for x in manifest}
diffs=[]; doubts=[]
def evidence_location(crop=None,bbox=None):
    return {'crop': 'readers/H162-01_162-1_scan003/R1/crops/'+crops[crop]['dest'] if crop else None,
            'bbox': crops[crop]['box'] if crop else bbox,
            'bbox_source':'H162-01_162-1_scan003.jpg (1683 x 2150; b begins at y=995)'}
def D(place,c,h,reading,evidence,kind='other',cc=False,hc=True,marked=False,confidence='high',crop=None,bbox=None):
    diffs.append(dict(id='R1-D%03d'%(len(diffs)+1),place=place,C=c,H=h,reading=reading,evidence=evidence,
                      confidence=confidence,kind=kind,marked_in_H=marked,c_changed=cc,h_changed=hc,
                      **evidence_location(crop,bbox)))
def Q(place,c,reading,evidence,crop,confidence='medium',h='',cc=False,hc=False,kind='other',marked=False):
    doubts.append(dict(place=place,C=c,decision=reading,evidence=evidence,confidence=confidence,**evidence_location(crop)))
    if cc or hc: D(place,c,h,reading,evidence,kind,cc,hc,marked,confidence,crop)
# Every one of the 48 local C unsure wrappers is reconsidered separately.
Q('Head: parenthesis after Deligne',r'\unsure{suite}','suite','The low s, joined u, short i, tall crossed t and final e are separately visible under the single cancelling line.',1,'high',r'\emph{(suite)}',True,False)
Q('Head: surname before thèse',r'\unsure{Libermann|Libermans}',r'\unsure{Libermann|Libermans}','Initial tall L-like form and following short i/b strokes survive; the heavy horizontal obscures the final humps, leaving nn/s unresolved. The visible sequence does not support Hironaka.',1,'low','Hironaka, thèse',False,True,'misread word')
Q('Giraud: Notes sur',r'\unsure{$B_G$|$B_g$}',r'$B_G$','A large two-bowl B precedes a lowered open rounded G with a right bar and descending right terminal; there is no second closed g bowl.',7,'high',r'\ill\ 67',True,True,'misread symbol or index',True)
Q('Klose: end of lettre sur',r'\unsure{Ulmers|Ulmer}',r'\unsure{Ulmers|Ulmer}','The tall U/l pair and lower m/e/r strokes survive; a final hooked dark trace may be s but merges with the lower strike.',8,'low','Hartshorne',False,True,'misread word')
Q('Upper right: Griffiths',r'\unsure{Griffiths}',r'\unsure{Griffiths}','Large initial loop and successive tall ff/th-like uprights remain, but both horizontal cancellations cover the bodies.',2,'low',r'\uncertain{Griffiths}')
Q('Upper right: périodes',r'\unsure{périodes}',r'\unsure{périodes}','A descender followed by a low oval and short uprights is visible; the cancellation obliterates several letter bodies, so the doubt is retained.',2,'low','périodes',False,True)
Q('Upper right: punctuation after périodes',r'\unsure{\ldots|.}',r'\unsure{\ldots|.}','Several faint detached short traces follow the word, but their dot-versus-rule identity is insecure. Retained locally rather than supplied as certain ellipsis.',2,'low','',False,True,'omission')
Q('Upper right: SGA initials',r'\unsure{SGA|SG}',r'\unsure{SGA|SG}','The damaged left group is crossed and stained; its last letter is not recoverable enough to remove the SGA/SG alternative.',2,'low','SGA',False,True)
Q('Quillen/Adams: conj.',r'\unsure{conj.}','conj.','An open c, rounded o, low n, j descender and a small terminal point remain below and beside the crossing.',3,'high',r'\uncertain{sém.}',True,True,'misread word',True)
Q('Artin: initial 2',r'\unsure{2|2)}','2','The initial curved top descends to the low foot of 2. The following crossing consists of oblique strokes, not a separate closing parenthesis.',4,'high','2',True,False)
Q('Artin: crossed mark after 2',r'\unsure{x|X}',r'\draw[line width=.75pt] (949,224)--(977,257) (976,225)--(952,259);','Two oblique cancellation strokes cross after the numeral. There is no separately established underlying textual x/X; their physical shape is drawn.',4,'medium','',True,True,'drawing or diagram')
Q('Artin: lettre',r'\unsure{lettre}','lettre','The l stem, low e, two t stems, r and final e are visible; no final s is visible before the colon.',4,'high','lettres',True,True,'misread word')
Q('Artin: lowered date',r'\unsure{10.3.66|10.5.66}',r'10.\unsure{I|1}.66','The middle glyph is one upright with short terminal thickening; it has neither the two bowls of 3 nor the upper/lower construction of 5. I versus 1 remains open. Two separators and final 66 survive.',4,'medium','10.I.66',True,True,'misread symbol or index')
Q('Quillen under Goodman: title',r'\unsure{Deviations|Derivations}','Deviations','After De there is one distinct v-shaped down/up join followed by i, a and t; no extra r precedes that v. No acute accent is visible over e.',5,'high',r'\emph{Derivations}',True,True,'misread word')
Q('Hartshorne: final word',r'\unsure{dimension|dimensions}','dimension','The final n has a single up/down terminal, followed directly by detached dots; no separate s body is visible.',6,'medium',r'\ill',True,True,'readable ink left as \ill{}',True)
Q('Hartshorne: final punctuation',r'\unsure{..|\ldots}','..','Two separate dark points stand at the far right after dimension, beyond the heavy cancellation.',6,'high',r'\ill',True,True,'readable ink left as \ill{}',True)
Q('Shih: fibrés punctuation',r'\unsure{fibrés|fibrés,}','fibrés','The final s is followed by a blank before vectoriels. No detached comma is visible beneath or beside the cancellation in that gap.',10,'high','fibrés',True,False)
Q('Hatched left label: initial',r'\unsure{N|M}',r'\unsure{N|M}','The first form has two tall strokes joined diagonally; multiple oblique cancellation strokes prevent deciding N versus M.',11,'low',r'\ill',False,True,'readable ink left as \ill{}',True)
Q('Hatched abbreviation beside label',r'\unsure{PTTM|PTT M}','PTTM','P has a closed upper bowl, both T forms have upper bars, and the final M has two tall strokes and a central valley. Gaps between letters are comparable, so no word gap is assigned before M.',11,'medium',r'\ill',True,True,'readable ink left as \ill{}',True)
Q('Bertin: photocopies',r'\unsure{photocopies}','photocopies','The first p descender, h and t uprights, two round o bodies, c, second p, dotted i and final es survive below the single line.',12,'high','photocopie',True,True,'misread word')
Q('Below Bertin: Mme',r'\unsure{Mme|Mne}','Mme','A large M is followed by the low double hump of m and a short terminal e; no single n sequence is supported.',13,'medium','Mme',True,False)
Q('Below Bertin: surname',r'\unsure{Mathieu|Mathies}','Hakim','After the large H-like initial are a low a, tall k with lateral arm, dotted i and final m. The strokes do not spell Mathieu or Mathies.',13,'high','Mme Hakim',True,False,'misread word')
Q('Séminaire Gabriel: abbreviation',r'\unsure{Exp|Ex.}','Exp','The final sign has a descender attached to its upper bowl: p, not an abbreviation point.',13,'high',r'exp.~7',True,True,'abbreviation expanded or spelling modernised')
Q('Séminaire Gabriel: last numeral',r'\unsure{7|\mathrm I}','7','The top horizontal turns into a descending stem with a small cross stroke; it is the numeral 7, despite the cancellation intersection.',13,'medium','7',True,False,'misread symbol or index')
Q('Ferrand: heavily cancelled photocopies',r'\unsure{photocopies}',r'\unsure{photocopies}','The p descenders and several round bodies survive the repeated oblique hatches, but some internal cells remain covered. Doubt retained.',14,'low',r'\ill',False,True,'readable ink left as \ill{}',True)
Q('Dieudonné: parafactoriel/par.factoriel',r'\unsure{parafactoriel|par.factoriel}','par.factoriel','After the low par group a distinct detached point precedes the tall f. The ink gives an abbreviated par. form, not another a.',15,'high',r'\ill',True,True,'readable ink left as \ill{}',True)
Q('Dieudonné: before dim 2',r'\unsure{en|de}','en','The group has a low entry loop and one n-shaped hump, with no tall d ascender.',15,'high','de dimension 2',True,True,'misread word')
Q('Picard entry: foncteur',r'\unsure{foncteur}',r'\unsure{foncteur}','The long f descender and portions of the following connected letters are visible, but the middle compressed joins do not justify removing the local doubt.',16,'medium',r'\ill',False,True,'readable ink left as \ill{}',True)
Q('Cancelled cohomologie entry: letter before -adique',r'\unsure{\ell|l}',r'\unsure{\ell|l}','A tall looped stroke meets the horizontal deletion. Its loop does not settle script ell versus ordinary handwritten l.',17,'low','',False,True,'omission')
Q('Hirzebruch: close after question mark',r'\unsure{?\,)|?}',r'?\,)', 'The question mark has its own low point. To its right is a short open-left curved stroke, then a second much taller closing parenthesis. Both closes are retained.',18,'high',r'?)',True,True,'misread symbol or index')
Q('Serre brace: first abbreviation',r'\unsure{équ.}','équ.','A short accented e precedes a q with clear descender, a low u and a terminal point.',19,'medium',r'\ill',True,True,'readable ink left as \ill{}',True)
Q('Serre brace: word before L',r'\unsure{fonction|fonctions}','fonction','The terminal n rises and returns immediately before the distinct baseline L; there is no separate final s stroke.',19,'medium','',True,True,'omission')
Q('Serre brace: début',r'\unsure{début|défaut}','début','The middle tall letter has a b-like upper stem and lower bowl, with no f descender; the following low u and final t remain visible.',19,'medium','début',True,False)
Q('Serre brace: final points',r'\unsure{....|\ldots}','....','Four separated small marks are visible to the right of monodromie; the first two are closer together than the next two.',19,'high',r'\ill',True,True,'readable ink left as \ill{}',True)
Q('Berthelot right note: complexes',r'\unsure{complexes}','complexes','The word contains c/o, a compressed m, a p descender, tall l and the terminal exes sequence. There is no separate sur or initial opér-.',20,'medium','sur opérateurs',True,True,'misread word')
Q('Notes Serre formula: baseline letters',r'\unsure{\mathrm{ch}|\mathrm{dh}}',r'\unsure{\mathrm{ch}|\mathrm{dh}}','A short rounded first contour and adjacent tall h-like stem survive the heavy double cancellation; ch is preferred but dh remains possible.',21,'low',r'\ill',False,True,'readable ink left as \ill{}',True)
Q('Notes Serre formula: raised group',r'\unsure{n-i|n-1|n-\nu}',r'\unsure{n-\nu|n-i|n-1}','The final raised trace descends and turns upward in a small cup-like shape. That gives nu the visual preference, while crossing ink still permits i or 1.',21,'low',r'\ill',True,True,'misread symbol or index',True)
Q('Calcul: group between K and inner parenthesis',r'\unsure{(\mathrm{P}^{n}|\mathrm{CP}^{n}}',r'\unsure{(\mathrm{P}^{n}|\mathrm{CP}^{n}}','An open curved sign precedes a P with separately raised n. The curved sign can be an opening parenthesis or C, as C already records.',22,'low',r'\ill',False,True,'readable ink left as \ill{}',True)
Q('Calcul: inner letter and detached short stroke',r'\unsure{\overline{\mathrm L}|\mathrm L^{-}|\overline{\mathrm C}}',r'\unsure{\mathrm L^{-}|\overline{\mathrm L}}','The letter has an upright stem and rightward foot, supporting L rather than C. The short detached horizontal lies mostly to the upper right; superscript minus is preferred, with overbar still possible.',22,'medium',r'\ill',True,True,'misread symbol or index',True)
Q('Kleiman: initial case of Photocopies',r'\unsure{photocopies|Photocopies}',r'\unsure{Photocopies|photocopies}','The first letter has a tall upright and high bowl. Capital P is preferred, but the following h and crossing ink prevent a firm case decision.',24,'medium','Manuscrits ?',True,True,'misread word')
Q('Chev.: grassmanniennes',r'\unsure{grassmanniennes|grassmaniennes}',r'\unsure{grassmanniennes|grassmaniennes}','The low middle letters are reduced to separated humps and short horizontal joins beneath crossing paths; the number of n/m strokes is not securely recoverable.',25,'low',r'groupes \ill',False,True,'misread word',True)
Q('Note below Chev.: surname',r'\unsure{Agison|Agišon}',r'\unsure{Agison|Agišon}','A, a loop-descended g and the following short letters are visible. A short upper trace near the middle may be cancellation rather than a diacritic, so both forms remain.',26,'low',r'\ill',False,True,'readable ink left as \ill{}',True)
Q('Note below Chev.: title word',r'\unsure{bidéterminants|holodéterminants}',r'\unsure{holodéterminants|bidéterminants}','The beginning has a tall open h-like stem followed by rounded and tall traces before déterminants. This favours holo-, but broad crossing strokes keep bi- possible.',26,'low',r'\ill',True,True,'misread word',True)
Q('Verdier: SGA final sign',r'\unsure{SGAA|SGA 4}',r'\unsure{SGAA|SGA 4}','The last sign has an A-like pointed top, two legs and a middle connection like the preceding A. A figure 4 remains possible under the strike.',27,'low','SGA 4',False,True)
Q('Below Verdier entry: Gabriel',r'\unsure{Gabriel}',r'\unsure{Gabriel}','Large initial G, a following small oval and tall b survive; the closing riel group is heavily crossed. Doubt retained.',27,'low','Gabriel',False,True)
Q('Last left name',r'\unsure{Terjanian|Terzanian}',r'\unsure{Terjanian|Terzanian}','The medial descending hook supports j first, but the dot is insecure and a loop-descending z cannot be excluded beneath the line.',28,'medium',r'\ill',False,True,'readable ink left as \ill{}',True)
Q('Last entry: Articles',r'\unsure{Articles|Article}',r'\unsure{Articles|Article}','After the identifiable Articl- sequence, the final low e/s-like terminal sits directly in the cancellation; singular/plural remains open.',28,'medium','Article',False,True)
Q('Last entry: subscript of C',r'\unsure{$C_i$|$C_1$}',r'$C_i$','A tiny detached upper point stands over a short low stem and terminal, giving subscript i rather than 1.',28,'medium',r'\ill',True,True,'misread symbol or index',True)
# C's explicit illegible remainder is separate from its unsure initial.
doubts.append(dict(place='Hatched left label: remainder after initial N/M',C=r'\illegible{1}',decision=r'\illegible{1}',evidence='Several low loops remain between diagonal hatches, but no whole word is defensible. The one-word estimate is retained.',confidence='low',**evidence_location(11)))
# Additional substantive differences, including agreed C/H loci that the ink corrects.
D('Head: deletion covers Deligne and its parenthesis',r'\deleted{\uline{Deligne} (\unsure{suite})\quad \unsure{Libermann|Libermans}, thèse}',r'\textbf{Deligne} \emph{(suite)}',r'\deleted{\uline{Deligne} (suite)}','The horizontal strike runs through the name, suite and the neighbouring thesis entry. H gives the name and parenthesis live. The underline below Deligne is separate from that strike.','deletion state (struck given live or live given struck)',crop=1)
D('Printed stationery block', 'INSTITUT\\\\\nDES HAUTES ÉTUDES SCIENTIFIQUES\\\\\n91 - BURES-SUR-YVETTE\\\\\n928-48-53','', 'INSTITUT / DES HAUTES ÉTUDES SCIENTIFIQUES / 91 - BURES-SUR-YVETTE / 928-48-53','All four printed lines are visible; the handwritten Giraud cancellation crosses the telephone line. H omits the stationery.','omission',bbox=[136,139,616,328])
D('Upper right: leading upright cancellation traces',r'\tikz[baseline=-.45ex]{\draw (0,0)--(.06,.52) (.09,.04)--(.15,.49);}','',r'\draw[line width=.7pt] (935,29)--(934,100) (946,33)--(942,88) (957,46)--(951,77);','Two long near-vertical strokes and a shorter third upright are visible before Griffiths. The third is separate from the large initial G.','drawing or diagram',True,True,crop=2)
D('SGA line: numeral and two rules',r'$\overline{\underline{\mathrm{XII}}}$','XIV',r'$\overline{\underline{\mathrm{XII}}}$','After the crossed X there are two separate upright I strokes. No converging V is present; detached upper and lower rules bracket the numeral.','misread symbol or index',crop=2)
D('Chern entry: full wording','Classes de Chern des représentations.','Chern et\nclasses de Chern des représentations','Classes de Chern des représentations.','The line starts Classes, followed directly by de Chern des représentations, and ends with a detached point. There is no leading Chern et.','text not on the page',crop=3)
D('Quillen/Adams: separator after Quillen','Quillen :',r'Quillen sur',r'Quillen \unsure{:|.} sur','One low point is visible after Quillen. An upper point could be hidden by the heavy strike, so colon versus single point remains open. H omits the separator.','other',True,True,confidence='low',crop=3)
D('Artin entry: recipient and preposition','lettre} : Artin',r'lettres à \ill\ sur Atiyah--Adams)',r'lettre : Artin (sur Atiyah-Adams)','The source has a two-point colon, then capital A, r, t, i, n and an opening parenthesis. It does not have à, and the recipient is readable.','readable ink left as \ill{}',False,True,True,crop=4)
D('Artin entry: detached low point','','',r'\fill (938,265) ellipse (4 and 1.7);','A small dark point lies separately below the initial numeral/cross. Its relation to the cancellation is uncertain; it is preserved without a character value.','omission',True,True,confidence='medium',crop=4)
D('Artin date: state and added du',r'\inserted{\deleted{\unsure{10.3.66|10.5.66}}}',r'\add{du} 10.I.66',r'\inserted{\deleted{10.\unsure{I|1}.66}}','The small lowered date is crossed by a heavy horizontal and a shallow upper hooked trace. There is no separate du before it. H gives the date live and supplies du.','deletion state (struck given live or live given struck)',False,True,crop=4)
D('Artin date: surrounding shallow curved trace','','',r'\draw[line width=.4pt] (1127,278) .. controls (1148,237) and (1212,260) .. (1252,247);','A light shallow arc rises from the lower left of the date and runs over its top. It is independent of the horizontal cancellation and is drawn in its relative position.','drawing or diagram',True,True,crop=4)
D('Goodman thesis: readable name and initial case',r'Thèse \uline{Goodman}',r'thèse \ill',r'Thèse \uline{Goodman}','Capital T is tall with a horizontal head; Goodman has a large open G, two rounded o forms, d, m, a and n. A separate low rule runs beneath the name.','readable ink left as \ill{}',False,True,True,crop=5)
D('Quillen Deviations entry: deletion, comma and end points',r'\deleted{Quillen \unsure{Deviations|Derivations} \ldots}',r'Quillen, \emph{Derivations} \ill',r'\deleted{Quillen Deviations \ldots}','A direct dark strike crosses Quillen and the title within a pale enclosure. Three terminal points are visible. No comma follows Quillen; H leaves this entry live.','deletion state (struck given live or live given struck)',False,True,True,crop=5)
D('Hartshorne: English title',r'Hartshorne \uline{On Cohomological \unsure{dimension|dimensions}}\unsure{..|\ldots}',r'Hartshorne \ill\
cohomologie \ill',r'Hartshorne On Cohomological dimension..','The opening On and the long word Cohomological are written in Latin letters, with the tall initial C and final -logical visible around the strike. H replaces this with a partial French reading and illegibility.','readable ink left as \ill{}',False,True,True,crop=6)
D('Upper right: connected enclosures and long left entry path',r'''\deleted{Quillen \unsure{Deviations|Derivations} \ldots}

\deleted{Hartshorne \uline{On Cohomological \unsure{dimension|dimensions}}\unsure{..|\ldots}}''','',r'Upper paths at (600,133), (888,249), (939,365), (1640,375), and lower boundary through (920,399) to (1660,414), plus closed pale Quillen enclosure','The half shows the long path starting above the stationery, descending left of the titles and continuing across the title block. Its lower branch is the long low rule beneath Hartshorne. A separate pale oval surrounds Quillen Deviations. C linearizes this as title underlining and omits the connecting geometry; H has no drawing.','drawing or diagram',True,True,confidence='high',bbox=[593,126,1662,427])
D('Giraud: extra 67 in H','','67',r'Notes sur $B_G$','The lowered G has a terminal stroke but there are no separate figures 6 and 7 after it. H has converted part of this formula into 67.','text not on the page',crop=7)
D('Klose: readable label',r'\uline{Klose}',r'\textbf{\struck{\ill}}',r'\deleted{\uline{Klose}}','The large K, looped l, rounded o and final se survive the strike and a separate lower underline. H leaves this label illegible.','readable ink left as \ill{}',False,True,True,crop=8)
D('Algèbre III: numeral rules',r'$\overline{\underline{\mathrm{III}}}$','III',r'$\overline{\underline{\mathrm{III}}}$','Three uprights have a separate common upper and lower bar; the cancellation passes through the line independently. H gives a bare numeral.','misread symbol or index',bbox=[769,447,818,482])
D('Shih: name at beginning of subject','Rapport à Bourbaki calcul différentiel','R. Wood à Bourbaki, calcul différentiel','R. Wood à Bourbaki calcul différentiel','There is a large R followed by a detached point, then a capital W with two lower vertices and the short o/o/d sequence. This is not the continuous word Rapport. No comma occurs after Bourbaki.','misread word',True,True,crop=9)
D('Schwarzenberger: underline under numeral',r'\uline{3} articles','3 articles',r'\uline{3} articles','A short light low stroke beneath the numeral is distinct from the long dark cancellation through the entry.','omission',False,True,crop=10)
D('Hatched name/abbreviation: cancellation pattern',r'\deleted{\uline{\unsure{N|M}\illegible{1}}}\qquad \deleted{\unsure{PTTM|PTT M}}','',r'Oblique hatch strokes are drawn over both groups at source coordinates (184,712)-(293,772) and (456,711)-(624,767)','Repeated oblique strokes cancel the label and abbreviation locally; they are not one straight horizontal strike. The saved text draws these traces across the letters and intervening gaps.','drawing or diagram',True,True,crop=11)
D('Atiyah row: underlines and punctuation',r'\uuline{Papiers Atiyah} \uline{topologie} et \uline{op. elliptiques}','Papiers Atiyah, topologie et opérateurs\nelliptiques',r'\uuline{Papiers Atiyah} \uline{topologie} et \uline{op. elliptiques}','Two parallel low strokes run under Papiers Atiyah, and separate single strokes under topologie and op. elliptiques. There is no comma after Atiyah.','omission',False,True,bbox=[650,682,1644,784])
D('Atiyah row: abbreviated op.',r'op. elliptiques','opérateurs\nelliptiques','op. elliptiques','The source contains o, p, a point and a gap before elliptiques. The full word opérateurs is an editorial expansion in H.','abbreviation expanded or spelling modernised',False,True,bbox=[1318,689,1639,750])
D('Bertin: EGA IV bars',r'$\overline{\underline{\mathrm{IV}}}$','EGA IV 16--19',r'EGA $\overline{\underline{\mathrm{IV}}}$ 16--19','The I and V have separate shared cap and base strokes, independent of the cancelling line.','misread symbol or index',False,True,crop=12)
D('Bertin: comma before photocopies','','16--19, photocopie','16--19 photocopies','A long blank follows 19 before photocopies; no detached comma is visible there. The deletion line passes continuously through the gap.','text not on the page',False,True,crop=12)
D('Mme Hakim: two schémas',r'Séminaire Gabriel deux schémas,',r'Séminaire Gabriel, deux séminaires,',r'Séminaire Gabriel deux schémas,','After deux the source has an initial sch sequence and the shorter ending -émas; it does not contain the extra syllables of séminaires. A comma occurs after schémas, not after Gabriel.','misread word',False,True,crop=13)
D('Bertin/Mme Hakim: shared scalloped deletion','','',r'Shared scalloped paths and the long line (153,985)--(1395,907) over Bertin and Mme Hakim rows','The long stroke joins the name area to a succession of broad downward scallops across the space between the Bertin and Hakim entries. A separate top-right return curves toward the final 7. Both named rows and their subject rows are covered.','drawing or diagram',True,True,bbox=[121,804,1404,1005])
D('Ferrand: EGA IV bars',r'$\overline{\underline{\mathrm{IV}}}$','EGA IV 20, 21',r'EGA $\overline{\underline{\mathrm{IV}}}$ 20,21','The numeral has its own top and bottom strokes. The horizontal cancellation through EGA and the title is separate.','misread symbol or index',False,True,crop=14)
D('Ferrand: épreuves',r'épreuves','',r'\deleted{épreuves}','The terminal word has accented e, p/r uprights and the low euves sequence; it is crossed along with the EGA line. H has no readable counterpart.','omission',False,True,crop=14)
D('Ferrand: nested cancellation over photocopies',r'\deleted{\unsure{photocopies}}',r'\struck{\ill}',r'\deleted{\unsure{photocopies}} plus repeated oblique strokes over that word','A separate dense run of short slanted strokes cancels photocopies within the already cancelled whole line. C records nested deletion but not the graphic hatch run; H only records one illegible cancelled item.','drawing or diagram',True,True,True,crop=14)
D('Dieudonné: colon and dim abbreviation','Lettre : Dieudonné','Lettre à\nDieudonné','Lettre : Dieudonné','Two detached points follow Lettre. H replaces the separator with the preposition à.','misread word',False,True,crop=15)
D('Dieudonné: dim 2','dim 2','dimension 2','dim 2','Only the three short letters dim precede 2, with no abbreviation point. H expands the word.','abbreviation expanded or spelling modernised',False,True,crop=15)
D('Notes sur R.R.: oval and question mark',r'\tikz[baseline=(rr.base)]{\node[inner sep=2pt] (rr) {\deleted{Notes sur R.R.}};\draw (rr.center) ellipse [x radius=3.1em,y radius=.74em];}\ ?',r"\add{entouré, suivi d'un point d'interrogation}",r'Closed pale oval around cancelled Notes sur R.R.; separate live ? to its right','The pale oval encloses the entire short line and closes on the right before the separate question mark. H describes the feature editorially instead of transcribing the drawing; C already preserves the relation.','drawing or diagram',False,True,crop=16)
D('Picard: source le',r'Notes sur le \unsure{foncteur}',r'Notes sur \ill\ dét.',r'Notes sur le \unsure{foncteur} dét.','The short looped le is visible before the large descending f. H gives no separate le in the directly transcribed phrase.','omission',False,True,True,crop=16)
D('Picard: underlined phrase and final point',r'\uline{sur cat. de Picard} .',r'sur cat.\ de Picard',r'\uline{sur cat. de Picard} .','A continuous low rule begins under sur and ends under Picard. A separate small point stands to its far right. H gives no rule or terminal source point.','omission',False,True,crop=16)
D('Raised Hartshorne/Goodman entry: placement',r'\uline{Jouanolou}\quad 1\qquad \inserted{Papiers Hartshorne (dim. coh.) et Goodman}',r'\add{et} Godement ; \struck{Papiers \uncertain{Hertzbrouck}}',r'Raised node (635,1287) with \inserted{Papiers Hartshorne (dim. coh.) et Goodman}, above cancelled Notes cohomologie and opposite Jouanolou','The added title occupies its own raised baseline above Notes cohomologie. Goodman continues that same added title; it is not a continuation of the Picard line. C marks insertion but its linear placement does not preserve this height; H attaches et Godement to Picard.','insertion or placement',True,True,True,crop=17)
D('Raised entry: Hartshorne and Goodman wording/state',r'\inserted{Papiers Hartshorne (dim. coh.) et Goodman}',r'\add{et} Godement ; \struck{Papiers \uncertain{Hertzbrouck}}',r'\inserted{Papiers Hartshorne (dim. coh.) et Goodman}','Papiers and Hartshorne are above the cancelling line, followed by the parenthesized dim. coh. and the clearly formed Goodman. The strike belongs to the lower Notes cohomologie line. H both misreads the two surnames and gives Papiers as cancelled.','deletion state (struck given live or live given struck)',False,True,True,crop=17)
D('Cancelled cohomologie entry',r'\deleted{Notes cohomologie $\unsure{\ell|l}$-adique}','',r'Notes cohomologie $\unsure{\ell|l}$-adique','Notes and the cohomologie sequence lie on the lower baseline, with a long direct cancellation through them and the letter-adique ending. H has no corresponding entry.','omission',False,True,crop=17)
D('Hirzebruch entry: singular Papier and capital Congrès',r'Papier Hirzebruch (Congrès',r"Papiers Hirzebruch (congrès d'Amsterdam ?)",r"Papier Hirzebruch (Congrès d'Amsterdam ?\,) )",'The opening word ends in an r terminal without a following s. Congrès begins with a large capital C. The two closing curves are treated separately in the C-doubt row.','misread word',False,True,crop=18)
D('Serre letter: no supplied sur',r'Lettre : Serre',r'Lettre : Serre \add{sur}',r'Lettre : Serre','The source goes from Serre directly to the left brace; there is no intervening sur.','text not on the page',False,True,crop=19)
D('Serre first subject: singular fonctionnelle and baseline L',r'fonctionnelle \unsure{fonction|fonctions} }L',r'fonctionnelles, suite',r'fonctionnelle fonction $L$','The first adjective ends in -elle without an s; another word fonction follows on the same upper row, ending before a large baseline L. H collapses the two rows and omits L.','misread word',False,True,crop=19)
D('Serre letter: brace and two subject baselines',r'\left\{\begin{array}{l}', '',r'Opening brace from (861,1408) through (849,1453) to (863,1510), with subjects at y=1439 and y=1480','The left brace groups two separately written subject lines. Its lower tail reaches down beside the following stratifications entry; it is not prose punctuation between the subjects. H omits the brace.','drawing or diagram',False,True,crop=19)
D('Berthelot and right note: continuous cancellation and vertical rule',r'\margin{\noindent\vrule height 1ex depth 4.8ex width .35pt\hspace{.2em}\parbox[t]{.86\linewidth}{\deleted{Lettre Deligne \unsure{complexes} elliptiques}}}',r'\struck{lettre'+'\n'+r'Deligne sur opérateurs elliptiques}',r'Right note at y=1492 and y=1515, rule (1236,1469)--(1246,1625), shared cancellation (202,1524)--(1641,1475)','The right note consists of a first line ending complexes and a second indented elliptiques, beside a long vertical rule. A single sloping stroke runs from the Berthelot/stratifications row across the first note line. C lacks the shared connecting stroke; H omits the geometry.','drawing or diagram',True,True,crop=20)
D('Berthelot: RR without points',r'Notes RR (copie de Serre)',r'Notes R.R.\ (copie de Serre)',r'Notes RR (copie de Serre)','There are no detached points after either R in this entry; the neighbouring Ferrand entry does have two points. This local punctuation distinction is maintained.','misread symbol or index',False,True,crop=21)
D('Rapport Serre: no comma',r'Rapport Serre représentations de groupes finis','Rapport Serre,\nreprésentations de groupes finis','Rapport Serre représentations de groupes finis','After Serre there is a gap followed by représentations. No detached comma descends into the gap; long cancellation strokes cross above/below it.','text not on the page',False,True,crop=23)
D('Kleiman: EGA IV bars',r'$\overline{\underline{\mathrm{IV}}}$','EGA IV 20',r'EGA $\overline{\underline{\mathrm{IV}}}$ 20','The I/V group has a distinct upper and lower rule beneath the long cancelling stroke.','misread symbol or index',False,True,crop=24)
D('Following EGA V: numeral bars',r'$\overline{\underline{\mathrm{V}}}$','EGA V',r'EGA $\overline{\underline{\mathrm{V}}}$','V has separate cap and base bars, with the cancellation passing through the surrounding line.','misread symbol or index',False,True,crop=24)
D('Chev.: abbreviated name and doubtful stop','Chev.','Chevalley',r'Chev\unsure{.}','The visible form has C, h, e, v; the terminal point is not secure because a thin oblique cancellation crosses that location. Chevalley supplies letters absent from the line.','abbreviation expanded or spelling modernised',True,True,confidence='medium',crop=25)
D('Note Agison: singular opening',r'Note \unsure{Agison|Agišon}',r'Notes \ill',r'Note \unsure{Agison|Agišon}','The short initial word ends with the e terminal before the gap and capital A; there is no separate final s.','misread word',False,True,True,crop=26)
D('Problèmes de Géométrie Algébrique: deletion state',r'\deleted{Problèmes de Géométrie Algébrique}',r'\emph{Problèmes de Géométrie Algébrique}',r'\deleted{Problèmes de Géométrie Algébrique}','A direct dark line crosses this whole title; broad vertical/diagonal cancellation strokes also pass through it. H presents the title live.','deletion state (struck given live or live given struck)',False,True,crop=26)
D('Verdier: full title remains cancelled',r'\deleted{\uline{Verdier}\qquad \unsure{SGAA|SGA 4} fasc. 1, mon exemplaire personnel}',r'SGA 4 fasc.~1, \ill\ ;',r'\deleted{\unsure{SGAA|SGA 4} fasc. 1, mon exemplaire personnel}','The long strike crosses both Verdier and the complete title through personnel, with additional lower block cancellation. H marks only the name struck and gives the title live.','deletion state (struck given live or live given struck)',False,True,True,crop=27)
D('Verdier: readable mon exemplaire personnel','mon exemplaire personnel',r'SGA 4 fasc.~1, \ill\ ;','mon exemplaire personnel','After the comma are the low m/o/n group, the longer exemplaire with tall p/l, and personnel with final tall l. Crossings obscure parts but the sequence is legible as in C.','readable ink left as \ill{}',False,True,True,crop=27)
D('Last entry: Greenberg','Greenberg',r'\uncertain{Grünberg}','Greenberg','After the initial G/r are two low e loops rather than a u with two upper dots; the remaining n/b/e/r/g strokes include the final descender.','misread word',False,True,True,crop=28)
D('Lower list: paths across multiple entries','','',r'Lower cancelling paths anchored from Berthelot through Gabriel, and from the lower title block down across Greenberg, as drawn at source coordinates','Several long oblique paths begin by Berthelot/RR/the right note and cross intervening rows. Broad repeated down/up cancellation strokes cover Kleiman through the last title; a far-right enclosing return reaches the foot. C and H record local deletion states but omit these cross-entry graphic paths.','drawing or diagram',True,True,bbox=[278,1510,1604,2086])
# Additional current-page C question rows concern positively read marks, not unsure wrappers.
for place,c,decision,evidence,bbox in [
 ('C questions: cap/base rules around XII',r'$\overline{\underline{\mathrm{XII}}}$',r'$\overline{\underline{\mathrm{XII}}}$','X and two I uprights each checked; separate cap and base strokes are retained.',[970,82,1223,127]),
 ('C questions: cap/base rules around III',r'$\overline{\underline{\mathrm{III}}}$',r'$\overline{\underline{\mathrm{III}}}$','Three uprights stand between separate common top and bottom strokes.',[765,445,824,486]),
 ('C questions: detached number beside Shih','1','1','A single short upright with a small sloping top stands to the right of Shih.',[318,531,344,563]),
 ('C questions: detached number beside Jouanolou','1','1','The short isolated pale upright remains to the upper right of Jouanolou.',[468,1285,496,1322]),
 ('C questions: Atiyah underlines',r'\uuline{Papiers Atiyah}',r'\uuline{Papiers Atiyah}','Two low parallel strokes appear under the first group; topologie and op. elliptiques each have one separate low rule.',[651,681,1644,784]),
 ('C questions: R.R. versus RR',r'Notes RR (copie de Serre)','Ferrand R.R.; Berthelot RR','The Ferrand line has distinct points after both R forms. The Berthelot line has neither point.',[531,1538,1148,1598]),
 ('C questions: brace before Serre subjects',r'\left\{\begin{array}{l}',r'Opening brace before two subject rows','The curved central pinch and upper/lower arms are visible; preserved with the observed row heights.',[842,1398,1453,1514]),
 ('C questions: PTT before Grenoble','PTT','PTT','Three separate capitals P, T and T stand before Grenoble; no extra M occurs in this uncancelled entry.',[664,645,758,686]),
 ('C questions: baseline L in Serre subject','}L',r'fonction $L$','L has a tall rising stem and short right foot at the end of the upper subject row; it is a baseline letter, not an index.',[1372,1364,1416,1412])
]: doubts.append(dict(place=place,C=c,decision=decision,evidence=evidence,confidence='high',**evidence_location(None,bbox)))

inventory=[]
def I(element,kind,bbox,first,hand='handwritten'):
 inventory.append(dict(sheet_kind='list',hand=hand,element=element,kind=kind,position={'bbox':bbox,'bbox_source':'whole image'},first_words_or_objects=first,transcribed='yes'))
# Body text and independent material, including text underlying every cancellation.
for element,kind,bbox,first,hand in [
 ('First head row','text',[165,22,930,96],'Deligne (suite); Libermann, thèse','handwritten'),
 ('Griffiths entry','text',[967,27,1430,100],'Griffiths périodes','handwritten'),
 ('SGA entry','text',[969,82,1221,129],'SGA 6 XII','handwritten'),
 ('Chern entry','text',[970,125,1643,169],'Classes de Chern des représentations.','handwritten'),
 ('First Quillen entry','text',[971,165,1546,205],'Quillen :/. sur conj. de Adams','handwritten'),
 ('Artin letter entry','text',[921,203,1651,259],'2 lettre : Artin (sur Atiyah-Adams)','handwritten'),
 ('Lowered cancelled date','insertion',[1127,244,1323,282],'10.I/1.66','handwritten'),
 ('Goodman thesis entry','text',[974,280,1376,325],'Thèse Goodman','handwritten'),
 ('Second Quillen entry','text',[986,319,1442,369],'Quillen Deviations ...','handwritten'),
 ('Hartshorne title','text',[996,373,1662,418],'Hartshorne On Cohomological dimension..','handwritten'),
 ('Printed stationery: four lines','text',[136,139,615,328],'INSTITUT / DES HAUTES ÉTUDES SCIENTIFIQUES / 91 - BURES-SUR-YVETTE / 928-48-53','printed'),
 ('Giraud name and subject across telephone','text',[165,287,811,351],'Giraud; Notes sur B_G','handwritten'),
 ('Klose name and subject','text',[167,375,891,441],'Klose; lettre sur Ulmers/Ulmer','handwritten'),
 ('Algèbre entry','text',[476,445,1058,493],'Notes Algèbre III Bourbaki','handwritten'),
 ('Shih and detached 1','text',[177,528,345,591],'Shih 1','handwritten'),
 ('Shih first subject','text',[476,526,1394,586],'R. Wood à Bourbaki calcul différentiel','handwritten'),
 ('Schwarzenberger entry','text',[483,597,1588,651],'3 articles Schwarzenberger sur fibrés vectoriels','handwritten'),
 ('Grenoble entry','text',[498,648,960,690],'Résumé PTT Grenoble','handwritten'),
 ('Hatched unreadable left label','text',[180,713,294,779],'N/M + unreadable word','handwritten'),
 ('Hatched abbreviation','text',[451,708,627,776],'PTTM','handwritten'),
 ('Atiyah entry with multiple underlines','text',[649,685,1644,786],'Papiers Atiyah topologie et op. elliptiques','handwritten'),
 ('Bertin and EGA subject','text',[187,807,1132,874],'Bertin; EGA IV 16--19 photocopies','handwritten'),
 ('Mme Hakim and seminar subject','text',[120,900,1404,1007],'Mme Hakim; Séminaire Gabriel deux schémas, Exp 7','handwritten'),
 ('Ferrand label and detached 1','text',[220,1078,435,1128],'Ferrand 1','handwritten'),
 ('Ferrand EGA entry','text',[528,1037,1371,1113],'EGA IV 20,21 photocopies épreuves','handwritten'),
 ('Dieudonné letter entry','text',[530,1112,1626,1194],'Lettre : Dieudonné sur par.factoriel en dim 2','handwritten'),
 ('Short R.R. entry and outside question','text',[530,1167,917,1260],'Notes sur R.R. ?','handwritten'),
 ('Picard entry','text',[538,1178,1632,1271],'Notes sur le foncteur dét. / sur cat. de Picard .','handwritten'),
 ('Jouanolou and detached 1','text',[224,1296,496,1361],'Jouanolou 1','handwritten'),
 ('Raised additional paper title','insertion',[628,1236,1594,1298],'Papiers Hartshorne (dim. coh.) et Goodman','handwritten'),
 ('Cancelled cohomologie entry','text',[564,1277,1189,1331],'Notes cohomologie ell/l-adique','handwritten'),
 ('Hirzebruch entry','text',[553,1328,1568,1410],"Papier Hirzebruch (Congrès d'Amsterdam ?) )",'handwritten'),
 ('Serre letter label','text',[546,1426,827,1483],'Lettre : Serre','handwritten'),
 ('Serre upper subject','text',[879,1375,1414,1445],'équ. fonctionnelle fonction L','handwritten'),
 ('Serre lower subject','text',[888,1434,1435,1493],'suite, début de monodromie ....','handwritten'),
 ('Berthelot and stratifications','text',[203,1485,1007,1555],'Berthelot; Notes sur stratifications','handwritten'),
 ('Right two-line Deligne note','margin note',[1248,1450,1652,1539],'Lettre Deligne complexes / elliptiques','handwritten'),
 ('Berthelot RR entry','text',[536,1541,1150,1605],'Notes RR (copie de Serre)','handwritten'),
 ('Notes Serre formula entry','text',[539,1591,1029,1645],'Notes Serre sur ch/dh raised n-nu/i/1 = 0','handwritten'),
 ('Calcul formula entry','text',[546,1630,896,1688],'Calcul K((P^n/CP^n)(L^- / barred L))','handwritten'),
 ('Serre representation report entry','text',[597,1649,1460,1723],'Rapport Serre représentations de groupes finis','handwritten'),
 ('Kleiman name','text',[219,1710,547,1774],'Kleiman','handwritten'),
 ('Kleiman photocopy entry','text',[551,1688,1160,1759],'Photocopies/photocopies EGA IV 20','handwritten'),
 ('EGA V entry','text',[841,1739,1039,1789],'EGA V','handwritten'),
 ('Chev. entry','text',[556,1791,1406,1848],'Notes Chev. sur grassmanniennes/grassmaniennes','handwritten'),
 ('Agison entry','text',[558,1828,1089,1884],'Note Agison/Agišon holodéterminants/bidéterminants','handwritten'),
 ('Problèmes title','text',[559,1850,1218,1905],'Problèmes de Géométrie Algébrique','handwritten'),
 ('Verdier name and SGA entry','text',[238,1882,1595,1970],'Verdier; SGAA/SGA 4 fasc. 1, mon exemplaire personnel','handwritten'),
 ('Gabriel name below SGA','text',[566,1946,787,1996],'Gabriel','handwritten'),
 ('Terjanian name and final title','text',[234,2004,1553,2081],'Terjanian/Terzanian; Articles/Article Greenberg sur C_i','handwritten'),
 ('Archive number: recorded as comment only','margin note',[49,2060,104,2118],'2','pencil-like handwritten')
]: I(element,kind,bbox,first,hand)
# Source states and graphic relationships are inventoried independently of the words.
for element,kind,bbox,first in [
 ('Single deletion across first head row','deletion',[167,54,932,76],'Deligne through thèse'),
 ('Griffiths vertical and horizontal strikes','deletion',[932,25,1363,101],'Three uprights; two long horizontal strikes'),
 ('SGA direct cancellation','deletion',[971,99,1224,125],'SGA 6 XII'),
 ('Chern direct cancellation','deletion',[972,126,1643,161],'Classes de Chern...'),
 ('First Quillen direct cancellation','deletion',[974,170,1544,201],'Quillen sur conj. de Adams'),
 ('Artin main cancellation','deletion',[920,204,1640,247],'2 lettre : Artin ...'),
 ('Artin oblique cross','drawing',[948,222,980,261],'Two oblique strokes after 2'),
 ('Detached point below Artin numeral','drawing',[932,259,947,270],'Small point; relation to the crossing uncertain'),
 ('Date stroke and shallow arc','deletion',[1125,243,1324,282],'10.I/1.66, independent overcurve'),
 ('Goodman cancellation and underline','deletion',[974,294,1378,326],'Thèse Goodman'),
 ('Quillen/Hartshorne title cancellation','deletion',[987,335,1662,419],'Both title baselines crossed'),
 ('Upper connected paths and separate Quillen enclosure','drawing',[593,126,1662,427],'Long left entry curve, two horizontal branches, pale Quillen oval'),
 ('Giraud cancellation crosses printed telephone','deletion',[163,299,813,340],'Two broad strokes across Giraud and Notes sur B_G'),
 ('Klose subject double cancellation','deletion',[455,396,891,438],'lettre sur Ulmers/Ulmer'),
 ('Klose name cancellation and underline','deletion',[161,402,307,439],'Klose'),
 ('Algèbre direct cancellation','deletion',[475,448,1058,490],'Notes Algèbre III Bourbaki'),
 ('Schwarzenberger direct cancellation','deletion',[483,607,1588,639],'3 articles ...'),
 ('Oblique hatching over label and PTTM','deletion',[180,708,628,780],'Separate oblique runs across two groups'),
 ('Bertin/Hakim shared broad scallops','deletion',[121,803,1405,1007],'Scallops and long lower stroke cover both rows'),
 ('Ferrand whole-line cancellation','deletion',[529,1037,1373,1103],'EGA IV 20,21 photocopies épreuves'),
 ('Ferrand nested hatches over photocopies','deletion',[897,1045,1146,1090],'Dense short oblique run'),
 ('R.R. oval and independent cancellation','drawing',[528,1167,884,1256],'Oval around Notes sur R.R.; separate right question'),
 ('Cohomologie direct cancellation below addition','deletion',[560,1296,1185,1321],'Notes cohomologie ell/l-adique'),
 ('Serre two-line brace','drawing',[844,1398,870,1515],'Opening brace with central pinch'),
 ('Berthelot/right note shared cancellation','deletion',[199,1472,1646,1536],'Sloping cross-entry stroke'),
 ('Right note vertical divider and lower strike','drawing',[1231,1463,1627,1629],'Vertical rule; elliptiques crossed separately'),
 ('RR, Serre-formula, Calcul and report direct strikes','deletion',[534,1569,1463,1718],'Four cancelled entries; Serre formula doubly crossed'),
 ('Kleiman name long curved cancellation','deletion',[217,1715,550,1766],'Curved low path through Kleiman'),
 ('Kleiman EGA IV and EGA V cancellation','deletion',[549,1703,1159,1785],'Separate crossed title rows'),
 ('Chev., Agison and Problèmes direct strikes','deletion',[555,1787,1410,1904],'Three separate title rows'),
 ('Verdier and title shared strike','deletion',[238,1886,1596,1955],'Name through personnel'),
 ('Gabriel separate local cancellation','deletion',[567,1952,789,1990],'Gabriel'),
 ('Terjanian and final title cancellation','deletion',[235,2030,1551,2069],'Name and Greenberg title'),
 ('Lower long oblique paths','drawing',[278,1510,1447,2047],'Paths descend from Berthelot, RR and right note through later entries'),
 ('Lower broad repeated cancellation and far-right return','drawing',[560,1653,1604,2087],'Down/up paths across lower list plus right enclosing return')
]: I(element,kind,bbox,first)

remaining=[]
for q in doubts:
    s=q['decision']
    if r'\unsure{' in s or r'\illegible{' in s:
        remaining.append(dict(place=q['place'],reading=s,alternatives=s,confidence=q['confidence']))
remaining += [
 dict(place='Quillen/Adams separator',reading=r'\unsure{:|.}',alternatives=['colon','single point; upper point covered by strike'],confidence='low'),
 dict(place='Chev. terminal stop',reading=r'Chev\unsure{.}',alternatives=['period','terminal/crossing trace rather than independent stop'],confidence='medium'),
 dict(place='Detached point below Artin numeral',reading='literal point at (938,265)',alternatives=['part of cancellation','independent ink trace; no character value assigned'],confidence='medium')]

notes=[
 'This sheet is a handwritten list of names and associated papers, letters, notes and copies on printed Institut des Hautes Études Scientifiques stationery. Numerous entries are individually cancelled, and larger pen/pencil-like paths cross groups of entries.',
 'The left labels and right subjects are physically aligned, but several raised entries and broad cancellation paths require spatial transcription. The Hartshorne/Goodman addition remains raised over the cancelled cohomologie title; the right Deligne note retains its two lines and divider.',
 'The source itself questions the circled "Notes sur R.R." with a separate question mark and puts another question mark in the Hirzebruch/Congrès d’Amsterdam entry. The latter is followed by a short and then a tall closing curve. These are uncertainties about listed documents, not mathematical proof steps.',
 'The small date under the Artin entry reads 10.I/1.66; the upright middle glyph is not established as 3 or 5. It is cancelled and enclosed partly by a shallow arc. No du is visible.',
 'The lower-left 2 is an archive mark and is recorded in a TeX comment, not promoted to an authorial page number. The detached 1 marks beside Shih, Ferrand and Jouanolou are separately retained.',
 'Agreement loci were read from the whole image and both halves, including the printed address/telephone, names, accents, cancellation scope, Roman bars, final dots and the two-line Serre subject. H punctuation that simply separates successive list entries was treated as its linearizing layout; internal added commas and expanded words are reported.',
 'No external identification or mathematical repair was used. The source formulas remain locally doubtful where the cancellation covers letters or exponent strokes.',
 "The source's shortened Chev. is retained with a local doubt on its stop; the large upper-title curve is drawn as a path rather than interpreted as an independent underline only.",
 'Only this page packet and the supplied briefs/preamble/notation table were read. The subsequently removed out-of-page C_questions snippets were disregarded; no other reader or page was consulted.'
]
notation=[
 dict(place='All Roman references on this sheet',visible='Ordinary handwritten Roman strokes between separate top and bottom rules',reading=r'\overline{\underline{\mathrm{XII}}}, III, IV, V with the rules repeated at each occurrence',caution='No double-struck or script alphabet is inferred from dark cancellation ink.'),
 dict(place='Giraud formula',visible='Large two-bowl B with lowered open G',reading=r'B_G',caution='The terminal of G is not separately read as 67.'),
 dict(place='Date under Artin',visible='Single upright middle glyph between separators',reading=r'10.\unsure{I|1}.66',caution='I versus 1 remains open; no curved 3/5 construction survives.'),
 dict(place='Notes Serre formula',visible='Covered short rounded c/d and tall h; raised n followed by small horizontal and curved terminal',reading=r'{\unsure{\mathrm{ch}|\mathrm{dh}}}^{\unsure{n-\nu|n-i|n-1}}=0',caution='The terminal cup-like trace gives nu the first visual preference; no mathematical interpretation settles it.'),
 dict(place='Calcul entry',visible='K, open curved sign, P with independent raised n, inner L-like stem/foot and detached upper-right dash',reading=r'K\unsure{(\mathrm{P}^{n}|\mathrm{CP}^{n}}(\unsure{\mathrm L^{-}|\overline{\mathrm L}}))',caution='Outer opening parenthesis/C and minus/overbar remain alternatives.'),
 dict(place='Cohomologie entry',visible='Tall looped letter preceding -adique under a horizontal strike',reading=r'\unsure{\ell|l}',caution='No normalization from mathematical vocabulary.'),
 dict(place='Serre letter',visible='Large baseline L after fonction',reading='L',caution='No superscript or index assigned.'),
 dict(place='Final Greenberg entry',visible='Large C with low stem and separate upper point',reading=r'C_i',caution='Detached point supports i rather than 1.'),
 dict(place='Atiyah entry',visible='Two underlines under Papiers Atiyah; single underlines under topologie and op. elliptiques',reading=r'\uuline{Papiers Atiyah} \uline{topologie} et \uline{op. elliptiques}',caution='The low rules are distinct from deletion strokes elsewhere.'),
 dict(place='Artin point and multiple cancellation paths',visible='Detached low point; separate cross and broad strokes across entries',reading='Literal TikZ points and paths',caution='No character or mathematical-arrow value is assigned to the isolated point or crossing paths.')
]
abbreviations=[
 dict(form='conj.',expansion='conjecture or conjectures (editorial; number not supplied by this page)'),
 dict(form='R.',expansion='Personal-name initial; full name unresolved (editorial note only)'),
 dict(form='Mme',expansion='Madame (editorial expansion)'),
 dict(form='Exp',expansion='Exposé (editorial expansion; no point supplied in the reading)'),
 dict(form='op.',expansion='opérateurs (editorial expansion)'),
 dict(form='par.factoriel',expansion='parafactoriel (editorial expansion of the shortened form)'),
 dict(form='dim',expansion='dimension (editorial expansion; the Dieudonné entry has no point)'),
 dict(form='dim. coh.',expansion='dimension cohomologique (editorial expansion)'),
 dict(form='dét.',expansion='déterminant (editorial expansion)'),
 dict(form='cat.',expansion='catégorie or catégories (editorial expansion; number unresolved)'),
 dict(form='équ.',expansion='équation or équations (editorial expansion; number unresolved)'),
 dict(form='R.R. / RR',expansion='Riemann–Roch (editorial expansion, not written out on the sheet)'),
 dict(form='Chev.',expansion='Chevalley (editorial expansion suggested by H; letters after Chev are not supplied in the reading)'),
 dict(form='fasc.',expansion='fascicule (editorial expansion)'),
 dict(form='PTT / PTTM',expansion='Unresolved from this page; no expansion supplied (editorial note)'),
 dict(form='SGA / EGA',expansion='Initialisms retained; no full title supplied by this page (editorial note)')
]
math_checks=[
 {'place':'Whole sheet','action':'Read the list and its mathematical glyphs; no theorem or proof is present and no mathematical proof/computation was performed.','result':'The page records documents and topics, with local source questions; nothing has been certified mathematically.'},
 {'place':'Notes Serre formula','action':'Checked baseline, exponent height, equals sign and final oval against the one local crop.','result':'The position of the exponent and =0 is visible; ch/dh and n-nu/i/1 remain ink doubts.'},
 {'place':'Calcul formula','action':'Checked the separate raised n and the inner letter/dash against the one local crop.','result':'n is separately raised over P; interpretation of the two curved openings and inner dash is not resolved by expected mathematical notation.'}
]
report=dict(page='H162-01_162-1_scan003',reader='R1',
 viewed={'whole':'source/SP57_CW_97+123+162-1+162-6_scans/H162-01_162-1_scan003.jpg','a':'source/SP57_CW_97+123+162-1+162-6_scans/H162-01_162-1_scan003_a.jpg','b':'source/SP57_CW_97+123+162-1+162-6_scans/H162-01_162-1_scan003_b.jpg','whole_dimensions':[1683,2150],'half_dimensions':[1683,1155],'b_y_offset':995,'views':'whole once; each half once; each of the 28 listed local crops once'},
 reading_file='out/readers/H162-01_162-1_scan003/R1/reading.tex',differences=diffs,c_doubts=doubts,inventory=inventory,
 remaining_doubts=remaining,notes=notes,notation=notation,abbreviations=abbreviations,math_checks=math_checks,crop_count=len(manifest),
 workflow_feedback=['The page is a dense cancelled list, so preserving associations required spatial rows rather than reflowing all names/subjects into prose.',
 'Twenty-eight crops cover the unresolved local clusters; adjacent doubtful glyphs in one source row share a single enlarged crop. No locus was recropped.',
 'The complete reading was saved before the longer report. No optional TeX compilation or additional image pass was performed.',
 'The packet repair was acknowledged; removed out-of-page snippets were not used as evidence.'])
for q in remaining:
    value=q['alternatives']
    if isinstance(value,str):
        loc=value.find(r'\unsure{')
        if loc>=0:
            start=loc+8; depth=1; end=start
            while depth:
                if value[end]=='{': depth+=1
                elif value[end]=='}': depth-=1
                end+=1
            q['alternatives']=value[start:end-1].split('|')
        else: q['alternatives']=[value]
(BASE/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'reading_file':report['reading_file'],'report_file':str(BASE/'report.json'),'differences':len(diffs),'c_doubts':len(doubts),'inventory_elements':len(inventory),'crop_count':len(manifest)},ensure_ascii=False))
