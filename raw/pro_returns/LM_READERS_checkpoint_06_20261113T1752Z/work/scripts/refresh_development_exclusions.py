#!/usr/bin/env python3
"""Refresh publication-scope replacement mappings for development PDFs.

This reads only development files and records. It never opens a publication
PDF and never infers successful numerical or visual validation for a new
development file from an earlier file with the same name.
"""
from __future__ import annotations

import collections
import csv
import hashlib
import json
import re
from pathlib import Path

from package_release import BOOKS, common_items

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / 'work/data/development_pdf_exclusions.json'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def language_from_name(path):
    name = str(path).lower()
    found = []
    for language in ('fr', 'en'):
        if re.search(r'(?:^|[_/.-])' + language + r'(?:[_/.-]|$)', name):
            found.append(language)
    return found


def target(language, curated, requires_cancelled):
    if language == 'en':
        return {'final_archive': 'LM_READERS_EN.zip',
                'final_path': 'LM_EN_corrected_apparatus.pdf' if curated else 'LM_EN_reading.pdf'}
    return {'final_archive': 'LM_READERS_FR.zip',
            'final_path': ('LM_FR_diplomatique.pdf' if requires_cancelled else
                           'LM_FR_corrige_apparat.pdf' if curated else 'LM_FR_texte_de_lecture.pdf')}


def main():
    previous = json.loads(OUTPUT.read_text()) if OUTPUT.exists() else {}
    initial_paths = set(previous)
    with (ROOT / 'work/records/VISUAL_REPAIRS.tsv').open(newline='') as stream:
        visual = list(csv.DictReader(stream, delimiter='\t'))
    inventory = json.loads((ROOT / 'work/data/visual_repair_proof_inventory.json').read_text())
    by_path = collections.defaultdict(list)
    by_hash = collections.defaultdict(list)
    for row in visual:
        by_path[row['probe_pdf']].append(row)
        by_hash[row['probe_pdf_sha256']].append(row)
    for row in inventory:
        related = by_path.get(row.get('historical_checkpoint_pdf', ''), [])
        if related:
            by_path[row['original_pdf']].extend(related)
    mapped = {name: path for name, (path, _) in common_items(False, True, True).items()
              if Path(name).suffix.lower() == '.pdf' and Path(name).stem not in BOOKS}
    added, refreshed = [], []
    for name, path in sorted(mapped.items()):
        current_hash = digest(path)
        old = previous.get(name, {})
        # Preserve an original audited hash and wording as historical evidence;
        # the current path-level replacement reason makes no numerical claim.
        history = list(old.get('historical_versions', []))
        if old.get('source_pdf_sha256') and old['source_pdf_sha256'] != current_hash:
            witness = {'sha256': old['source_pdf_sha256'], 'reason': old.get('reason', '')}
            if witness not in history:
                history.append(witness)
        related = by_path.get(name, []) or by_hash.get(current_hash, [])
        curated = name.startswith(('proofs/visual_repairs/', 'work/visual_repair_proofs/'))
        languages = sorted({r['language'] for r in related if r.get('language')})
        language_basis = 'Exact curated proof record or identical proof-PDF hash'
        if not languages:
            languages = old.get('languages') or language_from_name(name)
            language_basis = 'Existing qualified mapping or explicit language token in the filename'
        if not languages:
            tex = path.with_suffix('.tex')
            source = tex.read_text(errors='replace') if tex.exists() else ''
            if re.search(r'\\usepackage\[english\]\{babel\}|\\selectlanguage\{english\}|_en\.tex', source):
                languages = ['en']
                language_basis = 'Associated TeX explicitly selects English or an English source package'
            elif re.search(r'\\usepackage\[french\]\{babel\}|\\selectlanguage\{french\}|fr/texts/', source):
                languages = ['fr']
                language_basis = 'Associated TeX explicitly selects French or a French source package'
        if not languages:
            # A language-neutral geometric/font diagnostic is replaced by
            # both completed language readers, without guessing its language.
            languages = ['fr', 'en']
            language_basis = 'Language-neutral or unqualified development diagnostic; both final language readers are indicated'
        scans = sorted({r['cote'] + ':' + str(r.get('affected_scan') or r['source_scan'])
                        for r in related if r.get('cote')}) or old.get('cote_scans', [])
        pngs = sorted({r['probe_image'] for r in related if r.get('probe_image')}) or old.get('evidence_pngs', [])
        cancelled = any('cancelled' in (r.get('before_issue', '') + ' ' + r.get('exact_action', '')).lower()
                        for r in related)
        targets = [target(language, curated, cancelled and language == 'fr') for language in languages]
        reason = (
            'Curated source-local proof PDF superseded as a publication deliverable by the completed full-book edition. '
            if curated else
            'Completed full-book edition replaces this development extract or diagnostic as a publication deliverable. '
        ) + (
            'FINAL contains exactly seven publication PDFs. Associated PNG evidence, TeX, logs and hash provenance '
            'remain in the records when available; historical checkpoint bytes remain recoverable. This is a '
            'publication-scope exclusion because the development document is not the certified current full edition. '
            'It is not an assertion of a numerical failure, and no numerical pass is inferred from an older file name.'
        )
        record = dict(old, reason=reason, **targets[0], source_pdf_sha256=current_hash,
                      curated_proof=curated, curated_evidence_duplicate=bool(related) and not curated,
                      languages=languages, language_qualification=language_basis,
                      cote_scans=scans, evidence_pngs=pngs, additional_final_targets=targets[1:])
        if old.get('reason') and 'zero compile errors' in old['reason']:
            record['earlier_numerical_audit'] = {
                'path': 'work/data/development_pdf_audit.json',
                'audited_pdf_sha256': old.get('source_pdf_sha256'),
                'scope': 'Original 104-path snapshot only; consult its recorded file hash and measurements.'}
        if history:
            record['historical_versions'] = history
        previous[name] = record
        (refreshed if name in initial_paths else added).append(name)
    if not initial_paths.issubset(previous):
        raise RuntimeError('An existing historical exclusion mapping was dropped.')
    OUTPUT.write_text(json.dumps(dict(sorted(previous.items())), ensure_ascii=False, indent=2) + '\n')
    summary = {'status': 'COMPLETE_PUBLICATION_SCOPE_MAPPING', 'total_paths': len(previous),
               'previous_paths_preserved': len(initial_paths), 'new_paths': len(added),
               'currently_mapped_development_pdf_paths': len(mapped),
               'added': added, 'refreshed': refreshed,
               'original_numerical_audit': 'work/data/development_pdf_audit.json',
               'original_numerical_audit_scope': '104 historical path instances; unchanged by this mapping refresh.',
               'publication_pdfs_opened': 0}
    (ROOT / 'work/data/development_pdf_exclusions_refresh.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({key: summary[key] for key in ('status', 'total_paths', 'previous_paths_preserved', 'new_paths', 'publication_pdfs_opened')}))


if __name__ == '__main__':
    main()
