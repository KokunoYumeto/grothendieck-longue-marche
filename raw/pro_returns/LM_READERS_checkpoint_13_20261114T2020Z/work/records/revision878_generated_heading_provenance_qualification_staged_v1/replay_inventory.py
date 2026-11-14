"""Replay the unchanged occurrence recorder into this isolated evidence stage.

Only the recorder's DATA destination is redirected.  No reader is rebuilt and
no existing source, inventory, review, PDF, or gate record may be written.
"""
from pathlib import Path
import ast
import collections
import contextlib
import csv
import hashlib
import importlib.util
import io
import json
import os
import sys

STAGE = Path(__file__).resolve().parent
ROOT = STAGE.parents[2]
REPLAY = STAGE / 'replay'
INVENTORY = ROOT / 'work/data/generated_heading_repairs.json'
GENERATOR = ROOT / 'work/scripts/record_generated_heading_repairs.py'
PROVENANCES = {'work/build/fr_provenance.json', 'work/build/en_provenance.json'}


def pin(path):
    path = Path(path)
    data = path.read_bytes()
    return dict(path=path.relative_to(ROOT).as_posix(), bytes=len(data),
                sha256=hashlib.sha256(data).hexdigest())


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True,
                      separators=(',', ':')).encode()


def main():
    assert Path.cwd().resolve() == ROOT
    assert not (REPLAY / 'generated_heading_repairs.json').exists()
    assert not (STAGE / 'REPLAY_RESULT.json').exists()
    assert GENERATOR.read_bytes() == (STAGE / 'preserved/record_generated_heading_repairs.py').read_bytes()
    assert (REPLAY / 'note_heading_probe.json').read_bytes() == (ROOT / 'work/data/note_heading_probe.json').read_bytes()

    scripts = ['record_generated_heading_repairs.py', 'build_readers.py',
               'editorial.py', 'mechanical_repairs.py', 'texenv.py']
    names = {'work/scripts/' + name for name in scripts}
    names |= {'work/scripts/book_preamble.tex',
              'sources/fr/records/CURRENT_TEXT_INDEX.tsv',
              'work/data/frontmatter.json', 'work/data/glossary_edits.json',
              'work/data/note_heading_probe.json',
              'work/records/MARGINAL_NOTE_CONTEXTS.tsv',
              'work/layout_probes/apparatus_heading_candidate.json',
              'work/layout_probes/retained_heading_candidate.json',
              'work/layout_probes/range_heading_candidate.json',
              'work/layout_probes/range134_heading_candidate.json',
              'work/layout_probes/revision864_root_probes_v1/range077_candidate.json',
              'work/data/generated_heading_repairs.json',
              'work/data/final_build_inputs.json',
              'work/data/layout_release_checkpoint.json',
              'work/data/revision878_final_review/STABLE_BUILD.json'} | PROVENANCES
    index_path = ROOT / 'sources/fr/records/CURRENT_TEXT_INDEX.tsv'
    with index_path.open() as stream:
        index = list(csv.DictReader(stream, delimiter='\t'))
    assert len(index) == 116
    for row in index:
        package = row['package']
        names.add('sources/fr/texts/' + package + '.tex')
        names.add('sources/en/packages/' + package + '_en.tex')
    books = ['LM_FR_diplomatique', 'LM_FR_corrige_apparat',
             'LM_FR_texte_de_lecture', 'LM_EN_corrected_apparatus',
             'LM_EN_reading', 'LM_FR_master_annotated', 'LM_EN_master_annotated']
    names |= {'work/build/' + book + '.tex' for book in books}
    before = {name: pin(ROOT / name) for name in sorted(names)}
    stable = json.loads((ROOT / 'work/data/revision878_final_review/STABLE_BUILD.json').read_text())
    build = json.loads((ROOT / 'work/data/final_build_inputs.json').read_text())
    assert stable['source_records'] == build['source_records'] == 878
    assert stable['build_record'] == before['work/data/final_build_inputs.json']
    assert build['status'] == 'TWO_PASS_BUILD_COMPLETE_INPUTS_UNCHANGED'
    assert build['changed_inputs'] == [] and build['return_code'] == 0
    assert len(stable['books']) == len({r['book'] for r in stable['books']}) == 7
    assert {r['book'] for r in stable['books']} == set(books)
    for row in stable['books']:
        actual = before['work/build/' + row['book'] + '.tex']
        assert actual['sha256'] == row['tex_sha256'] and actual['bytes'] == row['tex_bytes']
    for name, digest in build['assembly_dependencies'].items():
        if name in before:
            assert before[name]['sha256'] == digest

    observed_reads = set()
    observed_writes = []
    output = REPLAY / 'generated_heading_repairs.json'
    allowed_read_paths = {(ROOT / name).resolve() for name in names}
    allowed_read_paths.add((REPLAY / 'note_heading_probe.json').resolve())

    def audit(event, args):
        if event != 'open' or not isinstance(args[0], (str, bytes, os.PathLike)):
            return
        path = Path(os.fsdecode(args[0])).resolve()
        mode, flags = args[1], args[2]
        writing = (isinstance(mode, str) and any(x in mode for x in 'wax+')) or (
            isinstance(flags, int) and bool(flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC)))
        if writing:
            assert path == output, 'The recorder attempted a write outside its isolated output'
            observed_writes.append(path.relative_to(ROOT).as_posix())
        elif path.is_relative_to(ROOT):
            # Python may check an existing bytecode cache; no cache is written.
            if path.suffix == '.pyc':
                return
            assert path in allowed_read_paths, 'The recorder read an undeclared project input'
            observed_reads.add(path.relative_to(ROOT).as_posix())

    sys.dont_write_bytecode = True
    sys.path.insert(0, str(ROOT / 'work/scripts'))
    # The hook exists only in this child process.  Remove its enforcement after
    # the unchanged generator returns by using an explicit local phase flag.
    phase = {'recording': True}
    def scoped_audit(event, args):
        if phase['recording']:
            audit(event, args)
    sys.addaudithook(scoped_audit)
    spec = importlib.util.spec_from_file_location('isolated_generated_heading_recorder', GENERATOR)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    assert module.ROOT == ROOT and module.WORK == ROOT / 'work'
    assert module.SCRIPTS == ROOT / 'work/scripts'
    module.DATA = REPLAY
    stdout = io.StringIO()
    with contextlib.redirect_stdout(stdout):
        module.main()
    phase['recording'] = False
    assert observed_writes == [output.relative_to(ROOT).as_posix()]
    after = {name: pin(ROOT / name) for name in sorted(names)}
    assert before == after, 'A current input changed during the isolated replay'

    old = json.loads(INVENTORY.read_text())
    new = json.loads(output.read_text())
    old_dependencies = {r['path']: r for r in old['dependencies']}
    new_dependencies = {r['path']: r for r in new['dependencies']}
    expected = {'work/scripts/book_preamble.tex', 'work/scripts/build_readers.py',
                'work/records/MARGINAL_NOTE_CONTEXTS.tsv'} | PROVENANCES
    assert len(old['dependencies']) == len(new['dependencies']) == 5
    assert set(old_dependencies) == set(new_dependencies) == expected
    changed = [name for name in old_dependencies if old_dependencies[name] != new_dependencies[name]]
    assert set(changed) == PROVENANCES
    assert [r['path'] for r in old['dependencies']] == [r['path'] for r in new['dependencies']]
    for name, row in new_dependencies.items():
        assert set(row) == {'path', 'sha256'}
        assert row['sha256'] == before[name]['sha256']
    old_non = {k: v for k, v in old.items() if k != 'dependencies'}
    new_non = {k: v for k, v in new.items() if k != 'dependencies'}
    assert old_non == new_non, 'The current occurrence semantics differ from the preserved inventory'
    assert old['rows'] == new['rows'] and len(new['rows']) == 21648
    identities = [(r['reader'], r['id']) for r in new['rows']]
    assert len(identities) == len(set(identities))
    for row in new['rows']:
        assert row['record_basis'] == 'generated heading pagination'
    assert new['visual_review_claim'] is False and new['source_readings_changed'] is False
    result = dict(
        schema='revision878-generated-heading-provenance-replay-v1',
        status='PASS_EXACT_OCCURRENCE_REPLAY_ONLY_TWO_DEPENDENCY_IDENTITIES_CHANGED',
        source_records=878, canonical_inventory=before['work/data/generated_heading_repairs.json'],
        unchanged_recorder=before['work/scripts/record_generated_heading_repairs.py'],
        recorder_preserved_copy=pin(STAGE / 'preserved/record_generated_heading_repairs.py'),
        isolated_replayed_inventory=pin(output),
        exact_note_probe_copy=pin(REPLAY / 'note_heading_probe.json'),
        original_note_probe=before['work/data/note_heading_probe.json'],
        stable_build=before['work/data/revision878_final_review/STABLE_BUILD.json'],
        current_build=before['work/data/final_build_inputs.json'],
        input_identities=list(before.values()),
        all_inputs_unchanged_after_replay=True,
        observed_project_reads=sorted(observed_reads),
        observed_recorder_writes=observed_writes,
        rows=21648, rows_and_order_exact=True,
        row_identity_count=len(set(identities)),
        category_counts=new['counts'],
        row_sequence_sha256=hashlib.sha256(canonical(new['rows'])).hexdigest(),
        all_nondependency_fields_exact=True,
        nondependency_fields_sha256=hashlib.sha256(canonical(new_non)).hexdigest(),
        dependency_order_exact=True,
        dependency_changes=[dict(path=name, recorded=old_dependencies[name],
                                 current=new_dependencies[name], current_file=before[name]) for name in changed],
        unchanged_dependency_paths=sorted(expected - PROVENANCES),
        stdout_summary=json.loads(stdout.getvalue()),
        canonical_inventory_modified=False, current_source_or_review_modified=False,
        publication_PDF_bytes_read=False, source_build_or_compile_performed=False,
        queue_or_inventory_regenerated_in_canonical_location=False,
        visual_review_claim=False, current_publication_approval_claim=False,
        old_provenance_full_bytes_verified_by_this_replay=False,
        qualification_scope='The preserved occurrence rows retain their original full-file dependency identities. This replay separately proves their exact current applicability from current878 inputs; it does not relabel historical provenance bytes as current.'
    )
    result_path = STAGE / 'REPLAY_RESULT.json'
    result_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k: result[k] for k in ('status', 'rows', 'category_counts', 'dependency_changes')}))


if __name__ == '__main__':
    main()
