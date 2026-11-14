#!/usr/bin/env python3
"""Focused fixed-snapshot admission controls; no PDF reads or reconstruction."""
from pathlib import Path
import ast
import copy
import hashlib
import importlib.util
import json
import types

ROOT = Path.cwd().resolve()
STAGE = Path(__file__).resolve().parent


def pin(path):
    data = path.read_bytes()
    return {'path': path.relative_to(ROOT).as_posix(), 'bytes': len(data),
            'sha256': hashlib.sha256(data).hexdigest()}


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    assert STAGE == ROOT / 'work/records/revision878_snapshot_book_authority_staged_v1'
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

    before = load('snapshot_authority_before', STAGE / 'before/restore_checkpoint.py')
    after = load('snapshot_authority_after', STAGE / 'proposed/restore_checkpoint.py')
    declaration = json.loads((STAGE / 'SNAPSHOT_AUTHORITY.json').read_text())
    assert declaration == after.SNAPSHOT_PUBLICATION_AUTHORITY

    def functions(path):
        return {node.name: ast.dump(node, include_attributes=False)
                for node in ast.parse(path.read_text()).body
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))}

    old_defs = functions(STAGE / 'before/restore_checkpoint.py')
    new_defs = functions(STAGE / 'proposed/restore_checkpoint.py')
    assert new_defs.keys() - old_defs.keys() == {'validate_snapshot_publication_authority'}
    assert not old_defs.keys() - new_defs.keys()
    assert [name for name in old_defs if old_defs[name] != new_defs[name]] == ['validate_pdf_delta_logical_scope']
    assert before.PDF_DELTA_MAX_TARGETS == after.PDF_DELTA_MAX_TARGETS == 23
    assert before.PDF_DELTA_MAX_BYTES == after.PDF_DELTA_MAX_BYTES == 67108864
    passed('Only one closed validator is added and the existing delta-authority join changes; all codecs, PNGs and bounds remain exact')
    old_pack = functions(STAGE / 'before/package_release.py')
    new_pack = functions(STAGE / 'proposed/package_release.py')
    assert old_pack.keys() == new_pack.keys()
    assert [name for name in old_pack if old_pack[name] != new_pack[name]] == ['make_compact_zip']
    assert (ROOT / 'work/scripts/checkpoint_pdf_deltas.py').read_bytes() == (STAGE / 'before/checkpoint_pdf_deltas.py').read_bytes()
    passed('The qualifier remains byte-exact and only compact package authority/descriptor wiring changes')

    metadata = {}
    logical = {}

    def add_metadata(name):
        content = (ROOT / name).read_bytes()
        assert not name.lower().endswith('.pdf')
        metadata[name] = content
        logical[name] = {'path': name, 'bytes': len(content), 'sha256': after.digest(content), 'storage_kind': 'blob'}
        return json.loads(content)

    snapshot = add_metadata(declaration['snapshot']['logical_path'])
    for field in ('captured_stable', 'captured_build', 'captured_source_freeze'):
        add_metadata(declaration[field]['logical_path'])
    build = json.loads(metadata[declaration['captured_build']['logical_path']])
    captures = {row['original_path']: row for row in snapshot['files']}
    for field in ('source_dependencies', 'assembly_dependencies'):
        for original in build[field]:
            row = captures[original]
            name = row['snapshot_path']
            content = (ROOT / name).read_bytes()
            assert not name.lower().endswith('.pdf')
            metadata[name] = content
            logical[name] = {'path': name, 'bytes': len(content), 'sha256': after.digest(content), 'storage_kind': 'blob'}
    for row in declaration['pdfs']:
        logical[row['preserved_path']] = {'path': row['preserved_path'], 'bytes': row['bytes'],
                                         'sha256': row['sha256'], 'storage_kind': 'blob'}
    read_names = []

    def read(name):
        assert not name.lower().endswith('.pdf'), 'This control must not read a PDF.'
        read_names.append(name)
        return metadata[name]

    result = after.validate_snapshot_publication_authority(logical, read, declaration)
    expected = [{'reader': row['reader'], 'logical_path': row['preserved_path'],
                 'sha256': row['sha256'], 'bytes': row['bytes']} for row in declaration['pdfs']]
    assert result == expected and len(result) == 7
    assert len(set(read_names)) == 20
    passed('Actual fixed snapshot plus20 exact metadata files authorizes precisely the seven known historical PDF pins without reading PDFs')
    calls = []
    assert after.validate_snapshot_publication_authority({}, lambda name: calls.append(name), None) == []
    assert calls == []
    passed('Old archives with no declaration acquire no new authority or metadata reads')

    for label, mutate in [
        ('unregistered snapshot path', lambda d: d['snapshot'].update(logical_path='work/data/unregistered_snapshot.json')),
        ('wrong snapshot digest', lambda d: d['snapshot'].update(sha256='0' * 64)),
        ('wrong snapshot byte length', lambda d: d['snapshot'].update(bytes=d['snapshot']['bytes'] + 1)),
        ('different revision', lambda d: d.update(revision=878)),
        ('different named reader', lambda d: d['pdfs'][0].update(reader='LM_EN_reading')),
        ('different preserved PDF path', lambda d: d['pdfs'][0].update(preserved_path='work/data/other_book.pdf')),
        ('wrong fixed PDF digest', lambda d: d['pdfs'][0].update(sha256='0' * 64)),
        ('wrong fixed PDF byte length', lambda d: d['pdfs'][0].update(bytes=d['pdfs'][0]['bytes'] + 1)),
        ('duplicate or extra book row', lambda d: d['pdfs'].append(copy.deepcopy(d['pdfs'][0]))),
        ('integer replacing false review claim', lambda d: d.update(new_visual_review_claims=0)),
        ('unexpected declaration field', lambda d: d.update(extra=True)),
    ]:
        bad = copy.deepcopy(declaration); mutate(bad)
        rejected('Reject ' + label + ' before source reads', lambda bad=bad: after.validate_snapshot_publication_authority(
            logical, lambda name: (_ for _ in ()).throw(AssertionError('Unexpected read.')), bad))

    for label, name, field, value in [
        ('snapshot logical hash mismatch', declaration['snapshot']['logical_path'], 'sha256', '0' * 64),
        ('snapshot logical size mismatch', declaration['snapshot']['logical_path'], 'bytes', 1),
        ('metadata disguised as PNG recipe', declaration['captured_stable']['logical_path'], 'storage_kind', 'png_recipe'),
        ('PDF logical digest mismatch', declaration['pdfs'][0]['preserved_path'], 'sha256', '0' * 64),
        ('PDF logical size mismatch', declaration['pdfs'][0]['preserved_path'], 'bytes', 1),
        ('PDF logical path mismatch', declaration['pdfs'][0]['preserved_path'], 'path', 'work/data/wrong.pdf'),
        ('PDF disguised as PNG recipe', declaration['pdfs'][0]['preserved_path'], 'storage_kind', 'png_recipe'),
    ]:
        bad = copy.deepcopy(logical); bad[name][field] = value
        rejected('Reject ' + label, lambda bad=bad: after.validate_snapshot_publication_authority(bad, read, declaration))
    for label, name in [('snapshot', declaration['snapshot']['logical_path']),
                        ('captured stable', declaration['captured_stable']['logical_path']),
                        ('captured source freeze', declaration['captured_source_freeze']['logical_path'])]:
        rejected('Reject changed ' + label + ' bytes despite unchanged metadata',
                 lambda name=name: after.validate_snapshot_publication_authority(logical,
                     lambda n: read(n) + b' ' if n == name else read(n), declaration))
    source_name = captures[next(iter(build['source_dependencies']))]['snapshot_path']
    for label, name in [('captured source dependency', source_name),
                        ('historical PDF', declaration['pdfs'][0]['preserved_path'])]:
        bad = copy.deepcopy(logical); bad.pop(name)
        rejected('Reject missing exact ' + label, lambda bad=bad: after.validate_snapshot_publication_authority(bad, read, declaration))

    # This is a metadata-only view of one planned target. The unchanged codec
    # and full CompactArchive restoration are not executed by these controls.
    target = declaration['pdfs'][0]
    reader = target['reader']; base_sha = after.digest(b'synthetic current878 primitive metadata only')
    base_path = 'work/build/' + reader + '.pdf'; rid = 'pdf-delta-' + target['sha256']
    catalog_logical = copy.deepcopy(logical)
    catalog_logical[target['preserved_path']].update(storage_kind='pdf_delta', recipe_id=rid)
    catalog_logical[base_path] = {'path': base_path, 'bytes': 1000, 'sha256': base_sha, 'storage_kind': 'blob'}
    recipe = {'base_reader': reader, 'base_sha256': base_sha, 'target_reader': reader, 'target_sha256': target['sha256']}
    descriptor = {'source_pdfs': [{'reader': reader, 'logical_path': base_path, 'bytes': 1000, 'sha256': base_sha}],
                  'snapshot_publication_book_authority': declaration}
    archive = types.SimpleNamespace(logical=catalog_logical, descriptor=descriptor, pdf_deltas={rid: recipe}, logical_bytes=read)
    rejected('Old restorer authority gate rejects the exact snapshot-only target', lambda: before.validate_pdf_delta_logical_scope(archive))
    after.validate_pdf_delta_logical_scope(archive)
    passed('New restorer joins the same target only through its full fixed snapshot authority')
    missing = types.SimpleNamespace(logical=catalog_logical, descriptor={'source_pdfs': descriptor['source_pdfs']},
                                    pdf_deltas={rid: recipe}, logical_bytes=read)
    rejected('New restorer still rejects the target if the explicit authority block is omitted', lambda: after.validate_pdf_delta_logical_scope(missing))
    inherited = copy.deepcopy(missing.descriptor)
    inherited['inherited_recovery_inputs'] = [{'kind': 'source_pdf', 'reader': reader,
        'path': target['preserved_path'], 'logical_path_at_capture': 'work/build/' + reader + '.pdf',
        'sha256': target['sha256'], 'bytes': target['bytes']}]
    original_route = types.SimpleNamespace(logical=catalog_logical, descriptor=inherited,
        pdf_deltas={rid: recipe}, logical_bytes=lambda name: (_ for _ in ()).throw(AssertionError('No snapshot read expected.')))
    before.validate_pdf_delta_logical_scope(original_route)
    after.validate_pdf_delta_logical_scope(original_route)
    passed('Existing current/inherited named-book admission remains identical and performs no new snapshot reads')
    package = (STAGE / 'proposed/package_release.py').read_text()
    assert package.index('snapshot_pdf_books=recovery.validate_snapshot_publication_authority(') < package.index('pdf_delta.qualify(') < package.index('documents[book]=fitz.open(')
    assert 'pdf_delta.book_authorities(entries,inherited)+snapshot_pdf_books' in package
    assert "descriptor['snapshot_publication_book_authority']=snapshot_pdf_authority" in package
    passed('Package validates the closed join before delta generation/rendering and persists the same standalone authority block')
    output = {'schema': 'fixed872-snapshot-book-authority-controls-v1', 'status': 'PASS_STAGED_METADATA_ADMISSION_ONLY',
        'passed': len(checks), 'failed': 0, 'checks': checks,
        'checked_files': [pin(Path(__file__)), pin(STAGE / 'SNAPSHOT_AUTHORITY.json'), pin(STAGE / 'authority_fragment.py')] +
            [pin(STAGE / folder / name) for folder, names in [('before', ['restore_checkpoint.py','package_release.py','checkpoint_pdf_deltas.py']),
             ('proposed', ['restore_checkpoint.py','package_release.py'])] for name in names],
        'actual_metadata_inputs': [pin(ROOT / name) for name in sorted(metadata)],
        'exact_snapshot_PDF_pin_count': 7, 'actual_PDF_bytes_read': 0,
        'generation_decoding_rendering_collection_or_restore_executed': False,
        'production_helpers_changed': False, 'new_visual_review_claims': False}
    destination = STAGE / 'CONTROLS.json'
    with destination.open('x') as stream:
        json.dump(output, stream, ensure_ascii=False, indent=2); stream.write('\n')
    print(json.dumps(pin(destination), indent=2))


if __name__ == '__main__':
    main()
