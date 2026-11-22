"""Authorized canonical-locus cleanup and final-field command separation only."""
from pathlib import Path
import copy, hashlib, json
from datetime import datetime, timezone

W = Path('/workspace/scratch/d7279cb02214/SP92_C13_150+151_work')
LOG = W/'records/scoped_097_dedup_099_encoding_reader_b.json'
assert not LOG.exists()
sha=lambda b:hashlib.sha256(b).hexdigest()
targets = {
    '097':W/'records/150_scan097.json',
    '099_record':W/'records/150_scan099.json',
    '099_notes':W/'second/150_scan099_root_crop_notes.json',
    '099_adjudications':W/'second/150_scan099_adjudications.json',
}
raw={k:p.read_bytes() for k,p in targets.items()}
before={k:json.loads(b) for k,b in raw.items()}
after=copy.deepcopy(before)
fixed=[]
for page in ('150_scan097','150_scan099'):
    fixed.extend([W/'pages'/f'{page}.tex',W/'records'/f'{page}.tex',
                  W/'second'/f'{page}_first.tsv',W/'second'/f'{page}_second.tsv'])
fixed.extend([W/'second/150_scan097_root_crop_notes.json',W/'second/150_scan097_adjudications.json'])
fixed_hashes={str(p.relative_to(W)):sha(p.read_bytes()) for p in fixed}
now=datetime.now(timezone.utc).isoformat()

# Canonical C/H locus: C26; preserve the removed C34 row verbatim in new history.
d=after['097']
old34=copy.deepcopy(next(r for r in d['changes'] if r['id']=='C34'))
r26=next(r for r in d['changes'] if r['id']=='C26')
assert r26['box']==old34['box']
assert r26['final']==old34['final']
assert r26.pop('superseded_by')=='C34'
d['changes']=[r for r in d['changes'] if r['id']!='C34']
remapped=[]
for row in d['diff_coverage']:
    old=copy.deepcopy(row['change_ids'])
    row['change_ids']=list(dict.fromkeys('C26' if x=='C34' else x for x in old))
    if old!=row['change_ids']:
        remapped.append({'diff_id':row['diff_id'],'before':old,'after':row['change_ids']})
snapshot={
    'superseded_utc':now,
    'canonical_change_id':'C26',
    'excluded_from_current_counts':True,
    'reason':(
        'Root authorized one canonical C/H locus for the same split verb. C26 preserves the original '
        'uncertain marchent witness proposals and now has the audited marche-/raient final. C34 is the '
        'later audit delta at identical coordinates; its marcheront C/H summaries describe the superseded '
        'first-pass reading, not the original witness proposals. Counting both would count the same lexical '
        'correction twice. The row below is retained verbatim as history; the line break is not a second '
        'abbreviation or independent lexical correction.'
    ),
    'changes':[old34],
}
d.setdefault('superseded_changes',[]).append(snapshot)
assert d['superseded_changes'][-1]['changes'][0]==old34
assert d['decisions']==before['097']['decisions']
assert d['audit_changes']==before['097']['audit_changes']
assert d['second_boxes']==before['097']['second_boxes']
for row in d['changes']:
    old=next(r for r in before['097']['changes'] if r['id']==row['id'])
    expected=copy.deepcopy(old)
    if row['id']=='C26': expected.pop('superseded_by')
    assert row==expected
assert len(d['changes'])==len(before['097']['changes'])-1
assert len({r['id'] for r in d['changes']})==len(d['changes'])
assert all(set(r['change_ids']) <= {c['id'] for c in d['changes']} for r in d['diff_coverage'])

# Only authorized final fields receive encoding-only separation.
page99=(W/'pages/150_scan099.tex').read_text()
encoding_edits=[]
def repair_final(container,location,box):
    old=container.get('final','')
    new=old.replace(r'\qquadV',r'\qquad V').replace(r'\capV',r'\cap V')
    if new==old: return
    assert new in page99,(location,box,'Final is not an unchanged-page substring')
    container['final']=new
    encoding_edits.append({
        'file':location,'box':box,
        'qquadV_replacements':old.count(r'\qquadV'),
        'capV_replacements':old.count(r'\capV'),
        'matches_current_page':True,
    })
for box,row in after['099_notes'].items():
    repair_final(row,str(targets['099_notes'].relative_to(W)),box)
for row in after['099_adjudications']['adjudications']:
    repair_final(row,str(targets['099_adjudications'].relative_to(W)),row['box'])
for row in after['099_record']['audit_changes']:
    repair_final(row,str(targets['099_record'].relative_to(W)),row['box'])
assert len(encoding_edits)==9
for key in ('099_record','099_notes','099_adjudications'):
    expected=copy.deepcopy(before[key])
    if key=='099_notes': rows=list(expected.values())
    elif key=='099_adjudications': rows=expected['adjudications']
    else: rows=expected['audit_changes']
    for row in rows:
        if 'final' in row:
            row['final']=row['final'].replace(r'\qquadV',r'\qquad V').replace(r'\capV',r'\cap V')
    assert after[key]==expected
for key,collection in (('099_record','audit_changes'),('099_adjudications','adjudications')):
    assert [(r.get('box'),r.get('first'),r.get('second')) for r in before[key][collection]] == [
        (r.get('box'),r.get('first'),r.get('second')) for r in after[key][collection]
    ]
assert before['099_record']['changes']==after['099_record']['changes']
assert before['099_record']['superseded_changes']==after['099_record']['superseded_changes']
assert before['099_record']['second_boxes']==after['099_record']['second_boxes']
assert before['099_record']['decisions']==after['099_record']['decisions']
for key in ('097','099_record'):
    for field in ('line_count','check_events','audit_boxes','audit_differing_boxes',
                  'audit_changed_boxes','audit_token_difference_runs','audit_utc'):
        assert before[key][field]==after[key][field]
assert all(sha((W/p).read_bytes())==h for p,h in fixed_hashes.items())

for key,path in targets.items():
    assert path.read_bytes()==raw[key],f'Concurrent modification: {path}'
    text=json.dumps(after[key],ensure_ascii=False,indent=2)+'\n'
    assert json.loads(text)==after[key]
for key,path in targets.items():
    temp=path.with_suffix('.scoped_repair.tmp')
    assert not temp.exists()
    temp.write_text(json.dumps(after[key],ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    temp.replace(path)
assert all(sha((W/p).read_bytes())==h for p,h in fixed_hashes.items())

report={
    'reader':'reader_b','model':'GPT-6 Astra Pro','effort':'not exposed','run':'SP92',
    'completed_utc':datetime.now(timezone.utc).isoformat(),
    '097_canonical_locus':{
        'canonical':'C26','archived_verbatim':'C34','current_change_rows_before':len(before['097']['changes']),
        'current_change_rows_after':len(after['097']['changes']),'removed_superseded_by':'C34',
        'diff_link_remaps':remapped,'reason':snapshot['reason'],
        'decisions_page_second_boxes_and_original_audit_unchanged':True,
    },
    '099_encoding':{
        'edits':encoding_edits,
        'final_fields_changed':len(encoding_edits),
        'command_separations':sum(e['qquadV_replacements']+e['capV_replacements'] for e in encoding_edits),
        'first_second_fields_unchanged':True,'all_repaired_finals_match_current_page':True,
        'other_record_fields_unchanged':True,
    },
    'checks':{
        'json_round_trip':True,'unchanged_input_hashes_passed':True,
        'sealed_tsvs_unchanged':True,'page_and_candidate_tex_unchanged':True,
        'original_audit_first_second_unchanged':True,'existing_historical_snapshots_unchanged':True,
        'images_viewed':False,'new_readings':False,'compilation':False,'assembly':False,
    },
    'unchanged_input_hashes':fixed_hashes,
    'file_hashes':{str(targets[k].relative_to(W)):{'before':sha(raw[k]),'after':sha(targets[k].read_bytes())} for k in targets},
}
with LOG.open('x',encoding='utf-8') as f:
    json.dump(report,f,ensure_ascii=False,indent=2);f.write('\n')
print(json.dumps({'097_current_rows':len(d['changes']),'097_C34_archived_verbatim':True,
                  '097_diff_links_remapped':len(remapped),'099_final_fields_separated':len(encoding_edits),
                  'current_page_matches':True,'log':str(LOG)},ensure_ascii=False))
