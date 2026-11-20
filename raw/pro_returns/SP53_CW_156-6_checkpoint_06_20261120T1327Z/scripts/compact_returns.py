"""Print every return compactly; makes no decisions or witness normalization."""
from pathlib import Path
import json,sys
O=Path(__file__).resolve().parents[1];n=int(sys.argv[1])
for i in range(1,4):
    p=O/f'readers/scan{n:03}/R{i}';r=json.loads((p/'report.json').read_text())
    print(f'=== R{i} READING ===\n'+(p/'reading.tex').read_text())
    print(f'=== R{i} DIFFERENCES ===')
    for d in r['differences']:
        print(json.dumps({k:d.get(k) for k in ['id','place','c','h','reading','evidence','crop','crop_box','crop_source']},ensure_ascii=False))
    print('C_DOUBTS '+json.dumps([{k:d.get(k) for k in ['place','c','reading','disposition']} for d in r['c_doubts']],ensure_ascii=False))
    for field in ['s_rows','unresolved','notes','brief_feedback']:
        print(field.upper()+' '+json.dumps(r.get(field),ensure_ascii=False))
    print('INVENTORY '+json.dumps(r.get('inventory'),ensure_ascii=False))
