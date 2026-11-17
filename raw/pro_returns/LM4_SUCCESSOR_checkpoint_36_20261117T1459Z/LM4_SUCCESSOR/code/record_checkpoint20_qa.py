"""Record completed visible inspection; this script does not perform it."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import re

root = Path(__file__).resolve().parents[1]
m = json.loads((root/'records/checkpoint20_metrics.json').read_text())
assert hashlib.sha256((root/'LM4_SUCCESSOR_paper.pdf').read_bytes()).hexdigest() == m['pdf_sha256']
assert m['statements'] == 274 and m['pages'] == 404
assert m['statuses'] == {'Known':6, 'Proved':230, 'Refuted':19, 'Open':19}
assert not m['overfull'] and not m['warnings'] and not m['errors']
manifest = json.loads((root/'records/pdf_qa/checkpoint20_final/render_manifest.json').read_text())
pages = manifest['rendered_pages']
assert len(pages) == 53 and manifest['page_count'] == 404
enlarged = [1, 2, *range(298, 317), 400, 404]
assert len(enlarged) == 23 and set(enlarged) <= set(pages)
bib = re.split(r'(?m)(?=^@)', (root/'LM4_SUCCESSOR_references.bib').read_text())[1:]
assert len(bib) == 108 and all(re.search(r'\b(?:unverified|verified)\b', e, re.I) for e in bib)
comparison = json.loads((root/'records/pdf_qa/checkpoint20_final/unchanged_rendering_comparison.json').read_text())
now = datetime.now(timezone.utc).isoformat()
record = f'''# Twentieth-hour final PDF typesetting and visual verification

Final PDF SHA-256: {m['pdf_sha256']}.
Final size: {m['pdf_bytes']} bytes; {m['pages']} pages.
Register: {m['statements']} statements; {m['statuses']}.
Bibliography records: {m['bibliography_entries']}; task rows: {m['task_rows']}.
Visual review: PASS.

The first combined build attempt failed before PDF production because the
plain LuaLaTeX format was unavailable. Build2 used the recorded recovered
TeX environment and compiled B101--B104 in 402 pages. Build3 added B105 and
the exact source-cylinder elimination, producing 405 clean pages. The
last bibliography page had a stranded verification sentence, without any
overflow. We reduced bibliography inter-entry spacing from 3pt to 2.7pt.
Build4 therefore produced 404 pages. A subsequent exact-text scope patch
failed its assertion without changing any file; build5 repeated the same
clean source. The corrected patch updated only the B100 scope paragraph
to reference the proved B102/B105 comparison. Build6 is the final PDF.
All genuine drivers and pass logs remain retained, together with the
402-page draft and 405-page pre-repair PDF and its 54 page renderings.

The successful combined build logs have zero overfull boxes, warnings,
undefined references and errors. Combined before/after overfull counts
are 0/0, including boxes beyond 2pt; maximum 0pt. The bibliography repair
addresses a stranded final line, not an unreported overflow. All 108
bibliography records retain explicit verification status.

We rendered 53 final pages spread across every Part, every new proof and
the bibliography, and displayed and inspected all six final contact
sheets individually. We displayed and inspected the 23 critical pages
listed below individually at full size. This includes the title/abstract,
contents, every page of B101--B105, the revised B100 scope, a bibliography
sample and its final page. Pages 1, 2 and 299--303 had already been inspected
individually in the pre-repair draft; their final PNG bytes are identical,
as verified in unchanged_rendering_comparison.json. All remaining listed
pages were inspected from the final renderings. An initial combined image
attempt at pages 298 and 304 was truncated by the context limit. We did
not count that attempt: both pages were subsequently displayed separately
and inspected, as were pages 305--316 and the bibliography samples.
All literal word arrays, tables, equations, exact sequences and tags fit
and remain legible. We found no clipping, overlap, missing mathematical
glyphs or defective proof layout.

The canonical B101, B102, B104 and B105 component proofs also have their
owners' completed page reviews and genuine build records. Complete
independent mathematical proof reviews are recorded separately; visual
inspection is not substituted for them.

Rendered final pages:
{pages}

Full-size critical final pages:
{enlarged}

Combined drivers: records/checkpoint20_build1_driver.log through
records/checkpoint20_build6_driver.log. Complete genuine pass logs are
under records/build_passes/. Earlier retained PDFs and metrics are under
records/pdf_qa/checkpoint20_before_spherical/ and
records/pdf_qa/checkpoint20_before_bibliography/.
Final metrics: records/checkpoint20_metrics.json and checkpoint20_final_metrics.out.
Final render output: records/checkpoint20_render_final.out.
Final renderings: records/pdf_qa/checkpoint20_final/.
Scope-update provenance: records/B100_scope_update20.md.
Bibliography layout repair: records/checkpoint20_bibliography_layout_repair.md.

Recorded at {now}.
'''
(root/'records/checkpoint20_typesetting.txt').write_text(record)
(root/'records/checkpoint20_visual_review.json').write_text(json.dumps({
    'pdf_sha256':m['pdf_sha256'], 'rendered_pages':pages,
    'contact_sheets_inspected':6, 'individually_inspected_pages':enlarged,
    'inherited_individual_views_with_identical_final_png':[1,2,299,300,301,302,303],
    'combined_overfull_before':0, 'combined_overfull_after':0,
    'cosmetic_repair':'Bibliography inter-entry spacing 3pt to 2.7pt; removed isolated final verification line.',
    'visual_review':'PASS', 'recorded_at':now}, indent=2)+'\n')
p = root/'LM4_SUCCESSOR_report.md'
s = p.read_text()
marker = '### Twentieth-hour final typesetting verification'
assert marker not in s
s += f'''\n{marker}

The final paper has {m['pages']} pages and {m['pdf_bytes']} bytes, SHA-256
{m['pdf_sha256']}. Its final combined log has zero overfull boxes,
warnings, undefined references and errors. Successful combined builds
before and after the cosmetic bibliography repair have overfull counts
0/0, including beyond 2pt. Reducing bibliography inter-entry spacing from
3pt to 2.7pt moved a stranded verification sentence onto the preceding
page, reducing 405 pages to 404. The final source also updates B100's
scope paragraph to cite B102/B105, without changing its claim or proof.
All 108 bibliography records have explicit verification status.

We inspected all six final contact sheets for 53 rendered pages and 23
critical pages individually, including every page of B101--B105, the
updated B100 scope and the final bibliography page. Seven earlier
individual inspections transfer by verified byte-identical final PNGs;
the other sixteen use the final renderings. No clipping, overlapping
tags, missing glyphs or defective layout was found. The failed initial
TeX-format attempt and the later unsuccessful exact-text scope patch
are recorded separately from the successful builds. Exact page lists,
genuine build history and layout counts are retained in
records/checkpoint20_typesetting.txt. Both main full decisions remain Open.
'''
p.write_text(s)
print('Final PDF QA recorded: 53 pages, 6 contact sheets, 23 full-size pages; PASS.')
