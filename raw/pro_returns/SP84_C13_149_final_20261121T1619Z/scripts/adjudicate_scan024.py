"""One-use serialization of root's personally inspected scan024 decisions.

Reader A implements the saved root directive; this script does not read images,
choose readings, alter frozen inputs, or compile TeX.
"""
from pathlib import Path
from datetime import datetime, timezone
import copy
import csv
import hashlib
import json

from write_adjudications import write

ROOT = Path(__file__).resolve().parents[1]
STEM = '149_scan024'
REPORT = ROOT / f'reviews/{STEM}.json'
PAGE = ROOT / f'pages/{STEM}.tex'
CHOICES = ROOT / f'second/{STEM}_audit_choices.json'
DIRECTIVE = 'documentation/root_directive_scan024_20261121_1542.md'


def rows(path):
    with path.open() as stream:
        return list(csv.DictReader(stream, delimiter='\t'))


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


assert not CHOICES.exists(), 'One-use script: choices already exist.'
assert not (ROOT / f'second/{STEM}_adjudications.tsv').exists()
report_before = json.loads(REPORT.read_text())
assert report_before['root_approved'] and not report_before.get('audited')
report = copy.deepcopy(report_before)
page_before = PAGE.read_text()
page = page_before
first = {x['box']: x['reading'] for x in rows(ROOT / f'second/{STEM}_first.tsv')}
second = {x['box']: x['reading'] for x in rows(ROOT / f'second/{STEM}_second.tsv')}
boxes = {x['box']: x for x in rows(ROOT / f'second/{STEM}_boxes.tsv')}
different = {x['box'] for x in rows(ROOT / f'second/{STEM}_token_differences.tsv')}
frozen_paths = [ROOT / f'second/{STEM}_{tail}' for tail in (
    'boxes.tsv', 'first.tsv', 'second.tsv', 'token_differences.tsv',
    'comparison_provenance.json', 'crop_manifest.tsv', 'second_notes.md')]
frozen_before = {str(p.relative_to(ROOT)): sha(p) for p in frozen_paths}
choices = {}


def decide(box, evidence, final=None, crop=None):
    item = {
        'selection': 'first' if final is None else 'custom',
        'evidence': evidence,
        'changed': 'no' if final is None else 'yes',
        'personally_inspected': True,
        'inspected_by': 'root',
        'directive': DIRECTIVE,
    }
    if final is not None:
        item['final'] = final
    if crop:
        item['crop'] = crop
    choices[box] = item


new_map = r'\inserted{se plonge par un $i:Y\unsure{-|\longrightarrow}G$ un groupe algébrique commutatif $G$}'
new_nested = r'\inserted{\unsure{irred|(irred)}}'
new_condition = r'\inserted{et $X$ \deleted{normal} '+new_nested+r' et si $f$ ou $g$ est dominant}'
old_condition = first['b09']
assert old_condition in first['b08']
new_item_b = first['b08'].replace(old_condition, new_condition)
old_margin_end = r'\unsure{dominantes|dominant}.}'
new_margin_end = r'\unsure{dominantes|dominant} \unsure{$k$|$K$}.}'
assert old_margin_end in first['b12']
new_lower_note = first['b12'].replace(old_margin_end, new_margin_end)
new_cancelled = r'\deleted{\unsure{$f_1$|$\pi_1$|$f$} est}'

decide('b01', "The title has an independent underline, paired high quotation ticks and a colon. The heavily retraced terminal return in Corollaire and the closed return after géométrique can include a final s, but neither ending is settled. Retain both singular/plural doubts; underline syntax and quotation representation do not settle those endings.")
decide('b02', "Corollaire has its own underline. The following 1 is a straight tall stroke, lies outside that underline, and has no separate terminal stop. Both readings agree on the word and numeral; the underline commands differ only in representation.")
decide('b03', "The insertion occupies two rows above the baseline sur un. The stops after t and f are separate; réduits and connexes remain live. The long attachment stroke leads into the baseline and is not an opening parenthesis. The independent answer scopes only the insertion; retain the unchanged visible baseline context outside its wrapper.")
decide('b05', "The complete formula has separate low 1s in both mapped terms and both group arguments. The paired shafts have two heads; the f/g, X/Y and colon are retained. The independent answer adds neighboring prose and ends within that prose; the assigned formula agrees and is retained without completing the clipped context.")
decide('b06', "A strike crosses the whole est ... extension d'... phrase and obscures the small article endings. The ext...ion sequence is sufficiently readable to retain extension, while une/un and d'une/d'un remain uncertain. The second reading changes certainty rather than recovering an additional cancelled phrase.")
decide('b07', "Par has a p-descender with a closed head, low a and short r ending. In the next row only one un precedes groupe: there is no separate en, so remove that supplied word. The i:Y-to-G shaft ends in a single upturn, without a securely separable two-branch head; retain dash/arrow uncertainty. The raised terminal G has a rounded body and internal return matching the G in the map. The enclosing stroke is an insertion leader, not a textual parenthesis, and the terminal G remains resolved.", new_map)
decide('b08', "The main item retains the qualified Artin reading; ou has two joined bowls. The cancelled article remains tentative. The short fibrée/fibrées word does not have the full fibrations run; both succession endings remain open. Des has a d ascender, courbes remains qualified where overlapped, and anabéliennes has the b/l ascenders, dotted i and accent. The overlapping insertion is adjudicated in b09/b10: retain et, cancelled normal, irred with uncertain enclosing parentheses, and no comma after dominant. This box changes only through that shared insertion.", new_item_b)
decide('b09', "The first short word has a low loop and tall t return, supporting et rather than de. Every letter body of normal is readable beneath the horizontal strike. The lower replacement has a dotted i, paired r strokes, e and terminal d, without an independent stop. A curved arc above it and the tall curve at its right may enclose irred in parentheses or belong to the replacement leader, so retain irred/(irred) rather than assert punctuation. The long lower attachment stroke extends toward the cusp before alors. Its terminal hook after dominant is not an independent comma, and the tall curve does not establish a separate opening parenthesis before et si. Remove the comma and preserve the insertion before alors.", new_condition)
decide('b10', "The horizontal strike crosses the legible normal. The raised/lower replacement irred is present, although the independent target answer names only the cancelled word. Its possible enclosing parentheses remain qualified for the same arc/leader reason recorded in b09; do not turn the legible cancelled normal into an unresolved word.", r'\deleted{normal} '+new_nested)
decide('b11', "In the rotated whole note the opening is Ce cas n'est, and the following prouvé qu'en has the q descender rather than pour. Car. 0 is present; pour les courbes and the positive-characteristic formula retain their local doubts. The later wording concerns the structure du pi_1, not centralisateurs; the parenthetical labels, et même and the final centres des pi_1 remain as qualified in the first reading. The separate double-underlined b) has a loop and is not Si. The long oblique strike supports cancellation of the paragraph, but the lowest rows are not each crossed separately; retain the outer uncertainty over deletion scope. The independent shorter answer does not justify omitting the rest of the note.")
decide('b12', "The opening Une conjecture forte établirait l'unicité des morphismes and X irréductible remain readable. The short quantifier group retains tentative quels plus one unreadable small unit; it does not support expanding que soient les. Applications f,g is retained, while sans/faut les supposer and dominantes/dominant remain local doubts. Dark strokes on the last word follow its letter joins and rises; there is no independent continuous cancellation traversing that word, so it remains live. After it a separate glyph has an upright, forked junction and right branch, followed by a distinct point. The descender from above passes to its left and does not account for the whole glyph. Add that separate k/K under case uncertainty, then the stop. Root and the documented post-comparison consultation agree on this addition; the consultation is not a new independent audit.", new_lower_note)
decide('b13', "En fait has no separate following comma. Both H signs have low 1s with angled caps and feet, rather than n; the coefficient Z signs have the repeated doubled stroke and ell. The crossed exp-like tail remains unsure, not silently completed or dropped. The two full homology expressions and their indices are retained.")
decide('b14', "Démonstration has a separate underline and no following stop. The two underline commands represent the same reading.")
decide('b15', "The a is a small angular loop with retracing confined to the letter. There is no independent cancellation through it. Retain the clear live a and its baseline context.")
decide('b16', "The cancelled short word has a separate i dot and a tall looped l, supporting il rather than cela. The inserted l'existence has clear x and t strokes, and revient follows on the baseline. Preserve the deletion and insertion as separate states.")
decide('b17', "The added clause reads remplaçant Y par G et and its leader attaches before the baseline en choisissant. The long curve is a leader, not a parenthesis. The independent answer scopes only the insertion; retain en choisissant as unchanged following context.")
decide('b18', "The two quotation pairs around origine are short raised ticks, rendered as paired backticks and apostrophes. Straight quote characters in the independent answer are a representation difference, not different source words.")
decide('b19', "The complete f(a)=g(a)=0 formula has both equalities and the rounded zero. The independent reading includes neighboring prose but stops in a clipped qu... group outside the assigned formula. Retain the formula without completing that clipped context here.")
decide('b20', "Both pi forms have separate low 1s, and f, g, parentheses and equality are clear. The independent answer merely includes the preceding l'hyp. context; the formula itself agrees.")
decide('b21', "The cancelled cluster has a large f-like loop and descender, shorter stem/roof traces, and a low 1 that may overlap retracing. These strokes do not securely separate f_1, pi_1 and f. Retain the favored f_1 and both alternatives within one cancelled cluster, followed by est. Do not invent two chronological correction layers where the overwriting cannot be recovered.", new_cancelled)
decide('b22', "Both H subscripts have low 1s with angled caps and feet, not n. The two doubled Z signs and ell indices match the other homology equality on this page. The independent comma is neighboring context beyond this formula-only first reading; the full page already retains it after the equality.")
decide('b23', "The insertion reads ell premier à car. without an independent la. The apparent tall l continues through the insertion leader into the lower baseline's ascender; no separate a body precedes car. The dot between i and e, the final e-like form and stop favor i.e., but the compact sequence retains ici as an alternative. The following dash is one written stroke represented by two TeX hyphens. Retain the original attachment after the homology equality and the final il suffit.")

assert set(choices) == different
assert {k for k,v in choices.items() if v['changed']=='yes'} == {'b07','b08','b09','b10','b12','b21'}


def replace_once(old, new):
    global page
    assert page.count(old) == 1, (old, page.count(old))
    page = page.replace(old, new, 1)


replace_once(first['b07'], new_map)
replace_once(old_condition, new_condition)
replace_once(first['b12'], new_lower_note)
replace_once(first['b21'], new_cancelled)

changes = {x['id']:x for x in report['changes']}


def update_change(id, box, final, **extra):
    b = boxes[box]
    changes[id].update(final=final, evidence=choices[box]['evidence'],
        crop=choices[box].get('crop', f'crops/{STEM}_second_{box}.png'),
        box=[int(b[k]) for k in ('x0','y0','x1','y1')], **extra)


update_change('c07', 'b07', r'$i:Y\unsure{-|\longrightarrow}G$', confidence='medium')
update_change('c08', 'b07', r'un groupe algébrique commutatif $G$', against_C=True)
update_change('c15', 'b09', new_nested, confidence='medium')
update_change('c16', 'b09', new_condition, confidence='medium', against_C=True)
update_change('c20', 'b12', new_lower_note, confidence='medium', against_C=True)
update_change('c29', 'b21', new_cancelled, confidence='low')

for d in report['decisions']:
    if d['id']=='M1039':
        d['evidence']="The raised terminal G has a rounded upper body and internal return matching the map's G. It is a separate letter, not the enclosing insertion leader. Root retained this resolved reading in independent adjudication b07; the nearby arrowhead uncertainty does not affect the G."
    elif d['id']=='M1048':
        d['evidence'] += " Root's audit retains this word live: the dark retracing follows its letter bodies without an independent continuous cancellation. A separate uncertain k/K and a stop follow it."

for d in report['doubts']:
    if d['place']=='Proof, cancelled f':
        d.update(reading='$f_1$', alternatives=[r'$\pi_1$','$f$'], confidence='low', reason=choices['b21']['evidence'])
    elif d['place']=='Lower-left note, last word':
        d['place']='Lower-left note, word before the terminal k/K'
        d['reason'] += ' The word remains live; the final separate k/K glyph and stop follow it.'
report['doubts'].extend([
    {'place':'Item a, inserted i:Y-to-G link','reading':'-','alternatives':[r'\longrightarrow'],'confidence':'medium','reason':choices['b07']['evidence']},
    {'place':'Item b, enclosure of the nested replacement','reading':'irred','alternatives':['(irred)'],'confidence':'medium','reason':choices['b09']['evidence']},
    {'place':'Lower-left note, final separate glyph','reading':'$k$','alternatives':['$K$'],'confidence':'medium','reason':choices['b12']['evidence']},
])

report['notes'][3] = "S024.1 (transcribed claim, not checked): the corollary begins with two morphisms f,g whose displayed fundamental-group maps are equal as exterior homomorphisms. Item a describes an inserted map of Y into a commutative algebraic group and a translation parameter. The source says a in Y; it is not changed to G. The i:Y-to-G endpoint remains uncertain between shaft and arrow. The lower inserted row has un groupe, without the previously supplied en; its terminal G remains resolved."
report['notes'][4] = "S024.2 (transcribed claim, not checked): item b concerns an elementary variety/name and a short, partly uncertain fibration phrase followed by courbes anabéliennes. The condition on X and dominance is inserted before alors f=g. Normal is legibly cancelled and replaced by irred without a stop; possible parentheses immediately enclosing that short replacement remain doubtful. The terminal hook after dominant belongs to the attachment leader, so no independent comma or separate opening parenthesis before et si is supplied."
report['notes'][6] = "The lower-left note is live and separate from the upper cancellation. Its opening Une conjecture forte établirait l'unicité des morphismes and avec X irréductible are readable. After et, tentative quels plus one unreadable tiny group is retained, without expanding que soient les. Applications f,g remains. The sans/faut and dominantes/dominant ending remain local doubts. Dark retracing follows the last word's letters without an independent continuous strike, so that word is not deleted. A separate forked k/K-shaped glyph and a stop follow it. Root accepted this addition after its own crop inspection and the documented post-comparison consultation; the consultation is not an independent reading."
report['notes'][8] = "S024.4 (transcribed proof opening, not checked): the proof discusses uniqueness of a, replaces cancelled il with l'existence, and adds remplaçant Y par G et before en choisissant. The cancelled cluster before H_1 retains f_1, pi_1 and f as alternatives within one unresolved overwritten unit; no correction chronology is invented. The final ell condition remains attached after the equality and reads à car. without a separate la. The page ends after a dash and doubtful i.e./ici followed by il suffit."
report['notes'][9] = "Quotation marks are paired pen ticks, rendered as two backticks and two apostrophes. The long insertion leaders near sur un, the item-a group, before alors, and before en choisissant are not textual parentheses. Only the small possible enclosure immediately around irred remains qualified. H's editorial observations about the preceding page remain excluded from the source fragment."
report['notes'].append("Independent audit: root personally inspected all 22 differing boxes and directed these adopted readings. Six boxes change: b07, b08, b09, b10, b12 and b21; b08/b09/b10 overlap the same condition insertion and are not three independent textual corrections. The substantive new source changes remove en and a comma and add the terminal k/K glyph; the enclosure and pi alternatives localize uncertainty without new certainty-only witness counts. Reader A serialized root's saved directive without a new visual reading. Frozen first/second readings and comparison inputs remain intact.")

report['hand'][0]['consistency'] = "Verified in the title, the proof's a, and the dark final word of the lower-left note. Retracing follows letter bodies; independent strikes have a different continuous extent."
report['hand'][1]['consistency'] = "Verified above sur un, in the item-a insertion, the condition before alors, before en choisissant and after the prime condition. The hook after dominant is part of the leader; the small enclosure immediately around irred alone remains uncertain."
report['hand'][1]['misread'] = "H supplies parentheses at several leaders and moves the remplaçant clause. C supplies commas after the condition's terminal leader hook and after the final prime-condition leader."
report['hand'][4]['consistency'] = "The upper q-descender overlaps the lower note's quantifier and sans/faut rows. Near the end it passes to the left of a separate forked k/K sign and does not account for that complete glyph."
report['hand'][6]['consistency'] = "Irred is the short replacement beneath normal, without an independent stop. Its nearby arc and right-hand curve may be parentheses or its replacement leader; that enclosure remains qualified."
report['hand'].append({'habit':'A small upturned map endpoint can remain ambiguous between pen return and an arrowhead.','pages':[24],'consistency':'Local to i:Y-to-G; only one terminal upturn is secure.','misread':'Both witnesses give a headed map; the first pass asserted a plain shaft. The independent audit retains the endpoint uncertainty.'})

report['notation'][0].update(written='horizontal i:Y-to-G shaft with one small terminal upturn',rendering=r'$i:Y\unsure{-|\longrightarrow}G$',meaning='map-like expression whose head remains unresolved',evidence='Root adjudication b07: the single upturn does not securely establish a two-branch head; G remains clear.')

inventory = {x['element']:x for x in report['inventory']}
inventory['item_a_replacement']['first_words_or_objects'] = r'se plonge par un $i:Y\unsure{-|\longrightarrow}G$ un groupe'
inventory['item_b_condition']['first_words_or_objects'] = new_condition
inventory['item_b_new_adjective']['first_words_or_objects'] = r'\unsure{irred|(irred)}'
inventory['lower_left_note']['position'] = 'oblique lower-left note beside proof, ending in a separate unsure k/K and stop'
inventory['proof_old_formula_phrase']['first_words_or_objects'] = r'\unsure{$f_1$|$\pi_1$|$f$} est'

for d in report['diff_coverage']:
    if d['row']==9:
        d['reason']='The p-descender and r-ending give par. The complete inserted map retains dash/arrow-head uncertainty, recorded in c07 and audit b07.'
    elif d['row']==10:
        d['reason']='Audit b07 has only un before groupe, so the supplied en is removed. The enclosing curve is an insertion leader, not a textual parenthesis; terminal G remains resolved.'
    elif d['row']==12:
        d['reason'] += ' Audit b09 removes the comma after dominant and qualifies only the small enclosure around irred; b12 adds the separate terminal k/K in the lower note. The full corresponding rows c15, c16 and c20 are synchronized.'
    elif d['row']==21:
        d['reason']=r'The cancelled phrase retains \unsure{$f_1$|$\pi_1$|$f$} est in one unresolved overwritten cluster. The new pi alternative is certainty-only; the ell addition belongs after the equality and remains covered by c30.'

assert len(report['changes'])==len(report_before['changes'])
assert len(report['decisions'])==len(report_before['decisions'])
assert len(report['inventory'])==len(report_before['inventory'])
assert len(report['diff_coverage'])==24
for key in ('checks','audit_boxes','root_reviewed_crops','reader','lines_read'):
    assert report[key]==report_before[key], key

# All changed targets have been built and validated before the first mutation.
assert len(choices)==22 and sum(c['changed']=='yes' for c in choices.values())==6
for box in ('b07','b09','b12','b21'):
    assert choices[box]['final'] in page
assert choices['b08']['final'] in page
assert choices['b10']['final'] in page
assert PAGE.read_text()==page_before and json.loads(REPORT.read_text())==report_before
assert frozen_before=={str(p.relative_to(ROOT)):sha(p) for p in frozen_paths}

CHOICES.write_text(json.dumps(choices,ensure_ascii=False,indent=2)+'\n')
write(24, CHOICES)
PAGE.write_text(page)
REPORT.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
assert frozen_before=={str(p.relative_to(ROOT)):sha(p) for p in frozen_paths}

history=[]
for field in ('changes','decisions','doubts','notes','hand','notation','inventory','diff_coverage'):
    before=report_before[field]; after=report[field]
    for i in range(max(len(before),len(after))):
        old=before[i] if i<len(before) else None
        new=after[i] if i<len(after) else None
        if old!=new:
            history.append({'record':f'{field}[{i}]','before':old,'after':new})
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
auditlog={
    'implemented_utc':now, 'implemented_by':'reader_a', 'visual_adjudicator':'root',
    'directive':DIRECTIVE, 'postcomparison_consultation':'documentation/scan024_postcomparison_consultation.md',
    'changed_boxes':['b07','b08','b09','b10','b12','b21'],
    'overlap_note':'b08, b09 and b10 cover the same nested insertion in overlapping scopes.',
    'page_before_sha256':hashlib.sha256(page_before.encode()).hexdigest(),
    'page_after_sha256':sha(PAGE),
    'history':history,
    'validation':{'frozen_inputs_unchanged':True,'frozen_sha256':frozen_before,
                  'change_history_count_preserved':len(report['changes']),
                  'decision_count_preserved':len(report['decisions']),
                  'no_new_visual_reading_by_implementer':True},
}
(ROOT/'documentation/scan024_implementation_reader_a.json').write_text(json.dumps(auditlog,ensure_ascii=False,indent=2)+'\n')
(ROOT/'documentation/scan024_implementation_reader_a.md').write_text(
    '# Scan024: implementation of root adjudication\n\n'
    f'Implemented: {now}. Visual adjudicator: root; serializer: reader_a.\n\n'
    'The full directive was preserved before checkpoint05 closed. The post-comparison consultation remains advisory evidence, not a replacement independent reading. No new image reading, OCR, external research, or TeX compilation was performed for this implementation.\n\n'
    'Twenty-two differing boxes are adjudicated; six change (b07, b08, b09, b10, b12, b21). The three b08/b09/b10 changes overlap the same condition insertion. The substantive source edits remove en and a comma and add the terminal uncertain k/K. Map-head, irred-enclosure and cancelled-cluster alternatives remain localized. The upper marginal deletion scope remains qualified.\n\n'
    'The complete before-and-after report history, page hashes and frozen-input hashes are in scan024_implementation_reader_a.json. The 32 historical change records, 10 mark decisions, 23 inventory elements and 24 difference-coverage rows are retained; three new local doubts are added. finish_audit.py will validate the preserved comparison inputs and log completion with reader_b as the independent reader.\n')
print(json.dumps({'scan':24,'choices':len(choices),'changed_boxes':6,'metadata_records_updated':len(history),'frozen_inputs_unchanged':True}))
