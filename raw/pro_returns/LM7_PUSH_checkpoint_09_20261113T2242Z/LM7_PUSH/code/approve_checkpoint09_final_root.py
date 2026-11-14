#!/usr/bin/env python3
"""Record the actual final-page inspection and prepare the immutable checkpoint.

This script changes no mathematical proof. Earlier QA/report text and the
unmodified archiver are retained, and all active TeX hashes must still match
the already-built, inspected PDF.
"""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent.parent

def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(8 * 1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()

prior_path = ROOT/'research/checkpoint09_final_approval_prior.json'
assert not prior_path.exists()
qa_path = ROOT/'research/checkpoint09_visual_qa_final.json'
assert not qa_path.exists()
qa = json.loads((ROOT/'research/checkpoint09_final_delta_qa.json').read_text())
assert qa['page_count'] == 513
assert qa['changed_or_new_sampled_pages'] == [506, 507]
assert len(qa['byte_identical_previously_inspected_pages']) == 442
assert len(qa['rendered_pages']) == 444
assert qa['pdf_sha256'] == sha(ROOT/'LM7_PUSH_paper.pdf')
prior = ROOT/qa['prior_actual_inspection_record']
assert sha(prior) == qa['prior_record_sha256']
assert json.loads(prior.read_text())['visually_inspected']
for page in [506, 507]:
    name = f'page_{page:03d}.png'
    assert sha(ROOT/qa['render_directory']/name) == qa['image_sha256'][name]
assert qa['current_log']['overfull_boxes'] == 0
assert not qa['current_log']['undefined_citations']
assert not qa['current_log']['undefined_references']
inputs = json.loads((ROOT/'build/source_input_manifest.json').read_text())
assert all(sha(ROOT/name) == value for name, value in inputs['source_sha256'].items())

qa['visually_inspected'] = True
qa['approved_for_delivery'] = True
qa['freshly_inspected_full_resolution_pages'] = [506, 507]
qa['inspection_notes'] = [
    'Root actually viewed both changed final pages 506 and 507 at full resolution after the fifth build.',
    'The remaining 442 sampled page PNGs are byte-identical to the fourth-build approved record; that record retains eight inspected contact panels and sixteen full-resolution inspections.',
    'No clipped text, equation overlap, truncated table, footer collision, or margin overflow was observed on either changed page.',
    'The fifth build has 513 pages, zero overfull boxes, no undefined references or citations, and an exact active-source hash match.',
    'The fourth-build preservation reason contains the old numeral 512; its actual PDF and approved QA have 513 pages. The immutable reason is retained.',
]
old_report = (ROOT/'research/report_body.md').read_text()
old_visual = (ROOT/'research/visual_qa.json').read_text()
prior_path.write_text(json.dumps({
    'prior_report_body': old_report,
    'prior_visual_qa': old_visual,
    'prior_report_sha256': sha(ROOT/'research/report_body.md'),
    'prior_visual_qa_sha256': sha(ROOT/'research/visual_qa.json'),
    'active_tex_source_sha256': inputs['source_sha256'],
}, indent=2) + '\n')
qa_path.write_text(json.dumps(qa, indent=2) + '\n')
(ROOT/'research/visual_qa.json').write_bytes(qa_path.read_bytes())

addition = '''

## Checkpoint 09: verified integration through E.73

The assembled register contains 218 numbered statements: 207 Proved, seven Refuted, three Known with their reductions, and one Open. All 29 required task and lead rows are present. E.3 remains Open. The final paper contains 513 pages, with 103 active TeX inputs and 62 bibliography entries. E.59 through E.73 are integrated with their exact proved scopes and retained root replay records; E.58 already proves the full gentle extra-CM existence assertion. E.65's quadratic character on the full profinite GT group remains unevaluated.

The first checkpoint-09 build, before the later integrations, and every subsequent build attempt are preserved. The second and third builds each had one 27.21799-point overflow in an E.63 program-family list. The fourth and fifth builds have zero overfull boxes and no undefined references or citations. The active E.63 typesetting derivative replaces only that three-filename prose list by a three-line display; the frozen audited mathematical proof remains byte-identical in its original file. Exact source transformations and the failed local-stretch attempt are retained. One stale coverage sentence was then replaced by the completed E.73 result. The initial failed exact-string correction, its driver, outputs, and already valid QA record are preserved before the corrected run.

The final PDF SHA-256 is 20aaf32a06627e6a7c6f259fb8798cd8c4c7472eed5867dd6741bcdbeaa15207. The visual record samples 444 pages. Root viewed all eight new fourth-build contact panels and sixteen individual pages at full resolution. The fifth build has 442 byte-identical sampled pages and exactly two changed pages, 506 and 507, both inspected again at full resolution. No clipping, overlap, truncated table, or footer collision was observed. The entire inspection chain and image hashes are retained. The fourth-build preservation reason retains an obsolete numeral 512; its actual frozen PDF and verified inspection record both have 513 pages. Every active source hash still matches the final build.

E.74 and E.76 have passed complete root proof/program reads and isolated mathematical replays, but are not included in this checkpoint's numbered register. E.74's replay took 21.265699 seconds and retained all 55,296 finite values. E.76's replay took 19.532 seconds; its successor changes only the initial genus scope to the three certified genera 2, 3, and 4, with the earlier proof and manifest preserved. E.75's entire matrix/Gaussian comparison has been computed and independently reviewed; its final package is being completed. Root's next exact E.62-to-double-cover map has passed preparation, all 39 full-preimage queries, and an independent full word replay; its proof and prescribed-target evaluation are subsequent work. Files from these ongoing calculations are included as dated research state, not incorporated as additional proved statements. The A5 surface-cover and full-GT character routes continue.

The checkpoint archive retains all earlier immutable ZIP checkpoints. The derived archiver hardlinks only those immutable history ZIPs into the frozen staging tree, copies every other file, and streams large-file hashes. This changes storage mechanics only. The original archiver remains unchanged, and the exact derived transformation is recorded. The single complete ZIP and any delivery-sized parts are verified by hashes and ZIP CRCs. A checkpoint records the current work; it does not terminate the remaining E.3 investigation.
'''
(ROOT/'research/report_body.md').write_text(old_report + addition)

original_path = ROOT/'code/checkpoint_archive.py'
original = original_path.read_text()
derived = original.replace('import hashlib\n', 'import hashlib\nimport os\n', 1)
anchor = 'workspace = root.parent\n'
replacement = '''workspace = root.parent

def file_sha256(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(8 * 1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()

def copy_with_immutable_history_links(src, dst):
    source = Path(src)
    relative = source.relative_to(root)
    if relative.parts[0] == 'history' and source.suffix == '.zip':
        os.link(source, dst)
        return str(dst)
    return shutil.copy2(src, dst)
'''
assert derived.count(anchor) == 1
derived = derived.replace(anchor, replacement, 1)
anchor = 'shutil.copytree(root, frozen, ignore=shutil.ignore_patterns('
assert derived.count(anchor) == 1
derived = derived.replace(anchor, 'shutil.copytree(root, frozen, copy_function=copy_with_immutable_history_links, ignore=shutil.ignore_patterns(', 1)
anchor = "        data = path.read_bytes()\n        lines.append(f'{path.relative_to(frozen)}\\t{len(data)}\\t{hashlib.sha256(data).hexdigest()}')"
assert derived.count(anchor) == 1
derived = derived.replace(anchor, "        lines.append(f'{path.relative_to(frozen)}\\t{path.stat().st_size}\\t{file_sha256(path)}')", 1)
anchor = "'sha256': hashlib.sha256(archive.read_bytes()).hexdigest(),"
assert derived.count(anchor) == 1
derived = derived.replace(anchor, "'sha256': file_sha256(archive),", 1)
new_path = ROOT/'code/checkpoint_archive_safe_root.py'
assert not new_path.exists()
new_path.write_text(derived)
assert sha(original_path) == hashlib.sha256(original.encode()).hexdigest()
(ROOT/'research/checkpoint09_archive_derivation.json').write_text(json.dumps({
    'original': str(original_path.relative_to(ROOT)),
    'original_sha256': sha(original_path),
    'derived': str(new_path.relative_to(ROOT)),
    'derived_sha256': sha(new_path),
    'mutations': ['hardlink immutable history ZIPs only; copy2 every other main-tree file',
                  'stream manifest-file and final-archive SHA-256'],
    'original_unchanged': True,
}, indent=2) + '\n')
print(json.dumps({'status': 'PASS_FINAL_QA_AND_CHECKPOINT09_PREPARATION',
                  'pdf_sha256': qa['pdf_sha256'], 'pages': 513,
                  'sampled_pages': 444, 'fresh_inspected_pages': [506, 507],
                  'derived_archiver_sha256': sha(new_path)}, indent=2))
