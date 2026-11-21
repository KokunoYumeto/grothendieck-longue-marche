from pathlib import Path
import json
import re

WORK = Path('/workspace/scratch/481648fc487b/SP90_C13_150_work')
PACKET = Path('/workspace/scratch/481648fc487b/reader_packets/150_scan036')
OUT = WORK / 'reader_returns'
OUT.mkdir(exist_ok=True)

opening = r'(X,(X_i)_{i\in I}(B_\alpha,\mathcal E_\alpha)_{\alpha\in\unsure{\lambda|\Lambda}}'
union = r'\deleted{T}X_{I_0}=\bigcup_{\beta\in I_0}X_\beta'
pair = r'(B_{\unsure{\bar\alpha}},\mathcal E_\alpha)'
left22 = r'\underset{\text{stratification de }I^*}{(X_i^*)_{i\in I^*=I\setminus I_0}}'
right22 = r'''\underbrace{\big((\deleted{\unsure{\mathcal E}}B_\alpha,\mathcal E_\alpha)_{\alpha\in\Lambda},
(\dot X_\beta,\mathcal E_\beta)_{\beta\in I_0}\big)}
_{\substack{\text{famille \unsure{transverse|transversale}}\\\text{de sous-espaces}\\
\text{\unsure{bordants} ``cylindrisés''}\\
\text{de }X,\ \text{transversaux}\\\text{aux }X_i}}'''
display22 = '(22)\\qquad\nX^*,\\quad\n' + left22 + ',\n\\quad\n' + right22
display23 = r'''(23)\qquad
(X_\beta)_{\beta\in I_0},
(B_{\beta\alpha},\mathcal E_{\beta\alpha})_{\substack{\beta\in I_0\\\alpha\in\Lambda}}\big)'''

tex = r'''\scanpage{36}
par récurrence sur $\operatorname{card}I$ la notion de
donnée \deleted{de} coniques sur \deleted{cette base}
$''' + opening + r'''$
\deleted{On procède.} Si $I=\varnothing$, ce sera la structure
vide (il y en a une et une seule). Si
$I\ne\varnothing$, on prend $I_0$ ens des éléments minimaux
de $I$, et une donnée conique sera par
définition la donnée

\textcircled{a} d'un \deleted{tube}\inserted{vois. con. strict} $T_{I_0}$
de \deleted{\unsure{la somme}} $''' + union + r'''$,
transversal aux $''' + pair + r'''$ et
\deleted{\unsure{donc} admissible}
coniquement transversal aux $X_i$ ($i\in I$).
--- ce qui permet donc d'introduire les
structures (19), et en particulier

\[
''' + display22 + r'''
\]

en plus de
\[
''' + display23 + r'''
\]
On doit avoir de plus : $\infty$

\textcircled{b} Une structure conique sur (22) (ce qui
a un sens, par récurrence\ldots)
\margin{35}
'''

boxes = {
    'opening_data': [294,151,842,264],
    'cette_base_tuple': [996,143,1668,257],
    'tuple_edge_complete': [1370,135,1684,275],
    'on_procede': [298,249,697,356],
    'ce_sera': [1067,250,1351,325],
    'ens_elements': [915,434,1320,525],
    'sera_conique': [1022,548,1562,650],
    'tube_insert': [401,660,1031,812],
    'la_somme_union': [1037,690,1654,841],
    'pair_transversal': [834,820,1108,927],
    'donc_admissible': [1244,824,1670,927],
    'coniquement': [289,947,618,1093],
    'les_structures': [279,1035,1617,1269],
    'display22_left': [245,1254,997,1480],
    'display22_right': [931,1245,1670,1427],
    'display22_caption': [1165,1417,1634,1723],
    'display23': [244,1808,1435,1950],
    'infinity': [1042,1976,1135,2044],
    'b_conique': [393,2054,1659,2255],
    'folio35': [21,2302,82,2344],
}

changes = []
def change(place, C, H, final, evidence, crop, confidence, kind, error_kind,
           change_C, change_H, marked_in_H=False, consequential=''):
    changes.append(dict(place=place, C=C, H=H, final=final, evidence=evidence,
                        crop=f'150_scan036_{crop}.jpg', box=boxes[crop], confidence=confidence,
                        kind=kind, error_kind=error_kind, marked_in_H=marked_in_H,
                        change_C=change_C, change_H=change_H, consequential=consequential))

change('line 2 / donnée', r'\unsure{donnée|données}', 'donnée', 'donnée',
       'The last e has a short simple return, followed by a clear gap before the canceled de; there is no separate final s. The noun is singular, independently of the following plural adjective.',
       'opening_data', 'high', 'misread word', 'words', True, False)
change('line 2 / coniques', 'côniques', 'cônique', 'coniques',
       'The initial c and o lie below an empty space: no circumflex stroke is present. The later detached mark is the i dot. A low terminal s-like return follows the e, unlike the simple final e in donnée immediately to the left.',
       'opening_data', 'high', 'abbreviation expanded or spelling modernised', 'abbreviation/spelling', True, True,
       consequential='The source has singular donnée followed by plural coniques; the agreement is not repaired.')

old_opening = r'(X,(X_i)_{i\in I},(B_\alpha,\mathcal E_\alpha)_{\alpha\in\Lambda})'
change('line 2 / opening tuple separator', old_opening, old_opening, opening,
       'The white interval after the first family index i in I and before the opening parenthesis of the B/E pair has no comma. The index ends before that interval; its strokes do not supply a separator.',
       'tuple_edge_complete', 'high', 'text not on the page', 'text not on page', True, True)
change('line 2 / opening tuple right edge', old_opening + '$.', old_opening + '.', opening,
       'The B/E pair has its own closing parenthesis before the final index. At the dark right paper edge only two tiny protrusions survive; neither a complete outer closing parenthesis nor a terminal stop can be recovered. They are not supplied. The first crop ended at x1668, so one necessary completion to x1684 was made before this decision.',
       'tuple_edge_complete', 'medium', 'text not on the page', 'text not on page', True, True,
       consequential='The visible opening tuple remains unclosed at the paper edge.')
change('line 2 / final index of opening tuple', r'\alpha\in\Lambda', r'\alpha\in\Lambda',
       r'\alpha\in\unsure{\lambda|\Lambda}',
       'The terminal sign has a curved right stem rising above the point where its left arm joins, favoring lowercase lambda. The clear capital Lambda in display (23) has a different, complete apex. The edge and rapid formation prevent a categorical case decision.',
       'tuple_edge_complete', 'medium', 'misread symbol or index', 'symbols and indices', True, True,
       consequential='No identification of this lambda-shaped index with the later capital Lambda is imposed.')
change('line 3 / canceled opening verb', 'On procède', 'On posera', 'On procède.',
       'Below the horizontal strike, the word has a long p descender, a small ro run, an open c return, a tall d, and a final e. Those strokes favor procède over posera. The terminal point is recorded separately as a punctuation omission.',
       'on_procede', 'high', 'misread word', 'words', False, True)
change('line 3 / terminal point in canceled opening', r'\deleted{On procède}', r'\struck{On posera}',
       r'\deleted{On procède.}',
       'A dark isolated round point follows the final e, below the crossing stroke and before the unstruck Si. It belongs to the canceled phrase and is omitted by both witnesses.',
       'on_procede', 'high', 'omission', 'omissions', True, True)
change('line 3 / ce sera', 'ce sera', 'on pose', 'ce sera',
       'The first small group begins with an open c and a low e continuation. The next has an open s and a compressed era run. There is no n after an o and no p descender in this live phrase.',
       'ce_sera', 'high', 'misread word', 'words', False, True)
change('line 5 / ens without stop', 'ens', 'ens.', 'ens',
       'The abbreviation ends with a short downward return belonging to s. The following space before des has no detached point. The later dots and accents belong to éléments.',
       'ens_elements', 'high', 'abbreviation expanded or spelling modernised', 'abbreviation/spelling', False, True)
change('line 6 / conique', 'cônique', 'cônique', 'conique',
       'There is no accent over the initial o. The only detached upper mark is farther right over the i; the c/o outline and empty area above it are clear.',
       'sera_conique', 'high', 'abbreviation expanded or spelling modernised', 'abbreviation/spelling', True, True)
change('line 6 / sera', 'sera par', 'sur par', 'sera par',
       'An open s is followed by a long low era run with a final detached short a-like finish before par. This is the same compressed sera formation as line 3; it does not terminate immediately after ur.',
       'sera_conique', 'medium', 'misread word', 'words', False, True)
change('item a / canceled tube', r'\deleted{tube}', r"d'un \struck{\ill{}}", r'\deleted{tube}',
       'The crossing line still leaves the initial t upright, the low u trough, the b ascender and lower turn, and the final e return recoverable. The word is distinct from the raised replacement above it.',
       'tube_insert', 'high', r'readable ink left as \ill{}', 'readable ink left as illegible', False, True, True)
change('item a / plain T', r'\overline T_{I_0}', r'T_{I_0}', r'T_{I_0}',
       'The live T has one broad cap and a separate downward stem. The higher long rising curve connects the cancellation and raised replacement; it does not supply a detached horizontal overbar over T.',
       'tube_insert', 'high', 'misread symbol or index', 'symbols and indices', True, False)
change('item a / canceled la somme', r'\deleted{\unsure{la somme}}', r'de \struck{\ill{}}',
       r'\deleted{\unsure{la somme}}',
       'The initial looped l and rough s/mm ending support la somme, but the strike covers several internal letter portions. The existing C doubt is retained because every letter is not independently plain. H gives no readable letters at this place.',
       'la_somme_union', 'medium', r'readable ink left as \ill{}', 'readable ink left as illegible', False, True, True)
change('item a / overwritten T beneath left X', r'X_{I_0}=\bigcup_{\beta\in I_0}X_\beta',
       r'X_{I_0}=\bigcup_{\beta\in I_0}X_\beta', union,
       'Under the diagonal arms of the live X there is a distinct older horizontal cap and vertical downstroke forming T. These are not arms of X. The TeX places the canceled T before X to encode the physical superposition.',
       'la_somme_union', 'high', 'omission', 'omissions', True, True)
change('line 9 / detached mark above alpha', r'(B_\alpha,\mathcal E_\alpha)',
       r'(B_\alpha,\mathcal E_\alpha)', pair,
       'Above the alpha attached to B there is a detached short curved dash, with a low left end and nearly horizontal right end. It is darker than the paper and separate from B and alpha. A bar over alpha is the nearest literal encoding, but its exact function and shape remain uncertain.',
       'pair_transversal', 'medium', 'misread symbol or index', 'symbols and indices', True, True,
       consequential='The extra mark is retained without inventing a mathematical meaning for it.')
change('line 9 / canceled donc', r'\deleted{\unsure{donc} admissible}', r'\struck{\ill{} admissible}',
       r'\deleted{\unsure{donc} admissible}',
       'The initial tall d and final open c-like return are compatible with donc, but two heavy crossing strokes obscure the middle. C is not resolved; H is more noncommittal and leaves all letters illegible.',
       'donc_admissible', 'low', r'readable ink left as \ill{}', 'readable ink left as illegible', False, True, True)
change('line 10 / coniquement', 'côniquement', 'côniquement', 'coniquement',
       'The c/o group is followed by the n/i run and long q descender. Above the o there is clear blank paper and no circumflex stroke.',
       'coniquement', 'high', 'abbreviation expanded or spelling modernised', 'abbreviation/spelling', True, True)
change('lines 11–12 / les structures', 'les\nstructures (19)', 'la structure (19)', 'les\nstructures (19)',
       'The article at the right end of the first line has a small low terminal return after its looped l, and structures on the next line has the additional terminal s-like return. The plural is favored; the pen compresses these endings.',
       'les_structures', 'medium', 'misread word', 'words', False, True)
change('display (22) / left annotation without brace',
       r'\underbrace{(X_i^*)_{i\in I^*=I\setminus I_0}}' + '\n' + r'_{\text{stratification de }I^*}',
       r'\underbrace{X^{*},\ (X^{*}_i)_{i\in I^{*}=I\setminus I_0}}_{\text{stratification de } I^{*}}',
       left22,
       'The interval between the indexed X-star family and stratification de I-star contains no brace stroke. The annotation begins beneath the family rather than beneath the standalone X-star. A true underbrace is visibly drawn only under the right-hand group.',
       'display22_left', 'high', 'misread symbol or index', 'symbols and indices', True, True,
       consequential='The annotation is placed below the family without supplying a brace or bringing the standalone X-star under one.')
change('display (22) / transverse or transversale', r'\text{famille transverse}', r'\text{famille transversale}',
       r'\text{famille \unsure{transverse|transversale}}',
       'The word ends in a tall compressed turn followed by a low terminal return. Transverse is favored, but the turn cannot be separated decisively into the possible letters of transversale. This is an unresolved word disagreement with H, not a certainty-only difference against C.',
       'display22_caption', 'medium', 'misread word', 'words', False, True)
change('display (23) / supplied outer opening parenthesis',
       r'\big((X_\beta)_{\beta\in I_0}', r'\bigl((X_\beta)_{\beta\in I_0}',
       r'(X_\beta)_{\beta\in I_0}',
       'There is only one opening parenthesis before X_beta. The space after the equation number is empty until that stroke. A separate final closing parenthesis is present after the second indexed family and is retained without adding its missing outer mate.',
       'display23', 'high', 'text not on the page', 'text not on page', True, True,
       consequential='The source display remains parenthetically unbalanced.')
change('display (23) / stacked index without comma',
       r'(B_{\beta\alpha},\mathcal E_{\beta\alpha})_{\substack{\beta\in I_0\\\alpha\in\Lambda}}',
       r'(B_{\beta\alpha},\mathcal E_{\beta\alpha})_{\beta\in I_0,\ \alpha\in\Lambda}',
       r'(B_{\beta\alpha},\mathcal E_{\beta\alpha})_{\substack{\beta\in I_0\\\alpha\in\Lambda}}',
       'The beta-in-I-zero and alpha-in-Lambda conditions occupy two stacked rows. No comma follows the upper condition or precedes the lower one. H inserts a comma while putting them on one line.',
       'display23', 'high', 'text not on the page', 'text not on page', False, True)
change('line 16 / infinity sign after colon', r'\unsure{\infty|a}', '[absent]', r'\infty',
       'The small sign has two closed horizontal loops joined at a central waist. There is no independent upright a stem or terminal a return. The complete isolated sign is visible beside the colon.',
       'infinity', 'high', 'misread symbol or index', 'symbols and indices', True, True,
       consequential='The standalone infinity-shaped sign is retained without assigning it a role in the definition.')
change('item b / conique', 'cônique sur (22)', 'cônique sur (22)', 'conique sur (22)',
       'The initial co group is clear and has no upper accent. The i dot sits farther to the right. This agrees with the other three unaccented conique/coniques/coniquement occurrences on this leaf.',
       'b_conique', 'high', 'abbreviation expanded or spelling modernised', 'abbreviation/spelling', True, True)
change('bottom-left foliation', r'\margin{35}', '[absent]', r'\margin{35}',
       'A thin, lighter 3 is followed by a 5 with a horizontal cap and curved lower bowl. The number is 35. Its hand is not securely attributable to the author, so it is recorded as a margin number rather than his manuscript page number.',
       'folio35', 'high', 'omission', 'omissions', False, True)

marks = [
    dict(mark=r'\unsure{donnée|données}', context=r'\unsure{donnée|données} \deleted{de} côniques',
         decision='first', reading='donnée', evidence='A simple final e return, then a gap; no terminal s.',
         crop='150_scan036_opening_data.jpg', box=boxes['opening_data'], confidence='high'),
    dict(mark=r'\unsure{la somme}', context=r'de \deleted{\unsure{la somme}} $X_{I_0}',
         decision='undecided', reading=r'\unsure{la somme}',
         evidence='The initial l and partial s/mm strokes support the reading, but the strike obscures internal letters. The strict criterion for resolving an existing struck-text doubt is not met.',
         crop='150_scan036_la_somme_union.jpg', box=boxes['la_somme_union'], confidence='medium'),
    dict(mark=r'\unsure{donc}', context=r'\deleted{\unsure{donc} admissible}',
         decision='undecided', reading=r'\unsure{donc}',
         evidence='Initial d and a terminal open return survive; the middle remains covered by heavy cancellation. No forced resolution.',
         crop='150_scan036_donc_admissible.jpg', box=boxes['donc_admissible'], confidence='low'),
    dict(mark=r'\unsure{\infty|a}', context=r'On doit avoir de plus : $\unsure{\infty|a}$',
         decision='first', reading=r'\infty',
         evidence='Two closed horizontally arranged loops and a central waist, with no upright a stem.',
         crop='150_scan036_infinity.jpg', box=boxes['infinity'], confidence='high'),
]

inventory = []
def inv(kind, position, words, hand='his hand'):
    inventory.append(dict(element=f'036.E{len(inventory)+1:02d}', kind=kind, position=position,
                          first_words_or_objects=words, sheet_kind='text', hand=hand, transcribed='yes'))
inv('text', 'upper main text, lines 1–7', 'par récurrence sur card I … définition la donnée')
inv('deletion', 'line 2, after donnée', 'de')
inv('deletion', 'line 2, before the opening tuple', 'cette base')
inv('deletion', 'line 3, before Si', 'On procède.')
inv('text', 'item a, main lines 8–10', "circled a; d'un … coniquement transversal aux X_i")
inv('deletion', 'item a, line 8', 'tube')
inv('insertion', 'above canceled tube, joined by a long rising leader', 'vois. con. strict')
inv('deletion', 'line 8, after de', r'\unsure{la somme}')
inv('deletion', 'line 8, underneath live X at left of union equality', 'T overwritten by X')
inv('deletion', 'line 9, after et', r'\unsure{donc} admissible')
inv('text', 'lines 11–12', "— ce qui permet donc d'introduire les structures (19)")
inv('display', 'middle of page, line 13', '(22); X-star, indexed X-star family, two indexed pairs')
inv('deletion', 'display (22), immediately before B_alpha', r'\unsure{\mathcal E}')
inv('text', 'under the left indexed family in display (22), no brace', 'stratification de I-star')
inv('text', 'five-line annotation under the right underbrace in display (22)', r'famille \unsure{transverse|transversale} … aux X_i')
inv('text', 'line 14 above display (23)', 'en plus de')
inv('display', 'lower main text, line 15', '(23); indexed X_beta family and indexed B/E pair; unmatched final closing parenthesis')
inv('text', 'line 16', 'On doit avoir de plus : infinity sign')
inv('text', 'item b, lines 17–18', 'circled b; Une structure conique sur (22) … par récurrence…')
inv('margin note', 'extreme lower-left edge', '35', 'uncertain; thin lighter foliation, not securely his hand')

doubts = [
    dict(place='line 2 / terminal index of opening tuple', reading=r'\unsure{\lambda|\Lambda}', alternatives=r'\lambda | \Lambda', confidence='medium'),
    dict(place='item a / canceled la somme', reading=r'\unsure{la somme}', alternatives='la somme remains the favored reading; internal canceled letters not separately recoverable', confidence='medium'),
    dict(place='line 9 / mark above alpha of B', reading=r'B_{\unsure{\bar\alpha}}', alternatives='short curved dash above alpha; mathematical function undetermined', confidence='medium'),
    dict(place='line 9 / canceled donc', reading=r'\unsure{donc}', alternatives='donc favored, middle letters obscured', confidence='low'),
    dict(place='display (22) / canceled glyph before B_alpha', reading=r'\deleted{\unsure{\mathcal E}}', alternatives=r'E-like lower lobes; upper part heavily covered; H also considers dotted B', confidence='medium'),
    dict(place='display (22) / caption ending', reading=r'\unsure{transverse|transversale}', alternatives='transverse | transversale', confidence='medium'),
    dict(place='display (22) / bordants', reading=r'\unsure{bordants}', alternatives='bordants favored; compressed middle does not permit a secure shorter literal expansion or abbreviation reading', confidence='medium'),
]

notes = [
    'The page reports an inductive definition by card I of conical data on the displayed objects. It describes a unique empty structure when I is empty, then uses the set I_0 of minimal elements when I is nonempty. This is a report of the manuscript, not a proof check.',
    'Item a asks for a strict conical neighborhood of the union indexed by I_0, with the stated transversality. The text then introduces the objects labeled (22), the additional family (23), and begins item b by asking for a conical structure on (22). No mathematical validity check was performed.',
    'The opening noun is singular donnée, while its adjective has a visible final s: coniques. All four conique/coniques/coniquement occurrences lack a circumflex on the actual ink; the two witnesses supply one. This spelling and the number mismatch are preserved.',
    'The opening tuple has no separator comma after its first family index, no recoverable outer closing parenthesis, and no recoverable terminal stop at the dark right edge. Its last index is lambda-shaped and remains lambda/capital-Lambda doubtful. The first crop ended 16 pixels short of the image edge; a single necessary completion crop was made while this place was still unresolved. Both crop files are retained.',
    'The older T beneath the live X in the union equality is physically superposed. The inline deleted-T/live-X sequence records that replacement. The long rising stroke near the other T belongs to the canceled tube and raised vois. con. strict replacement, not a second cap or overbar.',
    'A detached curved dash is visible over the alpha attached to B in the transversal pair. Its literal bar-like appearance is retained with doubt; no mathematical role is inferred.',
    'The left stratification annotation in (22) has no drawn brace; only the right family has a drawn underbrace. The standalone X-star is outside the left annotation. In the right caption, de X and aux X_i are unstarred in the manuscript and are preserved.',
    'Display (23) has one opening parenthesis before X_beta and a separate extra final closing parenthesis. The missing outer opening is not supplied. The index conditions on the second family are stacked, with no comma between them.',
    'The infinity-shaped sign after On doit avoir de plus is visibly present; its intended role is not established by the reading. The bottom-left 35 is thin lighter foliation of uncertain hand, with no confident attribution to the author.',
    'The canceled E-like glyph in (22) is accounted for in H’s editorial note although absent from its main formula. Adding doubt to that glyph is not counted as a new C error or an H omission. H’s certainty-only treatment of cylindrisés is likewise not counted as a separate reading disagreement.',
    'Line count 24 comprises 18 principal baselines, the separate left annotation under (22), and the five right-caption baselines; the raised replacement and foliation are separately inventoried. Whole view and both native halves were each viewed once, followed by all 20 crop images covering 19 distinct places. No OCR, external research, or TeX compilation was used.',
]

notation = [
    dict(form=r'I_0', meaning_or_shape='Set of minimal elements named in the text; zero may be small and filled, while the capital I retains its two cap strokes.', places='line 5, item a, displays (22) and (23)'),
    dict(form=r'T_{I_0}', meaning_or_shape='Plain T with one horizontal cap; the nearby higher curve is a placement leader. A separate older T is overwritten by X in the union equality.', places='item a, line 8'),
    dict(form=r'B_{\unsure{\bar\alpha}}', meaning_or_shape='Detached short curved dash above the alpha index, retained graphically with uncertainty; no established semantic meaning.', places='line 9, transversal pair'),
    dict(form=r'\infty', meaning_or_shape='Two small horizontally joined closed loops; isolated after the colon, purpose unspecified.', places='line 16'),
]
abbreviations = [
    dict(form='card', expansion='cardinal'),
    dict(form='ens', expansion='ensemble'),
    dict(form='vois.', expansion='voisinage'),
    dict(form='con.', expansion='conique'),
]
hand_log = [
    dict(habit='The conique family is written without a circumflex, while an i dot may sit high and farther right.', places='036, lines 2, 6, 10 and item b', consistent='all four occurrences on this page', witness_errors='Both C and H supply circumflexes at all four places; H also loses the plural s in the opening adjective.'),
    dict(habit='Long low pen runs compress several ordinary letters without necessarily indicating an abbreviation.', places='036, ce sera, sera par, éléments, caption words', consistent='recurrent; some caption interiors remain doubtful', witness_errors='H reads ce sera as on pose and sera as sur. No new abbreviation is asserted for the compressed éléments.'),
    dict(habit='Small zero can appear as a solid point next to the serif capital I.', places='036, I_0 in item a and display (22)', consistent='some zeros are filled and some retain an opening', witness_errors='No new index-zero error established; individual digits were read rather than normalized.'),
    dict(habit='A long curved replacement leader can rise over a nearby capital T and resemble an extra bar.', places='036, canceled tube / inserted vois. con. strict / T_I0', consistent='one local occurrence', witness_errors='C reads an overlined T where only its ordinary cap is present.'),
    dict(habit='Horizontal cancellation can leave ascenders and descenders visible while obscuring internal short letters.', places='036, On procède., tube, la somme, donc admissible, canceled E-like glyph', consistent='varied visibility; existing struck-text doubts retained unless every letter is plain', witness_errors='H leaves tube illegible; la somme and donc remain partly readable but doubtful. Both omit the canceled phrase’s terminal point.'),
    dict(habit='A lowercase-lambda-like right stem can rise above the left-arm join; this is not enough to establish a universal capital-Lambda habit.', places='036, opening tuple compared with capital Lambda in display (23)', consistent='one doubtful occurrence against a clearer capital form', witness_errors='Both witnesses confidently use capital Lambda at the edge; a narrow lambda/Lambda doubt is retained.'),
]

second_boxes = []
def audit(kind, coords, reading, reason):
    second_boxes.append(dict(box=f'b{len(second_boxes)+1:02d}', kind=kind, coords=coords, reading=reading, reason=reason))
audit('struck passage; C/H word difference', boxes['opening_data'], r'donnée \deleted{de} coniques',
      'C noun doubt resolved; singular/plural adjective difference and absent circumflex; every canceled de stroke included.')
audit('struck passage; doubt formula; low-confidence departure', [996,135,1684,275],
      r'\deleted{cette base} $' + opening + '$',
      'Complete opening tuple through the true right image edge, including its lambda/capital-Lambda doubt, absent separator and unclosed ending; also covers canceled cette base.')
audit('struck passage; C/H word difference', boxes['on_procede'], r'\deleted{On procède.}',
      'Canceled word disagreement and terminal stop omitted by both witnesses.')
audit('C/H word difference', boxes['ce_sera'], 'ce sera la',
      'Genuine ce sera versus on pose difference.')
audit('handwritten number; C/H word difference', [280,425,1658,550],
      r'$I\ne\varnothing$, on prend $I_0$ ens des éléments minimaux',
      'Complete line includes numerical zero and the ens/ens. punctuation difference.')
audit('C/H word difference', boxes['sera_conique'], 'conique sera par',
      'Absent circumflex and sera versus sur; the latter remains a medium-confidence witness disagreement.')
audit('insertion; struck passage; handwritten number; C/H word difference', boxes['tube_insert'],
      r"\textcircled{a} d'un \deleted{tube}\inserted{vois. con. strict} $T_{I_0}$",
      'Every raised replacement and canceled tube; plain T rather than overlined T; numerical zero in its complete subscript.')
audit('struck passage; doubt formula; handwritten number; C/H word difference', boxes['la_somme_union'],
      r'de \deleted{\unsure{la somme}} $' + union + '$,',
      'Retained struck-text doubt, recovered overwritten T, and complete union equality with all zero indices.')
audit('doubt formula; low-confidence departure', boxes['pair_transversal'], '$' + pair + '$',
      'Whole transversal pair, including the uncertain detached bar-like mark over alpha.')
audit('struck passage; C/H word difference', boxes['donc_admissible'],
      r'\deleted{\unsure{donc} admissible}',
      'Every canceled letter; retained C doubt and substantive partial reading against H illegibility.')
audit('C/H word difference', boxes['coniquement'], 'coniquement',
      'Both witnesses supply an absent circumflex; enlarged word is preserved for audit.')
audit('C/H word difference; handwritten number', boxes['les_structures'],
      "--- ce qui permet donc d'introduire les\nstructures (19), et en particulier",
      'Plural article/noun difference across the line break and handwritten reference (19).')
audit('struck passage; doubt formula; handwritten number; C/H word difference', [245,1245,1684,1730],
      '\\[\n' + display22 + '\n\\]',
      'Whole display (22), every index zero, canceled E-like symbol, both annotations, disputed caption ending and bordants doubt, and absent left brace.')
audit('handwritten number', boxes['display23'], '\\[\n' + display23 + '\n\\]',
      'Whole display (23), all numerical zeros, unmatched final closing parenthesis, and stacked index conditions without comma.')
audit('doubt formula', boxes['infinity'], r': $\infty$',
      'Complete isolated sign from C’s infinity/a doubt, resolved on its crop; adjacent colon retained.')
audit('C/H word difference; handwritten number', [283,2054,1659,2255],
      r'\textcircled{b} Une structure conique sur (22) (ce qui' + '\n' + r'a un sens, par récurrence\ldots)',
      'Both lines of item b, absent circumflex, handwritten reference (22), and the three final dots.')
audit('margin note; handwritten number', boxes['folio35'], r'\margin{35}',
      'Entire bottom-left foliation, with hand attribution left uncertain.')

data = dict(scan=36, reader='reader_c', line_count=24, changes=changes, marks=marks,
            inventory=inventory, doubts=doubts, notes=notes, check_events=[],
            notation=notation, abbreviations=abbreviations, hand_log=hand_log,
            second_boxes=second_boxes)

(OUT / '150_scan036.tex').write_text(tex, encoding='utf-8')
(OUT / '150_scan036.json').write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

# Structural checks only. No TeX compilation or OCR.
norm = lambda s: re.sub(r'\s+', ' ', s).strip()
Ctext = (PACKET / 'C.tex').read_text(encoding='utf-8')
Htext = (PACKET / 'H.tex').read_text(encoding='utf-8')
errors = []
for i, item in enumerate(changes, 1):
    if item['final'] not in tex:
        errors.append(f'change {i}: final not literal in proposed TeX')
    if norm(item['C']) not in norm(Ctext):
        errors.append(f'change {i}: C quote not found')
    if item['H'] != '[absent]' and norm(item['H']) not in norm(Htext):
        errors.append(f'change {i}: H quote not found')
    if not (WORK / 'crops' / item['crop']).exists():
        errors.append(f'change {i}: missing crop')
for item in marks:
    if item['mark'] not in Ctext:
        errors.append('unmatched C mark: ' + item['mark'])
for name in boxes:
    if not (WORK / 'crops' / f'150_scan036_{name}.jpg').exists():
        errors.append('missing crop: ' + name)
depth = 0
for match in re.finditer(r'(?<!\\)[{}]', tex):
    depth += 1 if match.group() == '{' else -1
    if depth < 0:
        errors.append('negative TeX brace depth')
if depth:
    errors.append(f'TeX brace depth {depth}')
if len(re.findall(r'(?<!\\)\$', tex)) % 2:
    errors.append('odd dollar count')
print(json.dumps(dict(changes=len(changes), change_C=sum(x['change_C'] for x in changes),
                      change_H=sum(x['change_H'] for x in changes), marks=len(marks),
                      inventory=len(inventory), doubts=len(doubts), second_boxes=len(second_boxes),
                      crop_images=len(boxes), errors=errors), ensure_ascii=False))
if errors:
    raise SystemExit(1)
