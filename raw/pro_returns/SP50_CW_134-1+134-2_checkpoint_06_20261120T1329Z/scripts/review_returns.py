"""Compact comparison aid; never decides a reading or substitutes for ink."""
from pathlib import Path
import argparse,json,re,difflib

O=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('key');p.add_argument('--reader',choices=['r1','r2','r3']);p.add_argument('--loci',nargs='*',type=int);p.add_argument('--section',choices=['all','text','index','notes'],default='all');a=p.parse_args()
R={r:O/'readers'/a.key/r for r in ['r1','r2','r3']}
def tokens(s):return re.findall(r'\\[A-Za-z]+|[^\W\d_]+|\d+|[^\w\s]',s)
if a.reader:
    d=json.loads((R[a.reader]/'report.json').read_text())
    if a.section=='notes':
        print(json.dumps({k:d.get(k) for k in ['inventory','notes','checks','abbreviations','slips']},ensure_ascii=False));raise SystemExit
    for n,x in enumerate(d['changes'],1):
        if a.loci and n not in a.loci:continue
        if a.section=='index':print(json.dumps({'n':n,'location':x['location'],'final':x['final'],'C':x['against_c'],'H':x['against_h'],'confidence':x['confidence'],'crop':x.get('crop'),'bbox':x.get('source_bbox')},ensure_ascii=False))
        else:print(json.dumps({'n':n,**x},ensure_ascii=False))
else:
    base=(R['r1']/'reading.tex').read_text();print('R1 FULL READING\n'+base)
    bt=tokens(base)
    for r in ['r2','r3']:
        t=tokens((R[r]/'reading.tex').read_text());print('\nR1 → '+r+' TOKEN DIFFERENCES (spacing ignored)')
        for tag,i,j,k,l in difflib.SequenceMatcher(None,bt,t,autojunk=False).get_opcodes():
            if tag=='equal':continue
            print(json.dumps({'context':' '.join(bt[max(0,i-5):i]),'r1':' '.join(bt[i:j]),r:' '.join(t[k:l]),'following':' '.join(bt[j:j+5])},ensure_ascii=False))
    if a.section=='text':raise SystemExit
    for r,path in R.items():
        d=json.loads((path/'report.json').read_text());print('\n'+r+' LOCUS INDEX')
        for n,x in enumerate(d['changes'],1):
            print(json.dumps({'n':n,'location':x['location'],'final':x['final'],'C':x['against_c'],'H':x['against_h'],'confidence':x['confidence'],'crop':x.get('crop'),'bbox':x.get('source_bbox')},ensure_ascii=False))
        print('INVENTORY',json.dumps(d.get('inventory',[]),ensure_ascii=False))
        print('NOTES',json.dumps(d.get('notes',''),ensure_ascii=False))
        print('CHECKS',json.dumps(d.get('checks',[]),ensure_ascii=False))
