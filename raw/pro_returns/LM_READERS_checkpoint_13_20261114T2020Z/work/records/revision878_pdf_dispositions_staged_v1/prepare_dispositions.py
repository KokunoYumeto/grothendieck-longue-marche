#!/usr/bin/env python3
"""Stage exact additive development-PDF dispositions; never read live PDFs."""
from __future__ import annotations
import ast
import collections
import copy
import csv
import difflib
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import re
import sys

STAGE = Path(__file__).resolve().parent
ROOT = STAGE.parents[2]
SNAPSHOT = 'work/data/audit_history/revision872_final_discovery_v1/SNAPSHOT_COMPLETE.json'
SNAPSHOT_SHA = '5965d5b68af96c8b8066cb761cd6e9f0a5f2d4cb43018c7dccbdcf7f9139f24e'
SPECS = (
    ('revision872_scan027_region_parenthesis_v1', 'trial01_yshift3pt', False, '140-1', 27),
    ('revision872_scan027_region_parenthesis_v1', 'trial02_yshift6pt', True, '140-1', 27),
    ('revision872_scan085_minus1_v1', 'trial01_xshift_minus3pt', False, '140-3', 85),
    ('revision872_scan085_minus1_v1', 'trial02_xshift_minus6pt', True, '140-3', 85),
    ('revision872_scan085_zero_v1', 'trial01_xshift_minus10pt', True, '140-3', 85),
)
BOOKS_BY_FORM = {
    'fr': ['LM_FR_diplomatique', 'LM_FR_corrige_apparat', 'LM_FR_texte_de_lecture'],
    'en': ['LM_EN_corrected_apparatus', 'LM_EN_corrected_apparatus', 'LM_EN_reading'],
}
ACCEPTED_STATUSES = {
    'revision872_scan027_region_parenthesis_v1': 'PASS_ISOLATED_SIX_FORM_PROBE',
    'revision872_scan085_minus1_v1': 'PASS_ISOLATED_SIX_FORM_MINUS_ONE_PROBE',
    'revision872_scan085_zero_v1': 'PASS_ISOLATED_SIX_FORM_ZERO_PROBE',
}
READS = {}


def data(path):
    path = Path(path).resolve()
    name = path.relative_to(ROOT).as_posix()
    if name.startswith('work/build/') and path.suffix.lower() == '.pdf':
        raise ValueError('Reading a rebuilding publication PDF is forbidden.')
    content = path.read_bytes()
    READS[name] = dict(path=name, bytes=len(content), sha256=hashlib.sha256(content).hexdigest())
    return content


def pin(path):
    content = data(path)
    return copy.deepcopy(READS[Path(path).resolve().relative_to(ROOT).as_posix()])


def checked(ref):
    content = data(ROOT / ref['path'])
    assert hashlib.sha256(content).hexdigest() == ref['sha256'], ref['path']
    if 'bytes' in ref:
        assert len(content) == ref['bytes'], ref['path']
    return content


def document(path):
    return json.loads(data(path))


def write(name, value):
    path = STAGE / name
    content = value if isinstance(value, bytes) else (json.dumps(value, ensure_ascii=False, indent=2) + '\n').encode()
    with path.open('xb') as stream:
        stream.write(content)
    return pin(path)


def main():
    assert Path.cwd().resolve() == ROOT
    assert not (STAGE / 'QUALIFICATION.json').exists()
    before = document(STAGE / 'BEFORE.json')
    for row in before['files']:
        original = data(ROOT / row['active_path'])
        assert len(original) == row['bytes'] and hashlib.sha256(original).hexdigest() == row['sha256']
        assert original == data(ROOT / row['preserved_path'])
    baseline_bytes = data(STAGE / 'before/development_pdf_exclusions.json')
    baseline = json.loads(baseline_bytes)
    assert len(baseline) == 894
    visual_rows = list(csv.DictReader(io.StringIO(data(ROOT / 'work/records/VISUAL_REPAIRS.tsv').decode()), delimiter='\t'))
    curated_identities = {(r['probe_pdf'], r['probe_pdf_sha256']) for r in visual_rows}
    additions = {}
    qualifications = []
    for stem, trial, accepted, cote, scan in SPECS:
        directory = ROOT / 'work/layout_probes' / stem
        handoff = document(directory / 'HANDOFF.json')
        compile_path = directory / trial / 'compile_validation.json'
        compiled = document(compile_path)
        assert len(compiled['forms']) == 6
        assert {(f['language'], f['form']) for f in compiled['forms']} == {(l, f) for l in ('fr', 'en') for f in range(3)}
        if accepted:
            validation = json.loads(checked(handoff['validation']))
            assert validation['status'] == ACCEPTED_STATUSES[stem] and validation['actual_after_forms'] == 6
            assert validation['compile_validation']['path'] == compile_path.relative_to(ROOT).as_posix()
            checked(validation['compile_validation'])
            checked(validation['actual_observations'])
            classification = 'ACCEPTED_SOURCE_LOCAL_PROOF_COMPARISON'
            authority = dict(handoff=pin(directory / 'HANDOFF.json'), validation=handoff['validation'],
                             actual_observations=validation['actual_observations'], root_review=pin(directory / 'ROOT_REVIEW.json'))
            reason = ('Accepted isolated before/after label-position comparison, retained as development evidence. '
                      'It is superseded only as a publication document by the named final complete book. '
                      'The local proof acceptance is recorded in the exact validation and root review; this disposition makes no current-publication or full-book visual approval claim.')
        else:
            rejection_path = directory / trial / 'REJECTED.json'
            rejection = document(rejection_path)
            assert rejection['status'] == 'REJECTED_VISUAL_CONTACT_REMAINS'
            assert rejection['compile_validation']['path'] == compile_path.relative_to(ROOT).as_posix()
            checked(rejection['compile_validation'])
            classification = 'REJECTED_SMALLER_SHIFT_TRIAL'
            authority = dict(handoff=pin(directory / 'HANDOFF.json'), rejection=pin(rejection_path),
                             original_rejection_observation=rejection['observation'])
            reason = ('Rejected smaller-shift label-position trial. The exact rejection records a remaining French-apparatus contact; '
                      'it does not claim that the other five compiled forms were visually examined or cleared. '
                      'The named final complete book supersedes this unsuccessful isolated trial only as a publication document; '
                      'the rejection is a geometry finding, not an invented compiler failure.')
        candidate = compiled['candidate']; checked(candidate)
        for index, form in enumerate(compiled['forms']):
            language, number = form['language'], form['form']
            pdf = form['pdf']; tex = form['tex']; log = form['log']
            content = checked(pdf); assert content.startswith(b'%PDF-')
            text = checked(tex).decode(); checked(log)
            assert tex['path'] == str(Path(pdf['path']).with_suffix('.tex'))
            assert re.findall(r'\\newcommand\\LMlanguage\{(fr|en)\}', text) == [language]
            assert re.findall(r'^\\LMform=([012])\s*$', text, re.M) == [str(number)]
            assert all(form[field] == 0 for field in ('compile_exit_code', 'error_count', 'overfull_count', 'missing_character_count'))
            book = BOOKS_BY_FORM[language][number]
            note = reason + ' FINAL contains exactly seven latest publication PDFs. Exact trial PDF bytes remain in numbered checkpoints; associated source, portable logs, observation/rejection records and native PNG evidence remain retained.'
            if language == 'en' and number == 0:
                note += ' There is no separate requested English diplomatic publication; the English corrected apparatus is the named replacement, without asserting form or page identity.'
            name = pdf['path']; assert name not in baseline and name not in additions
            images = [p[k]['path'] for p in form['pages'] for k in ('native', 'full_context')]
            q = dict(kind='source_local_development_proof', classification=classification,
                     source_pdf=pdf, source_tex=tex, portable_log=log,
                     compile_validation=pin(compile_path), form_record_pointer='/forms/' + str(index),
                     candidate=candidate, language=language, form=number, authority=authority)
            additions[name] = dict(path=name, source_pdf_sha256=pdf['sha256'], source_pdf_bytes=pdf['bytes'],
                reader=book, final_archive='LM_READERS_' + language.upper() + '.zip', final_path=book + '.pdf',
                source_scope_qualification=q, reason=note, curated_proof=False,
                curated_evidence_duplicate=(name, pdf['sha256']) in curated_identities, languages=[language],
                language_qualification='Exact compile record and associated TeX language/form declarations, with matching PDF/TeX/portable-log bytes.',
                cote_scans=[cote + ':' + str(scan)], evidence_pngs=images, additional_final_targets=[],
                publication_closure_claim=False)
            qualifications.append(dict(path=name, classification=classification, language=language, form=number,
                pdf=pdf, tex=tex, portable_log=log, compile_record=q['compile_validation'],
                form_record_pointer=q['form_record_pointer'], authority=authority))
    snapshot = document(ROOT / SNAPSHOT)
    assert pin(ROOT / SNAPSHOT)['sha256'] == SNAPSHOT_SHA
    assert snapshot['schema'] == 'audit-revision-snapshot-v1' and snapshot['revision'] == 872
    assert snapshot['status'] == 'COMPLETE_RECORD_SNAPSHOT_NOT_RELEASE_APPROVAL'
    assert snapshot['additive_label'] == 'final_discovery' and snapshot['publication_closure_claim'] is False
    assert len(snapshot['pdfs']) == 7 and len({r['reader'] for r in snapshot['pdfs']}) == 7
    for index, record in enumerate(snapshot['pdfs']):
        book = record['reader']; name = record['preserved_path']
        assert record['path'] == 'work/build/' + book + '.pdf'
        pdf = dict(path=name, bytes=record['bytes'], sha256=record['sha256'])
        checked(pdf)
        assert name not in baseline and name not in additions
        q = dict(kind='immutable_snapshot_publication_pdf', snapshot=pin(ROOT / SNAPSHOT),
                 snapshot_revision=872, snapshot_pdf_index=index, snapshot_pdf_record=copy.deepcopy(record),
                 original_path=record['path'])
        additions[name] = dict(path=name, source_pdf_sha256=pdf['sha256'], source_pdf_bytes=pdf['bytes'],
            reader=book, final_archive='LM_READERS_' + ('FR' if '_FR_' in book else 'EN') + '.zip',
            final_path=book + '.pdf', source_scope_qualification=q,
            reason='Exact complete revision872 book preserved in the immutable final-discovery snapshot, including its historical unresolved findings. It is retained as a superseded development state in numbered checkpoints and excluded from FINAL as a publication document. The named latest complete publication replaces it; no historical-to-final page/pixel identity or current-publication visual approval is asserted. Snapshot, attributed reviews, source and build provenance remain retained. FINAL contains exactly seven latest publication PDFs.',
            publication_closure_claim=False)
        qualifications.append(dict(path=name, classification='SUPERSEDED_SNAPSHOT_PUBLICATION_STATE',
                                   pdf=pdf, snapshot=q['snapshot'], snapshot_pdf_index=index, original_path=record['path']))
    assert len(additions) == 37
    assert sum(r.get('curated_evidence_duplicate', False) for r in additions.values()) == 6
    old = data(STAGE / 'before/publication_pdf_scope.py')
    fragment = data(STAGE / 'snapshot_publication_validator.py')
    marker = b'def registry(root, requested=None):\n'
    assert old.count(marker) == 1
    branch = (b"            elif q.get('kind') == 'immutable_snapshot_publication_pdf':\n"
              b"                validate_snapshot_publication_pdf(root, name, row, snapshot_cache)\n"
              b"                add(name, row['source_pdf_sha256'], row['source_pdf_bytes'], row['reader'], q, row['reason'])\n")
    branch_marker = b"            elif q.get('kind') == 'immutable_snapshot_development_pdf':\n"
    assert old.count(branch_marker) == 1
    proposed_helper = old.replace(marker, fragment + b'\n' + marker, 1).replace(branch_marker, branch + branch_marker, 1)
    ast.parse(proposed_helper)
    helper_ref = write('proposed/publication_pdf_scope.py', proposed_helper)
    # Keep every existing member's literal UTF-8 representation and order.
    close = baseline_bytes.rfind(b'}')
    prefix = baseline_bytes[:close].rstrip(b' \t\r\n')
    tail = json.dumps(additions, ensure_ascii=False, indent=2).encode()[1:-1]
    proposed_bytes = prefix + b',' + tail + baseline_bytes[close:]
    proposed = json.loads(proposed_bytes)
    assert list(proposed) == list(baseline) + list(additions)
    assert all(proposed[k] == v for k, v in baseline.items()) and proposed_bytes.startswith(prefix + b',')
    catalog_ref = write('proposed/development_pdf_exclusions.json', proposed_bytes)
    additions_ref = write('ADDITIONS.json', additions)
    qualification_ref = write('QUALIFICATION.json', dict(
        schema='revision878-additive-development-pdf-dispositions-v1', status='STAGED_EXACT_ADDITIVE_IDENTITIES_NOT_INSTALLED',
        before=pin(STAGE / 'before/development_pdf_exclusions.json'), proposed=catalog_ref,
        prior_rows=894, accepted_trial_pdf_paths=18, rejected_trial_pdf_paths=12, preserved_snapshot_book_paths=7,
        added_rows=37, total_rows=931, old_objects_and_order_exact=True,
        previous_member_text_prefix_bytes=len(prefix), previous_member_text_prefix_sha256=hashlib.sha256(prefix).hexdigest(),
        complete_previous_member_text_prefix_exact=True, snapshot_authority=pin(ROOT / SNAPSHOT),
        evidence=qualifications, read_input_identities=list(READS.values()),
        current_publication_pdfs_read_or_hashed=0, final_privacy_audit_run=False,
        current_publication_visual_or_numerical_approval_claim=False,
        helper_extension='One new strict immutable snapshot whole-book validator and one registry branch; all original functions except the additive registry branch remain byte-exact.'))
    write('CHANGE.json', dict(schema='revision878-snapshot-pdf-disposition-helper-delta-v1',
        before=pin(STAGE / 'before/publication_pdf_scope.py'), proposed=helper_ref,
        new_function=pin(STAGE / 'snapshot_publication_validator.py'),
        diff=''.join(difflib.unified_diff(old.decode().splitlines(True), proposed_helper.decode().splitlines(True),
             fromfile='before/publication_pdf_scope.py', tofile='proposed/publication_pdf_scope.py')),
        old_snapshot_development_validator_unchanged=True, publication_pdf_bytes_read_only_at_preserved_paths=True))
    for row in before['files']:
        assert pin(ROOT / row['active_path']) == dict(path=row['active_path'], bytes=row['bytes'], sha256=row['sha256'])
    print(json.dumps(dict(status='STAGED', catalog=catalog_ref, helper=helper_ref, qualification=qualification_ref, additions=additions_ref)))


if __name__ == '__main__':
    main()
