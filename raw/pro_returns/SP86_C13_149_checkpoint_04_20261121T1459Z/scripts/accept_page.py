"""Record an already-adjudicated page and prepare the next single-page assignment."""
from pathlib import Path
from datetime import datetime, timezone
import json
import shutil
import sys
import assemble
import validate

BASE = Path(__file__).resolve().parents[1]
ROOT = BASE.parents[1]

def accept(page, next_page=None):
    path = BASE / 'reviews' / (page + '.json')
    report = json.loads(path.read_text())
    assert report.get('root_adjudication') and report.get('root_viewed')
    assert (BASE / 'pages' / (page + '.tex')).exists()
    state = json.loads((ROOT / 'run_state.json').read_text())
    assert page not in state['accepted'], 'Already accepted'
    assert state['assignments'][report['reader']] == page
    stamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    report['accepted_utc'] = stamp
    path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    crop_count = len({x for x in report['viewed'] if str(x).startswith('crops/')})
    with (BASE / 'progress.log').open('a') as log:
        log.write(f"scan {report['scan']:03d} done {stamp} cote 149: {report['line_count']} lines read, {crop_count} places cropped, {len(report['changes'])} rows\n")
    state['accepted'].append(page)
    if next_page:
        assert state['scans'][state['next_index']] == next_page
        state['next_index'] += 1
        state['assignments'][report['reader']] = next_page
    else:
        state['assignments'][report['reader']] = None
    for target in [ROOT / 'run_state.json', BASE / 'run_state.json']:
        target.write_text(json.dumps(state, indent=2) + '\n')
    assemble.build()
    result = validate.validate()
    if result['errors']:
        raise ValueError(result['errors'])
    if next_page:
        shutil.copyfile(BASE / 'notation.md', ROOT / 'packets' / next_page / 'notation.md')
    print(json.dumps({'accepted': page, 'utc': stamp, 'next': next_page}))

if __name__ == '__main__':
    accept(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
