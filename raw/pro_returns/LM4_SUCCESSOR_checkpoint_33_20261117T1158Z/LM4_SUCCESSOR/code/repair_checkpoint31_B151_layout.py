"""Preserve the genuine failed combined build and repair two B151 line breaks."""
from pathlib import Path
from datetime import datetime, timezone
import difflib
import hashlib
import json
import shutil

root = Path(__file__).resolve().parents[1]
source = 'work_DE/B151_one_sided_family_extension_proposed.tex'
target = 'sections/b_one_sided_family_extension.tex'
backup = root / 'records/pdf_qa/checkpoint31_before_B151_layout'
assert not backup.exists()
backup.mkdir(parents=True)
paths = [source, target, 'LM4_SUCCESSOR_paper.pdf', 'LM4_SUCCESSOR_paper.log',
         'records/checkpoint31_build_driver.out', 'records/checkpoint31_build_driver.err',
         'records/checkpoint31_root_formal_reviews.json',
         'records/checkpoint31_formal_source_copies.json']
for rel in paths:
    dest = backup / rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(root / rel, dest)
for suffix in ('aux', 'bbl', 'blg'):
    shutil.copy2(root / f'LM4_SUCCESSOR_paper.{suffix}',
                 backup / f'LM4_SUCCESSOR_paper_{suffix}.retained.txt')
old = (root / source).read_text()
assert (root / target).read_text() == old
assert hashlib.sha256(old.encode()).hexdigest() == '3977034db5a4bf8ad203033fd9826d040504f96b76097631ca340152aaeb1644'
before = '\\emph{B.151.4. The exact opposite-family projection.}\nThe left color deletion'
after = '\\emph{B.151.4. The exact opposite-family projection.}\\par\n\\noindent The left color deletion'
assert old.count(before) == 1
new = old.replace(before, after)
before = ('The full precursor proof is\n'
          '\\path{work_DE/next_marginal_source/one_sided_family_centralizer_extension30.md},\n'
          'independently reviewed in full by A, CE and root. The present\n')
after = ('The full precursor proof is the file\n'
         '\\begin{quote}\\small\n'
         '\\path{work_DE/next_marginal_source/}\\\\\n'
         '\\path{one_sided_family_centralizer_extension30.md}.\n'
         '\\end{quote}\n'
         'It was independently reviewed in full by A, CE and root. The present\n')
assert new.count(before) == 1
new = new.replace(before, after)
for rel in (source, target):
    (root / rel).write_text(new)
diff = ''.join(difflib.unified_diff(old.splitlines(True), new.splitlines(True),
                                 fromfile=source + ':before', tofile=source + ':after'))
(root / 'records/checkpoint31_B151_layout_repair.diff').write_text(diff)
record = {'recorded_at': datetime.now(timezone.utc).isoformat(),
          'source': source, 'target': target,
          'before_sha256': hashlib.sha256(old.encode()).hexdigest(),
          'after_sha256': hashlib.sha256(new.encode()).hexdigest(),
          'actual_initial_overfull_pt': [23.66608, 9.81163],
          'failed_build_retained': str(backup.relative_to(root)),
          'scope': 'One paragraph break and a two-line provenance path; no mathematical assertion or expression changed.',
          'new_build_and_visual_review': 'PENDING',
          'independent_final_source_review': 'PENDING'}
(root / 'records/checkpoint31_B151_layout_repair.json').write_text(json.dumps(record, indent=2)+'\n')
print(json.dumps(record, indent=2))
print(diff)
