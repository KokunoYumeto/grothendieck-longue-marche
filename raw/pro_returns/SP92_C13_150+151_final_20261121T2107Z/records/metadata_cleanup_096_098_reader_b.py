"""Synchronize current metadata with recorded blind-audit decisions; no new ink decisions."""
from pathlib import Path
import copy
import hashlib
import json
from datetime import datetime, timezone

W = Path('/workspace/scratch/d7279cb02214/SP92_C13_150+151_work')
PAGES = ('150_scan096', '150_scan097', '150_scan098')
LOG = W / 'records/metadata_cleanup_096_098_reader_b.json'
assert not LOG.exists(), 'This scoped cleanup has already been logged.'
sha = lambda data: hashlib.sha256(data).hexdigest()
paths = {p: W / 'records' / f'{p}.json' for p in PAGES}
raw = {p: paths[p].read_bytes() for p in PAGES}
before = {p: json.loads(raw[p]) for p in PAGES}
current = copy.deepcopy(before)
notes = {p: json.loads((W / 'second' / f'{p}_root_crop_notes.json').read_text()) for p in PAGES}
adjudications = {p: json.loads((W / 'second' / f'{p}_adjudications.json').read_text()) for p in PAGES}

# Read-only byte fingerprints: page text, historical reading tables, and adjudication evidence.
fixed_files = []
for p in PAGES:
    fixed_files.extend([
        W / 'pages' / f'{p}.tex',
        W / 'records' / f'{p}.tex',
        W / 'second' / f'{p}_first.tsv',
        W / 'second' / f'{p}_second.tsv',
        W / 'second' / f'{p}_root_crop_notes.json',
        W / 'second' / f'{p}_adjudications.json',
    ])
assert all(p.is_file() for p in fixed_files)
fixed_hashes = {str(p.relative_to(W)): sha(p.read_bytes()) for p in fixed_files}

protected_names = {
    'C', 'H', 'C_item', 'C_text', 'H_text', 'c', 'h',
    'first', 'second', 'first_reading', 'second_reading',
    'second_boxes', 'audit_changes', 'witness_errors',
}
def protected_values(value, path=()):
    result = {}
    if isinstance(value, dict):
        for key, item in value.items():
            if key in protected_names or key.startswith('witness_'):
                result[path + (key,)] = copy.deepcopy(item)
            else:
                result.update(protected_values(item, path + (key,)))
    elif isinstance(value, list):
        for index, item in enumerate(value):
            result.update(protected_values(item, path + (index,)))
    return result

allowed_roots = {
    'deletion_insertion_review', 'inventory', 'notes', 'diff_coverage',
    'changes', 'doubts', 'decisions', 'notation', 'hand_log',
    'review_status', 'validation',
}
edits = []
def setv(page, path, value, reason, boxes=()):
    assert path[0] in allowed_roots
    assert not any(part in protected_names for part in path if isinstance(part, str))
    container = current[page]
    for part in path[:-1]:
        container = container[part]
    key = path[-1]
    old = copy.deepcopy(container.get(key) if isinstance(container, dict) else container[key])
    if old == value:
        return
    container[key] = value
    edits.append({
        'page': page, 'path': '/'.join(map(str, path)), 'reason': reason,
        'audit_boxes': list(boxes),
        'before': old if len(json.dumps(old, ensure_ascii=False)) < 350 else {
            'sha256': sha(json.dumps(old, ensure_ascii=False).encode()), 'characters': len(str(old))
        },
        'after': value if len(json.dumps(value, ensure_ascii=False)) < 350 else {
            'sha256': sha(json.dumps(value, ensure_ascii=False).encode()), 'characters': len(str(value))
        },
    })

def by_id(page, collection, ident):
    key = 'diff_id' if collection == 'diff_coverage' else 'id'
    matches = [i for i, row in enumerate(current[page][collection]) if row[key] == ident]
    assert len(matches) == 1, (page, collection, ident)
    return matches[0]

def change(page, ident, field, value, reason, boxes=()):
    setv(page, ('changes', by_id(page, 'changes', ident), field), value, reason, boxes)

def diff(page, ident, field, value, reason, boxes=()):
    setv(page, ('diff_coverage', by_id(page, 'diff_coverage', ident), field), value, reason, boxes)

def replace_once(text, old, new):
    assert text.count(old) == 1, ('Expected one exact metadata passage', old[:100], text.count(old))
    return text.replace(old, new, 1)

# 096: cancelled V terms, broadened local doubts, and resolved bornera.
p = '150_scan096'
rev = {
    2: {
        'state': 'struck V term; index remains ij/j uncertain',
        'bounds': 'Only the cancelled V term precedes live si; neither enfin nor si is cancelled.',
        'reading': notes[p]['B08']['final'],
    },
    3: {
        'place': 'Before live comme/aura',
        'state': 'struck old start; d/donc/On unresolved',
        'bounds': 'The compact old group alone is cancelled; the following comme/aura group and V formula remain live.',
        'reading': r'\deleted{\unsure{d|donc|On}}',
    },
    4: {
        'state': 'struck V_i term, resolved',
        'bounds': 'Only V_i between pour and i<j is cancelled; the inequality remains live.',
        'reading': notes[p]['B11']['final'],
    },
}
for index, fields in rev.items():
    box = {2:'B08',3:'B09',4:'B11'}[index]
    for field, value in fields.items():
        setv(p, ('deletion_insertion_review',index,field), value,
             'Align the current revision description with the audited term/state.', (box,))
for index, fields in {
    8: {'element':'Cancelled V term after enfin', 'first_words_or_objects':r'V_{\unsure{ij|j}} (cancelled)'},
    9: {'element':'Cancelled old start before comme/aura', 'first_words_or_objects':'d | donc | On (uncertain, cancelled)'},
    10:{'element':'Cancelled V_i before i<j', 'first_words_or_objects':'V_i (cancelled)'},
    12:{'first_words_or_objects':'mais on se bornera …'},
}.items():
    box = {8:'B08',9:'B09',10:'B11',12:'B13'}[index]
    for field, value in fields.items():
        setv(p, ('inventory',index,field), value, 'Remove a superseded current inventory reading.', (box,))
setv(p, ('doubts',2,'place'), 'Cancelled old start before comme/aura',
     'The following live word remains a two-reading doubt.', ('B09',))
change(p, 'C12', 'place', 'Cancelled start immediately before comme/aura',
       'Match the current live-word uncertainty without changing witness fields.', ('B09',))
for ident, ids, reason, boxes in (
    ('D0700',['C34'],'The cancellation after enfin is a V term; the ij/j subscript remains uncertain. The audited correction is recorded in C34.',('B08',)),
    ('D0702',['C35'],'The cancelled term before i<j is V_i, resolved in the blind audit and recorded in C35.',('B11',)),
    ('D0703',['C36'],'The exposed r shoulder and final a resolve bornera. C36 records the audited reading; no pending borne/bornera doubt remains.',('B13',)),
):
    diff(p,ident,'change_ids',ids,'Connect current coverage to the existing audited correction.',boxes)
    diff(p,ident,'reason',reason,'Replace superseded or pending coverage language.',boxes)
diff(p,'D0692','reason',
     'The short group remains et/tt uncertain; neither alternative supplies H’s comma-plus-si sequence.',
     'Do not describe the audited local doubt as a certified et.',('B02',))
diff(p,'D0701','reason',
     'The cancelled start remains d/donc/On uncertain; the following live group separately remains comme/aura uncertain. C12 records the current cancelled reading.',
     'Preserve both uncertainties recorded by the audit.',('B09',))
n = current[p]['notes']
n = replace_once(n,
    'These areas remain in the blind reread set.',
    'The recorded blind audit retains these clipped readings without completing off-page letters.')
old = n[n.index('There are five canceled groups in the main text:'):n.index('\n\nThe star after the main-text protopos')]
new = (
    'There are five cancelled groups in the main text: the uncertain old verb between on and aura; '
    'the resolved et immediately after the first phi; a cancelled V term after enfin with an unresolved ij/j index; '
    'an old d/donc/On group before the separately uncertain live comme/aura; and the resolved cancelled V_i before i<j. '
    'The first group is not a live trouve followed by a second deletion as H parses it. Both live aura occurrences in the earlier cases remain independent of their strikes. '
    'The blind audit replaced the earlier short-word hypotheses after enfin and before i<j with the V terms. '
    'The old verb and old d/donc/On interiors remain uncertain. No strike extends into the following live formula or replacement.'
)
n = replace_once(n, old, new)
n = replace_once(n,
    'The whole expression remains in the blind reread set.',
    'The recorded blind audit retains this whole expression and its medium-confidence directed-limit reading.')
n = replace_once(n,
    'They do not decide whether the written limit mark is an underline or arrow, or the uncertain verb ending: those remain visual questions.',
    'They do not decide the written limit mark or the letters of the verb. The recorded visual audit retains the directed-limit reading at medium confidence and resolves the verb as bornera.')
setv(p, ('notes',), n, 'Remove stale revision readings and pending verb language from current prose.', ('B08','B09','B11','B13','B20'))

# 097: exact continuation shapes, annotation scope, and marche-/raient.
p = '150_scan097'
setv(p, ('deletion_insertion_review',2,'attachment'),
     'After the live X_i_n* and before alors followed by the unresolved on a/point-rule-point group; physically above the long cancelled formula, ending without a comma.',
     'Do not certify the audited doubtful words after alors.', ('B03','B05'))
setv(p, ('deletion_insertion_review',2,'evidence'),
     current[p]['deletion_insertion_review'][2]['evidence'] +
     ' The recorded audit places h above the parentheses around the wave; the first crowded label remains uncertain.',
     'State the audited label-parenthesis scope in the current insertion review.', ('B03',))
setv(p, ('inventory',9,'first_words_or_objects'),
     r'alors; \unsure{on a|point-rule-point}',
     'Carry the current local word/mark uncertainty into the inventory.', ('B05',))
setv(p, ('inventory',17,'first_words_or_objects'),
     'NB la définition et les deux formules marche- / raient encore...',
     'Replace superseded ront in the current inventory.', ('B12',))
setv(p, ('notation',0,'sign'),
     r'i_0,\mathord{\cdot}\mathord{-},i_n / i_0\mathord{\cdot}\mathord{-}i_n',
     'Record the audited point-and-rule shapes, not two dot glyphs.', ('B02','B06','B09'))
setv(p, ('notation',0,'reading'),
     'One point followed by one horizontal rule; commas occur only around the first (99) continuation.',
     'Make shape as well as count explicit.', ('B02','B06','B09'))
setv(p, ('notation',0,'evidence'),
     'Recorded audit: (99), (100) and the i-indexed generalization term have point-rule; the J-indexed generalization term has point-rule-point.',
     'Use the recorded audited distinctions.', ('B02','B06','B09'))
setv(p, ('notation',1,'sign'),
     r'J_0\prec\mathord{\cdot}\mathord{-}\prec I_n',
     'Replace the old typographic two-dot shorthand.', ('B10',))
setv(p, ('notation',1,'reading'),
     'The written flag ends in capital I_n and its continuation is one point followed by a rule.',
     'Preserve both audited letter and continuation shape.', ('B10',))
setv(p, ('notation',4,'sign'),
     r'\overset{\overset h{(\sim)}}{\hookrightarrow}',
     'Place h outside and above the parentheses enclosing the wave.', ('B06','B14','B15'))
setv(p, ('notation',4,'reading'),
     'Hooked arrow labeled by h above short parentheses enclosing a separate wave.',
     'Align the current notation wording with the audited scope.', ('B06','B14','B15'))
setv(p, ('hand_log',0,'scope'),
     'On this leaf, the audited i-index chains and flag have point-rule; the V_J chain has point-rule-point.',
     'Replace count-only shorthand with the occurrence-specific audited shapes.', ('B02','B06','B09','B10'))
m = by_id(p,'decisions','M0728')
setv(p, ('decisions',m,'reading'), current[p]['changes'][by_id(p,'changes','C09')]['final'],
     'Synchronize the current C-mark decision with the audited first-label scope.', ('B03',))
setv(p, ('decisions',m,'ink'),
     current[p]['decisions'][m]['ink'] + ' The recorded audit places h above parentheses around the wave, while retaining uncertainty in this crowded first label.',
     'Preserve the uncertainty with its corrected parenthesis scope.', ('B03',))
m = by_id(p,'decisions','M0729')
setv(p, ('decisions',m,'reading'), r'marche-\\' + '\nraient',
     'Replace the superseded current word decision.', ('B12',))
setv(p, ('decisions',m,'ink'), notes[p]['B12']['evidence'],
     'Use the existing audit’s dotted-i evidence; no fresh image reading.', ('B12',))
change(p,'C26','final',current[p]['changes'][by_id(p,'changes','C34')]['final'],
       'Align the earlier current change row with the audited final reading.',('B12',))
change(p,'C26','evidence',
       'The first line retains marche- with an independent hyphen. The recorded blind audit identifies an independent i dot in the following raient run before encore. The current reading is marche- / raient; the earlier ront hypothesis is superseded.',
       'Replace evidence that still asserted the superseded verb ending.',('B12',))
change(p,'C26','superseded_by','C34',
       'Document the existing same-locus first-pass/audit overlap without deleting rows or recounting.',('B12',))
change(p,'C11','evidence',
       'The closing curved parenthesis is followed by clear paper; no separate comma precedes the transition to alors and its following unresolved word/mark group.',
       'Avoid treating the audited on a/marks ambiguity as certain prose.',('B03','B05'))
change(p,'C14','evidence',
       current[p]['changes'][by_id(p,'changes','C14')]['evidence'] +
       ' The recorded blind audit separately leaves the following low group on a/point-rule-point uncertain; this does not weaken the identification of the raised question.',
       'Explain the current uncertainty present in this row’s final field.',('B05',))
for ident in ('D0718','D0719'):
    diff(p,ident,'reason',
         'The Z superscript is serialized before or after the same index. Independent point-rule continuation corrections are recorded in C01–C03, not inferred from this macro difference.',
         'Make current continuation evidence consistent with the audited shapes.',('B02',))
for ident in ('D0729','D0730'):
    diff(p,ident,'reason',
         'The Z superscript in (100) is serialized in a different order. The point-rule continuation at each index is independently corrected in C15–C16.',
         'Make current continuation evidence consistent with the audited shapes.',('B06',))
diff(p,'D0752','reason',
     'The diagram serializations shift the middle object and lower equality. H omits the separate wave in each homotopy label; the audited labels place h above parentheses around that wave. C29–C30 record these current label readings.',
     'Include the audited parenthesis scope in current difference coverage.',('B15',))
n = current[p]['notes']
n = replace_once(n, '**marche- / ront encore**', '**marche- / raient encore**')
n = replace_once(n,
    'There are two continuation marks in all three (99) indices, in both (100) indices, in the i-indexed V in the generalization paragraph, and between the two precedence signs of the written flag. The J-indexed V in that paragraph has three marks.',
    'A point followed by a longer rule occurs in all three (99) indices, both (100) indices, the i-indexed V in the generalization paragraph, and between the two precedence signs of the written flag. The J-indexed V in that paragraph has point-rule-point.')
n = replace_once(n,
    'The tilde beneath h is a separate mark wherever it is clear, not merely H’s (h) label.',
    'Where clear, h stands above the short parentheses enclosing a separate wave; the parentheses do not enclose h. The first crowded label remains uncertain.')
n = replace_once(n,
    'The two-line NB visibly divides **marche-** and **ront**, with an independent line-end hyphen. This resolves C’s marchent doubt to another reading; neither the tense nor the division is silently smoothed.',
    'The two-line NB divides **marche-** and **raient**, with an independent line-end hyphen and a visible i dot in the second line. The blind audit supersedes the earlier ront hypothesis. C’s marchent doubt is resolved to this written split form without smoothing the tense or division.')
n = replace_once(n,
    'The small independent question above alors is separated from the l ascender; no detached lower dot is exposed.',
    'The small independent question above alors is separated from the l ascender; no detached lower dot is exposed. The following low group remains on a/point-rule-point uncertain in the recorded audit.')
setv(p, ('notes',), n, 'Synchronize current prose with the audited verb, continuations, labels, and local word doubt.', ('B02','B03','B05','B06','B09','B10','B12','B14','B15'))
setv(p, ('review_status',),
     'Root finalized and blind audit completed; current metadata synchronized with the recorded adjudications.',
     'Remove the obsolete awaiting-root-finalization status.')
setv(p, ('validation','second_box_readings_check_scope'),
     'The candidate-substring check was a first-pass validation before the blind audit; the original second_boxes readings are preserved unchanged.',
     'Clarify the historical scope of a pre-audit validation without altering sealed first readings.')

# 098: bracket geometry and the newly recorded word/case doubts.
p = '150_scan098'
setv(p, ('deletion_insertion_review',1,'state'),
     'cancelled; et/Et and letter certainty unresolved',
     'Make the audited case doubt explicit in current revision metadata.', ('B02',))
setv(p, ('deletion_insertion_review',1,'evidence'),
     'The small looping word is under dense crossing strokes; its case remains et/Et uncertain. The strike does not reach the following paragraph.',
     'Align the current evidence with the existing audit.', ('B02',))
setv(p, ('deletion_insertion_review',4,'attachment'),
     'A square-ended lower bracket lies immediately beneath V_J cap X_L^*. Two upright equality bars link it to the lower V_J^{X_L^*}.',
     'Describe the audited grouping shape without changing the protected C_item.', ('B03',))
setv(p, ('deletion_insertion_review',4,'evidence'),
     'The lower bracket has a flat middle and short upturned ends, with no central cusp. The two comparison bars are live. The short word after the lower V term remains avec/en uncertain; notation (102) forms the next baseline.',
     'Remove the obsolete certified avec reading and state the bracket geometry.', ('B03',))
setv(p, ('deletion_insertion_review',7,'evidence'),
     current[p]['deletion_insertion_review'][7]['evidence'] +
     ' The short preceding group remains au/horizontal-rule uncertain, and the following word remains lieu/lien uncertain.',
     'Include the audited local word/mark doubts in the current proposal review.', ('B04',))
setv(p, ('deletion_insertion_review',8,'evidence'),
     'A square-ended lower bracket has a flat middle and short upturned ends, without a central cusp. It groups the intersection; the lower V_{j,l} label includes a separate comma between j and l.',
     'State the audited geometry without changing the protected witness underbrace field.', ('B05',))
setv(p, ('inventory',7,'first_words_or_objects'),
     r'\Vert; V_J^{X_L^*}\text{ \unsure{avec|en}};\ \text{notation }(102); square-ended lower bracket',
     'Replace certain avec and identify the audited annotation shape.', ('B03',))
setv(p, ('inventory',13,'position'),
     'Below the first intersection in (107), attached by a square-ended lower bracket',
     'Keep the current inventory consistent with the audited grouping shape.', ('B05',))
setv(p, ('hand_log',4,'places'),
     ['150_scan098 avec/en under (106)','150_scan098 NB les/tous','150_scan098 footnote est'],
     'Use the current local doubt in the place description.', ('B03',))
setv(p, ('hand_log',4,'scope'),
     'The lower short word remains avec/en uncertain; both est readings are clear, and the overwritten NB word stays doubtful. The preserved witness-error field refers to C’s original avec proposal, not a certified current word.',
     'Remove the obsolete assertion that avec is clear while preserving witness fields.', ('B03',))
change(p,'C03','evidence',
       'The little looping group is crossed by a dense oblique cancellation. Its exact case and letter forms remain et/Et uncertain. H acknowledges the deletion without a word reading.',
       'Match the existing audited case doubt in this row’s final field.',('B02',))
diff(p,'D0767','reason',
     'The star-order fragment is macro-only. The cancelled word remains et/Et uncertain; C offers a tentative word reading while H describes the deletion without reading it.',
     'Keep current difference coverage consistent with the audited case doubt.',('B02',))
diff(p,'D0775','reason',
     'This split includes the lower short word omitted from H’s quotation, now retained as avec/en uncertain, and the unresolved subset/equality disagreement.',
     'Do not call the audited doubtful word a certified avec.',('B03',))
diff(p,'D0783','reason',
     'Formula closing syntax is editorial/macro; the repeated lower-annotation quotation omits the short word before notation (102), now retained as avec/en uncertain.',
     'Remove the stale assertion of a certain written avec.',('B03',))
diff(p,'D0774','reason',
     'The lower V_J^{X_L^*} is encoded beneath the formula in C and quoted in H’s following note; that formula and the vertical comparison agree. The recorded audit independently corrects the shared brace encoding to a square-ended bracket in C39.',
     'Distinguish agreement of the lower formula from the audited grouping-shape correction.',('B03',))
diff(p,'D0782','reason',
     'H describes the same two upright comparison bars and lower formula that C places below the first intersection. The current grouping is the square-ended bracket recorded in C39; the witness alignment classification is unchanged.',
     'Make the current grouping shape explicit without reclassifying a witness alignment.',('B03',))
new_notation = copy.deepcopy(current[p]['notation'])
new_notation.append({
    'sign':'square-ended lower brackets',
    'reading':'Straight lower grouping strokes with short rising ends and no central cusp.',
    'evidence':'Recorded blind audit of the lower annotations in (106) and (107), B03 and B05; current encodings are the bracket drawings in C39 and C40.'
})
setv(p, ('notation',), new_notation, 'Record an already adjudicated graphic convention in current notation metadata.', ('B03','B05'))
n = current[p]['notes']
anchor = 'The two upright equality bars under (106) stay vertical.'
n = replace_once(n, anchor,
    anchor + ' The lower groupings in (106) and (107) are square-ended brackets, with a flat middle and short rising ends rather than a central cusp.')
anchor = 'The footnote\'s cancellation precedes the live est.'
n = replace_once(n, anchor,
    anchor + ' The short word under (106) remains avec/en uncertain. In the Suggestion, the preceding group remains au/horizontal-rule uncertain and the next word lieu/lien uncertain; the cancelled connective below (105) remains et/Et uncertain.')
setv(p, ('notes',), n, 'State the audited brackets and word doubts in the main current note, not only its audit appendix.', ('B02','B03','B04','B05'))

# Semantic safeguards: preserve source readings, historical audit records, and row identities.
for p in PAGES:
    assert protected_values(before[p]) == protected_values(current[p]), p
    for collection, key in (('changes','id'), ('diff_coverage','diff_id'), ('decisions','id')):
        assert [v[key] for v in before[p][collection]] == [v[key] for v in current[p][collection]], (p,collection)
    assert before[p]['check_events'] == current[p]['check_events']
    valid_ids = {v['id'] for v in current[p]['changes']}
    assert all(set(v['change_ids']) <= valid_ids for v in current[p]['diff_coverage'])
    assert current[p]['audited'] is True
    for field in ('line_count','audit_reader','audit_boxes','audit_differing_boxes','audit_token_difference_runs','audit_changed_boxes','audit_utc'):
        assert before[p][field] == current[p][field], (p,field)

assert current['150_scan096']['deletion_insertion_review'][2]['reading'] == notes['150_scan096']['B08']['final']
assert current['150_scan096']['deletion_insertion_review'][4]['reading'] == notes['150_scan096']['B11']['final']
assert 'borne|bornera' not in current['150_scan096']['inventory'][12]['first_words_or_objects']
assert 'marche- / ront' not in current['150_scan097']['notes']
assert current['150_scan097']['decisions'][by_id('150_scan097','decisions','M0729')]['reading'].endswith('raient')
assert r'\text{ avec}' not in current['150_scan098']['inventory'][7]['first_words_or_objects']
assert 'Avec and both est readings are clear' not in current['150_scan098']['hand_log'][4]['scope']

# Verify all source decisions and text remain fixed before any write.
assert fixed_hashes == {str(p.relative_to(W)): sha(p.read_bytes()) for p in fixed_files}
for p in PAGES:
    assert paths[p].read_bytes() == raw[p], f'Concurrent change detected: {p}'
    encoded = (json.dumps(current[p], ensure_ascii=False, indent=2) + '\n').encode('utf-8')
    assert json.loads(encoded) == current[p]
for p in PAGES:
    temp = paths[p].with_suffix('.metadata_cleanup.tmp')
    assert not temp.exists()
    temp.write_text(json.dumps(current[p], ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    temp.replace(paths[p])
    assert json.loads(paths[p].read_text()) == current[p]
assert fixed_hashes == {str(p.relative_to(W)): sha(p.read_bytes()) for p in fixed_files}

report = {
    'scope':list(PAGES),
    'reader':'reader_b',
    'model':'GPT-6 Astra Pro',
    'effort':'not exposed',
    'run':'SP92',
    'completed_utc':datetime.now(timezone.utc).isoformat(),
    'mode':'Metadata consistency cleanup against existing root audit decisions; no manuscript rereading.',
    'summary':{
        '150_scan096':'Current revision, inventory, prose, and difference coverage now use the cancelled V terms, d/donc/On with comme/aura, et/tt, and resolved bornera.',
        '150_scan097':'Current notes, inventory, notation, mark decisions and evidence now use point-rule shapes, h above the parenthesized wave, marche-/raient, and the retained on a/mark doubt.',
        '150_scan098':'Current revision, inventory, notes, notation and coverage now describe square-ended brackets and the audited word/case doubts.',
    },
    'field_edit_count':len(edits),
    'edits_by_page':{p:sum(e['page']==p for e in edits) for p in PAGES},
    'edits':edits,
    'existing_overlap_note':'097 C26 and C34 concern the same split verb. C26’s current fields were synchronized and marked superseded_by C34; all row IDs and row counts were retained. No aggregate or counting policy was changed.',
    'checks':{
        'json_round_trip':True,
        'witness_fields_unchanged':True,
        'original_second_boxes_unchanged':True,
        'original_audit_changes_and_first_second_fields_unchanged':True,
        'change_diff_and_mark_ids_and_order_unchanged':True,
        'change_row_counts_unchanged':True,
        'diff_change_references_valid':True,
        'check_events_unchanged':True,
        'line_and_audit_counts_unchanged':True,
        'page_text_and_candidate_tex_unchanged':True,
        'sealed_first_and_second_tsvs_unchanged':True,
        'root_crop_notes_and_adjudications_unchanged':True,
        'images_viewed':False,
        'new_manuscript_decisions':False,
        'tex_compiled':False,
        'aggregates_assembled':False,
    },
    'unchanged_input_hashes':fixed_hashes,
    'record_hashes':{p:{'before':sha(raw[p]),'after':sha(paths[p].read_bytes())} for p in PAGES},
}
with LOG.open('x', encoding='utf-8') as f:
    json.dump(report,f,ensure_ascii=False,indent=2)
    f.write('\n')
print(json.dumps({'field_edits':len(edits),'by_page':report['edits_by_page'],'log':str(LOG),'protected_checks':'passed'},ensure_ascii=False))
