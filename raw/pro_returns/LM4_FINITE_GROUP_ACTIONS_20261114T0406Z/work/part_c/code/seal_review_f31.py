"""Bind the independent F.31 review to the author's announced final files."""
from pathlib import Path
from hashlib import sha256
import argparse
import json
import re

ROOT = Path(__file__).resolve().parents[3]
STEM = ROOT/'work/part_a/f_full_product_one_affine_images'
EXPECTED_PROOF = '909cb42466354ecebfede5b5d27077381d13e87f9261ea62180dc507cf91c345'
EXPECTED_CHECKER = 'ffa5e83b3f98750b5fa3621fb3c4799c28e1a6c99bcdfa3133adcb3f510e270d'
EXPECTED_OUTPUT = '1de63f7a2f40dc965623ed83272ca741b04e64c2455eff0539c39d53b4f6091f'
EXPECTED_REPLAY = 'e0040984113b7bc3bb0239ac03a9154fcfb992d57c617c06cce9c6ed06476665'


def binding(path):
    data = path.read_bytes()
    return {'path': str(path.relative_to(ROOT)), 'bytes': len(data),
            'sha256': sha256(data).hexdigest(), 'lines': len(data.splitlines())}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--metadata-sha256', required=True)
    parser.add_argument('--report-sha256', required=True)
    parser.add_argument('--manifest-sha256', required=True)
    args = parser.parse_args()
    primary = {
        'proof': Path(str(STEM)+'.tex'),
        'author_metadata': Path(str(STEM)+'_results.json'),
        'author_report': Path(str(STEM)+'_report.txt'),
        'evidence_manifest': Path(str(STEM)+'_evidence_manifest.json'),
        'checker': ROOT/'work/part_a/code/affine_full_product_one_independent_audit.py',
        'checker_output': ROOT/'work/part_a/code/affine_full_product_one_independent_audit_output.json',
        'checker_stdout': ROOT/'work/part_a/code/affine_full_product_one_independent_audit_stdout.txt',
        'peer_replay_comparison': ROOT/'work/part_c/f31_independent_replay/comparison.json',
        'peer_replay_runner': ROOT/'work/part_c/code/replay_f31.py',
        'review_body': ROOT/'work/part_c/f31_peer_review_body.txt',
        'review_sealer': Path(__file__).resolve()}
    expected = {'proof': EXPECTED_PROOF, 'author_metadata': args.metadata_sha256,
                'author_report': args.report_sha256, 'evidence_manifest': args.manifest_sha256,
                'checker': EXPECTED_CHECKER, 'checker_output': EXPECTED_OUTPUT,
                'peer_replay_comparison': EXPECTED_REPLAY}
    bindings = {name: binding(path) for name, path in primary.items()}
    for name, digest in expected.items():
        assert bindings[name]['sha256'] == digest, name
    manifest = json.loads(primary['evidence_manifest'].read_text())
    assert manifest['claim'] == 'F.31'
    checked = []
    seen = set()
    for entry in manifest['entries']:
        path = Path(entry['path'])
        if not path.is_absolute():
            path = ROOT/path
        relative = str(path.relative_to(ROOT))
        assert relative not in seen, relative
        seen.add(relative)
        observed = binding(path)
        assert observed['sha256'] == entry['sha256'], relative
        assert observed['bytes'] == entry['bytes'], relative
        checked.append({'declared': entry, 'observed': observed, 'exact_match': True})
    for name in ['proof', 'author_metadata', 'author_report', 'checker', 'checker_output']:
        assert bindings[name]['path'] in seen, name
    audit = json.loads(primary['checker_output'].read_text())
    replay = json.loads(primary['peer_replay_comparison'].read_text())
    assert audit['total_exact_checks'] == replay['total_exact_checks'] == 1603
    assert audit['check_total'] == 977 and audit['reviewed_word_and_parser_check_total'] == 626
    assert len(audit['inputs']) == replay['copied_input_count'] == 10
    assert replay['whole_output_bytes_equal_after_exact_key_transport']
    assert replay['all_original_files_unchanged_after_replay']
    for item in replay['input_bindings']:
        for key in ['source', 'isolated_copy']:
            bound = item[key]
            current = binding(ROOT/bound['path'])
            assert current['sha256'] == bound['sha256'] and current['bytes'] == bound['bytes']
    for key in ['checker_copy', 'isolated_output', 'transported_output', 'stdout', 'stderr']:
        bound = replay[key]
        current = binding(ROOT/bound['path'])
        assert current['sha256'] == bound['sha256'] and current['bytes'] == bound['bytes']
    proof_text = primary['proof'].read_text()
    proof_lines = proof_text.splitlines()
    assert len(proof_lines) == 885
    assert sum(line.strip() == r'\[' for line in proof_lines) == 30
    assert sum(line.strip() == r'\]' for line in proof_lines) == 30
    assert [int(x) for x in re.findall(r'\\tag\{F\.31\.(\d+)\}', proof_text)] == list(range(1,31))
    braid_path = ROOT/'work/part_a/code/full_cross_source_stage/marginal_braids.json'
    f23_manifest_path = ROOT/'work/part_a/f_source_sign_and_marginal_images_evidence_manifest.json'
    f23_manifest = json.loads(f23_manifest_path.read_text())
    f23_braid = next(item for item in f23_manifest['entries']
                    if Path(item['path']).resolve() == braid_path.resolve())
    assert f23_braid['sha256'] == binding(braid_path)['sha256']
    assert f23_braid['bytes'] == binding(braid_path)['bytes']
    old_words = [item for item in json.loads(braid_path.read_text())['records'] if item['index'] < 11]
    assert [item['index'] for item in old_words] == list(range(11))
    source_inventory = [{'index_zero_based': item['index'], 'label': item['label'],
                         'negative_braid_length': len(item['negative_braid'])} for item in old_words]
    report_path = ROOT/'work/part_c/review_f31.txt'
    record_path = ROOT/'work/part_c/review_f31.json'
    assert not report_path.exists() and not record_path.exists(), 'Do not overwrite sealed review.'
    appendix = ['\n17. FINAL EXACT BINDINGS AND MANIFEST ACCEPTANCE\n',
                f"Author manifest status: {manifest.get('status','not specified')}",
                f"All {len(checked)} manifest entries were independently checked for exact bytes and SHA256.",
                'No missing, duplicate, mismatched or changed binding was found.',
                'The final metadata and author report were read in full before this sealing.',
                'The author manifest remains unchanged; this peer record is separate and acyclic.', '']
    for name, item in bindings.items():
        appendix += [name+': '+item['path'],
                     f"  {item['bytes']} bytes; {item['lines']} lines; SHA256 {item['sha256']}"]
    appendix += ['', 'All ten unchanged replay inputs:']
    for item in replay['input_bindings']:
        bound = item['source']
        appendix += [bound['path'], f"  {bound['bytes']} bytes; SHA256 {bound['sha256']}"]
    appendix += ['', 'Final acceptance: PASS on the exact source, complete final manifest,',
                 'all mathematical dependency maps and the unchanged isolated 1603-check replay.',
                 'No frozen source or certificate was edited. No further mathematical repair is requested.', '']
    report_path.write_text(primary['review_body'].read_text()+'\n'.join(appendix))
    categories = [
        'actual marginal maps and normal generation',
        'C=1 and equal scalar-field cases',
        'exact Laurent coefficient homomorphisms',
        'original source preservation and index convention',
        'continuous seven-coordinate cocycles',
        'both principal quotient maps and inverse composites',
        'boundary and X1 quotient maps and all source characters',
        'eight generic moving-root identities and four determinants',
        'exact proper fixed field and every nonzero cancelled factor',
        'all three generic minimal-type comparisons',
        'four r=1 moving-root identities and unit determinant',
        'all six r=1 minimal-type comparisons',
        'all fifteen sign coefficient maps and unique necessary boundary lifts',
        'every residual nonvanishing including characteristic three',
        'minimal invariant kernel and explicit inverse intertwiners',
        'exact summed cocycle kernel and rank',
        'trace identity and arbitrary original coefficient-field reduction',
        'both continuous based sign maps and their inverses',
        'full checker/helper/four-producer code review',
        'unchanged isolated literal-word replay',
        'final metadata/report read and complete manifest binding']
    record = {
        'status': 'PASS_INDEPENDENT_F31_FULL_PROOF_CODE_EVIDENCE_AND_REPLAY_REVIEW',
        'claim': 'F.31', 'reviewer': 'Part C peer agent',
        'corrections_requested': [], 'mathematical_issues': [],
        'proof_full_read_lines': 885, 'checker_full_read_lines': 421,
        'helper_full_read_lines': 386, 'producer_full_read_lines': [156,106,128,138],
        'primary_bindings': bindings,
        'author_announced_final_hashes': expected,
        'evidence_manifest_entry_count': len(checked),
        'all_manifest_entries_exact': True, 'manifest_entry_checks': checked,
        'read_and_checked_categories': categories,
        'source_inventory': source_inventory,
        'f23_manifest': binding(f23_manifest_path), 'f23_original_braid_entry': f23_braid,
        'source_display_check': {'standalone_opens': 30, 'standalone_closes': 30,
                                 'tags': list(range(1,31)), 'balanced': True},
        'independent_replay': {'comparison': bindings['peer_replay_comparison'],
                               'exact_input_path_key_count': 10,
                               'checker_assertions': 977, 'word_parser_assertions': 626,
                               'total_exact_checks': 1603,
                               'whole_output_byte_equality_after_exact_key_bijection': True,
                               'stdout_byte_equality_after_one_consequent_hash_substitution': True,
                               'stderr_bytes': 0, 'exit_code': 0,
                               'literal_word_chart_evaluations': 22,
                               'moving_operator_count': 12, 'square_determinant_count': 5,
                               'sign_stratum_count': 15,
                               'all_frozen_inputs_unchanged': True},
        'full_huge_matrix_outputs_read_manually': False,
        'matrix_output_validation': 'Every used full action, quotient block, core, prescribed row, determinant, forced lift and residual is verified coefficientwise by the unchanged literal-word replay. Exploratory unused failed scalar tests are outside the proved identities.',
        'scope': 'Actual affine marginal image equality on the full stated product-one character locus for both explicit bases, summed H1 injection, exact principal-tuple kernel and rank 6m+1. No general-character affine equality or full marginal subgroup equality is certified.',
        'assembled_pdf_compilation_or_visual_review': False,
        'all_completed_earlier_sources_unchanged': True,
        'report': binding(report_path)}
    record_path.write_text(json.dumps(record, indent=2)+'\n')
    print(json.dumps({'status': record['status'], 'manifest_entry_count': len(checked),
                      'report': binding(report_path), 'record': binding(record_path)}, indent=2))


if __name__ == '__main__':
    main()
