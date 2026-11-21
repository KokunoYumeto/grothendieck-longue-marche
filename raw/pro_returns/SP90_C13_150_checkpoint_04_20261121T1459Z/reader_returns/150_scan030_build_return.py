from pathlib import Path
import json
import re
from collections import Counter

BASE = Path('/workspace/scratch/481648fc487b/SP90_C13_150_work')
PACKET = Path('/workspace/scratch/481648fc487b/reader_packets/150_scan030')
OUT = BASE / 'reader_returns'
TEX = (OUT / '150_scan030.tex').read_text()
C = (PACKET / 'C.tex').read_text()
H = (PACKET / 'H.tex').read_text()

names = [
    'heading_voisinages', 'heading_pas', 'heading_recurrence', 'condition14',
    'condition_b', 'margin_generalization', 'parties_bord_Balpha', 'muni',
    'represente_les_germes', 'cylindres_convenables', 'imposant_exprimant',
    'aux_E', 'lon_a', 'product_relation', 'avec_definition', 'bien_sur_les',
    'margin_J', 'struck_soit', 'I0_part', 'struck_et_soit', 'coproduct',
    'struck_alors', 'germe_structure', 'strict_attachment', 'dun_voisinage',
    'equivaut_a', 'syst_de', 'des_Xi', 'final_Xi', 'margin29', 'transversalite',
    'first_E_Balpha', 'first_E_Balpha_complete',
]
crops = {}
for name in names:
    meta = json.loads((BASE / 'crops' / f'150_scan030_{name}.json').read_text())
    assert (BASE / 'crops' / meta['file']).is_file()
    crops[name] = meta

data = {
    'scan': 30, 'reader': 'reader_a', 'line_count': 24,
    'changes': [], 'marks': [], 'inventory': [], 'doubts': [], 'notes': [],
    'check_events': [], 'notation': [], 'abbreviations': [], 'hand_log': [],
    'second_boxes': [],
}

def change(place, c, h, final, evidence, crop, confidence='high',
           kind='misread word', error_kind='words', marked_in_H=False,
           change_C=False, change_H=True, consequential=''):
    data['changes'].append({
        'place': place, 'C': c, 'H': h, 'final': final, 'evidence': evidence,
        'crop': crops[crop]['file'], 'box': crops[crop]['box'],
        'confidence': confidence, 'kind': kind, 'error_kind': error_kind,
        'marked_in_H': marked_in_H, 'change_C': change_C,
        'change_H': change_H, 'consequential': consequential,
    })

change('line 1 / initial ink of voisinages',
       r'\uline{voisinages côniques}',
       r'\emph{\struck{\ill{}} voisinages côniques}',
       r'\uline{voisinages côniques}',
       'The beginning of voisinages is retraced and crowded. I cannot isolate a separate spaced-out cancelled word before the live word, as H does. The visible live word and its underline are retained; the underlying strokes are not reconstructed.',
       'heading_voisinages', 'medium',
       'deletion state (struck given live or live given struck)', 'struck text', True)
change('line 1 / le pas', 'le pas', r'le \uncertain{jeu}', 'le pas',
       'The first letter has a descending p-stroke; a small closed a and final flat s follow. These support pas rather than jeu.',
       'heading_pas', marked_in_H=True)
change('line 2 / de récurrence', 'de récurrence.',
       r'\add{des \uncertain{récurrences}}\ldots', 'de récurrence.',
       'The continuation reads de, with no following s, and récurrence in the singular. The end is a short terminal stop, not a row of ellipsis dots. No insertion caret is visible at this continuation; the spatial continuation is recorded without H’s added-text wrapper.',
       'heading_recurrence', marked_in_H=True)
change('line 6 / condition b and its placement',
       r'\inserted{b) $X=\bigcup_{i\in I}X_i$}',
       r'b) & X=\bigcup_{i\in I}X_i',
       r'\inserted{b) $X=\bigcup_{i\in I}X_i$}',
       'The second condition occupies a smaller separate line below the first displayed condition. I retain C’s added-line encoding provisionally; no caret proves its chronology, and H presents it as a regular array row. The formula itself is agreed and readable.',
       'condition_b', 'medium', 'insertion or placement', 'insertion placement')
change('left margin beside (14) / words',
       'Cette condition se généralise : aux intersections quelconques',
       r'Cette condition \uncertain{généralise} \ldots',
       'Cette condition se généralise : aux intersections quelconques',
       'After rotation, se is a short separate word before généralise; the colon is visible. The next two lines read aux intersections and quelconques. Their ascenders, the q-descender, and the final plural s support C’s words rather than H’s ellipses and illegibility placeholders.',
       'margin_generalization', marked_in_H=True, kind=r'readable ink left as \ill{}',
       error_kind='readable ink left as illegible')
change('left margin beside (14) / full intersection-union formula',
       r'\bigcap_{i\in J}X_i=\bigcup_{\substack{k\in I\\k\text{ minorant }J}}X_k',
       r'\bigcap X_i=\bigcup_{k\in I,\ k\le\ldots}X_k',
       r'\bigcap_{i\in J}X_i=\bigcup_{\unsure{\{}\,\substack{k\in I\\k\text{ minorant }J}}X_k',
       'The intersection has i∈J below it. Under the union are two lines, k∈I and k minorant J; the word minorant is written out, not a ≤ sign followed by an ellipsis. A crowded curved stroke stands to the left of these two conditions. It may be a grouping left brace, but its overlap with the lower line prevents a secure identification or deletion-state assignment; only that stroke is marked doubtful.',
       'margin_generalization', 'medium', 'misread symbol or index', 'symbols and indices',
       True, True, True,
       'Preserves the written lower-bound condition and records a possible grouping sign without normalizing it.')
change('left margin beside (14) / terminal punctuation',
       r'X_k$.', '[absent]', r'X_k$',
       'No separate stop is visible after the terminal X_k in the margin formula. The full-stop supplied by C is omitted.',
       'margin_generalization', 'high', 'text not on the page', 'text not on page',
       False, True, False)
change('line 7 / Transversalité underline state',
       'Transversalité', r'\emph{Transversalité}', 'Transversalité',
       'There is no independent underline below Transversalité. The strokes below belong to descending letters and adjacent writing; C’s plain heading state is retained.',
       'transversalite', kind='other', error_kind='other')
change('line 7 / parties-bord', 'parties-bord', 'parties bordantes', 'parties-bord',
       'A short hyphen separates parties and bord. The latter word ends after d; there are no inked -antes letters.',
       'parties_bord_Balpha')
change('line 7 / inserted B alpha, only occurrence at this place',
       r'\inserted{$B_\alpha$}', r'$B_\alpha$ \add{$B_\alpha$}',
       r'\inserted{$B_\alpha$}',
       'One B with lower alpha is written above the line with a curved attachment to the gap after parties-bord. H duplicates it as both ordinary and added text. Only one symbol is present.',
       'parties_bord_Balpha', kind='text not on the page', error_kind='text not on page')
change('line 8 / muni', 'munies', 'muni', 'muni',
       'The word ends at a dotted i. No e or s follows before the separated de. This is a literal reading of the ending, independent of grammatical agreement with an antecedent.',
       'muni', change_C=True, change_H=False)
change('line 10 / représente les germes', 'représente les germes',
       r'\uncertain{représentant} les germes', 'représente les germes',
       'The word before les germes has the final -te form, not -tant. The phrase is on the line before par des cylindres, not after that phrase as H places it. The r/p/s/t structure and the separate les and germes are recoverable.',
       'represente_les_germes', marked_in_H=True)
change('line 10 / cylindres convenables at right edge',
       'par des cylindres convenables', r'par des cylindres \ill{}',
       r'par des cylindres convenable\unsure{s}',
       'Par des cylindres and the beginning and body of convenable- are readable. The b/l ascenders and following small e reach the dark physical right edge; the final s is not independently bounded there. The supported word is retained with uncertainty confined to that ending.',
       'cylindres_convenables', 'medium', r'readable ink left as \ill{}',
       'readable ink left as illegible', True)
change('line 11 / initial cylinder label before imposant',
       r'$E_{B_\alpha}$,', '[absent]', r'$E_{B_\alpha}$,',
       'At the beginning of this line, E has a lower B and a still lower small looped alpha, followed by a comma. This first occurrence precedes imposant; it is distinct from the later occurrence after aux and is lost in H’s displaced wording.',
       'first_E_Balpha_complete', kind='omission', error_kind='omissions')
change('line 11 / imposant', r'\unsure{imposant}', r'\ill{} \ill{}', 'imposant',
       'The dotted opening i, compressed m, descending p, and the ending -sant can be followed in the main-line word. No cancellation stroke through the word is visible. The lower added word is recorded separately.',
       'imposant_exprimant', 'medium', r'readable ink left as \ill{}',
       'readable ink left as illegible', True, True)
change('line 11 / interlinear exprimant',
       r'\inserted{\unsure{exprimant}}', r'\uncertain{représentant}',
       r'\inserted{exprimant}',
       'The smaller interlinear word begins ex- with a crossing stroke, then has the long p-descender and the compressed -rimant ending. Its curved leader reaches the vicinity before que. It is not a second occurrence of représente, and it is not written over a struck imposant.',
       'imposant_exprimant', 'medium', 'misread word', 'words', True, True)
change('line 12 / aux and extra loop before cylinder label',
       r'aux $E_{B_\alpha}$',
       r"\ill{} \ill{} \uncertain{supposons} de l'$E_{B_\alpha}$",
       r"aux \unsure{l'}$E_{B_\alpha}$",
       'The left word looks aux. Between it and E is a separate tall loop with an exit stroke and an upper apostrophe-like upright; neither is part of E’s three-bar form. I retain a doubtful l\' reading rather than suppress the ink. No clear strike cancels it, but a corrective origin remains possible. The supposons de sequence in H is not supported by this line.',
       'aux_E', 'medium', 'misread word', 'words', True, True)
change('line 12 / l’on a', "l'on a", "l'isom.", "l'on a",
       'After the tall l and its apostrophe, there is a compressed on followed by a separate small a. No isom abbreviation or terminal abbreviation stop is present.',
       'lon_a')
change('line 13 / unmatched opening parenthesis',
       r'E_J\cap X_i\simeq (X_{iJ}\times I^J',
       r'E_J\cap X_i\simeq(X_{iJ}\times\mathbf{I}^J)',
       r'E_J\cap X_i\simeq (X_{iJ}\times I^J',
       'A thin opening parenthesis precedes X_iJ. There is no matching closing curve after the first I^J; farther right a new opening begins (induit par. H supplies a closing parenthesis absent from the ink.',
       'product_relation', kind='text not on the page', error_kind='text not on page')
change('line 14 / avec, following the product relation',
       r'avec $X_{iJ}=X_i\cap B_J$).',
       r'\text{, où } X_{iJ}=X_i\cap B_J\text{)}.',
       r'avec $X_{iJ}=X_i\cap B_J$).',
       'The next line begins with the short separate strokes of avec, not où. The equality, the indices iJ and J, the closing parenthesis, and the final dot are visible.',
       'avec_definition')
change('line 14 / struck Bien sûr les',
       r'\deleted{\unsure{Bien sûr les}}', r'\struck{\ill{}}',
       r'\deleted{Bien sûr les}',
       'The cancellation runs along the baseline, but B and the dotted i remain visible, followed by compressed en. The middle word retains a distinct circumflex over u; a tall l and flattened es end the phrase. These surviving strokes support Bien sûr les under the cancellation.',
       'bien_sur_les', 'medium', r'readable ink left as \ill{}',
       'readable ink left as illegible', True, True)
change('left margin beside product / pour J ... ensemble d’indices alpha',
       r"\margin{pour $J$ \deleted{\unsure{ensemble}} \unsure{ensemble} d'indices $\alpha$}",
       r"\marginal{$J$ \ill{} \ill{} pour \ill{} d'indices}",
       r"\margin{pour $J$ \deleted{\unsure{ensemble}} ensemble d'indices $\alpha$}",
       'The rotated margin begins pour J, followed by one crossed word and a separate live ensemble. The latter has a compressed first half and the taller b/l portion near its end. The next line reads d’indices with a separate alpha. The first crossed word remains too crowded to identify securely; C’s candidate is retained as a doubt, not confirmed by repetition.',
       'margin_J', 'medium', r'readable ink left as \ill{}',
       'readable ink left as illegible', True, True)
change('line 15 / struck opening candidate',
       r'\deleted{\unsure{Soit}}', r'\struck{\ill{}}',
       r'\deleted{\unsure{Soit}}',
       'The cancellation is dense and oblique. The surviving loops permit C’s Soit candidate but do not establish all its letters. I preserve that candidate with its doubt rather than claim a resolved reading of H’s illegible span.',
       'struck_soit', 'low', 'other', 'struck text', True)
change('line 15 / une partie de I zero',
       r'une partie de $\unsure{I_0|I}$ formée',
       r'une partie de $I$ formée', r'une partie de $I_0$ formée',
       'The capital I has a small closed loop attached to the lower-right end of its foot. It is a written subscript zero, not merely a flourish. The apparent redundancy of I_0 within I_0 is not corrected.',
       'I0_part', 'high', 'misread symbol or index', 'symbols and indices',
       False, True, True,
       'The page literally names I_0 a second time; a probable authorial slip is retained.')
change('line 16 / struck et and doubtful soit',
       r'\deleted{et \unsure{soit}}', r'\struck{\ill{}}',
       r'\deleted{et \unsure{soit}}',
       'The left et is recoverable under two horizontal strokes. The following crossed letters are compatible with soit but too overlaid to resolve it; the clear live et soit to the right is a comparison, not a substitute for the obscured ink.',
       'struck_et_soit', 'medium', r'readable ink left as \ill{}',
       'readable ink left as illegible', True)
change('line 17 / coproduct formula terminal stop',
       r'\coprod_{i\in I_0}X_i.', r'\coprod_{i\in I_0}X_i .',
       r'\coprod_{i\in I_0}X_i',
       'The final X has its attached i foot and one i-dot; there is no additional dot farther right. Both witnesses supply a sentence stop not visible in the displayed formula.',
       'coproduct', 'high', 'text not on the page', 'text not on page', False, True)
change('line 18 / struck opening candidate Alors',
       r'\deleted{\unsure{Alors}}', r'\struck{\ill{}}',
       r'\deleted{\unsure{Alors}}',
       'The initial cluster is blackened and the later loops are partly incorporated into the cancellation. Alors remains only a candidate; I do not resolve C’s doubt or claim the cancelled word fully legible.',
       'struck_alors', 'low', 'other', 'struck text', True)
change('line 19 / attachment of strict',
       r'cônique \inserted{strict} de $X_{I_0}$',
       r"d'un germe \add{strict}",
       r'cônique \inserted{strict} de $X_{I_0}$',
       'Strict lies below germe, with a long curved leader descending to the gap after cônique and before de X_I0. Its location on the sheet is not its reading-order attachment. H attaches it to germe instead.',
       'strict_attachment', kind='insertion or placement', error_kind='insertion placement')
change('line 19 / de before X_I0 is on the ordinary baseline',
       r'de $X_{I_0}$', r'\add{de} $X_{I_0}$', r'de $X_{I_0}$',
       'The de below the leader is written on the baseline of d’un voisinage cônique ... X_I0. The leader belongs to strict; there is no separate addition sign assigning de an inserted status.',
       'strict_attachment', kind='insertion or placement', error_kind='insertion placement')
change('line 19 / d’un voisinage cônique in reading order',
       r"d'un voisinage cônique \inserted{strict} de $X_{I_0}$",
       r"$X_{I_0}$ équivaut : d'un voisinage cônique",
       r"d'un voisinage cônique \inserted{strict} de $X_{I_0}$",
       'The line begins at the left with d’un voisinage cônique and proceeds rightward to de X_I0. These words do not follow the first équivaut as H’s reordered sentence would require. The ordinary left-to-right line and strict’s leader support C’s sequence.',
       'dun_voisinage', kind='insertion or placement', error_kind='insertion placement')
change('line 19 / single équivaut and ambiguous final cluster',
       r'équivaut à', r"équivaut : d'un voisinage cônique équivaut à",
       r'équivaut \unsure{à|:}',
       'Only one équivaut is present at the right of this line. After it are two separated blobs: the upper is accent-like and the lower could be an extremely compressed a, but a colon cannot be excluded from shape alone. H’s duplicated équivaut is not present; the surviving final cluster is left ambiguous.',
       'equivaut_a', 'medium', 'text not on the page', 'text not on page')
change('line 20 / syst without stop', 'syst de', 'syst. de', 'syst de',
       'The word syst is followed by a gap and de. There is no stop in that gap; the two small marks farther right belong to adjacent writing. The undotted abbreviation is retained.',
       'syst_de', kind='abbreviation expanded or spelling modernised', error_kind='abbreviation/spelling')
change('line 21 / des X_i', r'\unsure{dans $X$|des $X_i$}',
       r'des $X_i$', r'des $X_i$',
       'The short word after disjoints has the looped d and compressed es; I do not see the extra n required for dans. The X has an attached small i-foot and a separate dot. The alternative des X_i is favored from these strokes, with moderate confidence.',
       'des_Xi', 'medium', 'misread word', 'words', False, True, False)
change('line 21 / no independent stop before dash',
       r'\unsure{dans $X$|des $X_i$}. ---', r'des $X_i$. --',
       r'des $X_i$ ---',
       'The sole dot to the right of the X-foot occupies the i-dot position, matching dotted X_i elsewhere on this sheet. There is no second dot before the horizontal dash. Both witnesses supply an independent full stop.',
       'des_Xi', 'high', 'text not on the page', 'text not on page', False, True)
change('bottom left margin / number 29', r'\margin{29}', '[absent]', r'\margin{29}',
       'The bottom-left thin-ink number consists of 2 followed by a looped 9. It is transcribed as a margin number without assigning it to the main manuscript hand. H’s note about no number in his hand does not transcribe this visible foliation.',
       'margin29', kind='omission', error_kind='omissions')

def mark(literal, context, decision, reading, evidence, crop, confidence):
    data['marks'].append({
        'mark': literal, 'context': context, 'decision': decision, 'reading': reading,
        'evidence': evidence, 'crop': crops[crop]['file'],
        'box': crops[crop]['box'], 'confidence': confidence,
    })

mark(r'\unsure{imposant}', r'\unsure{imposant}\inserted', 'first', 'imposant',
     'Dotted i, compressed m, a descending p, and -sant are recoverable; no cancellation crosses the main-line word.',
     'imposant_exprimant', 'medium')
mark(r'\unsure{exprimant}', r'\inserted{\unsure{exprimant}}', 'first', 'exprimant',
     'The lower interlinear ex- crossing, p-descender, and -rimant ending support the candidate; a curved leader attaches it near que.',
     'imposant_exprimant', 'medium')
mark(r'\unsure{Bien sûr les}', r'\deleted{\unsure{Bien sûr les}}', 'first', 'Bien sûr les',
     'The B/i strokes, middle circumflex, and final tall l with compressed es survive the baseline cancellation.',
     'bien_sur_les', 'medium')
mark(r'\unsure{ensemble}', r'\deleted{\unsure{ensemble}}', 'undecided', r'\unsure{ensemble}',
     'The first word after J is crossed and heavily overlaid. Its initial looping stroke and internal letter divisions cannot be securely separated; the repeated live word is not sufficient evidence to resolve it.',
     'margin_J', 'low')
mark(r'\unsure{ensemble}', r"\unsure{ensemble} d'indices", 'first', 'ensemble',
     'The separate live word after the cancelled cluster has compressed ensem- and taller b/l strokes before its final e; the next line d’indices confirms its boundary, not its letters.',
     'margin_J', 'medium')
mark(r'\unsure{Soit}', r'\deleted{\unsure{Soit}}', 'undecided', r'\unsure{Soit}',
     'The oblique blackened cancellation prevents a secure letter-by-letter reading; Soit remains a candidate only.',
     'struck_soit', 'low')
mark(r'\unsure{I_0|I}', r'une partie de $\unsure{I_0|I}$', 'first', r'I_0',
     'A small closed loop is explicitly attached below and to the right of the capital I’s foot. It supports subscript zero despite the redundant resulting phrase.',
     'I0_part', 'high')
mark(r'\unsure{soit}', r'\deleted{et \unsure{soit}}', 'undecided', r'\unsure{soit}',
     'Et is recoverable, but the following short word is crossed by horizontal and oblique strokes. Live et soit at the right is not used to invent the obscured letters.',
     'struck_et_soit', 'low')
mark(r'\unsure{Alors}', r'\deleted{\unsure{Alors}}', 'undecided', r'\unsure{Alors}',
     'The initial blackened cluster and later intertwined loops do not securely establish Alors; the original candidate is retained with doubt.',
     'struck_alors', 'low')
mark(r'\unsure{dans $X$|des $X_i$}', r'disjoints \unsure{dans $X$|des $X_i$}',
     'alternative', r'des $X_i$',
     'The short d-es sequence lacks an independently visible n; the X has a small attached i-foot and a separate dot. The second reading is favored with moderate confidence.',
     'des_Xi', 'medium')

def inv(element, kind, position, reading, hand='his hand'):
    data['inventory'].append({
        'element': element, 'kind': kind, 'position': position,
        'first_words_or_objects': reading, 'sheet_kind': 'text',
        'hand': hand, 'transcribed': 'yes',
    })

inv('L01', 'text', 'top / main line 1',
    r'7. \uline{Stratifications} et \uline{voisinages côniques} : le pas')
inv('L02', 'text', 'top right / main line 2', 'de récurrence.')
inv('L03', 'text', 'main line 3', r'$(X_i)_{i\in I}$, famille croissante de parties de $X$,')
inv('L04', 'text', 'main line 4', 'satisfaisant')
inv('L05', 'display', 'main line 5',
    r'(14) a) \forall i,j\in I, on a X_i\cap X_j=\bigcup_{\alpha\le i,j}X_\alpha.')
inv('L06', 'insertion', 'smaller line 6 below (14a)', r'b) $X=\bigcup_{i\in I}X_i$')
inv('M01', 'margin note', 'left diagonal margin beside lines 4–8',
    r'Cette condition se généralise : aux intersections quelconques; \bigcap_{i\in J}X_i=\bigcup_{\unsure{\{}\,\substack{k\in I\\k\text{ minorant }J}}X_k')
inv('L07', 'text', 'main line 7', 'Transversalité : un syst. de parties-bord ... de')
inv('I01', 'insertion', 'above parties-bord in line 7, curved leader', r'$B_\alpha$')
inv('L08', 'text', 'main line 8', r'$X$, muni de germes de cylindres associés')
inv('L09', 'text', 'main line 9', '(mutuellement transversaux entre eux) : si on')
inv('L10', 'text', 'main line 10, extending to right physical edge',
    r'représente les germes par des cylindres convenable\unsure{s}')
inv('L11', 'text', 'main line 11', r'$E_{B_\alpha}$, imposant ... que les $X_i$ soient transversaux')
inv('I02', 'insertion', 'below imposant in line 11, curved leader to before que', 'exprimant')
inv('L12', 'text', 'main line 12', r"aux \unsure{l'}$E_{B_\alpha}$ --- cela implique que l'on a")
inv('L13', 'display', 'main line 13',
    r'E_J\cap X_i\simeq (X_{iJ}\times I^J (induit par E_J\simeq B_J\times I^J,')
inv('L14', 'text', 'main line 14 left', r'avec $X_{iJ}=X_i\cap B_J$).')
inv('D01', 'deletion', 'main line 14 right, after the definition', 'Bien sûr les')
inv('M02', 'margin note', 'left diagonal margin beside lines 13–15',
    r"pour $J$ \deleted{\unsure{ensemble}} ensemble d'indices $\alpha$")
inv('D02', 'deletion', 'within M02 after J', r'\unsure{ensemble}')
inv('D03', 'deletion', 'before live Soit in main line 15', r'\unsure{Soit}')
inv('L15', 'text', 'main line 15', r'Soit $I_0\subset I$ une partie de $I_0$ formée')
inv('L16', 'text', 'main line 16', r"d'éléments minimaux, ... et soit")
inv('D04', 'deletion', 'main line 16, before the live et soit', r'et \unsure{soit}')
inv('L17', 'display', 'main line 17',
    r'X_{I_0}=\bigcup_{i\in I_0}X_i=\coprod_{i\in I_0}X_i')
inv('D05', 'deletion', 'before La in main line 18', r'\unsure{Alors}')
inv('L18', 'text', 'main line 18', r"La donnée d'un germe ...")
inv('D06', 'deletion', 'right end of main line 18 after germe', 'de structure')
inv('L19', 'text', 'main line 19',
    r"d'un voisinage cônique ... de $X_{I_0}$ équivaut \unsure{à|:}")
inv('I03', 'insertion', 'between lines 18–19 below germe; leader to after cônique', 'strict')
inv('L20', 'text', 'main line 20', r"celle d'un syst de voisinages côniques")
inv('L21', 'text', 'main line 21', r'$T_i$ ($i\in I_0$) mutuellement disjoints des $X_i$ ---')
inv('L22', 'text', 'main line 22', r"celle d'un germe de voisinage cônique de $X$,")
inv('L23', 'text', 'main line 23', r"à celle d'une famille de germes de vois.")
inv('L24', 'text', 'bottom / main line 24', r'côniques des $\unsure{X_i|X}$ dans $X$.')
inv('M03', 'margin note', 'bottom-left corner, near lower paper edge', '29',
    'attribution uncertain; much thinner ink than the main writing')

data['doubts'] = [
    {'place': 'line 1 / overwritten initial strokes of voisinages',
     'reading': 'voisinages', 'alternatives': 'Underlying overwritten letters cannot be separated; H’s separate preceding struck word is not established.',
     'confidence': 'medium'},
    {'place': 'line 6 / status of b)',
     'reading': r'\inserted{b) $X=\bigcup_{i\in I}X_i$}',
     'alternatives': 'Smaller added line versus ordinary second row; no caret establishes chronology.',
     'confidence': 'medium'},
    {'place': 'left margin beside (14) / stroke before union conditions',
     'reading': r'\unsure{\{}',
     'alternatives': 'Grouping left brace versus overlapping correction/index stroke; no secure cancellation state.',
     'confidence': 'low'},
    {'place': 'line 10 / terminal letter at right paper edge',
     'reading': r'convenable\unsure{s}',
     'alternatives': 'The final s is expected from the visible word but is not independently bounded against the dark physical edge.',
     'confidence': 'medium'},
    {'place': 'line 12 / extra ink before E_Balpha',
     'reading': r"aux \unsure{l'}$E_{B_\alpha}$",
     'alternatives': 'A separate l and apostrophe, or a corrective loop/stroke whose textual role is unresolved; no deletion is evident.',
     'confidence': 'medium'},
    {'place': 'M02 / cancelled word after J',
     'reading': r'\deleted{\unsure{ensemble}}',
     'alternatives': 'The underlying cancelled word remains unidentified; the live ensemble is not used to fill it in.',
     'confidence': 'low'},
    {'place': 'line 15 / initial cancellation', 'reading': r'\deleted{\unsure{Soit}}',
     'alternatives': 'Soit is retained only as C’s candidate; individual letters remain obscured.',
     'confidence': 'low'},
    {'place': 'line 16 / cancellation after et', 'reading': r'\deleted{et \unsure{soit}}',
     'alternatives': 'The second word is not securely legible; nearby live soit supplies comparison only.',
     'confidence': 'low'},
    {'place': 'line 18 / initial cancellation', 'reading': r'\deleted{\unsure{Alors}}',
     'alternatives': 'Alors is retained only as a candidate under dense cancellation.',
     'confidence': 'low'},
    {'place': 'line 19 / cluster after équivaut', 'reading': r'\unsure{à|:}',
     'alternatives': 'An accented compressed a versus colon; both fit the two remaining blobs.',
     'confidence': 'medium'},
    {'place': 'line 21 / des X_i', 'reading': r'des $X_i$',
     'alternatives': 'The second C option is favored; the flattened short word remains less distinct than surrounding writing.',
     'confidence': 'medium'},
    {'place': 'line 24 / first X and attached foot', 'reading': r'$\unsure{X_i|X}$',
     'alternatives': 'Undotted attached i versus a long hooked foot of bare X. There is no independent i-dot here.',
     'confidence': 'medium'},
]

data['notes'] = [
    'This is a text sheet: 24 main writing lines, including four displayed/added formula rows, two diagonal margin notes, three interlinear insertions besides the added condition b, six cancelled passages, and a bottom-left number. No drawing or diagram is present.',
    'Reported content: the heading introduces stratifications and conic neighbourhoods as a recurrence step. An increasing family (X_i) is required to satisfy a binary-intersection formula indexed by common lower bounds and to cover X. The left margin writes an analogous formula for arbitrary intersections.',
    'Reported content: a system of boundary parts B_alpha carries mutually transverse cylinder germs. The text imposes/expresses transversality of X_i to their cylinders and writes a product relation involving E_J, B_J, I^J, and X_iJ=X_i∩B_J.',
    'Reported content: a minimal-index subset I_0 gives a union identified with a coproduct. The page then relates a strict conic-neighbourhood germ along X_I0 to mutually disjoint conic neighbourhoods of the X_i, and continues with a family-of-germs formulation.',
    'No targeted proof check, independent re-proof, computation, or background-verification claim is made. These notes report manuscript assertions only; check_events is intentionally empty.',
    'The second I_0 in “une partie de I_0” has a visible small zero. The resulting redundancy is retained as a possible authorial slip, not corrected from the surrounding mathematics.',
    'The product line has an opening parenthesis before X_iJ with no close after the first I^J, and then a separate opening before induit. The next-line definition has its closing parenthesis and stop. No missing delimiter is supplied.',
    'The additional loop before E_Balpha is preserved as a doubtful l-apostrophe even though “aux l’” is linguistically anomalous. Its ink is distinct; its corrective history is unresolved.',
    'The word strict is physically below germe, but its leader attaches after cônique. Only one équivaut is visible. H’s account of two instances is not adopted.',
    'The later phrase “d’un germe de voisinage cônique de X” is retained literally. I do not replace X by X_I0 on mathematical grounds.',
    'The first X on the final line has a hooked lower-right foot without a separate dot, unlike the clearly dotted X_i in nearby formulas. Only that symbol is newly marked X_i|X; the final bare X and stop are clear.',
    'No independent stops are visible at the end of the coproduct display or between des X_i and the following dash. A single dot at X_i is treated as its index dot. The margin formula likewise has no visible terminal stop.',
    'The bottom-left 29 is thin-ink foliation with uncertain attribution. It is recorded through margin, not mspage. The body also contains section 7 and displayed label (14).',
    'The beginning of heading voisinages contains overwritten or retraced ink, but no reliable older word can be isolated. The live word is preserved; an independent struck word is not invented.',
    'All 33 registered crops were viewed. The first first_E_Balpha crop accidentally clipped the lower subscript and was superseded for evidence by first_E_Balpha_complete; both remain registered. The unresolved margin brace was revisited in the same existing crop; no settled half-page was re-zoomed.',
    'Whole-page layout and both native halves were read, including agreed tokens. Source-spelling cônique, undotted syst in the lower paragraph, dotted syst. in the upper paragraph, and vois. are preserved. H’s editorial notes are excluded.',
]

data['notation'] = [
    {'form': r'I, I_0, I^J', 'meaning_or_shape': 'Capital I has top and bottom bars; its top bar may be detached. A small attached closed loop is subscript zero. In the product expressions its stroke is much heavier than in the index-set prose.', 'places': 'lines 3, 5–6, 13, 15, 17, 19, 21'},
    {'form': r'J', 'meaning_or_shape': 'Capital J often resembles a squared right bracket with a curved or hooked lower foot. This is distinct from the straight capital I with a lower serif.', 'places': 'margin formula, product line 13, definition line 14, margin M02'},
    {'form': r'X_i', 'meaning_or_shape': 'The i may be attached as a short extension of X’s lower-right stroke, with its dot separated farther right. The bottom-line first X lacks an independently visible dot and remains doubtful.', 'places': 'product, coproduct, line 21, line 24'},
    {'form': r'E_{B_\alpha}', 'meaning_or_shape': 'E with a lower B and a nested lower alpha; the alpha is a small loop with crossing/exit stroke. There are two separate references in the transversal paragraph.', 'places': 'lines 11–12'},
    {'form': r'\simeq', 'meaning_or_shape': 'A shallow wavy upper stroke over a straight short lower stroke; retained as the product-relation sign.', 'places': 'line 13, twice'},
    {'form': r'\coprod', 'meaning_or_shape': 'Two upright strokes meeting a long horizontal lower bar, distinct from the rounded union immediately before it.', 'places': 'line 17'},
    {'form': r'\unsure{\{}', 'meaning_or_shape': 'Tentative grouping left brace beside the two union-limit conditions. The stroke is crowded by the lower k and may include correction ink; the symbol is not established as certain.', 'places': 'left margin beside (14)'},
]
data['abbreviations'] = [
    {'form': 'syst.', 'expansion': 'système; expansion supplied only in this apparatus, not in the transcription'},
    {'form': 'syst', 'expansion': 'système; the lower occurrence is written without a stop'},
    {'form': 'vois.', 'expansion': 'voisinages; expansion supplied only in this apparatus, not in the transcription'},
]
data['hand_log'] = [
    {'habit': 'Cursive e/n/m/r sequences are often flattened into near-horizontal strokes, while p/q/g/l ascenders or descenders remain salient.',
     'places': 'représente les germes; convenables; imposant/exprimant; ensemble; l’on a',
     'consistent': 'Seen repeatedly within this sheet; cancellation and the right paper edge reduce recoverability at specified places.',
     'witness_errors': 'H reads jeu for pas, représentant for représente, l’isom. for l’on a, and leaves several recoverable spans as illegible.'},
    {'habit': 'Accented or dotted small letters can reduce to isolated blobs; a compressed à may resemble a colon.',
     'places': 'équivaut final cluster; dotted i in muni and X_i; accented généralise',
     'consistent': 'The cluster after équivaut remains unresolved; ordinary i dots are clear in several nearby examples.',
     'witness_errors': 'C gives à without doubt, H first gives a colon and later duplicates équivaut; the actual cluster remains à|:.'},
    {'habit': 'The capital I can have a detached cap; its small zero may join the lower serif.',
     'places': 'I_0 after une partie de; all three I_0 occurrences in the coproduct display',
     'consistent': 'All clear zero occurrences on this sheet support this shape.',
     'witness_errors': 'H omits the second I_0’s explicit zero; C leaves I_0|I doubtful.'},
    {'habit': 'An i index may continue X’s lower-right stroke, with a separate dot that can be mistaken for punctuation.',
     'places': 'final X_i in coproduct; des X_i before dash; bottom-line first X',
     'consistent': 'The bottom-line first X has no separate dot and is the explicit exception retained as a doubt.',
     'witness_errors': 'Both witnesses add a separate stop at the coproduct end and before the dash; neither flags the bottom-line undotted ambiguity.'},
    {'habit': 'Curved leaders can carry an interlinear insertion to a gap away from its physical position.',
     'places': 'B_alpha above parties-bord; exprimant below imposant; strict below germe',
     'consistent': 'Clear leader for B_alpha and strict; the end of the exprimant leader is crowded near que.',
     'witness_errors': 'H duplicates B_alpha and attaches strict after germe rather than at the leader’s destination after cônique.'},
    {'habit': 'Cancellations range from a long baseline stroke leaving letter tops visible to densely blackened oblique scribbles.',
     'places': 'Bien sûr les; de structure; initial Soit and Alors; cancelled et soit; margin word after J',
     'consistent': 'Bien sûr les and de structure are substantially recoverable; the other named spans retain narrow doubts.',
     'witness_errors': 'H leaves Bien sûr les as wholly illegible; C’s four unresolved cancelled-word candidates are not promoted to certain readings.'},
]

def second(kind, reading, reason, crop=None, coords=None):
    data['second_boxes'].append({
        'box': f"b{len(data['second_boxes']) + 1:02d}", 'kind': kind,
        'coords': coords if coords is not None else crops[crop]['box'],
        'reading': reading, 'reason': reason,
    })

second('handwritten number', '7.', 'Section number in the heading.',
       coords=[315, 72, 440, 184])
second('struck passage|C/H word difference', r'\uline{voisinages côniques}',
       'Overwritten heading word; witnesses differ about whether a separate cancelled word is present.',
       'heading_voisinages')
second('C/H word difference', 'le pas', 'Heading word differs between witnesses.', 'heading_pas')
second('C/H word difference|insertion', 'de récurrence.',
       'Heading continuation differs in wording, number, punctuation, and added-text state.', 'heading_recurrence')
second('handwritten number',
       r'(14)\qquad\text{a) }\forall i,j\in I,\ \text{on a}\qquad X_i\cap X_j=\bigcup_{\alpha\le i,j}X_\alpha.',
       'Displayed equation number; the complete adjacent expression is included.', 'condition14')
second('margin note|doubt formula|C/H word difference|low-confidence departure',
       r'\margin{Cette condition se généralise : aux intersections quelconques $\displaystyle\bigcap_{i\in J}X_i=\bigcup_{\unsure{\{}\,\substack{k\in I\\k\text{ minorant }J}}X_k$}',
       'Complete diagonal marginal note; wording differs and the full formula includes an unresolved limit-grouping stroke.',
       'margin_generalization')
second('insertion', r'\inserted{b) $X=\bigcup_{i\in I}X_i$}',
       'Smaller second condition, provisionally encoded as an insertion; its complete formula is included.', 'condition_b')
second('insertion|C/H word difference', r'parties-bord \inserted{$B_\alpha$} de',
       'Boundary-part wording differs; the raised symbol and its attachment are included.', 'parties_bord_Balpha')
second('C/H word difference', 'Transversalité', 'The witnesses encode different underlining states.', 'transversalite')
second('C/H word difference', 'muni', 'Word ending differs between witnesses.', 'muni')
second('C/H word difference', 'représente les germes',
       'Wording and reading order differ between witnesses.', 'represente_les_germes')
second('C/H word difference', r'par des cylindres convenable\unsure{s}',
       'Readable words replace an illegibility span; the word reaches the physical right edge and retains a terminal-letter doubt.',
       'cylindres_convenables')
second('doubt formula', r'$E_{B_\alpha}$,',
       'Additional formula audit: first cylinder reference differs by omission between witnesses; the whole nested subscript is included.',
       'first_E_Balpha_complete')
second('insertion|C/H word difference|low-confidence departure', r'imposant\inserted{exprimant}',
       'Interlinear addition and adjacent main-line word; both C marks are resolved provisionally at moderate confidence.',
       'imposant_exprimant')
second('doubt formula|C/H word difference|low-confidence departure', r"aux \unsure{l'}$E_{B_\alpha}$",
       'The wording differs and extra looped ink is unresolved; the complete following cylinder symbol is included.', 'aux_E')
second('C/H word difference', "l'on a", 'Wording differs at the end of the transversal sentence.', 'lon_a')
second('doubt formula',
       r'E_J\cap X_i\simeq (X_{iJ}\times I^J \qquad \text{(induit par }E_J\simeq B_J\times I^J,',
       'Complete two-part product formula; witnesses differ about a delimiter. Included for formula audit.', 'product_relation')
second('C/H word difference', r'avec $X_{iJ}=X_i\cap B_J$).',
       'The introductory word differs; the complete definition and its punctuation are included.', 'avec_definition')
second('struck passage|C/H word difference|low-confidence departure', r'\deleted{Bien sûr les}',
       'Entire cancelled phrase; C doubt resolved at moderate confidence and H gives illegibility.', 'bien_sur_les')
second('margin note|struck passage|C/H word difference|low-confidence departure',
       r"\margin{pour $J$ \deleted{\unsure{ensemble}} ensemble d'indices $\alpha$}",
       'Complete second diagonal margin note, including its cancelled word and live wording; one C doubt remains.', 'margin_J')
second('struck passage|C/H word difference', r'\deleted{\unsure{Soit}}',
       'Entire cancelled opening; candidate remains uncertain.', 'struck_soit')
second('handwritten number', r'Soit $I_0\subset I$',
       'The first I_0 in the minimal-index sentence contains a handwritten zero; the inclusion expression is included.',
       coords=[440, 1305, 920, 1450])
second('handwritten number|doubt formula|C/H word difference', r'une partie de $I_0$ formée',
       'The second I_0 contains a handwritten zero and resolves a C symbol doubt; the phrase differs from H.', 'I0_part')
second('struck passage|C/H word difference', r'\deleted{et \unsure{soit}} et soit',
       'Entire cancelled phrase together with the adjacent live phrase; the cancelled second word remains doubtful.', 'struck_et_soit')
second('handwritten number', r'X_{I_0}=\bigcup_{i\in I_0}X_i=\coprod_{i\in I_0}X_i',
       'Complete union–coproduct formula, including all three handwritten subscript zeros and terminal punctuation state.', 'coproduct')
second('struck passage|C/H word difference', r'\deleted{\unsure{Alors}}',
       'Entire cancelled opening; candidate remains uncertain.', 'struck_alors')
second('struck passage', r"La donnée d'un germe \deleted{de structure}",
       'Complete cancelled de structure with adjacent live phrase.', 'germe_structure')
second('insertion|handwritten number|C/H word difference', r'\inserted{strict} de $X_{I_0}$',
       'Interlinear addition and its attachment; the nearby full X_I0 includes a handwritten zero.', 'strict_attachment')
second('C/H word difference', r"d'un voisinage cônique",
       'The words occupy a different reading-order position in the two witnesses.', 'dun_voisinage')
second('C/H word difference', r'équivaut \unsure{à|:}',
       'Witnesses differ in repetition and punctuation; the terminal cluster remains unresolved.', 'equivaut_a')
second('C/H word difference', 'syst de', 'Abbreviation-stop state differs between witnesses.', 'syst_de')
second('handwritten number', r'$T_i$ ($i\in I_0$)',
       'The parenthetical indexing condition contains a handwritten zero; the full expression is included.',
       coords=[310, 1945, 960, 2095])
second('doubt formula|C/H word difference|low-confidence departure', r'disjoints des $X_i$ ---',
       'Complete phrase containing the resolved C word/formula alternatives; punctuation is included.', 'des_Xi')
second('doubt formula', r'$\unsure{X_i|X}$ dans $X$.',
       'Full bottom-line symbol sequence; the first symbol has an unresolved attached-foot/index reading.', 'final_Xi')
second('margin note|handwritten number', r'\margin{29}',
       'Thin-ink bottom-left foliation; attribution is unresolved.', 'margin29')

data['crops'] = [
    {
        'file': crops[name]['file'], 'box': crops[name]['box'],
        'rotation_degrees': crops[name]['rotation_degrees'], 'viewed': True,
        'status': ('clipped initial attempt; superseded for evidence by first_E_Balpha_complete'
                   if name == 'first_E_Balpha' else 'used or retained for audit'),
    }
    for name in names
]
data['crop_place_count'] = 32
data['crop_image_count'] = 33
data['line_count_basis'] = 'Twenty-four main writing lines, counting displayed condition a, smaller condition b, product display, and coproduct display; margin notes and interlinear additions are separate inventory elements.'

def norm(s):
    return re.sub(r'\s+', '', s)

def escaped(s, i):
    n = 0
    j = i - 1
    while j >= 0 and s[j] == '\\':
        n += 1
        j -= 1
    return n % 2 == 1

def balanced(s):
    depth = 0
    for i, ch in enumerate(s):
        if ch in '{}' and not escaped(s, i):
            depth += 1 if ch == '{' else -1
            assert depth >= 0, ('unmatched close', i)
    assert depth == 0, ('unclosed braces', depth)

def source_marks(s):
    result = []
    for match in re.finditer(r'\\(?:unsure|illegible)\{', s):
        start = match.start()
        depth = 1
        i = match.end()
        while depth and i < len(s):
            if s[i] in '{}' and not escaped(s, i):
                depth += 1 if s[i] == '{' else -1
            i += 1
        assert depth == 0
        result.append(s[start:i])
    return result

kinds = {
    'misread word', 'misread symbol or index', 'omission', 'text not on the page',
    'deletion state (struck given live or live given struck)', 'insertion or placement',
    'abbreviation expanded or spelling modernised', r'readable ink left as \ill{}',
    'drawing or diagram', 'other',
}
errors = {
    'symbols and indices', 'words', 'omissions', 'drawings and diagrams',
    'readable ink left as illegible', 'insertion placement', 'struck text',
    'abbreviation/spelling', 'text not on page', 'other',
}
for row in data['changes']:
    assert row['kind'] in kinds, row
    assert row['error_kind'] in errors, row
    for witness, source in [('C', C), ('H', H)]:
        if row[witness] != '[absent]':
            assert norm(row[witness]) in norm(source), (witness, row['place'], row[witness])
    assert norm(row['final']) in norm(TEX), ('final missing', row['place'], row['final'])
    assert (BASE / 'crops' / row['crop']).is_file()
for row in data['marks']:
    assert norm(row['context']) in norm(C), ('mark context', row)
    assert (BASE / 'crops' / row['crop']).is_file()
assert Counter(source_marks(C)) == Counter(row['mark'] for row in data['marks'])
for row in data['second_boxes']:
    x0, y0, x1, y1 = row['coords']
    assert 0 <= x0 < x1 <= 1690 and 0 <= y0 < y1 <= 2360, row
    assert norm(row['reading']) in norm(TEX), ('second reading absent', row)
balanced(TEX)
data['validation'] = {
    'source_quotes_checked': True, 'all_proposed_changes_present_in_tex': True,
    'all_C_marks_accounted_for': True, 'tex_braces_balanced': True,
    'all_crop_paths_exist': True, 'all_crops_viewed': True,
    'all_second_box_readings_present_in_tex': True,
    'no_ocr': True, 'no_tex_compilation': True, 'only_assigned_page_read': True,
}
(OUT / '150_scan030.json').write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({
    'scan': data['scan'], 'changes': len(data['changes']), 'marks': len(data['marks']),
    'inventory': len(data['inventory']), 'second_boxes': len(data['second_boxes']),
    'crop_places': data['crop_place_count'], 'crop_images': data['crop_image_count'],
    'tex': str(OUT / '150_scan030.tex'), 'json': str(OUT / '150_scan030.json'),
}, ensure_ascii=False))


