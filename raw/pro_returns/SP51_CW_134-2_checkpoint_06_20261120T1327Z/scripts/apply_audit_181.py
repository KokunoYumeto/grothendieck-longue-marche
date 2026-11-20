"""Apply text-only record clarifications; no transcription or image changes."""
from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]
p=root/'records/scan181/decision.json'
d=json.loads(p.read_text())
for i in [0,6,17]:
 d['differences'][i]['bbox_role']='Saved crop rectangle; the earlier reader feature rectangle is preserved in reader_report_bbox.'
d['differences'][6]['place']='L11, uncertain abbreviation stop after loc'
d['doubt_review'][11]['evidence']=d['doubt_review'][11]['evidence'].replace('incarnerait is separately supported by crop 03','incarnerait is separately supported by crops/scan181/A/L10_incarnerait.png')
d['differences'][17]['evidence']=d['differences'][17]['evidence'].replace('Both nouns are plural','The article and noun are plural')
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
audit=root/'records/technical_audit_181.md'
note='\n## Main-reader disposition\n\nAll four proposed metadata/citation clarifications were accepted. Saved crop rectangles, image decisions, final page text, counts and doubts are unchanged. Applied by scripts/apply_audit_181.py; no images were reopened.\n'
if '## Main-reader disposition' not in audit.read_text():
 with audit.open('a') as f:f.write(note)
print('Applied four scan181 record clarifications; final TeX unchanged.')
