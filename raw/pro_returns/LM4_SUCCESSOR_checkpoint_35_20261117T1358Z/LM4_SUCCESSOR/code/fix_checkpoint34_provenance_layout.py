"""Preserve the entire first34 build and repair one provenance-only overflow."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import difflib
import json
import shutil
import fitz

root=Path(__file__).resolve().parents[1]
backup=root/'records/pdf_qa/checkpoint34_first_layout'
assert not backup.exists()
paths=['LM4_SUCCESSOR_paper.'+e for e in ('pdf','tex','log','aux','bbl','blg','toc','out')]
paths+=['LM4_SUCCESSOR_results.csv','LM4_SUCCESSOR_references.bib',
        'records/checkpoint34_root_formal_reviews.json',
        'records/checkpoint34_formal_source_copies.json',
        'records/checkpoint34_independent_review_manifest.json',
        'records/checkpoint34_build_driver.out','records/checkpoint34_build_driver.err',
        'work_DE/A109_derived_cyclic_cohomology_proposed.tex',
        'sections/a_derived_cyclic_cohomology.tex']
paths+=[str(p.relative_to(root)) for p in (root/'records').glob('build_*.log')]
saved=[]
for rel in paths:
    p=root/rel
    if p.is_file():
        suffix='.retained.txt' if p.suffix in {'.aux','.bbl','.blg','.toc'} else ''
        out=backup/(rel+suffix);out.parent.mkdir(parents=True,exist_ok=True)
        shutil.copy2(p,out)
        saved.append({'path':rel,'preserved':str(out.relative_to(root)),
                      'sha256':sha256(p.read_bytes()).hexdigest()})
pdf=root/'LM4_SUCCESSOR_paper.pdf'
doc=fitz.open(pdf)
page=183
doc[page-1].get_pixmap(matrix=fitz.Matrix(2,2),alpha=False).save(backup/'page-183-overflow.png')
doc.close()
source=root/'work_DE/A109_derived_cyclic_cohomology_proposed.tex'
target=root/'sections/a_derived_cyclic_cohomology.tex'
before=source.read_text();assert target.read_text()==before
anchor='The complete predecessor proofs and original-source audit are retained\n'
assert before.count(anchor)==1
after=before.replace(anchor,'\\begingroup\\footnotesize\\raggedright\n'+anchor)
after=after.rstrip()+'\n\\par\\endgroup\n'
source.write_text(after);target.write_text(after)
diff=''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),
                               fromfile='A109_before_layout',tofile='A109_after_layout'))
(root/'records/checkpoint34_A109_layout.diff').write_text(diff)
record=dict(recorded_at=datetime.now(timezone.utc).isoformat(),
            actual_first_build_session=46912,actual_first_build_exit=1,
            actual_exit_observation_chunk='b1f7ed',first_build_directory='records/build_passes/20261117T121816148327Z',
            first_pdf_sha256=sha256(pdf.read_bytes()).hexdigest(),first_pdf_pages=646,
            first_overfull_count=1,first_overfull_pt=17.66902,first_overfull_page=183,
            source=str(source.relative_to(root)),target=str(target.relative_to(root)),
            before_sha256=sha256(before.encode()).hexdigest(),after_sha256=sha256(after.encode()).hexdigest(),
            layout_only=True,scope='Wrap only the final provenance paragraph in footnotesize raggedright. No theorem, proof, formula, citation, or path is removed or changed.',
            preserved=saved)
(root/'records/checkpoint34_layout_correction.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({k:v for k,v in record.items() if k!='preserved'},indent=2))
