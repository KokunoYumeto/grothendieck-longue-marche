from pathlib import Path
import json
import re
from collections import Counter

ROOT = Path('/workspace/scratch/481648fc487b/SP90_C13_150_work')
PACKET = Path('/workspace/scratch/481648fc487b/reader_packets/150_scan038')
OUT = ROOT / 'reader_returns'
C = (PACKET / 'C.tex').read_text()
H = (PACKET / 'H.tex').read_text()

tex = r'''\scanpage{38}
Il n'y a pas de différence essentielle avec
le traitement fait ici. Plus tard on
généralisera cette notion de stratification
cylindrique (globale) en une notion de
stratification cylindrique locale --- et ce sera
la même \unsure{théorie}.

9. \uline{Description d'une} \deleted{structure}
\inserted{stratification} \uline{cônique} \uline{de type} \(I\)
(\(I\) un ordonné fini).

Pour simplifier, on prend \inserted{d'abord} le cas où on
ne se donne pas de stratifications cylin-\\
driques sur \(X\) par dessus le marché.

\deleted{\unsure{Soit}}

\margin{37}
'''

crop_data = {}
for p in sorted((ROOT / 'crops').glob('150_scan038_*.json')):
    c = json.loads(p.read_text())
    assert (ROOT / 'crops' / c['file']).is_file(), c
    crop_data[p.stem.removeprefix('150_scan038_')] = c

def crop(name):
    c = crop_data[name]
    return {'crop': c['file'], 'box': c['box']}

changes = []
def change(place, c, h, final, evidence, name, confidence, kind, error_kind,
           change_C, change_H, marked_in_H=False, companions=()):
    row = dict(place=place, C=c, H=h, final=final, evidence=evidence,
               confidence=confidence, kind=kind, error_kind=error_kind,
               marked_in_H=marked_in_H, change_C=change_C, change_H=change_H,
               consequential='')
    row.update(crop(name))
    if companions:
        row['additional_crops'] = [crop(n) for n in companions]
    changes.append(row)

change('line 1, différence', 'différence', 'difficulté', 'différence',
       'The crop shows d, the dotted i, two conspicuously tall f strokes, and the low é-r-ence continuation. The additional tall l/t structure needed for difficulté is absent. This is a reading of the strokes, not a preference for the idiom.',
       'difference', 'high', 'misread word', 'words', False, True)

change('end of line 1 and beginning of line 2, avec le traitement',
       'avec\nle traitement', 'au traitement', 'avec\nle traitement',
       'The line-end word has the small a body, a separate v-like turn and the low ec ending; it is longer than au. At the next line the tall looped l and following e of le are explicit before traitement. The companion crop records that second part of this cross-line disagreement.',
       'avec', 'high', 'misread word', 'words', False, True,
       companions=('le_traitement',))

change('line 2, punctuation after tard', 'Plus tard on', 'Plus tard, on',
       'Plus tard on',
       'There is no separate comma after the final d of tard. The small next baseline mark belongs to the compressed o of on, followed by its low n stroke.',
       'plus_tard_on', 'high', 'text not on the page', 'text not on page',
       False, True)

change('lines 5–6, end of the opening paragraph',
       'et ce sera\nla même \\unsure{théorie}.',
       r'et \ill{} \ill{} \ill{}\ldots',
       'et ce sera\nla même \\unsure{théorie}.',
       'The first crop gives the separate words et ce sera; the companion gives la même and the final word. La and même, including its circumflex, are readable. In the last word the tall initial strokes and compressed medial cluster permit théorie but do not separate every letter, so that C doubt remains. A single terminal period is visible, not an ellipsis. H’s three illegibility placeholders cover this whole ending; they are not treated as a one-to-one count of manuscript words.',
       'et_ce_sera', 'medium', r'readable ink left as \ill{}',
       'readable ink left as illegible', False, True, True,
       companions=('la_meme_theorie',))

heading = r'''9. \uline{Description d'une} \deleted{structure}
\inserted{stratification} \uline{cônique} \uline{de type} \(I\)
(\(I\) un ordonné fini).'''
change('lines 7–8, extent of heading underlining', heading,
       r"9. \emph{Description d'une \struck{structure} \add{stratification} cônique de type $I$} ($I$ un ordonné fini).",
       heading,
       'Separate underline strokes belong to Description d’une, cônique and de type. The capital I after type is outside the last underline. The crossed structure and its replacement stratification are not part of one continuous underlined span. H’s emphasis wrapper encompasses all these words and I; the difference here is the visible scope, not the wrapper’s spelling. The heading correction crop separately records the strike and replacement.',
       'heading_type_I', 'high', 'other', 'other', False, True,
       companions=('heading_correction',))

plural_mark = r'\unsure{stratifications cylindriques|stratification cylindrique}'
plural_reading = 'stratifications cylin-\\\\\ndriques'
change('lines 10–11, plural endings and written cylin-/driques break',
       plural_mark, 'stratifications cylindriques', plural_reading,
       'The terminal flat runs and their small downward returns favor final s on both stratifications and driques, though the letters are compressed; the plural is selected with medium confidence from those endings, not from grammatical agreement. The word cylindriques is physically split: a distinct short horizontal hyphen follows cylin at the right end of line 10, and driques begins line 11. Both witnesses join the word and omit that written hyphen. The proposed source keeps the hyphen and forces its line break.',
       'stratifications_cylindriques', 'medium', 'other', 'other', True, True)

phrase_mark = r'\unsure{par dessus le marché|pour donner des ennuis}'
change('line 11, par dessus le marché', phrase_mark,
       r'\uncertain{par dessus le marché}', 'par dessus le marché',
       'Par has the long descending p and a short low ar continuation. Dessus has the looped initial d, compressed e, a separate angular s and a low ending. Le is separate; marché shows the low initial run, tall h and final accented e. These strokes do not support pour donner des ennuis. No hyphens are written in par dessus. This resolves C’s alternative; H already supplies the same words, so clearing H’s uncertainty alone is not counted as a substantive H change.',
       'par_dessus_le_marche', 'high', 'misread word', 'words', True, False,
       True)

change('line 12, heavily cancelled word', r'\deleted{\unsure{Soit}}',
       r'\struck{\ill{}}', r'\deleted{\unsure{Soit}}',
       'An initial capital S curve and the final tall t with a cross stroke survive the cancellation. The middle is crossed by several thick oblique strokes and is not independently legible letter by letter. Soit remains a tentative reading inside the deletion; it is not promoted to certainty. H leaves the entire word illegible.',
       'cancelled_Soit', 'medium', r'readable ink left as \ill{}',
       'readable ink left as illegible', False, True, True)

change('bottom-left foliation', r'\margin{37}', '[absent]', r'\margin{37}',
       'The pale lower-left numeral has the two lobes of 3 and the descending, crossed stroke of 7. The number is clear; its thinner ink and isolated position do not establish that it is the author’s own pagination.',
       'folio37', 'high', 'omission', 'omissions', False, True)

marks = []
def mark(m, context, decision, reading, evidence, name, confidence):
    row = dict(mark=m, context=context, decision=decision, reading=reading,
               evidence=evidence, confidence=confidence)
    row.update(crop(name))
    marks.append(row)

mark(r'\unsure{théorie}', r'la même \unsure{théorie}.', 'undecided',
     r'\unsure{théorie}',
     'Tall initial strokes followed by an S-shaped compressed cluster, a small point-like body and a low terminal stroke permit théorie. They do not isolate every letter. No positive alternative is established from the ink; the original one-reading doubt is retained.',
     'la_meme_theorie', 'medium')
mark(plural_mark, 'ne se donne pas de ' + plural_mark, 'first', plural_reading,
     'Both endings have extended low terminal runs with small returning/downward strokes, consistent with the plural s seen in the page’s compressed word endings. The reading is medium confidence. The written line-end hyphen between cylin and driques is clear and is preserved separately from the choice of number.',
     'stratifications_cylindriques', 'medium')
mark(phrase_mark, r'sur \(X\) ' + phrase_mark + '.', 'first',
     'par dessus le marché',
     'The descending p, looped initial d of dessus, separate le, and the tall h and accented ending in marché distinguish the first candidate from the second. All four words are readable on the crop.',
     'par_dessus_le_marche', 'high')
mark(r'\unsure{Soit}', r'\deleted{\unsure{Soit}}', 'undecided',
     r'\unsure{Soit}',
     'S and final t survive, while the center is covered by several heavy oblique cancellation strokes. The rule requiring every letter to be plain before resolving a struck doubt is not met.',
     'cancelled_Soit', 'medium')

inventory = [
    dict(element='T01', kind='text', position='top; principal lines 1–6',
         first_words_or_objects="Il n’y a pas de différence essentielle avec", sheet_kind='text',
         hand='his hand', transcribed='yes'),
    dict(element='T02', kind='text', position='upper-middle; principal lines 7–8',
         first_words_or_objects='9. Description d’une … cônique de type I (I un ordonné fini).',
         sheet_kind='text', hand='his hand', transcribed='yes'),
    dict(element='D01', kind='deletion', position='line 7, between d’une and cônique',
         first_words_or_objects='structure', sheet_kind='text', hand='his hand', transcribed='yes'),
    dict(element='I01', kind='insertion', position='above the cancelled structure in line 7',
         first_words_or_objects='stratification', sheet_kind='text', hand='his hand', transcribed='yes'),
    dict(element='T03', kind='text', position='principal lines 9–11',
         first_words_or_objects='Pour simplifier, on prend …', sheet_kind='text',
         hand='his hand', transcribed='yes'),
    dict(element='I02', kind='insertion', position='above line 9, attached after prend and before le',
         first_words_or_objects='d’abord; curved placement leader pointing to the gap after prend',
         sheet_kind='text', hand='his hand', transcribed='yes'),
    dict(element='D02', kind='deletion', position='principal line 12; isolated below paragraph',
         first_words_or_objects=r'\unsure{Soit}', sheet_kind='text',
         hand='his hand', transcribed='yes'),
    dict(element='M01', kind='margin note', position='bottom-left paper edge',
         first_words_or_objects='37', sheet_kind='text',
         hand='thin grey foliation; attribution uncertain', transcribed='yes'),
]

doubts = [
    dict(place='line 6, final word of opening paragraph', reading=r'\unsure{théorie}',
         alternatives='No competing full word is established; the compressed medial and terminal strokes leave the supplied candidate uncertain.', confidence='medium'),
    dict(place='line 12, cancelled word', reading=r'\deleted{\unsure{Soit}}',
         alternatives='Soit is tentative because the central letters remain obscured by cancellation.', confidence='medium'),
]

notes = [
    'Reported content only: the author says that the present global cylindrical-stratification notion will later be generalized to a local one, with the same remaining doubtful final word (théorie). Section 9 begins a description of a conical stratification of finite ordered type I, initially without additional cylindrical stratifications on X. No mathematical proof or validity check was performed.',
    'Twelve principal manuscript lines were read, plus two inserted words and the lower-left foliation. The lower portion after the isolated cancelled word is blank apart from 37. There is no visible author page number at the head.',
    'The written cylin- / driques division is preserved with a literal hyphen and a forced TeX line break. The plural reading is selected with medium confidence from the terminal strokes; grammatical agreement is not used as deciding evidence.',
    'The d’abord placement mark curves beneath the inserted word and bends down-left to a small terminal point in the gap after prend. It is an insertion leader, not a parenthesis, strike or mathematical figure. Its attachment is encoded by the position of the inserted word and inventoried separately from the paragraph. No independent mathematical drawing or diagram occurs.',
    'Structure is crossed out and stratification is written above it. The latter is live. Description d’une, cônique and de type have separate underline spans; the type letter I is not underlined.',
    'Foliation 37 is clear but written in thinner grey strokes than the main text. Its attribution is not established; it is retained as a margin entry, not assigned to the author’s own numbering.',
    'The spellings cônique and par dessus, the visible accents, and the absence of a comma after tard are retained. The two opening-paragraph occurrences of cylindrical-stratification wording and the agreed (globale) were read directly rather than accepted by agreement of witnesses.',
    'H’s opening note, generated section heading and final explanatory note are editorial material and are excluded from the transcription and collation counts. Its -- versus C’s --- is treated as a dash-encoding difference, not a substantive finding.',
    'Whole image and both native halves were visually read once. Fourteen distinct cropped places produced fourteen saved crop images, all visually inspected. No OCR, external research, TeX compilation, other-page reading or mathematical check was performed.',
    'The first-reader return contains both unresolved C doubts in place. Recovery of the legible portion of H’s paragraph ending and the tentative crossed Soit does not assert that their remaining doubtful letters have been settled.',
    'Second-reading boxes cover all complete coherent content wholly inside their coordinates. The broad heading box deliberately includes the following first paragraph line because the d’abord insertion lies beside the heading’s second line. The last two paragraph lines are likewise given in full in their shared box.',
]

notation = [
    dict(form='I', meaning_or_shape='Serif capital I, with separate upper and lower horizontal bars. Here the parenthesis explicitly calls it a finite ordered set; no interval meaning is supplied by this leaf.', places='heading de type I and following parenthesis, line 8'),
    dict(form='X', meaning_or_shape='Crossed freehand capital X, used for the underlying space in the final live line. No dot, index or accent is visible.', places='line 11, sur X'),
]

hand_log = [
    dict(habit='Very low linked letters may reduce to flat runs or small separate point-like bodies; these are not automatically punctuation or absent letters.',
         places='avec; globale; on after tard; sera; par dessus le marché',
         consistent='Repeated on this leaf; some taller letters remain separately formed.',
         witness_errors='H reads au for avec, supplies a comma after tard, and leaves readable words in the paragraph ending as illegible.'),
    dict(habit='Long f ascenders/descenders and their cross strokes distinguish a word’s structure even when the intervening letters are compressed.',
         places='différence; stratification and stratifications; fini',
         consistent='All inspected occurrences have conspicuous tall f strokes, with different degrees of linkage.',
         witness_errors='The double-f structure followed by a low ending supports différence against H difficulté.'),
    dict(habit='Terminal s can merge into an extended low run with a small downward return; an internal s may instead be a separate angular, reversed curve.',
         places='dessus; stratifications; line-broken driques',
         consistent='The internal/terminal contrast is visible here; the two plural endings remain a medium-confidence reading.',
         witness_errors='C marks singular/plural alternatives; H supplies the plural. The actual endings favor the plural without relying on grammar.'),
    dict(habit='An insertion may be placed above the line with a curved leader; its path determines attachment independently of the word reading.',
         places='d’abord above the gap after prend',
         consistent='One such leader on this page; the separate heading replacement is directly above its cancelled predecessor.',
         witness_errors='Both witnesses place d’abord correctly; no new placement error established.'),
    dict(habit='Capital I has distinct upper and lower bars and is not part of a neighboring underline.',
         places='de type I; I un ordonné fini',
         consistent='Both occurrences on this leaf.',
         witness_errors='H’s broad emphasis wrapper also encompasses the first I, which has no manuscript underline.'),
]

first_para_line = r"Pour simplifier, on prend \inserted{d'abord} le cas où on"
last_two_lines = 'ne se donne pas de ' + plural_reading + r' sur \(X\) par dessus le marché.'
second_boxes = [
    dict(box='b01', kind='C/H word difference', coords=[880,25,1198,160],
         reading='différence', reason='Complete differing word, including the long f descenders; H difficulté.'),
    dict(box='b02', kind='C/H word difference', coords=[1505,65,1640,148],
         reading='avec', reason='Line-end component of the avec le / au disagreement.'),
    dict(box='b03', kind='C/H word difference', coords=[330,140,850,250],
         reading='le traitement', reason='Complete words inside the box, including the next-line le suppressed by H’s contraction au.'),
    dict(box='b04', kind='C/H word difference', coords=[1215,130,1635,239],
         reading='Plus tard on', reason='Complete phrase containing H’s supplied comma; on is read as a whole word.'),
    dict(box='b05', kind='C/H word difference', coords=[1250,417,1640,509],
         reading='et ce sera', reason='First complete words in the opening-paragraph ending replaced by H illegibility spans.'),
    dict(box='b06', kind='C/H word difference', coords=[330,532,853,616],
         reading=r'la même \unsure{théorie}.', reason='Whole final line, including the unresolved C word and the single terminal period.'),
    dict(box='b07', kind='insertion|struck passage|handwritten number|C/H word difference',
         coords=[325,615,1665,982], reading=heading + '\n\n' + first_para_line,
         reason='Full heading and the following first prose line: section number 9, struck structure, replacement stratification, the entire parenthesis with both I occurrences, all underline scopes, and the d’abord insertion with its attachment after prend. No reading is restricted to just the numeral or the insertion while other complete text is inside.'),
    dict(box='b08', kind='C/H word difference|low-confidence departure',
         coords=[338,940,1663,1202], reading=last_two_lines,
         reason='All complete content in the last two live paragraph lines; covers the medium-confidence selection of plural endings, the written line-end hyphen, and the resolved par dessus le marché alternative. The full inline X expression is included.'),
    dict(box='b09', kind='struck passage', coords=[419,1205,524,1296],
         reading=r'\deleted{\unsure{Soit}}', reason='Entire isolated cancelled word, retaining its unresolved central letters.'),
    dict(box='b10', kind='margin note|handwritten number', coords=[22,2303,82,2358],
         reading=r'\margin{37}', reason='Complete thin foliation numeral at the bottom-left edge.'),
]

result = dict(scan=38, reader='reader_a', line_count=12, changes=changes,
              marks=marks, inventory=inventory, doubts=doubts, notes=notes,
              check_events=[], notation=notation, abbreviations=[],
              hand_log=hand_log, second_boxes=second_boxes,
              crop_count=14, cropped_place_count=14,
              crops=[dict(file=c['file'], box=c['box'], rotation_degrees=c['rotation_degrees'],
                          viewed=True) for c in crop_data.values()])

def norm(s):
    return re.sub(r'\s+', ' ', s).strip()

for row in changes:
    assert norm(row['C']) in norm(C), ('C quotation', row['place'])
    assert row['H'] == '[absent]' or norm(row['H']) in norm(H), ('H quotation', row['place'])
    assert norm(row['final']) in norm(tex), ('final change', row['place'], repr(row['final']))
for row in marks:
    assert row['mark'] in C and row['context'] in C, ('C mark/context', row)
    assert norm(row['reading']) in norm(tex), ('final mark', row)
for row in second_boxes:
    assert norm(row['reading']) in norm(tex), ('second-box reading', row['box'])
    x0, y0, x1, y1 = row['coords']
    assert 0 <= x0 < x1 <= 1690 and 0 <= y0 < y1 <= 2361

def get_macros(text, name):
    found = []
    start = 0
    token = '\\' + name + '{'
    while (pos := text.find(token, start)) >= 0:
        at = pos + len(token)
        depth = 1
        while depth and at < len(text):
            if text[at] in '{}':
                prior = at - 1
                slashes = 0
                while prior >= 0 and text[prior] == '\\':
                    slashes += 1
                    prior -= 1
                if slashes % 2 == 0:
                    depth += 1 if text[at] == '{' else -1
            at += 1
        assert depth == 0
        found.append(text[pos:at])
        start = at
    return found

assert Counter(get_macros(C, 'unsure') + get_macros(C, 'illegible')) == Counter(m['mark'] for m in marks)
depth = 0
for i, ch in enumerate(tex):
    if ch not in '{}':
        continue
    n = 0
    j = i - 1
    while j >= 0 and tex[j] == '\\':
        n += 1
        j -= 1
    if n % 2:
        continue
    depth += 1 if ch == '{' else -1
    assert depth >= 0
assert depth == 0
assert len(crop_data) == 14

(OUT / '150_scan038.tex').write_text(tex)
(OUT / '150_scan038.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(dict(scan=38, changes=len(changes), changes_C=sum(c['change_C'] for c in changes),
                      changes_H=sum(c['change_H'] for c in changes), marks=len(marks),
                      resolved_C_marks=sum(m['decision'] != 'undecided' for m in marks),
                      inventory=len(inventory), doubts=len(doubts), second_boxes=len(second_boxes),
                      crops=len(crop_data), tex_braces_balanced=True), ensure_ascii=False))
