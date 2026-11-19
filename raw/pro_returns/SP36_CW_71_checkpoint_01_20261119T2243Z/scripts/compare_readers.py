from pathlib import Path
import sys,json,difflib
ROOT=Path(__file__).resolve().parents[2];scan=int(sys.argv[1]);OUT=ROOT/'out'
c=(ROOT/'packets'/f'scan{scan:03d}'/'C.tex').read_text()
sections=[f'# Reader comparison scan {scan:03d}\n']
for r in ['R1','R2','R3']:
    p=OUT/'readers'/f'scan{scan:03d}'/r
    report=json.loads((p/'report.json').read_text())
    t=(p/'reading.tex').read_text()
    sections.append(f'## {r}\n')
    sections.append('```diff\n'+''.join(difflib.unified_diff(c.splitlines(True),t.splitlines(True),fromfile='C',tofile=r))+'```\n')
    for f in report.get('findings',[]):sections.append(json.dumps(f,ensure_ascii=False)+'\n')
    sections.append('NOTES '+json.dumps(report.get('notes',[]),ensure_ascii=False)+'\n')
    sections.append('BRIEF FEEDBACK '+json.dumps(report.get('brief_feedback',[]),ensure_ascii=False)+'\n')
text='\n'.join(sections)
dest=OUT/'adjudication'/f'scan{scan:03d}_comparison.md';dest.write_text(text)
print(text)
