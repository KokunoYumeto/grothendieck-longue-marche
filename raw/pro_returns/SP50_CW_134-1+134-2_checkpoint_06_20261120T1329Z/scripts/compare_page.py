"""Compact complete reader-return comparison for main visual adjudication."""
from pathlib import Path
import json,difflib,argparse
p=argparse.ArgumentParser();p.add_argument('key');a=p.parse_args()
O=Path(__file__).resolve().parents[1];b=O/'readers'/a.key
reports={};texts={}
for r in ['r1','r2','r3']:
    f=b/r/'report.json'
    if not f.exists():print(r,'PENDING');continue
    reports[r]=json.loads(f.read_text());texts[r]=(b/r/'reading.tex').read_text()
if 'r1' in texts:print('\nFULL R1\n'+texts['r1'])
for r in ['r2','r3']:
    if r in texts and 'r1' in texts:
        print('\nTEXT DIFFERENCES R1 TO '+r+'\n'+''.join(difflib.unified_diff(texts['r1'].splitlines(True),texts[r].splitlines(True))))
for r,d in reports.items():
    print('\n'+r+' ALL LOCI')
    for i,x in enumerate(d.get('changes',[]),1):
        print(json.dumps({'n':i,'id':x.get('id'),'loc':x.get('location'),'C':x.get('c'),'H':x.get('h'),'final':x.get('final'),'Cdiff':x.get('against_c'),'Hdiff':x.get('against_h'),'confidence':x.get('confidence'),'crop':x.get('crop'),'bbox':x.get('source_bbox',x.get('bbox_source_px',x.get('bbox')))},ensure_ascii=False))
    print('INVENTORY',json.dumps([{k:x.get(k) for k in ['element','kind','position','first_words_or_objects']} for x in d.get('inventory',[])],ensure_ascii=False))
    print('NOTES',json.dumps(d.get('notes'),ensure_ascii=False))
    print('CHECKS',json.dumps(d.get('checks'),ensure_ascii=False))
