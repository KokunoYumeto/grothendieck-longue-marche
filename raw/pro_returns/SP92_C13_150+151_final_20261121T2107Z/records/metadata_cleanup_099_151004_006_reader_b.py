"""Current-description cleanup only; existing audits decide all readings."""
from pathlib import Path
import copy, hashlib, json
from datetime import datetime, timezone

W = Path('/workspace/scratch/d7279cb02214/SP92_C13_150+151_work')
PAGES = ('150_scan099','151_scan004','151_scan006')
LOG = W / 'records/metadata_cleanup_099_151004_006_reader_b.json'
assert not LOG.exists(), 'Scoped cleanup is already logged.'
sha = lambda b: hashlib.sha256(b).hexdigest()
paths = {p:W/'records'/f'{p}.json' for p in PAGES}
raw = {p:paths[p].read_bytes() for p in PAGES}
before = {p:json.loads(raw[p]) for p in PAGES}
current = copy.deepcopy(before)
root_notes = {p:json.loads((W/'second'/f'{p}_root_crop_notes.json').read_text()) for p in PAGES}
adjudications = {p:json.loads((W/'second'/f'{p}_adjudications.json').read_text()) for p in PAGES}

fixed = []
for p in PAGES:
    fixed.extend([
        W/'pages'/f'{p}.tex', W/'records'/f'{p}.tex',
        W/'second'/f'{p}_first.tsv', W/'second'/f'{p}_second.tsv',
        W/'second'/f'{p}_root_crop_notes.json',
        W/'second'/f'{p}_adjudications.json',
    ])
fixed.extend([W/'records/150_scan097.json', W/'second/150_scan097_adjudications.json'])
assert all(p.is_file() for p in fixed)
fixed_hashes = {str(p.relative_to(W)):sha(p.read_bytes()) for p in fixed}
historical = {
    'C','H','C_item','C_text','H_text','c','h',
    'first','second','first_reading','second_reading',
    'second_boxes','audit_changes','superseded_changes','witness_errors',
    'half_review','root_review_note','root_reviewed_utc','root_review_time',
}
def protected(v, path=()):
    out = {}
    if isinstance(v,dict):
        for key,value in v.items():
            if key in historical or key.startswith('witness_'):
                out[path+(key,)] = copy.deepcopy(value)
            else: out.update(protected(value,path+(key,)))
    elif isinstance(v,list):
        for i,value in enumerate(v): out.update(protected(value,path+(i,)))
    return out

edits = []
allowed = {'deletion_insertion_review','inventory','notes','hand_log','changes','diff_coverage'}
def setv(page,path,value,reason,boxes=()):
    assert path[0] in allowed
    assert not any(k in historical for k in path if isinstance(k,str))
    obj = current[page]
    for key in path[:-1]: obj = obj[key]
    old = copy.deepcopy(obj[path[-1]])
    if old == value: return
    obj[path[-1]] = value
    def brief(x):
        encoded = json.dumps(x,ensure_ascii=False)
        return x if len(encoded)<350 else {'sha256':sha(encoded.encode()),'characters':len(str(x))}
    edits.append({'page':page,'path':'/'.join(map(str,path)),'before':brief(old),'after':brief(value),
                  'reason':reason,'audit_boxes':list(boxes)})
def idindex(page,collection,ident):
    key = 'diff_id' if collection=='diff_coverage' else 'id'
    found = [i for i,row in enumerate(current[page][collection]) if row[key]==ident]
    assert len(found)==1
    return found[0]
def replace_once(s,old,new):
    assert s.count(old)==1,(old,s.count(old))
    return s.replace(old,new,1)

p = '150_scan099'
for i,field,value,box in [
    (0,'place','Marginal cancelled X_J^* and uncertain cap/cup group','B04'),
    (1,'place','Cancelled head group before donc si','B05'),
    (1,'bounds','A horizontal cancellation crosses the claire-like opening, obscured middle and high t-like ending; it leaves the raised replacement words live. The internal word division remains uncertain.','B05'),
    (2,'bounds','The two words occupy the short raised line above the cancelled head group.','B05'),
    (2,'attachment','Replaces the cancelled head group; followed by the longer inserted condition.','B05'),
    (4,'place','Main cancelled X_J group, with uncertain star and cap/cup','B06'),
]:
    setv(p,('deletion_insertion_review',i,field),value,
         'Remove a descriptor that prematurely settled the audited local uncertainty.',(box,))
for i,field,value,box in [
    (6,'element','Cancelled head group','B05'),
    (7,'position','Above the cancelled head group','B05'),
    (11,'first_words_or_objects',r'V_{J,L}^Z hooked arrow V_{\unsure{J|\square},L}; h above parentheses around the wave','B08'),
    (13,'first_words_or_objects',r'V_{J\unsure{,|0}}^L (déf = V_{J,L}^{X_L^*}) hooked arrow V_{J,L}; h above parentheses around the wave','B09'),
]:
    setv(p,('inventory',i,field),value,
         'Carry the current audited index and word uncertainty into the inventory summary.',(box,))
i = idindex(p,'changes','C06')
setv(p,('changes',i,'place'),'Head of main line leading to (110), cancelled group',
     'Do not assert a single word where word division remains uncertain.',('B05',))
setv(p,('changes',i,'evidence'),
     current[p]['changes'][i]['evidence'].replace('The canceled word is retained','The canceled group is retained'),
     'Keep the current evidence neutral about the uncertain internal word division.',('B05',))
i = idindex(p,'changes','C07')
setv(p,('changes',i,'place'),'Replacement immediately above the cancelled head group',
     'Replace the stale definite clairement locator.',('B05',))
setv(p,('changes',i,'evidence'),
     'The words donc si occupy their own short interlinear line directly above the cancelled head group, whose reading remains clairement/claire et/claire est uncertain. They are replacement ink, not an unmarked continuation of the original baseline.',
     'Keep the replacement evidence consistent with the audited old-group uncertainty.',('B05',))
i = idindex(p,'changes','C14')
setv(p,('changes',i,'place'),'Ordered-bands chain, label112/111, continuation between J_1 and J_n',
     'Avoid treating the audited uncertain last label digit as settled.',('B10',))
setv(p,('hand_log',2,'places'),
     ['marginal flag tuple','ordered-bands chain, label112/111','six locations in (113)'],
     'Use the current uncertain label while preserving historical crop filenames.',('B10',))
setv(p,('hand_log',5,'places'),
     ['on aura','on posera','cancelled head group, clairement/claire et/claire est uncertain'],
     'Do not list the cancelled word as a certified occurrence of clairement.',('B05',))
i = idindex(p,'diff_coverage','D0834')
setv(p,('diff_coverage',i,'reason'),
     'The cancelled head group remains clairement/claire et/claire est uncertain; its separately raised donc si replacement is clear.',
     'Preserve uncertain word division in current coverage.',('B05',))
i = idindex(p,'diff_coverage','D0822')
setv(p,('diff_coverage',i,'reason'),
     'The underset/lim and varinjlim syntax places the same written conditions beneath the limit. The audited lower stroke in (109) remains underline-lim/directed-limit uncertain; this local doubt does not change the witness-syntax classification.',
     'Separate agreement on index placement from the current limit-stroke uncertainty.',('B03',))
n = current[p]['notes']
n = replace_once(n,
    'The page then introduces ordered bands in (112) and defines V for their tuple',
    'The page then introduces ordered bands in the chain labeled112/111, whose last digit remains uncertain, and defines V for their tuple')
n = replace_once(n,
    'dot followed by rule in the marginal tuple and (112);',
    'dot followed by rule in the marginal tuple and the ordered-bands chain;')
n = replace_once(n,
    'The canceled head word remains clairement/claire et/claire est uncertain:',
    'The cancelled head group remains clairement/claire et/claire est uncertain:')
setv(p,('notes',),n,'Align the current overview with the already audited label and word-division doubts.',('B05','B10'))

# 004 has no current contradiction: retain its record byte for byte.
p = '151_scan006'
n = replace_once(current[p]['notes'],
    'The autograph and foliation are the handwritten items requiring blind rereading.',
    'The autograph and foliation were included in the completed blind rereading.')
setv(p,('notes',),n,'Remove an obsolete pending-audit description; the recorded audit is complete.')

# No history, row/count, page, TSV or audit-source changes.
for p in PAGES:
    assert protected(before[p]) == protected(current[p]),p
    for collection,key in [('changes','id'),('diff_coverage','diff_id'),('decisions','id')]:
        assert [e[key] for e in before[p][collection]] == [e[key] for e in current[p][collection]],(p,collection)
    for field in ('line_count','check_events','audit_boxes','audit_differing_boxes',
                  'audit_token_difference_runs','audit_changed_boxes','audit_utc'):
        assert before[p][field] == current[p][field],(p,field)
    ids = {e['id'] for e in current[p]['changes']}
    assert all(set(e['change_ids']) <= ids for e in current[p]['diff_coverage'])
    assert current[p]['audited'] is True
assert current['151_scan004'] == before['151_scan004']
r99 = current['150_scan099']
ids99 = [e['id'] for e in r99['changes']]
assert ids99.count('C22') == 1 and not any(i in ids99 for i in ('C23','C24','C25'))
c22 = r99['changes'][idindex('150_scan099','changes','C22')]
assert c22['final'] == root_notes['150_scan099']['B13']['final']
assert r99['deletion_insertion_review'][6]['reading'] == c22['final']
assert r99['inventory'][20]['first_words_or_objects'] == c22['final']
assert c22['final'] in (W/'pages/150_scan099.tex').read_text()
assert all(sha((W/name).read_bytes())==digest for name,digest in fixed_hashes.items())

for p in PAGES:
    assert paths[p].read_bytes()==raw[p],f'Concurrent change detected: {p}'
    if current[p] != before[p]:
        text = json.dumps(current[p],ensure_ascii=False,indent=2)+'\n'
        assert json.loads(text)==current[p]
        temp=paths[p].with_suffix('.metadata_cleanup.tmp')
        assert not temp.exists()
        temp.write_text(text,encoding='utf-8')
        temp.replace(paths[p])
        assert json.loads(paths[p].read_text())==current[p]
assert paths['151_scan004'].read_bytes()==raw['151_scan004']
assert all(sha((W/name).read_bytes())==digest for name,digest in fixed_hashes.items())

r97 = json.loads((W/'records/150_scan097.json').read_text())
rows97 = {e['id']:e for e in r97['changes']}
assert rows97['C26']['box']==rows97['C34']['box']==[270,1572,1640,1848]
assert rows97['C26']['final']==rows97['C34']['final']
recommendation = {
    'mode':'Read-only; no 097 row, flag, witness field or count changed.',
    'finding':'C26 and C34 cover the same full split verb and the same coordinates. Neither provides an independent abbreviation change, and the preserved hyphen/line break is part of that same reading.',
    'witness_provenance':{
        'C26':{'C':rows97['C26']['C'],'H':rows97['C26']['H']},
        'C34':{'C':rows97['C34']['C'],'H':rows97['C34']['H']},
        'interpretation':'C26 retains the original uncertain marchent proposals. C34’s marcheront entries match the superseded first-pass reading documented by B12, not the proposals retained in C26.'
    },
    'recommendation':'Count one lexical/doubt-resolution locus. Prefer C26 as the C/H collation row with the audited marche-/raient final, and treat C34 as the audit delta/history. If C34 is instead the canonical counted row, exclude C26 and preserve the actual witness provenance separately. Do not count an additional line-break or abbreviation error.',
    'existing_superseded_by_left_unchanged':rows97['C26'].get('superseded_by'),
}
report = {
    'scope':list(PAGES),'reader':'reader_b','model':'GPT-6 Astra Pro','effort':'not exposed','run':'SP92',
    'completed_utc':datetime.now(timezone.utc).isoformat(),
    'authority':'Current pages and existing root crop notes/adjudications only; no images or new readings.',
    'field_edit_count':len(edits),
    'edits_by_page':{p:sum(e['page']==p for e in edits) for p in PAGES},
    'edits':edits,
    '099_inverted_block_check':'The current page, C22, revision review and inventory already agree exactly with audited B13. C23–25 remain absent from current changes; protected superseded_changes remains unchanged.',
    '004_result':'No stale current reading metadata found; record preserved byte for byte.',
    '006_result':'Substantive current metadata agrees with the audit; only the obsolete pending-blind-reading sentence was updated.',
    'independent_read_only_check':'A separate metadata reader checked 004 and006 against their pages and adjudications and found no substantive current reading contradictions.',
    '097_counting_recommendation':recommendation,
    'checks':{
        'json_round_trip':True,'historical_snapshots_and_witness_fields_unchanged':True,
        'second_boxes_and_audit_first_second_fields_unchanged':True,
        'change_diff_mark_ids_and_order_unchanged':True,'counts_and_check_events_unchanged':True,
        'diff_change_references_valid':True,'pages_and_candidate_tex_unchanged':True,
        'sealed_tsvs_unchanged':True,'root_crop_notes_and_adjudications_unchanged':True,
        '097_record_and_adjudication_unchanged':True,'004_record_byte_identical':True,
        'images_viewed':False,'new_manuscript_decisions':False,'compilation_run':False,'aggregates_assembled':False,
    },
    'unchanged_input_hashes':fixed_hashes,
    'record_hashes':{p:{'before':sha(raw[p]),'after':sha(paths[p].read_bytes())} for p in PAGES},
}
with LOG.open('x',encoding='utf-8') as f:
    json.dump(report,f,ensure_ascii=False,indent=2);f.write('\n')
print(json.dumps({'field_edits':len(edits),'by_page':report['edits_by_page'],
                  'protected_hashes_checked':len(fixed_hashes),'log':str(LOG),
                  '097_recommendation':'One locus only; prefer C26 as the C/H row and C34 as audit history.'},ensure_ascii=False))
