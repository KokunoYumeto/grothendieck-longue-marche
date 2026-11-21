"""Verify the final ZIP against the completed work tree and frozen text."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import sys
import zipfile

work = Path(__file__).resolve().parents[1]
archive = Path(sys.argv[1]).resolve()
expected = {str(p.relative_to(work)): p for p in work.rglob('*')
            if p.is_file() and '__pycache__' not in p.parts and p.suffix != '.zip'}
with zipfile.ZipFile(archive) as z:
    infos = z.infolist()
    names = [i.filename for i in infos]
    assert len(names) == len(set(names)), 'Duplicate ZIP members'
    assert set(names) == set(expected), 'Archive/work-tree member mismatch'
    assert z.testzip() is None, 'ZIP CRC failure'
    for i in infos:
        assert i.file_size == expected[i.filename].stat().st_size, i.filename
        parts = Path(i.filename).parts
        assert not any(x in parts for x in ['source', 'upload', 'reading_packets']), i.filename
        assert not i.filename.endswith('.zip'), i.filename
    json_count = 0
    for name in names:
        if name.endswith('.json'):
            json.loads(z.read(name))
            json_count += 1
    frozen = json.loads(z.read('audit/frozen_transcription_sha256.json'))
    for name, digest in frozen['sha256'].items():
        assert hashlib.sha256(z.read(name)).hexdigest() == digest, name
        assert hashlib.sha256(expected[name].read_bytes()).hexdigest() == digest, name
    state = json.loads(z.read('run_state.json'))
    assert len(state['order']) == len(state['completed']) == len(state['audited']) == 24
    result = {'utc': datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
              'archive': archive.name, 'bytes': archive.stat().st_size,
              'members': len(names), 'json_files_parsed': json_count,
              'crc': 'pass', 'complete_work_tree': True,
              'frozen_files_unchanged': len(frozen['sha256']),
              'source_inputs_or_prior_archives_included': False,
              'sha256': hashlib.sha256(archive.read_bytes()).hexdigest()}
print(json.dumps(result, indent=2))
