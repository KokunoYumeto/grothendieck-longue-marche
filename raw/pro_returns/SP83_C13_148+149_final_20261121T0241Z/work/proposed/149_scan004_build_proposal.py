from pathlib import Path
import json

BASE = Path('/workspace/scratch/f28c4f52d3ec')
PAGE = '149_scan004'
manifest = json.loads((BASE/'proposed/149_scan004_crop_manifest.json').read_text())
boundary_path = BASE/'proposed/149_scan004_boundary_manifest.json'
boundary = json.loads(boundary_path.read_text())
boundary['viewed'] = True
boundary['viewed_by'] = 'reader_b through tools.view_image; successfully displayed once'
boundary_path.write_text(json.dumps(boundary, ensure_ascii=False, indent=2)+'\n')
CROPS = {c['place']: {'crop': 'crops/'+Path(c['path']).name, 'box': c['box']} for c in manifest['crops']}
CROPS['footer_full'] = {'crop': 'crops/'+Path(boundary['path']).name, 'box': boundary['box']}

S = r'\unsure{\deleted{\prime}|*}'
F1 = r"B_{K'}-B_{K^{"+S+r'}}'
F2 = r"\Pi_{K'}\longrightarrow\Pi_{K^{"+S+r'}}.'
F3 = r"E_{\bar K'/K'}-E_{\bar K^{"+S+r'}/K^{'+S+r'}}'
PI = r'\Pi_{K^{'+S+r'}}'
KBAR = r'\bar K^{'+S+r'}'
SEP = r'\unsure{sép|\deleted{sép}}'

opening = r"i.e. un hom de schémas $\operatorname{Spec}K' - \operatorname{Spec}K$, on a un morphisme de Topos correspondant"
closure = r"Ceci s'explicite en disant qu'un \deleted{clôture} objet de $\Pi_{K'}$ (i.e. pt. de $B_{K'}$, ou rev. universel de $B_{K'}$, \deleted{)} ou clôture sép.\inserted{$\bar K'$} de $K'$)"
definition = r'en définit un de $'+PI+r'$ (associé, on prend $'+KBAR+r'=$ clôture \inserted{alg} '+SEP+r" de $K$ dans $\bar K'$)"
groups = r"et pour deux pts correspondants, on a un hom de groupes fondamentaux correspondants, qui s'interprète p.ex."
restriction = r"et qui permet de réconstituer l'hom. de topos comme une ``restriction des scalaires''."
footer = r"L'image de (3) est le sous-groupe fermé de $E_{\bar K/K}$ qui correspond à la sous-extension"
tex = '\n'.join([
    r'\scanpage{4}', opening, r'\[', r'(1)\qquad '+F1, r'\]',
    'associé à un hom de groupoïdes fond.', r'\[', r'(\unsure{2|1})\qquad '+F2, r'\]',
    closure+' '+definition+' '+groups+' comme', r'\[', r'\unsure{(3)|3)}\qquad '+F3, r'\]',
    restriction, '', r'\margin{\unsure{1}}', footer, r'\margin{3}', ''
])
(BASE/'proposed'/f'{PAGE}.tex').write_text(tex)

changes = []
def change(place, c, h, final, dc, dh, kind, error, evidence, crop, confidence='high', marked=False, consequential=False):
    changes.append({'id': f'{PAGE}-{len(changes)+1:02d}', 'place': place,
                    'c': c, 'h': h, 'final': final, 'diff_c': dc, 'diff_h': dh,
                    'kind': kind, 'error_kind': error, 'evidence': evidence,
                    **CROPS[crop], 'confidence': confidence,
                    'marked_in_h': marked, 'consequential': consequential})

change('Opening, Spec map', r"\operatorname{Spec}K' - \operatorname{Spec}K", r"\operatorname{Spec} K' \to \operatorname{Spec} K",
       r"\operatorname{Spec}K' - \operatorname{Spec}K", False, True,
       'misread symbol or index', 'Symbols and indices',
       'The entire shaft is visible between the two Spec expressions. Its right end is a blunt thickened downward nib; there is no separable chevron or second oblique branch. The source prime and both capital K letters are clear. The literal horizontal stroke is retained.', 'opening')
change('Opening, morphisme de Topos', 'Topos', 'topos', 'Topos', False, True,
       'misread word', 'Words',
       'The initial T has a tall upright and a broad curved crossbar well above the lower-case opos. The later de topos in the reconstruction sentence has a different lower-case initial.', 'opening')
change('Display (1), map shaft', r'\unsure{-|\longrightarrow}', r'\longrightarrow', '-', False, True,
       'misread symbol or index', 'Symbols and indices',
       'The complete B-to-B display has a single horizontal shaft with a thick rounded terminal and a small downward nib, without an independently drawn arrowhead. This resolves C to its first alternative; the row records H\'s different arrow reading.', 'formula1')

clusters = [
    {'place': 'Display (1), target K superscript', 'crop': 'formula1',
     'c': r'B_{K^{\deleted{\unsure{\prime}}}}', 'h': r'B_{K^{*}}', 'final': r'B_{K^{'+S+r'}}',
     'whole': r'(1)\qquad '+F1,
     'ink': 'A short dark upright is joined by angular upper and lower hooks. The cluster is more than a plain prime, but neither the original stroke beneath a cancellation nor a deliberately live star is securely separable.'},
    {'place': 'Display (2), target K superscript', 'crop': 'formula2',
     'c': r'\Pi_{K^{\deleted{\unsure{\prime}}}}', 'h': r'\Pi_{K^{*}}', 'final': PI,
     'whole': r'(\unsure{2|1})\qquad '+F2,
     'ink': 'A dark descending stub has a compact curved cross at its upper end and a short oblique to the left. The arms do not securely establish either an intentional star or a cancelled earlier prime.'},
    {'place': 'Inline Pi after en définit un de, target K superscript', 'crop': 'definition',
     'c': r'\Pi_{K^{\deleted{\unsure{\prime}}}}', 'h': r'\Pi_{K^{*}}', 'final': PI,
     'whole': PI,
     'ink': 'The small raised group beside K contains two oblique strokes and a dark central return. Its star-like outline is visible, but the crossing order and the survival of an underlying prime are not recoverable.'},
    {'place': 'Closure definition, K-bar superscript', 'crop': 'definition',
     'c': r'\bar K^{\deleted{\unsure{\prime}}}', 'h': r'\overline{K}^{*}', 'final': KBAR,
     'whole': KBAR+r'=$ clôture \inserted{alg} '+SEP+r" de $K$ dans $\bar K'",
     'ink': 'The bar over K is separate and clear. To its right a small upright has a hooked lower end and an overworked upper curl; the cluster cannot be decomposed confidently into a cancelled prime or a live star.'},
    {'place': 'Display (3), target numerator K-bar superscript', 'crop': 'formula3',
     'c': r'\bar K^{\deleted{\unsure{\prime}}}', 'h': r'\overline{K}^{*}', 'final': KBAR,
     'whole': r'\unsure{(3)|3)}\qquad '+F3,
     'ink': 'The numerator K has a distinct upper bar. Beside it two short acute diagonals and a small dark triangular return overlap the raised stroke. The resulting cluster does not establish its live or cancelled state.'},
    {'place': 'Display (3), target denominator K superscript', 'crop': 'formula3',
     'c': r'K^{\deleted{\unsure{\prime}}}', 'h': r'K^{*}', 'final': r'K^{'+S+r'}',
     'whole': r'\unsure{(3)|3)}\qquad '+F3,
     'ink': 'The denominator K has no upper bar. Its raised mark is a slender downward stroke with an angular dark cross at the top, distinct from the numerator cluster but equally insufficient to settle prime cancellation versus live star.'},
]
def cluster_change(index):
    cl = clusters[index]
    change(cl['place'], cl['c'], cl['h'], cl['final'], False, True,
           'deletion state (struck given live or live given struck)', 'Struck text',
           cl['ink']+' C\'s cancelled-prime possibility remains first; H\'s live-star possibility is explicitly retained. The new state doubt is not counted as a changed reading against C.',
           cl['crop'], 'low', True, False)
cluster_change(0)
cluster_change(1)
change('After universel de B_K-prime, cancelled closing parenthesis', r'\deleted{)}', 'absent', r'\deleted{)}', False, True,
       'omission', 'Omissions',
       'Immediately after the comma following B with K-prime, a separate tall curved closing parenthesis is crossed at its upper and middle parts. Its lower curved return survives. It is distinct from the following ou and remains cancelled.', 'closure')
cluster_change(2)
change('Parenthesis after inline Pi, associé / ainsi', 'associé', 'ainsi', 'associé', False, True,
       'misread word', 'Words',
       'After the opening parenthesis the compact initial a is followed by a run of low s/o/c strokes and an accented terminal ending. The final low turn and detached upper accent support associé rather than the final dotted i of ainsi. The comma is separately visible.', 'definition')
cluster_change(3)
change('Raised alg, terminal punctuation', r'\inserted{alg}', r'\add{alg.}', r'\inserted{alg}', False, True,
       'text not on the page', 'Text that is not on the page',
       'The raised a, looped l and descending g are visible. The curved stroke to their right continues downward as the attachment leader; no independent point follows g. The letters remain raised and live.', 'definition')
change('Second sép in the closure definition, cancellation state', 'sép', r'\struck{sép.}', SEP, False, True,
       'deletion state (struck given live or live given struck)', 'Struck text',
       'The s, e and long p are heavily retraced. No independent straight stroke can be followed through the complete word; the nearby large curve belongs to the raised alg attachment. Live sép remains first, while the possible cancellation is retained explicitly. This is a state uncertainty, not a proven removal of sép.', 'definition', 'medium')
change('Second sép in the closure definition, terminal punctuation', 'sép', r'\struck{sép.}', SEP, False, True,
       'text not on the page', 'Text that is not on the page',
       'After the dark descending p there is a blank before de; no independent terminal point is visible. The uncertainty about a strike is recorded separately and does not create a period. The first sép. higher on the page does have a separate visible point.', 'definition')
change('Corresponding-points paragraph, hom de groupes', 'des', 'de', 'de', True, False,
       'misread word', 'Words',
       'The d has a tall stem and small lower loop, followed by a low e exit. There is no additional s turn before the wide gap and the descending g of groupes. The short final downward nib belongs to the e exit.', 'groups')
change('Display (3), map shaft', r'\unsure{-|\longrightarrow}', r'\longrightarrow', '-', False, True,
       'misread symbol or index', 'Symbols and indices',
       'The full E-to-E expression shows one horizontal line ending in a short dark downward nib. There is no second oblique branch or detached chevron. It matches the visibly blunt shaft in display (1), while display (2) has a separate head. C resolves to its first alternative.', 'formula3')
cluster_change(4)
cluster_change(5)
change('Reconstruction sentence, written accent', 'reconstituer', 'reconstituer', 'réconstituer', True, True,
       'abbreviation expanded or spelling modernised', 'Abbreviations expanded, spelling modernised',
       'A separate short slanted stroke lies above the initial e in the r-e group, around original x1040,y1859. It is detached from the preceding de and from the displayed formula above. The written accent is retained; the rest of reconstituer is clear.', 'restriction')
change('Restriction des scalaires, quotation form', "``restriction des scalaires''", '« restriction des scalaires »', "``restriction des scalaires''", False, True,
       'misread symbol or index', 'Symbols and indices',
       'The opening quotation consists of two small elevated strokes before restriction, and the closing quotation has two elevated short strokes after scalaires. They are not lateral angle-shaped guillemets. The final full stop lies separately on the baseline.', 'restriction')
change('Left of final paragraph, marginal vertical annotation', r'\margin{\unsure{1}}', 'absent', r'\margin{\unsure{1}}', False, True,
       'omission', 'Omissions',
       'A separate dark nearly upright stroke stands well left of L\'image. Its upper part is thin and its lower end thickens slightly, without a secure numeral entry or basal foot. The ink is retained as the doubtful 1 of C rather than omitted.', 'footer_full', 'low')
change('Lower left folio', r'\margin{3}', 'absent', r'\margin{3}', False, True,
       'omission', 'Omissions',
       'The pale bottom annotation has two open right-hand lobes joined at a narrowed middle, with a curved lower foot: 3. Its physical position is separate from the dark margin stroke beside the last paragraph. The writer is not identified from appearance.', 'folio')

decisions = [
    {'id': 'M0952', 'decision': 'first', 'reading': '-',
     'evidence': 'The whole first displayed formula is visible. Its shaft has a blunt thickened right terminal and no independent arrowhead; resolve the first, minus-like stroke reading.', **CROPS['formula1'], 'confidence': 'high'},
    {'id': 'M0953', 'decision': 'first', 'reading': r'\longrightarrow',
     'evidence': 'A separate short right-pointing chevron sits just beyond the horizontal shaft. Both source and target Pi expressions and the final full stop were read together; the detached head distinguishes this from the other two shafts.', **CROPS['formula2'], 'confidence': 'high'},
    {'id': 'M0954', 'decision': 'first', 'reading': 'on',
     'evidence': 'The first letter is a small closed dark oval, followed by a long low n run. There is no open e entry. The comma before it and the following prend on the next row are distinct.', **CROPS['definition'], 'confidence': 'high'},
    {'id': 'M0955', 'decision': 'first', 'reading': '-',
     'evidence': 'The full third displayed formula shows a horizontal shaft with a dark short downward nib at the right, but no separate arrowhead branch. Both target superscripts remain doubtful independently.', **CROPS['formula3'], 'confidence': 'high'},
    {'id': 'M0956', 'decision': 'undecided', 'reading': r'\margin{\unsure{1}}',
     'evidence': 'The isolated dark vertical mark is real ink. Its narrow top and thick lower end do not distinguish a numeral 1 from a paragraph/reference stroke. No entry hook or basal foot is securely visible.', **CROPS['footer_full'], 'confidence': 'low'},
]

implicit = []
doubts = []
for i, cl in enumerate(clusters, 1):
    whole = cl['whole']
    if i == 4:
        whole = definition
    implicit.append({'id': f'{PAGE}-I{i:02d}', 'place': cl['place'],
                     'c_mark': r'\deleted{\unsure{\prime}}', 'decision': 'undecided',
                     'reading': whole, 'evidence': cl['ink'], **CROPS[cl['crop']], 'confidence': 'low'})
    doubts.append({'place': cl['place'], 'reading': whole,
                   'alternatives': 'A cancelled prime, or a live asterisk; both its underlying glyph and its live/cancelled state remain open.',
                   'confidence': 'low', 'reason': cl['ink']})
doubts += [
    {'place': 'Display (2), numeral in label', 'reading': r'(\unsure{2|1})\qquad '+F2,
     'alternatives': '2 or 1; the surrounding parentheses are clear.', 'confidence': 'medium',
     'reason': 'The digit has a hooked upper entry and short downward stroke but no securely separate basal foot. It differs from the straight diagonal 1 in the first label, without settling the digit. This added certainty-only doubt does not count as a material change.'},
    {'place': 'Display (3), opening parenthesis of label', 'reading': r'\unsure{(3)|3)}\qquad '+F3,
     'alternatives': '(3) or 3); the right parenthesis is clear.', 'confidence': 'medium',
     'reason': 'The compact 3-like run at the left has overlapping curved strokes, and an independent opening parenthesis cannot be securely separated. The 3 reading remains; only its opening punctuation is uncertain. This is certainty-only.'},
    {'place': 'Second sép in the closure definition', 'reading': definition,
     'alternatives': 'Live sép or cancelled sép; neither alternative has a terminal point.', 'confidence': 'medium',
     'reason': 'The retraced letters admit a possible strike, but no independent cancellation through the entire word can be traced. The curved alg leader does not by itself establish cancellation.'},
    {'place': 'Dark left margin annotation beside final paragraph', 'reading': r'\margin{\unsure{1}}',
     'alternatives': 'Numeral 1 or an unlabelled upright paragraph/reference stroke.', 'confidence': 'low',
     'reason': 'The mark is a single tapering upright without a secure numeral head or foot; it is retained rather than interpreted from paragraph function.'},
]

inventory = []
def inv(kind, position, words, hand='his hand'):
    inventory.append({'element': f'E{len(inventory)+1:02d}', 'sheet_kind': 'text', 'hand': hand,
                      'kind': kind, 'position': position, 'first_words_or_objects': words, 'transcribed': 'yes'})
inv('text', 'Upper three prose rows', opening)
inv('display', 'First display, including label (1)', r'(1)\qquad '+F1)
inv('deletion', 'First display target, possible cancelled raised stroke; state not settled', r'K^{'+S+r'}')
inv('text', 'Prose row between displays (1) and (2)', 'associé à un hom de groupoïdes fond.')
inv('display', 'Second display, including doubtful numeral and final point', r'(\unsure{2|1})\qquad '+F2)
inv('deletion', 'Second display target, possible cancelled raised stroke; state not settled', r'K^{'+S+r'}')
inv('text', 'Opening main clause after second display', "Ceci s'explicite en disant qu'un")
inv('deletion', 'End of Ceci row', r'\deleted{clôture}')
inv('text', 'Object/point/universal-cover/closure description, following two rows', r"objet de $\Pi_{K'}$ (i.e. pt. de $B_{K'}$, ou rev. universel de $B_{K'}$ ...")
inv('deletion', 'After comma following universel de B_K-prime', r'\deleted{)}')
inv('insertion', 'Raised above gap after the first sép.', r"\inserted{$\bar K'$}")
inv('text', 'Two rows defining the corresponding closure', definition)
inv('deletion', 'Inline Pi target, possible cancelled raised stroke; state not settled', PI)
inv('deletion', 'K-bar in closure definition, possible cancelled raised stroke; state not settled', KBAR)
inv('insertion', 'Raised above the second closure adjective', r'\inserted{alg}')
inv('deletion', 'Second sép, possible cancellation; live state leads', SEP)
inv('text', 'Corresponding points and fundamental groups, three rows plus comme', groups+' comme')
inv('display', 'Third display, including uncertain opening label parenthesis', r'\unsure{(3)|3)}\qquad '+F3)
inv('deletion', 'Third display target numerator, possible cancelled raised stroke; state not settled', KBAR)
inv('deletion', 'Third display target denominator, possible cancelled raised stroke; state not settled', r'K^{'+S+r'}')
inv('text', 'Three rows after third display', restriction)
inv('margin note', 'Dark upright left of final paragraph', r'\margin{\unsure{1}}', 'unnamed hand (marginal annotation; attribution uncertain)')
inv('text', 'Final two prose rows, unfinished at source edge', footer)
inv('margin note', 'Pale bottom-left folio annotation', r'\margin{3}', 'unnamed hand (folio annotation; attribution uncertain)')

notes = [
    {'id': PAGE+'-N01', 'text': 'The page continues with a map of spectra and corresponding maps of étale topoi and fundamental groupoids. The opening Spec stroke and the strokes in displays (1) and (3) are visibly blunt horizontal lines; only display (2) has a separable right head. Their literal forms are preserved without supplying arrowheads from the mathematical context.'},
    {'id': PAGE+'-N02', 'text': 'The main paragraph describes a point of B_K-prime, a universal covering, or a separable closure, and describes a corresponding closure of K inside K-bar-prime. The six overworked raised marks are all retained with cancelled-prime/live-star alternatives. No relation between them is proved by their repetition, and no mathematical convention is used to settle their ink state.'},
    {'id': PAGE+'-N03', 'text': 'The text asserts that the associated homomorphism of fundamental groups reconstructs the homomorphism of topoi as a restriction des scalaires. This global reconstruction assertion is transcribed as background; this reader did not prove it or identify the relative closure independently.'},
    {'id': PAGE+'-N04', 'text': 'The final paragraph begins to identify the image of (3) as a closed subgroup corresponding to a subextension, but the clause ends at sous-extension at the lower/right source edge. No continuation or terminal period is supplied. The literal E index there is K-bar/K, without the six overworked marks found above.'},
    {'id': PAGE+'-N05', 'text': 'Main-reader targeted proof check, actually reported in this run: for a group homomorphism h:E-prime to E and an E-action on X, define g-prime acting on x by h(g-prime) acting on x. The identity acts trivially because h(1)=1; the action law follows from h(g-prime k-prime)=h(g-prime)h(k-prime). This verifies only the action-level restriction construction behind the source phrase. It does not verify reconstruction of the étale morphism, identify the closure, or decide any written superscript.'},
    {'id': PAGE+'-N06', 'text': 'The ink gives capital Topos in the opening, de groupes, and an explicit detached accent in réconstituer. The quoted phrase has paired elevated quotation strokes rather than guillemets. Raised alg has no separate terminal point; the second sép has no separate terminal point and its cancellation state remains open. The first sép. has a clear point and is retained live.'},
    {'id': PAGE+'-N07', 'text': 'All handwritten numbering was checked: the first display label is (1); the second remains (2|1); the third has a clear right parenthesis but uncertain separate opening parenthesis; the final prose reference reads (3). A distinct dark upright at the final paragraph is retained as unsure 1. The lower pale folio is 3, with writer attribution left uncertain.'},
    {'id': PAGE+'-N08', 'text': 'First-reading protocol: the original was displayed once for layout and each prepared half once for a line-by-line reading. Twenty-one principal text/formula baselines were read, with the interlinear additions and marginal marks inspected separately. All witness agreements, bars, primes, indices, punctuation and revision scopes were checked against the ink. Ten distinct evidence places produced ten initial PNG crops; one footer boundary completion was added to recover the full ascenders and the entire source right edge. All eleven canonical PNG versions were successfully displayed by reader_b and reported viewed by the main reader. The prior footer remains unchanged. No original or half was reopened; no OCR, web search, TeX compilation or blind second reading was performed. Canonical evidence PNGs, manifests and generators are retained.'},
    {'id': PAGE+'-N09', 'text': 'H\'s editorial note about the second label and the superscripts is not source text. Macro names, bar/overline syntax and ordinary layout differences are excluded from material collation. Added certainty-only doubts in the second numeral, the opening parenthesis of the third label, and the state alternatives are recorded separately; the changes rows for disputed states record the actual C/H disagreement, not an invented resolution.'},
]
check_events = [
    {'statement_id': PAGE+'-N01', 'type': 'carried as background without fault found', 'outcome': 'The source presentation of spectra/topos/groupoid maps was transcribed. No construction theorem was proved in this first reading.'},
    {'statement_id': PAGE+'-N02', 'type': 'carried as background without fault found', 'outcome': 'The corresponding-closure description was read and its revisions inventoried; no independent field-theoretic verification was made.'},
    {'statement_id': PAGE+'-N03', 'type': 'carried as background without fault found', 'outcome': 'The asserted étale-topos reconstruction is retained as a source assertion. The separate action-level calculation does not certify this stronger statement.'},
    {'statement_id': PAGE+'-N04', 'type': 'carried as background without fault found', 'outcome': 'The unfinished image/subextension clause was preserved without completing or proving it.'},
    {'statement_id': PAGE+'-N05', 'type': 'targeted proof check', 'who': 'main reader', 'outcome': 'The main reader checked the identity and action law for restriction of a group action along a homomorphism. The result is limited to that action construction; it was not used to choose ink readings.'},
]
notation = [
    {'sign': r'- / \longrightarrow', 'meaning_or_form': 'A short horizontal map stroke may have only a blunt downward terminal; display (2) additionally has a separate right-pointing head.',
     'places': 'Opening Spec map and all three displays', 'universality': 'Each of the four map strokes was checked individually; only the Pi display has a separable head.',
     'witness_errors': 'H supplies arrows at all four positions. C preserves the first dash and doubts the three display strokes.'},
    {'sign': r'K^{\unsure{\deleted{\prime}|*}}', 'meaning_or_form': 'An overworked small raised cluster can be a cancelled prime or a deliberately live star; no secure layer decomposition.',
     'places': 'Targets of displays (1),(2); inline Pi and closure K-bar; both K letters in target of display (3)',
     'universality': 'Six separate occurrences, all individually inspected; their uncertainty is not resolved by repetition.',
     'witness_errors': 'C fixes cancellation state and doubts the underlying prime; H renders live stars. The proposed state alternatives retain both possibilities.'},
    {'sign': 'Topos / topos', 'meaning_or_form': 'The opening has a tall capital T with a broad curved crossbar; the later occurrence has a lower-case t.',
     'places': 'Opening morphisme de Topos; lower hom. de topos', 'universality': 'The two different local forms are preserved.', 'witness_errors': 'H lowercases the opening word.'},
    {'sign': 'réconstituer', 'meaning_or_form': 'A short detached accent lies above the initial e.', 'places': 'First row after display (3)',
     'universality': 'One occurrence on this sheet, checked directly; matches the supplied notation-log warning about written accents.', 'witness_errors': 'Both witnesses omit this accent.'},
    {'sign': 'de', 'meaning_or_form': 'A looped d joins a low e exit without an independent final s.', 'places': 'un hom de groupes',
     'universality': 'This disputed occurrence was inspected locally; no global de/des substitution is imposed.', 'witness_errors': 'C reads des; H preserves de.'},
    {'sign': 'Curved insertion leader', 'meaning_or_form': 'A curved attachment stroke descends from raised text to a baseline gap; it does not itself cancel neighbouring letters.',
     'places': 'Raised K-bar-prime after first sép.; raised alg before second sép', 'universality': 'Both local additions inspected separately.',
     'witness_errors': 'Both preserve the additions. H adds a point after alg and treats the neighbouring second sép as securely struck; the point is absent and state remains uncertain.'},
]
abbreviations = [
    {'form': 'i.e.', 'expansion': 'id est'},
    {'form': 'hom', 'expansion': 'homomorphisme'},
    {'form': 'hom.', 'expansion': 'homomorphisme'},
    {'form': 'fond.', 'expansion': 'fondamentaux'},
    {'form': 'pt.', 'expansion': 'point'},
    {'form': 'pts', 'expansion': 'points'},
    {'form': 'rev.', 'expansion': 'revêtement'},
    {'form': 'sép. / sép', 'expansion': 'séparable'},
    {'form': 'alg', 'expansion': 'algébrique'},
    {'form': 'p.ex.', 'expansion': 'par exemple'},
]
second = []
def unit(kind, crop, reading):
    x0,y0,x1,y1 = CROPS[crop]['box']
    second.append({'box': f'B{len(second)+1:02d}', 'kind': kind,
                   'x0': x0, 'y0': y0, 'x1': x1, 'y1': y1, 'reading': reading})
unit('different words', 'opening', opening)
unit('doubtful formula', 'formula1', r'\['+'\n'+r'(1)\qquad '+F1+'\n'+r'\]')
unit('doubtful formula', 'formula2', r'\['+'\n'+r'(\unsure{2|1})\qquad '+F2+'\n'+r'\]')
unit('struck passage', 'closure', closure)
unit('doubtful formula', 'definition', definition)
unit('different words', 'groups', groups)
unit('doubtful formula', 'formula3', 'comme\n'+r'\['+'\n'+r'\unsure{(3)|3)}\qquad '+F3+'\n'+r'\]')
unit('different words', 'restriction', restriction)
unit('margin note', 'footer_full', r'\margin{\unsure{1}}'+'\n'+footer)
unit('margin note', 'folio', r'\margin{3}')

record = {'page': PAGE, 'reader': 'reader_b', 'lines_read': 21, 'places_cropped': 10,
          'changes': changes, 'decisions': decisions, 'implicit_decisions': implicit, 'doubts': doubts,
          'inventory': inventory, 'notes': notes, 'check_events': check_events,
          'notation': notation, 'abbreviations': abbreviations, 'second_boxes': second}
(BASE/'proposed'/f'{PAGE}.json').write_text(json.dumps(record, ensure_ascii=False, indent=2)+'\n')
print(json.dumps({'page': PAGE, 'tex': str(BASE/'proposed'/f'{PAGE}.tex'),
                  'json': str(BASE/'proposed'/f'{PAGE}.json'),
                  **{key: len(record[key]) for key in ['changes','decisions','implicit_decisions','doubts','inventory','notes','check_events','notation','abbreviations','second_boxes']}}, indent=2))
