import json
from pathlib import Path

BASE = Path('/workspace/scratch/15c7af26487b/edition')
PAGE = '148_scan013'

coords = {
    'page_number': [751, 28, 827, 102],
    'ens_first': [1230, 115, 1495, 207],
    'ens_second': [1182, 205, 1460, 317],
    'order_six': [294, 348, 1517, 620],
    'order_three_triangles': [268, 610, 1638, 846],
    'parenthetical_insertion': [1055, 806, 1555, 975],
    'mutually_nonadjacent': [256, 969, 1618, 1119],
    'cellular_heading': [260, 1198, 1547, 1465],
    'set_expression': [300, 1863, 1525, 1998],
    'contains': [303, 1988, 1595, 2145],
    'second_triangles': [303, 2093, 1630, 2293],
    'lower_numeral': [34, 2261, 121, 2333],
    'first_hexagone': [260, 845, 1100, 975],
}

tex = r'''\cotefile{148}
\scanpage{13}
\mspage{5}

qui avec l'origine $e$ forment l'ens des pts fixes de $X_S$.
(L'ens des pts fixes sous $\mathbb Z/6\mathbb Z$ \unsure{est|se} réduit
à $e$.) Les deux pts fixes sous $\mathbb Z/3\mathbb Z$, distincts de $e$, corres-\newline
pondent aux deux triangles \unsure{co-inscrits|coinscrits} de l'hexagone $S$.
(\inserted{les deux} triplets des côtés mutuelle\unsure{m\textsuperscript{t}|ment} non adjacents.)

\uline{Décompositions cellulaires}\newline
\uline{canoniques}. Décomposition en deux faces triangulaires, par trois arêtes,
un seul sommet. Les faces triangulaires correspondent aux éléments de
$(X_S)^\zeta\setminus\{e\}$ (chaque face en contient un et un seul) i.e.
aux triangles \unsure{co-inscrits|coinscrits} de l'hexagone. Les arêtes correspondent aux trois

\margin{12}
'''

changes = []

def change(place, C, H, final, evidence, crop, kind, error_sheet_kind,
           confidence='high', differs_C=False, differs_H=True,
           marked_in_H=False, consequential=False):
    ident = f'{PAGE}-{len(changes) + 1:02d}'
    box = coords[crop]
    changes.append({
        'id': ident, 'place': place, 'C': C, 'H': H, 'final': final,
        'evidence': f'{evidence} Crop {PAGE}_{crop}.png, original box {box}.',
        'crop': f'{PAGE}_{crop}.png', 'box': box,
        'confidence': confidence, 'kind': kind, 'error_sheet_kind': error_sheet_kind,
        'differs_C': differs_C, 'differs_H': differs_H,
        'marked_in_H': marked_in_H, 'consequential': consequential,
    })
    return ident

ids = {}
ids['ens_first'] = change(
    'L01, first abbreviation at the right end of the baseline',
    "l'ens", "l'ens.", "l'ens",
    'The connected abbreviation ends in a heavy downward s hook. The space to its right has no detached punctuation mark.',
    'ens_first', 'text not on the page', 'Text that is not on the page')
ids['ens_second'] = change(
    'L02, abbreviation following the opening parenthesis',
    "(L'ens", "(L'ens.", "(L'ens",
    'The capital L, apostrophe and connected ens are visible. The terminal s bends down; no separate period follows it.',
    'ens_second', 'text not on the page', 'Text that is not on the page')
ids['adjective_first'] = change(
    'L06, first triangle adjective, M0110',
    r'\unsure{co-inscrits|coinscrits}', 'inscrits', r'\unsure{co-inscrits|coinscrits}',
    'A clear opening co precedes the dotted i. The ensuing nearly horizontal stroke is too compressed to establish whether a separate hyphen is written in the compound. The co-prefix is retained and the exact joining remains doubtful.',
    'order_three_triangles', 'misread word', 'Words', confidence='medium', consequential=True)
ids['de_first'] = change(
    'L07, preposition before the first occurrence of hexagone',
    "de l'hexagone", "dans l'hexagone", "de l'hexagone",
    'The short unit before the apostrophised article has a d ascender and a single flattened following run. The additional a-n-s sequence supplied by H is not visible. The same short de form occurs before the lower set expression and before the second hexagone.',
    'first_hexagone', 'misread word', 'Words')
ids['insertion'] = change(
    'L07 and its interline, placement of les deux before triplets',
    r'(\inserted{les deux} triplets',
    "\\add{les deux}\\note{en interligne} dans\nl'hexagone $S$. (Triplets",
    r'(\inserted{les deux} triplets',
    'Les deux is written above triplets. Its long insertion leader turns down immediately before the t, inside the opening parenthesis. The initial t has the tall crossed lowercase form also visible in triangles; the source does not supply a capital T here. The opening parenthesis is retraced. H records the raised words but places them in the preceding triangle phrase.',
    'parenthetical_insertion', 'insertion or placement', 'Insertions put in the wrong place',
    marked_in_H=True, consequential=True)
ids['des'] = change(
    'L07, word after triplets', 'des', 'de', 'des',
    'The d loop is followed by a low run terminating in a dark downward s hook, comparable to the terminal s of both ens abbreviations. The last hook remains part of the word.',
    'parenthetical_insertion', 'misread word', 'Words')
ids['mutuellement'] = change(
    'L08, compressed ending of the word between côtés and non',
    'mutuellement', 'mutuellement', r'mutuelle\unsure{m\textsuperscript{t}|ment}',
    'After the paired tall l strokes and the low following connection, the ending runs almost horizontally and finishes in a small crossed raised return. The full -ment sequence is not separately exposed. A contracted ending with raised t is retained first, with the full ending as an alternative; this remains a reading doubt, not a settled expansion.',
    'mutually_nonadjacent', 'abbreviation expanded or spelling modernised',
    'Abbreviations expanded, spelling modernised', confidence='medium', differs_C=True)
ids['contient'] = change(
    'L15, verb following face en', 'contient', 'contenant', 'contient',
    'The word shows the co opening, a flattened n, the tall crossed t, a small detached i mark and a compressed terminal run with a rising return. No second a-n syllable is exposed. These strokes support the shorter reading contient; the final letters are closely joined.',
    'contains', 'misread word', 'Words')
ids['adjective_second'] = change(
    'L16, second triangle adjective, M0111',
    r'\unsure{co-inscrits|coinscrits}', 'inscrits', r'\unsure{co-inscrits|coinscrits}',
    'The second occurrence again has the co opening before a dotted i and an elongated nearly horizontal following stroke. The prefix is secure; the hyphen-versus-joined spelling is not fully exposed. Both C alternatives remain in place.',
    'second_triangles', 'misread word', 'Words', confidence='medium', consequential=True)
ids['de_second'] = change(
    'L16, preposition before the second occurrence of hexagone',
    "de l'hexagone", "dans l'hexagone", "de l'hexagone",
    'The short word has the same d ascender and flattened following e connection as the first de l\'hexagone. There is no visible a-n-s sequence between it and the article.',
    'second_triangles', 'misread word', 'Words')
ids['sentence_end'] = change(
    'L16–L17, punctuation and following initial at the last sentence boundary',
    "l'hexagone. Les arêtes", "l'hexagone, les arêtes", "l'hexagone. Les arêtes",
    'The terminal sign is a detached short near-horizontal mark, with no descending comma tail. The same page has a similarly horizontal detached period after S in the first_hexagone crop. The following baseline begins with a full-height capital L. Both visible features support C.',
    'second_triangles', 'other', 'Other')
ids['lower_numeral'] = change(
    'Lower left margin', r'\margin{12}', '', r'\margin{12}',
    'A lighter slanted 1 and a curved 2 stand separately in the lower left margin. Both figures are complete. H has no corresponding marginal number.',
    'lower_numeral', 'omission', 'Omissions')

decisions = [
    {
        'id': 'M0109', 'decision': 'undecided', 'reading': r'\unsure{est|se}',
        'evidence': 'After the complete group expression, the word is a low nearly horizontal unit with a small angular raised return. Its internal letters are fused; there is no separately exposed tall crossed final t, but the stroke sequence does not securely settle either complete word. The surrounding verb is not used to decide the letters.',
        'crop': f'{PAGE}_order_six.png {coords["order_six"]}', 'confidence': 'low',
    },
    {
        'id': 'M0110', 'decision': 'undecided', 'reading': r'\unsure{co-inscrits|coinscrits}',
        'evidence': 'The initial co and dotted i are exposed. The flattened connection into the remaining letters does not securely separate a written hyphen from the joined letter strokes. H omits the visible co opening. The word is read as a whole in its two-baseline context.',
        'crop': f'{PAGE}_order_three_triangles.png {coords["order_three_triangles"]}', 'confidence': 'medium',
    },
    {
        'id': 'M0111', 'decision': 'undecided', 'reading': r'\unsure{co-inscrits|coinscrits}',
        'evidence': 'The second word independently exposes co before the dotted i, followed by the same long flattened joining stroke. A distinct hyphen remains uncertain, so the two C spellings are retained at this occurrence as well.',
        'crop': f'{PAGE}_second_triangles.png {coords["second_triangles"]}', 'confidence': 'medium',
    },
]

lines = [
    (1, 'qui avec l’origine e forment l’ens', 'upper paragraph, first baseline'),
    (2, 'des pts fixes de X_S. (L’ens', 'upper paragraph, second baseline'),
    (3, r'des pts fixes sous \mathbb Z/6\mathbb Z \unsure{est|se} réduit', 'upper paragraph, third baseline'),
    (4, 'à e.) Les deux pts fixes', 'upper paragraph, fourth baseline'),
    (5, r'sous \mathbb Z/3\mathbb Z, distincts de e, corres-', 'upper paragraph, fifth baseline'),
    (6, r'pondent aux deux triangles \unsure{co-inscrits|coinscrits}', 'upper paragraph, sixth baseline'),
    (7, 'de l’hexagone S. (triplets des', 'upper paragraph, seventh main baseline'),
    (8, r'côtés mutuelle\unsure{m\textsuperscript{t}|ment} non adjacents.)', 'upper paragraph, eighth baseline'),
    (9, 'Décompositions cellulaires', 'first underlined heading baseline'),
    (10, 'canoniques. Décomposition en', 'second heading baseline and beginning of following prose'),
    (11, 'deux faces triangulaires, par trois', 'lower paragraph, first complete prose baseline'),
    (12, 'arêtes, un seul sommet. Les', 'lower paragraph, second complete prose baseline'),
    (13, 'faces triangulaires correspondent aux', 'lower paragraph, third complete prose baseline'),
    (14, r'éléments de (X_S)^\zeta\setminus\{e\} (chaque', 'lower paragraph, baseline containing the set expression'),
    (15, 'face en contient un et un seul) i.e.', 'lower paragraph, following baseline'),
    (16, r'aux triangles \unsure{co-inscrits|coinscrits} de l’hexagone.', 'lower paragraph, penultimate baseline'),
    (17, 'Les arêtes correspondent aux trois', 'last baseline; unfinished at the leaf edge'),
]
inventory = [{
    'sheet_kind': 'text', 'hand': 'his hand', 'element': 'E01', 'kind': 'margin note',
    'position': 'top centre, above the main text', 'first_words_or_objects': '5', 'transcribed': 'yes',
}]
for number, words, position in lines:
    if number == 7:
        inventory.append({
            'sheet_kind': 'text', 'hand': 'his hand', 'element': f'E{len(inventory)+1:02d}',
            'kind': 'insertion', 'position': 'interline above L07, leader attaching before triplets inside the parenthesis',
            'first_words_or_objects': 'les deux', 'transcribed': 'yes',
        })
    inventory.append({
        'sheet_kind': 'text', 'hand': 'his hand', 'element': f'E{len(inventory)+1:02d}',
        'kind': 'text', 'position': f'L{number:02d}, {position}',
        'first_words_or_objects': words, 'transcribed': 'yes',
    })
inventory.append({
    'sheet_kind': 'text', 'hand': 'lighter hand; attribution unestablished',
    'element': f'E{len(inventory)+1:02d}', 'kind': 'margin note',
    'position': 'lower left margin', 'first_words_or_objects': '12', 'transcribed': 'yes',
})

doubts = [
    {'place': 'L03, M0109', 'reading': r'\unsure{est|se}', 'alternatives': 'est; se',
     'confidence': 'low', 'reason': 'The low short unit ends in an angular raised return; the fused internal letters do not securely expose either full sequence.'},
    {'place': 'L06, M0110', 'reading': r'\unsure{co-inscrits|coinscrits}', 'alternatives': 'co-inscrits; coinscrits',
     'confidence': 'medium', 'reason': 'The co-prefix is clear. The long flattened connection near the dotted i does not securely disclose a separate hyphen.'},
    {'place': 'L08, terminal contraction', 'reading': r'mutuelle\unsure{m\textsuperscript{t}|ment}',
     'alternatives': r'mutuellem\textsuperscript{t}; mutuellement', 'confidence': 'medium',
     'reason': 'The paired tall l strokes lead into a nearly flat terminal run and a small crossed raised return. The full -ment sequence remains unexposed; the contracted reading is placed first without expanding it as established text.'},
    {'place': 'L16, M0111', 'reading': r'\unsure{co-inscrits|coinscrits}', 'alternatives': 'co-inscrits; coinscrits',
     'confidence': 'medium', 'reason': 'The second occurrence independently preserves the co opening, while the separate-hyphen versus joined-letter issue remains unresolved.'},
]

second_boxes = []

def blind(kind, box, reading):
    second_boxes.append({
        'box': f'B{len(second_boxes)+1:02d}', 'kind': kind,
        'x0': box[0], 'y0': box[1], 'x1': box[2], 'y1': box[3], 'reading': reading,
    })

blind('upper handwritten number only', coords['page_number'], r'\mspage{5}')
blind('complete abbreviation at the end of the first baseline', coords['ens_first'], "l'ens")
blind('parenthetical opening and complete abbreviation on the second baseline', coords['ens_second'], "(L'ens")
blind('two complete main baselines including the entire inline group expression', coords['order_six'],
      r'''des pts fixes sous $\mathbb Z/6\mathbb Z$ \unsure{est|se} réduit
à $e$.) Les deux pts fixes''')
blind('two main baselines including the whole group expression and adjective; upper-edge descender and lower interlinear writing are context',
      coords['order_three_triangles'], r'''sous $\mathbb Z/3\mathbb Z$, distincts de $e$, corres-\newline
pondent aux deux triangles \unsure{co-inscrits|coinscrits}''')
blind('complete main phrase through its terminal punctuation; upper-edge descender is context',
      [260, 845, 1060, 975], r"de l'hexagone $S$.")
blind('parenthetical opening with its raised insertion, leader and following baseline; upper-edge descender is context',
      coords['parenthetical_insertion'], r'(\inserted{les deux} triplets des')
blind('complete main baseline including the whole word with a compressed ending and closing punctuation',
      coords['mutually_nonadjacent'], r'côtés mutuelle\unsure{m\textsuperscript{t}|ment} non adjacents.)')
blind('two complete heading baselines with their underlining and following prose', coords['cellular_heading'],
      r'''\uline{Décompositions cellulaires}\newline
\uline{canoniques}. Décomposition en''')
blind('two complete prose baselines containing the written counts', [275, 1470, 1590, 1730],
      '''deux faces triangulaires, par trois
arêtes, un seul sommet. Les''')
blind('complete main baseline including the entire inline set expression; upper-edge descenders are context', coords['set_expression'],
      r'éléments de $(X_S)^\zeta\setminus\{e\}$ (chaque')
blind('complete main baseline including the disputed verb and terminal abbreviation; neighboring baseline fragments are context', coords['contains'],
      'face en contient un et un seul) i.e.')
blind('last two complete main baselines including the whole adjective and sentence boundary; upper-left descender is context', coords['second_triangles'],
      r'''aux triangles \unsure{co-inscrits|coinscrits} de l'hexagone.
Les arêtes correspondent aux trois''')
blind('lower marginal handwritten number only', coords['lower_numeral'], r'\margin{12}')

diff_coverage = [
    {'row': 493, 'disposition': 'Editorial scan/page marker syntax: scan 13 is an edition marker; the visible manuscript 5 is retained as \\mspage{5}. H names this number inside its editorial page note. No text-change row.'},
    {'row': 494, 'disposition': 'H’s de l’auteur belongs to its editorial page note and is not manuscript prose. The visible top number is retained; no text-change row.'},
    {'row': 495, 'disposition': ids['ens_first']},
    {'row': 496, 'disposition': ids['ens_second']},
    {'row': 497, 'disposition': 'M0109 remains undecided as \\unsure{est|se}. H gives one of these alternatives; no secure replacement word has been established. Decision and doubt retained; no certainty-only change row.'},
    {'row': 498, 'disposition': ids['adjective_first'] + '; visible co-prefix retained, exact joining still doubtful.'},
    {'row': 499, 'disposition': ids['adjective_first'] + ' (word joining), ' + ids['de_first'] + ' (preposition), and ' + ids['insertion'] + ' (raised words’ attachment); en interligne is H editorial wording.'},
    {'row': 500, 'disposition': ids['insertion']},
    {'row': 501, 'disposition': ids['des']},
    {'row': 502, 'disposition': ids['contient']},
    {'row': 503, 'disposition': ids['adjective_second']},
    {'row': 504, 'disposition': ids['adjective_second'] + ' (word joining) and ' + ids['de_second'] + ' (preposition).'},
    {'row': 505, 'disposition': ids['sentence_end']},
    {'row': 506, 'disposition': ids['lower_numeral']},
]

report = {
    'page': PAGE, 'reader': 'reader_b', 'line_count': 17,
    'layout': 'Upright handwritten leaf, manuscript 5 centred above seventeen principal baselines. The upper paragraph occupies eight baselines and includes one raised insertion above its seventh baseline. A substantial blank separates it from a two-line underlined heading and the lower prose. The last baseline ends unfinished at trois. A lighter 12 stands in the lower left margin. No diagram or cancelled textual span is visible. Reading order is top number, upper prose with the insertion before triplets, underlined heading and lower prose, then lower marginal number.',
    'changes': changes, 'decisions': decisions, 'unnumbered_decisions': [],
    'inventory': inventory, 'doubts': doubts,
    'notation': [
        {'form': r'e', 'meaning': 'The manuscript calls e the origin in the opening continuation and names it in the following fixed-point parenthesis.',
         'evidence': 'L01, l’origine e; L04, à e; L05, distincts de e; L14, the excluded singleton.', 'scope': 'All four occurrences of e on this leaf were read.'},
        {'form': r'\mathbb Z/6\mathbb Z; \mathbb Z/3\mathbb Z',
         'meaning': 'The two group expressions written after sous in the successive fixed-point clauses; the page gives their numerical orders as part of the notation.',
         'evidence': 'L03 has a looped 6 between the quotient stroke and final Z; L05 has the open curved 3. Both complete expressions are included in tight crops and blind targets.',
         'scope': 'The two group expressions on this page only.'},
        {'form': r'(X_S)^\zeta\setminus\{e\}',
         'meaning': 'The expression to whose elements the manuscript says the triangular faces correspond; its following parenthesis says each face contains one.',
         'evidence': 'L14: parenthesised X with subscript S, raised ζ, descending difference stroke, and braced e; L15 supplies the following source clause.',
         'scope': 'The single lower occurrence of this expression, plus the earlier X_S in L02. This records the page’s notation and assertion without a proof check.'},
    ],
    'abbreviations': [
        {'form': 'ens', 'expansion': 'ensemble, tentative expansion only; neither occurrence has a detached final period.'},
        {'form': 'pts', 'expansion': 'points, tentative expansion only.'},
        {'form': 'i.e.', 'expansion': 'id est, tentative expansion only; both small points are retained.'},
        {'form': r'mutuellem\textsuperscript{t}', 'expansion': 'mutuellement, tentative and unresolved; the text retains a contracted/full-ending alternative.'},
    ],
    'hand': [
        {'habit': 'The connected ens has shallow flattened internal humps and a heavy terminal downward s hook.',
         'places': 'L01 and L02, the two ens abbreviations.', 'scope': 'Both occurrences on this page were independently cropped.',
         'witness_errors': 'H adds a detached final period at both loci; none is visible.'},
        {'habit': 'The recurring triangle adjective exposes co before a dotted i, while the following n region becomes a nearly horizontal run.',
         'places': 'L06 and L16.', 'scope': 'Both occurrences were independently inspected; no choice between a separate hyphen and joined spelling is imposed.',
         'witness_errors': 'H omits the co opening in both occurrences; C’s co-inscrits/coinscrits alternatives remain.'},
        {'habit': 'Long low terminal connections can end in a small raised or crossed return while obscuring intermediate letters.',
         'places': 'L03 short word; L08 ending after mutuelle; L15 ending of contient.',
         'scope': 'These local strokes were inspected individually. Their letter sequences were not equated merely because their outlines recur.',
         'witness_errors': 'M0109 remains undecided. Both witnesses give the full mutuellement, whose ending is retained as contracted/full alternatives. At L15, the visible dotted i and shorter stroke sequence support contient against H’s contenant.'},
        {'habit': 'The point at a sentence boundary can be a short detached horizontal stroke.',
         'places': 'L07 after S; L16 after hexagone.', 'scope': 'Only these two source marks were compared.',
         'witness_errors': 'H gives a comma at L16 and a lowercase following l; the source mark lacks a comma tail and the next baseline begins with a capital L.'},
        {'habit': 'A tall crossed initial t can belong to a lowercase word.',
         'places': 'L06 triangles, L07 triplets, L16 triangles.', 'scope': 'These three initial letters were compared on this leaf.',
         'witness_errors': 'H capitalises Triplets at the displaced insertion locus; C’s lowercase form matches the local letter shape.'},
    ],
    'legibility': 'The ink is generally dark and the large handwriting leaves most words and the three inline mathematical expressions separable. The upper 5 and lighter lower 12 are complete. Local difficulty comes from flattened connected minims, heavy terminal hooks and a small angular final return, especially in M0109, the two triangle adjectives and the ending after mutuelle. The raised les deux and its leader are sufficiently exposed to determine both words and their attachment before triplets. The heading strokes run below their words; the crossing of the q descender in canoniques does not cancel that word. C follows most of the visible prose, while H adds periods after ens, omits co twice, changes both de phrases, displaces the insertion and reads contenant. The witnesses’ agreement on mutuellement does not expose its compressed final letters, so that ending remains doubtful. Thirteen tight crops were inspected after the whole scan and both supplied halves; the first attempted multi-image display was truncated and was not counted as an inspection.',
    'notes': 'Manuscript p. 5 continues a preceding sentence with qui avec l’origine e (L01). The upper paragraph says that these objects with e form the fixed points of X_S; its parenthesis gives the expression Z/6Z and an unresolved est/se before réduit à e (L02–L04). It then names two fixed points under Z/3Z, distinct from e, and relates them to two triangles with the visible co-prefix (L05–L07). The parenthesis associates them with two triplets of mutually nonadjacent sides, with les deux inserted before triplets and the ending of mutuellem-raised-t/mutuellement left unresolved (L07–L08). These are statements read from the page, not mathematical results newly asserted here. The heading Décompositions cellulaires canoniques is underlined on two baselines; its final period lies beyond the underline. The following source prose describes two triangular faces, three edges and one vertex, then associates the faces with elements of (X_S)^ζ setminus {e}, adding that each face contains one (L09–L15). It repeats the triangle phrase and ends Les arêtes correspondent aux trois without a completion (L16–L17). The visible line-end hyphen in corres-/pondent is retained with its break; the underline is stopped before the heading period. These layout features do not create word-error rows. No deleted word or drawing is present. The insertion leader is represented by the established inserted-text convention at its observed attachment. H’s page note and en interligne are editorial language. No mathematical proof, calculation or theorem check was performed during this reading.',
    'check_events': [], 'second_boxes': second_boxes, 'diff_coverage': diff_coverage,
    'deletion_insertion_check': 'The sole C insertion, les deux, was read separately in parenthetical_insertion [1055,806,1555,975]. Both words are above triplets and the long leader turns down before its initial t, after the parenthesis has opened. The insertion stays at that place; H’s placement in the preceding adjective phrase is corrected. The opening parenthesis is retraced, not treated as a deleted textual span. The two heading strokes are underlines; they do not strike the heading, including the q descender they cross. No cancelled word is visible elsewhere. The separate line-end hyphen after corres is retained and is not treated as a deletion stroke.',
}

(BASE / 'work' / f'{PAGE}.tex').write_text(tex, encoding='utf-8')
(BASE / 'work' / f'{PAGE}_report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps({
    'page': PAGE, 'lines': report['line_count'], 'changes': len(changes),
    'decisions': len(decisions), 'inventory': len(inventory), 'doubts': len(doubts),
    'second_boxes': len(second_boxes), 'diff_rows': len(diff_coverage), 'crops': len(coords),
}, ensure_ascii=False))
