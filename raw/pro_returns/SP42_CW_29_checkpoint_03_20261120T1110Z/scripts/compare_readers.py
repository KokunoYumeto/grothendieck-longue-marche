from pathlib import Path
import sys,json,difflib
OUT=Path(__file__).resolve().parents[1];s=int(sys.argv[1]);base=OUT/'readers'/f'scan{s:03d}'
readings={}
for name in ['R1','R2','R3']:
 p=base/name;readings[name]=(p/'reading.tex').read_text()
 d=json.loads((p/'report.json').read_text())
 print('\nREADER',name,'REPORT')
 for k in ['differences','c_doubts','s_rows','remaining_doubts','notes','check_events','brief_feedback']:
  print(k,json.dumps(d.get(k,[]),ensure_ascii=False))
for name in ['R2','R3']:
 print('\nREADING DIFF R1 versus',name)
 print(''.join(difflib.unified_diff(readings['R1'].splitlines(True),readings[name].splitlines(True),fromfile='R1',tofile=name)))
