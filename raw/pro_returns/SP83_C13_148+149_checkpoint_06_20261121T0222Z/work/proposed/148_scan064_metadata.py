from pathlib import Path
import json

ROOT = Path('/workspace/scratch/f28c4f52d3ec')
PAGE = '148_scan064'
SIDE = ROOT / 'proposed' / f'{PAGE}_crop_boxes.json'
crops = json.loads(SIDE.read_text())
for record in crops:
    record['viewed'] = True
SIDE.write_text(json.dumps(crops, ensure_ascii=False, indent=2) + '\n')
crop_by_name = {record['name']: record for record in crops}

changes = []
def change(place, c, h, final, diff_c, diff_h, kind, error_kind, evidence,
           crop_name, confidence='high', marked_in_h=False, consequential=False):
    crop = crop_by_name[crop_name]
    changes.append(dict(id=f'{PAGE}-{len(changes)+1:02d}', place=place,
        c=c, h=h, final=final, diff_c=diff_c, diff_h=diff_h,
        kind=kind, error_kind=error_kind, evidence=evidence,
        crop=crop['crop'], box=crop['box'], confidence=confidence,
        marked_in_h=marked_in_h, consequential=consequential))

change('Main line 1, operation name', 'bouchage', 'bouclage', 'bouchage', False, True,
    'misread word', 'Words',
    'The middle tall stroke returns into a low right shoulder, giving h after the short c; it is not a separate looped l. The b, flattened ou, and descending g are visible.', 'bouchage')
change('Main line 2, en cela', 'cela', 'ce', 'cela', False, True,
    'misread word', 'Words',
    'After the open c and small e there is a distinct tall looped l and a terminal a. The two extra letters are not a continuation of ce.', 'cela')
change('Raised operation number above main line 5', r'\textcircled{$5^\circ$}',
    '(5°)', r'\inserted{\textcircled{$5^\circ$}}', True, False,
    'insertion or placement', 'Insertions put in the wrong place',
    'The numeral has a top bar, short upper vertical, and lower round turn: 5, followed by a small degree circle. Its enclosing oval is above the baseline, with a curved attachment stroke down toward the gap after opération. H describes this state in its editorial note.', 'operation5', consequential=True)
change('Main line 8, replacement and liaison', r'\deleted{une} \inserted{en} liaison',
    r"\struck{en} \uncertain{d'ailleurs}", r'\deleted{une} \inserted{en} liaison', False, True,
    'misread word', 'Struck text',
    'The baseline cancellation passes through low u/n strokes and a final e curl, read une. Above it, the separate open e and final n give en. The next live word has a tall looped l, dotted i, and the aison continuation: liaison. There is no d-apostrophe beginning for ailleurs.', 'liaison', 'medium', True)
change('Main line 9, beginning', 'avec ça,', 'absent', 'avec ça,', False, True,
    'omission', 'Omissions',
    'The short avec run is followed by a separate ça group and a dark comma. These are baseline words between liaison and une autre structure.', 'avec_ca')
change('Main line 10, order after celle', r'celle \deleted{\unsure{des}} des',
    r'celle des \struck{\ill{}}', r'celle des \deleted{\unsure{une|des}}', True, True,
    'insertion or placement', 'Struck text',
    'A clear live des, including its tall d and looped e, stands immediately after celle. To its right is the separately cancelled low word. Its surviving humps favour une, but the heavy horizontal stroke prevents recovery of every letter; des remains an alternative. C reverses the physical order.', 'celle_des', 'low', True)
change('Main line 11, complete tuple', r'$(X,[\unsure{\Sigma}],R)$',
    r'$(X, [\widetilde{\Sigma}], R)$', r'$(X,[\unsure{\widetilde{\Sigma}|\Sigma}],R)$', True, False,
    'misread symbol or index', 'Symbols and indices',
    'Both parentheses, both commas, X, square brackets, and R are visible. Over the compact Sigma body there is a short extra horizontal/wavy stroke, but the bracket and upper Sigma strokes are overworked. A tilde is favoured without eliminating plain Sigma. The adjacent raised formula is separately legible as capital Pi with index 1 and semicolon: Pi_1(X;R).', 'pi_tuple', 'low', consequential=True)
change('Main line 12, base-point abbreviation', 'à base', 'points-base', r'p\textsuperscript{ts}-base', True, True,
    'abbreviation expanded or spelling modernised', 'Abbreviations expanded, spelling modernised',
    'The first letter has a long p descender. A small elevated ts group follows it before the hyphen; the next word is base. It is an abbreviation, not à, and does not spell out points.', 'nonempty_base', consequential=True)
change('Main line 12, preposition before R', 'des', 'dans', 'dans', True, False,
    'misread word', 'Words',
    'The word begins with a tall d and continues with a low an run and terminal s-shaped hook. It is longer than de/des and reads dans before the separate capital R.', 'nonempty_base')
change('Raised nonempty condition, whole formula', r'\inserted{pour $R\ne\varnothing$,}',
    r'\add{pour $R \neq \emptyset$,}', r'\inserted{pour $R\ne\phi$,}', True, True,
    'misread symbol or index', 'Symbols and indices',
    'The rightmost sign is a small oval crossed by a long descending stem, the handwritten phi used here for the empty set. The capital R, two inequality bars with crossing stroke, and following comma are also visible.', 'nonempty_base', consequential=True)
change('Main line 12, condition attachment and en tant que',
    r'\inserted{pour $R\ne\varnothing$,} à base des $R$, (en tant que',
    r'\add{pour $R \neq \emptyset$,} points-base dans $R$, \add{en tant que}',
    r'p\textsuperscript{ts}-base dans $R$, \inserted{pour $R\ne\phi$,} en tant que', True, True,
    'insertion or placement', 'Insertions put in the wrong place',
    'The long curved leader begins after the baseline R-comma, immediately before en, then rises and runs under the added condition. The words en tant que stay on the baseline. The curved left end is not an independent opening parenthesis, and the insertion is attached after the base-point phrase.', 'nonempty_base', 'medium', consequential=True)
change('Main line 14, deleted phrase', r'\deleted{la donnée}', r'\struck{la dernière}',
    r'\deleted{la donnée}', False, True, 'misread word', 'Struck text',
    'The cancellation crosses la followed by a tall d, rounded o, two short n humps, and accented é/e. The accent and terminal e are visible above or below the cancellation; there is no visible r-i-è-r sequence for dernière.', 'donnee_comme')
change('Main line 14, comme', r'\unsure{comme}', r'\ill{}', 'comme', False, True,
    r'readable ink left as \ill{}', 'Readable ink left as illegible',
    'The open initial c, low o, two groups of m humps and final e hook are live and separate from the cancellation on la donnée.', 'donnee_comme', marked_in_h=True)
change('Main line 15, nouvelle opération', r'\unsure{nouvelle opération}',
    r'\ill{} \ill{} opérations', 'nouvelle opération', False, True,
    r'readable ink left as \ill{}', 'Readable ink left as illegible',
    'The first word has the flattened nouv- run followed by two separate tall l loops and final e. The following word has an o/p loop, accent, crossed t, dotted i and on ending. There is a gap before the closing parenthesis and no independent final s.', 'nouvelle', marked_in_h=True)
change('Main line 15, abbreviated quantifier', r'\unsure{tte}', 'les', 'tte', False, True,
    'misread word', 'Abbreviations expanded, spelling modernised',
    'Two adjacent tall crossed t strokes precede a separate small e. The source has the three-letter short form tte, without an l beginning and without expansion to toute.', 'representation')
change('Main line 15, cancelled predecessor of représentation', r'\deleted{\unsure{reconstitution}}',
    r'\struck{\ill{}}', r'\deleted{\unsure{reconstitution}}', False, True,
    r'readable ink left as \ill{}', 'Struck text',
    'A long old word is crossed below the replacement. Some initial re-/co-like low strokes and a long ending survive, but the cancellation and the replacement p descender obscure its centre. Reconstitution remains only a proposed reading, not a resolved deleted doubt.', 'representation', 'low', True)
change('Raised replacement above main line 15', r'\inserted{\unsure{représentation}}',
    r'\add{\ill{}}', r'\inserted{représentation}', False, True,
    r'readable ink left as \ill{}', 'Readable ink left as illegible',
    'The raised word has the initial ré- strokes, a long p descender, the following résen- run, a tall crossed t, dotted i and on ending. Its own baseline is above the cancellation; the p descender crossing the old stroke does not cancel the replacement.', 'representation', 'medium', True)
change('Main line 16, finite-set representation phrase', r'\unsure{du groupoïde par ens finis}',
    r'\ill{} groupoïde par \uncertain{ces} finis', 'du groupoïde par ens finis', False, True,
    r'readable ink left as \ill{}', 'Readable ink left as illegible',
    'The line begins du, then the g loop/descender, compressed rou, p descender and oïde ending of groupoïde. After par the small word starts with an e loop, followed by n and terminal s; it is ens, not ces. The tall f, two dotted i strokes, n and final s give finis. No abbreviation point is visible after ens.', 'du_groupoide', 'medium', True, True)
change('Raised covering phrase and its baseline attachment',
    r"\unsure{d'un} \inserted{[\unsure{définissant un}]}",
    r"\add{\struck{\ill{}} \ill{} d'un}",
    r"\inserted{[\unsure{définissant un}} d'un", True, True,
    'insertion or placement', 'Insertions put in the wrong place',
    'A tall opening square bracket precedes the raised phrase; no closing square bracket is visible. The f-like tall stem, dotted i strokes, -issant continuation and final un support définissant un, but the initial strokes are overworked, so the reading stays doubtful. The long lower stroke curves upward from immediately before baseline d’un and continues under the raised words: it is their leader, not a deletion of the whole raised phrase. Baseline d, apostrophe, u and n are distinct and live. The insertion is serialized before d’un.', 'covering_insert', 'medium', True, True)
change('Main line 17, revêtement ending', 'revêtement', r'\uncertain{revêtements}',
    'revêtement', False, True, 'misread word', 'Words',
    'The word ends in the tall terminal t with its cross/return. There is no separate s after that letter before the raised X-prime and the following preposition.', 'revetement', marked_in_h=True)
change('Above main line 17, X prime', r"\inserted{$X'$}", r"$X'$", r"\inserted{$X'$}", False, True,
    'insertion or placement', 'Insertions put in the wrong place',
    'X and a short separate prime are written above the baseline, between revêtement and the preposition, while the following X is on the baseline.', 'revetement', consequential=True)
change('Main line 17, preposition before X', 'de', 'des', r'\unsure{de|des}', False, True,
    'misread word', 'Words',
    'The tall d and following low e run are clear. Its terminal down-hook could be the ordinary finishing stroke or a compressed s; no grammatical choice is imposed. De is retained first with des as an explicit alternative.', 'revetement', 'low')
change('Main line 18, du before cancelled category', 'du', 'des', 'du', False, True,
    'misread word', 'Words',
    'The d is followed by a u-shaped low return. There is no separate e-plus-s group before the heavily cancelled category symbol.', 'du_groupoide_final')
change('Main line 18, cancelled category expression', r'\deleted{$\unsure{\mathcal T_{\mathrm{top}}}$}',
    r'\struck{\ill{}}', r'\deleted{$\unsure{\mathcal T_{\mathrm{top}}}$}', False, True,
    r'readable ink left as \ill{}', 'Struck text',
    'The cancelled expression has a large calligraphic-T-like body and a small lower top-like run. Multiple crossing/overwriting strokes prevent a secure symbol-by-symbol resolution, so the whole expression remains doubtful.', 'du_groupoide_final', 'low', True, True)
change('Main line 18, groupoïde ending', 'groupoïde', 'groupoïdes', 'groupoïde', False, True,
    'misread word', 'Words',
    'The word ends with the d stroke and low e return before the clear gap and large S of the category. There is no independent final s in that gap.', 'du_groupoide_final')
change('Marginal note, opening sign', r'$\Sigma$', r'$\widetilde{\Sigma}$',
    r'$\unsure{\widetilde{\Sigma}|\Sigma}$', True, False,
    'misread symbol or index', 'Symbols and indices',
    'A short separate upper stroke sits over the broad angular Sigma. It favours an accent, compatible with the short stroke over the tuple Sigma, but its exact join/shape is compressed. The tilde reading stays explicitly uncertain rather than being inferred from the mathematics.', 'margin', 'low', consequential=True)
change('Marginal note, est formellement', 'est formellement', r'\ill{}', 'est formellement', False, True,
    r'readable ink left as \ill{}', 'Readable ink left as illegible',
    'After ici, the short est group is live. The following line starts with a long f and has the compressed ormellement run ending in a terminal t-like finish. The cancellation starts only on the next word.', 'margin', 'medium', True)
change('Marginal note, cancelled first vide', r'\deleted{\unsure{vide}}', r'\struck{\ill{}}',
    r'\deleted{\unsure{vide}}', False, True,
    r'readable ink left as \ill{}', 'Struck text',
    'The old word after formellement has a low initial v/i-like run and a tall loop compatible with d, but the strike traverses its body. Vide is not resolved because all letters cannot be recovered under the stroke.', 'margin', 'low', True)
change('Marginal note, live vide', 'vide', r'\ill{}', 'vide', False, True,
    r'readable ink left as \ill{}', 'Readable ink left as illegible',
    'At the next marginal line the v, separate i dot, tall d and final e return are visible, followed by a dark comma. This live word is below and separate from the earlier cancellation.', 'margin_middle', marked_in_h=True)
change('Marginal note, autant and following word', r'\unsure{autant donc}', r'\ill{} \ill{}',
    r'autant \unsure{bien|donc}', True, True,
    'misread word', 'Words',
    'The low au run, tall crossed t and ant ending support autant. The next line begins with a looped tall letter followed by a short dotted/peaked run and low ending; bien is visually preferable, but the middle letters remain compressed and donc is retained as an alternative. No claim is made that the entire second word is decoded.', 'margin_middle', 'low', True)
change('Marginal note, middle phrase and imported main-line ink',
    r'\unsure{pour les mettre dans les}', r'les groupoïdes \ill{} dans les \ill{}',
    r'\unsure{pour les|pour se} mettre dans les', False, True,
    'insertion or placement', 'Insertions put in the wrong place',
    'The narrow note shows a p-starting short run and a following small compressed group, retained as pour les / pour se. The next line has the low me- strokes, tall tt strokes and re ending of mettre, then distinct dans and a short les. The larger groupoïdes at the right is on the main paragraph’s baseline: after rotating the note it slopes downward, unlike the note’s own lines. It is not duplicated into the margin.', 'margin_middle', 'low', True)
change('Marginal note, cas and following punctuation', r'\unsure{cas},', r'\ill{} \ill{} (',
    r'\unsure{cas}', True, True, 'other', 'Other',
    'The short word has a large open c, faint central stroke, and a final long turn compatible with s; cas stays doubtful. No separate dark comma follows it, and no independent opening parenthesis is visible before the following i.e. Both supplied punctuation marks are omitted.', 'margin_middle', 'low', True)
change('Marginal note, lower working-category phrase',
    r'i.e. travailler dans $S\mathcal T_{\mathrm{top}}^\pm$ au lieu de $S\mathcal TD_{\mathrm{top}}^\pm$',
    r'(i.e.\ $S\mathcal{T}^{\pm}_{\mathrm{top}} \subset S\mathcal{T}D^{\pm}_{\mathrm{top}}$) \ill{}',
    r'i.e. travailler dans $S\mathcal T_{\mathrm{top}}^\pm$ au lieu de $S\mathcal TD_{\mathrm{top}}^\pm$', False, True,
    r'readable ink left as \ill{}', 'Readable ink left as illegible',
    'The note spells i.e., travailler, dans and au lieu de. The two category expressions each have S, calligraphic T, top and a plus/minus sign; the second additionally has a separate capital D. There is no inclusion arrow/sign linking them. The short words occupy the intervening handwritten lines.', 'margin_lower', 'medium', True, True)
change('Marginal note, ending after second category', '.', 'absent', 'absent', True, False,
    'text not on the page', 'Text that is not on the page',
    'No separate dark terminal stop is visible next to the end of the second category expression. The isolated pale marks elsewhere in this crop are not added as punctuation.', 'margin_lower', 'medium')
change('Lower left handwritten folio', r'\mspage{63}', 'absent', r'\mspage{63}', False, True,
    'omission', 'Omissions',
    'The pale lower annotation has a closed lower bowl and upper turn for 6, then two rounded rightward turns for 3. Its writing hand is not securely attributable.', 'bottomfolio')

decisions = []
def decision(mark, status, reading, evidence, crop_name, confidence='high'):
    crop = crop_by_name[crop_name]
    decisions.append(dict(id=mark, decision=status, reading=reading, evidence=evidence,
        crop=crop['crop'], box=crop['box'], confidence=confidence))

decision('M0770', 'undecided', r'\unsure{\widetilde{\Sigma}|\Sigma}',
    'The complete tuple was read, including both commas, X, brackets and R. A short upper stroke favours a tilde over Sigma, but the upper bar and bracket overlap; plain Sigma remains possible.', 'pi_tuple', 'low')
decision('M0771', 'first', 'comme',
    'The open c, o, two m groups and terminal e are visible live after the cancelled phrase.', 'donnee_comme')
decision('M0772', 'first', 'nouvelle opération',
    'Two tall l loops settle nouvelle; the o/p beginning, accent, crossed t, dotted i and on ending settle opération. A gap before the closing parenthesis excludes an independent final s.', 'nouvelle')
decision('M0773', 'first', 'tte',
    'Two adjacent t stems with cross-strokes and a separate e give exactly the abbreviated tte.', 'representation')
decision('M0774', 'first', 'représentation',
    'The raised ré/p/résen/t/i/on sequence is readable above the old cancellation; the long p descender belongs to the live replacement.', 'representation', 'medium')
decision('M0775', 'first', 'du groupoïde par ens finis',
    'The d/u beginning, looped g and p descenders in groupoïde, par, e-n-s abbreviation, and f/i/n/i/s sequence can be followed across the whole line. There is no point after ens.', 'du_groupoide', 'medium')
decision('M0776', 'first', "d'un",
    'Baseline d has its loop and tall stem, followed by a separate apostrophe and distinct u/n low strokes. The curve preceding it belongs to the raised phrase’s insertion leader.', 'covering_insert')
decision('M0777', 'undecided', r'\unsure{définissant un}',
    'The tall f-like stem, dotted strokes, -issant ending and final un support this reading, but the initial dé area is overwritten. An opening square bracket is visible, with no matching closing bracket.', 'covering_insert', 'medium')
decision('M0778', 'undecided', r'autant \unsure{bien|donc}',
    'Autant has the low au run and tall t strokes. The following word’s looped beginning and short raised stroke favour bien, but its compressed middle is not fully legible.', 'margin_middle', 'low')
decision('M0779', 'undecided', r'\unsure{pour les|pour se} mettre dans les',
    'The initial p-starting run and short following group stay open. The next marginal line has visible me/tt/re, dans and les. The differently sloped large groupoïdes at right belongs to the main paragraph, not this note.', 'margin_middle', 'low')
decision('M0780', 'undecided', r'\unsure{cas}',
    'The open c and terminal long s-like turn are visible; the faint middle does not justify a full resolution. No independent comma is visible after it.', 'margin_middle', 'low')

implicit_decisions = []
for ident, reading, crop_name, evidence in [
    ('C064-D01', r'\unsure{une|des}', 'celle_des', 'The low cancelled word is to the right of live des. Its surviving humps favour une, but the strike masks enough letter bodies that des cannot be excluded.'),
    ('C064-D02', r'\unsure{reconstitution}', 'representation', 'The old long word is traversed by the cancellation and by a descender of the raised replacement; its centre is not letter-by-letter recoverable.'),
    ('C064-D03', r'\unsure{\mathcal T_{\mathrm{top}}}', 'du_groupoide_final', 'The large calligraphic-T-like form and lower top-like run remain heavily overworked. The whole cancelled formula is kept doubtful.'),
    ('C064-D04', r'\unsure{vide}', 'margin', 'The cancelled marginal word has only partial v/i/d/e-compatible traces; not every letter survives the strike clearly.')
]:
    crop = crop_by_name[crop_name]
    implicit_decisions.append(dict(id=ident, decision='undecided', reading=reading,
        evidence=evidence, crop=crop['crop'], box=crop['box'], confidence='low'))

doubts = [
    dict(place='Main line 10, cancelled word after live des', reading=r'\deleted{\unsure{une|des}}', alternatives='une; des', confidence='low', reason='A heavy cancellation obscures the low letter bodies; live des and the following position are secure.'),
    dict(place='Main line 11, Sigma within the full tuple', reading=r'$(X,[\unsure{\widetilde{\Sigma}|\Sigma}],R)$', alternatives='tilde Sigma; plain Sigma', confidence='low', reason='The short upper stroke is overworked with the symbol and bracket.'),
    dict(place='Main line 15, cancelled old word', reading=r'\deleted{\unsure{reconstitution}}', alternatives='reconstitution; unrecovered old word', confidence='low', reason='Cancellation and replacement descender prevent a complete literal reading.'),
    dict(place='Raised covering phrase', reading=r'\inserted{[\unsure{définissant un}}', alternatives='définissant un; initial overwritten letters unrecovered', confidence='medium', reason='The tall f and continuation are clearer than the overworked initial strokes; no closing bracket is supplied.'),
    dict(place='Main line 17, preposition before X', reading=r'\unsure{de|des}', alternatives='de; des', confidence='low', reason='The final hook does not securely distinguish a finishing stroke from s.'),
    dict(place='Main line 18, cancelled full category expression', reading=r'\deleted{$\unsure{\mathcal T_{\mathrm{top}}}$}', alternatives='calligraphic T with top; overworked source expression', confidence='low', reason='Several crossings obscure both the main symbol and small lower letters.'),
    dict(place='Marginal opening sign', reading=r'$\unsure{\widetilde{\Sigma}|\Sigma}$', alternatives='tilde Sigma; plain Sigma', confidence='low', reason='A separate short upper stroke favours an accent, but the exact shape is compressed.'),
    dict(place='Marginal cancelled first vide', reading=r'\deleted{\unsure{vide}}', alternatives='vide; unrecovered cancelled word', confidence='low', reason='The strike crosses letter bodies and not every letter is plain.'),
    dict(place='Margin, word after autant', reading=r'\unsure{bien|donc}', alternatives='bien; donc', confidence='low', reason='Looped beginning and short raised stroke favour bien; the middle is compressed.'),
    dict(place='Margin, short phrase before mettre', reading=r'\unsure{pour les|pour se}', alternatives='pour les; pour se', confidence='low', reason='The p-starting run and following small group cannot be completely segmented.'),
    dict(place='Margin, short word before i.e.', reading=r'\unsure{cas}', alternatives='cas; compressed middle letter unrecovered', confidence='low', reason='Only the large open c and long final turn are secure enough to support the proposal.')
]

inventory = []
def element(kind, position, first, hand='his hand'):
    inventory.append(dict(element=f'E{len(inventory)+1:02d}', sheet_kind='text',
        hand=hand, kind=kind, position=position, first_words_or_objects=first, transcribed='yes'))
element('text', 'Top centre', '20')
element('text', 'Upper seven main baselines', 'Mais ces opérations de bouchage')
element('insertion', 'Above main line 5', r'\textcircled{$5^\circ$}')
element('text', 'Main lines 8–21', 'Néanmoins, il y a')
element('deletion', 'Main line 8', 'une')
element('insertion', 'Above cancelled une', 'en')
element('deletion', 'Main line 10, after live des', r'\unsure{une|des}')
element('insertion', 'Above main line 11, before des and the tuple', r'$\Pi_1(X;R)$')
element('insertion', 'Above main line 12, attached after base-point R-comma', r'pour $R\ne\phi$,')
element('deletion', 'Main line 14', 'la donnée')
element('deletion', 'Main line 15', r'\unsure{reconstitution}')
element('insertion', 'Above main line 15, replacing cancelled word', 'représentation')
element('insertion', 'Above main line 16, attached before d’un', r'[\unsure{définissant un}')
element('insertion', 'Above main line 17', r"$X'$")
element('deletion', 'Main line 18, between du and groupoïde', r'$\unsure{\mathcal T_{\mathrm{top}}}$')
element('margin note', 'Left oblique note alongside groupoid and covering paragraph', r'$\unsure{\widetilde{\Sigma}|\Sigma}$ ici est formellement')
element('deletion', 'Second marginal baseline, after formellement', r'\unsure{vide}')
element('text', 'Lower left folio annotation', '63', 'unnamed hand (folio annotation; attribution uncertain)')

notes = [
    dict(id=f'{PAGE}-N01', text='The opening paragraph says that the bouchage operations are relatively superficial: at fixed g they do not relate the indicated objects to ones with smaller g. It points instead to erasing the cutting circles, labelled by the source’s raised circled 5°. The written numeral is retained; no cross-page renumbering is imported from H’s editorial note.'),
    dict(id=f'{PAGE}-N02', text='The next paragraph asks to make explicit the fundamental groupoids Pi_1(X;R) of the displayed triples, with the nonempty base-point condition and functorial dependence on R. The short form p^ts-base is preserved. The curved condition leader fixes its attachment after the baseline base-point phrase, while en tant que remains baseline text.'),
    dict(id=f'{PAGE}-N03', text='The rewritten passage speaks of every finite-set representation of the groupoid, an associated covering X-prime of X, and a new object of the displayed S T category. The author says that the question is already nontrivial for S_2 T_{0,3}, then calls the demand perhaps too ambitious. The page ends at car, leaving that reason unfinished. The cancelled predecessor, initial letters of the raised defining phrase, and de/des remain explicitly uncertain.'),
    dict(id=f'{PAGE}-N04', text='The margin says that the displayed Sigma is formally empty and ends with working in S T_top^± instead of S T D_top^±. Its middle wording is compressed and stays doubtful. The two category names and au lieu de were read directly; H’s inclusion symbol is unsupported. The larger groupoïdes on the right of the margin crop belongs to the main paragraph and is not repeated in the note.'),
    dict(id=f'{PAGE}-N05', text='Three long curved strokes function as attachment leaders under raised additions: Pi_1(X;R), the nonempty condition, and the defining phrase. No matching opening parentheses are manufactured from their curved left ends. The literal opening square bracket before the defining phrase is retained without an invented closing bracket; the source closing parentheses after opération and X are retained.'),
    dict(id=f'{PAGE}-N06', text='Every agreed main word and formula was compared on the original and prepared halves, then all differing words and resolved C doubts were inspected on enlarged crops. The original and each half were displayed once. Seventeen distinct places produced nineteen saved and actually viewed evidence files; the two additional files are targeted extensions of the still-open margin, not rereadings of settled text. No OCR, web reference or TeX compilation was used.'),
    dict(id=f'{PAGE}-N07', text='The initial five-image crop-view attempt returned a wholly truncated result, with no displayed image available for inspection. Those images were then successfully displayed in smaller batches; the nineteen recorded views count actual inspections, not the failed output. The pale lower 63 is recorded without attributing its hand.')
]

check_events = [
    dict(statement_id=f'{PAGE}-N01', type='carried as background without fault found', outcome='The claim about which operations can lower the indicated genus parameter is carried as the page states it. This first reading did not independently prove the claim or compare other leaves.'),
    dict(statement_id=f'{PAGE}-N02', type='carried as background without fault found', outcome='The page’s fundamental-groupoid and functoriality description is carried without an independent construction or proof in this reading.'),
    dict(statement_id=f'{PAGE}-N03', type='carried as background without fault found', outcome='The proposed passage from finite-set representations to coverings/new objects, and the stated nontriviality for S_2 T_{0,3}, are transcribed as source claims. Their proof is not asserted here.'),
    dict(statement_id=f'{PAGE}-N04', type='used and rechecked in this run', outcome='A local notation comparison checked both complete marginal category expressions: S, calligraphic T, top and ± recur, with D additionally present in the second. The intervening ink spells au lieu de. This verifies the reading relationship only; it is not a proof of a relation between the categories.'),
    dict(statement_id=f'{PAGE}-N04', type='carried as background without fault found', outcome='The mathematical reason for taking Sigma formally empty and changing the working category is carried as the note’s background claim. Its doubtful middle prose is not used to infer additional mathematical assumptions.')
]

notation = [
    dict(sign=r'\phi', meaning_or_form='Small oval with a long descending crossing stem, used for the empty set.', places='Raised condition R≠φ above main line 12.', universality='One nonempty condition on this page; only this occurrence is asserted here.', witness_errors='C normalizes it to varnothing and H to emptyset.'),
    dict(sign='Curved insertion leaders', meaning_or_form='A curved left end rises from an attachment point and continues horizontally beneath raised text; it can resemble an opening parenthesis at its left edge.', places='Pi_1(X;R), pour R≠φ, and the raised defining phrase.', universality='The same leader structure is visible at these three local additions.', witness_errors='C supplies an opening parenthesis before en tant que and places two additions before/after the wrong baseline phrase; H treats en tant que and d’un as part of additions.'),
    dict(sign=r'p\textsuperscript{ts}-base; tte; ens', meaning_or_form='Literal short forms: small raised ts after p; two t letters plus e; three low letters ens without a point.', places='Base-point phrase, quantifier before représentation, and finite-set phrase.', universality='Each short form occurs once on this page.', witness_errors='C misreads the base-point abbreviation; H expands points-base and reads les for tte and ces for ens.'),
    dict(sign=r'\unsure{\widetilde{\Sigma}|\Sigma}', meaning_or_form='Compact angular Sigma with a short upper stroke whose separation from the upper bar is not fully secure.', places='Middle entry of the triple and opening of the marginal note.', universality='The two local forms were compared; uncertainty is retained at both.', witness_errors='C gives plain Sigma, with doubt in the tuple only; H supplies a tilde securely.'),
    dict(sign='Terminal down-hook', meaning_or_form='A low word-ending hook may be a finishing stroke rather than an independent s.', places='Opération, revêtement, de/des, groupoïde.', universality='No blanket rule is imposed: the de/des case remains uncertain while independent final s strokes are absent at the other inspected endings.', witness_errors='H adds s to opération, revêtement and the final groupoïde; de/des remains open.'),
    dict(sign='Crossing descender of a raised replacement', meaning_or_form='A live raised p/f descender can cross the old cancellation or an insertion leader without making the raised word struck.', places='Représentation and the raised defining phrase.', universality='Both local overlaps were checked separately.', witness_errors='H leaves the replacement unreadable and appears to assign deletion to part of the raised defining phrase.')
]

abbreviations = [
    dict(form=r'p\textsuperscript{ts}-base', expansion='points-base'),
    dict(form='tte', expansion='toute'),
    dict(form='ens', expansion='ensembles'),
    dict(form='i.e.', expansion='id est')
]

margin_reading = r'\margin{$\unsure{\widetilde{\Sigma}|\Sigma}$ ici est formellement \deleted{\unsure{vide}} vide, autant \unsure{bien|donc} \unsure{pour les|pour se} mettre dans les \unsure{cas} i.e. travailler dans $S\mathcal T_{\mathrm{top}}^\pm$ au lieu de $S\mathcal TD_{\mathrm{top}}^\pm$}'
second_boxes = []
def audit(kind, box, reading):
    second_boxes.append(dict(box=f'B{len(second_boxes)+1:02d}', kind=kind,
        x0=box[0], y0=box[1], x1=box[2], y1=box[3], reading=reading))
audit('handwritten number', [748,31,854,92], r'\mspage{20}')
audit('different words', crop_by_name['bouchage']['box'], 'bouchage')
audit('different words', crop_by_name['cela']['box'], 'en cela')
audit('insertion', crop_by_name['operation5']['box'], r"l'opération \inserted{\textcircled{$5^\circ$}} de")
audit('struck passage', crop_by_name['liaison']['box'], r'\deleted{une} \inserted{en} liaison')
audit('different words', crop_by_name['avec_ca']['box'], 'avec ça,')
audit('struck passage', crop_by_name['celle_des']['box'], r"c'est celle des \deleted{\unsure{une|des}}")
audit('doubtful formula', crop_by_name['pi_tuple']['box'], r'\inserted{$\Pi_1(X;R)$} des $(X,[\unsure{\widetilde{\Sigma}|\Sigma}],R)$,')
audit('insertion', crop_by_name['nonempty_base']['box'], r'p\textsuperscript{ts}-base dans $R$, \inserted{pour $R\ne\phi$,} en tant que')
audit('struck passage', crop_by_name['donnee_comme']['box'], r'\deleted{la donnée} comme')
audit('different words', crop_by_name['nouvelle']['box'], 'nouvelle opération)')
audit('struck passage', crop_by_name['representation']['box'], r'pour tte \deleted{\unsure{reconstitution}} \inserted{représentation}')
audit('different words', crop_by_name['du_groupoide']['box'], 'du groupoïde par ens finis,')
audit('insertion', crop_by_name['covering_insert']['box'], r"\inserted{[\unsure{définissant un}} d'un")
audit('insertion', crop_by_name['revetement']['box'], r"revêtement \inserted{$X'$} \unsure{de|des} $X$),")
audit('doubtful formula', [304,1890,1245,2039], r'du \deleted{$\unsure{\mathcal T_{\mathrm{top}}}$} groupoïde $S\mathcal T_{\mathrm{top}}^\pm$.')
audit('handwritten number', [650,2025,1030,2145], r'$S_2\mathcal T_{0,3}$')
audit('margin note', crop_by_name['margin']['box'], margin_reading)
audit('handwritten number', crop_by_name['bottomfolio']['box'], r'\mspage{63}')

data = dict(page=PAGE, reader='reader_a', lines_read=39,
    places_cropped=17, crop_files_saved=len(crops), crop_files_viewed=sum(r['viewed'] for r in crops),
    reading_record=dict(original_views=1, prepared_half_views=[1,1],
        main_baselines=21, raised_baselines=7, marginal_baselines=9, folio_baselines=2,
        all_agreements_read=True, no_ocr=True, no_web=True, no_tex_compilation=True),
    changes=changes, decisions=decisions, implicit_decisions=implicit_decisions, doubts=doubts,
    inventory=inventory, notes=notes, check_events=check_events, notation=notation,
    abbreviations=abbreviations, second_boxes=second_boxes)

output = ROOT / 'proposed' / f'{PAGE}.json'
output.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(dict(page=PAGE, changes=len(changes), decisions=len(decisions),
    implicit_decisions=len(implicit_decisions), doubts=len(doubts),
    second_boxes=len(second_boxes), places_cropped=17, crop_files=len(crops)), ensure_ascii=False))
