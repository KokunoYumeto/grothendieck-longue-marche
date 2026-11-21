#!/usr/bin/env python3
"""Build the visually read scan131 return; no other page is accessed."""
from pathlib import Path
import json
import re

ROOT = Path('/workspace/scratch/12caffedf246')
PACKET = ROOT / 'packets/147_scan131'
OUT = ROOT / 'edition/reports'
C = (PACKET / 'C.tex').read_text()
H = (PACKET / 'H.tex').read_text()
CROPS = {
    Path(x['crop']).stem.removeprefix('147_scan131_'): x
    for x in map(json.loads, (OUT / '147_scan131_crops.jsonl').read_text().splitlines())
}

def between(source, first, last):
    i = source.index(first)
    return source[i:source.index(last, i) + len(last)]

formula212 = r'''\[
\tag{\unsure{212|217}}
\left\{\begin{aligned}
\Pi_{\Delta_r}&=\Pi_1D^*_{\Delta_r}\qquad\text{groupoïde fond.}\\
&\hspace{4cm}\text{de }D^*_{\Delta_r}\\
\widetilde\Pi_{\unsure{\Delta}_r}&=\Pi_1P^*_{\Delta_r}\qquad\text{et de }P^*_{\Delta_r}
\end{aligned}\right.
\]'''
diagram213 = r'''\diagram{\((213)\qquad\)\begin{tikzcd}[ampersand replacement=\&]
\widetilde\Pi_{\Delta_r}\arrow[r]\&\Pi_{\Delta_r}
\end{tikzcd}}'''
formula214 = r'''\[
\tag{214}
\left\{\begin{aligned}
\Pi_{\Delta_r}&=\coprod_{d_0\geq d_1\geq\mathord{\text{.\,--}}\geq d_r}\Pi_{d_0,d_1,,\text{--},d_r}\\
\widetilde\Pi_{\Delta_r}&=\coprod_{d_0\geq\text{--}\geq d_r}\widetilde\Pi_{d_0,d_1,\text{--},d_r}
\end{aligned}\right.
\]'''
local_formula = r'$T_{d_0\text{-\,-}d_r}$ sur les $\Pi_{d_0,\text{--},d_r}$.'
lastline = r"$\Pi_{d,d'}=\Pi_1D^*_{d,d'}$, et $\Pi_{d'}=\Pi_1D^*_{d'}$, (par"

proposed = '\\scanpage{131}\n' + formula212 + '\n' + r'''donc on a
''' + diagram213 + '\n' + r'''qui fait de $\widetilde\Pi_{\Delta_r}$ un groupoïde
extension de $\Pi_{\Delta_r}$ par $T_{\Delta_r}$.
Notons ``pour mémoire''
''' + formula214 + '\n' + r'''\margin{\deleted{\unsure{au fait}}}
le système local $T_{\Delta_r}$ sur $\Pi_{\Delta_r}$ \deleted{\unsure{pourra}}
\unsure{s'identifiant|s'identifie} aux systèmes locaux
''' + local_formula + '\n\n' + r'''Les $\Pi_{\Delta_r}$ n'ont pas de ``dépendance
simpliciale'' \unsure{p.v.|p.r.} aux $\Delta_r$, p. ex. on n'a
pas de morphisme naturel entre
''' + lastline + '\n\\margin{130}\n'

rows = []
def row(place, c, h, final, evidence, crop, kind, against_c=False,
        against_h=True, marked_h=False, math=False, confidence='high',
        category='Words', native_box=None):
    assert not c or c in C, ('nonliteral C span', place, c)
    assert not h or h in H, ('nonliteral H span', place, h)
    if native_box is None:
        source = CROPS[crop]
        image_path, coords = source['crop'], source['box']
    else:
        image_path, coords = '../packets/147_scan131/bottom.jpg', native_box
    rows.append(dict(place=place, C=c, H=h, final=final, scan_shows=evidence,
                     crop=image_path, box=coords, confidence=confidence,
                     kind=kind, against_C=against_c, against_H=against_h,
                     marked_in_H=marked_h, math_consequential=math,
                     error_category=category))

row('lower right annotation of the first display', r'\text{et de }P^*_{\Delta_r}',
    r'\text{id.\ de } P^{*}_{\Delta_r}', r'\text{et de }P^*_{\Delta_r}',
    'The first small word begins with a low curved e-like entry and rises into the tall narrow terminal t form; it has no i dot or following abbreviation point. De and the starred P are separate and clear.',
    'lower212', 'misread word')
row('prose between the first display and (213)', 'donc on a', 'donc un morph.', 'donc on a',
    'After donc there is a compact round o and low n stroke, then a separate small a-like body. The tall and descending strokes required by morph. are absent.',
    'donc', 'misread word')
row('quotation after Notons', "Notons ``pour mémoire''", 'Notons « pour mémoire »',
    "Notons ``pour mémoire''",
    'The opening consists of two separate short high strokes; the closing consists of two small high curled strokes. Neither end is a pair of angle-shaped guillemets.',
    'memoire', 'misread symbol or index', category='Symbols and indices')
row('(214), both coproduct expressions and their right-hand subscripts',
    between(C, r'\tag{214}', r'\end{aligned}\right.'),
    between(H, '(214)', r'\end{cases}'), formula214,
    'All inequality signs have a separate lower bar. In the upper index, a small low dot followed by a short continuous dash stands between the two final inequality signs; the lower index has one continuous dash. In the upper right subscript the small 1 attached to the second d is followed by two distinct low comma strokes, then a continuous dash and a comma before d_r. The lower right subscript has only one comma after its d_1, then its dash and the comma before d_r. These low comma strokes and dash forms are preserved instead of being replaced by a conventional dotted ellipsis. Both coproduct signs have a bottom bar and two uprights; tildes occur only on the lower row. Number214 is clear.',
    'formula214', 'misread symbol or index', against_c=True, math=False,
    category='Symbols and indices')
row('slanted cancelled left-margin note beside (214)', r'\margin{\deleted{\unsure{au fait}}}', '',
    r'\margin{\deleted{\unsure{au fait}}}',
    'After the crop is rotated upright, a short dark initial cluster, a long f-like descender, a low oval, a high dot and a tall final t-like stroke survive under the long strike. Au fait remains a tentative reading because several letters merge into that strike. The final tall stroke and preceding dot do not establish an extra question mark. H describes a crossed stroke without readable text in an editorial note; that description is not transcribed as source wording.',
    'margin_cancel', 'omission', marked_h=True, confidence='low', category='Omissions')
row('cancelled word at the right end of le système local line',
    r'\deleted{\unsure{pourra}}', r'\struck{provient}', r'\deleted{\unsure{pourra}}',
    'A looped p descender and rounded following bodies survive, but the middle and terminal sequence are crossed by the strong horizontal cancellation. The stroke ends to the right of the word; it does not cross the preceding Pi expression. Pourra remains a candidate, not a resolved reading; provient cannot be conclusively excluded from the obscured strokes.',
    'cancelled_verb', 'misread word', confidence='low')
row('live verb after that cancellation, M1295',
    r"\unsure{s'identifiant|s'identifie}", 'se réduisant', r"\unsure{s'identifiant|s'identifie}",
    'The live line begins with a short s-like body, then the dotted i/d loop and compressed identifi- sequence. Its ending has a long low run and a raised/crossed terminal turn that favors -ant, but not every terminal letter separates. The two C candidates remain. The word is live, without a crossing stroke; se réduisant does not fit the visible initial sequence.',
    'live_verb', 'misread word', confidence='medium')
row('local-system/component formula below the live verb',
    r'$T_{d_0\cdots d_r}$ sur les $\Pi_{d_0,\ldots,d_r}$.',
    r'$T_{d_0 \dots d_r}$ sur les $\Pi_{d_0,\dots,d_r}$.', local_formula,
    'Read directly on the native bottom half: the T subscript has d_0 followed by two short separated horizontal continuation strokes and d_r, without commas. The Pi subscript has d_0, a low comma, one continuous dash, a second comma and d_r. The final point is separate. These graphic continuation forms were settled on the native half, so no additional first-pass crop was made. The recorded box uses original full-page coordinates; bottom.jpg begins at original y1062.',
    None, 'misread symbol or index', against_c=True, math=False,
    category='Symbols and indices', native_box=[270,1770,1295,1905])
row('quotation around dépendance simpliciale', "``dépendance\nsimpliciale''", '« dépendance simpliciale »',
    "``dépendance\nsimpliciale''",
    'Two high individual strokes open the quotation before dépendance, and two short high strokes close it after simpliciale. There are no angle-shaped guillemets.',
    'simpliciale', 'misread symbol or index', category='Symbols and indices')
row('abbreviation and following preposition after simpliciale', 'p.r. aux', 'par rapport à',
    r'\unsure{p.v.|p.r.} aux',
    'The first letter has the p descender and its following point. The next letter has a low angular trough and rising right arm, visibly v-shaped, followed by a point; it can also be the author’s reduced r form. The literal form is retained with v first and r as the alternative. Aux consists of three compact low bodies after the abbreviation, rather than a single accented à. The expected expansion does not decide the ambiguous letter.',
    'simpliciale', 'abbreviation expanded or spelling modernised', against_c=True,
    confidence='medium', category='Abbreviations expanded, spelling modernised')
row('final parenthetical fragment after the two equalities', '(par', r"\uncertain{l'application}", '(par',
    'A curved opening delimiter is followed by a long p descender and the short a/r sequence. No further letters or closing parenthesis occur before the blank bottom-right edge. Both preceding D forms have distinct star strokes; their indices, Pi_1 forms, comma and intervening et are visible.',
    'lastline', 'misread word', marked_h=True)
row('pencil foliation at lower left', r'\margin{130}', '', r'\margin{130}',
    'The pale pencil sequence is 1 with a slanting entry, 3 with two curved lobes, and a closed oval 0. It is separate from the main ink and the scan border.',
    'footer130', 'omission', category='Omissions')

decisions = [dict(id='M1295', decision='undecided', reading=r"\unsure{s'identifiant|s'identifie}",
    ink='The live initial sequence favors s’identifi-; the long compressed ending and raised/crossed terminal turn favor -ant but do not separate every letter. Retain s’identifie as the alternative.',
    crop=CROPS['live_verb']['crop'], box=CROPS['live_verb']['box'], confidence='medium')]

inventory = []
def inv(kind, position, first, hand='his hand'):
    inventory.append(dict(element=f'E{len(inventory)+1:02d}', kind=kind,
                          position=position, first_words_or_objects=first,
                          sheet_kind='text', hand=hand, transcribed='yes'))
inv('display', 'top of sheet, two main rows with a left brace and three right-column annotation baselines', formula212)
inv('text', 'between first display and map (213)', 'donc on a')
inv('diagram', 'upper third, numbered at left (213)', diagram213)
inv('text', 'three prose baselines between (213) and (214)', "qui fait de / extension de / Notons ``pour mémoire''")
inv('display', 'middle, two rows under a left brace, numbered (214)', formula214)
inv('margin note', 'obliquely rising at the left of the lower row of (214)', r'\margin{\deleted{\unsure{au fait}}}')
inv('deletion', 'the complete short marginal phrase, under a single long slanted stroke', r'\deleted{\unsure{au fait}}')
inv('text', 'three prose baselines after (214)', r'le système local $T_{\Delta_r}$')
inv('deletion', 'right edge of the first of those three prose baselines', r'\deleted{\unsure{pourra}}')
inv('text', 'four final main prose baselines, ending in an open parenthetical fragment', r"Les $\Pi_{\Delta_r}$ n'ont pas de ``dépendance")
inv('margin note', 'bottom left, near the paper edge', '130', 'pencil foliation, hand unassigned')

doubts = [
    dict(place='number of the first display', reading=r'\unsure{212|217}', alternatives='212 / 217: the final digit has a short curved top, near-vertical descent and tiny right foot', confidence='medium'),
    dict(place='Delta in the lower left subscript of the first display', reading=r'\widetilde\Pi_{\unsure{\Delta}_r}', alternatives='Delta is the leading final form; earlier or retraced interior/upper strokes cannot be separated as another complete letter', confidence='medium'),
    dict(place='cancelled left margin', reading=r'\deleted{\unsure{au fait}}', alternatives='au fait tentative; letters partly merge with the strike', confidence='low'),
    dict(place='cancelled right-hand word after Pi_{Delta_r}', reading=r'\deleted{\unsure{pourra}}', alternatives='pourra tentative; H’s provient is not securely excluded under the strike', confidence='low'),
    dict(place='live verb, M1295', reading=r"\unsure{s'identifiant|s'identifie}", alternatives='s’identifiant / s’identifie; first candidate favored but ending compressed', confidence='medium'),
    dict(place='abbreviation after simpliciale', reading=r'\unsure{p.v.|p.r.}', alternatives='v-shaped letter / reduced r form; expansion is not used to resolve the shape', confidence='medium')
]

notes = [
    'Scan131 is upright. No separate author page number is visible above the first display; pencil foliation130 is at lower left. The whole image and both native halves were read once, and all11 first-pass crops were viewed. There are16 principal baselines:11 prose baselines and5 mathematical rows (two in the first display, one map row in213, two rows in214). The extra right-column continuation de D* in the first display is separately inventoried as annotation; the slanted cancelled margin and pencil number are not principal baselines.',
    'The first display is labelled 212 in both witnesses, but its final digit differs from the first2: it has a short curved top, near-vertical descent and small right foot. The reading 212|217 remains local uncertainty; neither the expected numbering sequence nor witness agreement is treated as evidence that resolves it. The lower left Delta is overtraced with interior and upper strokes; the final triangular form is tentative, and no invented earlier deleted letter is supplied.',
    'S131-01: the first display defines the two Pi symbols using the fundamental groupoids of the starred D and P spaces. The capital Pi forms have a horizontal top bar and two separate descending uprights throughout the page. The right-hand annotations say groupoïde fond., de D*, and et de P*. These definitions have been transcribed; no independent geometric identification is claimed.',
    'S131-02: the headed map(213) is asserted to make the tilde-Pi groupoid an extension of Pi by T. Its source, target, tilde, indices and complete rightward arrowhead are clear on the native upper half. The analytic or homotopy hypotheses needed for the asserted extension are not supplied on this sheet and were not independently verified. This assertion is carried as background, not certified from the diagram.',
    'S131-03: (214) recalls the coproduct decompositions by degree sequences. A limited topological check was performed: for an actual topological disjoint union X=∐X_i, each path and each path homotopy has connected parameter space and therefore stays in one summand; hence the ordinary fundamental groupoid of X is the disjoint union of the fundamental groupoids of the summands. This checks only that formal topological implication. It does not establish the stated analytic decomposition, a particular alternative meaning of Pi_1, or any geometry of the D/P spaces.',
    'The individual continuation strokes are preserved in (214) and in the subsequent local-system formula. In the upper coproduct index there is a small dot followed by a short dash; the lower index has a continuous dash. The upper right subscript has two commas after d_1 before its dash; the lower right subscript has one. In the prose formula, T has two short separated dash strokes without commas, whereas Pi has a single dash between commas. These are graphic shorthand for continuation, not a proposed subtraction operation or a silent repair of the degree indices.',
    'S131-04: the next paragraph identifies the local system on the coproduct groupoid with the degree-indexed local systems. The cancelled marginal phrase au fait and the cancelled word pourra remain doubtful. The live verb favors s’identifiant but keeps the s’identifie alternative because the ending is compressed. No independent verification of the local systems or their transport maps was made.',
    'S131-05: the last paragraph states that the Pi family lacks simplicial dependence and that there is no natural morphism between the two displayed degree-indexed groupoids. The reason begins only with the visible fragment (par at the bottom edge; its continuation is absent from this scan. The nonexistence assertion was not proved or refuted from this page alone.',
    'The abbreviation after simpliciale has a clearly v-shaped second letter, but a reduced r remains possible in this hand. Its literal p.v.|p.r. form is retained. The usual par rapport expansion may explain the intended phrase but cannot choose the letter. Aux is written after it. Both quotations on the page use paired high strokes, not guillemets. The pale texture and scan border carry no transcribed text.'
]
check_events = [
    dict(statement_id='S131-01', type='carried as background without fault found', outcome='Recorded the definitions of the two groupoids and read every symbol and annotation. No independent geometric construction or identification was attempted.'),
    dict(statement_id='S131-02', type='carried as background without fault found', outcome='Read the complete headed map and the asserted extension by T. The hypotheses needed for the extension were not checked from this page.'),
    dict(statement_id='S131-03', type='targeted proof check', outcome='For the ordinary topological fundamental groupoid of an actual disjoint union, checked that connected path and homotopy parameter spaces cannot cross summands. This establishes the coproduct property under that explicit hypothesis only.'),
    dict(statement_id='S131-04', type='carried as background without fault found', outcome='Recorded the asserted identification with the degree-indexed local systems, without verifying their construction or transport.'),
    dict(statement_id='S131-05', type='carried as background without fault found', outcome='Recorded the lack-of-simplicial-dependence and no-natural-morphism claims. Their explanation is truncated after (par, so no proof or refutation was claimed.')
]

hand_log = [
    dict(habit='Capital Pi has a straight top bar and two long descending uprights; its subscript1 is a separate low stroke.', places='first display, map213, display214, prose and final two equalities', scope='All visible Pi forms on scan131 were compared; no lower-case pi substitution is made.', misreadings='Both witnesses retain capital Pi; the case is confirmed locally.'),
    dict(habit='An overtraced triangular subscript can contain an extra interior bar and upper remnants.', places='lower left Delta in the first display', scope='One locally doubtful overwritten form on scan131; neighboring D/P subscripts have clear triangles.', misreadings='Both witnesses give a certain Delta here; a local doubt is added without assigning an earlier deleted letter.'),
    dict(habit='A compressed final digit may lack the broad returning base of a clearer2 on the same label.', places='first display label, compared with its initial2', scope='The last digit remains unresolved on scan131.', misreadings='Both witnesses give212 certainly; 212|217 is retained.'),
    dict(habit='A small1 attached to d and subsequent low comma strokes must be counted separately.', places='upper and lower right subscripts in214', scope='The upper row has two commas after d_1, the lower row one; confirmed on the full display crop.', misreadings='Both witnesses replace the continuation region with conventional ellipses and omit the upper duplicated comma.'),
    dict(habit='Continuation can be one continuous dash, a low dot plus dash, or two separated short dash strokes.', places='the indices of214 and the local-system prose formula', scope='Each local form is copied on scan131 rather than normalized to one uniform ellipsis.', misreadings='Both witnesses regularize these graphic forms to dots.'),
    dict(habit='The second letter of p.r./p.v. can have a low v-shaped trough.', places='after simpliciale in the final paragraph', scope='One occurrence on scan131 remains uncertain; no universal identification is asserted.', misreadings='C supplies r; H expands the phrase. The visible v-shaped candidate is placed first.'),
    dict(habit='Double quotation marks are paired high strokes.', places='pour mémoire; dépendance simpliciale', scope='Both quotations on scan131 were inspected.', misreadings='H uses guillemets at both locations.'),
    dict(habit='Strikes can run through nearly all of a small word while leaving a descender, dot and terminal upright.', places='au fait in the margin; pourra at the right edge of the local-system line', scope='Both cancellations remain locally doubtful.', misreadings='H leaves the margin unread and gives provient certainly in the other cancellation; neither is used to force the hidden letters.')
]
notation = [
    dict(notation=r'\Pi_{\Delta_r}=\Pi_1D^*_{\Delta_r}', meaning_or_form='Definition of the degree-simplex groupoid; capital Pi and starred D.', places='first display'),
    dict(notation=r'\widetilde\Pi_{\unsure{\Delta}_r}=\Pi_1P^*_{\Delta_r}', meaning_or_form='Definition of the tilde groupoid; the left Delta is overtraced and locally doubtful.', places='first display'),
    dict(notation=r'\widetilde\Pi_{\Delta_r}\longrightarrow\Pi_{\Delta_r}', meaning_or_form='A single rightward map with a complete visible head, no hook or terminal bar.', places='(213)'),
    dict(notation=r'T_{\Delta_r}', meaning_or_form='Named as the local system giving the asserted extension and then identified with the degree-indexed systems.', places='extension sentence and paragraph after214'),
    dict(notation=r'\Pi_{d_0,d_1,,\text{--},d_r}', meaning_or_form='Literal upper right subscript in214; duplicated comma and a continuous continuation dash are retained.', places='(214), upper row'),
    dict(notation=r"\Pi_{d,d'}=\Pi_1D^*_{d,d'},\quad\Pi_{d'}=\Pi_1D^*_{d'}", meaning_or_form='The two groupoids in the stated absence of a natural morphism; both D forms are starred, with distinct primes in the subscripts.', places='last prose baseline')
]
abbreviations = [
    dict(form='fond.', expansion='fondamental (in groupoïde fond.)'),
    dict(form=r'\unsure{p.v.|p.r.}', expansion='p.r. would expand as par rapport; the second written letter remains ambiguous and no expansion replaces it in the transcription'),
    dict(form='p. ex.', expansion='par exemple')
]

second_boxes = []
def box(kind, coords, reading):
    second_boxes.append(dict(box=f'B{len(second_boxes)+1:02d}', kind=kind,
                             coords=coords, reading=reading))
box('doubtful formula', [245,65,1605,365], formula212)
box('different words', CROPS['donc']['box'], 'donc on a')
box('number', [250,495,1165,640], diagram213)
box('different words', CROPS['memoire']['box'], "Notons ``pour mémoire''")
box('number', CROPS['formula214']['box'], formula214)
box('margin note', CROPS['margin_cancel']['box'], r'\margin{\deleted{\unsure{au fait}}}')
box('struck passage', CROPS['cancelled_verb']['box'], r'\deleted{\unsure{pourra}}')
box('different words', CROPS['live_verb']['box'], r"\unsure{s'identifiant|s'identifie}")
box('number', [270,1770,1295,1905], local_formula)
box('low confidence departure', CROPS['simpliciale']['box'], r'''Les $\Pi_{\Delta_r}$ n'ont pas de ``dépendance
simpliciale'' \unsure{p.v.|p.r.} aux $\Delta_r$, p. ex. on n'a''')
box('number', CROPS['lastline']['box'], lastline)
box('margin note', CROPS['footer130']['box'], r'\margin{130}')

unresolved = [
    'The final digit of the first label remains212|217; numbering continuity does not resolve its shape.',
    'The lower left Delta in that display is overtraced. The final triangular reading is tentative and the earlier strokes cannot be assigned a complete separate letter.',
    'The crossed left-margin phrase remains au fait uncertain; no extra question mark is supplied.',
    'The crossed right-hand word remains pourra uncertain; the obscured strokes do not securely eliminate H’s provient.',
    'M1295 remains undecided: s’identifiant is first, s’identifie remains possible because the terminal sequence is compressed.',
    'The abbreviation retains p.v.|p.r.; its expected expansion does not decide the v-shaped letter.',
    'The last parenthesis is open and the sentence ends with the visible fragment (par; continuation beyond this scan is not supplied.'
]
deletion_checks = [
    dict(span=r'\margin{\deleted{\unsure{au fait}}}', finding='A single long slanted stroke crosses the complete marginal phrase. The tall f-like descender, final t-like stroke and intervening dot survive; the phrase stays doubtful. No separate question mark is recoverable.'),
    dict(span=r'\deleted{\unsure{pourra}}', finding='The strong horizontal strike crosses the word at the right edge and extends slightly beyond it. The preceding Pi expression remains outside the cancellation. The underlying letters are not all separable, so the existing doubt stays.'),
    dict(span=r"\unsure{s'identifiant|s'identifie}", finding='The following line is live and not struck. Its terminal crossed/raised letter is part of the letter form, not a horizontal cancellation through the whole word.'),
    dict(span=r'\widetilde\Pi_{\Delta_r}', finding='In the lower row of the first display the Delta subscript is overtraced with extra interior/upper strokes. It is marked locally doubtful, but no complete earlier letter can be isolated as a deleted glyph.'),
    dict(span='all remaining text and mathematical rows', finding='Every other word, number, Greek letter, index, prime, star, relation, quote and punctuation mark was read directly from the page. No interlinear insertion or additional legible cancellation was found. The single ordinary map has one complete rightward head; the apparent margin drawing is cancelled text, not a diagram.')
]

report = dict(scan=131, reader='reader_b', line_count=16, rows=rows,
              decisions=decisions, inventory=inventory, doubts=doubts,
              notes=notes, check_events=check_events, hand_log=hand_log,
              notation=notation, abbreviations=abbreviations,
              second_boxes=second_boxes, unresolved=unresolved,
              deletion_insertion_checks=deletion_checks)
allowed_kinds = {'misread word','misread symbol or index','omission',
    'text not on the page','deletion state (struck given live or live given struck)',
    'insertion or placement','abbreviation expanded or spelling modernised',
    r'readable ink left as \ill{}','drawing or diagram','other'}
assert all(r['kind'] in allowed_kinds for r in rows)
assert {d['id'] for d in decisions} == {'M1295'}
assert all(r['against_C'] or r['against_H'] for r in rows)
for item in rows + decisions:
    assert (ROOT / 'edition' / item['crop']).is_file(), item['crop']
for item in second_boxes:
    x0,y0,x1,y1=item['coords']
    assert 0 <= x0 < x1 <= 1691 and 0 <= y0 < y1 <= 2360, item
assert len(re.findall(r'(?<!\\)\{', proposed)) == len(re.findall(r'(?<!\\)\}', proposed))
assert proposed.count(r'\[') == proposed.count(r'\]') == 2
assert proposed.count('$') % 2 == 0
assert proposed.count(r'\begin{tikzcd}') == proposed.count(r'\end{tikzcd}') == 1
(OUT / '147_scan131_proposed.tex').write_text(proposed)
(OUT / '147_scan131_report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
print(json.dumps(dict(scan=131, rows=len(rows), decisions=len(decisions),
    resolved=sum(d['decision']!='undecided' for d in decisions), crops=len(CROPS),
    second_boxes=len(second_boxes), inventory=len(inventory), doubts=len(doubts),
    against_C=sum(r['against_C'] for r in rows), against_H=sum(r['against_H'] for r in rows))))
