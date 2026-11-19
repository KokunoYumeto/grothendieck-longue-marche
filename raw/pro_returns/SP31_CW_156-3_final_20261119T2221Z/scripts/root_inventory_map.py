"""Explicit root mappings after all24 sequential image audits; no text inference."""
from work import *
anchors={2:{1:5,3:22,4:29},3:{2:6,5:24,6:27,7:39},4:{1:4,2:8,4:15,5:17,7:34},5:{1:4,2:15,7:43},6:{2:11,4:16},7:{1:4,4:18},8:{2:9,3:14},9:{1:4,2:6,3:10,4:12,6:19,7:22,8:24},10:{2:6,3:12},11:{1:3,10:36},12:{2:6,4:15,5:24,7:34,10:45},13:{1:3,5:24},14:{6:24,7:26,8:26,11:38},17:{1:3,2:6,5:15,7:21,8:24,9:27},18:{1:2,6:12,8:16},19:{2:5,3:18},20:{1:4,5:26},21:{3:10,4:12,5:17},22:{1:2,3:11,4:13},23:{3:6,4:7},24:{3:13},25:{3:7}}
with (OUT/'audit/inventory_root_mapping.tsv').open('a') as f:
 wr=csv.writer(f,delimiter='\t',lineterminator='\n')
 for n,items in anchors.items():
  p=OUT/'records'/f'{n:03}.json';r=json.loads(p.read_text());tex=(OUT/'pages'/r['filename']).read_text();ls=tex.splitlines()
  for block,line in items.items():
   b=r['blocks'][block-1];column=ls[line-1].index('on doit avoir')+1 if (n,block)==(14,8) else 1
   b[1]=b[1].split('; tex line')[0]+f'; tex line {line}, column {column} (root mapped after image audit)'
   if n==19 and block in (2,3):b[0]='display'
   wr.writerow([n,block,line,b[2]])
  p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
print('Mapped',sum(map(len,anchors.values())),'text blocks')
