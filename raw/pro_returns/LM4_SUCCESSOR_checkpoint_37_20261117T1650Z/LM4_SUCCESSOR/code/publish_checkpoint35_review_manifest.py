"""Bind the complete final proof reviews actually read by root."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import json
from integrate_checkpoint35_proofs import SPECS

root=Path(__file__).resolve().parents[1]
pairs=[('work_A/review_A112_A113_A117_A119_formal35','md'),
       ('work_CE/review_A114_A115_A116_A118_formal35','txt'),
       ('work_CE/review_A114_final_citation_diff35','txt'),
       ('work_DE/review_B167_B168_formal35','md')]
paths=[base+'.'+ext for base,kind in pairs for ext in (kind,'json')]
reviews={p:sha256((root/p).read_bytes()).hexdigest() for p in paths}
sources={p:h for _,p,_,h in SPECS}
all_text='\n'.join((root/p).read_text() for p in paths)
for p,h in sources.items():
    assert sha256((root/p).read_bytes()).hexdigest()==h
    assert h in all_text
out=dict(status='PASS_FINAL_SOURCES',recorded_at=datetime.now(timezone.utc).isoformat(),
    root_read_all_complete_reviews=True,source_hashes=sources,reviews=reviews,
    scope='Root read all ten entire mathematical sources, every final difference and every listed complete independent review and JSON. The complete actual B168 finite checker/output/certificate were read; its original execution was observed by CE, with no root rerun claimed. This manifest is not PDF visual approval.')
with (root/'records/checkpoint35_independent_review_manifest.json').open('x') as stream:
    json.dump(out,stream,indent=2);stream.write('\n')
print('Bound10 final sources and8 complete independent review records.')
