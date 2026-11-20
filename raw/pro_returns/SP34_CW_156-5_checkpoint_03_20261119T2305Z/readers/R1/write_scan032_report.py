from pathlib import Path
from datetime import datetime, timezone
import json, re

base = Path('/workspace/scratch/4770596940a0')
out = base / 'out/readers/R1'
prefix = 'crops/R1/scan032_'
rows = []

def row(i, place, C, H, reading, ink, confidence, kind, crop, against_C, against_H, marked_in_H=False):
    rows.append(dict(id=i, place=place, C=C, H=H, reading=reading, ink=ink,
                     confidence=confidence, kind=kind,
                     crop=[prefix + x + '.png' for x in crop],
                     against_C=against_C, against_H=against_H, marked_in_H=marked_in_H))

row('D01', 'opening A in F minus G', r'\unsure{F|\mathcal F}', 'F',
    r'\unsure{F|\mathcal F}',
    'Upright with two right arms and a loop returning down its left. Plain F is preferred, but intentional calligraphic styling is not fully decidable.',
    'medium', 'C doubt retained; alphabet', ['first_F'], False, False)
row('D02', 'crossed first Reste', r'\deleted{\unsure{Reste}}', r'\struck{Reste}',
    r'\deleted{Reste}', 'Tall R, low following run, and terminal e remain under a horizontal deletion. The succeeding live reste is separate.',
    'high', 'C doubt resolved', ['top'], True, False)
row('D03', 'live opening continuation', 'reste à voir que une strate', "Reste : voir qu'une strate",
    'reste à voir que une strate',
    'Lowercase initial r; the short accented a before voir is a letter, not a colon. The que group and une are separately spaced.',
    'high', 'H wording and punctuation', ['top'], False, True)
row('D04', 'raised glyph between strate and de F', r'\inserted{\unsure{$G$|$\in$}}', r'\add{de $G$}',
    r'\inserted{\unsure{$G$|$\in$}}',
    'A small rounded G/epsilon-shaped glyph has an inward horizontal and a short right descent. Its upper stroke meets the tail of réunion above. There is no separate de in the insertion.',
    'low', 'C doubt retained; H added word', ['insert_G'], False, True)
row('D05', 'crossed fragment after Soit A cette strate de F', r'\deleted{\unsure{On}}', r'\struck{On}',
    r'\deleted{\unsure{On}}',
    'Round opening loop with a low terminal stroke survives the two horizontal strokes; On remains plausible but the middle is obscured.',
    'medium', 'C doubt retained', ['top'], False, False)
row('D06', 'cancelled union, both lower-limit lines', r'B\in F; B\leq F', r'B\in F; B\leq F',
    r'B\in F; B\leq F',
    'The lower terminal letter has a shaft and two right arms, matching the F directly above. The two-part less-or-equal sign is visible; the upper B bears a small open ring.',
    'high', 'C notation/slip review', ['top_formula'], False, False)
row('D07', 'first case, after Si', r'A\notin G\prime', r'A\notin G', r'A\notin G\prime',
    'A detached short high stroke stands immediately to the right of G; no adjoining word or descender explains it away.',
    'high', 'H missing prime', ['top_formula'], False, True)
row('D08', 'same case, after alors', r'A\in F\setminus G\prime\subset F\prime', r'A\in F\setminus G\subset F\prime',
    r'A\in F\setminus G\prime\subset F\prime',
    'The second G also has a detached high prime. The following inclusion is open to the right and F has its own prime.',
    'high', 'H missing prime', ['top_formula'], False, True)
row('D09', 'second case and its conclusion', 'Si A in G ... et on gagne encore', 'Si A in G ... et on a gagné encore',
    'Si A in G ... et on gagne encore',
    'Second-case G is unprimed. In the final line, et and on precede gagne; there is no separate a, and the final e of gagne is not an accented past participle.',
    'high', 'H wording; C notation review', ['top_formula'], False, True)
row('D10', 'slanted note beside Corollaire', r'\unsure{Ultra} faux', 'Ultra faux', 'Ultra faux',
    'After clockwise rotation the tall U-l-t run and small ra are distinct. The nearby curved mark below faux belongs to the beginning of Corollaire, not punctuation added to this note.',
    'high', 'C doubt resolved', ['ultra', 'ultra_context'], True, False)
row('D11', 'article after Corollaire', r'\unsure{Le|La}', 'La', 'Le',
    'The small second letter has an open e-like angle and horizontal exit, without the round body of the adjacent a forms.',
    'high', 'C doubt resolved; H article', ['article'], True, True)
row('D12', 'corollary, before des propriétés', r'\inserted{chacune} des', r'\add{des}',
    r'\inserted{chacune} des',
    'Chacune is above the line with a long insertion curve into the point before the existing des. Des itself remains on the original baseline.',
    'high', 'H omission and insertion placement', ['article', 'corollary'], False, True)
row('D13', 'a), qui before G prime sur G', 'qui induit', 'qui induise', 'qui induit',
    'After the dotted i there is a separated terminal t-like upright and horizontal exit. No final se group is visible.',
    'high', 'H word ending', ['a_induit'], False, True)
row('D14', 'a), inserted replacement of maximal', r'\unsure{élémt|élément|élt}', 'élément',
    r'\unsure{élémt|élément|élt}',
    'The short word after grand has an initial e, tall l, reduced middle, and raised final stroke. The deletion diagonal crosses its end, preventing a reliable decision between abbreviated and full forms.',
    'medium', 'C doubt retained; possible H expansion', ['a_insert'], False, True)
row('D15', 'headings and maximal underlining', r'\uline{Corollaire}; \deleted{\uline{maximal}}; \uline{Dém}',
    r'\textbf{Corollaire}; \struck{maximal}; \textbf{Dém.}',
    r'\uline{Corollaire}; \deleted{\uline{maximal}}; \uline{Dém}',
    'Separate horizontal underlines stand below the two headings and below the locally cancelled maximal. The large X cancels all of a), including its replacement phrase.',
    'high', 'H state/formatting; whole-a cancellation review', ['corollary', 'a_insert', 'proof_On'], False, True)
row('D16', 'small mark immediately beneath qui in last long line of a)', 'omitted', 'omitted',
    'Separate angular E/in-like mark, reproduced in TikZ without choosing a lexical function.',
    'A nearly vertical left stroke joins a heavy lower arm; a shorter middle arm and a faint upper curved arm sit above it. It is separate from q’s descender and lies in the globally cancelled block.',
    'low', 'omission in both witnesses; unidentified graphical mark', ['a_angular'], True, True)
row('D17', 'starred note, after first equals sign', r'\unsure{parmi|pour}', 'pour', 'parmi',
    'A p descender is followed by a long middle run and a distinct terminal dotted i, favouring parmi over pour.',
    'high', 'C doubt resolved; H word', ['star_margin'], True, True)
row('D18', 'remaining starred note wording and literal marks', "cela revient au = ... d'une = F",
    "il revient au même ... d'un même F", "cela revient au = ... d'une = F",
    'The first word contains a c-like opening and l loop. Two pairs of parallel strokes are drawn literally after au and after d’une; neither position contains the written word même.',
    'high', 'H wording and expanded ditto marks', ['star_margin'], False, True)
row('D19', 'long oblique note, cancelled item before b)', r'\deleted{\unsure{a)}}', 'omitted',
    r'\deleted{\unsure{a)}}',
    'A heavily struck small form precedes the clear b), c), d) run. A curved closing stroke remains, but the character inside is mostly overwritten.',
    'low', 'C doubt retained; H omission', ['long_upper'], False, True)
row('D20', 'long oblique note, conjunction before impliquées', r'\unsure{et}', r'\uncertain{et ...}',
    r'\unsure{et}',
    'A short looped cluster and taller terminal stroke can be et; local retracing obscures the interior. No confident separate extra word can be extracted.',
    'low', 'C doubt retained', ['long_upper', 'note_clause'], False, False, True)
row('D21', 'long oblique note, underlined word and next preposition', r'\uline{\unsure{impliquées}} par a)',
    r'\uncertain{équivalentes à a)}', r'\uline{impliquées} par a)',
    'The word has a long p-like loop, an l upright, and q descender, followed by the short par group. A distinct underline follows its base.',
    'high', 'C doubt resolved; H mathematical wording', ['long_upper', 'note_clause'], True, True, True)
row('D22', 'long oblique note, relative word after a)', r'\unsure{lesquelles|laquelle}', r'\uncertain{lesquelles}',
    r'\unsure{lesquelles|laquelle}',
    'Initial le/la is compressed; a long q descent and two l loops follow. The terminal plural-like stroke is not completely separable from the crowded line.',
    'medium', 'C doubt retained', ['note_clause'], False, False, True)
row('D23', 'long oblique note, next verb', r'\unsure{caractérisent|caractérise}', r'conditions \ill{}',
    r'\unsure{caractérisent|caractérise}',
    'The opening c-a/r run and later tall t resemble caractérisée in the heading; the ending intersects the upright main text. A singular/plural ending remains undecided.',
    'medium', 'C doubt retained; H wording/lacuna', ['note_clause', 'long_upper'], False, True, True)
row('D24', 'long oblique note, after construite', r'\unsure{précédemment}', r'construite${}^{\#}$',
    r'\unsure{précédemm\textsuperscript{t}|précédemment}',
    'The beginning pré-cé-de and long reduced m run are visible. The final crossed t is raised; an abbreviated précédemm-t is possible and preferable to silently expanding that ending.',
    'medium', 'C doubt refined; H omitted word/misattached raised mark', ['long_lower', 'note_end'], True, True)
row('D25', 'long oblique note, abbreviated noun after trois', r'\unsure{cond.}', r'\ill{}',
    r'\unsure{cond.}',
    'Short rounded opening followed by reduced strokes and a tall ending; the small final dot is faint. The word overlaps neighbouring upright ink.',
    'medium', 'C doubt retained; H lacuna', ['long_margin', 'note_end'], False, True, True)
row('D26', 'long oblique note, before d’impliquer', r'\unsure{loin}', r'\ill{}',
    r'\unsure{loin}',
    'The reduced group is crossed by main-text strokes. Loin remains only a low-confidence reading; the following d’impliquer a) is clearer.',
    'low', 'C doubt retained; H lacuna', ['long_margin', 'note_end'], False, True, True)
row('D27', 'long oblique note, remaining words and order',
    'la subdivision construite ... Mais ces trois ... (b,c,d) sont ... d’impliquer a)',
    r'\ill{} subdivision construite ... Mais c) très \ill{} (b,c,d) \ill{}',
    'la subdivision construite ... Mais ces trois ... (b,c,d) sont ... d’impliquer a)',
    'La has an initial high loop; subdivision and construite are legible along the oblique baseline. Mais, ces, trois and the parenthesized three labels continue in that direction; the main upright c) must not be absorbed into this note.',
    'medium', 'H omitted/misread words and line assignment', ['long_margin', 'long_lower', 'note_end'], False, True, True)
row('D28', 'long curved stroke through the oblique note', 'note live; curve not encoded',
    'note live; editorial note says coupée d’un trait courbe',
    'Tentative whole-note cancellation, all wording retained; state explicitly uncertain.',
    'The long curved stroke passes through successive words rather than along an outer boundary, from conditions through équivalentes/impliquées and the later subdivision/précédemment lines. It may be a cancellation; a non-cancelling review stroke remains possible.',
    'medium', 'uncertain deletion state differing from both', ['long_margin'], True, True)
row('D29', 'b), after application', r'\unsure{can.}', r'\uncertain{canonique}', 'can.',
    'Only a short c-a-n group and a separate dot are present; no remaining canonique letters follow.',
    'high', 'C doubt resolved; H expansion', ['b'], True, True, True)
row('D30', 'right NB abbreviation', r'\unsure{tjrs|tojrs}', 'toujours', r'\unsure{tjrs|tojrs}',
    'Tight initial t-like group, long j descender and final r/s strokes; an additional small o loop is not securely separable.',
    'low', 'C doubt retained; H expansion', ['nb'], False, True)
row('D31', 'NB ending, emphasis and bracket', r"l'\uline{injectivité} qu'il faut prouver ici", "l'injectivité qu'il faut prouver",
    r"l'\uline{injectivité} qu'il faut prouver ici; left vertical bracket reproduced in TikZ",
    'Injectivité has a single underline; the final short ici group is visible at the right. A thin near-vertical bracket bounds the note on its left without crossing its words.',
    'high', 'H omission/emphasis; graphical grouping', ['nb', 'b'], True, True)
row('D32', 'c), long cancelled beginning and replacement',
    r'\deleted{Les strates ouvertes de F\prime qui ne sont}; live replacement',
    r'live phrase with two \struck{\ill{}} fragments, ouverte not transcribed',
    r'\deleted{Les strates ouvertes de F\prime qui ne sont}; above-line insertion forall A in F minus G, A-circle est une strate ouverte; live continuation de F\prime',
    'One long line cancels the original Les strates ... qui ne sont. The universal statement is placed above it, with ouverte visibly present; de F-prime continues below on the left.',
    'high', 'H wording and deletion extent; insertion state added to C', ['c_d'], True, True, True)
row('D33', 'Dém, C’s first supposedly deleted On', r'\deleted{\unsure{On}}', 'absent', 'No separate deleted On',
    'There is one O-to-n sequence. The tall opening stroke intersects Dém’s underline; no second O or independent crossed word is visible. Two tiny marks before va do not form On.',
    'high', 'C doubt rejected; duplicated word removed', ['proof_On'], True, False)
row('D34', 'Dém, live On', r'\unsure{On}', 'On', 'On',
    'A large open initial loop joins a dark n on one baseline. Its stroke meeting the underline belongs to the same live word.',
    'high', 'C doubt resolved', ['proof_On'], True, False)
row('D35', 'proof heading, after prouver', r'\unsure{p. ex}', 'omitted', 'p. ex',
    'A long p descender, separate point, then the small e/x group are visible before the implication cycle.',
    'high', 'C doubt resolved; H omission', ['proof'], True, True)
row('D36', 'bottom, crossed second proof heading', r'\deleted{\uline{\unsure{Dém}}}', r'\struck{Dém.}',
    r'\deleted{\uline{Dém}}',
    'Tall D and following reduced ém survive the crossing strokes; a separate underline runs below the heading.',
    'high', 'C doubt resolved; H underline', ['bottom_overwrite'], True, True)
row('D37', 'bottom, underlying overwritten noun', r'\deleted{\unsure{identité}}', 'live identité',
    r'\deleted{\unsure{identité}}',
    'An older tall t-like stroke and faint final accent remain above the darker superposed word. Identité is plausible for the older layer but not fully recoverable.',
    'low', 'C doubt retained; H deletion/layer assignment', ['bottom_overwrite'], False, True)
row('D38', 'bottom, live replacement noun', r'\unsure{inclusion}', 'identité', 'inclusion',
    'The dark layer has an initial in, a tall l loop after c, and the low usion ending. The extra tall t belongs to the lighter overwritten layer.',
    'high', 'C doubt resolved; H live word', ['bottom_overwrite'], True, True)
row('D39', 'bottom, raised abbreviation before inclusion arrow', r'\unsure{can.}', 'car in added parenthesis', 'can.',
    'The small raised c-a-n group ends with a dot, immediately before the written F minus G arrow F.',
    'high', 'C doubt resolved; H expansion/misreading', ['bottom_overwrite'], True, True)
row('D40', 'bottom, parenthesis and inserted mapping',
    r'\deleted{(trivial)} \inserted{can. F\setminus G\hookrightarrow F}',
    r'\add{(car F\smallsetminus G\subset F)}',
    r'\deleted{(trivial)} \inserted{can. F\setminus G\hookrightarrow F}',
    'The baseline parenthesized trivial is crossed. Above it stands can. and a hooked right arrow with a shaft and head, not an inclusion relation inside a car parenthesis.',
    'high', 'H wording, arrow and revision state', ['bottom_overwrite'], False, True)
row('D41', 'all order/mapping signs and primes in a), b)',
    r'F\prime\prime, F\prime, \preceq^{*}, \varphi:F\prime\to F, F\prime\setminus G\prime\xrightarrow{\sim}F\setminus G',
    'same substantive signs', 'Retain C signs',
    'Two short strokes on F in a), one in b); left-pointing curved order sign with lower stroke; raised star call; rightward mapping arrows and elevated wave; all four terminal letters and primes read individually.',
    'high', 'C notation review', ['a', 'b', 'star_margin'], False, False)
row('D42', 'c), d), implication cycle, restriction and foot equality',
    r'A^\circ, F\prime\supset F\setminus G, d=>b=>c=>a=>d, \varphi\mid F\setminus G, F\setminus G=F\prime\setminus G\prime',
    'same substantive signs', 'Retain C signs',
    'Small open circle over A; single open-left superset; four double-shaft right arrows in the stated order; vertical restriction bar; two parallel equality bars and primes only on right-hand F and G.',
    'high', 'C notation review', ['c_d', 'proof', 'bottom'], False, False)

cd_specs = [
    ('CD01','first F','D01','retained'), ('CD02','deleted Reste','D02','resolved'),
    ('CD03','raised G/in','D04','retained'), ('CD04','top deleted On','D05','retained'),
    ('CD05','Ultra','D10','resolved'), ('CD06','Le/La','D11','resolved'),
    ('CD07','élémt','D14','retained'), ('CD08','parmi/pour','D17','resolved'),
    ('CD09','deleted a) in oblique note','D19','retained'), ('CD10','et','D20','retained'),
    ('CD11','impliquées','D21','resolved'), ('CD12','lesquelles/laquelle','D22','retained'),
    ('CD13','caractérisent/caractérise','D23','retained'), ('CD14','précédemment','D24','refined'),
    ('CD15','cond.','D25','retained'), ('CD16','loin','D26','retained'),
    ('CD17','can. in b)','D29','resolved'), ('CD18','tjrs/tojrs','D30','retained'),
    ('CD19','deleted On at proof heading','D33','rejected as separate occurrence'),
    ('CD20','live On at proof heading','D34','resolved'), ('CD21','p. ex','D35','resolved'),
    ('CD22','deleted Dém','D36','resolved'), ('CD23','underlying identité','D37','retained'),
    ('CD24','live inclusion','D38','resolved'), ('CD25','can. in bottom insertion','D39','resolved')
]
cd = [dict(id=i, occurrence=o, difference_id=d, status=s) for i,o,d,s in cd_specs]

inventory = []
def inv(element, kind, position, objects, **extra):
    inventory.append(dict(element=element, kind=kind, position=position,
                          first_words_or_objects=objects, sheet_kind='text',
                          hand='his hand', transcribed='yes', **extra))
inv('I01','page number','top centre','31')
inv('I02','body paragraph','top three lines','Si A in F minus G ... Soit A cette strate de F')
inv('I03','deletion','beginning second line','Reste')
inv('I04','insertion','above strate/de F','G/in-like glyph with insertion slash')
inv('I05','deletion','end third line','On, uncertain')
inv('I06','cancelled display','upper left','A = union B-circle; B in F, B <= F')
inv('I07','case paragraph','upper right and following lines','Si A notin G-prime ... et on gagne')
inv('I08','case paragraph','upper middle','Si A in G ... et on gagne encore')
inv('I09','slanted margin note','left beside corollary','Ultra faux')
inv('I10','underlined heading and body','upper middle','Corollaire Le ... propriétés équivalentes suivantes')
inv('I11','local deletion and replacement','heading line','raffinement / subdivision')
inv('I12','insertion with curve','above des propriétés','chacune')
inv('I13','whole cancelled condition','centre','a) Pour toute subdivision F-double-prime ... G-prime sur G; large X')
inv('I14','underlined local deletion','inside a)','maximal')
inv('I15','above-line replacement','inside a)','un plus grand élémt/élément/élt')
inv('I16','unidentified angular mark','below qui in a)','E/in-like mark; reproduced in TikZ', state='within globally cancelled a; no separate local cancellation')
inv('I17','star call and slanted note','left of a)','* ou pour <<, cela revient au = parmi des subdivisions d’une = F')
inv('I18','long slanted note','centre left, crossing into body','les conditions ... d’impliquer a)', state='whole-note cancellation tentatively proposed; state uncertain')
inv('I19','local cancelled label','start of long note list','a), uncertain, before b), c), d)')
inv('I20','underline','within long note','impliquées')
inv('I21','long review/cancellation stroke','through long oblique note','curved stroke through successive words', state='uncertain cancellation')
inv('I22','condition paragraph','lower middle','b) L’application can. associée à F-prime preceq F')
inv('I23','displayed mapping','below b heading','phi: F-prime -> F')
inv('I24','bridge prose and displayed bijection','below mapping','induit une bijection; F-prime minus G-prime ~-> F minus G')
inv('I25','margin note','right of bijection','NB. c’est tjrs/tojrs surj. donc ... prouver ici')
inv('I26','underline and graphical bracket','NB','injectivité underlined; thin vertical left bracket, reproduced in TikZ')
inv('I27','cancelled line','condition c)','Les strates ouvertes de F-prime qui ne sont')
inv('I28','replacement insertion','above cancelled c line','forall A in F minus G, A-circle est une strate ouverte')
inv('I29','live continuation','left below c line','de F-prime')
inv('I30','condition paragraph','lower part','d) F-prime superset F minus G, i.e. forall A ... A in F-prime')
inv('I31','underlined proof heading and text','foot','Dém; one live On va prouver p. ex')
inv('I32','implication display','foot','d) => b) => c) => a) => d)')
inv('I33','cancelled underlined heading','bottom left','Dém')
inv('I34','proof paragraph','bottom','d) => b) Si ... restriction phi ... il reste à prouver')
inv('I35','overwriting layers','bottom noun','underlying identité uncertain; live inclusion')
inv('I36','cancelled parenthesis','bottom','(trivial)')
inv('I37','raised insertion','above parenthesis','can. F minus G hook-arrow F')
inv('I38','cancelled and live repeated word','bottom','donc / donc')
inv('I39','displayed equality','bottom edge','F minus G = F-prime minus G-prime')
inv('I40','tiny nonlexical marks','between On and va','two small pen marks; not a second On', state='recorded, not assigned invented text')
inventory[-1]['transcribed'] = 'recorded in a source-position comment; not assigned lexical text'

recipes = json.loads((base/'crops/R1/scan032_recipes.json').read_text())
tex = (out/'scan032.tex').read_text()
Ctex = (base/'source/SP34_CW_156-5_witnesses/codex/J156-5-04/pages/J156-5-04_156-5_scan032.tex').read_text()
source_unsure_count = Ctex.count('\\unsure{')
assert source_unsure_count == 25
assert len(cd) == source_unsure_count
assert len({r['id'] for r in rows}) == len(rows)
assert all((base/p).exists() for r in rows for p in r['crop'])

# Mechanical syntax checks only; this is not a LaTeX compilation or a proof check.
depth = 0
min_depth = 0
for c in tex:
    if c == '{': depth += 1
    if c == '}': depth -= 1
    min_depth = min(min_depth, depth)
env_begin = re.findall(r'\\begin\{([^}]+)\}',tex)
env_end = re.findall(r'\\end\{([^}]+)\}',tex)
syntax = dict(brace_balance=depth, minimum_brace_depth=min_depth,
              dollar_count=tex.count('$'), dollar_count_even=tex.count('$') % 2 == 0,
              display_opens=tex.count('\\['), display_closes=tex.count('\\]'),
              environments_begin=env_begin, environments_end=env_end,
              compiled=False, scope='Mechanical delimiter/environment review only')
assert depth == 0 and min_depth == 0
assert syntax['dollar_count_even']
assert syntax['display_opens'] == syntax['display_closes']
assert sorted(env_begin) == sorted(env_end)

now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
run = 'R1-scan032-20261119T215945Z'
model = 'GPT-6 Astra Pro'
effort = 'inherited; not separately exposed'
report = dict(
    scan=32, manuscript_page=31, reader='R1', model=model, effort=effort, run=run,
    start_utc='2026-11-19 21:59:45 UTC', end_utc=now,
    images_viewed=[
        'source/SP34_CW_156-5_scans/J156-5-04_156-5_scan032.jpg',
        'source/SP34_CW_156-5_scans/J156-5-04_156-5_scan032_a.jpg',
        'source/SP34_CW_156-5_scans/J156-5-04_156-5_scan032_b.jpg',
    ] + [r['file'] for r in recipes],
    viewing_order='Whole first, then half a, then half b; then all listed enlargements. Whole revisited for annotation positions. The first combined crop-view call was truncated; every affected crop was subsequently emitted and viewed again.',
    crops=recipes, differences=rows, C_doubt_resolutions=cd,
    C_doubt_coverage=dict(in_place_occurrences=25, reviewed=25,
                         additional_notation_and_slip_rows=['D06','D07','D08','D09','D18','D41','D42']),
    S_decisions=[],
    S_coverage=dict(source='source/SP34_CW_156-5_sweep3/readings/156-5_CORRECTIONS.tsv',
                    applicable_rows=0, decision='No S correction row for scan032; no S proposal imported.'),
    inventory=inventory,
    remaining_doubts=[
        dict(difference_id=r['id'], place=r['place'], reading=r['reading'], confidence=r['confidence'])
        for r in rows if r['id'] in ['D01','D04','D05','D14','D16','D19','D20','D22','D23','D24','D25','D26','D28','D30','D37']
    ],
    notation=[
        dict(place='opening and cancelled union', reading=r'\unsure{F|\mathcal F}; B\in F; B\leq F', decision='Alphabet doubt retained only at first occurrence; lower-limit F retained without mathematical repair.'),
        dict(place='two upper cases', reading=r'A\notin G\prime; A\in F\setminus G\prime\subset F\prime; A\in G; G\prime\preceq G', decision='Both first-case primes are ink; second-case unprimed G is also ink. No case repaired.'),
        dict(place='a, b and starred note', reading=r'F\prime\prime, F\prime, \preceq^{*}, \ll, =, =', decision='Prime counts, star call, paired left wedges and two literal equals/ditto marks preserved.'),
        dict(place='b, c, d and foot', reading=r'\varphi, \xrightarrow{\sim}, A^\circ, \supset, \Longrightarrow, \mid, \hookrightarrow, =', decision='Directions, circle, restriction and hooked arrow independently inspected; no added lower bar on d’s superset.'),
    ],
    notes=[
        dict(id='N032-1', type='reading note', text='Opening argument continues with reste à voir and two cases. The prime discrepancy is transcribed, not silently repaired.'),
        dict(id='N032-2', type='reading note', text='Ultra faux stands beside the corollary; condition a is globally crossed. The oblique note discusses b,c,d and a; its full reading and the uncertain cancellation state are preserved.'),
        dict(id='N032-3', type='reading note', text='NB says that injectivity is what must be proved ici. No proof of that general assertion was supplied by this reader.'),
        dict(id='N032-4', type='reading note', text='At the foot the author writes On va prouver p. ex, gives the four-arrow cycle, begins d=>b, and leaves the set equality as a goal with il reste à prouver.'),
        dict(id='N032-5', type='scope note', text='No later scan was opened. No root decisions, other-reader outputs or crops were consulted. Reading wording, counting signs and inspecting revision strokes are not called proof checks.'),
    ],
    checks=[dict(
        statement_id='R1-032-CHECK-1', place='bottom reduction of d=>b', date_utc=now,
        model=model, effort=effort, run=run, type='targeted proof check',
        statement='Conditional sufficiency of the displayed set equality for the desired bijection, assuming phi fixes the common elements of F and F-prime.',
        outcome='Passed as a conditional set-theoretic implication only.',
        reasoning='If F-prime minus G-prime equals F minus G, and phi restricted to F minus G is the canonical inclusion into F, then its restriction with codomain F minus G is the identity on that set. The identity has itself as inverse, so the displayed map is a bijection.',
        limits='The displayed set equality and the hypothesis that the canonical map fixes common elements were not proved here. No proof of the corollary, equivalence of b/c/d, or the asserted relation to a was performed.'
    )],
    reading_coverage=dict(whole=True, both_halves=True, all_lines=True,
                          all_C_doubts=True, all_C_H_differences_reviewed=True,
                          slanted_notes_rotated=True, no_OCR=True,
                          every_listed_crop_actually_viewed=True,
                          no_later_page=True, independent_of_other_readers=True),
    proposed_tex='out/readers/R1/scan032.tex', syntax_check=syntax)
(out/'scan032.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
(out/'scan032_crops.json').write_text(json.dumps(recipes, ensure_ascii=False, indent=2)+'\n')
print(json.dumps(dict(saved='out/readers/R1/scan032.json', differences=len(rows),
                      C_doubts=len(cd), inventory=len(inventory), crops=len(recipes),
                      checks=len(report['checks']), end_utc=now, syntax=syntax), ensure_ascii=False))
