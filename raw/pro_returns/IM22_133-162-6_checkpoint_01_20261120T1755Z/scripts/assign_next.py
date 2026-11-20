"""Main-reader's ordered single-page dispatcher. No OCR or content analysis."""
from pathlib import Path
from datetime import datetime, timezone
import fcntl, json, sys
W = Path(__file__).resolve().parents[1]
reader, previous = sys.argv[1:3]
assert reader in ('reader_1','reader_2','reader_3')
with (W/'dispatch.lock').open('a+') as lock:
    fcntl.flock(lock, fcntl.LOCK_EX)
    state = json.loads((W/'dispatch.json').read_text())
    assert state['current'].get(reader) == previous, (reader,previous,state)
    assert (W/'page_jobs'/previous/'result.json').exists(), 'Return the current page first'
    order = json.loads((W/'page_order.json').read_text())
    if state['next_index'] == len(order):
        state['current'][reader] = None
        print('ALL_PAGES_ASSIGNED. Stop; await final review requests.')
    else:
        stem = order[state['next_index']]
        state['next_index'] += 1
        state['current'][reader] = stem
        state['history'].append({'reader':reader,'stem':stem,'assigned_utc':datetime.now(timezone.utc).isoformat()})
        print(f'Your ONLY next assigned page is {W / "page_jobs" / stem / "input.json"}. Follow reader_instructions.md. Return result.json, notify the main reader, then request one next page using this dispatcher.')
    (W/'dispatch.json').write_text(json.dumps(state,indent=2)+'\n')
