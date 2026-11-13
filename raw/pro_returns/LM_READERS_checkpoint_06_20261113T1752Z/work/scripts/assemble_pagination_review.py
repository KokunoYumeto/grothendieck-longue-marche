#!/usr/bin/env python3
"""Collate supplied observations from actual pre-repair page-pair inspections.

This does not inspect images or manufacture review decisions. Every observation
must already exist, cover a unique scanner candidate, and match its saved image.
"""
from pathlib import Path
import collections
import csv
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / 'work/data'
REC = ROOT / 'work/records'
SOURCES = [
    ('equation_tag_pagination_original_reviewed.json', 'root'),
    ('glossary_expanded_pagination_reviewed.json', 'glossary'),
    ('fr_app_expanded_pagination_observations.json', 'editorial'),
    ('en_reading_expanded_pagination_observations.json', 'root'),
    ('en_app_expanded_pagination_editorial_observations.json', 'editorial'),
    ('en_app_expanded_pagination_root_observations.json', 'root'),
]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def key(row):
    return row['reader'], int(row['page']), row['tag']


def main():
    scan = json.loads((DATA / 'equation_tag_pagination_expanded.json').read_text())
    pdf_hashes = {r['reader']: r['sha256'] for r in scan['files']}
    candidates = {key(r): r for r in scan['candidates'] if 'master' not in r['reader']}
    reviewed = {}
    for name, reviewer in SOURCES:
        data = json.loads((DATA / name).read_text())
        rows = data.get('candidates', list(data.values())) if isinstance(data, dict) else data
        for row in rows:
            k = key(row)
            if k in reviewed:
                raise ValueError('Duplicate review: ' + str(k))
            if k not in candidates:
                raise ValueError('Review not in scanner inventory: ' + str(k))
            status = row.get('status') or row.get('inspection_status', '')
            if status in {'CONFIRMED_ORPHAN', 'CONFIRMED_DETACHED_TAG'}:
                decision = 'confirmed detached tag'
            elif status in {'VISUALLY_CLEARED', 'CLEARED_SAME_PAGE_DISPLAY', 'CLEAR_SAME_PAGE_DISPLAY', 'CLEARED'}:
                decision = 'visually cleared'
            else:
                raise ValueError('Unrecognised review status: ' + status)
            image = row['native_pair_image']
            expected = row.get('native_pair_image_sha256', row.get('native_pair_sha256'))
            if not expected or digest(ROOT / image) != expected:
                raise ValueError('Review image is missing or changed: ' + image)
            observation = row.get('observation', row.get('observations'))
            if not observation:
                raise ValueError('Actual observation missing: ' + str(k))
            source = row.get('source', row.get('confirmed_source', {}))
            source_cote = row.get('source_cote', source.get('cote', ''))
            source_scan = row.get('source_scan', source.get('scan', ''))
            source_package = row.get('source_package', source.get('package', ''))
            source_line = row.get('source_line', source.get('source_line', ''))
            reviewed[k] = dict(row,
                decision=decision, reviewer=row.get('reviewer', reviewer),
                historical_pdf_sha256=pdf_hashes[row['reader']],
                native_pair_image_sha256=expected,
                final_archive='LM_READERS_RECORDS.zip',
                final_archive_image=image.replace('work/visual_repair_proofs/', 'proofs/visual_repairs/', 1),
                observation_record='work/data/' + name,
                source_cote=source_cote, source_scan=source_scan,
                source_package=source_package, source_line=source_line,
                observation=observation,
            )
    if set(reviewed) != set(candidates):
        raise ValueError('Candidate coverage mismatch: ' + str(sorted(set(candidates) - set(reviewed))))
    rows = [reviewed[k] for k in sorted(reviewed)]
    counts = collections.Counter(r['decision'] for r in rows)
    report = {
        'status': 'PRE_REPAIR_PRIMARY_REVIEW_COMPLETE',
        'scope': 'All nonmaster candidates in the saved pre-repair scanner output. Actual native page-pair inspections supplied by the named reviewers; no final repaired-page inspection is asserted here.',
        'candidate_count': len(rows), 'decision_counts': dict(counts),
        'historical_pdf_hashes': pdf_hashes,
        'master_candidates': 'The 44 corresponding apparatus-master candidates are duplicates requiring the separately recorded final all-page pixel comparison, not additional claimed human inspections.',
        'observations_generated_by_script': False,
        'candidates': rows,
    }
    (DATA / 'pagination_review_before_repairs.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    fields = ['reader', 'page', 'adjacent_page', 'tag', 'decision', 'reviewer', 'historical_pdf_sha256',
              'source_cote', 'source_scan', 'source_package', 'source_line', 'final_archive',
              'final_archive_image', 'native_pair_image_sha256', 'observation_record', 'observation']
    with (REC / 'PAGINATION_REVIEW_BEFORE.tsv').open('w', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, delimiter='\t', lineterminator='\n', extrasaction='ignore')
        writer.writeheader()
        writer.writerows(rows)
    print(json.dumps({'reviewed_candidates': len(rows), 'decisions': dict(counts)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
