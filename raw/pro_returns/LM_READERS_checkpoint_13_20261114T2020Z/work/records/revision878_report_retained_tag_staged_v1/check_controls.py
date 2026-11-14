#!/usr/bin/env python3
"""Bounded reporter-branch controls; never run a full report or alter evidence."""
from __future__ import annotations

import argparse
import ast
import copy
import hashlib
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True


def digest(data):
    return hashlib.sha256(data).hexdigest()


def reference(path, root):
    raw = path.read_bytes()
    return {'path': path.resolve().relative_to(root).as_posix(),
            'bytes': len(raw), 'sha256': digest(raw)}


def verify_reference(ref, root):
    actual = reference(root / ref['path'], root)
    assert actual == ref, 'Pinned control input changed: ' + ref['path']


def observation_loop(path):
    tree = ast.parse(path.read_bytes())
    functions = [node for node in tree.body if isinstance(node, ast.FunctionDef)
                 and node.name == 'assess_pagination']
    assert len(functions) == 1
    expected = ast.dump(ast.parse('known+candidates', mode='eval').body,
                        include_attributes=False)
    loops = [node for node in functions[0].body if isinstance(node, ast.For)
             and ast.dump(node.iter, include_attributes=False) == expected]
    assert len(loops) == 1, 'Exact reporter observation loop is not unique'
    loop = copy.deepcopy(loops[0])
    module = ast.fix_missing_locations(ast.Module(body=[loop], type_ignores=[]))
    return compile(module, path.name, 'exec'), digest(
        ast.dump(loop, include_attributes=False).encode())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', type=Path, required=True)
    parser.add_argument('--stage', type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    root = args.root.resolve()
    stage = args.stage.resolve()
    assert not args.output.exists(), 'Control output must be a new file'
    inputs = json.loads((stage / 'INPUTS.json').read_text())
    change = json.loads((stage / 'CHANGE.json').read_text())
    fixtures = json.loads((stage / 'ACTUAL_FIXTURES.json').read_text())
    input_refs = [value for value in inputs.values()
                  if isinstance(value, dict) and 'path' in value]
    input_refs += inputs['sources'] + inputs['images']
    input_refs += [change['before'], change['proposed']]
    for ref in input_refs:
        verify_reference(ref, root)
    for name in ('INPUTS.json', 'CHANGE.json', 'STATIC_CHECKS.json',
                 'ACTUAL_FIXTURES.json', 'check_controls.py'):
        input_refs.append(reference(stage / name, root))
    before = (root / change['before']['path']).read_bytes()
    proposed = (root / change['proposed']['path']).read_bytes()
    assert before.count(change['old_literal'].encode()) == 1
    assert proposed == before.replace(change['old_literal'].encode(),
                                     change['new_literal'].encode(), 1)
    assert proposed.replace(change['new_literal'].encode(),
                            change['old_literal'].encode(), 1) == before

    audit = json.loads((root / fixtures['source_audit']['path']).read_text())
    rows = {}
    for fixture in fixtures['rows']:
        bucket, index = fixture['source_json_pointer'].strip('/').split('/')
        assert audit[bucket][int(index)] == fixture['row']
        row = fixture['row']
        rows[row['final_observation']['classification']] = row
    before_class = 'RETAINED_TAG_BEFORE_FULLY_CANCELLED_DISPLAY'
    after_class = 'RETAINED_TAG_AFTER_FULLY_CANCELLED_DISPLAY'
    assert set(rows) == {before_class, after_class}
    leading, trailing = rows[before_class], rows[after_class]

    sys.path.insert(0, str(root / 'work/scripts'))
    import verify_pagination_final as canonical
    from verify_pdf import sha256
    assert canonical.ROOT.resolve() == root
    original_code, original_ast = observation_loop(root / change['before']['path'])
    proposed_code, proposed_ast = observation_loop(root / change['proposed']['path'])
    checks = []

    def run(name, row, expected_prefix=None, code=proposed_code,
            expected_guard_calls=None, actual_fixture=False):
        failures, calls = [], []

        def guarded(item, observation):
            errors = canonical.retained_tag_source_errors(item, observation)
            calls.append({'classification': observation.get('classification'),
                          'errors': errors})
            return errors

        namespace = {'known': [], 'candidates': [copy.deepcopy(row)],
                     'failures': failures, 'ROOT': root, 'sha256': sha256,
                     'retained_tag_source_errors': guarded}
        exec(code, namespace)
        if expected_prefix is None:
            assert failures == [], name + ': unexpected rejection'
        else:
            assert len(failures) == 1 and failures[0].startswith(expected_prefix), (
                name + ': expected exact rejection category')
        if expected_guard_calls is not None:
            assert len(calls) == expected_guard_calls, name + ': source guard calls differ'
        checks.append({'name': name, 'status': 'PASS', 'fixture_id': row['id'],
                       'fixture_is_unchanged_actual_audit_row': actual_fixture,
                       'reporter': 'before' if code is original_code else 'proposed',
                       'expected_acceptance': expected_prefix is None,
                       'failures': failures, 'source_guard_calls': calls})

    def edited(row, edit):
        result = copy.deepcopy(row)
        edit(result, result['final_observation'])
        return result

    detached = 'Final equation number and complete display are not together: '
    source_error = 'Retained empty equation tag lacks exact source justification: '
    run('before_reporter_reproduces_actual_BEFORE_rejection', leading, detached,
        original_code, 0, True)
    run('before_reporter_accepts_actual_AFTER', trailing, code=original_code,
        expected_guard_calls=1, actual_fixture=True)
    run('proposed_accepts_actual_BEFORE_with_exact_source_guard', leading,
        expected_guard_calls=1, actual_fixture=True)
    run('proposed_accepts_actual_AFTER_with_exact_source_guard', trailing,
        expected_guard_calls=1, actual_fixture=True)
    run('BEFORE_source_rejects_AFTER_classification', edited(
        leading, lambda r, o: o.update(classification=after_class)), source_error,
        expected_guard_calls=1)
    run('AFTER_source_rejects_BEFORE_classification', edited(
        trailing, lambda r, o: o.update(classification=before_class)), source_error,
        expected_guard_calls=1)
    run('unknown_classification_cannot_admit_empty_display', edited(
        leading, lambda r, o: o.update(classification='RETAINED_TAG_UNQUALIFIED')),
        detached, expected_guard_calls=0)
    run('missing_classification_cannot_admit_empty_display', edited(
        leading, lambda r, o: o.pop('classification')), detached, expected_guard_calls=0)
    run('changed_source_file_hash_rejected', edited(
        leading, lambda r, o: o['source_assessment'].update(sha256='0' * 64)),
        source_error, expected_guard_calls=1)

    def change_fragment(r, o):
        assessment = o['source_assessment']
        assessment['fragment'] = assessment['fragment'].replace('(51)', '(52)', 1)
        assessment['fragment_sha256'] = digest(assessment['fragment'].encode())

    run('changed_source_fragment_even_with_rehashed_fragment_rejected',
        edited(leading, change_fragment), source_error, expected_guard_calls=1)
    run('changed_fragment_hash_rejected', edited(
        trailing, lambda r, o: o['source_assessment'].update(fragment_sha256='0' * 64)),
        source_error, expected_guard_calls=1)
    run('missing_source_assessment_rejected', edited(
        leading, lambda r, o: o.pop('source_assessment')), source_error,
        expected_guard_calls=1)
    run('different_candidate_tag_rejected', edited(
        leading, lambda r, o: r.update(tag='(52)')), source_error,
        expected_guard_calls=1)
    for label, row in [('BEFORE', leading), ('AFTER', trailing)]:
        run(label + '_retained_class_requires_exact_empty_display_list', edited(
            row, lambda r, o: o.update(display_pages=[o['tag_page']])),
            source_error, expected_guard_calls=0)

    def ordinary(r, o):
        o.pop('classification')
        o.pop('source_assessment')

    ordinary_row = edited(trailing, ordinary)
    run('ordinary_empty_display_still_rejected', ordinary_row, detached,
        expected_guard_calls=0)
    run('ordinary_same_page_display_still_accepted', edited(
        ordinary_row, lambda r, o: o.update(display_pages=[o['tag_page']])),
        expected_guard_calls=0)
    run('ordinary_detached_display_still_rejected', edited(
        ordinary_row, lambda r, o: o.update(display_pages=[o['tag_page'] + 1])),
        detached, expected_guard_calls=0)
    run('changed_image_hash_still_rejected', edited(
        leading, lambda r, o: o['images'][0].update(sha256='0' * 64)),
        'Final pagination image changed: ', expected_guard_calls=1)
    run('changed_observation_PDF_hash_still_rejected', edited(
        leading, lambda r, o: o.update(pdf_sha256='0' * 64)),
        'Final pagination image observation is incomplete: ', expected_guard_calls=1)
    assert len(checks) == 20
    for ref in input_refs:
        verify_reference(ref, root)
    report = {'schema': 'revision878-retained-tag-reporter-controls-v1',
              'status': 'PASS', 'control_count': len(checks), 'checks': checks,
              'checked_files': input_refs,
              'before_observation_loop_ast_sha256': original_ast,
              'proposed_observation_loop_ast_sha256': proposed_ast,
              'execution_scope': 'Only the exact observation loop extracted from assess_pagination, with the installed unchanged canonical retained_tag_source_errors and ordinary image hasher.',
              'full_report_or_gate_executed': False, 'PDF_bytes_read': False,
              'source_image_or_observation_modified': False,
              'new_visual_review_claims': False, 'inputs_stable': True}
    with args.output.open('x') as stream:
        stream.write(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'status': 'PASS', 'controls': len(checks),
                      'report': reference(args.output.resolve(), root)}, indent=2))


if __name__ == '__main__':
    main()
