#!/usr/bin/env python3
"""Install the additive eight source records and separate generated range guard.

Preparation writes only an immutable proposal. Installation requires the complete
revision864 discovery snapshot, saved checkpoint11 and independent full recovery.
The old source finalizer and old stress proofs are never regenerated here.
"""
from __future__ import annotations

import argparse
import collections
import copy
import csv
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import types
import zipfile

import compiler_output_privacy as compiler
from prepare_revision864_residual_manifest import require_manifest_evidence

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = 'work/data/layout_residual_batch_revision864.json'
STAGE = 'work/layout_probes/revision864_residual_staged_v3'
ADAPTER = 'work/layout_probes/snapshot_revision864_discovery_staged_v1/snapshot_revision864_discovery.py'
RESULT = 'work/data/layout_residual_revision864_integration_result.json'
BASELINE = 'work/layout_probes/revision864_baseline_v2/MANIFEST.json'
SOURCE_TARGETS = {
    'predicted_bindings': 'work/data/layout_tag_bindings.json',
    'predicted_additions': 'work/data/layout_pagination_additions.json',
    'predicted_expected_matches': 'work/data/layout_expected_matches.json',
}
AUDIT_SCRIPTS = ('layout_repairs.py', 'write_layout_exact_manifest.py',
                 'audit_layout_repair_integrity.py', 'reconcile_pagination_repairs.py')
CHECKPOINT_BOOKKEEPING = {'work/records/CHECKPOINT_STATUS.json',
                         'work/records/checkpoint_archives.jsonl', 'work/records/CHECKPOINT_SAVES.tsv'}


def read(path):
    return json.loads(Path(path).read_text())


def digest(path):
    with Path(path).open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def local(name):
    path = (ROOT / name).resolve()
    path.relative_to(ROOT)
    return path


def pin(path):
    path = Path(path).resolve()
    return dict(path=path.relative_to(ROOT).as_posix(), sha256=digest(path), bytes=path.stat().st_size)


def check(ref):
    actual = pin(local(ref['path']))
    assert actual['sha256'] == ref['sha256'], ref['path']
    if 'bytes' in ref:
        assert actual['bytes'] == ref['bytes'], ref['path']
    return actual


def write_new(path, value):
    with Path(path).open('x') as stream:
        json.dump(value, stream, ensure_ascii=False, indent=2)
        stream.write('\n')


def conserved(old, new, count):
    key = lambda row: (row['id'], row['language'])
    prior_keys = {key(row) for row in old}
    assert len(prior_keys) == len(old)
    assert len(new) == count and len({key(row) for row in new}) == count
    assert [row for row in new if key(row) in prior_keys] == old
    return [row for row in new if key(row) not in prior_keys]


def baseline_current(manifest):
    check(manifest['baseline_manifest'])
    baseline = read(local(manifest['baseline_manifest']['path']))
    refs = {row['original']['path']: row for row in baseline['files']}
    # The canonical observation validator had a separately reviewed source-only
    # scope extension after this baseline; it is not a build dependency.
    build = read(local('work/data/final_build_inputs.json'))
    assert build['source_records'] == 864 and build['changed_inputs'] == []
    names = set(build['source_dependencies']) | set(build['assembly_dependencies']) | {
        'work/data/layout_release_checkpoint.json', 'work/data/final_build_inputs.json',
        'work/data/layout_repairs_applied.json', 'work/data/layout_probe_validation.json'}
    for name in names:
        check(refs[name]['original'])
        check(refs[name]['preserved'])
    return refs


def prepare(stage):
    assert not stage.exists(), 'Preserve every existing proposal; use a new staging directory.'
    manifest = read(local(MANIFEST))
    require_manifest_evidence(manifest, ROOT)
    refs = baseline_current(manifest)
    preflight = read(local(manifest['source_preflight']['path']))
    old_bindings = read(local(refs[SOURCE_TARGETS['predicted_bindings']]['preserved']['path']))
    old_applied = read(local(refs['work/data/layout_repairs_applied.json']['preserved']['path']))
    added = conserved(old_bindings, read(local(preflight['predicted_bindings']['path'])), 524)
    assert len(added) == 8
    assert len(conserved(old_applied, read(local(preflight['predicted_applied']['path'])), 872)) == 8
    assert collections.Counter(row['language'] for row in added) == {'fr': 4, 'en': 4}
    files = []
    for field, destination in SOURCE_TARGETS.items():
        check(preflight[field])
        files.append(dict(destination=destination, before=pin(local(destination)), staged=preflight[field]))
    delta = read(local(manifest['generated_guard']['generator_delta']['path']))
    for row in delta['files']:
        assert pin(local(row['destination'])) == row['before']
        check(row['proposed'])
        files.append(dict(destination=row['destination'], before=row['before'], staged=row['proposed'],
                          preserved_before=row['preserved_before']))
    assert len(files) == 6 and len({row['destination'] for row in files}) == 6
    helpers = [pin(Path(__file__)), pin(local(ADAPTER)),
               pin(local('work/scripts/prepare_revision864_residual_manifest.py'))]
    helpers += [pin(local('work/scripts/' + name)) for name in AUDIT_SCRIPTS]
    proposal = dict(schema='revision864-exact-additive-installation-proposal-v1',
        status='STAGED_EXACT_REPLAY_READY', base_records=864, additions=8, superseded_records=0,
        expected_records=872, expected_pagination_records=524, source_readings_changed=False,
        manifest=MANIFEST, manifest_sha256=digest(local(MANIFEST)),
        source_preflight=manifest['source_preflight'], baseline_manifest=manifest['baseline_manifest'],
        predicted_applied=manifest['predicted_applied'], files=files, helpers=helpers,
        generated_guard=manifest['generated_guard']['generator_delta'],
        added=[{key: row[key] for key in ('id', 'language', 'package', 'scan')} for row in added],
        required_checkpoint='LM_READERS_checkpoint_11.zip', prior_checkpoint='LM_READERS_checkpoint_10.zip',
        checkpoint_bookkeeping_current_updates=sorted(CHECKPOINT_BOOKKEEPING),
        publication_closure_claim=False)
    stage.mkdir(parents=True)
    write_new(stage / 'proposal.json', proposal)
    return proposal


def load_proposal(stage):
    proposal = read(stage / 'proposal.json')
    assert proposal['status'] == 'STAGED_EXACT_REPLAY_READY'
    assert proposal['checkpoint_bookkeeping_current_updates'] == sorted(CHECKPOINT_BOOKKEEPING)
    assert proposal['manifest_sha256'] == digest(local(MANIFEST))
    assert proposal['expected_records'] == 872 and proposal['expected_pagination_records'] == 524
    manifest = read(local(MANIFEST))
    require_manifest_evidence(manifest, ROOT)
    baseline_current(manifest)
    for row in proposal['files']:
        check(row['before'])
        check(row['staged'])
    for ref in proposal['helpers']:
        check(ref)
    return proposal


def checkpoint_gate(stage, proposal, snapshot, archive):
    assert archive.name == proposal['required_checkpoint']
    saved = read(local('work/records/checkpoint11_save_receipt.json'))
    recovered = read(local('work/data/checkpoint11_restore_validation.json'))
    archive_sha = digest(archive)
    assert saved['status'] == 'succeeded' and saved['local_metadata_applied'] is True
    assert saved['library_file_id'].startswith('libfile_') and saved['filename'] == archive.name
    assert saved['sha256'] == archive_sha and saved['bytes'] == archive.stat().st_size <= 536870912
    assert recovered['status'] == 'PASS' and not recovered['failures']
    assert recovered['archive_filename'] == archive.name and recovered['archive_sha256'] == archive_sha
    assert recovered['archive_bytes'] == archive.stat().st_size and recovered['unaccounted_prior_entries'] == 0
    assert recovered['prior_checkpoint'] == proposal['prior_checkpoint']
    assert recovered['all_logical_files_independently_rehashed'] is True
    assert recovered['prior_checkpoint_sha256'] == digest(ROOT / 'deliverables' / proposal['prior_checkpoint'])
    preserved = read(snapshot)
    assert preserved['status'] == 'COMPLETE_DISCOVERY_SNAPSHOT_NOT_RELEASE_APPROVAL' and preserved['revision'] == 864
    assert preserved['manifest_sha256'] == proposal['manifest_sha256']
    refs = {row['original_path']: row for row in preserved['files']}
    assert len(refs) == len(preserved['files'])
    snapshot_ref = pin(snapshot)
    spec = importlib.util.spec_from_file_location('snapshot_revision864_install_gate', local(ADAPTER))
    adapter = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(adapter)
    current_logs = adapter.verify_current_log_snapshot_rows(ROOT, snapshot_ref)
    assert current_logs['status'] == 'PASS' and current_logs['count'] == 7 and current_logs['current_source_verified']
    log_names = {row['record']['original_path'] for row in current_logs['rows']}
    context = compiler.load_context(ROOT, MANIFEST)
    assert preserved['compiler_output_privacy_projection'] == context.registry_ref
    required = set(require_manifest_evidence(read(local(MANIFEST)), ROOT))
    required.update(compiler.required_snapshot_files(context))
    required.update(ref['path'] for ref in proposal['helpers'])
    required.update(row['staged']['path'] for row in proposal['files'])
    required.update((MANIFEST, (stage / 'proposal.json').relative_to(ROOT).as_posix()))
    assert required <= set(refs), sorted(required - set(refs))
    assert not required & CHECKPOINT_BOOKKEEPING
    bookkeeping = []
    with zipfile.ZipFile(archive) as container:
        descriptor_bytes = container.read('COMPACT_CHECKPOINT.json')
        descriptor = json.loads(descriptor_bytes)
        assert descriptor['schema'] == 'lm-compact-checkpoint-v1'
        assert hashlib.sha256(descriptor_bytes).hexdigest() == recovered['compact_descriptor_sha256']
        raw = container.read('LOGICAL_MANIFEST.tsv')
        rows = list(csv.DictReader(io.StringIO(raw.decode()), delimiter='\t'))
        logical = {row['path']: row for row in rows}
        assert len(logical) == len(rows) == descriptor['logical_manifest']['count']
        assert len(rows) == recovered['logical_entries'] == recovered['verified_entries']
        assert hashlib.sha256(raw).hexdigest() == descriptor['logical_manifest']['sha256'] == recovered['logical_manifest_sha256']
        assert descriptor['source_checkpoint']['filename'] == proposal['prior_checkpoint']
        assert descriptor['source_checkpoint']['sha256'] == recovered['prior_checkpoint_sha256']
        assert logical[snapshot_ref['path']]['sha256'] == snapshot_ref['sha256']
        assert int(logical[snapshot_ref['path']]['bytes']) == snapshot_ref['bytes']
        for index, row in enumerate(preserved['files']):
            name = row['original_path']
            if name in CHECKPOINT_BOOKKEEPING:
                # These three ordinary records change when a checkpoint is
                # created or saved. Preserve and verify their actual captured
                # bytes; do not describe the later record as the old bytes.
                assert row['snapshot_sha256'] == row['sha256']
                assert row['snapshot_bytes'] == row['bytes']
                check(dict(path=row['snapshot_path'], sha256=row['snapshot_sha256'], bytes=row['snapshot_bytes']))
                bookkeeping.append(dict(original_at_snapshot=dict(path=name, sha256=row['sha256'], bytes=row['bytes']),
                    current=pin(local(name)), packaged_original=dict(path=name, sha256=logical[name]['sha256'], bytes=int(logical[name]['bytes'])),
                    preserved_copy=dict(path=row['snapshot_path'], sha256=row['snapshot_sha256'], bytes=row['snapshot_bytes']),
                    reason='Numbered checkpoint creation and durable-save bookkeeping; captured bytes preserved exactly.'))
                expected = None
            elif name not in log_names:
                compiler.verify_snapshot_record(ROOT, row, context, authorization=dict(
                    record=snapshot_ref, kind='discovery_snapshot', pointer='/files/' + str(index), target='snapshot_path'))
                expected = compiler.packaged_identity(ROOT, dict(path=name, sha256=row['sha256'], bytes=row['bytes']), context)
            else:
                expected = dict(sha256=row['snapshot_sha256'], bytes=row['snapshot_bytes'])
            if expected is not None:
                assert logical[name]['sha256'] == expected['sha256'] and int(logical[name]['bytes']) == expected['bytes'], name
            assert logical[row['snapshot_path']]['sha256'] == row['snapshot_sha256'], name
            assert int(logical[row['snapshot_path']]['bytes']) == row['snapshot_bytes'], name
        for row in preserved['pdfs']:
            assert digest(local(row['path'])) == row['sha256'] == logical[row['path']]['sha256']
        for row in preserved['images']:
            assert digest(local(row['preserved_path'])) == row['sha256'] == logical[row['preserved_path']]['sha256']
    return dict(status='PASS', checkpoint=pin(archive), snapshot=snapshot_ref,
                save_receipt=pin(local('work/records/checkpoint11_save_receipt.json')),
                full_recovery=pin(local('work/data/checkpoint11_restore_validation.json')),
                logical_entries=len(rows), snapshot_files=len(refs), current_log_verification=current_logs,
                checkpoint_bookkeeping_updates=bookkeeping,
                new_visual_review_claims=False)


def generated_check(stage):
    import build_readers
    manifest = read(local(MANIFEST))
    guard = manifest['generated_guard']
    candidate = read(local(guard['candidate']))
    delta = read(local(guard['generator_delta']['path']))
    files = []
    for row in delta['files']:
        assert digest(local(row['destination'])) == row['proposed']['sha256']
        files.append(dict(destination=row['destination'], before=row['preserved_before'], after=pin(local(row['destination']))))
    before = next(row for row in delta['files'] if row['destination'] == 'work/scripts/build_readers.py')
    old = types.ModuleType('revision864_prior_generator')
    old.__file__ = str(local(before['destination']))
    exec(compile(local(before['preserved_before']['path']).read_text(), old.__file__, 'exec'), old.__dict__)
    checks = []
    with tempfile.TemporaryDirectory(prefix='lm-generated-guard-') as directory:
        old.WORK = Path(directory) / 'old'
        build_readers.WORK = Path(directory) / 'current'
        for module in (old, build_readers):
            module.DATA = module.WORK / 'data'
            module.RECORDS = module.WORK / 'records'
        for folder in (old.WORK, build_readers.WORK):
            (folder / 'build').mkdir(parents=True)
        for language in ('fr', 'en'):
            previous = old.assemble_language(language, 'build', {'LM_C4-077-095'})
            current = build_readers.assemble_language(language, 'build', {'LM_C4-077-095'})
            prior_prefix, prefix = candidate['old_generated_prefix'], candidate['new_generated_prefix']
            assert previous[0].count(prior_prefix) == current[0].count(prefix) == 1
            assert current[0].replace(prefix, prior_prefix, 1) == previous[0]
            assert current[1:] == previous[1:]
            for form in (0, 1, 2):
                row = dict(language=language, form=form, package='LM_C4-077-095', status='PASS',
                           conditional_prefix=prefix, active=form < 2, exact_body_inverse=True,
                           variants_and_provenance_unchanged=True)
                if form == 2:
                    assert current[0].replace(prefix, '', 1) == previous[0].replace(prior_prefix, '', 1)
                    row['reading_unchanged'] = True
                checks.append(row)
    result = dict(status='PASS', stage='generated_range', generator_delta=guard['generator_delta'],
                  files=files, prefix_checks=checks, raw_source_record_additions=0,
                  observations_generated_by_script=False, publication_closure_claim=False)
    write_new(stage / 'GENERATED_INTEGRATION_CHECK.json', result)
    return result


def commit(stage, snapshot, archive):
    assert not local(RESULT).exists(), 'Integration result already exists.'
    proposal = load_proposal(stage)
    gate = checkpoint_gate(stage, proposal, snapshot, archive)
    backup = stage / 'before_installation'
    backup.mkdir(exist_ok=False)
    names = {row['destination'] for row in proposal['files']}
    names.update('work/data/' + name for name in ('layout_repairs_applied.json', 'layout_exact_patches.json',
        'layout_semantic_command_audit.json', 'layout_pagination_reconciliation.json'))
    names.add('work/records/LAYOUT_REPAIR_DETAILS.tsv')
    names.update(path.relative_to(ROOT).as_posix() for path in (ROOT / 'work/layout_repaired').rglob('*.tex'))
    backups = []
    for name in sorted(names):
        target = backup / name
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open('xb') as stream:
            stream.write(local(name).read_bytes())
        backups.append(dict(original=pin(local(name)), preserved=pin(target)))
    write_new(backup / 'MANIFEST.json', backups)
    write_new(stage / 'CHECKPOINT_GATE.json', gate)
    write_new(stage / 'INSTALLATION_STARTED.json', dict(status='INSTALLATION_STARTED', proposal=pin(stage / 'proposal.json')))
    for row in proposal['files']:
        check(row['before'])
        check(row['staged'])
        local(row['destination']).write_bytes(local(row['staged']['path']).read_bytes())
        assert digest(local(row['destination'])) == row['staged']['sha256']
    for name in AUDIT_SCRIPTS:
        subprocess.run([sys.executable, '-B', str(ROOT / 'work/scripts' / name)], cwd=ROOT, check=True)
    actual = read(local('work/data/layout_repairs_applied.json'))
    assert actual == read(local(proposal['predicted_applied']['path'])) and len(actual) == 872
    assert collections.Counter(row['language'] for row in actual) == {'fr': 436, 'en': 436}
    assert len(read(local('work/data/layout_tag_bindings.json'))) == 524
    baseline = read(local(BASELINE))
    allowed = {row['destination'] for row in proposal['files']} | {
        'work/data/layout_repairs_applied.json', 'work/data/layout_exact_patches.json',
        'work/data/layout_semantic_command_audit.json', 'work/data/layout_pagination_reconciliation.json',
        'work/scripts/verify_pagination_final.py'}
    for row in baseline['files']:
        if row['original']['path'] not in allowed:
            check(row['original'])
    subprocess.run([sys.executable, '-B', str(Path(__file__)), 'generated-check', '--stage', str(stage)], cwd=ROOT, check=True)
    result = copy.deepcopy(proposal)
    result.update(status='INTEGRATED_EXACT_SOURCE_AUDITS_PASS_AWAIT_FROZEN_BUILD', actual_records=872,
        snapshot=snapshot.relative_to(ROOT).as_posix(), snapshot_sha256=digest(snapshot),
        backup_manifest=pin(backup / 'MANIFEST.json'), checkpoint_gate=pin(stage / 'CHECKPOINT_GATE.json'),
        generated_guard=read(stage / 'GENERATED_INTEGRATION_CHECK.json'),
        installed_files=[pin(local(row['destination'])) for row in proposal['files']],
        source_audits=[pin(local('work/data/' + name)) for name in ('layout_repairs_applied.json',
            'layout_exact_patches.json', 'layout_semantic_command_audit.json', 'layout_pagination_reconciliation.json')])
    write_new(local(RESULT), result)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['prepare', 'check', 'checkpoint-check', 'commit', 'generated-check'])
    parser.add_argument('--stage', default=STAGE)
    parser.add_argument('--snapshot', default='work/data/audit_history/revision864_selected_discovery/SNAPSHOT_COMPLETE.json')
    parser.add_argument('--checkpoint', default='deliverables/LM_READERS_checkpoint_11.zip')
    args = parser.parse_args()
    stage = local(args.stage)
    if args.command == 'prepare':
        result = prepare(stage)
    elif args.command == 'check':
        result = load_proposal(stage)
    elif args.command == 'checkpoint-check':
        result = checkpoint_gate(stage, load_proposal(stage), local(args.snapshot), local(args.checkpoint))
    elif args.command == 'generated-check':
        result = generated_check(stage)
    else:
        result = commit(stage, local(args.snapshot), local(args.checkpoint))
    print(json.dumps({key: result[key] for key in ('status', 'base_records', 'expected_records', 'actual_records') if key in result}), flush=True)


if __name__ == '__main__':
    main()
