"""Run the method audit under final gates, preserving the historical report.

The historical generator is retained as an immutable implementation base.
Adaptations below are applied in memory. Only final-named QA reports are
written. Additional independent checks are in reader_a_final_method_checks.py.
"""
from pathlib import Path
import hashlib

QA = Path(__file__).resolve().parent
base = QA / 'reader_a_method_audit.py'
assert hashlib.sha256(base.read_bytes()).hexdigest() == 'ce9a4c3d7315760a1b757d6d3336938d2cc3daefb40448daf06cdb6c64265d3f'
source = base.read_text()


def swap(old, new):
    global source
    assert source.count(old) == 1, (old[:100], source.count(old))
    source = source.replace(old, new)


swap("ROOT = Path('/workspace/scratch/f28c4f52d3ec')", "ROOT = Path(__file__).resolve().parents[2]")
swap("EXPECTED_PENDING = {'148_scan068', '148_scan069', '148_scan071', '148_scan072', '149_scan003', '149_scan004'}",
     'EXPECTED_PENDING = set()  # All23 audits completed before this final run.')
swap("add('R01', 'resolved_during_audit', 'Reversed 149_scan004 assignment row corrected during audit',",
     "add('R01', 'resolved_before_final_audit', 'Reversed 149_scan004 assignment row corrected before final audit',")
swap("add('P01', 'expected_pending', 'Aggregate decision export awaits final refresh',",
     "add('F08', 'action_required', 'Final aggregate decision export is stale',")
start = source.index("add('P02', 'expected_pending', 'Root adjudication and final transcription freeze remain in progress',")
end = source.index('\n# Packaging simulation:', start)
source = source[:start] + "check('All23 independent audits finalized', not pending_now and len(page_results)==23, {'pending_pages':pending_now})\n" + source[end:]
swap("metadata_files = list((OUT / 'records').glob('*.json')) + list((OUT / 'second').glob('*.json')) + list((ROOT / 'proposed').glob('*.json'))",
     "metadata_files = list((OUT / 'records').glob('*.json')) + list((OUT / 'second').glob('*.json')) + list((ROOT / 'proposed').glob('*.json'))\nmetadata_files.append(QA / 'early_intermediate_provenance.json')")
swap("'original_box', 'source_rect', 'rect', 'box', 'original_bbox', 'bounds',",
     "'original_box', 'source_rect', 'rect', 'box', 'original_bbox', 'bounds', 'source_box',")
swap("injected_archive_names = {'ARCHIVE_CONTENTS.txt', 'CROP_COMPRESSION_MANIFEST.json', 'CROPS_README.md', 'scripts/restore_crops.py'}",
     "injected_archive_names = {'ARCHIVE_CONTENTS.txt', 'CROP_COMPRESSION_MANIFEST.json', 'CROPS_README.md', 'scripts/restore_crops.py', 'CROP_COMPRESSION_MANIFEST_V2.json', 'CROPS_README_V2.md'}")
swap("            missing = sorted(documented_names - current_archive_names - injected_archive_names)",
     "            if 'CROP_COMPRESSION_MANIFEST_V2.json' in names:\n"
     "                compression_manifest = json.loads(z.read('CROP_COMPRESSION_MANIFEST_V2.json'))\n"
     "                documented_names |= {r['path'] for r in compression_manifest.get('original_entries', [])}\n"
     "                documented_names -= {r.get('archived_path') for r in compression_manifest.get('images', []) if r.get('archived_path') and r.get('archived_path') != r.get('original_path')}\n"
     "            missing = sorted(documented_names - current_archive_names - injected_archive_names)")
swap("    ok = bool(p.is_file() and receipt.get('status') == 'succeeded' and receipt.get('library_file_id') and receipt.get('sha256'))",
     "    ok = bool(p.is_file() and receipt.get('status') == 'succeeded' and receipt.get('library_file_id') and receipt.get('sha256'))\n"
     "    actual_archive_sha256 = sha(p) if p.is_file() else None\n"
     "    ok = ok and actual_archive_sha256 == receipt.get('sha256')")
swap("'note': receipt.get('note', '')})",
     "'note': receipt.get('note', ''), 'receipt_sha256':receipt.get('sha256'), 'actual_archive_sha256':actual_archive_sha256})")
swap('summary = {', 'from reader_a_final_method_checks import augment\naugment(globals())\n\nsummary = {')
swap("    'expected_pending_findings': sum(f['severity'] == 'expected_pending' for f in findings),",
     "    'expected_pending_findings': sum(f['severity'] == 'expected_pending' for f in findings),\n"
     "    'post_documentation_gates': sum(f['severity'] == 'post_documentation_gate' for f in findings),\n"
     "    'total_different_boxes': final_extensions['different_boxes'],\n"
     "    'total_changed_boxes': final_extensions['changed_boxes'],\n"
     "    'transcription_hashes': final_extensions['transcription_hashes'],\n"
     "    'final_aggregate_counts': final_extensions['final_aggregate_counts'],")
swap("'audit': 'reader_a read-only method/documentation completeness audit'",
     "'audit': 'reader_a final read-only method/documentation completeness audit'")
swap("'scope': 'Process structure, metadata, frozen row/hash preservation, crop references/provenance and packaging exclusions; no new ink adjudication.'",
     "'scope': 'Final method/identity/339-box comparison/261-MARKS checks,46 frozen TSV continuity,24 transcription hashes, crop provenance and checkpoint/package-tree exclusions. Reader_b owns complementary aggregate-byte/static-TeX/doubt mapping checks. No new ink adjudication or final ZIP creation.'")
swap("'write_scope': 'Only result/qa/reader_a_method_audit.py and reader_a_method_findings.md/.json.'",
     "'write_scope': 'Only new result/qa/reader_a_final_method_audit.py, reader_a_final_method_checks.py and reader_a_final_method_findings.md/.json. Historical19-audit report/generator preserved.'")
swap("'summary': summary, 'findings': findings, 'checks': checks, 'pages': page_results,",
     "'summary': summary, 'findings': findings, 'checks': checks, 'pages': page_results, 'final_extensions':final_extensions,")
swap("'Read-only checks are a timed snapshot while the root reader continues adjudication. Expected pending pages were supplied explicitly in the assignment.'",
     "'All23 adjudications were completed before this final run. Later root documentation synchronization is permitted; current hashes and report timestamps define this snapshot. The final ZIP and its restoration/save receipts require a separate post-package gate.'")
source = source.replace("QA / 'reader_a_method_findings.json'", "QA / 'reader_a_final_method_findings.json'")
source = source.replace("QA / 'reader_a_method_findings.md'", "QA / 'reader_a_final_method_findings.md'")
swap("md = ['# Method and documentation audit'", "md = ['# Final method and documentation audit'")
swap("md += ['## Expected pending work', '']", "md += ['## Final post-documentation gates', '']")
swap("    if f['severity'] == 'expected_pending':", "    if f['severity'] in ('expected_pending','post_documentation_gate'):")
swap("md += ['## Resolved during this audit', '']", "md += ['## Resolved prior findings', '']")
swap("md += ['', '## Limits', ''] + ['- ' + line for line in report['limitations']]",
     "md += ['', '## Final method metrics', '', '```json', json.dumps(final_extensions,ensure_ascii=False,indent=2), '```', '', '## Limits', ''] + ['- ' + line for line in report['limitations']]")

exec(source, globals())
