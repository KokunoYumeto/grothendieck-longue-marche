#!/usr/bin/env python3
"""Check only the staged metadata guards; never execute measurement main()."""
from pathlib import Path
import ast
import copy
import hashlib
import importlib.util
import json

ROOT = Path.cwd().resolve()
STAGE = Path(__file__).resolve().parent
SCRIPT = STAGE / 'measure_pdf_delta_plan.py'


def pin(path):
    content = path.read_bytes()
    return {'path': path.relative_to(ROOT).as_posix(), 'bytes': len(content),
            'sha256': hashlib.sha256(content).hexdigest()}


def main():
    require_stage = ROOT / 'work/records/revision878_pdf_delta_plan_staged_v1'
    assert STAGE == require_stage
    checks = []

    def passed(name):
        checks.append({'test': name, 'status': 'PASS'})

    def rejected(name, fn):
        try:
            fn()
        except ValueError:
            passed(name)
        else:
            raise AssertionError(name)

    source = SCRIPT.read_text()
    tree = ast.parse(source)
    compile(tree, 'staged-measurement-module', 'exec')
    spec = importlib.util.spec_from_file_location('staged878_metadata_contract', SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    passed('Staged script parses and imports definitions without invoking main or reading PDFs')
    lineage_path = STAGE / 'LINEAGE.json'
    assert pin(lineage_path)['sha256'] == module.LINEAGE_SHA256
    lineage = json.loads(lineage_path.read_text())
    snapshot_ref = lineage['revision872_snapshot']
    assert pin(ROOT / snapshot_ref['path']) == snapshot_ref
    snapshot = json.loads((ROOT / snapshot_ref['path']).read_text())
    for artifact in lineage['artifacts']:
        original = ROOT / artifact['original']['path']
        saved = STAGE / artifact['preserved']['path']
        assert pin(original) == artifact['original']
        assert original.read_bytes() == saved.read_bytes()
        rows = [row for row in snapshot['files'] if row['original_path'] == artifact['original']['path']]
        assert len(rows) == 1
        row = rows[0]
        assert row['stored_identity_mode'] == 'EXACT_BYTES'
        assert row['sha256'] == row['snapshot_sha256'] == artifact['original']['sha256']
        assert row['bytes'] == row['snapshot_bytes'] == artifact['original']['bytes']
        assert (ROOT / row['snapshot_path']).read_bytes() == original.read_bytes()
    passed('All eight immutable lineage files and captured metadata copies match exact snapshot authority')
    stable = {'source_records': 878, 'status': 'SEVEN_BOOK_TWO_PASS_BUILD_STABLE_REVISION878',
              'all_frozen_dependencies_rehashed': True}
    module.validate_stable(stable)
    passed('Exact878 stable metadata is admitted by the pure guard')
    for field, value in [('source_records', 872), ('status', 'BUILD_RUNNING'),
                         ('all_frozen_dependencies_rehashed', False)]:
        bad = dict(stable, **{field: value})
        rejected('Stable guard rejects ' + field + ' mismatch', lambda bad=bad: module.validate_stable(bad))
    build = {'status': 'TWO_PASS_BUILD_COMPLETE_INPUTS_UNCHANGED', 'source_records': 878,
             'books': 7, 'compile_passes': 2, 'return_code': 0, 'changed_inputs': []}
    module.validate_build(build)
    passed('Exact completed878 two-pass build metadata is admitted by the pure guard')
    for field, value in [('source_records', 872), ('status', 'RUNNING'), ('compile_passes', 1),
                         ('return_code', 1), ('changed_inputs', ['synthetic_changed_input'])]:
        bad = dict(build, **{field: value})
        rejected('Build guard rejects ' + field + ' mismatch', lambda bad=bad: module.validate_build(bad))
    old_stable = json.loads((STAGE / 'lineage/revision872_STABLE_BUILD.json').read_text())
    books = {row['book'] for row in old_stable['books']}

    def family(revision):
        return {book: {'reader': book, 'sha256': hashlib.sha256((str(revision) + book).encode()).hexdigest(),
                       'bytes': 1000 + revision} for book in books}

    old = {revision: family(revision) for revision in (724, 864, 872)}
    current = family(878)
    targets = module.current_base_targets(old, current, books)
    assert len(targets) == 23
    assert {row['base']['sha256'] for row in targets} == {
        pin['sha256'] for book, pin in current.items() if book not in module.MASTERS}
    assert {row['target']['sha256'] for row in targets} == {
        pin['sha256'] for generation in old.values() for pin in generation.values()} | {
        current[book]['sha256'] for book in module.MASTERS}
    assert all(row['base']['reader'] == module.MASTERS.get(row['target']['reader'], row['target']['reader'])
               for row in targets)
    passed('Synthetic metadata gives exactly28 identities,23 targets and five current full primary bases')
    bad = copy.deepcopy(old); bad[872].pop(next(iter(books)))
    rejected('Incomplete historical book generation is rejected', lambda: module.current_base_targets(bad, current, books))
    bad = copy.deepcopy(old); bad[873] = bad.pop(872)
    rejected('A substituted historical revision is rejected', lambda: module.current_base_targets(bad, current, books))
    bad = copy.deepcopy(old); book = sorted(books)[0]; bad[872][book]['sha256'] = current[book]['sha256']
    rejected('Duplicate old/current identity and base-target overlap are rejected', lambda: module.current_base_targets(bad, current, books))
    bad = copy.deepcopy(old); book = sorted(books)[0]; bad[724][book]['reader'] = sorted(books)[1]
    rejected('A pin labelled as another reader is rejected', lambda: module.current_base_targets(bad, current, books))
    main_node = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == 'main')
    main_text = ast.get_source_segment(source, main_node)
    assert main_text.index('validate_stable(stable)') < main_text.index('validate_build(build)') < main_text.index("import restore_checkpoint") < main_text.index("pdf = read('work/build/")
    assert 'recipe_bytes' not in main_text and 'get_pixmap' not in main_text and 'final_maps(' not in main_text
    passed('Actual878 stable/build/helper admission precedes current PDF reads; no renderer or final-map collection is invoked')
    output = {'schema': 'revision878-measurement-static-contract-v1',
              'status': 'PASS_STATIC_METADATA_CONTRACT_ONLY_AWAIT_STABLE878',
              'script': pin(SCRIPT), 'control_script': pin(Path(__file__)), 'lineage': pin(lineage_path),
              'passed': len(checks), 'failed': 0, 'checks': checks,
              'actual_metadata_only_snapshot_rows_checked': len(lineage['artifacts']),
              'actual_current_or_historical_PDFs_read': 0,
              'measurement_main_called': False, 'delta_generator_or_decoder_called': False,
              'production_plan_created': False, 'render_collection_or_restore_executed': False,
              'new_visual_review_claims': False}
    destination = STAGE / 'STATIC_CHECKS.json'
    with destination.open('x') as stream:
        json.dump(output, stream, ensure_ascii=False, indent=2); stream.write('\n')
    print(json.dumps(pin(destination), indent=2))


if __name__ == '__main__':
    main()
