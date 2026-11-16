from pathlib import Path
import argparse, hashlib, json, sys
sys.path.insert(0,str(Path(__file__).resolve().parent))
from page_work import ROOT,PREFIX,utc

parser=argparse.ArgumentParser()
parser.add_argument('action',choices=['freeze','verify'])
args=parser.parse_args()
manifest=ROOT/'records/frozen_hashes.json'
pages=sorted((ROOT/'pages').glob(f'{PREFIX}_43_scan*.tex'))
paths=pages+[ROOT/f'{PREFIX}_transcription.tex']
expected=[n for n in range(94,143) if n not in (99,111,127)]
assert [int(p.stem[-3:]) for p in pages]==expected
assert (ROOT/f'{PREFIX}_transcription.tex').read_bytes()==b''.join(p.read_bytes() for p in pages)
hashes={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
if args.action=='freeze':
 if manifest.exists():raise RuntimeError('Already frozen')
 log=(ROOT/'progress.log').read_text()
 assert 'context opened' not in log
 assert all(f'scan {n:03} audited ' in log for n in expected)
 stamp=utc()
 manifest.write_text(json.dumps({'time':stamp,'algorithm':'SHA-256','files':hashes},indent=2)+'\n',encoding='utf-8')
 with (ROOT/'progress.log').open('a',encoding='utf-8') as f:
  for rel,sha in hashes.items():f.write(f'sha256 {sha} {rel}\n')
  f.write('transcription frozen '+stamp+'\n')
 print('Frozen 46 page files and combined transcription at '+stamp)
else:
 saved=json.loads(manifest.read_text())
 assert hashes==saved['files'],'Frozen transcription hash mismatch'
 with (ROOT/'progress.log').open('a',encoding='utf-8') as f:f.write('frozen hashes unchanged '+utc()+'\n')
 print('All 47 frozen hashes unchanged')

