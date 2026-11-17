#!/usr/bin/env python3
"""Read-only final ZIP check; no scan reading, OCR, or source mutation."""
from pathlib import Path
import argparse,csv,hashlib,io,json,re,zipfile
p=argparse.ArgumentParser();p.add_argument('archive',type=Path);a=p.parse_args()
with zipfile.ZipFile(a.archive) as z:
 names=z.namelist();assert len(names)==len(set(names))
 assert z.testzip() is None
 assert not any(n.startswith(('scans/','context/','upload/')) or n.endswith(('.jpg','.jpeg','.zip','.pyc')) or '__pycache__' in n for n in names)
 h=json.loads(z.read('records/frozen_hashes.json'))['sha256']
 assert len(h)==39
 for name,digest in h.items():assert hashlib.sha256(z.read(name)).hexdigest()==digest,name
 pages=sorted(n for n in names if n.startswith('pages/') and n.endswith('.tex'))
 assert len(pages)==38
 assert b''.join(z.read(n)+b'\n' for n in pages)==z.read('MPL_64_002-039_transcription.tex')
 inv=list(csv.DictReader(io.StringIO(z.read('MPL_64_002-039_inventory.csv').decode())))
 assert len(inv)==761 and all(x['transcribed']=='yes' for x in inv)
 notes=z.read('MPL_64_002-039_notes.md').decode()
 ids=set(re.findall(r'^### (C64-[NQUT]\d{2})\b',notes,re.M));assert len(ids)==63
 checks=list(csv.DictReader(io.StringIO(z.read('CHECK_EVENTS.tsv').decode()),delimiter='\t'))
 assert len(checks)==196 and ids<={x['statement_id'] for x in checks}
 queries=json.loads(z.read('records/root_context_searches.json'))
 assert ids=={x['note_id'] for x in queries['records']}
 log=z.read('progress.log').decode()
 assert re.search(r'frozen hashes verified unchanged: 39 files 2026-',log)
 local_root=Path(__file__).resolve().parents[1]
 expected={str(f.relative_to(local_root)) for f in local_root.rglob('*') if f.is_file() and '__pycache__' not in f.parts and f.suffix not in {'.pyc','.zip'}}
 assert set(names)==expected,(set(names)-expected,expected-set(names))
 for n in names:assert z.read(n)==(local_root/n).read_bytes(),n
 print(json.dumps({'status':'PASS','archive':str(a.archive.resolve()),'files':len(names),'frozen_hashes_unchanged':39,'pages':len(pages),'inventory_elements':len(inv),'notes':len(ids),'check_events':len(checks),'sources_or_prior_archives_included':False,'all_payload_bytes_match_current_deliverables':True,'archive_bytes':a.archive.stat().st_size},ensure_ascii=False))
