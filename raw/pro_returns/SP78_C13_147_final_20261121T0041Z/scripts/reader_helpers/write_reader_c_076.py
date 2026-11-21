from pathlib import Path
import json
from datetime import datetime, timezone

ROOT = Path('/workspace/scratch/ea90d891106a')
WORK = ROOT / 'SP78_C13_147_work'
OUT = WORK / 'reader_returns/147_scan076'
OUT.mkdir(parents=True, exist_ok=True)
boxes = {int(k): v for k, v in json.loads((ROOT / 'runtime/reader_c_076_crops.json').read_text()).items()}

qopen = chr(96) * 2
qclose = "''"
quoted_an = qopen + 'an' + qclose
quoted_analytique = qopen + 'analytique' + qclose
quoted_grosse = qopen + 'grosse' + qclose

# The extra ink is represented graphically: neither a buried letter nor a
# semantic decoration is supplied.  Only the extra trace is uncertain.
g_trace = r'''\begin{tikzpicture}[baseline=(g.base),x=1ex,y=1ex]
\node[inner sep=0pt,outer sep=0pt] (g) at (0,0) {$\scriptstyle\underline G$};
\node[inner sep=0pt,outer sep=0pt,anchor=south] at (-0.08,0.25) {$\unsure{\begin{tikzpicture}[x=0.65ex,y=0.65ex,baseline=0pt]
\draw[line width=0.28pt] (0,0) -- (-0.11,1.18);
\draw[line width=0.28pt] (-0.04,0.59) -- (0.24,0.92);
\end{tikzpicture}}$};
\end{tikzpicture}'''
overworked_formula = r'\Pi M_{' + g_trace + '}'

low_trace = r'''\begin{tikzpicture}[x=1em,y=1em,baseline=0pt]
\draw[line width=0.4pt] (0,0) -- (4.0,0.34);
\draw[line width=0.3pt] (0.16,0.015) -- (0.20,0.12) -- (0.25,0.10) -- (0.21,0.02)
 -- (0.35,0.04) .. controls (0.48,0.10) and (0.53,-0.04) .. (0.68,0.035)
 .. controls (0.59,0.12) and (0.51,0.08) .. (0.50,0.045);
\draw[line width=0.3pt] (0.92,0.08) -- (0.94,0.15) -- (0.99,0.08)
 -- (1.14,0.10) -- (1.16,0.18) -- (1.20,0.11) -- (1.56,0.13);
\draw[line width=0.3pt] (1.86,0.16) .. controls (1.88,0.26) and (1.90,0.14) .. (1.98,0.18)
 -- (2.10,0.20) -- (2.12,0.29) -- (2.17,0.20) -- (2.44,0.22);
\draw[line width=0.3pt] (2.76,0.24) -- (2.79,0.31) -- (2.85,0.25) -- (3.19,0.28);
\draw[line width=0.3pt] (3.73,0.32) -- (3.80,0.25) -- (3.76,0.19);
\end{tikzpicture}'''
live_group_with_trace = r'$\underset{\unsure{' + low_trace + r'}}{\text{le groupe}}$'

abbr = r'\unsure{canoniq\textsuperscript{t}}'
heading = r'''\mspage{37}
9) \uline{La structure groupoïdale des} \inserted{\uline{espaces modulaires de}} \uline{Teichmuller} \uline{modules}'''
subtitle = '(la MDT-structure) : cas transcendant, morphismes de générisation.'
analytic = (r'Nous travaillons maintenant avec les $M^{\mathrm{an}}_{g,\nu}$, '
            r'$\widehat M^{\mathrm{an}}_{g,\nu}$ etc -- et pour ne pas traîner les exposants '
            + quoted_an + ' (pour ' + quoted_analytique + '), nous les faisons tomber.')
upper = (r'et son groupoïde fondamental, que je note $\Pi M_{\underline G}$. '
         r"C'est une \inserted{" + quoted_grosse + r'} catégorie, par la suite nous allons voir comment la remplacer '
         r'\inserted{' + abbr + r"} par une \deleted{catégorie} \inserted{groupoïde} dont l'ens des")
middle = 'objets soit fini. Dans nos constructions, il est en effet licite de remplacer un'
lower = ('groupoïde tel que $' + overworked_formula + r'$ par un groupoïde équivalent, pourvu que '
         r"\deleted{l'équivalence} \inserted{dans celui-ci}")
display = r'''\[
(94)\qquad \Gamma_{\underline G}=\operatorname{Aut}\underline G
\]'''
after = "opère, et que l'équivalence commute à l'action de ce groupe."
last = r'Notons déjà que $\Pi M_{\underline G}$ est un groupoïde'

proposed = (r'\scanpage{76}' + '\n' + heading + ' ' + subtitle + '\n\n' + analytic + '\n\n'
            + r'Considérons pour tout MD-graphe $\underline G$, la multiplicité modulaire (analytique) $M_{\underline G}$, '
            + upper + ' ' + middle + ' ' + lower + ' ' + live_group_with_trace + '\n' + display + '\n'
            + after + '\n\n' + last + '\n' + r'\margin{75}' + '\n')
(OUT / 'proposed.tex').write_text(proposed, encoding='utf-8')

changes = []
def ch(place, C, H, final, evidence, crop, *, confidence='high', against_C=False,
       against_H=True, kind='misread word', marked_in_H=False,
       error_sheet_kind='words', consequential=False):
    changes.append(dict(id=f'076-{len(changes)+1:02d}', place=place, C=C, H=H, final=final,
                        evidence=evidence, crop=f'147_scan076_place{crop:02d}.png', box=boxes[crop],
                        confidence=confidence, against_C=against_C, against_H=against_H,
                        kind=kind, marked_in_H=marked_in_H, error_sheet_kind=error_sheet_kind,
                        consequential=consequential))

ch('Heading: words in the supralinear insertion', 'espaces modulaires de',
   r'\uncertain{groupes} \uncertain{modulaires} \uncertain{des}', 'espaces modulaires de',
   'The first word has the low e/s opening and a p descender followed by aces; it does not begin with a g loop. The last word is the short looped d plus e, without a separate terminal s.', 1,
   marked_in_H=True)
ch('Heading: attachment of the supralinear insertion',
   r'des \inserted{\uline{espaces modulaires de}} Teichmüller',
   r'Teichmüller modulaires (\add{groupes modulaires des})',
   r'des \inserted{\uline{espaces modulaires de}} \uline{Teichmuller}',
   'The insertion is above the name and its curved connector descends into the gap immediately after des, before the initial T. No pair of parentheses encloses the inserted words.', 1,
   kind='insertion or placement', marked_in_H=True, error_sheet_kind='insertions put in wrong place')
ch('Heading: spelling of the proper name', 'Teichmüller', 'Teichmüller', 'Teichmuller',
   'There are no detached umlaut dots above the u. The two high following strokes are the two l ascenders, while the continuous higher stroke belongs to the underlined insertion. The exposed space above the u is blank.', 1,
   against_C=True, kind='abbreviation expanded or spelling modernised',
   error_sheet_kind='abbreviations expanded spelling modernised')
ch('Heading: final underlined noun, M1068', r'\unsure{modules|variétés}', 'modulaires', 'modules',
   'The short word has an m/o run, the short separated d ascender, and a final u-l-e-s run. It has neither the long -aires ending of modulaires nor the initial v and internal t of variétés.', 1)
ch('Heading continuation: punctuation around the subject line',
   'cas transcendant, morphismes de générisation.',
   'cas transcendant (morphismes de généralisation.)',
   'cas transcendant, morphismes de générisation.',
   'A comma follows transcendant at the right end of the first continuation line. The next line begins directly with morphismes and ends with a point; there is no opening or closing parenthesis around that line.', 2,
   kind='other', error_sheet_kind='other')
ch('Heading continuation: final technical word', 'générisation', 'généralisation', 'générisation',
   'After génér the small i stroke and s run follow directly. There is no a/l pair or tall l ascender before the -isation ending.', 2)
ch('Analytic-notation paragraph: abbreviation punctuation', 'etc --', 'etc. --', 'etc --',
   'The abbreviated etc is followed by the long dash strokes. No separate dark period appears between c and the dash.', 3,
   kind='abbreviation expanded or spelling modernised', error_sheet_kind='abbreviations expanded spelling modernised')
ch('Analytic-notation paragraph: quotation marks around an', quoted_an, r'\og an\fg{}', quoted_an,
   'The opening and closing marks are small paired quotation strokes above the word, not lateral guillemet chevrons.', 4,
   kind='other', error_sheet_kind='other')
ch('Analytic-notation paragraph: quotation marks around analytique', quoted_analytique,
   r'\og analytique\fg{}', quoted_analytique,
   'The longer quoted word likewise has paired upper quotation strokes at both ends. The enclosing parentheses and following comma remain separate.', 4,
   kind='other', error_sheet_kind='other')
ch('Analytic-notation paragraph: final verb', 'faisons', 'laisserons', 'faisons',
   'The word begins with the large looped f and has the short a/i group with its dot, followed by sons. It lacks the longer -sser- group required by laisserons.', 4)
ch('First category sentence: quoted supralinear adjective', r'\inserted{' + quoted_grosse + '}',
   r'\og \add{\uncertain{grosse}}\fg{}', r'\inserted{' + quoted_grosse + '}',
   'Both paired quotation groups stand on the same raised line as grosse. They are part of that inserted phrase, not baseline guillemets outside the insertion.', 6,
   kind='insertion or placement', marked_in_H=True, error_sheet_kind='insertions put in wrong place')
ch('First category sentence: state of catégorie', 'catégorie', r'\struck{catégorie}', 'catégorie',
   'The curved connector from the raised grosse enters the gap before catégorie and crosses the tall t area. It does not run horizontally through the bodies of the word. The first catégorie is live.', 6,
   kind='deletion state', error_sheet_kind='struck text')
ch('First category sentence: end of the note baseline', 'par la', 'par le', 'par la',
   'After the tall l, the short terminal form has the low closed/returning a form of the adjacent la occurrences; the following baseline begins suite.', 6)
ch('Promise of a later replacement: full clause', 'suite nous allons voir comment la',
   r"fait même \uncertain{qu'elle} est \uncertain{connexe} \uncertain{gouverne} le",
   'suite nous allons voir comment la',
   'The baseline opens with suite (including the tall t), then the short nous run, two tall l strokes in allons, the compact voir with its i dot, comment, and a final looped la. There are no additional words between these visible groups.', 7,
   marked_in_H=True)
ch('After remplacer: inserted abbreviated adverb, M1069', r'\inserted{\unsure{canoniqt}}',
   '(nothing)', r'\inserted{' + abbr + '}',
   'A distinct raised insertion with its own connector follows remplacer. The canoniq prefix and long q descender are visible. A very small raised terminal loop/stroke is compatible with t but remains doubtful; the abbreviation is not expanded.', 7,
   confidence='medium', against_C=True, kind='omission', error_sheet_kind='omissions')
ch('Before the canceled second catégorie: literal article', 'par une', 'par un', 'par une',
   'The article has three successive low humps/returns, including the final e, matching the earlier une. The feminine article survives the replacement of catégorie by groupoïde.', 7)
ch('After dont: abbreviated noun', "l'ens", "l'ensemble", "l'ens",
   'The word stops after the short e-n-s run. There is no -emble continuation and no detached period after s.', 7,
   kind='abbreviation expanded or spelling modernised', error_sheet_kind='abbreviations expanded spelling modernised')
ch('Construction paragraph: en effet', 'en effet', 'en fait', 'en effet',
   'The word begins with the low e and has two adjacent tall f strokes before the final e/t run; it is longer than fait and has no a body.', 8)
ch('Construction paragraph: article after remplacer', 'remplacer un', 'remplacer', 'remplacer un',
   'At the right end of the baseline, after remplacer, a separate two-hump un is written. It precedes groupoïde on the next physical line.', 8,
   kind='omission', error_sheet_kind='omissions')
ch('Construction paragraph: order around the middle fundamental-groupoid expression',
   r'groupoïde tel que $\Pi M_{\underline G}$ par un',
   r'$\Pi M_{\underline G}$ par un groupoïde tel que',
   'groupoïde tel que $' + overworked_formula + '$ par un',
   'The physical line reads groupoïde, then the tall t/l of tel and the descending q of que, then the complete Pi-M expression, followed by par un. The groupoïde tel que group is before the expression, not after it.', 9,
   kind='insertion or placement', error_sheet_kind='insertions put in wrong place')
ch('Middle fundamental-groupoid expression: extra ink through the G',
   r'\Pi M_{\underline G}', r'\Pi M_{\underline G}', overworked_formula,
   'The G body and its separate underline remain legible. An extra upright extends above the body and has a short rising right-hand branch; it is not part of an ordinary clean G outline. The trace is retained graphically with its state uncertain, without supplying a buried symbol.', 9,
   confidence='medium', against_C=True, kind='omission', error_sheet_kind='symbols and indices')
ch('After pourvu que: the canceled words and their position', r"\deleted{l'équivalence}",
   r"\struck{\ill{}} here; \struck{l'équivalence} earlier before groupoïde équivalent",
   r"\deleted{l'équivalence}",
   'The independent straight strike crosses the words immediately after pourvu que. The l and apostrophe, e/q loop with its descender, internal u/i/v run, tall l, and -ence ending support l’équivalence. The struck span is not before groupoïde équivalent.', 10,
   kind=r'readable ink left as \ill{}', marked_in_H=True, error_sheet_kind='readable ink left as illegible')
ch('Replacement above the canceled l’équivalence', r'\inserted{dans celui-ci}',
   r'\add{des \uncertain{échantillons}} earlier in the sentence', r'\inserted{dans celui-ci}',
   'The upper run begins with a looped d and the low ans run, followed by celui with a tall l and the short hyphen-ci ending. It sits directly above the canceled l’équivalence and has no letters supporting échantillons.', 10,
   marked_in_H=True)
ch('Immediately before (94): live words', 'le groupe', 'editorial description: a line le groupe rayée',
   'le groupe',
   'The words stand above the low irregular line. Their e, g loop, and remaining letter bodies are not traversed by a cancellation stroke; only the p descender reaches the lower trace. The readable words remain live.', 11,
   kind='deletion state', error_sheet_kind='struck text')
ch('Immediately below live le groupe: unresolved lower stroke', '(nothing)',
   'described as a strike through le groupe', live_group_with_trace,
   'The low rising line starts before le and carries small loops, vertical hooks, and a right terminal hook along it. It may cross unreadable trial writing or be an irregular underline. The actual stroke pattern is retained below the live words, with no supplied underlying letters or word count.', 11,
   confidence='medium', against_C=True, kind='drawing or diagram', error_sheet_kind='drawings and diagrams')
ch('Immediately after (94): beginning of the continuation', 'opère, et que', '(nothing)',
   'opère, et que',
   'Below the display, opère has its p descender and final comma. The following et has a long descending flourish attached to its t; then a separate que follows. The flourish is not an extra word.', 13,
   kind='omission', error_sheet_kind='omissions')
ch('Action compatibility clause: position relative to (94)',
   "after (94): l'équivalence commute à l'action", "before (94): l'équivalence commute à l'action",
   "after (94): l'équivalence commute à l'action",
   'The complete l’équivalence commute à l’action clause is on the same physical baseline as opère, et que, below the display. It is not above (94) after pourvu que.', 13,
   kind='insertion or placement', error_sheet_kind='insertions put in wrong place')
ch('Action compatibility clause: last words and punctuation', 'de ce groupe.', r'\uncertain{du groupe}',
   'de ce groupe.',
   'The lower continuation has a separate looped de, a separate short ce, then groupe. A dark final point follows the word; there is no single du joining the first two groups.', 13,
   marked_in_H=True)
ch('Lower-left pencil foliation', r'\margin{75}', '(nothing)', r'\margin{75}',
   'The pale numeral has the long top and descending stroke of 7, then a separate 5 with its upper turn and lower bowl. It is pencil foliation, separate from the ink author page 37.', 15,
   kind='omission', error_sheet_kind='omissions')

decisions = [
    dict(id='M1068', cote=147, scan=76, decision='first', reading='modules',
         ink='Initial m/o run, a short separate d ascender, and the final u-l-e-s run decide modules; neither variétés nor modulaires fits the surviving strokes.',
         crop='147_scan076_place01.png (318,18,1648,152)', confidence='high'),
    dict(id='M1069', cote=147, scan=76, decision='undecided', reading=abbr,
         ink='The canoniq prefix and q descender are legible, but the tiny raised final loop/stroke does not securely settle the abbreviated ending. No full word is supplied.',
         crop='147_scan076_place07.png (267,1083,1641,1297)', confidence='medium')
]

inventory = []
def inv(kind, position, first, hand='his hand'):
    inventory.append(dict(scan=76, sheet_kind='text', hand=hand, element=f'{len(inventory)+1:02d}',
                          kind=kind, position=position, first_words_or_objects=first, transcribed='yes'))
inv('text', 'Upper centre, above the heading', r'\mspage{37}')
inv('text', 'First main baseline', r'9) \uline{La structure groupoïdale des} ... \uline{Teichmuller} \uline{modules}')
inv('insertion', 'Above Teichmuller, attached after des', r'\inserted{\uline{espaces modulaires de}}')
inv('text', 'Second and third heading baselines', subtitle)
inv('text', 'Four baselines of the first prose paragraph', analytic)
inv('text', 'First two baselines of the main paragraph', r'Considérons pour tout MD-graphe $\underline G$, la multiplicité modulaire (analytique) $M_{\underline G}$,')
inv('text', 'Next two main baselines', r"et son groupoïde fondamental ... note $\Pi M_{\underline G}$. C'est une ... catégorie, par la")
inv('insertion', 'Above the first live catégorie', r'\inserted{' + quoted_grosse + '}')
inv('text', 'Following suite and remplacer baselines', 'suite nous allons voir comment la remplacer ... par une ... dont l’ens des')
inv('insertion', 'Above the gap after remplacer', r'\inserted{' + abbr + '}')
inv('deletion', 'After literal par une', r'\deleted{catégorie}')
inv('insertion', 'Above the canceled second catégorie', r'\inserted{groupoïde}')
inv('text', 'Objects and construction baselines', middle)
inv('text', 'Middle groupoid baseline', 'groupoïde tel que $' + overworked_formula + '$ par un')
inv('deletion', 'Over the G in the middle Pi-M expression; cancellation state unresolved', 'Uncertain extra upright and short branch through the readable underlined G, retained as a TikZ trace')
inv('text', 'Next main baseline', 'groupoïde équivalent, pourvu que')
inv('deletion', 'Right end of that baseline', r"\deleted{l'équivalence}")
inv('insertion', 'Directly above that canceled span', r'\inserted{dans celui-ci}')
inv('text', 'Short isolated line before the display', 'le groupe')
inv('deletion', 'Below live le groupe; possible trial deletion versus irregular underline', 'Uncertain low rising line with loops and hooks, retained as a TikZ trace without underlying text')
inv('display', 'Single numbered display', display)
inv('text', 'Two baselines below the display', after)
inv('text', 'Final unfinished baseline', last)
inv('margin note', 'Lower-left pencil foliation', r'\margin{75}', hand='pencil hand not confidently attributed')

doubts = [
    dict(place='M1069, insertion after remplacer', reading=abbr,
         alternatives='canoniq with another abbreviated terminal stroke; no secure expansion in the transcription',
         confidence='medium', reason='The q descender is clear, but the very small raised endpoint is overcompressed and its t-like form is not decisive.'),
    dict(place='G in the middle fundamental-groupoid expression', reading=overworked_formula,
         alternatives='Extra upright/branch may be a canceled underlying trial or overworking of the G; no buried symbol is identified.',
         confidence='medium', reason='The independent upper upright and branch survive clearly, but their relation to the G body and deletion state cannot be separated. The ordinary G and underline remain readable.'),
    dict(place='Low trace below live le groupe', reading=live_group_with_trace,
         alternatives='A line crossing unreadable trial writing, or an irregular underline; le groupe remains live in either case.',
         confidence='low', reason='Small loops and hooks accompany the low stroke, but no underlying sequence of letters is securely recoverable. The stroke does not cross the live word bodies.')
]

notes = [
    'Physical coverage: 29 reading bands were inspected: 22 primary baselines (including the one display and the final unfinished line), four supralinear insertion bands (canoniqt and the replacement groupoïde share one band), the ink page number 37, the low trace below le groupe, and pencil foliation 75. The entire scan was viewed once for layout and both native-resolution halves once; all 15 saved crops were viewed. The two extra stroke traces are included in the transcription and inventory. No OCR, outside research, TeX compilation, or blind second reading was used.',
    'The manuscript heading announces the groupoidal structure of the Teichmuller modules/spaces, called the MDT-structure, in the transcendental case, and morphisms of générisation. The source spelling Teichmuller has no visible umlaut dots. Underlining belongs to the first heading line and its inserted espaces modulaires de, not to the two following title baselines. H’s bold/emphasis macro choices alone were not counted as changes.',
    'The author explicitly says that he is now working with the analytic objects M^{an}_{g,nu} and widehat M^{an}_{g,nu}, and drops the an superscripts to avoid carrying them. Both original formula groups, the hat on the second M only, and their g,nu indices were inspected. This is a stated notation convention, not a proof of a comparison theorem.',
    'For every MD-graph underlined G, the manuscript considers the analytic modular multiplicity M_G and its fundamental groupoid Pi M_G. It calls this a grosse category and promises later to replace it canoniqt by a groupoid with a finite object set. The first catégorie is live under an insertion connector. The second catégorie is canceled and replaced by groupoïde, while the literal article une survives. This report does not establish a canonical finite-object replacement or any topological finiteness assertion.',
    'The construction paragraph states that replacing a groupoid such as Pi M_G by an equivalent groupoid is licit provided Gamma_G = Aut G acts in the replacement and the equivalence commutes with the action. The phrase dans celui-ci replaces the canceled l’équivalence. Formula (94) and its two separate G underlines were read directly. The equivariance requirement and the claimed licitness of replacement are manuscript assertions carried as background here, not proved in this reading.',
    'Two pieces of extra ink omitted or misassigned by the witnesses remain unresolved. The middle Pi-M expression has an upright and short branch through the upper G body; the readable G and underline are preserved with a graphical trace, without interpreting the mark as a mathematical exponent or supplying a canceled letter. Beneath live le groupe, the low rising stroke has loops and hooks and may cross trial writing or serve as an irregular underline. It is likewise reproduced graphically without a guessed word count. The TikZ traces approximate visible stroke geometry and do not claim the recovery of underlying text.',
    'The last line begins Notons déjà que Pi M_G est un groupoïde and ends on this sheet without terminal punctuation or a completed assertion. No continuation from another page was consulted or supplied. The pale lower-left 75 is kept as separate pencil foliation, with its hand unattributed; 37 is the ink author page number.'
]

now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
check_events = [
    dict(statement_id='147-076-N3', date=now, who='reader_c, GPT-6 Astra Pro (effort setting not exposed)',
         type='carried as background without fault found',
         outcome='Checked the written convention against both analytic formula groups and the sentence dropping an. This checks transcription and local notation only; no analytic/algebraic comparison or equivalence was proved.'),
    dict(statement_id='147-076-N4', date=now, who='reader_c, GPT-6 Astra Pro (effort setting not exposed)',
         type='carried as background without fault found',
         outcome='Read the fundamental-groupoid construction and the promise of a later canonical replacement with finitely many objects. No construction, finiteness proof, or canonicity proof was performed, and these expectations did not resolve the doubtful abbreviation.'),
    dict(statement_id='147-076-N5', date=now, who='reader_c, GPT-6 Astra Pro (effort setting not exposed)',
         type='carried as background without fault found',
         outcome='Read Gamma_G = Aut G and the requirement that an equivalence commute with its action. Checked the words, their replacement/placement, the label 94, and underlines. No general equivariant replacement theorem or automorphism computation was proved.')
]

notation = [
    dict(sign=r'\Pi', reading='Capital Pi in fundamental-groupoid notation',
         evidence='All three Pi glyphs have a continuous top bar and two tall downstrokes, in the first definition, the middle replacement example, and the final line.', scope='All three occurrences on scan076.'),
    dict(sign=r'\underline G', reading='G with a separate underline',
         evidence='All seven G occurrences were checked: MD-graphe G, M_G, the first and middle Pi-M examples, both G glyphs in (94), and the final Pi-M expression. The extra upright/branch in the middle occurrence is retained separately.', scope='Seven local occurrences; no global rule that every G is underlined.'),
    dict(sign=r'\Gamma_{\underline G}=\operatorname{Aut}\underline G', reading='Formula (94)',
         evidence='Gamma has one upright and upper arm; the equality has two bars; Aut is written in full and both G letters have separate lower strokes.', scope='Only the numbered display on this page.'),
    dict(sign='Two small paired quote strokes', reading='TeX opening and closing double quotation marks',
         evidence='Both quoted analytic labels and the inserted grosse have paired upper ticks, not guillemets.', scope='Three quoted groups on scan076.'),
    dict(sign='canoniq with a tiny raised final stroke', reading=abbr,
         evidence='The long q descender and compact final loop are visible, but the ending is not securely resolved.', scope='The single inserted abbreviation on this page; no assumed expansion in the text.')
]

hand_log = [
    dict(habit='A curved insertion connector can cross a tall letter without deleting the word.', pages=[76],
         all_occurrences='Confirmed for the connector from grosse crossing the first catégorie. The second catégorie and l’équivalence instead have independent straight strikes through their word bodies.',
         witness_misreadings='H marks the first catégorie as struck.'),
    dict(habit='An isolated low line with hooks need not cancel the readable words above it.', pages=[76],
         all_occurrences='One unresolved occurrence below le groupe; this is an occurrence-specific warning, not a general rule about underlining.',
         witness_misreadings='H assigns the low line as cancellation of le groupe; C omits the extra stroke pattern.'),
    dict(habit='The final stroke of et can descend far below the baseline.', pages=[76],
         all_occurrences='The et immediately after opère has a long attached descending flourish. Other et groups do not all have that flourish.',
         witness_misreadings='H omits opère, et que; the flourish is not separately transcribed as a word.'),
    dict(habit='Short source abbreviations may have no final dot or only a tiny raised endpoint.', pages=[76],
         all_occurrences='etc and ens have no detached periods; canoniq has an uncertain raised final t-like stroke. These are separate locally inspected cases.',
         witness_misreadings='H adds a dot to etc, expands ens to ensemble, and omits the inserted abbreviated canoniqt.')
]

abbreviations = [
    dict(written='an', expansion='analytique; explicitly explained in the manuscript'),
    dict(written='etc', expansion='et cetera; no final dot is written here'),
    dict(written="ens", expansion='ensemble; expansion is not inserted in the transcription'),
    dict(written='canoniq with uncertain raised t-like endpoint', expansion='probably canoniquement; ending and expansion remain inferential and are not supplied in the transcription'),
    dict(written='Aut', expansion='automorphismes; preserved as the written mathematical operator')
]

second_boxes = []
def sb(kind, box, reading):
    second_boxes.append(dict(box=f'B{len(second_boxes)+1:02d}', kind=kind,
                             x0=box[0], y0=box[1], x1=box[2], y1=box[3], reading=reading))
sb('handwritten number', [318,18,1648,152], heading)
sb('word disagreement', [405,142,1674,281], subtitle)
sb('word disagreement', [280,286,1674,692], analytic)
sb('insertion', [260,905,1645,1278], upper)
sb('word disagreement', [260,1281,1650,1480], middle)
sb('doubtful formula', [260,1478,1689,1735], lower)
sb('non-high-confidence change', [265,1745,1125,1940], live_group_with_trace + '\n' + display)
sb('word disagreement', [280,1944,1689,2135], after)
sb('margin note', [18,2284,88,2345], r'\margin{75}')

report = dict(scan=76, reader='reader_c', physical_lines_read=29, changes=changes,
              decisions=decisions, inventory=inventory, doubts=doubts, notes=notes,
              check_events=check_events, notation=notation, hand_log=hand_log,
              abbreviations=abbreviations, second_boxes=second_boxes,
              unresolved=[
                  'M1069: the tiny raised final stroke of canoniqt remains doubtful.',
                  'Extra upright and branch through the middle G: overwork versus canceled underlying trial remains unresolved; no buried symbol supplied.',
                  'Low stroke below le groupe: canceled trial versus irregular underline remains unresolved; live words retained, no underlying text supplied.'
              ],
              witness_comparison='C follows the physical word order and most words closely, including faisons, the finite-object sentence, en effet, the lower construction, dans celui-ci, and the post-display clause. H is substantially less reliable in the title and middle/lower prose: it misplaces the title insertion, changes générisation, marks a live catégorie as struck, garbles the later-replacement clause, expands ens, and rearranges the construction around (94). Both witnesses normalize Teichmuller to Teichmüller and omit the extra overwork through the middle G. C also leaves out the low stroke pattern beneath le groupe; H misassigns its state to the live words. H’s editorial page descriptions and continuation note were not transcribed as manuscript text. Macro-only differences were excluded.')

(OUT / 'report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

# Structural and coverage checks, without rendering or compiling the TeX.
assert [d['id'] for d in decisions] == ['M1068', 'M1069']
for row in changes:
    assert (WORK / 'crops' / row['crop']).is_file(), row['id']
    assert row['box'] == boxes[int(row['crop'].split('place')[1].split('.')[0])]
for box in second_boxes:
    assert box['reading'] in proposed, box['box']
assert r'\margin{75}' in proposed and r'\mspage{37}' in proposed
assert proposed.count(r'\deleted{') == 2
assert proposed.count(r'\inserted{') == 5
assert proposed.count(r'\unsure{') == 3
assert len(list((WORK / 'crops').glob('147_scan076_place*.png'))) == 15
for event in check_events:
    n = int(event['statement_id'].rsplit('N',1)[1])
    assert 1 <= n <= len(notes)
print(json.dumps({'scan':76, 'physical_bands':29, 'crops':15, 'changes':len(changes),
                  'decisions':len(decisions), 'inventory':len(inventory), 'doubts':len(doubts),
                  'notes':len(notes), 'check_events':len(check_events), 'second_boxes':len(second_boxes)},
                 ensure_ascii=False))
