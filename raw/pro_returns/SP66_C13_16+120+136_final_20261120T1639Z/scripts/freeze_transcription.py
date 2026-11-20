"""Freeze or verify the 25 page fragments and combined transcription by SHA-256."""
from pathlib import Path
import argparse,csv,hashlib,re
from datetime import datetime,timezone

ROOT=Path(__file__).resolve().parents[1]
PREFIX='SP66_C13_16+120+136'
def now():return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def paths():
 rows=list(csv.DictReader((ROOT/(PREFIX+'_inventory.csv')).open()))
 keys=list(dict.fromkeys(r['scan'] for r in rows))
 if len(keys)!=25:raise ValueError('Expected 25 pages')
 return ['pages/'+k+'.tex' for k in keys]+[PREFIX+'_transcription.tex']
def digest(name):return hashlib.sha256((ROOT/name).read_bytes()).hexdigest()

p=argparse.ArgumentParser(description=__doc__)
g=p.add_mutually_exclusive_group(required=True)
g.add_argument('--freeze',action='store_true')
g.add_argument('--verify',action='store_true')
args=p.parse_args()
log=ROOT/'progress.log';before=log.read_text();names=paths()
if args.freeze:
 if re.search(r'^transcription frozen ',before,re.M):raise RuntimeError('Transcription is already frozen')
 if len(re.findall(r'^scan \d+ audited .* cote \d+$',before,re.M))!=25:raise RuntimeError('All 25 audit entries are required')
 with log.open('a') as f:
  f.write('transcription frozen '+now()+'\n')
  for name in names:f.write('sha256 '+digest(name)+' '+name+'\n')
 print('Frozen 26 transcription files; hashes recorded in progress.log')
else:
 recorded=dict((name,value) for value,name in re.findall(r'^sha256 ([0-9a-f]{64}) (.+)$',before,re.M))
 if set(recorded)!=set(names):raise RuntimeError('Frozen path set does not match the 26 transcription files')
 changed=[name for name in names if digest(name)!=recorded[name]]
 if changed:raise RuntimeError('Transcription changed after freeze: '+', '.join(changed))
 with log.open('a') as f:f.write('transcription hashes verified unchanged '+now()+'; all 25 page files and the combined transcription (26 SHA-256 hashes)\n')
 print('All 26 frozen transcription hashes are unchanged')
