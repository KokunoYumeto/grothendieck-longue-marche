from pathlib import Path
import csv
import json

ROOT = Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work')
PACKET = ROOT / 'packets/145_scan010'
OUT = ROOT / 'edition/reader_reports'
OUT.mkdir(parents=True, exist_ok=True)
boxes = json.loads((ROOT / 'edition/crops/145_scan010_crop_boxes.json').read_text())

def locus(n):
    stem = next(k for k in boxes if k.startswith(f'145_scan010_{n:02d}_'))
    return {'crop': f'crops/{stem}.png', 'box': boxes[stem]}

changes = []
def change(place, C, H, final, ink, confidence, kind, c_changed, h_changed,
           marked_in_H, n, categories, consequence=''):
    obj = dict(id=f's010-{len(changes)+1:02d}', place=place, C=C, H=H,
               final=final, ink=ink, confidence=confidence, kind=kind,
               c_changed=c_changed, h_changed=h_changed,
               marked_in_H=marked_in_H, **locus(n),
               error_category=categories, math_consequence=consequence)
    changes.append(obj)
    return obj['id']

opening = change(
    'Opening continuation, upper main text', 'ou encore', 'on aura', 'ou encore',
    'The first word has a rounded o followed by an open low u. The second has the connected e-n-c-o-r-e sequence, including the rounded medial o and final low e; it is longer than aura.',
    'high', 'misread word', False, True, 'no', 1, [2])
initial = change(
    'First word of the oblique left marginal note', 'Il', 'il', 'il',
    'A short dotted i precedes the tall looped l. The first letter is at the small marginal x-height, not an upper-case I.',
    'high', 'misread word', True, False, 'no', 2, [2])
phantom_strike = change(
    'First marginal formula, between l_0^beta and g',
    r'\sigma_\infty(g^{-1})=l_0^\beta gl_1^\gamma',
    r'\sigma_\infty(g^{-1}) = l_0^{\beta}\, \struck{\ill{}}\, g\, l_1^{\gamma}',
    r'\sigma_\infty(g^{-1})=l_0^\beta gl_1^\gamma',
    'The descending curved stroke continues from the f of forme on the preceding marginal line. It is not a cancellation and covers no separate word or symbol. The l_0^beta, g, and l_1^gamma remain live.',
    'high', 'text not on the page', False, True, 'yes', 2, [7, 9])
phantom_condition = change(
    'Middle of the oblique margin, where it meets main-text Condition',
    '', r'(conditions \uncertain{de} définition)', '',
    'The large Condition and adjacent horizontal writing belong to the main-text parenthesis, at a different angle and scale. There is no small oblique phrase conditions de définition between the marginal formula and on trouve.',
    'high', 'text not on the page', False, True, 'yes', 3, [9])
passage = change(
    'Marginal prose following the first formula',
    r'on trouve, en \unsure{passant} au groupe \unsure{abélien}',
    r'\ill{} on trouve \ill{} \ill{}',
    'on trouve, en passant au groupe abélien',
    'The slanted writing gives on trouve, en, then passant with a p descender and terminal t. The next group has au groupe and abélien, with a looped b, an accent over é, the tall l, dotted i, and the final connected en. H leaves these readable groups as illegible. Removal of the two C doubt wrappers is recorded separately in decisions.',
    'high', r'readable ink left as \ill{}', False, True, 'yes', 3, [2, 3, 5])
connector = change(
    'Boundary immediately after marginal abélien', ', que', '', '',
    'After the final n of abélien there is no further small marginal word or comma. The nearby larger que is on the main display baseline in tels que, at a different angle after rotation. C has borrowed a connector absent from the marginal note.',
    'high', 'text not on the page', True, False, 'no', 14, [9])
beta_gamma = change(
    'Marginal equations between abélien and donc',
    r'$\beta=\gamma$ (i.e. $q=-r$)',
    r'(i.e. $\beta = r$, $\gamma = -q$)',
    r'$\beta=\gamma$ (i.e. $q=-r$)',
    'The first equation has beta with its double-lobed stem, an equals sign, and a descending gamma. In the parenthesis the left character is q with a descending tail, followed by equals, a short minus, and r. The two equations are separately legible.',
    'high', 'misread symbol or index', False, True, 'no', 3, [1, 3],
    'The note asserts equality of beta and gamma and gives q=-r as its equivalent condition; it does not state the two separate identifications written by H.')
final_beta = change(
    'Last marginal formula, exponent on the final l_1',
    r'\sigma_\infty(g^{-1})=l_0^\beta gl_1^\beta',
    r'\sigma_\infty(g^{-1}) = l_0^{\beta}\, g\, l_1^{\gamma}',
    r'\sigma_\infty(g^{-1})=l_0^\beta gl_1^\beta',
    'The final superscript has the same rising stem and two lobes as the beta over l_0 in this very formula. It lacks the descending gamma shape of the earlier marginal formula. The inverse exponent -1 and both subscripts 0 and 1 are also visible.',
    'high', 'misread symbol or index', False, True, 'no', 4, [1],
    'Both generator factors in the last marginal expression carry beta.')
condition = change(
    'Main text, parenthesis following the boxed display', 'Condition', 'condition', 'Condition',
    'After the opening parenthesis the initial C is a larger open curve extending above the following small letters. The parenthesis remains open on this page.',
    'high', 'misread word', False, True, 'no', 5, [2])
si = change(
    'Start of the replacement sentence on the next main-text line', 'Si', 'si', 'Si',
    'The initial S is a tall independent opening stroke before the short dotted i. The sentence begins on its own manuscript line after the semicolon in the preceding line.',
    'high', 'misread word', False, True, 'no', 6, [2])
dependent = change(
    'Main text following the simplified relation, after (q,r) ne',
    'dépendent', 'dépend', 'dépendent',
    'After the tall d in the latter part of dépend there is a further low continuation and a small detached upstroke before que. This is the contracted ent ending; the internal e/n strokes are compressed. The root reader independently concurred on the saved crop.',
    'medium', 'misread word', False, True, 'no', 7, [2])
autom_first = change(
    'First occurrence, l\'autom ext. défini par u', 'autom ext.', 'autom. ext.', 'autom ext.',
    'The final low m of autom is followed by a clear blank. The separate dark full stop is after the t of ext. There is no stop after autom.',
    'high', 'abbreviation expanded or spelling modernised', False, True, 'no', 8, [8, 9])
struck = change(
    'Cancellation after et pas du',
    r'\deleted{\unsure{choix de u}}', r'\struck{choix}',
    r'\deleted{\unsure{choix de u}}',
    'The cancellation continues through the small groups after choix, rather than stopping at choix. The initial ch, the dotted i, and part of de are visible, but the last character and some joins are entangled with the strike. Retain the doubt over the whole proposed choix de u; the crop does not justify resolving every letter.',
    'low', 'deletion state', False, True, 'no', 9, [3, 7])
son = change(
    'Live text immediately after the cancelled passage',
    'de son représentant', r'\uncertain{des} représentants', 'de son représentant',
    'There are separate de and son groups before représentant. The d has a loop and ascender; son begins with its own short s. The final word ends in a raised t without a further plural s.',
    'high', 'misread word', False, True, 'yes', 9, [2])
travaille = change(
    'Opening of the final paragraph, after On sait que,',
    'si on travaille sur', r'\uncertain{travaillant} avec', 'si on travaille sur',
    'Before the tall initial t of travaille are separate short si and on groups, although on is faint. In travaille the two l ascenders and the dotted i are present, followed by a low final e. The following three-letter group is sur; it does not have the longer avec sequence.',
    'high', 'misread word', False, True, 'yes', 10, [2, 3])
autom_last = change(
    'Final paragraph, l\'autom ext. identique', 'autom ext.', 'autom. ext.', 'autom ext.',
    'The end of autom is a low connected m followed by a wide blank; the stop is visibly after ext. The proposed stop after autom has no ink.',
    'high', 'abbreviation expanded or spelling modernised', False, True, 'no', 11, [8, 9])
insertion = change(
    'Small insertion above que in the final paragraph',
    r'\inserted{donc $p=\pm1$ et}', r'\marginal{des $p = \pm 1$ et}',
    r'\inserted{donc $p=\pm1$ et}',
    'The first small word has a looped rising d, low o/n connection, and final c: donc. The p, equals sign, plus-minus and 1 are clear, followed by et. A curved insertion stroke places this above-line phrase before que; it is not a free-standing margin note.',
    'high', 'insertion or placement', False, True, 'no', 12, [2, 6],
    'The phrase supplies the additional condition p=±1 at the point en exigeant ... que.')
footer = change(
    'Handwritten lower-left page number', r'\mspage{9}', '', r'\mspage{9}',
    'A single 9 has a closed upper loop and a long descending curved stem at the lower left of the sheet. This is physical source ink, not an editorial page header.',
    'high', 'omission', False, True, 'no', 13, [3])

tex = r'''\scanpage{10}
ou encore
\[
\exists\ q,r\in\hat{\mathbb Z}^{*}\quad\text{tels que}\quad\boxed{gl_1^q\sigma_\infty(g)=l_0^r}
\]
\margin{il vaut mieux écrire la relation sous la forme
\[
\sigma_\infty(g^{-1})=l_0^\beta gl_1^\gamma,
\]
on trouve, en passant au groupe abélien $\beta=\gamma$ (i.e. $q=-r$) donc
\[
\sigma_\infty(g^{-1})=l_0^\beta gl_1^\beta
\]}
(Condition qui ne dépend que de $g$, pas de $p$;

Si $g$ est remplacé par $g'=l_0^\alpha gl_1^{-\alpha}$, on aura $\sigma_\infty(g')=l_1^\alpha\sigma_\infty(g)l_0^{-\alpha}$, et la relation
\[
g'l_1^{q'}\sigma_\infty(g')=l_0^{r'}
\]
s'écrit
\[
l_0^\alpha gl_1^{-\alpha}l_1^{q'}l_1^\alpha\sigma_\infty(g)l_0^{-\alpha}=l_0^{r'}
\]
i.e. en simplifiant
\[
gl_1^{q'}\sigma_\infty(g)=l_0^{r'}
\]
donc $q=q'$, $r=r'$ i.e. $(q,r)$ ne dépendent que de l'autom ext. défini par $u$, et pas du \deleted{\unsure{choix de u}} de son représentant dans le normalisateur de $L_0$.

Dans le cas de $\tau$, où $g=l_1$, la relation devient
\[
l_1l_1^ql_0=l_0^r\quad\text{donc}\quad q=-1,\ r=1.
\]
On sait que, si on travaille sur les groupes discrets, en plus de l'autom ext. identique, il n'y a qu'une seule autre solution de nos équations (en exigeant \inserted{donc $p=\pm1$ et} que $l_0^p$ et $\operatorname{int}(g)l_1^p$ engendrent $\pi$, en plus des relations fondamentales
\mspage{9}
'''

decisions = [
    dict(id='M0792', decision='first', reading='passant',
         ink='The slanted word has a descending p, low a/ss/a/n sequence and a terminal t ascender; the letters remain separable after rotation and enlargement.',
         **locus(3), confidence='high'),
    dict(id='M0793', decision='first', reading='abélien',
         ink='The a is followed by a tall looped b; an accent is visible over é, then a tall l, dotted i and low en. These are not obscured by the intersecting main text.',
         **locus(3), confidence='high'),
]

inventory = []
def item(kind, position, text, box):
    inventory.append(dict(element=f'E{len(inventory)+1:02d}', kind=kind,
                          position=position, first_words_or_objects=text,
                          box=box, sheet_kind='text', hand='his hand',
                          transcribed='yes'))

item('text', 'Top main text', 'ou encore', [300,70,607,145])
item('display', 'Top, including rectangular frame around the equality',
     r'\exists q,r\in\hat{\mathbb Z}^{*}; gl_1^q\sigma_\infty(g)=l_0^r', [290,149,1641,306])
item('margin note', 'Oblique left margin, read upward along its slanted lines',
     'il vaut mieux écrire la relation sous la forme', [20,111,642,1177])
item('display', 'First formula inside the oblique margin',
     r'\sigma_\infty(g^{-1})=l_0^\beta gl_1^\gamma', [22,111,335,560])
item('text', 'Middle part of the oblique margin, including two small equations',
     r'on trouve, en passant au groupe abélien $\beta=\gamma$ (i.e. $q=-r$)', [20,245,642,933])
item('display', 'Last formula in the oblique margin, after donc',
     r'\sigma_\infty(g^{-1})=l_0^\beta gl_1^\beta', [25,862,301,1177])
item('text', 'Main text under the top display',
     '(Condition qui ne dépend que de g, pas de p;', [280,321,1564,421])
item('text', 'Next two main-text lines, including two inline equations',
     'Si g est remplacé par', [277,410,1640,638])
item('display', 'Main relation for the replaced g',
     r"g'l_1^{q'}\sigma_\infty(g')=l_0^{r'}", [400,635,1450,765])
item('text', 'Short lead-in above expanded relation', "s'écrit", [292,777,611,846])
item('display', 'Long expanded relation across the main column',
     r'l_0^\alpha gl_1^{-\alpha}l_1^{q\prime}l_1^\alpha', [280,846,1645,991])
item('text', 'Short lead-in above simplified relation', 'i.e. en simplifiant', [292,996,760,1066])
item('display', 'Simplified relation in the main column',
     r"gl_1^{q'}\sigma_\infty(g)=l_0^{r'}", [400,1060,1510,1201])
item('text', 'Four-line conclusion about the outer automorphism and its representative',
     r"donc $q=q'$, $r=r'$", [223,1180,1637,1615])
item('deletion', 'Start of line after et pas du, before live de son représentant',
     r'\deleted{\unsure{choix de u}}', [223,1398,458,1518])
item('text', 'Paragraph introducing the special case tau',
     r'Dans le cas de $\tau$, où $g=l_1$', [285,1623,1592,1727])
item('display', 'Special-case calculation below tau sentence',
     r'l_1l_1^ql_0=l_0^r; q=-1, r=1', [285,1727,1592,1840])
item('text', 'Final five main-text lines, continuing beyond this page',
     'On sait que, si on travaille sur les groupes discrets', [270,1848,1645,2337])
item('insertion', 'Small above-line addition attached before que after en exigeant',
     r'\inserted{donc $p=\pm1$ et}', [866,2089,1165,2172])
item('text', 'Lower-left handwritten page number', r'\mspage{9}', [28,2260,86,2341])

second = []
def second_box(kind, coords, reading):
    second.append(dict(box=f'B{len(second)+1:02d}', kind=kind, coords=coords, reading=reading))

second_box('C/H word disagreement', [300,70,607,145], 'ou encore')
second_box('Whole boxed display; handwritten generator indices 1 and 0',
           [290,149,1641,306],
           r'\[\exists\ q,r\in\hat{\mathbb Z}^{*}\quad\text{tels que}\quad\boxed{gl_1^q\sigma_\infty(g)=l_0^r}\]')
second_box('Upper marginal note; lower-case initial; alleged deletion; complete formula and its digits',
           [22,111,335,560],
           r'\margin{il vaut mieux écrire la relation sous la forme \[\sigma_\infty(g^{-1})=l_0^\beta gl_1^\gamma,\]}')
second_box('Middle marginal note; both C doubts; C/H word and equation disagreements; absent connector after abélien',
           [20,194,831,933],
           r'\margin{on trouve, en passant au groupe abélien $\beta=\gamma$ (i.e. $q=-r$)}')
second_box('End of marginal note; entire formula containing the beta/gamma disagreement and numeric indices',
           [25,862,301,1177],
           r'\margin{donc \[\sigma_\infty(g^{-1})=l_0^\beta gl_1^\beta\]}')
second_box('C/H initial-letter disagreement and unclosed authorial parenthesis',
           [280,321,1564,421],
           r'(Condition qui ne dépend que de $g$, pas de $p$;')
second_box('C/H initial-letter disagreement; complete replacement formula with indices 0 and 1',
           [277,410,1440,535],
           r"Si $g$ est remplacé par $g'=l_0^\alpha gl_1^{-\alpha}$, on aura")
second_box('Complete sigma formula containing handwritten indices 1 and 0',
           [277,530,1640,638],
           r"$\sigma_\infty(g')=l_1^\alpha\sigma_\infty(g)l_0^{-\alpha}$, et la relation")
second_box('Entire displayed relation with numeric generator indices and primes',
           [400,635,1450,765],
           r"\[g'l_1^{q'}\sigma_\infty(g')=l_0^{r'}\]")
second_box('Entire expanded displayed relation with all numeric indices and primes',
           [280,846,1645,991],
           r"\[l_0^\alpha gl_1^{-\alpha}l_1^{q'}l_1^\alpha\sigma_\infty(g)l_0^{-\alpha}=l_0^{r'}\]")
second_box('Entire simplified displayed relation with numeric indices and primes',
           [400,1060,1510,1201],
           r"\[gl_1^{q'}\sigma_\infty(g)=l_0^{r'}\]")
second_box('C/H word-ending disagreement in dépendent, with the preceding equalities',
           [278,1180,1637,1315],
           r"donc $q=q'$, $r=r'$ i.e. $(q,r)$ ne dépendent que")
second_box('C/H abbreviation punctuation disagreement, first autom',
           [277,1298,1637,1420],
           r"de l'autom ext. défini par $u$, et pas du")
second_box('Complete cancellation, retained C doubt, live de son représentant, and following numeric L_0',
           [223,1398,1637,1615],
           r'\deleted{\unsure{choix de u}} de son représentant dans le normalisateur de $L_0$.')
second_box('Special-case introduction and complete calculation; all handwritten 0, 1, -1',
           [285,1623,1592,1840],
           r'Dans le cas de $\tau$, où $g=l_1$, la relation devient \[l_1l_1^ql_0=l_0^r\quad\text{donc}\quad q=-1,\ r=1.\]')
second_box('C/H lexical disagreement in final paragraph',
           [594,1848,1267,1970], 'si on travaille sur les')
second_box('C/H abbreviation punctuation disagreement, second autom',
           [799,1941,1285,2062], "l'autom ext.")
second_box('Above-line insertion and attachment; full p=±1 and both adjacent generator formulas',
           [866,2089,1522,2240],
           r'\inserted{donc $p=\pm1$ et} que $l_0^p$ et $\operatorname{int}(g)l_1^p$')
second_box('Handwritten page number', [28,2260,86,2341], r'\mspage{9}')

diffs = list(csv.DictReader((PACKET/'differences.tsv').open(), delimiter='\t'))
coverage = []
substantive = {
    1: ([opening], 'The scan marker 10 is editorial; the actual opening word disagreement is substantive.'),
    5: ([initial,phantom_strike,phantom_condition,passage,connector,beta_gamma,final_beta,condition,si],
        'Long alignment shift caused by placement of the oblique margin. The marginal content and the two main-text initials are adjudicated in the linked loci; H note wrappers are editorial.'),
    20: ([dependent], ''),
    21: ([autom_first], ''),
    22: ([struck,son], 'The cancellation extends beyond choix; the following live words are de son représentant.'),
    23: ([initial,phantom_strike,phantom_condition,passage,connector,beta_gamma,final_beta],
         'The long shifted H margin is adjudicated in the linked loci. Both H note paragraphs are editorial. The tau sentence is present in both witnesses and in the ink.'),
    27: ([travaille], ''),
    28: ([autom_last], ''),
    29: ([insertion], ''),
    31: ([footer], 'This is the physical handwritten footer 9, retained as mspage; it is not an H editorial header.'),
}
for n, raw in enumerate(diffs, 1):
    row = {'row': n}
    if n in substantive:
        ids, explanation = substantive[n]
        row.update(status='substantive', change_id=ids[0])
        if len(ids)>1:
            row['related_change_ids']=ids[1:]
        if explanation:
            row['explanation']=explanation
    else:
        if n in (7,10):
            explanation='Inline-versus-display delimiters around the same sigma equation; no source reading changes.'
        elif n == 26:
            explanation=r'The semicolon token comes from H TeX \; spacing after the same written comma, not an ink semicolon.'
        else:
            explanation=r'Tokenization of TeX thin-space \, and adjacent multiplication factors; the same letters, indices and signs are present in both readings and in the ink.'
        row.update(status='macro/editorial', explanation=explanation)
    coverage.append(row)

report = {
    'scan': 10,
    'reader': '/root/reader_b',
    'lines_read': 31,
    'layout': 'One sheet of handwritten subject notes, upright, with a short top continuation and a framed existential relation; an oblique left marginal note runs beside the upper half. The main column develops a replacement of g through three displays, a four-line conclusion with one cancellation, then a tau example and a final five-line paragraph with a small above-line insertion. A handwritten 9 stands at the lower left. The whole and two original overlapping halves were viewed once each; targeted crops were then used for open places and disagreements. No diagram or drawing is present; the rectangular equation frame is reproduced with boxed.',
    'changes': changes,
    'decisions': decisions,
    'doubts': [
        {'place': 'Cancelled passage after et pas du',
         'reading': r'\deleted{\unsure{choix de u}}',
         'alternatives': ['The last word or some joined letters remain obscured; no confident alternative is supplied.'],
         'confidence': 'low',
         'reason': 'The strike is entangled with the letters after choix and in the final proposed u. Not every letter is plain, so C\'s nested uncertainty is retained.'}
    ],
    'inventory': inventory,
    'second_boxes': second,
    'notation': [
        {'observation': 'The recurring generator is lower-case looped l with subscript 0 or 1; capital L_0 is used for the normalizer at the end of the representative sentence.',
         'places': 'All main and marginal generator formulas; main paragraph ending normalisateur de L_0.',
         'qualification': 'Local comparison only; the l stems are taller than their numeric subscripts.'},
        {'observation': 'The marginal beta has a rising stem with two lobes; gamma has the distinct descending form. The first formula uses beta and gamma, the intermediate line beta=gamma, and the final formula beta twice.',
         'places': 'Oblique marginal note, crops02–04.',
         'qualification': 'These particular occurrences were read individually; no extension to other pages is inferred.'},
        {'observation': 'Primes occur on g, q and r in the replacement computation; the marginal inverse is g^{-1}. Sigma consistently has an infinity subscript in these displayed occurrences.',
         'places': 'Replacement sentence and its displays; two marginal formulas.',
         'qualification': 'No incidental ink dots have been added as primes.'},
        {'observation': 'The first line has a hat over the integer-group letter and a star; only the equality is enclosed by a drawn rectangle.',
         'places': 'Top existential display.',
         'qualification': 'The frame is encoded with boxed; no formula number appears.'},
        {'observation': 'The final generator condition ends with a small pi-shaped group sign, transcribed as pi in agreement with its local size.',
         'places': 'Final main-text line, engendrent pi.',
         'qualification': 'This is not a global ruling on Pi/pi letter case beyond this page.'},
    ],
    'hand': [
        {'habit': 'A long descender can cross another line without cancelling it.',
         'places': 'f of forme above the first marginal formula.',
         'universal_on_this_page': False,
         'witness_effect': 'H inserts a struck illegible item between l_0^beta and g; the stroke belongs to the f.'},
        {'habit': 'The oblique marginal writing crosses the visual territory of larger horizontal main text.',
         'places': 'Middle of the left marginal note beside Condition and the upper tels que.',
         'universal_on_this_page': False,
         'witness_effect': 'H transfers a nonexistent conditions de définition into the margin; C adds , que after abélien from neighboring main text.'},
        {'habit': 'Low connected endings may be highly compressed and a terminal upstroke detached.',
         'places': 'dépendent after (q,r) ne; faint on in si on travaille.',
         'universal_on_this_page': False,
         'witness_effect': 'H loses the ent ending and the small words si on.'},
        {'habit': 'The abbreviation autom has no full stop, while the following ext. has a distinct stop.',
         'places': 'Both occurrences on this page.',
         'universal_on_this_page': True,
         'witness_effect': 'H supplies autom. in both places.'},
        {'habit': 'Small inserted words use the same cursive forms as the main text, with a curved link locating the addition.',
         'places': 'donc p=±1 et above que in the final paragraph.',
         'universal_on_this_page': False,
         'witness_effect': 'H reads des and labels the addition as a margin note.'},
    ],
    'abbreviations': [
        {'form':'autom', 'expansion':'automorphisme', 'place':'Both occurrences of autom ext.'},
        {'form':'ext.', 'expansion':'extérieur', 'place':'Both occurrences of autom ext.'},
        {'form':'i.e.', 'expansion':'id est', 'place':'Marginal parenthesis; en simplifiant; conclusion after q=q\' and r=r\'.'},
        {'form':'int', 'expansion':'intérieur, in the notation for inner conjugation', 'place':'Final paragraph, int(g)l_1^p.'},
    ],
    'notes': [
        'The page continues an equivalent condition on g: the author writes an existential relation with q,r in the starred hatted integer group and frames the equation. The marginal note recommends the inverse form sigma_infinity(g^{-1})=l_0^beta g l_1^gamma, says that passage to the abelian group gives beta=gamma (i.e. q=-r), and repeats the inverse form with beta on both generator factors.',
        'In the main text the author replaces g by l_0^alpha g l_1^{-alpha}, writes the corresponding expression for sigma_infinity(g\'), substitutes it into a relation with q\',r\', and gives an expanded and a simplified equality. He concludes that q,r depend on the outer automorphism defined by u, not on its representative in the normalizer of L_0. The cancelled phrase before de son représentant remains uncertain and has not been silently repaired.',
        'For tau, the author uses g=l_1 and writes q=-1,r=1. The final paragraph says that for the discrete groups, besides the identical outer automorphism, there is only one other solution to the equations under the indicated generator and fundamental-relation requirements. An insertion supplies donc p=±1 et before que. The final sentence continues beyond the sheet; no continuation from another scan was consulted.',
        'The opening main-text parenthesis before Condition is not closed on this sheet, and the final en exigeant parenthesis is also open at the page end. These remain as written. There is no authorial date or explicit doubt phrase on this page. The handwritten page number is 9 at the lower left.',
        'C\'s lower-case/upper-case distinction at the marginal initial and its added , que after abélien have been corrected from the ink. C\'s two indexed doubt marks are resolved on crop03. Its nested doubt inside the cancellation is retained. H\'s two note paragraphs are editorial and are excluded from the transcription. The long main word normalisateur crosses a manuscript line break; it is transcribed continuously.',
        'No mathematical proof, formal computation, or independent algebra check was performed by this reader. Statements above describe the author\'s claims. Root reviewed the fourteen existing crops and concurred on the reported readings before this report was finalized; any separate root algebra check is not claimed here.',
    ],
    'check_events': [],
    'diff_coverage': coverage,
}

assert len(diffs) == 31
assert len(coverage) == 31
assert all(c['c_changed'] or c['h_changed'] for c in changes)
assert [d['id'] for d in decisions] == [r['id'] for r in csv.DictReader((PACKET/'marks.tsv').open(), delimiter='\t')]
assert all((ROOT/'edition'/c['crop']).exists() for c in changes+decisions)
assert all(i['sheet_kind']=='text' and i['hand']=='his hand' and i['transcribed']=='yes' for i in inventory)
assert len({b['box'] for b in second}) == len(second)
assert all(0 <= b['coords'][0] < b['coords'][2] <= 1678 and 0 <= b['coords'][1] < b['coords'][3] <= 2360 for b in second)
assert tex.count('{') == tex.count('}')
assert tex.count(r'\unsure{') == 1

(OUT/'145_scan010.tex').write_text(tex)
(OUT/'145_scan010.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
print(json.dumps({'scan':10, 'changes':len(changes), 'c_substantive_changes':sum(c['c_changed'] for c in changes), 'decisions':len(decisions), 'doubts':len(report['doubts']), 'inventory':len(inventory), 'second_boxes':len(second), 'crop_count':len(boxes), 'diff_rows':len(coverage)}, ensure_ascii=False))
