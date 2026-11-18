"""Validate delivery structure and frozen bytes; never modify the transcription."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import csv, hashlib, json, re

ROOT=Path(__file__).resolve().parents[1]
WORK=ROOT.parent
R=ROOT/'records/research'
expected=list(range(2,13))+list(range(14,38))+list(range(39,42))
manifest=json.loads((ROOT/'records/frozen_sha256.json').read_text())
hashes={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in manifest['sha256']}
assert hashes==manifest['sha256'], 'A frozen transcription hash changed'
assert len(hashes)==39
pages=sorted((ROOT/'pages').glob('MPL_118_118_scan*.tex'))
assert len(pages)==38
combined=(ROOT/'MPL_118_transcription.tex').read_text()
assert [int(x) for x in re.findall(r'\\scanpage\{(\d+)\}',combined)]==expected
assert all(p.read_text() in combined for p in pages)
assert '\\documentclass' not in combined and '\\includegraphics' not in combined
cotefile_count=combined.count('\\cotefile{118}')
assert cotefile_count==2, 'Expected the documented frozen assembly defect'

with (ROOT/'MPL_118_inventory.csv').open() as f:
    rd=csv.DictReader(f); inv=list(rd)
    assert rd.fieldnames==['cote','scan','sheet_kind','element','kind','position','first_words_or_objects','transcribed']
assert len(inv)==810 and all(x['transcribed']=='yes' for x in inv)
assert sorted({int(x['scan']) for x in inv})==expected
assert len({(x['cote'],x['scan'],x['element']) for x in inv})==len(inv)
sheet={}
for x in inv:
    n=int(x['scan']); assert n not in sheet or sheet[n]==x['sheet_kind'];sheet[n]=x['sheet_kind']
sheetcounts=dict(Counter(sheet.values()))
assert sheetcounts=={'cover':1,'text':31,'reused_typed':6}
doubts=json.loads((ROOT/'records/doubt_judgments.json').read_text())
assert len(doubts)==369
assert sum(p.read_text().count('\\unsure{') for p in pages)==369
assert sum(p.read_text().count('\\illegible{') for p in pages)==0
confidence=dict(Counter(d['confidence'] for d in doubts))
assert confidence=={'medium':98,'low':271}

progress=(ROOT/'progress.log').read_text()
done=[int(x) for x in re.findall(r'^118 scan (\d+) done ',progress,re.M)]
audited=[int(x) for x in re.findall(r'^scan (\d+) audited ',progress,re.M)]
assert done==expected and audited==expected
assert progress.index('transcription frozen ')<progress.index('context opened ')

source=(WORK/'context/DOSSIER_STATEMENTS_WITH_STATUS.md').read_text()
expected_dossier={m[1]:m[2] for m in re.finditer(r'^\| ((?:STRATA|PATHS|BISITE|RESIDUE) [^|]+?) \| .*? \| (claim \(return: [^)]+\)) \|',source,re.M)}
assert len(expected_dossier)==255
rows=[]
for fn in ['strata_paths_mapping.json','bisite_mapping.json','residue_mapping.json','new_results_mapping.json']:
    d=json.loads((R/fn).read_text());rows+=d.get('rows',d.get('records',[]))
assert len(rows)==270 and len({x['id'] for x in rows})==270
actual_dossier={x['id']:x['supplied_status'] for x in rows if not x['id'].startswith('NR')}
assert actual_dossier==expected_dossier
assert {x['id'] for x in rows if x['id'].startswith('NR')}=={f'NR{i}' for i in range(1,13)}|{f'NR-K{i}' for i in range(1,4)}
relations=dict(Counter(x['relation'] for x in rows))
assert relations=={'partial':18,'analogue':50,'absent':202}
quotations=0
for n in rows:
    if n.get('kind',n.get('note_kind'))=='own idea':
        assert n.get('own_comparison_confidence') and n.get('confidence_reason')
    for e in n.get('evidence',n.get('manuscript_evidence',[]))+n.get('nearest_related_evidence',[]):
        q=e.get('quote_tex',e.get('quotation_tex',e.get('quotation')))
        if q is None:continue
        p=e.get('page_file',e.get('frozen_page_file'))
        assert q in (WORK/p).read_text(), (n['id'],p)
        quotations+=1
assert quotations==262

notes=(ROOT/'MPL_118_notes.md').read_text()
primary_ids=re.findall(r'^### (MPL118-[A-Z]+\d+) —',notes,re.M)
assert len(primary_ids)==126 and len(set(primary_ids))==126
ledger=json.loads((R/'context_search_ledger.json').read_text())
assert {x['id'] for x in ledger['rows']}==set(primary_ids)
for fn in ['root_notes.md','root_additional_checks.md','root_claims.md','root_self_flags.md','root_reading_questions.md','root_titles.md']:
    for q in re.findall(r'(?<!`)`([^`\n]+)`(?!`)',(R/fn).read_text()):
        if '\\' in q and '/' not in q: assert q in combined, (fn,q)

with (ROOT/'CHECK_EVENTS.tsv').open() as f:
    events=list(csv.DictReader(f,delimiter='\t'))
event_ids={e['statement_id'] for e in events}
assert {x['id'] for x in rows}|set(primary_ids)<=event_ids
allowed={'targeted proof check','independent re-proof','computation or formal certificate',
         'used and rechecked in this run','carried as background without fault found'}
assert all(e['type'] in allowed or e['type'].startswith('refuted,') for e in events)
assert all('GPT-' in e['who'] and 'effort' in e['who'].lower() and 'run' in e['who'].lower() for e in events)
assert all(e['outcome'] and e['date'] for e in events)

static=json.loads((ROOT/'records/technical_qa/static_report.json').read_text())
static_hashes={str(Path(p['path']).relative_to(ROOT)):p['sha256'] for p in static['pages']}
assert all(hashes[p]==h for p,h in static_hashes.items())
assert sum(len(p['issues']) for p in static['pages'])==0
excluded_exts={'.jpg','.jpeg','.png','.pdf','.zip'}
assert not [str(p) for p in ROOT.rglob('*') if p.is_file() and p.suffix.lower() in excluded_exts], 'Unexpected supplied-source/image/archive file in deliverable tree'

now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
report={
 'validated_utc':now,'scope':'Structural/source-mapping checks and byte verification; no OCR, image audit, full mathematical certification, or successful TeX rendering implied.',
 'frozen_utc':manifest['frozen_utc'],'all_frozen_hashes_unchanged':True,'frozen_files_checked':39,
 'combined_sha256':hashes['MPL_118_transcription.tex'],'scan_count':38,'scan_order':expected,
 'done_log_entries':len(done),'audit_log_entries':len(audited),'inventory_rows':len(inv),
 'sheet_counts':sheetcounts,'unsure_occurrences':369,'illegible_occurrences':0,'doubt_confidence':confidence,
 'tikzcd_matrices':sum(len(p['diagrams']) for p in static['pages']),
 'diagram_arrows':sum(d['arrow_count'] for p in static['pages'] for d in p['diagrams']),
 'static_issue_count':0,'rendered_validation':False,
 'known_frozen_assembly_defect':'Two consecutive initial cotefile{118} markers; preserved after freeze.',
 'dossier_rows':255,'new_results_rows':15,'mapping_relations':relations,'literal_mapping_quotes_checked':quotations,
 'primary_notes':126,'total_notes_and_mappings':396,'event_rows_before_final_qa_event':len(events),
 'event_types':dict(Counter(e['type'] for e in events)),
 'original_scans_context_and_prior_zip_files_excluded':True,
}
(ROOT/'records/final_validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
with (R/'final_qa_events.tsv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t',lineterminator='\n');w.writeheader()
    w.writerow({'statement_id':'MPL118-QA-FINAL','date':now,'who':'GPT-6 Astra Pro; effort not exposed; primary run MPL_118/root',
                'type':'computation or formal certificate','outcome':'Technical computation only: all 39 frozen SHA-256 values unchanged; 38 page files and scan markers, 810 complete inventory rows, 369 doubt entries, 270 exact required mapping IDs/statuses, 262 literal evidence quotations, and 126 primary-note event/search records verified; no rendered-layout or mathematical proof certificate.'})
with (ROOT/'progress.log').open('a') as f:
    f.write('research notes complete '+now+': 126 primary notes, 255 dossier mappings, 15 NEW_RESULTS mappings; context statuses retained as claims; actual check scopes recorded\n')
    f.write('final frozen-hash verification '+now+': all 38 page files and combined transcription unchanged (39/39 SHA-256 matches); combined '+hashes['MPL_118_transcription.tex']+'\n')
print(json.dumps(report,ensure_ascii=False))
