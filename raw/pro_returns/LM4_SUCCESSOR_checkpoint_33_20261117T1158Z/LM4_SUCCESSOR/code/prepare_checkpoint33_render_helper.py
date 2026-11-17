"""Create the checkpoint33 renderer by explicit reviewed source-only substitutions."""
from pathlib import Path
import ast, difflib, hashlib, json
from datetime import datetime, timezone

root=Path(__file__).resolve().parents[1]
source=root/'code/render_checkpoint32_pdf.py'
target=root/'code/render_checkpoint33_pdf.py'
assert not target.exists()
before=source.read_text()
after=before.replace('32','33')
replacements={
 'range(95, 103)':'range(103, 106)',
 'range(155, 161)':'range(161, 165)',
 "headings['A.95']":"headings['A.103']",
 "headings['A.102']":"headings['A.105']",
 "headings['B.155']":"headings['B.161']",
 "headings['B.160']":"headings['B.164']",
 'A95_through_A102':'A103_through_A105',
 'B155_through_B160':'B161_through_B164',
 'A95-A102':'A103-A105',
 'B155-B160':'B161-B164',
 'Recovery33 source.':'Checkpoint33 source.',
}
for a,b in replacements.items():
    assert a in after,a
    after=after.replace(a,b)
ast.parse(after)
target.write_text(after)
(root/'records/checkpoint33_render_helper_source.diff').write_text(''.join(difflib.unified_diff(
    before.splitlines(True),after.splitlines(True),fromfile=str(source.relative_to(root)),tofile=str(target.relative_to(root)))))
(root/'records/checkpoint33_render_helper_source.json').write_text(json.dumps(dict(
    created_at=datetime.now(timezone.utc).isoformat(),source=str(source.relative_to(root)),
    source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),target=str(target.relative_to(root)),
    target_sha256=hashlib.sha256(target.read_bytes()).hexdigest(),
    scope='Source creation only; no PDF build, rendering, or visual approval.'),indent=2)+'\n')
print(target.relative_to(root))
