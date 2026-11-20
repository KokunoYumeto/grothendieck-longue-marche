"""List inventory and mathematical notes for manual coverage review."""
from pathlib import Path
import json,sys
out=Path(__file__).resolve().parents[1];s=int(sys.argv[1])
for r in ['R1','R2','R3']:
 d=json.loads((out/'readers'/f'scan{s:03d}'/r/'report.json').read_text())
 print('\n'+r+' INVENTORY')
 for x in d['inventory']:print(x['element'],x['kind'],x['position'],'|',x['first_words_or_objects'],'|',x['transcribed'])
 print('NOTES',json.dumps(d['notes'],ensure_ascii=False))
 print('EVENTS',json.dumps(d.get('check_events',[]),ensure_ascii=False))
 print('NOTATION',json.dumps(d.get('notation',[]),ensure_ascii=False))
