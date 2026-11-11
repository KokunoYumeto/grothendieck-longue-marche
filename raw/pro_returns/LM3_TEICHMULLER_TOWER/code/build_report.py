#!/usr/bin/env python3
from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]
header=(root/'audit/report_header.md').read_text()
validation=root/'audit/build_validation.json'
if validation.exists():
    b=json.loads(validation.read_text())
    status=b.get('status','UNRECORDED')
    build=(f"**Build status: {status}.** "+b.get('description','')+"\n\n"
           f"PDF pages: {b.get('pages','unrecorded')}. "
           f"All computation programs passed: {b.get('computations_passed','unrecorded')}. "
           f"Missing citation keys: {b.get('missing_citation_keys','unrecorded')}. "
           f"Undefined references: {b.get('undefined_references','unrecorded')}. "
           f"Overfull boxes: {b.get('overfull_boxes','unrecorded')}.\n\n"
           +b.get('visual_qa',''))
else:
    build="Build validation is pending; this intermediate report is not the final deliverable."
header=header.replace('BUILD_RECORD',build)
parts=[header]
for prefix in ('AF','BC','D','E'):
    text=(root/'audit'/f'{prefix}_report.md').read_text()
    # Keep each audit internally intact and recognizable.
    parts.append(text)
    parts.append('\n\n---\n\n')
(root/'LM3_TEICHMULLER_TOWER_report.md').write_text('\n\n'.join(parts))
print('Wrote consolidated report.')

