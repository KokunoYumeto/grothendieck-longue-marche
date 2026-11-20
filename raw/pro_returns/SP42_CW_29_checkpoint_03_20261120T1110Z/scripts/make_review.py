"""Create an editable review worksheet from independent returns, never a final decision."""
from pathlib import Path
import json,sys,difflib
OUT=Path(__file__).resolve().parents[1];ROOT=OUT.parent;s=int(sys.argv[1])
pkt=ROOT/'staging'/f'scan{s:03d}';info=json.loads((pkt/'page.json').read_text())
reports={r:json.loads((OUT/'readers'/f'scan{s:03d}'/r/'report.json').read_text()) for r in ['R1','R2','R3']}
review=OUT/'reviews'/f'scan{s:03d}';review.mkdir(parents=True,exist_ok=True)
rows=[]
for reader,d in reports.items():
 for kind in ['differences','c_doubts','s_rows']:
  for i,r in enumerate(d.get(kind,[]),1):rows.append(dict(source_reader=reader,source_kind=kind,source_index=i,**r))
(review/'all_loci.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
with (review/'review.txt').open('w') as f:
 for r in rows:
  f.write(f"{r['source_reader']}/{r['source_kind']}/{r['source_index']} {r.get('place',r.get('where',''))}\n")
  for k in ['c','h','reading','against_c','against_h','evidence','bbox','crop','resolved','math_note']:
   if k in r:f.write(k+': '+str(r[k])+'\n')
  f.write('\n')
 c=(pkt/'C.tex').read_text()
 for r in reports:
  text=(OUT/'readers'/f'scan{s:03d}'/r/'reading.tex').read_text()
  f.write(''.join(difflib.unified_diff(c.splitlines(True),text.splitlines(True),fromfile='C',tofile=r)))
print(str(review/'review.txt'))
