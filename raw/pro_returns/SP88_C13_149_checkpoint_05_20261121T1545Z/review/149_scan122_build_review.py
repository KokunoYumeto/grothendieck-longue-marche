from pathlib import Path
import json

ROOT = Path('/workspace/scratch/0cab6a548abb')
OUT = ROOT / 'edition/review'
PAGE = '149_scan122'

opening = r'''correspondent exactement (via $x\longmapsto\underline{O}_{\mathfrak X,x}$) aux jauges dans $L$ qui sont ent. de type fini sur $K$, de corps des fractions $L$ --- i.e. aux $V$ précédents.'''

second = r'''Sauf erreur, ces deux types de pts de $\mathfrak X$ (qui épuisent \deleted{tout} si $n=1$,\unsure{)} \inserted{qui est le seul cas, avec $n=0$, où $\mathfrak X$ \unsure{est|soit} un schéma !}) sont les seuls pour lesquels $\underline{O}_{\mathfrak X,x}$ soit noethérien. Cependant, on a'''

rule = r'''\margin{\begin{tikzpicture}[x=1mm,y=\baselineskip]
\draw[line width=0.3pt] (0,0) -- (0.06,-4.4) -- (-0.06,-4.7) -- (0.02,-4.9);
\end{tikzpicture}}'''

proposition = r'''\uline{Proposition} Pour $\forall x\in\mathfrak X$, $\underline{O}_{\mathfrak X,x}$ est un anneau de valuation dans $L$, de corps des fractions $L$, et contenant $K$. L'application $x\longmapsto\underline{O}_{\mathfrak X,x}$ est une bijection de $\mathfrak X$ sur l'ens de ces anneaux dans $L$.'''

margin = r'''\margin{On pourrait\newline partir d'un\newline schéma excellent\newline $X$, et construire\newline un $\mathfrak X$ relatif au\newline dessus\unsure{\ldots|..}}'''

proof = r'''\uline{Dém} a) Soit $f\in L\setminus\underline{O}_{\mathfrak X,x}$, il faut prouver $\frac1f\in\underline{O}_{\mathfrak X,x}$. Or $f=g/h$, \inserted{$g,h$}$\in\underline{O}_{X,a}$, où $X$ modèle \inserted{régulier} (propre), $a$ un pt, $f,g$ \deleted{\unsure{premiers} entre eux} --- utilisant la résolution, \deleted{\unsure{on} \uline{\unsure{sépare}} \unsure{les diviseurs}} \inserted{OPS $\exists$ système régulier} de paramètres, avec $f,g$ des monômes'''

folio = r'\margin{121}'
candidate = '\\scanpage{122}\n' + opening + '\n\n' + second + '\n\n' + rule + '\n' + proposition + '\n' + margin + '\n\n' + proof + '\n' + folio + '\n'
(OUT / f'{PAGE}.tex').write_text(candidate, encoding='utf-8')

geometry = json.loads((OUT / f'{PAGE}_crop_geometry.json').read_text(encoding='utf-8'))
G = {g['id']: g for g in geometry}

changes = []
def change(place, C, H, final, evidence, crop, confidence='high', vs_C=False,
           vs_H=True, kind='misread word', category='Words', H_marked=False,
           consequential=False, **extra):
    row = {'id': f'p{len(changes)+1:02d}', 'place': place, 'C': C, 'H': H,
           'final': final, 'evidence': evidence, 'crop': G[crop]['file'],
           'bbox': G[crop]['bbox'], 'confidence': confidence,
           'vs_C': vs_C, 'vs_H': vs_H, 'kind': kind,
           'error_category': category, 'H_marked': H_marked,
           'consequential': consequential}
    row.update(extra)
    changes.append(row)

change('main line 1, opening verb', 'correspondent', 'correspondant', 'correspondent',
       'After the d-like ascender the joining stroke is low and e-like before the final n/t movement; there is no separate closed a bowl. The cropped ending supports -ent. The remaining word is in the same running hand.', 'p01')
change('main line 2, short form after qui sont', r'\unsure{ess.|ext.}', r'ent.\ de', 'ent.',
       'The first character has an e loop. The middle is a low joined hump, without the crossed diagonals of x visible in aux on this same line. The terminal is a comparatively tall t stem, followed by a separate dark stop. There are not two successive s shapes.',
       'p02', vs_C=True, vs_H=False, consequential=True,
       scope='Only ent. is collated; the following de agrees in both witnesses.')
change('main line 5, abbreviated points', 'pts', r'p\supplied{oin}ts', 'pts',
       'Only p and the compact raised t/s group are written. There are no intervening oin letters and no final stop.',
       'p03', kind='abbreviation expanded or spelling modernised', category='Abbreviations expanded, spelling modernised')
change('insertion 1 between main lines 6 and 7',
       r'\inserted{qui est le seul cas, avec $n=0$, où $\mathfrak X$ est un schéma !}',
       r'\uncertain{qui est le seul cas}, \uncertain{avec} $n=0$, où $\mathfrak{X}$ soit un schéma !',
       r'\inserted{qui est le seul cas, avec $n=0$, où $\mathfrak X$ \unsure{est|soit} un schéma !}',
       'This whole clause is smaller writing on its own baseline between the n=1 line and sont les seuls. Its left edge begins below de X and its final ! and closing curve are below the earlier upper closing mark. The content is an inserted continuation of the parenthesis, not a main-line clause.',
       'p03', kind='insertion or placement', category='Insertions put in the wrong place', H_marked=True,
       scope='Placement only; est/soit and the upper closing mark have their own unresolved records.')
change('insertion 1, word after où X', 'est', 'soit', r'\unsure{est|soit}',
       'The initial short curved entry and final tall triangular t favor est; that t resembles the earlier est in the same insertion. The low middle is joined and equivocal, and no securely separate i dot can be assigned. The focused view does not settle the middle letters.',
       'p09', confidence='medium', vs_H=False, unresolved=True)
change('main line 6, altered mark after n=1 comma', '[absent]', '[absent]', r'\unsure{)}',
       'A real dark curved mark survives after the comma. It has a kinked/retraced top and a lower leftward return, so a closing parenthesis is plausible. No independent strike can be traced and no line securely connects it to the insertion below. It is retained as an unsure close; obsolete-close versus insertion-return status remains open.',
       'p09', confidence='low', vs_H=False, kind='other', category='Other', unresolved=True,
       scope='A newly retained visible mark with unsettled textual status; not counted as a settled error in either witness.')
change('left of Proposition, long vertical rule', r'\margin{$\big|$}',
       'note marginale ... reliée au texte par une accolade', rule,
       'A thin near-vertical line extends approximately from original y=1250 to y=1750 beside the Proposition. It has slight terminal irregularities, no mid-height brace notch and no inline absolute-value pairing. The large curved crossing at about y=1400 belongs to the f descender of relatif in the oblique note.',
       'p04', vs_C=True, kind='drawing or diagram', category='Drawings and diagrams',
       source_rule_bbox=[286, 1245, 302, 1752],
       scope='A real extent/shape correction, not a macro-syntax preference. H supplies the brace claim in its note; that note is not copied as manuscript text.')
change('main line 9, heading punctuation', r'\uline{Proposition}', r'\textbf{Proposition.}', r'\uline{Proposition}',
       'The final n ends in a low return; no separate stop follows before Pour. One straight underline runs below the word. The title is transcribed with that underline.',
       'p04', kind='text not on the page', category='Text that is not on the page',
       scope='The added stop is the lexical difference; bold/underline macro substitution alone is not counted.')
change('main line 9, quantifier after Pour', r'Pour $\forall x\in\mathfrak X$', r'Pour tout $x\in\mathfrak{X}$', r'Pour $\forall x\in\mathfrak X$',
       'A single large crossed quantifier sign stands between Pour and x; there is no written four-letter tout. The repaired contextual view includes the complete x∈X formula and the adjacent underlined O with both subscripts.',
       'p10', kind='misread symbol or index', category='Symbols and indices', consequential=True)
change('main lines 13–14, final phrase of Proposition',
       r"l'ens de ces anneaux dans $L$.",
       r"l'ens. des \uncertain{anneaux} \ill{} \uncertain{anneaux} \uncertain{dans} $L$.",
       r"l'ens de ces anneaux dans $L$.",
       'After ens there is open space with no separate stop. The next two groups are de and ces. The next line contains one anneaux, then dans L and a final dot; no second anneaux is written.',
       'p04', kind='readable ink left as \\ill{}', category='Readable ink left as illegible', H_marked=True)
change('oblique margin, lines 2–4 before the comma following X',
       r"partir d'un schéma excellent $X$", r'\ill{} \uncertain{relation} \ill{}',
       r"partir d'un schéma excellent $X$",
       'The rotated view shows partir with a tall crossed t, followed by d and the compact un; the next line has schéma and excellent with two adjacent tall l stems. A plain X begins the next line, before its comma. The phrase relation is not supported by these letter groups.',
       'p05', kind='readable ink left as \\ill{}', category='Readable ink left as illegible', H_marked=True)
change('oblique margin, line 4 following X comma', 'et construire', r'et alors \ill{}', 'et construire',
       'After the comma the short et is followed by a longer word with the con entry, a tall crossed t, and the final reduced ruire movement. There is no separate alors group.',
       'p05', H_marked=True)
change('oblique margin, lines 5–6', r'un $\mathfrak X$ relatif au dessus\ldots',
       r'\uncertain{relat.} \ill{} $\mathfrak{X}$ \ill{} \uncertain{dessus}…',
       r'un $\mathfrak X$ relatif au\newline dessus\unsure{\ldots|..}',
       'The written order is un, the looped X, relatif, au, then dessus on the next baseline. The final f of relatif has a long descender crossing the vertical rule. The ending punctuation consists of detached broad marks whose exact point count is separately left doubtful.',
       'p05', kind='readable ink left as \\ill{}', category='Readable ink left as illegible', H_marked=True,
       scope='Words and order only; ellipsis count is not counted as a resolved correction.')
change('main line 15, proof heading punctuation', r'\uline{Dém}', r'\emph{Dém.}', r'\uline{Dém}',
       'The accent belongs above the e. After the final low m there is a wide blank before a); there is no separate final stop. The word has one underline.',
       'p11', kind='text not on the page', category='Text that is not on the page',
       scope='Only the added stop is counted, not emphasis-macro syntax.')
change('insertion 2, g,h above membership sign in main line 16',
       r'\inserted{$g,h$}$\in\underline{O}_{X,a}$', r'$g,h\in\underline{O}_{X,a}$',
       r'\inserted{$g,h$}$\in\underline{O}_{X,a}$',
       'The small g, comma and tall h are written on a separate raised baseline above the membership position following f=g/h. A curved stroke attaches them to that place. The two local-ring subscripts are plain X,a, unlike the looped X,x in the earlier formula.',
       'p11', kind='insertion or placement', category='Insertions put in the wrong place', consequential=True)
change('main line 17, parenthetic model property', '(propre)', '(projectif)', '(propre)',
       'The word has two p descenders, with reduced ro between them and re following the second. It is short, and there is no j descender or separate ctif tail. The enclosing parentheses are visible below the insertion leader.',
       'p11', consequential=True)
change('main line 17, point abbreviation', 'pt', r'p\supplied{oin}t', 'pt',
       'A p and a compact raised t are written, with no oin between them. The following comma is separate; no abbreviation stop is present.',
       'p11', kind='abbreviation expanded or spelling modernised', category='Abbreviations expanded, spelling modernised')
change('main line 19, cancelled clause after résolution',
       r'\deleted{\unsure{on} \uline{\unsure{sépare}} \unsure{les diviseurs}}',
       r'\struck{\ill{}} \ill{} \struck{\ill{}}',
       r'\deleted{\unsure{on} \uline{\unsure{sépare}} \unsure{les diviseurs}}',
       'A cancellation crosses the lower baseline from the short group after résolution through the right-hand word group. The first group is mostly submerged. In the middle group a p-like descender and traces compatible with sépare survive, with an independent underline below it. The far-right letters intersect the replacement insertion. None of the three C readings can be resolved letter by letter under this overlap.',
       'p07', confidence='low', vs_H=False, kind='other', category='Struck text', H_marked=True, unresolved=True,
       scope='Unresolved word correspondence; the cancellation and separate underline are observed and retained, but the hypothetical word readings are not counted as settled H errors.')
change('insertion 4 above the cancelled main line 19 clause',
       r'\inserted{OPS $\exists$ \unsure{système} régulier}',
       r'OPS $\exists$ \uncertain{syst.} \struck{\ill{}} \ill{}',
       r'\inserted{OPS $\exists$ système régulier}',
       'OPS, the reversed-E existential sign, système and régulier run on a raised replacement baseline above the cancelled words. The cancellation crosses descenders from the upper words but is directed through the lower baseline. The replacement attaches after résolution and continues into de paramètres on the final line.',
       'p07', kind='insertion or placement', category='Insertions put in the wrong place', H_marked=True,
       scope='Insertion status and attachment; the système reading and recovery of régulier have separate rows.')
change('insertion 4, M0128 word following existential sign', r'\unsure{système}', r'\uncertain{syst.}', 'système',
       'The initial s and y descender are followed by the short s/t portion, then continued connected strokes for ème. In particular a long low m sequence and terminal e extend well beyond the t; there is no independent abbreviation stop at that point. The word is written in full, not syst.',
       'p07', H_marked=True)
change('insertion 4, final word', 'régulier', r'\ill{}', 'régulier',
       'After système there is a separate r/e entry with an accent, a looped g descending across the cancellation, then u, a tall l, and the short ier ending. The lower cancellation does not erase this upper word.',
       'p07', kind='readable ink left as \\ill{}', category='Readable ink left as illegible', H_marked=True)
change('main line 20, complete final line', r'de paramètres, avec $f,g$ des monômes',
       r'\ill{} $f$, $g$ \uncertain{des} \ill{} de \uncertain{paramètres}, \ill{}',
       r'de paramètres, avec $f,g$ des monômes',
       'The left-to-right order is de paramètres, a comma, avec, f and g, des, then monômes. The f has a tall stem and left-returning descender; g is a separate loop and descender. The circumflex is visible above monômes. No terminal period follows. The same literal f,g pair already appears after a un pt, despite the earlier inserted g,h.',
       'p07', kind='readable ink left as \\ill{}', category='Readable ink left as illegible', H_marked=True, consequential=True)
change('lower left, thin foliation', r'\margin{121}', '[absent]', r'\margin{121}',
       'The three thin figures are a rising-entry 1, a curved 2 with low foot, and another 1. They stand alone at the lower left. No author page number appears at the head of the sheet.',
       'p08', kind='omission', category='Omissions')

decisions = [
    {'id':'M0127', 'cote':'149', 'scan':'122', 'decision':'other', 'reading':'ent.',
     'evidence':changes[1]['evidence'], 'crop':G['p02']['file'], 'bbox':G['p02']['bbox'], 'confidence':'high'},
    {'id':'M0128', 'cote':'149', 'scan':'122', 'decision':'first', 'reading':'système',
     'evidence':changes[19]['evidence'], 'crop':G['p07']['file'], 'bbox':G['p07']['bbox'], 'confidence':'high'},
]

unlisted = []
for place, token, evidence in [
    ('main line 19, first cancelled group', 'on', 'The short group is largely covered by the cancellation; a curved entry and low continuation are compatible with on but do not make both letters plain.'),
    ('main line 19, underlined cancelled group', 'sépare', 'The independent underline and a p-like descender survive; several joined interior letters meet the strike, so sépare remains provisional.'),
    ('main line 19, final cancelled group', 'les diviseurs', 'The group overlaps the descenders of système and régulier above. Tall strokes and low tails survive, but the complete letter sequence cannot be isolated confidently.'),
]:
    unlisted.append({'place':place, 'C':f'\\unsure{{{token}}}', 'decision':'undecided',
                     'reading':f'\\unsure{{{token}}}', 'evidence':evidence,
                     'crop':G['p07']['file'], 'bbox':G['p07']['bbox'], 'confidence':'low',
                     'reason_outside_decisions':'Nested C doubt absent from supplied marks.tsv; no M ID invented.'})

inventory = []
def element(kind, position, text, hand='his hand', **extra):
    row = {'sheet_kind':'text', 'hand':hand, 'element':f'e{len(inventory)+1:02d}',
           'kind':kind, 'position':position, 'first_words_or_objects':text, 'transcribed':'yes'}
    row.update(extra)
    inventory.append(row)

element('text', 'main lines 1–4, page opening', 'correspondent exactement (via x↦O...)')
element('text', 'main lines 5–8, second paragraph', 'Sauf erreur, ces deux types de pts')
element('deletion', 'main line 6 after épuisent', 'tout')
element('insertion', 'between main lines 6 and 7', 'qui est le seul cas, avec n=0, où X est|soit un schéma !', logical_lines=1)
element('text', 'right end of main line 6, after n=1 comma', r'\unsure{)}', status='Textual/status classification uncertain; possible obsolete close or insertion return, not asserted deleted.')
element('text', 'main lines 9–14', 'Proposition Pour ∀x∈X...')
element('drawing', 'left of main lines 10–14', 'long vertical marginal rule', bbox=[286,1245,302,1752])
element('margin note', 'oblique left margin beside Proposition', "On pourrait / partir d'un / schéma excellent / X, et construire / un X relatif au / dessus...", logical_lines=6)
element('text', 'main lines 15–20, proof beginning and unfinished ending', 'Dém a) Soit f∈L...')
element('insertion', 'above membership sign on main line 16', 'g,h', logical_lines=1)
element('insertion', 'above modèle on main line 17', 'régulier', logical_lines=1)
element('deletion', 'main line 18 before the dash', 'premiers entre eux')
element('deletion', 'main line 19 after résolution', 'on sépare les diviseurs', decoration='One separate underline under sépare survives below the cancellation.')
element('insertion', 'above cancelled main line 19 words', 'OPS ∃ système régulier', logical_lines=1)
element('margin note', 'lower left edge', '121', hand='thin foliation hand, not assigned to author', logical_lines=1)

doubts = [
    {'place':'insertion 1 after où X', 'reading':r'\unsure{est|soit}', 'alternatives':'est | soit', 'confidence':'medium', 'crop':G['p09']['file'], 'bbox':G['p09']['bbox']},
    {'place':'altered upper closing mark after n=1 comma', 'reading':r'\unsure{)}', 'alternatives':'closing parenthesis; obsolete/revised closing parenthesis; insertion return or leader (status unresolved, no deletion asserted)', 'confidence':'low', 'crop':G['p09']['file'], 'bbox':G['p09']['bbox']},
    {'place':'end of oblique marginal note', 'reading':r'dessus\unsure{\ldots|..}', 'alternatives':'ellipsis of three points, with joined/elongated points | two points', 'confidence':'medium', 'crop':G['p05']['file'], 'bbox':G['p05']['bbox']},
    {'place':'main line 18, first cancelled word', 'reading':r'\deleted{\unsure{premiers} entre eux}', 'alternatives':'premiers (the interior letters are obscured; no unsupported replacement word proposed)', 'confidence':'medium', 'crop':G['p07']['file'], 'bbox':G['p07']['bbox']},
]
for u in unlisted:
    doubts.append({'place':u['place'], 'reading':u['reading'], 'alternatives':u['reading']+' remains provisional; no secure alternative',
                   'confidence':'low', 'crop':u['crop'], 'bbox':u['bbox']})

# The second paragraph, marginal text, proposition and proof interleave in height.
# A full contextual rectangle avoids transcribing English labels for clipped tails.
audit_boxes = [
    {'box':'b01', 'kind':'C/H word difference', 'bbox':[310,60,1625,177],
     'reading':r'correspondent exactement (via $x\longmapsto\underline{O}_{\mathfrak X,x}$)'},
    {'box':'b02', 'kind':'C/H word difference; resolved C doubt', 'bbox':[315,175,1645,305],
     'reading':r'aux jauges dans $L$ qui sont ent. de'},
    {'box':'b03', 'kind':'insertion; margin note; deletion; handwritten number; C/H word difference; less-than-high C departure; drawing',
     'bbox':[15,560,1665,2355],
     'reading':second+'\n\n'+rule+'\n'+proposition+'\n'+margin+'\n\n'+proof+'\n'+folio},
]

main_lines = [
    r'correspondent exactement (via $x\longmapsto\underline{O}_{\mathfrak X,x}$)',
    r'aux jauges dans $L$ qui sont ent. de',
    r'type fini sur $K$, de corps des',
    r'fractions $L$ --- i.e. aux $V$ précédents.',
    r'Sauf erreur, ces deux types de pts',
    r'de $\mathfrak X$ (qui épuisent \deleted{tout} si $n=1$,\unsure{)}',
    r'sont les seuls pour lesquels $\underline{O}_{\mathfrak X,x}$ soit',
    r'noethérien. Cependant, on a',
    r'\uline{Proposition} Pour $\forall x\in\mathfrak X$, $\underline{O}_{\mathfrak X,x}$ est',
    r'un anneau de valuation dans $L$, de',
    r'corps des fractions $L$, et contenant $K$.',
    r"L'application $x\longmapsto\underline{O}_{\mathfrak X,x}$ est une",
    r"bijection de $\mathfrak X$ sur l'ens de ces",
    r'anneaux dans $L$.',
    r'\uline{Dém} a) Soit $f\in L\setminus\underline{O}_{\mathfrak X,x}$, il faut',
    r'prouver $\frac1f\in\underline{O}_{\mathfrak X,x}$. Or $f=g/h$, $\in\underline{O}_{X,a}$, où',
    r'$X$ modèle (propre), $a$ un pt, $f,g$',
    r'\deleted{\unsure{premiers} entre eux} --- utilisant la',
    r'résolution, \deleted{\unsure{on} \uline{\unsure{sépare}} \unsure{les diviseurs}}',
    r'de paramètres, avec $f,g$ des monômes',
]
line_inventory = [{'label':f'main_{i:02d}', 'class':'main', 'reading':s} for i,s in enumerate(main_lines,1)]
for i,s in enumerate([r'On pourrait',r"partir d'un",r'schéma excellent',r'$X$, et construire',r'un $\mathfrak X$ relatif au',r'dessus\unsure{\ldots|..}'],1):
    line_inventory.append({'label':f'margin_{i:02d}','class':'margin','reading':s})
for i,s in enumerate([r'qui est le seul cas, avec $n=0$, où $\mathfrak X$ \unsure{est|soit} un schéma !)',r'$g,h$',r'régulier',r'OPS $\exists$ système régulier'],1):
    line_inventory.append({'label':f'insertion_{i:02d}','class':'insertion','reading':s})
line_inventory.append({'label':'number_01','class':'standalone_number','reading':'121'})

report = {
    'page':PAGE, 'scan':122, 'reader':'reader_a', 'line_count':31,
    'line_count_detail':{'main':20,'margin':6,'insertion':4,'standalone_numbers':1},
    'line_inventory':line_inventory,
    'changes':changes, 'decisions':decisions, 'unlisted_doubt_decisions':unlisted,
    'inventory':inventory, 'doubts':doubts, 'audit_boxes':audit_boxes,
    'notes':[
        'The page begins in the middle of a sentence about local rings and certain valuations. It distinguishes two types of points, states a proposed bijection between points and valuation rings in L containing K with fraction field L, and begins a proof using resolution. The proof continues beyond the bottom edge of this page.',
        'No author page or section number is visible at the head. The thin lower-left 121 is retained as foliation, not converted to an author mspage number.',
        'The literal opening abbreviation is ent. Its expansion cannot be established from this page alone; the reading is not replaced by a mathematically expected ess.',
        'The altered upper closing mark after n=1 is kept as an unsure parenthesis. Its relation to the lower inserted closing parenthesis is uncertain; it may be an obsolete/revised close or an insertion return. No distinct cancellation stroke is established, so deletion is not asserted.',
        'The insertion after n=1 occupies one separate small baseline. The inserted est|soit remains equivocal after a focused view, with est first on local letter shape. Both n=1 and n=0 are preserved exactly.',
        'The vertical rule is a long marginal line beside the Proposition, beginning below its heading line. The curved crossing of that rule comes from the f of relatif in the note. It is not a separate brace joining the note to the main text.',
        'The oblique note has six baselines. au belongs on the same marginal baseline as un X relatif; dessus and the terminal marks occupy the sixth. No hyphen is introduced in au dessus.',
        'The proof writes f=g/h and inserts g,h before the following membership sign, but then visibly writes f,g after a un pt and again before des monômes. These source letters are retained. They may represent an authorial mismatch; this page alone does not authorize a repair to g,h.',
        'The curved strokes under inserted g,h and régulier act as attachment strokes. The cancellation in the bottom cluster passes through the lower old clause and intersects descenders from the raised OPS ∃ système régulier; that crossing does not make the replacement itself deleted.',
        'The main proof is incomplete, and no independent mathematical proof verification or computation was performed. The transcription and local consistency observation are not a proof of the proposition.',
        'Audit box b03 is intentionally a complete contextual rectangle covering the second paragraph through the page bottom. The oblique note overlaps the Proposition horizontally, its descenders cross the rule, and the main-line ascenders/descenders overlap adjacent vertical bands. The reading field therefore gives all actual manuscript text in that rectangle instead of English descriptions of clipped context.',
        'Only M0127 and M0128 were supplied in marks.tsv. The three nested C doubts in the cancelled clause are reported separately and have no invented M IDs.',
    ],
    'checks':[],
    'hand_observations':[
        {'habit':'A low joined middle and a comparatively tall terminal t can make a short form resemble ess. or ext.; the crossing of a true x must be checked locally.',
         'places':'main line 2, ent.; comparison with aux on that line',
         'holds':'Only this occurrence of ent. is established here; no broader abbreviation meaning is inferred.',
         'witness_errors':'C offers ess.|ext.; H supplies the ink-supported ent.'},
        {'habit':'A long f descender in an oblique marginal note can cross an independent vertical rule and resemble a brace.',
         'places':'relatif in marginal line 5 and the adjacent Proposition rule',
         'holds':'One crossing on this page, traced to the f.',
         'witness_errors':"H's editorial note describes an accolade; the ink separates the f descender and the long rule."},
        {'habit':'The author uses a looped, double-return X for the space and a simpler plain X for a model.',
         'places':'opening mapping; Proposition; proof local-ring subscripts; oblique note; X modèle',
         'holds':'All read occurrences on this page respect that local distinction, although the first index is heavily reinforced.',
         'witness_errors':'No additional alphabet correction is asserted; the current C distinction is retained.'},
        {'habit':'Point abbreviations use a tall p followed by compact raised t or ts, without the letters oin.',
         'places':'main line 5 pts and main line 17 pt',
         'holds':'Both occurrences on this page.',
         'witness_errors':'H expands both as p[supplied oin]t(s).'},
        {'habit':'Replacement words on a raised baseline may have descenders crossing the cancellation of the lower words.',
         'places':'système régulier above cancelled on sépare les diviseurs',
         'holds':'The lower cancellation and the two raised words are distinguishable by baseline; interiors of the lower words remain doubtful.',
         'witness_errors':'H leaves the lower cluster and the replacement ending incompletely read.'},
    ],
    'notation':[
        {'written':r'$\underline{O}_{\mathfrak X,x}$', 'meaning_or_use':'The local-ring notation attached to x in the space X; O carries a short underline and the index has the looped X followed by x.', 'places':'opening mapping; second paragraph; Proposition; proof opening'},
        {'written':r'$\underline{O}_{X,a}$', 'meaning_or_use':'Local-ring notation for the plain model X and its point a; these indices are visibly distinct from the looped X,x above.', 'places':'proof main line 16'},
        {'written':r'$x\longmapsto\underline{O}_{\mathfrak X,x}$', 'meaning_or_use':'Mapping with a left vertical bar and a right arrowhead.', 'places':'main lines 1 and 12'},
        {'written':r'$\forall$', 'meaning_or_use':'Written quantifier after the word Pour; it is not replaced by tout.', 'places':'Proposition opening'},
        {'written':r'$\exists$', 'meaning_or_use':'Written existential sign in the raised OPS replacement.', 'places':'insertion 4'},
        {'written':r'$f,g$', 'meaning_or_use':'Literal pair in two proof phrases; retained alongside f=g/h and the separately inserted g,h.', 'places':'main lines 17 and 20'},
    ],
    'abbreviations':[
        {'written':'ent.','expansion':'Unresolved on this page; no expansion inserted.'},
        {'written':'pts','expansion':'points'},
        {'written':'pt','expansion':'point'},
        {'written':'ens','expansion':'ensemble'},
        {'written':'Dém','expansion':'Démonstration'},
        {'written':'i.e.','expansion':'id est'},
        {'written':'OPS','expansion':'on peut supposer (contextual expansion only; uppercase written form retained)'},
    ],
    'inspection':{
        'whole':True, 'halves':['top','bottom'], 'crops':[g['file'] for g in geometry],
        'crop_count':len(geometry), 'deletions_insertions_checked':True,
        'source_dimensions':[1681,2365], 'native_half_dimensions':[1681,1301],
        'crop_geometry_file':f'review/{PAGE}_crop_geometry.json',
        'crop_script':f'review/{PAGE}_make_crops.py',
        'inspection_notes':[
            'The whole image was inspected once for layout. The first attempted top-half display was truncated by context delivery and was unusable; top.png was then displayed successfully once. bottom.png was displayed successfully once.',
            'All eleven saved crops were visually inspected. No OCR, external research, text-layer extraction, other page reading or TeX compilation was used.',
            'p05 is a rotation of the still-open oblique note, not a second crop of a decided reading. p09 focuses the still-open inserted est/soit and altered upper closing mark.',
            'The top curls of the first Proposition formula touched/crossed the p04 top edge. p10 is the single incomplete-view repair for that formula. The faut ascender crossed the p06 top edge; p11 is the single complete proof-context repair. These repairs are not treated as additional independent evidence or reinspection of a previously decided reading.',
            'Crops p04, p06, p07, p09, p10 and p11 contain boundary fragments of adjacent context; those are not used as blind-audit boundaries. Complete actual-text audit box b03 covers all the interleaving context instead.',
        ]
    }
}

assert sum(report['line_count_detail'].values()) == report['line_count'] == len(line_inventory)
assert {d['id'] for d in decisions} == {'M0127','M0128'}
assert len(changes) == 23
assert len(doubts) == 7
assert len(geometry) == 11
assert all((ROOT / 'edition' / g['file']).is_file() for g in geometry)
(OUT / f'{PAGE}.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(json.dumps({'page':PAGE,'line_count':report['line_count'],'changes':len(changes),
                  'decisions':len(decisions),'unlisted_doubts':len(unlisted),
                  'crops':len(geometry),'remaining_doubts':len(doubts),
                  'audit_boxes':len(audit_boxes)}, ensure_ascii=False))
