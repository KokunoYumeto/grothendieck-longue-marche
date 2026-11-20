"""Print the three completed independent returns for human/model adjudication."""
from pathlib import Path
import json,argparse,difflib,re
p=argparse.ArgumentParser();p.add_argument('scan',type=int);p.add_argument('--texts',action='store_true');p.add_argument('--summary',action='store_true');p.add_argument('--diffs',action='store_true');p.add_argument('--compact',action='store_true',help='Compare whitespace-normalized text, printing whole-line comments separately; makes no reading decisions');p.add_argument('--reader',choices=list('ABC'));a=p.parse_args()
ROOT=Path(__file__).resolve().parents[1]
base=ROOT/'readers'/f'scan{a.scan:03}'
readings={}
for r in 'ABC':
    q=base/r
    if not (q/'report.json').exists():print(f'{r}: not complete');continue
    d=json.loads((q/'report.json').read_text());readings[r]=(q/'reading.tex').read_text()
    if a.reader and a.reader!=r:continue
    if a.summary or a.diffs or a.compact:
        print(json.dumps({'reader':r,'start':d.get('start_utc'),'end':d.get('end_utc'),'crops':len(d.get('crops',[])),'changes':len(d.get('changes',[])),'unresolved':len(d.get('unresolved',[])),'inventory':len(d.get('inventory',[]))},ensure_ascii=False))
    else:
        print(json.dumps({'reader':r,'start':d.get('start_utc'),'end':d.get('end_utc'),'crop_count':len(d.get('crops',[])),
           'changes':d.get('changes',[]),'unresolved':d.get('unresolved',[]),'notes':d.get('notes',[]),'math_checks':d.get('math_checks',[])},ensure_ascii=False,indent=2))
if a.texts and 'A' in readings:
    print('=== COMPLETE READER A TEXT ===\n'+readings['A'])
if a.compact:
    for r,text in readings.items():
        comments=[line for line in text.splitlines() if line.lstrip().startswith('%')]
        print(json.dumps({'reader':r,'comments':comments},ensure_ascii=False))
    compared={r:re.sub(r'\s+',' ','\n'.join(line for line in text.splitlines() if not line.lstrip().startswith('%'))).strip() for r,text in readings.items()}
else:
    compared=readings
if (a.texts or a.diffs or a.compact) and 'A' in readings:
    for r in 'BC':
        if r not in readings:continue
        print('=== A versus '+r+' ===')
        matcher=difflib.SequenceMatcher(None,compared['A'],compared[r],autojunk=False)
        for group in matcher.get_grouped_opcodes(55):
            i,j=group[0][1],group[-1][2];k,l=group[0][3],group[-1][4]
            print(json.dumps({'A_context':compared['A'][i:j],r+'_context':compared[r][k:l]},ensure_ascii=False))
