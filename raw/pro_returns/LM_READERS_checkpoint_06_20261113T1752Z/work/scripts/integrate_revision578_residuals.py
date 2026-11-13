#!/usr/bin/env python3
"""Stage or install the three source-qualified residual pagination repairs.

The two paired source edits only wrap unchanged spans in samepage. The third
change reserves the existing tall first source mark before one generated title.
Immutable manuscript and translation inputs are never written.
"""
from pathlib import Path
from collections import Counter
import argparse
import hashlib
import importlib
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / 'work/data'
PROBES = ROOT / 'work/layout_probes'
sys.path.insert(0, str(ROOT / 'work/scripts'))
import build_readers
import layout_repairs
from integrate_layout_pending import normalize


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def write(path, data):
    Path(path).write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')


def prepare():
    freeze = read(DATA / 'layout_release_checkpoint.json')
    assert freeze['records'] == 578, 'Require the explicit revision578 base.'
    for path, digest in freeze['sha256'].items():
        assert sha(ROOT / path) == digest, path
    manifest_path = DATA / 'layout_residual_batch_revision578.json'
    manifest = read(manifest_path)
    for item in manifest['items']:
        for field in ('candidate', 'validation'):
            assert sha(ROOT / item[field]) == item[field + '_sha256'], item[field]
        assert read(ROOT / item['validation'])['status'] == 'PASS', item['name']
    existing = read(DATA / 'layout_pagination_additions.json')
    old_keys = {(r['id'], r['language']) for r in existing}
    extras = []
    for item in manifest['items']:
        if item['stage'] != 'pagination':
            continue
        for raw in read(ROOT / item['candidate']):
            for pair in raw.get('variants', [raw]):
                assert pair['new'] == '\\begin{samepage}\n' + pair['old'] + '\n\\end{samepage}'
            source = ROOT / 'sources' / raw['source_path'].removeprefix('sources/')
            assert sha(source) == raw['source_sha256']
            original = source.read_bytes()
            a, b = raw['source_byte_start'], raw['source_byte_end']
            assert original[a:b].decode() == raw['source_old']
            row = normalize(raw, item['name'], 'pagination')
            assert (row['id'], row['language']) not in old_keys
            extras.append(row)
    assert len(extras) == 4
    assert Counter(r['language'] for r in extras) == {'fr': 2, 'en': 2}
    assert len({(r['id'], r['language']) for r in extras}) == 4
    staged = {'work/data/layout_pagination_additions.json':
              json.dumps(existing + extras, ensure_ascii=False, indent=2) + '\n'}
    replacements = read(PROBES / 'range134_generator_replacements.json')
    assert sha(PROBES / 'range134_generator_replacements.json') == manifest['generator_replacements_sha256']
    assert replacements['unchanged_other_package_prefixes'] == 115
    for change in replacements['replacements']:
        path = ROOT / change['path']
        assert sha(path) == change['source_sha256'], change['path']
        text = path.read_text()
        assert text.count(change['old']) == change['expected_match_count'] == 1
        revised = text.replace(change['old'], change['new'])
        assert hashlib.sha256(revised.encode()).hexdigest() == change['after_sha256']
        compile(revised, change['path'], 'exec')
        staged[change['path']] = revised
    directory = PROBES / 'revision578_residual_staged'
    directory.mkdir(exist_ok=True)
    files = []
    for dest, text in staged.items():
        path = directory / Path(dest).name
        path.write_text(text)
        files.append(dict(destination=dest, staged=path.relative_to(ROOT).as_posix(), sha256=sha(path)))
    proposal = dict(status='STAGED_EXACT_REPLAY_READY', base_records=578,
                    additions=4, expected_records=582, generated_package_exceptions=1,
                    source_readings_changed=False, files=files,
                    manifest=manifest_path.relative_to(ROOT).as_posix(),
                    manifest_sha256=sha(manifest_path))
    write(directory / 'proposal.json', proposal)
    print(json.dumps({k: proposal[k] for k in ('status', 'base_records', 'additions', 'expected_records')}, ensure_ascii=False), flush=True)
    return staged, proposal


def run(path, *args):
    subprocess.run([sys.executable, str(ROOT / path), *args], cwd=ROOT, check=True)


def commit(staged, proposal):
    snapshot = DATA / 'audit_history/revision578/SNAPSHOT_COMPLETE.json'
    assert snapshot.exists(), 'Preserve completed revision578 observations before source integration.'
    backup = PROBES / 'revision578_dependency_backup'
    backup.mkdir(exist_ok=False)
    freeze = read(DATA / 'layout_release_checkpoint.json')
    build = read(DATA / 'final_build_inputs.json')
    files = set(staged) | set(freeze['sha256']) | set(build['assembly_dependencies']) | {
        'work/data/layout_release_checkpoint.json', 'work/data/final_build_inputs.json',
        'work/data/layout_repairs_applied.json', 'work/data/layout_exact_patches.json',
        'work/data/layout_semantic_command_audit.json', 'work/data/layout_probe_validation.json',
    }
    saved = []
    for name in sorted(files):
        source = ROOT / name
        target = backup / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(source.read_bytes())
        saved.append(dict(path=name, preserved_as=target.relative_to(ROOT).as_posix(), sha256=sha(source)))
    write(backup / 'MANIFEST.json', saved)
    for name, text in staged.items():
        (ROOT / name).write_text(text)
    importlib.reload(build_readers)
    importlib.reload(layout_repairs)
    counts = Counter()
    for lang in ('fr', 'en'):
        for package in layout_repairs.COVERAGE:
            _, records = layout_repairs.repair(build_readers.raw_package(package, lang), package, lang, include_pagination=False)
            for row in records:
                if row['kind'] not in ('empty diagram cell', 'manuscript-page placement', 'paired marginal notes'):
                    counts[lang, package, row['scan']] += 1
    def expected():
        return [dict(language=lang, package=package, scan=scan, expected_changes=n)
                for (lang, package, scan), n in sorted(counts.items())]
    assert read(DATA / 'layout_geometry_expected_matches.json') == expected()
    run('work/layout_probes/inventory_tag_patterns.py')
    run('work/layout_probes/finalize_tag_bindings.py', '--commit')
    bindings = read(DATA / 'layout_tag_bindings.json')
    assert len(bindings) == 268
    for row in bindings:
        counts[row['language'], row['package'], row['scan']] += 1
    write(DATA / 'layout_expected_matches.json', expected())
    for script in ('layout_repairs.py', 'write_layout_exact_manifest.py',
                   'audit_layout_repair_integrity.py', 'reconcile_pagination_repairs.py'):
        run('work/scripts/' + script)
    actual = read(DATA / 'layout_repairs_applied.json')
    assert len(actual) == 582
    assert Counter(r['language'] for r in actual) == {'fr': 291, 'en': 291}
    proposal.update(status='INTEGRATED_EXACT_SOURCE_AUDITS_PASS_AWAIT_FROZEN_BUILD',
                    actual_records=len(actual), snapshot_sha256=sha(snapshot),
                    backup_manifest=(backup / 'MANIFEST.json').relative_to(ROOT).as_posix(),
                    backup_manifest_sha256=sha(backup / 'MANIFEST.json'))
    write(DATA / 'layout_residual_revision578_integration_result.json', proposal)
    print(proposal['status'], len(actual), flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--commit', action='store_true')
    args = parser.parse_args()
    staged, proposal = prepare()
    if args.commit:
        commit(staged, proposal)
