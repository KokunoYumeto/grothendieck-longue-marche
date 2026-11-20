"""Print complete independent readings and compact reports for main adjudication."""
from pathlib import Path
import argparse,json
parser=argparse.ArgumentParser()
parser.add_argument('scan',type=int)
parser.add_argument('fields',nargs='*')
parser.add_argument('--reader',choices=['A','B','C','ABC'],default='ABC')
args=parser.parse_args()
n=args.scan;root=Path(__file__).resolve().parents[1]
fields=args.fields or ['reading','differences','unresolved','notes','workflow_feedback']
reports={}
for reader in 'ABC':
    p=root/f'records/scan{n}/{reader}/report.json'
    if not p.exists():raise SystemExit(f'{reader}: report not available; wait for all three complete returns')
    reports[reader]=json.loads(p.read_text())
    if not reports[reader].get('complete'):raise SystemExit(f'{reader}: report incomplete; wait for all three complete returns')
for reader in args.reader:
 folder=root/f'records/scan{n}/{reader}'
 p=folder/'report.json'
 if not p.exists():print(f'{reader}: report not available');continue
 report=reports[reader]
 print(f'\nREADER {reader}')
 for key in fields:
  print('\n'+key)
  if key=='reading':print((folder/'reading.tex').read_text())
  elif key=='differences':
   for i,item in enumerate(report.get(key,[])):print(str(i)+' '+json.dumps(item,ensure_ascii=False))
  else:print(json.dumps(report.get(key),ensure_ascii=False,indent=2))
