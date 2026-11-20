"""Store manually adjudicated blind-box decisions, preserving both original readings.
Usage: record_second_decisions.py PAGE MANUAL_JSON [--finish SECOND_READER]
Each manual row needs box, decision, changed, reason and either final or an explicit
use='first'/'second'. This script stores decisions; it does not decide or edit pages.
The caller must have inspected the saved second-reading crop for every difference.
"""
from pathlib import Path
import csv,json,sys,datetime
O=Path(__file__).resolve().parents[1];page=sys.argv[1];manual=Path(sys.argv[2])
def rows(suffix):
 with (O/'second'/f'{page}_{suffix}.tsv').open(newline='') as f:return list(csv.DictReader(f,delimiter='\t'))
first={r['box']:r['reading'] for r in rows('first')};second={r['box']:r['reading'] for r in rows('second')};boxes={r['box']:r for r in rows('boxes')}
diffs={r['box'] for r in rows('comparison') if r['equal_tokens']=='no'}
dest=O/'second'/f'{page}_decisions.json';stored={r['box']:r for r in json.loads(dest.read_text())} if dest.exists() else {}
for r in json.loads(manual.read_text()):
 b=r['box'];assert b in diffs,(b,'not a token difference');assert b not in stored,(b,'already adjudicated')
 assert isinstance(r.get('changed'),bool);assert r.get('reason');assert r.get('decision')
 use=r.get('use');assert use in (None,'first','second')
 final=r['final'] if 'final' in r else {'first':first[b],'second':second[b]}[use]
 crop=r.get('crop',f'crops/second/{page}/{b}.png');assert(O/crop).is_file(),crop
 coords=r.get('coords',[int(boxes[b][k]) for k in ['x0','y0','x1','y1']])
 stored[b]={'box':b,'first':first[b],'second':second[b],'final':final,'decision':r['decision'],'changed':r['changed'],'reason':r['reason'],'crop':crop,'coords':coords}
ordered=[stored[b] for b in boxes if b in stored];dest.write_text(json.dumps(ordered,ensure_ascii=False,indent=2)+'\n')
print(f'{page}: {len(stored)}/{len(diffs)} differences adjudicated')
if '--finish' in sys.argv:
 assert set(stored)==diffs,sorted(diffs-set(stored))
 reader=sys.argv[sys.argv.index('--finish')+1];report=json.loads((O/'work'/f'{page}_decided.json').read_text());assert reader!=report['first_reader']
 auditpath=O/'second'/f'{page}_audit.json';assert not auditpath.exists(),'Audit already finalized'
 now=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');changed=sum(r['changed'] for r in stored.values())
 audit={'page':page,'first_reader':report['first_reader'],'second_reader':reader,'boxes':len(boxes),'differences':len(diffs),'changed':changed,'audited_utc':now}
 auditpath.write_text(json.dumps(audit,indent=2)+'\n')
 with (O/'progress.log').open('a') as f:f.write(f'{page}: scan {page.rsplit("scan",1)[1]} audited {now}: {len(boxes)} boxes read, {len(diffs)} differences, {changed} changed; second reader {reader}; root decided every token difference on its saved crop.\n')
 print(json.dumps(audit))
