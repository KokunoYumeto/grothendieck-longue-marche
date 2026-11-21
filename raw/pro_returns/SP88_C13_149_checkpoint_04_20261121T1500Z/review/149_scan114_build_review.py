from pathlib import Path
import json

ROOT = Path('/workspace/scratch/0cab6a548abb')
PAGE = '149_scan114'
REVIEW = ROOT / 'edition' / 'review'
BOXES = json.loads((REVIEW / f'{PAGE}_crop_boxes.json').read_text())

def crop(p):
    return f'crops/{PAGE}_{p}.png'

def change(ident, p, place, C, H, final, evidence, confidence='high',
           vs_C=False, vs_H=True, kind='misread word', error_category='Words',
           H_marked=False, consequential=False, **extra):
    return dict(id=ident, place=place, C=C, H=H, final=final,
                evidence=evidence, crop=crop(p), bbox=BOXES[p][0],
                confidence=confidence, vs_C=vs_C, vs_H=vs_H, kind=kind,
                error_category=error_category, H_marked=H_marked,
                consequential=consequential, **extra)

tex = r'''\scanpage{114}

d'un él. de $\mathcal E_{X\deleted{\unsure{/Y}}}^T$, opérant
sur le sous-groupe $\mathcal E_{X/Y}^T$ par autom.
intérieurs.

Les notations \inserted{$\mathcal E_X$,} $\mathcal E_{X/Y}$ évoquent
intuitivement un $p^t$ de vue qui
regarde $\mathcal E_{X\deleted{\unsure{/Y}}}^T$ comme une \uline{extension}
de $\mathcal E_Y^T$ (ou d'un ss groupe
convenable seulement) par $\mathcal E_{X/Y}^T$,
qui sera souvent, pour les besoins de
la cause, noté $\unsure{\pi|\Pi}$ --- il joue le
rôle d'un groupe fondamental
(géométrique), tandis que $\mathcal E_Y^T$ joue
le rôle d'un groupe de Galois ---
ou d'un groupe profini mixte.

\margin{et j'hésite\newline
encore entre les\newline
notations $\mathcal E_{X/Y}^T$ et\newline
$\unsure{\pi|\Pi}_{X/Y}^T$; que je\newline
vais peut-être\newline
employer concur-\newline
remment.}

Le cas le plus important pour nous
sera celui où $Y=\operatorname{Spec}K$, $K$ un corps.
\deleted{\unsure{Aussi|Assez} \unsure{formellement|fréquemment|souvent}} Dans ce cas, $\mathcal E_Y\simeq\mathcal E_Y^{\unsure{\widetilde Y|\overline Y}}$

\margin{113}
'''

changes = [
    change('p01', 'p01', 'Main line 1, opening abbreviation and cancelled index',
           r"d'un él. de $\mathcal E_{X\deleted{\unsure{/Y}}}^T$, opérant",
           r"d'un \ill{} de $\mathcal{E}^{T}_{X}$ \struck{$/Y$}, \uncertain{opérant}",
           r"d'un él. de $\mathcal E_{X\deleted{\unsure{/Y}}}^T$, opérant",
           'The short group after un has an accented initial e, a tall l and a separate stop: él. The following word has the descending p and terminal t of opérant. The cancellation is at the X-index level; a Y-like descending stroke survives, but the crossing ink does not securely resolve every stroke of /Y. The supplied C uncertainty is retained, not resolved.',
           kind=r'readable ink left as \ill{}', error_category='Readable ink left as illegible', H_marked=True),
    change('p02', 'p02', 'Main line 2, sous-groupe and autom.',
           r'sur le sous-groupe $\mathcal E_{X/Y}^T$ par autom.',
           r'sur le \ill{}-groupe $\mathcal{E}^{T}_{X/Y}$ par \uncertain{auto.}',
           r'sur le sous-groupe $\mathcal E_{X/Y}^T$ par autom.',
           'The first part of sous-groupe is written before a separate hyphen; the s-shaped entry, reduced middle strokes and final s are present. The final abbreviation has the tall t followed by low returning strokes, including the final m-shaped continuation, and then a separate stop. Read autom., without expanding it.', H_marked=True),
    change('p03a', 'p03', 'Main line 4, opening noun',
           'Les notations', 'Les relations', 'Les notations',
           'The noun begins with a low n, followed by the tall crossed t of notations; it does not begin with the re sequence of relations. The terminal s is present.'),
    change('p03b', 'p03', 'Supralinear addition before the original E relative notation on main line 4',
           r"\inserted{$\mathcal E_X$,} $\mathcal E_{X/Y}$",
           r"($\mathcal{E}_X$, $\mathcal{E}_{X/Y}$ \uncertain{nouvelles})",
           r"\inserted{$\mathcal E_X$,} $\mathcal E_{X/Y}$",
           'E with a lower X and a comma is written on the separate upper baseline. Its curved leader descends to the space before the original E_{X/Y}; it is not an opening parenthesis. No paired parenthesis surrounds these notations.',
           kind='insertion or placement', error_category='Insertions put in the wrong place', H_marked=False),
    change('p03c', 'p03', 'Main line 4, verb after the original relative E notation',
           'évoquent', r'\uncertain{nouvelles}', 'évoquent',
           'The word has an initial e/v sequence, a descending q in its latter portion and the final tall t. These are the visible strokes of évoquent; a nouvelles ending is not supported.', H_marked=True),
    change('p04', 'p04', 'Main line 5',
           r'intuitivement un $p^t$ de vue qui',
           r'\uncertain{relativement} \ill{} pt de vue qui',
           r'intuitivement un $p^t$ de vue qui',
           'The opening has the repeated short i strokes and two tall t strokes of intuitivement. A separate reduced un follows. The p has a distinct small raised t to its upper right; the abbreviation is kept as p^t. The remainder de vue qui is present and unaltered.', H_marked=True),
    change('p05', 'p05', 'Main line 6, second cancelled relative suffix',
           r'regarde $\mathcal E_{X\deleted{\unsure{/Y}}}^T$ comme une \uline{extension}',
           r'regarde $\mathcal{E}^{T}_{X}$ comme une \emph{extension}',
           r'regarde $\mathcal E_{X\deleted{\unsure{/Y}}}^T$ comme une \uline{extension}',
           'A compact cancellation immediately follows X in the subscript. A descending Y-like component remains visible, but the short preceding oblique is entangled with cancellation strokes; /Y therefore stays doubtful. The underline beneath extension is a real separate horizontal stroke. H omits this cancelled suffix.',
           confidence='medium', kind='omission', error_category='Struck text', consequential=True),
    change('p06', 'p06', 'Main line 7, abbreviated subgroup phrase',
           "d'un ss groupe", "d'un sous-groupe", "d'un ss groupe",
           'Two small linked s-shaped forms are written before groupe. There is neither room for the expanded sous nor a separate hyphen here. This differs from the fully written sous-groupe on line 2.',
           kind='abbreviation expanded or spelling modernised', error_category='Abbreviations expanded, spelling modernised'),
    change('p07', 'p07', 'Main line 8, word before the closing parenthesis',
           r'convenable \unsure{seulement}) par $\mathcal E_{X/Y}^T$,',
           r'\uncertain{convenable}) par $\mathcal{E}^{T}_{X/Y}$,',
           r'convenable seulement) par $\mathcal E_{X/Y}^T$,',
           'The word after convenable is separately written: an s-shaped entry, reduced eu, a clear looped l, and a long ending with a crossed terminal t support seulement. The closing parenthesis follows it; H omits the word. This resolves supplied M0070 to its first reading.',
           kind='omission', error_category='Omissions'),
    change('p08', 'p08', 'Main line 9, after qui',
           'qui sera souvent, pour les besoins de',
           r'qui \ill{}, pour les besoins de',
           'qui sera souvent, pour les besoins de',
           'Two separate word groups follow qui. The first begins with the low looped s and ends in a; the second has the s entry, reduced ou/v sequence and a tall terminal t before a separate comma. They read sera souvent.',
           kind=r'readable ink left as \ill{}', error_category='Readable ink left as illegible', H_marked=True),
    change('p09', 'p09', 'Main line 10, after cause',
           r'la cause, noté $\pi$ --- il joue le',
           r'la cause, \ill{} $\pi$ --- il joue le',
           r'la cause, noté $\unsure{\pi|\Pi}$ --- il joue le',
           'The short word has n/o entry, a tall crossed t and a separate acute stroke over its ending: noté. The following pi-shaped sign has a flat cap, two posts and a curved right foot. That case question remains unresolved separately; no mathematical expectation is used to choose it.',
           kind=r'readable ink left as \ill{}', error_category='Readable ink left as illegible', H_marked=True),
    change('p10', 'p10', 'Oblique left marginal note, seven written lines',
           r"et j'hésite encore entre les \uline{notations} $\mathcal E_{X/Y}^T$ et $\pi_{X/Y}^T$; que je vais peut-être employer concurremment.",
           r"\ill{} relation \ill{} $\pi^{T}_{X/Y}$ ; que \ill{} \ill{} \ill{} \ill{} \ill{} \uncertain{temporairement}.",
           r"et j'hésite\newline encore entre les\newline notations $\mathcal E_{X/Y}^T$ et\newline $\unsure{\pi|\Pi}_{X/Y}^T$; que je\newline vais peut-être\newline employer concur-\newline remment.",
           'Rotation makes the seven baselines legible: et j’hésite / encore entre les / notations E_{X/Y}^T et / pi-shaped_{X/Y}^T; que je / vais peut-être / employer concur- / remment. The word notations has the n entry and crossed t. The apparent underline beneath it is the cap of the T belonging to the pi-shaped formula on the next line; no separate underline is visible. The final word begins con on the employer line, ends that line with cur and a separate short hyphen, and continues remment. below. The pi-shaped sign has the same unresolved flat-cap/two-post/curved-foot construction as line 10.',
           vs_C=True, H_marked=True),
    change('p11', 'p11', 'Main line 12, closing punctuation of géométrique',
           r'(géométrique), tandis que $\mathcal E_Y^T$ joue',
           r'(géométrique)), tandis que $\mathcal{E}^{T}_{Y}$ joue',
           r'(géométrique), tandis que $\mathcal E_Y^T$ joue',
           'There is one tall closing-parenthesis stroke after géométrique, followed by a separate lower comma. A second closing parenthesis is not written.',
           kind='text not on the page', error_category='Text that is not on the page'),
    change('p12a', 'p12', 'Main line 14, opening alternative',
           "ou d'un groupe profini", "d'un groupe profini", "ou d'un groupe profini",
           'A low two-part ou is written at the left before d’un. It belongs to the main baseline and is not punctuation or a marginal continuation.',
           kind='omission', error_category='Omissions'),
    change('p12b', 'p12', 'Main line 14, last word',
           'mixte.', r'\ill{}.', 'mixte.',
           'The word has reduced mi, a distinct crossing x, the tall crossed t and a terminal e stroke, followed by a separate stop: mixte.',
           kind=r'readable ink left as \ill{}', error_category='Readable ink left as illegible', H_marked=True),
    change('p13', 'p13', 'Main line 17, two cancelled words',
           r'\deleted{\unsure{Aussi|Assez} \unsure{souvent|fréquemment}}',
           r'\struck{Aussi formellement}',
           r'\deleted{\unsure{Aussi|Assez} \unsure{formellement|fréquemment|souvent}}',
           'The strike runs through both words. The first begins with a visible capital A; its reduced interior and ending are crossed, so Aussi/Assez remains unresolved. The second begins with a tall descending f-like stroke, followed by a small loop, and ends with a tall t-like stroke. Those visible remnants favor an f-initial possibility, with formellement placed first because the following small loop can be o; the interior is not securely recoverable, and fréquemment and C’s souvent remain explicit alternatives. Neither the reordering nor adding H’s possibility is claimed as a resolved C correction.',
           confidence='low', vs_H=False, kind='misread word', error_category='Struck text',
           unresolved=True, crop_note='p13 fully shows the cancellation but clips the top of the separate final formula; the formula is assessed and audited from p16.'),
    change('p14', 'p14', 'Bottom-left standalone foliation',
           r'\margin{113}', '[absent]', r'\margin{113}',
           'Two narrow numeral-one strokes followed by the double curve of 3 form the small standalone number 113. The dark lower strip is the page edge, not an underline.',
           kind='omission', error_category='Omissions'),
    change('p16', 'p16', 'Main line 17, complete final formula and its overlapping upper context',
           r'\mathcal E_Y\simeq\mathcal E_Y^{\widetilde Y}',
           r'\mathcal{E}_{Y}\simeq\mathcal{E}^{\overline{Y}}_{Y}',
           r'\mathcal E_Y\simeq\mathcal E_Y^{\unsure{\widetilde Y|\overline Y}}',
           'The left and right E symbols, both lower Y indices, the two-part isomorphism sign and the upper Y are visible. A short curved component to the left above the upper Y and a rightward rising tail suggest a tilde; the descending p of corps from the previous line intersects that area. The exact decoration cannot be securely separated into its original strokes, so tilde/bar remains unresolved. p16 includes the whole formula and the complete upper words K un corps. that cause the overlap.',
           confidence='medium', vs_H=False, kind='misread symbol or index', error_category='Symbols and indices',
           consequential=True, unresolved=True),
]

main_lines = [
    r"d'un él. de $\mathcal E_{X\deleted{\unsure{/Y}}}^T$, opérant",
    r'sur le sous-groupe $\mathcal E_{X/Y}^T$ par autom.',
    'intérieurs.',
    r'Les notations [insertion: $\mathcal E_X$,] $\mathcal E_{X/Y}$ évoquent',
    r'intuitivement un $p^t$ de vue qui',
    r'regarde $\mathcal E_{X\deleted{\unsure{/Y}}}^T$ comme une \uline{extension}',
    r"de $\mathcal E_Y^T$ (ou d'un ss groupe",
    r'convenable seulement) par $\mathcal E_{X/Y}^T$,',
    'qui sera souvent, pour les besoins de',
    r'la cause, noté $\unsure{\pi|\Pi}$ --- il joue le',
    "rôle d'un groupe fondamental",
    r'(géométrique), tandis que $\mathcal E_Y^T$ joue',
    r"le rôle d'un groupe de Galois ---",
    "ou d'un groupe profini mixte.",
    'Le cas le plus important pour nous',
    r'sera celui où $Y=\operatorname{Spec}K$, $K$ un corps.',
    r'\deleted{\unsure{Aussi|Assez} \unsure{formellement|fréquemment|souvent}} Dans ce cas, $\mathcal E_Y\simeq\mathcal E_Y^{\unsure{\widetilde Y|\overline Y}}$',
]
margin_lines = ["et j'hésite", 'encore entre les', r'notations $\mathcal E_{X/Y}^T$ et',
                r'$\unsure{\pi|\Pi}_{X/Y}^T$; que je', 'vais peut-être', 'employer concur-', 'remment.']

inventory = [
    dict(sheet_kind='text', hand='his hand', element='e01', kind='text', position='Main lines 1–3, top', first_words_or_objects="d'un él. de ... opérant sur le sous-groupe", transcribed='yes'),
    dict(sheet_kind='text', hand='his hand', element='e02', kind='deletion', position='Main line 1, after X in the first E subscript', first_words_or_objects=r'\unsure{/Y}', transcribed='yes'),
    dict(sheet_kind='text', hand='his hand', element='e03', kind='text', position='Main lines 4–14, central paragraph; extension underlined on line 6', first_words_or_objects='Les notations ... évoquent intuitivement', transcribed='yes'),
    dict(sheet_kind='text', hand='his hand', element='e04', kind='insertion', position='Separate supralinear baseline above main line 4, with leader before the original E_{X/Y}', first_words_or_objects=r'$\mathcal E_X$,', transcribed='yes'),
    dict(sheet_kind='text', hand='his hand', element='e05', kind='deletion', position='Main line 6, after X in the E subscript', first_words_or_objects=r'\unsure{/Y}', transcribed='yes'),
    dict(sheet_kind='text', hand='his hand', element='e06', kind='margin note', position='Left margin beside main lines 9–14; seven oblique baselines', first_words_or_objects="et j'hésite encore entre les notations", transcribed='yes'),
    dict(sheet_kind='text', hand='his hand', element='e07', kind='text', position='Main lines 15–17, bottom paragraph and inline final formula', first_words_or_objects='Le cas le plus important pour nous', transcribed='yes'),
    dict(sheet_kind='text', hand='his hand', element='e08', kind='deletion', position='Main line 17, immediately before Dans ce cas', first_words_or_objects=r'\unsure{Aussi|Assez} \unsure{formellement|fréquemment|souvent}', transcribed='yes'),
    dict(sheet_kind='text', hand='unattributed numbering hand', element='e09', kind='margin note', position='Bottom-left standalone foliation', first_words_or_objects='113', transcribed='yes'),
]

def audit(box, kind, bbox, reading, context_note=None):
    d = dict(box=box, kind=kind, bbox=bbox, reading=reading)
    if context_note:
        d['context_note'] = context_note
    return d

margin_reading = r"\margin{et j'hésite\newline encore entre les\newline notations $\mathcal E_{X/Y}^T$ et\newline $\unsure{\pi|\Pi}_{X/Y}^T$; que je\newline vais peut-être\newline employer concur-\newline remment.}"

audit_boxes = [
    audit('b01', 'deletion; doubtful formula; C/H word difference', BOXES['p01'][0], main_lines[0]),
    audit('b02', 'C/H word difference', BOXES['p02'][0], main_lines[1]),
    audit('b03', 'insertion; C/H word difference', [300,360,1650,590],
          r'intérieurs. Les notations \inserted{$\mathcal E_X$,} $\mathcal E_{X/Y}$ évoquent',
          'The upper left has the complete end of the preceding sentence, intérieurs. The separate upper E_X and comma are attached by a leader between notations and the original relative E notation.'),
    audit('b04', 'C/H word difference', BOXES['p04'][0], main_lines[4]),
    audit('b05', 'deletion; doubtful formula; C/H word difference', [300,595,1650,885],
          main_lines[4] + '\n' + main_lines[5],
          'Both complete adjacent main lines are included, so the long descender of qui is context, not a mark on the E formula.'),
    audit('b06', 'C/H word difference', [298,880,1520,1146], main_lines[6] + '\n' + main_lines[7]),
    audit('b07', 'C/H word difference', BOXES['p08'][0], main_lines[8],
          'At the lower edge are clipped upper strokes from the following main line (la cause, noté ...), and at the lower left a clipped part of the adjacent marginal opening. They are separately read in b08 and b09; they are not additional words of this line.'),
    audit('b08', 'doubtful formula; C/H word difference', BOXES['p09'][0], main_lines[9],
          'The upper-left boundary includes the clipped lower descender of preceding qui. Small isolated strokes at the lower boundary are clipped upper portions of the following rôle line. The full pi-shaped sign and all text of the target line are included.'),
    audit('b09', 'margin note; doubtful formula; C/H word difference; less-than-high C departure', BOXES['p10'][0], margin_reading,
          'The rectangular box also intersects the adjacent main text at its right edge: a clipped descender from qui, the word la, clipped beginnings of rôle and (géométrique), and the short beginnings le and ou of later lines. These fragments are already transcribed on their respective main lines and are not continuations of the oblique marginal note. The box includes both complete marginal formulae; the saved crop is rotated clockwise 40 degrees for reading.'),
    audit('b10', 'C/H word difference', BOXES['p11'][0], main_lines[11],
          'Oblique clipped strokes at the upper left belong to the marginal ending concur- and its neighboring marginal context, fully transcribed in b09; they are not additional opening punctuation on the main line.'),
    audit('b11', 'C/H word difference', BOXES['p12'][0], main_lines[13]),
    audit('b12', 'deletion; C/H word difference', [274,2225,778,2330],
          r'\deleted{\unsure{Aussi|Assez} \unsure{formellement|fréquemment|souvent}}'),
    audit('b13', 'handwritten number', BOXES['p14'][0], r'\margin{113}',
          'The dark strip at the bottom is the photographed sheet edge, not a written underline or an additional character.'),
    audit('b14', 'doubtful formula; C/H word difference', [1215,2070,1648,2341],
          r', $K$ un corps. $\mathcal E_Y\simeq\mathcal E_Y^{\unsure{\widetilde Y|\overline Y}}$',
          'The upper context is the comma after Spec K followed by K un corps. The full final formula is on the lower baseline. Its upper decoration overlaps the descending p of corps. This audit rectangle deliberately includes the entire decoration and the upper word that causes the overlap.'),
]

doubts = [
    dict(place='Main line 1, first cancelled index suffix', reading=r'\deleted{\unsure{/Y}}', alternatives='The /Y reading remains tentative because of the dense crossing strokes; Y-like descender visible.', confidence='low', crop=crop('p01'), bbox=BOXES['p01'][0]),
    dict(place='Main line 6, second cancelled index suffix', reading=r'\deleted{\unsure{/Y}}', alternatives='The /Y reading remains tentative; the preceding slash cannot be separated securely from the cancellation.', confidence='low', crop=crop('p05'), bbox=BOXES['p05'][0]),
    dict(place='Main line 10, pi-shaped notation after noté', reading=r'\unsure{\pi|\Pi}', alternatives=r'\pi | \Pi; same flat-cap/two-post form as the marginal occurrence, with curved right foot.', confidence='medium', crop=crop('p09'), bbox=BOXES['p09'][0]),
    dict(place='Margin line 4, indexed pi-shaped notation', reading=r'\unsure{\pi|\Pi}_{X/Y}^T', alternatives=r'\pi_{X/Y}^T | \Pi_{X/Y}^T; local case unresolved independently of prior-page conventions.', confidence='medium', crop=crop('p10'), bbox=BOXES['p10'][0]),
    dict(place='Main line 17, first cancelled word', reading=r'\unsure{Aussi|Assez}', alternatives='Aussi | Assez; capital A plain, crossed interior and ending uncertain.', confidence='low', crop=crop('p13'), bbox=[274,2225,778,2330]),
    dict(place='Main line 17, second cancelled word', reading=r'\unsure{formellement|fréquemment|souvent}', alternatives='formellement | fréquemment | souvent; the tall descending f-like initial and following small loop support placing formellement first, but do not resolve the crossed interior.', confidence='low', crop=crop('p13'), bbox=[274,2225,778,2330]),
    dict(place='Main line 17, decoration on superscript Y in complete final formula', reading=r'\mathcal E_Y\simeq\mathcal E_Y^{\unsure{\widetilde Y|\overline Y}}', alternatives=r'\widetilde Y | \overline Y; a curved left component and rising right tail overlap the p-descender from corps.', confidence='medium', crop=crop('p16'), bbox=BOXES['p16'][0]),
]

unlisted = [
    dict(place='Main line 1, nested C doubt inside deleted index', decision='undecided', reading=r'\deleted{\unsure{/Y}}', evidence='Crossing strokes obscure the slash and part of the following Y-like form.', crop=crop('p01'), bbox=BOXES['p01'][0], confidence='low'),
    dict(place='Main line 6, nested C doubt inside deleted index', decision='undecided', reading=r'\deleted{\unsure{/Y}}', evidence='Small crossed cluster with surviving descender; /Y not fully recoverable.', crop=crop('p05'), bbox=BOXES['p05'][0], confidence='low'),
    dict(place='Main line 17, first nested cancelled-word C doubt', decision='undecided', reading=r'\unsure{Aussi|Assez}', evidence='Initial A plain; cancellation obscures deciding interior/ending strokes.', crop=crop('p13'), bbox=[274,2225,778,2330], confidence='low'),
    dict(place='Main line 17, second nested cancelled-word C doubt', decision='undecided', reading=r'\unsure{formellement|fréquemment|souvent}', evidence='Visible initial descender is f-like and the next small loop can be o. H’s possibility is added, with no asserted resolution of the interior.', crop=crop('p13'), bbox=[274,2225,778,2330], confidence='low'),
]

report = dict(
    page=PAGE, scan=114, reader='reader_a', line_count=26,
    line_count_detail=dict(main=17, margin=7, insertion=1, standalone_numbers=1),
    line_count_note='All separate logical written baselines are counted, including the inserted E_X comma above line 4, the seven marginal baselines and standalone 113. The superscript p^t and ordinary indices are not extra text lines. No author page number is visible at the head.',
    line_map=dict(main=[dict(line=i+1,reading=s) for i,s in enumerate(main_lines)],
                  margin=[dict(line=i+1,reading=s) for i,s in enumerate(margin_lines)],
                  insertion=[r'$\mathcal E_X$,'], standalone_numbers=['113']),
    changes=changes,
    decisions=[dict(id='M0070', cote='149', scan='114', decision='first', reading='seulement',
                    evidence='Separate word after convenable: s-shaped entry, reduced eu, clear looped l, and extended ending with crossed terminal t; closing parenthesis follows the complete word.',
                    crop=crop('p07'), bbox=BOXES['p07'][0], confidence='high')],
    unlisted_doubt_decisions=unlisted,
    inventory=inventory, doubts=doubts, audit_boxes=audit_boxes,
    notes=[
        'The leaf continues a discussion of inner action on a relative E group, describes an extension interpretation, proposes fundamental-group notation, and turns at the bottom to the case Y=Spec K. No external page or mathematical reconstruction supplies any wording.',
        'The only supplied mark ID is M0070. The four C doubts nested in cancellations are recorded outside decisions, without invented M IDs.',
        'The two cancelled /Y suffixes, the two cancelled words, both pi-shaped cases, and the final Y decoration remain explicitly uncertain. Reordering or broadening alternatives is not treated as a resolved correction of C.',
        'The main and marginal pi-shaped signs have matching local forms, but prior notation-table entries are not used to force uppercase or lowercase here.',
        'The bar below marginal notations is the top of the following formula’s superscript T, not a separate underline. The visibly written line-end hyphen in concur- is retained with the following remment. baseline.',
        'The cancelled second word begins with an f-like descending stroke. The following small loop permits formellement, but neither its interior l strokes nor a decisive alternative interior is recoverable beneath the strike. All proposed alternatives remain unconfirmed.',
        'p13 was sufficient for the cancelled phrase but clipped the final formula’s upper decoration. p15 is a contextual repair; p16 is a focused view of the unresolved overlap between the final decoration and corps-p. These are one visual problem, not three independent evidential observations. No more crops were made after p16.',
        'The standalone lower-left 113 is preserved as foliation. There is no visible author page number and no handwritten formula number on this leaf.',
        'Differences due only to math-macro order, TeX wrapping, scan markers, or certainty markers without changed wording are not counted as lexical changes. The final tilde/bar and cancelled-word witness divergences remain in changes as unresolved, with neither witness declared decisively wrong.',
        'Full sheet and both native halves were inspected once before cropped reading. Every saved crop p01–p16 was visually inspected. No OCR, external research, PDF text layer, access to another page’s sources, or TeX compilation was used.',
    ],
    checks=[dict(statement_id='149_114_n02', type='targeted proof check',
                 outcome='Only the local group-theoretic implication behind the opening wording was checked: for a normal subgroup N of G, conjugation n -> gng^{-1} maps N to N and has inverse conjugation by g^{-1}, hence is an automorphism of N. This page alone does not establish the needed normal-subgroup premise for the E groups, and this check was not used to reconstruct the cancelled indices.')],
    hand_observations=[
        dict(habit='Low, strongly reduced internal letter strokes with disproportionately tall t, l and descending p/q.', places='Main lines 2, 5, 8–10, 14.', holds='Confirmed locally in autom., intuitivement, seulement, souvent, noté and mixte; reduced middle letters do not justify expanding short forms.', witness_errors='H leaves several readable whole words as ill or substitutes relatives such as relativement.'),
        dict(habit='A curved leader can resemble a parenthesis when an upper addition is linearized.', places='Upper addition E_X, before main line 4.', holds='One clearly observed insertion; no enclosing pair of parentheses.', witness_errors='H treats the surrounding area as a parenthesized sequence.'),
        dict(habit='Flat cap over two posts, with a curved right foot, for the pi-shaped symbol.', places='Main line 10 and margin line 4.', holds='Both local occurrences match, but their case remains unresolved.', witness_errors='Both witnesses choose lowercase without expressing this local case uncertainty.'),
        dict(habit='Oblique marginal lines overlap the vertical range of superscripts on the next line.', places='Margin lines 3–4.', holds='The apparent underline under notations is the cap of T on the next formula.', witness_errors='C marks notations as underlined.'),
        dict(habit='A written line-end hyphen divides a word across marginal baselines.', places='Margin lines 6–7, concur- / remment.', holds='One confirmed divided word on this page.', witness_errors='C silently joins the word; H substitutes temporairement.'),
    ],
    notation=[
        dict(written=r'$\mathcal E_X$, $\mathcal E_{X/Y}$', meaning_or_use='Two notations said to evoke an extension viewpoint; E_X and its comma are supralinearly inserted.', places='Main line 4 and insertion.'),
        dict(written=r'$\mathcal E_{X\deleted{\unsure{/Y}}}^T$', meaning_or_use='Absolute E notation left after a cancelled relative suffix; the suffix itself remains doubtful.', places='Main lines 1 and 6.'),
        dict(written=r'$\mathcal E_{X/Y}^T$, $\mathcal E_Y^T$', meaning_or_use='Relative subgroup and quotient/base-group symbols in the prose extension discussion.', places='Main lines 2, 7–8, 12; margin line 3.'),
        dict(written=r'$\unsure{\pi|\Pi}$, $\unsure{\pi|\Pi}_{X/Y}^T$', meaning_or_use='Proposed fundamental-group notation; uppercase/lowercase remains unresolved from the local ink.', places='Main line 10; margin line 4.'),
        dict(written=r'$Y=\operatorname{Spec}K$', meaning_or_use='The field case introduced at the bottom; K is explicitly called un corps.', places='Main line 16.'),
        dict(written=r'$\mathcal E_Y\simeq\mathcal E_Y^{\unsure{\widetilde Y|\overline Y}}$', meaning_or_use='Final written identification; upper decoration on Y remains uncertain because it overlaps corps above.', places='Main line 17.'),
    ],
    abbreviations=[
        dict(written='él.', expansion='élément (expansion for the report only)'),
        dict(written='autom.', expansion='automorphismes (expansion for the report only)'),
        dict(written=r'$p^t$', expansion='point (raised t retained in transcription)'),
        dict(written='ss', expansion='sous (unexpanded and without an invented hyphen in transcription)'),
    ],
    inspection=dict(whole=True, halves=['top','bottom'], crops=[crop(f'p{i:02d}') for i in range(1,17)],
                    deletions_insertions_checked=True, crop_count=16,
                    crop_repairs=[dict(original='p13', repair='p15', focused='p16', reason='The original cancellation-context crop clipped the upper decoration of the final formula; the repair and focused unresolved-overlap view restore the whole formula without any rereading of a decided symbol.')]),
)

assert [d['id'] for d in report['decisions']] == ['M0070']
assert report['line_count'] == sum(report['line_count_detail'].values())
assert len(main_lines) == 17 and len(margin_lines) == 7
assert len(report['inspection']['crops']) == 16
for p in report['inspection']['crops']:
    assert (ROOT / 'edition' / p).exists(), p
(REVIEW / f'{PAGE}.tex').write_text(tex, encoding='utf-8')
(REVIEW / f'{PAGE}.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps(dict(page=PAGE, changes=len(changes), crops=16, doubts=len(doubts), audit_boxes=len(audit_boxes), line_count=26, decisions=['M0070']), ensure_ascii=False))
