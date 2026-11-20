"""Prepare the next ordered page's notation snapshot; never overwrite reader work."""
from pathlib import Path
from datetime import datetime,timezone
import json,shutil,sys
O=Path(__file__).resolve().parents[1]
W=O.parent
n=int(sys.argv[1]); brief=sys.argv[2] if len(sys.argv)>2 else 'v08'
order=json.loads((O/'page_order.json').read_text())
expected=[int(x['our_scan']) for x in order]
done=[json.loads(p.read_text()) for p in sorted((O/'decisions').glob('scan*.json'))]
assert all(d.get('decided_utc') for d in done),'Finish committing the current page first.'
assert [d['scan'] for d in done]==expected[:len(done)],'Committed pages are not an ordered prefix.'
assert len(done)<len(expected) and expected[len(done)]==n,'Only the next supplied page may be prepared.'
assert (O/f'briefs/brief_{brief}.md').exists(),'Missing reader brief.'
packet=W/f'packets/scan{n:03}'
for name in ['meta.json','C.tex','H.tex','C_context.md']:
    assert (packet/name).is_file(),f'Missing packet component {name}'
for a in 'ABC':
    p=O/f'readers/scan{n:03}/{a}'
    assert not p.exists() or not any(p.iterdir()),f'Existing reader work must be preserved: {p}'
snap=O/f'briefs/notation_snapshots/scan{n:03}.json'
assert not snap.exists(),'Do not replace an existing page snapshot.'
for a in 'ABC':(O/f'readers/scan{n:03}/{a}').mkdir(parents=True,exist_ok=True)
shutil.copy2(O/'notation.json',packet/'notation.json')
shutil.copy2(O/'notation.json',snap)
t=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (O/'progress.log').open('a') as f:f.write(f'scan {n:03} fresh-reader packet prepared under brief {brief} {t}; previous pages committed; notation snapshot saved\n')
print(json.dumps({'scan':n,'brief':brief,'prepared_utc':t,'packet':str(packet),'outputs':[str(O/f'readers/scan{n:03}/{a}') for a in 'ABC']},ensure_ascii=False))
