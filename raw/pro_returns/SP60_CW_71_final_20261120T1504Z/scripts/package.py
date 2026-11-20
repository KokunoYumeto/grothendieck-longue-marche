"""Freeze, verify and archive the completed single-reader transcription.
No OCR, source reading or TeX compilation is performed here.
"""
from pathlib import Path
from datetime import datetime,timezone
import argparse,hashlib,re,zipfile

ROOT=Path(__file__).resolve().parents[1]
PREFIX='SP60_CW_71'
def utc():return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def transcription_files():return sorted((ROOT/'pages').glob('*.tex'))+[ROOT/(PREFIX+'_transcription.tex')]
def freeze():
 p=ROOT/'progress.log';s=p.read_text()
 if 'transcription frozen ' in s:raise SystemExit('Already frozen; no new freeze written.')
 files=transcription_files();assert len(files)==12
 with p.open('a') as f:
  f.write('transcription frozen '+utc()+'\n')
  for q in files:f.write('sha256 '+digest(q)+' '+q.relative_to(ROOT).as_posix()+'\n')
 print('Frozen 11 page files and the combined transcription.')
def verify(log=False):
 s=(ROOT/'progress.log').read_text();found=re.findall(r'^sha256 ([0-9a-f]{64}) (.+)$',s,re.M)
 expected={q.relative_to(ROOT).as_posix() for q in transcription_files()}
 assert len(found)==12 and {p for h,p in found}==expected
 for h,p in found:assert digest(ROOT/p)==h, 'Changed frozen file: '+p
 if log:
  with (ROOT/'progress.log').open('a') as f:f.write('frozen hashes unchanged '+utc()+' — all 11 page files and the combined transcription match the recorded SHA-256 values.\n')
 print('All 12 frozen hashes are unchanged.')
def build(target):
 verify()
 target=target.resolve()
 if target.exists():raise SystemExit('Refusing to overwrite an existing ZIP: '+str(target))
 allowed={'.tex','.md','.tsv','.csv','.log','.py','.txt'}
 files=[p for p in sorted(ROOT.rglob('*')) if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc']
 for p in files:
  assert p.suffix in allowed, 'Unexpected artifact type: '+str(p)
  assert p.name!='PREAMBLE.tex', 'An input preamble must not be returned.'
 with zipfile.ZipFile(target,'x',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
  for p in files:z.write(p,p.relative_to(ROOT).as_posix())
 print(str(target)+'; '+str(len(files))+' files; '+str(target.stat().st_size)+' bytes; sha256 '+digest(target))

if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('action',choices=['freeze','verify','build']);a.add_argument('--log',action='store_true');a.add_argument('--target',type=Path);ns=a.parse_args()
 if ns.action=='freeze':freeze()
 elif ns.action=='verify':verify(ns.log)
 else:
  assert ns.target,'--target is required for build'
  build(ns.target)
