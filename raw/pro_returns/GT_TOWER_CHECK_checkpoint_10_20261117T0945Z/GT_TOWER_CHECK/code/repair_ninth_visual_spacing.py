#!/usr/bin/env python3
"""Preserve and repair the observed SVM.6 and bibliography spacing."""
from pathlib import Path
import shutil,re,json,hashlib
ROOT=Path(__file__).resolve().parents[1]
WORK=ROOT.parent/'work'
BACK=ROOT/'notes/ninth_visual_before_repair'
BACK.mkdir(exist_ok=True)
for source in [WORK/'main_fivepoint_signed_source_module.tex',WORK/'ghost_references.bib',
               ROOT/'GT_TOWER_CHECK_paper.pdf',ROOT/'notes/pdf_qa/manifest.json',
               ROOT/'notes/pdf_qa/checkpoint09_assignments.json']:
    dest=BACK/source.name
    assert not dest.exists(),str(dest)
    shutil.copy2(source,dest)
for page in [171,369,370,371,372]:
    source=ROOT/f'notes/pdf_qa/page_{page:03d}.png'
    shutil.copy2(source,BACK/source.name)
for source in (ROOT/'notes/pdf_qa').glob('checkpoint09_*.json'):
    if source.name!='checkpoint09_assignments.json':shutil.copy2(source,BACK/source.name)
source=WORK/'main_fivepoint_signed_source_module.tex'
value=source.read_text()
old=r''' \operatorname{rank}(\text{first map})&=96,\qquad
 \operatorname{rank}(\text{second map})=96,\qquad'''
new=old.replace(r'\qquad',r'\quad')
assert value.count(old)==1
source.write_text(value.replace(old,new))
source=WORK/'ghost_references.bib'
value=source.read_text()
value,n=re.subn(r'\b(pages?|Sections?|Propositions?|Theorems?|Definitions?|orders?|equations?)(?=[0-9(])',r'\1 ',value)
source.write_text(value)
(BACK/'repair_record.json').write_text(json.dumps({
    'observed':'SVM.6 last rank value was crowded under the equation tag; bibliography notes lacked spaces before several exact source locations.',
    'repair':'Both SVM.6 inter-column spacings changed from qquad to quad, preserving the two-line height. Exact bibliography content retained with ordinary word/number spacing.',
    'bibliography_spacing_replacements':n,
    'previous_pdf_sha256':hashlib.sha256((BACK/'GT_TOWER_CHECK_paper.pdf').read_bytes()).hexdigest()},indent=2)+'\n')
print('Repaired the observed display and',n,'bibliography spacing instances; exact previous files retained.')
