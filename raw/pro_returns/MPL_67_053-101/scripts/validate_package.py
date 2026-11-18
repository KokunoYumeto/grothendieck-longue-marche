"""Validate deliverable structure and frozen-byte identity; does not alter transcription."""
from pathlib import Path
from datetime import datetime,timezone
import json,csv,re,hashlib,collections,argparse
R=Path(__file__).resolve().parents[1]
ap=argparse.ArgumentParser();ap.add_argument('--seal',action='store_true');args=ap.parse_args()
expected=[n for n in range(53,102) if n not in (83,90)]
files=sorted((R/'pages').glob('*.tex'))
assert [int(re.search(r'scan(\d+)',x.name).group(1)) for x in files]==expected
frozen=json.loads((R/'records/frozen_sha256.json').read_text());assert len(frozen)==48
actual={p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in frozen}
assert actual==frozen,'A frozen hash changed'
s=(R/'MPL_67_053-101_transcription.tex').read_text()
assert s=='\n'.join(p.read_text() for p in files),'Combined text differs from page concatenation'
assert s.startswith('\\cotefile{67}\n\\scanpage{53}')
assert [int(n) for n in re.findall(r'\\scanpage\{(\d+)\}',s)]==expected
assert '\\documentclass' not in s and '\\begin{document}' not in s and '\\includegraphics' not in s
assert s.count('\\cotefile{')==1
assert s.count('\\unsure{')==450
assert re.findall(r'\\illegible\{([^}]*)\}',s)==['1']
illegible_at=s.index('\\illegible{1}')
inside_deletion=False
for m in re.finditer(r'\\deleted\{',s):
 depth=1;j=m.end()
 while j<len(s) and depth:
  if s[j] in '{}' and (j==0 or s[j-1]!='\\'):
   depth+=1 if s[j]=='{' else -1
  j+=1
 if m.end()<=illegible_at<j:inside_deletion=True
assert inside_deletion,'The illegible estimate must retain its cancelled state'
with (R/'MPL_67_053-101_inventory.csv').open(newline='') as f:
 rd=csv.DictReader(f);assert rd.fieldnames==['cote','scan','sheet_kind','element','kind','position','first_words_or_objects','transcribed'];inventory=list(rd)
assert len(inventory)==938 and all(x['transcribed']=='yes' for x in inventory)
assert sorted({int(x['scan']) for x in inventory})==expected
assert all(x['cote']=='67' for x in inventory)
assert len({(x['scan'],x['element']) for x in inventory})==938
assert {x['kind'] for x in inventory}<={'text','display','diagram','drawing','margin note','insertion','deletion'}
assert {x['sheet_kind'] for x in inventory}<={'text','reused_typed','cancelled_draft','cover'}
assert {int(x['scan']) for x in inventory if x['sheet_kind']=='reused_typed'}=={92,96}
prog=(R/'progress.log').read_text()
assert prog.splitlines()[0]=='2026-11-17 23:49:13 UTC'
assert [int(x) for x in re.findall(r'^67 scan (\d+) done ',prog,re.M)]==expected
assert sorted(int(x) for x in re.findall(r'^scan (\d+) audited ',prog,re.M))==expected
assert prog.index('transcription frozen 2026-11-18 01:15:15 UTC')<prog.index('context opened 2026-11-18 01:15:25 UTC')
audits=[json.loads(x) for x in (R/'records/audits.jsonl').read_text().splitlines() if x.strip()]
assert sorted(x['scan'] for x in audits)==expected
notes=(R/'MPL_67_053-101_notes.md').read_text()
ids=re.findall(r'^### ([SBOEP]\d{2}) —',notes,re.M)
required={f'{prefix}{n:02}' for prefix,last in [('S',34),('B',19),('O',16),('E',30),('P',1)] for n in range(1,last+1)}
assert len(ids)==100 and set(ids)==required
census=json.loads((R/'research/census_data.json').read_text())
assert len(census)==45 and {x['id'] for x in census}=={f'{p}{n:02}' for p,last in [('F',33),('T',12)] for n in range(1,last+1)}
searches={}
for family in ['surgery','octahedron','elliptic']:
 for x in json.loads((R/f'research/{family}/search_ledger.json').read_text()):
  searches[x['note_id']]=True
  if family=='surgery':assert x['total_matching_lines']>0
  elif family=='elliptic':assert x['match_count']>0
  else:assert any(q['total_hits']>0 for q in x['queries'])
b=json.loads((R/'research/bridges/search_ledger.json').read_text())
assert len(b['hua_coverage_searches'])==36
for x in b['notes']:
 searches[x['note_id']]=True;assert any(q['hit_count']>0 for q in x['searches'])
p=json.loads((R/'research/plan_search_ledger.json').read_text());searches[p['note']]=True;assert p['sample_hits']
assert set(searches)==required
cs=json.loads((R/'research/census_search_ledger.json').read_text());assert len(cs)==45 and all(x['sample_hits'] for x in cs)
assert {x['note'] for x in cs}=={x['id'] for x in census}
with (R/'CHECK_EVENTS.tsv').open(newline='') as f:
 rd=csv.DictReader(f,delimiter='\t');assert rd.fieldnames==['statement_id','date','who','type','outcome'];events=list(rd)
allowed={'targeted proof check','independent re-proof','computation or formal certificate','used and rechecked in this run','carried as background without fault found',"refuted, with the refined statement's id"}
assert all(x['type'] in allowed and all(x.values()) for x in events)
assert required|{x['id'] for x in census}<={x['statement_id'] for x in events}
# Cross-reference aliases to source records are intentionally retained as separate events.
for x in events:
 if x['type'].startswith('refuted'):assert re.search(r'[SOE]\d{2}',x['outcome']),x
log=(R/'validation/compile_check.log').read_text()
assert not re.search(r'^!|Missing character:|Overfull|Underfull',log,re.M)
assert 'pdfdraftmode enabled' in log and '[48' in log
for f in R.rglob('*.json'):json.loads(f.read_text())
for f in R.rglob('*.jsonl'):
 for line in f.read_text().splitlines():
  if line.strip():json.loads(line)
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
result={'validated_at_utc':now,'cote':67,'scans':expected,'pages':47,'frozen_hashes_checked':48,'all_frozen_hashes_unchanged':True,'combined_equals_page_concatenation':True,'all_pages_audited_before_context':True,'inventory_elements':938,'inventory_all_yes':True,'inventory_kind_counts':dict(collections.Counter(x['kind'] for x in inventory)),'doubt_macros':450,'illegible_macros':[1],'main_research_notes':100,'self_flagged_items':33,'title_count_items':12,'per_item_context_searches':145,'hua_coverage_headings':36,'check_event_rows':len(events),'check_event_type_counts':dict(collections.Counter(x['type'] for x in events)),'full_fragment_latex_compile':'successful, draftmode; no errors, missing characters or over/underfull boxes','no_source_images_in_transcription':True,'source_files_to_be_excluded_from_zip':['original user attachments','scans/','inspection/','context/','prior checkpoint ZIPs'],'limitations':'Structural validation is not a further image reading or mathematical proof. Explicit uncertainty and the research scope limitations remain.'}
(R/'validation/final_validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
if args.seal:
 with (R/'progress.log').open('a') as f:
  f.write(f'research completed {now}: 100 research notes; 33 self-flag census items; 12 title/count items; 36 Hua coverage headings; {len(events)} check events.\n')
  f.write(f'final frozen-hash check {now}: all 47 page files and combined transcription unchanged; all 48 SHA-256 values match the freeze.\n')
  f.write(f'final validation {now}: 47 pages, 938 inventory elements all yes, 450 unsure marks, one illegible-word estimate; exact combined/page concatenation and all per-item context searches verified.\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
