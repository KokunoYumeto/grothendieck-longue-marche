#!/usr/bin/env python3
"""Keep downloaded third-party reading material outside the deliverable."""
from pathlib import Path
import hashlib
import json

root = Path(__file__).resolve().parent.parent
old = root / 'research' / 'primary_sources'
new = root.parent / 'source_cache' / 'Ihara_beta_gamma'
new.mkdir(parents=True, exist_ok=True)
records = []
for source in sorted(old.iterdir()):
    if source.is_file():
        target = new / source.name
        assert not target.exists()
        records.append({'filename': source.name,
                        'sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
                        'bytes': source.stat().st_size,
                        'reading_cache_path': str(target)})
        source.rename(target)
old.rmdir()
(root / 'research' / 'primary_reading_cache.json').write_text(
    json.dumps(records, indent=2) + '\n')
print(json.dumps(records, indent=2))
