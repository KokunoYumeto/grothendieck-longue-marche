from pathlib import Path
import argparse,csv,re,sys
from datetime import datetime,timezone
ROOT=Path('/workspace/scratch/89f8415d3ab0/deliver')
PREFIX='MPL_81_038-055+154_046-076'
parser=argparse.ArgumentParser(description='Record page inventory, optionally without a completion timestamp.')
parser.add_argument('scan',type=int)
parser.add_argument('sheet_kind',nargs='?',choices=['text','reused_typed','cancelled_draft','cover'])
parser.add_argument('--inventory-only',action='store_true',help='Refresh only inventory rows; do not append to progress.log.')
parser.add_argument('--root',type=Path,default=ROOT,help='Deliverable directory; defaults to this task. Useful for synthetic checks.')
args=parser.parse_args()
ROOT=args.root
scan=args.scan
f=ROOT/f'{PREFIX}_inventory.csv'
with f.open(newline='') as h:old=list(csv.reader(h))
previous_kinds={row[2] for row in old if len(row)>=3 and row[0]=='154' and row[1].isdigit() and int(row[1])==scan}
if args.sheet_kind is not None:
    kind=args.sheet_kind
elif args.inventory_only and len(previous_kinds)==1:
    kind=next(iter(previous_kinds))
elif args.inventory_only and len(previous_kinds)>1:
    parser.error('Existing rows have different sheet kinds; supply sheet_kind explicitly.')
else:
    kind='text'
p=ROOT/'pages'/f'{PREFIX}_154_scan{scan:03d}.tex'
s=p.read_text()
events=[]
markers=list(re.finditer(r'^% E: ([^|]+)\|([^|]+)\|(.+)$',s,re.M))
for m in markers:
    events.append((m.start(),m[1],m[2],m[3]))
for m in re.finditer(r'\\(deleted|inserted|margin)\{',s):
    k=m.end(); depth=1
    while k<len(s) and depth:
        if s[k]=='{' and (k==0 or s[k-1]!='\\'):depth+=1
        if s[k]=='}' and (k==0 or s[k-1]!='\\'):depth-=1
        k+=1
    snippet=re.sub(r'\s+',' ',s[m.end():k-1])
    macro_kind={'deleted':'deletion','inserted':'insertion','margin':'margin note'}[m[1]]
    previous=next((marker for marker in reversed(markers) if marker.end()<=m.start()),None)
    # An explicit element marker immediately followed by its own outer macro
    # already inventories that element. Inner amendments remain separate rows.
    already_marked=previous is not None and previous[1]==macro_kind and not s[previous.end():m.start()].strip()
    if not already_marked:
        pos=(previous[2]+'; ' if previous is not None else '')+f'TeX line {s[:m.start()].count(chr(10))+1}'
        events.append((m.start(),macro_kind,pos,snippet[:160]))
events.sort(key=lambda item:item[0])
rows=[['154',str(scan),kind,str(i),event[1],event[2],event[3],'yes'] for i,event in enumerate(events,1)]
old=[row for row in old if not (len(row)>=2 and row[0]=='154' and row[1].isdigit() and int(row[1])==scan)]
with f.open('w',newline='') as h:csv.writer(h).writerows(old+rows)
if not args.inventory_only:
    with (ROOT/'progress.log').open('a') as h:h.write(f'154 scan {scan:03d} done '+datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')+'\n')
action='Refreshed inventory for' if args.inventory_only else 'Saved'
print(f'{action} scan {scan:03d}: {len(s)} characters; {len(rows)} inventory elements.')
