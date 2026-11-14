#!/usr/bin/env python3
"""Bounded staged PDF-disposition checks, with live publication reads denied."""
from __future__ import annotations
import ast
import collections
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import types

STAGE = Path(__file__).resolve().parent
ROOT = STAGE.parents[2]
sys.path.insert(0, str(ROOT / 'work/scripts'))
READS = []
original_read_bytes = Path.read_bytes
original_read_text = Path.read_text


def denied(path):
    path = Path(path).resolve()
    if path.is_relative_to(ROOT):
        name = path.relative_to(ROOT).as_posix()
        if name.startswith('work/build/') and path.suffix.lower() == '.pdf':
            raise AssertionError('A live publication PDF read was attempted.')
        READS.append(name)


def read_bytes(path):
    denied(path)
    return original_read_bytes(path)


def read_text(path, *args, **kwargs):
    denied(path)
    return original_read_text(path, *args, **kwargs)


def pin(path):
    path = Path(path); data = path.read_bytes()
    return dict(path=path.relative_to(ROOT).as_posix(), bytes=len(data), sha256=hashlib.sha256(data).hexdigest())


def exact(ref):
    actual = pin(ROOT / ref['path'])
    assert all(actual[k] == ref[k] for k in ('bytes', 'sha256')), ref['path']


def read(path):
    return json.loads(Path(path).read_bytes())


def load(path):
    spec = importlib.util.spec_from_file_location('staged_publication_pdf_scope_878', path)
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    return module


def main():
    assert not (STAGE / 'CONTROLS.json').exists()
    Path.read_bytes, Path.read_text = read_bytes, read_text
    results = []

    def passed(name, **details):
        results.append(dict(control=name, status='PASS', **details))

    def reject(name, callback):
        try:
            callback()
        except (ValueError, KeyError, RuntimeError):
            passed(name, disposition='REJECTED_AS_REQUIRED')
        else:
            raise AssertionError('Negative control accepted: ' + name)

    try:
        change = read(STAGE / 'CHANGE.json')
        module = load(ROOT / change['proposed']['path'])
        before = read(STAGE / 'before/development_pdf_exclusions.json')
        proposed = read(STAGE / 'proposed/development_pdf_exclusions.json')
        additions = read(STAGE / 'ADDITIONS.json')
        qualification = read(STAGE / 'QUALIFICATION.json')
        baseline_bytes = (STAGE / 'before/development_pdf_exclusions.json').read_bytes()
        proposed_bytes = (STAGE / 'proposed/development_pdf_exclusions.json').read_bytes()
        prefix = baseline_bytes[:baseline_bytes.rfind(b'}')].rstrip(b' \t\r\n')
        assert len(before) == 894 and len(proposed) == 931 and len(additions) == 37
        assert list(proposed) == list(before) + list(additions)
        assert all(proposed[k] == v for k, v in before.items())
        assert proposed_bytes.startswith(prefix + b',')
        assert proposed == dict(before, **additions)
        passed('all894 prior objects, order and complete member text prefix remain exact')
        source = (STAGE / 'before/publication_pdf_scope.py').read_text()
        target = (STAGE / 'proposed/publication_pdf_scope.py').read_text()
        fragment = (STAGE / 'snapshot_publication_validator.py').read_text()
        branch = ("            elif q.get('kind') == 'immutable_snapshot_publication_pdf':\n"
                  "                validate_snapshot_publication_pdf(root, name, row, snapshot_cache)\n"
                  "                add(name, row['source_pdf_sha256'], row['source_pdf_bytes'], row['reader'], q, row['reason'])\n")
        assert target.count(fragment + '\n') == target.count(branch) == 1
        assert target.replace(fragment + '\n', '', 1).replace(branch, '', 1) == source
        def functions(text):
            return {n.name: ast.dump(n, include_attributes=False) for n in ast.parse(text).body if isinstance(n, (ast.FunctionDef, ast.ClassDef))}
        old_ast, new_ast = functions(source), functions(target)
        assert set(new_ast) - set(old_ast) == {'validate_snapshot_publication_pdf'}
        assert set(old_ast) - set(new_ast) == set()
        assert {k for k in old_ast if old_ast[k] != new_ast[k]} == {'registry'}
        passed('only new whole-book validator and one registry branch change; old validators and consumers exact')

        trial_rows = {n: r for n, r in additions.items() if r['source_scope_qualification']['kind'] == 'source_local_development_proof'}
        counts = collections.Counter(r['source_scope_qualification']['classification'] for r in trial_rows.values())
        assert counts == {'ACCEPTED_SOURCE_LOCAL_PROOF_COMPARISON': 18, 'REJECTED_SMALLER_SHIFT_TRIAL': 12}
        for name, row in trial_rows.items():
            q = row['source_scope_qualification']; exact(q['source_pdf']); exact(q['source_tex']); exact(q['portable_log']); exact(q['compile_validation'])
            compiled = read(ROOT / q['compile_validation']['path'])
            form = compiled['forms'][int(q['form_record_pointer'].split('/')[-1])]
            assert all(q[qk] == form[fk] for qk, fk in [('source_pdf', 'pdf'), ('source_tex', 'tex'), ('portable_log', 'log')])
            assert q['language'] == form['language'] and q['form'] == form['form']
            assert row['path'] == name == q['source_pdf']['path']
            assert (row['source_pdf_sha256'], row['source_pdf_bytes']) == (form['pdf']['sha256'], form['pdf']['bytes'])
            assert row['publication_closure_claim'] is False
            authority = q['authority']
            if q['classification'] == 'REJECTED_SMALLER_SHIFT_TRIAL':
                exact(authority['rejection']); rejected = read(ROOT / authority['rejection']['path'])
                assert rejected['status'] == 'REJECTED_VISUAL_CONTACT_REMAINS'
                assert rejected['observation'] == authority['original_rejection_observation']
            else:
                for key in ('validation', 'actual_observations', 'root_review'):
                    exact(authority[key])
                assert read(ROOT / authority['validation']['path'])['actual_after_forms'] == 6
        passed('all30 exact proof PDF/TeX/log/compile tuples and accepted-versus-rejected authorities are distinct and correct')

        books = {n: r for n, r in additions.items() if r['source_scope_qualification']['kind'] == 'immutable_snapshot_publication_pdf'}
        assert len(books) == 7 and {r['reader'] for r in books.values()} == set(module.BOOKS)
        cache = {}
        for name, row in books.items():
            module.validate_snapshot_publication_pdf(ROOT, name, row, cache)
        passed('all seven actual preserved872 PDF bytes join the exact snapshot reader/path/SHA/size rows')

        name, row = next(iter(books.items()))
        def mutated(label, action):
            value = copy.deepcopy(row); action(value)
            reject(label, lambda: module.validate_snapshot_publication_pdf(ROOT, name, value, {}))
        mutated('changed snapshot authority digest rejects', lambda r: r['source_scope_qualification']['snapshot'].update(sha256='0' * 64))
        mutated('changed snapshot authority byte count rejects', lambda r: r['source_scope_qualification']['snapshot'].update(bytes=r['source_scope_qualification']['snapshot']['bytes'] + 1))
        mutated('unsafe snapshot authority path rejects', lambda r: r['source_scope_qualification']['snapshot'].update(path='../SNAPSHOT_COMPLETE.json'))
        mutated('boolean snapshot row index rejects', lambda r: r['source_scope_qualification'].update(snapshot_pdf_index=True))
        mutated('out-of-range snapshot row index rejects', lambda r: r['source_scope_qualification'].update(snapshot_pdf_index=7))
        mutated('wrong exact snapshot record association rejects', lambda r: r['source_scope_qualification']['snapshot_pdf_record'].update(pages=1))
        mutated('wrong original whole-book path rejects', lambda r: r['source_scope_qualification'].update(original_path='work/build/LM_EN_reading.pdf'))
        mutated('changed preserved PDF digest rejects', lambda r: r.update(source_pdf_sha256='0' * 64))
        mutated('changed preserved PDF size rejects', lambda r: r.update(source_pdf_bytes=r['source_pdf_bytes'] + 1))
        mutated('wrong named replacement reader rejects', lambda r: r.update(reader='LM_EN_reading'))
        mutated('wrong final archive rejects', lambda r: r.update(final_archive='LM_READERS_EN.zip'))
        mutated('wrong final publication path rejects', lambda r: r.update(final_path='LM_EN_reading.pdf'))
        reject('live publication path cannot be substituted for preserved path', lambda: module.validate_snapshot_publication_pdf(ROOT, row['source_scope_qualification']['original_path'], row, {}))
        q = row['source_scope_qualification']; snap = read(ROOT / q['snapshot']['path'])
        cache_key = (q['snapshot']['path'], q['snapshot']['sha256'], q['snapshot']['bytes'])
        for label, action in (
            ('non-discovery snapshot schema rejects', lambda d: d.update(schema='other')),
            ('incomplete snapshot status rejects', lambda d: d.update(status='PENDING')),
            ('snapshot observation-generation claim rejects', lambda d: d.update(observations_generated_by_script=True)),
            ('snapshot publication-closure claim rejects', lambda d: d.update(publication_closure_claim=True)),
            ('missing whole-book inventory row rejects', lambda d: d['pdfs'].pop()),
            ('duplicate whole-book identity rejects', lambda d: d['pdfs'].__setitem__(1, copy.deepcopy(d['pdfs'][0]))),
        ):
            changed = copy.deepcopy(snap); action(changed)
            reject(label, lambda changed=changed: module.validate_snapshot_publication_pdf(ROOT, name, row, {cache_key: changed}))

        # Exercise the existing registry/exclude code against only the new
        # scoped catalog, without replacing the active registry on disk.
        old_json = module.json
        active_text = (ROOT / 'work/data/development_pdf_exclusions.json').read_text()
        module.json = types.SimpleNamespace(loads=lambda text: additions if text == active_text else json.loads(text))
        try:
            joined = module.registry(ROOT, books)
            assert len(joined) == 7
            for name, value in books.items():
                assert joined[(name, value['source_pdf_sha256'], value['source_pdf_bytes'])]['reader'] == value['reader']
            passed('new registry branch admits exactly seven scoped snapshot rows in an isolated catalog view')
            source = {name: (ROOT / name, 'preserved historical publication') for name in books}
            omitted = module.exclude(source, ROOT, lambda path: path.read_bytes())
            assert source == {} and len(omitted) == 7
            passed('unchanged exclude consumer removes only exact seven snapshot PDFs from the scoped records map')
            unknown = {'work/data/unknown_historical_book.pdf': (b'%PDF-1.4\nunknown\n', 'negative fixture')}
            reject('unknown work-data PDF remains rejected', lambda: module.exclude(unknown, ROOT, lambda path: path.read_bytes()))
        finally:
            module.json = old_json

        for item in read(STAGE / 'BEFORE.json')['files']:
            exact(dict(path=item['active_path'], bytes=item['bytes'], sha256=item['sha256']))
        assert not any(n.startswith('work/build/') and n.lower().endswith('.pdf') for n in READS)
        passed('all active before files exact and zero live publication PDF reads or hashes')
        checked_paths = [Path(__file__), STAGE / 'prepare_dispositions.py', STAGE / 'snapshot_publication_validator.py',
                         STAGE / 'CHANGE.json', STAGE / 'ADDITIONS.json', STAGE / 'QUALIFICATION.json',
                         STAGE / 'proposed/publication_pdf_scope.py', STAGE / 'proposed/development_pdf_exclusions.json']
        report = dict(schema='revision878-pdf-disposition-boundary-controls-v1', status='PASS',
            passed=len(results), failed=0, controls=results, checked_files=[pin(p) for p in checked_paths],
            current_publication_pdf_reads_or_hashes=0, existing894_rows_preserved=True,
            final_privacy_audit_run=False, new_numerical_or_visual_approval_claim=False,
            active_files_changed=False, tests_limited_to_scoped_metadata_and_preserved_development_bytes=True)
    finally:
        Path.read_bytes, Path.read_text = original_read_bytes, original_read_text
    with (STAGE / 'CONTROLS.json').open('x') as stream:
        json.dump(report, stream, ensure_ascii=False, indent=2); stream.write('\n')
    print(json.dumps(dict(status='PASS', controls=report['passed'], report=pin(STAGE / 'CONTROLS.json'))))


if __name__ == '__main__':
    main()
