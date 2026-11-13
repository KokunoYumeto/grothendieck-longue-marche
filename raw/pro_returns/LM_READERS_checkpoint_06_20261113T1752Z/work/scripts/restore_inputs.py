"""Verify and unpack the three supplied archives into sources/.
Usage: python work/scripts/restore_inputs.py LM_FR.zip LM_EN.zip LM_TYPESET.zip
The input manifests are read and checked before any source file is extracted.
"""
from pathlib import Path
import argparse,csv,hashlib,io,json,zipfile
ROOT=Path(__file__).resolve().parents[2]
def main():
 ap=argparse.ArgumentParser();ap.add_argument('archives',nargs=3);a=ap.parse_args()
 out=ROOT/'sources';out.mkdir(exist_ok=True);records=[]
 for arg in a.archives:
  p=Path(arg)
  with zipfile.ZipFile(p) as z:
   manifest=z.read('MANIFEST.tsv').decode('utf-8');rows=list(csv.DictReader(io.StringIO(manifest),delimiter='\t'))
   for row in rows:
    data=z.read(row['path'])
    if len(data)!=int(row['bytes']) or hashlib.sha256(data).hexdigest()!=row['sha256']:raise ValueError('Manifest mismatch: '+p.name+':'+row['path'])
   for item in z.infolist():
    if item.filename=='MANIFEST.tsv':
     (out/(p.stem+'_MANIFEST.tsv')).write_bytes(z.read(item));continue
    q=Path(item.filename)
    if q.is_absolute() or '..' in q.parts:raise ValueError('Unsafe archive member')
    target=out/q;target.parent.mkdir(parents=True,exist_ok=True)
    if not item.is_dir():target.write_bytes(z.read(item))
   records.append({'archive':p.name,'files':len(rows),'status':'all byte counts and SHA-256 hashes verified'})
 (ROOT/'work/records').mkdir(parents=True,exist_ok=True)
 (ROOT/'work/records/INPUT_MANIFEST_VERIFICATION.json').write_text(json.dumps(records,indent=2)+'\n')
 print(json.dumps(records,indent=2))
if __name__=='__main__':main()
