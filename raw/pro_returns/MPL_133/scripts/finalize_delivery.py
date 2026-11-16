#!/usr/bin/env python3
"""One-time delivery packaging after the review; no frozen TeX file is modified."""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, json, re, subprocess, sys, zipfile
from collections import Counter

root=Path(__file__).resolve().parents[1]
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
frozen=json.loads((root/'records/frozen_sha256.json').read_text())
assert len(frozen)==51
for name,digest in frozen.items():
    assert hashlib.sha256((root/name).read_bytes()).hexdigest()==digest, name

notes=(root/'MPL_133_notes.md').read_text()
ids=re.findall(r'^### ([WPFBGJM]\d\d)\b',notes,re.M)
ledger=[json.loads(x) for x in (root/'records/context_searches.jsonl').read_text().splitlines()]
assert len(ids)==len(set(ids))==76
assert {x['note_id'] for x in ledger}==set(ids)
assert all(x['execution']['exit_code'] in (0,1) for x in ledger)
with (root/'MPL_133_inventory.csv').open(newline='') as stream:
    rows=list(csv.DictReader(stream))
assert len(rows)==809 and all(x['transcribed']=='yes' for x in rows)
scans={int(x['scan']):x['sheet_kind'] for x in rows}
assert Counter(scans.values())=={'cover':3,'text':37,'reused_typed':10}

(root/'records/WORK_STATUS.md').write_text(f'''# Work status: complete

Completed and packaged at {now}. All 50 supplied pages were transcribed and separately visually audited by one primary transcriber. The combined fragment compiled unchanged in the mechanical integration test. All 51 frozen TeX hashes were checked again after research and are unchanged.

The final main report contains 76 numbered notes, both standing registers, results-state reconciliation, and 27 references. The context-search ledger contains 76 executed query records with precise locators and bounded negatives. Longer proof checks remain in the research supplements.

The first hourly checkpoint was saved at 2026-11-16 22:38:56 UTC. Final delivery contains all principal files, records, logs, scripts, notes, and supporting calculations, excluding the supplied archives/scans/context, external source files, and temporary compilation products.

Do not rerun page-writing, audit-update, repair, assembly, reduction, or packaging scripts on this frozen delivery. The read-only `scripts/validate_package.py` is the final consistency checker. The main notes and final doubts supersede preliminary working observations; no mathematical finding was applied back to the frozen transcription.
''')
with (root/'progress.log').open('a') as stream:
    stream.write(f'research notes completed {now}: 76 numbered notes, 76 context-search records, both standing registers, 27 references, and proof supplements\n')
    stream.write(f'final hash verification {now}: all 51 frozen SHA-256 hashes unchanged (50 page files and combined transcription)\n')
    stream.write(f'final delivery prepared {now}: MPL_133.zip; source archives, scans/context, external literature and compile outputs excluded\n')

check=subprocess.run([sys.executable,str(root/'scripts/validate_package.py')],capture_output=True,text=True)
assert check.returncode==0,check.stdout+check.stderr
result=json.loads(check.stdout)
(root/'records/final_validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')

excluded={'.pyc','.jpg','.jpeg','.png','.pdf','.zip','.dvi','.aux','.toc','.out','.synctex'}
files=[p for p in root.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix.lower() not in excluded]
assert not any(p.is_symlink() for p in files)
assert not any(p.name in {'ps6.tex','ps7.tex','PROMPT(20261116-213727).md'} for p in files)
manifest=root/'records/package_manifest.json'
files=[p for p in files if p!=manifest]
manifest.write_text(json.dumps({'created_utc':now,'excludes_manifest_self_hash':True,'files':[{'path':p.relative_to(root).as_posix(),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(files)]},ensure_ascii=False,indent=2)+'\n')
files.append(manifest)
destination=root.parent/'MPL_133.zip'
with zipfile.ZipFile(destination,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as archive:
    for p in sorted(files):
        archive.write(p,p.relative_to(root).as_posix())
with zipfile.ZipFile(destination) as archive:
    assert archive.testzip() is None
    names=archive.namelist()
    assert len([n for n in names if n.startswith('pages/') and n.endswith('.tex')])==50
    for name,digest in frozen.items():
        assert hashlib.sha256(archive.read(name)).hexdigest()==digest
print(json.dumps({'archive':str(destination),'bytes':destination.stat().st_size,'files':len(files),'notes':len(ids),'context_records':len(ledger),'frozen_hashes_unchanged':len(frozen),'validation':result['ok'],'archive_sha256':hashlib.sha256(destination.read_bytes()).hexdigest()},indent=2))
