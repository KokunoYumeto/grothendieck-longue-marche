"""Assign one frozen image-only audit page to a different first-pass reader."""
from pathlib import Path
from datetime import datetime, timezone
import json
import sys

BASE = Path(__file__).resolve().parents[1]
ROOT = BASE.parents[1]

def assign(reader, requested=None):
    assert reader in ['reader_a', 'reader_b', 'reader_c']
    state = json.loads((ROOT / 'run_state.json').read_text())
    manifest = json.loads((BASE / 'second' / 'input_manifest.json').read_text())
    assert len(state['accepted']) == 23
    assignments = state.setdefault('audit_assignments', {})
    previous = assignments.get(reader)
    if previous:
        report = json.loads((BASE / 'reviews' / f'{previous}.json').read_text())
        assert report.get('audit', {}).get('completed_utc'), 'Root must finish the previous audit first'
    assigned = state.setdefault('audit_assigned', [])
    choices = [page for page in state['scans']
               if page not in assigned and manifest['pages'][page]['first_reader'] != reader]
    page = requested or (choices[0] if choices else None)
    assert page is None or page in choices, 'Page already assigned or previously read by this reader'
    assignments[reader] = page
    stamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    if page:
        assigned.append(page)
        with (BASE / 'progress.log').open('a') as log:
            log.write(f'{page} independent audit assigned {stamp}: {reader}; original image and frozen box list only\n')
    for path in [ROOT / 'run_state.json', BASE / 'run_state.json']:
        path.write_text(json.dumps(state, indent=2) + '\n')
    print(json.dumps({'reader': reader, 'page': page, 'utc': stamp}))

if __name__ == '__main__':
    assign(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
