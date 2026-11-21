from pathlib import Path
import importlib.util
import json
import re

ROOT = Path('/workspace/scratch/0cab6a548abb')
PAGE = '149_scan120'
PACKET = ROOT / 'packets' / PAGE
REVIEW = ROOT / 'edition/review'
C = ' '.join((PACKET / 'C.tex').read_text().split())
H = ' '.join((PACKET / 'H.tex').read_text().split())
F = ' '.join((REVIEW / f'{PAGE}.tex').read_text().split())
spec = importlib.util.spec_from_file_location('scan120_crops', REVIEW / f'{PAGE}_crops.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
BOXES = module.BOXES

def exact(witness, value):
    value = ' '.join(value.split())
    if value != '[absent]':
        assert value in witness, value
    return value

def span(witness, start, end):
    i = witness.index(start)
    j = witness.index(end, i) + len(end)
    return witness[i:j]

def crop(key):
    return f'crops/{PAGE}_{key}.png'

changes = []
def change(identifier, place, c, h, final, evidence, key, confidence='high',
           vs_c=False, vs_h=True, kind='misread word', category='Words',
           h_marked=False, consequential=False, **extra):
    row = dict(id=identifier, place=place, C=exact(C,c), H=exact(H,h), final=final,
               evidence=evidence, crop=crop(key), bbox=list(BOXES[key]),
               confidence=confidence, vs_C=vs_c, vs_H=vs_h, kind=kind,
               error_category=category, H_marked=h_marked, consequential=consequential)
    row.update(extra)
    changes.append(row)

change('p01', 'main line 1, terminal punctuation',
       r"--- à tirer au clair à l'occasion !", r"--- à tirer au clair à l'occasion !]",
       r"--- à tirer au clair à l'occasion !",
       'The line ends with an upright exclamation stroke and its separate point. There is no closing square bracket to its right.',
       'p01', kind='text not on the page', category='Text that is not on the page')

change('p02', 'main lines 2–3, opening singular constructions',
       span(C,'Revenant',"d'où"), span(H,r'\uncertain{Revenons}',"d'où"),
       span(F,'Revenant',"d'où"),
       'Revenant ends in a tall crossed t. The following words are au modèle, with no plural s, and the next line starts un quotient. The two calligraphic E terms, their U and L subscripts, and the barred L superscripts are preserved.',
       'p02', h_marked=True)

change('p16', 'main line 5, whole cancellation including its far-right fragment',
       r'\deleted{Il est clair que}', r'\struck{Il est clair que} \ill{}',
       r'\deleted{Il est clair que \unsure{si}}',
       'One long strike crosses Il est clair que and continues across a small separate group to the right. That group has a short s-like rise and return and a detached dot compatible with an i; the bodies are partly absorbed by the strike. si is a local uncertain reading, not a restored clean word. H leaves the final unread material outside its strike.',
       'p16', confidence='medium', vs_c=True, kind='omission', category='Omissions',
       h_marked=True, supporting_crops=[crop('p04')])

change('p04', 'main line 6, short hom and the following unresolved mark',
       r"qui n'est autre que l'hom \unsure{---}",
       r"qui \uncertain{n'est autre} que l'homom. \ill{}",
       r"qui n'est autre que l'hom \unsure{---}",
       'qui n’est autre que is legible. After the apostrophe and h, the low o/m strokes stop at hom; there is no second om or stop there. The next long black mark has a left-end return and small underside returns, but no separable letter sequence. Its uncertainty is retained.',
       'p04', kind='abbreviation expanded or spelling modernised',
       category='Abbreviations expanded, spelling modernised', h_marked=True,
       supporting_crops=[crop('p17')])

change('p17', 'main line 6, first small E-map',
       r'$\mathcal E_{\widetilde U_x}\unsure{\mathrel{\text{---}}|\longrightarrow}\mathcal E_U$',
       r'$\mathcal{E}_{\tilde{U}_x} \to \mathcal{E}_U$',
       r'$\mathcal E_{\widetilde U_x}\longrightarrow\mathcal E_U$',
       'Between the complete E terms there is one short shaft with a small rightward terminal thickening and hook. The hook is comparable with the other single arrows on this page, and distinct from the longer unresolved mark to the left.',
       'p17', vs_c=True, vs_h=False, kind='misread symbol or index', category='Symbols and indices')

change('p05', 'main line 7, associated map and short hom',
       r'associé à $\widetilde U_x\longrightarrow U$. \uline{Si} cet hom',
       r'\uncertain{induit} \ill{} par $\tilde{U}_x \to U$. \emph{Si} cet homom.',
       r'associé à $\widetilde U_x\longrightarrow U$. \uline{Si} cet hom',
       'The word begins with a and the paired low s strokes, followed by the c/i/é sequence; the next word is à. The U-map has one rightward arrowhead and a following stop. Si has one separate underline. The final short form is hom, without the added om and stop in H.',
       'p05', h_marked=True)

change('p06a', 'main line 8, initial verb',
       r'factorise par $\widetilde S_x$, il est immédiat',
       r'\uncertain{se} factorise par $\tilde{S}_x$, il est immédiat',
       r'factorise par $\widetilde S_x$, il est immédiat',
       'The main line begins directly with factorise. No preceding se is written between the previous hom and this verb. The remaining words and the tilde over S are plain.',
       'p06', kind='text not on the page', category='Text that is not on the page', h_marked=True)

change('p06b', 'main line 9, short hom in the induced-map clause',
       r"que l'hom induit $I_{x'}\longrightarrow\mathcal E_U^{\overline L}$ est",
       r"que l'homom. \uncertain{induit} $I_{x'} \to \mathcal{E}^{\overline{L}}_{U}$ est",
       r"que l'hom induit $I_{x'}\longrightarrow\mathcal E_U^{\overline L}$ est",
       'The same short hom, with no added om or period, occurs before induit. induit itself and the single-arrow I-map are readable; clearing H’s uncertainty on induit is not counted as a separate lexical change.',
       'p06', kind='abbreviation expanded or spelling modernised',
       category='Abbreviations expanded, spelling modernised')

change('p07a', 'main line 10 and its raised insertion',
       r"nul, puisque \inserted{$I_{x'}$} \deleted{\unsure{c'}}est le noyau de",
       r'nul, puisque \struck{\ill{}} la composée de',
       r"nul, puisque \inserted{$I_{x'}$} \deleted{\unsure{c'}}est le noyau de",
       'A raised I with subscript x and a prime is positioned over the struck beginning before est. The underlying c′ remains locally uncertain under crossing ink. The surviving baseline says est le noyau de, including the n, descending y, and final au, not la composée de.',
       'p07', kind='misread word', category='Words', h_marked=True, consequential=True)

change('p07b', 'main line 11, kernel E-map',
       r'$\mathcal E_{\widetilde U_x}\unsure{\Longrightarrow|\longrightarrow}\mathcal E_{\widetilde S_x}$',
       r'$\mathcal{E}_{\tilde{U}_x} \to \mathcal{E}_{\tilde{S}_x}$',
       r'$\mathcal E_{\widetilde U_x}\Longrightarrow\mathcal E_{\widetilde S_x}$',
       'Two distinct, parallel shafts run toward one rightward arrowhead. Both shafts remain separate before meeting the head. This resolves C’s first reading without changing that base reading; H has only one shaft.',
       'p07', kind='misread symbol or index', category='Symbols and indices')

change('p07c', 'main line 11, following E-map to E_U',
       r'$\mathcal E_{\widetilde U_x}\unsure{\mathrel{\text{---}}|\longrightarrow}\mathcal E_U$',
       r'$\mathcal{E}_{\tilde{U}_x} \to \mathcal{E}_U$',
       r'$\mathcal E_{\widetilde U_x}\longrightarrow\mathcal E_U$',
       'The second map on this line has one shaft and a short dark right-end head; it is not the two-shaft sign immediately before it. This selects C’s arrow alternative.',
       'p07', vs_c=True, vs_h=False, kind='misread symbol or index', category='Symbols and indices')

change('p08a', 'main line 12, completion of se factorise par',
       r'cet hom.',
       r'$\mathcal{E}_{\tilde{U}_x} \to \mathcal{E}_{\tilde{S}_x}$, \ill{} homom.',
       r'cet hom.',
       'The following baseline starts cet hom. and then opens the bracketed question. There is no repeated E-map here. The final period belongs after this particular hom.',
       'p08', kind='text not on the page', category='Text that is not on the page',
       h_marked=True, consequential=True)

change('p08b', 'main lines 12–13, bracketed question',
       r'[ \uline{A t-on une réciproque ?} regarder ! ]',
       span(H,r'[\uncertain{Avoir}',r'\ill{} ! ]'),
       r'[ \uline{A t-on une réciproque ?} regarder ! ]',
       'The question reads A t-on une réciproque ?, with no accent on A and no hyphen between A and t. One wavy underline passes beneath the question. regarder is legible on the following physical row, before the exclamation and closing bracket. H’s quoted span interleaves the lower marginal note, separately collated below.',
       'p08', h_marked=True)

upper_margin = r'\margin{i.e. \uline{si} $V$ a un ``centre sur $U$\'\' i.e. domine un anneau local de $U$\ldots}'.replace("\\'", "'")
change('p18', 'upper left marginal note, four oblique lines',
       upper_margin,
       r'\marginal{i.e. si $V$ a un « centre » sur $U$ … \ill{} \ill{} \ill{} \uncertain{local} \ill{} $U$…}',
       upper_margin,
       'The note says i.e. si V a / un “centre sur U” / i.e. domine un anneau / local de U…. The si has one underline. Paired high quotation ticks begin before centre and close after U, so sur U lies within them. The widened p18 contains the ending of anneau; its terminal small e/a/u sequence and the next local de U are visible. The source uses ticks, not angular guillemets.',
       'p18', kind='readable ink left as \\ill{}', category='Readable ink left as illegible',
       h_marked=True, consequential=True, supporting_crops=[crop('p09')])

lower_c = span(C,r'\margin{Ça devrait',r"d'un $K$}")
lower_h = span(H,r'\marginal{Ça devrait',r'$K$}')
lower_f = span(F,r'\margin{Ça devrait',r"d'un $K$}")
change('p10', 'lower left marginal note, eight oblique lines',
       lower_c, lower_h, lower_f,
       'Ça devrait être le cas pour U “élémentaire” is readable. The next words have the accented à, the tall f and following acteurs, then pas de. types has a tall t and descending y/p strokes; both ordered pairs are fully visible, and ni has an n shoulder and detached i mark. One continuous underline runs from types across (0,0), ni, and (0,1)…. The curved/vertical marks below ni do not form a separate horizontal underbar. The reduced linked phrase remains unsure{lié à ceci}; in the last phrase only enfin remains unsure, while à l’existence d’un K is separable. The C departure counted here is underline extent/number only; resolving its first lexical readings and narrowing uncertainty are not counted as C base changes.',
       'p10', vs_c=True, kind='other', category='Other', h_marked=True,
       consequential=True, consequential_against=['H'],
       confidence='medium', supporting_crops=[crop('p19'),crop('p20')],
       C_change_detail='One continuous underline replaces three segments and the double underline assigned to ni; no changed lexical base reading.')

change('p11', 'main line 14, the model and open subset',
       r'modèle \uline{projectif} dont $U$ est un ouvert,',
       r'\struck{\ill{}} modèle \emph{propre} \uncertain{dont} $U$ soit un ouvert,',
       r'modèle \uline{projectif} dont $U$ est un ouvert,',
       'The underlined word contains the descending j and the final tall f of projectif, not propre. The next short verb is est. No cancelled word precedes modèle in the visible line; the nearby diagonal writing belongs to the marginal note.',
       'p11', consequential=True)

change('p12', 'main lines 15–16, valuative explanation',
       r'on peut dire (par définition valuative de la propreté) que $V$ a nécessairement',
       r'\struck{\ill{}} (par exemple \ill{} \ill{} \uncertain{en} \ill{} \ill{}) que $V$ \uncertain{domine} \ill{} \ill{}',
       r'on peut dire (par définition valuative de la propreté) que $V$ a nécessairement',
       'The first line begins on peut dire, with no cancellation. After the opening parenthesis the tall f and t strokes belong to définition, followed by valuative de. The next row has la propreté), then que V a nécessairement. The latter word is a continuous low letter sequence with its i dot and final crossed t. The high strokes at the top right are also visible in the overlapping p11.',
       'p12', h_marked=True, consequential=True, supporting_crops=[crop('p11')])

change('p13', 'main lines 17–18, centre and NB replacement',
       r"un centre sur $X$, soit $a$, \deleted{et le centre} \inserted{(\uline{NB} $a$ pas} néc. de codim.1\ldots) et la condition",
       r'sur $X$, soit $a$, \struck{et la \ill{}} \add{(\textbf{NB} $a$ \ill{})} \ill{} de codim.\ 1…) et la condition',
       r"un centre sur $X$, soit $a$, \deleted{et le centre} \inserted{(\uline{NB} $a$ pas} néc. de codim.1\ldots) et la condition",
       'un centre sur X, soit a is legible. The strike crosses et le centre. Directly above it, an opening parenthesis, underlined NB, a, and pas form the replacement; there is no closing parenthesis after pas. The continuation is the abbreviated néc. de codim.1…, with its closing parenthesis on the baseline below. The numeral 1 is retained literally.',
       'p13', kind='insertion or placement', category='Insertions put in the wrong place',
       h_marked=True, consequential=True)

change('p14', 'main lines 19–20, condition and full final map',
       r"envisagée tantôt (assurant que $I_{x'}\unsure{\mathrel{\text{---}}|\longrightarrow}\mathcal E_U^{\overline L}$ est nul) est que $a\in U$.",
       r'\uncertain{nécessaire} \ill{} (\uncertain{c\'est-à-dire} que $\mathcal{E}^{\overline{L}}_{U}$ \uncertain{soit} \uncertain{nul}) est \uncertain{simplement} que $a \in U$.'.replace("\\'", "'"),
       r"envisagée tantôt (assurant que $I_{x'}\longrightarrow\mathcal E_U^{\overline L}$ est nul) est que $a\in U$.",
       'The words are envisagée tantôt (assurant que. An I with subscript x′ and a one-shaft rightward connector closes the physical row; the connector has a dark hooked right endpoint. The target E_U with barred-L superscript starts the next row, completing one map across the line break. The following words are est nul) est que a∈U., with no simplement. No grammatical repair is made to est que.',
       'p14', vs_c=True, h_marked=True, consequential=True)

change('p15', 'bottom left foliation',
       r'\margin{119}', '[absent]', r'\margin{119}',
       'The lighter foliation consists of two upright 1 forms followed by a looped 9. It is actual page ink, separately from the scan identifier.',
       'p15', kind='omission', category='Omissions')

decisions = []
def decision(identifier, outcome, reading, evidence, key, confidence='high'):
    decisions.append(dict(id=identifier,cote='149',scan='120',decision=outcome,
                          reading=reading,evidence=evidence,crop=crop(key),
                          bbox=list(BOXES[key]),confidence=confidence))

decision('M0116','undecided',r'\unsure{---}',
         'Long horizontal blackening after hom has a short left-end rise and lower returns. These do not yield a secure word or arrow direction; a dash-like mark and cancellation residue remain possible.','p17','low')
decision('M0117','alternative',r'\longrightarrow',
         'One shaft between the complete E terms ends in a small rightward hook/thickening. The source and target labels are both present.','p17')
decision('M0118','first',r'\Longrightarrow',
         'Two separate parallel shafts meet the rightward head; the lower shaft is not an underline or a descender.','p07')
decision('M0119','alternative',r'\longrightarrow',
         'The second E-map on the kernel row has one shaft and a small dark right-end head.','p07')
decision('M0120','first','à',
         'The isolated short word has an a body and a detached accent; it does not have the e/t sequence of et.','p19')
decision('M0121','first','pas',
         'After facteurs there is a descending p, a low a body, and a compact returning final s before the separate de.','p19')
decision('M0122','first',r'types $(0,0)$',
         'The letter group contains the tall/crossed t, y/p descenders, and reduced e/s ending. Both rounded zeros, the comma, and parentheses are distinct.','p19')
decision('M0123','first','ni',
         'The short group between the ordered pairs has an n shoulder followed by an i stroke with its detached mark. The lower curved mark is not a second underline.','p19')
decision('M0124','undecided',r'\unsure{lié à ceci}',
         'The sloping line beneath the long underline has reduced linked strokes compatible with the tentative phrase, but its internal divisions and last word are not secure. No new alternative is forced from sense.','p20','low')
decision('M0125','undecided',r"\unsure{enfin} à l'existence",
         'The initial word has a long low approach and a tall f-like stroke but reduced internal letters. The following à, apostrophe after l, x/i/s/t sequence and remaining existence strokes are separable, so the uncertainty is narrowed to enfin.','p20','medium')
decision('M0126','alternative',r'\longrightarrow',
         'The shaft after I_x′ has a dark, hooked right endpoint; its target continues on the next physical row. Both complete map labels are present in p14.','p14')

inventory = [
 dict(sheet_kind='text',hand='his hand',element='e01',kind='text',position='top isolated line',first_words_or_objects="--- à tirer au clair à l'occasion !",transcribed='yes'),
 dict(sheet_kind='text',hand='his hand',element='e02',kind='text',position='main upper paragraph, lines 2–4',first_words_or_objects='Revenant au modèle U, fournissant',transcribed='yes'),
 dict(sheet_kind='text',hand='his hand',element='e03',kind='deletion',position='separate struck main line 5',first_words_or_objects='Il est clair que; uncertain si at far right',transcribed='yes'),
 dict(sheet_kind='text',hand='his hand',element='e04',kind='text',position='main lines 6–12',first_words_or_objects="qui n'est autre que l'hom; unresolved long mark; maps and kernel statement",transcribed='yes'),
 dict(sheet_kind='text',hand='his hand',element='e05',kind='insertion',position='above the beginning of est in main line 10',first_words_or_objects='I_x′',transcribed='yes'),
 dict(sheet_kind='text',hand='his hand',element='e06',kind='deletion',position='main line 10, immediately before est',first_words_or_objects='uncertain c′',transcribed='yes'),
 dict(sheet_kind='text',hand='his hand',element='e07',kind='margin note',position='upper left, four steeply oblique lines beside factorization paragraph',first_words_or_objects='i.e. si V a un “centre sur U”',transcribed='yes'),
 dict(sheet_kind='text',hand='his hand',element='e08',kind='text',position='bracketed question on main lines 12–13',first_words_or_objects='A t-on une réciproque ? regarder !',transcribed='yes'),
 dict(sheet_kind='text',hand='his hand',element='e09',kind='margin note',position='lower left, eight oblique lines',first_words_or_objects='Ça devrait être le cas pour U “élémentaire”',transcribed='yes'),
 dict(sheet_kind='text',hand='his hand',element='e10',kind='text',position='main lower paragraph, lines 13–20',first_words_or_objects="Quand on dispose d'un modèle projectif",transcribed='yes'),
 dict(sheet_kind='text',hand='his hand',element='e11',kind='deletion',position='main line 17 after soit a',first_words_or_objects='et le centre',transcribed='yes'),
 dict(sheet_kind='text',hand='his hand',element='e12',kind='insertion',position='above deletion after soit a',first_words_or_objects='(NB a pas',transcribed='yes'),
 dict(sheet_kind='text',hand='foliation hand, not assigned',element='e13',kind='margin note',position='bottom left edge',first_words_or_objects='119',transcribed='yes'),
]

doubts = [
 dict(place='main line 5, cancelled fragment after que',reading=r'\deleted{\unsure{si}}',alternatives='si is compatible with the s-like rise and detached dot; the crossed bodies do not exclude another short fragment.',confidence='medium'),
 dict(place='main line 6, after hom; M0116',reading=r'\unsure{---}',alternatives='Dash-like mark or cancellation residue; no secure underlying letters or arrow direction.',confidence='low'),
 dict(place='main line 10, deleted initial before est',reading=r"\deleted{\unsure{c'}}",alternatives='c′ is the retained tentative reading; crossing ink obscures the short initial.',confidence='medium'),
 dict(place='lower margin, sixth line; M0124',reading=r'\unsure{lié à ceci}',alternatives='The reduced sequence remains undecided; no secure competing phrase is proposed.',confidence='low'),
 dict(place='lower margin, seventh line; M0125',reading=r"\unsure{enfin} à l'existence",alternatives='The first word remains tentative; the following à l’existence is readable.',confidence='medium'),
]

audit_boxes = []
def audit(number, kinds, bbox, reading, key, context='', **extra):
    entry=dict(box=f'b{number:02d}',kind=kinds,bbox=list(bbox),reading=reading,
               crop=crop(key),crop_bbox=list(BOXES[key]),context_fragments=context)
    entry.update(extra)
    audit_boxes.append(entry)

audit(1,'C/H word difference',BOXES['p01'],r"--- à tirer au clair à l'occasion !",'p01')
audit(2,'C/H word difference',BOXES['p02'],span(F,'Revenant',"d'où"),'p02',
      'At the lower edge are clipped upper strokes of the following map row; its complete two maps were inspected in p03 and are transcribed in the page.')
audit(3,'deletion; doubtful formula; C/H word difference; less-than-high C departure',
      (300,592,1632,805),
      r"\deleted{Il est clair que \unsure{si}} qui n'est autre que l'hom \unsure{---} $\mathcal E_{\widetilde U_x}\longrightarrow\mathcal E_U$",'p04',
      'Some upper strokes of the following associé line meet the lower edge. The audit rectangle extends below the initial crop to include the descenders on the qui/que line. The cancellation and long mark were separately inspected in p16 and p17.',
      supporting_crops=[crop('p16'),crop('p17')])
audit(4,'C/H word difference',BOXES['p05'],
      r'associé à $\widetilde U_x\longrightarrow U$. \uline{Si} cet hom','p05',
      'A descender from que in the preceding line crosses the upper context; it is not an extra mark on the U-map.')
audit(5,'C/H word difference; insertion',(281,838,1650,1140),
      r"factorise par $\widetilde S_x$, il est immédiat que l'hom induit $I_{x'}\longrightarrow\mathcal E_U^{\overline L}$ est \inserted{$I_{x'}$}",'p06',
      'The raised I_x′ belongs to the following nul, puisque sentence, read fully in b06. The left edge also approaches the oblique margin. The audit rectangle is slightly wider vertically than the initial crop so the complete tall strokes and raised insertion are available.')
audit(6,'insertion; deletion; doubtful formula; C/H word difference',
      (270,1020,1620,1338),
      r"nul, puisque \inserted{$I_{x'}$} \deleted{\unsure{c'}}est le noyau de $\mathcal E_{\widetilde U_x}\Longrightarrow\mathcal E_{\widetilde S_x}$, et $\mathcal E_{\widetilde U_x}\longrightarrow\mathcal E_U$ se factorise par",'p07',
      'Clipped descenders from the preceding que line and upper strokes of the following cet hom/question line are contextual overlaps. Both displayed-in-line maps and the raised I/c′ correction are the intended complete targets.')
audit(7,'C/H word difference',BOXES['p08'],
      r"cet hom. [ \uline{A t-on une réciproque ?} regarder ! ] Quand on dispose d'un",'p08',
      'The end of the preceding factorization line and parts of the oblique lower margin meet the outer edges. The question and the opening of the new paragraph share the sloping lower physical row. The underline of the question is visibly wavy.')
audit(8,'margin note; C/H word difference',BOXES['p18'],
      upper_margin + r" que nul, $\mathcal E_{\widetilde U_x}\Longrightarrow$",'p18',
      'The quoted margin note is complete. The additional que, nul, and beginning of the main E-map are neighboring main-text context visible at the right/lower side after rotation; the formula target lies beyond this margin box and is complete in b06. Clipped portions of other neighboring main-line letters are not additional marginal words.',
      rotation_degrees=-39)
audit(9,'margin note; doubtful formula; handwritten number; C/H word difference; less-than-high C departure',
      BOXES['p10'],lower_f,'p10',
      'This box contains the whole lower marginal note, including both full ordered pairs. Its right/lower boundary also intersects fragments of neighboring main text (cet hom, regarder, modèle, and on peut dire); those are main-text context, not continuations of the marginal note. p19 and p20 isolate the still-open middle and final lines.',
      supporting_crops=[crop('p19'),crop('p20')],rotation_degrees=-32)
audit(10,'C/H word difference',(266,1480,1639,1690),
      r'modèle \uline{projectif} dont $U$ est un ouvert,','p11',
      'The extended audit bounds include the entire tall projectif strokes. The upper left intersects the oblique note and the lower/right edge meets upper strokes of the following valuative line; those neighboring lines are fully read in b09 and b11.')
audit(11,'C/H word difference',(251,1580,1650,1915),
      r'on peut dire (par définition valuative de la propreté) que $V$ a nécessairement','p12',
      'The upper bound is widened for the high right-hand strokes of définition valuative, already seen in overlapping p11. The left upper context contains clipped portions of the preceding model line; at the lower right are the tops of the later NB insertion, read completely in b12.')
audit(12,'insertion; deletion; handwritten number; C/H word difference',BOXES['p13'],
      r"un centre sur $X$, soit $a$, \deleted{et le centre} \inserted{(\uline{NB} $a$ pas} néc. de codim.1\ldots) et la condition",'p13',
      'The top left includes the tail la propreté) and part of the preceding que line; the lower edge meets the tops of the final I-map. The replacement and struck phrase, both complete, are the intended target. There is no closing parenthesis after pas.')
audit(13,'doubtful formula; C/H word difference',(251,2070,1624,2320),
      r"envisagée tantôt (assurant que $I_{x'}\longrightarrow\mathcal E_U^{\overline L}$ est nul) est que $a\in U$.",'p14',
      'The complete map spans two physical rows: source and arrow on the first, target on the second. Upper-edge fragments belong to néc. de codim.1… from the preceding line, already complete in b12. The upper audit bound provides clearance for the source I cap.')
audit(14,'handwritten number',BOXES['p15'],r'\margin{119}','p15')

main_baselines = [
 '--- à tirer au clair à l’occasion !',
 'Revenant au modèle U, fournissant',
 'un quotient E_U^{bar L} de E_L^{bar L}, d’où',
 'N_x′ → E_U^{bar L}, induisant I_x′ → E_U^{bar L},',
 'cancelled Il est clair que [uncertain si]',
 'qui n’est autre que l’hom [uncertain long mark] E_Ux → E_U',
 'associé à U_x → U. Si cet hom',
 'factorise par S_x, il est immédiat',
 'que l’hom induit I_x′ → E_U^{bar L} est',
 'nul, puisque [cancelled c′]est le noyau de',
 'E_Ux ⇒ E_Sx, et E_Ux → E_U se factorise par',
 'cet hom. [ A t-on une réciproque ?',
 'regarder ! ] / Quand on dispose d’un',
 'modèle projectif dont U est un ouvert,',
 'on peut dire (par définition valuative de',
 'la propreté) que V a nécessairement',
 'un centre sur X, soit a, [cancelled et le centre]',
 'néc. de codim.1…) et la condition',
 'envisagée tantôt (assurant que I_x′ →',
 'E_U^{bar L} est nul) est que a∈U.',
]
margin_baselines = {
 'upper': ['i.e. si V a','un “centre sur U”','i.e. domine un anneau','local de U…'],
 'lower': ['Ça devrait','être le cas pour','U “élémentaire”','à facteurs pas de','types (0,0) ni (0,1)…','[uncertain lié à ceci]','[uncertain enfin] à l’existence','d’un K'],
}

data = dict(
 page=PAGE,scan=120,reader='reader_c',line_count=35,
 line_count_detail=dict(main=20,margin=12,insertion=2,standalone_numbers=1,diagram_rows=0,total=35,
     convention='All distinct written baselines, including struck lines, raised insertions, oblique marginal lines, and the standalone foliation. Inline numbers are counted with their host baseline.',
     main_baselines=main_baselines,margin_baselines=margin_baselines,
     insertion_baselines=['raised I_x′ above the cancelled c′','raised (NB a pas above et le centre'],
     standalone_number_baselines=['119'],
     counting_note='regarder ! ] and Quand on dispose d’un occupy one continuing sloping physical row, counted once. The kernel-map row contains two maps but is one baseline.'),
 changes=changes,decisions=decisions,inventory=inventory,doubts=doubts,audit_boxes=audit_boxes,
 notes=[
  'Continuation note: the author returns to a model U and its quotient E_U, relates an inertia map to the local E-map, and states that factorization through the S_x-map makes the inertia image trivial. The kernel identification is transcribed as written.',
  'The upper margin restates the proposed factorization condition through a centre of V on U. A bracketed question asks for a converse. The lower margin suggests the elementary-U case with exclusions involving the literal ordered pairs (0,0) and (0,1); its closing linked phrases remain partly uncertain.',
  'The final paragraph uses a projectif model containing U as an open set and explicitly invokes the définition valuative de la propreté. The NB correction says that a need not be of codimension 1. The literal final formulation est que a∈U is retained.',
  'The unusual short form hom is preserved. No homom., extra se, repeated E-map, phantom deletion before modèle/on peut dire, or simplement is supplied from H.',
  'The question underline is one wavy stroke, represented by the available uline convention. The lower-margin underline is one continuous stroke across types and both ordered pairs; the source does not support a second horizontal underline solely under ni.',
  'The far-right small fragment in the first cancellation is now represented locally as deleted unsure{si}. The long mark after hom remains unassigned as letters or arrow. Existing cancelled c′ and the reduced closing marginal phrases remain explicitly uncertain.',
  'All 20 saved crops were visually inspected. p16–p20 address only places still open after initial crops; p18 corrects the cut right edge at anneau. Some blind-audit bounds are larger than their recorded initial crop bounds to include tall strokes already visible in overlapping crops. No additional crop of a settled reading was made.',
  'Every supplied mark M0116–M0126 is represented exactly once. Cancelled c′ and the added cancelled si are separate doubts, not invented mark IDs. Clearing a first reading, narrowing doubt, and reordering alternative readings are not counted as C base changes.',
  'The root reported a conditional group-theoretic proof check of the factorization implication. This reader did not repeat it and leaves formal checks for the root to record with the correct attribution. No mathematical consistency has been used to repair the ink.',
 ],
 checks=[],
 hand_observations=[
  dict(habit='Very small right-end hooks can distinguish a short single arrow from a dash.',places='First small E-map after hom, second E-map in the kernel row, and final I-map; compare the clear upper N/I maps.',holds='One shaft at the three marked single-arrow sites; the kernel E-map alone has two distinct shafts.',witness_errors='C leaves three dash/arrow choices; H regularizes the double-shaft kernel map to one shaft.'),
  dict(habit='Short hom is written without homom expansion.',places='qui n’est autre que l’hom; Si cet hom; que l’hom induit; cet hom.',holds='All four occurrences are short; only the final cet hom has its visible terminal stop.',witness_errors='H expands the word repeatedly and adds stops.'),
  dict(habit='Main baselines rise strongly to the right, and marginal notes are steeply oblique.',places='Both paragraphs and both left notes.',holds='High right-hand letter tops can fall in the preceding rectangular crop; audit bounds explicitly allow for them.',witness_errors='No inference of supralinear insertion is made merely from the sloping small E-map.'),
  dict(habit='Quotation marks are paired high ticks.',places='centre sur U and élémentaire in the two notes.',holds='The first closing pair follows U, not centre alone.',witness_errors='H gives angular quotes around centre alone and loses the scope of the quotation.'),
  dict(habit='Underlines differ in stroke form and extent.',places='Si, marginal si, question, types…(0,1), projectif, NB.',holds='Single strokes at these sites; the question stroke is wavy and the lower note uses one continuous long stroke.',witness_errors='C incorrectly assigns a separate double underline to ni.'),
 ],
 notation=[
  dict(written=r'\mathcal E_U^{\overline L},\mathcal E_L^{\overline L}',meaning_or_use='The quotient and its source named in the opening lines.',places='main lines 2–4 and the induced-map clauses'),
  dict(written=r'N_{x\prime},I_{x\prime}',meaning_or_use='The N and I labels in the maps to the quotient; the author explicitly calls the raised I the kernel in the later sentence.',places='main lines 4,9–10,19'),
  dict(written=r'\widetilde U_x,\widetilde S_x',meaning_or_use='The local objects in the E-maps and proposed factorization.',places='main lines 6–11'),
  dict(written=r'V,X,U,a',meaning_or_use='V is said to have a centre a on X; the stated condition is a∈U.',places='upper margin and final paragraph'),
  dict(written=r'(0,0),(0,1)',meaning_or_use='The two literal type pairs excluded in the lower marginal suggestion.',places='lower margin, fifth baseline'),
  dict(written='K',meaning_or_use='Final symbol of the reduced lower marginal note; no expansion is supplied from this page.',places='lower margin, eighth baseline'),
 ],
 abbreviations=[
  dict(written='hom',expansion='homomorphisme'),
  dict(written='i.e.',expansion='id est'),
  dict(written='néc.',expansion='nécessairement'),
  dict(written='codim.',expansion='codimension'),
  dict(written='NB',expansion='nota bene'),
 ],
 inspection=dict(whole=True,halves=['top','bottom'],crops=[crop(k) for k in BOXES],deletions_insertions_checked=True,
                 method='Visual reading only; Pillow contextual cropping, enlargement, contrast, optional rotation/sharpening. No OCR, external sources, or TeX compilation.',
                 followup_crop_reasons={'p16':'extra still-open cancellation fragment','p17':'still-open long mark and short connector','p18':'still-open anneau ending cut by original margin crop','p19':'still-open lower-margin words and underline extent','p20':'still-open linked closing phrases'}),
)

assert len(main_baselines)==20
assert sum(map(len,margin_baselines.values()))==12
assert len(decisions)==11
assert {d['id'] for d in decisions}=={f'M{i:04d}' for i in range(116,127)}
assert len({d['id'] for d in decisions})==11
for path in data['inspection']['crops']:
    assert (ROOT/'edition'/path).is_file(),path
tex=(REVIEW/f'{PAGE}.tex').read_text()
level=0
for match in re.finditer(r'(?<!\\)[{}]',tex):
    level += 1 if match.group()=='{' else -1
    assert level>=0,match.start()
assert level==0,level
assert not re.search(r'\\(?:note|struck|ill|add|uncertain)\b',tex)
assert tex.count('$') % 2 == 0
data['structural_validation']={
 'unescaped_braces_balanced':True,'math_delimiters_even':True,
 'supplied_mark_ids_exact':True,'saved_crops_exist':True,
 'C_base_change_rows':[r['id'] for r in changes if r['vs_C']],
 'H_change_rows':[r['id'] for r in changes if r['vs_H']],
 'no_tex_compilation':True,
}
(REVIEW/f'{PAGE}.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'page':PAGE,'changes':len(changes),'C_changes':sum(r['vs_C'] for r in changes),'H_changes':sum(r['vs_H'] for r in changes),'crops':len(BOXES),'doubts':len(doubts),'audit_boxes':len(audit_boxes),'line_count':35},ensure_ascii=False))
