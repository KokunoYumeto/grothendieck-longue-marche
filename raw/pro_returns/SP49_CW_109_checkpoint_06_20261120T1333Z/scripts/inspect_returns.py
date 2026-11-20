from pathlib import Path
import json,sys,difflib
W=Path(__file__).resolve().parents[1]
n=int(sys.argv[1]);root=W/'readers'/f'{n:03}'
for r in 'ABC':
    d=root/r
    if not (d/'report.json').exists():
        print(r,'NOT READY');continue
    report=json.loads((d/'report.json').read_text())
    print('\nREADER',r,'LAYOUT:',report.get('layout',''))
    print('CHANGES',json.dumps(report.get('changes',[]),ensure_ascii=False,indent=2))
    print('C DOUBTS',json.dumps(report.get('c_doubts',[]),ensure_ascii=False,indent=2))
    print('NOTES',json.dumps(report.get('notes',[]),ensure_ascii=False))
    print('MATH',json.dumps(report.get('math_checks',[]),ensure_ascii=False))
    print('FEEDBACK',report.get('brief_feedback',''))
    print('DIFF FROM C:')
    print(''.join(difflib.unified_diff((W/'inputs'/f'{n:03}'/'C.tex').read_text().splitlines(True),(d/'reading.tex').read_text().splitlines(True))))
