"""Record actual individual image observations of the final checkpoint34 PDF."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil

root = Path(__file__).resolve().parents[1]
read = lambda rel: json.loads((root / rel).read_text())
sha = lambda rel: hashlib.sha256((root / rel).read_bytes()).hexdigest()
now = lambda: datetime.now(timezone.utc).isoformat()
m = read('records/checkpoint34_metrics.json')
render = read('records/pdf_qa/checkpoint34_final/render_manifest.json')
audit = read('records/checkpoint34_final_pdf_audit.json')
assert sha('LM4_SUCCESSOR_paper.pdf') == m['pdf_sha256'] == render['pdf_sha256'] == audit['final_pdf_sha256']
assert m['pages'] == render['page_count'] == 646
assert audit['final_overfull_count'] == 0 and audit['final_underfull_count'] == 19
assert audit['underfull_identical_to_checkpoint33']
render_path = 'records/pdf_qa/checkpoint34_final/render_manifest.json'
root_pages = [1, 2, 4, 186, 187, 188, 189, 635, 646]
observations = {
    1: 'Title, INCOMPLETE status, author credit and abstract text clear; no clipping or overlap.',
    2: 'New central-congruence and cohomology scope in abstract clear; whole page within margins.',
    4: 'End of abstract and contents transition clear, including wrapped Part C title.',
    186: 'A110 conclusion and provenance plus A111 statement, boxes, conjugator and cocycle definitions fit.',
    187: 'Whole original CM comparison statement and full conjugator/cocycle proof fit; tags and citations legible.',
    188: 'All signed matrices, centralizer proof and longer multi-line formulas remain legible within margins.',
    189: 'Six-row exact matrix table, finite-certificate provenance and transition to Part B are clear.',
    635: 'Reference opening and new Beyl entry including verified reading scope and retrieval limitation are legible.',
    646: 'Final reference entries and page number clear; no missing glyphs or clipped text.'}
receipt = dict(recorded_at=now(), reviewer='/root', status='PASS', pdf_sha256=m['pdf_sha256'],
    render_manifest_sha256=sha(render_path), individual_pages=root_pages,
    each_actual_image_view_was_separate=True, truncated_outputs_counted=False,
    excluded_attempt='The pre-compaction truncated page186 tool output is excluded; page186 was freshly opened in a complete standalone output after resumption.',
    pages=[dict(page=n, path=f'records/pdf_qa/checkpoint34_final/page-{n:03d}.png',
                sha256=sha(f'records/pdf_qa/checkpoint34_final/page-{n:03d}.png'),
                actually_viewed_individually=True, result='PASS', observation=observations[n], issues=[])
           for n in root_pages],
    contacts=[dict(path=f'records/pdf_qa/checkpoint34_final/contact-{n:02d}.png',
                   sha256=sha(f'records/pdf_qa/checkpoint34_final/contact-{n:02d}.png'),
                   actually_viewed_separately=True, result='PASS', issues=[]) for n in range(1,6)],
    contact_observation='Each of five complete contact images opened separately. All44 rendered pages have consistent margins, no clipped material, no collisions or missing-glyph patterns. Contact inspection supplements the individual new-page views.',
    issues=[])
root_receipt = 'records/checkpoint34_root_visual_observations.json'
assert not (root / root_receipt).exists()
(root / root_receipt).write_text(json.dumps(receipt, indent=2)+'\n')
receipts = ['work_A/review_checkpoint34_final_pages174_178.json',
            'work_CE/checkpoint34_visual_pages_179_185.json',
            'work_DE/checkpoint34_visual_review_pages552_556.json', root_receipt]
individual = set()
for rel in receipts:
    item = read(rel)
    assert item['pdf_sha256'] == m['pdf_sha256']
    manifest = item.get('render_manifest_sha256')
    if manifest is None:
        manifest = item['render_manifest']['sha256']
    assert manifest == sha(render_path)
    for row in item['pages']:
        assert row.get('result',row.get('status')) == 'PASS' and not row.get('issues', [])
        assert row.get('actually_viewed_individually',row.get('actually_viewed')) is True
        path = row.get('path',row.get('file'))
        assert sha(path) == row['sha256']
        individual.add(row['page'])
assert set(render['required_new_mathematical_pages']) <= individual
assert individual <= set(render['rendered_pages'])
for row in audit['final_log_and_stdout_audits']:
    assert sha(row['path']) == row['sha256'] and not row['warnings'] and not row['issues']
record = dict(recorded_at=now(), visual_review='PASS', pdf_sha256=m['pdf_sha256'],
    rendered_pages=render['rendered_pages'], required_math_pages=render['required_new_mathematical_pages'],
    individually_inspected_pages=sorted(individual),
    individual_page_review_receipts={rel:sha(rel) for rel in receipts},
    contact_sheets_inspected=5, each_contact_sheet_opened_separately=True, truncated_outputs_counted=False,
    final_log_and_stdout_case_insensitive='PASS', final_log_and_stdout_audits=audit['final_log_and_stdout_audits'],
    underfull_scope='Exactly19 final underfull notices, identical as a multiset to checkpoint33 and to the final stabilized stdout. No new underfull paragraph.',
    corrected_edition_scope='Final646-page PDF. All21 new mathematical pages freshly rendered and individually viewed. Five additional front/reference pages individually viewed. All44 rendered pages covered by five separately opened contact images. First34 build had one17.66902pt overflow on183; corrected first and final passes have zero. CE individually viewed the corrected183 page.')
target = root / 'records/checkpoint34_visual_review.json'
assert not target.exists()
target.write_text(json.dumps(record, indent=2)+'\n')
text = ('Visual review: PASS\nFinal PDF SHA256: '+m['pdf_sha256']+'\n'
        '646 pages;21 new mathematical pages individually inspected;26 individual pages overall;44 rendered pages on5 separately opened contact images.\n'
        'Final engine log and stabilized stdout:0 overfull,0 warnings,0 errors;19 unchanged underfull notices.\n'
        'Overflow counts: before integration0; first34 build1 at17.66902pt on page183; corrected first pass0; final0.\n'
        'The first build, every source change and log are preserved. The provenance-only correction changes no mathematical or path bytes.\n')
target = root / 'records/checkpoint34_typesetting.txt'
assert not target.exists()
target.write_text(text)
backup = root / 'records/checkpoint34_before_final_qa'
backup.mkdir(exist_ok=False)
append = '\n### Observed final34 typesetting verification\n\n'+text.replace('\n','  \n')+'\n'
for rel in ['records/thirty_fourth_hour_research_report.md','LM4_SUCCESSOR_report.md']:
    path = root / rel
    saved = backup / rel
    saved.parent.mkdir(parents=True,exist_ok=True)
    shutil.copyfile(path, saved)
    path.write_text(path.read_text()+append)
print(json.dumps(dict(status='PASS', pdf_sha256=m['pdf_sha256'], pages=646,
    required_math_pages=21, individual_pages=len(individual), rendered_pages=44, contacts=5),indent=2))
