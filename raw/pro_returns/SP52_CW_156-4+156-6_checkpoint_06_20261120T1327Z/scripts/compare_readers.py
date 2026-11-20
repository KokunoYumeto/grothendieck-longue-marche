"""Compare text returns only; makes no image recognition or reading decisions."""
from pathlib import Path
import json,difflib,sys
O=Path(__file__).resolve().parents[1];key=sys.argv[1];B=O/'readers'/key
texts={};reports={};lines=['# Reader comparison '+key,'']
for i in range(1,4):
 name=f'R{i}';texts[name]=(B/name/'reading.tex').read_text();reports[name]=json.loads((B/name/'report.json').read_text())
 lines+=[f'## {name} full reading','',texts[name],f'## {name} difference index','']
 for x in reports[name]['differences']:
  lines.append(json.dumps({f:x.get(f) for f in ['id','location','c','h','reading','confidence','crop','bbox','bbox_image','math_consequential']},ensure_ascii=False))
 lines+=['',f'## {name} notes and feedback',json.dumps({f:reports[name].get(f) for f in ['notes','check_events','workflow_feedback']},ensure_ascii=False,indent=2),'']
for x in ['R2','R3']:
 lines+=['## Text difference R1 / '+x,'']+list(difflib.unified_diff(texts['R1'].splitlines(),texts[x].splitlines(),fromfile='R1',tofile=x,lineterm=''))+['']
(O/'decisions'/(key+'_reader_comparison.txt')).write_text('\n'.join(lines))
print(json.dumps({'page':key,'readers':{k:{'differences':len(v['differences']),'c_doubts':len(v['c_doubts']),'crops':len(v['crops']),'remaining_doubts':len(v['remaining_doubts']),'inventory':len(v['inventory'])} for k,v in reports.items()},'comparison_file':str(O/'decisions'/(key+'_reader_comparison.txt'))},ensure_ascii=False))
