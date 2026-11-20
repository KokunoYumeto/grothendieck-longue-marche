from pathlib import Path
import json

root = Path(__file__).parent
reading = (root / 'reading.tex').read_text()
manifest = json.loads((root / 'crop_manifest.json').read_text())
crops = {item['id']: item for item in manifest}
low_start = reading.index(r'\makebox[0pt][l]{\hspace{-0.20em}')
low_end = reading.index(r'(K,\mathscr{N})\ .\tag*', low_start)
low_mark = reading[low_start:low_end]
pair_start = reading.index(r'\margin{\figure{\unsure{')
pair_end = reading.index('\n\nVu les significations', pair_start)
pair_mark = reading[pair_start:pair_end]

def decision(id, place, c_reading, final, diff_c, c_doubt, unresolved,
             alternatives, confidence, kind, scan_shows, bbox, crop_id):
    return dict(id=id, place=place, c_reading=c_reading, h_reading=None,
                reading=final, diff_c=diff_c, diff_h=False, c_doubt=c_doubt,
                unresolved=unresolved, alternatives=alternatives,
                confidence=confidence, kind=kind, scan_shows=scan_shows,
                crop=crops[crop_id]['file'] if crop_id else '', bbox=bbox)

decisions = [
    decision('B075-01', 'First word of the slanted upper-left pencil note',
             r'\unsure{joindre}', r'\unsure{Joindre|joindre}', True, True, True,
             ['Joindre', 'joindre'], 'medium', 'misread word',
             'The first letter has a long hooked descender, a high diagonal entry, and no separate dot. The following short joined forms end in a tall d-like stroke, a short r and a terminal e. Joindre is favored, but the compressed middle and the initial case are not completely fixed. Adding the capitalized candidate changes the recorded reading, not merely its macro syntax.',
             [48, 66, 143, 143], 'note_word'),
    decision('B075-02', 'Introduced cotangent-complex letter after Soit enfin',
             r'\unsure{K|\mathbb{K}}', r'\unsure{K|\mathbb{K}}', False, True, True,
             [r'K', r'\mathbb{K}'], 'medium', 'misread symbol or index',
             'Two close dark heads and a broad stem join at the lower left; the two right arms are distinct. The surviving ink allows either retracing of an ordinary K or a deliberately doubled left stroke. The formula occurrences have a single stem; this does not settle the introductory glyph.',
             [1156, 975, 1184, 1010], 'complex_K'),
    decision('B075-03', 'schéma before lisse',
             r'\unsure{schéma}', r'\unsure{schéma}', False, True, True,
             ['schéma'], 'medium', 'misread word',
             'The s, c, tall looped h, accented e and m are separately recoverable. The last place contains dense overlapping blue loops with a rounded bowl and a rightward terminal, favoring a. Its internal construction and any underlying character cannot be recovered securely, so C’s doubt is retained without inventing a deletion.',
             [946, 1126, 1065, 1168], 'schema_end'),
    decision('B075-04', 'Start of sentence after catégorie dérivée.',
             "il s'obtient", "il s'obtient", False, False, False,
             [], 'high', 'other',
             'The initial has a short upright and a separate high dot, followed by a looped ascender l. The ink is lower-case il despite the preceding full stop. This is an explicitly inspected, unmarked C-context target.',
             [1094, 1052, 1251, 1087], 'il_case'),
    decision('B075-05', 'Left-hand label of the sheaf-functor display',
             r'\tag*{(1)}', r'\tag*{(\unsure{1|i})}', True, False, True,
             ['1', 'i'], 'medium', 'misread symbol or index',
             'Between the curved parentheses is a short nearly upright unfooted stroke; a small separate point stands substantially above and to its left. The upright supports 1, while a displaced i dot remains possible. The label is therefore left uncertain; the later prose reference (1) remains as independently read.',
             [201, 1206, 249, 1250], 'formula_label'),
    decision('B075-06', 'Low trace below the superscript area of Ext in display (1)',
             '', low_mark, True, False, True,
             ['unassigned short gray mark and faint companion', 'incidental material traces'],
             'low', 'drawing or diagram',
             'A small low gray-brown wedge or flattened oval sits below and to the right of t; a much paler short oblique trace lies just to its right. Neither touches the letters. Their presence is recorded by shape; authorship and punctuation value are not asserted.',
             [1029, 1248, 1044, 1260], 'ext_low_mark'),
    decision('B075-07', 'Far right of the upper diagram row',
             r'\margin{\unsure{:}}', pair_mark, True, True, True,
             ['unassigned diagonal point pair', 'colon', 'incidental pen/material marks'],
             'low', 'drawing or diagram',
             'The lower-left mark is a short horizontal oval, while the upper-right mark is a taller oblique oval. Their centers form an ascending diagonal, and the pair is distant from the formula. The drawing retains their unequal shapes and relative positions without assigning a colon.',
             [1542, 1362, 1556, 1377], 'right_pair'),
]

body_hand = 'named other hand: P. Deligne (attribution in supplied H description)'
note_hand = 'his hand, pencil (attribution in supplied H description)'

def inv(element, kind, position, words, hand=body_hand):
    return dict(sheet_kind='letter', hand=hand, element=element, kind=kind,
                position=position, first_words_or_objects=words, transcribed='yes')

inventory = [
    inv('Slanted pencil instruction', 'margin note', 'upper-left, x48–228 y65–242',
        'Joindre / SGA 7 VI ? / App. II', note_hand),
    inv('Upper and lower rules around VI', 'drawing', 'upper-left note, x139–189 y86–136',
        r'\overline{\underline{\mathrm{VI}}}', note_hand),
    inv('Upper and lower rules around II', 'drawing', 'upper-left note, x119–156 y162–206',
        r'\overline{\underline{\mathrm{II}}}', note_hand),
    inv('Place and date', 'text', 'top-right, x780–1357 y70–113',
        'Bures sur Yvette, le 21 octobre 1968'),
    inv('Salutation', 'text', 'upper-center, x522–807 y214–266',
        'Cher Grothendieck,'),
    inv('Opening paragraph', 'text', 'x291–1400 y339–463',
        "En fait, il n'est pas nécessaire"),
    inv('Underlined proposition', 'text', 'x289–1482 y497–636',
        'proposition : Soit X un espace analytique complexe compact.'),
    inv('Square-zero reduction paragraph', 'text', 'x297–1532 y654–783',
        'On se ramène à supposer montrer que si X_0'),
    inv('Cancelled supposer', 'deletion', 'x684–792 y675–701', 'supposer'),
    inv('Implication display', 'display', 'x367–1135 y807–858',
        r'(X_0\text{ est un schéma})\Longrightarrow(X\text{ est un schéma})'),
    inv('Extension-group and cotangent-complex paragraph', 'text', 'x293–1534 y880–1175',
        r'Soit E^{\mathrm{an}}(X_0,\mathscr{N}) et E^{\mathrm{alg}}(X_0,\mathscr{N})'),
    inv('Sheaf-functor display and its uncertain label', 'display', 'x201–1286 y1199–1254',
        r'\mathscr{H}om(K,\mathscr{N}) et \mathscr{E}xt^1(K,\mathscr{N})'),
    inv('Low detached trace under Ext', 'drawing', 'x1029–1044 y1248–1260',
        'small wedge/oval and faint right companion', 'unnamed hand or incidental material; uncertain'),
    inv('Diagram introduction', 'text', 'x421–733 y1277–1325', 'Soit le diagramme :'),
    inv('Two-row comparison diagram, label (2)', 'diagram', 'x192–1319 y1344–1537',
        '0 → H → E → H, two rows; three downward comparison arrows'),
    inv('Detached diagonal point pair', 'drawing', 'right margin, x1542–1556 y1362–1377',
        'lower horizontal oval and upper-right upright oval', 'unnamed hand or incidental material; uncertain'),
    inv('Exactness and GAGA paragraph', 'text', 'x292–1478 y1560–1768',
        'Vu les significations (locales) de (1), les lignes sont exactes ;'),
    inv('Cancelled comparison phrase', 'deletion', 'x294–774 y1717–1767',
        r'comparer les images de \alpha et \beta'),
    inv('Archive number recorded only in a comment', 'text', 'bottom-left, x52–111 y1924–1967',
        '74', 'unnamed hand, pencil'),
]

report = dict(
    scan=75, reader='B',
    image_views=[
        '/workspace/scratch/006c0e32b2af/source/SP46_CW_37_scans/H37-01_37_scan075.jpg',
        '/workspace/scratch/006c0e32b2af/source/SP46_CW_37_scans/H37-01_37_scan075_a.jpg',
        '/workspace/scratch/006c0e32b2af/source/SP46_CW_37_scans/H37-01_37_scan075_b.jpg',
    ],
    reading_path=str(root/'reading.tex'),
    crops=[{k:item[k] for k in ['file','bbox','rotation','reason','processing']} for item in manifest],
    decisions=decisions,
    inventory=inventory,
    notes=(
        'Handwritten letter page on squared paper, attributed to P. Deligne by the supplied H description, '
        'dated Bures sur Yvette, le 21 octobre 1968 and addressed Cher Grothendieck. '
        'The underlined proposition claims that a compact complex analytic space X is a scheme exactly when its reduction is. '
        'The writer reduces to a square-zero ideal, introduces analytic and algebraic infinitesimal extension groups and a locally given cotangent complex, '
        'then displays the sheaf Hom and Ext and a two-row comparison diagram. The final paragraph claims exactness and outer vertical isomorphisms by GAGA, '
        'leaving an inclusion of images to show. These are page claims, not independently verified conclusions. '
        'The word supposer and the phrase comparer les images de alpha et beta are cancelled and retained as deletions. '
        'There is no document title beyond the underlined word proposition. No manuscript page number or total-page count is visible; '
        'the lower-left 74 is recorded only as an archive comment. H’s description calls this the first of two sheets, but that count is not added to the transcription. '
        'The upper-left pencil note has an explicit question mark after the SGA 7 VI reference. '
        'Its opening word/case, the introductory K, the crowded final letter of schéma, the display label, and the two detached-mark loci retain editorial uncertainty. '
        'H is descriptive only: all h_reading values are null and all diff_h values false.'
    ),
    math_reading_decisions=[
        r'The proposition has X_{\mathrm{red}} with a lowered joined red and no visible acute; the later X_0 indices are small lowered ovals. No normalization to réd was made.',
        r'The pencil groups are VI and II, each with a distinct upper and lower rule; the question mark follows the VI reference.',
        r'The ideal letter has the repeated looped script form \mathscr{N}, distinct from the plain crossed Xs.',
        r'The two extension-group letters are upright ordinary E; an and alg are raised words. Singular Soit is retained before the pair.',
        r'The introduction retains \unsure{K|\mathbb{K}} because the thick left side can be a retrace or a separate doubled stroke; the K occurrences in formulas have ordinary single stems.',
        r'The Hom initial has crossing loops and the Ext initial has curved upper and lower parts, represented by \mathscr{H}om and \mathscr{E}xt. The Ext degree is the visible raised upright 1.',
        r'The cohomology degrees and qualifiers keep the visible stepped rise: H^{1^{\mathrm{alg}}}, H^{1^{\mathrm{an}}}, H^0, H^{0^{\mathrm{an}}}. No alg is supplied to the upper-right H^0.',
        r'The implication has two shafts and a right head. The comparison diagram has six rightward arrows and three downward arrows; the two rightmost horizontal arrows carry alpha above and beta below, respectively.',
        r'The final image relation is \operatorname{Im}(\beta)\subset\operatorname{Im}(\alpha), with an open left-curved inclusion sign and no lower equality bar.',
        r'The low dotted i and looped l settle il s\textquotesingle obtient as lower case after the full stop. This textual target was inspected, not mathematically inferred.',
        r'The first display label retains a new 1/i ambiguity owing to the displaced upper point; its later (1) reference is independently legible and retained.',
        'No proof, external background verification, or mathematical computation was performed; notation consistency was used only as a diagnostic before returning to the visible strokes.',
    ],
    check_events=[],
    notation=[
        dict(sign='Ideal letter', latex=r'\mathscr{N}', evidence='Looped left entry and curved returning right downstroke, repeated in the formulas.', place='Square-zero paragraph and all extension/functor arguments'),
        dict(sign='Cotangent-complex introductory alphabet', latex=r'\unsure{K|\mathbb{K}}', evidence='Two close dark heads and a merged broad left stem; ordinary K versus deliberate doubled stem remains unresolved.', place='After Soit enfin'),
        dict(sign='Plain complex letter in formulas', latex='K', evidence='One upright and two right arms without an independent parallel stem.', place='Displays (1) and (2)'),
        dict(sign='Sheaf-functor script initials', latex=r'\mathscr{H}om; \mathscr{E}xt^1', evidence='Crossing looped H and rounded E, followed by baseline lower-case letters and raised 1.', place='Displays (1) and (2)'),
        dict(sign='Raised cohomology qualifiers', latex=r'H^{1^{\mathrm{alg}}}; H^{1^{\mathrm{an}}}; H^0; H^{0^{\mathrm{an}}}', evidence='The short qualifiers rise a second level beside the numerals; upper-right H has the oval alone.', place='Both diagram rows'),
        dict(sign='Reduction subscript', latex=r'X_{\mathrm{red}}', evidence='Three small joined letters below X; no accent above e.', place='Underlined proposition'),
        dict(sign='Display label ambiguity', latex=r'(\unsure{1|i})', evidence='Short unfooted upright plus displaced upper-left point between parentheses.', place='Left of the sheaf-functor display'),
        dict(sign='Right marginal point pair', latex=pair_mark, evidence='Lower horizontal oval and upper-right oblique upright oval; semantic and material status uncertain.', place='Far right of diagram first row'),
        dict(sign='Low unassigned mark', latex=low_mark, evidence='Gray compact low wedge with much fainter short companion on the right; no contact with text.', place='Below Ext superscript area in first display'),
    ],
    abbreviations=[
        dict(form='App.', expansion='appendice'),
        dict(form='red', expansion='réduit'),
        dict(form='an', expansion='analytique'),
        dict(form='alg', expansion='algébrique'),
        dict(form='GAGA', expansion='géométrie algébrique et géométrie analytique'),
        dict(form='Im', expansion='image'),
        dict(form='Hom', expansion='homomorphismes'),
        dict(form='Ext', expansion='extensions'),
    ],
    slips=[
        'Singular Soit precedes the two groups E an and E alg; it is preserved, without changing it to Soient.',
        'The lowercase il after the full stop following dérivée is preserved.',
        'Idéal starts with a capital I within the sentence and is preserved.',
    ],
    completion=(
        'Full assigned-page coverage completed: whole page viewed once for layout, then half a once and half b once in order; '
        'the halves overlap by 160 pixels and half b begins at whole-image y=920. '
        'Seven open loci were listed before cropping, and each retained enlarged crop was viewed once, in delivery batches of three, three, and one. '
        'No delivery was truncated and no image was reopened. All text blocks, underlining/rules, the two deletions, both displays, all diagram objects, nine arrows and two arrow labels, '
        'the slanted marginal note, detached marks, and archive comment are represented. '
        'No OCR, external research, TeX compilation, peer-file reading, other-page reading, or delegation was used. '
        'H supplied no transcription and contributes no differences.'
    ),
)

(root/'report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
print(root/'report.json')
