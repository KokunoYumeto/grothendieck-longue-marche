#!/usr/bin/env python3
"""Seal the independent F29 proof/code review against the frozen evidence."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[3]
STEM = 'work/part_a/f_four_parameter_product_one_images'
DEST = ROOT / 'work/part_c/review_f29.json'


def binding(path):
    path = ROOT / path if isinstance(path, str) else path
    content = path.read_bytes()
    return {'path': str(path.relative_to(ROOT)), 'bytes': len(content),
            'sha256': sha256(content).hexdigest()}


def main():
    assert not DEST.exists(), 'The sealed review must not be overwritten.'
    frozen = {
        STEM + '.tex': '8aa897e0df17844ff6fb538be5770aaace072afa25d14a378cfc934e06d557cd',
        STEM + '_results.json': '04169bf3db2fca17bdbd7177726cc6bf7cacd1b2664b393f062e6c133911b3d2',
        STEM + '_report.txt': 'e181ae7861f84d0d06594e57b349a3f22959cc94ba8b54c6ba9074cc2c4de231',
        STEM + '_evidence_manifest.json': 'aef9ee3a646f1e65e448864f81b3586a9394149d807fcb4004e876d859d62734',
    }
    protected = {
        'work/part_c/c91.tex': '0b5db75c25411d069d4316995b410faab63b5c624bed7f4044a963e27d1952ff',
        'work/part_c/c92.tex': 'e978d4c54fa14090d67e1fd0620561bd251a8e3673132284aa144030b129ad7c',
        'work/part_c/compact_family_displacement_graph.tex': 'e3f724056664f2e1e2ae164b2e046b1dd8f5cd4495a66b45866b88191ef58338',
        'work/part_a/f_rank_one_marginal_obstruction.tex': '44e84bb754b46e288df19ec3d931ba16687ea2208422a096ea43d9a2db3a9d75',
        'work/part_a/f_affine_scalar_field_images.tex': 'd94af591f2cf567ae5f31286a7b0c694ef94bfddd12927a0f24cdbdc90e5a0ee',
        'work/part_a/f_trace_obstruction_and_f9_images.tex': '1db6b7ce7170a2da642989abe86198811e9e4dbb42288d67263dd823932e1449',
        'work/part_a/f_product_one_character_locus_images.tex': '91dbd2e919ebda809dcfaa61f05d2ee465ef67739252b34991fb29fc44c9d21f',
        'work/part_a/f_three_parameter_product_one_images.tex': 'b9e5941bddeb92cc831825c067bc1ff8c6e8b952f35eb608cf02c142dae26262',
    }
    for path, digest in (frozen | protected).items():
        assert binding(path)['sha256'] == digest, path
    manifest = json.loads((ROOT / (STEM + '_evidence_manifest.json')).read_text())
    assert len(manifest['entries']) == 63
    assert len({entry['path'] for entry in manifest['entries']}) == 63
    for expected in manifest['entries']:
        assert binding(expected['path']) == expected

    source = (ROOT / (STEM + '.tex')).read_text()
    lines = source.splitlines()
    assert len(lines) == 795
    tags = re.findall(r'\\tag\{(F\.29\.[0-9]+)\}', source)
    assert tags == ['F.29.' + str(j) for j in range(1, 34)]
    opens = sum(line.strip() == r'\[' for line in lines)
    closes = sum(line.strip() == r'\]' for line in lines)
    assert opens == closes == 33
    replay_folder = ROOT / 'work/part_c/f29_independent_replay'
    comparison = json.loads((replay_folder / 'comparison.json').read_text())
    assert comparison['status'] == 'PASS'
    assert comparison['main_verifier_check_total'] == 4242
    assert comparison['exceptional_explicit_assertions'] == 20
    assert comparison['all_63_manifest_bindings_unchanged']
    before = json.loads((replay_folder / 'manifest_validation_before.json').read_text())
    after = json.loads((replay_folder / 'manifest_validation_after.json').read_text())
    assert before == after
    assert before['entries'] == manifest['entries']
    assert comparison['exceptional_verifier']['raw_byte_identical']

    programs = [
        'work/part_a/code/affine_four_parameter_extension_independent_audit.py',
        'work/part_a/code/affine_four_parameter_r1_independent_audit.py',
        'work/part_a/code/affine_product_one_four_parameter_stage.py',
        'work/part_a/code/affine_product_one_deleted_first_stage.py',
        'work/part_a/code/affine_deleted_first_two_parameter_stage.py',
        'work/root/four_parameter_r1_exploration/independent_exceptional_words.py',
        'work/root/four_parameter_r1_exploration/verify_forced_lifts.py',
    ]
    criteria = [
        {'passage': 'F.29.1-4', 'finding': 'PASS', 'review': 'Exact negative and positive bases, actual scalar images and field recovery s=c/(rtu); all trivial-scalar, equal-field, u=1 and four remaining strata covered.'},
        {'passage': 'F.29.5-8', 'finding': 'PASS', 'review': 'Literal original-word coefficient maps; finite-affine universal property gives the continuous Z1 space; both principal-quotient composites and the cleared actual source action checked.'},
        {'passage': 'F.29.9', 'finding': 'PASS', 'review': 'Frobenius coefficient maps and inverse exponents explicitly preserve cocycles, principals, sources and restrictions; exact field-generation identities prove distinct conjugate pairs.'},
        {'passage': 'F.29.10-13', 'finding': 'PASS', 'review': 'Three-dimensional core inclusion, projection, section and basis inverse checked; full extension retained; all ten type pairs excluded by exact scalar actions and integral annihilators.'},
        {'passage': 'F.29.14-18', 'finding': 'PASS', 'review': 'r=1 core and four quotient maps checked; all fifteen type pairs covered, including the sole boundary/X1 coincidence c=u=-1 and both exact forced-lift residuals with nonzero second coordinate -2.'},
        {'passage': 'F.29.19-22', 'finding': 'PASS', 'review': 'c=1 ring map and its inverse fix actual generator labels; X4 pivot applied before localization; all fifteen type pairs checked without assuming t!=1.'},
        {'passage': 'F.29.23-26', 'finding': 'PASS', 'review': 'Essential-line basis maps and actual source-2 correction checked; printed five commutator rows compared with original words; determinant independently expanded, with every factor nonzero in all characteristics.'},
        {'passage': 'F.29.27-28', 'finding': 'PASS', 'review': 'Actual seed13 cross_0_-1_1, source2 and K membership retained; derivative difference and character-one recurrence give t^n(1-h) on actual K words.'},
        {'passage': 'F.29.29-32', 'finding': 'PASS', 'review': 'Minimal invariant kernel projections have the stated exact inverse intertwiners; actual character-one evaluations give the Vandermonde matrix and explicit Lagrange inverse.'},
        {'passage': 'F.29.3,33 and final transport', 'finding': 'PASS', 'review': 'Exact principal cocycle kernel, dimension/rank, trace-zero criterion, scalar-preserving F26 larger-field reduction and F23 based positive-sign subgroup maps all checked.'},
    ]
    charts = [
        {'locus': 'c!=1,r!=1', 'pivot': 7, 'types': ['W','boundary','X5','X6'],
         'unordered_pair_count_including_repeats': 10,
         'same_type_sources': {'W': [0,7], 'boundary': [7,2], 'X5': [0,7], 'X6': [0,7]},
         'mixed_pairs': {'W/boundary': 'source0: r versus1',
                         'W/X5': 'source9 cubic annihilator puts t in k1, then source0',
                         'W/X6': 'source8 cubic annihilator puts t in k1, then source0',
                         'boundary/X5': 'source0: 1 versus r',
                         'boundary/X6': 'source0: 1 versus r',
                         'X5/X6': 'source9: c versus1'}},
        {'locus': 'c!=1,r=1', 'pivot': 7, 'types': ['W','boundary','X1','X5','X6'],
         'unordered_pair_count_including_repeats': 15,
         'same_type_sources': 'source2/source7 pairs determine t',
         'mixed_pairs': {'W/boundary': 'sources2,7 force t^2=1',
                         'W/X1': 'sources2,7 force t^2=1',
                         'W/X5': 'source9 quadratic annihilator puts t in k1',
                         'W/X6': 'source8 quadratic annihilator puts t in k1',
                         'boundary/X1': 'sources1,5 force c=u=-1; actual forced-lift residual excludes both types',
                         'boundary/X5': 'sources2,7 force t^2=1',
                         'boundary/X6': 'sources2,7 force t^2=1',
                         'X1/X5': 'sources2,7 force t^2=1',
                         'X1/X6': 'sources2,7 force t^2=1',
                         'X5/X6': 'source9: c versus1'}},
        {'locus': 'c=1,r!=1', 'pivot': 4, 'types': ['W','boundary','X5','X6','X7'],
         'unordered_pair_count_including_repeats': 15,
         'same_type_sources': {'W': [0,7], 'boundary': [7,2], 'X5': [0,7], 'X6': [0,7], 'X7': [0,7]},
         'mixed_pairs': {'W/boundary': 'source0: r versus1',
                         'W/X5': 'source10 forces t=1, then source7 compares1,h',
                         'W/X6': 'source10: 1 versus h',
                         'W/X7': 'source8: 1 versus h',
                         'boundary/X5': 'source0: 1 versus r',
                         'boundary/X6': 'source0: 1 versus r',
                         'boundary/X7': 'source0: 1 versus r',
                         'X5/X6': 'source8 forces t=1, then source10 compares1,h',
                         'X5/X7': 'source8: 1 versus h',
                         'X6/X7': 'source10: h versus1'}},
        {'locus': 'c=1,r=1', 'pivot': 4, 'method': 'essential line and actual Vandermonde evaluation',
         'line_vector': ['0','1','-1/s','0','0','0'],
         'additive_commutator_anchor': 4, 'other_source_indices': [1,2,5,7,9],
         'determinant': '(s-1)^6*(t-1)^6*(t+1)/t^6',
         'chosen_seed': {'index': 13, 'label': 'cross_0_-1_1'},
         'evaluation_source': 2, 'line_evaluations': 't^n*(1-s*t)',
         'evaluation_matrix': '((1-h)*t_j^n)_(0<=n,j<m)',
         'evaluation_determinant': '(1-h)^m*product_(j<l)(t_l-t_j)',
         'explicit_inverse': 'z_j=(1-h)^-1*sum_n h_jn*y_n, where sum_n h_jn X^n=product_(l!=j)(X-t_l)/(t_j-t_l)'}
    ]
    producer_counts = []
    for name in ['affine_product_one_four_parameter_stage', 'affine_product_one_deleted_first_stage',
                 'affine_deleted_first_two_parameter_stage']:
        path = 'work/part_a/code/' + name + '_output.json'
        data = json.loads((ROOT / path).read_text())
        assert len(data['source_records']) == 11
        assert [entry['index'] for entry in data['source_records']] == list(range(11))
        assert sum(data['checks'].values()) == data['check_total']
        producer_counts.append({'output': binding(path), 'recorded_checks': data['check_total'],
                                'check_categories': data['checks'], 'source_record_count': 11})
    assert [entry['recorded_checks'] for entry in producer_counts] == [754,691,956]
    result = {
        'claim': 'F.29', 'reviewer': '/root/c89_review_and_general_c', 'status': 'PASS',
        'sealed_at_utc': datetime.now(timezone.utc).isoformat(),
        'review_report': binding('work/part_c/review_f29.txt'),
        'reviewed_frozen_artifacts': [binding(path) for path in frozen],
        'complete_proof_read': True, 'proof_lines': 795,
        'equation_tags': tags, 'balanced_standalone_display_pairs': 33,
        'programs_read_in_full': [{**binding(path), 'lines': len((ROOT/path).read_text().splitlines())}
                                  for path in programs],
        'earlier_arithmetic_dependency': {
            'program': binding('work/part_a/code/affine_product_one_three_parameter_independent_audit.py'),
            'prior_full_review': binding('work/part_c/review_f28.json')},
        'final_metadata_and_report_read_in_full': True,
        'root_replay_comparison_read_in_full': True,
        'manifest_entry_count_verified': 63,
        'manifest_entries_verified': manifest['entries'],
        'mathematical_criteria': criteria, 'four_actual_charts': charts,
        'all_chart_type_pairs_covered_in_both_orders': True,
        'reverse_order_map': 'Inverse of the explicit isomorphism between the two minimal invariant coordinate images',
        'actual_old_source_indices': list(range(11)),
        'actual_source_label_map': {'0': 'old0', **{str(j+1):'old_1_'+str(j) for j in range(5)},
                                   **{str(j+6):'old_-1_'+str(j) for j in range(5)}},
        'exceptional_stratum': {
            'equations': 'c=u=-1,r=1,s=t^-1; characteristic odd; k1=F_p; t outside F_p',
            'coefficient_map': 's^a*t^b*u^d -> (-1)^d*t^(b-a)',
            'pivot_delta7': '-2', 'source_indices': [1,2,7],
            'forced_boundary_lift': ['1-2*t','2','1','0','0','0'],
            'forced_X1_lift': ['-t','0','0','1','0','0'],
            'source1_residual_for_both': ['3*t-1','-2','0','0','0','0'],
            'explicit_assertions_replayed': 20, 'additional_internal_checks': 54},
        'producer_recorded_checks': producer_counts,
        'peer_isolated_replay': comparison,
        'peer_replay_artifacts': [binding(path) for path in sorted(replay_folder.rglob('*')) if path.is_file()],
        'peer_runner': binding('work/part_c/code/replay_f29_independent_audits.py'),
        'sealing_program': binding(Path(__file__).resolve()),
        'protected_bindings_checked_unchanged': [binding(path) for path in protected],
        'mathematical_corrections_requested': [], 'source_files_edited': [],
        'symbolic_producers_rerun': False, 'universal_f24_certificate_rerun': False,
        'pdf_review_performed_for_f29': False,
        'scope': 'Independent full proof, code and exact evidence review for the four-parameter finite-affine image statement, summed H1 injection and exact principal kernel/rank on the stated character locus, including original positive-sign transport and arbitrary larger finite coefficient fields. No full marginal equality or original K+=D+ claim is certified.'
    }
    DEST.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'status': 'PASS', 'report': binding('work/part_c/review_f29.txt'),
                      'metadata': binding(DEST)}, indent=2))


if __name__ == '__main__':
    main()
