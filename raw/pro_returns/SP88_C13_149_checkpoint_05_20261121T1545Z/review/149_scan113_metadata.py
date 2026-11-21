import json
from pathlib import Path

ROOT = Path('/workspace/scratch/0cab6a548abb')
PAGE = '149_scan113'
BOXES = {
    'p01': [770, 29, 847, 87], 'p02': [295, 93, 950, 185],
    'p03': [980, 55, 1569, 195], 'p04': [290, 196, 1652, 329],
    'p05': [281, 331, 1543, 446], 'p06': [289, 473, 737, 539],
    'p07': [267, 535, 1140, 901], 'p08': [244, 947, 609, 1041],
    'p09': [735, 921, 1575, 1060], 'p10': [252, 1041, 1642, 1193],
    'p11': [260, 1183, 1609, 1325], 'p12': [247, 1483, 1615, 1755],
    'p13': [255, 1744, 1615, 1909], 'p14': [250, 2012, 1397, 2152],
    'p15': [257, 2146, 1598, 2290], 'p16': [21, 2304, 105, 2352],
}


def crop(place):
    return f'crops/{PAGE}_{place}.png'


def change(place, location, c, h, final, evidence, confidence, vs_c, vs_h,
           kind, category, h_marked=False, consequential=False):
    return dict(id=place, place=location, C=c, H=h, final=final,
                evidence=evidence, crop=crop(place), bbox=BOXES[place],
                confidence=confidence, vs_C=vs_c, vs_H=vs_h, kind=kind,
                error_category=category, H_marked=h_marked,
                consequential=consequential)


POINT = r'\unsure{\zeta|\xi}'
FORMULA = r'''\begin{aligned}
(20)\quad &\mathcal E_{X/Y}^{\unsure{\zeta|\xi}_T}\simeq\mathcal E_{X/Y}^T\\[0.5ex]
&\quad\rotatebox{90}{$\simeq$}\\[0.5ex]
&\Pi_1(X_{\unsure{\zeta|\xi}_Y},\unsure{\zeta|\xi}_T)
\end{aligned}'''
MIDDLE = r'''\deleted{\unsure{donc}} --- les $\Pi_1(X_{\unsure{\zeta|\xi}_Y},\unsure{\zeta|\xi}_T)$ des fibres géom, relatifs aux divers pts géom de $\mathcal E_{X/Y}^T$, sont canoniquement iso entre eux.'''
LOWER_START = r'''( Il faut bien faire attention que $\mathcal E_{X/Y}$ \inserted{($Z$ non précisé)} est une classe d'iso.'''
LAST = r'''$\mathcal E_{X/Y}^T$ et $\mathcal E_{X/Y}^{T'}$ provient du choix'''

CHANGES = [
    change('p02', 'First main line, before the correction',
           'Le lien avec la', r'La \ill{} \ill{}', 'Le lien avec la',
           'The capital L is followed by a low e, not an a. The next word has a tall l, an i stroke with its dot and low joined en; the following separated low strokes read avec. The final la is independently visible before the cancelled word.',
           'high', False, True, 'readable ink left as \\ill{}',
           'Readable ink left as illegible', True),
    change('p03', 'First-line cancellation and its supralinear replacement, before (11)',
           r'\deleted{définition}\inserted{description} (11)',
           r'\struck{définition} \add{\uncertain{les conventions}} (11)',
           r'\deleted{\unsure{definition|définition}}\inserted{description} (11)',
           'The upper replacement is one word, description: its opening d/e/s, following c/r/i, descending p, tall t and short ending are separable. There are no preceding les strokes. Below, one horizontal strike passes through the original word. Initial d, a long f descender and the later t rise support definition, but several small letters coincide with the strike. No detached accent over its e is securely visible; the unaccented reading is preferred only provisionally, with the accented alternative and word-level uncertainty retained. The reference is clearly (11).',
           'low', True, True, 'misread word', 'Words', True),
    change('p04', 'Second main line, opening phrase',
           'est évidemment que, si', 'et décidons que, si',
           'est évidemment que, si',
           'The short first word ends with the writer’s raised t turn. The next word shows the initial accented e, v/i sequence, tall d and extended low middle followed by the final t turn of évidemment. It has more written material than décidons. The full line, including the geometric-point expression, was inspected.',
           'high', False, True, 'misread word', 'Words'),
    change('p05', 'Third main line, point abbreviation and following géom',
           r'$p^t$ géom', 'pt géom.', r'$\unsure{p^t|pt}$ géom',
           'The p has a long descender and the adjacent t rises above the bowl. Its lower return is nearly level with that bowl, so a genuinely raised t versus ordinary pt is not securely distinguished. The first p^t reading is retained with this new positional doubt, not counted as a correction against C. There is no terminal abbreviation stop after géom. The whole line and its following geometric-point formula were inspected.',
           'medium', False, True, 'other', 'Other'),
    change('p06', 'Fourth main line, immediately above (20)',
           'des iso can', 'des isos canon.', 'des iso can',
           'After des the short form ends in a rounded o; no final s follows it. The next word has c, a small a and a long n ending, with neither on nor a terminal full stop. Both short forms stand without stops.',
           'high', False, True, 'abbreviation expanded or spelling modernised',
           'Abbreviations expanded, spelling modernised'),
    change('p07', 'Complete three-row display (20)',
           r'''\mathcal E_{X/Y}^{\unsure{\xi|\zeta}_T}\simeq\mathcal E_{X/Y}^T; \rotatebox{90}{$\simeq$}; \pi_1(X_{\unsure{\xi|\zeta}_Y},\unsure{\xi|\zeta}_T)''',
           r'''\mathcal{E}^{\xi_T}_{X/Y}\simeq\mathcal{E}^{T}_{X/Y}; \wr; \pi_1\bigl(X_{\xi_Y},\xi_T\bigr)''',
           FORMULA,
           'The lower leading glyph has a flat cap spanning two posts, supporting capital Pi. The vertical relation between the upper-left E term and the lower expression consists of a wavy left member and a distinct straight right member: a rotated simeq, not the wavy member alone. The upper horizontal relation is a wave over one straight bar. Both relative subscripts read X/Y, the upper-right exponent is T, and the lower parenthesis contains X with the point/Y subscript, a comma and the point/T argument. All three point-letter identities remain unresolved. Reordering their alternatives is not counted as a correction against C.',
           'high', True, True, 'misread symbol or index',
           'Symbols and indices', False, True),
    change('p08', 'Cancelled word before the dash introducing the fibre-group sentence',
           r'\deleted{\unsure{donc}} --- les',
           r'\struck{\ill{}} --- les', r'\deleted{\unsure{donc}} --- les',
           'A looped initial ascender and a low rounded return survive below the horizontal cancellation. The remaining small humps are crossed heavily. They support donc as a tentative reading only; the n/c sequence is not independently plain. The following dash and les are live and separate from the cancellation.',
           'low', False, True, 'readable ink left as \\ill{}',
           'Readable ink left as illegible', True),
    change('p09', 'Complete inline fibre-group formula after the dash',
           r'\pi_1(X_{\unsure{\xi|\zeta}_Y},\unsure{\xi|\zeta}_T)',
           r'\pi_1(X_{\xi_Y},\xi_T)',
           r'\Pi_1(X_{\unsure{\zeta|\xi}_Y},\unsure{\zeta|\xi}_T)',
           'The leading symbol has a flat cap and a straight left post. Its right post curves at the bottom, unlike the straighter post in (20), but the cap and separated posts support the same capital Pi form. The small 1 is below it. The complete parenthesis shows X, the point/Y subscript, a comma and the point/T argument. The two point glyphs remain ambiguous; the alternative ordering alone is not a C correction.',
           'high', True, True, 'misread symbol or index',
           'Symbols and indices', False, True),
    change('p10', 'Line beginning géom below the inline formula',
           'géom, relatifs aux divers pts géom',
           'géom., relatifs aux divers pts géom.',
           'géom, relatifs aux divers pts géom',
           'The first géom ends in its m return and is followed by a comma; no extra dot precedes the comma. The last géom ends at its final low return with no following full stop. The intervening words relatifs aux divers pts are continuous and readable.',
           'high', False, True, 'other', 'Other'),
    change('p11', 'End of the line beginning de E: short form after canoniquement',
           'iso', 'isom.', 'iso',
           'The final word has a dotted i, the curved s and a small terminal o. There is no following m or stop. The complete line reads de E^T_{X/Y}, sont canoniquement iso; the source really places the relative E expression after de.',
           'high', False, True, 'abbreviation expanded or spelling modernised',
           'Abbreviations expanded, spelling modernised'),
    change('p12', 'Opening two lines of the lower parenthesis and the inserted qualification',
           LOWER_START,
           r'''(Il faut bien faire attention (\uncertain{$Z$ non précisé}) que $\mathcal{E}_{X/Y}$ \uncertain{n'est} une classe d'isom.''',
           LOWER_START,
           'The insertion reads (Z non précisé), with a clear Z rather than T. A separate long leader runs from its right side to the gap immediately after E_{X/Y}, before est. The large descending curve that crosses part of précisé belongs to the f of faire above, not to a deletion of the insertion. After the leader there is the compact est; no n-apostrophe precedes it. The last short form is d’iso. with a visible terminal dot and no m.',
           'high', False, True, 'insertion or placement',
           'Insertions put in the wrong place', True, True),
    change('p13', 'Following line ending sans plus, pas',
           r'sans plus, \uline{pas}', r'\uncertain{sans} plus, \ill{}',
           r'sans plus, \uline{pas}',
           'The last word has a clear p loop and descender followed by a and s. A separate horizontal underline lies beneath its latter part. The preceding sans plus and comma are visible; the long f descender in profinis is not a strike.',
           'high', False, True, 'readable ink left as \\ill{}',
           'Readable ink left as illegible', True, True),
    change('p14', 'Penultimate main line, following L’arbitraire',
           "dans le choix d'un iso entre",
           r"de la donnée d'un \uncertain{isom.} entre",
           "dans le choix d'un iso entre",
           'The first word has the d loop and a compressed low continuation read as dans; the next is le. The following word has the opening ch, rounded o, dotted i and final crossed x of choix, not donnée. After d’un the short form ends at o, without an m or a stop. Entre follows on the same baseline.',
           'high', False, True, 'misread word', 'Words', True),
    change('p15', 'Last main line, after the two indexed E expressions',
           'provient du choix', 'provient des choix', 'provient du choix',
           'After provient the word has a looped d and one joined u-shaped return before the final horizontal exit. There is no separate terminal s. Both E expressions were read in the same crop: they have X/Y below and T, then T-prime, above. The sentence ends here without added punctuation or a closing parenthesis.',
           'high', False, True, 'misread word', 'Words'),
    change('p16', 'Lower-left foliation', r'\margin{112}', '[absent]',
           r'\margin{112}',
           'The thin lower-left foliation reads 112: two upright 1s with oblique entries, followed by a curved 2 with a broad lower return. It is separate from the authorial 56 at the head.',
           'high', False, True, 'omission', 'Omissions'),
]

POINT_PLACES = [
    ('M0063', 'Second main line, geometric point with subscript X', 'p04', r'\unsure{\zeta|\xi}_X',
     'A small upper curl leads into a long descending stroke; there is no reliably separable middle lobe that settles xi against zeta.'),
    ('M0064', 'Third main line, geometric point with subscript T', 'p05', r'\unsure{\zeta|\xi}_T',
     'The sign has a small hooked head and a long curved descent ending in a diagonal return beside the T; the compressed head does not settle the Greek-letter identity.'),
    ('M0065', 'Display (20), point/T exponent on the upper-left E', 'p07', r'\unsure{\zeta|\xi}_T',
     'This upper point glyph has more upper lobing than the running-text occurrences, then a long stem. Both xi and zeta remain compatible with this local hand.'),
    ('M0066', 'Display (20), geometric point/Y subscript within X', 'p07', r'\unsure{\zeta|\xi}_Y',
     'The small point glyph is dark and compressed, with an upper horizontal return and a descending lower stroke. No independent strike or recoverable older letter can be separated from its own strokes.'),
    ('M0067', 'Display (20), final point/T argument', 'p07', r'\unsure{\zeta|\xi}_T',
     'The glyph has a short top return, a bend and an elongated descending body; that shape does not uniquely distinguish xi and zeta.'),
    ('M0068', 'Inline fibre formula, geometric point/Y subscript within X', 'p09', r'\unsure{\zeta|\xi}_Y',
     'The small head bends left into a long nearly straight descent. There is no resolved set of upper lobes to decide the letter.'),
    ('M0069', 'Inline fibre formula, final point/T argument', 'p09', r'\unsure{\zeta|\xi}_T',
     'A short upper turn and long vertical body end in a small lower return next to T. Both candidate Greek identities remain possible.'),
]

DECISIONS = [dict(id=mid, cote='149', scan='113', decision='undecided',
                  reading=reading, evidence=evidence + ' The complete containing expression was inspected. The common zeta-first order is a preference, not a resolved correction.',
                  crop=crop(place), bbox=BOXES[place], confidence='medium')
             for mid, location, place, reading, evidence in POINT_PLACES]

DOUBTS = [dict(place=location, reading=reading,
               alternatives='xi remains possible; zeta is first under the supplied notation preference. ' + evidence,
               confidence='medium')
          for mid, location, place, reading, evidence in POINT_PLACES]
DOUBTS += [
    dict(place='Cancelled first-line word replaced by description',
         reading=r'\deleted{\unsure{definition|définition}}',
         alternatives='The strike traverses the small interior letters. No detached accent is securely visible, so an unaccented reading is first; accented définition remains possible. The whole cancelled word stays doubtful.',
         confidence='low'),
    dict(place='Third main line, point abbreviation',
         reading=r'\unsure{p^t|pt}',
         alternatives='The t rises above the p bowl, but its baseline return lies nearly level with that bowl. The crop does not securely separate a superscript t from an ordinary small t.',
         confidence='medium'),
    dict(place='Cancelled word before the dash introducing the fibre sentence',
         reading=r'\deleted{\unsure{donc}}',
         alternatives='The initial loop and lower rounded return support donc, but the strike hides the small final letters. No certain replacement for the tentative reading is supplied.',
         confidence='low'),
]

INVENTORY = [
    dict(sheet_kind='text', hand='authorial numbering in darker ink', element='e01', kind='margin note', position='top centre', first_words_or_objects='56', transcribed='yes'),
    dict(sheet_kind='text', hand='his hand', element='e02', kind='text', position='first four main prose lines', first_words_or_objects='Le lien avec la', transcribed='yes'),
    dict(sheet_kind='text', hand='his hand', element='e03', kind='deletion', position='first main line, before (11)', first_words_or_objects=r'\deleted{\unsure{definition|définition}}', transcribed='yes'),
    dict(sheet_kind='text', hand='his hand', element='e04', kind='insertion', position='above the cancelled first-line word', first_words_or_objects='description', transcribed='yes'),
    dict(sheet_kind='text', hand='his hand', element='e05', kind='display', position='three rows below des iso can', first_words_or_objects='(20), two relative E expressions; vertical isomorphism relation; Pi_1 expression', transcribed='yes'),
    dict(sheet_kind='text', hand='his hand', element='e06', kind='deletion', position='start of the first prose line below (20)', first_words_or_objects=r'\deleted{\unsure{donc}}', transcribed='yes'),
    dict(sheet_kind='text', hand='his hand', element='e07', kind='text', position='four prose lines from the dash to entre eux.', first_words_or_objects='--- les Pi_1', transcribed='yes'),
    dict(sheet_kind='text', hand='his hand', element='e08', kind='text', position='last six main prose lines, unfinished parenthesis', first_words_or_objects='( Il faut bien faire attention', transcribed='yes'),
    dict(sheet_kind='text', hand='his hand', element='e09', kind='insertion', position='between the first two lower-paragraph lines; leader to the gap after E_{X/Y}', first_words_or_objects='(Z non précisé)', transcribed='yes'),
    dict(sheet_kind='text', hand='separate thin foliation hand', element='e10', kind='margin note', position='bottom left', first_words_or_objects='112', transcribed='yes'),
]

AUDIT = [
    dict(box='b01', kind='handwritten number', bbox=BOXES['p01'], reading=r'\mspage{56}'),
    dict(box='b02', kind='C/H word difference', bbox=BOXES['p02'], reading='Le lien avec la'),
    dict(box='b03', kind='deletion; insertion; handwritten number; C/H word difference; less-than-high C departure', bbox=BOXES['p03'], reading=r'\deleted{\unsure{definition|définition}}\inserted{description} (11)'),
    dict(box='b04', kind='C/H word difference; doubtful formula', bbox=BOXES['p04'], reading=r"est évidemment que, si $\unsure{\zeta|\xi}_X$ provient d'un"),
    dict(box='b05', kind='C/H word difference; doubtful formula', bbox=BOXES['p05'], reading=r'$\unsure{p^t|pt}$ géom $\unsure{\zeta|\xi}_T$ de $T$, alors on aura'),
    dict(box='b06', kind='C/H word difference', bbox=BOXES['p06'], reading='des iso can'),
    dict(box='b07', kind='handwritten number; doubtful formula', bbox=BOXES['p07'], reading=FORMULA),
    dict(box='b08', kind='deletion; doubtful formula; handwritten number; C/H word difference', bbox=[244, 921, 1642, 1459], reading=MIDDLE),
    dict(box='b09', kind='insertion; C/H word difference', bbox=BOXES['p12'], reading=LOWER_START),
    dict(box='b10', kind='C/H word difference', bbox=[255, 1744, 1615, 2015], reading=r"de groupes profinis sans plus, \uline{pas} un groupe extérieur. L'arbitraire"),
    dict(box='b11', kind='C/H word difference', bbox=BOXES['p14'], reading="dans le choix d'un iso entre"),
    dict(box='b12', kind='C/H word difference', bbox=BOXES['p15'], reading=LAST),
    dict(box='b13', kind='margin note; handwritten number; C/H word difference', bbox=BOXES['p16'], reading=r'\margin{112}'),
]

DATA = dict(
    page=PAGE, scan=113, reader='reader_b', line_count=21,
    line_count_detail=dict(main=17, diagram=0, margin=0, insertion=2, standalone_numbers=2),
    changes=CHANGES, decisions=DECISIONS, inventory=INVENTORY,
    doubts=DOUBTS, audit_boxes=AUDIT,
    notes=[
        'The leaf relates the description (11) to geometric points, gives the isomorphism tableau (20), and says that the fibre-group expressions are canonically isomorphic. The lower parenthesis distinguishes an isomorphism class of profinite groups from an outer group and begins a discussion of the arbitrariness of an isomorphism. This summary describes the written text; it does not verify the claims.',
        'The authorial page number is 56 at the head; the lower-left thin foliation is 112. Both are transcribed and counted as separate logical lines.',
        'All-ink line count: four introductory prose baselines, three rows in (20), four prose baselines from the cancelled word to entre eux., and six lower-paragraph prose baselines give 17 main lines. The two supralinear insertions and the two standalone numbers give 21. The vertical isomorphism relation occupies its own written mathematical row. Inline (11), (20), and the two subscript 1s are on already-counted main rows.',
        'The first replacement description is above the cancelled word. Its attachment is clear. The original word remains doubtful because the strike coincides with interior strokes and its accent is not independently secure.',
        'The second insertion (Z non précisé) belongs after E_{X/Y}. Its separate long leader supplies the attachment. The f descender from faire crosses the insertion but is not a cancellation. No undertext is invented beneath that descender.',
        'The seven geometric-point glyphs remain xi/zeta unresolved. Their zeta-first ordering follows the supplied notation preference and is not counted as a correction against C. The two independent capital-Pi readings are actual symbol changes.',
        'The source reads pts géom de E^T_{X/Y}. That expression is preserved even though it may be an authorial slip. The supplied H editorial expectation of points of T is not inserted into the source text.',
        'The capital Z in the insertion is kept exactly, notwithstanding the T and T-prime notation elsewhere on the same leaf. No attempt is made to normalize these choices.',
        'The lower opening parenthesis remains unclosed and the page ends after du choix without added punctuation. The exact short forms and their written stops are preserved.',
        'The isomorphism tableau is set as three aligned mathematical rows, with the formula number beside its first row and the vertical relation kept vertical. This is a rendering choice, not a new equation or a directed diagram.',
        'Witness page-marker macros and editorial notes are not source wording. Their syntax, superscript/subscript source-code order, and line wrapping are excluded from the changes. The unlisted doubt on cancelled donc has no invented mark ID.',
        'Only this page packet, its current notation table, the common rules/protocol and the reader’s own files were used. The original and native halves were inspected once each; all sixteen saved crops were inspected. No OCR, external research or TeX compilation was used, and no proof verification is claimed.',
    ],
    checks=[],
    hand_observations=[
        dict(habit='Capital Pi has a flat cap and two separated posts; the right post may curve.', places='Display (20) and the following inline fibre formula.', holds='Both local occurrences have the cap and left post. The display right post is straighter; the inline right post curves at the bottom.', witness_errors='Both C and H gave lower-case pi at both places.'),
        dict(habit='The geometric-point letter varies from an upper-lobed sign to a simple hook and long descent.', places='Seven occurrences: two introductory points, three in (20), two in the following inline formula.', holds='All seven were inspected locally. This variation does not resolve xi versus zeta.', witness_errors='H silently chooses xi. C records both alternatives; its ordering alone is not treated as an error.'),
        dict(habit='A vertical isomorphism relation has a wavy member and a separate straight member.', places='Middle row of (20).', holds='Both members are visibly present and remain vertical.', witness_errors='H represents only the wavy member.'),
        dict(habit='Abbreviations and terminal returns must be kept without supplying stops or endings.', places='iso can; three géom occurrences; canoniquement iso; d’iso.; d’un iso.', holds='The three géom occurrences have no abbreviation stop; iso and can are bare. The lower d’iso. has its own visible stop. No final s in iso can or m after iso is written.', witness_errors='H expands or adds endings/stops in isos canon., géom., and isom.'),
        dict(habit='Long f descenders may cross another written level without cancelling it.', places='faire above the (Z non précisé) insertion; profinis above the following line.', holds='The stroke through the insertion can be traced to faire; the independent leader below it attaches the insertion after E_{X/Y}.', witness_errors='H places the insertion after attention rather than at the leader’s endpoint.'),
        dict(habit='The baseline of a short t after p may be too close to the p bowl to classify its typographic level securely.', places='Third introductory line.', holds='Only this local p/t occurrence is assessed. Superscript versus ordinary t remains doubtful.', witness_errors='C chooses p^t and H pt; neither is imposed as certain here.'),
    ],
    notation=[
        dict(written=r'\unsure{\zeta|\xi}_X,\ \unsure{\zeta|\xi}_T,\ \unsure{\zeta|\xi}_Y', meaning_or_use='Geometric-point notation; the letter identity remains unresolved in all seven occurrences.', places='Introductory prose, display (20), and fibre formula.'),
        dict(written=r'\mathcal E_{X/Y}^{\unsure{\zeta|\xi}_T}\simeq\mathcal E_{X/Y}^T', meaning_or_use='Upper horizontal isomorphism in (20).', places='First row of (20).'),
        dict(written=r'\Pi_1(X_{\unsure{\zeta|\xi}_Y},\unsure{\zeta|\xi}_T)', meaning_or_use='Written fibre-group expression; capital Pi retained from the local strokes.', places='Last row of (20) and the following inline formula.'),
        dict(written=r'\mathcal E_{X/Y}', meaning_or_use='Called a classe d’iso. de groupes profinis in the source, with inserted qualification Z non précisé.', places='Lower parenthesis.'),
        dict(written='Z non précisé', meaning_or_use='Literal inserted qualification; Z is not replaced by T.', places='Between the first two lower-paragraph lines, attached after E_{X/Y}.'),
        dict(written=r'\mathcal E_{X/Y}^T,\ \mathcal E_{X/Y}^{T\prime}', meaning_or_use='The two terms between which the lower paragraph discusses choosing an isomorphism.', places='Last main line.'),
    ],
    abbreviations=[
        dict(written=r'\unsure{p^t|pt}', expansion='point; typographic level of t remains doubtful'),
        dict(written='pts', expansion='points'),
        dict(written='géom', expansion='géométrique(s)'),
        dict(written='iso', expansion='isomorphisme(s)'),
        dict(written='iso.', expansion='isomorphisme, in classe d’iso.'),
        dict(written='can', expansion='canonique(s)'),
    ],
    inspection=dict(whole=True, halves=['top', 'bottom'],
                    crops=[crop(p) for p in BOXES],
                    deletions_insertions_checked=True),
)

if __name__ == '__main__':
    target = ROOT / f'edition/review/{PAGE}.json'
    if target.exists():
        raise FileExistsError(f'Refusing to overwrite frozen metadata: {target}')
    target.write_text(json.dumps(DATA, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(dict(path=str(target), changes=len(CHANGES),
                         crops=len(BOXES), doubts=len(DOUBTS),
                         audit_boxes=len(AUDIT), line_count=DATA['line_count'])))
