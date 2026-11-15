"""Read-only package checks; --freeze records hashes once, --verify checks them.
This does not read source images or the supplied context.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib,re,csv,argparse
root=Path(__file__).resolve().parents[1]
a=argparse.ArgumentParser();a.add_argument('--freeze',action='store_true');a.add_argument('--verify',action='store_true');args=a.parse_args()
pages=sorted((root/'pages').glob('*.tex'))
assert [int(p.stem[-3:]) for p in pages]==list(range(50,98))
texts=[p.read_text() for p in pages]
combined=root/'MPL_33_050-097_transcription.tex'
assert combined.read_text()=='\n'.join(s.rstrip()+'\n' for s in texts)
assert re.findall(r'\\scanpage\{(\d+)\}',combined.read_text())==[str(n) for n in range(50,98)]
assert combined.read_text().startswith('\\cotefile{33}\n\\scanpage{50}')
assert combined.read_text().count('\\cotefile{')==1
assert '\\documentclass' not in combined.read_text()
for p,s in zip(pages,texts):
 stack=[]
 for m in re.finditer(r'\\[A-Za-z]+|\\.|[{}]',s):
  if m.group()=='{':stack.append(m.start())
  elif m.group()=='}':assert stack,(p,'extra closing brace');stack.pop()
 assert not stack,(p,'open grouping brace')
rows=list(csv.DictReader((root/'MPL_33_050-097_inventory.csv').open()))
assert set(r['scan'] for r in rows)==set(map(str,range(50,98)))
assert all(r['transcribed']=='yes' for r in rows)
assert len(set(r['element'] for r in rows))==len(rows)
assert set(r['sheet_kind'] for r in rows)<={'text','reused_typed','cancelled_draft','cover'}
log=(root/'progress.log').read_text()
assert set(re.findall(r'^33 scan (\d+) done ',log,re.M))==set(f'{n:03d}' for n in range(50,98))
assert set(re.findall(r'^scan (\d+) audited ',log,re.M))==set(f'{n:03d}' for n in range(50,98))
paths=pages+[combined]
hashes={p.relative_to(root).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
manifest=root/'records/transcription_sha256.txt'
now=lambda:datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
if args.freeze:
 assert not manifest.exists(),'Transcription already frozen'
 assert 'context opened' not in log,'Context already opened'
 manifest.write_text(''.join(f'{v}  {k}\n' for k,v in hashes.items()))
 with (root/'progress.log').open('a') as f:
  for k,v in hashes.items():f.write(f'SHA-256 {k} {v}\n')
  f.write(f'transcription frozen {now()}\n')
if args.verify:
 expected={line.split('  ',1)[1]:line.split('  ',1)[0] for line in manifest.read_text().splitlines()}
 assert hashes==expected,'Frozen transcription changed'
 with (root/'progress.log').open('a') as f:f.write(f'frozen transcription hashes unchanged (48 page files and combined fragment) {now()}\n')
print(f'PASS: {len(pages)} pages, {len(rows)} complete inventory elements, ordered combined fragment, balanced grouping braces, all done/audit log entries.')
if args.freeze:print('49 SHA-256 hashes recorded; transcription frozen.')
if args.verify:print('49 SHA-256 hashes unchanged.')
