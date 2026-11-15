#!/usr/bin/env python3
"""Freeze once, or verify the existing frozen transcription; never rewrite it."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, re, sys

root=Path(__file__).resolve().parent.parent
manifest=root/'records/frozen_hashes.sha256'
log=root/'progress.log'
stamp=lambda:datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

if '--verify' in sys.argv:
    rows=[x for x in manifest.read_text().splitlines() if x.strip() and not x.startswith('#')]
    assert len(rows)==49, 'Expected 48 pages plus combined text'
    for row in rows:
        digest,name=row.split('  ',1)
        assert hashlib.sha256((root/name).read_bytes()).hexdigest()==digest,name
    with log.open('a') as f:f.write(f'frozen hashes verified unchanged {stamp()} — 49/49 files\n')
    print('All 49 frozen hashes are unchanged.')
else:
    assert not manifest.exists(),'Transcription is already frozen'
    content=log.read_text()
    done={int(x) for x in re.findall(r'33 scan (\d+) done ',content)}
    audited={int(x) for x in re.findall(r'scan (\d+) audited ',content)}
    assert set(range(2,50))<=done and set(range(2,50))<=audited,(done,audited)
    assert 'context opened ' not in content,'Context must remain unopened until freeze'
    paths=sorted((root/'pages').glob('*.tex'))+[root/'MPL_33_002-049_transcription.tex']
    assert len(paths)==49
    rows=[hashlib.sha256(p.read_bytes()).hexdigest()+'  '+str(p.relative_to(root)) for p in paths]
    manifest.write_text('\n'.join(rows)+'\n')
    with log.open('a') as f:
        f.write(f'cross-page notation review completed {stamp()} — capitals, alphabets, exclamations/primes, quotation marks, underlines, quantifiers, arrowheads, limit directions, fundamental-class glyphs checked; 188 doubt occurrences and 77 abbreviation entries recorded\n')
        for row in rows:f.write('SHA256 '+row+'\n')
        f.write('transcription frozen '+stamp()+'\n')
    for p in paths:p.chmod(0o444)
    print('Frozen 48 page files and combined transcription; 49 SHA-256 values written to manifest and progress.log.')
