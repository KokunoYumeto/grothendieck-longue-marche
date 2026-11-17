"""Read-only checks of frozen checkpoint31 evidence before its sole capture.

Pages, PDF identity and visual counts come from the actual final records.
The checkpoint30 compression measurement is not a checkpoint31 estimate.
"""
from pathlib import Path
from collections import Counter
import csv
import hashlib
import json
import re


def main():
    root = Path(__file__).resolve().parents[1]
    read = lambda rel: json.loads((root / rel).read_text())
    sha = lambda rel: hashlib.sha256((root / rel).read_bytes()).hexdigest()
    m = read('records/checkpoint31_metrics.json')
    assert m['statements'] == 333 and m['task_rows'] == 49
    assert m['statuses'] == {'Known': 6, 'Proved': 289, 'Refuted': 19, 'Open': 19}
    assert m['bibliography_entries'] == 114 and m['pages'] > 0
    assert not m['overfull'] and not m['warnings'] and not m['errors']
    assert sha('LM4_SUCCESSOR_paper.pdf') == m['pdf_sha256']
    assert (root / 'LM4_SUCCESSOR_paper.pdf').stat().st_size == m['pdf_bytes']

    review = read('records/checkpoint31_root_formal_reviews.json')
    assert review['status'] == 'PASS_COMPLETE_SOURCE_REVIEW'
    expected = {'A.92', 'A.93', 'A.94', *('B.' + str(n) for n in range(148, 155))}
    assert len(review['copies']) == 10
    assert {row['statement'] for row in review['copies']} == expected
    for row in review['copies']:
        assert (root / row['source']).read_bytes() == (root / row['target']).read_bytes()
        assert sha(row['target']) == row['sha256']
    assert read('records/checkpoint31_formal_source_copies.json')['copies'] == review['copies']
    for rel, digest in review['independent_reviews'].items():
        assert sha(rel) == digest, rel
    rows = list(csv.DictReader((root / 'LM4_SUCCESSOR_results.csv').open()))
    assert len(rows) == 333 and dict(Counter(r['status'] for r in rows)) == m['statuses']
    tasks = list(csv.DictReader((root / 'task_coverage.csv').open()))
    assert len(tasks) == 49
    for task in ('A.8', 'B.4'):
        assert next(r for r in tasks if r['task'] == task)['outcome'] == 'Open'
    assert (root / 'LM4_SUCCESSOR_report.md').read_text().splitlines()[0] == 'INCOMPLETE'
    entries = re.split(r'(?m)(?=^@)', (root / 'LM4_SUCCESSOR_references.bib').read_text())[1:]
    assert len(entries) == 114
    assert all(re.search(r'\b(?:verified|unverified)\b', entry, re.I) for entry in entries)
    assert len(re.findall(r'\\bibitem', (root / 'LM4_SUCCESSOR_paper.bbl').read_text())) == 114

    visual = read('records/checkpoint31_visual_review.json')
    render = read('records/pdf_qa/checkpoint31_final/render_manifest.json')
    assert visual['visual_review'] == 'PASS'
    assert visual['pdf_sha256'] == render['pdf_sha256'] == m['pdf_sha256']
    assert render['page_count'] == m['pages'] and render['dpi'] == 144
    assert visual['rendered_pages'] == render['rendered_pages']
    assert visual['required_math_pages'] == render['required_new_mathematical_pages']
    assert visual['required_math_pages'] and visual['rendered_pages']
    assert set(visual['required_math_pages']) <= set(visual['individually_inspected_pages'])
    assert set(visual['individually_inspected_pages']) <= set(visual['rendered_pages'])
    assert visual['contact_sheets_inspected'] == render['contact_sheets'] > 0
    assert visual['each_contact_sheet_opened_separately']
    assert not visual['truncated_outputs_counted']
    assert visual['final_log_and_stdout_case_insensitive'] == 'PASS'
    previous = read('records/checkpoint30_visual_review.json')
    old_notices = Counter(previous['final_log_and_stdout_audits'][0]['underfull_notices'])
    assert sum(old_notices.values()) == 19
    assert len(visual['final_log_and_stdout_audits']) >= 2
    final_notices = None
    for audit in visual['final_log_and_stdout_audits']:
        assert sha(audit['path']) == audit['sha256'], audit['path']
        assert not audit['warnings'] and not audit['issues']
        notices = Counter(audit['underfull_notices'])
        if final_notices is None:
            final_notices = notices
        else:
            assert notices == final_notices, 'Final log and stabilized stdout notices must agree.'
    assert visual['underfull_scope'], 'Document every retained, removed or newly accepted underfull notice.'
    qa = (root / 'records/checkpoint31_typesetting.txt').read_text()
    assert 'Visual review: PASS' in qa and m['pdf_sha256'] in qa

    # The unchanged 64 MiB extension was genuinely measured in cycle30.
    # Its evidence is retained; cycle31 also checks the actual immediately prior streams.
    measurement = read('records/checkpoint30_data64_measurement.json')
    compatibility = read('records/checkpoint30_storage_extension_check.json')
    assert measurement['input_archive'] == 'LM4_SUCCESSOR_checkpoint_29.zip'
    assert measurement['dictionary_bytes'] == compatibility['dictionary_bytes'] == 67108864
    assert measurement['zip_method'] == 'ZIP_LZMA'
    assert measurement['unchanged_standard_library_decoder_roundtrip'] == 'PASS_EVERY_BYTE_SHA256_AND_LENGTH'
    assert measurement['decoder_eof'] and not measurement['creates_zip']
    assert not measurement['mutates_earlier_archive'] and not measurement['new_work_estimate']
    assert compatibility['backward_reader_compatibility'] == 'PASS'
    assert compatibility['unchanged_standard_decoder_roundtrip'] == 'PASS_EXACT_BYTES'
    assert compatibility['dictionary_context_normal_and_exception_restore'] == 'PASS'
    assert compatibility['original_archive_unchanged'] and not compatibility['creates_zip']
    assert compatibility['original_archive_sha256'] == measurement['input_archive_sha256']
    measured_prior = read('records/checkpoint29_archive_verification.json')
    assert measured_prior['sha256'] == measurement['input_archive_sha256']
    assert measured_prior['bytes'] == measurement['input_archive_bytes']
    prior = read('records/checkpoint30_archive_verification.json')
    native = read('records/checkpoint30_system_tars_verification.json')
    assert native['archive'] == prior['archive'] == 'LM4_SUCCESSOR_checkpoint_30.zip'
    assert native['archive_sha256'] == prior['sha256']
    assert native['all_three_system_tar_restores'] == native['current_main_pdf_direct'] == 'PASS'
    assert native['all_three_container_zip_lzma_methods'] == 'PASS'
    assert native['data_lzma_dictionary_bytes'] == 67108864
    for kind in ('images', 'documents', 'data'):
        assert native['containers'][kind]['system_tar_restore'] == 'PASS'
        assert native['containers'][kind]['every_original_path_size_and_hash'] == 'PASS'
    assert prior['prior_entries_retained'] + prior['entries'] == 123532
    assert prior['crc'] == prior['every_manifest_entry'] == prior['every_retained_version'] == 'PASS'
    expected_archives = {f'LM4_SUCCESSOR_checkpoint_{n:02d}.zip' for n in range(1, 31)}
    assert {p.name for p in root.parent.glob('LM4_SUCCESSOR_checkpoint_[0-9][0-9].zip')} == expected_archives

    estimate = read('records/checkpoint31_size_estimate.json')
    assert estimate['estimated_total_with_allowance'] < estimate['delivery_cap_bytes'] == 536870912
    assert not estimate['creates_zip'] and not estimate['writes_authored_input_files']
    assert estimate['baseline_archive'] == prior['archive']
    assert estimate['baseline_bytes'] == prior['bytes'] and estimate['baseline_sha256'] == prior['sha256']
    assert estimate['current_main_pdf_sha256'] == m['pdf_sha256']
    for kind in ('images', 'documents', 'data'):
        assert estimate['prospective_bundles'][kind]['zip_method'] == 'ZIP_LZMA'
    assert estimate['prospective_bundles']['data']['dictionary_bytes'] == 67108864

    freeze = read('records/checkpoint31_writer_pause.json')
    assert freeze['all_writers_paused'] and len(freeze['agents']) == 3
    assert not freeze['live_producers']
    for rel in ('records/thirty_first_hour_research_report.md',
                'records/checkpoint31_computation_audit_state.md',
                'records/primary_readings31.md',
                'code/verify_checkpoint31_system_tars.py'):
        assert (root / rel).is_file(), rel
    late = read('records/checkpoint31_root_late_reviews.json')
    assert late['status'] == 'PASS_COMPLETE_LATE_PROOF_REVIEW_WITH_EXPLICIT_REMAINING_GATES'
    assert late['formal_statement_count'] == 333 and not late['formal_promotion']
    assert late['proof_sources'] and late['independent_reviews']
    for field in ('proof_sources', 'independent_reviews'):
        for rel, digest in late[field].items():
            assert sha(rel) == digest, rel
    assert not (root.parent / 'LM4_SUCCESSOR_checkpoint_31.zip').exists()
    print(f"PASS: 333 statements, {m['pages']} pages, 49 tasks, 114 printed references; "
          f'ten reviewed formal sources; {sum(final_notices.values())} documented underfull notices; '
          'three-container estimate and actual 64 MiB stream compatibility; both mains Open.')


if __name__ == '__main__':
    main()
