from pathlib import Path
from datetime import datetime, timezone
import csv,json,re,sys
from PIL import Image
BASE=Path(__file__).resolve().parents[2]
OUT=BASE/'out'
SRC=BASE/'source'
W=SRC/'SP33_CW_156-5_witnesses'
MAP=list(csv.DictReader((W/'page_map.tsv').open(),delimiter='\t'))
def utc():return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def mapping(n):return next(r for r in MAP if int(r['our_scan'])==n)
def ctext(n):return (W/mapping(n)['codex_file']).read_text()
def htext(n):
 r=mapping(n);s=(W/r['hua_file']).read_text(); pat=r'\\page\{'+r['their_page']+r'\}'
 start=re.search(pat,s).end(); m=re.search(r'\\page\{|\\end\{document\}',s[start:]);return s[start:start+m.start()] if m else s[start:]
def crop(n,label,box,angle=0,scale=2):
 r=mapping(n); src=SRC/'SP33_CW_156-5_scans'/f"{r['folder']}_156-5_scan{n:03}.jpg"
 im=Image.open(src).crop(tuple(box))
 if angle:im=im.rotate(angle,expand=True,fillcolor='white')
 im=im.resize((round(im.width*scale),round(im.height*scale)),Image.Resampling.LANCZOS)
 dest=OUT/'crops'/f'{n:03}_{label}.jpg';im.save(dest,quality=94)
 meta={'scan':n,'name':dest.name,'box':box,'rotation_degrees_ccw':angle,'scale':scale,'source':src.name,'created_utc':utc()}
 with (OUT/'records/crops.jsonl').open('a') as f:f.write(json.dumps(meta,ensure_ascii=False)+'\n')
 return dest

def md(s):return str(s).replace('|','\\|').replace('\n','<br>')
def _guard_frozen_transcription():
 # The manifest is created by root at the freeze, before opening context.
 # Its flat mapping is relative TeX path -> SHA-256. Presence always locks TeX.
 manifest=OUT/'records/frozen_hashes.json'
 if not manifest.exists():return False
 hashes=json.loads(manifest.read_text())
 if not isinstance(hashes,dict) or not hashes:
  raise RuntimeError('Frozen transcription manifest must be a nonempty path-to-SHA256 mapping')
 expected={str(p.relative_to(OUT)) for p in (OUT/'pages').glob('*.tex')}
 expected.add('SP33_CW_156-5_transcription.tex')
 if set(hashes)!=expected:
  raise RuntimeError('Frozen transcription manifest does not cover exactly all page TeX files and the combined transcription')
 for relative,digest in hashes.items():
  path=OUT/relative
  if not path.resolve().is_relative_to(OUT.resolve()) or not isinstance(digest,str) or not re.fullmatch(r'[0-9a-fA-F]{64}',digest):
   raise RuntimeError('Invalid frozen transcription manifest entry: '+str(relative))
  if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest()!=digest.lower():
   raise RuntimeError('Frozen transcription hash mismatch: '+relative)
 return True

def regenerate():
 frozen=_guard_frozen_transcription()
 records=[json.loads(p.read_text()) for p in sorted((OUT/'records').glob('scan[0-9][0-9][0-9].json'))]
 rows=[]; inv=[];counts=[]; consequential=[]; sections=[]; doubtrows=[]
 for r in records:
  n=r['scan']; sec=[f'## Scan {n:03} — manuscript page {n-1}', '', '| ID / place | C | H | Final | What the image shows; crop | Confidence |','|---|---|---|---|---|---|']
  changes=r.get('changes',[])
  for k,d in enumerate(changes,1):
   ident=d.get('id',f'{n:03}-{k:02}')
   sec.append('| '+' | '.join(md(v) for v in [ident+' / '+d['place'],d['c'],d['h'],d['final'],d['evidence'],d.get('confidence','high')])+' |')
   if d.get('h_changed'):
    rows.append([mapping(n)['folder'],n-1,n,d['place'],d['h'],d['c'],d['final'],d['evidence'],d.get('kind','other'),d.get('marked_h','no'),d.get('confidence','high')])
   if d.get('consequential'):consequential.append(f'- Scan {n:03}, {ident}: {d["consequential"]}')
  counts.append([n,sum(bool(d.get('c_changed')) for d in changes),sum(bool(d.get('h_changed')) for d in changes)]+[sum(d.get('confidence','high')==c for d in changes) for c in ['high','medium','low']])
  sec+=['','### C doubt decisions and witness S','',*['- '+x for x in r.get('doubt_decisions',[])],'','### Still unresolved','',*(['- '+x for x in r.get('unresolved',[])] or ['None.']),'']
  sections+=sec
  for k,e in enumerate(r.get('inventory',[]),1):
   inv.append([n,e.get('sheet_kind','text'),e.get('hand','Grothendieck'),f'{n:03}-{k:02}',e['kind'],e['position'],e['text'],'yes'])
  for d in r.get('doubts',[]):doubtrows.append([n,d['place'],d['reading'],d.get('alternatives',''),d.get('confidence','medium'),d.get('reason','')])
 header=['# Collation and changes','','Counts are editorial loci, not character or word edit distances. Changes against C include resolved/introduced uncertainty when the final diplomatic encoding differs; unchanged retained doubts are recorded separately. C and H macro wrappers for the same lettering/underlining are normalized and are not counted as reading changes. A row can differ from both witnesses. High/medium/low count all decision-table rows, including S decisions.','','| Scan | Changes against C | Changes against H | High | Medium | Low |','|---|---:|---:|---:|---:|---:|']
 header+=['| '+' | '.join(map(str,row))+' |' for row in counts]
 if counts:header+=['| Total | '+' | '.join(str(sum(row[i] for row in counts)) for i in range(1,6))+' |']
 header+=['','## Consequential corrections','']+(consequential or ['None recorded yet.'])+['']
 (OUT/'SP33_CW_156-5_changes.md').write_text('\n'.join(header+sections)+'\n')
 for filename,cols,data,delim in [('SP33_CW_156-5_collation.tsv',['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence'],rows,'\t'),('SP33_CW_156-5_inventory.csv',['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed'],inv,',')]:
  with (OUT/filename).open('w',newline='') as f:
   w=csv.writer(f,delimiter=delim);w.writerow(cols);w.writerows(data)
 notation=json.loads((OUT/'records/notation.json').read_text());abbr=json.loads((OUT/'records/abbreviations.json').read_text())
 ds=['# Notation table and remaining doubts','','## Notation table','','| Sign or usage | Ink and LaTeX reading | Image locations |','|---|---|---|']
 ds+=['| '+' | '.join(md(v) for v in row)+' |' for row in notation]
 ds+=['','## Remaining doubts','','| Scan | Place | Reading | Alternatives | Confidence | Reason |','|---|---|---|---|---|---|']
 ds+=['| '+' | '.join(md(v) for v in row)+' |' for row in doubtrows]
 ds+=['','## Abbreviations (expansions only here)','','| As written | Likely expansion |','|---|---|']+['| '+' | '.join(md(v) for v in row)+' |' for row in abbr]
 ds+=['','## Legibility and witness comparison','',(OUT/'records/legibility.txt').read_text() if (OUT/'records/legibility.txt').exists() else 'Assessment in progress; no claim of human verification.']
 (OUT/'SP33_CW_156-5_doubts.md').write_text('\n'.join(ds)+'\n')
 combined=''.join((OUT/'pages'/Path(mapping(r['scan'])['codex_file']).name).read_text() for r in records)
 combined_path=OUT/'SP33_CW_156-5_transcription.tex'
 if frozen:
  if combined!=combined_path.read_text():
   raise RuntimeError('Frozen combined TeX differs from page concatenation; refusing to overwrite')
  # Deliberately do not write even identical bytes after the freeze.
 else:combined_path.write_text(combined)

def save(n,text,record):
 assert not (OUT/'records/frozen_hashes.json').exists(),'Frozen transcription'
 for prev in range(2,n):assert (OUT/'records'/f'scan{prev:03}.json').exists(),f'Previous scan {prev} not saved'
 p=OUT/'pages'/Path(mapping(n)['codex_file']).name
 p.write_text(text.rstrip()+'\n')
 record.update({'scan':n,'completed_utc':utc()})
 (OUT/'records'/f'scan{n:03}.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
 regenerate()
 with (OUT/'progress.log').open('a') as f:f.write(f'scan {n:03} done {utc()}\n')
 state=json.loads((OUT/'records/run_state.json').read_text());state['last_completed_scan']=n;(OUT/'records/run_state.json').write_text(json.dumps(state,indent=2)+'\n')
 print(f'Saved scan {n:03}: {len(record.get("changes",[]))} decision rows; {len(record.get("inventory",[]))} inventory elements.')
if __name__=='__main__':
 if sys.argv[1]=='witness':
  n=int(sys.argv[2]);print('WITNESS C\n'+ctext(n));print('WITNESS H\n'+htext(n))
 elif sys.argv[1]=='regenerate':regenerate()
 elif sys.argv[1]=='crop':print(crop(int(sys.argv[2]),sys.argv[3],list(map(int,sys.argv[4:8])),float(sys.argv[8]) if len(sys.argv)>8 else 0,float(sys.argv[9]) if len(sys.argv)>9 else 2))
