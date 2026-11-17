"""Record completed visible inspection, without pretending the script performs it."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib,json,re

root=Path(__file__).resolve().parents[1]
m=json.loads((root/'records/checkpoint21_metrics.json').read_text())
assert hashlib.sha256((root/'LM4_SUCCESSOR_paper.pdf').read_bytes()).hexdigest()==m['pdf_sha256']
assert m['statements']==276 and m['pages']==408
assert m['statuses']=={'Known':6,'Proved':232,'Refuted':19,'Open':19}
assert not m['overfull'] and not m['warnings'] and not m['errors']
qa=root/'records/pdf_qa/checkpoint21_final'
manifest=json.loads((qa/'render_manifest.json').read_text())
pages=manifest['rendered_pages'];assert len(pages)==35
enlarged=[1,2,316,317,318,319,320,408]
assert set(enlarged)<=set(pages)
comparison=json.loads((qa/'unchanged_rendering_comparison.json').read_text())
assert comparison['different']==['contact-03.png','page-320.png']
assert comparison['identical_count']==37
bib=re.split(r'(?m)(?=^@)',(root/'LM4_SUCCESSOR_references.bib').read_text())[1:]
assert len(bib)==108 and all(re.search(r'\b(?:verified|unverified)\b',e,re.I) for e in bib)
now=datetime.now(timezone.utc).isoformat()
record=f'''# Twenty-first-hour final PDF typesetting and visual verification

Final PDF SHA-256:{m['pdf_sha256']}.
Final size:{m['pdf_bytes']} bytes;{m['pages']} pages.
Register:{m['statements']} statements;{m['statuses']}.
Bibliography:{m['bibliography_entries']} verified-status entries;49 task rows.
Visual review: PASS.

Build1 and build2 both compiled the complete276-statement paper cleanly
in408 pages. Both final logs have zero overfull boxes, warnings, undefined
references and errors. Before/after overfull counts are0/0, including
boxes beyond2pt; maximum0pt. The only visual repair changed the newly
added textual Herfort--Ribes citation, initially joined to the preceding
period, into a spaced parenthetical citation before that period.
It changed no mathematical content. The complete earlier PDF, metrics,
all35 page renderings and four contact sheets remain retained in
records/pdf_qa/checkpoint21_before_citation/.

We displayed and inspected every one of the four contact sheets for
the35 sampled pages, covering every Part, the complete new B106--B107
proofs, earlier dense formulas and tables, and the bibliography. All
four final contact sheets are covered: sheets1,2,4 are byte-identical
to the inspected pre-repair sheets, and the changed final sheet3 was
displayed again. We displayed eight critical pages individually.
Pages316--319 are byte-identical to their inspected pre-repair images;
the repaired320 and pages1,2,408 were displayed from final renderings.
The unchanged-rendering record checks every image individually, and
only page320 and its contact sheet differ. The repaired citation is
properly spaced. All equations, tags, statement openings, proof endings,
abstract, contents and bibliography entries fit without overlap,
clipping or missing glyphs. No additional layout repair was required.

Rendered pages:{pages}
Individually inspected pages:{enlarged}
Inherited full-page views by byte identity:[316,317,318,319].
Inherited contact sheets by byte identity:[1,2,4].

Genuine build drivers:records/checkpoint21_build1_driver.log and
records/checkpoint21_build2_driver.log; complete pass logs under
records/build_passes/. Final metrics:records/checkpoint21_metrics.json,
checkpoint21_final_metrics.out/.err. Final render output:
records/checkpoint21_render_final.out/.err. Mathematical full-proof
reviews are recorded separately; visual inspection does not replace them.

Recorded at{now}.
'''
(root/'records/checkpoint21_typesetting.txt').write_text(record)
(root/'records/checkpoint21_visual_review.json').write_text(json.dumps({
 'pdf_sha256':m['pdf_sha256'],'rendered_pages':pages,
 'contact_sheets_inspected':4,'individually_inspected_pages':enlarged,
 'inherited_individual_views_with_identical_final_png':[316,317,318,319],
 'inherited_contact_sheets_with_identical_final_png':[1,2,4],
 'combined_overfull_before':0,'combined_overfull_after':0,
 'cosmetic_repair':'Spaced parenthetical Herfort--Ribes citation on page320.',
 'visual_review':'PASS','recorded_at':now},indent=2)+'\n')
p=root/'LM4_SUCCESSOR_report.md';s=p.read_text()
marker='### Twenty-first-hour final typesetting verification'
assert marker not in s
s+=f'''\n{marker}

The final276-statement paper has408 pages and{m['pdf_bytes']} bytes,
SHA-256{m['pdf_sha256']}. Both complete builds have zero overfull
boxes, warnings, undefined references and errors; before/after counts
are0/0, including beyond2pt. A single cosmetic repair changed the new
Herfort--Ribes citation to a properly spaced parenthetical citation.
The earlier PDF and every rendering remain retained. All108 bibliography
entries have explicit verification status.

We inspected four contact sheets for35 pages distributed across every
Part and the bibliography, and eight critical pages individually,
including the full new proofs. Four individual views and three contact
sheets transfer to the final version by verified byte-identical PNGs;
the repaired page320 and its contact sheet were displayed anew. The
final title/abstract, contents and last bibliography page were also
displayed individually. No clipping, overlap, missing glyphs or defective
layout was found. Exact lists and genuine build history are in
records/checkpoint21_typesetting.txt. Both main full decisions remain Open.
'''
p.write_text(s)
print('Final PDF QA recorded:35 pages,4 contact sheets,8 full-size pages; PASS.')
