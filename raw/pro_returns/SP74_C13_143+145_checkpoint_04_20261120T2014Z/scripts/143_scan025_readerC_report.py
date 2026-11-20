from pathlib import Path
import json

root=Path('/workspace/scratch/8f839dff4bf0')
work=root/'SP74_C13_143+145_work'
p=json.loads((root/'reader_packets/143_scan025.json').read_text())
C,H=p['witness_C'],p['witness_H']
key='143_scan025'
tex=r'''\scanpage{25}
$\pi$ sur $\Lambda$, compatibles avec ses op. sur $\pi$ par autom int. Pour ceci, on va exiger
\[
\left\{\begin{gathered}
\forall t\in\unsure{\tau|\mathcal T}=\operatorname{Ob}\Lambda,\quad\text{la famille des}\\
\pi_{t,t'}\subset\pi\quad(t'\in\unsure{\tau|\mathcal T}\text{ variable})\text{ forme une}\\
\text{pseudo-partition de }\pi,\text{ i.e. }\forall\lambda\in\pi,\\
\exists\text{ un unique }t'\text{ tel que }\lambda\in\pi_{t\unsure{,|;}t'}\\
\text{i.e. une unique flèche de }\Lambda\text{ au-dessus}\\
\text{de }\lambda\text{ qui soit d'origine }t.
\end{gathered}\right.
\]
\margin{examinons à part ce condition $\exists!$ de remontage des flèches à origine remontée, pour un morphisme de groupoïdes\ldots}
ce qui donne l'opération de $\pi$ sur $\underset{\unsure{t}}{\unsure{\tau|\mathcal T}=\operatorname{Ob}\Lambda}$, et la façon de reconstituer
\[
\Lambda\simeq\langle\unsure{\tau|\mathcal T},\pi\rangle
\]
et le foncteur $\Lambda\longrightarrow\langle\pi\rangle$. \deleted{\unsure{Dans}} \inserted{On} \deleted{\illegible{1}} suppose de plus que les stabilisateurs $\pi_t$ sont abéliens, d'où une famille de \unsure{grpes|groupes} $(T_j)_{j\in J=\unsure{\tau|\mathcal T}/\pi)}$ et opérations de $\unsure{\mathcal E|\Sigma}$ sur $(T,\Lambda)$, de sorte que $\Lambda\longrightarrow\langle\pi\rangle$ soit compatible avec op. de $\unsure{\mathcal E|\Sigma}$\ldots.

Ce n'est pas bien élucidant --- peut-être est-il plus agréable de
\mspage{24}
'''

boxes={
 'margin-note':[25,548,424,1014],
 'partition-family':[472,478,1315,588],
 'tprime-condition':[1322,656,1580,772],
 'object-set-mark':[1437,942,1655,1068],
 'first-deletion-on':[1437,1206,1655,1325],
 'second-deletion-suppose':[350,1373,847,1487],
 'family-index':[986,1545,1657,1703],
 'operations-plural':[458,1709,861,1825],
 'compatibility-dots':[880,1920,1115,2032]
}
def crop(name):
 return f'crops/{key}_readerC_{name}.png' if name else 'page'
changes=[]
def add(place,c,h,final,against_C,against_H,kind,ink,confidence='high',locus=None,marked=False,consequential=False):
 assert c=='[no witness]' or c in C,(place,'C excerpt',c)
 assert h=='[no witness]' or h in H,(place,'H excerpt',h)
 assert final in tex,(place,'final excerpt',final)
 changes.append(dict(place=place,C=c,H=h,final=final,against_C=against_C,against_H=against_H,kind=kind,ink=ink,confidence=confidence,crop=crop(locus),box=boxes.get(locus),marked_in_H=marked,consequential=consequential))

add('Opening line: abbreviation before int.', 'autom', 'automorph.', 'autom', False, True,
 'abbreviation expanded or spelling modernised',
 'The word ends after the joined a-u-t-o-m run; no o-r-p-h segment or terminal abbreviation point follows m before int.')
add('Braced condition, first line: object-set letter',r'\forall t\in\tau',r'\forall t \in \mathcal{T}',r'\forall t\in\unsure{\tau|\mathcal T}',True,True,
 'misread symbol or index','A rounded set glyph with a short upper stroke is present; its alphabet cannot be settled as tau versus calligraphic T from this occurrence. The following equals and Ob Lambda are intact.','medium')
add('Braced condition, second line: variable target set',r"(t'\in\tau\text{ variable})",r"(t' \in \mathcal{T} \text{ variable})",r"(t'\in\unsure{\tau|\mathcal T}\text{ variable})",True,True,
 'misread symbol or index','The second t has a genuine attached upper-right prime, followed by membership and the same rounded set glyph. There is no evidence to force an alphabet beyond the provisional tau/T choice.','medium','partition-family')
add('Braced condition, fourth line: separator and terminal punctuation in membership formula',r"\lambda\in\pi_{t,t'},",r"\lambda \in \pi_{t,t'},",r"\lambda\in\pi_{t\unsure{,|;}t'}",True,True,
 'misread symbol or index','Both t letters and the attached prime on the second t are visible. Between the index letters a dark upper dot lies above a lower comma-like stroke: comma with a retrace and semicolon remain possible. There is no separate comma to the right of the final prime; neither witness\'s external comma is retained.','medium','tprime-condition')
add('Left margin, opening phrase',r'examinons à part \unsure{ce|cette} condition',r'examinons \ill{} condition','examinons à part ce condition',False,True,
 'readable ink left as \\ill{}','After examinons the accent of à and the short p-a-r-t sequence are visible. The determiner has an open c and one low e, with no tall or crossed t strokes. The grammatically unusual ce condition is preserved.','high','margin-note',True)
add('Left margin: first lifting word','de remontage des','de remontée des','de remontage des',False,True,
 'misread word','The first lifting word has a descending g loop before its final e; it is remontage, unlike the later remontée in the same note.','high','margin-note')
add('Left margin: flèches','flèches','glissements','flèches',False,True,
 'misread word','The initial tall f/l strokes, accented e, and short che-s ending make flèches; the longer g-l-i-s-s-e-m-e-n-t-s sequence is not present.','high','margin-note')
add('Left margin: à before origine','à origine',': origines','à origine',False,True,
 'misread word','A compact a and a separate accent stand before origine. Their stacked position can resemble a colon, but the lower mark is the letter; the phrase has no colon.','high','margin-note')
add('Left margin: singular origine','origine','origines','origine',False,True,
 'misread word','The word ends with the low e return immediately before remontée; there is no separate terminal s.','high','margin-note')
add('Left margin: second lifting word',r'origine \unsure{remontée},',r'origines \ill{},','origine remontée,',False,True,
 'readable ink left as \\ill{}','The re-mon sequence is followed by a tall crossed t, an accent, and a low final ée run. There is no g descender here. The comma after the word is present.','high','margin-note',True)
add('Left margin: final qualifying phrase','pour un morphisme de groupoïdes',r'\ill{} \ill{} de groupoïdes','pour un morphisme de groupoïdes',False,True,
 'readable ink left as \\ill{}','The connected p-o-u-r, short un, and long m-o-r-ph-i-s-m-e run occupy the last note line before de groupoïdes.','high','margin-note',True)
add('Main continuation after brace: initial case',"ce qui donne l'opération", "Ce qui donne l'opération", "ce qui donne l'opération",False,True,
 'misread word','The initial c is low and open, the same height as the following e; it is not an enlarged capital C.')
add('Main continuation: round set equation and separate lower mark',r'\unsure{\underset{t}{\tau}|\tau}=\operatorname{Ob}\Lambda',r'\mathcal{T} = \mathrm{Ob}\,\Lambda',r'\underset{\unsure{t}}{\unsure{\tau|\mathcal T}=\operatorname{Ob}\Lambda}',True,True,
 'insertion or placement','There is a separate dark crossed t-like stroke below the equation. Its centre lies below the middle of the whole tau/T = Ob Lambda expression, rather than directly beneath the set glyph. Its curved stem, horizontal cross stroke, and lower return are genuine ink; whether it is an index, a correction remnant, or unattached writing is not established. The underset reproduces position without assigning an index meaning.','low','object-set-mark',False,True)
add('Main continuation: façon','façon',r'\uncertain{vérification}','façon',False,True,
 'misread word','A tall f, short a-ç-o-n sequence, and lower cedilla are visible. The compact five-letter word cannot support the longer vérification reading.','high',None,True)
add('Main continuation: reconstituer','façon de reconstituer',r'\uncertain{vérification} de','façon de reconstituer',False,True,
 'omission','After de, a separate full reconstituer run extends across the line, with its repeated tall t strokes and terminal er. H stops after de.','high',None,True)
add('Reconstruction display: set letter',r'\langle\tau,\pi\rangle',r'\langle \mathcal{T}, \pi \rangle',r'\langle\unsure{\tau|\mathcal T},\pi\rangle',True,True,
 'misread symbol or index','The first object inside the angle brackets is the same rounded set letter, followed by a comma and pi. Its tau/T alphabet remains provisional.','medium')
add('After first functor: deleted word',r'\deleted{\unsure{Dans}}',r'\ill{} \struck{\ill{}}',r'\deleted{\unsure{Dans}}',False,True,
 'deletion state','A capital D survives above a strong horizontal cancellation. A low closed second letter and fragments of the later letters remain, supporting Dans provisionally but not excluding Donc or another D-word. The deletion is separate from the later canceled word at the next line\'s start. H\'s initial gap does not identify this deletion.','low','first-deletion-on',True)
add('Above first canceled word: replacement On',r'\deleted{\unsure{Dans}} On',r'\ill{} \struck{\ill{}}',r'\deleted{\unsure{Dans}} \inserted{On}',True,True,
 'insertion or placement','An enlarged oval O and trailing n are written above the canceled D-word. They are live replacement writing, not part of its cancellation; C gives On on the line without the insertion state.','high','first-deletion-on',True)
add('After second cancellation: suppose','suppose de plus',r'\ill{} de plus','suppose de plus',False,True,
 'readable ink left as \\ill{}','The live s-u-p-p-o-s-e run follows the separate canceled short word and precedes the legible de plus. The cancellation ends before suppose.','high','second-deletion-suppose',True)
add('Lower paragraph: family of groups, short word','une famille de groupes','une famille de groupes',r'une famille de \unsure{grpes|groupes}',True,True,
 'abbreviation expanded or spelling modernised','The compact word before the family expression has an initial descending g, an r shoulder, a p-like descent, and a short e-s tail. An explicit ou sequence is not separately recoverable; grpes is the leading reading, but tightly collapsed groupes remains possible.','medium','family-index')
add('Family index: quotient-set letter',r'J=\tau/\pi',r'J = \mathcal{T}/\pi',r'J=\unsure{\tau|\mathcal T}/\pi',True,True,
 'misread symbol or index','Following the angular J and two equals strokes, the rounded set glyph is followed by a solidus and pi. Its alphabet remains tau/T.','medium','family-index')
add('Family expression: final parenthesis and following punctuation',r'$(T_j)_{j\in J=\tau/\pi}$ et',r'$(T_j)_{j \in J = \mathcal{T}/\pi}$, et',r'$(T_j)_{j\in J=\unsure{\tau|\mathcal T}/\pi)}$ et',True,True,
 'omission','A distinct right parenthesis is written after pi at the level of the lowered index clause. Both witnesses omit it. There is no separate comma following that parenthesis before the next-line et. The unmatched visible parenthesis is retained without supplying a missing mate.','high','family-index')
add('Lower paragraph: plural opérations','et opérations de','et opération de','et opérations de',False,True,
 'misread word','The word has a terminal hooked s after its compressed ion run; the next de is separate. The plural opérations is retained.','medium','operations-plural')
add('Lower paragraph: first extension/action-group glyph',r'$\mathcal E$ sur',r'$\Sigma$ sur',r'$\unsure{\mathcal E|\Sigma}$ sur',True,True,
 'misread symbol or index','The rounded extension/action-group glyph is present. Its cursive E versus Sigma identification is globally unresolved; this row records that provisional alphabet encoding only.','low')
add('Compatibility clause: second extension/action-group glyph',r'avec op. de $\mathcal E$',r'avec op.\ de $\Sigma$',r'avec op. de $\unsure{\mathcal E|\Sigma}$',True,True,
 'misread symbol or index','The second rounded glyph has an upper curved stroke, middle reversal, and lower hooked return; it does not settle the E/Sigma disagreement. Only the provisional alphabet encoding changes.','low','compatibility-dots')
add('Compatibility clause: continuation punctuation',r'$\mathcal E$\ldots',r'$\Sigma$ \ldots',r'$\unsure{\mathcal E|\Sigma}$\ldots.',True,True,
 'omission','Four separate dark continuation marks lie in a horizontal row after the glyph. The last is slightly elongated; it is a fourth mark rather than paper noise. Both witnesses supply only three.','high','compatibility-dots')
add('Final author comment: élucidant','élucidant','éclairant','élucidant',False,True,
 'misread word','After initial é-l, the source has a u trough, c, dotted i and tall d, followed by ant. This gives élucidant rather than éclairant.')
add('Bottom-left pencil numeral',r'\mspage{24}','[no witness]',r'\mspage{24}',False,True,
 'omission','A light pencil 2 followed by angular 4 sits at the lower left. The numeral is retained, with the hand left unnamed rather than attributed to the author.')

report={
 'key':key,'reader':'C','stage':'first','image_views':['original','half1','half2'],
 'changes':changes,
 'decisions':[
  dict(id='M0706',decision='first',reading='ce',ink='The determiner has an open c and one low e, with no upright or crossing for either t of cette. The uncorrected source phrase is ce condition.',crop=crop('margin-note'),box=boxes['margin-note'],confidence='high'),
  dict(id='M0707',decision='first',reading='remontée',ink='After re-mon are a tall crossed t, an accent and the low ée ending. The preceding remontage in the note has a g descender that this occurrence lacks.',crop=crop('margin-note'),box=boxes['margin-note'],confidence='high'),
  dict(id='M0708',decision='other',reading=r'\underset{\unsure{t}}{\unsure{\tau|\mathcal T}=\operatorname{Ob}\Lambda}',ink='A genuine crossed t-like sign lies below the centre of the whole equation, farther right than the round set glyph. C\'s alternatives omit the attachment uncertainty. Retain the sign provisionally below the expression; neither an index nor a correction role is established.',crop=crop('object-set-mark'),box=boxes['object-set-mark'],confidence='low')
 ],
 'inventory':[
  dict(sheet_kind='text',hand='his hand',element='E01',kind='text',position='Top, opening continuation before brace',first_words_or_objects=r'$\pi$ sur $\Lambda$, compatibles',transcribed='yes'),
  dict(sheet_kind='text',hand='his hand',element='E02',kind='display',position='Upper centre/right, six lines under left brace',first_words_or_objects=r'\forall t\in\unsure{\tau|\mathcal T}=\operatorname{Ob}\Lambda',transcribed='yes'),
  dict(sheet_kind='text',hand='his hand',element='E03',kind='margin note',position='Left margin beside the braced condition; slanted lines',first_words_or_objects='examinons à part ce condition',transcribed='yes'),
  dict(sheet_kind='text',hand='his hand',element='E04',kind='text',position='Below brace, two-line explanation',first_words_or_objects="ce qui donne l'opération",transcribed='yes'),
  dict(sheet_kind='text',hand='his hand',element='E05',kind='text',position='Separate t-like sign below centre of object-set equation, around original x1546',first_words_or_objects=r'\unsure{t}; attachment not established',transcribed='yes'),
  dict(sheet_kind='text',hand='his hand',element='E06',kind='display',position='Mid-page reconstruction display',first_words_or_objects=r'\Lambda\simeq\langle\unsure{\tau|\mathcal T},\pi\rangle',transcribed='yes'),
  dict(sheet_kind='text',hand='his hand',element='E07',kind='text',position='Immediately below reconstruction display',first_words_or_objects=r'et le foncteur $\Lambda\longrightarrow\langle\pi\rangle$',transcribed='yes'),
  dict(sheet_kind='text',hand='his hand',element='E08',kind='deletion',position='Right end of first functor line',first_words_or_objects=r'\deleted{\unsure{Dans}}',transcribed='yes'),
  dict(sheet_kind='text',hand='his hand',element='E09',kind='insertion',position='Above the canceled D-word',first_words_or_objects='On',transcribed='yes'),
  dict(sheet_kind='text',hand='his hand',element='E10',kind='deletion',position='Start of next line, before suppose',first_words_or_objects=r'\deleted{\illegible{1}}',transcribed='yes'),
  dict(sheet_kind='text',hand='his hand',element='E11',kind='text',position='Lower paragraph from suppose through compatibility clause',first_words_or_objects='suppose de plus que les stabilisateurs',transcribed='yes'),
  dict(sheet_kind='text',hand='his hand',element='E12',kind='text',position='Final main-text paragraph, unfinished at de',first_words_or_objects="Ce n'est pas bien élucidant",transcribed='yes'),
  dict(sheet_kind='text',hand='unnamed hand',element='E13',kind='margin note',position='Bottom-left pencil numeral',first_words_or_objects='24',transcribed='yes')
 ],
 'remaining_doubts':[
  dict(place='Five occurrences of the round object/quotient set label',reading=r'\unsure{\tau|\mathcal T}',alternatives=r'\tau / \mathcal T',confidence='medium',reason='The rounded handwritten form is consistent locally, but tau versus calligraphic T remains a provisional alphabet choice. The different ornate Z form from the common notation table is not imposed.'),
  dict(place='Two extension/action-group glyphs',reading=r'\unsure{\mathcal E|\Sigma}',alternatives=r'\mathcal E / \Sigma',confidence='low',reason='The current common notation decision remains provisional; neither occurrence supplies decisive new alphabet evidence.'),
  dict(place='Fourth line of condition, separator between t and t-prime',reading=r"\pi_{t\unsure{,|;}t'}",alternatives='Comma with a dot/retrace / semicolon',confidence='medium',reason='An upper dark dot and lower comma-like stroke survive within the index. No external terminal comma is visible. See crops/143_scan025_readerC_tprime-condition.png.'),
  dict(place='M0708: lower sign and attachment under object-set equation',reading=r'\underset{\unsure{t}}{\unsure{\tau|\mathcal T}=\operatorname{Ob}\Lambda}',alternatives='t-like sign beneath whole equation / index intended for set glyph / correction remnant or unattached sign',confidence='low',reason='The sign is real ink but horizontally centred below the equation rather than the set letter. Position is represented; its mathematical function remains open. See crops/143_scan025_readerC_object-set-mark.png.'),
  dict(place='First cancellation, below inserted On',reading=r'\deleted{\unsure{Dans}}',alternatives='Dans / Donc or another D-word',confidence='low',reason='D and a low rounded second letter survive; the horizontal strike masks the later letters. See crops/143_scan025_readerC_first-deletion-on.png.'),
  dict(place='Second cancellation, before suppose',reading=r'\deleted{\illegible{1}}',alternatives='Short canceled word, unrecoverable',confidence='low',reason='The strong cancellation covers nearly the entire word. Only isolated lower fragments and one taller terminal stroke remain; they do not license a word. See crops/143_scan025_readerC_second-deletion-suppose.png.'),
  dict(place='Word before family expression',reading=r'\unsure{grpes|groupes}',alternatives='Abbreviated grpes / rapidly collapsed groupes',confidence='medium',reason='The visible compact g-r-p-e-s-like run does not separate an ou, but rapid joining cannot be excluded. See crops/143_scan025_readerC_family-index.png.')
 ],
 'certainty_resolutions':[
  dict(place='M0706, margin determiner',C=r'\unsure{ce|cette}',final='ce',ink='Only c and low e are present; no t strokes.'),
  dict(place='M0707, margin after origine',C=r'\unsure{remontée}',final='remontée',ink='The crossed t and accented low ée ending distinguish this occurrence from the earlier g-bearing remontage.'),
  dict(place='Stabilizers in lower paragraph; H uncertainty only',C='stabilisateurs',final='stabilisateurs',ink='The full s-t-a-b-i-l-i-s-a-t-e-u-r-s sequence is live, with tall t/l strokes and final s; C already gives this reading, while H wraps it in uncertain.')
 ],
 'notation':[
  dict(form=r'\unsure{\tau|\mathcal T}',meaning='Object set of Lambda and its quotient label; provisional alphabet',evidence='Five semantic occurrences inspected: two in the condition, one in the action equation, one in the reconstruction, and one in the family index.'),
  dict(form=r'\unsure{\mathcal E|\Sigma}',meaning='Extension/action-group notation; unresolved alphabet',evidence='Two occurrences in the lower paragraph, the second visible in the continuation-punctuation crop.'),
  dict(form=r'\pi_{t,t\prime}',meaning='Source/target-indexed subsets of pi',evidence='Both indexed pairs have t and a second primed t; the second pair has a locally uncertain internal separator.'),
  dict(form=r'\Lambda\longrightarrow\langle\pi\rangle',meaning='Functor shown twice in the prose',evidence='Both horizontal shafts have visible terminal heads; no bare shaft is converted from mathematical expectation.'),
  dict(form=r'\underset{\unsure{t}}{\unsure{\tau|\mathcal T}=\operatorname{Ob}\Lambda}',meaning='Positional rendering of the unresolved lower sign, not an asserted index',evidence='Its horizontal centre is under the complete equation rather than just the set glyph.'),
  dict(form=r'$(T_j)_{j\in J=\unsure{\tau|\mathcal T}/\pi)}$',meaning='Family expression with the visible additional closing parenthesis retained',evidence='A closing curve follows pi in the lowered index run; no missing opening parenthesis is supplied.')
 ],
 'abbreviations':[
  dict(form='op.',expansion='opération(s), according to context'),
  dict(form='autom',expansion='automorphismes'),
  dict(form='int.',expansion='intérieurs'),
  dict(form='i.e.',expansion='id est'),
  dict(form=r'\unsure{grpes|groupes}',expansion='groupes if the leading abbreviated reading is correct')
 ],
 'hand_log':[
  dict(habit='A t-prime can have its prime attached to the upper-right terminal stroke of t.',places='Both indexed pairs, parenthesised target variable, and unique-target clause in the condition.',scope='All four t-prime occurrences inspected on this page.',misreadings='No missing prime was inferred from notation; the visible ticks were checked individually.'),
  dict(habit='The object-set letter is round and can be encoded as tau or calligraphic T.',places='Five semantic occurrences throughout scan025.',scope='All current-page occurrences inspected; alphabet remains provisional.',misreadings='C tau versus H calligraphic T; both are retained as alternatives.'),
  dict(habit='The extension/action-group glyph has curved upper and lower returns.',places='Two lower-paragraph occurrences.',scope='Both inspected; no stronger alphabet conclusion than the common provisional E/Sigma decision.',misreadings='C E versus H Sigma.'),
  dict(habit='The final s may be a short down-hook joined to the preceding compressed letters.',places='opérations and the short group-word tail.',scope='Local observation; the group-word interior remains doubtful.',misreadings='H singular opération; both witnesses spell out groupes where the short source may be grpes.'),
  dict(habit='The same note distinguishes a descending g in remontage from crossed t and accented ée in remontée.',places='Two lifting words in the left margin.',scope='Both occurrences compared within the single margin crop.',misreadings='H reads the first word as remontée and leaves the second as illegible.'),
  dict(habit='Heavy horizontal cancellation may retain only the high capital or isolated terminal stroke.',places='D-word under On and separate short word before suppose.',scope='Both cancellations independently cropped and inspected.',misreadings='The first word remains doubtful; no word has been invented for the second.'),
  dict(habit='A separate underwritten sign need not be an index on the immediately preceding set glyph.',places='M0708 under the object-set equation.',scope='Single unresolved local placement.',misreadings='C confines alternatives to underset t on tau versus bare tau; the crop leaves attachment open.')
 ],
 'notes':[
  dict(id='143_scan025-N1',text='The page continues a discussion of actions of pi on Lambda compatible with inner automorphisms of pi. It imposes a pseudo-partition condition: for each source object and each lambda in pi, there is a unique target for membership in the indexed subset, restated as a unique arrow of Lambda over lambda with that source. The left margin asks to examine separately this existence-and-uniqueness lifting condition for a morphism of groupoids. This is an account of the source; the condition has not been proved or inferred from a theorem.'),
  dict(id='143_scan025-N2',text='The author says the condition gives the action on the object set and the way to reconstruct Lambda, with a displayed isomorphism and a functor to the one-object groupoid of pi. A t-like stroke below the object-set equation has uncertain attachment. The candidate preserves its visible position without asserting that it is an index or correcting it from the mathematics.'),
  dict(id='143_scan025-N3',text='After two separate cancellations and an inserted On, the author supposes that the stabilizers are abelian, gives a family indexed by the quotient object set, and asks for the indicated action to be compatible with the functor. The extra closing parenthesis after pi in the family index is preserved. The E/Sigma and tau/T alphabets remain provisional, and the short word before the family may be grpes rather than fully written groupes.'),
  dict(id='143_scan025-N4',text='The final author comment reads “Ce n\'est pas bien élucidant” and continues “peut-être est-il plus agréable de”, ending unfinished on this page. The wording reports the author\'s own dissatisfaction and is not replaced with H\'s éclairant.'),
  dict(id='143_scan025-N5',text='The margin reads ce condition without grammatical correction. The final compatibility clause has four continuation marks. The pencil numeral 24 at the bottom left is transcribed as a page numeral but assigned to an unnamed hand. H\'s description of the margin location is editorial and is excluded from source text.')
 ],
 'check_events':[
  dict(statement_id='143_scan025-condition',type='carried as background without fault found',outcome='Not proved. The displayed pseudo-partition and unique-arrow clauses were read against the ink and both witnesses; no implication was assumed to supply letters, primes, indices or punctuation.'),
  dict(statement_id='143_scan025-reconstruction',type='carried as background without fault found',outcome='Not proved. The reconstruction display and two headed functor arrows were visually inspected. No reconstruction argument was used to decide the unresolved lower sign.'),
  dict(statement_id='143_scan025-stabilizers-actions',type='carried as background without fault found',outcome='Not proved. The stabilizer, family and compatibility paragraph was transcribed. The unmatched closing parenthesis was not normalized from the expected family notation.')
 ],
 'unresolved_for_main':[
  'Inspect crops/143_scan025_readerC_object-set-mark.png for M0708: the t-like stroke is below the whole equation, not securely attached to the set glyph. Candidate retains a positional underset with doubtful t.',
  'Inspect crops/143_scan025_readerC_tprime-condition.png: internal comma-versus-semicolon and absence of a separate terminal comma; both primed t letters themselves are retained.',
  'Inspect crops/143_scan025_readerC_first-deletion-on.png: canceled D-word remains Dans provisionally; On is a live insertion above it.',
  'Inspect crops/143_scan025_readerC_second-deletion-suppose.png: second canceled short word remains physically unrecoverable.',
  'Inspect crops/143_scan025_readerC_family-index.png: grpes/groupes unresolved; definite extra closing parenthesis after pi retained at the index level, and H\'s external comma not retained.',
  'Global round-set tau/T and extension/action-group E/Sigma alphabet alternatives remain open; pure encoding rows have medium and low confidence respectively and are non-consequential.'
 ],
 'raw_difference_disposition':'All 25 packet differences were inspected against the original and both native halves. Difference 1 is the editorial scan marker; 3 and 7 are gathered/array syntax; 5 and 14 arise from H\'s TeX thin-space macro after Ob, not source commas; 12 is H\'s editorial marginal-location note. These do not receive material rows. Differences 2, 8–11, 15–16, 18, 20–24 and 25 are covered by the abbreviation, margin, reconstruction words, deletion/insertion/suppose, family punctuation, plural, extension-glyph, final-comment and pencil-numeral rows. Differences 4, 6, 13, 17 and 19 concern the round-set glyph; the action-equation occurrence additionally requires M0708 placement review. Agreements were also checked, including all quantifiers, memberships, subset sign, primes, indices, brace, angle brackets, source wording, arrows, corrections and marginal writing. Additional issues found in agreements are the final membership punctuation, short group-word, extra closing parenthesis and fourth continuation mark; lowercase ce also differs from H. Certainty-only resolutions and macro-only differences are excluded from material reading changes. All nine crops were emitted and visually inspected; no OCR, web research or TeX compilation was used.'
}

allowed={'misread word','misread symbol or index','omission','text not on the page','deletion state','insertion or placement','abbreviation expanded or spelling modernised','readable ink left as \\ill{}','drawing or diagram','other'}
assert [x['id'] for x in report['decisions']]==[x['id'] for x in p['marks']]
assert len(p['differences'])==25
for row in changes:
 assert row['kind'] in allowed,row['kind']
 if row['crop']!='page': assert (work/row['crop']).exists()
 if 'extension/action-group glyph' in row['place']:
  assert row['confidence']=='low' and row['consequential'] is False
for row in report['decisions']:
 assert row['reading'] in tex
for x in boxes:
 assert (work/crop(x)).exists()
(work/'reviews'/f'{key}_readerC.tex').write_text(tex)
(work/'reviews'/f'{key}_readerC.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'candidate':str(work/'reviews'/f'{key}_readerC.tex'),'report':str(work/'reviews'/f'{key}_readerC.json'),'changes':len(changes),'marks':len(report['decisions']),'inventory':len(report['inventory']),'crops':len(boxes)},indent=2))
