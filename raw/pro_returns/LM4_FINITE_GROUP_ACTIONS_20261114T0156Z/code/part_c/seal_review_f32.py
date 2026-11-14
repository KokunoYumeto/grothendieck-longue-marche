"""Bind the completed independent F.32 proof/code/evidence review."""
from pathlib import Path
from hashlib import sha256
import json
import re

ROOT = Path(__file__).resolve().parents[3]
PART = ROOT/'work/part_c'
STEM = 'work/part_a/f_nonproduct_first_character_one_images'
EXPECTED = {
    STEM+'.tex': 'b91fd2611f1d9bd5cde096c6307004dca0fc740463971c164aa0fe52a146af13',
    STEM+'_results.json': 'ba4c8a418f8a6b11fd083a2568689c1cb7fcec159003b290b53de968a7938cef',
    STEM+'_report.txt': '3522480edbca67dba678009f9e530e6670fefa60e787783b84a4245a8ffce37c',
    STEM+'_evidence_manifest.json': '86e68a925d9d6a151d5ce5e292d9042cf7848402e84e7b9d0a6a125d99a6881f',
    'work/part_a/code/affine_nonproduct_r1_independent_audit.py':
        '584b3f7de2e2093ac9c8b04c1c03b962d71b2a4fac7a75545fb9956c0e361482',
    'work/part_a/code/affine_nonproduct_r1_independent_audit_output.json':
        'c159761cb68c7750eb54a5be31e8fd41cf25b1a0ba3a0463ad4eab8809eec92a',
    'work/part_c/f32_independent_replay/comparison.json':
        '27fbfce87e9485dcb2bc728c7f25e49a9894eff2737576c38156536d63fe8dfa',
    'work/part_c/f32_independent_replay/printed_formula_crosscheck.py':
        'c0d191fc5ba4d354804eed3ce90e7b503edcc858c82f926b37e17f4483e9a0cc',
    'work/part_c/f32_independent_replay/printed_formula_crosscheck_output.json':
        '62837fb0c8824431e64ee1cf518103760bdd7b5805c286dc41d03beeeeac442d',
}


def resolve(path):
    answer = Path(path)
    return answer if answer.is_absolute() else ROOT/answer


def binding(path):
    path = resolve(path)
    assert path.is_relative_to(ROOT)
    data = path.read_bytes()
    return {'path': str(path.relative_to(ROOT)), 'bytes': len(data),
            'sha256': sha256(data).hexdigest()}


def check_record(record):
    observed = binding(record['path'])
    assert observed['sha256'] == record['sha256'], record['path']
    if 'bytes' in record:
        assert observed['bytes'] == record['bytes'], record['path']
    return observed


def verify_manifest(path):
    document = json.loads(resolve(path).read_text())
    entries = [check_record(record) for record in document['entries']]
    assert len({record['path'] for record in entries}) == len(entries)
    return {'manifest': binding(path), 'entry_count': len(entries),
            'all_entries_exact': True, 'entry_checks': entries}


def dump_bytes(value):
    return (json.dumps(value, indent=2)+'\n').encode()


def main():
    report_path, json_path = PART/'review_f32.txt', PART/'review_f32.json'
    assert not report_path.exists() and not json_path.exists()
    primary = [binding(path) for path in EXPECTED]
    for record in primary:
        assert record['sha256'] == EXPECTED[record['path']]
    author_manifest = verify_manifest(STEM+'_evidence_manifest.json')
    assert author_manifest['entry_count'] == 59
    author_meta = json.loads(resolve(STEM+'_results.json').read_text())
    assert author_meta['proof_sha256'] == EXPECTED[STEM+'.tex']
    assert author_meta['independent_check_count'] == 1088
    assert author_meta['peer_additional_printed_formula_checks'] == 86

    f23 = verify_manifest('work/part_a/f_source_sign_and_marginal_images_evidence_manifest.json')
    original_words = 'work/part_a/code/full_cross_source_stage/marginal_braids.json'
    original_record = next(e for e in f23['entry_checks'] if e['path'] == original_words)
    assert original_record['sha256'] == '06285f481708bdaa3c90922344a22381da2ac0ddbfde01684c9ef0013eb135fa'
    words = json.loads(resolve(original_words).read_text())
    labels = ['old0']+[f'old_1_{i}' for i in range(5)]+[f'old_-1_{i}' for i in range(5)]
    source_inventory = []
    for index, label in enumerate(labels):
        record = next(r for r in words['records'] if r['label'] == label)
        source_inventory.append({'zero_based_index': index, 'label': label,
                                 'negative_braid_length': len(record['negative_braid'])})
    assert [r['negative_braid_length'] for r in source_inventory] == [
        122, 60, 56, 92, 154, 104, 140, 170, 92, 66, 82]
    assert author_meta['literal_source_labels'] == labels
    assert author_meta['literal_source_braid_lengths'] == [
        r['negative_braid_length'] for r in source_inventory]

    preservation_path = STEM+'_preservation.json'
    preserved = json.loads(resolve(preservation_path).read_text())
    previous = []
    for item in preserved['manifests']:
        observed = verify_manifest(item['manifest'])
        assert observed['manifest']['sha256'] == item['manifest_sha256']
        assert observed['entry_count'] == item['entries']
        previous.append(observed)
    assert len(previous) == 8
    assert sum(item['entry_count'] for item in previous) == preserved['entry_count'] == 277

    replay_folder = PART/'f32_independent_replay'
    replay = json.loads((replay_folder/'comparison.json').read_text())
    assert replay['total_exact_checks'] == 1088
    assert replay['check_total'] == 710 and replay['word_parser_check_total'] == 378
    assert replay['exit_code'] == 0 and replay['stderr_bytes'] == 0
    assert replay['copied_input_count'] == 12
    for item in replay['input_bindings']:
        check_record(item['source'])
        check_record(item['isolated_copy'])
        assert resolve(item['source']['path']).read_bytes() == resolve(item['isolated_copy']['path']).read_bytes()
    for key in ['runner', 'checker_source', 'checker_copy', 'source_output',
                'isolated_output', 'transported_output', 'stdout', 'stderr']:
        check_record(replay[key])
    original = resolve(replay['source_output']['path']).read_bytes()
    isolated = resolve(replay['isolated_output']['path']).read_bytes()
    original_data, isolated_data = json.loads(original), json.loads(isolated)
    forward = replay['input_path_bijection']
    inverse = {old: new for new, old in forward.items()}
    assert len(forward) == len(inverse) == 12
    transported = dict(isolated_data)
    transported['inputs'] = {forward[p]: v for p, v in isolated_data['inputs'].items()}
    assert dump_bytes(transported) == original
    reversed_data = dict(original_data)
    reversed_data['inputs'] = {inverse[p]: v for p, v in original_data['inputs'].items()}
    assert dump_bytes(reversed_data) == isolated
    old_stdout_path = replay['stdout_transport']['source_stdout']['path']
    old_stdout = resolve(old_stdout_path).read_bytes()
    new_stdout = resolve(replay['stdout']['path']).read_bytes()
    old_hash = binding(replay['source_output']['path'])['sha256'].encode()
    new_hash = binding(replay['isolated_output']['path'])['sha256'].encode()
    assert old_stdout.count(old_hash) == new_stdout.count(new_hash) == 1
    assert old_stdout.replace(old_hash, new_hash) == new_stdout
    assert new_stdout.replace(new_hash, old_hash) == old_stdout
    formula = json.loads((replay_folder/'printed_formula_crosscheck_output.json').read_text())
    assert formula['total_exact_checks'] == 86
    for key in ['program', 'proof', 'checker', 'checker_output', 'general_producer_output']:
        check_record(formula[key])

    proof = resolve(STEM+'.tex').read_text()
    lines = proof.splitlines()
    tags = re.findall(r'\\tag\{(F\.32\.\d+)\}', proof)
    assert len(lines) == 677
    assert [line.strip() for line in lines].count(r'\[') == 24
    assert [line.strip() for line in lines].count(r'\]') == 24
    assert tags == [f'F.32.{i}' for i in range(1, 25)]
    producers = {
        'work/part_a/code/affine_nonproduct_boundary_quotient_stage.py': 125,
        'work/part_a/code/affine_nonproduct_r1_source_stage.py': 72,
        'work/part_a/code/affine_nonproduct_r1_moving_rows_stage.py': 104,
        'work/part_a/code/affine_nonproduct_r1_determinants_stage.py': 100,
    }
    for path, count in producers.items():
        assert len(resolve(path).read_text().splitlines()) == count
    assert len(resolve('work/part_a/code/affine_nonproduct_r1_independent_audit.py').read_text().splitlines()) == 318
    general = json.loads(resolve('work/part_a/code/affine_nonproduct_boundary_quotient_stage_output.json').read_text())
    assert general['records'][0]['source_zero_r_h_quadratic_zero'] is False
    assert general['records'][0]['source_zero_trace_equals_5r_plus_h'] is False

    appendix = [
        '', 'FINAL EXACT BINDING APPENDIX', '',
        'All SHA256 values below were independently recomputed by the peer sealer.',
        'Final author manifest: 59/59 exact path, byte-count and SHA256 bindings.',
        f'F.23 manifest: {f23["entry_count"]}/{f23["entry_count"]} exact bindings, including original words.',
        'F.24--F.31 preservation: eight manifests and all 277 recorded routes exact.',
        'Isolated replay: 1,088 PASS; complete output and stdout transports checked',
        'in both directions by the exact twelve-input-key and consequent hash maps.',
        'Direct TeX comparison: 86 PASS, including all forty printed row entries.',
        '',
    ]
    for record in primary:
        appendix += [record['path'], f'  {record["bytes"]} bytes; SHA256 {record["sha256"]}']
    appendix += ['', 'No frozen author or previously accepted proof/evidence file was edited.', '']
    report_path.write_text((PART/'review_f32_body.txt').read_text()+'\n'.join(appendix))
    result = {
        'status': 'PASS_INDEPENDENT_F32_FULL_PROOF_CODE_EVIDENCE_AND_REPLAY_REVIEW',
        'claim': 'F.32', 'reviewer': '/root/c89_review_and_general_c',
        'corrections_requested': [], 'mathematical_issues': [],
        'proof_full_read_lines': 677, 'checker_full_read_lines': 318,
        'producer_full_read_lines': producers,
        'reused_helpers': {
            'F29_word_arithmetic': 'Previously fully reviewed and hash-bound; executed unchanged by the literal-word checker.',
            'F31_sparse_arithmetic': 'Previously fully reviewed and hash-bound producer dependency; not executed by this isolated checker.'},
        'primary_bindings': primary,
        'author_announced_final_hashes': EXPECTED,
        'evidence_manifest': author_manifest,
        'read_and_checked_categories': [
            'Exact first-scalar-one/nontrivial-boundary scope and all coefficient-field cases',
            'Actual source membership and both-direction preservation of K',
            'Original deleted-generator scalar subgroup and both field inclusions',
            'Both six-variable Laurent coefficient maps',
            'Actual principal quotient N, H and inverse J/E maps',
            'Literal decoration, full source action and cleared intertwiners',
            'Actual X1 kernel, inverse basis and quotient character',
            'Eight polynomial annihilators and direct evaluation rows',
            'All forty printed row entries, P4/P6, roots and scalar tables',
            'Four determinants and exact column-scaling map',
            'Actual proper Frobenius fixed field and all nonzero factors',
            'Three exhaustive simple-subspace type comparisons with inverse intertwiners',
            'Minimal invariant kernel, exact principal tuples and rank',
            'Trace kernel and actual larger-field affine reduction',
            'Both original sign maps and all continuity statements',
            'Complete four-producer/checker review and isolated unchanged replay',
            'Unused failed general-data exploratory flags retained explicitly',
            'Final metadata/report/manifest and all prior evidence preservation'],
        'source_inventory': source_inventory,
        'f23_manifest': f23,
        'f23_original_braid_entry': original_record,
        'source_display_check': {'line_count': 677, 'standalone_open_displays': 24,
                                 'standalone_close_displays': 24, 'exact_numbered_tags': tags},
        'independent_replay': {
            'comparison': binding(replay_folder/'comparison.json'),
            'runner': binding('work/part_c/code/replay_f32.py'),
            'all_replay_files': [binding(p) for p in sorted(replay_folder.rglob('*')) if p.is_file()],
            'total_exact_checks': 1088, 'direct_checks': 710, 'word_parser_checks': 378,
            'input_key_bijection': forward, 'inverse_input_key_bijection': inverse,
            'whole_output_forward_and_inverse_bytes_equal': True,
            'whole_stdout_forward_and_inverse_bytes_equal': True,
            'original_input_and_checker_bytes_unchanged': True,
            'setup_correction': binding('work/part_c/f32_replay_setup_notes/setup_correction.json'),
            'setup_before_runner': binding('work/part_c/f32_replay_setup_notes/runner_before_setup_correction.py')},
        'printed_formula_comparison': {
            'program': binding(replay_folder/'printed_formula_crosscheck.py'),
            'output': binding(replay_folder/'printed_formula_crosscheck_output.json'),
            'counts': formula['checks'], 'total_exact_checks': 86,
            'source_formulas_parsed_directly': True,
            'integer_Laurent_parser_independent_of_certificate_helpers': True},
        'full_huge_matrix_outputs_read_manually': False,
        'matrix_output_validation': 'Reconstructed from literal original words and exact dictionary arithmetic; displayed formulas independently parsed and compared.',
        'preservation_record': binding(preservation_path),
        'prior_evidence_preservation': previous,
        'prior_manifest_count': 8, 'prior_route_count': 277,
        'scope': 'Exact F.32 character locus, all finite coefficient fields and both original signs; original image equality plus summed H1 injection, exact cocycle kernel and rank.',
        'assembled_pdf_compilation_or_visual_review': False,
        'all_completed_earlier_sources_unchanged': True,
        'review_body': binding(PART/'review_f32_body.txt'),
        'sealer': binding(Path(__file__).resolve()),
        'report': binding(report_path),
    }
    json_path.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': result['status'], 'manifest_entries': 59,
                      'prior_routes': 277, 'report': binding(report_path),
                      'metadata': binding(json_path)}, indent=2))


if __name__ == '__main__':
    main()
