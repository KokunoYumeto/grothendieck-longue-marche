from pathlib import Path
import json

base = Path('/workspace/scratch/d7279cb02214')
work = base / 'SP92_C13_150+151_work'
page = '150_scan093'
packet = json.loads((base / 'reading_packets' / page / 'packet.json').read_text())
crops = json.loads((work / 'records' / f'{page}_cropmap.json').read_text())
C, H = packet['witness_C'], packet['witness_H']
tex = (work / 'records' / f'{page}.tex').read_text()
changes = []

def add(place, c, h, final, evidence, crop, confidence, kind, error, ac, ah,
        consequential=False, marked=False, change_type=None):
    assert c == '' or c in C, ('C snippet', place, c)
    assert h == '' or h in H, ('H snippet', place, h)
    row = dict(id=f'C{len(changes)+1:02d}', place=place, C=c, H=h, final=final,
               evidence=evidence, crop=crops[crop]['crop'], box=crops[crop]['box'],
               confidence=confidence, kind=kind, error_kind=str(error),
               against_C=ac, against_H=ah, consequential=consequential,
               marked_in_H=marked)
    if change_type:
        row['change_type'] = change_type
    changes.append(row)

add('Opening words', 'On a', r'\uncertain{Les} \ill{}', 'On a',
    'An open, tall initial O turns into a reduced n along the baseline; the separated small oval with a right return is a. There is no tall e/s sequence corresponding to Les. The second On a on this leaf supplies a direct same-page comparison.',
    'on_a', 'high', 'misread word', 2, False, True, marked=True)
add('Opening line, after the assignment J to X star', 'aux unions',
    r'\ill{} \ill{} réunions', 'aux unions',
    'Three short low units spell aux. The following word begins with linked u/n humps, followed by the i mark, rounded o and terminal n/s return; it has no initial ré strokes. The complete opening line and its continuation were also read.',
    'aux_unions', 'high', 'misread word', 2, False, True, marked=True)
add('Unnumbered display after en particulier, both empty-set glyphs',
    r'X_\varnothing^*=\varnothing', r'X^{*}_\emptyset=\emptyset', r'X_\phi^*=\phi',
    'Both signs have a small loop around a long axial stem with a pronounced descending extension, not merely an oval crossed by an equal-length slash. The stem is slanted with this writing, but the loop-and-descender construction is phi-shaped. The whole display, including the I subscript and final period, was reread.',
    'empty_first', 'high', 'misread symbol or index', 1, True, True)
add('(95), canceled middle X and its uncrossed barred-J subscript',
    r'\deleted{X_{\bar J}}', '', r'\deleted{X}_{\bar J}',
    'Additional crossing strokes are confined to the middle X. The following J and its separate overbar are intact and have no strike through them; a further equality and live starred X follow. H mentions a canceled X editorially but omits this old subscript and term from its transcription. The candidate records the physical deletion span rather than extending the strike to the subscript.',
    'formula95', 'high', 'deletion state (struck given live or live given struck)', 7, True, True,
    consequential=True)
add('Introduction of (97)', 'Si on a (Strat 5), alors',
    r'\ill{} \ill{} (Strat 5), \uncertain{alors}', 'Si on a (Strat 5), alors',
    'The opening has the looped S and small i, followed by the low on and separate a. After the closing parenthesis and comma, the word has a small initial a, tall looped l and reduced ors ending. The digit has a top stroke and lower curve of 5.',
    'strat5', 'high', r'readable ink left as \ill{}', 5, False, True, marked=True)
add('Diagonal left margin, first word', 'dualement', r'dans \ill{}', 'dualement',
    'After rotation the d ascender, reduced u/a, tall l and continuous ement ending are visible in a single word. The word is substantially longer than dans.',
    'margin_dual', 'high', 'misread word', 2, False, True, marked=True)
add('Diagonal left margin, first mathematical term', r'$X_{\widetilde J}^*$',
    r'$X^{*}_J$', r'$X_{\widetilde J}^*$',
    'A separate wavy horizontal mark sits directly above J and below the high star. It is a tilde, not part of J or the adjacent word.',
    'margin_dual', 'high', 'misread symbol or index', 1, False, True,
    consequential=True, marked=True)
add('Diagonal left margin, description after first X', 'est le plus petit sous-ens.',
    r'\ill{} le plus petit \ill{} \ill{}', 'est le plus petit sous-ens.',
    'The small est follows the first formula. Below it, plus has its p descender and l ascender, petit has the paired t strokes, and sous-ens. has the two short groups separated by a visible hyphen and followed by a point. H leaves est and the compound short form unread.',
    'margin_dual', 'high', r'readable ink left as \ill{}', 5, False, True, marked=True)
add('Diagonal left margin, adjective after de X', 'saturé', r'\ill{}', 'saturé',
    'After X there is an s curve, a loop, a tall t, linked u/r and the final e with a separate accent stroke. It reads saturé.',
    'margin_dual', 'high', r'readable ink left as \ill{}', 5, False, True, marked=True)
add('M0720, subscript in de la forme X star', "\\unsure{?|J'}",
    '?', '?',
    'The tight rotated detail shows a curved question-mark head descending to a short stem and a detached low dot. There is no upper and lower-bar construction of J, nor a separate prime. The entire marginal statement was reread with this index.',
    'margin_index', 'high', 'misread symbol or index', 1, True, False,
    consequential=True, marked=True, change_type='doubt resolution')
add('Diagonal left margin, final relative clause',
    r'qui soit ouvert et contienne $X_J^*$',
    r'\ill{} \ill{} soit \ill{} (97) \ill{} $X^{*}_J$ \ill{} ouvert \ill{} \ill{}',
    r'qui soit ouvert et contienne $X_J^*$',
    'The q descender and dotted i form qui, followed to the right by soit. The next diagonal baseline begins with the open o and linked u/v/ert of ouvert, then the crossed t of et and the c-o-n-t-i-e-n-n-e sequence of contienne. Its final starred X has angular J below it. H shifts the order of these surviving words and includes the adjacent main display label; that label is separately accounted for below.',
    'margin_dual', 'high', r'readable ink left as \ill{}', 5, False, True, marked=True)
add('H includes main display label inside the diagonal marginal note', '', '(97)', '',
    'The large (97) is horizontal with the main formula. In the rotated marginal view it cuts across the space between the slanting marginal lines; it does not belong to their prose and is already transcribed at the main display.',
    'margin_dual', 'high', 'insertion or placement', 6, False, True, marked=True)
add('Canceled dotted-X display, left term', r'\dot X_J', r'\dot X^{*}_J', r'\dot X_J',
    'The left X has a single separate dot above its center and J below-right. The high area to its right contains the rising cancellation stroke and the definition label, with no separate star. The two right-hand X terms do each have a distinct star.',
    'canceled_dot', 'high', 'text not on the page', 9, False, True,
    consequential=True)
add('Canceled dotted-X display, definition label', r'\mathrm{déf}', r'\text{déf}', r'\mathrm{def}',
    'The enlarged, upward-reframed crop shows the tall d, connected e and tall f. There is no detached accent above the e, although the surrounding white space and both ascenders are present. The short form has no stop.',
    'canceled_dot', 'medium', 'abbreviation expanded or spelling modernised', 8, True, True)
add('Canceled expression immediately after donc',
    r'\deleted{$\unsure{\overline{X_J^*}=X_J^*}$}',
    r'\struck{$\overline{X^{*}_J}$ \ill{}}',
    r'\deleted{\unsure{\overline{X_J^*}=X_J^*}}',
    'The first X, its bar, angular J and small high star survive. After it, short lower strokes and the second crossed X survive beneath a heavy zigzag. The relation and final subscript are not separable enough to resolve C’s provisional expression; the uncertainty is deliberately retained rather than reported as a settled recovery. H leaves this tail as an illegibility.',
    'donc_math_detail', 'low', 'other', 10, False, True,
    consequential=True, marked=True)
add('Closedness paragraph, first empty-set glyph',
    r'X_{\bar J\setminus J}^*=\varnothing',
    r'X^{*}_{\overline J\smallsetminus J}=\emptyset',
    r'X_{\bar J\setminus J}^*=\phi',
    'The small oval is pierced by a long descending axial stroke. Its construction repeats the phi-shaped signs in the earlier unnumbered display; it is not a plain empty oval.',
    'closed_continuation', 'high', 'misread symbol or index', 1, True, True)
add('Closedness paragraph, abbreviation strat', 'strat', 'strat.', 'strat',
    'The last tall t ends in a short rightward foot. The space between that foot and est is clear, with no following dot. The earlier dots over the preceding si belong to i, not to this abbreviation.',
    'strat_word', 'high', 'abbreviation expanded or spelling modernised', 8, False, True)
add('Closedness paragraph, second empty-set glyph',
    r'\bar J\setminus J=\varnothing', r'\overline J\smallsetminus J=\emptyset',
    r'\bar J\setminus J=\phi',
    'This occurrence again has a small loop around an axial stroke whose long lower extension reaches well below the loop. It repeats the other three phi-shaped empty-set signs on the leaf.',
    'closed_continuation', 'high', 'misread symbol or index', 1, True, True)
add('Canceled letter between Si and L in final prose line',
    r'\deleted{\unsure{A}}', '', r'\deleted{\unsure{A|B}}',
    'A tall left side and looped right-side outline survive under upper and lower crossing strokes. These make A plausible, but the right loops also admit B; the letter is not resolved. H mentions a biffed letter in an editorial note but supplies no ink reading in its prose. The new alternative is an added doubt, not a claimed correction to C’s first reading.',
    'lower_canceled_letter', 'low', 'omission', 3, False, True)
add('(98), canceled letter between est and ouvert',
    r'\deleted{\unsure{f}}', '', r'\deleted{f}',
    'The tight detail separates the tall upper loop, long descending stem and leftward lower return of f from the lighter crossing stroke. There is one letter only, with no continuation before ouvert. C’s first reading is retained with its doubt removed; H omits it.',
    'canceled_f', 'medium', 'omission', 3, True, True,
    change_type='doubt resolution')
add('Lower-left foliation in a later thin grey hand', r'\margin{92}', '', r'\margin{92}',
    'The light grey 9 has an enclosed head and descending tail, followed by a curved 2 with a long baseline. Its thin grey hand differs from the dark upper 43 and body writing. It is preserved as marginal foliation, not as the author’s page number.',
    'folio92', 'high', 'omission', 3, False, True)
add('Opening assignment, headless mapping shaft', r'\mapsto', r'\mapsto',
    r'\mathrel{\mapstochar\relbar}',
    'The left endpoint has a short upright tail bar. The horizontal shaft ends on the right in a blunt dark cap, without upper or lower diagonal strokes forming an arrowhead. Both witness commands supply a head that is absent in the ink. The standard mapstochar plus relbar records the written sign without drawing running text.',
    'opening', 'high', 'misread symbol or index', 1, True, True,
    consequential=True)
add('Raised insertion, supposed comma after fermé',
    r'\inserted{i.e. $J=I\setminus L$ fermé,}',
    r'\add{i.e.\ $J=I\smallsetminus L$ fermé,}',
    r'\inserted{i.e. $J=I\setminus L$ fermé}',
    'The upturn to the right of fermé joins continuously to the long insertion leader beneath the clause. There is no detached comma at the word ending. The separate baseline comma after ouvert remains visible and is retained.',
    'lower_insertion', 'high', 'text not on the page', 9, True, True)

coverage = []
special = {
    540: ('editorial-only', [], 'Archive scan marker and H’s editorial description of the authorial 43; 43 is present in both readings.'),
    541: ('editorial-only', [], 'H’s words describing the number 43 and C’s display boundary are not additional source ink.'),
    544: ('reading', ['C01'], 'Opening On a versus H’s Les/illegibility; H’s intervening page-continuation note is editorial.'),
    546: ('reading', ['C02'], 'Aux unions versus unread slots and réunions; the star placement in the token list is only TeX order.'),
    561: ('reading', ['C04'], 'Alignment shifts because H omits the old middle X and barred-J subscript from the formula.'),
    562: ('reading', ['C04'], 'The omitted old middle term and second equality produce this alignment with H’s editorial note.'),
    563: ('reading', ['C04'], 'H describes a crossed X editorially; the candidate transcribes its exact physical scope and uncrossed subscript.'),
    564: ('reading', ['C04'], 'End of the old-term mismatch; H’s inclusion-shape comment is editorial. The relation itself remains a new narrow doubt, without a correction row.'),
    569: ('editorial-only', [], 'H’s location note for the same right marginal sentence is not source text.'),
    578: ('reading', ['C05'], 'Si on a and alors are readable in the ink where H leaves blanks/uncertainty.'),
    586: ('alignment-only', [], 'H’s note quotes the same moyennant densité that C places in a margin macro; then H orders the canceled display before the left marginal note.'),
    587: ('reading', ['C06','C07','C08','C09','C10','C11','C12','C13','C14'], 'Long shifted alignment combines the recovered diagonal margin and the canceled definition display; the quoted density note adds no source wording.'),
    591: ('reading', ['C06','C07'], 'Beginning of H’s later-placed diagonal margin has dans/blank and lacks the tilde.'),
    592: ('reading', ['C08','C09','C10','C11','C12','C15'], 'The long shifted margin alignment and the following canceled expression are accounted for at their physical places.'),
    593: ('reading', ['C15'], 'Superscript-order alignment lies within H’s partly unread canceled expression; C’s uncertainty is retained.'),
    594: ('reading', ['C15'], 'Same canceled-expression alignment; no additional live X is introduced.'),
    595: ('reading', ['C15'], 'C’s provisional relation and second term versus H’s unread tail remain uncertain under the strike.'),
    596: ('reading', ['C15'], 'End of the same crossed-expression mismatch; the following live X is separately present in both witnesses.'),
    603: ('reading', ['C17'], 'H supplies a stop after strat that is absent in the ink.'),
    604: ('reading', ['C19'], 'Canceled letter omitted from H’s prose, although mentioned in its note; its identity remains uncertain.'),
    608: ('macro-only', [], 'Subscript/superscript order and display closure before the same est ouvert continuation; no word-order change.'),
    609: ('reading', ['C20'], 'The canceled f before ouvert is omitted by H.'),
    610: ('reading', ['C19','C21'], 'H omits the later foliation 92; its following notes describe double underlining and the canceled letter, rather than new text.')
}
for d in packet['differences']:
    num = int(d['diff_id'][1:])
    cl, ids, reason = special.get(num, ('macro-only', [],
        'The witnesses have the same visible mathematical reading; this token difference comes from subscript/superscript order, equivalent bar/set-difference commands or display syntax. The relevant formula was read on the image.'))
    coverage.append(dict(diff_id=d['diff_id'], classification=cl, change_ids=ids, reason=reason))

inventory = []
def inv(element, kind, position, first, hand='author'):
    inventory.append(dict(sheet_kind='text', hand=hand, element=element, kind=kind,
                          position=position, first_words_or_objects=first, transcribed='yes'))
inv('Authorial page number', 'margin note', 'upper left', '43')
inv('Canceled opening equality', 'deletion', 'top, above opening prose', r'X_J^*=X_{\bar J}')
inv('Opening sentence', 'text', 'upper main block, two lines', 'On a compatibilité')
inv('Display (94)', 'display', 'upper main block', '(94), union and intersection formulas')
inv('Particular-case introduction', 'text', 'below (94)', 'en particulier')
inv('Empty and total-set display', 'display', 'below en particulier', r'X_\phi^*=\phi')
inv('Introduction to (95)', 'text', 'left above (95)', 'On a')
inv('Display (95)', 'display', 'upper middle', r'(95), X_J^*')
inv('Middle canceled X in (95)', 'deletion', 'middle of (95)', r'\deleted{X}_{\bar J}')
inv('Right marginal closed-case note', 'margin note', 'right of (95), four lines', 'en particulier si J fermé')
inv('Connective before (96)', 'text', 'left above (96)', 'et')
inv('Display (96)', 'display', 'middle', '(96), difference and underbrace J_0')
inv('Band paragraph', 'text', 'below (96), two lines', 'Si J est une bande')
inv('Condition introduction', 'text', 'above (97)', 'Si on a (Strat 5), alors')
inv('Display (97)', 'display', 'lower middle', '(97), closure and disjoint union')
inv('Density qualification', 'margin note', 'right below (97), slanting', 'moyennant densité')
inv('Dual statement', 'margin note', 'diagonal left margin beside (97) and following cancellations, five lines', 'dualement')
inv('Canceled dotted-X definition', 'deletion', 'below (97)', r'\dot X_J')
inv('Closedness discussion', 'text', 'lower main block, four lines', 'donc')
inv('Canceled expression after donc', 'deletion', 'first line of closedness discussion', r'\overline{X_J^*}')
inv('Final open-set sentence', 'text', 'above (98)', 'Si')
inv('Canceled letter before L', 'deletion', 'between Si and L', r'\unsure{A|B}')
inv('Raised closed-complement explanation', 'insertion', 'above final sentence, leader to before alors', r'i.e. J=I\setminus L fermé')
inv('Display (98) with right parenthetical', 'display', 'bottom main block, parenthetical in two short lines', '(98), complement formula')
inv('Canceled f in (98)', 'deletion', 'between est and ouvert', 'f')
inv('Later foliation', 'margin note', 'bottom left', '92', 'later thin grey hand, distinct from author')

def cb(name):
    return crops[name]['box']

second = []
def blind(kind, coords, reading):
    assert isinstance(reading, str) and reading
    second.append(dict(box=f'B{len(second)+1:02d}', kind=kind,
                       x0=coords[0], y0=coords[1], x1=coords[2], y1=coords[3], reading=reading))
blind('handwritten authorial number', [29,32,102,87], r'\mspage{43}')
blind('whole canceled formula', cb('head_canceled'), r'\deleted{X_J^*=X_{\bar J}}')
blind('C/H different words and complete opening, with headless assignment', cb('opening'), r'On a compatibilité de $J\mathrel{\mapstochar\relbar}X_J^*$ aux unions et intersections')
blind('whole numbered formula (94)', cb('formula94'), r'(94)\qquad\bigcup_\alpha X_{J_\alpha}^*=X_{\bigcup_\alpha J_\alpha}^*,\qquad\bigcap_\alpha X_{J_\alpha}^*=X_{\bigcap_\alpha J_\alpha}^*')
blind('whole formula with changed empty-set glyphs', cb('empty_first'), r'X_\phi^*=\phi,\quad X_I^*=X.')
blind('whole numbered formula (95), cancellation and uncertain relation', cb('formula95'), r'(95)\qquad X_J^*\unsure{\in|\subset}X_J=\deleted{X}_{\bar J}=X_{\bar J}^*')
blind('complete right marginal note', cb('margin95'), r'\margin{en particulier si $J$ fermé, on a $X_J=X_J^*$, et $X_J^*$ est fermé}')
blind('whole numbered formula (96) including J_0 underbrace', cb('formula96'), r'(96)\qquad X_J^*=X_{\bar J}^*\setminus X_{\underbrace{\bar J\setminus J}_{J_0}}^*')
blind('prose including handwritten subscript zero', [252,1057,1499,1277], r'Si $J$ est une bande, $J_0$ est fermé donc $X_J^*$ est loc. fermé.')
blind('condition numeral and C/H differing words', cb('strat5'), 'Si on a (Strat 5), alors')
blind('whole numbered formula (97)', cb('formula97'), r'(97)\qquad\overline{X_J^*}=X_J\ (=X_{\bar J}^*)=X_J^*\amalg X_{\bar J\setminus J}^*')
blind('complete density margin note and underline', cb('density'), r'\margin{moyennant \uline{densité}}')
blind('complete diagonal marginal statement with resolved C index', cb('margin_dual'), r'\margin{dualement $X_{\widetilde J}^*$ est le plus petit sous-ens. de $X$ saturé de la forme $X_?^*$, qui soit ouvert et contienne $X_J^*$}')
blind('whole canceled dotted formula and below-high-confidence definition label', cb('canceled_dot'), r'\deleted{\dot X_J\overset{\mathrm{def}}=\overline{X_J^*}\setminus X_J^*}')
blind('whole uncertain canceled expression and live first-line continuation', cb('donc_canceled'), r'donc $\deleted{\unsure{\overline{X_J^*}=X_J^*}}$ $X_J^*$ est fermé i.e.')
blind('closedness continuation, empty signs and unstopped strat', cb('closed_continuation'), r'égal à $\overline{X_J^*}$ $(=X_{\bar J}^*)$ ssi $X_{\bar J\setminus J}^*=\phi$ i.e. si les $X_i^*$ $(i\in\bar J\setminus J)$ sont vides, i.e. (si strat est fidèle) \uuline{ssi} $\bar J\setminus J=\phi$ i.e. $J=\bar J$ i.e. $J$ fermé.')
blind('complete final prose with canceled letter and raised insertion attachment', cb('lower_insertion'), r'Si \deleted{\unsure{A|B}} $L\subset I$ est ouvert, \inserted{i.e. $J=I\setminus L$ fermé} alors')
blind('whole numbered formula (98), canceled f and two-line parenthetical', cb('formula98'), r'(98)\qquad X_L^*=\complement_X X_J^*\text{ est }\text{\deleted{f}}\text{ ouvert}\qquad\left(\begin{gathered}\text{si }L\subset I\\\text{est ouvert}\end{gathered}\right)')
blind('later handwritten foliation', cb('folio92'), r'\margin{92}')

record = dict(
    page=page, cote='150', scan='93', reader='reader_a; GPT-6 Astra Pro; effort not exposed; run SP92',
    line_count=35,
    line_count_note='35 writing baselines: 22 main baselines/displays (including the canceled opening and dotted-X displays, and counting the two-line parenthetical at (98) as one extra baseline), 1 raised insertion baseline, 10 marginal prose baselines (4 beside (95), 1 density note, 5 diagonal left-margin lines), and 2 foliation baselines. Formula subscripts and the underbrace label J_0 are parts of their display, not extra prose baselines.',
    half_review='Viewed the whole original once for layout, then both supplied native overlapping halves (0–1298 and 1062–2360). Read every line, agreed text, all mathematical terms and indices, numbers, abbreviations, marginal notes, strike bounds and insertion attachment. Then created and personally viewed all 25 saved crops. The canceled-dot and closed-continuation files were reframed upward and the final versions viewed; no OCR, external research, or TeX compilation was used.',
    deletion_insertion_review=[
        {'place':'Top canceled display', 'C':r'\deleted{\[X_J^*=X_{\bar J}\]}', 'state':'A continuous strike crosses both terms and their equality. All content retained as canceled; the right J has a real overbar.'},
        {'place':'Middle term of (95)', 'C':r'\deleted{X_{\bar J}}', 'state':'Physical extra strokes cross X only. J and its overbar remain uncrossed; candidate uses a canceled X with its subscript outside the deletion. The second equality is live.'},
        {'place':'Dotted-X definition', 'C':r'\deleted{\[\dot X_J\overset{\mathrm{déf}}=\overline{X_J^*}\setminus X_J^*\]}', 'state':'One large wavy cancellation covers the entire definition, including the equality. The left term has a dot and no star; the two right terms have stars. The bar over the first right term belongs to its closure. The definition label is transcribed def without a supplied accent.'},
        {'place':'After donc', 'C':r'\deleted{$\unsure{\overline{X_J^*}=X_J^*}$}', 'state':'Heavy zigzag cancels the full old expression, stopping before the separate live X_J^* est fermé. C’s expression stays uncertain because the relation and terminal subscript cannot be wholly separated from the strike.'},
        {'place':'Between final Si and L', 'C':r'\deleted{\unsure{A}}', 'state':'An isolated old letter is canceled; A is retained first and B admitted as a narrow alternative. The neighboring L and inclusion are live.'},
        {'place':'Raised i.e. J=I setminus L fermé clause', 'C':r'\inserted{i.e. $J=I\setminus L$ fermé,}', 'state':'The clause is above the final sentence. A long leader curves down into the gap before alors. It is an insertion after est ouvert, not an underline of fermé or a parenthesis. The right upturn is continuous with that leader, so the comma supplied after fermé by both witnesses is removed; the baseline comma after ouvert remains.'},
        {'place':'In (98) between est and ouvert', 'C':r'\deleted{\unsure{f}}', 'state':'One canceled f precedes the live ouvert. The tight crop separates its upper loop and descending stem from the crossing stroke; the uncertainty is resolved at medium confidence.'}
    ],
    changes=changes, diff_coverage=coverage,
    decisions=[dict(id='M0720', cote='150', scan='93', decision='first', reading='?',
        ink='A question-mark hook with detached low dot is plainly present in the rotated detail; it is the author’s literal question mark, not an editorial doubt sign or J prime. The complete marginal formula and prose were also read.',
        crop=crops['margin_index']['crop'], box=cb('margin_index'), confidence='high')],
    inventory=inventory,
    notes=r'''## Page 150_scan093 (authorial 43)

The page states that the assignment from J to the starred X_J respects unions and intersections, then gives the empty and total-set cases. It relates the starred set to the unstarred X_J and the starred set indexed by barred J, expresses a difference using J_0, and says that a band gives a locally closed starred set. Under (Strat 5), formula (97) identifies a closure and writes a disjoint decomposition; the nearby marginal qualifier says “moyennant densité,” with densité underlined once. The following paragraph discusses when the starred set is closed, adding faithfulness in the final equivalence. Formula (98) gives the open complement case. These are descriptions of the page’s claims, not a verification of them.

### Mathematics-directed rereading

- The opening assignment has a short upright tail bar and a blunt right end. There is no arrowhead. Both witnesses supply one through mapsto; the candidate uses standard mapstochar plus relbar to preserve the headless sign in running mathematical text.
- Read the whole of (94), not merely the first term on the intersection side: the first intersection-side X has a small high star and the alpha remains attached beneath J. No new prime, numeral, or index was supplied.
- Read all of (95) and a tight view of its heavily retraced relation. A central-looking bar makes membership plausible, but a thick retracing of inclusion cannot be excluded. The candidate retains \unsure{\in|\subset}; adding this doubt alone is not a correction row. The canceled old X is followed by an uncrossed barred J and then another live equality. That physical cancellation scope is preserved even if the whole abandoned term was intended to be superseded.
- Read all of (96), including the two sloping set-difference strokes, the underbrace, and its handwritten zero. The following prose repeats J_0. No formula was regularized.
- Read all of (97), its closure bar, each star and subscript, the disjoint-union sign, and both marginal qualifications. The left marginal statement has a tilde over J in its first formula. Its later subscript is a literal question mark, visibly a hook and low dot; it records the author’s own unspecified index. M0720 is therefore resolved to C’s first reading. No J prime was substituted.
- The diagonal marginal words are readable after rotation. The large horizontal (97) that H includes amid them belongs only to the main display. The marginal note says dualement, est le plus petit sous-ens., saturé, and qui soit ouvert et contienne, in that order.
- Read the entire canceled dotted-X definition. The left X has a dot and no star. Both right-hand terms have stars; the first has a closure bar. The definition label has visible d/e/f but no separate accent, so the short form def is preserved at medium confidence. The cancellation is a genuine strike, not a drawing.
- The smaller canceled expression after donc remains uncertain. The first barred, starred X_J survives; the tail has short relation-like strokes and a second X, but its relation and final subscript are intertwined with the zigzag. The candidate retains C’s provisional complete expression under \unsure rather than declaring every symbol recovered. The possibility of wordlike strokes in the middle cannot be excluded.
- Four empty-set signs have a small loop and long axial descender: two in the unnumbered display and two in the closedness paragraph. They are transcribed \phi as written. The loop is not replaced by a modern empty-set glyph.
- Read the whole of (98), including the complement subscript X, both stars, the canceled f, and the two-line parenthetical at the right. The visible subset signs in the final prose and parenthetical are clean small C shapes; they do not settle the differently retraced relation in (95).

### Revision, hand and layout

The raised i.e. clause is connected by a leader to the gap before alors in the final sentence. The leader is not an underline or a parenthesis. Its continuous right upturn is not a comma after fermé; that shared witness punctuation is removed, while the separate baseline comma after ouvert remains. The canceled letter after Si remains narrowly A/B; the canceled f before ouvert is resolved from its upper loop and descender. The old equality after donc remains uncertain. Every C deletion/insertion was inspected, including the scope of the mid-(95) strike.

The author leaves strat unstopped in the lower prose, whereas loc. and sous-ens. have stops; i.e. is stopped and ssi is unexpanded. The final ssi has two independent underlines. Reduced à in égal à has the familiar small two-mark appearance. No grammatical or mathematical agreement was silently repaired.

There is no title or date. The dark upper-left 43 is the authorial page number. The thin grey 92 at the lower left is another hand’s foliation and is retained in a margin macro. There is no genuine diagram or drawing on this page: all crossed forms are mathematical writing or cancellation strokes. H’s source-bearing quoted density note is kept as the marginal source phrase; its descriptions of page position, continuation and underlining are editorial and are not copied into the transcription.

No mathematical validity check, proof, computation or theorem use was performed by reader_a for this page. check_events is empty. Whole-formula rereading served only to locate and read ink.''',
    check_events=[],
    notation=[
        {'sign':r'\mathrel{\mapstochar\relbar}', 'reading':'headless assignment shaft with upright tail', 'evidence':'Opening J to starred X: short left upright, horizontal shaft, blunt right cap and no arrowhead strokes.'},
        {'sign':r'\phi', 'reading':"ϕ : l'ensemble vide", 'evidence':'All four occurrences have small loops on long axial descenders; the first two are in the unnumbered display and the last two in the closedness paragraph.'},
        {'sign':'?', 'reading':'literal question-mark subscript', 'evidence':'Diagonal margin, de la forme X: hook-shaped head and detached low dot. M0720 is not J prime.'},
        {'sign':r'\dot X_J', 'reading':'dotted X_J without star', 'evidence':'Left term of the canceled definition has a dot above the center, no independent high-right star; its two right terms do have stars.'},
        {'sign':r'\unsure{\in|\subset}', 'reading':'unsettled retraced relation in (95)', 'evidence':'Three apparent horizontal levels, with lower ink merged by retracing; clean final subset forms cannot decide this instance.'},
        {'sign':'def', 'reading':'unaccented unstopped definition label', 'evidence':'Canceled definition label, upward-reframed crop, visible d/e/f with no detached accent.'}
    ],
    hand_log=[
        {'habit':'A tail-marked horizontal assignment may have no arrowhead.', 'places':['Opening J to starred X'], 'scope':'One occurrence on this leaf; the endpoints are inspected individually.', 'witness_errors':'Both C and H supply an arrowhead with mapsto.'},
        {'habit':'A very small star may collapse to a two-lobed dark mark.', 'places':['(94), first X on intersection side','(98), right X'], 'scope':'Several stars on this leaf; confirm individually, not every dot is a star.', 'witness_errors':'No new error at (94); H adds a star to the dotted left term of the canceled definition where the high-right area has no independent star.'},
        {'habit':'Phi-shaped empty-set signs may be strongly slanted while retaining their long axial descender.', 'places':['Unnumbered empty/total-set display, twice','Closedness paragraph, twice'], 'scope':'All four empty-set occurrences on this leaf.', 'witness_errors':'C uses varnothing and H emptyset; the written phi shape is retained.'},
        {'habit':'A question mark used as an index has a low detached dot, unlike angular J or a high prime.', 'places':['Diagonal margin, de la forme X'], 'scope':'One occurrence on this leaf.', 'witness_errors':'C offers J prime as alternative; tight detail resolves its first reading ?.'},
        {'habit':'A long curved insertion leader can resemble an underline, opening parenthesis or final comma.', 'places':['Raised clause above final sentence'], 'scope':'One clear leader here.', 'witness_errors':'C and H attach the clause correctly but both transcribe its continuous right upturn as a comma after fermé.'},
        {'habit':'Short forms have occurrence-specific punctuation.', 'places':['strat in lower paragraph','loc. below (96)','sous-ens. in left margin','def in canceled definition'], 'scope':'Only the observed occurrences are asserted.', 'witness_errors':'H adds a stop after strat; C and H supply an accent in the definition label.'}
    ],
    abbreviations=[
        {'form':'loc.', 'expansion':'localement'},
        {'form':'i.e.', 'expansion':'id est'},
        {'form':'ssi', 'expansion':'si et seulement si'},
        {'form':'sous-ens.', 'expansion':'sous-ensemble'},
        {'form':'strat', 'expansion':'stratification'},
        {'form':'def', 'expansion':'définition'}
    ],
    doubts=[
        {'place':'(95), relation between starred X_J and X_J', 'reading':r'\unsure{\in|\subset}', 'alternatives':[r'\in',r'\subset'], 'confidence':'medium', 'reason':'A separate-looking middle level favors membership, but thick lower retracing could be a repeated inclusion curve. This is a newly added doubt, not a settled correction.'},
        {'place':'Canceled expression after donc', 'reading':r'\unsure{\overline{X_J^*}=X_J^*}', 'alternatives':[r'\overline{X_J^*}=X_J^*','a wordlike middle and partially obscured second X term'], 'confidence':'low', 'reason':'The cancellation covers the middle relation and the second subscript; not every stroke can be separated. Retains C’s provisional reading, unresolved.'},
        {'place':'Canceled letter after final Si', 'reading':r'\unsure{A|B}', 'alternatives':['A','B'], 'confidence':'low', 'reason':'Top and bottom crossings overlap a tall left side and right loops; neither capital is safe enough to resolve the canceled ink.'}
    ],
    second_boxes=second,
    crops=[dict(name=k, **v, viewed_by_reader=True) for k,v in crops.items()]
)

allowed = {'misread word','misread symbol or index','omission','text not on the page',
           'deletion state (struck given live or live given struck)','insertion or placement',
           'abbreviation expanded or spelling modernised',r'readable ink left as \ill{}',
           'drawing or diagram','other'}
assert all(row['kind'] in allowed for row in changes)
assert len(coverage) == len(packet['differences']) == len({d['diff_id'] for d in coverage})
assert {d['diff_id'] for d in coverage} == {d['diff_id'] for d in packet['differences']}
assert [d['id'] for d in record['decisions']] == [m['id'] for m in packet['marks']]
assert all((work / c['crop']).exists() for c in changes)
assert all(0 <= b['x0'] < b['x1'] <= packet['size'][0] and 0 <= b['y0'] < b['y1'] <= packet['size'][1] for b in second)
assert all(b['reading'] in tex for b in second)
out = work / 'records' / f'{page}.json'
out.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'page':page,'changes':len(changes),'crops':len(crops),'diff_coverage':len(coverage),'decisions':len(record['decisions']),'inventory':len(inventory),'second_boxes':len(second),'doubts':len(record['doubts'])}))
