"""Prepare the new34 page-selection source without rendering or building."""
from pathlib import Path
from hashlib import sha256
import json

root=Path(__file__).resolve().parents[1]
source=root/'code/render_checkpoint33_pdf.py'
target=root/'code/render_checkpoint34_pdf.py'
assert not target.exists()
before=source.read_text()
after=before.replace('33','34')
replacements={
 'range(103, 106)':'range(106, 112)',
 'range(161, 165)':'range(165, 167)',
 "headings['A.103']":"headings['A.106']",
 "headings['A.105']":"headings['A.111']",
 "headings['B.161']":"headings['B.165']",
 "headings['B.164']":"headings['B.166']",
 'A103_through_A105':'A106_through_A111',
 'B161_through_B164':'B165_through_B166',
 'A103-A105':'A106-A111',
 'B161-B164':'B165-B166',
}
for a,b in replacements.items():
    assert a in after,a
    after=after.replace(a,b)
# The original 330-pixel contact width is a format constant; restore it.
after=after.replace('width, height = 340, 490','width, height = 330, 490')
compile(after,str(target),'exec')
with target.open('x') as stream: stream.write(after)
record=dict(source=str(source.relative_to(root)),source_sha256=sha256(before.encode()).hexdigest(),
            target=str(target.relative_to(root)),target_sha256=sha256(after.encode()).hexdigest(),
            scope='Only34 identities, exact actual new statement intervals, and current output directory change; no render or visual approval.')
with (root/'records/checkpoint34_render_helper_adaptation.json').open('x') as stream:
    json.dump(record,stream,indent=2);stream.write('\n')
print(json.dumps(record,indent=2))
