"""Archive a page's actual notation input and register its fresh readers."""
from pathlib import Path
import json,sys
W=Path(__file__).resolve().parents[1]
n=int(sys.argv[1]);state=json.loads((W/'state.json').read_text())
mapping=json.loads((W/'page_map.json').read_text())
order=[int(x['our_scan']) for x in mapping]
assert n==order[len(state['done'])], 'Complete the preceding page before preparing another.'
snapshot=W/f'briefs/notation_before_{n:03}.md'
notation=(W/'notation.md').read_text()
if snapshot.exists():
 assert snapshot.read_text()==notation, 'Do not silently change an existing reader input.'
else:snapshot.write_text(notation)
(W/f'inputs/{n:03}/notation.md').write_text(notation)
state['current_scan']=n
state['active_readers']=[f'/root/scan{n:03}_{r}' for r in 'abc']
(W/'state.json').write_text(json.dumps(state,indent=2))
print(f'Prepared scan {n:03}; brief version {state["brief_version"]}; three fresh readers required.')
