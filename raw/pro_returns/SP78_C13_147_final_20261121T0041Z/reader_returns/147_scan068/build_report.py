import csv
import json
import re
from pathlib import Path

root = Path('/workspace/scratch/ea90d891106a')
work = root / 'SP78_C13_147_work'
out = work / 'reader_returns/147_scan068'
packet = root / 'runtime/packets/147_scan068'
boxes = json.loads((out / 'crop_boxes.json').read_text())
proposed = (out / 'proposed.tex').read_text()
changes = []

def change(place, c, h, final, evidence, crop, confidence='high', against_c=False,
           against_h=True, kind='misread word', sheet='words', marked=True,
           consequential=False):
    key = f'{crop:02}'
    changes.append(dict(
        id=f'068-{len(changes)+1:02}', place=place, C=c, H=h, final=final,
        evidence=evidence, crop=f'147_scan068_place{key}.png', box=boxes[key],
        confidence=confidence, against_C=against_c, against_H=against_h,
        kind=kind, marked_in_H=marked, error_sheet_kind=sheet,
        consequential=consequential))

change('Heading, after Proposition', r'\uline{Proposition}', r'\emph{Proposition.}',
       r'\uline{Proposition}',
       'The final n ends in its ordinary return, then blank paper precedes Le. The underline is below the word; no separate full stop follows it.', 1,
       kind='text not on the page', sheet='text not on page', marked=False)
change('First line, inserted divisor notation', r'\inserted{$M^\infty_{0,I}$}',
       r'(\add{$M^{\infty}_{0,I}$})', r'\inserted{$M^\infty_{0,I}$}',
       'The complete M has a raised two-loop infinity and lower 0,I. A continuous curved connector leads from the inserted formula to the gap before de; it is not a pair of enclosing parentheses.', 2,
       kind='insertion or placement', sheet='insertions put in wrong place', marked=False)
change('Proposition, adjective after courbe', r'\unsure{standart|stable}',
       r'\uncertain{stable}', 'standart',
       'After the initial st, the line has compressed an, a tall looped d, low ar, and a final tall angular t with a short cross stroke. There is no b-shaped loop. The terminal t is preserved as written.', 3)
change('Proposition, inserted adjective and attachment', r'\inserted{déployée}',
       r'\add{\uncertain{déployée}} \uncertain{stable}',
       r'\inserted{\unsure{déployé|déployée}}',
       'The descending y returns into one short terminal e-shaped group under an accent. A second e is not separately distinguishable, but the compressed ending does not exclude it. The connector starts after standart, so the insertion follows that word. Neither ending is ruled out by agreement with courbe.', 3,
       confidence='medium', against_c=True, kind='insertion or placement',
       sheet='insertions put in wrong place')
change('Proposition, base of Spec', r'$\operatorname{Spec}\mathbf Z$',
       r'$\operatorname{Spec}\mathbb{Z}$', r'$\operatorname{Spec}\mathbb Z$',
       'The Z has two separated diagonal tracks between its upper and lower bars, rather than one thick diagonal.', 3,
       against_c=True, against_h=False, kind='misread symbol or index',
       sheet='symbols and indices', marked=False)
change('Proposition, first dodécaèdre adjective', 'dodécaèdre gauche',
       'dodécaèdre grand', 'dodécaèdre gauche',
       'The adjective begins with a descending looped g; after low au are the c and a tall h shoulder, followed by a short e. The ending is not the nd group of grand.', 5, marked=False)
change('Marginal NB, arrow and first description',
       r'$\widehat M_{0,I}\longrightarrow$ un vrai schéma projectif et lisse',
       r'$\widehat{M}_{0,I}$ \uncertain{est} un vrai schéma, \uncertain{projectif} et \uncertain{lisse}',
       r'$\widehat M_{0,I}\longrightarrow$ un vrai schéma projectif et lisse',
       'A single shaft ends in a right-pointing angular arrowhead after the complete hatted M with 0,I. The following baselines read un vrai schéma / projectif et lisse; schéma has no separate comma after its final stroke.', 6,
       kind='misread symbol or index', sheet='symbols and indices')
change('Marginal NB, phrase after lisse (M1055)', r'\unsure{et tant}',
       r'\uncertain{sur} $\mathbb{Z}$', r'\unsure{et tout|et tant}',
       'The short word after et has two t-like ends and a low compressed middle. No closed a is evident, making tout the preferred candidate, but the internal letters are not secure enough to reject tant. No separate Z is written in this phrase.', 6,
       confidence='low', against_c=True)
change('Marginal NB, rigidity clause and ensuing words',
       r'--- le groupoïde qu\'il représente est en effet rigide. Il en \unsure{va} pour tous les',
       r'\ill{} \ill{} \uncertain{Deligne} \ill{} \ill{}',
       r'--- le groupoïde qu\'il représente est en effet rigide. Il en \unsure{va} pour tous les',
       'The rotated crop separates a descending g in groupoïde, the diaeresis group, qu\'il, représente with its long p, est en, and the two tall f strokes in effet, then rigide. The next words Il en and pour tous les are present. The intervening short va remains doubtful. There is no Deligne-shaped capital and sequence.', 6,
       confidence='medium', kind='readable ink left as \\ill{}',
       sheet='readable ink left as illegible')
change('Marginal NB, whole isomorphism formula',
       r'$M_{0,I}\simeq M^!_{0,\nu}$',
       r'$\widehat{M}_{0,I} \simeq \widehat{M}_{0,5}$',
       r'$M_{0,I}\simeq M^!_{0,\nu}$',
       'Both M bodies in this formula are unhatted. The first index ends in a serifed I. The second M has a raised upright and detached dot, an exclamation mark, and its second lower index is the broad descending nu shape. The relation consists of a wavy upper stroke over a straight lower stroke.', 6,
       kind='misread symbol or index', sheet='symbols and indices',
       marked=False, consequential=True)
change('Marginal NB, qualifier before last formula', 'quelque soit', r'\ill{}',
       'quelque soit',
       'The final marginal baseline begins with the descending q of quelque, then the short soit group with a tall final t. The source spelling quelque is retained without a final s.', 6,
       kind='readable ink left as \\ill{}', sheet='readable ink left as illegible')
change('Marginal NB, final variable and relation', r'\nu\in',
       r'V \times', r'\nu\in',
       'The variable is a descending check-like nu. It is followed by a curved membership sign with a middle bar, not two diagonal crossing strokes. The N and trailing three dots complete the formula. The separate C alphabet difference is recorded in the following row.', 6,
       kind='misread symbol or index', sheet='symbols and indices', marked=False,
       consequential=True)
change('Marginal NB, alphabet of N', r'\mathbf N', r'\mathbb{N}', r'\mathbb N',
       'The N has a separated doubled left/upward track rather than a single bold stroke, agreeing with the double-stroked Z above.', 6,
       against_c=True, against_h=False, kind='misread symbol or index',
       sheet='symbols and indices', marked=False)
change('Bien entendu paragraph, first noun', 'genres', r'\uncertain{groupes}',
       'genres',
       'After the initial g descender, the low e-n-r-e-s sequence has no p descender and no separate ou group.', 7)
change('Bien entendu paragraph, first component description',
       'des composantes irréductibles sont nuls',
       r'\add{des \ill{} \uncertain{liés aux} \uncertain{arêtes}} \uncertain{libres} \uncertain{aux} \uncertain{arêtes}',
       'des comp. irréductibles sont nuls',
       'The first component word stops after a descending p and a detached abbreviation dot. The following irreduc- continues as tibles on the next baseline, followed by sont nuls. These are ordinary baseline words, without the insertion asserted by H. The later composantes on the next line is written out in full.', 7,
       against_c=True, kind='abbreviation expanded or spelling modernised',
       sheet='abbreviations expanded spelling modernised')
change('Bien entendu paragraph, punctuation before capital Il', 'nuls. Il',
       r'\uncertain{arêtes}. Il', 'nuls, Il',
       'The mark after nuls has a curved downward tail, a comma rather than a dot. The following I is visibly capital; the comma plus capital Il is retained.', 7,
       against_c=True, kind='other', sheet='other')
change('Bien entendu paragraph, interlinear insertion',
       r"Il n'y a pas \inserted{lieu de mettre}",
       r"Il n'y a pas \add{(\uncertain{dans} \og pts marqués\fg{})}",
       r"Il n'y a pas \inserted{lieu de mettre}",
       'Above the line, lieu has its tall l and short i, de its looped d, and mettre its t strokes. The connector attaches after pas. The words pts marqués belong to the ordinary line below, not to this insertion.', 7,
       kind='insertion or placement', sheet='insertions put in wrong place')
change('Bien entendu paragraph, ordinary quoted noun phrase',
       "des ``pts marqués''", r'\uncertain{les}', "des ``pts marqués''",
       'The baseline has a looped d in des, then two small opening strokes, pts with a p descender, marqués with an acute mark, and two closing strokes. H moved this phrase into the insertion and substituted les at this position.', 7,
       kind='omission', sheet='omissions')
change('After sur, canceled whole formula and its placement',
       r'sur \deleted{\unsure{$M_{0,I}$}}', r'\struck{$M_{0,5}$}',
       r'sur \deleted{\unsure{$M_{0,I}$}}',
       'The canceled formula is immediately after sur and before les, not after de at the end of the component phrase. The final index has a central upright with short top and bottom bars like the live I forms. The strike covers part of the M and lower index, so the whole canceled formula retains its doubt.', 8,
       confidence='medium', kind='deletion state', sheet='struck text',
       marked=False)
change('After the canceled M, inserted 10 and component phrase',
       r'les \inserted{$10$} composantes irréductibles de',
       r'\uncertain{les} \add{\uncertain{10}} \uncertain{composantes} \ill{} \uncertain{de}',
       r'les \inserted{$10$} composantes irréductibles de',
       'The raised digits are a straight 1 and a closed 0, inserted after les. Here composantes is fully written; the next word has the complete irreductibles sequence and is followed by de. The missing H word is visible baseline ink.', 8,
       kind='readable ink left as \\ill{}', sheet='readable ink left as illegible')
change('Whole live divisor formula after composantes irréductibles de',
       r'$M^\infty_{0,5}$', r'$M^{\infty}_{0,5}$', r'$M^\infty_{0,I}$',
       'The complete formula has M, a raised two-loop infinity, and lower 0,I. The final index is a straight upright with two short cross strokes; it has no upper turn or rounded lower bowl of a 5. It matches the serifed I in the first insertion and the later live M formula.', 9,
       against_c=True, kind='misread symbol or index', sheet='symbols and indices',
       marked=False, consequential=True)
change('After the live divisor formula, through the MD- line end',
       'qui est de toutes façons une MD-',
       r'qui \uncertain{soit} \struck{\ill{}} \add{\ill{}} \uncertain{courbe} \uncertain{de toutes façons} une \uncertain{MD}-',
       'qui est de toutes façons une MD-',
       'The short est has its e-s-t group, followed directly by de toutes façons une MD-. There is no canceled or interlinear span in this line. The hyphen after the capitals joins courbe on the following baseline.', 9,
       kind='other', sheet='other')
change('Following baseline, courbe through maximal',
       r'courbe \deleted{stable} à MD-graphe maximal',
       r'\ill{} \uncertain{MD-graphe} \uncertain{maximal}',
       r'courbe \deleted{\unsure{stable}} à MD-graphe maximal',
       'The ordinary line begins courbe, then a heavily crossed word before the separate à and the capitals MD-graphe maximal. Stable is a plausible canceled reading from its exposed ends, but the middle and tail are covered. Adding its doubt alone is not counted against C; H lacks this canceled word and the adjacent courbe à sequence in their source positions.', 10,
       confidence='medium', kind='deletion state', sheet='struck text')
change('Maximal-graph parenthesis, first baseline',
       '(tous les genres nuls, tous les sommets',
       r', \uncertain{tels} \uncertain{toutes} les 2-\uncertain{sommets} \ill{} (\uncertain{dans} les gerbes \ill{}',
       '(tous les genres nuls, tous les sommets',
       'There is one opening parenthesis followed by tous with a tall initial t, les genres with a g descender, nuls and a comma, then tous les sommets. No preceding extra tels/toutes/2-sommets clause is written.', 11)
change('Maximal-graph parenthesis, last words (M1057)',
       r'pas de \unsure{poids|pieds} marqués',
       r'\uncertain{par} \uncertain{des} \uncertain{pointes} \uncertain{marquées}',
       'pas de pieds marqués',
       'The first word ends in a short s return, and de has no final s. In pieds, the p is followed by a short i with detached mark, a low e, and a looped d before s; no rounded o precedes the i. The ending of marqués has one accented e and s, with no additional feminine e.', 12,
       against_c=True, consequential=True)
change('Third paragraph, wording after précédente',
       'tient compte', r"\uncertain{n'est} \ill{} \uncertain{compatible} \uncertain{qu'avec}",
       'tient compte',
       'The first word begins with a tall crossed t and dotted i, ending in another t stroke. The next group begins co-, has the p/t stems, and ends in a short e: compte. There is no initial n-apostrophe or the longer compatible sequence.', 13)
change('Third paragraph, words immediately before the symmetric group',
       r'des opérations de $\mathfrak S_I^+$', r'$\mathfrak{S}^{+}_{I}$',
       r'des opérations de $\mathfrak S_I^+$',
       'The baseline begins des, followed by opérations with its p descender and accented group, then de before the large looped S. The lower I and raised crossing plus are both present. H omits these words here and repeats an altered phrase later.', 14,
       kind='omission', sheet='omissions', marked=False)
change('Third paragraph, automorphism insertion and following sur formula',
       r'\inserted{$\simeq\operatorname{Aut}\text{ du dodécaèdre gauche}$} sur $M^\infty_{0,I}$, mais',
       r'${\simeq}$ \uncertain{Aut du dodécaèdre grand}, (sur $M^{\infty}_{0,I}$), mais',
       r'\inserted{$\simeq\operatorname{Aut}\text{ du dodécaèdre gauche}$} sur $M^\infty_{0,I}$, mais',
       'Above the line are the wavy-plus-straight isomorphism sign, Aut du dodécaèdre, and gauche with a descending g and h shoulder. One long connector returns after the group S_I^+; it is not an opening parenthesis around sur. After the complete live M infinity 0,I formula is a comma, without a closing parenthesis.', 14,
       kind='insertion or placement', sheet='insertions put in wrong place',
       consequential=True)
change('Third paragraph, negative clause before the second symmetric group',
       r'pas de celles de $\mathfrak S_I$', r'$\mathfrak{S}_I$',
       r'pas de celles de $\mathfrak S_I$',
       'The next baseline has pas with a p descender, de, celles with two tall l strokes, and a second de, all before the large S with lower I. These words are absent from H.', 15,
       kind='omission', sheet='omissions', marked=False, consequential=True)
change('Third paragraph, transition from entier to il faudrait',
       'il faudrait le comprendre du pt de vue',
       r'\uncertain{des} \uncertain{opérations} de \ill{} par celles de \ill{} -- il faudrait le comprendre du pt de vue',
       'il faudrait le comprendre du pt de vue',
       'After the previous line ends entier and its dash, the next baseline begins il faudrait le comprendre du pt de vue. The i/l and long f strokes start that line; the extra H des opérations ... par celles ... passage has no corresponding ink.', 16,
       kind='text not on the page', sheet='text not on page')
change('Geometry phrase, first inserted gauche and opening parenthesis',
       r"l'icosaèdre \inserted{gauche} (ou du",
       r"l'icosaèdre (\add{grand}) \uncertain{ou} \ill{}",
       r"l'icosaèdre \inserted{gauche} (ou du",
       'The small inserted word has the looped descending g, low au, h shoulder and terminal e. It attaches after icosaèdre. The ordinary text continues (ou du; there is no closing parenthesis immediately after the inserted adjective, and du is readable.', 17,
       kind='insertion or placement', sheet='insertions put in wrong place')
change('Geometry phrase, second inserted gauche and ellipsis',
       r'dodécaèdre \inserted{gauche}\ldots) ---',
       r'dodécaèdre (\add{grand}) ou … --',
       r'dodécaèdre \inserted{gauche}\ldots) ---',
       'The second small inserted adjective again has a g descender and h shoulder. The baseline after dodécaèdre has three ellipsis marks and a closing curved parenthesis, then a dash. There is no separate ou after that parenthesis.', 18,
       kind='insertion or placement', sheet='insertions put in wrong place')
change('Third paragraph, final bi-icosaèdre phrase',
       r'\uline{bi-icosaèdre} gauche combinatoire)',
       r'\emph{bi-icosaèdre} grand (\uncertain{combinatoire}).',
       r'\uline{bi-icosaèdre} gauche combinatoire)',
       'The underline ends with bi-icosaèdre. The following adjective has the same g-au-ch-e form as the other four gauche occurrences. Combinatoire follows without an opening parenthesis; one curved closing parenthesis ends the line, without a separate period. That unmatched closing delimiter is retained.', 19)
change('Lower-left pencil foliation', r'\margin{67}', '', r'\margin{67}',
       'The pale lower-left number has a looped 6 followed by an angled 7 with a short crossing stroke. It is separate from the author\'s black-ink page 33 at the top.', 20,
       kind='omission', sheet='omissions', marked=False)

def decision(mid, choice, reading, ink, crop, confidence):
    key = f'{crop:02}'
    return dict(id=mid, cote=147, scan=68, decision=choice, reading=reading,
                ink=ink, crop=f'147_scan068_place{key}.png and ({", ".join(map(str, boxes[key]))})',
                confidence=confidence)

decisions = [
    decision('M1054', 'first', 'standart',
             'The initial st is followed by compressed an, a tall looped d, low ar, and final t with its crossing stroke. Stable lacks the required letter shapes; the author\'s terminal t is retained.', 3, 'high'),
    decision('M1055', 'undecided', r'\unsure{et tout|et tant}',
             'The word after et has two t-like ends. The middle has no independently closed a, so tout is preferred, but the compressed middle leaves tant possible. This is not a grammatical resolution.', 6, 'low'),
    decision('M1056', 'undecided', r'\unsure{va}',
             'The short strokes after Il en are crowded at the margin\'s edge. They do not securely separate into a v and a. Va remains a candidate, not a resolved reading.', 6, 'low'),
    decision('M1057', 'alternative', 'pieds',
             'After p are a short dotted i, low e and looped d before s. There is no o between p and i; this rules against poids and supports pieds.', 12, 'high'),
]

inventory = []
def item(kind, position, words, hand='his hand'):
    inventory.append(dict(scan=68, sheet_kind='text', hand=hand,
                          element=f'{len(inventory)+1:02}', kind=kind,
                          position=position, first_words_or_objects=words,
                          transcribed='yes'))

item('text', 'Top centre, black-ink foliation', '33')
item('text', 'Main baselines 1–5', 'Underlined Proposition; Le diviseur à l\'infini')
item('insertion', 'Above main baseline 1, right', r'$M^\infty_{0,I}$')
item('insertion', 'Above main baseline 2, after standart', r'\unsure{déployé|déployée}')
item('deletion', 'Main baseline 3, after au', 'celui du')
item('margin note', 'Slanted upper-left margin, nine baselines', r'Underlined NB; $\widehat M_{0,I}\longrightarrow$')
item('text', 'Main baselines 6–12', 'Bien entendu, les genres des comp. irréductibles')
item('insertion', 'Above main baseline 7, after pas', 'lieu de mettre')
item('deletion', 'Main baseline 8, after sur and before les', r'\unsure{$M_{0,I}$}')
item('insertion', 'Main baseline 8, above the gap after les', '$10$')
item('deletion', 'Main baseline 10, after courbe', r'\unsure{stable}')
item('text', 'Main baselines 13–19', 'L\'isom. de la prop. précédente tient compte')
item('insertion', 'Above main baseline 14, after the group notation', r'$\simeq\operatorname{Aut}\text{ du dodécaèdre gauche}$')
item('deletion', 'Main baseline 15, before entier', r'\unsure{tout}')
item('insertion', 'Above main baseline 17, after icosaèdre', 'gauche')
item('insertion', 'Above main baseline 18, after dodécaèdre', 'gauche')
item('text', 'Main baselines 20–21', 'Quand on passe à la multiplicité modulaire')
item('margin note', 'Extreme lower-left, pale pencil foliation', '67', 'hand not confidently attributed')

doubts = [
    dict(place='Inserted adjective after standart, crop03', reading=r'\inserted{\unsure{déployé|déployée}}', alternatives='déployé; déployée', confidence='medium', reason='Only one terminal e-shaped group is separately visible after y; compression does not rule out a second e. Feminine agreement is not used to supply one.'),
    dict(place='Marginal NB after lisse, M1055, crop06', reading=r'\unsure{et tout|et tant}', alternatives='et tout; et tant', confidence='low', reason='Two t-like ends are visible but the low middle is insufficiently separated. The absence of a clear closed a favors tout without deciding the word.'),
    dict(place='Marginal NB after Il en, M1056, crop06', reading=r'\unsure{va}', alternatives='va; unresolved short group', confidence='low', reason='The compressed short group at the margin\'s edge does not establish both letters independently.'),
    dict(place='Canceled whole formula after sur, unindexed C doubt, crop08', reading=r'\deleted{\unsure{$M_{0,I}$}}', alternatives=r'$M_{0,I}$; H $M_{0,5}$', confidence='medium', reason='The final index favors the page\'s serifed I, but the cancellation covers other parts of the formula. The original whole-formula doubt is retained rather than claiming every underlying stroke is plain.'),
    dict(place='Canceled word after courbe, crop10', reading=r'\deleted{\unsure{stable}}', alternatives='stable; unresolved canceled word', confidence='low', reason='A heavy strike covers the middle and tail. Stable remains plausible from exposed strokes but not every letter is plain. This is a certainty-only addition to C, not a preferred-reading change.'),
    dict(place='Canceled word before entier, crop15', reading=r'\deleted{\unsure{tout}}', alternatives='tout; unresolved canceled word', confidence='medium', reason='The first and last t stems remain visible, while the internal ou is traversed by the cancellation. This is a certainty-only addition to C, not a preferred-reading change.'),
]

notes = [
    'The manuscript states a proposition identifying the divisor at infinity M^infinity_{0,I} of the hatted M_{0,I} as a courbe standart with an inserted déployé/déployée adjective over Spec Z, and its graph with the 1-skeleton of the dodécaèdre gauche defined by I with a suitable orientation. This is recorded as a manuscript claim. No independent proof of the scheme or graph identification was performed, and the named graph was not replaced by a familiar regular polyhedron.',
    'The manuscript says that the irreducible components have genus zero, inserts their number 10, says no marked points need to be put on them, and describes a maximal MD graph with all genera zero, all vertices of order 3, and no marked pieds. These statements were carried as background; no geometric or enumerative check was made. The corrected live index I is determined by its bars and upright, not by this mathematics.',
    'The manuscript says the preceding isomorphism takes account of the S_I^+ actions, inserts an identification with Aut of the dodécaèdre gauche, and says it does not take account of all of S_I. It asks for an interpretation from the geometry of the icosaèdre gauche or dodécaèdre gauche, linked to the combinatorial bi-icosaèdre gauche. No equivariance proof or independent group-order calculation was performed.',
    'The marginal NB claims that the hatted M_{0,I} is an actual smooth projective scheme because the represented groupoid is rigid, then extends a statement to all M_{0,I} isomorphic to M^!_{0,nu}, for nu in N. The short phrases after lisse and Il en remain doubtful. The rigidity and scheme assertions were not independently proved; the arrow, lack of hats in the later formula, exclamation exponent, nu and membership sign were read from ink.',
    'Diplomatic features retained include the spelling standart, the abbreviation comp. at its first occurrence but full composantes at its second, quelque soit, the comma before capital Il, all seven insertions, four struck spans, and the unmatched final closing parenthesis after combinatoire. The inserted ending déployé/déployée is not supplied from French agreement. All five adjectives read gauche, not H\'s grand.',
    'Physical-line count: 39 writing units, comprising 21 main baselines, 7 separate interlinear insertions, 9 slanted marginal baselines (NB and its first formula share one), and the two isolated foliation numbers 33 and 67. Main physical line wraps, including irréduc-/tibles and MD-/courbe, are joined in the diplomatic text. The complete scan was viewed once for layout, each native half once for line-by-line comparison, and all 20 saved place crops were viewed. The margin crop was rotated clockwise 45 degrees; all recorded boxes use original coordinates. No OCR, web research, TeX compilation, or second reading was performed.',
    'The canceled formula after sur keeps C\'s unindexed whole-formula doubt. Stable and tout acquire certainty-only doubts because their strikes obscure letters; these additions are not counted as substantive changes against C. The page has text, formulas within prose, insertions and marginal writing, but no diagram or drawing. Pencil foliation 67 is kept separate from the author\'s ink page 33.',
]

check_events = [dict(statement_id=f'147-068-N{i}', date='2026-11-20 21:56:12 UTC',
                     who='reader_a; GPT-6 Astra Pro; inherited reasoning effort not separately exposed',
                     type='carried as background without fault found', outcome=outcome)
                for i, outcome in [
                    (1, 'The proposition was recorded as a source assertion. No proof of the divisor description, splitness, or graph identification was attempted; no mathematical conclusion was used to force the inserted adjective ending.'),
                    (2, 'The genus-zero, ten-component, order-three and unmarked-feet assertions were carried as source background. No graph enumeration, handshaking calculation or geometric verification was performed.'),
                    (3, 'The manuscript\'s equivariance and proposed geometric relationship were carried as background. No independent group or automorphism computation was made.'),
                    (4, 'The marginal rigidity and smooth projective scheme claims were carried as background. No proof was made, and the unresolved short phrases remain unresolved.')]]

notation = [
    dict(sign='I with short upper and lower bars', reading=r'I in $M_{0,I}$ and $\mathfrak S_I$', evidence='The inserted opening M, main live M infinity, lower live M and symmetric-group indices all use a straight upright with two short bars. The canceled M retains a compatible visible final index.', scope='Scan068; establishes I rather than the C/H 5 in the main live divisor formula.'),
    dict(sign='Double-stroked Z and N', reading=r'\mathbb Z; \mathbb N', evidence='Z has paired diagonal tracks; N has a separated doubled track. These are not merely heavy single strokes.', scope='Scan068, Spec base and final marginal formula.'),
    dict(sign='Raised upright plus dot on M', reading=r'M^!_{0,\nu}', evidence='The complete marginal formula has a detached dot below its raised upright; the M has no hat.', scope='Scan068 marginal NB.'),
    dict(sign='Large looped symmetric-group letter', reading=r'\mathfrak S_I^+; \mathfrak S_I', evidence='Both occurrences have the same large looped body with an interior return. Only the first has a raised crossing plus.', scope='Scan068 third paragraph; consistent with the supplied local notation convention.'),
]

hand_log = [
    dict(habit='The index I has short top and bottom bars even when very small; its middle remains an upright rather than a numeral bowl.', pages=[68], all_occurrences='Confirmed in the opening insertion, both live main-text M formulas, the marginal formulas, and the symmetric-group indices. The visible end under the strike is compatible, while the full canceled formula remains doubtful.', witness_misreadings='C and H both read the middle live M infinity index as 5; H also reads the canceled index as 5 and the last marginal index as 5.'),
    dict(habit='In gauche the low au is compressed while the g descender and ch/h rise remain diagnostic.', pages=[68], all_occurrences='All five occurrences: first proposition, Aut insertion, inserted adjective after icosaèdre, inserted adjective after dodécaèdre, and final bi-icosaèdre phrase.', witness_misreadings='H reads grand in each of these places; C retains gauche.'),
    dict(habit='Long curved insertion connectors can resemble parentheses, but their return leads to interlinear ink.', pages=[68], all_occurrences='Checked at the opening M infinity, inserted adjective, lieu de mettre, Aut phrase, and two lower gauche insertions; the real parenthesis after the lower ellipsis and the final unmatched closing parenthesis remain.', witness_misreadings='H encloses the opening inserted M and the sur M phrase in parentheses and misplaces parentheses around the lower inserted adjectives.'),
]

abbreviations = [
    dict(written='NB', expansion='nota bene'),
    dict(written='comp.', expansion='composantes'),
    dict(written='pts', expansion='points'),
    dict(written='isom.', expansion='isomorphisme'),
    dict(written='prop.', expansion='proposition'),
    dict(written='pt', expansion='point'),
]

second_boxes = []
def blind(kind, box, reading):
    x0, y0, x1, y1 = box
    second_boxes.append(dict(box=f'B{len(second_boxes)+1:02}', kind=kind,
                             x0=x0, y0=y0, x1=x1, y1=y1, reading=reading))

blind('handwritten number', [843, 30, 910, 82], r'\mspage{33}')
blind('word disagreement', boxes['01'], r'\uline{Proposition}')
blind('insertion', boxes['02'], r'\inserted{$M^\infty_{0,I}$}')
blind('handwritten number', [255, 170, 465, 335], r'$\widehat M_{0,I}$')
blind('insertion', boxes['03'], r'courbe standart \inserted{\unsure{déployé|déployée}} sur $\operatorname{Spec}\mathbb Z$,')
blind('struck passage', boxes['04'], r'au \deleted{celui du}')
blind('word disagreement', boxes['05'], r'$1$-squelette du dodécaèdre gauche')
blind('margin note', boxes['06'], r"\margin{\uline{NB} $\widehat M_{0,I}\longrightarrow$ un vrai schéma projectif et lisse \unsure{et tout|et tant} --- le groupoïde qu'il représente est en effet rigide. Il en \unsure{va} pour tous les $M_{0,I}\simeq M^!_{0,\nu}$ quelque soit $\nu\in\mathbb N\ldots$}")
blind('insertion', boxes['07'], r"Bien entendu, les genres des comp. irréductibles sont nuls, Il n'y a pas \inserted{lieu de mettre} des ``pts marqués''")
blind('doubtful formula', boxes['08'], r'sur \deleted{\unsure{$M_{0,I}$}} les \inserted{$10$} composantes irréductibles de')
blind('handwritten number', boxes['09'], r'$M^\infty_{0,I}$, qui est de toutes façons une MD-')
blind('struck passage', boxes['10'], r'courbe \deleted{\unsure{stable}} à MD-graphe maximal')
blind('word disagreement', boxes['11'], '(tous les genres nuls, tous les sommets')
blind('handwritten number', boxes['12'], r"d'ordre $3$, pas de pieds marqués).")
blind('insertion', [268, 1368, 1615, 1630], r"L'isom. de la prop. précédente tient compte des opérations de $\mathfrak S_I^+$ \inserted{$\simeq\operatorname{Aut}\text{ du dodécaèdre gauche}$} sur $M^\infty_{0,I}$, mais")
blind('struck passage', boxes['15'], r'pas de celles de $\mathfrak S_I$ \deleted{\unsure{tout}} entier ---')
blind('word disagreement', boxes['16'], 'il faudrait le comprendre du pt de vue')
blind('insertion', [270, 1790, 1585, 2088], r"de la géométrie de l'icosaèdre \inserted{gauche} (ou du dodécaèdre \inserted{gauche}\ldots) --- ça doit être lié bien sûr")
blind('word disagreement', boxes['19'], r'au \uline{bi-icosaèdre} gauche combinatoire)')
blind('handwritten number', boxes['20'], r'\margin{67}')

report = dict(
    scan=68, reader='reader_a', physical_lines_read=39, changes=changes,
    decisions=decisions, inventory=inventory, doubts=doubts, notes=notes,
    check_events=check_events, notation=notation, hand_log=hand_log,
    abbreviations=abbreviations, second_boxes=second_boxes,
    unresolved=[
        'Inserted ending déployé versus déployée; déployé preferred without excluding the second e.',
        'M1055 et tout versus et tant; neither reading is ruled out.',
        'M1056 va remains unresolved.',
        'The entire canceled M_{0,I} remains doubtful despite the I-shaped final index.',
        'Canceled stable and tout retain uncertainty because strokes cover their letters.'
    ],
    witness_comparison='C is substantially closer to the continuous prose, the margin, the negative equivariance clause, the five gauche readings, and the placement of canceled and inserted spans. C expands comp., changes the comma before Il to a period, and shares H\'s erroneous live 5 index. It also renders the double-stroked Z and N as bold and supplies a terminal e in the inserted adjective that is not separately secure. H correctly uses the double-struck alphabets, but seriously fragments the middle paragraph and margin, introduces unsupported phrases and parentheses, reads grand five times, and omits pencil foliation 67. Uncertainty-only wrapper differences and macro-only differences are excluded from the change count.'
)

# Reading strings use ordinary apostrophes, not a TeX accent command.
for row in changes:
    for k in ('C', 'H', 'final'):
        row[k] = row[k].replace("\\'", "'")

assert len(changes) == 34
assert [d['id'] for d in decisions] == [r['id'] for r in csv.DictReader((packet/'marks.tsv').open(), delimiter='\t')]
assert all(c['against_C'] or c['against_H'] for c in changes)
assert all((work/'crops'/c['crop']).is_file() for c in changes)
assert all(len(c['box']) == 4 and 0 <= c['box'][0] < c['box'][2] <= 1696 and 0 <= c['box'][1] < c['box'][3] <= 2367 for c in changes)
assert all(0 <= b['x0'] < b['x1'] <= 1696 and 0 <= b['y0'] < b['y1'] <= 2367 for b in second_boxes)
assert all(b['reading'] in proposed for b in second_boxes)
assert all(c['final'] in proposed for c in changes)
assert proposed.count('{') == proposed.count('}')
assert proposed.count('$') % 2 == 0
assert proposed.count('\\inserted{') == 7
assert proposed.count('\\deleted{') == 4
assert set(re.findall(r'\\([A-Za-z]+)', proposed)) <= {
    'scanpage','mspage','uline','inserted','infty','widehat','unsure','operatorname',
    'mathbb','deleted','margin','longrightarrow','simeq','nu','in','ldots','mathfrak','text'
}

(out/'report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
print(json.dumps(dict(changes=len(changes), against_C=sum(c['against_C'] for c in changes),
                      against_H=sum(c['against_H'] for c in changes), decisions=len(decisions),
                      crops=len(boxes), inventory=len(inventory), second_boxes=len(second_boxes),
                      physical_lines=39, doubts=len(doubts)), ensure_ascii=False))
