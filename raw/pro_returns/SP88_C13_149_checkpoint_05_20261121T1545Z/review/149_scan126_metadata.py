from pathlib import Path
import importlib.util
import json
import re

ROOT=Path('/workspace/scratch/0cab6a548abb')
PAGE='149_scan126'
PACKET=ROOT/'packets'/PAGE
REVIEW=ROOT/'edition/review'
C=' '.join((PACKET/'C.tex').read_text().split())
H=' '.join((PACKET/'H.tex').read_text().split())
F=' '.join((REVIEW/f'{PAGE}.tex').read_text().split())
s=importlib.util.spec_from_file_location('scan126_crops',REVIEW/f'{PAGE}_crops.py')
m=importlib.util.module_from_spec(s)
s.loader.exec_module(m)
BOXES=m.BOXES

def span(w,start,end):
    i=w.index(start)
    return w[i:w.index(end,i)+len(end)]

def exact(w,v):
    v=' '.join(v.split())
    assert v=='[absent]' or v in w,v
    return v

def crop(key):
    return f'crops/{PAGE}_{key}.png'

changes=[]
def change(identifier,place,c,h,final,evidence,key,confidence='high',vs_c=False,vs_h=True,
           kind='misread word',category='Words',h_marked=False,consequential=False,**extra):
    r=dict(id=identifier,place=place,C=exact(C,c),H=exact(H,h),final=final,evidence=evidence,
           crop=crop(key),bbox=list(BOXES[key]),confidence=confidence,vs_C=vs_c,vs_H=vs_h,
           kind=kind,error_category=category,H_marked=h_marked,consequential=consequential)
    r.update(extra)
    changes.append(r)

change('p02','main line 3, parenthetical consequence',
       r"l'est (donc $V_1\ne L_1$)",r"l'est (et $V_1 \neq L_1$)",
       r"l'est (donc $V_1\ne L_1$)",
       'After the opening parenthesis there is a tall looped d followed by the low o/n/c sequence. The word is donc, not et. The two indexed letters and the crossed two-bar inequality are complete.',
       'p02')

change('p14','main line 3, deleted arrow and raised abbreviation',
       r'$V_1$ \deleted{$\longrightarrow$} \inserted{corresp. à} une',
       r'$V_1$ \add{\uncertain{correspond à une}}',
       r'$V_1$ \deleted{$\longrightarrow$} \inserted{corresp. \unsure{d} à} une',
       'The arrow remains visible below the raised wording; a heavy horizontal stroke continues beyond its head, supporting the deleted-arrow layer. The raised text has corresp. with a p descender and a small following point, then a separate low-loop/tall-terminal group tentatively read d, then the final accented à. The d-like group is not silently absorbed into an expansion. A curved leader joins the raised text to the gap before the baseline une. une itself remains on the baseline, not in the insertion.',
       'p14',confidence='medium',vs_c=True,kind='omission',category='Omissions',h_marked=True,
       supporting_crops=[crop('p02')],C_change_detail='The separate uncertain d-like group is additional ink absent from C; arrow state and baseline une otherwise follow C.')

change('p03','main line 4, quoted place and variable',
       r"``place'' du corps de fonctions d'une variable",
       r"« place » du corps de fonctions d'une variété",
       r"``place'' du corps de fonctions d'une variable",
       'The quotation signs are paired high ticks. The final word contains the separate tall b and l strokes followed by a low e; it is variable, not variété. p13 repairs the clipped top of the final tall stroke in the initial contextual crop; the word was not reopened as a new lexical decision.',
       'p03',consequential=True,supporting_crops=[crop('p13')])

change('p04','main line 7, complete E-map and target upper index',
       r'$\mathcal E_L^{\overline L}\longrightarrow\mathcal E_{L_1}^{\overline{L_1}}$',
       r'$\mathcal{E}_L^{\overline{L}} \to \mathcal{E}_{L_1}^{\overline{L}_1}$',
       r'$\mathcal E_L^{\overline L}\unsure{\longrightarrow|\twoheadrightarrow}\mathcal E_{L_1}^{\overline{L_1}}$',
       'The target upper bar extends beyond the horizontal foot of L to approximately the right edge of the small 1, supporting a bar over the whole upper L_1. Both lower indices are separately visible. The connector has one shaft and an outer head with an additional inner V-like return; a retraced single head and a double head remain possible. Adding this arrowhead uncertainty does not change C’s first/base reading.',
       'p04',confidence='medium',kind='misread symbol or index',category='Symbols and indices',
       H_change_detail='Bar scope on the complete upper L_1; arrow multiplicity remains unresolved against both witnesses.')

change('p05','main lines 8–9 and the raised insertion',
       r"l'image de $N_V$ normalise $I_{V_1}$, donc (si on a une \inserted{germe de} section",
       r"l'image de $N_V$ \add{germe de} normalise $I_{V_1}$, donc (si $\ldots$ une section",
       r"l'image de $N_V$ normalise $I_{V_1}$, donc (si on a une \inserted{germe de} section",
       'The raised germe de lies above section. Its leader bends down to the gap between une and section, rather than attaching after the N_V on the preceding row. In the baseline parenthesis, the low on and the separate small a are visible before une. The literal une is retained despite the inserted masculine noun.',
       'p05',kind='insertion or placement',category='Insertions put in the wrong place',consequential=True)

change('p07','main line 12, exponent on the restriction group',
       r'$\mathcal E_K^0$',r'$\mathcal{E}_K^{\circ}$',
       r'$\mathcal E_K^{\unsure{0|\circ}}$',
       'The superscript is a small closed oval with a dark return at its left. Its size and shape admit both a handwritten zero and a circle. There is no definition on this leaf to distinguish them. This records an unresolved C/H disagreement; neither witness is counted as corrected, and C’s added uncertainty is not a base change.',
       'p07',confidence='low',vs_h=False,kind='other',category='Other',
       collation_status='unresolved witness difference; neither alternative excluded')

margin_c=span(C,r'\margin{il faut',r'général\ldots}')
margin_h=span(H,r'\marginal{\ill{} fait',r'\ill{}…}')
margin_f=span(F,r'\margin{il faut',r'général....}')
change('p08','upper left oblique marginal note, six baselines',margin_c,margin_h,margin_f,
       'The six lines read il faut vérifier / que le corps des / fractions de V_1 / est bien L_1 — / c’est un fait / général. The long f strokes and the c/t/i/o/n/s sequence make fractions readable; est bien and the two small 1 indices are also visible. Four separate aligned dark points follow général. The fourth lies just below, but detached from, the descender of fait. The small de on the third row is retouched without a recoverable prior word. C differs only in its three-point ellipsis; H leaves or substitutes several readable words.',
       'p08',vs_c=True,kind='readable ink left as \\ill{}',category='Readable ink left as illegible',
       h_marked=True,consequential=True,consequential_against=['H'],
       C_change_detail='Four written terminal points replace C’s three-point ellipsis; no changed lexical base reading.')

change('p09','main line 14, heading punctuation',
       r'\uline{Conjecture}',r'\textbf{Conjecture.}',r'\uline{Conjecture}',
       'A single underline runs beneath Conjecture. No period follows the word before Soient. Bold versus underline wrappers are not counted separately; the added stop in H is the actual difference.',
       'p09',kind='text not on the page',category='Text that is not on the page')

change('p10','main line 17, parenthetical equivalence',
       r'(ou germe de tel, ça revient au $=$\ldots)',
       r'(ou germe de tel, sa variante $\ldots = \ldots$)',
       r'(ou germe de tel, ça revient au $=$\ldots)',
       'After tel and its comma, the first short word has a cedilla-like lower return and the following a. The next word has the r/e/v/i/e/n/t sequence, including an i dot and a final rising t; au follows in two very low connected forms. The two horizontal strokes of = and three following points are distinct. There is no ellipsis before the equals sign.',
       'p10',consequential=True)

change('p11','main line 19, valuation-ring label insertion',
       r'anneau de valuation \inserted{$V$} de $L$',
       r'anneau de valuation $V$ de $L$',
       r'anneau de valuation \inserted{$V$} de $L$',
       'V is raised above the baseline, and the leader descends to the gap after valuation and before de L. p15 extends upward to include the complete V and its leader, whose top touched the original p11 boundary. H prints the same letter but does not preserve its inserted state.',
       'p15',kind='insertion or placement',category='Insertions put in the wrong place',supporting_crops=[crop('p11')])

change('p15','main line 20, raised sur K and both cancellations',
       r'algébrique \inserted{sur $K$} \deleted{\unsure{,}} et \deleted{\unsure{ce}} $V$ est uniquement',
       r'algébrique \add{sur $K$}, et $V$ est uniquement',
       r'algébrique \inserted{sur $K$} \deleted{\unsure{,}} et \deleted{\unsure{ce}} $V$ est uniquement',
       'The raised sur K has a curved leader to the position after algébrique. A compact dark cancellation occupies the following baseline position; the comma remains tentative because its return is obscured. After the surviving et there is a second, separately blackened small group tentatively read ce. Neither cancellation is supplied as a clean surviving word or comma. The last visible words are V est uniquement, without added punctuation or completion.',
       'p15',confidence='medium',kind='deletion state',category='Struck text',supporting_crops=[crop('p11')])

change('p12','bottom left foliation',r'\margin{125}','[absent]',r'\margin{125}',
       'The light foliation shows 1, a curved 2 with a low foot, and 5 with a top horizontal and lower rounded return. It reads 125.',
       'p12',kind='omission',category='Omissions')

decisions=[dict(id='M0141',cote='149',scan='126',decision='undecided',
                reading=r'\unsure{I_V|N_V}',
                evidence='The group letter has horizontal top and bottom bars and a heavy upright, making I the preferred live reading. Reinforced inner oblique/vertical strokes leave the form layered enough that N is not excluded. No separately recoverable earlier N is asserted. The V subscript is clear.',
                crop=crop('p10'),bbox=list(BOXES['p10']),confidence='medium')]

doubts=[
 dict(place='raised abbreviation above main line 3',reading=r'\inserted{corresp. \unsure{d} à}',
      alternatives='The isolated group after corresp. is d-like; a contraction related to correspond is possible, but no full word is expanded or supplied.',confidence='medium'),
 dict(place='main line 7, whole E-map connector',
      reading=r'$\mathcal E_L^{\overline L}\unsure{\longrightarrow|\twoheadrightarrow}\mathcal E_{L_1}^{\overline{L_1}}$',
      alternatives='Retraced single arrowhead or two arrowheads; one shaft is secure.',confidence='medium'),
 dict(place='main line 12, restriction-group exponent',reading=r'\mathcal E_K^{\unsure{0|\circ}}',
      alternatives='Small handwritten zero or circle; C has 0 and H has circle, neither locally excluded.',confidence='low'),
 dict(place='main line 18, group symbol; M0141',reading=r'\unsure{I_V|N_V}',
      alternatives='I preferred from the horizontal bars; N remains possible through the reinforced interior strokes. No prior character is recovered.',confidence='medium'),
 dict(place='main line 20, first cancellation after algébrique/sur K',reading=r'\deleted{\unsure{,}}',
      alternatives='Comma retained tentatively; blackening prevents secure recovery of its full original shape.',confidence='medium'),
 dict(place='main line 20, second cancellation after et',reading=r'\deleted{\unsure{ce}}',
      alternatives='ce retained tentatively; the two-letter interior remains partly obscured.',confidence='medium'),
]

inventory=[
 dict(sheet_kind='text',hand='his hand',element='e01',kind='text',position='main lines 1–13',first_words_or_objects='dont le corps résiduel; functoriality and normalizing/centralizing statements',transcribed='yes'),
 dict(sheet_kind='text',hand='his hand',element='e02',kind='deletion',position='main line 2 between sera and fini',first_words_or_objects='alg',transcribed='yes'),
 dict(sheet_kind='text',hand='his hand',element='e03',kind='deletion',position='main line 3 after the second V_1',first_words_or_objects='rightward arrow',transcribed='yes'),
 dict(sheet_kind='text',hand='his hand',element='e04',kind='insertion',position='above the deleted arrow, attached before une',first_words_or_objects='corresp. [uncertain d] à',transcribed='yes'),
 dict(sheet_kind='text',hand='his hand',element='e05',kind='margin note',position='upper left; six oblique baselines',first_words_or_objects='il faut vérifier que le corps des fractions',transcribed='yes'),
 dict(sheet_kind='text',hand='his hand',element='e06',kind='insertion',position='above main line 9, between une and section',first_words_or_objects='germe de',transcribed='yes'),
 dict(sheet_kind='text',hand='his hand',element='e07',kind='text',position='retouched words in main lines 10 and 12',first_words_or_objects='le; sa',transcribed='yes'),
 dict(sheet_kind='text',hand='his hand',element='e08',kind='text',position='main lines 14–15, underlined heading and hypotheses',first_words_or_objects='Conjecture Soient K,L des ext. de type fini',transcribed='yes'),
 dict(sheet_kind='text',hand='his hand',element='e09',kind='text',position='main lines 16–20, unfinished item a)',first_words_or_objects='Toute section de E_L sur E_K',transcribed='yes'),
 dict(sheet_kind='text',hand='his hand',element='e10',kind='text',position='main line 18, heavily reinforced group letter',first_words_or_objects='I_V or N_V',transcribed='yes'),
 dict(sheet_kind='text',hand='his hand',element='e11',kind='insertion',position='above main line 19 after valuation',first_words_or_objects='V',transcribed='yes'),
 dict(sheet_kind='text',hand='his hand',element='e12',kind='insertion',position='above main line 20 after algébrique',first_words_or_objects='sur K',transcribed='yes'),
 dict(sheet_kind='text',hand='his hand',element='e13',kind='deletion',position='main line 20 beneath/right of sur K',first_words_or_objects='uncertain comma',transcribed='yes'),
 dict(sheet_kind='text',hand='his hand',element='e14',kind='deletion',position='main line 20 after et',first_words_or_objects='uncertain ce',transcribed='yes'),
 dict(sheet_kind='text',hand='foliation hand, not assigned',element='e15',kind='margin note',position='bottom left edge',first_words_or_objects='125',transcribed='yes'),
]

audit_boxes=[]
def audit(number,kinds,box,reading,key,context='',**extra):
    a=dict(box=f'b{number:02d}',kind=kinds,bbox=list(box),reading=reading,
           crop=crop(key),crop_bbox=list(BOXES[key]),context_fragments=context)
    a.update(extra)
    audit_boxes.append(a)

audit(1,'deletion',(455,154,1060,272),r'sera \deleted{alg} fini sur $K$','p01',
      'Only a clipped descender from the preceding corps line enters the top context; no complete additional word is present there.')
audit(2,'C/H word difference; handwritten number',(325,266,1018,355),
      r"l'est (donc $V_1\ne L_1$)",'p02')
audit(3,'insertion; deletion; handwritten number; less-than-high C departure',BOXES['p14'],
      r'$V_1$ \deleted{$\longrightarrow$} \inserted{corresp. \unsure{d} à} une','p14')
audit(4,'C/H word difference; handwritten number',(275,333,1635,568),
      r"``place'' du corps de fonctions d'une variable $L_1$ sur $K$. Or, par des fonctorialités",'p03',
      'The full two contextual baselines are transcribed. p13 repairs the variable ascender clipped by the initial p03 top edge; the audit rectangle contains the complete tall strokes.',
      supporting_crops=[crop('p13')])
audit(5,'doubtful formula; handwritten number; C/H word difference',BOXES['p04'],
      r'$\mathcal E_L^{\overline L}\unsure{\longrightarrow|\twoheadrightarrow}\mathcal E_{L_1}^{\overline{L_1}}$','p04',
      'A tiny clipped stroke from the preceding prose remains at the upper left; the complete formula is inside the box.')
audit(6,'insertion; doubtful formula; handwritten number; C/H word difference',(280,560,1663,1035),
      r"essentiellement évidentes, on voit que l'hom $\mathcal E_L^{\overline L}\unsure{\longrightarrow|\twoheadrightarrow}\mathcal E_{L_1}^{\overline{L_1}}$ envoie $N_V$ dans $N_{V_1}$, $I_V$ dans $I_{V_1}$ --- donc l'image de $N_V$ normalise $I_{V_1}$, donc (si on a une \inserted{germe de} section",'p05',
      'This complete contextual rectangle includes the transfer sentence, the two indexed I occurrences, and the actual insertion attachment. The saved focused p05 covers the attachment; p04 covers the complete uncertain arrow formula. The full context was read on the native top half.',
      supporting_crops=[crop('p04')],evidence_views=['packets/149_scan126/top.png'])
audit(7,'handwritten number',(280,1020,1635,1300),
      r'de $N_V$ sur $\mathcal E_K$) le germe de section obtenu de $\mathcal E_{L_1}$ sur $\mathcal E_K$ normalise $I_{V_1}$','p06',
      'Both complete main baselines are included, so the retouched le and indexed objects can be read with their actual context. The short p06 crop isolates le germe de section; both native halves supply the full lines.',
      evidence_views=['packets/149_scan126/top.png','packets/149_scan126/bottom.png'])
audit(8,'doubtful formula; handwritten number; C/H word difference',BOXES['p07'],
      r'--- et sa restriction à $\mathcal E_K^{\unsure{0|\circ}}$ centralise $I_{V_1}$ ---','p07')
audit(9,'margin note; handwritten number; C/H word difference',BOXES['p08'],
      margin_f+'\n'+r'``p','p08',
      'The margin is complete. At the lower right the crop also contains the opening ticks and p of the neighboring main word place; this actual fragment is included after the margin in reading. A farther cropped vertical stroke is from the subsequent main L, not another marginal word.',
      rotation_degrees=-30)
audit(10,'C/H word difference',(252,1630,606,1762),r'\uline{Conjecture}','p09',
      'The upper tip of the following fini ascender reaches the lower context; it does not form an extra complete word inside the heading box.')
audit(11,'doubtful formula; handwritten number; C/H word difference',BOXES['p10'],
      r'a) Toute section de $\mathcal E_L$ sur $\mathcal E_K$ (ou germe de tel, ça revient au $=$\ldots) normalise un $\unsure{I_V|N_V}$ associé à un anneau','p10',
      'Upper-edge fragments are descenders from the preceding type fini line. The three intended baselines and the whole reinforced I/N symbol with its V subscript are present.')
audit(12,'insertion; deletion; doubtful formula; C/H word difference',(250,2035,1664,2346),
      r'normalise un $\unsure{I_V|N_V}$ associé à un anneau de valuation \inserted{$V$} de $L$ contenant $K$, à corps résiduel algébrique \inserted{sur $K$} \deleted{\unsure{,}} et \deleted{\unsure{ce}} $V$ est uniquement','p15',
      'The audit rectangle extends to the complete preceding normalise line, instead of starting through its group symbol. p10 supplies that whole line and p15 supplies both lower lines with the complete V and leader. Only descender fragments of the parenthesis above remain at the upper boundary.',
      supporting_crops=[crop('p10'),crop('p11')])
audit(13,'handwritten number',BOXES['p12'],r'\margin{125}','p12')

main_baselines=[
 'dont le corps résiduel (contenu dans celui de',
 'V) sera [deleted alg] fini sur K si celui de V',
 'l’est (donc V_1 ≠ L_1) — donc V_1 [deleted arrow] une',
 '“place” du corps de fonctions d’une variable',
 'L_1 sur K. Or, par des fonctorialités',
 'essentiellement évidentes, on voit que',
 'l’hom E_L^{bar L} → E_{L_1}^{bar L_1} envoie N_V dans N_{V_1},',
 'I_V dans I_{V_1} — donc l’image de N_V',
 'normalise I_{V_1}, donc (si on a une section',
 'de N_V sur E_K) le germe de section',
 'obtenu de E_{L_1} sur E_K normalise I_{V_1}',
 '— et sa restriction à E_K^{0/circle} centralise',
 'I_{V_1} —',
 'Conjecture Soient K,L des ext. de',
 'type fini de Q, K⊂L. Alors',
 'a) Toute section de E_L sur E_K',
 '(ou germe de tel, ça revient au =…)',
 'normalise un I_V/N_V associé à un anneau',
 'de valuation de L contenant K, à corps',
 'résiduel algébrique [deleted comma] et [deleted ce] V est uniquement',
]
margin_baselines=['il faut vérifier','que le corps des','fractions de V_1','est bien L_1 —',"c'est un fait",'général....']

data=dict(
 page=PAGE,scan=126,reader='reader_c',line_count=31,
 line_count_detail=dict(main=20,margin=6,insertion=4,standalone_numbers=1,diagram_rows=0,total=31,
      convention='All distinct written baselines, including raised insertions, the oblique margin, and standalone foliation. Cancellations on existing baselines and inline indices do not add baselines.',
      main_baselines=main_baselines,margin_baselines=margin_baselines,
      insertion_baselines=['corresp. [uncertain d] à','germe de','V','sur K'],
      standalone_number_baselines=['125'],
      counting_note='The heading Conjecture shares its row with Soient K,L; a) shares the Toute section row. The short I_{V_1} — row is counted separately.'),
 changes=changes,decisions=decisions,inventory=inventory,doubts=doubts,audit_boxes=audit_boxes,
 notes=[
  'This leaf starts and ends in continuation. The first paragraph discusses a residual-field condition, the valuation V_1 and its place of the one-variable function field L_1, then states functorial transfer properties for the N and I groups.',
  'The author says that the induced germ of section normalizes I_{V_1} and that its restriction to the group with an unresolved zero/circle exponent centralizes I_{V_1}. These statements are recorded, not independently proved here.',
  'The six-line margin explicitly asks to verify that the fraction field of V_1 is L_1 and calls this a general fact. The text says fractions, not résid., and its terminal punctuation has four visible points.',
  'The underlined Conjecture introduces finite-type extensions K,L of the written Q and begins item a), proposing normalization of an inertia/decomposition-letter group associated to a valuation ring with algebraic residue field over K. The page ends at V est uniquement; no uniqueness completion is supplied.',
  'The insertion before section is germe de and the baseline preceding it is literally une. No agreement correction is made. The insertion before une in the upper paragraph is the short corresp., a separate uncertain d-like group, and à; possible relation to a contraction of correspond is a note only, not an expansion in the text.',
  'The target overbar of the upper E-map spans the complete upper L_1. The additional return inside its arrowhead remains ambiguous between retracing and a second head. The reinforced conjecture letter remains I_V|N_V without an inferred deleted N.',
  'Retouched le, sa, and the small marginal de have readable current letters but no securely separable earlier letters. Their blackening is not converted into invented deleted text.',
  'Only M0141 is a supplied mark ID, and it remains undecided. The extra d, arrowhead, exponent, and two retained cancellation doubts are recorded locally without inventing mark IDs. Adding uncertainty to a first/base reading is not counted as a C change.',
  'All 15 saved crops were visually inspected. p13 and p15 are declared boundary repairs for clipped tall strokes, not reopened lexical decisions; p14 focuses the still-open insertion cluster and arrow-deletion state. No other page content, OCR, external research, or TeX compilation was used.',
  'Audit reading fields contain actual text and mathematical notation. Larger contextual rectangles are used where a smaller crop would cut a formula or preceding line; their crop_bbox and supporting views remain explicit. No independent second audit was performed by this reader.',
 ],
 checks=[],
 hand_observations=[
  dict(habit='A small raised group can be separated from a short form by a point and wide space.',places='corresp. [d-like group] à above main line 3.',holds='The p descender and point are followed by a distinct cluster before the final accented a-like group.',witness_errors='Both witnesses omit or absorb the separate d-like ink; H additionally expands the short form and raises une.'),
  dict(habit='Curved leaders identify attachment separately from the text above them.',places='corresp. … à, germe de, V, and sur K.',holds='Four raised additions attach respectively before une, before section, after valuation, and after algébrique.',witness_errors='H misattaches germe de after the earlier N_V and does not preserve raised V.'),
  dict(habit='Reinforcement can create internal oblique strokes without a recoverable old letter.',places='le in le germe; sa restriction; de in the margin; I/N conjecture glyph.',holds='The first three current words are readable; the group-letter identity remains uncertain.',witness_errors='No inferred earlier letters are added merely from the darkening.'),
  dict(habit='Two horizontal bars plus a heavy upright favor I, while N elsewhere has a flowing curved outline.',places='Conjecture symbol compared with N_V in the preceding normalization paragraph and the ordinary I forms.',holds='I is preferred at the heavy conjecture glyph, but reinforcement prevents a unique decision.',witness_errors='H gives an unqualified I; C’s I|N doubt is retained.'),
  dict(habit='A terminal point can sit close to a descender while remaining separate.',places='Four points after général beneath the fait descender.',holds='All four points have distinct ink components; the last is aligned with the first three.',witness_errors='C gives only the standard three-point ellipsis.'),
 ],
 notation=[
  dict(written=r'V_1\ne L_1',meaning_or_use='Literal inequality in the consequence parenthesis; both subscripts are 1.',places='main line 3'),
  dict(written=r'\mathcal E_L^{\overline L}\unsure{\longrightarrow|\twoheadrightarrow}\mathcal E_{L_1}^{\overline{L_1}}',meaning_or_use='Functorial map named in the prose; the target overbar covers upper L_1 and head multiplicity remains uncertain.',places='main line 7'),
  dict(written=r'N_V,N_{V_1},I_V,I_{V_1}',meaning_or_use='Group labels in the stated transfer and normalization assertions.',places='main lines 7–13'),
  dict(written=r'\mathcal E_K^{\unsure{0|\circ}}',meaning_or_use='Restriction group whose exponent is not defined on this leaf.',places='main line 12'),
  dict(written=r'\unsure{I_V|N_V}',meaning_or_use='Group proposed to be normalized in the conjecture; letter remains reinforced and uncertain.',places='main line 18'),
  dict(written='=',meaning_or_use='Written short form in ça revient au =, meaning même in the prose.',places='main line 17'),
 ],
 abbreviations=[
  dict(written='alg',expansion='algébrique; this occurrence is struck'),
  dict(written=r'corresp. \unsure{d}',expansion='Unresolved abbreviated/contraction form, possibly related to correspond; not expanded in the transcription'),
  dict(written='hom',expansion='homomorphisme'),
  dict(written='ext.',expansion='extensions'),
  dict(written='=',expansion='même in the prose expression revient au ='),
 ],
 inspection=dict(whole=True,halves=['top','bottom'],crops=[crop(k) for k in BOXES],
      deletions_insertions_checked=True,
      method='Visual comparison of the full page once, both native halves once, and all saved contextual crops; Pillow enlargement/contrast and one rotated margin crop. No OCR, external sources, or TeX compilation.',
      followup_crop_reasons={'p13':'upward contextual repair for the clipped variable ascender','p14':'still-open arrow deletion and abbreviation cluster','p15':'upward contextual repair for the complete inserted V and leader'}),
)

assert len(main_baselines)==20 and len(margin_baselines)==6
assert [d['id'] for d in decisions]==['M0141']
for rel in data['inspection']['crops']:
    assert (ROOT/'edition'/rel).is_file(),rel
tex=(REVIEW/f'{PAGE}.tex').read_text()
depth=0
for mat in re.finditer(r'(?<!\\)[{}]',tex):
    depth+=1 if mat.group()=='{' else -1
    assert depth>=0
assert depth==0
assert tex.count('$')%2==0
assert not re.search(r'\\(?:note|struck|ill|add|uncertain)\b',tex)
data['structural_validation']=dict(unescaped_braces_balanced=True,math_delimiters_even=True,
     supplied_mark_ids_exact=True,saved_crops_exist=True,no_tex_compilation=True,
     C_base_change_rows=[r['id'] for r in changes if r['vs_C']],
     H_change_rows=[r['id'] for r in changes if r['vs_H']],
     unresolved_collation_rows=[r['id'] for r in changes if not r['vs_C'] and not r['vs_H']])
(REVIEW/f'{PAGE}.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(page=PAGE,changes=len(changes),C_changes=sum(r['vs_C'] for r in changes),
       H_changes=sum(r['vs_H'] for r in changes),crops=len(BOXES),doubts=len(doubts),
       decisions=len(decisions),audit_boxes=len(audit_boxes),line_count=31)))
