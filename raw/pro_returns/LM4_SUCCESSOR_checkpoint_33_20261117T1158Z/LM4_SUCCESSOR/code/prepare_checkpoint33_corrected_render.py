"""Preserve the first render after all assigned individual views have completed."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
root=Path(__file__).resolve().parents[1]
old=root/'records/pdf_qa/checkpoint33_final'
target=root/'records/pdf_qa/checkpoint33_abstract_firstpass/render'
assert old.exists() and not target.exists()
for rel in ['work_A/review_checkpoint33_initial_pages165_169.json','work_CE/checkpoint33_initial_visual_receipt_170_173.json','work_DE/checkpoint33_visual_review_pages529_536.json']:
    assert (root/rel).is_file()
record=dict(recorded_at=datetime.now(timezone.utc).isoformat(),reviewer='/root',
    pdf_sha256='f4eaebbf1ecadb549772cefcade0a2e4aea7f1b9cb0c6c4c44bbf2c88614c002',
    individual_pages=[1,2,4,615,626],contacts=[1,2,3,4,5],
    each_image_opened_separately=True,truncated_outputs_counted=False,
    observations='All40 rendered pages seen on five separately opened contact images; pages1,2,4,615,626 individually viewed. No clipping, overlap or missing glyphs. Last page is an ordinary three-line bibliography-note continuation.',
    image_sha256={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in old.glob('*.png')},
    issues=[],scope='Initial626-page PDF only. Final carry-forward requires exact final PNG equality; changed images must be freshly viewed.')
(root/'records/checkpoint33_initial_root_visual_observations.json').write_text(json.dumps(record,indent=2)+'\n')
old.rename(target)
print('Preserved initial final-render directory after all assigned individual views completed.')
