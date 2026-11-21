"""Apply root-reviewed line-map descriptions without moving physical lines."""
from pathlib import Path
from datetime import datetime, timezone
import json,re
B=Path(__file__).resolve().parents[1]
qa=json.loads((B/'reviews/final_line_map_review_b.json').read_text())
jp=B/'reviews/final_line_map_journal.json';assert not jp.exists()
assert len(qa['findings'])==17
reports={x['page']:json.loads((B/'reviews'/f"{x['page']}.json").read_text()) for x in qa['findings']}
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
for x in qa['findings']:
 m=re.fullmatch(r'source_line_map\[(\d+)\](?:\.(text|reading|layout_note))?',x['field']);assert m
 values=reports[x['page']]['source_line_map'];i=int(m[1]);key=m[2]
 before=values[i][key] if key else values[i]
 assert before==x['before'],(x['page'],x['field'])
 assert x['physical_division_preserved'] is True
 if key:values[i][key]=x['after']
 else:values[i]=x['after']
for page,r in reports.items():(B/'reviews'/f'{page}.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
jp.write_text(json.dumps(dict(applied_utc=stamp,source_report='reviews/final_line_map_review_b.json',edits=qa['findings'],scope='Current line-map metadata; all line numbers, physical divisions, page files and frozen audit records preserved.'),ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'utc':stamp,'field_updates':17,'pages':len(reports)}))
