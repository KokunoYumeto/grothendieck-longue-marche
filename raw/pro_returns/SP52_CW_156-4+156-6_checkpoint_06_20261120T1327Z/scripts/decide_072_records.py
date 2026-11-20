"""Build scan-072 administrative records from root's final text and decisions.

No images are opened. No OCR, compilation, mathematical check, shared-file build,
or finalization is performed. Only decisions/156-4_072.json is written.
"""
from pathlib import Path
from copy import deepcopy
import hashlib
import json
import re

O = Path(__file__).resolve().parents[1]
KEY = '156-4_072'
FILENAME = 'J156-4-09_156-4_scan072.tex'
P = O.parent / 'page_packets' / KEY
C = (P / 'C.tex').read_text()
H = (P / 'H.tex').read_text()
T = (O / 'pages' / FILENAME).read_text()
META = json.loads((P / 'metadata.json').read_text())
R = {n: json.loads((O / 'readers' / KEY / n / 'report.json').read_text())
     for n in ('R1', 'R2', 'R3')}
RT = {n: (O / 'readers' / KEY / n / 'reading.tex').read_text() for n in R}
DX = {n: {x['id']: x for x in R[n]['differences']} for n in R}


def macro(text, name, start=0):
    a = text.index('\\' + name + '{', start)
    i = a + len(name) + 2
    depth = 1
    while depth:
        if i >= len(text):
            raise ValueError('Unclosed macro')
        slash = 0
        j = i - 1
        while j >= 0 and text[j] == '\\':
            slash += 1
            j -= 1
        if slash % 2 == 0:
            if text[i] == '{':
                depth += 1
            elif text[i] == '}':
                depth -= 1
        i += 1
    return text[a:i]


def macros(text, name):
    out, pos = [], 0
    while True:
        a = text.find('\\' + name + '{', pos)
        if a < 0:
            return out
        value = macro(text, name, a)
        out.append(value)
        pos = a + len(value)


def line_with(needle, text=T):
    return next(s for s in text.splitlines() if needle in s)


def section(start, end, text=T):
    a = text.index(start)
    return text[a:text.index(end, a)].rstrip()


def environment(text, name, start=0):
    a = text.index('\\begin{' + name + '}', start)
    end = '\\end{' + name + '}'
    b = text.index(end, a) + len(end)
    return text[a:b]


CU = macros(C, 'unsure')
assert len(CU) == 30
assert H.count(r'\ill{}') == 15
CONTEXT_LINES = [s for s in (P / 'C_context.md').read_text().splitlines() if s.startswith('| ')]
assert len(CONTEXT_LINES) == 23
CAP = r'\mathrel{\vdash\joinrel\dashv}'
CAPITAL = macro(T, 'unsure', T.index('de la contrée'))
TOUT = r'\unsure{tout|\deleted{tout}}'
VERB = r'\unsure{satisfont|satisfait}'
MAPPING = macro(T, 'unsure', T.index("par $M'"))
QUESTION = macro(T, 'margin', T.index('% slanted left margin'))
MARK = section('% fig-b-curled-mark', r'\node[anchor=west] at (2.65,-1.6)')
INITIAL = macro(T, 'unsure', T.index('% The worked initial'))
SYM = r'sym\unsure{e|é}trique\\en $\leq,\preceq$'
FIRST_NOUN = r'\unsure{str.tes|strates}'
SECOND_NOUN = r'\unsure{\deleted{S}|S|s}tr\unsure{a|.}tes'
TEL = r'\unsure{tel|\deleted{tel}}les'
GTAIL = r'\unsure{G_n|G_m|G}'
COMPLEMENT = r'Ce compl\unsure{\.{e}|é|e}ment servira'
BODY_G = macro(T, 'unsure', T.index('On dit que'))
LOWER_G = macro(T, 'unsure', T.index(r'\margin{sur la sous-figure'))
PUNCT = macro(T, 'unsure', T.index('% figure: bottom-punctuation'))
FINAL_WORD = r'\deleted{\unsure{sous-fig|sous-fig.}}'
CORRESPOND = "s'en correspond"
FIRST_DIAGRAM = environment(T, 'tikzcd')
SECOND_DIAGRAM = environment(T, 'tikzcd', T.index(FIRST_DIAGRAM) + len(FIRST_DIAGRAM))
C_DIAGRAMS = macros(C, 'diagram')
PLEINE_ARM = line_with(r'\draw[line width=.55pt] (8.45,.48)')
LONG_ARM = line_with(r'\draw[line width=.45pt] (1.45,-2.14)')
SHORT_ARM = line_with(r'\draw[line width=.45pt] (6.8,-2.02)')
HEADLESS = line_with(r'\draw[line width=.6pt] (4.2,-.8)')
C_POINTER = section(r'\draw[line width=.45pt] (3.15,-1.3)', r'\end{tikzpicture}')
C_RESIDUAL = line_with(r'\draw[line width=.65pt] (.09,-1.03)')
POINTS = section(r'\fill (2.01,-.88)', r'\draw[line width=.4pt] (-.30,-.18)')
POINT3 = line_with(r'\fill (-.46,-2.12)')
LEFT_RULE = line_with(r'\draw[line width=.4pt] (-.30,-.18)')
B_RULES = section(r'\draw[line width=.5pt] (6.88,-3.67)', r'\end{tikzpicture}')
C_INSERT = macro(C, 'inserted', C.index("s'en"))
H_INSERT = macro(H, 'add', H.index("s'en"))
T_INSERT = macro(T, 'inserted', T.index('% fig-a-insertions'))
C_LOWER = section("par $M'", '\n\n% slanted', C)
H_LOWER = section(r"par $\mathcal{M}'", '\n  \\item[b)]', H)
T_LOWER = line_with("{par $M'")
H_NOTES = macros(H, 'note')
assert len(H_NOTES) == 2
for value in (CAPITAL, TOUT, VERB, MAPPING, QUESTION, INITIAL, SYM, FIRST_NOUN,
              SECOND_NOUN, TEL, GTAIL, COMPLEMENT, BODY_G, LOWER_G, PUNCT,
              FINAL_WORD, CORRESPOND, FIRST_DIAGRAM, SECOND_DIAGRAM):
    assert value in T, value

# Root's authorized evidence allowlist: no image is opened by this script.
E = {}
ALLOW = {'R1': {5, 11, 15}, 'R2': set(), 'R3': set(range(1, 18))}
for reader, numbers in ALLOW.items():
    for crop in R[reader]['crops']:
        number = int(Path(crop['path']).name[:2])
        if number not in numbers:
            continue
        value = deepcopy(crop)
        path = Path(value['path'])
        value['path'] = str(path.relative_to(O)) if path.is_absolute() else str(path)
        E[reader.lower() + '_' + f'{number:02d}'] = value
for crop in json.loads((O / 'crops' / KEY / 'manifest.json').read_text()):
    tag = Path(crop['path']).name[:3]
    if tag in {'a01', 'a02', 'a03', 'a04', 'a05'}:
        E[tag] = deepcopy(crop)
assert len(E) == 25, sorted(E)
assert all((O / e['path']).exists() for e in E.values())
E['a02']['root_framing_note'] = (
    'The lower edge clips the lowest G/order strokes. Existing R1/15 starts at '
    'source y2205 and overlaps a02 through y2215, covering the lower tails. '
    'Both crops are cited; no second square crop was made.')


def evidence(row, key, supporting=()):
    e = E[key]
    row.update(crop=e['path'], bbox=e['bbox'], bbox_image=e['source'],
               evidence_basis='Root viewed this crop; record assembly was text-only.')
    if supporting:
        row['supporting_crops'] = [E[k]['path'] for k in supporting]
        row['supporting_evidence'] = [
            {f: E[k][f] for f in ('path', 'source', 'bbox')} for k in supporting]


D = deepcopy(R['R1']['differences'])
EV = {
 1:'a01',2:'a01',3:'r3_01',4:'r3_02',5:'r3_03',6:'r3_03',7:'r3_04',8:'r3_04',
 9:'r3_04',10:'r1_05',11:'r1_05',12:'r3_06',13:'r3_07',14:'r3_07',15:'r3_07',
 16:'r3_07',17:'r3_07',18:'r3_07',19:'r3_08',20:'r3_08',21:'r3_08',22:'r3_09',
 23:'a04',24:'r3_10',25:'r3_10',26:'r3_10',27:'a04',28:'r3_10',29:'r3_10',
 30:'r3_11',31:'r3_11',32:'r3_11',33:'r3_11',34:'r3_11',35:'r3_11',36:'r3_11',
 37:'r3_11',38:'r3_11',39:'r3_11',40:'r3_13',41:'r1_11',42:'r3_12',43:'r1_11',
 44:'a03',45:'a03',46:'r3_14',47:'r3_14',48:'a02',49:'r3_15',50:'r3_15',
 51:'r3_15',52:'r3_15',53:'r3_15',54:'r3_15',55:'r3_15',56:'r1_15',57:'r1_15',
 58:'r1_15',59:'r1_15',60:'r1_15',61:'r3_17',62:'r3_17'}
for i, row in enumerate(D, 1):
    row['id'] = f'072-D{i:02d}'
    row['reader_source_ids'] = {'R1': [f'D{i:03d}']}
    row['decision'] = 'Root retains the indicated local reading; no mathematical repair is made.'
    row.pop('source', None)
    evidence(row, EV[i])


def amend(number, **fields):
    D[number - 1].update(fields)


amend(1, confidence='medium')
amend(3, reading='quand $= =$', decision='Retain both literal pairs of strokes; do not expand them to même.')
amend(5, decision='Read the raised bracketed pleine once at the definition. H’s bracketed placeholder after en forme maps to this same item, not to a second missing word.',
      scope_note='Bracketed word, underline and insertion attachment only; the distinct hook is D06.')
amend(6, reading=PLEINE_ARM, scope_note='The distinct long hooked leader only; its word is D05.')
amend(7, reading=CAPITAL, decision='Keep the local overprint alternatives and add plain calligraphic C. Convention 4 already permits C’s deleted-old/live sequence to encode one overwritten position; only the additional plain-C alternative is a C certainty change, not zero-width placement.')
amend(9, change_h=False, decision='Resolve C to the bowed preceq; H’s preccurlyeq represents the same observed bowed order.')
amend(10, reading=TOUT, confidence='low',
      scan_shows='The long bar at tout may be the last t bar or a cancellation. Root’s R1/05 view does not settle its state.',
      decision='Keep live tout first and struck tout second; grammatical expectation does not decide the crossing.')
amend(11, reading=VERB, change_c=True, confidence='low',
      scan_shows='A low closed oval follows f; no independent i dot is secure. Root puts satisfont first while retaining satisfait.',
      decision='Retain both alternatives with satisfont first. Under convention 6, first-candidate priority records what the ink favours, so this is a C preference revision; no grammatical correction is claimed.')
amend(13, reading=CORRESPOND, change_h=False,
      decision='Resolve the word as correspond. Convention 7 joins the physical corre-/spond division; the written hyphen is ink evidence only.',
      scope_note='One lexical uncertainty only; joining the physical line-end hyphen is not counted as a change.')
amend(14, reading=CAP, decision='The inserted link has a cap at each end; no arrowhead is supplied from the application meaning.')
amend(15, c=C_INSERT, h=H_INSERT, reading=T_INSERT,
      scan_shows='Both inserted family-F letters have curved looped heads and stems, rather than Gothic construction.',
      scope_note='The two family-F alphabets only. Mapping sign is D14; the plain intersection M is D63.')
amend(16, reading=section(r"\node[anchor=west] at (6.9,-1.9)", r"\draw[line width=.45pt] (1.45,-2.14)"),
      scope_note='Only raised M prime and baseline de M. The intervening mapping node is excluded from this count; its sign and alphabets are D14/D15/D63. The independent M-prime arm is D18.')
amend(17, reading=LONG_ARM, scope_note='Long insertion arm only; no text is counted again.')
amend(18, reading=SHORT_ARM, scope_note='Short raised-M-prime insertion arm only.')
amend(19, reading=MAPPING, decision='Retain left-cap-and-dash, two caps, and mapsto alternatives. The right endpoint is too worked to choose one identity.')
amend(20, c=C_LOWER, h=H_LOWER, reading=T_LOWER,
      scan_shows='The lower family F prime and membership-family F each have curved looped family-letter forms.',
      scope_note='Only the family F prime and membership-family F alphabets. Plain M primes, mapping endpoint, and barred F have separate rows.')
amend(22, reading=QUESTION,
      scan_shows='The main question, stricte and de are readable. The first condition group is compressed, et is crossed and uncertain, and a05 shows a short lge/large group followed by an actual closing curve.',
      decision='Retain the full question as one H passage. Keep the first condition and et uncertain; resolve stricte and de; retain lge/large with the terminal parenthesis present.',
      scope_note='H’s three placeholders belong to this one compressed marginal block; no artificial word-by-word partition is made.')
evidence(D[21], 'r3_09', ('a05',))
amend(23, scan_shows='Root a04 shows a detached comma after envisagées at the right edge, absent from both witnesses.',
      decision='Add the visible comma; do not infer its absence from reader crops with shorter right extent.')
amend(25, reading=MARK, decision='Retain the uncertain curled character and the two small crossing strokes literally; no brace/question identity is forced.')
amend(26, reading=r'\unsure{savoir|à savoir} :', change_c=True,
      decision='Keep both candidates under deletion, savoir first because an initial à is not independently secure. Convention 6 makes this changed first-candidate priority a C preference revision; no grammatical inference is used.')
amend(27, scan_shows='Root a04 covers the deleted clause through the right scan edge: X ∈ is followed by blank space, with no F.',
      decision='Retain the ending si X∈. Reject H’s extra F using complete right-edge coverage.')
amend(28, decision='Read the raised replacement qu’on va formuler; H’s editorial qui ne guess does not override the ink.')
amend(29, reading=section(r"\node[anchor=west] at (3.35,-1.6)", r"\end{tikzpicture}"),
      scope_note='Relative placement of deletion, raised replacement and later plus bas only; word content is D26–D28.')
amend(30, reading='reporter', confidence='medium', decision='Resolve reporter from its p descender and later t; no j is supplied.')
amend(31, decision='Retain fixé/fixée; the possible extra final e remains merged with the ending.')
amend(32, reading="G" + CAP + "G'", decision='Retain the two-capped G-to-G-prime link; its missing following comma is a separate D38 scope.')
amend(33, location='Marginal c, one worked initial and its lower residual strokes',
      reading=INITIAL + 'ous-fig.', additional_readings=[C_RESIDUAL],
      scan_shows='The initial has S/s-like outer strokes and F-like internal bars, with lower residual marks. A securely distinct earlier F layer is not established.',
      decision='Retain F-under-S/S/s alternatives because the earlier layer and live initial remain uncertain. C’s convention-4 deleted/live notation already permits an overprint; the actual C revision is this set of identity/state alternatives, not zero-width layout.',
      scope_note='Only the first worked initial; C’s alleged separate terminal s is D65.')
amend(34, reading=HEADLESS, kind='drawing or diagram',
      decision='Draw the literal horizontal and very short raised right tick. Do not assign an arrowhead or a new mathematical meaning.')
amend(37, reading=C_POINTER, h=H_NOTES[0], h_excerpt_type='Exact H editorial note, scoped only to its downward-pointer claim.',
      scope_note='Distinct pointer only; the circled c is D67.')
amend(38, decision='No detached comma follows the final G prime in root’s R3/11 view; preserve the line end without it.')
amend(39, decision='No detached comma follows the final F prime. Removal of C’s separate s is D65.')
amend(40, reading=SYM, scan_shows='The word continues through trique and en precedes the two signs. Its first e has no independently secure acute; the crossing C6 rule is not a cancellation.',
      decision='Keep sym e/é trique and the separate lower sur-note; H’s merged marginal block supplies no extra joining words.')
amend(41, reading=FIRST_DIAGRAM,
      scope_note='First relation layout, sign directions and H’s inline separator/closing punctuation only; qualifier and alphabet are D42.')
amend(42, reading=r'de $\mathcal F$', change_c=True, confidence='medium',
      scan_shows='One d loop is followed by a low e-like ending, without distinct ans or final s; the family F is looped.',
      decision='Resolve the qualifier to de and retain the calligraphic family F.')
amend(43, reading=POINTS, location='C6, two detached diagonal points left of the first diagram',
      scan_shows='Two tiny detached points descend diagonally to the right, just left of F prime.',
      scope_note='The two-point group only; the separate point by the symmetry note is D66.')
amend(44, reading=LEFT_RULE, h=H_NOTES[1],
      h_excerpt_type='Exact H editorial note, scoped only to the long left C6 rule.',
      scan_shows='Root a03 frames the long nearly straight border, its lower bend and its crossing of the oblique note.',
      decision='Draw the complete rule without treating its crossing as cancellation of the symmetry note.')
amend(45, location='C6 part a, circled label', reading=r'\textcircled{a}',
      scan_shows='The a is enclosed by a circle. H prints (a) and describes the circle in its editorial note.',
      scope_note='Circled a only; circled c is D67 and raised circled b is D49.')
amend(46, reading=r'H\in\mathcal F', decision='Retain the literal H; the lower-left square node is G prime. Do not harmonize the two positions.')
amend(47, reading=r'\unsure{avec|ou}', change_c=False,
      scan_shows='The final word has three low separated runs, favouring avec but not excluding ou; no colon is visible.',
      decision='Retain avec/ou with avec first, and omit H’s unsupported colon.')
amend(48, reading=SECOND_DIAGRAM,
      scan_shows='Root a02 and overlapping R1/15 together cover the square: F prime/F above G prime/G, bowed horizontal signs, and downward-facing straight signs with right-hand detached bars.',
      decision='Preserve the literal square. a02 alone clips its bottom; R1/15 supplies the lower tails.',
      framing_limitation=E['a02']['root_framing_note'])
evidence(D[47], 'a02', ('r1_15',))
amend(49, reading=section(r'\node[anchor=west] at (7.05,-3.73)', r'\node[anchor=west] at (8.04,-3.73)'),
      scope_note='et before the raised circled b only; the following noun has its own row.')
amend(50, reading=FIRST_NOUN, decision='Retain str.tes/strates, with the dot-like medial form first; arêtes does not fit the initial strokes.')
amend(51, reading=SECOND_NOUN,
      scan_shows='The second noun’s worked initial can be cancelled S, live S or live s; its medial mark can be a or a dot. A secure earlier S layer is not established.',
      decision='Retain cancelled-or-live S/S/s initial alternatives instead of asserting a secure earlier S layer. C’s convention-4 deleted/live notation permits an overprint; the actual C revision is layer/state/case uncertainty and the narrowed word candidates, not macro spacing.')
amend(52, reading=TEL, change_c=False, change_h=True, confidence='low',
      scan_shows='The long horizontal through tel can be the t bar or a cancellation. The root view does not securely separate the two states.',
      decision='Retain C’s live/deleted tel alternatives; do not adopt R1’s unconditional live telles.')
amend(53, reading=GTAIL, change_c=True,
      decision='Keep n/m/bare-G alternatives, n first from the two low terminal ticks. Convention 6 makes changed first-candidate priority a C preference revision; no suffix is chosen from mathematical expectation.')
amend(54, reading=section(r'\node[anchor=west] at (7.28,-5.72)', r'\draw[line width=.5pt] (6.88,-3.67)'),
      h=r'« \ill{} complètement \ill{} »',
      h_excerpt_type='Exact quotation inside H’s editorial note; it is not additional manuscript prose.',
      scan_shows='Ce, complément and plus bas are readable; the mark over the e can be point, acute or unaccented return. servira is legible as the reduced verbal run.',
      decision='Resolve servira; retain the accent/dot/plain-e alternatives. Map both editorial placeholders to this one added continuation.')
amend(55, reading=B_RULES, h=H_NOTES[1],
      h_excerpt_type='Exact H editorial note, scoped only to the b-note double rule.',
      scope_note='Paired rules and their short lower crossings only; no labels are counted again.')
amend(56, reading='$' + BODY_G + "'$",
      decision='Keep G, F-under-G, and E alternatives in one first-body capital position. The later G prime is a separate clean G prime.')
amend(57, location='Final body, first subd abbreviation stop', c=r'\uline{subd}', h=r'\emph{subd.\ de $G$ induite}',
      reading=r'\uline{subd}', scope_note='First subd terminal stop only; second occurrence is D68. Underline extent is D58.')
amend(60, reading=FINAL_WORD, decision='Retain the final crossed sous-fig with its terminal-point uncertainty; the scan edge does not settle the point.')
amend(61, reading=macro(T, 'margin', T.index(r'\margin{sur la sous-figure')),
      scope_note='Placement of the lower sur-note alongside the final paragraph only; its worked capital is D62.')
amend(62, reading=LOWER_G, decision='Keep one F-under-G/G/E position in the lower margin, without treating it as part of the symmetry note.')

# All three readings are retained with exact report IDs. Grouped reports are
# narrowed below where their complete excerpt would otherwise be repeated.
R2MAP = [1,2,3,4,[5,6],7,8,9,10,11,12,13,14,15,15,16,17,17,18,18,18,19,None,20,20,21,21,22,[21,22],23,23,23,23,23,23,23,24,23,23,26,25,25,28,27,32,30,31,33,34,34,34,34,34,36,35,37,38,38,41,42,43,43]
R3MAP = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,18,19,21,22,23,None,24,25,27,27,26,[27,26],28,30,31,32,34,36,37,38,31,35,45,39,[40,41,42],43,44,46,47,[48,49],50,51,52,[53,54],55,56,57,58,None,59,60,63,64,45,None]
assert len(R2MAP) == len(R3MAP) == 62


def ids(reader, value):
    if value is None:
        return []
    return [f'D{n:02d}' for n in (value if isinstance(value, list) else [value])]


def readings(reader, value):
    return ' / '.join(DX[reader][i]['reading'] for i in ids(reader, value)) or 'No separate report row; see the complete reader text.'


for i, row in enumerate(D, 1):
    vals = {'R1': R['R1']['differences'][i-1]['reading'],
            'R2': readings('R2', R2MAP[i-1]), 'R3': readings('R3', R3MAP[i-1])}
    for n, mapping in (('R2', R2MAP[i-1]), ('R3', R3MAP[i-1])):
        row['reader_source_ids'][n] = ids(n, mapping)
    row['reader_readings'] = vals


def rr(number, **values):
    D[number-1]['reader_readings'].update(values)


rr(5, R2='D05 treats the bracketed H item after en forme as unsupported; D06 separately reads the raised pleine insertion.')
rr(14, R2=CAP)
rr(15, R1=r'\mathcal F\ ;\ \mathcal F', R2=r'\mathcal F\ ;\ \mathcal F')
rr(17, R2='Long arm drawn in a-insertion-leaders.', R3='Long arm drawn in fig-a-insertions.')
rr(18, R2='Separate short M-prime arm drawn.', R3='Separate short M-prime arm drawn.')
rr(19, R2=r'\unsure{\mathrel{\mapstochar\relbar}|\mapsto|\mathrel{\vdash\joinrel\dashv}}')
rr(20, R1=r"\mathcal F'\ ;\ \mathcal F", R2=r"\mathcal F'\ ;\ \mathcal F")
rr(21, R2=r'\overline F')
rr(23, R2='envisagées (no comma in the complete text)', R3='envisagées (no comma in the complete text)')
rr(24, R2=r"$M'$ de $M$")
rr(25, R2=r'\unsure{\}|?}')
rr(26, R2=r'\unsure{savoir|à savoir} :', R3=r'\unsure{à savoir|savoir} :')
rr(27, R2=r'si $X\in$', R3=r'si $X\in$')
rr(29, R2='Deletion and replacement are serialized before plus bas in the b paragraph.', R3='Deletion and replacement are serialized before plus bas in the b paragraph.')
rr(30, R2=r'\unsure{reporter|rajouter}')
rr(31, R2='fixé')
rr(32, R2="G" + CAP + "G'", R3="G" + CAP + "G'")
rr(33, R2=r'\unsure{\rlap{\deleted{F}}sous-fig.|Sous-fig.}')
rr(34, R2=r'\mathrel{\relbar\joinrel\relbar}')
rr(35, R2='commute')
rr(36, R2='i.e.')
rr(38, R2="G'$ (no comma)", R3="G'$, (comma retained)")
rr(39, R2="F'$ (no comma)", R3="F'$ (no comma)")
rr(40, R3=r'\unsure{symétrique|symetrique} en $\leq,\preceq$; lower sur-note is separate.')
rr(41, R2='F prime left of F; G below F; downward-facing straight order. Literal tikzcd.', R3='F prime left of F; G below F; downward-facing straight order. Literal tikzcd.')
rr(42, R2=r'\unsure{de|dans|ds} $\mathcal F$', R3=r'\unsure{de|dans|ds} $\mathcal F$; no terminal period.')
rr(43, R1='Two diagonal points left of first diagram, drawn.', R2='Two diagonal points, drawn.', R3='Two diagonal points, drawn after dedicated crop.')
rr(47, R3=r'\unsure{avec|ou}; no colon')
rr(48, R2='Literal F prime/F above G prime/G square with downward-facing straight orders.', R3='Literal F prime/F above G prime/G square with downward-facing straight orders.')
rr(49, R2=r'et \textcircled{b} les; b raised in diagram')
rr(50, R2=r'\unsure{strates|str.tes}')
rr(51, R2=r'\unsure{\deleted{s}|s}tr\unsure{a|.}tes')
rr(52, R2=r'\unsure{tel|\deleted{tel}}les')
rr(53, R2=r'\unsure{G_m|G_n|G}')
rr(56, R3=r"$G'$ (plain; no separate difference row)")
rr(61, R3=r'\margin{sur la sous-figure $G$ de $F$}; separate lower note')
rr(62, R2=r'\unsure{G|\mathcal G}', R3='G (plain)')


def add(location, c, h, reading, ev, shows, decision, rids, rvals,
        kind='other', change_c=True, change_h=True, marked='no', confidence='high', **extra):
    row = dict(id=f'072-D{len(D)+1:02d}', location=location, c=c, h=h, reading=reading,
               scan_shows=shows, decision=decision, confidence=confidence, kind=kind,
               marked_in_h=marked, change_c=change_c, change_h=change_h,
               math_consequential=False, reader_source_ids=rids, reader_readings=rvals)
    evidence(row, ev)
    row.update(extra)
    D.append(row)


add('a, plain M in the inserted intersection', C_INSERT, H_INSERT, T_INSERT, 'r3_07',
    'The intersection’s ambient M is a plain two-peaked capital.',
    'Retain plain M; do not use H’s calligraphic M.',
    {'R1':['D015'],'R2':['D15'],'R3':['D16']}, {n:'M' for n in R},
    kind='misread symbol or index', change_c=False,
    scope_note='This intersection M alone; both family letters and the mapping sign are elsewhere.')
add('a, the two plain M primes in the lower formula', C_LOWER, H_LOWER, T_LOWER, 'r3_08',
    'Both lower-formula ambient letters are plain M with separate primes.',
    'Retain the two plain M primes; family-F alphabets and the roof are separate scopes.',
    {'R1':['D020'],'R2':['D18'],'R3':['D20']}, {n:"M' ; M'" for n in R},
    kind='misread symbol or index', change_c=False,
    scope_note='Both ambient M-prime alphabet occurrences only.')
add('Marginal c, C’s alleged separate deleted s after final F prime', r'\deleted{\unsure{s}}', '',
    "No independent s after F′.", 'r3_11',
    'Root finds no independent s after the final F prime; the residual strokes belong to the earlier worked initial.',
    'Remove the spurious separate token while preserving the initial’s residual strokes at D33.',
    {'R1':['D033'],'R2':['D23'],'R3':['D33']},
    {n:'No separate s after final F prime; worked initial represented once.' for n in R},
    kind='text not on the page', change_h=False,
    reading_type='absence_disposition',
    reading_excerpt_type='Absence disposition; not a quotation of manuscript text.',
    final_absence_anchor=line_with(r"{sous-fig. de $F'$}"))
add('C6, detached point beside the symmetry note and left rule', '', '', POINT3, 'a03',
    'A separate small point stands by the crossing symmetry note and left rule.',
    'Preserve it independently of the two diagonal points at D43; assign no punctuation function.',
    {'R1':['D043'],'R2':['D29'],'R3':[]},
    {'R1':'Separate point drawn by symmetry rule.','R2':'Separate point drawn by symmetry rule.','R3':'Not separately drawn.'},
    kind='drawing or diagram')
add('Marginal c, circled label', r'\textcircled{c}', '(c)', r'\textcircled{c}', 'r3_11',
    'The c is enclosed by a circle before Pour.',
    'Retain the circle; H’s editorial note acknowledges it but its transcription uses parentheses.',
    {'R1':['D045'],'R2':['D23'],'R3':['D29']}, {n:r'\textcircled{c}' for n in R},
    kind='drawing or diagram', change_c=False, marked='yes')
add('Final body, second subd abbreviation stop', "par la subd $F'$", "par la subd. $F'$", "par la subd $F'$", 'r1_15',
    'No detached stop follows the second subd.',
    'Keep subd without a supplied point; the first occurrence is D57.',
    {'R1':['D057'],'R2':['D39'],'R3':['D61']}, {n:'subd' for n in R},
    kind='text not on the page', change_c=False)
add('Final body, marks after F before ou', ",", ",", PUNCT, 'r1_15',
    'A long oblique, hooked low loop and second low curve follow the plain F. The first stroke alone does not establish a prime.',
    'Retain plain F and the exact uncertain drawing adopted from R2; do not add R3’s possible prime to F.',
    {'R1':[],'R2':['D40'],'R3':['D62']},
    {'R1':"de $F$, ou",'R2':'Plain F followed by doubt-marked slant/loop and second low curve.',
     'R3':r"de $\unsure{F|F'}$, ou"}, kind='drawing or diagram', confidence='low',
    supporting_reader_text='R2 reading.tex: figure bottom-punctuation; adopted as a drawing only after root’s local crop comparison.',
    scope_note='The adjacent graphic group alone; the clean later G prime is reviewed separately without a counted change.')
assert len(D) == 69
for row in D:
    row['readers'] = '; '.join(n + ': ' + row['reader_readings'][n] for n in R)

# Literal C rows are source-exact; seven context-only rows complete all 23 rows.
CD = deepcopy(R['R3']['c_doubts'])
CD_D = [3,4,7,9,11,12,13,14,19,22,22,22,22,25,26,30,31,33,34,65,36,42,47,50,51,51,52,53,54,60]
CD_VALUE = [
 '=', 'en forme', CAPITAL, r'\preceq', VERB, 'quelc.', CORRESPOND, CAP, MAPPING,
 r'(\unsure{condition} stricte)', r'\deleted{\unsure{et}}', 'de',
 r'\unsure{(condition lge)|(condition large)}', MARK, r'\unsure{savoir|à savoir}',
 'reporter', r'\unsure{fixé|fixée}', INITIAL, HEADLESS, D[64]['reading'], 'i.e.',
 r'de $\mathcal F$', r'\unsure{avec|ou}', FIRST_NOUN,
 r'\unsure{\deleted{S}|S|s}', SECOND_NOUN, TEL, GTAIL, 'servira',
 r'\unsure{sous-fig|sous-fig.}']
CD_STATUS = ['resolved','resolved','revised','resolved','revised','resolved','resolved','resolved',
             'revised','revised','retained','resolved','retained','revised','revised','resolved',
             'retained','revised','resolved','revised','resolved','resolved','retained','revised',
             'revised','revised','retained','revised','resolved','revised']
for i, row in enumerate(CD[:30]):
    src = D[CD_D[i]-1]
    row.update(id=f'072-C{i+1:02d}', c=CU[i], reading=CD_VALUE[i], status=CD_STATUS[i],
               scan_shows=src['scan_shows'], difference_ids=[src['id']],
               decision=src['decision'],
               evidence_basis='Root decisions applied to the exact C occurrence; text-only assembly.')
    for k in ('crop','bbox','bbox_image','supporting_crops','supporting_evidence','reading_type','reading_excerpt_type','final_absence_anchor'):
        if k in src:
            row[k] = deepcopy(src[k])
    row.pop('source', None)
CD_EXTRA = [
 (r'\mathcal F', r'\mathcal F', 8, 'resolved', []),
 (C_DIAGRAMS[0], FIRST_DIAGRAM, 41, 'resolved', [SECOND_DIAGRAM]),
 ("G"+CAP+"G'", "G"+CAP+"G'", 32, 'resolved', []),
 (r"\overline F\subset M'", r"\overline F\subset M'", 21, 'resolved', []),
 (r"\inserted{$M'$} de $M$", r"\inserted{$M'$}", 16, 'resolved', [r'de $M$,']),
 (r'\textcircled{a}', r'\textcircled{a}', 45, 'resolved', [r'\textcircled{b}',r'\textcircled{c}']),
 (r'H\in\mathcal F', r'H\in\mathcal F', 46, 'resolved', [SECOND_DIAGRAM]),
]
for i, (c, value, di, status, additional) in enumerate(CD_EXTRA, 30):
    src=D[di-1]; row=CD[i]
    row.update(id=f'072-C{i+1:02d}', c=c, reading=value, status=status,
               scan_shows=src['scan_shows'], difference_ids=[src['id']],
               evidence_basis='Context-only coverage from root decisions; text-only assembly.')
    for k in ('crop','bbox','bbox_image'):
        row[k]=src[k]
    if additional:
        row['additional_readings']=additional
    row.pop('source', None)
CD[31]['supporting_crops']=[E['a02']['path'],E['r1_15']['path']]
CD[35]['supporting_crops']=[E['r3_11']['path'],E['r3_15']['path']]
CD[36]['supporting_crops']=[E['a02']['path'],E['r1_15']['path']]

RD = []

def remaining(di, reading, alternatives, reason):
    RD.append(dict(location=D[di-1]['location'], reading=reading, alternatives=alternatives,
                   confidence='low', reason=reason))

remaining(7,CAPITAL,['C over calligraphic F','plain calligraphic C','script C','double-stroked C'], 'One heavily worked position does not independently establish a complete prior glyph.')
remaining(10,TOUT,['tout',r'\deleted{tout}'],'The long crossing can be a t bar or cancellation.')
remaining(11,VERB,['satisfont','satisfait'],'The low oval and reduced following strokes do not establish the internal vowel group.')
remaining(19,MAPPING,[r'\mathrel{\mapstochar\relbar}',CAP,r'\mapsto'],'The left cap is clear; the short dark right endpoint remains ambiguous.')
remaining(22,r'\unsure{condition}',['condition, compressed written form'],'The first condition group is compressed; no expanded spelling is asserted.')
remaining(22,r'\deleted{\unsure{et}}',['et'],'Cancellation masks the tiny group.')
remaining(22,r'\unsure{(condition lge)|(condition large)}',['(condition lge)','(condition large)'],'The final group favours a contraction, but the letters remain crowded. Root a05 establishes the closing parenthesis.')
remaining(25,MARK,['curled brace-like mark with crossed head','question-like mark'],'The literal crossed curve is preserved without a forced character identity.')
remaining(26,r'\unsure{savoir|à savoir}',['savoir','à savoir'],'A separate initial à is not secure under the cancellation.')
remaining(31,r'\unsure{fixé|fixée}',['fixé','fixée'],'A possible final e merges with the preceding strokes.')
remaining(33,INITIAL,[r'\rlap{\deleted{F}}S','S','s'],'F/S-like strokes share one position; the lower residual strokes are retained separately.')
remaining(40,r'\unsure{e|é}',['e','é'],'A detached acute above the first e of symetrique is not independently secure.')
remaining(47,r'\unsure{avec|ou}',['avec','ou'],'Three reduced low runs favour avec but do not exclude ou.')
remaining(50,FIRST_NOUN,['str.tes','strates'],'A medial dot-like mark may be a contraction or a reduced letter.')
remaining(51,SECOND_NOUN,['deleted S/S/s followed by trates','deleted S/S/s followed by tr.tes'],'Initial state/case and medial a/dot remain open within one word position.')
remaining(52,TEL,['telles',r'\deleted{tel}les'],'The long horizontal may be the t bar or a cancellation.')
remaining(53,GTAIL,['G_n','G_m','G'],'Two low terminal ticks can be a small suffix or part of a worked G.')
remaining(54,r'\unsure{\.{e}|é|e}',[r'\.{e}','é','e'],'The elevated mark can be a point, an acute or a connected return.')
remaining(56,BODY_G,['G','F-under-G','E'],'A looped exterior and internal straight bars occupy one capital position.')
remaining(69,PUNCT,['oblique stroke, low loop and low curve; identities unassigned'],'The joined punctuation shapes are preserved; the oblique alone does not establish a prime.')
remaining(60,r'\unsure{sous-fig|sous-fig.}',['sous-fig','sous-fig.'],'The cancellation and scan edge prevent a secure terminal-stop decision.')
remaining(62,LOWER_G,['F-under-G','G','E'],'The lower marginal capital has F-like internal bars within a G-like outer loop.')

# Preserve genuine reader disagreements, candidate order/certainty disagreements,
# and root corrections of all-reader regularization. Full returns stay unchanged.
DISPUTES = []
for di in [5,7,10,11,19,22,23,25,26,30,31,33,34,37,38,40,42,47,50,51,52,53,54,55,56,60,62,66,69]:
    row=D[di-1]
    DISPUTES.append(dict(location=row['location'],
        r1=row['reader_readings']['R1'],r2=row['reader_readings']['R2'],r3=row['reader_readings']['R3'],
        final=row['reading'],evidence=row['decision']+' '+row['scan_shows']+' ['+row['crop']+']',
        difference_id=row['id'],reader_source_ids=deepcopy(row['reader_source_ids'])))

# Inventory preserves one entry per element in original top-to-bottom position.
INV = deepcopy(R['R1']['inventory'])
INV[27]['first_words_or_objects']='F′ preceq F, G beneath F; de and looped family F at right'
INV[37]['first_words_or_objects']='Ce compl[e-dot/é/e]ment servira plus bas'
INV.insert(38,dict(element='Possible cancellation of tel',kind='deletion',position='right b note, before les que',
                  first_words_or_objects='tel live/deleted alternatives',sheet_kind='text',hand='his hand',transcribed='yes'))
INV.insert(42,dict(element='Uncertain graphic group after bottom F',kind='drawing',position='second final body line, between F and ou',
                  first_words_or_objects='long oblique, low loop and second low curve',sheet_kind='text',hand='his hand',transcribed='yes'))
# The tel state belongs before the paired rule/lower continuation in the same note.
by_element={x['element']:x for x in INV}
order=[x['element'] for x in INV]
order.remove('Possible cancellation of tel')
order.insert(order.index('b double rule'),'Possible cancellation of tel')
# Within a shared line/block, preserve raised-before-baseline and left-to-right order.
order.remove('Replacement b clause')
order.insert(order.index('Superseded b clause'),'Replacement b clause')
order.remove('Uncertain graphic group after bottom F')
order.insert(order.index('Final cancelled word'),'Uncertain graphic group after bottom F')
INV=[by_element[x] for x in order]
for row in INV:
    row['position']='Original scan orientation: '+row['position']
    if row['element']=='Bottom slanted note':
        row['position']='Original scan orientation: lower left, alongside the foot paragraph; separate from the earlier symmetry note'
    if row['element']=='Worked bottom-margin capital':
        row['position']='Original scan orientation: in the lower-left sur-note alongside the foot paragraph, after sous-figure'
assert len(INV)==45 and len({x['element'] for x in INV})==45

REVIEWS = [
 dict(reference='H raised bracketed placeholder',claim=r'la définition en forme [\ill{}]',
      decision='Map the bracketed placeholder once to raised [pleine] at the definition. R2’s separate missing-word interpretation is rejected without creating another omission.',
      evidence='Root’s pleine crop shows its raised placement, brackets, underline and connector.',crop=E['r3_03']['path']),
 dict(reference='H first editorial note',claim=H_NOTES[0],
      decision='The replacement reads qu’on va formuler; qui ne and an unread third word remain H’s editorial guesses. Circled c and its downward pointer are retained as graphics.',
      evidence='Replacement and c note are separately framed by R3/10 and R3/11.',crop=E['r3_10']['path'],supporting_crops=[E['r3_11']['path']]),
 dict(reference='H second editorial note',claim=H_NOTES[1],
      decision='Keep literal H in prose and G prime in the square, circled labels and drawn rules. The quoted complètement is aligned to the one Ce complément servira plus bas continuation; its two placeholders are editorial observations.',
      evidence='Root’s square, overlapping tail crop and right-note view preserve the separate scopes.',crop=E['r3_15']['path'],supporting_crops=[E['a02']['path'],E['r1_15']['path']]),
 dict(reference='H merged marginal block',claim=macro(H,'marginal',H.index(H_NOTES[1])+len(H_NOTES[1])),
      decision='Separate the symmetry note beside C6 from the lower sur-note alongside the final paragraph. Do not invent words for the three placeholder positions.',
      evidence='Separate local rotated crops frame the two notes.',crop=E['r3_13']['path'],supporting_crops=[E['r3_17']['path']]),
 dict(reference='H bowed-order encoding',claim=r'\preccurlyeq',
      decision='Treat H preccurlyeq and final preceq as the same bowed glyph; C’s straight/sloping alternative is resolved locally.',
      evidence='The first tuple order is straight; the second has a bowed lower stroke.',crop=E['r3_04']['path']),
 dict(reference='C_context first-capital comparisons to other scans',claim='The C in the same triple on 66 has a smooth open interior.',
      decision='No other manuscript page was consulted. Retain the local worked-position alternatives from scan072.',
      evidence='Only the root-viewed local tuple crop supports this record.',crop=E['r3_04']['path']),
 dict(reference='Bottom second G prime, provisional root suspicion',claim='The initial provisional crop note grouped the first and second bottom G-prime-like capitals as worked.',
      decision='Final root comparison retains the later G prime clean: its internal bar is an ordinary G crossbar. The first body capital and lower-margin capital retain separate uncertainties.',
      evidence='The existing R1/15 overlap supplies the final-body comparison; no extra glyph or change row is invented.',crop=E['r1_15']['path']),
 dict(reference='Square framing limitation',claim=E['a02']['root_framing_note'],
      decision='Cite a02 together with the existing overlapping R1/15. Do not describe a02 alone as complete and do not make another crop.',
      evidence='Source boxes overlap at y2205–2215 and R1/15 continues through the lower tails.',crop=E['a02']['path'],supporting_crops=[E['r1_15']['path']]),
]

NOTATION = [
 dict(sign='literal repetition marks',latex='= =',appearance='Two adjacent pairs of unequal horizontal strokes.',location='After quand',alternatives=[]),
 dict(sign='worked definition capital',latex=CAPITAL,appearance='Outer C-like loop and internal F-like stem/bar share one position.',location='Before tuple equals',alternatives=['C over F','calligraphic C','script C','double-stroked C']),
 dict(sign='family capital',latex=r'\mathcal F',appearance='Looped upper head and curved stem.',location='Tuple, mappings, qualifier and H membership',alternatives=[]),
 dict(sign='ambient and subset capital',latex="M, M'",appearance='Plain two-peaked M; independent prime where present.',location='Condition a and b',alternatives=[]),
 dict(sign='straight and bowed orders',latex=r'\leq;\preceq',appearance='First straight, second bowed; vertical straight orders point down with detached bar on right.',location='Tuple and C6 diagrams',alternatives=[]),
 dict(sign='two-capped mapping-like links',latex=CAP,appearance='Horizontal with an upright cap at each end, without an open arrowhead.',location='Raised family mapping and marginal G mapping',alternatives=[]),
 dict(sign='uncertain lower mapping',latex=MAPPING,appearance='Clear left cap, dark short right endpoint.',location='After lower M prime',alternatives=[r'\mathrel{\mapstochar\relbar}',CAP,r'\mapsto']),
 dict(sign='barred plain F',latex=r"\overline F\subset M'",appearance='Detached roof over the individual F, followed by subset sign.',location='Set condition in a',alternatives=[]),
 dict(sign='literal sous-figure connector',latex=HEADLESS,appearance='Horizontal stroke with a short raised right tick.',location='Marginal c',alternatives=['Function unassigned']),
 dict(sign='circled labels',latex=r'\textcircled{a};\textcircled{b};\textcircled{c}',appearance='Circles, with b raised after et.',location='C6 and its marginal continuation',alternatives=[]),
 dict(sign='H and lower-left G prime',latex=r"H;G'",appearance='H has two uprights; G prime is a rounded G with prime.',location='Existence sentence and square node',alternatives=[]),
 dict(sign='double angle and terminal G',latex=r"X'\ll"+GTAIL,appearance='Two left-pointing angles; G ends in two low ticks.',location='Right b note',alternatives=['G_n','G_m','G']),
 dict(sign='detached points',latex=POINTS+'\n'+POINT3,appearance='Two diagonal points and one independent point beside the symmetry rule.',location='C6',alternatives=['No linguistic function assigned']),
 dict(sign='bottom worked capitals',latex=BODY_G+'; '+LOWER_G,appearance='Outer loop and inner straight bars share one position in each local occurrence.',location='First final-body G prime and lower sur-note',alternatives=['G','F-under-G','E']),
 dict(sign='bottom punctuation group',latex=PUNCT,appearance='Long oblique, low hooked loop, second low curve.',location='After final F, before ou',alternatives=['Identity unassigned; no added F prime']),
]
ABBREVIATIONS = [
 dict(form='sous-ens.',expansion='sous-ensemble'),dict(form='sup / Sup',expansion='supremum'),
 dict(form='quelc.',expansion='quelconques'),dict(form='subd. / subd',expansion='subdivision'),
 dict(form='sous-fig. / sous-fig',expansion='sous-figure'),dict(form='i.e.',expansion='id est'),
 dict(form='str.tes (uncertain)',expansion='strates; retained without expansion in the transcription'),
 dict(form='lge (uncertain)',expansion='large; retained as a candidate contraction'),
 dict(form='condition (compressed and uncertain)',expansion='No additional expansion asserted'),
]

H_SCOPES = [
 r'les axiomes \ill{} passent',r'la définition en forme [\ill{}]',
 r'\ill{} plus bas)',r'\struck{\ill{} si $X \in F$}',
 r'\marginal{il faudra \ill{} des \ill{} (\ill{})}',
 r'\marginal{il faudra \ill{} des \ill{} (\ill{})}',
 r'\marginal{il faudra \ill{} des \ill{} (\ill{})}',
 r'\ill{} aux Sup',r'\ill{} :',
 r'« \ill{} complètement \ill{} »',r'« \ill{} complètement \ill{} »',
 r'\ill{} symétrie \ill{} $\leq$, $\preccurlyeq$ \ill{}',
 r'\ill{} symétrie \ill{} $\leq$, $\preccurlyeq$ \ill{}',
 r'\ill{} symétrie \ill{} $\leq$, $\preccurlyeq$ \ill{}',r'\ill{} que']
H_MAP=[2,5,28,26,22,22,22,35,47,54,54,40,40,40,59]
H_SCOPE_NOTES=[
 'Opening predicate, including H passent; one complete clause comparison.',
 'One raised bracketed pleine insertion; H’s preceding-paragraph placement does not create a second item.',
 'Raised replacement qu’on va formuler, above the b deletion.',
 'First part of the struck clause; its final F and placement are separate D27/D29 scopes.',
 'First of three placeholders in one compressed marginal-question block.',
 'Second of three placeholders in the same block; no second whole omission.',
 'Third of three placeholders in the same block; terminal parenthesis established by a05.',
 'The verb commute only.',
 'Final word avec/ou; the explicit H colon is outside the placeholder but in the same compared line end.',
 'First editorial-note placeholder in the partial quotation of the lower continuation, not a manuscript token.',
 'Second editorial-note placeholder in the same quotation; no second added sentence.',
 'First placeholder in the symmetry part of H’s combined marginal block; no invented prefix.',
 'Middle placeholder in the symmetry phrase; final en is read locally.',
 'Transition between symmetry and lower sur-note. No manuscript joining word is supplied; the lower note placement is D61.',
 'Conjunction ou before que.']
H_ALIGNMENT=[dict(ordinal=i,source=source,difference_id=D[di-1]['id'],
                  disposition=D[di-1]['reading'],scope=scope)
             for i,(source,di,scope) in enumerate(zip(H_SCOPES,H_MAP,H_SCOPE_NOTES),1)]

WORKFLOW=(
 'Three complete independent v08 reader returns are preserved unchanged. Root viewed no whole page or supplied half. '
 'Root viewed 20 distinct existing reader crops: R3 01–17 and R1 05,11,15; root made and viewed five crops a01–a05. '
 'R3/07’s initially truncated display was retried from the identical file and is counted once. '
 'a02 clips the square’s bottom and is paired with the already existing R1/15 overlap; no replacement crop was made. '
 'a05 covers only the missing terminal part of the oblique question. '
 'R1/05 settled neither tout state nor the inner verb letters; both alternatives remain. '
 'This administrative builder read text and metadata only. It opened no images, ran no OCR/compiler/research/proof check, '
 'and did not finalize or rebuild shared deliverables.')

DECISION=dict(
 key=KEY,cote='156-4',scan=72,folder=META['folder'],their_page=META['their_page'],filename=FILENAME,
 brief_version='v08',review_status='draft — awaiting root review',record_builder='scripts/decide_072_records.py',
 record_basis='Root’s explicit final choices, exact finalized page and all three preserved complete reader returns.',
 final_text_sha256=hashlib.sha256(T.encode()).hexdigest(),differences=D,c_doubts=CD,disputes=DISPUTES,
 remaining_doubts=RD,h_placeholder_alignment=H_ALIGNMENT,inventory=INV,notation=NOTATION,
 abbreviations=ABBREVIATIONS,witness_reviews=REVIEWS,check_events=[],
 reader_crop_counts={n:len(R[n]['crops']) for n in R},
 reader_report_counts={n:{k:len(R[n][k]) for k in ('differences','c_doubts','remaining_doubts','inventory')} for n in R},
 adjudicator_crop_count=5,adjudicator_existing_crop_views=20,adjudicator_successful_crop_views=25,
 root_viewed_crops=[E[k] for k in sorted(E)],workflow_note=WORKFLOW,
 administrative_audit='decisions/156-4_072_record_audit.md',
 context_source_rows=[dict(row=i,source=s) for i,s in enumerate(CONTEXT_LINES,1)],
 notes=dict(
  summary='Folio 71 introduces a full sub-contrée by two closure conditions. A slanted question leaves arbitrary versus finite suprema open. The marginal c assertion and C6 use two relation diagrams, corrections, added phrases and graphic marks. The final paragraph describes an induced subdivision and breaks off at a cancelled sous-fig; a separate lower note says sur la sous-figure G-like de F. These are transcribed manuscript statements, not established mathematical results.',
  math_reading_decisions=[
   'Straight versus bowed orders, cap terminals versus arrowheads, the roof over F, plain versus looped capitals, primes and G suffixes were decided or retained from local ink only.',
   'Literal H in the existence sentence and G prime in the square are both retained. No mathematical consistency repair was made.',
   'The last body F remains plain and is followed by an uncertain literal punctuation drawing; R3’s possible prime is not separately asserted.',
   'No proposition was proved, calculated, used as a validated result or refuted. check_events is empty.'],
  author_checks=[
   "Opening caution in the author’s own words: « il faut faire attention si les axiomes vont passer aux sous-contrées ».",
   "Slanted question in the author’s own words: « Je ne sais s'il faut prendre des sup quelconques … ou bien de sup finis seulement ». The ellipsis here omits the intervening parenthetical and crossed group, which are transcribed in full in the page.",
   'Ce complément servira plus bas is a forward-looking annotation, not an explicit completed check.',
   'No proof-check event occurred in this run.'],
  local_doubts=[
   'In the slanted question, the first condition group and crossed et remain doubtful; stricte and de are resolved. The final lge/large alternatives remain, while a05 confirms the closing parenthesis.',
   'Elsewhere, the worked capitals, tout state, satisfont/satisfait, lower mapping endpoint, crossed-clause initial, fixé/fixée, c initial, symmetry accent, avec/ou, strates-like forms, tel state, G suffix, complément accent and final sous-fig stop retain the local alternatives recorded in remaining_doubts.',
   'The marks after the last body F remain a literal uncertain drawing. The later body G prime is clean, while the first body capital and lower-margin capital retain separate worked alternatives.'],
  title_dates_pagination='Scan 72, running folio 71. Définition 1 and C6 are local underlined headings. No title, date or total page count is recorded.'),
)


def validate_records():
    kinds={'misread word','misread symbol or index','omission','text not on the page',
           'deletion state (struck given live or live given struck)','insertion or placement',
           'abbreviation expanded or spelling modernised',r'readable ink left as \ill{}',
           'drawing or diagram','other'}
    allowed={e['path'] for e in E.values()}
    assert len(D)==len({x['id'] for x in D})==69
    for row in D:
        assert row['kind'] in kinds,row['id']
        assert row['confidence'] in {'high','medium','low'},row['id']
        assert row['marked_in_h'] in {'yes','no'},row['id']
        assert all(type(row[k]) is bool for k in ('change_c','change_h','math_consequential')),row['id']
        assert row['crop'] in allowed,row['id']
        for k,source in (('c',C),('h',H)):
            assert not row[k] or row[k] in source,(row['id'],k,row[k])
        if row.get('reading_type')=='absence_disposition':
            assert row['id']=='072-D65' and row['final_absence_anchor'] in T
        else:
            assert row['reading'] in T,(row['id'],'reading',row['reading'])
        assert set(row['reader_readings'])==set(R),row['id']
        for n,source_ids in row['reader_source_ids'].items():
            assert all(i in DX[n] for i in source_ids),(row['id'],n,source_ids)
        for value in row.get('additional_readings',[]):
            assert value in T,(row['id'],'additional',value)
        assert all(p in allowed for p in row.get('supporting_crops',[])),row['id']
    assert [r['c'] for r in CD[:30]]==CU
    assert len(CD)==37
    assert {v for row in CD for v in row.get('context_rows',[])}==set(range(1,24))
    for row in CD:
        assert row['c'] in C,(row['id'],'source',row['c'])
        if row.get('reading_type')=='absence_disposition':
            assert row['id']=='072-C20' and row['final_absence_anchor'] in T
        else:
            assert row['reading'] in T,(row['id'],'reading',row['reading'])
        assert row['status'] in {'resolved','retained','revised'}
        assert row['crop'] in allowed
        for value in row.get('additional_readings',[]):
            assert value in T,(row['id'],'additional',value)
    for row in RD:
        assert row['reading'] in T,row['location']
    assert len(H_ALIGNMENT)==15
    assert [x['ordinal'] for x in H_ALIGNMENT]==list(range(1,16))
    for row in H_ALIGNMENT:
        assert row['source'] in H,row['ordinal']
        assert row['disposition'] in T,row['ordinal']
    assert len(INV)==len({x['element'] for x in INV})==45
    for row in INV:
        assert row['kind'] in {'text','display','diagram','drawing','margin note','insertion','deletion'}
        assert row['sheet_kind']=='text'
        assert row['transcribed']=='yes'
    assert all(R[n]['finished_utc'] for n in R)
    assert DECISION['reader_crop_counts']=={'R1':17,'R2':18,'R3':18}
    for n in R:
        covered={i for row in D for i in row['reader_source_ids'].get(n,[])}
        assert covered==set(DX[n]),('unmapped reader rows',n,set(DX[n])-covered)
    for value in macros(T,'unsure'):
        assert any(value in row['reading'] or row['reading'] in value for row in RD),('uncovered final doubt',value)
    assert DECISION['check_events']==[]
    return dict(differences=len(D),changes_C=sum(x['change_c'] for x in D),
                changes_H=sum(x['change_h'] for x in D),c_doubts=len(CD),context_rows=23,
                c_unsure_occurrences=30,h_ill_placeholders=15,disputes=len(DISPUTES),
                remaining_doubts=len(RD),inventory=len(INV),root_existing_crop_views=20,
                root_new_crops=5,check_events=0,final_unsure_occurrences=len(macros(T,'unsure')),
                reader_difference_rows_covered={n:len(DX[n]) for n in R})


if __name__=='__main__':
    DECISION['administrative_validation']=validate_records()
    output=O/'decisions'/(KEY+'.json')
    output.write_text(json.dumps(DECISION,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(output=str(output),**DECISION['administrative_validation']),ensure_ascii=False))
