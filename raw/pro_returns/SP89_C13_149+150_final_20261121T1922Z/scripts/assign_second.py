"""Record a blind second-reading assignment; never supplies first-reading text."""
from pathlib import Path
import json,csv,sys,datetime
W=Path(__file__).resolve().parents[1]
page,reader=sys.argv[1:3]
order=(W/'scripts/page_order.txt').read_text().splitlines()
reports={p:json.loads((W/'reports'/p/'report.json').read_text()) for p in order}
if not all(r.get('main_reviewed') for r in reports.values()):
 raise RuntimeError('All first readings must be finalized before any second assignment')
if reports[page]['reader']==reader:
 raise RuntimeError('Second reader must be different from first reader')
out=W/'second'/f'{page}_assignment.json'
if out.exists():raise RuntimeError('Page already assigned')
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
metadata=dict(page=page,reader=reader,first_reader=reports[page]['reader'],assigned_utc=stamp,
 supplied=['source/SP89_C13_149+150_scans/'+page+'.jpg','work/second/'+page+'_boxes.tsv','work/scripts/second_reader_protocol.md'],
 withheld=['C','H','first.tsv','page transcription','first-reading report','notes','changes'])
out.write_text(json.dumps(metadata,ensure_ascii=False,indent=2)+'\n')
with (W/'reports/assignments.tsv').open('a') as f:
 csv.writer(f,delimiter='\t').writerow(['second',page,reader,stamp])
print(page,reader,stamp)
