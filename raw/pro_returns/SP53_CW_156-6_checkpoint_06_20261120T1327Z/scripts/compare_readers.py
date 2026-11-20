from pathlib import Path
import json,difflib,sys
ROOT=Path(__file__).resolve().parents[2];n=int(sys.argv[1]);base=ROOT/f'out/readers/scan{n:03}'
texts=[]
for i in range(1,4):
    p=base/f'R{i}';r=json.loads((p/'report.json').read_text());s=(p/'reading.tex').read_text();texts.append(s)
    print(f'\n### READER R{i} FULL READING\n{s}')
    for field in ['differences','c_doubts','s_rows','unresolved','notes','notation_proposals','brief_feedback']:
        print(f'R{i} {field}: '+json.dumps(r.get(field,[]),ensure_ascii=False))
for i in [1,2]:
    print('\n'+''.join(difflib.unified_diff(texts[0].splitlines(True),texts[i].splitlines(True),fromfile='R1',tofile=f'R{i+1}')))
