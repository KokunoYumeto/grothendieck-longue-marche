"""Compact textual comparison of independent returns, without image recognition."""
from pathlib import Path
import json,argparse,difflib
p=argparse.ArgumentParser();p.add_argument('scan',type=int);p.add_argument('--reader',choices=list('ABC'));p.add_argument('--mode',choices=['index','issues','notes','inventory','diff','text'],default='index');p.add_argument('--ids',help='Comma-separated issue ids for bounded output');a=p.parse_args()
O=Path(__file__).resolve().parents[1];R=O/f'records/scan{a.scan:03d}'
for label in ([a.reader] if a.reader else list('ABC')):
 f=R/f'reader_{label}/report.json'
 if not f.exists(): print(label,'not yet returned');continue
 d=json.loads(f.read_text());print('\nREADER',label,'issues',len(d['issues']),'crops',d.get('crop_count'))
 if a.ids:d['issues']=[x for x in d['issues'] if x['id'] in set(a.ids.split(','))]
 if a.mode=='index':
  for x in d['issues']: print(x['id'],'|',x['location'],'|',x['reading'],'| C/H',x['diff_C'],x['diff_H'],'|',x['confidence'])
 elif a.mode=='issues':
  for x in d['issues']:print(json.dumps(x,ensure_ascii=False))
 elif a.mode in ['notes','inventory']:print(json.dumps(d.get(a.mode,[]),ensure_ascii=False,indent=2));print('CHECKS',json.dumps(d.get('checks',[]),ensure_ascii=False));print('FEEDBACK',json.dumps(d.get('brief_feedback',[]),ensure_ascii=False))
 elif a.mode=='diff':
  original=O.parent/f'reader_inputs/scan{a.scan:03d}/C.tex'
  print('\n'.join(difflib.unified_diff(original.read_text().splitlines(),(R/f'reader_{label}/reading.tex').read_text().splitlines(),fromfile='witness C',tofile='reader '+label,n=2)))
 elif a.mode=='text':print((R/f'reader_{label}/reading.tex').read_text())
