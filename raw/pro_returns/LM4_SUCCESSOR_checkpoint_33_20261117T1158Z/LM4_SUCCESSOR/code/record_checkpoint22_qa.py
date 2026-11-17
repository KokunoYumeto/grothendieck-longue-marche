"""Record the completed visible inspection; the script does not perform it."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import re

root = Path(__file__).resolve().parents[1]
m = json.loads((root/'records/checkpoint22_metrics.json').read_text())
assert hashlib.sha256((root/'LM4_SUCCESSOR_paper.pdf').read_bytes()).hexdigest() == m['pdf_sha256']
assert m['statements'] == 280 and m['pages'] == 425
assert m['statuses'] == {'Known':6,'Proved':236,'Refuted':19,'Open':19}
assert not m['overfull'] and not m['warnings'] and not m['errors']
base = root/'records/pdf_qa'
main = json.loads((base/'checkpoint22_final/render_manifest.json').read_text())
supp = json.loads((base/'checkpoint22_supplement/render_manifest.json').read_text())
pages = sorted(set(main['rendered_pages']) | set(supp['rendered_pages']))
assert len(main['rendered_pages']) == 40 and len(supp['rendered_pages']) == 4
assert len(pages) == 44
individual = [1,2]+list(range(320,337))+[421]
assert len(individual) == 20 and set(individual) <= set(pages)
old_log = (base/'checkpoint22_before_overflow_repair/LM4_SUCCESSOR_paper.log').read_text()
before = re.findall(r'Overfull \\hbox \((\d+\.?\d*)pt',old_log)
assert before == ['231.64224']
now = datetime.now(timezone.utc).isoformat()
record = f'''# Twenty-second-hour final PDF typesetting and visual verification

Final PDF SHA-256:{m['pdf_sha256']}.
Final size:{m['pdf_bytes']} bytes;425 pages.
Register:280 statements;236 Proved,19 Refuted,19 Open,6 Known.
Bibliography:109 verified-status entries;49 task/lead rows.
Visual review: PASS.

The first complete B108--B109 build compiled its TeX passes but failed
the mandatory final overflow assertion: one unbreakable typewriter path
produced a231.64224pt overfull box. The preceding PDF, final TeX log and
both formal sources are preserved in checkpoint22_before_overflow_repair.
Changing the three record filenames to the existing breakable path command
resolved it. The second complete build was clean in416 pages. The third
complete build incorporated B110--B111 and the109th bibliography entry;
it is the final clean425-page paper. All actual driver and pass outputs
remain. No mathematical repair was hidden in a layout change.

Initial/final overfull counts:1/0, also1/0 for boxes exceeding2pt.
Maximum initial/final overflow:231.64224pt/0pt. The final log has zero
overfull boxes, warnings, undefined references and errors.

We displayed and inspected all five main contact sheets covering40 pages,
plus the supplemental contact sheet covering4 further pages. The sample
contains every Part, all17 pages of the new B108--B111 material, earlier
dense formulas and tables, the abstract and contents, the new Lorensen
bibliography entry, and the last bibliography page. We additionally
displayed all17 new mathematical pages individually, together with the
title/abstract, continued abstract/contents, and new bibliography page.
All equations, tags, tables, statement openings, proof endings and record
paths fit. No clipping, overlap, missing glyph or additional layout defect
was found. B110's inverse-Nielsen display was placed in gathered before
the final build; its earlier source is retained. B111's canonical source
is byte-identical to the independently reviewed integrated source.

Rendered pages:{pages}
Individually inspected pages:{individual}
Contact sheets inspected:6, all freshly displayed from this final PDF.
No inherited or assumed visual inspection is counted.

Genuine build drivers:checkpoint22_build1_driver.log,
checkpoint22_build2_driver.log,checkpoint22_build3_driver.log.
Complete pass outputs:records/build_passes/.
Final metrics:records/checkpoint22_metrics.json and
checkpoint22_final_metrics.out/.err.
Final renders:checkpoint22_render_final.out/.err and
checkpoint22_render_supplement.out/.err.
Recorded at{now}.
'''
(root/'records/checkpoint22_typesetting.txt').write_text(record)
(root/'records/checkpoint22_visual_review.json').write_text(json.dumps({
    'pdf_sha256':m['pdf_sha256'],'rendered_pages':pages,
    'contact_sheets_inspected':6,'individually_inspected_pages':individual,
    'combined_overfull_before':1,'combined_overfull_after':0,
    'maximum_overflow_before_pt':231.64224,'maximum_overflow_after_pt':0,
    'visual_review':'PASS','recorded_at':now,
    'repair':'Three long B109 record paths made breakable; B110 inverse display gathered before final build.'
},indent=2)+'\n')
p = root/'LM4_SUCCESSOR_report.md'
s = p.read_text()
marker = '### Twenty-second-hour final typesetting verification'
assert marker not in s
s += f'''\n{marker}

The final paper has425 pages,280 statements and109 bibliography records.
Its SHA-256 is{m['pdf_sha256']}; size{m['pdf_bytes']} bytes. The first
build's one231.64224pt overfull path was repaired with breakable path
commands; its PDF, log and sources remain. The second and third complete
builds are clean. Initial/final overflow counts are1/0, including beyond2pt;
the final log also has zero warnings, undefined references and errors.

We inspected six fresh contact sheets covering44 distinct final pages
across all five Parts and the bibliography. Twenty pages were inspected
individually, including every page320--336 of the complete new proofs,
the title/abstract, contents and new Lorensen bibliography entry. All
equations, tables, tags, paths and proof endings fit without overlap,
clipping or missing glyphs. Full records:records/checkpoint22_typesetting.txt
and records/checkpoint22_visual_review.json. Both main decisions remain Open.
'''
p.write_text(s)
print('Final PDF QA recorded:425 pages;44 sampled pages,6 contact sheets,20 full-page views; PASS.')
