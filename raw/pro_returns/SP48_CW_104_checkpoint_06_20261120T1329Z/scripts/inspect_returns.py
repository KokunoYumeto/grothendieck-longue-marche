"""Print compact reader returns for manual comparison; does not infer readings."""
from pathlib import Path
import json,sys
O=Path(__file__).resolve().parents[1]
n=int(sys.argv[1])
for a in 'ABC':
 p=O/f'records/scan{n:03d}/reader_{a}/report.json'
 if not p.exists():
  print('reader',a,'not returned');continue
 d=json.loads(p.read_text())
 print('\nREADER',a,'crops',d.get('crop_count'),'issues',len(d.get('issues',[])))
 for i in d.get('issues',[]):
  print(i['id'],i['location'])
  print(' C:',i.get('C',''),' H:',i.get('H',''))
  print(' R:',i.get('reading',''),' confidence:',i.get('confidence'),' diffs:',i.get('diff_C'),i.get('diff_H'))
  print(' Ink:',i.get('evidence',''))
  print(' Crop:',i.get('crop',''),' bbox:',i.get('bbox',''))
 print('NOTES',json.dumps(d.get('notes',[]),ensure_ascii=False))
 print('CHECKS',json.dumps(d.get('checks',[]),ensure_ascii=False))
 print('FEEDBACK',json.dumps(d.get('brief_feedback',[]),ensure_ascii=False))
