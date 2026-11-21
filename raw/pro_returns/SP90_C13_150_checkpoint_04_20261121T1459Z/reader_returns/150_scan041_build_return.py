from pathlib import Path
import json
import re

ROOT = Path('/workspace/scratch/481648fc487b/SP90_C13_150_work')
PACKET = Path('/workspace/scratch/481648fc487b/reader_packets/150_scan041')
OUT = ROOT / 'reader_returns'
C = (PACKET / 'C.tex').read_text()
H = (PACKET / 'H.tex').read_text()
TEX = (OUT / '150_scan041.tex').read_text()
cropmeta = {}
for path in sorted((ROOT / 'crops').glob('150_scan041_*.json')):
    item = json.loads(path.read_text())
    cropmeta[path.stem.removeprefix('150_scan041_')] = item

data = dict(scan=41, reader='reader_a', line_count=18, changes=[], marks=[], inventory=[], doubts=[], notes=[], check_events=[], notation=[], abbreviations=[], hand_log=[], second_boxes=[])

def change(place, c, h, final, evidence, crop, confidence, kind, error_kind, change_C, change_H, marked_in_H=False, consequential=''):
    data['changes'].append(dict(place=place, C=c, H=h, final=final, evidence=evidence,
        crop=cropmeta[crop]['file'], box=cropmeta[crop]['box'], confidence=confidence,
        kind=kind, error_kind=error_kind, marked_in_H=marked_in_H,
        change_C=change_C, change_H=change_H, consequential=consequential))

change('line 1, first équivaut cluster', 'équivaut à la donnée', 'équivaut : à la donnée',
    r'équivaut \unsure{à|:} la donnée',
    'There is one two-level cluster between équivaut and la: an upper accent-like fleck and a small lower body. Its shape permits compressed à or a colon. There are not two consecutive clusters corresponding to H’s colon plus à. C receives uncertainty only here.',
    'equivaut_first', 'high', 'text not on the page', 'text not on page', False, True)
change('line 2, word at right paper edge', 'partition', 'partition', r'partit\unsure{i|.}',
    'The surviving run has p, a compressed a/r run, two tall t strokes, and a small detached terminal mark that can be a compressed i or a stop. No readable -on survives at the physical edge. A short low stroke reaches the dark edge; its letter affiliation cannot be established. No completion or editorial ellipsis is supplied.',
    'partition_edge', 'medium', 'text not on the page', 'text not on page', True, True)
change('line 5, cancelled word after Sigma-double-star', r'\deleted{\unsure{et|de}}', r'\struck{\ill{}}', r'\deleted{\unsure{et|de}}',
    'A short cancelled run and a tall terminal stroke remain. They permit C’s et/de alternatives, with et slightly favored by the final upright; the cancellation prevents every letter being read. H leaves the entire run illegible. This is a tentative partial reading, not resolution of the cancelled C doubt.',
    'cancelled_et_de', 'low', r'readable ink left as \ill{}', 'readable ink left as illegible', False, True, True)
change('line 5, au dessus', r'\unsure{au} dessus', 'au-dessus', 'au dessus',
    'The small filled a body is followed by a separate low u. Dessus begins after a space; there is no connecting hyphen. The crop resolves C’s au and shows that H’s hyphen is not written.',
    'au_dessus', 'high', 'abbreviation expanded or spelling modernised', 'abbreviation/spelling', True, True)
change('cancelled Drap formula, surviving stop', r'\deleted{\(\operatorname{Drap}_{\unsure{1|2}}(I)\)}', r'\struck{$\mathrm{Drap}_2(I)$}.',
    r'\deleted{\(\operatorname{Drap}_{\unsure{1|2}}(I)\)}.',
    'The closing parenthesis is followed by a separate uncrossed ink point. The small cancelled subscript remains 1/2: the strike covers the distinguishing portion. Only the missing stop is a substantive C change; uncertainty in H’s subscript is not counted as a separate change.',
    'Drap_cancelled', 'high', 'omission', 'omissions', True, False)
change('line 6, cancelled product', r'\deleted{\(\unsure{I\times I}\)}', r'\struck{$I\times I$}', r'\deleted{\(I\times I\)}',
    'Both serifed capital I forms and the small central crossing survive distinctly from the larger oblique cancelling stroke. Each component of this short formula is readable, so C’s whole-formula doubt is resolved.',
    'product_cancelled', 'high', 'other', 'symbols and indices', True, False)
change('line 6, Sigma convention, right-hand sign', r'\Sigma_{ij}=\varnothing', r'\Sigma_{ij}=\emptyset', r'\Sigma_{ij}=\phi',
    'The sign is a small loop with a long stem, in the handwritten phi form. The literal phi is retained instead of either witness’s normalized empty-set glyph. Its use for the empty set is an interpretation of the convention, not a replacement of the written sign.',
    'convention_Sigma', 'high', 'misread symbol or index', 'symbols and indices', True, True,
    consequential='Preserves the written phi in the convention; its apparent empty-set meaning is recorded in the notation entry.')
change('line 6, end of convention parenthesis', r'\(\Sigma_{ii}=\Sigma_i\)).', r'$\Sigma_{ii}=\Sigma_i$)', r'\(\Sigma_{ii}=\Sigma_i\))',
    'The final parenthesis is visible, followed by a white gap before the edge; no terminal point is present. C supplies a stop that H does not.',
    'convention_Sigma', 'high', 'text not on the page', 'text not on page', True, False)
G01 = r'\margin{\begin{tikzpicture}[baseline=-.3ex]\draw[line width=.5pt] (0,0)--(.45,.12);\end{tikzpicture}}'
change('between lines 7 and 8, detached right-hand stroke', '[absent]', '[absent]', G01,
    'One detached, dark, straight stroke slopes slightly upward to the right. It has neither a head nor another joining stroke. It is reproduced as a graphic-only path at the right, without assigning a map or minus role.',
    'isolated_stroke', 'high', 'drawing or diagram', 'drawings and diagrams', True, True)
change('line 8, source and but quotation marks', "``source'' et ``but''", '« source » et « but »', "``source'' et ``but''",
    'The marks are short high quotation ticks, paired where the pen strokes separate, not angular guillemets. The words source and but are clear.',
    'source_but_quotes', 'high', 'other', 'other', False, True)
change('before line 11, cancelled NB phrase', r'\deleted{\uline{NB} \unsure{le cas}}', r'\struck{\emph{NB} la \ill{}}', r'\deleted{\uline{NB} \unsure{le cas}}',
    'NB and its separate underline are readable. The cancelled following run has a tall l, a compressed vowel body, then a c-like opening and low ending. Le cas remains a tentative reading; the strike does not allow every letter to be established. H’s certain la and wholly illegible final run are not adopted. The C doubt remains.',
    'cancelled_NB', 'low', 'misread word', 'words', False, True, True)
change('line 11, first live word', r'\unsure{car|Comme}', 'Comme', r'\unsure{Cela|Celle}',
    'The crop shows a capital C, a small e-like loop, one conspicuous tall l-loop, and a long low ending with a raised hump. The tall loop excludes car; there is no clear pair of m humps for Comme. Cela is the first reading, with Celle retained because the low ending is compressed. The syntactic awkwardness is not repaired.',
    'Comme', 'medium', 'misread word', 'words', True, True)
change('line 12, graduation and absent la', r'\unsure{graduation}', 'la graduation', 'graduation',
    'The initial g/r/a/d strokes, flattened u/a run, tall t, dotted i, and low on are readable as graduation. The line begins with that g; no separate la precedes it. C’s doubt is resolved, and H’s additional article is omitted.',
    'graduation', 'high', 'text not on the page', 'text not on page', True, True)
change('line 12, et des', 'et des', 'et de', 'et des',
    'After et the looped d is followed by a low e and a distinct terminal s return. C’s des is retained against H’s de.',
    'et_des', 'high', 'misread word', 'words', False, True)
change('line 13, où', r'\unsure{où}', 'où', 'où',
    'An open o and flattened u are accompanied by a detached accent stroke above them. These components resolve the original C doubt.',
    'ou', 'high', 'other', 'words', True, False)
change('above line 13, loc. with raised t', r'\inserted{\unsure{loc.\(^{t}\)}}', r'\add{loc.\textsuperscript{t}}', r'\inserted{loc.\(^{t}\)}',
    'The inserted abbreviation has a looped l, rounded o, open c, separate full point, and raised t. The placement leader descends before un, after b est. C’s reading resolves without expanding the abbreviation.',
    'loc_t', 'high', 'other', 'words', True, False)
change('line 15, final a and possible colon', r'On a de plus \unsure{a}', 'On a de plus', r'On a de plus a \unsure{:}',
    'The final extra a has a closed bowl, short downstroke and foot, and is separate from plus. It is retained literally although the prose is awkward. Two much smaller dark points immediately to its right can be a colon; this punctuation is retained narrowly as doubtful. H omits the a and these points; C’s a is resolved.',
    'on_a_de_plus_a', 'medium', 'omission', 'omissions', True, True)
change('line 17, morphisme identité quotation marks', "``morphisme identité''", '« morphisme identité »', "``morphisme identité''",
    'The opening and closing marks are high quotation ticks, not guillemets; the trailing comma is separate and readable. C’s quotation form is retained.',
    'morphisme_identite_quotes', 'high', 'other', 'other', False, True)
change('lower-left foliation', r'\margin{40}', '[absent]', r'\margin{40}',
    'A thin grey 4 with cross-stroke and a rounded 0 appear at the lower-left edge. They are retained as foliation. Their hand cannot be securely identified with the heavy main writing.',
    'folio40', 'high', 'omission', 'omissions', False, True)

def extract_marks(text):
    found = []
    for match in re.finditer(r'\\(?:unsure|illegible)\{', text):
        start = match.start()
        pos = match.end()
        depth = 1
        while depth:
            if text[pos] == '{' and text[pos-1] != '\\': depth += 1
            if text[pos] == '}' and text[pos-1] != '\\': depth -= 1
            pos += 1
        found.append((text[start:pos], start, pos))
    return found

markrows = [
    ('undecided', r'\unsure{et|de}', 'Cancellation leaves a short low run and a terminal upright, but not every letter; neither alternative is forced.', 'cancelled_et_de', 'low'),
    ('first', 'au', 'A small filled a body and separate low u are plainly present before dessus.', 'au_dessus', 'high'),
    ('undecided', r'\unsure{1|2}', 'The digit is crossed; its surviving hooked/curved lower trace does not separate 1 and 2.', 'Drap_cancelled', 'low'),
    ('first', r'I\times I', 'Both capital I forms and the small multiplication crossing survive independently of the cancellation.', 'product_cancelled', 'high'),
    ('undecided', r'\unsure{le cas}', 'The tall l and low following traces permit le cas but the strike obscures the vowel and terminal letters.', 'cancelled_NB', 'low'),
    ('other', r'\unsure{Cela|Celle}', 'Capital C, small e-loop, tall l-loop and low ending favor Cela/Celle; no visible m pair supports Comme, and the tall loop excludes car.', 'Comme', 'medium'),
    ('undecided', r'\unsure{celle}', 'The c/e body and tall loops are interrupted by the cancellation; the full word is not independently plain.', 'cancelled_celle', 'low'),
    ('first', 'graduation', 'The g/r/a/d beginning, flattened middle, tall t and dotted i support the complete written word; the ending on is visible.', 'graduation', 'high'),
    ('first', 'où', 'Detached accent above an open o and flattened u resolves the reading.', 'ou', 'high'),
    ('first', r'loc.\(^{t}\)', 'Looped l, rounded o, open c, separate point and raised t are independently visible.', 'loc_t', 'high'),
    ('undecided', r'\unsure{bord}', 'The b ascender and final d survive but the central or is blackened by the strike.', 'cancelled_bord', 'low'),
    ('first', 'a', 'A closed bowl with short downstroke and foot follows plus; this extra a is not a stray dot.', 'on_a_de_plus_a', 'high'),
    ('undecided', r'\unsure{-|\longrightarrow}', 'The connector has a tiny blunt terminal wedge/return, but no independently clear open arrowhead; both forms remain possible.', 'identity_formula', 'medium'),
    ('undecided', r'\unsure{-|\longrightarrow}', 'The connector ends in a tiny wedge or blunt return. A short-headed arrow is possible, but a plain stroke cannot be excluded.', 'composition_formula', 'medium'),
]
original_marks = extract_marks(C)
assert len(original_marks) == len(markrows) == 14
for (macro, start, end), (decision, reading, evidence, crop, confidence) in zip(original_marks, markrows):
    context = C[max(0, start-48):min(len(C),end+50)]
    data['marks'].append(dict(mark=macro, context=context, decision=decision, reading=reading,
        evidence=evidence, crop=cropmeta[crop]['file'], box=cropmeta[crop]['box'], confidence=confidence))

def inventory(element, kind, position, first, hand='his hand'):
    data['inventory'].append(dict(element=element, kind=kind, position=position,
        first_words_or_objects=first, sheet_kind='text', hand=hand, transcribed='yes'))

inventory('N01','margin note','upper left, above first principal line','16')
inventory('T01','text','principal lines 1–4','La donnée des Sigma_i équivaut; et d’une partit…; Celle des Sigma_ij')
inventory('D01','display','principal line 2, left and center',r'\Sigma_*\in\mathcal M\quad(\Sigma_*=\coprod\Sigma_i)')
inventory('D02','display','principal line 4, left',r'\Sigma_*\longrightarrow I_{\mathcal M}.')
inventory('T02','text','principal lines 4–6','Celle des Sigma_ij; d’un objet Sigma-double-star au dessus de I×I; on pose')
inventory('S01','deletion','principal line 5, after Sigma-double-star',r'\unsure{et|de}')
inventory('S02','deletion','below principal line 5, left',r'\operatorname{Drap}_{\unsure{1|2}}(I)')
inventory('S03','deletion','principal line 6, before on pose',r'I\times I')
inventory('D03','display','principal line 6, right',r'(on pose \Sigma_{ij}=\phi si i\not\le j,\Sigma_{ii}=\Sigma_i)')
inventory('T03','text','principal lines 7–8','La donnée des; équivaut; de deux morphismes source et but')
inventory('G01','diagram','between principal lines 7–8, center',r'\Sigma_{ij}\hookrightarrow\Sigma_j; downward arrow to \Sigma_i')
inventory('G02','drawing','right side, between principal lines 7 and 8','one detached headless stroke sloping slightly upward to the right')
inventory('G03','diagram','principal line 9 and its lower row',r'\Sigma_{**}\to\Sigma_* labeled underlined b; downward arrow to \Sigma_* labeled underlined s')
inventory('T04','text','principal lines 10–14','compatibles avec les pr_1 et pr_2; Cela|Celle la bigraduation; graduation; où b est')
inventory('S04','deletion','after opening parenthesis before principal line 11',r'\uline{NB} \unsure{le cas}')
inventory('A01','insertion','above principal line 11, after bigraduation and before de Sigma-double-star',r'de type \(I\), with curved placement leader')
inventory('S05','deletion','right end of principal line 11, after est déduite de',r'\unsure{celle}')
inventory('A02','insertion','above principal line 13, after b est and before un',r'loc.\(^{t}\), with curved placement leader')
inventory('S06','deletion','principal line 14, after immersion',r'\unsure{bord}')
inventory('T05','text','principal lines 15–18','On a de plus a; morphisme identité; La donnée des Sigma_ijk revient')
inventory('D04','display','principal line 16',r'\underline{i}:\ \Sigma_*\unsure{-|\longrightarrow}\Sigma_{**}')
inventory('D05','display','principal line 18, right',r'\Sigma_{ijk}\unsure{-|\longrightarrow}\Sigma_{i\unsure{k|n}}')
inventory('N02','margin note','bottom left','40','thin foliation hand; attribution uncertain')

def doubt(place, reading, alternatives, confidence):
    data['doubts'].append(dict(place=place, reading=reading, alternatives=alternatives, confidence=confidence))

doubt('line 1, first équivaut cluster', r'\unsure{à|:}', 'One compressed à or one colon; not H’s two tokens : à.', 'medium')
doubt('line 2, right edge', r'partit\unsure{i|.}', 'The terminal small mark may be compressed i or an abbreviation stop; no -on is supplied.', 'medium')
doubt('line 4, second équivaut cluster', r'\unsure{à|:}', 'Upper dot/accent and lower slanted body permit either compressed à or colon.', 'medium')
doubt('line 5, cancelled word', r'\deleted{\unsure{et|de}}', 'et or de; letters under the strike are not all plain.', 'low')
doubt('cancelled Drap formula', r'\operatorname{Drap}_{\unsure{1|2}}(I)', 'The cancelled numerical subscript may be 1 or 2.', 'low')
doubt('line 7, third équivaut cluster', r'\unsure{à|:}', 'An accent-like upper stroke and a small lower body favor à, but colon remains possible.', 'medium')
doubt('cancelled NB phrase', r'\deleted{\uline{NB} \unsure{le cas}}', 'le cas remains tentative; the compressed vowel could be a, and the final run is crossed.', 'low')
doubt('line 11, first live word', r'\unsure{Cela|Celle}', 'One clear tall l-loop favors Cela; the low joined ending can also support Celle. No grammatical correction is made.', 'medium')
doubt('line 11, cancelled final word', r'\deleted{\unsure{celle}}', 'celle is plausible but individual letters are obscured by the strike.', 'low')
doubt('line 14, cancelled bord', r'\deleted{\unsure{bord}}', 'The ascenders support bord, but the crossed central letters are not independently plain.', 'low')
doubt('line 15, after extra a', r'a \unsure{:}', 'Two tiny dark points can be a colon; no punctuation beyond these points is supplied.', 'medium')
doubt('line 16, identity connector', r'\Sigma_*\unsure{-|\longrightarrow}\Sigma_{**}', 'Blunt-ended stroke versus abbreviated right arrow with a very small head.', 'medium')
doubt('line 18, composition connector', r'\Sigma_{ijk}\unsure{-|\longrightarrow}\Sigma_{i\unsure{k|n}}', 'Blunt-ended stroke versus abbreviated right arrow; target index has a separate narrow k/n doubt.', 'medium')
doubt('line 18, target index', r'\Sigma_{i\unsure{k|n}}', 'The dotted i is clear; the final low joined arch does not independently show both arms of k and can be n. This adds uncertainty only to the witnesses’ ik.', 'medium')
doubt('line 18, after revient', r'revient \unsure{à|:}', 'Upper detached blob and lower looped body favor compressed à but also resemble colon-like punctuation.', 'medium')

data['notes'] = [
    'This is a handwritten text sheet. The heavy main hand numbers it 16 at the upper left; thin lower-left foliation 40 has uncertain attribution. Scan number 41 is editorial, not source ink.',
    'The page reports that the family Sigma_i can be packaged as Sigma_* with a partition of type I, and the family Sigma_ij as Sigma_** over I×I. It reports source and target morphisms, with b locally a boundary morphism and s a fibration, then introduces an identity morphism and begins a composition statement. These are descriptions of the page’s claims only; no mathematical claim has been independently checked.',
    'Eighteen principal writing rows are counted. The lower rows of the two diagrams and the separately positioned cancelled and inserted spans are additionally inventoried, rather than counted as ordinary prose lines.',
    'Whole-page layout and both native-resolution halves were read once, token by token, including agreed text. All 32 saved deep-zoom crops were visually read; there are 32 distinct cropped places and 32 saved crop images, with no replacement crops.',
    'The clipped word after et d’une is retained as partit plus a narrow i/stop alternative. No -on, ellipsis, or expected completion is added. A short low stroke at the dark paper edge has no securely assignable letter value.',
    'All three équivaut clusters and the final cluster after revient contain one two-level mark. Each remains à/colon uncertain. H’s additional separate colon plus à in the first occurrence is excluded; adding uncertainty alone at the other occurrences is not counted as a collation change.',
    'The plain extra a in On a de plus a is legible and retained despite the awkward wording. The two tiny following points are retained as a doubtful colon. The words Cela/Celle la bigraduation are likewise not repaired by syntax.',
    'The one-sided foot of some capital I forms does not establish J. The first product, cancelled product, later I×I, and final I after dans were compared within this page. The central product crossing can have one shortened arm.',
    'The actual convention sign is retained as phi. Its use for the empty set follows the wording of the convention, without replacing the sign by varnothing or emptyset.',
    'The first diagram has a hooked right arrow and an ordinary downward arrow. The second has ordinary right/down arrows with separately underlined b and s. A small detached spot above the first horizontal shaft and a tiny off-baseline blob near the later prose dash have no established label or punctuation role and are not transcribed.',
    'The isolated headless diagonal stroke between the first diagram’s equivalence line and the source/but line is reproduced separately as graphic-only TikZ at the right. Its function is unknown. No running text is placed in a picture.',
    'The de type I insertion has a curved placement leader ending after bigraduation, before de Sigma-double-star; it is not an underline. The loc.-raised-t insertion attaches after b est and before un. The insertion macros encode these attachments; the leaders are placement marks, not additional mathematical relations.',
    'The cancelled Drap, I×I, NB phrase, celle, bord, and et/de are treated separately. Cancelled I×I is fully readable. Et/de, the Drap index, le cas, celle and bord remain doubtful under the strict cancelled-letter rule.',
    'The identity and composition connectors can be short-headed arrows, but the minute terminal wedges do not securely exclude plain strokes. The final target index’s low arch remains k/n uncertain. No formula is corrected from the expected identity or composition role.',
    'H’s editorial note about the upper page number and its document terminator are excluded from source transcription and from source quotations. Its emph/NB macro is treated as an underline equivalent, not an independent error.',
    'Six original C doubts are resolved to the first reading; one is revised from car/Comme to the still-doubtful Cela/Celle; seven remain undecided. All fourteen original marks are recorded. The proposed page contains fifteen narrow doubt marks.',
    'No mathematical check event is recorded: this work is a diplomatic reading. No OCR, external research, other-page reading, or TeX compilation was used.'
]

data['notation'] = [
    dict(form=r'\Sigma_i,\Sigma_*,\Sigma_{**}', meaning_or_shape='Sigma is a broad angular capital; one and two low star marks distinguish the packaged objects. The stars can be compressed to two or three prongs.', places='throughout, both diagrams and identity formula'),
    dict(form=r'\Sigma_*=\coprod\Sigma_i', meaning_or_shape='The written coproduct sign has two uprights on a shared lower bar. The page packages the family Sigma_i in Sigma-star.', places='principal line 2'),
    dict(form=r'\phi', meaning_or_shape='Handwritten loop-and-stem phi, apparently used for the empty set; literal symbol retained.', places='Sigma_ij convention on line 6'),
    dict(form=r'I,\ I\times I', meaning_or_shape='Serif capital I has a variable lower foot, sometimes hooked to the left. The product cross may have a shortened arm. These local shapes do not securely identify J or a different operator.', places='top product, cancelled product, pr_1/pr_2 clause'),
    dict(form=r'\underline b,\underline s,\underline i', meaning_or_shape='Separate short underlines appear beneath the diagram/morphism letters. The page calls b but, s source and i morphisme identité.', places='second diagram and subsequent prose; identity display'),
    dict(form=r'\Sigma_*\unsure{-|\longrightarrow}\Sigma_{**}', meaning_or_shape='Short connector with minute blunt terminal wedge; dash/abbreviated-arrow ambiguity is retained.', places='identity display; analogous composition connector on last line'),
    dict(form=r'\Sigma_{i\unsure{k|n}}', meaning_or_shape='The last target has a dotted i followed by a low joined arch; the second arm expected for k is not independently clear.', places='final composition formula')
]
data['abbreviations'] = [
    dict(form='i.e.', expansion='id est'),
    dict(form='NB', expansion='nota bene'),
    dict(form=r'loc.\(^{t}\)', expansion='localement'),
    dict(form=r'\operatorname{pr}', expansion='projection'),
    dict(form=r'\operatorname{Drap}', expansion='drapeau (operator name; written form is not expanded in the transcription)'),
    dict(form=r'partit\unsure{i|.}', expansion='partition is the likely intended word; the surviving written fragment is not completed')
]
data['hand_log'] = [
    dict(habit='A small a body can be nearly a filled point; with a separate upper accent, à can resemble a colon.', places='au dessus; three équivaut clusters; final revient cluster; On a de plus', consistent='Clear au and extra a are readable; the four two-level clusters remain uncertain rather than forced into a single punctuation reading.', witness_errors='H supplies : à at the first équivaut although only one cluster is written; other à/colon differences remain unresolved.'),
    dict(habit='Capital I has variable feet, including a leftward hooked foot that can resemble J.', places='top I×I, cancelled I×I, lower I×I and I after dans', consistent='All these occurrences retain I; the hook alone does not securely distinguish another letter on this page.', witness_errors='None established from the hooked foot.'),
    dict(habit='A low i can merge with a preceding capital’s foot while its dot stays detached; j has a longer hooked descent.', places='Sigma indices throughout and both diagrams; pr_1/pr_2 clause', consistent='Most indices remain clear; the final target’s following low letter remains k/n uncertain.', witness_errors='The added final-index doubt is certainty-only against both witnesses.'),
    dict(habit='A long low word body may hide several compressed letters, while a tall l-loop remains conspicuous.', places='live Cela/Celle; graduation; loc.-raised-t; top Celle comparisons', consistent='Cela/Celle retains uncertainty in its ending; graduation and loc.-raised-t are sufficiently separated on their crops.', witness_errors='Both witnesses’ Comme is unsupported by the conspicuous tall l; C doubts on graduation and loc.-raised-t resolve.'),
    dict(habit='A short arrow head can be only a small terminal return; no paired arrowhead is required.', places='both diagrams and the two final horizontal connectors', consistent='The diagram arrows have readable direction; the final connectors have less distinct blunt wedges and remain doubtful.', witness_errors='H’s certain final arrows are not treated as substantive errors solely because uncertainty is added.'),
    dict(habit='Raised t and a separate full point mark the abbreviation loc.-raised-t.', places='insertion above b est un', consistent='One occurrence on this page, with each component readable.', witness_errors='C’s original abbreviation doubt resolves without expansion.'),
    dict(habit='Cancellation strokes can preserve ascenders but hide the letters between them.', places='et/de, Drap subscript, NB phrase, celle, bord; contrast cancelled I×I', consistent='Only cancelled I×I is fully resolved; the five affected text/index places retain narrow doubts.', witness_errors='Certain H readings of cancelled bord/celle and Drap_2 are not adopted as certainty, but uncertainty-only differences are not counted as errors.')
]

def second(kind, coords, reading, reason):
    data['second_boxes'].append(dict(box=f"b{len(data['second_boxes'])+1:02d}", kind=kind, coords=coords, reading=reading, reason=reason))

second('handwritten number|margin note', [49,24,119,95], r'\mspage{16}', 'Complete upper handwritten page number.')
second('C/H word difference|low-confidence departure', [892,68,1257,174], r'équivaut \unsure{à|:} la', 'First équivaut cluster and complete coherent words inside the crop; H has an extra separate colon token.')
second('low-confidence departure', [1185,170,1673,272], r"et d'une partit\unsure{i|.}", 'Whole surviving right-edge phrase; both witnesses complete partition.')
second('C/H word difference|low-confidence departure', [1200,369,1641,490], r'équivaut \unsure{à|:} celle', 'Second whole equivalence phrase; unresolved à/colon difference.')
second('struck passage|C/H word difference|low-confidence departure', [977,512,1127,577], r'\deleted{\unsure{et|de}}', 'Complete cancelled word; H leaves it wholly illegible.')
second('C/H word difference', [1134,510,1508,582], 'au dessus de', 'Complete surviving phrase, including no written hyphen; resolves C au.')
second('struck passage|doubt formula|handwritten number', [278,569,504,649], r'\deleted{\(\operatorname{Drap}_{\unsure{1|2}}(I)\)}.', 'Whole cancelled Drap formula, doubtful numerical subscript and surviving final stop.')
second('struck passage', [267,632,450,709], r'\deleted{\(I\times I\)}', 'Whole separately cancelled product; C whole-formula doubt resolves.')
second('doubt formula', [510,600,1668,721], r'(on pose \(\Sigma_{ij}=\phi\) si \(i\not\le j\), \(\Sigma_{ii}=\Sigma_i\))', 'Complete convention formula and parenthesis, including the literal phi and absence of a terminal stop; included as a coherent mathematical check box for the nearby disputed sign.')
second('C/H word difference|low-confidence departure', [1224,730,1622,834], r'équivaut \unsure{à|:} celle', 'Third equivalence phrase with the unresolved à/colon difference.')
second('margin note', [1437,820,1526,881], G01, 'Complete isolated nonverbal stroke at the right; reproduced without assigning a relation role.')
second('C/H word difference', [1002,925,1485,1016], "``source'' et ``but''", 'Complete quoted names; handwritten high ticks differ from H guillemets.')
second('insertion|struck passage|handwritten number|C/H word difference|low-confidence departure', [205,1332,1635,1698],
    r'compatibles avec les \(\operatorname{pr}_1\) et \(\operatorname{pr}_2\) de \(I\times I\) dans \(I\) (\deleted{\uline{NB} \unsure{le cas}} \unsure{Cela|Celle} la bigraduation \inserted{de type \(I\)} de \(\Sigma_{**}\) est déduite de \deleted{\unsure{celle}} graduation de type \(I\) de \(\Sigma_*\), et des \(\underline b\) et \(\underline s\)) ---',
    'Complete three-row block, including numerical pr subscripts, cancelled NB phrase, whole live clause, de type I insertion and attachment, cancelled celle, graduation without la, et des, and closing parenthesis/dash. The broad box avoids fragment-only readings of the crowded insertion and deletions.')
second('insertion|C/H word difference', [238,1670,1100,1818], r'où \(\underline b\) est \inserted{loc.\(^{t}\)} un morphisme bord', 'Whole coherent portion containing où and the loc.-raised-t insertion, with every complete word inside this box.')
second('struck passage', [593,1830,735,1902], r'\deleted{\unsure{bord}}', 'Complete cancelled bord; unresolved under the strict cancelled-letter rule.')
second('C/H word difference|low-confidence departure', [242,1935,947,2023], r'On a de plus a \unsure{:}', 'Whole phrase, including the clear additional a and tentative colon.')
second('doubt formula', [656,2016,1196,2110], r'\underline{i}:\ \Sigma_*\unsure{-|\longrightarrow}\Sigma_{**}', 'Entire identity formula, not just its uncertain connector; includes underlined i, colon and all stars.')
second('C/H word difference', [205,2108,797,2205], "``morphisme identité'',", 'Whole quoted phrase and trailing comma.')
second('doubt formula|C/H word difference|low-confidence departure', [1004,2190,1658,2296], r'\(\Sigma_{ijk}\unsure{-|\longrightarrow}\Sigma_{i\unsure{k|n}}\) revient \unsure{à|:}', 'Entire final formula, including connector and target-index doubts, followed by the whole final word and its à/colon cluster.')
second('handwritten number|margin note', [19,2292,77,2350], r'\margin{40}', 'Complete thin lower-left foliation; hand attribution remains uncertain.')

data['crop_register'] = [dict(place=name, file=item['file'], box=item['box'], reader_viewed=True, phase='first') for name,item in cropmeta.items()]
data['crop_counts'] = dict(distinct_places=32, saved_images=32, viewed_images=32)
data['coverage'] = dict(whole_viewed_once=True, top_native_half_viewed_once=True, bottom_native_half_viewed_once=True,
    every_agreed_token_read=True, every_deletion_and_insertion_read=True, original_C_marks=14,
    original_C_marks_resolved=6, original_C_marks_revised_still_doubtful=1, original_C_marks_retained=7,
    proposed_doubt_marks=15, first_reading_complete=True)

norm = lambda s: ' '.join(s.split())
for row in data['changes']:
    for witness in ('C','H'):
        if row[witness] != '[absent]':
            assert norm(row[witness]) in norm(C if witness=='C' else H), (row['place'], witness, row[witness])
    assert norm(row['final']) in norm(TEX), (row['place'], row['final'])
    assert (ROOT/'crops'/row['crop']).exists()
for row in data['marks']:
    assert row['mark'] in C and row['context'] in C
    assert norm(row['reading']) in norm(TEX)
    assert (ROOT/'crops'/row['crop']).exists()
for item in cropmeta.values():
    assert (ROOT/'crops'/item['file']).exists()
assert len(cropmeta)==32
assert len(extract_marks(TEX))==15
depth=0
for i,char in enumerate(TEX):
    if char=='{' and (i==0 or TEX[i-1]!='\\'): depth+=1
    if char=='}' and (i==0 or TEX[i-1]!='\\'): depth-=1
    assert depth>=0
assert depth==0
dest=OUT/'150_scan041.json'
dest.write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n')
print(json.dumps(dict(output=str(dest), changes=len(data['changes']), C_changes=sum(x['change_C'] for x in data['changes']), H_changes=sum(x['change_H'] for x in data['changes']), marks=len(data['marks']), inventory=len(data['inventory']), doubts=len(data['doubts']), second_boxes=len(data['second_boxes']), crops=len(cropmeta)),ensure_ascii=False))
