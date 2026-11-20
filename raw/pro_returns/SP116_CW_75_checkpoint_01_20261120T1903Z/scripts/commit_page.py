"""Commit an already visually approved record to the assembled logs, then timestamp it."""
from pathlib import Path
import datetime,json,sys
from assemble import assemble
w=Path(__file__).resolve().parents[1]
n=int(sys.argv[1]);r=json.loads((w/'records'/f'scan{n:03}.json').read_text())
base=('J75-01' if n<=9 else 'J75-02')+f'_75_scan{n:03}'
assert (w/'pages'/f'{base}.tex').exists()
assert r.get('root_review')
assemble()
now=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
line=f"scan {n:03} done {now}: {r['line_count']} lines read, {r['crop_count']} places cropped, {len(r['changes'])} rows"
p=w/'progress.log'
assert f'scan {n:03} done ' not in p.read_text(), 'already committed'
with p.open('a') as f:f.write(line+'\n')
print(line)
