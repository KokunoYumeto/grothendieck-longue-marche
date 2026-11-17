"""Record root's completed final-PDF inspections and actual diagnostic audit."""
from datetime import datetime,timezone
from pathlib import Path
import hashlib
import json
import re
import shutil

root=Path(__file__).resolve().parents[1]
out=root/'records/pdf_qa/checkpoint26_final'
m=json.loads((root/'records/checkpoint26_metrics.json').read_text())
render=json.loads((out/'render_manifest.json').read_text())
digest=hashlib.sha256((root/'LM4_SUCCESSOR_paper.pdf').read_bytes()).hexdigest()
assert digest==m['pdf_sha256'] and m['pages']==493
required=list(range(385,405))
individual=[1,2,3,*required,493]
assert set(individual)<=set(render['rendered_pages'])
logs=['LM4_SUCCESSOR_paper.log',
      'records/build_passes/20261117T021757275652Z/build_stabilize_0.log']
audits=[]
for relative in logs:
    path=root/relative
    lines=path.read_text().splitlines()
    warnings=[line for line in lines if re.search(r'\bwarning\b',line,re.I)
              and not line.startswith(('Package:','File:'))]
    issues=[line for line in lines if re.search(r'^!|\berror\b|undefined|Overfull',line,re.I)
            and not line.startswith(('Package:','File:'))]
    assert not warnings and not issues,(relative,warnings,issues)
    audits.append({'path':relative,'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
                   'warnings':warnings,'issues':issues})
for suffix in ('aux','bbl','blg'):
    source=root/f'LM4_SUCCESSOR_paper.{suffix}'
    if source.exists(): shutil.copy2(source,out/f'{source.name}.retained.txt')
now=datetime.now(timezone.utc).isoformat()
record={
 'recorded_at':now,'pdf_sha256':digest,
 'rendered_pages':render['rendered_pages'],'required_math_pages':required,
 'individually_inspected_pages':individual,'contact_sheets_inspected':4,
 'each_contact_sheet_opened_separately':True,'truncated_outputs_counted':False,
 'combined_build_attempts':1,'combined_overfull_before':0,'combined_overfull_after':0,
 'maximum_overflow_before_pt':0,'maximum_overflow_after_pt':0,
 'printed_bibliography_entries':112,'final_log_and_stdout_audits':audits,
 'final_log_and_stdout_case_insensitive':'PASS','visual_review':'PASS',
}
(root/'records/checkpoint26_visual_review.json').write_text(json.dumps(record,indent=2)+'\n')
text=f'''# Twenty-sixth-hour final typesetting and visible verification

Final PDF SHA-256: {digest}.
Final size: {m['pdf_bytes']} bytes;493 pages.
Register:299 statements;255 Proved,19 Refuted,19 Open,6 Known.
Bibliography:112 entries in both source database and printed bbl.
Task/lead rows:49. Visual review: PASS.

The first combined checkpoint26 build is final. Its final TeX log and
actual stabilized engine stdout were both checked case-insensitively:
zero warnings,overfull boxes,undefined references or errors. Package
and file metadata descriptions are excluded from diagnostic matching.
Initial/final combined overfull counts are0/0; maximum overflow is0pt.
No visual repair or second combined build was required. The previous
PDF,source,log,printed bibliography,register,task table and report were
preserved before integration. The clean derived font map is unchanged.

Root opened each of the four contact sheets separately. They cover
all{len(render['rendered_pages'])} rendered pages: the title and updated
abstract,contents,unchanged representative pages across the Parts,
the complete new mathematical block and its two boundary pages,
and the first and last bibliography pages. The bibliography entries
are unchanged; all112 printed entries were counted independently.

Root then opened{len(individual)} pages individually:1,2,3,every page
385--404 containing B124--B130,and493. No truncated output or prior
private inspection substitutes for these actual final-PDF views.
Margins,displays,equation numbers,tables,proof endings,code paths,
glyphs and bibliography wrapping were inspected. No clipping,overlap,
missing glyph or other layout defect was found.

All seven source reviews and the authors' private all-page QA remain
separately bound to frozen source hashes. Initial syntax/layout files
and their genuine outputs are retained. The authored B128 initial
comma PDF has an explicit retention rule and is not discarded.

Rendered pages: {render['rendered_pages']}
Individually inspected pages: {individual}
Contact sheets inspected:4,each opened separately.
Combined driver:records/checkpoint26_build1_driver.log.
Genuine passes:records/build_passes/20261117T021757275652Z/.
Final metrics:records/checkpoint26_metrics.json.
Final renders:records/pdf_qa/checkpoint26_final/.
Recorded at:{now}.
'''
(root/'records/checkpoint26_typesetting.txt').write_text(text)
print('PASS:20 new mathematical pages,24 individual views,4 separate contact sheets;final log and stdout clean.')
